---
title: "Component Version (Internal) (componentversionnrddatasource) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Component Version (Internal) (componentversionnrddatasource) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Component Version (Internal) (componentversionnrddatasource) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Component Version (Internal) (componentversionnrddatasource) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /componentversionnrddatasourceset<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: False |`DELETE` /componentversionnrddatasourceset(*componentversionnrddatasourceid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `DeleteMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.DeleteMultiple?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /componentversionnrddatasourceset(*componentversionnrddatasourceid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: False | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: False |`GET` /componentversionnrddatasourceset<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /componentversionnrddatasourceset(*componentversionnrddatasourceid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /componentversionnrddatasourceset(*componentversionnrddatasourceid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Component Version (Internal) (componentversionnrddatasource) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Component Version (Internal)** |
| **DisplayCollectionName** | **Component Versions (Internal)** |
| **SchemaName** | `componentversionnrddatasource` |
| **CollectionSchemaName** | `componentversionnrddatasources` |
| **EntitySetName** | `componentversionnrddatasourceset`|
| **LogicalName** | `componentversionnrddatasource` |
| **LogicalCollectionName** | `componentversionnrddatasourceset` |
| **PrimaryIdAttribute** | `componentversionnrddatasourceid` |
| **PrimaryNameAttribute** |`componentversionname` |
| **TableType** | `Elastic` |
| **OwnershipType** | `None` |

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
|---|---|
|Description||
|DisplayName|**Change Summary**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`changesummary`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2048|

### <a name="BKMK_Component"></a> Component

|Property|Value|
|---|---|
|Description|**Owning component.**|
|DisplayName|**Component**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`component`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|workflow|

### <a name="BKMK_ComponentIdType"></a> ComponentIdType

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentidtype`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_componentversionname"></a> componentversionname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Version Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`componentversionname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_componentversionnrddatasourceId"></a> componentversionnrddatasourceId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Component Version (Internal)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentversionnrddatasourceid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Sequence number of the import that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_Operation"></a> Operation

|Property|Value|
|---|---|
|Description||
|DisplayName|**Operation**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`operation`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`componentversionnrddatasource_operation`|

#### Operation Choices/Options

|Value|Label|
|---|---|
|0|**Create**|
|1|**Update**|
|2|**Publish**|
|3|**Restore**|
|4|**Solution Import**|

### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|---|---|
|Description|**Date and time that the record was migrated.**|
|DisplayName|**Record Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overriddencreatedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_PartitionId"></a> PartitionId

|Property|Value|
|---|---|
|Description|**Logical partition id. A logical partition consists of a set of records with same partition id.**|
|DisplayName|**Partition Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`partitionid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_RestoredFromVersion"></a> RestoredFromVersion

|Property|Value|
|---|---|
|Description|**Base version that was restored.**|
|DisplayName|**Restored From Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`restoredfromversion`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|componentversionnrddatasource|

### <a name="BKMK_restoredfromversionPId"></a> restoredfromversionPId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`restoredfromversionpid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_SystemChangeSummary"></a> SystemChangeSummary

|Property|Value|
|---|---|
|Description||
|DisplayName|**System Change Summary**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`systemchangesummary`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_TTLInSeconds"></a> TTLInSeconds

|Property|Value|
|---|---|
|Description|**Time to live in seconds.**|
|DisplayName|**Time to live**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ttlinseconds`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|1|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [Payload](#BKMK_Payload)
- [Payload_Name](#BKMK_Payload_Name)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was created.**|
|DisplayName|**Created On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who created the record.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who modified the record.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who modified the record.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Owner Id**|
|DisplayName|**Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Unique identifier for the business unit that owns the record**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|---|---|
|Description|**Unique identifier for the team that owns the record.**|
|DisplayName|**Owning Team**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningteam`|
|RequiredLevel|None|
|Type|Lookup|
|Targets||

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier for the user that owns the record.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets||

### <a name="BKMK_Payload"></a> Payload

|Property|Value|
|---|---|
|Description|**Payload**|
|DisplayName|**Payload**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`payload`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|30720|

### <a name="BKMK_Payload_Name"></a> Payload_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`payload_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version Number**|
|DisplayName|**Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [ElasticFileAttachment_componentversionnrddatasource_Payload](#BKMK_ElasticFileAttachment_componentversionnrddatasource_Payload)
- [lk_componentversionnrddatasource_createdby](#BKMK_lk_componentversionnrddatasource_createdby)
- [lk_componentversionnrddatasource_createdonbehalfby](#BKMK_lk_componentversionnrddatasource_createdonbehalfby)
- [lk_componentversionnrddatasource_modifiedby](#BKMK_lk_componentversionnrddatasource_modifiedby)
- [lk_componentversionnrddatasource_modifiedonbehalfby](#BKMK_lk_componentversionnrddatasource_modifiedonbehalfby)
- [nrd_restoreversions](#BKMK_nrd_restoreversions-many-to-one)
- [workflow_componentversionnrddatasourceset](#BKMK_workflow_componentversionnrddatasourceset)

### <a name="BKMK_ElasticFileAttachment_componentversionnrddatasource_Payload"></a> ElasticFileAttachment_componentversionnrddatasource_Payload

One-To-Many Relationship: [elasticfileattachment ElasticFileAttachment_componentversionnrddatasource_Payload](elasticfileattachment.md#BKMK_ElasticFileAttachment_componentversionnrddatasource_Payload)

|Property|Value|
|---|---|
|ReferencedEntity|`elasticfileattachment`|
|ReferencedAttribute|`elasticfileattachmentid`|
|ReferencingAttribute|`payload`|
|ReferencingEntityNavigationPropertyName|`payload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_componentversionnrddatasource_createdby"></a> lk_componentversionnrddatasource_createdby

One-To-Many Relationship: [systemuser lk_componentversionnrddatasource_createdby](systemuser.md#BKMK_lk_componentversionnrddatasource_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_componentversionnrddatasource_createdonbehalfby"></a> lk_componentversionnrddatasource_createdonbehalfby

One-To-Many Relationship: [systemuser lk_componentversionnrddatasource_createdonbehalfby](systemuser.md#BKMK_lk_componentversionnrddatasource_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_componentversionnrddatasource_modifiedby"></a> lk_componentversionnrddatasource_modifiedby

One-To-Many Relationship: [systemuser lk_componentversionnrddatasource_modifiedby](systemuser.md#BKMK_lk_componentversionnrddatasource_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_componentversionnrddatasource_modifiedonbehalfby"></a> lk_componentversionnrddatasource_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_componentversionnrddatasource_modifiedonbehalfby](systemuser.md#BKMK_lk_componentversionnrddatasource_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_nrd_restoreversions-many-to-one"></a> nrd_restoreversions

One-To-Many Relationship: [componentversionnrddatasource nrd_restoreversions](#BKMK_nrd_restoreversions-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`componentversionnrddatasource`|
|ReferencedAttribute|`componentversionnrddatasourceid`|
|ReferencingAttribute|`restoredfromversion`|
|ReferencingEntityNavigationPropertyName|`restoredfromversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflow_componentversionnrddatasourceset"></a> workflow_componentversionnrddatasourceset

One-To-Many Relationship: [workflow workflow_componentversionnrddatasourceset](workflow.md#BKMK_workflow_componentversionnrddatasourceset)

|Property|Value|
|---|---|
|ReferencedEntity|`workflow`|
|ReferencedAttribute|`workflowid`|
|ReferencingAttribute|`component`|
|ReferencingEntityNavigationPropertyName|`component_workflow`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [componentversionnrddatasource_ElasticFileAttachments](#BKMK_componentversionnrddatasource_ElasticFileAttachments)
- [nrd_restoreversions](#BKMK_nrd_restoreversions-one-to-many)

### <a name="BKMK_componentversionnrddatasource_ElasticFileAttachments"></a> componentversionnrddatasource_ElasticFileAttachments

Many-To-One Relationship: [elasticfileattachment componentversionnrddatasource_ElasticFileAttachments](elasticfileattachment.md#BKMK_componentversionnrddatasource_ElasticFileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`elasticfileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`componentversionnrddatasource_ElasticFileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_nrd_restoreversions-one-to-many"></a> nrd_restoreversions

Many-To-One Relationship: [componentversionnrddatasource nrd_restoreversions](#BKMK_nrd_restoreversions-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`componentversionnrddatasource`|
|ReferencingAttribute|`restoredfromversion`|
|ReferencedEntityNavigationPropertyName|`restoredtoversions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.componentversionnrddatasource?displayProperty=fullName>
