---
title: "SystemUserAuthorizationChangeTracker table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the SystemUserAuthorizationChangeTracker table/entity."
ms.date: 03/04/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# SystemUserAuthorizationChangeTracker table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Internal authorization table to track user authorization changes

**Added by**: AuthorizationCore Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|SystemUserAuthorizationChangeTrackers|
|DisplayCollectionName|SystemUserAuthorizationChangeTrackers|
|DisplayName|SystemUserAuthorizationChangeTracker|
|EntitySetName|systemuserauthorizationchangetrackers|
|IsBPFEntity|False|
|LogicalCollectionName|systemuserauthorizationchangetrackers|
|LogicalName|systemuserauthorizationchangetracker|
|OwnershipType|None|
|PrimaryIdAttribute|systemuserid|
|PrimaryNameAttribute||
|SchemaName|SystemUserAuthorizationChangeTracker|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.


### <a name="BKMK_SystemUserId"></a> SystemUserId

|Property|Value|
|--------|-----|
|Description|Unique identifier for the user|
|DisplayName|User|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|systemuserid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ChangedOn](#BKMK_ChangedOn)
- [ChangedVersionNumber](#BKMK_ChangedVersionNumber)
- [ComputedOn](#BKMK_ComputedOn)
- [ComputedVersionNumber](#BKMK_ComputedVersionNumber)
- [SystemUserIdName](#BKMK_SystemUserIdName)
- [SystemUserIdYomiName](#BKMK_SystemUserIdYomiName)


### <a name="BKMK_ChangedOn"></a> ChangedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the column ChangedVersionNumber was changed.|
|DisplayName|Changed On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|changedon|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_ChangedVersionNumber"></a> ChangedVersionNumber

|Property|Value|
|--------|-----|
|Description|Database time stamp when user authorization settings were changed|
|DisplayName|ChangedVersionNumber|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|changedversionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|SystemRequired|
|Type|BigInt|


### <a name="BKMK_ComputedOn"></a> ComputedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the column ComputedVersionNumber was changed.|
|DisplayName|Computed On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|computedon|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_ComputedVersionNumber"></a> ComputedVersionNumber

|Property|Value|
|--------|-----|
|Description|Database time stamp when user authorization data were started recompute|
|DisplayName|ComputedVersionNumber|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|computedversionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|SystemRequired|
|Type|BigInt|


### <a name="BKMK_SystemUserIdName"></a> SystemUserIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|systemuseridname|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SystemUserIdYomiName"></a> SystemUserIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|systemuseridyominame|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [systemuserauthorizationchangetracker_SyncErrors](#BKMK_systemuserauthorizationchangetracker_SyncErrors)
- [systemuserauthorizationchangetracker_AsyncOperations](#BKMK_systemuserauthorizationchangetracker_AsyncOperations)
- [systemuserauthorizationchangetracker_MailboxTrackingFolders](#BKMK_systemuserauthorizationchangetracker_MailboxTrackingFolders)
- [systemuserauthorizationchangetracker_ProcessSession](#BKMK_systemuserauthorizationchangetracker_ProcessSession)
- [systemuserauthorizationchangetracker_BulkDeleteFailures](#BKMK_systemuserauthorizationchangetracker_BulkDeleteFailures)
- [systemuserauthorizationchangetracker_PrincipalObjectAttributeAccesses](#BKMK_systemuserauthorizationchangetracker_PrincipalObjectAttributeAccesses)


### <a name="BKMK_systemuserauthorizationchangetracker_SyncErrors"></a> systemuserauthorizationchangetracker_SyncErrors

**Added by**: System Solution Solution

Same as syncerror table [systemuserauthorizationchangetracker_SyncErrors](syncerror.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuserauthorizationchangetracker_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_systemuserauthorizationchangetracker_AsyncOperations"></a> systemuserauthorizationchangetracker_AsyncOperations

**Added by**: System Solution Solution

Same as asyncoperation table [systemuserauthorizationchangetracker_AsyncOperations](asyncoperation.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuserauthorizationchangetracker_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_systemuserauthorizationchangetracker_MailboxTrackingFolders"></a> systemuserauthorizationchangetracker_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as mailboxtrackingfolder table [systemuserauthorizationchangetracker_MailboxTrackingFolders](mailboxtrackingfolder.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuserauthorizationchangetracker_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_systemuserauthorizationchangetracker_ProcessSession"></a> systemuserauthorizationchangetracker_ProcessSession

**Added by**: System Solution Solution

Same as processsession table [systemuserauthorizationchangetracker_ProcessSession](processsession.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuserauthorizationchangetracker_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_systemuserauthorizationchangetracker_BulkDeleteFailures"></a> systemuserauthorizationchangetracker_BulkDeleteFailures

**Added by**: System Solution Solution

Same as bulkdeletefailure table [systemuserauthorizationchangetracker_BulkDeleteFailures](bulkdeletefailure.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuserauthorizationchangetracker_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_systemuserauthorizationchangetracker_PrincipalObjectAttributeAccesses"></a> systemuserauthorizationchangetracker_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as principalobjectattributeaccess table [systemuserauthorizationchangetracker_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|systemuserauthorizationchangetracker_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.


### <a name="BKMK_user_userauthztracker"></a> user_userauthztracker

**Added by**: System Solution Solution

See systemuser Table [user_userauthztracker](systemuser.md) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.systemuserauthorizationchangetracker?text=systemuserauthorizationchangetracker EntityType" />