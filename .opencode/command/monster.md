---
description: Create Draw Steel TTRPG monsters with formula-compliant stat blocks
---

Load the Draw Steel monster generator skill and help the user create a stat block.

## Workflow

### Step 1: Load skill

```
skill({ name: 'draw-steel-monster-generator' })
```

### Step 2: Parse user request

Extract from $ARGUMENTS:
- **Creature name**: e.g., "Griffin", "Red Dragon", "Goblin Scout"
- **Level**: 1-10
- **Organization**: Minion, Horde, Platoon, Elite, Leader, Solo
- **Role**: Ambusher, Artillery, Brute, Controller, Defender, Harrier, Hexer, Mount, Support

### Step 3: Calculate stats

Use formulas.md for:
- EV = ceil(((2 × Level) + 4) × Org_Modifier)
- Stamina = ceil(((10 × Level) + Role_Mod) × Org_Modifier)
- Damage = ceil((4 + Level + Dmg_Mod) × Tier_Mod) × Org_Mod
- Free Strike = Damage at Tier 1

### Step 4: Create stat block

Follow the output format in SKILL.md with:
- Signature ability using calculated damage values
- Secondary ability based on role archetype
- Malice feature (passive ability)
- Keywords from approved lists only

### Step 5: Validate and output

Run through the self-validation checklist in SKILL.md, then output the complete YAML stat block.

<user-request>
$ARGUMENTS
</user-request>
