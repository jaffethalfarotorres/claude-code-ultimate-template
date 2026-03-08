Perform a comprehensive security audit of the codebase, checking for common vulnerabilities and security best practices.

## Security Checklist

### 1. Secrets Detection
- [ ] Scan all files for hardcoded API keys
- [ ] Check for passwords in code
- [ ] Look for private keys or certificates
- [ ] Verify .env files are in .gitignore
- [ ] Check git history for accidentally committed secrets

### 2. Input Validation
- [ ] Review all user input handling
- [ ] Check for SQL injection vulnerabilities
- [ ] Verify NoSQL injection prevention
- [ ] Test command injection scenarios
- [ ] Review file upload validation

### 3. Authentication & Authorization
- [ ] Verify password hashing (bcrypt/argon2)
- [ ] Check JWT token implementation
- [ ] Review session management
- [ ] Test authorization checks on protected endpoints
- [ ] Verify role-based access control

### 4. Data Protection
- [ ] Check for XSS vulnerabilities
- [ ] Verify CSRF protection
- [ ] Review CORS configuration
- [ ] Check encryption of sensitive data
- [ ] Verify HTTPS enforcement

### 5. Dependencies
- [ ] Run npm audit or pip-audit
- [ ] Check for known vulnerabilities
- [ ] Review dependency versions
- [ ] Identify outdated packages
- [ ] Check for supply chain risks

### 6. API Security
- [ ] Verify rate limiting
- [ ] Check authentication on all endpoints
- [ ] Review error message disclosure
- [ ] Test for IDOR vulnerabilities
- [ ] Verify API key protection

### 7. Configuration
- [ ] Review security headers
- [ ] Check cookie security flags
- [ ] Verify environment-specific configs
- [ ] Review logging configuration
- [ ] Check file permissions

## Report Format

Provide findings in this structure:

### Critical Issues
- Description
- Location (file:line)
- Impact
- Recommended fix

### High Priority
- Description
- Location
- Recommendation

### Medium Priority
- Security improvements
- Best practice suggestions

### Low Priority / Informational
- Minor improvements
- Future considerations

## Actions

For each issue found:
1. Explain the vulnerability
2. Show the problematic code
3. Provide a secure code example
4. Prioritize by severity (Critical/High/Medium/Low)

Ask if you should fix the issues automatically or create a report for manual review.
