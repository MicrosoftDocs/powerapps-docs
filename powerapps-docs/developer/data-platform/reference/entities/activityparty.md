---
title: "ActivityParty table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the ActivityParty table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# ActivityParty table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Person or group associated with an activity. An activity can have multiple activity parties.


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|RetrieveMultiple|GET /activityparties<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|ActivityParties|
|DisplayCollectionName|Activity Parties|
|DisplayName|Activity Party|
|EntitySetName|activityparties|
|IsBPFEntity|False|
|LogicalCollectionName|activityparties|
|LogicalName|activityparty|
|OwnershipType|None|
|PrimaryIdAttribute|activitypartyid|
|PrimaryNameAttribute|partyidname|
|SchemaName|ActivityParty|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ActivityId](#BKMK_ActivityId)
- [ActivityPartyId](#BKMK_ActivityPartyId)
- [AddressUsed](#BKMK_AddressUsed)
- [Effort](#BKMK_Effort)
- [ExchangeEntryId](#BKMK_ExchangeEntryId)
- [ParticipationTypeMask](#BKMK_ParticipationTypeMask)
- [PartyId](#BKMK_PartyId)
- [PartyIdName](#BKMK_PartyIdName)
- [PartyObjectTypeCode](#BKMK_PartyObjectTypeCode)
- [UnresolvedPartyName](#BKMK_UnresolvedPartyName)


### <a name="BKMK_ActivityId"></a> ActivityId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the activity associated with the activity party. (A "party" is any person who is associated with an activity.)|
|DisplayName|Activity|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|activityid|
|RequiredLevel|SystemRequired|
|Targets|activitypointer|
|Type|Lookup|


### <a name="BKMK_ActivityPartyId"></a> ActivityPartyId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the activity party.|
|DisplayName|Activity Party|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|activitypartyid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_AddressUsed"></a> AddressUsed

|Property|Value|
|--------|-----|
|Description|Email address to which an email is delivered, and which is associated with the target entity.|
|DisplayName|Address |
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|addressused|
|MaxLength|320|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Effort"></a> Effort

|Property|Value|
|--------|-----|
|Description|Amount of effort used by the resource in a service appointment activity.|
|DisplayName|Effort|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|effort|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|
|RequiredLevel|None|
|Type|Double|


### <a name="BKMK_ExchangeEntryId"></a> ExchangeEntryId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Exchange Entry|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|exchangeentryid|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ParticipationTypeMask"></a> ParticipationTypeMask

|Property|Value|
|--------|-----|
|Description|Role of the person in the activity, such as sender, to, cc, bcc, required, optional, organizer, regarding, or owner.|
|DisplayName|Participation Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|participationtypemask|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ParticipationTypeMask Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Sender||
|2|To Recipient||
|3|CC Recipient||
|4|BCC Recipient||
|5|Required attendee||
|6|Optional attendee||
|7|Organizer||
|8|Regarding||
|9|Owner||
|10|Resource||
|11|Customer||
|12|Chat Participant||



### <a name="BKMK_PartyId"></a> PartyId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the party associated with the activity.|
|DisplayName|Party|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|partyid|
|RequiredLevel|None|
|Targets|account,contact,knowledgearticle,queue,systemuser|
|Type|Lookup|


### <a name="BKMK_PartyIdName"></a> PartyIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|partyidname|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PartyObjectTypeCode"></a> PartyObjectTypeCode

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|partyobjecttypecode|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_UnresolvedPartyName"></a> UnresolvedPartyName

**Added by**: msft_ActivitiesInfra_Extensions Solution

|Property|Value|
|--------|-----|
|Description|The name of the party to be used when the party is not resolved to an entity.|
|DisplayName|Unresolved Party Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|unresolvedpartyname|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AddressUsedEmailColumnNumber](#BKMK_AddressUsedEmailColumnNumber)
- [DoNotEmail](#BKMK_DoNotEmail)
- [DoNotFax](#BKMK_DoNotFax)
- [DoNotPhone](#BKMK_DoNotPhone)
- [DoNotPostalMail](#BKMK_DoNotPostalMail)
- [InstanceTypeCode](#BKMK_InstanceTypeCode)
- [IsPartyDeleted](#BKMK_IsPartyDeleted)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningUser](#BKMK_OwningUser)
- [ScheduledEnd](#BKMK_ScheduledEnd)
- [ScheduledStart](#BKMK_ScheduledStart)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_AddressUsedEmailColumnNumber"></a> AddressUsedEmailColumnNumber

|Property|Value|
|--------|-----|
|Description|Email address column number from associated party.|
|DisplayName|Email column number of party|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|addressusedemailcolumnnumber|
|MaxValue|2147483647|
|MinValue|1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_DoNotEmail"></a> DoNotEmail

|Property|Value|
|--------|-----|
|Description|Information about whether to allow sending email to the activity party.|
|DisplayName|Do not allow Emails|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|donotemail|
|RequiredLevel|None|
|Type|Boolean|

#### DoNotEmail Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Do Not Allow||
|0|Allow||

**DefaultValue**: 0



### <a name="BKMK_DoNotFax"></a> DoNotFax

|Property|Value|
|--------|-----|
|Description|Information about whether to allow sending faxes to the activity party.|
|DisplayName|Do not allow Faxes|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|donotfax|
|RequiredLevel|None|
|Type|Boolean|

#### DoNotFax Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Do Not Allow||
|0|Allow||

**DefaultValue**: 0



### <a name="BKMK_DoNotPhone"></a> DoNotPhone

|Property|Value|
|--------|-----|
|Description|Information about whether to allow phone calls to the lead.|
|DisplayName|Do not allow Phone Calls|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|donotphone|
|RequiredLevel|None|
|Type|Boolean|

#### DoNotPhone Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Do Not Allow||
|0|Allow||

**DefaultValue**: 0



### <a name="BKMK_DoNotPostalMail"></a> DoNotPostalMail

|Property|Value|
|--------|-----|
|Description|Information about whether to allow sending postal mail to the lead.|
|DisplayName|Do not allow Postal Mails|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|donotpostalmail|
|RequiredLevel|None|
|Type|Boolean|

#### DoNotPostalMail Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Do Not Allow||
|0|Allow||

**DefaultValue**: 0



### <a name="BKMK_InstanceTypeCode"></a> InstanceTypeCode

|Property|Value|
|--------|-----|
|Description|Type of instance of a recurring series.|
|DisplayName|Appointment Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|instancetypecode|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### InstanceTypeCode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Not Recurring||
|1|Recurring Master||
|2|Recurring Instance||
|3|Recurring Exception||
|4|Recurring Future Exception||



### <a name="BKMK_IsPartyDeleted"></a> IsPartyDeleted

|Property|Value|
|--------|-----|
|Description|Information about whether the underlying entity record is deleted.|
|DisplayName|Is Party Deleted|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ispartydeleted|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsPartyDeleted Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user or team who owns the activity_party.|
|DisplayName|Owner|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|ApplicationRequired|
|Targets|systemuser,team|
|Type|Owner|


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|owninguser|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_ScheduledEnd"></a> ScheduledEnd

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Scheduled end time of the activity.|
|DisplayName|Scheduled End|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|scheduledend|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ScheduledStart"></a> ScheduledStart

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Scheduled start time of the activity.|
|DisplayName|Scheduled Start|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|scheduledstart|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_ActivityParty_SyncErrors"></a> ActivityParty_SyncErrors

Same as the [ActivityParty_SyncErrors](syncerror.md#BKMK_ActivityParty_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|ActivityParty_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [account_activity_parties](#BKMK_account_activity_parties)
- [letter_activity_parties](#BKMK_letter_activity_parties)
- [phonecall_activity_parties](#BKMK_phonecall_activity_parties)
- [task_activity_parties](#BKMK_task_activity_parties)
- [recurringappointmentmaster_activity_parties](#BKMK_recurringappointmentmaster_activity_parties)
- [contact_activity_parties](#BKMK_contact_activity_parties)
- [system_user_activity_parties](#BKMK_system_user_activity_parties)
- [appointment_activity_parties](#BKMK_appointment_activity_parties)
- [socialactivity_activity_parties](#BKMK_socialactivity_activity_parties)
- [queue_activity_parties](#BKMK_queue_activity_parties)
- [knowledgearticle_activity_parties](#BKMK_knowledgearticle_activity_parties)
- [email_activity_parties](#BKMK_email_activity_parties)
- [fax_activity_parties](#BKMK_fax_activity_parties)
- [activitypointer_activity_parties](#BKMK_activitypointer_activity_parties)
- [chat_activity_parties](#BKMK_chat_activity_parties)


### <a name="BKMK_account_activity_parties"></a> account_activity_parties

See the [account_activity_parties](account.md#BKMK_account_activity_parties) one-to-many relationship for the [account](account.md) table/entity.

### <a name="BKMK_letter_activity_parties"></a> letter_activity_parties

See the [letter_activity_parties](letter.md#BKMK_letter_activity_parties) one-to-many relationship for the [letter](letter.md) table/entity.

### <a name="BKMK_phonecall_activity_parties"></a> phonecall_activity_parties

See the [phonecall_activity_parties](phonecall.md#BKMK_phonecall_activity_parties) one-to-many relationship for the [phonecall](phonecall.md) table/entity.

### <a name="BKMK_task_activity_parties"></a> task_activity_parties

See the [task_activity_parties](task.md#BKMK_task_activity_parties) one-to-many relationship for the [task](task.md) table/entity.

### <a name="BKMK_recurringappointmentmaster_activity_parties"></a> recurringappointmentmaster_activity_parties

See the [recurringappointmentmaster_activity_parties](recurringappointmentmaster.md#BKMK_recurringappointmentmaster_activity_parties) one-to-many relationship for the [recurringappointmentmaster](recurringappointmentmaster.md) table/entity.

### <a name="BKMK_contact_activity_parties"></a> contact_activity_parties

See the [contact_activity_parties](contact.md#BKMK_contact_activity_parties) one-to-many relationship for the [contact](contact.md) table/entity.

### <a name="BKMK_system_user_activity_parties"></a> system_user_activity_parties

See the [system_user_activity_parties](systemuser.md#BKMK_system_user_activity_parties) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_appointment_activity_parties"></a> appointment_activity_parties

See the [appointment_activity_parties](appointment.md#BKMK_appointment_activity_parties) one-to-many relationship for the [appointment](appointment.md) table/entity.

### <a name="BKMK_socialactivity_activity_parties"></a> socialactivity_activity_parties

See the [socialactivity_activity_parties](socialactivity.md#BKMK_socialactivity_activity_parties) one-to-many relationship for the [socialactivity](socialactivity.md) table/entity.

### <a name="BKMK_queue_activity_parties"></a> queue_activity_parties

See the [queue_activity_parties](queue.md#BKMK_queue_activity_parties) one-to-many relationship for the [queue](queue.md) table/entity.

### <a name="BKMK_knowledgearticle_activity_parties"></a> knowledgearticle_activity_parties

See the [knowledgearticle_activity_parties](knowledgearticle.md#BKMK_knowledgearticle_activity_parties) one-to-many relationship for the [knowledgearticle](knowledgearticle.md) table/entity.

### <a name="BKMK_email_activity_parties"></a> email_activity_parties

See the [email_activity_parties](email.md#BKMK_email_activity_parties) one-to-many relationship for the [email](email.md) table/entity.

### <a name="BKMK_fax_activity_parties"></a> fax_activity_parties

See the [fax_activity_parties](fax.md#BKMK_fax_activity_parties) one-to-many relationship for the [fax](fax.md) table/entity.

### <a name="BKMK_activitypointer_activity_parties"></a> activitypointer_activity_parties

See the [activitypointer_activity_parties](activitypointer.md#BKMK_activitypointer_activity_parties) one-to-many relationship for the [activitypointer](activitypointer.md) table/entity.

### <a name="BKMK_chat_activity_parties"></a> chat_activity_parties

**Added by**: Activities Patch Solution

See the [chat_activity_parties](chat.md#BKMK_chat_activity_parties) one-to-many relationship for the [chat](chat.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.activityparty?text=activityparty EntityType" />