---
title: "Entity table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Entity table/entity."
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

# Entity table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).




## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/entities<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|Entities|
|DisplayCollectionName|Entities|
|DisplayName|Entity|
|EntitySetName|entities|
|IsBPFEntity|False|
|LogicalCollectionName|entities|
|LogicalName|entity|
|OwnershipType|None|
|PrimaryIdAttribute|entityid|
|PrimaryNameAttribute|name|
|SchemaName|Entity|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AddressTableName](#BKMK_AddressTableName)
- [BaseTableName](#BKMK_BaseTableName)
- [CollectionName](#BKMK_CollectionName)
- [EntityId](#BKMK_EntityId)
- [EntitySetName](#BKMK_EntitySetName)
- [ExtensionTableName](#BKMK_ExtensionTableName)
- [ExternalCollectionName](#BKMK_ExternalCollectionName)
- [ExternalName](#BKMK_ExternalName)
- [LogicalCollectionName](#BKMK_LogicalCollectionName)
- [LogicalName](#BKMK_LogicalName)
- [Name](#BKMK_Name)
- [OriginalLocalizedCollectionName](#BKMK_OriginalLocalizedCollectionName)
- [OriginalLocalizedName](#BKMK_OriginalLocalizedName)
- [ParentControllingAttributeName](#BKMK_ParentControllingAttributeName)
- [PhysicalName](#BKMK_PhysicalName)
- [ReportViewName](#BKMK_ReportViewName)


### <a name="BKMK_AddressTableName"></a> AddressTableName

|Property|Value|
|--------|-----|
|Description|The address table name of this entity.|
|DisplayName|Address Table Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|addresstablename|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_BaseTableName"></a> BaseTableName

|Property|Value|
|--------|-----|
|Description|The base table name of this entity.|
|DisplayName|Base Table Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|basetablename|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CollectionName"></a> CollectionName

|Property|Value|
|--------|-----|
|Description|The collection name of this entity.|
|DisplayName|Collection Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|collectionname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EntityId"></a> EntityId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the entity.|
|DisplayName|Entity|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|entityid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_EntitySetName"></a> EntitySetName

|Property|Value|
|--------|-----|
|Description|The entity set name of this entity.|
|DisplayName|Entity Set Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|entitysetname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ExtensionTableName"></a> ExtensionTableName

|Property|Value|
|--------|-----|
|Description|The extension table name of this entity.|
|DisplayName|Extension Table Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|extensiontablename|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ExternalCollectionName"></a> ExternalCollectionName

|Property|Value|
|--------|-----|
|Description|The external collection name of this entity.|
|DisplayName|External Collection Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|externalcollectionname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ExternalName"></a> ExternalName

|Property|Value|
|--------|-----|
|Description|The external name of this entity.|
|DisplayName|External Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|externalname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_LogicalCollectionName"></a> LogicalCollectionName

|Property|Value|
|--------|-----|
|Description|The logical collection name of this entity.|
|DisplayName|Logical Collection Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|logicalcollectionname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_LogicalName"></a> LogicalName

|Property|Value|
|--------|-----|
|Description|The logical name of this entity.|
|DisplayName|Logical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|logicalname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|The name of this Entity.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OriginalLocalizedCollectionName"></a> OriginalLocalizedCollectionName

|Property|Value|
|--------|-----|
|Description|The original localized collection name of this entity.|
|DisplayName|Original Localized Collection Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|originallocalizedcollectionname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OriginalLocalizedName"></a> OriginalLocalizedName

|Property|Value|
|--------|-----|
|Description|The original localized name of this entity.|
|DisplayName|Original Localized Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|originallocalizedname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ParentControllingAttributeName"></a> ParentControllingAttributeName

|Property|Value|
|--------|-----|
|Description|The parent controlling attribute name of this entity.|
|DisplayName|Parent Controlling Attribute Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|parentcontrollingattributename|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PhysicalName"></a> PhysicalName

|Property|Value|
|--------|-----|
|Description|The physical name of this entity.|
|DisplayName|Physical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|physicalname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ReportViewName"></a> ReportViewName

|Property|Value|
|--------|-----|
|Description|The Report view name of this entity.|
|DisplayName|Report View Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|reportviewname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [VersionNumber](#BKMK_VersionNumber)


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
|Description|The version number of this entity.|
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

- [entity_solutioncomponentconfiguration](#BKMK_entity_solutioncomponentconfiguration)
- [entity_entityanalyticsconfig](#BKMK_entity_entityanalyticsconfig)
- [catalogassignment_entity](#BKMK_catalogassignment_entity)


### <a name="BKMK_entity_solutioncomponentconfiguration"></a> entity_solutioncomponentconfiguration

**Added by**: Solution Component Configuration Solution

Same as solutioncomponentconfiguration table [entity_solutioncomponentconfiguration](solutioncomponentconfiguration.md#BKMK_entity_solutioncomponentconfiguration) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentconfiguration|
|ReferencingAttribute|entityid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|entity_solutioncomponentconfiguration|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_entity_entityanalyticsconfig"></a> entity_entityanalyticsconfig

**Added by**: Advanced Analytics Infrastructure Solution

Same as entityanalyticsconfig table [entity_entityanalyticsconfig](entityanalyticsconfig.md#BKMK_entity_entityanalyticsconfig) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|entityanalyticsconfig|
|ReferencingAttribute|parententityid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|entity_entityanalyticsconfig|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_catalogassignment_entity"></a> catalogassignment_entity

**Added by**: CatalogFramework Solution

Same as catalogassignment table [catalogassignment_entity](catalogassignment.md#BKMK_catalogassignment_entity) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|catalogassignment|
|ReferencingAttribute|object|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|CatalogAssignments|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.entity?text=entity EntityType" />