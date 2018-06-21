---
title: "Queue Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the Queue entity."

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
ms.date: 03/07/2018
ms.author: jdaly
---
# Queue Entity Reference

A list of records that require action, such as accounts, activities, and cases.

## Entity Properties

**DisplayName**: Queue<br />
**DisplayCollectionName**: Queues<br />
**SchemaName**: Queue<br />
**CollectionSchemaName**: Queues<br />
**LogicalName**: queue<br />
**LogicalCollectionName**: queues<br />
**EntitySetName**: queues<br />
**PrimaryIdAttribute**: queueid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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

**Description**: Unique identifier of the business unit with which the queue is associated.<br />
**DisplayName**: Business Unit<br />
**LogicalName**: businessunitid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_Description"></a> Description

**Description**: Description of the queue.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_EMailAddress"></a> EMailAddress

**Description**: Email address that is associated with the queue.<br />
**DisplayName**: Incoming Email<br />
**LogicalName**: emailaddress<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Email<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_EmailRouterAccessApproval"></a> EmailRouterAccessApproval

**Description**: Shows the status of the primary email address.<br />
**DisplayName**: Primary Email Status<br />
**LogicalName**: emailrouteraccessapproval<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Empty
- **Value**: 1 **Label**: Approved
- **Value**: 2 **Label**: Pending Approval
- **Value**: 3 **Label**: Rejected



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


### <a name="BKMK_IgnoreUnsolicitedEmail"></a> IgnoreUnsolicitedEmail

**Description**: Information that specifies whether a queue is to ignore unsolicited email (deprecated).<br />
**DisplayName**: Convert To Email Activities<br />
**LogicalName**: ignoreunsolicitedemail<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Only specific Emails
- **FalseOption Value**: 0 **Label**: All incoming Emails

**DefaultValue**: False


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

**Description**: Unique identifier of the data import or data migration that created this record.<br />
**DisplayName**: Import Sequence Number<br />
**LogicalName**: importsequencenumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_IncomingEmailDeliveryMethod"></a> IncomingEmailDeliveryMethod

**Description**: Incoming email delivery method for the queue.<br />
**DisplayName**: Incoming Email Delivery Method<br />
**LogicalName**: incomingemaildeliverymethod<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: None
- **Value**: 2 **Label**: Server-Side Synchronization or Email Router
- **Value**: 3 **Label**: Forward Mailbox



### <a name="BKMK_IncomingEmailFilteringMethod"></a> IncomingEmailFilteringMethod

**Description**: Convert Incoming Email To Activities<br />
**DisplayName**: Convert Incoming Email To Activities<br />
**LogicalName**: incomingemailfilteringmethod<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: All email messages
- **Value**: 1 **Label**: Email messages in response to Dynamics 365 email
- **Value**: 2 **Label**: Email messages from Dynamics 365 Leads, Contacts and Accounts
- **Value**: 3 **Label**: Email messages from Dynamics 365 records that are email enabled



### <a name="BKMK_Name"></a> Name

**Description**: Name of the queue.<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_OutgoingEmailDeliveryMethod"></a> OutgoingEmailDeliveryMethod

**Description**: Outgoing email delivery method for the queue.<br />
**DisplayName**: Outgoing Email Delivery Method<br />
**LogicalName**: outgoingemaildeliverymethod<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: None
- **Value**: 2 **Label**: Server-Side Synchronization or Email Router



### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

**Description**: Date and time that the record was migrated.<br />
**DisplayName**: Record Created On<br />
**LogicalName**: overriddencreatedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Unique identifier of the user or team who owns the queue.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_PrimaryUserId"></a> PrimaryUserId

**Description**: Unique identifier of the owner of the queue.<br />
**DisplayName**: Owner (deprecated)<br />
**LogicalName**: primaryuserid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_QueueId"></a> QueueId

**Description**: Unique identifier of the queue.<br />
**DisplayName**: Queue<br />
**LogicalName**: queueid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_QueueViewType"></a> QueueViewType

**Description**: Select whether the queue is public or private. A public queue can be viewed by all. A private queue can be viewed only by the members added to the queue.<br />
**DisplayName**: Type<br />
**LogicalName**: queueviewtype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Public
- **Value**: 1 **Label**: Private



### <a name="BKMK_StateCode"></a> StateCode

**Description**: Status of the queue.<br />
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

**Description**: Reason for the status of the queue.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Status<br />
**Options**:

- **Value**: 1 **Label**: Active **State**: 0
- **Value**: 2 **Label**: Inactive **State**: 1



### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

**Description**: Unique identifier of the currency associated with the queue.<br />
**DisplayName**: Currency<br />
**LogicalName**: transactioncurrencyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: transactioncurrency

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

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

**Description**: This attribute is no longer used. The data is now in the Mailbox.AllowEmailConnectorToUseCredentials attribute.<br />
**DisplayName**: Allow to Use Credentials for Email Processing (Obsolete)<br />
**LogicalName**: allowemailcredentials<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_BusinessUnitIdName"></a> BusinessUnitIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: businessunitidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the queue record.<br />
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
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the queue was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the queue.<br />
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


### <a name="BKMK_DefaultMailbox"></a> DefaultMailbox

**Description**: Select the mailbox associated with this queue.<br />
**DisplayName**: Mailbox<br />
**LogicalName**: defaultmailbox<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: mailbox


### <a name="BKMK_DefaultMailboxName"></a> DefaultMailboxName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: defaultmailboxname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_EmailPassword"></a> EmailPassword

**Description**: This attribute is no longer used. The data is now in the Mailbox.Password attribute.<br />
**DisplayName**: Password (Obsolete)<br />
**LogicalName**: emailpassword<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_EmailUsername"></a> EmailUsername

**Description**: This attribute is no longer used. The data is now in the Mailbox.UserName attribute.<br />
**DisplayName**: User Name (Obsolete)<br />
**LogicalName**: emailusername<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


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


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

**Description**: Exchange rate for the currency associated with the queue with respect to the base currency.<br />
**DisplayName**: Exchange Rate<br />
**LogicalName**: exchangerate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0.0000000001<br />
**Precision**: 10


### <a name="BKMK_IsEmailAddressApprovedByO365Admin"></a> IsEmailAddressApprovedByO365Admin

**Description**: Shows the status of approval of the email address by O365 Admin.<br />
**DisplayName**: Email Address O365 Admin Approval Status<br />
**LogicalName**: isemailaddressapprovedbyo365admin<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsFaxQueue"></a> IsFaxQueue

**Description**: Indication of whether a queue is the fax delivery queue.<br />
**DisplayName**: Fax Queue<br />
**LogicalName**: isfaxqueue<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Fax Queue
- **FalseOption Value**: 0 **Label**: Non-fax Queue

**DefaultValue**: False


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the queue.<br />
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
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the queue was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the queue.<br />
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


### <a name="BKMK_NumberOfItems"></a> NumberOfItems

**Description**: Number of Queue items associated with the queue.<br />
**DisplayName**: Queue Items<br />
**LogicalName**: numberofitems<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_NumberOfMembers"></a> NumberOfMembers

**Description**: Number of Members associated with the queue.<br />
**DisplayName**: No. of Members<br />
**LogicalName**: numberofmembers<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization associated with the queue.<br />
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
**MaxLength**: 100


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Description**: <br />
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

**Description**: <br />
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

**Description**: Unique identifier of the business unit that owns the queue.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier of the team who owns the queue.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns the queue.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_PrimaryUserIdName"></a> PrimaryUserIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: primaryuseridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_PrimaryUserIdYomiName"></a> PrimaryUserIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: primaryuseridyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_QueueTypeCode"></a> QueueTypeCode

**Description**: Type of queue that is automatically assigned when a user or queue is created. The type can be public, private, or work in process.<br />
**DisplayName**: Queue Type<br />
**LogicalName**: queuetypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Default Value



### <a name="BKMK_TransactionCurrencyIdName"></a> TransactionCurrencyIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: transactioncurrencyidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: Version number of the queue.<br />
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

- [queue_system_user](#BKMK_queue_system_user)
- [userentityinstancedata_queue](#BKMK_userentityinstancedata_queue)
- [Queue_AsyncOperations](#BKMK_Queue_AsyncOperations)
- [queue_principalobjectattributeaccess](#BKMK_queue_principalobjectattributeaccess)
- [Queue_DuplicateMatchingRecord](#BKMK_Queue_DuplicateMatchingRecord)
- [Queue_SyncErrors](#BKMK_Queue_SyncErrors)
- [Queue_Email_EmailSender](#BKMK_Queue_Email_EmailSender)
- [Queue_DuplicateBaseRecord](#BKMK_Queue_DuplicateBaseRecord)
- [queue_activity_parties](#BKMK_queue_activity_parties)
- [queue_team](#BKMK_queue_team)
- [queue_entries](#BKMK_queue_entries)
- [queue_routingruleitem](#BKMK_queue_routingruleitem)
- [queue_convertruleitem](#BKMK_queue_convertruleitem)
- [Queue_ProcessSessions](#BKMK_Queue_ProcessSessions)
- [queue_PostFollows](#BKMK_queue_PostFollows)
- [convertrule_queue](#BKMK_convertrule_queue)
- [mailbox_regarding_queue](#BKMK_mailbox_regarding_queue)
- [Queue_BulkDeleteFailures](#BKMK_Queue_BulkDeleteFailures)


### <a name="BKMK_queue_system_user"></a> queue_system_user

Same as systemuser entity [queue_system_user](systemuser.md#BKMK_queue_system_user) Many-To-One relationship.

**ReferencingEntity**: systemuser<br />
**ReferencingAttribute**: queueid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: queue_system_user<br />
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


### <a name="BKMK_userentityinstancedata_queue"></a> userentityinstancedata_queue

Same as userentityinstancedata entity [userentityinstancedata_queue](userentityinstancedata.md#BKMK_userentityinstancedata_queue) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_queue<br />
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


### <a name="BKMK_Queue_AsyncOperations"></a> Queue_AsyncOperations

Same as asyncoperation entity [Queue_AsyncOperations](asyncoperation.md#BKMK_Queue_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Queue_AsyncOperations<br />
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


### <a name="BKMK_queue_principalobjectattributeaccess"></a> queue_principalobjectattributeaccess

Same as principalobjectattributeaccess entity [queue_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_queue_principalobjectattributeaccess) Many-To-One relationship.

**ReferencingEntity**: principalobjectattributeaccess<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: queue_principalobjectattributeaccess<br />
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


### <a name="BKMK_Queue_DuplicateMatchingRecord"></a> Queue_DuplicateMatchingRecord

Same as duplicaterecord entity [Queue_DuplicateMatchingRecord](duplicaterecord.md#BKMK_Queue_DuplicateMatchingRecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: duplicaterecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Queue_DuplicateMatchingRecord<br />
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


### <a name="BKMK_Queue_SyncErrors"></a> Queue_SyncErrors

Same as syncerror entity [Queue_SyncErrors](syncerror.md#BKMK_Queue_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: Queue_SyncErrors<br />
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


### <a name="BKMK_Queue_Email_EmailSender"></a> Queue_Email_EmailSender

Same as email entity [Queue_Email_EmailSender](email.md#BKMK_Queue_Email_EmailSender) Many-To-One relationship.

**ReferencingEntity**: email<br />
**ReferencingAttribute**: emailsender<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Queue_Email_EmailSender<br />
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


### <a name="BKMK_Queue_DuplicateBaseRecord"></a> Queue_DuplicateBaseRecord

Same as duplicaterecord entity [Queue_DuplicateBaseRecord](duplicaterecord.md#BKMK_Queue_DuplicateBaseRecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: baserecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Queue_DuplicateBaseRecord<br />
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


### <a name="BKMK_queue_activity_parties"></a> queue_activity_parties

Same as activityparty entity [queue_activity_parties](activityparty.md#BKMK_queue_activity_parties) Many-To-One relationship.

**ReferencingEntity**: activityparty<br />
**ReferencingAttribute**: partyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: queue_activity_parties<br />
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


### <a name="BKMK_queue_team"></a> queue_team

Same as team entity [queue_team](team.md#BKMK_queue_team) Many-To-One relationship.

**ReferencingEntity**: team<br />
**ReferencingAttribute**: queueid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: queue_team<br />
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


### <a name="BKMK_queue_entries"></a> queue_entries

Same as queueitem entity [queue_entries](queueitem.md#BKMK_queue_entries) Many-To-One relationship.

**ReferencingEntity**: queueitem<br />
**ReferencingAttribute**: queueid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: queue_entries<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_queue_routingruleitem"></a> queue_routingruleitem

Same as routingruleitem entity [queue_routingruleitem](routingruleitem.md#BKMK_queue_routingruleitem) Many-To-One relationship.

**ReferencingEntity**: routingruleitem<br />
**ReferencingAttribute**: routedqueueid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: queue_routingruleitem<br />
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


### <a name="BKMK_queue_convertruleitem"></a> queue_convertruleitem

Same as convertruleitem entity [queue_convertruleitem](convertruleitem.md#BKMK_queue_convertruleitem) Many-To-One relationship.

**ReferencingEntity**: convertruleitem<br />
**ReferencingAttribute**: queueid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: queue_convertruleitem<br />
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


### <a name="BKMK_Queue_ProcessSessions"></a> Queue_ProcessSessions

Same as processsession entity [Queue_ProcessSessions](processsession.md#BKMK_Queue_ProcessSessions) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Queue_ProcessSessions<br />
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


### <a name="BKMK_queue_PostFollows"></a> queue_PostFollows

Same as postfollow entity [queue_PostFollows](postfollow.md#BKMK_queue_PostFollows) Many-To-One relationship.

**ReferencingEntity**: postfollow<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: queue_PostFollows<br />
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


### <a name="BKMK_convertrule_queue"></a> convertrule_queue

Same as convertrule entity [convertrule_queue](convertrule.md#BKMK_convertrule_queue) Many-To-One relationship.

**ReferencingEntity**: convertrule<br />
**ReferencingAttribute**: queueid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: convertrule_queue<br />
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


### <a name="BKMK_mailbox_regarding_queue"></a> mailbox_regarding_queue

Same as mailbox entity [mailbox_regarding_queue](mailbox.md#BKMK_mailbox_regarding_queue) Many-To-One relationship.

**ReferencingEntity**: mailbox<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: mailbox_regarding_queue<br />
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
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_Queue_BulkDeleteFailures"></a> Queue_BulkDeleteFailures

Same as bulkdeletefailure entity [Queue_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Queue_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Queue_BulkDeleteFailures<br />
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

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

See mailbox Entity [queue_defaultmailbox_mailbox](mailbox.md#BKMK_queue_defaultmailbox_mailbox) One-To-Many relationship.

### <a name="BKMK_business_unit_queues"></a> business_unit_queues

See businessunit Entity [business_unit_queues](businessunit.md#BKMK_business_unit_queues) One-To-Many relationship.

### <a name="BKMK_business_unit_queues2"></a> business_unit_queues2

See businessunit Entity [business_unit_queues2](businessunit.md#BKMK_business_unit_queues2) One-To-Many relationship.

### <a name="BKMK_lk_queue_modifiedonbehalfby"></a> lk_queue_modifiedonbehalfby

See systemuser Entity [lk_queue_modifiedonbehalfby](systemuser.md#BKMK_lk_queue_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_queues"></a> organization_queues

See organization Entity [organization_queues](organization.md#BKMK_organization_queues) One-To-Many relationship.

### <a name="BKMK_lk_queuebase_createdby"></a> lk_queuebase_createdby

See systemuser Entity [lk_queuebase_createdby](systemuser.md#BKMK_lk_queuebase_createdby) One-To-Many relationship.

### <a name="BKMK_lk_queuebase_modifiedby"></a> lk_queuebase_modifiedby

See systemuser Entity [lk_queuebase_modifiedby](systemuser.md#BKMK_lk_queuebase_modifiedby) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_Queue"></a> TransactionCurrency_Queue

See transactioncurrency Entity [TransactionCurrency_Queue](transactioncurrency.md#BKMK_TransactionCurrency_Queue) One-To-Many relationship.

### <a name="BKMK_queue_primary_user"></a> queue_primary_user

See systemuser Entity [queue_primary_user](systemuser.md#BKMK_queue_primary_user) One-To-Many relationship.

### <a name="BKMK_lk_queue_createdonbehalfby"></a> lk_queue_createdonbehalfby

See systemuser Entity [lk_queue_createdonbehalfby](systemuser.md#BKMK_lk_queue_createdonbehalfby) One-To-Many relationship.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the Queue entity is the first entity in the relationship. Listed by **SchemaName**.


### <a name="BKMK_queuemembership_association"></a> queuemembership_association

**IntersectEntityName**: queuemembership<br />
**Entity1LogicalName**: queue<br />

- **Entity1IntersectAttribute**: queueid
- **Entity1NavigationPropertyName**: queuemembership_association
- **Entity1AssociatedMenuConfiguration**:

  - **Behavior**: DoNotDisplay
  - **Group**: Details
  - **Label**: 
  - **Order**: 

**Entity2LogicalName**: [systemuser](systemuser.md)<br />

- **Entity2IntersectAttribute**: systemuserid
- **Entity2NavigationPropertyName**: queuemembership_association
- **Entity2AssociatedMenuConfiguration**:

  - **Behavior**: DoNotDisplay
  - **Group**: Details
  - **Label**: 
  - **Order**: 

**IsCustomizable**: False<br />
queue

