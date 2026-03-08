#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cross-Business Learning Sync

Scans all businesses for new patterns in LEARNINGS.md files,
extracts generalizable patterns, updates template, and syncs
back to all businesses.

Usage:
    python sync-learnings.py [--dry-run] [--verbose]

Flags:
    --dry-run: Show what would be done without making changes
    --verbose: Show detailed output
"""

import sys
import os
from pathlib import Path
import re
from datetime import datetime
import json
import shutil
import io

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# ANSI color codes (compatible with Windows)
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"

class PatternSyncEngine:
    """Syncs patterns across all businesses."""

    def __init__(self, dry_run=False, verbose=False):
        self.dry_run = dry_run
        self.verbose = verbose
        self.template_root = Path(__file__).parent
        self.workspace_root = self.template_root.parent
        self.businesses_dir = self.workspace_root / "businesses"
        self.registry_file = self.template_root / "PATTERNS_DISCOVERED.md"
        self.rules_dir = self.template_root / ".claude" / "rules"

        # Statistics
        self.stats = {
            "businesses_scanned": 0,
            "patterns_found": 0,
            "patterns_new": 0,
            "patterns_updated": 0,
            "rules_created": 0,
            "businesses_synced": 0,
        }

        # Discovered patterns
        self.all_patterns = []
        self.new_patterns = []
        self.existing_patterns = {}

    def log(self, message, color=""):
        """Print message with optional color."""
        if color:
            print(f"{color}{message}{RESET}")
        else:
            print(message)

    def log_verbose(self, message):
        """Print message only in verbose mode."""
        if self.verbose:
            print(f"  {message}")

    def load_existing_patterns(self):
        """Load patterns from PATTERNS_DISCOVERED.md."""
        self.log_verbose("Loading existing patterns from registry...")

        if not self.registry_file.exists():
            self.log(f"Registry not found: {self.registry_file}", RED)
            return

        content = self.registry_file.read_text(encoding='utf-8')

        # Extract pattern names
        pattern_regex = r"^### Pattern \d+: (.+)$"
        for match in re.finditer(pattern_regex, content, re.MULTILINE):
            pattern_name = match.group(1).strip()
            self.existing_patterns[pattern_name] = True
            self.log_verbose(f"  Found existing pattern: {pattern_name}")

        self.log_verbose(f"Loaded {len(self.existing_patterns)} existing patterns")

    def scan_business(self, business_path):
        """Scan a single business for patterns in LEARNINGS.md."""
        business_name = business_path.name
        learnings_file = business_path / "LEARNINGS.md"

        if not learnings_file.exists():
            self.log_verbose(f"No LEARNINGS.md in {business_name}")
            return []

        self.log_verbose(f"Scanning {business_name}/LEARNINGS.md...")

        content = learnings_file.read_text(encoding='utf-8')

        # Extract patterns
        # Pattern format:
        # ## Pattern: [Name]
        # **Category:** [Category]
        # **Date Discovered:** [Date]
        # **Problem:** [Problem description]
        # **Solution:** [Solution description]
        # **Evidence:** [Evidence]
        # **Generalizability:** [HIGH/MEDIUM/LOW]

        patterns = []
        pattern_sections = re.split(r'^## Pattern: ', content, flags=re.MULTILINE)[1:]

        for section in pattern_sections:
            lines = section.split('\n')
            pattern_name = lines[0].strip()

            # Extract metadata
            category = self._extract_field(section, r'\*\*Category:\*\* (.+)')
            date = self._extract_field(section, r'\*\*Date Discovered:\*\* (.+)')
            problem = self._extract_field(section, r'\*\*Problem:\*\* (.+)')
            solution = self._extract_field(section, r'\*\*Solution:\*\*(.+?)(?=\*\*|$)', multiline=True)
            evidence = self._extract_field(section, r'\*\*Evidence:\*\*(.+?)(?=\*\*|$)', multiline=True)
            generalizability = self._extract_field(section, r'\*\*Generalizability:\*\* (HIGH|MEDIUM|LOW)')

            # Only extract if HIGH or MEDIUM generalizability
            if generalizability not in ["HIGH", "MEDIUM"]:
                self.log_verbose(f"  Skipping '{pattern_name}' (generalizability: {generalizability})")
                continue

            pattern = {
                "name": pattern_name,
                "category": category or "Unknown",
                "date": date or datetime.now().strftime("%Y-%m-%d"),
                "problem": problem or "",
                "solution": solution or "",
                "evidence": evidence or "",
                "value": generalizability,
                "source_business": business_name,
            }

            patterns.append(pattern)
            self.log_verbose(f"  Found pattern: {pattern_name} ({generalizability})")

        return patterns

    def _extract_field(self, text, regex, multiline=False):
        """Extract field from text using regex."""
        flags = re.MULTILINE | re.DOTALL if multiline else re.MULTILINE
        match = re.search(regex, text, flags)
        if match:
            return match.group(1).strip()
        return None

    def scan_all_businesses(self):
        """Scan all businesses for patterns."""
        self.log(f"\n{BLUE}=== Scanning Businesses ==={RESET}")

        if not self.businesses_dir.exists():
            self.log(f"Businesses directory not found: {self.businesses_dir}", RED)
            return

        for business_path in sorted(self.businesses_dir.iterdir()):
            if not business_path.is_dir():
                continue

            self.stats["businesses_scanned"] += 1
            patterns = self.scan_business(business_path)
            self.all_patterns.extend(patterns)
            self.stats["patterns_found"] += len(patterns)

        self.log(f"\nScanned {self.stats['businesses_scanned']} businesses")
        self.log(f"Found {self.stats['patterns_found']} total patterns")

    def identify_new_patterns(self):
        """Identify patterns not in registry."""
        self.log(f"\n{BLUE}=== Identifying New Patterns ==={RESET}")

        for pattern in self.all_patterns:
            if pattern["name"] not in self.existing_patterns:
                self.new_patterns.append(pattern)
                self.stats["patterns_new"] += 1
                self.log(f"  {GREEN}✓{RESET} New pattern: {pattern['name']} ({pattern['source_business']})")
            else:
                self.log_verbose(f"  Pattern already exists: {pattern['name']}")

        if self.stats["patterns_new"] == 0:
            self.log(f"\n{YELLOW}No new patterns discovered.{RESET}")
        else:
            self.log(f"\n{GREEN}Discovered {self.stats['patterns_new']} new patterns!{RESET}")

    def update_registry(self):
        """Add new patterns to PATTERNS_DISCOVERED.md."""
        if self.stats["patterns_new"] == 0:
            return

        self.log(f"\n{BLUE}=== Updating Pattern Registry ==={RESET}")

        if self.dry_run:
            self.log(f"{YELLOW}[DRY RUN] Would update registry with {self.stats['patterns_new']} new patterns{RESET}")
            return

        # Load existing registry
        content = self.registry_file.read_text(encoding='utf-8')

        # Find insertion point (before "## How to Add New Patterns")
        insertion_marker = "## How to Add New Patterns"
        if insertion_marker not in content:
            self.log(f"{RED}Error: Could not find insertion marker in registry{RESET}", RED)
            return

        # Get current pattern count
        pattern_count_match = re.search(r'\*\*Pattern Count:\*\* (\d+)', content)
        if pattern_count_match:
            current_count = int(pattern_count_match.group(1))
            new_count = current_count + self.stats["patterns_new"]

            # Update pattern count
            content = re.sub(
                r'\*\*Pattern Count:\*\* \d+',
                f'**Pattern Count:** {new_count}',
                content
            )

        # Update last updated date
        content = re.sub(
            r'\*\*Last Updated:\*\* \d{4}-\d{2}-\d{2}',
            f'**Last Updated:** {datetime.now().strftime("%Y-%m-%d")}',
            content
        )

        # Build new pattern entries
        new_entries = []
        for i, pattern in enumerate(self.new_patterns, start=current_count + 1):
            entry = f"""
---

### Pattern {i}: {pattern['name']}
**Category:** {pattern['category']}
**Value:** {pattern['value']}
**Source:** {pattern['source_business']}
**Date Discovered:** {pattern['date']}

**Problem Solved:**
{pattern['problem']}

**Solution:**
{pattern['solution']}

**Evidence of Success:**
{pattern['evidence']}

**Applicability:** {self._get_applicability(pattern['value'])}

**Implementation:**
See `businesses/{pattern['source_business']}/LEARNINGS.md` for detailed implementation.

"""
            new_entries.append(entry)

        # Insert new patterns
        parts = content.split(insertion_marker)
        updated_content = parts[0] + '\n'.join(new_entries) + "\n" + insertion_marker + parts[1]

        # Write updated registry
        self.registry_file.write_text(updated_content, encoding='utf-8')
        self.log(f"  {GREEN}✓{RESET} Updated registry with {self.stats['patterns_new']} new patterns")

    def _get_applicability(self, value):
        """Get applicability description based on value."""
        if value == "HIGH":
            return "Universal (benefits all businesses)"
        elif value == "MEDIUM":
            return "Useful for many businesses"
        else:
            return "Optional"

    def create_rule_files(self):
        """Create rule files for HIGH value patterns."""
        high_value_patterns = [p for p in self.new_patterns if p["value"] == "HIGH"]

        if not high_value_patterns:
            return

        self.log(f"\n{BLUE}=== Creating Rule Files ==={RESET}")

        for pattern in high_value_patterns:
            rule_filename = self._pattern_to_filename(pattern["name"])
            rule_file = self.rules_dir / f"{rule_filename}.md"

            if rule_file.exists():
                self.log_verbose(f"  Rule already exists: {rule_filename}.md")
                continue

            if self.dry_run:
                self.log(f"{YELLOW}[DRY RUN] Would create rule: {rule_filename}.md{RESET}")
                continue

            # Create rule file
            rule_content = f"""# {pattern['name']}

**Category:** {pattern['category']}
**Value:** {pattern['value']}
**Source:** {pattern['source_business']}
**Date:** {pattern['date']}

---

## Problem

{pattern['problem']}

---

## Solution

{pattern['solution']}

---

## Evidence

{pattern['evidence']}

---

## Implementation Guide

See `businesses/{pattern['source_business']}/LEARNINGS.md` for detailed implementation examples.

---

## When to Apply

This pattern is HIGH value and should be considered for all businesses in the workspace.

**Checklist:**
- [ ] Read implementation in source business
- [ ] Adapt to your business context
- [ ] Test in your environment
- [ ] Document in your LEARNINGS.md
"""

            rule_file.write_text(rule_content, encoding='utf-8')
            self.stats["rules_created"] += 1
            self.log(f"  {GREEN}✓{RESET} Created rule: {rule_filename}.md")

    def _pattern_to_filename(self, pattern_name):
        """Convert pattern name to filename."""
        # Remove special characters, convert to lowercase, replace spaces with hyphens
        filename = re.sub(r'[^a-zA-Z0-9\s-]', '', pattern_name)
        filename = filename.lower().replace(' ', '-')
        return filename

    def sync_rules_to_businesses(self):
        """Sync updated rules to all businesses."""
        self.log(f"\n{BLUE}=== Syncing Rules to Businesses ==={RESET}")

        if not self.businesses_dir.exists():
            return

        for business_path in sorted(self.businesses_dir.iterdir()):
            if not business_path.is_dir():
                continue

            business_rules_dir = business_path / ".claude" / "rules"

            if not business_rules_dir.exists():
                self.log_verbose(f"  Creating .claude/rules/ in {business_path.name}")
                if not self.dry_run:
                    business_rules_dir.mkdir(parents=True, exist_ok=True)

            # Copy all rules from template
            if self.dry_run:
                self.log(f"{YELLOW}[DRY RUN] Would sync rules to {business_path.name}{RESET}")
            else:
                for rule_file in self.rules_dir.glob("*.md"):
                    dest_file = business_rules_dir / rule_file.name
                    shutil.copy2(rule_file, dest_file)
                    self.log_verbose(f"    Copied {rule_file.name}")

                self.stats["businesses_synced"] += 1
                self.log(f"  {GREEN}✓{RESET} Synced rules to {business_path.name}")

    def create_audit_trail(self):
        """Create audit trail of sync operation."""
        self.log(f"\n{BLUE}=== Creating Audit Trail ==={RESET}")

        audit_dir = self.template_root / "audit"
        if not audit_dir.exists():
            audit_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        audit_file = audit_dir / f"sync_{timestamp}.json"

        audit_data = {
            "timestamp": timestamp,
            "dry_run": self.dry_run,
            "statistics": self.stats,
            "new_patterns": [
                {
                    "name": p["name"],
                    "category": p["category"],
                    "value": p["value"],
                    "source_business": p["source_business"],
                    "date": p["date"],
                }
                for p in self.new_patterns
            ],
        }

        if self.dry_run:
            self.log(f"{YELLOW}[DRY RUN] Would create audit trail: {audit_file.name}{RESET}")
        else:
            audit_file.write_text(json.dumps(audit_data, indent=2), encoding='utf-8')
            self.log(f"  {GREEN}✓{RESET} Created audit trail: {audit_file.name}")

    def print_summary(self):
        """Print summary of sync operation."""
        self.log(f"\n{BLUE}{'=' * 60}{RESET}")
        self.log(f"{BLUE}SYNC SUMMARY{RESET}")
        self.log(f"{BLUE}{'=' * 60}{RESET}")

        self.log(f"\nBusinesses scanned:     {self.stats['businesses_scanned']}")
        self.log(f"Patterns found:         {self.stats['patterns_found']}")
        self.log(f"New patterns:           {self.stats['patterns_new']}", GREEN if self.stats['patterns_new'] > 0 else "")
        self.log(f"Rules created:          {self.stats['rules_created']}")
        self.log(f"Businesses synced:      {self.stats['businesses_synced']}")

        if self.stats["patterns_new"] > 0:
            self.log(f"\n{GREEN}✓ New patterns discovered:{RESET}")
            for pattern in self.new_patterns:
                self.log(f"  • {pattern['name']} ({pattern['value']}) from {pattern['source_business']}")

        total_patterns = len(self.existing_patterns) + self.stats["patterns_new"]
        self.log(f"\n{BLUE}Total patterns in registry: {total_patterns}{RESET}")

        if self.dry_run:
            self.log(f"\n{YELLOW}DRY RUN MODE - No changes were made{RESET}")
        else:
            self.log(f"\n{GREEN}✓ Sync complete!{RESET}")

    def run(self):
        """Run the sync operation."""
        self.log(f"{BLUE}{'=' * 60}{RESET}")
        self.log(f"{BLUE}Cross-Business Learning Sync{RESET}")
        self.log(f"{BLUE}{'=' * 60}{RESET}")
        self.log(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        if self.dry_run:
            self.log(f"{YELLOW}Mode: DRY RUN (no changes will be made){RESET}")
        self.log("")

        # Step 1: Load existing patterns
        self.load_existing_patterns()

        # Step 2: Scan all businesses
        self.scan_all_businesses()

        # Step 3: Identify new patterns
        self.identify_new_patterns()

        # Step 4: Update registry
        self.update_registry()

        # Step 5: Create rule files for HIGH value patterns
        self.create_rule_files()

        # Step 6: Sync rules to all businesses
        self.sync_rules_to_businesses()

        # Step 7: Create audit trail
        self.create_audit_trail()

        # Step 8: Print summary
        self.print_summary()


def main():
    """Main entry point."""
    dry_run = "--dry-run" in sys.argv
    verbose = "--verbose" in sys.argv

    engine = PatternSyncEngine(dry_run=dry_run, verbose=verbose)
    engine.run()


if __name__ == "__main__":
    main()
