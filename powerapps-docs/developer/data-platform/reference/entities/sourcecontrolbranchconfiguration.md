---
title: "Source Control Branch Configuration (SourceControlBranchConfiguration) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Source Control Branch Configuration (SourceControlBranchConfiguration) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Source Control Branch Configuration (SourceControlBranchConfiguration) table/entity reference (Microsoft Dataverse)

Stores the source control branch configuration associated with the organization or solution

## Messages

The following table lists the messages for the Source Control Branch Configuration (SourceControlBranchConfiguration) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /sourcecontrolbranchconfigurations<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: False |`DELETE` /sourcecontrolbranchconfigurations(*sourcecontrolbranchconfigurationid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `DeleteMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.DeleteMultiple?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /sourcecontrolbranchconfigurations(*sourcecontrolbranchconfigurationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: False | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: False |`GET` /sourcecontrolbranchconfigurations<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /sourcecontrolbranchconfigurations(*sourcecontrolbranchconfigurationid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /sourcecontrolbranchconfigurations(*sourcecontrolbranchconfigurationid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Source Control Branch Configuration (SourceControlBranchConfiguration) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Source Control Branch Configuration** |
| **DisplayCollectionName** | **Source Control Branch Configurations** |
| **SchemaName** | `SourceControlBranchConfiguration` |
| **CollectionSchemaName** | `SourceControlBranchConfigurations` |
| **EntitySetName** | `sourcecontrolbranchconfigurations`|
| **LogicalName** | `sourcecontrolbranchconfiguration` |
| **LogicalCollectionName** | `sourcecontrolbranchconfigurations` |
| **PrimaryIdAttribute** | `sourcecontrolbranchconfigurationid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Elastic` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [BranchName](#BKMK_BranchName)
- [BranchSyncedCommitId](#BKMK_BranchSyncedCommitId)
- [BranchSyncedTime](#BKMK_BranchSyncedTime)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PartitionId](#BKMK_PartitionId)
- [RootFolderPath](#BKMK_RootFolderPath)
- [SourceControlBranchConfigurationId](#BKMK_SourceControlBranchConfigurationId)
- [SourceControlConfigurationId](#BKMK_SourceControlConfigurationId)
- [SourceControlConfigurationIdPId](#BKMK_SourceControlConfigurationIdPId)
- [StatusCode](#BKMK_StatusCode)
- [TTLInSeconds](#BKMK_TTLInSeconds)
- [UpstreamBranchName](#BKMK_UpstreamBranchName)
- [UpstreamBranchSyncedCommitId](#BKMK_UpstreamBranchSyncedCommitId)
- [UpstreamBranchSyncedTime](#BKMK_UpstreamBranchSyncedTime)

### <a name="BKMK_BranchName"></a> BranchName

|Property|Value|
|---|---|
|Description|**Name of the branch associated with the organization or solution**|
|DisplayName|**Branch Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`branchname`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_BranchSyncedCommitId"></a> BranchSyncedCommitId

|Property|Value|
|---|---|
|Description|**Git commit id of the branch which was last synced in the organization**|
|DisplayName|**Branch Synced Commit Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`branchsyncedcommitid`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_BranchSyncedTime"></a> BranchSyncedTime

|Property|Value|
|---|---|
|Description|**Specifies the time at which branch was last synced in the organization**|
|DisplayName|**Branch Synced Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`branchsyncedtime`|
|RequiredLevel|ApplicationRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

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

### <a name="BKMK_RootFolderPath"></a> RootFolderPath

|Property|Value|
|---|---|
|Description|**Specifies the relative path of the folder under which the organization or solution changes would be synced**|
|DisplayName|**Root Folder Path**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`rootfolderpath`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_SourceControlBranchConfigurationId"></a> SourceControlBranchConfigurationId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Source Control Branch Configuration**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sourcecontrolbranchconfigurationid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SourceControlConfigurationId"></a> SourceControlConfigurationId

|Property|Value|
|---|---|
|Description|**Unique identifier of source control configuration**|
|DisplayName|**Source Control Configuration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sourcecontrolconfigurationid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|sourcecontrolconfiguration|

### <a name="BKMK_SourceControlConfigurationIdPId"></a> SourceControlConfigurationIdPId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sourcecontrolconfigurationidpid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Describes solution git connection status.**|
|DisplayName|**StatusCode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`sourcecontrolbranchbonfiguration_statuscode`|

#### StatusCode Choices/Options

|Value|Label|
|---|---|
|0|**Connected**|
|1|**Disconnect**|
|2|**DisconnectInprogress**|
|3|**DisconnectFailed**|

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

### <a name="BKMK_UpstreamBranchName"></a> UpstreamBranchName

|Property|Value|
|---|---|
|Description|**Stores the git upstream branch name associated with the organization**|
|DisplayName|**Upstream Branch Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`upstreambranchname`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_UpstreamBranchSyncedCommitId"></a> UpstreamBranchSyncedCommitId

|Property|Value|
|---|---|
|Description|**Specifies the upstream branch commit id which was last synced to the current branch**|
|DisplayName|**Upstream Branch Synced Commit Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`upstreambranchsyncedcommitid`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_UpstreamBranchSyncedTime"></a> UpstreamBranchSyncedTime

|Property|Value|
|---|---|
|Description|**Specifies the time when the upstream branch was last synced to the current branch**|
|DisplayName|**Upstream Branch Synced Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`upstreambranchsyncedtime`|
|RequiredLevel|ApplicationRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|


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

- [lk_sourcecontrolbranchconfiguration_createdby](#BKMK_lk_sourcecontrolbranchconfiguration_createdby)
- [lk_sourcecontrolbranchconfiguration_createdonbehalfby](#BKMK_lk_sourcecontrolbranchconfiguration_createdonbehalfby)
- [lk_sourcecontrolbranchconfiguration_modifiedby](#BKMK_lk_sourcecontrolbranchconfiguration_modifiedby)
- [lk_sourcecontrolbranchconfiguration_modifiedonbehalfby](#BKMK_lk_sourcecontrolbranchconfiguration_modifiedonbehalfby)
- [sourcecontrolconfiguration_sourcecontrolbranchconfiguration](#BKMK_sourcecontrolconfiguration_sourcecontrolbranchconfiguration)

### <a name="BKMK_lk_sourcecontrolbranchconfiguration_createdby"></a> lk_sourcecontrolbranchconfiguration_createdby

One-To-Many Relationship: [systemuser lk_sourcecontrolbranchconfiguration_createdby](systemuser.md#BKMK_lk_sourcecontrolbranchconfiguration_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sourcecontrolbranchconfiguration_createdonbehalfby"></a> lk_sourcecontrolbranchconfiguration_createdonbehalfby

One-To-Many Relationship: [systemuser lk_sourcecontrolbranchconfiguration_createdonbehalfby](systemuser.md#BKMK_lk_sourcecontrolbranchconfiguration_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sourcecontrolbranchconfiguration_modifiedby"></a> lk_sourcecontrolbranchconfiguration_modifiedby

One-To-Many Relationship: [systemuser lk_sourcecontrolbranchconfiguration_modifiedby](systemuser.md#BKMK_lk_sourcecontrolbranchconfiguration_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sourcecontrolbranchconfiguration_modifiedonbehalfby"></a> lk_sourcecontrolbranchconfiguration_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_sourcecontrolbranchconfiguration_modifiedonbehalfby](systemuser.md#BKMK_lk_sourcecontrolbranchconfiguration_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sourcecontrolconfiguration_sourcecontrolbranchconfiguration"></a> sourcecontrolconfiguration_sourcecontrolbranchconfiguration

One-To-Many Relationship: [sourcecontrolconfiguration sourcecontrolconfiguration_sourcecontrolbranchconfiguration](sourcecontrolconfiguration.md#BKMK_sourcecontrolconfiguration_sourcecontrolbranchconfiguration)

|Property|Value|
|---|---|
|ReferencedEntity|`sourcecontrolconfiguration`|
|ReferencedAttribute|`sourcecontrolconfigurationid`|
|ReferencingAttribute|`sourcecontrolconfigurationid`|
|ReferencingEntityNavigationPropertyName|`sourcecontrolconfigurationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.sourcecontrolbranchconfiguration?displayProperty=fullName>
