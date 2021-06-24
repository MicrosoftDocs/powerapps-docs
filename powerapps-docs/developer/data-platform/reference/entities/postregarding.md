---
title: "PostRegarding table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the PostRegarding table/entity."
ms.date: 03/04/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# PostRegarding table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Represents which object an activity feed post is regarding. For internal use only.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|PostRegardings|
|DisplayCollectionName|Post Regarding|
|DisplayName|Post Regarding|
|EntitySetName|postregardings|
|IsBPFEntity|False|
|LogicalCollectionName|postregardings|
|LogicalName|postregarding|
|OwnershipType|None|
|PrimaryIdAttribute|postregardingid|
|PrimaryNameAttribute||
|SchemaName|PostRegarding|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [PostRegardingId](#BKMK_PostRegardingId)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectOwnerId](#BKMK_RegardingObjectOwnerId)
- [RegardingObjectOwnerIdType](#BKMK_RegardingObjectOwnerIdType)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)


### <a name="BKMK_PostRegardingId"></a> PostRegardingId

|Property|Value|
|--------|-----|
|Description|Shows the ID of the record that the post is referring to.|
|DisplayName|PostRegardingId|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|postregardingid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|--------|-----|
|Description|Choose the record that the post relates to.|
|DisplayName|RegardingObjectId|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|regardingobjectid|
|RequiredLevel|None|
|Targets|account,appointment,contact,externalparty,knowledgearticle,phonecall,processsession,queue,recurringappointmentmaster,systemuser,task,team|
|Type|Lookup|


### <a name="BKMK_RegardingObjectOwnerId"></a> RegardingObjectOwnerId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user or team who owns the regarding object.|
|DisplayName|Owner|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|regardingobjectownerid|
|RequiredLevel|None|
|Targets|systemuser,team|
|Type|Owner|


### <a name="BKMK_RegardingObjectOwnerIdType"></a> RegardingObjectOwnerIdType

|Property|Value|
|--------|-----|
|Description|Type of the RegardingObjectOwnerId|
|DisplayName|RegardingObjectOwnerIdType|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|regardingobjectowneridtype|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|--------|-----|
|Description|Type of the RegardingObject|
|DisplayName|RegardingObjectTypeCode|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|regardingobjecttypecode|
|RequiredLevel|SystemRequired|
|Type|EntityName|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [LatestAutoPostModifiedOn](#BKMK_LatestAutoPostModifiedOn)
- [LatestManualPostModifiedOn](#BKMK_LatestManualPostModifiedOn)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectIdYomiName](#BKMK_RegardingObjectIdYomiName)
- [RegardingObjectOwningBusinessUnit](#BKMK_RegardingObjectOwningBusinessUnit)
- [RegardingObjectTypeCodeForSharing](#BKMK_RegardingObjectTypeCodeForSharing)


### <a name="BKMK_LatestAutoPostModifiedOn"></a> LatestAutoPostModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date of Latest Auto Post on the Regarding entity|
|DisplayName|Latest Auto Post|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|latestautopostmodifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_LatestManualPostModifiedOn"></a> LatestManualPostModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date of Latest Manual Post on the Regarding entity|
|DisplayName|Latest Manual Post|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|latestmanualpostmodifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjectidname|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RegardingObjectIdYomiName"></a> RegardingObjectIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjectidyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RegardingObjectOwningBusinessUnit"></a> RegardingObjectOwningBusinessUnit

|Property|Value|
|--------|-----|
|Description|Select the business unit that owns the regarding object.|
|DisplayName|Regarding object owning Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjectowningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_RegardingObjectTypeCodeForSharing"></a> RegardingObjectTypeCodeForSharing

|Property|Value|
|--------|-----|
|Description|Indicates the entity type of the regarding object for sharing.|
|DisplayName|RegardingObjectTypeCodeForSharing|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjecttypecodeforsharing|
|RequiredLevel|SystemRequired|
|Type|EntityName|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_post_PostRegardings"></a> post_PostRegardings

Same as post table [post_PostRegardings](post.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|post|
|ReferencingAttribute|postregardingid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|post_PostRegardings|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [task_PostRegardings](#BKMK_task_PostRegardings)
- [appointment_PostRegardings](#BKMK_appointment_PostRegardings)
- [phonecall_PostRegardings](#BKMK_phonecall_PostRegardings)
- [recurringappointmentmaster_PostRegardings](#BKMK_recurringappointmentmaster_PostRegardings)
- [knowledgearticle_PostRegardings](#BKMK_knowledgearticle_PostRegardings)
- [processsession_PostRegardings](#BKMK_processsession_PostRegardings)
- [account_PostRegardings](#BKMK_account_PostRegardings)
- [systemuser_PostRegardings](#BKMK_systemuser_PostRegardings)
- [business_unit_PostRegarding](#BKMK_business_unit_PostRegarding)
- [contact_PostRegardings](#BKMK_contact_PostRegardings)
- [team_PostRegardings](#BKMK_team_PostRegardings)
- [queue_PostRegardings](#BKMK_queue_PostRegardings)


### <a name="BKMK_task_PostRegardings"></a> task_PostRegardings

See task Table [task_PostRegardings](task.md) One-To-Many relationship.

### <a name="BKMK_appointment_PostRegardings"></a> appointment_PostRegardings

See appointment Table [appointment_PostRegardings](appointment.md) One-To-Many relationship.

### <a name="BKMK_phonecall_PostRegardings"></a> phonecall_PostRegardings

See phonecall Table [phonecall_PostRegardings](phonecall.md) One-To-Many relationship.

### <a name="BKMK_recurringappointmentmaster_PostRegardings"></a> recurringappointmentmaster_PostRegardings

See recurringappointmentmaster Table [recurringappointmentmaster_PostRegardings](recurringappointmentmaster.md) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_PostRegardings"></a> knowledgearticle_PostRegardings

See knowledgearticle Table [knowledgearticle_PostRegardings](knowledgearticle.md) One-To-Many relationship.

### <a name="BKMK_processsession_PostRegardings"></a> processsession_PostRegardings

See processsession Table [processsession_PostRegardings](processsession.md) One-To-Many relationship.

### <a name="BKMK_account_PostRegardings"></a> account_PostRegardings

See account Table [account_PostRegardings](account.md) One-To-Many relationship.

### <a name="BKMK_systemuser_PostRegardings"></a> systemuser_PostRegardings

See systemuser Table [systemuser_PostRegardings](systemuser.md) One-To-Many relationship.

### <a name="BKMK_business_unit_PostRegarding"></a> business_unit_PostRegarding

See businessunit Table [business_unit_PostRegarding](businessunit.md) One-To-Many relationship.

### <a name="BKMK_contact_PostRegardings"></a> contact_PostRegardings

See contact Table [contact_PostRegardings](contact.md) One-To-Many relationship.

### <a name="BKMK_team_PostRegardings"></a> team_PostRegardings

See team Table [team_PostRegardings](team.md) One-To-Many relationship.

### <a name="BKMK_queue_PostRegardings"></a> queue_PostRegardings

See queue Table [queue_PostRegardings](queue.md) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.postregarding?text=postregarding EntityType" />