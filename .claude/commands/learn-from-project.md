Analyze another project that uses this template and extract learnings to improve the template itself.

## Purpose

This command creates a feedback loop where real-world usage of the template improves the template for future users. Projects using this template become sources of improvements.

## Usage

```bash
/learn-from-project <path-to-project>
```

Example:
```bash
/learn-from-project ../Projects/Centaur
```

## Analysis Steps

### 1. Discover What They Added

Scan the project for:
- Custom rules in `.claude/rules/` that aren't in the template
- New commands in `.claude/commands/` beyond template defaults
- Enhancements to CLAUDE.md structure
- New skills in `.claude/skills/`
- Hooks they created
- Configuration patterns in `settings.json`

### 2. Analyze Effectiveness

For each discovery, evaluate:
- **Usefulness**: Does this solve a common problem?
- **Generalizability**: Would other projects benefit from this?
- **Quality**: Is it well-documented and maintainable?
- **Patterns**: Does this reveal a pattern we should include?

### 3. Extract Learnings

Create learning report with:

**High-Value Additions** (should add to template):
- New rule files that solve common problems
- Commands that automate frequent workflows
- CLAUDE.md patterns that improve clarity
- Configuration patterns that enhance productivity

**Project-Specific Customizations** (document as examples):
- Domain-specific rules
- Business-specific commands
- Unique workflow patterns

**Anti-Patterns Observed** (add warnings):
- Common mistakes in customization
- Configuration pitfalls
- Documentation gaps

### 4. Propose Template Improvements

Generate proposals:

```markdown
## Proposed Template Enhancements

### Add to .claude/rules/
- **[new-rule].md** - [Description of what it solves]
  - Extracted from: [project-name]
  - Solves: [problem]
  - Benefit: [why it's useful]

### Add to .claude/commands/
- **[new-command].md** - [Description]
  - Use case: [when to use]
  - Impact: [productivity gain]

### Enhance Documentation
- Update README.md section: [section]
- Add example: [what example]

### Update CLAUDE.md Template
- Add section: [section name]
- Reason: [why it improves template]
```

### 5. Create Enhancement Branch

If improvements are approved:

```bash
# In template repo
git checkout -b enhancement/learned-from-[project-name]

# Apply improvements
# Commit with clear attribution

git commit -m "feat: Add [feature] learned from [project]

Discovered this pattern in [project-name] and generalized it
for the template. This solves [problem] for [use-case].

Source: [project-repo-url]
Credit: [original-author]"
```

## Learning Categories

### 1. **Rule Patterns**
- New categories of rules (e.g., `api-design.md`, `performance.md`)
- Better organization within rules
- Domain-specific adaptations (web, CLI, API, data, ML)

### 2. **Command Innovations**
- Workflow automation commands
- Integration commands (deploy, release, sync)
- Quality assurance commands

### 3. **CLAUDE.md Structure**
- Section organization improvements
- Information hierarchy patterns
- Context optimization techniques

### 4. **Configuration Wisdom**
- Permission patterns that work well
- Environment variable organization
- Settings that enhance productivity

### 5. **Documentation Excellence**
- README improvements
- Better examples
- Clearer quick-start guides

## Output Format

```markdown
# Learning Report: [Project Name]

**Date**: YYYY-MM-DD
**Project**: [name]
**Template Version**: [version they used]

## Summary
[2-3 sentence summary of key learnings]

## Discoveries

### High-Value (Recommend adding to template)
1. **[Discovery 1]**
   - What: [description]
   - Why: [benefit]
   - How: [implementation]
   - Files: [affected files]

### Interesting Patterns (Document as examples)
1. **[Pattern 1]**
   - Context: [when they use it]
   - Adaptation: [how they customized]

### Issues Observed (Fix in template)
1. **[Issue 1]**
   - Problem: [what went wrong]
   - Root cause: [why it happened]
   - Fix: [how to prevent]

## Proposed Changes

### Immediate (High Priority)
- [ ] Add [file/feature]
- [ ] Update [documentation]

### Consider (Medium Priority)
- [ ] Explore [idea]
- [ ] Document [pattern]

### Track (Low Priority / Future)
- [ ] Research [concept]
- [ ] Monitor [trend]

## Attribution

Credit: [project-author]
Source: [project-repo]
License: [if applicable]

## Next Steps

1. Create enhancement branch
2. Implement high-priority changes
3. Update documentation
4. Create PR for review
```

## Example Usage

After Centaur migration, run:
```bash
/learn-from-project ../Projects/Centaur
```

This would discover:
- Centaur's sophisticated session logging system
- Their two-PC continuity protocol
- Sprint log memory pattern
- Academic solver organization
- Web scraping security patterns

Extract generalizable patterns and add to template.

## Continuous Improvement Loop

```
Projects using template
    ↓
Learn from their adaptations
    ↓
Extract generalizable patterns
    ↓
Improve template
    ↓
New projects benefit
    ↓
(repeat)
```

**The template gets better with every project that uses it!**

## Notes

- Always credit original authors
- Respect project-specific IP (don't copy business logic)
- Generalize patterns (abstract away specifics)
- Document sources for transparency
- Get permission for significant borrowings
