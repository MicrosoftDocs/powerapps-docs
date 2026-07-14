---
title: "List Value Mapping (PickListMapping) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the List Value Mapping (PickListMapping) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# List Value Mapping (PickListMapping) table/entity reference (Microsoft Dataverse)

In a data map, maps list values from the source file to Microsoft Dynamics 365.

## Messages

The following table lists the messages for the List Value Mapping (PickListMapping) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /picklistmappings<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /picklistmappings(*picklistmappingid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /picklistmappings(*picklistmappingid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /picklistmappings<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the List Value Mapping (PickListMapping) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **List Value Mapping** |
| **DisplayCollectionName** | **List Value Mappings** |
| **SchemaName** | `PickListMapping` |
| **CollectionSchemaName** | `PickListMappings` |
| **EntitySetName** | `picklistmappings`|
| **LogicalName** | `picklistmapping` |
| **LogicalCollectionName** | `picklistmappings` |
| **PrimaryIdAttribute** | `picklistmappingid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ColumnMappingId](#BKMK_ColumnMappingId)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [PickListMappingId](#BKMK_PickListMappingId)
- [ProcessCode](#BKMK_ProcessCode)
- [SourceValue](#BKMK_SourceValue)
- [StatusCode](#BKMK_StatusCode)
- [TargetValue](#BKMK_TargetValue)

### <a name="BKMK_ColumnMappingId"></a> ColumnMappingId

|Property|Value|
|---|---|
|Description|**Unique identifier of the column mapping with which this list value mapping is associated.**|
|DisplayName|**Column Mapping Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`columnmappingid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|columnmapping|

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

### <a name="BKMK_PickListMappingId"></a> PickListMappingId

|Property|Value|
|---|---|
|Description|**Unique identifier of the picklist mapping.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`picklistmappingid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ProcessCode"></a> ProcessCode

|Property|Value|
|---|---|
|Description|**Information about whether the list value mapping needs to be processed.**|
|DisplayName|**Process Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`processcode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`picklistmapping_processcode`|

#### ProcessCode Choices/Options

|Value|Label|
|---|---|
|1|**Process**|
|2|**Ignore**|
|3|**Internal**|
|4|**Unmapped**|

### <a name="BKMK_SourceValue"></a> SourceValue

|Property|Value|
|---|---|
|Description|**Source value to be replaced.**|
|DisplayName|**Source Value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sourcevalue`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2097152|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Reason for the status of the picklist mapping.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|SystemRequired|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`picklistmapping_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />State:0<br />TransitionData: None|

### <a name="BKMK_TargetValue"></a> TargetValue

|Property|Value|
|---|---|
|Description|**Microsoft Dynamics 365 list value with which to replace the source value.**|
|DisplayName|**Target Value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`targetvalue`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|


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
- [PickListMappingIdUnique](#BKMK_PickListMappingIdUnique)
- [SolutionId](#BKMK_SolutionId)
- [StateCode](#BKMK_StateCode)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)

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
|Description|**Unique identifier of the user who created the list value mapping.**|
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
|Description|**Date and time when the list value mapping was created.**|
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
|Description|**Unique identifier of the delegate user who created the picklistmapping.**|
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
|Description|**Unique identifier of the user who last modified the list value mapping.**|
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
|Description|**Date and time when the list value mapping was last modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the picklistmapping.**|
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

### <a name="BKMK_PickListMappingIdUnique"></a> PickListMappingIdUnique

|Property|Value|
|---|---|
|Description|**Unique identifier of the Pick List Mapping.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`picklistmappingidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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
|Description|**Status of the picklist mapping.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`picklistmapping_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 0<br />InvariantName: `Active`|

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

- [lk_picklistmapping_createdby](#BKMK_lk_picklistmapping_createdby)
- [lk_picklistmapping_createdonbehalfby](#BKMK_lk_picklistmapping_createdonbehalfby)
- [lk_picklistmapping_modifiedby](#BKMK_lk_picklistmapping_modifiedby)
- [lk_picklistmapping_modifiedonbehalfby](#BKMK_lk_picklistmapping_modifiedonbehalfby)
- [PickListMapping_ColumnMapping](#BKMK_PickListMapping_ColumnMapping)

### <a name="BKMK_lk_picklistmapping_createdby"></a> lk_picklistmapping_createdby

One-To-Many Relationship: [systemuser lk_picklistmapping_createdby](systemuser.md#BKMK_lk_picklistmapping_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_picklistmapping_createdonbehalfby"></a> lk_picklistmapping_createdonbehalfby

One-To-Many Relationship: [systemuser lk_picklistmapping_createdonbehalfby](systemuser.md#BKMK_lk_picklistmapping_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_picklistmapping_modifiedby"></a> lk_picklistmapping_modifiedby

One-To-Many Relationship: [systemuser lk_picklistmapping_modifiedby](systemuser.md#BKMK_lk_picklistmapping_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_picklistmapping_modifiedonbehalfby"></a> lk_picklistmapping_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_picklistmapping_modifiedonbehalfby](systemuser.md#BKMK_lk_picklistmapping_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_PickListMapping_ColumnMapping"></a> PickListMapping_ColumnMapping

One-To-Many Relationship: [columnmapping PickListMapping_ColumnMapping](columnmapping.md#BKMK_PickListMapping_ColumnMapping)

|Property|Value|
|---|---|
|ReferencedEntity|`columnmapping`|
|ReferencedAttribute|`columnmappingid`|
|ReferencingAttribute|`columnmappingid`|
|ReferencingEntityNavigationPropertyName|`columnmappingid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.picklistmapping?displayProperty=fullName>
