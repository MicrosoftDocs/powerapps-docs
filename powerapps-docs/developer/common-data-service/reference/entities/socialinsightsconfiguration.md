---
title: "SocialInsightsConfiguration Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the SocialInsightsConfiguration entity."

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
# SocialInsightsConfiguration Entity Reference

Configuration for the social insights.

## Entity Properties

**DisplayName**: SocialInsightsConfiguration<br />
**DisplayCollectionName**: SocialInsightsConfigurations<br />
**SchemaName**: SocialInsightsConfiguration<br />
**CollectionSchemaName**: SocialInsightsConfigurations<br />
**LogicalName**: socialinsightsconfiguration<br />
**LogicalCollectionName**: socialinsightsconfigurations<br />
**EntitySetName**: socialinsightsconfigurations<br />
**PrimaryIdAttribute**: socialinsightsconfigurationid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ControlId](#BKMK_ControlId)
- [FormId](#BKMK_FormId)
- [FormTypeCode](#BKMK_FormTypeCode)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectIdYomiName](#BKMK_RegardingObjectIdYomiName)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [SocialDataItemId](#BKMK_SocialDataItemId)
- [SocialDataItemType](#BKMK_SocialDataItemType)
- [SocialDataParameters](#BKMK_SocialDataParameters)
- [SocialInsightsConfigurationId](#BKMK_SocialInsightsConfigurationId)


### <a name="BKMK_ControlId"></a> ControlId

**Description**: Id of the control.<br />
**DisplayName**: Control Id<br />
**LogicalName**: controlid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_FormId"></a> FormId

**Description**: Unique identifier of the form with which the like is associated.<br />
**DisplayName**: Associated Form<br />
**LogicalName**: formid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: post


### <a name="BKMK_FormTypeCode"></a> FormTypeCode

**Description**: Type of form.<br />
**DisplayName**: Form Type<br />
**LogicalName**: formtypecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1030 **Label**: System Form
- **Value**: 1031 **Label**: User Form



### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

**Description**: Unique identifier of the associated record.<br />
**DisplayName**: Regarding<br />
**LogicalName**: regardingobjectid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: 


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjectidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_RegardingObjectIdYomiName"></a> RegardingObjectIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjectidyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_SocialDataItemId"></a> SocialDataItemId

**Description**: Data Item Id for social data.<br />
**DisplayName**: Social Data Item Id<br />
**LogicalName**: socialdataitemid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_SocialDataItemType"></a> SocialDataItemType

**Description**: Type of social data item.<br />
**DisplayName**: Social Data Item Type<br />
**LogicalName**: socialdataitemtype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Search Item
- **Value**: 2 **Label**: Class



### <a name="BKMK_SocialDataParameters"></a> SocialDataParameters

**Description**: Parameters used to render social data.<br />
**DisplayName**: Social Data Parameters<br />
**LogicalName**: socialdataparameters<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1000


### <a name="BKMK_SocialInsightsConfigurationId"></a> SocialInsightsConfigurationId

**Description**: Shows the ID of the social insights configuration.<br />
**DisplayName**: SocialInsightsConfigurationId<br />
**LogicalName**: socialinsightsconfigurationid<br />
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
- [FormIdName](#BKMK_FormIdName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the record.<br />
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

**Description**: Date and time when the record was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the record.<br />
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


### <a name="BKMK_FormIdName"></a> FormIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: formidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who modified the record.<br />
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

**Description**: Date and time when the record was modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who modified the record.<br />
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


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization associated with the solution.<br />
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [lk_socialinsightsconfiguration_modifiedby](#BKMK_lk_socialinsightsconfiguration_modifiedby)
- [lk_socialinsightsconfiguration_createdonbehalfby](#BKMK_lk_socialinsightsconfiguration_createdonbehalfby)
- [lk_socialinsightsconfiguration_createdby](#BKMK_lk_socialinsightsconfiguration_createdby)
- [socialinsightsconfiguration_systemform](#BKMK_socialinsightsconfiguration_systemform)
- [organization_socialinsightsconfiguration](#BKMK_organization_socialinsightsconfiguration)
- [lk_socialinsightsconfiguration_modifiedonbehalfby](#BKMK_lk_socialinsightsconfiguration_modifiedonbehalfby)
- [socialinsightsconfiguration_userform](#BKMK_socialinsightsconfiguration_userform)


### <a name="BKMK_lk_socialinsightsconfiguration_modifiedby"></a> lk_socialinsightsconfiguration_modifiedby

See systemuser Entity [lk_socialinsightsconfiguration_modifiedby](systemuser.md#BKMK_lk_socialinsightsconfiguration_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_socialinsightsconfiguration_createdonbehalfby"></a> lk_socialinsightsconfiguration_createdonbehalfby

See systemuser Entity [lk_socialinsightsconfiguration_createdonbehalfby](systemuser.md#BKMK_lk_socialinsightsconfiguration_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_socialinsightsconfiguration_createdby"></a> lk_socialinsightsconfiguration_createdby

See systemuser Entity [lk_socialinsightsconfiguration_createdby](systemuser.md#BKMK_lk_socialinsightsconfiguration_createdby) One-To-Many relationship.

### <a name="BKMK_socialinsightsconfiguration_systemform"></a> socialinsightsconfiguration_systemform

See systemform Entity [socialinsightsconfiguration_systemform](systemform.md#BKMK_socialinsightsconfiguration_systemform) One-To-Many relationship.

### <a name="BKMK_organization_socialinsightsconfiguration"></a> organization_socialinsightsconfiguration

See organization Entity [organization_socialinsightsconfiguration](organization.md#BKMK_organization_socialinsightsconfiguration) One-To-Many relationship.

### <a name="BKMK_lk_socialinsightsconfiguration_modifiedonbehalfby"></a> lk_socialinsightsconfiguration_modifiedonbehalfby

See systemuser Entity [lk_socialinsightsconfiguration_modifiedonbehalfby](systemuser.md#BKMK_lk_socialinsightsconfiguration_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_socialinsightsconfiguration_userform"></a> socialinsightsconfiguration_userform

See userform Entity [socialinsightsconfiguration_userform](userform.md#BKMK_socialinsightsconfiguration_userform) One-To-Many relationship.
socialinsightsconfiguration

