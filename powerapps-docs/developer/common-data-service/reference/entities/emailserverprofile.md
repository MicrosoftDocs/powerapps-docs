---
title: "EmailServerProfile Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the EmailServerProfile entity."
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
# EmailServerProfile Entity Reference

Holds the Email Server Profiles of an organization

## Entity Properties

**DisplayName**: Email Server Profile<br />
**DisplayCollectionName**: Email Server Profiles<br />
**SchemaName**: EmailServerProfile<br />
**CollectionSchemaName**: EmailServerProfiles<br />
**LogicalName**: emailserverprofile<br />
**LogicalCollectionName**: emailserverprofiles<br />
**EntitySetName**: emailserverprofiles<br />
**PrimaryIdAttribute**: emailserverprofileid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [DefaultServerLocation](#BKMK_DefaultServerLocation)
- [Description](#BKMK_Description)
- [EmailServerProfileId](#BKMK_EmailServerProfileId)
- [EncodingCodePage](#BKMK_EncodingCodePage)
- [EntityImage](#BKMK_EntityImage)
- [ExchangeOnlineTenantId](#BKMK_ExchangeOnlineTenantId)
- [ExchangeVersion](#BKMK_ExchangeVersion)
- [IncomingAuthenticationProtocol](#BKMK_IncomingAuthenticationProtocol)
- [IncomingCredentialRetrieval](#BKMK_IncomingCredentialRetrieval)
- [IncomingPassword](#BKMK_IncomingPassword)
- [IncomingPortNumber](#BKMK_IncomingPortNumber)
- [IncomingServerLocation](#BKMK_IncomingServerLocation)
- [IncomingUseImpersonation](#BKMK_IncomingUseImpersonation)
- [IncomingUserName](#BKMK_IncomingUserName)
- [IncomingUseSSL](#BKMK_IncomingUseSSL)
- [LastAuthorizationStatus](#BKMK_LastAuthorizationStatus)
- [LastCrmMessage](#BKMK_LastCrmMessage)
- [LastTestExecutionStatus](#BKMK_LastTestExecutionStatus)
- [LastTestRequest](#BKMK_LastTestRequest)
- [LastTestResponse](#BKMK_LastTestResponse)
- [LastTestStartTime](#BKMK_LastTestStartTime)
- [LastTestTotalExecutionTime](#BKMK_LastTestTotalExecutionTime)
- [LastTestValidationStatus](#BKMK_LastTestValidationStatus)
- [MaxConcurrentConnections](#BKMK_MaxConcurrentConnections)
- [MinPollingIntervalInMinutes](#BKMK_MinPollingIntervalInMinutes)
- [MoveUndeliveredEmails](#BKMK_MoveUndeliveredEmails)
- [Name](#BKMK_Name)
- [OutgoingAuthenticationProtocol](#BKMK_OutgoingAuthenticationProtocol)
- [OutgoingAutoGrantDelegateAccess](#BKMK_OutgoingAutoGrantDelegateAccess)
- [OutgoingCredentialRetrieval](#BKMK_OutgoingCredentialRetrieval)
- [OutgoingPassword](#BKMK_OutgoingPassword)
- [OutgoingPortNumber](#BKMK_OutgoingPortNumber)
- [OutgoingServerLocation](#BKMK_OutgoingServerLocation)
- [OutgoingUseImpersonation](#BKMK_OutgoingUseImpersonation)
- [OutgoingUsername](#BKMK_OutgoingUsername)
- [OutgoingUseSSL](#BKMK_OutgoingUseSSL)
- [OwnerEmailAddress](#BKMK_OwnerEmailAddress)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [ProcessEmailsReceivedAfter](#BKMK_ProcessEmailsReceivedAfter)
- [SendEmailAlert](#BKMK_SendEmailAlert)
- [ServerType](#BKMK_ServerType)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [TimeoutMailboxConnection](#BKMK_TimeoutMailboxConnection)
- [TimeoutMailboxConnectionAfterAmount](#BKMK_TimeoutMailboxConnectionAfterAmount)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UseAutoDiscover](#BKMK_UseAutoDiscover)
- [UseDefaultTenantId](#BKMK_UseDefaultTenantId)
- [UseSameSettingsForOutgoingConnections](#BKMK_UseSameSettingsForOutgoingConnections)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_DefaultServerLocation"></a> DefaultServerLocation

**Description**: Type the default location of the server.<br />
**DisplayName**: Default Email Server Location<br />
**LogicalName**: defaultserverlocation<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2084


### <a name="BKMK_Description"></a> Description

**Description**: Type additional information that describes the email server profile.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_EmailServerProfileId"></a> EmailServerProfileId

**Description**: Unique identifier of the email server profile.<br />
**DisplayName**: EmailServerProfile<br />
**LogicalName**: emailserverprofileid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_EncodingCodePage"></a> EncodingCodePage

**Description**: Indicates the code page to use when encoding email content.<br />
**DisplayName**: Encoding Code Page<br />
**LogicalName**: encodingcodepage<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


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


### <a name="BKMK_ExchangeOnlineTenantId"></a> ExchangeOnlineTenantId

**Description**: Type the tenant ID of Exchange Online.<br />
**DisplayName**: Exchange Online Tenant Id<br />
**LogicalName**: exchangeonlinetenantid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 36


### <a name="BKMK_ExchangeVersion"></a> ExchangeVersion

**Description**: Select the version of Exchange that is on the email server.<br />
**DisplayName**: Exchange Version<br />
**LogicalName**: exchangeversion<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Exchange 2007
- **Value**: 1 **Label**: Exchange 2007 SP1
- **Value**: 2 **Label**: Exchange 2010
- **Value**: 3 **Label**: Exchange 2010 SP1
- **Value**: 4 **Label**: Exchange 2010 SP2
- **Value**: 5 **Label**: Exchange 2013



### <a name="BKMK_IncomingAuthenticationProtocol"></a> IncomingAuthenticationProtocol

**Description**: Select the incoming email authentication protocol that is used for connecting to the email server.<br />
**DisplayName**: Incoming Authentication Protocol<br />
**LogicalName**: incomingauthenticationprotocol<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Auto Detect
- **Value**: 1 **Label**: Negotiate
- **Value**: 2 **Label**: NTLM
- **Value**: 3 **Label**: Basic



### <a name="BKMK_IncomingCredentialRetrieval"></a> IncomingCredentialRetrieval

**Description**: Select how credentials will be retrieved for incoming email.<br />
**DisplayName**: Incoming Email Credential Retrieval<br />
**LogicalName**: incomingcredentialretrieval<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Credentials Specified by a User or Queue
- **Value**: 1 **Label**: Credentials Specified in Email Server Profile
- **Value**: 2 **Label**: Server to Server Authentication
- **Value**: 3 **Label**: Windows Integrated Authentication
- **Value**: 4 **Label**: Without Credentials (Anonymous)



### <a name="BKMK_IncomingPassword"></a> IncomingPassword

**Description**: Type the password for incoming email.<br />
**DisplayName**: Incoming Email Password<br />
**LogicalName**: incomingpassword<br />
**IsValidForForm**: True<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 250


### <a name="BKMK_IncomingPortNumber"></a> IncomingPortNumber

**Description**: Type the Exchange port number for incoming mail.<br />
**DisplayName**: Incoming Email Port<br />
**LogicalName**: incomingportnumber<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 65536<br />
**MinValue**: 0


### <a name="BKMK_IncomingServerLocation"></a> IncomingServerLocation

**Description**: Type the location of the server for incoming email.<br />
**DisplayName**: Incoming Email Server Location<br />
**LogicalName**: incomingserverlocation<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2084


### <a name="BKMK_IncomingUseImpersonation"></a> IncomingUseImpersonation

**Description**: Select whether to use impersonation to access the mailbox to process incoming emails.<br />
**DisplayName**: Use Impersonation for Incoming Email<br />
**LogicalName**: incominguseimpersonation<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IncomingUserName"></a> IncomingUserName

**Description**: Type the user name for incoming email.<br />
**DisplayName**: Incoming Email User Name<br />
**LogicalName**: incomingusername<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 250


### <a name="BKMK_IncomingUseSSL"></a> IncomingUseSSL

**Description**: Select whether to use the Secure Sockets Layer (SSL) protocol for incoming email.<br />
**DisplayName**: Use SSL for Incoming Email<br />
**LogicalName**: incomingusessl<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_LastAuthorizationStatus"></a> LastAuthorizationStatus

**Description**: Shows the last test authorization status of email server profile<br />
**DisplayName**: Last Test Authorization Status<br />
**LogicalName**: lastauthorizationstatus<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Failure
- **Value**: 1 **Label**: Success



### <a name="BKMK_LastCrmMessage"></a> LastCrmMessage

**Description**: Shows the Dynamics 365 message obtained during the Last Test<br />
**DisplayName**: Last Dynamics 365 Message<br />
**LogicalName**: lastcrmmessage<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2084


### <a name="BKMK_LastTestExecutionStatus"></a> LastTestExecutionStatus

**Description**: Shows the last test Execution status of email server profile<br />
**DisplayName**: Last Test Execution Status<br />
**LogicalName**: lasttestexecutionstatus<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Failure
- **Value**: 1 **Label**: Success
- **Value**: 2 **Label**: Warning



### <a name="BKMK_LastTestRequest"></a> LastTestRequest

**Description**: Shows the EWS Request created during the Last Test<br />
**DisplayName**: Last Test Request<br />
**LogicalName**: lasttestrequest<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2084


### <a name="BKMK_LastTestResponse"></a> LastTestResponse

**Description**: Shows the EWS Response obtained during the Last Test<br />
**DisplayName**: Last Test Response<br />
**LogicalName**: lasttestresponse<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2084


### <a name="BKMK_LastTestStartTime"></a> LastTestStartTime

**Description**: Shows the Last Test Start date and time<br />
**DisplayName**: Last Test Time<br />
**LogicalName**: lastteststarttime<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_LastTestTotalExecutionTime"></a> LastTestTotalExecutionTime

**Description**: Shows the Time taken while running the last test<br />
**DisplayName**: Last Test Time Taken<br />
**LogicalName**: lasttesttotalexecutiontime<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />


### <a name="BKMK_LastTestValidationStatus"></a> LastTestValidationStatus

**Description**: Shows the last test Validation status of email server profile<br />
**DisplayName**: Last Test Validation Status<br />
**LogicalName**: lasttestvalidationstatus<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Failure
- **Value**: 1 **Label**: Success



### <a name="BKMK_MaxConcurrentConnections"></a> MaxConcurrentConnections

**Description**: Maximum number of concurrent connections allowed to the email server per authenticated user.<br />
**DisplayName**: Maximum Concurrent Connections<br />
**LogicalName**: maxconcurrentconnections<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 65536<br />
**MinValue**: 1


### <a name="BKMK_MinPollingIntervalInMinutes"></a> MinPollingIntervalInMinutes

**Description**: Minimum polling interval, in minutes, for mailboxes that are associated with this email server profile.<br />
**DisplayName**: Minimum Polling Interval In Minutes<br />
**LogicalName**: minpollingintervalinminutes<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1440<br />
**MinValue**: 0


### <a name="BKMK_MoveUndeliveredEmails"></a> MoveUndeliveredEmails

**Description**: Indicates whether to move undelivered incoming emails to the Undeliverable folder in Microsoft Exchange.<br />
**DisplayName**: Move Undelivered Emails to the Undeliverable Folder<br />
**LogicalName**: moveundeliveredemails<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_Name"></a> Name

**Description**: Type a meaningful name for the email server profile. This name is displayed when you need to select an email server profile.<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OutgoingAuthenticationProtocol"></a> OutgoingAuthenticationProtocol

**Description**: Select the outgoing email authentication protocol that is used for connecting to the email server.<br />
**DisplayName**: Outgoing Authentication Protocol<br />
**LogicalName**: outgoingauthenticationprotocol<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Auto Detect
- **Value**: 1 **Label**: Negotiate
- **Value**: 2 **Label**: NTLM
- **Value**: 3 **Label**: Basic



### <a name="BKMK_OutgoingAutoGrantDelegateAccess"></a> OutgoingAutoGrantDelegateAccess

**Description**: Indicates whether the email connector will grant delegate access permissions to the accessing user when required while processing outgoing emails.<br />
**DisplayName**: Auto Grant Delegate Access for Outgoing Email.<br />
**LogicalName**: outgoingautograntdelegateaccess<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_OutgoingCredentialRetrieval"></a> OutgoingCredentialRetrieval

**Description**: Select how credentials will be retrieved for outgoing email.<br />
**DisplayName**: Outgoing Email Credential Retrieval<br />
**LogicalName**: outgoingcredentialretrieval<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Credentials Specified by a User or Queue
- **Value**: 1 **Label**: Credentials Specified in Email Server Profile
- **Value**: 2 **Label**: Server to Server Authentication
- **Value**: 3 **Label**: Windows Integrated Authentication
- **Value**: 4 **Label**: Without Credentials (Anonymous)



### <a name="BKMK_OutgoingPassword"></a> OutgoingPassword

**Description**: Type the password for outgoing email.<br />
**DisplayName**: Outgoing Email Password<br />
**LogicalName**: outgoingpassword<br />
**IsValidForForm**: True<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 250


### <a name="BKMK_OutgoingPortNumber"></a> OutgoingPortNumber

**Description**: Type the Exchange port number for outgoing mail.<br />
**DisplayName**: Outgoing Email Port<br />
**LogicalName**: outgoingportnumber<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 65536<br />
**MinValue**: 0


### <a name="BKMK_OutgoingServerLocation"></a> OutgoingServerLocation

**Description**: Type the location of the server for outgoing email.<br />
**DisplayName**: Outgoing Email Server Location<br />
**LogicalName**: outgoingserverlocation<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2084


### <a name="BKMK_OutgoingUseImpersonation"></a> OutgoingUseImpersonation

**Description**: Select whether to use impersonation for accessing the mailbox to process outgoing emails.<br />
**DisplayName**: Use Impersonation for Outgoing Email<br />
**LogicalName**: outgoinguseimpersonation<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_OutgoingUsername"></a> OutgoingUsername

**Description**: Type the user name for outgoing email.<br />
**DisplayName**: Outgoing Email User Name<br />
**LogicalName**: outgoingusername<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 250


### <a name="BKMK_OutgoingUseSSL"></a> OutgoingUseSSL

**Description**: Select whether to use the Secure Sockets Layer (SSL) protocol for outgoing email.<br />
**DisplayName**: Use SSL for Outgoing Email<br />
**LogicalName**: outgoingusessl<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_OwnerEmailAddress"></a> OwnerEmailAddress

**Description**: Email Server Profile Owner's email address<br />
**DisplayName**: Email Server Profile Owner's email address<br />
**LogicalName**: owneremailaddress<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


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


### <a name="BKMK_ProcessEmailsReceivedAfter"></a> ProcessEmailsReceivedAfter

**Description**: Shows the date and time after which email messages that are received will be processed for mailboxes associated with the email server profile.<br />
**DisplayName**: Process Emails Received After<br />
**LogicalName**: processemailsreceivedafter<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_SendEmailAlert"></a> SendEmailAlert

**Description**: Select whether to send an email alert if more than 50% of the mailboxes in this email server profile failed to synchronize in an hour period.<br />
**DisplayName**: Send an alert email to the owner of the email server profile reporting on major events<br />
**LogicalName**: sendemailalert<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_ServerType"></a> ServerType

**Description**: Select the profile's email server type.<br />
**DisplayName**: Email Server Type<br />
**LogicalName**: servertype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Exchange Server
- **Value**: 1 **Label**: Other (POP3/SMTP)
- **Value**: 2 **Label**: Exchange Server (Hybrid)
- **Value**: 3 **Label**: Exchange Online (Hybrid)



### <a name="BKMK_StateCode"></a> StateCode

**Description**: Shows whether the email server profile is active or inactive.<br />
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

**Description**: Select the email server profile's status.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Status<br />
**Options**:

- **Value**: 1 **Label**: Active **State**: 0
- **Value**: 2 **Label**: Inactive **State**: 1



### <a name="BKMK_TimeoutMailboxConnection"></a> TimeoutMailboxConnection

**Description**: Select whether to timeout a single mailbox.<br />
**DisplayName**: Timeout Mailbox Connection to Exchange<br />
**LogicalName**: timeoutmailboxconnection<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_TimeoutMailboxConnectionAfterAmount"></a> TimeoutMailboxConnectionAfterAmount

**Description**: Type the number of milliseconds to timeout a single mailbox. The upper limit is 100 seconds.<br />
**DisplayName**: Timeout a Single Mailbox Connection After this Amount of Milliseconds<br />
**LogicalName**: timeoutmailboxconnectionafteramount<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 100000<br />
**MinValue**: 0


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


### <a name="BKMK_UseAutoDiscover"></a> UseAutoDiscover

**Description**: Select whether to automatically discover the server location<br />
**DisplayName**: Auto Discover Server Location<br />
**LogicalName**: useautodiscover<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_UseDefaultTenantId"></a> UseDefaultTenantId

**Description**: Select whether to use the Exchange Online Tenant ID obtained from running Microsoft Azure PowerShell cmdlets (highly recommended). If you select No, you can edit this field manually<br />
**DisplayName**: Use Default Tenant Id<br />
**LogicalName**: usedefaulttenantid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_UseSameSettingsForOutgoingConnections"></a> UseSameSettingsForOutgoingConnections

**Description**: Select whether to use the same settings for incoming and outgoing connections.<br />
**DisplayName**: Use Same Settings for Outgoing Connection<br />
**LogicalName**: usesamesettingsforoutgoingconnections<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
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
- [EmailServerTypeName](#BKMK_EmailServerTypeName)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [IncomingPartnerApplication](#BKMK_IncomingPartnerApplication)
- [IncomingPartnerApplicationName](#BKMK_IncomingPartnerApplicationName)
- [IsIncomingPasswordSet](#BKMK_IsIncomingPasswordSet)
- [IsOutgoingPasswordSet](#BKMK_IsOutgoingPasswordSet)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OutgoingPartnerApplication](#BKMK_OutgoingPartnerApplication)
- [OutgoingPartnerApplicationName](#BKMK_OutgoingPartnerApplicationName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)


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


### <a name="BKMK_EmailServerTypeName"></a> EmailServerTypeName

**Description**: Email Server Type Name<br />
**DisplayName**: Email Server Type Name<br />
**LogicalName**: emailservertypename<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 250


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


### <a name="BKMK_IncomingPartnerApplication"></a> IncomingPartnerApplication

**Description**: Indicates the incoming partner application.<br />
**DisplayName**: Incoming Partner Application<br />
**LogicalName**: incomingpartnerapplication<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: partnerapplication


### <a name="BKMK_IncomingPartnerApplicationName"></a> IncomingPartnerApplicationName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: incomingpartnerapplicationname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_IsIncomingPasswordSet"></a> IsIncomingPasswordSet

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: isincomingpasswordset<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsOutgoingPasswordSet"></a> IsOutgoingPasswordSet

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: isoutgoingpasswordset<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


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

**Description**: Unique identifier of the organization associated with the record.<br />
**DisplayName**: Organization Id<br />
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
**MaxLength**: 100


### <a name="BKMK_OutgoingPartnerApplication"></a> OutgoingPartnerApplication

**Description**: Indicates the outgoing partner application.<br />
**DisplayName**: Outgoing Partner Application<br />
**LogicalName**: outgoingpartnerapplication<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: partnerapplication


### <a name="BKMK_OutgoingPartnerApplicationName"></a> OutgoingPartnerApplicationName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: outgoingpartnerapplicationname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


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
**MaxLength**: 100


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
**MaxLength**: 100


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
**MaxLength**: 100


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
**Targets**: 


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: Version number of the email server profile.<br />
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

- [emailserverprofile_mailbox](#BKMK_emailserverprofile_mailbox)
- [EmailServerProfile_SyncErrors](#BKMK_EmailServerProfile_SyncErrors)
- [tracelog_EmailServerProfile](#BKMK_tracelog_EmailServerProfile)
- [emailserverprofile_bulkdeletefailures](#BKMK_emailserverprofile_bulkdeletefailures)
- [emailserverprofile_asyncoperations](#BKMK_emailserverprofile_asyncoperations)
- [EmailServerProfile_Annotation](#BKMK_EmailServerProfile_Annotation)
- [emailserverprofile_duplicatebaserecord](#BKMK_emailserverprofile_duplicatebaserecord)
- [emailserverprofile_duplicatematchingrecord](#BKMK_emailserverprofile_duplicatematchingrecord)
- [EmailServerProfile_Organization](#BKMK_EmailServerProfile_Organization)


### <a name="BKMK_emailserverprofile_mailbox"></a> emailserverprofile_mailbox

Same as mailbox entity [emailserverprofile_mailbox](mailbox.md#BKMK_emailserverprofile_mailbox) Many-To-One relationship.

**ReferencingEntity**: mailbox<br />
**ReferencingAttribute**: emailserverprofile<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: emailserverprofile_mailbox<br />
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


### <a name="BKMK_EmailServerProfile_SyncErrors"></a> EmailServerProfile_SyncErrors

Same as syncerror entity [EmailServerProfile_SyncErrors](syncerror.md#BKMK_EmailServerProfile_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: EmailServerProfile_SyncErrors<br />
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


### <a name="BKMK_tracelog_EmailServerProfile"></a> tracelog_EmailServerProfile

Same as tracelog entity [tracelog_EmailServerProfile](tracelog.md#BKMK_tracelog_EmailServerProfile) Many-To-One relationship.

**ReferencingEntity**: tracelog<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: tracelog_EmailServerProfile<br />
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


### <a name="BKMK_emailserverprofile_bulkdeletefailures"></a> emailserverprofile_bulkdeletefailures

Same as bulkdeletefailure entity [emailserverprofile_bulkdeletefailures](bulkdeletefailure.md#BKMK_emailserverprofile_bulkdeletefailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: emailserverprofile_bulkdeletefailures<br />
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


### <a name="BKMK_emailserverprofile_asyncoperations"></a> emailserverprofile_asyncoperations

Same as asyncoperation entity [emailserverprofile_asyncoperations](asyncoperation.md#BKMK_emailserverprofile_asyncoperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: emailserverprofile_asyncoperations<br />
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


### <a name="BKMK_EmailServerProfile_Annotation"></a> EmailServerProfile_Annotation

Same as annotation entity [EmailServerProfile_Annotation](annotation.md#BKMK_EmailServerProfile_Annotation) Many-To-One relationship.

**ReferencingEntity**: annotation<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: EmailServerProfile_Annotation<br />
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


### <a name="BKMK_emailserverprofile_duplicatebaserecord"></a> emailserverprofile_duplicatebaserecord

Same as duplicaterecord entity [emailserverprofile_duplicatebaserecord](duplicaterecord.md#BKMK_emailserverprofile_duplicatebaserecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: baserecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: emailserverprofile_duplicatebaserecord<br />
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


### <a name="BKMK_emailserverprofile_duplicatematchingrecord"></a> emailserverprofile_duplicatematchingrecord

Same as duplicaterecord entity [emailserverprofile_duplicatematchingrecord](duplicaterecord.md#BKMK_emailserverprofile_duplicatematchingrecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: duplicaterecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: emailserverprofile_duplicatematchingrecord<br />
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


### <a name="BKMK_EmailServerProfile_Organization"></a> EmailServerProfile_Organization

Same as organization entity [EmailServerProfile_Organization](organization.md#BKMK_EmailServerProfile_Organization) Many-To-One relationship.

**ReferencingEntity**: organization<br />
**ReferencingAttribute**: defaultemailserverprofileid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: EmailServerProfile_Organization<br />
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [lk_emailserverprofile_createdonbehalfby](#BKMK_lk_emailserverprofile_createdonbehalfby)
- [lk_emailserverprofile_modifiedonbehalfby](#BKMK_lk_emailserverprofile_modifiedonbehalfby)
- [organization_emailserverprofile](#BKMK_organization_emailserverprofile)
- [team_emailserverprofile](#BKMK_team_emailserverprofile)
- [lk_emailserverprofile_modifiedby](#BKMK_lk_emailserverprofile_modifiedby)
- [lk_emailserverprofile_createdby](#BKMK_lk_emailserverprofile_createdby)
- [business_unit_emailserverprofile](#BKMK_business_unit_emailserverprofile)


### <a name="BKMK_lk_emailserverprofile_createdonbehalfby"></a> lk_emailserverprofile_createdonbehalfby

See systemuser Entity [lk_emailserverprofile_createdonbehalfby](systemuser.md#BKMK_lk_emailserverprofile_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_emailserverprofile_modifiedonbehalfby"></a> lk_emailserverprofile_modifiedonbehalfby

See systemuser Entity [lk_emailserverprofile_modifiedonbehalfby](systemuser.md#BKMK_lk_emailserverprofile_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_emailserverprofile"></a> organization_emailserverprofile

See organization Entity [organization_emailserverprofile](organization.md#BKMK_organization_emailserverprofile) One-To-Many relationship.

### <a name="BKMK_team_emailserverprofile"></a> team_emailserverprofile

See team Entity [team_emailserverprofile](team.md#BKMK_team_emailserverprofile) One-To-Many relationship.

### <a name="BKMK_lk_emailserverprofile_modifiedby"></a> lk_emailserverprofile_modifiedby

See systemuser Entity [lk_emailserverprofile_modifiedby](systemuser.md#BKMK_lk_emailserverprofile_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_emailserverprofile_createdby"></a> lk_emailserverprofile_createdby

See systemuser Entity [lk_emailserverprofile_createdby](systemuser.md#BKMK_lk_emailserverprofile_createdby) One-To-Many relationship.

### <a name="BKMK_business_unit_emailserverprofile"></a> business_unit_emailserverprofile

See businessunit Entity [business_unit_emailserverprofile](businessunit.md#BKMK_business_unit_emailserverprofile) One-To-Many relationship.
emailserverprofile

