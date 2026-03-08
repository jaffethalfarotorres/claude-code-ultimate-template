# Claude Code Repository Setup

A reference repository demonstrating best practices for setting up Claude Code projects according to Anthropic guidelines.

## Overview

This repository serves as a template and guide for organizing Claude Code projects with proper configuration, custom commands, and reusable skills. It follows Anthropic's recommended practices for repository structure and AI-assisted development workflows.

## Features

- **CLAUDE.md Configuration**: Project-specific context and guidelines for Claude
- **Custom Slash Commands**: Ready-to-use commands in `.claude/commands/`
- **Example Skills**: Demonstrative skill with proper SKILL.md structure
- **Best Practices**: Security, documentation, and workflow recommendations
- **Clean Structure**: Organized directory layout for easy navigation

## Repository Structure

```text
Claude/
├── .claude/
│   ├── commands/              # Custom slash commands
│   │   ├── review.md         # Code review command
│   │   ├── test.md           # Test execution command
│   │   └── explain.md        # Code explanation command
│   └── skills/               # Reusable skills
│       └── example-skill/    # Example skill demonstrating structure
│           ├── SKILL.md      # Skill definition with YAML frontmatter
│           └── references/   # Supporting documentation
├── .gitignore                # Git ignore patterns
├── CLAUDE.md                 # Claude's project memory
└── README.md                 # This file
```

## Quick Start

### 1. Clone or Use as Template

```bash
# Clone this repository
git clone <your-repo-url>

# Or use it as a GitHub template
# Click "Use this template" button on GitHub
```

### 2. Customize CLAUDE.md

Edit [CLAUDE.md](CLAUDE.md) to reflect your project's:

- Tech stack and dependencies
- Project structure
- Development commands
- Coding conventions
- Repository guidelines

**Tip**: Keep CLAUDE.md under 300 lines for optimal token usage.

### 3. Add Custom Commands

Create new slash commands in `.claude/commands/`:

```bash
# Example: Create a deployment command
echo "Deploy the application to production" > .claude/commands/deploy.md
```

Commands are automatically available as `/command-name` in Claude Code.

### 4. Create Skills

Add reusable skills in `.claude/skills/`:

```text
.claude/skills/my-skill/
├── SKILL.md           # Required: Skill definition
├── scripts/           # Optional: Helper scripts
├── references/        # Optional: Documentation
└── assets/           # Optional: Templates
```

**SKILL.md Template**:

```markdown
---
name: my-skill
description: What this skill does AND when to use it
allowed-tools:
  - Read
  - Write
  - Grep
---

# My Skill

Instructions for Claude when this skill is invoked...
```

## Using This Repository

### Available Commands

- **`/review`**: Review code changes and provide feedback
- **`/test`**: Run tests and analyze results
- **`/explain`**: Explain selected code or files

### Example Skill

The `example-skill` demonstrates:

- Proper YAML frontmatter structure
- Best practices for skill organization
- How to use supporting reference files
- Token-efficient prompt design

Invoke with `/example-skill` or let Claude use it automatically.

## Best Practices

### CLAUDE.md

- Keep concise (< 300 lines recommended)
- Include only universally applicable instructions
- Reference other files for detailed documentation
- Update when project structure changes significantly

### Commands vs Skills

| Feature | Commands | Skills |
|---------|----------|--------|
| Location | `.claude/commands/` | `.claude/skills/` |
| File Format | Simple Markdown | SKILL.md with YAML frontmatter |
| Invocation | Always manual (`/cmd`) | Manual or automatic |
| Complexity | Simple prompts | Complex workflows with tools |
| Best For | Quick tasks | Reusable, multi-step processes |

### Security

- Never commit API keys, tokens, or credentials
- Use `.gitignore` to exclude sensitive files
- Store secrets in environment variables
- Review staged files before committing

### Token Optimization

- Keep SKILL.md under 500 lines (200 preferred)
- Limit auto-invoked skills to 15-20 max
- Use reference files for detailed documentation
- Avoid redundant instructions

## Documentation

- **[CLAUDE.md](CLAUDE.md)**: Project context for Claude
- **[Example Skill](\.claude\skills\example-skill\SKILL.md)**: Skill template and guide
- **[Official Docs](https://code.claude.com/docs)**: Claude Code documentation

## Resources

### Official

- [Claude Code Documentation](https://code.claude.com/docs)
- [Anthropic Website](https://www.anthropic.com)

### Community

- [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code)
- [Skills Repository](https://github.com/anthropics/skills/)
- [Best Practices Guide](https://www.humanlayer.dev/blog/writing-a-good-claude-md)

## Contributing

This is a template repository. Feel free to:

- Fork and customize for your projects
- Submit issues for improvements
- Share your own best practices
- Create pull requests with enhancements

## License

This template is provided as-is for use in your own projects. Adapt as needed for your use case.

## Acknowledgments

Based on official Anthropic guidelines and community best practices for Claude Code development workflows.

---

**Ready to start?** Edit [CLAUDE.md](CLAUDE.md) and `.claude/` to match your project!
