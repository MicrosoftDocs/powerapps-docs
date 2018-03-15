---
title: "DataPerformance Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the DataPerformance entity."

services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/07/2018
ms.author: jdaly
---
# DataPerformance Entity Reference

Data Performance Dashboard.

## Entity Properties

**DisplayName**: Data Performance Dashboard<br />
**DisplayCollectionName**: Data Performance Collection<br />
**SchemaName**: DataPerformance<br />
**CollectionSchemaName**: DataPerformances<br />
**LogicalName**: dataperformance<br />
**LogicalCollectionName**: dataperformances<br />
**EntitySetName**: dataperformances<br />
**PrimaryIdAttribute**: dataperformanceid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.


### <a name="BKMK_DataPerformanceId"></a> DataPerformanceId

**Description**: Unique identifier of the performance suggestion.<br />
**DisplayName**: Id<br />
**LogicalName**: dataperformanceid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

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

**Description**: An internal state which indicates whether at least one optimization is applied.<br />
**DisplayName**: Any Optimization Applied<br />
**LogicalName**: anyoptimizationapplied<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_AnyOptimizationAvailable"></a> AnyOptimizationAvailable

**Description**: An internal state which indicates whether at least one optimization is available for this record.<br />
**DisplayName**: Any Optimization Available<br />
**LogicalName**: anyoptimizationavailable<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_Component"></a> Component

**Description**: Name of the component<br />
**DisplayName**: Component<br />
**LogicalName**: component<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100000


### <a name="BKMK_Count"></a> Count

**Description**: Number of times a queries were executed (Aggregated)<br />
**DisplayName**: Count<br />
**LogicalName**: count<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_Entity"></a> Entity

**Description**: Primary entity<br />
**DisplayName**: Entity<br />
**LogicalName**: entity<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100000


### <a name="BKMK_EstimatedOptimizationImpact"></a> EstimatedOptimizationImpact

**Description**: The expected average cost benefit of an optimization.<br />
**DisplayName**: Estimated Optimization Impact<br />
**LogicalName**: estimatedoptimizationimpact<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0<br />
**Precision**: 2


### <a name="BKMK_ExecutionPeriod"></a> ExecutionPeriod

**Description**: The execution period for which the performance metrics are calculated.<br />
**DisplayName**: Execution Period<br />
**LogicalName**: executionperiod<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_LastActionResult"></a> LastActionResult

**Description**: An internal state which shows the result of the last action that was taken on this record.<br />
**DisplayName**: Last Action Result<br />
**LogicalName**: lastactionresult<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_LastOptimizationDate"></a> LastOptimizationDate

**Description**: Last time an optimization was applied.<br />
**DisplayName**: Last Optimization Date<br />
**LogicalName**: lastoptimizationdate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_MaxTime"></a> MaxTime

**Description**: Maximum execution time in seconds. (Aggregated)<br />
**DisplayName**: Max Time<br />
**LogicalName**: maxtime<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0<br />
**Precision**: 2


### <a name="BKMK_MedianTime"></a> MedianTime

**Description**: Average execution time in seconds. (Aggregated)<br />
**DisplayName**: Median Time<br />
**LogicalName**: mediantime<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0<br />
**Precision**: 2


### <a name="BKMK_MinTime"></a> MinTime

**Description**: Minimum execution time in seconds. (Aggregated)<br />
**DisplayName**: Min Time<br />
**LogicalName**: mintime<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0<br />
**Precision**: 2


### <a name="BKMK_Operation"></a> Operation

**Description**: Data operation that triggered the query (Retrieve Multiple, etc.)<br />
**DisplayName**: Operation<br />
**LogicalName**: operation<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100000


### <a name="BKMK_OptimizationStatus"></a> OptimizationStatus

**Description**: Current optimization status of the record, showed to the customer.<br />
**DisplayName**: Optimization Status<br />
**LogicalName**: optimizationstatus<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_OptimizationStorage"></a> OptimizationStorage

**Description**: Storage consumed by the optimization. (MB)<br />
**DisplayName**: Optimization Storage<br />
**LogicalName**: optimizationstorage<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0<br />
**Precision**: 2


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization associated.<br />
**DisplayName**: <br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: organization


### <a name="BKMK_RealizedOptimizationImpact"></a> RealizedOptimizationImpact

**Description**: Actual performance change after taking an optimization action on the record.<br />
**DisplayName**: Optimization Impact (%)<br />
**LogicalName**: realizedoptimizationimpact<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_Solution"></a> Solution

**Description**: Name of the solution that owns the component<br />
**DisplayName**: Solution<br />
**LogicalName**: solution<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100000


### <a name="BKMK_Weight"></a> Weight

**Description**: Query Weight of the component. Factored with the Optimization Impact to determine the overall importance of applying an optimization. (P2)<br />
**DisplayName**: Weight<br />
**LogicalName**: weight<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0<br />
**Precision**: 2

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.


### <a name="BKMK_lk_dataperformance_organizationid"></a> lk_dataperformance_organizationid

See organization Entity [lk_dataperformance_organizationid](organization.md#BKMK_lk_dataperformance_organizationid) One-To-Many relationship.
dataperformance

