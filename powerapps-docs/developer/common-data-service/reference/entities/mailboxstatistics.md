---
title: "MailboxStatistics Entity Reference (Common Data Service for Apps)| MicrosoftDocs"
description: "Includes schema information and supported messages for the MailboxStatistics entity."

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
# MailboxStatistics Entity Reference

Stores data regarding Mailbox processing cycles

## Entity Properties

**DisplayName**: Mailbox Statistics<br />
**DisplayCollectionName**: Mailbox Statistics<br />
**SchemaName**: MailboxStatistics<br />
**CollectionSchemaName**: MailboxStatistics<br />
**LogicalName**: mailboxstatistics<br />
**LogicalCollectionName**: mailboxstatistics<br />
**EntitySetName**: mailboxstatistics<br />
**PrimaryIdAttribute**: mailboxstatisticsid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AsyncEventId](#BKMK_AsyncEventId)
- [CrmItemsBacklog](#BKMK_CrmItemsBacklog)
- [IndividualStepDurations](#BKMK_IndividualStepDurations)
- [ItemsFailed](#BKMK_ItemsFailed)
- [ItemsProcessed](#BKMK_ItemsProcessed)
- [MachineName](#BKMK_MachineName)
- [MailboxId](#BKMK_MailboxId)
- [MailboxProcessCompletedOn](#BKMK_MailboxProcessCompletedOn)
- [MailboxProcessScheduledOn](#BKMK_MailboxProcessScheduledOn)
- [MailboxProcessStartedOn](#BKMK_MailboxProcessStartedOn)
- [MailboxStatisticsId](#BKMK_MailboxStatisticsId)
- [OperationTypeId](#BKMK_OperationTypeId)
- [OrganizationId](#BKMK_OrganizationId)
- [ProcessResult](#BKMK_ProcessResult)
- [ProcessTimeIntervalInMinutes](#BKMK_ProcessTimeIntervalInMinutes)
- [ScheduledTimeIntervalInMinutes](#BKMK_ScheduledTimeIntervalInMinutes)


### <a name="BKMK_AsyncEventId"></a> AsyncEventId

**Description**: For internal use only.<br />
**DisplayName**: Async Event Id<br />
**LogicalName**: asynceventid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_CrmItemsBacklog"></a> CrmItemsBacklog

**Description**: Items remaining in CRM to process after this synchronization cycle.<br />
**DisplayName**: Items in CRM Left to Process<br />
**LogicalName**: crmitemsbacklog<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_IndividualStepDurations"></a> IndividualStepDurations

**Description**: Time each exchange sync step is taking<br />
**DisplayName**: Individual Step Durations<br />
**LogicalName**: individualstepdurations<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_ItemsFailed"></a> ItemsFailed

**Description**: Number of items processed unsuccessfully.<br />
**DisplayName**: Items Failed<br />
**LogicalName**: itemsfailed<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_ItemsProcessed"></a> ItemsProcessed

**Description**: Number of items processed.<br />
**DisplayName**: Items Processed<br />
**LogicalName**: itemsprocessed<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_MachineName"></a> MachineName

**Description**: Name of Machine on which mailbox was processed<br />
**DisplayName**: Machine Name<br />
**LogicalName**: machinename<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_MailboxId"></a> MailboxId

**Description**: Regarding Mailbox.<br />
**DisplayName**: Regarding Mailbox<br />
**LogicalName**: mailboxid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: mailbox


### <a name="BKMK_MailboxProcessCompletedOn"></a> MailboxProcessCompletedOn

**Description**: Completion time of the synchronization cycle.<br />
**DisplayName**: End Time for Processing<br />
**LogicalName**: mailboxprocesscompletedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_MailboxProcessScheduledOn"></a> MailboxProcessScheduledOn

**Description**: Scheduled time of the synchronization cycle.<br />
**DisplayName**: Scheduled Time for Processing<br />
**LogicalName**: mailboxprocessscheduledon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_MailboxProcessStartedOn"></a> MailboxProcessStartedOn

**Description**: Start time of the synchronization cycle.<br />
**DisplayName**: Start Time for Processing<br />
**LogicalName**: mailboxprocessstartedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_MailboxStatisticsId"></a> MailboxStatisticsId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: mailboxstatisticsid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_OperationTypeId"></a> OperationTypeId

**Description**: Type of the mailbox operation<br />
**DisplayName**: Mailbox Operation Type<br />
**LogicalName**: operationtypeid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Incoming Email
- **Value**: 1 **Label**: Outgoing Email
- **Value**: 2 **Label**: ACT



### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization associated with the record.<br />
**DisplayName**: Organization<br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: organization


### <a name="BKMK_ProcessResult"></a> ProcessResult

**Description**: Result of Mailbox processing cycle<br />
**DisplayName**: Process Result<br />
**LogicalName**: processresult<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Success
- **FalseOption Value**: 0 **Label**: Failure

**DefaultValue**: False


### <a name="BKMK_ProcessTimeIntervalInMinutes"></a> ProcessTimeIntervalInMinutes

**Description**: Time it took to process the mailbox.<br />
**DisplayName**: Process Duration<br />
**LogicalName**: processtimeintervalinminutes<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_ScheduledTimeIntervalInMinutes"></a> ScheduledTimeIntervalInMinutes

**Description**: Time it took from the scheduled time to the actual start time to process the mailbox.<br />
**DisplayName**: Queue Duration<br />
**LogicalName**: scheduledtimeintervalinminutes<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [organization_mailboxstatistics](#BKMK_organization_mailboxstatistics)
- [mailbox_mailboxstatistics](#BKMK_mailbox_mailboxstatistics)


### <a name="BKMK_organization_mailboxstatistics"></a> organization_mailboxstatistics

See organization Entity [organization_mailboxstatistics](organization.md#BKMK_organization_mailboxstatistics) One-To-Many relationship.

### <a name="BKMK_mailbox_mailboxstatistics"></a> mailbox_mailboxstatistics

See mailbox Entity [mailbox_mailboxstatistics](mailbox.md#BKMK_mailbox_mailboxstatistics) One-To-Many relationship.
mailboxstatistics

