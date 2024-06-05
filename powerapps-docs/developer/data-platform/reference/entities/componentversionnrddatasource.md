---
title: "Component Version (Internal) (componentversionnrddatasource)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Component Version (Internal) (componentversionnrddatasource)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Component Version (Internal) (componentversionnrddatasource)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Component Versioning Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST /componentversionnrddatasourceset<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /componentversionnrddatasourceset(*componentversionnrddatasourceid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET /componentversionnrddatasourceset(*componentversionnrddatasourceid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /componentversionnrddatasourceset<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH /componentversionnrddatasourceset(*componentversionnrddatasourceid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|Upsert||<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
|UpsertMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|componentversionnrddatasources|
|DisplayCollectionName|Component Versions (Internal)|
|DisplayName|Component Version (Internal)|
|EntitySetName|componentversionnrddatasourceset|
|IsBPFEntity|False|
|LogicalCollectionName|componentversionnrddatasourceset|
|LogicalName|componentversionnrddatasource|
|OwnershipType|None|
|PrimaryIdAttribute|componentversionnrddatasourceid|
|PrimaryNameAttribute|componentversionname|
|SchemaName|componentversionnrddatasource|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ChangeSummary](#BKMK_ChangeSummary)
- [Component](#BKMK_Component)
- [ComponentIdType](#BKMK_ComponentIdType)
- [componentversionname](#BKMK_componentversionname)
- [componentversionnrddatasourceId](#BKMK_componentversionnrddatasourceId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [Operation](#BKMK_Operation)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PartitionId](#BKMK_PartitionId)
- [RestoredFromVersion](#BKMK_RestoredFromVersion)
- [restoredfromversionPId](#BKMK_restoredfromversionPId)
- [SystemChangeSummary](#BKMK_SystemChangeSummary)
- [TTLInSeconds](#BKMK_TTLInSeconds)


### <a name="BKMK_ChangeSummary"></a> ChangeSummary

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Change Summary|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|changesummary|
|MaxLength|2048|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Component"></a> Component

|Property|Value|
|--------|-----|
|Description|Owning component.|
|DisplayName|Component|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|component|
|RequiredLevel|ApplicationRequired|
|Targets|workflow|
|Type|Lookup|


### <a name="BKMK_ComponentIdType"></a> ComponentIdType

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentidtype|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_componentversionname"></a> componentversionname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Version Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|componentversionname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_componentversionnrddatasourceId"></a> componentversionnrddatasourceId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Component Version (Internal)|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|componentversionnrddatasourceid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|Sequence number of the import that created this record.|
|DisplayName|Import Sequence Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|importsequencenumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_Operation"></a> Operation

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Operation|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|operation|
|RequiredLevel|None|
|Type|Picklist|

#### Operation Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Create||
|1|Update||
|2|Publish||
|3|Restore||
|4|Solution Import||



### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time that the record was migrated.|
|DisplayName|Record Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_PartitionId"></a> PartitionId

|Property|Value|
|--------|-----|
|Description|Logical partition id. A logical partition consists of a set of records with same partition id.|
|DisplayName|Partition Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|partitionid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RestoredFromVersion"></a> RestoredFromVersion

|Property|Value|
|--------|-----|
|Description|Base version that was restored.|
|DisplayName|Restored From Version|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|restoredfromversion|
|RequiredLevel|None|
|Targets|componentversionnrddatasource|
|Type|Lookup|


### <a name="BKMK_restoredfromversionPId"></a> restoredfromversionPId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|restoredfromversionpid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SystemChangeSummary"></a> SystemChangeSummary

|Property|Value|
|--------|-----|
|Description||
|DisplayName|System Change Summary|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|systemchangesummary|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TTLInSeconds"></a> TTLInSeconds

|Property|Value|
|--------|-----|
|Description|Time to live in seconds.|
|DisplayName|Time to live|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ttlinseconds|
|MaxValue|2147483647|
|MinValue|1|
|RequiredLevel|None|
|Type|Integer|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentName](#BKMK_ComponentName)
- [ComponentYomiName](#BKMK_ComponentYomiName)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [Payload](#BKMK_Payload)
- [Payload_Name](#BKMK_Payload_Name)
- [restoredfromversionName](#BKMK_restoredfromversionName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ComponentName"></a> ComponentName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentname|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ComponentYomiName"></a> ComponentYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentyominame|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the record.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the record.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who modified the record.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the record.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwnerId"></a> OwnerId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Owner Id|
|DisplayName|Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Targets|systemuser,team|
|Type|Owner|


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the business unit that owns the record|
|DisplayName|Owning Business Unit|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the team that owns the record.|
|DisplayName|Owning Team|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteam|
|RequiredLevel|None|
|Targets||
|Type|Lookup|


### <a name="BKMK_OwningUser"></a> OwningUser

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the user that owns the record.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets||
|Type|Lookup|


### <a name="BKMK_Payload"></a> Payload

|Property|Value|
|--------|-----|
|Description|Payload|
|DisplayName|Payload|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|payload|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_Payload_Name"></a> Payload_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|payload_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_restoredfromversionName"></a> restoredfromversionName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|restoredfromversionname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Version Number|
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

- [componentversionnrddatasource_ElasticFileAttachments](#BKMK_componentversionnrddatasource_ElasticFileAttachments)
- [nrd_restoreversions](#BKMK_nrd_restoreversions)


### <a name="BKMK_componentversionnrddatasource_ElasticFileAttachments"></a> componentversionnrddatasource_ElasticFileAttachments

**Added by**: NonRelational Data Provider Custom Actions Solution

Same as the [componentversionnrddatasource_ElasticFileAttachments](elasticfileattachment.md#BKMK_componentversionnrddatasource_ElasticFileAttachments) many-to-one relationship for the [elasticfileattachment](elasticfileattachment.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|elasticfileattachment|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|componentversionnrddatasource_ElasticFileAttachments|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_nrd_restoreversions"></a> nrd_restoreversions

Same as the [nrd_restoreversions](componentversionnrddatasource.md#BKMK_nrd_restoreversions) many-to-one relationship for the [componentversionnrddatasource](componentversionnrddatasource.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|componentversionnrddatasource|
|ReferencingAttribute|restoredfromversion|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|restoredtoversions|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_componentversionnrddatasource_createdby](#BKMK_lk_componentversionnrddatasource_createdby)
- [lk_componentversionnrddatasource_createdonbehalfby](#BKMK_lk_componentversionnrddatasource_createdonbehalfby)
- [lk_componentversionnrddatasource_modifiedby](#BKMK_lk_componentversionnrddatasource_modifiedby)
- [lk_componentversionnrddatasource_modifiedonbehalfby](#BKMK_lk_componentversionnrddatasource_modifiedonbehalfby)
- [ElasticFileAttachment_componentversionnrddatasource_Payload](#BKMK_ElasticFileAttachment_componentversionnrddatasource_Payload)
- [nrd_restoreversions](#BKMK_nrd_restoreversions)
- [workflow_componentversionnrddatasourceset](#BKMK_workflow_componentversionnrddatasourceset)


### <a name="BKMK_lk_componentversionnrddatasource_createdby"></a> lk_componentversionnrddatasource_createdby

**Added by**: System Solution Solution

See the [lk_componentversionnrddatasource_createdby](systemuser.md#BKMK_lk_componentversionnrddatasource_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_componentversionnrddatasource_createdonbehalfby"></a> lk_componentversionnrddatasource_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_componentversionnrddatasource_createdonbehalfby](systemuser.md#BKMK_lk_componentversionnrddatasource_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_componentversionnrddatasource_modifiedby"></a> lk_componentversionnrddatasource_modifiedby

**Added by**: System Solution Solution

See the [lk_componentversionnrddatasource_modifiedby](systemuser.md#BKMK_lk_componentversionnrddatasource_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_componentversionnrddatasource_modifiedonbehalfby"></a> lk_componentversionnrddatasource_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_componentversionnrddatasource_modifiedonbehalfby](systemuser.md#BKMK_lk_componentversionnrddatasource_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_ElasticFileAttachment_componentversionnrddatasource_Payload"></a> ElasticFileAttachment_componentversionnrddatasource_Payload

**Added by**: NonRelational Data Provider Custom Actions Solution

See the [ElasticFileAttachment_componentversionnrddatasource_Payload](elasticfileattachment.md#BKMK_ElasticFileAttachment_componentversionnrddatasource_Payload) one-to-many relationship for the [elasticfileattachment](elasticfileattachment.md) table/entity.

### <a name="BKMK_nrd_restoreversions"></a> nrd_restoreversions

See the [nrd_restoreversions](componentversionnrddatasource.md#BKMK_nrd_restoreversions) one-to-many relationship for the [componentversionnrddatasource](componentversionnrddatasource.md) table/entity.

### <a name="BKMK_workflow_componentversionnrddatasourceset"></a> workflow_componentversionnrddatasourceset

**Added by**: System Solution Solution

See the [workflow_componentversionnrddatasourceset](workflow.md#BKMK_workflow_componentversionnrddatasourceset) one-to-many relationship for the [workflow](workflow.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.componentversionnrddatasource?text=componentversionnrddatasource EntityType" />