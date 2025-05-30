---
title: "Staged Metadata Async Operation (StagedMetadataAsyncOperation) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Staged Metadata Async Operation (StagedMetadataAsyncOperation) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Staged Metadata Async Operation (StagedMetadataAsyncOperation) table/entity reference (Microsoft Dataverse)

Stores staged entity metadata to be processed before fully created.

## Messages

The following table lists the messages for the Staged Metadata Async Operation (StagedMetadataAsyncOperation) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /stagedmetadataasyncoperations<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /stagedmetadataasyncoperations(*stagedmetadataasyncoperationid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /stagedmetadataasyncoperations(*stagedmetadataasyncoperationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /stagedmetadataasyncoperations<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /stagedmetadataasyncoperations(*stagedmetadataasyncoperationid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /stagedmetadataasyncoperations(*stagedmetadataasyncoperationid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Staged Metadata Async Operation (StagedMetadataAsyncOperation) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Staged Metadata Async Operation** |
| **DisplayCollectionName** | **Staged Metadata Async Operations** |
| **SchemaName** | `StagedMetadataAsyncOperation` |
| **CollectionSchemaName** | `StagedMetadataAsyncOperations` |
| **EntitySetName** | `stagedmetadataasyncoperations`|
| **LogicalName** | `stagedmetadataasyncoperation` |
| **LogicalCollectionName** | `stagedmetadataasyncoperations` |
| **PrimaryIdAttribute** | `stagedmetadataasyncoperationid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

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

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Staged Metadata Async Operation**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`stagedmetadataasyncoperation_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Staged Metadata Async Operation**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`stagedmetadataasyncoperation_statuscode`|

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

- [AsyncJobStatus](#BKMK_AsyncJobStatus)
- [AsyncOperationId](#BKMK_AsyncOperationId)
- [ComponentType](#BKMK_ComponentType)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [Name](#BKMK_Name)
- [ObjectId](#BKMK_ObjectId)
- [StagedMetadataAsyncOperationId](#BKMK_StagedMetadataAsyncOperationId)
- [UnprocessedDependencies](#BKMK_UnprocessedDependencies)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_AsyncJobStatus"></a> AsyncJobStatus

|Property|Value|
|---|---|
|Description|**Status of the Async Job to process metadata operation.**|
|DisplayName|**Async Job Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`asyncjobstatus`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_AsyncOperationId"></a> AsyncOperationId

|Property|Value|
|---|---|
|Description|**Async Job OperationId.**|
|DisplayName|**Async Job OperationId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`asyncoperationid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ComponentType"></a> ComponentType

|Property|Value|
|---|---|
|Description|**Type of metadata component.**|
|DisplayName|**ComponentType**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`componenttype`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

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

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**The name of the staged metadata async operation.**|
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

### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|---|---|
|Description|**Component (Entity/Attribute) MetadataId**|
|DisplayName|**ObjectId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`objectid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_StagedMetadataAsyncOperationId"></a> StagedMetadataAsyncOperationId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Entity identifier**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`stagedmetadataasyncoperationid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_UnprocessedDependencies"></a> UnprocessedDependencies

|Property|Value|
|---|---|
|Description|**List of unprocessed dependencies**|
|DisplayName|**Unprocessed dependencies**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`unprocesseddependencies`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

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

- [lk_stagedmetadataasyncoperation_createdby](#BKMK_lk_stagedmetadataasyncoperation_createdby)
- [lk_stagedmetadataasyncoperation_createdonbehalfby](#BKMK_lk_stagedmetadataasyncoperation_createdonbehalfby)
- [lk_stagedmetadataasyncoperation_modifiedby](#BKMK_lk_stagedmetadataasyncoperation_modifiedby)
- [lk_stagedmetadataasyncoperation_modifiedonbehalfby](#BKMK_lk_stagedmetadataasyncoperation_modifiedonbehalfby)

### <a name="BKMK_lk_stagedmetadataasyncoperation_createdby"></a> lk_stagedmetadataasyncoperation_createdby

One-To-Many Relationship: [systemuser lk_stagedmetadataasyncoperation_createdby](systemuser.md#BKMK_lk_stagedmetadataasyncoperation_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_stagedmetadataasyncoperation_createdonbehalfby"></a> lk_stagedmetadataasyncoperation_createdonbehalfby

One-To-Many Relationship: [systemuser lk_stagedmetadataasyncoperation_createdonbehalfby](systemuser.md#BKMK_lk_stagedmetadataasyncoperation_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_stagedmetadataasyncoperation_modifiedby"></a> lk_stagedmetadataasyncoperation_modifiedby

One-To-Many Relationship: [systemuser lk_stagedmetadataasyncoperation_modifiedby](systemuser.md#BKMK_lk_stagedmetadataasyncoperation_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_stagedmetadataasyncoperation_modifiedonbehalfby"></a> lk_stagedmetadataasyncoperation_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_stagedmetadataasyncoperation_modifiedonbehalfby](systemuser.md#BKMK_lk_stagedmetadataasyncoperation_modifiedonbehalfby)

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

- [stagedmetadataasyncoperation_AsyncOperations](#BKMK_stagedmetadataasyncoperation_AsyncOperations)
- [stagedmetadataasyncoperation_BulkDeleteFailures](#BKMK_stagedmetadataasyncoperation_BulkDeleteFailures)
- [stagedmetadataasyncoperation_MailboxTrackingFolders](#BKMK_stagedmetadataasyncoperation_MailboxTrackingFolders)
- [stagedmetadataasyncoperation_PrincipalObjectAttributeAccesses](#BKMK_stagedmetadataasyncoperation_PrincipalObjectAttributeAccesses)
- [stagedmetadataasyncoperation_ProcessSession](#BKMK_stagedmetadataasyncoperation_ProcessSession)
- [stagedmetadataasyncoperation_SyncErrors](#BKMK_stagedmetadataasyncoperation_SyncErrors)

### <a name="BKMK_stagedmetadataasyncoperation_AsyncOperations"></a> stagedmetadataasyncoperation_AsyncOperations

Many-To-One Relationship: [asyncoperation stagedmetadataasyncoperation_AsyncOperations](asyncoperation.md#BKMK_stagedmetadataasyncoperation_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedmetadataasyncoperation_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedmetadataasyncoperation_BulkDeleteFailures"></a> stagedmetadataasyncoperation_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure stagedmetadataasyncoperation_BulkDeleteFailures](bulkdeletefailure.md#BKMK_stagedmetadataasyncoperation_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedmetadataasyncoperation_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedmetadataasyncoperation_MailboxTrackingFolders"></a> stagedmetadataasyncoperation_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder stagedmetadataasyncoperation_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_stagedmetadataasyncoperation_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedmetadataasyncoperation_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedmetadataasyncoperation_PrincipalObjectAttributeAccesses"></a> stagedmetadataasyncoperation_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess stagedmetadataasyncoperation_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_stagedmetadataasyncoperation_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`stagedmetadataasyncoperation_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedmetadataasyncoperation_ProcessSession"></a> stagedmetadataasyncoperation_ProcessSession

Many-To-One Relationship: [processsession stagedmetadataasyncoperation_ProcessSession](processsession.md#BKMK_stagedmetadataasyncoperation_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedmetadataasyncoperation_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedmetadataasyncoperation_SyncErrors"></a> stagedmetadataasyncoperation_SyncErrors

Many-To-One Relationship: [syncerror stagedmetadataasyncoperation_SyncErrors](syncerror.md#BKMK_stagedmetadataasyncoperation_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedmetadataasyncoperation_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.stagedmetadataasyncoperation?displayProperty=fullName>
