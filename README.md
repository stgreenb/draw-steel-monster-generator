# Draw Steel Monster Generator

A Python tool and OpenCode skill for generating Draw Steel TTRPG monsters with 100% formula compliance using official mechanics from Monster Basics chapter.

## Features

- **Deterministic Calculations:** All stats computed using official Draw Steel formulas
- **100% Compliance:** No D&D terminology, uses correct 2d10 Power Rolls and tier outcomes
- **Dual-Mode:** CLI invocation + Python module import
- **9 Roles Supported:** Ambusher, Artillery, Brute, Controller, Defender, Harrier, Hexer, Mount, Support
- **6 Organizations:** Minion, Horde, Platoon, Elite, Leader, Solo
- **Comprehensive Testing:** 90%+ code coverage with pytest

## Quick Start

### Python Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ds-monster-generator.git
cd ds-monster-generator

# Install dependencies
pip install -r requirements.txt

# Or use Poetry
poetry install
```

### CLI Usage

```bash
# Calculate stats for a Level 3 Platoon Harrier
python scripts/calculate_stats.py --level 3 --organization Platoon --role Harrier

# Output in text format
python scripts/calculate_stats.py --level 5 --organization Solo --role Brute --format text
```

### Python Module Usage

```python
from scripts.calculate_stats import calculate_all_stats, Organization, Role

# Generate monster stats
stats = calculate_all_stats(
    level=3,
    organization="Platoon",
    role="Harrier"
)

print(stats)
# {'level': 3, 'organization': 'Platoon', 'role': 'Harrier', 
#  'ev': 10, 'stamina': 50, 'free_strike': 5, 
#  'damage_t1': 5, 'damage_t2': 8, 'damage_t3': 10, 'error': None}
```

### OpenCode Usage

1. Copy `SKILL.md` to your OpenCode skills directory:
   - Global: `~/.config/opencode/skills/draw-steel-monster-generator/`
   - Project: `.opencode/skills/draw-steel-monster-generator/`

2. Run skill discovery:
   ```bash
   opencode skill list
   ```

3. Generate a monster:
   ```bash
   opencode run "Create a Level 3 Griffin, Platoon, Harrier"
   ```

## Formulas

All calculations use `ceil()` (round UP):

| Stat | Formula |
|------|---------|
| EV | `ceil(((2 × Level) + 4) × Organization_Modifier)` |
| Stamina | `ceil(((10 × Level) + Role_Modifier) × Organization_Modifier)` |
| Damage | `ceil((4 + Level + Damage_Modifier) × Tier_Modifier)` |
| Free Strike | Equals Tier 1 damage |

**Tier Multipliers:** T1=0.6, T2=1.1, T3=1.4

**Horde/Minion:** Damage divided by 2

See [formulas.md](formulas.md) for complete reference.

## Project Structure

```
ds-monster-generator/
├── SKILL.md              # OpenCode skill definition
├── formulas.md           # Formula reference
├── templates.md          # Ability templates by role
├── examples.md           # 5 complete creature examples
├── scripts/
│   └── calculate_stats.py # Python calculation engine
├── tests/
│   └── test_calculate_stats.py
├── .github/workflows/
│   ├── test.yml          # CI/CD test workflow
│   └── release.yml       # Release automation
├── pyproject.toml        # Poetry configuration
├── .flake8               # Linting config
├── .pre-commit-config.yaml
├── CHANGELOG.md
└── LICENSE
```

## Development

### Setup

```bash
# Install with dev dependencies
poetry install

# Activate virtual environment
poetry shell

# Run tests
pytest tests/ -v --cov=scripts

# Run with coverage report
pytest tests/ --cov=scripts --cov-report=html
```

### Code Quality

```bash
# Format code
black scripts/ tests/

# Lint
flake8 scripts/ tests/

# Type check
mypy scripts/
```

### Pre-commit Hooks

```bash
pre-commit install
pre-commit run --all-files
```

## Documentation

- [Formulas Reference](formulas.md) - Complete formula documentation
- [Ability Templates](templates.md) - Role-based ability patterns
- [Examples](examples.md) - 5 complete creature stat blocks
- [OpenSpec Change Proposal](openspec/changes/add-draw-steel-monster-generator/proposal.md)

## Troubleshooting

**Invalid level error:** Levels must be 1-10

**Invalid organization/role:** Check spelling against supported values:
- Organizations: Minion, Horde, Platoon, Elite, Leader, Solo
- Roles: Ambusher, Artillery, Brute, Controller, Defender, Harrier, Hexer, Mount, Support

**Zero damage for Horde/Minion:** This is correct - weaker creatures deal less damage

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit pull request

## License

MIT License - see [LICENSE](LICENSE) file.

## Acknowledgments

- Draw Steel TTRPG by MCDM Productions
- OpenCode for skill framework
- Draw Steel community for validation
