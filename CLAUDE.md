# Claude Code Instructions

This is an Obsidian-based personal knowledge management vault. When working with this project, follow these guidelines.

## Vault Structure

- `vault/00-inbox/` - Quick captures, needs processing
- `vault/01-notes/` - Permanent, evergreen notes
- `vault/02-projects/` - Active projects
- `vault/03-areas/` - Ongoing life areas
- `vault/04-resources/` - Reference materials
- `vault/05-archive/` - Inactive items
- `vault/templates/` - Note templates

## Working with Notes

### Creating Notes
- Use templates from `vault/templates/` as starting points
- Always include relevant tags
- Add `[[links]]` to connect related concepts
- Place new captures in `00-inbox/` unless they clearly belong elsewhere

### Note Formatting
- Use `# Title` for note titles
- Include metadata at the top (date, tags)
- Use `## Headings` to structure content
- Add a `## Related` section for links to other notes
- Keep notes atomic - one idea per note when possible

### Linking Conventions
- Use `[[Note Name]]` for internal links
- Use `[[Note Name|display text]]` for custom link text
- Tags use format: `#category/subcategory`

## Common Tasks

### Process Inbox
When asked to process the inbox:
1. Read each note in `00-inbox/`
2. Suggest appropriate folder and tags
3. Identify potential links to existing notes
4. Move to appropriate folder after user confirms

### Find Connections
When asked to find connections:
1. Search for related concepts across the vault
2. Suggest new `[[links]]` to add
3. Identify potential new notes that bridge concepts

### Summarize Topic
When asked to summarize a topic:
1. Search for all notes related to the topic
2. Synthesize key points across notes
3. Identify gaps or contradictions
4. Suggest areas for further exploration

### Create from Knowledge
When asked to create content:
1. Search vault for relevant source notes
2. Reference specific notes used
3. Maintain user's voice and style
4. Add links back to source notes
