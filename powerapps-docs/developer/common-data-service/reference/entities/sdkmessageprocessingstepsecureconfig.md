---
title: "SdkMessageProcessingStepSecureConfig Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the SdkMessageProcessingStepSecureConfig entity."
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
# SdkMessageProcessingStepSecureConfig Entity Reference

Non-public custom configuration that is passed to a plug-in's constructor.

## Entity Properties

**DisplayName**: Sdk Message Processing Step Secure Configuration<br />
**DisplayCollectionName**: Sdk Message Processing Step Secure Configurations<br />
**SchemaName**: SdkMessageProcessingStepSecureConfig<br />
**CollectionSchemaName**: SdkMessageProcessingStepSecureConfigs<br />
**LogicalName**: sdkmessageprocessingstepsecureconfig<br />
**LogicalCollectionName**: sdkmessageprocessingstepsecureconfigs<br />
**EntitySetName**: sdkmessageprocessingstepsecureconfigs<br />
**PrimaryIdAttribute**: sdkmessageprocessingstepsecureconfigid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [SdkMessageProcessingStepSecureConfigId](#BKMK_SdkMessageProcessingStepSecureConfigId)
- [SecureConfig](#BKMK_SecureConfig)


### <a name="BKMK_SdkMessageProcessingStepSecureConfigId"></a> SdkMessageProcessingStepSecureConfigId

**Description**: Unique identifier of the SDK message processing step secure configuration.<br />
**DisplayName**: <br />
**LogicalName**: sdkmessageprocessingstepsecureconfigid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SecureConfig"></a> SecureConfig

**Description**: Secure step-specific configuration for the plug-in type that is passed to the plug-in's constructor at run time.<br />
**DisplayName**: Secure Configuration<br />
**LogicalName**: secureconfig<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [CustomizationLevel](#BKMK_CustomizationLevel)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [SdkMessageProcessingStepSecureConfigIdUnique](#BKMK_SdkMessageProcessingStepSecureConfigIdUnique)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the SDK message processing step.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: True<br />
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


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the SDK message processing step was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the sdkmessageprocessingstepsecureconfig.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: True<br />
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


### <a name="BKMK_CustomizationLevel"></a> CustomizationLevel

**Description**: Customization level of the SDK message processing step secure configuration.<br />
**DisplayName**: <br />
**LogicalName**: customizationlevel<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 255<br />
**MinValue**: -255


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the SDK message processing step.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: True<br />
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


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the SDK message processing step was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the sdkmessageprocessingstepsecureconfig.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: True<br />
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

**Description**: Unique identifier of the organization with which the SDK message processing step is associated.<br />
**DisplayName**: <br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: organization


### <a name="BKMK_SdkMessageProcessingStepSecureConfigIdUnique"></a> SdkMessageProcessingStepSecureConfigIdUnique

**Description**: Unique identifier of the SDK message processing step.<br />
**DisplayName**: <br />
**LogicalName**: sdkmessageprocessingstepsecureconfigidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [userentityinstancedata_sdkmessageprocessingstepsecureconfig](#BKMK_userentityinstancedata_sdkmessageprocessingstepsecureconfig)
- [sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep](#BKMK_sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep)


### <a name="BKMK_userentityinstancedata_sdkmessageprocessingstepsecureconfig"></a> userentityinstancedata_sdkmessageprocessingstepsecureconfig

Same as userentityinstancedata entity [userentityinstancedata_sdkmessageprocessingstepsecureconfig](userentityinstancedata.md#BKMK_userentityinstancedata_sdkmessageprocessingstepsecureconfig) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_sdkmessageprocessingstepsecureconfig<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep"></a> sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep

Same as sdkmessageprocessingstep entity [sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstep<br />
**ReferencingAttribute**: sdkmessageprocessingstepsecureconfigid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby](#BKMK_lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby)
- [modifiedby_sdkmessageprocessingstepsecureconfig](#BKMK_modifiedby_sdkmessageprocessingstepsecureconfig)
- [lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby](#BKMK_lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby)
- [organization_sdkmessageprocessingstepsecureconfig](#BKMK_organization_sdkmessageprocessingstepsecureconfig)
- [createdby_sdkmessageprocessingstepsecureconfig](#BKMK_createdby_sdkmessageprocessingstepsecureconfig)


### <a name="BKMK_lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby"></a> lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby

See systemuser Entity [lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby](systemuser.md#BKMK_lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_modifiedby_sdkmessageprocessingstepsecureconfig"></a> modifiedby_sdkmessageprocessingstepsecureconfig

See systemuser Entity [modifiedby_sdkmessageprocessingstepsecureconfig](systemuser.md#BKMK_modifiedby_sdkmessageprocessingstepsecureconfig) One-To-Many relationship.

### <a name="BKMK_lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby"></a> lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby

See systemuser Entity [lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby](systemuser.md#BKMK_lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_sdkmessageprocessingstepsecureconfig"></a> organization_sdkmessageprocessingstepsecureconfig

See organization Entity [organization_sdkmessageprocessingstepsecureconfig](organization.md#BKMK_organization_sdkmessageprocessingstepsecureconfig) One-To-Many relationship.

### <a name="BKMK_createdby_sdkmessageprocessingstepsecureconfig"></a> createdby_sdkmessageprocessingstepsecureconfig

See systemuser Entity [createdby_sdkmessageprocessingstepsecureconfig](systemuser.md#BKMK_createdby_sdkmessageprocessingstepsecureconfig) One-To-Many relationship.
sdkmessageprocessingstepsecureconfig

