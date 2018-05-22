---
title: "DuplicateRecord Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the DuplicateRecord entity."

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
# DuplicateRecord Entity Reference

Potential duplicate record.

## Entity Properties

**DisplayName**: Duplicate Record<br />
**DisplayCollectionName**: Duplicate Records<br />
**SchemaName**: DuplicateRecord<br />
**CollectionSchemaName**: DuplicateRecords<br />
**LogicalName**: duplicaterecord<br />
**LogicalCollectionName**: duplicaterecords<br />
**EntitySetName**: duplicaterecords<br />
**PrimaryIdAttribute**: duplicateid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.


### <a name="BKMK_DuplicateId"></a> DuplicateId

**Description**: Unique identifier of the duplicate record.<br />
**DisplayName**: <br />
**LogicalName**: duplicateid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AsyncOperationId](#BKMK_AsyncOperationId)
- [BaseRecordId](#BKMK_BaseRecordId)
- [BaseRecordIdName](#BKMK_BaseRecordIdName)
- [BaseRecordIdTypeCode](#BKMK_BaseRecordIdTypeCode)
- [BaseRecordIdYomiName](#BKMK_BaseRecordIdYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [DuplicateRecordId](#BKMK_DuplicateRecordId)
- [DuplicateRecordIdName](#BKMK_DuplicateRecordIdName)
- [DuplicateRecordIdTypeCode](#BKMK_DuplicateRecordIdTypeCode)
- [DuplicateRecordIdYomiName](#BKMK_DuplicateRecordIdYomiName)
- [DuplicateRuleId](#BKMK_DuplicateRuleId)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningUser](#BKMK_OwningUser)


### <a name="BKMK_AsyncOperationId"></a> AsyncOperationId

**Description**: Unique identifier of the system job that created this record.<br />
**DisplayName**: System Job<br />
**LogicalName**: asyncoperationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: asyncoperation


### <a name="BKMK_BaseRecordId"></a> BaseRecordId

**Description**: Unique identifier of the base record.<br />
**DisplayName**: Base Record ID<br />
**LogicalName**: baserecordid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: account,appointment,channelaccessprofile,contact,email,emailserverprofile,fax,goal,goalrollupquery,kbarticle,knowledgearticle,knowledgebaserecord,letter,phonecall,publisher,queue,recurringappointmentmaster,sharepointdocumentlocation,sharepointsite,socialactivity,socialprofile,systemuser,task,team,transactioncurrency


### <a name="BKMK_BaseRecordIdName"></a> BaseRecordIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: baserecordidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 400


### <a name="BKMK_BaseRecordIdTypeCode"></a> BaseRecordIdTypeCode

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: baserecordidtypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_BaseRecordIdYomiName"></a> BaseRecordIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: baserecordidyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 400


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the duplicate record was created.<br />
**DisplayName**: <br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_DuplicateRecordId"></a> DuplicateRecordId

**Description**: Unique identifier of the potential duplicate record.<br />
**DisplayName**: Duplicate Record ID<br />
**LogicalName**: duplicaterecordid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: account,appointment,channelaccessprofile,contact,email,emailserverprofile,fax,goal,goalrollupquery,kbarticle,knowledgearticle,knowledgebaserecord,letter,phonecall,publisher,queue,recurringappointmentmaster,sharepointdocumentlocation,sharepointsite,socialactivity,socialprofile,systemuser,task,team,transactioncurrency


### <a name="BKMK_DuplicateRecordIdName"></a> DuplicateRecordIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: duplicaterecordidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 400


### <a name="BKMK_DuplicateRecordIdTypeCode"></a> DuplicateRecordIdTypeCode

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: duplicaterecordidtypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_DuplicateRecordIdYomiName"></a> DuplicateRecordIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: duplicaterecordidyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 400


### <a name="BKMK_DuplicateRuleId"></a> DuplicateRuleId

**Description**: Unique identifier of the duplicate rule against which this duplicate was found.<br />
**DisplayName**: <br />
**LogicalName**: duplicateruleid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: duplicaterule


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Unique identifier of the user or team who owns the duplicate record.<br />
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

**Description**: Unique identifier of the business unit that owns the duplicate record.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns the duplicate record.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Uniqueidentifier<br />

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_userentityinstancedata_duplicaterecord"></a> userentityinstancedata_duplicaterecord

Same as userentityinstancedata entity [userentityinstancedata_duplicaterecord](userentityinstancedata.md#BKMK_userentityinstancedata_duplicaterecord) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_duplicaterecord<br />
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

- [knowledgearticle_DuplicateMatchingRecord](#BKMK_knowledgearticle_DuplicateMatchingRecord)
- [knowledgearticle_DuplicateBaseRecord](#BKMK_knowledgearticle_DuplicateBaseRecord)
- [channelaccessprofile_DuplicateMatchingRecord](#BKMK_channelaccessprofile_DuplicateMatchingRecord)
- [channelaccessprofile_DuplicateBaseRecord](#BKMK_channelaccessprofile_DuplicateBaseRecord)
- [KnowledgeBaseRecord_DuplicateMatchingRecord](#BKMK_KnowledgeBaseRecord_DuplicateMatchingRecord)
- [KnowledgeBaseRecord_DuplicateBaseRecord](#BKMK_KnowledgeBaseRecord_DuplicateBaseRecord)
- [Email_DuplicateMatchingRecord](#BKMK_Email_DuplicateMatchingRecord)
- [Publisher_DuplicateMatchingRecord](#BKMK_Publisher_DuplicateMatchingRecord)
- [Queue_DuplicateBaseRecord](#BKMK_Queue_DuplicateBaseRecord)
- [Letter_DuplicateBaseRecord](#BKMK_Letter_DuplicateBaseRecord)
- [Team_DuplicateBaseRecord](#BKMK_Team_DuplicateBaseRecord)
- [KbArticle_DuplicateMatchingRecord](#BKMK_KbArticle_DuplicateMatchingRecord)
- [Appointment_DuplicateBaseRecord](#BKMK_Appointment_DuplicateBaseRecord)
- [Account_DuplicateBaseRecord](#BKMK_Account_DuplicateBaseRecord)
- [DuplicateRule_DuplicateBaseRecord](#BKMK_DuplicateRule_DuplicateBaseRecord)
- [SharePointSite_DuplicateBaseRecord](#BKMK_SharePointSite_DuplicateBaseRecord)
- [KbArticle_DuplicateBaseRecord](#BKMK_KbArticle_DuplicateBaseRecord)
- [Task_DuplicateMatchingRecord](#BKMK_Task_DuplicateMatchingRecord)
- [SocialProfile_DuplicateMatchingRecord](#BKMK_SocialProfile_DuplicateMatchingRecord)
- [PhoneCall_DuplicateBaseRecord](#BKMK_PhoneCall_DuplicateBaseRecord)
- [TransactionCurrency_DuplicateMatchingRecord](#BKMK_TransactionCurrency_DuplicateMatchingRecord)
- [Goal_DuplicateMatchingRecord](#BKMK_Goal_DuplicateMatchingRecord)
- [SharePointSite_DuplicateMatchingRecord](#BKMK_SharePointSite_DuplicateMatchingRecord)
- [emailserverprofile_duplicatebaserecord](#BKMK_emailserverprofile_duplicatebaserecord)
- [Publisher_DuplicateBaseRecord](#BKMK_Publisher_DuplicateBaseRecord)
- [SystemUser_DuplicateBaseRecord](#BKMK_SystemUser_DuplicateBaseRecord)
- [SocialActivity_DuplicateBaseRecord](#BKMK_SocialActivity_DuplicateBaseRecord)
- [Contact_DuplicateMatchingRecord](#BKMK_Contact_DuplicateMatchingRecord)
- [GoalRollupQuery_DuplicateMatchingRecord](#BKMK_GoalRollupQuery_DuplicateMatchingRecord)
- [Contact_DuplicateBaseRecord](#BKMK_Contact_DuplicateBaseRecord)
- [TransactionCurrency_DuplicateBaseRecord](#BKMK_TransactionCurrency_DuplicateBaseRecord)
- [Email_DuplicateBaseRecord](#BKMK_Email_DuplicateBaseRecord)
- [PhoneCall_DuplicateMatchingRecord](#BKMK_PhoneCall_DuplicateMatchingRecord)
- [Team_DuplicateMatchingRecord](#BKMK_Team_DuplicateMatchingRecord)
- [SystemUser_DuplicateMatchingRecord](#BKMK_SystemUser_DuplicateMatchingRecord)
- [Appointment_DuplicateMatchingRecord](#BKMK_Appointment_DuplicateMatchingRecord)
- [Account_DuplicateMatchingRecord](#BKMK_Account_DuplicateMatchingRecord)
- [Fax_DuplicateBaseRecord](#BKMK_Fax_DuplicateBaseRecord)
- [Letter_DuplicateMatchingRecord](#BKMK_Letter_DuplicateMatchingRecord)
- [emailserverprofile_duplicatematchingrecord](#BKMK_emailserverprofile_duplicatematchingrecord)
- [SharePointDocumentLocation_DuplicateBaseRecord](#BKMK_SharePointDocumentLocation_DuplicateBaseRecord)
- [Goal_DuplicateBaseRecord](#BKMK_Goal_DuplicateBaseRecord)
- [RecurringAppointmentMaster_DuplicateMatchingRecord](#BKMK_RecurringAppointmentMaster_DuplicateMatchingRecord)
- [Task_DuplicateBaseRecord](#BKMK_Task_DuplicateBaseRecord)
- [RecurringAppointmentMaster_DuplicateBaseRecord](#BKMK_RecurringAppointmentMaster_DuplicateBaseRecord)
- [Queue_DuplicateMatchingRecord](#BKMK_Queue_DuplicateMatchingRecord)
- [SocialProfile_DuplicateBaseRecord](#BKMK_SocialProfile_DuplicateBaseRecord)
- [SharePointDocumentLocation_DuplicateMatchingRecord](#BKMK_SharePointDocumentLocation_DuplicateMatchingRecord)
- [GoalRollupQuery_DuplicateBaseRecord](#BKMK_GoalRollupQuery_DuplicateBaseRecord)
- [AsyncOperation_DuplicateBaseRecord](#BKMK_AsyncOperation_DuplicateBaseRecord)
- [Fax_DuplicateMatchingRecord](#BKMK_Fax_DuplicateMatchingRecord)
- [SocialActivity_DuplicateMatchingRecord](#BKMK_SocialActivity_DuplicateMatchingRecord)


### <a name="BKMK_knowledgearticle_DuplicateMatchingRecord"></a> knowledgearticle_DuplicateMatchingRecord

See knowledgearticle Entity [knowledgearticle_DuplicateMatchingRecord](knowledgearticle.md#BKMK_knowledgearticle_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_DuplicateBaseRecord"></a> knowledgearticle_DuplicateBaseRecord

See knowledgearticle Entity [knowledgearticle_DuplicateBaseRecord](knowledgearticle.md#BKMK_knowledgearticle_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_channelaccessprofile_DuplicateMatchingRecord"></a> channelaccessprofile_DuplicateMatchingRecord

See channelaccessprofile Entity [channelaccessprofile_DuplicateMatchingRecord](channelaccessprofile.md#BKMK_channelaccessprofile_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_channelaccessprofile_DuplicateBaseRecord"></a> channelaccessprofile_DuplicateBaseRecord

See channelaccessprofile Entity [channelaccessprofile_DuplicateBaseRecord](channelaccessprofile.md#BKMK_channelaccessprofile_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_KnowledgeBaseRecord_DuplicateMatchingRecord"></a> KnowledgeBaseRecord_DuplicateMatchingRecord

See knowledgebaserecord Entity [KnowledgeBaseRecord_DuplicateMatchingRecord](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_KnowledgeBaseRecord_DuplicateBaseRecord"></a> KnowledgeBaseRecord_DuplicateBaseRecord

See knowledgebaserecord Entity [KnowledgeBaseRecord_DuplicateBaseRecord](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Email_DuplicateMatchingRecord"></a> Email_DuplicateMatchingRecord

See email Entity [Email_DuplicateMatchingRecord](email.md#BKMK_Email_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_Publisher_DuplicateMatchingRecord"></a> Publisher_DuplicateMatchingRecord

See publisher Entity [Publisher_DuplicateMatchingRecord](publisher.md#BKMK_Publisher_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_Queue_DuplicateBaseRecord"></a> Queue_DuplicateBaseRecord

See queue Entity [Queue_DuplicateBaseRecord](queue.md#BKMK_Queue_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Letter_DuplicateBaseRecord"></a> Letter_DuplicateBaseRecord

See letter Entity [Letter_DuplicateBaseRecord](letter.md#BKMK_Letter_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Team_DuplicateBaseRecord"></a> Team_DuplicateBaseRecord

See team Entity [Team_DuplicateBaseRecord](team.md#BKMK_Team_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_KbArticle_DuplicateMatchingRecord"></a> KbArticle_DuplicateMatchingRecord

See kbarticle Entity [KbArticle_DuplicateMatchingRecord](kbarticle.md#BKMK_KbArticle_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_Appointment_DuplicateBaseRecord"></a> Appointment_DuplicateBaseRecord

See appointment Entity [Appointment_DuplicateBaseRecord](appointment.md#BKMK_Appointment_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Account_DuplicateBaseRecord"></a> Account_DuplicateBaseRecord

See account Entity [Account_DuplicateBaseRecord](account.md#BKMK_Account_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_DuplicateRule_DuplicateBaseRecord"></a> DuplicateRule_DuplicateBaseRecord

See duplicaterule Entity [DuplicateRule_DuplicateBaseRecord](duplicaterule.md#BKMK_DuplicateRule_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_SharePointSite_DuplicateBaseRecord"></a> SharePointSite_DuplicateBaseRecord

See sharepointsite Entity [SharePointSite_DuplicateBaseRecord](sharepointsite.md#BKMK_SharePointSite_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_KbArticle_DuplicateBaseRecord"></a> KbArticle_DuplicateBaseRecord

See kbarticle Entity [KbArticle_DuplicateBaseRecord](kbarticle.md#BKMK_KbArticle_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Task_DuplicateMatchingRecord"></a> Task_DuplicateMatchingRecord

See task Entity [Task_DuplicateMatchingRecord](task.md#BKMK_Task_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_SocialProfile_DuplicateMatchingRecord"></a> SocialProfile_DuplicateMatchingRecord

See socialprofile Entity [SocialProfile_DuplicateMatchingRecord](socialprofile.md#BKMK_SocialProfile_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_PhoneCall_DuplicateBaseRecord"></a> PhoneCall_DuplicateBaseRecord

See phonecall Entity [PhoneCall_DuplicateBaseRecord](phonecall.md#BKMK_PhoneCall_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_DuplicateMatchingRecord"></a> TransactionCurrency_DuplicateMatchingRecord

See transactioncurrency Entity [TransactionCurrency_DuplicateMatchingRecord](transactioncurrency.md#BKMK_TransactionCurrency_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_Goal_DuplicateMatchingRecord"></a> Goal_DuplicateMatchingRecord

See goal Entity [Goal_DuplicateMatchingRecord](goal.md#BKMK_Goal_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_SharePointSite_DuplicateMatchingRecord"></a> SharePointSite_DuplicateMatchingRecord

See sharepointsite Entity [SharePointSite_DuplicateMatchingRecord](sharepointsite.md#BKMK_SharePointSite_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_emailserverprofile_duplicatebaserecord"></a> emailserverprofile_duplicatebaserecord

See emailserverprofile Entity [emailserverprofile_duplicatebaserecord](emailserverprofile.md#BKMK_emailserverprofile_duplicatebaserecord) One-To-Many relationship.

### <a name="BKMK_Publisher_DuplicateBaseRecord"></a> Publisher_DuplicateBaseRecord

See publisher Entity [Publisher_DuplicateBaseRecord](publisher.md#BKMK_Publisher_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_SystemUser_DuplicateBaseRecord"></a> SystemUser_DuplicateBaseRecord

See systemuser Entity [SystemUser_DuplicateBaseRecord](systemuser.md#BKMK_SystemUser_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_SocialActivity_DuplicateBaseRecord"></a> SocialActivity_DuplicateBaseRecord

See socialactivity Entity [SocialActivity_DuplicateBaseRecord](socialactivity.md#BKMK_SocialActivity_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Contact_DuplicateMatchingRecord"></a> Contact_DuplicateMatchingRecord

See contact Entity [Contact_DuplicateMatchingRecord](contact.md#BKMK_Contact_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_GoalRollupQuery_DuplicateMatchingRecord"></a> GoalRollupQuery_DuplicateMatchingRecord

See goalrollupquery Entity [GoalRollupQuery_DuplicateMatchingRecord](goalrollupquery.md#BKMK_GoalRollupQuery_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_Contact_DuplicateBaseRecord"></a> Contact_DuplicateBaseRecord

See contact Entity [Contact_DuplicateBaseRecord](contact.md#BKMK_Contact_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_DuplicateBaseRecord"></a> TransactionCurrency_DuplicateBaseRecord

See transactioncurrency Entity [TransactionCurrency_DuplicateBaseRecord](transactioncurrency.md#BKMK_TransactionCurrency_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Email_DuplicateBaseRecord"></a> Email_DuplicateBaseRecord

See email Entity [Email_DuplicateBaseRecord](email.md#BKMK_Email_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_PhoneCall_DuplicateMatchingRecord"></a> PhoneCall_DuplicateMatchingRecord

See phonecall Entity [PhoneCall_DuplicateMatchingRecord](phonecall.md#BKMK_PhoneCall_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_Team_DuplicateMatchingRecord"></a> Team_DuplicateMatchingRecord

See team Entity [Team_DuplicateMatchingRecord](team.md#BKMK_Team_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_SystemUser_DuplicateMatchingRecord"></a> SystemUser_DuplicateMatchingRecord

See systemuser Entity [SystemUser_DuplicateMatchingRecord](systemuser.md#BKMK_SystemUser_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_Appointment_DuplicateMatchingRecord"></a> Appointment_DuplicateMatchingRecord

See appointment Entity [Appointment_DuplicateMatchingRecord](appointment.md#BKMK_Appointment_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_Account_DuplicateMatchingRecord"></a> Account_DuplicateMatchingRecord

See account Entity [Account_DuplicateMatchingRecord](account.md#BKMK_Account_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_Fax_DuplicateBaseRecord"></a> Fax_DuplicateBaseRecord

See fax Entity [Fax_DuplicateBaseRecord](fax.md#BKMK_Fax_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Letter_DuplicateMatchingRecord"></a> Letter_DuplicateMatchingRecord

See letter Entity [Letter_DuplicateMatchingRecord](letter.md#BKMK_Letter_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_emailserverprofile_duplicatematchingrecord"></a> emailserverprofile_duplicatematchingrecord

See emailserverprofile Entity [emailserverprofile_duplicatematchingrecord](emailserverprofile.md#BKMK_emailserverprofile_duplicatematchingrecord) One-To-Many relationship.

### <a name="BKMK_SharePointDocumentLocation_DuplicateBaseRecord"></a> SharePointDocumentLocation_DuplicateBaseRecord

See sharepointdocumentlocation Entity [SharePointDocumentLocation_DuplicateBaseRecord](sharepointdocumentlocation.md#BKMK_SharePointDocumentLocation_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Goal_DuplicateBaseRecord"></a> Goal_DuplicateBaseRecord

See goal Entity [Goal_DuplicateBaseRecord](goal.md#BKMK_Goal_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_RecurringAppointmentMaster_DuplicateMatchingRecord"></a> RecurringAppointmentMaster_DuplicateMatchingRecord

See recurringappointmentmaster Entity [RecurringAppointmentMaster_DuplicateMatchingRecord](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_Task_DuplicateBaseRecord"></a> Task_DuplicateBaseRecord

See task Entity [Task_DuplicateBaseRecord](task.md#BKMK_Task_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_RecurringAppointmentMaster_DuplicateBaseRecord"></a> RecurringAppointmentMaster_DuplicateBaseRecord

See recurringappointmentmaster Entity [RecurringAppointmentMaster_DuplicateBaseRecord](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Queue_DuplicateMatchingRecord"></a> Queue_DuplicateMatchingRecord

See queue Entity [Queue_DuplicateMatchingRecord](queue.md#BKMK_Queue_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_SocialProfile_DuplicateBaseRecord"></a> SocialProfile_DuplicateBaseRecord

See socialprofile Entity [SocialProfile_DuplicateBaseRecord](socialprofile.md#BKMK_SocialProfile_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_SharePointDocumentLocation_DuplicateMatchingRecord"></a> SharePointDocumentLocation_DuplicateMatchingRecord

See sharepointdocumentlocation Entity [SharePointDocumentLocation_DuplicateMatchingRecord](sharepointdocumentlocation.md#BKMK_SharePointDocumentLocation_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_GoalRollupQuery_DuplicateBaseRecord"></a> GoalRollupQuery_DuplicateBaseRecord

See goalrollupquery Entity [GoalRollupQuery_DuplicateBaseRecord](goalrollupquery.md#BKMK_GoalRollupQuery_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_AsyncOperation_DuplicateBaseRecord"></a> AsyncOperation_DuplicateBaseRecord

See asyncoperation Entity [AsyncOperation_DuplicateBaseRecord](asyncoperation.md#BKMK_AsyncOperation_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Fax_DuplicateMatchingRecord"></a> Fax_DuplicateMatchingRecord

See fax Entity [Fax_DuplicateMatchingRecord](fax.md#BKMK_Fax_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_SocialActivity_DuplicateMatchingRecord"></a> SocialActivity_DuplicateMatchingRecord

See socialactivity Entity [SocialActivity_DuplicateMatchingRecord](socialactivity.md#BKMK_SocialActivity_DuplicateMatchingRecord) One-To-Many relationship.
duplicaterecord

