---
title: "textdatarecordsindexingstatus table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the textdatarecordsindexingstatus table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# textdatarecordsindexingstatus table/entity reference (Microsoft Dataverse)

Stores information about unstructured / text data records indexing status

## Messages

The following table lists the messages for the textdatarecordsindexingstatus table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /textdatarecordsindexingstatuses<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /textdatarecordsindexingstatuses(*textdatarecordsindexingstatusid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `DeleteMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.DeleteMultiple?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /textdatarecordsindexingstatuses(*textdatarecordsindexingstatusid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /textdatarecordsindexingstatuses<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /textdatarecordsindexingstatuses(*textdatarecordsindexingstatusid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: True |`PATCH` /textdatarecordsindexingstatuses(*textdatarecordsindexingstatusid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the textdatarecordsindexingstatus table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the textdatarecordsindexingstatus table.

|Property|Value|
| --- | --- |
| **DisplayName** | **TextDataRecordsIndexingStatus** |
| **DisplayCollectionName** | **TextDataRecordsIndexingStatus** |
| **SchemaName** | `textdatarecordsindexingstatus` |
| **CollectionSchemaName** | `textdatarecordsindexingstatuses` |
| **EntitySetName** | `textdatarecordsindexingstatuses`|
| **LogicalName** | `textdatarecordsindexingstatus` |
| **LogicalCollectionName** | `textdatarecordsindexingstatuses` |
| **PrimaryIdAttribute** | `textdatarecordsindexingstatusid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Elastic` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AttributeName](#BKMK_AttributeName)
- [EntityName](#BKMK_EntityName)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IndexingStatus](#BKMK_IndexingStatus)
- [Name](#BKMK_Name)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PartitionId](#BKMK_PartitionId)
- [RecordCreatedOnInCrm](#BKMK_RecordCreatedOnInCrm)
- [RecordId](#BKMK_RecordId)
- [RecordModifiedOnInCrm](#BKMK_RecordModifiedOnInCrm)
- [RecordSizeInBytesInCrm](#BKMK_RecordSizeInBytesInCrm)
- [RecordSizeInBytesInTextDataIndex](#BKMK_RecordSizeInBytesInTextDataIndex)
- [RecordVersionNumber](#BKMK_RecordVersionNumber)
- [TextDataIndexName](#BKMK_TextDataIndexName)
- [textdatarecordsindexingstatusId](#BKMK_textdatarecordsindexingstatusId)
- [TTLInSeconds](#BKMK_TTLInSeconds)

### <a name="BKMK_AttributeName"></a> AttributeName

|Property|Value|
|---|---|
|Description|**Attribute name.**|
|DisplayName|**AttributeName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`attributename`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_EntityName"></a> EntityName

|Property|Value|
|---|---|
|Description|**Entity name that identifies which entity does this record belong to.**|
|DisplayName|**EntityName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entityname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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

### <a name="BKMK_IndexingStatus"></a> IndexingStatus

|Property|Value|
|---|---|
|Description|**Unstructured / Text data indexing status of entity - attribute - recordId combination.**|
|DisplayName|**IndexingStatus**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`indexingstatus`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Json|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50000|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**The name of the record.**|
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
|MaxLength|200|

### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|---|---|
|Description|**Object type code of the entity that identifies which entity does this record belong to.**|
|DisplayName|**ObjectTypeCode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`objecttypecode`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

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
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_RecordCreatedOnInCrm"></a> RecordCreatedOnInCrm

|Property|Value|
|---|---|
|Description|**Created on of the record in CRM / Dataverse.**|
|DisplayName|**RecordCreatedOnInCrm**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`recordcreatedonincrm`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_RecordId"></a> RecordId

|Property|Value|
|---|---|
|Description|**Record Id**|
|DisplayName|**RecordId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`recordid`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_RecordModifiedOnInCrm"></a> RecordModifiedOnInCrm

|Property|Value|
|---|---|
|Description|**Modified on of the record in CRM / Dataverse.**|
|DisplayName|**RecordModifiedOnInCrm**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`recordmodifiedonincrm`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_RecordSizeInBytesInCrm"></a> RecordSizeInBytesInCrm

|Property|Value|
|---|---|
|Description|**Size of record in bytes in CRM**|
|DisplayName|**RecordSizeInBytesInCrm**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`recordsizeinbytesincrm`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_RecordSizeInBytesInTextDataIndex"></a> RecordSizeInBytesInTextDataIndex

|Property|Value|
|---|---|
|Description|**Size of record in bytes in Unstructured / Text data search index**|
|DisplayName|**RecordSizeInBytesInTextDataIndex**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`recordsizeinbytesintextdataindex`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_RecordVersionNumber"></a> RecordVersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the record.**|
|DisplayName|**RecordVersionNumber**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`recordversionnumber`|
|RequiredLevel|ApplicationRequired|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_TextDataIndexName"></a> TextDataIndexName

|Property|Value|
|---|---|
|Description|**Unstructured / Text data index name.**|
|DisplayName|**TextDataIndexName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`textdataindexname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_textdatarecordsindexingstatusId"></a> textdatarecordsindexingstatusId

|Property|Value|
|---|---|
|Description|**Unique identifier for TextDataRecordsIndexingStatus**|
|DisplayName|**Text data records indexing status id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`textdatarecordsindexingstatusid`|
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

- [lk_textdatarecordsindexingstatus_createdby](#BKMK_lk_textdatarecordsindexingstatus_createdby)
- [lk_textdatarecordsindexingstatus_createdonbehalfby](#BKMK_lk_textdatarecordsindexingstatus_createdonbehalfby)
- [lk_textdatarecordsindexingstatus_modifiedby](#BKMK_lk_textdatarecordsindexingstatus_modifiedby)
- [lk_textdatarecordsindexingstatus_modifiedonbehalfby](#BKMK_lk_textdatarecordsindexingstatus_modifiedonbehalfby)

### <a name="BKMK_lk_textdatarecordsindexingstatus_createdby"></a> lk_textdatarecordsindexingstatus_createdby

One-To-Many Relationship: [systemuser lk_textdatarecordsindexingstatus_createdby](systemuser.md#BKMK_lk_textdatarecordsindexingstatus_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_textdatarecordsindexingstatus_createdonbehalfby"></a> lk_textdatarecordsindexingstatus_createdonbehalfby

One-To-Many Relationship: [systemuser lk_textdatarecordsindexingstatus_createdonbehalfby](systemuser.md#BKMK_lk_textdatarecordsindexingstatus_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_textdatarecordsindexingstatus_modifiedby"></a> lk_textdatarecordsindexingstatus_modifiedby

One-To-Many Relationship: [systemuser lk_textdatarecordsindexingstatus_modifiedby](systemuser.md#BKMK_lk_textdatarecordsindexingstatus_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_textdatarecordsindexingstatus_modifiedonbehalfby"></a> lk_textdatarecordsindexingstatus_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_textdatarecordsindexingstatus_modifiedonbehalfby](systemuser.md#BKMK_lk_textdatarecordsindexingstatus_modifiedonbehalfby)

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
<xref:Microsoft.Dynamics.CRM.textdatarecordsindexingstatus?displayProperty=fullName>
