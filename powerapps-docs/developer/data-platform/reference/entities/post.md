---
title: "Post table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Post table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Post table/entity reference (Microsoft Dataverse)

An activity feed post.

## Messages

The following table lists the messages for the Post table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /posts<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /posts(*postid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /posts(*postid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /posts<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Post table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Post** |
| **DisplayCollectionName** | **Posts** |
| **SchemaName** | `Post` |
| **CollectionSchemaName** | `Posts` |
| **EntitySetName** | `posts`|
| **LogicalName** | `post` |
| **LogicalCollectionName** | `posts` |
| **PrimaryIdAttribute** | `postid` |
| **PrimaryNameAttribute** |`text` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [LargeText](#BKMK_LargeText)
- [PostId](#BKMK_PostId)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [Source](#BKMK_Source)
- [Text](#BKMK_Text)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [Type](#BKMK_Type)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_LargeText"></a> LargeText

|Property|Value|
|---|---|
|Description|**Shows the text of a post.**|
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

### <a name="BKMK_PostId"></a> PostId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Post**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`postid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**Choose the parent record for the post to identify the customer, opportunity, case, or other record that the post most closely relates to.**|
|DisplayName|**Regarding**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`regardingobjectid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets||

### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|---|---|
|Description|**Type of the RegardingObject**|
|DisplayName|**RegardingObjectTypeCode**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_Source"></a> Source

|Property|Value|
|---|---|
|Description|**Select whether the post was created manually or automatically.**|
|DisplayName|**Source**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`source`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|2|
|GlobalChoiceName|`post_source`|

#### Source Choices/Options

|Value|Label|
|---|---|
|1|**Auto Post**|
|2|**Manual Post**|
|3|**ActionHub Post**|

### <a name="BKMK_Text"></a> Text

|Property|Value|
|---|---|
|Description|**Shows the text of a post. If this is a manual post, it appears in plain text. If this is an auto post, it appears in XML.**|
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
|MaxLength|2000|

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

### <a name="BKMK_Type"></a> Type

|Property|Value|
|---|---|
|Description|**Select the post type.**|
|DisplayName|**Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`type`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`post_type`|

#### Type Choices/Options

|Value|Label|
|---|---|
|1|**Check-in**|
|2|**Idea**|
|3|**News**|
|4|**Private Message**|
|5|**Question**|
|6|**Re-post**|
|7|**Status**|

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
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [PostRegardingId](#BKMK_PostRegardingId)
- [PostToYammer](#BKMK_PostToYammer)
- [RegardingObjectOwnerId](#BKMK_RegardingObjectOwnerId)
- [RegardingObjectOwnerIdType](#BKMK_RegardingObjectOwnerIdType)
- [RegardingObjectOwningBusinessUnit](#BKMK_RegardingObjectOwningBusinessUnit)
- [YammerPostState](#BKMK_YammerPostState)
- [YammerRetryCount](#BKMK_YammerRetryCount)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Shows who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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
|Description|**Shows who created the record on behalf of another user.**|
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
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
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

### <a name="BKMK_PostRegardingId"></a> PostRegardingId

|Property|Value|
|---|---|
|Description|**Unique identifier of the post regarding with which the post is associated.**|
|DisplayName|**Post Regarding**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`postregardingid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|postregarding|

### <a name="BKMK_PostToYammer"></a> PostToYammer

|Property|Value|
|---|---|
|Description|**Internal use only.**|
|DisplayName|**post to yammer**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`posttoyammer`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`post_posttoyammer`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_RegardingObjectOwnerId"></a> RegardingObjectOwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user or team who owns the regarding object.**|
|DisplayName|**Owner**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjectownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_RegardingObjectOwnerIdType"></a> RegardingObjectOwnerIdType

|Property|Value|
|---|---|
|Description|**Type of the RegardingObjectOwnerId**|
|DisplayName|**RegardingObjectOwnerIdType**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjectowneridtype`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_RegardingObjectOwningBusinessUnit"></a> RegardingObjectOwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Unique identifier of the business unit that owns the regarding object.**|
|DisplayName|**Regarding object owning Business Unit**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjectowningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_YammerPostState"></a> YammerPostState

|Property|Value|
|---|---|
|Description|**Internal use only.**|
|DisplayName|**Yammer Post State**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`yammerpoststate`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|5|
|MinValue|0|

### <a name="BKMK_YammerRetryCount"></a> YammerRetryCount

|Property|Value|
|---|---|
|Description|**Internal use only.**|
|DisplayName|**Yammer Retry Count**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`yammerretrycount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [lk_post_createdby](#BKMK_lk_post_createdby)
- [lk_post_createdonbehalfby](#BKMK_lk_post_createdonbehalfby)
- [lk_post_modifiedby](#BKMK_lk_post_modifiedby)
- [lk_post_modifiedonbehalfby](#BKMK_lk_post_modifiedonbehalfby)
- [organization_post](#BKMK_organization_post)
- [post_PostRegardings](#BKMK_post_PostRegardings)

### <a name="BKMK_lk_post_createdby"></a> lk_post_createdby

One-To-Many Relationship: [systemuser lk_post_createdby](systemuser.md#BKMK_lk_post_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_post_createdonbehalfby"></a> lk_post_createdonbehalfby

One-To-Many Relationship: [systemuser lk_post_createdonbehalfby](systemuser.md#BKMK_lk_post_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_post_modifiedby"></a> lk_post_modifiedby

One-To-Many Relationship: [systemuser lk_post_modifiedby](systemuser.md#BKMK_lk_post_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_post_modifiedonbehalfby"></a> lk_post_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_post_modifiedonbehalfby](systemuser.md#BKMK_lk_post_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_post"></a> organization_post

One-To-Many Relationship: [organization organization_post](organization.md#BKMK_organization_post)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_post_PostRegardings"></a> post_PostRegardings

One-To-Many Relationship: [postregarding post_PostRegardings](postregarding.md#BKMK_post_PostRegardings)

|Property|Value|
|---|---|
|ReferencedEntity|`postregarding`|
|ReferencedAttribute|`postregardingid`|
|ReferencingAttribute|`postregardingid`|
|ReferencingEntityNavigationPropertyName|`postregardingid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [post_activity_file_attachment](#BKMK_post_activity_file_attachment)
- [post_AsyncOperations](#BKMK_post_AsyncOperations)
- [post_BulkDeleteFailures](#BKMK_post_BulkDeleteFailures)
- [Post_Comments](#BKMK_Post_Comments)
- [Post_Likes](#BKMK_Post_Likes)

### <a name="BKMK_post_activity_file_attachment"></a> post_activity_file_attachment

Many-To-One Relationship: [activityfileattachment post_activity_file_attachment](activityfileattachment.md#BKMK_post_activity_file_attachment)

|Property|Value|
|---|---|
|ReferencingEntity|`activityfileattachment`|
|ReferencingAttribute|`parentid`|
|ReferencedEntityNavigationPropertyName|`post_activity_file_attachment`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_post_AsyncOperations"></a> post_AsyncOperations

Many-To-One Relationship: [asyncoperation post_AsyncOperations](asyncoperation.md#BKMK_post_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`post_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_post_BulkDeleteFailures"></a> post_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure post_BulkDeleteFailures](bulkdeletefailure.md#BKMK_post_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`post_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Post_Comments"></a> Post_Comments

Many-To-One Relationship: [postcomment Post_Comments](postcomment.md#BKMK_Post_Comments)

|Property|Value|
|---|---|
|ReferencingEntity|`postcomment`|
|ReferencingAttribute|`postid`|
|ReferencedEntityNavigationPropertyName|`Post_Comments`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Post_Likes"></a> Post_Likes

Many-To-One Relationship: [postlike Post_Likes](postlike.md#BKMK_Post_Likes)

|Property|Value|
|---|---|
|ReferencingEntity|`postlike`|
|ReferencingAttribute|`postid`|
|ReferencedEntityNavigationPropertyName|`Post_Likes`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.post?displayProperty=fullName>
