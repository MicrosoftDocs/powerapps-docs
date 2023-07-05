---
title: "TimeZoneLocalizedName table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the TimeZoneLocalizedName table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# TimeZoneLocalizedName table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Localized name of the time zone.


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Retrieve|GET /timezonelocalizednames(*timezonelocalizednameid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /timezonelocalizednames<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|TimeZoneLocalizedNames|
|DisplayCollectionName|Time Zone Localized Names|
|DisplayName|Time Zone Localized Name|
|EntitySetName|timezonelocalizednames|
|IsBPFEntity|False|
|LogicalCollectionName|timezonelocalizednames|
|LogicalName|timezonelocalizedname|
|OwnershipType|None|
|PrimaryIdAttribute|timezonelocalizednameid|
|PrimaryNameAttribute|userinterfacename|
|SchemaName|TimeZoneLocalizedName|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CultureId](#BKMK_CultureId)
- [DaylightName](#BKMK_DaylightName)
- [StandardName](#BKMK_StandardName)
- [TimeZoneDefinitionId](#BKMK_TimeZoneDefinitionId)
- [TimeZoneLocalizedNameId](#BKMK_TimeZoneLocalizedNameId)
- [UserInterfaceName](#BKMK_UserInterfaceName)


### <a name="BKMK_CultureId"></a> CultureId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the culture that the UI names are encoded in.|
|DisplayName|Culture|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|cultureid|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_DaylightName"></a> DaylightName

|Property|Value|
|--------|-----|
|Description|Name of the time zone for the daylight time.|
|DisplayName|Daylight Name|
|FormatName|Text|
|IsLocalizable|True|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|daylightname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_StandardName"></a> StandardName

|Property|Value|
|--------|-----|
|Description|Name of the time zone for the standard time.|
|DisplayName|Standard Name|
|FormatName|Text|
|IsLocalizable|True|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|standardname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_TimeZoneDefinitionId"></a> TimeZoneDefinitionId

|Property|Value|
|--------|-----|
|Description|Unique identifier of time zone definition entity instances.|
|DisplayName|Time Zone Definition|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezonedefinitionid|
|RequiredLevel|SystemRequired|
|Targets|timezonedefinition|
|Type|Lookup|


### <a name="BKMK_TimeZoneLocalizedNameId"></a> TimeZoneLocalizedNameId

|Property|Value|
|--------|-----|
|Description|Unique identifier of entity instances.|
|DisplayName|Time Zone Localized Name|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|timezonelocalizednameid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_UserInterfaceName"></a> UserInterfaceName

|Property|Value|
|--------|-----|
|Description|Unique display name for the time zone in the Microsoft Windows registry.|
|DisplayName|User Interface Name|
|FormatName|Text|
|IsLocalizable|True|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|userinterfacename|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|

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
|Description|Unique identifier of the user who created the record.|
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
|Description|Date and time when the record was created.|
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
|Description|Unique identifier of the delegate user who created the timezonelocalizedname.|
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
|Description|Unique identifier of the user who last modified the time zone localized name.|
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
|Description|Date and time when the record was modified.|
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
|Description|Unique identifier of the delegate user who last modified the timezonelocalizedname.|
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
|Description|Unique identifier of the organization associated with the time zone localized name.|
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

- [lk_timezonelocalizedname_modifiedby](#BKMK_lk_timezonelocalizedname_modifiedby)
- [lk_timezonelocalizedname_createdby](#BKMK_lk_timezonelocalizedname_createdby)
- [lk_timezonelocalizedname_modifiedonbehalfby](#BKMK_lk_timezonelocalizedname_modifiedonbehalfby)
- [lk_timezonelocalizedname_createdonbehalfby](#BKMK_lk_timezonelocalizedname_createdonbehalfby)
- [lk_timezonelocalizedname_timezonedefinitionid](#BKMK_lk_timezonelocalizedname_timezonedefinitionid)


### <a name="BKMK_lk_timezonelocalizedname_modifiedby"></a> lk_timezonelocalizedname_modifiedby

See the [lk_timezonelocalizedname_modifiedby](systemuser.md#BKMK_lk_timezonelocalizedname_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_timezonelocalizedname_createdby"></a> lk_timezonelocalizedname_createdby

See the [lk_timezonelocalizedname_createdby](systemuser.md#BKMK_lk_timezonelocalizedname_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_timezonelocalizedname_modifiedonbehalfby"></a> lk_timezonelocalizedname_modifiedonbehalfby

See the [lk_timezonelocalizedname_modifiedonbehalfby](systemuser.md#BKMK_lk_timezonelocalizedname_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_timezonelocalizedname_createdonbehalfby"></a> lk_timezonelocalizedname_createdonbehalfby

See the [lk_timezonelocalizedname_createdonbehalfby](systemuser.md#BKMK_lk_timezonelocalizedname_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_timezonelocalizedname_timezonedefinitionid"></a> lk_timezonelocalizedname_timezonedefinitionid

See the [lk_timezonelocalizedname_timezonedefinitionid](timezonedefinition.md#BKMK_lk_timezonelocalizedname_timezonedefinitionid) one-to-many relationship for the [timezonedefinition](timezonedefinition.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.timezonelocalizedname?text=timezonelocalizedname EntityType" />