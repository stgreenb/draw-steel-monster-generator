# Draw Steel Monster Generator

Skill for generating Draw Steel TTRPG monsters with (optional) Foundry VTT JSON output. Compatible with Claude Code, OpenCode, and other LLM coding tools.

Don't have an LLM tool? Browse available options at [AgentSkills.io](https://agentskills.io/).

## Quick Start

### Claude Code / OpenCode

1. Copy `.claude/skills/draw-steel-monster-generator/` to your skills directory
2. Talk to your LLM using the example commands below

## What It Does

- Generates Draw Steel monsters using official Monster Basics formulas
- Converts monsters from other systems (D&D 5e, Pathfinder, etc.) - ignores source math, uses for inspiration only
- Creates and validates Foundry VTT-ready JSON for import

## Example Commands

```
"Create a Level 3 Griffin, Platoon, Harrier"
"Convert Slaad from D&D 5e, Level 5, Solo, Controller in foundry compatible json"
"Create a swarm of 10 Level 1 Giant Rats, Horde, Ambusher"
"Take this Pathfinder monster <insert monster block> and convert it to a level 3 elite in Draw Steel"
```

## Project Structure

```
.claude/
├── commands/
│   └── monster.md           # Slash command definition
├── skills/draw-steel-monster-generator/
│   ├── SKILL.md             # AI skill definition
│   └── scripts/
│       ├── generate_monster.py
│       └── validate_foundry_json.py  # Foundry JSON validator
└── output/                  # Generated monsters
```

## Validation (if Foundry Format is Requested)

The validator checks:
- Valid ability/distance/monster keywords
- Proper damageDisplay values (melee/ranged/"")
- Required villain actions for Solo/Leader monsters
- Malice costs appropriate for monster level
- Foundry schema compliance
