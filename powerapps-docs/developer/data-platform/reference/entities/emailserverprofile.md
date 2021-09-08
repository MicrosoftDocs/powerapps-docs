---
title: "EmailServerProfile table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the EmailServerProfile table/entity."
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

# EmailServerProfile table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Holds the Email Server Profiles of an organization


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/emailserverprofiles(*emailserverprofileid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/emailserverprofiles<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/emailserverprofiles(*emailserverprofileid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/emailserverprofiles(*emailserverprofileid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/emailserverprofiles<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/emailserverprofiles(*emailserverprofileid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/emailserverprofiles(*emailserverprofileid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|EmailServerProfiles|
|DisplayCollectionName|Email Server Profiles|
|DisplayName|Email Server Profile|
|EntitySetName|emailserverprofiles|
|IsBPFEntity|False|
|LogicalCollectionName|emailserverprofiles|
|LogicalName|emailserverprofile|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|emailserverprofileid|
|PrimaryNameAttribute|name|
|SchemaName|EmailServerProfile|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AadResourceId](#BKMK_AadResourceId)
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
- [keyvaultreferenceid](#BKMK_keyvaultreferenceid)
- [LastAuthorizationStatus](#BKMK_LastAuthorizationStatus)
- [LastCrmMessage](#BKMK_LastCrmMessage)
- [LastTestExecutionStatus](#BKMK_LastTestExecutionStatus)
- [LastTestRequest](#BKMK_LastTestRequest)
- [LastTestResponse](#BKMK_LastTestResponse)
- [LastTestStartTime](#BKMK_LastTestStartTime)
- [LastTestTotalExecutionTime](#BKMK_LastTestTotalExecutionTime)
- [LastTestValidationStatus](#BKMK_LastTestValidationStatus)
- [managedidentityid](#BKMK_managedidentityid)
- [MaxConcurrentConnections](#BKMK_MaxConcurrentConnections)
- [MinPollingIntervalInMinutes](#BKMK_MinPollingIntervalInMinutes)
- [MoveUndeliveredEmails](#BKMK_MoveUndeliveredEmails)
- [Name](#BKMK_Name)
- [OauthClientId](#BKMK_OauthClientId)
- [OauthClientSecret](#BKMK_OauthClientSecret)
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


### <a name="BKMK_AadResourceId"></a> AadResourceId

**Added by**: msft_ServerSideSync_Extensions Solution

|Property|Value|
|--------|-----|
|Description|AAD ResourceId used for OAuth athentication scheme|
|DisplayName|AAD ResourceId|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|aadresourceid|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_DefaultServerLocation"></a> DefaultServerLocation

|Property|Value|
|--------|-----|
|Description|Type the default location of the server.|
|DisplayName|Default Email Server Location|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|defaultserverlocation|
|MaxLength|2084|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Type additional information that describes the email server profile.|
|DisplayName|Description|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_EmailServerProfileId"></a> EmailServerProfileId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the email server profile.|
|DisplayName|EmailServerProfile|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|emailserverprofileid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_EncodingCodePage"></a> EncodingCodePage

|Property|Value|
|--------|-----|
|Description|Indicates the code page to use when encoding email content.|
|DisplayName|Encoding Code Page|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|encodingcodepage|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EntityImage"></a> EntityImage

|Property|Value|
|--------|-----|
|Description|The default image for the entity.|
|DisplayName|Entity Image|
|IsPrimaryImage|True|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimage|
|MaxHeight|144|
|MaxWidth|144|
|RequiredLevel|None|
|Type|Image|


### <a name="BKMK_ExchangeOnlineTenantId"></a> ExchangeOnlineTenantId

|Property|Value|
|--------|-----|
|Description|Type the tenant ID of Exchange Online.|
|DisplayName|Exchange Online Tenant Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangeonlinetenantid|
|MaxLength|36|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ExchangeVersion"></a> ExchangeVersion

|Property|Value|
|--------|-----|
|Description|Select the version of Exchange that is on the email server.|
|DisplayName|Exchange Version|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangeversion|
|RequiredLevel|None|
|Type|Picklist|

#### ExchangeVersion Choices/Options

|Value|Label|
|-----|-----|
|0|Exchange 2007|
|1|Exchange 2007 SP1|
|2|Exchange 2010|
|3|Exchange 2010 SP1|
|4|Exchange 2010 SP2|
|5|Exchange 2013|



### <a name="BKMK_IncomingAuthenticationProtocol"></a> IncomingAuthenticationProtocol

|Property|Value|
|--------|-----|
|Description|Select the incoming email authentication protocol that is used for connecting to the email server.|
|DisplayName|Incoming Authentication Protocol|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|incomingauthenticationprotocol|
|RequiredLevel|None|
|Type|Picklist|

#### IncomingAuthenticationProtocol Choices/Options

|Value|Label|
|-----|-----|
|0|Auto Detect|
|1|Negotiate|
|2|NTLM|
|3|Basic|
|4|OAuth|



### <a name="BKMK_IncomingCredentialRetrieval"></a> IncomingCredentialRetrieval

|Property|Value|
|--------|-----|
|Description|Select how credentials will be retrieved for incoming email.|
|DisplayName|Incoming Email Credential Retrieval|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|incomingcredentialretrieval|
|RequiredLevel|None|
|Type|Picklist|

#### IncomingCredentialRetrieval Choices/Options

|Value|Label|
|-----|-----|
|0|Credentials Specified by a User or Queue|
|1|Credentials Specified in Email Server Profile|
|2|Server to Server Authentication|
|3|Windows Integrated Authentication|
|4|Without Credentials (Anonymous)|
|5|Gmail OAuth|
|6|Exchange Hybrid Modern Auth (HMA)|
|7|Azure Active Directory OAuth|



### <a name="BKMK_IncomingPassword"></a> IncomingPassword

|Property|Value|
|--------|-----|
|Description|Type the password for incoming email.|
|DisplayName|Incoming Email Password|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|False|
|LogicalName|incomingpassword|
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IncomingPortNumber"></a> IncomingPortNumber

|Property|Value|
|--------|-----|
|Description|Type the Exchange port number for incoming mail.|
|DisplayName|Incoming Email Port|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|incomingportnumber|
|MaxValue|65536|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_IncomingServerLocation"></a> IncomingServerLocation

|Property|Value|
|--------|-----|
|Description|Type the location of the server for incoming email.|
|DisplayName|Incoming Email Server Location|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|incomingserverlocation|
|MaxLength|2084|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IncomingUseImpersonation"></a> IncomingUseImpersonation

|Property|Value|
|--------|-----|
|Description|Select whether to use impersonation to access the mailbox to process incoming emails.|
|DisplayName|Use Impersonation for Incoming Email|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|incominguseimpersonation|
|RequiredLevel|None|
|Type|Boolean|

#### IncomingUseImpersonation Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IncomingUserName"></a> IncomingUserName

|Property|Value|
|--------|-----|
|Description|Type the user name for incoming email.|
|DisplayName|Incoming Email User Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|incomingusername|
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IncomingUseSSL"></a> IncomingUseSSL

|Property|Value|
|--------|-----|
|Description|Select whether to use the Secure Sockets Layer (SSL) protocol for incoming email.|
|DisplayName|Use SSL for Incoming Email|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|incomingusessl|
|RequiredLevel|None|
|Type|Boolean|

#### IncomingUseSSL Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: True



### <a name="BKMK_keyvaultreferenceid"></a> keyvaultreferenceid

**Added by**: msft_ServerSideSync_Extensions Solution

|Property|Value|
|--------|-----|
|Description|The Azure Key Vault reference id|
|DisplayName|Key Vault Reference Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|keyvaultreferenceid|
|RequiredLevel|None|
|Targets|keyvaultreference|
|Type|Lookup|


### <a name="BKMK_LastAuthorizationStatus"></a> LastAuthorizationStatus

|Property|Value|
|--------|-----|
|Description|Shows the last test authorization status of email server profile|
|DisplayName|Last Test Authorization Status|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|lastauthorizationstatus|
|RequiredLevel|None|
|Type|Picklist|

#### LastAuthorizationStatus Choices/Options

|Value|Label|
|-----|-----|
|0|Failure|
|1|Success|



### <a name="BKMK_LastCrmMessage"></a> LastCrmMessage

|Property|Value|
|--------|-----|
|Description|Shows the Dynamics 365 message obtained during the Last Test|
|DisplayName|Last Dynamics 365 Message|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastcrmmessage|
|MaxLength|2084|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_LastTestExecutionStatus"></a> LastTestExecutionStatus

|Property|Value|
|--------|-----|
|Description|Shows the last test Execution status of email server profile|
|DisplayName|Last Test Execution Status|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|lasttestexecutionstatus|
|RequiredLevel|None|
|Type|Picklist|

#### LastTestExecutionStatus Choices/Options

|Value|Label|
|-----|-----|
|0|Failure|
|1|Success|
|2|Warning|



### <a name="BKMK_LastTestRequest"></a> LastTestRequest

|Property|Value|
|--------|-----|
|Description|Shows the EWS Request created during the Last Test|
|DisplayName|Last Test Request|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lasttestrequest|
|MaxLength|2084|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_LastTestResponse"></a> LastTestResponse

|Property|Value|
|--------|-----|
|Description|Shows the EWS Response obtained during the Last Test|
|DisplayName|Last Test Response|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lasttestresponse|
|MaxLength|2084|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_LastTestStartTime"></a> LastTestStartTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the Last Test Start date and time|
|DisplayName|Last Test Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastteststarttime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_LastTestTotalExecutionTime"></a> LastTestTotalExecutionTime

|Property|Value|
|--------|-----|
|Description|Shows the Time taken while running the last test|
|DisplayName|Last Test Time Taken|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lasttesttotalexecutiontime|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|


### <a name="BKMK_LastTestValidationStatus"></a> LastTestValidationStatus

|Property|Value|
|--------|-----|
|Description|Shows the last test Validation status of email server profile|
|DisplayName|Last Test Validation Status|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|lasttestvalidationstatus|
|RequiredLevel|None|
|Type|Picklist|

#### LastTestValidationStatus Choices/Options

|Value|Label|
|-----|-----|
|0|Failure|
|1|Success|



### <a name="BKMK_managedidentityid"></a> managedidentityid

**Added by**: msft_ServerSideSync_Extensions Solution

|Property|Value|
|--------|-----|
|Description|The managed identity id|
|DisplayName|Managed Identity Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|managedidentityid|
|RequiredLevel|None|
|Targets|managedidentity|
|Type|Lookup|


### <a name="BKMK_MaxConcurrentConnections"></a> MaxConcurrentConnections

|Property|Value|
|--------|-----|
|Description|Maximum number of concurrent connections allowed to the email server per authenticated user.|
|DisplayName|Maximum Concurrent Connections|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|maxconcurrentconnections|
|MaxValue|300|
|MinValue|1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_MinPollingIntervalInMinutes"></a> MinPollingIntervalInMinutes

|Property|Value|
|--------|-----|
|Description|Minimum polling interval, in minutes, for mailboxes that are associated with this email server profile.|
|DisplayName|Minimum Polling Interval In Minutes|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|minpollingintervalinminutes|
|MaxValue|1440|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_MoveUndeliveredEmails"></a> MoveUndeliveredEmails

|Property|Value|
|--------|-----|
|Description|Indicates whether to move undelivered incoming emails to the Undeliverable folder in Microsoft Exchange.|
|DisplayName|Move Undelivered Emails to the Undeliverable Folder|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|moveundeliveredemails|
|RequiredLevel|None|
|Type|Boolean|

#### MoveUndeliveredEmails Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Type a meaningful name for the email server profile. This name is displayed when you need to select an email server profile.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_OauthClientId"></a> OauthClientId

|Property|Value|
|--------|-----|
|Description|ClientId used for OAuth athentication scheme|
|DisplayName|Oauth ClientId|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|oauthclientid|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OauthClientSecret"></a> OauthClientSecret

|Property|Value|
|--------|-----|
|Description|Client secret used for the OAuth authentication scheme|
|DisplayName|OAuth Client Secret|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|False|
|LogicalName|oauthclientsecret|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OutgoingAuthenticationProtocol"></a> OutgoingAuthenticationProtocol

|Property|Value|
|--------|-----|
|Description|Select the outgoing email authentication protocol that is used for connecting to the email server.|
|DisplayName|Outgoing Authentication Protocol|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|outgoingauthenticationprotocol|
|RequiredLevel|None|
|Type|Picklist|

#### OutgoingAuthenticationProtocol Choices/Options

|Value|Label|
|-----|-----|
|0|Auto Detect|
|1|Negotiate|
|2|NTLM|
|3|Basic|
|4|OAuth|



### <a name="BKMK_OutgoingAutoGrantDelegateAccess"></a> OutgoingAutoGrantDelegateAccess

|Property|Value|
|--------|-----|
|Description|Indicates whether the email connector will grant delegate access permissions to the accessing user when required while processing outgoing emails.|
|DisplayName|Auto Grant Delegate Access for Outgoing Email.|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|outgoingautograntdelegateaccess|
|RequiredLevel|None|
|Type|Boolean|

#### OutgoingAutoGrantDelegateAccess Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_OutgoingCredentialRetrieval"></a> OutgoingCredentialRetrieval

|Property|Value|
|--------|-----|
|Description|Select how credentials will be retrieved for outgoing email.|
|DisplayName|Outgoing Email Credential Retrieval|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|outgoingcredentialretrieval|
|RequiredLevel|None|
|Type|Picklist|

#### OutgoingCredentialRetrieval Choices/Options

|Value|Label|
|-----|-----|
|0|Credentials Specified by a User or Queue|
|1|Credentials Specified in Email Server Profile|
|2|Server to Server Authentication|
|3|Windows Integrated Authentication|
|4|Without Credentials (Anonymous)|
|5|Gmail OAuth|
|6|Exchange Hybrid Modern Auth (HMA)|
|7|Azure Active Directory OAuth|



### <a name="BKMK_OutgoingPassword"></a> OutgoingPassword

|Property|Value|
|--------|-----|
|Description|Type the password for outgoing email.|
|DisplayName|Outgoing Email Password|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|False|
|LogicalName|outgoingpassword|
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OutgoingPortNumber"></a> OutgoingPortNumber

|Property|Value|
|--------|-----|
|Description|Type the Exchange port number for outgoing mail.|
|DisplayName|Outgoing Email Port|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|outgoingportnumber|
|MaxValue|65536|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_OutgoingServerLocation"></a> OutgoingServerLocation

|Property|Value|
|--------|-----|
|Description|Type the location of the server for outgoing email.|
|DisplayName|Outgoing Email Server Location|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|outgoingserverlocation|
|MaxLength|2084|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OutgoingUseImpersonation"></a> OutgoingUseImpersonation

|Property|Value|
|--------|-----|
|Description|Select whether to use impersonation for accessing the mailbox to process outgoing emails.|
|DisplayName|Use Impersonation for Outgoing Email|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|outgoinguseimpersonation|
|RequiredLevel|None|
|Type|Boolean|

#### OutgoingUseImpersonation Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_OutgoingUsername"></a> OutgoingUsername

|Property|Value|
|--------|-----|
|Description|Type the user name for outgoing email.|
|DisplayName|Outgoing Email User Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|outgoingusername|
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OutgoingUseSSL"></a> OutgoingUseSSL

|Property|Value|
|--------|-----|
|Description|Select whether to use the Secure Sockets Layer (SSL) protocol for outgoing email.|
|DisplayName|Use SSL for Outgoing Email|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|outgoingusessl|
|RequiredLevel|None|
|Type|Boolean|

#### OutgoingUseSSL Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: True



### <a name="BKMK_OwnerEmailAddress"></a> OwnerEmailAddress

|Property|Value|
|--------|-----|
|Description|Email Server Profile Owner's email address|
|DisplayName|Email Server Profile Owner's email address|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneremailaddress|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.|
|DisplayName|Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Targets|systemuser,team|
|Type|Owner|


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|--------|-----|
|Description|Owner Id Type|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_ProcessEmailsReceivedAfter"></a> ProcessEmailsReceivedAfter

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time after which email messages that are received will be processed for mailboxes associated with the email server profile.|
|DisplayName|Process Emails Received After|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|processemailsreceivedafter|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_SendEmailAlert"></a> SendEmailAlert

|Property|Value|
|--------|-----|
|Description|Select whether to send an email alert if more than 50% of the mailboxes in this email server profile failed to synchronize in an hour period.|
|DisplayName|Send an alert email to the owner of the email server profile reporting on major events|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|sendemailalert|
|RequiredLevel|None|
|Type|Boolean|

#### SendEmailAlert Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_ServerType"></a> ServerType

|Property|Value|
|--------|-----|
|Description|Select the profile's email server type.|
|DisplayName|Email Server Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|servertype|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### ServerType Choices/Options

|Value|Label|
|-----|-----|
|0|Exchange Server|
|1|Other (POP3/SMTP)|
|2|Exchange Server (Hybrid)|
|3|Exchange Online (Hybrid)|
|4|IMAP/SMTP|



### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|--------|-----|
|Description|Shows whether the email server profile is active or inactive.|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### StateCode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|1|Active|
|1|Inactive|2|Inactive|



### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|--------|-----|
|Description|Select the email server profile's status.|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### StatusCode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Active|0|
|2|Inactive|1|



### <a name="BKMK_TimeoutMailboxConnection"></a> TimeoutMailboxConnection

|Property|Value|
|--------|-----|
|Description|Select whether to timeout a single mailbox.|
|DisplayName|Timeout Mailbox Connection to Exchange|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|timeoutmailboxconnection|
|RequiredLevel|None|
|Type|Boolean|

#### TimeoutMailboxConnection Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: True



### <a name="BKMK_TimeoutMailboxConnectionAfterAmount"></a> TimeoutMailboxConnectionAfterAmount

|Property|Value|
|--------|-----|
|Description|Type the number of milliseconds to timeout a single mailbox. The upper limit is 100 seconds.|
|DisplayName|Timeout a Single Mailbox Connection After this Amount of Milliseconds|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|timeoutmailboxconnectionafteramount|
|MaxValue|100000|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


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


### <a name="BKMK_UseAutoDiscover"></a> UseAutoDiscover

|Property|Value|
|--------|-----|
|Description|Select whether to automatically discover the server location|
|DisplayName|Auto Discover Server Location|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|useautodiscover|
|RequiredLevel|None|
|Type|Boolean|

#### UseAutoDiscover Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_UseDefaultTenantId"></a> UseDefaultTenantId

|Property|Value|
|--------|-----|
|Description|Select whether to use the Exchange Online Tenant ID obtained from running Microsoft Azure PowerShell cmdlets (highly recommended). If you select No, you can edit this field manually|
|DisplayName|Use Default Tenant Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|usedefaulttenantid|
|RequiredLevel|None|
|Type|Boolean|

#### UseDefaultTenantId Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: True



### <a name="BKMK_UseSameSettingsForOutgoingConnections"></a> UseSameSettingsForOutgoingConnections

|Property|Value|
|--------|-----|
|Description|Select whether to use the same settings for incoming and outgoing connections.|
|DisplayName|Use Same Settings for Outgoing Connection|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|usesamesettingsforoutgoingconnections|
|RequiredLevel|None|
|Type|Boolean|

#### UseSameSettingsForOutgoingConnections Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

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
- [EmailServerTypeName](#BKMK_EmailServerTypeName)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [IncomingPartnerApplication](#BKMK_IncomingPartnerApplication)
- [IncomingPartnerApplicationName](#BKMK_IncomingPartnerApplicationName)
- [IsIncomingPasswordSet](#BKMK_IsIncomingPasswordSet)
- [IsOauthClientSecretSet](#BKMK_IsOauthClientSecretSet)
- [IsOutgoingPasswordSet](#BKMK_IsOutgoingPasswordSet)
- [keyvaultreferenceidName](#BKMK_keyvaultreferenceidName)
- [managedidentityidName](#BKMK_managedidentityidName)
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

|Property|Value|
|--------|-----|
|Description|Shows who created the record.|
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
|Description|Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
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
|Description|Shows who created the record on behalf of another user.|
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


### <a name="BKMK_EmailServerTypeName"></a> EmailServerTypeName

|Property|Value|
|--------|-----|
|Description|Email Server Type Name|
|DisplayName|Email Server Type Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|emailservertypename|
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EntityImage_Timestamp"></a> EntityImage_Timestamp

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimage_timestamp|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|


### <a name="BKMK_EntityImage_URL"></a> EntityImage_URL

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimage_url|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EntityImageId"></a> EntityImageId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Entity Image Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimageid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_IncomingPartnerApplication"></a> IncomingPartnerApplication

|Property|Value|
|--------|-----|
|Description|Indicates the incoming partner application.|
|DisplayName|Incoming Partner Application|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|incomingpartnerapplication|
|RequiredLevel|None|
|Targets|partnerapplication|
|Type|Lookup|


### <a name="BKMK_IncomingPartnerApplicationName"></a> IncomingPartnerApplicationName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|incomingpartnerapplicationname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IsIncomingPasswordSet"></a> IsIncomingPasswordSet

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isincomingpasswordset|
|RequiredLevel|None|
|Type|Boolean|

#### IsIncomingPasswordSet Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsOauthClientSecretSet"></a> IsOauthClientSecretSet

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isoauthclientsecretset|
|RequiredLevel|None|
|Type|Boolean|

#### IsOauthClientSecretSet Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsOutgoingPasswordSet"></a> IsOutgoingPasswordSet

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isoutgoingpasswordset|
|RequiredLevel|None|
|Type|Boolean|

#### IsOutgoingPasswordSet Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_keyvaultreferenceidName"></a> keyvaultreferenceidName

**Added by**: msft_ServerSideSync_Extensions Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|keyvaultreferenceidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_managedidentityidName"></a> managedidentityidName

**Added by**: msft_ServerSideSync_Extensions Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|managedidentityidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Shows who last updated the record.|
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
|Description|Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
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
|Description|Shows who last updated the record on behalf of another user.|
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
|Description|Unique identifier of the organization associated with the record.|
|DisplayName|Organization Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|SystemRequired|
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


### <a name="BKMK_OutgoingPartnerApplication"></a> OutgoingPartnerApplication

|Property|Value|
|--------|-----|
|Description|Indicates the outgoing partner application.|
|DisplayName|Outgoing Partner Application|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|outgoingpartnerapplication|
|RequiredLevel|None|
|Targets|partnerapplication|
|Type|Lookup|


### <a name="BKMK_OutgoingPartnerApplicationName"></a> OutgoingPartnerApplicationName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|outgoingpartnerapplicationname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|--------|-----|
|Description|Name of the owner|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|--------|-----|
|Description|Yomi name of the owner|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|--------|-----|
|Description|Select the business unit that owns the record.|
|DisplayName|Owning Business Unit|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningBusinessUnitName"></a> OwningBusinessUnitName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunitname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|--------|-----|
|Description|Unique identifier for the team that owns the record.|
|DisplayName|Owning Team|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteam|
|RequiredLevel|None|
|Targets|team|
|Type|Lookup|


### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|--------|-----|
|Description|Unique identifier for the user that owns the record.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets||
|Type|Lookup|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|Version number of the email server profile.|
|DisplayName|Version Number|
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

Same as mailbox table [emailserverprofile_mailbox](mailbox.md#BKMK_emailserverprofile_mailbox) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailbox|
|ReferencingAttribute|emailserverprofile|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|emailserverprofile_mailbox|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_EmailServerProfile_SyncErrors"></a> EmailServerProfile_SyncErrors

Same as syncerror table [EmailServerProfile_SyncErrors](syncerror.md#BKMK_EmailServerProfile_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|EmailServerProfile_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_tracelog_EmailServerProfile"></a> tracelog_EmailServerProfile

Same as tracelog table [tracelog_EmailServerProfile](tracelog.md#BKMK_tracelog_EmailServerProfile) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|tracelog|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|tracelog_EmailServerProfile|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_emailserverprofile_bulkdeletefailures"></a> emailserverprofile_bulkdeletefailures

Same as bulkdeletefailure table [emailserverprofile_bulkdeletefailures](bulkdeletefailure.md#BKMK_emailserverprofile_bulkdeletefailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|emailserverprofile_bulkdeletefailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_emailserverprofile_asyncoperations"></a> emailserverprofile_asyncoperations

Same as asyncoperation table [emailserverprofile_asyncoperations](asyncoperation.md#BKMK_emailserverprofile_asyncoperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|emailserverprofile_asyncoperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_EmailServerProfile_Annotation"></a> EmailServerProfile_Annotation

Same as annotation table [EmailServerProfile_Annotation](annotation.md#BKMK_EmailServerProfile_Annotation) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|EmailServerProfile_Annotation|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_emailserverprofile_duplicatebaserecord"></a> emailserverprofile_duplicatebaserecord

Same as duplicaterecord table [emailserverprofile_duplicatebaserecord](duplicaterecord.md#BKMK_emailserverprofile_duplicatebaserecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|emailserverprofile_duplicatebaserecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_emailserverprofile_duplicatematchingrecord"></a> emailserverprofile_duplicatematchingrecord

Same as duplicaterecord table [emailserverprofile_duplicatematchingrecord](duplicaterecord.md#BKMK_emailserverprofile_duplicatematchingrecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|emailserverprofile_duplicatematchingrecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_EmailServerProfile_Organization"></a> EmailServerProfile_Organization

Same as organization table [EmailServerProfile_Organization](organization.md#BKMK_EmailServerProfile_Organization) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|organization|
|ReferencingAttribute|defaultemailserverprofileid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|EmailServerProfile_Organization|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_emailserverprofile_createdonbehalfby](#BKMK_lk_emailserverprofile_createdonbehalfby)
- [lk_emailserverprofile_modifiedonbehalfby](#BKMK_lk_emailserverprofile_modifiedonbehalfby)
- [organization_emailserverprofile](#BKMK_organization_emailserverprofile)
- [team_emailserverprofile](#BKMK_team_emailserverprofile)
- [lk_emailserverprofile_modifiedby](#BKMK_lk_emailserverprofile_modifiedby)
- [lk_emailserverprofile_createdby](#BKMK_lk_emailserverprofile_createdby)
- [business_unit_emailserverprofile](#BKMK_business_unit_emailserverprofile)
- [keyvaultreference_emailserverprofile_keyvaultreferenceid](#BKMK_keyvaultreference_emailserverprofile_keyvaultreferenceid)
- [managedidentity_emailserverprofile_managedidentityid](#BKMK_managedidentity_emailserverprofile_managedidentityid)


### <a name="BKMK_lk_emailserverprofile_createdonbehalfby"></a> lk_emailserverprofile_createdonbehalfby

See systemuser Table [lk_emailserverprofile_createdonbehalfby](systemuser.md#BKMK_lk_emailserverprofile_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_emailserverprofile_modifiedonbehalfby"></a> lk_emailserverprofile_modifiedonbehalfby

See systemuser Table [lk_emailserverprofile_modifiedonbehalfby](systemuser.md#BKMK_lk_emailserverprofile_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_emailserverprofile"></a> organization_emailserverprofile

See organization Table [organization_emailserverprofile](organization.md#BKMK_organization_emailserverprofile) One-To-Many relationship.

### <a name="BKMK_team_emailserverprofile"></a> team_emailserverprofile

See team Table [team_emailserverprofile](team.md#BKMK_team_emailserverprofile) One-To-Many relationship.

### <a name="BKMK_lk_emailserverprofile_modifiedby"></a> lk_emailserverprofile_modifiedby

See systemuser Table [lk_emailserverprofile_modifiedby](systemuser.md#BKMK_lk_emailserverprofile_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_emailserverprofile_createdby"></a> lk_emailserverprofile_createdby

See systemuser Table [lk_emailserverprofile_createdby](systemuser.md#BKMK_lk_emailserverprofile_createdby) One-To-Many relationship.

### <a name="BKMK_business_unit_emailserverprofile"></a> business_unit_emailserverprofile

See businessunit Table [business_unit_emailserverprofile](businessunit.md#BKMK_business_unit_emailserverprofile) One-To-Many relationship.

### <a name="BKMK_keyvaultreference_emailserverprofile_keyvaultreferenceid"></a> keyvaultreference_emailserverprofile_keyvaultreferenceid

**Added by**: ManagedIdentityExtensions Solution

See keyvaultreference Table [keyvaultreference_emailserverprofile_keyvaultreferenceid](keyvaultreference.md#BKMK_keyvaultreference_emailserverprofile_keyvaultreferenceid) One-To-Many relationship.

### <a name="BKMK_managedidentity_emailserverprofile_managedidentityid"></a> managedidentity_emailserverprofile_managedidentityid

**Added by**: ManagedIdentityExtensions Solution

See managedidentity Table [managedidentity_emailserverprofile_managedidentityid](managedidentity.md#BKMK_managedidentity_emailserverprofile_managedidentityid) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.emailserverprofile?text=emailserverprofile EntityType" />