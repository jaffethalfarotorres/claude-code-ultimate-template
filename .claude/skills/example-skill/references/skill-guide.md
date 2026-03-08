# Skill Creation Guide

This reference document provides additional context for creating effective Claude Code skills.

## Key Principles

1. **Clarity**: Skills should have clear, specific purposes
2. **Efficiency**: Keep prompts concise to minimize token usage
3. **Reusability**: Design skills to work across different contexts
4. **Documentation**: Include clear instructions and examples

## Frontmatter Fields

- `name`: The skill identifier (must match folder name)
- `description`: What the skill does AND when to use it (critical for auto-invocation)
- `allowed-tools`: Which tools the skill can use

## Token Optimization

- Target: < 200 lines for SKILL.md
- Use references/ for detailed documentation
- Avoid redundant instructions
- Focus on unique value the skill provides

## Testing Skills

Before deploying a skill:

1. Test manual invocation with `/skill-name`
2. Verify auto-invocation triggers correctly
3. Check token usage in conversations
4. Validate output quality
5. Review for edge cases

## Common Patterns

- **Analysis Skills**: Read code, provide insights
- **Generation Skills**: Create files from templates
- **Workflow Skills**: Multi-step processes
- **Integration Skills**: Connect external tools
