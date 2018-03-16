---
title: "Audit Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the Audit entity."

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
# Audit Entity Reference

Track changes to records for analysis, record keeping, and compliance.

## Entity Properties

**DisplayName**: Auditing<br />
**DisplayCollectionName**: Audits<br />
**SchemaName**: Audit<br />
**CollectionSchemaName**: Audit<br />
**LogicalName**: audit<br />
**LogicalCollectionName**: audits<br />
**EntitySetName**: audits<br />
**PrimaryIdAttribute**: auditid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [UserAdditionalInfo](#BKMK_UserAdditionalInfo)


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

**Description**: Unique identifier of the object with which the record is associated.<br />
**DisplayName**: Regarding<br />
**LogicalName**: regardingobjectid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: 


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjectidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 400


### <a name="BKMK_UserAdditionalInfo"></a> UserAdditionalInfo

**Description**: Additional information associated to the user who caused the change.<br />
**DisplayName**: User Info<br />
**LogicalName**: useradditionalinfo<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 350

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [Action](#BKMK_Action)
- [AttributeMask](#BKMK_AttributeMask)
- [AuditId](#BKMK_AuditId)
- [CallingUserId](#BKMK_CallingUserId)
- [CallingUserIdName](#BKMK_CallingUserIdName)
- [ChangeData](#BKMK_ChangeData)
- [CreatedOn](#BKMK_CreatedOn)
- [ObjectId](#BKMK_ObjectId)
- [ObjectIdName](#BKMK_ObjectIdName)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [Operation](#BKMK_Operation)
- [TransactionId](#BKMK_TransactionId)
- [UserId](#BKMK_UserId)
- [UserIdName](#BKMK_UserIdName)


### <a name="BKMK_Action"></a> Action

**Description**: Actions the user can perform that cause a change<br />
**DisplayName**: Event<br />
**LogicalName**: action<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Unknown
- **Value**: 1 **Label**: Create
- **Value**: 2 **Label**: Update
- **Value**: 3 **Label**: Delete
- **Value**: 4 **Label**: Activate
- **Value**: 5 **Label**: Deactivate
- **Value**: 11 **Label**: Cascade
- **Value**: 12 **Label**: Merge
- **Value**: 13 **Label**: Assign
- **Value**: 14 **Label**: Share
- **Value**: 15 **Label**: Retrieve
- **Value**: 16 **Label**: Close
- **Value**: 17 **Label**: Cancel
- **Value**: 18 **Label**: Complete
- **Value**: 20 **Label**: Resolve
- **Value**: 21 **Label**: Reopen
- **Value**: 22 **Label**: Fulfill
- **Value**: 23 **Label**: Paid
- **Value**: 24 **Label**: Qualify
- **Value**: 25 **Label**: Disqualify
- **Value**: 26 **Label**: Submit
- **Value**: 27 **Label**: Reject
- **Value**: 28 **Label**: Approve
- **Value**: 29 **Label**: Invoice
- **Value**: 30 **Label**: Hold
- **Value**: 31 **Label**: Add Member
- **Value**: 32 **Label**: Remove Member
- **Value**: 33 **Label**: Associate Entities
- **Value**: 34 **Label**: Disassociate Entities
- **Value**: 35 **Label**: Add Members
- **Value**: 36 **Label**: Remove Members
- **Value**: 37 **Label**: Add Item
- **Value**: 38 **Label**: Remove Item
- **Value**: 39 **Label**: Add Substitute
- **Value**: 40 **Label**: Remove Substitute
- **Value**: 41 **Label**: Set State
- **Value**: 42 **Label**: Renew
- **Value**: 43 **Label**: Revise
- **Value**: 44 **Label**: Win
- **Value**: 45 **Label**: Lose
- **Value**: 46 **Label**: Internal Processing
- **Value**: 47 **Label**: Reschedule
- **Value**: 48 **Label**: Modify Share
- **Value**: 49 **Label**: Unshare
- **Value**: 50 **Label**: Book
- **Value**: 51 **Label**: Generate Quote From Opportunity
- **Value**: 52 **Label**: Add To Queue
- **Value**: 53 **Label**: Assign Role To Team
- **Value**: 54 **Label**: Remove Role From Team
- **Value**: 55 **Label**: Assign Role To User
- **Value**: 56 **Label**: Remove Role From User
- **Value**: 57 **Label**: Add Privileges to Role
- **Value**: 58 **Label**: Remove Privileges From Role
- **Value**: 59 **Label**: Replace Privileges In Role
- **Value**: 60 **Label**: Import Mappings
- **Value**: 61 **Label**: Clone
- **Value**: 62 **Label**: Send Direct Email
- **Value**: 63 **Label**: Enabled for organization
- **Value**: 64 **Label**: User Access via Web
- **Value**: 65 **Label**: User Access via Web Services
- **Value**: 100 **Label**: Delete Entity
- **Value**: 101 **Label**: Delete Attribute
- **Value**: 102 **Label**: Audit Change at Entity Level
- **Value**: 103 **Label**: Audit Change at Attribute Level
- **Value**: 104 **Label**: Audit Change at Org Level
- **Value**: 105 **Label**: Entity Audit Started
- **Value**: 106 **Label**: Attribute Audit Started
- **Value**: 107 **Label**: Audit Enabled
- **Value**: 108 **Label**: Entity Audit Stopped
- **Value**: 109 **Label**: Attribute Audit Stopped
- **Value**: 110 **Label**: Audit Disabled
- **Value**: 111 **Label**: Audit Log Deletion
- **Value**: 112 **Label**: User Access Audit Started
- **Value**: 113 **Label**: User Access Audit Stopped



### <a name="BKMK_AttributeMask"></a> AttributeMask

**Description**: Contains a CSV of the ColumnNumber metadata property of attributes<br />
**DisplayName**: Changed Field<br />
**LogicalName**: attributemask<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_AuditId"></a> AuditId

**Description**: Unique identifier of the auditing instance<br />
**DisplayName**: Record Id<br />
**LogicalName**: auditid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_CallingUserId"></a> CallingUserId

**Description**: Unique identifier of the calling user in case of an impersonated call<br />
**DisplayName**: Calling User<br />
**LogicalName**: callinguserid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CallingUserIdName"></a> CallingUserIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: callinguseridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ChangeData"></a> ChangeData

**Description**: Contains a CSV of old values of all the attributes whose IsAuditEnabled property is True and are being changed<br />
**DisplayName**: Change Data<br />
**LogicalName**: changedata<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the audit record was created.<br />
**DisplayName**: Changed Date<br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ObjectId"></a> ObjectId

**Description**: Unique identifier of the record that is being audited<br />
**DisplayName**: Record<br />
**LogicalName**: objectid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: 


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
**MaxLength**: 160


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

**Description**: Unique identifier of the entity that is being audited<br />
**DisplayName**: Entity<br />
**LogicalName**: objecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_Operation"></a> Operation

**Description**: The action that causes the audit--it will be create, delete, or update<br />
**DisplayName**: Operation<br />
**LogicalName**: operation<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Create
- **Value**: 2 **Label**: Update
- **Value**: 3 **Label**: Delete
- **Value**: 4 **Label**: Access



### <a name="BKMK_TransactionId"></a> TransactionId

**Description**: Unique identifier for multiple changes that are part of a single operation; this field contains the same GUID for all the audit rows generated in a single transaction<br />
**DisplayName**: Transaction Id<br />
**LogicalName**: transactionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_UserId"></a> UserId

**Description**: Unique identifier of the user who caused a change<br />
**DisplayName**: Changed By<br />
**LogicalName**: userid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: externalparty,systemuser


### <a name="BKMK_UserIdName"></a> UserIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: useridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_userentityinstancedata_audit"></a> userentityinstancedata_audit

Same as userentityinstancedata entity [userentityinstancedata_audit](userentityinstancedata.md#BKMK_userentityinstancedata_audit) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_audit<br />
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

- [lk_audit_userid](#BKMK_lk_audit_userid)
- [lk_audit_callinguserid](#BKMK_lk_audit_callinguserid)


### <a name="BKMK_lk_audit_userid"></a> lk_audit_userid

See systemuser Entity [lk_audit_userid](systemuser.md#BKMK_lk_audit_userid) One-To-Many relationship.

### <a name="BKMK_lk_audit_callinguserid"></a> lk_audit_callinguserid

See systemuser Entity [lk_audit_callinguserid](systemuser.md#BKMK_lk_audit_callinguserid) One-To-Many relationship.
audit

