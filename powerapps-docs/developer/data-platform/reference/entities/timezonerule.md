---
title: "TimeZoneRule table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the TimeZoneRule table/entity."
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

# TimeZoneRule table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Definition for time conversion between local time and Coordinated Universal Time (UTC) for a particular time zone at a particular time period.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Retrieve|GET [*org URI*]/api/data/v9.0/timezonerules(*timezoneruleid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/timezonerules<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|TimeZoneRules|
|DisplayCollectionName|Time Zone Rules|
|DisplayName|Time Zone Rule|
|EntitySetName|timezonerules|
|IsBPFEntity|False|
|LogicalCollectionName|timezonerules|
|LogicalName|timezonerule|
|OwnershipType|None|
|PrimaryIdAttribute|timezoneruleid|
|PrimaryNameAttribute|timezoneruleversionnumber|
|SchemaName|TimeZoneRule|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description|Base time bias of the time zone rule.|
|DisplayName|Bias|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|bias|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_DaylightBias"></a> DaylightBias

|Property|Value|
|--------|-----|
|Description|Time bias in addition to the base bias for daylight savings time.|
|DisplayName|Daylight Bias|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|daylightbias|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_DaylightDay"></a> DaylightDay

|Property|Value|
|--------|-----|
|Description|Day of the month when daylight savings time starts.|
|DisplayName|Daylight Day|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|daylightday|
|MaxValue|31|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_DaylightDayOfWeek"></a> DaylightDayOfWeek

|Property|Value|
|--------|-----|
|Description|Day of the week when daylight savings time starts.|
|DisplayName|Daylight Day Of Week|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|daylightdayofweek|
|MaxValue|6|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_DaylightHour"></a> DaylightHour

|Property|Value|
|--------|-----|
|Description|Hour of the day when daylight savings time starts|
|DisplayName|Daylight Hour|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|daylighthour|
|MaxValue|23|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_DaylightMinute"></a> DaylightMinute

|Property|Value|
|--------|-----|
|Description|Minute of the hour when daylight savings time starts.|
|DisplayName|Daylight Minute|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|daylightminute|
|MaxValue|59|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_DaylightMonth"></a> DaylightMonth

|Property|Value|
|--------|-----|
|Description|Month when daylight savings time starts.|
|DisplayName|Daylight Month|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|daylightmonth|
|MaxValue|12|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_DaylightSecond"></a> DaylightSecond

|Property|Value|
|--------|-----|
|Description|Second of the minute when daylight savings time starts|
|DisplayName|Daylight Second|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|daylightsecond|
|MaxValue|59|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_DaylightYear"></a> DaylightYear

|Property|Value|
|--------|-----|
|Description|Year when daylight savings times starts.|
|DisplayName|Daylight Year|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|daylightyear|
|MaxValue|32768|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_EffectiveDateTime"></a> EffectiveDateTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Time that this rule takes effect, in local time.|
|DisplayName|Effective Date Time|
|Format|DateOnly|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|effectivedatetime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_StandardBias"></a> StandardBias

|Property|Value|
|--------|-----|
|Description|Time bias in addition to the base bias for standard time.|
|DisplayName|Standard Bias|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|standardbias|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_StandardDay"></a> StandardDay

|Property|Value|
|--------|-----|
|Description|Day of the month when standard time starts.|
|DisplayName|Standard Day|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|standardday|
|MaxValue|31|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_StandardDayOfWeek"></a> StandardDayOfWeek

|Property|Value|
|--------|-----|
|Description|Day of the week when standard time starts.|
|DisplayName|Standard Day Of Week|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|standarddayofweek|
|MaxValue|6|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_StandardHour"></a> StandardHour

|Property|Value|
|--------|-----|
|Description|Hour of the day when standard time starts.|
|DisplayName|Standard Hour|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|standardhour|
|MaxValue|23|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_StandardMinute"></a> StandardMinute

|Property|Value|
|--------|-----|
|Description|Minute of the hour when standard time starts.|
|DisplayName|Standard Minute|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|standardminute|
|MaxValue|59|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_StandardMonth"></a> StandardMonth

|Property|Value|
|--------|-----|
|Description|Month when standard time starts.|
|DisplayName|Standard Month|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|standardmonth|
|MaxValue|12|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_StandardSecond"></a> StandardSecond

|Property|Value|
|--------|-----|
|Description|Second of the Minute when standard time starts.|
|DisplayName|Standard Second|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|standardsecond|
|MaxValue|59|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_StandardYear"></a> StandardYear

|Property|Value|
|--------|-----|
|Description|Year when standard time starts.|
|DisplayName|Standard Year|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|standardyear|
|MaxValue|32768|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TimeZoneDefinitionId"></a> TimeZoneDefinitionId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the time zone definition.|
|DisplayName|Time Zone Definition|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezonedefinitionid|
|RequiredLevel|SystemRequired|
|Targets|timezonedefinition|
|Type|Lookup|


### <a name="BKMK_TimeZoneRuleId"></a> TimeZoneRuleId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the time zone rule.|
|DisplayName|Time Zone Rule|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|timezoneruleid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|--------|-----|
|Description|For internal use only|
|DisplayName|Time Zone Rule Version Number|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|timezoneruleversionnumber|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|SystemRequired|
|Type|Integer|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the time zone rule.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the time zone rule was created.|
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
|Description|Unique identifier of the delegate user who created the timezonerule.|
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
|Description|Unique identifier of the user who last modified the time zone rule.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the time zone rule was modified.|
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
|Description|Unique identifier of the delegate user who last modified the timezonerule.|
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


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the organization associated with the time zone rule.|
|DisplayName|Organization|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|None|
|Targets|organization|
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_timezonerule_createdby](#BKMK_lk_timezonerule_createdby)
- [lk_timezonerule_modifiedonbehalfby](#BKMK_lk_timezonerule_modifiedonbehalfby)
- [lk_timezonerule_modifiedby](#BKMK_lk_timezonerule_modifiedby)
- [lk_timezonerule_timezonedefinitionid](#BKMK_lk_timezonerule_timezonedefinitionid)
- [lk_timezonerule_createdonbehalfby](#BKMK_lk_timezonerule_createdonbehalfby)


### <a name="BKMK_lk_timezonerule_createdby"></a> lk_timezonerule_createdby

See systemuser Table [lk_timezonerule_createdby](systemuser.md#BKMK_lk_timezonerule_createdby) One-To-Many relationship.

### <a name="BKMK_lk_timezonerule_modifiedonbehalfby"></a> lk_timezonerule_modifiedonbehalfby

See systemuser Table [lk_timezonerule_modifiedonbehalfby](systemuser.md#BKMK_lk_timezonerule_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_timezonerule_modifiedby"></a> lk_timezonerule_modifiedby

See systemuser Table [lk_timezonerule_modifiedby](systemuser.md#BKMK_lk_timezonerule_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_timezonerule_timezonedefinitionid"></a> lk_timezonerule_timezonedefinitionid

See timezonedefinition Table [lk_timezonerule_timezonedefinitionid](timezonedefinition.md#BKMK_lk_timezonerule_timezonedefinitionid) One-To-Many relationship.

### <a name="BKMK_lk_timezonerule_createdonbehalfby"></a> lk_timezonerule_createdonbehalfby

See systemuser Table [lk_timezonerule_createdonbehalfby](systemuser.md#BKMK_lk_timezonerule_createdonbehalfby) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.timezonerule?text=timezonerule EntityType" />