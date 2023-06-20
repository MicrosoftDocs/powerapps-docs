---
title: "EntityRelationship table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the EntityRelationship table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# EntityRelationship table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).




## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|RetrieveMultiple|GET /entityrelationships<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|EntityRelationships|
|DisplayCollectionName|Entity Relationships|
|DisplayName|Entity Relationship|
|EntitySetName|entityrelationships|
|IsBPFEntity|False|
|LogicalCollectionName|entityrelationships|
|LogicalName|entityrelationship|
|OwnershipType|None|
|PrimaryIdAttribute|entityrelationshipid|
|PrimaryNameAttribute|schemaname|
|SchemaName|EntityRelationship|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [EntityRelationshipId](#BKMK_EntityRelationshipId)
- [SchemaName](#BKMK_SchemaName)


### <a name="BKMK_EntityRelationshipId"></a> EntityRelationshipId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the entity relationship.|
|DisplayName|Entity Relationship|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|entityrelationshipid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SchemaName"></a> SchemaName

|Property|Value|
|--------|-----|
|Description|The name of this Entity Relationship.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|schemaname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)


### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Component State|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentstate|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ComponentState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Published||
|1|Unpublished||
|2|Deleted||
|3|Deleted Unpublished||



### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Record Overwrite Time|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overwritetime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the associated solution.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|solutionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_entityrelationship_config"></a> entityrelationship_config

**Added by**: Solution Component Configuration Solution

Same as the [entityrelationship_config](solutioncomponentrelationshipconfiguration.md#BKMK_entityrelationship_config) many-to-one relationship for the [solutioncomponentrelationshipconfiguration](solutioncomponentrelationshipconfiguration.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentrelationshipconfiguration|
|ReferencingAttribute|entityrelationshipid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|entityrelationship_config|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.entityrelationship?text=entityrelationship EntityType" />