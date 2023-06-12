---
title: "searchtelemetry table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the searchtelemetry table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# searchtelemetry table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Entity to log telemetry that used to improve search quality

**Added by**: msdyn_RelevanceSearch Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /searchtelemetries<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /searchtelemetries(*searchtelemetryid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /searchtelemetries(*searchtelemetryid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /searchtelemetries<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /searchtelemetries(*searchtelemetryid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|Upsert||<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|searchtelemetries|
|DisplayCollectionName|Search Telemetry|
|DisplayName|Search Telemetry|
|EntitySetName|searchtelemetries|
|IsBPFEntity|False|
|LogicalCollectionName|searchtelemetries|
|LogicalName|searchtelemetry|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|searchtelemetryid|
|PrimaryNameAttribute|userquery|
|SchemaName|searchtelemetry|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description|CorrelationId for the search|
|DisplayName|CorrelationId|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|correlationid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EyesOnAnalyticsAllowed"></a> EyesOnAnalyticsAllowed

|Property|Value|
|--------|-----|
|Description|If customer is allow our engineer to eye on|
|DisplayName|EyesOnAnalyticsAllowed|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|eyesonanalyticsallowed|
|RequiredLevel|None|
|Type|Boolean|

#### EyesOnAnalyticsAllowed Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_FeedbackData"></a> FeedbackData

|Property|Value|
|--------|-----|
|Description|Feedback data for the search|
|DisplayName|FeedbackData|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|feedbackdata|
|MaxLength|1048577|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PartitionId"></a> PartitionId

|Property|Value|
|--------|-----|
|Description|Logical partition id. A logical partition consists of a set of records with same partition id.|
|DisplayName|Partition Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|partitionid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RequestId"></a> RequestId

|Property|Value|
|--------|-----|
|Description|RequestId for the search|
|DisplayName|RequestId|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|requestid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ScenarioName"></a> ScenarioName

|Property|Value|
|--------|-----|
|Description|ScenarioName for the search, current will be one of RelevanceSearch/Marketing/Cxp|
|DisplayName|ScenarioName|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|scenarioname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_searchtelemetryId"></a> searchtelemetryId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|SearchTelemetry Id|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|searchtelemetryid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SessionId"></a> SessionId

|Property|Value|
|--------|-----|
|Description|SessionId for the search|
|DisplayName|SessionId|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|sessionid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TTLInSeconds"></a> TTLInSeconds

|Property|Value|
|--------|-----|
|Description|Time to live in seconds.|
|DisplayName|Time to live|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ttlinseconds|
|MaxValue|2147483647|
|MinValue|1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_UserQuery"></a> UserQuery

|Property|Value|
|--------|-----|
|Description|User Query|
|DisplayName|UserQuery|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|userquery|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedOn](#BKMK_CreatedOn)
- [versionnumber](#BKMK_versionnumber)


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_versionnumber"></a> versionnumber

|Property|Value|
|--------|-----|
|Description|Version number of SearchTelemetry.|
|DisplayName|Version Number|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|



### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.searchtelemetry?text=searchtelemetry EntityType" />