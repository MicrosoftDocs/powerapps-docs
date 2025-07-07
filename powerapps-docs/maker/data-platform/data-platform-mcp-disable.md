---
title: Disable a Dataverse model context protocol (MCP) server
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
# Disable a Dataverse MCP server using advanced connector policies

Dataverse model context protocol (MCP) is provided through the connector infrastructure. While the Dataverse connector itself is a non-blockable connector—meaning you can't disable it using traditional data Loss prevention (DLP) settings within the Power Platform admin cnter—you can selectively disable the Dataverse MCP server by leveraging advanced connector policies.

## Prerequisites

- <!-- A Dataverse environment that has been enabled as an MCP server. -->
- Access to the Power Platform admin center
- Appropriate permissions to manage environment groups and connector policies

## Disable a Dataverse a model context protocol

1. Go to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/), select **Manage**, and then select **Environment groups**. 
1. Select **New group** to create a new environment group or select an existing group where you want to turn off the Dataverse MCP server.
1. Open the environment group, and then on the **Rules** tab select **Advanced connector policies (preview)**.
1. Select the **Microsoft Dataverse** connector, and then select **Edit actions**.
1. Locate the action named **Dataverse MCP Server**, and turn **Off** this action as needed for your environment group.
1. Select **Save** and then select **Publish rules** to the enable the rule.

## Related articles

[Connect to Dataverse with model context protocol (preview)](data-platform-mcp.md)

[Connect to Dataverse with model context protocol FAQ (preview)](data-platform-mcp-faq.md)