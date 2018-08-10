---
title: "NavigationSetting Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the NavigationSetting entity."

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
# NavigationSetting Entity Reference

Navigation Setting: A setting page or group of pages available for configuration within an app. A record representing a group of pages is regarded as the parent navigation setting of one or more other records. For internal use only.

## Entity Properties

**DisplayName**: Navigation Setting<br />
**DisplayCollectionName**: Navigation Settings<br />
**SchemaName**: NavigationSetting<br />
**CollectionSchemaName**: NavigationSettings<br />
**LogicalName**: navigationsetting<br />
**LogicalCollectionName**: navigationsettings<br />
**EntitySetName**: navigationsettings<br />
**PrimaryIdAttribute**: navigationsettingid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AdvancedSettingOrder](#BKMK_AdvancedSettingOrder)
- [AppConfigId](#BKMK_AppConfigId)
- [AppConfigIdUnique](#BKMK_AppConfigIdUnique)
- [Description](#BKMK_Description)
- [GroupName](#BKMK_GroupName)
- [IconResourceId](#BKMK_IconResourceId)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [Name](#BKMK_Name)
- [NavigationSettingId](#BKMK_NavigationSettingId)
- [NavigationSettingIdUnique](#BKMK_NavigationSettingIdUnique)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [PageUrl](#BKMK_PageUrl)
- [ParentNavigationSettingId](#BKMK_ParentNavigationSettingId)
- [Privileges](#BKMK_Privileges)
- [ProgressState](#BKMK_ProgressState)
- [QuickSettingOrder](#BKMK_QuickSettingOrder)
- [ResourceId](#BKMK_ResourceId)
- [SettingType](#BKMK_SettingType)


### <a name="BKMK_AdvancedSettingOrder"></a> AdvancedSettingOrder

**Description**: Enter the position of this NavigationSetting as it should appear within its group in the Advanced Setup menu.<br />
**DisplayName**: AdvancedOrder<br />
**LogicalName**: advancedsettingorder<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_AppConfigId"></a> AppConfigId

**Description**: Enter the App Config record that this Navigation Setting is associated with.<br />
**DisplayName**: AppConfigId<br />
**LogicalName**: appconfigid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Lookup<br />
**Targets**: appmodule


### <a name="BKMK_AppConfigIdUnique"></a> AppConfigIdUnique

**Description**: For system use only.<br />
**DisplayName**: AppConfigIdUnique<br />
**LogicalName**: appconfigidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_Description"></a> Description

**Description**: Type a description that describes that Navigation Setting in detail.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: True<br />
**MaxLength**: 2000


### <a name="BKMK_GroupName"></a> GroupName

**Description**: Type the name of the group represented by this Navigation Setting record.<br />
**DisplayName**: Group Name<br />
**LogicalName**: groupname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: True<br />
**MaxLength**: 400


### <a name="BKMK_IconResourceId"></a> IconResourceId

**Description**: The web resource identifier of the icon to be used for a navigation setting area or sub area.<br />
**DisplayName**: IconResourceId<br />
**LogicalName**: iconresourceid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

**Description**: Version in which the similarity rule is introduced.<br />
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


### <a name="BKMK_Name"></a> Name

**Description**: Type a title or name that describes the Navigation Setting so it can be identified in Dynamics CRM views.<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: True<br />
**MaxLength**: 100


### <a name="BKMK_NavigationSettingId"></a> NavigationSettingId

**Description**: Identifies a single setting page or group of pages configured for use in a single app.<br />
**DisplayName**: NavigationSettingId<br />
**LogicalName**: navigationsettingid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_NavigationSettingIdUnique"></a> NavigationSettingIdUnique

**Description**: For system use only.<br />
**DisplayName**: NavigationSettingIdUnique<br />
**LogicalName**: navigationsettingidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

**Description**: Enter the Object Type Code of the entity associated whose page this Navigation Setting record represents.<br />
**DisplayName**: EntityObjectTypeCode<br />
**LogicalName**: objecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_PageUrl"></a> PageUrl

**Description**: Type the URL which locates the page associated with this Navigation Setting record.<br />
**DisplayName**: Page Url<br />
**LogicalName**: pageurl<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 400


### <a name="BKMK_ParentNavigationSettingId"></a> ParentNavigationSettingId

**Description**: The Navigation Setting record that represents the group that this record belongs to.<br />
**DisplayName**: Parent Navigation Setting Id<br />
**LogicalName**: parentnavigationsettingid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_Privileges"></a> Privileges

**Description**: Enter the Privilege Mask for the entity associated with this navigation setting page that will be the minimum requirement for the page to be made available to a user.<br />
**DisplayName**: Privileges<br />
**LogicalName**: privileges<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_ProgressState"></a> ProgressState

**Description**: Select the setup completion level for this Navigation Setting page.<br />
**DisplayName**: Progress State<br />
**LogicalName**: progressstate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Visited
- **FalseOption Value**: 0 **Label**: Not Visited

**DefaultValue**: False


### <a name="BKMK_QuickSettingOrder"></a> QuickSettingOrder

**Description**: Enter the position of this NavigationSetting as it should appear in the Quick Setup menu.<br />
**DisplayName**: QuickOrder<br />
**LogicalName**: quicksettingorder<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_ResourceId"></a> ResourceId

**Description**: The Web Resource that will be associated with this Navigation Setting record.<br />
**DisplayName**: Resource Id<br />
**LogicalName**: resourceid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SettingType"></a> SettingType

**Description**: Select the type of group this Navigation Setting record represents. This determines which of the three in-app customization menus will contain this group.<br />
**DisplayName**: Group Type<br />
**LogicalName**: settingtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Advanced Setup
- **Value**: 1 **Label**: Basic Setup
- **Value**: 2 **Label**: Advanced Setup Summary
- **Value**: 3 **Label**: Basic Setup Summary


<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

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

**Description**: Shows who created the record on behalf of another user.<br />
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

**Description**: Unique identifier of the data import or data migration that created this record.<br />
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

**Description**: For internal use only.<br />
**DisplayName**: Is Managed<br />
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

**Description**: System-populated field that identifies the organization that owns this Navigation Setting record.<br />
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

**Description**: Date and time that the record was migrated.<br />
**DisplayName**: Record Created On<br />
**LogicalName**: overriddencreatedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [lk_navigationsetting_modifiedonbehalfby](#BKMK_lk_navigationsetting_modifiedonbehalfby)
- [navigationsetting_appconfig](#BKMK_navigationsetting_appconfig)
- [lk_navigationsetting_createdonbehalfby](#BKMK_lk_navigationsetting_createdonbehalfby)
- [lk_navigationsetting_createdby](#BKMK_lk_navigationsetting_createdby)
- [lk_navigationsetting_modifiedby](#BKMK_lk_navigationsetting_modifiedby)
- [organization_navigationsetting](#BKMK_organization_navigationsetting)


### <a name="BKMK_lk_navigationsetting_modifiedonbehalfby"></a> lk_navigationsetting_modifiedonbehalfby

See systemuser Entity [lk_navigationsetting_modifiedonbehalfby](systemuser.md#BKMK_lk_navigationsetting_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_navigationsetting_appconfig"></a> navigationsetting_appconfig

See appconfig Entity [navigationsetting_appconfig](appconfig.md#BKMK_navigationsetting_appconfig) One-To-Many relationship.

### <a name="BKMK_lk_navigationsetting_createdonbehalfby"></a> lk_navigationsetting_createdonbehalfby

See systemuser Entity [lk_navigationsetting_createdonbehalfby](systemuser.md#BKMK_lk_navigationsetting_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_navigationsetting_createdby"></a> lk_navigationsetting_createdby

See systemuser Entity [lk_navigationsetting_createdby](systemuser.md#BKMK_lk_navigationsetting_createdby) One-To-Many relationship.

### <a name="BKMK_lk_navigationsetting_modifiedby"></a> lk_navigationsetting_modifiedby

See systemuser Entity [lk_navigationsetting_modifiedby](systemuser.md#BKMK_lk_navigationsetting_modifiedby) One-To-Many relationship.

### <a name="BKMK_organization_navigationsetting"></a> organization_navigationsetting

See organization Entity [organization_navigationsetting](organization.md#BKMK_organization_navigationsetting) One-To-Many relationship.
navigationsetting

