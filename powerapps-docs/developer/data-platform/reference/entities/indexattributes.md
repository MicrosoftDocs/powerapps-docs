---
title: "Index Attribute (IndexAttributes) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Index Attribute (IndexAttributes) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Index Attribute (IndexAttributes) table/entity reference (Microsoft Dataverse)

Stores index attributes

## Messages

The following table lists the messages for the Index Attribute (IndexAttributes) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|

## Properties

The following table lists selected properties for the Index Attribute (IndexAttributes) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Index Attribute** |
| **DisplayCollectionName** | **Index Attributes** |
| **SchemaName** | `IndexAttributes` |
| **CollectionSchemaName** | `IndexAttributes` |
| **EntitySetName** | `indexattributes`|
| **LogicalName** | `indexattributes` |
| **LogicalCollectionName** | `indexattributes` |
| **PrimaryIdAttribute** | `indexattributeid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [IndexAttributeId](#BKMK_IndexAttributeId)
- [IndexId](#BKMK_IndexId)

### <a name="BKMK_IndexAttributeId"></a> IndexAttributeId

|Property|Value|
|---|---|
|Description|**Unique identifier of the index attribute**|
|DisplayName|**Index Attribute Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`indexattributeid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_IndexId"></a> IndexId

|Property|Value|
|---|---|
|Description|**Unique identifier of the entity index**|
|DisplayName|**Index Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`indexid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [RecordId](#BKMK_RecordId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_RecordId"></a> RecordId

|Property|Value|
|---|---|
|Description|**The record id of this index attribute.**|
|DisplayName|**Record Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`recordid`|
|RequiredLevel|SystemRequired|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**The version number of this index attribute.**|
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

- [indexattributes_AsyncOperations](#BKMK_indexattributes_AsyncOperations)
- [indexattributes_BulkDeleteFailures](#BKMK_indexattributes_BulkDeleteFailures)
- [indexattributes_MailboxTrackingFolders](#BKMK_indexattributes_MailboxTrackingFolders)
- [indexattributes_PrincipalObjectAttributeAccesses](#BKMK_indexattributes_PrincipalObjectAttributeAccesses)
- [indexattributes_SyncErrors](#BKMK_indexattributes_SyncErrors)

### <a name="BKMK_indexattributes_AsyncOperations"></a> indexattributes_AsyncOperations

Many-To-One Relationship: [asyncoperation indexattributes_AsyncOperations](asyncoperation.md#BKMK_indexattributes_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`indexattributes_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_indexattributes_BulkDeleteFailures"></a> indexattributes_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure indexattributes_BulkDeleteFailures](bulkdeletefailure.md#BKMK_indexattributes_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`indexattributes_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_indexattributes_MailboxTrackingFolders"></a> indexattributes_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder indexattributes_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_indexattributes_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`indexattributes_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_indexattributes_PrincipalObjectAttributeAccesses"></a> indexattributes_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess indexattributes_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_indexattributes_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`indexattributes_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_indexattributes_SyncErrors"></a> indexattributes_SyncErrors

Many-To-One Relationship: [syncerror indexattributes_SyncErrors](syncerror.md#BKMK_indexattributes_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`indexattributes_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.indexattributes?displayProperty=fullName>
