---
title: "Privileges Removal Setting (PrivilegesRemovalSetting) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Privileges Removal Setting (PrivilegesRemovalSetting) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Privileges Removal Setting (PrivilegesRemovalSetting) table/entity reference (Microsoft Dataverse)

Privileges Removal Setting

## Messages

The following table lists the messages for the Privileges Removal Setting (PrivilegesRemovalSetting) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|

## Properties

The following table lists selected properties for the Privileges Removal Setting (PrivilegesRemovalSetting) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Privileges Removal Setting** |
| **DisplayCollectionName** | **Privileges Removal Settings** |
| **SchemaName** | `PrivilegesRemovalSetting` |
| **CollectionSchemaName** | `PrivilegesRemovalSettings` |
| **EntitySetName** | `privilegesremovalsettings`|
| **LogicalName** | `privilegesremovalsetting` |
| **LogicalCollectionName** | `privilegesremovalsettings` |
| **PrimaryIdAttribute** | `privilegesremovalsettingid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ExtensionOfRecordId](#BKMK_ExtensionOfRecordId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsAppendRemoved](#BKMK_IsAppendRemoved)
- [IsAppendToRemoved](#BKMK_IsAppendToRemoved)
- [IsAssignRemoved](#BKMK_IsAssignRemoved)
- [IsCreateRemoved](#BKMK_IsCreateRemoved)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsDeleteRemoved](#BKMK_IsDeleteRemoved)
- [IsReadRemoved](#BKMK_IsReadRemoved)
- [IsWriteRemoved](#BKMK_IsWriteRemoved)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PrivilegesRemovalSettingId](#BKMK_PrivilegesRemovalSettingId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_ExtensionOfRecordId"></a> ExtensionOfRecordId

|Property|Value|
|---|---|
|Description|**Unique identifier of the Entity record.**|
|DisplayName|**Extension Entity Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`extensionofrecordid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|entity|

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

### <a name="BKMK_IsAppendRemoved"></a> IsAppendRemoved

|Property|Value|
|---|---|
|Description|**Not Supported**|
|DisplayName|**IsAppendRemoved**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isappendremoved`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`privilegesremovalsetting_isappendremoved`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsAppendToRemoved"></a> IsAppendToRemoved

|Property|Value|
|---|---|
|Description|**Not Supported**|
|DisplayName|**IsAppendToRemoved**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isappendtoremoved`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`privilegesremovalsetting_isappendtoremoved`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsAssignRemoved"></a> IsAssignRemoved

|Property|Value|
|---|---|
|Description|**Not Supported**|
|DisplayName|**IsAssignRemoved**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isassignremoved`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`privilegesremovalsetting_isassignremoved`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsCreateRemoved"></a> IsCreateRemoved

|Property|Value|
|---|---|
|Description|**Skip Create Privilege Check for the Entity, which means all authenticated users could create entity records**|
|DisplayName|**IsCreateRemoved**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`iscreateremoved`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`privilegesremovalsetting_iscreateremoved`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Is Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_IsDeleteRemoved"></a> IsDeleteRemoved

|Property|Value|
|---|---|
|Description|**Skip Delete Privilege Check for the Entity, which means all authenticated users could delete entity records**|
|DisplayName|**IsDeleteRemoved**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isdeleteremoved`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`privilegesremovalsetting_isdeleteremoved`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsReadRemoved"></a> IsReadRemoved

|Property|Value|
|---|---|
|Description|**Skip Read Privilege Check for the Entity, which means all authenticated users could read all entity records**|
|DisplayName|**IsReadRemoved**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isreadremoved`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`privilegesremovalsetting_isreadremoved`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsWriteRemoved"></a> IsWriteRemoved

|Property|Value|
|---|---|
|Description|**Skip Write Privilege Check for the Entity, which means all authenticated users could write to any entity records**|
|DisplayName|**IsWriteRemoved**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`iswriteremoved`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`privilegesremovalsetting_iswriteremoved`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name**|
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

### <a name="BKMK_PrivilegesRemovalSettingId"></a> PrivilegesRemovalSettingId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Privileges Removal Setting**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`privilegesremovalsettingid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentIdUnique"></a> ComponentIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Row id unique**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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
|DefaultFormValue||
|GlobalChoiceName|`componentstate`|

#### ComponentState Choices/Options

|Value|Label|
|---|---|
|0|**Published**|
|1|**Unpublished**|
|2|**Deleted**|
|3|**Deleted Unpublished**|

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

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Indicates whether the solution component is part of a managed solution.**|
|DisplayName|**Is Managed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

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
|Format|DateAndTime|
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

### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`supportingsolutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

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

- [lk_privilegesremovalsetting_createdby](#BKMK_lk_privilegesremovalsetting_createdby)
- [lk_privilegesremovalsetting_createdonbehalfby](#BKMK_lk_privilegesremovalsetting_createdonbehalfby)
- [lk_privilegesremovalsetting_modifiedby](#BKMK_lk_privilegesremovalsetting_modifiedby)
- [lk_privilegesremovalsetting_modifiedonbehalfby](#BKMK_lk_privilegesremovalsetting_modifiedonbehalfby)
- [organization_privilegesremovalsetting](#BKMK_organization_privilegesremovalsetting)
- [privilegesremovalsetting_extensionofrecordid](#BKMK_privilegesremovalsetting_extensionofrecordid)

### <a name="BKMK_lk_privilegesremovalsetting_createdby"></a> lk_privilegesremovalsetting_createdby

One-To-Many Relationship: [systemuser lk_privilegesremovalsetting_createdby](systemuser.md#BKMK_lk_privilegesremovalsetting_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_privilegesremovalsetting_createdonbehalfby"></a> lk_privilegesremovalsetting_createdonbehalfby

One-To-Many Relationship: [systemuser lk_privilegesremovalsetting_createdonbehalfby](systemuser.md#BKMK_lk_privilegesremovalsetting_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_privilegesremovalsetting_modifiedby"></a> lk_privilegesremovalsetting_modifiedby

One-To-Many Relationship: [systemuser lk_privilegesremovalsetting_modifiedby](systemuser.md#BKMK_lk_privilegesremovalsetting_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_privilegesremovalsetting_modifiedonbehalfby"></a> lk_privilegesremovalsetting_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_privilegesremovalsetting_modifiedonbehalfby](systemuser.md#BKMK_lk_privilegesremovalsetting_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_privilegesremovalsetting"></a> organization_privilegesremovalsetting

One-To-Many Relationship: [organization organization_privilegesremovalsetting](organization.md#BKMK_organization_privilegesremovalsetting)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegesremovalsetting_extensionofrecordid"></a> privilegesremovalsetting_extensionofrecordid

One-To-Many Relationship: [entity privilegesremovalsetting_extensionofrecordid](entity.md#BKMK_privilegesremovalsetting_extensionofrecordid)

|Property|Value|
|---|---|
|ReferencedEntity|`entity`|
|ReferencedAttribute|`entityid`|
|ReferencingAttribute|`extensionofrecordid`|
|ReferencingEntityNavigationPropertyName|`extensionofrecordid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Cascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [privilegesremovalsetting_AsyncOperations](#BKMK_privilegesremovalsetting_AsyncOperations)
- [privilegesremovalsetting_BulkDeleteFailures](#BKMK_privilegesremovalsetting_BulkDeleteFailures)
- [privilegesremovalsetting_DuplicateBaseRecord](#BKMK_privilegesremovalsetting_DuplicateBaseRecord)
- [privilegesremovalsetting_DuplicateMatchingRecord](#BKMK_privilegesremovalsetting_DuplicateMatchingRecord)
- [privilegesremovalsetting_MailboxTrackingFolders](#BKMK_privilegesremovalsetting_MailboxTrackingFolders)
- [privilegesremovalsetting_PrincipalObjectAttributeAccesses](#BKMK_privilegesremovalsetting_PrincipalObjectAttributeAccesses)
- [privilegesremovalsetting_ProcessSession](#BKMK_privilegesremovalsetting_ProcessSession)
- [privilegesremovalsetting_SyncErrors](#BKMK_privilegesremovalsetting_SyncErrors)

### <a name="BKMK_privilegesremovalsetting_AsyncOperations"></a> privilegesremovalsetting_AsyncOperations

Many-To-One Relationship: [asyncoperation privilegesremovalsetting_AsyncOperations](asyncoperation.md#BKMK_privilegesremovalsetting_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`privilegesremovalsetting_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_privilegesremovalsetting_BulkDeleteFailures"></a> privilegesremovalsetting_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure privilegesremovalsetting_BulkDeleteFailures](bulkdeletefailure.md#BKMK_privilegesremovalsetting_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`privilegesremovalsetting_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_privilegesremovalsetting_DuplicateBaseRecord"></a> privilegesremovalsetting_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord privilegesremovalsetting_DuplicateBaseRecord](duplicaterecord.md#BKMK_privilegesremovalsetting_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`privilegesremovalsetting_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_privilegesremovalsetting_DuplicateMatchingRecord"></a> privilegesremovalsetting_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord privilegesremovalsetting_DuplicateMatchingRecord](duplicaterecord.md#BKMK_privilegesremovalsetting_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`privilegesremovalsetting_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_privilegesremovalsetting_MailboxTrackingFolders"></a> privilegesremovalsetting_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder privilegesremovalsetting_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_privilegesremovalsetting_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`privilegesremovalsetting_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_privilegesremovalsetting_PrincipalObjectAttributeAccesses"></a> privilegesremovalsetting_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess privilegesremovalsetting_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_privilegesremovalsetting_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`privilegesremovalsetting_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_privilegesremovalsetting_ProcessSession"></a> privilegesremovalsetting_ProcessSession

Many-To-One Relationship: [processsession privilegesremovalsetting_ProcessSession](processsession.md#BKMK_privilegesremovalsetting_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`privilegesremovalsetting_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_privilegesremovalsetting_SyncErrors"></a> privilegesremovalsetting_SyncErrors

Many-To-One Relationship: [syncerror privilegesremovalsetting_SyncErrors](syncerror.md#BKMK_privilegesremovalsetting_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`privilegesremovalsetting_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.privilegesremovalsetting?displayProperty=fullName>
