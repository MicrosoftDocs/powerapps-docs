---
title: "ImportEntityMapping table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the ImportEntityMapping table/entity."
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

# ImportEntityMapping table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Mapping for entities in a data map.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/importentitymappings<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/importentitymappings(*importentitymappingid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/importentitymappings(*importentitymappingid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/importentitymappings<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|ImportEntityMappings|
|DisplayCollectionName|Import Entity Mappings|
|DisplayName|Import Entity Mapping|
|EntitySetName|importentitymappings|
|IsBPFEntity|False|
|LogicalCollectionName|importentitymappings|
|LogicalName|importentitymapping|
|OwnershipType|None|
|PrimaryIdAttribute|importentitymappingid|
|PrimaryNameAttribute||
|SchemaName|ImportEntityMapping|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [DeDupe](#BKMK_DeDupe)
- [ImportEntityMappingId](#BKMK_ImportEntityMappingId)
- [ImportMapId](#BKMK_ImportMapId)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [ProcessCode](#BKMK_ProcessCode)
- [SourceEntityName](#BKMK_SourceEntityName)
- [StatusCode](#BKMK_StatusCode)
- [TargetEntityName](#BKMK_TargetEntityName)


### <a name="BKMK_DeDupe"></a> DeDupe

|Property|Value|
|--------|-----|
|Description|Information about whether the entity needs to be processed to find and delete duplicate records.|
|DisplayName|Remove Duplicates|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|dedupe|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### DeDupe Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Ignore||
|2|Eliminate||



### <a name="BKMK_ImportEntityMappingId"></a> ImportEntityMappingId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the import entity mapping.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|importentitymappingid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ImportMapId"></a> ImportMapId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the associated data map.|
|DisplayName|Data Map ID|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|importmapid|
|RequiredLevel|ApplicationRequired|
|Targets|importmap|
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


### <a name="BKMK_ProcessCode"></a> ProcessCode

|Property|Value|
|--------|-----|
|Description|Information about whether the import entity mapping needs to be processed.|
|DisplayName|Process Code|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|processcode|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ProcessCode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Process||
|2|Ignore||
|3|Internal||



### <a name="BKMK_SourceEntityName"></a> SourceEntityName

|Property|Value|
|--------|-----|
|Description|Name of the source entity.|
|DisplayName|Source Entity Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|sourceentityname|
|MaxLength|160|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the import entity mapping.|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|SystemRequired|
|Type|Status|

#### StatusCode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Active|0|



### <a name="BKMK_TargetEntityName"></a> TargetEntityName

|Property|Value|
|--------|-----|
|Description|Name of the Microsoft Dynamics 365 entity.|
|DisplayName|Target Entity|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|targetentityname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|

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
- [ImportEntityMappingIdUnique](#BKMK_ImportEntityMappingIdUnique)
- [ImportMapIdName](#BKMK_ImportMapIdName)
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
- [StateCode](#BKMK_StateCode)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)


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
|Description|Unique identifier of the user who created the import entity mapping.|
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
|Description|Date and time when the import entity mapping was created.|
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
|Description|Unique identifier of the delegate user who created the importentitymapping.|
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


### <a name="BKMK_ImportEntityMappingIdUnique"></a> ImportEntityMappingIdUnique

|Property|Value|
|--------|-----|
|Description|Unique identifier of the Import Entity Mapping.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|importentitymappingidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ImportMapIdName"></a> ImportMapIdName

|Property|Value|
|--------|-----|
|Description|Name of the associated data map.|
|DisplayName|Data Map|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|importmapidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
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
|Description|Unique identifier of the user who last modified the import entity mapping.|
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
|Description|Date and time when the import entity mapping was last modified.|
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
|Description|Unique identifier of the delegate user who last modified the importentitymapping.|
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
|Description|Status of the import entity mapping.|
|DisplayName|Status|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### StateCode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|1|Active|



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

- [lk_importentitymapping_createdonbehalfby](#BKMK_lk_importentitymapping_createdonbehalfby)
- [lk_importentitymapping_modifiedonbehalfby](#BKMK_lk_importentitymapping_modifiedonbehalfby)
- [lk_importentitymapping_createdby](#BKMK_lk_importentitymapping_createdby)
- [ImportEntityMapping_ImportMap](#BKMK_ImportEntityMapping_ImportMap)
- [lk_importentitymapping_modifiedby](#BKMK_lk_importentitymapping_modifiedby)


### <a name="BKMK_lk_importentitymapping_createdonbehalfby"></a> lk_importentitymapping_createdonbehalfby

See systemuser Table [lk_importentitymapping_createdonbehalfby](systemuser.md#BKMK_lk_importentitymapping_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_importentitymapping_modifiedonbehalfby"></a> lk_importentitymapping_modifiedonbehalfby

See systemuser Table [lk_importentitymapping_modifiedonbehalfby](systemuser.md#BKMK_lk_importentitymapping_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_importentitymapping_createdby"></a> lk_importentitymapping_createdby

See systemuser Table [lk_importentitymapping_createdby](systemuser.md#BKMK_lk_importentitymapping_createdby) One-To-Many relationship.

### <a name="BKMK_ImportEntityMapping_ImportMap"></a> ImportEntityMapping_ImportMap

See importmap Table [ImportEntityMapping_ImportMap](importmap.md#BKMK_ImportEntityMapping_ImportMap) One-To-Many relationship.

### <a name="BKMK_lk_importentitymapping_modifiedby"></a> lk_importentitymapping_modifiedby

See systemuser Table [lk_importentitymapping_modifiedby](systemuser.md#BKMK_lk_importentitymapping_modifiedby) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.importentitymapping?text=importentitymapping EntityType" />