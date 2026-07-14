---
title: "Shared Workspace Access Token (sharedworkspaceaccesstoken2) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Shared Workspace Access Token (sharedworkspaceaccesstoken2) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Shared Workspace Access Token (sharedworkspaceaccesstoken2) table/entity reference (Microsoft Dataverse)

Contains information about the shared workspace access tokens.

## Messages

The following table lists the messages for the Shared Workspace Access Token (sharedworkspaceaccesstoken2) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /sharedworkspaceaccesstoken2s<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /sharedworkspaceaccesstoken2s(*sharedworkspaceaccesstoken2id*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `DeleteMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.DeleteMultiple?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /sharedworkspaceaccesstoken2s(*sharedworkspaceaccesstoken2id*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /sharedworkspaceaccesstoken2s<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /sharedworkspaceaccesstoken2s(*sharedworkspaceaccesstoken2id*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: True |`PATCH` /sharedworkspaceaccesstoken2s(*sharedworkspaceaccesstoken2id*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Shared Workspace Access Token (sharedworkspaceaccesstoken2) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Shared Workspace Access Token** |
| **DisplayCollectionName** | **Shared Workspace Access Token2s** |
| **SchemaName** | `sharedworkspaceaccesstoken2` |
| **CollectionSchemaName** | `sharedworkspaceaccesstoken2s` |
| **EntitySetName** | `sharedworkspaceaccesstoken2s`|
| **LogicalName** | `sharedworkspaceaccesstoken2` |
| **LogicalCollectionName** | `sharedworkspaceaccesstoken2s` |
| **PrimaryIdAttribute** | `sharedworkspaceaccesstoken2id` |
| **PrimaryNameAttribute** |`systemuserid` |
| **TableType** | `Elastic` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [ObjectPartitionId](#BKMK_ObjectPartitionId)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PartitionId](#BKMK_PartitionId)
- [sharedworkspaceaccesstoken2Id](#BKMK_sharedworkspaceaccesstoken2Id)
- [SharedWorkspaceId](#BKMK_SharedWorkspaceId)
- [SystemUserId](#BKMK_SystemUserId)
- [TenantId](#BKMK_TenantId)
- [TokenId](#BKMK_TokenId)
- [TTLInSeconds](#BKMK_TTLInSeconds)

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

### <a name="BKMK_ObjectPartitionId"></a> ObjectPartitionId

|Property|Value|
|---|---|
|Description|**Logical object partition id to be used by an elastic table row.**|
|DisplayName|**Object Partition Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`objectpartitionid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

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

### <a name="BKMK_sharedworkspaceaccesstoken2Id"></a> sharedworkspaceaccesstoken2Id

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Shared Workspace Access Token**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sharedworkspaceaccesstoken2id`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SharedWorkspaceId"></a> SharedWorkspaceId

|Property|Value|
|---|---|
|Description|**Shared Workspace Id**|
|DisplayName|**SharedWorkspaceId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sharedworkspaceid`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_SystemUserId"></a> SystemUserId

|Property|Value|
|---|---|
|Description|**System User identifier**|
|DisplayName|**SystemUserId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`systemuserid`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_TenantId"></a> TenantId

|Property|Value|
|---|---|
|Description|**The tenant where the workspace resides**|
|DisplayName|**Tenant ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`tenantid`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_TokenId"></a> TokenId

|Property|Value|
|---|---|
|Description|**Access Token Id**|
|DisplayName|**TokenId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`tokenid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_TTLInSeconds"></a> TTLInSeconds

|Property|Value|
|---|---|
|Description|**After the specified number of seconds the access token will be deleted**|
|DisplayName|**Expiry (seconds)**|
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
|Description|**Date and time when entity was created.**|
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

- [lk_sharedworkspaceaccesstoken2_createdby](#BKMK_lk_sharedworkspaceaccesstoken2_createdby)
- [lk_sharedworkspaceaccesstoken2_createdonbehalfby](#BKMK_lk_sharedworkspaceaccesstoken2_createdonbehalfby)
- [lk_sharedworkspaceaccesstoken2_modifiedby](#BKMK_lk_sharedworkspaceaccesstoken2_modifiedby)
- [lk_sharedworkspaceaccesstoken2_modifiedonbehalfby](#BKMK_lk_sharedworkspaceaccesstoken2_modifiedonbehalfby)

### <a name="BKMK_lk_sharedworkspaceaccesstoken2_createdby"></a> lk_sharedworkspaceaccesstoken2_createdby

One-To-Many Relationship: [systemuser lk_sharedworkspaceaccesstoken2_createdby](systemuser.md#BKMK_lk_sharedworkspaceaccesstoken2_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sharedworkspaceaccesstoken2_createdonbehalfby"></a> lk_sharedworkspaceaccesstoken2_createdonbehalfby

One-To-Many Relationship: [systemuser lk_sharedworkspaceaccesstoken2_createdonbehalfby](systemuser.md#BKMK_lk_sharedworkspaceaccesstoken2_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sharedworkspaceaccesstoken2_modifiedby"></a> lk_sharedworkspaceaccesstoken2_modifiedby

One-To-Many Relationship: [systemuser lk_sharedworkspaceaccesstoken2_modifiedby](systemuser.md#BKMK_lk_sharedworkspaceaccesstoken2_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sharedworkspaceaccesstoken2_modifiedonbehalfby"></a> lk_sharedworkspaceaccesstoken2_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_sharedworkspaceaccesstoken2_modifiedonbehalfby](systemuser.md#BKMK_lk_sharedworkspaceaccesstoken2_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.sharedworkspaceaccesstoken2?displayProperty=fullName>
