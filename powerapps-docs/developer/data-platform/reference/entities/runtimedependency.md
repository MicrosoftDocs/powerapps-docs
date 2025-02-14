---
title: "RuntimeDependency table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the RuntimeDependency table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# RuntimeDependency table/entity reference (Microsoft Dataverse)

Form Level dependencies in CRM.

## Properties

The following table lists selected properties for the RuntimeDependency table.

|Property|Value|
| --- | --- |
| **DisplayName** | **RuntimeDependency** |
| **DisplayCollectionName** | **RuntimeDependencies** |
| **SchemaName** | `RuntimeDependency` |
| **CollectionSchemaName** | `RuntimeDependencies` |
| **EntitySetName** | `runtimedependencies`|
| **LogicalName** | `runtimedependency` |
| **LogicalCollectionName** | `runtimedependencies` |
| **PrimaryIdAttribute** | `dependencyid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [DependentComponentNodeId](#BKMK_DependentComponentNodeId)
- [DependentComponentType](#BKMK_DependentComponentType)
- [IsPublished](#BKMK_IsPublished)
- [RequiredComponentNodeId](#BKMK_RequiredComponentNodeId)
- [RequiredComponentType](#BKMK_RequiredComponentType)

### <a name="BKMK_DependentComponentNodeId"></a> DependentComponentNodeId

|Property|Value|
|---|---|
|Description|**Unique identifier of the dependent component's node.**|
|DisplayName|**Dependent Component**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`dependentcomponentnodeid`|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_DependentComponentType"></a> DependentComponentType

|Property|Value|
|---|---|
|Description|**Dependent Component Node Type**|
|DisplayName|**Dependent Component Node Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`dependentcomponenttype`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_IsPublished"></a> IsPublished

|Property|Value|
|---|---|
|Description|**Determines whether required component is published**|
|DisplayName|**IsPublished**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ispublished`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_RequiredComponentNodeId"></a> RequiredComponentNodeId

|Property|Value|
|---|---|
|Description|**Unique identifier of the required component's node**|
|DisplayName|**Required Component**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`requiredcomponentnodeid`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|300|

### <a name="BKMK_RequiredComponentType"></a> RequiredComponentType

|Property|Value|
|---|---|
|Description|**Required Component Node Type**|
|DisplayName|**Required Component Node Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`requiredcomponenttype`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedTime](#BKMK_CreatedTime)
- [DependencyId](#BKMK_DependencyId)
- [RequiredComponentModifiedTime](#BKMK_RequiredComponentModifiedTime)

### <a name="BKMK_CreatedTime"></a> CreatedTime

|Property|Value|
|---|---|
|Description|**Date and time when the record was created.**|
|DisplayName|**Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_DependencyId"></a> DependencyId

|Property|Value|
|---|---|
|Description|**Unique identifier of a dependency.**|
|DisplayName|**Dependency Identifier**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`dependencyid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_RequiredComponentModifiedTime"></a> RequiredComponentModifiedTime

|Property|Value|
|---|---|
|Description|**Date and time when the required component was modified.**|
|DisplayName|**Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`requiredcomponentmodifiedtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.runtimedependency?displayProperty=fullName>
