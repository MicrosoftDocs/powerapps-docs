---
title: "sharedworkspaceaccesstoken table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the sharedworkspaceaccesstoken table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# sharedworkspaceaccesstoken table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Contains information about the shared workspace access tokens.

**Added by**: Real-time Collaboration App Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST /sharedworkspaceaccesstokens<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /sharedworkspaceaccesstokens(*sharedworkspaceaccesstokenid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET /sharedworkspaceaccesstokens(*sharedworkspaceaccesstokenid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /sharedworkspaceaccesstokens<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH /sharedworkspaceaccesstokens(*sharedworkspaceaccesstokenid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|Upsert||<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
|UpsertMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|sharedworkspaceaccesstokens|
|DisplayCollectionName|Shared Workspace Access Tokens|
|DisplayName|Shared Workspace Access Token|
|EntitySetName|sharedworkspaceaccesstokens|
|IsBPFEntity|False|
|LogicalCollectionName|sharedworkspaceaccesstokens|
|LogicalName|sharedworkspaceaccesstoken|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|sharedworkspaceaccesstokenid|
|PrimaryNameAttribute|systemuserid|
|SchemaName|sharedworkspaceaccesstoken|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [ObjectPartitionId](#BKMK_ObjectPartitionId)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PartitionId](#BKMK_PartitionId)
- [sharedworkspaceaccesstokenId](#BKMK_sharedworkspaceaccesstokenId)
- [SharedWorkspaceId](#BKMK_SharedWorkspaceId)
- [SystemUserId](#BKMK_SystemUserId)
- [TenantId](#BKMK_TenantId)
- [TokenId](#BKMK_TokenId)
- [TTLInSeconds](#BKMK_TTLInSeconds)


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


### <a name="BKMK_ObjectPartitionId"></a> ObjectPartitionId

|Property|Value|
|--------|-----|
|Description|Logical object partition id to be used by an elastic table row.|
|DisplayName|Object Partition Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|objectpartitionid|
|MaxLength|256|
|RequiredLevel|None|
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


### <a name="BKMK_PartitionId"></a> PartitionId

|Property|Value|
|--------|-----|
|Description|Logical partition id. A logical partition consists of a set of records with same partition id.|
|DisplayName|Partition Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|partitionid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_sharedworkspaceaccesstokenId"></a> sharedworkspaceaccesstokenId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Shared Workspace Access Token|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|sharedworkspaceaccesstokenid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SharedWorkspaceId"></a> SharedWorkspaceId

|Property|Value|
|--------|-----|
|Description|Shared Workspace Id|
|DisplayName|SharedWorkspaceId|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|sharedworkspaceid|
|MaxLength|256|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_SystemUserId"></a> SystemUserId

|Property|Value|
|--------|-----|
|Description|System User identifier|
|DisplayName|SystemUserId|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|systemuserid|
|MaxLength|256|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_TenantId"></a> TenantId

|Property|Value|
|--------|-----|
|Description|The tenant where the workspace resides|
|DisplayName|Tenant ID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|tenantid|
|MaxLength|256|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_TokenId"></a> TokenId

|Property|Value|
|--------|-----|
|Description|Access Token Id|
|DisplayName|TokenId|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|tokenid|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TTLInSeconds"></a> TTLInSeconds

|Property|Value|
|--------|-----|
|Description|After the specified number of seconds the access token will be deleted|
|DisplayName|Expiry (seconds)|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ttlinseconds|
|MaxValue|2147483647|
|MinValue|1|
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
|Description|Date and time when entity was created.|
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_sharedworkspaceaccesstoken_createdby](#BKMK_lk_sharedworkspaceaccesstoken_createdby)
- [lk_sharedworkspaceaccesstoken_createdonbehalfby](#BKMK_lk_sharedworkspaceaccesstoken_createdonbehalfby)
- [lk_sharedworkspaceaccesstoken_modifiedby](#BKMK_lk_sharedworkspaceaccesstoken_modifiedby)
- [lk_sharedworkspaceaccesstoken_modifiedonbehalfby](#BKMK_lk_sharedworkspaceaccesstoken_modifiedonbehalfby)


### <a name="BKMK_lk_sharedworkspaceaccesstoken_createdby"></a> lk_sharedworkspaceaccesstoken_createdby

**Added by**: System Solution Solution

See the [lk_sharedworkspaceaccesstoken_createdby](systemuser.md#BKMK_lk_sharedworkspaceaccesstoken_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_sharedworkspaceaccesstoken_createdonbehalfby"></a> lk_sharedworkspaceaccesstoken_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_sharedworkspaceaccesstoken_createdonbehalfby](systemuser.md#BKMK_lk_sharedworkspaceaccesstoken_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_sharedworkspaceaccesstoken_modifiedby"></a> lk_sharedworkspaceaccesstoken_modifiedby

**Added by**: System Solution Solution

See the [lk_sharedworkspaceaccesstoken_modifiedby](systemuser.md#BKMK_lk_sharedworkspaceaccesstoken_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_sharedworkspaceaccesstoken_modifiedonbehalfby"></a> lk_sharedworkspaceaccesstoken_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_sharedworkspaceaccesstoken_modifiedonbehalfby](systemuser.md#BKMK_lk_sharedworkspaceaccesstoken_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.sharedworkspaceaccesstoken?text=sharedworkspaceaccesstoken EntityType" />