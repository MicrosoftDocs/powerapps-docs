---
title: "Search Telemetry (searchtelemetry) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Search Telemetry (searchtelemetry) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Search Telemetry (searchtelemetry) table/entity reference (Microsoft Dataverse)

Entity to log telemetry that used to improve search quality

## Messages

The following table lists the messages for the Search Telemetry (searchtelemetry) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Create`<br />Event: True |`POST` /searchtelemetries<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /searchtelemetries(*searchtelemetryid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `DeleteMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.DeleteMultiple?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retrieve`<br />Event: True |`GET` /searchtelemetries(*searchtelemetryid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /searchtelemetries<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /searchtelemetries(*searchtelemetryid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: True |`PATCH` /searchtelemetries(*searchtelemetryid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Search Telemetry (searchtelemetry) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Search Telemetry (searchtelemetry) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Search Telemetry** |
| **DisplayCollectionName** | **Search Telemetry** |
| **SchemaName** | `searchtelemetry` |
| **CollectionSchemaName** | `searchtelemetries` |
| **EntitySetName** | `searchtelemetries`|
| **LogicalName** | `searchtelemetry` |
| **LogicalCollectionName** | `searchtelemetries` |
| **PrimaryIdAttribute** | `searchtelemetryid` |
| **PrimaryNameAttribute** |`userquery` |
| **TableType** | `Elastic` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CorrelationId](#BKMK_CorrelationId)
- [EyesOnAnalyticsAllowed](#BKMK_EyesOnAnalyticsAllowed)
- [FeedbackData](#BKMK_FeedbackData)
- [PartitionId](#BKMK_PartitionId)
- [RequestId](#BKMK_RequestId)
- [ScenarioName](#BKMK_ScenarioName)
- [searchtelemetryId](#BKMK_searchtelemetryId)
- [SessionId](#BKMK_SessionId)
- [TTLInSeconds](#BKMK_TTLInSeconds)
- [UserQuery](#BKMK_UserQuery)

### <a name="BKMK_CorrelationId"></a> CorrelationId

|Property|Value|
|---|---|
|Description|**CorrelationId for the search**|
|DisplayName|**CorrelationId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`correlationid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_EyesOnAnalyticsAllowed"></a> EyesOnAnalyticsAllowed

|Property|Value|
|---|---|
|Description|**If customer is allow our engineer to eye on**|
|DisplayName|**EyesOnAnalyticsAllowed**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`eyesonanalyticsallowed`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`searchtelemetry_eyesonanalyticsallowed`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_FeedbackData"></a> FeedbackData

|Property|Value|
|---|---|
|Description|**Feedback data for the search**|
|DisplayName|**FeedbackData**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`feedbackdata`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048577|

### <a name="BKMK_PartitionId"></a> PartitionId

|Property|Value|
|---|---|
|Description|**Logical partition id. A logical partition consists of a set of records with same partition id.**|
|DisplayName|**Partition Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`partitionid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_RequestId"></a> RequestId

|Property|Value|
|---|---|
|Description|**RequestId for the search**|
|DisplayName|**RequestId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`requestid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ScenarioName"></a> ScenarioName

|Property|Value|
|---|---|
|Description|**ScenarioName for the search, current will be one of RelevanceSearch/Marketing/Cxp**|
|DisplayName|**ScenarioName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`scenarioname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_searchtelemetryId"></a> searchtelemetryId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**SearchTelemetry Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`searchtelemetryid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SessionId"></a> SessionId

|Property|Value|
|---|---|
|Description|**SessionId for the search**|
|DisplayName|**SessionId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sessionid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_TTLInSeconds"></a> TTLInSeconds

|Property|Value|
|---|---|
|Description|**Time to live in seconds.**|
|DisplayName|**Time to live**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ttlinseconds`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|1|

### <a name="BKMK_UserQuery"></a> UserQuery

|Property|Value|
|---|---|
|Description|**User Query**|
|DisplayName|**UserQuery**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`userquery`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedOn](#BKMK_CreatedOn)
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

### <a name="BKMK_versionnumber"></a> versionnumber

|Property|Value|
|---|---|
|Description|**Version number of SearchTelemetry.**|
|DisplayName|**Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.searchtelemetry?displayProperty=fullName>
