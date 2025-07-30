---
title: "Time Zone Rule (TimeZoneRule) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Time Zone Rule (TimeZoneRule) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Time Zone Rule (TimeZoneRule) table/entity reference (Microsoft Dataverse)

Definition for time conversion between local time and Coordinated Universal Time (UTC) for a particular time zone at a particular time period.

## Messages

The following table lists the messages for the Time Zone Rule (TimeZoneRule) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /timezonerules(*timezoneruleid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /timezonerules<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Time Zone Rule (TimeZoneRule) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Time Zone Rule** |
| **DisplayCollectionName** | **Time Zone Rules** |
| **SchemaName** | `TimeZoneRule` |
| **CollectionSchemaName** | `TimeZoneRules` |
| **EntitySetName** | `timezonerules`|
| **LogicalName** | `timezonerule` |
| **LogicalCollectionName** | `timezonerules` |
| **PrimaryIdAttribute** | `timezoneruleid` |
| **PrimaryNameAttribute** |`timezoneruleversionnumber` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Bias](#BKMK_Bias)
- [DaylightBias](#BKMK_DaylightBias)
- [DaylightDay](#BKMK_DaylightDay)
- [DaylightDayOfWeek](#BKMK_DaylightDayOfWeek)
- [DaylightHour](#BKMK_DaylightHour)
- [DaylightMinute](#BKMK_DaylightMinute)
- [DaylightMonth](#BKMK_DaylightMonth)
- [DaylightSecond](#BKMK_DaylightSecond)
- [DaylightYear](#BKMK_DaylightYear)
- [EffectiveDateTime](#BKMK_EffectiveDateTime)
- [StandardBias](#BKMK_StandardBias)
- [StandardDay](#BKMK_StandardDay)
- [StandardDayOfWeek](#BKMK_StandardDayOfWeek)
- [StandardHour](#BKMK_StandardHour)
- [StandardMinute](#BKMK_StandardMinute)
- [StandardMonth](#BKMK_StandardMonth)
- [StandardSecond](#BKMK_StandardSecond)
- [StandardYear](#BKMK_StandardYear)
- [TimeZoneDefinitionId](#BKMK_TimeZoneDefinitionId)
- [TimeZoneRuleId](#BKMK_TimeZoneRuleId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)

### <a name="BKMK_Bias"></a> Bias

|Property|Value|
|---|---|
|Description|**Base time bias of the time zone rule.**|
|DisplayName|**Bias**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`bias`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_DaylightBias"></a> DaylightBias

|Property|Value|
|---|---|
|Description|**Time bias in addition to the base bias for daylight savings time.**|
|DisplayName|**Daylight Bias**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`daylightbias`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_DaylightDay"></a> DaylightDay

|Property|Value|
|---|---|
|Description|**Day of the month when daylight savings time starts.**|
|DisplayName|**Daylight Day**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`daylightday`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|31|
|MinValue|0|

### <a name="BKMK_DaylightDayOfWeek"></a> DaylightDayOfWeek

|Property|Value|
|---|---|
|Description|**Day of the week when daylight savings time starts.**|
|DisplayName|**Daylight Day Of Week**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`daylightdayofweek`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|6|
|MinValue|0|

### <a name="BKMK_DaylightHour"></a> DaylightHour

|Property|Value|
|---|---|
|Description|**Hour of the day when daylight savings time starts**|
|DisplayName|**Daylight Hour**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`daylighthour`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|23|
|MinValue|0|

### <a name="BKMK_DaylightMinute"></a> DaylightMinute

|Property|Value|
|---|---|
|Description|**Minute of the hour when daylight savings time starts.**|
|DisplayName|**Daylight Minute**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`daylightminute`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|59|
|MinValue|0|

### <a name="BKMK_DaylightMonth"></a> DaylightMonth

|Property|Value|
|---|---|
|Description|**Month when daylight savings time starts.**|
|DisplayName|**Daylight Month**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`daylightmonth`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|12|
|MinValue|0|

### <a name="BKMK_DaylightSecond"></a> DaylightSecond

|Property|Value|
|---|---|
|Description|**Second of the minute when daylight savings time starts**|
|DisplayName|**Daylight Second**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`daylightsecond`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|59|
|MinValue|0|

### <a name="BKMK_DaylightYear"></a> DaylightYear

|Property|Value|
|---|---|
|Description|**Year when daylight savings times starts.**|
|DisplayName|**Daylight Year**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`daylightyear`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|32768|
|MinValue|0|

### <a name="BKMK_EffectiveDateTime"></a> EffectiveDateTime

|Property|Value|
|---|---|
|Description|**Time that this rule takes effect, in local time.**|
|DisplayName|**Effective Date Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`effectivedatetime`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_StandardBias"></a> StandardBias

|Property|Value|
|---|---|
|Description|**Time bias in addition to the base bias for standard time.**|
|DisplayName|**Standard Bias**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`standardbias`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_StandardDay"></a> StandardDay

|Property|Value|
|---|---|
|Description|**Day of the month when standard time starts.**|
|DisplayName|**Standard Day**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`standardday`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|31|
|MinValue|0|

### <a name="BKMK_StandardDayOfWeek"></a> StandardDayOfWeek

|Property|Value|
|---|---|
|Description|**Day of the week when standard time starts.**|
|DisplayName|**Standard Day Of Week**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`standarddayofweek`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|6|
|MinValue|0|

### <a name="BKMK_StandardHour"></a> StandardHour

|Property|Value|
|---|---|
|Description|**Hour of the day when standard time starts.**|
|DisplayName|**Standard Hour**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`standardhour`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|23|
|MinValue|0|

### <a name="BKMK_StandardMinute"></a> StandardMinute

|Property|Value|
|---|---|
|Description|**Minute of the hour when standard time starts.**|
|DisplayName|**Standard Minute**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`standardminute`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|59|
|MinValue|0|

### <a name="BKMK_StandardMonth"></a> StandardMonth

|Property|Value|
|---|---|
|Description|**Month when standard time starts.**|
|DisplayName|**Standard Month**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`standardmonth`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|12|
|MinValue|0|

### <a name="BKMK_StandardSecond"></a> StandardSecond

|Property|Value|
|---|---|
|Description|**Second of the Minute when standard time starts.**|
|DisplayName|**Standard Second**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`standardsecond`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|59|
|MinValue|0|

### <a name="BKMK_StandardYear"></a> StandardYear

|Property|Value|
|---|---|
|Description|**Year when standard time starts.**|
|DisplayName|**Standard Year**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`standardyear`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|32768|
|MinValue|0|

### <a name="BKMK_TimeZoneDefinitionId"></a> TimeZoneDefinitionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the time zone definition.**|
|DisplayName|**Time Zone Definition**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonedefinitionid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|timezonedefinition|

### <a name="BKMK_TimeZoneRuleId"></a> TimeZoneRuleId

|Property|Value|
|---|---|
|Description|**Unique identifier of the time zone rule.**|
|DisplayName|**Time Zone Rule**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezoneruleid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only**|
|DisplayName|**Time Zone Rule Version Number**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`timezoneruleversionnumber`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the time zone rule.**|
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
|Description|**Date and time when the time zone rule was created.**|
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
|Description|**Unique identifier of the delegate user who created the timezonerule.**|
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
|Description|**Unique identifier of the user who last modified the time zone rule.**|
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
|Description|**Date and time when the time zone rule was modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the timezonerule.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization associated with the time zone rule.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|organization|

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

- [lk_timezonerule_createdby](#BKMK_lk_timezonerule_createdby)
- [lk_timezonerule_createdonbehalfby](#BKMK_lk_timezonerule_createdonbehalfby)
- [lk_timezonerule_modifiedby](#BKMK_lk_timezonerule_modifiedby)
- [lk_timezonerule_modifiedonbehalfby](#BKMK_lk_timezonerule_modifiedonbehalfby)
- [lk_timezonerule_timezonedefinitionid](#BKMK_lk_timezonerule_timezonedefinitionid)

### <a name="BKMK_lk_timezonerule_createdby"></a> lk_timezonerule_createdby

One-To-Many Relationship: [systemuser lk_timezonerule_createdby](systemuser.md#BKMK_lk_timezonerule_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_timezonerule_createdonbehalfby"></a> lk_timezonerule_createdonbehalfby

One-To-Many Relationship: [systemuser lk_timezonerule_createdonbehalfby](systemuser.md#BKMK_lk_timezonerule_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_timezonerule_modifiedby"></a> lk_timezonerule_modifiedby

One-To-Many Relationship: [systemuser lk_timezonerule_modifiedby](systemuser.md#BKMK_lk_timezonerule_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_timezonerule_modifiedonbehalfby"></a> lk_timezonerule_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_timezonerule_modifiedonbehalfby](systemuser.md#BKMK_lk_timezonerule_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_timezonerule_timezonedefinitionid"></a> lk_timezonerule_timezonedefinitionid

One-To-Many Relationship: [timezonedefinition lk_timezonerule_timezonedefinitionid](timezonedefinition.md#BKMK_lk_timezonerule_timezonedefinitionid)

|Property|Value|
|---|---|
|ReferencedEntity|`timezonedefinition`|
|ReferencedAttribute|`timezonedefinitionid`|
|ReferencingAttribute|`timezonedefinitionid`|
|ReferencingEntityNavigationPropertyName|`timezonedefinitionid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.timezonerule?displayProperty=fullName>
