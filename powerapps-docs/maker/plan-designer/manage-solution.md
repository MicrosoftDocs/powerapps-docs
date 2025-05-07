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

Solutions built with Plan designer promote healthy application lifecycle management (ALM) practices from the start by using Power Platform solutions. By packaging all plan components into a single solution artifact, makers use advanced ALM capabilities to deploy their artifacts to target environments through managed solutions.

When you create a plan, it is stored within a solution, which enables the Objects view in Plan designer. This lets makers switch between their plan and the solution view without leaving Plan designer.

A plan can be associated with multiple solutions. For example, if you add an existing Dataverse table to the plan’s data model, the solutions linked to the Dataverse table also link to the plan.

The solutions associated with the plan are displayed as tabs across the top of the **Objects** view. Select a tab to view the objects in the solution. If there are more than five solutions, an overflow menu shows the remaining solutions. All solution objects are displayed, not just those included in the plan.

:::image type="content" source="media/manage-solution/object-view.png" alt-text="Screenshot of the Objects view in Plan designer showing objects in a solution.":::

For more information about solutions, see [Solution view](/power-apps/maker/data-platform/solutions-area).

## Show objects in this plan

Each plan has a main solution, but other solutions can become associated with the plan as you add existing tables or apps from other solutions. Each of these associated solutions can have many objects beyond those that you added to the plan. 

To track which objects from the associated solutions are specifically tied to the plan, select **Only show objects in this plan** to narrow the view to just those components explicitly designated as part of the plan. 

:::image type="content" source="media/manage-solution/only-show-objects-in-plan.png" alt-text="Only show objects in this plan":::

When you uncheck **Only show objects in this plan** it display the complete contents of these solutions, which helps in understanding the broader context, overall composition, and potential dependencies.

## Known issues

- When the **Only show objects in this plan** filter is on, some object categories with (0) items will still appear in the left tree view.
-	Some existing canvas apps that are added to the plan might not filter properly with the **Only show objects in this plan** filter. This sometimes affects canvas apps that are not a part of Dataverse.
-	There are intermittent caching issues. If associated solutions are not showing up in **Objects** view, please resave the plan and refresh the **Objects** view.

