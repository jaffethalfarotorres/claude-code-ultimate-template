# Contributing Guidelines

Thank you for considering contributing to this Claude Code template! This document outlines how to contribute effectively.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Collaborate openly

## How to Contribute

### Reporting Issues

Before creating an issue:
1. Search existing issues to avoid duplicates
2. Use a clear, descriptive title
3. Provide reproduction steps
4. Include environment details
5. Add relevant screenshots or logs

### Suggesting Enhancements

Enhancement suggestions are welcome! Please:
- Explain the problem it solves
- Describe the proposed solution
- Consider backward compatibility
- Provide use cases

### Pull Requests

1. **Fork and Clone**
   ```bash
   git clone https://github.com/your-username/claude-code-template
   cd claude-code-template
   ```

2. **Create Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**
   - Follow the code style guidelines
   - Add tests if applicable
   - Update documentation

4. **Test Your Changes**
   ```bash
   npm test  # or appropriate test command
   npm run lint
   ```

5. **Commit Changes**
   ```bash
   git commit -m "feat: Add your feature description"
   ```
   Follow [conventional commits](https://www.conventionalcommits.org/)

6. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```

## Development Setup

### Prerequisites
- Git
- Node.js 18+ (or Python 3.11+ for Python projects)
- Claude Code installed

### Setup Steps

```bash
# Clone repository
git clone <repo-url>
cd claude-code-template

# Install dependencies
npm install  # or pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Run tests
npm test
```

## Code Style

- Follow the conventions in [.claude/rules/code-style.md](.claude/rules/code-style.md)
- Use the project's linter and formatter
- Write clear, self-documenting code
- Add comments for complex logic

## Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Aim for >80% code coverage
- Follow testing guidelines in [.claude/rules/testing.md](.claude/rules/testing.md)

## Documentation

- Update README.md for user-facing changes
- Update CLAUDE.md for project context changes
- Add/update JSDoc comments for functions
- Include examples for new features

## Commit Messages

Follow conventional commits format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**: feat, fix, docs, style, refactor, test, chore

**Examples**:
```
feat(commands): Add deployment command
fix(security): Resolve XSS vulnerability in user input
docs(readme): Update installation instructions
```

## PR Requirements

Before submitting:

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] No merge conflicts
- [ ] Self-reviewed the changes
- [ ] Added tests for new features

## Review Process

1. Maintainers will review within 2-3 days
2. Address review comments
3. Once approved, maintainer will merge
4. Delete your branch after merge

## Questions?

- Check existing issues and discussions
- Read the documentation
- Ask in discussions section
- Contact maintainers

Thank you for contributing! 🎉
