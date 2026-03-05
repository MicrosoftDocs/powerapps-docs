---
title: Use plans to create AI-Powered business solutions with Copilot
description: Learn how to use plans, an AI-powered tool in Power Platform, to create comprehensive business solutions.
author: szlo
contributors:
ms.topic: how-to
ms.date: 02/24/2026
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

# Overview of plans

Plans in Power Apps is a copilot-first development tool that lets you quickly create comprehensive business solutions. Describe your business use case in natural language and add relevant images, like business process flows or screenshots of legacy apps. Plans generates a complete Power Platform solution tailored to your needs. It includes Microsoft Dataverse tables, canvas apps, model-driven apps, Power Pages sites, Power Automate flows, and Copilot Studio agents.

:::image type="content" source="media/overview-plan-designer/pd-overview-landing-page.png" alt-text="Screenshot of plans in Power Apps.":::

## Prerequisites

> [!IMPORTANT]
> For Government Community Cloud users, plans is supported only in the Government Community Cloud (GCC). For more information, see [Plans in Sovereign Clouds](https://github.com/microsoft/SLG-Business-Applications/blob/main/white-papers/Plan-Designer-disclaimer.md)

To use plans in Power Apps, follow these steps:

**1. Environment requirements** 

1. **Dataverse database required:** Make sure your environment includes a [Microsoft Dataverse database](/power-platform/admin/create-database).
1. **Copilot features enabled:** Plans is [generally available](/power-platform/admin/general-availability-deployment) and enabled by default. It can't be turned off except through Microsoft Support. A tenant administrator must [contact Support](/power-platform/admin/get-help-support) to request that it be turned off.
1. **Environment must be in an eligible locale**

**2. What if you don’t meet the prerequisites?**

1. **Developer Environment Option**: If your current environment doesn’t meet the requirements but you can use developer environments, you're automatically routed to your own developer environment. There, you have permission to create Dataverse tables. Learn more in [Create a developer environment](/power-platform/developer/create-developer-environment).
1. **No Developer Environment Available:** If you can’t use or create a developer environment, you won’t be able to create plans in your current environment. In this case, switch to an environment where you have permission to create tables and start building your plan there.


**3. Who can access plans?**

The following security roles can see the entry point for plans on the Power Apps home page:

- System admin
- [System customizer](/power-platform/admin/security-roles-privileges)
- Environment maker: Are redirected to their own developer environment when they save tables.
- For custom security roles: You need the following privileges for each operation in plans:

    | **Operation in plans** | **Table**        | **Privilege** |
    |--------------------------------|------------------|---------------|
    | Create a plan                  | Plan             | Read          |
    |                                | Publisher        | Read          |
    |                                | Entity           | Read          |
    |                                | Attribute        | Read          |
    |                                | Solution         | Read          |
    |                                | Relationship     | Read          |
    |                                | Entity           | Create        |
    | Save tables in plan            | Entity           | Read          |
    |                                | User settings    | Read          |
    |                                | Async operations | Read          |
    |                                | Entity           | Append to     |
    |                                | Entity           | Create        |
    | Share a plan                   | Plan             | Share         |


## Availability

Plans is [generally available](/power-platform/admin/general-availability-deployment) and enabled by default. Check if the feature is available in your region. Learn more in [Explore Copilot features by geography and languages](https://releaseplans.microsoft.com/availability-reports/?report=copilotfeaturereport).



## Next steps

[Create a plan](create-plan.md)
