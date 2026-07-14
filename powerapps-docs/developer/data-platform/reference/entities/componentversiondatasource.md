---
title: "Component Version Data Source (componentversiondatasource) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Component Version Data Source (componentversiondatasource) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Component Version Data Source (componentversiondatasource) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Component Version Data Source (componentversiondatasource) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Create`<br />Event: False |`POST` /componentversiondatasources<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: False |`DELETE` /componentversiondatasources(*componentversiondatasourceid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Retrieve`<br />Event: False |`GET` /componentversiondatasources(*componentversiondatasourceid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: False | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: False |`GET` /componentversiondatasources<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /componentversiondatasources(*componentversiondatasourceid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /componentversiondatasources(*componentversiondatasourceid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Component Version Data Source (componentversiondatasource) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Component Version Data Source** |
| **DisplayCollectionName** | **Component Version Data Sources** |
| **SchemaName** | `componentversiondatasource` |
| **CollectionSchemaName** | `componentversiondatasources` |
| **EntitySetName** | `componentversiondatasources`|
| **LogicalName** | `componentversiondatasource` |
| **LogicalCollectionName** | `componentversiondatasources` |
| **PrimaryIdAttribute** | `componentversiondatasourceid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [componentversiondatasourceId](#BKMK_componentversiondatasourceId)
- [name](#BKMK_name)

### <a name="BKMK_componentversiondatasourceId"></a> componentversiondatasourceId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Component Version Data Source**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentversiondatasourceid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_name"></a> name

|Property|Value|
|---|---|
|Description||
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
|MaxLength|100|




### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.componentversiondatasource?displayProperty=fullName>
