#!/bin/bash
# Quick capture script - adds a note to the inbox
# Usage: ./scripts/capture.sh "Note title" "Content"

VAULT_PATH="$(dirname "$0")/../vault"
INBOX_PATH="$VAULT_PATH/00-inbox"
DATE=$(date +%Y-%m-%d)
TIME=$(date +%H:%M)

TITLE="${1:-Untitled}"
CONTENT="${2:-}"

# Sanitize filename
FILENAME=$(echo "$TITLE" | sed 's/[^a-zA-Z0-9 ]//g' | sed 's/ /-/g')

cat > "$INBOX_PATH/$FILENAME.md" << EOF
# $TITLE

**Captured:** $DATE $TIME
**Tags:** #inbox

$CONTENT

## Notes


## Related
-
EOF

echo "Created: $INBOX_PATH/$FILENAME.md"
