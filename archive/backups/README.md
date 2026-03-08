# Backup Manifest

This directory contains versioned `.tar.gz` backups created before major changes.

## Purpose

- **Quick rollback** after failed experiments
- **Pre-deployment safety net**
- **Version snapshots** for comparison
- **Disaster recovery** (corrupted working directory)

## Backup Strategy

Backups are created:
- Before major feature additions
- Before experimental changes
- Before deployment
- After successful milestone completion

## Backup Inventory

| Version | Date | Size | Description | Files | Restore Command |
|---------|------|------|-------------|-------|-----------------|
| (example) | 2026-03-07 | 45KB | Initial template setup | 28 | `tar -xzf v1.0-initial-setup.tar.gz` |

---

## How to Create Backup

Use the `/create-backup` command or manually:

```bash
# Create backup
tar -czf archive/backups/v{VERSION}-{FEATURE}.tar.gz \
    --exclude=node_modules \
    --exclude=.git \
    --exclude=__pycache__ \
    --exclude=venv \
    --exclude=*.zip \
    .

# Verify integrity
tar -tzf archive/backups/v{VERSION}-{FEATURE}.tar.gz | wc -l

# Check size
du -h archive/backups/v{VERSION}-{FEATURE}.tar.gz
```

## How to Restore Backup

```bash
# CAUTION: This will overwrite your current working directory!

# 1. Verify backup exists
ls -lh archive/backups/v{VERSION}-{FEATURE}.tar.gz

# 2. Extract (from project root)
tar -xzf archive/backups/v{VERSION}-{FEATURE}.tar.gz

# 3. Verify restoration
git status  # Check what changed
```

## Best Practices

- ✅ **Create before destructive changes** (can't undo easily)
- ✅ **Tag with version and feature** (e.g., v1.2-auth-refactor)
- ✅ **Update this manifest** after each backup
- ✅ **Verify backup integrity** (test extraction)
- ✅ **Clean up old backups** (keep last 5-10 versions)
- ❌ **Don't backup .git folder** (use git for version control)
- ❌ **Don't backup dependencies** (node_modules, venv)
- ❌ **Don't backup secrets** (.env files get backed up - be careful!)

## Backup vs. Git

**Use Backups When:**
- Quick experiments (faster than branches)
- Need .gitignored files (.env, node_modules)
- Pre-deployment snapshot
- Local-only work

**Use Git When:**
- Collaboration needed
- Long-term version control
- Feature development
- Code review required

**Best Approach:** Use both! Git for version control + Backups for safety net.

---

**Note:** Backups are **local-only** (not version controlled). Store important backups externally (cloud, USB) for additional safety.
