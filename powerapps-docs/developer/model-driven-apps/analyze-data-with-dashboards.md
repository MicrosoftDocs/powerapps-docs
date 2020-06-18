---
title: "Analyze data with dashboards (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "The dashboard entities in Dynamics 365 Common Data Service enable you to present data from various charts, grids, IFRAMES, or web resources simultaneously. Dashboards allow you to compare and analyze various pieces of customer information, and give you data snapshots." # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: article
ms.assetid: 4b54597b-5603-2e6e-4630-bc120f711707
author: Nkrb # GitHub ID
ms.author: nabuthuk # MSFT alias of Microsoft employees only
manager: shilpas # MSFT alias of manager or PM counterpart
ms.reviewer: 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Analyze data with dashboards

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/customize-dev/analyze-data-with-dashboards -->

The dashboard entities in Common Data Service enable you to present data 
from various charts, grids, IFRAMES, or web resources simultaneously. Dashboards allow you to compare and analyze various pieces of customer information, and give you data snapshots.  
  
## Types of dashboards  

There are two types of dashboards: organization-owned dashboards and user-owned dashboards.  
  
**Organization-owned dashboard.**

An organization-owned dashboard is represented by the `SystemForm` entity, and can’t be assigned or shared. 
These dashboards are solution-aware entities. 
When you perform an update operation on this entity, you must publish the changes for the updates to be available across the organization. 
When you publish customizations using the <xref:Microsoft.Crm.Sdk.Messages.PublishAllXmlRequest> message, the newly-created organization-owned dashboards are also published and become available across the organization. 
Alternatively, you can publish the changes done to a specific dashboard by using the <xref:Microsoft.Crm.Sdk.Messages.PublishXmlRequest> message, and specifying the dashboard ID as the parameter in the request message.  
  
**User-owned dashboard.**

A user-owned dashboard is represented by the `UserForm` entity, can be assigned and shared with other users, and can be viewed by other users depending on the dashboard’s access privileges.  
  
> [!NOTE]
> You can’t programmatically create or manage the new interactive dashboards. 
> For information about working with interactive dashboards using the web client, see [Configure interactive experience dashboards](../../maker/model-driven-apps/configure-interactive-experience-dashboards.md) 
  
### See also  

 [Using FormXML for Dashboards](understand-dashboards-dashboard-components-formxml.md)   
 [Actions on Dashboards](actions-dashboards.md)   
 [Create a Dashboard](create-dashboard.md)   
 [Sample Dashboards](sample-dashboards.md)   
 [Dashboard Entities](/dynamics365/customer-engagement/developer/customize-dev/dashboard-entities)   <!-- TODO: Need to find the topic in powerapps repo to link-->
 [Sample: Create, Retrieve, Update and Delete (CRUD) a Dashboard](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/CRUDOperationsDashboard)
 [Sample: Assign a User-Owned Dashboard to Another User](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/AssignUserOwnedDashboardToAnother)  
 [Visualization data description schema](visualization-data-description-schema.md)     
 [Customize visualizations and dashboards](customize-visualizations-dashboards.md)
