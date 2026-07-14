---
title: "Email table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Email table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Email table/entity reference (Microsoft Dataverse)

Activity that is delivered using email protocols.

## Messages

The following table lists the messages for the Email table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /emails(*activityid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `BackgroundSendEmail`<br />Event: True |<xref:Microsoft.Dynamics.CRM.BackgroundSendEmail?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.BackgroundSendEmailRequest>|
| `CheckIncomingEmail`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CheckIncomingEmail?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.CheckIncomingEmailRequest>|
| `CheckPromoteEmail`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CheckPromoteEmail?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.CheckPromoteEmailRequest>|
| `Create`<br />Event: True |`POST` /emails<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateAndSendNewEmail`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateAndSendNewEmail?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Delete`<br />Event: True |`DELETE` /emails(*activityid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `DeliverImmediatePromoteEmail`<br />Event: True |<xref:Microsoft.Dynamics.CRM.DeliverImmediatePromoteEmail?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.DeliverImmediatePromoteEmailRequest>|
| `DeliverIncomingEmail`<br />Event: True |<xref:Microsoft.Dynamics.CRM.DeliverIncomingEmail?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.DeliverIncomingEmailRequest>|
| `DeliverPromoteEmail`<br />Event: True |<xref:Microsoft.Dynamics.CRM.DeliverPromoteEmail?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.DeliverPromoteEmailRequest>|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GetDecryptionKey`<br />Event: False | |<xref:Microsoft.Crm.Sdk.Messages.GetDecryptionKeyRequest>|
| `GetTrackingTokenEmail`<br />Event: False |<xref:Microsoft.Dynamics.CRM.GetTrackingTokenEmail?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GetTrackingTokenEmailRequest>|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /emails(*activityid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /emails<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SendEmail`<br />Event: True |<xref:Microsoft.Dynamics.CRM.SendEmail?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.SendEmailRequest>|
| `SendEmailFromTemplate`<br />Event: True |<xref:Microsoft.Dynamics.CRM.SendEmailFromTemplate?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.SendEmailFromTemplateRequest>|
| `SendFax`<br />Event: True |<xref:Microsoft.Dynamics.CRM.SendFax?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.SendFaxRequest>|
| `SendTemplate`<br />Event: True |<xref:Microsoft.Dynamics.CRM.SendTemplate?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.SendTemplateRequest>|
| `SetState`<br />Event: True |`PATCH` /emails(*activityid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /emails(*activityid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /emails(*activityid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Email table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Email** |
| **DisplayCollectionName** | **Email Messages** |
| **SchemaName** | `Email` |
| **CollectionSchemaName** | `Emails` |
| **EntitySetName** | `emails`|
| **LogicalName** | `email` |
| **LogicalCollectionName** | `emails` |
| **PrimaryIdAttribute** | `activityid` |
| **PrimaryNameAttribute** |`subject` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AcceptingEntityId](#BKMK_AcceptingEntityId)
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
- [correlatedsubjectchanged](#BKMK_correlatedsubjectchanged)
- [DelayedEmailSendTime](#BKMK_DelayedEmailSendTime)
- [DeliveryAttempts](#BKMK_DeliveryAttempts)
- [DeliveryPriorityCode](#BKMK_DeliveryPriorityCode)
- [DeliveryReceiptRequested](#BKMK_DeliveryReceiptRequested)
- [Description](#BKMK_Description)
- [DirectionCode](#BKMK_DirectionCode)
- [EmailReminderExpiryTime](#BKMK_EmailReminderExpiryTime)
- [EmailReminderText](#BKMK_EmailReminderText)
- [EmailReminderType](#BKMK_EmailReminderType)
- [EmailTrackingId](#BKMK_EmailTrackingId)
- [FollowEmailUserPreference](#BKMK_FollowEmailUserPreference)
- [from](#BKMK_from)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [InternetMessageHeaders](#BKMK_InternetMessageHeaders)
- [IsBilled](#BKMK_IsBilled)
- [IsDuplicateSenderUnresolved](#BKMK_IsDuplicateSenderUnresolved)
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
- [PurviewRights](#BKMK_PurviewRights)
- [ReadReceiptRequested](#BKMK_ReadReceiptRequested)
- [ReceivingMailboxId](#BKMK_ReceivingMailboxId)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [related](#BKMK_related)
- [ReminderActionCardId](#BKMK_ReminderActionCardId)
- [ReservedForInternalUse](#BKMK_ReservedForInternalUse)
- [ScheduledEnd](#BKMK_ScheduledEnd)
- [ScheduledStart](#BKMK_ScheduledStart)
- [Sender](#BKMK_Sender)
- [SensitivityLabelId](#BKMK_SensitivityLabelId)
- [SensitivityLabelInfo](#BKMK_SensitivityLabelInfo)
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

|Property|Value|
|---|---|
|Description|**The Entity that Accepted the Email**|
|DisplayName|**Accepting Entity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`acceptingentityid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|queue, systemuser|

### <a name="BKMK_AcceptingEntityTypeCode"></a> AcceptingEntityTypeCode

|Property|Value|
|---|---|
|Description|**Accepting Entity Object Type.**|
|DisplayName|**Accepting User Or Queue Object Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`acceptingentitytypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_ActivityAdditionalParams"></a> ActivityAdditionalParams

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Additional Parameters**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`activityadditionalparams`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|8192|

### <a name="BKMK_ActivityId"></a> ActivityId

|Property|Value|
|---|---|
|Description|**Unique identifier of the email activity.**|
|DisplayName|**Email Message**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`activityid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ActualDurationMinutes"></a> ActualDurationMinutes

|Property|Value|
|---|---|
|Description|**Type the number of minutes spent creating and sending the email. The duration is used in reporting.**|
|DisplayName|**Duration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`actualdurationminutes`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ActualEnd"></a> ActualEnd

|Property|Value|
|---|---|
|Description|**Enter the actual end date and time of the email. By default, it displays the date and time when the activity was completed or canceled, but can be edited to capture the actual time to create and send the email.**|
|DisplayName|**Actual End**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`actualend`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ActualStart"></a> ActualStart

|Property|Value|
|---|---|
|Description|**Enter the actual start date and time for the email. By default, it displays the date and time when the activity was created, but can be edited to capture the actual time to create and send the email.**|
|DisplayName|**Actual Start**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`actualstart`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_AttachmentOpenCount"></a> AttachmentOpenCount

|Property|Value|
|---|---|
|Description|**Shows the number of times an email attachment has been viewed.**|
|DisplayName|**Attachment Open Count**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`attachmentopencount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_BaseConversationIndexHash"></a> BaseConversationIndexHash

|Property|Value|
|---|---|
|Description|**Hash of base of conversation index.**|
|DisplayName|**Conversation Index (Hash)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`baseconversationindexhash`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_bcc"></a> bcc

|Property|Value|
|---|---|
|Description|**Enter the recipients that are included on the email distribution, but are not displayed to other recipients.**|
|DisplayName|**Bcc**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`bcc`|
|RequiredLevel|None|
|Type|PartyList|
|Targets|account, contact, knowledgearticle, queue, systemuser, unresolvedaddress|

### <a name="BKMK_Category"></a> Category

|Property|Value|
|---|---|
|Description|**Type a category to identify the email type, such as lead outreach, customer follow-up, or service alert, to tie the email to a business group or function.**|
|DisplayName|**Category**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`category`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_cc"></a> cc

|Property|Value|
|---|---|
|Description|**Enter the recipients that should be copied on the email.**|
|DisplayName|**Cc**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cc`|
|RequiredLevel|None|
|Type|PartyList|
|Targets|account, contact, knowledgearticle, queue, systemuser, unresolvedaddress|

### <a name="BKMK_ConversationTrackingId"></a> ConversationTrackingId

|Property|Value|
|---|---|
|Description|**Conversation Tracking Id.**|
|DisplayName|**Conversation Tracking Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`conversationtrackingid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_CorrelatedActivityId"></a> CorrelatedActivityId

|Property|Value|
|---|---|
|Description|**Correlated Activity Id**|
|DisplayName|**Correlated Activity Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`correlatedactivityid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|email|

### <a name="BKMK_correlatedsubjectchanged"></a> correlatedsubjectchanged

|Property|Value|
|---|---|
|Description|**Indicates if the subject changed compared to the subject of the correlated email**|
|DisplayName|**Correlated subject changed**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`correlatedsubjectchanged`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`email_correlatedsubjectchanged`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_DelayedEmailSendTime"></a> DelayedEmailSendTime

|Property|Value|
|---|---|
|Description|**Enter the expected date and time when email will be sent.**|
|DisplayName|**Send Later**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`delayedemailsendtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_DeliveryAttempts"></a> DeliveryAttempts

|Property|Value|
|---|---|
|Description|**Shows the count of the number of attempts made to send the email. The count is used as an indicator of email routing issues.**|
|DisplayName|**No. of Delivery Attempts**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`deliveryattempts`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

### <a name="BKMK_DeliveryPriorityCode"></a> DeliveryPriorityCode

|Property|Value|
|---|---|
|Description|**Select the priority of delivery of the email to the email server.**|
|DisplayName|**Delivery Priority**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`deliveryprioritycode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`activitypointer_deliveryprioritycode`|

#### DeliveryPriorityCode Choices/Options

|Value|Label|
|---|---|
|0|**Low**|
|1|**Normal**|
|2|**High**|

### <a name="BKMK_DeliveryReceiptRequested"></a> DeliveryReceiptRequested

|Property|Value|
|---|---|
|Description|**Select whether the sender should receive confirmation that the email was delivered.**|
|DisplayName|**Delivery Receipt Requested**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`deliveryreceiptrequested`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`email_deliveryreceiptrequested`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Type the greeting and message text of the email.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Email|
|FormatName|Email|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_DirectionCode"></a> DirectionCode

|Property|Value|
|---|---|
|Description|**Select the direction of the email as incoming or outbound.**|
|DisplayName|**Direction**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`directioncode`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`email_directioncode`|
|DefaultValue|True|
|True Label|Outgoing|
|False Label|Incoming|

### <a name="BKMK_EmailReminderExpiryTime"></a> EmailReminderExpiryTime

|Property|Value|
|---|---|
|Description|**Shows the date and time when an email reminder expires.**|
|DisplayName|**Email Reminder Expiry Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`emailreminderexpirytime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_EmailReminderText"></a> EmailReminderText

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Email Reminder Text**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`emailremindertext`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1250|

### <a name="BKMK_EmailReminderType"></a> EmailReminderType

|Property|Value|
|---|---|
|Description|**Shows the type of the email reminder.**|
|DisplayName|**Email Reminder Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`emailremindertype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`email_remindertype`|

#### EmailReminderType Choices/Options

|Value|Label|
|---|---|
|0|**If I do not receive a reply by**|
|1|**If the email is not opened by**|
|2|**Remind me anyways at**|

### <a name="BKMK_EmailTrackingId"></a> EmailTrackingId

|Property|Value|
|---|---|
|Description|**Email Tracking Id.**|
|DisplayName|**Email Tracking Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`emailtrackingid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_FollowEmailUserPreference"></a> FollowEmailUserPreference

|Property|Value|
|---|---|
|Description|**Select whether the email allows following recipient activities sent from Microsoft Dynamics 365.This is user preference state which can be overridden by system evaluated state.**|
|DisplayName|**Following**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`followemailuserpreference`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`email_followuserpreference`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_from"></a> from

|Property|Value|
|---|---|
|Description|**Enter the sender of the email.**|
|DisplayName|**From**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`from`|
|RequiredLevel|None|
|Type|PartyList|
|Targets|queue, systemuser|

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

### <a name="BKMK_InternetMessageHeaders"></a> InternetMessageHeaders

|Property|Value|
|---|---|
|Description|**Contains a set of internet headers associated to the email message in json format**|
|DisplayName|**Internet message headers**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`internetmessageheaders`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_IsBilled"></a> IsBilled

|Property|Value|
|---|---|
|Description|**Information regarding whether the email activity was billed as part of resolving a case.**|
|DisplayName|**Is Billed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isbilled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`email_isbilled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsDuplicateSenderUnresolved"></a> IsDuplicateSenderUnresolved

|Property|Value|
|---|---|
|Description|**Indicates if the sender of the email is unresolved in case of multiple match**|
|DisplayName|**Is Duplicate Sender Unresolved**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isduplicatesenderunresolved`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`email_isduplicatesenderunresolved`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsWorkflowCreated"></a> IsWorkflowCreated

|Property|Value|
|---|---|
|Description|**Indication if the email was created by a workflow rule.**|
|DisplayName|**Is Workflow Created**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isworkflowcreated`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`email_isworkflowcreated`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_LastOnHoldTime"></a> LastOnHoldTime

|Property|Value|
|---|---|
|Description|**Contains the date and time stamp of the last on hold time.**|
|DisplayName|**Last On Hold Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastonholdtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_LastOpenedTime"></a> LastOpenedTime

|Property|Value|
|---|---|
|Description|**Shows the latest date and time when email was opened.**|
|DisplayName|**Last Opened Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastopenedtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_LinksClickedCount"></a> LinksClickedCount

|Property|Value|
|---|---|
|Description|**Shows the number of times a link in an email has been clicked.**|
|DisplayName|**Links Clicked Count**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`linksclickedcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_MessageId"></a> MessageId

|Property|Value|
|---|---|
|Description|**Unique identifier of the email message. Used only for email that is received.**|
|DisplayName|**Message ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`messageid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|320|

### <a name="BKMK_MessageIdDupCheck"></a> MessageIdDupCheck

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Message ID Dup Check**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`messageiddupcheck`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_MimeType"></a> MimeType

|Property|Value|
|---|---|
|Description|**MIME type of the email message data.**|
|DisplayName|**Mime Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mimetype`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_Notifications"></a> Notifications

|Property|Value|
|---|---|
|Description|**Select the notification code to identify issues with the email recipients or attachments, such as blocked attachments.**|
|DisplayName|**Notifications**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`notifications`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`email_notifications`|

#### Notifications Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**The message was saved as a Microsoft Dynamics 365 email record, but not all the attachments could be saved with it. An attachment cannot be saved if it is blocked or if its file type is invalid.**|
|2|**Truncated body.**|

### <a name="BKMK_OpenCount"></a> OpenCount

|Property|Value|
|---|---|
|Description|**Shows the number of times an email has been opened.**|
|DisplayName|**Open Count**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`opencount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

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
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_ParentActivityId"></a> ParentActivityId

|Property|Value|
|---|---|
|Description|**Select the activity that the email is associated with.**|
|DisplayName|**Parent Activity Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentactivityid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|email|

### <a name="BKMK_PriorityCode"></a> PriorityCode

|Property|Value|
|---|---|
|Description|**Select the priority so that preferred customers or critical issues are handled quickly.**|
|DisplayName|**Priority**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`prioritycode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`email_prioritycode`|

#### PriorityCode Choices/Options

|Value|Label|
|---|---|
|0|**Low**|
|1|**Normal**|
|2|**High**|

### <a name="BKMK_ProcessId"></a> ProcessId

|Property|Value|
|---|---|
|Description|**Shows the ID of the process.**|
|DisplayName|**Process**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_PurviewRights"></a> PurviewRights

|Property|Value|
|---|---|
|Description|**Purview Rights**|
|DisplayName|**Purview Rights**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`purviewrights`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_ReadReceiptRequested"></a> ReadReceiptRequested

|Property|Value|
|---|---|
|Description|**Indicates that a read receipt is requested.**|
|DisplayName|**Read Receipt Requested**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`readreceiptrequested`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`email_readreceiptrequested`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ReceivingMailboxId"></a> ReceivingMailboxId

|Property|Value|
|---|---|
|Description|**The Mailbox that Received the Email.**|
|DisplayName|**Receiving Mailbox**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`receivingmailboxid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mailbox|

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**Choose the record that the email relates to.**|
|DisplayName|**Regarding**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`regardingobjectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account, adx_invitation, asyncoperation, contact, knowledgearticle, knowledgebaserecord, mspp_adplacement, mspp_pollplacement, mspp_publishingstatetransitionrule, mspp_redirect, mspp_shortcut, mspp_website|

### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_related"></a> related

|Property|Value|
|---|---|
|Description|**Enter the related records for the email.**|
|DisplayName|**Related**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`related`|
|RequiredLevel|None|
|Type|PartyList|
|Targets|account, contact, knowledgearticle, queue, systemuser, unresolvedaddress|

### <a name="BKMK_ReminderActionCardId"></a> ReminderActionCardId

|Property|Value|
|---|---|
|Description|**Reminder Action Card Id.**|
|DisplayName|**Reminder Action Card Id.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`reminderactioncardid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ReservedForInternalUse"></a> ReservedForInternalUse

|Property|Value|
|---|---|
|Description|**For internal use only**|
|DisplayName|**Reserved for internal use**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`reservedforinternaluse`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|40000|

### <a name="BKMK_ScheduledEnd"></a> ScheduledEnd

|Property|Value|
|---|---|
|Description|**Enter the expected due date and time for the activity to be completed to provide details about when the email will be sent.**|
|DisplayName|**Due Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`scheduledend`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ScheduledStart"></a> ScheduledStart

|Property|Value|
|---|---|
|Description|**Enter the expected start date and time for the activity to provide details about the tentative time when the email activity must be initiated.**|
|DisplayName|**Start Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`scheduledstart`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_Sender"></a> Sender

|Property|Value|
|---|---|
|Description|**Sender of the email.**|
|DisplayName|**From**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sender`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_SensitivityLabelId"></a> SensitivityLabelId

|Property|Value|
|---|---|
|Description|**The sensitivity label assigned to the Email.**|
|DisplayName|**Sensitivity Label**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sensitivitylabelid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|sensitivitylabel|

### <a name="BKMK_SensitivityLabelInfo"></a> SensitivityLabelInfo

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Sensitivity Label Info**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sensitivitylabelinfo`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_SLAId"></a> SLAId

|Property|Value|
|---|---|
|Description|**Choose the service level agreement (SLA) that you want to apply to the email record.**|
|DisplayName|**SLA**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`slaid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|sla|

### <a name="BKMK_SortDate"></a> SortDate

|Property|Value|
|---|---|
|Description|**Shows the date and time by which the activities are sorted.**|
|DisplayName|**Sort Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sortdate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_StageId"></a> StageId

|Property|Value|
|---|---|
|Description|**Shows the ID of the stage.**|
|DisplayName|**(Deprecated) Process Stage**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`stageid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Shows whether the email is open, completed, or canceled. Completed and canceled email is read-only and can't be edited.**|
|DisplayName|**Activity Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`email_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Open**<br />DefaultStatus: 1<br />InvariantName: `Open`|
|1|Label: **Completed**<br />DefaultStatus: 2<br />InvariantName: `Completed`|
|2|Label: **Canceled**<br />DefaultStatus: 5<br />InvariantName: `Canceled`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Select the email's status.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`email_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Draft**<br />State:0<br />TransitionData: None|
|2|Label: **Completed**<br />State:1<br />TransitionData: None|
|3|Label: **Sent**<br />State:1<br />TransitionData: None|
|4|Label: **Received**<br />State:1<br />TransitionData: None|
|5|Label: **Canceled**<br />State:2<br />TransitionData: None|
|6|Label: **Pending Send**<br />State:1<br />TransitionData: None|
|7|Label: **Sending**<br />State:1<br />TransitionData: None|
|8|Label: **Failed**<br />State:0<br />TransitionData: None|

### <a name="BKMK_Subcategory"></a> Subcategory

|Property|Value|
|---|---|
|Description|**Type a subcategory to identify the email type and relate the activity to a specific product, sales region, business group, or other function.**|
|DisplayName|**Sub-Category**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`subcategory`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_Subject"></a> Subject

|Property|Value|
|---|---|
|Description|**Type a short description about the objective or primary topic of the email.**|
|DisplayName|**Subject**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`subject`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|800|

### <a name="BKMK_SubmittedBy"></a> SubmittedBy

|Property|Value|
|---|---|
|Description|**Shows the Microsoft Office Outlook account for the user who submitted the email to Microsoft Dynamics 365.**|
|DisplayName|**Submitted By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`submittedby`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_TemplateId"></a> TemplateId

|Property|Value|
|---|---|
|Description|**For internal use only. ID for template used in email.**|
|DisplayName|**ID for template used.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`templateid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|template|

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

### <a name="BKMK_to"></a> to

|Property|Value|
|---|---|
|Description|**Enter the account, contact, lead, queue, or user recipients for the email.**|
|DisplayName|**To**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`to`|
|RequiredLevel|None|
|Type|PartyList|
|Targets|account, contact, knowledgearticle, queue, systemuser, unresolvedaddress|

### <a name="BKMK_ToRecipients"></a> ToRecipients

|Property|Value|
|---|---|
|Description|**Shows the email addresses corresponding to the recipients.**|
|DisplayName|**To Recipients**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`torecipients`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_TrackingToken"></a> TrackingToken

|Property|Value|
|---|---|
|Description|**Shows the tracking token assigned to the email to make sure responses are automatically tracked in Microsoft Dynamics 365.**|
|DisplayName|**Tracking Token**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`trackingtoken`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Choose the local currency for the record to make sure budgets are reported in the correct currency.**|
|DisplayName|**Currency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`transactioncurrencyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|transactioncurrency|

### <a name="BKMK_TraversedPath"></a> TraversedPath

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**(Deprecated) Traversed Path**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`traversedpath`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1250|

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

- [ActivityTypeCode](#BKMK_ActivityTypeCode)
- [AttachmentCount](#BKMK_AttachmentCount)
- [Compressed](#BKMK_Compressed)
- [ConversationIndex](#BKMK_ConversationIndex)
- [CorrelationMethod](#BKMK_CorrelationMethod)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [DescriptionBlobId](#BKMK_DescriptionBlobId)
- [DescriptionBlobId_Name](#BKMK_DescriptionBlobId_Name)
- [EmailReminderStatus](#BKMK_EmailReminderStatus)
- [EmailSender](#BKMK_EmailSender)
- [EmailSenderObjectTypeCode](#BKMK_EmailSenderObjectTypeCode)
- [ExchangeRate](#BKMK_ExchangeRate)
- [InReplyTo](#BKMK_InReplyTo)
- [IsEmailFollowed](#BKMK_IsEmailFollowed)
- [IsEmailReminderSet](#BKMK_IsEmailReminderSet)
- [IsRegularActivity](#BKMK_IsRegularActivity)
- [IsSafeDescriptionTruncated](#BKMK_IsSafeDescriptionTruncated)
- [IsUnsafe](#BKMK_IsUnsafe)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OnHoldTime](#BKMK_OnHoldTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [ParentSensitivityLabelId](#BKMK_ParentSensitivityLabelId)
- [PostponeEmailProcessingUntil](#BKMK_PostponeEmailProcessingUntil)
- [ReplyCount](#BKMK_ReplyCount)
- [SafeDescription](#BKMK_SafeDescription)
- [ScheduledDurationMinutes](#BKMK_ScheduledDurationMinutes)
- [SenderMailboxId](#BKMK_SenderMailboxId)
- [SendersAccount](#BKMK_SendersAccount)
- [SendersAccountObjectTypeCode](#BKMK_SendersAccountObjectTypeCode)
- [SentOn](#BKMK_SentOn)
- [SLAInvokedId](#BKMK_SLAInvokedId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ActivityTypeCode"></a> ActivityTypeCode

|Property|Value|
|---|---|
|Description|**Shows the type of activity.**|
|DisplayName|**Activity Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`activitytypecode`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_AttachmentCount"></a> AttachmentCount

|Property|Value|
|---|---|
|Description|**Shows the umber of attachments of the email message.**|
|DisplayName|**Attachment Count**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`attachmentcount`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_Compressed"></a> Compressed

|Property|Value|
|---|---|
|Description|**Indicates if the body is compressed.**|
|DisplayName|**Compression**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`compressed`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`email_compressed`|
|DefaultValue|False|
|True Label|Compressed|
|False Label|Not compressed|

### <a name="BKMK_ConversationIndex"></a> ConversationIndex

|Property|Value|
|---|---|
|Description|**Identifier for all the email responses for this conversation.**|
|DisplayName|**Conversation Index**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`conversationindex`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2048|

### <a name="BKMK_CorrelationMethod"></a> CorrelationMethod

|Property|Value|
|---|---|
|Description|**Shows how an email is correlated to an existing email in Microsoft Dynamics 365. XHeader and CustomCorrelation are not used. For system use only.**|
|DisplayName|**Correlation Method**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`correlationmethod`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`email_correlationmethod`|

#### CorrelationMethod Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Skipped**|
|2|**XHeader**|
|3|**InReplyTo**|
|4|**TrackingToken**|
|5|**ConversationIndex**|
|6|**SmartMatching**|
|7|**CustomCorrelation**|

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

### <a name="BKMK_DescriptionBlobId"></a> DescriptionBlobId

|Property|Value|
|---|---|
|Description|**File that contains description content.**|
|DisplayName|**Description File Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`descriptionblobid`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|128000|

### <a name="BKMK_DescriptionBlobId_Name"></a> DescriptionBlobId_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`descriptionblobid_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_EmailReminderStatus"></a> EmailReminderStatus

|Property|Value|
|---|---|
|Description|**Shows the status of the email reminder.**|
|DisplayName|**Email Reminder Status**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`emailreminderstatus`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`email_reminderstatus`|

#### EmailReminderStatus Choices/Options

|Value|Label|
|---|---|
|0|**NotSet**|
|1|**ReminderSet**|
|2|**ReminderExpired**|
|3|**ReminderInvalid**|

### <a name="BKMK_EmailSender"></a> EmailSender

|Property|Value|
|---|---|
|Description|**Shows the sender of the email.**|
|DisplayName|**Sender**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`emailsender`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account, contact, queue, systemuser|

### <a name="BKMK_EmailSenderObjectTypeCode"></a> EmailSenderObjectTypeCode

|Property|Value|
|---|---|
|Description|**Shows the object type of sender of the email.**|
|DisplayName|**Email Sender Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`emailsenderobjecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|---|---|
|Description|**Shows the conversion rate of the record's currency. The exchange rate is used to convert all money fields in the record from the local currency to the system's default currency.**|
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

### <a name="BKMK_InReplyTo"></a> InReplyTo

|Property|Value|
|---|---|
|Description|**Type the ID of the email message that this email activity is a response to.**|
|DisplayName|**In Reply To Message**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`inreplyto`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|320|

### <a name="BKMK_IsEmailFollowed"></a> IsEmailFollowed

|Property|Value|
|---|---|
|Description|**For internal use only. Shows whether this email is followed. This is evaluated state which overrides user selection of follow email.**|
|DisplayName|**Followed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isemailfollowed`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`activitypointer_isemailfollowed`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsEmailReminderSet"></a> IsEmailReminderSet

|Property|Value|
|---|---|
|Description|**For internal use only. Shows whether this email Reminder is Set.**|
|DisplayName|**Reminder Set**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isemailreminderset`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`email_isemailreminderset`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsRegularActivity"></a> IsRegularActivity

|Property|Value|
|---|---|
|Description|**Information regarding whether the activity is a regular activity type or event type.**|
|DisplayName|**Is Regular Activity**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isregularactivity`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`activitypointer_isregularactivity`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsSafeDescriptionTruncated"></a> IsSafeDescriptionTruncated

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**IsSafeDescriptionTruncated**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`issafedescriptiontruncated`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_IsUnsafe"></a> IsUnsafe

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**IsUnsafe**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isunsafe`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

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

### <a name="BKMK_OnHoldTime"></a> OnHoldTime

|Property|Value|
|---|---|
|Description|**Shows how long, in minutes, that the record was on hold.**|
|DisplayName|**On Hold Time (Minutes)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`onholdtime`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

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
|Description|**Unique identifier of the business unit that owns the email activity.**|
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
|Description|**Unique identifier of the team who owns the email activity.**|
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
|Description|**Unique identifier of the user who owns the email activity.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ParentSensitivityLabelId"></a> ParentSensitivityLabelId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Parent Sensitivity Label Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parentsensitivitylabelid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_PostponeEmailProcessingUntil"></a> PostponeEmailProcessingUntil

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Delay email processing until**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`postponeemailprocessinguntil`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ReplyCount"></a> ReplyCount

|Property|Value|
|---|---|
|Description|**Shows the number of replies received for an email.**|
|DisplayName|**Reply Count**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`replycount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_SafeDescription"></a> SafeDescription

|Property|Value|
|---|---|
|Description|**Safe body text of the e-mail.**|
|DisplayName|**Safe Description**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`safedescription`|
|RequiredLevel|None|
|Type|Memo|
|Format|Email|
|FormatName|Email|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_ScheduledDurationMinutes"></a> ScheduledDurationMinutes

|Property|Value|
|---|---|
|Description|**Scheduled duration of the email activity, specified in minutes.**|
|DisplayName|**Scheduled Duration**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`scheduleddurationminutes`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_SenderMailboxId"></a> SenderMailboxId

|Property|Value|
|---|---|
|Description|**Select the mailbox associated with the sender of the email message.**|
|DisplayName|**Sender's Mailbox**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sendermailboxid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mailbox|

### <a name="BKMK_SendersAccount"></a> SendersAccount

|Property|Value|
|---|---|
|Description|**Shows the parent account of the sender of the email.**|
|DisplayName|**Senders Account**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sendersaccount`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account|

### <a name="BKMK_SendersAccountObjectTypeCode"></a> SendersAccountObjectTypeCode

|Property|Value|
|---|---|
|Description|**Shows the parent account type code of the sender of the email.**|
|DisplayName|**SendersAccount Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sendersaccountobjecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_SentOn"></a> SentOn

|Property|Value|
|---|---|
|Description|**Shows the date and time that the email was sent.**|
|DisplayName|**Date Sent**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`senton`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_SLAInvokedId"></a> SLAInvokedId

|Property|Value|
|---|---|
|Description|**Last SLA that was applied to this email. This field is for internal use only.**|
|DisplayName|**Last SLA applied**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`slainvokedid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|sla|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the email message.**|
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

- [Account_Email_EmailSender](#BKMK_Account_Email_EmailSender)
- [Account_Email_SendersAccount](#BKMK_Account_Email_SendersAccount)
- [Account_Emails](#BKMK_Account_Emails)
- [activity_pointer_email](#BKMK_activity_pointer_email)
- [adx_invitation_Emails](#BKMK_adx_invitation_Emails)
- [AsyncOperation_Emails](#BKMK_AsyncOperation_Emails)
- [business_unit_email_activities](#BKMK_business_unit_email_activities)
- [Contact_Email_EmailSender](#BKMK_Contact_Email_EmailSender)
- [Contact_Emails](#BKMK_Contact_Emails)
- [email_acceptingentity_queue](#BKMK_email_acceptingentity_queue)
- [email_acceptingentity_systemuser](#BKMK_email_acceptingentity_systemuser)
- [email_email_CorrelatedActivityId](#BKMK_email_email_CorrelatedActivityId-many-to-one)
- [email_email_parentactivityid](#BKMK_email_email_parentactivityid-many-to-one)
- [Email_EmailTemplate](#BKMK_Email_EmailTemplate)
- [email_sendermailboxid_mailbox](#BKMK_email_sendermailboxid_mailbox)
- [FileAttachment_Email_DescriptionBlobId](#BKMK_FileAttachment_Email_DescriptionBlobId)
- [KnowledgeArticle_Emails](#BKMK_KnowledgeArticle_Emails)
- [KnowledgeBaseRecord_Emails](#BKMK_KnowledgeBaseRecord_Emails)
- [lk_email_createdby](#BKMK_lk_email_createdby)
- [lk_email_createdonbehalfby](#BKMK_lk_email_createdonbehalfby)
- [lk_email_modifiedby](#BKMK_lk_email_modifiedby)
- [lk_email_modifiedonbehalfby](#BKMK_lk_email_modifiedonbehalfby)
- [mailbox_email_ReceivingMailboxId](#BKMK_mailbox_email_ReceivingMailboxId)
- [manualsla_email](#BKMK_manualsla_email)
- [mspp_adplacement_Emails](#BKMK_mspp_adplacement_Emails)
- [mspp_pollplacement_Emails](#BKMK_mspp_pollplacement_Emails)
- [mspp_publishingstatetransitionrule_Emails](#BKMK_mspp_publishingstatetransitionrule_Emails)
- [mspp_redirect_Emails](#BKMK_mspp_redirect_Emails)
- [mspp_shortcut_Emails](#BKMK_mspp_shortcut_Emails)
- [mspp_website_Emails](#BKMK_mspp_website_Emails)
- [owner_emails](#BKMK_owner_emails)
- [processstage_emails](#BKMK_processstage_emails)
- [Queue_Email_EmailSender](#BKMK_Queue_Email_EmailSender)
- [sensitivitylabel_email_SensitivityLabelId](#BKMK_sensitivitylabel_email_SensitivityLabelId)
- [sla_email](#BKMK_sla_email)
- [SystemUser_Email_EmailSender](#BKMK_SystemUser_Email_EmailSender)
- [team_email](#BKMK_team_email)
- [TransactionCurrency_Email](#BKMK_TransactionCurrency_Email)
- [user_email](#BKMK_user_email)

### <a name="BKMK_Account_Email_EmailSender"></a> Account_Email_EmailSender

One-To-Many Relationship: [account Account_Email_EmailSender](account.md#BKMK_Account_Email_EmailSender)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`emailsender`|
|ReferencingEntityNavigationPropertyName|`emailsender_account`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Account_Email_SendersAccount"></a> Account_Email_SendersAccount

One-To-Many Relationship: [account Account_Email_SendersAccount](account.md#BKMK_Account_Email_SendersAccount)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`sendersaccount`|
|ReferencingEntityNavigationPropertyName|`sendersaccount`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Account_Emails"></a> Account_Emails

One-To-Many Relationship: [account Account_Emails](account.md#BKMK_Account_Emails)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_account_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_activity_pointer_email"></a> activity_pointer_email

One-To-Many Relationship: [activitypointer activity_pointer_email](activitypointer.md#BKMK_activity_pointer_email)

|Property|Value|
|---|---|
|ReferencedEntity|`activitypointer`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`activityid`|
|ReferencingEntityNavigationPropertyName|`activityid_activitypointer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_invitation_Emails"></a> adx_invitation_Emails

One-To-Many Relationship: [adx_invitation adx_invitation_Emails](adx_invitation.md#BKMK_adx_invitation_Emails)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_invitation`|
|ReferencedAttribute|`adx_invitationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_invitation_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_AsyncOperation_Emails"></a> AsyncOperation_Emails

One-To-Many Relationship: [asyncoperation AsyncOperation_Emails](asyncoperation.md#BKMK_AsyncOperation_Emails)

|Property|Value|
|---|---|
|ReferencedEntity|`asyncoperation`|
|ReferencedAttribute|`asyncoperationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_asyncoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_business_unit_email_activities"></a> business_unit_email_activities

One-To-Many Relationship: [businessunit business_unit_email_activities](businessunit.md#BKMK_business_unit_email_activities)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Contact_Email_EmailSender"></a> Contact_Email_EmailSender

One-To-Many Relationship: [contact Contact_Email_EmailSender](contact.md#BKMK_Contact_Email_EmailSender)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`emailsender`|
|ReferencingEntityNavigationPropertyName|`emailsender_contact`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Contact_Emails"></a> Contact_Emails

One-To-Many Relationship: [contact Contact_Emails](contact.md#BKMK_Contact_Emails)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_contact_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_email_acceptingentity_queue"></a> email_acceptingentity_queue

One-To-Many Relationship: [queue email_acceptingentity_queue](queue.md#BKMK_email_acceptingentity_queue)

|Property|Value|
|---|---|
|ReferencedEntity|`queue`|
|ReferencedAttribute|`queueid`|
|ReferencingAttribute|`acceptingentityid`|
|ReferencingEntityNavigationPropertyName|`acceptingentityid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_email_acceptingentity_systemuser"></a> email_acceptingentity_systemuser

One-To-Many Relationship: [systemuser email_acceptingentity_systemuser](systemuser.md#BKMK_email_acceptingentity_systemuser)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`acceptingentityid`|
|ReferencingEntityNavigationPropertyName|`acceptingentityid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_email_email_CorrelatedActivityId-many-to-one"></a> email_email_CorrelatedActivityId

One-To-Many Relationship: [email email_email_CorrelatedActivityId](#BKMK_email_email_CorrelatedActivityId-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`email`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`correlatedactivityid`|
|ReferencingEntityNavigationPropertyName|`CorrelatedActivityId_Email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_email_email_parentactivityid-many-to-one"></a> email_email_parentactivityid

One-To-Many Relationship: [email email_email_parentactivityid](#BKMK_email_email_parentactivityid-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`email`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`parentactivityid`|
|ReferencingEntityNavigationPropertyName|`parentactivityid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Email_EmailTemplate"></a> Email_EmailTemplate

One-To-Many Relationship: [template Email_EmailTemplate](template.md#BKMK_Email_EmailTemplate)

|Property|Value|
|---|---|
|ReferencedEntity|`template`|
|ReferencedAttribute|`templateid`|
|ReferencingAttribute|`templateid`|
|ReferencingEntityNavigationPropertyName|`templateid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_email_sendermailboxid_mailbox"></a> email_sendermailboxid_mailbox

One-To-Many Relationship: [mailbox email_sendermailboxid_mailbox](mailbox.md#BKMK_email_sendermailboxid_mailbox)

|Property|Value|
|---|---|
|ReferencedEntity|`mailbox`|
|ReferencedAttribute|`mailboxid`|
|ReferencingAttribute|`sendermailboxid`|
|ReferencingEntityNavigationPropertyName|`sendermailboxid_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_Email_DescriptionBlobId"></a> FileAttachment_Email_DescriptionBlobId

One-To-Many Relationship: [fileattachment FileAttachment_Email_DescriptionBlobId](fileattachment.md#BKMK_FileAttachment_Email_DescriptionBlobId)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`descriptionblobid`|
|ReferencingEntityNavigationPropertyName|`descriptionblobid_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KnowledgeArticle_Emails"></a> KnowledgeArticle_Emails

One-To-Many Relationship: [knowledgearticle KnowledgeArticle_Emails](knowledgearticle.md#BKMK_KnowledgeArticle_Emails)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgearticle_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_KnowledgeBaseRecord_Emails"></a> KnowledgeBaseRecord_Emails

One-To-Many Relationship: [knowledgebaserecord KnowledgeBaseRecord_Emails](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_Emails)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgebaserecord`|
|ReferencedAttribute|`knowledgebaserecordid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgebaserecord_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_email_createdby"></a> lk_email_createdby

One-To-Many Relationship: [systemuser lk_email_createdby](systemuser.md#BKMK_lk_email_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_email_createdonbehalfby"></a> lk_email_createdonbehalfby

One-To-Many Relationship: [systemuser lk_email_createdonbehalfby](systemuser.md#BKMK_lk_email_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_email_modifiedby"></a> lk_email_modifiedby

One-To-Many Relationship: [systemuser lk_email_modifiedby](systemuser.md#BKMK_lk_email_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_email_modifiedonbehalfby"></a> lk_email_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_email_modifiedonbehalfby](systemuser.md#BKMK_lk_email_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mailbox_email_ReceivingMailboxId"></a> mailbox_email_ReceivingMailboxId

One-To-Many Relationship: [mailbox mailbox_email_ReceivingMailboxId](mailbox.md#BKMK_mailbox_email_ReceivingMailboxId)

|Property|Value|
|---|---|
|ReferencedEntity|`mailbox`|
|ReferencedAttribute|`mailboxid`|
|ReferencingAttribute|`receivingmailboxid`|
|ReferencingEntityNavigationPropertyName|`ReceivingMailboxId_Email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_manualsla_email"></a> manualsla_email

One-To-Many Relationship: [sla manualsla_email](sla.md#BKMK_manualsla_email)

|Property|Value|
|---|---|
|ReferencedEntity|`sla`|
|ReferencedAttribute|`slaid`|
|ReferencingAttribute|`slaid`|
|ReferencingEntityNavigationPropertyName|`sla_email_sla`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_adplacement_Emails"></a> mspp_adplacement_Emails

One-To-Many Relationship: [mspp_adplacement mspp_adplacement_Emails](mspp_adplacement.md#BKMK_mspp_adplacement_Emails)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_adplacement`|
|ReferencedAttribute|`mspp_adplacementid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_adplacement_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_pollplacement_Emails"></a> mspp_pollplacement_Emails

One-To-Many Relationship: [mspp_pollplacement mspp_pollplacement_Emails](mspp_pollplacement.md#BKMK_mspp_pollplacement_Emails)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_pollplacement`|
|ReferencedAttribute|`mspp_pollplacementid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_pollplacement_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_publishingstatetransitionrule_Emails"></a> mspp_publishingstatetransitionrule_Emails

One-To-Many Relationship: [mspp_publishingstatetransitionrule mspp_publishingstatetransitionrule_Emails](mspp_publishingstatetransitionrule.md#BKMK_mspp_publishingstatetransitionrule_Emails)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_publishingstatetransitionrule`|
|ReferencedAttribute|`mspp_publishingstatetransitionruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_publishingstatetransitionrule_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_redirect_Emails"></a> mspp_redirect_Emails

One-To-Many Relationship: [mspp_redirect mspp_redirect_Emails](mspp_redirect.md#BKMK_mspp_redirect_Emails)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_redirect`|
|ReferencedAttribute|`mspp_redirectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_redirect_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_shortcut_Emails"></a> mspp_shortcut_Emails

One-To-Many Relationship: [mspp_shortcut mspp_shortcut_Emails](mspp_shortcut.md#BKMK_mspp_shortcut_Emails)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_shortcut`|
|ReferencedAttribute|`mspp_shortcutid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_shortcut_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_website_Emails"></a> mspp_website_Emails

One-To-Many Relationship: [mspp_website mspp_website_Emails](mspp_website.md#BKMK_mspp_website_Emails)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_website`|
|ReferencedAttribute|`mspp_websiteid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_website_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_emails"></a> owner_emails

One-To-Many Relationship: [owner owner_emails](owner.md#BKMK_owner_emails)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_processstage_emails"></a> processstage_emails

One-To-Many Relationship: [processstage processstage_emails](processstage.md#BKMK_processstage_emails)

|Property|Value|
|---|---|
|ReferencedEntity|`processstage`|
|ReferencedAttribute|`processstageid`|
|ReferencingAttribute|`stageid`|
|ReferencingEntityNavigationPropertyName|`stageid_processstage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Queue_Email_EmailSender"></a> Queue_Email_EmailSender

One-To-Many Relationship: [queue Queue_Email_EmailSender](queue.md#BKMK_Queue_Email_EmailSender)

|Property|Value|
|---|---|
|ReferencedEntity|`queue`|
|ReferencedAttribute|`queueid`|
|ReferencingAttribute|`emailsender`|
|ReferencingEntityNavigationPropertyName|`emailsender_queue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sensitivitylabel_email_SensitivityLabelId"></a> sensitivitylabel_email_SensitivityLabelId

One-To-Many Relationship: [sensitivitylabel sensitivitylabel_email_SensitivityLabelId](sensitivitylabel.md#BKMK_sensitivitylabel_email_SensitivityLabelId)

|Property|Value|
|---|---|
|ReferencedEntity|`sensitivitylabel`|
|ReferencedAttribute|`sensitivitylabelid`|
|ReferencingAttribute|`sensitivitylabelid`|
|ReferencingEntityNavigationPropertyName|`SensitivityLabelId_Email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sla_email"></a> sla_email

One-To-Many Relationship: [sla sla_email](sla.md#BKMK_sla_email)

|Property|Value|
|---|---|
|ReferencedEntity|`sla`|
|ReferencedAttribute|`slaid`|
|ReferencingAttribute|`slainvokedid`|
|ReferencingEntityNavigationPropertyName|`slainvokedid_email_sla`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SystemUser_Email_EmailSender"></a> SystemUser_Email_EmailSender

One-To-Many Relationship: [systemuser SystemUser_Email_EmailSender](systemuser.md#BKMK_SystemUser_Email_EmailSender)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`emailsender`|
|ReferencingEntityNavigationPropertyName|`emailsender_systemuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_email"></a> team_email

One-To-Many Relationship: [team team_email](team.md#BKMK_team_email)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_Email"></a> TransactionCurrency_Email

One-To-Many Relationship: [transactioncurrency TransactionCurrency_Email](transactioncurrency.md#BKMK_TransactionCurrency_Email)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencingEntityNavigationPropertyName|`transactioncurrencyid_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_email"></a> user_email

One-To-Many Relationship: [systemuser user_email](systemuser.md#BKMK_user_email)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [email_actioncard](#BKMK_email_actioncard)
- [email_activity_mime_attachment](#BKMK_email_activity_mime_attachment)
- [email_activity_parties](#BKMK_email_activity_parties)
- [Email_Annotation](#BKMK_Email_Annotation)
- [Email_AsyncOperations](#BKMK_Email_AsyncOperations)
- [Email_BulkDeleteFailures](#BKMK_Email_BulkDeleteFailures)
- [email_connections1](#BKMK_email_connections1)
- [email_connections2](#BKMK_email_connections2)
- [Email_DuplicateBaseRecord](#BKMK_Email_DuplicateBaseRecord)
- [Email_DuplicateMatchingRecord](#BKMK_Email_DuplicateMatchingRecord)
- [email_email_CorrelatedActivityId](#BKMK_email_email_CorrelatedActivityId-one-to-many)
- [email_email_parentactivityid](#BKMK_email_email_parentactivityid-one-to-many)
- [email_FileAttachments](#BKMK_email_FileAttachments)
- [email_principalobjectattributeaccess](#BKMK_email_principalobjectattributeaccess)
- [Email_ProcessSessions](#BKMK_Email_ProcessSessions)
- [Email_QueueItem](#BKMK_Email_QueueItem)
- [Email_SyncErrors](#BKMK_Email_SyncErrors)
- [slakpiinstance_email](#BKMK_slakpiinstance_email)

### <a name="BKMK_email_actioncard"></a> email_actioncard

Many-To-One Relationship: [actioncard email_actioncard](actioncard.md#BKMK_email_actioncard)

|Property|Value|
|---|---|
|ReferencingEntity|`actioncard`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`email_actioncard`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_email_activity_mime_attachment"></a> email_activity_mime_attachment

Many-To-One Relationship: [activitymimeattachment email_activity_mime_attachment](activitymimeattachment.md#BKMK_email_activity_mime_attachment)

|Property|Value|
|---|---|
|ReferencingEntity|`activitymimeattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`email_activity_mime_attachment`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_email_activity_parties"></a> email_activity_parties

Many-To-One Relationship: [activityparty email_activity_parties](activityparty.md#BKMK_email_activity_parties)

|Property|Value|
|---|---|
|ReferencingEntity|`activityparty`|
|ReferencingAttribute|`activityid`|
|ReferencedEntityNavigationPropertyName|`email_activity_parties`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Email_Annotation"></a> Email_Annotation

Many-To-One Relationship: [annotation Email_Annotation](annotation.md#BKMK_Email_Annotation)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`Email_Annotation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Email_AsyncOperations"></a> Email_AsyncOperations

Many-To-One Relationship: [asyncoperation Email_AsyncOperations](asyncoperation.md#BKMK_Email_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Email_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Email_BulkDeleteFailures"></a> Email_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure Email_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Email_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Email_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_email_connections1"></a> email_connections1

Many-To-One Relationship: [connection email_connections1](connection.md#BKMK_email_connections1)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record1id`|
|ReferencedEntityNavigationPropertyName|`email_connections1`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_email_connections2"></a> email_connections2

Many-To-One Relationship: [connection email_connections2](connection.md#BKMK_email_connections2)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record2id`|
|ReferencedEntityNavigationPropertyName|`email_connections2`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Email_DuplicateBaseRecord"></a> Email_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord Email_DuplicateBaseRecord](duplicaterecord.md#BKMK_Email_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`Email_DuplicateBaseRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Email_DuplicateMatchingRecord"></a> Email_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord Email_DuplicateMatchingRecord](duplicaterecord.md#BKMK_Email_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`Email_DuplicateMatchingRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_email_email_CorrelatedActivityId-one-to-many"></a> email_email_CorrelatedActivityId

Many-To-One Relationship: [email email_email_CorrelatedActivityId](#BKMK_email_email_CorrelatedActivityId-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`correlatedactivityid`|
|ReferencedEntityNavigationPropertyName|`email_email_CorrelatedActivityId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_email_email_parentactivityid-one-to-many"></a> email_email_parentactivityid

Many-To-One Relationship: [email email_email_parentactivityid](#BKMK_email_email_parentactivityid-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`parentactivityid`|
|ReferencedEntityNavigationPropertyName|`email_email_parentactivityid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_email_FileAttachments"></a> email_FileAttachments

Many-To-One Relationship: [fileattachment email_FileAttachments](fileattachment.md#BKMK_email_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`email_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_email_principalobjectattributeaccess"></a> email_principalobjectattributeaccess

Many-To-One Relationship: [principalobjectattributeaccess email_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_email_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`email_principalobjectattributeaccess`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Email_ProcessSessions"></a> Email_ProcessSessions

Many-To-One Relationship: [processsession Email_ProcessSessions](processsession.md#BKMK_Email_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Email_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Email_QueueItem"></a> Email_QueueItem

Many-To-One Relationship: [queueitem Email_QueueItem](queueitem.md#BKMK_Email_QueueItem)

|Property|Value|
|---|---|
|ReferencingEntity|`queueitem`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`Email_QueueItem`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Email_SyncErrors"></a> Email_SyncErrors

Many-To-One Relationship: [syncerror Email_SyncErrors](syncerror.md#BKMK_Email_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Email_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_slakpiinstance_email"></a> slakpiinstance_email

Many-To-One Relationship: [slakpiinstance slakpiinstance_email](slakpiinstance.md#BKMK_slakpiinstance_email)

|Property|Value|
|---|---|
|ReferencingEntity|`slakpiinstance`|
|ReferencingAttribute|`regarding`|
|ReferencedEntityNavigationPropertyName|`slakpiinstance_email`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.email?displayProperty=fullName>
