---
title: Create and edit canvas apps with AI code generation tools
description: Learn how to use AI code generation tools like Github Copilot and Claude Code to create and edit canvas apps in Power Apps.
author: shivanichander
ms.author: shivchan
ms.reviewer: mduelae
ms.date: 04/06/2026
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

This article describes how to use AI code generation tools, such as GitHub Copilot CLI and Claude Code, to create and edit canvas apps in Power Apps. By using this approach, you can integrate advanced code generation capabilities directly into your development workflow. You can create new canvas apps or iterate on existing ones by using natural language instructions.

[!INCLUDE [preview-note-pp](~/../shared-content/shared/preview-includes/preview-note-pp.md)]

Using AI code generation tools with canvas apps provides an alternative development approach that complements the UI-based experience in Power Apps (make.powerapps.com). 

## What you can do with code generation tools

- *Create new canvas apps* by using plain-language requirements.
- *Update existing canvas apps* by requesting changes or enhancements through your AI tool.
- *Work locally* by using your preferred IDE and development tools, syncing with live coauthoring sessions.

## How it works

1. You describe what you want to build in natural language, for example, "Create a canvas app for tracking expense reports with an approval workflow."
1. The AI code generation tool uses installed canvas app skills to discover available controls, connectors, and data sources. It asks clarifying questions about your requirements.
1. The tool generates `.pa.yaml` files that define your app screens, controls, and Power Fx formulas.
1. The tool validates the generated code by using the canvas app authoring MCP server and fixes any errors.
1. Your canvas app syncs with Power Apps Studio through the coauthoring session.

## Prerequisites

Before you start, make sure you have the required software and permissions described in this section.

### Software requirements

| Component | Minimum version | More information |
|-----------|-----------------|------------------|
| .NET SDK | 10.0 or later | [Download .NET SDK](https://dotnet.microsoft.com/download/dotnet/10.0) |
| GitHub Copilot CLI, Claude Code, or other code generation tool | Latest | [GitHub Copilot CLI](https://github.com/features/copilot/cli/) or [Claude Code](https://claude.ai/code) |

### Additional requirements

- A Power Platform environment with a canvas app.
- Power Apps Studio open with **coauthoring enabled** for your canvas app.
   - To enable coauthoring, open your app in Power Apps Studio, go to **Settings** > **Updates**, and turn on **Coauthoring**.

## Install the canvas apps plugin

To install the canvas apps MCP plugin, run the following commands in either Copilot CLI, or Claude Code:

1. Add the Power Platform Skills marketplace plugin: 

   ```shell
   /plugin marketplace add microsoft/power-platform-skills
   ```

1. Install the canvas apps plugin: 

   ```shell
   /plugin install canvas-apps@power-platform-skills
   ```

After you install the plugin, you need to configure the canvas app authoring MCP server before you can create or edit apps. You can configure the server by either of the following options:

- Run the `/configure-canvas-mcp` command to set up the MCP server connection.
- Describe what you want to build - the tool detects that the MCP server needs to be configured and guides you through setup.

## Configure the canvas app authoring MCP server

The canvas apps plugin uses an MCP (Model Context Protocol) server to communicate with Power Apps. Before creating or editing apps, you need to configure this server connection:

1. Open your canvas app in Power Apps Studio and ensure **coauthoring** is enabled.
1. Copy the Power Apps Studio URL from your browser.
1. Run `/configure-canvas-mcp` in your AI tool, or ask the tool to configure the MCP server.
1. Provide the Designer URL when prompted. The tool extracts your environment ID, app ID, and cluster information automatically.

By using the MCP server, your AI tool can list and describe available controls, discover APIs and data sources, validate app YAML, and sync app state from live coauthoring sessions.

The canvas-apps plugin [repository](https://aka.ms/canvas-authoring-mcp) includes control documentation, design guidance, technical reference, and workflow instructions necessary to create code adhering to canvas app requirements. Refer to the repository for information on accessing and using these resources with your preferred tool.

## Skills overview

The canvas apps plugin provides these skills for working with canvas apps.

| Skill | Command | Description |
|-------|-------------|---------|
| Generate canvas app | `/generate-canvas-app` | Create a new canvas app from a natural language description |
| Edit canvas app | `/edit-canvas-app` | Edit an existing canvas app from a natural language description |
| Configure Canvas MCP | `/configure-canvas-mcp` | Register the canvas app authoring MCP server with your AI tool |

These skills enable you to describe what you want to build and have the AI tool generate complete `.pa.yaml` files for your canvas app, validate them against the Canvas Authoring server, and sync changes with your live Power Apps Studio session.

## Create a new canvas app

Follow this workflow when building a new app from scratch.

1. Start a conversation with your AI tool. Describe what you want to create, including the layout and what data you want to include (which Dataverse tables, or connectors to use). Be as specific as you want - the more vague you are with the request, the more details the agent tries to fill in itself. You can also attach or provide an image or other materials to help guide the visuals, theming, and layout. For example:
   - "Create a canvas app for tracking inventory with a searchable list and detail view"
   - "Build a canvas app for employee onboarding with a multi-step form"
   - "Make a canvas app dashboard showing sales metrics with charts and KPIs"
   - "Create a canvas app for field inspections with photo capture"

2. Answer clarifying questions. The AI tool discovers available controls and data sources using the MCP server and asks questions to understand your requirements. Be specific about business needs and data requirements and mention any specific UI components or layout preferences.

3. Review code and validate. The AI tool generates `.pa.yaml` files for each screen and validates them using the canvas app authoring MCP server. The tool fixes any validation errors automatically. Your changes sync with the live coauthoring session in Power Apps Studio.

4. Test and iterate. Open your canvas app in Power Apps Studio to preview and test. If you need to make changes, return to your AI tool and describe the updates using natural language.

## Edit an existing canvas app

Use this workflow to update an app that already exists in your coauthoring session.

1. Sync the existing app. In your AI code generation tool, ask to edit your canvas app. The tool syncs the current app state from the coauthoring session, pulling all existing screens and controls into local `.pa.yaml` files. For example, "I want to edit my expense tracking canvas app."

2. Describe your updates. Tell the AI tool what changes you want to make. For example:
   - "Add a filter to show only pending expenses"
   - "Change the home screen layout to use a card-based grid"
   - "Add a new screen for viewing expense history with charts"
   - "Update the form to include a dropdown for expense categories"

3. Review, validate, test, and iterate. The AI tool generates updated `.pa.yaml` files based on your requested changes and validates them with the Canvas Authoring server. Follow the same review and test process described in the "Create a new canvas app" section. Continue iterating with natural language instructions until the app meets your requirements.

## Troubleshooting

### App doesn't reflect changes

If your changes don't appear in Power Apps Studio:

1. Verify the connection to the canvas app authoring MCP server by asking the tool to list available controls.
1. Ensure coauthoring is enabled in your Power Apps Studio session (**Settings** > **Updates** > **Coauthoring**).
1. Check that the MCP server is configured with the correct environment ID and app ID by running `/configure-canvas-mcp` again.

### MCP server connection problems

If the canvas app authoring MCP server isn't responding:

1. Verify that the .NET 10 SDK is installed by running `dotnet --version` in your terminal.
1. Ensure your Power Apps Studio session is still active and coauthoring is enabled.
1. Re-run `/configure-canvas-mcp` with a fresh Designer URL.

### Revert to a working version

If recent changes break your app or make problems worse, ask the AI tool to roll back to a previous working version:

"The recent changes broke the app. Please revert to the last working version."

The AI tool then:

1. Syncs the current state from the coauthoring session
1. Identifies the changes that you made
1. Restores the previous working code
1. Validates and resyncs the stable version

## Best practices

- Start simple. Begin with a basic version of your app and iterate to add complexity.
- Test frequently. Preview your app in Power Apps Studio after each significant change.
- Be specific. Provide detailed requirements to get better initial results.
- Use existing patterns. Reference similar apps or UI patterns when describing your requirements.
- Validate generated code. Always review the generated `.pa.yaml` files to ensure they meet your organization standards and compliance requirements.
- Bold design choices. Don't settle for generic layouts - describe the visual style and aesthetic direction you want.

> [!IMPORTANT]
> While AI code generation tools make a best-effort attempt to generate complete, production-ready code with accessibility and security best practices, you're ultimately responsible for validating the code. Ensure the generated code meets your organization standards, policies, and compliance requirements.

## Related content

- [Create a canvas app from scratch](create-blank-app.md)
- [Power Apps canvas app overview](getting-started.md)
