---
title: "Actions on visualizations (charts) (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "Using the Common Data Service for Apps web services, you can perform the following actions on the visualization entities." # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 08/01/2018
ms.service:
  - "powerapps"
ms.custom:
  - ""
ms.topic: article
ms.assetid: c7eb3bdf-9d6f-9bcc-8114-4c3dc5be2976
author: JimDaly # GitHub ID
ms.author: jdaly # MSFT alias of Microsoft employees only
manager: shilpas # MSFT alias of manager or PM counterpart
ms.reviewer: 
---

# Actions on visualizations (charts)

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/customize-dev/actions-visualizations-charts -->

Using the Common Data Service (CDS) for Apps Web Services, you can perform the following actions on the visualization entities.  
  
## Actions on organization-owned visualizations  
 To perform actions on an organization-owned visualization (`SavedQueryVisualization`), you must have the System Administrator or the System Customizer role. You can perform the following actions on an organization-owned visualization:  
  
- Create, retrieve, update, and delete an organization-owned visualization. More information: [Create a Visualization](create-visualization-chart.md)  
  
  > [!NOTE]
  >  After updating an organization-owned visualization, you must publish the metadata changes to make it visible across the organization by using the <xref:Microsoft.Crm.Sdk.Messages.PublishAllXmlRequest> message. Alternatively, whenever you publish an entity, all the unpublished organization-owned visualizations that are attached to the entity are published automatically.  
  
- Query and retrieve all the organization-owned visualizations that are attached to an entity using the `SavedQueryVisualization.PrimaryEntityTypeCode` attribute. Multiple organization-owned visualizations can be attached to a single entity. For a list of entities with which you can attach a visualization, see [Entities Supported for Visualizations](view-data-with-visualizations-charts.md#SupportedVisualizationEntities). For a code sample that demonstrates how to retrieve all the organization-owned visualizations attached to an entity, see [Sample: Retrieve all Charts Attached to an Entity](/dynamics365/customer-engagement/developer/customize-dev/sample-retrieve-all-charts-attached-entity).
  
  > [!NOTE]
  >  You cannot change or update a visualization to attach it with a different entity after you have created the visualization. It implies that the `SavedQueryVisualization.PrimaryEntityTypeCode` attribute is not valid for the update action on the organization-owned visualization.
  
- Specify an organization-owned visualization as the default visualization for the associated entity by setting the `SavedQueryVisualization.IsDefault` attribute to `true`. When you set an organization-owned visualization as the default visualization for an entity, the visualization is displayed by default when you select to view the visualizations for this entity in CDS for Apps.
  
  > [!NOTE]
  >  Using the CDS for Apps Web Services, if you set an organization-owned visualization as default for an entity that already has another visualization set as default, both the visualizations are marked as default visualizations for the entity.  To set a visualization as a default visualization for an entity, make sure that no other visualization is set as the default visualization for the entity.  
  
  For a list of supported messages on the organization-owned visualization entity, see [SavedQueryVisualization Entity](../common-data-service/reference/entities/savedqueryvisualization.md).
  
## Actions on user-owned visualizations  
 You can perform the following actions on a user-owned visualization (`UserQueryVisualization`):  
  
- Create, retrieve, update, and delete a user-owned visualization. More information: [Create a Visualization](create-visualization-chart.md)  
  
- Query and retrieve all the user-owned visualizations that are attached to an entity using the `UserQueryVisualization.PrimaryEntityTypeCode` attribute. Multiple user-owned visualizations can be attached to an entity. For a list of entities with which you can attach a visualization, see [Entities Supported for Visualizations](view-data-with-visualizations-charts.md#SupportedVisualizationEntities).  
  
  > [!NOTE]
  >  You cannot change or update a visualization to attach it with a different entity after you have created the visualization. It implies that the `UserQueryVisualization.PrimaryEntityTypeCode` attribute is not valid for the update action on the user-owned visualization.
  
- Change the ownership of a user-owned visualization by assigning it to another user or team using <xref:Microsoft.Crm.Sdk.Messages.AssignRequest>.  
  
- Retrieve the access that the specified security principal (user or team) has to a user-owned visualization using <xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>. You can also retrieve all the security principals (users or teams) that have access to a user-owned visualization, along with their access rights to the user-owned visualization using the <xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>.  
  
- Collaborate with other users and teams on specific areas by sharing a user-owned visualization with them using <xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>, <xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>, and <xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>.  
  
  For a list of supported messages on the user-owned visualization entity, see [UserQueryVisualization Entity](../common-data-service/reference/entities/userqueryvisualization.md).

### See also  
 [Charts](view-data-with-visualizations-charts.md)   
 [Understanding Charts: Underlying Data and Chart Representation](understand-charts-underlying-data-chart-representation.md)   
 [Create a Chart](create-visualization-chart.md)   
 [Sample Charts](sample-charts.md)   
 [Sample: Create, Retrieve, Update, and Delete (CRUD) a Chart](/dynamics365/customer-engagement/developer/customize-dev/sample-create-retrieve-update-delete-chart)  <!--TODO: Need to find the topic in Powerapps repo to link --> 
 [Sample: Retrieve all Charts Attached to an Entity](/dynamics365/customer-engagement/developer/customize-dev/sample-retrieve-all-charts-attached-entity)   <!--TODO: Need to find the topic in Powerapps repo to link -->
 [Sample: Assign a Chart to Another User](/dynamics365/customer-engagement/developer/customize-dev/sample-assign-chart-another-user)   <!--TODO: Need to find the topic in Powerapps repo to link -->
 [SavedQueryVisualization Entity](../common-data-service/reference/entities/savedqueryvisualization.md)   
 [UserQueryVisualization Entity](../common-data-service/reference/entities/userqueryvisualization.md)