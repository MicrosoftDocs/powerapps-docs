---
title: "Synapse Link Profile Entity State (synapselinkprofileentitystate) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Synapse Link Profile Entity State (synapselinkprofileentitystate) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Synapse Link Profile Entity State (synapselinkprofileentitystate) table/entity reference (Microsoft Dataverse)

Runtime state of the Synapse Link entity

## Messages

The following table lists the messages for the Synapse Link Profile Entity State (synapselinkprofileentitystate) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /synapselinkprofileentitystates<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /synapselinkprofileentitystates(*synapselinkprofileentitystateid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Retrieve`<br />Event: True |`GET` /synapselinkprofileentitystates(*synapselinkprofileentitystateid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /synapselinkprofileentitystates<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /synapselinkprofileentitystates(*synapselinkprofileentitystateid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /synapselinkprofileentitystates(*synapselinkprofileentitystateid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /synapselinkprofileentitystates(*synapselinkprofileentitystateid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Synapse Link Profile Entity State (synapselinkprofileentitystate) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Synapse Link Profile Entity State** |
| **DisplayCollectionName** | **Synapse Link Profile Entity States** |
| **SchemaName** | `synapselinkprofileentitystate` |
| **CollectionSchemaName** | `synapselinkprofileentitystates` |
| **EntitySetName** | `synapselinkprofileentitystates`|
| **LogicalName** | `synapselinkprofileentitystate` |
| **LogicalCollectionName** | `synapselinkprofileentitystates` |
| **PrimaryIdAttribute** | `synapselinkprofileentitystateid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AdditionTime](#BKMK_AdditionTime)
- [CrmRecordCount](#BKMK_CrmRecordCount)
- [CrmRecordCountModifiedTime](#BKMK_CrmRecordCountModifiedTime)
- [EntityName](#BKMK_EntityName)
- [EntitySource](#BKMK_EntitySource)
- [EntityType](#BKMK_EntityType)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [InitialSyncDataCompletedTime](#BKMK_InitialSyncDataCompletedTime)
- [InitialSyncMetadataCreatedTime](#BKMK_InitialSyncMetadataCreatedTime)
- [InitialSyncProcessCompletedTime](#BKMK_InitialSyncProcessCompletedTime)
- [InitialSyncState](#BKMK_InitialSyncState)
- [LakeRecordCount](#BKMK_LakeRecordCount)
- [LakeRecordCountModifiedTime](#BKMK_LakeRecordCountModifiedTime)
- [LastSyncedDataTime](#BKMK_LastSyncedDataTime)
- [LastSyncedDataVersion](#BKMK_LastSyncedDataVersion)
- [LastSyncedMetadataTime](#BKMK_LastSyncedMetadataTime)
- [LastSyncedMetadataVersion](#BKMK_LastSyncedMetadataVersion)
- [MetadataState](#BKMK_MetadataState)
- [MinSyncedDataVersion](#BKMK_MinSyncedDataVersion)
- [name](#BKMK_name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [profile](#BKMK_profile)
- [profileentity](#BKMK_profileentity)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [synapselinkprofileentitystateId](#BKMK_synapselinkprofileentitystateId)
- [SynapseTableCreationState](#BKMK_SynapseTableCreationState)
- [SyncState](#BKMK_SyncState)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_AdditionTime"></a> AdditionTime

|Property|Value|
|---|---|
|Description|**Addition time of entity**|
|DisplayName|**Addition Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`additiontime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_CrmRecordCount"></a> CrmRecordCount

|Property|Value|
|---|---|
|Description|**CRM record count**|
|DisplayName|**CRM Record Count**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`crmrecordcount`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_CrmRecordCountModifiedTime"></a> CrmRecordCountModifiedTime

|Property|Value|
|---|---|
|Description|**CRM record count modified time for entity**|
|DisplayName|**CRM Record Count Modified Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`crmrecordcountmodifiedtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_EntityName"></a> EntityName

|Property|Value|
|---|---|
|Description|**Name of the entity**|
|DisplayName|**EntityName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entityname`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_EntitySource"></a> EntitySource

|Property|Value|
|---|---|
|Description|**Source of the entity**|
|DisplayName|**Entity source**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entitysource`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`synapselinkentitysource`|

#### EntitySource Choices/Options

|Value|Label|
|---|---|
|0|**Dataverse**|
|1|**FnOTables**|

### <a name="BKMK_EntityType"></a> EntityType

|Property|Value|
|---|---|
|Description|**Type of the entity**|
|DisplayName|**EntityType**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entitytype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`synapselinkprofileentitytype`|

#### EntityType Choices/Options

|Value|Label|
|---|---|
|0|**Requested**|

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

### <a name="BKMK_InitialSyncDataCompletedTime"></a> InitialSyncDataCompletedTime

|Property|Value|
|---|---|
|Description|**Initial sync data completed time**|
|DisplayName|**Initial Sync Data Completed Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`initialsyncdatacompletedtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_InitialSyncMetadataCreatedTime"></a> InitialSyncMetadataCreatedTime

|Property|Value|
|---|---|
|Description|**Initial sync metadata created time**|
|DisplayName|**Initial Sync Metadata Created Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`initialsyncmetadatacreatedtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_InitialSyncProcessCompletedTime"></a> InitialSyncProcessCompletedTime

|Property|Value|
|---|---|
|Description|**Initial sync process completed time**|
|DisplayName|**Initial Sync Process Completed Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`initialsyncprocesscompletedtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_InitialSyncState"></a> InitialSyncState

|Property|Value|
|---|---|
|Description|**Initial sync state**|
|DisplayName|**Initial Sync State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`initialsyncstate`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`synapselinkentitysyncstate`|

#### InitialSyncState Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**NotStarted**|
|2|**InProgress**|
|4|**Completed**|
|8|**CompletedWithFailures**|
|16|**RequestedInitialData**|
|32|**Paused**|
|64|**PostProcessing**|

### <a name="BKMK_LakeRecordCount"></a> LakeRecordCount

|Property|Value|
|---|---|
|Description|**Lake record count**|
|DisplayName|**Lake Record Count**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lakerecordcount`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_LakeRecordCountModifiedTime"></a> LakeRecordCountModifiedTime

|Property|Value|
|---|---|
|Description|**Lake record count modified time for entity**|
|DisplayName|**Lake Record Count Modified Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lakerecordcountmodifiedtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_LastSyncedDataTime"></a> LastSyncedDataTime

|Property|Value|
|---|---|
|Description|**Last synced data time**|
|DisplayName|**Last Synced Data Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastsynceddatatime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_LastSyncedDataVersion"></a> LastSyncedDataVersion

|Property|Value|
|---|---|
|Description|**Last synced data version**|
|DisplayName|**Last Synced Data Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastsynceddataversion`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|32|

### <a name="BKMK_LastSyncedMetadataTime"></a> LastSyncedMetadataTime

|Property|Value|
|---|---|
|Description|**Last synced metadata time**|
|DisplayName|**Last Synced Metadata Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastsyncedmetadatatime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_LastSyncedMetadataVersion"></a> LastSyncedMetadataVersion

|Property|Value|
|---|---|
|Description|**Last synced metadata version**|
|DisplayName|**Last Synced Metadata Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastsyncedmetadataversion`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|32|

### <a name="BKMK_MetadataState"></a> MetadataState

|Property|Value|
|---|---|
|Description|**Metadata state**|
|DisplayName|**Metadata State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`metadatastate`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`synapselinkentitymetadatastate`|

#### MetadataState Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**NotCreated**|
|2|**MetadataCreating**|
|4|**RelationshipCreating**|
|8|**Created**|
|16|**Failure**|

### <a name="BKMK_MinSyncedDataVersion"></a> MinSyncedDataVersion

|Property|Value|
|---|---|
|Description|**Last Synced Minimum Data Version**|
|DisplayName|**MinSyncVersion**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`minsynceddataversion`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_name"></a> name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
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

### <a name="BKMK_profile"></a> profile

|Property|Value|
|---|---|
|Description|**Unique identifier for Synapse Link Profile associated with Synapse Link Profile Entity State.**|
|DisplayName|**Profile**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`profile`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|synapselinkprofile|

### <a name="BKMK_profileentity"></a> profileentity

|Property|Value|
|---|---|
|Description|**Unique identifier for Synapse Link Profile Entity associated with Synapse Link Profile Entity State.**|
|DisplayName|**ProfileEntity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`profileentity`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|synapselinkprofileentity|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Synapse Link Profile Entity State**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`synapselinkprofileentitystate_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Synapse Link Profile Entity State**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`synapselinkprofileentitystate_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_synapselinkprofileentitystateId"></a> synapselinkprofileentitystateId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Synapse Link Profile Entity State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`synapselinkprofileentitystateid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SynapseTableCreationState"></a> SynapseTableCreationState

|Property|Value|
|---|---|
|Description|**Synapse table creation state**|
|DisplayName|**Synapse Table Creation State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`synapsetablecreationstate`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`synapselinksynapsetablecreationstate`|

#### SynapseTableCreationState Choices/Options

|Value|Label|
|---|---|
|0|**NotStarted**|
|1|**InProgress**|
|2|**Completed**|
|3|**Failed**|

### <a name="BKMK_SyncState"></a> SyncState

|Property|Value|
|---|---|
|Description|**Entity sync state**|
|DisplayName|**SyncState**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`syncstate`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`synapselinkentitysyncstate`|

#### SyncState Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**NotStarted**|
|2|**InProgress**|
|4|**Completed**|
|8|**CompletedWithFailures**|
|16|**RequestedInitialData**|
|32|**Paused**|
|64|**PostProcessing**|

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


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
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

- [entitystate](#BKMK_entitystate)
- [lk_synapselinkprofileentitystate_createdby](#BKMK_lk_synapselinkprofileentitystate_createdby)
- [lk_synapselinkprofileentitystate_createdonbehalfby](#BKMK_lk_synapselinkprofileentitystate_createdonbehalfby)
- [lk_synapselinkprofileentitystate_modifiedby](#BKMK_lk_synapselinkprofileentitystate_modifiedby)
- [lk_synapselinkprofileentitystate_modifiedonbehalfby](#BKMK_lk_synapselinkprofileentitystate_modifiedonbehalfby)
- [organization_synapselinkprofileentitystate](#BKMK_organization_synapselinkprofileentitystate)
- [profileentitystates](#BKMK_profileentitystates)

### <a name="BKMK_entitystate"></a> entitystate

One-To-Many Relationship: [synapselinkprofileentity entitystate](synapselinkprofileentity.md#BKMK_entitystate)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofileentity`|
|ReferencedAttribute|`synapselinkprofileentityid`|
|ReferencingAttribute|`profileentity`|
|ReferencingEntityNavigationPropertyName|`profileentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_lk_synapselinkprofileentitystate_createdby"></a> lk_synapselinkprofileentitystate_createdby

One-To-Many Relationship: [systemuser lk_synapselinkprofileentitystate_createdby](systemuser.md#BKMK_lk_synapselinkprofileentitystate_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_synapselinkprofileentitystate_createdonbehalfby"></a> lk_synapselinkprofileentitystate_createdonbehalfby

One-To-Many Relationship: [systemuser lk_synapselinkprofileentitystate_createdonbehalfby](systemuser.md#BKMK_lk_synapselinkprofileentitystate_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_synapselinkprofileentitystate_modifiedby"></a> lk_synapselinkprofileentitystate_modifiedby

One-To-Many Relationship: [systemuser lk_synapselinkprofileentitystate_modifiedby](systemuser.md#BKMK_lk_synapselinkprofileentitystate_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_synapselinkprofileentitystate_modifiedonbehalfby"></a> lk_synapselinkprofileentitystate_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_synapselinkprofileentitystate_modifiedonbehalfby](systemuser.md#BKMK_lk_synapselinkprofileentitystate_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_synapselinkprofileentitystate"></a> organization_synapselinkprofileentitystate

One-To-Many Relationship: [organization organization_synapselinkprofileentitystate](organization.md#BKMK_organization_synapselinkprofileentitystate)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_profileentitystates"></a> profileentitystates

One-To-Many Relationship: [synapselinkprofile profileentitystates](synapselinkprofile.md#BKMK_profileentitystates)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofile`|
|ReferencedAttribute|`synapselinkprofileid`|
|ReferencingAttribute|`profile`|
|ReferencingEntityNavigationPropertyName|`profile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [synapselinkprofileentitystate_AsyncOperations](#BKMK_synapselinkprofileentitystate_AsyncOperations)
- [synapselinkprofileentitystate_BulkDeleteFailures](#BKMK_synapselinkprofileentitystate_BulkDeleteFailures)
- [synapselinkprofileentitystate_DuplicateBaseRecord](#BKMK_synapselinkprofileentitystate_DuplicateBaseRecord)
- [synapselinkprofileentitystate_DuplicateMatchingRecord](#BKMK_synapselinkprofileentitystate_DuplicateMatchingRecord)
- [synapselinkprofileentitystate_MailboxTrackingFolders](#BKMK_synapselinkprofileentitystate_MailboxTrackingFolders)
- [synapselinkprofileentitystate_PrincipalObjectAttributeAccesses](#BKMK_synapselinkprofileentitystate_PrincipalObjectAttributeAccesses)
- [synapselinkprofileentitystate_ProcessSession](#BKMK_synapselinkprofileentitystate_ProcessSession)
- [synapselinkprofileentitystate_SyncErrors](#BKMK_synapselinkprofileentitystate_SyncErrors)

### <a name="BKMK_synapselinkprofileentitystate_AsyncOperations"></a> synapselinkprofileentitystate_AsyncOperations

Many-To-One Relationship: [asyncoperation synapselinkprofileentitystate_AsyncOperations](asyncoperation.md#BKMK_synapselinkprofileentitystate_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofileentitystate_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofileentitystate_BulkDeleteFailures"></a> synapselinkprofileentitystate_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure synapselinkprofileentitystate_BulkDeleteFailures](bulkdeletefailure.md#BKMK_synapselinkprofileentitystate_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofileentitystate_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofileentitystate_DuplicateBaseRecord"></a> synapselinkprofileentitystate_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord synapselinkprofileentitystate_DuplicateBaseRecord](duplicaterecord.md#BKMK_synapselinkprofileentitystate_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofileentitystate_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofileentitystate_DuplicateMatchingRecord"></a> synapselinkprofileentitystate_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord synapselinkprofileentitystate_DuplicateMatchingRecord](duplicaterecord.md#BKMK_synapselinkprofileentitystate_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofileentitystate_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofileentitystate_MailboxTrackingFolders"></a> synapselinkprofileentitystate_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder synapselinkprofileentitystate_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_synapselinkprofileentitystate_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofileentitystate_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofileentitystate_PrincipalObjectAttributeAccesses"></a> synapselinkprofileentitystate_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess synapselinkprofileentitystate_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_synapselinkprofileentitystate_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofileentitystate_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofileentitystate_ProcessSession"></a> synapselinkprofileentitystate_ProcessSession

Many-To-One Relationship: [processsession synapselinkprofileentitystate_ProcessSession](processsession.md#BKMK_synapselinkprofileentitystate_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofileentitystate_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofileentitystate_SyncErrors"></a> synapselinkprofileentitystate_SyncErrors

Many-To-One Relationship: [syncerror synapselinkprofileentitystate_SyncErrors](syncerror.md#BKMK_synapselinkprofileentitystate_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofileentitystate_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.synapselinkprofileentitystate?displayProperty=fullName>
