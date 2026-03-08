#!/usr/bin/env python3
"""
Machine-First Architecture Validator

Checks if a project follows machine-first architecture rules:
1. Purpose-driven naming (not domain names)
2. English-only paths (ASCII characters)
3. Flat structure (max 2 levels)
4. No acronyms in filenames
5. Learning loop functional
6. Scripts reference current names (not legacy v4.x)

Usage:
    python VALIDATION.py [project_path]

    If project_path not provided, validates current directory.
"""

import sys
import os
from pathlib import Path
import re
import unicodedata

# ANSI color codes
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Validation rules
PURPOSE_SUFFIXES = ["-solver", "-modeling", "-reporting", "-analysis", "-generator", "-tracker", "-monitor"]
ACRONYMS_FILENAMES = ["KB.md", "config.md", "MAPA.md", "IO.md"]
LEGACY_V4_PATTERNS = [
    "products/",
    "solver-analytical/",
    "solver-symbolic/",
    "solver-systems/",
    "solver-logic/",
    "solver-docs/",
    "mate-general",
    "mate-financiera",
    "estadistica",
    "ingenieria-civil",
]


def is_ascii_path(path_str):
    """Check if path contains only ASCII characters."""
    try:
        path_str.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False


def has_accents(text):
    """Check if text has accented characters."""
    return any(unicodedata.category(c) == 'Mn' for c in unicodedata.normalize('NFD', text))


def is_spanish_word(word):
    """Basic check for common Spanish words (not exhaustive)."""
    spanish_words = [
        "estadistica", "fisica", "contabilidad", "logica",
        "ingenieria", "mate", "financiera", "estilo"
    ]
    return any(sp in word.lower() for sp in spanish_words)


def get_depth(path, root):
    """Get nesting depth relative to root."""
    rel_path = path.relative_to(root)
    return len(rel_path.parts)


def check_purpose_driven_naming(path):
    """Check if folder follows purpose-driven naming pattern."""
    name = path.name.lower()

    # Check for purpose suffixes
    has_purpose_suffix = any(name.endswith(suffix) for suffix in PURPOSE_SUFFIXES)

    # Check for domain/subject names (Spanish)
    is_domain_name = is_spanish_word(name)

    return has_purpose_suffix, is_domain_name


def validate_project(project_path):
    """Main validation function."""
    project_path = Path(project_path).resolve()

    if not project_path.exists():
        print(f"{RED}❌ Error: Path does not exist: {project_path}{RESET}")
        return False

    print(f"\n{BOLD}{BLUE}{'='*60}{RESET}")
    print(f"{BOLD}{BLUE}Machine-First Architecture Validator{RESET}")
    print(f"{BOLD}{BLUE}{'='*60}{RESET}\n")
    print(f"Validating: {project_path}\n")

    issues = []
    warnings = []
    passed = []

    # Ignore certain directories
    ignore_dirs = {".git", "node_modules", "__pycache__", ".vscode", ".idea", "archive", ".claude"}

    # ========== CHECK 1: English-only paths (ASCII) ==========
    print(f"{BOLD}[1/7] Checking for non-ASCII paths...{RESET}")
    non_ascii_paths = []
    for path in project_path.rglob("*"):
        if any(ignored in path.parts for ignored in ignore_dirs):
            continue
        if not is_ascii_path(str(path.relative_to(project_path))):
            non_ascii_paths.append(path.relative_to(project_path))

    if non_ascii_paths:
        issues.append(f"Non-ASCII paths found ({len(non_ascii_paths)}):")
        for p in non_ascii_paths[:5]:
            issues.append(f"  - {p}")
        if len(non_ascii_paths) > 5:
            issues.append(f"  ... and {len(non_ascii_paths) - 5} more")
    else:
        passed.append("✓ All paths use ASCII characters")

    # ========== CHECK 2: Purpose-driven naming ==========
    print(f"{BOLD}[2/7] Checking for purpose-driven naming...{RESET}")
    domain_names = []
    folders_checked = 0

    for path in project_path.iterdir():
        if path.is_dir() and path.name not in ignore_dirs and not path.name.startswith("_") and not path.name.startswith("."):
            folders_checked += 1
            has_purpose, is_domain = check_purpose_driven_naming(path)

            if is_domain:
                domain_names.append(path.name)

    if domain_names:
        issues.append(f"Domain-driven names found (should be purpose-driven):")
        for name in domain_names:
            issues.append(f"  - {name}/  (Spanish domain name)")
    else:
        passed.append(f"✓ All folders use purpose-driven naming ({folders_checked} checked)")

    # ========== CHECK 3: Flat structure (max 2 levels) ==========
    print(f"{BOLD}[3/7] Checking structure depth...{RESET}")
    deep_paths = []

    for path in project_path.rglob("*"):
        if any(ignored in path.parts for ignored in ignore_dirs):
            continue
        depth = get_depth(path, project_path)
        if depth > 2 and path.is_dir():
            deep_paths.append((path.relative_to(project_path), depth))

    if deep_paths:
        warnings.append(f"Deep nesting found (>{len(deep_paths)} folders >2 levels):")
        for p, d in sorted(deep_paths, key=lambda x: x[1], reverse=True)[:5]:
            warnings.append(f"  - {p} (depth: {d})")
    else:
        passed.append("✓ Flat structure (max 2 levels)")

    # ========== CHECK 4: No acronyms in filenames ==========
    print(f"{BOLD}[4/7] Checking for acronyms in filenames...{RESET}")
    acronym_files = []

    for path in project_path.rglob("*"):
        if any(ignored in path.parts for ignored in ignore_dirs):
            continue
        if path.is_file() and path.name in ACRONYMS_FILENAMES:
            acronym_files.append(path.relative_to(project_path))

    if acronym_files:
        issues.append(f"Acronym filenames found ({len(acronym_files)}):")
        for p in acronym_files[:5]:
            issues.append(f"  - {p} (use full name: knowledge.md, role.md, history.md)")
        if len(acronym_files) > 5:
            issues.append(f"  ... and {len(acronym_files) - 5} more")
    else:
        passed.append("✓ No acronyms in filenames")

    # ========== CHECK 5: Required folders exist ==========
    print(f"{BOLD}[5/7] Checking for required folders...{RESET}")
    required_folders = ["pipelines/intake", "_shared", "_meta"]
    missing_folders = []

    for folder in required_folders:
        if not (project_path / folder).exists():
            missing_folders.append(folder)

    if missing_folders:
        warnings.append(f"Recommended folders missing:")
        for folder in missing_folders:
            warnings.append(f"  - {folder}/")
    else:
        passed.append("✓ All required folders present")

    # ========== CHECK 6: Legacy v4.x references in scripts ==========
    print(f"{BOLD}[6/7] Checking for legacy v4.x references in scripts...{RESET}")
    legacy_refs = []

    for py_file in project_path.rglob("*.py"):
        if any(ignored in py_file.parts for ignored in ignore_dirs):
            continue
        try:
            content = py_file.read_text(encoding='utf-8')
            for pattern in LEGACY_V4_PATTERNS:
                if pattern in content:
                    legacy_refs.append((py_file.relative_to(project_path), pattern))
                    break  # Only report once per file
        except Exception as e:
            warnings.append(f"Could not read {py_file.name}: {e}")

    if legacy_refs:
        issues.append(f"Legacy v4.x references found in {len(legacy_refs)} script(s):")
        for file, pattern in legacy_refs[:5]:
            issues.append(f"  - {file} (contains '{pattern}')")
        if len(legacy_refs) > 5:
            issues.append(f"  ... and {len(legacy_refs) - 5} more")
        issues.append("  → Learning loop may be broken!")
    else:
        passed.append("✓ No legacy v4.x references in scripts")

    # ========== CHECK 7: Learning loop files exist ==========
    print(f"{BOLD}[7/7] Checking learning loop components...{RESET}")
    learning_loop_issues = []

    # Check for inbox processor
    if not (project_path / "pipelines/intake/process-inbox.py").exists():
        learning_loop_issues.append("  - pipelines/intake/process-inbox.py missing")

    # Check for knowledge.md files
    knowledge_files = list(project_path.rglob("knowledge.md"))
    if not knowledge_files:
        learning_loop_issues.append("  - No knowledge.md files found")

    if learning_loop_issues:
        warnings.append("Learning loop components missing:")
        warnings.extend(learning_loop_issues)
    else:
        passed.append(f"✓ Learning loop components present ({len(knowledge_files)} knowledge.md files)")

    # ========== SUMMARY ==========
    print(f"\n{BOLD}{BLUE}{'='*60}{RESET}")
    print(f"{BOLD}{BLUE}VALIDATION SUMMARY{RESET}")
    print(f"{BOLD}{BLUE}{'='*60}{RESET}\n")

    # Passed checks
    if passed:
        print(f"{GREEN}{BOLD}✓ PASSED ({len(passed)}){RESET}")
        for p in passed:
            print(f"{GREEN}{p}{RESET}")
        print()

    # Warnings
    if warnings:
        print(f"{YELLOW}{BOLD}⚠ WARNINGS ({len(warnings)}){RESET}")
        for w in warnings:
            print(f"{YELLOW}{w}{RESET}")
        print()

    # Critical issues
    if issues:
        print(f"{RED}{BOLD}❌ CRITICAL ISSUES ({len(issues)}){RESET}")
        for i in issues:
            print(f"{RED}{i}{RESET}")
        print()

    # Overall result
    print(f"{BOLD}{BLUE}{'='*60}{RESET}")
    if not issues:
        print(f"{GREEN}{BOLD}✅ PROJECT FOLLOWS MACHINE-FIRST ARCHITECTURE{RESET}")
        if warnings:
            print(f"{YELLOW}(with {len(warnings)} minor warnings){RESET}")
        return True
    else:
        print(f"{RED}{BOLD}❌ PROJECT HAS CRITICAL ISSUES{RESET}")
        print(f"{RED}Fix critical issues to fully comply with machine-first architecture.{RESET}")
        return False


def main():
    if len(sys.argv) > 1:
        project_path = sys.argv[1]
    else:
        project_path = os.getcwd()

    success = validate_project(project_path)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
