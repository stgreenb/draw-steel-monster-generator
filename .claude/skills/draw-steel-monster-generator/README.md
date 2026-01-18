# Draw Steel Monster Generator

A skill for generating Draw Steel TTRPG monsters with formula-compliant stat blocks.

## Quick Start

**Input Format:** `"Create a [Level] [Creature Name], [Organization], [Role]"`

**Examples:**
- `"Create a Level 3 Gremlin, Minion Harrier"`
- `"Create a Level 5 Red Dragon, Solo Brute"`
- `"Create a Level 1 Kobold Veles, Minion Harrier"`

## Directory Structure

This skill follows the [Agent Skills specification](https://agentskills.io/specification):

```
draw-steel-monster-generator/
├── SKILL.md              # Main instructions (required)
├── references/           # Detailed documentation
│   ├── templates.md      # Role archetypes and ability patterns
│   ├── examples.md       # Complete stat block examples
│   └── formulas.md       # Quick reference formulas
├── scripts/              # Utility scripts (empty)
└── assets/               # Static resources (empty)
```

## Platform Setup

### Claude Code

No setup required. Claude Code automatically scans `.claude/skills/` at startup.

### Cursor

Cursor scans both `.cursor/skills/` and `.claude/skills/`. If the skill doesn't appear:

**Option 1: Automatic (Recommended)**
Cursor should discover the skill via `.claude/skills/`.

**Option 2: Manual Symlink**
```bash
# Create symlink from .cursor/skills/ to canonical location
cd /path/to/project
ln -s ../.claude/skills/draw-steel-monster-generator .cursor/skills/
```

### Gemini CLI

Gemini CLI scans both `.gemini/skills/` and `.claude/skills/`. If the skill doesn't appear:

**Option 1: Automatic (Recommended)**
Gemini CLI should discover the skill via `.claude/skills/`.

**Option 2: Manual Symlink**
```bash
# Create symlink from .gemini/skills/ to canonical location
cd /path/to/project
ln -s ../.claude/skills/draw-steel-monster-generator .gemini/skills/
```

### Antigravity Google

Antigravity Google follows the Agent Skills specification. It should discover the skill via the standard skills directory.

## Manual Setup (All Platforms)

If automatic discovery doesn't work, create a symlink:

**Linux/macOS:**
```bash
cd /path/to/project
ln -s ../.claude/skills/draw-steel-monster-generator /path/to/platform-skills/
```

**Windows (PowerShell as Administrator):**
```powershell
cd C:\path\to\project
mklink /D .\platform-skills\draw-steel-monster-generator ..\.claude\skills\draw-steel-monster-generator
```

**Note:** Windows requires Developer Mode enabled or Administrator privileges for symlinks.

## Automated Setup

Run the setup script to create symlinks automatically:

```bash
# Make script executable
chmod +x scripts/setup-skill-symlinks.sh

# Run setup
./scripts/setup-skill-symlinks.sh
```

The script:
- Detects your OS
- Creates platform-specific directories
- Creates symlinks to the canonical location
- Provides fallback instructions if permissions are insufficient

## Validation

Validate the skill structure using the skills-ref tool:

```bash
# Install skills-ref
npm install -g skills-ref

# Validate skill
skills-ref validate ./claude/skills/draw-steel-monster-generator/
```

## License

MIT License - See LICENSE file for details.

## Author

stgreenb
