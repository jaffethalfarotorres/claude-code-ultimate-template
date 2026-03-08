# Claude Repository

This repository demonstrates best practices for setting up a Claude Code project according to Anthropic guidelines.

## Project Overview

This is a reference repository for Claude Code projects, showcasing:

- Proper CLAUDE.md configuration
- Custom slash commands in `.claude/commands/`
- Reusable skills in `.claude/skills/`
- Best practices for AI-assisted development

## Tech Stack

- **Claude Code**: AI-powered coding assistant
- **Git**: Version control
- **Markdown**: Documentation and configuration

## Project Structure

```text
Claude/
├── .claude/                 # Claude Code configuration
│   ├── commands/           # Custom slash commands
│   └── skills/             # Reusable skills
├── .gitignore              # Git ignore patterns
├── CLAUDE.md               # This file - Claude's project memory
└── README.md               # Project documentation
```

## Directory Descriptions

- **`.claude/commands/`**: Contains custom slash commands that can be invoked with `/command-name`
- **`.claude/skills/`**: Contains reusable skills with SKILL.md files that Claude can use autonomously
- **Root files**: Project configuration and documentation

## Development Commands

### Git Commands

```bash
git status              # Check repository status
git add .               # Stage all changes
git commit -m "message" # Commit with message
git push                # Push to remote
```

### Claude Code Usage

- Use `/` to see available slash commands
- Custom commands are in `.claude/commands/`
- Skills are automatically discovered from `.claude/skills/`

## Code Style & Conventions

### Markdown Files

- Use clear, descriptive headers
- Keep CLAUDE.md under 300 lines
- Keep SKILL.md files under 500 lines
- Use code blocks with language identifiers

### File Organization

- Group related commands in `.claude/commands/`
- Keep skills focused and single-purpose
- Use descriptive file and folder names

### Documentation Standards

- Include clear descriptions for all commands and skills
- Provide usage examples
- Document prerequisites and dependencies

## Repository Guidelines

### Commit Messages

- Use clear, descriptive commit messages
- Start with a verb (Add, Update, Fix, Remove)
- Keep subject line under 50 characters
- Add detailed description if needed

### Branch Naming

- `feature/` prefix for new features
- `fix/` prefix for bug fixes
- `docs/` prefix for documentation updates

### Best Practices

- Review changes before committing
- Test commands and skills before adding them
- Keep the repository clean and organized
- Update documentation when making changes

## Security

- **Never commit API keys or secrets**
- Store sensitive data in environment variables
- Use `.gitignore` to exclude credential files
- Review files before staging to prevent accidental leaks

## References

For more information, see:

- [Claude Code Documentation](https://code.claude.com/docs)
- [Anthropic's Official Guidelines](https://www.anthropic.com)
- The README.md file in this repository

## Notes for Claude

- Always read relevant files before making changes
- Use the custom commands and skills defined in `.claude/`
- Follow the code style and conventions outlined above
- Ask for clarification if project requirements are unclear
- Keep this CLAUDE.md file updated with significant project changes
