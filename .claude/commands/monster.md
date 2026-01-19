---
name: Create Monster
description: Generate a Draw Steel TTRPG monster with formula-compliant stat blocks. Supports Markdown and Foundry VTT export.
category: Monster
tags: [monster, draw-steel, rpg, ttrpg, foundry]
argument-hint: "[Level] [Creature Name], [Organization], [Role] [--format FORMAT]"
---

Load the Draw Steel Monster Generator skill and create a stat block.

## Input Format

Use the format: `"Create a [Level] [Creature Name], [Organization], [Role] [--format FORMAT]"`

### Organizations
- `Minion` - 1S size, lowest stats
- `Horde` - 1M size, 4 creatures, 2× EV multiplier
- `Platoon` - 1M size, 4 creatures, 2× EV multiplier
- `Elite` - 1M size, 2× EV multiplier
- `Leader` - 1M size, 2× EV multiplier, buffs allies
- `Solo` - 3×3 size, 3× EV multiplier, multiple turns

### Roles
- `Ambusher` - High burst damage, Agility-based
- `Artillery` - Area damage, Reason-based
- `Brute` - High damage, Might-based
- `Controller` - Area control, Reason-based
- `Defender` - Protection, Might-based
- `Harrier` - Disruption, Agility-based
- `Hexer` - Conditions, Reason-based
- `Mount` - Carrying capacity
- `Support` - Buffs/healing

### Output Format Options
- `--format markdown` (default) - Standard Markdown stat block
- `--format foundry` - Foundry VTT JSON file
- `--format both` - Both Markdown and Foundry VTT

## Examples

- `/create-monster "Level 1 Kobold Veles, Minion Harrier"`
- `/create-monster "Level 3 Gremlin, Platoon Brute"`
- `/create-monster "Level 5 Red Dragon, Solo Brute --format foundry"`
- `/create-monster "Level 8 Lich, Solo Hexer --format both"`

## Output

### Markdown (Default)
The skill will generate a complete Draw Steel stat block with:
- Stats (EV, Stamina, Speed, Size)
- Characteristics (Might, Agility, Reason, Intuition, Presence)
- Signature ability with power roll
- Secondary ability
- Traits and special features
- Free Strike value

### Foundry VTT
When using `--format foundry` or `--format both`, the skill also generates:
- Complete NPC actor JSON with all stats and characteristics
- Abilities as Foundry items with power roll effects
- Features and traits as passive items
- Role-based token images
- Solo Monster feature for solo creatures
- JSON file saved to `output/Monsters/{CreatureName}/npc_{creature}_{id}.json`

**Note:** The skill automatically loads the monster generator skill when you use this command.
