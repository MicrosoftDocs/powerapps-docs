---
title: "PostFollow Entity Reference (Common Data Service for Apps)| MicrosoftDocs"
description: "Includes schema information and supported messages for the PostFollow entity."

services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
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
# PostFollow Entity Reference

Represents a user following the activity feed of an object.

## Entity Properties

**DisplayName**: Follow<br />
**DisplayCollectionName**: Follows<br />
**SchemaName**: PostFollow<br />
**CollectionSchemaName**: PostFollows<br />
**LogicalName**: postfollow<br />
**LogicalCollectionName**: postfollows<br />
**EntitySetName**: postfollows<br />
**PrimaryIdAttribute**: postfollowid<br />
**PrimaryNameAttribute**: regardingobjectidname<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [PostFollowId](#BKMK_PostFollowId)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: Owner Id Type<br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_PostFollowId"></a> PostFollowId

**Description**: Shows the ID of the post follow.<br />
**DisplayName**: PostFollow<br />
**LogicalName**: postfollowid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

**Description**: Choose the parent record for the followed post to identify the customer, opportunity, case, or other record type that the post most closely relates to.<br />
**DisplayName**: Regarding<br />
**LogicalName**: regardingobjectid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: account,appointment,contact,knowledgearticle,phonecall,processsession,queue,recurringappointmentmaster,systemuser,task


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

**Description**: Type of the RegardingObject<br />
**DisplayName**: RegardingObjectTypeCode<br />
**LogicalName**: regardingobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


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
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [PostToYammer](#BKMK_PostToYammer)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectIdYomiName](#BKMK_RegardingObjectIdYomiName)
- [VersionNumber](#BKMK_VersionNumber)
- [YammerPostState](#BKMK_YammerPostState)
- [YammerRetryCount](#BKMK_YammerRetryCount)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Shows who created the record.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
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
**RequiredLevel**: SystemRequired<br />
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


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Description**: Name of the owner<br />
**DisplayName**: <br />
**LogicalName**: owneridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

**Description**: Yomi name of the owner<br />
**DisplayName**: <br />
**LogicalName**: owneridyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Description**: Unique identifier for the business unit that owns the record.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier of the team who owns the follow.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier for the user who owns the record.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_PostToYammer"></a> PostToYammer

**Description**: Internal Use Only<br />
**DisplayName**: Internal Use Only<br />
**LogicalName**: posttoyammer<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

**Description**: Display name of the type of entity that the user followed.<br />
**DisplayName**: Regarding Entity Name<br />
**LogicalName**: regardingobjectidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 4000


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


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: Version number of post follow.<br />
**DisplayName**: Version Number<br />
**LogicalName**: versionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />


### <a name="BKMK_YammerPostState"></a> YammerPostState

**Description**: Internal Use Only<br />
**DisplayName**: Internal Use Only<br />
**LogicalName**: yammerpoststate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 5<br />
**MinValue**: 0


### <a name="BKMK_YammerRetryCount"></a> YammerRetryCount

**Description**: Internal Use Only<br />
**DisplayName**: Internal Use Only<br />
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

- [PostFollow_AsyncOperations](#BKMK_PostFollow_AsyncOperations)
- [PostFollow_SyncErrors](#BKMK_PostFollow_SyncErrors)


### <a name="BKMK_PostFollow_AsyncOperations"></a> PostFollow_AsyncOperations

Same as asyncoperation entity [PostFollow_AsyncOperations](asyncoperation.md#BKMK_PostFollow_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: PostFollow_AsyncOperations<br />
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


### <a name="BKMK_PostFollow_SyncErrors"></a> PostFollow_SyncErrors

Same as syncerror entity [PostFollow_SyncErrors](syncerror.md#BKMK_PostFollow_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: PostFollow_SyncErrors<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [task_PostFollows](#BKMK_task_PostFollows)
- [appointment_PostFollows](#BKMK_appointment_PostFollows)
- [phonecall_PostFollows](#BKMK_phonecall_PostFollows)
- [recurringappointmentmaster_PostFollows](#BKMK_recurringappointmentmaster_PostFollows)
- [lk_PostFollow_createdby](#BKMK_lk_PostFollow_createdby)
- [account_PostFollows](#BKMK_account_PostFollows)
- [contact_PostFollows](#BKMK_contact_PostFollows)
- [systemuser_PostFollows](#BKMK_systemuser_PostFollows)
- [business_unit_postfollows](#BKMK_business_unit_postfollows)
- [OwningTeam_postfollows](#BKMK_OwningTeam_postfollows)
- [user_owner_postfollows](#BKMK_user_owner_postfollows)
- [lk_postfollow_createdonbehalfby](#BKMK_lk_postfollow_createdonbehalfby)
- [processsession_PostFollows](#BKMK_processsession_PostFollows)
- [queue_PostFollows](#BKMK_queue_PostFollows)
- [knowledgearticle_PostFollows](#BKMK_knowledgearticle_PostFollows)


### <a name="BKMK_task_PostFollows"></a> task_PostFollows

See task Entity [task_PostFollows](task.md#BKMK_task_PostFollows) One-To-Many relationship.

### <a name="BKMK_appointment_PostFollows"></a> appointment_PostFollows

See appointment Entity [appointment_PostFollows](appointment.md#BKMK_appointment_PostFollows) One-To-Many relationship.

### <a name="BKMK_phonecall_PostFollows"></a> phonecall_PostFollows

See phonecall Entity [phonecall_PostFollows](phonecall.md#BKMK_phonecall_PostFollows) One-To-Many relationship.

### <a name="BKMK_recurringappointmentmaster_PostFollows"></a> recurringappointmentmaster_PostFollows

See recurringappointmentmaster Entity [recurringappointmentmaster_PostFollows](recurringappointmentmaster.md#BKMK_recurringappointmentmaster_PostFollows) One-To-Many relationship.

### <a name="BKMK_lk_PostFollow_createdby"></a> lk_PostFollow_createdby

See systemuser Entity [lk_PostFollow_createdby](systemuser.md#BKMK_lk_PostFollow_createdby) One-To-Many relationship.

### <a name="BKMK_account_PostFollows"></a> account_PostFollows

See account Entity [account_PostFollows](account.md#BKMK_account_PostFollows) One-To-Many relationship.

### <a name="BKMK_contact_PostFollows"></a> contact_PostFollows

See contact Entity [contact_PostFollows](contact.md#BKMK_contact_PostFollows) One-To-Many relationship.

### <a name="BKMK_systemuser_PostFollows"></a> systemuser_PostFollows

See systemuser Entity [systemuser_PostFollows](systemuser.md#BKMK_systemuser_PostFollows) One-To-Many relationship.

### <a name="BKMK_business_unit_postfollows"></a> business_unit_postfollows

See businessunit Entity [business_unit_postfollows](businessunit.md#BKMK_business_unit_postfollows) One-To-Many relationship.

### <a name="BKMK_OwningTeam_postfollows"></a> OwningTeam_postfollows

See team Entity [OwningTeam_postfollows](team.md#BKMK_OwningTeam_postfollows) One-To-Many relationship.

### <a name="BKMK_user_owner_postfollows"></a> user_owner_postfollows

See systemuser Entity [user_owner_postfollows](systemuser.md#BKMK_user_owner_postfollows) One-To-Many relationship.

### <a name="BKMK_lk_postfollow_createdonbehalfby"></a> lk_postfollow_createdonbehalfby

See systemuser Entity [lk_postfollow_createdonbehalfby](systemuser.md#BKMK_lk_postfollow_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_processsession_PostFollows"></a> processsession_PostFollows

See processsession Entity [processsession_PostFollows](processsession.md#BKMK_processsession_PostFollows) One-To-Many relationship.

### <a name="BKMK_queue_PostFollows"></a> queue_PostFollows

See queue Entity [queue_PostFollows](queue.md#BKMK_queue_PostFollows) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_PostFollows"></a> knowledgearticle_PostFollows

See knowledgearticle Entity [knowledgearticle_PostFollows](knowledgearticle.md#BKMK_knowledgearticle_PostFollows) One-To-Many relationship.
postfollow

