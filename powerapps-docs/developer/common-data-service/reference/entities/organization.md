---
title: "Organization Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the Organization entity."

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
# Organization Entity Reference

Top level of the Microsoft Dynamics 365 business hierarchy. The organization can be a specific business, holding company, or corporation.

## Entity Properties

**DisplayName**: Organization<br />
**DisplayCollectionName**: Organizations<br />
**SchemaName**: Organization<br />
**CollectionSchemaName**: Organizations<br />
**LogicalName**: organization<br />
**LogicalCollectionName**: organizations<br />
**EntitySetName**: organizations<br />
**PrimaryIdAttribute**: organizationid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ACIWebEndpointUrl](#BKMK_ACIWebEndpointUrl)
- [AcknowledgementTemplateId](#BKMK_AcknowledgementTemplateId)
- [AllowAddressBookSyncs](#BKMK_AllowAddressBookSyncs)
- [AllowAutoResponseCreation](#BKMK_AllowAutoResponseCreation)
- [AllowAutoUnsubscribe](#BKMK_AllowAutoUnsubscribe)
- [AllowAutoUnsubscribeAcknowledgement](#BKMK_AllowAutoUnsubscribeAcknowledgement)
- [AllowClientMessageBarAd](#BKMK_AllowClientMessageBarAd)
- [AllowEntityOnlyAudit](#BKMK_AllowEntityOnlyAudit)
- [AllowMarketingEmailExecution](#BKMK_AllowMarketingEmailExecution)
- [AllowOfflineScheduledSyncs](#BKMK_AllowOfflineScheduledSyncs)
- [AllowOutlookScheduledSyncs](#BKMK_AllowOutlookScheduledSyncs)
- [AllowUnresolvedPartiesOnEmailSend](#BKMK_AllowUnresolvedPartiesOnEmailSend)
- [AllowUserFormModePreference](#BKMK_AllowUserFormModePreference)
- [AllowUsersSeeAppdownloadMessage](#BKMK_AllowUsersSeeAppdownloadMessage)
- [AllowWebExcelExport](#BKMK_AllowWebExcelExport)
- [AMDesignator](#BKMK_AMDesignator)
- [AppDesignerExperienceEnabled](#BKMK_AppDesignerExperienceEnabled)
- [AutoApplyDefaultonCaseCreate](#BKMK_AutoApplyDefaultonCaseCreate)
- [AutoApplyDefaultonCaseUpdate](#BKMK_AutoApplyDefaultonCaseUpdate)
- [AutoApplySLA](#BKMK_AutoApplySLA)
- [AzureSchedulerJobCollectionName](#BKMK_AzureSchedulerJobCollectionName)
- [BaseCurrencyId](#BKMK_BaseCurrencyId)
- [BingMapsApiKey](#BKMK_BingMapsApiKey)
- [BlockedAttachments](#BKMK_BlockedAttachments)
- [BoundDashboardDefaultCardExpanded](#BKMK_BoundDashboardDefaultCardExpanded)
- [BulkOperationPrefix](#BKMK_BulkOperationPrefix)
- [BusinessClosureCalendarId](#BKMK_BusinessClosureCalendarId)
- [CalendarType](#BKMK_CalendarType)
- [CampaignPrefix](#BKMK_CampaignPrefix)
- [CascadeStatusUpdate](#BKMK_CascadeStatusUpdate)
- [CasePrefix](#BKMK_CasePrefix)
- [CategoryPrefix](#BKMK_CategoryPrefix)
- [ClientFeatureSet](#BKMK_ClientFeatureSet)
- [ContractPrefix](#BKMK_ContractPrefix)
- [CortanaProactiveExperienceEnabled](#BKMK_CortanaProactiveExperienceEnabled)
- [CreateProductsWithoutParentInActiveState](#BKMK_CreateProductsWithoutParentInActiveState)
- [CurrencyDecimalPrecision](#BKMK_CurrencyDecimalPrecision)
- [CurrencyDisplayOption](#BKMK_CurrencyDisplayOption)
- [CurrencyFormatCode](#BKMK_CurrencyFormatCode)
- [CurrencySymbol](#BKMK_CurrencySymbol)
- [CurrentBulkOperationNumber](#BKMK_CurrentBulkOperationNumber)
- [CurrentCampaignNumber](#BKMK_CurrentCampaignNumber)
- [CurrentCaseNumber](#BKMK_CurrentCaseNumber)
- [CurrentCategoryNumber](#BKMK_CurrentCategoryNumber)
- [CurrentContractNumber](#BKMK_CurrentContractNumber)
- [CurrentInvoiceNumber](#BKMK_CurrentInvoiceNumber)
- [CurrentKaNumber](#BKMK_CurrentKaNumber)
- [CurrentKbNumber](#BKMK_CurrentKbNumber)
- [CurrentOrderNumber](#BKMK_CurrentOrderNumber)
- [CurrentQuoteNumber](#BKMK_CurrentQuoteNumber)
- [DateFormatCode](#BKMK_DateFormatCode)
- [DateFormatString](#BKMK_DateFormatString)
- [DateSeparator](#BKMK_DateSeparator)
- [DecimalSymbol](#BKMK_DecimalSymbol)
- [DefaultCountryCode](#BKMK_DefaultCountryCode)
- [DefaultCrmCustomName](#BKMK_DefaultCrmCustomName)
- [DefaultEmailServerProfileId](#BKMK_DefaultEmailServerProfileId)
- [DefaultEmailSettings](#BKMK_DefaultEmailSettings)
- [DefaultMobileOfflineProfileId](#BKMK_DefaultMobileOfflineProfileId)
- [DefaultRecurrenceEndRangeType](#BKMK_DefaultRecurrenceEndRangeType)
- [DefaultThemeData](#BKMK_DefaultThemeData)
- [DelegatedAdminUserId](#BKMK_DelegatedAdminUserId)
- [DisableSocialCare](#BKMK_DisableSocialCare)
- [DiscountCalculationMethod](#BKMK_DiscountCalculationMethod)
- [DisplayNavigationTour](#BKMK_DisplayNavigationTour)
- [EmailConnectionChannel](#BKMK_EmailConnectionChannel)
- [EmailCorrelationEnabled](#BKMK_EmailCorrelationEnabled)
- [EmailSendPollingPeriod](#BKMK_EmailSendPollingPeriod)
- [EnableBingMapsIntegration](#BKMK_EnableBingMapsIntegration)
- [EnableImmersiveSkypeIntegration](#BKMK_EnableImmersiveSkypeIntegration)
- [EnableLPAuthoring](#BKMK_EnableLPAuthoring)
- [EnableMicrosoftFlowIntegration](#BKMK_EnableMicrosoftFlowIntegration)
- [EnablePricingOnCreate](#BKMK_EnablePricingOnCreate)
- [EnableSmartMatching](#BKMK_EnableSmartMatching)
- [EnforceReadOnlyPlugins](#BKMK_EnforceReadOnlyPlugins)
- [EntityImage](#BKMK_EntityImage)
- [ExpireChangeTrackingInDays](#BKMK_ExpireChangeTrackingInDays)
- [ExpireSubscriptionsInDays](#BKMK_ExpireSubscriptionsInDays)
- [ExternalBaseUrl](#BKMK_ExternalBaseUrl)
- [ExternalPartyCorrelationKeys](#BKMK_ExternalPartyCorrelationKeys)
- [ExternalPartyEntitySettings](#BKMK_ExternalPartyEntitySettings)
- [FeatureSet](#BKMK_FeatureSet)
- [FiscalCalendarStart](#BKMK_FiscalCalendarStart)
- [FiscalPeriodFormat](#BKMK_FiscalPeriodFormat)
- [FiscalPeriodFormatPeriod](#BKMK_FiscalPeriodFormatPeriod)
- [FiscalPeriodType](#BKMK_FiscalPeriodType)
- [FiscalYearDisplayCode](#BKMK_FiscalYearDisplayCode)
- [FiscalYearFormat](#BKMK_FiscalYearFormat)
- [FiscalYearFormatPrefix](#BKMK_FiscalYearFormatPrefix)
- [FiscalYearFormatSuffix](#BKMK_FiscalYearFormatSuffix)
- [FiscalYearFormatYear](#BKMK_FiscalYearFormatYear)
- [FiscalYearPeriodConnect](#BKMK_FiscalYearPeriodConnect)
- [FullNameConventionCode](#BKMK_FullNameConventionCode)
- [FutureExpansionWindow](#BKMK_FutureExpansionWindow)
- [GenerateAlertsForErrors](#BKMK_GenerateAlertsForErrors)
- [GenerateAlertsForInformation](#BKMK_GenerateAlertsForInformation)
- [GenerateAlertsForWarnings](#BKMK_GenerateAlertsForWarnings)
- [GetStartedPaneContentEnabled](#BKMK_GetStartedPaneContentEnabled)
- [GlobalAppendUrlParametersEnabled](#BKMK_GlobalAppendUrlParametersEnabled)
- [GlobalHelpUrl](#BKMK_GlobalHelpUrl)
- [GlobalHelpUrlEnabled](#BKMK_GlobalHelpUrlEnabled)
- [GoalRollupExpiryTime](#BKMK_GoalRollupExpiryTime)
- [GoalRollupFrequency](#BKMK_GoalRollupFrequency)
- [GrantAccessToNetworkService](#BKMK_GrantAccessToNetworkService)
- [HashDeltaSubjectCount](#BKMK_HashDeltaSubjectCount)
- [HashFilterKeywords](#BKMK_HashFilterKeywords)
- [HashMaxCount](#BKMK_HashMaxCount)
- [HashMinAddressCount](#BKMK_HashMinAddressCount)
- [HighContrastThemeData](#BKMK_HighContrastThemeData)
- [IgnoreInternalEmail](#BKMK_IgnoreInternalEmail)
- [InactivityTimeoutEnabled](#BKMK_InactivityTimeoutEnabled)
- [InactivityTimeoutInMins](#BKMK_InactivityTimeoutInMins)
- [InactivityTimeoutReminderInMins](#BKMK_InactivityTimeoutReminderInMins)
- [IncomingEmailExchangeEmailRetrievalBatchSize](#BKMK_IncomingEmailExchangeEmailRetrievalBatchSize)
- [InitialVersion](#BKMK_InitialVersion)
- [IntegrationUserId](#BKMK_IntegrationUserId)
- [InvoicePrefix](#BKMK_InvoicePrefix)
- [IsActionCardEnabled](#BKMK_IsActionCardEnabled)
- [IsActionSupportFeatureEnabled](#BKMK_IsActionSupportFeatureEnabled)
- [IsActivityAnalysisEnabled](#BKMK_IsActivityAnalysisEnabled)
- [IsAppMode](#BKMK_IsAppMode)
- [IsAppointmentAttachmentSyncEnabled](#BKMK_IsAppointmentAttachmentSyncEnabled)
- [IsAssignedTasksSyncEnabled](#BKMK_IsAssignedTasksSyncEnabled)
- [IsAuditEnabled](#BKMK_IsAuditEnabled)
- [IsAutoDataCaptureEnabled](#BKMK_IsAutoDataCaptureEnabled)
- [IsAutoSaveEnabled](#BKMK_IsAutoSaveEnabled)
- [IsBPFEntityCustomizationFeatureEnabled](#BKMK_IsBPFEntityCustomizationFeatureEnabled)
- [IsConflictDetectionEnabledForMobileClient](#BKMK_IsConflictDetectionEnabledForMobileClient)
- [IsContactMailingAddressSyncEnabled](#BKMK_IsContactMailingAddressSyncEnabled)
- [IsDefaultCountryCodeCheckEnabled](#BKMK_IsDefaultCountryCodeCheckEnabled)
- [IsDelegateAccessEnabled](#BKMK_IsDelegateAccessEnabled)
- [IsDelveActionHubIntegrationEnabled](#BKMK_IsDelveActionHubIntegrationEnabled)
- [IsDuplicateDetectionEnabled](#BKMK_IsDuplicateDetectionEnabled)
- [IsDuplicateDetectionEnabledForImport](#BKMK_IsDuplicateDetectionEnabledForImport)
- [IsDuplicateDetectionEnabledForOfflineSync](#BKMK_IsDuplicateDetectionEnabledForOfflineSync)
- [IsDuplicateDetectionEnabledForOnlineCreateUpdate](#BKMK_IsDuplicateDetectionEnabledForOnlineCreateUpdate)
- [IsEmailMonitoringAllowed](#BKMK_IsEmailMonitoringAllowed)
- [IsEmailServerProfileContentFilteringEnabled](#BKMK_IsEmailServerProfileContentFilteringEnabled)
- [IsEnabledForAllRoles](#BKMK_IsEnabledForAllRoles)
- [IsExternalFileStorageEnabled](#BKMK_IsExternalFileStorageEnabled)
- [IsExternalSearchIndexEnabled](#BKMK_IsExternalSearchIndexEnabled)
- [IsFiscalPeriodMonthBased](#BKMK_IsFiscalPeriodMonthBased)
- [IsFolderAutoCreatedonSP](#BKMK_IsFolderAutoCreatedonSP)
- [IsFolderBasedTrackingEnabled](#BKMK_IsFolderBasedTrackingEnabled)
- [IsFullTextSearchEnabled](#BKMK_IsFullTextSearchEnabled)
- [IsHierarchicalSecurityModelEnabled](#BKMK_IsHierarchicalSecurityModelEnabled)
- [IsMailboxForcedUnlockingEnabled](#BKMK_IsMailboxForcedUnlockingEnabled)
- [IsMailboxInactiveBackoffEnabled](#BKMK_IsMailboxInactiveBackoffEnabled)
- [IsMobileClientOnDemandSyncEnabled](#BKMK_IsMobileClientOnDemandSyncEnabled)
- [IsMobileOfflineEnabled](#BKMK_IsMobileOfflineEnabled)
- [IsOfficeGraphEnabled](#BKMK_IsOfficeGraphEnabled)
- [IsOneDriveEnabled](#BKMK_IsOneDriveEnabled)
- [IsPresenceEnabled](#BKMK_IsPresenceEnabled)
- [IsPreviewEnabledForActionCard](#BKMK_IsPreviewEnabledForActionCard)
- [IsPreviewForAutoCaptureEnabled](#BKMK_IsPreviewForAutoCaptureEnabled)
- [IsPreviewForEmailMonitoringAllowed](#BKMK_IsPreviewForEmailMonitoringAllowed)
- [IsRelationshipInsightsEnabled](#BKMK_IsRelationshipInsightsEnabled)
- [IsResourceBookingExchangeSyncEnabled](#BKMK_IsResourceBookingExchangeSyncEnabled)
- [IsSOPIntegrationEnabled](#BKMK_IsSOPIntegrationEnabled)
- [IsTextWrapEnabled](#BKMK_IsTextWrapEnabled)
- [IsUserAccessAuditEnabled](#BKMK_IsUserAccessAuditEnabled)
- [ISVIntegrationCode](#BKMK_ISVIntegrationCode)
- [KaPrefix](#BKMK_KaPrefix)
- [KbPrefix](#BKMK_KbPrefix)
- [KMSettings](#BKMK_KMSettings)
- [LanguageCode](#BKMK_LanguageCode)
- [LocaleId](#BKMK_LocaleId)
- [LongDateFormatCode](#BKMK_LongDateFormatCode)
- [MailboxIntermittentIssueMinRange](#BKMK_MailboxIntermittentIssueMinRange)
- [MailboxPermanentIssueMinRange](#BKMK_MailboxPermanentIssueMinRange)
- [MaxActionStepsInBPF](#BKMK_MaxActionStepsInBPF)
- [MaxAppointmentDurationDays](#BKMK_MaxAppointmentDurationDays)
- [MaxConditionsForMobileOfflineFilters](#BKMK_MaxConditionsForMobileOfflineFilters)
- [MaxDepthForHierarchicalSecurityModel](#BKMK_MaxDepthForHierarchicalSecurityModel)
- [MaxFolderBasedTrackingMappings](#BKMK_MaxFolderBasedTrackingMappings)
- [MaximumActiveBusinessProcessFlowsAllowedPerEntity](#BKMK_MaximumActiveBusinessProcessFlowsAllowedPerEntity)
- [MaximumDynamicPropertiesAllowed](#BKMK_MaximumDynamicPropertiesAllowed)
- [MaximumEntitiesWithActiveSLA](#BKMK_MaximumEntitiesWithActiveSLA)
- [MaximumSLAKPIPerEntityWithActiveSLA](#BKMK_MaximumSLAKPIPerEntityWithActiveSLA)
- [MaximumTrackingNumber](#BKMK_MaximumTrackingNumber)
- [MaxProductsInBundle](#BKMK_MaxProductsInBundle)
- [MaxRecordsForExportToExcel](#BKMK_MaxRecordsForExportToExcel)
- [MaxRecordsForLookupFilters](#BKMK_MaxRecordsForLookupFilters)
- [MaxUploadFileSize](#BKMK_MaxUploadFileSize)
- [MicrosoftFlowEnvironment](#BKMK_MicrosoftFlowEnvironment)
- [MinAddressBookSyncInterval](#BKMK_MinAddressBookSyncInterval)
- [MinOfflineSyncInterval](#BKMK_MinOfflineSyncInterval)
- [MinOutlookSyncInterval](#BKMK_MinOutlookSyncInterval)
- [MobileOfflineSyncInterval](#BKMK_MobileOfflineSyncInterval)
- [Name](#BKMK_Name)
- [NegativeCurrencyFormatCode](#BKMK_NegativeCurrencyFormatCode)
- [NegativeFormatCode](#BKMK_NegativeFormatCode)
- [NextTrackingNumber](#BKMK_NextTrackingNumber)
- [NotifyMailboxOwnerOfEmailServerLevelAlerts](#BKMK_NotifyMailboxOwnerOfEmailServerLevelAlerts)
- [NumberFormat](#BKMK_NumberFormat)
- [NumberGroupFormat](#BKMK_NumberGroupFormat)
- [NumberSeparator](#BKMK_NumberSeparator)
- [OfficeAppsAutoDeploymentEnabled](#BKMK_OfficeAppsAutoDeploymentEnabled)
- [OfficeGraphDelveUrl](#BKMK_OfficeGraphDelveUrl)
- [OOBPriceCalculationEnabled](#BKMK_OOBPriceCalculationEnabled)
- [OrderPrefix](#BKMK_OrderPrefix)
- [OrgDbOrgSettings](#BKMK_OrgDbOrgSettings)
- [OrgInsightsEnabled](#BKMK_OrgInsightsEnabled)
- [PastExpansionWindow](#BKMK_PastExpansionWindow)
- [Picture](#BKMK_Picture)
- [PinpointLanguageCode](#BKMK_PinpointLanguageCode)
- [PluginTraceLogSetting](#BKMK_PluginTraceLogSetting)
- [PMDesignator](#BKMK_PMDesignator)
- [PostMessageWhitelistDomains](#BKMK_PostMessageWhitelistDomains)
- [PowerBiFeatureEnabled](#BKMK_PowerBiFeatureEnabled)
- [PricingDecimalPrecision](#BKMK_PricingDecimalPrecision)
- [PrivacyStatementUrl](#BKMK_PrivacyStatementUrl)
- [PrivilegeUserGroupId](#BKMK_PrivilegeUserGroupId)
- [PrivReportingGroupId](#BKMK_PrivReportingGroupId)
- [PrivReportingGroupName](#BKMK_PrivReportingGroupName)
- [ProductRecommendationsEnabled](#BKMK_ProductRecommendationsEnabled)
- [QuickFindRecordLimitEnabled](#BKMK_QuickFindRecordLimitEnabled)
- [QuotePrefix](#BKMK_QuotePrefix)
- [RecurrenceDefaultNumberOfOccurrences](#BKMK_RecurrenceDefaultNumberOfOccurrences)
- [RecurrenceExpansionJobBatchInterval](#BKMK_RecurrenceExpansionJobBatchInterval)
- [RecurrenceExpansionJobBatchSize](#BKMK_RecurrenceExpansionJobBatchSize)
- [RecurrenceExpansionSynchCreateMax](#BKMK_RecurrenceExpansionSynchCreateMax)
- [ReferenceSiteMapXml](#BKMK_ReferenceSiteMapXml)
- [RenderSecureIFrameForEmail](#BKMK_RenderSecureIFrameForEmail)
- [ReportingGroupId](#BKMK_ReportingGroupId)
- [ReportingGroupName](#BKMK_ReportingGroupName)
- [ReportScriptErrors](#BKMK_ReportScriptErrors)
- [RequireApprovalForQueueEmail](#BKMK_RequireApprovalForQueueEmail)
- [RequireApprovalForUserEmail](#BKMK_RequireApprovalForUserEmail)
- [ResolveSimilarUnresolvedEmailAddress](#BKMK_ResolveSimilarUnresolvedEmailAddress)
- [RestrictStatusUpdate](#BKMK_RestrictStatusUpdate)
- [RiErrorStatus](#BKMK_RiErrorStatus)
- [SampleDataImportId](#BKMK_SampleDataImportId)
- [SchemaNamePrefix](#BKMK_SchemaNamePrefix)
- [ServeStaticResourcesFromAzureCDN](#BKMK_ServeStaticResourcesFromAzureCDN)
- [SessionTimeoutEnabled](#BKMK_SessionTimeoutEnabled)
- [SessionTimeoutInMins](#BKMK_SessionTimeoutInMins)
- [SessionTimeoutReminderInMins](#BKMK_SessionTimeoutReminderInMins)
- [SharePointDeploymentType](#BKMK_SharePointDeploymentType)
- [ShareToPreviousOwnerOnAssign](#BKMK_ShareToPreviousOwnerOnAssign)
- [ShowKBArticleDeprecationNotification](#BKMK_ShowKBArticleDeprecationNotification)
- [ShowWeekNumber](#BKMK_ShowWeekNumber)
- [SignupOutlookDownloadFWLink](#BKMK_SignupOutlookDownloadFWLink)
- [SiteMapXml](#BKMK_SiteMapXml)
- [SlaPauseStates](#BKMK_SlaPauseStates)
- [SocialInsightsEnabled](#BKMK_SocialInsightsEnabled)
- [SocialInsightsInstance](#BKMK_SocialInsightsInstance)
- [SocialInsightsTermsAccepted](#BKMK_SocialInsightsTermsAccepted)
- [SortId](#BKMK_SortId)
- [SqlAccessGroupId](#BKMK_SqlAccessGroupId)
- [SqlAccessGroupName](#BKMK_SqlAccessGroupName)
- [SQMEnabled](#BKMK_SQMEnabled)
- [SupportUserId](#BKMK_SupportUserId)
- [SuppressSLA](#BKMK_SuppressSLA)
- [SyncOptInSelection](#BKMK_SyncOptInSelection)
- [SyncOptInSelectionStatus](#BKMK_SyncOptInSelectionStatus)
- [SystemUserId](#BKMK_SystemUserId)
- [TagMaxAggressiveCycles](#BKMK_TagMaxAggressiveCycles)
- [TagPollingPeriod](#BKMK_TagPollingPeriod)
- [TaskBasedFlowEnabled](#BKMK_TaskBasedFlowEnabled)
- [TextAnalyticsEnabled](#BKMK_TextAnalyticsEnabled)
- [TimeFormatCode](#BKMK_TimeFormatCode)
- [TimeFormatString](#BKMK_TimeFormatString)
- [TimeSeparator](#BKMK_TimeSeparator)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [TokenExpiry](#BKMK_TokenExpiry)
- [TokenKey](#BKMK_TokenKey)
- [TrackingPrefix](#BKMK_TrackingPrefix)
- [TrackingTokenIdBase](#BKMK_TrackingTokenIdBase)
- [TrackingTokenIdDigits](#BKMK_TrackingTokenIdDigits)
- [UniqueSpecifierLength](#BKMK_UniqueSpecifierLength)
- [UnresolveEmailAddressIfMultipleMatch](#BKMK_UnresolveEmailAddressIfMultipleMatch)
- [UseInbuiltRuleForDefaultPricelistSelection](#BKMK_UseInbuiltRuleForDefaultPricelistSelection)
- [UseLegacyRendering](#BKMK_UseLegacyRendering)
- [UsePositionHierarchy](#BKMK_UsePositionHierarchy)
- [UserAccessAuditingInterval](#BKMK_UserAccessAuditingInterval)
- [UseReadForm](#BKMK_UseReadForm)
- [UserGroupId](#BKMK_UserGroupId)
- [UseSkypeProtocol](#BKMK_UseSkypeProtocol)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [WebResourceHash](#BKMK_WebResourceHash)
- [WeekStartDayCode](#BKMK_WeekStartDayCode)
- [WidgetProperties](#BKMK_WidgetProperties)
- [YammerGroupId](#BKMK_YammerGroupId)
- [YammerNetworkPermalink](#BKMK_YammerNetworkPermalink)
- [YammerOAuthAccessTokenExpired](#BKMK_YammerOAuthAccessTokenExpired)
- [YammerPostMethod](#BKMK_YammerPostMethod)
- [YearStartWeekCode](#BKMK_YearStartWeekCode)


### <a name="BKMK_ACIWebEndpointUrl"></a> ACIWebEndpointUrl

**Description**: ACI Web Endpoint URL.<br />
**DisplayName**: ACI Tenant URL.<br />
**LogicalName**: aciwebendpointurl<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 500


### <a name="BKMK_AcknowledgementTemplateId"></a> AcknowledgementTemplateId

**Description**: Unique identifier of the template to be used for acknowledgement when a user unsubscribes.<br />
**DisplayName**: Acknowledgement Template<br />
**LogicalName**: acknowledgementtemplateid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: template


### <a name="BKMK_AllowAddressBookSyncs"></a> AllowAddressBookSyncs

**Description**: Indicates whether background address book synchronization in Microsoft Office Outlook is allowed.<br />
**DisplayName**: Allow Address Book Synchronization<br />
**LogicalName**: allowaddressbooksyncs<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_AllowAutoResponseCreation"></a> AllowAutoResponseCreation

**Description**: Indicates whether automatic response creation is allowed.<br />
**DisplayName**: Allow Automatic Response Creation<br />
**LogicalName**: allowautoresponsecreation<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_AllowAutoUnsubscribe"></a> AllowAutoUnsubscribe

**Description**: Indicates whether automatic unsubscribe is allowed.<br />
**DisplayName**: Allow Automatic Unsubscribe<br />
**LogicalName**: allowautounsubscribe<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_AllowAutoUnsubscribeAcknowledgement"></a> AllowAutoUnsubscribeAcknowledgement

**Description**: Indicates whether automatic unsubscribe acknowledgement email is allowed to send.<br />
**DisplayName**: Allow Automatic Unsubscribe Acknowledgement<br />
**LogicalName**: allowautounsubscribeacknowledgement<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_AllowClientMessageBarAd"></a> AllowClientMessageBarAd

**Description**: Indicates whether Outlook Client message bar advertisement is allowed.<br />
**DisplayName**: Allow Outlook Client Message Bar Advertisement<br />
**LogicalName**: allowclientmessagebarad<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_AllowEntityOnlyAudit"></a> AllowEntityOnlyAudit

**Description**: Indicates whether auditing of changes to entity is allowed when no attributes have changed.<br />
**DisplayName**: Allow Entity Level Auditing<br />
**LogicalName**: allowentityonlyaudit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_AllowMarketingEmailExecution"></a> AllowMarketingEmailExecution

**Description**: Indicates whether marketing emails execution is allowed.<br />
**DisplayName**: Allow Marketing Email Execution<br />
**LogicalName**: allowmarketingemailexecution<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_AllowOfflineScheduledSyncs"></a> AllowOfflineScheduledSyncs

**Description**: Indicates whether background offline synchronization in Microsoft Office Outlook is allowed.<br />
**DisplayName**: Allow Offline Scheduled Synchronization<br />
**LogicalName**: allowofflinescheduledsyncs<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_AllowOutlookScheduledSyncs"></a> AllowOutlookScheduledSyncs

**Description**: Indicates whether scheduled synchronizations to Outlook are allowed.<br />
**DisplayName**: Allow Scheduled Synchronization<br />
**LogicalName**: allowoutlookscheduledsyncs<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_AllowUnresolvedPartiesOnEmailSend"></a> AllowUnresolvedPartiesOnEmailSend

**Description**: Indicates whether users are allowed to send email to unresolved parties (parties must still have an email address).<br />
**DisplayName**: Allow Unresolved Address Email Send<br />
**LogicalName**: allowunresolvedpartiesonemailsend<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_AllowUserFormModePreference"></a> AllowUserFormModePreference

**Description**: Indicates whether individuals can select their form mode preference in their personal options.<br />
**DisplayName**: Allow User Form Mode Preference<br />
**LogicalName**: allowuserformmodepreference<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_AllowUsersSeeAppdownloadMessage"></a> AllowUsersSeeAppdownloadMessage

**Description**: Indicates whether the showing tablet application notification bars in a browser is allowed.<br />
**DisplayName**: Allow the showing tablet application notification bars in a browser.<br />
**LogicalName**: allowusersseeappdownloadmessage<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_AllowWebExcelExport"></a> AllowWebExcelExport

**Description**: Indicates whether Web-based export of grids to Microsoft Office Excel is allowed.<br />
**DisplayName**: Allow Export to Excel<br />
**LogicalName**: allowwebexcelexport<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_AMDesignator"></a> AMDesignator

**Description**: AM designator to use throughout Microsoft Dynamics CRM.<br />
**DisplayName**: AM Designator<br />
**LogicalName**: amdesignator<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 25


### <a name="BKMK_AppDesignerExperienceEnabled"></a> AppDesignerExperienceEnabled

**Description**: Indicates whether the appDesignerExperience is enabled for the organization.<br />
**DisplayName**: Enable App Designer Experience for this Organization<br />
**LogicalName**: appdesignerexperienceenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_AutoApplyDefaultonCaseCreate"></a> AutoApplyDefaultonCaseCreate

**Description**: Select whether to auto apply the default customer entitlement on case creation.<br />
**DisplayName**: Auto Apply Default Entitlement on Case Create<br />
**LogicalName**: autoapplydefaultoncasecreate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_AutoApplyDefaultonCaseUpdate"></a> AutoApplyDefaultonCaseUpdate

**Description**: Select whether to auto apply the default customer entitlement on case update.<br />
**DisplayName**: Auto Apply Default Entitlement on Case Update<br />
**LogicalName**: autoapplydefaultoncaseupdate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_AutoApplySLA"></a> AutoApplySLA

**Description**: Indicates whether to Auto-apply SLA on case record update after SLA was manually applied.<br />
**DisplayName**: Is Auto-apply SLA After Manually Over-riding<br />
**LogicalName**: autoapplysla<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_AzureSchedulerJobCollectionName"></a> AzureSchedulerJobCollectionName

**Description**: For internal use only.<br />
**DisplayName**: For internal use only.<br />
**LogicalName**: azureschedulerjobcollectionname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_BaseCurrencyId"></a> BaseCurrencyId

**Description**: Unique identifier of the base currency of the organization.<br />
**DisplayName**: Currency<br />
**LogicalName**: basecurrencyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: transactioncurrency


### <a name="BKMK_BingMapsApiKey"></a> BingMapsApiKey

**Description**: Api Key to be used in requests to Bing Maps services.<br />
**DisplayName**: Bing Maps API Key<br />
**LogicalName**: bingmapsapikey<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_BlockedAttachments"></a> BlockedAttachments

**Description**: Prevent upload or download of certain attachment types that are considered dangerous.<br />
**DisplayName**: Block Attachments<br />
**LogicalName**: blockedattachments<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_BoundDashboardDefaultCardExpanded"></a> BoundDashboardDefaultCardExpanded

**Description**: Display cards in expanded state for interactive dashboard<br />
**DisplayName**: Display cards in expanded state for Interactive Dashboard<br />
**LogicalName**: bounddashboarddefaultcardexpanded<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_BulkOperationPrefix"></a> BulkOperationPrefix

**Description**: Prefix used for bulk operation numbering.<br />
**DisplayName**: Bulk Operation Prefix<br />
**LogicalName**: bulkoperationprefix<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 20


### <a name="BKMK_BusinessClosureCalendarId"></a> BusinessClosureCalendarId

**Description**: Unique identifier of the business closure calendar of organization.<br />
**DisplayName**: Business Closure Calendar<br />
**LogicalName**: businessclosurecalendarid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_CalendarType"></a> CalendarType

**Description**: Calendar type for the system. Set to Gregorian US by default.<br />
**DisplayName**: Calendar Type<br />
**LogicalName**: calendartype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_CampaignPrefix"></a> CampaignPrefix

**Description**: Prefix used for campaign numbering.<br />
**DisplayName**: Campaign Prefix<br />
**LogicalName**: campaignprefix<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 20


### <a name="BKMK_CascadeStatusUpdate"></a> CascadeStatusUpdate

**Description**: Flag to cascade Update on incident.<br />
**DisplayName**: Cascade Status Update<br />
**LogicalName**: cascadestatusupdate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_CasePrefix"></a> CasePrefix

**Description**: Prefix to use for all cases throughout Microsoft Dynamics 365.<br />
**DisplayName**: Case Prefix<br />
**LogicalName**: caseprefix<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 20


### <a name="BKMK_CategoryPrefix"></a> CategoryPrefix

**Description**: Type the prefix to use for all categories in Microsoft Dynamics 365.<br />
**DisplayName**: Category Prefix<br />
**LogicalName**: categoryprefix<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 20


### <a name="BKMK_ClientFeatureSet"></a> ClientFeatureSet

**Description**: Client Features to be enabled as an XML BLOB.<br />
**DisplayName**: Client Feature Set<br />
**LogicalName**: clientfeatureset<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_ContractPrefix"></a> ContractPrefix

**Description**: Prefix to use for all contracts throughout Microsoft Dynamics 365.<br />
**DisplayName**: Contract Prefix<br />
**LogicalName**: contractprefix<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 20


### <a name="BKMK_CortanaProactiveExperienceEnabled"></a> CortanaProactiveExperienceEnabled

**Description**: Indicates whether the feature CortanaProactiveExperience Flow processes should be enabled for the organization.<br />
**DisplayName**: Enable Cortana Proactive Experience Flow processes for this Organization<br />
**LogicalName**: cortanaproactiveexperienceenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_CreateProductsWithoutParentInActiveState"></a> CreateProductsWithoutParentInActiveState

**Description**: Enable Initial state of newly created products to be Active instead of Draft<br />
**DisplayName**: Enable Active Initial Product State<br />
**LogicalName**: createproductswithoutparentinactivestate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_CurrencyDecimalPrecision"></a> CurrencyDecimalPrecision

**Description**: Number of decimal places that can be used for currency.<br />
**DisplayName**: Currency Decimal Precision<br />
**LogicalName**: currencydecimalprecision<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_CurrencyDisplayOption"></a> CurrencyDisplayOption

**Description**: Indicates whether to display money fields with currency code or currency symbol.<br />
**DisplayName**: Display Currencies Using<br />
**LogicalName**: currencydisplayoption<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Currency symbol
- **Value**: 1 **Label**: Currency code



### <a name="BKMK_CurrencyFormatCode"></a> CurrencyFormatCode

**Description**: Information about how currency symbols are placed throughout Microsoft Dynamics CRM.<br />
**DisplayName**: Currency Format Code<br />
**LogicalName**: currencyformatcode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: $123
- **Value**: 1 **Label**: 123$
- **Value**: 2 **Label**: $ 123
- **Value**: 3 **Label**: 123 $



### <a name="BKMK_CurrencySymbol"></a> CurrencySymbol

**Description**: Symbol used for currency throughout Microsoft Dynamics 365.<br />
**DisplayName**: Currency Symbol<br />
**LogicalName**: currencysymbol<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 13


### <a name="BKMK_CurrentBulkOperationNumber"></a> CurrentBulkOperationNumber

**Description**: Current bulk operation number. Deprecated. Use SetAutoNumberSeed message.<br />
**DisplayName**: Current Bulk Operation Number<br />
**LogicalName**: currentbulkoperationnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_CurrentCampaignNumber"></a> CurrentCampaignNumber

**Description**: Current campaign number. Deprecated. Use SetAutoNumberSeed message.<br />
**DisplayName**: Current Campaign Number<br />
**LogicalName**: currentcampaignnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_CurrentCaseNumber"></a> CurrentCaseNumber

**Description**: First case number to use. Deprecated. Use SetAutoNumberSeed message.<br />
**DisplayName**: Current Case Number<br />
**LogicalName**: currentcasenumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_CurrentCategoryNumber"></a> CurrentCategoryNumber

**Description**: Enter the first number to use for Categories. Deprecated. Use SetAutoNumberSeed message.<br />
**DisplayName**: Current Category Number<br />
**LogicalName**: currentcategorynumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_CurrentContractNumber"></a> CurrentContractNumber

**Description**: First contract number to use. Deprecated. Use SetAutoNumberSeed message.<br />
**DisplayName**: Current Contract Number<br />
**LogicalName**: currentcontractnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_CurrentInvoiceNumber"></a> CurrentInvoiceNumber

**Description**: First invoice number to use. Deprecated. Use SetAutoNumberSeed message.<br />
**DisplayName**: Current Invoice Number<br />
**LogicalName**: currentinvoicenumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_CurrentKaNumber"></a> CurrentKaNumber

**Description**: Enter the first number to use for knowledge articles. Deprecated. Use SetAutoNumberSeed message.<br />
**DisplayName**: Current Knowledge Article Number<br />
**LogicalName**: currentkanumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_CurrentKbNumber"></a> CurrentKbNumber

**Description**: First article number to use. Deprecated. Use SetAutoNumberSeed message.<br />
**DisplayName**: Current Article Number<br />
**LogicalName**: currentkbnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_CurrentOrderNumber"></a> CurrentOrderNumber

**Description**: First order number to use. Deprecated. Use SetAutoNumberSeed message.<br />
**DisplayName**: Current Order Number<br />
**LogicalName**: currentordernumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_CurrentQuoteNumber"></a> CurrentQuoteNumber

**Description**: First quote number to use. Deprecated. Use SetAutoNumberSeed message.<br />
**DisplayName**: Current Quote Number<br />
**LogicalName**: currentquotenumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_DateFormatCode"></a> DateFormatCode

**Description**: Information about how the date is displayed throughout Microsoft CRM.<br />
**DisplayName**: Date Format Code<br />
**LogicalName**: dateformatcode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:




### <a name="BKMK_DateFormatString"></a> DateFormatString

**Description**: String showing how the date is displayed throughout Microsoft CRM.<br />
**DisplayName**: Date Format String<br />
**LogicalName**: dateformatstring<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 255


### <a name="BKMK_DateSeparator"></a> DateSeparator

**Description**: Character used to separate the month, the day, and the year in dates throughout Microsoft Dynamics 365.<br />
**DisplayName**: Date Separator<br />
**LogicalName**: dateseparator<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 5


### <a name="BKMK_DecimalSymbol"></a> DecimalSymbol

**Description**: Symbol used for decimal in Microsoft Dynamics 365.<br />
**DisplayName**: Decimal Symbol<br />
**LogicalName**: decimalsymbol<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 5


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


### <a name="BKMK_DefaultCrmCustomName"></a> DefaultCrmCustomName

**Description**: Name of the default crm custom.<br />
**DisplayName**: Name of the default app<br />
**LogicalName**: defaultcrmcustomname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: True<br />
**MaxLength**: 100


### <a name="BKMK_DefaultEmailServerProfileId"></a> DefaultEmailServerProfileId

**Description**: Unique identifier of the default email server profile.<br />
**DisplayName**: Email Server Profile<br />
**LogicalName**: defaultemailserverprofileid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: emailserverprofile


### <a name="BKMK_DefaultEmailSettings"></a> DefaultEmailSettings

**Description**: XML string containing the default email settings that are applied when a user or queue is created.<br />
**DisplayName**: Default Email Settings<br />
**LogicalName**: defaultemailsettings<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_DefaultMobileOfflineProfileId"></a> DefaultMobileOfflineProfileId

**Description**: Unique identifier of the default mobile offline profile.<br />
**DisplayName**: Default Mobile Offline Profile<br />
**LogicalName**: defaultmobileofflineprofileid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: mobileofflineprofile


### <a name="BKMK_DefaultRecurrenceEndRangeType"></a> DefaultRecurrenceEndRangeType

**Description**: Type of default recurrence end range date.<br />
**DisplayName**: Default Recurrence End Range Type<br />
**LogicalName**: defaultrecurrenceendrangetype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: No End Date
- **Value**: 2 **Label**: Number of Occurrences
- **Value**: 3 **Label**: End By Date



### <a name="BKMK_DefaultThemeData"></a> DefaultThemeData

**Description**: Default theme data for the organization.<br />
**DisplayName**: Default Theme Data<br />
**LogicalName**: defaultthemedata<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_DelegatedAdminUserId"></a> DelegatedAdminUserId

**Description**: Unique identifier of the delegated admin user for the organization.<br />
**DisplayName**: Delegated Admin<br />
**LogicalName**: delegatedadminuserid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_DisableSocialCare"></a> DisableSocialCare

**Description**: Indicates whether Social Care is disabled.<br />
**DisplayName**: Is Social Care disabled<br />
**LogicalName**: disablesocialcare<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_DiscountCalculationMethod"></a> DiscountCalculationMethod

**Description**: Discount calculation method for the QOOI product.<br />
**DisplayName**: Discount calculation method<br />
**LogicalName**: discountcalculationmethod<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Line item
- **Value**: 1 **Label**: Per unit



### <a name="BKMK_DisplayNavigationTour"></a> DisplayNavigationTour

**Description**: Indicates whether or not navigation tour is displayed.<br />
**DisplayName**: Display Navigation Tour<br />
**LogicalName**: displaynavigationtour<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_EmailConnectionChannel"></a> EmailConnectionChannel

**Description**: Select if you want to use the Email Router or server-side synchronization for email processing.<br />
**DisplayName**: Email Connection Channel<br />
**LogicalName**: emailconnectionchannel<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Server-Side Synchronization
- **Value**: 1 **Label**: Microsoft Dynamics 365 Email Router



### <a name="BKMK_EmailCorrelationEnabled"></a> EmailCorrelationEnabled

**Description**: Flag to turn email correlation on or off.<br />
**DisplayName**: Use Email Correlation<br />
**LogicalName**: emailcorrelationenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_EmailSendPollingPeriod"></a> EmailSendPollingPeriod

**Description**: Normal polling frequency used for sending email in Microsoft Office Outlook.<br />
**DisplayName**: Email Send Polling Frequency<br />
**LogicalName**: emailsendpollingperiod<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_EnableBingMapsIntegration"></a> EnableBingMapsIntegration

**Description**: Enable Integration with Bing Maps<br />
**DisplayName**: Enable Integration with Bing Maps<br />
**LogicalName**: enablebingmapsintegration<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_EnableImmersiveSkypeIntegration"></a> EnableImmersiveSkypeIntegration

**Description**: Enable Integration with Immersive Skype<br />
**DisplayName**: Enable Integration with Immersive Skype<br />
**LogicalName**: enableimmersiveskypeintegration<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_EnableLPAuthoring"></a> EnableLPAuthoring

**Description**: Select to enable learning path auhtoring.<br />
**DisplayName**: Enable Learning Path Authoring<br />
**LogicalName**: enablelpauthoring<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_EnableMicrosoftFlowIntegration"></a> EnableMicrosoftFlowIntegration

**Description**: Enable Integration with Microsoft Flow<br />
**DisplayName**: Enable Integration with Microsoft Flow<br />
**LogicalName**: enablemicrosoftflowintegration<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_EnablePricingOnCreate"></a> EnablePricingOnCreate

**Description**: Enable pricing calculations on a Create call.<br />
**DisplayName**: Enable Pricing On Create<br />
**LogicalName**: enablepricingoncreate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_EnableSmartMatching"></a> EnableSmartMatching

**Description**: Use Smart Matching.<br />
**DisplayName**: Enable Smart Matching<br />
**LogicalName**: enablesmartmatching<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_EnforceReadOnlyPlugins"></a> EnforceReadOnlyPlugins

**Description**: Organization setting to enforce read only plugins.<br />
**DisplayName**: Organization setting to enforce read only plugins.<br />
**LogicalName**: enforcereadonlyplugins<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_EntityImage"></a> EntityImage

**Description**: The default image for the entity.<br />
**DisplayName**: Entity Image<br />
**LogicalName**: entityimage<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Image<br />
**IsPrimaryImage**: False<br />
**MaxHeight**: 144<br />
**MaxWidth**: 144


### <a name="BKMK_ExpireChangeTrackingInDays"></a> ExpireChangeTrackingInDays

**Description**: Maximum number of days to keep change tracking deleted records<br />
**DisplayName**: Days to Expire Change Tracking Deleted Records<br />
**LogicalName**: expirechangetrackingindays<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 365<br />
**MinValue**: 0


### <a name="BKMK_ExpireSubscriptionsInDays"></a> ExpireSubscriptionsInDays

**Description**: Maximum number of days before deleting inactive subscriptions.<br />
**DisplayName**: Days to Expire Subscriptions<br />
**LogicalName**: expiresubscriptionsindays<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_ExternalBaseUrl"></a> ExternalBaseUrl

**Description**: Specify the base URL to use to look for external document suggestions.<br />
**DisplayName**: External Base URL<br />
**LogicalName**: externalbaseurl<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 500


### <a name="BKMK_ExternalPartyCorrelationKeys"></a> ExternalPartyCorrelationKeys

**Description**: XML string containing the ExternalPartyEnabled entities correlation keys for association of existing External Party instance entities to newly created IsExternalPartyEnabled entities.For internal use only<br />
**DisplayName**: ExternalPartyEnabled Entities correlation Keys<br />
**LogicalName**: externalpartycorrelationkeys<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_ExternalPartyEntitySettings"></a> ExternalPartyEntitySettings

**Description**: XML string containing the ExternalPartyEnabled entities settings.<br />
**DisplayName**: ExternalPartyEnabled Entities Settings.For internal use only<br />
**LogicalName**: externalpartyentitysettings<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_FeatureSet"></a> FeatureSet

**Description**: Features to be enabled as an XML BLOB.<br />
**DisplayName**: Feature Set<br />
**LogicalName**: featureset<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_FiscalCalendarStart"></a> FiscalCalendarStart

**Description**: Start date for the fiscal period that is to be used throughout Microsoft CRM.<br />
**DisplayName**: Fiscal Calendar Start<br />
**LogicalName**: fiscalcalendarstart<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_FiscalPeriodFormat"></a> FiscalPeriodFormat

**Description**: Information that specifies how the name of the fiscal period is displayed throughout Microsoft CRM.<br />
**DisplayName**: Fiscal Period Format<br />
**LogicalName**: fiscalperiodformat<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 25


### <a name="BKMK_FiscalPeriodFormatPeriod"></a> FiscalPeriodFormatPeriod

**Description**: Format in which the fiscal period will be displayed.<br />
**DisplayName**: Format for Fiscal Period<br />
**LogicalName**: fiscalperiodformatperiod<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Quarter {0}
- **Value**: 2 **Label**: Q{0}
- **Value**: 3 **Label**: P{0}
- **Value**: 4 **Label**: Month {0}
- **Value**: 5 **Label**: M{0}
- **Value**: 6 **Label**: Semester {0}
- **Value**: 7 **Label**: Month Name



### <a name="BKMK_FiscalPeriodType"></a> FiscalPeriodType

**Description**: Type of fiscal period used throughout Microsoft CRM.<br />
**DisplayName**: Fiscal Period Type<br />
**LogicalName**: fiscalperiodtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_FiscalYearDisplayCode"></a> FiscalYearDisplayCode

**Description**: Information that specifies whether the fiscal year should be displayed based on the start date or the end date of the fiscal year.<br />
**DisplayName**: Fiscal Year Display<br />
**LogicalName**: fiscalyeardisplaycode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: <br />
**MinValue**: 


### <a name="BKMK_FiscalYearFormat"></a> FiscalYearFormat

**Description**: Information that specifies how the name of the fiscal year is displayed throughout Microsoft CRM.<br />
**DisplayName**: Fiscal Year Format<br />
**LogicalName**: fiscalyearformat<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 25


### <a name="BKMK_FiscalYearFormatPrefix"></a> FiscalYearFormatPrefix

**Description**: Prefix for the display of the fiscal year.<br />
**DisplayName**: Prefix for Fiscal Year<br />
**LogicalName**: fiscalyearformatprefix<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: FY
- **Value**: 2 **Label**: 



### <a name="BKMK_FiscalYearFormatSuffix"></a> FiscalYearFormatSuffix

**Description**: Suffix for the display of the fiscal year.<br />
**DisplayName**: Suffix for Fiscal Year<br />
**LogicalName**: fiscalyearformatsuffix<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: FY
- **Value**: 2 **Label**:  Fiscal Year
- **Value**: 3 **Label**: 



### <a name="BKMK_FiscalYearFormatYear"></a> FiscalYearFormatYear

**Description**: Format for the year.<br />
**DisplayName**: Fiscal Year Format Year<br />
**LogicalName**: fiscalyearformatyear<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: YYYY
- **Value**: 2 **Label**: YY
- **Value**: 3 **Label**: GGYY



### <a name="BKMK_FiscalYearPeriodConnect"></a> FiscalYearPeriodConnect

**Description**: Information that specifies how the names of the fiscal year and the fiscal period should be connected when displayed together.<br />
**DisplayName**: Fiscal Year Period Connector<br />
**LogicalName**: fiscalyearperiodconnect<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 5


### <a name="BKMK_FullNameConventionCode"></a> FullNameConventionCode

**Description**: Order in which names are to be displayed throughout Microsoft CRM.<br />
**DisplayName**: Full Name Display Order<br />
**LogicalName**: fullnameconventioncode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Last Name, First Name
- **Value**: 1 **Label**: First Name
- **Value**: 2 **Label**: Last Name, First Name, Middle Initial
- **Value**: 3 **Label**: First Name, Middle Initial, Last Name
- **Value**: 4 **Label**: Last Name, First Name, Middle Name
- **Value**: 5 **Label**: First Name, Middle Name, Last Name
- **Value**: 6 **Label**: Last Name, space, First Name
- **Value**: 7 **Label**: Last Name, no space, First Name



### <a name="BKMK_FutureExpansionWindow"></a> FutureExpansionWindow

**Description**: Specifies the maximum number of months in future for which the recurring activities can be created.<br />
**DisplayName**: Future Expansion Window<br />
**LogicalName**: futureexpansionwindow<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 140<br />
**MinValue**: 1


### <a name="BKMK_GenerateAlertsForErrors"></a> GenerateAlertsForErrors

**Description**: Indicates whether alerts will be generated for errors.<br />
**DisplayName**: Generate Alerts For Errors<br />
**LogicalName**: generatealertsforerrors<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_GenerateAlertsForInformation"></a> GenerateAlertsForInformation

**Description**: Indicates whether alerts will be generated for information.<br />
**DisplayName**: Generate Alerts For Information<br />
**LogicalName**: generatealertsforinformation<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_GenerateAlertsForWarnings"></a> GenerateAlertsForWarnings

**Description**: Indicates whether alerts will be generated for warnings.<br />
**DisplayName**: Generate Alerts For Warnings<br />
**LogicalName**: generatealertsforwarnings<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_GetStartedPaneContentEnabled"></a> GetStartedPaneContentEnabled

**Description**: Indicates whether Get Started content is enabled for this organization.<br />
**DisplayName**: Is Get Started Pane Content Enabled<br />
**LogicalName**: getstartedpanecontentenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_GlobalAppendUrlParametersEnabled"></a> GlobalAppendUrlParametersEnabled

**Description**: Indicates whether the append URL parameters is enabled.<br />
**DisplayName**: Is AppendUrl Parameters enabled<br />
**LogicalName**: globalappendurlparametersenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_GlobalHelpUrl"></a> GlobalHelpUrl

**Description**: URL for the web page global help.<br />
**DisplayName**: Global Help URL.<br />
**LogicalName**: globalhelpurl<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 500


### <a name="BKMK_GlobalHelpUrlEnabled"></a> GlobalHelpUrlEnabled

**Description**: Indicates whether the customizable global help is enabled.<br />
**DisplayName**: Is Customizable Global Help enabled<br />
**LogicalName**: globalhelpurlenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_GoalRollupExpiryTime"></a> GoalRollupExpiryTime

**Description**: Number of days after the goal's end date after which the rollup of the goal stops automatically.<br />
**DisplayName**: Rollup Expiration Time for Goal<br />
**LogicalName**: goalrollupexpirytime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 400<br />
**MinValue**: 0


### <a name="BKMK_GoalRollupFrequency"></a> GoalRollupFrequency

**Description**: Number of hours between automatic rollup jobs .<br />
**DisplayName**: Automatic Rollup Frequency for Goal<br />
**LogicalName**: goalrollupfrequency<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 1


### <a name="BKMK_GrantAccessToNetworkService"></a> GrantAccessToNetworkService

**Description**: For internal use only.<br />
**DisplayName**: Grant Access To Network Service<br />
**LogicalName**: grantaccesstonetworkservice<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_HashDeltaSubjectCount"></a> HashDeltaSubjectCount

**Description**: Maximum difference allowed between subject keywords count of the email messaged to be correlated<br />
**DisplayName**: Hash Delta Subject Count<br />
**LogicalName**: hashdeltasubjectcount<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_HashFilterKeywords"></a> HashFilterKeywords

**Description**: Filter Subject Keywords<br />
**DisplayName**: Hash Filter Keywords<br />
**LogicalName**: hashfilterkeywords<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_HashMaxCount"></a> HashMaxCount

**Description**: Maximum number of subject keywords or recipients used for correlation<br />
**DisplayName**: Hash Max Count<br />
**LogicalName**: hashmaxcount<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_HashMinAddressCount"></a> HashMinAddressCount

**Description**: Minimum number of recipients required to match for email messaged to be correlated<br />
**DisplayName**: Hash Min Address Count<br />
**LogicalName**: hashminaddresscount<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_HighContrastThemeData"></a> HighContrastThemeData

**Description**: High contrast theme data for the organization.<br />
**DisplayName**: High contrast Theme Data<br />
**LogicalName**: highcontrastthemedata<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_IgnoreInternalEmail"></a> IgnoreInternalEmail

**Description**: Indicates whether incoming email sent by internal Microsoft Dynamics 365 users or queues should be tracked.<br />
**DisplayName**: Ignore Internal Email<br />
**LogicalName**: ignoreinternalemail<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_InactivityTimeoutEnabled"></a> InactivityTimeoutEnabled

**Description**: Information that specifies whether Inactivity timeout is enabled<br />
**DisplayName**: Inactivity timeout enabled<br />
**LogicalName**: inactivitytimeoutenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_InactivityTimeoutInMins"></a> InactivityTimeoutInMins

**Description**: Inactivity timeout in minutes<br />
**DisplayName**: Inactivity timeout in minutes<br />
**LogicalName**: inactivitytimeoutinmins<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_InactivityTimeoutReminderInMins"></a> InactivityTimeoutReminderInMins

**Description**: Inactivity timeout reminder in minutes<br />
**DisplayName**: Inactivity timeout reminder in minutes<br />
**LogicalName**: inactivitytimeoutreminderinmins<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_IncomingEmailExchangeEmailRetrievalBatchSize"></a> IncomingEmailExchangeEmailRetrievalBatchSize

**Description**: Setting for the Async Service Mailbox Queue. Defines the retrieval batch size of exchange server.<br />
**DisplayName**: Exchange Email Retrieval Batch Size<br />
**LogicalName**: incomingemailexchangeemailretrievalbatchsize<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 1


### <a name="BKMK_InitialVersion"></a> InitialVersion

**Description**: Initial version of the organization.<br />
**DisplayName**: Initial Version<br />
**LogicalName**: initialversion<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 20


### <a name="BKMK_IntegrationUserId"></a> IntegrationUserId

**Description**: Unique identifier of the integration user for the organization.<br />
**DisplayName**: Integration User<br />
**LogicalName**: integrationuserid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_InvoicePrefix"></a> InvoicePrefix

**Description**: Prefix to use for all invoice numbers throughout Microsoft Dynamics 365.<br />
**DisplayName**: Invoice Prefix<br />
**LogicalName**: invoiceprefix<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 20


### <a name="BKMK_IsActionCardEnabled"></a> IsActionCardEnabled

**Description**: Indicates whether the feature Action Card should be enabled for the organization.<br />
**DisplayName**: Enable Action Card for this Organization<br />
**LogicalName**: isactioncardenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsActionSupportFeatureEnabled"></a> IsActionSupportFeatureEnabled

**Description**: Information that specifies whether Action Support Feature is enabled<br />
**DisplayName**: Action Support Feature enabled<br />
**LogicalName**: isactionsupportfeatureenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsActivityAnalysisEnabled"></a> IsActivityAnalysisEnabled

**Description**: Indicates whether the feature Relationship Analytics should be enabled for the organization.<br />
**DisplayName**: Enable Relationship Analytics for this Organization<br />
**LogicalName**: isactivityanalysisenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsAppMode"></a> IsAppMode

**Description**: Indicates whether loading of Microsoft Dynamics 365 in a browser window that does not have address, tool, and menu bars is enabled.<br />
**DisplayName**: Is Application Mode Enabled<br />
**LogicalName**: isappmode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsAppointmentAttachmentSyncEnabled"></a> IsAppointmentAttachmentSyncEnabled

**Description**: Enable or disable attachments sync for outlook and exchange.<br />
**DisplayName**: Is Attachment Sync Enabled<br />
**LogicalName**: isappointmentattachmentsyncenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsAssignedTasksSyncEnabled"></a> IsAssignedTasksSyncEnabled

**Description**: Enable or disable assigned tasks sync for outlook and exchange.<br />
**DisplayName**: Is Assigned Tasks Sync Enabled<br />
**LogicalName**: isassignedtaskssyncenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsAuditEnabled"></a> IsAuditEnabled

**Description**: Enable or disable auditing of changes.<br />
**DisplayName**: Is Auditing Enabled<br />
**LogicalName**: isauditenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsAutoDataCaptureEnabled"></a> IsAutoDataCaptureEnabled

**Description**: Indicates whether the feature Auto Capture should be enabled for the organization.<br />
**DisplayName**: Enable Auto Capture for this Organization<br />
**LogicalName**: isautodatacaptureenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsAutoSaveEnabled"></a> IsAutoSaveEnabled

**Description**: Information on whether auto save is enabled.<br />
**DisplayName**: Auto Save Enabled<br />
**LogicalName**: isautosaveenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_IsBPFEntityCustomizationFeatureEnabled"></a> IsBPFEntityCustomizationFeatureEnabled

**Description**: Information that specifies whether BPF Entity Customization Feature is enabled<br />
**DisplayName**: BPF Entity Customization Feature enabled<br />
**LogicalName**: isbpfentitycustomizationfeatureenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsConflictDetectionEnabledForMobileClient"></a> IsConflictDetectionEnabledForMobileClient

**Description**: Information that specifies whether conflict detection for mobile client is enabled.<br />
**DisplayName**: Is Conflict Detection for Mobile Client enabled<br />
**LogicalName**: isconflictdetectionenabledformobileclient<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsContactMailingAddressSyncEnabled"></a> IsContactMailingAddressSyncEnabled

**Description**: Enable or disable mailing address sync for outlook and exchange.<br />
**DisplayName**: Is Mailing Address Sync Enabled<br />
**LogicalName**: iscontactmailingaddresssyncenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_IsDefaultCountryCodeCheckEnabled"></a> IsDefaultCountryCodeCheckEnabled

**Description**: Enable or disable country code selection.<br />
**DisplayName**: Enable or disable country code selection<br />
**LogicalName**: isdefaultcountrycodecheckenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_IsDelegateAccessEnabled"></a> IsDelegateAccessEnabled

**Description**: Enable Delegation Access content<br />
**DisplayName**: Is Delegation Access Enabled<br />
**LogicalName**: isdelegateaccessenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsDelveActionHubIntegrationEnabled"></a> IsDelveActionHubIntegrationEnabled

**Description**: Indicates whether the feature Action Hub should be enabled for the organization.<br />
**DisplayName**: Enable Action Hub for this Organization<br />
**LogicalName**: isdelveactionhubintegrationenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsDuplicateDetectionEnabled"></a> IsDuplicateDetectionEnabled

**Description**: Indicates whether duplicate detection of records is enabled.<br />
**DisplayName**: Is Duplicate Detection Enabled<br />
**LogicalName**: isduplicatedetectionenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsDuplicateDetectionEnabledForImport"></a> IsDuplicateDetectionEnabledForImport

**Description**: Indicates whether duplicate detection of records during import is enabled.<br />
**DisplayName**: Is Duplicate Detection Enabled For Import<br />
**LogicalName**: isduplicatedetectionenabledforimport<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsDuplicateDetectionEnabledForOfflineSync"></a> IsDuplicateDetectionEnabledForOfflineSync

**Description**: Indicates whether duplicate detection of records during offline synchronization is enabled.<br />
**DisplayName**: Is Duplicate Detection Enabled For Offline Synchronization<br />
**LogicalName**: isduplicatedetectionenabledforofflinesync<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsDuplicateDetectionEnabledForOnlineCreateUpdate"></a> IsDuplicateDetectionEnabledForOnlineCreateUpdate

**Description**: Indicates whether duplicate detection during online create or update is enabled.<br />
**DisplayName**: Is Duplicate Detection Enabled for Online Create/Update<br />
**LogicalName**: isduplicatedetectionenabledforonlinecreateupdate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsEmailMonitoringAllowed"></a> IsEmailMonitoringAllowed

**Description**: Allow tracking recipient activity on sent emails.<br />
**DisplayName**: Allow tracking recipient activity on sent emails<br />
**LogicalName**: isemailmonitoringallowed<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_IsEmailServerProfileContentFilteringEnabled"></a> IsEmailServerProfileContentFilteringEnabled

**Description**: Enable Email Server Profile content filtering<br />
**DisplayName**: Is Email Server Profile Content Filtering Enabled<br />
**LogicalName**: isemailserverprofilecontentfilteringenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsEnabledForAllRoles"></a> IsEnabledForAllRoles

**Description**: Indicates whether appmodule is enabled for all roles<br />
**DisplayName**: option set values for isenabledforallroles<br />
**LogicalName**: isenabledforallroles<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_IsExternalFileStorageEnabled"></a> IsExternalFileStorageEnabled

**Description**: Indicates whether the organization's files are being stored in Azure.<br />
**DisplayName**: Enable external file storage<br />
**LogicalName**: isexternalfilestorageenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsExternalSearchIndexEnabled"></a> IsExternalSearchIndexEnabled

**Description**: Select whether data can be synchronized with an external search index.<br />
**DisplayName**: Enable external search data syncing<br />
**LogicalName**: isexternalsearchindexenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsFiscalPeriodMonthBased"></a> IsFiscalPeriodMonthBased

**Description**: Indicates whether the fiscal period is displayed as the month number.<br />
**DisplayName**: Is Fiscal Period Monthly<br />
**LogicalName**: isfiscalperiodmonthbased<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsFolderAutoCreatedonSP"></a> IsFolderAutoCreatedonSP

**Description**: Select whether folders should be automatically created on SharePoint.<br />
**DisplayName**: Automatically create folders<br />
**LogicalName**: isfolderautocreatedonsp<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsFolderBasedTrackingEnabled"></a> IsFolderBasedTrackingEnabled

**Description**: Enable or disable folder based tracking for Server Side Sync.<br />
**DisplayName**: Is Folder Based Tracking Enabled<br />
**LogicalName**: isfolderbasedtrackingenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsFullTextSearchEnabled"></a> IsFullTextSearchEnabled

**Description**: Indicates whether full-text search for Quick Find entities should be enabled for the organization.<br />
**DisplayName**: Enable Full-text search for Quick Find<br />
**LogicalName**: isfulltextsearchenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_IsHierarchicalSecurityModelEnabled"></a> IsHierarchicalSecurityModelEnabled

**Description**: Enable Hierarchical Security Model<br />
**DisplayName**: Enable Hierarchical Security Model<br />
**LogicalName**: ishierarchicalsecuritymodelenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_IsMailboxForcedUnlockingEnabled"></a> IsMailboxForcedUnlockingEnabled

**Description**: Enable or disable forced unlocking for Server Side Sync mailboxes.<br />
**DisplayName**: Is Mailbox Forced Unlocking Enabled<br />
**LogicalName**: ismailboxforcedunlockingenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsMailboxInactiveBackoffEnabled"></a> IsMailboxInactiveBackoffEnabled

**Description**: Enable or disable mailbox keep alive for Server Side Sync.<br />
**DisplayName**: Is Mailbox Keep Alive Enabled<br />
**LogicalName**: ismailboxinactivebackoffenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsMobileClientOnDemandSyncEnabled"></a> IsMobileClientOnDemandSyncEnabled

**Description**: Information that specifies whether mobile client on demand sync is enabled.<br />
**DisplayName**: Is Mobile Client On Demand Sync enabled<br />
**LogicalName**: ismobileclientondemandsyncenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsMobileOfflineEnabled"></a> IsMobileOfflineEnabled

**Description**: Indicates whether the feature MobileOffline should be enabled for the organization.<br />
**DisplayName**: Enable MobileOffline for this Organization<br />
**LogicalName**: ismobileofflineenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsOfficeGraphEnabled"></a> IsOfficeGraphEnabled

**Description**: Indicates whether the feature OfficeGraph should be enabled for the organization.<br />
**DisplayName**: Enable OfficeGraph for this Organization<br />
**LogicalName**: isofficegraphenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsOneDriveEnabled"></a> IsOneDriveEnabled

**Description**: Indicates whether the feature One Drive should be enabled for the organization.<br />
**DisplayName**: Enable One Drive for this Organization<br />
**LogicalName**: isonedriveenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsPresenceEnabled"></a> IsPresenceEnabled

**Description**: Information on whether IM presence is enabled.<br />
**DisplayName**: Presence Enabled<br />
**LogicalName**: ispresenceenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_IsPreviewEnabledForActionCard"></a> IsPreviewEnabledForActionCard

**Description**: Indicates whether the Preview feature for Action Card should be enabled for the organization.<br />
**DisplayName**: Enable Preview Action Card feature for this Organization<br />
**LogicalName**: ispreviewenabledforactioncard<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsPreviewForAutoCaptureEnabled"></a> IsPreviewForAutoCaptureEnabled

**Description**: Indicates whether the feature Auto Capture should be enabled for the organization at Preview Settings.<br />
**DisplayName**: Enable Auto Capture for this Organization at Preview Settings<br />
**LogicalName**: ispreviewforautocaptureenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsPreviewForEmailMonitoringAllowed"></a> IsPreviewForEmailMonitoringAllowed

**Description**: Is Preview For Email Monitoring Allowed.<br />
**DisplayName**: Allows Preview For Email Monitoring<br />
**LogicalName**: ispreviewforemailmonitoringallowed<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_IsRelationshipInsightsEnabled"></a> IsRelationshipInsightsEnabled

**Description**: Indicates whether the feature Relationship Insights should be enabled for the organization.<br />
**DisplayName**: Enable Relationship Insights for this Organization<br />
**LogicalName**: isrelationshipinsightsenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsResourceBookingExchangeSyncEnabled"></a> IsResourceBookingExchangeSyncEnabled

**Description**: Indicates if the synchronization of user resource booking with Exchange is enabled at organization level.<br />
**DisplayName**: Resource booking synchronization enabled<br />
**LogicalName**: isresourcebookingexchangesyncenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsSOPIntegrationEnabled"></a> IsSOPIntegrationEnabled

**Description**: Enable sales order processing integration.<br />
**DisplayName**: Is Sales Order Integration Enabled<br />
**LogicalName**: issopintegrationenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsTextWrapEnabled"></a> IsTextWrapEnabled

**Description**: Information on whether text wrap is enabled.<br />
**DisplayName**: Enable Text Wrap<br />
**LogicalName**: istextwrapenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_IsUserAccessAuditEnabled"></a> IsUserAccessAuditEnabled

**Description**: Enable or disable auditing of user access.<br />
**DisplayName**: Is User Access Auditing Enabled<br />
**LogicalName**: isuseraccessauditenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_ISVIntegrationCode"></a> ISVIntegrationCode

**Description**: Indicates whether loading of Microsoft Dynamics 365 in a browser window that does not have address, tool, and menu bars is enabled.<br />
**DisplayName**: ISV Integration Mode<br />
**LogicalName**: isvintegrationcode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: None
- **Value**: 1 **Label**: Web
- **Value**: 2 **Label**: Outlook Workstation Client
- **Value**: 3 **Label**: Web; Outlook Workstation Client
- **Value**: 4 **Label**: Outlook Laptop Client
- **Value**: 5 **Label**: Web; Outlook Laptop Client
- **Value**: 6 **Label**: Outlook
- **Value**: 7 **Label**: All



### <a name="BKMK_KaPrefix"></a> KaPrefix

**Description**: Type the prefix to use for all knowledge articles in Microsoft Dynamics 365.<br />
**DisplayName**: Knowledge Article Prefix<br />
**LogicalName**: kaprefix<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 20


### <a name="BKMK_KbPrefix"></a> KbPrefix

**Description**: Prefix to use for all articles in Microsoft Dynamics 365.<br />
**DisplayName**: Article Prefix<br />
**LogicalName**: kbprefix<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 20


### <a name="BKMK_KMSettings"></a> KMSettings

**Description**: XML string containing the Knowledge Management settings that are applied in Knowledge Management Wizard.<br />
**DisplayName**: Knowledge Management Settings<br />
**LogicalName**: kmsettings<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_LanguageCode"></a> LanguageCode

**Description**: Preferred language for the organization.<br />
**DisplayName**: Language<br />
**LogicalName**: languagecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: Locale<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_LocaleId"></a> LocaleId

**Description**: Unique identifier of the locale of the organization.<br />
**DisplayName**: Locale<br />
**LogicalName**: localeid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: Locale<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_LongDateFormatCode"></a> LongDateFormatCode

**Description**: Information that specifies how the Long Date format is displayed in Microsoft Dynamics 365.<br />
**DisplayName**: Long Date Format<br />
**LogicalName**: longdateformatcode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_MailboxIntermittentIssueMinRange"></a> MailboxIntermittentIssueMinRange

**Description**: Lower Threshold For Mailbox Intermittent Issue.<br />
**DisplayName**: Lower Threshold For Mailbox Intermittent Issue<br />
**LogicalName**: mailboxintermittentissueminrange<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_MailboxPermanentIssueMinRange"></a> MailboxPermanentIssueMinRange

**Description**: Lower Threshold For Mailbox Permanent Issue.<br />
**DisplayName**: Lower Threshold For Mailbox Permanent Issue.<br />
**LogicalName**: mailboxpermanentissueminrange<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_MaxActionStepsInBPF"></a> MaxActionStepsInBPF

**Description**: Maximum number of actionsteps allowed in a BPF<br />
**DisplayName**: Maximum number of actionsteps allowed in a BPF<br />
**LogicalName**: maxactionstepsinbpf<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 100<br />
**MinValue**: 0


### <a name="BKMK_MaxAppointmentDurationDays"></a> MaxAppointmentDurationDays

**Description**: Maximum number of days an appointment can last.<br />
**DisplayName**: Max Appointment Duration<br />
**LogicalName**: maxappointmentdurationdays<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_MaxConditionsForMobileOfflineFilters"></a> MaxConditionsForMobileOfflineFilters

**Description**: Maximum number of conditions allowed for mobile offline filters<br />
**DisplayName**: Maximum number of conditions allowed for mobile offline filters<br />
**LogicalName**: maxconditionsformobileofflinefilters<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_MaxDepthForHierarchicalSecurityModel"></a> MaxDepthForHierarchicalSecurityModel

**Description**: Maximum depth for hierarchy security propagation.<br />
**DisplayName**: Maximum depth for hierarchy security propagation.<br />
**LogicalName**: maxdepthforhierarchicalsecuritymodel<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_MaxFolderBasedTrackingMappings"></a> MaxFolderBasedTrackingMappings

**Description**: Maximum number of Folder Based Tracking mappings user can add<br />
**DisplayName**: Max Folder Based Tracking Mappings<br />
**LogicalName**: maxfolderbasedtrackingmappings<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 25<br />
**MinValue**: 1


### <a name="BKMK_MaximumActiveBusinessProcessFlowsAllowedPerEntity"></a> MaximumActiveBusinessProcessFlowsAllowedPerEntity

**Description**: Maximum number of active business process flows allowed per entity<br />
**DisplayName**: Maximum active business process flows per entity<br />
**LogicalName**: maximumactivebusinessprocessflowsallowedperentity<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 1


### <a name="BKMK_MaximumDynamicPropertiesAllowed"></a> MaximumDynamicPropertiesAllowed

**Description**: Restrict the maximum number of product properties for a product family/bundle<br />
**DisplayName**: Product Properties Item Limit<br />
**LogicalName**: maximumdynamicpropertiesallowed<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_MaximumEntitiesWithActiveSLA"></a> MaximumEntitiesWithActiveSLA

**Description**: Maximum number of active SLA allowed per entity in online<br />
**DisplayName**: Maximum number of active SLA allowed per entity in online<br />
**LogicalName**: maximumentitieswithactivesla<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_MaximumSLAKPIPerEntityWithActiveSLA"></a> MaximumSLAKPIPerEntityWithActiveSLA

**Description**: Maximum number of SLA KPI per active SLA allowed for entity in online<br />
**DisplayName**: Maximum number of active SLA KPI allowed per entity in online<br />
**LogicalName**: maximumslakpiperentitywithactivesla<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_MaximumTrackingNumber"></a> MaximumTrackingNumber

**Description**: Maximum tracking number before recycling takes place.<br />
**DisplayName**: Max Tracking Number<br />
**LogicalName**: maximumtrackingnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_MaxProductsInBundle"></a> MaxProductsInBundle

**Description**: Restrict the maximum no of items in a bundle<br />
**DisplayName**: Bundle Item Limit<br />
**LogicalName**: maxproductsinbundle<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_MaxRecordsForExportToExcel"></a> MaxRecordsForExportToExcel

**Description**: Maximum number of records that will be exported to a static Microsoft Office Excel worksheet when exporting from the grid.<br />
**DisplayName**: Max Records For Excel Export<br />
**LogicalName**: maxrecordsforexporttoexcel<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_MaxRecordsForLookupFilters"></a> MaxRecordsForLookupFilters

**Description**: Maximum number of lookup and picklist records that can be selected by user for filtering.<br />
**DisplayName**: Max Records Filter Selection<br />
**LogicalName**: maxrecordsforlookupfilters<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_MaxUploadFileSize"></a> MaxUploadFileSize

**Description**: Maximum allowed size of an attachment.<br />
**DisplayName**: Max Upload File Size<br />
**LogicalName**: maxuploadfilesize<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_MicrosoftFlowEnvironment"></a> MicrosoftFlowEnvironment

**Description**: Environment selected for Integration with Microsoft Flow<br />
**DisplayName**: Environment selected for Integration with Microsoft Flow<br />
**LogicalName**: microsoftflowenvironment<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_MinAddressBookSyncInterval"></a> MinAddressBookSyncInterval

**Description**: Normal polling frequency used for address book synchronization in Microsoft Office Outlook.<br />
**DisplayName**: Min Address Synchronization Frequency<br />
**LogicalName**: minaddressbooksyncinterval<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_MinOfflineSyncInterval"></a> MinOfflineSyncInterval

**Description**: Normal polling frequency used for background offline synchronization in Microsoft Office Outlook.<br />
**DisplayName**: Min Offline Synchronization Frequency<br />
**LogicalName**: minofflinesyncinterval<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_MinOutlookSyncInterval"></a> MinOutlookSyncInterval

**Description**: Minimum allowed time between scheduled Outlook synchronizations.<br />
**DisplayName**: Min Synchronization Frequency<br />
**LogicalName**: minoutlooksyncinterval<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_MobileOfflineSyncInterval"></a> MobileOfflineSyncInterval

**Description**: Sync interval for mobile offline.<br />
**DisplayName**: Sync interval for mobile offline.<br />
**LogicalName**: mobileofflinesyncinterval<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_Name"></a> Name

**Description**: Name of the organization. The name is set when Microsoft CRM is installed and should not be changed.<br />
**DisplayName**: Organization Name<br />
**LogicalName**: name<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_NegativeCurrencyFormatCode"></a> NegativeCurrencyFormatCode

**Description**: Information that specifies how negative currency numbers are displayed throughout Microsoft Dynamics 365.<br />
**DisplayName**: Negative Currency Format<br />
**LogicalName**: negativecurrencyformatcode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_NegativeFormatCode"></a> NegativeFormatCode

**Description**: Information that specifies how negative numbers are displayed throughout Microsoft CRM.<br />
**DisplayName**: Negative Format<br />
**LogicalName**: negativeformatcode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Brackets
- **Value**: 1 **Label**: Dash
- **Value**: 2 **Label**: Dash plus Space
- **Value**: 3 **Label**: Trailing Dash
- **Value**: 4 **Label**: Space plus Trailing Dash



### <a name="BKMK_NextTrackingNumber"></a> NextTrackingNumber

**Description**: Next token to be placed on the subject line of an email message.<br />
**DisplayName**: Next Tracking Number<br />
**LogicalName**: nexttrackingnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_NotifyMailboxOwnerOfEmailServerLevelAlerts"></a> NotifyMailboxOwnerOfEmailServerLevelAlerts

**Description**: Indicates whether mailbox owners will be notified of email server profile level alerts.<br />
**DisplayName**: Notify Mailbox Owner Of Email Server Level Alerts<br />
**LogicalName**: notifymailboxownerofemailserverlevelalerts<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_NumberFormat"></a> NumberFormat

**Description**: Specification of how numbers are displayed throughout Microsoft CRM.<br />
**DisplayName**: Number Format<br />
**LogicalName**: numberformat<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2


### <a name="BKMK_NumberGroupFormat"></a> NumberGroupFormat

**Description**: Specifies how numbers are grouped in Microsoft Dynamics 365.<br />
**DisplayName**: Number Grouping Format<br />
**LogicalName**: numbergroupformat<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_NumberSeparator"></a> NumberSeparator

**Description**: Symbol used for number separation in Microsoft Dynamics 365.<br />
**DisplayName**: Number Separator<br />
**LogicalName**: numberseparator<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 5


### <a name="BKMK_OfficeAppsAutoDeploymentEnabled"></a> OfficeAppsAutoDeploymentEnabled

**Description**: Indicates whether the Office Apps auto deployment is enabled for the organization.<br />
**DisplayName**: Enable Office Apps Auto Deployment for this Organization<br />
**LogicalName**: officeappsautodeploymentenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_OfficeGraphDelveUrl"></a> OfficeGraphDelveUrl

**Description**: The url to open the Delve for the organization.<br />
**DisplayName**: The url to open the Delve<br />
**LogicalName**: officegraphdelveurl<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1000


### <a name="BKMK_OOBPriceCalculationEnabled"></a> OOBPriceCalculationEnabled

**Description**: Enable OOB pricing calculation logic for Opportunity, Quote, Order and Invoice entities.<br />
**DisplayName**: Enable OOB Price calculation<br />
**LogicalName**: oobpricecalculationenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_OrderPrefix"></a> OrderPrefix

**Description**: Prefix to use for all orders throughout Microsoft Dynamics 365.<br />
**DisplayName**: Order Prefix<br />
**LogicalName**: orderprefix<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 20


### <a name="BKMK_OrgDbOrgSettings"></a> OrgDbOrgSettings

**Description**: Organization settings stored in Organization Database.<br />
**DisplayName**: Organization Database Organization Settings<br />
**LogicalName**: orgdborgsettings<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_OrgInsightsEnabled"></a> OrgInsightsEnabled

**Description**: Select whether to turn on OrgInsights for the organization.<br />
**DisplayName**: Enable OrgInsights for this Organization<br />
**LogicalName**: orginsightsenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_PastExpansionWindow"></a> PastExpansionWindow

**Description**: Specifies the maximum number of months in past for which the recurring activities can be created.<br />
**DisplayName**: Past Expansion Window<br />
**LogicalName**: pastexpansionwindow<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 120<br />
**MinValue**: 1


### <a name="BKMK_Picture"></a> Picture

**Description**: For internal use only.<br />
**DisplayName**: Picture<br />
**LogicalName**: picture<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_PinpointLanguageCode"></a> PinpointLanguageCode

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: pinpointlanguagecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Integer<br />
**Format**: Locale<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_PluginTraceLogSetting"></a> PluginTraceLogSetting

**Description**: Plug-in Trace Log Setting for the Organization.<br />
**DisplayName**: Plug-in Trace Log Setting<br />
**LogicalName**: plugintracelogsetting<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Off
- **Value**: 1 **Label**: Exception
- **Value**: 2 **Label**: All



### <a name="BKMK_PMDesignator"></a> PMDesignator

**Description**: PM designator to use throughout Microsoft Dynamics 365.<br />
**DisplayName**: PM Designator<br />
**LogicalName**: pmdesignator<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 25


### <a name="BKMK_PostMessageWhitelistDomains"></a> PostMessageWhitelistDomains

**Description**: For internal use only.<br />
**DisplayName**: For internal use only.<br />
**LogicalName**: postmessagewhitelistdomains<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 500


### <a name="BKMK_PowerBiFeatureEnabled"></a> PowerBiFeatureEnabled

**Description**: Indicates whether the Power BI feature should be enabled for the organization.<br />
**DisplayName**: Enable Power BI feature for this Organization<br />
**LogicalName**: powerbifeatureenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Enable
- **FalseOption Value**: 0 **Label**: Disable

**DefaultValue**: False


### <a name="BKMK_PricingDecimalPrecision"></a> PricingDecimalPrecision

**Description**: Number of decimal places that can be used for prices.<br />
**DisplayName**: Pricing Decimal Precision<br />
**LogicalName**: pricingdecimalprecision<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 4<br />
**MinValue**: 0


### <a name="BKMK_PrivacyStatementUrl"></a> PrivacyStatementUrl

**Description**: Privacy Statement URL<br />
**DisplayName**: Privacy Statement URL<br />
**LogicalName**: privacystatementurl<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 500


### <a name="BKMK_PrivilegeUserGroupId"></a> PrivilegeUserGroupId

**Description**: Unique identifier of the default privilege for users in the organization.<br />
**DisplayName**: Privilege User Group<br />
**LogicalName**: privilegeusergroupid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_PrivReportingGroupId"></a> PrivReportingGroupId

**Description**: For internal use only.<br />
**DisplayName**: Privilege Reporting Group<br />
**LogicalName**: privreportinggroupid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_PrivReportingGroupName"></a> PrivReportingGroupName

**Description**: For internal use only.<br />
**DisplayName**: Privilege Reporting Group Name<br />
**LogicalName**: privreportinggroupname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_ProductRecommendationsEnabled"></a> ProductRecommendationsEnabled

**Description**: Select whether to turn on product recommendations for the organization.<br />
**DisplayName**: Enable Product Recommendations for this Organization<br />
**LogicalName**: productrecommendationsenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_QuickFindRecordLimitEnabled"></a> QuickFindRecordLimitEnabled

**Description**: Indicates whether a quick find record limit should be enabled for this organization (allows for faster Quick Find queries but prevents overly broad searches).<br />
**DisplayName**: Quick Find Record Limit Enabled<br />
**LogicalName**: quickfindrecordlimitenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_QuotePrefix"></a> QuotePrefix

**Description**: Prefix to use for all quotes throughout Microsoft Dynamics 365.<br />
**DisplayName**: Quote Prefix<br />
**LogicalName**: quoteprefix<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 20


### <a name="BKMK_RecurrenceDefaultNumberOfOccurrences"></a> RecurrenceDefaultNumberOfOccurrences

**Description**: Specifies the default value for number of occurrences field in the recurrence dialog.<br />
**DisplayName**: Recurrence Default Number of Occurrences<br />
**LogicalName**: recurrencedefaultnumberofoccurrences<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 999<br />
**MinValue**: 1


### <a name="BKMK_RecurrenceExpansionJobBatchInterval"></a> RecurrenceExpansionJobBatchInterval

**Description**: Specifies the interval (in seconds) for pausing expansion job.<br />
**DisplayName**: Recurrence Expansion Job Batch Interval<br />
**LogicalName**: recurrenceexpansionjobbatchinterval<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_RecurrenceExpansionJobBatchSize"></a> RecurrenceExpansionJobBatchSize

**Description**: Specifies the value for number of instances created in on demand job in one shot.<br />
**DisplayName**: Recurrence Expansion On Demand Job Batch Size<br />
**LogicalName**: recurrenceexpansionjobbatchsize<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_RecurrenceExpansionSynchCreateMax"></a> RecurrenceExpansionSynchCreateMax

**Description**: Specifies the maximum number of instances to be created synchronously after creating a recurring appointment.<br />
**DisplayName**: Recurrence Expansion Synchronization Create Maximum<br />
**LogicalName**: recurrenceexpansionsynchcreatemax<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000<br />
**MinValue**: 1


### <a name="BKMK_ReferenceSiteMapXml"></a> ReferenceSiteMapXml

**Description**: XML string that defines the navigation structure for the application. This is the site map from the previously upgraded build and is used in a 3-way merge during upgrade.<br />
**DisplayName**: Reference SiteMap XML<br />
**LogicalName**: referencesitemapxml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_RenderSecureIFrameForEmail"></a> RenderSecureIFrameForEmail

**Description**: Flag to render the body of email in the Web form in an IFRAME with the security='restricted' attribute set. This is additional security but can cause a credentials prompt.<br />
**DisplayName**: Render Secure Frame For Email<br />
**LogicalName**: rendersecureiframeforemail<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_ReportingGroupId"></a> ReportingGroupId

**Description**: For internal use only.<br />
**DisplayName**: Reporting Group<br />
**LogicalName**: reportinggroupid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ReportingGroupName"></a> ReportingGroupName

**Description**: For internal use only.<br />
**DisplayName**: Reporting Group Name<br />
**LogicalName**: reportinggroupname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_ReportScriptErrors"></a> ReportScriptErrors

**Description**: Picklist for selecting the organization preference for reporting scripting errors.<br />
**DisplayName**: Report Script Errors<br />
**LogicalName**: reportscripterrors<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: No preference for sending an error report to Microsoft about Microsoft Dynamics 365
- **Value**: 1 **Label**: Ask me for permission to send an error report to Microsoft
- **Value**: 2 **Label**: Automatically send an error report to Microsoft without asking me for permission
- **Value**: 3 **Label**: Never send an error report to Microsoft about Microsoft Dynamics 365



### <a name="BKMK_RequireApprovalForQueueEmail"></a> RequireApprovalForQueueEmail

**Description**: Indicates whether Send As Other User privilege is enabled.<br />
**DisplayName**: Is Approval For Queue Email Required<br />
**LogicalName**: requireapprovalforqueueemail<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_RequireApprovalForUserEmail"></a> RequireApprovalForUserEmail

**Description**: Indicates whether Send As Other User privilege is enabled.<br />
**DisplayName**: Is Approval For User Email Required<br />
**LogicalName**: requireapprovalforuseremail<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_ResolveSimilarUnresolvedEmailAddress"></a> ResolveSimilarUnresolvedEmailAddress

**Description**: Apply same email address to all unresolved matches when you manually resolve it for one<br />
**DisplayName**: Apply same email address to all unresolved matches when you manually resolve it for one<br />
**LogicalName**: resolvesimilarunresolvedemailaddress<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_RestrictStatusUpdate"></a> RestrictStatusUpdate

**Description**: Flag to restrict Update on incident.<br />
**DisplayName**: Restrict Status Update<br />
**LogicalName**: restrictstatusupdate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_RiErrorStatus"></a> RiErrorStatus

**Description**: Error status of Relationship Insights provisioning.<br />
**DisplayName**: Error status of Relationship Insights provisioning.<br />
**LogicalName**: rierrorstatus<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_SampleDataImportId"></a> SampleDataImportId

**Description**: Unique identifier of the sample data import job.<br />
**DisplayName**: Sample Data Import<br />
**LogicalName**: sampledataimportid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SchemaNamePrefix"></a> SchemaNamePrefix

**Description**: Prefix used for custom entities and attributes.<br />
**DisplayName**: Customization Name Prefix<br />
**LogicalName**: schemanameprefix<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 8


### <a name="BKMK_ServeStaticResourcesFromAzureCDN"></a> ServeStaticResourcesFromAzureCDN

**Description**: Serve Static Content From CDN<br />
**DisplayName**: Serve Static Content From CDN<br />
**LogicalName**: servestaticresourcesfromazurecdn<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_SessionTimeoutEnabled"></a> SessionTimeoutEnabled

**Description**: Information that specifies whether session timeout is enabled<br />
**DisplayName**: Session timeout enabled<br />
**LogicalName**: sessiontimeoutenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_SessionTimeoutInMins"></a> SessionTimeoutInMins

**Description**: Session timeout in minutes<br />
**DisplayName**: Session timeout in minutes<br />
**LogicalName**: sessiontimeoutinmins<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_SessionTimeoutReminderInMins"></a> SessionTimeoutReminderInMins

**Description**: Session timeout reminder in minutes<br />
**DisplayName**: Session timeout reminder in minutes<br />
**LogicalName**: sessiontimeoutreminderinmins<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_SharePointDeploymentType"></a> SharePointDeploymentType

**Description**: Indicates which SharePoint deployment type is configured for Server to Server. (Online or On-Premises)<br />
**DisplayName**: Choose SharePoint Deployment Type<br />
**LogicalName**: sharepointdeploymenttype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Online
- **Value**: 1 **Label**: On-Premises



### <a name="BKMK_ShareToPreviousOwnerOnAssign"></a> ShareToPreviousOwnerOnAssign

**Description**: Information that specifies whether to share to previous owner on assign.<br />
**DisplayName**: Share To Previous Owner On Assign<br />
**LogicalName**: sharetopreviousowneronassign<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_ShowKBArticleDeprecationNotification"></a> ShowKBArticleDeprecationNotification

**Description**: Select whether to display a KB article deprecation notification to the user.<br />
**DisplayName**: Show KBArticle deprecation message to user<br />
**LogicalName**: showkbarticledeprecationnotification<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_ShowWeekNumber"></a> ShowWeekNumber

**Description**: Information that specifies whether to display the week number in calendar displays throughout Microsoft CRM.<br />
**DisplayName**: Show Week Number<br />
**LogicalName**: showweeknumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_SignupOutlookDownloadFWLink"></a> SignupOutlookDownloadFWLink

**Description**: CRM for Outlook Download URL<br />
**DisplayName**: CRMForOutlookDownloadURL<br />
**LogicalName**: signupoutlookdownloadfwlink<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_SiteMapXml"></a> SiteMapXml

**Description**: XML string that defines the navigation structure for the application.<br />
**DisplayName**: SiteMap XML<br />
**LogicalName**: sitemapxml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_SlaPauseStates"></a> SlaPauseStates

**Description**: Contains the on hold case status values.<br />
**DisplayName**: SLA pause states<br />
**LogicalName**: slapausestates<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_SocialInsightsEnabled"></a> SocialInsightsEnabled

**Description**: Flag for whether the organization is using Social Insights.<br />
**DisplayName**: Social Insights Enabled<br />
**LogicalName**: socialinsightsenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_SocialInsightsInstance"></a> SocialInsightsInstance

**Description**: Identifier for the Social Insights instance for the organization.<br />
**DisplayName**: Social Insights instance identifier<br />
**LogicalName**: socialinsightsinstance<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2048


### <a name="BKMK_SocialInsightsTermsAccepted"></a> SocialInsightsTermsAccepted

**Description**: Flag for whether the organization has accepted the Social Insights terms of use.<br />
**DisplayName**: Social Insights Terms of Use<br />
**LogicalName**: socialinsightstermsaccepted<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_SortId"></a> SortId

**Description**: For internal use only.<br />
**DisplayName**: Sort<br />
**LogicalName**: sortid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_SqlAccessGroupId"></a> SqlAccessGroupId

**Description**: For internal use only.<br />
**DisplayName**: SQL Access Group<br />
**LogicalName**: sqlaccessgroupid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SqlAccessGroupName"></a> SqlAccessGroupName

**Description**: For internal use only.<br />
**DisplayName**: SQL Access Group Name<br />
**LogicalName**: sqlaccessgroupname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_SQMEnabled"></a> SQMEnabled

**Description**: Setting for SQM data collection, 0 no, 1 yes enabled<br />
**DisplayName**: Is SQM Enabled<br />
**LogicalName**: sqmenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_SupportUserId"></a> SupportUserId

**Description**: Unique identifier of the support user for the organization.<br />
**DisplayName**: Support User<br />
**LogicalName**: supportuserid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SuppressSLA"></a> SuppressSLA

**Description**: Indicates whether SLA is suppressed.<br />
**DisplayName**: Is SLA suppressed<br />
**LogicalName**: suppresssla<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_SyncOptInSelection"></a> SyncOptInSelection

**Description**: Indicates the selection to use the Dynamics 365 azure sync framework or server side sync.<br />
**DisplayName**: Enable Dynamics 365 azure sync framework for this organization.<br />
**LogicalName**: syncoptinselection<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Enable
- **FalseOption Value**: 0 **Label**: Disable

**DefaultValue**: False


### <a name="BKMK_SyncOptInSelectionStatus"></a> SyncOptInSelectionStatus

**Description**: Indicates the status of the opt-in or opt-out operation for Dynamics 365 azure sync.<br />
**DisplayName**: Status of opt-in or opt-out operation for Dynamics 365 azure sync.<br />
**LogicalName**: syncoptinselectionstatus<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Processing
- **Value**: 2 **Label**: Passed
- **Value**: 3 **Label**: Failed



### <a name="BKMK_SystemUserId"></a> SystemUserId

**Description**: Unique identifier of the system user for the organization.<br />
**DisplayName**: System User<br />
**LogicalName**: systemuserid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_TagMaxAggressiveCycles"></a> TagMaxAggressiveCycles

**Description**: Maximum number of aggressive polling cycles executed for email auto-tagging when a new email is received.<br />
**DisplayName**: Auto-Tag Max Cycles<br />
**LogicalName**: tagmaxaggressivecycles<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: <br />
**MinValue**: 


### <a name="BKMK_TagPollingPeriod"></a> TagPollingPeriod

**Description**: Normal polling frequency used for email receive auto-tagging in outlook.<br />
**DisplayName**: Auto-Tag Interval<br />
**LogicalName**: tagpollingperiod<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_TaskBasedFlowEnabled"></a> TaskBasedFlowEnabled

**Description**: Select whether to turn on task flows for the organization.<br />
**DisplayName**: Enable Task Flow processes for this Organization<br />
**LogicalName**: taskbasedflowenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_TextAnalyticsEnabled"></a> TextAnalyticsEnabled

**Description**: Select whether to turn on text analytics for the organization.<br />
**DisplayName**: Enable Text Analytics for this Organization<br />
**LogicalName**: textanalyticsenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_TimeFormatCode"></a> TimeFormatCode

**Description**: Information that specifies how the time is displayed throughout Microsoft CRM.<br />
**DisplayName**: Time Format Code<br />
**LogicalName**: timeformatcode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:




### <a name="BKMK_TimeFormatString"></a> TimeFormatString

**Description**: Text for how time is displayed in Microsoft Dynamics 365.<br />
**DisplayName**: Time Format String<br />
**LogicalName**: timeformatstring<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 255


### <a name="BKMK_TimeSeparator"></a> TimeSeparator

**Description**: Text for how the time separator is displayed throughout Microsoft Dynamics 365.<br />
**DisplayName**: Time Separator<br />
**LogicalName**: timeseparator<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 5


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


### <a name="BKMK_TokenExpiry"></a> TokenExpiry

**Description**: Duration used for token expiration.<br />
**DisplayName**: Token Expiration Duration<br />
**LogicalName**: tokenexpiry<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: <br />
**MinValue**: 


### <a name="BKMK_TokenKey"></a> TokenKey

**Description**: Token key.<br />
**DisplayName**: Token Key<br />
**LogicalName**: tokenkey<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 90


### <a name="BKMK_TrackingPrefix"></a> TrackingPrefix

**Description**: History list of tracking token prefixes.<br />
**DisplayName**: Tracking Prefix<br />
**LogicalName**: trackingprefix<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_TrackingTokenIdBase"></a> TrackingTokenIdBase

**Description**: Base number used to provide separate tracking token identifiers to users belonging to different deployments.<br />
**DisplayName**: Tracking Token Base<br />
**LogicalName**: trackingtokenidbase<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_TrackingTokenIdDigits"></a> TrackingTokenIdDigits

**Description**: Number of digits used to represent a tracking token identifier.<br />
**DisplayName**: Tracking Token Digits<br />
**LogicalName**: trackingtokeniddigits<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: <br />
**MinValue**: 


### <a name="BKMK_UniqueSpecifierLength"></a> UniqueSpecifierLength

**Description**: Number of characters appended to invoice, quote, and order numbers.<br />
**DisplayName**: Unique String Length<br />
**LogicalName**: uniquespecifierlength<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 6<br />
**MinValue**: 4


### <a name="BKMK_UnresolveEmailAddressIfMultipleMatch"></a> UnresolveEmailAddressIfMultipleMatch

**Description**: Indicates whether email address should be unresolved if multiple matches are found<br />
**DisplayName**: Set To,cc,bcc fields as unresolved if multiple matches are found<br />
**LogicalName**: unresolveemailaddressifmultiplematch<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_UseInbuiltRuleForDefaultPricelistSelection"></a> UseInbuiltRuleForDefaultPricelistSelection

**Description**: Flag indicates whether to Use Inbuilt Rule For DefaultPricelist.<br />
**DisplayName**: Use Inbuilt Rule For Default Pricelist Selection<br />
**LogicalName**: useinbuiltrulefordefaultpricelistselection<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_UseLegacyRendering"></a> UseLegacyRendering

**Description**: Select whether to use legacy form rendering.<br />
**DisplayName**: Legacy Form Rendering<br />
**LogicalName**: uselegacyrendering<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_UsePositionHierarchy"></a> UsePositionHierarchy

**Description**: Use position hierarchy<br />
**DisplayName**: Use position hierarchy<br />
**LogicalName**: usepositionhierarchy<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_UserAccessAuditingInterval"></a> UserAccessAuditingInterval

**Description**: The interval at which user access is checked for auditing.<br />
**DisplayName**: User Authentication Auditing Interval<br />
**LogicalName**: useraccessauditinginterval<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_UseReadForm"></a> UseReadForm

**Description**: Indicates whether the read-optimized form should be enabled for this organization.<br />
**DisplayName**: Use Read-Optimized Form<br />
**LogicalName**: usereadform<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_UserGroupId"></a> UserGroupId

**Description**: Unique identifier of the default group of users in the organization.<br />
**DisplayName**: User Group<br />
**LogicalName**: usergroupid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_UseSkypeProtocol"></a> UseSkypeProtocol

**Description**: Indicates default protocol selected for organization.<br />
**DisplayName**: User Skype Protocol<br />
**LogicalName**: useskypeprotocol<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

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


### <a name="BKMK_WebResourceHash"></a> WebResourceHash

**Description**: Hash value of web resources.<br />
**DisplayName**: Web resource hash<br />
**LogicalName**: webresourcehash<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_WeekStartDayCode"></a> WeekStartDayCode

**Description**: Designated first day of the week throughout Microsoft Dynamics 365.<br />
**DisplayName**: Week Start Day Code<br />
**LogicalName**: weekstartdaycode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:




### <a name="BKMK_WidgetProperties"></a> WidgetProperties

**Description**: For Internal use only.<br />
**DisplayName**: For Internal use only.<br />
**LogicalName**: widgetproperties<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_YammerGroupId"></a> YammerGroupId

**Description**: Denotes the Yammer group ID<br />
**DisplayName**: Yammer Group Id<br />
**LogicalName**: yammergroupid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_YammerNetworkPermalink"></a> YammerNetworkPermalink

**Description**: Denotes the Yammer network permalink<br />
**DisplayName**: Yammer Network Permalink<br />
**LogicalName**: yammernetworkpermalink<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_YammerOAuthAccessTokenExpired"></a> YammerOAuthAccessTokenExpired

**Description**: Denotes whether the OAuth access token for Yammer network has expired<br />
**DisplayName**: Yammer OAuth Access Token Expired<br />
**LogicalName**: yammeroauthaccesstokenexpired<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_YammerPostMethod"></a> YammerPostMethod

**Description**: Internal Use Only<br />
**DisplayName**: Internal Use Only<br />
**LogicalName**: yammerpostmethod<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Public
- **Value**: 1 **Label**: Private



### <a name="BKMK_YearStartWeekCode"></a> YearStartWeekCode

**Description**: Information that specifies how the first week of the year is specified in Microsoft Dynamics 365.<br />
**DisplayName**: Year Start Week Code<br />
**LogicalName**: yearstartweekcode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AcknowledgementTemplateIdName](#BKMK_AcknowledgementTemplateIdName)
- [BaseCurrencyIdName](#BKMK_BaseCurrencyIdName)
- [BaseCurrencyPrecision](#BKMK_BaseCurrencyPrecision)
- [BaseCurrencySymbol](#BKMK_BaseCurrencySymbol)
- [BaseISOCurrencyCode](#BKMK_BaseISOCurrencyCode)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [CurrentImportSequenceNumber](#BKMK_CurrentImportSequenceNumber)
- [CurrentParsedTableNumber](#BKMK_CurrentParsedTableNumber)
- [DaysSinceRecordLastModifiedMaxValue](#BKMK_DaysSinceRecordLastModifiedMaxValue)
- [DefaultEmailServerProfileIdName](#BKMK_DefaultEmailServerProfileIdName)
- [DefaultMobileOfflineProfileIdName](#BKMK_DefaultMobileOfflineProfileIdName)
- [DisabledReason](#BKMK_DisabledReason)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [FiscalSettingsUpdated](#BKMK_FiscalSettingsUpdated)
- [IsDisabled](#BKMK_IsDisabled)
- [MaxSupportedInternetExplorerVersion](#BKMK_MaxSupportedInternetExplorerVersion)
- [MaxVerboseLoggingMailbox](#BKMK_MaxVerboseLoggingMailbox)
- [MaxVerboseLoggingSyncCycles](#BKMK_MaxVerboseLoggingSyncCycles)
- [MetadataSyncLastTimeOfNeverExpiredDeletedObjects](#BKMK_MetadataSyncLastTimeOfNeverExpiredDeletedObjects)
- [MetadataSyncTimestamp](#BKMK_MetadataSyncTimestamp)
- [MobileOfflineMinLicenseProd](#BKMK_MobileOfflineMinLicenseProd)
- [MobileOfflineMinLicenseTrial](#BKMK_MobileOfflineMinLicenseTrial)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [NextCustomObjectTypeCode](#BKMK_NextCustomObjectTypeCode)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationState](#BKMK_OrganizationState)
- [ParsedTableColumnPrefix](#BKMK_ParsedTableColumnPrefix)
- [ParsedTablePrefix](#BKMK_ParsedTablePrefix)
- [V3CalloutConfigHash](#BKMK_V3CalloutConfigHash)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_AcknowledgementTemplateIdName"></a> AcknowledgementTemplateIdName

**Description**: Name of the template to be used for unsubscription acknowledgement.<br />
**DisplayName**: <br />
**LogicalName**: acknowledgementtemplateidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_BaseCurrencyIdName"></a> BaseCurrencyIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: basecurrencyidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_BaseCurrencyPrecision"></a> BaseCurrencyPrecision

**Description**: Number of decimal places that can be used for the base currency.<br />
**DisplayName**: Base Currency Precision<br />
**LogicalName**: basecurrencyprecision<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 4<br />
**MinValue**: 0


### <a name="BKMK_BaseCurrencySymbol"></a> BaseCurrencySymbol

**Description**: Symbol used for the base currency.<br />
**DisplayName**: Base Currency Symbol<br />
**LogicalName**: basecurrencysymbol<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 5


### <a name="BKMK_BaseISOCurrencyCode"></a> BaseISOCurrencyCode

**Description**: <br />
**DisplayName**: Base ISO Currency Code<br />
**LogicalName**: baseisocurrencycode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 5


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the organization.<br />
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

**Description**: Date and time when the organization was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the organization.<br />
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


### <a name="BKMK_CurrentImportSequenceNumber"></a> CurrentImportSequenceNumber

**Description**: Import sequence to use.<br />
**DisplayName**: Current Import Sequence Number<br />
**LogicalName**: currentimportsequencenumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_CurrentParsedTableNumber"></a> CurrentParsedTableNumber

**Description**: First parsed table number to use.<br />
**DisplayName**: Current Parsed Table Number<br />
**LogicalName**: currentparsedtablenumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_DaysSinceRecordLastModifiedMaxValue"></a> DaysSinceRecordLastModifiedMaxValue

**Description**: The maximum value for the Mobile Offline setting Days since record last modified<br />
**DisplayName**: Max value of Days since record last modified<br />
**LogicalName**: dayssincerecordlastmodifiedmaxvalue<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_DefaultEmailServerProfileIdName"></a> DefaultEmailServerProfileIdName

**Description**: Name of the email server profile to be used as default profile for the mailboxes.<br />
**DisplayName**: <br />
**LogicalName**: defaultemailserverprofileidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_DefaultMobileOfflineProfileIdName"></a> DefaultMobileOfflineProfileIdName

**Description**: Name of the default mobile offline profile to be used as default profile for mobile offline.<br />
**DisplayName**: <br />
**LogicalName**: defaultmobileofflineprofileidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_DisabledReason"></a> DisabledReason

**Description**: Reason for disabling the organization.<br />
**DisplayName**: Disabled Reason<br />
**LogicalName**: disabledreason<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 500


### <a name="BKMK_EntityImage_Timestamp"></a> EntityImage_Timestamp

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: entityimage_timestamp<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />


### <a name="BKMK_EntityImage_URL"></a> EntityImage_URL

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: entityimage_url<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Url<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_EntityImageId"></a> EntityImageId

**Description**: For internal use only.<br />
**DisplayName**: Entity Image Id<br />
**LogicalName**: entityimageid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_FiscalSettingsUpdated"></a> FiscalSettingsUpdated

**Description**: Information that specifies whether the fiscal settings have been updated.<br />
**DisplayName**: Is Fiscal Settings Updated<br />
**LogicalName**: fiscalsettingsupdated<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsDisabled"></a> IsDisabled

**Description**: Information that specifies whether the organization is disabled.<br />
**DisplayName**: Is Organization Disabled<br />
**LogicalName**: isdisabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_MaxSupportedInternetExplorerVersion"></a> MaxSupportedInternetExplorerVersion

**Description**: The maximum version of IE to run browser emulation for in Outlook client<br />
**DisplayName**: Max supported IE version<br />
**LogicalName**: maxsupportedinternetexplorerversion<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_MaxVerboseLoggingMailbox"></a> MaxVerboseLoggingMailbox

**Description**: Maximum number of mailboxes that can be toggled for verbose logging<br />
**DisplayName**: Max No Of Mailboxes To Enable For Verbose Logging<br />
**LogicalName**: maxverboseloggingmailbox<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_MaxVerboseLoggingSyncCycles"></a> MaxVerboseLoggingSyncCycles

**Description**: Maximum number of sync cycles for which verbose logging will be enabled by default<br />
**DisplayName**: Maximum number of sync cycles for which verbose logging will be enabled by default<br />
**LogicalName**: maxverboseloggingsynccycles<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_MetadataSyncLastTimeOfNeverExpiredDeletedObjects"></a> MetadataSyncLastTimeOfNeverExpiredDeletedObjects

**Description**: What is the last date/time where there are metadata tracking deleted objects that have never been outside of the expiration period.<br />
**DisplayName**: The last date/time for never expired metadata tracking deleted objects<br />
**LogicalName**: metadatasynclasttimeofneverexpireddeletedobjects<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_MetadataSyncTimestamp"></a> MetadataSyncTimestamp

**Description**: Contains the maximum version number for attributes used by metadata synchronization that have changed.<br />
**DisplayName**: Metadata sync version<br />
**LogicalName**: metadatasynctimestamp<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: SystemRequired<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />


### <a name="BKMK_MobileOfflineMinLicenseProd"></a> MobileOfflineMinLicenseProd

**Description**: Minimum number of user license required for mobile offline service by production/preview organization<br />
**DisplayName**: Minimum number of user license required for mobile offline service by production/preview organization<br />
**LogicalName**: mobileofflineminlicenseprod<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_MobileOfflineMinLicenseTrial"></a> MobileOfflineMinLicenseTrial

**Description**: Minimum number of user license required for mobile offline service by trial organization<br />
**DisplayName**: Minimum number of user license required for mobile offline service by trial organization<br />
**LogicalName**: mobileofflineminlicensetrial<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the organization.<br />
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
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the organization was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the organization.<br />
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


### <a name="BKMK_NextCustomObjectTypeCode"></a> NextCustomObjectTypeCode

**Description**: Next entity type code to use for custom entities.<br />
**DisplayName**: Next Entity Type Code<br />
**LogicalName**: nextcustomobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 10000


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization.<br />
**DisplayName**: Organization<br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_OrganizationState"></a> OrganizationState

**Description**: Indicates the organization lifecycle state<br />
**DisplayName**: Organization State<br />
**LogicalName**: organizationstate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Creating
- **Value**: 1 **Label**: Upgrading
- **Value**: 2 **Label**: Updating
- **Value**: 3 **Label**: Active



### <a name="BKMK_ParsedTableColumnPrefix"></a> ParsedTableColumnPrefix

**Description**: Prefix used for parsed table columns.<br />
**DisplayName**: Parsed Table Column Prefix<br />
**LogicalName**: parsedtablecolumnprefix<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 20


### <a name="BKMK_ParsedTablePrefix"></a> ParsedTablePrefix

**Description**: Prefix used for parsed tables.<br />
**DisplayName**: Parsed Table Prefix<br />
**LogicalName**: parsedtableprefix<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 20


### <a name="BKMK_V3CalloutConfigHash"></a> V3CalloutConfigHash

**Description**: Hash of the V3 callout configuration file.<br />
**DisplayName**: V3 Callout Hash<br />
**LogicalName**: v3calloutconfighash<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: Version number of the organization.<br />
**DisplayName**: Version Number<br />
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

- [organization_territories](#BKMK_organization_territories)
- [lk_principalobjectattributeaccess_organizationid](#BKMK_lk_principalobjectattributeaccess_organizationid)
- [organization_theme](#BKMK_organization_theme)
- [organization_UserMapping](#BKMK_organization_UserMapping)
- [organization_suggestioncardtemplate](#BKMK_organization_suggestioncardtemplate)
- [organization_metric](#BKMK_organization_metric)
- [organization_position](#BKMK_organization_position)
- [organization_officegraphdocument](#BKMK_organization_officegraphdocument)
- [organization_delveactionhub](#BKMK_organization_delveactionhub)
- [organization_recommendeddocument](#BKMK_organization_recommendeddocument)
- [organization_KnowledgeBaseRecord](#BKMK_organization_KnowledgeBaseRecord)
- [organization_translationprocess](#BKMK_organization_translationprocess)
- [organization_orginsightsmetric](#BKMK_organization_orginsightsmetric)
- [organization_navigationsetting](#BKMK_organization_navigationsetting)
- [organization_plugintype](#BKMK_organization_plugintype)
- [organization_azureserviceconnection](#BKMK_organization_azureserviceconnection)
- [organization_sdkmessageresponse](#BKMK_organization_sdkmessageresponse)
- [organization_business_unit_news_articles](#BKMK_organization_business_unit_news_articles)
- [organization_saved_query_visualizations](#BKMK_organization_saved_query_visualizations)
- [customcontrolresource_organization](#BKMK_customcontrolresource_organization)
- [organization_post](#BKMK_organization_post)
- [organization_PostComment](#BKMK_organization_PostComment)
- [organization_postlike](#BKMK_organization_postlike)
- [organization_importjob](#BKMK_organization_importjob)
- [organization_licenses](#BKMK_organization_licenses)
- [organization_expanderevent](#BKMK_organization_expanderevent)
- [organization_ribbon_customization](#BKMK_organization_ribbon_customization)
- [organization_queues](#BKMK_organization_queues)
- [organization_sdkmessageprocessingstepimage](#BKMK_organization_sdkmessageprocessingstepimage)
- [organization_savedorginsightsconfiguration](#BKMK_organization_savedorginsightsconfiguration)
- [organization_plugintypestatistic](#BKMK_organization_plugintypestatistic)
- [MobileOfflineProfileItemAssociation_organization](#BKMK_MobileOfflineProfileItemAssociation_organization)
- [organization_relationship_roles](#BKMK_organization_relationship_roles)
- [organization_appmodule](#BKMK_organization_appmodule)
- [organization_sdkmessagepair](#BKMK_organization_sdkmessagepair)
- [organization_kb_articles](#BKMK_organization_kb_articles)
- [organization_systemforms](#BKMK_organization_systemforms)
- [organization_appconfig](#BKMK_organization_appconfig)
- [organization_sdkmessagerequestfield](#BKMK_organization_sdkmessagerequestfield)
- [organization_connection_roles](#BKMK_organization_connection_roles)
- [customcontrol_organization](#BKMK_customcontrol_organization)
- [userentityinstancedata_organization](#BKMK_userentityinstancedata_organization)
- [organization_subjects](#BKMK_organization_subjects)
- [organization_calendars](#BKMK_organization_calendars)
- [organization_publisher](#BKMK_organization_publisher)
- [organization_queueitems](#BKMK_organization_queueitems)
- [organization_teams](#BKMK_organization_teams)
- [organization_advancedsimilarityrule](#BKMK_organization_advancedsimilarityrule)
- [organization_socialinsightsconfiguration](#BKMK_organization_socialinsightsconfiguration)
- [organization_entitymap](#BKMK_organization_entitymap)
- [channelproperty_organization](#BKMK_channelproperty_organization)
- [organization_entitydataprovider](#BKMK_organization_entitydataprovider)
- [organization_sharepointdocument](#BKMK_organization_sharepointdocument)
- [webresource_organization](#BKMK_webresource_organization)
- [organization_textanalyticsentitymapping](#BKMK_organization_textanalyticsentitymapping)
- [MobileOfflineProfile_organization](#BKMK_MobileOfflineProfile_organization)
- [organization_transactioncurrencies](#BKMK_organization_transactioncurrencies)
- [organization_expiredprocess](#BKMK_organization_expiredprocess)
- [organization_mailbox](#BKMK_organization_mailbox)
- [lk_dataperformance_organizationid](#BKMK_lk_dataperformance_organizationid)
- [organization_isvconfigs](#BKMK_organization_isvconfigs)
- [organization_sharepointdata](#BKMK_organization_sharepointdata)
- [offlinecommanddefinition_organization](#BKMK_offlinecommanddefinition_organization)
- [MobileOfflineProfileItem_organization](#BKMK_MobileOfflineProfileItem_organization)
- [organization_custom_displaystrings](#BKMK_organization_custom_displaystrings)
- [Organization_SyncErrors](#BKMK_Organization_SyncErrors)
- [channelpropertygroup_organization](#BKMK_channelpropertygroup_organization)
- [organization_sdkmessagerequest](#BKMK_organization_sdkmessagerequest)
- [Organization_AsyncOperations](#BKMK_Organization_AsyncOperations)
- [customcontroldefaultconfig_organization](#BKMK_customcontroldefaultconfig_organization)
- [organization_sitemap](#BKMK_organization_sitemap)
- [Organization_MailboxTrackingFolder](#BKMK_Organization_MailboxTrackingFolder)
- [organization_emailserverprofile](#BKMK_organization_emailserverprofile)
- [lk_organizationui_organizationid](#BKMK_lk_organizationui_organizationid)
- [organization_pluginassembly](#BKMK_organization_pluginassembly)
- [organization_mailboxstatistics](#BKMK_organization_mailboxstatistics)
- [organization_knowledgesearchmodel](#BKMK_organization_knowledgesearchmodel)
- [Organization_BulkDeleteFailures](#BKMK_Organization_BulkDeleteFailures)
- [lk_fieldsecurityprofile_organizationid](#BKMK_lk_fieldsecurityprofile_organizationid)
- [organization_sdkmessagefilter](#BKMK_organization_sdkmessagefilter)
- [organization_kb_article_templates](#BKMK_organization_kb_article_templates)
- [organization_roles](#BKMK_organization_roles)
- [organization_sdkmessageprocessingstepsecureconfig](#BKMK_organization_sdkmessageprocessingstepsecureconfig)
- [organization_entitydatasource](#BKMK_organization_entitydatasource)
- [organization_aciviewmapper](#BKMK_organization_aciviewmapper)
- [organization_system_users](#BKMK_organization_system_users)
- [languagelocale_organization](#BKMK_languagelocale_organization)
- [organization_business_units](#BKMK_organization_business_units)
- [organization_sdkmessageresponsefield](#BKMK_organization_sdkmessageresponsefield)
- [organization_attributemap](#BKMK_organization_attributemap)
- [organization_newprocess](#BKMK_organization_newprocess)
- [organization_hierarchyrules](#BKMK_organization_hierarchyrules)
- [organization_sdkmessageprocessingstep](#BKMK_organization_sdkmessageprocessingstep)
- [organization_RoutingRules](#BKMK_organization_RoutingRules)
- [organization_orginsightsnotification](#BKMK_organization_orginsightsnotification)
- [organization_appconfiginstance](#BKMK_organization_appconfiginstance)
- [organization_routingruleitems](#BKMK_organization_routingruleitems)
- [lk_documenttemplatebase_organization](#BKMK_lk_documenttemplatebase_organization)
- [organization_serviceendpoint](#BKMK_organization_serviceendpoint)
- [organization_sdkmessage](#BKMK_organization_sdkmessage)
- [organization_appconfigmaster](#BKMK_organization_appconfigmaster)
- [organization_saved_queries](#BKMK_organization_saved_queries)
- [organization_tracelog](#BKMK_organization_tracelog)
- [organization_solution](#BKMK_organization_solution)


### <a name="BKMK_organization_territories"></a> organization_territories

Same as territory entity [organization_territories](territory.md#BKMK_organization_territories) Many-To-One relationship.

**ReferencingEntity**: territory<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_territories<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_lk_principalobjectattributeaccess_organizationid"></a> lk_principalobjectattributeaccess_organizationid

Same as principalobjectattributeaccess entity [lk_principalobjectattributeaccess_organizationid](principalobjectattributeaccess.md#BKMK_lk_principalobjectattributeaccess_organizationid) Many-To-One relationship.

**ReferencingEntity**: principalobjectattributeaccess<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_principalobjectattributeaccess_organizationid<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_theme"></a> organization_theme

Same as theme entity [organization_theme](theme.md#BKMK_organization_theme) Many-To-One relationship.

**ReferencingEntity**: theme<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: organization_theme<br />
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


### <a name="BKMK_organization_UserMapping"></a> organization_UserMapping

Same as usermapping entity [organization_UserMapping](usermapping.md#BKMK_organization_UserMapping) Many-To-One relationship.

**ReferencingEntity**: usermapping<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: organization_UserMapping<br />
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


### <a name="BKMK_organization_suggestioncardtemplate"></a> organization_suggestioncardtemplate

Same as suggestioncardtemplate entity [organization_suggestioncardtemplate](suggestioncardtemplate.md#BKMK_organization_suggestioncardtemplate) Many-To-One relationship.

**ReferencingEntity**: suggestioncardtemplate<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: organization_suggestioncardtemplate<br />
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


### <a name="BKMK_organization_metric"></a> organization_metric

Same as metric entity [organization_metric](metric.md#BKMK_organization_metric) Many-To-One relationship.

**ReferencingEntity**: metric<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_metric<br />
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


### <a name="BKMK_organization_position"></a> organization_position

Same as position entity [organization_position](position.md#BKMK_organization_position) Many-To-One relationship.

**ReferencingEntity**: position<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: organization_position<br />
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


### <a name="BKMK_organization_officegraphdocument"></a> organization_officegraphdocument

Same as officegraphdocument entity [organization_officegraphdocument](officegraphdocument.md#BKMK_organization_officegraphdocument) Many-To-One relationship.

**ReferencingEntity**: officegraphdocument<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: organization_officegraphdocument<br />
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


### <a name="BKMK_organization_delveactionhub"></a> organization_delveactionhub

Same as delveactionhub entity [organization_delveactionhub](delveactionhub.md#BKMK_organization_delveactionhub) Many-To-One relationship.

**ReferencingEntity**: delveactionhub<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: organization_delveactionhub<br />
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


### <a name="BKMK_organization_recommendeddocument"></a> organization_recommendeddocument

Same as recommendeddocument entity [organization_recommendeddocument](recommendeddocument.md#BKMK_organization_recommendeddocument) Many-To-One relationship.

**ReferencingEntity**: recommendeddocument<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: organization_recommendeddocument<br />
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


### <a name="BKMK_organization_KnowledgeBaseRecord"></a> organization_KnowledgeBaseRecord

Same as knowledgebaserecord entity [organization_KnowledgeBaseRecord](knowledgebaserecord.md#BKMK_organization_KnowledgeBaseRecord) Many-To-One relationship.

**ReferencingEntity**: knowledgebaserecord<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: organization_KnowledgeBaseRecord<br />
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


### <a name="BKMK_organization_translationprocess"></a> organization_translationprocess

Same as translationprocess entity [organization_translationprocess](translationprocess.md#BKMK_organization_translationprocess) Many-To-One relationship.

**ReferencingEntity**: translationprocess<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: organization_translationprocess<br />
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


### <a name="BKMK_organization_orginsightsmetric"></a> organization_orginsightsmetric

Same as orginsightsmetric entity [organization_orginsightsmetric](orginsightsmetric.md#BKMK_organization_orginsightsmetric) Many-To-One relationship.

**ReferencingEntity**: orginsightsmetric<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_orginsightsmetric<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_navigationsetting"></a> organization_navigationsetting

Same as navigationsetting entity [organization_navigationsetting](navigationsetting.md#BKMK_organization_navigationsetting) Many-To-One relationship.

**ReferencingEntity**: navigationsetting<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_navigationsetting<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_plugintype"></a> organization_plugintype

Same as plugintype entity [organization_plugintype](plugintype.md#BKMK_organization_plugintype) Many-To-One relationship.

**ReferencingEntity**: plugintype<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_plugintype<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_azureserviceconnection"></a> organization_azureserviceconnection

Same as azureserviceconnection entity [organization_azureserviceconnection](azureserviceconnection.md#BKMK_organization_azureserviceconnection) Many-To-One relationship.

**ReferencingEntity**: azureserviceconnection<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_azureserviceconnection<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_sdkmessageresponse"></a> organization_sdkmessageresponse

Same as sdkmessageresponse entity [organization_sdkmessageresponse](sdkmessageresponse.md#BKMK_organization_sdkmessageresponse) Many-To-One relationship.

**ReferencingEntity**: sdkmessageresponse<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_sdkmessageresponse<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_business_unit_news_articles"></a> organization_business_unit_news_articles

Same as businessunitnewsarticle entity [organization_business_unit_news_articles](businessunitnewsarticle.md#BKMK_organization_business_unit_news_articles) Many-To-One relationship.

**ReferencingEntity**: businessunitnewsarticle<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_business_unit_news_articles<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_saved_query_visualizations"></a> organization_saved_query_visualizations

Same as savedqueryvisualization entity [organization_saved_query_visualizations](savedqueryvisualization.md#BKMK_organization_saved_query_visualizations) Many-To-One relationship.

**ReferencingEntity**: savedqueryvisualization<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_saved_query_visualizations<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_customcontrolresource_organization"></a> customcontrolresource_organization

Same as customcontrolresource entity [customcontrolresource_organization](customcontrolresource.md#BKMK_customcontrolresource_organization) Many-To-One relationship.

**ReferencingEntity**: customcontrolresource<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: customcontrolresource_organization<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_post"></a> organization_post

Same as post entity [organization_post](post.md#BKMK_organization_post) Many-To-One relationship.

**ReferencingEntity**: post<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_post<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_PostComment"></a> organization_PostComment

Same as postcomment entity [organization_PostComment](postcomment.md#BKMK_organization_PostComment) Many-To-One relationship.

**ReferencingEntity**: postcomment<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_PostComment<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_postlike"></a> organization_postlike

Same as postlike entity [organization_postlike](postlike.md#BKMK_organization_postlike) Many-To-One relationship.

**ReferencingEntity**: postlike<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_postlike<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_importjob"></a> organization_importjob

Same as importjob entity [organization_importjob](importjob.md#BKMK_organization_importjob) Many-To-One relationship.

**ReferencingEntity**: importjob<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_importjob<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_licenses"></a> organization_licenses

Same as license entity [organization_licenses](license.md#BKMK_organization_licenses) Many-To-One relationship.

**ReferencingEntity**: license<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_licenses<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_expanderevent"></a> organization_expanderevent

Same as expanderevent entity [organization_expanderevent](expanderevent.md#BKMK_organization_expanderevent) Many-To-One relationship.

**ReferencingEntity**: expanderevent<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_expanderevent<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_ribbon_customization"></a> organization_ribbon_customization

Same as ribboncustomization entity [organization_ribbon_customization](ribboncustomization.md#BKMK_organization_ribbon_customization) Many-To-One relationship.

**ReferencingEntity**: ribboncustomization<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_ribbon_customization<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_queues"></a> organization_queues

Same as queue entity [organization_queues](queue.md#BKMK_organization_queues) Many-To-One relationship.

**ReferencingEntity**: queue<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_queues<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_sdkmessageprocessingstepimage"></a> organization_sdkmessageprocessingstepimage

Same as sdkmessageprocessingstepimage entity [organization_sdkmessageprocessingstepimage](sdkmessageprocessingstepimage.md#BKMK_organization_sdkmessageprocessingstepimage) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstepimage<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_sdkmessageprocessingstepimage<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_savedorginsightsconfiguration"></a> organization_savedorginsightsconfiguration

Same as savedorginsightsconfiguration entity [organization_savedorginsightsconfiguration](savedorginsightsconfiguration.md#BKMK_organization_savedorginsightsconfiguration) Many-To-One relationship.

**ReferencingEntity**: savedorginsightsconfiguration<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_savedorginsightsconfiguration<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_plugintypestatistic"></a> organization_plugintypestatistic

Same as plugintypestatistic entity [organization_plugintypestatistic](plugintypestatistic.md#BKMK_organization_plugintypestatistic) Many-To-One relationship.

**ReferencingEntity**: plugintypestatistic<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_plugintypestatistic<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_MobileOfflineProfileItemAssociation_organization"></a> MobileOfflineProfileItemAssociation_organization

Same as mobileofflineprofileitemassociation entity [MobileOfflineProfileItemAssociation_organization](mobileofflineprofileitemassociation.md#BKMK_MobileOfflineProfileItemAssociation_organization) Many-To-One relationship.

**ReferencingEntity**: mobileofflineprofileitemassociation<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: MobileOfflineProfileItemAssociation_organization<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_relationship_roles"></a> organization_relationship_roles

Same as relationshiprole entity [organization_relationship_roles](relationshiprole.md#BKMK_organization_relationship_roles) Many-To-One relationship.

**ReferencingEntity**: relationshiprole<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_relationship_roles<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_appmodule"></a> organization_appmodule

Same as appmodule entity [organization_appmodule](appmodule.md#BKMK_organization_appmodule) Many-To-One relationship.

**ReferencingEntity**: appmodule<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_appmodule<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_sdkmessagepair"></a> organization_sdkmessagepair

Same as sdkmessagepair entity [organization_sdkmessagepair](sdkmessagepair.md#BKMK_organization_sdkmessagepair) Many-To-One relationship.

**ReferencingEntity**: sdkmessagepair<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_sdkmessagepair<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_kb_articles"></a> organization_kb_articles

Same as kbarticle entity [organization_kb_articles](kbarticle.md#BKMK_organization_kb_articles) Many-To-One relationship.

**ReferencingEntity**: kbarticle<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_kb_articles<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_systemforms"></a> organization_systemforms

Same as systemform entity [organization_systemforms](systemform.md#BKMK_organization_systemforms) Many-To-One relationship.

**ReferencingEntity**: systemform<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_systemforms<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_appconfig"></a> organization_appconfig

Same as appconfig entity [organization_appconfig](appconfig.md#BKMK_organization_appconfig) Many-To-One relationship.

**ReferencingEntity**: appconfig<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_appconfig<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_sdkmessagerequestfield"></a> organization_sdkmessagerequestfield

Same as sdkmessagerequestfield entity [organization_sdkmessagerequestfield](sdkmessagerequestfield.md#BKMK_organization_sdkmessagerequestfield) Many-To-One relationship.

**ReferencingEntity**: sdkmessagerequestfield<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_sdkmessagerequestfield<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_connection_roles"></a> organization_connection_roles

Same as connectionrole entity [organization_connection_roles](connectionrole.md#BKMK_organization_connection_roles) Many-To-One relationship.

**ReferencingEntity**: connectionrole<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_connection_roles<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_customcontrol_organization"></a> customcontrol_organization

Same as customcontrol entity [customcontrol_organization](customcontrol.md#BKMK_customcontrol_organization) Many-To-One relationship.

**ReferencingEntity**: customcontrol<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: customcontrol_organization<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_userentityinstancedata_organization"></a> userentityinstancedata_organization

Same as userentityinstancedata entity [userentityinstancedata_organization](userentityinstancedata.md#BKMK_userentityinstancedata_organization) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_organization<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_subjects"></a> organization_subjects

Same as subject entity [organization_subjects](subject.md#BKMK_organization_subjects) Many-To-One relationship.

**ReferencingEntity**: subject<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_subjects<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_calendars"></a> organization_calendars

Same as calendar entity [organization_calendars](calendar.md#BKMK_organization_calendars) Many-To-One relationship.

**ReferencingEntity**: calendar<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_calendars<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_publisher"></a> organization_publisher

Same as publisher entity [organization_publisher](publisher.md#BKMK_organization_publisher) Many-To-One relationship.

**ReferencingEntity**: publisher<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_publisher<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_queueitems"></a> organization_queueitems

Same as queueitem entity [organization_queueitems](queueitem.md#BKMK_organization_queueitems) Many-To-One relationship.

**ReferencingEntity**: queueitem<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_queueitems<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_teams"></a> organization_teams

Same as team entity [organization_teams](team.md#BKMK_organization_teams) Many-To-One relationship.

**ReferencingEntity**: team<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_teams<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_advancedsimilarityrule"></a> organization_advancedsimilarityrule

Same as advancedsimilarityrule entity [organization_advancedsimilarityrule](advancedsimilarityrule.md#BKMK_organization_advancedsimilarityrule) Many-To-One relationship.

**ReferencingEntity**: advancedsimilarityrule<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_advancedsimilarityrule<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_socialinsightsconfiguration"></a> organization_socialinsightsconfiguration

Same as socialinsightsconfiguration entity [organization_socialinsightsconfiguration](socialinsightsconfiguration.md#BKMK_organization_socialinsightsconfiguration) Many-To-One relationship.

**ReferencingEntity**: socialinsightsconfiguration<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_socialinsightsconfiguration<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_entitymap"></a> organization_entitymap

Same as entitymap entity [organization_entitymap](entitymap.md#BKMK_organization_entitymap) Many-To-One relationship.

**ReferencingEntity**: entitymap<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_entitymap<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_channelproperty_organization"></a> channelproperty_organization

Same as channelproperty entity [channelproperty_organization](channelproperty.md#BKMK_channelproperty_organization) Many-To-One relationship.

**ReferencingEntity**: channelproperty<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: channelproperty_organization<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_entitydataprovider"></a> organization_entitydataprovider

Same as entitydataprovider entity [organization_entitydataprovider](entitydataprovider.md#BKMK_organization_entitydataprovider) Many-To-One relationship.

**ReferencingEntity**: entitydataprovider<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_entitydataprovider<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_sharepointdocument"></a> organization_sharepointdocument

Same as sharepointdocument entity [organization_sharepointdocument](sharepointdocument.md#BKMK_organization_sharepointdocument) Many-To-One relationship.

**ReferencingEntity**: sharepointdocument<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_sharepointdocument<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_webresource_organization"></a> webresource_organization

Same as webresource entity [webresource_organization](webresource.md#BKMK_webresource_organization) Many-To-One relationship.

**ReferencingEntity**: webresource<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: webresource_organization<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_textanalyticsentitymapping"></a> organization_textanalyticsentitymapping

Same as textanalyticsentitymapping entity [organization_textanalyticsentitymapping](textanalyticsentitymapping.md#BKMK_organization_textanalyticsentitymapping) Many-To-One relationship.

**ReferencingEntity**: textanalyticsentitymapping<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_textanalyticsentitymapping<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_MobileOfflineProfile_organization"></a> MobileOfflineProfile_organization

Same as mobileofflineprofile entity [MobileOfflineProfile_organization](mobileofflineprofile.md#BKMK_MobileOfflineProfile_organization) Many-To-One relationship.

**ReferencingEntity**: mobileofflineprofile<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: MobileOfflineProfile_organization<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_transactioncurrencies"></a> organization_transactioncurrencies

Same as transactioncurrency entity [organization_transactioncurrencies](transactioncurrency.md#BKMK_organization_transactioncurrencies) Many-To-One relationship.

**ReferencingEntity**: transactioncurrency<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_transactioncurrencies<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_expiredprocess"></a> organization_expiredprocess

Same as expiredprocess entity [organization_expiredprocess](expiredprocess.md#BKMK_organization_expiredprocess) Many-To-One relationship.

**ReferencingEntity**: expiredprocess<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: organization_expiredprocess<br />
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


### <a name="BKMK_organization_mailbox"></a> organization_mailbox

Same as mailbox entity [organization_mailbox](mailbox.md#BKMK_organization_mailbox) Many-To-One relationship.

**ReferencingEntity**: mailbox<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_mailbox<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_lk_dataperformance_organizationid"></a> lk_dataperformance_organizationid

Same as dataperformance entity [lk_dataperformance_organizationid](dataperformance.md#BKMK_lk_dataperformance_organizationid) Many-To-One relationship.

**ReferencingEntity**: dataperformance<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_dataperformance_organizationid<br />
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


### <a name="BKMK_organization_isvconfigs"></a> organization_isvconfigs

Same as isvconfig entity [organization_isvconfigs](isvconfig.md#BKMK_organization_isvconfigs) Many-To-One relationship.

**ReferencingEntity**: isvconfig<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_isvconfigs<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_sharepointdata"></a> organization_sharepointdata

Same as sharepointdata entity [organization_sharepointdata](sharepointdata.md#BKMK_organization_sharepointdata) Many-To-One relationship.

**ReferencingEntity**: sharepointdata<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_sharepointdata<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_offlinecommanddefinition_organization"></a> offlinecommanddefinition_organization

Same as offlinecommanddefinition entity [offlinecommanddefinition_organization](offlinecommanddefinition.md#BKMK_offlinecommanddefinition_organization) Many-To-One relationship.

**ReferencingEntity**: offlinecommanddefinition<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: offlinecommanddefinition_organization<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_MobileOfflineProfileItem_organization"></a> MobileOfflineProfileItem_organization

Same as mobileofflineprofileitem entity [MobileOfflineProfileItem_organization](mobileofflineprofileitem.md#BKMK_MobileOfflineProfileItem_organization) Many-To-One relationship.

**ReferencingEntity**: mobileofflineprofileitem<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: MobileOfflineProfileItem_organization<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_custom_displaystrings"></a> organization_custom_displaystrings

Same as displaystring entity [organization_custom_displaystrings](displaystring.md#BKMK_organization_custom_displaystrings) Many-To-One relationship.

**ReferencingEntity**: displaystring<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_custom_displaystrings<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_Organization_SyncErrors"></a> Organization_SyncErrors

Same as syncerror entity [Organization_SyncErrors](syncerror.md#BKMK_Organization_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: Organization_SyncErrors<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: NoCascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_channelpropertygroup_organization"></a> channelpropertygroup_organization

Same as channelpropertygroup entity [channelpropertygroup_organization](channelpropertygroup.md#BKMK_channelpropertygroup_organization) Many-To-One relationship.

**ReferencingEntity**: channelpropertygroup<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: channelpropertygroup_organization<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_sdkmessagerequest"></a> organization_sdkmessagerequest

Same as sdkmessagerequest entity [organization_sdkmessagerequest](sdkmessagerequest.md#BKMK_organization_sdkmessagerequest) Many-To-One relationship.

**ReferencingEntity**: sdkmessagerequest<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_sdkmessagerequest<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_Organization_AsyncOperations"></a> Organization_AsyncOperations

Same as asyncoperation entity [Organization_AsyncOperations](asyncoperation.md#BKMK_Organization_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Organization_AsyncOperations<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_customcontroldefaultconfig_organization"></a> customcontroldefaultconfig_organization

Same as customcontroldefaultconfig entity [customcontroldefaultconfig_organization](customcontroldefaultconfig.md#BKMK_customcontroldefaultconfig_organization) Many-To-One relationship.

**ReferencingEntity**: customcontroldefaultconfig<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: customcontroldefaultconfig_organization<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_sitemap"></a> organization_sitemap

Same as sitemap entity [organization_sitemap](sitemap.md#BKMK_organization_sitemap) Many-To-One relationship.

**ReferencingEntity**: sitemap<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_sitemap<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_Organization_MailboxTrackingFolder"></a> Organization_MailboxTrackingFolder

Same as mailboxtrackingfolder entity [Organization_MailboxTrackingFolder](mailboxtrackingfolder.md#BKMK_Organization_MailboxTrackingFolder) Many-To-One relationship.

**ReferencingEntity**: mailboxtrackingfolder<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Organization_MailboxTrackingFolder<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_emailserverprofile"></a> organization_emailserverprofile

Same as emailserverprofile entity [organization_emailserverprofile](emailserverprofile.md#BKMK_organization_emailserverprofile) Many-To-One relationship.

**ReferencingEntity**: emailserverprofile<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_emailserverprofile<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_lk_organizationui_organizationid"></a> lk_organizationui_organizationid

Same as organizationui entity [lk_organizationui_organizationid](organizationui.md#BKMK_lk_organizationui_organizationid) Many-To-One relationship.

**ReferencingEntity**: organizationui<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_organizationui_organizationid<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_pluginassembly"></a> organization_pluginassembly

Same as pluginassembly entity [organization_pluginassembly](pluginassembly.md#BKMK_organization_pluginassembly) Many-To-One relationship.

**ReferencingEntity**: pluginassembly<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_pluginassembly<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_mailboxstatistics"></a> organization_mailboxstatistics

Same as mailboxstatistics entity [organization_mailboxstatistics](mailboxstatistics.md#BKMK_organization_mailboxstatistics) Many-To-One relationship.

**ReferencingEntity**: mailboxstatistics<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_mailboxstatistics<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_knowledgesearchmodel"></a> organization_knowledgesearchmodel

Same as knowledgesearchmodel entity [organization_knowledgesearchmodel](knowledgesearchmodel.md#BKMK_organization_knowledgesearchmodel) Many-To-One relationship.

**ReferencingEntity**: knowledgesearchmodel<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_knowledgesearchmodel<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_Organization_BulkDeleteFailures"></a> Organization_BulkDeleteFailures

Same as bulkdeletefailure entity [Organization_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Organization_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Organization_BulkDeleteFailures<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_lk_fieldsecurityprofile_organizationid"></a> lk_fieldsecurityprofile_organizationid

Same as fieldsecurityprofile entity [lk_fieldsecurityprofile_organizationid](fieldsecurityprofile.md#BKMK_lk_fieldsecurityprofile_organizationid) Many-To-One relationship.

**ReferencingEntity**: fieldsecurityprofile<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_fieldsecurityprofile_organizationid<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_sdkmessagefilter"></a> organization_sdkmessagefilter

Same as sdkmessagefilter entity [organization_sdkmessagefilter](sdkmessagefilter.md#BKMK_organization_sdkmessagefilter) Many-To-One relationship.

**ReferencingEntity**: sdkmessagefilter<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_sdkmessagefilter<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_kb_article_templates"></a> organization_kb_article_templates

Same as kbarticletemplate entity [organization_kb_article_templates](kbarticletemplate.md#BKMK_organization_kb_article_templates) Many-To-One relationship.

**ReferencingEntity**: kbarticletemplate<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_kb_article_templates<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_roles"></a> organization_roles

Same as role entity [organization_roles](role.md#BKMK_organization_roles) Many-To-One relationship.

**ReferencingEntity**: role<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_roles<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_sdkmessageprocessingstepsecureconfig"></a> organization_sdkmessageprocessingstepsecureconfig

Same as sdkmessageprocessingstepsecureconfig entity [organization_sdkmessageprocessingstepsecureconfig](sdkmessageprocessingstepsecureconfig.md#BKMK_organization_sdkmessageprocessingstepsecureconfig) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstepsecureconfig<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_sdkmessageprocessingstepsecureconfig<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_entitydatasource"></a> organization_entitydatasource

Same as entitydatasource entity [organization_entitydatasource](entitydatasource.md#BKMK_organization_entitydatasource) Many-To-One relationship.

**ReferencingEntity**: entitydatasource<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_entitydatasource<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_aciviewmapper"></a> organization_aciviewmapper

Same as aciviewmapper entity [organization_aciviewmapper](aciviewmapper.md#BKMK_organization_aciviewmapper) Many-To-One relationship.

**ReferencingEntity**: aciviewmapper<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_aciviewmapper<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_system_users"></a> organization_system_users

Same as systemuser entity [organization_system_users](systemuser.md#BKMK_organization_system_users) Many-To-One relationship.

**ReferencingEntity**: systemuser<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_system_users<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_languagelocale_organization"></a> languagelocale_organization

Same as languagelocale entity [languagelocale_organization](languagelocale.md#BKMK_languagelocale_organization) Many-To-One relationship.

**ReferencingEntity**: languagelocale<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: languagelocale_organization<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_business_units"></a> organization_business_units

Same as businessunit entity [organization_business_units](businessunit.md#BKMK_organization_business_units) Many-To-One relationship.

**ReferencingEntity**: businessunit<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_business_units<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_sdkmessageresponsefield"></a> organization_sdkmessageresponsefield

Same as sdkmessageresponsefield entity [organization_sdkmessageresponsefield](sdkmessageresponsefield.md#BKMK_organization_sdkmessageresponsefield) Many-To-One relationship.

**ReferencingEntity**: sdkmessageresponsefield<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_sdkmessageresponsefield<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_attributemap"></a> organization_attributemap

Same as attributemap entity [organization_attributemap](attributemap.md#BKMK_organization_attributemap) Many-To-One relationship.

**ReferencingEntity**: attributemap<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_attributemap<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_newprocess"></a> organization_newprocess

Same as newprocess entity [organization_newprocess](newprocess.md#BKMK_organization_newprocess) Many-To-One relationship.

**ReferencingEntity**: newprocess<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: organization_newprocess<br />
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


### <a name="BKMK_organization_hierarchyrules"></a> organization_hierarchyrules

Same as hierarchyrule entity [organization_hierarchyrules](hierarchyrule.md#BKMK_organization_hierarchyrules) Many-To-One relationship.

**ReferencingEntity**: hierarchyrule<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_hierarchyrules<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_sdkmessageprocessingstep"></a> organization_sdkmessageprocessingstep

Same as sdkmessageprocessingstep entity [organization_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_organization_sdkmessageprocessingstep) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstep<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_sdkmessageprocessingstep<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_RoutingRules"></a> organization_RoutingRules

Same as routingrule entity [organization_RoutingRules](routingrule.md#BKMK_organization_RoutingRules) Many-To-One relationship.

**ReferencingEntity**: routingrule<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_RoutingRules<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_orginsightsnotification"></a> organization_orginsightsnotification

Same as orginsightsnotification entity [organization_orginsightsnotification](orginsightsnotification.md#BKMK_organization_orginsightsnotification) Many-To-One relationship.

**ReferencingEntity**: orginsightsnotification<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_orginsightsnotification<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_appconfiginstance"></a> organization_appconfiginstance

Same as appconfiginstance entity [organization_appconfiginstance](appconfiginstance.md#BKMK_organization_appconfiginstance) Many-To-One relationship.

**ReferencingEntity**: appconfiginstance<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_appconfiginstance<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_routingruleitems"></a> organization_routingruleitems

Same as routingruleitem entity [organization_routingruleitems](routingruleitem.md#BKMK_organization_routingruleitems) Many-To-One relationship.

**ReferencingEntity**: routingruleitem<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_routingruleitems<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_lk_documenttemplatebase_organization"></a> lk_documenttemplatebase_organization

Same as documenttemplate entity [lk_documenttemplatebase_organization](documenttemplate.md#BKMK_lk_documenttemplatebase_organization) Many-To-One relationship.

**ReferencingEntity**: documenttemplate<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_documenttemplatebase_organization<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_serviceendpoint"></a> organization_serviceendpoint

Same as serviceendpoint entity [organization_serviceendpoint](serviceendpoint.md#BKMK_organization_serviceendpoint) Many-To-One relationship.

**ReferencingEntity**: serviceendpoint<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_serviceendpoint<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_sdkmessage"></a> organization_sdkmessage

Same as sdkmessage entity [organization_sdkmessage](sdkmessage.md#BKMK_organization_sdkmessage) Many-To-One relationship.

**ReferencingEntity**: sdkmessage<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_sdkmessage<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_appconfigmaster"></a> organization_appconfigmaster

Same as appconfigmaster entity [organization_appconfigmaster](appconfigmaster.md#BKMK_organization_appconfigmaster) Many-To-One relationship.

**ReferencingEntity**: appconfigmaster<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_appconfigmaster<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_saved_queries"></a> organization_saved_queries

Same as savedquery entity [organization_saved_queries](savedquery.md#BKMK_organization_saved_queries) Many-To-One relationship.

**ReferencingEntity**: savedquery<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_saved_queries<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_tracelog"></a> organization_tracelog

Same as tracelog entity [organization_tracelog](tracelog.md#BKMK_organization_tracelog) Many-To-One relationship.

**ReferencingEntity**: tracelog<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_tracelog<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_organization_solution"></a> organization_solution

Same as solution entity [organization_solution](solution.md#BKMK_organization_solution) Many-To-One relationship.

**ReferencingEntity**: solution<br />
**ReferencingAttribute**: organizationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: organization_solution<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [lk_organizationbase_modifiedby](#BKMK_lk_organizationbase_modifiedby)
- [lk_organization_createdonbehalfby](#BKMK_lk_organization_createdonbehalfby)
- [EmailServerProfile_Organization](#BKMK_EmailServerProfile_Organization)
- [DefaultMobileOfflineProfile_Organization](#BKMK_DefaultMobileOfflineProfile_Organization)
- [lk_organizationbase_createdby](#BKMK_lk_organizationbase_createdby)
- [basecurrency_organization](#BKMK_basecurrency_organization)
- [lk_organization_modifiedonbehalfby](#BKMK_lk_organization_modifiedonbehalfby)
- [calendar_organization](#BKMK_calendar_organization)
- [Template_Organization](#BKMK_Template_Organization)


### <a name="BKMK_lk_organizationbase_modifiedby"></a> lk_organizationbase_modifiedby

See systemuser Entity [lk_organizationbase_modifiedby](systemuser.md#BKMK_lk_organizationbase_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_organization_createdonbehalfby"></a> lk_organization_createdonbehalfby

See systemuser Entity [lk_organization_createdonbehalfby](systemuser.md#BKMK_lk_organization_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_EmailServerProfile_Organization"></a> EmailServerProfile_Organization

See emailserverprofile Entity [EmailServerProfile_Organization](emailserverprofile.md#BKMK_EmailServerProfile_Organization) One-To-Many relationship.

### <a name="BKMK_DefaultMobileOfflineProfile_Organization"></a> DefaultMobileOfflineProfile_Organization

See mobileofflineprofile Entity [DefaultMobileOfflineProfile_Organization](mobileofflineprofile.md#BKMK_DefaultMobileOfflineProfile_Organization) One-To-Many relationship.

### <a name="BKMK_lk_organizationbase_createdby"></a> lk_organizationbase_createdby

See systemuser Entity [lk_organizationbase_createdby](systemuser.md#BKMK_lk_organizationbase_createdby) One-To-Many relationship.

### <a name="BKMK_basecurrency_organization"></a> basecurrency_organization

See transactioncurrency Entity [basecurrency_organization](transactioncurrency.md#BKMK_basecurrency_organization) One-To-Many relationship.

### <a name="BKMK_lk_organization_modifiedonbehalfby"></a> lk_organization_modifiedonbehalfby

See systemuser Entity [lk_organization_modifiedonbehalfby](systemuser.md#BKMK_lk_organization_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_calendar_organization"></a> calendar_organization

See calendar Entity [calendar_organization](calendar.md#BKMK_calendar_organization) One-To-Many relationship.

### <a name="BKMK_Template_Organization"></a> Template_Organization

See template Entity [Template_Organization](template.md#BKMK_Template_Organization) One-To-Many relationship.
organization

