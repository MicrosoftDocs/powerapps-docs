---
title: "Analyze data with dashboards (model-driven apps)"
description: "The dashboard tables in Microsoft Dataverse enable you to present data from various charts, grids, IFRAMES, or web resources simultaneously. Dashboards allow you to compare and analyze various pieces of customer information, and give you data snapshots."
author: jasongre
ms.author: jasongre
ms.date: 04/01/2022
ms.reviewer: jdaly
ms.topic: article
ms.subservice: mda-developer
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# Analyze data with dashboards

The dashboard tables in Microsoft Dataverse enable you to present data from various charts, grids, IFRAMES, or web resources simultaneously. Dashboards allow you to compare and analyze various pieces of customer information, and give you data snapshots.

## Types of dashboards

There are two types of dashboards: organization-owned dashboards and user-owned dashboards.

**Organization-owned dashboard**

An organization-owned dashboard is represented by the `SystemForm` table, and can't be assigned or shared. These dashboards are solution-aware tables. When you perform an update operation on this table, you must publish the changes for the updates to be available across the organization. When you publish customizations using the <xref:Microsoft.Crm.Sdk.Messages.PublishAllXmlRequest> message, the newly-created organization-owned dashboards are also published and become available across the organization.

Alternatively, you can publish the changes done to a specific dashboard by using the <xref:Microsoft.Crm.Sdk.Messages.PublishXmlRequest> message, and specifying the dashboard ID as the parameter in the request message.

**User-owned dashboard**

A user-owned dashboard is represented by the `UserForm` table, can be assigned and shared with other users, and can be viewed by other users depending on the dashboard's access privileges.

> [!NOTE]
> You can't programmatically create or manage the new interactive dashboards.
> For information about working with interactive dashboards using the web client, see [Configure interactive experience dashboards](../../maker/model-driven-apps/configure-interactive-experience-dashboards.md)

### See also

[Using FormXML for dashboards](understand-dashboards-dashboard-components-formxml.md)  
 [Actions on dashboards](actions-dashboards.md)  
 [Create a dashboard](create-dashboard.md)  
 [Sample dashboards](sample-dashboards.md)  
 [Sample: Create, retrieve, update, and delete (CRUD) a dashboard](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/CRUDOperationsDashboard)  
 [Sample: Assign a user-owned dashboard to another user](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/AssignUserOwnedDashboardToAnother)  
 [Visualization data description schema](visualization-data-description-schema.md)  
 [Customize visualizations and dashboards](customize-visualizations-dashboards.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
