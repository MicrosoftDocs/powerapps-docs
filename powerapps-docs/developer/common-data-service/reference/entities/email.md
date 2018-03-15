---
title: "Email Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the Email entity."

services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
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
# Email Entity Reference

Activity that is delivered using email protocols.

## Entity Properties

**DisplayName**: Email<br />
**DisplayCollectionName**: Email Messages<br />
**SchemaName**: Email<br />
**CollectionSchemaName**: Emails<br />
**LogicalName**: email<br />
**LogicalCollectionName**: emails<br />
**EntitySetName**: emails<br />
**PrimaryIdAttribute**: activityid<br />
**PrimaryNameAttribute**: subject<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [ReminderActionCardId](#BKMK_ReminderActionCardId)
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


### <a name="BKMK_ActivityAdditionalParams"></a> ActivityAdditionalParams

**Description**: For internal use only.<br />
**DisplayName**: Additional Parameters<br />
**LogicalName**: activityadditionalparams<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 8192


### <a name="BKMK_ActivityId"></a> ActivityId

**Description**: Unique identifier of the email activity.<br />
**DisplayName**: Email Message<br />
**LogicalName**: activityid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ActualDurationMinutes"></a> ActualDurationMinutes

**Description**: Type the number of minutes spent creating and sending the email. The duration is used in reporting.<br />
**DisplayName**: Duration<br />
**LogicalName**: actualdurationminutes<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: Duration<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_ActualEnd"></a> ActualEnd

**Description**: Enter the actual end date and time of the email. By default, it displays the date and time when the activity was completed or canceled, but can be edited to capture the actual time to create and send the email.<br />
**DisplayName**: Actual End<br />
**LogicalName**: actualend<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_ActualStart"></a> ActualStart

**Description**: Enter the actual start date and time for the email. By default, it displays the date and time when the activity was created, but can be edited to capture the actual time to create and send the email.<br />
**DisplayName**: Actual Start<br />
**LogicalName**: actualstart<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_AttachmentOpenCount"></a> AttachmentOpenCount

**Description**: Shows the number of times an email attachment has been viewed.<br />
**DisplayName**: Attachment Open Count<br />
**LogicalName**: attachmentopencount<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_BaseConversationIndexHash"></a> BaseConversationIndexHash

**Description**: Hash of base of conversation index.<br />
**DisplayName**: Conversation Index (Hash)<br />
**LogicalName**: baseconversationindexhash<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_bcc"></a> bcc

**Description**: Enter the recipients that are included on the email distribution, but are not displayed to other recipients.<br />
**DisplayName**: Bcc<br />
**LogicalName**: bcc<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: PartyList<br />
**Targets**: account,contact,knowledgearticle,queue,systemuser,unresolvedaddress


### <a name="BKMK_Category"></a> Category

**Description**: Type a category to identify the email type, such as lead outreach, customer follow-up, or service alert, to tie the email to a business group or function.<br />
**DisplayName**: Category<br />
**LogicalName**: category<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 250


### <a name="BKMK_cc"></a> cc

**Description**: Enter the recipients that should be copied on the email.<br />
**DisplayName**: Cc<br />
**LogicalName**: cc<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: PartyList<br />
**Targets**: account,contact,knowledgearticle,queue,systemuser,unresolvedaddress


### <a name="BKMK_ConversationTrackingId"></a> ConversationTrackingId

**Description**: Conversation Tracking Id.<br />
**DisplayName**: Conversation Tracking Id<br />
**LogicalName**: conversationtrackingid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_DelayedEmailSendTime"></a> DelayedEmailSendTime

**Description**: Enter the expected date and time when email will be sent.<br />
**DisplayName**: Send Later<br />
**LogicalName**: delayedemailsendtime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_DeliveryAttempts"></a> DeliveryAttempts

**Description**: Shows the count of the number of attempts made to send the email. The count is used as an indicator of email routing issues.<br />
**DisplayName**: No. of Delivery Attempts<br />
**LogicalName**: deliveryattempts<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0


### <a name="BKMK_DeliveryPriorityCode"></a> DeliveryPriorityCode

**Description**: Select the priority of delivery of the email to the email server.<br />
**DisplayName**: Delivery Priority<br />
**LogicalName**: deliveryprioritycode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Low
- **Value**: 1 **Label**: Normal
- **Value**: 2 **Label**: High



### <a name="BKMK_DeliveryReceiptRequested"></a> DeliveryReceiptRequested

**Description**: Select whether the sender should receive confirmation that the email was delivered.<br />
**DisplayName**: Delivery Receipt Requested<br />
**LogicalName**: deliveryreceiptrequested<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_Description"></a> Description

**Description**: Type the greeting and message text of the email.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: Email<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_DirectionCode"></a> DirectionCode

**Description**: Select the direction of the email as incoming or outbound.<br />
**DisplayName**: Direction<br />
**LogicalName**: directioncode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Outgoing
- **FalseOption Value**: 0 **Label**: Incoming

**DefaultValue**: True


### <a name="BKMK_EmailReminderExpiryTime"></a> EmailReminderExpiryTime

**Description**: Shows the date and time when an email reminder expires.<br />
**DisplayName**: Email Reminder Expiry Time<br />
**LogicalName**: emailreminderexpirytime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_EmailReminderText"></a> EmailReminderText

**Description**: For internal use only.<br />
**DisplayName**: Email Reminder Text<br />
**LogicalName**: emailremindertext<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1250


### <a name="BKMK_EmailReminderType"></a> EmailReminderType

**Description**: Shows the type of the email reminder.<br />
**DisplayName**: Email Reminder Type<br />
**LogicalName**: emailremindertype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: If I do not receive a reply by
- **Value**: 1 **Label**: If the email is not opened by
- **Value**: 2 **Label**: Remind me anyways at



### <a name="BKMK_EmailSenderName"></a> EmailSenderName

**Description**: Shows the name of the sender of the email.<br />
**DisplayName**: Email Sender Name<br />
**LogicalName**: emailsendername<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 400


### <a name="BKMK_EmailTrackingId"></a> EmailTrackingId

**Description**: Email Tracking Id.<br />
**DisplayName**: Email Tracking Id<br />
**LogicalName**: emailtrackingid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_FollowEmailUserPreference"></a> FollowEmailUserPreference

**Description**: Select whether the email allows following recipient activities sent from Microsoft Dynamics 365.This is user preference state which can be overridden by system evaluated state.<br />
**DisplayName**: Following<br />
**LogicalName**: followemailuserpreference<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: True
- **FalseOption Value**: 0 **Label**: False

**DefaultValue**: False


### <a name="BKMK_from"></a> from

**Description**: Enter the sender of the email.<br />
**DisplayName**: From<br />
**LogicalName**: from<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: PartyList<br />
**Targets**: queue,systemuser


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


### <a name="BKMK_IsBilled"></a> IsBilled

**Description**: Information regarding whether the email activity was billed as part of resolving a case.<br />
**DisplayName**: Is Billed<br />
**LogicalName**: isbilled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsWorkflowCreated"></a> IsWorkflowCreated

**Description**: Indication if the email was created by a workflow rule.<br />
**DisplayName**: Is Workflow Created<br />
**LogicalName**: isworkflowcreated<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_LastOnHoldTime"></a> LastOnHoldTime

**Description**: Contains the date and time stamp of the last on hold time.<br />
**DisplayName**: Last On Hold Time<br />
**LogicalName**: lastonholdtime<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_LastOpenedTime"></a> LastOpenedTime

**Description**: Shows the latest date and time when email was opened.<br />
**DisplayName**: Last Opened Time<br />
**LogicalName**: lastopenedtime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_LinksClickedCount"></a> LinksClickedCount

**Description**: Shows the number of times a link in an email has been clicked.<br />
**DisplayName**: Links Clicked Count<br />
**LogicalName**: linksclickedcount<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_MessageId"></a> MessageId

**Description**: Unique identifier of the email message. Used only for email that is received.<br />
**DisplayName**: Message ID<br />
**LogicalName**: messageid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 320


### <a name="BKMK_MessageIdDupCheck"></a> MessageIdDupCheck

**Description**: For internal use only.<br />
**DisplayName**: Message ID Dup Check<br />
**LogicalName**: messageiddupcheck<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_MimeType"></a> MimeType

**Description**: MIME type of the email message data.<br />
**DisplayName**: Mime Type<br />
**LogicalName**: mimetype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_Notifications"></a> Notifications

**Description**: Select the notification code to identify issues with the email recipients or attachments, such as blocked attachments.<br />
**DisplayName**: Notifications<br />
**LogicalName**: notifications<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: None
- **Value**: 1 **Label**: The message was saved as a Microsoft Dynamics 365 email record, but not all the attachments could be saved with it. An attachment cannot be saved if it is blocked or if its file type is invalid.
- **Value**: 2 **Label**: Truncated body.



### <a name="BKMK_OpenCount"></a> OpenCount

**Description**: Shows the number of times an email has been opened.<br />
**DisplayName**: Open Count<br />
**LogicalName**: opencount<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


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

**Description**: Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.<br />
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


### <a name="BKMK_ParentActivityId"></a> ParentActivityId

**Description**: Select the activity that the email is associated with.<br />
**DisplayName**: Parent Activity Id<br />
**LogicalName**: parentactivityid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: email


### <a name="BKMK_PriorityCode"></a> PriorityCode

**Description**: Select the priority so that preferred customers or critical issues are handled quickly.<br />
**DisplayName**: Priority<br />
**LogicalName**: prioritycode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Low
- **Value**: 1 **Label**: Normal
- **Value**: 2 **Label**: High



### <a name="BKMK_ProcessId"></a> ProcessId

**Description**: Shows the ID of the process.<br />
**DisplayName**: Process<br />
**LogicalName**: processid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ReadReceiptRequested"></a> ReadReceiptRequested

**Description**: Indicates that a read receipt is requested.<br />
**DisplayName**: Read Receipt Requested<br />
**LogicalName**: readreceiptrequested<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

**Description**: Choose the record that the email relates to.<br />
**DisplayName**: Regarding<br />
**LogicalName**: regardingobjectid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: account,asyncoperation,contact,knowledgearticle,knowledgebaserecord


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_ReminderActionCardId"></a> ReminderActionCardId

**Description**: Reminder Action Card Id.<br />
**DisplayName**: Reminder Action Card Id.<br />
**LogicalName**: reminderactioncardid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ScheduledEnd"></a> ScheduledEnd

**Description**: Enter the expected due date and time for the activity to be completed to provide details about when the email will be sent.<br />
**DisplayName**: Due Date<br />
**LogicalName**: scheduledend<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ScheduledStart"></a> ScheduledStart

**Description**: Enter the expected start date and time for the activity to provide details about the tentative time when the email activity must be initiated.<br />
**DisplayName**: Start Date<br />
**LogicalName**: scheduledstart<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_Sender"></a> Sender

**Description**: Sender of the email.<br />
**DisplayName**: From<br />
**LogicalName**: sender<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 250


### <a name="BKMK_SendersAccountName"></a> SendersAccountName

**Description**: Shows the name of the sender account of the email.<br />
**DisplayName**: Email Sender Account Name<br />
**LogicalName**: sendersaccountname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 400


### <a name="BKMK_SLAId"></a> SLAId

**Description**: Choose the service level agreement (SLA) that you want to apply to the email record.<br />
**DisplayName**: SLA<br />
**LogicalName**: slaid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: sla


### <a name="BKMK_SortDate"></a> SortDate

**Description**: Shows the date and time by which the activities are sorted.<br />
**DisplayName**: Sort Date<br />
**LogicalName**: sortdate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_StageId"></a> StageId

**Description**: Shows the ID of the stage.<br />
**DisplayName**: Process Stage<br />
**LogicalName**: stageid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_StateCode"></a> StateCode

**Description**: Shows whether the email is open, completed, or canceled. Completed and canceled email is read-only and can't be edited.<br />
**DisplayName**: Activity Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Open **DefaultStatus**: 1 **InvariantName**: Open
- **Value**: 1 **Label**: Completed **DefaultStatus**: 2 **InvariantName**: Completed
- **Value**: 2 **Label**: Canceled **DefaultStatus**: 5 **InvariantName**: Canceled



### <a name="BKMK_StatusCode"></a> StatusCode

**Added by**: Activities Solution<br />
**Description**: Select the email's status.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Status<br />
**Options**:

- **Value**: 1 **Label**: Draft **State**: 0
- **Value**: 2 **Label**: Completed **State**: 1
- **Value**: 3 **Label**: Sent **State**: 1
- **Value**: 4 **Label**: Received **State**: 1
- **Value**: 5 **Label**: Canceled **State**: 2
- **Value**: 6 **Label**: Pending Send **State**: 1
- **Value**: 7 **Label**: Sending **State**: 1
- **Value**: 8 **Label**: Failed **State**: 0



### <a name="BKMK_Subcategory"></a> Subcategory

**Description**: Type a subcategory to identify the email type and relate the activity to a specific product, sales region, business group, or other function.<br />
**DisplayName**: Sub-Category<br />
**LogicalName**: subcategory<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 250


### <a name="BKMK_Subject"></a> Subject

**Description**: Type a short description about the objective or primary topic of the email.<br />
**DisplayName**: Subject<br />
**LogicalName**: subject<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_SubmittedBy"></a> SubmittedBy

**Description**: Shows the Microsoft Office Outlook account for the user who submitted the email to Microsoft Dynamics 365.<br />
**DisplayName**: Submitted By<br />
**LogicalName**: submittedby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 250


### <a name="BKMK_TemplateId"></a> TemplateId

**Description**: For internal use only. ID for template used in email.<br />
**DisplayName**: ID for template used.<br />
**LogicalName**: templateid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: template


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


### <a name="BKMK_to"></a> to

**Description**: Enter the account, contact, lead, queue, or user recipients for the email.<br />
**DisplayName**: To<br />
**LogicalName**: to<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: PartyList<br />
**Targets**: account,contact,knowledgearticle,queue,systemuser,unresolvedaddress


### <a name="BKMK_ToRecipients"></a> ToRecipients

**Description**: Shows the email addresses corresponding to the recipients.<br />
**DisplayName**: To Recipients<br />
**LogicalName**: torecipients<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 500


### <a name="BKMK_TrackingToken"></a> TrackingToken

**Description**: Shows the tracking token assigned to the email to make sure responses are automatically tracked in Microsoft Dynamics 365.<br />
**DisplayName**: Tracking Token<br />
**LogicalName**: trackingtoken<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

**Description**: Choose the local currency for the record to make sure budgets are reported in the correct currency.<br />
**DisplayName**: Currency<br />
**LogicalName**: transactioncurrencyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: transactioncurrency


### <a name="BKMK_TraversedPath"></a> TraversedPath

**Description**: For internal use only.<br />
**DisplayName**: Traversed Path<br />
**LogicalName**: traversedpath<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1250


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

- [ActivityTypeCode](#BKMK_ActivityTypeCode)
- [AttachmentCount](#BKMK_AttachmentCount)
- [Compressed](#BKMK_Compressed)
- [ConversationIndex](#BKMK_ConversationIndex)
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

**Description**: Shows the type of activity.<br />
**DisplayName**: Activity Type<br />
**LogicalName**: activitytypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_AttachmentCount"></a> AttachmentCount

**Description**: Shows the umber of attachments of the email message.<br />
**DisplayName**: Attachment Count<br />
**LogicalName**: attachmentcount<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_Compressed"></a> Compressed

**Description**: Indicates if the body is compressed.<br />
**DisplayName**: Compression<br />
**LogicalName**: compressed<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Compressed
- **FalseOption Value**: 0 **Label**: Not compressed

**DefaultValue**: False


### <a name="BKMK_ConversationIndex"></a> ConversationIndex

**Description**: Identifier for all the email responses for this conversation.<br />
**DisplayName**: Conversation Index<br />
**LogicalName**: conversationindex<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2048


### <a name="BKMK_CorrelationMethod"></a> CorrelationMethod

**Description**: Shows how an email is matched to an existing email in Microsoft Dynamics 365. For system use only.<br />
**DisplayName**: Correlation Method<br />
**LogicalName**: correlationmethod<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: None
- **Value**: 1 **Label**: Skipped
- **Value**: 2 **Label**: XHeader
- **Value**: 3 **Label**: InReplyTo
- **Value**: 4 **Label**: TrackingToken
- **Value**: 5 **Label**: ConversationIndex
- **Value**: 6 **Label**: SmartMatching
- **Value**: 7 **Label**: CustomCorrelation



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
**RequiredLevel**: None<br />
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
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_EmailReminderStatus"></a> EmailReminderStatus

**Description**: Shows the status of the email reminder.<br />
**DisplayName**: Email Reminder Status<br />
**LogicalName**: emailreminderstatus<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: NotSet
- **Value**: 1 **Label**: ReminderSet
- **Value**: 2 **Label**: ReminderExpired
- **Value**: 3 **Label**: ReminderInvalid



### <a name="BKMK_EmailSender"></a> EmailSender

**Description**: Shows the sender of the email.<br />
**DisplayName**: Sender<br />
**LogicalName**: emailsender<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: account,contact,queue,systemuser


### <a name="BKMK_EmailSenderObjectTypeCode"></a> EmailSenderObjectTypeCode

**Description**: Shows the object type of sender of the email.<br />
**DisplayName**: Email Sender Type<br />
**LogicalName**: emailsenderobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_EmailSenderYomiName"></a> EmailSenderYomiName

**Description**: Shows the yomi name of the email sender<br />
**DisplayName**: Email Sender yomi Name<br />
**LogicalName**: emailsenderyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 400


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

**Description**: Shows the conversion rate of the record's currency. The exchange rate is used to convert all money fields in the record from the local currency to the system's default currency.<br />
**DisplayName**: Exchange Rate<br />
**LogicalName**: exchangerate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0.0000000001<br />
**Precision**: 10


### <a name="BKMK_InReplyTo"></a> InReplyTo

**Description**: Type the ID of the email message that this email activity is a response to.<br />
**DisplayName**: In Reply To Message<br />
**LogicalName**: inreplyto<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 320


### <a name="BKMK_IsEmailFollowed"></a> IsEmailFollowed

**Description**: For internal use only. Shows whether this email is followed. This is evaluated state which overrides user selection of follow email.<br />
**DisplayName**: Followed<br />
**LogicalName**: isemailfollowed<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsEmailReminderSet"></a> IsEmailReminderSet

**Description**: For internal use only. Shows whether this email Reminder is Set.<br />
**DisplayName**: Reminder Set<br />
**LogicalName**: isemailreminderset<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsRegularActivity"></a> IsRegularActivity

**Description**: Information regarding whether the activity is a regular activity type or event type.<br />
**DisplayName**: Is Regular Activity<br />
**LogicalName**: isregularactivity<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsUnsafe"></a> IsUnsafe

**Description**: For internal use only.<br />
**DisplayName**: IsUnsafe<br />
**LogicalName**: isunsafe<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


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
**RequiredLevel**: None<br />
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
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OnHoldTime"></a> OnHoldTime

**Description**: Shows how long, in minutes, that the record was on hold.<br />
**DisplayName**: On Hold Time (Minutes)<br />
**LogicalName**: onholdtime<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


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

**Description**: Unique identifier of the business unit that owns the email activity.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier of the team who owns the email activity.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns the email activity.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ParentActivityIdName"></a> ParentActivityIdName

**Description**: Parent Activity Name<br />
**DisplayName**: Parent Activity Name<br />
**LogicalName**: parentactivityidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 400


### <a name="BKMK_PostponeEmailProcessingUntil"></a> PostponeEmailProcessingUntil

**Description**: For internal use only.<br />
**DisplayName**: Delay email processing until<br />
**LogicalName**: postponeemailprocessinguntil<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjectidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_RegardingObjectIdYomiName"></a> RegardingObjectIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjectidyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ReplyCount"></a> ReplyCount

**Description**: Shows the number of replies received for an email.<br />
**DisplayName**: Reply Count<br />
**LogicalName**: replycount<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_SafeDescription"></a> SafeDescription

**Description**: Safe body text of the e-mail.<br />
**DisplayName**: Safe Description<br />
**LogicalName**: safedescription<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: Email<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_ScheduledDurationMinutes"></a> ScheduledDurationMinutes

**Description**: Scheduled duration of the email activity, specified in minutes.<br />
**DisplayName**: Scheduled Duration<br />
**LogicalName**: scheduleddurationminutes<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: Duration<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_SenderMailboxId"></a> SenderMailboxId

**Description**: Select the mailbox associated with the sender of the email message.<br />
**DisplayName**: Sender's Mailbox<br />
**LogicalName**: sendermailboxid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: mailbox


### <a name="BKMK_SenderMailboxIdName"></a> SenderMailboxIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: sendermailboxidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_SendersAccount"></a> SendersAccount

**Description**: Shows the parent account of the sender of the email.<br />
**DisplayName**: Senders Account<br />
**LogicalName**: sendersaccount<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: account


### <a name="BKMK_SendersAccountObjectTypeCode"></a> SendersAccountObjectTypeCode

**Description**: Shows the parent account type code of the sender of the email.<br />
**DisplayName**:  SendersAccount Type<br />
**LogicalName**: sendersaccountobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_SendersAccountYomiName"></a> SendersAccountYomiName

**Description**: Shows the name of the sender account yomi name <br />
**DisplayName**: Email Sender Account yomi Name<br />
**LogicalName**: sendersaccountyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 400


### <a name="BKMK_SentOn"></a> SentOn

**Description**: Shows the date and time that the email was sent.<br />
**DisplayName**: Date Sent<br />
**LogicalName**: senton<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_SLAInvokedId"></a> SLAInvokedId

**Description**: Last SLA that was applied to this email. This field is for internal use only.<br />
**DisplayName**: Last SLA applied<br />
**LogicalName**: slainvokedid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: sla


### <a name="BKMK_SLAInvokedIdName"></a> SLAInvokedIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: slainvokedidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_SLAName"></a> SLAName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: slaname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_TemplateIdName"></a> TemplateIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: templateidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


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

**Description**: Version number of the email message.<br />
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
- [userentityinstancedata_email](#BKMK_userentityinstancedata_email)
- [Email_BulkDeleteFailures](#BKMK_Email_BulkDeleteFailures)
- [email_connections1](#BKMK_email_connections1)
- [email_connections2](#BKMK_email_connections2)
- [Email_QueueItem](#BKMK_Email_QueueItem)


### <a name="BKMK_email_actioncard"></a> email_actioncard

Same as actioncard entity [email_actioncard](actioncard.md#BKMK_email_actioncard) Many-To-One relationship.

**ReferencingEntity**: actioncard<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: email_actioncard<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_email_activity_parties"></a> email_activity_parties

Same as activityparty entity [email_activity_parties](activityparty.md#BKMK_email_activity_parties) Many-To-One relationship.

**ReferencingEntity**: activityparty<br />
**ReferencingAttribute**: activityid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: email_activity_parties<br />
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


### <a name="BKMK_Email_DuplicateMatchingRecord"></a> Email_DuplicateMatchingRecord

Same as duplicaterecord entity [Email_DuplicateMatchingRecord](duplicaterecord.md#BKMK_Email_DuplicateMatchingRecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: duplicaterecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Email_DuplicateMatchingRecord<br />
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


### <a name="BKMK_Email_SyncErrors"></a> Email_SyncErrors

Same as syncerror entity [Email_SyncErrors](syncerror.md#BKMK_Email_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: Email_SyncErrors<br />
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


### <a name="BKMK_Email_DuplicateBaseRecord"></a> Email_DuplicateBaseRecord

Same as duplicaterecord entity [Email_DuplicateBaseRecord](duplicaterecord.md#BKMK_Email_DuplicateBaseRecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: baserecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Email_DuplicateBaseRecord<br />
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


### <a name="BKMK_Email_AsyncOperations"></a> Email_AsyncOperations

Same as asyncoperation entity [Email_AsyncOperations](asyncoperation.md#BKMK_Email_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Email_AsyncOperations<br />
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


### <a name="BKMK_Email_ProcessSessions"></a> Email_ProcessSessions

Same as processsession entity [Email_ProcessSessions](processsession.md#BKMK_Email_ProcessSessions) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Email_ProcessSessions<br />
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


### <a name="BKMK_slakpiinstance_email"></a> slakpiinstance_email

Same as slakpiinstance entity [slakpiinstance_email](slakpiinstance.md#BKMK_slakpiinstance_email) Many-To-One relationship.

**ReferencingEntity**: slakpiinstance<br />
**ReferencingAttribute**: regarding<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: slakpiinstance_email<br />
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


### <a name="BKMK_Email_Annotation"></a> Email_Annotation

Same as annotation entity [Email_Annotation](annotation.md#BKMK_Email_Annotation) Many-To-One relationship.

**ReferencingEntity**: annotation<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: Email_Annotation<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_email_activity_mime_attachment"></a> email_activity_mime_attachment

Same as activitymimeattachment entity [email_activity_mime_attachment](activitymimeattachment.md#BKMK_email_activity_mime_attachment) Many-To-One relationship.

**ReferencingEntity**: activitymimeattachment<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: email_activity_mime_attachment<br />
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


### <a name="BKMK_email_email_parentactivityid"></a> email_email_parentactivityid

Same as email entity [email_email_parentactivityid](email.md#BKMK_email_email_parentactivityid) Many-To-One relationship.

**ReferencingEntity**: email<br />
**ReferencingAttribute**: parentactivityid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: email_email_parentactivityid<br />
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


### <a name="BKMK_email_principalobjectattributeaccess"></a> email_principalobjectattributeaccess

Same as principalobjectattributeaccess entity [email_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_email_principalobjectattributeaccess) Many-To-One relationship.

**ReferencingEntity**: principalobjectattributeaccess<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: email_principalobjectattributeaccess<br />
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


### <a name="BKMK_userentityinstancedata_email"></a> userentityinstancedata_email

Same as userentityinstancedata entity [userentityinstancedata_email](userentityinstancedata.md#BKMK_userentityinstancedata_email) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_email<br />
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


### <a name="BKMK_Email_BulkDeleteFailures"></a> Email_BulkDeleteFailures

Same as bulkdeletefailure entity [Email_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Email_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Email_BulkDeleteFailures<br />
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


### <a name="BKMK_email_connections1"></a> email_connections1

Same as connection entity [email_connections1](connection.md#BKMK_email_connections1) Many-To-One relationship.

**ReferencingEntity**: connection<br />
**ReferencingAttribute**: record1id<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: email_connections1<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 100

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_email_connections2"></a> email_connections2

Same as connection entity [email_connections2](connection.md#BKMK_email_connections2) Many-To-One relationship.

**ReferencingEntity**: connection<br />
**ReferencingAttribute**: record2id<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: email_connections2<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 100

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_Email_QueueItem"></a> Email_QueueItem

Same as queueitem entity [Email_QueueItem](queueitem.md#BKMK_Email_QueueItem) Many-To-One relationship.

**ReferencingEntity**: queueitem<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: Email_QueueItem<br />
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


### <a name="BKMK_KnowledgeBaseRecord_Emails"></a> KnowledgeBaseRecord_Emails

See knowledgebaserecord Entity [KnowledgeBaseRecord_Emails](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_Emails) One-To-Many relationship.

### <a name="BKMK_lk_email_modifiedby"></a> lk_email_modifiedby

See systemuser Entity [lk_email_modifiedby](systemuser.md#BKMK_lk_email_modifiedby) One-To-Many relationship.

### <a name="BKMK_Account_Email_SendersAccount"></a> Account_Email_SendersAccount

See account Entity [Account_Email_SendersAccount](account.md#BKMK_Account_Email_SendersAccount) One-To-Many relationship.

### <a name="BKMK_Email_EmailTemplate"></a> Email_EmailTemplate

See template Entity [Email_EmailTemplate](template.md#BKMK_Email_EmailTemplate) One-To-Many relationship.

### <a name="BKMK_Queue_Email_EmailSender"></a> Queue_Email_EmailSender

See queue Entity [Queue_Email_EmailSender](queue.md#BKMK_Queue_Email_EmailSender) One-To-Many relationship.

### <a name="BKMK_Contact_Email_EmailSender"></a> Contact_Email_EmailSender

See contact Entity [Contact_Email_EmailSender](contact.md#BKMK_Contact_Email_EmailSender) One-To-Many relationship.

### <a name="BKMK_Account_Email_EmailSender"></a> Account_Email_EmailSender

See account Entity [Account_Email_EmailSender](account.md#BKMK_Account_Email_EmailSender) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_Email"></a> TransactionCurrency_Email

See transactioncurrency Entity [TransactionCurrency_Email](transactioncurrency.md#BKMK_TransactionCurrency_Email) One-To-Many relationship.

### <a name="BKMK_Contact_Emails"></a> Contact_Emails

See contact Entity [Contact_Emails](contact.md#BKMK_Contact_Emails) One-To-Many relationship.

### <a name="BKMK_user_email"></a> user_email

See systemuser Entity [user_email](systemuser.md#BKMK_user_email) One-To-Many relationship.

### <a name="BKMK_SystemUser_Email_EmailSender"></a> SystemUser_Email_EmailSender

See systemuser Entity [SystemUser_Email_EmailSender](systemuser.md#BKMK_SystemUser_Email_EmailSender) One-To-Many relationship.

### <a name="BKMK_AsyncOperation_Emails"></a> AsyncOperation_Emails

See asyncoperation Entity [AsyncOperation_Emails](asyncoperation.md#BKMK_AsyncOperation_Emails) One-To-Many relationship.

### <a name="BKMK_lk_email_createdonbehalfby"></a> lk_email_createdonbehalfby

See systemuser Entity [lk_email_createdonbehalfby](systemuser.md#BKMK_lk_email_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_KnowledgeArticle_Emails"></a> KnowledgeArticle_Emails

See knowledgearticle Entity [KnowledgeArticle_Emails](knowledgearticle.md#BKMK_KnowledgeArticle_Emails) One-To-Many relationship.

### <a name="BKMK_email_sendermailboxid_mailbox"></a> email_sendermailboxid_mailbox

See mailbox Entity [email_sendermailboxid_mailbox](mailbox.md#BKMK_email_sendermailboxid_mailbox) One-To-Many relationship.

### <a name="BKMK_activity_pointer_email"></a> activity_pointer_email

See activitypointer Entity [activity_pointer_email](activitypointer.md#BKMK_activity_pointer_email) One-To-Many relationship.

### <a name="BKMK_lk_email_modifiedonbehalfby"></a> lk_email_modifiedonbehalfby

See systemuser Entity [lk_email_modifiedonbehalfby](systemuser.md#BKMK_lk_email_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_team_email"></a> team_email

See team Entity [team_email](team.md#BKMK_team_email) One-To-Many relationship.

### <a name="BKMK_manualsla_email"></a> manualsla_email

See sla Entity [manualsla_email](sla.md#BKMK_manualsla_email) One-To-Many relationship.

### <a name="BKMK_business_unit_email_activities"></a> business_unit_email_activities

See businessunit Entity [business_unit_email_activities](businessunit.md#BKMK_business_unit_email_activities) One-To-Many relationship.

### <a name="BKMK_Account_Emails"></a> Account_Emails

See account Entity [Account_Emails](account.md#BKMK_Account_Emails) One-To-Many relationship.

### <a name="BKMK_email_email_parentactivityid"></a> email_email_parentactivityid

See email Entity [email_email_parentactivityid](email.md#BKMK_email_email_parentactivityid) One-To-Many relationship.

### <a name="BKMK_processstage_emails"></a> processstage_emails

See processstage Entity [processstage_emails](processstage.md#BKMK_processstage_emails) One-To-Many relationship.

### <a name="BKMK_sla_email"></a> sla_email

See sla Entity [sla_email](sla.md#BKMK_sla_email) One-To-Many relationship.

### <a name="BKMK_lk_email_createdby"></a> lk_email_createdby

See systemuser Entity [lk_email_createdby](systemuser.md#BKMK_lk_email_createdby) One-To-Many relationship.
email

