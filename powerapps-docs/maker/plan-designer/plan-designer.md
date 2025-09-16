---
title: Use Plan designer to create AI-Powered business solutions with Copilot
description: Learn how to use Plan designer, an AI-powered tool in Power Platform, to create comprehensive business solutions.
author: szlo
contributors:
ms.topic: how-to
ms.date: 06/25/2025
ms.update-cycle: 180-days
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

Plan designer is a copilot-first development tool that lets you quickly create comprehensive business solutions. Describe your business use case in natural language and add relevant images, like business process flows or screenshots of legacy apps. Plan designer generates a complete Power Platform solution tailored to your needs. It includes Microsoft Dataverse tables, canvas apps, model-driven apps, Power Pages sites, Power Automate flows, and Copilot Studio agents.

:::image type="content" source="media/overview-plan-designer/pd-overview-landing-page.png" alt-text="Screenshot of Plan designer landing page in Power Apps.":::

## Prerequisites

Include a Dataverse database in your environment. Learn more in [Add a Microsoft Dataverse database](/power-platform/admin/create-database).

If your environment doesn't meet the prerequisites and you have access to developer environments, you're routed to your own developer environment where you have permissions to create Dataverse tables. Learn more in [Create a developer environment with the Power Apps Developer Plan](/power-platform/developer/create-developer-environment).

If your environment doesn't meet the prerequisites and you don't have access to existing developer environments or the ability to create new ones, you can't create plans in your current environment. In this situation, switch to an environment where you have the necessary permissions to create tables and start building your plan there.

The following security roles can see the Plan designer entry point on the Power Apps home page:

- System admin
- System customizer [security role](/power-platform/admin/security-roles-privileges).
- Environment maker. Environment makers are redirected to their own developer environment when they save tables.

For custom security roles, you need the following privileges for each operation in the Plan designer:

| Operation in Plan designer | Privileges [Table name - privilege] |
|---------------------------|-------------------------------------|
| Create a plan | - Plan - Read<br>- Publisher - Read<br>- Entity - Read<br>- Attribute - Read<br>- Solution - Read<br>- Relationship - Read<br>- Entity - Create |
| Save tables in plan | - Entity - Read<br>- User settings - Read<br>- Async operations - Read<br>- Entity - Append to<br>- Entity - Create |
| Share a plan | - Plan - Share |



## Availability

Plan designer is generally available. Check if this feature is available in your region. Learn more in [Explore Copilot features by geography and languages](https://releaseplans.microsoft.com/availability-reports/?report=copilotfeaturereport).

### Turn on preview features for Plan designer

Some features in Plan designer are only available in preview. When you turn on the preview experience for a plan, the entire plan is generated using the preview experience, which can include multiple preview features at any time.

To turn on preview features, select the **Include preview features** option when you enter your business problem.

:::image type="content" source="media/overview-plan-designer/preview-in-pd.png" alt-text="Screenshot of enabling preview feature for Plan designer.":::

If you have a plan and want to switch between the preview and generally available (GA) version, select the **Preview feature** icon to turn preview features on or off. You can change a plan from preview to GA only after saving it. To restart an unsaved plan without preview features, go to the Power Apps homepage and create a new plan.

:::image type="content" source="media/overview-plan-designer/turn-off-preview.png" alt-text="Screenshot of turning off preview feature for Plan designer.":::

> [!NOTE]
> When you switch the preview experience for Plan designer on or off, some content in the plan can be modified, regenerated, or deleted.


Preview Copilot features are available by default, but admins can turn them off for a specific environment or tenant. Learn more in [Copilot in Power Apps overview (preview)](../canvas-apps/ai-overview.md#disable-copilot-in-power-apps).


## Next steps

[Create a plan using Plan designer](create-plan.md)
