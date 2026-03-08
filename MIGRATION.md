# Migration Guide

This guide helps you migrate existing projects to use this Claude Code template structure.

## Overview

Migrating an existing project involves:
1. Adding the `.claude/` directory structure
2. Creating or updating `CLAUDE.md`
3. Configuring settings
4. Adding commands and skills
5. Setting up documentation

## Quick Migration (Automated)

```bash
# Use the migrate-project command
/migrate-project
```

This command will guide you through the migration process interactively.

## Manual Migration

### Prerequisites

- [ ] Project is under git version control
- [ ] All changes are committed
- [ ] You have a backup or can revert changes

### Step 1: Create Safety Checkpoint

```bash
git checkout -b claude-code-migration
git add .
git commit -m "chore: Checkpoint before Claude Code migration"
```

### Step 2: Add .claude Directory Structure

```bash
mkdir -p .claude/{commands,skills,rules}
```

### Step 3: Copy Template Files

From this repository, copy:

```bash
# Essential files
cp template/.claude/settings.json .claude/
cp template/.claude/settings.local.json.example .claude/
cp template/.editorconfig ./
cp template/.env.example ./  # If you don't have one

# Rules (customize for your project)
cp template/.claude/rules/*.md .claude/rules/

# Commands (optional, add what you need)
cp template/.claude/commands/review.md .claude/commands/
cp template/.claude/commands/test.md .claude/commands/
cp template/.claude/commands/explain.md .claude/commands/
```

### Step 4: Generate or Update CLAUDE.md

#### Option A: Generate Fresh

```bash
# Use the custom-init command
/custom-init
```

#### Option B: Manual Creation

Create `CLAUDE.md` with your project specifics:

```markdown
# [Your Project Name]

## Project Overview
[Brief description]

## Tech Stack
- Framework: [e.g., React, Django]
- Language: [e.g., TypeScript, Python]
- Database: [e.g., PostgreSQL]
- [Other key technologies]

## Project Structure
\`\`\`
your-project/
├── src/
├── tests/
└── [other directories]
\`\`\`

## Development Commands
\`\`\`bash
npm install  # or pip install -r requirements.txt
npm run dev  # Start development server
npm test     # Run tests
\`\`\`

## Code Conventions
[Your specific conventions]

## Notes for Claude
[Project-specific guidelines]
```

### Step 5: Customize Rules

Edit `.claude/rules/` files to match your project:

**code-style.md**:
- Update to reflect your linting rules (.eslintrc, .prettierrc)
- Add language-specific conventions
- Include team preferences

**testing.md**:
- Update test framework (Jest, Pytest, etc.)
- Add project-specific testing patterns
- Include coverage requirements

**security.md**:
- Add project-specific security concerns
- List sensitive endpoints
- Document authentication flow

**git-workflow.md**:
- Match your team's branching strategy
- Update commit message format
- Add PR review process

**documentation.md**:
- Match existing documentation standards
- Add project-specific requirements

### Step 6: Configure Settings

Edit `.claude/settings.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(npm *)",
      "Bash(git *)",
      // Add your project's commands
    ],
    "deny": [
      "Read(./.env)",
      // Add sensitive files
    ]
  },
  "env": {
    "NODE_ENV": "development"
    // Add project environment variables
  }
}
```

### Step 7: Update .gitignore

Add to `.gitignore`:

```gitignore
# Claude Code specific
.claude/settings.local.json
.claude/local/
```

### Step 8: Add Custom Commands

Create project-specific commands in `.claude/commands/`:

**deploy.md** (if applicable):
```markdown
Deploy the application to [your deployment target].

Follow the deployment checklist:
1. Run tests
2. Build production bundle
3. Run deployment script
4. Verify deployment

[Project-specific deployment steps]
```

### Step 9: (Optional) Add Skills

For complex, reusable workflows, create skills in `.claude/skills/`:

```markdown
---
name: your-skill-name
description: What this skill does and when to use it
allowed-tools:
  - Read
  - Write
  - Grep
---

# Skill Instructions
[Detailed workflow steps]
```

### Step 10: Update Documentation

#### README.md

Add section about Claude Code:

```markdown
## Development with Claude Code

This project uses Claude Code for AI-assisted development.

### Getting Started
- Read [CLAUDE.md](CLAUDE.md) for project context
- Review [.claude/rules/](.claude/rules/) for conventions
- Use `/help` in Claude Code to see available commands

### Available Commands
- `/review` - Code review
- `/test` - Run tests
- `/deploy` - Deploy application
```

#### Create CONTRIBUTING.md

If you don't have one, create contribution guidelines (see CONTRIBUTING.md template in this repository).

### Step 11: Test the Setup

```bash
# Start Claude Code in your project
claude

# Test commands
/review
/test

# Verify CLAUDE.md loads
# Check that rules are being applied
```

### Step 12: Commit Changes

```bash
git add .claude/ CLAUDE.md .editorconfig .env.example .gitignore
git commit -m "feat: Add Claude Code configuration

- Add .claude/ directory with commands, rules, and settings
- Create CLAUDE.md with project context
- Configure permissions and environment
- Add development commands for common tasks

This enables AI-assisted development with Claude Code."
```

## Migration Checklist

- [ ] Safety commit created
- [ ] `.claude/` directory structure created
- [ ] `CLAUDE.md` created or updated
- [ ] `.claude/settings.json` configured
- [ ] `.claude/settings.local.json.example` created
- [ ] Rules customized for project
- [ ] Project-specific commands added
- [ ] `.gitignore` updated
- [ ] `.editorconfig` added
- [ ] `.env.example` updated
- [ ] README updated
- [ ] CONTRIBUTING.md created/updated
- [ ] All commands tested
- [ ] Changes committed

## Common Migration Patterns

### For React/Next.js Projects

```markdown
# CLAUDE.md additions
## Tech Stack
- React 18+ with TypeScript
- Next.js 14 (App Router)
- Tailwind CSS
- React Query for data fetching

## Code Conventions
- Use App Router conventions
- Prefer server components by default
- Use 'use client' sparingly
- Collocate tests with components
```

### For Python/Django Projects

```markdown
# CLAUDE.md additions
## Tech Stack
- Python 3.11+
- Django 5.0+
- PostgreSQL 15
- Celery for async tasks

## Code Conventions
- Follow PEP 8
- Use Django's conventions
- Type hints required
- Docstrings for all public functions
```

### For API Projects

```markdown
# CLAUDE.md additions
## API Conventions
- RESTful design
- Versioned endpoints (/api/v1/)
- Standard HTTP status codes
- JSON responses
- OpenAPI/Swagger documentation
```

## Troubleshooting

### Commands not working

- Check `.claude/commands/` files have .md extension
- Verify file permissions
- Restart Claude Code session

### Rules not being applied

- Check files are in `.claude/rules/` directory
- Verify markdown format
- Check for frontmatter errors if using path targeting

### Settings not loading

- Verify JSON syntax in `settings.json`
- Check file location (`.claude/settings.json`)
- Look for schema validation errors

## Rolling Back

If migration causes issues:

```bash
git checkout main  # or your main branch
git branch -D claude-code-migration
```

## Getting Help

- Check [Claude Code Docs](https://code.claude.com/docs)
- Review examples in this template
- Ask Claude for help: "Help me troubleshoot my Claude Code setup"

## Next Steps After Migration

1. **Team Onboarding**: Share the updated repository with team
2. **Documentation**: Update team wiki/docs about Claude Code usage
3. **Iteration**: Refine rules and commands based on usage
4. **Feedback**: Gather team feedback and improve configuration

## Version-Specific Migrations

### Migrating from Claude Code v1.x to v2.x

- Move commands from `.claude/commands/` to skills format if using YAML
- Update `settings.json` schema to v2 format
- Migrate to `.claude/rules/` from monolithic CLAUDE.md if applicable

See [official migration guide](https://code.claude.com/docs/migration) for version-specific details.
