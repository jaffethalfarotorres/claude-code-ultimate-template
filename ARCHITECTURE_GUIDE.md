# Machine-First Architecture Guide

> **Build systems optimized for Claude.ai and AI agents, not human mental models.**

## The Core Insight

**Traditional approach:** Design for human understanding → adapt for computers
**Machine-first approach:** Design for computer processing → humans understand naturally

**Result:** Systems that are BOTH easier for AI to navigate AND clearer for humans.

---

## The 3 Pillars

### 1. **Purpose-Driven Naming**
Names describe WHAT IT DOES, not what subject it covers.

**Why?**
- Future-proof (scope can expand without renaming)
- Self-documenting (no guessing what "IO" means)
- Search-friendly (grep for `*-solver` finds all solvers)

**Examples:**
- `data-analysis` not `estadistica` (purpose > domain)
- `financial-modeling` not `mate-financiera` (English > Spanish)
- `optimization-modeling` not `io` (clear > acronym)

### 2. **Zero-Friction Automation**
If it needs a manual command, it has friction.

**Why?**
- Forgotten steps = broken learning loop
- Manual operations = inconsistent execution
- Friction = resistance to using the system

**Implementation:**
- File watchers (drop files → auto-process)
- Background processes (runs while you sleep)
- Git-based sync (shared brain across machines)

### 3. **Self-Improving Systems**
Every file processed teaches the system something new.

**Why?**
- Static knowledge = code, not intelligence
- Learning from usage = continuously better
- Self-optimization = less maintenance

**Implementation:**
- Extract formulas from assignments → update knowledge.md
- Learn keywords from filenames → improve routing
- Track patterns → build knowledge graph

---

## Quick Start: Apply Machine-First to Any Project

### Step 1: Audit Current State
```bash
# Check for anti-patterns:
find . -name "*.md" | grep -E "(KB|config|MAPA)"  # Acronyms?
find . -type d -name "*[áéíóú]*"  # Non-ASCII?
find . -type d | awk -F/ '{print NF-1}' | sort -rn | head -1  # Nesting depth?

# If you found issues → migrate to machine-first
```

### Step 2: Choose Template
```
business-automation/  → For solver-based systems (Centaur-like)
web-app/             → For SaaS/web applications
data-pipeline/       → For ETL/analytics projects
```

### Step 3: Apply Architecture Rules
```bash
# Link to centralized rules:
ln -s ../../Claude/.claude/rules .claude/rules

# Now ALL architecture rules inherited automatically
```

### Step 4: Migrate Modules
```bash
# Rename folders (domain → purpose):
mv estadistica data-analysis
mv mate-financiera financial-modeling

# Rename files (acronyms → clear names):
cd data-analysis
mv KB.md knowledge.md
mv config.md role.md
mv MAPA.md history.md
```

### Step 5: Fix Scripts
```bash
# Find broken references:
grep -r "estadistica" --include="*.py"
grep -r "KB.md" --include="*.py"

# Update to new names
```

### Step 6: Test Learning Loop
```bash
# Drop test file in inbox
# Verify: classified → extracted → archived
# If broken → fix scripts, test again
```

---

## Architecture Patterns

### Pattern 1: Solver-Based Business
**Use case:** Process different types of work (assignments, reports, analysis)

**Structure:**
```
project/
├── data-analysis/       # Solves statistics problems
├── financial-modeling/  # Models financial scenarios
├── algebra-solver/      # Solves algebra
├── _shared/             # Shared knowledge
├── _meta/               # Self-improvement
└── pipelines/intake/    # Zero-friction automation
```

**Example:** Centaur (academic ghostwriting), consulting services, specialized agencies

### Pattern 2: Pipeline-Based System
**Use case:** Data flows through stages (ETL, processing, analysis)

**Structure:**
```
project/
├── data-ingestion/      # Brings data in
├── data-cleaning/       # Cleans/validates
├── data-transform/      # Transforms format
├── data-analysis/       # Analyzes patterns
├── data-export/         # Exports results
├── _shared/             # Common schemas
└── pipelines/           # Orchestration
```

**Example:** Analytics platforms, data warehouses, ML pipelines

### Pattern 3: Service-Based Architecture
**Use case:** Multiple independent services (microservices, SaaS modules)

**Structure:**
```
project/
├── user-authentication/
├── payment-processing/
├── notification-delivery/
├── analytics-tracking/
├── _shared/             # Shared utilities
└── _meta/               # Service dependencies
```

**Example:** SaaS platforms, marketplaces, multi-tenant applications

---

## Migration Strategies

### Strategy 1: Big Bang (Recommended for Small Projects)
**When:** <10 modules, <1000 files, greenfield or early-stage

**Approach:**
1. Create branch: `git checkout -b machine-first-migration`
2. Rename ALL modules in one session
3. Update ALL scripts
4. Test thoroughly
5. Merge when 100% working

**Time:** 2-4 hours
**Risk:** Low (all-at-once, easier to test)

### Strategy 2: Incremental (Recommended for Large Projects)
**When:** >10 modules, >1000 files, production system

**Approach:**
1. Migrate 1-2 modules per week
2. Use aliases for backward compatibility:
   ```python
   PROJECTS = {
       "algebra-solver": "algebra-solver",  # v5.0
       "mate-general": "algebra-solver",     # v4.x alias
   }
   ```
3. Deprecate old names after 30 days
4. Remove aliases when usage = 0

**Time:** 4-8 weeks
**Risk:** Low (gradual, production stays running)

### Strategy 3: Copy Template (Recommended for New Projects)
**When:** Starting fresh

**Approach:**
1. `cp -r Claude/PROJECT_TEMPLATES/business-automation/ MyProject/`
2. Link rules: `ln -s ../Claude/.claude/rules .claude/rules`
3. Customize for your business
4. Start using immediately

**Time:** 30 minutes
**Risk:** Zero (no migration, just customization)

---

## Real-World Example: Centaur Migration

### Before (v4.x)
```
Centaur/
└── products/
    ├── solver-analytical/
    │   ├── estadistica/
    │   │   ├── KB.md (Spanish + acronym)
    │   │   ├── config.md (vague)
    │   │   └── MAPA.md (Spanish acronym)
    │   └── mate-financiera/
    │       └── ... (same issues)
    └── solver-symbolic/
        ├── fisica/
        └── mate-general/
            └── ... (same issues)
```

**Problems:**
- 3-click navigation (`products/` → `solver-symbolic/` → `fisica/`)
- Spanish names (non-universal)
- Acronyms (unclear)
- Arbitrary categories (is finance "analytical" or "systems"?)
- Scripts broke when structure changed

### After (v5.0)
```
Centaur/
├── data-analysis/       # Was: estadistica
│   ├── knowledge.md     # Was: KB.md
│   ├── role.md          # Was: config.md
│   └── history.md       # Was: MAPA.md
├── financial-modeling/  # Was: mate-financiera
├── algebra-solver/      # Was: mate-general
├── mechanics-solver/    # Was: fisica
├── _shared/             # NEW: Deduplicated knowledge
├── _meta/               # NEW: Self-improvement layer
└── pipelines/intake/    # NEW: Zero-friction automation
```

**Benefits:**
- 1-click navigation (all at root level)
- English names (universal)
- Purpose-driven (clear what each does)
- Flat structure (no arbitrary categories)
- Scripts validated, learning loop working

**Metrics:**
- Navigation: 3 clicks → 1 click (-66%)
- Classification accuracy: 100% (7/7 test files)
- Learning loop: Broken → Fixed
- Routing keywords: Auto-updated from filenames

---

## Common Pitfalls & Solutions

### Pitfall 1: "But my team knows the old names"
**Problem:** Resistance to change
**Solution:** Old names were domain-specific (only your team knows). New names are self-documenting (anyone understands).

**Example:**
- Old: "IO" → Only your team knows this means "Investigación de Operaciones"
- New: "optimization-modeling" → Everyone understands immediately

### Pitfall 2: "Categories help organize"
**Problem:** Arbitrary categories add friction
**Solution:** Let PURPOSE create natural grouping. Use glob patterns instead.

**Example:**
```bash
# Instead of products/solver-analytical/ folder:
ls *-analysis  # Finds: data-analysis, customer-analysis
ls *-modeling  # Finds: financial-modeling, optimization-modeling
```

### Pitfall 3: "Renaming breaks everything"
**Problem:** Scripts reference old names
**Solution:** Fix scripts FIRST, test thoroughly, THEN merge.

**Checklist:**
```bash
# Find ALL references:
grep -r "old-name" --include="*.py" --include="*.md"

# Update each one
# Test learning loop end-to-end
# Only merge when 100% working
```

### Pitfall 4: "English is harder for non-English speakers"
**Problem:** Team prefers Spanish
**Solution:** Machine-first ≠ human-last. English is EASIER for:
- APIs (all use English)
- Tools (GitHub, VSCode, etc.)
- Documentation (StackOverflow, docs)
- International collaboration

**Result:** Team learns universal terminology, system works with all tools.

---

## Validation & Quality Gates

### Automated Validation
```bash
# Run validation script:
python Claude/VALIDATION.py

# Checks:
# ✓ All folder names ASCII (no accents)
# ✓ All folder names English
# ✓ Purpose-driven naming pattern
# ✓ Flat structure (max 2 levels)
# ✓ No acronyms in filenames
# ✓ Learning loop functional
# ✓ Scripts reference current names
```

### Manual Review Checklist
- [ ] Can a new developer understand module names without asking?
- [ ] Does `ls *-solver` find all solvers?
- [ ] Drop test file in inbox → processed correctly?
- [ ] Knowledge.md updated from test file?
- [ ] Can explain system architecture in <2 minutes?

---

## Success Metrics

### Quantitative
- **Navigation clicks:** Before → After (target: <2 clicks)
- **Classification accuracy:** % files routed correctly (target: >95%)
- **Learning loop uptime:** Days without manual intervention (target: 30+)
- **Knowledge growth:** Formulas added per month (target: >0)

### Qualitative
- **"How does this work?"** → Obvious from names
- **"Where does X go?"** → Clear from purpose-driven name
- **"Is the system learning?"** → Check history.md, see entries
- **"Can I trust automation?"** → Drop files, grab results, never think about it

---

## Next Steps

1. **Read architecture rules:** `.claude/rules/machine-first.md`
2. **Audit your project:** Run `VALIDATION.py`
3. **Choose migration strategy:** Big bang vs incremental
4. **Execute migration:** Rename → Update scripts → Test → Merge
5. **Validate learning loop:** Drop test files, verify knowledge grows
6. **Monitor metrics:** Track navigation, accuracy, growth

**Remember:** Machine-first architecture makes life easier for BOTH computers AND humans.

---

## Resources

- **Architecture Rules:** `.claude/rules/`
  - `machine-first.md` — Naming, structure, patterns
  - `zero-friction.md` — Automation philosophy
  - `self-improving.md` — Learning loop design

- **Project Templates:** `PROJECT_TEMPLATES/`
  - `business-automation/` — Solver-based systems
  - (More coming: `web-app/`, `data-pipeline/`)

- **Validation:** `VALIDATION.py` — Check if project follows rules

- **Examples:**
  - `Projects/Centaur/` — v5.0 production system
  - `Projects/CarPooling/` — Demo application

---

**Guide Version:** 1.0 (2026-03-08)
**Author:** Jaffeth Alfaro Torres + Claude
**Philosophy:** Computers first → Humans understand naturally
