---
title: "Relationship Entity (Relationship)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Relationship Entity (Relationship)  table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Relationship Entity (Relationship)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).




## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|RetrieveMultiple|GET /relationships<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|Relationships|
|DisplayCollectionName|Relationship Entities|
|DisplayName|Relationship Entity|
|EntitySetName|relationships|
|IsBPFEntity|False|
|LogicalCollectionName|relationships|
|LogicalName|relationship|
|OwnershipType|None|
|PrimaryIdAttribute|relationshipid|
|PrimaryNameAttribute|name|
|SchemaName|Relationship|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [EntityKeyId](#BKMK_EntityKeyId)
- [Name](#BKMK_Name)
- [RelationshipId](#BKMK_RelationshipId)


### <a name="BKMK_EntityKeyId"></a> EntityKeyId

|Property|Value|
|--------|-----|
|Description|Referenced Entity's Alternate Key|
|DisplayName|Entity Key Id|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|entitykeyid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of the relationship.|
|DisplayName|Relationship Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|name|
|MaxLength|255|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_RelationshipId"></a> RelationshipId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the entity relationship.|
|DisplayName|Relationship Id|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|relationshipid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CascadeArchive](#BKMK_CascadeArchive)
- [ComponentState](#BKMK_ComponentState)
- [IsRelationshipAttributeDenormalized](#BKMK_IsRelationshipAttributeDenormalized)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CascadeArchive"></a> CascadeArchive

**Added by**: Metadata Extension Solution

|Property|Value|
|--------|-----|
|Description|Cascade archive setting|
|DisplayName|Cascade archive setting|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|cascadearchive|
|MaxValue||
|MinValue||
|RequiredLevel|SystemRequired|
|Type|Integer|


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



### <a name="BKMK_IsRelationshipAttributeDenormalized"></a> IsRelationshipAttributeDenormalized

**Added by**: Metadata Extension Solution

|Property|Value|
|--------|-----|
|Description|Is the relationship attribute denormalized.|
|DisplayName|IsRelationshipAttributeDenormalized|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isrelationshipattributedenormalized|
|RequiredLevel|None|
|Type|Boolean|

#### IsRelationshipAttributeDenormalized Choices/Options

|Value|Label|Description|
|-----|-----|--------|


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


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Added by**: Metadata Extension Solution

|Property|Value|
|--------|-----|
|Description|The version number of this relationship.|
|DisplayName|Version Number|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_relationship_relationshipattribute"></a> relationship_relationshipattribute

**Added by**: Metadata Extension Solution

Same as the [relationship_relationshipattribute](relationshipattribute.md#BKMK_relationship_relationshipattribute) many-to-one relationship for the [relationshipattribute](relationshipattribute.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|relationshipattribute|
|ReferencingAttribute|relationshipid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|relationship_relationshipattribute|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.relationship?text=relationship EntityType" />