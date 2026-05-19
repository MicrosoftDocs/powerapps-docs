---
title: Create and edit canvas apps with AI code generation tools
description: Learn how to use AI code generation tools such as GitHub Copilot CLI and Claude Code to create and edit canvas apps in Power Apps.
author: shivanichander
ms.author: shivchan
ms.reviewer: mduelae
ms.date: 05/19/2026
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

# Create and edit canvas apps with AI code generation tools (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

This article explains how to use AI code generation tools, such as GitHub Copilot CLI and Claude Code, to create and edit canvas apps in Power Apps. With this approach, you describe what you want in natural language and use a local tool to generate and validate app code.

[!INCLUDE [preview-note-pp](~/../shared-content/shared/preview-includes/preview-note-pp.md)]

Using AI code generation tools with canvas apps gives you an authoring option that complements the visual experience in Power Apps at [make.powerapps.com](https://make.powerapps.com).

## What you can do with code generation tools

- **Create new canvas apps** from plain-language requirements.
- **Update existing canvas apps** by describing the changes you want.
- **Work locally** in your preferred IDE and development environment while syncing with a live coauthoring session.

## How it works

1. You describe what you want to build in natural language. For example, you might say, "Create a canvas app for tracking expense reports with an approval workflow."
1. The AI code generation tool uses installed canvas app skills to discover available controls, connectors, and data sources. It can ask follow-up questions to clarify your requirements.
1. The tool generates `.pa.yaml` files that define your screens, controls, and Power Fx formulas.
1. The tool validates the generated code by using the canvas app authoring MCP server and fixes any validation errors.
1. The app syncs with Power Apps Studio through the coauthoring session.

## Prerequisites

Before you start, make sure that you have the required software and permissions.

### Software requirements

| Component | Minimum version | More information |
|-----------|-----------------|------------------|
| .NET SDK | 10.0 or later | [Download .NET SDK](https://dotnet.microsoft.com/download/dotnet/10.0) |
| GitHub Copilot CLI, Claude Code, or another code generation tool | Latest | [GitHub Copilot CLI](https://github.com/features/copilot/cli/) or [Claude Code](https://claude.ai/code) |

### Additional requirements

- A Power Platform environment and permission to create or edit a canvas app.
- Power Apps Studio open with **coauthoring** enabled for the app that you want to create or edit.
  - To enable coauthoring, open your app in Power Apps Studio, go to **Settings** > **Updates**, and turn on **Coauthoring**.

## Install the canvas apps plugin

To install the canvas apps MCP plugin, run the following commands in GitHub Copilot CLI or Claude Code.

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

## Configure the canvas app authoring MCP server

The canvas apps plugin uses an MCP (Model Context Protocol) server to communicate with Power Apps. Before you create or edit apps, configure this connection.

1. Open your canvas app in Power Apps Studio and confirm that **coauthoring** is enabled.
1. Copy the Power Apps Studio URL from your browser.
1. Run `/configure-canvas-mcp` in your AI tool, or ask the tool to configure the MCP server.
1. Provide the Designer URL when prompted. The tool extracts the environment ID, app ID, and cluster information automatically.

By using the MCP server, your AI tool can list and describe available controls, discover APIs and data sources, validate app YAML, and sync app state from the live coauthoring session.

The canvas apps plugin [repository](https://aka.ms/canvas-authoring-mcp) includes control documentation, design guidance, technical reference, and workflow instructions that help you create code that follows canvas app requirements.

## Skills overview

The canvas apps plugin provides these skills for working with canvas apps.

| Skill | Command | Description |
|-------|-------------|---------|
| Generate canvas app | `/generate-canvas-app` | Create a new canvas app from a natural language description |
| Edit canvas app | `/edit-canvas-app` | Edit an existing canvas app from a natural language description |
| Configure Canvas MCP | `/configure-canvas-mcp` | Register the canvas app authoring MCP server with your AI tool |

These skills let you describe what you want to build, generate `.pa.yaml` files for your app, validate those files against the canvas authoring server, and sync changes with a live Power Apps Studio session.

## Create a new canvas app

Follow this workflow when you build a new app from scratch.

1. Start a conversation with your AI tool. Describe what you want to create, including the layout and the data you want to use, such as Dataverse tables or connectors. The more specific you are, the better the initial result is likely to be. You can also attach images or other materials to guide the visuals, theming, and layout. For example:
   - "Create a canvas app for tracking inventory with a searchable list and detail view"
   - "Build a canvas app for employee onboarding with a multi-step form"
   - "Make a canvas app dashboard showing sales metrics with charts and KPIs"
   - "Create a canvas app for field inspections with photo capture"
1. Answer any clarifying questions. The AI tool uses the MCP server to discover available controls and data sources and asks questions to better understand your requirements.
1. Review the generated code and validate it. The AI tool generates `.pa.yaml` files for each screen and validates them by using the canvas app authoring MCP server. The tool fixes validation errors automatically, and your changes sync with the live coauthoring session in Power Apps Studio.
1. Test and iterate. Open your canvas app in Power Apps Studio to preview and test it. If you need changes, return to your AI tool and describe the updates in natural language.

## Edit an existing canvas app

Use this workflow to update an app that already exists in your coauthoring session.

1. Sync the existing app. In your AI code generation tool, ask to edit your canvas app. The tool syncs the current app state from the coauthoring session and pulls the existing screens and controls into local `.pa.yaml` files. For example, "I want to edit my expense tracking canvas app."
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

1. Verify that the .NET 10 SDK is installed by running `dotnet --version` in your terminal.
1. Ensure that your Power Apps Studio session is still active and that coauthoring is enabled.
1. Run `/configure-canvas-mcp` again with a fresh Designer URL.

### Revert to a working version

If recent changes break your app or make problems worse, ask the AI tool to roll back to a previous working version. For example:

> The recent changes broke the app. Please revert to the last working version.

The AI tool then:

1. Syncs the current state from the coauthoring session.
1. Identifies the changes that you made.
1. Restores the previous working code.
1. Validates and resyncs the stable version.

## Best practices

- Start simple. Begin with a basic version of your app and add complexity over time.
- Test often. Preview your app in Power Apps Studio after significant changes.
- Be specific. Detailed requirements usually produce better initial results.
- Reuse patterns. Reference similar apps or UI patterns when you describe your requirements.
- Validate generated code. Always review the generated `.pa.yaml` files to make sure that they meet your organization's standards and compliance requirements.
- Describe the visual direction. If you want a specific layout or style, include that guidance in your prompt.

> [!IMPORTANT]
> AI code generation tools make a best-effort attempt to generate complete, production-ready code that follows accessibility and security best practices, but you're still responsible for validation. Make sure that the generated code meets your organization's standards, policies, and compliance requirements.

## Related content

- [Create a canvas app from scratch](create-blank-app.md)
- [Power Apps canvas app overview](getting-started.md)
