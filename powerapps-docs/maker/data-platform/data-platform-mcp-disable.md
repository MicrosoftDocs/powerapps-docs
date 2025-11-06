---
title: Enable the Dataverse model context protocol (MCP) server
description: Step-by-step instructions about how to enable or disable a Microsoft Dataverse model context protocol server that uses advanced connector policies. 
author: anibakore-msft
contributors: spatankar
ms.component: cds
ms.topic: how-to
ms.date: 09/22/2025
ms.subservice: dataverse-maker
ms.author: banirud
ms. reviewer: matp
search.audienceType: 
  - maker
---
# Enable the Dataverse MCP server for an environment (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Microsoft Dataverse model context protocol (MCP) is provided through the connector infrastructure. While the Dataverse connector itself is a non-blockable connector—meaning you can't disable it using traditional data loss prevention (DLP) settings within the Power Platform admin center—you can selectively disable a Dataverse MCP server by setting advanced connector policies.

[!INCLUDE [preview-note-pp.md](../../../shared/preview-includes/preview-note-pp.md)]

## Prerequisites

- Power Platform administrator role in order to manage environment settings, environment group, and connector policies.
- The steps described in this article require that the environment be a Managed Environment.
- By default, the Dataverse MCP server is disabled for environments. You must enable it in the Power Platform admin center before you can connect to it. More information: [Enable the Dataverse MCP server for an environment](#enable-the-dataverse-mcp-server-for-an-environment)
- The Power Platform with Dataverse environment must be setup with the MCP via connector as described in [Connect to Dataverse with model context protocol (preview)](data-platform-mcp.md).

## Enable the Dataverse MCP server for an environment

1. To enable Dataverse MCP server, go to [Power Platform Admin Center](https://admin.powerplatform.microsoft.com/). Select **Manage** > **Environments**.
1. Select the **Environment Name** where you want to turn on the Dataverse MCP server, and then select **Settings**.
1. Under **Settings**, select **Product** > **Features**.
1. Under **Features** scroll down to locate **Dataverse MCP server** and turn it **On**.

## Connect to Dataverse MCP server in Visual Studio Code

1. Click this link:
      https://<orgurl> /main.aspx?appid=76d9c540-8ca5-f011-b422-000d3a346029&pagetype=entitylist&etn=allowedmcpclient&viewid=2f87c3fe-4ed3-4425-9800-77ff580d9135&viewType=1039
2. Select Microsoft Github Copilot
   <img width="1090" height="591" alt="image" src="https://github.com/user-attachments/assets/f138cfa6-771d-4135-9551-a17d57a3d8ed" />
3. Turn the Is Enabled = Yes
   <img width="1090" height="584" alt="image" src="https://github.com/user-attachments/assets/2c359ee9-9696-48f0-a232-188e672e048d" />


   

## Disable the Dataverse MCP server for an  environment

1. Go to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/), select **Manage**, and then select **Environment groups**. 
1. Select **New group** to create a new environment group or select an existing group where you want to turn off the Dataverse MCP server.
1. Open the environment group, and then on the **Rules** tab select **Advanced connector policies (preview)**.
1. Select the **Microsoft Dataverse** connector, and then select **Edit actions**.
   :::image type="content" source="media/data-platform-mcp/data-platform-connector.png" alt-text="Screenshot showing where to select the Microsoft Dataverse connector and then select Edit actions" lightbox="media/data-platform-mcp/data-platform-connector.png":::
1. Locate the action named **Dataverse MCP Server**, and turn **Off** this action as needed for your environment group.
   :::image type="content" source="media/data-platform-mcp/dataverse-mcp-server-action.png" alt-text="Screenshot of the Dataverse MCP server action" lightbox="media/data-platform-mcp/dataverse-mcp-server-action.png":::
1. Select **Save** and then select **Publish rules** to the enable the rule.

## Related articles

[Advanced connector policies (preview) - Power Platform](/power-platform/admin/advanced-connector-policies?tabs=new)

[Connect to Dataverse with model context protocol (preview)](data-platform-mcp.md)

[Connect to Dataverse with model context protocol FAQ (preview)](data-platform-mcp-faq.md)
