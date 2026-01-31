#!/usr/bin/env python3
"""Convert VTT subtitle files to Obsidian markdown notes."""

import os
import re
import json
import subprocess
from pathlib import Path

VAULT_PATH = Path(__file__).parent.parent / "vault" / "04-resources" / "youtube-transcripts"
TEMP_PATH = Path(__file__).parent.parent / "temp-subs"

def get_video_metadata():
    """Fetch video metadata from playlist."""
    result = subprocess.run(
        ["python", "-m", "yt_dlp", "--flat-playlist", "--dump-json",
         "https://www.youtube.com/playlist?list=PLwSZjmNyZZnwsWlN1ZEOh4Pvrm9rDll2K"],
        capture_output=True, text=True
    )

    metadata = {}
    for line in result.stdout.strip().split('\n'):
        if line:
            data = json.loads(line)
            metadata[data['id']] = {
                'title': data.get('title', 'Untitled'),
                'url': f"https://www.youtube.com/watch?v={data['id']}"
            }
    return metadata

def clean_vtt(vtt_content):
    """Convert VTT to clean text."""
    lines = vtt_content.split('\n')

    # Skip header
    text_lines = []
    skip_next = False
    prev_text = ""

    for line in lines:
        line = line.strip()

        # Skip WEBVTT header and empty lines
        if line.startswith('WEBVTT') or line.startswith('Kind:') or line.startswith('Language:'):
            continue

        # Skip timestamp lines
        if '-->' in line:
            continue

        # Skip cue identifiers (numbers or position info)
        if re.match(r'^\d+$', line) or line.startswith('align:') or line.startswith('position:'):
            continue

        if not line:
            continue

        # Remove VTT tags like <c> </c>
        line = re.sub(r'<[^>]+>', '', line)

        # Avoid duplicates (VTT often repeats lines)
        if line != prev_text:
            text_lines.append(line)
            prev_text = line

    return ' '.join(text_lines)

def sanitize_filename(title):
    """Create a safe filename from title."""
    # Remove special characters
    safe = re.sub(r'[<>:"/\\|?*]', '', title)
    # Replace problematic characters
    safe = safe.replace('€', 'euro').replace('…', '...')
    # Remove emojis and other non-ASCII characters that cause issues
    safe = safe.encode('ascii', 'ignore').decode('ascii')
    # Clean up multiple spaces
    safe = re.sub(r'\s+', ' ', safe)
    # Limit length
    if len(safe) > 100:
        safe = safe[:100]
    return safe.strip()

def create_note(video_id, title, url, transcript):
    """Create an Obsidian markdown note."""
    safe_title = sanitize_filename(title)

    content = f"""# {title}

**Source:** [YouTube]({url})
**Video ID:** {video_id}
**Tags:** #youtube #transcript #ai-report

---

## Transcript

{transcript}

---

## Notes


## Key Takeaways
-

## Related
-
"""

    note_path = VAULT_PATH / f"{safe_title}.md"

    # Handle duplicates
    counter = 1
    while note_path.exists():
        note_path = VAULT_PATH / f"{safe_title} ({counter}).md"
        counter += 1

    with open(note_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return note_path

def main():
    print("Fetching video metadata...")
    metadata = get_video_metadata()
    print(f"Found {len(metadata)} videos in playlist")

    # Ensure output directory exists
    VAULT_PATH.mkdir(parents=True, exist_ok=True)

    # Process each VTT file
    vtt_files = list(TEMP_PATH.glob("*.nl.vtt"))
    print(f"Processing {len(vtt_files)} transcript files...")

    created = 0
    for vtt_file in vtt_files:
        video_id = vtt_file.stem.replace('.nl', '')

        if video_id not in metadata:
            print(f"Warning: No metadata for {video_id}")
            continue

        with open(vtt_file, 'r', encoding='utf-8') as f:
            vtt_content = f.read()

        transcript = clean_vtt(vtt_content)

        if not transcript.strip():
            print(f"Warning: Empty transcript for {video_id}")
            continue

        info = metadata[video_id]
        note_path = create_note(video_id, info['title'], info['url'], transcript)
        created += 1
        try:
            print(f"Created: {note_path.name}")
        except UnicodeEncodeError:
            print(f"Created: {video_id}.md")

    print(f"\nDone! Created {created} notes in {VAULT_PATH}")

if __name__ == "__main__":
    main()
