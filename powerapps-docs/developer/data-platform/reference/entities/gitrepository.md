---
title: "Git Repository (GitRepository) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Git Repository (GitRepository) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Git Repository (GitRepository) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Git Repository (GitRepository) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Create`<br />Event: False |`POST` /gitrepositories<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: False |`DELETE` /gitrepositories(*gitrepositoryid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Retrieve`<br />Event: False |`GET` /gitrepositories(*gitrepositoryid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: False | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: False |`GET` /gitrepositories<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /gitrepositories(*gitrepositoryid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /gitrepositories(*gitrepositoryid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Git Repository (GitRepository) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Git Repository** |
| **DisplayCollectionName** | **Git Repositories** |
| **SchemaName** | `GitRepository` |
| **CollectionSchemaName** | `GitRepositories` |
| **EntitySetName** | `gitrepositories`|
| **LogicalName** | `gitrepository` |
| **LogicalCollectionName** | `gitrepositories` |
| **PrimaryIdAttribute** | `gitrepositoryid` |
| **PrimaryNameAttribute** |`repositoryname` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [DefaultBranch](#BKMK_DefaultBranch)
- [GitRepositoryId](#BKMK_GitRepositoryId)
- [OrganizationName](#BKMK_OrganizationName)
- [ProjectName](#BKMK_ProjectName)
- [RepositoryName](#BKMK_RepositoryName)

### <a name="BKMK_DefaultBranch"></a> DefaultBranch

|Property|Value|
|---|---|
|Description|**Name of Git Default Git Branch with Git Repository.**|
|DisplayName|**Git Repository Default Branch**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`defaultbranch`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_GitRepositoryId"></a> GitRepositoryId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Git Repository**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`gitrepositoryid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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
|Description|**The name of the Git Repository.**|
|DisplayName|**Git Repository Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`repositoryname`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|




### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.gitrepository?displayProperty=fullName>
