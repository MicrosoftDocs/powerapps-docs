---
title: "mobileofflineprofileitemfilter table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the mobileofflineprofileitemfilter table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# mobileofflineprofileitemfilter table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the mobileofflineprofileitemfilter table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mobileofflineprofileitemfilters<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mobileofflineprofileitemfilters(*mobileofflineprofileitemfilterid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Retrieve`<br />Event: True |`GET` /mobileofflineprofileitemfilters(*mobileofflineprofileitemfilterid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /mobileofflineprofileitemfilters<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /mobileofflineprofileitemfilters(*mobileofflineprofileitemfilterid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /mobileofflineprofileitemfilters(*mobileofflineprofileitemfilterid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mobileofflineprofileitemfilters(*mobileofflineprofileitemfilterid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the mobileofflineprofileitemfilter table.

|Property|Value|
| --- | --- |
| **DisplayName** | **MobileOfflineProfileItemFilter** |
| **DisplayCollectionName** | **MobileOfflineProfileItemFilters** |
| **SchemaName** | `mobileofflineprofileitemfilter` |
| **CollectionSchemaName** | `mobileofflineprofileitemfilters` |
| **EntitySetName** | `mobileofflineprofileitemfilters`|
| **LogicalName** | `mobileofflineprofileitemfilter` |
| **LogicalCollectionName** | `mobileofflineprofileitemfilters` |
| **PrimaryIdAttribute** | `mobileofflineprofileitemfilterid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

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
|---|---|
|Description||
|DisplayName|**FetchXML**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`fetchxml`|
|RequiredLevel|SystemRequired|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_IsActivity"></a> IsActivity

|Property|Value|
|---|---|
|Description||
|DisplayName|**IsActivity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isactivity`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mobileofflineprofileitemfilter_isactivity`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsIntersect"></a> IsIntersect

|Property|Value|
|---|---|
|Description||
|DisplayName|**IsIntersect**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isintersect`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mobileofflineprofileitemfilter_isintersect`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mobileofflineprofileid"></a> mobileofflineprofileid

|Property|Value|
|---|---|
|Description|**Unique identifier for Mobile Offline Profile associated with MobileOfflineProfileItemFilter.**|
|DisplayName|**MobileOfflineProfile**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mobileofflineprofileid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|mobileofflineprofile|

### <a name="BKMK_mobileofflineprofileitemfilterId"></a> mobileofflineprofileitemfilterId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**MobileOfflineProfileItemFilter**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mobileofflineprofileitemfilterid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_mobileofflineprofileitemid"></a> mobileofflineprofileitemid

|Property|Value|
|---|---|
|Description||
|DisplayName|**MobileOfflineProfileItemId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mobileofflineprofileitemid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|64|

### <a name="BKMK_offlinesql"></a> offlinesql

|Property|Value|
|---|---|
|Description||
|DisplayName|**OfflineSQL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`offlinesql`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_outerFetchXml"></a> outerFetchXml

|Property|Value|
|---|---|
|Description||
|DisplayName|**OuterFetchXML**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`outerfetchXml`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_returnedtypecode"></a> returnedtypecode

|Property|Value|
|---|---|
|Description||
|DisplayName|**ReturnedTypecode**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`returnedtypecode`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_subtype"></a> subtype

|Property|Value|
|---|---|
|Description||
|DisplayName|**Subtype**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`subtype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`mobileofflineprofileitemfilter_subtype`|

#### subtype Choices/Options

|Value|Label|
|---|---|
|0|**CUD\_IN**|
|1|**RELATED\_CUD\_IN**|
|2|**SHARED\_IN**|
|3|**RELATED\_SHARED\_IN**|
|4|**CUD\_OUT**|
|5|**FULL\_SYNC**|
|6|**RELATED\_ENTITIES**|
|7|**RELATED\_INTERSECT\_ENTITIES**|

### <a name="BKMK_type"></a> type

|Property|Value|
|---|---|
|Description||
|DisplayName|**Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`type`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`mobileofflineprofileitemfilter_type`|

#### type Choices/Options

|Value|Label|
|---|---|
|0|**DELTA\_IN**|
|1|**DELTA\_OUT**|
|2|**FULL\_SYNC**|
|3|**TOP\_1**|
|4|**RELATED\_ENTITIES**|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedOn](#BKMK_CreatedOn)
- [ModifiedOn](#BKMK_ModifiedOn)
- [OrganizationId](#BKMK_OrganizationId)
- [versionnumber](#BKMK_versionnumber)

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

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier for the organization**|
|DisplayName|**Organization Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets||

### <a name="BKMK_versionnumber"></a> versionnumber

|Property|Value|
|---|---|
|Description|**Version number.**|
|DisplayName|**Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

### <a name="BKMK_mobileofflineprofile_mobileofflineprofile"></a> mobileofflineprofile_mobileofflineprofile

One-To-Many Relationship: [mobileofflineprofile mobileofflineprofile_mobileofflineprofile](mobileofflineprofile.md#BKMK_mobileofflineprofile_mobileofflineprofile)

|Property|Value|
|---|---|
|ReferencedEntity|`mobileofflineprofile`|
|ReferencedAttribute|`mobileofflineprofileid`|
|ReferencingAttribute|`mobileofflineprofileid`|
|ReferencingEntityNavigationPropertyName|`mobileofflineprofileid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mobileofflineprofileitemfilter?displayProperty=fullName>
