---
title: "Queue table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Queue table/entity."
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

# Queue table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

A list of records that require action, such as accounts, activities, and cases.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|AddPrincipalToQueue|<xref href="Microsoft.Dynamics.CRM.AddPrincipalToQueue?text=AddPrincipalToQueue Action" />|<xref:Microsoft.Crm.Sdk.Messages.AddPrincipalToQueueRequest>|
|Assign|PATCH [*org URI*]/api/data/v9.0/queues(*queueid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/queues<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/queues(*queueid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/queues(*queueid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/queues<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RetrieveUserQueues|<xref href="Microsoft.Dynamics.CRM.RetrieveUserQueues?text=RetrieveUserQueues Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveUserQueuesRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/queues(*queueid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/queues(*queueid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|Queues|
|DisplayCollectionName|Queues|
|DisplayName|Queue|
|EntitySetName|queues|
|IsBPFEntity|False|
|LogicalCollectionName|queues|
|LogicalName|queue|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|queueid|
|PrimaryNameAttribute|name|
|SchemaName|Queue|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [BusinessUnitId](#BKMK_BusinessUnitId)
- [Description](#BKMK_Description)
- [EMailAddress](#BKMK_EMailAddress)
- [EmailRouterAccessApproval](#BKMK_EmailRouterAccessApproval)
- [EntityImage](#BKMK_EntityImage)
- [IgnoreUnsolicitedEmail](#BKMK_IgnoreUnsolicitedEmail)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IncomingEmailDeliveryMethod](#BKMK_IncomingEmailDeliveryMethod)
- [IncomingEmailFilteringMethod](#BKMK_IncomingEmailFilteringMethod)
- [Name](#BKMK_Name)
- [OutgoingEmailDeliveryMethod](#BKMK_OutgoingEmailDeliveryMethod)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [PrimaryUserId](#BKMK_PrimaryUserId)
- [QueueId](#BKMK_QueueId)
- [QueueViewType](#BKMK_QueueViewType)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)


### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the business unit with which the queue is associated.|
|DisplayName|Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|businessunitid|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Description of the queue.|
|DisplayName|Description|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_EMailAddress"></a> EMailAddress

|Property|Value|
|--------|-----|
|Description|Email address that is associated with the queue.|
|DisplayName|Incoming Email|
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
|Description|Shows the status of the primary email address.|
|DisplayName|Primary Email Status|
|IsValidForCreate|False|
|IsValidForForm|True|
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


### <a name="BKMK_IgnoreUnsolicitedEmail"></a> IgnoreUnsolicitedEmail

|Property|Value|
|--------|-----|
|Description|Information that specifies whether a queue is to ignore unsolicited email (deprecated).|
|DisplayName|Convert To Email Activities|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ignoreunsolicitedemail|
|RequiredLevel|None|
|Type|Boolean|

#### IgnoreUnsolicitedEmail Choices/Options

|Value|Label|
|-----|-----|
|1|Only specific Emails|
|0|All incoming Emails|

**DefaultValue**: False



### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|Unique identifier of the data import or data migration that created this record.|
|DisplayName|Import Sequence Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|importsequencenumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_IncomingEmailDeliveryMethod"></a> IncomingEmailDeliveryMethod

|Property|Value|
|--------|-----|
|Description|Incoming email delivery method for the queue.|
|DisplayName|Incoming Email Delivery Method|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|incomingemaildeliverymethod|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### IncomingEmailDeliveryMethod Choices/Options

|Value|Label|
|-----|-----|
|0|None|
|2|Server-Side Synchronization or Email Router|
|3|Forward Mailbox|



### <a name="BKMK_IncomingEmailFilteringMethod"></a> IncomingEmailFilteringMethod

|Property|Value|
|--------|-----|
|Description|Convert Incoming Email To Activities|
|DisplayName|Convert Incoming Email To Activities|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|incomingemailfilteringmethod|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### IncomingEmailFilteringMethod Choices/Options

|Value|Label|
|-----|-----|
|0|All email messages|
|1|Email messages in response to Dynamics 365 email|
|2|Email messages from Dynamics 365 Leads, Contacts and Accounts|
|3|Email messages from Dynamics 365 records that are email enabled|
|4|No email messages|



### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of the queue.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|200|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_OutgoingEmailDeliveryMethod"></a> OutgoingEmailDeliveryMethod

|Property|Value|
|--------|-----|
|Description|Outgoing email delivery method for the queue.|
|DisplayName|Outgoing Email Delivery Method|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|outgoingemaildeliverymethod|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### OutgoingEmailDeliveryMethod Choices/Options

|Value|Label|
|-----|-----|
|0|None|
|2|Server-Side Synchronization or Email Router|



### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time that the record was migrated.|
|DisplayName|Record Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user or team who owns the queue.|
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
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_PrimaryUserId"></a> PrimaryUserId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the owner of the queue.|
|DisplayName|Owner (deprecated)|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|primaryuserid|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_QueueId"></a> QueueId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the queue.|
|DisplayName|Queue|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|queueid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_QueueViewType"></a> QueueViewType

|Property|Value|
|--------|-----|
|Description|Select whether the queue is public or private. A public queue can be viewed by all. A private queue can be viewed only by the members added to the queue.|
|DisplayName|Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|queueviewtype|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### QueueViewType Choices/Options

|Value|Label|
|-----|-----|
|0|Public|
|1|Private|



### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|--------|-----|
|Description|Status of the queue.|
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
|Description|Reason for the status of the queue.|
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



### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the currency associated with the queue.|
|DisplayName|Currency|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|transactioncurrencyid|
|RequiredLevel|None|
|Targets|transactioncurrency|
|Type|Lookup|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AllowEmailCredentials](#BKMK_AllowEmailCredentials)
- [BusinessUnitIdName](#BKMK_BusinessUnitIdName)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [DefaultMailbox](#BKMK_DefaultMailbox)
- [DefaultMailboxName](#BKMK_DefaultMailboxName)
- [EmailPassword](#BKMK_EmailPassword)
- [EmailUsername](#BKMK_EmailUsername)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [ExchangeRate](#BKMK_ExchangeRate)
- [IsEmailAddressApprovedByO365Admin](#BKMK_IsEmailAddressApprovedByO365Admin)
- [IsFaxQueue](#BKMK_IsFaxQueue)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [NumberOfItems](#BKMK_NumberOfItems)
- [NumberOfMembers](#BKMK_NumberOfMembers)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [PrimaryUserIdName](#BKMK_PrimaryUserIdName)
- [PrimaryUserIdYomiName](#BKMK_PrimaryUserIdYomiName)
- [QueueTypeCode](#BKMK_QueueTypeCode)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_AllowEmailCredentials"></a> AllowEmailCredentials

|Property|Value|
|--------|-----|
|Description|This attribute is no longer used. The data is now in the Mailbox.AllowEmailConnectorToUseCredentials attribute.|
|DisplayName|Allow to Use Credentials for Email Processing (Obsolete)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|allowemailcredentials|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### AllowEmailCredentials Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_BusinessUnitIdName"></a> BusinessUnitIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|businessunitidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the queue record.|
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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the queue was created.|
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
|Description|Unique identifier of the delegate user who created the queue.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|False|
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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_DefaultMailbox"></a> DefaultMailbox

|Property|Value|
|--------|-----|
|Description|Select the mailbox associated with this queue.|
|DisplayName|Mailbox|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|defaultmailbox|
|RequiredLevel|None|
|Targets|mailbox|
|Type|Lookup|


### <a name="BKMK_DefaultMailboxName"></a> DefaultMailboxName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|defaultmailboxname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EmailPassword"></a> EmailPassword

|Property|Value|
|--------|-----|
|Description|This attribute is no longer used. The data is now in the Mailbox.Password attribute.|
|DisplayName|Password (Obsolete)|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|emailpassword|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EmailUsername"></a> EmailUsername

|Property|Value|
|--------|-----|
|Description|This attribute is no longer used. The data is now in the Mailbox.UserName attribute.|
|DisplayName|User Name (Obsolete)|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|emailusername|
|MaxLength|200|
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


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|--------|-----|
|Description|Exchange rate for the currency associated with the queue with respect to the base currency.|
|DisplayName|Exchange Rate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.0000000001|
|Precision|10|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_IsEmailAddressApprovedByO365Admin"></a> IsEmailAddressApprovedByO365Admin

|Property|Value|
|--------|-----|
|Description|Shows the status of approval of the email address by O365 Admin.|
|DisplayName|Email Address O365 Admin Approval Status|
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



### <a name="BKMK_IsFaxQueue"></a> IsFaxQueue

|Property|Value|
|--------|-----|
|Description|Indication of whether a queue is the fax delivery queue.|
|DisplayName|Fax Queue|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isfaxqueue|
|RequiredLevel|None|
|Type|Boolean|

#### IsFaxQueue Choices/Options

|Value|Label|
|-----|-----|
|1|Fax Queue|
|0|Non-fax Queue|

**DefaultValue**: False



### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the queue.|
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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the queue was last modified.|
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
|Description|Unique identifier of the delegate user who last modified the queue.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|False|
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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_NumberOfItems"></a> NumberOfItems

|Property|Value|
|--------|-----|
|Description|Number of Queue items associated with the queue.|
|DisplayName|Queue Items|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|numberofitems|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_NumberOfMembers"></a> NumberOfMembers

|Property|Value|
|--------|-----|
|Description|Number of Members associated with the queue.|
|DisplayName|No. of Members|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|numberofmembers|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the organization associated with the queue.|
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
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|--------|-----|
|Description||
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
|Description||
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
|Description|Unique identifier of the business unit that owns the queue.|
|DisplayName|Owning Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|--------|-----|
|Description|Unique identifier of the team who owns the queue.|
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
|Description|Unique identifier of the user who owns the queue.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_PrimaryUserIdName"></a> PrimaryUserIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|primaryuseridname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PrimaryUserIdYomiName"></a> PrimaryUserIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|primaryuseridyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_QueueTypeCode"></a> QueueTypeCode

|Property|Value|
|--------|-----|
|Description|Type of queue that is automatically assigned when a user or queue is created. The type can be public, private, or work in process.|
|DisplayName|Queue Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|queuetypecode|
|RequiredLevel|None|
|Type|Picklist|

#### QueueTypeCode Choices/Options

|Value|Label|
|-----|-----|
|1|Default Value|



### <a name="BKMK_TransactionCurrencyIdName"></a> TransactionCurrencyIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|transactioncurrencyidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|Version number of the queue.|
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

- [queue_system_user](#BKMK_queue_system_user)
- [Queue_AsyncOperations](#BKMK_Queue_AsyncOperations)
- [queue_principalobjectattributeaccess](#BKMK_queue_principalobjectattributeaccess)
- [Queue_DuplicateMatchingRecord](#BKMK_Queue_DuplicateMatchingRecord)
- [Queue_SyncErrors](#BKMK_Queue_SyncErrors)
- [Queue_Email_EmailSender](#BKMK_Queue_Email_EmailSender)
- [Queue_DuplicateBaseRecord](#BKMK_Queue_DuplicateBaseRecord)
- [queue_activity_parties](#BKMK_queue_activity_parties)
- [queue_team](#BKMK_queue_team)
- [queue_entries](#BKMK_queue_entries)
- [Queue_ProcessSessions](#BKMK_Queue_ProcessSessions)
- [queue_PostFollows](#BKMK_queue_PostFollows)
- [mailbox_regarding_queue](#BKMK_mailbox_regarding_queue)
- [Queue_BulkDeleteFailures](#BKMK_Queue_BulkDeleteFailures)
- [email_acceptingentity_queue](#BKMK_email_acceptingentity_queue)


### <a name="BKMK_queue_system_user"></a> queue_system_user

Same as systemuser table [queue_system_user](systemuser.md#BKMK_queue_system_user) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|systemuser|
|ReferencingAttribute|queueid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|queue_system_user|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Queue_AsyncOperations"></a> Queue_AsyncOperations

Same as asyncoperation table [Queue_AsyncOperations](asyncoperation.md#BKMK_Queue_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Queue_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_queue_principalobjectattributeaccess"></a> queue_principalobjectattributeaccess

Same as principalobjectattributeaccess table [queue_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_queue_principalobjectattributeaccess) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|queue_principalobjectattributeaccess|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Queue_DuplicateMatchingRecord"></a> Queue_DuplicateMatchingRecord

Same as duplicaterecord table [Queue_DuplicateMatchingRecord](duplicaterecord.md#BKMK_Queue_DuplicateMatchingRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Queue_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Queue_SyncErrors"></a> Queue_SyncErrors

Same as syncerror table [Queue_SyncErrors](syncerror.md#BKMK_Queue_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Queue_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_Queue_Email_EmailSender"></a> Queue_Email_EmailSender

Same as email table [Queue_Email_EmailSender](email.md#BKMK_Queue_Email_EmailSender) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|emailsender|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Queue_Email_EmailSender|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Queue_DuplicateBaseRecord"></a> Queue_DuplicateBaseRecord

Same as duplicaterecord table [Queue_DuplicateBaseRecord](duplicaterecord.md#BKMK_Queue_DuplicateBaseRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Queue_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_queue_activity_parties"></a> queue_activity_parties

Same as activityparty table [queue_activity_parties](activityparty.md#BKMK_queue_activity_parties) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activityparty|
|ReferencingAttribute|partyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|queue_activity_parties|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_queue_team"></a> queue_team

Same as team table [queue_team](team.md#BKMK_queue_team) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|team|
|ReferencingAttribute|queueid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|queue_team|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_queue_entries"></a> queue_entries

Same as queueitem table [queue_entries](queueitem.md#BKMK_queue_entries) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|queueitem|
|ReferencingAttribute|queueid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|queue_entries|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Queue_ProcessSessions"></a> Queue_ProcessSessions

Same as processsession table [Queue_ProcessSessions](processsession.md#BKMK_Queue_ProcessSessions) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Queue_ProcessSessions|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 110|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_queue_PostFollows"></a> queue_PostFollows

Same as postfollow table [queue_PostFollows](postfollow.md#BKMK_queue_PostFollows) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|postfollow|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|queue_PostFollows|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mailbox_regarding_queue"></a> mailbox_regarding_queue

Same as mailbox table [mailbox_regarding_queue](mailbox.md#BKMK_mailbox_regarding_queue) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailbox|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mailbox_regarding_queue|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Queue_BulkDeleteFailures"></a> Queue_BulkDeleteFailures

Same as bulkdeletefailure table [Queue_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Queue_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Queue_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_email_acceptingentity_queue"></a> email_acceptingentity_queue

**Added by**: msft_ActivitiesInfra_Extensions Solution

Same as email table [email_acceptingentity_queue](email.md#BKMK_email_acceptingentity_queue) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|acceptingentityid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|email_acceptingentity_queue|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [queue_defaultmailbox_mailbox](#BKMK_queue_defaultmailbox_mailbox)
- [business_unit_queues](#BKMK_business_unit_queues)
- [business_unit_queues2](#BKMK_business_unit_queues2)
- [lk_queue_modifiedonbehalfby](#BKMK_lk_queue_modifiedonbehalfby)
- [organization_queues](#BKMK_organization_queues)
- [lk_queuebase_createdby](#BKMK_lk_queuebase_createdby)
- [lk_queuebase_modifiedby](#BKMK_lk_queuebase_modifiedby)
- [TransactionCurrency_Queue](#BKMK_TransactionCurrency_Queue)
- [queue_primary_user](#BKMK_queue_primary_user)
- [lk_queue_createdonbehalfby](#BKMK_lk_queue_createdonbehalfby)


### <a name="BKMK_queue_defaultmailbox_mailbox"></a> queue_defaultmailbox_mailbox

See mailbox Table [queue_defaultmailbox_mailbox](mailbox.md#BKMK_queue_defaultmailbox_mailbox) One-To-Many relationship.

### <a name="BKMK_business_unit_queues"></a> business_unit_queues

See businessunit Table [business_unit_queues](businessunit.md#BKMK_business_unit_queues) One-To-Many relationship.

### <a name="BKMK_business_unit_queues2"></a> business_unit_queues2

See businessunit Table [business_unit_queues2](businessunit.md#BKMK_business_unit_queues2) One-To-Many relationship.

### <a name="BKMK_lk_queue_modifiedonbehalfby"></a> lk_queue_modifiedonbehalfby

See systemuser Table [lk_queue_modifiedonbehalfby](systemuser.md#BKMK_lk_queue_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_queues"></a> organization_queues

See organization Table [organization_queues](organization.md#BKMK_organization_queues) One-To-Many relationship.

### <a name="BKMK_lk_queuebase_createdby"></a> lk_queuebase_createdby

See systemuser Table [lk_queuebase_createdby](systemuser.md#BKMK_lk_queuebase_createdby) One-To-Many relationship.

### <a name="BKMK_lk_queuebase_modifiedby"></a> lk_queuebase_modifiedby

See systemuser Table [lk_queuebase_modifiedby](systemuser.md#BKMK_lk_queuebase_modifiedby) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_Queue"></a> TransactionCurrency_Queue

See transactioncurrency Table [TransactionCurrency_Queue](transactioncurrency.md#BKMK_TransactionCurrency_Queue) One-To-Many relationship.

### <a name="BKMK_queue_primary_user"></a> queue_primary_user

See systemuser Table [queue_primary_user](systemuser.md#BKMK_queue_primary_user) One-To-Many relationship.

### <a name="BKMK_lk_queue_createdonbehalfby"></a> lk_queue_createdonbehalfby

See systemuser Table [lk_queue_createdonbehalfby](systemuser.md#BKMK_lk_queue_createdonbehalfby) One-To-Many relationship.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the Queue table is the first table in the relationship. Listed by **SchemaName**.


### <a name="BKMK_queuemembership_association"></a> queuemembership_association

IntersectEntityName: queuemembership<br />
#### Table 1

|Property|Value|
|--------|-----|
|IntersectAttribute|queueid|
|IsCustomizable|False|
|LogicalName|queue|
|NavigationPropertyName|queuemembership_association|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |

#### Table 2

|Property|Value|
|--------|-----|
|LogicalName|systemuser|
|IntersectAttribute|systemuserid|
|NavigationPropertyName|queuemembership_association|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |


### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.queue?text=queue EntityType" />