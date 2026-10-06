# LSP-mdita

![LICENSE](https://img.shields.io/badge/LICENSE-MIT-green?style=for-the-badge) ![Sublime Text](https://img.shields.io/badge/ST-Build%204126+-orange?style=for-the-badge&logo=sublime-text)

`LSP-mdita` is an LSP helper package for the [mdita-lsp](https://github.com/aireilly/mdita-lsp) language server. It acts as a glue between the [LSP](https://packagecontrol.io/packages/LSP) package and the mdita-lsp language server, configuring and managing the server for you.

Unlike npm-based LSP helpers, this package expects the `mdita-lsp` binary to be pre-installed on your system.

## Features

Everything that the [mdita-lsp](https://github.com/aireilly/mdita-lsp) language server supports, which includes:

- Document and workspace symbols from headings.
- Completion for inline links, heading anchors, keyrefs, conrefs, task section headings, and YAML front matter keys.
- Hover for links, headings, YAML keys, keyrefs, conrefs, task sections, and the task structure the plug-in derives implicitly.
- `Go to Definition` and `Find References` for headings, links, keyrefs, and conrefs.
- Diagnostics for broken and ambiguous links, missing front matter, missing short descriptions, heading hierarchy, `$schema` values, MDITA profile violations, footnotes, keyref resolution, conref resolution, and map validation.
- Code Lens with reference counts on headings.
- Rename refactoring across files.
- Code actions: create missing file, add front matter, add to map, add task sections, fix NBSP, footnotes, and heading levels, build with DITA-OT.
- DITA-OT build integration (xhtml, dita output formats).
- Document formatting (table alignment, trailing whitespace cleanup, heading spacing, trailing newline), including table alignment on save.
- Inlay hints showing resolved link, keyref, and conref targets.
- Semantic token highlighting for `{.class}` block attributes.
- Linked editing of heading text.
- Document highlight for a heading and its intra-document references.
- Folding ranges for headings and YAML front matter.
- Selection range expansion (line, element, section).
- File rename refactoring (updates markdown links and map references).
- Map support for `.mditamap` files and `.md` files declaring the DITA map schema.
- DITA fragment addressing (`file.md#topic-id/element-id`).
- MDITA core and extended profile awareness.

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

   No runtime dependencies are required -- the binary is self-contained (~4.3 MB).

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

### Server configuration

The server reads `.mdita-lsp.yaml` from the project root, falling back to `~/.config/mdita-lsp/config.yaml`. Settings live under `core.mdita`:

```yaml
core:
  mdita:
    enable: true
    profile: extended          # "core" or "extended"
    map_extensions: [mditamap]
    formatTablesOnSave: true
```

A document that declares an MDITA `$schema` selects its own profile and overrides `profile`. See the [server README](https://github.com/aireilly/mdita-lsp#configuration) for the full set, including `implicit_task_sections`, per-diagnostic toggles, and DITA-OT build options.

## Keyboard Shortcuts

All keybindings are scoped to Markdown files (`text.html.markdown`) and require the corresponding LSP server capability.

| Shortcut | Command | Description |
|---|---|---|
| <kbd>F12</kbd> | Go to Definition | Jump to the definition of a heading, link, or keyref target |
| <kbd>Shift+F12</kbd> | Find References | Find all references to a heading or link |
| <kbd>F2</kbd> | Rename Symbol | Rename a heading and update all cross-file references |
| <kbd>Ctrl+Shift+O</kbd> | Document Symbols | Navigate headings in the current file |
| <kbd>Ctrl+Shift+R</kbd> | Workspace Symbols | Search symbols across all project files |
| <kbd>Ctrl+Shift+A</kbd> | Code Actions | Trigger code actions (create file, add to map, add task sections, front matter, DITA-OT build) |
| <kbd>Ctrl+Shift+H</kbd> | Hover | Show hover information for links, headings, and keyrefs |
| <kbd>Ctrl+Space</kbd> | Auto Complete | Trigger completions for links, keyrefs, front matter fields |
| <kbd>Ctrl+Shift+F</kbd> | Format Document | Format the document (table alignment, whitespace, spacing) |
| <kbd>Ctrl+Click</kbd> | Go to Definition | Click a file reference or link to jump to it |
| <kbd>Ctrl+Shift+Click</kbd> | Go to Definition (side-by-side) | Open the target in a split view |

## Snippets

Tab-trigger snippets are available in Markdown files for common MDITA constructs:

| Tab Trigger | Description | Output |
|---|---|---|
| `mdita-topic` | Full topic template | YAML front matter with `$schema` + heading + body |
| `frontmatter` | YAML front matter block | `---` block with `$schema`, `id`, `author` |
| `xref` | Cross-reference link | `[link text](filename.md)` |
| `fragref` | DITA fragment ID link | `[link text](filename.md#topicID/sectionID)` |
| `mapentry` | MDITA map entry | `- [Topic Title](path/to/topic.md)` |
| `keyref` | DITA keyref | `[key-name]` |
| `keydef` | Key definition for a map | `[key-name]: topic.md "Title"` |
| `datakeyref` | Inline keyword keyref | `<span data-keyref="key-name">` |
| `conref` | Content reference | `<p data-conref="shared.md#topic-id/element-id">` |
| `conkeyref` | Content key reference | `<span data-conkeyref="key-name/element-id">` |
| `task` | Task topic skeleton | `$schema` task front matter with Prerequisites, Procedure, Verification |
| `admonition` | Admonition block | `!!! note` with content |

`admonition` works in Markdown DITA files, including topics typed by a `dita` `$schema`, from plug-in 6.2.0 onwards. Earlier versions do not enable admonitions for schema-declared topics. The MDITA profiles never support them.

## Completions

YAML front matter field completions are provided when editing Markdown files. Type the field name and press <kbd>Tab</kbd> to expand:

`$schema`, `id`, `author`, `source`, `publisher`, `permissions`, `audience`, `category`, `keyword`, `resourceid`

There is no `shortdesc` key. The plug-in builds `<shortdesc>` from the first paragraph after the title, when the topic declares a `$schema` or the title carries a `{.concept}`, `{.task}`, or `{.reference}` class.

The `$schema` completions offer the Markdown DITA types first (`topic`, `concept`, `task`, `reference`, `map`), then the MDITA profiles. Prefer a `dita` value: the MDITA profiles cannot express a task, drop `{...}` attribute blocks, and reduce the element set.

## Reporting issues

If you encounter problems, first check whether the same issue occurs with `mdita-lsp` directly. If it does, file an issue with the [language server](https://github.com/aireilly/mdita-lsp/issues). For issues specific to the Sublime Text integration, file them at:

https://github.com/aireilly/LSP-mdita/issues

## Acknowledgements

This package relies on [LSP](https://packagecontrol.io/packages/LSP) for LSP capabilities in Sublime Text and [mdita-lsp](https://github.com/aireilly/mdita-lsp) for the language server implementation.

## License

The MIT License (MIT). See [LICENSE.md](LICENSE.md) for details.
