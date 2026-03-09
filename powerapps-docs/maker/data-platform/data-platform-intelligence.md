---
title: "What is Dataverse intelligence?" 
description: Learn how to use Microsoft Dataverse intelligence to bring business data understanding to AI agents and Copilot.
ms.date: 03/06/2026
ms.reviewer: matp
ms.topic: how-to
author: prithvi-khosla
ms.subservice: dataverse-maker
ms.author: pkhosla
ms.service: powerapps
search.audienceType: 
  - maker
---
# What is Dataverse intelligence?

[!INCLUDE [preview-banner](../../../shared/preview-includes/preview-banner.md)]

Microsoft Dataverse intelligence extends Work IQ to bring business data understanding to AI agents and Microsoft Copilot. Work IQ helps agents understand work artifacts like files, meetings, and messages. Dataverse intelligence builds on this foundation by enabling agents to understand and act on your business data.

With Dataverse intelligence, you can define reusable business context that agents use to understand what your data means, follow your organization's processes when taking actions, and read and update Dataverse records reliably. This business context is shared across agents, so you define it once and use it everywhere.

[!INCLUDE [cc-preview-features-definition](../../../shared/preview-includes/preview-note-pp.md)]

## Prerequistes

- Power Platform administrator role to access Dataverse intelligence environment settings. 
- The environment where you use Dataverse intelligence must be a Managed Environment.
- The environment must be enabled and configured for Dataverse MCP server preview. Business skills are only available for use with the preview version of Dataverse MCP server. More information: [Use preview tools and upcoming features in Dataverse MCP server](data-platform-mcp-preview-tools.md)   

## Enable Dataverse intelligence

To enable Dataverse intelligence, you need the following requirements:

- Power Platform administrator role to access Dataverse intelligence environment settings.
- To use this feature, the environment must be a [Managed Environment](/power-platform/admin/managed-environment-overview).

1. Go to [Power Platform admin center](https://admin.powerplatform.microsoft.com/). Select **Manage** >**Environments**.
1. Open the environment where you want to turn on the Dataverse MCP server, and then select **Settings** > **Product** > **Features**.  
1. Scroll down to locate **Dataverse intelligence**.  
1. Turn on **Enable Dataverse intelligence (Work IQ) for agents and AI experiences**. 
1. Make sure **Allow MCP clients to interact with Dataverse MCP server (Preview version)** is enabled. If it's not, enable it. 
1. Select **Save** to save the setting changes.

## Next steps

[Business skills overview](data-platform-business-skill-overview.md)

[Create and use business skills](data-platform-business-skills.md)