---
title: "User Settings (UserSettings) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the User Settings (UserSettings) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# User Settings (UserSettings) table/entity reference (Microsoft Dataverse)

User's preferred settings.

## Messages

The following table lists the messages for the User Settings (UserSettings) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /usersettingscollection(*systemuserid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /usersettingscollection<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /usersettingscollection(*systemuserid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|

## Properties

The following table lists selected properties for the User Settings (UserSettings) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **User Settings** |
| **DisplayCollectionName** | **User Settings** |
| **SchemaName** | `UserSettings` |
| **CollectionSchemaName** | `UserSettingses` |
| **EntitySetName** | `usersettingscollection`|
| **LogicalName** | `usersettings` |
| **LogicalCollectionName** | `usersettingses` |
| **PrimaryIdAttribute** | `systemuserid` |
| **TableType** | `Standard` |
| **OwnershipType** | `BusinessOwned` |

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
- [D365AutoInstallAttemptStatus](#BKMK_D365AutoInstallAttemptStatus)
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
- [LastModifiedTimeForViewPersonalizationSettings](#BKMK_LastModifiedTimeForViewPersonalizationSettings)
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
- [PreferredSolution](#BKMK_PreferredSolution)
- [PricingDecimalPrecision](#BKMK_PricingDecimalPrecision)
- [ReleaseChannel](#BKMK_ReleaseChannel)
- [ReportScriptErrors](#BKMK_ReportScriptErrors)
- [ResourceBookingExchangeSyncVersion](#BKMK_ResourceBookingExchangeSyncVersion)
- [SelectedGlobalFilterId](#BKMK_SelectedGlobalFilterId)
- [ShowWeekNumber](#BKMK_ShowWeekNumber)
- [SplitViewState](#BKMK_SplitViewState)
- [SyncContactCompany](#BKMK_SyncContactCompany)
- [SystemUserId](#BKMK_SystemUserId)
- [TableScopedDVSearchFeatureTeachingBubbleViews](#BKMK_TableScopedDVSearchFeatureTeachingBubbleViews)
- [TableScopedDVSearchQuickFindTeachingBubbleViews](#BKMK_TableScopedDVSearchQuickFindTeachingBubbleViews)
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
- [TryToggleSets](#BKMK_TryToggleSets)
- [TryToggleStatus](#BKMK_TryToggleStatus)
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
|---|---|
|Description|**Normal polling frequency used for address book synchronization in Microsoft Office Outlook.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`addressbooksyncinterval`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_AdvancedFindStartupMode"></a> AdvancedFindStartupMode

|Property|Value|
|---|---|
|Description|**Default mode, such as simple or detailed, for advanced find.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`advancedfindstartupmode`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_AMDesignator"></a> AMDesignator

|Property|Value|
|---|---|
|Description|**AM designator to use in Microsoft Dynamics 365.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`amdesignator`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|25|

### <a name="BKMK_AutoCaptureUserStatus"></a> AutoCaptureUserStatus

|Property|Value|
|---|---|
|Description|**Set user status for ADC Suggestions**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`autocaptureuserstatus`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_AutoCreateContactOnPromote"></a> AutoCreateContactOnPromote

|Property|Value|
|---|---|
|Description|**Auto-create contact on client promote**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`autocreatecontactonpromote`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

|Property|Value|
|---|---|
|Description|**Unique identifier of the business unit with which the user is associated.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`businessunitid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_CalendarType"></a> CalendarType

|Property|Value|
|---|---|
|Description|**Calendar type for the system. Set to Gregorian US by default.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`calendartype`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_CurrencyDecimalPrecision"></a> CurrencyDecimalPrecision

|Property|Value|
|---|---|
|Description|**Number of decimal places that can be used for currency.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`currencydecimalprecision`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_CurrencyFormatCode"></a> CurrencyFormatCode

|Property|Value|
|---|---|
|Description|**Information about how currency symbols are placed in Microsoft Dynamics 365.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`currencyformatcode`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_CurrencySymbol"></a> CurrencySymbol

|Property|Value|
|---|---|
|Description|**Symbol used for currency in Microsoft Dynamics 365.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`currencysymbol`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|13|

### <a name="BKMK_D365AutoInstallAttemptStatus"></a> D365AutoInstallAttemptStatus

|Property|Value|
|---|---|
|Description|**Determines the status of auto install of Dynamics 365 to Teams attempt has been completed**|
|DisplayName|**d365autoinstallattemptstatus**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`d365autoinstallattemptstatus`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`usersettings_d365autoinstallattemptstatus`|

#### D365AutoInstallAttemptStatus Choices/Options

|Value|Label|
|---|---|
|0|**Not attempted**|
|1|**Auto installed**|
|2|**Already installed**|
|3|**Teams admin blocked**|
|4|**Unauthorized**|
|5|**No Solution**|
|6|**No Graph API**|
|7|**Resource Disabled**|

### <a name="BKMK_DataValidationModeForExportToExcel"></a> DataValidationModeForExportToExcel

|Property|Value|
|---|---|
|Description|**Information that specifies the level of data validation in excel worksheets exported in a format suitable for import.**|
|DisplayName|**Data Validation Mode For Export To Excel**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`datavalidationmodeforexporttoexcel`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`usersettings_datavalidationmodeforexporttoexcel`|

#### DataValidationModeForExportToExcel Choices/Options

|Value|Label|
|---|---|
|0|**Full**|
|1|**None**|

### <a name="BKMK_DateFormatCode"></a> DateFormatCode

|Property|Value|
|---|---|
|Description|**Information about how the date is displayed in Microsoft Dynamics 365.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`dateformatcode`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_DateFormatString"></a> DateFormatString

|Property|Value|
|---|---|
|Description|**String showing how the date is displayed throughout Microsoft 365.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`dateformatstring`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|255|

### <a name="BKMK_DateSeparator"></a> DateSeparator

|Property|Value|
|---|---|
|Description|**Character used to separate the month, the day, and the year in dates in Microsoft Dynamics 365.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`dateseparator`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5|

### <a name="BKMK_DecimalSymbol"></a> DecimalSymbol

|Property|Value|
|---|---|
|Description|**Symbol used for decimal in Microsoft Dynamics 365.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`decimalsymbol`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5|

### <a name="BKMK_DefaultCalendarView"></a> DefaultCalendarView

|Property|Value|
|---|---|
|Description|**Default calendar view for the user.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`defaultcalendarview`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_DefaultCountryCode"></a> DefaultCountryCode

|Property|Value|
|---|---|
|Description|**Text area to enter default country code.**|
|DisplayName|**Default Country Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`defaultcountrycode`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|30|

### <a name="BKMK_DefaultDashboardId"></a> DefaultDashboardId

|Property|Value|
|---|---|
|Description|**Unique identifier of the default dashboard.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`defaultdashboardid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_DefaultSearchExperience"></a> DefaultSearchExperience

|Property|Value|
|---|---|
|Description|**Default search experience for the user.**|
|DisplayName|**Default Search Experience**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`defaultsearchexperience`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|2|
|GlobalChoiceName|`usersettings_defaultsearchexperience`|

#### DefaultSearchExperience Choices/Options

|Value|Label|
|---|---|
|0|**Relevance search**|
|1|**Categorized search**|
|2|**Use last search**|
|3|**Custom search**|

### <a name="BKMK_EntityFormMode"></a> EntityFormMode

|Property|Value|
|---|---|
|Description|**Indicates the form mode to be used.**|
|DisplayName|**Form Mode**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityformmode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`usersettings_entityformmode`|

#### EntityFormMode Choices/Options

|Value|Label|
|---|---|
|0|**Organization default**|
|1|**Read-optimized**|
|2|**Edit**|

### <a name="BKMK_FullNameConventionCode"></a> FullNameConventionCode

|Property|Value|
|---|---|
|Description|**Order in which names are to be displayed in Microsoft Dynamics 365.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fullnameconventioncode`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_GetStartedPaneContentEnabled"></a> GetStartedPaneContentEnabled

|Property|Value|
|---|---|
|Description|**Information that specifies whether the Get Started pane in lists is enabled.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`getstartedpanecontentenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`usersettings_getstartedpanecontentenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_HelpLanguageId"></a> HelpLanguageId

|Property|Value|
|---|---|
|Description|**Unique identifier of the Help language.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`helplanguageid`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_HomepageArea"></a> HomepageArea

|Property|Value|
|---|---|
|Description|**Web site home page for the user.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`homepagearea`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_HomepageLayout"></a> HomepageLayout

|Property|Value|
|---|---|
|Description|**Configuration of the home page layout.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`homepagelayout`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_HomepageSubarea"></a> HomepageSubarea

|Property|Value|
|---|---|
|Description|**Web site page for the user.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`homepagesubarea`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_IgnoreUnsolicitedEmail"></a> IgnoreUnsolicitedEmail

|Property|Value|
|---|---|
|Description|**Information that specifies whether a user account is to ignore unsolicited email (deprecated).**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ignoreunsolicitedemail`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`usersettings_ignoreunsolicitedemail`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IncomingEmailFilteringMethod"></a> IncomingEmailFilteringMethod

|Property|Value|
|---|---|
|Description|**Incoming email filtering method.**|
|DisplayName|**Incoming Email Filtering Method**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`incomingemailfilteringmethod`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|2|
|GlobalChoiceName|`usersettings_incomingemailfilteringmethod`|

#### IncomingEmailFilteringMethod Choices/Options

|Value|Label|
|---|---|
|0|**All email messages**|
|1|**Email messages in response to Dynamics 365 email**|
|2|**Email messages from Dynamics 365 Leads, Contacts and Accounts**|
|3|**Email messages from Dynamics 365 records that are email enabled**|
|4|**No email messages**|

### <a name="BKMK_IsAppsForCrmAlertDismissed"></a> IsAppsForCrmAlertDismissed

|Property|Value|
|---|---|
|Description|**Show or dismiss alert for Apps for 365.**|
|DisplayName|**Show alert for Apps for 365.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isappsforcrmalertdismissed`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`usersettings_isappsforcrmalertdismissed`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsAutoDataCaptureEnabled"></a> IsAutoDataCaptureEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether to use the Auto Capture feature enabled or not.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isautodatacaptureenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`usersettings_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsDefaultCountryCodeCheckEnabled"></a> IsDefaultCountryCodeCheckEnabled

|Property|Value|
|---|---|
|Description|**Enable or disable country code selection .**|
|DisplayName|**Enable Default Country Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isdefaultcountrycodecheckenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`user_iscountrycodeselectionenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsDuplicateDetectionEnabledWhenGoingOnline"></a> IsDuplicateDetectionEnabledWhenGoingOnline

|Property|Value|
|---|---|
|Description|**Indicates if duplicate detection is enabled when going online.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isduplicatedetectionenabledwhengoingonline`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`usersettings_isduplicatedetectionenabledwhengoingonline`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsEmailConversationViewEnabled"></a> IsEmailConversationViewEnabled

|Property|Value|
|---|---|
|Description|**Enable or disable email conversation view on timeline wall selection.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isemailconversationviewenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`usersettings_isemailconversationviewenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsGuidedHelpEnabled"></a> IsGuidedHelpEnabled

|Property|Value|
|---|---|
|Description|**Enable or disable guided help.**|
|DisplayName|**Enable Default Guided Help**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isguidedhelpenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`usersettings_isguidedhelpenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsResourceBookingExchangeSyncEnabled"></a> IsResourceBookingExchangeSyncEnabled

|Property|Value|
|---|---|
|Description|**Indicates if the synchronization of user resource booking with Exchange is enabled at user level.**|
|DisplayName|**Resource booking synchronization enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isresourcebookingexchangesyncenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`usersettings_isresourcebookingexchangesyncenabled`|
|DefaultValue|False|
|True Label|Enabled|
|False Label|Disabled|

### <a name="BKMK_IsSendAsAllowed"></a> IsSendAsAllowed

|Property|Value|
|---|---|
|Description|**Indicates if send as other user privilege is enabled or not.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`issendasallowed`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`usersettings_issendasallowed`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_LastAlertsViewedTime"></a> LastAlertsViewedTime

|Property|Value|
|---|---|
|Description|**Shows the last time when the traces were read from the database.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastalertsviewedtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_LastModifiedTimeForViewPersonalizationSettings"></a> LastModifiedTimeForViewPersonalizationSettings

|Property|Value|
|---|---|
|Description|**Stores the timestamp for when the ViewPersonalizationSettings attribute was updated for this user in the UserEntityUISettings table.**|
|DisplayName|**Last modified timestamp for the view personalization settings in UserEntityUISettings table**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastmodifiedtimeforviewpersonalizationsettings`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_LocaleId"></a> LocaleId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user locale.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`localeid`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_LongDateFormatCode"></a> LongDateFormatCode

|Property|Value|
|---|---|
|Description|**Information that specifies how Long Date is displayed throughout Microsoft 365.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`longdateformatcode`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_NegativeCurrencyFormatCode"></a> NegativeCurrencyFormatCode

|Property|Value|
|---|---|
|Description|**Information that specifies how negative currency numbers are displayed in Microsoft Dynamics 365.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`negativecurrencyformatcode`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|15|
|MinValue|0|

### <a name="BKMK_NegativeFormatCode"></a> NegativeFormatCode

|Property|Value|
|---|---|
|Description|**Information that specifies how negative numbers are displayed in Microsoft Dynamics 365.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`negativeformatcode`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_NextTrackingNumber"></a> NextTrackingNumber

|Property|Value|
|---|---|
|Description|**Next tracking number.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`nexttrackingnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_NumberGroupFormat"></a> NumberGroupFormat

|Property|Value|
|---|---|
|Description|**Information that specifies how numbers are grouped in Microsoft Dynamics 365.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`numbergroupformat`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|25|

### <a name="BKMK_NumberSeparator"></a> NumberSeparator

|Property|Value|
|---|---|
|Description|**Symbol used for number separation in Microsoft Dynamics 365.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`numberseparator`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5|

### <a name="BKMK_OfflineSyncInterval"></a> OfflineSyncInterval

|Property|Value|
|---|---|
|Description|**Normal polling frequency used for background offline synchronization in Microsoft Office Outlook.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`offlinesyncinterval`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_OutlookSyncInterval"></a> OutlookSyncInterval

|Property|Value|
|---|---|
|Description|**Normal polling frequency used for record synchronization in Microsoft Office Outlook.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`outlooksyncinterval`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_PagingLimit"></a> PagingLimit

|Property|Value|
|---|---|
|Description|**Information that specifies how many items to list on a page in list views.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`paginglimit`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_PersonalizationSettings"></a> PersonalizationSettings

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`personalizationsettings`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_PMDesignator"></a> PMDesignator

|Property|Value|
|---|---|
|Description|**PM designator to use in Microsoft Dynamics 365.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`pmdesignator`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|25|

### <a name="BKMK_PreferredSolution"></a> PreferredSolution

|Property|Value|
|---|---|
|Description|**Preferred Solution when create a component without under a solution in this organization**|
|DisplayName|**Preferred Solution**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`preferredsolution`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|solution|

### <a name="BKMK_PricingDecimalPrecision"></a> PricingDecimalPrecision

|Property|Value|
|---|---|
|Description|**Number of decimal places that can be used for prices.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`pricingdecimalprecision`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_ReleaseChannel"></a> ReleaseChannel

|Property|Value|
|---|---|
|Description|**Model app channel override**|
|DisplayName|**Model app channel override**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`releasechannel`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`usersettings_releasechannel`|

#### ReleaseChannel Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Semi-annual channel override**|
|2|**Monthly channel override**|
|3|**Inner channel override**|

### <a name="BKMK_ReportScriptErrors"></a> ReportScriptErrors

|Property|Value|
|---|---|
|Description|**Picklist for selecting the user preference for reporting scripting errors.**|
|DisplayName|**Report Script Errors**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`reportscripterrors`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`usersettings_reportscripterrors`|

#### ReportScriptErrors Choices/Options

|Value|Label|
|---|---|
|1|**Ask me for permission to send an error report to Microsoft**|
|2|**Automatically send an error report to Microsoft without asking me for permission**|
|3|**Never send an error report to Microsoft about Microsoft Dynamics 365**|

### <a name="BKMK_ResourceBookingExchangeSyncVersion"></a> ResourceBookingExchangeSyncVersion

|Property|Value|
|---|---|
|Description|**The version number for resource booking synchronization with Exchange.**|
|DisplayName|**User resource booking synchronization version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`resourcebookingexchangesyncversion`|
|RequiredLevel|SystemRequired|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_SelectedGlobalFilterId"></a> SelectedGlobalFilterId

|Property|Value|
|---|---|
|Description|**Store selected customer service hub dashboard saved filter id.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`selectedglobalfilterid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ShowWeekNumber"></a> ShowWeekNumber

|Property|Value|
|---|---|
|Description|**Information that specifies whether to display the week number in calendar displays in Microsoft Dynamics 365.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`showweeknumber`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`usersettings_showweeknumber`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_SplitViewState"></a> SplitViewState

|Property|Value|
|---|---|
|Description|**For Internal use only**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`splitviewstate`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`usersettings_splitviewstate`|
|DefaultValue|False|
|True Label|Expanded|
|False Label|Collapsed|

### <a name="BKMK_SyncContactCompany"></a> SyncContactCompany

|Property|Value|
|---|---|
|Description|**Indicates if the company field in Microsoft Office Outlook items are set during Outlook synchronization.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`synccontactcompany`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`usersettings_synccontactcompany`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_SystemUserId"></a> SystemUserId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`systemuserid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_TableScopedDVSearchFeatureTeachingBubbleViews"></a> TableScopedDVSearchFeatureTeachingBubbleViews

|Property|Value|
|---|---|
|Description|**The number of times a user has interacted with the Tabled Scoped Dataverse Search feature teaching bubble.**|
|DisplayName|**Table Scoped Dataverse Search Feature Teaching Bubble Views**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`tablescopeddvsearchfeatureteachingbubbleviews`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|100|
|MinValue|0|

### <a name="BKMK_TableScopedDVSearchQuickFindTeachingBubbleViews"></a> TableScopedDVSearchQuickFindTeachingBubbleViews

|Property|Value|
|---|---|
|Description|**The number of times a user has interacted with the Tabled Scoped Dataverse Search Quick Find teaching bubble.**|
|DisplayName|**Table Scoped Dataverse Search Quick Find Teaching Bubble Views**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`tablescopeddvsearchquickfindteachingbubbleviews`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|100|
|MinValue|0|

### <a name="BKMK_TimeFormatCode"></a> TimeFormatCode

|Property|Value|
|---|---|
|Description|**Information that specifies how the time is displayed in Microsoft Dynamics 365.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timeformatcode`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_TimeFormatString"></a> TimeFormatString

|Property|Value|
|---|---|
|Description|**Text for how time is displayed in Microsoft Dynamics 365.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timeformatstring`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|255|

### <a name="BKMK_TimeSeparator"></a> TimeSeparator

|Property|Value|
|---|---|
|Description|**Text for how time is displayed in Microsoft Dynamics 365.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timeseparator`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5|

### <a name="BKMK_TimeZoneBias"></a> TimeZoneBias

|Property|Value|
|---|---|
|Description|**Local time zone adjustment for the user. System calculated based on the time zone selected.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonebias`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_TimeZoneCode"></a> TimeZoneCode

|Property|Value|
|---|---|
|Description|**Local time zone for the user.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonecode`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_TimeZoneDaylightBias"></a> TimeZoneDaylightBias

|Property|Value|
|---|---|
|Description|**Local time zone daylight adjustment for the user. System calculated based on the time zone selected.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonedaylightbias`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_TimeZoneDaylightDay"></a> TimeZoneDaylightDay

|Property|Value|
|---|---|
|Description|**Local time zone daylight day for the user. System calculated based on the time zone selected.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonedaylightday`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_TimeZoneDaylightDayOfWeek"></a> TimeZoneDaylightDayOfWeek

|Property|Value|
|---|---|
|Description|**Local time zone daylight day of week for the user. System calculated based on the time zone selected in Options.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonedaylightdayofweek`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_TimeZoneDaylightHour"></a> TimeZoneDaylightHour

|Property|Value|
|---|---|
|Description|**Local time zone daylight hour for the user. System calculated based on the time zone selected.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonedaylighthour`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_TimeZoneDaylightMinute"></a> TimeZoneDaylightMinute

|Property|Value|
|---|---|
|Description|**Local time zone daylight minute for the user. System calculated based on the time zone selected.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonedaylightminute`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_TimeZoneDaylightMonth"></a> TimeZoneDaylightMonth

|Property|Value|
|---|---|
|Description|**Local time zone daylight month for the user. System calculated based on the time zone selected.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonedaylightmonth`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_TimeZoneDaylightSecond"></a> TimeZoneDaylightSecond

|Property|Value|
|---|---|
|Description|**Local time zone daylight second for the user. System calculated based on the time zone selected.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonedaylightsecond`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_TimeZoneDaylightYear"></a> TimeZoneDaylightYear

|Property|Value|
|---|---|
|Description|**Local time zone daylight year for the user. System calculated based on the time zone selected.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonedaylightyear`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_TimeZoneStandardBias"></a> TimeZoneStandardBias

|Property|Value|
|---|---|
|Description|**Local time zone standard time bias for the user. System calculated based on the time zone selected.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonestandardbias`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_TimeZoneStandardDay"></a> TimeZoneStandardDay

|Property|Value|
|---|---|
|Description|**Local time zone standard day for the user. System calculated based on the time zone selected.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonestandardday`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_TimeZoneStandardDayOfWeek"></a> TimeZoneStandardDayOfWeek

|Property|Value|
|---|---|
|Description|**Local time zone standard day of week for the user. System calculated based on the time zone selected.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonestandarddayofweek`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_TimeZoneStandardHour"></a> TimeZoneStandardHour

|Property|Value|
|---|---|
|Description|**Local time zone standard hour for the user. System calculated based on the time zone selected.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonestandardhour`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_TimeZoneStandardMinute"></a> TimeZoneStandardMinute

|Property|Value|
|---|---|
|Description|**Local time zone standard minute for the user. System calculated based on the time zone selected.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonestandardminute`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_TimeZoneStandardMonth"></a> TimeZoneStandardMonth

|Property|Value|
|---|---|
|Description|**Local time zone standard month for the user. System calculated based on the time zone selected.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonestandardmonth`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_TimeZoneStandardSecond"></a> TimeZoneStandardSecond

|Property|Value|
|---|---|
|Description|**Local time zone standard second for the user. System calculated based on the time zone selected.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonestandardsecond`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_TimeZoneStandardYear"></a> TimeZoneStandardYear

|Property|Value|
|---|---|
|Description|**Local time zone standard year for the user. System calculated based on the time zone selected.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonestandardyear`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_TrackingTokenId"></a> TrackingTokenId

|Property|Value|
|---|---|
|Description|**Tracking token ID.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`trackingtokenid`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Unique identifier of the default currency of the user.**|
|DisplayName|**Currency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`transactioncurrencyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|transactioncurrency|

### <a name="BKMK_TryToggleSets"></a> TryToggleSets

|Property|Value|
|---|---|
|Description|**The list of app modules with try toggle sets**|
|DisplayName|**TryToggleSets**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`trytogglesets`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_TryToggleStatus"></a> TryToggleStatus

|Property|Value|
|---|---|
|Description|**Enable or disable try toggle status.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`trytogglestatus`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`usersettings_trytogglestatus`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_UILanguageId"></a> UILanguageId

|Property|Value|
|---|---|
|Description|**Unique identifier of the language in which to view the user interface (UI).**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`uilanguageid`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_UseCrmFormForAppointment"></a> UseCrmFormForAppointment

|Property|Value|
|---|---|
|Description|**Indicates whether to use the Microsoft Dynamics 365 appointment form within Microsoft Office Outlook for creating new appointments.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`usecrmformforappointment`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`usersettings_usecrmformforappointment`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_UseCrmFormForContact"></a> UseCrmFormForContact

|Property|Value|
|---|---|
|Description|**Indicates whether to use the Microsoft Dynamics 365 contact form within Microsoft Office Outlook for creating new contacts.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`usecrmformforcontact`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`usersettings_usecrmformforcontact`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_UseCrmFormForEmail"></a> UseCrmFormForEmail

|Property|Value|
|---|---|
|Description|**Indicates whether to use the Microsoft Dynamics 365 email form within Microsoft Office Outlook for creating new emails.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`usecrmformforemail`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`usersettings_usecrmformforemail`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_UseCrmFormForTask"></a> UseCrmFormForTask

|Property|Value|
|---|---|
|Description|**Indicates whether to use the Microsoft Dynamics 365 task form within Microsoft Office Outlook for creating new tasks.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`usecrmformfortask`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`usersettings_usecrmformfortask`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_UseImageStrips"></a> UseImageStrips

|Property|Value|
|---|---|
|Description|**Indicates whether image strips are used to render images.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`useimagestrips`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`usersettings_useimagestrips`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_UserProfile"></a> UserProfile

|Property|Value|
|---|---|
|Description|**Specifies user profile ids in comma separated list.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`userprofile`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_VisualizationPaneLayout"></a> VisualizationPaneLayout

|Property|Value|
|---|---|
|Description|**The layout of the visualization pane.**|
|DisplayName|**Visualization Pane Layout.**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`visualizationpanelayout`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`usersettings_visualizationpanelayout`|

#### VisualizationPaneLayout Choices/Options

|Value|Label|
|---|---|
|0|**Top-bottom**|
|1|**Side-by-side**|

### <a name="BKMK_WorkdayStartTime"></a> WorkdayStartTime

|Property|Value|
|---|---|
|Description|**Workday start time for the user.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`workdaystarttime`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5|

### <a name="BKMK_WorkdayStopTime"></a> WorkdayStopTime

|Property|Value|
|---|---|
|Description|**Workday stop time for the user.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`workdaystoptime`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [AllowEmailCredentials](#BKMK_AllowEmailCredentials)
- [BusinessUnitIdName](#BKMK_BusinessUnitIdName)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [EmailPassword](#BKMK_EmailPassword)
- [EmailUsername](#BKMK_EmailUsername)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_AllowEmailCredentials"></a> AllowEmailCredentials

|Property|Value|
|---|---|
|Description|**This attribute is no longer used. The data is now in the Mailbox.AllowEmailConnectorToUseCredentials attribute.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowemailcredentials`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`usersettings_allowemailcredentials`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_BusinessUnitIdName"></a> BusinessUnitIdName

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`businessunitidname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the user settings.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the user settings object was created.**|
|DisplayName||
|IsValidForForm|False|
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
|Description|**Unique identifier of the delegate user who created the usersettings.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_EmailPassword"></a> EmailPassword

|Property|Value|
|---|---|
|Description|**This attribute is no longer used. The data is now in the Mailbox.Password attribute.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`emailpassword`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_EmailUsername"></a> EmailUsername

|Property|Value|
|---|---|
|Description|**This attribute is no longer used. The data is now in the Mailbox.UserName attribute.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`emailusername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the user settings.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the user settings object was last modified.**|
|DisplayName||
|IsValidForForm|False|
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
|Description|**Unique identifier of the delegate user who last modified the usersettings.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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

- [business_unit_user_settings](#BKMK_business_unit_user_settings)
- [lk_usersettings_createdonbehalfby](#BKMK_lk_usersettings_createdonbehalfby)
- [lk_usersettings_modifiedonbehalfby](#BKMK_lk_usersettings_modifiedonbehalfby)
- [lk_usersettingsbase_createdby](#BKMK_lk_usersettingsbase_createdby)
- [lk_usersettingsbase_modifiedby](#BKMK_lk_usersettingsbase_modifiedby)
- [transactioncurrency_usersettings](#BKMK_transactioncurrency_usersettings)
- [user_settings](#BKMK_user_settings)
- [user_settings_preferred_solution](#BKMK_user_settings_preferred_solution)

### <a name="BKMK_business_unit_user_settings"></a> business_unit_user_settings

One-To-Many Relationship: [businessunit business_unit_user_settings](businessunit.md#BKMK_business_unit_user_settings)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`businessunitid`|
|ReferencingEntityNavigationPropertyName|`businessunitid_businessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_usersettings_createdonbehalfby"></a> lk_usersettings_createdonbehalfby

One-To-Many Relationship: [systemuser lk_usersettings_createdonbehalfby](systemuser.md#BKMK_lk_usersettings_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_usersettings_modifiedonbehalfby"></a> lk_usersettings_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_usersettings_modifiedonbehalfby](systemuser.md#BKMK_lk_usersettings_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_usersettingsbase_createdby"></a> lk_usersettingsbase_createdby

One-To-Many Relationship: [systemuser lk_usersettingsbase_createdby](systemuser.md#BKMK_lk_usersettingsbase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_usersettingsbase_modifiedby"></a> lk_usersettingsbase_modifiedby

One-To-Many Relationship: [systemuser lk_usersettingsbase_modifiedby](systemuser.md#BKMK_lk_usersettingsbase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_transactioncurrency_usersettings"></a> transactioncurrency_usersettings

One-To-Many Relationship: [transactioncurrency transactioncurrency_usersettings](transactioncurrency.md#BKMK_transactioncurrency_usersettings)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencingEntityNavigationPropertyName|`transactioncurrencyid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_settings"></a> user_settings

One-To-Many Relationship: [systemuser user_settings](systemuser.md#BKMK_user_settings)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`systemuserid`|
|ReferencingEntityNavigationPropertyName|`systemuserid_systemuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_settings_preferred_solution"></a> user_settings_preferred_solution

One-To-Many Relationship: [solution user_settings_preferred_solution](solution.md#BKMK_user_settings_preferred_solution)

|Property|Value|
|---|---|
|ReferencedEntity|`solution`|
|ReferencedAttribute|`solutionid`|
|ReferencingAttribute|`preferredsolution`|
|ReferencingEntityNavigationPropertyName|`preferredsolution`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.usersettings?displayProperty=fullName>
