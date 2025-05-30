---
title: "Time Zone Definition (TimeZoneDefinition) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Time Zone Definition (TimeZoneDefinition) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Time Zone Definition (TimeZoneDefinition) table/entity reference (Microsoft Dataverse)

Time zone definition, including name and time zone code.

## Messages

The following table lists the messages for the Time Zone Definition (TimeZoneDefinition) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GetAllTimeZonesWithDisplayName`<br />Event: False |<xref:Microsoft.Dynamics.CRM.GetAllTimeZonesWithDisplayName?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GetAllTimeZonesWithDisplayNameRequest>|
| `GetTimeZoneCodeByLocalizedName`<br />Event: False |<xref:Microsoft.Dynamics.CRM.GetTimeZoneCodeByLocalizedName?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GetTimeZoneCodeByLocalizedNameRequest>|
| `LocalTimeFromUtcTime`<br />Event: False |<xref:Microsoft.Dynamics.CRM.LocalTimeFromUtcTime?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.LocalTimeFromUtcTimeRequest>|
| `Retrieve`<br />Event: False |`GET` /timezonedefinitions(*timezonedefinitionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /timezonedefinitions<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `UtcTimeFromLocalTime`<br />Event: False | |<xref:Microsoft.Crm.Sdk.Messages.UtcTimeFromLocalTimeRequest>|

## Properties

The following table lists selected properties for the Time Zone Definition (TimeZoneDefinition) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Time Zone Definition** |
| **DisplayCollectionName** | **Time Zone Definitions** |
| **SchemaName** | `TimeZoneDefinition` |
| **CollectionSchemaName** | `TimeZoneDefinitions` |
| **EntitySetName** | `timezonedefinitions`|
| **LogicalName** | `timezonedefinition` |
| **LogicalCollectionName** | `timezonedefinitions` |
| **PrimaryIdAttribute** | `timezonedefinitionid` |
| **PrimaryNameAttribute** |`userinterfacename` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Bias](#BKMK_Bias)
- [DaylightName](#BKMK_DaylightName)
- [RetiredOrder](#BKMK_RetiredOrder)
- [StandardName](#BKMK_StandardName)
- [TimeZoneCode](#BKMK_TimeZoneCode)
- [TimeZoneDefinitionId](#BKMK_TimeZoneDefinitionId)
- [UserInterfaceName](#BKMK_UserInterfaceName)

### <a name="BKMK_Bias"></a> Bias

|Property|Value|
|---|---|
|Description|**Base time bias of the time zone.**|
|DisplayName|**Bias**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`bias`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_DaylightName"></a> DaylightName

|Property|Value|
|---|---|
|Description|**Time zone name for the daylight time.**|
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

### <a name="BKMK_RetiredOrder"></a> RetiredOrder

|Property|Value|
|---|---|
|Description|**Order an entry for a time zone definition is retired. 0 for the latest entry.**|
|DisplayName|**Retired Order**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`retiredorder`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_StandardName"></a> StandardName

|Property|Value|
|---|---|
|Description|**Time zone name for the standard time.**|
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

### <a name="BKMK_TimeZoneCode"></a> TimeZoneCode

|Property|Value|
|---|---|
|Description|**Time zone identification code.**|
|DisplayName|**Time Zone Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`timezonecode`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_TimeZoneDefinitionId"></a> TimeZoneDefinitionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the time zone record.**|
|DisplayName|**Time Zone Definition**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezonedefinitionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_UserInterfaceName"></a> UserInterfaceName

|Property|Value|
|---|---|
|Description|**Display name for the time zone in the Microsoft Windows registry.**|
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
|Description|**Unique identifier of the user who created the time zone record.**|
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
|Description|**Date and time when the time zone record was created.**|
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
|Description|**Unique identifier of the delegate user who created the timezonedefinition.**|
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
|Description|**Unique identifier of the user who last modified the time zone record.**|
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
|Description|**Date and time when the time zone record was modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the timezonedefinition.**|
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
|Description|**Unique identifier of the organization associated with the time zone definition.**|
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

- [lk_timezonedefinition_createdby](#BKMK_lk_timezonedefinition_createdby)
- [lk_timezonedefinition_createdonbehalfby](#BKMK_lk_timezonedefinition_createdonbehalfby)
- [lk_timezonedefinition_modifiedby](#BKMK_lk_timezonedefinition_modifiedby)
- [lk_timezonedefinition_modifiedonbehalfby](#BKMK_lk_timezonedefinition_modifiedonbehalfby)

### <a name="BKMK_lk_timezonedefinition_createdby"></a> lk_timezonedefinition_createdby

One-To-Many Relationship: [systemuser lk_timezonedefinition_createdby](systemuser.md#BKMK_lk_timezonedefinition_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_timezonedefinition_createdonbehalfby"></a> lk_timezonedefinition_createdonbehalfby

One-To-Many Relationship: [systemuser lk_timezonedefinition_createdonbehalfby](systemuser.md#BKMK_lk_timezonedefinition_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_timezonedefinition_modifiedby"></a> lk_timezonedefinition_modifiedby

One-To-Many Relationship: [systemuser lk_timezonedefinition_modifiedby](systemuser.md#BKMK_lk_timezonedefinition_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_timezonedefinition_modifiedonbehalfby"></a> lk_timezonedefinition_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_timezonedefinition_modifiedonbehalfby](systemuser.md#BKMK_lk_timezonedefinition_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [lk_timezonelocalizedname_timezonedefinitionid](#BKMK_lk_timezonelocalizedname_timezonedefinitionid)
- [lk_timezonerule_timezonedefinitionid](#BKMK_lk_timezonerule_timezonedefinitionid)

### <a name="BKMK_lk_timezonelocalizedname_timezonedefinitionid"></a> lk_timezonelocalizedname_timezonedefinitionid

Many-To-One Relationship: [timezonelocalizedname lk_timezonelocalizedname_timezonedefinitionid](timezonelocalizedname.md#BKMK_lk_timezonelocalizedname_timezonedefinitionid)

|Property|Value|
|---|---|
|ReferencingEntity|`timezonelocalizedname`|
|ReferencingAttribute|`timezonedefinitionid`|
|ReferencedEntityNavigationPropertyName|`lk_timezonelocalizedname_timezonedefinitionid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_timezonerule_timezonedefinitionid"></a> lk_timezonerule_timezonedefinitionid

Many-To-One Relationship: [timezonerule lk_timezonerule_timezonedefinitionid](timezonerule.md#BKMK_lk_timezonerule_timezonedefinitionid)

|Property|Value|
|---|---|
|ReferencingEntity|`timezonerule`|
|ReferencingAttribute|`timezonedefinitionid`|
|ReferencedEntityNavigationPropertyName|`lk_timezonerule_timezonedefinitionid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.timezonedefinition?displayProperty=fullName>
