---
title: "Relationship Entity (Relationship) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Relationship Entity (Relationship) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Relationship Entity (Relationship) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Relationship Entity (Relationship) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `RetrieveMultiple`<br />Event: False |`GET` /relationships<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Relationship Entity (Relationship) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Relationship Entity** |
| **DisplayCollectionName** | **Relationship Entities** |
| **SchemaName** | `Relationship` |
| **CollectionSchemaName** | `Relationships` |
| **EntitySetName** | `relationships`|
| **LogicalName** | `relationship` |
| **LogicalCollectionName** | `relationships` |
| **PrimaryIdAttribute** | `relationshipid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [EntityKeyId](#BKMK_EntityKeyId)
- [Name](#BKMK_Name)
- [RelationshipId](#BKMK_RelationshipId)

### <a name="BKMK_EntityKeyId"></a> EntityKeyId

|Property|Value|
|---|---|
|Description|**Referenced Entity's Alternate Key**|
|DisplayName|**Entity Key Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entitykeyid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the relationship.**|
|DisplayName|**Relationship Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|255|

### <a name="BKMK_RelationshipId"></a> RelationshipId

|Property|Value|
|---|---|
|Description|**Unique identifier of the entity relationship.**|
|DisplayName|**Relationship Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`relationshipid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CascadeArchive](#BKMK_CascadeArchive)
- [ComponentState](#BKMK_ComponentState)
- [IsRelationshipAttributeDenormalized](#BKMK_IsRelationshipAttributeDenormalized)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CascadeArchive"></a> CascadeArchive

|Property|Value|
|---|---|
|Description|**Cascade archive setting**|
|DisplayName|**Cascade archive setting**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`cascadearchive`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue||
|MinValue||

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

### <a name="BKMK_IsRelationshipAttributeDenormalized"></a> IsRelationshipAttributeDenormalized

|Property|Value|
|---|---|
|Description|**Is the relationship attribute denormalized.**|
|DisplayName|**IsRelationshipAttributeDenormalized**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isrelationshipattributedenormalized`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`_relationship_isrelationshipattributedenormalized`|
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

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**The version number of this relationship.**|
|DisplayName|**Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_relationship_relationshipattribute"></a> relationship_relationshipattribute

Many-To-One Relationship: [relationshipattribute relationship_relationshipattribute](relationshipattribute.md#BKMK_relationship_relationshipattribute)

|Property|Value|
|---|---|
|ReferencingEntity|`relationshipattribute`|
|ReferencingAttribute|`relationshipid`|
|ReferencedEntityNavigationPropertyName|`relationship_relationshipattribute`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.relationship?displayProperty=fullName>
