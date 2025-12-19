---
title: Connect to Dataverse with model context protocol in Microsoft Copilot Studio
description: Learn how to connect to Dataverse using the Model Context Protocol (MCP) server in Microsoft Copilot Studio. Follow step-by-step instructions to enable seamless data interaction.
#customer intent: As a Power Apps maker, I want to connect to Dataverse using the Model Context Protocol server so that I can choose from different MCP clients that can interact with my data through natural language queries.
author: ShefaaliP
ms.author: spatankar
ms.reviewer: matp
ms.date: 11/10/2025
ms.topic: how-to
ms.collection: bap-ai-copilot
ms.subservice: dataverse-maker
---

# Connect to Dataverse with model context protocol in Microsoft Copilot Studio

This article explains how to set up and use the Microsoft Dataverse model context protocol (MCP) server with Microsoft Copilot Studio. By following the steps in this article, you can interact with Dataverse, asking natural language questions like *show me my contacts* and receive answers based on stored data.

## Prerequisites

- The Microsoft Copilot Studio MCP client must be allowed in the environment. More information: [Configure and manage the Dataverse MCP server for an environment](data-platform-mcp-disable.md#configure-and-manage-the-dataverse-mcp-server)

## Connect to Dataverse using an MCP server in Microsoft Copilot Studio

1. Go to [Power App](https://make.powerapps.com/) and select your environment from the top right environment selector.
1. From the left navigation pane, select **Agents** > **Create new agent**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select **Create**.
1. Scroll down to the **Tools** section and select **+ Add tool**.
1. Select **Model Context Protocol**, and then select **Dataverse MCP Server**.
    - If there's no existing Dataverse connection, you're prompted to connect one.
1. Select **Add to agent**.

The individual tools available on this MCP server can be viewed and modified by selecting **...** > **Edit** next to the **Dataverse MCP Server** tool.

You can now interact with the Dataverse MCP Server tool in the **Test your agent** chat pane. Try commands like "list tables in Dataverse," "describe table account," or "how many accounts do I have." :::image type="content" source="media/data-platform-mcp-copilot-studio/mcp-copilot-studio.png" alt-text="Screenshot of Dataverse MCP in Copilot Studio.":::

## Related articles

[Connect to Dataverse with Model Context Protocol](data-platform-mcp.md)
