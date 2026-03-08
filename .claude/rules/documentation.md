# Documentation Guidelines

This file defines documentation standards and best practices for the project.

## Documentation Philosophy

- **Code is read more than written**: Invest in clarity
- **Self-documenting code first**: Good names reduce need for comments
- **Document the "why"**: Code shows "what", docs explain "why"
- **Keep docs close to code**: Easier to maintain and update
- **Docs are code**: Review, test, and maintain documentation

## Required Documentation

### 1. README.md (Required)

Every project must have a README with:

```markdown
# Project Name

Brief description (1-2 sentences)

## Features

- Key feature 1
- Key feature 2
- Key feature 3

## Prerequisites

- Node.js 18+
- PostgreSQL 14+
- API key from [Service Name]

## Installation

\`\`\`bash
npm install
cp .env.example .env
# Edit .env with your configuration
npm run setup
\`\`\`

## Usage

\`\`\`bash
npm start
\`\`\`

Visit `http://localhost:3000`

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| PORT | Server port | 3000 |
| DATABASE_URL | Postgres connection | - |

## Development

\`\`\`bash
npm run dev
npm test
npm run lint
\`\`\`

## Project Structure

\`\`\`
src/
  ├── components/
  ├── services/
  └── utils/
\`\`\`

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT
```

### 2. API Documentation

For APIs, document:

- Endpoints
- Request/response formats
- Authentication
- Error codes
- Rate limits
- Examples

**Tools**: OpenAPI/Swagger, Postman Collections

### 3. Code Comments

#### When to Comment

✅ **DO comment**:

- Complex algorithms
- Business logic/rules
- Workarounds for bugs
- Performance optimizations
- Security considerations
- Regex patterns
- Magic numbers

❌ **DON'T comment**:

- Obvious code
- What the code does (should be self-evident)
- Commented-out code (delete it, it's in git)

#### Comment Style

```javascript
// Good - explains WHY
// Using Set for O(1) lookup instead of Array.includes() O(n)
const uniqueIds = new Set(ids);

// Bad - explains WHAT (obvious)
// Create a new Set from ids
const uniqueIds = new Set(ids);

// Good - explains business rule
// Grace period of 30 days before account deletion per company policy
const GRACE_PERIOD_DAYS = 30;

// Good - explains workaround
// HACK: setTimeout needed because third-party lib triggers
// callback before DOM updates. Remove when upgrading to v3.
setTimeout(() => callback(), 0);
```

### 4. Function/Method Documentation

#### JavaScript/TypeScript (JSDoc)

```javascript
/**
 * Calculates the final price after applying tax and discount.
 *
 * @param {number} basePrice - The original price before adjustments
 * @param {Object} options - Configuration options
 * @param {number} options.taxRate - Tax rate as decimal (e.g., 0.15 for 15%)
 * @param {number} [options.discountPercent=0] - Discount percentage (0-100)
 * @returns {number} The final calculated price
 * @throws {Error} If basePrice is negative
 *
 * @example
 * const price = calculatePrice(100, { taxRate: 0.15, discountPercent: 10 });
 * // Returns: 103.5 (100 - 10% discount + 15% tax)
 */
function calculatePrice(basePrice, { taxRate, discountPercent = 0 }) {
  if (basePrice < 0) {
    throw new Error('Base price cannot be negative');
  }

  const discountedPrice = basePrice * (1 - discountPercent / 100);
  return discountedPrice * (1 + taxRate);
}
```

#### Python (Docstrings)

```python
def calculate_price(base_price: float, tax_rate: float, discount_percent: float = 0) -> float:
    """
    Calculate the final price after applying tax and discount.

    Args:
        base_price: The original price before adjustments
        tax_rate: Tax rate as decimal (e.g., 0.15 for 15%)
        discount_percent: Discount percentage (0-100), defaults to 0

    Returns:
        The final calculated price

    Raises:
        ValueError: If base_price is negative

    Examples:
        >>> calculate_price(100, 0.15, 10)
        103.5
    """
    if base_price < 0:
        raise ValueError("Base price cannot be negative")

    discounted_price = base_price * (1 - discount_percent / 100)
    return discounted_price * (1 + tax_rate)
```

### 5. Class Documentation

```javascript
/**
 * Manages user authentication and session handling.
 *
 * This class handles user login, logout, token generation,
 * and session validation. It uses JWT for token-based auth.
 *
 * @class
 * @example
 * const auth = new AuthManager(database);
 * const token = await auth.login(email, password);
 */
class AuthManager {
  /**
   * Creates an instance of AuthManager.
   *
   * @param {Database} database - Database instance for user lookup
   */
  constructor(database) {
    this.database = database;
  }

  /**
   * Authenticates a user and returns a JWT token.
   *
   * @async
   * @param {string} email - User's email address
   * @param {string} password - User's password (plain text)
   * @returns {Promise<string>} JWT authentication token
   * @throws {AuthenticationError} If credentials are invalid
   */
  async login(email, password) {
    // Implementation
  }
}
```

## Architecture Documentation

### 1. ARCHITECTURE.md

Document system design:

```markdown
# Architecture Overview

## System Components

- **Web Server**: Express.js REST API
- **Database**: PostgreSQL with Prisma ORM
- **Cache**: Redis for session storage
- **Queue**: Bull for async job processing

## Data Flow

\`\`\`
Client → API → Service Layer → Database
                    ↓
                Job Queue → Workers
\`\`\`

## Key Decisions

### Why PostgreSQL over MongoDB?
Need for ACID transactions and complex relational queries.

### Why Redis for sessions?
Fast in-memory lookups for frequently accessed session data.
```

### 2. ADR (Architecture Decision Records)

For significant decisions:

```markdown
# ADR 001: Use React for Frontend

## Status
Accepted

## Context
Need to choose a frontend framework for the web application.

## Decision
We will use React with TypeScript.

## Consequences
### Positive
- Large ecosystem and community
- Strong typing with TypeScript
- Good developer tools
- Team has existing experience

### Negative
- Learning curve for new developers
- Need to choose additional libraries (state management, routing)
- Bundle size considerations
```

## Inline Documentation

### Configuration Files

```javascript
// config/database.js

/**
 * Database configuration for different environments.
 *
 * Pool size calculation:
 * - Development: 5 connections (local, minimal load)
 * - Production: 20 connections (estimated 100 concurrent users / 5 avg queries per user)
 *
 * Timeout: 30s chosen based on slowest query (user_reports: 25s)
 */
module.exports = {
  development: {
    client: 'postgresql',
    connection: process.env.DATABASE_URL,
    pool: { min: 2, max: 5 },
    acquireConnectionTimeout: 30000
  },
  production: {
    client: 'postgresql',
    connection: process.env.DATABASE_URL,
    pool: { min: 5, max: 20 },
    acquireConnectionTimeout: 30000
  }
};
```

### Complex Algorithms

```javascript
/**
 * Implements the Luhn algorithm for credit card validation.
 *
 * Algorithm steps:
 * 1. Starting from the rightmost digit, double every second digit
 * 2. If doubling results in two digits, sum them (e.g., 16 → 1+6 = 7)
 * 3. Sum all digits
 * 4. If total modulo 10 equals 0, the number is valid
 *
 * @see https://en.wikipedia.org/wiki/Luhn_algorithm
 */
function validateCardNumber(cardNumber) {
  const digits = cardNumber.replace(/\D/g, '').split('').map(Number).reverse();

  const sum = digits.reduce((acc, digit, idx) => {
    if (idx % 2 === 1) {
      // Double every second digit
      digit *= 2;
      if (digit > 9) digit -= 9; // Sum digits if > 9
    }
    return acc + digit;
  }, 0);

  return sum % 10 === 0;
}
```

## CHANGELOG.md

Track all notable changes:

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- User profile customization

### Changed
- Updated dashboard UI

## [1.2.0] - 2026-03-07

### Added
- Two-factor authentication
- Export data to CSV
- Dark mode support

### Changed
- Improved search performance (2s → 200ms)
- Updated dependencies to latest versions

### Fixed
- Memory leak in websocket connections
- Incorrect timezone handling for scheduled tasks

### Security
- Fixed SQL injection vulnerability in search
- Updated vulnerable dependencies

## [1.1.0] - 2026-02-15

...
```

## README Templates

### Minimal README

```markdown
# Project Name

One-line description

## Quick Start

\`\`\`bash
npm install
npm start
\`\`\`

## Documentation

See [docs/](docs/) for full documentation.
```

### Comprehensive README

Include all sections: Features, Prerequisites, Installation, Usage, Configuration, Development, Testing, Deployment, Contributing, License, Credits

## Documentation Tools

### Generated Documentation

- **JSDoc**: JavaScript documentation generator
- **TypeDoc**: TypeScript documentation generator
- **Sphinx**: Python documentation generator
- **Swagger/OpenAPI**: API documentation

### Markdown Linters

- markdownlint
- remark-lint

### Diagramming

- **Mermaid**: Code-based diagrams in Markdown
- **PlantUML**: UML diagrams as code
- **Draw.io**: Visual diagrams

### Example Mermaid Diagram

```markdown
\`\`\`mermaid
graph TD
    A[Client] --> B[API Gateway]
    B --> C{Auth?}
    C -->|Yes| D[Process Request]
    C -->|No| E[Return 401]
    D --> F[Database]
\`\`\`
```

## Documentation Maintenance

### Keep Docs Updated

- Update docs when changing code
- Include doc updates in PRs
- Review docs in code reviews
- Test examples regularly

### Documentation Debt

- Track outdated docs as technical debt
- Schedule regular doc reviews
- Archive old documentation
- Remove obsolete docs

## Best Practices Summary

- [ ] Every project has a README
- [ ] APIs are documented (OpenAPI/Postman)
- [ ] Complex code has explanatory comments
- [ ] Public functions have JSDoc/docstrings
- [ ] Architecture decisions are recorded
- [ ] CHANGELOG is maintained
- [ ] Examples are provided and tested
- [ ] Setup instructions are clear
- [ ] Configuration is documented
- [ ] Docs are kept up to date

## Common Documentation Anti-Patterns

**AVOID**:

- Outdated documentation (worse than none)
- Documenting obvious code
- Walls of text without examples
- Incomplete setup instructions
- Broken links in documentation
- Code examples that don't work
- Documenting internal implementation details
- Copy-pasted documentation without updates

## Notes for Claude

- Update documentation when changing code
- Add comments for complex logic
- Ensure examples are correct and tested
- Keep documentation concise and relevant
- Use clear, simple language
- Provide examples for new features
- Update README for significant changes
- Maintain CHANGELOG with all changes
