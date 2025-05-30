---
title: "Entity Index (EntityIndex) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Entity Index (EntityIndex) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Entity Index (EntityIndex) table/entity reference (Microsoft Dataverse)

Metadata describing index of an entity

## Messages

The following table lists the messages for the Entity Index (EntityIndex) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|

## Properties

The following table lists selected properties for the Entity Index (EntityIndex) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Entity Index** |
| **DisplayCollectionName** | **Entity Indexes** |
| **SchemaName** | `EntityIndex` |
| **CollectionSchemaName** | `EntityIndexes` |
| **EntitySetName** | `entityindexes`|
| **LogicalName** | `entityindex` |
| **LogicalCollectionName** | `entityindexes` |
| **PrimaryIdAttribute** | `indexid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [IndexId](#BKMK_IndexId)
- [Name](#BKMK_Name)
- [SequentialKeyStatus](#BKMK_SequentialKeyStatus)

### <a name="BKMK_IndexId"></a> IndexId

|Property|Value|
|---|---|
|Description|**Unique identifier of the index id**|
|DisplayName|**Index Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`indexid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Display Name**|
|DisplayName|**Display Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_SequentialKeyStatus"></a> SequentialKeyStatus

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Sequential Key Status**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sequentialkeystatus`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [OverwriteTime](#BKMK_OverwriteTime)
- [RecordId](#BKMK_RecordId)
- [SolutionId](#BKMK_SolutionId)
- [VersionNumber](#BKMK_VersionNumber)

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
|DefaultFormValue|-1|
|GlobalChoiceName|`componentstate`|

#### ComponentState Choices/Options

|Value|Label|
|---|---|
|0|**Published**|
|1|**Unpublished**|
|2|**Deleted**|
|3|**Deleted Unpublished**|

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
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_RecordId"></a> RecordId

|Property|Value|
|---|---|
|Description|**The record id of this entity index.**|
|DisplayName|**Record Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`recordid`|
|RequiredLevel|SystemRequired|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

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

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**The version number of this entity index.**|
|DisplayName|**Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|SystemRequired|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [entityindex_AsyncOperations](#BKMK_entityindex_AsyncOperations)
- [entityindex_BulkDeleteFailures](#BKMK_entityindex_BulkDeleteFailures)
- [entityindex_MailboxTrackingFolders](#BKMK_entityindex_MailboxTrackingFolders)
- [entityindex_PrincipalObjectAttributeAccesses](#BKMK_entityindex_PrincipalObjectAttributeAccesses)
- [entityindex_SyncErrors](#BKMK_entityindex_SyncErrors)

### <a name="BKMK_entityindex_AsyncOperations"></a> entityindex_AsyncOperations

Many-To-One Relationship: [asyncoperation entityindex_AsyncOperations](asyncoperation.md#BKMK_entityindex_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`entityindex_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_entityindex_BulkDeleteFailures"></a> entityindex_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure entityindex_BulkDeleteFailures](bulkdeletefailure.md#BKMK_entityindex_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`entityindex_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_entityindex_MailboxTrackingFolders"></a> entityindex_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder entityindex_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_entityindex_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`entityindex_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_entityindex_PrincipalObjectAttributeAccesses"></a> entityindex_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess entityindex_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_entityindex_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`entityindex_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_entityindex_SyncErrors"></a> entityindex_SyncErrors

Many-To-One Relationship: [syncerror entityindex_SyncErrors](syncerror.md#BKMK_entityindex_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`entityindex_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.entityindex?displayProperty=fullName>
