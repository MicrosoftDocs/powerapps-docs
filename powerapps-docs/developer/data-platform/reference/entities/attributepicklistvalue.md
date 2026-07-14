---
title: "Option Set Value (AttributePicklistValue) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Option Set Value (AttributePicklistValue) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Option Set Value (AttributePicklistValue) table/entity reference (Microsoft Dataverse)

Option Set Value

## Messages

The following table lists the messages for the Option Set Value (AttributePicklistValue) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|

## Properties

The following table lists selected properties for the Option Set Value (AttributePicklistValue) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Option Set Value** |
| **DisplayCollectionName** | **Option Set Values** |
| **SchemaName** | `AttributePicklistValue` |
| **CollectionSchemaName** | `AttributePicklistValues` |
| **EntitySetName** | `AttributePicklistValues`|
| **LogicalName** | `attributepicklistvalue` |
| **LogicalCollectionName** | `AttributePicklistValues` |
| **PrimaryIdAttribute** | `attributepicklistvalueid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AttributePicklistValueId](#BKMK_AttributePicklistValueId)
- [IsHidden](#BKMK_IsHidden)

### <a name="BKMK_AttributePicklistValueId"></a> AttributePicklistValueId

|Property|Value|
|---|---|
|Description|**Unique identifier of the AttributePicklistValue**|
|DisplayName|**AttributePicklistValue Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`attributepicklistvalueid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_IsHidden"></a> IsHidden

|Property|Value|
|---|---|
|Description|**Hides or shows the AttributePicklistValue**|
|DisplayName|**IsHidden**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ishidden`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`_attributepicklistvalue_ishidden`|
|DefaultValue|False|
|True Label||
|False Label||


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [OverwriteTime](#BKMK_OverwriteTime)
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
|Description|**The version number of this attribute picklist value.**|
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

- [attributepicklistvalue_AsyncOperations](#BKMK_attributepicklistvalue_AsyncOperations)
- [attributepicklistvalue_BulkDeleteFailures](#BKMK_attributepicklistvalue_BulkDeleteFailures)
- [attributepicklistvalue_MailboxTrackingFolders](#BKMK_attributepicklistvalue_MailboxTrackingFolders)
- [attributepicklistvalue_PrincipalObjectAttributeAccesses](#BKMK_attributepicklistvalue_PrincipalObjectAttributeAccesses)
- [attributepicklistvalue_SyncErrors](#BKMK_attributepicklistvalue_SyncErrors)

### <a name="BKMK_attributepicklistvalue_AsyncOperations"></a> attributepicklistvalue_AsyncOperations

Many-To-One Relationship: [asyncoperation attributepicklistvalue_AsyncOperations](asyncoperation.md#BKMK_attributepicklistvalue_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`attributepicklistvalue_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_attributepicklistvalue_BulkDeleteFailures"></a> attributepicklistvalue_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure attributepicklistvalue_BulkDeleteFailures](bulkdeletefailure.md#BKMK_attributepicklistvalue_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`attributepicklistvalue_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_attributepicklistvalue_MailboxTrackingFolders"></a> attributepicklistvalue_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder attributepicklistvalue_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_attributepicklistvalue_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`attributepicklistvalue_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_attributepicklistvalue_PrincipalObjectAttributeAccesses"></a> attributepicklistvalue_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess attributepicklistvalue_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_attributepicklistvalue_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`attributepicklistvalue_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_attributepicklistvalue_SyncErrors"></a> attributepicklistvalue_SyncErrors

Many-To-One Relationship: [syncerror attributepicklistvalue_SyncErrors](syncerror.md#BKMK_attributepicklistvalue_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`attributepicklistvalue_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.attributepicklistvalue?displayProperty=fullName>
