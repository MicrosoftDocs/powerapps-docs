---
title: "OData v4 Data Source (msdyn_odatav4ds) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the OData v4 Data Source (msdyn_odatav4ds) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# OData v4 Data Source (msdyn_odatav4ds) table/entity reference (Microsoft Dataverse)

Data sources used by the OData v4 data provider to access data from an external web service.

## Messages

The following table lists the messages for the OData v4 Data Source (msdyn_odatav4ds) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Create`<br />Event: True |`POST` /msdyn_odatav4ds<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_odatav4ds(*msdyn_odatav4dsid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Retrieve`<br />Event: True |`GET` /msdyn_odatav4ds(*msdyn_odatav4dsid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_odatav4ds<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /msdyn_odatav4ds(*msdyn_odatav4dsid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_odatav4ds(*msdyn_odatav4dsid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the OData v4 Data Source (msdyn_odatav4ds) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **OData v4 Data Source** |
| **DisplayCollectionName** | **OData v4 Data Sources** |
| **SchemaName** | `msdyn_odatav4ds` |
| **CollectionSchemaName** | `msdyn_odatav4dses` |
| **EntitySetName** | `msdyn_odatav4ds`|
| **LogicalName** | `msdyn_odatav4ds` |
| **LogicalCollectionName** | `msdyn_odatav4dses` |
| **PrimaryIdAttribute** | `msdyn_odatav4dsid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [msdyn_description](#BKMK_msdyn_description)
- [msdyn_isparameter10header](#BKMK_msdyn_isparameter10header)
- [msdyn_isparameter1header](#BKMK_msdyn_isparameter1header)
- [msdyn_isparameter2header](#BKMK_msdyn_isparameter2header)
- [msdyn_isparameter3header](#BKMK_msdyn_isparameter3header)
- [msdyn_isparameter4header](#BKMK_msdyn_isparameter4header)
- [msdyn_isparameter5header](#BKMK_msdyn_isparameter5header)
- [msdyn_isparameter6header](#BKMK_msdyn_isparameter6header)
- [msdyn_isparameter7header](#BKMK_msdyn_isparameter7header)
- [msdyn_isparameter8header](#BKMK_msdyn_isparameter8header)
- [msdyn_isparameter9header](#BKMK_msdyn_isparameter9header)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_odatav4dsId](#BKMK_msdyn_odatav4dsId)
- [msdyn_paginationmode](#BKMK_msdyn_paginationmode)
- [msdyn_paginationtype](#BKMK_msdyn_paginationtype)
- [msdyn_parameter10name](#BKMK_msdyn_parameter10name)
- [msdyn_parameter10value](#BKMK_msdyn_parameter10value)
- [msdyn_parameter1name](#BKMK_msdyn_parameter1name)
- [msdyn_parameter1value](#BKMK_msdyn_parameter1value)
- [msdyn_parameter2name](#BKMK_msdyn_parameter2name)
- [msdyn_parameter2value](#BKMK_msdyn_parameter2value)
- [msdyn_parameter3name](#BKMK_msdyn_parameter3name)
- [msdyn_parameter3value](#BKMK_msdyn_parameter3value)
- [msdyn_parameter4name](#BKMK_msdyn_parameter4name)
- [msdyn_parameter4value](#BKMK_msdyn_parameter4value)
- [msdyn_parameter5name](#BKMK_msdyn_parameter5name)
- [msdyn_parameter5value](#BKMK_msdyn_parameter5value)
- [msdyn_parameter6name](#BKMK_msdyn_parameter6name)
- [msdyn_parameter6value](#BKMK_msdyn_parameter6value)
- [msdyn_parameter7name](#BKMK_msdyn_parameter7name)
- [msdyn_parameter7value](#BKMK_msdyn_parameter7value)
- [msdyn_parameter8name](#BKMK_msdyn_parameter8name)
- [msdyn_parameter8value](#BKMK_msdyn_parameter8value)
- [msdyn_parameter9name](#BKMK_msdyn_parameter9name)
- [msdyn_parameter9value](#BKMK_msdyn_parameter9value)
- [msdyn_returninlinecount](#BKMK_msdyn_returninlinecount)
- [msdyn_timeout](#BKMK_msdyn_timeout)
- [msdyn_uri](#BKMK_msdyn_uri)

### <a name="BKMK_msdyn_description"></a> msdyn_description

|Property|Value|
|---|---|
|Description|**Type additional information to describe this OData v4 data source. What environment does this data source target and what is the purpose of this system ?**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_description`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_msdyn_isparameter10header"></a> msdyn_isparameter10header

|Property|Value|
|---|---|
|Description|**Parameter10 Type**|
|DisplayName|**Parameter10 Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isparameter10header`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_isparameter10header`|
|DefaultValue|False|
|True Label|Header|
|False Label|Query String|

### <a name="BKMK_msdyn_isparameter1header"></a> msdyn_isparameter1header

|Property|Value|
|---|---|
|Description|**Parameter1 Type**|
|DisplayName|**Parameter1 Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isparameter1header`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_isparameter1header`|
|DefaultValue|False|
|True Label|Header|
|False Label|Query String|

### <a name="BKMK_msdyn_isparameter2header"></a> msdyn_isparameter2header

|Property|Value|
|---|---|
|Description|**Parameter2 Type**|
|DisplayName|**Parameter2 Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isparameter2header`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_isparameter2header`|
|DefaultValue|False|
|True Label|Header|
|False Label|Query String|

### <a name="BKMK_msdyn_isparameter3header"></a> msdyn_isparameter3header

|Property|Value|
|---|---|
|Description|**Parameter3 Type**|
|DisplayName|**Parameter3 Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isparameter3header`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_isparameter3header`|
|DefaultValue|False|
|True Label|Header|
|False Label|Query String|

### <a name="BKMK_msdyn_isparameter4header"></a> msdyn_isparameter4header

|Property|Value|
|---|---|
|Description|**Parameter4 Type**|
|DisplayName|**Parameter4 Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isparameter4header`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_isparameter4header`|
|DefaultValue|False|
|True Label|Header|
|False Label|Query String|

### <a name="BKMK_msdyn_isparameter5header"></a> msdyn_isparameter5header

|Property|Value|
|---|---|
|Description|**Parameter5 Type**|
|DisplayName|**Parameter5 Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isparameter5header`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_isparameter5header`|
|DefaultValue|False|
|True Label|Header|
|False Label|Query String|

### <a name="BKMK_msdyn_isparameter6header"></a> msdyn_isparameter6header

|Property|Value|
|---|---|
|Description|**Parameter6 Type**|
|DisplayName|**Parameter6 Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isparameter6header`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_isparameter6header`|
|DefaultValue|False|
|True Label|Header|
|False Label|Query String|

### <a name="BKMK_msdyn_isparameter7header"></a> msdyn_isparameter7header

|Property|Value|
|---|---|
|Description|**Parameter7 Type**|
|DisplayName|**Parameter7 Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isparameter7header`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_isparameter7header`|
|DefaultValue|False|
|True Label|Header|
|False Label|Query String|

### <a name="BKMK_msdyn_isparameter8header"></a> msdyn_isparameter8header

|Property|Value|
|---|---|
|Description|**Parameter8 Type**|
|DisplayName|**Parameter8 Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isparameter8header`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_isparameter8header`|
|DefaultValue|False|
|True Label|Header|
|False Label|Query String|

### <a name="BKMK_msdyn_isparameter9header"></a> msdyn_isparameter9header

|Property|Value|
|---|---|
|Description|**Parameter9 Type**|
|DisplayName|**Parameter9 Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isparameter9header`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_isparameter9header`|
|DefaultValue|False|
|True Label|Header|
|False Label|Query String|

### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|---|---|
|Description|**Name of the OData v4 data source. This name appears in the data source drop-down list when creating a new entity.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_odatav4dsId"></a> msdyn_odatav4dsId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**OData v4 Data Source**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_odatav4dsid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_paginationmode"></a> msdyn_paginationmode

|Property|Value|
|---|---|
|Description||
|DisplayName|**Pagination Mode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_paginationmode`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`new_odatadatasource_paginationmode`|
|DefaultValue|False|
|True Label|Server-side Paging|
|False Label|Client-side Paging|

### <a name="BKMK_msdyn_paginationtype"></a> msdyn_paginationtype

|Property|Value|
|---|---|
|Description||
|DisplayName|**Pagination Mode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_paginationtype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`new_odatadatasource_paginationtype`|

#### msdyn_paginationtype Choices/Options

|Value|Label|
|---|---|
|0|**Client-side Paging**|
|1|**Server-side Paging**|

### <a name="BKMK_msdyn_parameter10name"></a> msdyn_parameter10name

|Property|Value|
|---|---|
|Description||
|DisplayName|**parameter10name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parameter10name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_msdyn_parameter10value"></a> msdyn_parameter10value

|Property|Value|
|---|---|
|Description||
|DisplayName|**parameter10value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parameter10value`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_msdyn_parameter1name"></a> msdyn_parameter1name

|Property|Value|
|---|---|
|Description||
|DisplayName|**parameter1name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parameter1name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_msdyn_parameter1value"></a> msdyn_parameter1value

|Property|Value|
|---|---|
|Description||
|DisplayName|**parameter1value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parameter1value`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_msdyn_parameter2name"></a> msdyn_parameter2name

|Property|Value|
|---|---|
|Description||
|DisplayName|**parameter2name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parameter2name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_msdyn_parameter2value"></a> msdyn_parameter2value

|Property|Value|
|---|---|
|Description||
|DisplayName|**parameter2value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parameter2value`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_msdyn_parameter3name"></a> msdyn_parameter3name

|Property|Value|
|---|---|
|Description||
|DisplayName|**parameter3name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parameter3name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_msdyn_parameter3value"></a> msdyn_parameter3value

|Property|Value|
|---|---|
|Description||
|DisplayName|**parameter3value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parameter3value`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_msdyn_parameter4name"></a> msdyn_parameter4name

|Property|Value|
|---|---|
|Description||
|DisplayName|**parameter4name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parameter4name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_msdyn_parameter4value"></a> msdyn_parameter4value

|Property|Value|
|---|---|
|Description||
|DisplayName|**parameter4value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parameter4value`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_msdyn_parameter5name"></a> msdyn_parameter5name

|Property|Value|
|---|---|
|Description||
|DisplayName|**parameter5name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parameter5name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_msdyn_parameter5value"></a> msdyn_parameter5value

|Property|Value|
|---|---|
|Description||
|DisplayName|**parameter5value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parameter5value`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_msdyn_parameter6name"></a> msdyn_parameter6name

|Property|Value|
|---|---|
|Description||
|DisplayName|**parameter6name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parameter6name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_msdyn_parameter6value"></a> msdyn_parameter6value

|Property|Value|
|---|---|
|Description||
|DisplayName|**parameter6value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parameter6value`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_msdyn_parameter7name"></a> msdyn_parameter7name

|Property|Value|
|---|---|
|Description||
|DisplayName|**parameter7name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parameter7name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_msdyn_parameter7value"></a> msdyn_parameter7value

|Property|Value|
|---|---|
|Description||
|DisplayName|**parameter7value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parameter7value`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_msdyn_parameter8name"></a> msdyn_parameter8name

|Property|Value|
|---|---|
|Description||
|DisplayName|**parameter8name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parameter8name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_msdyn_parameter8value"></a> msdyn_parameter8value

|Property|Value|
|---|---|
|Description||
|DisplayName|**parameter8value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parameter8value`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_msdyn_parameter9name"></a> msdyn_parameter9name

|Property|Value|
|---|---|
|Description||
|DisplayName|**parameter9name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parameter9name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_msdyn_parameter9value"></a> msdyn_parameter9value

|Property|Value|
|---|---|
|Description||
|DisplayName|**parameter9value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_parameter9value`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_msdyn_returninlinecount"></a> msdyn_returninlinecount

|Property|Value|
|---|---|
|Description||
|DisplayName|**Return Inline Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_returninlinecount`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`new_odatadatasource_returninlinecount`|
|DefaultValue|True|
|True Label|True|
|False Label|False|

### <a name="BKMK_msdyn_timeout"></a> msdyn_timeout

|Property|Value|
|---|---|
|Description|**Amount of time to wait, in seconds, before timing out an OData v4 request.**|
|DisplayName|**Timeout**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_timeout`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|120|
|MinValue|0|

### <a name="BKMK_msdyn_uri"></a> msdyn_uri

|Property|Value|
|---|---|
|Description|**URL of the OData v4 web service endpoint this data source will target.**|
|DisplayName|**URL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_uri`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|




### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_odatav4ds?displayProperty=fullName>
