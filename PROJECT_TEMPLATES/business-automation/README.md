# Business Automation Project Template

> **Quick-start template for business automation projects following machine-first architecture.**

## What This Template Provides

✅ **Machine-first architecture** — Purpose-driven naming, flat structure, English-only
✅ **Zero-friction automation** — Inbox processing, file watcher setup
✅ **Self-improving system** — Learning loop built-in
✅ **Shared knowledge layer** — `_shared/` for cross-module intelligence
✅ **Meta intelligence** — `_meta/` for self-optimization

---

## Quick Start

### 1. Copy Template to New Project
```bash
cp -r PROJECT_TEMPLATES/business-automation/ ../Projects/MyNewProject/
cd ../Projects/MyNewProject/
```

### 2. Link to Centralized Rules
```bash
# Windows (PowerShell as Admin):
New-Item -ItemType SymbolicLink -Path ".claude\rules" -Target "..\..\Claude\.claude\rules"

# Mac/Linux:
ln -s ../../Claude/.claude/rules .claude/rules
```

### 3. Customize for Your Business
Edit these files:
- `README.md` — Replace with your project description
- `CLAUDE.md` — Add your business context
- `.gitignore` — Add your specific exclusions

### 4. Add Your Modules
Create modules following machine-first patterns:
```bash
# Example: Create a report-generator module
mkdir report-generator
cd report-generator
echo "# Report Generator Knowledge" > knowledge.md
echo "# Report Generator Role" > role.md
echo "# Report Generator History" > history.md
```

### 5. Set Up Automation
```bash
pip install watchdog  # If not already installed
python pipelines/intake/watch-inbox.py &  # Start file watcher
```

### 6. Start Using
Drop files in `pipelines/intake/inbox/` and watch the magic happen!

---

## Folder Structure

```
business-automation/
├── .claude/
│   └── rules/ → symlink to Claude/.claude/rules/  # Centralized architecture rules
│
├── _shared/                   # Cross-module shared knowledge
│   ├── README.md
│   └── (add your shared data here)
│
├── _meta/                     # Self-improvement intelligence
│   ├── README.md
│   └── (auto-generated insights go here)
│
├── pipelines/
│   └── intake/
│       ├── inbox/             # Drop files here
│       ├── outbox/            # Solutions appear here
│       ├── processed/         # Auto-archived
│       ├── process-inbox.py   # Classification & extraction
│       └── watch-inbox.py     # File watcher (zero-friction)
│
├── archive/                   # Reversible operations
│   └── trash-can/             # Review before deleting
│
├── knowledge/                 # Project-wide knowledge
│   ├── SPRINT_LOG.md
│   └── CHRONICLE.md
│
├── (your modules go at root level)
│   example-module/
│   ├── knowledge.md
│   ├── role.md
│   └── history.md
│
├── .gitignore
├── README.md
└── CLAUDE.md
```

---

## Architecture Patterns

### Module Pattern
```
{purpose}-{type}/
├── knowledge.md   # Procedural knowledge (formulas, methods)
├── role.md        # Identity & constraints
└── history.md     # Learning history
```

**Naming conventions:**
- `*-solver/` — Solves specific problem types
- `*-modeling/` — Models scenarios/systems
- `*-reporting/` — Generates reports/outputs
- `*-analyzer/` — Analyzes data/patterns

### Shared Knowledge Pattern
```
_shared/
├── {entities}.md          # e.g., customers.md, products.md
├── {reference-data}.md    # e.g., pricing.md, locations.md
└── {cross-cutting}.md     # e.g., terminology.md, standards.md
```

### Meta Intelligence Pattern
```
_meta/
├── knowledge-graph.md     # Concept relationships
├── routing-rules.md       # Classification logic
└── naming-evolution.md    # Why names changed
```

---

## Zero-Friction Automation

### Inbox Processing Workflow

1. **Drop file** in `pipelines/intake/inbox/`
2. **File watcher detects** new file (instant)
3. **Classifier routes** to correct module
4. **Extractor updates** knowledge.md
5. **Archive moves** to `processed/{date}/`

**No commands needed.** System runs in background.

### Setting Up File Watcher

```bash
# One-time setup:
pip install watchdog

# Run in background:
python pipelines/intake/watch-inbox.py &

# Or add to startup (Windows):
# Create shortcut in: shell:startup
# Target: pythonw.exe C:\path\to\watch-inbox.py
```

---

## Learning Loop

### What the System Learns

1. **New patterns** from processed files
2. **Routing keywords** for better classification
3. **Common mistakes** to avoid
4. **Cross-module relationships** (knowledge graph)

### How to Verify Learning

```bash
# Check if knowledge is growing:
git log -- */knowledge.md

# Check routing accuracy:
python pipelines/intake/validate-routing.py

# Check learning events:
git log -- */history.md
```

---

## Customization Guide

### For Different Business Types

**E-commerce:**
```
order-fulfillment/
inventory-analyzer/
customer-segmentation/
pricing-optimizer/
```

**Consulting:**
```
client-analysis/
report-generator/
proposal-builder/
time-tracker/
```

**SaaS:**
```
user-onboarding/
health-monitoring/
analytics-reporter/
billing-calculator/
```

**Content:**
```
seo-analyzer/
content-scheduler/
performance-tracker/
trend-detector/
```

### Adding New Modules

```bash
# 1. Create module folder (purpose-driven name)
mkdir customer-segmentation

# 2. Create standard files
cd customer-segmentation
echo "# Customer Segmentation Knowledge" > knowledge.md
echo "# Customer Segmentation Role" > role.md
echo "# Customer Segmentation History" > history.md

# 3. Add routing keywords
# Edit: pipelines/intake/process-inbox.py
# Add keywords for this module

# 4. Start using
# Drop relevant files in inbox/, system learns
```

---

## Validation

### Run Validation Script
```bash
python ../../Claude/VALIDATION.py
```

**Checks:**
- ✓ All folder names in English
- ✓ Purpose-driven naming
- ✓ Flat structure (max 2 levels)
- ✓ No acronyms in filenames
- ✓ Learning loop functional
- ✓ Scripts reference current names

---

## Migration from Existing Project

### Step 1: Backup
```bash
git commit -m "Backup before machine-first migration"
```

### Step 2: Copy Template
```bash
cp -r ../Claude/PROJECT_TEMPLATES/business-automation/* .
```

### Step 3: Migrate Modules
```bash
# Rename to purpose-driven names:
mv old-name/ purpose-driven-name/

# Rename files:
cd purpose-driven-name/
mv KB.md knowledge.md
mv config.md role.md
```

### Step 4: Update Scripts
```bash
# Find broken references:
grep -r "old-name" --include="*.py"

# Fix each one
```

### Step 5: Test Learning Loop
```bash
# Drop test file in inbox
# Verify classification works
# Verify knowledge gets updated
```

---

## Best Practices

### ✅ Do This
- Use purpose-driven names (`report-generator` not `reports`)
- Keep structure flat (max 2 levels)
- Update knowledge.md from every processed file
- Log learning events in history.md
- Archive processed files (reversible operations)

### ❌ Avoid This
- Domain names (`accounting` → use `financial-reporting`)
- Spanish/non-English names
- Deep nesting (>2 levels)
- Acronyms in filenames (`KB.md` → use `knowledge.md`)
- Manual knowledge updates (automate extraction)

---

## Troubleshooting

### File Watcher Not Working
```bash
# Check if running:
ps aux | grep watch-inbox

# Check logs:
tail -f pipelines/intake/watch-inbox.log

# Restart:
pkill -f watch-inbox
python pipelines/intake/watch-inbox.py &
```

### Classification Incorrect
```bash
# Check routing keywords:
cat pipelines/intake/process-inbox.py | grep KEYWORD

# Add missing keywords for your module
```

### Knowledge Not Updating
```bash
# Check if extraction script works:
python pipelines/intake/extract-knowledge.py test-file.pdf

# Check paths in update script:
cat pipelines/intake/update_kb.py | grep PROJECTS
```

---

## Next Steps

1. **Customize** modules for your business
2. **Test** inbox processing with real files
3. **Monitor** learning metrics (knowledge growth)
4. **Iterate** based on usage patterns

**Remember:** The system improves with use. Drop files, let it learn, stay lean.

---

**Template Version:** 1.0 (2026-03-08)
**Based on:** Centaur v5.0 production architecture
**Maintained by:** Claude Code Ultimate Template
