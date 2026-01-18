# Draw Steel Monster Formulas Reference

This document provides the complete formulas and lookup tables for generating Draw Steel TTRPG monsters with 100% official compliance.

## Core Formulas (Official from Monster Basics.md)

All calculations use **ceil()** - round UP to the nearest whole number.

### Encounter Value (EV)
```
EV = ceil(((2 × Level) + 4) × Organization_Modifier)
```

### Stamina
```
Stamina = ceil(((10 × Level) + Role_Stamina_Modifier) × Organization_Modifier)
```

### Damage (any tier)
```
Damage = ceil((4 + Level + Role_Damage_Modifier) × Tier_Modifier)

For Horde and Minion: Damage = ceil(Damage ÷ 2)
```

### Free Strike
```
Free Strike = Damage at Tier 1 (ALWAYS!)
```

### Strike Bonus (from Monster Basics.md line 1360)
For abilities with the **Strike** keyword, add the monster's highest characteristic to the damage:

```
Damage = Base_Damage + Highest_Characteristic
```

**Example:** A Level 3 Brute (Might +2) making a strike at Tier 2:
- Base damage: 8
- Strike bonus: +2
- Final damage: 10

This bonus applies to all tiers of the power roll.

### Extra Stamina (Non-Minions Only)
```
Extra_Stamina = ceil((3 × Level) + 3)
```

---

## Organization Modifiers

| Organization | EV Modifier | Stamina Modifier | Damage Modifier | Notes |
|--------------|-------------|------------------|-----------------|-------|
| Minion | 0.5 | 0.5 | ÷2 | Squad-based Stamina |
| Horde | 0.5 | 0.5 | ÷2 | Outnumber ~2:1 |
| Platoon | 1.0 | 1.0 | 1.0 | Well-rounded |
| Elite | 2.0 | 2.0 | 2.0 | Hardy, ~2 heroes |
| Leader | 2.0 | 2.0 | 2.0 | Has villain actions |
| Solo | 6.0 | 6.0 | 6.0 | Full encounter alone |

---

## Role Modifiers

| Role | Stamina Modifier | Damage Modifier | Characteristic |
|------|------------------|-----------------|----------------|
| Ambusher | +20 | +1 | Agility |
| Artillery | +10 | +1 | Reason |
| Brute | +30 | +1 | Might |
| Controller | +10 | +0 | Reason |
| Defender | +30 | +0 | Might |
| Harrier | +20 | +0 | Agility |
| Hexer | +10 | +0 | Reason |
| Mount | +20 | +0 | Might/Agility |
| Support | +20 | +0 | Presence |

---

## Tier Multipliers

| Tier | Roll Range | Multiplier |
|------|------------|------------|
| Tier 1 | ≤11 | 0.6 |
| Tier 2 | 12-16 | 1.1 |
| Tier 3 | 17+ | 1.4 |

---

## Rounding Rules

| Stat | Rounding Method |
|------|-----------------|
| EV | `ceil()` |
| Stamina | `ceil()` |
| Free Strike | `ceil()` (equals T1 damage) |
| Damage | `ceil()` |

---

## Example Calculations

### Level 3 Platoon Harrier
- EV: `ceil(((2×3)+4) × 1.0) = ceil(10) = 10`
- Stamina: `ceil(((10×3)+20) × 1.0) = ceil(50) = 50`
- Free Strike: `ceil((4+3+0) × 0.6) = ceil(4.2) = 5`
- Damage T1: `ceil((4+3+0) × 0.6) = 5`
- Damage T2: `ceil((4+3+0) × 1.1) = ceil(7.7) = 8`
- Damage T3: `ceil((4+3+0) × 1.4) = ceil(9.8) = 10`

### Level 5 Solo Brute
- EV: `ceil(((2×5)+4) × 6.0) = ceil(14 × 6) = 84`
- Stamina: `ceil(((10×5)+30) × 6.0) = ceil(80 × 6) = 480`
- Free Strike: `ceil((4+5+1) × 0.6) = ceil(6.0) = 6`
- Damage T1: `ceil((4+5+1) × 0.6 × 6) = ceil(36) = 36`
- Damage T2: `ceil((4+5+1) × 1.1 × 6) = ceil(66) = 66`
- Damage T3: `ceil((4+5+1) × 1.4 × 6) = ceil(84) = 84`

### Level 1 Horde Controller
- EV: `ceil(((2×1)+4) × 0.5) = ceil(6 × 0.5) = 3`
- Stamina: `ceil(((10×1)+10) × 0.5) = ceil(20 × 0.5) = 10`
- Free Strike: `ceil((4+1+0) × 0.6) ÷ 2 = ceil(3.0) ÷ 2 = 2`
- Damage T1: `ceil((4+1+0) × 0.6) ÷ 2 = 2`
- Damage T2: `ceil((4+1+0) × 1.1) ÷ 2 = ceil(5.5) ÷ 2 = 3`
- Damage T3: `ceil((4+1+0) × 1.4) ÷ 2 = ceil(7.0) ÷ 2 = 4`

---

## Quick Reference: Level 1-10 Free Strike

| Level | Free Strike |
|-------|-------------|
| 1 | 3 |
| 2 | 4 |
| 3 | 5 |
| 4 | 5 |
| 5 | 6 |
| 6 | 7 |
| 7 | 7 |
| 8 | 8 |
| 9 | 9 |
| 10 | 9 |

*Note: Values vary by role and organization. Calculate using the formula.*

### Target Damage Scaling

When an ability targets more or fewer creatures than normal, adjust damage:

| Target Change | Multiplier |
|---------------|------------|
| -1 target | 1.2x |
| Normal | 1.0x |
| +1 target | 0.8x |
| +2+ targets | 0.5x |

**Example:** Elite Controller (normally 2 targets) targeting 3 creatures
- Base damage: 10
- Multiplier: 0.8x
- Final damage: 8 per tier
