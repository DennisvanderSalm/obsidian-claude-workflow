# Obsidian + Claude Code Workflow

A personal knowledge management system that combines Obsidian's powerful note-taking with Claude Code's AI capabilities.

## Overview

This workflow leverages two tools:
- **Obsidian** - A markdown-based knowledge base with bidirectional linking and graph visualization
- **Claude Code** - An AI assistant that can read, write, and reason about your files directly

Together, they create an intelligent second brain that can not only store information but actively help you connect, synthesize, and expand your knowledge.

## Core Workflow Concepts

### 1. Capture
Quickly capture ideas, notes, and information into your vault. Claude Code can help format, tag, and file new content appropriately.

### 2. Connect
Use Obsidian's linking to connect related concepts. Claude Code can suggest connections you might have missed by analyzing your existing notes.

### 3. Synthesize
Ask Claude Code to summarize topics across multiple notes, identify patterns, or generate new insights from your collected knowledge.

### 4. Create
Generate new content (articles, summaries, outlines) using your vault as context. Claude Code can reference your notes to produce personalized output.

## Getting Started

### Prerequisites
- [Obsidian](https://obsidian.md/) installed
- [Claude Code](https://claude.ai/claude-code) CLI installed and authenticated
- This repository cloned locally

### Setup
1. Clone this repository
2. Open the `vault/` folder as an Obsidian vault
3. Run Claude Code from this directory to interact with your notes

## Project Structure

```
obsidian-claude-workflow/
├── vault/                  # Obsidian vault
│   ├── 00-inbox/          # Quick capture, unsorted notes
│   ├── 01-notes/          # Processed, permanent notes
│   ├── 02-projects/       # Active project notes
│   ├── 03-areas/          # Ongoing areas of responsibility
│   ├── 04-resources/      # Reference materials
│   ├── 05-archive/        # Completed/inactive items
│   └── templates/         # Note templates
├── scripts/               # Automation scripts
└── README.md
```

## Example Commands

Once set up, you can use Claude Code for tasks like:

- "Summarize all my notes about [topic]"
- "What connections exist between [concept A] and [concept B]?"
- "Create a new note about [topic] based on what I've learned"
- "Review my inbox and suggest how to organize these notes"
- "Find gaps in my knowledge about [subject]"

## License

MIT
