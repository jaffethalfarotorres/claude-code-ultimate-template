# Cross-Business Pattern Discovery & Propagation

**Purpose:** Enable businesses to learn from each other without interfering with each other.

**Vision:** Your GitHub workspace is a **self-improving ecosystem** where each business evolves independently but teaches all others through pattern discovery.

---

## The Core Concept

```
┌─────────────────────────────────────────────────────────────┐
│                    VIBE CODING WORKFLOW                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Monday morning (high energy):                              │
│  → Work on carpooling-platform                              │
│  → Discover clever caching pattern for route optimization   │
│                                                              │
│  Tuesday afternoon (analytical mood):                       │
│  → Work on academic-ghostwriting                            │
│  → Discover pattern for handling multi-format exports       │
│                                                              │
│  Wednesday (want to experiment):                            │
│  → Work in sandbox/ on new idea                             │
│  → No rules, just play                                      │
│                                                              │
│  Friday (review mode):                                      │
│  → Run sync-learnings.py                                    │
│  → Caching pattern from carpooling → Exported to template   │
│  → Multi-format pattern from ghostwriting → Exported        │
│  → BOTH businesses now have BOTH patterns                   │
│  → New business next week inherits ALL accumulated wisdom   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Result:** Compound learning. Each business makes the whole ecosystem smarter.

---

## The Learning Flow

### Step 1: Discovery (Happens Naturally)
You're working on a business, solving problems. You create something clever.

**Examples:**
- academic-ghostwriting: "Two-PC continuity system using git as shared brain"
- carpooling-platform: "Route optimization caching with geospatial indexing"
- future-invoicing-tool: "Multi-currency handling with real-time exchange rates"

### Step 2: Documentation (In Your Business)
Document the pattern in your business's `LEARNINGS.md`:

```markdown
# businesses/carpooling-platform/LEARNINGS.md

## Pattern: Route Optimization Caching
**Category:** Performance
**Date Discovered:** 2026-03-08
**Problem:** Same routes calculated repeatedly (waste of compute)

**Solution:**
- Cache route calculations with composite key: (origin, destination, time_of_day)
- Invalidate cache after 15 minutes (traffic changes)
- Use Redis for sub-millisecond lookup

**Implementation:**
```python
# route-optimizer/cache.py
def get_cached_route(origin, destination, time_of_day):
    cache_key = f"route:{origin}:{destination}:{time_of_day}"
    cached = redis.get(cache_key)
    if cached:
        return json.loads(cached)

    # Calculate route
    route = calculate_optimal_route(origin, destination, time_of_day)

    # Cache for 15 minutes
    redis.setex(cache_key, 900, json.dumps(route))
    return route
```

**Evidence of Success:**
- Route calculation time: 450ms → 12ms (97% reduction)
- Server load: 80% → 35%
- Tested with 1000 requests/minute

**Generalizability:** HIGH
- Can apply to any business with expensive repeated calculations
- Academic ghostwriting: Cache citation formatting
- Future invoice tool: Cache tax calculations
```

### Step 3: Extraction (Manual or Automated)

#### Option A: Automated (Recommended)
```bash
# From template directory
python sync-learnings.py
```

This script:
1. Scans all `businesses/*/LEARNINGS.md` files
2. Identifies new patterns (not in `PATTERNS_DISCOVERED.md`)
3. Extracts generalizable patterns
4. Updates template rules/documentation
5. Syncs updated rules back to all businesses
6. Creates audit trail

#### Option B: Manual
```bash
# Extract specific pattern from one business
python extract-pattern.py businesses/carpooling-platform/LEARNINGS.md "Route Optimization Caching"
```

### Step 4: Template Integration
Once extracted, the pattern gets integrated into the template:

**Possible outcomes:**
1. **Added to pattern registry** → `PATTERNS_DISCOVERED.md` (always)
2. **New rule created** → `.claude/rules/caching-strategies.md` (if major pattern)
3. **Template updated** → `PROJECT_TEMPLATES/saas-platform/` includes caching example
4. **Guide created** → `guides/caching-best-practices.md` (if complex)

### Step 5: Propagation (Automatic)
`sync-learnings.py` syncs updated rules back to all businesses:

```bash
# Updates all businesses automatically
businesses/academic-ghostwriting/.claude/rules/ ← Updated
businesses/carpooling-platform/.claude/rules/ ← Updated
businesses/future-invoice-tool/.claude/rules/ ← Updated (when created)
```

**Result:** All businesses now know about route optimization caching pattern, even if they don't use it yet.

---

## Pattern Categories & Thresholds

### When to Extract a Pattern

**✅ Extract if:**
- Solved a non-trivial problem (>1 hour to figure out)
- Generalizable to other businesses (not business-specific logic)
- Has measurable evidence of success (metrics, test results)
- You'd want this pattern in your next business

**❌ Don't extract if:**
- Business-specific logic (e.g., "Formula for calculating ghostwriting price per page")
- Trivial solution (e.g., "Use a for loop")
- Not proven yet (no evidence it works)
- Already exists in pattern registry

### Pattern Categories

1. **Architecture** — Folder structure, naming, organization
2. **Automation** — Zero-friction workflows, pipelines
3. **Intelligence** — Learning loops, knowledge extraction
4. **Operations** — Backups, decisions, session continuity
5. **Safety** — Reversible operations, validation
6. **Performance** — Caching, optimization, scaling
7. **Integration** — APIs, webhooks, third-party services
8. **Testing** — Test strategies, mocking, fixtures
9. **Deployment** — CI/CD, environments, rollback
10. **Monitoring** — Logging, alerting, observability

### Pattern Value Levels

**HIGH** — Universal benefit, solves major pain point
- Examples: Two-PC continuity, autonomous decision framework

**MEDIUM** — Useful for many businesses, improves workflows
- Examples: Trash-can pattern, ADRs, backup strategy

**LOW** — Nice to have, optional
- Examples: Version consistency checks

---

## Business Independence (No Interference)

### Each Business Has Own Git Repo

```bash
# Each business is independent
cd businesses/academic-ghostwriting
git status  # Own repo, own commits, own remote

cd businesses/carpooling-platform
git status  # Different repo, different history
```

**Why:** Can deploy, version, and manage separately.

### Shared Architecture Rules (Via Template)

```bash
# But all share same architecture rules
businesses/academic-ghostwriting/.claude/rules/  # Copied from template
businesses/carpooling-platform/.claude/rules/    # Same rules
```

**Why:** Consistent patterns across all businesses, but implementation is independent.

### Knowledge Stays Local, Patterns Go Global

**Local (stays in business):**
- Domain knowledge (formulas, business logic)
- Customer data (private)
- Business-specific configs

**Global (shared via template):**
- Architecture patterns
- Automation strategies
- Best practices
- Tool configurations

---

## Vibe Coding: Switch Without Friction

### The Problem (Before Machine-First)
```
Monday: Work on Centaur
- Folder: products/solver-analytical/estadistica/
- Files: KB.md, config.md, MAPA.md
- Spanish naming, nested structure

Tuesday: Work on CarPooling
- Folder: src/services/matching/
- Files: README.md, config.js
- English naming, different structure

Result: Mental context switch. Different patterns. Confusing.
```

### The Solution (After Machine-First)
```
Monday: Work on academic-ghostwriting
- Folder: businesses/academic-ghostwriting/data-analysis/
- Files: knowledge.md, role.md, history.md
- Purpose-driven naming, flat structure

Tuesday: Work on carpooling-platform
- Folder: businesses/carpooling-platform/user-matching/
- Files: knowledge.md, role.md, history.md
- Same naming, same structure

Result: Zero mental context switch. Same patterns. Instant familiarity.
```

**Benefits:**
- Switch projects based on mood/energy (vibe coding)
- Same folder patterns across all businesses
- Same automation patterns (inbox/, outbox/)
- Same documentation patterns (CLAUDE.md, SPRINT_LOG.md)

---

## Cross-Business Pattern Examples

### Example 1: Caching Pattern

**Discovered in:** carpooling-platform (route optimization caching)

**Extracted to:** `PATTERNS_DISCOVERED.md` + `.claude/rules/caching-strategies.md`

**Applied to:**
- academic-ghostwriting: Cache citation formatting (APA, IEEE) — Don't reformat same source twice
- future-invoice-tool: Cache tax calculations per country — Tax rules don't change hourly

**Result:** 3 businesses benefit from 1 discovery.

---

### Example 2: Multi-Format Export

**Discovered in:** academic-ghostwriting (export solutions as PDF, DOCX, LaTeX)

**Extracted to:** `PATTERNS_DISCOVERED.md` + template example code

**Applied to:**
- carpooling-platform: Export reports as PDF, Excel, CSV
- future-invoice-tool: Export invoices as PDF, XML (for accounting software)

**Pattern:**
```python
# _shared/export_manager.py
class ExportManager:
    def __init__(self):
        self.exporters = {
            'pdf': PDFExporter(),
            'docx': DocxExporter(),
            'latex': LaTeXExporter(),
        }

    def export(self, content, format):
        if format not in self.exporters:
            raise ValueError(f"Unknown format: {format}")
        return self.exporters[format].export(content)
```

**Result:** All businesses handle multi-format export the same way. Consistent, predictable.

---

### Example 3: Two-PC Continuity

**Discovered in:** academic-ghostwriting (work from home PC + laptop)

**Extracted to:** `PATTERNS_DISCOVERED.md` (Pattern 1)

**Applied to:**
- carpooling-platform: Developer works from office + home
- future-invoice-tool: Same developer, same workflow

**Pattern:**
- `.ai/session_logs/` for real-time logging
- `knowledge/MEMORY.md` for current state
- Git commits preserve session logs
- MEMORY.md tracked in git

**Result:** Every business supports multi-machine workflow automatically.

---

## Automation: sync-learnings.py

### What It Does
Scans all businesses → Extracts new patterns → Updates template → Syncs back to all businesses

### When to Run
- **Weekly:** Scheduled sync (cron job or GitHub Actions)
- **Manual:** After major discovery (run `python _template/sync-learnings.py`)
- **Pre-deployment:** Before creating new business (ensures latest patterns)

### How It Works

```python
# Pseudocode for sync-learnings.py

def sync_learnings():
    # Step 1: Scan all businesses
    businesses = glob("businesses/*/LEARNINGS.md")
    all_patterns = []

    for business in businesses:
        patterns = extract_patterns(business)
        all_patterns.extend(patterns)

    # Step 2: Identify new patterns (not in registry)
    registry = load_registry("_template/PATTERNS_DISCOVERED.md")
    new_patterns = [p for p in all_patterns if p not in registry]

    # Step 3: Update registry
    for pattern in new_patterns:
        add_to_registry(pattern)

    # Step 4: Update rules if needed
    for pattern in new_patterns:
        if pattern.value == "HIGH":
            create_rule_file(pattern)

    # Step 5: Update project templates
    update_templates(new_patterns)

    # Step 6: Sync back to all businesses
    for business in businesses:
        copy_rules("_template/.claude/rules/", f"{business}/.claude/rules/")

    # Step 7: Create audit trail
    log_sync(new_patterns)
```

### Output Example
```
=== Cross-Business Learning Sync ===
Date: 2026-03-08

Businesses scanned: 3
- academic-ghostwriting
- carpooling-platform
- invoice-automation

New patterns discovered: 2

[1] Route Optimization Caching (carpooling-platform)
    Category: Performance
    Value: HIGH
    → Added to PATTERNS_DISCOVERED.md
    → Created .claude/rules/caching-strategies.md
    → Updated PROJECT_TEMPLATES/saas-platform/

[2] Multi-Currency Handling (invoice-automation)
    Category: Integration
    Value: MEDIUM
    → Added to PATTERNS_DISCOVERED.md
    → Updated PROJECT_TEMPLATES/financial-tool/

Rules synced to:
✓ businesses/academic-ghostwriting/.claude/rules/
✓ businesses/carpooling-platform/.claude/rules/
✓ businesses/invoice-automation/.claude/rules/

All businesses now have access to 14 patterns (was 12).

Next sync: 2026-03-15 (weekly)
```

---

## Quality Gates

### Before Pattern Extraction

**Checklist:**
- [ ] Problem is non-trivial (>1 hour to solve)
- [ ] Solution is generalizable (not business-specific)
- [ ] Evidence of success (metrics, test results)
- [ ] Documented clearly in LEARNINGS.md
- [ ] Pattern doesn't already exist in registry

### After Pattern Extraction

**Validation:**
- [ ] Added to `PATTERNS_DISCOVERED.md` with all metadata
- [ ] Categorized correctly (Architecture, Performance, etc.)
- [ ] Value level assigned (HIGH/MEDIUM/LOW)
- [ ] Source business credited
- [ ] Applicability scope defined
- [ ] Implementation example provided
- [ ] Evidence included

---

## Anti-Patterns (What NOT to Do)

### ❌ Don't Extract Business Logic
**Bad:**
```markdown
## Pattern: Ghostwriting Pricing Formula
Price = (pages × $15) + (urgency_multiplier × 1.5)
```

**Why:** This is business-specific logic, not a generalizable pattern.

### ❌ Don't Extract Trivial Solutions
**Bad:**
```markdown
## Pattern: Use Environment Variables
Store API keys in .env file instead of hardcoding.
```

**Why:** This is common knowledge, not a discovered pattern.

### ❌ Don't Extract Unproven Patterns
**Bad:**
```markdown
## Pattern: Experimental Caching Strategy
I think this might work, haven't tested yet.
```

**Why:** Only extract patterns with evidence of success.

### ❌ Don't Duplicate Existing Patterns
**Bad:**
```markdown
## Pattern: Backup Before Major Changes
Create backups before risky operations.
```

**Why:** Pattern 9 (Backup/Rollback Strategy) already covers this.

---

## Growth Strategy

### Phase 1: Current (2 Businesses)
- academic-ghostwriting (10 patterns)
- carpooling-platform (2 patterns)
- **Total: 12 patterns**

### Phase 2: Expansion (3-5 Businesses)
- Add invoice-automation (likely discovers: multi-currency, tax calculations, PDF generation)
- Add data-analytics-tool (likely discovers: data pipeline patterns, visualization strategies)
- **Projected: 20-25 patterns**

### Phase 3: Maturity (6+ Businesses)
- Pattern discovery slows (most common patterns already discovered)
- Focus shifts to optimization and refinement
- **Projected: 30-40 patterns (plateau)**

### Phase 4: Ecosystem
- New businesses inherit 30-40 proven patterns from day 1
- 80% less trial-and-error
- Focus on business logic, not infrastructure

---

## Success Metrics

### Pattern Discovery
- **Patterns per business:** Target 3-5 HIGH value patterns per business
- **Discovery rate:** 1-2 new patterns per week during active development

### Pattern Adoption
- **Adoption rate:** % of patterns used in each business
- **Target:** 60%+ adoption (not all patterns apply to all businesses)

### Time Savings
- **New business setup:** 30 minutes (vs 4+ hours from scratch)
- **Pattern implementation:** 15 minutes (vs 1-2 hours discovery)

### Code Quality
- **Consistency:** Same patterns across all businesses
- **Maintainability:** Switching projects takes <5 minutes (vibe coding)

---

## The Compound Effect

```
Month 1: Business 1 discovers 5 patterns
Month 2: Business 2 inherits 5, discovers 3 more (total: 8)
Month 3: Business 3 inherits 8, discovers 4 more (total: 12)
Month 4: Business 4 inherits 12, discovers 2 more (total: 14)
Month 5: Business 5 inherits 14, discovers 1 more (total: 15)

Result: Business 5 starts with 14 proven patterns.
        Business 1 had to discover from scratch.

Advantage: Business 5 is 10x faster to build.
```

**This is the power of the cross-business learning ecosystem.**

---

## Quick Reference

### Document a Pattern in Your Business
1. Add to `businesses/your-business/LEARNINGS.md`
2. Include: Problem, Solution, Evidence, Generalizability

### Extract Patterns to Template
```bash
# Automated (recommended)
python _template/sync-learnings.py

# Manual (specific pattern)
python _template/extract-pattern.py businesses/your-business/LEARNINGS.md "Pattern Name"
```

### Create New Business with All Patterns
```bash
# Copy template
cp -r _template/PROJECT_TEMPLATES/saas-platform/ businesses/new-business/

# Already includes all discovered patterns!
```

### Check Pattern Registry
```bash
# View all discovered patterns
cat _template/PATTERNS_DISCOVERED.md

# Count patterns
grep "^### Pattern" _template/PATTERNS_DISCOVERED.md | wc -l
```

---

🌱 **Your businesses learn from each other. Work on what inspires you today. The whole ecosystem gets smarter.**
