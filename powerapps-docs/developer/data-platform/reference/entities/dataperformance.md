---
title: "Data Performance Dashboard (DataPerformance) table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Data Performance Dashboard (DataPerformance) table/entity."
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

# Data Performance Dashboard (DataPerformance) table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Data Performance Dashboard.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Retrieve|GET [*org URI*]/api/data/v9.0/dataperformances(*dataperformanceid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/dataperformances<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|DataPerformances|
|DisplayCollectionName|Data Performance Collection|
|DisplayName|Data Performance Dashboard|
|EntitySetName|dataperformances|
|IsBPFEntity|False|
|LogicalCollectionName|dataperformances|
|LogicalName|dataperformance|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|dataperformanceid|
|PrimaryNameAttribute||
|SchemaName|DataPerformance|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.


### <a name="BKMK_DataPerformanceId"></a> DataPerformanceId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the performance suggestion.|
|DisplayName|Id|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|dataperformanceid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AnyOptimizationApplied](#BKMK_AnyOptimizationApplied)
- [AnyOptimizationAvailable](#BKMK_AnyOptimizationAvailable)
- [Component](#BKMK_Component)
- [Count](#BKMK_Count)
- [Entity](#BKMK_Entity)
- [EstimatedOptimizationImpact](#BKMK_EstimatedOptimizationImpact)
- [ExecutionPeriod](#BKMK_ExecutionPeriod)
- [LastActionResult](#BKMK_LastActionResult)
- [LastOptimizationDate](#BKMK_LastOptimizationDate)
- [MaxTime](#BKMK_MaxTime)
- [MedianTime](#BKMK_MedianTime)
- [MinTime](#BKMK_MinTime)
- [Operation](#BKMK_Operation)
- [OptimizationStatus](#BKMK_OptimizationStatus)
- [OptimizationStorage](#BKMK_OptimizationStorage)
- [OrganizationId](#BKMK_OrganizationId)
- [RealizedOptimizationImpact](#BKMK_RealizedOptimizationImpact)
- [Solution](#BKMK_Solution)
- [Weight](#BKMK_Weight)


### <a name="BKMK_AnyOptimizationApplied"></a> AnyOptimizationApplied

|Property|Value|
|--------|-----|
|Description|An internal state which indicates whether at least one optimization is applied.|
|DisplayName|Any Optimization Applied|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|anyoptimizationapplied|
|RequiredLevel|None|
|Type|Boolean|

#### AnyOptimizationApplied Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_AnyOptimizationAvailable"></a> AnyOptimizationAvailable

|Property|Value|
|--------|-----|
|Description|An internal state which indicates whether at least one optimization is available for this record.|
|DisplayName|Any Optimization Available|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|anyoptimizationavailable|
|RequiredLevel|None|
|Type|Boolean|

#### AnyOptimizationAvailable Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_Component"></a> Component

|Property|Value|
|--------|-----|
|Description|Name of the component|
|DisplayName|Component|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|component|
|MaxLength|100000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Count"></a> Count

|Property|Value|
|--------|-----|
|Description|Number of times a queries were executed (Aggregated)|
|DisplayName|Count|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|count|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_Entity"></a> Entity

|Property|Value|
|--------|-----|
|Description|Primary entity|
|DisplayName|Entity|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|entity|
|MaxLength|100000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EstimatedOptimizationImpact"></a> EstimatedOptimizationImpact

|Property|Value|
|--------|-----|
|Description|The expected average cost benefit of an optimization.|
|DisplayName|Estimated Optimization Impact|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|estimatedoptimizationimpact|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_ExecutionPeriod"></a> ExecutionPeriod

|Property|Value|
|--------|-----|
|Description|The execution period for which the performance metrics are calculated.|
|DisplayName|Execution Period|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|executionperiod|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_LastActionResult"></a> LastActionResult

|Property|Value|
|--------|-----|
|Description|An internal state which shows the result of the last action that was taken on this record.|
|DisplayName|Last Action Result|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastactionresult|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_LastOptimizationDate"></a> LastOptimizationDate

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Last time an optimization was applied.|
|DisplayName|Last Optimization Date|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastoptimizationdate|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_MaxTime"></a> MaxTime

|Property|Value|
|--------|-----|
|Description|Maximum execution time in seconds. (Aggregated)|
|DisplayName|Max Time|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|maxtime|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_MedianTime"></a> MedianTime

|Property|Value|
|--------|-----|
|Description|Average execution time in seconds. (Aggregated)|
|DisplayName|Median Time|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mediantime|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_MinTime"></a> MinTime

|Property|Value|
|--------|-----|
|Description|Minimum execution time in seconds. (Aggregated)|
|DisplayName|Min Time|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mintime|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_Operation"></a> Operation

|Property|Value|
|--------|-----|
|Description|Data operation that triggered the query (Retrieve Multiple, etc.)|
|DisplayName|Operation|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|operation|
|MaxLength|100000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OptimizationStatus"></a> OptimizationStatus

|Property|Value|
|--------|-----|
|Description|Current optimization status of the record, showed to the customer.|
|DisplayName|Optimization Status|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|optimizationstatus|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OptimizationStorage"></a> OptimizationStorage

|Property|Value|
|--------|-----|
|Description|Storage consumed by the optimization. (MB)|
|DisplayName|Optimization Storage|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|optimizationstorage|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the organization associated.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|SystemRequired|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_RealizedOptimizationImpact"></a> RealizedOptimizationImpact

|Property|Value|
|--------|-----|
|Description|Actual performance change after taking an optimization action on the record.|
|DisplayName|Optimization Impact (%)|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|realizedoptimizationimpact|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Solution"></a> Solution

|Property|Value|
|--------|-----|
|Description|Name of the solution that owns the component|
|DisplayName|Solution|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|solution|
|MaxLength|100000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Weight"></a> Weight

|Property|Value|
|--------|-----|
|Description|Query Weight of the component. Factored with the Optimization Impact to determine the overall importance of applying an optimization. (P2)|
|DisplayName|Weight|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|weight|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|
|RequiredLevel|None|
|Type|Decimal|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.


### <a name="BKMK_lk_dataperformance_organizationid"></a> lk_dataperformance_organizationid

See organization Table [lk_dataperformance_organizationid](organization.md#BKMK_lk_dataperformance_organizationid) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.dataperformance?text=dataperformance EntityType" />