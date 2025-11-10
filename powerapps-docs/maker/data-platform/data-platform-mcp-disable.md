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
1. The list of available clients is shown. Open the client that you want. In this example, the **Microsoft GitHub Copilot** client is enabled.
1. <!-- Stop here-->

<!-- REMOVE THIS IF NO LONGER NEEDED
## Connect to Dataverse MCP server in Visual Studio Code

1. Go to this view in Dataverse, where *&lt;orgurl&gt;* is your environment URL, such as *contoso.crm.dynamics.com*:

      `https://*<orgurl>*/main.aspx?appid=76d9c540-8ca5-f011-b422-000d3a346029&pagetype=entitylist&etn=allowedmcpclient&viewid=2f87c3fe-4ed3-4425-9800-77ff580d9135&viewType=1039`
1. Open the **Microsoft Github Copilot** record.
   :::image type="content" source="media/data-platform-mcp/allowed-mcp-clients.png" alt-text="Allowed MCP clients" lightbox="media/data-platform-mcp/allowed-mcp-clients.png":::
1. Turn **Is Enabled** to **Yes**.
   :::image type="content" source="media/data-platform-mcp/github-copilot-record.png" alt-text="GitHub Copilot record enable." lightbox="media/data-platform-mcp/github-copilot-record.png":::
1. Select **Save & Close**.

## Disable the Dataverse MCP server for an  environment

1. Go to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/), select **Manage**, and then select **Environment groups**. 
1. Select **New group** to create a new environment group or select an existing group where you want to turn off the Dataverse MCP server.
1. Open the environment group, and then on the **Rules** tab select **Advanced connector policies**.
1. Select the **Microsoft Dataverse** connector, and then select **Edit actions**.
   :::image type="content" source="media/data-platform-mcp/data-platform-connector.png" alt-text="Screenshot showing where to select the Microsoft Dataverse connector and then select Edit actions" lightbox="media/data-platform-mcp/data-platform-connector.png":::
1. Locate the action named **Dataverse MCP Server**, and turn **Off** this action as needed for your environment group.
   :::image type="content" source="media/data-platform-mcp/dataverse-mcp-server-action.png" alt-text="Screenshot of the Dataverse MCP server action" lightbox="media/data-platform-mcp/dataverse-mcp-server-action.png":::
1. Select **Save**, and then select **Publish rules** to the enable the rule. -->

## Related articles

[Advanced connector policies - Power Platform](/power-platform/admin/advanced-connector-policies?tabs=new)

[Connect to Dataverse with model context protocol](data-platform-mcp.md)

[Connect to Dataverse with model context protocol FAQ](data-platform-mcp-faq.md)
