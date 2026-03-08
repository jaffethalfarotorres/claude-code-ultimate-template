# Learning Report: Centaur Project Analysis

**Date:** 2026-03-07
**Analyzed Project:** Centaur v4.0 LITE (Academic Ghostwriting Platform)
**Template Version:** v2.1.0 → Proposing v2.2.0
**Analyzer:** template-improver skill

---

## Executive Summary

Centaur is a sophisticated production business system operating a Costa Rican academic ghostwriting service with **9 specialized AI solvers**, **autonomous maintenance**, and **two-PC continuity**. The project reveals **8 innovative patterns** that would significantly enhance the Claude Code template for real-world multi-session, multi-machine workflows.

**Key Discovery:** Centaur has solved the **session continuity problem** across machines and time using a unique combination of session logging, persistent memory (SPRINT_LOG.md), and historical narrative (CHRONICLE.md).

---

## Patterns Discovered

### 🌟 Pattern 1: Two-PC Continuity System (HIGH VALUE)

**What it is:**
A protocol for seamless work across multiple machines where Claude Code conversation history is local but the repo is the shared brain.

**How it works:**

```markdown
## Session Protocol (Two-PC Continuity System)

### On Session START (automatic, zero user typing):
1. `git pull` immediately — sync before anything else
2. `AskUserQuestion` tool — two single-select questions:
   - Q1: Which PC? (Corporate / Personal / Other)
   - Q2: Session mode? (Continue last session / Quick task / New feature / Business work)
3. Load context: `git log --oneline -5`, check `.ai/session_logs/` for OPEN logs
4. Create new session log: `.ai/session_logs/YYYY-MM-DD_HH-MM_[personal|corporate].md`
5. Reply with 3-line brief: last thing done, current state, what's pending

### During Session (real-time incremental logging):
Append 1 line after every meaningful action:
```
HH:MM — [what was done / decided / discovered]
```

### On Session CLOSE:
1. Write final summary (3-5 lines)
2. Mark session log: CLOSED
3. Update MEMORY.md with current state + pending items
4. Commit + push session log and MEMORY.md
```

**Why this matters:**
Solves the **biggest pain point** of Claude Code: conversation history doesn't persist across sessions or machines. Git becomes the shared memory system.

**Template Enhancement Proposal:**

1. Add `.ai/session_logs/` directory structure
2. Add `MEMORY.md` template for persistent state tracking
3. Create `/start-session` command that implements this protocol
4. Document two-PC workflow pattern in CLAUDE.md

---

### 🌟 Pattern 2: Autonomous Agent with Decision Framework (HIGH VALUE)

**What it is:**
A unified agent (centaur-agent.md) with clear **autonomous vs. approval-required** decision boundaries documented in frontmatter and decision tables.

**How it works:**

```yaml
---
description: Centaur autonomous maintenance agent. Use this agent for repo audits...
---

## Decision Framework

**Acts Autonomously:**
✅ Reversible archival (parent-child relationship analysis)
✅ Git conflict merges (information-additive)
✅ Empty directory removal
✅ Sprint Log updates
✅ Pattern discovery scans

**Asks for Approval:**
❌ Irreversible deletions
❌ Business logic changes
❌ New feature additions
❌ Revenue-impacting decisions
```

**Why this matters:**
Gives Claude clear guidelines on what it can do without asking vs. what needs approval. Reduces decision paralysis and speeds up workflows.

**Proven Results from Centaur:**
- 147 → 122 files (-17%) in one autonomous session
- 24 orphaned dependencies discovered and archived
- Git conflicts resolved autonomously
- Zero human intervention needed for maintenance tasks

**Template Enhancement Proposal:**

1. Add `decision-framework.md` to `.claude/rules/`
2. Document autonomous vs. approval patterns
3. Create examples of reversible vs. irreversible actions
4. Add to agent skill templates

---

### 🌟 Pattern 3: Sprint Log as Persistent Memory (MEDIUM-HIGH VALUE)

**What it is:**
A living document (`knowledge/SPRINT_LOG.md`) that tracks:
- Current system state (metrics table updated after every audit)
- Recent activity (weekly sprints with detailed actions)
- Backlog of improvements (prioritized proposals)
- Historical decisions (sprint archive)

**How it differs from CHANGELOG:**
CHANGELOG = user-facing version history
SPRINT_LOG = AI-facing operational memory

**Example structure:**

```markdown
## Estado actual del ecosistema

| Proyecto | KB (líneas) | MAPA (entradas) | Última fecha KB | Salud |
|----------|-------------|-----------------|-----------------|-------|
| estadistica | 1.647 | 10 | 2026-02-25 | 🟢 |
| mate-financiera | 846 | 4 | 2026-03-01 | 🟢 |
...

## Backlog de mejoras

| # | Prioridad | Propuesta | Estado | Semana |
|---|-----------|-----------|--------|--------|
| 1 | Media | MAPAs con pocas entradas — expandir | Pendiente | 2026-03-02 |
...

## Historial de sprints

### Sprint 4 — Auditoría semanal (2026-03-02)
**Ejecutor:** Cowork (scheduled task centaur-pm)
**Auditoría completa:** ...
**Correcciones ejecutadas:** ...
**Hallazgos principales:** ...
```

**Why this matters:**
Gives Claude **persistent context** across sessions. When starting a new session, Claude reads SPRINT_LOG to understand current system state without the user explaining everything.

**Template Enhancement Proposal:**

1. Add `SPRINT_LOG.md` template to `knowledge/` directory
2. Document when/how to update it
3. Include in session start protocol (read SPRINT_LOG after git pull)
4. Add `/update-sprint-log` command

---

### 🌟 Pattern 4: Chronicle (Historical Narrative) (MEDIUM VALUE)

**What it is:**
A narrative-style log (`knowledge/CHRONICLE.md`) documenting the **journey** of the project with full context of technical decisions, learnings, and errors.

**Different from SPRINT_LOG:**
- SPRINT_LOG = operational metrics, current state
- CHRONICLE = story of evolution, why decisions were made, lessons learned

**Example entry format:**

```markdown
### CHR-2026-03-02-007: Fase 0 — Commitear archivos base del sistema

**Contexto:**
Jaffeth diseñó Centaur OS v2 en Claude.ai y generó carpeta `claude-code/` con CONTEXT.md, AGENTS.md, PLAN.md. Claude Code leyó estos archivos y ejecutó el upgrade completo.

**Decisión técnica:**
Commitear CURRICULUM_MAP.md + CHRONICLE.md primero — sin dependencias.

**Implementación:**
- Created `knowledge/CURRICULUM_MAP.md` (410 lines)
- Created `knowledge/CHRONICLE.md` (this file)
- Commit message: "feat: knowledge base — CURRICULUM_MAP + CHRONICLE"

**Resultado:**
✅ Knowledge base initialized
✅ Fase 0 complete → Fase 1 enabled

**Aprendizajes:**
Context engineering > prompt engineering — structured files beat verbal instructions

**Errores encontrados:**
None in this phase
```

**Why this matters:**
Captures **why** decisions were made, not just **what** changed. Essential for understanding project evolution and avoiding repeating mistakes.

**Template Enhancement Proposal:**

1. Add `CHRONICLE.md` template
2. Document entry format
3. Clarify difference between SPRINT_LOG (current ops) vs CHRONICLE (historical journey)
4. Add to `.claude/skills/` as a learnings extraction pattern

---

### 🌟 Pattern 5: Trash-Can Pattern (Reversible Cleanup) (MEDIUM VALUE)

**What it is:**
Archive-first approach for cleanup sessions to maintain reversibility and confidence.

**How it works:**

```markdown
**Trash-Can Pattern:**

1. Move questionable files to `archive/trash-can/{category}/`
2. Review the trash-can in a second pass
3. Only do real deletes after review

Never permanently delete without a review step.
```

**Why this matters:**
Reduces fear of autonomous cleanup. Everything can be recovered if the agent makes a mistake.

**Example from Centaur:**
- 24 files moved to `archive/trash-can/mcp-experiments/`
- Reviewed in next session
- Permanently deleted only after human confirmation

**Template Enhancement Proposal:**

1. Add `archive/trash-can/` directory structure
2. Document reversible cleanup workflow
3. Add to `decision-framework.md` as a safe autonomous action
4. Include in cleanup commands/skills

---

### 🌟 Pattern 6: Linked Documentation System (MEDIUM VALUE)

**What it is:**
Every folder has a `README.md` explaining its purpose, acting as a "folder contract."

**How it works:**

```markdown
| Folder | README covers |
|--------|--------------|
| `.ai/` | session logs, historical context, real-client-cases |
| `products/` | 9 Solvers structure, workflow, KB health |
| `knowledge/` | SPRINT_LOG, CHRONICLE, CURRICULUM_MAP purpose and rules |
| `docs/` | documentation index, when to use each file |
| `pipelines/intake/` | material intake workflow, update_kb.py usage |

Rule: When a folder's purpose changes, update its README. Don't let documentation drift.
```

**Why this matters:**
Self-documenting repository structure. Claude can understand folder purpose without asking user.

**Template Enhancement Proposal:**

1. Add `README.md` templates for common folder types
2. Document folder README conventions in `.claude/rules/documentation.md`
3. Add `/audit-readmes` command to check for missing folder docs
4. Include in new project setup workflow

---

### 🌟 Pattern 7: Root Hygiene Rules (LOW-MEDIUM VALUE)

**What it is:**
Strict conventions for what belongs at repository root vs. feature folders.

**Rules from Centaur:**

```markdown
**Root should only contain:**
- README.md, CLAUDE.md, AGENTS.md, VERSIONS.md, LICENSE
- .gitignore, .editorconfig

**Feature docs belong in their feature folder:**
- Scraper docs → `scrapers/`
- Workflow docs → `pipelines/intake/`

**Session artifacts do NOT belong at root:**
- READY_TO_COMMIT.md, SESSION_SUMMARY.md → `archive/trash-can/`

**.ai/ root should only contain:**
- README.md — everything else goes to `session_logs/`, `context/`, or `archive/`
```

**Why this matters:**
Prevents root folder bloat. Keeps repository navigable and professional.

**Template Enhancement Proposal:**

1. Add root hygiene rules to `.claude/rules/git-workflow.md`
2. Create `/audit-root` command to check for violations
3. Document standard root file list
4. Include in autonomous cleanup patterns

---

### 🌟 Pattern 8: Version Consistency Checks (LOW VALUE)

**What it is:**
Automated checks that all documentation references match the same version number.

**How it works:**

```bash
# Check all locations that reference agent version
grep -r "centaur-agent v[0-9]" --include="*.md"
grep -r "Centaur Unified Agent v[0-9]" --include="*.md"

# Flag MEDIUM if they don't match
# Source of truth: `.claude/agents/centaur-agent.md` header
```

**Rule from Centaur:**
When bumping version, ALL reference updates MUST be in the same commit to prevent drift.

**Why this matters:**
Prevents documentation version drift. Ensures consistency across all docs.

**Template Enhancement Proposal:**

1. Add version consistency check to `/review` command
2. Document version bump procedure in git-workflow.md
3. Add automated check script
4. Include in PR review checklist

---

## Business-Specific Patterns (Not Generalizable)

These patterns are specific to Centaur's academic ghostwriting business and wouldn't fit a general template:

- ❌ 9 Academic Solver structure (product-specific)
- ❌ MAPA.md university mapping (domain-specific)
- ❌ Spanish-CR language architecture (market-specific)
- ❌ KB.md knowledge base format (business-specific)
- ❌ WhatsApp message parsing (workflow-specific)
- ❌ Notion CRM integration (tool-specific)
- ❌ Chrome scraper integration (use-case specific)

---

## Recommended Template Enhancements

### Priority 1: HIGH VALUE (Implement in v2.2.0)

1. **Two-PC Continuity System**
   - Add `.ai/session_logs/` directory
   - Add `MEMORY.md` template
   - Create `/start-session` command
   - Document in CLAUDE.md

2. **Autonomous Agent Decision Framework**
   - Add `.claude/rules/decision-framework.md`
   - Document autonomous vs. approval patterns
   - Include in agent skill templates
   - Add decision table examples

3. **Sprint Log Pattern**
   - Add `SPRINT_LOG.md` template to `knowledge/`
   - Document update conventions
   - Include in session protocol
   - Add `/update-sprint-log` command

### Priority 2: MEDIUM VALUE (Consider for v2.3.0)

4. **Chronicle Pattern**
   - Add `CHRONICLE.md` template
   - Document entry format
   - Clarify vs. SPRINT_LOG difference

5. **Trash-Can Pattern**
   - Add `archive/trash-can/` structure
   - Document reversible cleanup workflow
   - Include in cleanup commands

6. **Linked Documentation System**
   - Add folder README templates
   - Document conventions
   - Add `/audit-readmes` command

7. **Root Hygiene Rules**
   - Add to git-workflow.md
   - Create `/audit-root` command
   - Document standard root file list

### Priority 3: LOW VALUE (Nice to have)

8. **Version Consistency Checks**
   - Add to `/review` command
   - Document version bump procedure
   - Add automated check script

---

## Files to Create/Modify for v2.2.0

### New Files

```
.ai/
├── session_logs/
│   └── .gitkeep
└── MEMORY.md (template)

knowledge/
├── SPRINT_LOG.md (template)
└── CHRONICLE.md (template)

.claude/
├── commands/
│   ├── start-session.md (NEW)
│   ├── update-sprint-log.md (NEW)
│   └── audit-root.md (NEW)
└── rules/
    └── decision-framework.md (NEW)

archive/
└── trash-can/
    └── .gitkeep
```

### Modified Files

```
CLAUDE.md
- Add Two-PC Continuity section
- Reference new patterns
- Document session protocol

README.md
- Add "Session Continuity" section
- Document autonomous agent patterns
- Reference SPRINT_LOG and CHRONICLE

.claude/rules/git-workflow.md
- Add root hygiene rules
- Add version consistency conventions

.claude/rules/documentation.md
- Add linked documentation system
- Add folder README conventions

TEMPLATE_EVOLUTION.md
- Add Centaur learning entry
- Document v2.1.0 → v2.2.0 evolution
```

---

## Attribution

**Original Project:** Centaur v4.0 LITE
**Author:** Jaffeth Alfaro Torres
**Repository:** https://github.com/jaffethalfarotorres/Centaur
**Analyzed:** 2026-03-07

**Key Innovations:**
- Two-PC continuity protocol
- Autonomous agent decision framework
- Sprint Log as persistent memory
- Chronicle as historical narrative
- Trash-can reversible cleanup pattern

**Template Benefit:**
These patterns solve **real-world pain points** discovered through production use of an AI-assisted business system operating across multiple machines and sessions.

---

## Next Steps

1. ✅ Learning report generated
2. ⏭️ Propose changes to template maintainer (Jaffeth)
3. ⏭️ Implement Priority 1 patterns in v2.2.0
4. ⏭️ Update TEMPLATE_EVOLUTION.md
5. ⏭️ Test patterns in new projects
6. ⏭️ Gather feedback from community

---

**Template Evolution Philosophy:**

> "The best templates are learned from production systems, not imagined in isolation."

Centaur demonstrates that **real-world usage patterns** are more valuable than theoretical best practices. This learning report extracts 8 generalizable patterns from a production business system that can improve the template for everyone.

🌱 → 🌳 **The template grows from the projects that use it!**
