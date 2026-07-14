---
title: "Data Performance Dashboard (DataPerformance) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Data Performance Dashboard (DataPerformance) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Data Performance Dashboard (DataPerformance) table/entity reference (Microsoft Dataverse)

Data Performance Dashboard.

## Messages

The following table lists the messages for the Data Performance Dashboard (DataPerformance) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /dataperformances(*dataperformanceid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /dataperformances<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Data Performance Dashboard (DataPerformance) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Data Performance Dashboard** |
| **DisplayCollectionName** | **Data Performance Collection** |
| **SchemaName** | `DataPerformance` |
| **CollectionSchemaName** | `DataPerformances` |
| **EntitySetName** | `dataperformances`|
| **LogicalName** | `dataperformance` |
| **LogicalCollectionName** | `dataperformances` |
| **PrimaryIdAttribute** | `dataperformanceid` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

### <a name="BKMK_DataPerformanceId"></a> DataPerformanceId

|Property|Value|
|---|---|
|Description|**Unique identifier of the performance suggestion.**|
|DisplayName|**Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`dataperformanceid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

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
|---|---|
|Description|**An internal state which indicates whether at least one optimization is applied.**|
|DisplayName|**Any Optimization Applied**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`anyoptimizationapplied`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`dataperformance_anyoptimizationapplied`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_AnyOptimizationAvailable"></a> AnyOptimizationAvailable

|Property|Value|
|---|---|
|Description|**An internal state which indicates whether at least one optimization is available for this record.**|
|DisplayName|**Any Optimization Available**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`anyoptimizationavailable`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`dataperformance_anyoptimizationavailable`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Component"></a> Component

|Property|Value|
|---|---|
|Description|**Name of the component**|
|DisplayName|**Component**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`component`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_Count"></a> Count

|Property|Value|
|---|---|
|Description|**Number of times a queries were executed (Aggregated)**|
|DisplayName|**Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`count`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_Entity"></a> Entity

|Property|Value|
|---|---|
|Description|**Primary entity**|
|DisplayName|**Entity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entity`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_EstimatedOptimizationImpact"></a> EstimatedOptimizationImpact

|Property|Value|
|---|---|
|Description|**The expected average cost benefit of an optimization.**|
|DisplayName|**Estimated Optimization Impact**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`estimatedoptimizationimpact`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Auto|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|
|SourceTypeMask|0|

### <a name="BKMK_ExecutionPeriod"></a> ExecutionPeriod

|Property|Value|
|---|---|
|Description|**The execution period for which the performance metrics are calculated.**|
|DisplayName|**Execution Period**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`executionperiod`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_LastActionResult"></a> LastActionResult

|Property|Value|
|---|---|
|Description|**An internal state which shows the result of the last action that was taken on this record.**|
|DisplayName|**Last Action Result**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastactionresult`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_LastOptimizationDate"></a> LastOptimizationDate

|Property|Value|
|---|---|
|Description|**Last time an optimization was applied.**|
|DisplayName|**Last Optimization Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastoptimizationdate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_MaxTime"></a> MaxTime

|Property|Value|
|---|---|
|Description|**Maximum execution time in seconds. (Aggregated)**|
|DisplayName|**Max Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`maxtime`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Auto|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|
|SourceTypeMask|0|

### <a name="BKMK_MedianTime"></a> MedianTime

|Property|Value|
|---|---|
|Description|**Average execution time in seconds. (Aggregated)**|
|DisplayName|**Median Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mediantime`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Auto|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|
|SourceTypeMask|0|

### <a name="BKMK_MinTime"></a> MinTime

|Property|Value|
|---|---|
|Description|**Minimum execution time in seconds. (Aggregated)**|
|DisplayName|**Min Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mintime`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Auto|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|
|SourceTypeMask|0|

### <a name="BKMK_Operation"></a> Operation

|Property|Value|
|---|---|
|Description|**Data operation that triggered the query (Retrieve Multiple, etc.)**|
|DisplayName|**Operation**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`operation`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_OptimizationStatus"></a> OptimizationStatus

|Property|Value|
|---|---|
|Description|**Current optimization status of the record, showed to the customer.**|
|DisplayName|**Optimization Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`optimizationstatus`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_OptimizationStorage"></a> OptimizationStorage

|Property|Value|
|---|---|
|Description|**Storage consumed by the optimization. (MB)**|
|DisplayName|**Optimization Storage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`optimizationstorage`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Auto|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|
|SourceTypeMask|0|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization associated.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_RealizedOptimizationImpact"></a> RealizedOptimizationImpact

|Property|Value|
|---|---|
|Description|**Actual performance change after taking an optimization action on the record.**|
|DisplayName|**Optimization Impact (%)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`realizedoptimizationimpact`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Solution"></a> Solution

|Property|Value|
|---|---|
|Description|**Name of the solution that owns the component**|
|DisplayName|**Solution**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`solution`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_Weight"></a> Weight

|Property|Value|
|---|---|
|Description|**Query Weight of the component. Factored with the Optimization Impact to determine the overall importance of applying an optimization. (P2)**|
|DisplayName|**Weight**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`weight`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Auto|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|
|SourceTypeMask|0|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

### <a name="BKMK_lk_dataperformance_organizationid"></a> lk_dataperformance_organizationid

One-To-Many Relationship: [organization lk_dataperformance_organizationid](organization.md#BKMK_lk_dataperformance_organizationid)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.dataperformance?displayProperty=fullName>
