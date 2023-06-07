---
title: "mobileofflineprofileitemfilter table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the mobileofflineprofileitemfilter table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# mobileofflineprofileitemfilter table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: MobileOfflineDirectDeviceSync Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST /mobileofflineprofileitemfilters<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mobileofflineprofileitemfilters(*mobileofflineprofileitemfilterid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|Retrieve|GET /mobileofflineprofileitemfilters(*mobileofflineprofileitemfilterid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /mobileofflineprofileitemfilters<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|SetState|PATCH /mobileofflineprofileitemfilters(*mobileofflineprofileitemfilterid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /mobileofflineprofileitemfilters(*mobileofflineprofileitemfilterid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mobileofflineprofileitemfilters|
|DisplayCollectionName|MobileOfflineProfileItemFilters|
|DisplayName|MobileOfflineProfileItemFilter|
|EntitySetName|mobileofflineprofileitemfilters|
|IsBPFEntity|False|
|LogicalCollectionName|mobileofflineprofileitemfilters|
|LogicalName|mobileofflineprofileitemfilter|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mobileofflineprofileitemfilterid|
|PrimaryNameAttribute|name|
|SchemaName|mobileofflineprofileitemfilter|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [fetchxml](#BKMK_fetchxml)
- [IsActivity](#BKMK_IsActivity)
- [IsIntersect](#BKMK_IsIntersect)
- [mobileofflineprofileid](#BKMK_mobileofflineprofileid)
- [mobileofflineprofileitemfilterId](#BKMK_mobileofflineprofileitemfilterId)
- [mobileofflineprofileitemid](#BKMK_mobileofflineprofileitemid)
- [Name](#BKMK_Name)
- [offlinesql](#BKMK_offlinesql)
- [outerFetchXml](#BKMK_outerFetchXml)
- [returnedtypecode](#BKMK_returnedtypecode)
- [subtype](#BKMK_subtype)
- [type](#BKMK_type)


### <a name="BKMK_fetchxml"></a> fetchxml

|Property|Value|
|--------|-----|
|Description||
|DisplayName|FetchXML|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|fetchxml|
|MaxLength|1048576|
|RequiredLevel|SystemRequired|
|Type|Memo|


### <a name="BKMK_IsActivity"></a> IsActivity

|Property|Value|
|--------|-----|
|Description||
|DisplayName|IsActivity|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isactivity|
|RequiredLevel|None|
|Type|Boolean|

#### IsActivity Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_IsIntersect"></a> IsIntersect

|Property|Value|
|--------|-----|
|Description||
|DisplayName|IsIntersect|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isintersect|
|RequiredLevel|None|
|Type|Boolean|

#### IsIntersect Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mobileofflineprofileid"></a> mobileofflineprofileid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Mobile Offline Profile associated with MobileOfflineProfileItemFilter.|
|DisplayName|MobileOfflineProfile|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mobileofflineprofileid|
|RequiredLevel|SystemRequired|
|Targets|mobileofflineprofile|
|Type|Lookup|


### <a name="BKMK_mobileofflineprofileitemfilterId"></a> mobileofflineprofileitemfilterId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|MobileOfflineProfileItemFilter|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mobileofflineprofileitemfilterid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_mobileofflineprofileitemid"></a> mobileofflineprofileitemid

|Property|Value|
|--------|-----|
|Description||
|DisplayName|MobileOfflineProfileItemId|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mobileofflineprofileitemid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|name|
|MaxLength|64|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_offlinesql"></a> offlinesql

|Property|Value|
|--------|-----|
|Description||
|DisplayName|OfflineSQL|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|offlinesql|
|MaxLength|1048576|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_outerFetchXml"></a> outerFetchXml

|Property|Value|
|--------|-----|
|Description||
|DisplayName|OuterFetchXML|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|outerfetchXml|
|MaxLength|1048576|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_returnedtypecode"></a> returnedtypecode

|Property|Value|
|--------|-----|
|Description||
|DisplayName|ReturnedTypecode|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|returnedtypecode|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_subtype"></a> subtype

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Subtype|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|subtype|
|RequiredLevel|None|
|Type|Picklist|

#### subtype Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|CUD_IN||
|1|RELATED_CUD_IN||
|2|SHARED_IN||
|3|RELATED_SHARED_IN||
|4|CUD_OUT||
|5|FULL_SYNC||
|6|RELATED_ENTITIES||
|7|RELATED_INTERSECT_ENTITIES||



### <a name="BKMK_type"></a> type

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|type|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### type Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|DELTA_IN||
|1|DELTA_OUT||
|2|FULL_SYNC||
|3|TOP_1||
|4|RELATED_ENTITIES||


<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedOn](#BKMK_CreatedOn)
- [mobileofflineprofileidName](#BKMK_mobileofflineprofileidName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [OrganizationId](#BKMK_OrganizationId)
- [versionnumber](#BKMK_versionnumber)


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


### <a name="BKMK_mobileofflineprofileidName"></a> mobileofflineprofileidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mobileofflineprofileidname|
|MaxLength|255|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier for the organization|
|DisplayName|Organization Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|None|
|Targets||
|Type|Lookup|


### <a name="BKMK_versionnumber"></a> versionnumber

|Property|Value|
|--------|-----|
|Description|Version number.|
|DisplayName|Version Number|
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


### <a name="BKMK_mobileofflineprofile_mobileofflineprofile"></a> mobileofflineprofile_mobileofflineprofile

**Added by**: System Solution Solution

See the [mobileofflineprofile_mobileofflineprofile](mobileofflineprofile.md#BKMK_mobileofflineprofile_mobileofflineprofile) one-to-many relationship for the [mobileofflineprofile](mobileofflineprofile.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mobileofflineprofileitemfilter?text=mobileofflineprofileitemfilter EntityType" />