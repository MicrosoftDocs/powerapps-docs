---
title: "Recurrence Rule (RecurrenceRule) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Recurrence Rule (RecurrenceRule) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Recurrence Rule (RecurrenceRule) table/entity reference (Microsoft Dataverse)

Recurrence Rule represents the pattern of incidence of recurring entities.

## Messages

The following table lists the messages for the Recurrence Rule (RecurrenceRule) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /recurrencerules<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /recurrencerules(*ruleid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /recurrencerules(*ruleid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /recurrencerules<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /recurrencerules(*ruleid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /recurrencerules(*ruleid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `ValidateRecurrenceRule`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ValidateRecurrenceRule?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ValidateRecurrenceRuleRequest>|

## Properties

The following table lists selected properties for the Recurrence Rule (RecurrenceRule) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Recurrence Rule** |
| **DisplayCollectionName** | **Recurrence Rules** |
| **SchemaName** | `RecurrenceRule` |
| **CollectionSchemaName** | `RecurrenceRules` |
| **EntitySetName** | `recurrencerules`|
| **LogicalName** | `recurrencerule` |
| **LogicalCollectionName** | `recurrencerules` |
| **PrimaryIdAttribute** | `ruleid` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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

|Property|Value|
|---|---|
|Description|**The day of the month on which the recurring appointment or task occurs.**|
|DisplayName|**Day Of Month**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`dayofmonth`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|31|
|MinValue|0|

### <a name="BKMK_DaysOfWeekMask"></a> DaysOfWeekMask

|Property|Value|
|---|---|
|Description|**Bitmask representing the days of the week on which the recurring appointment or task occurs.**|
|DisplayName|**Days Of Week Mask**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`daysofweekmask`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|127|
|MinValue|1|

### <a name="BKMK_Duration"></a> Duration

|Property|Value|
|---|---|
|Description|**Duration of the recurrence pattern in minutes.**|
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
|Description|**The actual end date for expansion of the recurrence pattern.**|
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
|Description|**The actual start date for expansion of the recurrence pattern.**|
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
|DisplayName|**End Time**|
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
|Description|**First day Of week for the recurrence pattern.**|
|DisplayName|**First Day Of Week**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`firstdayofweek`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|6|
|MinValue|0|

### <a name="BKMK_Instance"></a> Instance

|Property|Value|
|---|---|
|Description|**Specifies the count for which the recurrence pattern is valid for a given interval.**|
|DisplayName|**Instance**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`instance`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`recurrencerule_instance`|

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

### <a name="BKMK_IsNthMonthly"></a> IsNthMonthly

|Property|Value|
|---|---|
|Description|**Specifies whether the monthly recurrence pattern is Nth monthly, valid only for monthly recurrence.**|
|DisplayName|**Nth Monthly**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isnthmonthly`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`recurrencerule_isnthmonthly`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsNthYearly"></a> IsNthYearly

|Property|Value|
|---|---|
|Description|**Specifies whether the yearly recurrence pattern is Nth yearly, valid only for yearly recurrence.**|
|DisplayName|**Nth Yearly**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isnthyearly`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`recurrencerule_isnthyearly`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsRegenerate"></a> IsRegenerate

|Property|Value|
|---|---|
|Description|**Valid only for task type recurrence,indicates whether task should be regenerated.**|
|DisplayName|**Regenerate**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isregenerate`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`recurrencerule_isregenerate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsWeekDayPattern"></a> IsWeekDayPattern

|Property|Value|
|---|---|
|Description|**Specifies whether the weekly recurrence pattern is actually a daily every weekday pattern, valid only for weekly recurrence.**|
|DisplayName|**Every Weekday**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isweekdaypattern`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`recurrencerule_isweekdaypattern`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_MonthOfYear"></a> MonthOfYear

|Property|Value|
|---|---|
|Description|**Specifies the month of the year valid for the recurrence pattern.**|
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

### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|---|---|
|Description|**Unique identifier of the object with which the recurrence rule is associated.**|
|DisplayName|**Regarding**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|activitypointer|

### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|---|---|
|Description||
|DisplayName|**Object Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_Occurrences"></a> Occurrences

|Property|Value|
|---|---|
|Description|**Number of occurrences of the recurrence pattern.**|
|DisplayName|**Occurrences**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`occurrences`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|999|
|MinValue|1|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user or team who owns the recurrence rule.**|
|DisplayName|**Owner**|
|IsValidForForm|False|
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
|Description|**End date of the Recurrence Range.**|
|DisplayName|**Recurrence Range End**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`patternenddate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_PatternEndType"></a> PatternEndType

|Property|Value|
|---|---|
|Description|**Pattern End Type of a recurring series.**|
|DisplayName|**Pattern End Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`patternendtype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`recurrencerule_patternendtype`|

#### PatternEndType Choices/Options

|Value|Label|
|---|---|
|1|**No End Date**|
|2|**Occurrences**|
|3|**Pattern End Date**|

### <a name="BKMK_PatternStartDate"></a> PatternStartDate

|Property|Value|
|---|---|
|Description|**Start date of the Recurrence Range.**|
|DisplayName|**Recurrence Range Start**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`patternstartdate`|
|RequiredLevel|ApplicationRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_RecurrencePatternType"></a> RecurrencePatternType

|Property|Value|
|---|---|
|Description|**Type of Recurrence.**|
|DisplayName|**Recurrence Pattern**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`recurrencepatterntype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`recurrencerule_recurrencepatterntype`|

#### RecurrencePatternType Choices/Options

|Value|Label|
|---|---|
|0|**Daily**|
|1|**Weekly**|
|2|**Monthly**|
|3|**Yearly**|

### <a name="BKMK_RuleId"></a> RuleId

|Property|Value|
|---|---|
|Description|**Unique identifier of the entity associated with recurrence rule.**|
|DisplayName|**Recurrence Rule**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ruleid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_StartTime"></a> StartTime

|Property|Value|
|---|---|
|Description|**Start time of the recurring activity.**|
|DisplayName|**Start Time**|
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


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the recurrence rule.**|
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
|Description|**Date and time when the recurrence rule was created.**|
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
|Description|**Unique identifier of the delegate user who created the recurrence rule.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the recurrence rule.**|
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
|Description|**Date and time when the recurrence rule was last modified.**|
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
|Description|**Unique identifier of the delegate user who modified the recurrence rule.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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
|Description|**Unique identifier of the business unit that owns the recurrence rule.**|
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
|Description||
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
|Description||
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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

- [activity_pointer_recurrencerule](#BKMK_activity_pointer_recurrencerule)
- [business_unit_recurrencerule](#BKMK_business_unit_recurrencerule)
- [lk_recurrencerule_createdby](#BKMK_lk_recurrencerule_createdby)
- [lk_recurrencerule_modifiedby](#BKMK_lk_recurrencerule_modifiedby)
- [lk_recurrencerulebase_createdonbehalfby](#BKMK_lk_recurrencerulebase_createdonbehalfby)
- [lk_recurrencerulebase_modifiedonbehalfby](#BKMK_lk_recurrencerulebase_modifiedonbehalfby)
- [owner_recurrencerules](#BKMK_owner_recurrencerules)

### <a name="BKMK_activity_pointer_recurrencerule"></a> activity_pointer_recurrencerule

One-To-Many Relationship: [activitypointer activity_pointer_recurrencerule](activitypointer.md#BKMK_activity_pointer_recurrencerule)

|Property|Value|
|---|---|
|ReferencedEntity|`activitypointer`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_business_unit_recurrencerule"></a> business_unit_recurrencerule

One-To-Many Relationship: [businessunit business_unit_recurrencerule](businessunit.md#BKMK_business_unit_recurrencerule)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_recurrencerule_createdby"></a> lk_recurrencerule_createdby

One-To-Many Relationship: [systemuser lk_recurrencerule_createdby](systemuser.md#BKMK_lk_recurrencerule_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_recurrencerule_modifiedby"></a> lk_recurrencerule_modifiedby

One-To-Many Relationship: [systemuser lk_recurrencerule_modifiedby](systemuser.md#BKMK_lk_recurrencerule_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_recurrencerulebase_createdonbehalfby"></a> lk_recurrencerulebase_createdonbehalfby

One-To-Many Relationship: [systemuser lk_recurrencerulebase_createdonbehalfby](systemuser.md#BKMK_lk_recurrencerulebase_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_recurrencerulebase_modifiedonbehalfby"></a> lk_recurrencerulebase_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_recurrencerulebase_modifiedonbehalfby](systemuser.md#BKMK_lk_recurrencerulebase_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_recurrencerules"></a> owner_recurrencerules

One-To-Many Relationship: [owner owner_recurrencerules](owner.md#BKMK_owner_recurrencerules)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_recurrencerule_recurringappointmentmaster"></a> recurrencerule_recurringappointmentmaster

Many-To-One Relationship: [recurringappointmentmaster recurrencerule_recurringappointmentmaster](recurringappointmentmaster.md#BKMK_recurrencerule_recurringappointmentmaster)

|Property|Value|
|---|---|
|ReferencingEntity|`recurringappointmentmaster`|
|ReferencingAttribute|`activityid`|
|ReferencedEntityNavigationPropertyName|`recurrencerule_recurringappointmentmaster`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.recurrencerule?displayProperty=fullName>
