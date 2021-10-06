---
title: "UserSettings table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the UserSettings table/entity."
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

# UserSettings table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

User's preferred settings.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Retrieve|GET [*org URI*]/api/data/v9.0/usersettingscollection(*systemuserid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/usersettingscollection<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/usersettingscollection(*systemuserid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|UserSettingses|
|DisplayCollectionName|User Settings|
|DisplayName|User Settings|
|EntitySetName|usersettingscollection|
|IsBPFEntity|False|
|LogicalCollectionName|usersettingses|
|LogicalName|usersettings|
|OwnershipType|BusinessOwned|
|PrimaryIdAttribute|systemuserid|
|PrimaryNameAttribute||
|SchemaName|UserSettings|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AddressBookSyncInterval](#BKMK_AddressBookSyncInterval)
- [AdvancedFindStartupMode](#BKMK_AdvancedFindStartupMode)
- [AMDesignator](#BKMK_AMDesignator)
- [AutoCaptureUserStatus](#BKMK_AutoCaptureUserStatus)
- [AutoCreateContactOnPromote](#BKMK_AutoCreateContactOnPromote)
- [BusinessUnitId](#BKMK_BusinessUnitId)
- [CalendarType](#BKMK_CalendarType)
- [CurrencyDecimalPrecision](#BKMK_CurrencyDecimalPrecision)
- [CurrencyFormatCode](#BKMK_CurrencyFormatCode)
- [CurrencySymbol](#BKMK_CurrencySymbol)
- [DataValidationModeForExportToExcel](#BKMK_DataValidationModeForExportToExcel)
- [DateFormatCode](#BKMK_DateFormatCode)
- [DateFormatString](#BKMK_DateFormatString)
- [DateSeparator](#BKMK_DateSeparator)
- [DecimalSymbol](#BKMK_DecimalSymbol)
- [DefaultCalendarView](#BKMK_DefaultCalendarView)
- [DefaultCountryCode](#BKMK_DefaultCountryCode)
- [DefaultDashboardId](#BKMK_DefaultDashboardId)
- [DefaultSearchExperience](#BKMK_DefaultSearchExperience)
- [EntityFormMode](#BKMK_EntityFormMode)
- [FullNameConventionCode](#BKMK_FullNameConventionCode)
- [GetStartedPaneContentEnabled](#BKMK_GetStartedPaneContentEnabled)
- [HelpLanguageId](#BKMK_HelpLanguageId)
- [HomepageArea](#BKMK_HomepageArea)
- [HomepageLayout](#BKMK_HomepageLayout)
- [HomepageSubarea](#BKMK_HomepageSubarea)
- [IgnoreUnsolicitedEmail](#BKMK_IgnoreUnsolicitedEmail)
- [IncomingEmailFilteringMethod](#BKMK_IncomingEmailFilteringMethod)
- [IsAppsForCrmAlertDismissed](#BKMK_IsAppsForCrmAlertDismissed)
- [IsAutoDataCaptureEnabled](#BKMK_IsAutoDataCaptureEnabled)
- [IsDefaultCountryCodeCheckEnabled](#BKMK_IsDefaultCountryCodeCheckEnabled)
- [IsDuplicateDetectionEnabledWhenGoingOnline](#BKMK_IsDuplicateDetectionEnabledWhenGoingOnline)
- [IsEmailConversationViewEnabled](#BKMK_IsEmailConversationViewEnabled)
- [IsGuidedHelpEnabled](#BKMK_IsGuidedHelpEnabled)
- [IsResourceBookingExchangeSyncEnabled](#BKMK_IsResourceBookingExchangeSyncEnabled)
- [IsSendAsAllowed](#BKMK_IsSendAsAllowed)
- [LastAlertsViewedTime](#BKMK_LastAlertsViewedTime)
- [LocaleId](#BKMK_LocaleId)
- [LongDateFormatCode](#BKMK_LongDateFormatCode)
- [NegativeCurrencyFormatCode](#BKMK_NegativeCurrencyFormatCode)
- [NegativeFormatCode](#BKMK_NegativeFormatCode)
- [NextTrackingNumber](#BKMK_NextTrackingNumber)
- [NumberGroupFormat](#BKMK_NumberGroupFormat)
- [NumberSeparator](#BKMK_NumberSeparator)
- [OfflineSyncInterval](#BKMK_OfflineSyncInterval)
- [OutlookSyncInterval](#BKMK_OutlookSyncInterval)
- [PagingLimit](#BKMK_PagingLimit)
- [PersonalizationSettings](#BKMK_PersonalizationSettings)
- [PMDesignator](#BKMK_PMDesignator)
- [PricingDecimalPrecision](#BKMK_PricingDecimalPrecision)
- [ReportScriptErrors](#BKMK_ReportScriptErrors)
- [ResourceBookingExchangeSyncVersion](#BKMK_ResourceBookingExchangeSyncVersion)
- [SelectedGlobalFilterId](#BKMK_SelectedGlobalFilterId)
- [ShowWeekNumber](#BKMK_ShowWeekNumber)
- [SplitViewState](#BKMK_SplitViewState)
- [SyncContactCompany](#BKMK_SyncContactCompany)
- [SystemUserId](#BKMK_SystemUserId)
- [TimeFormatCode](#BKMK_TimeFormatCode)
- [TimeFormatString](#BKMK_TimeFormatString)
- [TimeSeparator](#BKMK_TimeSeparator)
- [TimeZoneBias](#BKMK_TimeZoneBias)
- [TimeZoneCode](#BKMK_TimeZoneCode)
- [TimeZoneDaylightBias](#BKMK_TimeZoneDaylightBias)
- [TimeZoneDaylightDay](#BKMK_TimeZoneDaylightDay)
- [TimeZoneDaylightDayOfWeek](#BKMK_TimeZoneDaylightDayOfWeek)
- [TimeZoneDaylightHour](#BKMK_TimeZoneDaylightHour)
- [TimeZoneDaylightMinute](#BKMK_TimeZoneDaylightMinute)
- [TimeZoneDaylightMonth](#BKMK_TimeZoneDaylightMonth)
- [TimeZoneDaylightSecond](#BKMK_TimeZoneDaylightSecond)
- [TimeZoneDaylightYear](#BKMK_TimeZoneDaylightYear)
- [TimeZoneStandardBias](#BKMK_TimeZoneStandardBias)
- [TimeZoneStandardDay](#BKMK_TimeZoneStandardDay)
- [TimeZoneStandardDayOfWeek](#BKMK_TimeZoneStandardDayOfWeek)
- [TimeZoneStandardHour](#BKMK_TimeZoneStandardHour)
- [TimeZoneStandardMinute](#BKMK_TimeZoneStandardMinute)
- [TimeZoneStandardMonth](#BKMK_TimeZoneStandardMonth)
- [TimeZoneStandardSecond](#BKMK_TimeZoneStandardSecond)
- [TimeZoneStandardYear](#BKMK_TimeZoneStandardYear)
- [TrackingTokenId](#BKMK_TrackingTokenId)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [UILanguageId](#BKMK_UILanguageId)
- [UseCrmFormForAppointment](#BKMK_UseCrmFormForAppointment)
- [UseCrmFormForContact](#BKMK_UseCrmFormForContact)
- [UseCrmFormForEmail](#BKMK_UseCrmFormForEmail)
- [UseCrmFormForTask](#BKMK_UseCrmFormForTask)
- [UseImageStrips](#BKMK_UseImageStrips)
- [UserProfile](#BKMK_UserProfile)
- [VisualizationPaneLayout](#BKMK_VisualizationPaneLayout)
- [WorkdayStartTime](#BKMK_WorkdayStartTime)
- [WorkdayStopTime](#BKMK_WorkdayStopTime)


### <a name="BKMK_AddressBookSyncInterval"></a> AddressBookSyncInterval

|Property|Value|
|--------|-----|
|Description|Normal polling frequency used for address book synchronization in Microsoft Office Outlook.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|addressbooksyncinterval|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_AdvancedFindStartupMode"></a> AdvancedFindStartupMode

|Property|Value|
|--------|-----|
|Description|Default mode, such as simple or detailed, for advanced find.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|advancedfindstartupmode|
|MaxValue||
|MinValue||
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_AMDesignator"></a> AMDesignator

|Property|Value|
|--------|-----|
|Description|AM designator to use in Microsoft Dynamics 365.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|amdesignator|
|MaxLength|25|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_AutoCaptureUserStatus"></a> AutoCaptureUserStatus

|Property|Value|
|--------|-----|
|Description|Set user status for ADC Suggestions|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|autocaptureuserstatus|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_AutoCreateContactOnPromote"></a> AutoCreateContactOnPromote

|Property|Value|
|--------|-----|
|Description|Auto-create contact on client promote|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|autocreatecontactonpromote|
|MaxValue||
|MinValue||
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the business unit with which the user is associated.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|businessunitid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_CalendarType"></a> CalendarType

|Property|Value|
|--------|-----|
|Description|Calendar type for the system. Set to Gregorian US by default.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|calendartype|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_CurrencyDecimalPrecision"></a> CurrencyDecimalPrecision

|Property|Value|
|--------|-----|
|Description|Number of decimal places that can be used for currency.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|currencydecimalprecision|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|ApplicationRequired|
|Type|Integer|


### <a name="BKMK_CurrencyFormatCode"></a> CurrencyFormatCode

|Property|Value|
|--------|-----|
|Description|Information about how currency symbols are placed in Microsoft Dynamics 365.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|currencyformatcode|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_CurrencySymbol"></a> CurrencySymbol

|Property|Value|
|--------|-----|
|Description|Symbol used for currency in Microsoft Dynamics 365.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|currencysymbol|
|MaxLength|13|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_DataValidationModeForExportToExcel"></a> DataValidationModeForExportToExcel

|Property|Value|
|--------|-----|
|Description|Information that specifies the level of data validation in excel worksheets exported in a format suitable for import.|
|DisplayName|Data Validation Mode For Export To Excel|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|datavalidationmodeforexporttoexcel|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### DataValidationModeForExportToExcel Choices/Options

|Value|Label|
|-----|-----|
|0|Full|
|1|None|



### <a name="BKMK_DateFormatCode"></a> DateFormatCode

|Property|Value|
|--------|-----|
|Description|Information about how the date is displayed in Microsoft Dynamics 365.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|dateformatcode|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_DateFormatString"></a> DateFormatString

|Property|Value|
|--------|-----|
|Description|String showing how the date is displayed throughout Microsoft 365.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|dateformatstring|
|MaxLength|255|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_DateSeparator"></a> DateSeparator

|Property|Value|
|--------|-----|
|Description|Character used to separate the month, the day, and the year in dates in Microsoft Dynamics 365.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|dateseparator|
|MaxLength|5|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_DecimalSymbol"></a> DecimalSymbol

|Property|Value|
|--------|-----|
|Description|Symbol used for decimal in Microsoft Dynamics 365.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|decimalsymbol|
|MaxLength|5|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_DefaultCalendarView"></a> DefaultCalendarView

|Property|Value|
|--------|-----|
|Description|Default calendar view for the user.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|defaultcalendarview|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_DefaultCountryCode"></a> DefaultCountryCode

|Property|Value|
|--------|-----|
|Description|Text area to enter default country code.|
|DisplayName|Default Country Code|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|defaultcountrycode|
|MaxLength|30|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_DefaultDashboardId"></a> DefaultDashboardId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the default dashboard.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|defaultdashboardid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_DefaultSearchExperience"></a> DefaultSearchExperience

|Property|Value|
|--------|-----|
|Description|Default search experience for the user.|
|DisplayName|Default Search Experience|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|defaultsearchexperience|
|RequiredLevel|None|
|Type|Picklist|

#### DefaultSearchExperience Choices/Options

|Value|Label|
|-----|-----|
|0|Dataverse search|
|1|Categorized search|
|2|Use last search|
|3|Custom search|



### <a name="BKMK_EntityFormMode"></a> EntityFormMode

|Property|Value|
|--------|-----|
|Description|Indicates the form mode to be used.|
|DisplayName|Form Mode|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityformmode|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### EntityFormMode Choices/Options

|Value|Label|
|-----|-----|
|0|Organization default|
|1|Read-optimized|
|2|Edit|



### <a name="BKMK_FullNameConventionCode"></a> FullNameConventionCode

|Property|Value|
|--------|-----|
|Description|Order in which names are to be displayed in Microsoft Dynamics 365.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|fullnameconventioncode|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_GetStartedPaneContentEnabled"></a> GetStartedPaneContentEnabled

|Property|Value|
|--------|-----|
|Description|Information that specifies whether the Get Started pane in lists is enabled.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|getstartedpanecontentenabled|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### GetStartedPaneContentEnabled Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: True



### <a name="BKMK_HelpLanguageId"></a> HelpLanguageId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the Help language.|
|DisplayName||
|Format|Language|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|helplanguageid|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|ApplicationRequired|
|Type|Integer|


### <a name="BKMK_HomepageArea"></a> HomepageArea

|Property|Value|
|--------|-----|
|Description|Web site home page for the user.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|homepagearea|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_HomepageLayout"></a> HomepageLayout

|Property|Value|
|--------|-----|
|Description|Configuration of the home page layout.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|homepagelayout|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_HomepageSubarea"></a> HomepageSubarea

|Property|Value|
|--------|-----|
|Description|Web site page for the user.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|homepagesubarea|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IgnoreUnsolicitedEmail"></a> IgnoreUnsolicitedEmail

|Property|Value|
|--------|-----|
|Description|Information that specifies whether a user account is to ignore unsolicited email (deprecated).|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ignoreunsolicitedemail|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IgnoreUnsolicitedEmail Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: True



### <a name="BKMK_IncomingEmailFilteringMethod"></a> IncomingEmailFilteringMethod

|Property|Value|
|--------|-----|
|Description|Incoming email filtering method.|
|DisplayName|Incoming Email Filtering Method|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|incomingemailfilteringmethod|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### IncomingEmailFilteringMethod Choices/Options

|Value|Label|
|-----|-----|
|0|All email messages|
|1|Email messages in response to Dynamics 365 email|
|2|Email messages from Dynamics 365 Leads, Contacts and Accounts|
|3|Email messages from Dynamics 365 records that are email enabled|
|4|No email messages|



### <a name="BKMK_IsAppsForCrmAlertDismissed"></a> IsAppsForCrmAlertDismissed

|Property|Value|
|--------|-----|
|Description|Show or dismiss alert for Apps for 365.|
|DisplayName|Show alert for Apps for 365.|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isappsforcrmalertdismissed|
|RequiredLevel|None|
|Type|Boolean|

#### IsAppsForCrmAlertDismissed Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsAutoDataCaptureEnabled"></a> IsAutoDataCaptureEnabled

|Property|Value|
|--------|-----|
|Description|Indicates whether to use the Auto Capture feature enabled or not.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isautodatacaptureenabled|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsAutoDataCaptureEnabled Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsDefaultCountryCodeCheckEnabled"></a> IsDefaultCountryCodeCheckEnabled

|Property|Value|
|--------|-----|
|Description|Enable or disable country code selection .|
|DisplayName|Enable Default Country Code|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isdefaultcountrycodecheckenabled|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsDefaultCountryCodeCheckEnabled Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: True



### <a name="BKMK_IsDuplicateDetectionEnabledWhenGoingOnline"></a> IsDuplicateDetectionEnabledWhenGoingOnline

|Property|Value|
|--------|-----|
|Description|Indicates if duplicate detection is enabled when going online.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isduplicatedetectionenabledwhengoingonline|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsDuplicateDetectionEnabledWhenGoingOnline Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsEmailConversationViewEnabled"></a> IsEmailConversationViewEnabled

|Property|Value|
|--------|-----|
|Description|Enable or disable email conversation view on timeline wall selection.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isemailconversationviewenabled|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsEmailConversationViewEnabled Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsGuidedHelpEnabled"></a> IsGuidedHelpEnabled

|Property|Value|
|--------|-----|
|Description|Enable or disable guided help.|
|DisplayName|Enable Default Guided Help|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isguidedhelpenabled|
|RequiredLevel|None|
|Type|Boolean|

#### IsGuidedHelpEnabled Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: True



### <a name="BKMK_IsResourceBookingExchangeSyncEnabled"></a> IsResourceBookingExchangeSyncEnabled

|Property|Value|
|--------|-----|
|Description|Indicates if the synchronization of user resource booking with Exchange is enabled at user level.|
|DisplayName|Resource booking synchronization enabled|
|IsValidForCreate|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isresourcebookingexchangesyncenabled|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsResourceBookingExchangeSyncEnabled Choices/Options

|Value|Label|
|-----|-----|
|1|Enabled|
|0|Disabled|

**DefaultValue**: False



### <a name="BKMK_IsSendAsAllowed"></a> IsSendAsAllowed

|Property|Value|
|--------|-----|
|Description|Indicates if send as other user privilege is enabled or not.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|issendasallowed|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsSendAsAllowed Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_LastAlertsViewedTime"></a> LastAlertsViewedTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the last time when the traces were read from the database.|
|DisplayName||
|Format|DateAndTime|
|IsValidForCreate|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|lastalertsviewedtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_LocaleId"></a> LocaleId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user locale.|
|DisplayName||
|Format|Locale|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|localeid|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|ApplicationRequired|
|Type|Integer|


### <a name="BKMK_LongDateFormatCode"></a> LongDateFormatCode

|Property|Value|
|--------|-----|
|Description|Information that specifies how Long Date is displayed throughout Microsoft 365.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|longdateformatcode|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_NegativeCurrencyFormatCode"></a> NegativeCurrencyFormatCode

|Property|Value|
|--------|-----|
|Description|Information that specifies how negative currency numbers are displayed in Microsoft Dynamics 365.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|negativecurrencyformatcode|
|MaxValue|15|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_NegativeFormatCode"></a> NegativeFormatCode

|Property|Value|
|--------|-----|
|Description|Information that specifies how negative numbers are displayed in Microsoft Dynamics 365.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|negativeformatcode|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_NextTrackingNumber"></a> NextTrackingNumber

|Property|Value|
|--------|-----|
|Description|Next tracking number.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|nexttrackingnumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_NumberGroupFormat"></a> NumberGroupFormat

|Property|Value|
|--------|-----|
|Description|Information that specifies how numbers are grouped in Microsoft Dynamics 365.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|numbergroupformat|
|MaxLength|25|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_NumberSeparator"></a> NumberSeparator

|Property|Value|
|--------|-----|
|Description|Symbol used for number separation in Microsoft Dynamics 365.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|numberseparator|
|MaxLength|5|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OfflineSyncInterval"></a> OfflineSyncInterval

|Property|Value|
|--------|-----|
|Description|Normal polling frequency used for background offline synchronization in Microsoft Office Outlook.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|offlinesyncinterval|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_OutlookSyncInterval"></a> OutlookSyncInterval

|Property|Value|
|--------|-----|
|Description|Normal polling frequency used for record synchronization in Microsoft Office Outlook.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|outlooksyncinterval|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_PagingLimit"></a> PagingLimit

|Property|Value|
|--------|-----|
|Description|Information that specifies how many items to list on a page in list views.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|paginglimit|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_PersonalizationSettings"></a> PersonalizationSettings

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName||
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|personalizationsettings|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_PMDesignator"></a> PMDesignator

|Property|Value|
|--------|-----|
|Description|PM designator to use in Microsoft Dynamics 365.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|pmdesignator|
|MaxLength|25|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_PricingDecimalPrecision"></a> PricingDecimalPrecision

|Property|Value|
|--------|-----|
|Description|Number of decimal places that can be used for prices.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|pricingdecimalprecision|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|ApplicationRequired|
|Type|Integer|


### <a name="BKMK_ReportScriptErrors"></a> ReportScriptErrors

|Property|Value|
|--------|-----|
|Description|Picklist for selecting the user preference for reporting scripting errors.|
|DisplayName|Report Script Errors|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|reportscripterrors|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ReportScriptErrors Choices/Options

|Value|Label|
|-----|-----|
|1|Ask me for permission to send an error report to Microsoft|
|2|Automatically send an error report to Microsoft without asking me for permission|
|3|Never send an error report to Microsoft about Microsoft Dynamics 365|



### <a name="BKMK_ResourceBookingExchangeSyncVersion"></a> ResourceBookingExchangeSyncVersion

|Property|Value|
|--------|-----|
|Description|The version number for resource booking synchronization with Exchange.|
|DisplayName|User resource booking synchronization version|
|IsValidForCreate|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|resourcebookingexchangesyncversion|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|SystemRequired|
|Type|BigInt|


### <a name="BKMK_SelectedGlobalFilterId"></a> SelectedGlobalFilterId

|Property|Value|
|--------|-----|
|Description|Store selected customer service hub dashboard saved filter id.|
|DisplayName||
|IsValidForCreate|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|selectedglobalfilterid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_ShowWeekNumber"></a> ShowWeekNumber

|Property|Value|
|--------|-----|
|Description|Information that specifies whether to display the week number in calendar displays in Microsoft Dynamics 365.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|showweeknumber|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### ShowWeekNumber Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_SplitViewState"></a> SplitViewState

|Property|Value|
|--------|-----|
|Description|For Internal use only|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|splitviewstate|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### SplitViewState Choices/Options

|Value|Label|
|-----|-----|
|1|Expanded|
|0|Collapsed|

**DefaultValue**: False



### <a name="BKMK_SyncContactCompany"></a> SyncContactCompany

|Property|Value|
|--------|-----|
|Description|Indicates if the company field in Microsoft Office Outlook items are set during Outlook synchronization.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|synccontactcompany|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### SyncContactCompany Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_SystemUserId"></a> SystemUserId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|systemuserid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_TimeFormatCode"></a> TimeFormatCode

|Property|Value|
|--------|-----|
|Description|Information that specifies how the time is displayed in Microsoft Dynamics 365.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timeformatcode|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TimeFormatString"></a> TimeFormatString

|Property|Value|
|--------|-----|
|Description|Text for how time is displayed in Microsoft Dynamics 365.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timeformatstring|
|MaxLength|255|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TimeSeparator"></a> TimeSeparator

|Property|Value|
|--------|-----|
|Description|Text for how time is displayed in Microsoft Dynamics 365.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timeseparator|
|MaxLength|5|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TimeZoneBias"></a> TimeZoneBias

|Property|Value|
|--------|-----|
|Description|Local time zone adjustment for the user. System calculated based on the time zone selected.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezonebias|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TimeZoneCode"></a> TimeZoneCode

|Property|Value|
|--------|-----|
|Description|Local time zone for the user.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezonecode|
|MaxValue||
|MinValue||
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TimeZoneDaylightBias"></a> TimeZoneDaylightBias

|Property|Value|
|--------|-----|
|Description|Local time zone daylight adjustment for the user. System calculated based on the time zone selected.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezonedaylightbias|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TimeZoneDaylightDay"></a> TimeZoneDaylightDay

|Property|Value|
|--------|-----|
|Description|Local time zone daylight day for the user. System calculated based on the time zone selected.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezonedaylightday|
|MaxValue||
|MinValue||
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TimeZoneDaylightDayOfWeek"></a> TimeZoneDaylightDayOfWeek

|Property|Value|
|--------|-----|
|Description|Local time zone daylight day of week for the user. System calculated based on the time zone selected in Options.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezonedaylightdayofweek|
|MaxValue||
|MinValue||
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TimeZoneDaylightHour"></a> TimeZoneDaylightHour

|Property|Value|
|--------|-----|
|Description|Local time zone daylight hour for the user. System calculated based on the time zone selected.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezonedaylighthour|
|MaxValue||
|MinValue||
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TimeZoneDaylightMinute"></a> TimeZoneDaylightMinute

|Property|Value|
|--------|-----|
|Description|Local time zone daylight minute for the user. System calculated based on the time zone selected.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezonedaylightminute|
|MaxValue||
|MinValue||
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TimeZoneDaylightMonth"></a> TimeZoneDaylightMonth

|Property|Value|
|--------|-----|
|Description|Local time zone daylight month for the user. System calculated based on the time zone selected.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezonedaylightmonth|
|MaxValue||
|MinValue||
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TimeZoneDaylightSecond"></a> TimeZoneDaylightSecond

|Property|Value|
|--------|-----|
|Description|Local time zone daylight second for the user. System calculated based on the time zone selected.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezonedaylightsecond|
|MaxValue||
|MinValue||
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TimeZoneDaylightYear"></a> TimeZoneDaylightYear

|Property|Value|
|--------|-----|
|Description|Local time zone daylight year for the user. System calculated based on the time zone selected.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezonedaylightyear|
|MaxValue||
|MinValue||
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TimeZoneStandardBias"></a> TimeZoneStandardBias

|Property|Value|
|--------|-----|
|Description|Local time zone standard time bias for the user. System calculated based on the time zone selected.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezonestandardbias|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TimeZoneStandardDay"></a> TimeZoneStandardDay

|Property|Value|
|--------|-----|
|Description|Local time zone standard day for the user. System calculated based on the time zone selected.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezonestandardday|
|MaxValue||
|MinValue||
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TimeZoneStandardDayOfWeek"></a> TimeZoneStandardDayOfWeek

|Property|Value|
|--------|-----|
|Description|Local time zone standard day of week for the user. System calculated based on the time zone selected.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezonestandarddayofweek|
|MaxValue||
|MinValue||
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TimeZoneStandardHour"></a> TimeZoneStandardHour

|Property|Value|
|--------|-----|
|Description|Local time zone standard hour for the user. System calculated based on the time zone selected.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezonestandardhour|
|MaxValue||
|MinValue||
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TimeZoneStandardMinute"></a> TimeZoneStandardMinute

|Property|Value|
|--------|-----|
|Description|Local time zone standard minute for the user. System calculated based on the time zone selected.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezonestandardminute|
|MaxValue||
|MinValue||
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TimeZoneStandardMonth"></a> TimeZoneStandardMonth

|Property|Value|
|--------|-----|
|Description|Local time zone standard month for the user. System calculated based on the time zone selected.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezonestandardmonth|
|MaxValue||
|MinValue||
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TimeZoneStandardSecond"></a> TimeZoneStandardSecond

|Property|Value|
|--------|-----|
|Description|Local time zone standard second for the user. System calculated based on the time zone selected.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezonestandardsecond|
|MaxValue||
|MinValue||
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TimeZoneStandardYear"></a> TimeZoneStandardYear

|Property|Value|
|--------|-----|
|Description|Local time zone standard year for the user. System calculated based on the time zone selected.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezonestandardyear|
|MaxValue||
|MinValue||
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TrackingTokenId"></a> TrackingTokenId

|Property|Value|
|--------|-----|
|Description|Tracking token ID.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|trackingtokenid|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the default currency of the user.|
|DisplayName|Currency|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|transactioncurrencyid|
|RequiredLevel|None|
|Targets|transactioncurrency|
|Type|Lookup|


### <a name="BKMK_UILanguageId"></a> UILanguageId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the language in which to view the user interface (UI).|
|DisplayName||
|Format|Language|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|uilanguageid|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_UseCrmFormForAppointment"></a> UseCrmFormForAppointment

|Property|Value|
|--------|-----|
|Description|Indicates whether to use the Microsoft Dynamics 365 appointment form within Microsoft Office Outlook for creating new appointments.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|usecrmformforappointment|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### UseCrmFormForAppointment Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_UseCrmFormForContact"></a> UseCrmFormForContact

|Property|Value|
|--------|-----|
|Description|Indicates whether to use the Microsoft Dynamics 365 contact form within Microsoft Office Outlook for creating new contacts.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|usecrmformforcontact|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### UseCrmFormForContact Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_UseCrmFormForEmail"></a> UseCrmFormForEmail

|Property|Value|
|--------|-----|
|Description|Indicates whether to use the Microsoft Dynamics 365 email form within Microsoft Office Outlook for creating new emails.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|usecrmformforemail|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### UseCrmFormForEmail Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_UseCrmFormForTask"></a> UseCrmFormForTask

|Property|Value|
|--------|-----|
|Description|Indicates whether to use the Microsoft Dynamics 365 task form within Microsoft Office Outlook for creating new tasks.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|usecrmformfortask|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### UseCrmFormForTask Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_UseImageStrips"></a> UseImageStrips

|Property|Value|
|--------|-----|
|Description|Indicates whether image strips are used to render images.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|useimagestrips|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### UseImageStrips Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: True



### <a name="BKMK_UserProfile"></a> UserProfile

|Property|Value|
|--------|-----|
|Description|Specifies user profile ids in comma separated list.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|userprofile|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_VisualizationPaneLayout"></a> VisualizationPaneLayout

|Property|Value|
|--------|-----|
|Description|The layout of the visualization pane.|
|DisplayName|Visualization Pane Layout.|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|visualizationpanelayout|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### VisualizationPaneLayout Choices/Options

|Value|Label|
|-----|-----|
|0|Top-bottom|
|1|Side-by-side|



### <a name="BKMK_WorkdayStartTime"></a> WorkdayStartTime

|Property|Value|
|--------|-----|
|Description|Workday start time for the user.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|workdaystarttime|
|MaxLength|5|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_WorkdayStopTime"></a> WorkdayStopTime

|Property|Value|
|--------|-----|
|Description|Workday stop time for the user.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|workdaystoptime|
|MaxLength|5|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AllowEmailCredentials](#BKMK_AllowEmailCredentials)
- [BusinessUnitIdName](#BKMK_BusinessUnitIdName)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [EmailPassword](#BKMK_EmailPassword)
- [EmailUsername](#BKMK_EmailUsername)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_AllowEmailCredentials"></a> AllowEmailCredentials

|Property|Value|
|--------|-----|
|Description|This attribute is no longer used. The data is now in the Mailbox.AllowEmailConnectorToUseCredentials attribute.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|allowemailcredentials|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### AllowEmailCredentials Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_BusinessUnitIdName"></a> BusinessUnitIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|businessunitidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the user settings.|
|DisplayName||
|IsValidForForm|False|
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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the user settings object was created.|
|DisplayName||
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the usersettings.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|False|
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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EmailPassword"></a> EmailPassword

|Property|Value|
|--------|-----|
|Description|This attribute is no longer used. The data is now in the Mailbox.Password attribute.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|emailpassword|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EmailUsername"></a> EmailUsername

|Property|Value|
|--------|-----|
|Description|This attribute is no longer used. The data is now in the Mailbox.UserName attribute.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|emailusername|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the user settings.|
|DisplayName||
|IsValidForForm|False|
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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the user settings object was last modified.|
|DisplayName||
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who last modified the usersettings.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|False|
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
|RequiredLevel|None|
|Type|String|


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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [transactioncurrency_usersettings](#BKMK_transactioncurrency_usersettings)
- [user_settings](#BKMK_user_settings)
- [lk_usersettingsbase_createdby](#BKMK_lk_usersettingsbase_createdby)
- [lk_usersettings_createdonbehalfby](#BKMK_lk_usersettings_createdonbehalfby)
- [lk_usersettingsbase_modifiedby](#BKMK_lk_usersettingsbase_modifiedby)
- [lk_usersettings_modifiedonbehalfby](#BKMK_lk_usersettings_modifiedonbehalfby)
- [business_unit_user_settings](#BKMK_business_unit_user_settings)


### <a name="BKMK_transactioncurrency_usersettings"></a> transactioncurrency_usersettings

See transactioncurrency Table [transactioncurrency_usersettings](transactioncurrency.md#BKMK_transactioncurrency_usersettings) One-To-Many relationship.

### <a name="BKMK_user_settings"></a> user_settings

See systemuser Table [user_settings](systemuser.md#BKMK_user_settings) One-To-Many relationship.

### <a name="BKMK_lk_usersettingsbase_createdby"></a> lk_usersettingsbase_createdby

See systemuser Table [lk_usersettingsbase_createdby](systemuser.md#BKMK_lk_usersettingsbase_createdby) One-To-Many relationship.

### <a name="BKMK_lk_usersettings_createdonbehalfby"></a> lk_usersettings_createdonbehalfby

See systemuser Table [lk_usersettings_createdonbehalfby](systemuser.md#BKMK_lk_usersettings_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_usersettingsbase_modifiedby"></a> lk_usersettingsbase_modifiedby

See systemuser Table [lk_usersettingsbase_modifiedby](systemuser.md#BKMK_lk_usersettingsbase_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_usersettings_modifiedonbehalfby"></a> lk_usersettings_modifiedonbehalfby

See systemuser Table [lk_usersettings_modifiedonbehalfby](systemuser.md#BKMK_lk_usersettings_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_business_unit_user_settings"></a> business_unit_user_settings

See businessunit Table [business_unit_user_settings](businessunit.md#BKMK_business_unit_user_settings) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.usersettings?text=usersettings EntityType" />