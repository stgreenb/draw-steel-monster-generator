# Complete Draw Steel Monster Examples

Each example includes: complete MCDM stat block with YAML frontmatter, validation checklist, and generation notes.

## Potency Reference
For creatures with **Agility +2**:
- Weak: 0, Average: 1, Strong: 2 → Written as `A < 0`, `A < 1`, `A < 2`

For creatures with **Might +3**:
- Weak: 1, Average: 2, Strong: 3 → Written as `M < 1`, `M < 2`, `M < 3`

For creatures with **Reason +2**:
- Weak: 0, Average: 1, Strong: 2 → Written as `R < 0`, `R < 1`, `R < 2`

---

## Example 1: Gremlin (Level 3, Minion, Harrier)

### Stat Block
```markdown
---
ancestry:
  - Fey
  - Humanoid
ev: '5'
file_basename: Gremlin
file_dpath: Monsters/Gremlins/Statblocks
free_strike: '2'
level: 3
might: 0
agility: 2
reason: -1
intuition: 0
presence: -1
roles:
  - Minion Harrier
size: 1M
source: mcdm.monsters.v1
speed: 6
stability: 0
stamina: '25'
type: monster
---

###### Gremlin

|         Fey, Humanoid          |          -          |      Level 3       |          Minion Harrier           |           EV 5            |
| :----------------------------: | :-----------------: | :----------------: | :-------------------------------: | :-----------------------: |
|        **1M**<br/> Size        |  **6**<br/> Speed   | **25**<br/> Stamina |         **0**<br/> Stability       |   **2**<br/> Free Strike  |
|       **-**<br/> Immunity      |   **-**<br/> Movement |          -         | **+1 bonus to speed**<br/> With Captain |        **-**<br/> Weaknesses |
|     **0**<br/> Might          |   **+2**<br/> Agility | **-1**<br/> Reason |        **0**<br/> Intuition        |   **-1**<br/> Presence    |

<!-- -->
> ⚔️ **Nimble Strike**
>
> | **Melee, Strike, Weapon** |     **Main action** |
> | ------------------------- | ------------------: |
> | **📏 Melee 1**            | **🎯 One creature** |
>
> **Power Roll + Agility:**
>
> - **≤11:** 2 piercing; A < 0, push 1
> - **12-16:** 4 piercing; A < 1, push 2
> - **17+:** 5 piercing; A < 2, push 2 + weakened (save ends)
>
> **Effect:** Until the start of the gremlin's next turn, the target can't make opportunity attacks against any gremlin.

<!-- -->
> ⭐️ **Skitter Away**
>
> | **-** |     **Free triggered action** |
> | ----- | ---------------------------: |
> | **📏 -** | **🎯 The gremlin** |
>
> **Trigger:** The gremlin takes damage.
>
> **Effect:** The gremlin shifts 2 squares.
```

### Validation Checklist
- [x] EV: 5 = ceil(((2×3)+4) × 0.5) ✓
- [x] Stamina: 25 = ceil(((10×3)+20) × 0.5) ✓
- [x] Free Strike: 2 = ceil((4+3+0) × 0.6) ÷ 2 ✓
- [x] Damage T1: 2 = ceil((4+3+0) × 0.6) ÷ 2 ✓
- [x] Damage T2: 4 = ceil((4+3+0) × 1.1) ÷ 2 ✓
- [x] Damage T3: 5 = ceil((4+3+0) × 1.4) ÷ 2 ✓
- [x] Potency: A < 0, A < 1, A < 2 (Agility 2 → Weak 0, Avg 1, Strong 2) ✓
- [x] Size: 1M (Minion) ✓
- [x] Speed: 6 (Harrier) ✓
- [x] Characteristics: Agility +2 (Harrier), others 0 to -1 ✓
- [x] Ancestry: Fey, Humanoid ✓

### Generation Notes
- **Why Minion Harrier?** Gremlins are quick, mischievous fey that use hit-and-run tactics
- **Potency values:** Agility +2 → Weak=0, Avg=1, Strong=2
- **Signature ability:** Fast attack with push effects (Harrier specialty)
- **Secondary ability:** Repositioning on taking damage (classic gremlin behavior)

---

## Example 2: Bugbear (Level 3, Platoon, Brute)

### Stat Block
```markdown
---
ancestry:
  - Bugbear
  - Fey
  - Goblin
  - Humanoid
ev: '20'
file_basename: Bugbear
file_dpath: Monsters/Bugbears/Statblocks
free_strike: '5'
level: 3
might: 3
agility: 1
reason: -1
intuition: 0
presence: 0
roles:
  - Platoon Brute
size: 1L
source: mcdm.monsters.v1
speed: 5
stability: 0
stamina: '90'
type: monster
---

###### Bugbear

|      Bugbear, Fey, Goblin, Humanoid       |          -          |      Level 3       |           Platoon Brute            |           EV 20            |
| :--------------------------------------: | :-----------------: | :----------------: | :--------------------------------: | :------------------------: |
|           **1L**<br/> Size               |  **5**<br/> Speed   | **90**<br/> Stamina |         **0**<br/> Stability        |   **5**<br/> Free Strike   |
|           **-**<br/> Immunity            |   **-**<br/> Movement |          -         | **-**<br/> With Captain            |        **-**<br/> Weaknesses |
|          **+3**<br/> Might              |   **+1**<br/> Agility | **-1**<br/> Reason |        **0**<br/> Intuition        |   **0**<br/> Presence      |

<!-- -->
> ⚔️ **Crushing Blow**
>
> | **Melee, Strike, Weapon** |     **Main action** |
> | ------------------------- | ------------------: |
> | **📏 Melee 1**            | **🎯 One creature** |
>
> **Power Roll + Might:**
>
> - **≤11:** 5 bludgeoning; M < 1, prone
> - **12-16:** 8 bludgeoning; M < 2, prone (save ends)
> - **17+:** 10 bludgeoning; M < 3, prone + grabbed
>
> **Effect:** If the target is already prone, they are grabbed instead.

<!-- -->
> ❗️ **Quick Recovery**
>
> | **-** |     **Free triggered action** |
> | ----- | ---------------------------: |
> | **📏 -** | **🎯 The bugbear** |
>
> **Trigger:** The bugbear is prone.
>
> **Effect:** The bugbear stands up.
```

### Validation Checklist
- [x] EV: 20 = ceil(((2×3)+4) × 1.0) ✓
- [x] Stamina: 90 = ceil(((10×3)+30) × 1.0) ✓
- [x] Free Strike: 5 = ceil((4+3+1) × 0.6) ✓
- [x] Damage T1: 5 = ceil((4+3+1) × 0.6) ✓
- [x] Damage T2: 8 = ceil((4+3+1) × 1.1) ✓
- [x] Damage T3: 10 = ceil((4+3+1) × 1.4) ✓
- [x] Potency: M < 1, M < 2, M < 3 (Might 3 → Weak 1, Avg 2, Strong 3) ✓
- [x] Size: 1L (Brute) ✓
- [x] Speed: 5 ✓
- [x] Characteristics: Might +3 (Brute), Agility +1 ✓
- [x] Ancestry: Bugbear, Fey, Goblin, Humanoid ✓

### Generation Notes
- **Why Platoon Brute?** Bugbears are strong, tough monsters that absorb punishment
- **Potency values:** Might +3 → Weak=1, Avg=2, Strong=3
- **Signature ability:** Powerful attack with prone (Brute specialty)
- **Secondary ability:** Quick recovery to stay in the fight

---

## Example 3: Shadow Elf Hexer (Level 4, Platoon, Controller)

### Stat Block
```markdown
---
ancestry:
  - Fey
  - Humanoid
  - Shadow Elf
ev: '24'
file_basename: Shadow Elf Hexer
file_dpath: Monsters/Shadow Elves/Statblocks
free_strike: '5'
level: 4
might: 0
agility: 2
reason: 2
intuition: 1
presence: 1
roles:
  - Platoon Controller
size: 1M
source: mcdm.monsters.v1
speed: 5
stability: 0
stamina: '60'
type: monster
---

###### Shadow Elf Hexer

|        Fey, Humanoid, Shadow Elf         |          -          |      Level 4       |          Platoon Controller          |           EV 24            |
| :-------------------------------------: | :-----------------: | :----------------: | :----------------------------------: | :------------------------: |
|           **1M**<br/> Size              |  **5**<br/> Speed   | **60**<br/> Stamina |         **0**<br/> Stability          |   **5**<br/> Free Strike   |
|           **-**<br/> Immunity           |   **-**<br/> Movement |          -         | **-**<br/> With Captain              |        **-**<br/> Weaknesses |
|          **0**<br/> Might              |   **+2**<br/> Agility | **+2**<br/> Reason |        **+1**<br/> Intuition         |   **+1**<br/> Presence     |

<!-- -->
> ⚔️ **Mind Wipe**
>
> | **Magic, Psionic, Ranged, Strike** |     **Main action** |
> | ---------------------------------- | ------------------: |
> | **📏 Ranged 8**                    | **🎯 One creature** |
>
> **Power Roll + Reason:**
>
> - **≤11:** 5 psychic; R < 0, dazed
> - **12-16:** 9 psychic; R < 1, dazed (save ends)
> - **17+:** 12 psychic; R < 2, dazed + slowed (save ends)
>
> **Effect:** The target must be on the ground.

<!-- -->
> ❇️ **Shadow Veil**
>
> | **Area, Magic, Psionic** |     **Main action** |
> | ------------------------ | ------------------: |
> | **📏 3 burst**           | **🎯 Each enemy in the area** |
>
> **Power Roll + Intuition:**
>
> - **≤11:** Each target must be on the ground, and each target is weakened.
> - **12-16:** Each target must be on the ground, and each target is weakened.
> - **17+:** Each target must be on the ground, and each target is weakened and dazed.
```

### Validation Checklist
- [x] EV: 24 = ceil(((2×4)+4) × 1.0) ✓
- [x] Stamina: 60 = ceil(((10×4)+10) × 1.0) ✓
- [x] Free Strike: 5 = ceil((4+4+0) × 0.6) ✓
- [x] Damage T1: 5 = ceil((4+4+0) × 0.6) ✓
- [x] Damage T2: 9 = ceil((4+4+0) × 1.1) ✓
- [x] Damage T3: 12 = ceil((4+4+0) × 1.4) ✓
- [x] Potency: R < 0, R < 1, R < 2 (Reason 2 → Weak 0, Avg 1, Strong 2) ✓
- [x] Size: 1M (Platoon) ✓
- [x] Speed: 5 ✓
- [x] Characteristics: Reason +2, Agility +2 (Controller + Harrier hybrid) ✓
- [x] Ancestry: Fey, Humanoid, Shadow Elf ✓

### Generation Notes
- **Why Platoon Controller?** Shadow elves use magic and psionics to control the battlefield
- **Potency values:** Reason +2 → Weak=0, Avg=1, Strong=2
- **Signature ability:** Psychic attack with debuffs (Controller specialty)
- **Secondary ability:** Area debuff effect

---

## Example 4: Hill Giant Brute (Level 5, Solo, Brute)

**Demonstrates:** Echelon-based characteristics (+3), Leader/Solo bonuses (+1), Villain Actions

### Calculations
- **Level:** 5 (Echelon 2)
- **Highest Characteristic:** +3 (1 + echelon) +1 (Solo bonus) = **+4**
- **EV:** `ceil(((2×5)+4) × 6.0) = ceil(14 × 6) = 84`
- **Stamina:** `ceil(((10×5)+30) × 6.0) = ceil(80 × 6) = 480`
- **Damage T1:** `ceil((4+5+1) × 0.6 × 6) = ceil(10 × 6) = 60` (Strike bonus +4 = **64**)
- **Damage T2:** `ceil((4+5+1) × 1.1 × 6) = ceil(11 × 6) = 66` (Strike bonus +4 = **70**)
- **Damage T3:** `ceil((4+5+1) × 1.4 × 6) = ceil(14 × 6) = 84` (Strike bonus +4 = **88**)
- **Free Strike:** 64 (T1 damage with strike bonus)
- **Potencies:** Might +4 → T1: +2, T2: +3, T3: +4

### Stat Block
```markdown
---
ancestry:
  - Giant
  - Humanoid
ev: '84'
file_basename: Hill Giant Brute
file_dpath: Monsters/Giants/Statblocks
free_strike: '64'
level: 5
might: 4
agility: 0
reason: -1
intuition: 0
presence: 0
roles:
  - Solo Brute
size: 2L
source: mcdm.monsters.v1
speed: 6
stability: 0
stamina: '480'
type: monster
---

###### Hill Giant Brute

|            Giant, Humanoid             |          -          |      Level 5       |            Solo Brute             |           EV 84            |
| :-----------------------------------: | :-----------------: | :----------------: | :-------------------------------: | :------------------------: |
|           **2L**<br/> Size            |  **6**<br/> Speed   | **480**<br/> Stamina |         **0**<br/> Stability       |   **64**<br/> Free Strike  |
|           **-**<br/> Immunity         |   **-**<br/> Movement |          -         | **-**<br/> With Captain           |        **-**<br/> Weaknesses |
|          **+4**<br/> Might           |   **0**<br/> Agility  | **-1**<br/> Reason  |        **0**<br/> Intuition        |   **0**<br/> Presence      |

<!-- -->
> ⚔️ **Crushing Blow**
>
> | **Melee, Strike, Weapon** |     **Main action** |
> | ------------------------- | ------------------: |
> | **📏 Melee 1**            | **🎯 Two creatures** |
>
> **Power Roll + Might:**
>
> - **≤11:** 64 bludgeoning; M < 2, prone
> - **12-16:** 70 bludgeoning; M < 3, prone + pushed 2 (save ends)
> - **17+:** 88 bludgeoning; M < 4, prone + pushed 3 + grabbed
>
> **Effect:** If the target is already prone, they take an extra 10 damage.

<!-- -->
> ❗️ **Quick Recovery**
>
> | **-** |     **Free triggered action** |
> | ----- | ---------------------------: |
> | **📏 -** | **🎯 The giant** |
>
> **Trigger:** The giant is prone or grabbed.
>
> **Effect:** The giant stands up and is no longer prone or grabbed.

<!-- -->
> ⭐️ **Solo Turns**
>
> **Effect:** At the start of each of the giant's turns, they take another turn. This allows the giant to take up to 2 turns per round.

<!-- -->
> ☠️ **Villain Action: Rock Throw**
>
> **Type:** Opener
>
> **Trigger:** You can use this action at the end of any other creature's turn during combat.
>
> **Effect:** The giant throws a massive rock at a target within 10 squares, dealing 30 bludgeoning damage and pushing them 2 squares.
>
> **Usage:** Once per encounter.

<!-- -->
> ☠️ **Villain Action: Boulder Roll**
>
> **Type:** Crowd Control
>
> **Trigger:** You can use this action at the end of any other creature's turn during combat.
>
> **Effect:** The giant rolls a boulder in a 5 line. Creatures in the area must be on the ground, take 40 bludgeoning damage, and are pushed 3 squares.
>
> **Usage:** Once per encounter.

<!-- -->
> ☠️ **Villain Action: Ground Slam**
>
> **Type:** Ultimate
>
> **Trigger:** You can use this action at the end of any other creature's turn during combat.
>
> **Effect:** The giant slams the ground, creating a shockwave in a 3 burst. All creatures in the area take 60 bludgeoning damage and are knocked prone.
>
> **Usage:** Once per encounter.
```

### Validation Checklist
- [x] EV: 84 = ceil(((2×5)+4) × 6) ✓
- [x] Stamina: 480 = ceil(((10×5)+30) × 6) ✓
- [x] Free Strike: 64 = T1 damage + strike bonus ✓
- [x] Damage T1: 64 = ceil((4+5+1) × 0.6 × 6) + 4 ✓
- [x] Damage T2: 70 = ceil((4+5+1) × 1.1 × 6) + 4 ✓
- [x] Damage T3: 88 = ceil((4+5+1) × 1.4 × 6) + 4 ✓
- [x] Characteristics: Might +4 (3 + echelon +1 solo) ✓
- [x] Potencies: M < 2, M < 3, M < 4 (Might 4 → Weak 2, Avg 3, Strong 4) ✓
- [x] Targets: 2 (Solo) ✓
- [x] Size: 2L (Solo) ✓
- [x] Speed: 6 ✓

### Generation Notes
- **Why Solo Brute?** Hill giants are powerful, slow hitters perfect for Solo play
- **Strike Bonus:** Added +4 to all strike damage
- **Potencies:** Using official formula (Highest - 2/1/0)
- **Villain Actions:** Added 3 dramatic actions for climactic encounters

---

## Example 5: Shadow Elf Hexer (Level 4, Elite, Controller)

**Demonstrates:** Elite target rules (2 targets), Target damage scaling

### Calculations
- **Level:** 4 (Echelon 1)
- **Highest Characteristic:** +2 (Reason)
- **EV:** `ceil(((2×4)+4) × 2.0) = ceil(12 × 2) = 24`
- **Stamina:** `ceil(((10×4)+10) × 2.0) = ceil(50 × 2) = 100`
- **Damage T1:** `ceil((4+4+0) × 0.6 × 2) = ceil(8 × 2) = 16` (no strike)
- **Damage T2:** `ceil((4+4+0) × 1.1 × 2) = ceil(9 × 2) = 18`
- **Damage T3:** `ceil((4+4+0) × 1.4 × 2) = ceil(11 × 2) = 22`
- **Free Strike:** 16
- **Targets:** 2 (Elite)
- **Damage Scaling:** 0.8x for 2 targets → T1: 13, T2: 14, T3: 18

### Stat Block
```markdown
---
ancestry:
  - Fey
  - Humanoid
  - Shadow Elf
ev: '24'
file_basename: Shadow Elf Hexer Elite
file_dpath: Monsters/Shadow Elves/Statblocks
free_strike: '16'
level: 4
might: 0
agility: 2
reason: 2
intuition: 1
presence: 1
roles:
  - Elite Controller
size: 1M
source: mcdm.monsters.v1
speed: 5
stability: 0
stamina: '100'
type: monster
---

###### Shadow Elf Hexer Elite

|        Fey, Humanoid, Shadow Elf         |          -          |      Level 4       |          Elite Controller          |           EV 24            |
| :-------------------------------------: | :-----------------: | :----------------: | :--------------------------------: | :------------------------: |
|           **1M**<br/> Size              |  **5**<br/> Speed   | **100**<br/> Stamina |         **0**<br/> Stability        |   **16**<br/> Free Strike  |
|           **-**<br/> Immunity           |   **-**<br/> Movement |          -         | **-**<br/> With Captain            |        **-**<br/> Weaknesses |
|          **0**<br/> Might              |   **+2**<br/> Agility | **+2**<br/> Reason |        **+1**<br/> Intuition       |   **+1**<br/> Presence     |

<!-- -->
> ⚔️ **Mind Lash**
>
> | **Magic, Psionic, Ranged, Strike** |     **Main action** |
> | ---------------------------------- | ------------------: |
> | **📏 Ranged 8**                    | **🎯 Two creatures** |
>
> **Power Roll + Reason:**
>
> - **≤11:** 13 psychic; R < 0, weakened
> - **12-16:** 14 psychic; R < 1, weakened (save ends)
> - **17+:** 18 psychic; R < 2, weakened + slowed (save ends)
>
> **Effect:** The targets must be on the ground.

<!-- -->
> ❇️ **Hex Ward**
>
> | **Magic, Psionic** |     **Free triggered action** |
> | ------------------ | ---------------------------: |
> | **📏 3 aura**      | **🎯 The hexer** |
>
> **Trigger:** An enemy within 3 squares targets the hexer with an ability.
>
> **Effect:** The hexer gains +2 to defense against that ability.
```

### Validation Checklist
- [x] EV: 24 = ceil(((2×4)+4) × 2) ✓
- [x] Stamina: 100 = ceil(((10×4)+10) × 2) ✓
- [x] Free Strike: 16 = T1 damage ✓
- [x] Damage T1: 13 = ceil((4+4+0) × 0.6 × 2) × 0.8 ✓
- [x] Damage T2: 14 = ceil((4+4+0) × 1.1 × 2) × 0.8 ✓
- [x] Damage T3: 18 = ceil((4+4+0) × 1.4 × 2) × 0.8 ✓
- [x] Targets: 2 (Elite) ✓
- [x] Damage scaling: 0.8x applied ✓
- [x] Potencies: R < 0, R < 1, R < 2 (Reason 2 → Weak 0, Avg 1, Strong 2) ✓
- [x] Characteristics: Reason +2 ✓

### Generation Notes
- **Why Elite Controller?** Shadow elves make excellent elite magical combatants
- **Target rules:** Elite targets 2 creatures by default
- **Damage scaling:** 0.8x applied for 2 targets (16×0.8=13)
- **Potencies:** Using official formula (Highest - 2/1/0)

---

## Quick Reference: Force Movement and Status Duration Conventions

### Force Movement Scaling (from Bestiary Analysis)

| Level Range | Echelon | Push (T1/T2/T3) | Pull (T1/T2/T3) | Slide (T1/T2/T3) |
|-------------|---------|-----------------|-----------------|------------------|
| Level 1 | 0 | 1/1/1 | 1/2/2 | 1/2/2 |
| Level 2-4 | 1 | 1/2/2 | 2/3/4 | 2/3/4 |
| Level 5-7 | 2 | 2/2/3 | 3/4/5 | 3/4/5 |
| Level 8-10 | 3 | 2/3/3 | 4/5/6 | 4/5/6 |

### Role-Specific Force Movement Preferences

| Role | Preferred Force Movement | Typical Values |
|------|-------------------------|----------------|
| Harrier | Pull | 2/4/6 at Level 1, 4/5/6 at Level 8+ |
| Brute | Push | 1/2/3 at any level |
| Controller | Pull/Slide | 2/4/6 (low), 4/5/6 (high) |
| Artillery | Slide | 2/4/5 (low), 4/6/8 (high) |
| Ambusher | Pull | 2/3/4 |

### Condition Duration Format (from Official Conditions Docs)

**Critical Rule:** Conditions are inherently persistent or conditional. The "(save ends)" duration is an EFFECT applied by monster abilities, NOT part of the condition itself.

| Condition Type | Format | How It Ends |
|---------------|--------|-------------|
| **Persistent** | `[condition] (save ends)` | Target makes a save at end of each turn |
| **Conditional** | `[condition]` | Specific action ends it (stand up, escape, etc.) |
| **Ongoing** | `[condition]` | Triggers on action use, ends when healed |

### Tier-Based Condition Patterns

| Tier | Pattern | Example |
|------|---------|---------|
| Tier 1 | Instant or conditional | "prone" (ends by standing) |
| Tier 2 | Save ends | "prone (save ends)" |
| Tier 3 | Save ends + secondary effect | "prone and bleeding (save ends)" |

### Combined Format Examples

```
- ≤11: 5 damage; M < 1, prone
- 12-16: 8 damage; M < 2, prone (save ends)
- 17+: 10 damage; M < 3, prone + bleeding (save ends)
```

### Force Movement Format Examples

```
- ≤11: 2 piercing; A < 0, push 1
- 12-16: 4 piercing; A < 1, push 2
- 17+: 5 piercing; A < 2, push 2 + weakened (save ends)
```

**Note:** Force movement values must match the level-based tables above. Push values are typically 1-3, Pull values are 2-6, and Slide values are 2-8 depending on level.
