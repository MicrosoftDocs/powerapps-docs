---
title: Connect Dataverse MCP with GitHub Copilot in Visual Studio Code and Copilot CLI
description: Learn how to connect to Dataverse using the Model Context Protocol (MCP) server in Visual Studio Code GitHub Copilot and GitHub Copilot CLI. Follow step-by-step instructions to enable seamless data interaction.
#customer intent: As a Power Apps maker, I want to connect to Dataverse using the Model Context Protocol server so that I can choose from different MCP clients that can interact with my data through natural language queries.
author: seanwat-msft
ms.author: spatankar
ms.reviewer: matp
ms.date: 03/09/2026
ms.topic: how-to
ms.collection: bap-ai-copilot
ms.subservice: dataverse-maker
---

# Connect Dataverse MCP with GitHub Copilot in Visual Studio Code and Copilot CLI

This article explains how to set up and use the Microsoft Dataverse model context protocol (MCP) server with GitHub Copilot in Visual Studio Code and GitHub Copilot CLI.

## GitHub Copilot in Visual Studio Code

### Prerequisites

- The **Microsoft GitHub Copilot** MCP client must be allowed in the environment. More information: [Configure and manage the Dataverse MCP server for an environment](data-platform-mcp-disable.md#configure-and-manage-the-dataverse-mcp-server)
- Visual Studio Code installed with GitHub Copilot extension. More information: [GitHub Copilot extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)

### Steps to connect to Dataverse MCP server in Visual Studio Code

1. Open Visual Studio Code. Select **View** > **Command Palette** (Ctrl+Shift+P), type **MCP: Add Server** and press **Enter**.  

1. Select **HTTP or Server Sent Events** and then press **Enter**.  

1. Paste your instance URL, such as `https://contoso.crm.dynamics.com/`, append */api/mcp* to it, and press Enter. You can get the instance URL at make.powerapps.com > **Settings** (gear icon) > **Session details** > **Instance url**.
   :::image type="content" source="media/data-platform-mcp-vsc/data-platform-mcp-github-org-url.png" alt-text="Organization URL with appendix.":::

   This step generates the MCP server configuration in Visual Studio Code.  
   
1. Press **Ctrl+Alt+I** and ensure that agent mode is selected.
   :::image type="content" source="media/data-platform-mcp-vsc/vscode-agent-mode.png" alt-text="Agent mode in Visual Studio Code GitHub Copilot":::

## GitHub Copilot CLI

### Prerequisites

- GitHub Copilot CLI installed. More information: [GitHub Copilot CLI](https://docs.github.com/en/copilot/github-copilot-in-the-cli)
- The **Microsoft GitHub Copilot** MCP client must be allowed in the environment. More information: [Configure and manage the Dataverse MCP server for an environment](data-platform-mcp-disable.md#configure-and-manage-the-dataverse-mcp-server)

### Option 1: Manually add the MCP server

You can configure the Dataverse MCP server in GitHub Copilot CLI by editing the MCP configuration file directly.

1. Open your MCP configuration file. For global configuration, edit `~/.copilot/mcp-config.json`. For project-scoped configuration, edit `.mcp/copilot/mcp.json` in your project directory.

1. Add the following JSON snippet. Replace `<your org URL>` with your Dataverse environment URL (for example, `https://contoso.crm.dynamics.com`).

   ```json
   {
     "mcpServers": {
       "DataverseMcp": {
         "type": "http",
         "url": "<your org URL>/api/mcp"
       }
     }
   }
   ```

1. Save the file and restart GitHub Copilot CLI for the changes to take effect.

### Option 2: Use the Dataverse plugin from the Awesome Copilot marketplace

The [Awesome Copilot](https://github.com/github/awesome-copilot) marketplace provides a Dataverse plugin that includes an `mcp-configure` skill. This skill guides you through configuring the Dataverse MCP server interactively, including environment discovery and endpoint selection.

1. Add the Awesome Copilot marketplace to your Copilot CLI:

   ```bash
   copilot plugin marketplace add github/awesome-copilot
   ```

1. Install the Dataverse plugin:

   ```bash
   copilot plugin install dataverse@awesome-copilot
   ```

1. In a Copilot chat session, use the `/dataverse:mcp-configure` skill to configure the Dataverse MCP server. The skill walks you through selecting your environment and choosing between the generally available (`/api/mcp`) and preview (`/api/mcp_preview`) endpoints.

## Related articles

[Connect to Dataverse with Model Context Protocol](data-platform-mcp.md)
