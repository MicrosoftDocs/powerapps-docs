---
title: "SLAKPIInstance Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the SLAKPIInstance entity."
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
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# SLAKPIInstance Entity Reference

Service level agreement (SLA) key performance indicator (KPI) instance that is tracked for an individual case

## Entity Properties

**DisplayName**: SLA KPI Instance<br />
**DisplayCollectionName**: SLA KPI Instances<br />
**SchemaName**: SLAKPIInstance<br />
**CollectionSchemaName**: SLAKPIInstances<br />
**LogicalName**: slakpiinstance<br />
**LogicalCollectionName**: slakpiinstances<br />
**EntitySetName**: slakpiinstances<br />
**PrimaryIdAttribute**: slakpiinstanceid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ComputedFailureTime](#BKMK_ComputedFailureTime)
- [ComputedWarningTime](#BKMK_ComputedWarningTime)
- [Description](#BKMK_Description)
- [FailureTime](#BKMK_FailureTime)
- [Name](#BKMK_Name)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [Regarding](#BKMK_Regarding)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [SLAKPIInstanceId](#BKMK_SLAKPIInstanceId)
- [Status](#BKMK_Status)
- [SucceededOn](#BKMK_SucceededOn)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [WarningTime](#BKMK_WarningTime)
- [WarningTimeReached](#BKMK_WarningTimeReached)


### <a name="BKMK_ComputedFailureTime"></a> ComputedFailureTime

**Description**: Computed Failure Date and time<br />
**DisplayName**: Computed Failure Time<br />
**LogicalName**: computedfailuretime<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ComputedWarningTime"></a> ComputedWarningTime

**Description**: Computed Warning Date and time<br />
**DisplayName**: Computed Warning Time<br />
**LogicalName**: computedwarningtime<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_Description"></a> Description

**Description**: For internal use only.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_FailureTime"></a> FailureTime

**Description**: Enter the date and time when the service level agreement (SLA) key performance indicator (KPI) will expire.<br />
**DisplayName**: Failure Time<br />
**LogicalName**: failuretime<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_Name"></a> Name

**Description**: Type a descriptive name for the service level agreement (SLA) key performance indicator (KPI) instance.<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user or team.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Owner<br />
**Targets**: systemuser


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Description**: Owning Business Unit.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: OwningTeam.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: 


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Owning User.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: 


### <a name="BKMK_Regarding"></a> Regarding

**Description**: Unique identifier of the record that this service level agreement (SLA) key performance indicator (KPI) instance is associated with.<br />
**DisplayName**: Regarding<br />
**LogicalName**: regarding<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: account,activitypointer,appointment,contact,email,fax,letter,phonecall,socialactivity,task


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

**Description**: RegardingObjectTypeCode<br />
**DisplayName**: RegardingObjectTypeCode<br />
**LogicalName**: regardingobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_SLAKPIInstanceId"></a> SLAKPIInstanceId

**Description**: Unique identifier of the SLA KPI Instance.<br />
**DisplayName**: SLA KPI InstanceId<br />
**LogicalName**: slakpiinstanceid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_Status"></a> Status

**Description**: Reason for the status of the service level agreement (SLA) key performance indicator (KPI) instance. For example, the SLA KPI could be Noncompliant or Succeeded.<br />
**DisplayName**: Status<br />
**LogicalName**: status<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: In Progress
- **Value**: 1 **Label**: Noncompliant
- **Value**: 2 **Label**: Nearing Noncompliance
- **Value**: 3 **Label**: Paused
- **Value**: 4 **Label**: Succeeded
- **Value**: 5 **Label**: Canceled



### <a name="BKMK_SucceededOn"></a> SucceededOn

**Description**: Shows the date and time when the service level agreement (SLA) key performance indicator (KPI) success criteria was met.<br />
**DisplayName**: Succeeded On<br />
**LogicalName**: succeededon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

**Description**: Choose the local currency for the record to make sure budgets are reported in the correct currency.<br />
**DisplayName**: Currency<br />
**LogicalName**: transactioncurrencyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: transactioncurrency


### <a name="BKMK_WarningTime"></a> WarningTime

**Description**: Enter the date and time when the service level agreement (SLA) key performance indicator (KPI)will go to a warning state.<br />
**DisplayName**: Warning Time<br />
**LogicalName**: warningtime<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_WarningTimeReached"></a> WarningTimeReached

**Description**: Shows information about whether the case has reached its warning time.<br />
**DisplayName**: Warning Time Reached<br />
**LogicalName**: warningtimereached<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: No
- **Value**: 1 **Label**: Yes


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
- [ExchangeRate](#BKMK_ExchangeRate)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [RegardingIdName](#BKMK_RegardingIdName)
- [RegardingYomiName](#BKMK_RegardingYomiName)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: For internal use only.<br />
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

**Description**: For internal use only.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: For internal use only.<br />
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


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

**Description**: For internal use only.<br />
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

**Description**: For internal use only.<br />
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

**Description**: For internal use only.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: For internal use only.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: True<br />
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


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Description**: <br />
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

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_RegardingIdName"></a> RegardingIdName

**Description**: RegardingName<br />
**DisplayName**: RegardingName<br />
**LogicalName**: regardingidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_RegardingYomiName"></a> RegardingYomiName

**Description**: RegardingYomiName<br />
**DisplayName**: RegardingYomiName<br />
**LogicalName**: regardingyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 400


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

**Description**: For internal use only.<br />
**DisplayName**: Version Number<br />
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


### <a name="BKMK_SLAKPIInstance_SyncErrors"></a> SLAKPIInstance_SyncErrors

Same as syncerror entity [SLAKPIInstance_SyncErrors](syncerror.md#BKMK_SLAKPIInstance_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: SLAKPIInstance_SyncErrors<br />
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

- [slakpiinstance_activitypointer](#BKMK_slakpiinstance_activitypointer)
- [slakpiinstance_email](#BKMK_slakpiinstance_email)
- [slakpiinstance_fax](#BKMK_slakpiinstance_fax)
- [lk_slakpiinstancebase_createdonbehalfby](#BKMK_lk_slakpiinstancebase_createdonbehalfby)
- [lk_slakpiinstancebase_modifiedonbehalfby](#BKMK_lk_slakpiinstancebase_modifiedonbehalfby)
- [slakpiinstance_account](#BKMK_slakpiinstance_account)
- [slakpiinstance_letter](#BKMK_slakpiinstance_letter)
- [slakpiinstance_phonecall](#BKMK_slakpiinstance_phonecall)
- [business_unit_slakpiinstance](#BKMK_business_unit_slakpiinstance)
- [slakpiinstance_socialactivity](#BKMK_slakpiinstance_socialactivity)
- [slakpiinstance_task](#BKMK_slakpiinstance_task)
- [lk_slakpiinstancebase_modifiedby](#BKMK_lk_slakpiinstancebase_modifiedby)
- [TransactionCurrency_slakpiinstance](#BKMK_TransactionCurrency_slakpiinstance)
- [slakpiinstance_contact](#BKMK_slakpiinstance_contact)
- [lk_slakpiinstancebase_createdby](#BKMK_lk_slakpiinstancebase_createdby)
- [slakpiinstance_appointment](#BKMK_slakpiinstance_appointment)


### <a name="BKMK_slakpiinstance_activitypointer"></a> slakpiinstance_activitypointer

See activitypointer Entity [slakpiinstance_activitypointer](activitypointer.md#BKMK_slakpiinstance_activitypointer) One-To-Many relationship.

### <a name="BKMK_slakpiinstance_email"></a> slakpiinstance_email

See email Entity [slakpiinstance_email](email.md#BKMK_slakpiinstance_email) One-To-Many relationship.

### <a name="BKMK_slakpiinstance_fax"></a> slakpiinstance_fax

See fax Entity [slakpiinstance_fax](fax.md#BKMK_slakpiinstance_fax) One-To-Many relationship.

### <a name="BKMK_lk_slakpiinstancebase_createdonbehalfby"></a> lk_slakpiinstancebase_createdonbehalfby

See systemuser Entity [lk_slakpiinstancebase_createdonbehalfby](systemuser.md#BKMK_lk_slakpiinstancebase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_slakpiinstancebase_modifiedonbehalfby"></a> lk_slakpiinstancebase_modifiedonbehalfby

See systemuser Entity [lk_slakpiinstancebase_modifiedonbehalfby](systemuser.md#BKMK_lk_slakpiinstancebase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_slakpiinstance_account"></a> slakpiinstance_account

See account Entity [slakpiinstance_account](account.md#BKMK_slakpiinstance_account) One-To-Many relationship.

### <a name="BKMK_slakpiinstance_letter"></a> slakpiinstance_letter

See letter Entity [slakpiinstance_letter](letter.md#BKMK_slakpiinstance_letter) One-To-Many relationship.

### <a name="BKMK_slakpiinstance_phonecall"></a> slakpiinstance_phonecall

See phonecall Entity [slakpiinstance_phonecall](phonecall.md#BKMK_slakpiinstance_phonecall) One-To-Many relationship.

### <a name="BKMK_business_unit_slakpiinstance"></a> business_unit_slakpiinstance

See businessunit Entity [business_unit_slakpiinstance](businessunit.md#BKMK_business_unit_slakpiinstance) One-To-Many relationship.

### <a name="BKMK_slakpiinstance_socialactivity"></a> slakpiinstance_socialactivity

See socialactivity Entity [slakpiinstance_socialactivity](socialactivity.md#BKMK_slakpiinstance_socialactivity) One-To-Many relationship.

### <a name="BKMK_slakpiinstance_task"></a> slakpiinstance_task

See task Entity [slakpiinstance_task](task.md#BKMK_slakpiinstance_task) One-To-Many relationship.

### <a name="BKMK_lk_slakpiinstancebase_modifiedby"></a> lk_slakpiinstancebase_modifiedby

See systemuser Entity [lk_slakpiinstancebase_modifiedby](systemuser.md#BKMK_lk_slakpiinstancebase_modifiedby) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_slakpiinstance"></a> TransactionCurrency_slakpiinstance

See transactioncurrency Entity [TransactionCurrency_slakpiinstance](transactioncurrency.md#BKMK_TransactionCurrency_slakpiinstance) One-To-Many relationship.

### <a name="BKMK_slakpiinstance_contact"></a> slakpiinstance_contact

See contact Entity [slakpiinstance_contact](contact.md#BKMK_slakpiinstance_contact) One-To-Many relationship.

### <a name="BKMK_lk_slakpiinstancebase_createdby"></a> lk_slakpiinstancebase_createdby

See systemuser Entity [lk_slakpiinstancebase_createdby](systemuser.md#BKMK_lk_slakpiinstancebase_createdby) One-To-Many relationship.

### <a name="BKMK_slakpiinstance_appointment"></a> slakpiinstance_appointment

See appointment Entity [slakpiinstance_appointment](appointment.md#BKMK_slakpiinstance_appointment) One-To-Many relationship.
slakpiinstance

