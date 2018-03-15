---
title: "FieldPermission Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the FieldPermission entity."

services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/07/2018
ms.author: jdaly
---
# FieldPermission Entity Reference

Group of privileges used to categorize users to provide appropriate access to secured columns.

## Entity Properties

**DisplayName**: Field Permission<br />
**DisplayCollectionName**: Field Permissions<br />
**SchemaName**: FieldPermission<br />
**CollectionSchemaName**: FieldPermissions<br />
**LogicalName**: fieldpermission<br />
**LogicalCollectionName**: fieldpermissions<br />
**EntitySetName**: fieldpermissions<br />
**PrimaryIdAttribute**: fieldpermissionid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AttributeLogicalName](#BKMK_AttributeLogicalName)
- [CanCreate](#BKMK_CanCreate)
- [CanRead](#BKMK_CanRead)
- [CanUpdate](#BKMK_CanUpdate)
- [EntityName](#BKMK_EntityName)
- [FieldPermissionId](#BKMK_FieldPermissionId)
- [FieldSecurityProfileId](#BKMK_FieldSecurityProfileId)


### <a name="BKMK_AttributeLogicalName"></a> AttributeLogicalName

**Description**: Attribute Name.<br />
**DisplayName**: Name of the attribute for which this privilege is defined<br />
**LogicalName**: attributelogicalname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_CanCreate"></a> CanCreate

**Description**: Can this Profile create the attribute<br />
**DisplayName**: Can create the attribute<br />
**LogicalName**: cancreate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Not Allowed
- **Value**: 4 **Label**: Allowed



### <a name="BKMK_CanRead"></a> CanRead

**Description**: Can this Profile read the attribute<br />
**DisplayName**: Can Read the attribute<br />
**LogicalName**: canread<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Not Allowed
- **Value**: 4 **Label**: Allowed



### <a name="BKMK_CanUpdate"></a> CanUpdate

**Description**: Can this Profile update the attribute<br />
**DisplayName**: Can Update the attribute<br />
**LogicalName**: canupdate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Not Allowed
- **Value**: 4 **Label**: Allowed



### <a name="BKMK_EntityName"></a> EntityName

**Description**: Entity name.<br />
**DisplayName**: Name of the Entity for which this privilege is defined<br />
**LogicalName**: entityname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_FieldPermissionId"></a> FieldPermissionId

**Description**: Unique identifier of the Field Permission.<br />
**DisplayName**: Field Permission<br />
**LogicalName**: fieldpermissionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_FieldSecurityProfileId"></a> FieldSecurityProfileId

**Description**: Unique identifier of profile to which this privilege belongs.<br />
**DisplayName**: Profile<br />
**LogicalName**: fieldsecurityprofileid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: fieldsecurityprofile

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [FieldPermissionIdUnique](#BKMK_FieldPermissionIdUnique)
- [IsManaged](#BKMK_IsManaged)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ComponentState"></a> ComponentState

**Description**: For internal use only.<br />
**DisplayName**: Component State<br />
**LogicalName**: componentstate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Published
- **Value**: 1 **Label**: Unpublished
- **Value**: 2 **Label**: Deleted
- **Value**: 3 **Label**: Deleted Unpublished



### <a name="BKMK_FieldPermissionIdUnique"></a> FieldPermissionIdUnique

**Description**: For internal use only.<br />
**DisplayName**: Field Permission<br />
**LogicalName**: fieldpermissionidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_IsManaged"></a> IsManaged

**Description**: Indicates whether the solution component is part of a managed solution.<br />
**DisplayName**: Is Managed<br />
**LogicalName**: ismanaged<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Managed
- **FalseOption Value**: 0 **Label**: Unmanaged

**DefaultValue**: False


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier for the organization<br />
**DisplayName**: Organization Id<br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: 


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

**Description**: For internal use only.<br />
**DisplayName**: Record Overwrite Time<br />
**LogicalName**: overwritetime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_SolutionId"></a> SolutionId

**Description**: Unique identifier of the associated solution.<br />
**DisplayName**: Solution<br />
**LogicalName**: solutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

**Description**: For internal use only.<br />
**DisplayName**: Solution<br />
**LogicalName**: supportingsolutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: versionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [userentityinstancedata_fieldpermission](#BKMK_userentityinstancedata_fieldpermission)
- [FieldPermission_SyncErrors](#BKMK_FieldPermission_SyncErrors)


### <a name="BKMK_userentityinstancedata_fieldpermission"></a> userentityinstancedata_fieldpermission

Same as userentityinstancedata entity [userentityinstancedata_fieldpermission](userentityinstancedata.md#BKMK_userentityinstancedata_fieldpermission) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_fieldpermission<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_FieldPermission_SyncErrors"></a> FieldPermission_SyncErrors

Same as syncerror entity [FieldPermission_SyncErrors](syncerror.md#BKMK_FieldPermission_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: FieldPermission_SyncErrors<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.


### <a name="BKMK_lk_fieldpermission_fieldsecurityprofileid"></a> lk_fieldpermission_fieldsecurityprofileid

See fieldsecurityprofile Entity [lk_fieldpermission_fieldsecurityprofileid](fieldsecurityprofile.md#BKMK_lk_fieldpermission_fieldsecurityprofileid) One-To-Many relationship.
fieldpermission

