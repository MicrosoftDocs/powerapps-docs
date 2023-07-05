---
title: "synapselinkexternaltablestate table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the synapselinkexternaltablestate table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# synapselinkexternaltablestate table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Synapse Link external table states

**Added by**: Synapse Link Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST /synapselinkexternaltablestates<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /synapselinkexternaltablestates(*synapselinkexternaltablestateid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|Retrieve|GET /synapselinkexternaltablestates(*synapselinkexternaltablestateid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /synapselinkexternaltablestates<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|SetState|PATCH /synapselinkexternaltablestates(*synapselinkexternaltablestateid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /synapselinkexternaltablestates(*synapselinkexternaltablestateid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|synapselinkexternaltablestates|
|DisplayCollectionName|Synapse Link External Table States|
|DisplayName|Synapse Link External Table State|
|EntitySetName|synapselinkexternaltablestates|
|IsBPFEntity|False|
|LogicalCollectionName|synapselinkexternaltablestates|
|LogicalName|synapselinkexternaltablestate|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|synapselinkexternaltablestateid|
|PrimaryNameAttribute|name|
|SchemaName|synapselinkexternaltablestate|

<a name="writable-attributes"></a>

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
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_datalakefolder"></a> datalakefolder

|Property|Value|
|--------|-----|
|Description|Unique identifier for Data Lake Folder associated with Synapse Link External Table State.|
|DisplayName|Data Lake Folder|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|datalakefolder|
|RequiredLevel|ApplicationRequired|
|Targets|datalakefolder|
|Type|Lookup|


### <a name="BKMK_EntityName"></a> EntityName

|Property|Value|
|--------|-----|
|Description|Name of the entity|
|DisplayName|Entity Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|entityname|
|MaxLength|64|
|RequiredLevel|ApplicationRequired|
|Type|String|


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


### <a name="BKMK_LakehouseShortcutState"></a> LakehouseShortcutState

|Property|Value|
|--------|-----|
|Description|State of lakehouse shortcut creation for an entity|
|DisplayName|Lakehouse Shortcut State|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lakehouseshortcutstate|
|RequiredLevel|None|
|Type|Picklist|

#### LakehouseShortcutState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Not Created|Not created|
|1|Created|Created|
|2|Failed|Failed|
|3|Deleted|Deleted|



### <a name="BKMK_LastSynchronizedOn"></a> LastSynchronizedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Last SynchronizedOn Date time|
|DisplayName|Last Synchronized On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastsynchronizedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_LastSyncState"></a> LastSyncState

|Property|Value|
|--------|-----|
|Description|Last data synchronization state|
|DisplayName|Last Synchronization State|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastsyncstate|
|RequiredLevel|None|
|Type|Picklist|

#### LastSyncState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Not Created|Not created|
|1|Created|Created|
|2|Failed|Failed|
|3|Deleted|Deleted|



### <a name="BKMK_MaxRecordVersion"></a> MaxRecordVersion

|Property|Value|
|--------|-----|
|Description|Maximum record version synchronized to the lake|
|DisplayName|Maximum Record Version|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|maxrecordversion|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|


### <a name="BKMK_MetadataVersion"></a> MetadataVersion

|Property|Value|
|--------|-----|
|Description|Metadata version|
|DisplayName|Metadata Version|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|metadataversion|
|MaxLength|32|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_name"></a> name

|Property|Value|
|--------|-----|
|Description|The name of the custom entity.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


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


### <a name="BKMK_RecordCount"></a> RecordCount

|Property|Value|
|--------|-----|
|Description|Record count synchronized to lake|
|DisplayName|Record Count|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|recordcount|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|


### <a name="BKMK_SchemaModifiedOn"></a> SchemaModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Schema modified on date-time|
|DisplayName|Schema Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|schemamodifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Synapse Link External Table State|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### statecode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|1|Active|
|1|Inactive|2|Inactive|



### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the Synapse Link External Table State|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### statuscode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Active|0|
|2|Inactive|1|



### <a name="BKMK_SynapseDatabaseName"></a> SynapseDatabaseName

|Property|Value|
|--------|-----|
|Description|Synapse database name|
|DisplayName|Synapse Database Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|synapsedatabasename|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_synapselinkexternaltablestateId"></a> synapselinkexternaltablestateId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Synapse Link External Table State|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|synapselinkexternaltablestateid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SynapseWorkspaceName"></a> SynapseWorkspaceName

|Property|Value|
|--------|-----|
|Description|Synapse workspace name|
|DisplayName|Synapse Workspace Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|synapseworkspacename|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_TableState"></a> TableState

|Property|Value|
|--------|-----|
|Description|External table state|
|DisplayName|Table State|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|tablestate|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### TableState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Not Created|Not created|
|1|Created|Created|
|2|Failed|Failed|
|3|Deleted|Deleted|



### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Time Zone Rule Version Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezoneruleversionnumber|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|--------|-----|
|Description|Time zone code that was in use when the record was created.|
|DisplayName|UTC Conversion Time Zone Code|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|utcconversiontimezonecode|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [datalakefolderName](#BKMK_datalakefolderName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [VersionNumber](#BKMK_VersionNumber)


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


### <a name="BKMK_datalakefolderName"></a> datalakefolderName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|datalakefoldername|
|MaxLength|100|
|RequiredLevel|None|
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


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the organization|
|DisplayName|Organization Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|None|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
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

- [synapselinkexternaltablestate_SyncErrors](#BKMK_synapselinkexternaltablestate_SyncErrors)
- [synapselinkexternaltablestate_DuplicateMatchingRecord](#BKMK_synapselinkexternaltablestate_DuplicateMatchingRecord)
- [synapselinkexternaltablestate_DuplicateBaseRecord](#BKMK_synapselinkexternaltablestate_DuplicateBaseRecord)
- [synapselinkexternaltablestate_AsyncOperations](#BKMK_synapselinkexternaltablestate_AsyncOperations)
- [synapselinkexternaltablestate_MailboxTrackingFolders](#BKMK_synapselinkexternaltablestate_MailboxTrackingFolders)
- [synapselinkexternaltablestate_ProcessSession](#BKMK_synapselinkexternaltablestate_ProcessSession)
- [synapselinkexternaltablestate_BulkDeleteFailures](#BKMK_synapselinkexternaltablestate_BulkDeleteFailures)
- [synapselinkexternaltablestate_PrincipalObjectAttributeAccesses](#BKMK_synapselinkexternaltablestate_PrincipalObjectAttributeAccesses)


### <a name="BKMK_synapselinkexternaltablestate_SyncErrors"></a> synapselinkexternaltablestate_SyncErrors

**Added by**: System Solution Solution

Same as the [synapselinkexternaltablestate_SyncErrors](syncerror.md#BKMK_synapselinkexternaltablestate_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkexternaltablestate_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkexternaltablestate_DuplicateMatchingRecord"></a> synapselinkexternaltablestate_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as the [synapselinkexternaltablestate_DuplicateMatchingRecord](duplicaterecord.md#BKMK_synapselinkexternaltablestate_DuplicateMatchingRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkexternaltablestate_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkexternaltablestate_DuplicateBaseRecord"></a> synapselinkexternaltablestate_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as the [synapselinkexternaltablestate_DuplicateBaseRecord](duplicaterecord.md#BKMK_synapselinkexternaltablestate_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkexternaltablestate_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkexternaltablestate_AsyncOperations"></a> synapselinkexternaltablestate_AsyncOperations

**Added by**: System Solution Solution

Same as the [synapselinkexternaltablestate_AsyncOperations](asyncoperation.md#BKMK_synapselinkexternaltablestate_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkexternaltablestate_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkexternaltablestate_MailboxTrackingFolders"></a> synapselinkexternaltablestate_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [synapselinkexternaltablestate_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_synapselinkexternaltablestate_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkexternaltablestate_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkexternaltablestate_ProcessSession"></a> synapselinkexternaltablestate_ProcessSession

**Added by**: System Solution Solution

Same as the [synapselinkexternaltablestate_ProcessSession](processsession.md#BKMK_synapselinkexternaltablestate_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkexternaltablestate_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkexternaltablestate_BulkDeleteFailures"></a> synapselinkexternaltablestate_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [synapselinkexternaltablestate_BulkDeleteFailures](bulkdeletefailure.md#BKMK_synapselinkexternaltablestate_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkexternaltablestate_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkexternaltablestate_PrincipalObjectAttributeAccesses"></a> synapselinkexternaltablestate_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [synapselinkexternaltablestate_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_synapselinkexternaltablestate_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkexternaltablestate_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_synapselinkexternaltablestate_createdby](#BKMK_lk_synapselinkexternaltablestate_createdby)
- [lk_synapselinkexternaltablestate_createdonbehalfby](#BKMK_lk_synapselinkexternaltablestate_createdonbehalfby)
- [lk_synapselinkexternaltablestate_modifiedby](#BKMK_lk_synapselinkexternaltablestate_modifiedby)
- [lk_synapselinkexternaltablestate_modifiedonbehalfby](#BKMK_lk_synapselinkexternaltablestate_modifiedonbehalfby)
- [organization_synapselinkexternaltablestate](#BKMK_organization_synapselinkexternaltablestate)
- [synapselinkexternaltablestates](#BKMK_synapselinkexternaltablestates)


### <a name="BKMK_lk_synapselinkexternaltablestate_createdby"></a> lk_synapselinkexternaltablestate_createdby

**Added by**: System Solution Solution

See the [lk_synapselinkexternaltablestate_createdby](systemuser.md#BKMK_lk_synapselinkexternaltablestate_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_synapselinkexternaltablestate_createdonbehalfby"></a> lk_synapselinkexternaltablestate_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_synapselinkexternaltablestate_createdonbehalfby](systemuser.md#BKMK_lk_synapselinkexternaltablestate_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_synapselinkexternaltablestate_modifiedby"></a> lk_synapselinkexternaltablestate_modifiedby

**Added by**: System Solution Solution

See the [lk_synapselinkexternaltablestate_modifiedby](systemuser.md#BKMK_lk_synapselinkexternaltablestate_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_synapselinkexternaltablestate_modifiedonbehalfby"></a> lk_synapselinkexternaltablestate_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_synapselinkexternaltablestate_modifiedonbehalfby](systemuser.md#BKMK_lk_synapselinkexternaltablestate_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_organization_synapselinkexternaltablestate"></a> organization_synapselinkexternaltablestate

**Added by**: System Solution Solution

See the [organization_synapselinkexternaltablestate](organization.md#BKMK_organization_synapselinkexternaltablestate) one-to-many relationship for the [organization](organization.md) table/entity.

### <a name="BKMK_synapselinkexternaltablestates"></a> synapselinkexternaltablestates

**Added by**: Data lake workspaces Solution

See the [synapselinkexternaltablestates](datalakefolder.md#BKMK_synapselinkexternaltablestates) one-to-many relationship for the [datalakefolder](datalakefolder.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.synapselinkexternaltablestate?text=synapselinkexternaltablestate EntityType" />