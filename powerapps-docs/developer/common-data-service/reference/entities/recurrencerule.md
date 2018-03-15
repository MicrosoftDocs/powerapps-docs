---
title: "RecurrenceRule Entity Reference (Common Data Service for Apps)| MicrosoftDocs"
description: "Includes schema information and supported messages for the RecurrenceRule entity."

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
# RecurrenceRule Entity Reference

Recurrence Rule represents the pattern of incidence of recurring entities.

## Entity Properties

**DisplayName**: Recurrence Rule<br />
**DisplayCollectionName**: Recurrence Rules<br />
**SchemaName**: RecurrenceRule<br />
**CollectionSchemaName**: RecurrenceRules<br />
**LogicalName**: recurrencerule<br />
**LogicalCollectionName**: recurrencerules<br />
**EntitySetName**: recurrencerules<br />
**PrimaryIdAttribute**: ruleid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [DayOfMonth](#BKMK_DayOfMonth)
- [DaysOfWeekMask](#BKMK_DaysOfWeekMask)
- [Duration](#BKMK_Duration)
- [EffectiveEndDate](#BKMK_EffectiveEndDate)
- [EffectiveStartDate](#BKMK_EffectiveStartDate)
- [EndTime](#BKMK_EndTime)
- [FirstDayOfWeek](#BKMK_FirstDayOfWeek)
- [Instance](#BKMK_Instance)
- [Interval](#BKMK_Interval)
- [IsNthMonthly](#BKMK_IsNthMonthly)
- [IsNthYearly](#BKMK_IsNthYearly)
- [IsRegenerate](#BKMK_IsRegenerate)
- [IsWeekDayPattern](#BKMK_IsWeekDayPattern)
- [MonthOfYear](#BKMK_MonthOfYear)
- [ObjectId](#BKMK_ObjectId)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [Occurrences](#BKMK_Occurrences)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [PatternEndDate](#BKMK_PatternEndDate)
- [PatternEndType](#BKMK_PatternEndType)
- [PatternStartDate](#BKMK_PatternStartDate)
- [RecurrencePatternType](#BKMK_RecurrencePatternType)
- [RuleId](#BKMK_RuleId)
- [StartTime](#BKMK_StartTime)


### <a name="BKMK_DayOfMonth"></a> DayOfMonth

**Description**: The day of the month on which the recurring appointment or task occurs.<br />
**DisplayName**: Day Of Month<br />
**LogicalName**: dayofmonth<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 31<br />
**MinValue**: 0


### <a name="BKMK_DaysOfWeekMask"></a> DaysOfWeekMask

**Description**: Bitmask representing the days of the week on which the recurring appointment or task occurs.<br />
**DisplayName**: Days Of Week Mask<br />
**LogicalName**: daysofweekmask<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 127<br />
**MinValue**: 1


### <a name="BKMK_Duration"></a> Duration

**Description**: Duration of the recurrence pattern in minutes.<br />
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

**Description**: The actual end date for expansion of the recurrence pattern.<br />
**DisplayName**: Effective End Date<br />
**LogicalName**: effectiveenddate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_EffectiveStartDate"></a> EffectiveStartDate

**Description**: The actual start date for expansion of the recurrence pattern.<br />
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
**DisplayName**: End Time<br />
**LogicalName**: endtime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_FirstDayOfWeek"></a> FirstDayOfWeek

**Description**: First day Of week for the recurrence pattern.<br />
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


### <a name="BKMK_Instance"></a> Instance

**Description**: Specifies the count for which the recurrence pattern is valid for a given interval.<br />
**DisplayName**: Instance<br />
**LogicalName**: instance<br />
**IsValidForForm**: True<br />
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


### <a name="BKMK_IsNthMonthly"></a> IsNthMonthly

**Description**: Specifies whether the monthly recurrence pattern is Nth monthly, valid only for monthly recurrence.<br />
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

**Description**: Specifies whether the yearly recurrence pattern is Nth yearly, valid only for yearly recurrence.<br />
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

**Description**: Valid only for task type recurrence,indicates whether task should be regenerated.<br />
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

**Description**: Specifies whether the weekly recurrence pattern is actually a daily every weekday pattern, valid only for weekly recurrence.<br />
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


### <a name="BKMK_MonthOfYear"></a> MonthOfYear

**Description**: Specifies the month of the year valid for the recurrence pattern.<br />
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



### <a name="BKMK_ObjectId"></a> ObjectId

**Description**: Unique identifier of the object with which the recurrence rule is associated.<br />
**DisplayName**: Regarding<br />
**LogicalName**: objectid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: activitypointer


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

**Description**: <br />
**DisplayName**: Object Type <br />
**LogicalName**: objecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_Occurrences"></a> Occurrences

**Description**: Number of occurrences of the recurrence pattern.<br />
**DisplayName**: Occurrences<br />
**LogicalName**: occurrences<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 999<br />
**MinValue**: 1


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Unique identifier of the user or team who owns the recurrence rule.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_PatternEndDate"></a> PatternEndDate

**Description**: End date of the Recurrence Range.<br />
**DisplayName**: Recurrence Range End<br />
**LogicalName**: patternenddate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_PatternEndType"></a> PatternEndType

**Description**: Pattern End Type of a recurring series.<br />
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

**Description**: Start date of the Recurrence Range.<br />
**DisplayName**: Recurrence Range Start<br />
**LogicalName**: patternstartdate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_RecurrencePatternType"></a> RecurrencePatternType

**Description**: Type of Recurrence.<br />
**DisplayName**: Recurrence Pattern<br />
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



### <a name="BKMK_RuleId"></a> RuleId

**Description**: Unique identifier of the entity associated with recurrence rule.<br />
**DisplayName**: Recurrence Rule<br />
**LogicalName**: ruleid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_StartTime"></a> StartTime

**Description**: Start time of the recurring activity.<br />
**DisplayName**: Start Time<br />
**LogicalName**: starttime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the recurrence rule.<br />
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

**Description**: Date and time when the recurrence rule was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the recurrence rule.<br />
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


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the recurrence rule.<br />
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

**Description**: Date and time when the recurrence rule was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who modified the recurrence rule.<br />
**DisplayName**: Created By (Delegate)<br />
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

**Description**: Unique identifier of the business unit that owns the recurrence rule.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: <br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: <br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


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


### <a name="BKMK_recurrencerule_recurringappointmentmaster"></a> recurrencerule_recurringappointmentmaster

Same as recurringappointmentmaster entity [recurrencerule_recurringappointmentmaster](recurringappointmentmaster.md#BKMK_recurrencerule_recurringappointmentmaster) Many-To-One relationship.

**ReferencingEntity**: recurringappointmentmaster<br />
**ReferencingAttribute**: activityid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: recurrencerule_recurringappointmentmaster<br />
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [business_unit_recurrencerule](#BKMK_business_unit_recurrencerule)
- [activity_pointer_recurrencerule](#BKMK_activity_pointer_recurrencerule)
- [lk_recurrencerule_modifiedby](#BKMK_lk_recurrencerule_modifiedby)
- [lk_recurrencerule_createdby](#BKMK_lk_recurrencerule_createdby)
- [lk_recurrencerulebase_createdonbehalfby](#BKMK_lk_recurrencerulebase_createdonbehalfby)
- [lk_recurrencerulebase_modifiedonbehalfby](#BKMK_lk_recurrencerulebase_modifiedonbehalfby)


### <a name="BKMK_business_unit_recurrencerule"></a> business_unit_recurrencerule

See businessunit Entity [business_unit_recurrencerule](businessunit.md#BKMK_business_unit_recurrencerule) One-To-Many relationship.

### <a name="BKMK_activity_pointer_recurrencerule"></a> activity_pointer_recurrencerule

See activitypointer Entity [activity_pointer_recurrencerule](activitypointer.md#BKMK_activity_pointer_recurrencerule) One-To-Many relationship.

### <a name="BKMK_lk_recurrencerule_modifiedby"></a> lk_recurrencerule_modifiedby

See systemuser Entity [lk_recurrencerule_modifiedby](systemuser.md#BKMK_lk_recurrencerule_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_recurrencerule_createdby"></a> lk_recurrencerule_createdby

See systemuser Entity [lk_recurrencerule_createdby](systemuser.md#BKMK_lk_recurrencerule_createdby) One-To-Many relationship.

### <a name="BKMK_lk_recurrencerulebase_createdonbehalfby"></a> lk_recurrencerulebase_createdonbehalfby

See systemuser Entity [lk_recurrencerulebase_createdonbehalfby](systemuser.md#BKMK_lk_recurrencerulebase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_recurrencerulebase_modifiedonbehalfby"></a> lk_recurrencerulebase_modifiedonbehalfby

See systemuser Entity [lk_recurrencerulebase_modifiedonbehalfby](systemuser.md#BKMK_lk_recurrencerulebase_modifiedonbehalfby) One-To-Many relationship.
recurrencerule

