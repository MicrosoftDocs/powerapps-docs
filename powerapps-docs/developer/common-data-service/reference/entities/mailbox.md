---
title: "Mailbox Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the Mailbox entity."
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
ms.date: 10/31/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Mailbox Entity Reference



## Entity Properties

**DisplayName**: Mailbox<br />
**DisplayCollectionName**: Mailboxes<br />
**SchemaName**: Mailbox<br />
**CollectionSchemaName**: Mailboxes<br />
**LogicalName**: mailbox<br />
**LogicalCollectionName**: mailboxes<br />
**EntitySetName**: mailboxes<br />
**PrimaryIdAttribute**: mailboxid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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
- [LastSyncError](#BKMK_LastSyncError)
- [LastSyncErrorCode](#BKMK_LastSyncErrorCode)
- [LastSyncErrorCount](#BKMK_LastSyncErrorCount)
- [LastSyncErrorMachineName](#BKMK_LastSyncErrorMachineName)
- [LastSyncErrorOccurredOn](#BKMK_LastSyncErrorOccurredOn)
- [MailboxId](#BKMK_MailboxId)
- [MailboxProcessingContext](#BKMK_MailboxProcessingContext)
- [Name](#BKMK_Name)
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
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [TestEmailConfigurationRetryCount](#BKMK_TestEmailConfigurationRetryCount)
- [TestEmailConfigurationScheduled](#BKMK_TestEmailConfigurationScheduled)
- [TestMailboxAccessCompletedOn](#BKMK_TestMailboxAccessCompletedOn)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UndeliverableFolder](#BKMK_UndeliverableFolder)
- [Username](#BKMK_Username)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [VerboseLoggingEnabled](#BKMK_VerboseLoggingEnabled)


### <a name="BKMK_ACTDeliveryMethod"></a> ACTDeliveryMethod

**Description**: Choose the delivery method for the mailbox for appointments, contacts, and tasks.<br />
**DisplayName**: Appointments, Contacts, and Tasks<br />
**LogicalName**: actdeliverymethod<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Microsoft Dynamics 365 for Outlook
- **Value**: 1 **Label**: Server-Side Synchronization
- **Value**: 2 **Label**: None



### <a name="BKMK_ACTStatus"></a> ACTStatus

**Description**: Status of the Appointments, Contacts, and Tasks.<br />
**DisplayName**: Appointments, Contacts, and Tasks Status<br />
**LogicalName**: actstatus<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Not Run
- **Value**: 1 **Label**: Success
- **Value**: 2 **Label**: Failure



### <a name="BKMK_AllowEmailConnectorToUseCredentials"></a> AllowEmailConnectorToUseCredentials

**Description**: Choose whether to allow the email connector to use credentials.<br />
**DisplayName**: Allow to Use Credentials for Email Processing<br />
**LogicalName**: allowemailconnectortousecredentials<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_EmailAddress"></a> EmailAddress

**Description**: Type the email address of the mailbox.<br />
**DisplayName**: Email Address<br />
**LogicalName**: emailaddress<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Email<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_EmailRouterAccessApproval"></a> EmailRouterAccessApproval

**Description**: Shows the status of the email address.<br />
**DisplayName**: Email Address Status<br />
**LogicalName**: emailrouteraccessapproval<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Empty
- **Value**: 1 **Label**: Approved
- **Value**: 2 **Label**: Pending Approval
- **Value**: 3 **Label**: Rejected



### <a name="BKMK_EmailServerProfile"></a> EmailServerProfile

**Description**: Select the email server profile of the mailbox.<br />
**DisplayName**: Server Profile<br />
**LogicalName**: emailserverprofile<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: emailserverprofile


### <a name="BKMK_EnabledForACT"></a> EnabledForACT

**Description**: Indicates whether the mailbox is enabled for Appointments, Contacts, and Tasks.<br />
**DisplayName**: Enabled For Appointments, Contacts, And Tasks<br />
**LogicalName**: enabledforact<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_EnabledForIncomingEmail"></a> EnabledForIncomingEmail

**Description**: Choose whether the mailbox is enabled for receiving email.<br />
**DisplayName**: Enabled For Incoming Email<br />
**LogicalName**: enabledforincomingemail<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_EnabledForOutgoingEmail"></a> EnabledForOutgoingEmail

**Description**: Choose whether the mailbox is enabled for sending email.<br />
**DisplayName**: Enabled For Outgoing Email<br />
**LogicalName**: enabledforoutgoingemail<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


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


### <a name="BKMK_EWSURL"></a> EWSURL

**Description**: Exchange web services endpoint URL for the mailbox.<br />
**DisplayName**: Exchange Web Services URL<br />
**LogicalName**: ewsurl<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Url<br />
**IsLocalizable**: False<br />
**MaxLength**: 2084


### <a name="BKMK_ExchangeContactsImportStatus"></a> ExchangeContactsImportStatus

**Description**: Indicates the exchange contacts import status for a mailbox record.<br />
**DisplayName**: Exchange Contacts Import Status<br />
**LogicalName**: exchangecontactsimportstatus<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: NotImported
- **Value**: 1 **Label**: Imported
- **Value**: 2 **Label**: ImportFailed



### <a name="BKMK_ExchangeSyncStateXml"></a> ExchangeSyncStateXml

**Description**: Contains the exchange synchronization state in XML format.<br />
**DisplayName**: Exchange Sync State<br />
**LogicalName**: exchangesyncstatexml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_FolderHierarchy"></a> FolderHierarchy

**Description**: Holds the hierarchy of folders under inbox in XML format.<br />
**DisplayName**: Folder Hierarchy<br />
**LogicalName**: folderhierarchy<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1048576


### <a name="BKMK_IncomingEmailDeliveryMethod"></a> IncomingEmailDeliveryMethod

**Description**: Select how incoming email will be delivered to the mailbox.<br />
**DisplayName**: Incoming Email<br />
**LogicalName**: incomingemaildeliverymethod<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: None
- **Value**: 1 **Label**: Microsoft Dynamics 365 for Outlook
- **Value**: 2 **Label**: Server-Side Synchronization or Email Router
- **Value**: 3 **Label**: Forward Mailbox



### <a name="BKMK_IncomingEmailStatus"></a> IncomingEmailStatus

**Description**: Select the status that will be assigned to incoming email messages.<br />
**DisplayName**: Incoming Email Status<br />
**LogicalName**: incomingemailstatus<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Not Run
- **Value**: 1 **Label**: Success
- **Value**: 2 **Label**: Failure



### <a name="BKMK_IsACTSyncOrgFlagSet"></a> IsACTSyncOrgFlagSet

**Description**: Set the current organization as the synchronization organization.<br />
**DisplayName**: Set Current Organization as Synchronization Organization<br />
**LogicalName**: isactsyncorgflagset<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsEmailAddressApprovedByO365Admin"></a> IsEmailAddressApprovedByO365Admin

**Description**: Shows the status of approval of the email address by O365 Admin.<br />
**DisplayName**: Email Address O365 Admin Approval Status<br />
**LogicalName**: isemailaddressapprovedbyo365admin<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_ItemsFailedForLastSync"></a> ItemsFailedForLastSync

**Description**: For internal use only.<br />
**DisplayName**: Items Failed For Last Sync<br />
**LogicalName**: itemsfailedforlastsync<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_ItemsProcessedForLastSync"></a> ItemsProcessedForLastSync

**Description**: For internal use only.<br />
**DisplayName**: Items Processed For Last Sync<br />
**LogicalName**: itemsprocessedforlastsync<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_LastAutoDiscoveredOn"></a> LastAutoDiscoveredOn

**Description**: Shows the date and time when the Exchange web services URL was last discovered using the AutoDiscover service.<br />
**DisplayName**: Last Auto Discovered On<br />
**LogicalName**: lastautodiscoveredon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_LastSyncError"></a> LastSyncError

**Description**: For internal use only.<br />
**DisplayName**: Last Sync Error Stack<br />
**LogicalName**: lastsyncerror<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2048


### <a name="BKMK_LastSyncErrorCode"></a> LastSyncErrorCode

**Description**: For internal use only.<br />
**DisplayName**: Last Sync Error Code<br />
**LogicalName**: lastsyncerrorcode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_LastSyncErrorCount"></a> LastSyncErrorCount

**Description**: For internal use only<br />
**DisplayName**: Last Sync Error Continuous Count<br />
**LogicalName**: lastsyncerrorcount<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_LastSyncErrorMachineName"></a> LastSyncErrorMachineName

**Description**: For internal use only.<br />
**DisplayName**: Last Sync Error Machine Name<br />
**LogicalName**: lastsyncerrormachinename<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 320


### <a name="BKMK_LastSyncErrorOccurredOn"></a> LastSyncErrorOccurredOn

**Description**: For internal use only.<br />
**DisplayName**: Last Sync Error Time<br />
**LogicalName**: lastsyncerroroccurredon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_MailboxId"></a> MailboxId

**Description**: Unique identifier of the mailbox.<br />
**DisplayName**: Mailbox<br />
**LogicalName**: mailboxid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_MailboxProcessingContext"></a> MailboxProcessingContext

**Description**: For internal use only.<br />
**DisplayName**: Processing Context of the Mailbox<br />
**LogicalName**: mailboxprocessingcontext<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_Name"></a> Name

**Description**: Type the name of the mailbox.<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_OfficeAppsDeploymentScheduled"></a> OfficeAppsDeploymentScheduled

**Description**: Indicates if the office apps deployment has been scheduled for a mailbox record.<br />
**DisplayName**: Office Apps Deployment Scheduled<br />
**LogicalName**: officeappsdeploymentscheduled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_OfficeAppsDeploymentStatus"></a> OfficeAppsDeploymentStatus

**Description**: Indicates the office apps deployment type for a mailbox record.<br />
**DisplayName**: Office Apps Deployment Type<br />
**LogicalName**: officeappsdeploymentstatus<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: NotInstalled
- **Value**: 1 **Label**: Installed
- **Value**: 2 **Label**: InstallFailed
- **Value**: 3 **Label**: UninstallFailed
- **Value**: 4 **Label**: UpgradeRequired



### <a name="BKMK_OrgMarkedAsPrimaryForExchangeSync"></a> OrgMarkedAsPrimaryForExchangeSync

**Description**: Indicates if the crm org is to be marked as primary syncing org for the mailbox record.<br />
**DisplayName**: Crm Org Marked as Primary Org for Exchange Mailbox<br />
**LogicalName**: orgmarkedasprimaryforexchangesync<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_OutgoingEmailDeliveryMethod"></a> OutgoingEmailDeliveryMethod

**Description**: Select how outgoing email will be sent from the mailbox.<br />
**DisplayName**: Outgoing Email<br />
**LogicalName**: outgoingemaildeliverymethod<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: None
- **Value**: 1 **Label**: Microsoft Dynamics 365 for Outlook
- **Value**: 2 **Label**: Server-Side Synchronization or Email Router



### <a name="BKMK_OutgoingEmailStatus"></a> OutgoingEmailStatus

**Description**: Select the status of outgoing email messages.<br />
**DisplayName**: Outgoing Email Status<br />
**LogicalName**: outgoingemailstatus<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Not Run
- **Value**: 1 **Label**: Success
- **Value**: 2 **Label**: Failure



### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: Owner Id Type<br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_Password"></a> Password

**Description**: Type the password for the mailbox.<br />
**DisplayName**: Password<br />
**LogicalName**: password<br />
**IsValidForForm**: True<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_PostponeMailboxProcessingUntil"></a> PostponeMailboxProcessingUntil

**Description**: Shows the date and time when processing will begin on this mailbox.<br />
**DisplayName**: Postpone Mailbox Processing Until<br />
**LogicalName**: postponemailboxprocessinguntil<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_PostponeOfficeAppsDeploymentUntil"></a> PostponeOfficeAppsDeploymentUntil

**Description**: Shows the date and time when the next outlook mail app install will be run for a mailbox record.<br />
**DisplayName**: Postpone Outlook Mail App Install Until<br />
**LogicalName**: postponeofficeappsdeploymentuntil<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_PostponeSendingUntil"></a> PostponeSendingUntil

**Description**: Shows the date and time when the mailbox can start sending emails.<br />
**DisplayName**: Postpone Sending Until<br />
**LogicalName**: postponesendinguntil<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_PostponeTestEmailConfigurationUntil"></a> PostponeTestEmailConfigurationUntil

**Description**: Shows the date and time when the next email configuration test will be run for a mailbox record.<br />
**DisplayName**: Postpone Test Email Configuration Until<br />
**LogicalName**: postponetestemailconfigurationuntil<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ProcessAndDeleteEmails"></a> ProcessAndDeleteEmails

**Description**: Select whether to delete emails from the mailbox after processing.<br />
**DisplayName**: Delete Emails after Processing<br />
**LogicalName**: processanddeleteemails<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_ProcessEmailReceivedAfter"></a> ProcessEmailReceivedAfter

**Description**: Shows the date and time to start processing email received by the mailbox.<br />
**DisplayName**: Process Email Received After<br />
**LogicalName**: processemailreceivedafter<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_StateCode"></a> StateCode

**Description**: Shows whether the mailbox is active or inactive.<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Active **DefaultStatus**: 1 **InvariantName**: Active
- **Value**: 1 **Label**: Inactive **DefaultStatus**: 2 **InvariantName**: Inactive



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Select the mailbox's status.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Status<br />
**Options**:

- **Value**: 1 **Label**: Active **State**: 0
- **Value**: 2 **Label**: Inactive **State**: 1



### <a name="BKMK_TestEmailConfigurationRetryCount"></a> TestEmailConfigurationRetryCount

**Description**: Shows the number of times an email configuration test has been performed.<br />
**DisplayName**: Test Email Configuration Retry Count<br />
**LogicalName**: testemailconfigurationretrycount<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_TestEmailConfigurationScheduled"></a> TestEmailConfigurationScheduled

**Description**: Indicates if the email configuration test has been scheduled for a mailbox record.<br />
**DisplayName**: Test Email Configuration Scheduled<br />
**LogicalName**: testemailconfigurationscheduled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_TestMailboxAccessCompletedOn"></a> TestMailboxAccessCompletedOn

**Description**: Date and time when the last email configuration test was completed for a mailbox record.<br />
**DisplayName**: Mailbox Test Completed On<br />
**LogicalName**: testmailboxaccesscompletedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


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


### <a name="BKMK_UndeliverableFolder"></a> UndeliverableFolder

**Description**: Shows the ID of the Undeliverable folder in the mailbox managed by Microsoft Exchange.<br />
**DisplayName**: Undeliverable Folder<br />
**LogicalName**: undeliverablefolder<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_Username"></a> Username

**Description**: Type a user name used for mailbox authentication.<br />
**DisplayName**: User Name<br />
**LogicalName**: username<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


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


### <a name="BKMK_VerboseLoggingEnabled"></a> VerboseLoggingEnabled

**Description**: Indicates if verbose tracing needs to be enabled for this mailbox.<br />
**DisplayName**: Verbose Logging<br />
**LogicalName**: verboseloggingenabled<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 100<br />
**MinValue**: 0

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AverageTotalDuration](#BKMK_AverageTotalDuration)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [EmailServerProfileName](#BKMK_EmailServerProfileName)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [ExchangeContactsImportCompletedOn](#BKMK_ExchangeContactsImportCompletedOn)
- [ForcedUnlockCount](#BKMK_ForcedUnlockCount)
- [HostId](#BKMK_HostId)
- [IsExchangeContactsImportScheduled](#BKMK_IsExchangeContactsImportScheduled)
- [IsForwardMailbox](#BKMK_IsForwardMailbox)
- [IsPasswordSet](#BKMK_IsPasswordSet)
- [IsServiceAccount](#BKMK_IsServiceAccount)
- [LastActiveOn](#BKMK_LastActiveOn)
- [LastDuration](#BKMK_LastDuration)
- [LastMailboxForcedUnlockOccurredOn](#BKMK_LastMailboxForcedUnlockOccurredOn)
- [LastMessageId](#BKMK_LastMessageId)
- [LastSuccessfulSyncCompletedOn](#BKMK_LastSuccessfulSyncCompletedOn)
- [LastSyncStartedOn](#BKMK_LastSyncStartedOn)
- [MailboxStatus](#BKMK_MailboxStatus)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [NoACTCount](#BKMK_NoACTCount)
- [NoEmailCount](#BKMK_NoEmailCount)
- [OfficeAppsDeploymentCompleteOn](#BKMK_OfficeAppsDeploymentCompleteOn)
- [OfficeAppsDeploymentError](#BKMK_OfficeAppsDeploymentError)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [ProcessedTimes](#BKMK_ProcessedTimes)
- [ProcessingLastAttemptedOn](#BKMK_ProcessingLastAttemptedOn)
- [ProcessingStateCode](#BKMK_ProcessingStateCode)
- [ReceivingPostponedUntil](#BKMK_ReceivingPostponedUntil)
- [ReceivingPostponedUntilForACT](#BKMK_ReceivingPostponedUntilForACT)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [TransientFailureCount](#BKMK_TransientFailureCount)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_AverageTotalDuration"></a> AverageTotalDuration

**Description**: Mailbox Total Duration in Average<br />
**DisplayName**: Monitor Total Performance<br />
**LogicalName**: averagetotalduration<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Shows who created the record.<br />
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
**MaxLength**: 160


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
**MaxLength**: 160


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Shows who created the record on behalf of another user.<br />
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
**MaxLength**: 160


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
**MaxLength**: 160


### <a name="BKMK_EmailServerProfileName"></a> EmailServerProfileName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: emailserverprofilename<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


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


### <a name="BKMK_ExchangeContactsImportCompletedOn"></a> ExchangeContactsImportCompletedOn

**Description**: Date and time when the exchange contacts import was last completed for a mailbox record.<br />
**DisplayName**: Exchange Contacts Import Completed On<br />
**LogicalName**: exchangecontactsimportcompletedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ForcedUnlockCount"></a> ForcedUnlockCount

**Description**: For internal use only<br />
**DisplayName**: Count of the number of times a mailbox gets forced unlocked<br />
**LogicalName**: forcedunlockcount<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_HostId"></a> HostId

**Description**: Unique identifier of the async host that is processing this mailbox.<br />
**DisplayName**: Host<br />
**LogicalName**: hostid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_IsExchangeContactsImportScheduled"></a> IsExchangeContactsImportScheduled

**Description**: Is Exchange Contacts Import Scheduled.<br />
**DisplayName**: Is Exchange Contacts Import Scheduled.<br />
**LogicalName**: isexchangecontactsimportscheduled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsForwardMailbox"></a> IsForwardMailbox

**Description**: Select whether the mailbox is a forward mailbox.<br />
**DisplayName**: Is Forward Mailbox<br />
**LogicalName**: isforwardmailbox<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_IsPasswordSet"></a> IsPasswordSet

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: ispasswordset<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsServiceAccount"></a> IsServiceAccount

**Description**: Select whether the mailbox corresponds to one for the service account.<br />
**DisplayName**: Is Service Account<br />
**LogicalName**: isserviceaccount<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_LastActiveOn"></a> LastActiveOn

**Description**: For internal use only.<br />
**DisplayName**: Last Active On<br />
**LogicalName**: lastactiveon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_LastDuration"></a> LastDuration

**Description**: Last Duration for the mailbox<br />
**DisplayName**: Monitor last duration Performance<br />
**LogicalName**: lastduration<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_LastMailboxForcedUnlockOccurredOn"></a> LastMailboxForcedUnlockOccurredOn

**Description**: For internal use only.<br />
**DisplayName**: Last Date Time when a mailbox got forced unlocked<br />
**LogicalName**: lastmailboxforcedunlockoccurredon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_LastMessageId"></a> LastMessageId

**Description**: Unique identifier of the last message.<br />
**DisplayName**: Last Message ID<br />
**LogicalName**: lastmessageid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 320


### <a name="BKMK_LastSuccessfulSyncCompletedOn"></a> LastSuccessfulSyncCompletedOn

**Description**: Last Successful Sync Time<br />
**DisplayName**: Last Successful Sync Time<br />
**LogicalName**: lastsuccessfulsynccompletedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_LastSyncStartedOn"></a> LastSyncStartedOn

**Description**: Last Sync Start Time<br />
**DisplayName**: Last Sync Start Time<br />
**LogicalName**: lastsyncstartedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_MailboxStatus"></a> MailboxStatus

**Description**: Last Sync Status for Outgoing, Incoming and ACT as a whole.<br />
**DisplayName**: Mailbox Status<br />
**LogicalName**: mailboxstatus<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Not Run
- **Value**: 1 **Label**: Success
- **Value**: 2 **Label**: Failure



### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Shows who last updated the record.<br />
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
**MaxLength**: 160


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
**MaxLength**: 160


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Shows who last updated the record on behalf of another user.<br />
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
**MaxLength**: 160


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
**MaxLength**: 160


### <a name="BKMK_NoACTCount"></a> NoACTCount

**Description**: For internal use only.<br />
**DisplayName**: Zero appointment, contact, task count for mailbox<br />
**LogicalName**: noactcount<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_NoEmailCount"></a> NoEmailCount

**Description**: For internal use only.<br />
**DisplayName**: Zero email count for mailbox<br />
**LogicalName**: noemailcount<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_OfficeAppsDeploymentCompleteOn"></a> OfficeAppsDeploymentCompleteOn

**Description**: Date and time when the last office apps deployment was completed for a mailbox record.<br />
**DisplayName**: Office Apps Deployment Completed On<br />
**LogicalName**: officeappsdeploymentcompleteon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_OfficeAppsDeploymentError"></a> OfficeAppsDeploymentError

**Description**: The Office Apps deployment error.<br />
**DisplayName**: Office Apps Deployment Error<br />
**LogicalName**: officeappsdeploymenterror<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2048


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization associated with the record.<br />
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
**MaxLength**: 160


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Description**: Name of the owner<br />
**DisplayName**: <br />
**LogicalName**: owneridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

**Description**: Yomi name of the owner<br />
**DisplayName**: <br />
**LogicalName**: owneridyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Description**: Select the business unit that owns the record.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningBusinessUnitName"></a> OwningBusinessUnitName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owningbusinessunitname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier for the team that owns the record.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier for the user that owns the record.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ProcessedTimes"></a> ProcessedTimes

**Description**: The number of times mailbox has processed<br />
**DisplayName**: Monitor Performance<br />
**LogicalName**: processedtimes<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_ProcessingLastAttemptedOn"></a> ProcessingLastAttemptedOn

**Description**: Date and time when the processing of the mailbox was last attempted.<br />
**DisplayName**: Date Processing Last Attempted<br />
**LogicalName**: processinglastattemptedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ProcessingStateCode"></a> ProcessingStateCode

**Description**: Information that indicates whether email will be processed for this mailbox<br />
**DisplayName**: Mailbox Processing State<br />
**LogicalName**: processingstatecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_ReceivingPostponedUntil"></a> ReceivingPostponedUntil

**Description**: For internal use only.<br />
**DisplayName**: Postpone receiving emails for the mailbox until the specified data and time.<br />
**LogicalName**: receivingpostponeduntil<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_ReceivingPostponedUntilForACT"></a> ReceivingPostponedUntilForACT

**Description**: For internal use only.<br />
**DisplayName**: Postpone processing Appointments, Contacts, and Tasks for the mailbox until the specified data and time.<br />
**LogicalName**: receivingpostponeduntilforact<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

**Description**: Choose the user associated to the mailbox.<br />
**DisplayName**: Regarding<br />
**LogicalName**: regardingobjectid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: queue,systemuser


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

**Description**: Name for User associated with Mailbox.<br />
**DisplayName**: Regarding Name<br />
**LogicalName**: regardingobjectidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

**Description**: Object Type of the entity associated with the mailbox.<br />
**DisplayName**: Regarding Object Type Code<br />
**LogicalName**: regardingobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_TransientFailureCount"></a> TransientFailureCount

**Description**: Concatenation of transient failure counts of all mailbox operations.<br />
**DisplayName**: Transient Failure Count<br />
**LogicalName**: transientfailurecount<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: Version number of the mailbox.<br />
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

- [mailbox_userentityinstancedatas](#BKMK_mailbox_userentityinstancedatas)
- [systemuser_defaultmailbox_mailbox](#BKMK_systemuser_defaultmailbox_mailbox)
- [queue_defaultmailbox_mailbox](#BKMK_queue_defaultmailbox_mailbox)
- [activitypointer_sendermailboxid_mailbox](#BKMK_activitypointer_sendermailboxid_mailbox)
- [Mailbox_MailboxTrackingFolder](#BKMK_Mailbox_MailboxTrackingFolder)
- [Mailbox_Annotation](#BKMK_Mailbox_Annotation)
- [Mailbox_SyncErrors](#BKMK_Mailbox_SyncErrors)
- [mailbox_processsessions](#BKMK_mailbox_processsessions)
- [mailbox_asyncoperations](#BKMK_mailbox_asyncoperations)
- [tracelog_Mailbox](#BKMK_tracelog_Mailbox)
- [email_sendermailboxid_mailbox](#BKMK_email_sendermailboxid_mailbox)
- [mailbox_mailboxstatistics](#BKMK_mailbox_mailboxstatistics)


### <a name="BKMK_mailbox_userentityinstancedatas"></a> mailbox_userentityinstancedatas

Same as userentityinstancedata entity [mailbox_userentityinstancedatas](userentityinstancedata.md#BKMK_mailbox_userentityinstancedatas) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: mailbox_userentityinstancedatas<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_systemuser_defaultmailbox_mailbox"></a> systemuser_defaultmailbox_mailbox

Same as systemuser entity [systemuser_defaultmailbox_mailbox](systemuser.md#BKMK_systemuser_defaultmailbox_mailbox) Many-To-One relationship.

**ReferencingEntity**: systemuser<br />
**ReferencingAttribute**: defaultmailbox<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: systemuser_defaultmailbox_mailbox<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_queue_defaultmailbox_mailbox"></a> queue_defaultmailbox_mailbox

Same as queue entity [queue_defaultmailbox_mailbox](queue.md#BKMK_queue_defaultmailbox_mailbox) Many-To-One relationship.

**ReferencingEntity**: queue<br />
**ReferencingAttribute**: defaultmailbox<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: queue_defaultmailbox_mailbox<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_activitypointer_sendermailboxid_mailbox"></a> activitypointer_sendermailboxid_mailbox

Same as activitypointer entity [activitypointer_sendermailboxid_mailbox](activitypointer.md#BKMK_activitypointer_sendermailboxid_mailbox) Many-To-One relationship.

**ReferencingEntity**: activitypointer<br />
**ReferencingAttribute**: sendermailboxid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: activitypointer_sendermailboxid_mailbox<br />
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


### <a name="BKMK_Mailbox_MailboxTrackingFolder"></a> Mailbox_MailboxTrackingFolder

Same as mailboxtrackingfolder entity [Mailbox_MailboxTrackingFolder](mailboxtrackingfolder.md#BKMK_Mailbox_MailboxTrackingFolder) Many-To-One relationship.

**ReferencingEntity**: mailboxtrackingfolder<br />
**ReferencingAttribute**: mailboxid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Mailbox_MailboxTrackingFolder<br />
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


### <a name="BKMK_Mailbox_Annotation"></a> Mailbox_Annotation

Same as annotation entity [Mailbox_Annotation](annotation.md#BKMK_Mailbox_Annotation) Many-To-One relationship.

**ReferencingEntity**: annotation<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Mailbox_Annotation<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_Mailbox_SyncErrors"></a> Mailbox_SyncErrors

Same as syncerror entity [Mailbox_SyncErrors](syncerror.md#BKMK_Mailbox_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: Mailbox_SyncErrors<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_mailbox_processsessions"></a> mailbox_processsessions

Same as processsession entity [mailbox_processsessions](processsession.md#BKMK_mailbox_processsessions) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: mailbox_processsessions<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 110

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_mailbox_asyncoperations"></a> mailbox_asyncoperations

Same as asyncoperation entity [mailbox_asyncoperations](asyncoperation.md#BKMK_mailbox_asyncoperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: mailbox_asyncoperations<br />
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


### <a name="BKMK_tracelog_Mailbox"></a> tracelog_Mailbox

Same as tracelog entity [tracelog_Mailbox](tracelog.md#BKMK_tracelog_Mailbox) Many-To-One relationship.

**ReferencingEntity**: tracelog<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: tracelog_Mailbox<br />
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


### <a name="BKMK_email_sendermailboxid_mailbox"></a> email_sendermailboxid_mailbox

Same as email entity [email_sendermailboxid_mailbox](email.md#BKMK_email_sendermailboxid_mailbox) Many-To-One relationship.

**ReferencingEntity**: email<br />
**ReferencingAttribute**: sendermailboxid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: email_sendermailboxid_mailbox<br />
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


### <a name="BKMK_mailbox_mailboxstatistics"></a> mailbox_mailboxstatistics

Same as mailboxstatistics entity [mailbox_mailboxstatistics](mailboxstatistics.md#BKMK_mailbox_mailboxstatistics) Many-To-One relationship.

**ReferencingEntity**: mailboxstatistics<br />
**ReferencingAttribute**: mailboxid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: mailbox_mailboxstatistics<br />
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

- [lk_mailbox_createdby](#BKMK_lk_mailbox_createdby)
- [lk_mailbox_createdonbehalfby](#BKMK_lk_mailbox_createdonbehalfby)
- [lk_mailbox_modifiedby](#BKMK_lk_mailbox_modifiedby)
- [lk_mailbox_modifiedonbehalfby](#BKMK_lk_mailbox_modifiedonbehalfby)
- [user_mailbox](#BKMK_user_mailbox)
- [team_mailbox](#BKMK_team_mailbox)
- [business_unit_mailbox](#BKMK_business_unit_mailbox)
- [mailbox_regarding_systemuser](#BKMK_mailbox_regarding_systemuser)
- [emailserverprofile_mailbox](#BKMK_emailserverprofile_mailbox)
- [organization_mailbox](#BKMK_organization_mailbox)
- [mailbox_regarding_queue](#BKMK_mailbox_regarding_queue)


### <a name="BKMK_lk_mailbox_createdby"></a> lk_mailbox_createdby

See systemuser Entity [lk_mailbox_createdby](systemuser.md#BKMK_lk_mailbox_createdby) One-To-Many relationship.

### <a name="BKMK_lk_mailbox_createdonbehalfby"></a> lk_mailbox_createdonbehalfby

See systemuser Entity [lk_mailbox_createdonbehalfby](systemuser.md#BKMK_lk_mailbox_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_mailbox_modifiedby"></a> lk_mailbox_modifiedby

See systemuser Entity [lk_mailbox_modifiedby](systemuser.md#BKMK_lk_mailbox_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_mailbox_modifiedonbehalfby"></a> lk_mailbox_modifiedonbehalfby

See systemuser Entity [lk_mailbox_modifiedonbehalfby](systemuser.md#BKMK_lk_mailbox_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_user_mailbox"></a> user_mailbox

See systemuser Entity [user_mailbox](systemuser.md#BKMK_user_mailbox) One-To-Many relationship.

### <a name="BKMK_team_mailbox"></a> team_mailbox

See team Entity [team_mailbox](team.md#BKMK_team_mailbox) One-To-Many relationship.

### <a name="BKMK_business_unit_mailbox"></a> business_unit_mailbox

See businessunit Entity [business_unit_mailbox](businessunit.md#BKMK_business_unit_mailbox) One-To-Many relationship.

### <a name="BKMK_mailbox_regarding_systemuser"></a> mailbox_regarding_systemuser

See systemuser Entity [mailbox_regarding_systemuser](systemuser.md#BKMK_mailbox_regarding_systemuser) One-To-Many relationship.

### <a name="BKMK_emailserverprofile_mailbox"></a> emailserverprofile_mailbox

See emailserverprofile Entity [emailserverprofile_mailbox](emailserverprofile.md#BKMK_emailserverprofile_mailbox) One-To-Many relationship.

### <a name="BKMK_organization_mailbox"></a> organization_mailbox

See organization Entity [organization_mailbox](organization.md#BKMK_organization_mailbox) One-To-Many relationship.

### <a name="BKMK_mailbox_regarding_queue"></a> mailbox_regarding_queue

See queue Entity [mailbox_regarding_queue](queue.md#BKMK_mailbox_regarding_queue) One-To-Many relationship.
mailbox

