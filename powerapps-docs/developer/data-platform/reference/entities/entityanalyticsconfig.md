---
title: "Entity Analytics Config (EntityAnalyticsConfig) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Entity Analytics Config (EntityAnalyticsConfig) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Entity Analytics Config (EntityAnalyticsConfig) table/entity reference (Microsoft Dataverse)

This entity contains information about which entities are enabled for Azure Data Lake Services integration

## Messages

The following table lists the messages for the Entity Analytics Config (EntityAnalyticsConfig) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /entityanalyticsconfigs<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: False |`DELETE` /entityanalyticsconfigs(*entityanalyticsconfigid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /entityanalyticsconfigs(*entityanalyticsconfigid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /entityanalyticsconfigs<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /entityanalyticsconfigs(*entityanalyticsconfigid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /entityanalyticsconfigs(*entityanalyticsconfigid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Entity Analytics Config (EntityAnalyticsConfig) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Entity Analytics Config** |
| **DisplayCollectionName** | **Entity Analytics Config** |
| **SchemaName** | `EntityAnalyticsConfig` |
| **CollectionSchemaName** | `EntityAnalyticsConfigs` |
| **EntitySetName** | `entityanalyticsconfigs`|
| **LogicalName** | `entityanalyticsconfig` |
| **LogicalCollectionName** | `entityanalyticsconfigs` |
| **PrimaryIdAttribute** | `entityanalyticsconfigid` |
| **PrimaryNameAttribute** |`parententitylogicalname` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [EntityAnalyticsConfigId](#BKMK_EntityAnalyticsConfigId)
- [EntityDataSource](#BKMK_EntityDataSource)
- [IsEnabledForADLS](#BKMK_IsEnabledForADLS)
- [IsEnabledForTimeSeries](#BKMK_IsEnabledForTimeSeries)
- [ParentEntityId](#BKMK_ParentEntityId)
- [ParentEntityLogicalName](#BKMK_ParentEntityLogicalName)

### <a name="BKMK_EntityAnalyticsConfigId"></a> EntityAnalyticsConfigId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Entity Analytics Config**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityanalyticsconfigid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_EntityDataSource"></a> EntityDataSource

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Entity Data Source**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entitydatasource`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`entityanalyticsconfig_entitydatasourcee`|

#### EntityDataSource Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Dataverse**|
|2|**FnOTables**|

### <a name="BKMK_IsEnabledForADLS"></a> IsEnabledForADLS

|Property|Value|
|---|---|
|Description|**Azure Data Lake Storage is enabled for the selected entity**|
|DisplayName|**Is Enabled For ADLS**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isenabledforadls`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`none_entityanalyticsconfig_isenabledforadls`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsEnabledForTimeSeries"></a> IsEnabledForTimeSeries

|Property|Value|
|---|---|
|Description|**Time series is enabled for the selected entity**|
|DisplayName|**Is Enabled For Time Series**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isenabledfortimeseries`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`entityanalyticsconfig_isenabledfortimeseries`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ParentEntityId"></a> ParentEntityId

|Property|Value|
|---|---|
|Description|**Unique identifier for Entity associated with Entity Analytics Config.**|
|DisplayName|**Parent Entity Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parententityid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|entity|

### <a name="BKMK_ParentEntityLogicalName"></a> ParentEntityLogicalName

|Property|Value|
|---|---|
|Description|**Entity Logical Name For Analytics**|
|DisplayName|**Entity Logical Name For Analytics**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parententitylogicalname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedOn](#BKMK_CreatedOn)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedOn](#BKMK_ModifiedOn)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentIdUnique"></a> ComponentIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Row id unique**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Component State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentstate`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`componentstate`|

#### ComponentState Choices/Options

|Value|Label|
|---|---|
|0|**Published**|
|1|**Unpublished**|
|2|**Deleted**|
|3|**Deleted Unpublished**|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was created.**|
|DisplayName|**Created On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Indicates whether the solution component is part of a managed solution.**|
|DisplayName|**Is Managed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier for the organization**|
|DisplayName|**Organization Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Record Overwrite Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overwritetime`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the associated solution.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`supportingsolutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of Entity Analytics Config.**|
|DisplayName|**Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [entity_entityanalyticsconfig](#BKMK_entity_entityanalyticsconfig)
- [organization_entityanalyticsconfig](#BKMK_organization_entityanalyticsconfig)

### <a name="BKMK_entity_entityanalyticsconfig"></a> entity_entityanalyticsconfig

One-To-Many Relationship: [entity entity_entityanalyticsconfig](entity.md#BKMK_entity_entityanalyticsconfig)

|Property|Value|
|---|---|
|ReferencedEntity|`entity`|
|ReferencedAttribute|`entityid`|
|ReferencingAttribute|`parententityid`|
|ReferencingEntityNavigationPropertyName|`parententityid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_organization_entityanalyticsconfig"></a> organization_entityanalyticsconfig

One-To-Many Relationship: [organization organization_entityanalyticsconfig](organization.md#BKMK_organization_entityanalyticsconfig)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [entityanalyticsconfig_AsyncOperations](#BKMK_entityanalyticsconfig_AsyncOperations)
- [entityanalyticsconfig_BulkDeleteFailures](#BKMK_entityanalyticsconfig_BulkDeleteFailures)
- [entityanalyticsconfig_MailboxTrackingFolders](#BKMK_entityanalyticsconfig_MailboxTrackingFolders)
- [entityanalyticsconfig_PrincipalObjectAttributeAccesses](#BKMK_entityanalyticsconfig_PrincipalObjectAttributeAccesses)
- [entityanalyticsconfig_SyncErrors](#BKMK_entityanalyticsconfig_SyncErrors)

### <a name="BKMK_entityanalyticsconfig_AsyncOperations"></a> entityanalyticsconfig_AsyncOperations

Many-To-One Relationship: [asyncoperation entityanalyticsconfig_AsyncOperations](asyncoperation.md#BKMK_entityanalyticsconfig_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`entityanalyticsconfig_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_entityanalyticsconfig_BulkDeleteFailures"></a> entityanalyticsconfig_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure entityanalyticsconfig_BulkDeleteFailures](bulkdeletefailure.md#BKMK_entityanalyticsconfig_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`entityanalyticsconfig_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_entityanalyticsconfig_MailboxTrackingFolders"></a> entityanalyticsconfig_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder entityanalyticsconfig_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_entityanalyticsconfig_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`entityanalyticsconfig_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_entityanalyticsconfig_PrincipalObjectAttributeAccesses"></a> entityanalyticsconfig_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess entityanalyticsconfig_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_entityanalyticsconfig_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`entityanalyticsconfig_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_entityanalyticsconfig_SyncErrors"></a> entityanalyticsconfig_SyncErrors

Many-To-One Relationship: [syncerror entityanalyticsconfig_SyncErrors](syncerror.md#BKMK_entityanalyticsconfig_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`entityanalyticsconfig_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.entityanalyticsconfig?displayProperty=fullName>
