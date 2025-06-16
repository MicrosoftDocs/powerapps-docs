---
title: "Mailbox table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Mailbox table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Mailbox table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Mailbox table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: False |`PATCH` /mailboxes(*mailboxid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mailboxes<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /mailboxes(*mailboxid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `ModifyAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: False |`GET` /mailboxes(*mailboxid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /mailboxes<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: False |`PATCH` /mailboxes(*mailboxid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /mailboxes(*mailboxid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /mailboxes(*mailboxid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Mailbox table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Mailbox** |
| **DisplayCollectionName** | **Mailboxes** |
| **SchemaName** | `Mailbox` |
| **CollectionSchemaName** | `Mailboxes` |
| **EntitySetName** | `mailboxes`|
| **LogicalName** | `mailbox` |
| **LogicalCollectionName** | `mailboxes` |
| **PrimaryIdAttribute** | `mailboxid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ACSEnabledForOutgoingEmail](#BKMK_ACSEnabledForOutgoingEmail)
- [ACSMailFromCreated](#BKMK_ACSMailFromCreated)
- [ACSOutgoingEmailStatus](#BKMK_ACSOutgoingEmailStatus)
- [ACTDeliveryMethod](#BKMK_ACTDeliveryMethod)
- [ACTStatus](#BKMK_ACTStatus)
- [AllowEmailConnectorToUseCredentials](#BKMK_AllowEmailConnectorToUseCredentials)
- [EmailAddress](#BKMK_EmailAddress)
- [EmailRouterAccessApproval](#BKMK_EmailRouterAccessApproval)
- [EmailServerProfile](#BKMK_EmailServerProfile)
- [EnabledForACT](#BKMK_EnabledForACT)
- [EnabledForIncomingEmail](#BKMK_EnabledForIncomingEmail)
- [EnabledForOutgoingEmail](#BKMK_EnabledForOutgoingEmail)
- [EntityImage](#BKMK_EntityImage)
- [EWSURL](#BKMK_EWSURL)
- [ExchangeContactsImportStatus](#BKMK_ExchangeContactsImportStatus)
- [ExchangeSyncStateXml](#BKMK_ExchangeSyncStateXml)
- [FolderHierarchy](#BKMK_FolderHierarchy)
- [IncomingEmailDeliveryMethod](#BKMK_IncomingEmailDeliveryMethod)
- [IncomingEmailStatus](#BKMK_IncomingEmailStatus)
- [IsACTSyncOrgFlagSet](#BKMK_IsACTSyncOrgFlagSet)
- [IsEmailAddressApprovedByO365Admin](#BKMK_IsEmailAddressApprovedByO365Admin)
- [ItemsFailedForLastSync](#BKMK_ItemsFailedForLastSync)
- [ItemsProcessedForLastSync](#BKMK_ItemsProcessedForLastSync)
- [LastAutoDiscoveredOn](#BKMK_LastAutoDiscoveredOn)
- [LastIncomingEmailsRequestedFromEmailServerOn](#BKMK_LastIncomingEmailsRequestedFromEmailServerOn)
- [LastMessageId](#BKMK_LastMessageId)
- [LastSuccessfulSyncCompletedOn](#BKMK_LastSuccessfulSyncCompletedOn)
- [LastSyncError](#BKMK_LastSyncError)
- [LastSyncErrorCode](#BKMK_LastSyncErrorCode)
- [LastSyncErrorCount](#BKMK_LastSyncErrorCount)
- [LastSyncErrorMachineName](#BKMK_LastSyncErrorMachineName)
- [LastSyncErrorOccurredOn](#BKMK_LastSyncErrorOccurredOn)
- [LastTagCompletedOn](#BKMK_LastTagCompletedOn)
- [LastTaggedMessageId](#BKMK_LastTaggedMessageId)
- [LastTagProcessedMaxItems](#BKMK_LastTagProcessedMaxItems)
- [MailboxId](#BKMK_MailboxId)
- [MailboxProcessingContext](#BKMK_MailboxProcessingContext)
- [Name](#BKMK_Name)
- [OauthAccessToken](#BKMK_OauthAccessToken)
- [OauthRefreshToken](#BKMK_OauthRefreshToken)
- [OauthTokenExpiresOn](#BKMK_OauthTokenExpiresOn)
- [OfficeAppsDeploymentScheduled](#BKMK_OfficeAppsDeploymentScheduled)
- [OfficeAppsDeploymentStatus](#BKMK_OfficeAppsDeploymentStatus)
- [OrgMarkedAsPrimaryForExchangeSync](#BKMK_OrgMarkedAsPrimaryForExchangeSync)
- [OutgoingEmailDeliveryMethod](#BKMK_OutgoingEmailDeliveryMethod)
- [OutgoingEmailStatus](#BKMK_OutgoingEmailStatus)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [Password](#BKMK_Password)
- [PostponeMailboxProcessingUntil](#BKMK_PostponeMailboxProcessingUntil)
- [PostponeOfficeAppsDeploymentUntil](#BKMK_PostponeOfficeAppsDeploymentUntil)
- [PostponeSendingUntil](#BKMK_PostponeSendingUntil)
- [PostponeTestEmailConfigurationUntil](#BKMK_PostponeTestEmailConfigurationUntil)
- [ProcessAndDeleteEmails](#BKMK_ProcessAndDeleteEmails)
- [ProcessEmailReceivedAfter](#BKMK_ProcessEmailReceivedAfter)
- [ProcessingLastAttemptedOn](#BKMK_ProcessingLastAttemptedOn)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [TagEmailsAfter](#BKMK_TagEmailsAfter)
- [TestEmailConfigurationRetryCount](#BKMK_TestEmailConfigurationRetryCount)
- [TestEmailConfigurationScheduled](#BKMK_TestEmailConfigurationScheduled)
- [TestMailboxAccessCompletedOn](#BKMK_TestMailboxAccessCompletedOn)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UndeliverableFolder](#BKMK_UndeliverableFolder)
- [Username](#BKMK_Username)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [VerboseLoggingEnabled](#BKMK_VerboseLoggingEnabled)

### <a name="BKMK_ACSEnabledForOutgoingEmail"></a> ACSEnabledForOutgoingEmail

|Property|Value|
|---|---|
|Description|**Determines if ACS integration should be enabled for outgoing email synchronization.**|
|DisplayName|**ACS Enabled for Outgoing Email**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`acsenabledforoutgoingemail`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mailbox_acsenabledforoutgoingemail`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ACSMailFromCreated"></a> ACSMailFromCreated

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**ACS MailFrom Created**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`acsmailfromcreated`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mailbox_acsmailfromcreated`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ACSOutgoingEmailStatus"></a> ACSOutgoingEmailStatus

|Property|Value|
|---|---|
|Description|**The status of ACS outgoing email synchronization.**|
|DisplayName|**ACS Outgoing Email Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`acsoutgoingemailstatus`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`mailbox_acsoutgoingemailstatus`|

#### ACSOutgoingEmailStatus Choices/Options

|Value|Label|
|---|---|
|0|**Not Run**|
|1|**Success**|
|2|**Failure**|

### <a name="BKMK_ACTDeliveryMethod"></a> ACTDeliveryMethod

|Property|Value|
|---|---|
|Description|**Choose the delivery method for the mailbox for appointments, contacts, and tasks.**|
|DisplayName|**Appointments, Contacts, and Tasks**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`actdeliverymethod`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`mailbox_actdeliverymethod`|

#### ACTDeliveryMethod Choices/Options

|Value|Label|
|---|---|
|0|**Microsoft Dynamics 365 for Outlook**|
|1|**Server-Side Synchronization**|
|2|**None**|

### <a name="BKMK_ACTStatus"></a> ACTStatus

|Property|Value|
|---|---|
|Description|**Status of the Appointments, Contacts, and Tasks.**|
|DisplayName|**Appointments, Contacts, and Tasks Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`actstatus`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`mailbox_actstatus`|

#### ACTStatus Choices/Options

|Value|Label|
|---|---|
|0|**Not Run**|
|1|**Success**|
|2|**Failure**|

### <a name="BKMK_AllowEmailConnectorToUseCredentials"></a> AllowEmailConnectorToUseCredentials

|Property|Value|
|---|---|
|Description|**Choose whether to allow the email connector to use credentials.**|
|DisplayName|**Allow to Use Credentials for Email Processing**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`allowemailconnectortousecredentials`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mailbox_allowemailconnectortousecredentials`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EmailAddress"></a> EmailAddress

|Property|Value|
|---|---|
|Description|**Type the email address of the mailbox.**|
|DisplayName|**Email Address**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`emailaddress`|
|RequiredLevel|None|
|Type|String|
|Format|Email|
|FormatName|Email|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_EmailRouterAccessApproval"></a> EmailRouterAccessApproval

|Property|Value|
|---|---|
|Description|**Shows the status of the email address.**|
|DisplayName|**Email Address Status**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`emailrouteraccessapproval`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`mailbox_emailrouteraccessapproval`|

#### EmailRouterAccessApproval Choices/Options

|Value|Label|
|---|---|
|0|**Empty**|
|1|**Approved**|
|2|**Pending Approval**|
|3|**Rejected**|

### <a name="BKMK_EmailServerProfile"></a> EmailServerProfile

|Property|Value|
|---|---|
|Description|**Select the email server profile of the mailbox.**|
|DisplayName|**Server Profile**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`emailserverprofile`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|emailserverprofile|

### <a name="BKMK_EnabledForACT"></a> EnabledForACT

|Property|Value|
|---|---|
|Description|**Indicates whether the mailbox is enabled for Appointments, Contacts, and Tasks.**|
|DisplayName|**Enabled For Appointments, Contacts, And Tasks**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`enabledforact`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`mailbox_enabledforact`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnabledForIncomingEmail"></a> EnabledForIncomingEmail

|Property|Value|
|---|---|
|Description|**Choose whether the mailbox is enabled for receiving email.**|
|DisplayName|**Enabled For Incoming Email**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`enabledforincomingemail`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`mailbox_enabledforincomingemail`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EnabledForOutgoingEmail"></a> EnabledForOutgoingEmail

|Property|Value|
|---|---|
|Description|**Choose whether the mailbox is enabled for sending email.**|
|DisplayName|**Enabled For Outgoing Email**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`enabledforoutgoingemail`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`mailbox_enabledforoutgoingemail`|
|DefaultValue|True|
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

### <a name="BKMK_EWSURL"></a> EWSURL

|Property|Value|
|---|---|
|Description|**Exchange web services endpoint URL for the mailbox.**|
|DisplayName|**Exchange Web Services URL**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ewsurl`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2084|

### <a name="BKMK_ExchangeContactsImportStatus"></a> ExchangeContactsImportStatus

|Property|Value|
|---|---|
|Description|**Indicates the exchange contacts import status for a mailbox record.**|
|DisplayName|**Exchange Contacts Import Status**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`exchangecontactsimportstatus`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`mailbox_exchangecontactsimportstatus`|

#### ExchangeContactsImportStatus Choices/Options

|Value|Label|
|---|---|
|0|**NotImported**|
|1|**Imported**|
|2|**ImportFailed**|

### <a name="BKMK_ExchangeSyncStateXml"></a> ExchangeSyncStateXml

|Property|Value|
|---|---|
|Description|**Contains the exchange synchronization state in XML format.**|
|DisplayName|**Exchange Sync State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`exchangesyncstatexml`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_FolderHierarchy"></a> FolderHierarchy

|Property|Value|
|---|---|
|Description|**Holds the hierarchy of folders under inbox in XML format.**|
|DisplayName|**Folder Hierarchy**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`folderhierarchy`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_IncomingEmailDeliveryMethod"></a> IncomingEmailDeliveryMethod

|Property|Value|
|---|---|
|Description|**Select how incoming email will be delivered to the mailbox.**|
|DisplayName|**Incoming Email**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`incomingemaildeliverymethod`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`mailbox_incomingemaildeliverymethod`|

#### IncomingEmailDeliveryMethod Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Microsoft Dynamics 365 for Outlook**|
|2|**Server-Side Synchronization**|
|3|**Forward Mailbox**|

### <a name="BKMK_IncomingEmailStatus"></a> IncomingEmailStatus

|Property|Value|
|---|---|
|Description|**Select the status that will be assigned to incoming email messages.**|
|DisplayName|**Incoming Email Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`incomingemailstatus`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`mailbox_incomingemailstatus`|

#### IncomingEmailStatus Choices/Options

|Value|Label|
|---|---|
|0|**Not Run**|
|1|**Success**|
|2|**Failure**|

### <a name="BKMK_IsACTSyncOrgFlagSet"></a> IsACTSyncOrgFlagSet

|Property|Value|
|---|---|
|Description|**Set the current organization as the synchronization organization.**|
|DisplayName|**Set Current Organization as Synchronization Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isactsyncorgflagset`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mailbox_isactsyncorgflagset`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsEmailAddressApprovedByO365Admin"></a> IsEmailAddressApprovedByO365Admin

|Property|Value|
|---|---|
|Description|**Shows the status of approval of the email address by O365 Admin.**|
|DisplayName|**Email Address O365 Admin Approval Status**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isemailaddressapprovedbyo365admin`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`mailbox_isemailaddressapprovedbyo365admin`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ItemsFailedForLastSync"></a> ItemsFailedForLastSync

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Items Failed For Last Sync**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`itemsfailedforlastsync`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ItemsProcessedForLastSync"></a> ItemsProcessedForLastSync

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Items Processed For Last Sync**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`itemsprocessedforlastsync`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_LastAutoDiscoveredOn"></a> LastAutoDiscoveredOn

|Property|Value|
|---|---|
|Description|**Shows the date and time when the Exchange web services URL was last discovered using the AutoDiscover service.**|
|DisplayName|**Last Auto Discovered On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastautodiscoveredon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_LastIncomingEmailsRequestedFromEmailServerOn"></a> LastIncomingEmailsRequestedFromEmailServerOn

|Property|Value|
|---|---|
|Description|**The timestamp when last set of incoming emails were requested from external email server. For internal use only.**|
|DisplayName|**Last Incoming Emails Requested From Email Server On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastincomingemailsrequestedfromemailserveron`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_LastMessageId"></a> LastMessageId

|Property|Value|
|---|---|
|Description|**Unique identifier of the last message.**|
|DisplayName|**Last Message ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastmessageid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|320|

### <a name="BKMK_LastSuccessfulSyncCompletedOn"></a> LastSuccessfulSyncCompletedOn

|Property|Value|
|---|---|
|Description|**Last Successful Sync Time**|
|DisplayName|**Last Successful Sync Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastsuccessfulsynccompletedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_LastSyncError"></a> LastSyncError

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Last Sync Error Stack**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastsyncerror`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2048|

### <a name="BKMK_LastSyncErrorCode"></a> LastSyncErrorCode

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Last Sync Error Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastsyncerrorcode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_LastSyncErrorCount"></a> LastSyncErrorCount

|Property|Value|
|---|---|
|Description|**For internal use only**|
|DisplayName|**Last Sync Error Continuous Count**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastsyncerrorcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_LastSyncErrorMachineName"></a> LastSyncErrorMachineName

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Last Sync Error Machine Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastsyncerrormachinename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|320|

### <a name="BKMK_LastSyncErrorOccurredOn"></a> LastSyncErrorOccurredOn

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Last Sync Error Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastsyncerroroccurredon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_LastTagCompletedOn"></a> LastTagCompletedOn

|Property|Value|
|---|---|
|Description|**Identifies the timestamp when tagging last completed. For internal use only.**|
|DisplayName|**Last Tag Completed On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lasttagcompletedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_LastTaggedMessageId"></a> LastTaggedMessageId

|Property|Value|
|---|---|
|Description|**Identifies the last MessageId that has been processed for tagging in the remote system.**|
|DisplayName|**Last Tagged MessageId**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lasttaggedmessageid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|320|

### <a name="BKMK_LastTagProcessedMaxItems"></a> LastTagProcessedMaxItems

|Property|Value|
|---|---|
|Description|**Indicates if the last tagging cycle processed the maximum number of items. For internal use only.**|
|DisplayName|**Last Tag Processed Max Items**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lasttagprocessedmaxitems`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mailbox_lasttagprocessedmaxitems`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_MailboxId"></a> MailboxId

|Property|Value|
|---|---|
|Description|**Unique identifier of the mailbox.**|
|DisplayName|**Mailbox**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mailboxid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_MailboxProcessingContext"></a> MailboxProcessingContext

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Processing Context of the Mailbox**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mailboxprocessingcontext`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Type the name of the mailbox.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_OauthAccessToken"></a> OauthAccessToken

|Property|Value|
|---|---|
|Description|**Type the Oauth access token for the mailbox.**|
|DisplayName|**Oauth access token**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`oauthaccesstoken`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_OauthRefreshToken"></a> OauthRefreshToken

|Property|Value|
|---|---|
|Description|**Type the Oauth refresh token for the mailbox.**|
|DisplayName|**Oauth refresh token**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`oauthrefreshtoken`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_OauthTokenExpiresOn"></a> OauthTokenExpiresOn

|Property|Value|
|---|---|
|Description|**Date and time when the Oauth token will expire**|
|DisplayName|**Oauth token expiration datetime**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`oauthtokenexpireson`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_OfficeAppsDeploymentScheduled"></a> OfficeAppsDeploymentScheduled

|Property|Value|
|---|---|
|Description|**Indicates if the office apps deployment has been scheduled for a mailbox record.**|
|DisplayName|**Office Apps Deployment Scheduled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`officeappsdeploymentscheduled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mailbox_officeappsdeploymentscheduled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_OfficeAppsDeploymentStatus"></a> OfficeAppsDeploymentStatus

|Property|Value|
|---|---|
|Description|**Indicates the office apps deployment type for a mailbox record.**|
|DisplayName|**Office Apps Deployment Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`officeappsdeploymentstatus`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`mailbox_officeappsdeploymentstatus`|

#### OfficeAppsDeploymentStatus Choices/Options

|Value|Label|
|---|---|
|0|**NotInstalled**|
|1|**Installed**|
|2|**InstallFailed**|
|3|**UninstallFailed**|
|4|**UpgradeRequired**|

### <a name="BKMK_OrgMarkedAsPrimaryForExchangeSync"></a> OrgMarkedAsPrimaryForExchangeSync

|Property|Value|
|---|---|
|Description|**Indicates if the crm org is to be marked as primary syncing org for the mailbox record.**|
|DisplayName|**Crm Org Marked as Primary Org for Exchange Mailbox**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`orgmarkedasprimaryforexchangesync`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mailbox_orgmarkedasprimaryforexchangesync`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_OutgoingEmailDeliveryMethod"></a> OutgoingEmailDeliveryMethod

|Property|Value|
|---|---|
|Description|**Select how outgoing email will be sent from the mailbox.**|
|DisplayName|**Outgoing Email**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`outgoingemaildeliverymethod`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`mailbox_outgoingemaildeliverymethod`|

#### OutgoingEmailDeliveryMethod Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Microsoft Dynamics 365 for Outlook**|
|2|**Server-Side Synchronization**|

### <a name="BKMK_OutgoingEmailStatus"></a> OutgoingEmailStatus

|Property|Value|
|---|---|
|Description|**Select the status of outgoing email messages.**|
|DisplayName|**Outgoing Email Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`outgoingemailstatus`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`mailbox_outgoingemailstatus`|

#### OutgoingEmailStatus Choices/Options

|Value|Label|
|---|---|
|0|**Not Run**|
|1|**Success**|
|2|**Failure**|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.**|
|DisplayName|**Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description|**Owner Id Type**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_Password"></a> Password

|Property|Value|
|---|---|
|Description|**Type the password for the mailbox.**|
|DisplayName|**Password**|
|IsValidForForm|True|
|IsValidForRead|False|
|LogicalName|`password`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_PostponeMailboxProcessingUntil"></a> PostponeMailboxProcessingUntil

|Property|Value|
|---|---|
|Description|**Shows the date and time when processing will begin on this mailbox.**|
|DisplayName|**Postpone Mailbox Processing Until**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`postponemailboxprocessinguntil`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_PostponeOfficeAppsDeploymentUntil"></a> PostponeOfficeAppsDeploymentUntil

|Property|Value|
|---|---|
|Description|**Shows the date and time when the next outlook mail app install will be run for a mailbox record.**|
|DisplayName|**Postpone Outlook Mail App Install Until**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`postponeofficeappsdeploymentuntil`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_PostponeSendingUntil"></a> PostponeSendingUntil

|Property|Value|
|---|---|
|Description|**Shows the date and time when the mailbox can start sending emails.**|
|DisplayName|**Postpone Sending Until**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`postponesendinguntil`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_PostponeTestEmailConfigurationUntil"></a> PostponeTestEmailConfigurationUntil

|Property|Value|
|---|---|
|Description|**Shows the date and time when the next email configuration test will be run for a mailbox record.**|
|DisplayName|**Postpone Test Email Configuration Until**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`postponetestemailconfigurationuntil`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ProcessAndDeleteEmails"></a> ProcessAndDeleteEmails

|Property|Value|
|---|---|
|Description|**Select whether to delete emails from the mailbox after processing.**|
|DisplayName|**Delete Emails after Processing**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`processanddeleteemails`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mailbox_processanddeleteemails`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ProcessEmailReceivedAfter"></a> ProcessEmailReceivedAfter

|Property|Value|
|---|---|
|Description|**Shows the date and time to start processing email received by the mailbox.**|
|DisplayName|**Process Email Received After**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`processemailreceivedafter`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ProcessingLastAttemptedOn"></a> ProcessingLastAttemptedOn

|Property|Value|
|---|---|
|Description|**Date and time when the processing of the mailbox was last attempted.**|
|DisplayName|**Date Processing Last Attempted**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`processinglastattemptedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Shows whether the mailbox is active or inactive.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`mailbox_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Select the mailbox's status.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|SystemRequired|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`mailbox_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_TagEmailsAfter"></a> TagEmailsAfter

|Property|Value|
|---|---|
|Description|**Identifies the timestamp after for which emails should be tagged in the remote system.**|
|DisplayName|**Tag Emails After**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`tagemailsafter`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_TestEmailConfigurationRetryCount"></a> TestEmailConfigurationRetryCount

|Property|Value|
|---|---|
|Description|**Shows the number of times an email configuration test has been performed.**|
|DisplayName|**Test Email Configuration Retry Count**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`testemailconfigurationretrycount`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_TestEmailConfigurationScheduled"></a> TestEmailConfigurationScheduled

|Property|Value|
|---|---|
|Description|**Indicates if the email configuration test has been scheduled for a mailbox record.**|
|DisplayName|**Test Email Configuration Scheduled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`testemailconfigurationscheduled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mailbox_testemailconfigurationscheduled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_TestMailboxAccessCompletedOn"></a> TestMailboxAccessCompletedOn

|Property|Value|
|---|---|
|Description|**Date and time when the last email configuration test was completed for a mailbox record.**|
|DisplayName|**Mailbox Test Completed On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`testmailboxaccesscompletedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

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

### <a name="BKMK_UndeliverableFolder"></a> UndeliverableFolder

|Property|Value|
|---|---|
|Description|**Shows the ID of the Undeliverable folder in the mailbox managed by Microsoft Exchange.**|
|DisplayName|**Undeliverable Folder**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`undeliverablefolder`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_Username"></a> Username

|Property|Value|
|---|---|
|Description|**Type a user name used for mailbox authentication.**|
|DisplayName|**User Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`username`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

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

### <a name="BKMK_VerboseLoggingEnabled"></a> VerboseLoggingEnabled

|Property|Value|
|---|---|
|Description|**Indicates if verbose tracing needs to be enabled for this mailbox.**|
|DisplayName|**Verbose Logging**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`verboseloggingenabled`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|100|
|MinValue|0|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [AverageTotalDuration](#BKMK_AverageTotalDuration)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [EmailAddressApprovedBy](#BKMK_EmailAddressApprovedBy)
- [EmailAddressApprovedOn](#BKMK_EmailAddressApprovedOn)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [ExchangeContactsImportCompletedOn](#BKMK_ExchangeContactsImportCompletedOn)
- [ExchangeSyncStateXmlFileRef](#BKMK_ExchangeSyncStateXmlFileRef)
- [ExchangeSyncStateXmlFileRef_Name](#BKMK_ExchangeSyncStateXmlFileRef_Name)
- [ForcedUnlockCount](#BKMK_ForcedUnlockCount)
- [HostId](#BKMK_HostId)
- [IsExchangeContactsImportScheduled](#BKMK_IsExchangeContactsImportScheduled)
- [IsForwardMailbox](#BKMK_IsForwardMailbox)
- [IsOauthAccessTokenSet](#BKMK_IsOauthAccessTokenSet)
- [IsOauthRefreshTokenSet](#BKMK_IsOauthRefreshTokenSet)
- [IsPasswordSet](#BKMK_IsPasswordSet)
- [IsServiceAccount](#BKMK_IsServiceAccount)
- [LastActiveOn](#BKMK_LastActiveOn)
- [LastDuration](#BKMK_LastDuration)
- [LastMailboxForcedUnlockOccurredOn](#BKMK_LastMailboxForcedUnlockOccurredOn)
- [LastSyncStartedOn](#BKMK_LastSyncStartedOn)
- [MailboxStatus](#BKMK_MailboxStatus)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [NextScheduledACTSyncInSeconds](#BKMK_NextScheduledACTSyncInSeconds)
- [NoACTCount](#BKMK_NoACTCount)
- [NoEmailCount](#BKMK_NoEmailCount)
- [OfficeAppsDeploymentCompleteOn](#BKMK_OfficeAppsDeploymentCompleteOn)
- [OfficeAppsDeploymentError](#BKMK_OfficeAppsDeploymentError)
- [OrganizationId](#BKMK_OrganizationId)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [ProcessedTimes](#BKMK_ProcessedTimes)
- [ProcessingStateCode](#BKMK_ProcessingStateCode)
- [ReceivingPostponedUntil](#BKMK_ReceivingPostponedUntil)
- [ReceivingPostponedUntilForACT](#BKMK_ReceivingPostponedUntilForACT)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [TestAndEnableLastAttemptedBy](#BKMK_TestAndEnableLastAttemptedBy)
- [TestAndEnableLastAttemptedOn](#BKMK_TestAndEnableLastAttemptedOn)
- [TransientFailureCount](#BKMK_TransientFailureCount)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_AverageTotalDuration"></a> AverageTotalDuration

|Property|Value|
|---|---|
|Description|**Mailbox Total Duration in Average**|
|DisplayName|**Monitor Total Performance**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`averagetotalduration`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Shows who created the record.**|
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
|Description|**Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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
|Description|**Shows who created the record on behalf of another user.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_EmailAddressApprovedBy"></a> EmailAddressApprovedBy

|Property|Value|
|---|---|
|Description|**The user who approved the email address for synchronization.**|
|DisplayName|**Email Address Approved By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`emailaddressapprovedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_EmailAddressApprovedOn"></a> EmailAddressApprovedOn

|Property|Value|
|---|---|
|Description|**Date and time the mailbox's email address was approved.**|
|DisplayName|**Email Address Approved On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`emailaddressapprovedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

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

### <a name="BKMK_ExchangeContactsImportCompletedOn"></a> ExchangeContactsImportCompletedOn

|Property|Value|
|---|---|
|Description|**Date and time when the exchange contacts import was last completed for a mailbox record.**|
|DisplayName|**Exchange Contacts Import Completed On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`exchangecontactsimportcompletedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_ExchangeSyncStateXmlFileRef"></a> ExchangeSyncStateXmlFileRef

|Property|Value|
|---|---|
|Description|**Reference to the ExchangeSyncStateXml file on Azure.**|
|DisplayName|**ExchangeSyncStateXml File Ref**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`exchangesyncstatexmlfileref`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|131072|

### <a name="BKMK_ExchangeSyncStateXmlFileRef_Name"></a> ExchangeSyncStateXmlFileRef_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`exchangesyncstatexmlfileref_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_ForcedUnlockCount"></a> ForcedUnlockCount

|Property|Value|
|---|---|
|Description|**For internal use only**|
|DisplayName|**Count of the number of times a mailbox gets forced unlocked**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`forcedunlockcount`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_HostId"></a> HostId

|Property|Value|
|---|---|
|Description|**Unique identifier of the async host that is processing this mailbox.**|
|DisplayName|**Host**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`hostid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_IsExchangeContactsImportScheduled"></a> IsExchangeContactsImportScheduled

|Property|Value|
|---|---|
|Description|**Is Exchange Contacts Import Scheduled.**|
|DisplayName|**Is Exchange Contacts Import Scheduled.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isexchangecontactsimportscheduled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`mailbox_isexchangecontactsimportscheduled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsForwardMailbox"></a> IsForwardMailbox

|Property|Value|
|---|---|
|Description|**Select whether the mailbox is a forward mailbox.**|
|DisplayName|**Is Forward Mailbox**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isforwardmailbox`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`mailbox_isforwardmailbox`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsOauthAccessTokenSet"></a> IsOauthAccessTokenSet

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isoauthaccesstokenset`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`isencryptedattributevalueset`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsOauthRefreshTokenSet"></a> IsOauthRefreshTokenSet

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isoauthrefreshtokenset`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`isencryptedattributevalueset`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsPasswordSet"></a> IsPasswordSet

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ispasswordset`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`isencryptedattributevalueset`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsServiceAccount"></a> IsServiceAccount

|Property|Value|
|---|---|
|Description|**Select whether the mailbox corresponds to one for the service account.**|
|DisplayName|**Is Service Account**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isserviceaccount`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`mailbox_isserviceaccount`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_LastActiveOn"></a> LastActiveOn

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Last Active On**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`lastactiveon`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_LastDuration"></a> LastDuration

|Property|Value|
|---|---|
|Description|**Last Duration for the mailbox**|
|DisplayName|**Monitor last duration Performance**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastduration`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_LastMailboxForcedUnlockOccurredOn"></a> LastMailboxForcedUnlockOccurredOn

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Last Date Time when a mailbox got forced unlocked**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastmailboxforcedunlockoccurredon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_LastSyncStartedOn"></a> LastSyncStartedOn

|Property|Value|
|---|---|
|Description|**Last Sync Start Time**|
|DisplayName|**Last Sync Start Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastsyncstartedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_MailboxStatus"></a> MailboxStatus

|Property|Value|
|---|---|
|Description|**Last Sync Status for Outgoing, Incoming and ACT as a whole.**|
|DisplayName|**Mailbox Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mailboxstatus`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`mailbox_status`|

#### MailboxStatus Choices/Options

|Value|Label|
|---|---|
|0|**Not Run**|
|1|**Success**|
|2|**Failure**|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Shows who last updated the record.**|
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
|Description|**Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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
|Description|**Shows who last updated the record on behalf of another user.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_NextScheduledACTSyncInSeconds"></a> NextScheduledACTSyncInSeconds

|Property|Value|
|---|---|
|Description|**The next scheduled ACT sync delay, in seconds, to apply to the mailbox.**|
|DisplayName|**Next Scheduled ACT Sync Delay In Seconds**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`nextscheduledactsyncinseconds`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_NoACTCount"></a> NoACTCount

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Zero appointment, contact, task count for mailbox**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`noactcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_NoEmailCount"></a> NoEmailCount

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Zero email count for mailbox**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`noemailcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_OfficeAppsDeploymentCompleteOn"></a> OfficeAppsDeploymentCompleteOn

|Property|Value|
|---|---|
|Description|**Date and time when the last office apps deployment was completed for a mailbox record.**|
|DisplayName|**Office Apps Deployment Completed On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`officeappsdeploymentcompleteon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_OfficeAppsDeploymentError"></a> OfficeAppsDeploymentError

|Property|Value|
|---|---|
|Description|**The Office Apps deployment error.**|
|DisplayName|**Office Apps Deployment Error**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`officeappsdeploymenterror`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2048|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization associated with the record.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description|**Name of the owner**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|---|---|
|Description|**Yomi name of the owner**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridyominame`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Select the business unit that owns the record.**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|---|---|
|Description|**Unique identifier for the team that owns the record.**|
|DisplayName|**Owning Team**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningteam`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|team|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier for the user that owns the record.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ProcessedTimes"></a> ProcessedTimes

|Property|Value|
|---|---|
|Description|**The number of times mailbox has processed**|
|DisplayName|**Monitor Performance**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processedtimes`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_ProcessingStateCode"></a> ProcessingStateCode

|Property|Value|
|---|---|
|Description|**Information that indicates whether email will be processed for this mailbox**|
|DisplayName|**Mailbox Processing State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processingstatecode`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ReceivingPostponedUntil"></a> ReceivingPostponedUntil

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Postpone receiving emails for the mailbox until the specified data and time.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`receivingpostponeduntil`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ReceivingPostponedUntilForACT"></a> ReceivingPostponedUntilForACT

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Postpone processing Appointments, Contacts, and Tasks for the mailbox until the specified data and time.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`receivingpostponeduntilforact`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**Choose the user associated to the mailbox.**|
|DisplayName|**Regarding**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`regardingobjectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|queue, systemuser|

### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|---|---|
|Description|**Object Type of the entity associated with the mailbox.**|
|DisplayName|**Regarding Object Type Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_TestAndEnableLastAttemptedBy"></a> TestAndEnableLastAttemptedBy

|Property|Value|
|---|---|
|Description|**The user who last attempted to Test and Enable the mailbox.**|
|DisplayName|**Test and Enable Last Attempted By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`testandenablelastattemptedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_TestAndEnableLastAttemptedOn"></a> TestAndEnableLastAttemptedOn

|Property|Value|
|---|---|
|Description|**The date and time of the last test and enable attempt.**|
|DisplayName|**Test and Enable Last Attempted On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`testandenablelastattemptedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_TransientFailureCount"></a> TransientFailureCount

|Property|Value|
|---|---|
|Description|**Concatenation of transient failure counts of all mailbox operations.**|
|DisplayName|**Transient Failure Count**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`transientfailurecount`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the mailbox.**|
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

- [business_unit_mailbox](#BKMK_business_unit_mailbox)
- [emailserverprofile_mailbox](#BKMK_emailserverprofile_mailbox)
- [FileAttachment_Mailbox_ExchangeSyncStateXmlFileRef](#BKMK_FileAttachment_Mailbox_ExchangeSyncStateXmlFileRef)
- [lk_mailbox_createdby](#BKMK_lk_mailbox_createdby)
- [lk_mailbox_createdonbehalfby](#BKMK_lk_mailbox_createdonbehalfby)
- [lk_mailbox_modifiedby](#BKMK_lk_mailbox_modifiedby)
- [lk_mailbox_modifiedonbehalfby](#BKMK_lk_mailbox_modifiedonbehalfby)
- [mailbox_emailaddressapprovedby_systemuser](#BKMK_mailbox_emailaddressapprovedby_systemuser)
- [mailbox_regarding_queue](#BKMK_mailbox_regarding_queue)
- [mailbox_regarding_systemuser](#BKMK_mailbox_regarding_systemuser)
- [mailbox_testandenablelastattemptedby_systemuser](#BKMK_mailbox_testandenablelastattemptedby_systemuser)
- [organization_mailbox](#BKMK_organization_mailbox)
- [owner_mailbox](#BKMK_owner_mailbox)
- [team_mailbox](#BKMK_team_mailbox)
- [user_mailbox](#BKMK_user_mailbox)

### <a name="BKMK_business_unit_mailbox"></a> business_unit_mailbox

One-To-Many Relationship: [businessunit business_unit_mailbox](businessunit.md#BKMK_business_unit_mailbox)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_emailserverprofile_mailbox"></a> emailserverprofile_mailbox

One-To-Many Relationship: [emailserverprofile emailserverprofile_mailbox](emailserverprofile.md#BKMK_emailserverprofile_mailbox)

|Property|Value|
|---|---|
|ReferencedEntity|`emailserverprofile`|
|ReferencedAttribute|`emailserverprofileid`|
|ReferencingAttribute|`emailserverprofile`|
|ReferencingEntityNavigationPropertyName|`emailserverprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_Mailbox_ExchangeSyncStateXmlFileRef"></a> FileAttachment_Mailbox_ExchangeSyncStateXmlFileRef

One-To-Many Relationship: [fileattachment FileAttachment_Mailbox_ExchangeSyncStateXmlFileRef](fileattachment.md#BKMK_FileAttachment_Mailbox_ExchangeSyncStateXmlFileRef)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`exchangesyncstatexmlfileref`|
|ReferencingEntityNavigationPropertyName|`exchangesyncstatexmlfileref`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_mailbox_createdby"></a> lk_mailbox_createdby

One-To-Many Relationship: [systemuser lk_mailbox_createdby](systemuser.md#BKMK_lk_mailbox_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_mailbox_createdonbehalfby"></a> lk_mailbox_createdonbehalfby

One-To-Many Relationship: [systemuser lk_mailbox_createdonbehalfby](systemuser.md#BKMK_lk_mailbox_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_mailbox_modifiedby"></a> lk_mailbox_modifiedby

One-To-Many Relationship: [systemuser lk_mailbox_modifiedby](systemuser.md#BKMK_lk_mailbox_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_mailbox_modifiedonbehalfby"></a> lk_mailbox_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_mailbox_modifiedonbehalfby](systemuser.md#BKMK_lk_mailbox_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mailbox_emailaddressapprovedby_systemuser"></a> mailbox_emailaddressapprovedby_systemuser

One-To-Many Relationship: [systemuser mailbox_emailaddressapprovedby_systemuser](systemuser.md#BKMK_mailbox_emailaddressapprovedby_systemuser)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`emailaddressapprovedby`|
|ReferencingEntityNavigationPropertyName|`emailaddressapprovedby_mailbox`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mailbox_regarding_queue"></a> mailbox_regarding_queue

One-To-Many Relationship: [queue mailbox_regarding_queue](queue.md#BKMK_mailbox_regarding_queue)

|Property|Value|
|---|---|
|ReferencedEntity|`queue`|
|ReferencedAttribute|`queueid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_queue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mailbox_regarding_systemuser"></a> mailbox_regarding_systemuser

One-To-Many Relationship: [systemuser mailbox_regarding_systemuser](systemuser.md#BKMK_mailbox_regarding_systemuser)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mailbox_testandenablelastattemptedby_systemuser"></a> mailbox_testandenablelastattemptedby_systemuser

One-To-Many Relationship: [systemuser mailbox_testandenablelastattemptedby_systemuser](systemuser.md#BKMK_mailbox_testandenablelastattemptedby_systemuser)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`testandenablelastattemptedby`|
|ReferencingEntityNavigationPropertyName|`testandenablelastattemptedby_mailbox`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_mailbox"></a> organization_mailbox

One-To-Many Relationship: [organization organization_mailbox](organization.md#BKMK_organization_mailbox)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_mailbox"></a> owner_mailbox

One-To-Many Relationship: [owner owner_mailbox](owner.md#BKMK_owner_mailbox)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_mailbox"></a> team_mailbox

One-To-Many Relationship: [team team_mailbox](team.md#BKMK_team_mailbox)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_mailbox"></a> user_mailbox

One-To-Many Relationship: [systemuser user_mailbox](systemuser.md#BKMK_user_mailbox)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [activitypointer_sendermailboxid_mailbox](#BKMK_activitypointer_sendermailboxid_mailbox)
- [adx_inviteredemption_mailbox_sendermailboxid](#BKMK_adx_inviteredemption_mailbox_sendermailboxid)
- [adx_portalcomment_mailbox_sendermailboxid](#BKMK_adx_portalcomment_mailbox_sendermailboxid)
- [chat_mailbox_sendermailboxid](#BKMK_chat_mailbox_sendermailboxid)
- [email_sendermailboxid_mailbox](#BKMK_email_sendermailboxid_mailbox)
- [Mailbox_Annotation](#BKMK_Mailbox_Annotation)
- [mailbox_asyncoperations](#BKMK_mailbox_asyncoperations)
- [mailbox_email_ReceivingMailboxId](#BKMK_mailbox_email_ReceivingMailboxId)
- [mailbox_FileAttachments](#BKMK_mailbox_FileAttachments)
- [Mailbox_MailboxTrackingFolder](#BKMK_Mailbox_MailboxTrackingFolder)
- [mailbox_processsessions](#BKMK_mailbox_processsessions)
- [Mailbox_SyncErrors](#BKMK_Mailbox_SyncErrors)
- [queue_defaultmailbox_mailbox](#BKMK_queue_defaultmailbox_mailbox)
- [systemuser_defaultmailbox_mailbox](#BKMK_systemuser_defaultmailbox_mailbox)
- [tracelog_Mailbox](#BKMK_tracelog_Mailbox)

### <a name="BKMK_activitypointer_sendermailboxid_mailbox"></a> activitypointer_sendermailboxid_mailbox

Many-To-One Relationship: [activitypointer activitypointer_sendermailboxid_mailbox](activitypointer.md#BKMK_activitypointer_sendermailboxid_mailbox)

|Property|Value|
|---|---|
|ReferencingEntity|`activitypointer`|
|ReferencingAttribute|`sendermailboxid`|
|ReferencedEntityNavigationPropertyName|`activitypointer_sendermailboxid_mailbox`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_inviteredemption_mailbox_sendermailboxid"></a> adx_inviteredemption_mailbox_sendermailboxid

Many-To-One Relationship: [adx_inviteredemption adx_inviteredemption_mailbox_sendermailboxid](adx_inviteredemption.md#BKMK_adx_inviteredemption_mailbox_sendermailboxid)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_inviteredemption`|
|ReferencingAttribute|`sendermailboxid`|
|ReferencedEntityNavigationPropertyName|`adx_inviteredemption_mailbox_sendermailboxid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_portalcomment_mailbox_sendermailboxid"></a> adx_portalcomment_mailbox_sendermailboxid

Many-To-One Relationship: [adx_portalcomment adx_portalcomment_mailbox_sendermailboxid](adx_portalcomment.md#BKMK_adx_portalcomment_mailbox_sendermailboxid)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_portalcomment`|
|ReferencingAttribute|`sendermailboxid`|
|ReferencedEntityNavigationPropertyName|`adx_portalcomment_mailbox_sendermailboxid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_chat_mailbox_sendermailboxid"></a> chat_mailbox_sendermailboxid

Many-To-One Relationship: [chat chat_mailbox_sendermailboxid](chat.md#BKMK_chat_mailbox_sendermailboxid)

|Property|Value|
|---|---|
|ReferencingEntity|`chat`|
|ReferencingAttribute|`sendermailboxid`|
|ReferencedEntityNavigationPropertyName|`chat_mailbox_sendermailboxid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_email_sendermailboxid_mailbox"></a> email_sendermailboxid_mailbox

Many-To-One Relationship: [email email_sendermailboxid_mailbox](email.md#BKMK_email_sendermailboxid_mailbox)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`sendermailboxid`|
|ReferencedEntityNavigationPropertyName|`email_sendermailboxid_mailbox`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Mailbox_Annotation"></a> Mailbox_Annotation

Many-To-One Relationship: [annotation Mailbox_Annotation](annotation.md#BKMK_Mailbox_Annotation)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`Mailbox_Annotation`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mailbox_asyncoperations"></a> mailbox_asyncoperations

Many-To-One Relationship: [asyncoperation mailbox_asyncoperations](asyncoperation.md#BKMK_mailbox_asyncoperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mailbox_asyncoperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mailbox_email_ReceivingMailboxId"></a> mailbox_email_ReceivingMailboxId

Many-To-One Relationship: [email mailbox_email_ReceivingMailboxId](email.md#BKMK_mailbox_email_ReceivingMailboxId)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`receivingmailboxid`|
|ReferencedEntityNavigationPropertyName|`mailbox_email_ReceivingMailboxId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mailbox_FileAttachments"></a> mailbox_FileAttachments

Many-To-One Relationship: [fileattachment mailbox_FileAttachments](fileattachment.md#BKMK_mailbox_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`mailbox_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Mailbox_MailboxTrackingFolder"></a> Mailbox_MailboxTrackingFolder

Many-To-One Relationship: [mailboxtrackingfolder Mailbox_MailboxTrackingFolder](mailboxtrackingfolder.md#BKMK_Mailbox_MailboxTrackingFolder)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`mailboxid`|
|ReferencedEntityNavigationPropertyName|`Mailbox_MailboxTrackingFolder`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mailbox_processsessions"></a> mailbox_processsessions

Many-To-One Relationship: [processsession mailbox_processsessions](processsession.md#BKMK_mailbox_processsessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mailbox_processsessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Mailbox_SyncErrors"></a> Mailbox_SyncErrors

Many-To-One Relationship: [syncerror Mailbox_SyncErrors](syncerror.md#BKMK_Mailbox_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Mailbox_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_queue_defaultmailbox_mailbox"></a> queue_defaultmailbox_mailbox

Many-To-One Relationship: [queue queue_defaultmailbox_mailbox](queue.md#BKMK_queue_defaultmailbox_mailbox)

|Property|Value|
|---|---|
|ReferencingEntity|`queue`|
|ReferencingAttribute|`defaultmailbox`|
|ReferencedEntityNavigationPropertyName|`queue_defaultmailbox_mailbox`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_systemuser_defaultmailbox_mailbox"></a> systemuser_defaultmailbox_mailbox

Many-To-One Relationship: [systemuser systemuser_defaultmailbox_mailbox](systemuser.md#BKMK_systemuser_defaultmailbox_mailbox)

|Property|Value|
|---|---|
|ReferencingEntity|`systemuser`|
|ReferencingAttribute|`defaultmailbox`|
|ReferencedEntityNavigationPropertyName|`systemuser_defaultmailbox_mailbox`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_tracelog_Mailbox"></a> tracelog_Mailbox

Many-To-One Relationship: [tracelog tracelog_Mailbox](tracelog.md#BKMK_tracelog_Mailbox)

|Property|Value|
|---|---|
|ReferencingEntity|`tracelog`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`tracelog_Mailbox`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mailbox?displayProperty=fullName>
