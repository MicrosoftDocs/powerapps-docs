---
title: "Appointment table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Appointment table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Appointment table/entity reference (Microsoft Dataverse)

Commitment representing a time interval with start/end times and duration.

## Messages

The following table lists the messages for the Appointment table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /appointments(*activityid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Book`<br />Event: True |<xref:Microsoft.Dynamics.CRM.Book?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.BookRequest>|
| `Create`<br />Event: True |`POST` /appointments<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateException`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateException?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.CreateExceptionRequest>|
| `Delete`<br />Event: True |`DELETE` /appointments(*activityid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `ImmediateBook`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ImmediateBook?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ImmediateBookRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Reschedule`<br />Event: True |<xref:Microsoft.Dynamics.CRM.Reschedule?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RescheduleRequest>|
| `Retrieve`<br />Event: True |`GET` /appointments(*activityid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /appointments<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /appointments(*activityid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /appointments(*activityid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /appointments(*activityid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `Validate`<br />Event: True |<xref:Microsoft.Dynamics.CRM.Validate?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ValidateRequest>|
| `ValidateSavedQuery`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ValidateSavedQuery?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ValidateSavedQueryRequest>|
| `ValidateUnpublished`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ValidateUnpublished?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ValidateUnpublishedRequest>|

## Properties

The following table lists selected properties for the Appointment table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Appointment** |
| **DisplayCollectionName** | **Appointments** |
| **SchemaName** | `Appointment` |
| **CollectionSchemaName** | `Appointments` |
| **EntitySetName** | `appointments`|
| **LogicalName** | `appointment` |
| **LogicalCollectionName** | `appointments` |
| **PrimaryIdAttribute** | `activityid` |
| **PrimaryNameAttribute** |`subject` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ActivityAdditionalParams](#BKMK_ActivityAdditionalParams)
- [ActivityId](#BKMK_ActivityId)
- [ActualDurationMinutes](#BKMK_ActualDurationMinutes)
- [ActualEnd](#BKMK_ActualEnd)
- [ActualStart](#BKMK_ActualStart)
- [AttachmentErrors](#BKMK_AttachmentErrors)
- [Category](#BKMK_Category)
- [Description](#BKMK_Description)
- [GlobalObjectId](#BKMK_GlobalObjectId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsAllDayEvent](#BKMK_IsAllDayEvent)
- [IsBilled](#BKMK_IsBilled)
- [IsDraft](#BKMK_IsDraft)
- [IsMapiPrivate](#BKMK_IsMapiPrivate)
- [IsOnlineMeeting](#BKMK_IsOnlineMeeting)
- [IsWorkflowCreated](#BKMK_IsWorkflowCreated)
- [LastOnHoldTime](#BKMK_LastOnHoldTime)
- [Location](#BKMK_Location)
- [OnlineMeetingChatId](#BKMK_OnlineMeetingChatId)
- [OnlineMeetingId](#BKMK_OnlineMeetingId)
- [OnlineMeetingJoinUrl](#BKMK_OnlineMeetingJoinUrl)
- [OnlineMeetingType](#BKMK_OnlineMeetingType)
- [OptionalAttendees](#BKMK_OptionalAttendees)
- [Organizer](#BKMK_Organizer)
- [OutlookOwnerApptId](#BKMK_OutlookOwnerApptId)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [PriorityCode](#BKMK_PriorityCode)
- [ProcessId](#BKMK_ProcessId)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [requiredattendees](#BKMK_requiredattendees)
- [ScheduledDurationMinutes](#BKMK_ScheduledDurationMinutes)
- [ScheduledEnd](#BKMK_ScheduledEnd)
- [ScheduledStart](#BKMK_ScheduledStart)
- [SLAId](#BKMK_SLAId)
- [SortDate](#BKMK_SortDate)
- [StageId](#BKMK_StageId)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [Subcategory](#BKMK_Subcategory)
- [Subject](#BKMK_Subject)
- [SubscriptionId](#BKMK_SubscriptionId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [TraversedPath](#BKMK_TraversedPath)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

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
|Description|**Unique identifier of the appointment.**|
|DisplayName|**Appointment**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`activityid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ActualDurationMinutes"></a> ActualDurationMinutes

|Property|Value|
|---|---|
|Description|**Shows the value selected in the Duration field on the appointment at the time that the appointment is closed as completed. The duration is used to report the time spent on the activity.**|
|DisplayName|**Actual Duration**|
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
|Description|**Enter the actual end date and time of the appointment. By default, it displays the date and time when the activity was completed or canceled, but can be edited to capture the actual duration of the appointment.**|
|DisplayName|**Actual End**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`actualend`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ActualStart"></a> ActualStart

|Property|Value|
|---|---|
|Description|**Enter the actual start date and time for the appointment. By default, it displays the date and time when the activity was created, but can be edited to capture the actual duration of the appointment.**|
|DisplayName|**Actual Start**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`actualstart`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_AttachmentErrors"></a> AttachmentErrors

|Property|Value|
|---|---|
|Description|**Select the error code to identify issues with the outlook item recipients or attachments, such as blocked attachments.**|
|DisplayName|**AttachmentErrors**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`attachmenterrors`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`appointment_attachmenterrors`|

#### AttachmentErrors Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**The appointment was saved as a Microsoft Dynamics 365 appointment record, but not all the attachments could be saved with it. An attachment cannot be saved if it is blocked or if its file type is invalid.**|

### <a name="BKMK_Category"></a> Category

|Property|Value|
|---|---|
|Description|**Type a category to identify the appointment type, such as sales demo, prospect call, or service call, to tie the appointment to a business group or function.**|
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

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Type additional information to describe the purpose of the appointment.**|
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
|MaxLength|1048576|

### <a name="BKMK_GlobalObjectId"></a> GlobalObjectId

|Property|Value|
|---|---|
|Description|**Shows the ID of the appointment in Microsoft Office Outlook. The ID is used to synchronize the appointment between Microsoft Dynamics 365 and the correct Exchange account.**|
|DisplayName|**Outlook Appointment**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`globalobjectid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|300|

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

### <a name="BKMK_IsAllDayEvent"></a> IsAllDayEvent

|Property|Value|
|---|---|
|Description|**Select whether the appointment is an all-day event to make sure that the required resources are scheduled for the full day.**|
|DisplayName|**All Day Event**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isalldayevent`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`appointment_isalldayevent`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsBilled"></a> IsBilled

|Property|Value|
|---|---|
|Description|**Information regarding whether the appointment was billed as part of resolving a case.**|
|DisplayName|**Is Billed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isbilled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`appointment_isbilled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsDraft"></a> IsDraft

|Property|Value|
|---|---|
|Description|**Information regarding whether the appointment is a draft.**|
|DisplayName|**IsDraft**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isdraft`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`appointment_isdraft`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsMapiPrivate"></a> IsMapiPrivate

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Is Private**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismapiprivate`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`appointment_ismapiprivate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsOnlineMeeting"></a> IsOnlineMeeting

|Property|Value|
|---|---|
|Description|**Displays whether or not this is an online meeting.**|
|DisplayName|**Is Online Meeting**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isonlinemeeting`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`isonlinemeeting`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsWorkflowCreated"></a> IsWorkflowCreated

|Property|Value|
|---|---|
|Description|**Information regarding whether the appointment was created from a workflow rule.**|
|DisplayName|**Is Workflow Created**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isworkflowcreated`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`appointment_isworkflowcreated`|
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

### <a name="BKMK_Location"></a> Location

|Property|Value|
|---|---|
|Description|**Type the location where the appointment will take place, such as a conference room or customer office.**|
|DisplayName|**Location**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`location`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_OnlineMeetingChatId"></a> OnlineMeetingChatId

|Property|Value|
|---|---|
|Description|**Shows the online meeting chat id.**|
|DisplayName|**Online Meeting Chat Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`onlinemeetingchatid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_OnlineMeetingId"></a> OnlineMeetingId

|Property|Value|
|---|---|
|Description|**Shows the online meeting id.**|
|DisplayName|**Online Meeting Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`onlinemeetingid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|300|

### <a name="BKMK_OnlineMeetingJoinUrl"></a> OnlineMeetingJoinUrl

|Property|Value|
|---|---|
|Description|**Shows the online meeting join url.**|
|DisplayName|**Online Meeting Join Url**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`onlinemeetingjoinurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|600|

### <a name="BKMK_OnlineMeetingType"></a> OnlineMeetingType

|Property|Value|
|---|---|
|Description|**Displays the online meeting type.**|
|DisplayName|**Online Meeting Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`onlinemeetingtype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`onlinemeetingtype`|

#### OnlineMeetingType Choices/Options

|Value|Label|
|---|---|
|1|**Teams Meeting**|

### <a name="BKMK_OptionalAttendees"></a> OptionalAttendees

|Property|Value|
|---|---|
|Description|**Enter the account, contact, lead, user, or other equipment resources that are not needed at the appointment, but can optionally attend.**|
|DisplayName|**Optional Attendees**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`optionalattendees`|
|RequiredLevel|None|
|Type|PartyList|
|Targets|account, contact, knowledgearticle, queue, systemuser, unresolvedaddress|

### <a name="BKMK_Organizer"></a> Organizer

|Property|Value|
|---|---|
|Description|**Enter the user who is in charge of coordinating or leading the appointment to make sure the appointment is displayed in the user's My Activities view.**|
|DisplayName|**Organizer**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`organizer`|
|RequiredLevel|None|
|Type|PartyList|
|Targets|systemuser|

### <a name="BKMK_OutlookOwnerApptId"></a> OutlookOwnerApptId

|Property|Value|
|---|---|
|Description|**Unique identifier of the Microsoft Office Outlook appointment owner that correlates to the PR\_OWNER\_APPT\_ID MAPI property.**|
|DisplayName|**Outlook Appointment Owner**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`outlookownerapptid`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

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
|GlobalChoiceName|`appointment_prioritycode`|

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

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**Choose the record that the appointment relates to.**|
|DisplayName|**Regarding**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`regardingobjectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account, adx_invitation, contact, knowledgearticle, knowledgebaserecord, mspp_adplacement, mspp_pollplacement, mspp_publishingstatetransitionrule, mspp_redirect, mspp_shortcut, mspp_website|

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

### <a name="BKMK_requiredattendees"></a> requiredattendees

|Property|Value|
|---|---|
|Description|**Enter the account, contact, lead, user, or other equipment resources that are required to attend the appointment.**|
|DisplayName|**Required Attendees**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`requiredattendees`|
|RequiredLevel|None|
|Type|PartyList|
|Targets|account, contact, knowledgearticle, queue, systemuser, unresolvedaddress|

### <a name="BKMK_ScheduledDurationMinutes"></a> ScheduledDurationMinutes

|Property|Value|
|---|---|
|Description|**Shows the expected duration of the appointment, in minutes.**|
|DisplayName|**Duration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`scheduleddurationminutes`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ScheduledEnd"></a> ScheduledEnd

|Property|Value|
|---|---|
|Description|**Enter the expected due date and time for the activity to be completed to provide details about the timing of the appointment.**|
|DisplayName|**End Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`scheduledend`|
|RequiredLevel|ApplicationRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ScheduledStart"></a> ScheduledStart

|Property|Value|
|---|---|
|Description|**Enter the expected start date and time for the activity to provide details about the timing of the appointment.**|
|DisplayName|**Start Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`scheduledstart`|
|RequiredLevel|ApplicationRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_SLAId"></a> SLAId

|Property|Value|
|---|---|
|Description|**Choose the service level agreement (SLA) that you want to apply to the appointment record.**|
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
|Description|**Shows whether the appointment is open, completed, or canceled. Completed and canceled appointments are read-only and can't be edited.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`appointment_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Open**<br />DefaultStatus: 1<br />InvariantName: `Open`|
|1|Label: **Completed**<br />DefaultStatus: 3<br />InvariantName: `Completed`|
|2|Label: **Canceled**<br />DefaultStatus: 4<br />InvariantName: `Canceled`|
|3|Label: **Scheduled**<br />DefaultStatus: 5<br />InvariantName: `Scheduled`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Select the appointment's status.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`appointment_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Free**<br />State:0<br />TransitionData: None|
|2|Label: **Tentative**<br />State:0<br />TransitionData: None|
|3|Label: **Completed**<br />State:1<br />TransitionData: None|
|4|Label: **Canceled**<br />State:2<br />TransitionData: None|
|5|Label: **Busy**<br />State:3<br />TransitionData: None|
|6|Label: **Out of Office**<br />State:3<br />TransitionData: None|

### <a name="BKMK_Subcategory"></a> Subcategory

|Property|Value|
|---|---|
|Description|**Type a subcategory to identify the appointment type and relate the activity to a specific product, sales region, business group, or other function.**|
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
|Description|**Type a short description about the objective or primary topic of the appointment.**|
|DisplayName|**Subject**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`subject`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_SubscriptionId"></a> SubscriptionId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Subscription**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`subscriptionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

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
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ExchangeRate](#BKMK_ExchangeRate)
- [FormattedScheduledEnd](#BKMK_FormattedScheduledEnd)
- [FormattedScheduledStart](#BKMK_FormattedScheduledStart)
- [InstanceTypeCode](#BKMK_InstanceTypeCode)
- [IsRegularActivity](#BKMK_IsRegularActivity)
- [IsUnsafe](#BKMK_IsUnsafe)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedFieldsMask](#BKMK_ModifiedFieldsMask)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OnHoldTime](#BKMK_OnHoldTime)
- [OriginalStartDate](#BKMK_OriginalStartDate)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [SafeDescription](#BKMK_SafeDescription)
- [SeriesId](#BKMK_SeriesId)
- [SLAInvokedId](#BKMK_SLAInvokedId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ActivityTypeCode"></a> ActivityTypeCode

|Property|Value|
|---|---|
|Description|**Type of activity.**|
|DisplayName|**Activity Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`activitytypecode`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_AttachmentCount"></a> AttachmentCount

|Property|Value|
|---|---|
|Description|**Shows the number of attachments on the appointment.**|
|DisplayName|**Attachment Count**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`attachmentcount`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

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

### <a name="BKMK_FormattedScheduledEnd"></a> FormattedScheduledEnd

|Property|Value|
|---|---|
|Description|**Formatted scheduled end time of the appointment.**|
|DisplayName|**Formatted End Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`formattedscheduledend`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|TimeZoneIndependent|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_FormattedScheduledStart"></a> FormattedScheduledStart

|Property|Value|
|---|---|
|Description|**Formatted scheduled start time of the appointment.**|
|DisplayName|**Formatted Start Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`formattedscheduledstart`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|TimeZoneIndependent|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_InstanceTypeCode"></a> InstanceTypeCode

|Property|Value|
|---|---|
|Description|**Type of instance of a recurring series.**|
|DisplayName|**Appointment Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`instancetypecode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`appointment_instancetypecode`|

#### InstanceTypeCode Choices/Options

|Value|Label|
|---|---|
|0|**Not Recurring**|
|1|**Recurring Master**|
|2|**Recurring Instance**|
|3|**Recurring Exception**|
|4|**Recurring Future Exception**|

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

### <a name="BKMK_ModifiedFieldsMask"></a> ModifiedFieldsMask

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Modified Fields Mask**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedfieldsmask`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

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
|Description|**Shows who created the record on behalf of another user.**|
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

### <a name="BKMK_OriginalStartDate"></a> OriginalStartDate

|Property|Value|
|---|---|
|Description|**The original start date of the appointment.**|
|DisplayName|**Original Start Date**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`originalstartdate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

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
|Description|**Shows the business unit that the record owner belongs to.**|
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
|Description|**Unique identifier of the team that owns the appointment.**|
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
|Description|**Unique identifier of the user that owns the appointment.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_SafeDescription"></a> SafeDescription

|Property|Value|
|---|---|
|Description|**Safe body text of the appointment.**|
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

### <a name="BKMK_SeriesId"></a> SeriesId

|Property|Value|
|---|---|
|Description|**Shows the ID of the recurring series of an instance.**|
|DisplayName|**Series Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`seriesid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_SLAInvokedId"></a> SLAInvokedId

|Property|Value|
|---|---|
|Description|**Last SLA that was applied to this appointment. This field is for internal use only.**|
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
|Description|**Version number of the appointment.**|
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

- [Account_Appointments](#BKMK_Account_Appointments)
- [activity_pointer_appointment](#BKMK_activity_pointer_appointment)
- [adx_invitation_Appointments](#BKMK_adx_invitation_Appointments)
- [business_unit_appointment_activities](#BKMK_business_unit_appointment_activities)
- [Contact_Appointments](#BKMK_Contact_Appointments)
- [KnowledgeArticle_Appointments](#BKMK_KnowledgeArticle_Appointments)
- [KnowledgeBaseRecord_Appointments](#BKMK_KnowledgeBaseRecord_Appointments)
- [lk_appointment_createdby](#BKMK_lk_appointment_createdby)
- [lk_appointment_createdonbehalfby](#BKMK_lk_appointment_createdonbehalfby)
- [lk_appointment_modifiedby](#BKMK_lk_appointment_modifiedby)
- [lk_appointment_modifiedonbehalfby](#BKMK_lk_appointment_modifiedonbehalfby)
- [manualsla_appointment](#BKMK_manualsla_appointment)
- [mspp_adplacement_Appointments](#BKMK_mspp_adplacement_Appointments)
- [mspp_pollplacement_Appointments](#BKMK_mspp_pollplacement_Appointments)
- [mspp_publishingstatetransitionrule_Appointments](#BKMK_mspp_publishingstatetransitionrule_Appointments)
- [mspp_redirect_Appointments](#BKMK_mspp_redirect_Appointments)
- [mspp_shortcut_Appointments](#BKMK_mspp_shortcut_Appointments)
- [mspp_website_Appointments](#BKMK_mspp_website_Appointments)
- [owner_appointments](#BKMK_owner_appointments)
- [processstage_appointments](#BKMK_processstage_appointments)
- [recurringappointmentmaster_appointment](#BKMK_recurringappointmentmaster_appointment)
- [sla_appointment](#BKMK_sla_appointment)
- [team_appointment](#BKMK_team_appointment)
- [TransactionCurrency_Appointment](#BKMK_TransactionCurrency_Appointment)
- [user_appointment](#BKMK_user_appointment)

### <a name="BKMK_Account_Appointments"></a> Account_Appointments

One-To-Many Relationship: [account Account_Appointments](account.md#BKMK_Account_Appointments)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_account_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_activity_pointer_appointment"></a> activity_pointer_appointment

One-To-Many Relationship: [activitypointer activity_pointer_appointment](activitypointer.md#BKMK_activity_pointer_appointment)

|Property|Value|
|---|---|
|ReferencedEntity|`activitypointer`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`activityid`|
|ReferencingEntityNavigationPropertyName|`activityid_activitypointer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_invitation_Appointments"></a> adx_invitation_Appointments

One-To-Many Relationship: [adx_invitation adx_invitation_Appointments](adx_invitation.md#BKMK_adx_invitation_Appointments)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_invitation`|
|ReferencedAttribute|`adx_invitationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_invitation_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_business_unit_appointment_activities"></a> business_unit_appointment_activities

One-To-Many Relationship: [businessunit business_unit_appointment_activities](businessunit.md#BKMK_business_unit_appointment_activities)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Contact_Appointments"></a> Contact_Appointments

One-To-Many Relationship: [contact Contact_Appointments](contact.md#BKMK_Contact_Appointments)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_contact_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_KnowledgeArticle_Appointments"></a> KnowledgeArticle_Appointments

One-To-Many Relationship: [knowledgearticle KnowledgeArticle_Appointments](knowledgearticle.md#BKMK_KnowledgeArticle_Appointments)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgearticle_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_KnowledgeBaseRecord_Appointments"></a> KnowledgeBaseRecord_Appointments

One-To-Many Relationship: [knowledgebaserecord KnowledgeBaseRecord_Appointments](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_Appointments)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgebaserecord`|
|ReferencedAttribute|`knowledgebaserecordid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgebaserecord_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_appointment_createdby"></a> lk_appointment_createdby

One-To-Many Relationship: [systemuser lk_appointment_createdby](systemuser.md#BKMK_lk_appointment_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_appointment_createdonbehalfby"></a> lk_appointment_createdonbehalfby

One-To-Many Relationship: [systemuser lk_appointment_createdonbehalfby](systemuser.md#BKMK_lk_appointment_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_appointment_modifiedby"></a> lk_appointment_modifiedby

One-To-Many Relationship: [systemuser lk_appointment_modifiedby](systemuser.md#BKMK_lk_appointment_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_appointment_modifiedonbehalfby"></a> lk_appointment_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_appointment_modifiedonbehalfby](systemuser.md#BKMK_lk_appointment_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_manualsla_appointment"></a> manualsla_appointment

One-To-Many Relationship: [sla manualsla_appointment](sla.md#BKMK_manualsla_appointment)

|Property|Value|
|---|---|
|ReferencedEntity|`sla`|
|ReferencedAttribute|`slaid`|
|ReferencingAttribute|`slaid`|
|ReferencingEntityNavigationPropertyName|`sla_appointment_sla`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_adplacement_Appointments"></a> mspp_adplacement_Appointments

One-To-Many Relationship: [mspp_adplacement mspp_adplacement_Appointments](mspp_adplacement.md#BKMK_mspp_adplacement_Appointments)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_adplacement`|
|ReferencedAttribute|`mspp_adplacementid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_adplacement_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_pollplacement_Appointments"></a> mspp_pollplacement_Appointments

One-To-Many Relationship: [mspp_pollplacement mspp_pollplacement_Appointments](mspp_pollplacement.md#BKMK_mspp_pollplacement_Appointments)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_pollplacement`|
|ReferencedAttribute|`mspp_pollplacementid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_pollplacement_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_publishingstatetransitionrule_Appointments"></a> mspp_publishingstatetransitionrule_Appointments

One-To-Many Relationship: [mspp_publishingstatetransitionrule mspp_publishingstatetransitionrule_Appointments](mspp_publishingstatetransitionrule.md#BKMK_mspp_publishingstatetransitionrule_Appointments)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_publishingstatetransitionrule`|
|ReferencedAttribute|`mspp_publishingstatetransitionruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_publishingstatetransitionrule_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_redirect_Appointments"></a> mspp_redirect_Appointments

One-To-Many Relationship: [mspp_redirect mspp_redirect_Appointments](mspp_redirect.md#BKMK_mspp_redirect_Appointments)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_redirect`|
|ReferencedAttribute|`mspp_redirectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_redirect_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_shortcut_Appointments"></a> mspp_shortcut_Appointments

One-To-Many Relationship: [mspp_shortcut mspp_shortcut_Appointments](mspp_shortcut.md#BKMK_mspp_shortcut_Appointments)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_shortcut`|
|ReferencedAttribute|`mspp_shortcutid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_shortcut_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_website_Appointments"></a> mspp_website_Appointments

One-To-Many Relationship: [mspp_website mspp_website_Appointments](mspp_website.md#BKMK_mspp_website_Appointments)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_website`|
|ReferencedAttribute|`mspp_websiteid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_website_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_appointments"></a> owner_appointments

One-To-Many Relationship: [owner owner_appointments](owner.md#BKMK_owner_appointments)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_processstage_appointments"></a> processstage_appointments

One-To-Many Relationship: [processstage processstage_appointments](processstage.md#BKMK_processstage_appointments)

|Property|Value|
|---|---|
|ReferencedEntity|`processstage`|
|ReferencedAttribute|`processstageid`|
|ReferencingAttribute|`stageid`|
|ReferencingEntityNavigationPropertyName|`stageid_processstage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recurringappointmentmaster_appointment"></a> recurringappointmentmaster_appointment

One-To-Many Relationship: [recurringappointmentmaster recurringappointmentmaster_appointment](recurringappointmentmaster.md#BKMK_recurringappointmentmaster_appointment)

|Property|Value|
|---|---|
|ReferencedEntity|`recurringappointmentmaster`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`seriesid`|
|ReferencingEntityNavigationPropertyName|`seriesid_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sla_appointment"></a> sla_appointment

One-To-Many Relationship: [sla sla_appointment](sla.md#BKMK_sla_appointment)

|Property|Value|
|---|---|
|ReferencedEntity|`sla`|
|ReferencedAttribute|`slaid`|
|ReferencingAttribute|`slainvokedid`|
|ReferencingEntityNavigationPropertyName|`slainvokedid_appointment_sla`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_appointment"></a> team_appointment

One-To-Many Relationship: [team team_appointment](team.md#BKMK_team_appointment)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_Appointment"></a> TransactionCurrency_Appointment

One-To-Many Relationship: [transactioncurrency TransactionCurrency_Appointment](transactioncurrency.md#BKMK_TransactionCurrency_Appointment)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencingEntityNavigationPropertyName|`transactioncurrencyid_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_appointment"></a> user_appointment

One-To-Many Relationship: [systemuser user_appointment](systemuser.md#BKMK_user_appointment)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [appointment_actioncard](#BKMK_appointment_actioncard)
- [appointment_activity_mime_attachment](#BKMK_appointment_activity_mime_attachment)
- [appointment_activity_parties](#BKMK_appointment_activity_parties)
- [Appointment_Annotation](#BKMK_Appointment_Annotation)
- [Appointment_AsyncOperations](#BKMK_Appointment_AsyncOperations)
- [Appointment_BulkDeleteFailures](#BKMK_Appointment_BulkDeleteFailures)
- [appointment_connections1](#BKMK_appointment_connections1)
- [appointment_connections2](#BKMK_appointment_connections2)
- [Appointment_DuplicateBaseRecord](#BKMK_Appointment_DuplicateBaseRecord)
- [Appointment_DuplicateMatchingRecord](#BKMK_Appointment_DuplicateMatchingRecord)
- [appointment_PostFollows](#BKMK_appointment_PostFollows)
- [appointment_PostRegardings](#BKMK_appointment_PostRegardings)
- [appointment_principalobjectattributeaccess](#BKMK_appointment_principalobjectattributeaccess)
- [Appointment_ProcessSessions](#BKMK_Appointment_ProcessSessions)
- [Appointment_QueueItem](#BKMK_Appointment_QueueItem)
- [Appointment_SyncErrors](#BKMK_Appointment_SyncErrors)
- [slakpiinstance_appointment](#BKMK_slakpiinstance_appointment)

### <a name="BKMK_appointment_actioncard"></a> appointment_actioncard

Many-To-One Relationship: [actioncard appointment_actioncard](actioncard.md#BKMK_appointment_actioncard)

|Property|Value|
|---|---|
|ReferencingEntity|`actioncard`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`appointment_actioncard`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_appointment_activity_mime_attachment"></a> appointment_activity_mime_attachment

Many-To-One Relationship: [activitymimeattachment appointment_activity_mime_attachment](activitymimeattachment.md#BKMK_appointment_activity_mime_attachment)

|Property|Value|
|---|---|
|ReferencingEntity|`activitymimeattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`appointment_activity_mime_attachment`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_appointment_activity_parties"></a> appointment_activity_parties

Many-To-One Relationship: [activityparty appointment_activity_parties](activityparty.md#BKMK_appointment_activity_parties)

|Property|Value|
|---|---|
|ReferencingEntity|`activityparty`|
|ReferencingAttribute|`activityid`|
|ReferencedEntityNavigationPropertyName|`appointment_activity_parties`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Appointment_Annotation"></a> Appointment_Annotation

Many-To-One Relationship: [annotation Appointment_Annotation](annotation.md#BKMK_Appointment_Annotation)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`Appointment_Annotation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Appointment_AsyncOperations"></a> Appointment_AsyncOperations

Many-To-One Relationship: [asyncoperation Appointment_AsyncOperations](asyncoperation.md#BKMK_Appointment_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Appointment_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Appointment_BulkDeleteFailures"></a> Appointment_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure Appointment_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Appointment_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Appointment_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_appointment_connections1"></a> appointment_connections1

Many-To-One Relationship: [connection appointment_connections1](connection.md#BKMK_appointment_connections1)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record1id`|
|ReferencedEntityNavigationPropertyName|`appointment_connections1`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_appointment_connections2"></a> appointment_connections2

Many-To-One Relationship: [connection appointment_connections2](connection.md#BKMK_appointment_connections2)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record2id`|
|ReferencedEntityNavigationPropertyName|`appointment_connections2`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Appointment_DuplicateBaseRecord"></a> Appointment_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord Appointment_DuplicateBaseRecord](duplicaterecord.md#BKMK_Appointment_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`Appointment_DuplicateBaseRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Appointment_DuplicateMatchingRecord"></a> Appointment_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord Appointment_DuplicateMatchingRecord](duplicaterecord.md#BKMK_Appointment_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`Appointment_DuplicateMatchingRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_appointment_PostFollows"></a> appointment_PostFollows

Many-To-One Relationship: [postfollow appointment_PostFollows](postfollow.md#BKMK_appointment_PostFollows)

|Property|Value|
|---|---|
|ReferencingEntity|`postfollow`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`appointment_PostFollows`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_appointment_PostRegardings"></a> appointment_PostRegardings

Many-To-One Relationship: [postregarding appointment_PostRegardings](postregarding.md#BKMK_appointment_PostRegardings)

|Property|Value|
|---|---|
|ReferencingEntity|`postregarding`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`appointment_PostRegardings`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_appointment_principalobjectattributeaccess"></a> appointment_principalobjectattributeaccess

Many-To-One Relationship: [principalobjectattributeaccess appointment_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_appointment_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`appointment_principalobjectattributeaccess`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Appointment_ProcessSessions"></a> Appointment_ProcessSessions

Many-To-One Relationship: [processsession Appointment_ProcessSessions](processsession.md#BKMK_Appointment_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Appointment_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Appointment_QueueItem"></a> Appointment_QueueItem

Many-To-One Relationship: [queueitem Appointment_QueueItem](queueitem.md#BKMK_Appointment_QueueItem)

|Property|Value|
|---|---|
|ReferencingEntity|`queueitem`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`Appointment_QueueItem`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Appointment_SyncErrors"></a> Appointment_SyncErrors

Many-To-One Relationship: [syncerror Appointment_SyncErrors](syncerror.md#BKMK_Appointment_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Appointment_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_slakpiinstance_appointment"></a> slakpiinstance_appointment

Many-To-One Relationship: [slakpiinstance slakpiinstance_appointment](slakpiinstance.md#BKMK_slakpiinstance_appointment)

|Property|Value|
|---|---|
|ReferencingEntity|`slakpiinstance`|
|ReferencingAttribute|`regarding`|
|ReferencedEntityNavigationPropertyName|`slakpiinstance_appointment`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.appointment?displayProperty=fullName>
