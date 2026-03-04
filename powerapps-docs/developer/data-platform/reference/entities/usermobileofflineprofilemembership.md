---
title: "usermobileofflineprofilemembership table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the usermobileofflineprofilemembership table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# usermobileofflineprofilemembership table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the usermobileofflineprofilemembership table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|

## Properties

The following table lists selected properties for the usermobileofflineprofilemembership table.

|Property|Value|
| --- | --- |
| **DisplayName** | **UserMobileOfflineProfileMembership** |
| **DisplayCollectionName** | **UserMobileOfflineProfileMemberships** |
| **SchemaName** | `usermobileofflineprofilemembership` |
| **CollectionSchemaName** | `usermobileofflineprofilememberships` |
| **EntitySetName** | `usermobileofflineprofilememberships`|
| **LogicalName** | `usermobileofflineprofilemembership` |
| **LogicalCollectionName** | `usermobileofflineprofilememberships` |
| **PrimaryIdAttribute** | `usermobileofflineprofilemembershipid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [HasMobileOfflineProfileIdConflict](#BKMK_HasMobileOfflineProfileIdConflict)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [MobileOfflineProfileId](#BKMK_MobileOfflineProfileId)
- [name](#BKMK_name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [SystemUserId](#BKMK_SystemUserId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [usermobileofflineprofilemembershipId](#BKMK_usermobileofflineprofilemembershipId)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_HasMobileOfflineProfileIdConflict"></a> HasMobileOfflineProfileIdConflict

|Property|Value|
|---|---|
|Description||
|DisplayName|**HasMobileOfflineProfileIdConflict**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`hasmobileofflineprofileidconflict`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`usermobileofflineprofilemembership_hasmobileofflineprofileidconflict`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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

### <a name="BKMK_MobileOfflineProfileId"></a> MobileOfflineProfileId

|Property|Value|
|---|---|
|Description||
|DisplayName|**MobileOfflineProfileId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mobileofflineprofileid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mobileofflineprofile|

### <a name="BKMK_name"></a> name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
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
|MaxLength|100|

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
|Description|**Status of the UserMobileOfflineProfileMembership**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`usermobileofflineprofilemembership_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the UserMobileOfflineProfileMembership**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`usermobileofflineprofilemembership_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_SystemUserId"></a> SystemUserId

|Property|Value|
|---|---|
|Description||
|DisplayName|**SystemUserId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`systemuserid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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

### <a name="BKMK_usermobileofflineprofilemembershipId"></a> usermobileofflineprofilemembershipId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**UserMobileOfflineProfileMembership**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`usermobileofflineprofilemembershipid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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
- [OrganizationId](#BKMK_OrganizationId)
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

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of UserMobileOfflineProfileMembership.**|
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

- [lk_usermobileofflineprofilemembership_createdby](#BKMK_lk_usermobileofflineprofilemembership_createdby)
- [lk_usermobileofflineprofilemembership_createdonbehalfby](#BKMK_lk_usermobileofflineprofilemembership_createdonbehalfby)
- [lk_usermobileofflineprofilemembership_modifiedby](#BKMK_lk_usermobileofflineprofilemembership_modifiedby)
- [lk_usermobileofflineprofilemembership_modifiedonbehalfby](#BKMK_lk_usermobileofflineprofilemembership_modifiedonbehalfby)
- [mobileofflineprofile_usermobileofflineprofilemembership_MobileOfflineProfileId](#BKMK_mobileofflineprofile_usermobileofflineprofilemembership_MobileOfflineProfileId)
- [organization_usermobileofflineprofilemembership](#BKMK_organization_usermobileofflineprofilemembership)
- [systemuser_usermobileofflineprofilemembership_SystemUserId](#BKMK_systemuser_usermobileofflineprofilemembership_SystemUserId)

### <a name="BKMK_lk_usermobileofflineprofilemembership_createdby"></a> lk_usermobileofflineprofilemembership_createdby

One-To-Many Relationship: [systemuser lk_usermobileofflineprofilemembership_createdby](systemuser.md#BKMK_lk_usermobileofflineprofilemembership_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_usermobileofflineprofilemembership_createdonbehalfby"></a> lk_usermobileofflineprofilemembership_createdonbehalfby

One-To-Many Relationship: [systemuser lk_usermobileofflineprofilemembership_createdonbehalfby](systemuser.md#BKMK_lk_usermobileofflineprofilemembership_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_usermobileofflineprofilemembership_modifiedby"></a> lk_usermobileofflineprofilemembership_modifiedby

One-To-Many Relationship: [systemuser lk_usermobileofflineprofilemembership_modifiedby](systemuser.md#BKMK_lk_usermobileofflineprofilemembership_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_usermobileofflineprofilemembership_modifiedonbehalfby"></a> lk_usermobileofflineprofilemembership_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_usermobileofflineprofilemembership_modifiedonbehalfby](systemuser.md#BKMK_lk_usermobileofflineprofilemembership_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mobileofflineprofile_usermobileofflineprofilemembership_MobileOfflineProfileId"></a> mobileofflineprofile_usermobileofflineprofilemembership_MobileOfflineProfileId

One-To-Many Relationship: [mobileofflineprofile mobileofflineprofile_usermobileofflineprofilemembership_MobileOfflineProfileId](mobileofflineprofile.md#BKMK_mobileofflineprofile_usermobileofflineprofilemembership_MobileOfflineProfileId)

|Property|Value|
|---|---|
|ReferencedEntity|`mobileofflineprofile`|
|ReferencedAttribute|`mobileofflineprofileid`|
|ReferencingAttribute|`mobileofflineprofileid`|
|ReferencingEntityNavigationPropertyName|`MobileOfflineProfileId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_usermobileofflineprofilemembership"></a> organization_usermobileofflineprofilemembership

One-To-Many Relationship: [organization organization_usermobileofflineprofilemembership](organization.md#BKMK_organization_usermobileofflineprofilemembership)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_systemuser_usermobileofflineprofilemembership_SystemUserId"></a> systemuser_usermobileofflineprofilemembership_SystemUserId

One-To-Many Relationship: [systemuser systemuser_usermobileofflineprofilemembership_SystemUserId](systemuser.md#BKMK_systemuser_usermobileofflineprofilemembership_SystemUserId)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`systemuserid`|
|ReferencingEntityNavigationPropertyName|`SystemUserId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [usermobileofflineprofilemembership_AsyncOperations](#BKMK_usermobileofflineprofilemembership_AsyncOperations)
- [usermobileofflineprofilemembership_BulkDeleteFailures](#BKMK_usermobileofflineprofilemembership_BulkDeleteFailures)
- [usermobileofflineprofilemembership_MailboxTrackingFolders](#BKMK_usermobileofflineprofilemembership_MailboxTrackingFolders)
- [usermobileofflineprofilemembership_PrincipalObjectAttributeAccesses](#BKMK_usermobileofflineprofilemembership_PrincipalObjectAttributeAccesses)
- [usermobileofflineprofilemembership_ProcessSession](#BKMK_usermobileofflineprofilemembership_ProcessSession)
- [usermobileofflineprofilemembership_SyncErrors](#BKMK_usermobileofflineprofilemembership_SyncErrors)

### <a name="BKMK_usermobileofflineprofilemembership_AsyncOperations"></a> usermobileofflineprofilemembership_AsyncOperations

Many-To-One Relationship: [asyncoperation usermobileofflineprofilemembership_AsyncOperations](asyncoperation.md#BKMK_usermobileofflineprofilemembership_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`usermobileofflineprofilemembership_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_usermobileofflineprofilemembership_BulkDeleteFailures"></a> usermobileofflineprofilemembership_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure usermobileofflineprofilemembership_BulkDeleteFailures](bulkdeletefailure.md#BKMK_usermobileofflineprofilemembership_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`usermobileofflineprofilemembership_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_usermobileofflineprofilemembership_MailboxTrackingFolders"></a> usermobileofflineprofilemembership_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder usermobileofflineprofilemembership_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_usermobileofflineprofilemembership_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`usermobileofflineprofilemembership_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_usermobileofflineprofilemembership_PrincipalObjectAttributeAccesses"></a> usermobileofflineprofilemembership_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess usermobileofflineprofilemembership_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_usermobileofflineprofilemembership_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`usermobileofflineprofilemembership_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_usermobileofflineprofilemembership_ProcessSession"></a> usermobileofflineprofilemembership_ProcessSession

Many-To-One Relationship: [processsession usermobileofflineprofilemembership_ProcessSession](processsession.md#BKMK_usermobileofflineprofilemembership_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`usermobileofflineprofilemembership_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_usermobileofflineprofilemembership_SyncErrors"></a> usermobileofflineprofilemembership_SyncErrors

Many-To-One Relationship: [syncerror usermobileofflineprofilemembership_SyncErrors](syncerror.md#BKMK_usermobileofflineprofilemembership_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`usermobileofflineprofilemembership_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.usermobileofflineprofilemembership?displayProperty=fullName>
