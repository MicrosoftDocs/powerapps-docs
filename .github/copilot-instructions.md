# Copilot instructions for Microsoft Learn

These instructions define a unified style and process standard for authoring and maintaining learn.microsoft.com documentation with GitHub Copilot or other AI assistance.

## Learn-wide instructions

The following instructions apply to all Microsoft Learn documentation authored with AI assistance. The Learn product team updates this guidance periodically as needed. Each repository shouldn't update this guidance to avoid being overwritten, but update the repository-specific instructions as needed.

### AI usage and disclosure
All Markdown content created or substantially modified with AI assistance must include an `ai-usage` front matter entry:
- `ai-usage: ai-generated` – AI produced the initial draft with minimal human authorship.
- `ai-usage: ai-assisted` – Human-directed, reviewed, and edited with AI support.
- Omit only for purely human-authored legacy content.

If missing, **add it**. However, don't add or update the `ai-usage` tag if the changes proposed are confined solely to:
- Links (link text and URLs).
- Single words or short phrases, such as entries in table cells.
- Less than 5% of the article's word count.

### Writing style

Follow the [Microsoft Writing Style Guide](https://learn.microsoft.com/style-guide/welcome/) with these specifics:

#### Voice and tone

- Active voice, second person addressing reader directly
- Conversational tone with contractions
- Present tense for instructions and descriptions
- Imperative mood for instructions ("Call the method" not "You should call the method")
- Use "might" instead of "may" for possibility
- Avoid "we" and "our" when referring to documentation authors

#### Structure and format

- Sentence case headings (no gerunds in titles)
- Be concise, and break up long sentences
- Use the Oxford comma in lists
- Number all ordered lists sequentially like "1.", "2.", "3.".
- Complete sentences with proper punctuation in all list items
- Avoid "etc." or "and so on" - provide complete lists or use "for example"
- No consecutive headings without content between them

#### Formatting conventions

- **Bold** for UI elements
- `Code style` for file names, folders, custom types, and non-localizable text
- Raw URLs in angle brackets
- Use relative links for files in this repo
- Remove `https://learn.microsoft.com/en-us` from learn.microsoft.com links

## Repository-specific instructions

The following instructions are specific to this repository. Repository maintainers might update these instructions as needed.

<!--- Add additional repository level instructions below. Do NOT update this line or above. --->
