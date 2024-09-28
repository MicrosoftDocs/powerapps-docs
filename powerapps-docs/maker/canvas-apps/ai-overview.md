---
title: Copilot in Power Apps overview (preview)
description: Learn how Copilot in Power Apps makes it easy to build apps and provide insights to your users by describing what you need in natural language.
author: mduelae
ms.author: tapanm
ms.topic: conceptual
ms.custom: 
  - canvas
  - ai-gen-docs-bap
  - ai-gen-title
  - ai-gen-desc
  - ai-seo-date: 07/16/2024
ai-usage: ai-assisted
ms.reviewer: 
ms.date: 06/11/2024
ms.subservice: canvas-maker
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

Copilot in Power Apps is a new way to create apps that understand natural language. You can build an app, including the data behind it, by having a conversation with Copilot. You don't need to write any code or design any screens. Copilot generates the app for you based on your description.

But that's not all. Your app also gets a built-in Copilot experience for your users. They can ask questions or give commands to the app, and Copilot responds with relevant insights or actions, all in natural language, making your app more engaging and intuitive for your users.

In this article, you'll find resources to help you learn how to use Copilot features in Power Apps.

## Copilot in canvas apps

- [Build apps through conversation](ai-conversations-create-app.md)
- [Continue editing your app with Copilot (preview)](ai-edit-app.md)
- [Add a Copilot control to a canvas app (preview)](add-ai-copilot.md)
- [Leverage Azure OpenAI Service in AI Builder (preview)](/ai-builder/prebuilt-azure-openai)
- [Create Power Fx formulas with Copilot](ai-formulas-formulabar.md)
- [Use field suggestions by Copilot](ai-field-suggestions.md)

## Copilot in model-driven apps

- [Add the Copilot control to the rich text editor](../model-driven-apps/copilot-control.md)
- [Use Copilot in the email rich text editor](../model-driven-apps/use-copilot-email-assist.md)
- [Add Copilot for app users in model-driven apps](../model-driven-apps/add-ai-copilot.md)

## Copilot for app users

- [Filter, sort, and search galleries with Copilot (preview)](../../user/smartgrid.md)
- [Draft well-written input text with Copilot (preview)](../../user/well-written-input-text-copilot.md)

## Microsoft Dataverse

- [Add Dataverse tables in Microsoft Copilot Studio as a knowledge source](/microsoft-copilot-studio/knowledge-add-existing-copilot#dataverse)

> [!IMPORTANT]
>
> - Preview features aren't meant for production use and might have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback. Learn more in [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability is in the process of rolling out, and might not be available in your region yet. Learn more in [Explore Copilot features by geography and languages](https://releaseplans.microsoft.com/en-US/availability-reports/?report=copilotfeaturereport).
> - This capability may be subject to usage limits or capacity throttling.
> - You should understand the capabilities and limitations of AI-powered and Copilot features in Power Apps. Learn more in [FAQ about using AI responsibly in Power Apps](../common/transparency-note.md)

## Prerequisites

- To use Copilot in Power Apps, your administrator must turn on Copilot features.
- Some Copilot features are already generally available and are turned on by default. Learn more in [Enable or disable Copilot in Power Apps](ai-overview.md#enable-or-disable-copilot-in-power-apps).
- Each Copilot feature might have different requirements. Refer to the specific documentation for each feature for detailed information.

## Enable or disable Copilot in Power Apps

[Generally available](/power-platform/admin/general-availability-deployment) Copilot features are enabled by default and can't be turned off except by Microsoft Support. To disable them, a tenant admin must [contact Support](/power-platform/admin/get-help-support).

Preview Copilot features are also enabled by default, but your admin can turn them off for your tenant or for an environment.

### Disable Copilot for your tenant

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).
1. In the navigation pane, select **Settings** > **Tenant settings**.
1. Select **Copilot (preview)**, and then set the toggle to **Off**.
1. Select **Save**.

> [!NOTE]
> Turning off Copilot for your tenant disables Copilot for makers only. It doesn't disable the [Copilot control for canvas apps](add-ai-copilot.md) or [Copilot for model-driven apps](../model-driven-apps/add-ai-copilot.md).

### Disable Copilot for an environment

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).
2. In the navigation pane, select **Environments**.
3. Select the environment, and then in the command bar, select **Settings**.
4. Set the **Copilot** toggle to **On** or **Off**.

## Related information

- [FAQ about using AI responsibly in Power Apps](../common/transparency-note.md)
- [Language availability for Power Platform](https://dynamics.microsoft.com/availability-reports/languagereport/)
- [Geographical availability for Power Platform](https://dynamics.microsoft.com/availability-reports/georeport/)
