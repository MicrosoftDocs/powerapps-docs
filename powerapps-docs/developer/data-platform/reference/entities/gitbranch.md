---
title: "Git Branch (GitBranch) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Git Branch (GitBranch) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Git Branch (GitBranch) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Git Branch (GitBranch) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Create`<br />Event: False |`POST` /gitbranches<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: False |`DELETE` /gitbranches(*gitbranchid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Retrieve`<br />Event: False |`GET` /gitbranches(*gitbranchid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: False | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: False |`GET` /gitbranches<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /gitbranches(*gitbranchid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /gitbranches(*gitbranchid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Git Branch (GitBranch) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Git Branch** |
| **DisplayCollectionName** | **Git Branches** |
| **SchemaName** | `GitBranch` |
| **CollectionSchemaName** | `GitBranchs` |
| **EntitySetName** | `gitbranches`|
| **LogicalName** | `gitbranch` |
| **LogicalCollectionName** | `gitbranchs` |
| **PrimaryIdAttribute** | `gitbranchid` |
| **PrimaryNameAttribute** |`branchname` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [BranchName](#BKMK_BranchName)
- [GitBranchId](#BKMK_GitBranchId)
- [GitCommitId](#BKMK_GitCommitId)
- [OrganizationName](#BKMK_OrganizationName)
- [ProjectName](#BKMK_ProjectName)
- [RepositoryName](#BKMK_RepositoryName)
- [UpstreamBranchName](#BKMK_UpstreamBranchName)

### <a name="BKMK_BranchName"></a> BranchName

|Property|Value|
|---|---|
|Description|**The name of the Git Branch.**|
|DisplayName|**Git Branch Name**|
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

### <a name="BKMK_GitBranchId"></a> GitBranchId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Git Branch**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`gitbranchid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_GitCommitId"></a> GitCommitId

|Property|Value|
|---|---|
|Description|**Current Git Commit Id of the Git Branch.**|
|DisplayName|**Current Git Commit Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`gitcommitid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_OrganizationName"></a> OrganizationName

|Property|Value|
|---|---|
|Description|**Name of the Git Organization associated with Git Project.**|
|DisplayName|**Git Organization Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`organizationname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_ProjectName"></a> ProjectName

|Property|Value|
|---|---|
|Description|**Name of Git Project associated with Git Repository.**|
|DisplayName|**Git Project Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`projectname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_RepositoryName"></a> RepositoryName

|Property|Value|
|---|---|
|Description|**Name of Git Repository associated with Git Branch.**|
|DisplayName|**Git Repository Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`repositoryname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_UpstreamBranchName"></a> UpstreamBranchName

|Property|Value|
|---|---|
|Description|**Name of the Git upstream branch from which the branch is created**|
|DisplayName|**Git upstream branch name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`upstreambranchname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|




### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.gitbranch?displayProperty=fullName>
