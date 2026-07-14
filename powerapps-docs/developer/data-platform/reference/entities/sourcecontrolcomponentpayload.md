---
title: "Source Control Component Payload (SourceControlComponentPayload) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Source Control Component Payload (SourceControlComponentPayload) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Source Control Component Payload (SourceControlComponentPayload) table/entity reference (Microsoft Dataverse)

Stores the Source Control Component Payloads associated with components.

## Messages

The following table lists the messages for the Source Control Component Payload (SourceControlComponentPayload) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /sourcecontrolcomponentpayloads<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: False |`DELETE` /sourcecontrolcomponentpayloads(*sourcecontrolcomponentpayloadid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `DeleteMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.DeleteMultiple?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /sourcecontrolcomponentpayloads(*sourcecontrolcomponentpayloadid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: False | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: False |`GET` /sourcecontrolcomponentpayloads<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /sourcecontrolcomponentpayloads(*sourcecontrolcomponentpayloadid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /sourcecontrolcomponentpayloads(*sourcecontrolcomponentpayloadid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Source Control Component Payload (SourceControlComponentPayload) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Source Control Component Payload** |
| **DisplayCollectionName** | **Source Control Component Payloads** |
| **SchemaName** | `SourceControlComponentPayload` |
| **CollectionSchemaName** | `SourceControlComponentPayloads` |
| **EntitySetName** | `sourcecontrolcomponentpayloads`|
| **LogicalName** | `sourcecontrolcomponentpayload` |
| **LogicalCollectionName** | `sourcecontrolcomponentpayloads` |
| **PrimaryIdAttribute** | `sourcecontrolcomponentpayloadid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Elastic` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ComponentId](#BKMK_ComponentId)
- [GitHashId](#BKMK_GitHashId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [LastSyncHashId](#BKMK_LastSyncHashId)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PartitionId](#BKMK_PartitionId)
- [ReferringSolutions](#BKMK_ReferringSolutions)
- [SourceControlComponentPayloadId](#BKMK_SourceControlComponentPayloadId)
- [TTLInSeconds](#BKMK_TTLInSeconds)

### <a name="BKMK_ComponentId"></a> ComponentId

|Property|Value|
|---|---|
|Description|**Component id of the component**|
|DisplayName|**Component Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`componentid`|
|RequiredLevel|Recommended|
|Type|Uniqueidentifier|

### <a name="BKMK_GitHashId"></a> GitHashId

|Property|Value|
|---|---|
|Description|**This stores git hash id.**|
|DisplayName|**GitHash Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`githashid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

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

### <a name="BKMK_LastSyncHashId"></a> LastSyncHashId

|Property|Value|
|---|---|
|Description|**This stores last sync hash id.**|
|DisplayName|**LastSyncHash Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastsynchashid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description||
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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

### <a name="BKMK_ReferringSolutions"></a> ReferringSolutions

|Property|Value|
|---|---|
|Description|**List of solution identifiers where this component is present**|
|DisplayName|**List of solution identifiers where this component is present**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`referringsolutions`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_SourceControlComponentPayloadId"></a> SourceControlComponentPayloadId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Source Control Component Payload Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sourcecontrolcomponentpayloadid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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

- [ComponentPayload](#BKMK_ComponentPayload)
- [ComponentPayload_Name](#BKMK_ComponentPayload_Name)
- [ComponentPayloadInGit](#BKMK_ComponentPayloadInGit)
- [ComponentPayloadInGit_Name](#BKMK_ComponentPayloadInGit_Name)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentPayload"></a> ComponentPayload

|Property|Value|
|---|---|
|Description|**Payload of the component**|
|DisplayName|**Component Payload**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`componentpayload`|
|RequiredLevel|ApplicationRequired|
|Type|File|
|MaxSizeInKB|131072|

### <a name="BKMK_ComponentPayload_Name"></a> ComponentPayload_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentpayload_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_ComponentPayloadInGit"></a> ComponentPayloadInGit

|Property|Value|
|---|---|
|Description|**Payload of the component in Git**|
|DisplayName|**Component Payload in Git**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`componentpayloadingit`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|131072|

### <a name="BKMK_ComponentPayloadInGit_Name"></a> ComponentPayloadInGit_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentpayloadingit_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

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

- [ElasticFileAttachment_SourceControlComponentPayload_ComponentPayload](#BKMK_ElasticFileAttachment_SourceControlComponentPayload_ComponentPayload)
- [ElasticFileAttachment_SourceControlComponentPayload_ComponentPayloadInGit](#BKMK_ElasticFileAttachment_SourceControlComponentPayload_ComponentPayloadInGit)
- [lk_sourcecontrolcomponentpayload_createdby](#BKMK_lk_sourcecontrolcomponentpayload_createdby)
- [lk_sourcecontrolcomponentpayload_createdonbehalfby](#BKMK_lk_sourcecontrolcomponentpayload_createdonbehalfby)
- [lk_sourcecontrolcomponentpayload_modifiedby](#BKMK_lk_sourcecontrolcomponentpayload_modifiedby)
- [lk_sourcecontrolcomponentpayload_modifiedonbehalfby](#BKMK_lk_sourcecontrolcomponentpayload_modifiedonbehalfby)

### <a name="BKMK_ElasticFileAttachment_SourceControlComponentPayload_ComponentPayload"></a> ElasticFileAttachment_SourceControlComponentPayload_ComponentPayload

One-To-Many Relationship: [elasticfileattachment ElasticFileAttachment_SourceControlComponentPayload_ComponentPayload](elasticfileattachment.md#BKMK_ElasticFileAttachment_SourceControlComponentPayload_ComponentPayload)

|Property|Value|
|---|---|
|ReferencedEntity|`elasticfileattachment`|
|ReferencedAttribute|`elasticfileattachmentid`|
|ReferencingAttribute|`componentpayload`|
|ReferencingEntityNavigationPropertyName|`componentpayload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ElasticFileAttachment_SourceControlComponentPayload_ComponentPayloadInGit"></a> ElasticFileAttachment_SourceControlComponentPayload_ComponentPayloadInGit

One-To-Many Relationship: [elasticfileattachment ElasticFileAttachment_SourceControlComponentPayload_ComponentPayloadInGit](elasticfileattachment.md#BKMK_ElasticFileAttachment_SourceControlComponentPayload_ComponentPayloadInGit)

|Property|Value|
|---|---|
|ReferencedEntity|`elasticfileattachment`|
|ReferencedAttribute|`elasticfileattachmentid`|
|ReferencingAttribute|`componentpayloadingit`|
|ReferencingEntityNavigationPropertyName|`componentpayloadingit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sourcecontrolcomponentpayload_createdby"></a> lk_sourcecontrolcomponentpayload_createdby

One-To-Many Relationship: [systemuser lk_sourcecontrolcomponentpayload_createdby](systemuser.md#BKMK_lk_sourcecontrolcomponentpayload_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sourcecontrolcomponentpayload_createdonbehalfby"></a> lk_sourcecontrolcomponentpayload_createdonbehalfby

One-To-Many Relationship: [systemuser lk_sourcecontrolcomponentpayload_createdonbehalfby](systemuser.md#BKMK_lk_sourcecontrolcomponentpayload_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sourcecontrolcomponentpayload_modifiedby"></a> lk_sourcecontrolcomponentpayload_modifiedby

One-To-Many Relationship: [systemuser lk_sourcecontrolcomponentpayload_modifiedby](systemuser.md#BKMK_lk_sourcecontrolcomponentpayload_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sourcecontrolcomponentpayload_modifiedonbehalfby"></a> lk_sourcecontrolcomponentpayload_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_sourcecontrolcomponentpayload_modifiedonbehalfby](systemuser.md#BKMK_lk_sourcecontrolcomponentpayload_modifiedonbehalfby)

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

- [sourcecontrolcomponentpayload_ElasticFileAttachments](#BKMK_sourcecontrolcomponentpayload_ElasticFileAttachments)
- [sourcecontrolcomponentpayload_sourcecontrolcomponent](#BKMK_sourcecontrolcomponentpayload_sourcecontrolcomponent)

### <a name="BKMK_sourcecontrolcomponentpayload_ElasticFileAttachments"></a> sourcecontrolcomponentpayload_ElasticFileAttachments

Many-To-One Relationship: [elasticfileattachment sourcecontrolcomponentpayload_ElasticFileAttachments](elasticfileattachment.md#BKMK_sourcecontrolcomponentpayload_ElasticFileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`elasticfileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`sourcecontrolcomponentpayload_ElasticFileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sourcecontrolcomponentpayload_sourcecontrolcomponent"></a> sourcecontrolcomponentpayload_sourcecontrolcomponent

Many-To-One Relationship: [sourcecontrolcomponent sourcecontrolcomponentpayload_sourcecontrolcomponent](sourcecontrolcomponent.md#BKMK_sourcecontrolcomponentpayload_sourcecontrolcomponent)

|Property|Value|
|---|---|
|ReferencingEntity|`sourcecontrolcomponent`|
|ReferencingAttribute|`sourcecontrolcomponentpayloadid`|
|ReferencedEntityNavigationPropertyName|`sourcecontrolcomponentpayload`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.sourcecontrolcomponentpayload?displayProperty=fullName>
