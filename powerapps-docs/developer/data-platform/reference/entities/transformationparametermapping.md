---
title: "Transformation Parameter Mapping (TransformationParameterMapping) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Transformation Parameter Mapping (TransformationParameterMapping) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Transformation Parameter Mapping (TransformationParameterMapping) table/entity reference (Microsoft Dataverse)

In a data map, defines parameters for a transformation.

## Messages

The following table lists the messages for the Transformation Parameter Mapping (TransformationParameterMapping) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /transformationparametermappings<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /transformationparametermappings(*transformationparametermappingid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /transformationparametermappings(*transformationparametermappingid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /transformationparametermappings<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Transformation Parameter Mapping (TransformationParameterMapping) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Transformation Parameter Mapping** |
| **DisplayCollectionName** | **Transformation Parameter Mappings** |
| **SchemaName** | `TransformationParameterMapping` |
| **CollectionSchemaName** | `TransformationParameterMappings` |
| **EntitySetName** | `transformationparametermappings`|
| **LogicalName** | `transformationparametermapping` |
| **LogicalCollectionName** | `transformationparametermappings` |
| **PrimaryIdAttribute** | `transformationparametermappingid` |
| **PrimaryNameAttribute** |`data` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

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
|---|---|
|Description|**Transformation data for transformation parameter**|
|DisplayName|**Data**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`data`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_DataTypeCode"></a> DataTypeCode

|Property|Value|
|---|---|
|Description|**Data type of the transformation parameter.**|
|DisplayName|**Parameter Data Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`datatypecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`transformationparametermapping_datatypecode`|

#### DataTypeCode Choices/Options

|Value|Label|
|---|---|
|0|**Reference**|
|1|**Value**|

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Version in which the component is introduced.**|
|DisplayName|**Introduced Version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`introducedversion`|
|RequiredLevel|None|
|Type|String|
|Format|VersionNumber|
|FormatName|VersionNumber|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|48|

### <a name="BKMK_ParameterArrayIndex"></a> ParameterArrayIndex

|Property|Value|
|---|---|
|Description|**Index of the array if the input parameter is an array.**|
|DisplayName|**Parameter Array Index**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parameterarrayindex`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ParameterSequence"></a> ParameterSequence

|Property|Value|
|---|---|
|Description|**Parameter sequence number.**|
|DisplayName|**Parameter Sequence**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parametersequence`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|1|

### <a name="BKMK_ParameterTypeCode"></a> ParameterTypeCode

|Property|Value|
|---|---|
|Description|**Type of transformation parameter.**|
|DisplayName|**Parameter Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parametertypecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`transformationparametermapping_parametertypecode`|

#### ParameterTypeCode Choices/Options

|Value|Label|
|---|---|
|0|**Input**|
|1|**Output**|

### <a name="BKMK_TransformationMappingId"></a> TransformationMappingId

|Property|Value|
|---|---|
|Description|**Unique identifier of the transformation with which the parameter is associated.**|
|DisplayName|**Transformation Mapping Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`transformationmappingid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|transformationmapping|

### <a name="BKMK_TransformationParameterMappingId"></a> TransformationParameterMappingId

|Property|Value|
|---|---|
|Description|**Unique identifier of the transformation parameter mapping.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`transformationparametermappingid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [TransformationParameterMappingIdUnique](#BKMK_TransformationParameterMappingIdUnique)

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

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the parameter mapping.**|
|DisplayName|**Created By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the transformation parameter mapping was created.**|
|DisplayName|**Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who created the transformationparametermapping.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Information that specifies whether this component is managed.**|
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

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the transformation parameter mapping.**|
|DisplayName|**Modified By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the transformation parameter mapping was last modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedon`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who last modified the transformationparametermapping.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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

### <a name="BKMK_TransformationParameterMappingIdUnique"></a> TransformationParameterMappingIdUnique

|Property|Value|
|---|---|
|Description|**Unique identifier of the Transformation Parameter Mapping.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`transformationparametermappingidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [lk_transformationparametermapping_createdby](#BKMK_lk_transformationparametermapping_createdby)
- [lk_transformationparametermapping_createdonbehalfby](#BKMK_lk_transformationparametermapping_createdonbehalfby)
- [lk_transformationparametermapping_modifiedby](#BKMK_lk_transformationparametermapping_modifiedby)
- [lk_transformationparametermapping_modifiedonbehalfby](#BKMK_lk_transformationparametermapping_modifiedonbehalfby)
- [TransformationParameterMapping_TransformationMapping](#BKMK_TransformationParameterMapping_TransformationMapping)

### <a name="BKMK_lk_transformationparametermapping_createdby"></a> lk_transformationparametermapping_createdby

One-To-Many Relationship: [systemuser lk_transformationparametermapping_createdby](systemuser.md#BKMK_lk_transformationparametermapping_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_transformationparametermapping_createdonbehalfby"></a> lk_transformationparametermapping_createdonbehalfby

One-To-Many Relationship: [systemuser lk_transformationparametermapping_createdonbehalfby](systemuser.md#BKMK_lk_transformationparametermapping_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_transformationparametermapping_modifiedby"></a> lk_transformationparametermapping_modifiedby

One-To-Many Relationship: [systemuser lk_transformationparametermapping_modifiedby](systemuser.md#BKMK_lk_transformationparametermapping_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_transformationparametermapping_modifiedonbehalfby"></a> lk_transformationparametermapping_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_transformationparametermapping_modifiedonbehalfby](systemuser.md#BKMK_lk_transformationparametermapping_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransformationParameterMapping_TransformationMapping"></a> TransformationParameterMapping_TransformationMapping

One-To-Many Relationship: [transformationmapping TransformationParameterMapping_TransformationMapping](transformationmapping.md#BKMK_TransformationParameterMapping_TransformationMapping)

|Property|Value|
|---|---|
|ReferencedEntity|`transformationmapping`|
|ReferencedAttribute|`transformationmappingid`|
|ReferencingAttribute|`transformationmappingid`|
|ReferencingEntityNavigationPropertyName|`transformationmappingid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_LookUpMapping_TransformationParameterMapping"></a> LookUpMapping_TransformationParameterMapping

Many-To-One Relationship: [lookupmapping LookUpMapping_TransformationParameterMapping](lookupmapping.md#BKMK_LookUpMapping_TransformationParameterMapping)

|Property|Value|
|---|---|
|ReferencingEntity|`lookupmapping`|
|ReferencingAttribute|`transformationparametermappingid`|
|ReferencedEntityNavigationPropertyName|`LookUpMapping_TransformationParameterMapping`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.transformationparametermapping?displayProperty=fullName>
