---
title: "QueueItem Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the QueueItem entity."
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
ms.date: 10/31/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# QueueItem Entity Reference

A specific item in a queue, such as a case record or an activity record.

## Entity Properties

**DisplayName**: Queue Item<br />
**DisplayCollectionName**: Queue Items<br />
**SchemaName**: QueueItem<br />
**CollectionSchemaName**: QueueItems<br />
**LogicalName**: queueitem<br />
**LogicalCollectionName**: queueitems<br />
**EntitySetName**: queueitems<br />
**PrimaryIdAttribute**: queueitemid<br />
**PrimaryNameAttribute**: title<br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [ObjectId](#BKMK_ObjectId)
- [ObjectIdTypeCode](#BKMK_ObjectIdTypeCode)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [Priority](#BKMK_Priority)
- [QueueId](#BKMK_QueueId)
- [QueueItemId](#BKMK_QueueItemId)
- [Sender](#BKMK_Sender)
- [State](#BKMK_State)
- [StateCode](#BKMK_StateCode)
- [Status](#BKMK_Status)
- [StatusCode](#BKMK_StatusCode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [ToRecipients](#BKMK_ToRecipients)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [WorkerId](#BKMK_WorkerId)
- [WorkerIdType](#BKMK_WorkerIdType)


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

**Description**: Unique identifier of the data import or data migration that created this record.<br />
**DisplayName**: Import Sequence Number<br />
**LogicalName**: importsequencenumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_ObjectId"></a> ObjectId

**Description**: Choose the activity, case, or article assigned to the queue.<br />
**DisplayName**: Object<br />
**LogicalName**: objectid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: activitypointer,appointment,email,fax,knowledgearticle,letter,phonecall,recurringappointmentmaster,socialactivity,task


### <a name="BKMK_ObjectIdTypeCode"></a> ObjectIdTypeCode

**Description**: <br />
**DisplayName**: Regarding Object Type<br />
**LogicalName**: objectidtypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

**Description**: Date and time that the record was migrated.<br />
**DisplayName**: Record Created On<br />
**LogicalName**: overriddencreatedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_Priority"></a> Priority

**Description**: Priority of the queue item.<br />
**DisplayName**: Priority<br />
**LogicalName**: priority<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0


### <a name="BKMK_QueueId"></a> QueueId

**Description**: Choose the queue that the item is assigned to.<br />
**DisplayName**: Queue<br />
**LogicalName**: queueid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: queue


### <a name="BKMK_QueueItemId"></a> QueueItemId

**Description**: Unique identifier of the queue item.<br />
**DisplayName**: Queue Item<br />
**LogicalName**: queueitemid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_Sender"></a> Sender

**Description**: Sender who created the queue item.<br />
**DisplayName**: From<br />
**LogicalName**: sender<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 250


### <a name="BKMK_State"></a> State

**Description**: Status of the queue item.<br />
**DisplayName**: Status (deprecated)<br />
**LogicalName**: state<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0


### <a name="BKMK_StateCode"></a> StateCode

**Description**: Shows whether the queue record is active or inactive. Inactive queue records are read-only and can't be edited unless they are reactivated.<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Active **DefaultStatus**: 1 **InvariantName**: Active
- **Value**: 1 **Label**: Inactive **DefaultStatus**: 2 **InvariantName**: Inactive



### <a name="BKMK_Status"></a> Status

**Description**: Reason for the status of the queue item.<br />
**DisplayName**: Status Reason (deprecated)<br />
**LogicalName**: status<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0


### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Select the item's status.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Status<br />
**Options**:

- **Value**: 1 **Label**: Active **State**: 0
- **Value**: 2 **Label**: Inactive **State**: 1



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


### <a name="BKMK_ToRecipients"></a> ToRecipients

**Description**: Recipients listed on the To line of the message for email queue items.<br />
**DisplayName**: To<br />
**LogicalName**: torecipients<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 500


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

**Description**: Choose the local currency for the record to make sure budgets are reported in the correct currency.<br />
**DisplayName**: Currency<br />
**LogicalName**: transactioncurrencyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: transactioncurrency


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


### <a name="BKMK_WorkerId"></a> WorkerId

**Description**: Shows who is working on the queue item.<br />
**DisplayName**: Worked By<br />
**LogicalName**: workerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser,team


### <a name="BKMK_WorkerIdType"></a> WorkerIdType

**Description**: <br />
**DisplayName**: Worker Type<br />
**LogicalName**: workeridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: EntityName<br />

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
- [EnteredOn](#BKMK_EnteredOn)
- [ExchangeRate](#BKMK_ExchangeRate)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [ObjectIdName](#BKMK_ObjectIdName)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningUser](#BKMK_OwningUser)
- [QueueIdName](#BKMK_QueueIdName)
- [Title](#BKMK_Title)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)
- [WorkerIdModifiedOn](#BKMK_WorkerIdModifiedOn)
- [WorkerIdName](#BKMK_WorkerIdName)
- [WorkerIdYomiName](#BKMK_WorkerIdYomiName)


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
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Shows who created the record on behalf of another user.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: False<br />
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


### <a name="BKMK_EnteredOn"></a> EnteredOn

**Description**: Shows the date the record was assigned to the queue.<br />
**DisplayName**: Entered Queue<br />
**LogicalName**: enteredon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

**Description**: Shows the conversion rate of the record's currency. The exchange rate is used to convert all money fields in the record from the local currency to the system's default currency.<br />
**DisplayName**: Exchange Rate<br />
**LogicalName**: exchangerate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0.0000000001<br />
**Precision**: 10


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Shows who last updated the record.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: True<br />
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


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyyominame<br />
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

**Description**: Unique identifier of the delegate user who last modified the queueitem.<br />
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


### <a name="BKMK_ObjectIdName"></a> ObjectIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: objectidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 300


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

**Description**: Select the type of the queue item, such as activity, case, or appointment.<br />
**DisplayName**: Type<br />
**LogicalName**: objecttypecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 4200 **Label**: Activity
- **Value**: 4201 **Label**: Appointment
- **Value**: 4202 **Label**: Email
- **Value**: 4204 **Label**: Fax
- **Value**: 4207 **Label**: Letter
- **Value**: 4210 **Label**: Phone Call
- **Value**: 4212 **Label**: Task
- **Value**: 4216 **Label**: Social Activity
- **Value**: 4251 **Label**: Recurring Appointment
- **Value**: 9953 **Label**: Knowledge Article



### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization with which the queue item is associated.<br />
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


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Unique identifier of the user or team who owns the queue item.<br />
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

**Description**: Unique identifier of the business unit that owns the queue item.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns the queue item.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_QueueIdName"></a> QueueIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: queueidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 400


### <a name="BKMK_Title"></a> Title

**Description**: Shows the title or name that describes the queue record. This value is copied from the record that was assigned to the queue.<br />
**DisplayName**: Title<br />
**LogicalName**: title<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 300


### <a name="BKMK_TransactionCurrencyIdName"></a> TransactionCurrencyIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: transactioncurrencyidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: Version number of the queue item.<br />
**DisplayName**: Version Number<br />
**LogicalName**: versionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />


### <a name="BKMK_WorkerIdModifiedOn"></a> WorkerIdModifiedOn

**Description**: Shows the date and time when the queue item was last assigned to a user.<br />
**DisplayName**: Worked On<br />
**LogicalName**: workeridmodifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_WorkerIdName"></a> WorkerIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: workeridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_WorkerIdYomiName"></a> WorkerIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: workeridyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [userentityinstancedata_queueitem](#BKMK_userentityinstancedata_queueitem)
- [QueueItem_AsyncOperations](#BKMK_QueueItem_AsyncOperations)
- [QueueItem_SyncErrors](#BKMK_QueueItem_SyncErrors)
- [QueueItem_BulkDeleteFailures](#BKMK_QueueItem_BulkDeleteFailures)
- [queueitem_principalobjectattributeaccess](#BKMK_queueitem_principalobjectattributeaccess)
- [QueueItem_ProcessSessions](#BKMK_QueueItem_ProcessSessions)


### <a name="BKMK_userentityinstancedata_queueitem"></a> userentityinstancedata_queueitem

Same as userentityinstancedata entity [userentityinstancedata_queueitem](userentityinstancedata.md#BKMK_userentityinstancedata_queueitem) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_queueitem<br />
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


### <a name="BKMK_QueueItem_AsyncOperations"></a> QueueItem_AsyncOperations

Same as asyncoperation entity [QueueItem_AsyncOperations](asyncoperation.md#BKMK_QueueItem_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: QueueItem_AsyncOperations<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
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


### <a name="BKMK_QueueItem_SyncErrors"></a> QueueItem_SyncErrors

Same as syncerror entity [QueueItem_SyncErrors](syncerror.md#BKMK_QueueItem_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: QueueItem_SyncErrors<br />
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


### <a name="BKMK_QueueItem_BulkDeleteFailures"></a> QueueItem_BulkDeleteFailures

Same as bulkdeletefailure entity [QueueItem_BulkDeleteFailures](bulkdeletefailure.md#BKMK_QueueItem_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: QueueItem_BulkDeleteFailures<br />
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


### <a name="BKMK_queueitem_principalobjectattributeaccess"></a> queueitem_principalobjectattributeaccess

Same as principalobjectattributeaccess entity [queueitem_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_queueitem_principalobjectattributeaccess) Many-To-One relationship.

**ReferencingEntity**: principalobjectattributeaccess<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: queueitem_principalobjectattributeaccess<br />
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


### <a name="BKMK_QueueItem_ProcessSessions"></a> QueueItem_ProcessSessions

Same as processsession entity [QueueItem_ProcessSessions](processsession.md#BKMK_QueueItem_ProcessSessions) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: QueueItem_ProcessSessions<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 110

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [knowledgearticle_QueueItems](#BKMK_knowledgearticle_QueueItems)
- [lk_queueitem_createdonbehalfby](#BKMK_lk_queueitem_createdonbehalfby)
- [lk_queueitembase_workerid](#BKMK_lk_queueitembase_workerid)
- [ActivityPointer_QueueItem](#BKMK_ActivityPointer_QueueItem)
- [queue_entries](#BKMK_queue_entries)
- [lk_queueitembase_createdby](#BKMK_lk_queueitembase_createdby)
- [organization_queueitems](#BKMK_organization_queueitems)
- [TransactionCurrency_QueueItem](#BKMK_TransactionCurrency_QueueItem)
- [Appointment_QueueItem](#BKMK_Appointment_QueueItem)
- [Fax_QueueItem](#BKMK_Fax_QueueItem)
- [team_queueitembase_workerid](#BKMK_team_queueitembase_workerid)
- [Email_QueueItem](#BKMK_Email_QueueItem)
- [SocialActivity_QueueItem](#BKMK_SocialActivity_QueueItem)
- [lk_queueitem_modifiedonbehalfby](#BKMK_lk_queueitem_modifiedonbehalfby)
- [PhoneCall_QueueItem](#BKMK_PhoneCall_QueueItem)
- [Task_QueueItem](#BKMK_Task_QueueItem)
- [RecurringAppointmentMaster_QueueItem](#BKMK_RecurringAppointmentMaster_QueueItem)
- [Letter_QueueItem](#BKMK_Letter_QueueItem)
- [lk_queueitembase_modifiedby](#BKMK_lk_queueitembase_modifiedby)


### <a name="BKMK_knowledgearticle_QueueItems"></a> knowledgearticle_QueueItems

See knowledgearticle Entity [knowledgearticle_QueueItems](knowledgearticle.md#BKMK_knowledgearticle_QueueItems) One-To-Many relationship.

### <a name="BKMK_lk_queueitem_createdonbehalfby"></a> lk_queueitem_createdonbehalfby

See systemuser Entity [lk_queueitem_createdonbehalfby](systemuser.md#BKMK_lk_queueitem_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_queueitembase_workerid"></a> lk_queueitembase_workerid

See systemuser Entity [lk_queueitembase_workerid](systemuser.md#BKMK_lk_queueitembase_workerid) One-To-Many relationship.

### <a name="BKMK_ActivityPointer_QueueItem"></a> ActivityPointer_QueueItem

See activitypointer Entity [ActivityPointer_QueueItem](activitypointer.md#BKMK_ActivityPointer_QueueItem) One-To-Many relationship.

### <a name="BKMK_queue_entries"></a> queue_entries

See queue Entity [queue_entries](queue.md#BKMK_queue_entries) One-To-Many relationship.

### <a name="BKMK_lk_queueitembase_createdby"></a> lk_queueitembase_createdby

See systemuser Entity [lk_queueitembase_createdby](systemuser.md#BKMK_lk_queueitembase_createdby) One-To-Many relationship.

### <a name="BKMK_organization_queueitems"></a> organization_queueitems

See organization Entity [organization_queueitems](organization.md#BKMK_organization_queueitems) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_QueueItem"></a> TransactionCurrency_QueueItem

See transactioncurrency Entity [TransactionCurrency_QueueItem](transactioncurrency.md#BKMK_TransactionCurrency_QueueItem) One-To-Many relationship.

### <a name="BKMK_Appointment_QueueItem"></a> Appointment_QueueItem

See appointment Entity [Appointment_QueueItem](appointment.md#BKMK_Appointment_QueueItem) One-To-Many relationship.

### <a name="BKMK_Fax_QueueItem"></a> Fax_QueueItem

See fax Entity [Fax_QueueItem](fax.md#BKMK_Fax_QueueItem) One-To-Many relationship.

### <a name="BKMK_team_queueitembase_workerid"></a> team_queueitembase_workerid

See team Entity [team_queueitembase_workerid](team.md#BKMK_team_queueitembase_workerid) One-To-Many relationship.

### <a name="BKMK_Email_QueueItem"></a> Email_QueueItem

See email Entity [Email_QueueItem](email.md#BKMK_Email_QueueItem) One-To-Many relationship.

### <a name="BKMK_SocialActivity_QueueItem"></a> SocialActivity_QueueItem

See socialactivity Entity [SocialActivity_QueueItem](socialactivity.md#BKMK_SocialActivity_QueueItem) One-To-Many relationship.

### <a name="BKMK_lk_queueitem_modifiedonbehalfby"></a> lk_queueitem_modifiedonbehalfby

See systemuser Entity [lk_queueitem_modifiedonbehalfby](systemuser.md#BKMK_lk_queueitem_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_PhoneCall_QueueItem"></a> PhoneCall_QueueItem

See phonecall Entity [PhoneCall_QueueItem](phonecall.md#BKMK_PhoneCall_QueueItem) One-To-Many relationship.

### <a name="BKMK_Task_QueueItem"></a> Task_QueueItem

See task Entity [Task_QueueItem](task.md#BKMK_Task_QueueItem) One-To-Many relationship.

### <a name="BKMK_RecurringAppointmentMaster_QueueItem"></a> RecurringAppointmentMaster_QueueItem

See recurringappointmentmaster Entity [RecurringAppointmentMaster_QueueItem](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_QueueItem) One-To-Many relationship.

### <a name="BKMK_Letter_QueueItem"></a> Letter_QueueItem

See letter Entity [Letter_QueueItem](letter.md#BKMK_Letter_QueueItem) One-To-Many relationship.

### <a name="BKMK_lk_queueitembase_modifiedby"></a> lk_queueitembase_modifiedby

See systemuser Entity [lk_queueitembase_modifiedby](systemuser.md#BKMK_lk_queueitembase_modifiedby) One-To-Many relationship.
queueitem

