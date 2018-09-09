---
title: "Theme Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the Theme entity."
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
# Theme Entity Reference

Information that's used to set custom visual theme options for client applications.

## Entity Properties

**DisplayName**: Theme<br />
**DisplayCollectionName**: Themes<br />
**SchemaName**: Theme<br />
**CollectionSchemaName**: Themes<br />
**LogicalName**: theme<br />
**LogicalCollectionName**: themes<br />
**EntitySetName**: themes<br />
**PrimaryIdAttribute**: themeid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AccentColor](#BKMK_AccentColor)
- [BackgroundColor](#BKMK_BackgroundColor)
- [ControlBorder](#BKMK_ControlBorder)
- [ControlShade](#BKMK_ControlShade)
- [DefaultCustomEntityColor](#BKMK_DefaultCustomEntityColor)
- [DefaultEntityColor](#BKMK_DefaultEntityColor)
- [GlobalLinkColor](#BKMK_GlobalLinkColor)
- [HeaderColor](#BKMK_HeaderColor)
- [HoverLinkEffect](#BKMK_HoverLinkEffect)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsDefaultTheme](#BKMK_IsDefaultTheme)
- [LogoId](#BKMK_LogoId)
- [LogoToolTip](#BKMK_LogoToolTip)
- [MainColor](#BKMK_MainColor)
- [Name](#BKMK_Name)
- [NavBarBackgroundColor](#BKMK_NavBarBackgroundColor)
- [NavBarShelfColor](#BKMK_NavBarShelfColor)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PageHeaderBackgroundColor](#BKMK_PageHeaderBackgroundColor)
- [PanelHeaderBackgroundColor](#BKMK_PanelHeaderBackgroundColor)
- [ProcessControlColor](#BKMK_ProcessControlColor)
- [SelectedLinkEffect](#BKMK_SelectedLinkEffect)
- [statuscode](#BKMK_statuscode)
- [ThemeId](#BKMK_ThemeId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [Type](#BKMK_Type)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_AccentColor"></a> AccentColor

**Description**: Choose the Unified Interface secondary theme color to be used on the process control<br />
**DisplayName**: Accent Color<br />
**LogicalName**: accentcolor<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 7


### <a name="BKMK_BackgroundColor"></a> BackgroundColor

**Description**: For internal use only.<br />
**DisplayName**: Background Color<br />
**LogicalName**: backgroundcolor<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 7


### <a name="BKMK_ControlBorder"></a> ControlBorder

**Description**: Choose the color that controls will use for borders<br />
**DisplayName**: Control Hover Border Color<br />
**LogicalName**: controlborder<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 7


### <a name="BKMK_ControlShade"></a> ControlShade

**Description**: Choose the background color for controls to use to indicate when you hover over items<br />
**DisplayName**: Control Hover Fill Color<br />
**LogicalName**: controlshade<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 7


### <a name="BKMK_DefaultCustomEntityColor"></a> DefaultCustomEntityColor

**Description**: Choose the default custom entity color if no color is assigned<br />
**DisplayName**: Default Custom Entity Color<br />
**LogicalName**: defaultcustomentitycolor<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 7


### <a name="BKMK_DefaultEntityColor"></a> DefaultEntityColor

**Description**: Choose the default color for system entities if no color is assigned<br />
**DisplayName**: Default Entity Color<br />
**LogicalName**: defaultentitycolor<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 7


### <a name="BKMK_GlobalLinkColor"></a> GlobalLinkColor

**Description**: Choose the color for all links, such as e-mail address and lookup links, and for all buttons that are in focus<br />
**DisplayName**: Link and Button Text Color<br />
**LogicalName**: globallinkcolor<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 7


### <a name="BKMK_HeaderColor"></a> HeaderColor

**Description**: Choose the color for title text, such as form tab labels<br />
**DisplayName**: Title Text Color<br />
**LogicalName**: headercolor<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 7


### <a name="BKMK_HoverLinkEffect"></a> HoverLinkEffect

**Description**: Choose the color that commands or lists will use to indicate hovered over items<br />
**DisplayName**: Hover Link Color<br />
**LogicalName**: hoverlinkeffect<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 7


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

**Description**: Sequence number of the import that created this record.<br />
**DisplayName**: Import Sequence Number<br />
**LogicalName**: importsequencenumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_IsDefaultTheme"></a> IsDefaultTheme

**Description**: Default status of theme.<br />
**DisplayName**: Default Theme<br />
**LogicalName**: isdefaulttheme<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_LogoId"></a> LogoId

**Description**: Upload a web resource to use as a logo. Recommended dimensions are a height of 50 pixels and a maximum width of 400 pixels.<br />
**DisplayName**: Logo<br />
**LogicalName**: logoid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: webresource


### <a name="BKMK_LogoToolTip"></a> LogoToolTip

**Description**: Enter text that will be used as the tooltip and alt text for the logo.<br />
**DisplayName**: Logo Tooltip<br />
**LogicalName**: logotooltip<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 80


### <a name="BKMK_MainColor"></a> MainColor

**Description**: Choose the Unified Interface primary theme color to be used on main command bar, buttons and tabs<br />
**DisplayName**: Main Color<br />
**LogicalName**: maincolor<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 7


### <a name="BKMK_Name"></a> Name

**Description**: The name of the Theme Entity.<br />
**DisplayName**: Theme Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_NavBarBackgroundColor"></a> NavBarBackgroundColor

**Description**: Choose the primary Navigation Bar background color<br />
**DisplayName**: Navigation Bar Fill Color<br />
**LogicalName**: navbarbackgroundcolor<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 7


### <a name="BKMK_NavBarShelfColor"></a> NavBarShelfColor

**Description**: Choose the secondary Navigation Bar background color<br />
**DisplayName**: Navigation Bar Shelf Fill Color<br />
**LogicalName**: navbarshelfcolor<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 7


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

**Description**: Date and time that the record was migrated.<br />
**DisplayName**: Record Created On<br />
**LogicalName**: overriddencreatedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_PageHeaderBackgroundColor"></a> PageHeaderBackgroundColor

**Description**: Choose the page header background color<br />
**DisplayName**: Page Header Fill Color<br />
**LogicalName**: pageheaderbackgroundcolor<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 7


### <a name="BKMK_PanelHeaderBackgroundColor"></a> PanelHeaderBackgroundColor

**Description**: Choose the panel header background color<br />
**DisplayName**: Panel Header Fill Color<br />
**LogicalName**: panelheaderbackgroundcolor<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 7


### <a name="BKMK_ProcessControlColor"></a> ProcessControlColor

**Description**: Choose the primary background color for process controls<br />
**DisplayName**: Legacy Accent Color<br />
**LogicalName**: processcontrolcolor<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 7


### <a name="BKMK_SelectedLinkEffect"></a> SelectedLinkEffect

**Description**: Choose the color that commands or lists will use to indicate selected items<br />
**DisplayName**: Selected Link Color<br />
**LogicalName**: selectedlinkeffect<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 7


### <a name="BKMK_statuscode"></a> statuscode

**Description**: Reason for the status of the Theme<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Status<br />
**Options**:

- **Value**: 1 **Label**: Custom **State**: 0
- **Value**: 2 **Label**: System **State**: 1



### <a name="BKMK_ThemeId"></a> ThemeId

**Description**: Unique identifier for entity instances<br />
**DisplayName**: Theme<br />
**LogicalName**: themeid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


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


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

**Description**: Exchange rate for the currency associated with the Theme with respect to the base currency.<br />
**DisplayName**: Currency<br />
**LogicalName**: transactioncurrencyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: transactioncurrency


### <a name="BKMK_Type"></a> Type

**Description**: Define type of theme.<br />
**DisplayName**: Type<br />
**LogicalName**: type<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Custom
- **FalseOption Value**: 0 **Label**: System

**DefaultValue**: True


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

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ExchangeRate](#BKMK_ExchangeRate)
- [LogoIdName](#BKMK_LogoIdName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [statecode](#BKMK_statecode)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the record.<br />
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
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the record.<br />
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
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

**Description**: Exchange rate for the currency associated with the Theme with respect to the base currency.<br />
**DisplayName**: ExchangeRate<br />
**LogicalName**: exchangerate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0.0000000001<br />
**Precision**: 10


### <a name="BKMK_LogoIdName"></a> LogoIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: logoidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 400


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who modified the record.<br />
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
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who modified the record.<br />
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
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier for the organization<br />
**DisplayName**: Organization Id<br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
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


### <a name="BKMK_statecode"></a> statecode

**Description**: Status of the Theme<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Custom **DefaultStatus**: 1 **InvariantName**: Active
- **Value**: 1 **Label**: System **DefaultStatus**: 2 **InvariantName**: Inactive



### <a name="BKMK_TransactionCurrencyIdName"></a> TransactionCurrencyIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: transactioncurrencyidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


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

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [theme_AsyncOperations](#BKMK_theme_AsyncOperations)
- [theme_UserEntityInstanceDatas](#BKMK_theme_UserEntityInstanceDatas)
- [theme_ProcessSession](#BKMK_theme_ProcessSession)
- [theme_BulkDeleteFailures](#BKMK_theme_BulkDeleteFailures)


### <a name="BKMK_theme_AsyncOperations"></a> theme_AsyncOperations

Same as asyncoperation entity [theme_AsyncOperations](asyncoperation.md#BKMK_theme_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: theme_AsyncOperations<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_theme_UserEntityInstanceDatas"></a> theme_UserEntityInstanceDatas

Same as userentityinstancedata entity [theme_UserEntityInstanceDatas](userentityinstancedata.md#BKMK_theme_UserEntityInstanceDatas) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: theme_UserEntityInstanceDatas<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_theme_ProcessSession"></a> theme_ProcessSession

Same as processsession entity [theme_ProcessSession](processsession.md#BKMK_theme_ProcessSession) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: theme_ProcessSession<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_theme_BulkDeleteFailures"></a> theme_BulkDeleteFailures

Same as bulkdeletefailure entity [theme_BulkDeleteFailures](bulkdeletefailure.md#BKMK_theme_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: theme_BulkDeleteFailures<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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

- [lk_theme_createdby](#BKMK_lk_theme_createdby)
- [lk_theme_createdonbehalfby](#BKMK_lk_theme_createdonbehalfby)
- [lk_theme_modifiedby](#BKMK_lk_theme_modifiedby)
- [lk_theme_modifiedonbehalfby](#BKMK_lk_theme_modifiedonbehalfby)
- [organization_theme](#BKMK_organization_theme)
- [TransactionCurrency_Theme](#BKMK_TransactionCurrency_Theme)
- [lk_theme_logoid](#BKMK_lk_theme_logoid)


### <a name="BKMK_lk_theme_createdby"></a> lk_theme_createdby

See systemuser Entity [lk_theme_createdby](systemuser.md#BKMK_lk_theme_createdby) One-To-Many relationship.

### <a name="BKMK_lk_theme_createdonbehalfby"></a> lk_theme_createdonbehalfby

See systemuser Entity [lk_theme_createdonbehalfby](systemuser.md#BKMK_lk_theme_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_theme_modifiedby"></a> lk_theme_modifiedby

See systemuser Entity [lk_theme_modifiedby](systemuser.md#BKMK_lk_theme_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_theme_modifiedonbehalfby"></a> lk_theme_modifiedonbehalfby

See systemuser Entity [lk_theme_modifiedonbehalfby](systemuser.md#BKMK_lk_theme_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_theme"></a> organization_theme

See organization Entity [organization_theme](organization.md#BKMK_organization_theme) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_Theme"></a> TransactionCurrency_Theme

See transactioncurrency Entity [TransactionCurrency_Theme](transactioncurrency.md#BKMK_TransactionCurrency_Theme) One-To-Many relationship.

### <a name="BKMK_lk_theme_logoid"></a> lk_theme_logoid

See webresource Entity [lk_theme_logoid](webresource.md#BKMK_lk_theme_logoid) One-To-Many relationship.
theme

