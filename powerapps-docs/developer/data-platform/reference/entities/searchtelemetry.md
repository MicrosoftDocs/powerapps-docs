---
title: "searchtelemetry table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the searchtelemetry table/entity."
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

# searchtelemetry table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Entity to log telemetry that used to improve search quality

**Added by**: msdyn_RelevanceSearch Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/searchtelemetries<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/searchtelemetries(*searchtelemetryid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/searchtelemetries(*searchtelemetryid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/searchtelemetries<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/searchtelemetries(*searchtelemetryid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|Upsert||<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

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
|1|Yes|
|0|No|

**DefaultValue**: False



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



### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.searchtelemetry?text=searchtelemetry EntityType" />