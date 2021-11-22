---
title: "TransformationParameterMapping table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the TransformationParameterMapping table/entity."
ms.date: 10/05/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "margoc"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# TransformationParameterMapping table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

In a data map, defines parameters for a transformation.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/transformationparametermappings<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/transformationparametermappings(*transformationparametermappingid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/transformationparametermappings(*transformationparametermappingid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/transformationparametermappings<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|TransformationParameterMappings|
|DisplayCollectionName|Transformation Parameter Mappings|
|DisplayName|Transformation Parameter Mapping|
|EntitySetName|transformationparametermappings|
|IsBPFEntity|False|
|LogicalCollectionName|transformationparametermappings|
|LogicalName|transformationparametermapping|
|OwnershipType|None|
|PrimaryIdAttribute|transformationparametermappingid|
|PrimaryNameAttribute|data|
|SchemaName|TransformationParameterMapping|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Data](#BKMK_Data)
- [DataTypeCode](#BKMK_DataTypeCode)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [ParameterArrayIndex](#BKMK_ParameterArrayIndex)
- [ParameterSequence](#BKMK_ParameterSequence)
- [ParameterTypeCode](#BKMK_ParameterTypeCode)
- [TransformationMappingId](#BKMK_TransformationMappingId)
- [TransformationParameterMappingId](#BKMK_TransformationParameterMappingId)


### <a name="BKMK_Data"></a> Data

|Property|Value|
|--------|-----|
|Description|Transformation data for transformation parameter|
|DisplayName|Data|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|data|
|MaxLength|500|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_DataTypeCode"></a> DataTypeCode

|Property|Value|
|--------|-----|
|Description|Data type of the transformation parameter.|
|DisplayName|Parameter Data Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|datatypecode|
|RequiredLevel|None|
|Type|Picklist|

#### DataTypeCode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Reference||
|1|Value||



### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|--------|-----|
|Description|Version in which the component is introduced.|
|DisplayName|Introduced Version|
|FormatName|VersionNumber|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|introducedversion|
|MaxLength|48|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ParameterArrayIndex"></a> ParameterArrayIndex

|Property|Value|
|--------|-----|
|Description|Index of the array if the input parameter is an array.|
|DisplayName|Parameter Array Index|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|parameterarrayindex|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ParameterSequence"></a> ParameterSequence

|Property|Value|
|--------|-----|
|Description|Parameter sequence number.|
|DisplayName|Parameter Sequence|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|parametersequence|
|MaxValue|2147483647|
|MinValue|1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ParameterTypeCode"></a> ParameterTypeCode

|Property|Value|
|--------|-----|
|Description|Type of transformation parameter.|
|DisplayName|Parameter Type|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|parametertypecode|
|RequiredLevel|None|
|Type|Picklist|

#### ParameterTypeCode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Input||
|1|Output||



### <a name="BKMK_TransformationMappingId"></a> TransformationMappingId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the transformation with which the parameter is associated.|
|DisplayName|Transformation Mapping Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|transformationmappingid|
|RequiredLevel|None|
|Targets|transformationmapping|
|Type|Lookup|


### <a name="BKMK_TransformationParameterMappingId"></a> TransformationParameterMappingId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the transformation parameter mapping.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|transformationparametermappingid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [TransformationMappingIdName](#BKMK_TransformationMappingIdName)
- [TransformationParameterMappingIdUnique](#BKMK_TransformationParameterMappingIdUnique)


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



### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the parameter mapping.|
|DisplayName|Created By|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the transformation parameter mapping was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the transformationparametermapping.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|--------|-----|
|Description|Information that specifies whether this component is managed.|
|DisplayName|State|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsManaged Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Managed|
|0|Unmanaged|

**DefaultValue**: False



### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the transformation parameter mapping.|
|DisplayName|Modified By|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the transformation parameter mapping was last modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who last modified the transformationparametermapping.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|supportingsolutionid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_TransformationMappingIdName"></a> TransformationMappingIdName

|Property|Value|
|--------|-----|
|Description|Name of the transformation.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|transformationmappingidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_TransformationParameterMappingIdUnique"></a> TransformationParameterMappingIdUnique

|Property|Value|
|--------|-----|
|Description|Unique identifier of the Transformation Parameter Mapping.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|transformationparametermappingidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_LookUpMapping_TransformationParameterMapping"></a> LookUpMapping_TransformationParameterMapping

Same as lookupmapping table [LookUpMapping_TransformationParameterMapping](lookupmapping.md#BKMK_LookUpMapping_TransformationParameterMapping) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|lookupmapping|
|ReferencingAttribute|transformationparametermappingid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|LookUpMapping_TransformationParameterMapping|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [TransformationParameterMapping_TransformationMapping](#BKMK_TransformationParameterMapping_TransformationMapping)
- [lk_transformationparametermapping_modifiedonbehalfby](#BKMK_lk_transformationparametermapping_modifiedonbehalfby)
- [lk_transformationparametermapping_createdonbehalfby](#BKMK_lk_transformationparametermapping_createdonbehalfby)
- [lk_transformationparametermapping_modifiedby](#BKMK_lk_transformationparametermapping_modifiedby)
- [lk_transformationparametermapping_createdby](#BKMK_lk_transformationparametermapping_createdby)


### <a name="BKMK_TransformationParameterMapping_TransformationMapping"></a> TransformationParameterMapping_TransformationMapping

See transformationmapping Table [TransformationParameterMapping_TransformationMapping](transformationmapping.md#BKMK_TransformationParameterMapping_TransformationMapping) One-To-Many relationship.

### <a name="BKMK_lk_transformationparametermapping_modifiedonbehalfby"></a> lk_transformationparametermapping_modifiedonbehalfby

See systemuser Table [lk_transformationparametermapping_modifiedonbehalfby](systemuser.md#BKMK_lk_transformationparametermapping_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_transformationparametermapping_createdonbehalfby"></a> lk_transformationparametermapping_createdonbehalfby

See systemuser Table [lk_transformationparametermapping_createdonbehalfby](systemuser.md#BKMK_lk_transformationparametermapping_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_transformationparametermapping_modifiedby"></a> lk_transformationparametermapping_modifiedby

See systemuser Table [lk_transformationparametermapping_modifiedby](systemuser.md#BKMK_lk_transformationparametermapping_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_transformationparametermapping_createdby"></a> lk_transformationparametermapping_createdby

See systemuser Table [lk_transformationparametermapping_createdby](systemuser.md#BKMK_lk_transformationparametermapping_createdby) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.transformationparametermapping?text=transformationparametermapping EntityType" />