---
title: Dataverse long term data retention overview
description: Overview of long term retention for data in Microsoft Dataverse 
author: Mattp123
ms.service: powerapps
ms.author: matp
ms.topic: overview
ms.date: 03/23/2023
ms.custom: template-overview
---
# Dataverse long term data retention overview (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Microsoft Dataverse provides a custom policy driven approach to enable operational effectiveness and storage management of business application data. Support your business growth with unlimited storage.

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]
> - For public preview, only non-production environments are allowed for previewing the long-term data retention feature.
> - There's no additional Power Platform licensing requirement during this preview. When this feature becomes generally available, there will be a licensing requirement.

## Business application data lifecycle

Consider the business application data lifecycle in three stages. First active data, which over time transitions to non-active data, and finally transitions to deleted data.

:::image type="content" source="media/business-app-data-lifecycle.png" alt-text="Business application data lifecycle diagram":::

|Stage  |Description  |
|---------|---------|
|1. Active data     |  Data is readily available and transformed via apps. <br /> Accessed across al application workflows.  <br /> Also referred to as *live* data.     |
|2. Non-active data     | Data is immutable. <br />  Is stored in long term retention.  <br /> Has limited access. Retained for compliance, audit, and legal discovery. <br />Also referred to as *cold* data.      |
|3. Deleted data   |  Permanently deleted. Data lifecycle is completed.        |

Dataverse delivers native platform support for long term retention of data. It allows organizations to get immediate and ongoing benefits.

- Reduces historical data in the live application and improves application performance, without the requirement to move data outside Dataverse. 
- Ensures regulatory compliance with Dataverse enterprise governance.
- Powers business value by using low cost with Microsoft low code/no code tools to build custom screens.
- Reduces total cost of ownership when compared to custom compliance solutions.

## How it works

When an application maker has enabled long term retention for a table in Power Apps (make.powerapps.com), a Power Platform admin can set a retention policy on the table from the Power Platform admin center. Notice that, when a maker enables retention on a parent root table, it also enables retention for all related child tables.

The retained data is never moved out of Dataverse and the data is always secured with Dataverse security and backed by Azure Active Directory.

> [!IMPORTANT]
> - Once data is moved to long term (non-active) data store it can't be moved back to the active data store.
>
> - When a retention policy is run, the process makes API requests in Microsoft Power Platform. These requests are counted towards the existing API requests available with your plan. More information: [Requests limits and allocations](/power-platform/admin/api-request-limits-allocations)

Dataverse provides read-only access to the immutable retained data via:

- Advanced Find within an application.
- Power Automate cloud flow templates.
- Dataverse OData APIs that can be used to build custom application workflows.

### Long term data retention and existing delete action and plugins

All the existing delete action cascade relationships and plugins for a table are started when a data retention policy is run on a table.

## Kinds of data retained long term

With the exception of system tables, Dataverse standard and activity tables, along with attachments, can be retained in in the long term storage.

Data retained by long term storage is made available to features like [Lockbox](/power-platform/admin/about-lockbox) and [customer managed key](/power-platform/admin/customer-managed-key).

### Tables not currently supported for retention

- PostFollow
- PostRegarding
- PostRole
- Post
- PostLike
- PostComment

## Next steps

[Set a data retention policy for a table](data-retention-set.md)
