---
title: "TimeZoneDefinition table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the TimeZoneDefinition table/entity."
ms.date: 05/20/2021
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

# TimeZoneDefinition table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Time zone definition, including name and time zone code.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|GetAllTimeZonesWithDisplayName|<xref href="Microsoft.Dynamics.CRM.GetAllTimeZonesWithDisplayName?text=GetAllTimeZonesWithDisplayName Function" />|<xref:Microsoft.Crm.Sdk.Messages.GetAllTimeZonesWithDisplayNameRequest>|
|GetTimeZoneCodeByLocalizedName|<xref href="Microsoft.Dynamics.CRM.GetTimeZoneCodeByLocalizedName?text=GetTimeZoneCodeByLocalizedName Function" />|<xref:Microsoft.Crm.Sdk.Messages.GetTimeZoneCodeByLocalizedNameRequest>|
|LocalTimeFromUtcTime|<xref href="Microsoft.Dynamics.CRM.LocalTimeFromUtcTime?text=LocalTimeFromUtcTime Function" />|<xref:Microsoft.Crm.Sdk.Messages.LocalTimeFromUtcTimeRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/timezonedefinitions(*timezonedefinitionid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/timezonedefinitions<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|UtcTimeFromLocalTime||<xref:Microsoft.Crm.Sdk.Messages.UtcTimeFromLocalTimeRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|TimeZoneDefinitions|
|DisplayCollectionName|Time Zone Definitions|
|DisplayName|Time Zone Definition|
|EntitySetName|timezonedefinitions|
|IsBPFEntity|False|
|LogicalCollectionName|timezonedefinitions|
|LogicalName|timezonedefinition|
|OwnershipType|None|
|PrimaryIdAttribute|timezonedefinitionid|
|PrimaryNameAttribute|userinterfacename|
|SchemaName|TimeZoneDefinition|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description|Base time bias of the time zone.|
|DisplayName|Bias|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|bias|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_DaylightName"></a> DaylightName

|Property|Value|
|--------|-----|
|Description|Time zone name for the daylight time.|
|DisplayName|Daylight Name|
|FormatName|Text|
|IsLocalizable|True|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|daylightname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RetiredOrder"></a> RetiredOrder

|Property|Value|
|--------|-----|
|Description|Order an entry for a time zone definition is retired. 0 for the latest entry.|
|DisplayName|Retired Order|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|retiredorder|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_StandardName"></a> StandardName

|Property|Value|
|--------|-----|
|Description|Time zone name for the standard time.|
|DisplayName|Standard Name|
|FormatName|Text|
|IsLocalizable|True|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|standardname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_TimeZoneCode"></a> TimeZoneCode

|Property|Value|
|--------|-----|
|Description|Time zone identification code.|
|DisplayName|Time Zone Code|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|timezonecode|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TimeZoneDefinitionId"></a> TimeZoneDefinitionId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the time zone record.|
|DisplayName|Time Zone Definition|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|timezonedefinitionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_UserInterfaceName"></a> UserInterfaceName

|Property|Value|
|--------|-----|
|Description|Display name for the time zone in the Microsoft Windows registry.|
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
|Description|Unique identifier of the user who created the time zone record.|
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
|Description|Date and time when the time zone record was created.|
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
|Description|Unique identifier of the delegate user who created the timezonedefinition.|
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
|Description|Unique identifier of the user who last modified the time zone record.|
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
|Description|Date and time when the time zone record was modified.|
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
|Description|Unique identifier of the delegate user who last modified the timezonedefinition.|
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
|Description|Unique identifier of the organization associated with the time zone definition.|
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

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [lk_timezonerule_timezonedefinitionid](#BKMK_lk_timezonerule_timezonedefinitionid)
- [lk_timezonelocalizedname_timezonedefinitionid](#BKMK_lk_timezonelocalizedname_timezonedefinitionid)


### <a name="BKMK_lk_timezonerule_timezonedefinitionid"></a> lk_timezonerule_timezonedefinitionid

Same as timezonerule table [lk_timezonerule_timezonedefinitionid](timezonerule.md#BKMK_lk_timezonerule_timezonedefinitionid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|timezonerule|
|ReferencingAttribute|timezonedefinitionid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_timezonerule_timezonedefinitionid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_timezonelocalizedname_timezonedefinitionid"></a> lk_timezonelocalizedname_timezonedefinitionid

Same as timezonelocalizedname table [lk_timezonelocalizedname_timezonedefinitionid](timezonelocalizedname.md#BKMK_lk_timezonelocalizedname_timezonedefinitionid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|timezonelocalizedname|
|ReferencingAttribute|timezonedefinitionid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_timezonelocalizedname_timezonedefinitionid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_timezonedefinition_modifiedby](#BKMK_lk_timezonedefinition_modifiedby)
- [lk_timezonedefinition_modifiedonbehalfby](#BKMK_lk_timezonedefinition_modifiedonbehalfby)
- [lk_timezonedefinition_createdonbehalfby](#BKMK_lk_timezonedefinition_createdonbehalfby)
- [lk_timezonedefinition_createdby](#BKMK_lk_timezonedefinition_createdby)


### <a name="BKMK_lk_timezonedefinition_modifiedby"></a> lk_timezonedefinition_modifiedby

See systemuser Table [lk_timezonedefinition_modifiedby](systemuser.md#BKMK_lk_timezonedefinition_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_timezonedefinition_modifiedonbehalfby"></a> lk_timezonedefinition_modifiedonbehalfby

See systemuser Table [lk_timezonedefinition_modifiedonbehalfby](systemuser.md#BKMK_lk_timezonedefinition_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_timezonedefinition_createdonbehalfby"></a> lk_timezonedefinition_createdonbehalfby

See systemuser Table [lk_timezonedefinition_createdonbehalfby](systemuser.md#BKMK_lk_timezonedefinition_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_timezonedefinition_createdby"></a> lk_timezonedefinition_createdby

See systemuser Table [lk_timezonedefinition_createdby](systemuser.md#BKMK_lk_timezonedefinition_createdby) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.timezonedefinition?text=timezonedefinition EntityType" />