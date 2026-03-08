---
description: Create versioned backup before major changes
---

# Create Backup

Creates a `.tar.gz` backup of the current project state before major changes.

## When to Use

- Before major feature additions
- Before experimental refactoring
- Before deployment
- After successful milestone completion
- Before destructive operations

## What It Does

1. Prompts for version tag and description
2. Creates compressed backup excluding common artifacts
3. Verifies backup integrity
4. Updates backup manifest
5. Reports backup size and location

## Execution

Before running backup, ask user:

**Questions:**
1. Version tag? (e.g., "v1.2", "v2.0-beta")
2. Feature description? (e.g., "auth-refactor", "api-redesign")

**Then execute:**

### Step 1: Create Backup

```bash
# Create compressed archive
tar -czf archive/backups/{VERSION}-{FEATURE}.tar.gz \
    --exclude=node_modules \
    --exclude=.git \
    --exclude=__pycache__ \
    --exclude=venv \
    --exclude=.venv \
    --exclude=env \
    --exclude=*.zip \
    --exclude=*.tar.gz \
    --exclude=dist \
    --exclude=build \
    --exclude=.next \
    --exclude=.nuxt \
    .
```

### Step 2: Verify Integrity

```bash
# Count files in backup
FILE_COUNT=$(tar -tzf archive/backups/{VERSION}-{FEATURE}.tar.gz | wc -l)

# Check if backup is valid
tar -tzf archive/backups/{VERSION}-{FEATURE}.tar.gz > /dev/null && echo "✅ Backup valid" || echo "❌ Backup corrupted"
```

### Step 3: Get Backup Size

```bash
# Human-readable size
du -h archive/backups/{VERSION}-{FEATURE}.tar.gz
```

### Step 4: Update Manifest

Append to `archive/backups/README.md`:

```markdown
| {VERSION} | {DATE} | {SIZE} | {DESCRIPTION} | {FILE_COUNT} | `tar -xzf archive/backups/{VERSION}-{FEATURE}.tar.gz` |
```

### Step 5: Report Success

```
✅ Backup created successfully!

📦 File: archive/backups/{VERSION}-{FEATURE}.tar.gz
📊 Size: {SIZE}
📁 Files: {FILE_COUNT}
📅 Date: {DATE}

To restore:
  tar -xzf archive/backups/{VERSION}-{FEATURE}.tar.gz

Manifest updated: archive/backups/README.md
```

## Example Usage

**User:** /create-backup

**Claude:**
```
Creating backup. I need some information:

1. Version tag (e.g., v1.2): v1.3
2. Feature description (e.g., auth-refactor): database-migration

[Creates backup...]

✅ Backup created successfully!

📦 File: archive/backups/v1.3-database-migration.tar.gz
📊 Size: 42KB
📁 Files: 156
📅 Date: 2026-03-07

To restore:
  tar -xzf archive/backups/v1.3-database-migration.tar.gz

Manifest updated: archive/backups/README.md
```

## Safety Notes

**Backups Include:**
- ✅ All source code
- ✅ Configuration files
- ✅ .gitignored files (.env, etc.) ⚠️ **May contain secrets!**
- ✅ Documentation

**Backups Exclude:**
- ❌ Dependencies (node_modules, venv)
- ❌ Git history (.git folder)
- ❌ Build artifacts (dist, build)
- ❌ Compressed files (*.zip, *.tar.gz)

**⚠️ Security Warning:**
Backups may contain `.env` files and other secrets. Do NOT:
- Commit backups to git
- Share backups publicly
- Upload backups to untrusted cloud storage

## Restore Instructions

**To restore a backup:**

1. **Verify current state** (optional):
   ```bash
   git status  # See uncommitted changes
   git stash   # Save current work
   ```

2. **Extract backup:**
   ```bash
   tar -xzf archive/backups/{VERSION}-{FEATURE}.tar.gz
   ```

3. **Verify restoration:**
   ```bash
   git status  # See what changed
   ```

4. **Reinstall dependencies** (if needed):
   ```bash
   npm install  # Node.js
   pip install -r requirements.txt  # Python
   ```

## Backup Management

**Cleanup old backups:**

```bash
# Keep only last 10 backups
cd archive/backups
ls -t *.tar.gz | tail -n +11 | xargs rm -f
```

**List all backups:**

```bash
ls -lh archive/backups/*.tar.gz
```

**Compare backup sizes:**

```bash
du -h archive/backups/*.tar.gz | sort -h
```

## Integration with Git

Backups complement git, they don't replace it:

**Git is better for:**
- Version control and history
- Collaboration
- Code review
- Branching strategies

**Backups are better for:**
- Quick experiments (faster than branches)
- Including .gitignored files
- Pre-deployment snapshots
- Local-only safety net

**Best practice:** Use both!

```bash
# Before major change:
1. Create git branch: git checkout -b feature/new-auth
2. Create backup: /create-backup (v1.2, pre-auth-refactor)
3. Make changes with confidence!
```

---

**Note:** This command creates **local-only** backups. For critical backups, also store externally (cloud, USB drive).
