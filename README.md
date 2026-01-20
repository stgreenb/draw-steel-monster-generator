# Draw Steel Monster Generator

OpenCode skill for generating Draw Steel TTRPG monsters with Foundry VTT JSON output.

## Usage

```
opencode run "Create a Level 3 Griffin, Platoon, Harrier"
opencode run "Convert Slaad from D&D 5e, Level 5, Solo, Controller"
```

## Features

- **Formula-compliant** - Uses official Draw Steel monster creation rules
- **Foundry VTT ready** - Generates import-ready JSON
- **Cross-system conversion** - Convert monsters from other TTRPGs

## Project Structure

- `SKILL.md` - OpenCode skill definition
- `scripts/validate_foundry_json.py` - Foundry JSON validator
- `output/` - Generated monster JSON files

## Validation

```bash
python scripts/validate_foundry_json.py output/Monsters
```
