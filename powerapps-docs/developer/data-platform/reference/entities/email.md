---
title: "Email table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Email table/entity."
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

# Email table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Activity that is delivered using email protocols.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/emails(*activityid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|BackgroundSendEmail|<xref href="Microsoft.Dynamics.CRM.BackgroundSendEmail?text=BackgroundSendEmail Action" />|<xref:Microsoft.Crm.Sdk.Messages.BackgroundSendEmailRequest>|
|CheckIncomingEmail|<xref href="Microsoft.Dynamics.CRM.CheckIncomingEmail?text=CheckIncomingEmail Function" />|<xref:Microsoft.Crm.Sdk.Messages.CheckIncomingEmailRequest>|
|CheckPromoteEmail|<xref href="Microsoft.Dynamics.CRM.CheckPromoteEmail?text=CheckPromoteEmail Function" />|<xref:Microsoft.Crm.Sdk.Messages.CheckPromoteEmailRequest>|
|Create|POST [*org URI*]/api/data/v9.0/emails<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/emails(*activityid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|DeliverImmediatePromoteEmail|<xref href="Microsoft.Dynamics.CRM.DeliverImmediatePromoteEmail?text=DeliverImmediatePromoteEmail Action" />|<xref:Microsoft.Crm.Sdk.Messages.DeliverImmediatePromoteEmailRequest>|
|DeliverIncomingEmail|<xref href="Microsoft.Dynamics.CRM.DeliverIncomingEmail?text=DeliverIncomingEmail Action" />|<xref:Microsoft.Crm.Sdk.Messages.DeliverIncomingEmailRequest>|
|DeliverPromoteEmail|<xref href="Microsoft.Dynamics.CRM.DeliverPromoteEmail?text=DeliverPromoteEmail Action" />|<xref:Microsoft.Crm.Sdk.Messages.DeliverPromoteEmailRequest>|
|GetTrackingTokenEmail|<xref href="Microsoft.Dynamics.CRM.GetTrackingTokenEmail?text=GetTrackingTokenEmail Action" />|<xref:Microsoft.Crm.Sdk.Messages.GetTrackingTokenEmailRequest>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/emails(*activityid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/emails<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SendEmail|<xref href="Microsoft.Dynamics.CRM.SendEmail?text=SendEmail Action" />|<xref:Microsoft.Crm.Sdk.Messages.SendEmailRequest>|
|SendEmailFromTemplate|<xref href="Microsoft.Dynamics.CRM.SendEmailFromTemplate?text=SendEmailFromTemplate Action" />|<xref:Microsoft.Crm.Sdk.Messages.SendEmailFromTemplateRequest>|
|SendFax|<xref href="Microsoft.Dynamics.CRM.SendFax?text=SendFax Action" />|<xref:Microsoft.Crm.Sdk.Messages.SendFaxRequest>|
|SendTemplate|<xref href="Microsoft.Dynamics.CRM.SendTemplate?text=SendTemplate Action" />|<xref:Microsoft.Crm.Sdk.Messages.SendTemplateRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/emails(*activityid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/emails(*activityid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|Emails|
|DisplayCollectionName|Email Messages|
|DisplayName|Email|
|EntitySetName|emails|
|IsBPFEntity|False|
|LogicalCollectionName|emails|
|LogicalName|email|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|activityid|
|PrimaryNameAttribute|subject|
|SchemaName|Email|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AcceptingEntityId](#BKMK_AcceptingEntityId)
- [AcceptingEntityIdName](#BKMK_AcceptingEntityIdName)
- [AcceptingEntityTypeCode](#BKMK_AcceptingEntityTypeCode)
- [ActivityAdditionalParams](#BKMK_ActivityAdditionalParams)
- [ActivityId](#BKMK_ActivityId)
- [ActualDurationMinutes](#BKMK_ActualDurationMinutes)
- [ActualEnd](#BKMK_ActualEnd)
- [ActualStart](#BKMK_ActualStart)
- [AttachmentOpenCount](#BKMK_AttachmentOpenCount)
- [BaseConversationIndexHash](#BKMK_BaseConversationIndexHash)
- [bcc](#BKMK_bcc)
- [Category](#BKMK_Category)
- [cc](#BKMK_cc)
- [ConversationTrackingId](#BKMK_ConversationTrackingId)
- [CorrelatedActivityId](#BKMK_CorrelatedActivityId)
- [DelayedEmailSendTime](#BKMK_DelayedEmailSendTime)
- [DeliveryAttempts](#BKMK_DeliveryAttempts)
- [DeliveryPriorityCode](#BKMK_DeliveryPriorityCode)
- [DeliveryReceiptRequested](#BKMK_DeliveryReceiptRequested)
- [Description](#BKMK_Description)
- [DirectionCode](#BKMK_DirectionCode)
- [EmailReminderExpiryTime](#BKMK_EmailReminderExpiryTime)
- [EmailReminderText](#BKMK_EmailReminderText)
- [EmailReminderType](#BKMK_EmailReminderType)
- [EmailSenderName](#BKMK_EmailSenderName)
- [EmailTrackingId](#BKMK_EmailTrackingId)
- [FollowEmailUserPreference](#BKMK_FollowEmailUserPreference)
- [from](#BKMK_from)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsBilled](#BKMK_IsBilled)
- [IsWorkflowCreated](#BKMK_IsWorkflowCreated)
- [LastOnHoldTime](#BKMK_LastOnHoldTime)
- [LastOpenedTime](#BKMK_LastOpenedTime)
- [LinksClickedCount](#BKMK_LinksClickedCount)
- [MessageId](#BKMK_MessageId)
- [MessageIdDupCheck](#BKMK_MessageIdDupCheck)
- [MimeType](#BKMK_MimeType)
- [Notifications](#BKMK_Notifications)
- [OpenCount](#BKMK_OpenCount)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [ParentActivityId](#BKMK_ParentActivityId)
- [PriorityCode](#BKMK_PriorityCode)
- [ProcessId](#BKMK_ProcessId)
- [ReadReceiptRequested](#BKMK_ReadReceiptRequested)
- [ReceivingMailboxId](#BKMK_ReceivingMailboxId)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [ReminderActionCardId](#BKMK_ReminderActionCardId)
- [ReservedForInternalUse](#BKMK_ReservedForInternalUse)
- [ScheduledEnd](#BKMK_ScheduledEnd)
- [ScheduledStart](#BKMK_ScheduledStart)
- [Sender](#BKMK_Sender)
- [SendersAccountName](#BKMK_SendersAccountName)
- [SLAId](#BKMK_SLAId)
- [SortDate](#BKMK_SortDate)
- [StageId](#BKMK_StageId)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [Subcategory](#BKMK_Subcategory)
- [Subject](#BKMK_Subject)
- [SubmittedBy](#BKMK_SubmittedBy)
- [TemplateId](#BKMK_TemplateId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [to](#BKMK_to)
- [ToRecipients](#BKMK_ToRecipients)
- [TrackingToken](#BKMK_TrackingToken)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [TraversedPath](#BKMK_TraversedPath)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_AcceptingEntityId"></a> AcceptingEntityId

**Added by**: msft_ActivitiesInfra_Extensions Solution

|Property|Value|
|--------|-----|
|Description|The Entity that Accepted the Email|
|DisplayName|Accepting Entity|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|acceptingentityid|
|RequiredLevel|None|
|Targets|queue,systemuser|
|Type|Lookup|


### <a name="BKMK_AcceptingEntityIdName"></a> AcceptingEntityIdName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Accepting Entity Name|
|DisplayName|Accepting Entity Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|acceptingentityidname|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_AcceptingEntityTypeCode"></a> AcceptingEntityTypeCode

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Accepting Entity Object Type.|
|DisplayName|Accepting User Or Queue Object Type|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|acceptingentitytypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_ActivityAdditionalParams"></a> ActivityAdditionalParams

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Additional Parameters|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|activityadditionalparams|
|MaxLength|8192|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_ActivityId"></a> ActivityId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the email activity.|
|DisplayName|Email Message|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|activityid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ActualDurationMinutes"></a> ActualDurationMinutes

|Property|Value|
|--------|-----|
|Description|Type the number of minutes spent creating and sending the email. The duration is used in reporting.|
|DisplayName|Duration|
|Format|Duration|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|actualdurationminutes|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ActualEnd"></a> ActualEnd

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Enter the actual end date and time of the email. By default, it displays the date and time when the activity was completed or canceled, but can be edited to capture the actual time to create and send the email.|
|DisplayName|Actual End|
|Format|DateOnly|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|actualend|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ActualStart"></a> ActualStart

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Enter the actual start date and time for the email. By default, it displays the date and time when the activity was created, but can be edited to capture the actual time to create and send the email.|
|DisplayName|Actual Start|
|Format|DateOnly|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|actualstart|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_AttachmentOpenCount"></a> AttachmentOpenCount

|Property|Value|
|--------|-----|
|Description|Shows the number of times an email attachment has been viewed.|
|DisplayName|Attachment Open Count|
|Format|None|
|IsValidForCreate|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|attachmentopencount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_BaseConversationIndexHash"></a> BaseConversationIndexHash

|Property|Value|
|--------|-----|
|Description|Hash of base of conversation index.|
|DisplayName|Conversation Index (Hash)|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|baseconversationindexhash|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_bcc"></a> bcc

|Property|Value|
|--------|-----|
|Description|Enter the recipients that are included on the email distribution, but are not displayed to other recipients.|
|DisplayName|Bcc|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|bcc|
|RequiredLevel|None|
|Targets|account,contact,knowledgearticle,queue,systemuser,unresolvedaddress|
|Type|PartyList|


### <a name="BKMK_Category"></a> Category

|Property|Value|
|--------|-----|
|Description|Type a category to identify the email type, such as lead outreach, customer follow-up, or service alert, to tie the email to a business group or function.|
|DisplayName|Category|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|category|
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_cc"></a> cc

|Property|Value|
|--------|-----|
|Description|Enter the recipients that should be copied on the email.|
|DisplayName|Cc|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|cc|
|RequiredLevel|None|
|Targets|account,contact,knowledgearticle,queue,systemuser,unresolvedaddress|
|Type|PartyList|


### <a name="BKMK_ConversationTrackingId"></a> ConversationTrackingId

|Property|Value|
|--------|-----|
|Description|Conversation Tracking Id.|
|DisplayName|Conversation Tracking Id|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|conversationtrackingid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_CorrelatedActivityId"></a> CorrelatedActivityId

**Added by**: msft_ActivitiesInfra_Extensions Solution

|Property|Value|
|--------|-----|
|Description|Correlated Activity Id|
|DisplayName|Correlated Activity Id|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|correlatedactivityid|
|RequiredLevel|None|
|Targets|email|
|Type|Lookup|


### <a name="BKMK_DelayedEmailSendTime"></a> DelayedEmailSendTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Enter the expected date and time when email will be sent.|
|DisplayName|Send Later|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|delayedemailsendtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_DeliveryAttempts"></a> DeliveryAttempts

|Property|Value|
|--------|-----|
|Description|Shows the count of the number of attempts made to send the email. The count is used as an indicator of email routing issues.|
|DisplayName|No. of Delivery Attempts|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|deliveryattempts|
|MaxValue|1000000000|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_DeliveryPriorityCode"></a> DeliveryPriorityCode

|Property|Value|
|--------|-----|
|Description|Select the priority of delivery of the email to the email server.|
|DisplayName|Delivery Priority|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|deliveryprioritycode|
|RequiredLevel|None|
|Type|Picklist|

#### DeliveryPriorityCode Choices/Options

|Value|Label|
|-----|-----|
|0|Low|
|1|Normal|
|2|High|



### <a name="BKMK_DeliveryReceiptRequested"></a> DeliveryReceiptRequested

|Property|Value|
|--------|-----|
|Description|Select whether the sender should receive confirmation that the email was delivered.|
|DisplayName|Delivery Receipt Requested|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|deliveryreceiptrequested|
|RequiredLevel|None|
|Type|Boolean|

#### DeliveryReceiptRequested Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Type the greeting and message text of the email.|
|DisplayName|Description|
|Format|Email|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_DirectionCode"></a> DirectionCode

|Property|Value|
|--------|-----|
|Description|Select the direction of the email as incoming or outbound.|
|DisplayName|Direction|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|directioncode|
|RequiredLevel|None|
|Type|Boolean|

#### DirectionCode Choices/Options

|Value|Label|
|-----|-----|
|1|Outgoing|
|0|Incoming|

**DefaultValue**: True



### <a name="BKMK_EmailReminderExpiryTime"></a> EmailReminderExpiryTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when an email reminder expires.|
|DisplayName|Email Reminder Expiry Time|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|emailreminderexpirytime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_EmailReminderText"></a> EmailReminderText

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Email Reminder Text|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|emailremindertext|
|MaxLength|1250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EmailReminderType"></a> EmailReminderType

|Property|Value|
|--------|-----|
|Description|Shows the type of the email reminder.|
|DisplayName|Email Reminder Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|emailremindertype|
|RequiredLevel|None|
|Type|Picklist|

#### EmailReminderType Choices/Options

|Value|Label|
|-----|-----|
|0|If I do not receive a reply by|
|1|If the email is not opened by|
|2|Remind me anyways at|



### <a name="BKMK_EmailSenderName"></a> EmailSenderName

|Property|Value|
|--------|-----|
|Description|Shows the name of the sender of the email.|
|DisplayName|Email Sender Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|emailsendername|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EmailTrackingId"></a> EmailTrackingId

|Property|Value|
|--------|-----|
|Description|Email Tracking Id.|
|DisplayName|Email Tracking Id|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|emailtrackingid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_FollowEmailUserPreference"></a> FollowEmailUserPreference

|Property|Value|
|--------|-----|
|Description|Select whether the email allows following recipient activities sent from Microsoft Dynamics 365.This is user preference state which can be overridden by system evaluated state.|
|DisplayName|Following|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|followemailuserpreference|
|RequiredLevel|None|
|Type|Boolean|

#### FollowEmailUserPreference Choices/Options

|Value|Label|
|-----|-----|
|1|True|
|0|False|

**DefaultValue**: False



### <a name="BKMK_from"></a> from

|Property|Value|
|--------|-----|
|Description|Enter the sender of the email.|
|DisplayName|From|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|from|
|RequiredLevel|None|
|Targets|queue,systemuser|
|Type|PartyList|


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


### <a name="BKMK_IsBilled"></a> IsBilled

|Property|Value|
|--------|-----|
|Description|Information regarding whether the email activity was billed as part of resolving a case.|
|DisplayName|Is Billed|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isbilled|
|RequiredLevel|None|
|Type|Boolean|

#### IsBilled Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsWorkflowCreated"></a> IsWorkflowCreated

|Property|Value|
|--------|-----|
|Description|Indication if the email was created by a workflow rule.|
|DisplayName|Is Workflow Created|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isworkflowcreated|
|RequiredLevel|None|
|Type|Boolean|

#### IsWorkflowCreated Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_LastOnHoldTime"></a> LastOnHoldTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Contains the date and time stamp of the last on hold time.|
|DisplayName|Last On Hold Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastonholdtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_LastOpenedTime"></a> LastOpenedTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the latest date and time when email was opened.|
|DisplayName|Last Opened Time|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|lastopenedtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_LinksClickedCount"></a> LinksClickedCount

|Property|Value|
|--------|-----|
|Description|Shows the number of times a link in an email has been clicked.|
|DisplayName|Links Clicked Count|
|Format|None|
|IsValidForCreate|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|linksclickedcount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_MessageId"></a> MessageId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the email message. Used only for email that is received.|
|DisplayName|Message ID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|messageid|
|MaxLength|320|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_MessageIdDupCheck"></a> MessageIdDupCheck

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Message ID Dup Check|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|messageiddupcheck|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_MimeType"></a> MimeType

|Property|Value|
|--------|-----|
|Description|MIME type of the email message data.|
|DisplayName|Mime Type|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mimetype|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Notifications"></a> Notifications

|Property|Value|
|--------|-----|
|Description|Select the notification code to identify issues with the email recipients or attachments, such as blocked attachments.|
|DisplayName|Notifications|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|notifications|
|RequiredLevel|None|
|Type|Picklist|

#### Notifications Choices/Options

|Value|Label|
|-----|-----|
|0|None|
|1|The message was saved as a Microsoft Dynamics 365 email record, but not all the attachments could be saved with it. An attachment cannot be saved if it is blocked or if its file type is invalid.|
|2|Truncated body.|



### <a name="BKMK_OpenCount"></a> OpenCount

|Property|Value|
|--------|-----|
|Description|Shows the number of times an email has been opened.|
|DisplayName|Open Count|
|Format|None|
|IsValidForCreate|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|opencount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


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
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_ParentActivityId"></a> ParentActivityId

|Property|Value|
|--------|-----|
|Description|Select the activity that the email is associated with.|
|DisplayName|Parent Activity Id|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|parentactivityid|
|RequiredLevel|None|
|Targets|email|
|Type|Lookup|


### <a name="BKMK_PriorityCode"></a> PriorityCode

|Property|Value|
|--------|-----|
|Description|Select the priority so that preferred customers or critical issues are handled quickly.|
|DisplayName|Priority|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|prioritycode|
|RequiredLevel|None|
|Type|Picklist|

#### PriorityCode Choices/Options

|Value|Label|
|-----|-----|
|0|Low|
|1|Normal|
|2|High|



### <a name="BKMK_ProcessId"></a> ProcessId

|Property|Value|
|--------|-----|
|Description|Shows the ID of the process.|
|DisplayName|Process|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|processid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_ReadReceiptRequested"></a> ReadReceiptRequested

|Property|Value|
|--------|-----|
|Description|Indicates that a read receipt is requested.|
|DisplayName|Read Receipt Requested|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|readreceiptrequested|
|RequiredLevel|None|
|Type|Boolean|

#### ReadReceiptRequested Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_ReceivingMailboxId"></a> ReceivingMailboxId

**Added by**: msft_ActivitiesInfra_Extensions Solution

|Property|Value|
|--------|-----|
|Description|The Mailbox that Received the Email.|
|DisplayName|Receiving Mailbox|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|receivingmailboxid|
|RequiredLevel|None|
|Targets|mailbox|
|Type|Lookup|


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|--------|-----|
|Description|Choose the record that the email relates to.|
|DisplayName|Regarding|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|regardingobjectid|
|RequiredLevel|None|
|Targets|account,asyncoperation,contact,knowledgearticle,knowledgebaserecord|
|Type|Lookup|


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjecttypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_ReminderActionCardId"></a> ReminderActionCardId

|Property|Value|
|--------|-----|
|Description|Reminder Action Card Id.|
|DisplayName|Reminder Action Card Id.|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|reminderactioncardid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_ReservedForInternalUse"></a> ReservedForInternalUse

**Added by**: Activities Patch Solution

|Property|Value|
|--------|-----|
|Description|For internal use only|
|DisplayName|Reserved for internal use|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|reservedforinternaluse|
|MaxLength|40000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_ScheduledEnd"></a> ScheduledEnd

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Enter the expected due date and time for the activity to be completed to provide details about when the email will be sent.|
|DisplayName|Due Date|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|scheduledend|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ScheduledStart"></a> ScheduledStart

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Enter the expected start date and time for the activity to provide details about the tentative time when the email activity must be initiated.|
|DisplayName|Start Date|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|scheduledstart|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_Sender"></a> Sender

|Property|Value|
|--------|-----|
|Description|Sender of the email.|
|DisplayName|From|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|sender|
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SendersAccountName"></a> SendersAccountName

|Property|Value|
|--------|-----|
|Description|Shows the name of the sender account of the email.|
|DisplayName|Email Sender Account Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|sendersaccountname|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SLAId"></a> SLAId

|Property|Value|
|--------|-----|
|Description|Choose the service level agreement (SLA) that you want to apply to the email record.|
|DisplayName|SLA|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|slaid|
|RequiredLevel|None|
|Targets|sla|
|Type|Lookup|


### <a name="BKMK_SortDate"></a> SortDate

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time by which the activities are sorted.|
|DisplayName|Sort Date|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|sortdate|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_StageId"></a> StageId

|Property|Value|
|--------|-----|
|Description|Shows the ID of the stage.|
|DisplayName|(Deprecated) Process Stage|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|stageid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|--------|-----|
|Description|Shows whether the email is open, completed, or canceled. Completed and canceled email is read-only and can't be edited.|
|DisplayName|Activity Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### StateCode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Open|1|Open|
|1|Completed|2|Completed|
|2|Canceled|5|Canceled|



### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|--------|-----|
|Description|Select the email's status.|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### StatusCode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Draft|0|
|2|Completed|1|
|3|Sent|1|
|4|Received|1|
|5|Canceled|2|
|6|Pending Send|1|
|7|Sending|1|
|8|Failed|0|



### <a name="BKMK_Subcategory"></a> Subcategory

|Property|Value|
|--------|-----|
|Description|Type a subcategory to identify the email type and relate the activity to a specific product, sales region, business group, or other function.|
|DisplayName|Sub-Category|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|subcategory|
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Subject"></a> Subject

|Property|Value|
|--------|-----|
|Description|Type a short description about the objective or primary topic of the email.|
|DisplayName|Subject|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|subject|
|MaxLength|800|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SubmittedBy"></a> SubmittedBy

|Property|Value|
|--------|-----|
|Description|Shows the Microsoft Office Outlook account for the user who submitted the email to Microsoft Dynamics 365.|
|DisplayName|Submitted By|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|submittedby|
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TemplateId"></a> TemplateId

|Property|Value|
|--------|-----|
|Description|For internal use only. ID for template used in email.|
|DisplayName|ID for template used.|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|templateid|
|RequiredLevel|None|
|Targets|template|
|Type|Lookup|


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


### <a name="BKMK_to"></a> to

|Property|Value|
|--------|-----|
|Description|Enter the account, contact, lead, queue, or user recipients for the email.|
|DisplayName|To|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|to|
|RequiredLevel|None|
|Targets|account,contact,knowledgearticle,queue,systemuser,unresolvedaddress|
|Type|PartyList|


### <a name="BKMK_ToRecipients"></a> ToRecipients

|Property|Value|
|--------|-----|
|Description|Shows the email addresses corresponding to the recipients.|
|DisplayName|To Recipients|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|torecipients|
|MaxLength|500|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TrackingToken"></a> TrackingToken

|Property|Value|
|--------|-----|
|Description|Shows the tracking token assigned to the email to make sure responses are automatically tracked in Microsoft Dynamics 365.|
|DisplayName|Tracking Token|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|trackingtoken|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|--------|-----|
|Description|Choose the local currency for the record to make sure budgets are reported in the correct currency.|
|DisplayName|Currency|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|transactioncurrencyid|
|RequiredLevel|None|
|Targets|transactioncurrency|
|Type|Lookup|


### <a name="BKMK_TraversedPath"></a> TraversedPath

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|(Deprecated) Traversed Path|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|traversedpath|
|MaxLength|1250|
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

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ActivityTypeCode](#BKMK_ActivityTypeCode)
- [AttachmentCount](#BKMK_AttachmentCount)
- [Compressed](#BKMK_Compressed)
- [ConversationIndex](#BKMK_ConversationIndex)
- [CorrelatedActivityIdName](#BKMK_CorrelatedActivityIdName)
- [CorrelationMethod](#BKMK_CorrelationMethod)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [EmailReminderStatus](#BKMK_EmailReminderStatus)
- [EmailSender](#BKMK_EmailSender)
- [EmailSenderObjectTypeCode](#BKMK_EmailSenderObjectTypeCode)
- [EmailSenderYomiName](#BKMK_EmailSenderYomiName)
- [ExchangeRate](#BKMK_ExchangeRate)
- [InReplyTo](#BKMK_InReplyTo)
- [IsEmailFollowed](#BKMK_IsEmailFollowed)
- [IsEmailReminderSet](#BKMK_IsEmailReminderSet)
- [IsRegularActivity](#BKMK_IsRegularActivity)
- [IsUnsafe](#BKMK_IsUnsafe)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OnHoldTime](#BKMK_OnHoldTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [ParentActivityIdName](#BKMK_ParentActivityIdName)
- [PostponeEmailProcessingUntil](#BKMK_PostponeEmailProcessingUntil)
- [ReceivingMailboxIdName](#BKMK_ReceivingMailboxIdName)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectIdYomiName](#BKMK_RegardingObjectIdYomiName)
- [ReplyCount](#BKMK_ReplyCount)
- [SafeDescription](#BKMK_SafeDescription)
- [ScheduledDurationMinutes](#BKMK_ScheduledDurationMinutes)
- [SenderMailboxId](#BKMK_SenderMailboxId)
- [SenderMailboxIdName](#BKMK_SenderMailboxIdName)
- [SendersAccount](#BKMK_SendersAccount)
- [SendersAccountObjectTypeCode](#BKMK_SendersAccountObjectTypeCode)
- [SendersAccountYomiName](#BKMK_SendersAccountYomiName)
- [SentOn](#BKMK_SentOn)
- [SLAInvokedId](#BKMK_SLAInvokedId)
- [SLAInvokedIdName](#BKMK_SLAInvokedIdName)
- [SLAName](#BKMK_SLAName)
- [TemplateIdName](#BKMK_TemplateIdName)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ActivityTypeCode"></a> ActivityTypeCode

|Property|Value|
|--------|-----|
|Description|Shows the type of activity.|
|DisplayName|Activity Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|activitytypecode|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_AttachmentCount"></a> AttachmentCount

|Property|Value|
|--------|-----|
|Description|Shows the umber of attachments of the email message.|
|DisplayName|Attachment Count|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|attachmentcount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_Compressed"></a> Compressed

|Property|Value|
|--------|-----|
|Description|Indicates if the body is compressed.|
|DisplayName|Compression|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|compressed|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### Compressed Choices/Options

|Value|Label|
|-----|-----|
|1|Compressed|
|0|Not compressed|

**DefaultValue**: False



### <a name="BKMK_ConversationIndex"></a> ConversationIndex

|Property|Value|
|--------|-----|
|Description|Identifier for all the email responses for this conversation.|
|DisplayName|Conversation Index|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|conversationindex|
|MaxLength|2048|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CorrelatedActivityIdName"></a> CorrelatedActivityIdName

**Added by**: msft_ActivitiesInfra_Extensions Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|correlatedactivityidname|
|MaxLength|800|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CorrelationMethod"></a> CorrelationMethod

|Property|Value|
|--------|-----|
|Description|Shows how an email is matched to an existing email in Microsoft Dynamics 365. For system use only.|
|DisplayName|Correlation Method|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|correlationmethod|
|RequiredLevel|None|
|Type|Picklist|

#### CorrelationMethod Choices/Options

|Value|Label|
|-----|-----|
|0|None|
|1|Skipped|
|2|XHeader|
|3|InReplyTo|
|4|TrackingToken|
|5|ConversationIndex|
|6|SmartMatching|
|7|CustomCorrelation|



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
|RequiredLevel|None|
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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EmailReminderStatus"></a> EmailReminderStatus

|Property|Value|
|--------|-----|
|Description|Shows the status of the email reminder.|
|DisplayName|Email Reminder Status|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|emailreminderstatus|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### EmailReminderStatus Choices/Options

|Value|Label|
|-----|-----|
|0|NotSet|
|1|ReminderSet|
|2|ReminderExpired|
|3|ReminderInvalid|



### <a name="BKMK_EmailSender"></a> EmailSender

|Property|Value|
|--------|-----|
|Description|Shows the sender of the email.|
|DisplayName|Sender|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|emailsender|
|RequiredLevel|None|
|Targets|account,contact,queue,systemuser|
|Type|Lookup|


### <a name="BKMK_EmailSenderObjectTypeCode"></a> EmailSenderObjectTypeCode

|Property|Value|
|--------|-----|
|Description|Shows the object type of sender of the email.|
|DisplayName|Email Sender Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|emailsenderobjecttypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_EmailSenderYomiName"></a> EmailSenderYomiName

|Property|Value|
|--------|-----|
|Description|Shows the yomi name of the email sender|
|DisplayName|Email Sender yomi Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|emailsenderyominame|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|--------|-----|
|Description|Shows the conversion rate of the record's currency. The exchange rate is used to convert all money fields in the record from the local currency to the system's default currency.|
|DisplayName|Exchange Rate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.0000000001|
|Precision|10|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_InReplyTo"></a> InReplyTo

|Property|Value|
|--------|-----|
|Description|Type the ID of the email message that this email activity is a response to.|
|DisplayName|In Reply To Message|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|inreplyto|
|MaxLength|320|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IsEmailFollowed"></a> IsEmailFollowed

|Property|Value|
|--------|-----|
|Description|For internal use only. Shows whether this email is followed. This is evaluated state which overrides user selection of follow email.|
|DisplayName|Followed|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isemailfollowed|
|RequiredLevel|None|
|Type|Boolean|

#### IsEmailFollowed Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsEmailReminderSet"></a> IsEmailReminderSet

|Property|Value|
|--------|-----|
|Description|For internal use only. Shows whether this email Reminder is Set.|
|DisplayName|Reminder Set|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isemailreminderset|
|RequiredLevel|None|
|Type|Boolean|

#### IsEmailReminderSet Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsRegularActivity"></a> IsRegularActivity

|Property|Value|
|--------|-----|
|Description|Information regarding whether the activity is a regular activity type or event type.|
|DisplayName|Is Regular Activity|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isregularactivity|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsRegularActivity Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsUnsafe"></a> IsUnsafe

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|IsUnsafe|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isunsafe|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


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
|RequiredLevel|None|
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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OnHoldTime"></a> OnHoldTime

|Property|Value|
|--------|-----|
|Description|Shows how long, in minutes, that the record was on hold.|
|DisplayName|On Hold Time (Minutes)|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|onholdtime|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


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
|Description|Unique identifier of the business unit that owns the email activity.|
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
|Description|Unique identifier of the team who owns the email activity.|
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
|Description|Unique identifier of the user who owns the email activity.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ParentActivityIdName"></a> ParentActivityIdName

|Property|Value|
|--------|-----|
|Description|Parent Activity Name|
|DisplayName|Parent Activity Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentactivityidname|
|MaxLength|800|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PostponeEmailProcessingUntil"></a> PostponeEmailProcessingUntil

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Delay email processing until|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|postponeemailprocessinguntil|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ReceivingMailboxIdName"></a> ReceivingMailboxIdName

**Added by**: msft_ActivitiesInfra_Extensions Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|receivingmailboxidname|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjectidname|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RegardingObjectIdYomiName"></a> RegardingObjectIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjectidyominame|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ReplyCount"></a> ReplyCount

|Property|Value|
|--------|-----|
|Description|Shows the number of replies received for an email.|
|DisplayName|Reply Count|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|replycount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_SafeDescription"></a> SafeDescription

|Property|Value|
|--------|-----|
|Description|Safe body text of the e-mail.|
|DisplayName|Safe Description|
|Format|Email|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|safedescription|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_ScheduledDurationMinutes"></a> ScheduledDurationMinutes

|Property|Value|
|--------|-----|
|Description|Scheduled duration of the email activity, specified in minutes.|
|DisplayName|Scheduled Duration|
|Format|Duration|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|scheduleddurationminutes|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_SenderMailboxId"></a> SenderMailboxId

|Property|Value|
|--------|-----|
|Description|Select the mailbox associated with the sender of the email message.|
|DisplayName|Sender's Mailbox|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|sendermailboxid|
|RequiredLevel|None|
|Targets|mailbox|
|Type|Lookup|


### <a name="BKMK_SenderMailboxIdName"></a> SenderMailboxIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|sendermailboxidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SendersAccount"></a> SendersAccount

|Property|Value|
|--------|-----|
|Description|Shows the parent account of the sender of the email.|
|DisplayName|Senders Account|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|sendersaccount|
|RequiredLevel|None|
|Targets|account|
|Type|Lookup|


### <a name="BKMK_SendersAccountObjectTypeCode"></a> SendersAccountObjectTypeCode

|Property|Value|
|--------|-----|
|Description|Shows the parent account type code of the sender of the email.|
|DisplayName| SendersAccount Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|sendersaccountobjecttypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_SendersAccountYomiName"></a> SendersAccountYomiName

|Property|Value|
|--------|-----|
|Description|Shows the name of the sender account yomi name |
|DisplayName|Email Sender Account yomi Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|sendersaccountyominame|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SentOn"></a> SentOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time that the email was sent.|
|DisplayName|Date Sent|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|senton|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_SLAInvokedId"></a> SLAInvokedId

|Property|Value|
|--------|-----|
|Description|Last SLA that was applied to this email. This field is for internal use only.|
|DisplayName|Last SLA applied|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|slainvokedid|
|RequiredLevel|None|
|Targets|sla|
|Type|Lookup|


### <a name="BKMK_SLAInvokedIdName"></a> SLAInvokedIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|slainvokedidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SLAName"></a> SLAName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|slaname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TemplateIdName"></a> TemplateIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|templateidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


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
|Description|Version number of the email message.|
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

- [email_actioncard](#BKMK_email_actioncard)
- [email_activity_parties](#BKMK_email_activity_parties)
- [Email_DuplicateMatchingRecord](#BKMK_Email_DuplicateMatchingRecord)
- [Email_SyncErrors](#BKMK_Email_SyncErrors)
- [Email_DuplicateBaseRecord](#BKMK_Email_DuplicateBaseRecord)
- [Email_AsyncOperations](#BKMK_Email_AsyncOperations)
- [Email_ProcessSessions](#BKMK_Email_ProcessSessions)
- [slakpiinstance_email](#BKMK_slakpiinstance_email)
- [Email_Annotation](#BKMK_Email_Annotation)
- [email_activity_mime_attachment](#BKMK_email_activity_mime_attachment)
- [email_email_parentactivityid](#BKMK_email_email_parentactivityid)
- [email_principalobjectattributeaccess](#BKMK_email_principalobjectattributeaccess)
- [Email_BulkDeleteFailures](#BKMK_Email_BulkDeleteFailures)
- [email_connections1](#BKMK_email_connections1)
- [email_connections2](#BKMK_email_connections2)
- [Email_QueueItem](#BKMK_Email_QueueItem)
- [email_email_CorrelatedActivityId](#BKMK_email_email_CorrelatedActivityId)


### <a name="BKMK_email_actioncard"></a> email_actioncard

Same as actioncard table [email_actioncard](actioncard.md#BKMK_email_actioncard) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|actioncard|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|email_actioncard|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_email_activity_parties"></a> email_activity_parties

Same as activityparty table [email_activity_parties](activityparty.md#BKMK_email_activity_parties) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activityparty|
|ReferencingAttribute|activityid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|email_activity_parties|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Email_DuplicateMatchingRecord"></a> Email_DuplicateMatchingRecord

Same as duplicaterecord table [Email_DuplicateMatchingRecord](duplicaterecord.md#BKMK_Email_DuplicateMatchingRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Email_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Email_SyncErrors"></a> Email_SyncErrors

Same as syncerror table [Email_SyncErrors](syncerror.md#BKMK_Email_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Email_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_Email_DuplicateBaseRecord"></a> Email_DuplicateBaseRecord

Same as duplicaterecord table [Email_DuplicateBaseRecord](duplicaterecord.md#BKMK_Email_DuplicateBaseRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Email_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Email_AsyncOperations"></a> Email_AsyncOperations

Same as asyncoperation table [Email_AsyncOperations](asyncoperation.md#BKMK_Email_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Email_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Email_ProcessSessions"></a> Email_ProcessSessions

Same as processsession table [Email_ProcessSessions](processsession.md#BKMK_Email_ProcessSessions) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Email_ProcessSessions|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 110|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_slakpiinstance_email"></a> slakpiinstance_email

Same as slakpiinstance table [slakpiinstance_email](slakpiinstance.md#BKMK_slakpiinstance_email) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|slakpiinstance|
|ReferencingAttribute|regarding|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|slakpiinstance_email|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Email_Annotation"></a> Email_Annotation

Same as annotation table [Email_Annotation](annotation.md#BKMK_Email_Annotation) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Email_Annotation|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_email_activity_mime_attachment"></a> email_activity_mime_attachment

Same as activitymimeattachment table [email_activity_mime_attachment](activitymimeattachment.md#BKMK_email_activity_mime_attachment) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitymimeattachment|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|email_activity_mime_attachment|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_email_email_parentactivityid"></a> email_email_parentactivityid

Same as email table [email_email_parentactivityid](email.md#BKMK_email_email_parentactivityid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|parentactivityid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|email_email_parentactivityid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_email_principalobjectattributeaccess"></a> email_principalobjectattributeaccess

Same as principalobjectattributeaccess table [email_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_email_principalobjectattributeaccess) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|email_principalobjectattributeaccess|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Email_BulkDeleteFailures"></a> Email_BulkDeleteFailures

Same as bulkdeletefailure table [Email_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Email_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Email_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_email_connections1"></a> email_connections1

Same as connection table [email_connections1](connection.md#BKMK_email_connections1) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record1id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|email_connections1|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_email_connections2"></a> email_connections2

Same as connection table [email_connections2](connection.md#BKMK_email_connections2) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record2id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|email_connections2|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Email_QueueItem"></a> Email_QueueItem

Same as queueitem table [Email_QueueItem](queueitem.md#BKMK_Email_QueueItem) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|queueitem|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Email_QueueItem|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_email_email_CorrelatedActivityId"></a> email_email_CorrelatedActivityId

**Added by**: msft_ActivitiesInfra_Extensions Solution

Same as email table [email_email_CorrelatedActivityId](email.md#BKMK_email_email_CorrelatedActivityId) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|correlatedactivityid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|email_email_CorrelatedActivityId|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [KnowledgeBaseRecord_Emails](#BKMK_KnowledgeBaseRecord_Emails)
- [lk_email_modifiedby](#BKMK_lk_email_modifiedby)
- [Account_Email_SendersAccount](#BKMK_Account_Email_SendersAccount)
- [Email_EmailTemplate](#BKMK_Email_EmailTemplate)
- [Queue_Email_EmailSender](#BKMK_Queue_Email_EmailSender)
- [Contact_Email_EmailSender](#BKMK_Contact_Email_EmailSender)
- [Account_Email_EmailSender](#BKMK_Account_Email_EmailSender)
- [TransactionCurrency_Email](#BKMK_TransactionCurrency_Email)
- [Contact_Emails](#BKMK_Contact_Emails)
- [user_email](#BKMK_user_email)
- [SystemUser_Email_EmailSender](#BKMK_SystemUser_Email_EmailSender)
- [AsyncOperation_Emails](#BKMK_AsyncOperation_Emails)
- [lk_email_createdonbehalfby](#BKMK_lk_email_createdonbehalfby)
- [KnowledgeArticle_Emails](#BKMK_KnowledgeArticle_Emails)
- [email_sendermailboxid_mailbox](#BKMK_email_sendermailboxid_mailbox)
- [activity_pointer_email](#BKMK_activity_pointer_email)
- [lk_email_modifiedonbehalfby](#BKMK_lk_email_modifiedonbehalfby)
- [team_email](#BKMK_team_email)
- [manualsla_email](#BKMK_manualsla_email)
- [business_unit_email_activities](#BKMK_business_unit_email_activities)
- [Account_Emails](#BKMK_Account_Emails)
- [email_email_parentactivityid](#BKMK_email_email_parentactivityid)
- [processstage_emails](#BKMK_processstage_emails)
- [sla_email](#BKMK_sla_email)
- [lk_email_createdby](#BKMK_lk_email_createdby)
- [email_email_CorrelatedActivityId](#BKMK_email_email_CorrelatedActivityId)
- [mailbox_email_ReceivingMailboxId](#BKMK_mailbox_email_ReceivingMailboxId)
- [email_acceptingentity_queue](#BKMK_email_acceptingentity_queue)
- [email_acceptingentity_systemuser](#BKMK_email_acceptingentity_systemuser)


### <a name="BKMK_KnowledgeBaseRecord_Emails"></a> KnowledgeBaseRecord_Emails

See knowledgebaserecord Table [KnowledgeBaseRecord_Emails](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_Emails) One-To-Many relationship.

### <a name="BKMK_lk_email_modifiedby"></a> lk_email_modifiedby

See systemuser Table [lk_email_modifiedby](systemuser.md#BKMK_lk_email_modifiedby) One-To-Many relationship.

### <a name="BKMK_Account_Email_SendersAccount"></a> Account_Email_SendersAccount

See account Table [Account_Email_SendersAccount](account.md#BKMK_Account_Email_SendersAccount) One-To-Many relationship.

### <a name="BKMK_Email_EmailTemplate"></a> Email_EmailTemplate

See template Table [Email_EmailTemplate](template.md#BKMK_Email_EmailTemplate) One-To-Many relationship.

### <a name="BKMK_Queue_Email_EmailSender"></a> Queue_Email_EmailSender

See queue Table [Queue_Email_EmailSender](queue.md#BKMK_Queue_Email_EmailSender) One-To-Many relationship.

### <a name="BKMK_Contact_Email_EmailSender"></a> Contact_Email_EmailSender

See contact Table [Contact_Email_EmailSender](contact.md#BKMK_Contact_Email_EmailSender) One-To-Many relationship.

### <a name="BKMK_Account_Email_EmailSender"></a> Account_Email_EmailSender

See account Table [Account_Email_EmailSender](account.md#BKMK_Account_Email_EmailSender) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_Email"></a> TransactionCurrency_Email

See transactioncurrency Table [TransactionCurrency_Email](transactioncurrency.md#BKMK_TransactionCurrency_Email) One-To-Many relationship.

### <a name="BKMK_Contact_Emails"></a> Contact_Emails

See contact Table [Contact_Emails](contact.md#BKMK_Contact_Emails) One-To-Many relationship.

### <a name="BKMK_user_email"></a> user_email

See systemuser Table [user_email](systemuser.md#BKMK_user_email) One-To-Many relationship.

### <a name="BKMK_SystemUser_Email_EmailSender"></a> SystemUser_Email_EmailSender

See systemuser Table [SystemUser_Email_EmailSender](systemuser.md#BKMK_SystemUser_Email_EmailSender) One-To-Many relationship.

### <a name="BKMK_AsyncOperation_Emails"></a> AsyncOperation_Emails

See asyncoperation Table [AsyncOperation_Emails](asyncoperation.md#BKMK_AsyncOperation_Emails) One-To-Many relationship.

### <a name="BKMK_lk_email_createdonbehalfby"></a> lk_email_createdonbehalfby

See systemuser Table [lk_email_createdonbehalfby](systemuser.md#BKMK_lk_email_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_KnowledgeArticle_Emails"></a> KnowledgeArticle_Emails

See knowledgearticle Table [KnowledgeArticle_Emails](knowledgearticle.md#BKMK_KnowledgeArticle_Emails) One-To-Many relationship.

### <a name="BKMK_email_sendermailboxid_mailbox"></a> email_sendermailboxid_mailbox

See mailbox Table [email_sendermailboxid_mailbox](mailbox.md#BKMK_email_sendermailboxid_mailbox) One-To-Many relationship.

### <a name="BKMK_activity_pointer_email"></a> activity_pointer_email

See activitypointer Table [activity_pointer_email](activitypointer.md#BKMK_activity_pointer_email) One-To-Many relationship.

### <a name="BKMK_lk_email_modifiedonbehalfby"></a> lk_email_modifiedonbehalfby

See systemuser Table [lk_email_modifiedonbehalfby](systemuser.md#BKMK_lk_email_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_team_email"></a> team_email

See team Table [team_email](team.md#BKMK_team_email) One-To-Many relationship.

### <a name="BKMK_manualsla_email"></a> manualsla_email

See sla Table [manualsla_email](sla.md#BKMK_manualsla_email) One-To-Many relationship.

### <a name="BKMK_business_unit_email_activities"></a> business_unit_email_activities

See businessunit Table [business_unit_email_activities](businessunit.md#BKMK_business_unit_email_activities) One-To-Many relationship.

### <a name="BKMK_Account_Emails"></a> Account_Emails

See account Table [Account_Emails](account.md#BKMK_Account_Emails) One-To-Many relationship.

### <a name="BKMK_email_email_parentactivityid"></a> email_email_parentactivityid

See email Table [email_email_parentactivityid](email.md#BKMK_email_email_parentactivityid) One-To-Many relationship.

### <a name="BKMK_processstage_emails"></a> processstage_emails

See processstage Table [processstage_emails](processstage.md#BKMK_processstage_emails) One-To-Many relationship.

### <a name="BKMK_sla_email"></a> sla_email

See sla Table [sla_email](sla.md#BKMK_sla_email) One-To-Many relationship.

### <a name="BKMK_lk_email_createdby"></a> lk_email_createdby

See systemuser Table [lk_email_createdby](systemuser.md#BKMK_lk_email_createdby) One-To-Many relationship.

### <a name="BKMK_email_email_CorrelatedActivityId"></a> email_email_CorrelatedActivityId

See email Table [email_email_CorrelatedActivityId](email.md#BKMK_email_email_CorrelatedActivityId) One-To-Many relationship.

### <a name="BKMK_mailbox_email_ReceivingMailboxId"></a> mailbox_email_ReceivingMailboxId

See mailbox Table [mailbox_email_ReceivingMailboxId](mailbox.md#BKMK_mailbox_email_ReceivingMailboxId) One-To-Many relationship.

### <a name="BKMK_email_acceptingentity_queue"></a> email_acceptingentity_queue

See queue Table [email_acceptingentity_queue](queue.md#BKMK_email_acceptingentity_queue) One-To-Many relationship.

### <a name="BKMK_email_acceptingentity_systemuser"></a> email_acceptingentity_systemuser

See systemuser Table [email_acceptingentity_systemuser](systemuser.md#BKMK_email_acceptingentity_systemuser) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.email?text=email EntityType" />