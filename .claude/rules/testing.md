# Testing Guidelines

This file defines testing standards, strategies, and best practices for the project.

## Testing Philosophy

- **Tests are documentation**: They show how code should be used
- **Test behavior, not implementation**: Focus on what, not how
- **Fail fast**: Tests should catch bugs early
- **Maintainable tests**: Tests should be as clean as production code

## Testing Pyramid

Strive for the right balance:

```text
        /\
       /E2E\      <- 10% (Slow, brittle, expensive)
      /------\
     /Integr.\   <- 20% (Medium speed, medium cost)
    /----------\
   /   Unit     \ <- 70% (Fast, stable, cheap)
  /--------------\
```

- **70% Unit Tests**: Test individual functions/methods
- **20% Integration Tests**: Test component interactions
- **10% E2E Tests**: Test critical user workflows

## Coverage Goals

- **Minimum**: 80% code coverage
- **Target**: 90%+ for critical paths
- **100%** for:
  - Business logic
  - Security-critical code
  - Data transformation functions
  - API endpoints

## Test-Driven Development (TDD)

### Preferred Workflow

```text
1. Red: Write failing test
2. Green: Write minimal code to pass
3. Refactor: Improve code while keeping tests green
```

### Benefits

- Better design (testable code is better code)
- Faster debugging (know exactly what broke)
- Confidence in refactoring
- Living documentation

## Unit Tests

### Characteristics

- **Fast**: Runs in milliseconds
- **Isolated**: No dependencies on external systems
- **Deterministic**: Same input = same output
- **Independent**: Tests don't depend on each other

### Structure (AAA Pattern)

```javascript
describe('calculateDiscount', () => {
  it('should apply 10% discount for premium users', () => {
    // Arrange - setup test data
    const price = 100;
    const user = { isPremium: true };

    // Act - execute the function
    const result = calculateDiscount(price, user);

    // Assert - verify the result
    expect(result).toBe(90);
  });
});
```

### Naming Convention

```javascript
// Pattern: should [expected behavior] when [condition]
it('should return null when input is empty', () => {});
it('should throw error when user is unauthorized', () => {});
it('should calculate tax correctly for multiple items', () => {});
```

### What to Test

**DO test**:

- Happy path (normal use cases)
- Edge cases (empty, null, undefined, zero, negative)
- Error conditions
- Boundary values

**DON'T test**:

- Framework/library code (they have their own tests)
- Trivial getters/setters
- Constants
- Private implementation details

### Mocking and Stubbing

```javascript
// Good - mock external dependencies
describe('UserService', () => {
  it('should fetch user from database', async () => {
    // Mock database
    const mockDb = {
      findUser: jest.fn().mockResolvedValue({ id: 1, name: 'John' })
    };

    const service = new UserService(mockDb);
    const user = await service.getUser(1);

    expect(mockDb.findUser).toHaveBeenCalledWith(1);
    expect(user.name).toBe('John');
  });
});
```

## Integration Tests

### Purpose

Test interactions between:

- Multiple modules/components
- Database operations
- API calls
- File system operations

### Example

```javascript
describe('User Registration Flow', () => {
  let database;

  beforeAll(async () => {
    database = await setupTestDatabase();
  });

  afterAll(async () => {
    await database.cleanup();
  });

  it('should create user and send welcome email', async () => {
    const userData = { email: 'test@example.com', password: 'secure123' };

    const user = await registerUser(userData);

    // Verify database
    const savedUser = await database.users.findOne({ email: userData.email });
    expect(savedUser).toBeDefined();

    // Verify email was queued
    const emails = await database.emailQueue.find();
    expect(emails).toHaveLength(1);
    expect(emails[0].type).toBe('welcome');
  });
});
```

## End-to-End (E2E) Tests

### Purpose

Test complete user workflows from UI to database.

### When to Write E2E Tests

- Critical business flows (checkout, payment, signup)
- Most common user paths
- Regression-prone features

### Example (Playwright/Cypress)

```javascript
test('user can complete purchase', async ({ page }) => {
  // Navigate to product
  await page.goto('/products/123');

  // Add to cart
  await page.click('[data-test="add-to-cart"]');

  // Go to checkout
  await page.click('[data-test="checkout"]');

  // Fill payment details
  await page.fill('[name="cardNumber"]', '4242424242424242');
  await page.fill('[name="expiry"]', '12/25');

  // Submit
  await page.click('[data-test="submit-payment"]');

  // Verify success
  await expect(page.locator('[data-test="success-message"]')).toBeVisible();
});
```

## Test Data Management

### Test Fixtures

```javascript
// fixtures/users.js
export const testUsers = {
  admin: {
    id: 1,
    email: 'admin@example.com',
    role: 'admin'
  },
  regular: {
    id: 2,
    email: 'user@example.com',
    role: 'user'
  }
};
```

### Factory Pattern

```javascript
// factories/user.factory.js
export function createTestUser(overrides = {}) {
  return {
    id: Math.random(),
    email: `user${Date.now()}@example.com`,
    name: 'Test User',
    role: 'user',
    ...overrides
  };
}

// Usage
const admin = createTestUser({ role: 'admin' });
const premium = createTestUser({ isPremium: true });
```

## Test Organization

### File Structure

```text
src/
  ├── components/
  │   ├── Button.tsx
  │   └── Button.test.tsx        # Co-located with source
  ├── services/
  │   ├── UserService.ts
  │   └── UserService.test.ts
  └── __tests__/
      ├── integration/
      │   └── user-flow.test.ts
      └── e2e/
          └── purchase.test.ts
```

### Test Suites

```javascript
describe('UserService', () => {
  describe('getUser', () => {
    it('should return user when found', () => {});
    it('should return null when not found', () => {});
    it('should throw when database error', () => {});
  });

  describe('createUser', () => {
    it('should create user with valid data', () => {});
    it('should validate email format', () => {});
    it('should hash password', () => {});
  });
});
```

## Async Testing

### Promises and Async/Await

```javascript
// Good - use async/await
it('should fetch data', async () => {
  const data = await fetchData();
  expect(data).toBeDefined();
});

// Good - return promise
it('should fetch data', () => {
  return fetchData().then(data => {
    expect(data).toBeDefined();
  });
});

// Bad - forgot to await
it('should fetch data', () => {
  const data = fetchData(); // Missing await!
  expect(data).toBeDefined(); // Will fail
});
```

## Error Testing

```javascript
// Testing exceptions
it('should throw error for invalid input', () => {
  expect(() => {
    validateEmail('invalid');
  }).toThrow('Invalid email format');
});

// Testing async errors
it('should reject with error', async () => {
  await expect(fetchData()).rejects.toThrow('Network error');
});
```

## Test Doubles

### Mock - Replace entire module

```javascript
jest.mock('./database');
```

### Spy - Monitor function calls

```javascript
const spy = jest.spyOn(object, 'method');
expect(spy).toHaveBeenCalled();
```

### Stub - Provide controlled responses

```javascript
const stub = jest.fn().mockReturnValue(42);
```

### Fake - Simplified implementation

```javascript
class FakeDatabase {
  constructor() {
    this.data = [];
  }
  save(item) {
    this.data.push(item);
  }
  findAll() {
    return this.data;
  }
}
```

## Performance Testing

```javascript
it('should process 1000 items in under 100ms', () => {
  const start = Date.now();

  processLargeDataset(generateItems(1000));

  const duration = Date.now() - start;
  expect(duration).toBeLessThan(100);
});
```

## Snapshot Testing

```javascript
// Use sparingly - good for React components
it('should render correctly', () => {
  const component = render(<UserProfile user={testUser} />);
  expect(component).toMatchSnapshot();
});
```

**Warning**: Snapshots can hide bugs. Review snapshot changes carefully.

## Flaky Tests

### Prevention

- Avoid time-dependent tests
- Don't rely on execution order
- Clean up after each test
- Use fixed test data
- Avoid race conditions

### Debugging

```javascript
// Add retries for legitimate flaky scenarios
test.retry(3)('flaky network test', async () => {
  // Test that might fail due to network
});
```

## Continuous Integration

### Requirements

- All tests must pass before merge
- Run tests on every commit
- Monitor coverage trends
- Fail build if coverage drops

## Testing Tools

### Recommended Stack

- **Unit/Integration**: Jest, Vitest
- **E2E**: Playwright, Cypress
- **Mocking**: Jest, Sinon
- **Coverage**: Istanbul (built into Jest)
- **Visual Regression**: Percy, Chromatic

## Best Practices Summary

- [ ] Write tests before code (TDD)
- [ ] Aim for 80%+ coverage
- [ ] Keep tests fast (< 5 sec for unit tests)
- [ ] One assertion per test (ideally)
- [ ] Test edge cases and errors
- [ ] Use descriptive test names
- [ ] Mock external dependencies
- [ ] Clean up after tests
- [ ] Keep tests maintainable
- [ ] Run tests before committing

## Common Anti-Patterns

**DON'T**:

- Test implementation details
- Write tests that depend on each other
- Use random data (use fixed seeds)
- Skip cleanup
- Test private methods directly
- Have tests with side effects
- Write tests just for coverage

## Notes for Claude

- Always write tests for new features
- Update tests when refactoring
- Aim for TDD when possible
- Suggest test cases for edge conditions
- Ensure tests are isolated and deterministic
- Help maintain high test coverage
