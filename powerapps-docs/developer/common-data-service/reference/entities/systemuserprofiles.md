---
title: "SystemUserProfiles Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the SystemUserProfiles entity."
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
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# SystemUserProfiles Entity Reference



## Entity Properties

**DisplayName**: <br />
**DisplayCollectionName**: <br />
**SchemaName**: SystemUserProfiles<br />
**CollectionSchemaName**: <br />
**LogicalName**: systemuserprofiles<br />
**LogicalCollectionName**: <br />
**EntitySetName**: systemuserprofilescollection<br />
**PrimaryIdAttribute**: systemuserprofileid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.


### <a name="BKMK_SystemUserProfileId"></a> SystemUserProfileId

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: systemuserprofileid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [FieldSecurityProfileId](#BKMK_FieldSecurityProfileId)
- [SystemUserId](#BKMK_SystemUserId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_FieldSecurityProfileId"></a> FieldSecurityProfileId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: fieldsecurityprofileid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SystemUserId"></a> SystemUserId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: systemuserid<br />
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

Relationship details provided where the SystemUserProfiles entity is the first entity in the relationship. Listed by **SchemaName**.


### <a name="BKMK_systemuserprofiles_association"></a> systemuserprofiles_association

See systemuser Entity [systemuserprofiles_association](systemuser.md#BKMK_systemuserprofiles_association) Many-To-Many Relationship.
systemuserprofiles

