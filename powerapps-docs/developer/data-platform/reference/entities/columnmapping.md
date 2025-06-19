---
title: "Column Mapping (ColumnMapping) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Column Mapping (ColumnMapping) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Column Mapping (ColumnMapping) table/entity reference (Microsoft Dataverse)

Mapping for columns in a data map.

## Messages

The following table lists the messages for the Column Mapping (ColumnMapping) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /columnmappings<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /columnmappings(*columnmappingid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /columnmappings(*columnmappingid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /columnmappings<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Column Mapping (ColumnMapping) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Column Mapping** |
| **DisplayCollectionName** | **Column Mappings** |
| **SchemaName** | `ColumnMapping` |
| **CollectionSchemaName** | `ColumnMappings` |
| **EntitySetName** | `columnmappings`|
| **LogicalName** | `columnmapping` |
| **LogicalCollectionName** | `columnmappings` |
| **PrimaryIdAttribute** | `columnmappingid` |
| **PrimaryNameAttribute** |`sourceattributename` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ColumnMappingId](#BKMK_ColumnMappingId)
- [ImportMapId](#BKMK_ImportMapId)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [ProcessCode](#BKMK_ProcessCode)
- [SourceAttributeName](#BKMK_SourceAttributeName)
- [SourceEntityName](#BKMK_SourceEntityName)
- [StatusCode](#BKMK_StatusCode)
- [TargetAttributeName](#BKMK_TargetAttributeName)
- [TargetEntityName](#BKMK_TargetEntityName)

### <a name="BKMK_ColumnMappingId"></a> ColumnMappingId

|Property|Value|
|---|---|
|Description|**Unique identifier of the column mapping.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`columnmappingid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ImportMapId"></a> ImportMapId

|Property|Value|
|---|---|
|Description|**Unique identifier of the associated data map.**|
|DisplayName|**Data Map ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`importmapid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|importmap|

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

### <a name="BKMK_ProcessCode"></a> ProcessCode

|Property|Value|
|---|---|
|Description|**Information about whether the column mapping needs to be processed.**|
|DisplayName|**Process Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`processcode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`columnmapping_processcode`|

#### ProcessCode Choices/Options

|Value|Label|
|---|---|
|1|**Process**|
|2|**Ignore**|
|3|**Internal**|

### <a name="BKMK_SourceAttributeName"></a> SourceAttributeName

|Property|Value|
|---|---|
|Description|**Name of the source attribute.**|
|DisplayName|**Source Attribute**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sourceattributename`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_SourceEntityName"></a> SourceEntityName

|Property|Value|
|---|---|
|Description|**Name of the source entity.**|
|DisplayName|**Source Entity Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sourceentityname`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Reason for the status of the column mapping.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|SystemRequired|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`columnmapping_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|

### <a name="BKMK_TargetAttributeName"></a> TargetAttributeName

|Property|Value|
|---|---|
|Description|**Name of the Microsoft Dynamics 365 attribute.**|
|DisplayName|**Target Attribute**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`targetattributename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_TargetEntityName"></a> TargetEntityName

|Property|Value|
|---|---|
|Description|**Name of the Microsoft Dynamics 365 entity.**|
|DisplayName|**Target Entity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`targetentityname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ColumnMappingIdUnique](#BKMK_ColumnMappingIdUnique)
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
- [StateCode](#BKMK_StateCode)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)

### <a name="BKMK_ColumnMappingIdUnique"></a> ColumnMappingIdUnique

|Property|Value|
|---|---|
|Description|**Unique identifier of the Column Mapping.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`columnmappingidunique`|
|RequiredLevel|SystemRequired|
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

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the column mapping.**|
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
|Description|**Date and time when the column mapping was created.**|
|DisplayName||
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
|Description|**Unique identifier of the delegate user who created the columnmapping.**|
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
|Description|**Unique identifier of the user who last modified the column mapping.**|
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
|Description|**Date and time when the column mapping was last modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the columnmapping.**|
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

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Status of the column mapping.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`columnmapping_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|

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

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [ColumnMapping_ImportMap](#BKMK_ColumnMapping_ImportMap)
- [lk_columnmapping_createdby](#BKMK_lk_columnmapping_createdby)
- [lk_columnmapping_createdonbehalfby](#BKMK_lk_columnmapping_createdonbehalfby)
- [lk_columnmapping_modifiedby](#BKMK_lk_columnmapping_modifiedby)
- [lk_columnmapping_modifiedonbehalfby](#BKMK_lk_columnmapping_modifiedonbehalfby)

### <a name="BKMK_ColumnMapping_ImportMap"></a> ColumnMapping_ImportMap

One-To-Many Relationship: [importmap ColumnMapping_ImportMap](importmap.md#BKMK_ColumnMapping_ImportMap)

|Property|Value|
|---|---|
|ReferencedEntity|`importmap`|
|ReferencedAttribute|`importmapid`|
|ReferencingAttribute|`importmapid`|
|ReferencingEntityNavigationPropertyName|`importmapid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_columnmapping_createdby"></a> lk_columnmapping_createdby

One-To-Many Relationship: [systemuser lk_columnmapping_createdby](systemuser.md#BKMK_lk_columnmapping_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_columnmapping_createdonbehalfby"></a> lk_columnmapping_createdonbehalfby

One-To-Many Relationship: [systemuser lk_columnmapping_createdonbehalfby](systemuser.md#BKMK_lk_columnmapping_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_columnmapping_modifiedby"></a> lk_columnmapping_modifiedby

One-To-Many Relationship: [systemuser lk_columnmapping_modifiedby](systemuser.md#BKMK_lk_columnmapping_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_columnmapping_modifiedonbehalfby"></a> lk_columnmapping_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_columnmapping_modifiedonbehalfby](systemuser.md#BKMK_lk_columnmapping_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [LookUpMapping_ColumnMapping](#BKMK_LookUpMapping_ColumnMapping)
- [PickListMapping_ColumnMapping](#BKMK_PickListMapping_ColumnMapping)

### <a name="BKMK_LookUpMapping_ColumnMapping"></a> LookUpMapping_ColumnMapping

Many-To-One Relationship: [lookupmapping LookUpMapping_ColumnMapping](lookupmapping.md#BKMK_LookUpMapping_ColumnMapping)

|Property|Value|
|---|---|
|ReferencingEntity|`lookupmapping`|
|ReferencingAttribute|`columnmappingid`|
|ReferencedEntityNavigationPropertyName|`LookUpMapping_ColumnMapping`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_PickListMapping_ColumnMapping"></a> PickListMapping_ColumnMapping

Many-To-One Relationship: [picklistmapping PickListMapping_ColumnMapping](picklistmapping.md#BKMK_PickListMapping_ColumnMapping)

|Property|Value|
|---|---|
|ReferencingEntity|`picklistmapping`|
|ReferencingAttribute|`columnmappingid`|
|ReferencedEntityNavigationPropertyName|`PickListMapping_ColumnMapping`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.columnmapping?displayProperty=fullName>
