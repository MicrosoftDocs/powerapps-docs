---
title: Connect Dataverse MCP with GitHub Copilot in Visual Studio Code
description: Learn how to connect to Dataverse using the Model Context Protocol (MCP) server in Visual Studio Code GitHub Copilot. Follow step-by-step instructions to enable seamless data interaction.
#customer intent: As a Power Apps maker, I want to connect to Dataverse using the Model Context Protocol server so that I can choose from different MCP clients that can interact with my data through natural language queries.
author: ShefaaliP
ms.author: spatankar
ms.reviewer: matp
ms.date: 11/10/2025
ms.topic: how-to
ms.collection: bap-ai-copilot
ms.subservice: dataverse-maker
---

# Connect Dataverse MCP with GitHub Copilot in Visual Studio Code

This article explains how to set up and use the Microsoft Dataverse model context protocol (MCP) server with Visual Studio GitHub Copilot.

## Prerequisites

- The Visual Studio Code GitHub Copilot MCP client must be allowed in the environment. More information: [Configure and manage the Dataverse MCP server for an environment](data-platform-mcp-disable.md#configure-and-manage-the-dataverse-mcp-server-for-an-environment)
- Visual Studio Code installed with GitHub Copilot extension. More information: [GitHub Copilot extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)

## Steps to connect to Dataverse MCP server in Visual Studio Code

1. Open Visual Studio Code. Select **View** > **Command Palette** (Ctrl+Shift+P), type **MCP: Add Server** and press **Enter**.  

1. Select **HTTP or Server Sent Events** and then press **Enter**.  

1. Paste your instance URL, such as `https://contoso.crm.dynamics.com/`, append */api/mcp* to it, and press Enter. You can get the instance URL at make.powerapps.com > **Settings** (gear icon) > **Session details** > **Instance url**.
   :::image type="content" source="media/data-platform-mcp-vsc/data-platform-mcp-github-org-url.png" alt-text="Organization URL with appendix.":::

   This step generates the MCP server configuration in Visual Studio Code.  
   
1. Press **Ctrl+Alt+I** and ensure that agent mode is selected.
   :::image type="content" source="media/data-platform-mcp-vsc/vscode-agent-mode.png" alt-text="Agent mode in Visual Studio Code GitHub Copilot":::

## Related articles

[Connect to Dataverse with Model Context Protocol](data-platform-mcp.md)