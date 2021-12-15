---
title: "Customize table definitions (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Tables are defined by table definitions. By defining or changing the table definitions, you can control the capabilities of a table." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/12/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Customize table definitions

Tables are defined by table definitions. By defining or changing the table definitions, you can control the capabilities of a table. To view the table definitions for your environment, use the metadata browser. [Download the table definitions browser](https://download.microsoft.com/download/8/E/3/8E3279FE-7915-48FE-A68B-ACAFB86DA69C/MetadataBrowser_3_0_0_5_managed.zip).

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

More information: [Browse table definitions for your environment](browse-your-metadata.md)  
  
 This topic is about how to work with tables programmatically. See [Create or edit tables (record types)](/dynamics365/customer-engagement/customize/create-edit-entities)  for information about working with tables in the application.  

Tables can be created using either the organization service or the Web API. The following information can be applied to both.

- With the organization service you will use the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata> class. More information: [Create a custom table](/dynamics365/customer-engagement/developer/org-service/create-custom-entity) and [Retrieve, update, and delete tables](/dynamics365/customer-engagement/developer/org-service/retrieve-update-delete-entities)
- With the Web API you will use the <xref:Microsoft.Dynamics.CRM.EntityMetadata> EntityType. More information : [Create and update table definitions using the Web API](/dynamics365/customer-engagement/developer/webapi/create-update-entity-definitions-using-web-api).
 
## Table definitions operations

How you work with table definitions depends on which service you use.

Since the Web API is a RESTful endpoint, it uses a different way to create, retrieve, update, and delete table definitions. Use `POST`, `GET`, `PUT`, and `DELETE` HTTP verbs to work with table definitions entitytypes. More information : [Create and update table definitions using the Web API](/dynamics365/customer-engagement/developer/webapi/create-update-entity-definitions-using-web-api).

One exception to this is the <xref href="Microsoft.Dynamics.CRM.RetrieveMetadataChanges?text=RetrieveMetadataChanges Function" /> provides a way to compose table definitions query and track changes over time. 

If working with Organization Service, use <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest> class. This class contains the data that is needed to retrieve a collection of table definitions records that satisfy the specified criteria. The <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesResponse> returns a timestamp value that can be used with this request at a later time to return information about how table definitions has changed since the last request.
   

|                                                                                                                                                                          Message                                                                                                                                                                           |                                               Web API                                                |                           SDK Assembly                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
|                                                                                                                                                                        CreateEntity                                                                                                                                                                        |                         Use a POST request to send data to create a table.                         |      <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest>       |
|                                                                                                                                                                        DeleteEntity                                                                                                                                                                        |                              Use a DELETE request to delete a table.                               |      <xref:Microsoft.Xrm.Sdk.Messages.DeleteEntityRequest>       |
|                                                                                                                                                                    RetrieveAllEntities                                                                                                                                                                     |                               Use GET request to retrieve table data.                               |   <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllEntitiesRequest>   |
|                                                                                                                                                                       RetrieveEntity                                                                                                                                                                       |          <xref href="Microsoft.Dynamics.CRM.RetrieveEntity?text=RetrieveEntity Function" />          |     <xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityRequest>      |
|                                                                                                                                                                        UpdateEntity                                                                                                                                                                        |                                Use a PUT request to update a table.                                |      <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest>       |
| RetrieveMetadataChanges</br>Used together with objects in the <xref:Microsoft.Xrm.Sdk.Metadata.Query> namespace to create a query to efficiently retrieve and detect changes to specific table definitions. More information: [Retrieve and Detect Changes to Metadata](/dynamics365/customer-engagement/developer/retrieve-detect-changes-metadata). | <xref href="Microsoft.Dynamics.CRM.RetrieveMetadataChanges?text=RetrieveMetadataChanges Function" /> | <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest> |


## Options available when you create a custom table  

 The following lists the options that are available when you create a custom table. You can only set these properties when you create a custom table.  

|Option|Description|  
|------------|-----------------|  
|**Create as custom activity**|You can create a table that is an activity by setting the `IsActivity` property when using the organization service or Web API respectively. For more information, see [Custom Activities in Dynamics 365](custom-activities.md).|  
|**Table Names**|There are two types of names, and both must have a customization prefix:<br /><br /> `LogicalName`: Name that is the version of the table name that is set in all lowercase letters.<br /><br /> `SchemaName`: Name that will be used to create the database tables. This name can be mixed case. The casing that you use sets the name of the object generated for programming with strong types or when you use the REST endpoint.<br /><br /> **Note**: If the logical name differs from the schema name, the schema name will override the value that you set for the logical name.<br /><br /> When a table is created in the application in the context of a specific solution, the customization prefix used is the one set for the `Publisher` of the solution. When a table is created programmatically, you can set the customization prefix to a string that is between two and eight characters in length, all alphanumeric characters and it must start with a letter. It cannot start with “mscrm”. The best practice is to use the customization prefix defined by the publisher that the solution is associated with, but this is not a requirement. An underscore character must be included between the customization prefix and the logical or schema name.|  
|**Ownership**|Use the `OwnershipType` property to set this. Use the <xref:Microsoft.Xrm.Sdk.Metadata.OwnershipTypes> enumeration or <xref:Microsoft.Dynamics.CRM.OwnershipTypes> EnumType to set the type of table ownership. The only valid values for custom tables are `OrgOwned` or `UserOwned`. For more information, see [Table Ownership](/dynamics365/customer-engagement/developer/introduction-entities#EntityOwnership).|  
|**Primary Column**|With the Organization service, use <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest>.<xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest.PrimaryAttribute> property to set this.<br /><br />With the Web API the JSON defining the table must include one <xref:Microsoft.Dynamics.CRM.StringAttributeMetadata> with the `IsPrimaryName` property set to true.<br /><br /> In both cases string column must be formatted as `Text`. The value of this column is what is shown in a lookup for any related tables. Therefore, the value of the column should represent a name for the record.|  

## Enable table capabilities  

 The following lists table capabilities. You can set these capabilities when you create a table or you can enable them later. Once enabled, these capabilities cannot be disabled.  

|Capability|Description|  
|----------------|-----------------|  
|**Business Process flows**|Set `IsBusinessProcessEnabled` to true in order to enable the table for business process flows.|  
|**Notes**| To create a relationship with the `Annotation` table and enable the inclusion of a **Notes** area in the form. By including **Notes**, you can also add attachments to records. <br /><br />With the Organization service, use the <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest> or <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest> `HasNotes` property <br /><br />With the Web API set the <xref:Microsoft.Dynamics.CRM.EntityMetadata>.`HasNotes` property.|  
|**Activities**|To create a relationship with the `ActivityPointer` table so that all the activity type tables can be associated with this table.<br /><br /> With the Organization service  use the <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest> or <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest> `HasActivities` property. <br /><br /> With the Web API, set the  <xref:Microsoft.Dynamics.CRM.EntityMetadata>.`HasActivities` property.| 
|**Connections**|To enable creating connection records to associate this table with other connection tables set the `IsConnectionsEnabled.Value` property value to true.|  
|**Queues**|Use the `IsValidForQueue` property to add support for queues. When you enable this option, you can also set the `AutoRouteToOwnerQueue` property to automatically move records to the owner’s default queue when a record of this type is created or assigned.|  
|**E-mail**|Set the `IsActivityParty` property so that you can send e-mail to an e-mail address in this type of record.|  

## Editable table properties
  
 The following lists table properties that you can edit. Unless a managed property disallows these options, you can update them at any time.  


|                                        Property                                        |                                                                                                                                                                                                     Description                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                 **Allow Quick Create**                                 |                                                                                   Use `IsQuickCreateEnabled` to enable quick create forms for the table. Before you can use quick create forms you must first create and publish a quick create form.<br /> **Note**:<br /> Activity tables do not support quick create forms.                                                                                   |
|                                    **Access Teams**                                    |                                                                                                                                Use `AutoCreateAccessTeams` to enable the table for access teams. See [About team templates](/dynamics365/customer-engagement/admin/about-team-templates) for more information.                                                                                                                                |
|                                   **Primary Image**                                    |                                                                                             If a table has an image column you can enable or disable displaying that image in the application using `PrimaryImageAttribute`. For more information see [Entity Images](/dynamics365/customer-engagement/developer/introduction-entities).                                                                                             |
|                                **Change display text**                                 |                                                                                             The managed property `IsRenameable` prevents the display name from being changed in the application. You can still programmatically change the labels by updating the `DisplayName` and `DisplayCollectionName` properties.                                                                                             |
|                            **Edit the table Description**                             |                                                                                                         The managed property `IsRenameable` prevents the table description from being changed in the application. You can still programmatically change the labels by updating the `Description` property.                                                                                                         |
|                            **Enable for use while offline**                            |                                                                                                          Use `IsAvailableOffline` to enable or disable the ability of Dynamics 365 for Microsoft Office Outlook with Offline Access users to take data for this table offline.                                                                                                           |
|                          **Enable the Outlook Reading Pane**                           | **Note**:<br /><br /> The `IsReadingPaneEnabled` property is for internal use only.<br /><br /> To enable or disable the ability of Office Outlook users to view data for this table, use the Outlook reading pane. You must set this property in the application. |
|                                 **Enable Mail Merge**                                  |                                                                                                                 Use `IsMailMergeEnabled` to enable or disable the ability to generate Office Word merged documents that use data from this table.                                                                                                                  |
|                             **Enable Duplicate Detection**                             |                                                                                                       Use `IsDuplicateDetectionEnabled` to enable or disable duplicate detection for the table. For more information, see [Detect Duplicate Data in Dynamics 365](/dynamics365/customer-engagement/developer/detect-duplicate-data-for-developers).                                                                                                        |
|                           **Enable SharePoint Integration**                            |                                                          Use `IsDocumentManagementEnabled` to enable or disable SharePoint server integration for the table. For more information, see [Enable Document Management for tables](/dynamics365/customer-engagement/developer/integration-dev/enable-document-management-entities).                                                          |
| **Enable Dynamics 365 for phones** |                                                                                                                      Use `IsVisibleInMobile` to enable or disable the ability of Dynamics 365 for phones users to see data for this table.                                                                                                                       |
|              **Dynamics 365 for tablets**               |                             Use `IsVisibleInMobileClient` to enable or disable the ability of Dynamics 365 for tablets users to see data for this table.<br /><br /> If the table is available for Dynamics 365 for tablets you can use `IsReadOnlyInMobileClient` to specify that the data for the record is read-only.                              |
|                                  **Enable Auditing**                                   |                                                                                                              Use `IsAuditEnabled` to enable or disable auditing for the table. For more information, see [Configure table and columns for Auditing](configure-entities-attributes-auditing.md).                                                                                                              |
|                        **Change areas that display the table**                        |                                                                                                                                                  You can control where table grids appear in the application Navigation Pane. This is controlled by the SiteMap.                                                                                                                                                   |
|                              **Add or Remove Columns**                              |                                                                                     As long as the managed property `CanCreateAttributes.Value` allows for creating columns, you can add columns to the table. For more information, see [Customize table definitions](/dynamics365/customer-engagement/developer/customize-entity-attribute-metadata).                                                                                      |
|                                **Add or Remove Views**                                 |                                                                                                                                As long as the managed property `CanCreateViews.Value` allows for creating views, you can use the `SavedQuery` table to create views for a table.                                                                                                                                 |
|                                **Add or Remove Charts**                                |              As long as the managed property `CanCreateCharts.Value` allows for creating charts and the `IsEnabledForCharts` table property is true, you can use the [SavedQueryVisualization table](/reference/entities/savedqueryvisualization.md) to create charts for a table. For more information, see [View Data with Visualizations (Charts)](/dynamics365/customer-engagement/developer/customize-dev/view-data-with-visualizations-charts).              |
|                         **Add or Remove table relationships**                         |                                                                                        There are several managed properties that control the types of relationships that you can create for a table. For more information, see [Customize table relationship definitions](/dynamics365/customer-engagement/developer/customize-entity-relationship-metadata).                                                                                        |
|                                    **Change Icons**                                    |                                                                                                                                             You can change the icons used for custom tables. For more information, see [Modify Icons](/dynamics365/customer-engagement/developer/modify-icons-entity).                                                                                                                                             |
|                        **Can Change Hierarchical Relationship**                        |                                                                                        `CanChangeHierarchicalRelationship.Value` controls whether the hierarchical state of relationships included in your managed solutions can be changed. More information:                                                                                         |
  


## Messages supported by custom tables  

 Custom tables support the same base messages as system tables. The set of messages available depends on whether the custom table is user-owned or organization owned. For more information, see [Actions on Records](/dynamics365/customer-engagement/developer/introduction-entities#ActionsOnEntityRecords).  
  
### See also
  
[Use the Web API with table definitions](webapi/use-web-api-metadata.md)

[Work with table definitions using the Organization service](org-service/work-with-metadata.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]