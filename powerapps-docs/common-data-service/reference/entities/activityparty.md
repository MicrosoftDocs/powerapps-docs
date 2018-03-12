---
title: "ActivityParty Entity Reference (Common Data Service for Apps)| MicrosoftDocs"
description: "Includes schema information and supported messages for the ActivityParty entity."

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
# ActivityParty Entity Reference

Person or group associated with an activity. An activity can have multiple activity parties.

## Entity Properties

**DisplayName**: Activity Party<br />
**DisplayCollectionName**: Activity Parties<br />
**SchemaName**: ActivityParty<br />
**CollectionSchemaName**: ActivityParties<br />
**LogicalName**: activityparty<br />
**LogicalCollectionName**: activityparties<br />
**EntitySetName**: activityparties<br />
**PrimaryIdAttribute**: activitypartyid<br />
**PrimaryNameAttribute**: partyidname<br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ActivityId](#BKMK_ActivityId)
- [ActivityPartyId](#BKMK_ActivityPartyId)
- [AddressUsed](#BKMK_AddressUsed)
- [Effort](#BKMK_Effort)
- [ExchangeEntryId](#BKMK_ExchangeEntryId)
- [ParticipationTypeMask](#BKMK_ParticipationTypeMask)
- [PartyId](#BKMK_PartyId)
- [PartyIdName](#BKMK_PartyIdName)
- [PartyObjectTypeCode](#BKMK_PartyObjectTypeCode)


### <a name="BKMK_ActivityId"></a> ActivityId

**Description**: Unique identifier of the activity associated with the activity party. (A "party" is any person who is associated with an activity.)<br />
**DisplayName**: Activity<br />
**LogicalName**: activityid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: activitypointer


### <a name="BKMK_ActivityPartyId"></a> ActivityPartyId

**Description**: Unique identifier of the activity party.<br />
**DisplayName**: Activity Party<br />
**LogicalName**: activitypartyid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_AddressUsed"></a> AddressUsed

**Description**: Email address to which an email is delivered, and which is associated with the target entity.<br />
**DisplayName**: Address <br />
**LogicalName**: addressused<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_Effort"></a> Effort

**Description**: Amount of effort used by the resource in a service appointment activity.<br />
**DisplayName**: Effort<br />
**LogicalName**: effort<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Double<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0<br />
**Precision**: 2


### <a name="BKMK_ExchangeEntryId"></a> ExchangeEntryId

**Description**: For internal use only.<br />
**DisplayName**: Exchange Entry<br />
**LogicalName**: exchangeentryid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_ParticipationTypeMask"></a> ParticipationTypeMask

**Description**: Role of the person in the activity, such as sender, to, cc, bcc, required, optional, organizer, regarding, or owner.<br />
**DisplayName**: Participation Type<br />
**LogicalName**: participationtypemask<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Sender
- **Value**: 2 **Label**: To Recipient
- **Value**: 3 **Label**: CC Recipient
- **Value**: 4 **Label**: BCC Recipient
- **Value**: 5 **Label**: Required attendee
- **Value**: 6 **Label**: Optional attendee
- **Value**: 7 **Label**: Organizer
- **Value**: 8 **Label**: Regarding
- **Value**: 9 **Label**: Owner
- **Value**: 10 **Label**: Resource
- **Value**: 11 **Label**: Customer



### <a name="BKMK_PartyId"></a> PartyId

**Description**: Unique identifier of the party associated with the activity.<br />
**DisplayName**: Party<br />
**LogicalName**: partyid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: account,contact,knowledgearticle,queue,systemuser


### <a name="BKMK_PartyIdName"></a> PartyIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: partyidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 400


### <a name="BKMK_PartyObjectTypeCode"></a> PartyObjectTypeCode

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: partyobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

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

**Description**: Email address column number from associated party.<br />
**DisplayName**: Email column number of party<br />
**LogicalName**: addressusedemailcolumnnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 1


### <a name="BKMK_DoNotEmail"></a> DoNotEmail

**Description**: Information about whether to allow sending email to the activity party.<br />
**DisplayName**: Do not allow Emails<br />
**LogicalName**: donotemail<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Do Not Allow
- **FalseOption Value**: 0 **Label**: Allow

**DefaultValue**: False


### <a name="BKMK_DoNotFax"></a> DoNotFax

**Description**: Information about whether to allow sending faxes to the activity party.<br />
**DisplayName**: Do not allow Faxes<br />
**LogicalName**: donotfax<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Do Not Allow
- **FalseOption Value**: 0 **Label**: Allow

**DefaultValue**: False


### <a name="BKMK_DoNotPhone"></a> DoNotPhone

**Description**: Information about whether to allow phone calls to the lead.<br />
**DisplayName**: Do not allow Phone Calls<br />
**LogicalName**: donotphone<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Do Not Allow
- **FalseOption Value**: 0 **Label**: Allow

**DefaultValue**: False


### <a name="BKMK_DoNotPostalMail"></a> DoNotPostalMail

**Description**: Information about whether to allow sending postal mail to the lead.<br />
**DisplayName**: Do not allow Postal Mails<br />
**LogicalName**: donotpostalmail<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Do Not Allow
- **FalseOption Value**: 0 **Label**: Allow

**DefaultValue**: False


### <a name="BKMK_InstanceTypeCode"></a> InstanceTypeCode

**Description**: Type of instance of a recurring series.<br />
**DisplayName**: Appointment Type<br />
**LogicalName**: instancetypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Not Recurring
- **Value**: 1 **Label**: Recurring Master
- **Value**: 2 **Label**: Recurring Instance
- **Value**: 3 **Label**: Recurring Exception
- **Value**: 4 **Label**: Recurring Future Exception



### <a name="BKMK_IsPartyDeleted"></a> IsPartyDeleted

**Description**: Information about whether the underlying entity record is deleted.<br />
**DisplayName**: Is Party Deleted<br />
**LogicalName**: ispartydeleted<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Unique identifier of the user or team who owns the activity_party.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ScheduledEnd"></a> ScheduledEnd

**Description**: Scheduled end time of the activity.<br />
**DisplayName**: Scheduled End<br />
**LogicalName**: scheduledend<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_ScheduledStart"></a> ScheduledStart

**Description**: Scheduled start time of the activity.<br />
**DisplayName**: Scheduled Start<br />
**LogicalName**: scheduledstart<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: versionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [userentityinstancedata_activityparty](#BKMK_userentityinstancedata_activityparty)
- [ActivityParty_SyncErrors](#BKMK_ActivityParty_SyncErrors)


### <a name="BKMK_userentityinstancedata_activityparty"></a> userentityinstancedata_activityparty

Same as userentityinstancedata entity [userentityinstancedata_activityparty](userentityinstancedata.md#BKMK_userentityinstancedata_activityparty) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_activityparty<br />
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


### <a name="BKMK_ActivityParty_SyncErrors"></a> ActivityParty_SyncErrors

Same as syncerror entity [ActivityParty_SyncErrors](syncerror.md#BKMK_ActivityParty_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: ActivityParty_SyncErrors<br />
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


### <a name="BKMK_account_activity_parties"></a> account_activity_parties

See account Entity [account_activity_parties](account.md#BKMK_account_activity_parties) One-To-Many relationship.

### <a name="BKMK_letter_activity_parties"></a> letter_activity_parties

See letter Entity [letter_activity_parties](letter.md#BKMK_letter_activity_parties) One-To-Many relationship.

### <a name="BKMK_phonecall_activity_parties"></a> phonecall_activity_parties

See phonecall Entity [phonecall_activity_parties](phonecall.md#BKMK_phonecall_activity_parties) One-To-Many relationship.

### <a name="BKMK_task_activity_parties"></a> task_activity_parties

See task Entity [task_activity_parties](task.md#BKMK_task_activity_parties) One-To-Many relationship.

### <a name="BKMK_recurringappointmentmaster_activity_parties"></a> recurringappointmentmaster_activity_parties

See recurringappointmentmaster Entity [recurringappointmentmaster_activity_parties](recurringappointmentmaster.md#BKMK_recurringappointmentmaster_activity_parties) One-To-Many relationship.

### <a name="BKMK_contact_activity_parties"></a> contact_activity_parties

See contact Entity [contact_activity_parties](contact.md#BKMK_contact_activity_parties) One-To-Many relationship.

### <a name="BKMK_system_user_activity_parties"></a> system_user_activity_parties

See systemuser Entity [system_user_activity_parties](systemuser.md#BKMK_system_user_activity_parties) One-To-Many relationship.

### <a name="BKMK_appointment_activity_parties"></a> appointment_activity_parties

See appointment Entity [appointment_activity_parties](appointment.md#BKMK_appointment_activity_parties) One-To-Many relationship.

### <a name="BKMK_socialactivity_activity_parties"></a> socialactivity_activity_parties

See socialactivity Entity [socialactivity_activity_parties](socialactivity.md#BKMK_socialactivity_activity_parties) One-To-Many relationship.

### <a name="BKMK_queue_activity_parties"></a> queue_activity_parties

See queue Entity [queue_activity_parties](queue.md#BKMK_queue_activity_parties) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_activity_parties"></a> knowledgearticle_activity_parties

See knowledgearticle Entity [knowledgearticle_activity_parties](knowledgearticle.md#BKMK_knowledgearticle_activity_parties) One-To-Many relationship.

### <a name="BKMK_email_activity_parties"></a> email_activity_parties

See email Entity [email_activity_parties](email.md#BKMK_email_activity_parties) One-To-Many relationship.

### <a name="BKMK_fax_activity_parties"></a> fax_activity_parties

See fax Entity [fax_activity_parties](fax.md#BKMK_fax_activity_parties) One-To-Many relationship.

### <a name="BKMK_activitypointer_activity_parties"></a> activitypointer_activity_parties

See activitypointer Entity [activitypointer_activity_parties](activitypointer.md#BKMK_activitypointer_activity_parties) One-To-Many relationship.
activityparty

