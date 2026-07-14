---
title: "NonRelational Data Source (msdyn_nonrelationalds) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the NonRelational Data Source (msdyn_nonrelationalds) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# NonRelational Data Source (msdyn_nonrelationalds) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the NonRelational Data Source (msdyn_nonrelationalds) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Create`<br />Event: True |`POST` /msdyn_nonrelationaldses<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_nonrelationaldses(*msdyn_nonrelationaldsid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Retrieve`<br />Event: True |`GET` /msdyn_nonrelationaldses(*msdyn_nonrelationaldsid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_nonrelationaldses<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /msdyn_nonrelationaldses(*msdyn_nonrelationaldsid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_nonrelationaldses(*msdyn_nonrelationaldsid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the NonRelational Data Source (msdyn_nonrelationalds) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **NonRelational Data Source** |
| **DisplayCollectionName** | **NonRelational Data Source** |
| **SchemaName** | `msdyn_nonrelationalds` |
| **CollectionSchemaName** | `msdyn_nonrelationaldses` |
| **EntitySetName** | `msdyn_nonrelationaldses`|
| **LogicalName** | `msdyn_nonrelationalds` |
| **LogicalCollectionName** | `msdyn_nonrelationaldses` |
| **PrimaryIdAttribute** | `msdyn_nonrelationaldsid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_nonrelationaldsId](#BKMK_msdyn_nonrelationaldsId)

### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
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

### <a name="BKMK_msdyn_nonrelationaldsId"></a> msdyn_nonrelationaldsId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**NonRelational Data Source**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_nonrelationaldsid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|




### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_nonrelationalds?displayProperty=fullName>
