# Zero-Friction Automation Rules

> **Philosophy:** If it requires a manual command, it has friction. Eliminate friction through background automation.

## The Friction Hierarchy

### **Zero Friction** (Best)
System operates automatically in the background. No human intervention needed.

**Example:**
```
File watcher detects new file in inbox
  ↓ (automatic)
Classifier routes to correct module
  ↓ (automatic)
Knowledge extractor updates knowledge.md
  ↓ (automatic)
File archived to processed/
```

**Human action:** Drop file. **Computer action:** Everything else.

### **Low Friction** (Acceptable)
Single button/click triggers automation.

**Example:**
```
Click "Sync" button in GitHub connector
  ↓
Manual sync completes
```

**Friction cost:** 2 seconds per sync. **Frequency:** Once per session. **Acceptable.**

### **Medium Friction** (Warning Zone)
Requires typing a command or running a script.

**Example:**
```
$ python process-inbox.py
```

**Friction cost:** 5-10 seconds. **Risk:** Easy to forget. **Solution:** Automate with file watcher.

### **High Friction** (Unacceptable)
Requires multiple commands, remembering syntax, or context switching.

**Example:**
```
$ cd pipelines/intake
$ ls inbox/
$ python update_kb.py data-analysis
$ python update_kb.py financial-modeling
$ mv inbox/* processed/$(date +%Y-%m-%d)/
```

**Friction cost:** 30-60 seconds. **Risk:** Error-prone, forgotten steps. **Solution:** Eliminate entirely with automation.

---

## Zero-Friction Design Patterns

### Pattern 1: Drop Zone + File Watcher

**Problem:** Need to manually run commands to process files.

**Solution:**
```python
# watch-inbox.py
from watchdog import FileSystemEventHandler

class InboxHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        # Auto-process new file
        process_file(event.src_path)
```

**Setup Once:**
```bash
pip install watchdog
python watch-inbox.py  # Runs in background
```

**Usage Forever:** Just drop files. System handles rest.

### Pattern 2: Git-Based Shared Brain

**Problem:** Two machines need to stay in sync.

**Solution:**
```bash
# On PC 1:
git add .
git commit -m "Update from corporate PC"
git push

# On PC 2:
git pull  # Get latest changes
```

**Why it works:**
- Git = shared memory between machines
- Session logs committed = persistent state
- No cloud sync needed
- Works offline (commit locally, push when connected)

### Pattern 3: Inbox as Digestive System

**Problem:** Files come from many sources (WhatsApp, email, campus downloads, screenshots).

**Solution:** Single drop zone for EVERYTHING.

```
pipelines/intake/inbox/  ← Drop ANYTHING here
    ↓
Classifier decides what to do
    ↓
Knowledge update, archive, or trash
```

**Benefits:**
- No decision fatigue ("where does this go?")
- System learns from ALL inputs
- Stays lean (auto-archives processed files)

### Pattern 4: Outbox for Results

**Problem:** Need to find solutions after processing.

**Solution:**
```
pipelines/intake/
├── inbox/    ← Input (you drop files)
├── outbox/   ← Output (solutions appear here)
└── processed/ ← Archive (auto-cleanup)
```

**Workflow:**
1. Drop assignment in `inbox/`
2. Grab solution from `outbox/`
3. Send to student
4. Get paid

**No manual searching.** Output always in same place.

---

## Automation Triggers

### Trigger Type 1: File System Events
```python
# Watches: inbox/ folder
# Fires when: New file created
# Action: Auto-classify and process
```

**Use for:** Inbox processing, backup triggers, file organization

### Trigger Type 2: Time-Based (Cron/Scheduled)
```python
# Runs: Every 5 minutes
# Checks: New files in inbox
# Action: Batch process all
```

**Use for:** Periodic cleanup, scheduled reports, stale file detection

**⚠️ Caution:** Slower than file watcher (5 min delay vs instant). Use only if file watcher can't be set up.

### Trigger Type 3: Git Hooks
```bash
# .git/hooks/pre-commit
# Fires: Before every git commit
# Action: Validate files, run linters, update logs
```

**Use for:** Code validation, automatic documentation, session logging

**⚠️ Caution:** Adds time to commits. Use sparingly.

### Trigger Type 4: Manual (Button/Command)
```bash
# User runs: python process-inbox.py
# Or clicks: "Sync" button
```

**Use for:** Operations that need human verification, low-frequency tasks

---

## Zero-Friction Testing

### Test 1: The Drop Test
1. Drop file in inbox
2. Wait 5 seconds
3. Check if file was processed

**Pass criteria:** File classified, knowledge updated, file archived. No commands run.

### Test 2: The Sync Test
1. Make change on PC 1
2. Commit + push
3. Switch to PC 2
4. Pull changes

**Pass criteria:** Session continues seamlessly. No data loss.

### Test 3: The Interruption Test
1. Start processing files
2. Kill process mid-run
3. Restart process

**Pass criteria:** Picks up where it left off. No duplicate processing.

### Test 4: The Forget Test
1. Leave system running for 1 week
2. Drop files randomly
3. Come back, check results

**Pass criteria:** All files processed correctly. No manual intervention needed.

---

## Anti-Friction Patterns

### ✅ Use Background Processes
```python
# Runs forever, waits for files
python watch-inbox.py &
```

### ✅ Use .gitignore for Transient Files
```gitignore
# Don't commit processed student solutions (privacy)
pipelines/intake/outbox/

# Don't commit logs
*.log
```

### ✅ Use Symlinks for Shared Configuration
```bash
# All projects inherit same rules
ln -s ../../Claude/.claude/rules .claude/rules
```

### ✅ Use Defaults for Common Operations
```python
# Default to current directory
inbox = Path(os.getenv("INBOX_PATH", "./pipelines/intake/inbox"))
```

### ❌ Avoid Manual File Moving
```bash
# BAD: Requires remembering syntax
mv inbox/file.pdf processed/2026-03-08/

# GOOD: Script handles it
python process-inbox.py  # Or better: file watcher auto-processes
```

### ❌ Avoid Multi-Step Workflows
```bash
# BAD: Multiple commands
cd pipelines/intake
python classify.py file.pdf
python extract.py file.pdf
python archive.py file.pdf

# GOOD: Single entry point
python process-inbox.py  # Or file watcher
```

### ❌ Avoid Remembering Paths
```bash
# BAD: Need to remember where things are
python scripts/tools/inbox-processor/main.py

# GOOD: Predictable location
python pipelines/intake/process-inbox.py
```

---

## The 3-Second Rule

**If a frequent operation takes more than 3 seconds, automate it.**

### Examples:

| Operation | Current Time | Friction Level | Solution |
|-----------|--------------|----------------|----------|
| Process inbox file | 30 sec (manual) | HIGH | File watcher (0 sec) |
| Find solution | 15 sec (search) | MEDIUM | Outbox folder (1 sec) |
| Update knowledge | 60 sec (copy-paste) | HIGH | Auto-extract (0 sec) |
| Sync between PCs | 10 sec (git push/pull) | LOW | Acceptable |
| Click GitHub sync | 2 sec (click button) | LOW | Acceptable |

---

## Friction Detection

### Red Flags (Indicates Friction)

- "I need to remember to run X"
- "Where did I put that file?"
- "What was the command again?"
- "I forgot to archive the processed files"
- "I need to manually copy this to 3 places"

### Green Signals (Zero Friction)

- "I just drop files and grab results"
- "It handles that automatically"
- "I never think about it"
- "Works the same on both PCs"
- "I forgot it was running in the background"

---

## Setup Once, Use Forever

**Good automation:**
```bash
# Setup (one time, 5 minutes):
pip install watchdog
python watch-inbox.py &

# Usage (forever):
# Just drop files in inbox/
```

**Bad automation:**
```bash
# Every time (30 seconds):
cd pipelines/intake
python process.py --input inbox/ --output outbox/ --archive processed/
```

**The test:** If you need to document HOW to use it, it has friction.

---

## Inbox as Universal Interface

**Philosophy:** One input method for EVERYTHING.

### What Goes in Inbox?

- ✅ Student assignments (PDFs, DOCX, Excel)
- ✅ Screenshots of problems
- ✅ Campus downloads (automatic from scraper)
- ✅ WhatsApp files
- ✅ Email attachments
- ✅ Scanned images
- ✅ Text files with notes
- ✅ Supporting materials (textbooks, examples)

### What Inbox Does

**1. Classify:**
- Assignment → Route to correct solver
- Learning material → Extract to knowledge.md
- Garbage → Archive to trash-can
- Unknown → Flag for manual review

**2. Extract:**
- Formulas → Add to knowledge.md
- Examples → Add to knowledge.md
- Professor requirements → Add to professors.md
- Concepts → Update knowledge graph

**3. Archive:**
- Move to `processed/{date}/`
- Keep 30 days, then delete (or longer if needed)
- Audit trail for "did I process this?"

**4. Output:**
- Solutions → `outbox/`
- Reports → `outbox/`
- Errors → `outbox/errors.log`

---

## The Perfect Workflow

```
Human: Drops file in inbox/
    ↓ (0 seconds later)
Computer: Detects new file
    ↓ (1 second later)
Computer: Classifies → "data-analysis assignment"
    ↓ (2 seconds later)
Computer: Extracts knowledge → Updates data-analysis/knowledge.md
    ↓ (3 seconds later)
Computer: Processes assignment → Generates solution
    ↓ (60 seconds later)
Computer: Writes solution to outbox/solution.pdf
    ↓ (61 seconds later)
Computer: Archives original to processed/2026-03-08/
    ↓ (62 seconds later)
Computer: Logs completion