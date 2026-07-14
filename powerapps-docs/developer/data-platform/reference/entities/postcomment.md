---
title: "Comment (PostComment) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Comment (PostComment) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Comment (PostComment) table/entity reference (Microsoft Dataverse)

A comment on an activity feed post.

## Messages

The following table lists the messages for the Comment (PostComment) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /postcomments<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /postcomments(*postcommentid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /postcomments(*postcommentid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /postcomments<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Comment (PostComment) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Comment** |
| **DisplayCollectionName** | **Comments** |
| **SchemaName** | `PostComment` |
| **CollectionSchemaName** | `PostComments` |
| **EntitySetName** | `postcomments`|
| **LogicalName** | `postcomment` |
| **LogicalCollectionName** | `postcomments` |
| **PrimaryIdAttribute** | `postcommentid` |
| **PrimaryNameAttribute** |`text` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [LargeText](#BKMK_LargeText)
- [PostCommentId](#BKMK_PostCommentId)
- [PostId](#BKMK_PostId)
- [Text](#BKMK_Text)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_LargeText"></a> LargeText

|Property|Value|
|---|---|
|Description|**Shows the text of a post comment.**|
|DisplayName|**Text**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`largetext`|
|RequiredLevel|ApplicationRequired|
|Type|Memo|
|Format|Email|
|FormatName|Email|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_PostCommentId"></a> PostCommentId

|Property|Value|
|---|---|
|Description|**Shows the ID of the post comment.**|
|DisplayName|**PostComment**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`postcommentid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_PostId"></a> PostId

|Property|Value|
|---|---|
|Description|**Unique identifier of the post with which the comment is associated.**|
|DisplayName|**Post**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`postid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|post|

### <a name="BKMK_Text"></a> Text

|Property|Value|
|---|---|
|Description|**Text of the comment.**|
|DisplayName|**Text**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`text`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

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

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)

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
|RequiredLevel|SystemRequired|
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

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization associated with the solution.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [lk_postcomment_createdby](#BKMK_lk_postcomment_createdby)
- [lk_postcomment_createdonbehalfby](#BKMK_lk_postcomment_createdonbehalfby)
- [organization_PostComment](#BKMK_organization_PostComment)
- [Post_Comments](#BKMK_Post_Comments)

### <a name="BKMK_lk_postcomment_createdby"></a> lk_postcomment_createdby

One-To-Many Relationship: [systemuser lk_postcomment_createdby](systemuser.md#BKMK_lk_postcomment_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_postcomment_createdonbehalfby"></a> lk_postcomment_createdonbehalfby

One-To-Many Relationship: [systemuser lk_postcomment_createdonbehalfby](systemuser.md#BKMK_lk_postcomment_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_PostComment"></a> organization_PostComment

One-To-Many Relationship: [organization organization_PostComment](organization.md#BKMK_organization_PostComment)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Post_Comments"></a> Post_Comments

One-To-Many Relationship: [post Post_Comments](post.md#BKMK_Post_Comments)

|Property|Value|
|---|---|
|ReferencedEntity|`post`|
|ReferencedAttribute|`postid`|
|ReferencingAttribute|`postid`|
|ReferencingEntityNavigationPropertyName|`postid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_post_comment_activity_file_attachment"></a> post_comment_activity_file_attachment

Many-To-One Relationship: [activityfileattachment post_comment_activity_file_attachment](activityfileattachment.md#BKMK_post_comment_activity_file_attachment)

|Property|Value|
|---|---|
|ReferencingEntity|`activityfileattachment`|
|ReferencingAttribute|`parentid`|
|ReferencedEntityNavigationPropertyName|`post_comment_activity_file_attachment`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.postcomment?displayProperty=fullName>
