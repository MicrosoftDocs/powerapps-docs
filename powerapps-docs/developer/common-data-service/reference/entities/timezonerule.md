---
title: "TimeZoneRule Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the TimeZoneRule entity."
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
# TimeZoneRule Entity Reference

Definition for time conversion between local time and Coordinated Universal Time (UTC) for a particular time zone at a particular time period.

## Entity Properties

**DisplayName**: Time Zone Rule<br />
**DisplayCollectionName**: Time Zone Rules<br />
**SchemaName**: TimeZoneRule<br />
**CollectionSchemaName**: TimeZoneRules<br />
**LogicalName**: timezonerule<br />
**LogicalCollectionName**: timezonerules<br />
**EntitySetName**: timezonerules<br />
**PrimaryIdAttribute**: timezoneruleid<br />
**PrimaryNameAttribute**: timezoneruleversionnumber<br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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

**Description**: Base time bias of the time zone rule.<br />
**DisplayName**: Bias<br />
**LogicalName**: bias<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_DaylightBias"></a> DaylightBias

**Description**: Time bias in addition to the base bias for daylight savings time.<br />
**DisplayName**: Daylight Bias<br />
**LogicalName**: daylightbias<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_DaylightDay"></a> DaylightDay

**Description**: Day of the month when daylight savings time starts.<br />
**DisplayName**: Daylight Day<br />
**LogicalName**: daylightday<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 31<br />
**MinValue**: 0


### <a name="BKMK_DaylightDayOfWeek"></a> DaylightDayOfWeek

**Description**: Day of the week when daylight savings time starts.<br />
**DisplayName**: Daylight Day Of Week<br />
**LogicalName**: daylightdayofweek<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 6<br />
**MinValue**: 0


### <a name="BKMK_DaylightHour"></a> DaylightHour

**Description**: Hour of the day when daylight savings time starts<br />
**DisplayName**: Daylight Hour<br />
**LogicalName**: daylighthour<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 23<br />
**MinValue**: 0


### <a name="BKMK_DaylightMinute"></a> DaylightMinute

**Description**: Minute of the hour when daylight savings time starts.<br />
**DisplayName**: Daylight Minute<br />
**LogicalName**: daylightminute<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 59<br />
**MinValue**: 0


### <a name="BKMK_DaylightMonth"></a> DaylightMonth

**Description**: Month when daylight savings time starts.<br />
**DisplayName**: Daylight Month<br />
**LogicalName**: daylightmonth<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 12<br />
**MinValue**: 0


### <a name="BKMK_DaylightSecond"></a> DaylightSecond

**Description**: Second of the minute when daylight savings time starts<br />
**DisplayName**: Daylight Second<br />
**LogicalName**: daylightsecond<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 59<br />
**MinValue**: 0


### <a name="BKMK_DaylightYear"></a> DaylightYear

**Description**: Year when daylight savings times starts.<br />
**DisplayName**: Daylight Year<br />
**LogicalName**: daylightyear<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 32768<br />
**MinValue**: 0


### <a name="BKMK_EffectiveDateTime"></a> EffectiveDateTime

**Description**: Time that this rule takes effect, in local time.<br />
**DisplayName**: Effective Date Time<br />
**LogicalName**: effectivedatetime<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_StandardBias"></a> StandardBias

**Description**: Time bias in addition to the base bias for standard time.<br />
**DisplayName**: Standard Bias<br />
**LogicalName**: standardbias<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_StandardDay"></a> StandardDay

**Description**: Day of the month when standard time starts.<br />
**DisplayName**: Standard Day<br />
**LogicalName**: standardday<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 31<br />
**MinValue**: 0


### <a name="BKMK_StandardDayOfWeek"></a> StandardDayOfWeek

**Description**: Day of the week when standard time starts.<br />
**DisplayName**: Standard Day Of Week<br />
**LogicalName**: standarddayofweek<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 6<br />
**MinValue**: 0


### <a name="BKMK_StandardHour"></a> StandardHour

**Description**: Hour of the day when standard time starts.<br />
**DisplayName**: Standard Hour<br />
**LogicalName**: standardhour<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 23<br />
**MinValue**: 0


### <a name="BKMK_StandardMinute"></a> StandardMinute

**Description**: Minute of the hour when standard time starts.<br />
**DisplayName**: Standard Minute<br />
**LogicalName**: standardminute<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 59<br />
**MinValue**: 0


### <a name="BKMK_StandardMonth"></a> StandardMonth

**Description**: Month when standard time starts.<br />
**DisplayName**: Standard Month<br />
**LogicalName**: standardmonth<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 12<br />
**MinValue**: 0


### <a name="BKMK_StandardSecond"></a> StandardSecond

**Description**: Second of the Minute when standard time starts.<br />
**DisplayName**: Standard Second<br />
**LogicalName**: standardsecond<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 59<br />
**MinValue**: 0


### <a name="BKMK_StandardYear"></a> StandardYear

**Description**: Year when standard time starts.<br />
**DisplayName**: Standard Year<br />
**LogicalName**: standardyear<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 32768<br />
**MinValue**: 0


### <a name="BKMK_TimeZoneDefinitionId"></a> TimeZoneDefinitionId

**Description**: Unique identifier of the time zone definition.<br />
**DisplayName**: Time Zone Definition<br />
**LogicalName**: timezonedefinitionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: timezonedefinition


### <a name="BKMK_TimeZoneRuleId"></a> TimeZoneRuleId

**Description**: Unique identifier of the time zone rule.<br />
**DisplayName**: Time Zone Rule<br />
**LogicalName**: timezoneruleid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

**Description**: For internal use only<br />
**DisplayName**: Time Zone Rule Version Number<br />
**LogicalName**: timezoneruleversionnumber<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

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

**Description**: Unique identifier of the user who created the time zone rule.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the time zone rule was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the timezonerule.<br />
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

**Description**: Unique identifier of the user who last modified the time zone rule.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the time zone rule was modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the timezonerule.<br />
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


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization associated with the time zone rule.<br />
**DisplayName**: Organization<br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: organization


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


### <a name="BKMK_userentityinstancedata_timezonerule"></a> userentityinstancedata_timezonerule

Same as userentityinstancedata entity [userentityinstancedata_timezonerule](userentityinstancedata.md#BKMK_userentityinstancedata_timezonerule) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_timezonerule<br />
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

- [lk_timezonerule_createdby](#BKMK_lk_timezonerule_createdby)
- [lk_timezonerule_modifiedonbehalfby](#BKMK_lk_timezonerule_modifiedonbehalfby)
- [lk_timezonerule_modifiedby](#BKMK_lk_timezonerule_modifiedby)
- [lk_timezonerule_timezonedefinitionid](#BKMK_lk_timezonerule_timezonedefinitionid)
- [lk_timezonerule_createdonbehalfby](#BKMK_lk_timezonerule_createdonbehalfby)


### <a name="BKMK_lk_timezonerule_createdby"></a> lk_timezonerule_createdby

See systemuser Entity [lk_timezonerule_createdby](systemuser.md#BKMK_lk_timezonerule_createdby) One-To-Many relationship.

### <a name="BKMK_lk_timezonerule_modifiedonbehalfby"></a> lk_timezonerule_modifiedonbehalfby

See systemuser Entity [lk_timezonerule_modifiedonbehalfby](systemuser.md#BKMK_lk_timezonerule_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_timezonerule_modifiedby"></a> lk_timezonerule_modifiedby

See systemuser Entity [lk_timezonerule_modifiedby](systemuser.md#BKMK_lk_timezonerule_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_timezonerule_timezonedefinitionid"></a> lk_timezonerule_timezonedefinitionid

See timezonedefinition Entity [lk_timezonerule_timezonedefinitionid](timezonedefinition.md#BKMK_lk_timezonerule_timezonedefinitionid) One-To-Many relationship.

### <a name="BKMK_lk_timezonerule_createdonbehalfby"></a> lk_timezonerule_createdonbehalfby

See systemuser Entity [lk_timezonerule_createdonbehalfby](systemuser.md#BKMK_lk_timezonerule_createdonbehalfby) One-To-Many relationship.
timezonerule

