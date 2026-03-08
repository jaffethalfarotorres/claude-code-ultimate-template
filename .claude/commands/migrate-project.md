Help migrate this existing project to use Claude Code best practices by setting up the proper `.claude/` directory structure.

## Migration Steps

1. **Assessment**:
   - Check if .claude/ directory exists
   - Identify existing CLAUDE.md or similar files
   - Assess current project organization

2. **Create Structure**:
   - Create `.claude/` directory if it doesn't exist
   - Create `.claude/commands/` subdirectory
   - Create `.claude/skills/` subdirectory
   - Create `.claude/rules/` subdirectory

3. **Generate CLAUDE.md**:
   - Run analysis similar to `/custom-init`
   - Generate project-specific CLAUDE.md
   - Move any existing CLAUDE.md content

4. **Create Essential Rules**:
   - Extract code style from existing linter configs (.eslintrc, .prettierrc, etc.)
   - Generate testing.md based on test structure
   - Create security.md with project-specific concerns
   - Add git-workflow.md based on repository history

5. **Setup Settings**:
   - Create `.claude/settings.json` with sensible defaults
   - Create `.claude/settings.local.json.example`
   - Update `.gitignore` to exclude local settings

6. **Add Common Commands**:
   - Create `/review` command
   - Create `/test` command
   - Create `/explain` command
   - Add project-specific commands based on package.json scripts

7. **Documentation**:
   - Create or update README.md
   - Add MIGRATION.md to track what was changed
   - Document the new `.claude/` structure

## Safety Measures

- Create a git commit before starting migration
- Don't delete existing files
- Preserve all existing content
- Make changes incrementally
- Test each step

## Output

Provide:
- Summary of changes made
- List of files created
- Recommended next steps
- Migration checklist

Ask for confirmation before making each major change.
