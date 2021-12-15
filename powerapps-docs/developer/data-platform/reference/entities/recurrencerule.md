---
title: "RecurrenceRule table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the RecurrenceRule table/entity."
ms.date: 10/05/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "margoc"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# RecurrenceRule table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Recurrence Rule represents the pattern of incidence of recurring entities.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/recurrencerules<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/recurrencerules(*ruleid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/recurrencerules(*ruleid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/recurrencerules<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/recurrencerules(*ruleid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|ValidateRecurrenceRule|<xref href="Microsoft.Dynamics.CRM.ValidateRecurrenceRule?text=ValidateRecurrenceRule Function" />|<xref:Microsoft.Crm.Sdk.Messages.ValidateRecurrenceRuleRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|RecurrenceRules|
|DisplayCollectionName|Recurrence Rules|
|DisplayName|Recurrence Rule|
|EntitySetName|recurrencerules|
|IsBPFEntity|False|
|LogicalCollectionName|recurrencerules|
|LogicalName|recurrencerule|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|ruleid|
|PrimaryNameAttribute||
|SchemaName|RecurrenceRule|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description|The day of the month on which the recurring appointment or task occurs.|
|DisplayName|Day Of Month|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|dayofmonth|
|MaxValue|31|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_DaysOfWeekMask"></a> DaysOfWeekMask

|Property|Value|
|--------|-----|
|Description|Bitmask representing the days of the week on which the recurring appointment or task occurs.|
|DisplayName|Days Of Week Mask|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|daysofweekmask|
|MaxValue|127|
|MinValue|1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_Duration"></a> Duration

|Property|Value|
|--------|-----|
|Description|Duration of the recurrence pattern in minutes.|
|DisplayName|Duration|
|Format|Duration|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|duration|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_EffectiveEndDate"></a> EffectiveEndDate

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|The actual end date for expansion of the recurrence pattern.|
|DisplayName|Effective End Date|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|effectiveenddate|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_EffectiveStartDate"></a> EffectiveStartDate

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|The actual start date for expansion of the recurrence pattern.|
|DisplayName|Effective Start Date|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|effectivestartdate|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_EndTime"></a> EndTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|End time of the associated activity.|
|DisplayName|End Time|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|endtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_FirstDayOfWeek"></a> FirstDayOfWeek

|Property|Value|
|--------|-----|
|Description|First day Of week for the recurrence pattern.|
|DisplayName|First Day Of Week|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|firstdayofweek|
|MaxValue|6|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_Instance"></a> Instance

|Property|Value|
|--------|-----|
|Description|Specifies the count for which the recurrence pattern is valid for a given interval.|
|DisplayName|Instance|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|instance|
|RequiredLevel|None|
|Type|Picklist|

#### Instance Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|First||
|2|Second||
|3|Third||
|4|Fourth||
|5|Last||



### <a name="BKMK_Interval"></a> Interval

|Property|Value|
|--------|-----|
|Description|Number of units of a given recurrence type between occurrences.|
|DisplayName|Interval|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|interval|
|MaxValue|1000|
|MinValue|1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_IsNthMonthly"></a> IsNthMonthly

|Property|Value|
|--------|-----|
|Description|Specifies whether the monthly recurrence pattern is Nth monthly, valid only for monthly recurrence.|
|DisplayName|Nth Monthly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isnthmonthly|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsNthMonthly Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsNthYearly"></a> IsNthYearly

|Property|Value|
|--------|-----|
|Description|Specifies whether the yearly recurrence pattern is Nth yearly, valid only for yearly recurrence.|
|DisplayName|Nth Yearly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isnthyearly|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsNthYearly Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsRegenerate"></a> IsRegenerate

|Property|Value|
|--------|-----|
|Description|Valid only for task type recurrence,indicates whether task should be regenerated.|
|DisplayName|Regenerate|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isregenerate|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsRegenerate Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsWeekDayPattern"></a> IsWeekDayPattern

|Property|Value|
|--------|-----|
|Description|Specifies whether the weekly recurrence pattern is actually a daily every weekday pattern, valid only for weekly recurrence.|
|DisplayName|Every Weekday|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isweekdaypattern|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsWeekDayPattern Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_MonthOfYear"></a> MonthOfYear

|Property|Value|
|--------|-----|
|Description|Specifies the month of the year valid for the recurrence pattern.|
|DisplayName|Month Of Year|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|monthofyear|
|RequiredLevel|None|
|Type|Picklist|

#### MonthOfYear Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Invalid Month Of Year||
|1|January||
|2|February||
|3|March||
|4|April||
|5|May||
|6|June||
|7|July||
|8|August||
|9|September||
|10|October||
|11|November||
|12|December||



### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the object with which the recurrence rule is associated.|
|DisplayName|Regarding|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|objectid|
|RequiredLevel|None|
|Targets|activitypointer|
|Type|Lookup|


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Object Type |
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|objecttypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_Occurrences"></a> Occurrences

|Property|Value|
|--------|-----|
|Description|Number of occurrences of the recurrence pattern.|
|DisplayName|Occurrences|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|occurrences|
|MaxValue|999|
|MinValue|1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user or team who owns the recurrence rule.|
|DisplayName|Owner|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
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
|IsValidForUpdate|False|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_PatternEndDate"></a> PatternEndDate

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|End date of the Recurrence Range.|
|DisplayName|Recurrence Range End|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|patternenddate|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_PatternEndType"></a> PatternEndType

|Property|Value|
|--------|-----|
|Description|Pattern End Type of a recurring series.|
|DisplayName|Pattern End Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|patternendtype|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### PatternEndType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|No End Date||
|2|Occurrences||
|3|Pattern End Date||



### <a name="BKMK_PatternStartDate"></a> PatternStartDate

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Start date of the Recurrence Range.|
|DisplayName|Recurrence Range Start|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|patternstartdate|
|RequiredLevel|ApplicationRequired|
|Type|DateTime|


### <a name="BKMK_RecurrencePatternType"></a> RecurrencePatternType

|Property|Value|
|--------|-----|
|Description|Type of Recurrence.|
|DisplayName|Recurrence Pattern|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|recurrencepatterntype|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### RecurrencePatternType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Daily||
|1|Weekly||
|2|Monthly||
|3|Yearly||



### <a name="BKMK_RuleId"></a> RuleId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the entity associated with recurrence rule.|
|DisplayName|Recurrence Rule|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|ruleid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_StartTime"></a> StartTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Start time of the recurring activity.|
|DisplayName|Start Time|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|starttime|
|RequiredLevel|None|
|Type|DateTime|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

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

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the recurrence rule.|
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
|Description|Date and time when the recurrence rule was created.|
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
|Description|Unique identifier of the delegate user who created the recurrence rule.|
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


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the recurrence rule.|
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


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the recurrence rule was last modified.|
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
|Description|Unique identifier of the delegate user who modified the recurrence rule.|
|DisplayName|Created By (Delegate)|
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
|Description|Unique identifier of the business unit that owns the recurrence rule.|
|DisplayName|Owning Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|--------|-----|
|Description||
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
|Description||
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


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

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_recurrencerule_recurringappointmentmaster"></a> recurrencerule_recurringappointmentmaster

Same as recurringappointmentmaster table [recurrencerule_recurringappointmentmaster](recurringappointmentmaster.md#BKMK_recurrencerule_recurringappointmentmaster) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurringappointmentmaster|
|ReferencingAttribute|activityid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|recurrencerule_recurringappointmentmaster|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [business_unit_recurrencerule](#BKMK_business_unit_recurrencerule)
- [activity_pointer_recurrencerule](#BKMK_activity_pointer_recurrencerule)
- [lk_recurrencerule_modifiedby](#BKMK_lk_recurrencerule_modifiedby)
- [lk_recurrencerule_createdby](#BKMK_lk_recurrencerule_createdby)
- [lk_recurrencerulebase_createdonbehalfby](#BKMK_lk_recurrencerulebase_createdonbehalfby)
- [lk_recurrencerulebase_modifiedonbehalfby](#BKMK_lk_recurrencerulebase_modifiedonbehalfby)


### <a name="BKMK_business_unit_recurrencerule"></a> business_unit_recurrencerule

See businessunit Table [business_unit_recurrencerule](businessunit.md#BKMK_business_unit_recurrencerule) One-To-Many relationship.

### <a name="BKMK_activity_pointer_recurrencerule"></a> activity_pointer_recurrencerule

See activitypointer Table [activity_pointer_recurrencerule](activitypointer.md#BKMK_activity_pointer_recurrencerule) One-To-Many relationship.

### <a name="BKMK_lk_recurrencerule_modifiedby"></a> lk_recurrencerule_modifiedby

See systemuser Table [lk_recurrencerule_modifiedby](systemuser.md#BKMK_lk_recurrencerule_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_recurrencerule_createdby"></a> lk_recurrencerule_createdby

See systemuser Table [lk_recurrencerule_createdby](systemuser.md#BKMK_lk_recurrencerule_createdby) One-To-Many relationship.

### <a name="BKMK_lk_recurrencerulebase_createdonbehalfby"></a> lk_recurrencerulebase_createdonbehalfby

See systemuser Table [lk_recurrencerulebase_createdonbehalfby](systemuser.md#BKMK_lk_recurrencerulebase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_recurrencerulebase_modifiedonbehalfby"></a> lk_recurrencerulebase_modifiedonbehalfby

See systemuser Table [lk_recurrencerulebase_modifiedonbehalfby](systemuser.md#BKMK_lk_recurrencerulebase_modifiedonbehalfby) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.recurrencerule?text=recurrencerule EntityType" />