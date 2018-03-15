---
title: "AppModuleComponent Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the AppModuleComponent entity."

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
# AppModuleComponent Entity Reference

A component available in a business app such as entity, dashboard, form, view, chart, and business process.

## Entity Properties

**DisplayName**: App Module Component<br />
**DisplayCollectionName**: App Module Components<br />
**SchemaName**: AppModuleComponent<br />
**CollectionSchemaName**: App Module Components<br />
**LogicalName**: appmodulecomponent<br />
**LogicalCollectionName**: appmodulecomponents<br />
**EntitySetName**: appmodulecomponents<br />
**PrimaryIdAttribute**: appmodulecomponentid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AppModuleComponentId](#BKMK_AppModuleComponentId)
- [AppModuleComponentIdUnique](#BKMK_AppModuleComponentIdUnique)
- [AppModuleIdUnique](#BKMK_AppModuleIdUnique)
- [ComponentType](#BKMK_ComponentType)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsDefault](#BKMK_IsDefault)
- [IsMetadata](#BKMK_IsMetadata)
- [ObjectId](#BKMK_ObjectId)
- [RootAppModuleComponentId](#BKMK_RootAppModuleComponentId)
- [RootComponentBehavior](#BKMK_RootComponentBehavior)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_AppModuleComponentId"></a> AppModuleComponentId

**Description**: Unique identifier for entity instances<br />
**DisplayName**: App Module Component<br />
**LogicalName**: appmodulecomponentid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_AppModuleComponentIdUnique"></a> AppModuleComponentIdUnique

**Description**: Unique identifier of the Application Component used when synchronizing customizations for the Microsoft Dynamics 365 client for Outlook<br />
**DisplayName**: Application Component Unique Id<br />
**LogicalName**: appmodulecomponentidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_AppModuleIdUnique"></a> AppModuleIdUnique

**Description**: The App Module Id Unique<br />
**DisplayName**: AppModule<br />
**LogicalName**: appmoduleidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Lookup<br />
**Targets**: appmodule


### <a name="BKMK_ComponentType"></a> ComponentType

**Description**: The object type code of the component.<br />
**DisplayName**: Object Type Code<br />
**LogicalName**: componenttype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Entities
- **Value**: 26 **Label**: Views
- **Value**: 29 **Label**: Business Process Flows
- **Value**: 48 **Label**: Command (Ribbon) for Forms, Grids, sub grids
- **Value**: 59 **Label**: Charts
- **Value**: 60 **Label**: Forms
- **Value**: 62 **Label**: Sitemap



### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

**Description**: Version in which the application component record is introduced.<br />
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


### <a name="BKMK_IsDefault"></a> IsDefault

**Description**: Is Default<br />
**DisplayName**: Is Default<br />
**LogicalName**: isdefault<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsMetadata"></a> IsMetadata

**Description**: Is Metadata<br />
**DisplayName**: Is Metadata<br />
**LogicalName**: ismetadata<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Metadata
- **FalseOption Value**: 0 **Label**: Data

**DefaultValue**: False


### <a name="BKMK_ObjectId"></a> ObjectId

**Description**: Object Id<br />
**DisplayName**: Object<br />
**LogicalName**: objectid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_RootAppModuleComponentId"></a> RootAppModuleComponentId

**Description**: The parent ID of the subcomponent, which will be a root<br />
**DisplayName**: Root App Module Component<br />
**LogicalName**: rootappmodulecomponentid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_RootComponentBehavior"></a> RootComponentBehavior

**Description**: Indicates the include behavior of the root component.<br />
**DisplayName**: Root Component Behavior<br />
**LogicalName**: rootcomponentbehavior<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Include Subcomponents
- **Value**: 1 **Label**: Do not include subcomponents
- **Value**: 2 **Label**: Include As Shell Only



### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

**Description**: For internal use only.<br />
**DisplayName**: Time Zone Rule Version Number<br />
**LogicalName**: timezoneruleversionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

**Description**: Time zone code that was in use when the record was created.<br />
**DisplayName**: UTC Conversion Time Zone Code<br />
**LogicalName**: utcconversiontimezonecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AppModuleIdName](#BKMK_AppModuleIdName)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ExchangeRate](#BKMK_ExchangeRate)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_AppModuleIdName"></a> AppModuleIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: appmoduleidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


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
**RequiredLevel**: ApplicationRequired<br />
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
**RequiredLevel**: SystemRequired<br />
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
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

**Description**: Exchange rate for the currency associated with the Application Component with respect to the base currency.<br />
**DisplayName**: ExchangeRate<br />
**LogicalName**: exchangerate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0.0000000001<br />
**Precision**: 10


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
**RequiredLevel**: SystemRequired<br />
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
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

**Description**: Date and time when the record was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: overwritetime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


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

- [appmodule_appmodulecomponent](#BKMK_appmodule_appmodulecomponent)
- [lk_appmodulecomponent_createdonbehalfby](#BKMK_lk_appmodulecomponent_createdonbehalfby)
- [lk_appmodulecomponent_modifiedonbehalfby](#BKMK_lk_appmodulecomponent_modifiedonbehalfby)
- [lk_appmodulecomponent_createdby](#BKMK_lk_appmodulecomponent_createdby)
- [lk_appmodulecomponent_modifiedby](#BKMK_lk_appmodulecomponent_modifiedby)


### <a name="BKMK_appmodule_appmodulecomponent"></a> appmodule_appmodulecomponent

See appmodule Entity [appmodule_appmodulecomponent](appmodule.md#BKMK_appmodule_appmodulecomponent) One-To-Many relationship.

### <a name="BKMK_lk_appmodulecomponent_createdonbehalfby"></a> lk_appmodulecomponent_createdonbehalfby

See systemuser Entity [lk_appmodulecomponent_createdonbehalfby](systemuser.md#BKMK_lk_appmodulecomponent_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_appmodulecomponent_modifiedonbehalfby"></a> lk_appmodulecomponent_modifiedonbehalfby

See systemuser Entity [lk_appmodulecomponent_modifiedonbehalfby](systemuser.md#BKMK_lk_appmodulecomponent_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_appmodulecomponent_createdby"></a> lk_appmodulecomponent_createdby

See systemuser Entity [lk_appmodulecomponent_createdby](systemuser.md#BKMK_lk_appmodulecomponent_createdby) One-To-Many relationship.

### <a name="BKMK_lk_appmodulecomponent_modifiedby"></a> lk_appmodulecomponent_modifiedby

See systemuser Entity [lk_appmodulecomponent_modifiedby](systemuser.md#BKMK_lk_appmodulecomponent_modifiedby) One-To-Many relationship.
appmodulecomponent

