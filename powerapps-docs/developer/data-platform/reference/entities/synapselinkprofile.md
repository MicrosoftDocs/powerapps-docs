---
title: "synapselinkprofile table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the synapselinkprofile table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# synapselinkprofile table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Synapse Link Profile

**Added by**: Synapse Link Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST /synapselinkprofiles<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /synapselinkprofiles(*synapselinkprofileid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|Retrieve|GET /synapselinkprofiles(*synapselinkprofileid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /synapselinkprofiles<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|SetState|PATCH /synapselinkprofiles(*synapselinkprofileid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /synapselinkprofiles(*synapselinkprofileid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|synapselinkprofiles|
|DisplayCollectionName|Synapse Link Profiles|
|DisplayName|Synapse Link Profile|
|EntitySetName|synapselinkprofiles|
|IsBPFEntity|False|
|LogicalCollectionName|synapselinkprofiles|
|LogicalName|synapselinkprofile|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|synapselinkprofileid|
|PrimaryNameAttribute|name|
|SchemaName|synapselinkprofile|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ActivationTime](#BKMK_ActivationTime)
- [CopyAttachments](#BKMK_CopyAttachments)
- [CopyFiles](#BKMK_CopyFiles)
- [datalakefolder](#BKMK_datalakefolder)
- [DestinationSyncState](#BKMK_DestinationSyncState)
- [ExtendedProperties](#BKMK_ExtendedProperties)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [name](#BKMK_name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [ProfileState](#BKMK_ProfileState)
- [ProfileType](#BKMK_ProfileType)
- [ProfileUpdatedTime](#BKMK_ProfileUpdatedTime)
- [ProfileVersion](#BKMK_ProfileVersion)
- [SnapshotsToPersist](#BKMK_SnapshotsToPersist)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [synapselinkprofileId](#BKMK_synapselinkprofileId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UniqueName](#BKMK_UniqueName)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_ActivationTime"></a> ActivationTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Activation time of profile|
|DisplayName|Activation Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|activationtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CopyAttachments"></a> CopyAttachments

|Property|Value|
|--------|-----|
|Description|Enable Copy Attachments|
|DisplayName|Copy Attachments|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|copyattachments|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|

#### CopyAttachments Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_CopyFiles"></a> CopyFiles

|Property|Value|
|--------|-----|
|Description|Enable Copy Files|
|DisplayName|Copy Files|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|copyfiles|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|

#### CopyFiles Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_datalakefolder"></a> datalakefolder

|Property|Value|
|--------|-----|
|Description|Unique identifier for Data Lake Folder associated with Synapse Link Profile.|
|DisplayName|Data Lake Folder|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|datalakefolder|
|RequiredLevel|ApplicationRequired|
|Targets|datalakefolder|
|Type|Lookup|


### <a name="BKMK_DestinationSyncState"></a> DestinationSyncState

|Property|Value|
|--------|-----|
|Description|Sync state of the profile|
|DisplayName|Destination Sync State|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|destinationsyncstate|
|RequiredLevel|None|
|Type|Picklist|

#### DestinationSyncState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|None|None|
|1|NotCompleted|Not Completed|
|2|Completed|Completed|



### <a name="BKMK_ExtendedProperties"></a> ExtendedProperties

|Property|Value|
|--------|-----|
|Description|Extended properties|
|DisplayName|Extended Properties|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|extendedproperties|
|MaxLength|4000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

**Added by**: Basic Solution Solution

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


### <a name="BKMK_IsCustomizable"></a> IsCustomizable

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Is Customizable|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iscustomizable|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


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


### <a name="BKMK_ProfileState"></a> ProfileState

|Property|Value|
|--------|-----|
|Description|State of the profile|
|DisplayName|Profile State|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|profilestate|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### ProfileState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Inactive|Inactive|
|1|Active|Active|
|2|Error|Error|
|3|Deleted|Deleted|
|4|Aborting|Aborting|
|5|Aborted|Aborted|
|6|Suspended|Suspended|
|7|Suspending|Suspending|
|8|Deactivated|Deactivated|



### <a name="BKMK_ProfileType"></a> ProfileType

|Property|Value|
|--------|-----|
|Description|Type of profile|
|DisplayName|Profile Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|profiletype|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### ProfileType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|SynapseLink|Synapse Link profile|
|1|EventAnalytics|Event Analytics profile|



### <a name="BKMK_ProfileUpdatedTime"></a> ProfileUpdatedTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Profile Updated Time|
|DisplayName|Profile Updated Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|profileupdatedtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ProfileVersion"></a> ProfileVersion

|Property|Value|
|--------|-----|
|Description|Profile version|
|DisplayName|Profile Version|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|profileversion|
|MaxLength|32|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_SnapshotsToPersist"></a> SnapshotsToPersist

|Property|Value|
|--------|-----|
|Description|Number of snapshots To persist|
|DisplayName|Snapshots To Persist|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|snapshotstopersist|
|MaxValue|100|
|MinValue|0|
|RequiredLevel|ApplicationRequired|
|Type|Integer|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Synapse Link Profile|
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
|Description|Reason for the status of the Synapse Link Profile|
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



### <a name="BKMK_synapselinkprofileId"></a> synapselinkprofileId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Synapse Link Profile|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|synapselinkprofileid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


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


### <a name="BKMK_UniqueName"></a> UniqueName

|Property|Value|
|--------|-----|
|Description|Unique name|
|DisplayName|Unique Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|uniquename|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


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

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [datalakefolderName](#BKMK_datalakefolderName)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ComponentIdUnique"></a> ComponentIdUnique

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Row id unique|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ComponentState"></a> ComponentState

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Component State|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentstate|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ComponentState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Published||
|1|Unpublished||
|2|Deleted||
|3|Deleted Unpublished||



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


### <a name="BKMK_IsManaged"></a> IsManaged

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|Indicates whether the solution component is part of a managed solution.|
|DisplayName|Is Managed|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsManaged Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Managed||
|0|Unmanaged||

**DefaultValue**: 0



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


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Record Overwrite Time|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overwritetime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_SolutionId"></a> SolutionId

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the associated solution.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|solutionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|supportingsolutionid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


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

- [synapselinkprofile_SyncErrors](#BKMK_synapselinkprofile_SyncErrors)
- [synapselinkprofile_DuplicateMatchingRecord](#BKMK_synapselinkprofile_DuplicateMatchingRecord)
- [synapselinkprofile_DuplicateBaseRecord](#BKMK_synapselinkprofile_DuplicateBaseRecord)
- [synapselinkprofile_AsyncOperations](#BKMK_synapselinkprofile_AsyncOperations)
- [synapselinkprofile_MailboxTrackingFolders](#BKMK_synapselinkprofile_MailboxTrackingFolders)
- [synapselinkprofile_ProcessSession](#BKMK_synapselinkprofile_ProcessSession)
- [synapselinkprofile_BulkDeleteFailures](#BKMK_synapselinkprofile_BulkDeleteFailures)
- [synapselinkprofile_PrincipalObjectAttributeAccesses](#BKMK_synapselinkprofile_PrincipalObjectAttributeAccesses)
- [profileentities](#BKMK_profileentities)
- [profileentitystates](#BKMK_profileentitystates)
- [profileschedules](#BKMK_profileschedules)


### <a name="BKMK_synapselinkprofile_SyncErrors"></a> synapselinkprofile_SyncErrors

**Added by**: System Solution Solution

Same as the [synapselinkprofile_SyncErrors](syncerror.md#BKMK_synapselinkprofile_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkprofile_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkprofile_DuplicateMatchingRecord"></a> synapselinkprofile_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as the [synapselinkprofile_DuplicateMatchingRecord](duplicaterecord.md#BKMK_synapselinkprofile_DuplicateMatchingRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkprofile_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkprofile_DuplicateBaseRecord"></a> synapselinkprofile_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as the [synapselinkprofile_DuplicateBaseRecord](duplicaterecord.md#BKMK_synapselinkprofile_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkprofile_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkprofile_AsyncOperations"></a> synapselinkprofile_AsyncOperations

**Added by**: System Solution Solution

Same as the [synapselinkprofile_AsyncOperations](asyncoperation.md#BKMK_synapselinkprofile_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkprofile_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkprofile_MailboxTrackingFolders"></a> synapselinkprofile_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [synapselinkprofile_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_synapselinkprofile_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkprofile_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkprofile_ProcessSession"></a> synapselinkprofile_ProcessSession

**Added by**: System Solution Solution

Same as the [synapselinkprofile_ProcessSession](processsession.md#BKMK_synapselinkprofile_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkprofile_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkprofile_BulkDeleteFailures"></a> synapselinkprofile_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [synapselinkprofile_BulkDeleteFailures](bulkdeletefailure.md#BKMK_synapselinkprofile_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkprofile_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkprofile_PrincipalObjectAttributeAccesses"></a> synapselinkprofile_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [synapselinkprofile_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_synapselinkprofile_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapselinkprofile_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_profileentities"></a> profileentities

Same as the [profileentities](synapselinkprofileentity.md#BKMK_profileentities) many-to-one relationship for the [synapselinkprofileentity](synapselinkprofileentity.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|synapselinkprofileentity|
|ReferencingAttribute|profile|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|profileentities|
|AssociatedMenuConfiguration|Behavior: UseLabel<br />Group: Details<br />Label: Profile<br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_profileentitystates"></a> profileentitystates

Same as the [profileentitystates](synapselinkprofileentitystate.md#BKMK_profileentitystates) many-to-one relationship for the [synapselinkprofileentitystate](synapselinkprofileentitystate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|synapselinkprofileentitystate|
|ReferencingAttribute|profile|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|profileentitystates|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_profileschedules"></a> profileschedules

Same as the [profileschedules](synapselinkschedule.md#BKMK_profileschedules) many-to-one relationship for the [synapselinkschedule](synapselinkschedule.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|synapselinkschedule|
|ReferencingAttribute|profile|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|profileschedules|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_synapselinkprofile_createdby](#BKMK_lk_synapselinkprofile_createdby)
- [lk_synapselinkprofile_createdonbehalfby](#BKMK_lk_synapselinkprofile_createdonbehalfby)
- [lk_synapselinkprofile_modifiedby](#BKMK_lk_synapselinkprofile_modifiedby)
- [lk_synapselinkprofile_modifiedonbehalfby](#BKMK_lk_synapselinkprofile_modifiedonbehalfby)
- [organization_synapselinkprofile](#BKMK_organization_synapselinkprofile)
- [synapselinkprofiles](#BKMK_synapselinkprofiles)


### <a name="BKMK_lk_synapselinkprofile_createdby"></a> lk_synapselinkprofile_createdby

**Added by**: System Solution Solution

See the [lk_synapselinkprofile_createdby](systemuser.md#BKMK_lk_synapselinkprofile_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_synapselinkprofile_createdonbehalfby"></a> lk_synapselinkprofile_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_synapselinkprofile_createdonbehalfby](systemuser.md#BKMK_lk_synapselinkprofile_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_synapselinkprofile_modifiedby"></a> lk_synapselinkprofile_modifiedby

**Added by**: System Solution Solution

See the [lk_synapselinkprofile_modifiedby](systemuser.md#BKMK_lk_synapselinkprofile_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_synapselinkprofile_modifiedonbehalfby"></a> lk_synapselinkprofile_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_synapselinkprofile_modifiedonbehalfby](systemuser.md#BKMK_lk_synapselinkprofile_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_organization_synapselinkprofile"></a> organization_synapselinkprofile

**Added by**: System Solution Solution

See the [organization_synapselinkprofile](organization.md#BKMK_organization_synapselinkprofile) one-to-many relationship for the [organization](organization.md) table/entity.

### <a name="BKMK_synapselinkprofiles"></a> synapselinkprofiles

**Added by**: Data lake workspaces Solution

See the [synapselinkprofiles](datalakefolder.md#BKMK_synapselinkprofiles) one-to-many relationship for the [datalakefolder](datalakefolder.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.synapselinkprofile?text=synapselinkprofile EntityType" />