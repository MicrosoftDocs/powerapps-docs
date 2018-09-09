---
title: "SystemUserLicenses Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the SystemUserLicenses entity."
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
# SystemUserLicenses Entity Reference



## Entity Properties

**DisplayName**: <br />
**DisplayCollectionName**: <br />
**SchemaName**: SystemUserLicenses<br />
**CollectionSchemaName**: <br />
**LogicalName**: systemuserlicenses<br />
**LogicalCollectionName**: <br />
**EntitySetName**: systemuserlicensescollection<br />
**PrimaryIdAttribute**: systemuserlicenseid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.


### <a name="BKMK_SystemUserLicenseId"></a> SystemUserLicenseId

**Description**: Unique identifier of the user licenses.<br />
**DisplayName**: <br />
**LogicalName**: systemuserlicenseid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [LicenseId](#BKMK_LicenseId)
- [SystemUserId](#BKMK_SystemUserId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_LicenseId"></a> LicenseId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: licenseid<br />
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
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />


systemuserlicenses

