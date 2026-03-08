# Claude Code Ultimate Template

**Version 2.3.0** - The definitive, production-ready template for Claude Code projects (2026 Edition - Production Patterns)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude-Code-blue.svg)](https://code.claude.com)

A comprehensive, self-explanatory template following Anthropic's latest best practices and community standards for Claude Code development.

## ✨ Features

- 🎯 **2026 Best Practices** - Latest Anthropic guidelines and community standards
- 📁 **Modular Rules System** - Organized `.claude/rules/` for scalable configuration
- ⚡ **Production-Ready** - Enterprise-grade settings and security
- 🔧 **Enhanced Commands** - Custom init, migration, security audit, and more
- 🎓 **Self-Explanatory** - Comprehensive documentation for easy onboarding
- 🔒 **Security-First** - Built-in security patterns and guidelines
- 🚀 **Migration Tools** - Easy adoption for existing projects
- 📚 **Complete Documentation** - Guides for every aspect
- 🌱 **Self-Improving** - Learns from real-world projects and evolves
- 💾 **Backup/Rollback** (v2.3.0 NEW!) - Quick `.tar.gz` snapshots before major changes
- 📋 **Architectural Decision Records** (v2.3.0 NEW!) - Document the "why" behind decisions
- 🔄 **Session Continuity** (v2.3.0 NEW!) - Work seamlessly across multiple machines

## 🚀 Quick Start

### For New Projects

```bash
# 1. Use this as a template (GitHub) or clone
git clone https://github.com/your-username/claude-code-template my-project
cd my-project

# 2. Customize for your project
# Edit CLAUDE.md with your project details
# Update .claude/rules/ with your conventions
# Copy .env.example to .env and configure

# 3. Start developing with Claude Code!
claude
```

### For Existing Projects

```bash
# Navigate to your project
cd your-existing-project

# Start Claude Code and use migration command
claude
/migrate-project

# Or see detailed migration guide
# Read MIGRATION.md for step-by-step instructions
```

## 📂 Repository Structure

```text
Claude/
├── .claude/
│   ├── commands/                    # Custom slash commands
│   │   ├── custom-init.md          # Generate CLAUDE.md for any project
│   │   ├── migrate-project.md      # Migrate existing projects
│   │   ├── security-audit.md       # Security vulnerability scanner
│   │   ├── review.md               # Code review
│   │   ├── test.md                 # Test execution
│   │   └── explain.md              # Code explanation
│   ├── skills/                      # Reusable workflows
│   │   └── example-skill/
│   │       ├── SKILL.md            # Skill definition
│   │       └── references/         # Supporting docs
│   ├── rules/                       # Modular project rules
│   │   ├── code-style.md           # Code formatting & conventions
│   │   ├── testing.md              # Testing standards & TDD
│   │   ├── security.md             # Security best practices
│   │   ├── git-workflow.md         # Git & PR conventions
│   │   └── documentation.md        # Documentation standards
│   ├── settings.json                # Project settings (committed)
│   └── settings.local.json.example  # Local settings template
├── docs/                            # Extended documentation
├── .editorconfig                    # Editor configuration
├── .env.example                     # Environment variables template
├── .gitignore                       # Git ignore patterns
├── CLAUDE.md                        # Claude's project memory
├── CONTRIBUTING.md                  # Contribution guidelines
├── MIGRATION.md                     # Migration guide for existing projects
├── README.md                        # This file
└── LICENSE                          # MIT License
```

## 🎯 Core Concepts

### CLAUDE.md - Claude's Memory

The central configuration file that Claude automatically loads. Contains:
- Project overview and purpose
- Tech stack and dependencies
- Development commands
- Code quality standards
- Team collaboration guidelines

**Best Practice**: Keep under 200-300 lines

### .claude/rules/ - Modular Organization

Instead of one giant CLAUDE.md, organize specific concerns into focused rule files:
- **code-style.md**: Formatting, naming, linting
- **testing.md**: Testing strategies and TDD
- **security.md**: Security requirements
- **git-workflow.md**: Git and PR conventions
- **documentation.md**: Documentation standards

Rules load automatically and can target specific file paths.

### Commands vs Skills

| Feature | Commands | Skills |
|---------|----------|--------|
| **Location** | `.claude/commands/` | `.claude/skills/` |
| **Format** | Simple Markdown | Markdown + YAML frontmatter |
| **Invocation** | Manual (`/command`) | Manual or automatic |
| **Best For** | Quick prompts | Complex workflows |
| **Example** | `/review`, `/test` | Auto-invoked debugging skill |

## 🛠️ Available Commands

- **`/custom-init`** - Generate tailored CLAUDE.md for any project
- **`/migrate-project`** - Guided migration for existing projects
- **`/security-audit`** - Comprehensive security vulnerability scan
- **`/review`** - Detailed code review with feedback
- **`/test`** - Run and analyze test suite
- **`/explain`** - Explain selected code or files

## 📋 What's Included

### Configuration Files
- ✅ `.claude/settings.json` - Team-shared settings
- ✅ `.claude/settings.local.json.example` - Personal settings template
- ✅ `.editorconfig` - Editor consistency
- ✅ `.env.example` - Environment variables template
- ✅ `.gitignore` - Comprehensive ignore patterns

### Documentation
- ✅ **CLAUDE.md** - 300-line project context
- ✅ **MIGRATION.md** - Step-by-step migration guide
- ✅ **CONTRIBUTING.md** - Contribution guidelines
- ✅ **README.md** - This comprehensive guide

### Rules (`.claude/rules/`)
- ✅ **code-style.md** - Complete style guide
- ✅ **testing.md** - Testing best practices
- ✅ **security.md** - Security checklist
- ✅ **git-workflow.md** - Git conventions
- ✅ **documentation.md** - Documentation standards

### Commands & Skills
- ✅ 6 production-ready commands
- ✅ Example skill with full structure
- ✅ Templates for creating your own

## 🎓 Getting Started Guide

### 1. Understand CLAUDE.md

Read [CLAUDE.md](CLAUDE.md) to see how Claude understands your project.

### 2. Review the Rules

Check [.claude/rules/](.claude/rules/) to see coding conventions:
- How code should be formatted
- Testing approach
- Security requirements
- Git workflow
- Documentation standards

### 3. Try the Commands

```bash
# Start Claude Code in this directory
claude

# Try available commands
/help           # See all commands
/review         # Review code changes
/custom-init    # Generate CLAUDE.md for a project
/security-audit # Run security scan
```

### 4. Customize for Your Project

- Edit `CLAUDE.md` with your project details
- Update `.claude/rules/` to match your conventions
- Add project-specific commands to `.claude/commands/`
- Configure `.claude/settings.json`

### 5. Add to Your Workflow

- Use `/review` before creating PRs
- Run `/security-audit` regularly
- Leverage `/test` for comprehensive testing
- Create custom commands for common tasks

## 🔒 Security

This template includes:
- ✅ Comprehensive security guidelines in `.claude/rules/security.md`
- ✅ Secrets detection patterns in `.gitignore`
- ✅ Security-focused permissions in `settings.json`
- ✅ `/security-audit` command for vulnerability scanning
- ✅ Environment variable templates (`.env.example`)

## 🔧 Configuration

### Project Settings (`.claude/settings.json`)

Shared across the team, includes:
- Permission policies (allow/deny)
- Environment variables
- Attribution settings
- Committed to version control

### Local Settings (`.claude/settings.local.json`)

Personal overrides, includes:
- API keys and tokens
- Personal preferences
- **Never committed** (in .gitignore)

Copy `.claude/settings.local.json.example` to get started.

## 🆕 What's New in v2.3.0 (Production Patterns)

This release adds **4 battle-tested patterns** extracted from real-world production projects:

### 💾 Backup/Rollback Strategy

Quick `.tar.gz` backups before major changes:

```bash
/create-backup  # Versioned safety net
```

**Benefits:**
- Faster than git branches for experiments
- Includes .gitignored files (.env, node_modules)
- Pre-deployment snapshots
- Easy rollback if something breaks

**Example:** `archive/backups/v1.3-database-migration.tar.gz`

### 📋 Architectural Decision Records (ADRs)

Document the "why" behind decisions:

```bash
/record-decision  # Creates numbered ADR
```

**When to use:**
- Technology choices (React vs Vue)
- Architecture patterns (microservices vs monolith)
- Process decisions (testing strategy)
- Tool selections (CI/CD platform)

**Example:** `decisions/004-use-postgresql-for-database.md`

### 🔄 Session Continuity (Multi-Machine Workflows)

Work seamlessly across multiple machines:

**Session Logs:** `.ai/session_logs/` - Real-time incremental logging
**Persistent Memory:** `knowledge/` - SPRINT_LOG, CHRONICLE, MEMORY
**Git as Shared Brain:** Conversation history stays local, context lives in repo

**Use case:** Work on PC A during the day, continue on PC B at home without losing context.

### 🗑️ Reversible Operations (Trash-Can Pattern)

Archive-first cleanup approach:

1. Move questionable files to `archive/trash-can/{category}/`
2. Review in second pass
3. Delete only after confirmation

**Result:** Confident autonomous cleanup with safety net.

---

**These patterns solve real pain points:**
- ✅ Session continuity across machines (#1 Claude Code pain point)
- ✅ Safe experimentation with quick rollback
- ✅ Institutional memory via ADRs
- ✅ Fearless cleanup with reversibility

**Source:** Extracted from [Centaur](https://github.com/jaffethalfarotorres/Centaur) (production business system) and [CarPooling](https://github.com/jaffethalfarotorres/CarPooling) (demo app) projects.

## 📚 Documentation

### For Users
- **[README.md](README.md)** - This file, complete overview
- **[CLAUDE.md](CLAUDE.md)** - Project context for Claude
- **[MIGRATION.md](MIGRATION.md)** - Migrate existing projects

### For Contributors
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute
- **[.claude/rules/](\.claude\rules\)** - Development guidelines

### For Reference
- **[Example Skill](\.claude\skills\example-skill\SKILL.md)** - Skill template
- **[Commands](\.claude\commands\)** - Command examples

## 🌟 Use Cases

### For Individual Developers
- Start new projects with best practices
- Maintain consistent coding standards
- Automate common development tasks

### For Teams
- Onboard new developers quickly
- Enforce team conventions
- Share institutional knowledge
- Streamline code reviews

### For Projects
- Migrate existing codebases
- Improve code quality
- Enhance security
- Standardize workflows

## 🚦 Migration Path

Already have a project? See [MIGRATION.md](MIGRATION.md) for:
- ✅ Pre-migration checklist
- ✅ Step-by-step instructions
- ✅ Common migration patterns
- ✅ Troubleshooting guide
- ✅ Automated migration with `/migrate-project`

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- How to report issues
- How to suggest enhancements
- Pull request process
- Development setup
- Code style guidelines

## 📖 Resources

### Official Documentation
- [Claude Code Docs](https://code.claude.com/docs)
- [Anthropic Platform](https://platform.anthropic.com)
- [Model Context Protocol](https://modelcontextprotocol.io)

### Community Resources
- [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code)
- [Claude Code Best Practices](https://github.com/awattar/claude-code-best-practices)
- [Skills Marketplace](https://github.com/anthropics/skills)

### Related Projects
- [Claude Code Templates Collection](https://github.com/davila7/claude-code-templates)
- [BMAD Method for Claude](https://github.com/aj-geddes/claude-code-bmad-skills)

## ❓ FAQ

**Q: Do I need all these files for my project?**
A: No! Use what you need. The template shows what's possible. Start with CLAUDE.md and add more as needed.

**Q: Can I use this for existing projects?**
A: Absolutely! See [MIGRATION.md](MIGRATION.md) or use `/migrate-project` command.

**Q: How do I keep the template updated?**
A: Add this repo as a remote and pull updates, or manually sync files you want to update.

**Q: What if my team doesn't use Claude Code?**
A: The conventions (code style, testing, git workflow) are useful regardless. The .claude/ directory won't interfere with other tools.

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Based on:
- Anthropic's official Claude Code guidelines
- Community best practices from awesome-claude-code
- Real-world usage patterns from production projects
- Feedback from Claude Code developers worldwide

## 🌱 Self-Improving Template

**This template learns and evolves!**

Every project using this template can contribute improvements back:

```
Your Projects → Extract Learnings → Improve Template → Better for Everyone
                                            ↓
                                    Template Evolves 🌱
```

### How It Works

1. **Use the Template**: Build your project with it
2. **Innovate**: Create custom rules, commands, patterns
3. **Share Back**: Use `/learn-from-project` to extract insights
4. **Everyone Benefits**: Your innovations improve the template

### Learning Commands

- **`/learn-from-project <path>`** - Analyze a project and extract generalizable patterns
- Automated by **template-improver skill** - Continuously identifies improvement opportunities

See [TEMPLATE_EVOLUTION.md](TEMPLATE_EVOLUTION.md) for learning history and contribution guidelines.

---

## 🔖 Version

**2.1.0** (March 2026) - Learning System Edition

### What's New in 2.1
- 🧠 **Self-improving system** - Template learns from real-world usage
- 🔍 `/learn-from-project` command - Extract patterns from projects
- 📊 **template-improver skill** - Automated enhancement discovery
- 📈 **TEMPLATE_EVOLUTION.md** - Track improvements over time
- 🌐 **Feedback loop** - Projects make template better

### What's in 2.0
- ✨ Modular `.claude/rules/` system
- ✨ Enhanced commands (`/custom-init`, `/migrate-project`, `/security-audit`)
- ✨ Comprehensive migration guide
- ✨ Production-ready configurations
- ✨ 2026 best practices
- ✨ Self-explanatory documentation

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/your-username/claude-code-template/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-username/claude-code-template/discussions)
- **Documentation**: This README and linked guides

---

**Ready to supercharge your development with Claude Code?**

```bash
git clone https://github.com/your-username/claude-code-template my-project
cd my-project
claude
```

Happy coding with Claude! 🚀
