# Self-Improving System Rules

> **Philosophy:** The system learns from every file processed, every pattern discovered, every error encountered.

## The Learning Loop

```
INPUT (inbox/)
   ↓
CLASSIFY (what type of problem?)
   ↓
SOLVE (generate solution)
   ↓
EXTRACT LEARNINGS (what's new?)
   ↓
UPDATE KNOWLEDGE (add to knowledge.md)
   ↓
ARCHIVE (processed/)
   ↓
SYSTEM IS SMARTER ✓
```

**Critical:** If the loop is broken at any step, the system stops learning.

---

## What the System Learns

### 1. **Formulas & Methods**
```markdown
# BEFORE: knowledge.md (100 formulas)
## Hypothesis Testing
- Z-test formula: ...
- T-test formula: ...

# NEW FILE PROCESSED: Introduces Chi-Square test

# AFTER: knowledge.md (101 formulas)
## Hypothesis Testing
- Z-test formula: ...
- T-test formula: ...
- Chi-square test formula: ...  ← NEW
```

### 2. **Professor Requirements**
```markdown
# BEFORE: _shared/professors.md
## Prof. Ana Méndez
- Decimals: 4 places
- Format: Excel

# NEW ASSIGNMENT: Prof. Méndez requires specific CCSS rates

# AFTER: _shared/professors.md
## Prof. Ana Méndez
- Decimals: 4 places
- Format: Excel
- CCSS Rates (2026): 10.83% employee, 26.83% employer  ← NEW
```

### 3. **Common Patterns**
```markdown
# BEFORE: _meta/knowledge-graph.md
(Empty)

# AFTER PROCESSING 50 FILES: Discovers patterns

## Common Co-Occurrence
- "Hypothesis testing" + "ANOVA" appear together in 80% of stats assignments
- "Amortization" + "Effective rate" appear together in 90% of finance assignments
→ INSIGHT: When classifier sees "hypothesis", pre-load ANOVA knowledge
```

### 4. **Routing Keywords**
```python
# BEFORE: process-inbox.py
KEYWORD_TO_PROJECT = {
    "hipotesis": "data-analysis",
    "anova": "data-analysis",
}

# NEW FILE PROCESSED: Uses phrase "prueba de normalidad"

# AFTER: process-inbox.py (auto-updated)
KEYWORD_TO_PROJECT = {
    "hipotesis": "data-analysis",
    "anova": "data-analysis",
    "prueba de normalidad": "data-analysis",  # ← NEW (learned)
}
```

### 5. **Error Corrections**
```markdown
# BEFORE: data-analysis/history.md
(No errors recorded)

# PROCESSED ASSIGNMENT: Student submission had wrong answer

# AFTER: data-analysis/history.md
## 2026-03-08 — Hypothesis Test Error
- Student used one-tailed when two-tailed was correct
- Confusion: "mayor que" implies one-tailed, but question asks "diferente" (two-tailed)
- Learning: Always check for keywords: "diferente", "distinto" → two-tailed
```

---

## Knowledge File Structure

### `knowledge.md` — Procedural Knowledge
```markdown
# SECTION 1: PROTOCOLS
## 1.1 Standard Format for Solutions
1. **Hypotheses** (H₀ and H₁)
2. **Significance level** (α = 0.05)
3. **Test statistic** (formula + calculation)
4. **Critical value** (table lookup)
5. **Decision** (reject or fail to reject)
6. **Conclusion** (in context)

# SECTION 2: FORMULAS
## 2.1 Hypothesis Testing
### Z-Test (known σ)
Z = (x̄ - μ₀) / (σ / √n)

### T-Test (unknown σ)
t = (x̄ - μ₀) / (s / √n)

# SECTION 3: EXAMPLES
## 3.1 Example: Hypothesis Test for Mean
... (full worked example)
```

**Rule:** Every new formula/method extracted from inbox goes to correct section.

### `role.md` — Identity & Constraints
```markdown
# Role: Data Analysis Solver

**Purpose:** Solve statistics assignments for university students in Costa Rica.

**Constraints:**
- Must follow professor-specific requirements (see _shared/professors.md)
- Must use exact decimal places requested
- Must show ALL work (no shortcuts)
- Must use Spanish terminology when required

**Output Format:**
- Excel for numeric problems
- Word for conceptual explanations
- Both for hybrid assignments
```

**Rule:** Role defines WHAT you are, not HOW you solve. HOW goes in knowledge.md.

### `history.md` — Learning History
```markdown
# Learning History — Data Analysis Solver

## 2026-03-08 — Chi-Square Test Added
- **Source:** Assignment from Prof. José Navarro (UNED)
- **New concept:** Goodness-of-fit test
- **Formula added:** χ² = Σ((O - E)² / E)
- **Example added:** Dice fairness test
- **Keywords learned:** "bondad de ajuste", "chi cuadrado"

## 2026-03-05 — ANOVA Multiple Comparisons
- **Source:** Assignment from Prof. Ana Méndez (UCR)
- **New concept:** Tukey HSD post-hoc test
- **Insight:** ANOVA tells IF groups differ, Tukey tells WHICH groups
- **Added to knowledge.md:** Section 2.5
```

**Rule:** Every learning event gets timestamped entry. Helps understand where knowledge came from.

---

## Learning Triggers

### Trigger 1: New Formula Detected
```python
def extract_formulas(file_content):
    # Detect LaTeX: $ ... $
    # Detect images of equations
    # Detect Excel formulas

    for formula in detected_formulas:
        if formula not in knowledge_base:
            add_to_knowledge(formula)
            log_learning_event(formula, source=file)
```

### Trigger 2: New Keyword Detected
```python
def update_routing_keywords(file_name, classified_project):
    # Extract keywords from filename
    keywords = extract_keywords(file_name)

    for keyword in keywords:
        if keyword not in KEYWORD_TO_PROJECT:
            KEYWORD_TO_PROJECT[keyword] = classified_project
            log_learning_event(keyword, action="added_to_routing")
```

### Trigger 3: Professor Requirement Detected
```python
def extract_professor_requirements(assignment):
    # Check for signature patterns
    if "usar 4 decimales" in assignment:
        update_professor_profile(professor, decimals=4)

    if "formato Excel" in assignment:
        update_professor_profile(professor, format="Excel")
```

### Trigger 4: Error Pattern Detected
```python
def learn_from_errors(solution, student_feedback):
    if feedback == "incorrect":
        analyze_error(solution)
        add_to_history(
            error=solution,
            correct=student_feedback,
            lesson="Don't make this mistake again"
        )
```

---

## The Meta Layer (`_meta/`)

### `knowledge-graph.md` — Concept Relationships
```markdown
# Knowledge Graph — Cross-Solver Intelligence

## Cluster 1: Quantitative Analysis
**Nodes:** data-analysis, financial-modeling
**Common concepts:**
- Hypothesis testing (investment decisions)
- Confidence intervals (financial forecasts)
- Regression analysis (trend analysis)

**Insight:** When student asks about "investment analysis", may need BOTH financial-modeling (calculations) AND data-analysis (statistical validation).
```

**Purpose:** Discovers relationships ACROSS solvers. Enables smarter routing.

### `routing-rules.md` — CRM Tag → Solver Mapping
```markdown
# Routing Rules — Keyword-Based Classification

## data-analysis
**Tags:** Estadística, Estadística I, Estadística II, Probabilidad
**Keywords:**
- Spanish: hipótesis, anova, regresión, muestreo
- English: hypothesis, regression, sampling
**Confidence:** HIGH if 3+ keywords match

## optimization-modeling
**Tags:** Investigación de Operaciones, IO
**Keywords:**
- Spanish: transporte, vogel, simplex, cpm, pert
- English: transportation, linear programming
**Confidence:** HIGH if 2+ keywords match (specialized domain)
```

**Purpose:** Centralizes routing logic. Easy to update when new patterns emerge.

### `naming-evolution.md` — Institutional Memory
```markdown
# Naming Evolution — Why Names Changed

## v4.x → v5.0 Migration (2026-03-08)

| Old Name | New Name | Reasoning |
|----------|----------|-----------|
| `estadistica` | `data-analysis` | Purpose > Domain. Analyzes data, not just "statistics" |
| `io` | `optimization-modeling` | Clarity. "IO" is ambiguous acronym |
| `contabilidad` | `financial-reporting` | English + purpose. Produces reports, not just "accounting" |

**Pattern discovered:** Domain names age poorly. Purpose names stay relevant.
```

**Purpose:** Future you understands WHY decisions were made. Prevents reverting to old patterns.

---

## Self-Validation

### The system validates itself:

**1. Freshness Check**
```bash
# Flag stale knowledge
git log --since="30 days ago" -- data-analysis/knowledge.md
# If no updates in 30 days → Flag: "Possibly stale OR no new assignments"
```

**2. Routing Accuracy Check**
```python
# Test classifier on processed files
for file in processed/:
    predicted = classify(file.name)
    actual = file.location  # Where it was actually processed

    if predicted != actual:
        log_error(file, predicted, actual)
        # Learn: Update keyword weights
```

**3. Broken Reference Check**
```bash
# Find references to old v4.x names
grep -r "mate-general" --include="*.py"
grep -r "products/" --include="*.py"
# If found → Flag: "Broken references, learning loop may be broken"
```

**4. Knowledge Drift Check**
```python
# Compare solver knowledge bases
for solver in solvers:
    formula_count = count_formulas(solver)
    if formula_count_delta_30d == 0:
        log_warning(f"{solver} hasn't learned new formulas in 30 days")
```

---

## Anti-Patterns (Breaks Learning)

### ❌ Static Knowledge
```markdown
# knowledge.md created once, never updated
# → System doesn't learn from new assignments
```

**Fix:** Auto-extract formulas/methods from each processed file.

### ❌ Manual Knowledge Updates
```markdown
# Human manually copies formulas to knowledge.md
# → Slow, error-prone, forgotten
```

**Fix:** Extraction script (`extract_knowledge.py`) runs automatically on each file.

### ❌ No Learning History
```markdown
# knowledge.md updated, but no record of WHEN or WHY
# → Can't understand knowledge evolution
```

**Fix:** Every update to knowledge.md gets timestamped entry in history.md.

### ❌ Broken Scripts
```python
# Scripts reference old v4.x paths
PROJECTS = {"mate-general": "solver-symbolic/mate-general"}
# → Files classified correctly but can't update knowledge (path doesn't exist)
```

**Fix:** Update ALL scripts when structure changes. Test learning loop end-to-end.

### ❌ Knowledge Silos
```markdown
# Each solver learns independently
# → Misses cross-solver patterns (e.g., stats + finance often used together)
```

**Fix:** `_meta/knowledge-graph.md` tracks relationships across solvers.

---

## Learning Metrics

Track these to validate the system is learning:

| Metric | Good Trend | Warning Sign |
|--------|------------|--------------|
| **Formulas in knowledge.md** | Growing steadily | Flat for 30+ days |
| **Routing keywords** | Growing with usage | Static |
| **Classification accuracy** | >95% | Dropping |
| **Professor profiles** | Growing | Empty/sparse |
| **Knowledge graph connections** | Increasing | None discovered |
| **history.md entries** | Regular additions | No new entries |

---

## The Learning Dashboard (Future)

Ideal: Auto-generated report showing system health.

```markdown
# System Learning Report — 2026-03-08

## Knowledge Growth
- data-analysis: +5 formulas this month
- financial-modeling: +3 methods this month
- algebra-solver: +0 (warning: no growth)

## Routing Accuracy
- 47/50 files classified correctly (94%)
- 3 misclassifications (manual review needed)

## Professor Intelligence
- 13 professors tracked
- 8 with complete profiles
- 5 need more data

## Knowledge Graph
- 12 cross-solver relationships discovered
- Strongest: data-analysis ↔ financial-modeling (15 shared concepts)

## Recommendations
1. Investigate algebra-solver stagnation (no new formulas)
2. Review 3 misclassified files to improve routing
3. Next assignment from Prof. X → capture missing profile data
```

---

## Version History

- **v1.0 (2026-03-08):** Extracted from Centaur v5.0 architecture
- Based on: Learning loop patterns from production system
- Principle: System that doesn't learn is static code, not intelligence

---

**This is a living document.** Update as new learning patterns emerge.
