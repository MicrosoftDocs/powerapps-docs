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

Microsoft Dataverse supports custom retention policies to securely retain data long term in a cost-efficient way. With retention policies, you can support your business growth with unlimited storage.

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]
> - For public preview, only non-production environments are allowed for previewing the long-term data retention feature.
> - No additional Power Platform licensing requirement is required to experience this feature during the preview. However, there will be a licensing requirement once the feature is generally available.

## Business application data lifecycle

Consider the business application data lifecycle in three stages. First active data, which over time transitions to non-active data, and finally transitions to deleted data.

:::image type="content" source="media/business-app-data-lifecycle.png" alt-text="Business application data lifecycle diagram":::

|Stage  |Description  |
|---------|---------|
|1. Active data     |  Data is readily available and transformed via apps. <br /> Accessed across al application workflows.  <br /> Also referred to as *live* data.     |
|2. Non-active data     | Data is immutable. <br />  Is stored in long term retention.  <br /> Has limited access. Retained for compliance, audit, and legal discovery. <br />Also referred to as *cold* data.      |
|3. Deleted data   |  Permanently deleted. Data lifecycle is completed.        |

Dataverse delivers native platform support for long term retention of data. It allows organizations to get immediate and ongoing benefits:

- Reduce historical application data from the live application.
- Securely retain the historical data long term.
- Retain data without losing the ability to build custom screens.
- Avoid investments due to the need for custom solutions for long term retention of historical data.

## How it works

Application admins set up custom policies for a table with criterion to retain data long term. The retained data is never moved out of Dataverse, it is stored in a Dataverse managed data lake. The data is always secured with Dataverse security backed by Azure Active Directory.  

The retained data is never moved out of Dataverse and the data is always secured with Dataverse security and backed by Azure Active Directory.

> [!IMPORTANT]
> - Once data is moved to long term (non-active) data store it can't be moved back to the active (live) data store.
> - When a retention policy is run, the process makes API requests in Microsoft Power Platform. These requests are counted towards the existing API requests available with your plan. More information: [Requests limits and allocations](/power-platform/admin/api-request-limits-allocations)

Dataverse provides read-only access to the read-only retained data via:

- Advanced Find within an application.
- Power Automate cloud flow templates.
- Dataverse OData APIs used to build custom application workflows.

## Types of data retained long term

Dataverse standard (except system) tables, custom tables, along with attachments, can be retained in in Dataverse long term storage. 

> [!NOTE]
> Currently, audit rows, elastic table rows, and images aren't supported for long term retention.

Admins set retention policies on tables when the application maker has enabled long term retention for the table. When a maker enables retention on a parent root table, it also enables retention for all child tables.

### Long term data retention and existing delete action and plugins

All the existing delete action cascade relationships and plugins for tables are started when a data retention policy is run on the table.

### Tables not currently supported for retention

- PostFollow
- PostRegarding
- PostRole
- Post
- PostLike
- PostComment

## Next steps

[Set a data retention policy for a table](data-retention-set.md)
