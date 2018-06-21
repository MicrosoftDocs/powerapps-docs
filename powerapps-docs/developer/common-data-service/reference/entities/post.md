---
title: "Post Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the Post entity."

services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: kvivek
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/07/2018
ms.author: jdaly
---
# Post Entity Reference

An activity feed post.

## Entity Properties

**DisplayName**: Post<br />
**DisplayCollectionName**: Posts<br />
**SchemaName**: Post<br />
**CollectionSchemaName**: Posts<br />
**LogicalName**: post<br />
**LogicalCollectionName**: posts<br />
**EntitySetName**: posts<br />
**PrimaryIdAttribute**: postid<br />
**PrimaryNameAttribute**: text<br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [PostId](#BKMK_PostId)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [Source](#BKMK_Source)
- [Text](#BKMK_Text)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [Type](#BKMK_Type)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_PostId"></a> PostId

**Description**: Unique identifier for entity instances<br />
**DisplayName**: Post<br />
**LogicalName**: postid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

**Description**: Choose the parent record for the post to identify the customer, opportunity, case, or other record that the post most closely relates to.<br />
**DisplayName**: Regarding<br />
**LogicalName**: regardingobjectid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: 


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjectidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 4000


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

**Description**: Type of the RegardingObject<br />
**DisplayName**: RegardingObjectTypeCode<br />
**LogicalName**: regardingobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_Source"></a> Source

**Description**: Select whether the post was created manually or automatically.<br />
**DisplayName**: Source<br />
**LogicalName**: source<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Auto Post
- **Value**: 2 **Label**: Manual Post
- **Value**: 3 **Label**: ActionHub Post



### <a name="BKMK_Text"></a> Text

**Description**: Shows the text of a post. If this is a manual post, it appears in plain text. If this is an auto post, it appears in XML.<br />
**DisplayName**: Text<br />
**LogicalName**: text<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

**Description**: For internal use only.<br />
**DisplayName**: Time Zone Rule Version Number<br />
**LogicalName**: timezoneruleversionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_Type"></a> Type

**Description**: Select the post type.<br />
**DisplayName**: Type<br />
**LogicalName**: type<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Check-in
- **Value**: 2 **Label**: Idea
- **Value**: 3 **Label**: News
- **Value**: 4 **Label**: Private Message
- **Value**: 5 **Label**: Question
- **Value**: 6 **Label**: Re-post
- **Value**: 7 **Label**: Status



### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

**Description**: Time zone code that was in use when the record was created.<br />
**DisplayName**: UTC Conversion Time Zone Code<br />
**LogicalName**: utcconversiontimezonecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [PostRegardingId](#BKMK_PostRegardingId)
- [PostToYammer](#BKMK_PostToYammer)
- [RegardingObjectIdYomiName](#BKMK_RegardingObjectIdYomiName)
- [RegardingObjectOwnerId](#BKMK_RegardingObjectOwnerId)
- [RegardingObjectOwnerIdType](#BKMK_RegardingObjectOwnerIdType)
- [RegardingObjectOwningBusinessUnit](#BKMK_RegardingObjectOwningBusinessUnit)
- [YammerPostState](#BKMK_YammerPostState)
- [YammerRetryCount](#BKMK_YammerRetryCount)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Shows who created the record.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Shows who created the record on behalf of another user.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who modified the record.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who modified the record.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization associated with the solution.<br />
**DisplayName**: Organization<br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: organization


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: organizationidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_PostRegardingId"></a> PostRegardingId

**Description**: Unique identifier of the post regarding with which the post is associated.<br />
**DisplayName**: Post Regarding<br />
**LogicalName**: postregardingid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: postregarding


### <a name="BKMK_PostToYammer"></a> PostToYammer

**Description**: Internal use only.<br />
**DisplayName**: post to yammer<br />
**LogicalName**: posttoyammer<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_RegardingObjectIdYomiName"></a> RegardingObjectIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjectidyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_RegardingObjectOwnerId"></a> RegardingObjectOwnerId

**Description**: Unique identifier of the user or team who owns the regarding object.<br />
**DisplayName**: Owner<br />
**LogicalName**: regardingobjectownerid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_RegardingObjectOwnerIdType"></a> RegardingObjectOwnerIdType

**Description**: Type of the RegardingObjectOwnerId<br />
**DisplayName**: RegardingObjectOwnerIdType<br />
**LogicalName**: regardingobjectowneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_RegardingObjectOwningBusinessUnit"></a> RegardingObjectOwningBusinessUnit

**Description**: Unique identifier of the business unit that owns the regarding object.<br />
**DisplayName**: Regarding object owning Business Unit<br />
**LogicalName**: regardingobjectowningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_YammerPostState"></a> YammerPostState

**Description**: Internal use only.<br />
**DisplayName**: Yammer Post State<br />
**LogicalName**: yammerpoststate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 5<br />
**MinValue**: 0


### <a name="BKMK_YammerRetryCount"></a> YammerRetryCount

**Description**: Internal use only.<br />
**DisplayName**: Yammer Retry Count<br />
**LogicalName**: yammerretrycount<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [post_AsyncOperations](#BKMK_post_AsyncOperations)
- [post_BulkDeleteFailures](#BKMK_post_BulkDeleteFailures)
- [Post_Comments](#BKMK_Post_Comments)
- [Post_Likes](#BKMK_Post_Likes)


### <a name="BKMK_post_AsyncOperations"></a> post_AsyncOperations

Same as asyncoperation entity [post_AsyncOperations](asyncoperation.md#BKMK_post_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: post_AsyncOperations<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_post_BulkDeleteFailures"></a> post_BulkDeleteFailures

Same as bulkdeletefailure entity [post_BulkDeleteFailures](bulkdeletefailure.md#BKMK_post_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: post_BulkDeleteFailures<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_Post_Comments"></a> Post_Comments

Same as postcomment entity [Post_Comments](postcomment.md#BKMK_Post_Comments) Many-To-One relationship.

**ReferencingEntity**: postcomment<br />
**ReferencingAttribute**: postid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Post_Comments<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_Post_Likes"></a> Post_Likes

Same as postlike entity [Post_Likes](postlike.md#BKMK_Post_Likes) Many-To-One relationship.

**ReferencingEntity**: postlike<br />
**ReferencingAttribute**: postid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Post_Likes<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [lk_post_createdby](#BKMK_lk_post_createdby)
- [lk_post_createdonbehalfby](#BKMK_lk_post_createdonbehalfby)
- [lk_post_modifiedby](#BKMK_lk_post_modifiedby)
- [lk_post_modifiedonbehalfby](#BKMK_lk_post_modifiedonbehalfby)
- [organization_post](#BKMK_organization_post)


### <a name="BKMK_lk_post_createdby"></a> lk_post_createdby

See systemuser Entity [lk_post_createdby](systemuser.md#BKMK_lk_post_createdby) One-To-Many relationship.

### <a name="BKMK_lk_post_createdonbehalfby"></a> lk_post_createdonbehalfby

See systemuser Entity [lk_post_createdonbehalfby](systemuser.md#BKMK_lk_post_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_post_modifiedby"></a> lk_post_modifiedby

See systemuser Entity [lk_post_modifiedby](systemuser.md#BKMK_lk_post_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_post_modifiedonbehalfby"></a> lk_post_modifiedonbehalfby

See systemuser Entity [lk_post_modifiedonbehalfby](systemuser.md#BKMK_lk_post_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_post"></a> organization_post

See organization Entity [organization_post](organization.md#BKMK_organization_post) One-To-Many relationship.
post

