---
title: Copilot in Power Apps overview
description: Copilot in Power Apps helps you build apps easily using natural language. Discover how to create apps faster and boost productivity. Try Copilot today!
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
ms.date: 10/1/2025
ms.update-cycle: 180-days
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

# Copilot in Power Apps overview 

Copilot in Power Apps lets you quickly build apps using natural language. Describe your business needs, and the service generates an app and data model for you—no coding required. People interact with your app by asking questions or giving commands in everyday language, making the experience more intuitive and engaging. This article gives an overview of Copilot in Power Apps, including prerequisites, availability, and how to manage Copilot features in your environment. Learn about Copilot and generative AI features in [Microsoft Power Apps.](../../copilot-landing-page.yml)

> [!NOTE]
>
> This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).

## Prerequisites

Each Copilot feature can have different requirements. Check the documentation for each feature to learn what you need.

> [!IMPORTANT]
>
> - Some Copilot features are in preview.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so customers can get early access and provide feedback.

## Availability

- This capability might not be available in your region yet. Learn more in [Explore Copilot features by geography and languages](https://releaseplans.microsoft.com/en-US/availability-reports/?report=copilotfeaturereport).
- This capability might be subject to usage limits or capacity throttling.
- Understand the capabilities and limitations of AI-powered and Copilot features in Power Apps. Learn more in [FAQ about using AI responsibly in Power Apps](../common/transparency-note.md).


## Enable or disable Copilot features

 [Generally available](/power-platform/admin/general-availability-deployment) Copilot features are on by default and can't be turned off except by Microsoft Support. To turn them off, a tenant admin needs to [contact Support](/power-platform/admin/get-help-support).

### Turn off Copilot preview features in Power Apps

Copilot preview features are on by default, but your admin can turn them off for an environment or a tenant.

#### Turn off Copilot preview features for an environment

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).
1. In the navigation pane, select **Environments**, and then select an environment.
1. On the command bar, select **Settings** > **Features**.
1. Set the **Copilot** toggle to **Off**.

#### Turn off Copilot preview features for your tenant

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).
1. In the navigation pane, select **Settings** to open the **Tenant settings** page.
1. Select **Copilot in Power Apps (preview)**, and then set the toggle to **Off**.
1. Select **Save**.

> [!NOTE]
> Turning off Copilot for your tenant turns off Copilot for makers only. It doesn't turn off the [Copilot control for canvas apps](add-ai-copilot.md) or [Copilot for model-driven apps](../model-driven-apps/add-ai-copilot.md).

### Related information

- [Copilot features in Power Apps](../../copilot-landing-page.yml)
- [FAQ about using AI responsibly in Power Apps](../common/transparency-note.md)
- [Language availability for Power Platform](https://dynamics.microsoft.com/availability-reports/languagereport/)
- [Geographical availability for Power Platform](https://dynamics.microsoft.com/availability-reports/georeport/)
