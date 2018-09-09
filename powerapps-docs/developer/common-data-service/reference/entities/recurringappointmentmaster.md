---
title: "RecurringAppointmentMaster Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the RecurringAppointmentMaster entity."
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
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# RecurringAppointmentMaster Entity Reference

The Master appointment of a recurring appointment series.

## Entity Properties

**DisplayName**: Recurring Appointment<br />
**DisplayCollectionName**: Recurring Appointments<br />
**SchemaName**: RecurringAppointmentMaster<br />
**CollectionSchemaName**: RecurringAppointmentMasters<br />
**LogicalName**: recurringappointmentmaster<br />
**LogicalCollectionName**: recurringappointmentmasters<br />
**EntitySetName**: recurringappointmentmasters<br />
**PrimaryIdAttribute**: activityid<br />
**PrimaryNameAttribute**: subject<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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
- [IsRegenerate](#BKMK_IsRegenerate)
- [IsWeekDayPattern](#BKMK_IsWeekDayPattern)
- [IsWorkflowCreated](#BKMK_IsWorkflowCreated)
- [Location](#BKMK_Location)
- [MonthOfYear](#BKMK_MonthOfYear)
- [Occurrences](#BKMK_Occurrences)
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

**Description**: Unique identifier of the recurring appointment series.<br />
**DisplayName**: Recurring Appointment<br />
**LogicalName**: activityid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_Category"></a> Category

**Description**: Type a category to identify the recurring appointment type, such as status meeting or service call, to tie the appointment to a business group or function.<br />
**DisplayName**: Category<br />
**LogicalName**: category<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 250


### <a name="BKMK_DayOfMonth"></a> DayOfMonth

**Description**: The day of the month on which the recurring appointment occurs.<br />
**DisplayName**: Day Of Month<br />
**LogicalName**: dayofmonth<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 31<br />
**MinValue**: 1


### <a name="BKMK_DaysOfWeekMask"></a> DaysOfWeekMask

**Description**: Bitmask that represents the days of the week on which the recurring appointment occurs.<br />
**DisplayName**: Days Of Week Mask<br />
**LogicalName**: daysofweekmask<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 127<br />
**MinValue**: 1


### <a name="BKMK_Description"></a> Description

**Description**: Type additional information to describe the recurring appointment, such as key talking points or objectives.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_Duration"></a> Duration

**Description**: Duration of the recurring appointment series in minutes.<br />
**DisplayName**: Duration<br />
**LogicalName**: duration<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: Duration<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_EffectiveEndDate"></a> EffectiveEndDate

**Description**: Actual end date of the recurring appointment series based on the specified end date and recurrence pattern.<br />
**DisplayName**: Effective End Date<br />
**LogicalName**: effectiveenddate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_EffectiveStartDate"></a> EffectiveStartDate

**Description**: Actual start date of the recurring appointment series based on the specified start date and recurrence pattern.<br />
**DisplayName**: Effective Start Date<br />
**LogicalName**: effectivestartdate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_EndTime"></a> EndTime

**Description**: End time of the associated activity.<br />
**DisplayName**: Pattern End Time<br />
**LogicalName**: endtime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_FirstDayOfWeek"></a> FirstDayOfWeek

**Description**: First day of week for the recurrence pattern.<br />
**DisplayName**: First Day Of Week<br />
**LogicalName**: firstdayofweek<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 6<br />
**MinValue**: 0


### <a name="BKMK_GlobalObjectId"></a> GlobalObjectId

**Description**: Unique Outlook identifier to correlate recurring appointment series across Exchange mailboxes.<br />
**DisplayName**: Outlook Recurring Appointment Master<br />
**LogicalName**: globalobjectid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 300


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


### <a name="BKMK_Instance"></a> Instance

**Description**: Specifies the recurring appointment series to occur on every Nth day of a month. Valid for monthly and yearly recurrence patterns only.<br />
**DisplayName**: Instance<br />
**LogicalName**: instance<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: First
- **Value**: 2 **Label**: Second
- **Value**: 3 **Label**: Third
- **Value**: 4 **Label**: Fourth
- **Value**: 5 **Label**: Last



### <a name="BKMK_Interval"></a> Interval

**Description**: Number of units of a given recurrence type between occurrences.<br />
**DisplayName**: Interval<br />
**LogicalName**: interval<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000<br />
**MinValue**: 1


### <a name="BKMK_IsAllDayEvent"></a> IsAllDayEvent

**Description**: Select whether the recurring appointment is an all-day event to make sure that the required resources are scheduled for the full day.<br />
**DisplayName**: All Day Event<br />
**LogicalName**: isalldayevent<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsBilled"></a> IsBilled

**Description**: Indicates whether the recurring appointment series was billed as part of resolving a case.<br />
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


### <a name="BKMK_IsMapiPrivate"></a> IsMapiPrivate

**Description**: For internal use only.<br />
**DisplayName**: Is Private<br />
**LogicalName**: ismapiprivate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsNthMonthly"></a> IsNthMonthly

**Description**: Indicates whether the recurring appointment series should occur after every N months. Valid for monthly recurrence pattern only.<br />
**DisplayName**: Nth Monthly<br />
**LogicalName**: isnthmonthly<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsNthYearly"></a> IsNthYearly

**Description**: Indicates whether the recurring appointment series should occur after every N years. Valid for yearly recurrence pattern only.<br />
**DisplayName**: Nth Yearly<br />
**LogicalName**: isnthyearly<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsRegenerate"></a> IsRegenerate

**Description**: For internal use only.<br />
**DisplayName**: Regenerate<br />
**LogicalName**: isregenerate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsWeekDayPattern"></a> IsWeekDayPattern

**Description**: Indicates whether the weekly recurrence pattern is a daily weekday pattern. Valid for weekly recurrence pattern only.<br />
**DisplayName**: Every Weekday<br />
**LogicalName**: isweekdaypattern<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsWorkflowCreated"></a> IsWorkflowCreated

**Description**: Indicates whether the recurring appointment series was created from a workflow rule.<br />
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


### <a name="BKMK_Location"></a> Location

**Description**: Type the location where the recurring appointment will take place, such as a conference room or customer office.<br />
**DisplayName**: Location<br />
**LogicalName**: location<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_MonthOfYear"></a> MonthOfYear

**Description**: Indicates the month of the year for the recurrence pattern.<br />
**DisplayName**: Month Of Year<br />
**LogicalName**: monthofyear<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Invalid Month Of Year
- **Value**: 1 **Label**: January
- **Value**: 2 **Label**: February
- **Value**: 3 **Label**: March
- **Value**: 4 **Label**: April
- **Value**: 5 **Label**: May
- **Value**: 6 **Label**: June
- **Value**: 7 **Label**: July
- **Value**: 8 **Label**: August
- **Value**: 9 **Label**: September
- **Value**: 10 **Label**: October
- **Value**: 11 **Label**: November
- **Value**: 12 **Label**: December



### <a name="BKMK_Occurrences"></a> Occurrences

**Description**: Number of appointment occurrences in a recurring appointment series.<br />
**DisplayName**: Occurrences<br />
**LogicalName**: occurrences<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 999<br />
**MinValue**: 1


### <a name="BKMK_OptionalAttendees"></a> OptionalAttendees

**Description**: Enter the account, contact, lead, user, or other equipment resources that are not needed at the recurring appointment, but can optionally attend.<br />
**DisplayName**: Optional Attendees<br />
**LogicalName**: optionalattendees<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: PartyList<br />
**Targets**: account,contact,systemuser


### <a name="BKMK_Organizer"></a> Organizer

**Description**: Enter the user who is in charge of coordinating or leading the recurring appointment to make sure the appointment is displayed in the user's My Activities view.<br />
**DisplayName**: Organizer<br />
**LogicalName**: organizer<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: PartyList<br />
**Targets**: systemuser


### <a name="BKMK_OutlookOwnerApptId"></a> OutlookOwnerApptId

**Description**: Unique identifier of the Microsoft Office Outlook recurring appointment series owner that correlates to the PR_OWNER_APPT_ID MAPI property.<br />
**DisplayName**: Outlook Recurring Appointment Master Owner<br />
**LogicalName**: outlookownerapptid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


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


### <a name="BKMK_PatternEndDate"></a> PatternEndDate

**Description**: End date of the recurrence range.<br />
**DisplayName**: Recurrence Range End<br />
**LogicalName**: patternenddate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_PatternEndType"></a> PatternEndType

**Description**: Select the type of end date for the recurring appointment, such as no end date or the number of occurrences.<br />
**DisplayName**: Pattern End Type<br />
**LogicalName**: patternendtype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: No End Date
- **Value**: 2 **Label**: Occurrences
- **Value**: 3 **Label**: Pattern End Date



### <a name="BKMK_PatternStartDate"></a> PatternStartDate

**Description**: Start date of the recurrence range.<br />
**DisplayName**: Recurrence Range Start<br />
**LogicalName**: patternstartdate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


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


### <a name="BKMK_RecurrencePatternType"></a> RecurrencePatternType

**Description**: Select the pattern type for the recurring appointment to indicate whether the appointment occurs daily, weekly, monthly, or yearly.<br />
**DisplayName**: Recurrence Frequency<br />
**LogicalName**: recurrencepatterntype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Daily
- **Value**: 1 **Label**: Weekly
- **Value**: 2 **Label**: Monthly
- **Value**: 3 **Label**: Yearly



### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

**Description**: Choose the record that the recurring appointment series relates to.<br />
**DisplayName**: Regarding<br />
**LogicalName**: regardingobjectid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: account,contact,knowledgearticle,knowledgebaserecord


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_RequiredAttendees"></a> RequiredAttendees

**Description**: Enter the account, contact, lead, user, or other equipment resources that are required to attend the recurring appointment.<br />
**DisplayName**: Required Attendees<br />
**LogicalName**: requiredattendees<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: PartyList<br />
**Targets**: account,contact,systemuser


### <a name="BKMK_SeriesStatus"></a> SeriesStatus

**Description**: Indicates whether the recurring appointment series is active or inactive.<br />
**DisplayName**: Series Status<br />
**LogicalName**: seriesstatus<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Active
- **FalseOption Value**: 0 **Label**: Inactive

**DefaultValue**: True


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


### <a name="BKMK_StartTime"></a> StartTime

**Description**: Start time of the recurring appointment series.<br />
**DisplayName**: Pattern Start Time<br />
**LogicalName**: starttime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_StateCode"></a> StateCode

**Description**: Shows whether the recurring appointment is open, scheduled, completed, or canceled. Completed and canceled appointments are read-only and can't be edited.<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Open **DefaultStatus**: 1 **InvariantName**: Open
- **Value**: 1 **Label**: Completed **DefaultStatus**: 3 **InvariantName**: Completed
- **Value**: 2 **Label**: Canceled **DefaultStatus**: 4 **InvariantName**: Canceled
- **Value**: 3 **Label**: Scheduled **DefaultStatus**: 5 **InvariantName**: Scheduled



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Select the recurring appointment's status.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Status<br />
**Options**:

- **Value**: 1 **Label**: Free **State**: 0
- **Value**: 2 **Label**: Tentative **State**: 0
- **Value**: 3 **Label**: Completed **State**: 1
- **Value**: 4 **Label**: Canceled **State**: 2
- **Value**: 5 **Label**: Busy **State**: 3
- **Value**: 6 **Label**: Out of Office **State**: 3



### <a name="BKMK_Subcategory"></a> Subcategory

**Description**: Type a subcategory to identify the recurring appointment type and relate the activity to a specific product, sales region, business group, or other function.<br />
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

**Description**: Type a short description about the objective or primary topic of the recurring appointment.<br />
**DisplayName**: Subject<br />
**LogicalName**: subject<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_SubscriptionId"></a> SubscriptionId

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: subscriptionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: timezoneruleversionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


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
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [DeletedExceptionsList](#BKMK_DeletedExceptionsList)
- [ExchangeRate](#BKMK_ExchangeRate)
- [ExpansionStateCode](#BKMK_ExpansionStateCode)
- [GroupId](#BKMK_GroupId)
- [InstanceTypeCode](#BKMK_InstanceTypeCode)
- [IsRegularActivity](#BKMK_IsRegularActivity)
- [LastExpandedInstanceDate](#BKMK_LastExpandedInstanceDate)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [NextExpansionInstanceDate](#BKMK_NextExpansionInstanceDate)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectIdYomiName](#BKMK_RegardingObjectIdYomiName)
- [RuleId](#BKMK_RuleId)
- [ScheduledEnd](#BKMK_ScheduledEnd)
- [ScheduledStart](#BKMK_ScheduledStart)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ActivityTypeCode"></a> ActivityTypeCode

**Description**: Type of activity.<br />
**DisplayName**: Activity Type<br />
**LogicalName**: activitytypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


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


### <a name="BKMK_DeletedExceptionsList"></a> DeletedExceptionsList

**Description**: List of deleted instances of the recurring appointment series.<br />
**DisplayName**: Deleted Appointments<br />
**LogicalName**: deletedexceptionslist<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


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


### <a name="BKMK_ExpansionStateCode"></a> ExpansionStateCode

**Description**: State code to indicate whether the recurring appointment series is expanded fully or partially.<br />
**DisplayName**: Expansion State Code<br />
**LogicalName**: expansionstatecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Unexpanded
- **Value**: 1 **Label**: Partial
- **Value**: 2 **Label**: Full



### <a name="BKMK_GroupId"></a> GroupId

**Description**: Unique identifier of the recurring appointment series for which the recurrence information was updated. <br />
**DisplayName**: Group Id<br />
**LogicalName**: groupid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: recurringappointmentmaster


### <a name="BKMK_InstanceTypeCode"></a> InstanceTypeCode

**Description**: Type of instance of a recurring appointment series.<br />
**DisplayName**: Appointment Type<br />
**LogicalName**: instancetypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Not Recurring
- **Value**: 1 **Label**: Recurring Master
- **Value**: 2 **Label**: Recurring Instance
- **Value**: 3 **Label**: Recurring Exception
- **Value**: 4 **Label**: Recurring Future Exception



### <a name="BKMK_IsRegularActivity"></a> IsRegularActivity

**Description**: Indicates whether the activity is a regular activity type or event type.<br />
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


### <a name="BKMK_LastExpandedInstanceDate"></a> LastExpandedInstanceDate

**Description**: Date of last expanded instance of a recurring appointment series.<br />
**DisplayName**: Last Expanded Instance Date<br />
**LogicalName**: lastexpandedinstancedate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


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


### <a name="BKMK_NextExpansionInstanceDate"></a> NextExpansionInstanceDate

**Description**: Date of the next expanded instance of a recurring appointment series.<br />
**DisplayName**: Next Expanded Instance Date<br />
**LogicalName**: nextexpansioninstancedate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


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

**Description**: Unique identifier of the business unit that owns the recurring appointment series.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier of the team who owns the recurring appointment series.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns the recurring appointment series.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


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


### <a name="BKMK_RuleId"></a> RuleId

**Description**: Unique identifier of the recurrence rule that is associated with the recurring appointment series.<br />
**DisplayName**: Recurrence Rule<br />
**LogicalName**: ruleid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: recurrencerule


### <a name="BKMK_ScheduledEnd"></a> ScheduledEnd

**Description**: Scheduled end time of the recurring appointment series.<br />
**DisplayName**: End Time<br />
**LogicalName**: scheduledend<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ScheduledStart"></a> ScheduledStart

**Description**: Scheduled start time of the recurring appointment series.<br />
**DisplayName**: Start Time<br />
**LogicalName**: scheduledstart<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


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

**Description**: <br />
**DisplayName**: <br />
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

- [recurringappointmentmaster_PostFollows](#BKMK_recurringappointmentmaster_PostFollows)
- [RecurringAppointmentMaster_SyncErrors](#BKMK_RecurringAppointmentMaster_SyncErrors)
- [RecurringAppointmentMaster_DuplicateBaseRecord](#BKMK_RecurringAppointmentMaster_DuplicateBaseRecord)
- [recurringappointmentmaster_actioncard](#BKMK_recurringappointmentmaster_actioncard)
- [RecurringAppointmentMaster_BulkDeleteFailures](#BKMK_RecurringAppointmentMaster_BulkDeleteFailures)
- [RecurringAppointmentMaster_QueueItem](#BKMK_RecurringAppointmentMaster_QueueItem)
- [RecurringAppointmentMaster_AsyncOperations](#BKMK_RecurringAppointmentMaster_AsyncOperations)
- [userentityinstancedata_recurringappointmentmaster](#BKMK_userentityinstancedata_recurringappointmentmaster)
- [recurringappointmentmaster_activity_parties](#BKMK_recurringappointmentmaster_activity_parties)
- [recurringappointmentmaster_connections2](#BKMK_recurringappointmentmaster_connections2)
- [recurringappointmentmaster_connections1](#BKMK_recurringappointmentmaster_connections1)
- [recurringappointmentmaster_principalobjectattributeaccess](#BKMK_recurringappointmentmaster_principalobjectattributeaccess)
- [recurringappointmentmaster_appointment](#BKMK_recurringappointmentmaster_appointment)
- [RecurringAppointmentMaster_ProcessSessions](#BKMK_RecurringAppointmentMaster_ProcessSessions)
- [RecurringAppointmentMaster_Annotation](#BKMK_RecurringAppointmentMaster_Annotation)
- [RecurringAppointmentMaster_DuplicateMatchingRecord](#BKMK_RecurringAppointmentMaster_DuplicateMatchingRecord)


### <a name="BKMK_recurringappointmentmaster_PostFollows"></a> recurringappointmentmaster_PostFollows

Same as postfollow entity [recurringappointmentmaster_PostFollows](postfollow.md#BKMK_recurringappointmentmaster_PostFollows) Many-To-One relationship.

**ReferencingEntity**: postfollow<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: recurringappointmentmaster_PostFollows<br />
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


### <a name="BKMK_RecurringAppointmentMaster_SyncErrors"></a> RecurringAppointmentMaster_SyncErrors

Same as syncerror entity [RecurringAppointmentMaster_SyncErrors](syncerror.md#BKMK_RecurringAppointmentMaster_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: RecurringAppointmentMaster_SyncErrors<br />
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


### <a name="BKMK_RecurringAppointmentMaster_DuplicateBaseRecord"></a> RecurringAppointmentMaster_DuplicateBaseRecord

Same as duplicaterecord entity [RecurringAppointmentMaster_DuplicateBaseRecord](duplicaterecord.md#BKMK_RecurringAppointmentMaster_DuplicateBaseRecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: baserecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: RecurringAppointmentMaster_DuplicateBaseRecord<br />
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


### <a name="BKMK_recurringappointmentmaster_actioncard"></a> recurringappointmentmaster_actioncard

Same as actioncard entity [recurringappointmentmaster_actioncard](actioncard.md#BKMK_recurringappointmentmaster_actioncard) Many-To-One relationship.

**ReferencingEntity**: actioncard<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: recurringappointmentmaster_actioncard<br />
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


### <a name="BKMK_RecurringAppointmentMaster_BulkDeleteFailures"></a> RecurringAppointmentMaster_BulkDeleteFailures

Same as bulkdeletefailure entity [RecurringAppointmentMaster_BulkDeleteFailures](bulkdeletefailure.md#BKMK_RecurringAppointmentMaster_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: RecurringAppointmentMaster_BulkDeleteFailures<br />
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


### <a name="BKMK_RecurringAppointmentMaster_QueueItem"></a> RecurringAppointmentMaster_QueueItem

Same as queueitem entity [RecurringAppointmentMaster_QueueItem](queueitem.md#BKMK_RecurringAppointmentMaster_QueueItem) Many-To-One relationship.

**ReferencingEntity**: queueitem<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: RecurringAppointmentMaster_QueueItem<br />
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


### <a name="BKMK_RecurringAppointmentMaster_AsyncOperations"></a> RecurringAppointmentMaster_AsyncOperations

Same as asyncoperation entity [RecurringAppointmentMaster_AsyncOperations](asyncoperation.md#BKMK_RecurringAppointmentMaster_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: RecurringAppointmentMaster_AsyncOperations<br />
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


### <a name="BKMK_userentityinstancedata_recurringappointmentmaster"></a> userentityinstancedata_recurringappointmentmaster

Same as userentityinstancedata entity [userentityinstancedata_recurringappointmentmaster](userentityinstancedata.md#BKMK_userentityinstancedata_recurringappointmentmaster) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_recurringappointmentmaster<br />
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


### <a name="BKMK_recurringappointmentmaster_activity_parties"></a> recurringappointmentmaster_activity_parties

Same as activityparty entity [recurringappointmentmaster_activity_parties](activityparty.md#BKMK_recurringappointmentmaster_activity_parties) Many-To-One relationship.

**ReferencingEntity**: activityparty<br />
**ReferencingAttribute**: activityid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: recurringappointmentmaster_activity_parties<br />
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


### <a name="BKMK_recurringappointmentmaster_connections2"></a> recurringappointmentmaster_connections2

Same as connection entity [recurringappointmentmaster_connections2](connection.md#BKMK_recurringappointmentmaster_connections2) Many-To-One relationship.

**ReferencingEntity**: connection<br />
**ReferencingAttribute**: record2id<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: recurringappointmentmaster_connections2<br />
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


### <a name="BKMK_recurringappointmentmaster_connections1"></a> recurringappointmentmaster_connections1

Same as connection entity [recurringappointmentmaster_connections1](connection.md#BKMK_recurringappointmentmaster_connections1) Many-To-One relationship.

**ReferencingEntity**: connection<br />
**ReferencingAttribute**: record1id<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: recurringappointmentmaster_connections1<br />
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


### <a name="BKMK_recurringappointmentmaster_principalobjectattributeaccess"></a> recurringappointmentmaster_principalobjectattributeaccess

Same as principalobjectattributeaccess entity [recurringappointmentmaster_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_recurringappointmentmaster_principalobjectattributeaccess) Many-To-One relationship.

**ReferencingEntity**: principalobjectattributeaccess<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: recurringappointmentmaster_principalobjectattributeaccess<br />
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


### <a name="BKMK_recurringappointmentmaster_appointment"></a> recurringappointmentmaster_appointment

Same as appointment entity [recurringappointmentmaster_appointment](appointment.md#BKMK_recurringappointmentmaster_appointment) Many-To-One relationship.

**ReferencingEntity**: appointment<br />
**ReferencingAttribute**: seriesid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: recurringappointmentmaster_appointment<br />
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


### <a name="BKMK_RecurringAppointmentMaster_ProcessSessions"></a> RecurringAppointmentMaster_ProcessSessions

Same as processsession entity [RecurringAppointmentMaster_ProcessSessions](processsession.md#BKMK_RecurringAppointmentMaster_ProcessSessions) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: RecurringAppointmentMaster_ProcessSessions<br />
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


### <a name="BKMK_RecurringAppointmentMaster_Annotation"></a> RecurringAppointmentMaster_Annotation

Same as annotation entity [RecurringAppointmentMaster_Annotation](annotation.md#BKMK_RecurringAppointmentMaster_Annotation) Many-To-One relationship.

**ReferencingEntity**: annotation<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: RecurringAppointmentMaster_Annotation<br />
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


### <a name="BKMK_RecurringAppointmentMaster_DuplicateMatchingRecord"></a> RecurringAppointmentMaster_DuplicateMatchingRecord

Same as duplicaterecord entity [RecurringAppointmentMaster_DuplicateMatchingRecord](duplicaterecord.md#BKMK_RecurringAppointmentMaster_DuplicateMatchingRecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: duplicaterecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: RecurringAppointmentMaster_DuplicateMatchingRecord<br />
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

- [KnowledgeBaseRecord_RecurringAppointmentMasters](#BKMK_KnowledgeBaseRecord_RecurringAppointmentMasters)
- [TransactionCurrency_RecurringAppointmentMaster](#BKMK_TransactionCurrency_RecurringAppointmentMaster)
- [lk_recurringappointmentmaster_modifiedby](#BKMK_lk_recurringappointmentmaster_modifiedby)
- [activity_pointer_recurringappointmentmaster](#BKMK_activity_pointer_recurringappointmentmaster)
- [recurrencerule_recurringappointmentmaster](#BKMK_recurrencerule_recurringappointmentmaster)
- [team_recurringappointmentmaster](#BKMK_team_recurringappointmentmaster)
- [Contact_RecurringAppointmentMasters](#BKMK_Contact_RecurringAppointmentMasters)
- [processstage_recurringappointmentmasters](#BKMK_processstage_recurringappointmentmasters)
- [business_unit_recurringappointmentmaster_activities](#BKMK_business_unit_recurringappointmentmaster_activities)
- [lk_recurringappointmentmaster_createdonbehalfby](#BKMK_lk_recurringappointmentmaster_createdonbehalfby)
- [lk_recurringappointmentmaster_createdby](#BKMK_lk_recurringappointmentmaster_createdby)
- [Account_RecurringAppointmentMasters](#BKMK_Account_RecurringAppointmentMasters)
- [lk_recurringappointmentmaster_modifiedonbehalfby](#BKMK_lk_recurringappointmentmaster_modifiedonbehalfby)
- [user_recurringappointmentmaster](#BKMK_user_recurringappointmentmaster)
- [KnowledgeArticle_RecurringAppointmentMasters](#BKMK_KnowledgeArticle_RecurringAppointmentMasters)


### <a name="BKMK_KnowledgeBaseRecord_RecurringAppointmentMasters"></a> KnowledgeBaseRecord_RecurringAppointmentMasters

See knowledgebaserecord Entity [KnowledgeBaseRecord_RecurringAppointmentMasters](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_RecurringAppointmentMasters) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_RecurringAppointmentMaster"></a> TransactionCurrency_RecurringAppointmentMaster

See transactioncurrency Entity [TransactionCurrency_RecurringAppointmentMaster](transactioncurrency.md#BKMK_TransactionCurrency_RecurringAppointmentMaster) One-To-Many relationship.

### <a name="BKMK_lk_recurringappointmentmaster_modifiedby"></a> lk_recurringappointmentmaster_modifiedby

See systemuser Entity [lk_recurringappointmentmaster_modifiedby](systemuser.md#BKMK_lk_recurringappointmentmaster_modifiedby) One-To-Many relationship.

### <a name="BKMK_activity_pointer_recurringappointmentmaster"></a> activity_pointer_recurringappointmentmaster

See activitypointer Entity [activity_pointer_recurringappointmentmaster](activitypointer.md#BKMK_activity_pointer_recurringappointmentmaster) One-To-Many relationship.

### <a name="BKMK_recurrencerule_recurringappointmentmaster"></a> recurrencerule_recurringappointmentmaster

See recurrencerule Entity [recurrencerule_recurringappointmentmaster](recurrencerule.md#BKMK_recurrencerule_recurringappointmentmaster) One-To-Many relationship.

### <a name="BKMK_team_recurringappointmentmaster"></a> team_recurringappointmentmaster

See team Entity [team_recurringappointmentmaster](team.md#BKMK_team_recurringappointmentmaster) One-To-Many relationship.

### <a name="BKMK_Contact_RecurringAppointmentMasters"></a> Contact_RecurringAppointmentMasters

See contact Entity [Contact_RecurringAppointmentMasters](contact.md#BKMK_Contact_RecurringAppointmentMasters) One-To-Many relationship.

### <a name="BKMK_processstage_recurringappointmentmasters"></a> processstage_recurringappointmentmasters

See processstage Entity [processstage_recurringappointmentmasters](processstage.md#BKMK_processstage_recurringappointmentmasters) One-To-Many relationship.

### <a name="BKMK_business_unit_recurringappointmentmaster_activities"></a> business_unit_recurringappointmentmaster_activities

See businessunit Entity [business_unit_recurringappointmentmaster_activities](businessunit.md#BKMK_business_unit_recurringappointmentmaster_activities) One-To-Many relationship.

### <a name="BKMK_lk_recurringappointmentmaster_createdonbehalfby"></a> lk_recurringappointmentmaster_createdonbehalfby

See systemuser Entity [lk_recurringappointmentmaster_createdonbehalfby](systemuser.md#BKMK_lk_recurringappointmentmaster_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_recurringappointmentmaster_createdby"></a> lk_recurringappointmentmaster_createdby

See systemuser Entity [lk_recurringappointmentmaster_createdby](systemuser.md#BKMK_lk_recurringappointmentmaster_createdby) One-To-Many relationship.

### <a name="BKMK_Account_RecurringAppointmentMasters"></a> Account_RecurringAppointmentMasters

See account Entity [Account_RecurringAppointmentMasters](account.md#BKMK_Account_RecurringAppointmentMasters) One-To-Many relationship.

### <a name="BKMK_lk_recurringappointmentmaster_modifiedonbehalfby"></a> lk_recurringappointmentmaster_modifiedonbehalfby

See systemuser Entity [lk_recurringappointmentmaster_modifiedonbehalfby](systemuser.md#BKMK_lk_recurringappointmentmaster_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_user_recurringappointmentmaster"></a> user_recurringappointmentmaster

See systemuser Entity [user_recurringappointmentmaster](systemuser.md#BKMK_user_recurringappointmentmaster) One-To-Many relationship.

### <a name="BKMK_KnowledgeArticle_RecurringAppointmentMasters"></a> KnowledgeArticle_RecurringAppointmentMasters

See knowledgearticle Entity [KnowledgeArticle_RecurringAppointmentMasters](knowledgearticle.md#BKMK_KnowledgeArticle_RecurringAppointmentMasters) One-To-Many relationship.
recurringappointmentmaster

