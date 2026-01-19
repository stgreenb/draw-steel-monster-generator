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

## Malice Features and Villain Actions

Malice is a Director resource. Monsters can spend malice to activate powerful abilities at the start of their turn. Villain Actions are special abilities for Leaders and Solos that can be used once per encounter at the end of any other creature's turn.

### Malice Feature Structure

Malice features use the feature item type with malice cost in the description:

```json
{
  "name": "Brutal Effectiveness",
  "type": "feature",
  "system": {
    "description": {
      "value": "<p><strong>3 Malice.</strong> The monster's next ability with a potency has that potency increased by 1.</p>",
      "director": ""
    },
    "source": {
      "book": "Monsters",
      "license": "Draw Steel Creator License"
    },
    "malice": {
      "cost": 3
    }
  },
  "_id": "BrutalEffectiveness123"
}
```

### Malicious Strike Structure

```json
{
  "name": "Malicious Strike",
  "type": "feature",
  "system": {
    "description": {
      "value": "<p><strong>5+ Malice.</strong> The monster's next strike deals extra damage equal to their highest characteristic score. Extra damage increases by 1 for each additional Malice spent (max 3x highest characteristic).</p><p><em>Cannot be used two rounds in a row.</em></p>",
      "director": ""
    },
    "source": {
      "book": "Monsters",
      "license": "Draw Steel Creator License"
    },
    "malice": {
      "cost": 5
    }
  },
  "_id": "MaliciousStrike1234"
}
```

### Villain Action Structure

Villain actions use `type: "ability"` with `system.type: "villain"` and `system.category: "villain"`:

```json
{
  "name": "Villain Action 1: The Monster Takes the Offensive",
  "type": "ability",
  "system": {
    "type": "villain",
    "category": "villain",
    "keywords": ["area"],
    "distance": {
      "type": "burst",
      "primary": 3
    },
    "target": {
      "type": "creature",
      "value": null
    },
    "power": {
      "roll": {
        "formula": "@chr",
        "characteristics": ["reason"]
      },
      "effects": {}
    },
    "effect": {
      "before": "<p><strong>End of any creature's turn.</strong> Each target makes a Reason test. Each target who fails is [[/apply slowed end=save]].</p>",
      "after": ""
    },
    "trigger": "End of any creature's turn",
    "resource": {
      "resettable": true
    },
    "source": {
      "book": "Monsters",
      "license": "Draw Steel Creator License"
    }
  },
  "_id": "VillainAction1012345"
}
```

### Complete Solo Monster with Malice Features

```json
{
  "name": "Ancient Black Dragon",
  "type": "npc",
  "img": "systems/draw-steel/assets/roles/solo.webp",
  "system": {
    "stamina": {
      "value": 350,
      "max": 350,
      "temporary": 0
    },
    "characteristics": {
      "might": {"value": 4},
      "agility": {"value": 3},
      "reason": {"value": 2},
      "intuition": {"value": 3},
      "presence": {"value": 2}
    },
    "combat": {
      "save": {"threshold": 8, "bonus": ""},
      "size": {"value": 5, "letter": "L"},
      "stability": 0,
      "turns": 2
    },
    "movement": {
      "value": 8,
      "types": ["fly"],
      "hover": true,
      "disengage": 1
    },
    "damage": {
      "immunities": {"poison": 0, "acid": 0, "corruption": 0},
      "weaknesses": {"holy": 5}
    },
    "negotiation": {
      "interest": 5,
      "patience": 5,
      "impression": 1,
      "motivations": [],
      "pitfalls": []
    },
    "monster": {
      "freeStrike": 12,
      "keywords": ["Dragon", "Acid"],
      "level": 9,
      "ev": 72,
      "role": "solo",
      "organization": "solo"
    }
  },
  "prototypeToken": {
    "name": "Ancient Black Dragon",
    "displayName": 20,
    "displayBars": 20,
    "bar1": {"attribute": "stamina"},
    "width": 1,
    "height": 1,
    "disposition": -1,
    "texture": {
      "src": "systems/draw-steel/assets/roles/solo.webp"
    }
  },
  "items": [
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
      },
      "_id": "SoloMonsterFeature001"
    },
    {
      "name": "Brutal Effectiveness",
      "type": "feature",
      "system": {
        "description": {
          "value": "<p><strong>3 Malice.</strong> The monster's next ability with a potency has that potency increased by 1.</p>",
          "director": ""
        },
        "source": {
          "book": "Monsters",
          "license": "Draw Steel Creator License"
        },
        "malice": {
          "cost": 3
        }
      },
      "_id": "BrutalEff001"
    },
    {
      "name": "Malicious Strike",
      "type": "feature",
      "system": {
        "description": {
          "value": "<p><strong>5+ Malice.</strong> The monster's next strike deals extra damage equal to their highest characteristic score. Extra damage increases by 1 for each additional Malice spent (max 3x highest characteristic).</p><p><em>Cannot be used two rounds in a row.</em></p>",
          "director": ""
        },
        "source": {
          "book": "Monsters",
          "license": "Draw Steel Creator License"
        },
        "malice": {
          "cost": 5
        }
      },
      "_id": "MaliciousStrike001"
    },
    {
      "name": "Acid Breath",
      "type": "ability",
      "system": {
        "type": "main",
        "category": "signature",
        "keywords": ["area", "acid", "weapon"],
        "distance": {
          "type": "cone",
          "primary": 8
        },
        "target": {
          "type": "creature",
          "value": null
        },
        "power": {
          "roll": {
            "formula": "@chr",
            "characteristics": ["reason"]
          },
          "effects": {}
        },
        "effect": {
          "before": "<p><dl class=\"power-roll-display\"><dt class=\"tier1\"><p>!</p></dt><dd><p>[[/damage 15d6]] acid damage; [[/apply weakened end=save]] (R < 2).</p></dd><dt class=\"tier2\"><p>@</p></dt><dd><p>[[/damage 20d6]] acid damage; [[/apply weakened end=save]] (R < 3).</p></dd><dt class=\"tier3\"><p>#</p></dt><dd><p>[[/damage 25d6]] acid damage; [[/apply weakened and slowed end=save]] (R < 4).</p></dd></dl></p>",
          "after": ""
        },
        "source": {
          "book": "Monsters",
          "license": "Draw Steel Creator License"
        },
        "_dsid": "acid-breath"
      },
      "_id": "AcidBreathSignature1"
    },
    {
      "name": "Villain Action 1: Acid Deluge",
      "type": "ability",
      "system": {
        "type": "villain",
        "category": "villain",
        "keywords": ["area", "acid"],
        "distance": {
          "type": "burst",
          "primary": 5
        },
        "target": {
          "type": "creature",
          "value": null
        },
        "power": {
          "roll": {
            "formula": "@chr",
            "characteristics": ["reason"]
          },
          "effects": {}
        },
        "effect": {
          "before": "<p><strong>End of any creature's turn.</strong> The dragon breathes acid in a 5-square burst. Each target makes a Reason test.</p><p>- ≤11: [[/damage 10d6]] acid damage and [[/apply slowed end=save]]</p><p>- 12-16: [[/damage 15d6]] acid damage</p><p>- 17+: [[/damage 20d6]] acid damage</p>",
          "after": ""
        },
        "trigger": "End of any creature's turn",
        "resource": {
          "resettable": true
        },
        "source": {
          "book": "Monsters",
          "license": "Draw Steel Creator License"
        }
      },
      "_id": "VillainAction1Acid001"
    },
    {
      "name": "Villain Action 2: Swallow Whole",
      "type": "ability",
      "system": {
        "type": "villain",
        "category": "villain",
        "keywords": ["melee"],
        "distance": {
          "type": "melee",
          "primary": 1
        },
        "target": {
          "type": "creature",
          "value": 1
        },
        "power": {
          "roll": {
            "formula": "@chr",
            "characteristics": ["might"]
          },
          "effects": {}
        },
        "effect": {
          "before": "<p><strong>End of any creature's turn.</strong> The dragon attempts to swallow a Large or smaller creature. The target makes a Might test.</p><p>- ≤11: Swallowed and [[/apply grabbed]] (escape DC 15)</p><p>- 12-16: [[/damage 12]] acid damage</p><p>- 17+: [[/damage 8]] acid damage</p>",
          "after": ""
        },
        "trigger": "End of any creature's turn",
        "resource": {
          "resettable": true
        },
        "source": {
          "book": "Monsters",
          "license": "Draw Steel Creator License"
        }
      },
      "_id": "VillainAction2Swallow01"
    },
    {
      "name": "Villain Action 3: Death Roll",
      "type": "ability",
      "system": {
        "type": "villain",
        "category": "villain",
        "keywords": ["melee", "strike"],
        "distance": {
          "type": "melee",
          "primary": 1
        },
        "target": {
          "type": "creature",
          "value": 1
        },
        "power": {
          "roll": {
            "formula": "@chr",
            "characteristics": ["might"]
          },
          "effects": {}
        },
        "effect": {
          "before": "<p><strong>End of any creature's turn.</strong> The dragon makes a devastating bite attack.</p><p>- ≤11: [[/damage 18]] piercing; [[/apply prone]]</p><p>- 12-16: [[/damage 24]] piercing; [[/apply prone]]</p><p>- 17+: [[/damage 30]] piercing; [[/apply prone and grabbed]]</p>",
          "after": ""
        },
        "trigger": "End of any creature's turn",
        "resource": {
          "resettable": true
        },
        "source": {
          "book": "Monsters",
          "license": "Draw Steel Creator License"
        }
      },
      "_id": "VillainAction3Death001"
    }
  ],
  "_stats": {
    "systemId": "draw-steel",
    "systemVersion": "0.9.0"
  },
  "_id": "AncientBlackDragon001"
}
```

### Leader Monster with Villain Actions

```json
{
  "name": "Orc War Chief",
  "type": "npc",
  "img": "systems/draw-steel/assets/roles/leader.webp",
  "system": {
    "stamina": {
      "value": 60,
      "max": 60,
      "temporary": 0
    },
    "characteristics": {
      "might": {"value": 3},
      "agility": {"value": 2},
      "reason": {"value": 0},
      "intuition": {"value": 2},
      "presence": {"value": 3}
    },
    "combat": {
      "save": {"threshold": 7, "bonus": ""},
      "size": {"value": 1, "letter": "L"},
      "stability": 1,
      "turns": 1
    },
    "movement": {
      "value": 6,
      "types": ["walk"],
      "hover": false,
      "disengage": 1
    },
    "damage": {
      "immunities": {},
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
      "freeStrike": 6,
      "keywords": ["Humanoid", "Orc"],
      "level": 5,
      "ev": 28,
      "role": "brute",
      "organization": "leader"
    }
  },
  "prototypeToken": {
    "name": "Orc War Chief",
    "displayName": 20,
    "displayBars": 20,
    "bar1": {"attribute": "stamina"},
    "width": 1,
    "height": 1,
    "disposition": -1,
    "texture": {
      "src": "systems/draw-steel/assets/roles/leader.webp"
    }
  },
  "items": [
    {
      "name": "Brutal Effectiveness",
      "type": "feature",
      "system": {
        "description": {
          "value": "<p><strong>3 Malice.</strong> The monster's next ability with a potency has that potency increased by 1.</p>",
          "director": ""
        },
        "source": {
          "book": "Monsters",
          "license": "Draw Steel Creator License"
        },
        "malice": {
          "cost": 3
        }
      },
      "_id": "BrutalEffLeader001"
    },
    {
      "name": "Malicious Strike",
      "type": "feature",
      "system": {
        "description": {
          "value": "<p><strong>5+ Malice.</strong> The monster's next strike deals extra damage equal to their highest characteristic score. Extra damage increases by 1 for each additional Malice spent (max 3x highest characteristic).</p><p><em>Cannot be used two rounds in a row.</em></p>",
          "director": ""
        },
        "source": {
          "book": "Monsters",
          "license": "Draw Steel Creator License"
        },
        "malice": {
          "cost": 5
        }
      },
      "_id": "MaliciousStrikeLeader1"
    },
    {
      "name": "Commanding Shout",
      "type": "feature",
      "system": {
        "description": {
          "value": "<p><strong>7 Malice.</strong> Each ally within 5 squares gains 5 temporary stamina and advantage on their next attack.</p>",
          "director": ""
        },
        "source": {
          "book": "Monsters",
          "license": "Draw Steel Creator License"
        },
        "malice": {
          "cost": 7
        }
      },
      "_id": "CommandingShout001"
    },
    {
      "name": "Greataxe Strike",
      "type": "ability",
      "system": {
        "type": "main",
        "category": "signature",
        "keywords": ["melee", "strike", "weapon"],
        "distance": {
          "type": "melee",
          "primary": 1
        },
        "target": {
          "type": "creature",
          "value": 1
        },
        "power": {
          "roll": {
            "formula": "@chr",
            "characteristics": ["might"]
          },
          "effects": {}
        },
        "effect": {
          "before": "<p><dl class=\"power-roll-display\"><dt class=\"tier1\"><p>!</p></dt><dd><p>[[/damage 8]] slashing; [[/apply slowed end=save]] (M < 2).</p></dd><dt class=\"tier2\"><p>@</p></dt><dd><p>[[/damage 12]] slashing; [[/apply slowed end=save]] (M < 3).</p></dd><dt class=\"tier3\"><p>#</p></dt><dd><p>[[/damage 16]] slashing; [[/apply prone]] (M < 4).</p></dd></dl></p>",
          "after": ""
        },
        "source": {
          "book": "Monsters",
          "license": "Draw Steel Creator License"
        },
        "_dsid": "greataxe-strike"
      },
      "_id": "GreataxeStrike001"
    },
    {
      "name": "Villain Action 1: Rally the Troops",
      "type": "ability",
      "system": {
        "type": "villain",
        "category": "villain",
        "keywords": ["aura"],
        "distance": {
          "type": "aura",
          "primary": 5
        },
        "target": {
          "type": "creature",
          "value": null
        },
        "power": {
          "roll": {
            "formula": "@chr",
            "characteristics": []
          },
          "effects": {}
        },
        "effect": {
          "before": "<p><strong>End of any creature's turn.</strong> Each ally in the aura shifts up to their speed and can make a free strike.</p>",
          "after": ""
        },
        "trigger": "End of any creature's turn",
        "resource": {
          "resettable": true
        },
        "source": {
          "book": "Monsters",
          "license": "Draw Steel Creator License"
        }
      },
      "_id": "VA1RallyTroops001"
    },
    {
      "name": "Villain Action 2: Intimidating Roar",
      "type": "ability",
      "system": {
        "type": "villain",
        "category": "villain",
        "keywords": ["area"],
        "distance": {
          "type": "burst",
          "primary": 5
        },
        "target": {
          "type": "creature",
          "value": null
        },
        "power": {
          "roll": {
            "formula": "@chr",
            "characteristics": ["presence"]
          },
          "effects": {}
        },
        "effect": {
          "before": "<p><strong>End of any creature's turn.</strong> Each target makes a Presence test.</p><p>- ≤11: [[/apply frightened end=encounter]]</p><p>- 12-16: [[/apply slowed end=save]]</p><p>- 17+: No effect</p>",
          "after": ""
        },
        "trigger": "End of any creature's turn",
        "resource": {
          "resettable": true
        },
        "source": {
          "book": "Monsters",
          "license": "Draw Steel Creator License"
        }
      },
      "_id": "VA2Intimidate001"
    },
    {
      "name": "Villain Action 3: Decisive Strike",
      "type": "ability",
      "system": {
        "type": "villain",
        "category": "villain",
        "keywords": ["melee", "strike"],
        "distance": {
          "type": "melee",
          "primary": 1
        },
        "target": {
          "type": "creature",
          "value": 1
        },
        "power": {
          "roll": {
            "formula": "@chr",
            "characteristics": ["might"]
          },
          "effects": {}
        },
        "effect": {
          "before": "<p><strong>End of any creature's turn.</strong> The war chief makes a devastating strike against one target.</p><p>- ≤11: [[/damage 16]] slashing and [[/apply prone]]</p><p>- 12-16: [[/damage 24]] slashing</p><p>- 17+: [[/damage 32]] slashing and [[/apply prone]]</p>",
          "after": ""
        },
        "trigger": "End of any creature's turn",
        "resource": {
          "resettable": true
        },
        "source": {
          "book": "Monsters",
          "license": "Draw Steel Creator License"
        }
      },
      "_id": "VA3Decisive001"
    }
  ],
  "_stats": {
    "systemId": "draw-steel",
    "systemVersion": "0.9.0"
  },
  "_id": "OrcWarChief001"
}
```

### Key Differences: Malice Features vs Villain Actions

| Aspect | Malice Feature | Villain Action |
|--------|----------------|----------------|
| **Type** | `feature` | `ability` |
| **Trigger** | Start of monster's turn | End of any creature's turn |
| **Reuse** | Can be used multiple times per encounter | Can be used only once per encounter |
| **Limit per round** | No limit (spend malice as available) | Only 1 villain action per round total |
| **System type** | `malice.cost` in description | `system.type: "villain"` |
| **Resource** | Malice pool | `resource.resettable: true` |
| **Icon** | ⭐️, 🗡️, 🔳, ❇️, 🌀 | ☠️ |
| **Available to** | All organizations | **Leaders and Solos ONLY** |

### Critical Rule: Villain Actions Are Only for Leaders and Solos

**DO NOT add villain actions to:**
- Minion (any level)
- Horde (any level)
- Platoon (any level)
- Elite (any level)

**ONLY add villain actions to:**
- Leader
- Solo

Villain Actions represent coordinated tactics and dramatic moments appropriate for boss-level creatures. A Minotaur Skeleton Platoon Brute should not have villain actions - those belong to leaders and solos.
