---
title: Disable the Dataverse model context protocol (MCP) server
description: Step-by-step instructions about how to disable a Microsoft Dataverse model context protocol server using advanced connector policies. 
author: anibakore-msft
ms.component: cds
ms.topic: how-to
ms.date: 07/07/2025
ms.subservice: dataverse-maker
ms.author: banirud
ms. reviewer: matp
search.audienceType: 
  - maker
---
# Disable the Dataverse MCP server using advanced connector policies (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Microsoft Dataverse model context protocol (MCP) is provided through the connector infrastructure. While the Dataverse connector itself is a non-blockable connector—meaning you can't disable it using traditional data loss prevention (DLP) settings within the Power Platform admin center—you can selectively disable a Dataverse MCP server by setting advanced connector policies.

[!INCLUDE [preview-note-pp.md](../../../shared/preview-includes/preview-note-pp.md)]

## Prerequisites

- A Power Platform with Dataverse environment setup with MCP via connector as described in [Connect to Dataverse with model context protocol (preview)](data-platform-mcp.md).
- Power Platform administrator role in order to manage environment group and connector policies.
- The steps described in this article require that the environment be a Managed Environment.

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
