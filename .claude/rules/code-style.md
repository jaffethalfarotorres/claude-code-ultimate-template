# Code Style Guidelines

This file defines code style, formatting, and naming conventions for the project.

## General Principles

- **Consistency**: Code should look like it was written by one person
- **Readability**: Optimize for reading, not writing
- **Simplicity**: Simple code over clever code
- **Maintainability**: Think about future developers (including yourself)

## Formatting

### Indentation

- Use **spaces**, not tabs
- Indentation size: **2 spaces** for web/JS, **4 spaces** for Python/Java
- Consistent indentation throughout the file

### Line Length

- Maximum line length: **100 characters** (soft limit)
- Hard limit: **120 characters**
- Break long lines logically (after commas, operators, etc.)

### Whitespace

- One blank line between function/method definitions
- Two blank lines between class definitions
- No trailing whitespace
- File should end with a single newline

### Braces and Blocks

```javascript
// Good - K&R style
if (condition) {
  doSomething();
} else {
  doSomethingElse();
}

// Bad - Egyptian braces
if (condition)
{
  doSomething();
}
```

## Naming Conventions

### General Rules

- Use **descriptive names** over abbreviations
- Avoid single-letter variables (except loop counters)
- Be consistent with naming patterns

### Language-Specific

**JavaScript/TypeScript**:

- `camelCase` for variables and functions
- `PascalCase` for classes and React components
- `SCREAMING_SNAKE_CASE` for constants
- Private methods: prefix with `_` or use `#` (private fields)

**Python**:

- `snake_case` for variables and functions
- `PascalCase` for classes
- `SCREAMING_SNAKE_CASE` for constants
- Private methods: prefix with single `_`
- Name-mangled methods: prefix with double `__`

**File Names**:

- `kebab-case.js` for JavaScript/TypeScript files
- `snake_case.py` for Python files
- `PascalCase.tsx` for React components

### Naming Patterns

```javascript
// Boolean variables - use "is", "has", "should", "can"
const isActive = true;
const hasPermission = false;
const shouldValidate = true;

// Functions - use verbs
function calculateTotal() { }
function getUserById(id) { }
function validateInput(data) { }

// Classes - use nouns
class UserManager { }
class DataProcessor { }
class ApiClient { }

// Constants
const MAX_RETRY_ATTEMPTS = 3;
const API_BASE_URL = 'https://api.example.com';
```

## Code Organization

### File Structure

```javascript
// 1. Imports (grouped and sorted)
import { standardLib } from 'node:fs';
import { thirdParty } from 'external-package';
import { localModule } from './local';

// 2. Constants
const CONSTANT_VALUE = 'value';

// 3. Type definitions
interface UserData { }

// 4. Main code
export class MainClass { }

// 5. Helper functions
function helperFunction() { }

// 6. Exports
export { helperFunction };
```

### Import Organization

Group imports in this order:

1. Node.js built-in modules
2. External dependencies
3. Internal/local modules
4. Types (if separate)

Separate groups with a blank line.

## Functions and Methods

### Function Length

- Keep functions under **50 lines** (ideal: 10-20 lines)
- One function should do one thing
- If function is too long, extract sub-functions

### Function Parameters

- Maximum **3-4 parameters**
- Use objects for more parameters
- Use default parameters when appropriate

```javascript
// Good - use object for multiple params
function createUser({ name, email, role = 'user' }) {
  // ...
}

// Bad - too many parameters
function createUser(name, email, role, permissions, settings, metadata) {
  // ...
}
```

### Return Early

```javascript
// Good - early returns
function processData(data) {
  if (!data) return null;
  if (!data.isValid) return null;

  return transform(data);
}

// Bad - nested conditions
function processData(data) {
  if (data) {
    if (data.isValid) {
      return transform(data);
    }
  }
  return null;
}
```

## Comments

### When to Comment

- **Why**, not **what**: Explain reasoning, not obvious code
- Complex algorithms or business logic
- Workarounds or temporary solutions
- TODOs and FIXMEs

### Comment Style

```javascript
// Good - explains why
// Using exponential backoff to handle API rate limiting
const delay = Math.pow(2, retryCount) * 1000;

// Bad - explains what (obvious)
// Multiply 2 to the power of retryCount and multiply by 1000
const delay = Math.pow(2, retryCount) * 1000;
```

### Documentation Comments

```javascript
/**
 * Calculates the total price including tax and discount.
 *
 * @param {number} price - Base price
 * @param {number} taxRate - Tax rate as decimal (e.g., 0.15 for 15%)
 * @param {number} discount - Discount as decimal (e.g., 0.10 for 10%)
 * @returns {number} Final price after tax and discount
 */
function calculateTotal(price, taxRate, discount) {
  // Implementation
}
```

## Error Handling

- Always handle errors explicitly
- Use try-catch for async operations
- Provide meaningful error messages
- Log errors appropriately

```javascript
// Good
try {
  const data = await fetchData();
  return processData(data);
} catch (error) {
  logger.error('Failed to fetch data:', error);
  throw new DataFetchError('Unable to retrieve data', { cause: error });
}

// Bad
try {
  return await fetchData();
} catch (e) {
  console.log(e); // Poor error handling
}
```

## DRY (Don't Repeat Yourself)

- Extract repeated code into functions
- Use utilities for common operations
- Avoid copy-paste programming

## Code Smells to Avoid

- **Magic numbers**: Use named constants
- **Nested ternaries**: Use if-else or extract to function
- **Long parameter lists**: Use objects
- **Deep nesting**: Extract to functions, use early returns
- **God classes**: Break into smaller, focused classes

## Linting and Formatting

### Tools

- **ESLint** for JavaScript/TypeScript
- **Prettier** for auto-formatting
- **Black** for Python
- **.editorconfig** for editor settings

### Pre-commit Hooks

- Run linters before commit
- Auto-format code
- Fix auto-fixable issues

## Language-Specific Guidelines

### JavaScript/TypeScript

- Use `const` by default, `let` when needed, never `var`
- Prefer arrow functions for callbacks
- Use template literals over string concatenation
- Use optional chaining `?.` and nullish coalescing `??`
- Prefer `async/await` over promise chains

### Python

- Follow PEP 8
- Use list/dict comprehensions appropriately
- Use context managers (`with` statement)
- Type hints for function signatures
- Use f-strings for formatting

## Review Checklist

Before submitting code:

- [ ] Code follows style guidelines
- [ ] Names are descriptive and consistent
- [ ] Functions are focused and small
- [ ] Comments explain "why", not "what"
- [ ] No commented-out code
- [ ] No console.log/print statements (use proper logging)
- [ ] Code is DRY
- [ ] Linter passes with no warnings
- [ ] Formatter has been run

## Notes for Claude

- Always follow these style guidelines when writing or refactoring code
- Run formatters and linters before committing changes
- Suggest improvements if existing code doesn't follow guidelines
- Ask about project-specific style preferences if unclear
