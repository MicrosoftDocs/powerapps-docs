---
title: "Queue table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Queue table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Queue table/entity reference (Microsoft Dataverse)

A list of records that require action, such as accounts, activities, and cases.

## Messages

The following table lists the messages for the Queue table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `AddPrincipalToQueue`<br />Event: True |<xref:Microsoft.Dynamics.CRM.AddPrincipalToQueue?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.AddPrincipalToQueueRequest>|
| `Assign`<br />Event: True |`PATCH` /queues(*queueid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /queues<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /queues(*queueid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /queues(*queueid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /queues<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RetrieveUserQueues`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveUserQueues?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUserQueuesRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /queues(*queueid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /queues(*queueid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /queues(*queueid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Queue table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Queue** |
| **DisplayCollectionName** | **Queues** |
| **SchemaName** | `Queue` |
| **CollectionSchemaName** | `Queues` |
| **EntitySetName** | `queues`|
| **LogicalName** | `queue` |
| **LogicalCollectionName** | `queues` |
| **PrimaryIdAttribute** | `queueid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

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
|---|---|
|Description|**Unique identifier of the business unit with which the queue is associated.**|
|DisplayName|**Business Unit**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`businessunitid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the queue.**|
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

### <a name="BKMK_EMailAddress"></a> EMailAddress

|Property|Value|
|---|---|
|Description|**Email address that is associated with the queue.**|
|DisplayName|**Incoming Email**|
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
|Description|**Shows the status of the primary email address.**|
|DisplayName|**Primary Email Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`emailrouteraccessapproval`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`queue_emailrouteraccessapproval`|

#### EmailRouterAccessApproval Choices/Options

|Value|Label|
|---|---|
|0|**Empty**|
|1|**Approved**|
|2|**Pending Approval**|
|3|**Rejected**|

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

### <a name="BKMK_IgnoreUnsolicitedEmail"></a> IgnoreUnsolicitedEmail

|Property|Value|
|---|---|
|Description|**Information that specifies whether a queue is to ignore unsolicited email (deprecated).**|
|DisplayName|**Convert To Email Activities**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ignoreunsolicitedemail`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`queue_ignoreunsolicitedemail`|
|DefaultValue|False|
|True Label|Only specific Emails|
|False Label|All incoming Emails|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Unique identifier of the data import or data migration that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_IncomingEmailDeliveryMethod"></a> IncomingEmailDeliveryMethod

|Property|Value|
|---|---|
|Description|**Incoming email delivery method for the queue.**|
|DisplayName|**Incoming Email Delivery Method**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`incomingemaildeliverymethod`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`queue_incomingemaildeliverymethod`|

#### IncomingEmailDeliveryMethod Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|2|**Server-Side Synchronization or Email Router**|
|3|**Forward Mailbox**|

### <a name="BKMK_IncomingEmailFilteringMethod"></a> IncomingEmailFilteringMethod

|Property|Value|
|---|---|
|Description|**Convert Incoming Email To Activities**|
|DisplayName|**Convert Incoming Email To Activities**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`incomingemailfilteringmethod`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`queue_incomingemailfilteringmethod`|

#### IncomingEmailFilteringMethod Choices/Options

|Value|Label|
|---|---|
|0|**All email messages**|
|1|**Email messages in response to Dynamics 365 email**|
|2|**Email messages from Dynamics 365 Leads, Contacts and Accounts**|
|3|**Email messages from Dynamics 365 records that are email enabled**|
|4|**No email messages**|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the queue.**|
|DisplayName|**Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_OutgoingEmailDeliveryMethod"></a> OutgoingEmailDeliveryMethod

|Property|Value|
|---|---|
|Description|**Outgoing email delivery method for the queue.**|
|DisplayName|**Outgoing Email Delivery Method**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`outgoingemaildeliverymethod`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`queue_outgoingemaildeliverymethod`|

#### OutgoingEmailDeliveryMethod Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|2|**Server-Side Synchronization or Email Router**|

### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|---|---|
|Description|**Date and time that the record was migrated.**|
|DisplayName|**Record Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overriddencreatedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user or team who owns the queue.**|
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
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_PrimaryUserId"></a> PrimaryUserId

|Property|Value|
|---|---|
|Description|**Unique identifier of the owner of the queue.**|
|DisplayName|**Owner (deprecated)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`primaryuserid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_QueueId"></a> QueueId

|Property|Value|
|---|---|
|Description|**Unique identifier of the queue.**|
|DisplayName|**Queue**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`queueid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_QueueViewType"></a> QueueViewType

|Property|Value|
|---|---|
|Description|**Select whether the queue is public or private. A public queue can be viewed by all. A private queue can be viewed only by the members added to the queue.**|
|DisplayName|**Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`queueviewtype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`queue_queueviewtype`|

#### QueueViewType Choices/Options

|Value|Label|
|---|---|
|0|**Public**|
|1|**Private**|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Status of the queue.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`queue_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Reason for the status of the queue.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|SystemRequired|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`queue_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Unique identifier of the currency associated with the queue.**|
|DisplayName|**Currency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`transactioncurrencyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|transactioncurrency|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [AllowEmailCredentials](#BKMK_AllowEmailCredentials)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [DefaultMailbox](#BKMK_DefaultMailbox)
- [EmailPassword](#BKMK_EmailPassword)
- [EmailUsername](#BKMK_EmailUsername)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [ExchangeRate](#BKMK_ExchangeRate)
- [IsEmailAddressApprovedByO365Admin](#BKMK_IsEmailAddressApprovedByO365Admin)
- [IsFaxQueue](#BKMK_IsFaxQueue)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [NumberOfItems](#BKMK_NumberOfItems)
- [NumberOfMembers](#BKMK_NumberOfMembers)
- [OrganizationId](#BKMK_OrganizationId)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [QueueTypeCode](#BKMK_QueueTypeCode)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_AllowEmailCredentials"></a> AllowEmailCredentials

|Property|Value|
|---|---|
|Description|**This attribute is no longer used. The data is now in the Mailbox.AllowEmailConnectorToUseCredentials attribute.**|
|DisplayName|**Allow to Use Credentials for Email Processing (Obsolete)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`allowemailcredentials`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`queue_allowemailcredentials`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the queue record.**|
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
|Description|**Date and time when the queue was created.**|
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
|Description|**Unique identifier of the delegate user who created the queue.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_DefaultMailbox"></a> DefaultMailbox

|Property|Value|
|---|---|
|Description|**Select the mailbox associated with this queue.**|
|DisplayName|**Mailbox**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`defaultmailbox`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mailbox|

### <a name="BKMK_EmailPassword"></a> EmailPassword

|Property|Value|
|---|---|
|Description|**This attribute is no longer used. The data is now in the Mailbox.Password attribute.**|
|DisplayName|**Password (Obsolete)**|
|IsValidForForm|True|
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
|DisplayName|**User Name (Obsolete)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`emailusername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

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

### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|---|---|
|Description|**Exchange rate for the currency associated with the queue with respect to the base currency.**|
|DisplayName|**Exchange Rate**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`exchangerate`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Disabled|
|MaxValue|100000000000|
|MinValue|1E-12|
|Precision|12|
|SourceTypeMask|0|

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
|GlobalChoiceName|`queue_isemailaddressapprovedbyo365admin`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsFaxQueue"></a> IsFaxQueue

|Property|Value|
|---|---|
|Description|**Indication of whether a queue is the fax delivery queue.**|
|DisplayName|**Fax Queue**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isfaxqueue`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`queue_isfaxqueue`|
|DefaultValue|False|
|True Label|Fax Queue|
|False Label|Non-fax Queue|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the queue.**|
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
|Description|**Date and time when the queue was last modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the queue.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_NumberOfItems"></a> NumberOfItems

|Property|Value|
|---|---|
|Description|**Number of Queue items associated with the queue.**|
|DisplayName|**Queue Items**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`numberofitems`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_NumberOfMembers"></a> NumberOfMembers

|Property|Value|
|---|---|
|Description|**Number of Members associated with the queue.**|
|DisplayName|**No. of Members**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`numberofmembers`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization associated with the queue.**|
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
|Description||
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
|Description||
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
|Description|**Unique identifier of the business unit that owns the queue.**|
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
|Description|**Unique identifier of the team who owns the queue.**|
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
|Description|**Unique identifier of the user who owns the queue.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_QueueTypeCode"></a> QueueTypeCode

|Property|Value|
|---|---|
|Description|**Type of queue that is automatically assigned when a user or queue is created. The type can be public, private, or work in process.**|
|DisplayName|**Queue Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`queuetypecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`queue_queuetypecode`|

#### QueueTypeCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the queue.**|
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

- [business_unit_queues](#BKMK_business_unit_queues)
- [business_unit_queues2](#BKMK_business_unit_queues2)
- [lk_queue_createdonbehalfby](#BKMK_lk_queue_createdonbehalfby)
- [lk_queue_modifiedonbehalfby](#BKMK_lk_queue_modifiedonbehalfby)
- [lk_queuebase_createdby](#BKMK_lk_queuebase_createdby)
- [lk_queuebase_modifiedby](#BKMK_lk_queuebase_modifiedby)
- [organization_queues](#BKMK_organization_queues)
- [owner_queues](#BKMK_owner_queues)
- [queue_defaultmailbox_mailbox](#BKMK_queue_defaultmailbox_mailbox)
- [queue_primary_user](#BKMK_queue_primary_user)
- [TransactionCurrency_Queue](#BKMK_TransactionCurrency_Queue)

### <a name="BKMK_business_unit_queues"></a> business_unit_queues

One-To-Many Relationship: [businessunit business_unit_queues](businessunit.md#BKMK_business_unit_queues)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`businessunitid`|
|ReferencingEntityNavigationPropertyName|`businessunitid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_business_unit_queues2"></a> business_unit_queues2

One-To-Many Relationship: [businessunit business_unit_queues2](businessunit.md#BKMK_business_unit_queues2)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_queue_createdonbehalfby"></a> lk_queue_createdonbehalfby

One-To-Many Relationship: [systemuser lk_queue_createdonbehalfby](systemuser.md#BKMK_lk_queue_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_queue_modifiedonbehalfby"></a> lk_queue_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_queue_modifiedonbehalfby](systemuser.md#BKMK_lk_queue_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_queuebase_createdby"></a> lk_queuebase_createdby

One-To-Many Relationship: [systemuser lk_queuebase_createdby](systemuser.md#BKMK_lk_queuebase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_queuebase_modifiedby"></a> lk_queuebase_modifiedby

One-To-Many Relationship: [systemuser lk_queuebase_modifiedby](systemuser.md#BKMK_lk_queuebase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_queues"></a> organization_queues

One-To-Many Relationship: [organization organization_queues](organization.md#BKMK_organization_queues)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_queues"></a> owner_queues

One-To-Many Relationship: [owner owner_queues](owner.md#BKMK_owner_queues)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_queue_defaultmailbox_mailbox"></a> queue_defaultmailbox_mailbox

One-To-Many Relationship: [mailbox queue_defaultmailbox_mailbox](mailbox.md#BKMK_queue_defaultmailbox_mailbox)

|Property|Value|
|---|---|
|ReferencedEntity|`mailbox`|
|ReferencedAttribute|`mailboxid`|
|ReferencingAttribute|`defaultmailbox`|
|ReferencingEntityNavigationPropertyName|`defaultmailbox`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_queue_primary_user"></a> queue_primary_user

One-To-Many Relationship: [systemuser queue_primary_user](systemuser.md#BKMK_queue_primary_user)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`primaryuserid`|
|ReferencingEntityNavigationPropertyName|`primaryuserid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_Queue"></a> TransactionCurrency_Queue

One-To-Many Relationship: [transactioncurrency TransactionCurrency_Queue](transactioncurrency.md#BKMK_TransactionCurrency_Queue)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencingEntityNavigationPropertyName|`transactioncurrencyid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [email_acceptingentity_queue](#BKMK_email_acceptingentity_queue)
- [mailbox_regarding_queue](#BKMK_mailbox_regarding_queue)
- [queue_activity_parties](#BKMK_queue_activity_parties)
- [Queue_AsyncOperations](#BKMK_Queue_AsyncOperations)
- [Queue_BulkDeleteFailures](#BKMK_Queue_BulkDeleteFailures)
- [Queue_DuplicateBaseRecord](#BKMK_Queue_DuplicateBaseRecord)
- [Queue_DuplicateMatchingRecord](#BKMK_Queue_DuplicateMatchingRecord)
- [Queue_Email_EmailSender](#BKMK_Queue_Email_EmailSender)
- [queue_entries](#BKMK_queue_entries)
- [queue_PostFollows](#BKMK_queue_PostFollows)
- [queue_PostRegardings](#BKMK_queue_PostRegardings)
- [queue_principalobjectattributeaccess](#BKMK_queue_principalobjectattributeaccess)
- [Queue_ProcessSessions](#BKMK_Queue_ProcessSessions)
- [Queue_SyncErrors](#BKMK_Queue_SyncErrors)
- [queue_system_user](#BKMK_queue_system_user)
- [queue_team](#BKMK_queue_team)

### <a name="BKMK_email_acceptingentity_queue"></a> email_acceptingentity_queue

Many-To-One Relationship: [email email_acceptingentity_queue](email.md#BKMK_email_acceptingentity_queue)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`acceptingentityid`|
|ReferencedEntityNavigationPropertyName|`email_acceptingentity_queue`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mailbox_regarding_queue"></a> mailbox_regarding_queue

Many-To-One Relationship: [mailbox mailbox_regarding_queue](mailbox.md#BKMK_mailbox_regarding_queue)

|Property|Value|
|---|---|
|ReferencingEntity|`mailbox`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mailbox_regarding_queue`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_queue_activity_parties"></a> queue_activity_parties

Many-To-One Relationship: [activityparty queue_activity_parties](activityparty.md#BKMK_queue_activity_parties)

|Property|Value|
|---|---|
|ReferencingEntity|`activityparty`|
|ReferencingAttribute|`partyid`|
|ReferencedEntityNavigationPropertyName|`queue_activity_parties`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Queue_AsyncOperations"></a> Queue_AsyncOperations

Many-To-One Relationship: [asyncoperation Queue_AsyncOperations](asyncoperation.md#BKMK_Queue_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Queue_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Queue_BulkDeleteFailures"></a> Queue_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure Queue_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Queue_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Queue_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Queue_DuplicateBaseRecord"></a> Queue_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord Queue_DuplicateBaseRecord](duplicaterecord.md#BKMK_Queue_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`Queue_DuplicateBaseRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Queue_DuplicateMatchingRecord"></a> Queue_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord Queue_DuplicateMatchingRecord](duplicaterecord.md#BKMK_Queue_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`Queue_DuplicateMatchingRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Queue_Email_EmailSender"></a> Queue_Email_EmailSender

Many-To-One Relationship: [email Queue_Email_EmailSender](email.md#BKMK_Queue_Email_EmailSender)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`emailsender`|
|ReferencedEntityNavigationPropertyName|`Queue_Email_EmailSender`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_queue_entries"></a> queue_entries

Many-To-One Relationship: [queueitem queue_entries](queueitem.md#BKMK_queue_entries)

|Property|Value|
|---|---|
|ReferencingEntity|`queueitem`|
|ReferencingAttribute|`queueid`|
|ReferencedEntityNavigationPropertyName|`queue_entries`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `31c1d587-5374-4c22-bdcf-54fe8cd1aee5`|

### <a name="BKMK_queue_PostFollows"></a> queue_PostFollows

Many-To-One Relationship: [postfollow queue_PostFollows](postfollow.md#BKMK_queue_PostFollows)

|Property|Value|
|---|---|
|ReferencingEntity|`postfollow`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`queue_PostFollows`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_queue_PostRegardings"></a> queue_PostRegardings

Many-To-One Relationship: [postregarding queue_PostRegardings](postregarding.md#BKMK_queue_PostRegardings)

|Property|Value|
|---|---|
|ReferencingEntity|`postregarding`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`queue_PostRegardings`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_queue_principalobjectattributeaccess"></a> queue_principalobjectattributeaccess

Many-To-One Relationship: [principalobjectattributeaccess queue_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_queue_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`queue_principalobjectattributeaccess`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Queue_ProcessSessions"></a> Queue_ProcessSessions

Many-To-One Relationship: [processsession Queue_ProcessSessions](processsession.md#BKMK_Queue_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Queue_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Queue_SyncErrors"></a> Queue_SyncErrors

Many-To-One Relationship: [syncerror Queue_SyncErrors](syncerror.md#BKMK_Queue_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Queue_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_queue_system_user"></a> queue_system_user

Many-To-One Relationship: [systemuser queue_system_user](systemuser.md#BKMK_queue_system_user)

|Property|Value|
|---|---|
|ReferencingEntity|`systemuser`|
|ReferencingAttribute|`queueid`|
|ReferencedEntityNavigationPropertyName|`queue_system_user`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_queue_team"></a> queue_team

Many-To-One Relationship: [team queue_team](team.md#BKMK_queue_team)

|Property|Value|
|---|---|
|ReferencingEntity|`team`|
|ReferencingAttribute|`queueid`|
|ReferencedEntityNavigationPropertyName|`queue_team`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

### <a name="BKMK_queuemembership_association"></a> queuemembership_association

See [systemuser queuemembership_association Many-To-Many Relationship](systemuser.md#BKMK_queuemembership_association)

|Property|Value|
|---|---|
|IntersectEntityName|`queuemembership`|
|IsCustomizable|False|
|SchemaName|`queuemembership_association`|
|IntersectAttribute|`queueid`|
|NavigationPropertyName|`queuemembership_association`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.queue?displayProperty=fullName>
