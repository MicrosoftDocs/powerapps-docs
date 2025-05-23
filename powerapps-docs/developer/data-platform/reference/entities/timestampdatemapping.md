---
title: "Time Stamp Date Mapping (TimeStampDateMapping) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Time Stamp Date Mapping (TimeStampDateMapping) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Time Stamp Date Mapping (TimeStampDateMapping) table/entity reference (Microsoft Dataverse)

For internal use only.`

## Properties

The following table lists selected properties for the Time Stamp Date Mapping (TimeStampDateMapping) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Time Stamp Date Mapping** |
| **DisplayCollectionName** | **Time Stamp Date Mappings** |
| **SchemaName** | `TimeStampDateMapping` |
| **CollectionSchemaName** | `TimeStampDateMappings` |
| **EntitySetName** | `timestampdatemappings`|
| **LogicalName** | `timestampdatemapping` |
| **LogicalCollectionName** | `timestampdatemappings` |
| **PrimaryIdAttribute** | `timestampdatemappingid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

### <a name="BKMK_TimeStampDateMappingId"></a> TimeStampDateMappingId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timestampdatemappingid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [Date](#BKMK_Date)
- [TimeStamp](#BKMK_TimeStamp)

### <a name="BKMK_Date"></a> Date

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`date`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_TimeStamp"></a> TimeStamp

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timestamp`|
|RequiredLevel|SystemRequired|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.timestampdatemapping?displayProperty=fullName>
