---
title: "Staged relationship (StagedViewAttribute) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Staged relationship (StagedViewAttribute) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Staged relationship (StagedViewAttribute) table/entity reference (Microsoft Dataverse)

Stores staged replationship metadata to be processed asynchronous.

## Messages

The following table lists the messages for the Staged relationship (StagedViewAttribute) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /stagedviewattributes<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /stagedviewattributes(*stagedviewattributeid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /stagedviewattributes(*stagedviewattributeid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /stagedviewattributes<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /stagedviewattributes(*stagedviewattributeid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /stagedviewattributes(*stagedviewattributeid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Staged relationship (StagedViewAttribute) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Staged relationship** |
| **DisplayCollectionName** | **Staged relationships** |
| **SchemaName** | `StagedViewAttribute` |
| **CollectionSchemaName** | `StagedViewAttributes` |
| **EntitySetName** | `stagedviewattributes`|
| **LogicalName** | `stagedviewattribute` |
| **LogicalCollectionName** | `stagedviewattributes` |
| **PrimaryIdAttribute** | `stagedviewattributeid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AttributeId](#BKMK_AttributeId)
- [ComponentState](#BKMK_ComponentState)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [MetadataDescription](#BKMK_MetadataDescription)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OverwriteTime](#BKMK_OverwriteTime)
- [RelationshipId](#BKMK_RelationshipId)
- [RemoteAttributeId](#BKMK_RemoteAttributeId)
- [SolutionId](#BKMK_SolutionId)
- [StagedViewAttributeId](#BKMK_StagedViewAttributeId)
- [StagingExecutionContextId](#BKMK_StagingExecutionContextId)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_AttributeId"></a> AttributeId

|Property|Value|
|---|---|
|Description|**Identifier of the attribute.**|
|DisplayName|**Attribute Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`attributeid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|---|---|
|Description|**Solution component state of view attribute.**|
|DisplayName|**Component State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`componentstate`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue||
|MinValue||

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

### <a name="BKMK_MetadataDescription"></a> MetadataDescription

|Property|Value|
|---|---|
|Description|**Metadata description of view attribute.**|
|DisplayName|**Metadata Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`metadatadescription`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|8000|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**The name of the view attribute.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|255|

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

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**Overwrite time of the solution component view attribute.**|
|DisplayName|**Overwrite Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`overwritetime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_RelationshipId"></a> RelationshipId

|Property|Value|
|---|---|
|Description|**Identifier of the relationship.**|
|DisplayName|**Relationship Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`relationshipid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_RemoteAttributeId"></a> RemoteAttributeId

|Property|Value|
|---|---|
|Description|**Identifier of the remote attribute.**|
|DisplayName|**Remote Attribute Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`remoteattributeid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**Identifier of the solution that contains view attribute.**|
|DisplayName|**Solution Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_StagedViewAttributeId"></a> StagedViewAttributeId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances.**|
|DisplayName|**Staged View Attribute**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`stagedviewattributeid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_StagingExecutionContextId"></a> StagingExecutionContextId

|Property|Value|
|---|---|
|Description|**A unique identifier used to tie together all objects staged within the same transaction.**|
|DisplayName|**Staging Execution Context Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`stagingexecutioncontextid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the staged view attribute.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`stagedviewattribute_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the staged view attribute.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`stagedviewattribute_statuscode`|

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

- [lk_stagedviewattribute_createdby](#BKMK_lk_stagedviewattribute_createdby)
- [lk_stagedviewattribute_createdonbehalfby](#BKMK_lk_stagedviewattribute_createdonbehalfby)
- [lk_stagedviewattribute_modifiedby](#BKMK_lk_stagedviewattribute_modifiedby)
- [lk_stagedviewattribute_modifiedonbehalfby](#BKMK_lk_stagedviewattribute_modifiedonbehalfby)

### <a name="BKMK_lk_stagedviewattribute_createdby"></a> lk_stagedviewattribute_createdby

One-To-Many Relationship: [systemuser lk_stagedviewattribute_createdby](systemuser.md#BKMK_lk_stagedviewattribute_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_stagedviewattribute_createdonbehalfby"></a> lk_stagedviewattribute_createdonbehalfby

One-To-Many Relationship: [systemuser lk_stagedviewattribute_createdonbehalfby](systemuser.md#BKMK_lk_stagedviewattribute_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_stagedviewattribute_modifiedby"></a> lk_stagedviewattribute_modifiedby

One-To-Many Relationship: [systemuser lk_stagedviewattribute_modifiedby](systemuser.md#BKMK_lk_stagedviewattribute_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_stagedviewattribute_modifiedonbehalfby"></a> lk_stagedviewattribute_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_stagedviewattribute_modifiedonbehalfby](systemuser.md#BKMK_lk_stagedviewattribute_modifiedonbehalfby)

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

- [stagedviewattribute_AsyncOperations](#BKMK_stagedviewattribute_AsyncOperations)
- [stagedviewattribute_BulkDeleteFailures](#BKMK_stagedviewattribute_BulkDeleteFailures)
- [stagedviewattribute_MailboxTrackingFolders](#BKMK_stagedviewattribute_MailboxTrackingFolders)
- [stagedviewattribute_PrincipalObjectAttributeAccesses](#BKMK_stagedviewattribute_PrincipalObjectAttributeAccesses)
- [stagedviewattribute_ProcessSession](#BKMK_stagedviewattribute_ProcessSession)
- [stagedviewattribute_SyncErrors](#BKMK_stagedviewattribute_SyncErrors)

### <a name="BKMK_stagedviewattribute_AsyncOperations"></a> stagedviewattribute_AsyncOperations

Many-To-One Relationship: [asyncoperation stagedviewattribute_AsyncOperations](asyncoperation.md#BKMK_stagedviewattribute_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedviewattribute_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedviewattribute_BulkDeleteFailures"></a> stagedviewattribute_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure stagedviewattribute_BulkDeleteFailures](bulkdeletefailure.md#BKMK_stagedviewattribute_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedviewattribute_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedviewattribute_MailboxTrackingFolders"></a> stagedviewattribute_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder stagedviewattribute_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_stagedviewattribute_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedviewattribute_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedviewattribute_PrincipalObjectAttributeAccesses"></a> stagedviewattribute_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess stagedviewattribute_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_stagedviewattribute_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`stagedviewattribute_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedviewattribute_ProcessSession"></a> stagedviewattribute_ProcessSession

Many-To-One Relationship: [processsession stagedviewattribute_ProcessSession](processsession.md#BKMK_stagedviewattribute_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedviewattribute_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedviewattribute_SyncErrors"></a> stagedviewattribute_SyncErrors

Many-To-One Relationship: [syncerror stagedviewattribute_SyncErrors](syncerror.md#BKMK_stagedviewattribute_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedviewattribute_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   

