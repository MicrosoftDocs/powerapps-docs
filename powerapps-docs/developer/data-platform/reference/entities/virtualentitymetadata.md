---
title: "Virtual Entity  Metadata (VirtualEntityMetadata) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Virtual Entity  Metadata (VirtualEntityMetadata) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Virtual Entity  Metadata (VirtualEntityMetadata) table/entity reference (Microsoft Dataverse)

Holds  metadata values for virtual entities

## Messages

The following table lists the messages for the Virtual Entity  Metadata (VirtualEntityMetadata) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /virtualentitymetadatas<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /virtualentitymetadatas(*virtualentitymetadataid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Retrieve`<br />Event: True |`GET` /virtualentitymetadatas(*virtualentitymetadataid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /virtualentitymetadatas<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /virtualentitymetadatas(*virtualentitymetadataid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /virtualentitymetadatas(*virtualentitymetadataid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /virtualentitymetadatas(*virtualentitymetadataid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Virtual Entity  Metadata (VirtualEntityMetadata) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Virtual Entity  Metadata** |
| **DisplayCollectionName** | **Virtual Entity  Metadatas** |
| **SchemaName** | `VirtualEntityMetadata` |
| **CollectionSchemaName** | `VirtualEntityMetadatas` |
| **EntitySetName** | `virtualentitymetadatas`|
| **LogicalName** | `virtualentitymetadata` |
| **LogicalCollectionName** | `virtualentitymetadatas` |
| **PrimaryIdAttribute** | `virtualentitymetadataid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ExtensionOfRecordId](#BKMK_ExtensionOfRecordId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsAttachmentsSupported](#BKMK_IsAttachmentsSupported)
- [IsChangedFieldsEnabledForUpdateEvent](#BKMK_IsChangedFieldsEnabledForUpdateEvent)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsOnExternalCreatedEnabled](#BKMK_IsOnExternalCreatedEnabled)
- [IsOnExternalDeletedEnabled](#BKMK_IsOnExternalDeletedEnabled)
- [IsOnExternalUpdatedEnabled](#BKMK_IsOnExternalUpdatedEnabled)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [VirtualEntityMetadataId](#BKMK_VirtualEntityMetadataId)

### <a name="BKMK_ExtensionOfRecordId"></a> ExtensionOfRecordId

|Property|Value|
|---|---|
|Description|**The name of the virtual entity that these settings are for.**|
|DisplayName|**Virtual Entity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`extensionofrecordid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|entity|

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

### <a name="BKMK_IsAttachmentsSupported"></a> IsAttachmentsSupported

|Property|Value|
|---|---|
|Description|**Indicates if attachments are supported for the virtual entity**|
|DisplayName|**Is Attachments Supported**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isattachmentssupported`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`virtualentitymetadata_isattachmentssupported`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsChangedFieldsEnabledForUpdateEvent"></a> IsChangedFieldsEnabledForUpdateEvent

|Property|Value|
|---|---|
|Description|**Whether the OnExternalUpdated message ChangedFields parameter will include data about which fields have changed.**|
|DisplayName|**Includes data on changed fields for the update message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ischangedfieldsenabledforupdateevent`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`virtualentitymetadata_ischangedfieldsenabledforupdateevent`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Is Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_IsOnExternalCreatedEnabled"></a> IsOnExternalCreatedEnabled

|Property|Value|
|---|---|
|Description|**Will enable a message to send information about new records created in the external data source.**|
|DisplayName|**Enable external create message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isonexternalcreatedenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`virtualentitymetadata_isonexternalcreatedenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsOnExternalDeletedEnabled"></a> IsOnExternalDeletedEnabled

|Property|Value|
|---|---|
|Description|**Will enable a message to send information about deleted records in the external data source.**|
|DisplayName|**Enable external delete message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isonexternaldeletedenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`virtualentitymetadata_isonexternaldeletedenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsOnExternalUpdatedEnabled"></a> IsOnExternalUpdatedEnabled

|Property|Value|
|---|---|
|Description|**Will enable a message to send information about updated records in the external data source.**|
|DisplayName|**Enable external update message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isonexternalupdatedenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`virtualentitymetadata_isonexternalupdatedenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**The name of the  settings.**|
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

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the VirtualEntityMetadata**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`virtualentitymetadata_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the VirtualEntityMetadata**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`virtualentitymetadata_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Time Zone Rule Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezoneruleversionnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|---|---|
|Description|**Time zone code that was in use when the record was created.**|
|DisplayName|**UTC Conversion Time Zone Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`utcconversiontimezonecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_VirtualEntityMetadataId"></a> VirtualEntityMetadataId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**VirtualEntityMetadata**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`virtualentitymetadataid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentIdUnique"></a> ComponentIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Row id unique**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentidunique`|
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
|DefaultFormValue||
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

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Indicates whether the solution component is part of a managed solution.**|
|DisplayName|**Is Managed**|
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

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier for the organization**|
|DisplayName|**Organization Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|organization|

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
|Format|DateAndTime|
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

- [lk_virtualentitymetadata_createdby](#BKMK_lk_virtualentitymetadata_createdby)
- [lk_virtualentitymetadata_createdonbehalfby](#BKMK_lk_virtualentitymetadata_createdonbehalfby)
- [lk_virtualentitymetadata_modifiedby](#BKMK_lk_virtualentitymetadata_modifiedby)
- [lk_virtualentitymetadata_modifiedonbehalfby](#BKMK_lk_virtualentitymetadata_modifiedonbehalfby)
- [organization_virtualentitymetadata](#BKMK_organization_virtualentitymetadata)
- [virtualentitymetadata_extensionofrecordid](#BKMK_virtualentitymetadata_extensionofrecordid)

### <a name="BKMK_lk_virtualentitymetadata_createdby"></a> lk_virtualentitymetadata_createdby

One-To-Many Relationship: [systemuser lk_virtualentitymetadata_createdby](systemuser.md#BKMK_lk_virtualentitymetadata_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_virtualentitymetadata_createdonbehalfby"></a> lk_virtualentitymetadata_createdonbehalfby

One-To-Many Relationship: [systemuser lk_virtualentitymetadata_createdonbehalfby](systemuser.md#BKMK_lk_virtualentitymetadata_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_virtualentitymetadata_modifiedby"></a> lk_virtualentitymetadata_modifiedby

One-To-Many Relationship: [systemuser lk_virtualentitymetadata_modifiedby](systemuser.md#BKMK_lk_virtualentitymetadata_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_virtualentitymetadata_modifiedonbehalfby"></a> lk_virtualentitymetadata_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_virtualentitymetadata_modifiedonbehalfby](systemuser.md#BKMK_lk_virtualentitymetadata_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_virtualentitymetadata"></a> organization_virtualentitymetadata

One-To-Many Relationship: [organization organization_virtualentitymetadata](organization.md#BKMK_organization_virtualentitymetadata)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_virtualentitymetadata_extensionofrecordid"></a> virtualentitymetadata_extensionofrecordid

One-To-Many Relationship: [entity virtualentitymetadata_extensionofrecordid](entity.md#BKMK_virtualentitymetadata_extensionofrecordid)

|Property|Value|
|---|---|
|ReferencedEntity|`entity`|
|ReferencedAttribute|`entityid`|
|ReferencingAttribute|`extensionofrecordid`|
|ReferencingEntityNavigationPropertyName|`extensionofrecordid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Cascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [virtualentitymetadata_AsyncOperations](#BKMK_virtualentitymetadata_AsyncOperations)
- [virtualentitymetadata_BulkDeleteFailures](#BKMK_virtualentitymetadata_BulkDeleteFailures)
- [virtualentitymetadata_MailboxTrackingFolders](#BKMK_virtualentitymetadata_MailboxTrackingFolders)
- [virtualentitymetadata_PrincipalObjectAttributeAccesses](#BKMK_virtualentitymetadata_PrincipalObjectAttributeAccesses)
- [virtualentitymetadata_ProcessSession](#BKMK_virtualentitymetadata_ProcessSession)
- [virtualentitymetadata_SyncErrors](#BKMK_virtualentitymetadata_SyncErrors)

### <a name="BKMK_virtualentitymetadata_AsyncOperations"></a> virtualentitymetadata_AsyncOperations

Many-To-One Relationship: [asyncoperation virtualentitymetadata_AsyncOperations](asyncoperation.md#BKMK_virtualentitymetadata_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`virtualentitymetadata_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_virtualentitymetadata_BulkDeleteFailures"></a> virtualentitymetadata_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure virtualentitymetadata_BulkDeleteFailures](bulkdeletefailure.md#BKMK_virtualentitymetadata_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`virtualentitymetadata_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_virtualentitymetadata_MailboxTrackingFolders"></a> virtualentitymetadata_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder virtualentitymetadata_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_virtualentitymetadata_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`virtualentitymetadata_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_virtualentitymetadata_PrincipalObjectAttributeAccesses"></a> virtualentitymetadata_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess virtualentitymetadata_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_virtualentitymetadata_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`virtualentitymetadata_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_virtualentitymetadata_ProcessSession"></a> virtualentitymetadata_ProcessSession

Many-To-One Relationship: [processsession virtualentitymetadata_ProcessSession](processsession.md#BKMK_virtualentitymetadata_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`virtualentitymetadata_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_virtualentitymetadata_SyncErrors"></a> virtualentitymetadata_SyncErrors

Many-To-One Relationship: [syncerror virtualentitymetadata_SyncErrors](syncerror.md#BKMK_virtualentitymetadata_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`virtualentitymetadata_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.virtualentitymetadata?displayProperty=fullName>
