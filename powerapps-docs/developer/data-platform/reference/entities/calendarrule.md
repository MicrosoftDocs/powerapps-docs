---
title: "CalendarRule table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the CalendarRule table/entity."
ms.date: 03/04/2021
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

# CalendarRule table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Defines free/busy times for a service and for resources or resource groups, such as working, non-working, vacation, and blocked.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|CalendarRules|
|DisplayCollectionName|Calendar Rules|
|DisplayName|Calendar Rule|
|EntitySetName|calendarrules|
|IsBPFEntity|False|
|LogicalCollectionName|calendarrules|
|LogicalName|calendarrule|
|OwnershipType|None|
|PrimaryIdAttribute|calendarruleid|
|PrimaryNameAttribute|name|
|SchemaName|CalendarRule|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CalendarId](#BKMK_CalendarId)
- [CalendarRuleId](#BKMK_CalendarRuleId)
- [Description](#BKMK_Description)
- [Duration](#BKMK_Duration)
- [EffectiveIntervalEnd](#BKMK_EffectiveIntervalEnd)
- [EffectiveIntervalStart](#BKMK_EffectiveIntervalStart)
- [Effort](#BKMK_Effort)
- [EndTime](#BKMK_EndTime)
- [ExtentCode](#BKMK_ExtentCode)
- [GroupDesignator](#BKMK_GroupDesignator)
- [InnerCalendarId](#BKMK_InnerCalendarId)
- [IsModified](#BKMK_IsModified)
- [IsSelected](#BKMK_IsSelected)
- [IsSimple](#BKMK_IsSimple)
- [IsVaried](#BKMK_IsVaried)
- [Name](#BKMK_Name)
- [Offset](#BKMK_Offset)
- [Pattern](#BKMK_Pattern)
- [Rank](#BKMK_Rank)
- [StartTime](#BKMK_StartTime)
- [SubCode](#BKMK_SubCode)
- [TimeCode](#BKMK_TimeCode)
- [TimeZoneCode](#BKMK_TimeZoneCode)


### <a name="BKMK_CalendarId"></a> CalendarId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the calendar with which the calendar rule is associated.|
|DisplayName|Calendar|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|calendarid|
|RequiredLevel|SystemRequired|
|Targets|calendar|
|Type|Lookup|


### <a name="BKMK_CalendarRuleId"></a> CalendarRuleId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the calendar rule.|
|DisplayName|Calendar Rule|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|calendarruleid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Defines free/busy times for a service and for resources or resource groups, such as working, non-working, vacation, and blocked.|
|DisplayName|Description|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_Duration"></a> Duration

|Property|Value|
|--------|-----|
|Description|Duration of the calendar rule in minutes.|
|DisplayName|Duration|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|duration|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_EffectiveIntervalEnd"></a> EffectiveIntervalEnd

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Effective interval end of the calendar rule.|
|DisplayName|Effective Interval End|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|effectiveintervalend|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_EffectiveIntervalStart"></a> EffectiveIntervalStart

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Effective interval start of the calendar rule.|
|DisplayName|Effective Interval Start|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|effectiveintervalstart|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_Effort"></a> Effort

|Property|Value|
|--------|-----|
|Description|Effort available for a resource during the time described by the calendar rule.|
|DisplayName|Effort|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|effort|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|
|RequiredLevel|None|
|Type|Double|


### <a name="BKMK_EndTime"></a> EndTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|End|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|endtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ExtentCode"></a> ExtentCode

|Property|Value|
|--------|-----|
|Description|Extent of the calendar rule.|
|DisplayName|Extent Code|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|extentcode|
|MaxValue|1000000000|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_GroupDesignator"></a> GroupDesignator

|Property|Value|
|--------|-----|
|Description|Unique identifier of the group.|
|DisplayName|Group Designator|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|groupdesignator|
|MaxLength|36|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_InnerCalendarId"></a> InnerCalendarId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the inner calendar for non-leaf calendar rules.|
|DisplayName|Inner Calendar|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|innercalendarid|
|RequiredLevel|None|
|Targets|calendar|
|Type|Lookup|


### <a name="BKMK_IsModified"></a> IsModified

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Is Modified|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismodified|
|RequiredLevel|None|
|Type|Boolean|

#### IsModified Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsSelected"></a> IsSelected

|Property|Value|
|--------|-----|
|Description|Flag used in vary-by-day calendar rules.|
|DisplayName|Is Selected|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isselected|
|RequiredLevel|None|
|Type|Boolean|

#### IsSelected Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsSimple"></a> IsSimple

|Property|Value|
|--------|-----|
|Description|Flag used in vary-by-day calendar rules.|
|DisplayName|Is Simple|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|issimple|
|RequiredLevel|None|
|Type|Boolean|

#### IsSimple Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsVaried"></a> IsVaried

|Property|Value|
|--------|-----|
|Description|Flag used in leaf nonrecurring rules.|
|DisplayName|Is Varied|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isvaried|
|RequiredLevel|None|
|Type|Boolean|

#### IsVaried Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of the calendar rule.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Offset"></a> Offset

|Property|Value|
|--------|-----|
|Description|Start offset for leaf nonrecurring rules.|
|DisplayName|Offset|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|offset|
|MaxValue|1000000000|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_Pattern"></a> Pattern

|Property|Value|
|--------|-----|
|Description|Pattern of the rule recurrence.|
|DisplayName|Recurrence Pattern|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|pattern|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Rank"></a> Rank

|Property|Value|
|--------|-----|
|Description|Rank of the calendar rule.|
|DisplayName|Rank|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|rank|
|MaxValue|1000000000|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_StartTime"></a> StartTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Start time for the rule.|
|DisplayName|Start|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|starttime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_SubCode"></a> SubCode

|Property|Value|
|--------|-----|
|Description|Sub-type of calendar rule.|
|DisplayName|Sub Code|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|subcode|
|MaxValue|1000000000|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_TimeCode"></a> TimeCode

|Property|Value|
|--------|-----|
|Description|Type of calendar rule such as working hours, break, holiday, or time off.|
|DisplayName|Type|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timecode|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_TimeZoneCode"></a> TimeZoneCode

|Property|Value|
|--------|-----|
|Description|Local time zone for the calendar rule.|
|DisplayName|Time Zone|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezonecode|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [BusinessUnitId](#BKMK_BusinessUnitId)
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
- [OrganizationId](#BKMK_OrganizationId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the business unit with which the calendar rule is associated.|
|DisplayName|Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|businessunitid|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the calendar rule.|
|DisplayName|Created By|
|IsValidForForm|False|
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
|Description|Date and time when the calendar rule was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the calendarrule.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|False|
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


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the calendar rule.|
|DisplayName|Modified By|
|IsValidForForm|False|
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
|Description|Date and time when the calendar rule was last modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who last modified the calendarrule.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|False|
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


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the organization with which the calendar rule is associated.|
|DisplayName|Organization |
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_calendarrule_createdonbehalfby](#BKMK_lk_calendarrule_createdonbehalfby)
- [lk_calendarrule_createdby](#BKMK_lk_calendarrule_createdby)
- [inner_calendar_calendar_rules](#BKMK_inner_calendar_calendar_rules)
- [lk_calendarrule_modifiedby](#BKMK_lk_calendarrule_modifiedby)
- [lk_calendarrule_modifiedonbehalfby](#BKMK_lk_calendarrule_modifiedonbehalfby)
- [calendar_calendar_rules](#BKMK_calendar_calendar_rules)


### <a name="BKMK_lk_calendarrule_createdonbehalfby"></a> lk_calendarrule_createdonbehalfby

See systemuser Table [lk_calendarrule_createdonbehalfby](systemuser.md) One-To-Many relationship.

### <a name="BKMK_lk_calendarrule_createdby"></a> lk_calendarrule_createdby

See systemuser Table [lk_calendarrule_createdby](systemuser.md) One-To-Many relationship.

### <a name="BKMK_inner_calendar_calendar_rules"></a> inner_calendar_calendar_rules

See calendar Table [inner_calendar_calendar_rules](calendar.md) One-To-Many relationship.

### <a name="BKMK_lk_calendarrule_modifiedby"></a> lk_calendarrule_modifiedby

See systemuser Table [lk_calendarrule_modifiedby](systemuser.md) One-To-Many relationship.

### <a name="BKMK_lk_calendarrule_modifiedonbehalfby"></a> lk_calendarrule_modifiedonbehalfby

See systemuser Table [lk_calendarrule_modifiedonbehalfby](systemuser.md) One-To-Many relationship.

### <a name="BKMK_calendar_calendar_rules"></a> calendar_calendar_rules

See calendar Table [calendar_calendar_rules](calendar.md) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.calendarrule?text=calendarrule EntityType" />