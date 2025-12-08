---
title: Add Microsoft 365 Copilot chat for app users in model-driven apps
description: Learn how to turn on Microsoft 365 Copilot chat in model-driven apps to help app users get AI-powered insights about their data.
author: Mattp123
ms.service: powerapps
ms.subservice: mda-maker
ms.author: yogupt
ms.reviewer: matp
ms.date: 05/29/2025
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

# Add Microsoft 365 Copilot for app users in model-driven apps

Microsoft 365 Copilot chat for model-driven apps is a next-generation AI assistant that helps app users get insights about the data in their apps through conversation in natural language. Microsoft 365 Copilot chat helps app users boost their productivity through AI-powered insights and intuitive app navigation.

> [!IMPORTANT]
>
> This feature is in preview.  
>
> - You must have or create an [Early release cycle environment](/power-platform/admin/early-release) to use this feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - Microsoft 365 Copilot Chat will eventually replace [Copilot chat in model-driven apps](../../user/use-copilot-model-driven-apps.md).  For a period of time, the transition from one to the other will be at the discretion of the app maker. App makers will be able to control whether an end user has one, the other, or both available to them.

When enabled, Microsoft 365 Copilot chat can be accessed through the Copilot button near the upper-right corner of the page.

:::image type="content" source="media/m365-copilot-button.png" alt-text="Screenshot of the Microsoft 365 Copilot chat pane in a model-driven app.":::

If Microsoft 365 Copilot chat and [Use Copilot chat in model-driven apps](../../user/use-copilot-model-driven-apps.md) are both enabled, users will have the option to try both. The **Chat** option represents Microsoft 365 Copilot and the **App Skills** option represents [Copilot chat in model-driven apps](../../user/use-copilot-model-driven-apps.md).  These terms are used to align with Microsoft 365 apps for consistency.

:::image type="content" source="media/copilot-chat-switcher.png" alt-text="Screenshot that shows the Copilot split button showcasing Chat and App Skills options on a page.":::

Microsoft 365 Copilot chat in model-driven apps can answer questions about the Microsoft Dataverse table data in the environment. Learn more in [Use Microsoft 365 Copilot chat in model-driven apps](../../user/use-microsoft-365-copilot-model-driven-apps.md).

## Enable Microsoft 365 Copilot for model-driven apps in your environment

Management of Microsoft 365 Copilot for model-driven apps starts with an understanding of how to [Manage Microsoft 365 Copilot Chat](/copilot/manage).

Additionally, Power Platform administrators configure the Microsoft 365 Copilot chat feature in model-driven apps for users in their environments in the [Power Platform admin center](https://admin.powerplatform.microsoft.com).

1. Sign in to the Power Platform admin center at [https://admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com).

1. In the navigation pane, go to **Copilot** > **Settings** and in the **Power Apps** section, expand **Chat Agent** and select **Microsoft 365 Copilot Chat**.
  :::image type="content" source="media/m365-copilot-ppac-setting.png" alt-text="Screenshot that shows how to find the Microsoft 365 Copilot in Power Platform Admin center.":::

1. Select either an **Environment Group** or an **Environment**, then select **Edit Setting**.
  :::image type="content" source="media/m365-copilot-ppac-group-selection.png" alt-text="Screenshot that shows how to edit the Copilot setting in Power Platform Admin center for an Environment Group or Environment.":::

1. Adjust the setting to reflect your preference, then select the **Save** button.
  :::image type="content" source="media/m365-copilot-ppac-save.png" alt-text="Screenshot that shows how to Save the Microsoft 365 Copilot setting preference.":::

## Enable Microsoft 365 Copilot chat for a model-driven app

Makers can enable or disable Microsoft 365 Copilot chat for a specific model-driven app. In app designer, open the model-driven app for **Edit**, and then select **Settings** on the command bar. Select **Upcoming** on the **Settings** screen, set **Microsoft 365 Copilot control** to **Default**, **On** or **Off**, and then select **Save**.

:::image type="content" source="media/m365-copoliot-app-setting.png" alt-text="Screenshot that shows how to turn Microsoft 365 Copilot chat on or off in a model-driven app.":::

**Save** and **Publish** the model-driven app for the changes to take effect.

### Known limitations

1. **Microsoft 365 Copilot for model-driven apps** allows users to retrieve information from Dataverse through read-only operations. This means that users can only view data that matches their queries and can't make any changes to the data unless the customize with an agent.
1. Create, update, or other generic actions saren't supported unless the customize with an agent.
1. **Microsoft 365 Copilot model-driven apps** isn't supported with the Power Apps mobile app.

## Related information

- [Customize Microsoft 365 Copilot chat in model-driven apps](../model-driven-apps/Microsoft 365-customize-copilot-chat.md)
- [Use Microsoft 365 Copilot chat in model-driven apps](../model-driven-apps/use-Microsoft 365-copilot-model-driven-apps.md)
