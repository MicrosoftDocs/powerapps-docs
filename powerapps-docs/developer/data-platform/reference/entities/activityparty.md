---
title: "Activity Party (ActivityParty) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Activity Party (ActivityParty) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Activity Party (ActivityParty) table/entity reference (Microsoft Dataverse)

Person or group associated with an activity. An activity can have multiple activity parties.

## Messages

The following table lists the messages for the Activity Party (ActivityParty) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `AppendRelatedParty`<br />Event: True |**AppendRelatedParty action** |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `RetrieveMultiple`<br />Event: True |`GET` /activityparties<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Activity Party (ActivityParty) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Activity Party** |
| **DisplayCollectionName** | **Activity Parties** |
| **SchemaName** | `ActivityParty` |
| **CollectionSchemaName** | `ActivityParties` |
| **EntitySetName** | `activityparties`|
| **LogicalName** | `activityparty` |
| **LogicalCollectionName** | `activityparties` |
| **PrimaryIdAttribute** | `activitypartyid` |
| **PrimaryNameAttribute** |`partyidname` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ActivityId](#BKMK_ActivityId)
- [ActivityPartyId](#BKMK_ActivityPartyId)
- [AddressUsed](#BKMK_AddressUsed)
- [Effort](#BKMK_Effort)
- [ExchangeEntryId](#BKMK_ExchangeEntryId)
- [ExternalId](#BKMK_ExternalId)
- [ExternalIdType](#BKMK_ExternalIdType)
- [ParticipationTypeMask](#BKMK_ParticipationTypeMask)
- [PartyId](#BKMK_PartyId)
- [PartyObjectTypeCode](#BKMK_PartyObjectTypeCode)
- [UnresolvedPartyName](#BKMK_UnresolvedPartyName)

### <a name="BKMK_ActivityId"></a> ActivityId

|Property|Value|
|---|---|
|Description|**Unique identifier of the activity associated with the activity party. (A "party" is any person who is associated with an activity.)**|
|DisplayName|**Activity**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`activityid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|activitypointer|

### <a name="BKMK_ActivityPartyId"></a> ActivityPartyId

|Property|Value|
|---|---|
|Description|**Unique identifier of the activity party.**|
|DisplayName|**Activity Party**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`activitypartyid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_AddressUsed"></a> AddressUsed

|Property|Value|
|---|---|
|Description|**Email address to which an email is delivered, and which is associated with the target entity.**|
|DisplayName|**Address**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`addressused`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|320|

### <a name="BKMK_Effort"></a> Effort

|Property|Value|
|---|---|
|Description|**Amount of effort used by the resource in a service appointment activity.**|
|DisplayName|**Effort**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`effort`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Disabled|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|

### <a name="BKMK_ExchangeEntryId"></a> ExchangeEntryId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Exchange Entry**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`exchangeentryid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_ExternalId"></a> ExternalId

|Property|Value|
|---|---|
|Description|**The external id used when the party does not have an email address.**|
|DisplayName|**External Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`externalid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_ExternalIdType"></a> ExternalIdType

|Property|Value|
|---|---|
|Description|**The external id type used when the party does not have an email address.**|
|DisplayName|**External Id Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`externalidtype`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_ParticipationTypeMask"></a> ParticipationTypeMask

|Property|Value|
|---|---|
|Description|**Role of the person in the activity, such as sender, to, cc, bcc, required, optional, organizer, regarding, or owner.**|
|DisplayName|**Participation Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`participationtypemask`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`activityparty_participationtypemask`|

#### ParticipationTypeMask Choices/Options

|Value|Label|
|---|---|
|1|**Sender**|
|2|**To Recipient**|
|3|**CC Recipient**|
|4|**BCC Recipient**|
|5|**Required attendee**|
|6|**Optional attendee**|
|7|**Organizer**|
|8|**Regarding**|
|9|**Owner**|
|10|**Resource**|
|11|**Customer**|
|12|**Chat Participant**|
|13|**Related**|

### <a name="BKMK_PartyId"></a> PartyId

|Property|Value|
|---|---|
|Description|**Unique identifier of the party associated with the activity.**|
|DisplayName|**Party**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`partyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account, contact, knowledgearticle, queue, systemuser|

### <a name="BKMK_PartyObjectTypeCode"></a> PartyObjectTypeCode

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`partyobjecttypecode`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_UnresolvedPartyName"></a> UnresolvedPartyName

|Property|Value|
|---|---|
|Description|**The name of the party to be used when the party is not resolved to an entity.**|
|DisplayName|**Unresolved Party Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`unresolvedpartyname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

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
|---|---|
|Description|**Email address column number from associated party.**|
|DisplayName|**Email column number of party**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`addressusedemailcolumnnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|1|

### <a name="BKMK_DoNotEmail"></a> DoNotEmail

|Property|Value|
|---|---|
|Description|**Information about whether to allow sending email to the activity party.**|
|DisplayName|**Do not allow Emails**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`donotemail`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`activityparty_donotemail`|
|DefaultValue|False|
|True Label|Do Not Allow|
|False Label|Allow|

### <a name="BKMK_DoNotFax"></a> DoNotFax

|Property|Value|
|---|---|
|Description|**Information about whether to allow sending faxes to the activity party.**|
|DisplayName|**Do not allow Faxes**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`donotfax`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`activityparty_donotfax`|
|DefaultValue|False|
|True Label|Do Not Allow|
|False Label|Allow|

### <a name="BKMK_DoNotPhone"></a> DoNotPhone

|Property|Value|
|---|---|
|Description|**Information about whether to allow phone calls to the lead.**|
|DisplayName|**Do not allow Phone Calls**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`donotphone`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`activityparty_donotphone`|
|DefaultValue|False|
|True Label|Do Not Allow|
|False Label|Allow|

### <a name="BKMK_DoNotPostalMail"></a> DoNotPostalMail

|Property|Value|
|---|---|
|Description|**Information about whether to allow sending postal mail to the lead.**|
|DisplayName|**Do not allow Postal Mails**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`donotpostalmail`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`activityparty_donotpostalmail`|
|DefaultValue|False|
|True Label|Do Not Allow|
|False Label|Allow|

### <a name="BKMK_InstanceTypeCode"></a> InstanceTypeCode

|Property|Value|
|---|---|
|Description|**Type of instance of a recurring series.**|
|DisplayName|**Appointment Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`instancetypecode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`activityparty_instancetypecode`|

#### InstanceTypeCode Choices/Options

|Value|Label|
|---|---|
|0|**Not Recurring**|
|1|**Recurring Master**|
|2|**Recurring Instance**|
|3|**Recurring Exception**|
|4|**Recurring Future Exception**|

### <a name="BKMK_IsPartyDeleted"></a> IsPartyDeleted

|Property|Value|
|---|---|
|Description|**Information about whether the underlying entity record is deleted.**|
|DisplayName|**Is Party Deleted**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ispartydeleted`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`activityparty_ispartydeleted`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user or team who owns the activity\_party.**|
|DisplayName|**Owner**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|ApplicationRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ScheduledEnd"></a> ScheduledEnd

|Property|Value|
|---|---|
|Description|**Scheduled end time of the activity.**|
|DisplayName|**Scheduled End**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`scheduledend`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ScheduledStart"></a> ScheduledStart

|Property|Value|
|---|---|
|Description|**Scheduled start time of the activity.**|
|DisplayName|**Scheduled Start**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`scheduledstart`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

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

- [account_activity_parties](#BKMK_account_activity_parties)
- [activitypointer_activity_parties](#BKMK_activitypointer_activity_parties)
- [adx_inviteredemption_activity_parties](#BKMK_adx_inviteredemption_activity_parties)
- [adx_portalcomment_activity_parties](#BKMK_adx_portalcomment_activity_parties)
- [appointment_activity_parties](#BKMK_appointment_activity_parties)
- [chat_activity_parties](#BKMK_chat_activity_parties)
- [contact_activity_parties](#BKMK_contact_activity_parties)
- [email_activity_parties](#BKMK_email_activity_parties)
- [fax_activity_parties](#BKMK_fax_activity_parties)
- [knowledgearticle_activity_parties](#BKMK_knowledgearticle_activity_parties)
- [letter_activity_parties](#BKMK_letter_activity_parties)
- [phonecall_activity_parties](#BKMK_phonecall_activity_parties)
- [queue_activity_parties](#BKMK_queue_activity_parties)
- [recurringappointmentmaster_activity_parties](#BKMK_recurringappointmentmaster_activity_parties)
- [socialactivity_activity_parties](#BKMK_socialactivity_activity_parties)
- [system_user_activity_parties](#BKMK_system_user_activity_parties)
- [task_activity_parties](#BKMK_task_activity_parties)

### <a name="BKMK_account_activity_parties"></a> account_activity_parties

One-To-Many Relationship: [account account_activity_parties](account.md#BKMK_account_activity_parties)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`partyid`|
|ReferencingEntityNavigationPropertyName|`partyid_account`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_activitypointer_activity_parties"></a> activitypointer_activity_parties

One-To-Many Relationship: [activitypointer activitypointer_activity_parties](activitypointer.md#BKMK_activitypointer_activity_parties)

|Property|Value|
|---|---|
|ReferencedEntity|`activitypointer`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`activityid`|
|ReferencingEntityNavigationPropertyName|`activityid_activitypointer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_inviteredemption_activity_parties"></a> adx_inviteredemption_activity_parties

One-To-Many Relationship: [adx_inviteredemption adx_inviteredemption_activity_parties](adx_inviteredemption.md#BKMK_adx_inviteredemption_activity_parties)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_inviteredemption`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`activityid`|
|ReferencingEntityNavigationPropertyName|`activityid_adx_inviteredemption_activityparty`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_portalcomment_activity_parties"></a> adx_portalcomment_activity_parties

One-To-Many Relationship: [adx_portalcomment adx_portalcomment_activity_parties](adx_portalcomment.md#BKMK_adx_portalcomment_activity_parties)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_portalcomment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`activityid`|
|ReferencingEntityNavigationPropertyName|`activityid_adx_portalcomment_activityparty`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appointment_activity_parties"></a> appointment_activity_parties

One-To-Many Relationship: [appointment appointment_activity_parties](appointment.md#BKMK_appointment_activity_parties)

|Property|Value|
|---|---|
|ReferencedEntity|`appointment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`activityid`|
|ReferencingEntityNavigationPropertyName|`activityid_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_chat_activity_parties"></a> chat_activity_parties

One-To-Many Relationship: [chat chat_activity_parties](chat.md#BKMK_chat_activity_parties)

|Property|Value|
|---|---|
|ReferencedEntity|`chat`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`activityid`|
|ReferencingEntityNavigationPropertyName|`activityid_chat_activityparty`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_contact_activity_parties"></a> contact_activity_parties

One-To-Many Relationship: [contact contact_activity_parties](contact.md#BKMK_contact_activity_parties)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`partyid`|
|ReferencingEntityNavigationPropertyName|`partyid_contact`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_email_activity_parties"></a> email_activity_parties

One-To-Many Relationship: [email email_activity_parties](email.md#BKMK_email_activity_parties)

|Property|Value|
|---|---|
|ReferencedEntity|`email`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`activityid`|
|ReferencingEntityNavigationPropertyName|`activityid_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fax_activity_parties"></a> fax_activity_parties

One-To-Many Relationship: [fax fax_activity_parties](fax.md#BKMK_fax_activity_parties)

|Property|Value|
|---|---|
|ReferencedEntity|`fax`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`activityid`|
|ReferencingEntityNavigationPropertyName|`activityid_fax`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgearticle_activity_parties"></a> knowledgearticle_activity_parties

One-To-Many Relationship: [knowledgearticle knowledgearticle_activity_parties](knowledgearticle.md#BKMK_knowledgearticle_activity_parties)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`partyid`|
|ReferencingEntityNavigationPropertyName|`partyid_knowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_letter_activity_parties"></a> letter_activity_parties

One-To-Many Relationship: [letter letter_activity_parties](letter.md#BKMK_letter_activity_parties)

|Property|Value|
|---|---|
|ReferencedEntity|`letter`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`activityid`|
|ReferencingEntityNavigationPropertyName|`activityid_letter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_phonecall_activity_parties"></a> phonecall_activity_parties

One-To-Many Relationship: [phonecall phonecall_activity_parties](phonecall.md#BKMK_phonecall_activity_parties)

|Property|Value|
|---|---|
|ReferencedEntity|`phonecall`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`activityid`|
|ReferencingEntityNavigationPropertyName|`activityid_phonecall`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_queue_activity_parties"></a> queue_activity_parties

One-To-Many Relationship: [queue queue_activity_parties](queue.md#BKMK_queue_activity_parties)

|Property|Value|
|---|---|
|ReferencedEntity|`queue`|
|ReferencedAttribute|`queueid`|
|ReferencingAttribute|`partyid`|
|ReferencingEntityNavigationPropertyName|`partyid_queue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recurringappointmentmaster_activity_parties"></a> recurringappointmentmaster_activity_parties

One-To-Many Relationship: [recurringappointmentmaster recurringappointmentmaster_activity_parties](recurringappointmentmaster.md#BKMK_recurringappointmentmaster_activity_parties)

|Property|Value|
|---|---|
|ReferencedEntity|`recurringappointmentmaster`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`activityid`|
|ReferencingEntityNavigationPropertyName|`activityid_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_socialactivity_activity_parties"></a> socialactivity_activity_parties

One-To-Many Relationship: [socialactivity socialactivity_activity_parties](socialactivity.md#BKMK_socialactivity_activity_parties)

|Property|Value|
|---|---|
|ReferencedEntity|`socialactivity`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`activityid`|
|ReferencingEntityNavigationPropertyName|`activityid_socialactivity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_system_user_activity_parties"></a> system_user_activity_parties

One-To-Many Relationship: [systemuser system_user_activity_parties](systemuser.md#BKMK_system_user_activity_parties)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`partyid`|
|ReferencingEntityNavigationPropertyName|`partyid_systemuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_task_activity_parties"></a> task_activity_parties

One-To-Many Relationship: [task task_activity_parties](task.md#BKMK_task_activity_parties)

|Property|Value|
|---|---|
|ReferencedEntity|`task`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`activityid`|
|ReferencingEntityNavigationPropertyName|`activityid_task`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_ActivityParty_SyncErrors"></a> ActivityParty_SyncErrors

Many-To-One Relationship: [syncerror ActivityParty_SyncErrors](syncerror.md#BKMK_ActivityParty_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`ActivityParty_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.activityparty?displayProperty=fullName>
