# Machine-First Architecture Rules

> **Philosophy:** Design for computers first, humans second. Structure optimized for Claude.ai, APIs, and automation.

## Purpose-Driven Naming Convention

**Rule:** Names describe WHAT IT DOES, not what domain it belongs to.

### ✅ Good Examples (Purpose-Driven)
- `data-analysis` — Analyzes datasets (not "statistics")
- `financial-modeling` — Models financial scenarios (not "math-finance")
- `algebra-solver` — Solves algebra problems (not "general-math")
- `optimization-modeling` — Optimizes systems (not "operations-research")
- `financial-reporting` — Produces financial reports (not "accounting")

### ❌ Bad Examples (Domain-Driven)
- `estadistica` — What is this? Statistics? Spanish? Confusing.
- `mate-financiera` — Subject name, not purpose
- `io` — Acronym (IO = Investigación de Operaciones, but unclear)
- `contabilidad` — Domain in Spanish (fails computer-first test)

### Why Purpose > Domain?
1. **Future-proof:** `academic-writing` can handle APA, IEEE, Chicago. Name stays correct. `estilo-apa` would be wrong if we added IEEE.
2. **Self-documenting:** `mechanics-solver` tells you exactly what it does
3. **Searchable:** Grep for `*-solver` finds all solvers instantly
4. **Cross-language:** English is universal for APIs, tools, documentation

---

## Flat Structure Convention

**Rule:** Max 2 levels deep. No arbitrary categorization.

### ✅ Good Structure (Flat)
```
project-root/
├── data-analysis/
├── financial-modeling/
├── algebra-solver/
├── optimization-modeling/
└── _shared/
```
- 1 click to navigate
- Alphabetical sorting works naturally
- Easy to glob: `*-solver/`, `*-modeling/`

### ❌ Bad Structure (Nested)
```
project-root/
└── products/
    ├── solver-analytical/
    │   ├── estadistica/
    │   └── mate-financiera/
    ├── solver-symbolic/
    │   ├── fisica/
    │   └── mate-general/
    └── solver-systems/
        ├── io/
        └── ingenieria-civil/
```
- 3 clicks to navigate
- Arbitrary categories (is finance "analytical" or "systems"?)
- Categories add no value, only friction

### Why Flat > Nested?
1. **Speed:** 1-click vs 3-click navigation
2. **Clarity:** No mental model needed ("Where does X belong?")
3. **Tool-friendly:** GitHub connector, file watchers, glob patterns all work better

---

## English-Only Naming

**Rule:** All paths, folders, files in English with ASCII characters.

### ✅ Good
- `financial-reporting/knowledge.md`
- `data-analysis/history.md`
- `optimization-modeling/role.md`

### ❌ Bad
- `contabilidad/KB.md` (Spanish + acronym)
- `estadística/MAPA.md` (Spanish + Spanish acronym)
- `física/config.md` (accented character breaks some tools)

### Why English-Only?
1. **Cross-platform:** Works on Windows, Mac, Linux without encoding issues
2. **API-friendly:** REST APIs, URLs, JSON keys all expect ASCII
3. **Universal:** International teams, documentation, StackOverflow
4. **Tool compatibility:** Some tools break on non-ASCII paths

---

## Predictable Patterns

**Rule:** Use consistent suffixes for similar purposes.

### Solver Pattern
```
{purpose}-solver/
├── knowledge.md
├── role.md
└── history.md
```

Examples: `algebra-solver/`, `mechanics-solver/`

### Modeling Pattern
```
{domain}-modeling/
├── knowledge.md
├── role.md
└── history.md
```

Examples: `financial-modeling/`, `optimization-modeling/`

### Reporting Pattern
```
{output}-reporting/
├── knowledge.md
├── role.md
└── history.md
```

Examples: `financial-reporting/`, `academic-writing/`

### Why Predictable?
1. **Glob-friendly:** `ls *-solver` finds all solvers
2. **Pattern recognition:** Humans and computers learn faster
3. **Automation-ready:** Scripts can detect types by pattern

---

## Standard Folder Conventions

### `_shared/` — Cross-Module Shared Knowledge
```
_shared/
├── universities.md
├── professors.md
├── courses.md
└── citations.md
```
- Single source of truth
- Deduplicated data
- Shared by all modules

### `_meta/` — Self-Improvement Intelligence
```
_meta/
├── knowledge-graph.md
├── routing-rules.md
└── naming-evolution.md
```
- Auto-generated insights
- Cross-module intelligence
- System learns patterns

### `pipelines/intake/` — Zero-Friction Automation
```
pipelines/intake/
├── inbox/          # Drop files here
├── processed/      # Archived by date
├── outbox/         # Solutions appear here
└── process-inbox.py
```
- Drop files → Auto-process → Grab output
- No manual commands required

### `archive/` — Reversible Operations
```
archive/
├── v3.6-automation/
├── v4.0-lite/
└── trash-can/      # Review before deleting
```
- Archive-first cleanup
- Reversible operations
- Confidence in autonomous actions

---

## File Naming Standards

**Rule:** No acronyms. Clear purpose in filename.

### ✅ Good
- `knowledge.md` — Clear, describes content
- `role.md` — Describes what this defines
- `history.md` — Learning history

### ❌ Bad
- `KB.md` — Acronym (Knowledge Base)
- `config.md` — Vague (config for what?)
- `MAPA.md` — Spanish acronym (unclear)

### Why No Acronyms?
1. **Searchability:** Grep for "knowledge" finds it
2. **Clarity:** New contributors understand immediately
3. **Self-documenting:** No need to explain "KB means Knowledge Base"

---

## Learning Loop Requirements

**Every project MUST have these 4 components:**

### 1. Inbox Folder
Drop zone for new knowledge (files, data, assignments)

### 2. Classification System
Route files to correct module based on keywords/content

### 3. Extraction Mechanism
Update `knowledge.md` files from processed content

### 4. Archive System
Processed files moved to `processed/{date}/`

### ✅ Complete Learning Loop
```
inbox/ → classify → extract → update knowledge.md → archive
```

### ❌ Broken Learning Loop
If your scripts still reference old names (v4.x paths), the learning loop is BROKEN.

**Example of broken:**
```python
# ❌ BROKEN: Still references old v4.x structure
PROJECTS = {
    "mate-general": "solver-symbolic/mate-general"  # Doesn't exist!
}
```

**Fixed:**
```python
# ✅ FIXED: References v5.0 structure
PROJECTS = {
    "algebra-solver": "algebra-solver"  # Correct!
}
```

---

## Validation Checklist

Use this checklist to validate if a project follows machine-first architecture:

- [ ] **All folder names in English?** (no Spanish, no accents)
- [ ] **All folder names purpose-driven?** (not domain names)
- [ ] **Structure is flat?** (max 2 levels deep)
- [ ] **No acronyms in file names?** (`knowledge.md` not `KB.md`)
- [ ] **Has `_shared/` folder?** (single source of truth)
- [ ] **Has `_meta/` folder?** (self-improvement layer)
- [ ] **Has `pipelines/intake/` folder?** (zero-friction automation)
- [ ] **Scripts use current names?** (not v4.x legacy names)
- [ ] **Learning loop works?** (inbox → classify → extract → archive)
- [ ] **Glob patterns work?** (`*-solver`, `*-modeling`, etc.)

---

## Migration Strategy

### When Renaming Existing Projects

**1. Update folder structure:**
```bash
mv estadistica data-analysis
mv mate-financiera financial-modeling
# etc.
```

**2. Update file names:**
```bash
cd data-analysis
mv KB.md knowledge.md
mv config.md role.md
mv MAPA.md history.md
```

**3. Update ALL scripts that reference old names:**
```bash
# Find all broken references:
grep -r "mate-general" --include="*.py"
grep -r "products/" --include="*.py"
grep -r "KB.md" --include="*.py"

# Fix each one
```

**4. Update documentation:**
- README.md
- CLAUDE.md
- Agent instructions
- Command files

**5. Test learning loop:**
```bash
# Drop test file in inbox
# Verify it gets classified correctly
# Verify knowledge.md gets updated
# Verify file gets archived
```

---

## Anti-Patterns to Avoid

### ❌ "We might need categories later"
- Start flat. Add nesting only when you have 50+ modules and clear grouping emerges from usage patterns.

### ❌ "But the domain name is clearer to humans"
- Optimize for computers first. `financial-modeling` is clear to both humans AND machines.

### ❌ "Let's keep some acronyms for brevity"
- Brevity < Clarity. `knowledge.md` is 3 characters longer than `KB.md` but infinitely clearer.

### ❌ "Spanish is fine, we're all Spanish speakers"
- Today you are. Tomorrow you hire internationally, use APIs, integrate tools. Start universal.

### ❌ "We'll fix the scripts later"
- Scripts breaking = learning loop broken = system doesn't improve = technical debt compounds.

---

## Version History

- **v1.0 (2026-03-08):** Extracted from Centaur v5.0 migration
- Based on: Real production system (9 solvers, 2 PCs, autonomous agent)
- Proven: 100% routing accuracy, zero-friction automation working

---

**This is a living document.** Update as patterns emerge from actual usage.
