---
title: Copilot in Power Apps overview (preview)
description: Learn how Copilot in Microsoft Power Apps makes it easy to build apps by providing insights and actions in response to natural language requests.
author: mduelae
ms.author: tapanm
ms.topic: article
ms.custom: 
  - canvas
  - ai-gen-docs-bap
  - ai-gen-title
  - ai-gen-desc
  - ai-seo-date: 5/25/2025
ai-usage: ai-assisted
ms.reviewer: 
ms.date: 06/27/2025
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

Copilot in Power Apps helps you build apps using natural language. You can build an app with a data model behind it, by having a conversation with Copilot. You don't need to write any code or design any screens. Copilot generates the app for you based on your description of the business solution.

Users can ask questions or give commands to the app, and Copilot responds with relevant insights or actions. All questions or commands can be in natural language, making your app more engaging and intuitive for your users.

In this article, you learn how to use Copilot features in Power Apps.

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.

> [!NOTE]
>
> This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).

## Prerequisites

Each Copilot feature might have different requirements. Refer to the specific documentation for each feature in the following articles.

If you need to disable Copilot, see [Disable Copilot in Power Apps](#disable-copilot-in-power-apps).

### Availability

- This capability might not be available in your region yet. Learn more in [Explore Copilot features by geography and languages](https://releaseplans.microsoft.com/en-US/availability-reports/?report=copilotfeaturereport).
- This capability might be subject to usage limits or capacity throttling.
- Understand the capabilities and limitations of AI-powered and Copilot features in Power Apps. Learn more in [FAQ about using AI responsibly in Power Apps](../common/transparency-note.md).

## Copilot use in Power Apps

The following articles can help you build various apps in different scenarios using Copilot.

- [Create a plan using Plan designer](../plan-designer/create-plan.md)

## Copilot in canvas apps

- [Build apps through conversation](ai-conversations-create-app.md)
- [Edit your app with Copilot (preview)](ai-edit-app.md)
- [Add a Copilot control to a canvas app (preview)](add-ai-copilot.md)
- [Create Power Fx formulas with Copilot](ai-formulas-formulabar.md)
- [Use field suggestions by Copilot](ai-field-suggestions.md)
- [Add a custom Copilot to a canvas app (preview)](add-custom-copilot.md)
- [Build an agent to automate your business process (preview)](agent-builder.md)
- [Rename controls in canvas apps with Copilot (preview)](./controls/copilot-rename-controls.md)

## Copilot in model-driven apps

Model-driven apps support [AI features](../../user/ai-in-apps.md) to improve the efficiency and productivity of business processes with intelligent automation and assistance.

## Copilot feature use

- [Filter, sort, and search galleries with Copilot (preview)](../../user/smartgrid.md)
- [Draft well-written input text with Copilot (preview)](../../user/well-written-input-text-copilot.md)
- [Visualize data in a view with Copilot (preview)](../../user/visualize-data-in-copilot.md)

## Microsoft Dataverse

- [Add knowledge to an existing copilot: Dataverse](../data-platform/data-platform-copilot.md)

## Disable Copilot in Power Apps

Preview Copilot features are enabled by default, but your admin can turn them off for an environment or tenant.

> [!NOTE]
>
> [Generally available](/power-platform/admin/general-availability-deployment) Copilot features are enabled by default and can't be turned off except by Microsoft Support. To disable them, a tenant admin must [contact Support](/power-platform/admin/get-help-support).

### Disable preview Copilot for an environment

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).
1. In the navigation pane, select **Environments**, then select an environment.
1. From the command bar, select **Settings** > **Features**.
1. Set the **Copilot** toggle to **Off**.

### Disable preview Copilot for your tenant

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).
1. In the navigation pane, select **Settings** and you see the **Tenant settings** page.
1. Select **Copilot in Power Apps (preview)**, and then set the toggle to **Off**.
1. Select **Save**.

> [!NOTE]
> Turning off Copilot for your tenant disables Copilot for makers only. It doesn't disable the [Copilot control for canvas apps](add-ai-copilot.md) or [Copilot for model-driven apps](../model-driven-apps/add-ai-copilot.md).

### Related information

- [FAQ about using AI responsibly in Power Apps](../common/transparency-note.md)
- [Language availability for Power Platform](https://dynamics.microsoft.com/availability-reports/languagereport/)
- [Geographical availability for Power Platform](https://dynamics.microsoft.com/availability-reports/georeport/)
