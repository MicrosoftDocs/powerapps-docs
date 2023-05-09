---
title: Dataverse long term data retention overview
description: Overview of long term retention for data in Microsoft Dataverse 
author: Mattp123
ms.service: powerapps
ms.author: matp
ms.topic: overview
ms.date: 05/09/2023
ms.custom: template-overview
---
# Dataverse long term data retention overview (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Microsoft Dataverse supports custom retention policies to securely retain data long term in a cost-efficient way. With retention policies, you can support your business growth with unlimited storage.

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]
> - For public preview, only non-production environments are allowed for previewing the long-term data retention feature. Production and Dataverse for Teams environments can't be used with this feature.
> - No additional Power Platform licensing requirement is required to experience this feature during the preview. However, there will be a licensing requirement once the feature is generally available.

## Business application data lifecycle

Consider the business application data lifecycle in three stages. First active data, which over time transitions to inactive data, and finally transitions to deleted data.

:::image type="content" source="media/business-app-data-lifecycle.png" alt-text="Business application data lifecycle diagram":::  <!-- Girish to update diagram -->

|Stage  |Description  |
|---------|---------|
|1. Active data     |  Data is readily available and transformed via apps. <br /> Accessed across all application workflows.  <br /> Also referred to as *live* data.     |
|2. Inactive data     | Data is immutable and read-only. <br />  Is stored in long term retention.  <br /> Has limited access. Retained for compliance, audit, and legal discovery.      |
|3. Deleted data   |  Permanently deleted. Data lifecycle is completed.        |

Dataverse delivers native platform support for long term retention of data. It allows organizations to get immediate and ongoing benefits:

- Securely retain the historical application data long term for audit, legal, and regulatory requirements.
- Access the read-only data for limited inquiry purposes.
- Reduce database capacity consumed.
- Avoid IT investments required to build and maintain custom solutions for long term retention of historical application data.

## How it works

Application admins set up custom policies for a table with criterion to retain data long term. The retained data is never moved out of Dataverse, it's stored in a Dataverse managed data lake. The data is always secured with Dataverse security backed by Azure Active Directory.  

> [!IMPORTANT]
> - Once data is retained in the Dataverse long term (inactive) store it can't be moved back to the Dataverse live (active) data store.
> - When a retention policy is run, the process makes API requests in Microsoft Power Platform. These requests are counted towards the existing API requests available with your plan. More information: [Requests limits and allocations](/power-platform/admin/api-request-limits-allocations)

Dataverse provides read-only access to the retained data via:

- Advanced Find within an application.
- Power Automate cloud flow.
- Dataverse OData APIs for custom screens.

## Types of data retained long term

Dataverse standard (except system) tables, custom tables, along with attachments, can be retained in Dataverse long term storage.

> [!NOTE]
> Currently, audit, elastic tables, and images aren't supported for long term retention.

Admins set retention policies on tables when the application maker has enabled long term retention for the table. When a maker enables retention on a parent root table, it also enables retention for all child tables.

### Long term data retention and existing delete action and plugins

All the existing delete action cascade relationships and plugins for tables are started when a data retention policy is run on the table.

## Next steps

[Set a data retention policy for a table](data-retention-set.md)
