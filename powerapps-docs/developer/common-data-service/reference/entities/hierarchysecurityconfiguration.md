---
title: "HierarchySecurityConfiguration Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the HierarchySecurityConfiguration entity."
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
# HierarchySecurityConfiguration Entity Reference



## Entity Properties

**DisplayName**: Hierarchy Security Configuration<br />
**DisplayCollectionName**: Hierarchy Security Configurations<br />
**SchemaName**: HierarchySecurityConfiguration<br />
**CollectionSchemaName**: HierarchySecurityConfiguration<br />
**LogicalName**: hierarchysecurityconfiguration<br />
**LogicalCollectionName**: hierarchysecurityconfigurations<br />
**EntitySetName**: hierarchysecurityconfigurations<br />
**PrimaryIdAttribute**: hierarchysecuritymodelingsettingid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [EntityName](#BKMK_EntityName)
- [HierarchySecurityModelingSettingId](#BKMK_HierarchySecurityModelingSettingId)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_EntityName"></a> EntityName

**Description**: Logical entity name of the entity that is configured for hierarchy security.<br />
**DisplayName**: Entity Name<br />
**LogicalName**: entityname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 64


### <a name="BKMK_HierarchySecurityModelingSettingId"></a> HierarchySecurityModelingSettingId

**Description**: Shows the entity used for the Hierarchy Security Modeling Configuration.<br />
**DisplayName**: <br />
**LogicalName**: hierarchysecuritymodelingsettingid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: objecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: versionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />


hierarchysecurityconfiguration

