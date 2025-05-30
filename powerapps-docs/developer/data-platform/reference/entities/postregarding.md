---
title: "Post Regarding (PostRegarding) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Post Regarding (PostRegarding) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Post Regarding (PostRegarding) table/entity reference (Microsoft Dataverse)

Represents which object an activity feed post is regarding. For internal use only.

## Messages

The following table lists the messages for the Post Regarding (PostRegarding) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|

## Properties

The following table lists selected properties for the Post Regarding (PostRegarding) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Post Regarding** |
| **DisplayCollectionName** | **Post Regarding** |
| **SchemaName** | `PostRegarding` |
| **CollectionSchemaName** | `PostRegardings` |
| **EntitySetName** | `postregardings`|
| **LogicalName** | `postregarding` |
| **LogicalCollectionName** | `postregardings` |
| **PrimaryIdAttribute** | `postregardingid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [PostRegardingId](#BKMK_PostRegardingId)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectOwnerId](#BKMK_RegardingObjectOwnerId)
- [RegardingObjectOwnerIdType](#BKMK_RegardingObjectOwnerIdType)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)

### <a name="BKMK_PostRegardingId"></a> PostRegardingId

|Property|Value|
|---|---|
|Description|**Shows the ID of the record that the post is referring to.**|
|DisplayName|**PostRegardingId**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`postregardingid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**Choose the record that the post relates to.**|
|DisplayName|**RegardingObjectId**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account, appointment, contact, externalparty, knowledgearticle, phonecall, processsession, queue, recurringappointmentmaster, systemuser, task, team|

### <a name="BKMK_RegardingObjectOwnerId"></a> RegardingObjectOwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user or team who owns the regarding object.**|
|DisplayName|**Owner**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjectownerid`|
|RequiredLevel|None|
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

### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|---|---|
|Description|**Type of the RegardingObject**|
|DisplayName|**RegardingObjectTypeCode**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjecttypecode`|
|RequiredLevel|SystemRequired|
|Type|EntityName|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [LatestAutoPostModifiedOn](#BKMK_LatestAutoPostModifiedOn)
- [LatestManualPostModifiedOn](#BKMK_LatestManualPostModifiedOn)
- [RegardingObjectOwningBusinessUnit](#BKMK_RegardingObjectOwningBusinessUnit)
- [RegardingObjectTypeCodeForSharing](#BKMK_RegardingObjectTypeCodeForSharing)

### <a name="BKMK_LatestAutoPostModifiedOn"></a> LatestAutoPostModifiedOn

|Property|Value|
|---|---|
|Description|**Date of Latest Auto Post on the Regarding entity**|
|DisplayName|**Latest Auto Post**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`latestautopostmodifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_LatestManualPostModifiedOn"></a> LatestManualPostModifiedOn

|Property|Value|
|---|---|
|Description|**Date of Latest Manual Post on the Regarding entity**|
|DisplayName|**Latest Manual Post**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`latestmanualpostmodifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_RegardingObjectOwningBusinessUnit"></a> RegardingObjectOwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Select the business unit that owns the regarding object.**|
|DisplayName|**Regarding object owning Business Unit**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjectowningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_RegardingObjectTypeCodeForSharing"></a> RegardingObjectTypeCodeForSharing

|Property|Value|
|---|---|
|Description|**Indicates the entity type of the regarding object for sharing.**|
|DisplayName|**RegardingObjectTypeCodeForSharing**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjecttypecodeforsharing`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [account_PostRegardings](#BKMK_account_PostRegardings)
- [appointment_PostRegardings](#BKMK_appointment_PostRegardings)
- [business_unit_PostRegarding](#BKMK_business_unit_PostRegarding)
- [contact_PostRegardings](#BKMK_contact_PostRegardings)
- [knowledgearticle_PostRegardings](#BKMK_knowledgearticle_PostRegardings)
- [phonecall_PostRegardings](#BKMK_phonecall_PostRegardings)
- [processsession_PostRegardings](#BKMK_processsession_PostRegardings)
- [queue_PostRegardings](#BKMK_queue_PostRegardings)
- [recurringappointmentmaster_PostRegardings](#BKMK_recurringappointmentmaster_PostRegardings)
- [systemuser_PostRegardings](#BKMK_systemuser_PostRegardings)
- [task_PostRegardings](#BKMK_task_PostRegardings)
- [team_PostRegardings](#BKMK_team_PostRegardings)

### <a name="BKMK_account_PostRegardings"></a> account_PostRegardings

One-To-Many Relationship: [account account_PostRegardings](account.md#BKMK_account_PostRegardings)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_account`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appointment_PostRegardings"></a> appointment_PostRegardings

One-To-Many Relationship: [appointment appointment_PostRegardings](appointment.md#BKMK_appointment_PostRegardings)

|Property|Value|
|---|---|
|ReferencedEntity|`appointment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_business_unit_PostRegarding"></a> business_unit_PostRegarding

One-To-Many Relationship: [businessunit business_unit_PostRegarding](businessunit.md#BKMK_business_unit_PostRegarding)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`regardingobjectowningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`regardingobjectowningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_contact_PostRegardings"></a> contact_PostRegardings

One-To-Many Relationship: [contact contact_PostRegardings](contact.md#BKMK_contact_PostRegardings)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_contact`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgearticle_PostRegardings"></a> knowledgearticle_PostRegardings

One-To-Many Relationship: [knowledgearticle knowledgearticle_PostRegardings](knowledgearticle.md#BKMK_knowledgearticle_PostRegardings)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_phonecall_PostRegardings"></a> phonecall_PostRegardings

One-To-Many Relationship: [phonecall phonecall_PostRegardings](phonecall.md#BKMK_phonecall_PostRegardings)

|Property|Value|
|---|---|
|ReferencedEntity|`phonecall`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_phonecall`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_processsession_PostRegardings"></a> processsession_PostRegardings

One-To-Many Relationship: [processsession processsession_PostRegardings](processsession.md#BKMK_processsession_PostRegardings)

|Property|Value|
|---|---|
|ReferencedEntity|`processsession`|
|ReferencedAttribute|`processsessionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_processsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_queue_PostRegardings"></a> queue_PostRegardings

One-To-Many Relationship: [queue queue_PostRegardings](queue.md#BKMK_queue_PostRegardings)

|Property|Value|
|---|---|
|ReferencedEntity|`queue`|
|ReferencedAttribute|`queueid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_queue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recurringappointmentmaster_PostRegardings"></a> recurringappointmentmaster_PostRegardings

One-To-Many Relationship: [recurringappointmentmaster recurringappointmentmaster_PostRegardings](recurringappointmentmaster.md#BKMK_recurringappointmentmaster_PostRegardings)

|Property|Value|
|---|---|
|ReferencedEntity|`recurringappointmentmaster`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_systemuser_PostRegardings"></a> systemuser_PostRegardings

One-To-Many Relationship: [systemuser systemuser_PostRegardings](systemuser.md#BKMK_systemuser_PostRegardings)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_systemuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_task_PostRegardings"></a> task_PostRegardings

One-To-Many Relationship: [task task_PostRegardings](task.md#BKMK_task_PostRegardings)

|Property|Value|
|---|---|
|ReferencedEntity|`task`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_task`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_PostRegardings"></a> team_PostRegardings

One-To-Many Relationship: [team team_PostRegardings](team.md#BKMK_team_PostRegardings)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_team`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_post_PostRegardings"></a> post_PostRegardings

Many-To-One Relationship: [post post_PostRegardings](post.md#BKMK_post_PostRegardings)

|Property|Value|
|---|---|
|ReferencingEntity|`post`|
|ReferencingAttribute|`postregardingid`|
|ReferencedEntityNavigationPropertyName|`post_PostRegardings`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.postregarding?displayProperty=fullName>
