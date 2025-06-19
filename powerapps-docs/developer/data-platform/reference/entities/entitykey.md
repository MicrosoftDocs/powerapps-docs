---
title: "Entity Key (EntityKey) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Entity Key (EntityKey) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Entity Key (EntityKey) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Entity Key (EntityKey) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `RetrieveMultiple`<br />Event: False |`GET` /entitykeys<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Entity Key (EntityKey) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Entity Key** |
| **DisplayCollectionName** | **Entity Keys** |
| **SchemaName** | `EntityKey` |
| **CollectionSchemaName** | `EntityKeys` |
| **EntitySetName** | `entitykeys`|
| **LogicalName** | `entitykey` |
| **LogicalCollectionName** | `entitykeys` |
| **PrimaryIdAttribute** | `entitykeyid` |
| **PrimaryNameAttribute** |`logicalname` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [EntityKeyId](#BKMK_EntityKeyId)
- [LogicalName](#BKMK_LogicalName)
- [Name](#BKMK_Name)

### <a name="BKMK_EntityKeyId"></a> EntityKeyId

|Property|Value|
|---|---|
|Description|**Unique identifier of the entity key.**|
|DisplayName|**Entity Key**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entitykeyid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_LogicalName"></a> LogicalName

|Property|Value|
|---|---|
|Description|**The logical name of this Entity Key.**|
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

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**The name of this Entity Key.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [IsSecondaryKey](#BKMK_IsSecondaryKey)
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

### <a name="BKMK_IsSecondaryKey"></a> IsSecondaryKey

|Property|Value|
|---|---|
|Description|**Is the attribute secondary key.**|
|DisplayName|**IsSecondaryKey**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`issecondarykey`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`_entitykey_issecondarykey`|
|DefaultValue|False|
|True Label||
|False Label||

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
<xref:Microsoft.Dynamics.CRM.entitykey?displayProperty=fullName>
