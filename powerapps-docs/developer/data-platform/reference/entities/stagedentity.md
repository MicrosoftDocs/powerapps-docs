---
title: "Staged Entity (StagedEntity) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Staged Entity (StagedEntity) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Staged Entity (StagedEntity) table/entity reference (Microsoft Dataverse)

Stores staged entity metadata to be processed before fully created.

## Messages

The following table lists the messages for the Staged Entity (StagedEntity) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /stagedentities<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /stagedentities(*stagedentityid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /stagedentities(*stagedentityid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /stagedentities<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /stagedentities(*stagedentityid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /stagedentities(*stagedentityid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Staged Entity (StagedEntity) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Staged Entity** |
| **DisplayCollectionName** | **Staged Entities** |
| **SchemaName** | `StagedEntity` |
| **CollectionSchemaName** | `StagedEntities` |
| **EntitySetName** | `stagedentities`|
| **LogicalName** | `stagedentity` |
| **LogicalCollectionName** | `stagedentities` |
| **PrimaryIdAttribute** | `stagedentityid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CollectionName](#BKMK_CollectionName)
- [DataproviderId](#BKMK_DataproviderId)
- [DatasourceId](#BKMK_DatasourceId)
- [EntityDescription](#BKMK_EntityDescription)
- [EntitySetName](#BKMK_EntitySetName)
- [ExternalCollectionName](#BKMK_ExternalCollectionName)
- [ExternalName](#BKMK_ExternalName)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [LogicalCollectionName](#BKMK_LogicalCollectionName)
- [LogicalName](#BKMK_LogicalName)
- [Name](#BKMK_Name)
- [OriginalLocalizedCollectionName](#BKMK_OriginalLocalizedCollectionName)
- [OriginalLocalizedDescription](#BKMK_OriginalLocalizedDescription)
- [OriginalLocalizedName](#BKMK_OriginalLocalizedName)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PhysicalName](#BKMK_PhysicalName)
- [StagedEntityId](#BKMK_StagedEntityId)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_CollectionName"></a> CollectionName

|Property|Value|
|---|---|
|Description|**The collection name of the staged entity.**|
|DisplayName|**Collection Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`collectionname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_DataproviderId"></a> DataproviderId

|Property|Value|
|---|---|
|Description|**The ID of the data provider for virtual entity.**|
|DisplayName|**Dataprovider ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`dataproviderid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_DatasourceId"></a> DatasourceId

|Property|Value|
|---|---|
|Description|**The ID of the data source for virtual entity.**|
|DisplayName|**Datasource ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`datasourceid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_EntityDescription"></a> EntityDescription

|Property|Value|
|---|---|
|Description|**The entity decription with properties for delta update**|
|DisplayName|**EntityDescription**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entitydescription`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|8000|

### <a name="BKMK_EntitySetName"></a> EntitySetName

|Property|Value|
|---|---|
|Description|**The entity set name of the staged entity.**|
|DisplayName|**Entity Set Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entitysetname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_ExternalCollectionName"></a> ExternalCollectionName

|Property|Value|
|---|---|
|Description|**The external collection name of the staged entity for VT scenario.**|
|DisplayName|**External Collection Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`externalcollectionname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_ExternalName"></a> ExternalName

|Property|Value|
|---|---|
|Description|**The external name for virtual entity.**|
|DisplayName|**ExternalName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`externalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Sequence number of the import that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_LogicalCollectionName"></a> LogicalCollectionName

|Property|Value|
|---|---|
|Description|**The logical collection name of the staged entity.**|
|DisplayName|**Logical Collection Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`logicalcollectionname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_LogicalName"></a> LogicalName

|Property|Value|
|---|---|
|Description|**The logical name of the staged entity.**|
|DisplayName|**Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`logicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**The name of the staged entity.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_OriginalLocalizedCollectionName"></a> OriginalLocalizedCollectionName

|Property|Value|
|---|---|
|Description|**The original localized collection name of the staged entity.**|
|DisplayName|**Original Localized Collection Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`originallocalizedcollectioname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_OriginalLocalizedDescription"></a> OriginalLocalizedDescription

|Property|Value|
|---|---|
|Description|**The localized description of the entity.**|
|DisplayName|**OriginalLocalizedDescription**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`originallocalizedescription`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|8000|

### <a name="BKMK_OriginalLocalizedName"></a> OriginalLocalizedName

|Property|Value|
|---|---|
|Description|**The original localized name of the staged entity.**|
|DisplayName|**Original Localized Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`originallocalizedname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|---|---|
|Description|**Date and time that the record was migrated.**|
|DisplayName|**Record Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overriddencreatedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_PhysicalName"></a> PhysicalName

|Property|Value|
|---|---|
|Description|**The physical name of the staged entity.**|
|DisplayName|**Physical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`physicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_StagedEntityId"></a> StagedEntityId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Entity identifier**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`stagedentityid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Staged Entity**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`stagedentity_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Staged Entity**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`stagedentity_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Time Zone Rule Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezoneruleversionnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|---|---|
|Description|**Time zone code that was in use when the record was created.**|
|DisplayName|**UTC Conversion Time Zone Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`utcconversiontimezonecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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

### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who created the record.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who modified the record.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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

### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who modified the record.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version Number**|
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

- [lk_stagedentity_createdby](#BKMK_lk_stagedentity_createdby)
- [lk_stagedentity_createdonbehalfby](#BKMK_lk_stagedentity_createdonbehalfby)
- [lk_stagedentity_modifiedby](#BKMK_lk_stagedentity_modifiedby)
- [lk_stagedentity_modifiedonbehalfby](#BKMK_lk_stagedentity_modifiedonbehalfby)

### <a name="BKMK_lk_stagedentity_createdby"></a> lk_stagedentity_createdby

One-To-Many Relationship: [systemuser lk_stagedentity_createdby](systemuser.md#BKMK_lk_stagedentity_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_stagedentity_createdonbehalfby"></a> lk_stagedentity_createdonbehalfby

One-To-Many Relationship: [systemuser lk_stagedentity_createdonbehalfby](systemuser.md#BKMK_lk_stagedentity_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_stagedentity_modifiedby"></a> lk_stagedentity_modifiedby

One-To-Many Relationship: [systemuser lk_stagedentity_modifiedby](systemuser.md#BKMK_lk_stagedentity_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_stagedentity_modifiedonbehalfby"></a> lk_stagedentity_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_stagedentity_modifiedonbehalfby](systemuser.md#BKMK_lk_stagedentity_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [stagedentity_AsyncOperations](#BKMK_stagedentity_AsyncOperations)
- [stagedentity_BulkDeleteFailures](#BKMK_stagedentity_BulkDeleteFailures)
- [stagedentity_MailboxTrackingFolders](#BKMK_stagedentity_MailboxTrackingFolders)
- [stagedentity_PrincipalObjectAttributeAccesses](#BKMK_stagedentity_PrincipalObjectAttributeAccesses)
- [stagedentity_ProcessSession](#BKMK_stagedentity_ProcessSession)
- [stagedentity_SyncErrors](#BKMK_stagedentity_SyncErrors)

### <a name="BKMK_stagedentity_AsyncOperations"></a> stagedentity_AsyncOperations

Many-To-One Relationship: [asyncoperation stagedentity_AsyncOperations](asyncoperation.md#BKMK_stagedentity_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedentity_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedentity_BulkDeleteFailures"></a> stagedentity_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure stagedentity_BulkDeleteFailures](bulkdeletefailure.md#BKMK_stagedentity_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedentity_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedentity_MailboxTrackingFolders"></a> stagedentity_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder stagedentity_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_stagedentity_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedentity_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedentity_PrincipalObjectAttributeAccesses"></a> stagedentity_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess stagedentity_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_stagedentity_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`stagedentity_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedentity_ProcessSession"></a> stagedentity_ProcessSession

Many-To-One Relationship: [processsession stagedentity_ProcessSession](processsession.md#BKMK_stagedentity_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedentity_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedentity_SyncErrors"></a> stagedentity_SyncErrors

Many-To-One Relationship: [syncerror stagedentity_SyncErrors](syncerror.md#BKMK_stagedentity_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedentity_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.stagedentity?displayProperty=fullName>
