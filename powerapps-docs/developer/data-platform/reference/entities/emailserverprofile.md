---
title: "Email Server Profile (EmailServerProfile) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Email Server Profile (EmailServerProfile) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Email Server Profile (EmailServerProfile) table/entity reference (Microsoft Dataverse)

Holds the Email Server Profiles of an organization

## Messages

The following table lists the messages for the Email Server Profile (EmailServerProfile) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: False |`PATCH` /emailserverprofiles(*emailserverprofileid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /emailserverprofiles<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /emailserverprofiles(*emailserverprofileid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `ModifyAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: False |`GET` /emailserverprofiles(*emailserverprofileid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /emailserverprofiles<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: False |`PATCH` /emailserverprofiles(*emailserverprofileid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: False |`PATCH` /emailserverprofiles(*emailserverprofileid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /emailserverprofiles(*emailserverprofileid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Email Server Profile (EmailServerProfile) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Email Server Profile** |
| **DisplayCollectionName** | **Email Server Profiles** |
| **SchemaName** | `EmailServerProfile` |
| **CollectionSchemaName** | `EmailServerProfiles` |
| **EntitySetName** | `emailserverprofiles`|
| **LogicalName** | `emailserverprofile` |
| **LogicalCollectionName** | `emailserverprofiles` |
| **PrimaryIdAttribute** | `emailserverprofileid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AadResourceId](#BKMK_AadResourceId)
- [ACSEmailServiceName](#BKMK_ACSEmailServiceName)
- [ACSEnabledForOutgoingEmail](#BKMK_ACSEnabledForOutgoingEmail)
- [ACSEndpointUrl](#BKMK_ACSEndpointUrl)
- [ACSManagedIdentityId](#BKMK_ACSManagedIdentityId)
- [ACSResourceGroupName](#BKMK_ACSResourceGroupName)
- [ACSSubscriptionId](#BKMK_ACSSubscriptionId)
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
- [PurviewManagedIdentityId](#BKMK_PurviewManagedIdentityId)
- [SendEmailAlert](#BKMK_SendEmailAlert)
- [ServerAuthority](#BKMK_ServerAuthority)
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

|Property|Value|
|---|---|
|Description|**Microsoft Entra resource ID used for OAuth athentication scheme**|
|DisplayName|**Microsoft Entra resource ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`aadresourceid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_ACSEmailServiceName"></a> ACSEmailServiceName

|Property|Value|
|---|---|
|Description|**The name of the email service resource associated with the Azure Communication Service.**|
|DisplayName|**ACS Email Service Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`acsemailservicename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

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
|GlobalChoiceName|`emailserverprofile_acsenabledforoutgoingemail`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ACSEndpointUrl"></a> ACSEndpointUrl

|Property|Value|
|---|---|
|Description|**ACS Endpoint Url**|
|DisplayName|**ACS Endpoint Url**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`acsendpointurl`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|300|

### <a name="BKMK_ACSManagedIdentityId"></a> ACSManagedIdentityId

|Property|Value|
|---|---|
|Description|**Unique identifier for managed identity associated with emailserverprofile for ACS integration.**|
|DisplayName|**ACS Managed Identity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`acsmanagedidentityid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|managedidentity|

### <a name="BKMK_ACSResourceGroupName"></a> ACSResourceGroupName

|Property|Value|
|---|---|
|Description|**The name of the resource group associated with the Email Communication Service. The name is case insensitive.**|
|DisplayName|**ACS Resource Group Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`acsresourcegroupname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_ACSSubscriptionId"></a> ACSSubscriptionId

|Property|Value|
|---|---|
|Description|**The ID of the target Azure subscription associated with the Email Communication Service.**|
|DisplayName|**ACS SubscriptionId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`acssubscriptionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_DefaultServerLocation"></a> DefaultServerLocation

|Property|Value|
|---|---|
|Description|**Type the default location of the server.**|
|DisplayName|**Default Email Server Location**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`defaultserverlocation`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2084|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Type additional information that describes the email server profile.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_EmailServerProfileId"></a> EmailServerProfileId

|Property|Value|
|---|---|
|Description|**Unique identifier of the email server profile.**|
|DisplayName|**EmailServerProfile**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`emailserverprofileid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_EncodingCodePage"></a> EncodingCodePage

|Property|Value|
|---|---|
|Description|**Indicates the code page to use when encoding email content.**|
|DisplayName|**Encoding Code Page**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`encodingcodepage`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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

### <a name="BKMK_ExchangeOnlineTenantId"></a> ExchangeOnlineTenantId

|Property|Value|
|---|---|
|Description|**Type the tenant ID of Exchange Online.**|
|DisplayName|**Exchange Online Tenant Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`exchangeonlinetenantid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|36|

### <a name="BKMK_ExchangeVersion"></a> ExchangeVersion

|Property|Value|
|---|---|
|Description|**Select the version of Exchange that is on the email server.**|
|DisplayName|**Exchange Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`exchangeversion`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`emailserverprofile_exchangeversion`|

#### ExchangeVersion Choices/Options

|Value|Label|
|---|---|
|0|**Exchange 2007**|
|1|**Exchange 2007 SP1**|
|2|**Exchange 2010**|
|3|**Exchange 2010 SP1**|
|4|**Exchange 2010 SP2**|
|5|**Exchange 2013**|

### <a name="BKMK_IncomingAuthenticationProtocol"></a> IncomingAuthenticationProtocol

|Property|Value|
|---|---|
|Description|**Select the incoming email authentication protocol that is used for connecting to the email server.**|
|DisplayName|**Incoming Authentication Protocol**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`incomingauthenticationprotocol`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`emailserverprofile_authenticationprotocol`|

#### IncomingAuthenticationProtocol Choices/Options

|Value|Label|
|---|---|
|0|**Auto Detect**|
|1|**Negotiate**|
|2|**NTLM**|
|3|**Basic**|
|4|**OAuth**|

### <a name="BKMK_IncomingCredentialRetrieval"></a> IncomingCredentialRetrieval

|Property|Value|
|---|---|
|Description|**Select how credentials will be retrieved for incoming email.**|
|DisplayName|**Incoming Email Credential Retrieval**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`incomingcredentialretrieval`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`emailserverprofile_incomingcredentialretrieval`|

#### IncomingCredentialRetrieval Choices/Options

|Value|Label|
|---|---|
|0|**Credentials Specified by a User or Queue**|
|1|**Credentials Specified in Email Server Profile**|
|2|**Server to Server Authentication**|
|3|**Windows Integrated Authentication**|
|4|**Without Credentials (Anonymous)**|
|5|**Gmail OAuth**|
|6|**Exchange Hybrid Modern Auth (HMA)**|
|7|**OAuth with Microsoft Entra ID**|

### <a name="BKMK_IncomingPassword"></a> IncomingPassword

|Property|Value|
|---|---|
|Description|**Type the password for incoming email.**|
|DisplayName|**Incoming Email Password**|
|IsValidForForm|True|
|IsValidForRead|False|
|LogicalName|`incomingpassword`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_IncomingPortNumber"></a> IncomingPortNumber

|Property|Value|
|---|---|
|Description|**Type the Exchange port number for incoming mail.**|
|DisplayName|**Incoming Email Port**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`incomingportnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|65536|
|MinValue|0|

### <a name="BKMK_IncomingServerLocation"></a> IncomingServerLocation

|Property|Value|
|---|---|
|Description|**Type the location of the server for incoming email.**|
|DisplayName|**Incoming Email Server Location**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`incomingserverlocation`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2084|

### <a name="BKMK_IncomingUseImpersonation"></a> IncomingUseImpersonation

|Property|Value|
|---|---|
|Description|**Select whether to use impersonation to access the mailbox to process incoming emails.**|
|DisplayName|**Use Impersonation for Incoming Email**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`incominguseimpersonation`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`emailserverprofile_incominguseimpersonation`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IncomingUserName"></a> IncomingUserName

|Property|Value|
|---|---|
|Description|**Type the user name for incoming email.**|
|DisplayName|**Incoming Email User Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`incomingusername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_IncomingUseSSL"></a> IncomingUseSSL

|Property|Value|
|---|---|
|Description|**Select whether to use the Secure Sockets Layer (SSL) protocol for incoming email.**|
|DisplayName|**Use SSL for Incoming Email**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`incomingusessl`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`emailserverprofile_incomingusessl`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_keyvaultreferenceid"></a> keyvaultreferenceid

|Property|Value|
|---|---|
|Description|**The Azure Key Vault reference id**|
|DisplayName|**Key Vault Reference Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`keyvaultreferenceid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|keyvaultreference|

### <a name="BKMK_LastAuthorizationStatus"></a> LastAuthorizationStatus

|Property|Value|
|---|---|
|Description|**Shows the last test authorization status of email server profile**|
|DisplayName|**Last Test Authorization Status**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastauthorizationstatus`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`emailserverprofile_lastauthorizationstatus`|

#### LastAuthorizationStatus Choices/Options

|Value|Label|
|---|---|
|0|**Failure**|
|1|**Success**|

### <a name="BKMK_LastCrmMessage"></a> LastCrmMessage

|Property|Value|
|---|---|
|Description|**Shows the Dynamics 365 message obtained during the Last Test**|
|DisplayName|**Last Dynamics 365 Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastcrmmessage`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2084|

### <a name="BKMK_LastTestExecutionStatus"></a> LastTestExecutionStatus

|Property|Value|
|---|---|
|Description|**Shows the last test Execution status of email server profile**|
|DisplayName|**Last Test Execution Status**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lasttestexecutionstatus`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`emailserverprofile_lasttestexecutionstatus`|

#### LastTestExecutionStatus Choices/Options

|Value|Label|
|---|---|
|0|**Failure**|
|1|**Success**|
|2|**Warning**|

### <a name="BKMK_LastTestRequest"></a> LastTestRequest

|Property|Value|
|---|---|
|Description|**Shows the EWS Request created during the Last Test**|
|DisplayName|**Last Test Request**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lasttestrequest`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2084|

### <a name="BKMK_LastTestResponse"></a> LastTestResponse

|Property|Value|
|---|---|
|Description|**Shows the EWS Response obtained during the Last Test**|
|DisplayName|**Last Test Response**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lasttestresponse`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2084|

### <a name="BKMK_LastTestStartTime"></a> LastTestStartTime

|Property|Value|
|---|---|
|Description|**Shows the Last Test Start date and time**|
|DisplayName|**Last Test Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastteststarttime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_LastTestTotalExecutionTime"></a> LastTestTotalExecutionTime

|Property|Value|
|---|---|
|Description|**Shows the Time taken while running the last test**|
|DisplayName|**Last Test Time Taken**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lasttesttotalexecutiontime`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_LastTestValidationStatus"></a> LastTestValidationStatus

|Property|Value|
|---|---|
|Description|**Shows the last test Validation status of email server profile**|
|DisplayName|**Last Test Validation Status**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lasttestvalidationstatus`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`emailserverprofile_lasttestvalidationstatus`|

#### LastTestValidationStatus Choices/Options

|Value|Label|
|---|---|
|0|**Failure**|
|1|**Success**|

### <a name="BKMK_managedidentityid"></a> managedidentityid

|Property|Value|
|---|---|
|Description|**The managed identity id**|
|DisplayName|**Managed Identity Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`managedidentityid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|managedidentity|

### <a name="BKMK_MaxConcurrentConnections"></a> MaxConcurrentConnections

|Property|Value|
|---|---|
|Description|**Maximum number of concurrent connections allowed to the email server per authenticated user.**|
|DisplayName|**Maximum Concurrent Connections**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`maxconcurrentconnections`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|300|
|MinValue|1|

### <a name="BKMK_MinPollingIntervalInMinutes"></a> MinPollingIntervalInMinutes

|Property|Value|
|---|---|
|Description|**Minimum polling interval, in minutes, for mailboxes that are associated with this email server profile.**|
|DisplayName|**Minimum Polling Interval In Minutes**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`minpollingintervalinminutes`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1440|
|MinValue|0|

### <a name="BKMK_MoveUndeliveredEmails"></a> MoveUndeliveredEmails

|Property|Value|
|---|---|
|Description|**Indicates whether to move undelivered incoming emails to the Undeliverable folder in Microsoft Exchange.**|
|DisplayName|**Move Undelivered Emails to the Undeliverable Folder**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`moveundeliveredemails`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`emailserverprofile_moveundeliveredemails`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Type a meaningful name for the email server profile. This name is displayed when you need to select an email server profile.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OauthClientId"></a> OauthClientId

|Property|Value|
|---|---|
|Description|**ClientId used for OAuth athentication scheme**|
|DisplayName|**Oauth ClientId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`oauthclientid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_OauthClientSecret"></a> OauthClientSecret

|Property|Value|
|---|---|
|Description|**Client secret used for the OAuth authentication scheme**|
|DisplayName|**OAuth Client Secret**|
|IsValidForForm|True|
|IsValidForRead|False|
|LogicalName|`oauthclientsecret`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_OutgoingAuthenticationProtocol"></a> OutgoingAuthenticationProtocol

|Property|Value|
|---|---|
|Description|**Select the outgoing email authentication protocol that is used for connecting to the email server.**|
|DisplayName|**Outgoing Authentication Protocol**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`outgoingauthenticationprotocol`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`emailserverprofile_authenticationprotocol`|

#### OutgoingAuthenticationProtocol Choices/Options

|Value|Label|
|---|---|
|0|**Auto Detect**|
|1|**Negotiate**|
|2|**NTLM**|
|3|**Basic**|
|4|**OAuth**|

### <a name="BKMK_OutgoingAutoGrantDelegateAccess"></a> OutgoingAutoGrantDelegateAccess

|Property|Value|
|---|---|
|Description|**Indicates whether the email connector will grant delegate access permissions to the accessing user when required while processing outgoing emails.**|
|DisplayName|**Auto Grant Delegate Access for Outgoing Email.**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`outgoingautograntdelegateaccess`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`emailserverprofile_outgoingautograntdelegateaccess`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_OutgoingCredentialRetrieval"></a> OutgoingCredentialRetrieval

|Property|Value|
|---|---|
|Description|**Select how credentials will be retrieved for outgoing email.**|
|DisplayName|**Outgoing Email Credential Retrieval**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`outgoingcredentialretrieval`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`emailserverprofile_outgoingcredentialretrieval`|

#### OutgoingCredentialRetrieval Choices/Options

|Value|Label|
|---|---|
|0|**Credentials Specified by a User or Queue**|
|1|**Credentials Specified in Email Server Profile**|
|2|**Server to Server Authentication**|
|3|**Windows Integrated Authentication**|
|4|**Without Credentials (Anonymous)**|
|5|**Gmail OAuth**|
|6|**Exchange Hybrid Modern Auth (HMA)**|
|7|**OAuth with Microsoft Entra ID**|

### <a name="BKMK_OutgoingPassword"></a> OutgoingPassword

|Property|Value|
|---|---|
|Description|**Type the password for outgoing email.**|
|DisplayName|**Outgoing Email Password**|
|IsValidForForm|True|
|IsValidForRead|False|
|LogicalName|`outgoingpassword`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_OutgoingPortNumber"></a> OutgoingPortNumber

|Property|Value|
|---|---|
|Description|**Type the Exchange port number for outgoing mail.**|
|DisplayName|**Outgoing Email Port**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`outgoingportnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|65536|
|MinValue|0|

### <a name="BKMK_OutgoingServerLocation"></a> OutgoingServerLocation

|Property|Value|
|---|---|
|Description|**Type the location of the server for outgoing email.**|
|DisplayName|**Outgoing Email Server Location**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`outgoingserverlocation`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2084|

### <a name="BKMK_OutgoingUseImpersonation"></a> OutgoingUseImpersonation

|Property|Value|
|---|---|
|Description|**Select whether to use impersonation for accessing the mailbox to process outgoing emails.**|
|DisplayName|**Use Impersonation for Outgoing Email**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`outgoinguseimpersonation`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`emailserverprofile_outgoinguseimpersonation`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_OutgoingUsername"></a> OutgoingUsername

|Property|Value|
|---|---|
|Description|**Type the user name for outgoing email.**|
|DisplayName|**Outgoing Email User Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`outgoingusername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_OutgoingUseSSL"></a> OutgoingUseSSL

|Property|Value|
|---|---|
|Description|**Select whether to use the Secure Sockets Layer (SSL) protocol for outgoing email.**|
|DisplayName|**Use SSL for Outgoing Email**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`outgoingusessl`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`emailserverprofile_outgoingusessl`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_OwnerEmailAddress"></a> OwnerEmailAddress

|Property|Value|
|---|---|
|Description|**Email Server Profile Owner's email address**|
|DisplayName|**Email Server Profile Owner's email address**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneremailaddress`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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

### <a name="BKMK_ProcessEmailsReceivedAfter"></a> ProcessEmailsReceivedAfter

|Property|Value|
|---|---|
|Description|**Shows the date and time after which email messages that are received will be processed for mailboxes associated with the email server profile.**|
|DisplayName|**Process Emails Received After**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`processemailsreceivedafter`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_PurviewManagedIdentityId"></a> PurviewManagedIdentityId

|Property|Value|
|---|---|
|Description|**Unique identifier for managed identity associated with emailserverprofile for Purview integration.**|
|DisplayName|**Purview Managed Identity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`purviewmanagedidentityid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|managedidentity|

### <a name="BKMK_SendEmailAlert"></a> SendEmailAlert

|Property|Value|
|---|---|
|Description|**Select whether to send an email alert if more than 50% of the mailboxes in this email server profile failed to synchronize in an hour period.**|
|DisplayName|**Send an alert email to the owner of the email server profile reporting on major events**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sendemailalert`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`emailserverprofile_sendemailalert`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ServerAuthority"></a> ServerAuthority

|Property|Value|
|---|---|
|Description|**Select the authority for the email server.**|
|DisplayName|**Email server authority**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`serverauthority`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`emailserverprofile_serverauthority`|

#### ServerAuthority Choices/Options

|Value|Label|
|---|---|
|0|**Public (\+GCC) (https://login.microsoftonline.com)**|
|1|**US Government (GCC High and DoD) (https://login.microsoftonline.us)**|
|2|**China (21Vianet) (https://login.chinacloudapi.cn)**|
|3|**Automatic (determined by Dynamics 365 cloud)**|

### <a name="BKMK_ServerType"></a> ServerType

|Property|Value|
|---|---|
|Description|**Select the profile's email server type.**|
|DisplayName|**Email Server Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`servertype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`emailserverprofile_servertype`|

#### ServerType Choices/Options

|Value|Label|
|---|---|
|0|**Exchange Server**|
|1|**Other (POP3/SMTP)**|
|2|**Exchange Server (Hybrid)**|
|3|**Exchange Online (Hybrid)**|
|4|**IMAP/SMTP**|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Shows whether the email server profile is active or inactive.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`emailserverprofile_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Select the email server profile's status.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`emailserverprofile_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_TimeoutMailboxConnection"></a> TimeoutMailboxConnection

|Property|Value|
|---|---|
|Description|**Select whether to timeout a single mailbox.**|
|DisplayName|**Timeout Mailbox Connection to Exchange**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`timeoutmailboxconnection`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`emailserverprofile_timeoutmailboxconnection`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_TimeoutMailboxConnectionAfterAmount"></a> TimeoutMailboxConnectionAfterAmount

|Property|Value|
|---|---|
|Description|**Type the number of milliseconds to timeout a single mailbox. The upper limit is 100 seconds.**|
|DisplayName|**Timeout a Single Mailbox Connection After this Amount of Milliseconds**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`timeoutmailboxconnectionafteramount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|100000|
|MinValue|0|

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

### <a name="BKMK_UseAutoDiscover"></a> UseAutoDiscover

|Property|Value|
|---|---|
|Description|**Select whether to automatically discover the server location**|
|DisplayName|**Auto Discover Server Location**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`useautodiscover`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`emailserverprofile_useautodiscover`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_UseDefaultTenantId"></a> UseDefaultTenantId

|Property|Value|
|---|---|
|Description|**Select whether to use the Exchange Online Tenant ID obtained from running Microsoft Azure PowerShell cmdlets (highly recommended). If you select No, you can edit this field manually**|
|DisplayName|**Use Default Tenant Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`usedefaulttenantid`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`emailserverprofile_usedefaulttenantid`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_UseSameSettingsForOutgoingConnections"></a> UseSameSettingsForOutgoingConnections

|Property|Value|
|---|---|
|Description|**Select whether to use the same settings for incoming and outgoing connections.**|
|DisplayName|**Use Same Settings for Outgoing Connection**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`usesamesettingsforoutgoingconnections`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`emailserverprofile_usesamesettingsforoutgoingconnections`|
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


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [EmailServerTypeName](#BKMK_EmailServerTypeName)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [IncomingPartnerApplication](#BKMK_IncomingPartnerApplication)
- [IsIncomingPasswordSet](#BKMK_IsIncomingPasswordSet)
- [IsOauthClientSecretSet](#BKMK_IsOauthClientSecretSet)
- [IsOutgoingPasswordSet](#BKMK_IsOutgoingPasswordSet)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OutgoingPartnerApplication](#BKMK_OutgoingPartnerApplication)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)

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

### <a name="BKMK_EmailServerTypeName"></a> EmailServerTypeName

|Property|Value|
|---|---|
|Description|**Email Server Type Name**|
|DisplayName|**Email Server Type Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`emailservertypename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|250|

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

### <a name="BKMK_IncomingPartnerApplication"></a> IncomingPartnerApplication

|Property|Value|
|---|---|
|Description|**Indicates the incoming partner application.**|
|DisplayName|**Incoming Partner Application**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`incomingpartnerapplication`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|partnerapplication|

### <a name="BKMK_IsIncomingPasswordSet"></a> IsIncomingPasswordSet

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isincomingpasswordset`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`isencryptedattributevalueset`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsOauthClientSecretSet"></a> IsOauthClientSecretSet

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isoauthclientsecretset`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`isencryptedattributevalueset`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsOutgoingPasswordSet"></a> IsOutgoingPasswordSet

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isoutgoingpasswordset`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`isencryptedattributevalueset`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization associated with the record.**|
|DisplayName|**Organization Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_OutgoingPartnerApplication"></a> OutgoingPartnerApplication

|Property|Value|
|---|---|
|Description|**Indicates the outgoing partner application.**|
|DisplayName|**Outgoing Partner Application**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`outgoingpartnerapplication`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|partnerapplication|

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
|MaxLength|100|

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
|MaxLength|100|

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
|Targets||

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the email server profile.**|
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

- [business_unit_emailserverprofile](#BKMK_business_unit_emailserverprofile)
- [keyvaultreference_emailserverprofile_keyvaultreferenceid](#BKMK_keyvaultreference_emailserverprofile_keyvaultreferenceid)
- [lk_emailserverprofile_createdby](#BKMK_lk_emailserverprofile_createdby)
- [lk_emailserverprofile_createdonbehalfby](#BKMK_lk_emailserverprofile_createdonbehalfby)
- [lk_emailserverprofile_modifiedby](#BKMK_lk_emailserverprofile_modifiedby)
- [lk_emailserverprofile_modifiedonbehalfby](#BKMK_lk_emailserverprofile_modifiedonbehalfby)
- [managedidentity_emailserverprofile_acsmanagedidentityid](#BKMK_managedidentity_emailserverprofile_acsmanagedidentityid)
- [managedidentity_emailserverprofile_managedidentityid](#BKMK_managedidentity_emailserverprofile_managedidentityid)
- [managedidentity_emailserverprofile_purviewmanagedidentityid](#BKMK_managedidentity_emailserverprofile_purviewmanagedidentityid)
- [organization_emailserverprofile](#BKMK_organization_emailserverprofile)
- [owner_emailserverprofile](#BKMK_owner_emailserverprofile)
- [team_emailserverprofile](#BKMK_team_emailserverprofile)

### <a name="BKMK_business_unit_emailserverprofile"></a> business_unit_emailserverprofile

One-To-Many Relationship: [businessunit business_unit_emailserverprofile](businessunit.md#BKMK_business_unit_emailserverprofile)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_keyvaultreference_emailserverprofile_keyvaultreferenceid"></a> keyvaultreference_emailserverprofile_keyvaultreferenceid

One-To-Many Relationship: [keyvaultreference keyvaultreference_emailserverprofile_keyvaultreferenceid](keyvaultreference.md#BKMK_keyvaultreference_emailserverprofile_keyvaultreferenceid)

|Property|Value|
|---|---|
|ReferencedEntity|`keyvaultreference`|
|ReferencedAttribute|`keyvaultreferenceid`|
|ReferencingAttribute|`keyvaultreferenceid`|
|ReferencingEntityNavigationPropertyName|`keyvaultreferenceid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_emailserverprofile_createdby"></a> lk_emailserverprofile_createdby

One-To-Many Relationship: [systemuser lk_emailserverprofile_createdby](systemuser.md#BKMK_lk_emailserverprofile_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_emailserverprofile_createdonbehalfby"></a> lk_emailserverprofile_createdonbehalfby

One-To-Many Relationship: [systemuser lk_emailserverprofile_createdonbehalfby](systemuser.md#BKMK_lk_emailserverprofile_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_emailserverprofile_modifiedby"></a> lk_emailserverprofile_modifiedby

One-To-Many Relationship: [systemuser lk_emailserverprofile_modifiedby](systemuser.md#BKMK_lk_emailserverprofile_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_emailserverprofile_modifiedonbehalfby"></a> lk_emailserverprofile_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_emailserverprofile_modifiedonbehalfby](systemuser.md#BKMK_lk_emailserverprofile_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_managedidentity_emailserverprofile_acsmanagedidentityid"></a> managedidentity_emailserverprofile_acsmanagedidentityid

One-To-Many Relationship: [managedidentity managedidentity_emailserverprofile_acsmanagedidentityid](managedidentity.md#BKMK_managedidentity_emailserverprofile_acsmanagedidentityid)

|Property|Value|
|---|---|
|ReferencedEntity|`managedidentity`|
|ReferencedAttribute|`managedidentityid`|
|ReferencingAttribute|`acsmanagedidentityid`|
|ReferencingEntityNavigationPropertyName|`acsmanagedidentityid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_managedidentity_emailserverprofile_managedidentityid"></a> managedidentity_emailserverprofile_managedidentityid

One-To-Many Relationship: [managedidentity managedidentity_emailserverprofile_managedidentityid](managedidentity.md#BKMK_managedidentity_emailserverprofile_managedidentityid)

|Property|Value|
|---|---|
|ReferencedEntity|`managedidentity`|
|ReferencedAttribute|`managedidentityid`|
|ReferencingAttribute|`managedidentityid`|
|ReferencingEntityNavigationPropertyName|`managedidentityid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_managedidentity_emailserverprofile_purviewmanagedidentityid"></a> managedidentity_emailserverprofile_purviewmanagedidentityid

One-To-Many Relationship: [managedidentity managedidentity_emailserverprofile_purviewmanagedidentityid](managedidentity.md#BKMK_managedidentity_emailserverprofile_purviewmanagedidentityid)

|Property|Value|
|---|---|
|ReferencedEntity|`managedidentity`|
|ReferencedAttribute|`managedidentityid`|
|ReferencingAttribute|`purviewmanagedidentityid`|
|ReferencingEntityNavigationPropertyName|`purviewmanagedidentityid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_emailserverprofile"></a> organization_emailserverprofile

One-To-Many Relationship: [organization organization_emailserverprofile](organization.md#BKMK_organization_emailserverprofile)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_emailserverprofile"></a> owner_emailserverprofile

One-To-Many Relationship: [owner owner_emailserverprofile](owner.md#BKMK_owner_emailserverprofile)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_emailserverprofile"></a> team_emailserverprofile

One-To-Many Relationship: [team team_emailserverprofile](team.md#BKMK_team_emailserverprofile)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [EmailServerProfile_Annotation](#BKMK_EmailServerProfile_Annotation)
- [emailserverprofile_asyncoperations](#BKMK_emailserverprofile_asyncoperations)
- [emailserverprofile_bulkdeletefailures](#BKMK_emailserverprofile_bulkdeletefailures)
- [emailserverprofile_duplicatebaserecord](#BKMK_emailserverprofile_duplicatebaserecord)
- [emailserverprofile_duplicatematchingrecord](#BKMK_emailserverprofile_duplicatematchingrecord)
- [emailserverprofile_mailbox](#BKMK_emailserverprofile_mailbox)
- [EmailServerProfile_Organization](#BKMK_EmailServerProfile_Organization)
- [EmailServerProfile_SyncErrors](#BKMK_EmailServerProfile_SyncErrors)
- [tracelog_EmailServerProfile](#BKMK_tracelog_EmailServerProfile)

### <a name="BKMK_EmailServerProfile_Annotation"></a> EmailServerProfile_Annotation

Many-To-One Relationship: [annotation EmailServerProfile_Annotation](annotation.md#BKMK_EmailServerProfile_Annotation)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`EmailServerProfile_Annotation`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_emailserverprofile_asyncoperations"></a> emailserverprofile_asyncoperations

Many-To-One Relationship: [asyncoperation emailserverprofile_asyncoperations](asyncoperation.md#BKMK_emailserverprofile_asyncoperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`emailserverprofile_asyncoperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_emailserverprofile_bulkdeletefailures"></a> emailserverprofile_bulkdeletefailures

Many-To-One Relationship: [bulkdeletefailure emailserverprofile_bulkdeletefailures](bulkdeletefailure.md#BKMK_emailserverprofile_bulkdeletefailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`emailserverprofile_bulkdeletefailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_emailserverprofile_duplicatebaserecord"></a> emailserverprofile_duplicatebaserecord

Many-To-One Relationship: [duplicaterecord emailserverprofile_duplicatebaserecord](duplicaterecord.md#BKMK_emailserverprofile_duplicatebaserecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`emailserverprofile_duplicatebaserecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_emailserverprofile_duplicatematchingrecord"></a> emailserverprofile_duplicatematchingrecord

Many-To-One Relationship: [duplicaterecord emailserverprofile_duplicatematchingrecord](duplicaterecord.md#BKMK_emailserverprofile_duplicatematchingrecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`emailserverprofile_duplicatematchingrecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_emailserverprofile_mailbox"></a> emailserverprofile_mailbox

Many-To-One Relationship: [mailbox emailserverprofile_mailbox](mailbox.md#BKMK_emailserverprofile_mailbox)

|Property|Value|
|---|---|
|ReferencingEntity|`mailbox`|
|ReferencingAttribute|`emailserverprofile`|
|ReferencedEntityNavigationPropertyName|`emailserverprofile_mailbox`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_EmailServerProfile_Organization"></a> EmailServerProfile_Organization

Many-To-One Relationship: [organization EmailServerProfile_Organization](organization.md#BKMK_EmailServerProfile_Organization)

|Property|Value|
|---|---|
|ReferencingEntity|`organization`|
|ReferencingAttribute|`defaultemailserverprofileid`|
|ReferencedEntityNavigationPropertyName|`EmailServerProfile_Organization`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_EmailServerProfile_SyncErrors"></a> EmailServerProfile_SyncErrors

Many-To-One Relationship: [syncerror EmailServerProfile_SyncErrors](syncerror.md#BKMK_EmailServerProfile_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`EmailServerProfile_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_tracelog_EmailServerProfile"></a> tracelog_EmailServerProfile

Many-To-One Relationship: [tracelog tracelog_EmailServerProfile](tracelog.md#BKMK_tracelog_EmailServerProfile)

|Property|Value|
|---|---|
|ReferencingEntity|`tracelog`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`tracelog_EmailServerProfile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.emailserverprofile?displayProperty=fullName>
