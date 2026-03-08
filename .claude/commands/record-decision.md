---
description: Create Architectural Decision Record (ADR)
---

# Record Decision

Creates an Architectural Decision Record (ADR) documenting **why** an architectural choice was made.

## When to Use

- Major technology choices (React vs Vue, SQL vs NoSQL)
- Architecture patterns (microservices, monolith, serverless)
- Process decisions (testing strategy, deployment workflow)
- Tool selections (CI/CD platform, hosting provider)
- Design patterns (state management, API design)

## What It Does

1. Finds next ADR number automatically
2. Creates new ADR from template
3. Guides user through all sections
4. Commits ADR to repository

## Execution

### Step 1: Find Next ADR Number

```bash
# Get last ADR number
LAST_NUMBER=$(ls decisions/ 2>/dev/null | grep -E '^[0-9]{3}-' | sort -r | head -1 | cut -d'-' -f1)

# Calculate next number
if [ -z "$LAST_NUMBER" ]; then
  NEXT_NUMBER="001"
else
  NEXT_NUMBER=$(printf "%03d" $((10#$LAST_NUMBER + 1)))
fi
```

### Step 2: Get Decision Details

Ask user:

1. **Decision title** (e.g., "Use PostgreSQL for database")
2. **Brief description** (1-2 sentences explaining the decision)

Generate slug from title:
```bash
# "Use PostgreSQL for database" → "use-postgresql-for-database"
SLUG=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | sed 's/[^a-z0-9-]//g')
```

### Step 3: Create ADR File

Create file: `decisions/{NEXT_NUMBER}-{SLUG}.md`

Copy from template: `decisions/000-template.md`

Pre-fill:
- `{NUMBER}` → NEXT_NUMBER
- `{TITLE}` → Decision title
- `{DATE}` → Current date (YYYY-MM-DD)
- `{DECIDERS}` → Current user (from git config)

### Step 4: Guide User Through Sections

Open file in editor and guide user:

```markdown
I've created decisions/{NEXT_NUMBER}-{SLUG}.md

Please fill in the following sections:

## Context
- What problem are we solving?
- What constraints do we have?
- What's the current situation?

## Decision
- What specific decision did we make?
- What will we do?
- What won't we do?

## Consequences
- Positive: What benefits do we gain?
- Negative: What tradeoffs do we accept?
- Neutral: What interesting side effects?

## Alternatives Considered
- What other options did we evaluate?
- Why did we reject them?

## Implementation Notes
- How will we implement this?
- What are the next steps?

The template is open. When you're done editing, save and I'll commit it.
```

### Step 5: Commit ADR

After user confirms completion:

```bash
git add decisions/{NEXT_NUMBER}-{SLUG}.md
git commit -m "docs: ADR-{NEXT_NUMBER} - {TITLE}

Architectural Decision Record documenting {BRIEF_DESCRIPTION}.

Status: Accepted
Date: {DATE}

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

### Step 6: Report Success

```
✅ ADR created successfully!

📄 File: decisions/{NEXT_NUMBER}-{SLUG}.md
🔢 Number: {NEXT_NUMBER}
📅 Date: {DATE}
✅ Status: Accepted

The decision has been documented and committed.

To update status later:
- Edit the file and change Status field
- Commit with: git commit -m "docs: update ADR-{NEXT_NUMBER} status"

To reference in code:
- Add comment: // See ADR-{NEXT_NUMBER} for rationale
```

## Example Usage

**User:** /record-decision

**Claude:**
```
Creating Architectural Decision Record.

Next ADR number: 004

1. Decision title: Use PostgreSQL for database
2. Brief description: Migrating from SQLite to PostgreSQL for production

Creating decisions/004-use-postgresql-for-database.md...

I've pre-filled the template with:
- Decision 004: Use PostgreSQL for database
- Date: 2026-03-07
- Decider: Jaffeth Alfaro Torres

Please fill in:
- Context (why are we making this decision?)
- Decision (specific choice we made)
- Consequences (pros/cons/tradeoffs)
- Alternatives Considered (what else did we evaluate?)
- Implementation Notes (how will we do this?)

The file is ready. Would you like me to open it for editing?
```

**After user edits and confirms:**

```
✅ ADR created successfully!

📄 File: decisions/004-use-postgresql-for-database.md
🔢 Number: 004
📅 Date: 2026-03-07
✅ Status: Accepted

Committed: docs: ADR-004 - Use PostgreSQL for database
```

## ADR Lifecycle

**Statuses:**

1. **Proposed** - Decision suggested, under discussion
2. **Accepted** - Decision made and approved
3. **Deprecated** - No longer recommended, but not forbidden
4. **Superseded** - Replaced by newer decision (reference new ADR)

**Updating ADR status:**

```bash
# Edit decisions/{NUMBER}-{SLUG}.md
# Change: **Status:** Accepted → Deprecated

git add decisions/{NUMBER}-{SLUG}.md
git commit -m "docs: deprecate ADR-{NUMBER}"
```

## ADR Numbering

ADRs use sequential numbering:

- `001-first-decision.md`
- `002-second-decision.md`
- `003-third-decision.md`

**Never reuse numbers!** Even if ADR is deprecated, keep the number for historical reference.

## ADR Best Practices

**DO:**
- ✅ Write ADRs for significant architectural decisions
- ✅ Explain the "why" not just the "what"
- ✅ Document alternatives considered
- ✅ Keep it concise (1-2 pages max)
- ✅ Reference ADRs in code comments
- ✅ Update status when decisions change

**DON'T:**
- ❌ Write ADRs for trivial decisions (variable names, etc.)
- ❌ Delete or renumber ADRs
- ❌ Skip the "Alternatives Considered" section
- ❌ Use vague language ("might", "could", "maybe")

## Integration with Code

Reference ADRs in your code:

```python
# PostgreSQL connection setup
# See ADR-004 for database choice rationale
DATABASE_URL = os.getenv("DATABASE_URL")
```

```javascript
// Using Redux for state management
// See ADR-007 for state management decision
import { createStore } from 'redux';
```

## ADR vs. Other Documentation

**ADR vs. CHANGELOG:**
- CHANGELOG = what changed (user-facing)
- ADR = why we decided (developer-facing)

**ADR vs. Chronicle:**
- Chronicle = journey narrative (storytelling)
- ADR = decision records (rationale)

**ADR vs. Comments:**
- Comments = how code works (implementation)
- ADR = why we chose this approach (architecture)

## Viewing All ADRs

List all decisions:

```bash
ls decisions/*.md
```

Create ADR index:

```bash
echo "# Architectural Decision Records" > decisions/README.md
echo "" >> decisions/README.md
for file in decisions/[0-9]*.md; do
  NUMBER=$(basename "$file" | cut -d'-' -f1)
  TITLE=$(grep "^# Decision" "$file" | sed "s/# Decision $NUMBER: //")
  STATUS=$(grep "^\*\*Status:\*\*" "$file" | sed 's/\*\*Status:\*\* \[\(.*\)\]/\1/')
  echo "- [ADR-$NUMBER]($file): $TITLE (Status: $STATUS)" >> decisions/README.md
done
```

## References

- [ADR GitHub](https://adr.github.io/)
- [Michael Nygard's blog post](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

---

**Note:** ADRs create institutional memory. Future developers (including future you!) will thank you for documenting **why** decisions were made.
