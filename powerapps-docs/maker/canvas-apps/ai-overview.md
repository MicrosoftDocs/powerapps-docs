---
title: Copilot in Power Apps overview (preview)
description: Learn how to use AI to build apps by describing what you want them to do with Copilot in Power Apps.
author: mduelae
ms.topic: conceptual
ms.custom: 
 - canvas
 - copilot-learning-hub
ms.reviewer: 
ms.date: 08/08/2024
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType: 
  - maker
ms.collection: 
    - bap-ai-copilot
    - get started
contributors:
  - mduelae
  - Mattp123
---

# Copilot in Power Apps overview (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Bringing the power of Copilot to both app makers and their end-users in Power Apps. With Copilot you can build an app, including the data behind it, just by describing what you need through multiple steps of conversation. Your apps have copilot-powered experiences built in from the first screen&mdash;so your users can discover insights in conversation instead of mouse-clicks.

Learn how to use Copilot features in Power Apps.

## Canvas apps

- [Build apps through conversation](ai-conversations-create-app.md)
- [Continue editing your app with Copilot (preview)](ai-edit-app.md)
- [Add a Chatbot control to a canvas app (preview)](add-ai-chatbot.md)
- [Add a Copilot control to a canvas app (preview)](add-ai-copilot.md)
- [Add a custom Copilot to a canvas app (preview)](add-custom-copilot.md)
- [Leverage Azure OpenAI Service in AI Builder (preview)](/ai-builder/prebuilt-azure-openai)
- [Create Power Fx formulas with Copilot](ai-formulas-formulabar.md)
- [Use field suggestions by Copilot](ai-field-suggestions.md)

## Model-driven apps

- [Add the Copilot control to the rich text editor](../model-driven-apps/copilot-control.md)
- [Use Copilot in the email rich text editor](../model-driven-apps/use-copilot-email-assist.md)
- [Add copilot for app users in model-driven apps](../model-driven-apps/add-ai-copilot.md)

## App users

- [Filter, sort, and search galleries with Copilot (preview)](../../user/smartgrid.md)
- [Draft well-written input text with Copilot (preview)](../../user/well-written-input-text-copilot.md)

## Microsoft Dataverse

- [Add Dataverse tables in Microsoft Copilot Studio as a knowledge source](/microsoft-copilot-studio/knowledge-add-existing-copilot#dataverse)

> [!IMPORTANT]
>
> - Preview features aren't meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - For more information, go to the [preview terms](https://go.microsoft.com/fwlink/?linkid=2173149).
> - This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability is in the process of rolling out, and may not be available in your region yet.
> - This capability may be subject to usage limits or capacity throttling.
> - To understand capabilities and limitations of AI-powered and Copilot features in Power Apps, see [FAQ about using AI responsibly in Power Apps](../common/transparency-note.md)

## Prerequisites for the Copilot features in Power Apps

- To use Copilot in Power Apps, your administrator must turn on Copilot features.
- For Copilot availability in your region, refer to [Release Planner Availability Reports](https://releaseplans.microsoft.com/en-US/availability-reports/?report=copilotfeaturereport).
- Some Copilot features are already generally available and are turned on by default. Learn more in [Enable or disable Copilot (preview) in Power Apps](ai-overview.md#enable-or-disable-copilot-preview-in-power-apps).
- Each Copilot feature might have different requirements. Refer to the specific documentation for each feature for detailed information.

## Enable or disable Copilot (preview) in Power Apps

[Generally available](/power-platform/admin/general-availability-deployment) Copilot features are enabled by default and can't be turned off. To disable them, a tenant admin must [contact support](/power-platform/admin/get-help-support).

**Copilot** (preview) features are also enabled by default, but your administrator can disable them.

Follow these steps to disable **Copilot** (preview) in Power Apps for your tenant.

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).
2. Select **Settings** > **Tenant settings** in the left-side navigation pane.
3. Select **Copilot (preview)**, turn the toggle **Off**, and then select **Save**.

> [!NOTE]
> Turning off Copilot for your tenant will only disable Copilot for makers. It won't disable [Copilot control for canvas apps](add-ai-copilot.md) or [Copilot for model-driven apps](../model-driven-apps/add-ai-copilot.md).

Follow these steps to enable or disable **Copilot** preview features for your environment.

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).
2. In the left-side navigation pane, select **Environments**.
3. Select the environment, and on the command bar, select **Settings**.
4. Set the **Copilot** toggle to **On** or **Off**.

## Related information

- [FAQ about using AI responsibly in Power Apps](../common/transparency-note.md)
- [Language availability for Power Platform](https://dynamics.microsoft.com/availability-reports/languagereport/)
- [Geographical availability for Power Platform](https://dynamics.microsoft.com/availability-reports/georeport/)
