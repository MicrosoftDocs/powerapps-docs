---
title: "Article Comment (KbArticleComment) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Article Comment (KbArticleComment) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Article Comment (KbArticleComment) table/entity reference (Microsoft Dataverse)

Comment on a knowledge base article.

## Messages

The following table lists the messages for the Article Comment (KbArticleComment) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /kbarticlecomments<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /kbarticlecomments(*kbarticlecommentid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /kbarticlecomments(*kbarticlecommentid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /kbarticlecomments<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /kbarticlecomments(*kbarticlecommentid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /kbarticlecomments(*kbarticlecommentid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Article Comment (KbArticleComment) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Article Comment** |
| **DisplayCollectionName** | **Article Comments** |
| **SchemaName** | `KbArticleComment` |
| **CollectionSchemaName** | `KbArticleComments` |
| **EntitySetName** | `kbarticlecomments`|
| **LogicalName** | `kbarticlecomment` |
| **LogicalCollectionName** | `kbarticlecomments` |
| **PrimaryIdAttribute** | `kbarticlecommentid` |
| **PrimaryNameAttribute** |`title` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CommentText](#BKMK_CommentText)
- [KbArticleCommentId](#BKMK_KbArticleCommentId)
- [KbArticleId](#BKMK_KbArticleId)
- [Title](#BKMK_Title)

### <a name="BKMK_CommentText"></a> CommentText

|Property|Value|
|---|---|
|Description|**Comment text for the knowledge base article.**|
|DisplayName|**Comment Text**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`commenttext`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_KbArticleCommentId"></a> KbArticleCommentId

|Property|Value|
|---|---|
|Description|**Unique identifier of the knowledge base article comment.**|
|DisplayName|**Article Comment**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`kbarticlecommentid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_KbArticleId"></a> KbArticleId

|Property|Value|
|---|---|
|Description|**Unique identifier of the knowledge base article to which the comment applies.**|
|DisplayName|**KB Article**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`kbarticleid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|kbarticle|

### <a name="BKMK_Title"></a> Title

|Property|Value|
|---|---|
|Description|**Title of the knowledge base article comment.**|
|DisplayName|**Title**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`title`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|


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
|Description|**Unique identifier of the user who created the knowledge base article comment.**|
|DisplayName|**Created By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the knowledge base article comment was created.**|
|DisplayName|**Created On**|
|IsValidForForm|False|
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
|Description|**Unique identifier of the delegate user who created the kbarticlecomment.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the knowledge base article comment.**|
|DisplayName|**Modified By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the knowledge base article comment was last modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|False|
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
|Description|**Unique identifier of the delegate user who last modified the kbarticlecomment.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization with which the article comment is associated.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [kbarticle_comments](#BKMK_kbarticle_comments)
- [lk_kbarticlecomment_createdonbehalfby](#BKMK_lk_kbarticlecomment_createdonbehalfby)
- [lk_kbarticlecomment_modifiedonbehalfby](#BKMK_lk_kbarticlecomment_modifiedonbehalfby)
- [lk_kbarticlecommentbase_createdby](#BKMK_lk_kbarticlecommentbase_createdby)
- [lk_kbarticlecommentbase_modifiedby](#BKMK_lk_kbarticlecommentbase_modifiedby)

### <a name="BKMK_kbarticle_comments"></a> kbarticle_comments

One-To-Many Relationship: [kbarticle kbarticle_comments](kbarticle.md#BKMK_kbarticle_comments)

|Property|Value|
|---|---|
|ReferencedEntity|`kbarticle`|
|ReferencedAttribute|`kbarticleid`|
|ReferencingAttribute|`kbarticleid`|
|ReferencingEntityNavigationPropertyName|`kbarticleid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_kbarticlecomment_createdonbehalfby"></a> lk_kbarticlecomment_createdonbehalfby

One-To-Many Relationship: [systemuser lk_kbarticlecomment_createdonbehalfby](systemuser.md#BKMK_lk_kbarticlecomment_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_kbarticlecomment_modifiedonbehalfby"></a> lk_kbarticlecomment_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_kbarticlecomment_modifiedonbehalfby](systemuser.md#BKMK_lk_kbarticlecomment_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_kbarticlecommentbase_createdby"></a> lk_kbarticlecommentbase_createdby

One-To-Many Relationship: [systemuser lk_kbarticlecommentbase_createdby](systemuser.md#BKMK_lk_kbarticlecommentbase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_kbarticlecommentbase_modifiedby"></a> lk_kbarticlecommentbase_modifiedby

One-To-Many Relationship: [systemuser lk_kbarticlecommentbase_modifiedby](systemuser.md#BKMK_lk_kbarticlecommentbase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [KbArticleComment_AsyncOperations](#BKMK_KbArticleComment_AsyncOperations)
- [KbArticleComment_BulkDeleteFailures](#BKMK_KbArticleComment_BulkDeleteFailures)
- [KbArticleComment_ProcessSessions](#BKMK_KbArticleComment_ProcessSessions)

### <a name="BKMK_KbArticleComment_AsyncOperations"></a> KbArticleComment_AsyncOperations

Many-To-One Relationship: [asyncoperation KbArticleComment_AsyncOperations](asyncoperation.md#BKMK_KbArticleComment_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KbArticleComment_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KbArticleComment_BulkDeleteFailures"></a> KbArticleComment_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure KbArticleComment_BulkDeleteFailures](bulkdeletefailure.md#BKMK_KbArticleComment_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KbArticleComment_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KbArticleComment_ProcessSessions"></a> KbArticleComment_ProcessSessions

Many-To-One Relationship: [processsession KbArticleComment_ProcessSessions](processsession.md#BKMK_KbArticleComment_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KbArticleComment_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.kbarticlecomment?displayProperty=fullName>
