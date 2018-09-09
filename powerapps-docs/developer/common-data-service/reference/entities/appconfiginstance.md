---
title: "AppConfigInstance Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the AppConfigInstance entity."
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
# AppConfigInstance Entity Reference

Contains a property or a list of properties from the app configuration master list that can be customized for any app in Dynamics 365. For internal use only.

## Entity Properties

**DisplayName**: App Configuration Instance<br />
**DisplayCollectionName**: App Configuration Instance<br />
**SchemaName**: AppConfigInstance<br />
**CollectionSchemaName**: AppConfigInstances<br />
**LogicalName**: appconfiginstance<br />
**LogicalCollectionName**: appconfiginstances<br />
**EntitySetName**: appconfiginstances<br />
**PrimaryIdAttribute**: appconfiginstanceid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AppConfigId](#BKMK_AppConfigId)
- [AppConfigIdUnique](#BKMK_AppConfigIdUnique)
- [AppConfigInstanceIdUnique](#BKMK_AppConfigInstanceIdUnique)
- [AppConfigMasterId](#BKMK_AppConfigMasterId)
- [ComponentType](#BKMK_ComponentType)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [ObjectId](#BKMK_ObjectId)
- [Value](#BKMK_Value)


### <a name="BKMK_AppConfigId"></a> AppConfigId

**Description**: System-calculated App Configuration unique identifier.<br />
**DisplayName**: App Config ID<br />
**LogicalName**: appconfigid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Lookup<br />
**Targets**: appconfig


### <a name="BKMK_AppConfigIdUnique"></a> AppConfigIdUnique

**Description**: Enter the App Configuration unique identifier of AppConfig entity for which this customization belongs.<br />
**DisplayName**: App Config ID Unique<br />
**LogicalName**: appconfigidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_AppConfigInstanceIdUnique"></a> AppConfigInstanceIdUnique

**Description**: System-populated App Configuration Instance unique identifier.<br />
**DisplayName**: AppConfigInstanceIdUnique<br />
**LogicalName**: appconfiginstanceidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_AppConfigMasterId"></a> AppConfigMasterId

**Description**: System-calculated App Configuration Master identifier.<br />
**DisplayName**: App Config Master ID<br />
**LogicalName**: appconfigmasterid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Lookup<br />
**Targets**: appconfigmaster


### <a name="BKMK_ComponentType"></a> ComponentType

**Description**: ComponentType<br />
**DisplayName**: Enter the componenet type of the artifact (Form/View etc.) for which customization is to be created.<br />
**LogicalName**: componenttype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

**Description**: Shows the version in which the App Configuration Instance is introduced.<br />
**DisplayName**: Introduced Version<br />
**LogicalName**: introducedversion<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: VersionNumber<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ObjectId"></a> ObjectId

**Description**: ObjectId<br />
**DisplayName**: Enter the object identifier for the artifact (Form/View etc.) for which customization is to be created.<br />
**LogicalName**: objectid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_Value"></a> Value

**Description**: Enter a value for the customization property that is valid as per the validator XML specified in the app configuration master record.<br />
**DisplayName**: Value<br />
**LogicalName**: value<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AppConfigInstanceId](#BKMK_AppConfigInstanceId)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_AppConfigInstanceId"></a> AppConfigInstanceId

**Description**: System-Populated App Configuration instance identifier.<br />
**DisplayName**: AppConfig Instance ID<br />
**LogicalName**: appconfiginstanceid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ComponentState"></a> ComponentState

**Description**: System-Populated Published or UnPublished state of App Configuration Instance.<br />
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

**Description**: Shows who created the record.<br />
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


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics CRM options.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Shows who created the record on behalfÂ of another user.<br />
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
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

**Description**: For internal use only.<br />
**DisplayName**: Import Sequence Number<br />
**LogicalName**: importsequencenumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_IsManaged"></a> IsManaged

**Description**: Is Managed<br />
**DisplayName**: Shows whether the App Configuration Instance is managed or not.<br />
**LogicalName**: ismanaged<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Managed
- **FalseOption Value**: 0 **Label**: Unmanaged

**DefaultValue**: False


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Shows who last updated the record.<br />
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


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics CRM options.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Shows who last updated the record on behalf of another user.<br />
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
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: System-calculated field for Organization identifier.<br />
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


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

**Description**: Shows the date and time when the record was migrated. The date and time are displayed in the time zone selected in Microsoft Dynamics CRM options.<br />
**DisplayName**: Record Created On<br />
**LogicalName**: overriddencreatedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

**Description**: Shows the last overwrite time for the App Configuration Instance.<br />
**DisplayName**: Overwrite Time<br />
**LogicalName**: overwritetime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_SolutionId"></a> SolutionId

**Description**: Set the solution idenfitier for associated solution.<br />
**DisplayName**: SolutionId<br />
**LogicalName**: solutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

**Description**: Set the supporting solution idenfitier for associated solution.<br />
**DisplayName**: SupportingSolutionId<br />
**LogicalName**: supportingsolutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [appconfig_appconfiginstance](#BKMK_appconfig_appconfiginstance)
- [lk_appconfiginstance_modifiedby](#BKMK_lk_appconfiginstance_modifiedby)
- [lk_appconfiginstance_createdby](#BKMK_lk_appconfiginstance_createdby)
- [lk_appconfiginstance_createdonbehalfby](#BKMK_lk_appconfiginstance_createdonbehalfby)
- [lk_appconfiginstance_modifiedonbehalfby](#BKMK_lk_appconfiginstance_modifiedonbehalfby)
- [organization_appconfiginstance](#BKMK_organization_appconfiginstance)
- [appconfigmaster_appconfiginstance](#BKMK_appconfigmaster_appconfiginstance)


### <a name="BKMK_appconfig_appconfiginstance"></a> appconfig_appconfiginstance

See appconfig Entity [appconfig_appconfiginstance](appconfig.md#BKMK_appconfig_appconfiginstance) One-To-Many relationship.

### <a name="BKMK_lk_appconfiginstance_modifiedby"></a> lk_appconfiginstance_modifiedby

See systemuser Entity [lk_appconfiginstance_modifiedby](systemuser.md#BKMK_lk_appconfiginstance_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_appconfiginstance_createdby"></a> lk_appconfiginstance_createdby

See systemuser Entity [lk_appconfiginstance_createdby](systemuser.md#BKMK_lk_appconfiginstance_createdby) One-To-Many relationship.

### <a name="BKMK_lk_appconfiginstance_createdonbehalfby"></a> lk_appconfiginstance_createdonbehalfby

See systemuser Entity [lk_appconfiginstance_createdonbehalfby](systemuser.md#BKMK_lk_appconfiginstance_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_appconfiginstance_modifiedonbehalfby"></a> lk_appconfiginstance_modifiedonbehalfby

See systemuser Entity [lk_appconfiginstance_modifiedonbehalfby](systemuser.md#BKMK_lk_appconfiginstance_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_appconfiginstance"></a> organization_appconfiginstance

See organization Entity [organization_appconfiginstance](organization.md#BKMK_organization_appconfiginstance) One-To-Many relationship.

### <a name="BKMK_appconfigmaster_appconfiginstance"></a> appconfigmaster_appconfiginstance

See appconfigmaster Entity [appconfigmaster_appconfiginstance](appconfigmaster.md#BKMK_appconfigmaster_appconfiginstance) One-To-Many relationship.
appconfiginstance

