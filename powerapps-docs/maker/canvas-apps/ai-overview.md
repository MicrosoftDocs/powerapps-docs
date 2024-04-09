---
title: AI Copilot overview
description: AI Copilot overview in Power Apps.
author: mduelae
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 02/07/2024
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType: 
  - maker
ms.collection: 
    - bap-ai-copilot
    - get started
contributors:
  - mduelae
---

# AI Copilot overview

[This article is prerelease documentation and is subject to change.]

Bringing the power of AI Copilot to both app makers and their end-users in Power Apps. With Copilot you can build an app, including the data behind it, just by describing what you need through multiple steps of conversation. Your apps will have copilot-powered experiences built in from the first screen&mdash;so your users can discover insights in conversation instead of mouse-clicks.

To learn how to use the new AI features in Power Apps, see:

- [Build apps through conversation](ai-conversations-create-app.md)
- [Continue editing your app with Copilot (preview)](ai-edit-app.md)
- [Add Chatbot control to a canvas app (preview)](add-ai-chatbot.md)
- [Add Copilot control to a canvas app (preview)](add-ai-copilot.md)
- [Leverage Azure OpenAI Service in AI Builder (preview)](/ai-builder/prebuilt-azure-openai)
- [Use Copilot to work with Formulas in the Formula Bar](ai-formulas-formulabar.md)

> [!IMPORTANT]
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - For more information, go to the [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability is in the process of rolling out, and may not be available in your region yet.
> - This capability may be subject to usage limits or capacity throttling.
> - To understand capabilities and limitations of AI-powered and Copilot features in Power Apps, see [FAQ about using AI responsibly in Power Apps](../common/transparency-note.md)

## Prerequisites for the AI features in Power Apps

- Have a [Microsoft Dataverse database](/power-platform/admin/create-database) in your environment.  

- AI Builder must be enabled for your environment to use the AI models or controls leveraging AI models:

    1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).

    2. In the admin center, go to **Environments** &gt; *\[select an environment\]* &gt; **Settings** &gt; **Product** &gt; **Features**.

    3. On the **Features** settings page, under **AI Builder**, enable or disable **AI Builder preview models**.

## Enable or disable Copilot (preview) in Power Apps

[Generally available](/power-platform/admin/general-availability-deployment) Copilot features are enabled by default and cannot be turned off. To disable them, a tenant admin must [contact support](/power-platform/admin/get-help-support).

Copilot features in preview are also enabled by default, but can be disabled by an administrator.

Follow these steps to disable **Copilot** (preview) in Power Apps for your tenant.

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).
2. Select **Settings** > **Tenant settings** in the left-side navigation pane.
3. Select **Copilot (preview)** > set the toggle to **Off** > **Save**.

> [!NOTE]
> Turning off Copilot for your tenant will only disable Copilot for makers. It won't disable [Copilot control for canvas apps](add-ai-copilot.md) or [Copilot for model-driven apps](../model-driven-apps/add-ai-copilot.md).

Follow these steps to enable or disable **Copilot** preview features for your environment.

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).
2. In the left-side navigation pane **Environment**.
3. Select the environment and on the command bar, select **Settings**.
4. Select one of the following options:
   - To turn it on, set the toggle to **On** for **Copilot**.
   - To turn it off, set the toggle to **Off** for **Copilot**.


## See also

- [FAQ about using AI responsibly in Power Apps](../common/transparency-note.md)
- [Language availability for Power Platform](https://dynamics.microsoft.com/availability-reports/languagereport/)
- [Geographical availability for Power Platform](https://dynamics.microsoft.com/availability-reports/georeport/)
  
