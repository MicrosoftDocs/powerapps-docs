---
title: "ElasticFileAttachment table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the ElasticFileAttachment table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# ElasticFileAttachment table/entity reference (Microsoft Dataverse)

Elastic File Attachment

## Messages

The following table lists the messages for the ElasticFileAttachment table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /elasticfileattachments<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /elasticfileattachments(*elasticfileattachmentid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `DeleteMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.DeleteMultiple?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /elasticfileattachments(*elasticfileattachmentid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /elasticfileattachments<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /elasticfileattachments(*elasticfileattachmentid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: True |`PATCH` /elasticfileattachments(*elasticfileattachmentid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the ElasticFileAttachment table.

|Property|Value|
| --- | --- |
| **DisplayName** | **ElasticFileAttachment** |
| **DisplayCollectionName** | **ElasticFileAttachments** |
| **SchemaName** | `ElasticFileAttachment` |
| **CollectionSchemaName** | `ElasticFileAttachments` |
| **EntitySetName** | `elasticfileattachments`|
| **LogicalName** | `elasticfileattachment` |
| **LogicalCollectionName** | `elasticfileattachments` |
| **PrimaryIdAttribute** | `elasticfileattachmentid` |
| **PrimaryNameAttribute** |`filename` |
| **TableType** | `Elastic` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ElasticFileAttachmentId](#BKMK_ElasticFileAttachmentId)
- [FileName](#BKMK_FileName)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [MimeType](#BKMK_MimeType)
- [ObjectId](#BKMK_ObjectId)
- [ObjectIdTypeCode](#BKMK_ObjectIdTypeCode)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PartitionId](#BKMK_PartitionId)
- [RegardingFieldName](#BKMK_RegardingFieldName)
- [TTLInSeconds](#BKMK_TTLInSeconds)

### <a name="BKMK_ElasticFileAttachmentId"></a> ElasticFileAttachmentId

|Property|Value|
|---|---|
|Description|**Unique identifier of the elastic file attachment.**|
|DisplayName|**ElasticFileAttachmentId**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`elasticfileattachmentid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_FileName"></a> FileName

|Property|Value|
|---|---|
|Description|**File name of the attachment.**|
|DisplayName|**File Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`filename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|255|

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

### <a name="BKMK_MimeType"></a> MimeType

|Property|Value|
|---|---|
|Description|**MIME type of the attachment.**|
|DisplayName|**MIME Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mimetype`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|---|---|
|Description|**Unique identifier of the object with which the attachment is associated.**|
|DisplayName|**Regarding**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|componentchangesetpayload, componentversionnrddatasource, sourcecontrolcomponentpayload|

### <a name="BKMK_ObjectIdTypeCode"></a> ObjectIdTypeCode

|Property|Value|
|---|---|
|Description|**Type of entity with which the elastic file attachment is associated.**|
|DisplayName|**Object Id Type Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objectidtypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|---|---|
|Description|**Type of entity with which the elastic file attachment is associated.**|
|DisplayName|**Object Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

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

### <a name="BKMK_RegardingFieldName"></a> RegardingFieldName

|Property|Value|
|---|---|
|Description|**Regarding attribute schema name of the attachment.**|
|DisplayName|**Regarding Attribute Schema Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingfieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|255|

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

- [CreatedOn](#BKMK_CreatedOn)
- [FilePointer](#BKMK_FilePointer)
- [FileSizeInBytes](#BKMK_FileSizeInBytes)
- [Prefix](#BKMK_Prefix)
- [StoragePointer](#BKMK_StoragePointer)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the attachment was created.**|
|DisplayName|**Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_FilePointer"></a> FilePointer

|Property|Value|
|---|---|
|Description|**File pointer of the attachment.**|
|DisplayName|**File Pointer**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`filepointer`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|255|

### <a name="BKMK_FileSizeInBytes"></a> FileSizeInBytes

|Property|Value|
|---|---|
|Description|**File size of the attachment in bytes.**|
|DisplayName|**File Size (Bytes)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`filesizeinbytes`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_Prefix"></a> Prefix

|Property|Value|
|---|---|
|Description|**Prefix of the file pointer in blob storage.**|
|DisplayName|**Prefix**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`prefix`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10|

### <a name="BKMK_StoragePointer"></a> StoragePointer

|Property|Value|
|---|---|
|Description|**Storage pointer.**|
|DisplayName|**Storage Pointer**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`storagepointer`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the file attachment.**|
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

- [componentchangesetpayload_ElasticFileAttachments](#BKMK_componentchangesetpayload_ElasticFileAttachments)
- [componentversionnrddatasource_ElasticFileAttachments](#BKMK_componentversionnrddatasource_ElasticFileAttachments)
- [sourcecontrolcomponentpayload_ElasticFileAttachments](#BKMK_sourcecontrolcomponentpayload_ElasticFileAttachments)

### <a name="BKMK_componentchangesetpayload_ElasticFileAttachments"></a> componentchangesetpayload_ElasticFileAttachments

One-To-Many Relationship: [componentchangesetpayload componentchangesetpayload_ElasticFileAttachments](componentchangesetpayload.md#BKMK_componentchangesetpayload_ElasticFileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`componentchangesetpayload`|
|ReferencedAttribute|`componentchangesetpayloadid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_componentversionnrddatasource_ElasticFileAttachments"></a> componentversionnrddatasource_ElasticFileAttachments

One-To-Many Relationship: [componentversionnrddatasource componentversionnrddatasource_ElasticFileAttachments](componentversionnrddatasource.md#BKMK_componentversionnrddatasource_ElasticFileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`componentversionnrddatasource`|
|ReferencedAttribute|`componentversionnrddatasourceid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_componentversionnrddatasource`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sourcecontrolcomponentpayload_ElasticFileAttachments"></a> sourcecontrolcomponentpayload_ElasticFileAttachments

One-To-Many Relationship: [sourcecontrolcomponentpayload sourcecontrolcomponentpayload_ElasticFileAttachments](sourcecontrolcomponentpayload.md#BKMK_sourcecontrolcomponentpayload_ElasticFileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`sourcecontrolcomponentpayload`|
|ReferencedAttribute|`sourcecontrolcomponentpayloadid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_sourcecontrolcomponentpayload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [ElasticFileAttachment_componentchangesetpayload_payload](#BKMK_ElasticFileAttachment_componentchangesetpayload_payload)
- [ElasticFileAttachment_componentversionnrddatasource_Payload](#BKMK_ElasticFileAttachment_componentversionnrddatasource_Payload)
- [ElasticFileAttachment_SourceControlComponentPayload_ComponentPayload](#BKMK_ElasticFileAttachment_SourceControlComponentPayload_ComponentPayload)
- [ElasticFileAttachment_SourceControlComponentPayload_ComponentPayloadInGit](#BKMK_ElasticFileAttachment_SourceControlComponentPayload_ComponentPayloadInGit)

### <a name="BKMK_ElasticFileAttachment_componentchangesetpayload_payload"></a> ElasticFileAttachment_componentchangesetpayload_payload

Many-To-One Relationship: [componentchangesetpayload ElasticFileAttachment_componentchangesetpayload_payload](componentchangesetpayload.md#BKMK_ElasticFileAttachment_componentchangesetpayload_payload)

|Property|Value|
|---|---|
|ReferencingEntity|`componentchangesetpayload`|
|ReferencingAttribute|`payload`|
|ReferencedEntityNavigationPropertyName|`ElasticFileAttachment_componentchangesetpayload_payload`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_ElasticFileAttachment_componentversionnrddatasource_Payload"></a> ElasticFileAttachment_componentversionnrddatasource_Payload

Many-To-One Relationship: [componentversionnrddatasource ElasticFileAttachment_componentversionnrddatasource_Payload](componentversionnrddatasource.md#BKMK_ElasticFileAttachment_componentversionnrddatasource_Payload)

|Property|Value|
|---|---|
|ReferencingEntity|`componentversionnrddatasource`|
|ReferencingAttribute|`payload`|
|ReferencedEntityNavigationPropertyName|`ElasticFileAttachment_componentversionnrddatasource_Payload`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_ElasticFileAttachment_SourceControlComponentPayload_ComponentPayload"></a> ElasticFileAttachment_SourceControlComponentPayload_ComponentPayload

Many-To-One Relationship: [sourcecontrolcomponentpayload ElasticFileAttachment_SourceControlComponentPayload_ComponentPayload](sourcecontrolcomponentpayload.md#BKMK_ElasticFileAttachment_SourceControlComponentPayload_ComponentPayload)

|Property|Value|
|---|---|
|ReferencingEntity|`sourcecontrolcomponentpayload`|
|ReferencingAttribute|`componentpayload`|
|ReferencedEntityNavigationPropertyName|`ElasticFileAttachment_SourceControlComponentPayload_ComponentPayload`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_ElasticFileAttachment_SourceControlComponentPayload_ComponentPayloadInGit"></a> ElasticFileAttachment_SourceControlComponentPayload_ComponentPayloadInGit

Many-To-One Relationship: [sourcecontrolcomponentpayload ElasticFileAttachment_SourceControlComponentPayload_ComponentPayloadInGit](sourcecontrolcomponentpayload.md#BKMK_ElasticFileAttachment_SourceControlComponentPayload_ComponentPayloadInGit)

|Property|Value|
|---|---|
|ReferencingEntity|`sourcecontrolcomponentpayload`|
|ReferencingAttribute|`componentpayloadingit`|
|ReferencedEntityNavigationPropertyName|`ElasticFileAttachment_SourceControlComponentPayload_ComponentPayloadInGit`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.elasticfileattachment?displayProperty=fullName>
