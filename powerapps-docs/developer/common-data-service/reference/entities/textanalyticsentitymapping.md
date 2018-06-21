---
title: "TextAnalyticsEntityMapping Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the TextAnalyticsEntityMapping entity."

services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: kvivek
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
# TextAnalyticsEntityMapping Entity Reference



## Entity Properties

**DisplayName**: Text Analytics Entity Mapping<br />
**DisplayCollectionName**: Text Analytics Entity Mappings<br />
**SchemaName**: TextAnalyticsEntityMapping<br />
**CollectionSchemaName**: TextAnalyticsEntityMappings<br />
**LogicalName**: textanalyticsentitymapping<br />
**LogicalCollectionName**: textanalyticsentitymapping<br />
**EntitySetName**: textanalyticsentitymappings<br />
**PrimaryIdAttribute**: textanalyticsentitymappingid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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

**Description**: Advanced Similarity RuleId associated with entity mapping.<br />
**DisplayName**: Advanced Similarity RuleId<br />
**LogicalName**: advancedsimilarityruleid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Lookup<br />
**Targets**: 


### <a name="BKMK_Entity"></a> Entity

**Description**: Entity<br />
**DisplayName**: Entity<br />
**LogicalName**: entity<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_EntityDisplayName"></a> EntityDisplayName

**Description**: Entity Display Name<br />
**DisplayName**: Entity Name<br />
**LogicalName**: entitydisplayname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_EntityPickList"></a> EntityPickList

**Description**: Select Entity<br />
**DisplayName**: Entity<br />
**LogicalName**: entitypicklist<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_Field"></a> Field

**Description**: Field<br />
**DisplayName**: Field<br />
**LogicalName**: field<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_FieldDisplayName"></a> FieldDisplayName

**Description**: Field Display Name<br />
**DisplayName**: Field Name<br />
**LogicalName**: fielddisplayname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_FieldPickList"></a> FieldPickList

**Description**: Select Field<br />
**DisplayName**: Field<br />
**LogicalName**: fieldpicklist<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: No
- **Value**: 2 **Label**: Yes



### <a name="BKMK_IsTextMatchMapping"></a> IsTextMatchMapping

**Description**: Specify if the mapping is for text match or exact match<br />
**DisplayName**: Criteria<br />
**LogicalName**: istextmatchmapping<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Text Match
- **FalseOption Value**: 0 **Label**: Exact Match

**DefaultValue**: True


### <a name="BKMK_KnowledgeSearchModelId"></a> KnowledgeSearchModelId

**Description**: Knowledge Search Model associated with entity mapping.<br />
**DisplayName**: Knowledge Search Model Id<br />
**LogicalName**: knowledgesearchmodelid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Lookup<br />
**Targets**: 


### <a name="BKMK_ModelType"></a> ModelType

**Description**: Model Type.<br />
**DisplayName**: Model Type<br />
**LogicalName**: modeltype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_RelationshipName"></a> RelationshipName

**Description**: Relationship Name<br />
**DisplayName**: Relationship Name<br />
**LogicalName**: relationshipname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_SimilarityRuleId"></a> SimilarityRuleId

**Description**: Similarity Rule associated with entity mapping.<br />
**DisplayName**: Similarity Rule Id<br />
**LogicalName**: similarityruleid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Lookup<br />
**Targets**: similarityrule


### <a name="BKMK_TextAnalyticsEntityMappingId"></a> TextAnalyticsEntityMappingId

**Description**: Unique identifier for entity instances<br />
**DisplayName**: Text Analytics Entity Mapping<br />
**LogicalName**: textanalyticsentitymappingid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AdvancedSimilarityRuleIdName](#BKMK_AdvancedSimilarityRuleIdName)
- [ComponentState](#BKMK_ComponentState)
- [IsManaged](#BKMK_IsManaged)
- [KnowledgeSearchModelIdName](#BKMK_KnowledgeSearchModelIdName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SimilarityRuleIdName](#BKMK_SimilarityRuleIdName)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [TextAnalyticsEntityMappingIdUnique](#BKMK_TextAnalyticsEntityMappingIdUnique)


### <a name="BKMK_AdvancedSimilarityRuleIdName"></a> AdvancedSimilarityRuleIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: advancedsimilarityruleidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ComponentState"></a> ComponentState

**Description**: For internal use only.<br />
**DisplayName**: Component State<br />
**LogicalName**: componentstate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Published
- **Value**: 1 **Label**: Unpublished
- **Value**: 2 **Label**: Deleted
- **Value**: 3 **Label**: Deleted Unpublished



### <a name="BKMK_IsManaged"></a> IsManaged

**Description**: Is Manageed<br />
**DisplayName**: State<br />
**LogicalName**: ismanaged<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Managed
- **FalseOption Value**: 0 **Label**: Unmanaged

**DefaultValue**: False


### <a name="BKMK_KnowledgeSearchModelIdName"></a> KnowledgeSearchModelIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: knowledgesearchmodelidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization associated with the Text Analytics Entity Mapping.<br />
**DisplayName**: Organization<br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: organization


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: organizationidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

**Description**: Date and time when the record was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: overwritetime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_SimilarityRuleIdName"></a> SimilarityRuleIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: similarityruleidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_SolutionId"></a> SolutionId

**Description**: Unique identifier of the associated solution.<br />
**DisplayName**: Solution<br />
**LogicalName**: solutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

**Description**: For internal use only.<br />
**DisplayName**: Solution<br />
**LogicalName**: supportingsolutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_TextAnalyticsEntityMappingIdUnique"></a> TextAnalyticsEntityMappingIdUnique

**Description**: Unique identifier of the Text Analytics Entity Mapping<br />
**DisplayName**: Text Analytics Entity Mapping Unique Id<br />
**LogicalName**: textanalyticsentitymappingidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [advancedsimilarityrule_textanalyticsentitymapping](#BKMK_advancedsimilarityrule_textanalyticsentitymapping)
- [organization_textanalyticsentitymapping](#BKMK_organization_textanalyticsentitymapping)
- [knowledgesearchmodel_textanalyticsentitymapping](#BKMK_knowledgesearchmodel_textanalyticsentitymapping)


### <a name="BKMK_advancedsimilarityrule_textanalyticsentitymapping"></a> advancedsimilarityrule_textanalyticsentitymapping

See advancedsimilarityrule Entity [advancedsimilarityrule_textanalyticsentitymapping](advancedsimilarityrule.md#BKMK_advancedsimilarityrule_textanalyticsentitymapping) One-To-Many relationship.

### <a name="BKMK_organization_textanalyticsentitymapping"></a> organization_textanalyticsentitymapping

See organization Entity [organization_textanalyticsentitymapping](organization.md#BKMK_organization_textanalyticsentitymapping) One-To-Many relationship.

### <a name="BKMK_knowledgesearchmodel_textanalyticsentitymapping"></a> knowledgesearchmodel_textanalyticsentitymapping

See knowledgesearchmodel Entity [knowledgesearchmodel_textanalyticsentitymapping](knowledgesearchmodel.md#BKMK_knowledgesearchmodel_textanalyticsentitymapping) One-To-Many relationship.
textanalyticsentitymapping

