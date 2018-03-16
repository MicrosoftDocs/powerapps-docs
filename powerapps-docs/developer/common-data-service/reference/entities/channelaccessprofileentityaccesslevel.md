---
title: "ChannelAccessProfileEntityAccessLevel Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the ChannelAccessProfileEntityAccessLevel entity."

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
# ChannelAccessProfileEntityAccessLevel Entity Reference

Group of privileges used to categorize users to provide appropriate access to entities.

## Entity Properties

**DisplayName**: <br />
**DisplayCollectionName**: <br />
**SchemaName**: ChannelAccessProfileEntityAccessLevel<br />
**CollectionSchemaName**: <br />
**LogicalName**: channelaccessprofileentityaccesslevel<br />
**LogicalCollectionName**: <br />
**EntitySetName**: channelaccessprofileentityaccesslevels<br />
**PrimaryIdAttribute**: channelaccessprofileentityaccesslevelid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ChannelAccessProfileEntityAccessLevelId](#BKMK_ChannelAccessProfileEntityAccessLevelId)
- [EntityAccessLevelDepthMask](#BKMK_EntityAccessLevelDepthMask)


### <a name="BKMK_ChannelAccessProfileEntityAccessLevelId"></a> ChannelAccessProfileEntityAccessLevelId

**Description**: Unique identifier of the entity access level associated with the channel access profile.<br />
**DisplayName**: <br />
**LogicalName**: channelaccessprofileentityaccesslevelid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_EntityAccessLevelDepthMask"></a> EntityAccessLevelDepthMask

**Description**: System-generated attribute that stores the privileges associated with the role.<br />
**DisplayName**: <br />
**LogicalName**: entityaccessleveldepthmask<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ChannelAccessProfileEntityAccessLevelIdUnique](#BKMK_ChannelAccessProfileEntityAccessLevelIdUnique)
- [ChannelAccessProfileId](#BKMK_ChannelAccessProfileId)
- [ComponentState](#BKMK_ComponentState)
- [EntityAccessLevelId](#BKMK_EntityAccessLevelId)
- [IsManaged](#BKMK_IsManaged)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ChannelAccessProfileEntityAccessLevelIdUnique"></a> ChannelAccessProfileEntityAccessLevelIdUnique

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: channelaccessprofileentityaccesslevelidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ChannelAccessProfileId"></a> ChannelAccessProfileId

**Description**: Unique identifier of the channel access profile.<br />
**DisplayName**: <br />
**LogicalName**: channelaccessprofileid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


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



### <a name="BKMK_EntityAccessLevelId"></a> EntityAccessLevelId

**Description**: Unique identifier of the entity access level associated with the channel access profile<br />
**DisplayName**: <br />
**LogicalName**: entityaccesslevelid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_IsManaged"></a> IsManaged

**Description**: <br />
**DisplayName**: <br />
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

<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the ChannelAccessProfileEntityAccessLevel entity is the first entity in the relationship. Listed by **SchemaName**.


### <a name="BKMK_ChannelAccessProfile_Privilege"></a> ChannelAccessProfile_Privilege

See privilege Entity [ChannelAccessProfile_Privilege](privilege.md#BKMK_ChannelAccessProfile_Privilege) Many-To-Many Relationship.
channelaccessprofileentityaccesslevel

