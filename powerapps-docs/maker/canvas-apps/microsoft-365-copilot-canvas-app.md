---
title: Add Microsoft 365 Copilot chat for app users in canvas apps (preview)
description: Learn how to enable Microsoft 365 Copilot chat in canvas apps to provide AI-powered insights and enhance productivity for your app users.
author: mduelae
ms.service: powerapps
ms.subservice: canvas-maker
ms.author: marcsc
ms.reviewer: mkaur
ms.date: 04/22/2026
ms.update-cycle: 180-days
ms.topic: how-to
applies_to: 
  - "powerapps"
search.audienceType: 
  - maker
contributors:
  - marcsc
  - mkaur
ms.collection: bap-ai-copilot
---

# Add Microsoft 365 Copilot for app users in canvas apps (preview)

[This article is prerelease documentation and is subject to change.]

Microsoft 365 Copilot makes it easier for users to work with canvas apps by offering AI-powered insights through natural language conversations. By using this feature, users can quickly find information, navigate apps more easily, and get help to boost their productivity.
App makers can enable Microsoft 365 Copilot to give users access to conversational AI that understands app data and provides helpful, contextual answers. Users can ask questions about their Microsoft Dataverse table or SharePoint list data in plain language and receive immediate, relevant responses.

This article shows you how to enable and configure Microsoft 365 Copilot for your canvas apps, both at the environment level and for individual apps.

When enabled, users can open Microsoft 365 Copilot in their canvas app by selecting **Copilot** on the upper-right corner. For more information, see [Use Microsoft 365 Copilot in canvas apps](../../user/use-microsoft-365-copilot-canvas-apps.md).

:::image type="content" source="../../user/media/microsoft-365-copilot-button-canvas.png" alt-text="Screenshot of Microsoft 365 Copilot in the canvas app":::

> [!IMPORTANT]
>
> - This feature is in preview.  
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520). They're available before an official release so that customers can get early access and provide feedback.
> -  This feature is in the process of rolling out and might not be available in your region yet.

## Prerequisites

To use Microsoft 365 Copilot in canvas apps, make sure the following prerequisites are met:

- You must have access to an [early release cycle environment](/power-platform/admin/early-release) to use this feature.
- Your tenant must be set to allow **Dataverse data available in Microsoft 365 Copilot**. For more information, see [Enable Microsoft 365 admin center Copilot Dataverse settings](../data-platform/data-platform-intelligence.md#enable-microsoft-365-admin-center-copilot-dataverse-settings).
- Dataverse Search must be set to **Default** or **On** for the environment. For more information, see [Understand what this means for generative AI experiences](/power-platform/admin/configure-relevance-search-organization#what-dataverse-search-means-for-generative-ai-enabled-experiences).
- To use the Microsoft 365 Copilot feature in your app, users must have a Microsoft 365 Copilot license.

> [!NOTE]
>
> - Microsoft 365 Copilot for canvas apps with Dataverse relies on Dataverse Search indexes. Enabling this feature might increase your environment’s Dataverse capacity consumption. For more information, see [What actions can makers or admins take to manage Dataverse Search efficiently](../../user/relevance-search-benefits.md#what-actions-can-makers-or-admins-take-to-manage-dataverse-search-efficiently).
> - Sufficient Dataverse database capacity must be available to support indexing, semantic search, and Copilot operations. For more information, see [Capacity page details](/power-platform/admin/capacity-storage#capacity-page-details).

## Enable Microsoft 365 Copilot for your environment

To manage Microsoft 365 Copilot for canvas apps, start by learning [how to manage Microsoft 365 Copilot](/copilot/manage).

Power Platform administrators can set up and configure the Microsoft 365 Copilot feature for users in their environment.

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).

1. In the navigation pane, go to **Copilot** > **Settings**. Under **Power Apps**, expand **Chat Agent** and choose **M365 Copilot**.

1. Select an environment group or an environment name, and then select **Edit Setting**.

1. Select **On** and then select **Save** to enable Microsoft 365 Copilot for your canvas apps in the selected environment group or environment.

## Enable Microsoft 365 Copilot in a canvas app

Makers can enable or disable Microsoft 365 Copilot for a specific canvas app.

1. Sign in to [Power Apps](https://make.powerapps.com).
1. Open a canvas app for editing.
1. Select **Settings** in the command bar.
1. On the left, select **General**.
1. To enable Microsoft 365 Copilot, set **M365 Copilot in canvas apps (Preview)** to **On**. To disable it, set the option to **Off**.

    :::image type="content" source="media/microsoft-365-canvas-apps/microsoft-365-copilot-app-setting.png" alt-text="Screenshot that shows how to turn Microsoft 365 Copilot on or off in a canvas app.":::

1. Select **Save** and then publish the app for the changes to take effect.

## Microsoft 365 Copilot vs. Copilot chat

 Microsoft 365 Copilot is replacing [Copilot chat in canvas apps](add-ai-copilot.md).

### Known limitations

- Agents you author can't yet use in‑app user context to optimize their responses.
- M365 Copilot in canvas apps supports apps that use either SharePoint or Dataverse as a data source but not both within the same app.
- During the initial preview phase, for SharePoint, only applications containing a single SharePoint list will return answers to questions.
- If your canvas app connects to a SharePoint list through an environment variable, Microsoft 365 Copilot won't reference data from that SharePoint list.
- Microsoft 365 Copilot for canvas apps allows users to view data by using read-only operations. This capability means that users can only view data that matches their queries and can't make any changes. To make changes, customization with an agent is required.
- Microsoft 365 Copilot for canvas apps isn't available in the Power Apps mobile app.
- As this feature is being gradually deployed, certain settings in the Power Platform Admin Center might not be accessible yet, depending on the geographic location of your tenant.

## Related information

- [Customize Microsoft 365 Copilot with an agent](../model-driven-apps/customize-microsoft-365-copilot-chat.md)
- [Use Microsoft 365 Copilot in canvas apps](../../user/use-microsoft-365-copilot-canvas-apps.md)
