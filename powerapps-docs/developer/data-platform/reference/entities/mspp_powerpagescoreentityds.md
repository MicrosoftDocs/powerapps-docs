---
title: "Power Pages Core Entity DS (mspp_powerpagescoreentityds) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Power Pages Core Entity DS (mspp_powerpagescoreentityds) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Power Pages Core Entity DS (mspp_powerpagescoreentityds) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Power Pages Core Entity DS (mspp_powerpagescoreentityds) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Create`<br />Event: True |`POST` /mspp_powerpagescoreentitydses<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mspp_powerpagescoreentitydses(*mspp_powerpagescoreentitydsid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Retrieve`<br />Event: True |`GET` /mspp_powerpagescoreentitydses(*mspp_powerpagescoreentitydsid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /mspp_powerpagescoreentitydses<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /mspp_powerpagescoreentitydses(*mspp_powerpagescoreentitydsid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mspp_powerpagescoreentitydses(*mspp_powerpagescoreentitydsid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Power Pages Core Entity DS (mspp_powerpagescoreentityds) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Power Pages Core Entity DS (mspp_powerpagescoreentityds) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Power Pages Core Entity DS** |
| **DisplayCollectionName** | **Power Pages Core Entity DSs** |
| **SchemaName** | `mspp_powerpagescoreentityds` |
| **CollectionSchemaName** | `mspp_powerpagescoreentitydses` |
| **EntitySetName** | `mspp_powerpagescoreentitydses`|
| **LogicalName** | `mspp_powerpagescoreentityds` |
| **LogicalCollectionName** | `mspp_powerpagescoreentitydses` |
| **PrimaryIdAttribute** | `mspp_powerpagescoreentitydsid` |
| **PrimaryNameAttribute** |`mspp_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_name](#BKMK_mspp_name)
- [mspp_powerpagescoreentitydsId](#BKMK_mspp_powerpagescoreentitydsId)

### <a name="BKMK_mspp_name"></a> mspp_name

|Property|Value|
|---|---|
|Description||
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_powerpagescoreentitydsId"></a> mspp_powerpagescoreentitydsId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Power Pages Core Entity DS**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspp_powerpagescoreentitydsid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|




### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mspp_powerpagescoreentityds?displayProperty=fullName>
