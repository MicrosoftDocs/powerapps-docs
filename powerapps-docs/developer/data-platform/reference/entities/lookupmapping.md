---
title: "LookUpMapping table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the LookUpMapping table/entity."
ms.date: 05/20/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# LookUpMapping table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

In a data map, maps a lookup attribute in a source file to Microsoft Dynamics 365.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/lookupmappings<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/lookupmappings(*lookupmappingid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/lookupmappings(*lookupmappingid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/lookupmappings<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|LookUpMappings|
|DisplayCollectionName|Lookup Mappings|
|DisplayName|Lookup Mapping|
|EntitySetName|lookupmappings|
|IsBPFEntity|False|
|LogicalCollectionName|lookupmappings|
|LogicalName|lookupmapping|
|OwnershipType|None|
|PrimaryIdAttribute|lookupmappingid|
|PrimaryNameAttribute||
|SchemaName|LookUpMapping|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ColumnMappingId](#BKMK_ColumnMappingId)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [LookUpAttributeName](#BKMK_LookUpAttributeName)
- [LookUpEntityName](#BKMK_LookUpEntityName)
- [LookUpMappingId](#BKMK_LookUpMappingId)
- [LookUpSourceCode](#BKMK_LookUpSourceCode)
- [ProcessCode](#BKMK_ProcessCode)
- [StatusCode](#BKMK_StatusCode)
- [TransformationParameterMappingId](#BKMK_TransformationParameterMappingId)


### <a name="BKMK_ColumnMappingId"></a> ColumnMappingId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the column mapping with which this lookup mapping is associated.|
|DisplayName|Column Mapping Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|columnmappingid|
|RequiredLevel|None|
|Targets|columnmapping|
|Type|Lookup|


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


### <a name="BKMK_LookUpAttributeName"></a> LookUpAttributeName

|Property|Value|
|--------|-----|
|Description|Name of the field with which the lookup is associated.|
|DisplayName|Lookup Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lookupattributename|
|MaxLength|160|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_LookUpEntityName"></a> LookUpEntityName

|Property|Value|
|--------|-----|
|Description|Name of the entity with which the lookup is associated.|
|DisplayName|Lookup Entity Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lookupentityname|
|MaxLength|160|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_LookUpMappingId"></a> LookUpMappingId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the lookup mapping.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|lookupmappingid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_LookUpSourceCode"></a> LookUpSourceCode

|Property|Value|
|--------|-----|
|Description|Lookup source code for lookup mapping.|
|DisplayName|Lookup Source|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lookupsourcecode|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### LookUpSourceCode Choices/Options

|Value|Label|
|-----|-----|
|0|Source|
|1|System|



### <a name="BKMK_ProcessCode"></a> ProcessCode

|Property|Value|
|--------|-----|
|Description|Information about whether the lookup mapping has to be processed.|
|DisplayName|Process Code|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|processcode|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ProcessCode Choices/Options

|Value|Label|
|-----|-----|
|1|Process|
|2|Ignore|
|3|Internal|



### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the lookup mapping.|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|SystemRequired|
|Type|Status|

#### StatusCode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|0|Active|0|



### <a name="BKMK_TransformationParameterMappingId"></a> TransformationParameterMappingId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the transformation parameter mapping with which this lookup mapping is associated.|
|DisplayName|Transformation Parameter Mapping Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|transformationparametermappingid|
|RequiredLevel|None|
|Targets|transformationparametermapping|
|Type|Lookup|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ColumnMappingIdName](#BKMK_ColumnMappingIdName)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IsManaged](#BKMK_IsManaged)
- [LookUpMappingIdUnique](#BKMK_LookUpMappingIdUnique)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [StateCode](#BKMK_StateCode)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)


### <a name="BKMK_ColumnMappingIdName"></a> ColumnMappingIdName

|Property|Value|
|--------|-----|
|Description|Name of the column mapping.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|columnmappingidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


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

|Value|Label|
|-----|-----|
|0|Published|
|1|Unpublished|
|2|Deleted|
|3|Deleted Unpublished|



### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the lookup mapping.|
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
|Description|Date and time when the lookup mapping was created.|
|DisplayName||
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the lookupmapping.|
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

|Value|Label|
|-----|-----|
|1|Managed|
|0|Unmanaged|

**DefaultValue**: False



### <a name="BKMK_LookUpMappingIdUnique"></a> LookUpMappingIdUnique

|Property|Value|
|--------|-----|
|Description|Unique identifier of the LookUp Mapping.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|lookupmappingidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the lookup mapping.|
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
|Description|Date and time when the lookup mapping was last modified.|
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
|Description|Unique identifier of the delegate user who last modified the lookupmapping.|
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


### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|--------|-----|
|Description|Status of the lookup mapping.|
|DisplayName|Status|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### StateCode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|0|Active|



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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_lookupmapping_createdby](#BKMK_lk_lookupmapping_createdby)
- [lk_lookupmapping_createdonbehalfby](#BKMK_lk_lookupmapping_createdonbehalfby)
- [LookUpMapping_ColumnMapping](#BKMK_LookUpMapping_ColumnMapping)
- [lk_lookupmapping_modifiedby](#BKMK_lk_lookupmapping_modifiedby)
- [LookUpMapping_TransformationParameterMapping](#BKMK_LookUpMapping_TransformationParameterMapping)
- [lk_lookupmapping_modifiedonbehalfby](#BKMK_lk_lookupmapping_modifiedonbehalfby)


### <a name="BKMK_lk_lookupmapping_createdby"></a> lk_lookupmapping_createdby

See systemuser Table [lk_lookupmapping_createdby](systemuser.md#BKMK_lk_lookupmapping_createdby) One-To-Many relationship.

### <a name="BKMK_lk_lookupmapping_createdonbehalfby"></a> lk_lookupmapping_createdonbehalfby

See systemuser Table [lk_lookupmapping_createdonbehalfby](systemuser.md#BKMK_lk_lookupmapping_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_LookUpMapping_ColumnMapping"></a> LookUpMapping_ColumnMapping

See columnmapping Table [LookUpMapping_ColumnMapping](columnmapping.md#BKMK_LookUpMapping_ColumnMapping) One-To-Many relationship.

### <a name="BKMK_lk_lookupmapping_modifiedby"></a> lk_lookupmapping_modifiedby

See systemuser Table [lk_lookupmapping_modifiedby](systemuser.md#BKMK_lk_lookupmapping_modifiedby) One-To-Many relationship.

### <a name="BKMK_LookUpMapping_TransformationParameterMapping"></a> LookUpMapping_TransformationParameterMapping

See transformationparametermapping Table [LookUpMapping_TransformationParameterMapping](transformationparametermapping.md#BKMK_LookUpMapping_TransformationParameterMapping) One-To-Many relationship.

### <a name="BKMK_lk_lookupmapping_modifiedonbehalfby"></a> lk_lookupmapping_modifiedonbehalfby

See systemuser Table [lk_lookupmapping_modifiedonbehalfby](systemuser.md#BKMK_lk_lookupmapping_modifiedonbehalfby) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.lookupmapping?text=lookupmapping EntityType" />