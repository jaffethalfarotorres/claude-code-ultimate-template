# Claude Code Repository Template

**Version**: 2.3.0 (2026 Edition - Production Patterns)
**Last Updated**: March 2026

This is the ultimate production-ready template for Claude Code projects, following Anthropic's latest best practices and community standards.

## What is This Repository?

This repository serves as a comprehensive, self-explanatory template for:

- **New Projects**: Start with Claude Code from day one
- **Existing Projects**: Migrate using our migration guide ([MIGRATION.md](MIGRATION.md))
- **Team Onboarding**: Share consistent Claude Code setup across teams
- **Learning**: Reference implementation of 2026 best practices

## Quick Start

### For New Projects

```bash
# 1. Clone or copy this template
git clone <your-repo-url> my-new-project

# 2. Customize CLAUDE.md for your project
# 3. Update .claude/rules/ with your conventions
# 4. Start coding with Claude!
```

### For Existing Projects

See [MIGRATION.md](MIGRATION.md) for a complete migration guide, or use:

```bash
/migrate-project  # Guided migration command
```

## Project Structure

```text
Claude/
├── .claude/
│   ├── commands/              # Custom slash commands
│   ├── skills/                # Reusable skills with SKILL.md
│   ├── rules/                 # Modular project rules
│   ├── settings.json          # Project-level settings
│   └── settings.local.json.example  # Local settings template
├── archive/
│   ├── backups/               # Version backups (v2.3.0 NEW!)
│   └── trash-can/             # Reversible deletion staging
├── decisions/                 # Architectural Decision Records (v2.3.0 NEW!)
├── knowledge/                 # Persistent memory (optional)
│   ├── SPRINT_LOG.md         # Operational metrics
│   ├── CHRONICLE.md          # Historical narrative
│   └── MEMORY.md             # Current state
├── .ai/
│   └── session_logs/          # Session continuity logs
├── docs/                      # Extended documentation
├── templates/                 # Project type templates
├── .editorconfig              # Editor configuration
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore patterns
├── CLAUDE.md                  # This file - Claude's memory
├── CONTRIBUTING.md            # Contribution guidelines
├── MIGRATION.md               # Migration guide
├── TEMPLATE_EVOLUTION.md      # Template learning history
└── README.md                  # Full documentation
```

## Core Concepts

### CLAUDE.md (This File)

- **Purpose**: Claude's long-term memory for your project
- **Best Practice**: Keep under 200-300 lines
- **Loading**: Automatically loaded in every Claude Code session
- **Scope**: Project-wide context and high-level guidelines

### .claude/rules/ Directory

Modular organization for specific concerns (loaded automatically):

- **code-style.md**: Formatting, naming conventions, linting
- **testing.md**: Testing standards and TDD practices
- **security.md**: Security requirements and patterns
- **git-workflow.md**: Git conventions and PR guidelines
- **documentation.md**: Documentation standards

**Pro Tip**: Use path-based targeting in frontmatter to load rules only for specific files:

```markdown
---
paths: src/api/**/*.ts
---
# API-specific rules here
```

### Commands vs Skills

| Feature | Commands | Skills |
|---------|----------|--------|
| Location | `.claude/commands/` | `.claude/skills/` |
| Invocation | Manual only | Manual or automatic |
| Format | Simple Markdown | Markdown + YAML frontmatter |
| Best For | Quick prompts | Complex workflows |

## Configuration Files

### .claude/settings.json (Project Settings)

Shared team configuration:

- Permission policies
- Environment variables
- Attribution settings
- Checked into version control

### .claude/settings.local.json (Personal Settings)

Developer-specific overrides:

- API keys and tokens
- Personal preferences
- **Never committed** (in .gitignore)

## Development Workflow

### Git Workflow

1. **Always create feature branches** for new work
2. **Use descriptive commit messages** following conventions
3. **Review changes** before committing (use `/review`)
4. **Run tests** before pushing (use `/test`)

### Commit Message Convention

```text
<type>: <subject>

<body>

<footer>
```

**Types**: feat, fix, docs, style, refactor, test, chore

**Example**:

```text
feat: Add user authentication system

Implement JWT-based authentication with refresh tokens.
Includes middleware for protected routes.

Closes #123
```

### Claude Code Commands

- `/review` - Comprehensive code review
- `/test` - Run and analyze tests
- `/explain` - Explain code sections
- `/custom-init` - Generate CLAUDE.md for any project
- `/migrate-project` - Migrate existing projects
- `/security-audit` - Security review
- `/learn-from-project` - Extract learnings from projects using this template
- `/deploy` - Deployment workflow

## Self-Improving Template System

This template learns from projects that use it:

- **template-improver skill** - Analyzes project adaptations and extracts patterns
- **TEMPLATE_EVOLUTION.md** - Tracks how the template improves over time
- **Feedback loop** - Your innovations can improve the template for everyone

When you build something innovative with this template, use `/learn-from-project` to share insights back. The template gets better with each project!

## Code Quality Standards

### General Principles

- **DRY** (Don't Repeat Yourself)
- **SOLID** principles for OOP
- **Clear naming** over clever code
- **Comments for "why"**, not "what"
- **Test coverage** > 80%

### File Organization

- One concept per file
- Max file size: 300-500 lines
- Logical folder structure
- Consistent naming conventions

See [.claude/rules/code-style.md](.claude/rules/code-style.md) for detailed standards.

## Testing Strategy

- **Unit tests**: Individual functions and methods
- **Integration tests**: Component interactions
- **E2E tests**: Critical user flows
- **TDD preferred** for new features

See [.claude/rules/testing.md](.claude/rules/testing.md) for testing guidelines.

## Security Best Practices

🔒 **Critical Security Rules**:

- **Never commit secrets** (API keys, tokens, passwords)
- **Use .env files** for sensitive configuration
- **Review dependencies** for vulnerabilities
- **Validate all inputs** from users/external sources
- **Use HTTPS** for all external communication

See [.claude/rules/security.md](.claude/rules/security.md) for detailed security guidelines.

## Documentation Requirements

- **README.md**: Project overview, setup, usage
- **Code comments**: Complex logic, algorithms, workarounds
- **API docs**: All public interfaces
- **Inline docs**: Function/class documentation
- **CHANGELOG.md**: Track all notable changes

See [.claude/rules/documentation.md](.claude/rules/documentation.md) for standards.

## MCP (Model Context Protocol) Integration

Claude Code can connect to external tools via MCP servers:

- **GitHub**: Repository management
- **Filesystem**: Advanced file operations
- **Web Search**: Real-time information
- **Databases**: Direct database access
- **Custom**: Build your own MCP servers

**Setup**: See [docs/mcp-setup.md](docs/mcp-setup.md)

## Context Optimization

Keep Claude's context efficient:

### Token Budget Guidelines

- **CLAUDE.md**: 200-300 lines max
- **Each rule file**: 50-150 lines
- **Total rules**: 5-10 files max
- **Skills**: 15-20 max auto-invoked

### Hierarchical Loading

Claude loads context in priority order:

1. Current file/selection
2. CLAUDE.md (root + directory-specific)
3. .claude/rules/ (matching paths)
4. Skills (auto-invoked when relevant)

## Team Collaboration

### For New Team Members

1. Clone the repository
2. Read [README.md](README.md) and this file
3. Review [.claude/rules/](.claude/rules/) for conventions
4. Copy `.claude/settings.local.json.example` to `.claude/settings.local.json`
5. Configure your API keys and preferences

### For Project Leads

- Keep CLAUDE.md and rules up to date
- Document architectural decisions
- Add project-specific commands/skills
- Review and approve .claude/ changes

## Advanced Features

### Hooks

Automate workflows with hooks:

- **UserPromptSubmit**: Enrich prompts automatically
- **PreToolUse**: Validate before tool execution
- **PostToolUse**: Log or process results

**Example**: See [docs/hooks-guide.md](docs/hooks-guide.md)

### Custom Skills

Build reusable skills for:

- Code generation from templates
- Complex refactoring workflows
- Automated testing strategies
- Deployment procedures

**Tutorial**: See [docs/creating-skills.md](docs/creating-skills.md)

## Project Templates

Choose a template for your project type:

- `templates/web-app/` - Web applications
- `templates/api/` - REST/GraphQL APIs
- `templates/cli/` - Command-line tools
- `templates/monorepo/` - Monorepo projects

## Migration Guide

Migrating an existing project? See [MIGRATION.md](MIGRATION.md) for:

- Pre-migration checklist
- Step-by-step migration process
- Common migration patterns
- Troubleshooting guide

## Contributing

Want to improve this template? See [CONTRIBUTING.md](CONTRIBUTING.md).

## Resources

### Official Documentation

- [Claude Code Docs](https://code.claude.com/docs)
- [Anthropic Platform](https://platform.anthropic.com)
- [Model Context Protocol](https://modelcontextprotocol.io)

### Community Resources

- [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code)
- [Claude Code Best Practices](https://github.com/awattar/claude-code-best-practices)
- [Skills Marketplace](https://github.com/anthropics/skills)

## Notes for Claude

When working with this project:

1. **Read first**: Always read relevant files before making changes
2. **Follow rules**: Respect conventions in `.claude/rules/`
3. **Test changes**: Run tests before committing
4. **Document decisions**: Update docs for significant changes
5. **Security first**: Never compromise on security practices
6. **Ask when uncertain**: Clarify requirements before proceeding
7. **Use available commands**: Leverage project-specific slash commands
8. **Maintain quality**: Uphold code quality standards
9. **Think modular**: Keep changes focused and single-purpose
10. **Stay updated**: Keep CLAUDE.md and rules current

## Production Patterns (v2.3.0 NEW!)

### Backup/Rollback Strategy

Before major changes, create quick backups:

```bash
/create-backup  # Creates versioned .tar.gz backup
```

**Benefits:**
- Faster than git branches for experiments
- Includes .gitignored files (.env, node_modules)
- Pre-deployment safety net
- Easy rollback if something breaks

**Location:** `archive/backups/`
**Manifest:** `archive/backups/README.md`

### Architectural Decision Records (ADRs)

Document **why** architectural choices were made:

```bash
/record-decision  # Creates numbered ADR
```

**When to use:**
- Technology choices (React vs Vue)
- Architecture patterns (microservices vs monolith)
- Process decisions (testing strategy)
- Tool selections (CI/CD platform)

**Location:** `decisions/`
**Template:** `decisions/000-template.md`

**Example:** `decisions/003-use-postgresql-for-database.md`

### Session Continuity (Multi-Machine Workflows)

For teams working across multiple machines:

**Session Logs:** `.ai/session_logs/YYYY-MM-DD_HH-MM_{machine}.md`
- Real-time incremental logging during work
- Git as shared brain (conversation history is local)
- Automatic session start protocol

**Persistent Memory:** `knowledge/`
- `SPRINT_LOG.md` - Operational metrics and backlog
- `CHRONICLE.md` - Historical narrative and learnings
- `MEMORY.md` - Current state and pending items

**Use case:** Work on PC A, continue on PC B without losing context.

### Reversible Operations

**Trash-can pattern:**
1. Move questionable files to `archive/trash-can/{category}/`
2. Review in second pass
3. Delete only after confirmation

**Result:** Confident autonomous cleanup with safety net.

---

## Version History

- **2.3.0** (March 2026): Production patterns from real-world usage (backups, ADRs, session continuity)
- **2.2.0** (March 2026): 8 patterns from Centaur project
- **2.1.0** (March 2026): Self-improving learning system
- **2.0.0** (March 2026): Ultimate template with 2026 best practices
- **1.0.0** (Initial): Basic Claude Code template

---

**Remember**: This CLAUDE.md is a living document. Update it as your project evolves.

**Template Evolution**: This template learns from projects that use it. See [TEMPLATE_EVOLUTION.md](TEMPLATE_EVOLUTION.md) for how we continuously improve.
