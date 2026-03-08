---
name: example-skill
description: An example skill demonstrating best practices for SKILL.md structure. Use this when you need a template for creating new skills.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Edit
  - Write
---

# Example Skill

This is an example skill that demonstrates the proper structure for creating reusable skills in Claude Code.

## Purpose

Skills extend Claude's capabilities by providing specialized knowledge and workflows. This example shows:

- How to structure SKILL.md with YAML frontmatter
- Best practices for skill descriptions
- How to organize supporting files
- Token-efficient prompt design

## When to Use This Skill

This skill should be invoked when:

- Creating a new skill and need a template
- Learning about skill structure
- Understanding YAML frontmatter configuration

## Instructions

When this skill is invoked:

1. **Read the Documentation**: Check if there are reference files in the `references/` subdirectory
2. **Analyze the Request**: Understand what the user is trying to accomplish
3. **Execute the Workflow**: Follow the specific steps for the task
4. **Provide Results**: Return clear, actionable output

## Skill Structure Best Practices

### YAML Frontmatter

```yaml
---
name: skill-name           # Must match the folder name
description: Clear description of what the skill does AND when to use it
allowed-tools:             # List of tools this skill can use
  - Read
  - Grep
  - Glob
---
```

### Content Organization

- Keep SKILL.md under 500 lines (200 lines preferred)
- Use clear sections with headers
- Provide specific, actionable instructions
- Include examples where helpful

### Supporting Files

- `scripts/`: Executable scripts (Python, Bash)
- `references/`: Documentation loaded into context
- `assets/`: Templates and resources

## Example Workflow

1. Identify the task requirements
2. Read relevant files using allowed tools
3. Process information according to instructions
4. Generate output or modifications
5. Validate results

## Notes

- Skills can be invoked manually with `/skill-name` or automatically when relevant
- Keep descriptions clear so Claude knows when to use the skill
- Optimize for token efficiency - shorter is better
- Test skills thoroughly before deploying
