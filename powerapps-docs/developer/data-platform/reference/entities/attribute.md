---
title: "Attribute table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Attribute table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Attribute table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).




## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|RetrieveMultiple|GET /attributes<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|Attributes|
|DisplayCollectionName|Attributes|
|DisplayName|Attribute|
|EntitySetName|attributes|
|IsBPFEntity|False|
|LogicalCollectionName|attributes|
|LogicalName|attribute|
|OwnershipType|None|
|PrimaryIdAttribute|attributeid|
|PrimaryNameAttribute|name|
|SchemaName|Attribute|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AttributeId](#BKMK_AttributeId)
- [ExternalName](#BKMK_ExternalName)
- [LogicalName](#BKMK_LogicalName)
- [ManagedPropertyLogicalName](#BKMK_ManagedPropertyLogicalName)
- [ManagedPropertyParentAttributeName](#BKMK_ManagedPropertyParentAttributeName)
- [Name](#BKMK_Name)
- [PhysicalName](#BKMK_PhysicalName)
- [TableColumnName](#BKMK_TableColumnName)


### <a name="BKMK_AttributeId"></a> AttributeId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the attribute.|
|DisplayName|Attribute|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|attributeid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ExternalName"></a> ExternalName

|Property|Value|
|--------|-----|
|Description|The external name of this attribute.|
|DisplayName|External Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|externalname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_LogicalName"></a> LogicalName

|Property|Value|
|--------|-----|
|Description|The logical name of this attribute.|
|DisplayName|Logical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|logicalname|
|MaxLength|128|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ManagedPropertyLogicalName"></a> ManagedPropertyLogicalName

|Property|Value|
|--------|-----|
|Description|The managed property logical name of this attribute.|
|DisplayName|Managed Property Logical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|managedpropertylogicalname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ManagedPropertyParentAttributeName"></a> ManagedPropertyParentAttributeName

|Property|Value|
|--------|-----|
|Description|The managed property parent attribute name of this attribute.|
|DisplayName|Managed Property Parent Attribute Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|managedpropertyparentattributename|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|The name of this Attribute.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PhysicalName"></a> PhysicalName

|Property|Value|
|--------|-----|
|Description|The physical name of this attribute.|
|DisplayName|Physical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|physicalname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TableColumnName"></a> TableColumnName

|Property|Value|
|--------|-----|
|Description|The table column name of this attribute.|
|DisplayName|Table Column Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|tablecolumnname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AttributeOf](#BKMK_AttributeOf)
- [AttributeTypeId](#BKMK_AttributeTypeId)
- [ComponentState](#BKMK_ComponentState)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [ValidForReadAPI](#BKMK_ValidForReadAPI)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_AttributeOf"></a> AttributeOf

**Added by**: Metadata Extension Solution

|Property|Value|
|--------|-----|
|Description|Attribute Of|
|DisplayName|Attribute Of|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|attributeof|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_AttributeTypeId"></a> AttributeTypeId

**Added by**: Metadata Extension Solution

|Property|Value|
|--------|-----|
|Description|Attribute Type Id|
|DisplayName|Attribute Type Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|attributetypeid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


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


### <a name="BKMK_ValidForReadAPI"></a> ValidForReadAPI

**Added by**: Metadata Extension Solution

|Property|Value|
|--------|-----|
|Description|Valid For Read API|
|DisplayName|Valid For Read API|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|validforreadapi|
|RequiredLevel|None|
|Type|Boolean|

#### ValidForReadAPI Choices/Options

|Value|Label|Description|
|-----|-----|--------|


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Added by**: Metadata Extension Solution

|Property|Value|
|--------|-----|
|Description|The version number of this attribute.|
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

- [attribute_solutioncomponentattrconfig](#BKMK_attribute_solutioncomponentattrconfig)
- [referencingattribute_relationshipattribute](#BKMK_referencingattribute_relationshipattribute)
- [referencedattribute_relationshipattribute](#BKMK_referencedattribute_relationshipattribute)


### <a name="BKMK_attribute_solutioncomponentattrconfig"></a> attribute_solutioncomponentattrconfig

**Added by**: Solution Component Configuration Solution

Same as the [attribute_solutioncomponentattrconfig](solutioncomponentattributeconfiguration.md#BKMK_attribute_solutioncomponentattrconfig) many-to-one relationship for the [solutioncomponentattributeconfiguration](solutioncomponentattributeconfiguration.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentattributeconfiguration|
|ReferencingAttribute|attributeid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|attribute_solutioncomponentattrconfig|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_referencingattribute_relationshipattribute"></a> referencingattribute_relationshipattribute

**Added by**: Metadata Extension Solution

Same as the [referencingattribute_relationshipattribute](relationshipattribute.md#BKMK_referencingattribute_relationshipattribute) many-to-one relationship for the [relationshipattribute](relationshipattribute.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|relationshipattribute|
|ReferencingAttribute|referencingattributeid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|referencingdattribute_relationshipattribute|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_referencedattribute_relationshipattribute"></a> referencedattribute_relationshipattribute

**Added by**: Metadata Extension Solution

Same as the [referencedattribute_relationshipattribute](relationshipattribute.md#BKMK_referencedattribute_relationshipattribute) many-to-one relationship for the [relationshipattribute](relationshipattribute.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|relationshipattribute|
|ReferencingAttribute|referencedattributeid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|referencedattribute_relationshipattribute|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.attribute?text=attribute EntityType" />