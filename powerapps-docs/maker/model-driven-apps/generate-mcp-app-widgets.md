---
title: Generate MCP App widgets with AI code generation tools
description: Learn how to generate MCP app widgets with AI code generation tools.
#customer intent: As a Power Apps maker, I want to know how to use AI code generation tools like GitHub Copilot CLI or Claude Code to generate interactive MCP app widgets for your model-driven Power Apps MCP tools.
author: Mattp123
ms.author: hemantg
ms.reviewer: matp
ms.date: 04/16/2026
ms.topic: how-to
ms.service: powerapps
ms.subservice: mda-maker
---
# Generate MCP app widgets with AI code generation tools

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This article explains how to use AI code generation tools like GitHub Copilot CLI or Claude Code to generate interactive model context protocol (MCP) apps for your model-driven Power Apps MCP tools. MCP apps are self-contained HTML files that render a tool's JSON output visually as cards, charts, dashboards, or maps inside any MCP Apps compatible host, including Microsoft 365 Copilot, Claude, and Visual Studio Code.

If you have an MCP tool that returns JSON data, the `generate-mcp-app-ui` skill can produce a polished, theme-aware widget that displays that data in a compact visual format directly inside a chat conversation.

> [!IMPORTANT]
>
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]
> - MCP apps support in Microsoft 365 Copilot Chat is generally available as of March 2026. Power Apps support for MCP apps in declarative agents is currently in public preview. For the full announcement, see [MCP Apps now available in Copilot Chat](https://devblogs.microsoft.com/microsoft365dev/mcp-apps-now-available-in-copilot-chat/).

## What you can do with the generate-mcp-app-ui skill

- *Create visual widgets* for any MCP tool by describing what you want and pasting the tool's JSON output.
- Choose the right visual for your data, such as charts for numeric trends, cards for structured records, tables for comparisons, maps for coordinates, and so on.
- Support light and dark themes automatically through Fluent UI design tokens.
- Add interactivity so widgets can call your tool again at runtime (for example, a refresh button).
- Refine the UX iteratively by describing changes in natural language. For example, "make the gallery compact," "add a chart," or "use a card layout."

## Prerequisites

### Software requirements

| Component | Minimum version | More information |
|---|---|---|
| GitHub Copilot CLI, Claude Code, or other code generation tool | Latest | [Claude Code](https://claude.ai/code), [GitHub Copilot CLI](https://github.com/features/copilot/cli/) |
| A modern browser | Any | For previewing generated widgets locally |

### Additional requirements

- An MCP tool that returns JSON output. Your tool's output type must be set to **JSON**.
- A working internet connection. Widgets load Fluent UI and other libraries from the Content Delivery Network (CDN) at runtime.

### Install the plugin

Run the following installer command from GitHub Copilot CLI or Claude Code. The installer automatically detects available tools and installs all Power Platform plugins, including `generate-mcp-app-ui`.

```
/plugin marketplace add microsoft/power-platform-skills
```

To install only the MCP App widget skill:
```
/plugin install mcp-apps@power-platform-skills
```

> [!TIP]
> Turn on auto-update to automatically receive skill updates. Use the `/plugin` command, navigate to **Marketplaces**, choose the marketplace, and turn on auto-update.

## Skills overview

| Skill | Command | Description |
|---|---|---|
| MCP Apps widget generator | `/generate-mcp-app-ui` | Generate a self-contained MCP app widget (HTML file) for an MCP tool's JSON output |

The skill is also triggered by natural language phrases such as "create a widget," "build a widget for my tool," or "make an MCP app."

## Generate a widget

Follow these steps to create a new widget for an MCP tool.

1. **Create and test a custom tool** from model-driven app designers and copy the full JSON output. Make sure the tool's output type is set to JSON. More information: [Create custom tools](enable-your-app-copilot.md#create-custom-tools)

1. **Invoke the skill** and describe what you want displayed, pasting the JSON output into the conversation:

   ```
   /generate-mcp-app-ui Visualizes flights using an animated arc map for routes and a synchronized Gantt timeline for departure and arrival schedules, enabling quick understanding of flight coverage, timing, and overlaps. Here's an example of the tool's output: {"flight_records":[{"Departure Time":"2024-07-02T05:00:00Z","Arrival Time":"2024-07-02T07:30:00Z","Flight Name":"Zava 1001","Status":"Active","Airport":"Seattle-Tacoma","Airport1":"Los Angeles Intl"},{"Departure Time":"2024-07-02T03:00:00Z","Arrival Time":"2024-07-02T10:00:00Z","Flight Name":"Zava 103","Status":"Active","Airport":"Seattle-Tacoma","Airport1":"Hartsfield-Jackson"}]}
   ```

1. **Review the generated HTML file.** The skill writes a self-contained HTML file, for example, `flight-map.html`, to your working directory.
1. **Preview in a browser.** Open the HTML file locally as widget has the fallback option for testing. You can ask chat agent to add standalone HTML preview if missing. 
1. **Iterate.** Describe any changes directly in the chat:
   - "Make the map larger"
   - "Add tool tips on the Chart"
   - "Decrease the height and fit in 250 pixels with responsive layout and no scroll bars"

> [!NOTE]
> The skill requires actual JSON from your tool—not sample or mock data. The data shape drives the widget generation. If you paste mock data, the generated widget might not work correctly when connected to the real tool.

## Deploy your widget

Once your widget is ready, copy the HTML file to the UX input for corresponding tool and it will be returned as the tool's UI response. Refer to your [create custom tools documentation](enable-your-app-copilot.md#create-custom-tools) for details. 

## Add interactivity with callServerTool

If you also provide your tool's name when invoking the skill, the generated widget can include interactive tool-call integration. This allows the widget to call your tool again at runtime. For example a refresh button on the tool UX can call itself.

```
/generate-mcp-app-ui Show the current weather conditions with a refresh button. Tool name: get_weather. Tool output: {"city":"Seattle","temp_f":54,"condition":"Overcast","humidity":78,"forecast":[...]}
```

The skill wires up `app.callServerTool` in the widget so that when users select **Refresh**, the widget fetches updated data directly from your tool.
If you don't provide a tool name, the widget is read-only and renders only the data delivered through the `ontoolresult` callback.

- **Microsoft 365 Copilot chat**: See [MCP apps in Copilot Chat](https://devblogs.microsoft.com/microsoft365dev/mcp-apps-now-available-in-copilot-chat/) for deployment paths including sideloading for testing, deploying through the Microsoft 365 admin center for organizational use, and publishing to the Microsoft 365 agent store.
- **Power Apps declarative agents**: See [Power Apps MCP declarative agent documentation](/power-apps/maker/model-driven-apps/generative-page-external-tools) for how to connect MCP tools with model-driven apps.
- **Other MCP hosts**: Consult your host's documentation for the MCP apps widget registration process.

## Widget technical details

### MCP apps protocol

Widgets communicate with the chat host using the `App` class from the `@modelcontextprotocol/ext-apps` package. The protocol manages these callbacks and methods.

| Callback / method | Description |
|---|---|
| `app.ontoolresult` | Fires when the host delivers tool data. *Your data is always at `result.structuredContent`*—not `result.data` or `result` itself. |
| `app.onhostcontextchanged` | Fires when the host context changes, including theme (`ctx.theme` is `'light'` or `'dark'`). |
| `app.onteardown` | Fires when the widget is removed from the conversation. |
| `app.connect()` | Establishes communication with the host. All event handlers must be registered *before* calling `connect()`. |
| `app.getHostContext()` | Returns the current host context (including initial theme) after `connect()` completes. |
| `app.callServerTool({ name, arguments })` | Calls a tool interactively. Returns `result.isError` and `result.structuredContent`. |


### CDN imports

Widgets load all dependencies from CDN. No build step or local installation is required. Dependencies come in two formats:

- **ECMAScript Modules (ESM)** — imported inside `<script type="module">` using a URL ending in `/+esm`
- **Universal Module Definition (UMD)** — loaded via a plain `<script src>` tag; registers itself globally as a side effect

  | Library | Format | URL | Purpose |
  |---|---|---|---|
  | `@modelcontextprotocol/ext-apps` | ESM | `cdn.jsdelivr.net/npm/@modelcontextprotocol/ext-apps/+esm` | MCP apps `App` class |
  | `@fluentui/tokens` | ESM | `cdn.jsdelivr.net/npm/@fluentui/tokens/+esm` | `webLightTheme` / `webDarkTheme` token sets |
  | `@fluentui/web-components@beta` | UMD | `unpkg.com/@fluentui/web-components@beta/dist/web-components.min.js` | Fluent UI custom elements

### Visual states

Every widget handles three states:

| State | Guidance |
|---|---|
| Loading | Show a `<fluent-spinner>` with a contextual message ("Finding attractions…" not just "Loading…"). |
| Loaded | Render the content compactly. Use the full available width. |
| Error | Show a friendly message and a "Try again" button. If the widget uses `callServerTool`, the button re-invokes the tool. |

### Fluent UI components

The following Fluent UI web components are available in widgets:

`<fluent-card>`, `<fluent-button>`, `<fluent-text-input>`, `<fluent-textarea>`, `<fluent-dropdown>`, `<fluent-listbox>`, `<fluent-option>`, `<fluent-checkbox>`, `<fluent-spinner>`, `<fluent-divider>`, `<fluent-badge>`, `<fluent-switch>`, `<fluent-tooltip>`

### Theme support

Widgets support light and dark themes through Fluent UI design tokens. The widget applies the correct token values when the host's theme changes via `onhostcontextchanged`. Always use token variables, for example, `var(--colorNeutralForeground1)`, rather than hardcoded color values to ensure correct rendering in both themes.

### Color tokens

| Use | Token |
|---|---|
| Primary text | `var(--colorNeutralForeground1)` |
| Secondary text | `var(--colorNeutralForeground2)` |
| Primary background | `var(--colorNeutralBackground1)` |
| Card/hover background | `var(--colorNeutralBackground2)` |
| Brand/accent | `var(--colorBrandBackground)` |
| Text on brand surface | `var(--colorNeutralForegroundOnBrand)` |
| Borders | `var(--colorNeutralStroke1)` |
| Error text | `var(--colorStatusDangerForeground1)` |
| Success text | `var(--colorStatusSuccessForeground1)` |

Never use hardcoded hexidecimal or RGB values. Don't invent token names not listed here.

## Best practices

- Provide real test data. The skill analyzes the actual JSON structure to select the right visual. Mock data produces widgets that break when connected to the real tool.
- Be specific about the visual. Describe the format you want, such as map, chart, table, or card layout. Vague descriptions lead to generic results.
- Start with one view. Widgets are compact conversation cards, not full applications. No tabs, page navigation, or search bars that duplicate the chat input.
- Test with both themes. Preview in light and dark mode to verify contrast and readability.
- Match the visual to the data. Maps for coordinates, charts for numeric or trend data, cards for structured records, tables for comparisons.

## Limitations

- Widgets must load all external libraries from CDN. An internet connection is required at runtime.
- [Full screen display mode](enable-your-app-copilot.md#full-screen-example) requires additional implementation beyond what the skill generates.
- The skill doesn't handle MCP server registration or deployment to the Microsoft 365 admin center. You must complete those steps separately.
- Authentication (OAuth 2.1, Microsoft Entra SSO) is handled by the MCP host environment, not the widget HTML itself.

## Related documentation

### Microsoft 365 developer documentation

- [MCP Apps now available in Copilot Chat](https://devblogs.microsoft.com/microsoft365dev/mcp-apps-now-available-in-copilot-chat/)
- [Microsoft 365 Agents Toolkit](/microsoftteams/platform/toolkit/teams-toolkit-fundamentals)

### Power Platform documentation

- [Create and edit generative pages with AI code generation tools](/power-apps/maker/model-driven-apps/generative-page-external-tools)
- [Power Platform CLI reference](/power-platform/developer/cli/introduction)

### External references

- [Model Context Protocol (MCP) specification](https://modelcontextprotocol.io/)
- [Fluent UI Web Components](https://fluent2.microsoft.design/)
- [Power Platform Skills repository](https://github.com/microsoft/power-platform-skills)
