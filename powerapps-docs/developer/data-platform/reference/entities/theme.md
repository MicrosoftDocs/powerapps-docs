---
title: "Theme table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Theme table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Theme table/entity reference (Microsoft Dataverse)

Information that's used to set custom visual theme options for client applications.

## Messages

The following table lists the messages for the Theme table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /themes<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /themes(*themeid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `PublishTheme`<br />Event: True |<xref:Microsoft.Dynamics.CRM.PublishTheme?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.PublishThemeRequest>|
| `Retrieve`<br />Event: True |`GET` /themes(*themeid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /themes<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /themes(*themeid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /themes(*themeid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Theme table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Theme** |
| **DisplayCollectionName** | **Themes** |
| **SchemaName** | `Theme` |
| **CollectionSchemaName** | `Themes` |
| **EntitySetName** | `themes`|
| **LogicalName** | `theme` |
| **LogicalCollectionName** | `themes` |
| **PrimaryIdAttribute** | `themeid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

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
|---|---|
|Description|**Choose the Unified Interface secondary theme color to be used on the process control**|
|DisplayName|**Accent Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`accentcolor`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|7|

### <a name="BKMK_BackgroundColor"></a> BackgroundColor

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Background Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`backgroundcolor`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|7|

### <a name="BKMK_ControlBorder"></a> ControlBorder

|Property|Value|
|---|---|
|Description|**Choose the color that controls will use for borders**|
|DisplayName|**Control Hover Border Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`controlborder`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|7|

### <a name="BKMK_ControlShade"></a> ControlShade

|Property|Value|
|---|---|
|Description|**Choose the background color for controls to use to indicate when you hover over items**|
|DisplayName|**Control Hover Fill Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`controlshade`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|7|

### <a name="BKMK_DefaultCustomEntityColor"></a> DefaultCustomEntityColor

|Property|Value|
|---|---|
|Description|**Choose the default custom entity color if no color is assigned**|
|DisplayName|**Default Custom Entity Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`defaultcustomentitycolor`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|7|

### <a name="BKMK_DefaultEntityColor"></a> DefaultEntityColor

|Property|Value|
|---|---|
|Description|**Choose the default color for system entities if no color is assigned**|
|DisplayName|**Default Entity Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`defaultentitycolor`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|7|

### <a name="BKMK_GlobalLinkColor"></a> GlobalLinkColor

|Property|Value|
|---|---|
|Description|**Choose the color for all links, such as e-mail address and lookup links, and for all buttons that are in focus**|
|DisplayName|**Link and Button Text Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`globallinkcolor`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|7|

### <a name="BKMK_HeaderColor"></a> HeaderColor

|Property|Value|
|---|---|
|Description|**Choose the color for title text, such as form tab labels**|
|DisplayName|**Title Text Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`headercolor`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|7|

### <a name="BKMK_HoverLinkEffect"></a> HoverLinkEffect

|Property|Value|
|---|---|
|Description|**Choose the color that commands or lists will use to indicate hovered over items**|
|DisplayName|**Hover Link Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`hoverlinkeffect`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|7|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Sequence number of the import that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_IsDefaultTheme"></a> IsDefaultTheme

|Property|Value|
|---|---|
|Description|**Default status of theme.**|
|DisplayName|**Default Theme**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isdefaulttheme`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`theme_defaultstatus`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_LogoId"></a> LogoId

|Property|Value|
|---|---|
|Description|**Upload a web resource to use as a logo. Recommended dimensions are a height of 50 pixels and a maximum width of 400 pixels.**|
|DisplayName|**Logo**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`logoid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|webresource|

### <a name="BKMK_LogoToolTip"></a> LogoToolTip

|Property|Value|
|---|---|
|Description|**Enter text that will be used as the tooltip and alt text for the logo.**|
|DisplayName|**Logo Tooltip**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`logotooltip`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|80|

### <a name="BKMK_MainColor"></a> MainColor

|Property|Value|
|---|---|
|Description|**Choose the Unified Interface primary theme color to be used on main command bar, buttons and tabs**|
|DisplayName|**Main Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`maincolor`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|7|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**The name of the Theme Entity.**|
|DisplayName|**Theme Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_NavBarBackgroundColor"></a> NavBarBackgroundColor

|Property|Value|
|---|---|
|Description|**Choose the primary Navigation Bar background color**|
|DisplayName|**Navigation Bar Fill Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`navbarbackgroundcolor`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|7|

### <a name="BKMK_NavBarShelfColor"></a> NavBarShelfColor

|Property|Value|
|---|---|
|Description|**Choose the secondary Navigation Bar background color**|
|DisplayName|**Navigation Bar Shelf Fill Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`navbarshelfcolor`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|7|

### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|---|---|
|Description|**Date and time that the record was migrated.**|
|DisplayName|**Record Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overriddencreatedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_PageHeaderBackgroundColor"></a> PageHeaderBackgroundColor

|Property|Value|
|---|---|
|Description|**Choose the page header background color**|
|DisplayName|**Page Header Fill Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`pageheaderbackgroundcolor`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|7|

### <a name="BKMK_PanelHeaderBackgroundColor"></a> PanelHeaderBackgroundColor

|Property|Value|
|---|---|
|Description|**Choose the panel header background color**|
|DisplayName|**Panel Header Fill Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`panelheaderbackgroundcolor`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|7|

### <a name="BKMK_ProcessControlColor"></a> ProcessControlColor

|Property|Value|
|---|---|
|Description|**Choose the primary background color for process controls**|
|DisplayName|**Legacy Accent Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`processcontrolcolor`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|7|

### <a name="BKMK_SelectedLinkEffect"></a> SelectedLinkEffect

|Property|Value|
|---|---|
|Description|**Choose the color that commands or lists will use to indicate selected items**|
|DisplayName|**Selected Link Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`selectedlinkeffect`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|7|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Theme**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`theme_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Custom**<br />State:0<br />TransitionData: None|
|2|Label: **System**<br />State:1<br />TransitionData: None|

### <a name="BKMK_ThemeId"></a> ThemeId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Theme**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`themeid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Time Zone Rule Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezoneruleversionnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Exchange rate for the currency associated with the Theme with respect to the base currency.**|
|DisplayName|**Currency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`transactioncurrencyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|transactioncurrency|

### <a name="BKMK_Type"></a> Type

|Property|Value|
|---|---|
|Description|**Define type of theme.**|
|DisplayName|**Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`type`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`theme_type`|
|DefaultValue|True|
|True Label|Custom|
|False Label|System|

### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|---|---|
|Description|**Time zone code that was in use when the record was created.**|
|DisplayName|**UTC Conversion Time Zone Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`utcconversiontimezonecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ExchangeRate](#BKMK_ExchangeRate)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [statecode](#BKMK_statecode)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was created.**|
|DisplayName|**Created On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who created the record.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|---|---|
|Description|**Exchange rate for the currency associated with the Theme with respect to the base currency.**|
|DisplayName|**ExchangeRate**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`exchangerate`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Disabled|
|MaxValue|100000000000|
|MinValue|1E-12|
|Precision|12|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who modified the record.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who modified the record.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier for the organization**|
|DisplayName|**Organization Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Theme**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`theme_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Custom**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **System**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [lk_theme_createdby](#BKMK_lk_theme_createdby)
- [lk_theme_createdonbehalfby](#BKMK_lk_theme_createdonbehalfby)
- [lk_theme_logoid](#BKMK_lk_theme_logoid)
- [lk_theme_modifiedby](#BKMK_lk_theme_modifiedby)
- [lk_theme_modifiedonbehalfby](#BKMK_lk_theme_modifiedonbehalfby)
- [organization_theme](#BKMK_organization_theme)
- [TransactionCurrency_Theme](#BKMK_TransactionCurrency_Theme)

### <a name="BKMK_lk_theme_createdby"></a> lk_theme_createdby

One-To-Many Relationship: [systemuser lk_theme_createdby](systemuser.md#BKMK_lk_theme_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_theme_createdonbehalfby"></a> lk_theme_createdonbehalfby

One-To-Many Relationship: [systemuser lk_theme_createdonbehalfby](systemuser.md#BKMK_lk_theme_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_theme_logoid"></a> lk_theme_logoid

One-To-Many Relationship: [webresource lk_theme_logoid](webresource.md#BKMK_lk_theme_logoid)

|Property|Value|
|---|---|
|ReferencedEntity|`webresource`|
|ReferencedAttribute|`webresourceid`|
|ReferencingAttribute|`logoid`|
|ReferencingEntityNavigationPropertyName|`logoimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_theme_modifiedby"></a> lk_theme_modifiedby

One-To-Many Relationship: [systemuser lk_theme_modifiedby](systemuser.md#BKMK_lk_theme_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_theme_modifiedonbehalfby"></a> lk_theme_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_theme_modifiedonbehalfby](systemuser.md#BKMK_lk_theme_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_theme"></a> organization_theme

One-To-Many Relationship: [organization organization_theme](organization.md#BKMK_organization_theme)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_Theme"></a> TransactionCurrency_Theme

One-To-Many Relationship: [transactioncurrency TransactionCurrency_Theme](transactioncurrency.md#BKMK_TransactionCurrency_Theme)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencingEntityNavigationPropertyName|`transactioncurrencyid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [theme_AsyncOperations](#BKMK_theme_AsyncOperations)
- [theme_BulkDeleteFailures](#BKMK_theme_BulkDeleteFailures)
- [theme_ProcessSession](#BKMK_theme_ProcessSession)

### <a name="BKMK_theme_AsyncOperations"></a> theme_AsyncOperations

Many-To-One Relationship: [asyncoperation theme_AsyncOperations](asyncoperation.md#BKMK_theme_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`theme_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_theme_BulkDeleteFailures"></a> theme_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure theme_BulkDeleteFailures](bulkdeletefailure.md#BKMK_theme_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`theme_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_theme_ProcessSession"></a> theme_ProcessSession

Many-To-One Relationship: [processsession theme_ProcessSession](processsession.md#BKMK_theme_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`theme_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.theme?displayProperty=fullName>
