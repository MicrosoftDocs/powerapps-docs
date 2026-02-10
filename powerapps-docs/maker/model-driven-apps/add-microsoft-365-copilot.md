---
title: Add Microsoft 365 Copilot chat for app users in model-driven apps (preview)
description: Learn how to enable Microsoft 365 Copilot chat in model-driven apps to provide AI-powered insights and enhance productivity for your app users.
author: Mattp123
ms.service: powerapps
ms.subservice: mda-maker
ms.author: yogupt
ms.reviewer: matp
ms.date: 02/06/2026
ms.update-cycle: 180-days
ms.topic: how-to
applies_to: 
  - "powerapps"
search.audienceType: 
  - maker
contributors:
  - makolomi
  - marianaraujo
ms.collection: bap-ai-copilot
---

# Add Microsoft 365 Copilot chat for app users in model-driven apps (preview)

[This article is prerelease documentation and is subject to change.]

Microsoft 365 Copilot chat makes it easier for users to work with model-driven apps by offering AI-powered insights through natural language conversations. With this feature, users can quickly find information, navigate apps more easily, and get help to boost their productivity.
App makers can enable Microsoft 365 Copilot chat to give users access to conversational AI that understands app data and provides helpful, contextual answers. Users can ask questions about their Microsoft Dataverse table data in plain language and receive immediate, relevant responses.

This article shows you how to enable and configure Microsoft 365 Copilot chat for your model-driven apps, both at the environment level and for individual apps.

When enabled, users can open Microsoft 365 Copilot chat in their model-driven app by selecting **Copilot** > **Chat** on the upper-right corner. For more information, see [Use Microsoft 365 Copilot chat in model-driven apps](../../user/use-microsoft-365-copilot-model-driven-apps.md).

:::image type="content" source="media/microsoft-365-chat-model-driven-apps/copilot-chat-in-model-driven-apps.png" alt-text="Screenshot of Microsoft 365 Copilot chat in a model-driven app":::

> [!IMPORTANT]
>
> - This feature is in preview.  
> - Preview features aren't meant for production use and might have restricted functionality These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.

## Prerequisites

- To use Microsoft 365 Copilot chat with Power Apps, Dataverse Search must be set to **Default** or **On** for the environment. More information: [Know what this means for generative AI experiences](/power-platform/admin/configure-relevance-search-organization#what-dataverse-search-means-for-generative-ai-enabled-experiences)

> NOTE!
>
> Microsoft 365 Copilot chat for model‑driven apps relies on Dataverse Search indexes. Enabling this feature might increase your environment’s Dataverse capacity consumption. More information: [What actions can makers or admins take to manage Dataverse Search efficiently?](/power-apps/user/relevance-search-benefits?branch=main&branchFallbackFrom=pr-en-us-11552#what-actions-can-makers-or-admins-take-to-manage-dataverse-search-efficiently)
>
> Sufficient Dataverse database capacity must be available to support indexing, semantic search, and Copilot operations. More information [Capacity page details](/power-platform/admin/capacity-storage#capacity-page-details)

## Enable Microsoft 365 Copilot for your environment

To manage Microsoft 365 Copilot Chat for model-driven apps, start by learning [how to manage Microsoft 365 Copilot Chat](/copilot/manage).

Power Platform administrators can set up and configure the Microsoft 365 Copilot chat feature for users in their environment. 

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).

1. In the navigation pane, go to **Copilot** > **Settings**. Under **Power Apps**, expand **Chat Agent** and choose **M365 Copilot Chat**.

    :::image type="content" source="media/microsoft-365-chat-model-driven-apps/enable-chat-in-admin-center.png" alt-text="Screenshot of admin setting to enable Microsoft 365 Copilot Chat for model-driven apps":::

1. Select an environment group or an environment name, then select **Edit Setting**.

1. Select **On** and then select **Save** to enable Microsoft 365 Copilot chat for your model-driven apps in the selected environment group or environment.

## Enable Microsoft 365 Copilot chat in a model-driven app

Makers can enable or disable Microsoft 365 Copilot chat for a specific model-driven app.

1. Sign in to [Power Apps](https://make.powerapps.com).
1. Open a model-driven app for editing.
1. Select **Settings** in the command bar.
1. On the left, select **Upcoming**.
1. To enable Microsoft 365 Copilot chat, set **M365 Copilot in model-driven apps** to **On**. To disable it, set the option to **Off**.

    :::image type="content" source="media/microsoft-365-chat-model-driven-apps/microsoft-365-copilot-app-setting.png" alt-text="Screenshot that shows how to turn Microsoft 365 Copilot chat on or off in a model-driven app.":::

1. Select **Save** and then publish the app for the changes to take effect.

## Microsoft 365 Copilot chat vs. Copilot chat

 Microsoft 365 Copilot chat is gradually replacing [Copilot chat in model-driven apps](add-ai-copilot.md).

During the transition period, makers can enable either one or both chat experiences. When both options are available, the **Copilot** dropdown menu shows the following options:

- **Chat** button opens [Microsoft 365 Copilot chat](../../user/use-microsoft-365-copilot-model-driven-apps.md)
- **App Skills** button opens [Copilot chat in model-driven apps](../../user/use-copilot-model-driven-apps.md).

    :::image type="content" source="media/microsoft-365-chat-model-driven-apps/both-chat-experiences.png" alt-text="Screenshot show both chat experiences in a model-driven app":::

### Known limitations

- Microsoft 365 Copilot for model-driven apps allows users to view Dataverse data by using read-only operations. This capability means that users can only view data that matches their queries and can't make any changes. To make changes, customization with an agent is required.
- Creating, updating, or performing other actions isn't supported unless you customize with an agent.
- Microsoft 365 Copilot for model-driven apps isn't available in the Power Apps mobile app.
- As this feature is being gradually deployed, certain settings in the Power Platform Admin Center might not be accessible yet, depending on the geographic location of your tenant.

## Related information

- [Customize Microsoft 365 Copilot chat with an agent (preview)](customize-microsoft-365-copilot-chat.md)
- [Use Microsoft 365 Copilot chat in model-driven apps](../../user/use-microsoft-365-copilot-model-driven-apps.md)
