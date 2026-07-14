---
title: "Managed Property (ManagedProperty) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Managed Property (ManagedProperty) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Managed Property (ManagedProperty) table/entity reference (Microsoft Dataverse)



## Properties

The following table lists selected properties for the Managed Property (ManagedProperty) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Managed Property** |
| **DisplayCollectionName** | **Managed Properties** |
| **SchemaName** | `ManagedProperty` |
| **CollectionSchemaName** | `ManagedProperties` |
| **EntitySetName** | `managedproperties`|
| **LogicalName** | `managedproperty` |
| **LogicalCollectionName** | `managedproperties` |
| **PrimaryIdAttribute** | `managedpropertyid` |
| **PrimaryNameAttribute** |`logicalname` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [EnablesAttributeName](#BKMK_EnablesAttributeName)
- [EnablesEntityName](#BKMK_EnablesEntityName)
- [LogicalName](#BKMK_LogicalName)
- [ManagedPropertyId](#BKMK_ManagedPropertyId)
- [ManagedPropertyRowId](#BKMK_ManagedPropertyRowId)

### <a name="BKMK_EnablesAttributeName"></a> EnablesAttributeName

|Property|Value|
|---|---|
|Description|**Enables Attribute Name of this Managed Property.**|
|DisplayName|**Enables Atrribute Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`enablesattributename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_EnablesEntityName"></a> EnablesEntityName

|Property|Value|
|---|---|
|Description|**Enables Entity Name of this Managed Property.**|
|DisplayName|**Enables Entity Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`enablesentityname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_LogicalName"></a> LogicalName

|Property|Value|
|---|---|
|Description|**The logical name of this Managed Property.**|
|DisplayName|**Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`logicalname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_ManagedPropertyId"></a> ManagedPropertyId

|Property|Value|
|---|---|
|Description|**Unique identifier of the managed property key.**|
|DisplayName|**Managed Property Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`managedpropertyid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ManagedPropertyRowId"></a> ManagedPropertyRowId

|Property|Value|
|---|---|
|Description|**Unique identifier of the Managed Property**|
|DisplayName|**Managed Property Row Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`managedpropertyrowid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)

### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Component State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentstate`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`componentstate`|

#### ComponentState Choices/Options

|Value|Label|
|---|---|
|0|**Published**|
|1|**Unpublished**|
|2|**Deleted**|
|3|**Deleted Unpublished**|

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Record Overwrite Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overwritetime`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the associated solution.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.managedproperty?displayProperty=fullName>
