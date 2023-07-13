---
title: Dataverse long term data retention overview
description: Overview of long term retention for data in Microsoft Dataverse 
author: Mattp123
ms.service: powerapps
ms.author: matp
ms.topic: overview
ms.date: 05/24/2023
ms.custom: template-overview
---
# Dataverse long term data retention overview (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Microsoft Dataverse supports custom retention policies to securely retain unlimited data long term in a cost-efficient way. While Dataverse can support your business growth with no limit on active data, you might want to consider moving inactive data to the Dataverse long term retention store.

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]
> - For public preview, only non-production environments are allowed for previewing the long-term data retention feature. Production and Dataverse for Teams environments can't be used with this feature.
> - No additional Power Platform licensing requirement is required to experience this feature during the preview. However, there will be a licensing requirement once the feature is generally available.
> - Pricing information for long term data retention will be available at general availability.

Watch this video to learn about Dataverse long term data retention.
> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RW15oAf]

## Business application data lifecycle

Consider the business application data lifecycle in three stages. First active data, which over time transitions to inactive data, and finally transitions to deleted data.

:::image type="content" source="media/business-app-data-lifecycle.png" alt-text="Business application data lifecycle diagram"::: 

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
> - Customers using self-managed encryption key (BYOK) should be aware that long term retained data in the Azure data lake is encrypted with Microsoft managed key. Consider migrating to customer managed key. More information: [Migrate bring-your-own-key environments to customer-managed key](/power-platform/admin/cmk-migrate-from-byok)
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

All the existing delete action cascade relationships and plugins for tables are executed when a data retention policy is run on the table.

More information: [Long-term data retention](../../developer/data-platform/long-term-retention.md)

## Storage capacity reports

With Dataverse long term retention, data is never moved out of Dataverse. The reported capacity in the existing Power Platform admin reports includes both live (active) and retained (inactive) data in GBs.

- Database capacity details reported:
  - Database capacity reported is the sum of the live and retained data. The overall database capacity consumed is reduced depending on the proportion of the data rows retained during a policy run.  
- Notice that the policy run will take 72 to 96 hours to complete and there will be an additional 24 hours afterward for the database capacity reports to appear.
- When available, the reports display two entries for a table that has been enabled for long term retention:
   - *Table*, such as **Case**<sup>1</sup> or **Contact**.
   - *Table-Retained*, such as **Case-Retained** and **Contact-Retained**.

   <sup>1</sup> The case table requires a Dynamics 365 app, such as Dynamics 365 Service.

- File capacity details reported:
  - If there are associated file attachments retained long term, the file capacity reflects the sum of the live and retained data. There will be no reduction or savings observed with file capacity after running a retention policy, which involved file attachments.  

Log capacity reports aren't currently available.

### Viewing the capacity reports

Imagine a non-production scenario where all the live data for the case and contacts tables are retained with Dataverse long term retention. After the long term retention policy is successfully completed, there are entries for **Case-Retained** and **Contact-Retained** in the report. The reduction in database capacity consumed depends on the number of rows and column data types involved in the retention process.

:::image type="content" source="media/data-retention-storage-capacity-report.png" alt-text="Storage capacity report that includes retained table data" lightbox="media/data-retention-storage-capacity-report.png":::

> [!NOTE]
> - If the tables are not visible in the report, export the view to an Excel worksheet by selecting the three vertical bars on the top right of the capacity report, and then select **Download all tables**. 
> - If a table commonly has associated child tables, the capacity reports also display the child table-retained GB size.

For more information about capacity reports, go to [New Microsoft Dataverse storage capacity](/power-platform/admin/capacity-storage).

## Solution aware retention policies

Dataverse retention policies are solution aware. Dataverse retention policies added to a solution are known as solution-aware retention policies. You can add multiple retention policies to a single solution. Retention policies are added to an unmanaged solution. This helps makers follow application lifecycle management (ALM) best practices when working with Dataverse retention policies.

When you include your retention policies in a solution, their definitions become portable, making it easier to move them from one environment to another, saving time required to create the retention policy. For example, you first develop a solution containing a retention policy in a development or sandbox environment. You then move that retention policy to a pre-production environment to test and validate that the solution works well and is ready for production. After testing is completed, the admin imports the solution into the production environment.

> [!NOTE]
> - The data retained by retention policies isn't portable as part of solutions, only the retention policy definitions are. You must run the retention policy in an environment to retain the data in Dataverse long term storage.
> - Only retention policies created in Power Platform environments can be solution-aware.

You create a solution before you add a retention policy to it. Exporting and importing solutions containing retention policies is the same as with other solution components.

For more information about solutions and solution components, go to [Solutions overview](solutions-overview.md).

## Next steps

[Set a data retention policy for a table](data-retention-set.md) <br />
[Share your ideas](https://experience.dynamics.com/ideas/categories/list/?category=55f731de-11f3-ed11-8848-00224827ed7b&forum=eef9aef6-0ff3-ed11-8848-00224827e88b)
