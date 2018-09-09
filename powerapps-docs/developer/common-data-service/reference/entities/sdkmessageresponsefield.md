---
title: "SdkMessageResponseField Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the SdkMessageResponseField entity."
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
# SdkMessageResponseField Entity Reference

For internal use only.

## Entity Properties

**DisplayName**: Sdk Message Response Field<br />
**DisplayCollectionName**: Sdk MessageResponse Fields<br />
**SchemaName**: SdkMessageResponseField<br />
**CollectionSchemaName**: SdkMessageResponseFields<br />
**LogicalName**: sdkmessageresponsefield<br />
**LogicalCollectionName**: sdkmessageresponsefields<br />
**EntitySetName**: sdkmessageresponsefields<br />
**PrimaryIdAttribute**: sdkmessageresponsefieldid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ClrFormatter](#BKMK_ClrFormatter)
- [Formatter](#BKMK_Formatter)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [Name](#BKMK_Name)
- [ParameterBindingInformation](#BKMK_ParameterBindingInformation)
- [PublicName](#BKMK_PublicName)
- [SdkMessageResponseFieldId](#BKMK_SdkMessageResponseFieldId)
- [Value](#BKMK_Value)


### <a name="BKMK_ClrFormatter"></a> ClrFormatter

**Description**: Common language runtime (CLR)-based formatter of the SDK message response field.<br />
**DisplayName**: <br />
**LogicalName**: clrformatter<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_Formatter"></a> Formatter

**Description**: Formatter for the SDK message response field.<br />
**DisplayName**: <br />
**LogicalName**: formatter<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

**Description**: Version in which the component is introduced.<br />
**DisplayName**: Introduced Version<br />
**LogicalName**: introducedversion<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: VersionNumber<br />
**IsLocalizable**: False<br />
**MaxLength**: 48


### <a name="BKMK_Name"></a> Name

**Description**: Name of the SDK message response field.<br />
**DisplayName**: <br />
**LogicalName**: name<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_ParameterBindingInformation"></a> ParameterBindingInformation

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: parameterbindinginformation<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 128


### <a name="BKMK_PublicName"></a> PublicName

**Description**: Public name of the SDK message response field.<br />
**DisplayName**: <br />
**LogicalName**: publicname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_SdkMessageResponseFieldId"></a> SdkMessageResponseFieldId

**Description**: Unique identifier of the SDK message response field entity.<br />
**DisplayName**: <br />
**LogicalName**: sdkmessageresponsefieldid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_Value"></a> Value

**Description**: Actual value of the SDK message response field.<br />
**DisplayName**: <br />
**LogicalName**: value<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [CustomizationLevel](#BKMK_CustomizationLevel)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [Position](#BKMK_Position)
- [SdkMessageResponseFieldIdUnique](#BKMK_SdkMessageResponseFieldIdUnique)
- [SdkMessageResponseId](#BKMK_SdkMessageResponseId)
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



### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the SDK message response field.<br />
**DisplayName**: <br />
**LogicalName**: createdby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the SDK message response field was created.<br />
**DisplayName**: <br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the sdkmessageresponsefield.<br />
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


### <a name="BKMK_CustomizationLevel"></a> CustomizationLevel

**Description**: Customization level of the SDK message response field.<br />
**DisplayName**: <br />
**LogicalName**: customizationlevel<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 255<br />
**MinValue**: -255


### <a name="BKMK_IsManaged"></a> IsManaged

**Description**: Information that specifies whether this component is managed.<br />
**DisplayName**: State<br />
**LogicalName**: ismanaged<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Managed
- **FalseOption Value**: 0 **Label**: Unmanaged

**DefaultValue**: False


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the SDK message response field.<br />
**DisplayName**: <br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the SDK message response field was last modified.<br />
**DisplayName**: <br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the sdkmessageresponsefield.<br />
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

**Description**: Unique identifier of the organization with which the SDK message response field is associated.<br />
**DisplayName**: <br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: organization


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


### <a name="BKMK_Position"></a> Position

**Description**: Position of the Sdk message response field<br />
**DisplayName**: <br />
**LogicalName**: position<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_SdkMessageResponseFieldIdUnique"></a> SdkMessageResponseFieldIdUnique

**Description**: Unique identifier of the SDK message response field.<br />
**DisplayName**: <br />
**LogicalName**: sdkmessageresponsefieldidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SdkMessageResponseId"></a> SdkMessageResponseId

**Description**: Unique identifier of the message response with which the SDK message response field is associated.<br />
**DisplayName**: <br />
**LogicalName**: sdkmessageresponseid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: sdkmessageresponse


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

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: versionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_userentityinstancedata_sdkmessageresponsefield"></a> userentityinstancedata_sdkmessageresponsefield

Same as userentityinstancedata entity [userentityinstancedata_sdkmessageresponsefield](userentityinstancedata.md#BKMK_userentityinstancedata_sdkmessageresponsefield) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_sdkmessageresponsefield<br />
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [modifiedby_sdkmessageresponsefield](#BKMK_modifiedby_sdkmessageresponsefield)
- [lk_sdkmessageresponsefield_modifiedonbehalfby](#BKMK_lk_sdkmessageresponsefield_modifiedonbehalfby)
- [createdby_sdkmessageresponsefield](#BKMK_createdby_sdkmessageresponsefield)
- [organization_sdkmessageresponsefield](#BKMK_organization_sdkmessageresponsefield)
- [messageresponse_sdkmessageresponsefield](#BKMK_messageresponse_sdkmessageresponsefield)
- [lk_sdkmessageresponsefield_createdonbehalfby](#BKMK_lk_sdkmessageresponsefield_createdonbehalfby)


### <a name="BKMK_modifiedby_sdkmessageresponsefield"></a> modifiedby_sdkmessageresponsefield

See systemuser Entity [modifiedby_sdkmessageresponsefield](systemuser.md#BKMK_modifiedby_sdkmessageresponsefield) One-To-Many relationship.

### <a name="BKMK_lk_sdkmessageresponsefield_modifiedonbehalfby"></a> lk_sdkmessageresponsefield_modifiedonbehalfby

See systemuser Entity [lk_sdkmessageresponsefield_modifiedonbehalfby](systemuser.md#BKMK_lk_sdkmessageresponsefield_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_createdby_sdkmessageresponsefield"></a> createdby_sdkmessageresponsefield

See systemuser Entity [createdby_sdkmessageresponsefield](systemuser.md#BKMK_createdby_sdkmessageresponsefield) One-To-Many relationship.

### <a name="BKMK_organization_sdkmessageresponsefield"></a> organization_sdkmessageresponsefield

See organization Entity [organization_sdkmessageresponsefield](organization.md#BKMK_organization_sdkmessageresponsefield) One-To-Many relationship.

### <a name="BKMK_messageresponse_sdkmessageresponsefield"></a> messageresponse_sdkmessageresponsefield

See sdkmessageresponse Entity [messageresponse_sdkmessageresponsefield](sdkmessageresponse.md#BKMK_messageresponse_sdkmessageresponsefield) One-To-Many relationship.

### <a name="BKMK_lk_sdkmessageresponsefield_createdonbehalfby"></a> lk_sdkmessageresponsefield_createdonbehalfby

See systemuser Entity [lk_sdkmessageresponsefield_createdonbehalfby](systemuser.md#BKMK_lk_sdkmessageresponsefield_createdonbehalfby) One-To-Many relationship.
sdkmessageresponsefield

