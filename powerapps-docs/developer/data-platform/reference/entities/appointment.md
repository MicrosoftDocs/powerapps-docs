---
title: "Appointment table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Appointment table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Appointment table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Commitment representing a time interval with start/end times and duration.


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /appointments(*activityid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Book|<xref:Microsoft.Dynamics.CRM.Book?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.BookRequest>|
|Create|POST /appointments<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateException|<xref:Microsoft.Dynamics.CRM.CreateException?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.CreateExceptionRequest>|
|Delete|DELETE /appointments(*activityid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|ImmediateBook|<xref:Microsoft.Dynamics.CRM.ImmediateBook?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ImmediateBookRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Reschedule|<xref:Microsoft.Dynamics.CRM.Reschedule?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RescheduleRequest>|
|Retrieve|GET /appointments(*activityid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /appointments<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH /appointments(*activityid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /appointments(*activityid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|Validate|<xref:Microsoft.Dynamics.CRM.Validate?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ValidateRequest>|
|ValidateSavedQuery|<xref:Microsoft.Dynamics.CRM.ValidateSavedQuery?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ValidateSavedQueryRequest>|
|ValidateUnpublished|<xref:Microsoft.Dynamics.CRM.ValidateUnpublished?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ValidateUnpublishedRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|Appointments|
|DisplayCollectionName|Appointments|
|DisplayName|Appointment|
|EntitySetName|appointments|
|IsBPFEntity|False|
|LogicalCollectionName|appointments|
|LogicalName|appointment|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|activityid|
|PrimaryNameAttribute|subject|
|SchemaName|Appointment|

<a name="writable-attributes"></a>

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
|Description|Unique identifier of the appointment.|
|DisplayName|Appointment|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|activityid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ActualDurationMinutes"></a> ActualDurationMinutes

|Property|Value|
|--------|-----|
|Description|Shows the value selected in the Duration field on the appointment at the time that the appointment is closed as completed. The duration is used to report the time spent on the activity.|
|DisplayName|Actual Duration|
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
|Description|Enter the actual end date and time of the appointment. By default, it displays the date and time when the activity was completed or canceled, but can be edited to capture the actual duration of the appointment.|
|DisplayName|Actual End|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|actualend|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ActualStart"></a> ActualStart

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Enter the actual start date and time for the appointment. By default, it displays the date and time when the activity was created, but can be edited to capture the actual duration of the appointment.|
|DisplayName|Actual Start|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|actualstart|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_AttachmentErrors"></a> AttachmentErrors

|Property|Value|
|--------|-----|
|Description|Select the error code to identify issues with the outlook item recipients or attachments, such as blocked attachments.|
|DisplayName|AttachmentErrors|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|attachmenterrors|
|RequiredLevel|None|
|Type|Picklist|

#### AttachmentErrors Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|None||
|1|The appointment was saved as a Microsoft Dynamics 365 appointment record, but not all the attachments could be saved with it. An attachment cannot be saved if it is blocked or if its file type is invalid.||



### <a name="BKMK_Category"></a> Category

|Property|Value|
|--------|-----|
|Description|Type a category to identify the appointment type, such as sales demo, prospect call, or service call, to tie the appointment to a business group or function.|
|DisplayName|Category|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|category|
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Type additional information to describe the purpose of the appointment.|
|DisplayName|Description|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|1048576|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_GlobalObjectId"></a> GlobalObjectId

|Property|Value|
|--------|-----|
|Description|Shows the ID of the appointment in Microsoft Office Outlook. The ID is used to synchronize the appointment between Microsoft Dynamics 365 and the correct Exchange account.|
|DisplayName|Outlook Appointment|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|globalobjectid|
|MaxLength|300|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_IsAllDayEvent"></a> IsAllDayEvent

|Property|Value|
|--------|-----|
|Description|Select whether the appointment is an all-day event to make sure that the required resources are scheduled for the full day.|
|DisplayName|All Day Event|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isalldayevent|
|RequiredLevel|None|
|Type|Boolean|

#### IsAllDayEvent Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_IsBilled"></a> IsBilled

|Property|Value|
|--------|-----|
|Description|Information regarding whether the appointment was billed as part of resolving a case.|
|DisplayName|Is Billed|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isbilled|
|RequiredLevel|None|
|Type|Boolean|

#### IsBilled Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_IsDraft"></a> IsDraft

|Property|Value|
|--------|-----|
|Description|Information regarding whether the appointment is a draft.|
|DisplayName|IsDraft|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isdraft|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsDraft Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_IsMapiPrivate"></a> IsMapiPrivate

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Is Private|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismapiprivate|
|RequiredLevel|None|
|Type|Boolean|

#### IsMapiPrivate Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_IsOnlineMeeting"></a> IsOnlineMeeting

**Added by**: msft_ActivitiesInfra_Extensions Solution

|Property|Value|
|--------|-----|
|Description|Displays whether or not this is an online meeting.|
|DisplayName|Is Online Meeting|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isonlinemeeting|
|RequiredLevel|None|
|Type|Boolean|

#### IsOnlineMeeting Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_IsWorkflowCreated"></a> IsWorkflowCreated

|Property|Value|
|--------|-----|
|Description|Information regarding whether the appointment was created from a workflow rule.|
|DisplayName|Is Workflow Created|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isworkflowcreated|
|RequiredLevel|None|
|Type|Boolean|

#### IsWorkflowCreated Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



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


### <a name="BKMK_Location"></a> Location

|Property|Value|
|--------|-----|
|Description|Type the location where the appointment will take place, such as a conference room or customer office.|
|DisplayName|Location|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|location|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OnlineMeetingChatId"></a> OnlineMeetingChatId

**Added by**: msft_ActivitiesInfra_Extensions Solution

|Property|Value|
|--------|-----|
|Description|Shows the online meeting chat id.|
|DisplayName|Online Meeting Chat Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|onlinemeetingchatid|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OnlineMeetingId"></a> OnlineMeetingId

**Added by**: msft_ActivitiesInfra_Extensions Solution

|Property|Value|
|--------|-----|
|Description|Shows the online meeting id.|
|DisplayName|Online Meeting Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|onlinemeetingid|
|MaxLength|300|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OnlineMeetingJoinUrl"></a> OnlineMeetingJoinUrl

**Added by**: msft_ActivitiesInfra_Extensions Solution

|Property|Value|
|--------|-----|
|Description|Shows the online meeting join url.|
|DisplayName|Online Meeting Join Url|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|onlinemeetingjoinurl|
|MaxLength|600|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OnlineMeetingType"></a> OnlineMeetingType

**Added by**: msft_ActivitiesInfra_Extensions Solution

|Property|Value|
|--------|-----|
|Description|Displays the online meeting type.|
|DisplayName|Online Meeting Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|onlinemeetingtype|
|RequiredLevel|None|
|Type|Picklist|

#### OnlineMeetingType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Teams Meeting||



### <a name="BKMK_OptionalAttendees"></a> OptionalAttendees

|Property|Value|
|--------|-----|
|Description|Enter the account, contact, lead, user, or other equipment resources that are not needed at the appointment, but can optionally attend.|
|DisplayName|Optional Attendees|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|optionalattendees|
|RequiredLevel|None|
|Targets|account,contact,knowledgearticle,queue,systemuser,unresolvedaddress|
|Type|PartyList|


### <a name="BKMK_Organizer"></a> Organizer

|Property|Value|
|--------|-----|
|Description|Enter the user who is in charge of coordinating or leading the appointment to make sure the appointment is displayed in the user's My Activities view.|
|DisplayName|Organizer|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|organizer|
|RequiredLevel|None|
|Targets|systemuser|
|Type|PartyList|


### <a name="BKMK_OutlookOwnerApptId"></a> OutlookOwnerApptId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the Microsoft Office Outlook appointment owner that correlates to the PR_OWNER_APPT_ID MAPI property.|
|DisplayName|Outlook Appointment Owner|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|outlookownerapptid|
|MaxValue|2147483647|
|MinValue|-2147483648|
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

|Value|Label|Description|
|-----|-----|--------|
|0|Low||
|1|Normal||
|2|High||



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


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|--------|-----|
|Description|Choose the record that the appointment relates to.|
|DisplayName|Regarding|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|regardingobjectid|
|RequiredLevel|None|
|Targets|account,contact,knowledgearticle,knowledgebaserecord|
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


### <a name="BKMK_requiredattendees"></a> requiredattendees

|Property|Value|
|--------|-----|
|Description|Enter the account, contact, lead, user, or other equipment resources that are required to attend the appointment.|
|DisplayName|Required Attendees|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|requiredattendees|
|RequiredLevel|None|
|Targets|account,contact,knowledgearticle,queue,systemuser,unresolvedaddress|
|Type|PartyList|


### <a name="BKMK_ScheduledDurationMinutes"></a> ScheduledDurationMinutes

|Property|Value|
|--------|-----|
|Description|Shows the expected duration of the appointment, in minutes.|
|DisplayName|Duration|
|Format|Duration|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|scheduleddurationminutes|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ScheduledEnd"></a> ScheduledEnd

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Enter the expected due date and time for the activity to be completed to provide details about the timing of the appointment.|
|DisplayName|End Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|scheduledend|
|RequiredLevel|ApplicationRequired|
|Type|DateTime|


### <a name="BKMK_ScheduledStart"></a> ScheduledStart

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Enter the expected start date and time for the activity to provide details about the timing of the appointment.|
|DisplayName|Start Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|scheduledstart|
|RequiredLevel|ApplicationRequired|
|Type|DateTime|


### <a name="BKMK_SLAId"></a> SLAId

|Property|Value|
|--------|-----|
|Description|Choose the service level agreement (SLA) that you want to apply to the appointment record.|
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
|Description|Shows whether the appointment is open, completed, or canceled. Completed and canceled appointments are read-only and can't be edited.|
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
|0|Open|1|Open|
|1|Completed|3|Completed|
|2|Canceled|4|Canceled|
|3|Scheduled|5|Scheduled|



### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|--------|-----|
|Description|Select the appointment's status.|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### StatusCode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Free|0|
|2|Tentative|0|
|3|Completed|1|
|4|Canceled|2|
|5|Busy|3|
|6|Out of Office|3|



### <a name="BKMK_Subcategory"></a> Subcategory

|Property|Value|
|--------|-----|
|Description|Type a subcategory to identify the appointment type and relate the activity to a specific product, sales region, business group, or other function.|
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
|Description|Type a short description about the objective or primary topic of the appointment.|
|DisplayName|Subject|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|subject|
|MaxLength|200|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_SubscriptionId"></a> SubscriptionId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Subscription|
|IsValidForForm|False|
|IsValidForRead|False|
|IsValidForUpdate|False|
|LogicalName|subscriptionid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


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
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ExchangeRate](#BKMK_ExchangeRate)
- [FormattedScheduledEnd](#BKMK_FormattedScheduledEnd)
- [FormattedScheduledStart](#BKMK_FormattedScheduledStart)
- [InstanceTypeCode](#BKMK_InstanceTypeCode)
- [IsRegularActivity](#BKMK_IsRegularActivity)
- [IsUnsafe](#BKMK_IsUnsafe)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedFieldsMask](#BKMK_ModifiedFieldsMask)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OnHoldTime](#BKMK_OnHoldTime)
- [OriginalStartDate](#BKMK_OriginalStartDate)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectIdYomiName](#BKMK_RegardingObjectIdYomiName)
- [SafeDescription](#BKMK_SafeDescription)
- [SeriesId](#BKMK_SeriesId)
- [SLAInvokedId](#BKMK_SLAInvokedId)
- [SLAInvokedIdName](#BKMK_SLAInvokedIdName)
- [SLAName](#BKMK_SLAName)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ActivityTypeCode"></a> ActivityTypeCode

|Property|Value|
|--------|-----|
|Description|Type of activity.|
|DisplayName|Activity Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|activitytypecode|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_AttachmentCount"></a> AttachmentCount

|Property|Value|
|--------|-----|
|Description|Shows the number of attachments on the appointment.|
|DisplayName|Attachment Count|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|attachmentcount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|SystemRequired|
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


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|--------|-----|
|Description|Shows the conversion rate of the record's currency. The exchange rate is used to convert all money fields in the record from the local currency to the system's default currency.|
|DisplayName|Exchange Rate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.000000000001|
|Precision|12|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_FormattedScheduledEnd"></a> FormattedScheduledEnd

**Added by**: msft_ActivitiesInfra_Extensions Solution

|Property|Value|
|--------|-----|
|DateTimeBehavior|TimeZoneIndependent|
|Description|Formatted scheduled end time of the appointment.|
|DisplayName|Formatted End Date|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|formattedscheduledend|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_FormattedScheduledStart"></a> FormattedScheduledStart

**Added by**: msft_ActivitiesInfra_Extensions Solution

|Property|Value|
|--------|-----|
|DateTimeBehavior|TimeZoneIndependent|
|Description|Formatted scheduled start time of the appointment.|
|DisplayName|Formatted Start Date|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|formattedscheduledstart|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_InstanceTypeCode"></a> InstanceTypeCode

|Property|Value|
|--------|-----|
|Description|Type of instance of a recurring series.|
|DisplayName|Appointment Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|instancetypecode|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### InstanceTypeCode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Not Recurring||
|1|Recurring Master||
|2|Recurring Instance||
|3|Recurring Exception||
|4|Recurring Future Exception||



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

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



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


### <a name="BKMK_ModifiedFieldsMask"></a> ModifiedFieldsMask

|Property|Value|
|--------|-----|
|Description|For internal use only. |
|DisplayName|Modified Fields Mask|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedfieldsmask|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


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
|Description|Shows who created the record on behalf of another user.|
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


### <a name="BKMK_OriginalStartDate"></a> OriginalStartDate

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|The original start date of the appointment.|
|DisplayName|Original Start Date|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|originalstartdate|
|RequiredLevel|None|
|Type|DateTime|


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
|Description|Shows the business unit that the record owner belongs to.|
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
|Description|Unique identifier of the team that owns the appointment.|
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
|Description|Unique identifier of the user that owns the appointment.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


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


### <a name="BKMK_SafeDescription"></a> SafeDescription

|Property|Value|
|--------|-----|
|Description|Safe body text of the appointment.|
|DisplayName|Safe Description|
|Format|Email|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|safedescription|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_SeriesId"></a> SeriesId

|Property|Value|
|--------|-----|
|Description|Shows the ID of the recurring series of an instance.|
|DisplayName|Series Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|seriesid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_SLAInvokedId"></a> SLAInvokedId

|Property|Value|
|--------|-----|
|Description|Last SLA that was applied to this appointment. This field is for internal use only.|
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
|Description|Version number of the appointment.|
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

- [appointment_PostFollows](#BKMK_appointment_PostFollows)
- [Appointment_DuplicateMatchingRecord](#BKMK_Appointment_DuplicateMatchingRecord)
- [Appointment_ProcessSessions](#BKMK_Appointment_ProcessSessions)
- [appointment_connections1](#BKMK_appointment_connections1)
- [appointment_activity_parties](#BKMK_appointment_activity_parties)
- [Appointment_Annotation](#BKMK_Appointment_Annotation)
- [appointment_connections2](#BKMK_appointment_connections2)
- [Appointment_DuplicateBaseRecord](#BKMK_Appointment_DuplicateBaseRecord)
- [slakpiinstance_appointment](#BKMK_slakpiinstance_appointment)
- [Appointment_SyncErrors](#BKMK_Appointment_SyncErrors)
- [Appointment_AsyncOperations](#BKMK_Appointment_AsyncOperations)
- [appointment_actioncard](#BKMK_appointment_actioncard)
- [appointment_principalobjectattributeaccess](#BKMK_appointment_principalobjectattributeaccess)
- [appointment_activity_mime_attachment](#BKMK_appointment_activity_mime_attachment)
- [Appointment_QueueItem](#BKMK_Appointment_QueueItem)
- [Appointment_BulkDeleteFailures](#BKMK_Appointment_BulkDeleteFailures)


### <a name="BKMK_appointment_PostFollows"></a> appointment_PostFollows

Same as the [appointment_PostFollows](postfollow.md#BKMK_appointment_PostFollows) many-to-one relationship for the [postfollow](postfollow.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|postfollow|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|appointment_PostFollows|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Appointment_DuplicateMatchingRecord"></a> Appointment_DuplicateMatchingRecord

Same as the [Appointment_DuplicateMatchingRecord](duplicaterecord.md#BKMK_Appointment_DuplicateMatchingRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Appointment_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Appointment_ProcessSessions"></a> Appointment_ProcessSessions

Same as the [Appointment_ProcessSessions](processsession.md#BKMK_Appointment_ProcessSessions) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Appointment_ProcessSessions|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 110|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_appointment_connections1"></a> appointment_connections1

Same as the [appointment_connections1](connection.md#BKMK_appointment_connections1) many-to-one relationship for the [connection](connection.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record1id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|appointment_connections1|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_appointment_activity_parties"></a> appointment_activity_parties

Same as the [appointment_activity_parties](activityparty.md#BKMK_appointment_activity_parties) many-to-one relationship for the [activityparty](activityparty.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|activityparty|
|ReferencingAttribute|activityid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|appointment_activity_parties|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Appointment_Annotation"></a> Appointment_Annotation

Same as the [Appointment_Annotation](annotation.md#BKMK_Appointment_Annotation) many-to-one relationship for the [annotation](annotation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Appointment_Annotation|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_appointment_connections2"></a> appointment_connections2

Same as the [appointment_connections2](connection.md#BKMK_appointment_connections2) many-to-one relationship for the [connection](connection.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record2id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|appointment_connections2|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Appointment_DuplicateBaseRecord"></a> Appointment_DuplicateBaseRecord

Same as the [Appointment_DuplicateBaseRecord](duplicaterecord.md#BKMK_Appointment_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Appointment_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_slakpiinstance_appointment"></a> slakpiinstance_appointment

Same as the [slakpiinstance_appointment](slakpiinstance.md#BKMK_slakpiinstance_appointment) many-to-one relationship for the [slakpiinstance](slakpiinstance.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|slakpiinstance|
|ReferencingAttribute|regarding|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|slakpiinstance_appointment|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Appointment_SyncErrors"></a> Appointment_SyncErrors

Same as the [Appointment_SyncErrors](syncerror.md#BKMK_Appointment_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Appointment_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_Appointment_AsyncOperations"></a> Appointment_AsyncOperations

Same as the [Appointment_AsyncOperations](asyncoperation.md#BKMK_Appointment_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Appointment_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_appointment_actioncard"></a> appointment_actioncard

Same as the [appointment_actioncard](actioncard.md#BKMK_appointment_actioncard) many-to-one relationship for the [actioncard](actioncard.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|actioncard|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|appointment_actioncard|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_appointment_principalobjectattributeaccess"></a> appointment_principalobjectattributeaccess

Same as the [appointment_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_appointment_principalobjectattributeaccess) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|appointment_principalobjectattributeaccess|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_appointment_activity_mime_attachment"></a> appointment_activity_mime_attachment

Same as the [appointment_activity_mime_attachment](activitymimeattachment.md#BKMK_appointment_activity_mime_attachment) many-to-one relationship for the [activitymimeattachment](activitymimeattachment.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitymimeattachment|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|appointment_activity_mime_attachment|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Appointment_QueueItem"></a> Appointment_QueueItem

Same as the [Appointment_QueueItem](queueitem.md#BKMK_Appointment_QueueItem) many-to-one relationship for the [queueitem](queueitem.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|queueitem|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Appointment_QueueItem|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Appointment_BulkDeleteFailures"></a> Appointment_BulkDeleteFailures

Same as the [Appointment_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Appointment_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Appointment_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [KnowledgeBaseRecord_Appointments](#BKMK_KnowledgeBaseRecord_Appointments)
- [business_unit_appointment_activities](#BKMK_business_unit_appointment_activities)
- [lk_appointment_modifiedby](#BKMK_lk_appointment_modifiedby)
- [TransactionCurrency_Appointment](#BKMK_TransactionCurrency_Appointment)
- [lk_appointment_modifiedonbehalfby](#BKMK_lk_appointment_modifiedonbehalfby)
- [lk_appointment_createdby](#BKMK_lk_appointment_createdby)
- [sla_appointment](#BKMK_sla_appointment)
- [Contact_Appointments](#BKMK_Contact_Appointments)
- [lk_appointment_createdonbehalfby](#BKMK_lk_appointment_createdonbehalfby)
- [KnowledgeArticle_Appointments](#BKMK_KnowledgeArticle_Appointments)
- [Account_Appointments](#BKMK_Account_Appointments)
- [manualsla_appointment](#BKMK_manualsla_appointment)
- [team_appointment](#BKMK_team_appointment)
- [user_appointment](#BKMK_user_appointment)
- [recurringappointmentmaster_appointment](#BKMK_recurringappointmentmaster_appointment)
- [processstage_appointments](#BKMK_processstage_appointments)
- [activity_pointer_appointment](#BKMK_activity_pointer_appointment)


### <a name="BKMK_KnowledgeBaseRecord_Appointments"></a> KnowledgeBaseRecord_Appointments

See the [KnowledgeBaseRecord_Appointments](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_Appointments) one-to-many relationship for the [knowledgebaserecord](knowledgebaserecord.md) table/entity.

### <a name="BKMK_business_unit_appointment_activities"></a> business_unit_appointment_activities

See the [business_unit_appointment_activities](businessunit.md#BKMK_business_unit_appointment_activities) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_lk_appointment_modifiedby"></a> lk_appointment_modifiedby

See the [lk_appointment_modifiedby](systemuser.md#BKMK_lk_appointment_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_TransactionCurrency_Appointment"></a> TransactionCurrency_Appointment

See the [TransactionCurrency_Appointment](transactioncurrency.md#BKMK_TransactionCurrency_Appointment) one-to-many relationship for the [transactioncurrency](transactioncurrency.md) table/entity.

### <a name="BKMK_lk_appointment_modifiedonbehalfby"></a> lk_appointment_modifiedonbehalfby

See the [lk_appointment_modifiedonbehalfby](systemuser.md#BKMK_lk_appointment_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_appointment_createdby"></a> lk_appointment_createdby

See the [lk_appointment_createdby](systemuser.md#BKMK_lk_appointment_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_sla_appointment"></a> sla_appointment

See the [sla_appointment](sla.md#BKMK_sla_appointment) one-to-many relationship for the [sla](sla.md) table/entity.

### <a name="BKMK_Contact_Appointments"></a> Contact_Appointments

See the [Contact_Appointments](contact.md#BKMK_Contact_Appointments) one-to-many relationship for the [contact](contact.md) table/entity.

### <a name="BKMK_lk_appointment_createdonbehalfby"></a> lk_appointment_createdonbehalfby

See the [lk_appointment_createdonbehalfby](systemuser.md#BKMK_lk_appointment_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_KnowledgeArticle_Appointments"></a> KnowledgeArticle_Appointments

See the [KnowledgeArticle_Appointments](knowledgearticle.md#BKMK_KnowledgeArticle_Appointments) one-to-many relationship for the [knowledgearticle](knowledgearticle.md) table/entity.

### <a name="BKMK_Account_Appointments"></a> Account_Appointments

See the [Account_Appointments](account.md#BKMK_Account_Appointments) one-to-many relationship for the [account](account.md) table/entity.

### <a name="BKMK_manualsla_appointment"></a> manualsla_appointment

See the [manualsla_appointment](sla.md#BKMK_manualsla_appointment) one-to-many relationship for the [sla](sla.md) table/entity.

### <a name="BKMK_team_appointment"></a> team_appointment

See the [team_appointment](team.md#BKMK_team_appointment) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_user_appointment"></a> user_appointment

See the [user_appointment](systemuser.md#BKMK_user_appointment) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_recurringappointmentmaster_appointment"></a> recurringappointmentmaster_appointment

See the [recurringappointmentmaster_appointment](recurringappointmentmaster.md#BKMK_recurringappointmentmaster_appointment) one-to-many relationship for the [recurringappointmentmaster](recurringappointmentmaster.md) table/entity.

### <a name="BKMK_processstage_appointments"></a> processstage_appointments

See the [processstage_appointments](processstage.md#BKMK_processstage_appointments) one-to-many relationship for the [processstage](processstage.md) table/entity.

### <a name="BKMK_activity_pointer_appointment"></a> activity_pointer_appointment

See the [activity_pointer_appointment](activitypointer.md#BKMK_activity_pointer_appointment) one-to-many relationship for the [activitypointer](activitypointer.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.appointment?text=appointment EntityType" />