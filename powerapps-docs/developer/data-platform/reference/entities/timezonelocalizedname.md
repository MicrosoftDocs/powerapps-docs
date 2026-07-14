---
title: "Time Zone Localized Name (TimeZoneLocalizedName) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Time Zone Localized Name (TimeZoneLocalizedName) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Time Zone Localized Name (TimeZoneLocalizedName) table/entity reference (Microsoft Dataverse)

Localized name of the time zone.

## Messages

The following table lists the messages for the Time Zone Localized Name (TimeZoneLocalizedName) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /timezonelocalizednames(*timezonelocalizednameid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /timezonelocalizednames<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Time Zone Localized Name (TimeZoneLocalizedName) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Time Zone Localized Name** |
| **DisplayCollectionName** | **Time Zone Localized Names** |
| **SchemaName** | `TimeZoneLocalizedName` |
| **CollectionSchemaName** | `TimeZoneLocalizedNames` |
| **EntitySetName** | `timezonelocalizednames`|
| **LogicalName** | `timezonelocalizedname` |
| **LogicalCollectionName** | `timezonelocalizednames` |
| **PrimaryIdAttribute** | `timezonelocalizednameid` |
| **PrimaryNameAttribute** |`userinterfacename` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

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
|---|---|
|Description|**Unique identifier of the culture that the UI names are encoded in.**|
|DisplayName|**Culture**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cultureid`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_DaylightName"></a> DaylightName

|Property|Value|
|---|---|
|Description|**Name of the time zone for the daylight time.**|
|DisplayName|**Daylight Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`daylightname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|100|

### <a name="BKMK_StandardName"></a> StandardName

|Property|Value|
|---|---|
|Description|**Name of the time zone for the standard time.**|
|DisplayName|**Standard Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`standardname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|100|

### <a name="BKMK_TimeZoneDefinitionId"></a> TimeZoneDefinitionId

|Property|Value|
|---|---|
|Description|**Unique identifier of time zone definition entity instances.**|
|DisplayName|**Time Zone Definition**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonedefinitionid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|timezonedefinition|

### <a name="BKMK_TimeZoneLocalizedNameId"></a> TimeZoneLocalizedNameId

|Property|Value|
|---|---|
|Description|**Unique identifier of entity instances.**|
|DisplayName|**Time Zone Localized Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonelocalizednameid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_UserInterfaceName"></a> UserInterfaceName

|Property|Value|
|---|---|
|Description|**Unique display name for the time zone in the Microsoft Windows registry.**|
|DisplayName|**User Interface Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`userinterfacename`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|100|


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
|Description|**Unique identifier of the user who created the record.**|
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
|Description|**Date and time when the record was created.**|
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
|Description|**Unique identifier of the delegate user who created the timezonelocalizedname.**|
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
|Description|**Unique identifier of the user who last modified the time zone localized name.**|
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
|Description|**Date and time when the record was modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the timezonelocalizedname.**|
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
|Description|**Unique identifier of the organization associated with the time zone localized name.**|
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

- [lk_timezonelocalizedname_createdby](#BKMK_lk_timezonelocalizedname_createdby)
- [lk_timezonelocalizedname_createdonbehalfby](#BKMK_lk_timezonelocalizedname_createdonbehalfby)
- [lk_timezonelocalizedname_modifiedby](#BKMK_lk_timezonelocalizedname_modifiedby)
- [lk_timezonelocalizedname_modifiedonbehalfby](#BKMK_lk_timezonelocalizedname_modifiedonbehalfby)
- [lk_timezonelocalizedname_timezonedefinitionid](#BKMK_lk_timezonelocalizedname_timezonedefinitionid)

### <a name="BKMK_lk_timezonelocalizedname_createdby"></a> lk_timezonelocalizedname_createdby

One-To-Many Relationship: [systemuser lk_timezonelocalizedname_createdby](systemuser.md#BKMK_lk_timezonelocalizedname_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_timezonelocalizedname_createdonbehalfby"></a> lk_timezonelocalizedname_createdonbehalfby

One-To-Many Relationship: [systemuser lk_timezonelocalizedname_createdonbehalfby](systemuser.md#BKMK_lk_timezonelocalizedname_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_timezonelocalizedname_modifiedby"></a> lk_timezonelocalizedname_modifiedby

One-To-Many Relationship: [systemuser lk_timezonelocalizedname_modifiedby](systemuser.md#BKMK_lk_timezonelocalizedname_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_timezonelocalizedname_modifiedonbehalfby"></a> lk_timezonelocalizedname_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_timezonelocalizedname_modifiedonbehalfby](systemuser.md#BKMK_lk_timezonelocalizedname_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_timezonelocalizedname_timezonedefinitionid"></a> lk_timezonelocalizedname_timezonedefinitionid

One-To-Many Relationship: [timezonedefinition lk_timezonelocalizedname_timezonedefinitionid](timezonedefinition.md#BKMK_lk_timezonelocalizedname_timezonedefinitionid)

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
<xref:Microsoft.Dynamics.CRM.timezonelocalizedname?displayProperty=fullName>
