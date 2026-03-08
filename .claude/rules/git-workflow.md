# Git Workflow Guidelines

This file defines Git conventions, branching strategies, and commit standards.

## Branch Strategy

### Main Branches

- **`main`** (or `master`): Production-ready code
- **`develop`**: Integration branch for features (optional for smaller projects)

### Feature Branches

```bash
# Create feature branch from main/develop
git checkout -b feature/user-authentication main

# Convention: feature/<short-description>
feature/add-dark-mode
feature/user-profile-page
feature/payment-integration
```

### Other Branch Types

```text
fix/bug-description        # Bug fixes
hotfix/critical-fix        # Production hotfixes
refactor/code-cleanup      # Code refactoring
docs/update-readme         # Documentation updates
test/add-unit-tests        # Testing improvements
chore/update-dependencies  # Maintenance tasks
```

## Commit Messages

### Format

```text
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, missing semi-colons, etc.)
- **refactor**: Code refactoring (no functionality change)
- **perf**: Performance improvements
- **test**: Adding or updating tests
- **chore**: Build process, dependencies, tooling
- **revert**: Reverting previous commit

### Examples

```bash
# Simple commit
git commit -m "feat: Add user authentication"

# With scope
git commit -m "fix(auth): Resolve token expiration issue"

# With body and footer
git commit -m "feat(api): Add pagination to user endpoint

Implement cursor-based pagination for better performance
with large datasets. Includes backward compatibility.

Closes #123
Breaking Change: query parameter 'page' replaced with 'cursor'"
```

### Good Commit Messages

✅ **DO**:

- Use imperative mood ("Add feature" not "Added feature")
- Keep subject line under 50 characters
- Capitalize first letter
- No period at the end of subject
- Separate subject from body with blank line
- Wrap body at 72 characters
- Explain **what** and **why**, not **how**

❌ **DON'T**:

- "Fixed stuff"
- "WIP"
- "asdfgh"
- "Updates"
- "Minor changes"

## Workflow

### Starting New Work

```bash
# 1. Ensure you're on main/develop
git checkout main

# 2. Pull latest changes
git pull origin main

# 3. Create feature branch
git checkout -b feature/my-new-feature

# 4. Work on your feature
# ... make changes ...

# 5. Commit frequently with good messages
git add .
git commit -m "feat: Implement core functionality"
```

### Before Committing

```bash
# 1. Check what changed
git status
git diff

# 2. Review staged changes
git diff --staged

# 3. Run tests
npm test

# 4. Run linter
npm run lint

# 5. Commit
git commit -m "feat: Add new feature"
```

### Pushing Changes

```bash
# First push - set upstream
git push -u origin feature/my-feature

# Subsequent pushes
git push
```

### Creating Pull Requests

```bash
# 1. Ensure branch is up to date with main
git checkout main
git pull origin main
git checkout feature/my-feature
git rebase main  # or git merge main

# 2. Push to remote
git push origin feature/my-feature

# 3. Create PR on GitHub/GitLab
# Use /review command to get code review before creating PR
```

## Pull Request Guidelines

### PR Title

Same format as commit messages:

```text
feat: Add user authentication system
fix: Resolve memory leak in data processor
docs: Update API documentation
```

### PR Description Template

```markdown
## Description

Brief description of changes

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing

- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Checklist

- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No console.log/debug statements
- [ ] Tests added/updated

## Screenshots (if applicable)

## Related Issues

Closes #123
Related to #456
```

### PR Size

- Keep PRs small and focused (<400 lines changed ideally)
- One feature/fix per PR
- Split large features into multiple PRs

## Code Review

### As Author

- Self-review before requesting review
- Respond to comments promptly
- Be open to feedback
- Make requested changes or discuss alternatives
- Keep PR updated with main branch

### As Reviewer

- Review promptly (within 24 hours)
- Be constructive and respectful
- Test the changes locally if needed
- Approve only when confident
- Use suggestions for minor changes

## Merging Strategy

### Squash and Merge (Recommended)

- Clean, linear history
- One commit per PR
- Good for feature branches

```bash
# GitHub does this automatically with "Squash and merge"
```

### Rebase and Merge

- Linear history with all commits preserved
- Good for maintaining detailed history

### Merge Commit

- Preserves all commits and branch history
- Can become messy
- Use for large, long-lived branches

## Branch Protection Rules

### Main Branch

- Require PR reviews (minimum 1-2 approvals)
- Require status checks to pass
- Require branches to be up to date
- No force pushes
- No deletions

## Common Workflows

### Updating Feature Branch

```bash
# Option 1: Rebase (cleaner history)
git checkout feature/my-feature
git fetch origin
git rebase origin/main

# Option 2: Merge (preserves history)
git checkout feature/my-feature
git merge main
```

### Fixing Mistakes

```bash
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Amend last commit
git add forgotten-file.js
git commit --amend --no-edit

# Revert a commit (creates new commit)
git revert <commit-hash>
```

### Stashing Changes

```bash
# Save work in progress
git stash

# Apply stashed changes
git stash pop

# List stashes
git stash list

# Apply specific stash
git stash apply stash@{0}
```

## Git Hooks

### Pre-commit

```bash
# .git/hooks/pre-commit
#!/bin/sh
npm run lint
npm test
```

### Pre-push

```bash
# .git/hooks/pre-push
#!/bin/sh
npm run build
```

## Tags and Releases

### Semantic Versioning

```text
MAJOR.MINOR.PATCH

1.0.0 → Initial release
1.1.0 → New feature (backward compatible)
1.1.1 → Bug fix
2.0.0 → Breaking change
```

### Creating Tags

```bash
# Annotated tag (recommended)
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0

# List tags
git tag -l
```

## .gitignore Best Practices

```gitignore
# Dependencies
node_modules/
.pnp/

# Environment variables
.env
.env.local
.env.*.local

# Build outputs
dist/
build/
out/

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Logs
*.log
npm-debug.log*

# Testing
coverage/

# Never ignore
!.env.example
!.gitignore
```

## Conflict Resolution

```bash
# During merge/rebase conflicts
# 1. View conflicting files
git status

# 2. Open files and resolve conflicts manually
# Look for <<<<<<< HEAD markers

# 3. Mark as resolved
git add resolved-file.js

# 4. Continue merge/rebase
git rebase --continue
# or
git merge --continue
```

## Best Practices Summary

- [ ] Branch off main for new work
- [ ] Use descriptive branch names
- [ ] Write clear commit messages
- [ ] Commit frequently, push regularly
- [ ] Keep PRs small and focused
- [ ] Review code before committing
- [ ] Run tests before pushing
- [ ] Rebase/merge from main regularly
- [ ] Never commit secrets or sensitive data
- [ ] Delete branches after merging
- [ ] Use meaningful tag names for releases

## Common Anti-Patterns

**AVOID**:

- Committing directly to main
- Vague commit messages ("fix", "update")
- Huge PRs (>1000 lines)
- Committing broken code
- Force pushing to shared branches
- Leaving branches unmerged for weeks
- Not updating from main regularly

## Notes for Claude

- Always create feature branches for new work
- Write clear, conventional commit messages
- Run tests and linters before committing
- Keep commits focused and atomic
- Suggest splitting large changes into multiple commits
- Help maintain a clean git history
- Never commit sensitive data or secrets
