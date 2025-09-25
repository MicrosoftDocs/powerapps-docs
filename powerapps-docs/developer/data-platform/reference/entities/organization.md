---
title: "Organization table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Organization table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Organization table/entity reference (Microsoft Dataverse)

Top level of the Microsoft Dynamics 365 business hierarchy. The organization can be a specific business, holding company, or corporation.

## Messages

The following table lists the messages for the Organization table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /organizations(*organizationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /organizations<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /organizations(*organizationid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|

## Properties

The following table lists selected properties for the Organization table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Organization** |
| **DisplayCollectionName** | **Organizations** |
| **SchemaName** | `Organization` |
| **CollectionSchemaName** | `Organizations` |
| **EntitySetName** | `organizations`|
| **LogicalName** | `organization` |
| **LogicalCollectionName** | `organizations` |
| **PrimaryIdAttribute** | `organizationid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ACIWebEndpointUrl](#BKMK_ACIWebEndpointUrl)
- [AcknowledgementTemplateId](#BKMK_AcknowledgementTemplateId)
- [ActivityTypeFilter](#BKMK_ActivityTypeFilter)
- [ActivityTypeFilterV2](#BKMK_ActivityTypeFilterV2)
- [AdvancedColumnEditorEnabled](#BKMK_AdvancedColumnEditorEnabled)
- [AdvancedColumnFilteringEnabled](#BKMK_AdvancedColumnFilteringEnabled)
- [AdvancedFilteringEnabled](#BKMK_AdvancedFilteringEnabled)
- [AdvancedLookupEnabled](#BKMK_AdvancedLookupEnabled)
- [AdvancedLookupInEditFilter](#BKMK_AdvancedLookupInEditFilter)
- [AiPromptsEnabled](#BKMK_AiPromptsEnabled)
- [AllowAddressBookSyncs](#BKMK_AllowAddressBookSyncs)
- [AllowApplicationUserAccess](#BKMK_AllowApplicationUserAccess)
- [AllowAutoResponseCreation](#BKMK_AllowAutoResponseCreation)
- [AllowAutoUnsubscribe](#BKMK_AllowAutoUnsubscribe)
- [AllowAutoUnsubscribeAcknowledgement](#BKMK_AllowAutoUnsubscribeAcknowledgement)
- [AllowClientMessageBarAd](#BKMK_AllowClientMessageBarAd)
- [AllowConnectorsOnPowerFXActions](#BKMK_AllowConnectorsOnPowerFXActions)
- [AllowedApplicationsForDVAccess](#BKMK_AllowedApplicationsForDVAccess)
- [AllowedIpRangeForFirewall](#BKMK_AllowedIpRangeForFirewall)
- [AllowedIpRangeForStorageAccessSignatures](#BKMK_AllowedIpRangeForStorageAccessSignatures)
- [AllowedListOfIpRangesForFirewall](#BKMK_AllowedListOfIpRangesForFirewall)
- [AllowedMimeTypes](#BKMK_AllowedMimeTypes)
- [AllowedServiceTagsForFirewall](#BKMK_AllowedServiceTagsForFirewall)
- [AllowEntityOnlyAudit](#BKMK_AllowEntityOnlyAudit)
- [AllowLeadingWildcardsInGridSearch](#BKMK_AllowLeadingWildcardsInGridSearch)
- [AllowLeadingWildcardsInQuickFind](#BKMK_AllowLeadingWildcardsInQuickFind)
- [AllowLegacyClientExperience](#BKMK_AllowLegacyClientExperience)
- [AllowLegacyDialogsEmbedding](#BKMK_AllowLegacyDialogsEmbedding)
- [AllowMarketingEmailExecution](#BKMK_AllowMarketingEmailExecution)
- [AllowMicrosoftTrustedServiceTags](#BKMK_AllowMicrosoftTrustedServiceTags)
- [AllowOfflineScheduledSyncs](#BKMK_AllowOfflineScheduledSyncs)
- [AllowOutlookScheduledSyncs](#BKMK_AllowOutlookScheduledSyncs)
- [AllowRedirectAdminSettingsToModernUI](#BKMK_AllowRedirectAdminSettingsToModernUI)
- [AllowUnresolvedPartiesOnEmailSend](#BKMK_AllowUnresolvedPartiesOnEmailSend)
- [AllowUserFormModePreference](#BKMK_AllowUserFormModePreference)
- [AllowUsersHidingSystemViews](#BKMK_AllowUsersHidingSystemViews)
- [AllowUsersSeeAppdownloadMessage](#BKMK_AllowUsersSeeAppdownloadMessage)
- [AllowVirtualEntityPluginExecutionOnNestedPipeline](#BKMK_AllowVirtualEntityPluginExecutionOnNestedPipeline)
- [AllowWebExcelExport](#BKMK_AllowWebExcelExport)
- [AMDesignator](#BKMK_AMDesignator)
- [AppDesignerExperienceEnabled](#BKMK_AppDesignerExperienceEnabled)
- [ApplicationBasedAccessControlMode](#BKMK_ApplicationBasedAccessControlMode)
- [AppointmentRichEditorExperience](#BKMK_AppointmentRichEditorExperience)
- [AppointmentWithTeamsMeeting](#BKMK_AppointmentWithTeamsMeeting)
- [AppointmentWithTeamsMeetingV2](#BKMK_AppointmentWithTeamsMeetingV2)
- [AreAutomationCenterPreviewFeaturesEnabled](#BKMK_AreAutomationCenterPreviewFeaturesEnabled)
- [AreProcessInsightsPreviewFeaturesEnabled](#BKMK_AreProcessInsightsPreviewFeaturesEnabled)
- [AuditRetentionPeriod](#BKMK_AuditRetentionPeriod)
- [AuditRetentionPeriodV2](#BKMK_AuditRetentionPeriodV2)
- [AuditSettings](#BKMK_AuditSettings)
- [AutoApplyDefaultonCaseCreate](#BKMK_AutoApplyDefaultonCaseCreate)
- [AutoApplyDefaultonCaseUpdate](#BKMK_AutoApplyDefaultonCaseUpdate)
- [AutoApplySLA](#BKMK_AutoApplySLA)
- [AzureSchedulerJobCollectionName](#BKMK_AzureSchedulerJobCollectionName)
- [BaseCurrencyId](#BKMK_BaseCurrencyId)
- [BingMapsApiKey](#BKMK_BingMapsApiKey)
- [BlockAccessToSessionTranscriptsForCopilotStudio](#BKMK_BlockAccessToSessionTranscriptsForCopilotStudio)
- [BlockCopilotAuthorAuthentication](#BKMK_BlockCopilotAuthorAuthentication)
- [BlockedApplicationsForDVAccess](#BKMK_BlockedApplicationsForDVAccess)
- [BlockedAttachments](#BKMK_BlockedAttachments)
- [BlockedMimeTypes](#BKMK_BlockedMimeTypes)
- [BlockTranscriptRecordingForCopilotStudio](#BKMK_BlockTranscriptRecordingForCopilotStudio)
- [BoundDashboardDefaultCardExpanded](#BKMK_BoundDashboardDefaultCardExpanded)
- [BulkOperationPrefix](#BKMK_BulkOperationPrefix)
- [BusinessCardOptions](#BKMK_BusinessCardOptions)
- [BusinessClosureCalendarId](#BKMK_BusinessClosureCalendarId)
- [CalendarType](#BKMK_CalendarType)
- [CampaignPrefix](#BKMK_CampaignPrefix)
- [CanOptOutNewSearchExperience](#BKMK_CanOptOutNewSearchExperience)
- [CascadeStatusUpdate](#BKMK_CascadeStatusUpdate)
- [CasePrefix](#BKMK_CasePrefix)
- [CategoryPrefix](#BKMK_CategoryPrefix)
- [ClientFeatureSet](#BKMK_ClientFeatureSet)
- [ContentSecurityPolicyConfiguration](#BKMK_ContentSecurityPolicyConfiguration)
- [ContentSecurityPolicyConfigurationForCanvas](#BKMK_ContentSecurityPolicyConfigurationForCanvas)
- [ContentSecurityPolicyOptions](#BKMK_ContentSecurityPolicyOptions)
- [ContentSecurityPolicyReportUri](#BKMK_ContentSecurityPolicyReportUri)
- [ContractPrefix](#BKMK_ContractPrefix)
- [CopresenceRefreshRate](#BKMK_CopresenceRefreshRate)
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
- [DaysBeforeEmailDescriptionIsMigrated](#BKMK_DaysBeforeEmailDescriptionIsMigrated)
- [DaysBeforeInactiveTeamsChatSyncDisabled](#BKMK_DaysBeforeInactiveTeamsChatSyncDisabled)
- [DecimalSymbol](#BKMK_DecimalSymbol)
- [DefaultCountryCode](#BKMK_DefaultCountryCode)
- [DefaultCrmCustomName](#BKMK_DefaultCrmCustomName)
- [DefaultEmailServerProfileId](#BKMK_DefaultEmailServerProfileId)
- [DefaultEmailSettings](#BKMK_DefaultEmailSettings)
- [DefaultMobileOfflineProfileId](#BKMK_DefaultMobileOfflineProfileId)
- [DefaultRecurrenceEndRangeType](#BKMK_DefaultRecurrenceEndRangeType)
- [DefaultThemeData](#BKMK_DefaultThemeData)
- [DelegatedAdminUserId](#BKMK_DelegatedAdminUserId)
- [DesktopFlowQueueLogsTtlInMinutes](#BKMK_DesktopFlowQueueLogsTtlInMinutes)
- [DesktopFlowRunActionLogsStatus](#BKMK_DesktopFlowRunActionLogsStatus)
- [DesktopFlowRunActionLogVerbosity](#BKMK_DesktopFlowRunActionLogVerbosity)
- [DesktopFlowRunActionLogVersion](#BKMK_DesktopFlowRunActionLogVersion)
- [DisableSocialCare](#BKMK_DisableSocialCare)
- [DisableSystemLabelsCacheSharing](#BKMK_DisableSystemLabelsCacheSharing)
- [DiscountCalculationMethod](#BKMK_DiscountCalculationMethod)
- [DisplayNavigationTour](#BKMK_DisplayNavigationTour)
- [EmailConnectionChannel](#BKMK_EmailConnectionChannel)
- [EmailCorrelationEnabled](#BKMK_EmailCorrelationEnabled)
- [EmailSendPollingPeriod](#BKMK_EmailSendPollingPeriod)
- [EnableAsyncMergeAPIForUCI](#BKMK_EnableAsyncMergeAPIForUCI)
- [EnableBingMapsIntegration](#BKMK_EnableBingMapsIntegration)
- [EnableCanvasAppsInSolutionsByDefault](#BKMK_EnableCanvasAppsInSolutionsByDefault)
- [EnableCopilotStudioCrossGeoShareDataWithVivaInsights](#BKMK_EnableCopilotStudioCrossGeoShareDataWithVivaInsights)
- [EnableCopilotStudioShareDataWithVI](#BKMK_EnableCopilotStudioShareDataWithVI)
- [EnableCopilotStudioShareDataWithVivaInsights](#BKMK_EnableCopilotStudioShareDataWithVivaInsights)
- [EnableEnvironmentSettingsApp](#BKMK_EnableEnvironmentSettingsApp)
- [EnableFlowsInSolutionByDefault](#BKMK_EnableFlowsInSolutionByDefault)
- [EnableFlowsInSolutionByDefaultGracePeriod](#BKMK_EnableFlowsInSolutionByDefaultGracePeriod)
- [EnableImmersiveSkypeIntegration](#BKMK_EnableImmersiveSkypeIntegration)
- [EnableIpBasedCookieBinding](#BKMK_EnableIpBasedCookieBinding)
- [EnableIpBasedFirewallRule](#BKMK_EnableIpBasedFirewallRule)
- [EnableIpBasedFirewallRuleInAuditMode](#BKMK_EnableIpBasedFirewallRuleInAuditMode)
- [EnableIpBasedStorageAccessSignatureRule](#BKMK_EnableIpBasedStorageAccessSignatureRule)
- [EnableLivePersonaCardUCI](#BKMK_EnableLivePersonaCardUCI)
- [EnableLivePersonCardIntegrationInOffice](#BKMK_EnableLivePersonCardIntegrationInOffice)
- [EnableLPAuthoring](#BKMK_EnableLPAuthoring)
- [EnableMakerSwitchToClassic](#BKMK_EnableMakerSwitchToClassic)
- [EnableMicrosoftFlowIntegration](#BKMK_EnableMicrosoftFlowIntegration)
- [EnablePricingOnCreate](#BKMK_EnablePricingOnCreate)
- [EnableSmartMatching](#BKMK_EnableSmartMatching)
- [EnableUnifiedClientCDN](#BKMK_EnableUnifiedClientCDN)
- [EnableUnifiedInterfaceShellRefresh](#BKMK_EnableUnifiedInterfaceShellRefresh)
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
- [FlowLogsTtlInMinutes](#BKMK_FlowLogsTtlInMinutes)
- [FlowRunTimeToLiveInSeconds](#BKMK_FlowRunTimeToLiveInSeconds)
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
- [ImproveSearchLoggingEnabled](#BKMK_ImproveSearchLoggingEnabled)
- [InactivityTimeoutEnabled](#BKMK_InactivityTimeoutEnabled)
- [InactivityTimeoutInMins](#BKMK_InactivityTimeoutInMins)
- [InactivityTimeoutReminderInMins](#BKMK_InactivityTimeoutReminderInMins)
- [IncomingEmailExchangeEmailRetrievalBatchSize](#BKMK_IncomingEmailExchangeEmailRetrievalBatchSize)
- [InitialVersion](#BKMK_InitialVersion)
- [IntegrationUserId](#BKMK_IntegrationUserId)
- [InvoicePrefix](#BKMK_InvoicePrefix)
- [IpBasedStorageAccessSignatureMode](#BKMK_IpBasedStorageAccessSignatureMode)
- [IsActionCardEnabled](#BKMK_IsActionCardEnabled)
- [IsActionSupportFeatureEnabled](#BKMK_IsActionSupportFeatureEnabled)
- [IsActivityAnalysisEnabled](#BKMK_IsActivityAnalysisEnabled)
- [IsAppMode](#BKMK_IsAppMode)
- [IsAppointmentAttachmentSyncEnabled](#BKMK_IsAppointmentAttachmentSyncEnabled)
- [IsAssignedTasksSyncEnabled](#BKMK_IsAssignedTasksSyncEnabled)
- [IsAuditEnabled](#BKMK_IsAuditEnabled)
- [IsAutoDataCaptureEnabled](#BKMK_IsAutoDataCaptureEnabled)
- [IsAutoDataCaptureV2Enabled](#BKMK_IsAutoDataCaptureV2Enabled)
- [IsAutoInstallAppForD365InTeamsEnabled](#BKMK_IsAutoInstallAppForD365InTeamsEnabled)
- [IsAutoSaveEnabled](#BKMK_IsAutoSaveEnabled)
- [IsBaseCardStaticFieldDataEnabled](#BKMK_IsBaseCardStaticFieldDataEnabled)
- [IsBasicGeospatialIntegrationEnabled](#BKMK_IsBasicGeospatialIntegrationEnabled)
- [IsBPFEntityCustomizationFeatureEnabled](#BKMK_IsBPFEntityCustomizationFeatureEnabled)
- [IsCloudFlowSavingsEnabled](#BKMK_IsCloudFlowSavingsEnabled)
- [IsCollaborationExperienceEnabled](#BKMK_IsCollaborationExperienceEnabled)
- [IsComputerUseInMCSEnabled](#BKMK_IsComputerUseInMCSEnabled)
- [IsConflictDetectionEnabledForMobileClient](#BKMK_IsConflictDetectionEnabledForMobileClient)
- [IsContactMailingAddressSyncEnabled](#BKMK_IsContactMailingAddressSyncEnabled)
- [IsContentSecurityPolicyEnabled](#BKMK_IsContentSecurityPolicyEnabled)
- [IsContentSecurityPolicyEnabledForCanvas](#BKMK_IsContentSecurityPolicyEnabledForCanvas)
- [IsContextualEmailEnabled](#BKMK_IsContextualEmailEnabled)
- [IsContextualHelpEnabled](#BKMK_IsContextualHelpEnabled)
- [IsCopilotFeedbackEnabled](#BKMK_IsCopilotFeedbackEnabled)
- [IsCustomControlsInCanvasAppsEnabled](#BKMK_IsCustomControlsInCanvasAppsEnabled)
- [IsDefaultCountryCodeCheckEnabled](#BKMK_IsDefaultCountryCodeCheckEnabled)
- [IsDelegateAccessEnabled](#BKMK_IsDelegateAccessEnabled)
- [IsDelveActionHubIntegrationEnabled](#BKMK_IsDelveActionHubIntegrationEnabled)
- [IsDesktopFlowConnectionEmbeddingEnabled](#BKMK_IsDesktopFlowConnectionEmbeddingEnabled)
- [IsDesktopFlowRuntimeRepairAttendedEnabled](#BKMK_IsDesktopFlowRuntimeRepairAttendedEnabled)
- [IsDesktopFlowRuntimeRepairUnattendedEnabled](#BKMK_IsDesktopFlowRuntimeRepairUnattendedEnabled)
- [IsDesktopFlowSavingsEnabled](#BKMK_IsDesktopFlowSavingsEnabled)
- [IsDesktopFlowSchemaV2Enabled](#BKMK_IsDesktopFlowSchemaV2Enabled)
- [IsDesktopFlowVanillaImageSharingEnabled](#BKMK_IsDesktopFlowVanillaImageSharingEnabled)
- [IsDuplicateDetectionEnabled](#BKMK_IsDuplicateDetectionEnabled)
- [IsDuplicateDetectionEnabledForImport](#BKMK_IsDuplicateDetectionEnabledForImport)
- [IsDuplicateDetectionEnabledForOfflineSync](#BKMK_IsDuplicateDetectionEnabledForOfflineSync)
- [IsDuplicateDetectionEnabledForOnlineCreateUpdate](#BKMK_IsDuplicateDetectionEnabledForOnlineCreateUpdate)
- [IsEmailAddressValidationEnabled](#BKMK_IsEmailAddressValidationEnabled)
- [IsEmailMonitoringAllowed](#BKMK_IsEmailMonitoringAllowed)
- [IsEmailServerProfileContentFilteringEnabled](#BKMK_IsEmailServerProfileContentFilteringEnabled)
- [IsEnabledForAllRoles](#BKMK_IsEnabledForAllRoles)
- [IsExternalFileStorageEnabled](#BKMK_IsExternalFileStorageEnabled)
- [IsExternalSearchIndexEnabled](#BKMK_IsExternalSearchIndexEnabled)
- [IsFiscalPeriodMonthBased](#BKMK_IsFiscalPeriodMonthBased)
- [IsFolderAutoCreatedonSP](#BKMK_IsFolderAutoCreatedonSP)
- [IsFolderBasedTrackingEnabled](#BKMK_IsFolderBasedTrackingEnabled)
- [IsFullTextSearchEnabled](#BKMK_IsFullTextSearchEnabled)
- [IsGeospatialAzureMapsIntegrationEnabled](#BKMK_IsGeospatialAzureMapsIntegrationEnabled)
- [IsHierarchicalSecurityModelEnabled](#BKMK_IsHierarchicalSecurityModelEnabled)
- [IsIdeasDataCollectionEnabled](#BKMK_IsIdeasDataCollectionEnabled)
- [IsLUISEnabledforD365Bot](#BKMK_IsLUISEnabledforD365Bot)
- [IsMailboxForcedUnlockingEnabled](#BKMK_IsMailboxForcedUnlockingEnabled)
- [IsMailboxInactiveBackoffEnabled](#BKMK_IsMailboxInactiveBackoffEnabled)
- [IsManualSalesForecastingEnabled](#BKMK_IsManualSalesForecastingEnabled)
- [IsMobileClientOnDemandSyncEnabled](#BKMK_IsMobileClientOnDemandSyncEnabled)
- [IsMobileOfflineEnabled](#BKMK_IsMobileOfflineEnabled)
- [IsModelDrivenAppsInMSTeamsEnabled](#BKMK_IsModelDrivenAppsInMSTeamsEnabled)
- [IsMoneySavingsAllowed](#BKMK_IsMoneySavingsAllowed)
- [IsMSTeamsCollaborationEnabled](#BKMK_IsMSTeamsCollaborationEnabled)
- [IsMSTeamsEnabled](#BKMK_IsMSTeamsEnabled)
- [IsMSTeamsSettingChangedByUser](#BKMK_IsMSTeamsSettingChangedByUser)
- [IsMSTeamsUserSyncEnabled](#BKMK_IsMSTeamsUserSyncEnabled)
- [IsNewAddProductExperienceEnabled](#BKMK_IsNewAddProductExperienceEnabled)
- [IsNotesAnalysisEnabled](#BKMK_IsNotesAnalysisEnabled)
- [IsNotificationForD365InTeamsEnabled](#BKMK_IsNotificationForD365InTeamsEnabled)
- [IsOfficeGraphEnabled](#BKMK_IsOfficeGraphEnabled)
- [IsOneDriveEnabled](#BKMK_IsOneDriveEnabled)
- [IsPAIEnabled](#BKMK_IsPAIEnabled)
- [IsPDFGenerationEnabled](#BKMK_IsPDFGenerationEnabled)
- [IsPerProcessCapacityOverageEnabled](#BKMK_IsPerProcessCapacityOverageEnabled)
- [IsPlaybookEnabled](#BKMK_IsPlaybookEnabled)
- [IsPresenceEnabled](#BKMK_IsPresenceEnabled)
- [IsPreviewEnabledForActionCard](#BKMK_IsPreviewEnabledForActionCard)
- [IsPreviewForAutoCaptureEnabled](#BKMK_IsPreviewForAutoCaptureEnabled)
- [IsPreviewForEmailMonitoringAllowed](#BKMK_IsPreviewForEmailMonitoringAllowed)
- [IsPriceListMandatory](#BKMK_IsPriceListMandatory)
- [IsProcessCapacityAutoClaimEnabled](#BKMK_IsProcessCapacityAutoClaimEnabled)
- [IsQuickCreateEnabledForOpportunityClose](#BKMK_IsQuickCreateEnabledForOpportunityClose)
- [IsReadAuditEnabled](#BKMK_IsReadAuditEnabled)
- [IsRelationshipInsightsEnabled](#BKMK_IsRelationshipInsightsEnabled)
- [IsResourceBookingExchangeSyncEnabled](#BKMK_IsResourceBookingExchangeSyncEnabled)
- [IsRichTextNotesEnabled](#BKMK_IsRichTextNotesEnabled)
- [IsRpaAutoscaleAadJoinEnabled](#BKMK_IsRpaAutoscaleAadJoinEnabled)
- [IsRpaAutoscaleEnabled](#BKMK_IsRpaAutoscaleEnabled)
- [IsRpaBoxCrossGeoEnabled](#BKMK_IsRpaBoxCrossGeoEnabled)
- [IsRpaBoxEnabled](#BKMK_IsRpaBoxEnabled)
- [IsRpaUnattendedEnabled](#BKMK_IsRpaUnattendedEnabled)
- [IsSalesAssistantEnabled](#BKMK_IsSalesAssistantEnabled)
- [IsSharingInOrgAllowed](#BKMK_IsSharingInOrgAllowed)
- [IsSOPIntegrationEnabled](#BKMK_IsSOPIntegrationEnabled)
- [IsTextWrapEnabled](#BKMK_IsTextWrapEnabled)
- [IsUserAccessAuditEnabled](#BKMK_IsUserAccessAuditEnabled)
- [ISVIntegrationCode](#BKMK_ISVIntegrationCode)
- [IsWorkQueueSavingsEnabled](#BKMK_IsWorkQueueSavingsEnabled)
- [IsWriteInProductsAllowed](#BKMK_IsWriteInProductsAllowed)
- [KaPrefix](#BKMK_KaPrefix)
- [KbPrefix](#BKMK_KbPrefix)
- [KMSettings](#BKMK_KMSettings)
- [LanguageCode](#BKMK_LanguageCode)
- [LegacyAppToggle](#BKMK_LegacyAppToggle)
- [LocaleId](#BKMK_LocaleId)
- [LongDateFormatCode](#BKMK_LongDateFormatCode)
- [LookupCharacterCountBeforeResolve](#BKMK_LookupCharacterCountBeforeResolve)
- [LookupResolveDelayMS](#BKMK_LookupResolveDelayMS)
- [MailboxIntermittentIssueMinRange](#BKMK_MailboxIntermittentIssueMinRange)
- [MailboxPermanentIssueMinRange](#BKMK_MailboxPermanentIssueMinRange)
- [MaxActionStepsInBPF](#BKMK_MaxActionStepsInBPF)
- [MaxAllowedPendingRollupJobCount](#BKMK_MaxAllowedPendingRollupJobCount)
- [MaxAllowedPendingRollupJobPercentage](#BKMK_MaxAllowedPendingRollupJobPercentage)
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
- [MaxRollupFieldsPerEntity](#BKMK_MaxRollupFieldsPerEntity)
- [MaxRollupFieldsPerOrg](#BKMK_MaxRollupFieldsPerOrg)
- [MaxSLAItemsPerSLA](#BKMK_MaxSLAItemsPerSLA)
- [MaxUploadFileSize](#BKMK_MaxUploadFileSize)
- [MicrosoftFlowEnvironment](#BKMK_MicrosoftFlowEnvironment)
- [MinAddressBookSyncInterval](#BKMK_MinAddressBookSyncInterval)
- [MinOfflineSyncInterval](#BKMK_MinOfflineSyncInterval)
- [MinOutlookSyncInterval](#BKMK_MinOutlookSyncInterval)
- [MobileOfflineSyncInterval](#BKMK_MobileOfflineSyncInterval)
- [ModernAdvancedFindFiltering](#BKMK_ModernAdvancedFindFiltering)
- [ModernAppDesignerCoauthoringEnabled](#BKMK_ModernAppDesignerCoauthoringEnabled)
- [MultiColumnSortEnabled](#BKMK_MultiColumnSortEnabled)
- [Name](#BKMK_Name)
- [NaturalLanguageAssistFilter](#BKMK_NaturalLanguageAssistFilter)
- [NegativeCurrencyFormatCode](#BKMK_NegativeCurrencyFormatCode)
- [NegativeFormatCode](#BKMK_NegativeFormatCode)
- [NewSearchExperienceEnabled](#BKMK_NewSearchExperienceEnabled)
- [NextTrackingNumber](#BKMK_NextTrackingNumber)
- [NotifyMailboxOwnerOfEmailServerLevelAlerts](#BKMK_NotifyMailboxOwnerOfEmailServerLevelAlerts)
- [NumberFormat](#BKMK_NumberFormat)
- [NumberGroupFormat](#BKMK_NumberGroupFormat)
- [NumberSeparator](#BKMK_NumberSeparator)
- [OfficeAppsAutoDeploymentEnabled](#BKMK_OfficeAppsAutoDeploymentEnabled)
- [OfficeGraphDelveUrl](#BKMK_OfficeGraphDelveUrl)
- [OOBPriceCalculationEnabled](#BKMK_OOBPriceCalculationEnabled)
- [OptOutSchemaV2EnabledByDefault](#BKMK_OptOutSchemaV2EnabledByDefault)
- [OrderPrefix](#BKMK_OrderPrefix)
- [OrgDbOrgSettings](#BKMK_OrgDbOrgSettings)
- [OrgInsightsEnabled](#BKMK_OrgInsightsEnabled)
- [PaiPreviewScenarioEnabled](#BKMK_PaiPreviewScenarioEnabled)
- [PastExpansionWindow](#BKMK_PastExpansionWindow)
- [PcfDatasetGridEnabled](#BKMK_PcfDatasetGridEnabled)
- [PerformACTSyncAfter](#BKMK_PerformACTSyncAfter)
- [Picture](#BKMK_Picture)
- [PinpointLanguageCode](#BKMK_PinpointLanguageCode)
- [PluginTraceLogSetting](#BKMK_PluginTraceLogSetting)
- [PMDesignator](#BKMK_PMDesignator)
- [PostMessageWhitelistDomains](#BKMK_PostMessageWhitelistDomains)
- [PowerAppsMakerBotEnabled](#BKMK_PowerAppsMakerBotEnabled)
- [PowerBIAllowCrossRegionOperations](#BKMK_PowerBIAllowCrossRegionOperations)
- [PowerBIAutomaticPermissionsAssignment](#BKMK_PowerBIAutomaticPermissionsAssignment)
- [PowerBIComponentsCreate](#BKMK_PowerBIComponentsCreate)
- [PowerBiFeatureEnabled](#BKMK_PowerBiFeatureEnabled)
- [PricingDecimalPrecision](#BKMK_PricingDecimalPrecision)
- [PrivacyStatementUrl](#BKMK_PrivacyStatementUrl)
- [PrivilegeUserGroupId](#BKMK_PrivilegeUserGroupId)
- [PrivReportingGroupId](#BKMK_PrivReportingGroupId)
- [PrivReportingGroupName](#BKMK_PrivReportingGroupName)
- [ProductRecommendationsEnabled](#BKMK_ProductRecommendationsEnabled)
- [QualifyLeadAdditionalOptions](#BKMK_QualifyLeadAdditionalOptions)
- [QuickActionToOpenRecordsInSidePaneEnabled](#BKMK_QuickActionToOpenRecordsInSidePaneEnabled)
- [QuickFindRecordLimitEnabled](#BKMK_QuickFindRecordLimitEnabled)
- [QuotePrefix](#BKMK_QuotePrefix)
- [RecalculateSLA](#BKMK_RecalculateSLA)
- [RecurrenceDefaultNumberOfOccurrences](#BKMK_RecurrenceDefaultNumberOfOccurrences)
- [RecurrenceExpansionJobBatchInterval](#BKMK_RecurrenceExpansionJobBatchInterval)
- [RecurrenceExpansionJobBatchSize](#BKMK_RecurrenceExpansionJobBatchSize)
- [RecurrenceExpansionSynchCreateMax](#BKMK_RecurrenceExpansionSynchCreateMax)
- [ReferenceSiteMapXml](#BKMK_ReferenceSiteMapXml)
- [ReleaseCadence](#BKMK_ReleaseCadence)
- [ReleaseChannel](#BKMK_ReleaseChannel)
- [ReleaseWaveName](#BKMK_ReleaseWaveName)
- [RelevanceSearchEnabledByPlatform](#BKMK_RelevanceSearchEnabledByPlatform)
- [RelevanceSearchModifiedOn](#BKMK_RelevanceSearchModifiedOn)
- [RenderSecureIFrameForEmail](#BKMK_RenderSecureIFrameForEmail)
- [ReportingGroupId](#BKMK_ReportingGroupId)
- [ReportingGroupName](#BKMK_ReportingGroupName)
- [ReportScriptErrors](#BKMK_ReportScriptErrors)
- [RequireApprovalForQueueEmail](#BKMK_RequireApprovalForQueueEmail)
- [RequireApprovalForUserEmail](#BKMK_RequireApprovalForUserEmail)
- [ResolveSimilarUnresolvedEmailAddress](#BKMK_ResolveSimilarUnresolvedEmailAddress)
- [RestrictGuestUserAccess](#BKMK_RestrictGuestUserAccess)
- [RestrictStatusUpdate](#BKMK_RestrictStatusUpdate)
- [ReverseProxyIpAddresses](#BKMK_ReverseProxyIpAddresses)
- [RiErrorStatus](#BKMK_RiErrorStatus)
- [SameSiteModeForSessionCookie](#BKMK_SameSiteModeForSessionCookie)
- [SampleDataImportId](#BKMK_SampleDataImportId)
- [SavingEventsTTLInMinutes](#BKMK_SavingEventsTTLInMinutes)
- [SchemaNamePrefix](#BKMK_SchemaNamePrefix)
- [SendBulkEmailInUCI](#BKMK_SendBulkEmailInUCI)
- [ServeStaticResourcesFromAzureCDN](#BKMK_ServeStaticResourcesFromAzureCDN)
- [SessionRecordingEnabled](#BKMK_SessionRecordingEnabled)
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
- [SuppressValidationEmails](#BKMK_SuppressValidationEmails)
- [SyncBulkOperationBatchSize](#BKMK_SyncBulkOperationBatchSize)
- [SyncBulkOperationMaxLimit](#BKMK_SyncBulkOperationMaxLimit)
- [SyncOptInSelection](#BKMK_SyncOptInSelection)
- [SyncOptInSelectionStatus](#BKMK_SyncOptInSelectionStatus)
- [SystemUserId](#BKMK_SystemUserId)
- [TableScopedDVSearchInApps](#BKMK_TableScopedDVSearchInApps)
- [TagMaxAggressiveCycles](#BKMK_TagMaxAggressiveCycles)
- [TagPollingPeriod](#BKMK_TagPollingPeriod)
- [TaskBasedFlowEnabled](#BKMK_TaskBasedFlowEnabled)
- [TeamsChatDataSync](#BKMK_TeamsChatDataSync)
- [TelemetryInstrumentationKey](#BKMK_TelemetryInstrumentationKey)
- [TextAnalyticsEnabled](#BKMK_TextAnalyticsEnabled)
- [TimeFormatCode](#BKMK_TimeFormatCode)
- [TimeFormatString](#BKMK_TimeFormatString)
- [TimeSeparator](#BKMK_TimeSeparator)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [TokenExpiry](#BKMK_TokenExpiry)
- [TokenKey](#BKMK_TokenKey)
- [TraceLogMaximumAgeInDays](#BKMK_TraceLogMaximumAgeInDays)
- [TrackingPrefix](#BKMK_TrackingPrefix)
- [TrackingTokenIdBase](#BKMK_TrackingTokenIdBase)
- [TrackingTokenIdDigits](#BKMK_TrackingTokenIdDigits)
- [UniqueSpecifierLength](#BKMK_UniqueSpecifierLength)
- [UnresolveEmailAddressIfMultipleMatch](#BKMK_UnresolveEmailAddressIfMultipleMatch)
- [UseInbuiltRuleForDefaultPricelistSelection](#BKMK_UseInbuiltRuleForDefaultPricelistSelection)
- [UseLegacyRendering](#BKMK_UseLegacyRendering)
- [UsePositionHierarchy](#BKMK_UsePositionHierarchy)
- [UseQuickFindViewForGridSearch](#BKMK_UseQuickFindViewForGridSearch)
- [UserAccessAuditingInterval](#BKMK_UserAccessAuditingInterval)
- [UseReadForm](#BKMK_UseReadForm)
- [UserGroupId](#BKMK_UserGroupId)
- [UserRatingEnabled](#BKMK_UserRatingEnabled)
- [UseSkypeProtocol](#BKMK_UseSkypeProtocol)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [ValidationMode](#BKMK_ValidationMode)
- [WebResourceHash](#BKMK_WebResourceHash)
- [WeekStartDayCode](#BKMK_WeekStartDayCode)
- [WidgetProperties](#BKMK_WidgetProperties)
- [YammerGroupId](#BKMK_YammerGroupId)
- [YammerNetworkPermalink](#BKMK_YammerNetworkPermalink)
- [YammerOAuthAccessTokenExpired](#BKMK_YammerOAuthAccessTokenExpired)
- [YammerPostMethod](#BKMK_YammerPostMethod)
- [YearStartWeekCode](#BKMK_YearStartWeekCode)

### <a name="BKMK_ACIWebEndpointUrl"></a> ACIWebEndpointUrl

|Property|Value|
|---|---|
|Description|**ACI Web Endpoint URL.**|
|DisplayName|**ACI Tenant URL.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`aciwebendpointurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_AcknowledgementTemplateId"></a> AcknowledgementTemplateId

|Property|Value|
|---|---|
|Description|**Unique identifier of the template to be used for acknowledgement when a user unsubscribes.**|
|DisplayName|**Acknowledgement Template**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`acknowledgementtemplateid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|template|

### <a name="BKMK_ActivityTypeFilter"></a> ActivityTypeFilter

|Property|Value|
|---|---|
|Description|**Information on whether filtering activity based on entity in app.**|
|DisplayName|**Enable Rich Editing Experience for Appointment**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`activitytypefilter`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_activitytypefilter`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ActivityTypeFilterV2"></a> ActivityTypeFilterV2

|Property|Value|
|---|---|
|Description|**Whether to show only activities configured in this app or all activities in the 'New activity' button.**|
|DisplayName|**Show only activities configured in the app when accessing 'New activity' button**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`activitytypefilterv2`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_activitytypefilterv2`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AdvancedColumnEditorEnabled"></a> AdvancedColumnEditorEnabled

|Property|Value|
|---|---|
|Description|**Flag to indicate if the display column options on a view in model-driven apps is enabled**|
|DisplayName|**Advanced column editor enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`advancedcolumneditorenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AdvancedColumnFilteringEnabled"></a> AdvancedColumnFilteringEnabled

|Property|Value|
|---|---|
|Description|**Flag to indicate if the advanced column filtering in a view in model-driven apps is enabled**|
|DisplayName|**Advanced column filtering enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`advancedcolumnfilteringenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AdvancedFilteringEnabled"></a> AdvancedFilteringEnabled

|Property|Value|
|---|---|
|Description|**Flag to indicate if the advanced filtering on all tables in a model-driven app is enabled**|
|DisplayName|**Advanced filtering enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`advancedfilteringenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AdvancedLookupEnabled"></a> AdvancedLookupEnabled

|Property|Value|
|---|---|
|Description|**Flag to indicate if the Advanced Lookup feature is enabled for lookup controls**|
|DisplayName|**Advanced lookup enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`advancedlookupenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AdvancedLookupInEditFilter"></a> AdvancedLookupInEditFilter

|Property|Value|
|---|---|
|Description|**Enables advanced lookup in grid edit filter panel**|
|DisplayName|**Enable Advanced Lookup In Edit Filter**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`advancedlookupineditfilter`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|100|
|MinValue|0|

### <a name="BKMK_AiPromptsEnabled"></a> AiPromptsEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether AI Prompts feature is enabled.**|
|DisplayName|**Enable AI Prompts.**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`aipromptsenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowAddressBookSyncs"></a> AllowAddressBookSyncs

|Property|Value|
|---|---|
|Description|**Indicates whether background address book synchronization in Microsoft Office Outlook is allowed.**|
|DisplayName|**Allow Address Book Synchronization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowaddressbooksyncs`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_allowaddressbooksyncs`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowApplicationUserAccess"></a> AllowApplicationUserAccess

|Property|Value|
|---|---|
|Description|**Information that specifies whether all application users are allowed to access the environment**|
|DisplayName|**Allow All Application Users Access.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowapplicationuseraccess`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowAutoResponseCreation"></a> AllowAutoResponseCreation

|Property|Value|
|---|---|
|Description|**Indicates whether automatic response creation is allowed.**|
|DisplayName|**Allow Automatic Response Creation**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowautoresponsecreation`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organization_allowautoresponsecreation`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowAutoUnsubscribe"></a> AllowAutoUnsubscribe

|Property|Value|
|---|---|
|Description|**Indicates whether automatic unsubscribe is allowed.**|
|DisplayName|**Allow Automatic Unsubscribe**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowautounsubscribe`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organization_allowautounsubscribe`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowAutoUnsubscribeAcknowledgement"></a> AllowAutoUnsubscribeAcknowledgement

|Property|Value|
|---|---|
|Description|**Indicates whether automatic unsubscribe acknowledgement email is allowed to send.**|
|DisplayName|**Allow Automatic Unsubscribe Acknowledgement**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowautounsubscribeacknowledgement`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organization_allowautounsubscribeacknowledgement`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowClientMessageBarAd"></a> AllowClientMessageBarAd

|Property|Value|
|---|---|
|Description|**Indicates whether Outlook Client message bar advertisement is allowed.**|
|DisplayName|**Allow Outlook Client Message Bar Advertisement**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowclientmessagebarad`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_allowclientmessagebarad`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowConnectorsOnPowerFXActions"></a> AllowConnectorsOnPowerFXActions

|Property|Value|
|---|---|
|Description|**Information on whether connectors on power fx actions is enabled.**|
|DisplayName|**Enable connectors on power fx actions.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowconnectorsonpowerfxactions`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_allowconnectorsonpowerfxactions`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowedApplicationsForDVAccess"></a> AllowedApplicationsForDVAccess

|Property|Value|
|---|---|
|Description|**Information that specifies the Applications that are in allow list for the accessing DV resources.**|
|DisplayName|**List of Applications that are in allow list for the accessing DV resources.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowedapplicationsfordvaccess`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20000|

### <a name="BKMK_AllowedIpRangeForFirewall"></a> AllowedIpRangeForFirewall

|Property|Value|
|---|---|
|Description|**Information that specifies the range of IP addresses that are in allow list for the firewall.**|
|DisplayName|**List of IP Ranges to be allowed by the firewall rule**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowediprangeforfirewall`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_AllowedIpRangeForStorageAccessSignatures"></a> AllowedIpRangeForStorageAccessSignatures

|Property|Value|
|---|---|
|Description|**Information that specifies the range of IP addresses that are in allowed list for generating the SAS URIs.**|
|DisplayName|**List of IP Ranges to be allowed for generating the SAS URIs.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowediprangeforstorageaccesssignatures`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_AllowedListOfIpRangesForFirewall"></a> AllowedListOfIpRangesForFirewall

|Property|Value|
|---|---|
|Description|**Specifies list of allowed IP addresses for firewall.**|
|DisplayName|**List of IP Ranges to be allowed by the firewall rule**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowedlistofiprangesforfirewall`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_AllowedMimeTypes"></a> AllowedMimeTypes

|Property|Value|
|---|---|
|Description|**Allow upload or download of certain mime types.**|
|DisplayName|**List of allowed mime types.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowedmimetypes`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_AllowedServiceTagsForFirewall"></a> AllowedServiceTagsForFirewall

|Property|Value|
|---|---|
|Description|**Information that specifies the List of Service Tags that should be allowed by the firewall.**|
|DisplayName|**List of Service Tags to be allowed by the firewall rule**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowedservicetagsforfirewall`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_AllowEntityOnlyAudit"></a> AllowEntityOnlyAudit

|Property|Value|
|---|---|
|Description|**Indicates whether auditing of changes to entity is allowed when no attributes have changed.**|
|DisplayName|**Allow Entity Level Auditing**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowentityonlyaudit`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_allowentityonlyaudit`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowLeadingWildcardsInGridSearch"></a> AllowLeadingWildcardsInGridSearch

|Property|Value|
|---|---|
|Description|**Enables ends-with searches in grids with the use of a leading wildcard on all tables in the environment**|
|DisplayName|**Allow Leading Wildcards In Grid Search**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`allowleadingwildcardsingridsearch`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowLeadingWildcardsInQuickFind"></a> AllowLeadingWildcardsInQuickFind

|Property|Value|
|---|---|
|Description|**Enables ends-with searches in grids with the use of a leading wildcard on all tables in the environment**|
|DisplayName|**Allow Leading Wildcards In Quick Find**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`allowleadingwildcardsinquickfind`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|100|
|MinValue|0|

### <a name="BKMK_AllowLegacyClientExperience"></a> AllowLegacyClientExperience

|Property|Value|
|---|---|
|Description|**Enable access to legacy web client UI**|
|DisplayName|**Enable access to legacy web client UI**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowlegacyclientexperience`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowLegacyDialogsEmbedding"></a> AllowLegacyDialogsEmbedding

|Property|Value|
|---|---|
|Description|**Enable embedding of certain legacy dialogs in Unified Interface browser client**|
|DisplayName|**Enable embedding of certain legacy dialogs in Unified Interface browser client**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowlegacydialogsembedding`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowMarketingEmailExecution"></a> AllowMarketingEmailExecution

|Property|Value|
|---|---|
|Description|**Indicates whether marketing emails execution is allowed.**|
|DisplayName|**Allow Marketing Email Execution**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowmarketingemailexecution`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_allowmarketingemailexecution`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowMicrosoftTrustedServiceTags"></a> AllowMicrosoftTrustedServiceTags

|Property|Value|
|---|---|
|Description|**Information that specifies whether Microsoft Trusted Service Tags are allowed**|
|DisplayName|**Allow Microsoft Trusted Service Tags**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowmicrosofttrustedservicetags`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowOfflineScheduledSyncs"></a> AllowOfflineScheduledSyncs

|Property|Value|
|---|---|
|Description|**Indicates whether background offline synchronization in Microsoft Office Outlook is allowed.**|
|DisplayName|**Allow Offline Scheduled Synchronization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowofflinescheduledsyncs`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_allowofflinescheduledsyncs`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowOutlookScheduledSyncs"></a> AllowOutlookScheduledSyncs

|Property|Value|
|---|---|
|Description|**Indicates whether scheduled synchronizations to Outlook are allowed.**|
|DisplayName|**Allow Scheduled Synchronization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowoutlookscheduledsyncs`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_allowoutlookscheduledsyncs`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowRedirectAdminSettingsToModernUI"></a> AllowRedirectAdminSettingsToModernUI

|Property|Value|
|---|---|
|Description|**Control whether the organization Allow Redirect Legacy Admin Settings To Modern UI**|
|DisplayName|**Allow Redirect Legacy Admin Settings To Modern UI**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`allowredirectadminsettingstomodernui`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowUnresolvedPartiesOnEmailSend"></a> AllowUnresolvedPartiesOnEmailSend

|Property|Value|
|---|---|
|Description|**Indicates whether users are allowed to send email to unresolved parties (parties must still have an email address).**|
|DisplayName|**Allow Unresolved Address Email Send**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowunresolvedpartiesonemailsend`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_allowunresolvedpartiesonemailsend`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowUserFormModePreference"></a> AllowUserFormModePreference

|Property|Value|
|---|---|
|Description|**Indicates whether individuals can select their form mode preference in their personal options.**|
|DisplayName|**Allow User Form Mode Preference**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowuserformmodepreference`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_allowuserformmodepreference`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowUsersHidingSystemViews"></a> AllowUsersHidingSystemViews

|Property|Value|
|---|---|
|Description|**Flag to indicate if allow end users to hide system views in model-driven apps is enabled**|
|DisplayName|**Allow users hiding system views**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`allowusershidingsystemviews`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowUsersSeeAppdownloadMessage"></a> AllowUsersSeeAppdownloadMessage

|Property|Value|
|---|---|
|Description|**Indicates whether the showing tablet application notification bars in a browser is allowed.**|
|DisplayName|**Allow the showing tablet application notification bars in a browser.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowusersseeappdownloadmessage`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_allowusersseeappdownloadmessage`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowVirtualEntityPluginExecutionOnNestedPipeline"></a> AllowVirtualEntityPluginExecutionOnNestedPipeline

|Property|Value|
|---|---|
|Description|**Warning : Allowing  Virtual Entity plugin execution on nested pipeline does not offer transactional support. i.e. if call in native entity pipeline fails, then virtual entity operation will not be reverted.**|
|DisplayName|**Allow Virtual Entity Plugin Execution In Nested Pipeline.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowvirtualentitypluginexecutiononnestedpipeline`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_allowvirtualentitypluginexecutiononnestedpipelines`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AllowWebExcelExport"></a> AllowWebExcelExport

|Property|Value|
|---|---|
|Description|**Indicates whether Web-based export of grids to Microsoft Office Excel is allowed.**|
|DisplayName|**Allow Export to Excel**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowwebexcelexport`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_allowwebexcelexport`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AMDesignator"></a> AMDesignator

|Property|Value|
|---|---|
|Description|**AM designator to use throughout Microsoft Dynamics CRM.**|
|DisplayName|**AM Designator**|
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

### <a name="BKMK_AppDesignerExperienceEnabled"></a> AppDesignerExperienceEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether the appDesignerExperience is enabled for the organization.**|
|DisplayName|**Enable App Designer Experience for this Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appdesignerexperienceenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_appdesignerexperienceenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ApplicationBasedAccessControlMode"></a> ApplicationBasedAccessControlMode

|Property|Value|
|---|---|
|Description|**Application Based Access Control Mode. 0 is Disabled, 1 is audit mode , 2 is enforcement mode**|
|DisplayName|**Application Based Access Control Mode**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`applicationbasedaccesscontrolmode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`organization_applicationbasedaccesscontrolmode`|

#### ApplicationBasedAccessControlMode Choices/Options

|Value|Label|
|---|---|
|0|**Disabled**|
|1|**Enabled**|
|2|**AuditMode**|
|3|**Enabled for roles**|

### <a name="BKMK_AppointmentRichEditorExperience"></a> AppointmentRichEditorExperience

|Property|Value|
|---|---|
|Description|**Information on whether rich editing experience for Appointment is enabled.**|
|DisplayName|**Enable Rich Editing Experience for Appointment**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appointmentricheditorexperience`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_appointmentricheditorexperience`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AppointmentWithTeamsMeeting"></a> AppointmentWithTeamsMeeting

|Property|Value|
|---|---|
|Description|**Information on whether Teams meeting experience for Appointment is enabled.**|
|DisplayName|**Enable teams Meeting experience for appointment**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appointmentwithteamsmeeting`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_appointmentwithteamsmeeting`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AppointmentWithTeamsMeetingV2"></a> AppointmentWithTeamsMeetingV2

|Property|Value|
|---|---|
|Description|**Whether Teams meetings experience for appointments is enabled.**|
|DisplayName|**Enable Teams meetings for appointments**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appointmentwithteamsmeetingv2`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_appointmentwithteamsmeetingv2`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AreAutomationCenterPreviewFeaturesEnabled"></a> AreAutomationCenterPreviewFeaturesEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether Power Automate Automation Center preview features will be available for all users in this organization.**|
|DisplayName|**Enable Power Automate Automation Center preview features for all users in this organization.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`areautomationcenterpreviewfeaturesenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AreProcessInsightsPreviewFeaturesEnabled"></a> AreProcessInsightsPreviewFeaturesEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether Process Insights Preview features are enabled in this organization.**|
|DisplayName|**Enable Process Insights Preview features for this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`areprocessinsightspreviewfeaturesenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AuditRetentionPeriod"></a> AuditRetentionPeriod

|Property|Value|
|---|---|
|Description|**Audit Retention Period settings stored in Organization Database.**|
|DisplayName|**Audit Retention Period Settings**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`auditretentionperiod`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|30|

### <a name="BKMK_AuditRetentionPeriodV2"></a> AuditRetentionPeriodV2

|Property|Value|
|---|---|
|Description|**Audit Retention Period settings stored in Organization Database.**|
|DisplayName|**Audit Retention Period Settings**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`auditretentionperiodv2`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_AuditSettings"></a> AuditSettings

|Property|Value|
|---|---|
|Description|**Audit Settings of the organization**|
|DisplayName|**Audit Settings of the organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`auditsettings`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_AutoApplyDefaultonCaseCreate"></a> AutoApplyDefaultonCaseCreate

|Property|Value|
|---|---|
|Description|**Select whether to auto apply the default customer entitlement on case creation.**|
|DisplayName|**Auto Apply Default Entitlement on Case Create**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`autoapplydefaultoncasecreate`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_autoapplydefaultoncasecreate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AutoApplyDefaultonCaseUpdate"></a> AutoApplyDefaultonCaseUpdate

|Property|Value|
|---|---|
|Description|**Select whether to auto apply the default customer entitlement on case update.**|
|DisplayName|**Auto Apply Default Entitlement on Case Update**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`autoapplydefaultoncaseupdate`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_autoapplydefaultoncaseupdate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AutoApplySLA"></a> AutoApplySLA

|Property|Value|
|---|---|
|Description|**Indicates whether to Auto-apply SLA on case record update after SLA was manually applied.**|
|DisplayName|**Is Auto-apply SLA After Manually Over-riding**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`autoapplysla`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_autoapplysla`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AzureSchedulerJobCollectionName"></a> AzureSchedulerJobCollectionName

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**For internal use only.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`azureschedulerjobcollectionname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_BaseCurrencyId"></a> BaseCurrencyId

|Property|Value|
|---|---|
|Description|**Unique identifier of the base currency of the organization.**|
|DisplayName|**Currency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`basecurrencyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|transactioncurrency|

### <a name="BKMK_BingMapsApiKey"></a> BingMapsApiKey

|Property|Value|
|---|---|
|Description|**Api Key to be used in requests to Bing Maps services.**|
|DisplayName|**Bing Maps API Key**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`bingmapsapikey`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_BlockAccessToSessionTranscriptsForCopilotStudio"></a> BlockAccessToSessionTranscriptsForCopilotStudio

|Property|Value|
|---|---|
|Description|**Enable this feature to prevent makers from accessing and downloading session transcripts**|
|DisplayName|**Block access to session transcripts for Copilot Studio**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`blockaccesstosessiontranscriptsforcopilotstudio`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_BlockCopilotAuthorAuthentication"></a> BlockCopilotAuthorAuthentication

|Property|Value|
|---|---|
|Description|**Prevent makers from allowing end-users to use their credentials during authentication to use connectors, actions, flows, and triggers that are connected to an agent**|
|DisplayName|**Block makers from allowing end-users to use their credentials during authentication to use connectors, actions, flows, and triggers that are connected to an agent**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`blockcopilotauthorauthentication`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_BlockedApplicationsForDVAccess"></a> BlockedApplicationsForDVAccess

|Property|Value|
|---|---|
|Description|**Information that specifies the Applications that are in block list for the accessing DV resources.**|
|DisplayName|**List of Applications that are in block list for the accessing DV resources.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`blockedapplicationsfordvaccess`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_BlockedAttachments"></a> BlockedAttachments

|Property|Value|
|---|---|
|Description|**Prevent upload or download of certain attachment types that are considered dangerous.**|
|DisplayName|**Block Attachments**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`blockedattachments`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_BlockedMimeTypes"></a> BlockedMimeTypes

|Property|Value|
|---|---|
|Description|**Prevent upload or download of certain mime types that are considered dangerous.**|
|DisplayName|**List of blocked mime types.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`blockedmimetypes`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_BlockTranscriptRecordingForCopilotStudio"></a> BlockTranscriptRecordingForCopilotStudio

|Property|Value|
|---|---|
|Description|**Enable this feature to block access to session transcripts and conversational transcripts from being written to Dataverse for an individual environment**|
|DisplayName|**Block access to session transcripts and conversational transcript recording for Copilot Studio**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`blocktranscriptrecordingforcopilotstudio`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_BoundDashboardDefaultCardExpanded"></a> BoundDashboardDefaultCardExpanded

|Property|Value|
|---|---|
|Description|**Display cards in expanded state for interactive dashboard**|
|DisplayName|**Display cards in expanded state for Interactive Dashboard**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`bounddashboarddefaultcardexpanded`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_bounddashboarddefaultcardexpanded`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_BulkOperationPrefix"></a> BulkOperationPrefix

|Property|Value|
|---|---|
|Description|**Prefix used for bulk operation numbering.**|
|DisplayName|**Bulk Operation Prefix**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`bulkoperationprefix`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_BusinessCardOptions"></a> BusinessCardOptions

|Property|Value|
|---|---|
|Description|**BusinessCardOptions**|
|DisplayName|**Enable New BusinessCardOptions**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`businesscardoptions`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_BusinessClosureCalendarId"></a> BusinessClosureCalendarId

|Property|Value|
|---|---|
|Description|**Unique identifier of the business closure calendar of organization.**|
|DisplayName|**Business Closure Calendar**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`businessclosurecalendarid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_CalendarType"></a> CalendarType

|Property|Value|
|---|---|
|Description|**Calendar type for the system. Set to Gregorian US by default.**|
|DisplayName|**Calendar Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`calendartype`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_CampaignPrefix"></a> CampaignPrefix

|Property|Value|
|---|---|
|Description|**Prefix used for campaign numbering.**|
|DisplayName|**Campaign Prefix**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`campaignprefix`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_CanOptOutNewSearchExperience"></a> CanOptOutNewSearchExperience

|Property|Value|
|---|---|
|Description|**Indicates whether the organization can opt out of the new Relevance search experience (released in Oct 2020)**|
|DisplayName|**Can disable Oct 2020 Search**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`canoptoutnewsearchexperience`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_CascadeStatusUpdate"></a> CascadeStatusUpdate

|Property|Value|
|---|---|
|Description|**Flag to cascade Update on incident.**|
|DisplayName|**Cascade Status Update**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`cascadestatusupdate`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organization_cascadestatusupdate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_CasePrefix"></a> CasePrefix

|Property|Value|
|---|---|
|Description|**Prefix to use for all cases throughout Microsoft Dynamics 365.**|
|DisplayName|**Case Prefix**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`caseprefix`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_CategoryPrefix"></a> CategoryPrefix

|Property|Value|
|---|---|
|Description|**Type the prefix to use for all categories in Microsoft Dynamics 365.**|
|DisplayName|**Category Prefix**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`categoryprefix`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_ClientFeatureSet"></a> ClientFeatureSet

|Property|Value|
|---|---|
|Description|**Client Features to be enabled as an XML BLOB.**|
|DisplayName|**Client Feature Set**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`clientfeatureset`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_ContentSecurityPolicyConfiguration"></a> ContentSecurityPolicyConfiguration

|Property|Value|
|---|---|
|Description|**Policy configuration for CSP**|
|DisplayName|**Content Security Policy Configuration**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`contentsecuritypolicyconfiguration`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_ContentSecurityPolicyConfigurationForCanvas"></a> ContentSecurityPolicyConfigurationForCanvas

|Property|Value|
|---|---|
|Description|**Content Security Policy configuration for Canvas apps.**|
|DisplayName|**Content Security Policy Configuration for Canvas apps**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`contentsecuritypolicyconfigurationforcanvas`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_ContentSecurityPolicyOptions"></a> ContentSecurityPolicyOptions

|Property|Value|
|---|---|
|Description|**Content Security Policy Options.**|
|DisplayName|**Content Security Policy Options**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`contentsecuritypolicyoptions`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|1024|
|MinValue|0|

### <a name="BKMK_ContentSecurityPolicyReportUri"></a> ContentSecurityPolicyReportUri

|Property|Value|
|---|---|
|Description|**Content Security Policy Report Uri.**|
|DisplayName|**Content Security Policy Report Uri**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`contentsecuritypolicyreporturi`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_ContractPrefix"></a> ContractPrefix

|Property|Value|
|---|---|
|Description|**Prefix to use for all contracts throughout Microsoft Dynamics 365.**|
|DisplayName|**Contract Prefix**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`contractprefix`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_CopresenceRefreshRate"></a> CopresenceRefreshRate

|Property|Value|
|---|---|
|Description|**Refresh rate for copresence data in seconds.**|
|DisplayName|**CopresenceRefreshRate**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`copresencerefreshrate`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|30|

### <a name="BKMK_CortanaProactiveExperienceEnabled"></a> CortanaProactiveExperienceEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether the feature CortanaProactiveExperience Flow processes should be enabled for the organization.**|
|DisplayName|**Enable Cortana Proactive Experience Flow processes for this Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`cortanaproactiveexperienceenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_cortanaproactiveexperienceenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_CreateProductsWithoutParentInActiveState"></a> CreateProductsWithoutParentInActiveState

|Property|Value|
|---|---|
|Description|**Enable Initial state of newly created products to be Active instead of Draft**|
|DisplayName|**Enable Active Initial Product State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createproductswithoutparentinactivestate`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_createproductswithoutparentinactivestate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_CurrencyDecimalPrecision"></a> CurrencyDecimalPrecision

|Property|Value|
|---|---|
|Description|**Number of decimal places that can be used for currency.**|
|DisplayName|**Currency Decimal Precision**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`currencydecimalprecision`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|10|
|MinValue|0|

### <a name="BKMK_CurrencyDisplayOption"></a> CurrencyDisplayOption

|Property|Value|
|---|---|
|Description|**Indicates whether to display money fields with currency code or currency symbol.**|
|DisplayName|**Display Currencies Using**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`currencydisplayoption`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`organization_currencydisplayoption`|

#### CurrencyDisplayOption Choices/Options

|Value|Label|
|---|---|
|0|**Currency symbol**|
|1|**Currency code**|

### <a name="BKMK_CurrencyFormatCode"></a> CurrencyFormatCode

|Property|Value|
|---|---|
|Description|**Information about how currency symbols are placed throughout Microsoft Dynamics CRM.**|
|DisplayName|**Currency Format Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`currencyformatcode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`organization_currencyformatcode`|

#### CurrencyFormatCode Choices/Options

|Value|Label|
|---|---|
|0|**$123**|
|1|**123$**|
|2|**$ 123**|
|3|**123 $**|

### <a name="BKMK_CurrencySymbol"></a> CurrencySymbol

|Property|Value|
|---|---|
|Description|**Symbol used for currency throughout Microsoft Dynamics 365.**|
|DisplayName|**Currency Symbol**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`currencysymbol`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|13|

### <a name="BKMK_CurrentBulkOperationNumber"></a> CurrentBulkOperationNumber

|Property|Value|
|---|---|
|Description|**Current bulk operation number. Deprecated. Use SetAutoNumberSeed message.**|
|DisplayName|**Current Bulk Operation Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`currentbulkoperationnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_CurrentCampaignNumber"></a> CurrentCampaignNumber

|Property|Value|
|---|---|
|Description|**Current campaign number. Deprecated. Use SetAutoNumberSeed message.**|
|DisplayName|**Current Campaign Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`currentcampaignnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_CurrentCaseNumber"></a> CurrentCaseNumber

|Property|Value|
|---|---|
|Description|**First case number to use. Deprecated. Use SetAutoNumberSeed message.**|
|DisplayName|**Current Case Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`currentcasenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_CurrentCategoryNumber"></a> CurrentCategoryNumber

|Property|Value|
|---|---|
|Description|**Enter the first number to use for Categories. Deprecated. Use SetAutoNumberSeed message.**|
|DisplayName|**Current Category Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`currentcategorynumber`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_CurrentContractNumber"></a> CurrentContractNumber

|Property|Value|
|---|---|
|Description|**First contract number to use. Deprecated. Use SetAutoNumberSeed message.**|
|DisplayName|**Current Contract Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`currentcontractnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_CurrentInvoiceNumber"></a> CurrentInvoiceNumber

|Property|Value|
|---|---|
|Description|**First invoice number to use. Deprecated. Use SetAutoNumberSeed message.**|
|DisplayName|**Current Invoice Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`currentinvoicenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_CurrentKaNumber"></a> CurrentKaNumber

|Property|Value|
|---|---|
|Description|**Enter the first number to use for knowledge articles. Deprecated. Use SetAutoNumberSeed message.**|
|DisplayName|**Current Knowledge Article Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`currentkanumber`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_CurrentKbNumber"></a> CurrentKbNumber

|Property|Value|
|---|---|
|Description|**First article number to use. Deprecated. Use SetAutoNumberSeed message.**|
|DisplayName|**Current Article Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`currentkbnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_CurrentOrderNumber"></a> CurrentOrderNumber

|Property|Value|
|---|---|
|Description|**First order number to use. Deprecated. Use SetAutoNumberSeed message.**|
|DisplayName|**Current Order Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`currentordernumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_CurrentQuoteNumber"></a> CurrentQuoteNumber

|Property|Value|
|---|---|
|Description|**First quote number to use. Deprecated. Use SetAutoNumberSeed message.**|
|DisplayName|**Current Quote Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`currentquotenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_DateFormatCode"></a> DateFormatCode

|Property|Value|
|---|---|
|Description|**Information about how the date is displayed throughout Microsoft CRM.**|
|DisplayName|**Date Format Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`dateformatcode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`organization_dateformatcode`|

#### DateFormatCode Choices/Options

|Value|Label|
|---|---|

### <a name="BKMK_DateFormatString"></a> DateFormatString

|Property|Value|
|---|---|
|Description|**String showing how the date is displayed throughout Microsoft CRM.**|
|DisplayName|**Date Format String**|
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
|Description|**Character used to separate the month, the day, and the year in dates throughout Microsoft Dynamics 365.**|
|DisplayName|**Date Separator**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`dateseparator`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5|

### <a name="BKMK_DaysBeforeEmailDescriptionIsMigrated"></a> DaysBeforeEmailDescriptionIsMigrated

|Property|Value|
|---|---|
|Description|**Number of days before we migrate email description to blob.**|
|DisplayName|**Number of days before we migrate email description to blob.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`daysbeforeemaildescriptionismigrated`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_DaysBeforeInactiveTeamsChatSyncDisabled"></a> DaysBeforeInactiveTeamsChatSyncDisabled

|Property|Value|
|---|---|
|Description|**Days of inactivity before sync is disabled for a Teams Chat.**|
|DisplayName|**Days Before Inactive Teams Chat Sync Disabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`daysbeforeinactiveteamschatsyncdisabled`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|28|
|MinValue|1|

### <a name="BKMK_DecimalSymbol"></a> DecimalSymbol

|Property|Value|
|---|---|
|Description|**Symbol used for decimal in Microsoft Dynamics 365.**|
|DisplayName|**Decimal Symbol**|
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

### <a name="BKMK_DefaultCrmCustomName"></a> DefaultCrmCustomName

|Property|Value|
|---|---|
|Description|**Name of the default crm custom.**|
|DisplayName|**Name of the default app**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`defaultcrmcustomname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|100|

### <a name="BKMK_DefaultEmailServerProfileId"></a> DefaultEmailServerProfileId

|Property|Value|
|---|---|
|Description|**Unique identifier of the default email server profile.**|
|DisplayName|**Email Server Profile**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`defaultemailserverprofileid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|emailserverprofile|

### <a name="BKMK_DefaultEmailSettings"></a> DefaultEmailSettings

|Property|Value|
|---|---|
|Description|**XML string containing the default email settings that are applied when a user or queue is created.**|
|DisplayName|**Default Email Settings**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`defaultemailsettings`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_DefaultMobileOfflineProfileId"></a> DefaultMobileOfflineProfileId

|Property|Value|
|---|---|
|Description|**Unique identifier of the default mobile offline profile.**|
|DisplayName|**Default Mobile Offline Profile**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`defaultmobileofflineprofileid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mobileofflineprofile|

### <a name="BKMK_DefaultRecurrenceEndRangeType"></a> DefaultRecurrenceEndRangeType

|Property|Value|
|---|---|
|Description|**Type of default recurrence end range date.**|
|DisplayName|**Default Recurrence End Range Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`defaultrecurrenceendrangetype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`organization_defaultrecurrenceendrangetype`|

#### DefaultRecurrenceEndRangeType Choices/Options

|Value|Label|
|---|---|
|1|**No End Date**|
|2|**Number of Occurrences**|
|3|**End By Date**|

### <a name="BKMK_DefaultThemeData"></a> DefaultThemeData

|Property|Value|
|---|---|
|Description|**Default theme data for the organization.**|
|DisplayName|**Default Theme Data**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`defaultthemedata`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_DelegatedAdminUserId"></a> DelegatedAdminUserId

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegated admin user for the organization.**|
|DisplayName|**Delegated Admin**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`delegatedadminuserid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_DesktopFlowQueueLogsTtlInMinutes"></a> DesktopFlowQueueLogsTtlInMinutes

|Property|Value|
|---|---|
|Description|**Default time to live in minutes for new desktop flow queue log records.**|
|DisplayName|**The TTL for new desktop flow queue log records.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`desktopflowqueuelogsttlinminutes`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|33554432|
|MinValue|0|

### <a name="BKMK_DesktopFlowRunActionLogsStatus"></a> DesktopFlowRunActionLogsStatus

|Property|Value|
|---|---|
|Description|**Toggle the activation of the Power Automate Desktop Flow run action logs.**|
|DisplayName|**Desktop Flow Run Action Logs Status**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`desktopflowrunactionlogsstatus`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`organization_desktopflowrunactionlogsstatus`|

#### DesktopFlowRunActionLogsStatus Choices/Options

|Value|Label|
|---|---|
|0|**Enabled**|
|1|**OnFailure**|
|2|**Disabled**|

### <a name="BKMK_DesktopFlowRunActionLogVerbosity"></a> DesktopFlowRunActionLogVerbosity

|Property|Value|
|---|---|
|Description|**What verbosity level the Power Automate Desktop Flow Run Action Logs allow.**|
|DisplayName|**Desktop Flow Run Action Log Verbosity**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`desktopflowrunactionlogverbosity`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`organization_desktopflowrunactionlogverbosity`|

#### DesktopFlowRunActionLogVerbosity Choices/Options

|Value|Label|
|---|---|
|0|**Full**|
|1|**Debug**|
|2|**Custom**|
|3|**Warning**|
|4|**Error**|

### <a name="BKMK_DesktopFlowRunActionLogVersion"></a> DesktopFlowRunActionLogVersion

|Property|Value|
|---|---|
|Description|**Where the Power Automate Desktop Flow Run Action logs are stored.**|
|DisplayName|**Desktop Flow Run Action Log Version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`desktopflowrunactionlogversion`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`organization_desktopflowrunactionlogversion`|

#### DesktopFlowRunActionLogVersion Choices/Options

|Value|Label|
|---|---|
|0|**AdditionalContext**|
|1|**FlowLogs**|
|2|**AdditionalContextAndFlowLogs**|

### <a name="BKMK_DisableSocialCare"></a> DisableSocialCare

|Property|Value|
|---|---|
|Description|**Indicates whether Social Care is disabled.**|
|DisplayName|**Is Social Care disabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`disablesocialcare`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_disablesocialcare`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_DisableSystemLabelsCacheSharing"></a> DisableSystemLabelsCacheSharing

|Property|Value|
|---|---|
|Description|**Disable sharing system labels for the organization.**|
|DisplayName|**Disable System Labels Cache Sharing.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`disablesystemlabelscachesharing`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_disablesystemlabelscachesharing`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_DiscountCalculationMethod"></a> DiscountCalculationMethod

|Property|Value|
|---|---|
|Description|**Discount calculation method for the QOOI product.**|
|DisplayName|**Discount calculation method**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`discountcalculationmethod`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`organization_discountcalculationmethod`|

#### DiscountCalculationMethod Choices/Options

|Value|Label|
|---|---|
|0|**Line item**|
|1|**Per unit**|

### <a name="BKMK_DisplayNavigationTour"></a> DisplayNavigationTour

|Property|Value|
|---|---|
|Description|**Indicates whether or not navigation tour is displayed.**|
|DisplayName|**Display Navigation Tour**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`displaynavigationtour`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_displaynavigationtour`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EmailConnectionChannel"></a> EmailConnectionChannel

|Property|Value|
|---|---|
|Description|**Select if you want to use the Email Router or server-side synchronization for email processing.**|
|DisplayName|**Email Connection Channel**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`emailconnectionchannel`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`organization_emailconnectionchannel`|

#### EmailConnectionChannel Choices/Options

|Value|Label|
|---|---|
|0|**Server-Side Synchronization**|
|1|**Microsoft Dynamics 365 Email Router**|

### <a name="BKMK_EmailCorrelationEnabled"></a> EmailCorrelationEnabled

|Property|Value|
|---|---|
|Description|**Flag to turn email correlation on or off.**|
|DisplayName|**Use Email Correlation**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`emailcorrelationenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_emailcorrelationenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EmailSendPollingPeriod"></a> EmailSendPollingPeriod

|Property|Value|
|---|---|
|Description|**Normal polling frequency used for sending email in Microsoft Office Outlook.**|
|DisplayName|**Email Send Polling Frequency**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`emailsendpollingperiod`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_EnableAsyncMergeAPIForUCI"></a> EnableAsyncMergeAPIForUCI

|Property|Value|
|---|---|
|Description|**Determines whether records merged through the merge dialog in UCI are merged asynchronously**|
|DisplayName|**Asynchronous merge enabled for UCI**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`enableasyncmergeapiforuci`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnableBingMapsIntegration"></a> EnableBingMapsIntegration

|Property|Value|
|---|---|
|Description|**Enable Integration with Bing Maps**|
|DisplayName|**Enable Integration with Bing Maps**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`enablebingmapsintegration`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_enablebingmapsintegration`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnableCanvasAppsInSolutionsByDefault"></a> EnableCanvasAppsInSolutionsByDefault

|Property|Value|
|---|---|
|Description|**Note: By enabling this feature, you will also enable the automatic creation of enviornment variables when adding data sources for your apps.**|
|DisplayName|**Enable the creation of Canvas apps in Dataverse / Solution by default**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`enablecanvasappsinsolutionsbydefault`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnableCopilotStudioCrossGeoShareDataWithVivaInsights"></a> EnableCopilotStudioCrossGeoShareDataWithVivaInsights

|Property|Value|
|---|---|
|Description|**Enable this feature to allow cross-geo boundary sharing of aggregated analytics data if your preferred data location for Viva Insights is different than the location of your environment**|
|DisplayName|**Allow cross-geo boundary sharing of aggregated analytics data if your preferred data location for Viva Insights is different than the location of your environment**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`enablecopilotstudiocrossgeosharedatawithvivainsights`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnableCopilotStudioShareDataWithVI"></a> EnableCopilotStudioShareDataWithVI

|Property|Value|
|---|---|
|Description|**(Deprecated) Enable this feature to allow Copilot Studio to share aggregated analytics data for custom agents with Viva Insights for an individual environment**|
|DisplayName|**(Deprecated) Allow Copilot Studio to share aggregated analytics data for custom agents with Viva Insights**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`enablecopilotstudiosharedatawithvi`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnableCopilotStudioShareDataWithVivaInsights"></a> EnableCopilotStudioShareDataWithVivaInsights

|Property|Value|
|---|---|
|Description|**Enable this feature to allow Copilot Studio to share aggregated analytics data for custom agents with Viva Insights for an individual environment**|
|DisplayName|**Allow Copilot Studio to share aggregated analytics data for custom agents with Viva Insights**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`enablecopilotstudiosharedatawithvivainsights`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnableEnvironmentSettingsApp"></a> EnableEnvironmentSettingsApp

|Property|Value|
|---|---|
|Description|**Enables the Environment Settings App**|
|DisplayName|**Enable Environment Settings App**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`enableenvironmentsettingsapp`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnableFlowsInSolutionByDefault"></a> EnableFlowsInSolutionByDefault

|Property|Value|
|---|---|
|Description|**Indicates whether the creation of flows is within a solution by default for this organization.**|
|DisplayName|**Enable the creation of flows within a solution by default.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`enableflowsinsolutionbydefault`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnableFlowsInSolutionByDefaultGracePeriod"></a> EnableFlowsInSolutionByDefaultGracePeriod

|Property|Value|
|---|---|
|Description|**Organizations with this attribute set to true will be granted a grace period and excluded from the initial world wide enablement of 'creation of flows within a solution by default' functionality. Once the grace period expires, the functionality will be enabled in your organization.**|
|DisplayName|**Indicates whether the organization is opted into a grace period for auto-enablement of 'creation of flows within a solution by default' functionality.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`enableflowsinsolutionbydefaultgraceperiod`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnableImmersiveSkypeIntegration"></a> EnableImmersiveSkypeIntegration

|Property|Value|
|---|---|
|Description|**Enable Integration with Immersive Skype**|
|DisplayName|**Enable Integration with Immersive Skype**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`enableimmersiveskypeintegration`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_enableimmersiveskypeintegration`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnableIpBasedCookieBinding"></a> EnableIpBasedCookieBinding

|Property|Value|
|---|---|
|Description|**Information that specifies whether IP based cookie binding is enabled**|
|DisplayName|**Enable IP Address Based Cookie Binding**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`enableipbasedcookiebinding`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnableIpBasedFirewallRule"></a> EnableIpBasedFirewallRule

|Property|Value|
|---|---|
|Description|**Information that specifies whether IP based firewall rule is enabled**|
|DisplayName|**Enable IP Range based Firewall**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`enableipbasedfirewallrule`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnableIpBasedFirewallRuleInAuditMode"></a> EnableIpBasedFirewallRuleInAuditMode

|Property|Value|
|---|---|
|Description|**Information that specifies whether IP based firewall rule is enabled in Audit Only Mode**|
|DisplayName|**Enable IP Range based Firewall In Audit Only Mode**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`enableipbasedfirewallruleinauditmode`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnableIpBasedStorageAccessSignatureRule"></a> EnableIpBasedStorageAccessSignatureRule

|Property|Value|
|---|---|
|Description|**Information that specifies whether IP based SAS URI generation rule is enabled**|
|DisplayName|**Enable IP SAS URI generation rule**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`enableipbasedstorageaccesssignaturerule`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`_organization_enableipbasedstorageaccesssignaturerule`|
|DefaultValue|False|
|True Label||
|False Label||

### <a name="BKMK_EnableLivePersonaCardUCI"></a> EnableLivePersonaCardUCI

|Property|Value|
|---|---|
|Description|**Indicates whether the user has enabled or disabled Live Persona Card feature in UCI.**|
|DisplayName|**Indicates whether the user has enabled or disabled Live Persona Card feature in UCI.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`enablelivepersonacarduci`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_enablelivepersonacarduci`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnableLivePersonCardIntegrationInOffice"></a> EnableLivePersonCardIntegrationInOffice

|Property|Value|
|---|---|
|Description|**Indicates whether the user has enabled or disabled LivePersonCardIntegration in Office.**|
|DisplayName|**Indicates whether the user has enabled or disabled LivePersonCardIntegration in Office.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`enablelivepersoncardintegrationinoffice`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnableLPAuthoring"></a> EnableLPAuthoring

|Property|Value|
|---|---|
|Description|**Select to enable learning path auhtoring.**|
|DisplayName|**Enable Learning Path Authoring**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`enablelpauthoring`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_enablelpauthoring`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnableMakerSwitchToClassic"></a> EnableMakerSwitchToClassic

|Property|Value|
|---|---|
|Description|**Control whether the organization Switch Maker Portal to Classic**|
|DisplayName|**Switch Maker Portal to Classic**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`enablemakerswitchtoclassic`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnableMicrosoftFlowIntegration"></a> EnableMicrosoftFlowIntegration

|Property|Value|
|---|---|
|Description|**Enable Integration with Microsoft Flow**|
|DisplayName|**Enable Integration with Microsoft Flow**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`enablemicrosoftflowintegration`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_enablemicrosoftflowintegration`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnablePricingOnCreate"></a> EnablePricingOnCreate

|Property|Value|
|---|---|
|Description|**Enable pricing calculations on a Create call.**|
|DisplayName|**Enable Pricing On Create**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`enablepricingoncreate`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_enablepricingoncreate`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnableSmartMatching"></a> EnableSmartMatching

|Property|Value|
|---|---|
|Description|**Use Smart Matching.**|
|DisplayName|**Enable Smart Matching**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`enablesmartmatching`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organization_enablesmartmatching`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnableUnifiedClientCDN"></a> EnableUnifiedClientCDN

|Property|Value|
|---|---|
|Description|**Leave empty to use default setting. Set to on/off to enable/disable CDN for UCI.**|
|DisplayName|**Enable UCI CDN for organization**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`enableunifiedclientcdn`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnableUnifiedInterfaceShellRefresh"></a> EnableUnifiedInterfaceShellRefresh

|Property|Value|
|---|---|
|Description|**Enable site map and commanding update**|
|DisplayName|**Enable site map and commanding update**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`enableunifiedinterfaceshellrefresh`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnforceReadOnlyPlugins"></a> EnforceReadOnlyPlugins

|Property|Value|
|---|---|
|Description|**Organization setting to enforce read only plugins.**|
|DisplayName|**Organization setting to enforce read only plugins.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`enforcereadonlyplugins`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_enforcereadonlyplugins`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EntityImage"></a> EntityImage

|Property|Value|
|---|---|
|Description|**The default image for the entity.**|
|DisplayName|**Entity Image**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimage`|
|RequiredLevel|None|
|Type|Image|
|CanStoreFullImage|False|
|IsPrimaryImage|True|
|MaxHeight|144|
|MaxSizeInKB|10240|
|MaxWidth|144|

### <a name="BKMK_ExpireChangeTrackingInDays"></a> ExpireChangeTrackingInDays

|Property|Value|
|---|---|
|Description|**Maximum number of days to keep change tracking deleted records**|
|DisplayName|**Days to Expire Change Tracking Deleted Records**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`expirechangetrackingindays`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|365|
|MinValue|0|

### <a name="BKMK_ExpireSubscriptionsInDays"></a> ExpireSubscriptionsInDays

|Property|Value|
|---|---|
|Description|**Maximum number of days before deleting inactive subscriptions.**|
|DisplayName|**Days to Expire Subscriptions**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`expiresubscriptionsindays`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ExternalBaseUrl"></a> ExternalBaseUrl

|Property|Value|
|---|---|
|Description|**Specify the base URL to use to look for external document suggestions.**|
|DisplayName|**External Base URL**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`externalbaseurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_ExternalPartyCorrelationKeys"></a> ExternalPartyCorrelationKeys

|Property|Value|
|---|---|
|Description|**XML string containing the ExternalPartyEnabled entities correlation keys for association of existing External Party instance entities to newly created IsExternalPartyEnabled entities.For internal use only**|
|DisplayName|**ExternalPartyEnabled Entities correlation Keys**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`externalpartycorrelationkeys`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_ExternalPartyEntitySettings"></a> ExternalPartyEntitySettings

|Property|Value|
|---|---|
|Description|**XML string containing the ExternalPartyEnabled entities settings.**|
|DisplayName|**ExternalPartyEnabled Entities Settings.For internal use only**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`externalpartyentitysettings`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_FeatureSet"></a> FeatureSet

|Property|Value|
|---|---|
|Description|**Features to be enabled as an XML BLOB.**|
|DisplayName|**Feature Set**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`featureset`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_FiscalCalendarStart"></a> FiscalCalendarStart

|Property|Value|
|---|---|
|Description|**Start date for the fiscal period that is to be used throughout Microsoft CRM.**|
|DisplayName|**Fiscal Calendar Start**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fiscalcalendarstart`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_FiscalPeriodFormat"></a> FiscalPeriodFormat

|Property|Value|
|---|---|
|Description|**Information that specifies how the name of the fiscal period is displayed throughout Microsoft CRM.**|
|DisplayName|**Fiscal Period Format**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fiscalperiodformat`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|25|

### <a name="BKMK_FiscalPeriodFormatPeriod"></a> FiscalPeriodFormatPeriod

|Property|Value|
|---|---|
|Description|**Format in which the fiscal period will be displayed.**|
|DisplayName|**Format for Fiscal Period**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fiscalperiodformatperiod`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`organization_fiscalperiodformat`|

#### FiscalPeriodFormatPeriod Choices/Options

|Value|Label|
|---|---|
|1|**Quarter \{0\}**|
|2|**Q\{0\}**|
|3|**P\{0\}**|
|4|**Month \{0\}**|
|5|**M\{0\}**|
|6|**Semester \{0\}**|
|7|**Month Name**|

### <a name="BKMK_FiscalPeriodType"></a> FiscalPeriodType

|Property|Value|
|---|---|
|Description|**Type of fiscal period used throughout Microsoft CRM.**|
|DisplayName|**Fiscal Period Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fiscalperiodtype`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_FiscalYearDisplayCode"></a> FiscalYearDisplayCode

|Property|Value|
|---|---|
|Description|**Information that specifies whether the fiscal year should be displayed based on the start date or the end date of the fiscal year.**|
|DisplayName|**Fiscal Year Display**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fiscalyeardisplaycode`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_FiscalYearFormat"></a> FiscalYearFormat

|Property|Value|
|---|---|
|Description|**Information that specifies how the name of the fiscal year is displayed throughout Microsoft CRM.**|
|DisplayName|**Fiscal Year Format**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fiscalyearformat`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|25|

### <a name="BKMK_FiscalYearFormatPrefix"></a> FiscalYearFormatPrefix

|Property|Value|
|---|---|
|Description|**Prefix for the display of the fiscal year.**|
|DisplayName|**Prefix for Fiscal Year**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fiscalyearformatprefix`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`organization_fiscalyearformatprefix`|

#### FiscalYearFormatPrefix Choices/Options

|Value|Label|
|---|---|
|1|**FY**|
|2|`No label value`|

### <a name="BKMK_FiscalYearFormatSuffix"></a> FiscalYearFormatSuffix

|Property|Value|
|---|---|
|Description|**Suffix for the display of the fiscal year.**|
|DisplayName|**Suffix for Fiscal Year**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fiscalyearformatsuffix`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`organization_fiscalyearformatsuffix`|

#### FiscalYearFormatSuffix Choices/Options

|Value|Label|
|---|---|
|1|**FY**|
|2|**Fiscal Year**|
|3|`No label value`|

### <a name="BKMK_FiscalYearFormatYear"></a> FiscalYearFormatYear

|Property|Value|
|---|---|
|Description|**Format for the year.**|
|DisplayName|**Fiscal Year Format Year**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fiscalyearformatyear`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`organization_fiscalyearformatyear`|

#### FiscalYearFormatYear Choices/Options

|Value|Label|
|---|---|
|1|**YYYY**|
|2|**YY**|
|3|**GGYY**|

### <a name="BKMK_FiscalYearPeriodConnect"></a> FiscalYearPeriodConnect

|Property|Value|
|---|---|
|Description|**Information that specifies how the names of the fiscal year and the fiscal period should be connected when displayed together.**|
|DisplayName|**Fiscal Year Period Connector**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fiscalyearperiodconnect`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5|

### <a name="BKMK_FlowLogsTtlInMinutes"></a> FlowLogsTtlInMinutes

|Property|Value|
|---|---|
|Description|**Default time to live in minutes for new records in the Flow Logs entity.**|
|DisplayName|**The TTL for records in the Flow Logs Entity.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`flowlogsttlinminutes`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|33554432|
|MinValue|0|

### <a name="BKMK_FlowRunTimeToLiveInSeconds"></a> FlowRunTimeToLiveInSeconds

|Property|Value|
|---|---|
|Description|**Time to live (in seconds) for flow run**|
|DisplayName|**Time to live (in seconds) for flow run**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`flowruntimetoliveinseconds`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_FullNameConventionCode"></a> FullNameConventionCode

|Property|Value|
|---|---|
|Description|**Order in which names are to be displayed throughout Microsoft CRM.**|
|DisplayName|**Full Name Display Order**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fullnameconventioncode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`organization_fullnameconventioncode`|

#### FullNameConventionCode Choices/Options

|Value|Label|
|---|---|
|0|**Last Name, First Name**|
|1|**First Name**|
|2|**Last Name, First Name, Middle Initial**|
|3|**First Name, Middle Initial, Last Name**|
|4|**Last Name, First Name, Middle Name**|
|5|**First Name, Middle Name, Last Name**|
|6|**Last Name, space, First Name**|
|7|**Last Name, no space, First Name**|

### <a name="BKMK_FutureExpansionWindow"></a> FutureExpansionWindow

|Property|Value|
|---|---|
|Description|**Specifies the maximum number of months in future for which the recurring activities can be created.**|
|DisplayName|**Future Expansion Window**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`futureexpansionwindow`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|140|
|MinValue|1|

### <a name="BKMK_GenerateAlertsForErrors"></a> GenerateAlertsForErrors

|Property|Value|
|---|---|
|Description|**Indicates whether alerts will be generated for errors.**|
|DisplayName|**Generate Alerts For Errors**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`generatealertsforerrors`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_generatealertsforerrors`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_GenerateAlertsForInformation"></a> GenerateAlertsForInformation

|Property|Value|
|---|---|
|Description|**Indicates whether alerts will be generated for information.**|
|DisplayName|**Generate Alerts For Information**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`generatealertsforinformation`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_generatealertsforinformation`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_GenerateAlertsForWarnings"></a> GenerateAlertsForWarnings

|Property|Value|
|---|---|
|Description|**Indicates whether alerts will be generated for warnings.**|
|DisplayName|**Generate Alerts For Warnings**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`generatealertsforwarnings`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_generatealertsforwarnings`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_GetStartedPaneContentEnabled"></a> GetStartedPaneContentEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether Get Started content is enabled for this organization.**|
|DisplayName|**Is Get Started Pane Content Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`getstartedpanecontentenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_getstartedpanecontentenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_GlobalAppendUrlParametersEnabled"></a> GlobalAppendUrlParametersEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether the append URL parameters is enabled.**|
|DisplayName|**Is AppendUrl Parameters enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`globalappendurlparametersenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_globalappendurlparametersenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_GlobalHelpUrl"></a> GlobalHelpUrl

|Property|Value|
|---|---|
|Description|**URL for the web page global help.**|
|DisplayName|**Global Help URL.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`globalhelpurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_GlobalHelpUrlEnabled"></a> GlobalHelpUrlEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether the customizable global help is enabled.**|
|DisplayName|**Is Customizable Global Help enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`globalhelpurlenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_globalhelpurlenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_GoalRollupExpiryTime"></a> GoalRollupExpiryTime

|Property|Value|
|---|---|
|Description|**Number of days after the goal's end date after which the rollup of the goal stops automatically.**|
|DisplayName|**Rollup Expiration Time for Goal**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`goalrollupexpirytime`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|400|
|MinValue|0|

### <a name="BKMK_GoalRollupFrequency"></a> GoalRollupFrequency

|Property|Value|
|---|---|
|Description|**Number of hours between automatic rollup jobs .**|
|DisplayName|**Automatic Rollup Frequency for Goal**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`goalrollupfrequency`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|1|

### <a name="BKMK_GrantAccessToNetworkService"></a> GrantAccessToNetworkService

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Grant Access To Network Service**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`grantaccesstonetworkservice`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organization_grantaccesstonetworkservice`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_HashDeltaSubjectCount"></a> HashDeltaSubjectCount

|Property|Value|
|---|---|
|Description|**Maximum difference allowed between subject keywords count of the email messaged to be correlated**|
|DisplayName|**Hash Delta Subject Count**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`hashdeltasubjectcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_HashFilterKeywords"></a> HashFilterKeywords

|Property|Value|
|---|---|
|Description|**Filter Subject Keywords**|
|DisplayName|**Hash Filter Keywords**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`hashfilterkeywords`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_HashMaxCount"></a> HashMaxCount

|Property|Value|
|---|---|
|Description|**Maximum number of subject keywords or recipients used for correlation**|
|DisplayName|**Hash Max Count**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`hashmaxcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_HashMinAddressCount"></a> HashMinAddressCount

|Property|Value|
|---|---|
|Description|**Minimum number of recipients required to match for email messaged to be correlated**|
|DisplayName|**Hash Min Address Count**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`hashminaddresscount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_HighContrastThemeData"></a> HighContrastThemeData

|Property|Value|
|---|---|
|Description|**High contrast theme data for the organization.**|
|DisplayName|**High contrast Theme Data**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`highcontrastthemedata`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_IgnoreInternalEmail"></a> IgnoreInternalEmail

|Property|Value|
|---|---|
|Description|**Indicates whether incoming email sent by internal Microsoft Dynamics 365 users or queues should be tracked.**|
|DisplayName|**Ignore Internal Email**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ignoreinternalemail`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_ignoreinternalemail`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ImproveSearchLoggingEnabled"></a> ImproveSearchLoggingEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether an organization has consented to sharing search query data to help improve search results**|
|DisplayName|**Share search query data**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`improvesearchloggingenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_InactivityTimeoutEnabled"></a> InactivityTimeoutEnabled

|Property|Value|
|---|---|
|Description|**Information that specifies whether Inactivity timeout is enabled**|
|DisplayName|**Inactivity timeout enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`inactivitytimeoutenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_InactivityTimeoutInMins"></a> InactivityTimeoutInMins

|Property|Value|
|---|---|
|Description|**Inactivity timeout in minutes**|
|DisplayName|**Inactivity timeout in minutes**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`inactivitytimeoutinmins`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_InactivityTimeoutReminderInMins"></a> InactivityTimeoutReminderInMins

|Property|Value|
|---|---|
|Description|**Inactivity timeout reminder in minutes**|
|DisplayName|**Inactivity timeout reminder in minutes**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`inactivitytimeoutreminderinmins`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_IncomingEmailExchangeEmailRetrievalBatchSize"></a> IncomingEmailExchangeEmailRetrievalBatchSize

|Property|Value|
|---|---|
|Description|**Setting for the Async Service Mailbox Queue. Defines the retrieval batch size of exchange server.**|
|DisplayName|**Exchange Email Retrieval Batch Size**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`incomingemailexchangeemailretrievalbatchsize`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|1|

### <a name="BKMK_InitialVersion"></a> InitialVersion

|Property|Value|
|---|---|
|Description|**Initial version of the organization.**|
|DisplayName|**Initial Version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`initialversion`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_IntegrationUserId"></a> IntegrationUserId

|Property|Value|
|---|---|
|Description|**Unique identifier of the integration user for the organization.**|
|DisplayName|**Integration User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`integrationuserid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_InvoicePrefix"></a> InvoicePrefix

|Property|Value|
|---|---|
|Description|**Prefix to use for all invoice numbers throughout Microsoft Dynamics 365.**|
|DisplayName|**Invoice Prefix**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`invoiceprefix`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_IpBasedStorageAccessSignatureMode"></a> IpBasedStorageAccessSignatureMode

|Property|Value|
|---|---|
|Description|**IP Based SAS mode.**|
|DisplayName|**IP Based SAS mode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ipbasedstorageaccesssignaturemode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`ipbasedstorageaccesssignaturemode`|

#### IpBasedStorageAccessSignatureMode Choices/Options

|Value|Label|
|---|---|
|0|**IP Binding only**|
|1|**IP Firewall only**|
|2|**IP Binding and IP Firewall**|
|3|**IP Binding or IP Firewall**|

### <a name="BKMK_IsActionCardEnabled"></a> IsActionCardEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether the feature Action Card should be enabled for the organization.**|
|DisplayName|**Enable Action Card for this Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isactioncardenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsActionSupportFeatureEnabled"></a> IsActionSupportFeatureEnabled

|Property|Value|
|---|---|
|Description|**Information that specifies whether Action Support Feature is enabled**|
|DisplayName|**Action Support Feature enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isactionsupportfeatureenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsActivityAnalysisEnabled"></a> IsActivityAnalysisEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether the feature Relationship Analytics should be enabled for the organization.**|
|DisplayName|**Enable Relationship Analytics for this Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isactivityanalysisenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsAppMode"></a> IsAppMode

|Property|Value|
|---|---|
|Description|**Indicates whether loading of Microsoft Dynamics 365 in a browser window that does not have address, tool, and menu bars is enabled.**|
|DisplayName|**Is Application Mode Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isappmode`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isappmode`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsAppointmentAttachmentSyncEnabled"></a> IsAppointmentAttachmentSyncEnabled

|Property|Value|
|---|---|
|Description|**Enable or disable attachments sync for outlook and exchange.**|
|DisplayName|**Is Attachment Sync Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isappointmentattachmentsyncenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isappointmentattachmentsyncenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsAssignedTasksSyncEnabled"></a> IsAssignedTasksSyncEnabled

|Property|Value|
|---|---|
|Description|**Enable or disable assigned tasks sync for outlook and exchange.**|
|DisplayName|**Is Assigned Tasks Sync Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isassignedtaskssyncenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isassignedtaskssyncenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsAuditEnabled"></a> IsAuditEnabled

|Property|Value|
|---|---|
|Description|**Enable or disable auditing of changes.**|
|DisplayName|**Is Auditing Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isauditenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isauditenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsAutoDataCaptureEnabled"></a> IsAutoDataCaptureEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether the feature Auto Capture should be enabled for the organization.**|
|DisplayName|**Enable Auto Capture for this Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isautodatacaptureenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsAutoDataCaptureV2Enabled"></a> IsAutoDataCaptureV2Enabled

|Property|Value|
|---|---|
|Description|**Indicates whether the V2 feature of Auto Capture should be enabled for the organization.**|
|DisplayName|**Enable Auto Capture V2 for this Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isautodatacapturev2enabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsAutoInstallAppForD365InTeamsEnabled"></a> IsAutoInstallAppForD365InTeamsEnabled

|Property|Value|
|---|---|
|Description||
|DisplayName|**IsAutoInstallAppForD365InTeamsEnabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isautoinstallappford365inteamsenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isautoinstallappford365inteamsenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsAutoSaveEnabled"></a> IsAutoSaveEnabled

|Property|Value|
|---|---|
|Description|**Information on whether auto save is enabled.**|
|DisplayName|**Auto Save Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isautosaveenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isautosaveenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsBaseCardStaticFieldDataEnabled"></a> IsBaseCardStaticFieldDataEnabled

|Property|Value|
|---|---|
|Description||
|DisplayName|**IsBaseCardStaticFieldDataEnabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isbasecardstaticfielddataenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isbasecardstaticfielddataenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsBasicGeospatialIntegrationEnabled"></a> IsBasicGeospatialIntegrationEnabled

|Property|Value|
|---|---|
|Description|**Determines whether users can make use of basic Geospatial featuers in Canvas apps.**|
|DisplayName|**Enable the basic Geospatial features in Canvas Apps**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isbasicgeospatialintegrationenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsBPFEntityCustomizationFeatureEnabled"></a> IsBPFEntityCustomizationFeatureEnabled

|Property|Value|
|---|---|
|Description|**Information that specifies whether BPF Entity Customization Feature is enabled**|
|DisplayName|**BPF Entity Customization Feature enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isbpfentitycustomizationfeatureenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsCloudFlowSavingsEnabled"></a> IsCloudFlowSavingsEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether Power Automate savings feature is enabled for Cloudflow.**|
|DisplayName|**Enable Power Automate savings feature for Cloudflow**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscloudflowsavingsenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsCollaborationExperienceEnabled"></a> IsCollaborationExperienceEnabled

|Property|Value|
|---|---|
|Description||
|DisplayName|**IsCollaborationExperienceEnabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscollaborationexperienceenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_iscollaborationexperienceenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsComputerUseInMCSEnabled"></a> IsComputerUseInMCSEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether Computer Use in MCS feature is enabled in this organization.**|
|DisplayName|**Enable Computer Use in MCS feature for this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscomputeruseinmcsenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsConflictDetectionEnabledForMobileClient"></a> IsConflictDetectionEnabledForMobileClient

|Property|Value|
|---|---|
|Description|**Information that specifies whether conflict detection for mobile client is enabled.**|
|DisplayName|**Is Conflict Detection for Mobile Client enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isconflictdetectionenabledformobileclient`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsContactMailingAddressSyncEnabled"></a> IsContactMailingAddressSyncEnabled

|Property|Value|
|---|---|
|Description|**Enable or disable mailing address sync for outlook and exchange.**|
|DisplayName|**Is Mailing Address Sync Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscontactmailingaddresssyncenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_iscontactmailingaddresssyncenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsContentSecurityPolicyEnabled"></a> IsContentSecurityPolicyEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether Content Security Policy has been enabled for the organization.**|
|DisplayName|**Enable Content Security Policy for this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscontentsecuritypolicyenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsContentSecurityPolicyEnabledForCanvas"></a> IsContentSecurityPolicyEnabledForCanvas

|Property|Value|
|---|---|
|Description|**Indicates whether Content Security Policy has been enabled for this organization's Canvas apps.**|
|DisplayName|**Enable Content Security Policy for this organization's Canvas apps**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`iscontentsecuritypolicyenabledforcanvas`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsContextualEmailEnabled"></a> IsContextualEmailEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether Contextual email experience is enabled on this organization**|
|DisplayName|**Indicates whether Contextual email experience is enabled on this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscontextualemailenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsContextualHelpEnabled"></a> IsContextualHelpEnabled

|Property|Value|
|---|---|
|Description|**Select to enable Contextual Help in UCI.**|
|DisplayName|**Enables Contextual Help in UCI**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscontextualhelpenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsCopilotFeedbackEnabled"></a> IsCopilotFeedbackEnabled

|Property|Value|
|---|---|
|Description|**Determines whether users can provide feedback Copilot experiences.**|
|DisplayName|**Allow users to provide feedback to improve Copilot experiences**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`iscopilotfeedbackenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsCustomControlsInCanvasAppsEnabled"></a> IsCustomControlsInCanvasAppsEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether Custom Controls in canvas PowerApps feature has been enabled for the organization.**|
|DisplayName|**Enable Custom Controls in canvas PowerApps feature for this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomcontrolsincanvasappsenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsDefaultCountryCodeCheckEnabled"></a> IsDefaultCountryCodeCheckEnabled

|Property|Value|
|---|---|
|Description|**Enable or disable country code selection.**|
|DisplayName|**Enable or disable country code selection**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isdefaultcountrycodecheckenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_iscountrycodeselectionenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsDelegateAccessEnabled"></a> IsDelegateAccessEnabled

|Property|Value|
|---|---|
|Description|**Enable Delegation Access content**|
|DisplayName|**Is Delegation Access Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isdelegateaccessenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isdelegationaccessenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsDelveActionHubIntegrationEnabled"></a> IsDelveActionHubIntegrationEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether the feature Action Hub should be enabled for the organization.**|
|DisplayName|**Enable Action Hub for this Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isdelveactionhubintegrationenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsDesktopFlowConnectionEmbeddingEnabled"></a> IsDesktopFlowConnectionEmbeddingEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether connection embedding in Desktop Flows is enabled in this organization.**|
|DisplayName|**Enable connection embedding in Desktop Flows for this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isdesktopflowconnectionembeddingenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsDesktopFlowRuntimeRepairAttendedEnabled"></a> IsDesktopFlowRuntimeRepairAttendedEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether the Desktop Flows UI Automation Runtime Repair for Attended feature for this organization.**|
|DisplayName|**Enable the Desktop Flows UI Automation Runtime Repair for Attended feature for this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isdesktopflowruntimerepairattendedenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsDesktopFlowRuntimeRepairUnattendedEnabled"></a> IsDesktopFlowRuntimeRepairUnattendedEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether the Desktop Flows UI Automation Runtime Repair for Unattended feature for this organization.**|
|DisplayName|**Enable the Desktop Flows UI Automation Runtime Repair for Unattended feature for this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isdesktopflowruntimerepairunattendedenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsDesktopFlowSavingsEnabled"></a> IsDesktopFlowSavingsEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether Power Automate savings feature is enabled for Desktopflow.**|
|DisplayName|**Enable Power Automate savings feature for Desktopflow**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isdesktopflowsavingsenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsDesktopFlowSchemaV2Enabled"></a> IsDesktopFlowSchemaV2Enabled

|Property|Value|
|---|---|
|Description|**Indicates whether v2 schema for Desktop Flows is enabled in this organization.**|
|DisplayName|**Enable v2 schema for Desktop Flows in this organization.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isdesktopflowschemav2enabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsDesktopFlowVanillaImageSharingEnabled"></a> IsDesktopFlowVanillaImageSharingEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether Windows Vanilla Image will be available for Desktop Flow users in this organization.**|
|DisplayName|**Enable Sharing the Windows Vanilla Image with every Desktop Flow user in this organization.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isdesktopflowvanillaimagesharingenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsDuplicateDetectionEnabled"></a> IsDuplicateDetectionEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether duplicate detection of records is enabled.**|
|DisplayName|**Is Duplicate Detection Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isduplicatedetectionenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isduplicatedetectionenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsDuplicateDetectionEnabledForImport"></a> IsDuplicateDetectionEnabledForImport

|Property|Value|
|---|---|
|Description|**Indicates whether duplicate detection of records during import is enabled.**|
|DisplayName|**Is Duplicate Detection Enabled For Import**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isduplicatedetectionenabledforimport`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isduplicatedetectionenabledforimport`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsDuplicateDetectionEnabledForOfflineSync"></a> IsDuplicateDetectionEnabledForOfflineSync

|Property|Value|
|---|---|
|Description|**Indicates whether duplicate detection of records during offline synchronization is enabled.**|
|DisplayName|**Is Duplicate Detection Enabled For Offline Synchronization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isduplicatedetectionenabledforofflinesync`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isduplicatedetectionenabledforofflinesync`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsDuplicateDetectionEnabledForOnlineCreateUpdate"></a> IsDuplicateDetectionEnabledForOnlineCreateUpdate

|Property|Value|
|---|---|
|Description|**Indicates whether duplicate detection during online create or update is enabled.**|
|DisplayName|**Is Duplicate Detection Enabled for Online Create/Update**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isduplicatedetectionenabledforonlinecreateupdate`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isduplicatedetectionenabledforonlinecreateupdate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsEmailAddressValidationEnabled"></a> IsEmailAddressValidationEnabled

|Property|Value|
|---|---|
|Description|**Information on whether Smart Email Address Validation is enabled.**|
|DisplayName|**Enable Smart Email Address Validation.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isemailaddressvalidationenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isemailaddressvalidationenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsEmailMonitoringAllowed"></a> IsEmailMonitoringAllowed

|Property|Value|
|---|---|
|Description|**Allow tracking recipient activity on sent emails.**|
|DisplayName|**Allow tracking recipient activity on sent emails**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isemailmonitoringallowed`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isemailmonitoringallowed`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsEmailServerProfileContentFilteringEnabled"></a> IsEmailServerProfileContentFilteringEnabled

|Property|Value|
|---|---|
|Description|**Enable Email Server Profile content filtering**|
|DisplayName|**Is Email Server Profile Content Filtering Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isemailserverprofilecontentfilteringenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isemailserverprofilecontentfilteringenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsEnabledForAllRoles"></a> IsEnabledForAllRoles

|Property|Value|
|---|---|
|Description|**Indicates whether appmodule is enabled for all roles**|
|DisplayName|**option set values for isenabledforallroles**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isenabledforallroles`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isenabledforallroles`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsExternalFileStorageEnabled"></a> IsExternalFileStorageEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether the organization's files are being stored in Azure.**|
|DisplayName|**Enable external file storage**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isexternalfilestorageenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isexternalfilestorageenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsExternalSearchIndexEnabled"></a> IsExternalSearchIndexEnabled

|Property|Value|
|---|---|
|Description|**Select whether data can be synchronized with an external search index.**|
|DisplayName|**Enable external search data syncing**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isexternalsearchindexenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isexternalsearchindexenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsFiscalPeriodMonthBased"></a> IsFiscalPeriodMonthBased

|Property|Value|
|---|---|
|Description|**Indicates whether the fiscal period is displayed as the month number.**|
|DisplayName|**Is Fiscal Period Monthly**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isfiscalperiodmonthbased`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isfiscalperiodmonthbased`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsFolderAutoCreatedonSP"></a> IsFolderAutoCreatedonSP

|Property|Value|
|---|---|
|Description|**Select whether folders should be automatically created on SharePoint.**|
|DisplayName|**Automatically create folders**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isfolderautocreatedonsp`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsFolderBasedTrackingEnabled"></a> IsFolderBasedTrackingEnabled

|Property|Value|
|---|---|
|Description|**Enable or disable folder based tracking for Server Side Sync.**|
|DisplayName|**Is Folder Based Tracking Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isfolderbasedtrackingenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isfolderbasedtrackingenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsFullTextSearchEnabled"></a> IsFullTextSearchEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether full-text search for Quick Find entities should be enabled for the organization.**|
|DisplayName|**Enable Full-text search for Quick Find**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isfulltextsearchenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isfulltextsearchenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsGeospatialAzureMapsIntegrationEnabled"></a> IsGeospatialAzureMapsIntegrationEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether geospatial capabilities leveraging Azure Maps are enabled.**|
|DisplayName|**Enable geospatial Azure Maps integration.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isgeospatialazuremapsintegrationenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsHierarchicalSecurityModelEnabled"></a> IsHierarchicalSecurityModelEnabled

|Property|Value|
|---|---|
|Description|**Enable Hierarchical Security Model**|
|DisplayName|**Enable Hierarchical Security Model**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ishierarchicalsecuritymodelenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_hierarchicalsecuritymodelenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsIdeasDataCollectionEnabled"></a> IsIdeasDataCollectionEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether data collection for ideas in canvas PowerApps has been enabled.**|
|DisplayName|**Enable Ideas data collection.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isideasdatacollectionenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsLUISEnabledforD365Bot"></a> IsLUISEnabledforD365Bot

|Property|Value|
|---|---|
|Description|**Give Consent to use LUIS in Dynamics 365 Bot**|
|DisplayName|**LUIS Consent for Dynamics 365 Bot**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isluisenabledford365bot`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsMailboxForcedUnlockingEnabled"></a> IsMailboxForcedUnlockingEnabled

|Property|Value|
|---|---|
|Description|**Enable or disable forced unlocking for Server Side Sync mailboxes.**|
|DisplayName|**Is Mailbox Forced Unlocking Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismailboxforcedunlockingenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_ismailboxforcedunlockingenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsMailboxInactiveBackoffEnabled"></a> IsMailboxInactiveBackoffEnabled

|Property|Value|
|---|---|
|Description|**Enable or disable mailbox keep alive for Server Side Sync.**|
|DisplayName|**Is Mailbox Keep Alive Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismailboxinactivebackoffenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_ismailboxinactivebackoffenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsManualSalesForecastingEnabled"></a> IsManualSalesForecastingEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether Manual Sales Forecasting feature has been enabled for the organization.**|
|DisplayName|**Enable Manual Sales Forecasting feature for this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanualsalesforecastingenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsMobileClientOnDemandSyncEnabled"></a> IsMobileClientOnDemandSyncEnabled

|Property|Value|
|---|---|
|Description|**Information that specifies whether mobile client on demand sync is enabled.**|
|DisplayName|**Is Mobile Client On Demand Sync enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismobileclientondemandsyncenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsMobileOfflineEnabled"></a> IsMobileOfflineEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether the feature MobileOffline should be enabled for the organization.**|
|DisplayName|**Enable MobileOffline for this Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismobileofflineenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_ismobileofflineenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsModelDrivenAppsInMSTeamsEnabled"></a> IsModelDrivenAppsInMSTeamsEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether Model Apps can be embedded within Microsoft Teams. This is a tenant admin controlled preview/experimental feature.**|
|DisplayName|**Enable embedding Model Apps in Microsoft Teams**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismodeldrivenappsinmsteamsenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsMoneySavingsAllowed"></a> IsMoneySavingsAllowed

|Property|Value|
|---|---|
|Description|**Indicates whether the maker can create Power Automate money based saving rules.**|
|DisplayName|**Enable the ability to makers to create Power Automate money savings rule**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismoneysavingsallowed`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsMSTeamsCollaborationEnabled"></a> IsMSTeamsCollaborationEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether Microsoft Teams Collaboration feature has been enabled for the organization.**|
|DisplayName|**Enable Microsoft Teams Collaboration for this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismsteamscollaborationenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsMSTeamsEnabled"></a> IsMSTeamsEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether Microsoft Teams integration has been enabled for the organization.**|
|DisplayName|**Enable Microsoft Teams integration**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismsteamsenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsMSTeamsSettingChangedByUser"></a> IsMSTeamsSettingChangedByUser

|Property|Value|
|---|---|
|Description|**Indicates whether the user has enabled or disabled Microsoft Teams integration.**|
|DisplayName|**Microsoft Teams integration changed by user**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismsteamssettingchangedbyuser`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_msteamssettingchangedbyuser`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsMSTeamsUserSyncEnabled"></a> IsMSTeamsUserSyncEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether Microsoft Teams User Sync feature has been enabled for the organization.**|
|DisplayName|**Enable Microsoft Teams User Sync for this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismsteamsusersyncenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsNewAddProductExperienceEnabled"></a> IsNewAddProductExperienceEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether new add product experience is enabled.**|
|DisplayName|**Indicates whether new add product experience is enabled in opportunity form**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isnewaddproductexperienceenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsNotesAnalysisEnabled"></a> IsNotesAnalysisEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether the feature Notes Analysis should be enabled for the organization.**|
|DisplayName|**Enable Notes Analysis for this Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isnotesanalysisenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsNotificationForD365InTeamsEnabled"></a> IsNotificationForD365InTeamsEnabled

|Property|Value|
|---|---|
|Description||
|DisplayName|**IsNotificationForD365InTeamsEnabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isnotificationford365inteamsenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isnotificationford365inteamsenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsOfficeGraphEnabled"></a> IsOfficeGraphEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether the feature OfficeGraph should be enabled for the organization.**|
|DisplayName|**Enable OfficeGraph for this Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isofficegraphenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isofficegraphenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsOneDriveEnabled"></a> IsOneDriveEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether the feature One Drive should be enabled for the organization.**|
|DisplayName|**Enable One Drive for this Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isonedriveenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isonedriveenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsPAIEnabled"></a> IsPAIEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether PAI feature has been enabled for the organization.**|
|DisplayName|**Enable PAI feature for this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ispaienabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsPDFGenerationEnabled"></a> IsPDFGenerationEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether PDF Generation feature has been enabled for the organization.**|
|DisplayName|**Enable PDF Generation feature for this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ispdfgenerationenabled`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_IsPerProcessCapacityOverageEnabled"></a> IsPerProcessCapacityOverageEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether the Per Process overage feature is enabled in this organization.**|
|DisplayName|**Enable the Per Process overage feature for this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isperprocesscapacityoverageenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsPlaybookEnabled"></a> IsPlaybookEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether playbook feature has been enabled for the organization.**|
|DisplayName|**Enable playbook feature for this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isplaybookenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsPresenceEnabled"></a> IsPresenceEnabled

|Property|Value|
|---|---|
|Description|**Information on whether IM presence is enabled.**|
|DisplayName|**Presence Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ispresenceenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organization_ispresenceenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsPreviewEnabledForActionCard"></a> IsPreviewEnabledForActionCard

|Property|Value|
|---|---|
|Description|**Indicates whether the Preview feature for Action Card should be enabled for the organization.**|
|DisplayName|**Enable Preview Action Card feature for this Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ispreviewenabledforactioncard`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsPreviewForAutoCaptureEnabled"></a> IsPreviewForAutoCaptureEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether the feature Auto Capture should be enabled for the organization at Preview Settings.**|
|DisplayName|**Enable Auto Capture for this Organization at Preview Settings**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ispreviewforautocaptureenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsPreviewForEmailMonitoringAllowed"></a> IsPreviewForEmailMonitoringAllowed

|Property|Value|
|---|---|
|Description|**Is Preview For Email Monitoring Allowed.**|
|DisplayName|**Allows Preview For Email Monitoring**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ispreviewforemailmonitoringallowed`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_ispreviewforemailmonitoringallowed`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsPriceListMandatory"></a> IsPriceListMandatory

|Property|Value|
|---|---|
|Description|**Indicates whether PriceList is mandatory for adding existing products to sales entities.**|
|DisplayName|**Indicates whether PriceList is mandatory for adding existing products to sales entities**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ispricelistmandatory`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsProcessCapacityAutoClaimEnabled"></a> IsProcessCapacityAutoClaimEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether the Process capacity auto-claim feature is enabled in this organization.**|
|DisplayName|**Enable the Process capacity auto-claim feature for this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isprocesscapacityautoclaimenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsQuickCreateEnabledForOpportunityClose"></a> IsQuickCreateEnabledForOpportunityClose

|Property|Value|
|---|---|
|Description|**Select whether to use the standard Out-of-box Opportunity Close experience or opt to for a customized experience.**|
|DisplayName|**Enable quick create form for opportunity close feature for this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isquickcreateenabledforopportunityclose`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsReadAuditEnabled"></a> IsReadAuditEnabled

|Property|Value|
|---|---|
|Description|**Enable or disable auditing of read operations.**|
|DisplayName|**Is Read Auditing Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isreadauditenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isreadauditenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsRelationshipInsightsEnabled"></a> IsRelationshipInsightsEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether the feature Relationship Insights should be enabled for the organization.**|
|DisplayName|**Enable Relationship Insights for this Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isrelationshipinsightsenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsResourceBookingExchangeSyncEnabled"></a> IsResourceBookingExchangeSyncEnabled

|Property|Value|
|---|---|
|Description|**Indicates if the synchronization of user resource booking with Exchange is enabled at organization level.**|
|DisplayName|**Resource booking synchronization enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isresourcebookingexchangesyncenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsRichTextNotesEnabled"></a> IsRichTextNotesEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether rich text editor for notes experience is enabled on this organization**|
|DisplayName|**Indicates whether rich text editor for notes experience is enabled on this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isrichtextnotesenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsRpaAutoscaleAadJoinEnabled"></a> IsRpaAutoscaleAadJoinEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether AAD Join for RPA Autoscale is enabled in this organization..**|
|DisplayName|**Enable AAD Join for RPA Autoscale feature for this organization.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isrpaautoscaleaadjoinenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsRpaAutoscaleEnabled"></a> IsRpaAutoscaleEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether Autoscale feature for RPA is enabled in this organization.**|
|DisplayName|**Enable RPA Autoscale feature for this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isrpaautoscaleenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsRpaBoxCrossGeoEnabled"></a> IsRpaBoxCrossGeoEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether RPA Box feature is enabled in this organization in locations outside the tenant's geographical location.**|
|DisplayName|**Enable RPA Box cross geo feature for this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isrpaboxcrossgeoenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsRpaBoxEnabled"></a> IsRpaBoxEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether RPA Box feature is enabled in this organization.**|
|DisplayName|**Enable RPA Box feature for this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isrpaboxenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsRpaUnattendedEnabled"></a> IsRpaUnattendedEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether Unattended runs feature for RPA is enabled in this organization.**|
|DisplayName|**Enable RPA Unattended feature for this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isrpaunattendedenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsSalesAssistantEnabled"></a> IsSalesAssistantEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether Sales Assistant mobile app has been enabled for the organization.**|
|DisplayName|**Enable Sales Assistant mobile app**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`issalesassistantenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsSharingInOrgAllowed"></a> IsSharingInOrgAllowed

|Property|Value|
|---|---|
|Description||
|DisplayName|**IsSharingInOrgAllowed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`issharinginorgallowed`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_issharinginorgallowed`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsSOPIntegrationEnabled"></a> IsSOPIntegrationEnabled

|Property|Value|
|---|---|
|Description|**Enable sales order processing integration.**|
|DisplayName|**Is Sales Order Integration Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`issopintegrationenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_issopintegrationenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsTextWrapEnabled"></a> IsTextWrapEnabled

|Property|Value|
|---|---|
|Description|**Information on whether text wrap is enabled.**|
|DisplayName|**Enable Text Wrap**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`istextwrapenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_istextwrapenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsUserAccessAuditEnabled"></a> IsUserAccessAuditEnabled

|Property|Value|
|---|---|
|Description|**Enable or disable auditing of user access.**|
|DisplayName|**Is User Access Auditing Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isuseraccessauditenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_isuseraccessauditenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ISVIntegrationCode"></a> ISVIntegrationCode

|Property|Value|
|---|---|
|Description|**Indicates whether loading of Microsoft Dynamics 365 in a browser window that does not have address, tool, and menu bars is enabled.**|
|DisplayName|**ISV Integration Mode**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isvintegrationcode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`organization_isvintegrationcode`|

#### ISVIntegrationCode Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Web**|
|2|**Outlook Workstation Client**|
|3|**Web; Outlook Workstation Client**|
|4|**Outlook Laptop Client**|
|5|**Web; Outlook Laptop Client**|
|6|**Outlook**|
|7|**All**|

### <a name="BKMK_IsWorkQueueSavingsEnabled"></a> IsWorkQueueSavingsEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether Power Automate savings feature is enabled for WorkQueue.**|
|DisplayName|**Enable Power Automate savings feature for WorkQueue**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isworkqueuesavingsenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsWriteInProductsAllowed"></a> IsWriteInProductsAllowed

|Property|Value|
|---|---|
|Description|**Indicates whether Write-in Products can be added to Opportunity/Quote/Order/Invoice or not.**|
|DisplayName|**Indicates whether Write-in Products can be added to Opportunity/Quote/Order/Invoice or not**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iswriteinproductsallowed`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_KaPrefix"></a> KaPrefix

|Property|Value|
|---|---|
|Description|**Type the prefix to use for all knowledge articles in Microsoft Dynamics 365.**|
|DisplayName|**Knowledge Article Prefix**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`kaprefix`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_KbPrefix"></a> KbPrefix

|Property|Value|
|---|---|
|Description|**Prefix to use for all articles in Microsoft Dynamics 365.**|
|DisplayName|**Article Prefix**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`kbprefix`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_KMSettings"></a> KMSettings

|Property|Value|
|---|---|
|Description|**XML string containing the Knowledge Management settings that are applied in Knowledge Management Wizard.**|
|DisplayName|**Knowledge Management Settings**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`kmsettings`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_LanguageCode"></a> LanguageCode

|Property|Value|
|---|---|
|Description|**Preferred language for the organization.**|
|DisplayName|**Language**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`languagecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_LegacyAppToggle"></a> LegacyAppToggle

|Property|Value|
|---|---|
|Description|**Show legacy app for admins**|
|DisplayName|**Show legacy app for admins**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`legacyapptoggle`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`organization_legacyapptoggle`|

#### LegacyAppToggle Choices/Options

|Value|Label|
|---|---|
|0|**Auto**|
|1|**On**|
|2|**Off**|

### <a name="BKMK_LocaleId"></a> LocaleId

|Property|Value|
|---|---|
|Description|**Unique identifier of the locale of the organization.**|
|DisplayName|**Locale**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`localeid`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_LongDateFormatCode"></a> LongDateFormatCode

|Property|Value|
|---|---|
|Description|**Information that specifies how the Long Date format is displayed in Microsoft Dynamics 365.**|
|DisplayName|**Long Date Format**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`longdateformatcode`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_LookupCharacterCountBeforeResolve"></a> LookupCharacterCountBeforeResolve

|Property|Value|
|---|---|
|Description|**Minimum number of characters that should be entered in the lookup control before resolving for suggestions**|
|DisplayName|**Minimum number of characters before resolving suggestions in lookup**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lookupcharactercountbeforeresolve`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_LookupResolveDelayMS"></a> LookupResolveDelayMS

|Property|Value|
|---|---|
|Description|**Minimum delay (in milliseconds) between consecutive inputs in a lookup control that will trigger a search for suggestions**|
|DisplayName|**Minimum delay (in milliseconds) for debouncing lookup control input**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lookupresolvedelayms`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|250|

### <a name="BKMK_MailboxIntermittentIssueMinRange"></a> MailboxIntermittentIssueMinRange

|Property|Value|
|---|---|
|Description|**Lower Threshold For Mailbox Intermittent Issue.**|
|DisplayName|**Lower Threshold For Mailbox Intermittent Issue**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mailboxintermittentissueminrange`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_MailboxPermanentIssueMinRange"></a> MailboxPermanentIssueMinRange

|Property|Value|
|---|---|
|Description|**Lower Threshold For Mailbox Permanent Issue.**|
|DisplayName|**Lower Threshold For Mailbox Permanent Issue.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mailboxpermanentissueminrange`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_MaxActionStepsInBPF"></a> MaxActionStepsInBPF

|Property|Value|
|---|---|
|Description|**Maximum number of actionsteps allowed in a BPF**|
|DisplayName|**Maximum number of actionsteps allowed in a BPF**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maxactionstepsinbpf`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|100|
|MinValue|0|

### <a name="BKMK_MaxAllowedPendingRollupJobCount"></a> MaxAllowedPendingRollupJobCount

|Property|Value|
|---|---|
|Description|**Maximum Allowed Pending Rollup Job Count**|
|DisplayName|**MaxAllowedPendingRollupJobCount**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maxallowedpendingrollupjobcount`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_MaxAllowedPendingRollupJobPercentage"></a> MaxAllowedPendingRollupJobPercentage

|Property|Value|
|---|---|
|Description|**Percentage Of Entity Table Size For Kicking Off Bootstrap Job**|
|DisplayName|**MaxAllowedPendingRollupJobPercentage**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maxallowedpendingrollupjobpercentage`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|100|
|MinValue|0|

### <a name="BKMK_MaxAppointmentDurationDays"></a> MaxAppointmentDurationDays

|Property|Value|
|---|---|
|Description|**Maximum number of days an appointment can last.**|
|DisplayName|**Max Appointment Duration**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maxappointmentdurationdays`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_MaxConditionsForMobileOfflineFilters"></a> MaxConditionsForMobileOfflineFilters

|Property|Value|
|---|---|
|Description|**Maximum number of conditions allowed for mobile offline filters**|
|DisplayName|**Maximum number of conditions allowed for mobile offline filters**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maxconditionsformobileofflinefilters`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_MaxDepthForHierarchicalSecurityModel"></a> MaxDepthForHierarchicalSecurityModel

|Property|Value|
|---|---|
|Description|**Maximum depth for hierarchy security propagation.**|
|DisplayName|**Maximum depth for hierarchy security propagation.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maxdepthforhierarchicalsecuritymodel`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_MaxFolderBasedTrackingMappings"></a> MaxFolderBasedTrackingMappings

|Property|Value|
|---|---|
|Description|**Maximum number of Folder Based Tracking mappings user can add**|
|DisplayName|**Max Folder Based Tracking Mappings**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maxfolderbasedtrackingmappings`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|25|
|MinValue|1|

### <a name="BKMK_MaximumActiveBusinessProcessFlowsAllowedPerEntity"></a> MaximumActiveBusinessProcessFlowsAllowedPerEntity

|Property|Value|
|---|---|
|Description|**Maximum number of active business process flows allowed per entity**|
|DisplayName|**Maximum active business process flows per entity**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maximumactivebusinessprocessflowsallowedperentity`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|1|

### <a name="BKMK_MaximumDynamicPropertiesAllowed"></a> MaximumDynamicPropertiesAllowed

|Property|Value|
|---|---|
|Description|**Restrict the maximum number of product properties for a product family/bundle**|
|DisplayName|**Product Properties Item Limit**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maximumdynamicpropertiesallowed`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_MaximumEntitiesWithActiveSLA"></a> MaximumEntitiesWithActiveSLA

|Property|Value|
|---|---|
|Description|**Maximum number of active SLA allowed per entity in online**|
|DisplayName|**Maximum number of active SLA allowed per entity in online**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maximumentitieswithactivesla`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_MaximumSLAKPIPerEntityWithActiveSLA"></a> MaximumSLAKPIPerEntityWithActiveSLA

|Property|Value|
|---|---|
|Description|**Maximum number of SLA KPI per active SLA allowed for entity in online**|
|DisplayName|**Maximum number of active SLA KPI allowed per entity in online**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maximumslakpiperentitywithactivesla`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_MaximumTrackingNumber"></a> MaximumTrackingNumber

|Property|Value|
|---|---|
|Description|**Maximum tracking number before recycling takes place.**|
|DisplayName|**Max Tracking Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maximumtrackingnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_MaxProductsInBundle"></a> MaxProductsInBundle

|Property|Value|
|---|---|
|Description|**Restrict the maximum no of items in a bundle**|
|DisplayName|**Bundle Item Limit**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maxproductsinbundle`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_MaxRecordsForExportToExcel"></a> MaxRecordsForExportToExcel

|Property|Value|
|---|---|
|Description|**Maximum number of records that will be exported to a static Microsoft Office Excel worksheet when exporting from the grid.**|
|DisplayName|**Max Records For Excel Export**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maxrecordsforexporttoexcel`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_MaxRecordsForLookupFilters"></a> MaxRecordsForLookupFilters

|Property|Value|
|---|---|
|Description|**Maximum number of lookup and picklist records that can be selected by user for filtering.**|
|DisplayName|**Max Records Filter Selection**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maxrecordsforlookupfilters`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_MaxRollupFieldsPerEntity"></a> MaxRollupFieldsPerEntity

|Property|Value|
|---|---|
|Description|**Maximum Rollup Fields Per Entity**|
|DisplayName|**MaxRollupFieldsPerEntity**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maxrollupfieldsperentity`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|50|
|MinValue|0|

### <a name="BKMK_MaxRollupFieldsPerOrg"></a> MaxRollupFieldsPerOrg

|Property|Value|
|---|---|
|Description|**Maximum Rollup Fields Per Organization**|
|DisplayName|**MaxRollupFieldsPerOrg**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maxrollupfieldsperorg`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|500|
|MinValue|0|

### <a name="BKMK_MaxSLAItemsPerSLA"></a> MaxSLAItemsPerSLA

|Property|Value|
|---|---|
|Description||
|DisplayName|**Max SLA Items Per SLA**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`maxslaitemspersla`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_MaxUploadFileSize"></a> MaxUploadFileSize

|Property|Value|
|---|---|
|Description|**Maximum allowed size of an attachment.**|
|DisplayName|**Max Upload File Size**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maxuploadfilesize`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_MicrosoftFlowEnvironment"></a> MicrosoftFlowEnvironment

|Property|Value|
|---|---|
|Description|**(Deprecated) Environment selected for Integration with Microsoft Flow**|
|DisplayName|**(Deprecated) Environment selected for Integration with Microsoft Flow**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`microsoftflowenvironment`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_MinAddressBookSyncInterval"></a> MinAddressBookSyncInterval

|Property|Value|
|---|---|
|Description|**Normal polling frequency used for address book synchronization in Microsoft Office Outlook.**|
|DisplayName|**Min Address Synchronization Frequency**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`minaddressbooksyncinterval`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_MinOfflineSyncInterval"></a> MinOfflineSyncInterval

|Property|Value|
|---|---|
|Description|**Normal polling frequency used for background offline synchronization in Microsoft Office Outlook.**|
|DisplayName|**Min Offline Synchronization Frequency**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`minofflinesyncinterval`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_MinOutlookSyncInterval"></a> MinOutlookSyncInterval

|Property|Value|
|---|---|
|Description|**Minimum allowed time between scheduled Outlook synchronizations.**|
|DisplayName|**Min Synchronization Frequency**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`minoutlooksyncinterval`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_MobileOfflineSyncInterval"></a> MobileOfflineSyncInterval

|Property|Value|
|---|---|
|Description|**Sync interval for mobile offline.**|
|DisplayName|**Sync interval for mobile offline.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mobileofflinesyncinterval`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ModernAdvancedFindFiltering"></a> ModernAdvancedFindFiltering

|Property|Value|
|---|---|
|Description|**Flag to indicate if the modern advanced find filtering on all tables in a model-driven app is enabled**|
|DisplayName|**Modern advanced find filtering**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modernadvancedfindfiltering`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ModernAppDesignerCoauthoringEnabled"></a> ModernAppDesignerCoauthoringEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether coauthoring is enabled in modern app designer**|
|DisplayName|**Coauthoring in Modern App Designer Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modernappdesignercoauthoringenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_MultiColumnSortEnabled"></a> MultiColumnSortEnabled

|Property|Value|
|---|---|
|Description|**Show the sort by button on views**|
|DisplayName|**Enable Multi Column Sort Editor In Views**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`multicolumnsortenabled`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|100|
|MinValue|0|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the organization. The name is set when Microsoft CRM is installed and should not be changed.**|
|DisplayName|**Organization Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_NaturalLanguageAssistFilter"></a> NaturalLanguageAssistFilter

|Property|Value|
|---|---|
|Description|**Enables Natural Language Assist Filter.**|
|DisplayName|**Natural Language Assist**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`naturallanguageassistfilter`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_NegativeCurrencyFormatCode"></a> NegativeCurrencyFormatCode

|Property|Value|
|---|---|
|Description|**Information that specifies how negative currency numbers are displayed throughout Microsoft Dynamics 365.**|
|DisplayName|**Negative Currency Format**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`negativecurrencyformatcode`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_NegativeFormatCode"></a> NegativeFormatCode

|Property|Value|
|---|---|
|Description|**Information that specifies how negative numbers are displayed throughout Microsoft CRM.**|
|DisplayName|**Negative Format**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`negativeformatcode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`organization_negativeformatcode`|

#### NegativeFormatCode Choices/Options

|Value|Label|
|---|---|
|0|**Brackets**|
|1|**Dash**|
|2|**Dash plus Space**|
|3|**Trailing Dash**|
|4|**Space plus Trailing Dash**|

### <a name="BKMK_NewSearchExperienceEnabled"></a> NewSearchExperienceEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether an organization has enabled the new Relevance search experience (released in Oct 2020) for the organization**|
|DisplayName|**Oct 2020 Search enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`newsearchexperienceenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_NextTrackingNumber"></a> NextTrackingNumber

|Property|Value|
|---|---|
|Description|**Next token to be placed on the subject line of an email message.**|
|DisplayName|**Next Tracking Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`nexttrackingnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_NotifyMailboxOwnerOfEmailServerLevelAlerts"></a> NotifyMailboxOwnerOfEmailServerLevelAlerts

|Property|Value|
|---|---|
|Description|**Indicates whether mailbox owners will be notified of email server profile level alerts.**|
|DisplayName|**Notify Mailbox Owner Of Email Server Level Alerts**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`notifymailboxownerofemailserverlevelalerts`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_notifymailboxownerofemailserverlevelalerts`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_NumberFormat"></a> NumberFormat

|Property|Value|
|---|---|
|Description|**Specification of how numbers are displayed throughout Microsoft CRM.**|
|DisplayName|**Number Format**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`numberformat`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2|

### <a name="BKMK_NumberGroupFormat"></a> NumberGroupFormat

|Property|Value|
|---|---|
|Description|**Specifies how numbers are grouped in Microsoft Dynamics 365.**|
|DisplayName|**Number Grouping Format**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`numbergroupformat`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_NumberSeparator"></a> NumberSeparator

|Property|Value|
|---|---|
|Description|**Symbol used for number separation in Microsoft Dynamics 365.**|
|DisplayName|**Number Separator**|
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

### <a name="BKMK_OfficeAppsAutoDeploymentEnabled"></a> OfficeAppsAutoDeploymentEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether the Office Apps auto deployment is enabled for the organization.**|
|DisplayName|**Enable Office Apps Auto Deployment for this Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`officeappsautodeploymentenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_officeappsautodeploymentenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_OfficeGraphDelveUrl"></a> OfficeGraphDelveUrl

|Property|Value|
|---|---|
|Description|**The url to open the Delve for the organization.**|
|DisplayName|**The url to open the Delve**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`officegraphdelveurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_OOBPriceCalculationEnabled"></a> OOBPriceCalculationEnabled

|Property|Value|
|---|---|
|Description|**Enable OOB pricing calculation logic for Opportunity, Quote, Order and Invoice entities.**|
|DisplayName|**Enable OOB Price calculation**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`oobpricecalculationenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_oobpricecalculationenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_OptOutSchemaV2EnabledByDefault"></a> OptOutSchemaV2EnabledByDefault

|Property|Value|
|---|---|
|Description|**Indicates if this organization will opt-out from automatically enabling schema v2 on the organization.**|
|DisplayName|**Opt-out of schema v2 being automatically enabled for this organization.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`optoutschemav2enabledbydefault`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_OrderPrefix"></a> OrderPrefix

|Property|Value|
|---|---|
|Description|**Prefix to use for all orders throughout Microsoft Dynamics 365.**|
|DisplayName|**Order Prefix**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`orderprefix`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_OrgDbOrgSettings"></a> OrgDbOrgSettings

|Property|Value|
|---|---|
|Description|**Organization settings stored in Organization Database.**|
|DisplayName|**Organization Database Organization Settings**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`orgdborgsettings`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_OrgInsightsEnabled"></a> OrgInsightsEnabled

|Property|Value|
|---|---|
|Description|**Select whether to turn on OrgInsights for the organization.**|
|DisplayName|**Enable OrgInsights for this Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`orginsightsenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_PaiPreviewScenarioEnabled"></a> PaiPreviewScenarioEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether Preview feature has been enabled for the organization.**|
|DisplayName|**Display Preview Feature for this organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`paipreviewscenarioenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_PastExpansionWindow"></a> PastExpansionWindow

|Property|Value|
|---|---|
|Description|**Specifies the maximum number of months in past for which the recurring activities can be created.**|
|DisplayName|**Past Expansion Window**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`pastexpansionwindow`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|120|
|MinValue|1|

### <a name="BKMK_PcfDatasetGridEnabled"></a> PcfDatasetGridEnabled

|Property|Value|
|---|---|
|Description|**Leave empty to use default setting. Set to on/off to enable/disable replacement of default grids with modern ones in model-driven apps.**|
|DisplayName|**Enable modern grids in model-driven apps**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`pcfdatasetgridenabled`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|16|

### <a name="BKMK_PerformACTSyncAfter"></a> PerformACTSyncAfter

|Property|Value|
|---|---|
|Description|**This setting contains the date time before an ACT sync can execute.**|
|DisplayName|**PerformACTSyncAfter**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`performactsyncafter`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_Picture"></a> Picture

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Picture**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`picture`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_PinpointLanguageCode"></a> PinpointLanguageCode

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`pinpointlanguagecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_PluginTraceLogSetting"></a> PluginTraceLogSetting

|Property|Value|
|---|---|
|Description|**Plug-in Trace Log Setting for the Organization.**|
|DisplayName|**Plug-in Trace Log Setting**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`plugintracelogsetting`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`organization_plugintracelogsetting`|

#### PluginTraceLogSetting Choices/Options

|Value|Label|
|---|---|
|0|**Off**|
|1|**Exception**|
|2|**All**|

### <a name="BKMK_PMDesignator"></a> PMDesignator

|Property|Value|
|---|---|
|Description|**PM designator to use throughout Microsoft Dynamics 365.**|
|DisplayName|**PM Designator**|
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

### <a name="BKMK_PostMessageWhitelistDomains"></a> PostMessageWhitelistDomains

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**For internal use only.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`postmessagewhitelistdomains`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_PowerAppsMakerBotEnabled"></a> PowerAppsMakerBotEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether bot for makers is enabled.**|
|DisplayName|**Enable bot for makers.**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`powerappsmakerbotenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_PowerBIAllowCrossRegionOperations"></a> PowerBIAllowCrossRegionOperations

|Property|Value|
|---|---|
|Description|**Indicates whether cross region operations are allowed for the organization**|
|DisplayName|**Power BI allow cross region operations**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`powerbiallowcrossregionoperations`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_PowerBIAutomaticPermissionsAssignment"></a> PowerBIAutomaticPermissionsAssignment

|Property|Value|
|---|---|
|Description|**Indicates whether automatic permissions assignment to Power BI has been enabled for the organization**|
|DisplayName|**Power BI automatic permissions assignment**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`powerbiautomaticpermissionsassignment`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_PowerBIComponentsCreate"></a> PowerBIComponentsCreate

|Property|Value|
|---|---|
|Description|**Indicates whether creation of Power BI components has been enabled for the organization**|
|DisplayName|**Power BI components creation**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`powerbicomponentscreate`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_PowerBiFeatureEnabled"></a> PowerBiFeatureEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether the Power BI feature should be enabled for the organization.**|
|DisplayName|**Enable Power BI feature for this Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`powerbifeatureenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_powerbifeature`|
|DefaultValue|False|
|True Label|Enable|
|False Label|Disable|

### <a name="BKMK_PricingDecimalPrecision"></a> PricingDecimalPrecision

|Property|Value|
|---|---|
|Description|**Number of decimal places that can be used for prices.**|
|DisplayName|**Pricing Decimal Precision**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`pricingdecimalprecision`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|10|
|MinValue|0|

### <a name="BKMK_PrivacyStatementUrl"></a> PrivacyStatementUrl

|Property|Value|
|---|---|
|Description|**Privacy Statement URL**|
|DisplayName|**Privacy Statement URL**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`privacystatementurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_PrivilegeUserGroupId"></a> PrivilegeUserGroupId

|Property|Value|
|---|---|
|Description|**Unique identifier of the default privilege for users in the organization.**|
|DisplayName|**Privilege User Group**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`privilegeusergroupid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_PrivReportingGroupId"></a> PrivReportingGroupId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Privilege Reporting Group**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`privreportinggroupid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_PrivReportingGroupName"></a> PrivReportingGroupName

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Privilege Reporting Group Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`privreportinggroupname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_ProductRecommendationsEnabled"></a> ProductRecommendationsEnabled

|Property|Value|
|---|---|
|Description|**Select whether to turn on product recommendations for the organization.**|
|DisplayName|**Enable Product Recommendations for this Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`productrecommendationsenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_QualifyLeadAdditionalOptions"></a> QualifyLeadAdditionalOptions

|Property|Value|
|---|---|
|Description|**Indicates whether prompt should be shown for new Qualify Lead Experience**|
|DisplayName|**Enable New Qualify Lead Experience with configuration MDD**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`qualifyleadadditionaloptions`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_QuickActionToOpenRecordsInSidePaneEnabled"></a> QuickActionToOpenRecordsInSidePaneEnabled

|Property|Value|
|---|---|
|Description|**Flag to indicate if the feature to use quick action to open records in search side pane is enabled**|
|DisplayName|**Enable quick actions to open records in search side pane**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`quickactiontoopenrecordsinsidepaneenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_QuickFindRecordLimitEnabled"></a> QuickFindRecordLimitEnabled

|Property|Value|
|---|---|
|Description|**Indicates whether a quick find record limit should be enabled for this organization (allows for faster Quick Find queries but prevents overly broad searches).**|
|DisplayName|**Quick Find Record Limit Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`quickfindrecordlimitenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_enablequickfindrecordlimit`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_QuotePrefix"></a> QuotePrefix

|Property|Value|
|---|---|
|Description|**Prefix to use for all quotes throughout Microsoft Dynamics 365.**|
|DisplayName|**Quote Prefix**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`quoteprefix`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_RecalculateSLA"></a> RecalculateSLA

|Property|Value|
|---|---|
|Description|**Indicates whether SLA Recalculation has been enabled for the organization**|
|DisplayName|**Indicates whether SLA Recalculation has been enabled for the organization**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`recalculatesla`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_RecurrenceDefaultNumberOfOccurrences"></a> RecurrenceDefaultNumberOfOccurrences

|Property|Value|
|---|---|
|Description|**Specifies the default value for number of occurrences field in the recurrence dialog.**|
|DisplayName|**Recurrence Default Number of Occurrences**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`recurrencedefaultnumberofoccurrences`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|999|
|MinValue|1|

### <a name="BKMK_RecurrenceExpansionJobBatchInterval"></a> RecurrenceExpansionJobBatchInterval

|Property|Value|
|---|---|
|Description|**Specifies the interval (in seconds) for pausing expansion job.**|
|DisplayName|**Recurrence Expansion Job Batch Interval**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`recurrenceexpansionjobbatchinterval`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_RecurrenceExpansionJobBatchSize"></a> RecurrenceExpansionJobBatchSize

|Property|Value|
|---|---|
|Description|**Specifies the value for number of instances created in on demand job in one shot.**|
|DisplayName|**Recurrence Expansion On Demand Job Batch Size**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`recurrenceexpansionjobbatchsize`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_RecurrenceExpansionSynchCreateMax"></a> RecurrenceExpansionSynchCreateMax

|Property|Value|
|---|---|
|Description|**Specifies the maximum number of instances to be created synchronously after creating a recurring appointment.**|
|DisplayName|**Recurrence Expansion Synchronization Create Maximum**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`recurrenceexpansionsynchcreatemax`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|1000|
|MinValue|1|

### <a name="BKMK_ReferenceSiteMapXml"></a> ReferenceSiteMapXml

|Property|Value|
|---|---|
|Description|**XML string that defines the navigation structure for the application. This is the site map from the previously upgraded build and is used in a 3-way merge during upgrade.**|
|DisplayName|**Reference SiteMap XML**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`referencesitemapxml`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_ReleaseCadence"></a> ReleaseCadence

|Property|Value|
|---|---|
|Description|**Current orgnization release cadence value**|
|DisplayName|**Current orgnization release cadence value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`releasecadence`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|100|
|MinValue|0|

### <a name="BKMK_ReleaseChannel"></a> ReleaseChannel

|Property|Value|
|---|---|
|Description|**Model app refresh channel**|
|DisplayName|**Model app refresh channel**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`releasechannel`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`organization_releasechannel`|

#### ReleaseChannel Choices/Options

|Value|Label|
|---|---|
|0|**Auto**|
|1|**Monthly channel**|
|2|**Microsoft Inner channel**|
|3|**Semi-annual channel**|

### <a name="BKMK_ReleaseWaveName"></a> ReleaseWaveName

|Property|Value|
|---|---|
|Description|**Release Wave Applied to Environment.**|
|DisplayName|**Release Wave**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`releasewavename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_RelevanceSearchEnabledByPlatform"></a> RelevanceSearchEnabledByPlatform

|Property|Value|
|---|---|
|Description|**Indicates whether relevance search was enabled for the environment as part of Dataverse's relevance search on-by-default sweep**|
|DisplayName|**Relevance search enabled automatically by Dataverse**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`relevancesearchenabledbyplatform`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_RelevanceSearchModifiedOn"></a> RelevanceSearchModifiedOn

|Property|Value|
|---|---|
|Description|**This setting contains the last modified date for relevance search setting that appears as a toggle in PPAC.**|
|DisplayName|**RelevanceSearchModifiedOnDate**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`relevancesearchmodifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_RenderSecureIFrameForEmail"></a> RenderSecureIFrameForEmail

|Property|Value|
|---|---|
|Description|**Flag to render the body of email in the Web form in an IFRAME with the security='restricted' attribute set. This is additional security but can cause a credentials prompt.**|
|DisplayName|**Render Secure Frame For Email**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`rendersecureiframeforemail`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_rendersecureiframeforemail`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ReportingGroupId"></a> ReportingGroupId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Reporting Group**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`reportinggroupid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ReportingGroupName"></a> ReportingGroupName

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Reporting Group Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`reportinggroupname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_ReportScriptErrors"></a> ReportScriptErrors

|Property|Value|
|---|---|
|Description|**Picklist for selecting the organization preference for reporting scripting errors.**|
|DisplayName|**Report Script Errors**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`reportscripterrors`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`organization_reportscripterrors`|

#### ReportScriptErrors Choices/Options

|Value|Label|
|---|---|
|0|**No preference for sending an error report to Microsoft about Microsoft Dynamics 365**|
|1|**Ask me for permission to send an error report to Microsoft**|
|2|**Automatically send an error report to Microsoft without asking me for permission**|
|3|**Never send an error report to Microsoft about Microsoft Dynamics 365**|

### <a name="BKMK_RequireApprovalForQueueEmail"></a> RequireApprovalForQueueEmail

|Property|Value|
|---|---|
|Description|**Indicates whether Send As Other User privilege is enabled.**|
|DisplayName|**Is Approval For Queue Email Required**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`requireapprovalforqueueemail`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_requireapprovalforqueueemail`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_RequireApprovalForUserEmail"></a> RequireApprovalForUserEmail

|Property|Value|
|---|---|
|Description|**Indicates whether Send As Other User privilege is enabled.**|
|DisplayName|**Is Approval For User Email Required**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`requireapprovalforuseremail`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_requireapprovalforuseremail`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ResolveSimilarUnresolvedEmailAddress"></a> ResolveSimilarUnresolvedEmailAddress

|Property|Value|
|---|---|
|Description|**Apply same email address to all unresolved matches when you manually resolve it for one**|
|DisplayName|**Apply same email address to all unresolved matches when you manually resolve it for one**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`resolvesimilarunresolvedemailaddress`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_resolvesimilarunresolvedemailaddress`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_RestrictGuestUserAccess"></a> RestrictGuestUserAccess

|Property|Value|
|---|---|
|Description|**Information that specifies whether guest user restriction is enabled**|
|DisplayName|**Restrict guest users access to the organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`restrictGuestUserAccess`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_RestrictStatusUpdate"></a> RestrictStatusUpdate

|Property|Value|
|---|---|
|Description|**Flag to restrict Update on incident.**|
|DisplayName|**Restrict Status Update**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`restrictstatusupdate`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organization_restrictstatusupdate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ReverseProxyIpAddresses"></a> ReverseProxyIpAddresses

|Property|Value|
|---|---|
|Description|**Information that specifies Reverse Proxy IP addresses from which requests have to be allowed.**|
|DisplayName|**List of reverse proxy IP addresses to be allowed.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`reverseproxyipaddresses`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_RiErrorStatus"></a> RiErrorStatus

|Property|Value|
|---|---|
|Description|**Error status of Relationship Insights provisioning.**|
|DisplayName|**Error status of Relationship Insights provisioning.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`rierrorstatus`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_SameSiteModeForSessionCookie"></a> SameSiteModeForSessionCookie

|Property|Value|
|---|---|
|Description|**Samesite mode for Session Cookie 0 is Default, 1 is None, 2 is Lax , 3 is Strict**|
|DisplayName|**Samesite mode for Session Cookie**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`samesitemodeforsessioncookie`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`organization_samesitemodeforsessioncookie`|

#### SameSiteModeForSessionCookie Choices/Options

|Value|Label|
|---|---|
|0|**Default**|
|1|**None**|
|2|**Lax**|
|3|**Strict**|

### <a name="BKMK_SampleDataImportId"></a> SampleDataImportId

|Property|Value|
|---|---|
|Description|**Unique identifier of the sample data import job.**|
|DisplayName|**Sample Data Import**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sampledataimportid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_SavingEventsTTLInMinutes"></a> SavingEventsTTLInMinutes

|Property|Value|
|---|---|
|Description|**Default time to live in minutes for new Power Automate savings events records in flow aggregation.**|
|DisplayName|**The TTL in minutes for new Power Automate savings events records in flow aggregation.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`savingeventsttlinminutes`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|52560000|
|MinValue|0|

### <a name="BKMK_SchemaNamePrefix"></a> SchemaNamePrefix

|Property|Value|
|---|---|
|Description|**Prefix used for custom entities and attributes.**|
|DisplayName|**Customization Name Prefix**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`schemanameprefix`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|8|

### <a name="BKMK_SendBulkEmailInUCI"></a> SendBulkEmailInUCI

|Property|Value|
|---|---|
|Description|**Indicates whether Send Bulk Email in UCI is enabled for the org.**|
|DisplayName|**Send Bulk Email in UCI**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sendbulkemailinuci`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ServeStaticResourcesFromAzureCDN"></a> ServeStaticResourcesFromAzureCDN

|Property|Value|
|---|---|
|Description|**Serve Static Content From CDN**|
|DisplayName|**Serve Static Content From CDN**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`servestaticresourcesfromazurecdn`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_SessionRecordingEnabled"></a> SessionRecordingEnabled

|Property|Value|
|---|---|
|Description|**Enable the session recording feature to record user sessions in UCI**|
|DisplayName|**Enable the session recording feature**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sessionrecordingenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_SessionTimeoutEnabled"></a> SessionTimeoutEnabled

|Property|Value|
|---|---|
|Description|**Information that specifies whether session timeout is enabled**|
|DisplayName|**Session timeout enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sessiontimeoutenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_SessionTimeoutInMins"></a> SessionTimeoutInMins

|Property|Value|
|---|---|
|Description|**Session timeout in minutes**|
|DisplayName|**Session timeout in minutes**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sessiontimeoutinmins`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_SessionTimeoutReminderInMins"></a> SessionTimeoutReminderInMins

|Property|Value|
|---|---|
|Description|**Session timeout reminder in minutes**|
|DisplayName|**Session timeout reminder in minutes**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sessiontimeoutreminderinmins`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_SharePointDeploymentType"></a> SharePointDeploymentType

|Property|Value|
|---|---|
|Description|**Indicates which SharePoint deployment type is configured for Server to Server. (Online or On-Premises)**|
|DisplayName|**Choose SharePoint Deployment Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sharepointdeploymenttype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`organization_sharepointdeploymenttype`|

#### SharePointDeploymentType Choices/Options

|Value|Label|
|---|---|
|0|**Online**|
|1|**On-Premises**|

### <a name="BKMK_ShareToPreviousOwnerOnAssign"></a> ShareToPreviousOwnerOnAssign

|Property|Value|
|---|---|
|Description|**Information that specifies whether to share to previous owner on assign.**|
|DisplayName|**Share To Previous Owner On Assign**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sharetopreviousowneronassign`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_sharetopreviousowneronassign`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ShowKBArticleDeprecationNotification"></a> ShowKBArticleDeprecationNotification

|Property|Value|
|---|---|
|Description|**Select whether to display a KB article deprecation notification to the user.**|
|DisplayName|**Show KBArticle deprecation message to user**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`showkbarticledeprecationnotification`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_showkbarticledeprecationnotification`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ShowWeekNumber"></a> ShowWeekNumber

|Property|Value|
|---|---|
|Description|**Information that specifies whether to display the week number in calendar displays throughout Microsoft CRM.**|
|DisplayName|**Show Week Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`showweeknumber`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organization_showweeknumber`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_SignupOutlookDownloadFWLink"></a> SignupOutlookDownloadFWLink

|Property|Value|
|---|---|
|Description|**CRM for Outlook Download URL**|
|DisplayName|**CRMForOutlookDownloadURL**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`signupoutlookdownloadfwlink`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_SiteMapXml"></a> SiteMapXml

|Property|Value|
|---|---|
|Description|**XML string that defines the navigation structure for the application.**|
|DisplayName|**SiteMap XML**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sitemapxml`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_SlaPauseStates"></a> SlaPauseStates

|Property|Value|
|---|---|
|Description|**Contains the on hold case status values.**|
|DisplayName|**SLA pause states**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`slapausestates`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_SocialInsightsEnabled"></a> SocialInsightsEnabled

|Property|Value|
|---|---|
|Description|**Flag for whether the organization is using Social Insights.**|
|DisplayName|**Social Insights Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`socialinsightsenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`socialinsightsconfiguration_enabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_SocialInsightsInstance"></a> SocialInsightsInstance

|Property|Value|
|---|---|
|Description|**Identifier for the Social Insights instance for the organization.**|
|DisplayName|**Social Insights instance identifier**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`socialinsightsinstance`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2048|

### <a name="BKMK_SocialInsightsTermsAccepted"></a> SocialInsightsTermsAccepted

|Property|Value|
|---|---|
|Description|**Flag for whether the organization has accepted the Social Insights terms of use.**|
|DisplayName|**Social Insights Terms of Use**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`socialinsightstermsaccepted`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`socialinsightsconfiguration_termsaccepted`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_SortId"></a> SortId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Sort**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sortid`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_SqlAccessGroupId"></a> SqlAccessGroupId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**SQL Access Group**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sqlaccessgroupid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_SqlAccessGroupName"></a> SqlAccessGroupName

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**SQL Access Group Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sqlaccessgroupname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_SQMEnabled"></a> SQMEnabled

|Property|Value|
|---|---|
|Description|**Setting for SQM data collection, 0 no, 1 yes enabled**|
|DisplayName|**Is SQM Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sqmenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organization_sqmenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_SupportUserId"></a> SupportUserId

|Property|Value|
|---|---|
|Description|**Unique identifier of the support user for the organization.**|
|DisplayName|**Support User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`supportuserid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_SuppressSLA"></a> SuppressSLA

|Property|Value|
|---|---|
|Description|**Indicates whether SLA is suppressed.**|
|DisplayName|**Is SLA suppressed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`suppresssla`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_suppresssla`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_SuppressValidationEmails"></a> SuppressValidationEmails

|Property|Value|
|---|---|
|Description|**Leave empty to use default setting. Set to on/off to enable/disable Admin emails when Solution Checker validation fails.**|
|DisplayName|**Whether Admin emails are sent when Solution Checker validation fails**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`suppressvalidationemails`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_SyncBulkOperationBatchSize"></a> SyncBulkOperationBatchSize

|Property|Value|
|---|---|
|Description|**Number of records to update per operation in Sync Bulk Pause/Resume/Cancel**|
|DisplayName|**Number of records to update per operation in Sync Bulk Pause/Resume/Cancel**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`syncbulkoperationbatchsize`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|1000|
|MinValue|1|

### <a name="BKMK_SyncBulkOperationMaxLimit"></a> SyncBulkOperationMaxLimit

|Property|Value|
|---|---|
|Description|**Max total number of records to update in database for Sync Bulk Pause/Resume/Cancel**|
|DisplayName|**Max total number of records to update in database for Sync Bulk Pause/Resume/Cancel**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`syncbulkoperationmaxlimit`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|500000|
|MinValue|1|

### <a name="BKMK_SyncOptInSelection"></a> SyncOptInSelection

|Property|Value|
|---|---|
|Description|**Indicates the selection to use the dynamics 365 azure sync framework or server side sync.**|
|DisplayName|**Enable dynamics 365 azure sync framework for this organization.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`syncoptinselection`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_syncoptinselection`|
|DefaultValue|False|
|True Label|Enable|
|False Label|Disable|

### <a name="BKMK_SyncOptInSelectionStatus"></a> SyncOptInSelectionStatus

|Property|Value|
|---|---|
|Description|**Indicates the status of the opt-in or opt-out operation for dynamics 365 azure sync.**|
|DisplayName|**Status of opt-in or opt-out operation for dynamics 365 azure sync.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`syncoptinselectionstatus`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`organization_syncoptinselectionstatus`|

#### SyncOptInSelectionStatus Choices/Options

|Value|Label|
|---|---|
|1|**Processing**|
|2|**Passed**|
|3|**Failed**|

### <a name="BKMK_SystemUserId"></a> SystemUserId

|Property|Value|
|---|---|
|Description|**Unique identifier of the system user for the organization.**|
|DisplayName|**System User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`systemuserid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_TableScopedDVSearchInApps"></a> TableScopedDVSearchInApps

|Property|Value|
|---|---|
|Description|**Controls the appearance of option to search over a single DV search indexed table in model-driven apps’ global search in the header.**|
|DisplayName|**Table Scoped Dataverse Search In Apps**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`tablescopeddvsearchinapps`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_TagMaxAggressiveCycles"></a> TagMaxAggressiveCycles

|Property|Value|
|---|---|
|Description|**Maximum number of aggressive polling cycles executed for email auto-tagging when a new email is received.**|
|DisplayName|**Auto-Tag Max Cycles**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`tagmaxaggressivecycles`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_TagPollingPeriod"></a> TagPollingPeriod

|Property|Value|
|---|---|
|Description|**Normal polling frequency used for email receive auto-tagging in outlook.**|
|DisplayName|**Auto-Tag Interval**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`tagpollingperiod`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_TaskBasedFlowEnabled"></a> TaskBasedFlowEnabled

|Property|Value|
|---|---|
|Description|**Select whether to turn on task flows for the organization.**|
|DisplayName|**Enable Task Flow processes for this Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`taskbasedflowenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_taskbasedflowenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_TeamsChatDataSync"></a> TeamsChatDataSync

|Property|Value|
|---|---|
|Description|**Information on whether Teams Chat Data Sync is enabled.**|
|DisplayName|**Enable Teams Chat Data Sync.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`teamschatdatasync`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_teamschatdatasync`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_TelemetryInstrumentationKey"></a> TelemetryInstrumentationKey

|Property|Value|
|---|---|
|Description|**Instrumentation key for Application Insights used to log plugins telemetry.**|
|DisplayName|**Telemetry Instrumentation Key**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`telemetryinstrumentationkey`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_TextAnalyticsEnabled"></a> TextAnalyticsEnabled

|Property|Value|
|---|---|
|Description|**Select whether to turn on text analytics for the organization.**|
|DisplayName|**Enable Text Analytics for this Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`textanalyticsenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_TimeFormatCode"></a> TimeFormatCode

|Property|Value|
|---|---|
|Description|**Information that specifies how the time is displayed throughout Microsoft CRM.**|
|DisplayName|**Time Format Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timeformatcode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`organization_timeformatcode`|

#### TimeFormatCode Choices/Options

|Value|Label|
|---|---|

### <a name="BKMK_TimeFormatString"></a> TimeFormatString

|Property|Value|
|---|---|
|Description|**Text for how time is displayed in Microsoft Dynamics 365.**|
|DisplayName|**Time Format String**|
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
|Description|**Text for how the time separator is displayed throughout Microsoft Dynamics 365.**|
|DisplayName|**Time Separator**|
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

### <a name="BKMK_TokenExpiry"></a> TokenExpiry

|Property|Value|
|---|---|
|Description|**Duration used for token expiration.**|
|DisplayName|**Token Expiration Duration**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`tokenexpiry`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_TokenKey"></a> TokenKey

|Property|Value|
|---|---|
|Description|**Token key.**|
|DisplayName|**Token Key**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`tokenkey`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|90|

### <a name="BKMK_TraceLogMaximumAgeInDays"></a> TraceLogMaximumAgeInDays

|Property|Value|
|---|---|
|Description|**Tracelog record maximum age in days**|
|DisplayName|**Tracelog record maximum age in days**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`tracelogmaximumageindays`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_TrackingPrefix"></a> TrackingPrefix

|Property|Value|
|---|---|
|Description|**History list of tracking token prefixes.**|
|DisplayName|**Tracking Prefix**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`trackingprefix`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_TrackingTokenIdBase"></a> TrackingTokenIdBase

|Property|Value|
|---|---|
|Description|**Base number used to provide separate tracking token identifiers to users belonging to different deployments.**|
|DisplayName|**Tracking Token Base**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`trackingtokenidbase`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_TrackingTokenIdDigits"></a> TrackingTokenIdDigits

|Property|Value|
|---|---|
|Description|**Number of digits used to represent a tracking token identifier.**|
|DisplayName|**Tracking Token Digits**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`trackingtokeniddigits`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_UniqueSpecifierLength"></a> UniqueSpecifierLength

|Property|Value|
|---|---|
|Description|**Number of characters appended to invoice, quote, and order numbers.**|
|DisplayName|**Unique String Length**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`uniquespecifierlength`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|6|
|MinValue|4|

### <a name="BKMK_UnresolveEmailAddressIfMultipleMatch"></a> UnresolveEmailAddressIfMultipleMatch

|Property|Value|
|---|---|
|Description|**Indicates whether email address should be unresolved if multiple matches are found**|
|DisplayName|**Set To,cc,bcc fields as unresolved if multiple matches are found**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`unresolveemailaddressifmultiplematch`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_unresolveemailaddressifmultiplematch`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_UseInbuiltRuleForDefaultPricelistSelection"></a> UseInbuiltRuleForDefaultPricelistSelection

|Property|Value|
|---|---|
|Description|**Flag indicates whether to Use Inbuilt Rule For DefaultPricelist.**|
|DisplayName|**Use Inbuilt Rule For Default Pricelist Selection**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`useinbuiltrulefordefaultpricelistselection`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organization_usebuiltinrulefordefaultpricelistselection`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_UseLegacyRendering"></a> UseLegacyRendering

|Property|Value|
|---|---|
|Description|**Select whether to use legacy form rendering.**|
|DisplayName|**Legacy Form Rendering**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`uselegacyrendering`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_uselegacyrendering`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_UsePositionHierarchy"></a> UsePositionHierarchy

|Property|Value|
|---|---|
|Description|**Use position hierarchy**|
|DisplayName|**Use position hierarchy**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`usepositionhierarchy`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_usepositionhierarchy`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_UseQuickFindViewForGridSearch"></a> UseQuickFindViewForGridSearch

|Property|Value|
|---|---|
|Description|**Indicates whether searching in a grid should use the Quick Find view for the entity.**|
|DisplayName|**Use Quick Find view when searching in grids**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`usequickfindviewforgridsearch`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_UserAccessAuditingInterval"></a> UserAccessAuditingInterval

|Property|Value|
|---|---|
|Description|**The interval at which user access is checked for auditing.**|
|DisplayName|**User Authentication Auditing Interval**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`useraccessauditinginterval`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_UseReadForm"></a> UseReadForm

|Property|Value|
|---|---|
|Description|**Indicates whether the read-optimized form should be enabled for this organization.**|
|DisplayName|**Use Read-Optimized Form**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`usereadform`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_usereadform`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_UserGroupId"></a> UserGroupId

|Property|Value|
|---|---|
|Description|**Unique identifier of the default group of users in the organization.**|
|DisplayName|**User Group**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`usergroupid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_UserRatingEnabled"></a> UserRatingEnabled

|Property|Value|
|---|---|
|Description|**Enable the user rating feature to show the NSAT score and comment to maker**|
|DisplayName|**Enable the user rating feature**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`userratingenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_UseSkypeProtocol"></a> UseSkypeProtocol

|Property|Value|
|---|---|
|Description|**Indicates default protocol selected for organization.**|
|DisplayName|**User Skype Protocol**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`useskypeprotocol`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_useskypeprotocol`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

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

### <a name="BKMK_ValidationMode"></a> ValidationMode

|Property|Value|
|---|---|
|Description|**Validation mode for apps in this environment**|
|DisplayName|**Validation mode for apps in this environment**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`validationmode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`organization_validationmode`|

#### ValidationMode Choices/Options

|Value|Label|
|---|---|
|0|**Off**|
|1|**Warn**|
|2|**Block**|

### <a name="BKMK_WebResourceHash"></a> WebResourceHash

|Property|Value|
|---|---|
|Description|**Hash value of web resources.**|
|DisplayName|**Web resource hash**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`webresourcehash`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_WeekStartDayCode"></a> WeekStartDayCode

|Property|Value|
|---|---|
|Description|**Designated first day of the week throughout Microsoft Dynamics 365.**|
|DisplayName|**Week Start Day Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`weekstartdaycode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`organization_weekstartdaycode`|

#### WeekStartDayCode Choices/Options

|Value|Label|
|---|---|

### <a name="BKMK_WidgetProperties"></a> WidgetProperties

|Property|Value|
|---|---|
|Description|**For Internal use only.**|
|DisplayName|**For Internal use only.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`widgetproperties`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_YammerGroupId"></a> YammerGroupId

|Property|Value|
|---|---|
|Description|**Denotes the Yammer group ID**|
|DisplayName|**Yammer Group Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`yammergroupid`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_YammerNetworkPermalink"></a> YammerNetworkPermalink

|Property|Value|
|---|---|
|Description|**Denotes the Yammer network permalink**|
|DisplayName|**Yammer Network Permalink**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`yammernetworkpermalink`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_YammerOAuthAccessTokenExpired"></a> YammerOAuthAccessTokenExpired

|Property|Value|
|---|---|
|Description|**Denotes whether the OAuth access token for Yammer network has expired**|
|DisplayName|**Yammer OAuth Access Token Expired**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`yammeroauthaccesstokenexpired`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organization_yammeroauthtokenexpired`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_YammerPostMethod"></a> YammerPostMethod

|Property|Value|
|---|---|
|Description|**Internal Use Only**|
|DisplayName|**Internal Use Only**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`yammerpostmethod`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`organization_yammerpostmethod`|

#### YammerPostMethod Choices/Options

|Value|Label|
|---|---|
|0|**Public**|
|1|**Private**|

### <a name="BKMK_YearStartWeekCode"></a> YearStartWeekCode

|Property|Value|
|---|---|
|Description|**Information that specifies how the first week of the year is specified in Microsoft Dynamics 365.**|
|DisplayName|**Year Start Week Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`yearstartweekcode`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [BaseCurrencyPrecision](#BKMK_BaseCurrencyPrecision)
- [BaseCurrencySymbol](#BKMK_BaseCurrencySymbol)
- [BaseISOCurrencyCode](#BKMK_BaseISOCurrencyCode)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CurrentImportSequenceNumber](#BKMK_CurrentImportSequenceNumber)
- [CurrentParsedTableNumber](#BKMK_CurrentParsedTableNumber)
- [DaysSinceRecordLastModifiedMaxValue](#BKMK_DaysSinceRecordLastModifiedMaxValue)
- [DisabledReason](#BKMK_DisabledReason)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [FiscalSettingsUpdated](#BKMK_FiscalSettingsUpdated)
- [IsAllMoneyDecimal](#BKMK_IsAllMoneyDecimal)
- [IsClusteringEnabled](#BKMK_IsClusteringEnabled)
- [IsDisabled](#BKMK_IsDisabled)
- [MaxSupportedInternetExplorerVersion](#BKMK_MaxSupportedInternetExplorerVersion)
- [MaxVerboseLoggingMailbox](#BKMK_MaxVerboseLoggingMailbox)
- [MaxVerboseLoggingSyncCycles](#BKMK_MaxVerboseLoggingSyncCycles)
- [MetadataSyncLastTimeOfNeverExpiredDeletedObjects](#BKMK_MetadataSyncLastTimeOfNeverExpiredDeletedObjects)
- [MetadataSyncTimestamp](#BKMK_MetadataSyncTimestamp)
- [MobileOfflineMinLicenseProd](#BKMK_MobileOfflineMinLicenseProd)
- [MobileOfflineMinLicenseTrial](#BKMK_MobileOfflineMinLicenseTrial)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [NextCustomObjectTypeCode](#BKMK_NextCustomObjectTypeCode)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationState](#BKMK_OrganizationState)
- [ParsedTableColumnPrefix](#BKMK_ParsedTableColumnPrefix)
- [ParsedTablePrefix](#BKMK_ParsedTablePrefix)
- [V3CalloutConfigHash](#BKMK_V3CalloutConfigHash)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_BaseCurrencyPrecision"></a> BaseCurrencyPrecision

|Property|Value|
|---|---|
|Description|**Number of decimal places that can be used for the base currency.**|
|DisplayName|**Base Currency Precision**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`basecurrencyprecision`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|10|
|MinValue|0|

### <a name="BKMK_BaseCurrencySymbol"></a> BaseCurrencySymbol

|Property|Value|
|---|---|
|Description|**Symbol used for the base currency.**|
|DisplayName|**Base Currency Symbol**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`basecurrencysymbol`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5|

### <a name="BKMK_BaseISOCurrencyCode"></a> BaseISOCurrencyCode

|Property|Value|
|---|---|
|Description||
|DisplayName|**Base ISO Currency Code**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`baseisocurrencycode`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|5|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the organization.**|
|DisplayName|**Created By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the organization was created.**|
|DisplayName|**Created On**|
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
|Description|**Unique identifier of the delegate user who created the organization.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CurrentImportSequenceNumber"></a> CurrentImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Import sequence to use.**|
|DisplayName|**Current Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`currentimportsequencenumber`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_CurrentParsedTableNumber"></a> CurrentParsedTableNumber

|Property|Value|
|---|---|
|Description|**First parsed table number to use.**|
|DisplayName|**Current Parsed Table Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`currentparsedtablenumber`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_DaysSinceRecordLastModifiedMaxValue"></a> DaysSinceRecordLastModifiedMaxValue

|Property|Value|
|---|---|
|Description|**The maximum value for the Mobile Offline setting Days since record last modified**|
|DisplayName|**Max value of Days since record last modified**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`dayssincerecordlastmodifiedmaxvalue`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_DisabledReason"></a> DisabledReason

|Property|Value|
|---|---|
|Description|**Reason for disabling the organization.**|
|DisplayName|**Disabled Reason**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`disabledreason`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_EntityImage_Timestamp"></a> EntityImage_Timestamp

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimage_timestamp`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_EntityImage_URL"></a> EntityImage_URL

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimage_url`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_EntityImageId"></a> EntityImageId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Entity Image Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimageid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_FiscalSettingsUpdated"></a> FiscalSettingsUpdated

|Property|Value|
|---|---|
|Description|**Information that specifies whether the fiscal settings have been updated.**|
|DisplayName|**Is Fiscal Settings Updated**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fiscalsettingsupdated`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_fiscalsettingsupdated`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsAllMoneyDecimal"></a> IsAllMoneyDecimal

|Property|Value|
|---|---|
|Description|**Indicates whether all money attributes are converted to decimal.**|
|DisplayName|**Set if all money attributes are converted to decimal**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isallmoneydecimal`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`organization_featureenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsClusteringEnabled"></a> IsClusteringEnabled

|Property|Value|
|---|---|
|Description|**Read-only flag indicating whether clustering is enabled for the organization.**|
|DisplayName|**Clustering is enabled.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isclusteringenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organization_isclusteringenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsDisabled"></a> IsDisabled

|Property|Value|
|---|---|
|Description|**Information that specifies whether the organization is disabled.**|
|DisplayName|**Is Organization Disabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isdisabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`organization_isdisabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_MaxSupportedInternetExplorerVersion"></a> MaxSupportedInternetExplorerVersion

|Property|Value|
|---|---|
|Description|**The maximum version of IE to run browser emulation for in Outlook client**|
|DisplayName|**Max supported IE version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maxsupportedinternetexplorerversion`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_MaxVerboseLoggingMailbox"></a> MaxVerboseLoggingMailbox

|Property|Value|
|---|---|
|Description|**Maximum number of mailboxes that can be toggled for verbose logging**|
|DisplayName|**Max No Of Mailboxes To Enable For Verbose Logging**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maxverboseloggingmailbox`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_MaxVerboseLoggingSyncCycles"></a> MaxVerboseLoggingSyncCycles

|Property|Value|
|---|---|
|Description|**Maximum number of sync cycles for which verbose logging will be enabled by default**|
|DisplayName|**Maximum number of sync cycles for which verbose logging will be enabled by default**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maxverboseloggingsynccycles`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_MetadataSyncLastTimeOfNeverExpiredDeletedObjects"></a> MetadataSyncLastTimeOfNeverExpiredDeletedObjects

|Property|Value|
|---|---|
|Description|**What is the last date/time where there are metadata tracking deleted objects that have never been outside of the expiration period.**|
|DisplayName|**The last date/time for never expired metadata tracking deleted objects**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`metadatasynclasttimeofneverexpireddeletedobjects`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_MetadataSyncTimestamp"></a> MetadataSyncTimestamp

|Property|Value|
|---|---|
|Description|**Contains the maximum version number for attributes used by metadata synchronization that have changed.**|
|DisplayName|**Metadata sync version**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`metadatasynctimestamp`|
|RequiredLevel|SystemRequired|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_MobileOfflineMinLicenseProd"></a> MobileOfflineMinLicenseProd

|Property|Value|
|---|---|
|Description|**Minimum number of user license required for mobile offline service by production/preview organization**|
|DisplayName|**Minimum number of user license required for mobile offline service by production/preview organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mobileofflineminlicenseprod`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_MobileOfflineMinLicenseTrial"></a> MobileOfflineMinLicenseTrial

|Property|Value|
|---|---|
|Description|**Minimum number of user license required for mobile offline service by trial organization**|
|DisplayName|**Minimum number of user license required for mobile offline service by trial organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mobileofflineminlicensetrial`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the organization.**|
|DisplayName|**Modified By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the organization was last modified.**|
|DisplayName|**Modified On**|
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
|Description|**Unique identifier of the delegate user who last modified the organization.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_NextCustomObjectTypeCode"></a> NextCustomObjectTypeCode

|Property|Value|
|---|---|
|Description|**Next entity type code to use for custom entities.**|
|DisplayName|**Next Entity Type Code**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`nextcustomobjecttypecode`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|10000|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_OrganizationState"></a> OrganizationState

|Property|Value|
|---|---|
|Description|**Indicates the organization lifecycle state**|
|DisplayName|**Organization State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationstate`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`organization_organizationstate`|

#### OrganizationState Choices/Options

|Value|Label|
|---|---|
|0|**Creating**|
|1|**Upgrading**|
|2|**Updating**|
|3|**Active**|

### <a name="BKMK_ParsedTableColumnPrefix"></a> ParsedTableColumnPrefix

|Property|Value|
|---|---|
|Description|**Prefix used for parsed table columns.**|
|DisplayName|**Parsed Table Column Prefix**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parsedtablecolumnprefix`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_ParsedTablePrefix"></a> ParsedTablePrefix

|Property|Value|
|---|---|
|Description|**Prefix used for parsed tables.**|
|DisplayName|**Parsed Table Prefix**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parsedtableprefix`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_V3CalloutConfigHash"></a> V3CalloutConfigHash

|Property|Value|
|---|---|
|Description|**Hash of the V3 callout configuration file.**|
|DisplayName|**V3 Callout Hash**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`v3calloutconfighash`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the organization.**|
|DisplayName|**Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [basecurrency_organization](#BKMK_basecurrency_organization)
- [calendar_organization](#BKMK_calendar_organization)
- [DefaultMobileOfflineProfile_Organization](#BKMK_DefaultMobileOfflineProfile_Organization)
- [EmailServerProfile_Organization](#BKMK_EmailServerProfile_Organization)
- [lk_organization_createdonbehalfby](#BKMK_lk_organization_createdonbehalfby)
- [lk_organization_modifiedonbehalfby](#BKMK_lk_organization_modifiedonbehalfby)
- [lk_organizationbase_createdby](#BKMK_lk_organizationbase_createdby)
- [lk_organizationbase_modifiedby](#BKMK_lk_organizationbase_modifiedby)
- [Template_Organization](#BKMK_Template_Organization)

### <a name="BKMK_basecurrency_organization"></a> basecurrency_organization

One-To-Many Relationship: [transactioncurrency basecurrency_organization](transactioncurrency.md#BKMK_basecurrency_organization)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`basecurrencyid`|
|ReferencingEntityNavigationPropertyName|`basecurrencyid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_calendar_organization"></a> calendar_organization

One-To-Many Relationship: [calendar calendar_organization](calendar.md#BKMK_calendar_organization)

|Property|Value|
|---|---|
|ReferencedEntity|`calendar`|
|ReferencedAttribute|`calendarid`|
|ReferencingAttribute|`businessclosurecalendarid`|
|ReferencingEntityNavigationPropertyName|`businessclosurecalendarid_calendar`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_DefaultMobileOfflineProfile_Organization"></a> DefaultMobileOfflineProfile_Organization

One-To-Many Relationship: [mobileofflineprofile DefaultMobileOfflineProfile_Organization](mobileofflineprofile.md#BKMK_DefaultMobileOfflineProfile_Organization)

|Property|Value|
|---|---|
|ReferencedEntity|`mobileofflineprofile`|
|ReferencedAttribute|`mobileofflineprofileid`|
|ReferencingAttribute|`defaultmobileofflineprofileid`|
|ReferencingEntityNavigationPropertyName|`defaultmobileofflineprofileid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_EmailServerProfile_Organization"></a> EmailServerProfile_Organization

One-To-Many Relationship: [emailserverprofile EmailServerProfile_Organization](emailserverprofile.md#BKMK_EmailServerProfile_Organization)

|Property|Value|
|---|---|
|ReferencedEntity|`emailserverprofile`|
|ReferencedAttribute|`emailserverprofileid`|
|ReferencingAttribute|`defaultemailserverprofileid`|
|ReferencingEntityNavigationPropertyName|`defaultemailserverprofileid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_organization_createdonbehalfby"></a> lk_organization_createdonbehalfby

One-To-Many Relationship: [systemuser lk_organization_createdonbehalfby](systemuser.md#BKMK_lk_organization_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_organization_modifiedonbehalfby"></a> lk_organization_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_organization_modifiedonbehalfby](systemuser.md#BKMK_lk_organization_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_organizationbase_createdby"></a> lk_organizationbase_createdby

One-To-Many Relationship: [systemuser lk_organizationbase_createdby](systemuser.md#BKMK_lk_organizationbase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_organizationbase_modifiedby"></a> lk_organizationbase_modifiedby

One-To-Many Relationship: [systemuser lk_organizationbase_modifiedby](systemuser.md#BKMK_lk_organizationbase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Template_Organization"></a> Template_Organization

One-To-Many Relationship: [template Template_Organization](template.md#BKMK_Template_Organization)

|Property|Value|
|---|---|
|ReferencedEntity|`template`|
|ReferencedAttribute|`templateid`|
|ReferencingAttribute|`acknowledgementtemplateid`|
|ReferencingEntityNavigationPropertyName|`acknowledgementtemplateid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [customcontrol_organization](#BKMK_customcontrol_organization)
- [customcontroldefaultconfig_organization](#BKMK_customcontroldefaultconfig_organization)
- [customcontrolresource_organization](#BKMK_customcontrolresource_organization)
- [languagelocale_organization](#BKMK_languagelocale_organization)
- [lk_dataperformance_organizationid](#BKMK_lk_dataperformance_organizationid)
- [lk_documenttemplatebase_organization](#BKMK_lk_documenttemplatebase_organization)
- [lk_fieldsecurityprofile_organizationid](#BKMK_lk_fieldsecurityprofile_organizationid)
- [lk_principalobjectattributeaccess_organizationid](#BKMK_lk_principalobjectattributeaccess_organizationid)
- [MobileOfflineProfile_organization](#BKMK_MobileOfflineProfile_organization)
- [MobileOfflineProfileItem_organization](#BKMK_MobileOfflineProfileItem_organization)
- [MobileOfflineProfileItemAssociation_organization](#BKMK_MobileOfflineProfileItemAssociation_organization)
- [organization_aciviewmapper](#BKMK_organization_aciviewmapper)
- [organization_adx_externalidentity](#BKMK_organization_adx_externalidentity)
- [organization_adx_webformsession](#BKMK_organization_adx_webformsession)
- [organization_aicopilot](#BKMK_organization_aicopilot)
- [organization_aiplugintitle](#BKMK_organization_aiplugintitle)
- [organization_appaction](#BKMK_organization_appaction)
- [organization_appactionmigration](#BKMK_organization_appactionmigration)
- [organization_appactionrule](#BKMK_organization_appactionrule)
- [organization_appconfig](#BKMK_organization_appconfig)
- [organization_appconfiginstance](#BKMK_organization_appconfiginstance)
- [organization_appconfigmaster](#BKMK_organization_appconfigmaster)
- [organization_application](#BKMK_organization_application)
- [organization_appmodule](#BKMK_organization_appmodule)
- [Organization_AsyncOperations](#BKMK_Organization_AsyncOperations)
- [organization_attributeclusterconfig](#BKMK_organization_attributeclusterconfig)
- [Organization_BulkDeleteFailures](#BKMK_Organization_BulkDeleteFailures)
- [organization_business_unit_news_articles](#BKMK_organization_business_unit_news_articles)
- [organization_business_units](#BKMK_organization_business_units)
- [organization_calendars](#BKMK_organization_calendars)
- [organization_catalog](#BKMK_organization_catalog)
- [organization_catalogassignment](#BKMK_organization_catalogassignment)
- [organization_complexcontrols](#BKMK_organization_complexcontrols)
- [organization_connection_roles](#BKMK_organization_connection_roles)
- [organization_copilotexamplequestion](#BKMK_organization_copilotexamplequestion)
- [organization_custom_displaystrings](#BKMK_organization_custom_displaystrings)
- [organization_datalakeworkspace](#BKMK_organization_datalakeworkspace)
- [organization_datalakeworkspacepermission](#BKMK_organization_datalakeworkspacepermission)
- [organization_dataprocessingconfiguration](#BKMK_organization_dataprocessingconfiguration)
- [organization_delegatedauthorization](#BKMK_organization_delegatedauthorization)
- [organization_emailaddressconfiguration](#BKMK_organization_emailaddressconfiguration)
- [organization_emailserverprofile](#BKMK_organization_emailserverprofile)
- [organization_entityanalyticsconfig](#BKMK_organization_entityanalyticsconfig)
- [organization_entityclusterconfig](#BKMK_organization_entityclusterconfig)
- [organization_entitydataprovider](#BKMK_organization_entitydataprovider)
- [organization_entityrecordfilter](#BKMK_organization_entityrecordfilter)
- [organization_expiredprocess](#BKMK_organization_expiredprocess)
- [organization_importjob](#BKMK_organization_importjob)
- [organization_kb_article_templates](#BKMK_organization_kb_article_templates)
- [organization_kb_articles](#BKMK_organization_kb_articles)
- [organization_KnowledgeBaseRecord](#BKMK_organization_KnowledgeBaseRecord)
- [organization_mailbox](#BKMK_organization_mailbox)
- [Organization_MailboxTrackingFolder](#BKMK_Organization_MailboxTrackingFolder)
- [organization_mainfewshot](#BKMK_organization_mainfewshot)
- [organization_makerfewshot](#BKMK_organization_makerfewshot)
- [organization_maskingrule](#BKMK_organization_maskingrule)
- [organization_metadataforarchival](#BKMK_organization_metadataforarchival)
- [organization_metric](#BKMK_organization_metric)
- [organization_mobileofflineprofileextension](#BKMK_organization_mobileofflineprofileextension)
- [organization_msdyn_appinsightsmetadata](#BKMK_organization_msdyn_appinsightsmetadata)
- [organization_msdyn_federatedarticleincident](#BKMK_organization_msdyn_federatedarticleincident)
- [organization_msdyn_helppage](#BKMK_organization_msdyn_helppage)
- [organization_msdyn_insightsstorevirtualentity](#BKMK_organization_msdyn_insightsstorevirtualentity)
- [organization_msdyn_kmpersonalizationsetting](#BKMK_organization_msdyn_kmpersonalizationsetting)
- [organization_msdyn_knowledgeconfiguration](#BKMK_organization_msdyn_knowledgeconfiguration)
- [organization_msdyn_modulerundetail](#BKMK_organization_msdyn_modulerundetail)
- [organization_msdyn_solutionhealthruleset](#BKMK_organization_msdyn_solutionhealthruleset)
- [organization_msdyn_tour](#BKMK_organization_msdyn_tour)
- [organization_msdyn_workflowactionstatus](#BKMK_organization_msdyn_workflowactionstatus)
- [organization_navigationsetting](#BKMK_organization_navigationsetting)
- [organization_newprocess](#BKMK_organization_newprocess)
- [organization_officegraphdocument](#BKMK_organization_officegraphdocument)
- [organization_organizationdatasyncfnostate](#BKMK_organization_organizationdatasyncfnostate)
- [organization_organizationdatasyncstate](#BKMK_organization_organizationdatasyncstate)
- [organization_organizationdatasyncsubscription](#BKMK_organization_organizationdatasyncsubscription)
- [organization_organizationdatasyncsubscriptionentity](#BKMK_organization_organizationdatasyncsubscriptionentity)
- [organization_organizationdatasyncsubscriptionfnotable](#BKMK_organization_organizationdatasyncsubscriptionfnotable)
- [organization_package](#BKMK_organization_package)
- [organization_packagehistory](#BKMK_organization_packagehistory)
- [organization_pluginassembly](#BKMK_organization_pluginassembly)
- [organization_pluginpackage](#BKMK_organization_pluginpackage)
- [organization_plugintype](#BKMK_organization_plugintype)
- [organization_plugintypestatistic](#BKMK_organization_plugintypestatistic)
- [organization_position](#BKMK_organization_position)
- [organization_post](#BKMK_organization_post)
- [organization_PostComment](#BKMK_organization_PostComment)
- [organization_postlike](#BKMK_organization_postlike)
- [organization_privilegesremovalsetting](#BKMK_organization_privilegesremovalsetting)
- [organization_publisher](#BKMK_organization_publisher)
- [organization_queueitems](#BKMK_organization_queueitems)
- [organization_queues](#BKMK_organization_queues)
- [organization_recommendeddocument](#BKMK_organization_recommendeddocument)
- [organization_recordfilter](#BKMK_organization_recordfilter)
- [organization_recyclebinconfig](#BKMK_organization_recyclebinconfig)
- [organization_relationshipattribute](#BKMK_organization_relationshipattribute)
- [organization_retentionoperationdetail](#BKMK_organization_retentionoperationdetail)
- [organization_roleeditorlayout](#BKMK_organization_roleeditorlayout)
- [organization_roles](#BKMK_organization_roles)
- [organization_sa_suggestedaction](#BKMK_organization_sa_suggestedaction)
- [organization_sa_suggestedactioncriteria](#BKMK_organization_sa_suggestedactioncriteria)
- [organization_saved_queries](#BKMK_organization_saved_queries)
- [organization_saved_query_visualizations](#BKMK_organization_saved_query_visualizations)
- [organization_sdkmessage](#BKMK_organization_sdkmessage)
- [organization_sdkmessagefilter](#BKMK_organization_sdkmessagefilter)
- [organization_sdkmessageprocessingstep](#BKMK_organization_sdkmessageprocessingstep)
- [organization_sdkmessageprocessingstepimage](#BKMK_organization_sdkmessageprocessingstepimage)
- [organization_sdkmessageprocessingstepsecureconfig](#BKMK_organization_sdkmessageprocessingstepsecureconfig)
- [organization_searchattributesettings](#BKMK_organization_searchattributesettings)
- [organization_searchcustomanalyzer](#BKMK_organization_searchcustomanalyzer)
- [organization_searchrelationshipsettings](#BKMK_organization_searchrelationshipsettings)
- [organization_serviceendpoint](#BKMK_organization_serviceendpoint)
- [organization_sharedlinksetting](#BKMK_organization_sharedlinksetting)
- [organization_sharepointmanagedidentity](#BKMK_organization_sharepointmanagedidentity)
- [organization_similarityrule](#BKMK_organization_similarityrule)
- [organization_sitemap](#BKMK_organization_sitemap)
- [organization_solution](#BKMK_organization_solution)
- [organization_solutioncomponentattributeconfiguration](#BKMK_organization_solutioncomponentattributeconfiguration)
- [organization_solutioncomponentconfiguration](#BKMK_organization_solutioncomponentconfiguration)
- [organization_solutioncomponentrelationshipconfiguration](#BKMK_organization_solutioncomponentrelationshipconfiguration)
- [organization_subjects](#BKMK_organization_subjects)
- [organization_supportusertable](#BKMK_organization_supportusertable)
- [organization_synapselinkexternaltablestate](#BKMK_organization_synapselinkexternaltablestate)
- [organization_synapselinkprofile](#BKMK_organization_synapselinkprofile)
- [organization_synapselinkprofileentity](#BKMK_organization_synapselinkprofileentity)
- [organization_synapselinkprofileentitystate](#BKMK_organization_synapselinkprofileentitystate)
- [organization_synapselinkschedule](#BKMK_organization_synapselinkschedule)
- [Organization_SyncErrors](#BKMK_Organization_SyncErrors)
- [organization_system_users](#BKMK_organization_system_users)
- [organization_systemforms](#BKMK_organization_systemforms)
- [organization_teammobileofflineprofilemembership](#BKMK_organization_teammobileofflineprofilemembership)
- [organization_teams](#BKMK_organization_teams)
- [organization_territories](#BKMK_organization_territories)
- [organization_textanalyticsentitymapping](#BKMK_organization_textanalyticsentitymapping)
- [organization_theme](#BKMK_organization_theme)
- [organization_tracelog](#BKMK_organization_tracelog)
- [organization_transactioncurrencies](#BKMK_organization_transactioncurrencies)
- [organization_translationprocess](#BKMK_organization_translationprocess)
- [organization_UserMapping](#BKMK_organization_UserMapping)
- [organization_usermobileofflineprofilemembership](#BKMK_organization_usermobileofflineprofilemembership)
- [organization_userrating](#BKMK_organization_userrating)
- [organization_viewasexamplequestion](#BKMK_organization_viewasexamplequestion)
- [organization_virtualentitymetadata](#BKMK_organization_virtualentitymetadata)
- [organization_webwizard](#BKMK_organization_webwizard)
- [webresource_organization](#BKMK_webresource_organization)

### <a name="BKMK_customcontrol_organization"></a> customcontrol_organization

Many-To-One Relationship: [customcontrol customcontrol_organization](customcontrol.md#BKMK_customcontrol_organization)

|Property|Value|
|---|---|
|ReferencingEntity|`customcontrol`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`customcontrol_organization`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_customcontroldefaultconfig_organization"></a> customcontroldefaultconfig_organization

Many-To-One Relationship: [customcontroldefaultconfig customcontroldefaultconfig_organization](customcontroldefaultconfig.md#BKMK_customcontroldefaultconfig_organization)

|Property|Value|
|---|---|
|ReferencingEntity|`customcontroldefaultconfig`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`customcontroldefaultconfig_organization`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_customcontrolresource_organization"></a> customcontrolresource_organization

Many-To-One Relationship: [customcontrolresource customcontrolresource_organization](customcontrolresource.md#BKMK_customcontrolresource_organization)

|Property|Value|
|---|---|
|ReferencingEntity|`customcontrolresource`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`customcontrolresource_organization`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_languagelocale_organization"></a> languagelocale_organization

Many-To-One Relationship: [languagelocale languagelocale_organization](languagelocale.md#BKMK_languagelocale_organization)

|Property|Value|
|---|---|
|ReferencingEntity|`languagelocale`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`languagelocale_organization`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_dataperformance_organizationid"></a> lk_dataperformance_organizationid

Many-To-One Relationship: [dataperformance lk_dataperformance_organizationid](dataperformance.md#BKMK_lk_dataperformance_organizationid)

|Property|Value|
|---|---|
|ReferencingEntity|`dataperformance`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`lk_dataperformance_organizationid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_documenttemplatebase_organization"></a> lk_documenttemplatebase_organization

Many-To-One Relationship: [documenttemplate lk_documenttemplatebase_organization](documenttemplate.md#BKMK_lk_documenttemplatebase_organization)

|Property|Value|
|---|---|
|ReferencingEntity|`documenttemplate`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`lk_documenttemplatebase_organization`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_fieldsecurityprofile_organizationid"></a> lk_fieldsecurityprofile_organizationid

Many-To-One Relationship: [fieldsecurityprofile lk_fieldsecurityprofile_organizationid](fieldsecurityprofile.md#BKMK_lk_fieldsecurityprofile_organizationid)

|Property|Value|
|---|---|
|ReferencingEntity|`fieldsecurityprofile`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`lk_fieldsecurityprofile_organizationid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_principalobjectattributeaccess_organizationid"></a> lk_principalobjectattributeaccess_organizationid

Many-To-One Relationship: [principalobjectattributeaccess lk_principalobjectattributeaccess_organizationid](principalobjectattributeaccess.md#BKMK_lk_principalobjectattributeaccess_organizationid)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`lk_principalobjectattributeaccess_organizationid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_MobileOfflineProfile_organization"></a> MobileOfflineProfile_organization

Many-To-One Relationship: [mobileofflineprofile MobileOfflineProfile_organization](mobileofflineprofile.md#BKMK_MobileOfflineProfile_organization)

|Property|Value|
|---|---|
|ReferencingEntity|`mobileofflineprofile`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`MobileOfflineProfile_organization`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_MobileOfflineProfileItem_organization"></a> MobileOfflineProfileItem_organization

Many-To-One Relationship: [mobileofflineprofileitem MobileOfflineProfileItem_organization](mobileofflineprofileitem.md#BKMK_MobileOfflineProfileItem_organization)

|Property|Value|
|---|---|
|ReferencingEntity|`mobileofflineprofileitem`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`MobileOfflineProfileItem_organization`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_MobileOfflineProfileItemAssociation_organization"></a> MobileOfflineProfileItemAssociation_organization

Many-To-One Relationship: [mobileofflineprofileitemassociation MobileOfflineProfileItemAssociation_organization](mobileofflineprofileitemassociation.md#BKMK_MobileOfflineProfileItemAssociation_organization)

|Property|Value|
|---|---|
|ReferencingEntity|`mobileofflineprofileitemassociation`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`MobileOfflineProfileItemAssociation_organization`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_aciviewmapper"></a> organization_aciviewmapper

Many-To-One Relationship: [aciviewmapper organization_aciviewmapper](aciviewmapper.md#BKMK_organization_aciviewmapper)

|Property|Value|
|---|---|
|ReferencingEntity|`aciviewmapper`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_aciviewmapper`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_adx_externalidentity"></a> organization_adx_externalidentity

Many-To-One Relationship: [adx_externalidentity organization_adx_externalidentity](adx_externalidentity.md#BKMK_organization_adx_externalidentity)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_externalidentity`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_adx_externalidentity`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_adx_webformsession"></a> organization_adx_webformsession

Many-To-One Relationship: [adx_webformsession organization_adx_webformsession](adx_webformsession.md#BKMK_organization_adx_webformsession)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_webformsession`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_adx_webformsession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_aicopilot"></a> organization_aicopilot

Many-To-One Relationship: [aicopilot organization_aicopilot](aicopilot.md#BKMK_organization_aicopilot)

|Property|Value|
|---|---|
|ReferencingEntity|`aicopilot`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_aicopilot`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_aiplugintitle"></a> organization_aiplugintitle

Many-To-One Relationship: [aiplugintitle organization_aiplugintitle](aiplugintitle.md#BKMK_organization_aiplugintitle)

|Property|Value|
|---|---|
|ReferencingEntity|`aiplugintitle`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_aiplugintitle`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_appaction"></a> organization_appaction

Many-To-One Relationship: [appaction organization_appaction](appaction.md#BKMK_organization_appaction)

|Property|Value|
|---|---|
|ReferencingEntity|`appaction`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_appaction`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_appactionmigration"></a> organization_appactionmigration

Many-To-One Relationship: [appactionmigration organization_appactionmigration](appactionmigration.md#BKMK_organization_appactionmigration)

|Property|Value|
|---|---|
|ReferencingEntity|`appactionmigration`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_appactionmigration`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_appactionrule"></a> organization_appactionrule

Many-To-One Relationship: [appactionrule organization_appactionrule](appactionrule.md#BKMK_organization_appactionrule)

|Property|Value|
|---|---|
|ReferencingEntity|`appactionrule`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_appactionrule`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_appconfig"></a> organization_appconfig

Many-To-One Relationship: [appconfig organization_appconfig](appconfig.md#BKMK_organization_appconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`appconfig`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_appconfig`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_appconfiginstance"></a> organization_appconfiginstance

Many-To-One Relationship: [appconfiginstance organization_appconfiginstance](appconfiginstance.md#BKMK_organization_appconfiginstance)

|Property|Value|
|---|---|
|ReferencingEntity|`appconfiginstance`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_appconfiginstance`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_appconfigmaster"></a> organization_appconfigmaster

Many-To-One Relationship: [appconfigmaster organization_appconfigmaster](appconfigmaster.md#BKMK_organization_appconfigmaster)

|Property|Value|
|---|---|
|ReferencingEntity|`appconfigmaster`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_appconfigmaster`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_application"></a> organization_application

Many-To-One Relationship: [application organization_application](application.md#BKMK_organization_application)

|Property|Value|
|---|---|
|ReferencingEntity|`application`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_application`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_appmodule"></a> organization_appmodule

Many-To-One Relationship: [appmodule organization_appmodule](appmodule.md#BKMK_organization_appmodule)

|Property|Value|
|---|---|
|ReferencingEntity|`appmodule`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_appmodule`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Organization_AsyncOperations"></a> Organization_AsyncOperations

Many-To-One Relationship: [asyncoperation Organization_AsyncOperations](asyncoperation.md#BKMK_Organization_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Organization_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_attributeclusterconfig"></a> organization_attributeclusterconfig

Many-To-One Relationship: [attributeclusterconfig organization_attributeclusterconfig](attributeclusterconfig.md#BKMK_organization_attributeclusterconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`attributeclusterconfig`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_attributeclusterconfig`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Organization_BulkDeleteFailures"></a> Organization_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure Organization_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Organization_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Organization_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_business_unit_news_articles"></a> organization_business_unit_news_articles

Many-To-One Relationship: [businessunitnewsarticle organization_business_unit_news_articles](businessunitnewsarticle.md#BKMK_organization_business_unit_news_articles)

|Property|Value|
|---|---|
|ReferencingEntity|`businessunitnewsarticle`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_business_unit_news_articles`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_business_units"></a> organization_business_units

Many-To-One Relationship: [businessunit organization_business_units](businessunit.md#BKMK_organization_business_units)

|Property|Value|
|---|---|
|ReferencingEntity|`businessunit`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_business_units`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_calendars"></a> organization_calendars

Many-To-One Relationship: [calendar organization_calendars](calendar.md#BKMK_organization_calendars)

|Property|Value|
|---|---|
|ReferencingEntity|`calendar`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_calendars`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_catalog"></a> organization_catalog

Many-To-One Relationship: [catalog organization_catalog](catalog.md#BKMK_organization_catalog)

|Property|Value|
|---|---|
|ReferencingEntity|`catalog`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_catalog`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_catalogassignment"></a> organization_catalogassignment

Many-To-One Relationship: [catalogassignment organization_catalogassignment](catalogassignment.md#BKMK_organization_catalogassignment)

|Property|Value|
|---|---|
|ReferencingEntity|`catalogassignment`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_catalogassignment`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_complexcontrols"></a> organization_complexcontrols

Many-To-One Relationship: [complexcontrol organization_complexcontrols](complexcontrol.md#BKMK_organization_complexcontrols)

|Property|Value|
|---|---|
|ReferencingEntity|`complexcontrol`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_complexcontrols`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_connection_roles"></a> organization_connection_roles

Many-To-One Relationship: [connectionrole organization_connection_roles](connectionrole.md#BKMK_organization_connection_roles)

|Property|Value|
|---|---|
|ReferencingEntity|`connectionrole`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_connection_roles`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_copilotexamplequestion"></a> organization_copilotexamplequestion

Many-To-One Relationship: [copilotexamplequestion organization_copilotexamplequestion](copilotexamplequestion.md#BKMK_organization_copilotexamplequestion)

|Property|Value|
|---|---|
|ReferencingEntity|`copilotexamplequestion`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_copilotexamplequestion`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_custom_displaystrings"></a> organization_custom_displaystrings

Many-To-One Relationship: [displaystring organization_custom_displaystrings](displaystring.md#BKMK_organization_custom_displaystrings)

|Property|Value|
|---|---|
|ReferencingEntity|`displaystring`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_custom_displaystrings`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_datalakeworkspace"></a> organization_datalakeworkspace

Many-To-One Relationship: [datalakeworkspace organization_datalakeworkspace](datalakeworkspace.md#BKMK_organization_datalakeworkspace)

|Property|Value|
|---|---|
|ReferencingEntity|`datalakeworkspace`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_datalakeworkspace`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_datalakeworkspacepermission"></a> organization_datalakeworkspacepermission

Many-To-One Relationship: [datalakeworkspacepermission organization_datalakeworkspacepermission](datalakeworkspacepermission.md#BKMK_organization_datalakeworkspacepermission)

|Property|Value|
|---|---|
|ReferencingEntity|`datalakeworkspacepermission`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_datalakeworkspacepermission`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_dataprocessingconfiguration"></a> organization_dataprocessingconfiguration

Many-To-One Relationship: [dataprocessingconfiguration organization_dataprocessingconfiguration](dataprocessingconfiguration.md#BKMK_organization_dataprocessingconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`dataprocessingconfiguration`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_dataprocessingconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_delegatedauthorization"></a> organization_delegatedauthorization

Many-To-One Relationship: [delegatedauthorization organization_delegatedauthorization](delegatedauthorization.md#BKMK_organization_delegatedauthorization)

|Property|Value|
|---|---|
|ReferencingEntity|`delegatedauthorization`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_delegatedauthorization`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_emailaddressconfiguration"></a> organization_emailaddressconfiguration

Many-To-One Relationship: [emailaddressconfiguration organization_emailaddressconfiguration](emailaddressconfiguration.md#BKMK_organization_emailaddressconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`emailaddressconfiguration`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_emailaddressconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_emailserverprofile"></a> organization_emailserverprofile

Many-To-One Relationship: [emailserverprofile organization_emailserverprofile](emailserverprofile.md#BKMK_organization_emailserverprofile)

|Property|Value|
|---|---|
|ReferencingEntity|`emailserverprofile`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_emailserverprofile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_entityanalyticsconfig"></a> organization_entityanalyticsconfig

Many-To-One Relationship: [entityanalyticsconfig organization_entityanalyticsconfig](entityanalyticsconfig.md#BKMK_organization_entityanalyticsconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`entityanalyticsconfig`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_entityanalyticsconfig`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_entityclusterconfig"></a> organization_entityclusterconfig

Many-To-One Relationship: [entityclusterconfig organization_entityclusterconfig](entityclusterconfig.md#BKMK_organization_entityclusterconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`entityclusterconfig`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_entityclusterconfig`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_entitydataprovider"></a> organization_entitydataprovider

Many-To-One Relationship: [entitydataprovider organization_entitydataprovider](entitydataprovider.md#BKMK_organization_entitydataprovider)

|Property|Value|
|---|---|
|ReferencingEntity|`entitydataprovider`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_entitydataprovider`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_entityrecordfilter"></a> organization_entityrecordfilter

Many-To-One Relationship: [entityrecordfilter organization_entityrecordfilter](entityrecordfilter.md#BKMK_organization_entityrecordfilter)

|Property|Value|
|---|---|
|ReferencingEntity|`entityrecordfilter`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_entityrecordfilter`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_expiredprocess"></a> organization_expiredprocess

Many-To-One Relationship: [expiredprocess organization_expiredprocess](expiredprocess.md#BKMK_organization_expiredprocess)

|Property|Value|
|---|---|
|ReferencingEntity|`expiredprocess`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_expiredprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_importjob"></a> organization_importjob

Many-To-One Relationship: [importjob organization_importjob](importjob.md#BKMK_organization_importjob)

|Property|Value|
|---|---|
|ReferencingEntity|`importjob`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_importjob`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_kb_article_templates"></a> organization_kb_article_templates

Many-To-One Relationship: [kbarticletemplate organization_kb_article_templates](kbarticletemplate.md#BKMK_organization_kb_article_templates)

|Property|Value|
|---|---|
|ReferencingEntity|`kbarticletemplate`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_kb_article_templates`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_kb_articles"></a> organization_kb_articles

Many-To-One Relationship: [kbarticle organization_kb_articles](kbarticle.md#BKMK_organization_kb_articles)

|Property|Value|
|---|---|
|ReferencingEntity|`kbarticle`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_kb_articles`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_KnowledgeBaseRecord"></a> organization_KnowledgeBaseRecord

Many-To-One Relationship: [knowledgebaserecord organization_KnowledgeBaseRecord](knowledgebaserecord.md#BKMK_organization_KnowledgeBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`knowledgebaserecord`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_KnowledgeBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_mailbox"></a> organization_mailbox

Many-To-One Relationship: [mailbox organization_mailbox](mailbox.md#BKMK_organization_mailbox)

|Property|Value|
|---|---|
|ReferencingEntity|`mailbox`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_mailbox`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Organization_MailboxTrackingFolder"></a> Organization_MailboxTrackingFolder

Many-To-One Relationship: [mailboxtrackingfolder Organization_MailboxTrackingFolder](mailboxtrackingfolder.md#BKMK_Organization_MailboxTrackingFolder)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`Organization_MailboxTrackingFolder`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_mainfewshot"></a> organization_mainfewshot

Many-To-One Relationship: [mainfewshot organization_mainfewshot](mainfewshot.md#BKMK_organization_mainfewshot)

|Property|Value|
|---|---|
|ReferencingEntity|`mainfewshot`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_mainfewshot`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_makerfewshot"></a> organization_makerfewshot

Many-To-One Relationship: [makerfewshot organization_makerfewshot](makerfewshot.md#BKMK_organization_makerfewshot)

|Property|Value|
|---|---|
|ReferencingEntity|`makerfewshot`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_makerfewshot`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_maskingrule"></a> organization_maskingrule

Many-To-One Relationship: [maskingrule organization_maskingrule](maskingrule.md#BKMK_organization_maskingrule)

|Property|Value|
|---|---|
|ReferencingEntity|`maskingrule`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_maskingrule`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_metadataforarchival"></a> organization_metadataforarchival

Many-To-One Relationship: [metadataforarchival organization_metadataforarchival](metadataforarchival.md#BKMK_organization_metadataforarchival)

|Property|Value|
|---|---|
|ReferencingEntity|`metadataforarchival`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_metadataforarchival`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_metric"></a> organization_metric

Many-To-One Relationship: [metric organization_metric](metric.md#BKMK_organization_metric)

|Property|Value|
|---|---|
|ReferencingEntity|`metric`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_metric`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_mobileofflineprofileextension"></a> organization_mobileofflineprofileextension

Many-To-One Relationship: [mobileofflineprofileextension organization_mobileofflineprofileextension](mobileofflineprofileextension.md#BKMK_organization_mobileofflineprofileextension)

|Property|Value|
|---|---|
|ReferencingEntity|`mobileofflineprofileextension`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_mobileofflineprofileextension`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_msdyn_appinsightsmetadata"></a> organization_msdyn_appinsightsmetadata

Many-To-One Relationship: [msdyn_appinsightsmetadata organization_msdyn_appinsightsmetadata](msdyn_appinsightsmetadata.md#BKMK_organization_msdyn_appinsightsmetadata)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_appinsightsmetadata`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_msdyn_appinsightsmetadata`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_msdyn_federatedarticleincident"></a> organization_msdyn_federatedarticleincident

Many-To-One Relationship: [msdyn_federatedarticleincident organization_msdyn_federatedarticleincident](msdyn_federatedarticleincident.md#BKMK_organization_msdyn_federatedarticleincident)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_federatedarticleincident`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_msdyn_federatedarticleincident`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_msdyn_helppage"></a> organization_msdyn_helppage

Many-To-One Relationship: [msdyn_helppage organization_msdyn_helppage](msdyn_helppage.md#BKMK_organization_msdyn_helppage)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_helppage`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_msdyn_helppage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_msdyn_insightsstorevirtualentity"></a> organization_msdyn_insightsstorevirtualentity

Many-To-One Relationship: [msdyn_insightsstorevirtualentity organization_msdyn_insightsstorevirtualentity](msdyn_insightsstorevirtualentity.md#BKMK_organization_msdyn_insightsstorevirtualentity)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_insightsstorevirtualentity`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_msdyn_insightsstorevirtualentity`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_msdyn_kmpersonalizationsetting"></a> organization_msdyn_kmpersonalizationsetting

Many-To-One Relationship: [msdyn_kmpersonalizationsetting organization_msdyn_kmpersonalizationsetting](msdyn_kmpersonalizationsetting.md#BKMK_organization_msdyn_kmpersonalizationsetting)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_kmpersonalizationsetting`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_msdyn_kmpersonalizationsetting`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_msdyn_knowledgeconfiguration"></a> organization_msdyn_knowledgeconfiguration

Many-To-One Relationship: [msdyn_knowledgeconfiguration organization_msdyn_knowledgeconfiguration](msdyn_knowledgeconfiguration.md#BKMK_organization_msdyn_knowledgeconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgeconfiguration`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_msdyn_knowledgeconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_msdyn_modulerundetail"></a> organization_msdyn_modulerundetail

Many-To-One Relationship: [msdyn_modulerundetail organization_msdyn_modulerundetail](msdyn_modulerundetail.md#BKMK_organization_msdyn_modulerundetail)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_modulerundetail`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_msdyn_modulerundetail`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_msdyn_solutionhealthruleset"></a> organization_msdyn_solutionhealthruleset

Many-To-One Relationship: [msdyn_solutionhealthruleset organization_msdyn_solutionhealthruleset](msdyn_solutionhealthruleset.md#BKMK_organization_msdyn_solutionhealthruleset)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_solutionhealthruleset`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_msdyn_solutionhealthruleset`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_msdyn_tour"></a> organization_msdyn_tour

Many-To-One Relationship: [msdyn_tour organization_msdyn_tour](msdyn_tour.md#BKMK_organization_msdyn_tour)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_tour`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_msdyn_tour`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_msdyn_workflowactionstatus"></a> organization_msdyn_workflowactionstatus

Many-To-One Relationship: [msdyn_workflowactionstatus organization_msdyn_workflowactionstatus](msdyn_workflowactionstatus.md#BKMK_organization_msdyn_workflowactionstatus)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_workflowactionstatus`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_msdyn_workflowactionstatus`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_navigationsetting"></a> organization_navigationsetting

Many-To-One Relationship: [navigationsetting organization_navigationsetting](navigationsetting.md#BKMK_organization_navigationsetting)

|Property|Value|
|---|---|
|ReferencingEntity|`navigationsetting`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_navigationsetting`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_newprocess"></a> organization_newprocess

Many-To-One Relationship: [newprocess organization_newprocess](newprocess.md#BKMK_organization_newprocess)

|Property|Value|
|---|---|
|ReferencingEntity|`newprocess`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_newprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_officegraphdocument"></a> organization_officegraphdocument

Many-To-One Relationship: [officegraphdocument organization_officegraphdocument](officegraphdocument.md#BKMK_organization_officegraphdocument)

|Property|Value|
|---|---|
|ReferencingEntity|`officegraphdocument`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_officegraphdocument`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_organizationdatasyncfnostate"></a> organization_organizationdatasyncfnostate

Many-To-One Relationship: [organizationdatasyncfnostate organization_organizationdatasyncfnostate](organizationdatasyncfnostate.md#BKMK_organization_organizationdatasyncfnostate)

|Property|Value|
|---|---|
|ReferencingEntity|`organizationdatasyncfnostate`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_organizationdatasyncfnostate`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_organizationdatasyncstate"></a> organization_organizationdatasyncstate

Many-To-One Relationship: [organizationdatasyncstate organization_organizationdatasyncstate](organizationdatasyncstate.md#BKMK_organization_organizationdatasyncstate)

|Property|Value|
|---|---|
|ReferencingEntity|`organizationdatasyncstate`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_organizationdatasyncstate`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_organizationdatasyncsubscription"></a> organization_organizationdatasyncsubscription

Many-To-One Relationship: [organizationdatasyncsubscription organization_organizationdatasyncsubscription](organizationdatasyncsubscription.md#BKMK_organization_organizationdatasyncsubscription)

|Property|Value|
|---|---|
|ReferencingEntity|`organizationdatasyncsubscription`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_organizationdatasyncsubscription`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_organizationdatasyncsubscriptionentity"></a> organization_organizationdatasyncsubscriptionentity

Many-To-One Relationship: [organizationdatasyncsubscriptionentity organization_organizationdatasyncsubscriptionentity](organizationdatasyncsubscriptionentity.md#BKMK_organization_organizationdatasyncsubscriptionentity)

|Property|Value|
|---|---|
|ReferencingEntity|`organizationdatasyncsubscriptionentity`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_organizationdatasyncsubscriptionentity`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_organizationdatasyncsubscriptionfnotable"></a> organization_organizationdatasyncsubscriptionfnotable

Many-To-One Relationship: [organizationdatasyncsubscriptionfnotable organization_organizationdatasyncsubscriptionfnotable](organizationdatasyncsubscriptionfnotable.md#BKMK_organization_organizationdatasyncsubscriptionfnotable)

|Property|Value|
|---|---|
|ReferencingEntity|`organizationdatasyncsubscriptionfnotable`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_organizationdatasyncsubscriptionfnotable`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_package"></a> organization_package

Many-To-One Relationship: [package organization_package](package.md#BKMK_organization_package)

|Property|Value|
|---|---|
|ReferencingEntity|`package`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_package`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_packagehistory"></a> organization_packagehistory

Many-To-One Relationship: [packagehistory organization_packagehistory](packagehistory.md#BKMK_organization_packagehistory)

|Property|Value|
|---|---|
|ReferencingEntity|`packagehistory`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_packagehistory`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_pluginassembly"></a> organization_pluginassembly

Many-To-One Relationship: [pluginassembly organization_pluginassembly](pluginassembly.md#BKMK_organization_pluginassembly)

|Property|Value|
|---|---|
|ReferencingEntity|`pluginassembly`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_pluginassembly`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_pluginpackage"></a> organization_pluginpackage

Many-To-One Relationship: [pluginpackage organization_pluginpackage](pluginpackage.md#BKMK_organization_pluginpackage)

|Property|Value|
|---|---|
|ReferencingEntity|`pluginpackage`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_pluginpackage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_plugintype"></a> organization_plugintype

Many-To-One Relationship: [plugintype organization_plugintype](plugintype.md#BKMK_organization_plugintype)

|Property|Value|
|---|---|
|ReferencingEntity|`plugintype`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_plugintype`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_plugintypestatistic"></a> organization_plugintypestatistic

Many-To-One Relationship: [plugintypestatistic organization_plugintypestatistic](plugintypestatistic.md#BKMK_organization_plugintypestatistic)

|Property|Value|
|---|---|
|ReferencingEntity|`plugintypestatistic`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_plugintypestatistic`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_position"></a> organization_position

Many-To-One Relationship: [position organization_position](position.md#BKMK_organization_position)

|Property|Value|
|---|---|
|ReferencingEntity|`position`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_position`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_post"></a> organization_post

Many-To-One Relationship: [post organization_post](post.md#BKMK_organization_post)

|Property|Value|
|---|---|
|ReferencingEntity|`post`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_post`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_PostComment"></a> organization_PostComment

Many-To-One Relationship: [postcomment organization_PostComment](postcomment.md#BKMK_organization_PostComment)

|Property|Value|
|---|---|
|ReferencingEntity|`postcomment`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_PostComment`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_postlike"></a> organization_postlike

Many-To-One Relationship: [postlike organization_postlike](postlike.md#BKMK_organization_postlike)

|Property|Value|
|---|---|
|ReferencingEntity|`postlike`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_postlike`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_privilegesremovalsetting"></a> organization_privilegesremovalsetting

Many-To-One Relationship: [privilegesremovalsetting organization_privilegesremovalsetting](privilegesremovalsetting.md#BKMK_organization_privilegesremovalsetting)

|Property|Value|
|---|---|
|ReferencingEntity|`privilegesremovalsetting`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_privilegesremovalsetting`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_publisher"></a> organization_publisher

Many-To-One Relationship: [publisher organization_publisher](publisher.md#BKMK_organization_publisher)

|Property|Value|
|---|---|
|ReferencingEntity|`publisher`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_publisher`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_queueitems"></a> organization_queueitems

Many-To-One Relationship: [queueitem organization_queueitems](queueitem.md#BKMK_organization_queueitems)

|Property|Value|
|---|---|
|ReferencingEntity|`queueitem`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_queueitems`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_queues"></a> organization_queues

Many-To-One Relationship: [queue organization_queues](queue.md#BKMK_organization_queues)

|Property|Value|
|---|---|
|ReferencingEntity|`queue`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_queues`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_recommendeddocument"></a> organization_recommendeddocument

Many-To-One Relationship: [recommendeddocument organization_recommendeddocument](recommendeddocument.md#BKMK_organization_recommendeddocument)

|Property|Value|
|---|---|
|ReferencingEntity|`recommendeddocument`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_recommendeddocument`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_recordfilter"></a> organization_recordfilter

Many-To-One Relationship: [recordfilter organization_recordfilter](recordfilter.md#BKMK_organization_recordfilter)

|Property|Value|
|---|---|
|ReferencingEntity|`recordfilter`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_recordfilter`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_recyclebinconfig"></a> organization_recyclebinconfig

Many-To-One Relationship: [recyclebinconfig organization_recyclebinconfig](recyclebinconfig.md#BKMK_organization_recyclebinconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`recyclebinconfig`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_recyclebinconfig`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_relationshipattribute"></a> organization_relationshipattribute

Many-To-One Relationship: [relationshipattribute organization_relationshipattribute](relationshipattribute.md#BKMK_organization_relationshipattribute)

|Property|Value|
|---|---|
|ReferencingEntity|`relationshipattribute`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_relationshipattribute`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_retentionoperationdetail"></a> organization_retentionoperationdetail

Many-To-One Relationship: [retentionoperationdetail organization_retentionoperationdetail](retentionoperationdetail.md#BKMK_organization_retentionoperationdetail)

|Property|Value|
|---|---|
|ReferencingEntity|`retentionoperationdetail`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_retentionoperationdetail`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_roleeditorlayout"></a> organization_roleeditorlayout

Many-To-One Relationship: [roleeditorlayout organization_roleeditorlayout](roleeditorlayout.md#BKMK_organization_roleeditorlayout)

|Property|Value|
|---|---|
|ReferencingEntity|`roleeditorlayout`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_roleeditorlayout`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_roles"></a> organization_roles

Many-To-One Relationship: [role organization_roles](role.md#BKMK_organization_roles)

|Property|Value|
|---|---|
|ReferencingEntity|`role`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_roles`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_sa_suggestedaction"></a> organization_sa_suggestedaction

Many-To-One Relationship: [sa_suggestedaction organization_sa_suggestedaction](sa_suggestedaction.md#BKMK_organization_sa_suggestedaction)

|Property|Value|
|---|---|
|ReferencingEntity|`sa_suggestedaction`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_sa_suggestedaction`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_sa_suggestedactioncriteria"></a> organization_sa_suggestedactioncriteria

Many-To-One Relationship: [sa_suggestedactioncriteria organization_sa_suggestedactioncriteria](sa_suggestedactioncriteria.md#BKMK_organization_sa_suggestedactioncriteria)

|Property|Value|
|---|---|
|ReferencingEntity|`sa_suggestedactioncriteria`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_sa_suggestedactioncriteria`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_saved_queries"></a> organization_saved_queries

Many-To-One Relationship: [savedquery organization_saved_queries](savedquery.md#BKMK_organization_saved_queries)

|Property|Value|
|---|---|
|ReferencingEntity|`savedquery`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_saved_queries`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_saved_query_visualizations"></a> organization_saved_query_visualizations

Many-To-One Relationship: [savedqueryvisualization organization_saved_query_visualizations](savedqueryvisualization.md#BKMK_organization_saved_query_visualizations)

|Property|Value|
|---|---|
|ReferencingEntity|`savedqueryvisualization`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_saved_query_visualizations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_sdkmessage"></a> organization_sdkmessage

Many-To-One Relationship: [sdkmessage organization_sdkmessage](sdkmessage.md#BKMK_organization_sdkmessage)

|Property|Value|
|---|---|
|ReferencingEntity|`sdkmessage`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_sdkmessage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_sdkmessagefilter"></a> organization_sdkmessagefilter

Many-To-One Relationship: [sdkmessagefilter organization_sdkmessagefilter](sdkmessagefilter.md#BKMK_organization_sdkmessagefilter)

|Property|Value|
|---|---|
|ReferencingEntity|`sdkmessagefilter`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_sdkmessagefilter`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_sdkmessageprocessingstep"></a> organization_sdkmessageprocessingstep

Many-To-One Relationship: [sdkmessageprocessingstep organization_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_organization_sdkmessageprocessingstep)

|Property|Value|
|---|---|
|ReferencingEntity|`sdkmessageprocessingstep`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_sdkmessageprocessingstep`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_sdkmessageprocessingstepimage"></a> organization_sdkmessageprocessingstepimage

Many-To-One Relationship: [sdkmessageprocessingstepimage organization_sdkmessageprocessingstepimage](sdkmessageprocessingstepimage.md#BKMK_organization_sdkmessageprocessingstepimage)

|Property|Value|
|---|---|
|ReferencingEntity|`sdkmessageprocessingstepimage`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_sdkmessageprocessingstepimage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_sdkmessageprocessingstepsecureconfig"></a> organization_sdkmessageprocessingstepsecureconfig

Many-To-One Relationship: [sdkmessageprocessingstepsecureconfig organization_sdkmessageprocessingstepsecureconfig](sdkmessageprocessingstepsecureconfig.md#BKMK_organization_sdkmessageprocessingstepsecureconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`sdkmessageprocessingstepsecureconfig`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_sdkmessageprocessingstepsecureconfig`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_searchattributesettings"></a> organization_searchattributesettings

Many-To-One Relationship: [searchattributesettings organization_searchattributesettings](searchattributesettings.md#BKMK_organization_searchattributesettings)

|Property|Value|
|---|---|
|ReferencingEntity|`searchattributesettings`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_searchattributesettings`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_searchcustomanalyzer"></a> organization_searchcustomanalyzer

Many-To-One Relationship: [searchcustomanalyzer organization_searchcustomanalyzer](searchcustomanalyzer.md#BKMK_organization_searchcustomanalyzer)

|Property|Value|
|---|---|
|ReferencingEntity|`searchcustomanalyzer`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_searchcustomanalyzer`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_searchrelationshipsettings"></a> organization_searchrelationshipsettings

Many-To-One Relationship: [searchrelationshipsettings organization_searchrelationshipsettings](searchrelationshipsettings.md#BKMK_organization_searchrelationshipsettings)

|Property|Value|
|---|---|
|ReferencingEntity|`searchrelationshipsettings`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_searchrelationshipsettings`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_serviceendpoint"></a> organization_serviceendpoint

Many-To-One Relationship: [serviceendpoint organization_serviceendpoint](serviceendpoint.md#BKMK_organization_serviceendpoint)

|Property|Value|
|---|---|
|ReferencingEntity|`serviceendpoint`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_serviceendpoint`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_sharedlinksetting"></a> organization_sharedlinksetting

Many-To-One Relationship: [sharedlinksetting organization_sharedlinksetting](sharedlinksetting.md#BKMK_organization_sharedlinksetting)

|Property|Value|
|---|---|
|ReferencingEntity|`sharedlinksetting`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_sharedlinksetting`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_sharepointmanagedidentity"></a> organization_sharepointmanagedidentity

Many-To-One Relationship: [sharepointmanagedidentity organization_sharepointmanagedidentity](sharepointmanagedidentity.md#BKMK_organization_sharepointmanagedidentity)

|Property|Value|
|---|---|
|ReferencingEntity|`sharepointmanagedidentity`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_sharepointmanagedidentity`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_similarityrule"></a> organization_similarityrule

Many-To-One Relationship: [similarityrule organization_similarityrule](similarityrule.md#BKMK_organization_similarityrule)

|Property|Value|
|---|---|
|ReferencingEntity|`similarityrule`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_similarityrule`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_sitemap"></a> organization_sitemap

Many-To-One Relationship: [sitemap organization_sitemap](sitemap.md#BKMK_organization_sitemap)

|Property|Value|
|---|---|
|ReferencingEntity|`sitemap`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_sitemap`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_solution"></a> organization_solution

Many-To-One Relationship: [solution organization_solution](solution.md#BKMK_organization_solution)

|Property|Value|
|---|---|
|ReferencingEntity|`solution`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_solution`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_solutioncomponentattributeconfiguration"></a> organization_solutioncomponentattributeconfiguration

Many-To-One Relationship: [solutioncomponentattributeconfiguration organization_solutioncomponentattributeconfiguration](solutioncomponentattributeconfiguration.md#BKMK_organization_solutioncomponentattributeconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`solutioncomponentattributeconfiguration`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_solutioncomponentattributeconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_solutioncomponentconfiguration"></a> organization_solutioncomponentconfiguration

Many-To-One Relationship: [solutioncomponentconfiguration organization_solutioncomponentconfiguration](solutioncomponentconfiguration.md#BKMK_organization_solutioncomponentconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`solutioncomponentconfiguration`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_solutioncomponentconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_solutioncomponentrelationshipconfiguration"></a> organization_solutioncomponentrelationshipconfiguration

Many-To-One Relationship: [solutioncomponentrelationshipconfiguration organization_solutioncomponentrelationshipconfiguration](solutioncomponentrelationshipconfiguration.md#BKMK_organization_solutioncomponentrelationshipconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`solutioncomponentrelationshipconfiguration`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_solutioncomponentrelationshipconfiguration`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_subjects"></a> organization_subjects

Many-To-One Relationship: [subject organization_subjects](subject.md#BKMK_organization_subjects)

|Property|Value|
|---|---|
|ReferencingEntity|`subject`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_subjects`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_supportusertable"></a> organization_supportusertable

Many-To-One Relationship: [supportusertable organization_supportusertable](supportusertable.md#BKMK_organization_supportusertable)

|Property|Value|
|---|---|
|ReferencingEntity|`supportusertable`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_supportusertable`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_synapselinkexternaltablestate"></a> organization_synapselinkexternaltablestate

Many-To-One Relationship: [synapselinkexternaltablestate organization_synapselinkexternaltablestate](synapselinkexternaltablestate.md#BKMK_organization_synapselinkexternaltablestate)

|Property|Value|
|---|---|
|ReferencingEntity|`synapselinkexternaltablestate`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_synapselinkexternaltablestate`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_synapselinkprofile"></a> organization_synapselinkprofile

Many-To-One Relationship: [synapselinkprofile organization_synapselinkprofile](synapselinkprofile.md#BKMK_organization_synapselinkprofile)

|Property|Value|
|---|---|
|ReferencingEntity|`synapselinkprofile`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_synapselinkprofile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_synapselinkprofileentity"></a> organization_synapselinkprofileentity

Many-To-One Relationship: [synapselinkprofileentity organization_synapselinkprofileentity](synapselinkprofileentity.md#BKMK_organization_synapselinkprofileentity)

|Property|Value|
|---|---|
|ReferencingEntity|`synapselinkprofileentity`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_synapselinkprofileentity`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_synapselinkprofileentitystate"></a> organization_synapselinkprofileentitystate

Many-To-One Relationship: [synapselinkprofileentitystate organization_synapselinkprofileentitystate](synapselinkprofileentitystate.md#BKMK_organization_synapselinkprofileentitystate)

|Property|Value|
|---|---|
|ReferencingEntity|`synapselinkprofileentitystate`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_synapselinkprofileentitystate`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_synapselinkschedule"></a> organization_synapselinkschedule

Many-To-One Relationship: [synapselinkschedule organization_synapselinkschedule](synapselinkschedule.md#BKMK_organization_synapselinkschedule)

|Property|Value|
|---|---|
|ReferencingEntity|`synapselinkschedule`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_synapselinkschedule`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Organization_SyncErrors"></a> Organization_SyncErrors

Many-To-One Relationship: [syncerror Organization_SyncErrors](syncerror.md#BKMK_Organization_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Organization_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_system_users"></a> organization_system_users

Many-To-One Relationship: [systemuser organization_system_users](systemuser.md#BKMK_organization_system_users)

|Property|Value|
|---|---|
|ReferencingEntity|`systemuser`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_system_users`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_systemforms"></a> organization_systemforms

Many-To-One Relationship: [systemform organization_systemforms](systemform.md#BKMK_organization_systemforms)

|Property|Value|
|---|---|
|ReferencingEntity|`systemform`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_systemforms`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_teammobileofflineprofilemembership"></a> organization_teammobileofflineprofilemembership

Many-To-One Relationship: [teammobileofflineprofilemembership organization_teammobileofflineprofilemembership](teammobileofflineprofilemembership.md#BKMK_organization_teammobileofflineprofilemembership)

|Property|Value|
|---|---|
|ReferencingEntity|`teammobileofflineprofilemembership`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_teammobileofflineprofilemembership`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_teams"></a> organization_teams

Many-To-One Relationship: [team organization_teams](team.md#BKMK_organization_teams)

|Property|Value|
|---|---|
|ReferencingEntity|`team`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_teams`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_territories"></a> organization_territories

Many-To-One Relationship: [territory organization_territories](territory.md#BKMK_organization_territories)

|Property|Value|
|---|---|
|ReferencingEntity|`territory`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_territories`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_textanalyticsentitymapping"></a> organization_textanalyticsentitymapping

Many-To-One Relationship: [textanalyticsentitymapping organization_textanalyticsentitymapping](textanalyticsentitymapping.md#BKMK_organization_textanalyticsentitymapping)

|Property|Value|
|---|---|
|ReferencingEntity|`textanalyticsentitymapping`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_textanalyticsentitymapping`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_theme"></a> organization_theme

Many-To-One Relationship: [theme organization_theme](theme.md#BKMK_organization_theme)

|Property|Value|
|---|---|
|ReferencingEntity|`theme`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_theme`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_tracelog"></a> organization_tracelog

Many-To-One Relationship: [tracelog organization_tracelog](tracelog.md#BKMK_organization_tracelog)

|Property|Value|
|---|---|
|ReferencingEntity|`tracelog`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_tracelog`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_transactioncurrencies"></a> organization_transactioncurrencies

Many-To-One Relationship: [transactioncurrency organization_transactioncurrencies](transactioncurrency.md#BKMK_organization_transactioncurrencies)

|Property|Value|
|---|---|
|ReferencingEntity|`transactioncurrency`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_transactioncurrencies`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_translationprocess"></a> organization_translationprocess

Many-To-One Relationship: [translationprocess organization_translationprocess](translationprocess.md#BKMK_organization_translationprocess)

|Property|Value|
|---|---|
|ReferencingEntity|`translationprocess`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_translationprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_UserMapping"></a> organization_UserMapping

Many-To-One Relationship: [usermapping organization_UserMapping](usermapping.md#BKMK_organization_UserMapping)

|Property|Value|
|---|---|
|ReferencingEntity|`usermapping`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_UserMapping`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_usermobileofflineprofilemembership"></a> organization_usermobileofflineprofilemembership

Many-To-One Relationship: [usermobileofflineprofilemembership organization_usermobileofflineprofilemembership](usermobileofflineprofilemembership.md#BKMK_organization_usermobileofflineprofilemembership)

|Property|Value|
|---|---|
|ReferencingEntity|`usermobileofflineprofilemembership`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_usermobileofflineprofilemembership`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_userrating"></a> organization_userrating

Many-To-One Relationship: [userrating organization_userrating](userrating.md#BKMK_organization_userrating)

|Property|Value|
|---|---|
|ReferencingEntity|`userrating`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_userrating`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_viewasexamplequestion"></a> organization_viewasexamplequestion

Many-To-One Relationship: [viewasexamplequestion organization_viewasexamplequestion](viewasexamplequestion.md#BKMK_organization_viewasexamplequestion)

|Property|Value|
|---|---|
|ReferencingEntity|`viewasexamplequestion`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_viewasexamplequestion`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_virtualentitymetadata"></a> organization_virtualentitymetadata

Many-To-One Relationship: [virtualentitymetadata organization_virtualentitymetadata](virtualentitymetadata.md#BKMK_organization_virtualentitymetadata)

|Property|Value|
|---|---|
|ReferencingEntity|`virtualentitymetadata`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_virtualentitymetadata`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organization_webwizard"></a> organization_webwizard

Many-To-One Relationship: [webwizard organization_webwizard](webwizard.md#BKMK_organization_webwizard)

|Property|Value|
|---|---|
|ReferencingEntity|`webwizard`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`organization_webwizard`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_webresource_organization"></a> webresource_organization

Many-To-One Relationship: [webresource webresource_organization](webresource.md#BKMK_webresource_organization)

|Property|Value|
|---|---|
|ReferencingEntity|`webresource`|
|ReferencingAttribute|`organizationid`|
|ReferencedEntityNavigationPropertyName|`webresource_organization`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.organization?displayProperty=fullName>
