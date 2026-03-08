---
name: template-improver
description: Analyzes projects using this template and extracts generalizable patterns to improve the template itself. Use when reviewing feedback from template users or when analyzing successful template adaptations.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Write
  - Bash
---

# Template Improver Skill

This skill implements a continuous improvement loop where real-world template usage informs template enhancements.

## Purpose

Projects using this template often develop innovative solutions. This skill:
1. Identifies valuable patterns in user projects
2. Generalizes project-specific solutions
3. Proposes template improvements
4. Maintains evolution history

## When This Skill Activates

Automatically invokes when:
- User runs `/learn-from-project <path>`
- Reviewing GitHub issues with "enhancement" label
- Analyzing template usage feedback
- Conducting quarterly template improvement reviews

## Workflow

### Phase 1: Discovery

Scan the target project for innovations:

```bash
# Find custom rules
ls -la <project>/.claude/rules/

# Find custom commands
ls -la <project>/.claude/commands/

# Find custom skills
ls -la <project>/.claude/skills/

# Check CLAUDE.md enhancements
diff <template>/CLAUDE.md <project>/CLAUDE.md
```

**Look for**:
- Files that don't exist in template
- Significant enhancements to template files
- Novel configuration patterns
- Workflow innovations

### Phase 2: Analysis

For each discovery, evaluate:

**Usefulness Score** (1-10):
- Does it solve a real problem?
- How often would users need this?
- Does it save significant time/effort?

**Generalizability Score** (1-10):
- Is it project-specific or broadly applicable?
- Can it be abstracted for general use?
- Does it require domain knowledge?

**Quality Score** (1-10):
- Is it well-documented?
- Is it maintainable?
- Does it follow best practices?

**Priority Calculation**:
```
Priority = (Usefulness × 0.4) + (Generalizability × 0.4) + (Quality × 0.2)

High Priority: 8.0+
Medium Priority: 5.0-7.9
Low Priority: < 5.0
```

### Phase 3: Extraction

For high/medium priority discoveries:

1. **Abstract the Pattern**
   - Remove project-specific details
   - Generalize variable names
   - Document the underlying concept

2. **Create Template Version**
   - Adapt for general use
   - Add comprehensive documentation
   - Include usage examples

3. **Document Attribution**
   - Credit original project
   - Note original author
   - Link to source (if public)

### Phase 4: Proposal

Generate improvement proposal:

```markdown
## Template Enhancement Proposal

**From Project**: [name]
**Discovery Date**: YYYY-MM-DD
**Priority**: High/Medium/Low
**Estimated Impact**: [description]

### What We Found

[Description of the pattern/feature]

**Original Implementation**:
[Link to original or summary]

**Key Innovation**:
[What makes this valuable]

### Proposed Template Addition

**New File**: `.claude/[category]/[filename]`

**Content Summary**:
[What would be added]

**Documentation Updates**:
- README.md: [section to add/update]
- CLAUDE.md: [section to reference]
- TEMPLATE_EVOLUTION.md: [learning to log]

### Benefits

1. **For New Users**: [benefit]
2. **For Existing Users**: [benefit]
3. **For Template**: [benefit]

### Implementation Plan

1. [ ] Create enhancement branch
2. [ ] Add new file(s)
3. [ ] Update documentation
4. [ ] Add to TEMPLATE_EVOLUTION.md
5. [ ] Test with sample project
6. [ ] Create PR for review

### Attribution

**Original Author**: [name]
**Source Project**: [link if public]
**License**: [if applicable]
```

### Phase 5: Implementation

If approved:

```bash
# Create enhancement branch
git checkout -b enhancement/learned-from-[project]

# Add new files
# Update documentation
# Update TEMPLATE_EVOLUTION.md

git add .
git commit -m "feat: Add [feature] learned from [project]

Discovered [pattern] in [project] and generalized it for template use.

This enhancement:
- Solves: [problem]
- Helps: [use case]
- Impact: [benefit]

Original pattern by [author] from [project].
Adapted and generalized for template v[version].

Source: [link]
Credit: [author]
"

# Push and create PR
git push -u origin enhancement/learned-from-[project]
gh pr create --title "Enhancement: [description]" --body "[proposal]"
```

## Learning Categories

### 1. New Rule Categories

**Example from Centaur**:
- Session management patterns
- Multi-machine continuity
- Memory/state management

**Template Addition**:
```
.claude/rules/session-management.md
.claude/rules/multi-env.md
```

### 2. Workflow Commands

**Example from Centaur**:
- Session start/close automation
- Cross-machine sync
- State preservation

**Template Addition**:
```
.claude/commands/session-start.md
.claude/commands/session-close.md
```

### 3. Skills & Automation

**Example from Centaur**:
- Automated conflict resolution
- Pattern recognition
- Metric tracking

**Template Addition**:
```
.claude/skills/conflict-resolver/
.claude/skills/pattern-tracker/
```

### 4. CLAUDE.md Patterns

**Example from Centaur**:
- Role definitions (PM/Developer/Agent)
- Decision frameworks
- Workflow protocols

**Template Addition**:
- Better role definition templates
- Decision framework examples
- Protocol documentation patterns

### 5. Configuration Wisdom

**Example from Centaur**:
- Permission patterns for Python/web scraping
- Environment separation (corporate/personal)
- Settings organization

**Template Addition**:
- Domain-specific settings examples
- Multi-environment patterns
- Security-focused permissions

## Output Format

Create file: `learnings/YYYY-MM-DD-[project-name].md`

```markdown
# Learning Report: [Project Name]

**Analysis Date**: YYYY-MM-DD
**Project**: [name and description]
**Template Version Used**: v[X.Y.Z]
**Project Type**: [web/CLI/data/API/etc]

## Executive Summary

[2-3 sentences: key learnings and impact]

## Discoveries

### High Priority (Implement Now)

#### 1. [Discovery Name]
- **What**: [description]
- **Why**: [value/benefit]
- **How**: [implementation approach]
- **Files**: [affected files]
- **Priority Score**: [X.X/10]

### Medium Priority (Consider)

#### 1. [Discovery Name]
[same structure]

### Low Priority (Track)

#### 1. [Discovery Name]
[same structure]

## Interesting Patterns (Document)

### 1. [Pattern Name]
- **Context**: [when used]
- **Approach**: [how implemented]
- **Learning**: [insight gained]

## Issues Observed (Fix)

### 1. [Issue Name]
- **Problem**: [what went wrong]
- **Cause**: [root cause]
- **Fix**: [prevention strategy]

## Attribution

**Project**: [name]
**Author**: [name]
**Source**: [link if public]
**License**: [license]
**Permission**: [obtained/public/etc]

## Next Steps

### Immediate
- [ ] [action item]

### Short Term
- [ ] [action item]

### Long Term
- [ ] [action item]

## Template Version Impact

This analysis contributed to template v[X.Y.Z] with:
- [X] new rule files
- [X] new commands
- [X] new skills
- [X] documentation updates

---

**Template Evolution**: This project made the template better! 🌱
```

## Success Metrics

Track learning effectiveness:

| Metric | Target | Actual |
|--------|--------|--------|
| Discoveries per project | 3-5 | - |
| High priority findings | 1-2 | - |
| Template enhancements | 2-3/quarter | - |
| Projects analyzed | 1/month | - |

## Continuous Improvement

This skill itself improves over time:
- Refine evaluation criteria
- Improve pattern recognition
- Better abstraction techniques
- Enhanced documentation

## Notes for Claude

When using this skill:
- Be thorough in analysis
- Respect project IP (don't copy business logic)
- Focus on generalizable patterns
- Always attribute original authors
- Get permission for significant borrowings
- Think "How does this make the template better for everyone?"

**Goal**: Make every project using this template contribute to making it better for the next project.
