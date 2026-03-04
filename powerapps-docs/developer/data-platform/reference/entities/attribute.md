---
title: "Attribute table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Attribute table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Attribute table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Attribute table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `RetrieveMultiple`<br />Event: False |`GET` /attributes<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Attribute table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Attribute** |
| **DisplayCollectionName** | **Attributes** |
| **SchemaName** | `Attribute` |
| **CollectionSchemaName** | `Attributes` |
| **EntitySetName** | `attributes`|
| **LogicalName** | `attribute` |
| **LogicalCollectionName** | `attributes` |
| **PrimaryIdAttribute** | `attributeid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

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
|---|---|
|Description|**Unique identifier of the attribute.**|
|DisplayName|**Attribute**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`attributeid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ExternalName"></a> ExternalName

|Property|Value|
|---|---|
|Description|**The external name of this attribute.**|
|DisplayName|**External Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`externalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_LogicalName"></a> LogicalName

|Property|Value|
|---|---|
|Description|**The logical name of this attribute.**|
|DisplayName|**Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`logicalname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_ManagedPropertyLogicalName"></a> ManagedPropertyLogicalName

|Property|Value|
|---|---|
|Description|**The managed property logical name of this attribute.**|
|DisplayName|**Managed Property Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`managedpropertylogicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_ManagedPropertyParentAttributeName"></a> ManagedPropertyParentAttributeName

|Property|Value|
|---|---|
|Description|**The managed property parent attribute name of this attribute.**|
|DisplayName|**Managed Property Parent Attribute Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`managedpropertyparentattributename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**The name of this Attribute.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_PhysicalName"></a> PhysicalName

|Property|Value|
|---|---|
|Description|**The physical name of this attribute.**|
|DisplayName|**Physical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`physicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_TableColumnName"></a> TableColumnName

|Property|Value|
|---|---|
|Description|**The table column name of this attribute.**|
|DisplayName|**Table Column Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`tablecolumnname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [AttributeOf](#BKMK_AttributeOf)
- [AttributeTypeId](#BKMK_AttributeTypeId)
- [ComponentState](#BKMK_ComponentState)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [ValidForReadAPI](#BKMK_ValidForReadAPI)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_AttributeOf"></a> AttributeOf

|Property|Value|
|---|---|
|Description|**Attribute Of**|
|DisplayName|**Attribute Of**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`attributeof`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_AttributeTypeId"></a> AttributeTypeId

|Property|Value|
|---|---|
|Description|**Attribute Type Id**|
|DisplayName|**Attribute Type Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`attributetypeid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

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

### <a name="BKMK_ValidForReadAPI"></a> ValidForReadAPI

|Property|Value|
|---|---|
|Description|**Valid For Read API**|
|DisplayName|**Valid For Read API**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`validforreadapi`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`_attribute_validforreadapi`|
|DefaultValue|False|
|True Label||
|False Label||

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**The version number of this attribute.**|
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

- [attribute_dvfilesearchattribute](#BKMK_attribute_dvfilesearchattribute)
- [attribute_dvtablesearchattribute](#BKMK_attribute_dvtablesearchattribute)
- [attribute_sensitivitylabelattributemapping_AttributeId](#BKMK_attribute_sensitivitylabelattributemapping_AttributeId)
- [attribute_solutioncomponentattrconfig](#BKMK_attribute_solutioncomponentattrconfig)
- [attributeclusterconfig_extensionofrecordid_attribute](#BKMK_attributeclusterconfig_extensionofrecordid_attribute)
- [emailaddressconfiguration_attribute_AttributeId](#BKMK_emailaddressconfiguration_attribute_AttributeId)
- [referencedattribute_relationshipattribute](#BKMK_referencedattribute_relationshipattribute)
- [referencingattribute_relationshipattribute](#BKMK_referencingattribute_relationshipattribute)

### <a name="BKMK_attribute_dvfilesearchattribute"></a> attribute_dvfilesearchattribute

Many-To-One Relationship: [dvfilesearchattribute attribute_dvfilesearchattribute](dvfilesearchattribute.md#BKMK_attribute_dvfilesearchattribute)

|Property|Value|
|---|---|
|ReferencingEntity|`dvfilesearchattribute`|
|ReferencingAttribute|`attribute`|
|ReferencedEntityNavigationPropertyName|`attribute_dvfilesearchattribute`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_attribute_dvtablesearchattribute"></a> attribute_dvtablesearchattribute

Many-To-One Relationship: [dvtablesearchattribute attribute_dvtablesearchattribute](dvtablesearchattribute.md#BKMK_attribute_dvtablesearchattribute)

|Property|Value|
|---|---|
|ReferencingEntity|`dvtablesearchattribute`|
|ReferencingAttribute|`attribute`|
|ReferencedEntityNavigationPropertyName|`attribute_dvtablesearchattribute`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_attribute_sensitivitylabelattributemapping_AttributeId"></a> attribute_sensitivitylabelattributemapping_AttributeId

Many-To-One Relationship: [sensitivitylabelattributemapping attribute_sensitivitylabelattributemapping_AttributeId](sensitivitylabelattributemapping.md#BKMK_attribute_sensitivitylabelattributemapping_AttributeId)

|Property|Value|
|---|---|
|ReferencingEntity|`sensitivitylabelattributemapping`|
|ReferencingAttribute|`attributeid`|
|ReferencedEntityNavigationPropertyName|`attribute_sensitivitylabelattributemapping_AttributeId`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_attribute_solutioncomponentattrconfig"></a> attribute_solutioncomponentattrconfig

Many-To-One Relationship: [solutioncomponentattributeconfiguration attribute_solutioncomponentattrconfig](solutioncomponentattributeconfiguration.md#BKMK_attribute_solutioncomponentattrconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`solutioncomponentattributeconfiguration`|
|ReferencingAttribute|`attributeid`|
|ReferencedEntityNavigationPropertyName|`attribute_solutioncomponentattrconfig`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_attributeclusterconfig_extensionofrecordid_attribute"></a> attributeclusterconfig_extensionofrecordid_attribute

Many-To-One Relationship: [attributeclusterconfig attributeclusterconfig_extensionofrecordid_attribute](attributeclusterconfig.md#BKMK_attributeclusterconfig_extensionofrecordid_attribute)

|Property|Value|
|---|---|
|ReferencingEntity|`attributeclusterconfig`|
|ReferencingAttribute|`extensionofrecordid`|
|ReferencedEntityNavigationPropertyName|`attributeclusterconfig_extensionofrecordid_attribute`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_emailaddressconfiguration_attribute_AttributeId"></a> emailaddressconfiguration_attribute_AttributeId

Many-To-One Relationship: [emailaddressconfiguration emailaddressconfiguration_attribute_AttributeId](emailaddressconfiguration.md#BKMK_emailaddressconfiguration_attribute_AttributeId)

|Property|Value|
|---|---|
|ReferencingEntity|`emailaddressconfiguration`|
|ReferencingAttribute|`attributeid`|
|ReferencedEntityNavigationPropertyName|`emailaddressconfiguration_attribute_AttributeId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_referencedattribute_relationshipattribute"></a> referencedattribute_relationshipattribute

Many-To-One Relationship: [relationshipattribute referencedattribute_relationshipattribute](relationshipattribute.md#BKMK_referencedattribute_relationshipattribute)

|Property|Value|
|---|---|
|ReferencingEntity|`relationshipattribute`|
|ReferencingAttribute|`referencedattributeid`|
|ReferencedEntityNavigationPropertyName|`referencedattribute_relationshipattribute`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_referencingattribute_relationshipattribute"></a> referencingattribute_relationshipattribute

Many-To-One Relationship: [relationshipattribute referencingattribute_relationshipattribute](relationshipattribute.md#BKMK_referencingattribute_relationshipattribute)

|Property|Value|
|---|---|
|ReferencingEntity|`relationshipattribute`|
|ReferencingAttribute|`referencingattributeid`|
|ReferencedEntityNavigationPropertyName|`referencingdattribute_relationshipattribute`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.attribute?displayProperty=fullName>
