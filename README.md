# Draw Steel Monster Generator

OpenCode skill for generating Draw Steel TTRPG monsters with Foundry VTT JSON output. Compatible with [AgentSkills.io](https://agentskills.io/) and other AI coding tools.

## Quick Start

### Claude Code / OpenCode

1. Copy `.claude/skills/draw-steel-monster-generator/` to your skills directory
2. Run: `opencode run "Create a Level 3 Griffin, Platoon, Harrier"`

### Direct Usage

```bash
# Validate Foundry VTT JSON
python scripts/validate_foundry_json.py output/Monsters

# Validate single file
python scripts/validate_foundry_json.py output/Monsters/griffin.json
```

## What It Does

- Generates Draw Steel monsters using official Monster Basics formulas
- Creates Foundry VTT-ready JSON for import
- Converts monsters from other systems (D&D 5e, Pathfinder, etc.)
- Validates JSON against Foundry schema requirements

## Example Commands

```
"Create a Level 3 Griffin, Platoon, Harrier"
"Convert Slaad from D&D 5e, Level 5, Solo, Controller"
"Create a swarm of 10 Level 1 Giant Rats, Horde, Ambusher"
```

## Project Structure

```
.claude/skills/draw-steel-monster-generator/
├── SKILL.md              # AI skill definition
├── scripts/
│   ├── generate_monster.py
│   └── validate_foundry_json.py  # Foundry JSON validator
└── output/               # Generated monsters
```

## Validation

The validator checks:
- Valid ability/distance/monster keywords
- Proper damageDisplay values (melee/ranged/"")
- Required villain actions for Solo/Leader monsters
- Malice costs appropriate for monster level
- Foundry schema compliance
