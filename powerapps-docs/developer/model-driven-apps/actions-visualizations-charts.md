---
title: "Actions on visualizations (charts) (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "Using the Microsoft Dataverse web services, you can perform the following actions on the visualization tables." # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: article
ms.assetid: c7eb3bdf-9d6f-9bcc-8114-4c3dc5be2976
author: Nkrb # GitHub ID
ms.subservice: mda-developer
ms.author: nabuthuk # MSFT alias of Microsoft employees only
manager: shilpas # MSFT alias of manager or PM counterpart
ms.reviewer: 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Actions on visualizations (charts)

Using the Microsoft Dataverse Web Services, you can perform the following actions on the visualization tables.  
  
## Actions on organization-owned visualizations 

To perform actions on an organization-owned visualization (`SavedQueryVisualization`), you must have the System Administrator or the System Customizer role. You can perform the following actions on an organization-owned visualization:  
  
- Create, retrieve, update, and delete an organization-owned visualization. More information: [Create a visualization](create-visualization-chart.md)  
  
  > [!NOTE]
  >  After updating an organization-owned visualization, you must publish the table definitions changes to make it visible across the organization by using the <xref:Microsoft.Crm.Sdk.Messages.PublishAllXmlRequest> message. Alternatively, whenever you publish a table, all the unpublished organization-owned visualizations that are attached to the table are published automatically.  
  
- Query and retrieve all the organization-owned visualizations that are attached to a table using the `SavedQueryVisualization.PrimaryEntityTypeCode`. Multiple organization-owned visualizations can be attached to a single table. For a list of tables with which you can attach a visualization, see [Tables Supported for visualizations](view-data-with-visualizations-charts.md). For a code sample that demonstrates how to retrieve all the organization-owned visualizations attached to a table, see [Sample: Retrieve all charts attached to a table](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/RetrieveChartsAttachedToEntity).
  
  > [!NOTE]
  >  You cannot change or update a visualization to attach it with a different table after you have created the visualization. It implies that the `SavedQueryVisualization.PrimaryEntityTypeCode` is not valid for the update action on the organization-owned visualization.
  
- Specify an organization-owned visualization as the default visualization for the associated table by setting the `SavedQueryVisualization.IsDefault` to `true`. When you set an organization-owned visualization as the default visualization for a table, the visualization is displayed by default when you select to view the visualizations for this table in Dataverse.
  
  > [!NOTE]
  >  Using the Dataverse Web Services, if you set an organization-owned visualization as default for a table that already has another visualization set as default, both the visualizations are marked as default visualizations for the table.  To set a visualization as a default visualization for a table, make sure that no other visualization is set as the default visualization for the table.  
  
  For a list of supported messages on the organization-owned visualization table, see [SavedQueryVisualization table](../data-platform/reference/entities/savedqueryvisualization.md).
  [!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

## Actions on user-owned visualizations  

 You can perform the following actions on a user-owned visualization (`UserQueryVisualization`):  
  
- Create, retrieve, update, and delete a user-owned visualization. More information: [Create a visualization](create-visualization-chart.md)  
  
- Query and retrieve all the user-owned visualizations that are attached to a table using the `UserQueryVisualization.PrimaryEntityTypeCode`. Multiple user-owned visualizations can be attached to a table. For a list of tables with which you can attach a visualization, see [Tables supported for visualizations](view-data-with-visualizations-charts.md).  
  
  > [!NOTE]
  >  You cannot change or update a visualization to attach it with a different table after you have created the visualization. It implies that the `UserQueryVisualization.PrimaryEntityTypeCode` is not valid for the update action on the user-owned visualization.
  
- Change the ownership of a user-owned visualization by assigning it to another user or team using <xref:Microsoft.Crm.Sdk.Messages.AssignRequest>.  
  
- Retrieve the access that the specified security principal (user or team) has to a user-owned visualization using <xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>. You can also retrieve all the security principals (users or teams) that have access to a user-owned visualization, along with their access rights to the user-owned visualization using the <xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>.  
  
- Collaborate with other users and teams on specific areas by sharing a user-owned visualization with them using <xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>, <xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>, and <xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>.  
  
  For a list of supported messages on the user-owned visualization table, see [UserQueryVisualization table](../data-platform/reference/entities/userqueryvisualization.md).

### See also  

 [Charts](view-data-with-visualizations-charts.md)   
 [Understanding Charts: Underlying data and chart representation](understand-charts-underlying-data-chart-representation.md)   
 [Create a chart](create-visualization-chart.md)   
 [Sample charts](sample-charts.md)   
 [Sample: Create, retrieve, update, and delete (CRUD) a chart](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/CRUDOperationsChart)  
 [Sample: Retrieve all charts attached to a table](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/RetrieveChartsAttachedToEntity)   
 [Sample: Assign a chart to another user](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/AssignChartToAnotherUser)   
 [SavedQueryVisualization table](../data-platform/reference/entities/savedqueryvisualization.md)   
 [UserQueryVisualization table](../data-platform/reference/entities/userqueryvisualization.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]