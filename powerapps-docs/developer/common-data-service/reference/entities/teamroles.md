---
title: "TeamRoles Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the TeamRoles entity."
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
ms.date: 03/07/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# TeamRoles Entity Reference



## Entity Properties

**DisplayName**: <br />
**DisplayCollectionName**: <br />
**SchemaName**: TeamRoles<br />
**CollectionSchemaName**: <br />
**LogicalName**: teamroles<br />
**LogicalCollectionName**: <br />
**EntitySetName**: teamrolescollection<br />
**PrimaryIdAttribute**: teamroleid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.


### <a name="BKMK_TeamRoleId"></a> TeamRoleId

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: teamroleid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [RoleId](#BKMK_RoleId)
- [TeamId](#BKMK_TeamId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_RoleId"></a> RoleId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: roleid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_TeamId"></a> TeamId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: teamid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
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

Relationship details provided where the TeamRoles entity is the first entity in the relationship. Listed by **SchemaName**.


### <a name="BKMK_teamroles_association"></a> teamroles_association

See team Entity [teamroles_association](team.md#BKMK_teamroles_association) Many-To-Many Relationship.
teamroles

