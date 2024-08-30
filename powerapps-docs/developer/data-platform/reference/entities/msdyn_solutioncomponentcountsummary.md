---
title: "Solution Component Count Summary (msdyn_solutioncomponentcountsummary) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Solution Component Count Summary (msdyn_solutioncomponentcountsummary) table/entity with Microsoft Dataverse."
ms.date: 08/30/2024
ms.service: powerapps
ms.topic: reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Solution Component Count Summary (msdyn_solutioncomponentcountsummary) table/entity reference



## Messages

The following table lists the messages for the Solution Component Count Summary (msdyn_solutioncomponentcountsummary) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Create`<br />Event: True |`POST` /msdyn_solutioncomponentcountsummaries<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /msdyn_solutioncomponentcountsummaries(*msdyn_solutioncomponentcountsummaryid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Retrieve`<br />Event: False |`GET` /msdyn_solutioncomponentcountsummaries(*msdyn_solutioncomponentcountsummaryid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: False |`GET` /msdyn_solutioncomponentcountsummaries<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /msdyn_solutioncomponentcountsummaries(*msdyn_solutioncomponentcountsummaryid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /msdyn_solutioncomponentcountsummaries(*msdyn_solutioncomponentcountsummaryid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Solution Component Count Summary (msdyn_solutioncomponentcountsummary) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Solution Component Count Summary** |
| **DisplayCollectionName** | **Solution Component Count Summaries** |
| **SchemaName** | `msdyn_solutioncomponentcountsummary` |
| **CollectionSchemaName** | `msdyn_solutioncomponentcountsummaries` |
| **EntitySetName** | `msdyn_solutioncomponentcountsummaries`|
| **LogicalName** | `msdyn_solutioncomponentcountsummary` |
| **LogicalCollectionName** | `msdyn_solutioncomponentcountsummaries` |
| **PrimaryIdAttribute** | `msdyn_solutioncomponentcountsummaryid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [msdyn_componentlogicalname](#BKMK_msdyn_componentlogicalname)
- [msdyn_componenttype](#BKMK_msdyn_componenttype)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_primaryentityname](#BKMK_msdyn_primaryentityname)
- [msdyn_solutioncomponentcountsummaryId](#BKMK_msdyn_solutioncomponentcountsummaryId)
- [msdyn_solutionid](#BKMK_msdyn_solutionid)
- [msdyn_subtype](#BKMK_msdyn_subtype)
- [msdyn_total](#BKMK_msdyn_total)
- [msdyn_workflowcategory](#BKMK_msdyn_workflowcategory)

### <a name="BKMK_msdyn_componentlogicalname"></a> msdyn_componentlogicalname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Component Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_componentlogicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_componenttype"></a> msdyn_componenttype

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_componenttype**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_componenttype`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Auto|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|2|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
|DisplayName|**msdyn_name**|
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

### <a name="BKMK_msdyn_primaryentityname"></a> msdyn_primaryentityname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Primary Entity Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_primaryentityname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_solutioncomponentcountsummaryId"></a> msdyn_solutioncomponentcountsummaryId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**SolutionComponentCountSummary**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_solutioncomponentcountsummaryid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_solutionid"></a> msdyn_solutionid

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_solutionid**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_solutionid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_subtype"></a> msdyn_subtype

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_subtype**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_subtype`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_total"></a> msdyn_total

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_total**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_total`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Auto|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|2|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_workflowcategory"></a> msdyn_workflowcategory

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_workflowcategory**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_workflowcategory`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

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



### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_solutioncomponentcountsummary?displayProperty=fullName>
