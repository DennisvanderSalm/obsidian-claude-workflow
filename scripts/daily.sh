#!/bin/bash
# Create daily note from template
# Usage: ./scripts/daily.sh

VAULT_PATH="$(dirname "$0")/../vault"
DATE=$(date +%Y-%m-%d)

cat > "$VAULT_PATH/00-inbox/$DATE.md" << EOF
# $DATE

**Tags:** #daily

## Focus for Today
-

## Tasks
- [ ]

## Notes


## Wins


## Learned


## Tomorrow
-
EOF

echo "Created daily note: $VAULT_PATH/00-inbox/$DATE.md"
