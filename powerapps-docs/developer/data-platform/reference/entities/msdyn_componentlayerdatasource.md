---
title: "Component Layer Data Source (msdyn_componentlayerdatasource) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Component Layer Data Source (msdyn_componentlayerdatasource) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Component Layer Data Source (msdyn_componentlayerdatasource) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Component Layer Data Source (msdyn_componentlayerdatasource) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Create`<br />Event: True |`POST` /msdyn_componentlayerdatasources<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /msdyn_componentlayerdatasources(*msdyn_componentlayerdatasourceid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Retrieve`<br />Event: True |`GET` /msdyn_componentlayerdatasources(*msdyn_componentlayerdatasourceid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_componentlayerdatasources<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /msdyn_componentlayerdatasources(*msdyn_componentlayerdatasourceid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /msdyn_componentlayerdatasources(*msdyn_componentlayerdatasourceid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Component Layer Data Source (msdyn_componentlayerdatasource) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Component Layer Data Source** |
| **DisplayCollectionName** | **Component Layer Data Sources** |
| **SchemaName** | `msdyn_componentlayerdatasource` |
| **CollectionSchemaName** | `msdyn_componentlayerdatasources` |
| **EntitySetName** | `msdyn_componentlayerdatasources`|
| **LogicalName** | `msdyn_componentlayerdatasource` |
| **LogicalCollectionName** | `msdyn_componentlayerdatasources` |
| **PrimaryIdAttribute** | `msdyn_componentlayerdatasourceid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [msdyn_componentlayerdatasourceId](#BKMK_msdyn_componentlayerdatasourceId)
- [msdyn_name](#BKMK_msdyn_name)

### <a name="BKMK_msdyn_componentlayerdatasourceId"></a> msdyn_componentlayerdatasourceId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Component Layer Data Source**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_componentlayerdatasourceid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|---|---|
|Description||
|DisplayName|**Name**|
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




### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_componentlayerdatasource?displayProperty=fullName>
