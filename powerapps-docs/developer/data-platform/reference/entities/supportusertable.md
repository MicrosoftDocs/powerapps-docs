---
title: "supportusertable table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the supportusertable table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# supportusertable table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the supportusertable table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|

## Properties

The following table lists selected properties for the supportusertable table.

|Property|Value|
| --- | --- |
| **DisplayName** | **SupportUserTable** |
| **DisplayCollectionName** | **SupportUserTables** |
| **SchemaName** | `supportusertable` |
| **CollectionSchemaName** | `supportusertables` |
| **EntitySetName** | `supportusertables`|
| **LogicalName** | `supportusertable` |
| **LogicalCollectionName** | `supportusertables` |
| **PrimaryIdAttribute** | `supportusertableid` |
| **PrimaryNameAttribute** |`aaduserobjectid` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AADUserObjectId](#BKMK_AADUserObjectId)
- [EnabledforSoftDelete](#BKMK_EnabledforSoftDelete)
- [ExpiryDateTime](#BKMK_ExpiryDateTime)
- [IdentityProvider](#BKMK_IdentityProvider)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsActive](#BKMK_IsActive)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [supportusertableId](#BKMK_supportusertableId)
- [TenantId](#BKMK_TenantId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UPN](#BKMK_UPN)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_AADUserObjectId"></a> AADUserObjectId

|Property|Value|
|---|---|
|Description|**AAD ObjectId of the support user.**|
|DisplayName|**aaduserobjectid**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`aaduserobjectid`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_EnabledforSoftDelete"></a> EnabledforSoftDelete

|Property|Value|
|---|---|
|Description|**Status of the record for deletion**|
|DisplayName|**EnabledforSoftDelete**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`enabledforsoftdelete`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`field_security_permission_type`|

#### EnabledforSoftDelete Choices/Options

|Value|Label|
|---|---|
|0|**Not Allowed**|
|4|**Allowed**|

### <a name="BKMK_ExpiryDateTime"></a> ExpiryDateTime

|Property|Value|
|---|---|
|Description|**Expiration time for the User access.**|
|DisplayName|**ExpiryDateTime**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`expirydatetime`|
|RequiredLevel|ApplicationRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_IdentityProvider"></a> IdentityProvider

|Property|Value|
|---|---|
|Description||
|DisplayName|**IdentityProvider**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`identityprovider`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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

### <a name="BKMK_IsActive"></a> IsActive

|Property|Value|
|---|---|
|Description|**Status of the User record.**|
|DisplayName|**IsActive**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isactive`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|4|
|GlobalChoiceName|`field_security_permission_type`|

#### IsActive Choices/Options

|Value|Label|
|---|---|
|0|**Not Allowed**|
|4|**Allowed**|

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
|Description|**Status of the SupportUserTable**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`supportusertable_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the SupportUserTable**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`supportusertable_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_supportusertableId"></a> supportusertableId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**SupportUserTable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`supportusertableid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_TenantId"></a> TenantId

|Property|Value|
|---|---|
|Description||
|DisplayName|**TenantId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`tenantid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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

### <a name="BKMK_UPN"></a> UPN

|Property|Value|
|---|---|
|Description||
|DisplayName|**UPN**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`upn`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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

- [lk_supportusertable_createdby](#BKMK_lk_supportusertable_createdby)
- [lk_supportusertable_createdonbehalfby](#BKMK_lk_supportusertable_createdonbehalfby)
- [lk_supportusertable_modifiedby](#BKMK_lk_supportusertable_modifiedby)
- [lk_supportusertable_modifiedonbehalfby](#BKMK_lk_supportusertable_modifiedonbehalfby)
- [organization_supportusertable](#BKMK_organization_supportusertable)

### <a name="BKMK_lk_supportusertable_createdby"></a> lk_supportusertable_createdby

One-To-Many Relationship: [systemuser lk_supportusertable_createdby](systemuser.md#BKMK_lk_supportusertable_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_supportusertable_createdonbehalfby"></a> lk_supportusertable_createdonbehalfby

One-To-Many Relationship: [systemuser lk_supportusertable_createdonbehalfby](systemuser.md#BKMK_lk_supportusertable_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_supportusertable_modifiedby"></a> lk_supportusertable_modifiedby

One-To-Many Relationship: [systemuser lk_supportusertable_modifiedby](systemuser.md#BKMK_lk_supportusertable_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_supportusertable_modifiedonbehalfby"></a> lk_supportusertable_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_supportusertable_modifiedonbehalfby](systemuser.md#BKMK_lk_supportusertable_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_supportusertable"></a> organization_supportusertable

One-To-Many Relationship: [organization organization_supportusertable](organization.md#BKMK_organization_supportusertable)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [supportusertable_AsyncOperations](#BKMK_supportusertable_AsyncOperations)
- [supportusertable_BulkDeleteFailures](#BKMK_supportusertable_BulkDeleteFailures)
- [supportusertable_DuplicateBaseRecord](#BKMK_supportusertable_DuplicateBaseRecord)
- [supportusertable_DuplicateMatchingRecord](#BKMK_supportusertable_DuplicateMatchingRecord)
- [supportusertable_MailboxTrackingFolders](#BKMK_supportusertable_MailboxTrackingFolders)
- [supportusertable_PrincipalObjectAttributeAccesses](#BKMK_supportusertable_PrincipalObjectAttributeAccesses)
- [supportusertable_ProcessSession](#BKMK_supportusertable_ProcessSession)
- [supportusertable_SyncErrors](#BKMK_supportusertable_SyncErrors)

### <a name="BKMK_supportusertable_AsyncOperations"></a> supportusertable_AsyncOperations

Many-To-One Relationship: [asyncoperation supportusertable_AsyncOperations](asyncoperation.md#BKMK_supportusertable_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`supportusertable_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_supportusertable_BulkDeleteFailures"></a> supportusertable_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure supportusertable_BulkDeleteFailures](bulkdeletefailure.md#BKMK_supportusertable_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`supportusertable_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_supportusertable_DuplicateBaseRecord"></a> supportusertable_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord supportusertable_DuplicateBaseRecord](duplicaterecord.md#BKMK_supportusertable_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`supportusertable_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_supportusertable_DuplicateMatchingRecord"></a> supportusertable_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord supportusertable_DuplicateMatchingRecord](duplicaterecord.md#BKMK_supportusertable_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`supportusertable_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_supportusertable_MailboxTrackingFolders"></a> supportusertable_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder supportusertable_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_supportusertable_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`supportusertable_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_supportusertable_PrincipalObjectAttributeAccesses"></a> supportusertable_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess supportusertable_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_supportusertable_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`supportusertable_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_supportusertable_ProcessSession"></a> supportusertable_ProcessSession

Many-To-One Relationship: [processsession supportusertable_ProcessSession](processsession.md#BKMK_supportusertable_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`supportusertable_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_supportusertable_SyncErrors"></a> supportusertable_SyncErrors

Many-To-One Relationship: [syncerror supportusertable_SyncErrors](syncerror.md#BKMK_supportusertable_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`supportusertable_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.supportusertable?displayProperty=fullName>
