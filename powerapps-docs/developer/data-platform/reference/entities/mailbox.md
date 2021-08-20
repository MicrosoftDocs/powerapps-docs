---
title: "Mailbox table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Mailbox table/entity."
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

# Mailbox table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).




## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/mailboxes(*mailboxid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/mailboxes<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/mailboxes(*mailboxid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/mailboxes(*mailboxid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/mailboxes<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/mailboxes(*mailboxid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/mailboxes(*mailboxid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|Mailboxes|
|DisplayCollectionName|Mailboxes|
|DisplayName|Mailbox|
|EntitySetName|mailboxes|
|IsBPFEntity|False|
|LogicalCollectionName|mailboxes|
|LogicalName|mailbox|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|mailboxid|
|PrimaryNameAttribute|name|
|SchemaName|Mailbox|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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
- [LastSuccessfulSyncCompletedOn](#BKMK_LastSuccessfulSyncCompletedOn)
- [LastSyncError](#BKMK_LastSyncError)
- [LastSyncErrorCode](#BKMK_LastSyncErrorCode)
- [LastSyncErrorCount](#BKMK_LastSyncErrorCount)
- [LastSyncErrorMachineName](#BKMK_LastSyncErrorMachineName)
- [LastSyncErrorOccurredOn](#BKMK_LastSyncErrorOccurredOn)
- [LastTaggedMessageId](#BKMK_LastTaggedMessageId)
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


### <a name="BKMK_ACTDeliveryMethod"></a> ACTDeliveryMethod

|Property|Value|
|--------|-----|
|Description|Choose the delivery method for the mailbox for appointments, contacts, and tasks.|
|DisplayName|Appointments, Contacts, and Tasks|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|actdeliverymethod|
|RequiredLevel|None|
|Type|Picklist|

#### ACTDeliveryMethod Choices/Options

|Value|Label|
|-----|-----|
|0|Microsoft Dynamics 365 for Outlook|
|1|Server-Side Synchronization|
|2|None|



### <a name="BKMK_ACTStatus"></a> ACTStatus

|Property|Value|
|--------|-----|
|Description|Status of the Appointments, Contacts, and Tasks.|
|DisplayName|Appointments, Contacts, and Tasks Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|actstatus|
|RequiredLevel|None|
|Type|Picklist|

#### ACTStatus Choices/Options

|Value|Label|
|-----|-----|
|0|Not Run|
|1|Success|
|2|Failure|



### <a name="BKMK_AllowEmailConnectorToUseCredentials"></a> AllowEmailConnectorToUseCredentials

|Property|Value|
|--------|-----|
|Description|Choose whether to allow the email connector to use credentials.|
|DisplayName|Allow to Use Credentials for Email Processing|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|allowemailconnectortousecredentials|
|RequiredLevel|None|
|Type|Boolean|

#### AllowEmailConnectorToUseCredentials Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_EmailAddress"></a> EmailAddress

|Property|Value|
|--------|-----|
|Description|Type the email address of the mailbox.|
|DisplayName|Email Address|
|FormatName|Email|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|emailaddress|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EmailRouterAccessApproval"></a> EmailRouterAccessApproval

|Property|Value|
|--------|-----|
|Description|Shows the status of the email address.|
|DisplayName|Email Address Status|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|emailrouteraccessapproval|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### EmailRouterAccessApproval Choices/Options

|Value|Label|
|-----|-----|
|0|Empty|
|1|Approved|
|2|Pending Approval|
|3|Rejected|



### <a name="BKMK_EmailServerProfile"></a> EmailServerProfile

|Property|Value|
|--------|-----|
|Description|Select the email server profile of the mailbox.|
|DisplayName|Server Profile|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|emailserverprofile|
|RequiredLevel|None|
|Targets|emailserverprofile|
|Type|Lookup|


### <a name="BKMK_EnabledForACT"></a> EnabledForACT

|Property|Value|
|--------|-----|
|Description|Indicates whether the mailbox is enabled for Appointments, Contacts, and Tasks.|
|DisplayName|Enabled For Appointments, Contacts, And Tasks|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|enabledforact|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### EnabledForACT Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: True



### <a name="BKMK_EnabledForIncomingEmail"></a> EnabledForIncomingEmail

|Property|Value|
|--------|-----|
|Description|Choose whether the mailbox is enabled for receiving email.|
|DisplayName|Enabled For Incoming Email|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|enabledforincomingemail|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### EnabledForIncomingEmail Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: True



### <a name="BKMK_EnabledForOutgoingEmail"></a> EnabledForOutgoingEmail

|Property|Value|
|--------|-----|
|Description|Choose whether the mailbox is enabled for sending email.|
|DisplayName|Enabled For Outgoing Email|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|enabledforoutgoingemail|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### EnabledForOutgoingEmail Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: True



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


### <a name="BKMK_EWSURL"></a> EWSURL

|Property|Value|
|--------|-----|
|Description|Exchange web services endpoint URL for the mailbox.|
|DisplayName|Exchange Web Services URL|
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ewsurl|
|MaxLength|2084|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ExchangeContactsImportStatus"></a> ExchangeContactsImportStatus

|Property|Value|
|--------|-----|
|Description|Indicates the exchange contacts import status for a mailbox record.|
|DisplayName|Exchange Contacts Import Status|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|exchangecontactsimportstatus|
|RequiredLevel|None|
|Type|Picklist|

#### ExchangeContactsImportStatus Choices/Options

|Value|Label|
|-----|-----|
|0|NotImported|
|1|Imported|
|2|ImportFailed|



### <a name="BKMK_ExchangeSyncStateXml"></a> ExchangeSyncStateXml

|Property|Value|
|--------|-----|
|Description|Contains the exchange synchronization state in XML format.|
|DisplayName|Exchange Sync State|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|exchangesyncstatexml|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_FolderHierarchy"></a> FolderHierarchy

|Property|Value|
|--------|-----|
|Description|Holds the hierarchy of folders under inbox in XML format.|
|DisplayName|Folder Hierarchy|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|folderhierarchy|
|MaxLength|1048576|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_IncomingEmailDeliveryMethod"></a> IncomingEmailDeliveryMethod

|Property|Value|
|--------|-----|
|Description|Select how incoming email will be delivered to the mailbox.|
|DisplayName|Incoming Email|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|incomingemaildeliverymethod|
|RequiredLevel|None|
|Type|Picklist|

#### IncomingEmailDeliveryMethod Choices/Options

|Value|Label|
|-----|-----|
|0|None|
|1|Microsoft Dynamics 365 for Outlook|
|2|Server-Side Synchronization or Email Router|
|3|Forward Mailbox|



### <a name="BKMK_IncomingEmailStatus"></a> IncomingEmailStatus

|Property|Value|
|--------|-----|
|Description|Select the status that will be assigned to incoming email messages.|
|DisplayName|Incoming Email Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|incomingemailstatus|
|RequiredLevel|None|
|Type|Picklist|

#### IncomingEmailStatus Choices/Options

|Value|Label|
|-----|-----|
|0|Not Run|
|1|Success|
|2|Failure|



### <a name="BKMK_IsACTSyncOrgFlagSet"></a> IsACTSyncOrgFlagSet

|Property|Value|
|--------|-----|
|Description|Set the current organization as the synchronization organization.|
|DisplayName|Set Current Organization as Synchronization Organization|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isactsyncorgflagset|
|RequiredLevel|None|
|Type|Boolean|

#### IsACTSyncOrgFlagSet Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsEmailAddressApprovedByO365Admin"></a> IsEmailAddressApprovedByO365Admin

|Property|Value|
|--------|-----|
|Description|Shows the status of approval of the email address by O365 Admin.|
|DisplayName|Email Address O365 Admin Approval Status|
|IsValidForCreate|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isemailaddressapprovedbyo365admin|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsEmailAddressApprovedByO365Admin Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_ItemsFailedForLastSync"></a> ItemsFailedForLastSync

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Items Failed For Last Sync|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|itemsfailedforlastsync|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ItemsProcessedForLastSync"></a> ItemsProcessedForLastSync

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Items Processed For Last Sync|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|itemsprocessedforlastsync|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_LastAutoDiscoveredOn"></a> LastAutoDiscoveredOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the Exchange web services URL was last discovered using the AutoDiscover service.|
|DisplayName|Last Auto Discovered On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|lastautodiscoveredon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_LastSuccessfulSyncCompletedOn"></a> LastSuccessfulSyncCompletedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Last Successful Sync Time|
|DisplayName|Last Successful Sync Time|
|Format|DateAndTime|
|IsValidForCreate|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|lastsuccessfulsynccompletedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_LastSyncError"></a> LastSyncError

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Last Sync Error Stack|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|lastsyncerror|
|MaxLength|2048|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_LastSyncErrorCode"></a> LastSyncErrorCode

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Last Sync Error Code|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|lastsyncerrorcode|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_LastSyncErrorCount"></a> LastSyncErrorCount

|Property|Value|
|--------|-----|
|Description|For internal use only|
|DisplayName|Last Sync Error Continuous Count|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|lastsyncerrorcount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_LastSyncErrorMachineName"></a> LastSyncErrorMachineName

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Last Sync Error Machine Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|lastsyncerrormachinename|
|MaxLength|320|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_LastSyncErrorOccurredOn"></a> LastSyncErrorOccurredOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Last Sync Error Time|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|lastsyncerroroccurredon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_LastTaggedMessageId"></a> LastTaggedMessageId

**Added by**: msft_ServerSideSync_Extensions Solution

|Property|Value|
|--------|-----|
|Description|Identifies the last MessageId that has been processed for tagging in the remote system.|
|DisplayName|Last Tagged MessageId|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForCreate|False|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|lasttaggedmessageid|
|MaxLength|320|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_MailboxId"></a> MailboxId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the mailbox.|
|DisplayName|Mailbox|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mailboxid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_MailboxProcessingContext"></a> MailboxProcessingContext

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Processing Context of the Mailbox|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mailboxprocessingcontext|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Type the name of the mailbox.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|200|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OauthAccessToken"></a> OauthAccessToken

|Property|Value|
|--------|-----|
|Description|Type the Oauth access token for the mailbox.|
|DisplayName|Oauth access token|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|oauthaccesstoken|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OauthRefreshToken"></a> OauthRefreshToken

|Property|Value|
|--------|-----|
|Description|Type the Oauth refresh token for the mailbox.|
|DisplayName|Oauth refresh token|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|oauthrefreshtoken|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OauthTokenExpiresOn"></a> OauthTokenExpiresOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the Oauth token will expire|
|DisplayName|Oauth token expiration datetime|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|oauthtokenexpireson|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_OfficeAppsDeploymentScheduled"></a> OfficeAppsDeploymentScheduled

|Property|Value|
|--------|-----|
|Description|Indicates if the office apps deployment has been scheduled for a mailbox record.|
|DisplayName|Office Apps Deployment Scheduled|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|officeappsdeploymentscheduled|
|RequiredLevel|None|
|Type|Boolean|

#### OfficeAppsDeploymentScheduled Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_OfficeAppsDeploymentStatus"></a> OfficeAppsDeploymentStatus

|Property|Value|
|--------|-----|
|Description|Indicates the office apps deployment type for a mailbox record.|
|DisplayName|Office Apps Deployment Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|officeappsdeploymentstatus|
|RequiredLevel|None|
|Type|Picklist|

#### OfficeAppsDeploymentStatus Choices/Options

|Value|Label|
|-----|-----|
|0|NotInstalled|
|1|Installed|
|2|InstallFailed|
|3|UninstallFailed|
|4|UpgradeRequired|



### <a name="BKMK_OrgMarkedAsPrimaryForExchangeSync"></a> OrgMarkedAsPrimaryForExchangeSync

|Property|Value|
|--------|-----|
|Description|Indicates if the crm org is to be marked as primary syncing org for the mailbox record.|
|DisplayName|Crm Org Marked as Primary Org for Exchange Mailbox|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|orgmarkedasprimaryforexchangesync|
|RequiredLevel|None|
|Type|Boolean|

#### OrgMarkedAsPrimaryForExchangeSync Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_OutgoingEmailDeliveryMethod"></a> OutgoingEmailDeliveryMethod

|Property|Value|
|--------|-----|
|Description|Select how outgoing email will be sent from the mailbox.|
|DisplayName|Outgoing Email|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|outgoingemaildeliverymethod|
|RequiredLevel|None|
|Type|Picklist|

#### OutgoingEmailDeliveryMethod Choices/Options

|Value|Label|
|-----|-----|
|0|None|
|1|Microsoft Dynamics 365 for Outlook|
|2|Server-Side Synchronization or Email Router|



### <a name="BKMK_OutgoingEmailStatus"></a> OutgoingEmailStatus

|Property|Value|
|--------|-----|
|Description|Select the status of outgoing email messages.|
|DisplayName|Outgoing Email Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|outgoingemailstatus|
|RequiredLevel|None|
|Type|Picklist|

#### OutgoingEmailStatus Choices/Options

|Value|Label|
|-----|-----|
|0|Not Run|
|1|Success|
|2|Failure|



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


### <a name="BKMK_Password"></a> Password

|Property|Value|
|--------|-----|
|Description|Type the password for the mailbox.|
|DisplayName|Password|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|False|
|LogicalName|password|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PostponeMailboxProcessingUntil"></a> PostponeMailboxProcessingUntil

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when processing will begin on this mailbox.|
|DisplayName|Postpone Mailbox Processing Until|
|Format|DateOnly|
|IsValidForCreate|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|postponemailboxprocessinguntil|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_PostponeOfficeAppsDeploymentUntil"></a> PostponeOfficeAppsDeploymentUntil

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the next outlook mail app install will be run for a mailbox record.|
|DisplayName|Postpone Outlook Mail App Install Until|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|postponeofficeappsdeploymentuntil|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_PostponeSendingUntil"></a> PostponeSendingUntil

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the mailbox can start sending emails.|
|DisplayName|Postpone Sending Until|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|postponesendinguntil|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_PostponeTestEmailConfigurationUntil"></a> PostponeTestEmailConfigurationUntil

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the next email configuration test will be run for a mailbox record.|
|DisplayName|Postpone Test Email Configuration Until|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|postponetestemailconfigurationuntil|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ProcessAndDeleteEmails"></a> ProcessAndDeleteEmails

|Property|Value|
|--------|-----|
|Description|Select whether to delete emails from the mailbox after processing.|
|DisplayName|Delete Emails after Processing|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|processanddeleteemails|
|RequiredLevel|None|
|Type|Boolean|

#### ProcessAndDeleteEmails Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_ProcessEmailReceivedAfter"></a> ProcessEmailReceivedAfter

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time to start processing email received by the mailbox.|
|DisplayName|Process Email Received After|
|Format|DateOnly|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|processemailreceivedafter|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|--------|-----|
|Description|Shows whether the mailbox is active or inactive.|
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
|Description|Select the mailbox's status.|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|SystemRequired|
|Type|Status|

#### StatusCode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Active|0|
|2|Inactive|1|



### <a name="BKMK_TagEmailsAfter"></a> TagEmailsAfter

**Added by**: msft_ServerSideSync_Extensions Solution

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Identifies the timestamp after for which emails should be tagged in the remote system.|
|DisplayName|Tag Emails After|
|Format|DateOnly|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|tagemailsafter|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_TestEmailConfigurationRetryCount"></a> TestEmailConfigurationRetryCount

|Property|Value|
|--------|-----|
|Description|Shows the number of times an email configuration test has been performed.|
|DisplayName|Test Email Configuration Retry Count|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|testemailconfigurationretrycount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TestEmailConfigurationScheduled"></a> TestEmailConfigurationScheduled

|Property|Value|
|--------|-----|
|Description|Indicates if the email configuration test has been scheduled for a mailbox record.|
|DisplayName|Test Email Configuration Scheduled|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|testemailconfigurationscheduled|
|RequiredLevel|None|
|Type|Boolean|

#### TestEmailConfigurationScheduled Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_TestMailboxAccessCompletedOn"></a> TestMailboxAccessCompletedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the last email configuration test was completed for a mailbox record.|
|DisplayName|Mailbox Test Completed On|
|Format|DateAndTime|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|testmailboxaccesscompletedon|
|RequiredLevel|None|
|Type|DateTime|


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


### <a name="BKMK_UndeliverableFolder"></a> UndeliverableFolder

|Property|Value|
|--------|-----|
|Description|Shows the ID of the Undeliverable folder in the mailbox managed by Microsoft Exchange.|
|DisplayName|Undeliverable Folder|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForCreate|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|undeliverablefolder|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Username"></a> Username

|Property|Value|
|--------|-----|
|Description|Type a user name used for mailbox authentication.|
|DisplayName|User Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|username|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_VerboseLoggingEnabled"></a> VerboseLoggingEnabled

|Property|Value|
|--------|-----|
|Description|Indicates if verbose tracing needs to be enabled for this mailbox.|
|DisplayName|Verbose Logging|
|Format|None|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|verboseloggingenabled|
|MaxValue|100|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

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
- [LastMessageId](#BKMK_LastMessageId)
- [LastSyncStartedOn](#BKMK_LastSyncStartedOn)
- [MailboxStatus](#BKMK_MailboxStatus)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [NextScheduledACTSyncInSeconds](#BKMK_NextScheduledACTSyncInSeconds)
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

|Property|Value|
|--------|-----|
|Description|Mailbox Total Duration in Average|
|DisplayName|Monitor Total Performance|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|averagetotalduration|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


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
|MaxLength|160|
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
|MaxLength|160|
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
|MaxLength|160|
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
|MaxLength|160|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_EmailServerProfileName"></a> EmailServerProfileName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|emailserverprofilename|
|MaxLength|100|
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


### <a name="BKMK_ExchangeContactsImportCompletedOn"></a> ExchangeContactsImportCompletedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the exchange contacts import was last completed for a mailbox record.|
|DisplayName|Exchange Contacts Import Completed On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|exchangecontactsimportcompletedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ExchangeSyncStateXmlFileRef_Name"></a> ExchangeSyncStateXmlFileRef_Name

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|exchangesyncstatexmlfileref_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ForcedUnlockCount"></a> ForcedUnlockCount

|Property|Value|
|--------|-----|
|Description|For internal use only|
|DisplayName|Count of the number of times a mailbox gets forced unlocked|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|forcedunlockcount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_HostId"></a> HostId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the async host that is processing this mailbox.|
|DisplayName|Host|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|hostid|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IsExchangeContactsImportScheduled"></a> IsExchangeContactsImportScheduled

|Property|Value|
|--------|-----|
|Description|Is Exchange Contacts Import Scheduled.|
|DisplayName|Is Exchange Contacts Import Scheduled.|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isexchangecontactsimportscheduled|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsExchangeContactsImportScheduled Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsForwardMailbox"></a> IsForwardMailbox

|Property|Value|
|--------|-----|
|Description|Select whether the mailbox is a forward mailbox.|
|DisplayName|Is Forward Mailbox|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isforwardmailbox|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsForwardMailbox Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: True



### <a name="BKMK_IsOauthAccessTokenSet"></a> IsOauthAccessTokenSet

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isoauthaccesstokenset|
|RequiredLevel|None|
|Type|Boolean|

#### IsOauthAccessTokenSet Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsOauthRefreshTokenSet"></a> IsOauthRefreshTokenSet

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isoauthrefreshtokenset|
|RequiredLevel|None|
|Type|Boolean|

#### IsOauthRefreshTokenSet Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsPasswordSet"></a> IsPasswordSet

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ispasswordset|
|RequiredLevel|None|
|Type|Boolean|

#### IsPasswordSet Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsServiceAccount"></a> IsServiceAccount

|Property|Value|
|--------|-----|
|Description|Select whether the mailbox corresponds to one for the service account.|
|DisplayName|Is Service Account|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isserviceaccount|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsServiceAccount Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_LastActiveOn"></a> LastActiveOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Last Active On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|lastactiveon|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_LastDuration"></a> LastDuration

|Property|Value|
|--------|-----|
|Description|Last Duration for the mailbox|
|DisplayName|Monitor last duration Performance|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|lastduration|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_LastMailboxForcedUnlockOccurredOn"></a> LastMailboxForcedUnlockOccurredOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Last Date Time when a mailbox got forced unlocked|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|lastmailboxforcedunlockoccurredon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_LastMessageId"></a> LastMessageId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the last message.|
|DisplayName|Last Message ID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|lastmessageid|
|MaxLength|320|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_LastSyncStartedOn"></a> LastSyncStartedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Last Sync Start Time|
|DisplayName|Last Sync Start Time|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|lastsyncstartedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_MailboxStatus"></a> MailboxStatus

|Property|Value|
|--------|-----|
|Description|Last Sync Status for Outgoing, Incoming and ACT as a whole.|
|DisplayName|Mailbox Status|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mailboxstatus|
|RequiredLevel|None|
|Type|Picklist|

#### MailboxStatus Choices/Options

|Value|Label|
|-----|-----|
|0|Not Run|
|1|Success|
|2|Failure|



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
|MaxLength|160|
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
|MaxLength|160|
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
|MaxLength|160|
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
|MaxLength|160|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_NextScheduledACTSyncInSeconds"></a> NextScheduledACTSyncInSeconds

**Added by**: msft_ServerSideSync_Extensions Solution

|Property|Value|
|--------|-----|
|Description|The next scheduled ACT sync delay, in seconds, to apply to the mailbox.|
|DisplayName|Next Scheduled ACT Sync Delay In Seconds|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|nextscheduledactsyncinseconds|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_NoACTCount"></a> NoACTCount

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Zero appointment, contact, task count for mailbox|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|noactcount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_NoEmailCount"></a> NoEmailCount

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Zero email count for mailbox|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|noemailcount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_OfficeAppsDeploymentCompleteOn"></a> OfficeAppsDeploymentCompleteOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the last office apps deployment was completed for a mailbox record.|
|DisplayName|Office Apps Deployment Completed On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|officeappsdeploymentcompleteon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_OfficeAppsDeploymentError"></a> OfficeAppsDeploymentError

|Property|Value|
|--------|-----|
|Description|The Office Apps deployment error.|
|DisplayName|Office Apps Deployment Error|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|officeappsdeploymenterror|
|MaxLength|2048|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the organization associated with the record.|
|DisplayName|Organization|
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
|MaxLength|160|
|RequiredLevel|SystemRequired|
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
|MaxLength|160|
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
|MaxLength|160|
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
|MaxLength|160|
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
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ProcessedTimes"></a> ProcessedTimes

|Property|Value|
|--------|-----|
|Description|The number of times mailbox has processed|
|DisplayName|Monitor Performance|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|processedtimes|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ProcessingLastAttemptedOn"></a> ProcessingLastAttemptedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the processing of the mailbox was last attempted.|
|DisplayName|Date Processing Last Attempted|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|processinglastattemptedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ProcessingStateCode"></a> ProcessingStateCode

|Property|Value|
|--------|-----|
|Description|Information that indicates whether email will be processed for this mailbox|
|DisplayName|Mailbox Processing State|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|processingstatecode|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_ReceivingPostponedUntil"></a> ReceivingPostponedUntil

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Postpone receiving emails for the mailbox until the specified data and time.|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|receivingpostponeduntil|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ReceivingPostponedUntilForACT"></a> ReceivingPostponedUntilForACT

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Postpone processing Appointments, Contacts, and Tasks for the mailbox until the specified data and time.|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|receivingpostponeduntilforact|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|--------|-----|
|Description|Choose the user associated to the mailbox.|
|DisplayName|Regarding|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|regardingobjectid|
|RequiredLevel|None|
|Targets|queue,systemuser|
|Type|Lookup|


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

|Property|Value|
|--------|-----|
|Description|Name for User associated with Mailbox.|
|DisplayName|Regarding Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjectidname|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|--------|-----|
|Description|Object Type of the entity associated with the mailbox.|
|DisplayName|Regarding Object Type Code|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjecttypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_TransientFailureCount"></a> TransientFailureCount

|Property|Value|
|--------|-----|
|Description|Concatenation of transient failure counts of all mailbox operations.|
|DisplayName|Transient Failure Count|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|transientfailurecount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|Version number of the mailbox.|
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
- [mailbox_email_ReceivingMailboxId](#BKMK_mailbox_email_ReceivingMailboxId)


### <a name="BKMK_systemuser_defaultmailbox_mailbox"></a> systemuser_defaultmailbox_mailbox

Same as systemuser table [systemuser_defaultmailbox_mailbox](systemuser.md#BKMK_systemuser_defaultmailbox_mailbox) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|systemuser|
|ReferencingAttribute|defaultmailbox|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|systemuser_defaultmailbox_mailbox|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_queue_defaultmailbox_mailbox"></a> queue_defaultmailbox_mailbox

Same as queue table [queue_defaultmailbox_mailbox](queue.md#BKMK_queue_defaultmailbox_mailbox) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|queue|
|ReferencingAttribute|defaultmailbox|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|queue_defaultmailbox_mailbox|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_activitypointer_sendermailboxid_mailbox"></a> activitypointer_sendermailboxid_mailbox

Same as activitypointer table [activitypointer_sendermailboxid_mailbox](activitypointer.md#BKMK_activitypointer_sendermailboxid_mailbox) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitypointer|
|ReferencingAttribute|sendermailboxid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|activitypointer_sendermailboxid_mailbox|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Mailbox_MailboxTrackingFolder"></a> Mailbox_MailboxTrackingFolder

Same as mailboxtrackingfolder table [Mailbox_MailboxTrackingFolder](mailboxtrackingfolder.md#BKMK_Mailbox_MailboxTrackingFolder) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|mailboxid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Mailbox_MailboxTrackingFolder|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Mailbox_Annotation"></a> Mailbox_Annotation

Same as annotation table [Mailbox_Annotation](annotation.md#BKMK_Mailbox_Annotation) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Mailbox_Annotation|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_Mailbox_SyncErrors"></a> Mailbox_SyncErrors

Same as syncerror table [Mailbox_SyncErrors](syncerror.md#BKMK_Mailbox_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Mailbox_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_mailbox_processsessions"></a> mailbox_processsessions

Same as processsession table [mailbox_processsessions](processsession.md#BKMK_mailbox_processsessions) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mailbox_processsessions|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 110|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mailbox_asyncoperations"></a> mailbox_asyncoperations

Same as asyncoperation table [mailbox_asyncoperations](asyncoperation.md#BKMK_mailbox_asyncoperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mailbox_asyncoperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_tracelog_Mailbox"></a> tracelog_Mailbox

Same as tracelog table [tracelog_Mailbox](tracelog.md#BKMK_tracelog_Mailbox) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|tracelog|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|tracelog_Mailbox|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_email_sendermailboxid_mailbox"></a> email_sendermailboxid_mailbox

Same as email table [email_sendermailboxid_mailbox](email.md#BKMK_email_sendermailboxid_mailbox) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|sendermailboxid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|email_sendermailboxid_mailbox|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mailbox_email_ReceivingMailboxId"></a> mailbox_email_ReceivingMailboxId

**Added by**: msft_ActivitiesInfra_Extensions Solution

Same as email table [mailbox_email_ReceivingMailboxId](email.md#BKMK_mailbox_email_ReceivingMailboxId) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|receivingmailboxid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mailbox_email_ReceivingMailboxId|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

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

See systemuser Table [lk_mailbox_createdby](systemuser.md#BKMK_lk_mailbox_createdby) One-To-Many relationship.

### <a name="BKMK_lk_mailbox_createdonbehalfby"></a> lk_mailbox_createdonbehalfby

See systemuser Table [lk_mailbox_createdonbehalfby](systemuser.md#BKMK_lk_mailbox_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_mailbox_modifiedby"></a> lk_mailbox_modifiedby

See systemuser Table [lk_mailbox_modifiedby](systemuser.md#BKMK_lk_mailbox_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_mailbox_modifiedonbehalfby"></a> lk_mailbox_modifiedonbehalfby

See systemuser Table [lk_mailbox_modifiedonbehalfby](systemuser.md#BKMK_lk_mailbox_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_user_mailbox"></a> user_mailbox

See systemuser Table [user_mailbox](systemuser.md#BKMK_user_mailbox) One-To-Many relationship.

### <a name="BKMK_team_mailbox"></a> team_mailbox

See team Table [team_mailbox](team.md#BKMK_team_mailbox) One-To-Many relationship.

### <a name="BKMK_business_unit_mailbox"></a> business_unit_mailbox

See businessunit Table [business_unit_mailbox](businessunit.md#BKMK_business_unit_mailbox) One-To-Many relationship.

### <a name="BKMK_mailbox_regarding_systemuser"></a> mailbox_regarding_systemuser

See systemuser Table [mailbox_regarding_systemuser](systemuser.md#BKMK_mailbox_regarding_systemuser) One-To-Many relationship.

### <a name="BKMK_emailserverprofile_mailbox"></a> emailserverprofile_mailbox

See emailserverprofile Table [emailserverprofile_mailbox](emailserverprofile.md#BKMK_emailserverprofile_mailbox) One-To-Many relationship.

### <a name="BKMK_organization_mailbox"></a> organization_mailbox

See organization Table [organization_mailbox](organization.md#BKMK_organization_mailbox) One-To-Many relationship.

### <a name="BKMK_mailbox_regarding_queue"></a> mailbox_regarding_queue

See queue Table [mailbox_regarding_queue](queue.md#BKMK_mailbox_regarding_queue) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.mailbox?text=mailbox EntityType" />