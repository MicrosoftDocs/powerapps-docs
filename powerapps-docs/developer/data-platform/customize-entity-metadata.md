---
title: "Customize Table Definitions (Microsoft Dataverse) | Microsoft Docs"
description: "Learn how to customize Microsoft Dataverse table definitions with the SDK for .NET or Web API to control table capabilities and editable properties." 
ms.date: 08/07/2026
ms.reviewer: pehecke
ms.topic: article
author: MsSQLGirl
ms.author: jukoesma
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
---
# Customize table definitions

By defining or changing the table definitions, you can control the capabilities of a table. To view the table definitions for your environment, use the metadata browser. [Browse table definitions in your environment](browse-your-metadata.md).

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]
  
This article explains how to work with tables programmatically. To work with tables in [Power Apps](https://make.powerapps.com), see [Tables in Dataverse](../../maker/data-platform/entity-overview.md).

You can create tables by using the SDK for .NET, the Dataverse SDK for Python, or the Web API. The following information applies to all three methods.

| Method | Interface | Learn more |
| --- | --- | --- |
| Web API | [EntityMetadata entity type](xref:Microsoft.Dynamics.CRM.EntityMetadata) | [Create and update table definitions using the Web API](webapi/create-update-entity-definitions-using-web-api.md) |
| SDK for .NET | [EntityMetadata class](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata) | [Create a custom table using code](org-service/create-custom-entity.md)<br />[Retrieve, update, and delete tables](org-service/metadata-retrieve-update-delete-entities.md) |
| Dataverse SDK for Python | `client.tables` | [Use metadata to customize tables and columns](sdk-python/metadata.md) |

 
## Create, retrieve, update, and delete table definitions

How you work with table definitions depends on which service you use.
   

|Message|Web API|.NET SDK|SDK for Python|
|-------|--------|--------|--------|
|`CreateEntity`|Use a `POST` request to send data to create a table.|[CreateEntityRequest class](xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest)|Use `client.tables.create` to create a custom table and optionally its columns.|
|`DeleteEntity`|Use a `DELETE` request to delete a table.|[DeleteEntityRequest class](xref:Microsoft.Xrm.Sdk.Messages.DeleteEntityRequest)|Use `client.tables.delete` to delete a custom table.|
|`RetrieveAllEntities`|   Use `GET` request to retrieve table data.   |   [RetrieveAllEntitiesRequest class](xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllEntitiesRequest)|Use `client.tables.list` to list table definitions.|
|`RetrieveEntity`|[RetrieveEntity function](xref:Microsoft.Dynamics.CRM.RetrieveEntity)   | [RetrieveEntityRequest class](xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityRequest)|Use `client.tables.get` to retrieve a table definition.|
|`UpdateEntity`|Use a PUT request to update a table.|[UpdateEntityRequest class](xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest)|Not currently supported. The SDK for Python doesn't provide a table update method.|
| `RetrieveMetadataChanges`</br>Used together with objects in the [Metadata.Query namespace](xref:Microsoft.Xrm.Sdk.Metadata.Query) to create a query to efficiently retrieve and detect changes to specific table definitions. More information: [Query schema definitions](query-schema-definitions.md). | [RetrieveMetadataChanges function](xref:Microsoft.Dynamics.CRM.RetrieveMetadataChanges) | [RetrieveMetadataChangesRequest class](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest) | Not currently supported. The SDK for Python doesn't provide a way to invoke this function. |


## Options available when you create a custom table  

 The following list describes the options that are available when you create a custom table. You can set these properties only when you create a custom table.  

|Option|Description|  
|------------|-----------------|  
|**Create as custom activity**|Create a table that is an activity by setting the `IsActivity` property when using the SDK for .NET or Web API respectively. For more information, see [Custom activities](custom-activities.md).|  
|**Table Names**|Two types of names exist. Custom tables must have a customization prefix:<br /><br /> `LogicalName`: Name that is the version of the table name set in all lowercase letters.<br /><br /> `SchemaName`: Name used to create the database tables. This name can be mixed case. The casing that you use sets the name of the object generated for programming with strong types or when you use the REST endpoint.<br /><br /> **Note**: If the logical name differs from the schema name, the schema name overrides the value that you set for the logical name.<br /><br /> When you create a table in the application in the context of a specific solution, the customization prefix used is the one set for the `Publisher` of the solution. When you create a table programmatically, set the customization prefix to a string that is between two and eight characters in length, all alphanumeric characters, and it must start with a letter. It can't start with `mscrm`. The best practice is to use the customization prefix defined by the publisher that the solution is associated with, but this best practice isn't enforced. An underscore character must be included between the customization prefix and the logical or schema name.|  
|**Ownership**|Use the `OwnershipType` property to set how table records are owned. Use the [OwnershipTypes enumeration](xref:Microsoft.Xrm.Sdk.Metadata.OwnershipTypes) or [OwnershipTypes enum type](xref:Microsoft.Dynamics.CRM.OwnershipTypes) to set the type of table ownership. The only valid values for custom tables are `OrgOwned` or `UserOwned`. For more information, see [Table ownership](entity-metadata.md#table-ownership).|
|**Primary Column**|With the SDK for .NET, use the [CreateEntityRequest.PrimaryAttribute property](xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest.PrimaryAttribute) to set the primary column.<br /><br />With the Web API, the JSON defining the table must include one [StringAttributeMetadata entity type](xref:Microsoft.Dynamics.CRM.StringAttributeMetadata) with the `IsPrimaryName` property set to true.<br /><br /> In both cases, string column must be formatted as `Text`. The value of the primary column is what is shown in a lookup for any related tables. Therefore, the value of the column should represent a name for the record.|  

## Enable table capabilities  

The following list describes table capabilities. You can set these capabilities when you create a table or enable them later. 

> [!NOTE]
> You can't disable these capabilities once you enable them.

|Capability|Description|  
|----------|-----------|  
|**Business Process flows**|Set `IsBusinessProcessEnabled` to true to enable the table for business process flows.|  
|**Notes**| Create a relationship with the `Annotation` table and enable the inclusion of a **Notes** area in the form. By including **Notes**, you can also add attachments to records. <br /><br />By using the SDK for .NET, use the [CreateEntityRequest](xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest) or [UpdateEntityRequest](xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest) `HasNotes` property <br /><br />By using the Web API, set the [EntityMetadata](xref:Microsoft.Dynamics.CRM.EntityMetadata)`.HasNotes` property|  
|**Activities**| Create a relationship with the `ActivityPointer` table so that all the activity type tables can be associated with this table.<br /><br /> By using the SDK for .NET, use the [CreateEntityRequest](xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest) or [UpdateEntityRequest](xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest) `HasActivities` property. <br /><br /> By using the Web API, set the [EntityMetadata](xref:Microsoft.Dynamics.CRM.EntityMetadata)`.HasActivities` property| 
|**Connections**| Set the `IsConnectionsEnabled.Value` property to true to enable creating connection records to associate this table with other connection tables. To learn more about connections, see [Configure connection roles](../../maker/data-platform/configure-connection-roles.md) and [Use connections to link records to each other](connection-entities.md).| 
|**Queues**|Use the `IsValidForQueue` property to add support for queues. When you enable this option, you can also set the `AutoRouteToOwnerQueue` property to automatically move records to the owner's default queue when a record of this type is created or assigned. To learn more, see [Learn more about queues](/dynamics365/customer-service/use/work-with-queues) and [queue tables](queue-entities.md).|  
|**E-mail**|Set the `IsActivityParty` property so that you can send e-mail to an e-mail address in this type of record. [Learn more about activity parties](activityparty-entity.md). |  

## Editable table properties
  
 The following list shows table properties that you can edit. Unless a [managed property](/power-platform/alm/managed-properties-alm) disallows these options, you can update them at any time.  [Learn more about managed properties](/power-platform/alm/use-managed-properties)


|Property | Description |
|--------|--------------|
|**Allow Quick Create**|Use `IsQuickCreateEnabled` to enable quick create forms for the table. Before you can use quick create forms, you must first create and publish a quick create form. [Learn more about model-driven app quick create forms](../../maker/model-driven-apps/create-edit-quick-create-forms.md)<br /> **Note**:<br /> Activity tables don't support quick create forms.      |
|**Access Teams**|  Use `AutoCreateAccessTeams` to enable the table for access teams. See [About collaborating with team templates](/power-platform/admin/about-team-templates) for more information.  |
|**Primary Image** |  If a table has an image column, you can enable or disable displaying that image in the application by using `PrimaryImageAttribute`. [Learn to work with image column definitions using code](image-attributes.md)|
|**Change display text**|  The [managed property](/power-platform/alm/managed-properties-alm) `IsRenameable` prevents the display name from being changed in the application. You can still programmatically change the labels by updating the `DisplayName` and `DisplayCollectionName` properties.  |
|**Edit the table Description** |The [managed property](/power-platform/alm/managed-properties-alm) `IsRenameable` prevents the table description from being changed in the application. You can still programmatically change the labels by updating the `Description` property.|
|**Enable the Outlook Reading Pane**      | **Note**:The `IsReadingPaneEnabled` property is for internal use only.<br /><br /> To enable or disable the ability of Office Outlook users to view data for this table, use the Outlook reading pane. You must set this property in the application. |
|**Enable Mail Merge**| Use `IsMailMergeEnabled` to enable or disable the ability to generate Office Word merged documents that use data from this table.  |
|**Enable Duplicate Detection**|Use `IsDuplicateDetectionEnabled` to enable or disable duplicate detection for the table. For more information, see [Detect duplicate data using code](detect-duplicate-data-with-code.md)|
|**Enable SharePoint Integration**|  Use `IsDocumentManagementEnabled` to enable or disable SharePoint server integration for the table. For more information, see [Enable SharePoint document management for specific entities](/power-platform/admin/enable-sharepoint-document-management-specific-entities).  |
|**Enable Dynamics 365 for phones**| Use `IsVisibleInMobile` to enable or disable the ability of Dynamics 365 for phones users to see data for this table.|
|**Dynamics 365 for tablets** | Use `IsVisibleInMobileClient` to enable or disable the ability of Dynamics 365 for tablets users to see data for this table.<br /><br /> If the table is available for Dynamics 365 for tablets, you can use `IsReadOnlyInMobileClient` to specify that the data for the record is read-only.  |
|**Enable Auditing**| Use `IsAuditEnabled` to enable or disable auditing for the table. For more information, see [Configure table and columns for Auditing](auditing/configure.md#configure-tables-and-columns).|
|**Add or Remove Columns**| As long as the [managed property](/power-platform/alm/managed-properties-alm) `CanCreateAttributes.Value` allows for creating columns, you can add columns to the table. For more information, see [Column definitions](entity-attribute-metadata.md).  |
|**Add or Remove Views**|  As long as the [managed property](/power-platform/alm/managed-properties-alm) `CanCreateViews.Value` allows for creating views, you can use the `SavedQuery` table to create views for a table.|
|**Add or Remove Charts**|As long as the [managed property](/power-platform/alm/managed-properties-alm) `CanCreateCharts.Value` allows for creating charts and the `IsEnabledForCharts` table property is true, you can use the [SavedQueryVisualization table](reference/entities/savedqueryvisualization.md) to create charts for a table. For more information, see [View data with visualizations (charts)](../model-driven-apps/view-data-with-visualizations-charts.md).|
|**Add or Remove table relationships** |Several managed properties control the types of relationships that you can create for a table. For more information, see [Table relationship definitions](entity-relationship-metadata.md).|
|**Change Icons** | You can change the icons used for custom tables. For more information, see [Change model-driven app custom table icons](../../maker/model-driven-apps/change-custom-entity-icons.md)|
|**Can Change Hierarchical Relationship** |`CanChangeHierarchicalRelationship.Value` controls whether the hierarchical state of relationships included in your managed solutions can be changed. Learn more: [Define and query hierarchically related data](../../maker/data-platform/define-query-hierarchical-data.md) and [Query hierarchical data](query-hierarchical-data.md)|
|**Entity set name**|`EntitySetName` specifies the name used to uniquely identify the table by using the Dataverse Web API. This name is usually the same as the `LogicalCollectionName`, but you can't change the `LogicalCollectionName`. You should only change `EntitySetName` before any code is written using the default entity set name. [Learn more about entity set names](webapi/web-api-service-documents.md#entity-set-name) |

## Messages supported by custom tables  

Custom tables support the same base messages as system tables. The set of messages you can use depends on whether the custom table is user-owned or organization owned. User-owned tables support sharing, so you can use messages such as `GrantAccess`, `ModifyAccess`, and `RevokeAccess`.
  
### See also
  
[Use the Web API with table definitions](webapi/use-web-api-metadata.md)<br />
[Work with table definitions using the SDK for .NET](org-service/work-with-metadata.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
