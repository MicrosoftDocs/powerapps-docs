---
title: Plan Designer Solutions and ALM Practices  
description: Learn how Plan Designer promotes healthy Application Lifecycle Management (ALM) practices by packaging plan components into solutions for advanced ALM capabilities.  
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
  - copilot-scenario-highlight  
---

# Manage your solution

Business solutions built with Plan designer promote healthy application lifecycle management (ALM) practices by using Power Platform resources. Use advanced ALM capabilities to deploy artifacts to target environments through managed solutions by packaging all components of a plan into a single solution artifact.

When you create a plan, the plan is stored in the main solution, which enables the **Objects** view in Plan designer. Makers can switch between the plan and the solution view without leaving Plan designer.

A plan might be associated with multiple solutions. For example, adding an existing Dataverse table to the plan's data model links the solutions associated with the Dataverse table to the plan.

The solutions associated with the plan display as tabs across the top when you select the **Objects** view. Select a tab to view objects in the solution. If there are more than five solutions, an overflow menu shows the remaining solutions. All solution objects are displayed, not just the ones included in the plan.

Learn more about solutions in [Solution view](/power-apps/maker/data-platform/solutions-area).

:::image type="content" source="media/manage-solution/object-view.png" alt-text="Screenshot of the Objects view in Plan designer that shows objects in a solution.":::

## Show objects in this plan

Each plan has a main solution, but other solutions are associated with the plan when you add existing tables or apps from them. These associated solutions might include many objects beyond the ones you add to the plan.

To track which objects from the associated solutions are tied to the plan, select **Only show objects in this plan**. This option lets you view components explicitly designated as part of the plan. 

:::image type="content" source="media/manage-solution/only-show-objects-in-plan.png" alt-text="Screenshot of the 'Only show objects in this plan' option.":::

When you clear **Only show objects in this plan**, the complete contents of these solutions are shown. This helps you understand the broader context, overall composition, and potential dependencies.

## Known issues

- When the **Only show objects in this plan** filter is on, some object categories with zero items still appear in the left tree view.
- Some existing canvas apps added to the plan might not filter properly with the **Only show objects in this plan** filter. This issue sometimes affects canvas apps that aren't connected to Dataverse.
- Intermittent caching issues occur. If associated solutions don't show up in the **Objects** view, resave the plan and refresh the **Objects** view to fix the issue.

## Related information

- [Create a plan using Plan designer](create-plan.md)
- [Create a plan from a solution](create-plan-from-solution.md)