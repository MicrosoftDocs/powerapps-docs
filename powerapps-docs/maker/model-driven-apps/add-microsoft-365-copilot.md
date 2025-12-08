---
title: Add Microsoft 365 Copilot chat for app users in model-driven apps (preview)
description: Learn how to enable Microsoft 365 Copilot chat in model-driven apps to provide AI-powered insights and enhance productivity for your app users.
author: Mattp123
ms.service: powerapps
ms.subservice: mda-maker
ms.author: yogupt
ms.reviewer: matp
ms.date: 12/08/2025
ms.update-cycle: 180-days
ms.topic: how-to
applies_to: 
  - "powerapps"
search.audienceType: 
  - maker
contributors:
  - makolomi
ms.collection: bap-ai-copilot
---

# Add Microsoft 365 Copilot for app users in model-driven apps (preview)

[This article is prerelease documentation and is subject to change.]

Microsoft 365 Copilot chat makes it easier for users to work with model-driven apps by offering AI-powered insights through natural language conversations. With this feature, users can quickly find information, navigate apps more easily, and get help to boost their productivity.
App makers can enable Microsoft 365 Copilot chat to give users access to conversational AI that understands app data and provides helpful, contextual answers. Users can ask questions about their Microsoft Dataverse table data in plain language and receive immediate, relevant responses.

This article shows you how to enable and configure Microsoft 365 Copilot chat for your model-driven apps, both at the environment level and for individual apps.

When enabled, users can open Microsoft 365 Copilot chat in their model-driven app by selecting **Copilot** > **Chat** on the upper-right corner.


:::image type="content" source="media/microsoft-365-chat-model-driven-apps/copilot-chat-in-model-driven-apps.png" alt-text="Screenshot of Microsoft 365 Copilot chat in a model-driven app":::

For more information, see [Use Microsoft 365 Copilot chat in model-driven apps](../../user/use-microsoft-365-copilot-model-driven-apps.md).

> [!IMPORTANT]
>
> This feature is in preview.  
>
> - Preview features aren't meant for production use and might have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).


## Prerequisites

- You must have or create an [Early release cycle environment](/power-platform/admin/early-release) to use this feature.

> [!NOTE]
>
> - Microsoft 365 Copilot Chat is gradually replacing [Copilot chat in model-driven apps](../../user/use-copilot-model-driven-apps.md). During this transition, app makers can decide which chat experience is available to users. Makers can enable Microsoft 365 Copilot Chat, Copilot chat, or both, depending on their needs. 
> - If both Microsoft 365 Copilot Chat and [Copilot chat in model-driven apps](../../user/use-copilot-model-driven-apps.md) are enabled, users can access and try each option. The **Chat** button opens Microsoft 365 Copilot Chat, and the **App Skills** button opens Copilot chat in model-driven apps. :::image type="content" source="media/microsoft-365-chat-model-driven-apps/both-chat-experiences.png" alt-text="Screenshot show both chat experiences in a model-driven app":::


## Enable Microsoft 365 Copilot for model-driven apps in your environment

To manage Microsoft 365 Copilot Chat for model-driven apps, start by learning [how to manage Microsoft 365 Copilot Chat](/copilot/manage).

Power Platform administrators can set up and configure the Microsoft 365 Copilot chat feature for users in their environment. 

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).

1. In the navigation pane, go to **Copilot** > **Settings**. Under **Power Apps**, expand **Chat Agent** and choose **M365 Copilot Chat**.

:::image type="content" source="media/microsoft-365-chat-model-driven-apps/enable-chat-in-admin-center.png" alt-text="Screenshot of admin setting to enable Microsoft 365 Copilot Chat for model-driven apps":::

1. Select an environment group or an environment name, and then select **Edit Setting**.

1. Select **On** and then select **Save** to enable Microsoft 365 Copilot chat for your model-driven apps in the selected environment group or environment.


## Enable Microsoft 365 Copilot chat for a model-driven app

Makers can enable or disable Microsoft 365 Copilot chat for a specific model-driven app.

1. Sign in to [Power Apps](https://make.powerapps.com).
1. Open a model-driven app for editing.
1. Select **Settings** in the command bar.
1. Select **Upcoming** on the Settings screen.
1. To enable Microsoft 365 Copilot chat set **M365 Copilot in model-driven apps** to  **On**. Or, to set it to **Off** to disable it.

    :::image type="content" source="media/microsoft-365-chat-model-driven-apps/microsoft-365-copilot-app-setting.png" alt-text="Screenshot that shows how to turn Microsoft 365 Copilot chat on or off in a model-driven app.":::

1. Select **Save** and then publish the app for the changes to take effect.

### Known limitations

1. Microsoft 365 Copilot for model-driven apps allows users to view Dataverse data using read-only operations. This capability means that users can only view data that matches their queries and can't make any changes. To make changes, customization with an agent is required.
1. Creating, updating, or performing other actions isn't supported unless you customize with an agent.
1. Microsoft 365 Copilot for model-driven apps isn't available in the Power Apps mobile app.


## Related information

- [Customize Microsoft 365 Copilot chat in model-driven apps](../model-driven-apps/microsoft-365-customize-copilot-chat.md)
- [Use Microsoft 365 Copilot chat in model-driven apps](../../user/use-microsoft-365-copilot-model-driven-apps.md)
