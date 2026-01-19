# Foundry VTT JSON Export Reference

This document provides the exact JSON structure required when generating Foundry VTT JSON for the Draw Steel system.

## Complete Actor Structure

```json
{
  "name": "MonsterName",
  "type": "npc",
  "img": "systems/draw-steel/assets/roles/controller.webp",
  "system": {
    "stamina": {
      "value": 30,
      "max": 30,
      "temporary": 0
    },
    "characteristics": {
      "might": {"value": 0},
      "agility": {"value": 0},
      "reason": {"value": 2},
      "intuition": {"value": 1},
      "presence": {"value": 0}
    },
    "combat": {
      "save": {"threshold": 6, "bonus": ""},
      "size": {"value": 1, "letter": "M"},
      "stability": 0,
      "turns": 1
    },
    "movement": {
      "value": 5,
      "types": ["walk"],
      "hover": false,
      "disengage": 1
    },
    "damage": {
      "immunities": {"fire": 0, "cold": 0, "corruption": 0, "acid": 0, "lightning": 0, "poison": 0, "psychic": 0, "sonic": 0, "holy": 0},
      "weaknesses": {}
    },
    "negotiation": {
      "interest": 5,
      "patience": 5,
      "impression": 1,
      "motivations": [],
      "pitfalls": []
    },
    "monster": {
      "freeStrike": 4,
      "keywords": ["Aberration", "Fiend"],
      "level": 2,
      "ev": 8,
      "role": "controller",
      "organization": "platoon"
    }
  },
  "prototypeToken": {
    "name": "MonsterName",
    "displayName": 20,
    "displayBars": 20,
    "bar1": {"attribute": "stamina"},
    "bar2": {"attribute": "hero.resources"},
    "width": 1,
    "height": 1,
    "disposition": -1,
    "texture": {
      "src": "systems/draw-steel/assets/roles/controller.webp",
      "anchorX": 0.5,
      "anchorY": 0.5,
      "fit": "contain",
      "scaleX": 1,
      "scaleY": 1
    },
    "lockRotation": true,
    "alpha": 1
  },
  "items": [],
  "_stats": {
    "systemId": "draw-steel",
    "systemVersion": "0.9.0"
  },
  "_id": "uuid-here"
}
```

## Ability Item Structure

```json
{
  "name": "Mind Wrench",
  "type": "ability",
  "system": {
    "type": "main",
    "category": "signature",
    "keywords": ["Psychic", "Magic"],
    "distance": {
      "type": "ranged",
      "primary": 5
    },
    "target": {
      "type": "creature",
      "value": 1
    },
    "power": {
      "roll": {
        "formula": "@chr",
        "characteristics": ["reason"]
      },
      "effects": {
        "damage-id-1": {
          "type": "damage",
          "damage": {
            "tier1": {"value": "4", "types": ["psychic"], "properties": []},
            "tier2": {"value": "7", "types": ["psychic"], "properties": []},
            "tier3": {"value": "9", "types": ["psychic"], "properties": []}
          }
        },
        "applied-id-1": {
          "type": "applied",
          "applied": {
            "tier1": {
              "display": "{{potency}} dazed",
              "potency": {"value": "@potency.1", "characteristic": "reason"}
            },
            "tier2": {
              "display": "{{potency}} dazed (save ends)",
              "potency": {"value": "@potency.2", "characteristic": "reason"}
            },
            "tier3": {
              "display": "{{potency}} dazed and slowed (save ends)",
              "potency": {"value": "@potency.3", "characteristic": "reason"}
            }
          }
        }
      }
    },
    "effect": {
      "before": "",
      "after": ""
    },
    "source": {
      "book": "Monsters",
      "page": "",
      "license": "Draw Steel Creator License"
    }
  }
}
```

## Feature/Trait Item Structure

```json
{
  "name": "Psychic Static",
  "type": "feature",
  "system": {
    "description": {
      "value": "<p>Create a zone of psychic energy...</p>",
      "director": ""
    },
    "source": {
      "book": "Monsters",
      "license": "Draw Steel Creator License"
    }
  }
}
```

## Solo Monster Feature

Solo monsters require a "Solo Monster" feature item:

```json
{
  "name": "Solo Monster",
  "type": "feature",
  "system": {
    "description": {
      "value": "<p><strong>End Effect:</strong> At the end of each of their turns, the creature can take 20 damage to end one effect on them that can be ended by a saving throw.</p><p><strong>Solo Turns:</strong> The creature can take two turns each round.</p>",
      "director": ""
    },
    "source": {
      "book": "Monsters",
      "license": "Draw Steel Creator License"
    }
  }
}
```

## Critical Rules

### DO:
- Use `characteristics.{name}.value` (NOT `abilities` or `mod/bonus`)
- Use `stamina.value` and `stamina.max` (NOT `hp`)
- Solo monsters: `combat.turns = 2`, others = `1`
- Use `damage`, `applied`, `forced` effect types
- Use `prototypeToken` with `disposition: -1` for hostile

### DON'T:
- Don't use `powerRoll.tiers` - use `power.effects` instead
- Don't use `free` for free triggered - use `freeTriggered`
- Don't use generic token images - use role-based paths

## Before vs After Examples

### WRONG (Common Mistakes)
```json
{
  "system": {
    "attributes": { "hp": { "value": 140, "max": 140 } },  // WRONG: uses hp
    "characteristics": { "might": 3 },  // WRONG: no value wrapper
    "speed": 6  // WRONG: should be in movement.value
  },
  "items": [{
    "type": "ability",
    "system": {
      "keywords": ["Main Action"],  // WRONG: type in keywords
      "tiers": {  // WRONG: uses tiers instead of power.effects
        "tier1": { "damage": 5 }
      }
    }
  }],
  "token": { "img": "modules/mcdm-monsters/..." }  // WRONG: wrong path
}
```

### CORRECT
```json
{
  "system": {
    "stamina": { "value": 140, "max": 140, "temporary": 0 },
    "characteristics": { "might": { "value": 3 } },
    "movement": { "value": 6, "types": ["walk"], "hover": false, "disengage": 1 },
    "combat": { "save": { "threshold": 6 }, "turns": 1, "size": { "value": 1 } }
  },
  "items": [{
    "type": "ability",
    "system": {
      "type": "main",  // CORRECT: type field
      "category": "signature",
      "power": {  // CORRECT: power.effects structure
        "effects": {
          "uuid-1": {
            "type": "damage",
            "damage": { "tier1": { "value": "5", "types": ["corruption"] } }
          }
        }
      }
    }
  }],
  "prototypeToken": { "texture": { "src": "systems/draw-steel/assets/roles/brute.webp" } }
}
```

## Ability Type Mapping

| Skill Input | JSON Value |
|-------------|------------|
| Main Action | `main` |
| Maneuver | `maneuver` |
| Triggered Action | `triggered` |
| Free Triggered Action | `freeTriggered` |
| Villain Action | `villain` |
| Passive/Trait | `feature` |

## Distance Type Mapping

| Range Text | JSON Type |
|------------|-----------|
| Melee 1 | `{"type": "melee", "primary": 1}` |
| Melee 2 | `{"type": "melee", "primary": 2}` |
| Ranged 5 | `{"type": "ranged", "primary": 5}` |
| Ranged 8 | `{"type": "ranged", "primary": 8}` |
| 3 burst | `{"type": "burst", "primary": 3}` |
| 5 wall/line | `{"type": "line", "primary": 5}` |
| 2 cube | `{"type": "cube", "primary": 2}` |
| Self | `{"type": "self"}` |

## Role Image Paths

| Role | Image Path |
|------|------------|
| Ambusher | `systems/draw-steel/assets/roles/ambusher.webp` |
| Artillery | `systems/draw-steel/assets/roles/artillery.webp` |
| Brute | `systems/draw-steel/assets/roles/brute.webp` |
| Controller | `systems/draw-steel/assets/roles/controller.webp` |
| Defender | `systems/draw-steel/assets/roles/defender.webp` |
| Harrier | `systems/draw-steel/assets/roles/harrier.webp` |
| Hexer | `systems/draw-steel/assets/roles/hexer.webp` |
| Mount | `systems/draw-steel/assets/roles/mount.webp` |
| Support | `systems/draw-steel/assets/roles/support.webp` |
| Solo | `systems/draw-steel/assets/roles/solo.webp` |

## Movement Types

- `["walk"]` - Default
- `["fly"]` - Flying monsters
- `["fly"]` with `hover: true` - Hover capability
- `["walk", "fly"]` - Both walk and fly
- `["swim"]` - Swimming
- `["burrow"]` - Burrowing
- `["climb"]` - Climbing
- `["teleport"]` - Teleportation

---

## Before You Generate JSON

1. [ ] Have you read this entire reference file?
2. [ ] Do you understand the difference between `power.tiers` and `power.effects`?
3. [ ] Do you know which ability type to use (`main`, `maneuver`, `freeTriggered`, etc.)?
4. [ ] Have you checked the role image path?

**If you answered NO to any question, re-read this file before generating JSON.**
