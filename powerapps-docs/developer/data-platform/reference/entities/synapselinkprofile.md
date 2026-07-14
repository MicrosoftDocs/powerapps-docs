---
title: "Synapse Link Profile (synapselinkprofile) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Synapse Link Profile (synapselinkprofile) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Synapse Link Profile (synapselinkprofile) table/entity reference (Microsoft Dataverse)

Synapse Link Profile

## Messages

The following table lists the messages for the Synapse Link Profile (synapselinkprofile) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /synapselinkprofiles<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /synapselinkprofiles(*synapselinkprofileid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Retrieve`<br />Event: True |`GET` /synapselinkprofiles(*synapselinkprofileid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /synapselinkprofiles<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /synapselinkprofiles(*synapselinkprofileid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /synapselinkprofiles(*synapselinkprofileid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /synapselinkprofiles(*synapselinkprofileid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Synapse Link Profile (synapselinkprofile) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Synapse Link Profile** |
| **DisplayCollectionName** | **Synapse Link Profiles** |
| **SchemaName** | `synapselinkprofile` |
| **CollectionSchemaName** | `synapselinkprofiles` |
| **EntitySetName** | `synapselinkprofiles`|
| **LogicalName** | `synapselinkprofile` |
| **LogicalCollectionName** | `synapselinkprofiles` |
| **PrimaryIdAttribute** | `synapselinkprofileid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

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
|---|---|
|Description|**Activation time of profile**|
|DisplayName|**Activation Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`activationtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_CopyAttachments"></a> CopyAttachments

|Property|Value|
|---|---|
|Description|**Enable Copy Attachments**|
|DisplayName|**Copy Attachments**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`copyattachments`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`synapselinkprofile_copyattachments`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_CopyFiles"></a> CopyFiles

|Property|Value|
|---|---|
|Description|**Enable Copy Files**|
|DisplayName|**Copy Files**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`copyfiles`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`synapselinkprofile_copyfiles`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_datalakefolder"></a> datalakefolder

|Property|Value|
|---|---|
|Description|**Unique identifier for Data Lake Folder associated with Synapse Link Profile.**|
|DisplayName|**Data Lake Folder**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`datalakefolder`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|datalakefolder|

### <a name="BKMK_DestinationSyncState"></a> DestinationSyncState

|Property|Value|
|---|---|
|Description|**Sync state of the profile**|
|DisplayName|**Destination Sync State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`destinationsyncstate`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`synapselinkdestinationsyncstate`|

#### DestinationSyncState Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**NotCompleted**|
|2|**Completed**|

### <a name="BKMK_ExtendedProperties"></a> ExtendedProperties

|Property|Value|
|---|---|
|Description|**Extended properties**|
|DisplayName|**Extended Properties**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`extendedproperties`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

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

### <a name="BKMK_ProfileState"></a> ProfileState

|Property|Value|
|---|---|
|Description|**State of the profile**|
|DisplayName|**Profile State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`profilestate`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`synapselinkprofilestate`|

#### ProfileState Choices/Options

|Value|Label|
|---|---|
|0|**Inactive**|
|1|**Active**|
|2|**Error**|
|3|**Deleted**|
|4|**Aborting**|
|5|**Aborted**|
|6|**Suspended**|
|7|**Suspending**|
|8|**Deactivated**|

### <a name="BKMK_ProfileType"></a> ProfileType

|Property|Value|
|---|---|
|Description|**Type of profile**|
|DisplayName|**Profile Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`profiletype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`synapselinkprofiletype`|

#### ProfileType Choices/Options

|Value|Label|
|---|---|
|0|**SynapseLink**|
|1|**EventAnalytics**|

### <a name="BKMK_ProfileUpdatedTime"></a> ProfileUpdatedTime

|Property|Value|
|---|---|
|Description|**Profile Updated Time**|
|DisplayName|**Profile Updated Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`profileupdatedtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_ProfileVersion"></a> ProfileVersion

|Property|Value|
|---|---|
|Description|**Profile version**|
|DisplayName|**Profile Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`profileversion`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|32|

### <a name="BKMK_SnapshotsToPersist"></a> SnapshotsToPersist

|Property|Value|
|---|---|
|Description|**Number of snapshots To persist**|
|DisplayName|**Snapshots To Persist**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`snapshotstopersist`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|100|
|MinValue|0|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Synapse Link Profile**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`synapselinkprofile_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Synapse Link Profile**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`synapselinkprofile_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_synapselinkprofileId"></a> synapselinkprofileId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Synapse Link Profile**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`synapselinkprofileid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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

### <a name="BKMK_UniqueName"></a> UniqueName

|Property|Value|
|---|---|
|Description|**Unique name**|
|DisplayName|**Unique Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`uniquename`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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

- [lk_synapselinkprofile_createdby](#BKMK_lk_synapselinkprofile_createdby)
- [lk_synapselinkprofile_createdonbehalfby](#BKMK_lk_synapselinkprofile_createdonbehalfby)
- [lk_synapselinkprofile_modifiedby](#BKMK_lk_synapselinkprofile_modifiedby)
- [lk_synapselinkprofile_modifiedonbehalfby](#BKMK_lk_synapselinkprofile_modifiedonbehalfby)
- [organization_synapselinkprofile](#BKMK_organization_synapselinkprofile)
- [synapselinkprofiles](#BKMK_synapselinkprofiles)

### <a name="BKMK_lk_synapselinkprofile_createdby"></a> lk_synapselinkprofile_createdby

One-To-Many Relationship: [systemuser lk_synapselinkprofile_createdby](systemuser.md#BKMK_lk_synapselinkprofile_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_synapselinkprofile_createdonbehalfby"></a> lk_synapselinkprofile_createdonbehalfby

One-To-Many Relationship: [systemuser lk_synapselinkprofile_createdonbehalfby](systemuser.md#BKMK_lk_synapselinkprofile_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_synapselinkprofile_modifiedby"></a> lk_synapselinkprofile_modifiedby

One-To-Many Relationship: [systemuser lk_synapselinkprofile_modifiedby](systemuser.md#BKMK_lk_synapselinkprofile_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_synapselinkprofile_modifiedonbehalfby"></a> lk_synapselinkprofile_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_synapselinkprofile_modifiedonbehalfby](systemuser.md#BKMK_lk_synapselinkprofile_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_synapselinkprofile"></a> organization_synapselinkprofile

One-To-Many Relationship: [organization organization_synapselinkprofile](organization.md#BKMK_organization_synapselinkprofile)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofiles"></a> synapselinkprofiles

One-To-Many Relationship: [datalakefolder synapselinkprofiles](datalakefolder.md#BKMK_synapselinkprofiles)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakefolder`|
|ReferencedAttribute|`datalakefolderid`|
|ReferencingAttribute|`datalakefolder`|
|ReferencingEntityNavigationPropertyName|`datalakefolder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [profileentities](#BKMK_profileentities)
- [profileentitystates](#BKMK_profileentitystates)
- [profileschedules](#BKMK_profileschedules)
- [synapselinkprofile_AsyncOperations](#BKMK_synapselinkprofile_AsyncOperations)
- [synapselinkprofile_BulkDeleteFailures](#BKMK_synapselinkprofile_BulkDeleteFailures)
- [synapselinkprofile_DuplicateBaseRecord](#BKMK_synapselinkprofile_DuplicateBaseRecord)
- [synapselinkprofile_DuplicateMatchingRecord](#BKMK_synapselinkprofile_DuplicateMatchingRecord)
- [synapselinkprofile_MailboxTrackingFolders](#BKMK_synapselinkprofile_MailboxTrackingFolders)
- [synapselinkprofile_PrincipalObjectAttributeAccesses](#BKMK_synapselinkprofile_PrincipalObjectAttributeAccesses)
- [synapselinkprofile_ProcessSession](#BKMK_synapselinkprofile_ProcessSession)
- [synapselinkprofile_SyncErrors](#BKMK_synapselinkprofile_SyncErrors)

### <a name="BKMK_profileentities"></a> profileentities

Many-To-One Relationship: [synapselinkprofileentity profileentities](synapselinkprofileentity.md#BKMK_profileentities)

|Property|Value|
|---|---|
|ReferencingEntity|`synapselinkprofileentity`|
|ReferencingAttribute|`profile`|
|ReferencedEntityNavigationPropertyName|`profileentities`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseLabel`<br />Group: `Details`<br />Label: Profile<br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_profileentitystates"></a> profileentitystates

Many-To-One Relationship: [synapselinkprofileentitystate profileentitystates](synapselinkprofileentitystate.md#BKMK_profileentitystates)

|Property|Value|
|---|---|
|ReferencingEntity|`synapselinkprofileentitystate`|
|ReferencingAttribute|`profile`|
|ReferencedEntityNavigationPropertyName|`profileentitystates`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_profileschedules"></a> profileschedules

Many-To-One Relationship: [synapselinkschedule profileschedules](synapselinkschedule.md#BKMK_profileschedules)

|Property|Value|
|---|---|
|ReferencingEntity|`synapselinkschedule`|
|ReferencingAttribute|`profile`|
|ReferencedEntityNavigationPropertyName|`profileschedules`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofile_AsyncOperations"></a> synapselinkprofile_AsyncOperations

Many-To-One Relationship: [asyncoperation synapselinkprofile_AsyncOperations](asyncoperation.md#BKMK_synapselinkprofile_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofile_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofile_BulkDeleteFailures"></a> synapselinkprofile_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure synapselinkprofile_BulkDeleteFailures](bulkdeletefailure.md#BKMK_synapselinkprofile_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofile_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofile_DuplicateBaseRecord"></a> synapselinkprofile_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord synapselinkprofile_DuplicateBaseRecord](duplicaterecord.md#BKMK_synapselinkprofile_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofile_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofile_DuplicateMatchingRecord"></a> synapselinkprofile_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord synapselinkprofile_DuplicateMatchingRecord](duplicaterecord.md#BKMK_synapselinkprofile_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofile_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofile_MailboxTrackingFolders"></a> synapselinkprofile_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder synapselinkprofile_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_synapselinkprofile_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofile_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofile_PrincipalObjectAttributeAccesses"></a> synapselinkprofile_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess synapselinkprofile_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_synapselinkprofile_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofile_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofile_ProcessSession"></a> synapselinkprofile_ProcessSession

Many-To-One Relationship: [processsession synapselinkprofile_ProcessSession](processsession.md#BKMK_synapselinkprofile_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofile_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofile_SyncErrors"></a> synapselinkprofile_SyncErrors

Many-To-One Relationship: [syncerror synapselinkprofile_SyncErrors](syncerror.md#BKMK_synapselinkprofile_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofile_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.synapselinkprofile?displayProperty=fullName>
