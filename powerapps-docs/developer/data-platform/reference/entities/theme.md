---
title: "Theme table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Theme table/entity."
ms.date: 05/20/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Theme table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Information that's used to set custom visual theme options for client applications.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/themes<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/themes(*themeid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PublishTheme|<xref href="Microsoft.Dynamics.CRM.PublishTheme?text=PublishTheme Action" />|<xref:Microsoft.Crm.Sdk.Messages.PublishThemeRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/themes(*themeid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/themes<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/themes(*themeid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|Themes|
|DisplayCollectionName|Themes|
|DisplayName|Theme|
|EntitySetName|themes|
|IsBPFEntity|False|
|LogicalCollectionName|themes|
|LogicalName|theme|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|themeid|
|PrimaryNameAttribute|name|
|SchemaName|Theme|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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

|Property|Value|
|--------|-----|
|Description|Choose the Unified Interface secondary theme color to be used on the process control|
|DisplayName|Accent Color|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|accentcolor|
|MaxLength|7|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_BackgroundColor"></a> BackgroundColor

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Background Color|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|backgroundcolor|
|MaxLength|7|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ControlBorder"></a> ControlBorder

|Property|Value|
|--------|-----|
|Description|Choose the color that controls will use for borders|
|DisplayName|Control Hover Border Color|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|controlborder|
|MaxLength|7|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ControlShade"></a> ControlShade

|Property|Value|
|--------|-----|
|Description|Choose the background color for controls to use to indicate when you hover over items|
|DisplayName|Control Hover Fill Color|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|controlshade|
|MaxLength|7|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_DefaultCustomEntityColor"></a> DefaultCustomEntityColor

|Property|Value|
|--------|-----|
|Description|Choose the default custom entity color if no color is assigned|
|DisplayName|Default Custom Entity Color|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|defaultcustomentitycolor|
|MaxLength|7|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_DefaultEntityColor"></a> DefaultEntityColor

|Property|Value|
|--------|-----|
|Description|Choose the default color for system entities if no color is assigned|
|DisplayName|Default Entity Color|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|defaultentitycolor|
|MaxLength|7|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_GlobalLinkColor"></a> GlobalLinkColor

|Property|Value|
|--------|-----|
|Description|Choose the color for all links, such as e-mail address and lookup links, and for all buttons that are in focus|
|DisplayName|Link and Button Text Color|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|globallinkcolor|
|MaxLength|7|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_HeaderColor"></a> HeaderColor

|Property|Value|
|--------|-----|
|Description|Choose the color for title text, such as form tab labels|
|DisplayName|Title Text Color|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|headercolor|
|MaxLength|7|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_HoverLinkEffect"></a> HoverLinkEffect

|Property|Value|
|--------|-----|
|Description|Choose the color that commands or lists will use to indicate hovered over items|
|DisplayName|Hover Link Color|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|hoverlinkeffect|
|MaxLength|7|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|Sequence number of the import that created this record.|
|DisplayName|Import Sequence Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|importsequencenumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_IsDefaultTheme"></a> IsDefaultTheme

|Property|Value|
|--------|-----|
|Description|Default status of theme.|
|DisplayName|Default Theme|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isdefaulttheme|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsDefaultTheme Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_LogoId"></a> LogoId

|Property|Value|
|--------|-----|
|Description|Upload a web resource to use as a logo. Recommended dimensions are a height of 50 pixels and a maximum width of 400 pixels.|
|DisplayName|Logo|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|logoid|
|RequiredLevel|None|
|Targets|webresource|
|Type|Lookup|


### <a name="BKMK_LogoToolTip"></a> LogoToolTip

|Property|Value|
|--------|-----|
|Description|Enter text that will be used as the tooltip and alt text for the logo.|
|DisplayName|Logo Tooltip|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|logotooltip|
|MaxLength|80|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_MainColor"></a> MainColor

|Property|Value|
|--------|-----|
|Description|Choose the Unified Interface primary theme color to be used on main command bar, buttons and tabs|
|DisplayName|Main Color|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|maincolor|
|MaxLength|7|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|The name of the Theme Entity.|
|DisplayName|Theme Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_NavBarBackgroundColor"></a> NavBarBackgroundColor

|Property|Value|
|--------|-----|
|Description|Choose the primary Navigation Bar background color|
|DisplayName|Navigation Bar Fill Color|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|navbarbackgroundcolor|
|MaxLength|7|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_NavBarShelfColor"></a> NavBarShelfColor

|Property|Value|
|--------|-----|
|Description|Choose the secondary Navigation Bar background color|
|DisplayName|Navigation Bar Shelf Fill Color|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|navbarshelfcolor|
|MaxLength|7|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time that the record was migrated.|
|DisplayName|Record Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_PageHeaderBackgroundColor"></a> PageHeaderBackgroundColor

|Property|Value|
|--------|-----|
|Description|Choose the page header background color|
|DisplayName|Page Header Fill Color|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|pageheaderbackgroundcolor|
|MaxLength|7|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PanelHeaderBackgroundColor"></a> PanelHeaderBackgroundColor

|Property|Value|
|--------|-----|
|Description|Choose the panel header background color|
|DisplayName|Panel Header Fill Color|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|panelheaderbackgroundcolor|
|MaxLength|7|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ProcessControlColor"></a> ProcessControlColor

|Property|Value|
|--------|-----|
|Description|Choose the primary background color for process controls|
|DisplayName|Legacy Accent Color|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|processcontrolcolor|
|MaxLength|7|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SelectedLinkEffect"></a> SelectedLinkEffect

|Property|Value|
|--------|-----|
|Description|Choose the color that commands or lists will use to indicate selected items|
|DisplayName|Selected Link Color|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|selectedlinkeffect|
|MaxLength|7|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the Theme|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### statuscode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Custom|0|
|2|System|1|



### <a name="BKMK_ThemeId"></a> ThemeId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Theme|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|themeid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Time Zone Rule Version Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezoneruleversionnumber|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|--------|-----|
|Description|Exchange rate for the currency associated with the Theme with respect to the base currency.|
|DisplayName|Currency|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|transactioncurrencyid|
|RequiredLevel|None|
|Targets|transactioncurrency|
|Type|Lookup|


### <a name="BKMK_Type"></a> Type

|Property|Value|
|--------|-----|
|Description|Define type of theme.|
|DisplayName|Type|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|type|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### Type Choices/Options

|Value|Label|
|-----|-----|
|1|Custom|
|0|System|

**DefaultValue**: True



### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|--------|-----|
|Description|Time zone code that was in use when the record was created.|
|DisplayName|UTC Conversion Time Zone Code|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|utcconversiontimezonecode|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

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

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the record.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the record.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|--------|-----|
|Description|Exchange rate for the currency associated with the Theme with respect to the base currency.|
|DisplayName|ExchangeRate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.0000000001|
|Precision|10|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_LogoIdName"></a> LogoIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|logoidname|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who modified the record.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the record.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier for the organization|
|DisplayName|Organization Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|None|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Theme|
|DisplayName|Status|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### statecode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Custom|1|Active|
|1|System|2|Inactive|



### <a name="BKMK_TransactionCurrencyIdName"></a> TransactionCurrencyIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|transactioncurrencyidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [theme_AsyncOperations](#BKMK_theme_AsyncOperations)
- [theme_ProcessSession](#BKMK_theme_ProcessSession)
- [theme_BulkDeleteFailures](#BKMK_theme_BulkDeleteFailures)


### <a name="BKMK_theme_AsyncOperations"></a> theme_AsyncOperations

Same as asyncoperation table [theme_AsyncOperations](asyncoperation.md#BKMK_theme_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|theme_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_theme_ProcessSession"></a> theme_ProcessSession

Same as processsession table [theme_ProcessSession](processsession.md#BKMK_theme_ProcessSession) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|theme_ProcessSession|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_theme_BulkDeleteFailures"></a> theme_BulkDeleteFailures

Same as bulkdeletefailure table [theme_BulkDeleteFailures](bulkdeletefailure.md#BKMK_theme_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|theme_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_theme_createdby](#BKMK_lk_theme_createdby)
- [lk_theme_createdonbehalfby](#BKMK_lk_theme_createdonbehalfby)
- [lk_theme_modifiedby](#BKMK_lk_theme_modifiedby)
- [lk_theme_modifiedonbehalfby](#BKMK_lk_theme_modifiedonbehalfby)
- [organization_theme](#BKMK_organization_theme)
- [TransactionCurrency_Theme](#BKMK_TransactionCurrency_Theme)
- [lk_theme_logoid](#BKMK_lk_theme_logoid)


### <a name="BKMK_lk_theme_createdby"></a> lk_theme_createdby

See systemuser Table [lk_theme_createdby](systemuser.md#BKMK_lk_theme_createdby) One-To-Many relationship.

### <a name="BKMK_lk_theme_createdonbehalfby"></a> lk_theme_createdonbehalfby

See systemuser Table [lk_theme_createdonbehalfby](systemuser.md#BKMK_lk_theme_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_theme_modifiedby"></a> lk_theme_modifiedby

See systemuser Table [lk_theme_modifiedby](systemuser.md#BKMK_lk_theme_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_theme_modifiedonbehalfby"></a> lk_theme_modifiedonbehalfby

See systemuser Table [lk_theme_modifiedonbehalfby](systemuser.md#BKMK_lk_theme_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_theme"></a> organization_theme

See organization Table [organization_theme](organization.md#BKMK_organization_theme) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_Theme"></a> TransactionCurrency_Theme

See transactioncurrency Table [TransactionCurrency_Theme](transactioncurrency.md#BKMK_TransactionCurrency_Theme) One-To-Many relationship.

### <a name="BKMK_lk_theme_logoid"></a> lk_theme_logoid

See webresource Table [lk_theme_logoid](webresource.md#BKMK_lk_theme_logoid) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.theme?text=theme EntityType" />