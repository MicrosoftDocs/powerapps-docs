---
title: "OrganizationUI Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the OrganizationUI entity."
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
# OrganizationUI Entity Reference

Entity customizations including form layout and icons. Includes current and past versions.

## Entity Properties

**DisplayName**: Organization UI<br />
**DisplayCollectionName**: Organization UI Settings<br />
**SchemaName**: OrganizationUI<br />
**CollectionSchemaName**: OrganizationUIs<br />
**LogicalName**: organizationui<br />
**LogicalCollectionName**: organizationuis<br />
**EntitySetName**: organizationuis<br />
**PrimaryIdAttribute**: formid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [FieldXml](#BKMK_FieldXml)
- [FormId](#BKMK_FormId)
- [FormXml](#BKMK_FormXml)
- [GridIcon](#BKMK_GridIcon)
- [IsCustomizable](#BKMK_IsCustomizable)
- [LargeEntityIcon](#BKMK_LargeEntityIcon)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [OutlookShortcutIcon](#BKMK_OutlookShortcutIcon)
- [PreviewColumnsetXml](#BKMK_PreviewColumnsetXml)
- [PreviewXml](#BKMK_PreviewXml)
- [Version](#BKMK_Version)


### <a name="BKMK_FieldXml"></a> FieldXml

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: fieldxml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_FormId"></a> FormId

**Description**: Unique identifier of the record type form.<br />
**DisplayName**: <br />
**LogicalName**: formid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_FormXml"></a> FormXml

**Description**: XML representation of the form layout.<br />
**DisplayName**: <br />
**LogicalName**: formxml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_GridIcon"></a> GridIcon

**Description**: Binary representation of the icon used in record type grid views.<br />
**DisplayName**: <br />
**LogicalName**: gridicon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_IsCustomizable"></a> IsCustomizable

**Description**: Information that specifies whether this component can be customized.<br />
**DisplayName**: Customizable<br />
**LogicalName**: iscustomizable<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: ManagedProperty<br />


### <a name="BKMK_LargeEntityIcon"></a> LargeEntityIcon

**Description**: Binary representation of the large icon used in the record type form.<br />
**DisplayName**: <br />
**LogicalName**: largeentityicon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

**Description**: Code that represents the record type.<br />
**DisplayName**: <br />
**LogicalName**: objecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_OutlookShortcutIcon"></a> OutlookShortcutIcon

**Description**: Binary representation of the large icon used in the Microsoft Dynamics 365 client for Outlook for this record type.<br />
**DisplayName**: <br />
**LogicalName**: outlookshortcuticon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_PreviewColumnsetXml"></a> PreviewColumnsetXml

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: previewcolumnsetxml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_PreviewXml"></a> PreviewXml

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: previewxml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_Version"></a> Version

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: version<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [FormIdUnique](#BKMK_FormIdUnique)
- [IsManaged](#BKMK_IsManaged)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
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



### <a name="BKMK_FormIdUnique"></a> FormIdUnique

**Description**: Unique identifier of the form used when synchronizing customizations for the Microsoft Dynamics 365 client for Outlook.<br />
**DisplayName**: <br />
**LogicalName**: formidunique<br />
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


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization.<br />
**DisplayName**: <br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: organization


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: organizationidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


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

**Description**: Represents a version of customizations to be synchronized with the Microsoft Dynamics 365 client for Outlook.<br />
**DisplayName**: <br />
**LogicalName**: versionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.


### <a name="BKMK_lk_organizationui_organizationid"></a> lk_organizationui_organizationid

See organization Entity [lk_organizationui_organizationid](organization.md#BKMK_lk_organizationui_organizationid) One-To-Many relationship.
organizationui

