---
title: "BulkDeleteOperation Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the BulkDeleteOperation entity."

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
# BulkDeleteOperation Entity Reference

User-submitted bulk deletion job.

## Entity Properties

**DisplayName**: Bulk Delete Operation<br />
**DisplayCollectionName**: Bulk Delete Operations<br />
**SchemaName**: BulkDeleteOperation<br />
**CollectionSchemaName**: BulkDeleteOperations<br />
**LogicalName**: bulkdeleteoperation<br />
**LogicalCollectionName**: bulkdeleteoperations<br />
**EntitySetName**: bulkdeleteoperations<br />
**PrimaryIdAttribute**: bulkdeleteoperationid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

**Description**: For internal use only.<br />
**DisplayName**: <br />
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
**DisplayName**: <br />
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

- [AsyncOperationId](#BKMK_AsyncOperationId)
- [BulkDeleteOperationId](#BKMK_BulkDeleteOperationId)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [FailureCount](#BKMK_FailureCount)
- [IsRecurring](#BKMK_IsRecurring)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [Name](#BKMK_Name)
- [NextRun](#BKMK_NextRun)
- [OrderedQuerySetXml](#BKMK_OrderedQuerySetXml)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningUser](#BKMK_OwningUser)
- [ProcessingQEIndex](#BKMK_ProcessingQEIndex)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [SuccessCount](#BKMK_SuccessCount)


### <a name="BKMK_AsyncOperationId"></a> AsyncOperationId

**Description**: Unique identifier of the system job that created this record<br />
**DisplayName**: System Job<br />
**LogicalName**: asyncoperationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: asyncoperation


### <a name="BKMK_BulkDeleteOperationId"></a> BulkDeleteOperationId

**Description**: Unique identifier of the bulk deletion job.<br />
**DisplayName**: Bulk Deletion Job<br />
**LogicalName**: bulkdeleteoperationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the bulk deletion job.<br />
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

**Description**: Date and time when the bulk deletion job was created.<br />
**DisplayName**: <br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the bulkdeleteoperation.<br />
**DisplayName**: <br />
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


### <a name="BKMK_FailureCount"></a> FailureCount

**Description**: Number of records that could not be deleted by the bulk deletion job.<br />
**DisplayName**: Failures<br />
**LogicalName**: failurecount<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0


### <a name="BKMK_IsRecurring"></a> IsRecurring

**Description**: Information about if recurrence is defined for the bulk deletion job.<br />
**DisplayName**: Is Recurring<br />
**LogicalName**: isrecurring<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the bulk deletion job.<br />
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

**Description**: Date and time when the bulk deletion job record was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the bulkdeleteoperation.<br />
**DisplayName**: <br />
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


### <a name="BKMK_Name"></a> Name

**Description**: Name of the bulk deletion job.<br />
**DisplayName**: System Job Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_NextRun"></a> NextRun

**Description**: Next scheduled time for the bulk deletion job to run.<br />
**DisplayName**: Next Run<br />
**LogicalName**: nextrun<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_OrderedQuerySetXml"></a> OrderedQuerySetXml

**Description**: Fetch XML of the ordered query set.<br />
**DisplayName**: <br />
**LogicalName**: orderedquerysetxml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Unique identifier of the user or team who owns the bulk delete operation.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
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

**Description**: Business unit that owns the bulk deletion job.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Business user what owns the bulk delete operation.<br />
**DisplayName**: <br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ProcessingQEIndex"></a> ProcessingQEIndex

**Description**: Index of the ordered query expression that defines the deletion set.<br />
**DisplayName**: Query Index<br />
**LogicalName**: processingqeindex<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0


### <a name="BKMK_StateCode"></a> StateCode

**Description**: Status of the bulk deletion job.<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Ready **DefaultStatus**: 1 **InvariantName**: Ready
- **Value**: 1 **Label**: Suspended **DefaultStatus**: 2 **InvariantName**: Suspended
- **Value**: 2 **Label**: Locked **DefaultStatus**: 2 **InvariantName**: Locked
- **Value**: 3 **Label**: Completed **DefaultStatus**: 2 **InvariantName**: Completed



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Reason for the status of the bulk deletion job.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Status<br />
**Options**:

- **Value**: 0 **Label**: Waiting For Resources **State**: 0
- **Value**: 10 **Label**: Waiting **State**: 1
- **Value**: 11 **Label**: Retrying **State**: 1
- **Value**: 12 **Label**: Paused **State**: 1
- **Value**: 20 **Label**: In Progress **State**: 2
- **Value**: 21 **Label**: Pausing **State**: 2
- **Value**: 22 **Label**: Canceling **State**: 2
- **Value**: 30 **Label**: Succeeded **State**: 3
- **Value**: 31 **Label**: Failed **State**: 3
- **Value**: 32 **Label**: Canceled **State**: 3



### <a name="BKMK_SuccessCount"></a> SuccessCount

**Description**: Number of records deleted by the bulk deletion job.<br />
**DisplayName**: Deleted<br />
**LogicalName**: successcount<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [BulkDeleteOperation_BulkDeleteFailure](#BKMK_BulkDeleteOperation_BulkDeleteFailure)
- [userentityinstancedata_bulkdeleteoperation](#BKMK_userentityinstancedata_bulkdeleteoperation)


### <a name="BKMK_BulkDeleteOperation_BulkDeleteFailure"></a> BulkDeleteOperation_BulkDeleteFailure

Same as bulkdeletefailure entity [BulkDeleteOperation_BulkDeleteFailure](bulkdeletefailure.md#BKMK_BulkDeleteOperation_BulkDeleteFailure) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: bulkdeleteoperationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: BulkDeleteOperation_BulkDeleteFailure<br />
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


### <a name="BKMK_userentityinstancedata_bulkdeleteoperation"></a> userentityinstancedata_bulkdeleteoperation

Same as userentityinstancedata entity [userentityinstancedata_bulkdeleteoperation](userentityinstancedata.md#BKMK_userentityinstancedata_bulkdeleteoperation) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_bulkdeleteoperation<br />
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

- [lk_bulkdeleteoperationbase_modifiedby](#BKMK_lk_bulkdeleteoperationbase_modifiedby)
- [AsyncOperation_BulkDeleteOperation](#BKMK_AsyncOperation_BulkDeleteOperation)
- [lk_bulkdeleteoperation_createdonbehalfby](#BKMK_lk_bulkdeleteoperation_createdonbehalfby)
- [lk_bulkdeleteoperation_modifiedonbehalfby](#BKMK_lk_bulkdeleteoperation_modifiedonbehalfby)
- [lk_bulkdeleteoperationbase_createdby](#BKMK_lk_bulkdeleteoperationbase_createdby)
- [BulkDeleteOperation_BusinessUnit](#BKMK_BulkDeleteOperation_BusinessUnit)


### <a name="BKMK_lk_bulkdeleteoperationbase_modifiedby"></a> lk_bulkdeleteoperationbase_modifiedby

See systemuser Entity [lk_bulkdeleteoperationbase_modifiedby](systemuser.md#BKMK_lk_bulkdeleteoperationbase_modifiedby) One-To-Many relationship.

### <a name="BKMK_AsyncOperation_BulkDeleteOperation"></a> AsyncOperation_BulkDeleteOperation

See asyncoperation Entity [AsyncOperation_BulkDeleteOperation](asyncoperation.md#BKMK_AsyncOperation_BulkDeleteOperation) One-To-Many relationship.

### <a name="BKMK_lk_bulkdeleteoperation_createdonbehalfby"></a> lk_bulkdeleteoperation_createdonbehalfby

See systemuser Entity [lk_bulkdeleteoperation_createdonbehalfby](systemuser.md#BKMK_lk_bulkdeleteoperation_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_bulkdeleteoperation_modifiedonbehalfby"></a> lk_bulkdeleteoperation_modifiedonbehalfby

See systemuser Entity [lk_bulkdeleteoperation_modifiedonbehalfby](systemuser.md#BKMK_lk_bulkdeleteoperation_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_bulkdeleteoperationbase_createdby"></a> lk_bulkdeleteoperationbase_createdby

See systemuser Entity [lk_bulkdeleteoperationbase_createdby](systemuser.md#BKMK_lk_bulkdeleteoperationbase_createdby) One-To-Many relationship.

### <a name="BKMK_BulkDeleteOperation_BusinessUnit"></a> BulkDeleteOperation_BusinessUnit

See businessunit Entity [BulkDeleteOperation_BusinessUnit](businessunit.md#BKMK_BulkDeleteOperation_BusinessUnit) One-To-Many relationship.
bulkdeleteoperation

