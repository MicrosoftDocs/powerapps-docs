---
title: "UserSettings Entity Reference (Common Data Service for Apps)| MicrosoftDocs"
description: "Includes schema information and supported messages for the UserSettings entity."

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
# UserSettings Entity Reference

User's preferred settings.

## Entity Properties

**DisplayName**: User Settings<br />
**DisplayCollectionName**: User Settings<br />
**SchemaName**: UserSettings<br />
**CollectionSchemaName**: UserSettingses<br />
**LogicalName**: usersettings<br />
**LogicalCollectionName**: usersettingses<br />
**EntitySetName**: usersettingscollection<br />
**PrimaryIdAttribute**: systemuserid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: BusinessOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AddressBookSyncInterval](#BKMK_AddressBookSyncInterval)
- [AdvancedFindStartupMode](#BKMK_AdvancedFindStartupMode)
- [AMDesignator](#BKMK_AMDesignator)
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

**Description**: Normal polling frequency used for address book synchronization in Microsoft Office Outlook.<br />
**DisplayName**: <br />
**LogicalName**: addressbooksyncinterval<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_AdvancedFindStartupMode"></a> AdvancedFindStartupMode

**Description**: Default mode, such as simple or detailed, for advanced find.<br />
**DisplayName**: <br />
**LogicalName**: advancedfindstartupmode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: <br />
**MinValue**: 


### <a name="BKMK_AMDesignator"></a> AMDesignator

**Description**: AM designator to use in Microsoft Dynamics 365.<br />
**DisplayName**: <br />
**LogicalName**: amdesignator<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 25


### <a name="BKMK_AutoCreateContactOnPromote"></a> AutoCreateContactOnPromote

**Description**: Auto-create contact on client promote<br />
**DisplayName**: <br />
**LogicalName**: autocreatecontactonpromote<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: <br />
**MinValue**: 


### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

**Description**: Unique identifier of the business unit with which the user is associated.<br />
**DisplayName**: <br />
**LogicalName**: businessunitid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_CalendarType"></a> CalendarType

**Description**: Calendar type for the system. Set to Gregorian US by default.<br />
**DisplayName**: <br />
**LogicalName**: calendartype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_CurrencyDecimalPrecision"></a> CurrencyDecimalPrecision

**Description**: Number of decimal places that can be used for currency.<br />
**DisplayName**: <br />
**LogicalName**: currencydecimalprecision<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_CurrencyFormatCode"></a> CurrencyFormatCode

**Description**: Information about how currency symbols are placed in Microsoft Dynamics 365.<br />
**DisplayName**: <br />
**LogicalName**: currencyformatcode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_CurrencySymbol"></a> CurrencySymbol

**Description**: Symbol used for currency in Microsoft Dynamics 365.<br />
**DisplayName**: <br />
**LogicalName**: currencysymbol<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 13


### <a name="BKMK_DataValidationModeForExportToExcel"></a> DataValidationModeForExportToExcel

**Description**: Information that specifies the level of data validation in excel worksheets exported in a format suitable for import.<br />
**DisplayName**: Data Validation Mode For Export To Excel<br />
**LogicalName**: datavalidationmodeforexporttoexcel<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Full
- **Value**: 1 **Label**: None



### <a name="BKMK_DateFormatCode"></a> DateFormatCode

**Description**: Information about how the date is displayed in Microsoft Dynamics 365.<br />
**DisplayName**: <br />
**LogicalName**: dateformatcode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_DateFormatString"></a> DateFormatString

**Description**: String showing how the date is displayed throughout Microsoft 365.<br />
**DisplayName**: <br />
**LogicalName**: dateformatstring<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 255


### <a name="BKMK_DateSeparator"></a> DateSeparator

**Description**: Character used to separate the month, the day, and the year in dates in Microsoft Dynamics 365.<br />
**DisplayName**: <br />
**LogicalName**: dateseparator<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 5


### <a name="BKMK_DecimalSymbol"></a> DecimalSymbol

**Description**: Symbol used for decimal in Microsoft Dynamics 365.<br />
**DisplayName**: <br />
**LogicalName**: decimalsymbol<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 5


### <a name="BKMK_DefaultCalendarView"></a> DefaultCalendarView

**Description**: Default calendar view for the user.<br />
**DisplayName**: <br />
**LogicalName**: defaultcalendarview<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_DefaultCountryCode"></a> DefaultCountryCode

**Description**: Text area to enter default country code.<br />
**DisplayName**: Default Country Code<br />
**LogicalName**: defaultcountrycode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 30


### <a name="BKMK_DefaultDashboardId"></a> DefaultDashboardId

**Description**: Unique identifier of the default dashboard.<br />
**DisplayName**: <br />
**LogicalName**: defaultdashboardid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_DefaultSearchExperience"></a> DefaultSearchExperience

**Description**: Default search experience for the user.<br />
**DisplayName**: Default Search Experience<br />
**LogicalName**: defaultsearchexperience<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Relevance search
- **Value**: 1 **Label**: Categorized search
- **Value**: 2 **Label**: Use last search
- **Value**: 3 **Label**: Custom search



### <a name="BKMK_EntityFormMode"></a> EntityFormMode

**Description**: Indicates the form mode to be used.<br />
**DisplayName**: Form Mode<br />
**LogicalName**: entityformmode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Organization default
- **Value**: 1 **Label**: Read-optimized
- **Value**: 2 **Label**: Edit



### <a name="BKMK_FullNameConventionCode"></a> FullNameConventionCode

**Description**: Order in which names are to be displayed in Microsoft Dynamics 365.<br />
**DisplayName**: <br />
**LogicalName**: fullnameconventioncode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_GetStartedPaneContentEnabled"></a> GetStartedPaneContentEnabled

**Description**: Information that specifies whether the Get Started pane in lists is enabled.<br />
**DisplayName**: <br />
**LogicalName**: getstartedpanecontentenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_HelpLanguageId"></a> HelpLanguageId

**Description**: Unique identifier of the Help language.<br />
**DisplayName**: <br />
**LogicalName**: helplanguageid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Integer<br />
**Format**: Language<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_HomepageArea"></a> HomepageArea

**Description**: Web site home page for the user.<br />
**DisplayName**: <br />
**LogicalName**: homepagearea<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_HomepageLayout"></a> HomepageLayout

**Description**: Configuration of the home page layout.<br />
**DisplayName**: <br />
**LogicalName**: homepagelayout<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_HomepageSubarea"></a> HomepageSubarea

**Description**: Web site page for the user.<br />
**DisplayName**: <br />
**LogicalName**: homepagesubarea<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_IgnoreUnsolicitedEmail"></a> IgnoreUnsolicitedEmail

**Description**: Information that specifies whether a user account is to ignore unsolicited email (deprecated).<br />
**DisplayName**: <br />
**LogicalName**: ignoreunsolicitedemail<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_IncomingEmailFilteringMethod"></a> IncomingEmailFilteringMethod

**Description**: Incoming email filtering method.<br />
**DisplayName**: Incoming Email Filtering Method<br />
**LogicalName**: incomingemailfilteringmethod<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: All email messages
- **Value**: 1 **Label**: Email messages in response to Dynamics 365 email
- **Value**: 2 **Label**: Email messages from Dynamics 365 Leads, Contacts and Accounts
- **Value**: 3 **Label**: Email messages from Dynamics 365 records that are email enabled



### <a name="BKMK_IsAppsForCrmAlertDismissed"></a> IsAppsForCrmAlertDismissed

**Description**: Show or dismiss alert for Apps for 365.<br />
**DisplayName**: Show alert for Apps for 365.<br />
**LogicalName**: isappsforcrmalertdismissed<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsAutoDataCaptureEnabled"></a> IsAutoDataCaptureEnabled

**Description**: Indicates whether to use the Auto Capture feature enabled or not.<br />
**DisplayName**: <br />
**LogicalName**: isautodatacaptureenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsDefaultCountryCodeCheckEnabled"></a> IsDefaultCountryCodeCheckEnabled

**Description**: Enable or disable country code selection .<br />
**DisplayName**: Enable Default Country Code<br />
**LogicalName**: isdefaultcountrycodecheckenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_IsDuplicateDetectionEnabledWhenGoingOnline"></a> IsDuplicateDetectionEnabledWhenGoingOnline

**Description**: Indicates if duplicate detection is enabled when going online.<br />
**DisplayName**: <br />
**LogicalName**: isduplicatedetectionenabledwhengoingonline<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsGuidedHelpEnabled"></a> IsGuidedHelpEnabled

**Description**: Enable or disable guided help.<br />
**DisplayName**: Enable Default Guided Help<br />
**LogicalName**: isguidedhelpenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_IsResourceBookingExchangeSyncEnabled"></a> IsResourceBookingExchangeSyncEnabled

**Description**: Indicates if the synchronization of user resource booking with Exchange is enabled at user level.<br />
**DisplayName**: Resource booking synchronization enabled<br />
**LogicalName**: isresourcebookingexchangesyncenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Enabled
- **FalseOption Value**: 0 **Label**: Disabled

**DefaultValue**: False


### <a name="BKMK_IsSendAsAllowed"></a> IsSendAsAllowed

**Description**: Indicates if send as other user privilege is enabled or not.<br />
**DisplayName**: <br />
**LogicalName**: issendasallowed<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_LastAlertsViewedTime"></a> LastAlertsViewedTime

**Description**: Shows the last time when the traces were read from the database.<br />
**DisplayName**: <br />
**LogicalName**: lastalertsviewedtime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_LocaleId"></a> LocaleId

**Description**: Unique identifier of the user locale.<br />
**DisplayName**: <br />
**LogicalName**: localeid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Integer<br />
**Format**: Locale<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_LongDateFormatCode"></a> LongDateFormatCode

**Description**: Information that specifies how Long Date is displayed throughout Microsoft 365.<br />
**DisplayName**: <br />
**LogicalName**: longdateformatcode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_NegativeCurrencyFormatCode"></a> NegativeCurrencyFormatCode

**Description**: Information that specifies how negative currency numbers are displayed in Microsoft Dynamics 365.<br />
**DisplayName**: <br />
**LogicalName**: negativecurrencyformatcode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 15<br />
**MinValue**: 0


### <a name="BKMK_NegativeFormatCode"></a> NegativeFormatCode

**Description**: Information that specifies how negative numbers are displayed in Microsoft Dynamics 365.<br />
**DisplayName**: <br />
**LogicalName**: negativeformatcode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_NextTrackingNumber"></a> NextTrackingNumber

**Description**: Next tracking number.<br />
**DisplayName**: <br />
**LogicalName**: nexttrackingnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_NumberGroupFormat"></a> NumberGroupFormat

**Description**: Information that specifies how numbers are grouped in Microsoft Dynamics 365.<br />
**DisplayName**: <br />
**LogicalName**: numbergroupformat<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 25


### <a name="BKMK_NumberSeparator"></a> NumberSeparator

**Description**: Symbol used for number separation in Microsoft Dynamics 365.<br />
**DisplayName**: <br />
**LogicalName**: numberseparator<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 5


### <a name="BKMK_OfflineSyncInterval"></a> OfflineSyncInterval

**Description**: Normal polling frequency used for background offline synchronization in Microsoft Office Outlook.<br />
**DisplayName**: <br />
**LogicalName**: offlinesyncinterval<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_OutlookSyncInterval"></a> OutlookSyncInterval

**Description**: Normal polling frequency used for record synchronization in Microsoft Office Outlook.<br />
**DisplayName**: <br />
**LogicalName**: outlooksyncinterval<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_PagingLimit"></a> PagingLimit

**Description**: Information that specifies how many items to list on a page in list views.<br />
**DisplayName**: <br />
**LogicalName**: paginglimit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_PersonalizationSettings"></a> PersonalizationSettings

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: personalizationsettings<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_PMDesignator"></a> PMDesignator

**Description**: PM designator to use in Microsoft Dynamics 365.<br />
**DisplayName**: <br />
**LogicalName**: pmdesignator<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 25


### <a name="BKMK_PricingDecimalPrecision"></a> PricingDecimalPrecision

**Description**: Number of decimal places that can be used for prices.<br />
**DisplayName**: <br />
**LogicalName**: pricingdecimalprecision<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_ReportScriptErrors"></a> ReportScriptErrors

**Description**: Picklist for selecting the user preference for reporting scripting errors.<br />
**DisplayName**: Report Script Errors<br />
**LogicalName**: reportscripterrors<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Ask me for permission to send an error report to Microsoft
- **Value**: 2 **Label**: Automatically send an error report to Microsoft without asking me for permission
- **Value**: 3 **Label**: Never send an error report to Microsoft about Microsoft Dynamics 365



### <a name="BKMK_ResourceBookingExchangeSyncVersion"></a> ResourceBookingExchangeSyncVersion

**Description**: The version number for resource booking synchronization with Exchange.<br />
**DisplayName**: User resource booking synchronization version<br />
**LogicalName**: resourcebookingexchangesyncversion<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />


### <a name="BKMK_SelectedGlobalFilterId"></a> SelectedGlobalFilterId

**Description**: Store selected customer service hub dashboard saved filter id.<br />
**DisplayName**: <br />
**LogicalName**: selectedglobalfilterid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ShowWeekNumber"></a> ShowWeekNumber

**Description**: Information that specifies whether to display the week number in calendar displays in Microsoft Dynamics 365.<br />
**DisplayName**: <br />
**LogicalName**: showweeknumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_SplitViewState"></a> SplitViewState

**Description**: For Internal use only<br />
**DisplayName**: <br />
**LogicalName**: splitviewstate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Expanded
- **FalseOption Value**: 0 **Label**: Collapsed

**DefaultValue**: False


### <a name="BKMK_SyncContactCompany"></a> SyncContactCompany

**Description**: Indicates if the company field in Microsoft Office Outlook items are set during Outlook synchronization.<br />
**DisplayName**: <br />
**LogicalName**: synccontactcompany<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_SystemUserId"></a> SystemUserId

**Description**: Unique identifier of the user.<br />
**DisplayName**: <br />
**LogicalName**: systemuserid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_TimeFormatCode"></a> TimeFormatCode

**Description**: Information that specifies how the time is displayed in Microsoft Dynamics 365.<br />
**DisplayName**: <br />
**LogicalName**: timeformatcode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_TimeFormatString"></a> TimeFormatString

**Description**: Text for how time is displayed in Microsoft Dynamics 365.<br />
**DisplayName**: <br />
**LogicalName**: timeformatstring<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 255


### <a name="BKMK_TimeSeparator"></a> TimeSeparator

**Description**: Text for how time is displayed in Microsoft Dynamics 365.<br />
**DisplayName**: <br />
**LogicalName**: timeseparator<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 5


### <a name="BKMK_TimeZoneBias"></a> TimeZoneBias

**Description**: Local time zone adjustment for the user. System calculated based on the time zone selected.<br />
**DisplayName**: <br />
**LogicalName**: timezonebias<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_TimeZoneCode"></a> TimeZoneCode

**Description**: Local time zone for the user.<br />
**DisplayName**: <br />
**LogicalName**: timezonecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: <br />
**MinValue**: 


### <a name="BKMK_TimeZoneDaylightBias"></a> TimeZoneDaylightBias

**Description**: Local time zone daylight adjustment for the user. System calculated based on the time zone selected.<br />
**DisplayName**: <br />
**LogicalName**: timezonedaylightbias<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_TimeZoneDaylightDay"></a> TimeZoneDaylightDay

**Description**: Local time zone daylight day for the user. System calculated based on the time zone selected.<br />
**DisplayName**: <br />
**LogicalName**: timezonedaylightday<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: <br />
**MinValue**: 


### <a name="BKMK_TimeZoneDaylightDayOfWeek"></a> TimeZoneDaylightDayOfWeek

**Description**: Local time zone daylight day of week for the user. System calculated based on the time zone selected in Options.<br />
**DisplayName**: <br />
**LogicalName**: timezonedaylightdayofweek<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: <br />
**MinValue**: 


### <a name="BKMK_TimeZoneDaylightHour"></a> TimeZoneDaylightHour

**Description**: Local time zone daylight hour for the user. System calculated based on the time zone selected.<br />
**DisplayName**: <br />
**LogicalName**: timezonedaylighthour<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: <br />
**MinValue**: 


### <a name="BKMK_TimeZoneDaylightMinute"></a> TimeZoneDaylightMinute

**Description**: Local time zone daylight minute for the user. System calculated based on the time zone selected.<br />
**DisplayName**: <br />
**LogicalName**: timezonedaylightminute<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: <br />
**MinValue**: 


### <a name="BKMK_TimeZoneDaylightMonth"></a> TimeZoneDaylightMonth

**Description**: Local time zone daylight month for the user. System calculated based on the time zone selected.<br />
**DisplayName**: <br />
**LogicalName**: timezonedaylightmonth<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: <br />
**MinValue**: 


### <a name="BKMK_TimeZoneDaylightSecond"></a> TimeZoneDaylightSecond

**Description**: Local time zone daylight second for the user. System calculated based on the time zone selected.<br />
**DisplayName**: <br />
**LogicalName**: timezonedaylightsecond<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: <br />
**MinValue**: 


### <a name="BKMK_TimeZoneDaylightYear"></a> TimeZoneDaylightYear

**Description**: Local time zone daylight year for the user. System calculated based on the time zone selected.<br />
**DisplayName**: <br />
**LogicalName**: timezonedaylightyear<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: <br />
**MinValue**: 


### <a name="BKMK_TimeZoneStandardBias"></a> TimeZoneStandardBias

**Description**: Local time zone standard time bias for the user. System calculated based on the time zone selected.<br />
**DisplayName**: <br />
**LogicalName**: timezonestandardbias<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_TimeZoneStandardDay"></a> TimeZoneStandardDay

**Description**: Local time zone standard day for the user. System calculated based on the time zone selected.<br />
**DisplayName**: <br />
**LogicalName**: timezonestandardday<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: <br />
**MinValue**: 


### <a name="BKMK_TimeZoneStandardDayOfWeek"></a> TimeZoneStandardDayOfWeek

**Description**: Local time zone standard day of week for the user. System calculated based on the time zone selected.<br />
**DisplayName**: <br />
**LogicalName**: timezonestandarddayofweek<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: <br />
**MinValue**: 


### <a name="BKMK_TimeZoneStandardHour"></a> TimeZoneStandardHour

**Description**: Local time zone standard hour for the user. System calculated based on the time zone selected.<br />
**DisplayName**: <br />
**LogicalName**: timezonestandardhour<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: <br />
**MinValue**: 


### <a name="BKMK_TimeZoneStandardMinute"></a> TimeZoneStandardMinute

**Description**: Local time zone standard minute for the user. System calculated based on the time zone selected.<br />
**DisplayName**: <br />
**LogicalName**: timezonestandardminute<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: <br />
**MinValue**: 


### <a name="BKMK_TimeZoneStandardMonth"></a> TimeZoneStandardMonth

**Description**: Local time zone standard month for the user. System calculated based on the time zone selected.<br />
**DisplayName**: <br />
**LogicalName**: timezonestandardmonth<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: <br />
**MinValue**: 


### <a name="BKMK_TimeZoneStandardSecond"></a> TimeZoneStandardSecond

**Description**: Local time zone standard second for the user. System calculated based on the time zone selected.<br />
**DisplayName**: <br />
**LogicalName**: timezonestandardsecond<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: <br />
**MinValue**: 


### <a name="BKMK_TimeZoneStandardYear"></a> TimeZoneStandardYear

**Description**: Local time zone standard year for the user. System calculated based on the time zone selected.<br />
**DisplayName**: <br />
**LogicalName**: timezonestandardyear<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: <br />
**MinValue**: 


### <a name="BKMK_TrackingTokenId"></a> TrackingTokenId

**Description**: Tracking token ID.<br />
**DisplayName**: <br />
**LogicalName**: trackingtokenid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

**Description**: Unique identifier of the default currency of the user.<br />
**DisplayName**: Currency<br />
**LogicalName**: transactioncurrencyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: transactioncurrency


### <a name="BKMK_UILanguageId"></a> UILanguageId

**Description**: Unique identifier of the language in which to view the user interface (UI).<br />
**DisplayName**: <br />
**LogicalName**: uilanguageid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: Language<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_UseCrmFormForAppointment"></a> UseCrmFormForAppointment

**Description**: Indicates whether to use the Microsoft Dynamics 365 appointment form within Microsoft Office Outlook for creating new appointments.<br />
**DisplayName**: <br />
**LogicalName**: usecrmformforappointment<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_UseCrmFormForContact"></a> UseCrmFormForContact

**Description**: Indicates whether to use the Microsoft Dynamics 365 contact form within Microsoft Office Outlook for creating new contacts.<br />
**DisplayName**: <br />
**LogicalName**: usecrmformforcontact<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_UseCrmFormForEmail"></a> UseCrmFormForEmail

**Description**: Indicates whether to use the Microsoft Dynamics 365 email form within Microsoft Office Outlook for creating new emails.<br />
**DisplayName**: <br />
**LogicalName**: usecrmformforemail<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_UseCrmFormForTask"></a> UseCrmFormForTask

**Description**: Indicates whether to use the Microsoft Dynamics 365 task form within Microsoft Office Outlook for creating new tasks.<br />
**DisplayName**: <br />
**LogicalName**: usecrmformfortask<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_UseImageStrips"></a> UseImageStrips

**Description**: Indicates whether image strips are used to render images.<br />
**DisplayName**: <br />
**LogicalName**: useimagestrips<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_UserProfile"></a> UserProfile

**Description**: Specifies user profile ids in comma separated list.<br />
**DisplayName**: <br />
**LogicalName**: userprofile<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_VisualizationPaneLayout"></a> VisualizationPaneLayout

**Description**: The layout of the visualization pane.<br />
**DisplayName**: Visualization Pane Layout.<br />
**LogicalName**: visualizationpanelayout<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Top-bottom
- **Value**: 1 **Label**: Side-by-side



### <a name="BKMK_WorkdayStartTime"></a> WorkdayStartTime

**Description**: Workday start time for the user.<br />
**DisplayName**: <br />
**LogicalName**: workdaystarttime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 5


### <a name="BKMK_WorkdayStopTime"></a> WorkdayStopTime

**Description**: Workday stop time for the user.<br />
**DisplayName**: <br />
**LogicalName**: workdaystoptime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 5

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

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

**Description**: This attribute is no longer used. The data is now in the Mailbox.AllowEmailConnectorToUseCredentials attribute.<br />
**DisplayName**: <br />
**LogicalName**: allowemailcredentials<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_BusinessUnitIdName"></a> BusinessUnitIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: businessunitidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the user settings.<br />
**DisplayName**: <br />
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

**Description**: Date and time when the user settings object was created.<br />
**DisplayName**: <br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the usersettings.<br />
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


### <a name="BKMK_EmailPassword"></a> EmailPassword

**Description**: This attribute is no longer used. The data is now in the Mailbox.Password attribute.<br />
**DisplayName**: <br />
**LogicalName**: emailpassword<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_EmailUsername"></a> EmailUsername

**Description**: This attribute is no longer used. The data is now in the Mailbox.UserName attribute.<br />
**DisplayName**: <br />
**LogicalName**: emailusername<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the user settings.<br />
**DisplayName**: <br />
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

**Description**: Date and time when the user settings object was last modified.<br />
**DisplayName**: <br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the usersettings.<br />
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [transactioncurrency_usersettings](#BKMK_transactioncurrency_usersettings)
- [user_settings](#BKMK_user_settings)
- [lk_usersettingsbase_createdby](#BKMK_lk_usersettingsbase_createdby)
- [lk_usersettings_createdonbehalfby](#BKMK_lk_usersettings_createdonbehalfby)
- [lk_usersettingsbase_modifiedby](#BKMK_lk_usersettingsbase_modifiedby)
- [lk_usersettings_modifiedonbehalfby](#BKMK_lk_usersettings_modifiedonbehalfby)
- [business_unit_user_settings](#BKMK_business_unit_user_settings)


### <a name="BKMK_transactioncurrency_usersettings"></a> transactioncurrency_usersettings

See transactioncurrency Entity [transactioncurrency_usersettings](transactioncurrency.md#BKMK_transactioncurrency_usersettings) One-To-Many relationship.

### <a name="BKMK_user_settings"></a> user_settings

See systemuser Entity [user_settings](systemuser.md#BKMK_user_settings) One-To-Many relationship.

### <a name="BKMK_lk_usersettingsbase_createdby"></a> lk_usersettingsbase_createdby

See systemuser Entity [lk_usersettingsbase_createdby](systemuser.md#BKMK_lk_usersettingsbase_createdby) One-To-Many relationship.

### <a name="BKMK_lk_usersettings_createdonbehalfby"></a> lk_usersettings_createdonbehalfby

See systemuser Entity [lk_usersettings_createdonbehalfby](systemuser.md#BKMK_lk_usersettings_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_usersettingsbase_modifiedby"></a> lk_usersettingsbase_modifiedby

See systemuser Entity [lk_usersettingsbase_modifiedby](systemuser.md#BKMK_lk_usersettingsbase_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_usersettings_modifiedonbehalfby"></a> lk_usersettings_modifiedonbehalfby

See systemuser Entity [lk_usersettings_modifiedonbehalfby](systemuser.md#BKMK_lk_usersettings_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_business_unit_user_settings"></a> business_unit_user_settings

See businessunit Entity [business_unit_user_settings](businessunit.md#BKMK_business_unit_user_settings) One-To-Many relationship.
usersettings

