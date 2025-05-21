---
title: "Synapse Link External Table State (synapselinkexternaltablestate) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Synapse Link External Table State (synapselinkexternaltablestate) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Synapse Link External Table State (synapselinkexternaltablestate) table/entity reference (Microsoft Dataverse)

Synapse Link external table states

## Messages

The following table lists the messages for the Synapse Link External Table State (synapselinkexternaltablestate) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /synapselinkexternaltablestates<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /synapselinkexternaltablestates(*synapselinkexternaltablestateid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Retrieve`<br />Event: True |`GET` /synapselinkexternaltablestates(*synapselinkexternaltablestateid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /synapselinkexternaltablestates<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /synapselinkexternaltablestates(*synapselinkexternaltablestateid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /synapselinkexternaltablestates(*synapselinkexternaltablestateid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /synapselinkexternaltablestates(*synapselinkexternaltablestateid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Synapse Link External Table State (synapselinkexternaltablestate) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Synapse Link External Table State** |
| **DisplayCollectionName** | **Synapse Link External Table States** |
| **SchemaName** | `synapselinkexternaltablestate` |
| **CollectionSchemaName** | `synapselinkexternaltablestates` |
| **EntitySetName** | `synapselinkexternaltablestates`|
| **LogicalName** | `synapselinkexternaltablestate` |
| **LogicalCollectionName** | `synapselinkexternaltablestates` |
| **PrimaryIdAttribute** | `synapselinkexternaltablestateid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [datalakefolder](#BKMK_datalakefolder)
- [EntityName](#BKMK_EntityName)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [LakehouseShortcutState](#BKMK_LakehouseShortcutState)
- [LastSynchronizedOn](#BKMK_LastSynchronizedOn)
- [LastSyncState](#BKMK_LastSyncState)
- [MaxRecordVersion](#BKMK_MaxRecordVersion)
- [MetadataVersion](#BKMK_MetadataVersion)
- [MinSyncedDataVersion](#BKMK_MinSyncedDataVersion)
- [name](#BKMK_name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [RecordCount](#BKMK_RecordCount)
- [SchemaModifiedOn](#BKMK_SchemaModifiedOn)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [SynapseDatabaseName](#BKMK_SynapseDatabaseName)
- [synapselinkexternaltablestateId](#BKMK_synapselinkexternaltablestateId)
- [SynapseWorkspaceName](#BKMK_SynapseWorkspaceName)
- [TableState](#BKMK_TableState)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [TrinoState](#BKMK_TrinoState)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_datalakefolder"></a> datalakefolder

|Property|Value|
|---|---|
|Description|**Unique identifier for Data Lake Folder associated with Synapse Link External Table State.**|
|DisplayName|**Data Lake Folder**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`datalakefolder`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|datalakefolder|

### <a name="BKMK_EntityName"></a> EntityName

|Property|Value|
|---|---|
|Description|**Name of the entity**|
|DisplayName|**Entity Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entityname`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|64|

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

### <a name="BKMK_LakehouseShortcutState"></a> LakehouseShortcutState

|Property|Value|
|---|---|
|Description|**State of lakehouse shortcut creation for an entity**|
|DisplayName|**Lakehouse Shortcut State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lakehouseshortcutstate`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`synapselinkexternaltablestate`|

#### LakehouseShortcutState Choices/Options

|Value|Label|
|---|---|
|0|**Not Created**|
|1|**Created**|
|2|**Failed**|
|3|**Deleted**|
|4|**In Progress**|

### <a name="BKMK_LastSynchronizedOn"></a> LastSynchronizedOn

|Property|Value|
|---|---|
|Description|**Last SynchronizedOn Date time**|
|DisplayName|**Last Synchronized On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastsynchronizedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_LastSyncState"></a> LastSyncState

|Property|Value|
|---|---|
|Description|**Last data synchronization state**|
|DisplayName|**Last Synchronization State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastsyncstate`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`synapselinkexternaltablestate`|

#### LastSyncState Choices/Options

|Value|Label|
|---|---|
|0|**Not Created**|
|1|**Created**|
|2|**Failed**|
|3|**Deleted**|
|4|**In Progress**|

### <a name="BKMK_MaxRecordVersion"></a> MaxRecordVersion

|Property|Value|
|---|---|
|Description|**Maximum record version synchronized to the lake**|
|DisplayName|**Maximum Record Version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maxrecordversion`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_MetadataVersion"></a> MetadataVersion

|Property|Value|
|---|---|
|Description|**Metadata version**|
|DisplayName|**Metadata Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`metadataversion`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|32|

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

### <a name="BKMK_RecordCount"></a> RecordCount

|Property|Value|
|---|---|
|Description|**Record count synchronized to lake**|
|DisplayName|**Record Count**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`recordcount`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_SchemaModifiedOn"></a> SchemaModifiedOn

|Property|Value|
|---|---|
|Description|**Schema modified on date-time**|
|DisplayName|**Schema Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`schemamodifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Synapse Link External Table State**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`synapselinkexternaltablestate_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Synapse Link External Table State**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`synapselinkexternaltablestate_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_SynapseDatabaseName"></a> SynapseDatabaseName

|Property|Value|
|---|---|
|Description|**Synapse database name**|
|DisplayName|**Synapse Database Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`synapsedatabasename`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_synapselinkexternaltablestateId"></a> synapselinkexternaltablestateId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Synapse Link External Table State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`synapselinkexternaltablestateid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SynapseWorkspaceName"></a> SynapseWorkspaceName

|Property|Value|
|---|---|
|Description|**Synapse workspace name**|
|DisplayName|**Synapse Workspace Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`synapseworkspacename`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_TableState"></a> TableState

|Property|Value|
|---|---|
|Description|**External table state**|
|DisplayName|**Table State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`tablestate`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`synapselinkexternaltablestate`|

#### TableState Choices/Options

|Value|Label|
|---|---|
|0|**Not Created**|
|1|**Created**|
|2|**Failed**|
|3|**Deleted**|
|4|**In Progress**|

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

### <a name="BKMK_TrinoState"></a> TrinoState

|Property|Value|
|---|---|
|Description|**State of Trino registration for an entity**|
|DisplayName|**Trino State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`trinostate`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`synapselinkexternaltablestate`|

#### TrinoState Choices/Options

|Value|Label|
|---|---|
|0|**Not Created**|
|1|**Created**|
|2|**Failed**|
|3|**Deleted**|
|4|**In Progress**|

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

- [lk_synapselinkexternaltablestate_createdby](#BKMK_lk_synapselinkexternaltablestate_createdby)
- [lk_synapselinkexternaltablestate_createdonbehalfby](#BKMK_lk_synapselinkexternaltablestate_createdonbehalfby)
- [lk_synapselinkexternaltablestate_modifiedby](#BKMK_lk_synapselinkexternaltablestate_modifiedby)
- [lk_synapselinkexternaltablestate_modifiedonbehalfby](#BKMK_lk_synapselinkexternaltablestate_modifiedonbehalfby)
- [organization_synapselinkexternaltablestate](#BKMK_organization_synapselinkexternaltablestate)
- [synapselinkexternaltablestates](#BKMK_synapselinkexternaltablestates)

### <a name="BKMK_lk_synapselinkexternaltablestate_createdby"></a> lk_synapselinkexternaltablestate_createdby

One-To-Many Relationship: [systemuser lk_synapselinkexternaltablestate_createdby](systemuser.md#BKMK_lk_synapselinkexternaltablestate_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_synapselinkexternaltablestate_createdonbehalfby"></a> lk_synapselinkexternaltablestate_createdonbehalfby

One-To-Many Relationship: [systemuser lk_synapselinkexternaltablestate_createdonbehalfby](systemuser.md#BKMK_lk_synapselinkexternaltablestate_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_synapselinkexternaltablestate_modifiedby"></a> lk_synapselinkexternaltablestate_modifiedby

One-To-Many Relationship: [systemuser lk_synapselinkexternaltablestate_modifiedby](systemuser.md#BKMK_lk_synapselinkexternaltablestate_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_synapselinkexternaltablestate_modifiedonbehalfby"></a> lk_synapselinkexternaltablestate_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_synapselinkexternaltablestate_modifiedonbehalfby](systemuser.md#BKMK_lk_synapselinkexternaltablestate_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_synapselinkexternaltablestate"></a> organization_synapselinkexternaltablestate

One-To-Many Relationship: [organization organization_synapselinkexternaltablestate](organization.md#BKMK_organization_synapselinkexternaltablestate)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkexternaltablestates"></a> synapselinkexternaltablestates

One-To-Many Relationship: [datalakefolder synapselinkexternaltablestates](datalakefolder.md#BKMK_synapselinkexternaltablestates)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakefolder`|
|ReferencedAttribute|`datalakefolderid`|
|ReferencingAttribute|`datalakefolder`|
|ReferencingEntityNavigationPropertyName|`datalakefolder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [synapselinkexternaltablestate_AsyncOperations](#BKMK_synapselinkexternaltablestate_AsyncOperations)
- [synapselinkexternaltablestate_BulkDeleteFailures](#BKMK_synapselinkexternaltablestate_BulkDeleteFailures)
- [synapselinkexternaltablestate_DuplicateBaseRecord](#BKMK_synapselinkexternaltablestate_DuplicateBaseRecord)
- [synapselinkexternaltablestate_DuplicateMatchingRecord](#BKMK_synapselinkexternaltablestate_DuplicateMatchingRecord)
- [synapselinkexternaltablestate_MailboxTrackingFolders](#BKMK_synapselinkexternaltablestate_MailboxTrackingFolders)
- [synapselinkexternaltablestate_PrincipalObjectAttributeAccesses](#BKMK_synapselinkexternaltablestate_PrincipalObjectAttributeAccesses)
- [synapselinkexternaltablestate_ProcessSession](#BKMK_synapselinkexternaltablestate_ProcessSession)
- [synapselinkexternaltablestate_SyncErrors](#BKMK_synapselinkexternaltablestate_SyncErrors)

### <a name="BKMK_synapselinkexternaltablestate_AsyncOperations"></a> synapselinkexternaltablestate_AsyncOperations

Many-To-One Relationship: [asyncoperation synapselinkexternaltablestate_AsyncOperations](asyncoperation.md#BKMK_synapselinkexternaltablestate_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkexternaltablestate_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkexternaltablestate_BulkDeleteFailures"></a> synapselinkexternaltablestate_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure synapselinkexternaltablestate_BulkDeleteFailures](bulkdeletefailure.md#BKMK_synapselinkexternaltablestate_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkexternaltablestate_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkexternaltablestate_DuplicateBaseRecord"></a> synapselinkexternaltablestate_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord synapselinkexternaltablestate_DuplicateBaseRecord](duplicaterecord.md#BKMK_synapselinkexternaltablestate_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`synapselinkexternaltablestate_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkexternaltablestate_DuplicateMatchingRecord"></a> synapselinkexternaltablestate_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord synapselinkexternaltablestate_DuplicateMatchingRecord](duplicaterecord.md#BKMK_synapselinkexternaltablestate_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`synapselinkexternaltablestate_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkexternaltablestate_MailboxTrackingFolders"></a> synapselinkexternaltablestate_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder synapselinkexternaltablestate_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_synapselinkexternaltablestate_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkexternaltablestate_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkexternaltablestate_PrincipalObjectAttributeAccesses"></a> synapselinkexternaltablestate_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess synapselinkexternaltablestate_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_synapselinkexternaltablestate_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkexternaltablestate_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkexternaltablestate_ProcessSession"></a> synapselinkexternaltablestate_ProcessSession

Many-To-One Relationship: [processsession synapselinkexternaltablestate_ProcessSession](processsession.md#BKMK_synapselinkexternaltablestate_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkexternaltablestate_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkexternaltablestate_SyncErrors"></a> synapselinkexternaltablestate_SyncErrors

Many-To-One Relationship: [syncerror synapselinkexternaltablestate_SyncErrors](syncerror.md#BKMK_synapselinkexternaltablestate_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkexternaltablestate_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.synapselinkexternaltablestate?displayProperty=fullName>
