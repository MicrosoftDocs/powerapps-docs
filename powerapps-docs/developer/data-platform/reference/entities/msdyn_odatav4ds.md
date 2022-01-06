---
title: "msdyn_odatav4ds table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the msdyn_odatav4ds table/entity."
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

# msdyn_odatav4ds table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Data sources used by the OData v4 data provider to access data from an external web service.

**Added by**: OData v4 Data Provider Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/msdyn_odatav4ds<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/msdyn_odatav4ds(*msdyn_odatav4dsid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/msdyn_odatav4ds(*msdyn_odatav4dsid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/msdyn_odatav4ds<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/msdyn_odatav4ds(*msdyn_odatav4dsid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msdyn_odatav4dses|
|DisplayCollectionName|OData v4 Data Sources|
|DisplayName|OData v4 Data Source|
|EntitySetName|msdyn_odatav4ds|
|IsBPFEntity|False|
|LogicalCollectionName|msdyn_odatav4dses|
|LogicalName|msdyn_odatav4ds|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|msdyn_odatav4dsid|
|PrimaryNameAttribute|msdyn_name|
|SchemaName|msdyn_odatav4ds|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description|Type additional information to describe this OData v4 data source. What environment does this data source target and what is the purpose of this system ?|
|DisplayName|Description|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_description|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_isparameter10header"></a> msdyn_isparameter10header

|Property|Value|
|--------|-----|
|Description|Parameter10 Type|
|DisplayName|Parameter10 Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isparameter10header|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_isparameter10header Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Header|
|0|Query String|

**DefaultValue**: False



### <a name="BKMK_msdyn_isparameter1header"></a> msdyn_isparameter1header

|Property|Value|
|--------|-----|
|Description|Parameter1 Type|
|DisplayName|Parameter1 Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isparameter1header|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_isparameter1header Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Header|
|0|Query String|

**DefaultValue**: False



### <a name="BKMK_msdyn_isparameter2header"></a> msdyn_isparameter2header

|Property|Value|
|--------|-----|
|Description|Parameter2 Type|
|DisplayName|Parameter2 Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isparameter2header|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_isparameter2header Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Header|
|0|Query String|

**DefaultValue**: False



### <a name="BKMK_msdyn_isparameter3header"></a> msdyn_isparameter3header

|Property|Value|
|--------|-----|
|Description|Parameter3 Type|
|DisplayName|Parameter3 Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isparameter3header|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_isparameter3header Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Header|
|0|Query String|

**DefaultValue**: False



### <a name="BKMK_msdyn_isparameter4header"></a> msdyn_isparameter4header

|Property|Value|
|--------|-----|
|Description|Parameter4 Type|
|DisplayName|Parameter4 Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isparameter4header|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_isparameter4header Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Header|
|0|Query String|

**DefaultValue**: False



### <a name="BKMK_msdyn_isparameter5header"></a> msdyn_isparameter5header

|Property|Value|
|--------|-----|
|Description|Parameter5 Type|
|DisplayName|Parameter5 Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isparameter5header|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_isparameter5header Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Header|
|0|Query String|

**DefaultValue**: False



### <a name="BKMK_msdyn_isparameter6header"></a> msdyn_isparameter6header

|Property|Value|
|--------|-----|
|Description|Parameter6 Type|
|DisplayName|Parameter6 Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isparameter6header|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_isparameter6header Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Header|
|0|Query String|

**DefaultValue**: False



### <a name="BKMK_msdyn_isparameter7header"></a> msdyn_isparameter7header

|Property|Value|
|--------|-----|
|Description|Parameter7 Type|
|DisplayName|Parameter7 Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isparameter7header|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_isparameter7header Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Header|
|0|Query String|

**DefaultValue**: False



### <a name="BKMK_msdyn_isparameter8header"></a> msdyn_isparameter8header

|Property|Value|
|--------|-----|
|Description|Parameter8 Type|
|DisplayName|Parameter8 Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isparameter8header|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_isparameter8header Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Header|
|0|Query String|

**DefaultValue**: False



### <a name="BKMK_msdyn_isparameter9header"></a> msdyn_isparameter9header

|Property|Value|
|--------|-----|
|Description|Parameter9 Type|
|DisplayName|Parameter9 Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isparameter9header|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_isparameter9header Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Header|
|0|Query String|

**DefaultValue**: False



### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|--------|-----|
|Description|Name of the OData v4 data source. This name appears in the data source drop-down list when creating a new entity.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_name|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msdyn_odatav4dsId"></a> msdyn_odatav4dsId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|OData v4 Data Source|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_odatav4dsid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_msdyn_paginationmode"></a> msdyn_paginationmode

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Pagination Mode|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_paginationmode|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_paginationmode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Server-side Paging|
|0|Client-side Paging|

**DefaultValue**: False



### <a name="BKMK_msdyn_paginationtype"></a> msdyn_paginationtype

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Pagination Mode|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_paginationtype|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### msdyn_paginationtype Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Client-side Paging||
|1|Server-side Paging||



### <a name="BKMK_msdyn_parameter10name"></a> msdyn_parameter10name

|Property|Value|
|--------|-----|
|Description||
|DisplayName|parameter10name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_parameter10name|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_parameter10value"></a> msdyn_parameter10value

|Property|Value|
|--------|-----|
|Description||
|DisplayName|parameter10value|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_parameter10value|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_parameter1name"></a> msdyn_parameter1name

|Property|Value|
|--------|-----|
|Description||
|DisplayName|parameter1name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_parameter1name|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_parameter1value"></a> msdyn_parameter1value

|Property|Value|
|--------|-----|
|Description||
|DisplayName|parameter1value|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_parameter1value|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_parameter2name"></a> msdyn_parameter2name

|Property|Value|
|--------|-----|
|Description||
|DisplayName|parameter2name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_parameter2name|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_parameter2value"></a> msdyn_parameter2value

|Property|Value|
|--------|-----|
|Description||
|DisplayName|parameter2value|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_parameter2value|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_parameter3name"></a> msdyn_parameter3name

|Property|Value|
|--------|-----|
|Description||
|DisplayName|parameter3name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_parameter3name|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_parameter3value"></a> msdyn_parameter3value

|Property|Value|
|--------|-----|
|Description||
|DisplayName|parameter3value|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_parameter3value|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_parameter4name"></a> msdyn_parameter4name

|Property|Value|
|--------|-----|
|Description||
|DisplayName|parameter4name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_parameter4name|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_parameter4value"></a> msdyn_parameter4value

|Property|Value|
|--------|-----|
|Description||
|DisplayName|parameter4value|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_parameter4value|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_parameter5name"></a> msdyn_parameter5name

|Property|Value|
|--------|-----|
|Description||
|DisplayName|parameter5name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_parameter5name|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_parameter5value"></a> msdyn_parameter5value

|Property|Value|
|--------|-----|
|Description||
|DisplayName|parameter5value|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_parameter5value|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_parameter6name"></a> msdyn_parameter6name

|Property|Value|
|--------|-----|
|Description||
|DisplayName|parameter6name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_parameter6name|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_parameter6value"></a> msdyn_parameter6value

|Property|Value|
|--------|-----|
|Description||
|DisplayName|parameter6value|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_parameter6value|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_parameter7name"></a> msdyn_parameter7name

|Property|Value|
|--------|-----|
|Description||
|DisplayName|parameter7name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_parameter7name|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_parameter7value"></a> msdyn_parameter7value

|Property|Value|
|--------|-----|
|Description||
|DisplayName|parameter7value|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_parameter7value|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_parameter8name"></a> msdyn_parameter8name

|Property|Value|
|--------|-----|
|Description||
|DisplayName|parameter8name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_parameter8name|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_parameter8value"></a> msdyn_parameter8value

|Property|Value|
|--------|-----|
|Description||
|DisplayName|parameter8value|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_parameter8value|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_parameter9name"></a> msdyn_parameter9name

|Property|Value|
|--------|-----|
|Description||
|DisplayName|parameter9name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_parameter9name|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_parameter9value"></a> msdyn_parameter9value

|Property|Value|
|--------|-----|
|Description||
|DisplayName|parameter9value|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_parameter9value|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_returninlinecount"></a> msdyn_returninlinecount

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Return Inline Count|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_returninlinecount|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_returninlinecount Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|True|
|0|False|

**DefaultValue**: True



### <a name="BKMK_msdyn_timeout"></a> msdyn_timeout

|Property|Value|
|--------|-----|
|Description|Amount of time to wait, in seconds, before timing out an OData v4 request.|
|DisplayName|Timeout|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_timeout|
|MaxValue|120|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_msdyn_uri"></a> msdyn_uri

|Property|Value|
|--------|-----|
|Description|URL of the OData v4 web service endpoint this data source will target.|
|DisplayName|URL|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_uri|
|MaxLength|1024|
|RequiredLevel|ApplicationRequired|
|Type|String|



### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.msdyn_odatav4ds?text=msdyn_odatav4ds EntityType" />