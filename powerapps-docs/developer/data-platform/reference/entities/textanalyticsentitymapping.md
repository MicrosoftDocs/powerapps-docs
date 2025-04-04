---
title: "Text Analytics Entity Mapping (TextAnalyticsEntityMapping) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Text Analytics Entity Mapping (TextAnalyticsEntityMapping) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Text Analytics Entity Mapping (TextAnalyticsEntityMapping) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Text Analytics Entity Mapping (TextAnalyticsEntityMapping) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /textanalyticsentitymappings<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /textanalyticsentitymappings(*textanalyticsentitymappingid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /textanalyticsentitymappings(*textanalyticsentitymappingid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /textanalyticsentitymappings<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /textanalyticsentitymappings(*textanalyticsentitymappingid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /textanalyticsentitymappings(*textanalyticsentitymappingid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Text Analytics Entity Mapping (TextAnalyticsEntityMapping) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Text Analytics Entity Mapping** |
| **DisplayCollectionName** | **Text Analytics Entity Mappings** |
| **SchemaName** | `TextAnalyticsEntityMapping` |
| **CollectionSchemaName** | `TextAnalyticsEntityMappings` |
| **EntitySetName** | `textanalyticsentitymappings`|
| **LogicalName** | `textanalyticsentitymapping` |
| **LogicalCollectionName** | `textanalyticsentitymapping` |
| **PrimaryIdAttribute** | `textanalyticsentitymappingid` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AdvancedSimilarityRuleId](#BKMK_AdvancedSimilarityRuleId)
- [Entity](#BKMK_Entity)
- [EntityDisplayName](#BKMK_EntityDisplayName)
- [EntityPickList](#BKMK_EntityPickList)
- [Field](#BKMK_Field)
- [FieldDisplayName](#BKMK_FieldDisplayName)
- [FieldPickList](#BKMK_FieldPickList)
- [IsTextMatchMapping](#BKMK_IsTextMatchMapping)
- [KnowledgeSearchModelId](#BKMK_KnowledgeSearchModelId)
- [ModelType](#BKMK_ModelType)
- [RelationshipName](#BKMK_RelationshipName)
- [SimilarityRuleId](#BKMK_SimilarityRuleId)
- [TextAnalyticsEntityMappingId](#BKMK_TextAnalyticsEntityMappingId)

### <a name="BKMK_AdvancedSimilarityRuleId"></a> AdvancedSimilarityRuleId

|Property|Value|
|---|---|
|Description|**Advanced Similarity RuleId associated with entity mapping.**|
|DisplayName|**Advanced Similarity RuleId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`advancedsimilarityruleid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets||

### <a name="BKMK_Entity"></a> Entity

|Property|Value|
|---|---|
|Description|**Entity**|
|DisplayName|**Entity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entity`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_EntityDisplayName"></a> EntityDisplayName

|Property|Value|
|---|---|
|Description|**Entity Display Name**|
|DisplayName|**Entity Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entitydisplayname`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_EntityPickList"></a> EntityPickList

|Property|Value|
|---|---|
|Description|**Select Entity**|
|DisplayName|**Entity**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entitypicklist`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`textanalyticsentitymapping_entity`|

#### EntityPickList Choices/Options

|Value|Label|
|---|---|
|1|**No**|
|2|**Yes**|

### <a name="BKMK_Field"></a> Field

|Property|Value|
|---|---|
|Description|**Field**|
|DisplayName|**Field**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`field`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_FieldDisplayName"></a> FieldDisplayName

|Property|Value|
|---|---|
|Description|**Field Display Name**|
|DisplayName|**Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`fielddisplayname`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_FieldPickList"></a> FieldPickList

|Property|Value|
|---|---|
|Description|**Select Field**|
|DisplayName|**Field**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fieldpicklist`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`textanalyticsentitymapping_fields`|

#### FieldPickList Choices/Options

|Value|Label|
|---|---|
|1|**No**|
|2|**Yes**|

### <a name="BKMK_IsTextMatchMapping"></a> IsTextMatchMapping

|Property|Value|
|---|---|
|Description|**Specify if the mapping is for text match or exact match**|
|DisplayName|**Criteria**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`istextmatchmapping`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`textanalyticsentitymapping_istextmatchmapping`|
|DefaultValue|True|
|True Label|Text Match|
|False Label|Exact Match|

### <a name="BKMK_KnowledgeSearchModelId"></a> KnowledgeSearchModelId

|Property|Value|
|---|---|
|Description|**Knowledge Search Model associated with entity mapping.**|
|DisplayName|**Knowledge Search Model Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`knowledgesearchmodelid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets||

### <a name="BKMK_ModelType"></a> ModelType

|Property|Value|
|---|---|
|Description|**Model Type.**|
|DisplayName|**Model Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modeltype`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_RelationshipName"></a> RelationshipName

|Property|Value|
|---|---|
|Description|**Relationship Name**|
|DisplayName|**Relationship Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`relationshipname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_SimilarityRuleId"></a> SimilarityRuleId

|Property|Value|
|---|---|
|Description|**Similarity Rule associated with entity mapping.**|
|DisplayName|**Similarity Rule Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`similarityruleid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|similarityrule|

### <a name="BKMK_TextAnalyticsEntityMappingId"></a> TextAnalyticsEntityMappingId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Text Analytics Entity Mapping**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`textanalyticsentitymappingid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [IsManaged](#BKMK_IsManaged)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [TextAnalyticsEntityMappingIdUnique](#BKMK_TextAnalyticsEntityMappingIdUnique)

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

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Is Manageed**|
|DisplayName|**State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization associated with the Text Analytics Entity Mapping.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**Date and time when the record was created.**|
|DisplayName|**Created On**|
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

### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`supportingsolutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_TextAnalyticsEntityMappingIdUnique"></a> TextAnalyticsEntityMappingIdUnique

|Property|Value|
|---|---|
|Description|**Unique identifier of the Text Analytics Entity Mapping**|
|DisplayName|**Text Analytics Entity Mapping Unique Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`textanalyticsentitymappingidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [organization_textanalyticsentitymapping](#BKMK_organization_textanalyticsentitymapping)
- [similarityrule_textanalyticsentitymapping](#BKMK_similarityrule_textanalyticsentitymapping)

### <a name="BKMK_organization_textanalyticsentitymapping"></a> organization_textanalyticsentitymapping

One-To-Many Relationship: [organization organization_textanalyticsentitymapping](organization.md#BKMK_organization_textanalyticsentitymapping)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_similarityrule_textanalyticsentitymapping"></a> similarityrule_textanalyticsentitymapping

One-To-Many Relationship: [similarityrule similarityrule_textanalyticsentitymapping](similarityrule.md#BKMK_similarityrule_textanalyticsentitymapping)

|Property|Value|
|---|---|
|ReferencedEntity|`similarityrule`|
|ReferencedAttribute|`similarityruleid`|
|ReferencingAttribute|`similarityruleid`|
|ReferencingEntityNavigationPropertyName|`similarityruleid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.textanalyticsentitymapping?displayProperty=fullName>
