---
title: "Customize table definitions (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "By defining or changing the table definitions, you can control the capabilities of a table." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 09/04/2022
ms.reviewer: pehecke
ms.topic: article
author: mkannapiran
ms.author: kamanick
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
---
# Customize table definitions

By defining or changing the table definitions, you can control the capabilities of a table. To view the table definitions for your environment, use the metadata browser. [Browse table definitions in your environment](browse-your-metadata.md).

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

More information: [Browse table definitions for your environment](browse-your-metadata.md)  
  
This article is about how to work with tables programmatically. To work with tables in [Power Apps](https://make.powerapps.com) See [Tables in Dataverse](../../maker/data-platform/entity-overview.md).

Tables can be created using either the SDK for .NET or the Web API. The following information can be applied to both.

- With the SDK for .NET, use the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata> class. More information: [Create a custom table using code](org-service/create-custom-entity.md) and [Retrieve, update, and delete tables](org-service/metadata-retrieve-update-delete-entities.md)
- With the Web API, use the <xref:Microsoft.Dynamics.CRM.EntityMetadata> EntityType. [Learn to create and update table definitions using the Web API](webapi/create-update-entity-definitions-using-web-api.md)
 
## Table definitions operations

How you work with table definitions depends on which service you use.

Since the Web API is a RESTful endpoint, it uses a different way to create, retrieve, update, and delete table definitions. Use `POST`, `GET`, `PUT`, and `DELETE` HTTP verbs to work with table definitions entity types. [Learn to create and update table definitions using the Web API](webapi/create-update-entity-definitions-using-web-api.md)

One exception to this is the <xref:Microsoft.Dynamics.CRM.RetrieveMetadataChanges?text=RetrieveMetadataChanges Function> provides a way to compose table definitions query and track changes over time.

If working with SDK for .NET, use <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest> class. This class contains the data that is needed to retrieve a collection of table definitions records that satisfy the specified criteria. The <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesResponse> returns a timestamp value that can be used with this request at a later time to return information about how table definitions changed since the last request.
   

|Message|Web API|SDK Assembly|
|-------|--------|--------|
|`CreateEntity`|Use a POST request to send data to create a table.|<xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest>|
|`DeleteEntity`|Use a DELETE request to delete a table.|<xref:Microsoft.Xrm.Sdk.Messages.DeleteEntityRequest>|
|`RetrieveAllEntities`|   Use GET request to retrieve table data.   |   <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllEntitiesRequest>|
|`RetrieveEntity`|<xref:Microsoft.Dynamics.CRM.RetrieveEntity?text=RetrieveEntity Function>   | <xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityRequest>|
|`UpdateEntity`|Use a PUT request to update a table.|<xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest>|
| `RetrieveMetadataChanges`</br>Used together with objects in the <xref:Microsoft.Xrm.Sdk.Metadata.Query> namespace to create a query to efficiently retrieve and detect changes to specific table definitions. More information: [Retrieve and detect changes to table definitions](org-service/metadata-retrieve-detect-changes.md). | <xref:Microsoft.Dynamics.CRM.RetrieveMetadataChanges?text=RetrieveMetadataChanges Function> | <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest> |


## Options available when you create a custom table  

 The following lists the options that are available when you create a custom table. You can only set these properties when you create a custom table.  

|Option|Description|  
|------------|-----------------|  
|**Create as custom activity**|You can create a table that is an activity by setting the `IsActivity` property when using the SDK for .NET or Web API respectively. For more information, see [Custom Activities in Dynamics 365](custom-activities.md).|  
|**Table Names**|There are two types of names, and both must have a customization prefix:<br /><br /> `LogicalName`: Name that is the version of the table name that is set in all lowercase letters.<br /><br /> `SchemaName`: Name used to create the database tables. This name can be mixed case. The casing that you use sets the name of the object generated for programming with strong types or when you use the REST endpoint.<br /><br /> **Note**: If the logical name differs from the schema name, the schema name overrides the value that you set for the logical name.<br /><br /> When a table is created in the application in the context of a specific solution, the customization prefix used is the one set for the `Publisher` of the solution. When a table is created programmatically, you can set the customization prefix to a string that is between two and eight characters in length, all alphanumeric characters and it must start with a letter. It can't start with `mscrm`. The best practice is to use the customization prefix defined by the publisher that the solution is associated with, but this best practice isn't enforced. An underscore character must be included between the customization prefix and the logical or schema name.|  
|**Ownership**|Use the `OwnershipType` property to set how table records are owned. Use the <xref:Microsoft.Xrm.Sdk.Metadata.OwnershipTypes> enumeration or <xref:Microsoft.Dynamics.CRM.OwnershipTypes> EnumType to set the type of table ownership. The only valid values for custom tables are `OrgOwned` or `UserOwned`. For more information, see [Table ownership](entity-metadata.md#table-ownership).|  
|**Primary Column**|With the SDK for .NET, use <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest>.<xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest.PrimaryAttribute> property to set the primary column.<br /><br />With the Web API, the JSON defining the table must include one <xref:Microsoft.Dynamics.CRM.StringAttributeMetadata> with the `IsPrimaryName` property set to true.<br /><br /> In both cases, string column must be formatted as `Text`. The value of the primary column is what is shown in a lookup for any related tables. Therefore, the value of the column should represent a name for the record.|  

## Enable table capabilities  

 The following lists table capabilities. You can set these capabilities when you create a table or you can enable them later. Once enabled, these capabilities can't be disabled.  

|Capability|Description|  
|----------|-----------|  
|**Business Process flows**|Set `IsBusinessProcessEnabled` to true in order to enable the table for business process flows.|  
|**Notes**| To create a relationship with the `Annotation` table and enable the inclusion of a **Notes** area in the form. By including **Notes**, you can also add attachments to records. <br /><br />With the SDK for .NET, use the <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest> or <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest> `HasNotes` property <br /><br />With the Web API, set the <xref:Microsoft.Dynamics.CRM.EntityMetadata>.`HasNotes` property.|  
|**Activities**|To create a relationship with the `ActivityPointer` table so that all the activity type tables can be associated with this table.<br /><br /> With the SDK for .NET,  use the <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest> or <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest> `HasActivities` property. <br /><br /> With the Web API, set the  <xref:Microsoft.Dynamics.CRM.EntityMetadata>.`HasActivities` property.| 
|**Connections**|To enable creating connection records to associate this table with other connection tables set the `IsConnectionsEnabled.Value` property value to true.|  
|**Queues**|Use the `IsValidForQueue` property to add support for queues. When you enable this option, you can also set the `AutoRouteToOwnerQueue` property to automatically move records to the owner's default queue when a record of this type is created or assigned.|  
|**E-mail**|Set the `IsActivityParty` property so that you can send e-mail to an e-mail address in this type of record.|  

## Editable table properties
  
 The following lists table properties that you can edit. Unless a managed property disallows these options, you can update them at any time.  


|Property | Description |
|--------|--------------|
|**Allow Quick Create**|Use `IsQuickCreateEnabled` to enable quick create forms for the table. Before you can use quick create forms, you must first create and publish a quick create form.<br /> **Note**:<br /> Activity tables don't support quick create forms.      |
|**Access Teams**|  Use `AutoCreateAccessTeams` to enable the table for access teams. See [About collaborating with team templates](/power-platform/admin/about-team-templates) for more information.  |
|**Primary Image** |  If a table has an image column, you can enable or disable displaying that image in the application using `PrimaryImageAttribute`. [Learn to work with image column definitions using code](image-attributes.md)|
|**Change display text**|  The managed property `IsRenameable` prevents the display name from being changed in the application. You can still programmatically change the labels by updating the `DisplayName` and `DisplayCollectionName` properties.  |
|**Edit the table Description** |The managed property `IsRenameable` prevents the table description from being changed in the application. You can still programmatically change the labels by updating the `Description` property.|
|**Enable for use while offline**| Use `IsAvailableOffline` to enable or disable the ability of Dynamics 365 for Microsoft Office Outlook with Offline Access users to take data for this table offline.  |
|**Enable the Outlook Reading Pane**      | **Note**:<br /><br /> The `IsReadingPaneEnabled` property is for internal use only.<br /><br /> To enable or disable the ability of Office Outlook users to view data for this table, use the Outlook reading pane. You must set this property in the application. |
|**Enable Mail Merge**| Use `IsMailMergeEnabled` to enable or disable the ability to generate Office Word merged documents that use data from this table.  |
|**Enable Duplicate Detection**|Use `IsDuplicateDetectionEnabled` to enable or disable duplicate detection for the table. For more information, see [Detect duplicate data using code](detect-duplicate-data-with-code.md)|
|**Enable SharePoint Integration**|  Use `IsDocumentManagementEnabled` to enable or disable SharePoint server integration for the table. For more information, see [Enable SharePoint document management for specific entities](/power-platform/admin/enable-sharepoint-document-management-specific-entities).  |
|**Enable Dynamics 365 for phones**| Use `IsVisibleInMobile` to enable or disable the ability of Dynamics 365 for phones users to see data for this table.|
|**Dynamics 365 for tablets** | Use `IsVisibleInMobileClient` to enable or disable the ability of Dynamics 365 for tablets users to see data for this table.<br /><br /> If the table is available for Dynamics 365 for tablets, you can use `IsReadOnlyInMobileClient` to specify that the data for the record is read-only.  |
|**Enable Auditing**| Use `IsAuditEnabled` to enable or disable auditing for the table. For more information, see [Configure table and columns for Auditing](auditing/configure.md#configure-tables-and-columns).|
|**Change areas that display the table**|      You can control where table grids appear in the application Navigation Pane. This is controlled by the SiteMap.|
|**Add or Remove Columns**| As long as the managed property `CanCreateAttributes.Value` allows for creating columns, you can add columns to the table. For more information, see [Column definitions](entity-attribute-metadata.md).  |
|**Add or Remove Views**|  As long as the managed property `CanCreateViews.Value` allows for creating views, you can use the `SavedQuery` table to create views for a table.|
|**Add or Remove Charts**|As long as the managed property `CanCreateCharts.Value` allows for creating charts and the `IsEnabledForCharts` table property is true, you can use the [SavedQueryVisualization table](reference/entities/savedqueryvisualization.md) to create charts for a table. For more information, see [View data with visualizations (charts)](../model-driven-apps/view-data-with-visualizations-charts.md).|
|**Add or Remove table relationships** |There are several managed properties that control the types of relationships that you can create for a table. For more information, see [Table relationship definitions](entity-relationship-metadata.md).|
|**Change Icons** | You can change the icons used for custom tables. For more information, see [Change model-driven app custom table icons](../../maker/model-driven-apps/change-custom-entity-icons.md)|
|**Can Change Hierarchical Relationship** |`CanChangeHierarchicalRelationship.Value` controls whether the hierarchical state of relationships included in your managed solutions can be changed.|
|**Entity set name**|`EntitySetName` specifies the name used to uniquely identify the table using the Dataverse Web API. This is usually the same as the `LogicalCollectionName`, but you can't change the `LogicalCollectionName`. You should only change `EntitySetName` before any code is written using the default entity set name. [Learn more about entity set names](webapi/web-api-service-documents.md#entity-set-name) |

## Messages supported by custom tables  

Custom tables support the same base messages as system tables. The set of messages available depends on whether the custom table is user-owned or organization owned. User-owned tables support sharing, so messages such as `GrantAccess`, `ModifyAccess`, and `RevokeAccess` are available.
  
### See also
  
[Use the Web API with table definitions](webapi/use-web-api-metadata.md)<br />
[Work with table definitions using the SDK for .NET](org-service/work-with-metadata.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
