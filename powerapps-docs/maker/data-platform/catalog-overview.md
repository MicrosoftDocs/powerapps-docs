---
title: Discover, acquire, and reuse solution templates with catalogs
description: Provides an overview of catalogs in Power Apps.
ms.date: 05/04/2023
ms.reviewer: matp
ms.topic: overview
author: derekkwanpm
ms.subservice: dataverse-maker
ms.author: "derekkwan"
search.audienceType:
  - maker
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-title
  - ai-seo-date:03/07/2024
---
# Discover, acquire, and reuse solution templates with catalogs

A catalog allows makers to publish, discover, and acquire company specific Power Platform objects to accelerate the building of apps, flows, and solutions. Catalogs provide a dedicated workspace inside of Power Apps.

Building from templates customized for your company reduces duplicative work and inconsistencies in implementation. For example, imagine building a webpage from scratch rather than using a webpage already designed with your company header and footer, branding, privacy links, and so on that can be reused as needed.

Every Power Platform tenant has a single catalog, which contains re-usable solution objects for your organization. You can choose to have multiple catalogs across environments for different regions or departments, however in most cases, you only need one catalog.

Solutions can be published to the catalog for other makers to acquire and use, as one of these two artifact types:

- A template: This is a copy of your unmanaged solution that other makers can edit however they choose. Updates to the original unmanaged solution doesn't update templates because templates aren't *connected* to the solution they come from. If you want other makers to freely customize these solution objects, use a template.
- A managed item: Managed items can be updated with more versions as the original solution is updated, but are generally restricted from editing. If you want makers to use your solution *as is* and you also want to keep copies updated with your changes in the future, use a managed item.

## Catalog governance and creation

The default catalog is designed for makers of any level of experience to publish, discover, and acquire useful artifacts. However, Power Platform admins can create additional catalogs, manage access and security, approve catalog items, and more in the *Catalogs* area in the Power Platform admin center. The Catalog Manager is the dedicated workspace for admins of the catalogs.

More information: <!-- Link to PPAC article for admins do this so needs to go in the PPAC docs-->

## Work with the catalog

When you create a solution, consider whether it contains solution objects that would be useful for resuse for yourself or others in your organization.

### Add a solution to the catalog

1. Sign in to Power Apps.
1. Select **Solutions** on the left navigation pane, and then select the unmanaged solution you want to add to the catalog. 
1. Select **Publish to catalog** on the command bar.
1. The **Add your solution** step appears. On the **Select catalog** pane, select the catalog you want to publish to and then select **Next**.
1. Select from the following choices:
   1. **What kind of submission is this?**
      - **Template**. For unmanaged solutions that can be customized by you and other makers.
      - **Managed item**. For managed solutions with objects that you typically don't want customized.
   1. **Select primary component**. Select the solution object, such as an app or a flow, that is the primary component. Optionally, leave the primary component as **Undefined**.
1. Select **Next**.
1. On the **Add some details about you solution** step, enter the following information:
   - **Title**. Leave the name of the solution or change it.
   - **Description**. Enter a description for the solution.
   - **Business justification** (optional). Enter a business justification that is viewed by catalog approvers.
   - **Select business catagories** (optional). Select among the relevant categories that were configured for the catalog.
   - **Publisher**. Select the solution publisher or create a new one.
   - **Author**. Add the user that will be identified as the author of the solution.
   - **Add you solution icon** (optional). Browse or drag and drop a 216 x 216 pixel dimension icon for the solution.
1. On the **Solution info** step, enter the following optional links to available resources:
   - **Help link**
   - **Privacy policy link**
   - **Legal terms link**
1. Select **Next**.
1. On the **Review + finish** step, review the publishing settings and if no changes are needed select **Submit**.

Makers with access to the catalog can publish to the catalog. However, after a solution has been published to the catalog, the maker must be a part of the catalog publishing group to publish that same solution to the catalog again. If you do not have access, you receive the message "Access needed. This solution has already been published to the catalog as &lt;catalog name &gt;. You need to be a member of the publisher group that owns this:" When this occurs, contact your admin for publishing permission.

## See also

[Solutions overview](solutions-overview.md)

[Enterprise templates for Power Platform](/power-platform/enterprise-templates/overview)