---
title: "AppModuleRoles Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the AppModuleRoles entity."
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/31/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# AppModuleRoles Entity Reference

Security roles that have access to a business app.

## Entity Properties

**DisplayName**: App Module Roles<br />
**DisplayCollectionName**: App Module Roles<br />
**SchemaName**: AppModuleRoles<br />
**CollectionSchemaName**: <br />
**LogicalName**: appmoduleroles<br />
**LogicalCollectionName**: <br />
**EntitySetName**: appmodulerolescollection<br />
**PrimaryIdAttribute**: appmoduleroleid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AppModuleRoleId](#BKMK_AppModuleRoleId)
- [AppModuleRoleIdUnique](#BKMK_AppModuleRoleIdUnique)
- [IntroducedVersion](#BKMK_IntroducedVersion)


### <a name="BKMK_AppModuleRoleId"></a> AppModuleRoleId

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: appmoduleroleid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_AppModuleRoleIdUnique"></a> AppModuleRoleIdUnique

**Description**: Unique identifier of the App Module Roles used when synchronizing customizations for the Microsoft Dynamics 365 client for Outlook<br />
**DisplayName**: App Module Role Unique Id<br />
**LogicalName**: appmoduleroleidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

**Description**: Version in which the similarity rule is introduced.<br />
**DisplayName**: Introduced Version<br />
**LogicalName**: introducedversion<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: VersionNumber<br />
**IsLocalizable**: False<br />
**MaxLength**: 100

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AppModuleId](#BKMK_AppModuleId)
- [AppModuleIdName](#BKMK_AppModuleIdName)
- [ComponentState](#BKMK_ComponentState)
- [IsManaged](#BKMK_IsManaged)
- [OverwriteTime](#BKMK_OverwriteTime)
- [RoleId](#BKMK_RoleId)
- [RoleIdName](#BKMK_RoleIdName)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_AppModuleId"></a> AppModuleId

**Description**: Unique identifier of the app module.<br />
**DisplayName**: AppModule<br />
**LogicalName**: appmoduleid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: appmodule


### <a name="BKMK_AppModuleIdName"></a> AppModuleIdName

**Description**: name of the appmodule.<br />
**DisplayName**: AppModule<br />
**LogicalName**: appmoduleidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ComponentState"></a> ComponentState

**Description**: For internal use only<br />
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



### <a name="BKMK_IsManaged"></a> IsManaged

**Description**: Is Managed<br />
**DisplayName**: IsManaged<br />
**LogicalName**: ismanaged<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Managed
- **FalseOption Value**: 0 **Label**: Unmanaged

**DefaultValue**: False


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

**Description**: Internal use only<br />
**DisplayName**: Overwrite Time<br />
**LogicalName**: overwritetime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_RoleId"></a> RoleId

**Description**: <br />
**DisplayName**: Role<br />
**LogicalName**: roleid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: role


### <a name="BKMK_RoleIdName"></a> RoleIdName

**Description**: name of the role.<br />
**DisplayName**: Role<br />
**LogicalName**: roleidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


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

<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the AppModuleRoles entity is the first entity in the relationship. Listed by **SchemaName**.


### <a name="BKMK_appmoduleroles_association"></a> appmoduleroles_association

See appmodule Entity [appmoduleroles_association](appmodule.md#BKMK_appmoduleroles_association) Many-To-Many Relationship.
appmoduleroles

