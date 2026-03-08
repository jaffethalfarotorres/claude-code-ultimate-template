# Patterns Discovered Across All Businesses

**Last Updated:** 2026-03-08
**Pattern Count:** 12
**Contributing Businesses:** 2 (academic-ghostwriting, carpooling-platform)

---

## Purpose

This registry tracks **generalizable patterns** discovered across all businesses in the workspace. Each pattern originates from solving real problems in one business, then gets extracted and shared with all others.

**The Learning Flow:**
```
Business solves problem → Discover pattern → Document in LEARNINGS.md → Extract to template → All businesses benefit
```

---

## Pattern Categories

- **Architecture** — Folder structure, naming conventions, organization
- **Automation** — Zero-friction workflows, file watchers, pipelines
- **Intelligence** — Learning loops, knowledge extraction, self-improvement
- **Operations** — Backup strategies, decision tracking, session continuity
- **Safety** — Reversible operations, validation, error handling

---

## All Patterns (12 Total)

### Pattern 1: Two-PC Continuity System
**Category:** Operations
**Value:** HIGH
**Source:** academic-ghostwriting (Centaur)
**Date Discovered:** 2026-03-07

**Problem Solved:**
Session continuity when working across multiple machines (home PC + laptop). Conversation history is local to Claude Code, but git is universal.

**Solution:**
- `.ai/session_logs/` for real-time session logging
- `knowledge/` for persistent memory across machines
- Git as shared brain (commit session logs)
- `MEMORY.md` for current state tracking

**Applicability:** Universal (any business with multi-machine workflows)

**Implementation:**
```
businesses/{business}/
├── .ai/session_logs/
│   └── 2026-03-08-session.md
├── knowledge/
│   ├── MEMORY.md          # Current state (what's happening now)
│   └── patterns.md         # Accumulated learnings
```

**Evidence of Success:** Developer successfully switched machines mid-session, picked up exactly where they left off using MEMORY.md + git log.

---

### Pattern 2: Autonomous Agent Decision Framework
**Category:** Safety
**Value:** HIGH
**Source:** academic-ghostwriting (Centaur)
**Date Discovered:** 2026-03-07

**Problem Solved:**
How to let Claude Code work autonomously without breaking things? Need clear boundaries for what's safe to do vs. what needs approval.

**Solution:**
- Create decision tables: Reversible vs Irreversible actions
- Autonomous = anything reversible (archive, rename, refactor)
- Approval required = anything irreversible (delete permanently, push to prod, change configs)
- Use trash-can pattern for confident autonomous cleanup

**Applicability:** Universal (any business using Claude Code for autonomous work)

**Implementation:**
```markdown
# .claude/rules/decision-framework.md

## Autonomous (No Approval Needed)
- Archive files (move to archive/trash-can/)
- Rename variables/functions
- Refactor code
- Update knowledge.md
- Run tests

## Approval Required
- Delete permanently
- Push to production
- Modify git config
- Change environment variables
- Install dependencies
```

**Evidence of Success:** Centaur went from 147 files → 122 files (-17%) in one autonomous session. Zero mistakes, all reversible.

---

### Pattern 3: Sprint Log Pattern
**Category:** Intelligence
**Value:** HIGH
**Source:** academic-ghostwriting (Centaur)
**Date Discovered:** 2026-03-07

**Problem Solved:**
Persistent operational memory that survives across sessions. What's the current state? What's in backlog? What was accomplished?

**Solution:**
- `SPRINT_LOG.md` with 3 sections:
  1. **Current State** — Metrics table (files, modules, status)
  2. **Active Sprint** — Current goals and progress
  3. **Backlog** — Prioritized todo list
  4. **Sprint History** — Archive of completed sprints

**Applicability:** Universal (any business with ongoing development)

**Implementation:**
```markdown
# SPRINT_LOG.md

## Current State
| Metric | Value | Last Updated |
|--------|-------|--------------|
| Total Modules | 9 | 2026-03-08 |
| Active Features | 3 | 2026-03-08 |

## Active Sprint (Sprint 7: 2026-03-08)
**Goal:** Implement pattern discovery system

**Progress:**
- [x] Create PATTERNS_DISCOVERED.md
- [ ] Create sync-learnings.py
- [ ] Test pattern propagation

## Backlog (Prioritized)
1. Add email notification module
2. Optimize route-optimizer performance
3. Refactor user-matching algorithm

## Sprint History
<details>
<summary>Sprint 6: v5.0 Migration (2026-03-07)</summary>
Completed full migration to purpose-driven architecture.
</details>
```

**Evidence of Success:** Developer can return after 1 week absence and know exactly where they left off in 30 seconds.

---

### Pattern 4: Chronicle (Historical Narrative)
**Category:** Intelligence
**Value:** MEDIUM
**Source:** academic-ghostwriting (Centaur)
**Date Discovered:** 2026-03-07

**Problem Solved:**
Git log shows WHAT changed. Chronicle shows WHY decisions were made, with full context and lessons learned.

**Solution:**
- `CHRONICLE.md` — Narrative documentation of the journey
- Documents decision context (what was tried, why it failed, why final approach was chosen)
- Lessons learned tracked for future reference

**Applicability:** High-value for complex businesses, optional for simple ones

**Implementation:**
```markdown
# CHRONICLE.md

## Chapter 3: The Great Architecture Redesign (March 2026)

### The Problem
We had Spanish folder names that made no sense to computers. `estadistica` could mean statistics, or it could mean Estado de Tica (Costa Rican state data). Ambiguous.

### What We Tried
1. **Attempt 1:** Just translate to English → Still domain-driven, not purpose-driven
2. **Attempt 2:** Keep domains but add purpose in README → Nobody reads READMEs
3. **Attempt 3:** Purpose-driven naming → WINNER

### Why It Worked
Names describe OUTPUT, not DOMAIN. `data-analysis` tells you exactly what it does. Future-proof.

### Lessons Learned
- Computers need clarity, not cleverness
- Purpose > Domain for scalability
- Flat > Nested for navigation
```

---

### Pattern 5: Trash-Can Pattern (Reversible Operations)
**Category:** Safety
**Value:** MEDIUM
**Source:** academic-ghostwriting (Centaur)
**Date Discovered:** 2026-03-07

**Problem Solved:**
Fear of deleting files prevents autonomous cleanup. Need confidence that mistakes can be undone.

**Solution:**
- `archive/trash-can/` — Staging area for deletions
- Review before permanent removal
- Enables confident autonomous cleanup

**Applicability:** Universal (any business with file cleanup needs)

**Implementation:**
```
businesses/{business}/
├── archive/
│   ├── trash-can/
│   │   └── 2026-03-08/  # Dated folders for easy review
│   └── backups/
```

**Evidence of Success:** Claude Code autonomously cleaned 25 deprecated files with zero mistakes (all reversible via trash-can).

---

### Pattern 6: Linked Documentation System
**Category:** Architecture
**Value:** MEDIUM
**Source:** academic-ghostwriting (Centaur)
**Date Discovered:** 2026-03-07

**Problem Solved:**
Navigating unfamiliar codebases is slow. Need self-documenting structure.

**Solution:**
- Every folder has `README.md` explaining its purpose
- Links to related documentation
- Creates navigation trail

**Applicability:** Universal (improves onboarding for all businesses)

**Implementation:**
```
businesses/{business}/
├── route-optimizer/
│   └── README.md         # "This module calculates optimal routes..."
├── user-matching/
│   └── README.md         # "This module matches riders with drivers..."
```

---

### Pattern 7: Root Hygiene Rules
**Category:** Architecture
**Value:** MEDIUM
**Source:** academic-ghostwriting (Centaur)
**Date Discovered:** 2026-03-07

**Problem Solved:**
Root folder becomes dumping ground for random documentation. Hard to navigate.

**Solution:**
- Strict conventions for root folder contents
- Feature docs go in feature folders
- Root only has: README, CLAUDE.md, core documentation, pipelines/, modules/

**Applicability:** Universal (prevents root bloat in all businesses)

**Rules:**
```
✅ Root folder (allowed):
- README.md, CLAUDE.md, SPRINT_LOG.md, CHRONICLE.md
- pipelines/, _shared/, _meta/
- Module folders (route-optimizer/, user-matching/)

❌ Root folder (forbidden):
- Feature documentation (goes in feature folder)
- Temporary files (goes in archive/trash-can/)
- Random notes (goes in knowledge/ or _shared/)
```

---

### Pattern 8: Version Consistency Checks
**Category:** Operations
**Value:** LOW
**Source:** academic-ghostwriting (Centaur)
**Date Discovered:** 2026-03-07

**Problem Solved:**
Documentation references version numbers in multiple places. Easy to update one and forget others.

**Solution:**
- Automated script checks for version references across all docs
- Warns if inconsistent

**Applicability:** Optional (useful for businesses with versioned releases)

---

### Pattern 9: Backup/Rollback Strategy
**Category:** Operations
**Value:** MEDIUM
**Source:** carpooling-platform (CarPooling demo)
**Date Discovered:** 2026-03-07

**Problem Solved:**
Need quick rollback before experiments. Git branches feel heavy.

**Solution:**
- Quick `.tar.gz` snapshots with version tags
- Backup manifest tracking
- Faster rollback than git branches
- Includes gitignored files (.env, node_modules)

**Applicability:** Universal (safe experimentation for all businesses)

**Implementation:**
```bash
# .claude/commands/create-backup.md
tar -czf archive/backups/pre-experiment-v1.0.5.tar.gz \
  --exclude='.git' \
  --exclude='node_modules' \
  --exclude='archive' \
  .
```

**Evidence of Success:** Rolled back failed database migration in 30 seconds (vs 5+ minutes with git).

---

### Pattern 10: Architectural Decision Records (ADRs)
**Category:** Intelligence
**Value:** MEDIUM
**Source:** carpooling-platform (CarPooling demo)
**Date Discovered:** 2026-03-07

**Problem Solved:**
6 months later: "Why did we choose PostgreSQL over MongoDB?" Nobody remembers.

**Solution:**
- Lightweight ADR template
- Sequential numbering (001, 002, 003...)
- Documents: Context, Decision, Consequences, Alternatives

**Applicability:** High-value for complex businesses with architectural decisions

**Implementation:**
```
businesses/{business}/
├── decisions/
│   ├── 000-template.md
│   ├── 001-use-postgresql.md
│   ├── 002-event-driven-architecture.md
```

**Template:**
```markdown
# ADR 001: Use PostgreSQL for Primary Database

**Status:** Accepted
**Date:** 2026-03-08
**Deciders:** Development Team

## Context
Need a database for carpooling platform. Requirements: ACID compliance, geospatial queries, scalability.

## Decision
Use PostgreSQL with PostGIS extension.

## Consequences
**Positive:**
- ACID compliance for payment transactions
- PostGIS for route calculations
- Mature ecosystem

**Negative:**
- Horizontal scaling harder than MongoDB
- Requires more DevOps expertise

## Alternatives Considered
- MongoDB: Better horizontal scaling, but lacks ACID
- MySQL: No geospatial support
```

---

### Pattern 11: Session Continuity (Multi-Machine Workflows)
**Category:** Operations
**Value:** HIGH
**Source:** academic-ghostwriting (Centaur)
**Date Discovered:** 2026-03-07

**Problem Solved:**
Same as Pattern 1 (Two-PC Continuity System). Listed separately in original docs but same solution.

**See:** Pattern 1

---

### Pattern 12: Reversible Operations (Archive-First)
**Category:** Safety
**Value:** MEDIUM
**Source:** academic-ghostwriting (Centaur)
**Date Discovered:** 2026-03-07

**Problem Solved:**
Same as Pattern 5 (Trash-Can Pattern). Listed separately in original docs but same solution.

**See:** Pattern 5

---

## How to Add New Patterns

### 1. Discover Pattern in Your Business
Work on your business, solve a problem in a clever way.

### 2. Document in LEARNINGS.md
Add to your business's `LEARNINGS.md`:
```markdown
## Pattern: [Name]
**Problem:** [What problem did this solve?]
**Solution:** [How did you solve it?]
**Evidence:** [Proof it works - metrics, examples]
```

### 3. Extract to Template (Manual or Automated)
Option A: Run `python _template/sync-learnings.py` (auto-scan all businesses)
Option B: Run `python _template/extract-pattern.py businesses/your-business/LEARNINGS.md "Pattern Name"`

### 4. Template Updates
Once extracted:
- Added to `PATTERNS_DISCOVERED.md` (this file)
- May create new rule in `.claude/rules/`
- May update project templates
- Synced back to all businesses

### 5. All Businesses Benefit
Next time someone creates a new business or updates rules, they inherit this pattern.

---

## Pattern Metrics

### By Category
- Architecture: 2 patterns
- Automation: 0 patterns (opportunity!)
- Intelligence: 3 patterns
- Operations: 4 patterns
- Safety: 3 patterns

### By Value
- HIGH: 3 patterns (Two-PC Continuity, Autonomous Decisions, Sprint Log)
- MEDIUM: 8 patterns
- LOW: 1 pattern

### By Source Business
- academic-ghostwriting: 10 patterns
- carpooling-platform: 2 patterns

**Insight:** Academic ghostwriting has contributed most patterns because it's been actively developed. CarPooling is next. As more businesses are created, this registry will grow.

---

## Next Patterns to Discover

**Gaps identified:**
1. **Automation** — No patterns yet for zero-friction automation workflows
2. **Testing** — No patterns for test strategies across businesses
3. **Deployment** — No patterns for CI/CD or deployment strategies
4. **Monitoring** — No patterns for observability and alerting

**Hypothesis:** CarPooling platform will likely discover automation patterns (real-time matching, route optimization pipelines).

---

## Cross-Business Pattern Opportunities

**Pattern combinations that haven't been tried yet:**

1. **Sprint Log + ADRs** → Track sprint decisions in ADR format
2. **Trash-Can + Backup Strategy** → Two-tier safety (trash-can for files, backup for entire state)
3. **Chronicle + Learning Loop** → Chronicle auto-generates from session logs

These are experiments waiting to happen.

---

🌱 **This registry grows with each business.** The more problems you solve, the smarter the whole ecosystem gets.
