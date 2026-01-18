#!/bin/bash
#
# setup-skill-symlinks.sh
#
# Creates symlinks for the Draw Steel Monster Generator skill
# across different AI coding platforms.
#
# Usage: ./setup-skill-symlinks.sh
#

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
CANONICAL_DIR=".claude/skills/draw-steel-monster-generator"
SKILL_NAME="draw-steel-monster-generator"

# Platforms to set up
PLATFORMS=(
    ".cursor/skills/${SKILL_NAME}"
    ".gemini/skills/${SKILL_NAME}"
)

detect_platform() {
    case "$(uname -s)" in
        Linux*)
            echo "linux"
            ;;
        Darwin*)
            echo "macos"
            ;;
        CYGWIN*|MINGW*|MSYS*)
            echo "windows"
            ;;
        *)
            echo "unknown"
            ;;
    esac
}

create_symlink_unix() {
    local target="$1"
    local link="$2"
    local platform="$3"

    # Check if target exists
    if [ ! -d "$target" ]; then
        echo -e "${RED}ERROR${NC}: Target directory not found: $target"
        echo "Make sure you're running from the project root."
        return 1
    fi

    # Remove existing symlink or directory if it exists
    if [ -L "$link" ]; then
        echo "Removing existing symlink: $link"
        rm "$link"
    elif [ -d "$link" ]; then
        echo -e "${YELLOW}WARNING${NC}: Directory already exists: $link"
        echo "Remove it manually if you want to create a symlink."
        return 0
    fi

    # Create symlink
    if ln -s "$target" "$link" 2>/dev/null; then
        echo -e "${GREEN}SUCCESS${NC}: Created symlink for $platform"
        echo "  $link -> $target"
        return 0
    else
        echo -e "${RED}ERROR${NC}: Failed to create symlink for $platform"
        return 1
    fi
}

create_symlink_windows() {
    local target="$1"
    local link="$2"
    local platform="$3"

    # Convert to Windows-style paths
    local target_win=$(cygpath -w "$target" 2>/dev/null || echo "$target")
    local link_win=$(cygpath -w "$link" 2>/dev/null || echo "$link")

    # Check if target exists
    if [ ! -d "$target" ]; then
        echo -e "${RED}ERROR${NC}: Target directory not found: $target"
        echo "Make sure you're running from the project root."
        return 1
    fi

    # Check if running with appropriate permissions
    # Try using mklink first (requires admin)
    if cmd //c "mklink /D $link_win $target_win" 2>/dev/null; then
        echo -e "${GREEN}SUCCESS${NC}: Created junction for $platform (mklink)"
        return 0
    fi

    # Try using PowerShell junction
    if command -v powershell &> /dev/null; then
        if powershell -Command "New-Item -ItemType Junction -Name '$link_win' -Target '$target_win'" 2>/dev/null; then
            echo -e "${GREEN}SUCCESS${NC}: Created junction for $platform (PowerShell)"
            return 0
        fi
    fi

    echo -e "${RED}ERROR${NC}: Failed to create symlink for $platform"
    echo ""
    echo "Windows requires Administrator privileges or Developer Mode enabled."
    echo ""
    echo "Manual setup options:"
    echo ""
    echo "Option 1: Run as Administrator"
    echo "  Open PowerShell as Administrator and run:"
    echo "  mklink /D $link_win $target_win"
    echo ""
    echo "Option 2: Enable Developer Mode"
    echo "  Go to Settings > System > Developer Options > Developer Mode"
    echo "  Then run this script again."
    echo ""
    echo "Option 3: Manual symlink creation"
    echo "  mklink /D $link_win $target_win"

    return 1
}

setup_platform() {
    local platform_dir="$1"
    local platform_name=$(dirname "$platform_dir")

    echo "Setting up $platform_name..."

    # Create parent directory if it doesn't exist
    local parent_dir=$(dirname "$platform_dir")
    if [ ! -d "$parent_dir" ]; then
        mkdir -p "$parent_dir"
    fi

    # Create symlink based on platform
    local platform=$(detect_platform)

    case "$platform" in
        windows)
            create_symlink_windows "$CANONICAL_DIR" "$platform_dir" "$platform_name"
            ;;
        linux|macos|unknown)
            create_symlink_unix "$CANONICAL_DIR" "$platform_dir" "$platform_name"
            ;;
        *)
            echo -e "${RED}ERROR${NC}: Unknown platform: $platform"
            return 1
            ;;
    esac
}

print_header() {
    echo ""
    echo "=============================================="
    echo "  Draw Steel Monster Generator - Skill Setup"
    echo "=============================================="
    echo ""
}

print_summary() {
    echo ""
    echo "=============================================="
    echo "  Setup Complete"
    echo "=============================================="
    echo ""
    echo "The skill is now available in the following locations:"
    echo "  - ${GREEN}.claude/skills/${SKILL_NAME}${NC} (canonical)"
    for platform in "${PLATFORMS[@]}"; do
        if [ -d "$platform" ] || [ -L "$platform" ]; then
            echo "  - ${GREEN}$platform${NC} (symlink)"
        fi
    done
    echo ""
    echo "Note: Many platforms automatically scan .claude/skills/"
    echo "so symlinks may not be necessary."
    echo ""
}

main() {
    local errors=0

    print_header

    # Check if canonical directory exists
    if [ ! -d "$CANONICAL_DIR" ]; then
        echo -e "${RED}ERROR${NC}: Canonical directory not found: $CANONICAL_DIR"
        echo "Make sure you're running from the project root."
        exit 1
    fi

    echo "Canonical directory: $CANONICAL_DIR"
    echo "Platforms to set up: ${#PLATFORMS[@]}"
    echo ""

    # Setup each platform
    for platform in "${PLATFORMS[@]}"; do
        if ! setup_platform "$platform"; then
            ((errors++))
        fi
    done

    if [ $errors -gt 0 ]; then
        echo ""
        echo -e "${YELLOW}WARNING${NC}: $errors platform(s) failed to set up."
        echo "You may need to set them up manually."
    fi

    print_summary
}

main "$@"
