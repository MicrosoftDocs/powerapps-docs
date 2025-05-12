---
title: Use Plan Designer to Create AI-Powered Business Solutions with Copilot
description: Learn how to use the Plan Designer, an AI-powered tool in Power Platform, to create comprehensive business solutions.
author: szlo
contributors:
ms.topic: conceptual
ms.date: 05/19/2025
ms.author: mkaur
ms.reviewer: mkaur
ms.collection:
  - bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-title
  - ai-gen-desc
  - copilot-scenario
---

# Overview of Plan designer

Plan designer is a copilot-first development tool that lets you create comprehensive business solutions quickly. Simply describe your business use case in natural language and add relevant images, such as business process flows or screenshots of legacy apps. The Plan designer generates a complete Power Platform solution tailored to your needs. It includes Dataverse tables, canvas apps, model-driven apps, and Power Automate flows.

:::image type="content" source="media/overview-plan-designer/pd-overview-landing-page.png" alt-text="Screenshot of Plan designer landing page in Power Apps.":::

## Prerequisites

Include a Dataverse database in your environment. Learn more in [Add a Microsoft Dataverse database](/power-platform/admin/create-database).

If your environment doesn't meet the prerequisites, you are routed to your own developer environment where you have permissions to create Dataverse tables. Learn more in [create a developer environment with the Power Apps Developer Plan](/power-platform/developer/create-developer-environment).

## Availability

Confirm that this feature is available in your region. Learn more in [Explore Copilot features by geography and languages](https://releaseplans.microsoft.com/en-US/availability-reports/?report=copilotfeaturereport).

### Turn on preview features for Plan designer

Some features within Plan designer are only available in preview. When you turn on the preview experience for a plan, the entire plan is generated using the preview experience, which might include multiple preview features at any time.

To turn on preview features, select the **Include preview features** option when entering your business problem.

:::image type="content" source="media/overview-plan-designer/preview-in-pd.png" alt-text="Enable preview feature for Plan designer":::


If you've already created a plan and want to switch between the preview and General Availability (GA) experience, select the **Preview feature** icon to turn preview features on or off for the plan. A plan can only be changed from preview to General Availability after it has been saved. To restart an unsaved plan without preview features, go back to the Power Apps homepage and create a new plan.

:::image type="content" source="media/overview-plan-designer/turn-off-preview.png" alt-text="Turn off preview feature for Plan designer":::

> [!CAUTION]
> When you switch the preview experience for Plan designer on or off, some content in the plan might be edited, regenerated, or removed.

Preview Copilot features are available by default, but admins can turn them off for a specific environment or tenant. Learn more in [Copilot in Power Apps overview (preview)](../canvas-apps/ai-overview.md#disable-copilot-in-power-apps).


## Next s
ds
[Create a plan using Plan designer](create-plan.md)
