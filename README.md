# LSP-mdita

![LICENSE](https://img.shields.io/badge/LICENSE-MIT-green?style=for-the-badge) ![Sublime Text](https://img.shields.io/badge/ST-Build%204126+-orange?style=for-the-badge&logo=sublime-text)

`LSP-mdita` is an LSP helper package for the [mdita-lsp](https://github.com/aireilly/mdita-lsp) language server. It acts as a glue between the [LSP](https://packagecontrol.io/packages/LSP) package and the mdita-lsp language server, configuring and managing the server for you.

Unlike npm-based LSP helpers, this package expects the `mdita-lsp` binary to be pre-installed on your system.

## Features

Everything that the [mdita-lsp](https://github.com/aireilly/mdita-lsp) language server supports, which includes:

- Document and workspace symbols from headings.
- Completion for wiki links, inline links, keyrefs, and YAML front matter fields.
- Hover preview for links, headings, and keyref targets.
- `Go to Definition` and `Find References` for headings, links, and keyrefs.
- Diagnostics for broken links, missing YAML front matter, short descriptions, heading hierarchy, DITA schema validation, and keyref resolution.
- Code Lens with reference counts on headings.
- Rename refactoring across files.
- Code actions: generate Table of Contents, create missing file, add to map, convert wiki links to markdown links, add front matter.
- DITA OT build integration (xhtml, dita output formats).
- Document formatting (table alignment, trailing whitespace cleanup, heading spacing, trailing newline).
- Inlay hints showing resolved wiki link titles and keyref targets.
- Semantic token highlighting for wiki links.
- Linked editing of headings and their intra-doc wiki link references.
- Folding ranges for headings, YAML front matter, and ToC markers.
- Selection range expansion (line, element, section).
- File rename refactoring (updates wiki links, markdown links, and map references).
- MDITA map file (`.mditamap`) support.
- DITA fragment identifier support (`topicID/sectionID`).
- Diagnostic quick-fixes (NBSP removal, footnote conversion, heading hierarchy).

## Installation

### Prerequisites

1. Install the [LSP](https://packagecontrol.io/packages/LSP) package from Package Control.

2. Download the prebuilt binary for your platform from the [latest release](https://github.com/aireilly/mdita-lsp/releases/latest):

   | Platform | Binary |
   |----------|--------|
   | Linux x64 | `mdita-lsp-linux-amd64` |
   | Linux arm64 | `mdita-lsp-linux-arm64` |
   | macOS Apple Silicon | `mdita-lsp-darwin-arm64` |
   | macOS Intel | `mdita-lsp-darwin-amd64` |
   | Windows x64 | `mdita-lsp-windows-amd64.exe` |

3. Make the binary executable (Linux/macOS):
   ```bash
   chmod +x mdita-lsp-linux-amd64
   ```

4. Copy it to a directory on your `PATH` (Linux):
   ```bash
   cp mdita-lsp-linux-amd64 $HOME/.local/bin/mdita-lsp
   ```

   No runtime dependencies are required -- the binary is self-contained (~3.5 MB).

   Alternatively, build from source:
   ```bash
   git clone https://github.com/aireilly/mdita-lsp
   cd mdita-lsp
   make install
   ```

### Package Control

1. Open `Package Control: Install Package` from the command palette.
2. Search for `LSP-mdita` and press <kbd>Enter</kbd>.

### Manual installation

1. Open `Package Control: Add Repository` from the command palette.
2. Enter `https://github.com/aireilly/LSP-mdita` into the input panel.
3. Open `Package Control: Install Package` and search for `LSP-mdita`.

## Configuration

Open the settings via the command palette:

```
Preferences: LSP-mdita Settings
```

Or navigate to: **Preferences > Package Settings > LSP > Servers > LSP-mdita**.

### Custom binary path

If `mdita-lsp` is not on your `PATH`, specify the full path in your user settings:

```json
{
    "command": ["/path/to/mdita-lsp"],
}
```

### MDITA mode

To enable MDITA-specific diagnostics (missing YAML front matter, short description validation, heading hierarchy, DITA schema checks), create a `.mdita-lsp.yaml` file in your project root with:

```yaml
mdita:
  enable: true
```

## Keyboard Shortcuts

All keybindings are scoped to Markdown files (`text.html.markdown`) and require the corresponding LSP server capability.

| Shortcut | Command | Description |
|---|---|---|
| <kbd>F12</kbd> | Go to Definition | Jump to the definition of a heading, link, or keyref target |
| <kbd>Shift+F12</kbd> | Find References | Find all references to a heading or link |
| <kbd>F2</kbd> | Rename Symbol | Rename a heading and update all cross-file references |
| <kbd>Ctrl+Shift+O</kbd> | Document Symbols | Navigate headings in the current file |
| <kbd>Ctrl+Shift+R</kbd> | Workspace Symbols | Search symbols across all project files |
| <kbd>Ctrl+Shift+A</kbd> | Code Actions | Trigger code actions (ToC, add to map, create file, convert links) |
| <kbd>Ctrl+Shift+H</kbd> | Hover | Show hover information for links, headings, and keyrefs |
| <kbd>Ctrl+Space</kbd> | Auto Complete | Trigger completions for links, keyrefs, front matter fields |
| <kbd>Ctrl+Shift+F</kbd> | Format Document | Format the document (table alignment, whitespace, spacing) |
| <kbd>Ctrl+Click</kbd> | Go to Definition | Click a file reference or link to jump to it |
| <kbd>Ctrl+Shift+Click</kbd> | Go to Definition (side-by-side) | Open the target in a split view |

## Snippets

Tab-trigger snippets are available in Markdown files for common MDITA constructs:

| Tab Trigger | Description | Output |
|---|---|---|
| `mdita-topic` | Full MDITA topic template | YAML front matter with `$schema` + heading + body |
| `frontmatter` | YAML front matter block | `---` block with `$schema`, `id`, `author` |
| `xref` | Cross-reference link | `[link text](filename.md)` |
| `fragref` | DITA fragment ID link | `[link text](filename.md#topicID/sectionID)` |
| `mapentry` | MDITA map entry | `- [Topic Title](path/to/topic.md)` |
| `wiki` | Wiki-style link | `[[target-topic]]` |
| `keyref` | DITA keyref | `[key-name]` |
| `admonition` | Admonition block | `!!! note` with content |

## Completions

YAML front matter field completions are provided when editing Markdown files. Type the field name and press <kbd>Tab</kbd> to expand:

`$schema`, `id`, `shortdesc`, `author`, `source`, `publisher`, `permissions`, `audience`, `category`, `keyword`, `resourceid`

## Reporting issues

If you encounter problems, first check whether the same issue occurs with `mdita-lsp` directly. If it does, file an issue with the [language server](https://github.com/aireilly/mdita-lsp/issues). For issues specific to the Sublime Text integration, file them at:

https://github.com/aireilly/LSP-mdita/issues

## Acknowledgements

This package relies on [LSP](https://packagecontrol.io/packages/LSP) for LSP capabilities in Sublime Text and [mdita-lsp](https://github.com/aireilly/mdita-lsp) for the language server implementation.

## License

The MIT License (MIT). See [LICENSE.md](LICENSE.md) for details.
