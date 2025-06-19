---
title: "Calendar Rule (CalendarRule) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Calendar Rule (CalendarRule) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Calendar Rule (CalendarRule) table/entity reference (Microsoft Dataverse)

Defines free/busy times for a service and for resources or resource groups, such as working, non-working, vacation, and blocked.

## Messages

The following table lists the messages for the Calendar Rule (CalendarRule) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|

## Properties

The following table lists selected properties for the Calendar Rule (CalendarRule) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Calendar Rule** |
| **DisplayCollectionName** | **Calendar Rules** |
| **SchemaName** | `CalendarRule` |
| **CollectionSchemaName** | `CalendarRules` |
| **EntitySetName** | `calendarrules`|
| **LogicalName** | `calendarrule` |
| **LogicalCollectionName** | `calendarrules` |
| **PrimaryIdAttribute** | `calendarruleid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

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
|---|---|
|Description|**Unique identifier of the calendar with which the calendar rule is associated.**|
|DisplayName|**Calendar**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`calendarid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|calendar|

### <a name="BKMK_CalendarRuleId"></a> CalendarRuleId

|Property|Value|
|---|---|
|Description|**Unique identifier of the calendar rule.**|
|DisplayName|**Calendar Rule**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`calendarruleid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Defines free/busy times for a service and for resources or resource groups, such as working, non-working, vacation, and blocked.**|
|DisplayName|**Description**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_Duration"></a> Duration

|Property|Value|
|---|---|
|Description|**Duration of the calendar rule in minutes.**|
|DisplayName|**Duration**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`duration`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_EffectiveIntervalEnd"></a> EffectiveIntervalEnd

|Property|Value|
|---|---|
|Description|**Effective interval end of the calendar rule.**|
|DisplayName|**Effective Interval End**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`effectiveintervalend`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_EffectiveIntervalStart"></a> EffectiveIntervalStart

|Property|Value|
|---|---|
|Description|**Effective interval start of the calendar rule.**|
|DisplayName|**Effective Interval Start**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`effectiveintervalstart`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_Effort"></a> Effort

|Property|Value|
|---|---|
|Description|**Effort available for a resource during the time described by the calendar rule.**|
|DisplayName|**Effort**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`effort`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Disabled|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|

### <a name="BKMK_EndTime"></a> EndTime

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**End**|
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

### <a name="BKMK_ExtentCode"></a> ExtentCode

|Property|Value|
|---|---|
|Description|**Extent of the calendar rule.**|
|DisplayName|**Extent Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`extentcode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

### <a name="BKMK_GroupDesignator"></a> GroupDesignator

|Property|Value|
|---|---|
|Description|**Unique identifier of the group.**|
|DisplayName|**Group Designator**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`groupdesignator`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|36|

### <a name="BKMK_InnerCalendarId"></a> InnerCalendarId

|Property|Value|
|---|---|
|Description|**Unique identifier of the inner calendar for non-leaf calendar rules.**|
|DisplayName|**Inner Calendar**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`innercalendarid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|calendar|

### <a name="BKMK_IsModified"></a> IsModified

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Is Modified**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismodified`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`calendarrule_ismodified`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsSelected"></a> IsSelected

|Property|Value|
|---|---|
|Description|**Flag used in vary-by-day calendar rules.**|
|DisplayName|**Is Selected**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isselected`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`calendarrule_isselected`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsSimple"></a> IsSimple

|Property|Value|
|---|---|
|Description|**Flag used in vary-by-day calendar rules.**|
|DisplayName|**Is Simple**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`issimple`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`calendarrule_issimple`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsVaried"></a> IsVaried

|Property|Value|
|---|---|
|Description|**Flag used in leaf nonrecurring rules.**|
|DisplayName|**Is Varied**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isvaried`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`calendarrule_isvaried`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the calendar rule.**|
|DisplayName|**Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_Offset"></a> Offset

|Property|Value|
|---|---|
|Description|**Start offset for leaf nonrecurring rules.**|
|DisplayName|**Offset**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`offset`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

### <a name="BKMK_Pattern"></a> Pattern

|Property|Value|
|---|---|
|Description|**Pattern of the rule recurrence.**|
|DisplayName|**Recurrence Pattern**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`pattern`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_Rank"></a> Rank

|Property|Value|
|---|---|
|Description|**Rank of the calendar rule.**|
|DisplayName|**Rank**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`rank`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

### <a name="BKMK_StartTime"></a> StartTime

|Property|Value|
|---|---|
|Description|**Start time for the rule.**|
|DisplayName|**Start**|
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

### <a name="BKMK_SubCode"></a> SubCode

|Property|Value|
|---|---|
|Description|**Sub-type of calendar rule.**|
|DisplayName|**Sub Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`subcode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

### <a name="BKMK_TimeCode"></a> TimeCode

|Property|Value|
|---|---|
|Description|**Type of calendar rule such as working hours, break, holiday, or time off.**|
|DisplayName|**Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_TimeZoneCode"></a> TimeZoneCode

|Property|Value|
|---|---|
|Description|**Local time zone for the calendar rule.**|
|DisplayName|**Time Zone**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [BusinessUnitId](#BKMK_BusinessUnitId)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

|Property|Value|
|---|---|
|Description|**Unique identifier of the business unit with which the calendar rule is associated.**|
|DisplayName|**Business Unit**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`businessunitid`|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the calendar rule.**|
|DisplayName|**Created By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the calendar rule was created.**|
|DisplayName|**Created On**|
|IsValidForForm|False|
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
|Description|**Unique identifier of the delegate user who created the calendarrule.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the calendar rule.**|
|DisplayName|**Modified By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the calendar rule was last modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|False|
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
|Description|**Unique identifier of the delegate user who last modified the calendarrule.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization with which the calendar rule is associated.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|

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

- [calendar_calendar_rules](#BKMK_calendar_calendar_rules)
- [inner_calendar_calendar_rules](#BKMK_inner_calendar_calendar_rules)
- [lk_calendarrule_createdby](#BKMK_lk_calendarrule_createdby)
- [lk_calendarrule_createdonbehalfby](#BKMK_lk_calendarrule_createdonbehalfby)
- [lk_calendarrule_modifiedby](#BKMK_lk_calendarrule_modifiedby)
- [lk_calendarrule_modifiedonbehalfby](#BKMK_lk_calendarrule_modifiedonbehalfby)

### <a name="BKMK_calendar_calendar_rules"></a> calendar_calendar_rules

One-To-Many Relationship: [calendar calendar_calendar_rules](calendar.md#BKMK_calendar_calendar_rules)

|Property|Value|
|---|---|
|ReferencedEntity|`calendar`|
|ReferencedAttribute|`calendarid`|
|ReferencingAttribute|`calendarid`|
|ReferencingEntityNavigationPropertyName|`calendarid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_inner_calendar_calendar_rules"></a> inner_calendar_calendar_rules

One-To-Many Relationship: [calendar inner_calendar_calendar_rules](calendar.md#BKMK_inner_calendar_calendar_rules)

|Property|Value|
|---|---|
|ReferencedEntity|`calendar`|
|ReferencedAttribute|`calendarid`|
|ReferencingAttribute|`innercalendarid`|
|ReferencingEntityNavigationPropertyName|`innercalendarid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_calendarrule_createdby"></a> lk_calendarrule_createdby

One-To-Many Relationship: [systemuser lk_calendarrule_createdby](systemuser.md#BKMK_lk_calendarrule_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_calendarrule_createdonbehalfby"></a> lk_calendarrule_createdonbehalfby

One-To-Many Relationship: [systemuser lk_calendarrule_createdonbehalfby](systemuser.md#BKMK_lk_calendarrule_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_calendarrule_modifiedby"></a> lk_calendarrule_modifiedby

One-To-Many Relationship: [systemuser lk_calendarrule_modifiedby](systemuser.md#BKMK_lk_calendarrule_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_calendarrule_modifiedonbehalfby"></a> lk_calendarrule_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_calendarrule_modifiedonbehalfby](systemuser.md#BKMK_lk_calendarrule_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.calendarrule?displayProperty=fullName>
