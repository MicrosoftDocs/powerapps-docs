---
title: "TeamProfiles Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the TeamProfiles entity."

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
---
# TeamProfiles Entity Reference

Team Profiles

## Entity Properties

**DisplayName**: Team Profiles<br />
**DisplayCollectionName**: Team Profiles<br />
**SchemaName**: TeamProfiles<br />
**CollectionSchemaName**: TeamProfiles<br />
**LogicalName**: teamprofiles<br />
**LogicalCollectionName**: teamprofilescollection<br />
**EntitySetName**: teamprofilescollection<br />
**PrimaryIdAttribute**: teamprofileid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.


### <a name="BKMK_TeamProfileId"></a> TeamProfileId

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: teamprofileid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [FieldSecurityProfileId](#BKMK_FieldSecurityProfileId)
- [TeamId](#BKMK_TeamId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_FieldSecurityProfileId"></a> FieldSecurityProfileId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: fieldsecurityprofileid<br />
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

Relationship details provided where the TeamProfiles entity is the first entity in the relationship. Listed by **SchemaName**.


### <a name="BKMK_teamprofiles_association"></a> teamprofiles_association

See team Entity [teamprofiles_association](team.md#BKMK_teamprofiles_association) Many-To-Many Relationship.
teamprofiles

