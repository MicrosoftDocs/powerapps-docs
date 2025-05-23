---
title: "SystemUserAuthorizationChangeTracker table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the SystemUserAuthorizationChangeTracker table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# SystemUserAuthorizationChangeTracker table/entity reference (Microsoft Dataverse)

Internal authorization table to track user authorization changes

## Messages

The following table lists the messages for the SystemUserAuthorizationChangeTracker table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|

## Properties

The following table lists selected properties for the SystemUserAuthorizationChangeTracker table.

|Property|Value|
| --- | --- |
| **DisplayName** | **SystemUserAuthorizationChangeTracker** |
| **DisplayCollectionName** | **SystemUserAuthorizationChangeTrackers** |
| **SchemaName** | `SystemUserAuthorizationChangeTracker` |
| **CollectionSchemaName** | `SystemUserAuthorizationChangeTrackers` |
| **EntitySetName** | `systemuserauthorizationchangetrackers`|
| **LogicalName** | `systemuserauthorizationchangetracker` |
| **LogicalCollectionName** | `systemuserauthorizationchangetrackers` |
| **PrimaryIdAttribute** | `systemuserid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

### <a name="BKMK_SystemUserId"></a> SystemUserId

|Property|Value|
|---|---|
|Description|**Unique identifier for the user**|
|DisplayName|**User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`systemuserid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ChangedOn](#BKMK_ChangedOn)
- [ChangedVersionNumber](#BKMK_ChangedVersionNumber)
- [ComputedOn](#BKMK_ComputedOn)
- [ComputedVersionNumber](#BKMK_ComputedVersionNumber)
- [SystemUserIdName](#BKMK_SystemUserIdName)
- [SystemUserIdYomiName](#BKMK_SystemUserIdYomiName)

### <a name="BKMK_ChangedOn"></a> ChangedOn

|Property|Value|
|---|---|
|Description|**Date and time when the column ChangedVersionNumber was changed.**|
|DisplayName|**Changed On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`changedon`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ChangedVersionNumber"></a> ChangedVersionNumber

|Property|Value|
|---|---|
|Description|**Database time stamp when user authorization settings were changed**|
|DisplayName|**ChangedVersionNumber**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`changedversionnumber`|
|RequiredLevel|SystemRequired|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_ComputedOn"></a> ComputedOn

|Property|Value|
|---|---|
|Description|**Date and time when the column ComputedVersionNumber was changed.**|
|DisplayName|**Computed On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`computedon`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ComputedVersionNumber"></a> ComputedVersionNumber

|Property|Value|
|---|---|
|Description|**Database time stamp when user authorization data were started recompute**|
|DisplayName|**ComputedVersionNumber**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`computedversionnumber`|
|RequiredLevel|SystemRequired|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_SystemUserIdName"></a> SystemUserIdName

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`systemuseridname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_SystemUserIdYomiName"></a> SystemUserIdYomiName

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`systemuseridyominame`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

### <a name="BKMK_user_userauthztracker"></a> user_userauthztracker

One-To-Many Relationship: [systemuser user_userauthztracker](systemuser.md#BKMK_user_userauthztracker)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`systemuserid`|
|ReferencingEntityNavigationPropertyName|`systemuserid_userauthztracker`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [systemuserauthorizationchangetracker_AsyncOperations](#BKMK_systemuserauthorizationchangetracker_AsyncOperations)
- [systemuserauthorizationchangetracker_BulkDeleteFailures](#BKMK_systemuserauthorizationchangetracker_BulkDeleteFailures)
- [systemuserauthorizationchangetracker_MailboxTrackingFolders](#BKMK_systemuserauthorizationchangetracker_MailboxTrackingFolders)
- [systemuserauthorizationchangetracker_PrincipalObjectAttributeAccesses](#BKMK_systemuserauthorizationchangetracker_PrincipalObjectAttributeAccesses)
- [systemuserauthorizationchangetracker_ProcessSession](#BKMK_systemuserauthorizationchangetracker_ProcessSession)
- [systemuserauthorizationchangetracker_SyncErrors](#BKMK_systemuserauthorizationchangetracker_SyncErrors)

### <a name="BKMK_systemuserauthorizationchangetracker_AsyncOperations"></a> systemuserauthorizationchangetracker_AsyncOperations

Many-To-One Relationship: [asyncoperation systemuserauthorizationchangetracker_AsyncOperations](asyncoperation.md#BKMK_systemuserauthorizationchangetracker_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`systemuserauthorizationchangetracker_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_systemuserauthorizationchangetracker_BulkDeleteFailures"></a> systemuserauthorizationchangetracker_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure systemuserauthorizationchangetracker_BulkDeleteFailures](bulkdeletefailure.md#BKMK_systemuserauthorizationchangetracker_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`systemuserauthorizationchangetracker_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_systemuserauthorizationchangetracker_MailboxTrackingFolders"></a> systemuserauthorizationchangetracker_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder systemuserauthorizationchangetracker_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_systemuserauthorizationchangetracker_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`systemuserauthorizationchangetracker_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_systemuserauthorizationchangetracker_PrincipalObjectAttributeAccesses"></a> systemuserauthorizationchangetracker_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess systemuserauthorizationchangetracker_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_systemuserauthorizationchangetracker_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`systemuserauthorizationchangetracker_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_systemuserauthorizationchangetracker_ProcessSession"></a> systemuserauthorizationchangetracker_ProcessSession

Many-To-One Relationship: [processsession systemuserauthorizationchangetracker_ProcessSession](processsession.md#BKMK_systemuserauthorizationchangetracker_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`systemuserauthorizationchangetracker_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_systemuserauthorizationchangetracker_SyncErrors"></a> systemuserauthorizationchangetracker_SyncErrors

Many-To-One Relationship: [syncerror systemuserauthorizationchangetracker_SyncErrors](syncerror.md#BKMK_systemuserauthorizationchangetracker_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`systemuserauthorizationchangetracker_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.systemuserauthorizationchangetracker?displayProperty=fullName>
