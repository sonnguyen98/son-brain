#!/bin/bash
# Prepare docs/ folder for MkDocs build by copying markdown files from root.
# Root structure stays Obsidian-friendly; docs/ is generated, not committed.
#
# Usage: ./scripts/build-docs.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$ROOT_DIR"

echo "→ Cleaning docs/"
rm -rf docs
mkdir -p docs

echo "→ Copying README.md as homepage (index.md)"
cp README.md docs/index.md

echo "→ Copying root markdown files (QUICK-START.md, etc.)"
for f in QUICK-START.md; do
  if [ -f "$f" ]; then
    cp "$f" "docs/"
    echo "  ✓ $f"
  fi
done

echo "→ Copying 7 content folders"
for dir in 00-triet-ly 01-cai-dat 02-vault-dau-tien-brain 03-mo-rong-multi-vault 04-agents-skills-memory 05-bao-tri-lint 99-templates; do
  if [ -d "$dir" ]; then
    cp -r "$dir" "docs/"
    echo "  ✓ $dir"
  fi
done

echo "→ Copying assets/ for extra CSS"
if [ -d "assets" ]; then
  cp -r assets docs/
fi

echo "→ Copying .claude/skills/ for online preview"
if [ -d ".claude/skills" ]; then
  mkdir -p docs/skills
  # Copy README index
  cp .claude/skills/README.md docs/skills/index.md
  # Copy each skill's SKILL.md as docs/skills/<name>.md
  for skill_dir in .claude/skills/*/; do
    skill_name=$(basename "$skill_dir")
    if [ -f "$skill_dir/SKILL.md" ]; then
      cp "$skill_dir/SKILL.md" "docs/skills/$skill_name.md"
      echo "  ✓ $skill_name"
    fi
  done
fi

echo "✓ docs/ ready. Run: mkdocs build  or  mkdocs serve"
