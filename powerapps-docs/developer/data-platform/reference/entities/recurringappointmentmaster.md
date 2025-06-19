---
title: "Recurring Appointment (RecurringAppointmentMaster) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Recurring Appointment (RecurringAppointmentMaster) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Recurring Appointment (RecurringAppointmentMaster) table/entity reference (Microsoft Dataverse)

The Master appointment of a recurring appointment series.

## Messages

The following table lists the messages for the Recurring Appointment (RecurringAppointmentMaster) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `AddRecurrence`<br />Event: True |<xref:Microsoft.Dynamics.CRM.AddRecurrence?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.AddRecurrenceRequest>|
| `Assign`<br />Event: True |`PATCH` /recurringappointmentmasters(*activityid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Book`<br />Event: True |<xref:Microsoft.Dynamics.CRM.Book?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.BookRequest>|
| `Create`<br />Event: True |`POST` /recurringappointmentmasters<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateInstance`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateInstance?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.CreateInstanceRequest>|
| `Delete`<br />Event: True |`DELETE` /recurringappointmentmasters(*activityid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `DeleteOpenInstances`<br />Event: True |<xref:Microsoft.Dynamics.CRM.DeleteOpenInstances?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.DeleteOpenInstancesRequest>|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Reschedule`<br />Event: True |<xref:Microsoft.Dynamics.CRM.Reschedule?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RescheduleRequest>|
| `Retrieve`<br />Event: True |`GET` /recurringappointmentmasters(*activityid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /recurringappointmentmasters<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /recurringappointmentmasters(*activityid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /recurringappointmentmasters(*activityid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /recurringappointmentmasters(*activityid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Recurring Appointment (RecurringAppointmentMaster) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Recurring Appointment** |
| **DisplayCollectionName** | **Recurring Appointments** |
| **SchemaName** | `RecurringAppointmentMaster` |
| **CollectionSchemaName** | `RecurringAppointmentMasters` |
| **EntitySetName** | `recurringappointmentmasters`|
| **LogicalName** | `recurringappointmentmaster` |
| **LogicalCollectionName** | `recurringappointmentmasters` |
| **PrimaryIdAttribute** | `activityid` |
| **PrimaryNameAttribute** |`subject` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ActivityId](#BKMK_ActivityId)
- [Category](#BKMK_Category)
- [DayOfMonth](#BKMK_DayOfMonth)
- [DaysOfWeekMask](#BKMK_DaysOfWeekMask)
- [Description](#BKMK_Description)
- [Duration](#BKMK_Duration)
- [EffectiveEndDate](#BKMK_EffectiveEndDate)
- [EffectiveStartDate](#BKMK_EffectiveStartDate)
- [EndTime](#BKMK_EndTime)
- [FirstDayOfWeek](#BKMK_FirstDayOfWeek)
- [GlobalObjectId](#BKMK_GlobalObjectId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [Instance](#BKMK_Instance)
- [Interval](#BKMK_Interval)
- [IsAllDayEvent](#BKMK_IsAllDayEvent)
- [IsBilled](#BKMK_IsBilled)
- [IsMapiPrivate](#BKMK_IsMapiPrivate)
- [IsNthMonthly](#BKMK_IsNthMonthly)
- [IsNthYearly](#BKMK_IsNthYearly)
- [IsOnlineMeeting](#BKMK_IsOnlineMeeting)
- [IsRegenerate](#BKMK_IsRegenerate)
- [IsWeekDayPattern](#BKMK_IsWeekDayPattern)
- [IsWorkflowCreated](#BKMK_IsWorkflowCreated)
- [Location](#BKMK_Location)
- [MonthOfYear](#BKMK_MonthOfYear)
- [Occurrences](#BKMK_Occurrences)
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
- [PatternEndDate](#BKMK_PatternEndDate)
- [PatternEndType](#BKMK_PatternEndType)
- [PatternStartDate](#BKMK_PatternStartDate)
- [PriorityCode](#BKMK_PriorityCode)
- [ProcessId](#BKMK_ProcessId)
- [RecurrencePatternType](#BKMK_RecurrencePatternType)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [RequiredAttendees](#BKMK_RequiredAttendees)
- [SeriesStatus](#BKMK_SeriesStatus)
- [SortDate](#BKMK_SortDate)
- [StageId](#BKMK_StageId)
- [StartTime](#BKMK_StartTime)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [Subcategory](#BKMK_Subcategory)
- [Subject](#BKMK_Subject)
- [SubscriptionId](#BKMK_SubscriptionId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [TraversedPath](#BKMK_TraversedPath)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_ActivityId"></a> ActivityId

|Property|Value|
|---|---|
|Description|**Unique identifier of the recurring appointment series.**|
|DisplayName|**Recurring Appointment**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`activityid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Category"></a> Category

|Property|Value|
|---|---|
|Description|**Type a category to identify the recurring appointment type, such as status meeting or service call, to tie the appointment to a business group or function.**|
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

### <a name="BKMK_DayOfMonth"></a> DayOfMonth

|Property|Value|
|---|---|
|Description|**The day of the month on which the recurring appointment occurs.**|
|DisplayName|**Day Of Month**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`dayofmonth`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|31|
|MinValue|1|

### <a name="BKMK_DaysOfWeekMask"></a> DaysOfWeekMask

|Property|Value|
|---|---|
|Description|**Bitmask that represents the days of the week on which the recurring appointment occurs.**|
|DisplayName|**Days Of Week Mask**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`daysofweekmask`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|127|
|MinValue|1|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Type additional information to describe the recurring appointment, such as key talking points or objectives.**|
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

### <a name="BKMK_Duration"></a> Duration

|Property|Value|
|---|---|
|Description|**Duration of the recurring appointment series in minutes.**|
|DisplayName|**Duration**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`duration`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_EffectiveEndDate"></a> EffectiveEndDate

|Property|Value|
|---|---|
|Description|**Actual end date of the recurring appointment series based on the specified end date and recurrence pattern.**|
|DisplayName|**Effective End Date**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`effectiveenddate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_EffectiveStartDate"></a> EffectiveStartDate

|Property|Value|
|---|---|
|Description|**Actual start date of the recurring appointment series based on the specified start date and recurrence pattern.**|
|DisplayName|**Effective Start Date**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`effectivestartdate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_EndTime"></a> EndTime

|Property|Value|
|---|---|
|Description|**End time of the associated activity.**|
|DisplayName|**Pattern End Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`endtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_FirstDayOfWeek"></a> FirstDayOfWeek

|Property|Value|
|---|---|
|Description|**First day of week for the recurrence pattern.**|
|DisplayName|**First Day Of Week**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`firstdayofweek`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|6|
|MinValue|0|

### <a name="BKMK_GlobalObjectId"></a> GlobalObjectId

|Property|Value|
|---|---|
|Description|**Unique Outlook identifier to correlate recurring appointment series across Exchange mailboxes.**|
|DisplayName|**Outlook Recurring Appointment Master**|
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

### <a name="BKMK_Instance"></a> Instance

|Property|Value|
|---|---|
|Description|**Specifies the recurring appointment series to occur on every Nth day of a month. Valid for monthly and yearly recurrence patterns only.**|
|DisplayName|**Instance**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`instance`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`recurringappointmentmaster_instance`|

#### Instance Choices/Options

|Value|Label|
|---|---|
|1|**First**|
|2|**Second**|
|3|**Third**|
|4|**Fourth**|
|5|**Last**|

### <a name="BKMK_Interval"></a> Interval

|Property|Value|
|---|---|
|Description|**Number of units of a given recurrence type between occurrences.**|
|DisplayName|**Interval**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`interval`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000|
|MinValue|1|

### <a name="BKMK_IsAllDayEvent"></a> IsAllDayEvent

|Property|Value|
|---|---|
|Description|**Select whether the recurring appointment is an all-day event to make sure that the required resources are scheduled for the full day.**|
|DisplayName|**All Day Event**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isalldayevent`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`recurringappointmentmaster_isalldayevent`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsBilled"></a> IsBilled

|Property|Value|
|---|---|
|Description|**Indicates whether the recurring appointment series was billed as part of resolving a case.**|
|DisplayName|**Is Billed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isbilled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`recurringappointmentmaster_isbilled`|
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
|GlobalChoiceName|`recurringappointmentmaster_ismapiprivate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsNthMonthly"></a> IsNthMonthly

|Property|Value|
|---|---|
|Description|**Indicates whether the recurring appointment series should occur after every N months. Valid for monthly recurrence pattern only.**|
|DisplayName|**Nth Monthly**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isnthmonthly`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`recurringappointmentmaster_isnthmonthly`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsNthYearly"></a> IsNthYearly

|Property|Value|
|---|---|
|Description|**Indicates whether the recurring appointment series should occur after every N years. Valid for yearly recurrence pattern only.**|
|DisplayName|**Nth Yearly**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isnthyearly`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`recurringappointmentmaster_isnthyearly`|
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

### <a name="BKMK_IsRegenerate"></a> IsRegenerate

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Regenerate**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isregenerate`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`recurringappointmentmaster_isregenerate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsWeekDayPattern"></a> IsWeekDayPattern

|Property|Value|
|---|---|
|Description|**Indicates whether the weekly recurrence pattern is a daily weekday pattern. Valid for weekly recurrence pattern only.**|
|DisplayName|**Every Weekday**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isweekdaypattern`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`recurringappointmentmaster_isweekdaypattern`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsWorkflowCreated"></a> IsWorkflowCreated

|Property|Value|
|---|---|
|Description|**Indicates whether the recurring appointment series was created from a workflow rule.**|
|DisplayName|**Is Workflow Created**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isworkflowcreated`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`recurringappointmentmaster_isworkflowcreated`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Location"></a> Location

|Property|Value|
|---|---|
|Description|**Type the location where the recurring appointment will take place, such as a conference room or customer office.**|
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

### <a name="BKMK_MonthOfYear"></a> MonthOfYear

|Property|Value|
|---|---|
|Description|**Indicates the month of the year for the recurrence pattern.**|
|DisplayName|**Month Of Year**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`monthofyear`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`recurrencerule_monthofyear`|

#### MonthOfYear Choices/Options

|Value|Label|
|---|---|
|0|**Invalid Month Of Year**|
|1|**January**|
|2|**February**|
|3|**March**|
|4|**April**|
|5|**May**|
|6|**June**|
|7|**July**|
|8|**August**|
|9|**September**|
|10|**October**|
|11|**November**|
|12|**December**|

### <a name="BKMK_Occurrences"></a> Occurrences

|Property|Value|
|---|---|
|Description|**Number of appointment occurrences in a recurring appointment series.**|
|DisplayName|**Occurrences**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`occurrences`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|999|
|MinValue|1|

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
|DefaultFormValue|-1|
|GlobalChoiceName|`onlinemeetingtype`|

#### OnlineMeetingType Choices/Options

|Value|Label|
|---|---|
|1|**Teams Meeting**|

### <a name="BKMK_OptionalAttendees"></a> OptionalAttendees

|Property|Value|
|---|---|
|Description|**Enter the account, contact, lead, user, or other equipment resources that are not needed at the recurring appointment, but can optionally attend.**|
|DisplayName|**Optional Attendees**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`optionalattendees`|
|RequiredLevel|None|
|Type|PartyList|
|Targets|account, contact, systemuser|

### <a name="BKMK_Organizer"></a> Organizer

|Property|Value|
|---|---|
|Description|**Enter the user who is in charge of coordinating or leading the recurring appointment to make sure the appointment is displayed in the user's My Activities view.**|
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
|Description|**Unique identifier of the Microsoft Office Outlook recurring appointment series owner that correlates to the PR\_OWNER\_APPT\_ID MAPI property.**|
|DisplayName|**Outlook Recurring Appointment Master Owner**|
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

### <a name="BKMK_PatternEndDate"></a> PatternEndDate

|Property|Value|
|---|---|
|Description|**End date of the recurrence range.**|
|DisplayName|**Recurrence Range End**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`patternenddate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_PatternEndType"></a> PatternEndType

|Property|Value|
|---|---|
|Description|**Select the type of end date for the recurring appointment, such as no end date or the number of occurrences.**|
|DisplayName|**Pattern End Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`patternendtype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`recurringappointmentmaster_patternendtype`|

#### PatternEndType Choices/Options

|Value|Label|
|---|---|
|1|**No End Date**|
|2|**Occurrences**|
|3|**Pattern End Date**|

### <a name="BKMK_PatternStartDate"></a> PatternStartDate

|Property|Value|
|---|---|
|Description|**Start date of the recurrence range.**|
|DisplayName|**Recurrence Range Start**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`patternstartdate`|
|RequiredLevel|ApplicationRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

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
|GlobalChoiceName|`recurringappointmentmaster_prioritycode`|

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

### <a name="BKMK_RecurrencePatternType"></a> RecurrencePatternType

|Property|Value|
|---|---|
|Description|**Select the pattern type for the recurring appointment to indicate whether the appointment occurs daily, weekly, monthly, or yearly.**|
|DisplayName|**Recurrence Frequency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`recurrencepatterntype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`recurringappointmentmaster_recurrencepatterntype`|

#### RecurrencePatternType Choices/Options

|Value|Label|
|---|---|
|0|**Daily**|
|1|**Weekly**|
|2|**Monthly**|
|3|**Yearly**|

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**Choose the record that the recurring appointment series relates to.**|
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

### <a name="BKMK_RequiredAttendees"></a> RequiredAttendees

|Property|Value|
|---|---|
|Description|**Enter the account, contact, lead, user, or other equipment resources that are required to attend the recurring appointment.**|
|DisplayName|**Required Attendees**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`requiredattendees`|
|RequiredLevel|None|
|Type|PartyList|
|Targets|account, contact, systemuser|

### <a name="BKMK_SeriesStatus"></a> SeriesStatus

|Property|Value|
|---|---|
|Description|**Indicates whether the recurring appointment series is active or inactive.**|
|DisplayName|**Series Status**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`seriesstatus`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`recurringappointmentmaster_seriesstatus`|
|DefaultValue|True|
|True Label|Active|
|False Label|Inactive|

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

### <a name="BKMK_StartTime"></a> StartTime

|Property|Value|
|---|---|
|Description|**Start time of the recurring appointment series.**|
|DisplayName|**Pattern Start Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`starttime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Shows whether the recurring appointment is open, scheduled, completed, or canceled. Completed and canceled appointments are read-only and can't be edited.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`recurringappointmentmaster_statecode`|

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
|Description|**Select the recurring appointment's status.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`recurringappointmentmaster_statuscode`|

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
|Description|**Type a subcategory to identify the recurring appointment type and relate the activity to a specific product, sales region, business group, or other function.**|
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
|Description|**Type a short description about the objective or primary topic of the recurring appointment.**|
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
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`subscriptionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
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
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [DeletedExceptionsList](#BKMK_DeletedExceptionsList)
- [ExchangeRate](#BKMK_ExchangeRate)
- [ExpansionStateCode](#BKMK_ExpansionStateCode)
- [GroupId](#BKMK_GroupId)
- [InstanceTypeCode](#BKMK_InstanceTypeCode)
- [IsRegularActivity](#BKMK_IsRegularActivity)
- [IsUnsafe](#BKMK_IsUnsafe)
- [LastExpandedInstanceDate](#BKMK_LastExpandedInstanceDate)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [NextExpansionInstanceDate](#BKMK_NextExpansionInstanceDate)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [RuleId](#BKMK_RuleId)
- [SafeDescription](#BKMK_SafeDescription)
- [ScheduledEnd](#BKMK_ScheduledEnd)
- [ScheduledStart](#BKMK_ScheduledStart)
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

### <a name="BKMK_DeletedExceptionsList"></a> DeletedExceptionsList

|Property|Value|
|---|---|
|Description|**List of deleted instances of the recurring appointment series.**|
|DisplayName|**Deleted Appointments**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`deletedexceptionslist`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

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

### <a name="BKMK_ExpansionStateCode"></a> ExpansionStateCode

|Property|Value|
|---|---|
|Description|**State code to indicate whether the recurring appointment series is expanded fully or partially.**|
|DisplayName|**Expansion State Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`expansionstatecode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`recurringappointmentmaster_expansionstatecode`|

#### ExpansionStateCode Choices/Options

|Value|Label|
|---|---|
|0|**Unexpanded**|
|1|**Partial**|
|2|**Full**|

### <a name="BKMK_GroupId"></a> GroupId

|Property|Value|
|---|---|
|Description|**Unique identifier of the recurring appointment series for which the recurrence information was updated.**|
|DisplayName|**Group Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`groupid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|recurringappointmentmaster|

### <a name="BKMK_InstanceTypeCode"></a> InstanceTypeCode

|Property|Value|
|---|---|
|Description|**Type of instance of a recurring appointment series.**|
|DisplayName|**Appointment Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`instancetypecode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`recurringappointmentmaster_instancetypecode`|

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
|Description|**Indicates whether the activity is a regular activity type or event type.**|
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

### <a name="BKMK_LastExpandedInstanceDate"></a> LastExpandedInstanceDate

|Property|Value|
|---|---|
|Description|**Date of last expanded instance of a recurring appointment series.**|
|DisplayName|**Last Expanded Instance Date**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastexpandedinstancedate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

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

### <a name="BKMK_NextExpansionInstanceDate"></a> NextExpansionInstanceDate

|Property|Value|
|---|---|
|Description|**Date of the next expanded instance of a recurring appointment series.**|
|DisplayName|**Next Expanded Instance Date**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`nextexpansioninstancedate`|
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
|Description|**Unique identifier of the business unit that owns the recurring appointment series.**|
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
|Description|**Unique identifier of the team who owns the recurring appointment series.**|
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
|Description|**Unique identifier of the user who owns the recurring appointment series.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_RuleId"></a> RuleId

|Property|Value|
|---|---|
|Description|**Unique identifier of the recurrence rule that is associated with the recurring appointment series.**|
|DisplayName|**Recurrence Rule**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ruleid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|recurrencerule|

### <a name="BKMK_SafeDescription"></a> SafeDescription

|Property|Value|
|---|---|
|Description|**Safe body text of the recurring appointment.**|
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

### <a name="BKMK_ScheduledEnd"></a> ScheduledEnd

|Property|Value|
|---|---|
|Description|**Scheduled end time of the recurring appointment series.**|
|DisplayName|**End Time**|
|IsValidForForm|False|
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
|Description|**Scheduled start time of the recurring appointment series.**|
|DisplayName|**Start Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`scheduledstart`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [Account_RecurringAppointmentMasters](#BKMK_Account_RecurringAppointmentMasters)
- [activity_pointer_recurringappointmentmaster](#BKMK_activity_pointer_recurringappointmentmaster)
- [adx_invitation_RecurringAppointmentMasters](#BKMK_adx_invitation_RecurringAppointmentMasters)
- [business_unit_recurringappointmentmaster_activities](#BKMK_business_unit_recurringappointmentmaster_activities)
- [Contact_RecurringAppointmentMasters](#BKMK_Contact_RecurringAppointmentMasters)
- [KnowledgeArticle_RecurringAppointmentMasters](#BKMK_KnowledgeArticle_RecurringAppointmentMasters)
- [KnowledgeBaseRecord_RecurringAppointmentMasters](#BKMK_KnowledgeBaseRecord_RecurringAppointmentMasters)
- [lk_recurringappointmentmaster_createdby](#BKMK_lk_recurringappointmentmaster_createdby)
- [lk_recurringappointmentmaster_createdonbehalfby](#BKMK_lk_recurringappointmentmaster_createdonbehalfby)
- [lk_recurringappointmentmaster_modifiedby](#BKMK_lk_recurringappointmentmaster_modifiedby)
- [lk_recurringappointmentmaster_modifiedonbehalfby](#BKMK_lk_recurringappointmentmaster_modifiedonbehalfby)
- [mspp_adplacement_RecurringAppointmentMasters](#BKMK_mspp_adplacement_RecurringAppointmentMasters)
- [mspp_pollplacement_RecurringAppointmentMasters](#BKMK_mspp_pollplacement_RecurringAppointmentMasters)
- [mspp_publishingstatetransitionrule_RecurringAppointmentMasters](#BKMK_mspp_publishingstatetransitionrule_RecurringAppointmentMasters)
- [mspp_redirect_RecurringAppointmentMasters](#BKMK_mspp_redirect_RecurringAppointmentMasters)
- [mspp_shortcut_RecurringAppointmentMasters](#BKMK_mspp_shortcut_RecurringAppointmentMasters)
- [mspp_website_RecurringAppointmentMasters](#BKMK_mspp_website_RecurringAppointmentMasters)
- [owner_recurringappointmentmasters](#BKMK_owner_recurringappointmentmasters)
- [processstage_recurringappointmentmasters](#BKMK_processstage_recurringappointmentmasters)
- [recurrencerule_recurringappointmentmaster](#BKMK_recurrencerule_recurringappointmentmaster)
- [team_recurringappointmentmaster](#BKMK_team_recurringappointmentmaster)
- [TransactionCurrency_RecurringAppointmentMaster](#BKMK_TransactionCurrency_RecurringAppointmentMaster)
- [user_recurringappointmentmaster](#BKMK_user_recurringappointmentmaster)

### <a name="BKMK_Account_RecurringAppointmentMasters"></a> Account_RecurringAppointmentMasters

One-To-Many Relationship: [account Account_RecurringAppointmentMasters](account.md#BKMK_Account_RecurringAppointmentMasters)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_account_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_activity_pointer_recurringappointmentmaster"></a> activity_pointer_recurringappointmentmaster

One-To-Many Relationship: [activitypointer activity_pointer_recurringappointmentmaster](activitypointer.md#BKMK_activity_pointer_recurringappointmentmaster)

|Property|Value|
|---|---|
|ReferencedEntity|`activitypointer`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`activityid`|
|ReferencingEntityNavigationPropertyName|`activityid_activitypointer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_invitation_RecurringAppointmentMasters"></a> adx_invitation_RecurringAppointmentMasters

One-To-Many Relationship: [adx_invitation adx_invitation_RecurringAppointmentMasters](adx_invitation.md#BKMK_adx_invitation_RecurringAppointmentMasters)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_invitation`|
|ReferencedAttribute|`adx_invitationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_invitation_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_business_unit_recurringappointmentmaster_activities"></a> business_unit_recurringappointmentmaster_activities

One-To-Many Relationship: [businessunit business_unit_recurringappointmentmaster_activities](businessunit.md#BKMK_business_unit_recurringappointmentmaster_activities)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Contact_RecurringAppointmentMasters"></a> Contact_RecurringAppointmentMasters

One-To-Many Relationship: [contact Contact_RecurringAppointmentMasters](contact.md#BKMK_Contact_RecurringAppointmentMasters)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_contact_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_KnowledgeArticle_RecurringAppointmentMasters"></a> KnowledgeArticle_RecurringAppointmentMasters

One-To-Many Relationship: [knowledgearticle KnowledgeArticle_RecurringAppointmentMasters](knowledgearticle.md#BKMK_KnowledgeArticle_RecurringAppointmentMasters)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgearticle_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_KnowledgeBaseRecord_RecurringAppointmentMasters"></a> KnowledgeBaseRecord_RecurringAppointmentMasters

One-To-Many Relationship: [knowledgebaserecord KnowledgeBaseRecord_RecurringAppointmentMasters](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_RecurringAppointmentMasters)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgebaserecord`|
|ReferencedAttribute|`knowledgebaserecordid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgebaserecord_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_recurringappointmentmaster_createdby"></a> lk_recurringappointmentmaster_createdby

One-To-Many Relationship: [systemuser lk_recurringappointmentmaster_createdby](systemuser.md#BKMK_lk_recurringappointmentmaster_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_recurringappointmentmaster_createdonbehalfby"></a> lk_recurringappointmentmaster_createdonbehalfby

One-To-Many Relationship: [systemuser lk_recurringappointmentmaster_createdonbehalfby](systemuser.md#BKMK_lk_recurringappointmentmaster_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_recurringappointmentmaster_modifiedby"></a> lk_recurringappointmentmaster_modifiedby

One-To-Many Relationship: [systemuser lk_recurringappointmentmaster_modifiedby](systemuser.md#BKMK_lk_recurringappointmentmaster_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_recurringappointmentmaster_modifiedonbehalfby"></a> lk_recurringappointmentmaster_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_recurringappointmentmaster_modifiedonbehalfby](systemuser.md#BKMK_lk_recurringappointmentmaster_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_adplacement_RecurringAppointmentMasters"></a> mspp_adplacement_RecurringAppointmentMasters

One-To-Many Relationship: [mspp_adplacement mspp_adplacement_RecurringAppointmentMasters](mspp_adplacement.md#BKMK_mspp_adplacement_RecurringAppointmentMasters)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_adplacement`|
|ReferencedAttribute|`mspp_adplacementid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_adplacement_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_pollplacement_RecurringAppointmentMasters"></a> mspp_pollplacement_RecurringAppointmentMasters

One-To-Many Relationship: [mspp_pollplacement mspp_pollplacement_RecurringAppointmentMasters](mspp_pollplacement.md#BKMK_mspp_pollplacement_RecurringAppointmentMasters)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_pollplacement`|
|ReferencedAttribute|`mspp_pollplacementid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_pollplacement_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_publishingstatetransitionrule_RecurringAppointmentMasters"></a> mspp_publishingstatetransitionrule_RecurringAppointmentMasters

One-To-Many Relationship: [mspp_publishingstatetransitionrule mspp_publishingstatetransitionrule_RecurringAppointmentMasters](mspp_publishingstatetransitionrule.md#BKMK_mspp_publishingstatetransitionrule_RecurringAppointmentMasters)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_publishingstatetransitionrule`|
|ReferencedAttribute|`mspp_publishingstatetransitionruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_publishingstatetransitionrule_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_redirect_RecurringAppointmentMasters"></a> mspp_redirect_RecurringAppointmentMasters

One-To-Many Relationship: [mspp_redirect mspp_redirect_RecurringAppointmentMasters](mspp_redirect.md#BKMK_mspp_redirect_RecurringAppointmentMasters)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_redirect`|
|ReferencedAttribute|`mspp_redirectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_redirect_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_shortcut_RecurringAppointmentMasters"></a> mspp_shortcut_RecurringAppointmentMasters

One-To-Many Relationship: [mspp_shortcut mspp_shortcut_RecurringAppointmentMasters](mspp_shortcut.md#BKMK_mspp_shortcut_RecurringAppointmentMasters)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_shortcut`|
|ReferencedAttribute|`mspp_shortcutid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_shortcut_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_website_RecurringAppointmentMasters"></a> mspp_website_RecurringAppointmentMasters

One-To-Many Relationship: [mspp_website mspp_website_RecurringAppointmentMasters](mspp_website.md#BKMK_mspp_website_RecurringAppointmentMasters)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_website`|
|ReferencedAttribute|`mspp_websiteid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_website_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_recurringappointmentmasters"></a> owner_recurringappointmentmasters

One-To-Many Relationship: [owner owner_recurringappointmentmasters](owner.md#BKMK_owner_recurringappointmentmasters)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_processstage_recurringappointmentmasters"></a> processstage_recurringappointmentmasters

One-To-Many Relationship: [processstage processstage_recurringappointmentmasters](processstage.md#BKMK_processstage_recurringappointmentmasters)

|Property|Value|
|---|---|
|ReferencedEntity|`processstage`|
|ReferencedAttribute|`processstageid`|
|ReferencingAttribute|`stageid`|
|ReferencingEntityNavigationPropertyName|`stageid_processstage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recurrencerule_recurringappointmentmaster"></a> recurrencerule_recurringappointmentmaster

One-To-Many Relationship: [recurrencerule recurrencerule_recurringappointmentmaster](recurrencerule.md#BKMK_recurrencerule_recurringappointmentmaster)

|Property|Value|
|---|---|
|ReferencedEntity|`recurrencerule`|
|ReferencedAttribute|`objectid`|
|ReferencingAttribute|`activityid`|
|ReferencingEntityNavigationPropertyName|`activityid_recurrencerule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_recurringappointmentmaster"></a> team_recurringappointmentmaster

One-To-Many Relationship: [team team_recurringappointmentmaster](team.md#BKMK_team_recurringappointmentmaster)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_RecurringAppointmentMaster"></a> TransactionCurrency_RecurringAppointmentMaster

One-To-Many Relationship: [transactioncurrency TransactionCurrency_RecurringAppointmentMaster](transactioncurrency.md#BKMK_TransactionCurrency_RecurringAppointmentMaster)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencingEntityNavigationPropertyName|`transactioncurrencyid_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_recurringappointmentmaster"></a> user_recurringappointmentmaster

One-To-Many Relationship: [systemuser user_recurringappointmentmaster](systemuser.md#BKMK_user_recurringappointmentmaster)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [recurringappointmentmaster_actioncard](#BKMK_recurringappointmentmaster_actioncard)
- [recurringappointmentmaster_activity_parties](#BKMK_recurringappointmentmaster_activity_parties)
- [RecurringAppointmentMaster_Annotation](#BKMK_RecurringAppointmentMaster_Annotation)
- [recurringappointmentmaster_appointment](#BKMK_recurringappointmentmaster_appointment)
- [RecurringAppointmentMaster_AsyncOperations](#BKMK_RecurringAppointmentMaster_AsyncOperations)
- [RecurringAppointmentMaster_BulkDeleteFailures](#BKMK_RecurringAppointmentMaster_BulkDeleteFailures)
- [recurringappointmentmaster_connections1](#BKMK_recurringappointmentmaster_connections1)
- [recurringappointmentmaster_connections2](#BKMK_recurringappointmentmaster_connections2)
- [RecurringAppointmentMaster_DuplicateBaseRecord](#BKMK_RecurringAppointmentMaster_DuplicateBaseRecord)
- [RecurringAppointmentMaster_DuplicateMatchingRecord](#BKMK_RecurringAppointmentMaster_DuplicateMatchingRecord)
- [recurringappointmentmaster_PostFollows](#BKMK_recurringappointmentmaster_PostFollows)
- [recurringappointmentmaster_PostRegardings](#BKMK_recurringappointmentmaster_PostRegardings)
- [recurringappointmentmaster_principalobjectattributeaccess](#BKMK_recurringappointmentmaster_principalobjectattributeaccess)
- [RecurringAppointmentMaster_ProcessSessions](#BKMK_RecurringAppointmentMaster_ProcessSessions)
- [RecurringAppointmentMaster_QueueItem](#BKMK_RecurringAppointmentMaster_QueueItem)
- [RecurringAppointmentMaster_SyncErrors](#BKMK_RecurringAppointmentMaster_SyncErrors)

### <a name="BKMK_recurringappointmentmaster_actioncard"></a> recurringappointmentmaster_actioncard

Many-To-One Relationship: [actioncard recurringappointmentmaster_actioncard](actioncard.md#BKMK_recurringappointmentmaster_actioncard)

|Property|Value|
|---|---|
|ReferencingEntity|`actioncard`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`recurringappointmentmaster_actioncard`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_recurringappointmentmaster_activity_parties"></a> recurringappointmentmaster_activity_parties

Many-To-One Relationship: [activityparty recurringappointmentmaster_activity_parties](activityparty.md#BKMK_recurringappointmentmaster_activity_parties)

|Property|Value|
|---|---|
|ReferencingEntity|`activityparty`|
|ReferencingAttribute|`activityid`|
|ReferencedEntityNavigationPropertyName|`recurringappointmentmaster_activity_parties`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_RecurringAppointmentMaster_Annotation"></a> RecurringAppointmentMaster_Annotation

Many-To-One Relationship: [annotation RecurringAppointmentMaster_Annotation](annotation.md#BKMK_RecurringAppointmentMaster_Annotation)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`RecurringAppointmentMaster_Annotation`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_recurringappointmentmaster_appointment"></a> recurringappointmentmaster_appointment

Many-To-One Relationship: [appointment recurringappointmentmaster_appointment](appointment.md#BKMK_recurringappointmentmaster_appointment)

|Property|Value|
|---|---|
|ReferencingEntity|`appointment`|
|ReferencingAttribute|`seriesid`|
|ReferencedEntityNavigationPropertyName|`recurringappointmentmaster_appointment`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_RecurringAppointmentMaster_AsyncOperations"></a> RecurringAppointmentMaster_AsyncOperations

Many-To-One Relationship: [asyncoperation RecurringAppointmentMaster_AsyncOperations](asyncoperation.md#BKMK_RecurringAppointmentMaster_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`RecurringAppointmentMaster_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_RecurringAppointmentMaster_BulkDeleteFailures"></a> RecurringAppointmentMaster_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure RecurringAppointmentMaster_BulkDeleteFailures](bulkdeletefailure.md#BKMK_RecurringAppointmentMaster_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`RecurringAppointmentMaster_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_recurringappointmentmaster_connections1"></a> recurringappointmentmaster_connections1

Many-To-One Relationship: [connection recurringappointmentmaster_connections1](connection.md#BKMK_recurringappointmentmaster_connections1)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record1id`|
|ReferencedEntityNavigationPropertyName|`recurringappointmentmaster_connections1`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_recurringappointmentmaster_connections2"></a> recurringappointmentmaster_connections2

Many-To-One Relationship: [connection recurringappointmentmaster_connections2](connection.md#BKMK_recurringappointmentmaster_connections2)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record2id`|
|ReferencedEntityNavigationPropertyName|`recurringappointmentmaster_connections2`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_RecurringAppointmentMaster_DuplicateBaseRecord"></a> RecurringAppointmentMaster_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord RecurringAppointmentMaster_DuplicateBaseRecord](duplicaterecord.md#BKMK_RecurringAppointmentMaster_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`RecurringAppointmentMaster_DuplicateBaseRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_RecurringAppointmentMaster_DuplicateMatchingRecord"></a> RecurringAppointmentMaster_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord RecurringAppointmentMaster_DuplicateMatchingRecord](duplicaterecord.md#BKMK_RecurringAppointmentMaster_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`RecurringAppointmentMaster_DuplicateMatchingRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_recurringappointmentmaster_PostFollows"></a> recurringappointmentmaster_PostFollows

Many-To-One Relationship: [postfollow recurringappointmentmaster_PostFollows](postfollow.md#BKMK_recurringappointmentmaster_PostFollows)

|Property|Value|
|---|---|
|ReferencingEntity|`postfollow`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`recurringappointmentmaster_PostFollows`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_recurringappointmentmaster_PostRegardings"></a> recurringappointmentmaster_PostRegardings

Many-To-One Relationship: [postregarding recurringappointmentmaster_PostRegardings](postregarding.md#BKMK_recurringappointmentmaster_PostRegardings)

|Property|Value|
|---|---|
|ReferencingEntity|`postregarding`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`recurringappointmentmaster_PostRegardings`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_recurringappointmentmaster_principalobjectattributeaccess"></a> recurringappointmentmaster_principalobjectattributeaccess

Many-To-One Relationship: [principalobjectattributeaccess recurringappointmentmaster_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_recurringappointmentmaster_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`recurringappointmentmaster_principalobjectattributeaccess`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_RecurringAppointmentMaster_ProcessSessions"></a> RecurringAppointmentMaster_ProcessSessions

Many-To-One Relationship: [processsession RecurringAppointmentMaster_ProcessSessions](processsession.md#BKMK_RecurringAppointmentMaster_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`RecurringAppointmentMaster_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_RecurringAppointmentMaster_QueueItem"></a> RecurringAppointmentMaster_QueueItem

Many-To-One Relationship: [queueitem RecurringAppointmentMaster_QueueItem](queueitem.md#BKMK_RecurringAppointmentMaster_QueueItem)

|Property|Value|
|---|---|
|ReferencingEntity|`queueitem`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`RecurringAppointmentMaster_QueueItem`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_RecurringAppointmentMaster_SyncErrors"></a> RecurringAppointmentMaster_SyncErrors

Many-To-One Relationship: [syncerror RecurringAppointmentMaster_SyncErrors](syncerror.md#BKMK_RecurringAppointmentMaster_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`RecurringAppointmentMaster_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.recurringappointmentmaster?displayProperty=fullName>
