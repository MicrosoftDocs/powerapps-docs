---
title: "Privilege Entity Reference (Common Data Service for Apps)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Privilege entity."

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
# Privilege Entity Reference

Permission to perform an action in Microsoft CRM. The platform checks for the privilege and rejects the attempt if the user does not hold the privilege.

## Entity Properties

**DisplayName**: Privilege<br />
**DisplayCollectionName**: Privileges<br />
**SchemaName**: Privilege<br />
**CollectionSchemaName**: Privileges<br />
**LogicalName**: privilege<br />
**LogicalCollectionName**: privileges<br />
**EntitySetName**: privileges<br />
**PrimaryIdAttribute**: privilegeid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AccessRight](#BKMK_AccessRight)
- [CanBeBasic](#BKMK_CanBeBasic)
- [CanBeDeep](#BKMK_CanBeDeep)
- [CanBeEntityReference](#BKMK_CanBeEntityReference)
- [CanBeGlobal](#BKMK_CanBeGlobal)
- [CanBeLocal](#BKMK_CanBeLocal)
- [CanBeParentEntityReference](#BKMK_CanBeParentEntityReference)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [Name](#BKMK_Name)
- [PrivilegeId](#BKMK_PrivilegeId)
- [PrivilegeRowId](#BKMK_PrivilegeRowId)


### <a name="BKMK_AccessRight"></a> AccessRight

**Description**: Rights a user has to an instance of an entity.<br />
**DisplayName**: <br />
**LogicalName**: accessright<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_CanBeBasic"></a> CanBeBasic

**Description**: Information that specifies whether the privilege applies to the user, the user's team, or objects shared by the user.<br />
**DisplayName**: <br />
**LogicalName**: canbebasic<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_CanBeDeep"></a> CanBeDeep

**Description**: Information that specifies whether the privilege applies to child business units of the business unit associated with the user.<br />
**DisplayName**: <br />
**LogicalName**: canbedeep<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_CanBeEntityReference"></a> CanBeEntityReference

**Description**: Information that specifies whether the privilege applies to the local reference of an external party.<br />
**DisplayName**: <br />
**LogicalName**: canbeentityreference<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_CanBeGlobal"></a> CanBeGlobal

**Description**: Information that specifies whether the privilege applies to the entire organization.<br />
**DisplayName**: <br />
**LogicalName**: canbeglobal<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_CanBeLocal"></a> CanBeLocal

**Description**: Information that specifies whether the privilege applies to the user's business unit.<br />
**DisplayName**: <br />
**LogicalName**: canbelocal<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_CanBeParentEntityReference"></a> CanBeParentEntityReference

**Description**: Information that specifies whether the privilege applies to parent reference of the external party.<br />
**DisplayName**: <br />
**LogicalName**: canbeparententityreference<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

**Description**: Version in which the component is introduced.<br />
**DisplayName**: Introduced Version<br />
**LogicalName**: introducedversion<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: VersionNumber<br />
**IsLocalizable**: False<br />
**MaxLength**: 48


### <a name="BKMK_Name"></a> Name

**Description**: Name of the privilege.<br />
**DisplayName**: <br />
**LogicalName**: name<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_PrivilegeId"></a> PrivilegeId

**Description**: Unique identifier of the privilege.<br />
**DisplayName**: <br />
**LogicalName**: privilegeid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_PrivilegeRowId"></a> PrivilegeRowId

**Description**: Unique identifier of the Privilege used when synchronizing customizations for the Microsoft Dynamics CRM client for Outlook<br />
**DisplayName**: App Module Unique Id<br />
**LogicalName**: privilegerowid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [IsDisabledWhenIntegrated](#BKMK_IsDisabledWhenIntegrated)
- [IsManaged](#BKMK_IsManaged)
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



### <a name="BKMK_IsDisabledWhenIntegrated"></a> IsDisabledWhenIntegrated

**Description**: Specifies whether the privilege is disabled.<br />
**DisplayName**: <br />
**LogicalName**: isdisabledwhenintegrated<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsManaged"></a> IsManaged

**Description**: Information that specifies whether this component is managed.<br />
**DisplayName**: State<br />
**LogicalName**: ismanaged<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Managed
- **FalseOption Value**: 0 **Label**: Unmanaged

**DefaultValue**: False


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

- [Privilege_AsyncOperations](#BKMK_Privilege_AsyncOperations)
- [Privilege_BulkDeleteFailures](#BKMK_Privilege_BulkDeleteFailures)
- [userentityinstancedata_privilege](#BKMK_userentityinstancedata_privilege)


### <a name="BKMK_Privilege_AsyncOperations"></a> Privilege_AsyncOperations

Same as asyncoperation entity [Privilege_AsyncOperations](asyncoperation.md#BKMK_Privilege_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Privilege_AsyncOperations<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_Privilege_BulkDeleteFailures"></a> Privilege_BulkDeleteFailures

Same as bulkdeletefailure entity [Privilege_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Privilege_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Privilege_BulkDeleteFailures<br />
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


### <a name="BKMK_userentityinstancedata_privilege"></a> userentityinstancedata_privilege

Same as userentityinstancedata entity [userentityinstancedata_privilege](userentityinstancedata.md#BKMK_userentityinstancedata_privilege) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_privilege<br />
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

<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the Privilege entity is the first entity in the relationship. Listed by **SchemaName**.

- [roleprivileges_association](#BKMK_roleprivileges_association)
- [ChannelAccessProfile_Privilege](#BKMK_ChannelAccessProfile_Privilege)


### <a name="BKMK_roleprivileges_association"></a> roleprivileges_association

**IntersectEntityName**: roleprivileges<br />
**Entity1LogicalName**: privilege<br />

- **Entity1IntersectAttribute**: privilegeid
- **Entity1NavigationPropertyName**: roleprivileges_association
- **Entity1AssociatedMenuConfiguration**:

  - **Behavior**: DoNotDisplay
  - **Group**: Details
  - **Label**: 
  - **Order**: 

**Entity2LogicalName**: [role](role.md)<br />

- **Entity2IntersectAttribute**: roleid
- **Entity2NavigationPropertyName**: roleprivileges_association
- **Entity2AssociatedMenuConfiguration**:

  - **Behavior**: DoNotDisplay
  - **Group**: Details
  - **Label**: 
  - **Order**: 

**IsCustomizable**: False<br />

### <a name="BKMK_ChannelAccessProfile_Privilege"></a> ChannelAccessProfile_Privilege

**IntersectEntityName**: channelaccessprofileentityaccesslevel<br />
**Entity1LogicalName**: privilege<br />

- **Entity1IntersectAttribute**: entityaccesslevelid
- **Entity1NavigationPropertyName**: ChannelAccessProfile_Privilege
- **Entity1AssociatedMenuConfiguration**:

  - **Behavior**: DoNotDisplay
  - **Group**: Details
  - **Label**: 
  - **Order**: 

**Entity2LogicalName**: [channelaccessprofile](channelaccessprofile.md)<br />

- **Entity2IntersectAttribute**: channelaccessprofileid
- **Entity2NavigationPropertyName**: ChannelAccessProfile_Privilege
- **Entity2AssociatedMenuConfiguration**:

  - **Behavior**: DoNotDisplay
  - **Group**: Details
  - **Label**: 
  - **Order**: 

**IsCustomizable**: False<br />
privilege

