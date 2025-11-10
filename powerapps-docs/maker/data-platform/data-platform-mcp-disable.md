---
title: Configure the Dataverse model context protocol (MCP) server
description: Step-by-step instructions about how to enable or disable a Microsoft Dataverse model context protocol server that uses advanced connector policies. 
author: ShefaaliP
ms.component: cds
ms.topic: how-to
ms.date: 11/17/2025
ms.subservice: dataverse-maker
ms.author: spatankar
ms. reviewer: matp
search.audienceType: 
  - maker
---
# Configure the Dataverse MCP server for an environment

<!--Needs intro -->

## Prerequisites

- Power Platform administrator role in order to enable Dataverse MCP server, manage environment settings, environment group, and connector policies.
- The steps described in this article require that the environment be a Managed Environment.
- By default, the Dataverse MCP server is enabled for all environments in Microsoft Copilot Studio. You must enable the additional clients it in the Power Platform admin center before you can connect to the client.

## Configure and manage the Dataverse MCP server for an environment

1. Go to [Power Platform Admin Center](https://admin.powerplatform.microsoft.com/). Select **Manage** > **Environments**.
1. Select the **Environment Name** where you want to turn on the Dataverse MCP server, and then select **Settings**. Under **Settings**, select **Product** > **Features**. Scroll down to locate **Dataverse Model Context Protocol**.
1. By default the **Allow MCP clients to interact with Dataverse MCP server** is turned on for Microsoft Copilot Studio, clear it to turn it off. <!--You're prompted for confirmation that it will halt any existing workflows. Need clarification on impact. -->
1. To enable the Dataverse MCP server for Visual Studio GitHub Copilot or any other non-Microsoft client, you must use advanced settings to enable each client. Select **Advanced Settings**.
      :::image type="content" source="media/data-platform-mcp/data-platform-mcp-enable-clients.png" alt-text="Open GitHub Copilot to enable.":::

1. The list of available clients is shown. Open the client that you want. In this example, the **Microsoft GitHub Copilot** client is enabled.
   :::image type="content" source="media/data-platform-mcp/data-platform-mcp-enable-github-copilot.png" alt-text="Enable GitHub Copilot client." lightbox="media/data-platform-mcp/data-platform-enable-mcp-github-copilot.png":::
1. On the MCP client record, set **Is Enabled** to **Yes**.
   :::image type="content" source="media/data-platform-mcp/data-platform-mcp-client-enabled.png" alt-text="GitHub Copilot client enabled." lightbox="media/data-platform-mcp/data-platform-mcp-client-enabled.png":::

1. Select **Save & Close**.

## Disable the Dataverse MCP server for an  environment in Copilot Studio <!-- What do you mean by "in Copilot Studio?" Worded this way it makes it sound like you disable the server in MCS, which is not how these instructions work. Do you mean only the Microsoft Copilot Studio MCP server or any MCP servers that appear in Copilot Studio?-->

1. Go to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/), select **Manage**, and then select **Environment groups**.
1. Select **New group** to create a new environment group or select an existing group where you want to turn off the Dataverse MCP server.
1. Open the environment group, and then on the **Rules** tab select **Advanced connector policies**.
1. Select the **Microsoft Dataverse** connector, and then select **Edit actions**.
   :::image type="content" source="media/data-platform-mcp/data-platform-connector.png" alt-text="Screenshot showing where to select the Microsoft Dataverse connector and then select Edit actions" lightbox="media/data-platform-mcp/data-platform-connector.png":::
1. Locate the action named **Dataverse MCP Server**, and turn **Off** this action as needed for your environment group.
   :::image type="content" source="media/data-platform-mcp/dataverse-mcp-server-action.png" alt-text="Screenshot of the Dataverse MCP server action" lightbox="media/data-platform-mcp/dataverse-mcp-server-action.png":::
1. Select **Save**, and then select **Publish rules** to the enable the rule. 

## Related articles

[Advanced connector policies - Power Platform](/power-platform/admin/advanced-connector-policies?tabs=new)

[Connect to Dataverse with model context protocol](data-platform-mcp.md)

[Connect to Dataverse with model context protocol FAQ](data-platform-mcp-faq.md)
