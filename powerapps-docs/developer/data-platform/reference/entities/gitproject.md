---
title: "Git Project (GitProject) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Git Project (GitProject) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Git Project (GitProject) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Git Project (GitProject) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Create`<br />Event: False |`POST` /gitprojects<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: False |`DELETE` /gitprojects(*gitprojectid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Retrieve`<br />Event: False |`GET` /gitprojects(*gitprojectid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: False | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: False |`GET` /gitprojects<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /gitprojects(*gitprojectid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /gitprojects(*gitprojectid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Git Project (GitProject) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Git Project** |
| **DisplayCollectionName** | **Git Projects** |
| **SchemaName** | `GitProject` |
| **CollectionSchemaName** | `GitProjects` |
| **EntitySetName** | `gitprojects`|
| **LogicalName** | `gitproject` |
| **LogicalCollectionName** | `gitprojects` |
| **PrimaryIdAttribute** | `gitprojectid` |
| **PrimaryNameAttribute** |`projectname` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [GitProjectId](#BKMK_GitProjectId)
- [OrganizationName](#BKMK_OrganizationName)
- [ProjectName](#BKMK_ProjectName)

### <a name="BKMK_GitProjectId"></a> GitProjectId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Git Project**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`gitprojectid`|
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
|Description|**The name of the Git Project.**|
|DisplayName|**Git Project Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`projectname`|
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
<xref:Microsoft.Dynamics.CRM.gitproject?displayProperty=fullName>
