---
title: "SharePointData Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the SharePointData entity."

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
# SharePointData Entity Reference

SharePoint's Data Corresponding to a user , Record , Location and Page

## Entity Properties

**DisplayName**: SharePoint Data<br />
**DisplayCollectionName**: SharePoint Data<br />
**SchemaName**: SharePointData<br />
**CollectionSchemaName**: SharePointData<br />
**LogicalName**: sharepointdata<br />
**LogicalCollectionName**: sharepointdatacollection<br />
**EntitySetName**: sharepointdatacollection<br />
**PrimaryIdAttribute**: sharepointdataid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Data](#BKMK_Data)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [SharePointDataId](#BKMK_SharePointDataId)


### <a name="BKMK_Data"></a> Data

**Description**: SharePoint Data Serialized<br />
**DisplayName**: SharePoint Data<br />
**LogicalName**: data<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_SharePointDataId"></a> SharePointDataId

**Description**: Unique identifier of the SharePoint data record.<br />
**DisplayName**: SharePoint data ID<br />
**LogicalName**: sharepointdataid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IsValid](#BKMK_IsValid)
- [Location](#BKMK_Location)
- [LocationName](#BKMK_LocationName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [NextPageToken](#BKMK_NextPageToken)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [PageNumber](#BKMK_PageNumber)
- [PreviousPageToken](#BKMK_PreviousPageToken)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [UserId](#BKMK_UserId)
- [UserName](#BKMK_UserName)
- [UserYomiName](#BKMK_UserYomiName)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the SharePoint Data.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the SharePoint Data was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the SharePoint Data.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_IsValid"></a> IsValid

**Description**: Is valid<br />
**DisplayName**: Is Valid<br />
**LogicalName**: isvalid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Valid Data
- **FalseOption Value**: 0 **Label**: Invalid Data

**DefaultValue**: False


### <a name="BKMK_Location"></a> Location

**Description**: Unique identifier of the user who created the SharePoint Data.<br />
**DisplayName**: Location<br />
**LogicalName**: location<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_LocationName"></a> LocationName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: locationname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the SharePoint Data.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the Sharepoint Data was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the SharePoint Data.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_NextPageToken"></a> NextPageToken

**Description**: Next Page Token of the SharePoint document.<br />
**DisplayName**: Next Page Token<br />
**LogicalName**: nextpagetoken<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization associated with the SharePoint Data.<br />
**DisplayName**: Organization<br />
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


### <a name="BKMK_PageNumber"></a> PageNumber

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: pagenumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_PreviousPageToken"></a> PreviousPageToken

**Description**: Previous Page Token of the SharePoint document.<br />
**DisplayName**: Previous Page Token<br />
**LogicalName**: previouspagetoken<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

**Description**: Regarding Object Id.<br />
**DisplayName**: Regarding Object Id.<br />
**LogicalName**: regardingobjectid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_UserId"></a> UserId

**Description**: Unique identifier of the user who created the SharePoint data.<br />
**DisplayName**: User Id<br />
**LogicalName**: userid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_UserName"></a> UserName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: username<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_UserYomiName"></a> UserYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: useryominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [lk_SharePointData_createdonbehalfby](#BKMK_lk_SharePointData_createdonbehalfby)
- [lk_SharePointData_createdby](#BKMK_lk_SharePointData_createdby)
- [lk_SharePointData_modifiedonbehalfby](#BKMK_lk_SharePointData_modifiedonbehalfby)
- [organization_sharepointdata](#BKMK_organization_sharepointdata)
- [lk_sharepointdata_user](#BKMK_lk_sharepointdata_user)
- [lk_SharePointData_modifiedby](#BKMK_lk_SharePointData_modifiedby)
- [sharepointdata_sharepointdocumentlocation](#BKMK_sharepointdata_sharepointdocumentlocation)


### <a name="BKMK_lk_SharePointData_createdonbehalfby"></a> lk_SharePointData_createdonbehalfby

See systemuser Entity [lk_SharePointData_createdonbehalfby](systemuser.md#BKMK_lk_SharePointData_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_SharePointData_createdby"></a> lk_SharePointData_createdby

See systemuser Entity [lk_SharePointData_createdby](systemuser.md#BKMK_lk_SharePointData_createdby) One-To-Many relationship.

### <a name="BKMK_lk_SharePointData_modifiedonbehalfby"></a> lk_SharePointData_modifiedonbehalfby

See systemuser Entity [lk_SharePointData_modifiedonbehalfby](systemuser.md#BKMK_lk_SharePointData_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_sharepointdata"></a> organization_sharepointdata

See organization Entity [organization_sharepointdata](organization.md#BKMK_organization_sharepointdata) One-To-Many relationship.

### <a name="BKMK_lk_sharepointdata_user"></a> lk_sharepointdata_user

See systemuser Entity [lk_sharepointdata_user](systemuser.md#BKMK_lk_sharepointdata_user) One-To-Many relationship.

### <a name="BKMK_lk_SharePointData_modifiedby"></a> lk_SharePointData_modifiedby

See systemuser Entity [lk_SharePointData_modifiedby](systemuser.md#BKMK_lk_SharePointData_modifiedby) One-To-Many relationship.

### <a name="BKMK_sharepointdata_sharepointdocumentlocation"></a> sharepointdata_sharepointdocumentlocation

See sharepointdocumentlocation Entity [sharepointdata_sharepointdocumentlocation](sharepointdocumentlocation.md#BKMK_sharepointdata_sharepointdocumentlocation) One-To-Many relationship.
sharepointdata

