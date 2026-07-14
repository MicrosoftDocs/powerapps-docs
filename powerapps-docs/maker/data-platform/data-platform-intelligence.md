---
title: "What is Dataverse intelligence?" 
description: Learn how to use Microsoft Dataverse intelligence to bring business data understanding to AI agents and Copilot.
ms.date: 06/03/2026
ms.reviewer: matp
ms.topic: how-to
author: prithvi-khosla
ms.subservice: dataverse-maker
ms.author: pkhosla
ms.contributors: paulliew
ms.service: powerapps
search.audienceType: 
  - maker
---
# What is Dataverse intelligence? (preview)

[!INCLUDE [preview-banner](../../../shared/preview-includes/preview-banner.md)]

Microsoft Dataverse intelligence brings business data understanding to AI agents and Microsoft Copilot. Work IQ helps agents understand work artifacts like files, meetings, and messages. Dataverse intelligence builds on this foundation by enabling agents to understand and act on your business data.

With Dataverse intelligence, you can define reusable business context that agents use to understand what your data means, follow your organization's processes when taking actions, and read and update Dataverse records reliably. This business context is shared across agents, so you define it once and use it everywhere.

[!INCLUDE [cc-preview-features-definition](../../../shared/preview-includes/preview-note-pp.md)]

## Dataverse data in Microsoft 365 Copilot

Microsoft 365 Copilot can use Dataverse data to help users find information and take action with natural language across Microsoft 365 experiences.

Dataverse table data from Power Apps (model-driven) can be searched and reasoned over in Microsoft 365 Copilot. Copilot can find relevant rows and related records, interpret table relationships, and summarize or answer questions based on your data. More information: [Dataverse data in Microsoft 365 Copilot](data-platform-data-copilot.md)

### Dataverse data in Microsoft 365 Copilot prerequisites

- Enable your tenant to allow Dataverse data in Microsoft 365 Copilot.
  > Microsoft 365 admin role (AI administrator or Global administrator) to access Microsoft 365 admin center Copilot settings. More information: [Enable Microsoft 365 admin center Copilot Dataverse settings](#enable-microsoft-365-admin-center-copilot-dataverse-settings)
- Enable the Environment Copilot settings to allow users to use copilot.
  > Power Platform administrator role to access Copilot environment settings. More information: [Enable Copilot](/power-platform/admin/settings-features#copilot-preview).
- Enable Dataverse search to provide index for Microsoft 365 Copilot responses.
  > Power Platform administrator role to access Dataverse Search environment settings. More information: [Enable Dataverse search:Turn on search indexing to support Dataverse intelligence (Work IQ) in AI and agent experiences](/power-platform/admin/settings-features#search).
- Enable the **Allow data availability in M365 Copilot**
  > Power Platform administrator role to access Dataverse intelligence environment settings. More information: [Enable Dataverse intelligence: Allow data availability in Microsoft 365 Copilot](/power-platform/admin/settings-features#dataverse-intelligence-preview).
- Enable **Search for records in Microsoft 365 apps**
   > Power Platform administrator role to access Search for records in Microsoft 365 apps environment settings. More information: [Enable Search for records in Microsoft 365 apps](/power-platform/admin/settings-features#search).
- Enable the Power Apps application settings to allow searching for tables related to the application.
  > Power Platform administrator role to access the Power Apps application settings. More information: [Enable Microsoft 365 Copilot in a model-driven app](/power-apps/maker/model-driven-apps/add-microsoft-365-copilot#enable-microsoft-365-copilot-in-a-model-driven-app).

#### Enable Microsoft 365 admin center Copilot Dataverse settings

1. Go to [Microsoft 365 admin center](https://admin.cloud.microsoft/?#/homepage). Select **Copilot** >**Settings**.
1. Locate and select **Dataverse data available in Microsoft 365 Copilot**.
1. Select **All users**, or
1. Select **Specific groups** and enter the list of Entra security groups. 
1. Select **Save** to save the setting changes.

## Business skills

Business skills help makers and users interpret data, improve processes, and make decisions. Intelligence experiences can support key skills like problem framing, requirements discovery, communicating insights, and iterating with stakeholders. More information: [Business skills overview](data-platform-business-skill-overview.md)

### Business skills prerequisites

- The environment must be enabled and configured for Dataverse MCP server. More information: [Configure the Dataverse MCP server for an environment](data-platform-mcp-disable.md)

## Next steps

[Dataverse data in Microsoft 365 Copilot](data-platform-data-copilot.md)

[Business skills overview](data-platform-business-skill-overview.md)

[Create and use business skills](data-platform-business-skills.md)
