---
title: Create and edit canvas apps with AI code generation tools
description: Learn how to use AI code generation tools such as GitHub Copilot CLI and Claude Code to create and edit canvas apps in Power Apps.
author: tashascott
ms.author: tashas
ms.reviewer: mduelae
ms.date: 08/27/2026
ms.topic: how-to
ms.service: powerapps
ms.subservice: canvas-maker
search.audienceType:
- maker
- developer
ms.collection:
- bap-ai-copilot
applies_to:
- PowerApps
ms.contributors:
  - mikehung
  - lesaltzm
---

# Create and edit canvas apps with AI code generation tools 

This article explains how to use AI code generation tools, such as GitHub Copilot and Claude Code, to build and edit canvas apps in Power Apps. With this approach, you describe what you want in natural language and use a local tool to generate and validate app code.

Using AI code generation tools with canvas apps gives you an authoring option that complements the visual experience in Power Apps at [make.powerapps.com](https://make.powerapps.com).

## What you can do with code generation tools

- **Build new canvas apps** from blank using plain-language requirements.
- **Update existing canvas apps** by describing the changes you want.
- **Work locally** in your preferred IDE and development environment while syncing with a live coauthoring session.

> [!IMPORTANT]
> The app must already exist. It can be new and completely blank, but you must create it in Power Apps, save it in the intended environment, and enable coauthoring before connecting. 

## How it works

1. You create or open a canvas app in Power Apps Studio and connect your AI code generation tool to its coauthoring session.
1. You describe what you want to build in natural language. For example, you might say, "Create a canvas app for tracking expense reports with an approval workflow."
1. The AI code generation tool uses installed canvas app skills to discover available controls, connectors, and data sources. It can ask follow-up questions to clarify your requirements.
1. The tool generates `.pa.yaml` files that define your screens, controls, and Power Fx formulas.
1. The tool validates the generated code by using the canvas app authoring MCP server and fixes any validation errors.
1. The app syncs with Power Apps Studio through the coauthoring session.

## Prerequisites

Before you start, ensure that you have the required software and permissions.

### Software requirements

| Component | Requirements | More information |
|-----------|-----------------|------------------|
| .NET SDK | Version 10.0 or later | [Download .NET SDK](https://dotnet.microsoft.com/download/dotnet/10.0) |
| A coding agent | Support for MCP servers and agent plugins | For example, [GitHub Copilot](https://github.com/features/copilot), Claude Code, or another code generation tool. |

### Additional requirements

- A Power Platform environment and permission to create or edit a canvas app.
- An existing, saved canvas app in the intended environment.
- Power Apps Studio open with **[coauthoring](copresence-power-apps-studio.md)** enabled for the app that you want to build or edit.
  - To enable coauthoring, open your app in Power Apps Studio, go to **Settings** > **Updates**, and turn on **Coauthoring**.

Confirm that the .NET 10 SDK or later is installed:

```shell
dotnet --list-sdks
```

The output must include a version that begins with `10.` or a later major version. If the command isn't found or no supported version appears, install the SDK and restart your terminal and coding agent.

## Install the canvas apps plugin

Install the canvas apps plugin from your coding agent's plugin marketplace.

### Install from a plugin marketplace

Run the following commands in a coding agent that supports plugin marketplace commands:

1. Add the Power Platform Skills marketplace plugin.

   ```shell
   /plugin marketplace add microsoft/power-platform-skills
   ```

1. Install the canvas apps plugin.

   ```shell
   /plugin install canvas-apps@power-platform-skills
   ```

After you install the plugin, configure the canvas app authoring MCP server before you create or edit apps. You can configure the server in either of these ways:

- Run the `/configure-canvas-mcp` command.
- Describe what you want to build, and let the tool guide you through setup.

If your coding agent doesn't support these commands, use its plugin marketplace interface. Search for the `microsoft/power-platform-skills` marketplace, and then install `canvas-apps`.

### Install in Visual Studio Code

1. Open the **Extensions** view.
1. Enter `@agentPlugins canvas apps` in the search field.
1. Select **Canvas Apps**, published by Microsoft, and then select **Install**.
1. Open Chat in Agent mode and confirm that the `canvas-app` and `configure-canvas-mcp` skills are available.

If agent plugins don't appear in the Extensions view, open **Preferences: Open User Settings (JSON)** from the Command Palette, add `"chat.plugins.enabled": true` inside the outer braces, save the file, and search again. For more information, see [Install a plugin from a marketplace](https://code.visualstudio.com/docs/agent-customization/agent-plugins#_install-a-plugin-from-a-marketplace).

## Configure the canvas app authoring MCP server

The canvas apps plugin uses an MCP (Model Context Protocol) server to communicate with Power Apps. Before you create or edit apps, configure this connection.

1. Open your canvas app in Power Apps Studio and confirm that **coauthoring** is enabled.
1. Keep the Power Apps Studio browser tab open for the entire session.
1. Copy the Power Apps Studio URL from your browser.
1. Run `/configure-canvas-mcp` in your AI tool, or ask the tool to configure the MCP server.
1. Provide the complete Studio URL when prompted and complete any sign-in prompt. The tool extracts the environment ID, app ID, and cluster information automatically.
1. Verify the connection by asking the agent, "List the available Canvas App controls."

The connection depends on the open Power Apps Studio coauthoring session. If you close the browser tab or the Studio session expires, reopen the app and run `/configure-canvas-mcp` again.

By using the MCP server, your AI tool can list and describe available controls, discover APIs and data sources, validate app YAML, and sync app state from the live coauthoring session.

The canvas apps plugin [repository](https://aka.ms/canvas-authoring-mcp) includes control documentation, design guidance, technical reference, and workflow instructions that help you create code that follows canvas app requirements.

## Skills overview

The canvas apps plugin provides these skills for working with canvas apps.

| Skill | Command | Description |
|-------|-------------|---------|
| Canvas app | `/canvas-app` | Build a connected blank app or edit an app that already contains screens and content |
| Configure Canvas MCP | `/configure-canvas-mcp` | Connect the canvas app authoring MCP server to the current Power Apps Studio coauthoring session |
| Add data source | `/add-data-source` | Guide you to add a connector or data source in Power Apps Studio and verify that it's available |

These skills let you describe what you want to build, generate `.pa.yaml` files for your app, validate those files against the canvas authoring server, and sync changes with a live Power Apps Studio session.

## Build a blank canvas app

Follow this workflow to build a new app in Power Apps Studio.

1. Create and save a blank canvas app in the intended environment, enable coauthoring, and connect the canvas app authoring MCP server.
1. Run `/canvas-app`, or start a conversation with your AI tool and describe what you want to create, including the layout and the data you want to use, such as Dataverse tables or connectors. Say "Canvas App" in your request to help the coding agent select the right skill. The more detail you include, the better the initial result is likely to be. You can also attach images or other materials to guide the visuals, theming, and layout. For example:
   - "Create a canvas app for tracking inventory with a searchable list and detail view"
   - "Build a canvas app for employee onboarding with a multi-step form"
   - "Make a canvas app dashboard showing sales metrics with charts and KPIs"
   - "Create a canvas app for field inspections with photo capture"
1. Answer any clarifying questions. The AI tool uses the MCP server to discover available controls and data sources and asks questions to better understand your requirements.
1. Review the generated code and validate it. The AI tool generates `.pa.yaml` files for each screen and validates them by using the canvas app authoring MCP server. The tool fixes validation errors automatically, and your changes sync with the live coauthoring session in Power Apps Studio.
1. Test and iterate. Open your canvas app in Power Apps Studio to preview and test it. If you need changes, return to your AI tool and describe the updates in natural language.

Add required connectors and data sources through the **Data** panel in Power Apps Studio. You can run `/add-data-source` for guided setup and verification.

## Edit an existing canvas app

Use this workflow to update an app that already exists in your coauthoring session.

1. Open the app in Power Apps Studio, keep the browser tab open, and connect the canvas app authoring MCP server.
1. Sync the existing app. Run `/canvas-app`, or ask to edit your canvas app. The tool syncs the current app state from the coauthoring session and pulls the existing screens and controls into local `.pa.yaml` files. For example, "I want to edit my expense tracking Canvas App."
1. Describe the updates you want. For example:
   - "Add a filter to show only pending expenses"
   - "Change the home screen layout to use a card-based grid"
   - "Add a new screen for viewing expense history with charts"
   - "Update the form to include a dropdown for expense categories"
1. Review, validate, test, and iterate. The AI tool generates updated `.pa.yaml` files based on your requested changes and validates them with the canvas authoring server. Continue iterating with natural language instructions until the app meets your requirements.

## Troubleshooting

### App doesn't reflect changes

If your changes don't appear in Power Apps Studio:

1. Verify the connection to the canvas app authoring MCP server by asking the tool to list available controls.
1. Ensure coauthoring is enabled in your Power Apps Studio session (**Settings** > **Updates** > **Coauthoring**).
1. Check that the MCP server is configured with the correct environment ID and app ID by running `/configure-canvas-mcp` again.

### MCP server connection problems

If the canvas app authoring MCP server isn't responding:

1. Verify that the .NET 10 SDK is installed by running `dotnet --list-sdks` in your terminal.
1. Ensure that your Power Apps Studio session is still active and that coauthoring is enabled.
1. Confirm that you copied the URL from the app's edit session in Power Apps Studio, not from the app player or Power Apps home page.
1. Run `/configure-canvas-mcp` again with a fresh Studio URL.

### Controls, connectors, or data sources are missing

If expected resources aren't available:

1. Confirm that the MCP server is connected to the intended app and environment.
1. Add required connectors and data sources through the **Data** panel in Power Apps Studio.
1. Ask the agent to list the resources again.
1. Check whether your organization's data policies restrict the resource.

### Plugin installation problems

If the plugin doesn't appear or install, confirm that your coding agent supports MCP and agent plugins. In Visual Studio Code, search for `@agentPlugins canvas apps`, install **Canvas Apps** published by Microsoft, and then restart or reload Visual Studio Code. If the plugin is still unavailable, ask your administrator whether organizational policies block agent plugins, third-party MCP servers, or local MCP processes.

If `dotnet` or `dnx` isn't found, install the .NET 10 SDK, not only the runtime. Restart your terminal and coding agent, and then run `dotnet --list-sdks`.

If the MCP server can't download its package and the error mentions `https://api.nuget.org/v3/index.json`, run `dotnet nuget list source`. Confirm that an enabled source contains `Microsoft.PowerApps.CanvasAuthoring.McpServer`. If none does, ask your administrator which approved NuGet source to use. Update the canvas apps plugin before retrying.

## Security considerations

The plugin handles credentials through the official Azure Identity SDK and doesn't store or manage tokens directly.

- Install the plugin only from a trusted marketplace, and keep the plugin, coding agent, and .NET SDK current.
- Connect with an account that has only the permissions needed to edit the intended app.
- Check the Power Apps environment, app URL, proposed action, and tool parameters before you approve an operation.
- Validate generated changes in a development or nonproduction app before you apply them to a production app.
- Never paste passwords, access tokens, connection strings, or other secrets into prompts, issue reports, or logs.
- Be aware of your organization's connector and data loss prevention policies.
- Review unexpected actions proposed by your coding agent, especially when you work with external data.

For more information, see [Defend against indirect prompt injection attacks](/security/zero-trust/sfi/defend-indirect-prompt-injection) and [Manage Power Platform data policies](/power-platform/admin/prevent-data-loss).

## Best practices

- Start simple. Begin with a basic version of your app and add complexity over time.
- Test often. Preview your app in Power Apps Studio after significant changes.
- Be specific. Detailed requirements usually produce better initial results.
- Reuse patterns. Reference similar apps or UI patterns when you describe your requirements.
- Validate generated code. Always review the generated `.pa.yaml` files to make sure that they meet your organization's standards and compliance requirements.
- Describe the visual direction. If you want a specific layout or style, include that guidance in your prompt.

> [!IMPORTANT]
> AI code generation tools make a best-effort attempt to generate complete, production-ready code that follows accessibility and security best practices, but you're still responsible for validation. Ensure that the generated code meets your organization's standards, policies, and compliance requirements.

## Related content

- [Canvas Apps plugin repository](https://aka.ms/canvas-authoring-mcp)
- [Report a Canvas Apps plugin issue](https://aka.ms/power-skills-canvas-issues)
- [Create a canvas app from scratch](create-blank-app.md)
- [Power Apps canvas app overview](getting-started.md)
