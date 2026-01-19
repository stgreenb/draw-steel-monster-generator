#!/usr/bin/env python3
"""
Foundry VTT JSON Validation Script for Draw Steel Monster Generator

This script validates generated monster JSON files against common errors
that cause import failures in Foundry VTT.
"""

import json
import re
import sys
from pathlib import Path

# Valid Draw Steel monster keywords
VALID_MONSTER_KEYWORDS = {
    "abyssal",
    "accursed",
    "animal",
    "beast",
    "construct",
    "dragon",
    "elemental",
    "fey",
    "giant",
    "horror",
    "humanoid",
    "infernal",
    "plant",
    "soulless",
    "swarm",
    "undead",
}

# Valid ability keywords
VALID_ABILITY_KEYWORDS = {
    "animal",
    "animapathy",
    "area",
    "charge",
    "chronopathy",
    "cryokinesis",
    "earth",
    "fire",
    "green",
    "magic",
    "melee",
    "metamorphosis",
    "psionic",
    "pyrokinesis",
    "ranged",
    "resopathy",
    "rot",
    "performance",
    "strike",
    "telekinesis",
    "telepathy",
    "void",
    "weapon",
}

# Valid monster roles
VALID_MONSTER_ROLES = {
    "ambusher",
    "artillery",
    "brute",
    "controller",
    "defender",
    "harrier",
    "hexer",
    "mount",
    "support",
    "solo",
}

# Valid monster organizations
VALID_MONSTER_ORGANIZATIONS = {"minion", "horde", "platoon", "elite", "leader", "solo"}

# Valid ability types
VALID_ABILITY_TYPES = {
    "main",
    "maneuver",
    "freeManeuver",
    "triggered",
    "freeTriggered",
    "move",
    "none",
    "villain",
}

# Valid ability categories
VALID_ABILITY_CATEGORIES = {"heroic", "freeStrike", "signature", "villain"}

# Valid item types for monsters
VALID_ITEM_TYPES = {"ability", "feature"}


class ValidationResult:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.passed = True

    def add_error(self, message):
        self.errors.append(message)
        self.passed = False

    def add_warning(self, message):
        self.warnings.append(message)

    def is_valid(self):
        return self.passed

    def print_report(self, filename: str):
        """Print a validation report for the given file."""
        print(f"\n{'=' * 60}")
        print(f"Validation Report: {filename}")
        print(f"{'=' * 60}")

        if self.passed and not self.warnings:
            print("✓ PASSED - No errors or warnings found")
            return

        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for i, error in enumerate(self.errors, 1):
                print(f"  {i}. {error}")

        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for i, warning in enumerate(self.warnings, 1):
                print(f"  {i}. {warning}")

        print(f"\nStatus: {'✓ PASSED' if self.passed else '❌ FAILED'}")


def is_valid_16_char_id(value: str) -> bool:
    """Check if value is exactly 16 alphanumeric characters."""
    if not isinstance(value, str):
        return False
    return bool(re.match(r"^[a-zA-Z0-9]{16}$", value))


def validate_actor_type(data: dict, result: ValidationResult) -> None:
    """Validate that actor type is 'npc'."""
    actor_type = data.get("type")
    if actor_type != "npc":
        result.add_error(f"Actor type must be 'npc', got '{actor_type}'")


def validate_item_types(data: dict, result: ValidationResult) -> None:
    """Validate that all items have valid types."""
    items = data.get("items", [])
    for item in items:
        item_type = item.get("type")
        if item_type not in VALID_ITEM_TYPES:
            result.add_error(
                f"Item '{item.get('name', 'Unknown')}' has invalid type '{item_type}'. "
                f"Must be one of: {', '.join(sorted(VALID_ITEM_TYPES))}"
            )


def validate_ability_type(data: dict, result: ValidationResult) -> None:
    """Validate ability system.type values."""
    items = data.get("items", [])
    for item in items:
        if item.get("type") == "ability":
            system = item.get("system", {})
            ability_type = system.get("type")
            if ability_type and ability_type not in VALID_ABILITY_TYPES:
                result.add_error(
                    f"Ability '{item.get('name', 'Unknown')}' has invalid type '{ability_type}'. "
                    f"Must be one of: {', '.join(sorted(VALID_ABILITY_TYPES))}"
                )


def validate_ability_category(data: dict, result: ValidationResult) -> None:
    """Validate ability system.category values."""
    items = data.get("items", [])
    for item in items:
        if item.get("type") == "ability":
            system = item.get("system", {})
            category = system.get("category")
            if category and category not in VALID_ABILITY_CATEGORIES:
                result.add_error(
                    f"Ability '{item.get('name', 'Unknown')}' has invalid category '{category}'. "
                    f"Must be one of: {', '.join(sorted(VALID_ABILITY_CATEGORIES))} or empty"
                )


def validate_monster_role(data: dict, result: ValidationResult) -> None:
    """Validate monster role."""
    system = data.get("system", {})
    monster = system.get("monster", {})
    role = monster.get("role")
    if role and role not in VALID_MONSTER_ROLES:
        result.add_error(
            f"Invalid monster role '{role}'. "
            f"Must be one of: {', '.join(sorted(VALID_MONSTER_ROLES))}"
        )


def validate_monster_organization(data: dict, result: ValidationResult) -> None:
    """Validate monster organization."""
    system = data.get("system", {})
    monster = system.get("monster", {})
    org = monster.get("organization")
    if org and org not in VALID_MONSTER_ORGANIZATIONS:
        result.add_error(
            f"Invalid monster organization '{org}'. "
            f"Must be one of: {', '.join(sorted(VALID_MONSTER_ORGANIZATIONS))}"
        )


def validate_monster_keywords(data: dict, result: ValidationResult) -> None:
    """Validate monster keywords."""
    system = data.get("system", {})
    monster = system.get("monster", {})
    keywords = monster.get("keywords", [])

    for keyword in keywords:
        if keyword not in VALID_MONSTER_KEYWORDS:
            result.add_error(
                f"Invalid monster keyword '{keyword}'. "
                f"Must be one of: {', '.join(sorted(VALID_MONSTER_KEYWORDS))}"
            )


def validate_ability_keywords(data: dict, result: ValidationResult) -> None:
    """Validate ability keywords."""
    items = data.get("items", [])
    for item in items:
        if item.get("type") == "ability":
            system = item.get("system", {})
            keywords = system.get("keywords", [])

            for keyword in keywords:
                if keyword not in VALID_ABILITY_KEYWORDS:
                    result.add_error(
                        f"Ability '{item.get('name', 'Unknown')}' has invalid keyword '{keyword}'. "
                        f"Must be one of: {', '.join(sorted(VALID_ABILITY_KEYWORDS))}"
                    )


def validate_id_format(data: dict, result: ValidationResult, path: str = "") -> None:
    """Validate that all _id fields are exactly 16 alphanumeric characters."""
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{path}.{key}" if path else key
            if key == "_id":
                if not is_valid_16_char_id(value):
                    if isinstance(value, str) and "-" in value:
                        result.add_error(
                            f"{new_path} contains UUID format (contains dashes). "
                            f"Must be exactly 16 alphanumeric characters, got: {value}"
                        )
                    elif isinstance(value, str) and len(value) != 16:
                        result.add_error(
                            f"{new_path} has invalid length. "
                            f"Must be exactly 16 characters, got {len(value)}: {value}"
                        )
                    else:
                        result.add_error(
                            f"{new_path} contains invalid characters. "
                            f"Must be exactly 16 alphanumeric characters, got: {value}"
                        )
            else:
                validate_id_format(value, result, new_path)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            validate_id_format(item, result, f"{path}[{i}]")


def validate_formula_syntax(data: dict, result: ValidationResult) -> None:
    """Validate that power.roll.formula equals '@chr'."""
    items = data.get("items", [])
    for item in items:
        if item.get("type") == "ability":
            system = item.get("system", {})
            power = system.get("power", {})
            roll = power.get("roll", {})
            formula = roll.get("formula")

            if formula and formula != "@chr":
                if formula.startswith("@") and formula != "@chr":
                    result.add_error(
                        f"Ability '{item.get('name', 'Unknown')}' has invalid formula '{formula}'. "
                        f"Must be '@chr' not characteristic name like '@might', '@agility', etc."
                    )


def validate_keywords_lowercase(data: dict, result: ValidationResult) -> None:
    """Validate that all keywords are lowercase strings."""
    items = data.get("items", [])
    for item in items:
        if item.get("type") == "ability":
            system = item.get("system", {})
            keywords = system.get("keywords", [])

            for keyword in keywords:
                if not keyword.islower():
                    result.add_error(
                        f"Ability '{item.get('name', 'Unknown')}' has capitalized keyword '{keyword}'. "
                        f"All keywords must be lowercase."
                    )

    system = data.get("system", {})
    monster = system.get("monster", {})
    keywords = monster.get("keywords", [])

    for keyword in keywords:
        if not keyword.islower():
            result.add_error(
                f"Monster has capitalized keyword '{keyword}'. "
                f"All keywords must be lowercase."
            )


def validate_power_effects(data: dict, result: ValidationResult) -> None:
    """
    Validate power effects structure.

    For generated abilities (heroic, signature, villain), power.effects should be empty.
    For freeStrike or no category, effects may contain data.
    """
    items = data.get("items", [])
    for item in items:
        if item.get("type") == "ability":
            system = item.get("system", {})
            category = system.get("category")
            power = system.get("power", {})
            effects = power.get("effects", {})

            is_generated_ability = category in ("heroic", "signature", "villain")

            if is_generated_ability and effects and len(effects) > 0:
                result.add_warning(
                    f"Ability '{item.get('name', 'Unknown')}' has non-empty power.effects. "
                    f"Generated abilities (heroic, signature, villain) should have empty {{}}. "
                    f"Found effects with keys: {list(effects.keys())}"
                )


def validate_html_entities(data: dict, result: ValidationResult) -> None:
    """Detect HTML entities in effect text."""
    html_entities = ["&lt;", "&gt;", "&amp;"]

    items = data.get("items", [])
    for item in items:
        system = item.get("system", {})
        effect = system.get("effect", {})

        if not isinstance(effect, dict):
            continue

        before = effect.get("before", "")
        after = effect.get("after", "")

        for entity in html_entities:
            if entity in before or entity in after:
                clean_entity = entity.replace("&", "").replace(";", "")
                result.add_warning(
                    f"Ability '{item.get('name', 'Unknown')}' contains HTML entity '{entity}'. "
                    f"Use raw '<', '>', '&' instead."
                )


def validate_required_fields(data: dict, result: ValidationResult) -> None:
    """Validate required actor fields are present and valid."""
    system = data.get("system", {})

    # Stamina
    stamina = system.get("stamina", {})
    if not isinstance(stamina.get("value"), int) or stamina.get("value", 0) < 0:
        result.add_error(
            "Missing or invalid system.stamina.value (must be positive integer)"
        )
    if not isinstance(stamina.get("max"), int) or stamina.get("max", 0) < 0:
        result.add_error(
            "Missing or invalid system.stamina.max (must be positive integer)"
        )

    # Characteristics
    characteristics = system.get("characteristics", {})
    required_chars = ["might", "agility", "reason", "intuition", "presence"]
    for char in required_chars:
        if char not in characteristics:
            result.add_error(f"Missing system.characteristics.{char}")
        else:
            char_value = characteristics[char]
            if isinstance(char_value, dict):
                if not isinstance(char_value.get("value"), int):
                    result.add_error(f"Invalid system.characteristics.{char}.value")
            elif isinstance(char_value, int):
                pass  # Valid integer value
            else:
                result.add_error(f"Invalid system.characteristics.{char}")

    # Combat
    combat = system.get("combat", {})
    save = combat.get("save", {})
    if not isinstance(save.get("threshold"), int) or save.get("threshold", 0) < 0:
        result.add_error(
            "Missing or invalid system.combat.save.threshold (must be positive integer)"
        )
    if (
        not isinstance(combat.get("size", {}).get("value"), int)
        or combat.get("size", {}).get("value", 0) < 0
    ):
        result.add_error(
            "Missing or invalid system.combat.size.value (must be positive integer)"
        )

    # Monster stats
    monster = system.get("monster", {})
    if not isinstance(monster.get("level"), int) or monster.get("level", 0) < 0:
        result.add_error(
            "Missing or invalid system.monster.level (must be positive integer)"
        )
    if not isinstance(monster.get("ev"), int) or monster.get("ev", 0) < 0:
        result.add_error(
            "Missing or invalid system.monster.ev (must be positive integer)"
        )


def validate_token_config(data: dict, result: ValidationResult) -> None:
    """Validate prototypeToken configuration."""
    token = data.get("prototypeToken", {})

    bar_attr = token.get("bar1", {}).get("attribute")
    if bar_attr != "stamina":
        result.add_warning(
            f"prototypeToken.bar1.attribute should be 'stamina', got '{bar_attr}'"
        )

    width = token.get("width")
    height = token.get("height")
    if width is not None and (not isinstance(width, int) or width < 1):
        result.add_warning(
            f"Invalid prototypeToken.width (must be positive integer), got: {width}"
        )
    if height is not None and (not isinstance(height, int) or height < 1):
        result.add_warning(
            f"Invalid prototypeToken.height (must be positive integer), got: {height}"
        )

    disposition = token.get("disposition")
    if disposition is not None and disposition not in (-1, 0, 1):
        result.add_warning(
            f"Invalid prototypeToken.disposition (must be -1, 0, or 1), got: {disposition}"
        )


def validate_json_file(filepath: str) -> ValidationResult:
    """
    Validate a single JSON file and return a ValidationResult.
    """
    result = ValidationResult()

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        result.add_error(f"Invalid JSON: {e}")
        return result
    except FileNotFoundError:
        result.add_error(f"File not found: {filepath}")
        return result

    # Run all validations
    validate_actor_type(data, result)
    validate_item_types(data, result)
    validate_ability_type(data, result)
    validate_ability_category(data, result)
    validate_monster_role(data, result)
    validate_monster_organization(data, result)
    validate_monster_keywords(data, result)
    validate_ability_keywords(data, result)
    validate_id_format(data, result)
    validate_formula_syntax(data, result)
    validate_keywords_lowercase(data, result)
    validate_power_effects(data, result)
    validate_html_entities(data, result)
    validate_required_fields(data, result)
    validate_token_config(data, result)

    return result


def validate_directory(directory: str) -> tuple:
    """
    Validate all JSON files in a directory.
    Returns (passed_count, failed_count, total_count).
    """
    passed = 0
    failed = 0
    total = 0

    path = Path(directory)
    if not path.exists():
        print(f"Error: Directory not found: {directory}")
        return 0, 0, 0

    json_files = list(path.glob("**/*.json"))

    for json_file in json_files:
        total += 1
        result = validate_json_file(str(json_file))
        result.print_report(json_file.name)

        if result.is_valid():
            passed += 1
        else:
            failed += 1

    print(f"\n{'=' * 60}")
    print(f"Summary: {passed}/{total} files passed validation")
    print(f"{'=' * 60}")

    return passed, failed, total


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate Draw Steel monster JSON files for Foundry VTT import"
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to JSON file or directory to validate (default: current directory)",
    )
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    parser.add_argument(
        "--strict", action="store_true", help="Treat warnings as errors"
    )

    args = parser.parse_args()

    path = Path(args.path)

    if path.is_file() and path.suffix == ".json":
        result = validate_json_file(str(path))
        result.print_report(path.name)

        if args.strict and result.warnings:
            result.passed = False
            result.errors.extend(result.warnings)
            result.warnings.clear()

        if args.json:
            output = {
                "file": path.name,
                "passed": result.passed,
                "errors": result.errors,
                "warnings": result.warnings,
            }
            print(json.dumps(output, indent=2))

        sys.exit(0 if result.passed else 1)

    elif path.is_dir():
        passed, failed, total = validate_directory(str(path))

        if args.json:
            output = {
                "directory": str(path),
                "passed": passed,
                "failed": failed,
                "total": total,
            }
            print(json.dumps(output, indent=2))

        sys.exit(0 if failed == 0 else 1)

    else:
        print(f"Error: Path not found or not a JSON file: {args.path}")
        sys.exit(1)


if __name__ == "__main__":
    main()
