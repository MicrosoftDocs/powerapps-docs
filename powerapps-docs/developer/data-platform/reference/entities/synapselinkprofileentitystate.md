---
title: "synapselinkprofileentitystate table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the synapselinkprofileentitystate table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# synapselinkprofileentitystate table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Runtime state of the Synapse Link entity

**Added by**: Synapse Link Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST /synapselinkprofileentitystates<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /synapselinkprofileentitystates(*synapselinkprofileentitystateid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|Retrieve|GET /synapselinkprofileentitystates(*synapselinkprofileentitystateid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /synapselinkprofileentitystates<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|SetState|PATCH /synapselinkprofileentitystates(*synapselinkprofileentitystateid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /synapselinkprofileentitystates(*synapselinkprofileentitystateid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|synapselinkprofileentitystates|
|DisplayCollectionName|Synapse Link Profile Entity States|
|DisplayName|Synapse Link Profile Entity State|
|EntitySetName|synapselinkprofileentitystates|
|IsBPFEntity|False|
|LogicalCollectionName|synapselinkprofileentitystates|
|LogicalName|synapselinkprofileentitystate|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|synapselinkprofileentitystateid|
|PrimaryNameAttribute|name|
|SchemaName|synapselinkprofileentitystate|

<a name="writable-attributes"></a>

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
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Addition time of entity|
|DisplayName|Addition Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|additiontime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CrmRecordCount"></a> CrmRecordCount

|Property|Value|
|--------|-----|
|Description|CRM record count|
|DisplayName|CRM Record Count|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|crmrecordcount|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|


### <a name="BKMK_CrmRecordCountModifiedTime"></a> CrmRecordCountModifiedTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|CRM record count modified time for entity|
|DisplayName|CRM Record Count Modified Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|crmrecordcountmodifiedtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_EntityName"></a> EntityName

|Property|Value|
|--------|-----|
|Description|Name of the entity|
|DisplayName|EntityName|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|entityname|
|MaxLength|64|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_EntitySource"></a> EntitySource

|Property|Value|
|--------|-----|
|Description|Source of the entity|
|DisplayName|Entity source|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|entitysource|
|RequiredLevel|None|
|Type|Picklist|

#### EntitySource Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Dataverse|Dataverse|
|1|FnOTables|FnOTables|



### <a name="BKMK_EntityType"></a> EntityType

|Property|Value|
|--------|-----|
|Description|Type of the entity|
|DisplayName|EntityType|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|entitytype|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### EntityType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Requested|Requested|



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


### <a name="BKMK_InitialSyncDataCompletedTime"></a> InitialSyncDataCompletedTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Initial sync data completed time|
|DisplayName|Initial Sync Data Completed Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|initialsyncdatacompletedtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_InitialSyncMetadataCreatedTime"></a> InitialSyncMetadataCreatedTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Initial sync metadata created time|
|DisplayName|Initial Sync Metadata Created Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|initialsyncmetadatacreatedtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_InitialSyncProcessCompletedTime"></a> InitialSyncProcessCompletedTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Initial sync process completed time|
|DisplayName|Initial Sync Process Completed Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|initialsyncprocesscompletedtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_InitialSyncState"></a> InitialSyncState

|Property|Value|
|--------|-----|
|Description|Initial sync state|
|DisplayName|Initial Sync State|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|initialsyncstate|
|RequiredLevel|None|
|Type|Picklist|

#### InitialSyncState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|None|None|
|1|NotStarted|Not started|
|2|InProgress|In progress|
|4|Completed|Completed|
|8|CompletedWithFailures|Completed with failures|
|16|RequestedInitialData|Requested initial data|
|32|Paused|Paused|
|64|PostProcessing|Post processing|



### <a name="BKMK_LakeRecordCount"></a> LakeRecordCount

|Property|Value|
|--------|-----|
|Description|Lake record count|
|DisplayName|Lake Record Count|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|lakerecordcount|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|


### <a name="BKMK_LakeRecordCountModifiedTime"></a> LakeRecordCountModifiedTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Lake record count modified time for entity|
|DisplayName|Lake Record Count Modified Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lakerecordcountmodifiedtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_LastSyncedDataTime"></a> LastSyncedDataTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Last synced data time|
|DisplayName|Last Synced Data Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastsynceddatatime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_LastSyncedDataVersion"></a> LastSyncedDataVersion

|Property|Value|
|--------|-----|
|Description|Last synced data version|
|DisplayName|Last Synced Data Version|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastsynceddataversion|
|MaxLength|32|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_LastSyncedMetadataTime"></a> LastSyncedMetadataTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Last synced metadata time|
|DisplayName|Last Synced Metadata Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastsyncedmetadatatime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_LastSyncedMetadataVersion"></a> LastSyncedMetadataVersion

|Property|Value|
|--------|-----|
|Description|Last synced metadata version|
|DisplayName|Last Synced Metadata Version|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastsyncedmetadataversion|
|MaxLength|32|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_MetadataState"></a> MetadataState

|Property|Value|
|--------|-----|
|Description|Metadata state|
|DisplayName|Metadata State|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|metadatastate|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### MetadataState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|None|None state for flag enumeration. Not a valid state for usage|
|1|NotCreated|Not created|
|2|MetadataCreating|Metadata creating|
|4|RelationshipCreating|Relationship creating|
|8|Created|Created|
|16|Failure|Failure|



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


### <a name="BKMK_profile"></a> profile

|Property|Value|
|--------|-----|
|Description|Unique identifier for Synapse Link Profile associated with Synapse Link Profile Entity State.|
|DisplayName|Profile|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|profile|
|RequiredLevel|ApplicationRequired|
|Targets|synapselinkprofile|
|Type|Lookup|


### <a name="BKMK_profileentity"></a> profileentity

|Property|Value|
|--------|-----|
|Description|Unique identifier for Synapse Link Profile Entity associated with Synapse Link Profile Entity State.|
|DisplayName|ProfileEntity|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|profileentity|
|RequiredLevel|SystemRequired|
|Targets|synapselinkprofileentity|
|Type|Lookup|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Synapse Link Profile Entity State|
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
|Description|Reason for the status of the Synapse Link Profile Entity State|
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



### <a name="BKMK_synapselinkprofileentitystateId"></a> synapselinkprofileentitystateId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Synapse Link Profile Entity State|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|synapselinkprofileentitystateid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SynapseTableCreationState"></a> SynapseTableCreationState

|Property|Value|
|--------|-----|
|Description|Synapse table creation state|
|DisplayName|Synapse Table Creation State|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|synapsetablecreationstate|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### SynapseTableCreationState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|NotStarted|Not started|
|1|InProgress|In progress|
|2|Completed|Completed|
|3|Failed|Failed|



### <a name="BKMK_SyncState"></a> SyncState

|Property|Value|
|--------|-----|
|Description|Entity sync state|
|DisplayName|SyncState|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|syncstate|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### SyncState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|None|None|
|1|NotStarted|Not started|
|2|InProgress|In progress|
|4|Completed|Completed|
|8|CompletedWithFailures|Completed with failures|
|16|RequestedInitialData|Requested initial data|
|32|Paused|Paused|
|64|PostProcessing|Post processing|



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
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [profileentityName](#BKMK_profileentityName)
- [profileName](#BKMK_profileName)
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


### <a name="BKMK_profileentityName"></a> profileentityName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|profileentityname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_profileName"></a> profileName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|profilename|
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

- [synapselinkprofileentitystate_SyncErrors](#BKMK_synapselinkprofileentitystate_SyncErrors)
- [synapselinkprofileentitystate_DuplicateMatchingRecord](#BKMK_synapselinkprofileentitystate_DuplicateMatchingRecord)
- [synapselinkprofileentitystate_DuplicateBaseRecord](#BKMK_synapselinkprofileentitystate_DuplicateBaseRecord)
- [synapselinkprofileentitystate_AsyncOperations](#BKMK_synapselinkprofileentitystate_AsyncOperations)
- [synapselinkprofileentitystate_MailboxTrackingFolders](#BKMK_synapselinkprofileentitystate_MailboxTrackingFolders)
- [synapselinkprofileentitystate_ProcessSession](#BKMK_synapselinkprofileentitystate_ProcessSession)
- [synapselinkprofileentitystate_BulkDeleteFailures](#BKMK_synapselinkprofileentitystate_BulkDeleteFailures)
- [synapselinkprofileentitystate_PrincipalObjectAttributeAccesses](#BKMK_synapselinkprofileentitystate_PrincipalObjectAttributeAccesses)


### <a name="BKMK_synapselinkprofileentitystate_SyncErrors"></a> synapselinkprofileentitystate_SyncErrors

**Added by**: System Solution Solution

Same as the [synapselinkprofileentitystate_SyncErrors](syncerror.md#BKMK_synapselinkprofileentitystate_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkprofileentitystate_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkprofileentitystate_DuplicateMatchingRecord"></a> synapselinkprofileentitystate_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as the [synapselinkprofileentitystate_DuplicateMatchingRecord](duplicaterecord.md#BKMK_synapselinkprofileentitystate_DuplicateMatchingRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkprofileentitystate_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkprofileentitystate_DuplicateBaseRecord"></a> synapselinkprofileentitystate_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as the [synapselinkprofileentitystate_DuplicateBaseRecord](duplicaterecord.md#BKMK_synapselinkprofileentitystate_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkprofileentitystate_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkprofileentitystate_AsyncOperations"></a> synapselinkprofileentitystate_AsyncOperations

**Added by**: System Solution Solution

Same as the [synapselinkprofileentitystate_AsyncOperations](asyncoperation.md#BKMK_synapselinkprofileentitystate_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkprofileentitystate_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkprofileentitystate_MailboxTrackingFolders"></a> synapselinkprofileentitystate_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [synapselinkprofileentitystate_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_synapselinkprofileentitystate_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkprofileentitystate_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkprofileentitystate_ProcessSession"></a> synapselinkprofileentitystate_ProcessSession

**Added by**: System Solution Solution

Same as the [synapselinkprofileentitystate_ProcessSession](processsession.md#BKMK_synapselinkprofileentitystate_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkprofileentitystate_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkprofileentitystate_BulkDeleteFailures"></a> synapselinkprofileentitystate_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [synapselinkprofileentitystate_BulkDeleteFailures](bulkdeletefailure.md#BKMK_synapselinkprofileentitystate_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkprofileentitystate_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkprofileentitystate_PrincipalObjectAttributeAccesses"></a> synapselinkprofileentitystate_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [synapselinkprofileentitystate_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_synapselinkprofileentitystate_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkprofileentitystate_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_synapselinkprofileentitystate_createdby](#BKMK_lk_synapselinkprofileentitystate_createdby)
- [lk_synapselinkprofileentitystate_createdonbehalfby](#BKMK_lk_synapselinkprofileentitystate_createdonbehalfby)
- [lk_synapselinkprofileentitystate_modifiedby](#BKMK_lk_synapselinkprofileentitystate_modifiedby)
- [lk_synapselinkprofileentitystate_modifiedonbehalfby](#BKMK_lk_synapselinkprofileentitystate_modifiedonbehalfby)
- [organization_synapselinkprofileentitystate](#BKMK_organization_synapselinkprofileentitystate)
- [entitystate](#BKMK_entitystate)
- [profileentitystates](#BKMK_profileentitystates)


### <a name="BKMK_lk_synapselinkprofileentitystate_createdby"></a> lk_synapselinkprofileentitystate_createdby

**Added by**: System Solution Solution

See the [lk_synapselinkprofileentitystate_createdby](systemuser.md#BKMK_lk_synapselinkprofileentitystate_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_synapselinkprofileentitystate_createdonbehalfby"></a> lk_synapselinkprofileentitystate_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_synapselinkprofileentitystate_createdonbehalfby](systemuser.md#BKMK_lk_synapselinkprofileentitystate_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_synapselinkprofileentitystate_modifiedby"></a> lk_synapselinkprofileentitystate_modifiedby

**Added by**: System Solution Solution

See the [lk_synapselinkprofileentitystate_modifiedby](systemuser.md#BKMK_lk_synapselinkprofileentitystate_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_synapselinkprofileentitystate_modifiedonbehalfby"></a> lk_synapselinkprofileentitystate_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_synapselinkprofileentitystate_modifiedonbehalfby](systemuser.md#BKMK_lk_synapselinkprofileentitystate_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_organization_synapselinkprofileentitystate"></a> organization_synapselinkprofileentitystate

**Added by**: System Solution Solution

See the [organization_synapselinkprofileentitystate](organization.md#BKMK_organization_synapselinkprofileentitystate) one-to-many relationship for the [organization](organization.md) table/entity.

### <a name="BKMK_entitystate"></a> entitystate

See the [entitystate](synapselinkprofileentity.md#BKMK_entitystate) one-to-many relationship for the [synapselinkprofileentity](synapselinkprofileentity.md) table/entity.

### <a name="BKMK_profileentitystates"></a> profileentitystates

See the [profileentitystates](synapselinkprofile.md#BKMK_profileentitystates) one-to-many relationship for the [synapselinkprofile](synapselinkprofile.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.synapselinkprofileentitystate?text=synapselinkprofileentitystate EntityType" />