# Security Guidelines

This file defines security best practices and requirements for the project.

## Security Philosophy

- **Security by Design**: Think about security from the start
- **Defense in Depth**: Multiple layers of protection
- **Least Privilege**: Minimal access by default
- **Fail Secure**: When errors occur, fail safely
- **Trust No One**: Validate everything

## Critical Security Rules

🔒 **NEVER commit**:

- API keys, tokens, or credentials
- Private keys or certificates
- Database passwords
- OAuth secrets
- Session secrets
- Encryption keys
- `.env` files with real data

## Secrets Management

### Environment Variables

```bash
# .env (NEVER commit - in .gitignore)
DATABASE_URL=postgresql://user:pass@localhost/db
API_KEY=sk_live_abc123
JWT_SECRET=your-secret-key-here
```

```javascript
// Good - use environment variables
const apiKey = process.env.API_KEY;
const dbUrl = process.env.DATABASE_URL;

// Bad - hardcoded secrets
const apiKey = 'sk_live_abc123'; // NEVER DO THIS
```

### .env.example Template

```bash
# .env.example (safe to commit)
DATABASE_URL=postgresql://user:password@localhost/dbname
API_KEY=your_api_key_here
JWT_SECRET=your_jwt_secret_here
```

### Secrets in CI/CD

- Use platform secret managers (GitHub Secrets, AWS Secrets Manager)
- Rotate secrets regularly
- Use different secrets for each environment
- Never log secrets

## Input Validation

### Always Validate User Input

```javascript
// Good - validate and sanitize
function createUser(req, res) {
  const { email, name } = req.body;

  // Validate
  if (!isValidEmail(email)) {
    return res.status(400).json({ error: 'Invalid email format' });
  }

  if (!name || name.length < 2 || name.length > 100) {
    return res.status(400).json({ error: 'Invalid name' });
  }

  // Sanitize
  const sanitizedName = sanitizeString(name);

  // Proceed with validated data
  saveUser({ email, name: sanitizedName });
}

// Bad - no validation
function createUser(req, res) {
  saveUser(req.body); // Dangerous!
}
```

### SQL Injection Prevention

```javascript
// Good - parameterized queries
const user = await db.query(
  'SELECT * FROM users WHERE id = $1',
  [userId]
);

// Bad - string concatenation
const user = await db.query(
  `SELECT * FROM users WHERE id = ${userId}` // SQL injection risk!
);
```

### NoSQL Injection Prevention

```javascript
// Good - strict type checking
const userId = String(req.params.id);
const user = await User.findById(userId);

// Bad - accepting objects
const user = await User.find(req.query); // Can inject $where, $ne, etc.
```

## Authentication & Authorization

### Password Security

```javascript
// Good - hash passwords
const bcrypt = require('bcrypt');
const SALT_ROUNDS = 12;

async function hashPassword(password) {
  return await bcrypt.hash(password, SALT_ROUNDS);
}

async function verifyPassword(password, hash) {
  return await bcrypt.compare(password, hash);
}

// Bad - plain text passwords
function savePassword(password) {
  db.save({ password }); // NEVER DO THIS
}
```

### Password Requirements

- Minimum 8 characters (12+ recommended)
- Mix of upper/lower case, numbers, symbols
- No common passwords (use a password strength library)
- Consider passphrase option for better UX

### JWT (JSON Web Tokens)

```javascript
// Good - secure JWT configuration
const jwt = require('jsonwebtoken');

function generateToken(user) {
  return jwt.sign(
    { userId: user.id, role: user.role },
    process.env.JWT_SECRET,
    {
      expiresIn: '15m', // Short expiration
      issuer: 'your-app',
      audience: 'your-api'
    }
  );
}

// Use refresh tokens for long sessions
function generateRefreshToken(user) {
  return jwt.sign(
    { userId: user.id, type: 'refresh' },
    process.env.REFRESH_SECRET,
    { expiresIn: '7d' }
  );
}
```

### Session Management

- Use secure, HTTP-only cookies
- Implement session timeout
- Regenerate session ID after login
- Clear sessions on logout

```javascript
// Good - secure session config
app.use(session({
  secret: process.env.SESSION_SECRET,
  resave: false,
  saveUninitialized: false,
  cookie: {
    secure: true,      // HTTPS only
    httpOnly: true,    // No JavaScript access
    sameSite: 'strict', // CSRF protection
    maxAge: 3600000    // 1 hour
  }
}));
```

### Authorization

```javascript
// Good - check permissions
function deleteResource(req, res) {
  const { resourceId } = req.params;
  const { user } = req;

  // Check if user owns resource or is admin
  const resource = await Resource.findById(resourceId);

  if (resource.ownerId !== user.id && user.role !== 'admin') {
    return res.status(403).json({ error: 'Forbidden' });
  }

  await resource.delete();
}

// Bad - no authorization check
function deleteResource(req, res) {
  await Resource.findByIdAndDelete(req.params.id); // Anyone can delete!
}
```

## Cross-Site Scripting (XSS) Prevention

### Output Encoding

```javascript
// Good - React auto-escapes
<div>{userInput}</div>

// Dangerous - bypass escaping
<div dangerouslySetInnerHTML={{ __html: userInput }} /> // Avoid!

// If you must use HTML, sanitize first
import DOMPurify from 'dompurify';
const clean = DOMPurify.sanitize(userInput);
```

### Content Security Policy (CSP)

```javascript
// Add CSP headers
app.use(helmet.contentSecurityPolicy({
  directives: {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'", "'unsafe-inline'"], // Avoid unsafe-inline in production
    styleSrc: ["'self'", "'unsafe-inline'"],
    imgSrc: ["'self'", 'data:', 'https:'],
    connectSrc: ["'self'"],
    fontSrc: ["'self'"],
    objectSrc: ["'none'"],
    mediaSrc: ["'self'"],
    frameSrc: ["'none'"],
  }
}));
```

## Cross-Site Request Forgery (CSRF) Protection

```javascript
// Use CSRF tokens
const csurf = require('csurf');
const csrfProtection = csurf({ cookie: true });

app.post('/transfer', csrfProtection, (req, res) => {
  // Process transfer
});

// In forms
<form method="POST" action="/transfer">
  <input type="hidden" name="_csrf" value="{csrfToken}">
  <!-- form fields -->
</form>
```

## HTTPS/TLS

### Enforce HTTPS

```javascript
// Redirect HTTP to HTTPS
app.use((req, res, next) => {
  if (req.header('x-forwarded-proto') !== 'https') {
    res.redirect(`https://${req.header('host')}${req.url}`);
  } else {
    next();
  }
});

// HSTS (HTTP Strict Transport Security)
app.use(helmet.hsts({
  maxAge: 31536000, // 1 year
  includeSubDomains: true,
  preload: true
}));
```

## API Security

### Rate Limiting

```javascript
const rateLimit = require('express-rate-limit');

// Global rate limit
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // 100 requests per window
  message: 'Too many requests, please try again later'
});

app.use('/api/', limiter);

// Stricter limit for auth endpoints
const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5, // 5 attempts
  skipSuccessfulRequests: true
});

app.post('/api/login', authLimiter, loginHandler);
```

### CORS Configuration

```javascript
const cors = require('cors');

// Good - specific origins
app.use(cors({
  origin: ['https://yourdomain.com', 'https://app.yourdomain.com'],
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization']
}));

// Bad - allow all origins
app.use(cors({ origin: '*' })); // Dangerous!
```

## File Upload Security

```javascript
const multer = require('multer');
const path = require('path');

// Good - validate file types and size
const upload = multer({
  storage: multer.diskStorage({
    destination: './uploads/',
    filename: (req, file, cb) => {
      // Generate unique filename
      const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
      cb(null, file.fieldname + '-' + uniqueSuffix);
    }
  }),
  limits: {
    fileSize: 5 * 1024 * 1024, // 5MB max
  },
  fileFilter: (req, file, cb) => {
    // Allow only specific types
    const allowedTypes = /jpeg|jpg|png|pdf/;
    const extname = allowedTypes.test(path.extname(file.originalname).toLowerCase());
    const mimetype = allowedTypes.test(file.mimetype);

    if (extname && mimetype) {
      cb(null, true);
    } else {
      cb(new Error('Invalid file type'));
    }
  }
});
```

## Dependency Security

### Regular Updates

```bash
# Check for vulnerabilities
npm audit

# Fix vulnerabilities
npm audit fix

# Check for outdated packages
npm outdated
```

### Use Lock Files

- Commit `package-lock.json` or `yarn.lock`
- Ensures consistent dependency versions
- Prevents supply chain attacks

### Automated Scanning

- Use Dependabot, Snyk, or npm audit in CI/CD
- Set up automated PR for security updates
- Monitor for zero-day vulnerabilities

## Logging & Monitoring

### Secure Logging

```javascript
// Good - log security events, not sensitive data
logger.info('User login attempt', {
  userId: user.id,
  ip: req.ip,
  userAgent: req.get('User-Agent')
});

// Bad - logging sensitive data
logger.info('User login', {
  password: user.password, // NEVER LOG PASSWORDS
  creditCard: user.card    // NEVER LOG PII
});
```

### Monitor for Attacks

- Track failed login attempts
- Monitor for brute force attacks
- Alert on unusual activity patterns
- Log and investigate security errors

## Error Handling

```javascript
// Good - generic error messages
try {
  await authenticate(username, password);
} catch (error) {
  // Don't reveal why it failed
  return res.status(401).json({ error: 'Invalid credentials' });
}

// Bad - revealing error messages
catch (error) {
  // Reveals whether user exists
  return res.status(401).json({ error: `User ${username} not found` });
}
```

## Security Headers

```javascript
const helmet = require('helmet');

// Use helmet for security headers
app.use(helmet());

// Or configure individually
app.use(helmet.frameguard({ action: 'deny' }));           // X-Frame-Options
app.use(helmet.xssFilter());                              // X-XSS-Protection
app.use(helmet.noSniff());                                // X-Content-Type-Options
app.use(helmet.referrerPolicy({ policy: 'no-referrer' })); // Referrer-Policy
```

## Database Security

- Use least privilege database users
- Encrypt sensitive data at rest
- Enable database audit logging
- Regular backups with encryption
- Separate read/write permissions

## Third-Party Integrations

- Validate webhooks signatures
- Use OAuth 2.0 for API access
- Implement API key rotation
- Whitelist IP addresses when possible
- Monitor third-party service status

## Security Checklist

Before deploying:

- [ ] All secrets in environment variables
- [ ] HTTPS enforced
- [ ] CSP headers configured
- [ ] CSRF protection enabled
- [ ] Rate limiting implemented
- [ ] Input validation on all endpoints
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (output encoding)
- [ ] Authentication implemented correctly
- [ ] Authorization checks on all protected resources
- [ ] Password hashing with bcrypt/argon2
- [ ] Security headers (helmet)
- [ ] Dependencies updated and scanned
- [ ] Error messages don't leak info
- [ ] Logging doesn't include sensitive data
- [ ] File uploads validated
- [ ] CORS configured properly

## Security Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/)
- [Node.js Security Best Practices](https://nodejs.org/en/docs/guides/security/)
- [Snyk Vulnerability Database](https://snyk.io/vuln/)

## Notes for Claude

- Always prioritize security in code reviews
- Validate all user inputs
- Never hardcode secrets
- Suggest security improvements proactively
- Flag potential security vulnerabilities
- Recommend security testing for new features
- Keep dependencies updated
