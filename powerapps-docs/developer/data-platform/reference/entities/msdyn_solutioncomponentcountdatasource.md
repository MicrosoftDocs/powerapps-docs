---
title: "Solution Component Count Data Source (msdyn_solutioncomponentcountdatasource) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Solution Component Count Data Source (msdyn_solutioncomponentcountdatasource) table/entity with Microsoft Dataverse."
ms.date: 08/30/2024
ms.service: powerapps
ms.topic: reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Solution Component Count Data Source (msdyn_solutioncomponentcountdatasource) table/entity reference



## Messages

The following table lists the messages for the Solution Component Count Data Source (msdyn_solutioncomponentcountdatasource) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Create`<br />Event: True |`POST` /msdyn_solutioncomponentcountdatasources<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /msdyn_solutioncomponentcountdatasources(*msdyn_solutioncomponentcountdatasourceid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Retrieve`<br />Event: False |`GET` /msdyn_solutioncomponentcountdatasources(*msdyn_solutioncomponentcountdatasourceid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: False |`GET` /msdyn_solutioncomponentcountdatasources<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /msdyn_solutioncomponentcountdatasources(*msdyn_solutioncomponentcountdatasourceid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /msdyn_solutioncomponentcountdatasources(*msdyn_solutioncomponentcountdatasourceid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Solution Component Count Data Source (msdyn_solutioncomponentcountdatasource) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Solution Component Count Data Source** |
| **DisplayCollectionName** | **Solution Component Count Data Sources** |
| **SchemaName** | `msdyn_solutioncomponentcountdatasource` |
| **CollectionSchemaName** | `msdyn_solutioncomponentcountdatasources` |
| **EntitySetName** | `msdyn_solutioncomponentcountdatasources`|
| **LogicalName** | `msdyn_solutioncomponentcountdatasource` |
| **LogicalCollectionName** | `msdyn_solutioncomponentcountdatasources` |
| **PrimaryIdAttribute** | `msdyn_solutioncomponentcountdatasourceid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_solutioncomponentcountdatasourceId](#BKMK_msdyn_solutioncomponentcountdatasourceId)

### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_solutioncomponentcountdatasourceId"></a> msdyn_solutioncomponentcountdatasourceId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Solution Component Data Source**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_solutioncomponentcountdatasourceid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


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
|Type|Uniqueidentifier|



### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_solutioncomponentcountdatasource?displayProperty=fullName>
