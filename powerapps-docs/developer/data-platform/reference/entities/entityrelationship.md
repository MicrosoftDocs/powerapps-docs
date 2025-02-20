---
title: "Entity Relationship (EntityRelationship) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Entity Relationship (EntityRelationship) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Entity Relationship (EntityRelationship) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Entity Relationship (EntityRelationship) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `RetrieveMultiple`<br />Event: False |`GET` /entityrelationships<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Entity Relationship (EntityRelationship) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Entity Relationship** |
| **DisplayCollectionName** | **Entity Relationships** |
| **SchemaName** | `EntityRelationship` |
| **CollectionSchemaName** | `EntityRelationships` |
| **EntitySetName** | `entityrelationships`|
| **LogicalName** | `entityrelationship` |
| **LogicalCollectionName** | `entityrelationships` |
| **PrimaryIdAttribute** | `entityrelationshipid` |
| **PrimaryNameAttribute** |`schemaname` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [EntityRelationshipId](#BKMK_EntityRelationshipId)
- [SchemaName](#BKMK_SchemaName)

### <a name="BKMK_EntityRelationshipId"></a> EntityRelationshipId

|Property|Value|
|---|---|
|Description|**Unique identifier of the entity relationship.**|
|DisplayName|**Entity Relationship**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityrelationshipid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SchemaName"></a> SchemaName

|Property|Value|
|---|---|
|Description|**The name of this Entity Relationship.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`schemaname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|


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

## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_entityrelationship_config"></a> entityrelationship_config

Many-To-One Relationship: [solutioncomponentrelationshipconfiguration entityrelationship_config](solutioncomponentrelationshipconfiguration.md#BKMK_entityrelationship_config)

|Property|Value|
|---|---|
|ReferencingEntity|`solutioncomponentrelationshipconfiguration`|
|ReferencingAttribute|`entityrelationshipid`|
|ReferencedEntityNavigationPropertyName|`entityrelationship_config`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.entityrelationship?displayProperty=fullName>
