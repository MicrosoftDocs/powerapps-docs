---
title: "DuplicateRecord Entity Reference (Common Data Service)| MicrosoftDocs"
description: "Includes schema information and supported messages for the DuplicateRecord entity in Common Data Service."
ms.date: 11/07/2019
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
---
# DuplicateRecord Entity Reference

Potential duplicate record.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Retrieve|GET [*org URI*]/api/data/v9.0/duplicaterecords(*duplicateid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/duplicaterecords<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Entity Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|DuplicateRecords|
|DisplayCollectionName|Duplicate Records|
|DisplayName|Duplicate Record|
|EntitySetName|duplicaterecords|
|IsBPFEntity|False|
|LogicalCollectionName|duplicaterecords|
|LogicalName|duplicaterecord|
|OwnershipType|None|
|PrimaryIdAttribute|duplicateid|
|PrimaryNameAttribute||
|SchemaName|DuplicateRecord|

<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.


### <a name="BKMK_DuplicateId"></a> DuplicateId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the duplicate record.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|duplicateid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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

|Property|Value|
|--------|-----|
|Description|Unique identifier of the system job that created this record.|
|DisplayName|System Job|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|asyncoperationid|
|RequiredLevel|None|
|Targets|asyncoperation|
|Type|Lookup|


### <a name="BKMK_BaseRecordId"></a> BaseRecordId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the base record.|
|DisplayName|Base Record ID|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|baserecordid|
|RequiredLevel|None|
|Targets|account,appointment,channelaccessprofile,connector,contact,email,emailserverprofile,environmentvariabledefinition,environmentvariablevalue,fax,feedback,goal,goalrollupquery,kbarticle,knowledgearticle,knowledgebaserecord,letter,msdyn_aiodimage,msdyn_aiodlabel,msdyn_aiodtrainingboundingbox,msdyn_aiodtrainingimage,msdyn_analysiscomponent,msdyn_analysisjob,msdyn_analysisresult,msdyn_analysisresultdetail,msdyn_knowledgearticleimage,msdyn_knowledgearticletemplate,msdyn_solutionhealthrule,msdyn_solutionhealthruleargument,msdyn_solutionhealthruleset,phonecall,publisher,queue,recurringappointmentmaster,sharepointdocumentlocation,sharepointsite,socialactivity,socialprofile,systemuser,task,team,transactioncurrency|
|Type|Lookup|


### <a name="BKMK_BaseRecordIdName"></a> BaseRecordIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|baserecordidname|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_BaseRecordIdTypeCode"></a> BaseRecordIdTypeCode

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|baserecordidtypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_BaseRecordIdYomiName"></a> BaseRecordIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|baserecordidyominame|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the duplicate record was created.|
|DisplayName||
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_DuplicateRecordId"></a> DuplicateRecordId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the potential duplicate record.|
|DisplayName|Duplicate Record ID|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|duplicaterecordid|
|RequiredLevel|None|
|Targets|account,appointment,channelaccessprofile,connector,contact,email,emailserverprofile,environmentvariabledefinition,environmentvariablevalue,fax,feedback,goal,goalrollupquery,kbarticle,knowledgearticle,knowledgebaserecord,letter,msdyn_aiodimage,msdyn_aiodlabel,msdyn_aiodtrainingboundingbox,msdyn_aiodtrainingimage,msdyn_analysiscomponent,msdyn_analysisjob,msdyn_analysisresult,msdyn_analysisresultdetail,msdyn_knowledgearticleimage,msdyn_knowledgearticletemplate,msdyn_solutionhealthrule,msdyn_solutionhealthruleargument,msdyn_solutionhealthruleset,phonecall,publisher,queue,recurringappointmentmaster,sharepointdocumentlocation,sharepointsite,socialactivity,socialprofile,systemuser,task,team,transactioncurrency|
|Type|Lookup|


### <a name="BKMK_DuplicateRecordIdName"></a> DuplicateRecordIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|duplicaterecordidname|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_DuplicateRecordIdTypeCode"></a> DuplicateRecordIdTypeCode

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|duplicaterecordidtypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_DuplicateRecordIdYomiName"></a> DuplicateRecordIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|duplicaterecordidyominame|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_DuplicateRuleId"></a> DuplicateRuleId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the duplicate rule against which this duplicate was found.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|duplicateruleid|
|RequiredLevel|None|
|Targets|duplicaterule|
|Type|Lookup|


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user or team who owns the duplicate record.|
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
|Description|Unique identifier of the business unit that owns the duplicate record.|
|DisplayName|Owning Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who owns the duplicate record.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [feedback_DuplicateMatchingRecord](#BKMK_feedback_DuplicateMatchingRecord)
- [feedback_DuplicateBaseRecord](#BKMK_feedback_DuplicateBaseRecord)
- [knowledgearticle_DuplicateMatchingRecord](#BKMK_knowledgearticle_DuplicateMatchingRecord)
- [knowledgearticle_DuplicateBaseRecord](#BKMK_knowledgearticle_DuplicateBaseRecord)
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
- [msdyn_knowledgearticleimage_DuplicateMatchingRecord](#BKMK_msdyn_knowledgearticleimage_DuplicateMatchingRecord)
- [msdyn_knowledgearticleimage_DuplicateBaseRecord](#BKMK_msdyn_knowledgearticleimage_DuplicateBaseRecord)
- [msdyn_knowledgearticletemplate_DuplicateMatchingRecord](#BKMK_msdyn_knowledgearticletemplate_DuplicateMatchingRecord)
- [msdyn_knowledgearticletemplate_DuplicateBaseRecord](#BKMK_msdyn_knowledgearticletemplate_DuplicateBaseRecord)
- [connector_DuplicateMatchingRecord](#BKMK_connector_DuplicateMatchingRecord)
- [connector_DuplicateBaseRecord](#BKMK_connector_DuplicateBaseRecord)
- [msdyn_aiodimage_DuplicateMatchingRecord](#BKMK_msdyn_aiodimage_DuplicateMatchingRecord)
- [msdyn_aiodimage_DuplicateBaseRecord](#BKMK_msdyn_aiodimage_DuplicateBaseRecord)
- [msdyn_aiodlabel_DuplicateMatchingRecord](#BKMK_msdyn_aiodlabel_DuplicateMatchingRecord)
- [msdyn_aiodlabel_DuplicateBaseRecord](#BKMK_msdyn_aiodlabel_DuplicateBaseRecord)
- [msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord](#BKMK_msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord)
- [msdyn_aiodtrainingboundingbox_DuplicateBaseRecord](#BKMK_msdyn_aiodtrainingboundingbox_DuplicateBaseRecord)
- [msdyn_aiodtrainingimage_DuplicateMatchingRecord](#BKMK_msdyn_aiodtrainingimage_DuplicateMatchingRecord)
- [msdyn_aiodtrainingimage_DuplicateBaseRecord](#BKMK_msdyn_aiodtrainingimage_DuplicateBaseRecord)
- [environmentvariabledefinition_DuplicateMatchingRecord](#BKMK_environmentvariabledefinition_DuplicateMatchingRecord)
- [environmentvariabledefinition_DuplicateBaseRecord](#BKMK_environmentvariabledefinition_DuplicateBaseRecord)
- [environmentvariablevalue_DuplicateMatchingRecord](#BKMK_environmentvariablevalue_DuplicateMatchingRecord)
- [environmentvariablevalue_DuplicateBaseRecord](#BKMK_environmentvariablevalue_DuplicateBaseRecord)
- [msdyn_analysiscomponent_DuplicateMatchingRecord](#BKMK_msdyn_analysiscomponent_DuplicateMatchingRecord)
- [msdyn_analysiscomponent_DuplicateBaseRecord](#BKMK_msdyn_analysiscomponent_DuplicateBaseRecord)
- [msdyn_analysisjob_DuplicateMatchingRecord](#BKMK_msdyn_analysisjob_DuplicateMatchingRecord)
- [msdyn_analysisjob_DuplicateBaseRecord](#BKMK_msdyn_analysisjob_DuplicateBaseRecord)
- [msdyn_analysisresult_DuplicateMatchingRecord](#BKMK_msdyn_analysisresult_DuplicateMatchingRecord)
- [msdyn_analysisresult_DuplicateBaseRecord](#BKMK_msdyn_analysisresult_DuplicateBaseRecord)
- [msdyn_analysisresultdetail_DuplicateMatchingRecord](#BKMK_msdyn_analysisresultdetail_DuplicateMatchingRecord)
- [msdyn_analysisresultdetail_DuplicateBaseRecord](#BKMK_msdyn_analysisresultdetail_DuplicateBaseRecord)
- [msdyn_solutionhealthrule_DuplicateMatchingRecord](#BKMK_msdyn_solutionhealthrule_DuplicateMatchingRecord)
- [msdyn_solutionhealthrule_DuplicateBaseRecord](#BKMK_msdyn_solutionhealthrule_DuplicateBaseRecord)
- [msdyn_solutionhealthruleargument_DuplicateMatchingRecord](#BKMK_msdyn_solutionhealthruleargument_DuplicateMatchingRecord)
- [msdyn_solutionhealthruleargument_DuplicateBaseRecord](#BKMK_msdyn_solutionhealthruleargument_DuplicateBaseRecord)
- [msdyn_solutionhealthruleset_DuplicateMatchingRecord](#BKMK_msdyn_solutionhealthruleset_DuplicateMatchingRecord)
- [msdyn_solutionhealthruleset_DuplicateBaseRecord](#BKMK_msdyn_solutionhealthruleset_DuplicateBaseRecord)


### <a name="BKMK_feedback_DuplicateMatchingRecord"></a> feedback_DuplicateMatchingRecord

See feedback Entity [feedback_DuplicateMatchingRecord](feedback.md#BKMK_feedback_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_feedback_DuplicateBaseRecord"></a> feedback_DuplicateBaseRecord

See feedback Entity [feedback_DuplicateBaseRecord](feedback.md#BKMK_feedback_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_DuplicateMatchingRecord"></a> knowledgearticle_DuplicateMatchingRecord

See knowledgearticle Entity [knowledgearticle_DuplicateMatchingRecord](knowledgearticle.md#BKMK_knowledgearticle_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_DuplicateBaseRecord"></a> knowledgearticle_DuplicateBaseRecord

See knowledgearticle Entity [knowledgearticle_DuplicateBaseRecord](knowledgearticle.md#BKMK_knowledgearticle_DuplicateBaseRecord) One-To-Many relationship.

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

### <a name="BKMK_msdyn_knowledgearticleimage_DuplicateMatchingRecord"></a> msdyn_knowledgearticleimage_DuplicateMatchingRecord

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgearticleimage Entity [msdyn_knowledgearticleimage_DuplicateMatchingRecord](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgearticleimage_DuplicateBaseRecord"></a> msdyn_knowledgearticleimage_DuplicateBaseRecord

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgearticleimage Entity [msdyn_knowledgearticleimage_DuplicateBaseRecord](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgearticletemplate_DuplicateMatchingRecord"></a> msdyn_knowledgearticletemplate_DuplicateMatchingRecord

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgearticletemplate Entity [msdyn_knowledgearticletemplate_DuplicateMatchingRecord](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgearticletemplate_DuplicateBaseRecord"></a> msdyn_knowledgearticletemplate_DuplicateBaseRecord

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgearticletemplate Entity [msdyn_knowledgearticletemplate_DuplicateBaseRecord](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_connector_DuplicateMatchingRecord"></a> connector_DuplicateMatchingRecord

**Added by**: Power Connector Solution Solution

See connector Entity [connector_DuplicateMatchingRecord](connector.md#BKMK_connector_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_connector_DuplicateBaseRecord"></a> connector_DuplicateBaseRecord

**Added by**: Power Connector Solution Solution

See connector Entity [connector_DuplicateBaseRecord](connector.md#BKMK_connector_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodimage_DuplicateMatchingRecord"></a> msdyn_aiodimage_DuplicateMatchingRecord

**Added by**: AI Solution default templates Solution

See msdyn_aiodimage Entity [msdyn_aiodimage_DuplicateMatchingRecord](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodimage_DuplicateBaseRecord"></a> msdyn_aiodimage_DuplicateBaseRecord

**Added by**: AI Solution default templates Solution

See msdyn_aiodimage Entity [msdyn_aiodimage_DuplicateBaseRecord](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodlabel_DuplicateMatchingRecord"></a> msdyn_aiodlabel_DuplicateMatchingRecord

**Added by**: AI Solution default templates Solution

See msdyn_aiodlabel Entity [msdyn_aiodlabel_DuplicateMatchingRecord](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodlabel_DuplicateBaseRecord"></a> msdyn_aiodlabel_DuplicateBaseRecord

**Added by**: AI Solution default templates Solution

See msdyn_aiodlabel Entity [msdyn_aiodlabel_DuplicateBaseRecord](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord"></a> msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord

**Added by**: AI Solution default templates Solution

See msdyn_aiodtrainingboundingbox Entity [msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodtrainingboundingbox_DuplicateBaseRecord"></a> msdyn_aiodtrainingboundingbox_DuplicateBaseRecord

**Added by**: AI Solution default templates Solution

See msdyn_aiodtrainingboundingbox Entity [msdyn_aiodtrainingboundingbox_DuplicateBaseRecord](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodtrainingimage_DuplicateMatchingRecord"></a> msdyn_aiodtrainingimage_DuplicateMatchingRecord

**Added by**: AI Solution default templates Solution

See msdyn_aiodtrainingimage Entity [msdyn_aiodtrainingimage_DuplicateMatchingRecord](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodtrainingimage_DuplicateBaseRecord"></a> msdyn_aiodtrainingimage_DuplicateBaseRecord

**Added by**: AI Solution default templates Solution

See msdyn_aiodtrainingimage Entity [msdyn_aiodtrainingimage_DuplicateBaseRecord](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_environmentvariabledefinition_DuplicateMatchingRecord"></a> environmentvariabledefinition_DuplicateMatchingRecord

**Added by**: Environment Variables Solution

See environmentvariabledefinition Entity [environmentvariabledefinition_DuplicateMatchingRecord](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_environmentvariabledefinition_DuplicateBaseRecord"></a> environmentvariabledefinition_DuplicateBaseRecord

**Added by**: Environment Variables Solution

See environmentvariabledefinition Entity [environmentvariabledefinition_DuplicateBaseRecord](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_environmentvariablevalue_DuplicateMatchingRecord"></a> environmentvariablevalue_DuplicateMatchingRecord

**Added by**: Environment Variables Solution

See environmentvariablevalue Entity [environmentvariablevalue_DuplicateMatchingRecord](environmentvariablevalue.md#BKMK_environmentvariablevalue_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_environmentvariablevalue_DuplicateBaseRecord"></a> environmentvariablevalue_DuplicateBaseRecord

**Added by**: Environment Variables Solution

See environmentvariablevalue Entity [environmentvariablevalue_DuplicateBaseRecord](environmentvariablevalue.md#BKMK_environmentvariablevalue_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_analysiscomponent_DuplicateMatchingRecord"></a> msdyn_analysiscomponent_DuplicateMatchingRecord

**Added by**: PowerApps Checker Solution

See msdyn_analysiscomponent Entity [msdyn_analysiscomponent_DuplicateMatchingRecord](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_analysiscomponent_DuplicateBaseRecord"></a> msdyn_analysiscomponent_DuplicateBaseRecord

**Added by**: PowerApps Checker Solution

See msdyn_analysiscomponent Entity [msdyn_analysiscomponent_DuplicateBaseRecord](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisjob_DuplicateMatchingRecord"></a> msdyn_analysisjob_DuplicateMatchingRecord

**Added by**: PowerApps Checker Solution

See msdyn_analysisjob Entity [msdyn_analysisjob_DuplicateMatchingRecord](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisjob_DuplicateBaseRecord"></a> msdyn_analysisjob_DuplicateBaseRecord

**Added by**: PowerApps Checker Solution

See msdyn_analysisjob Entity [msdyn_analysisjob_DuplicateBaseRecord](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisresult_DuplicateMatchingRecord"></a> msdyn_analysisresult_DuplicateMatchingRecord

**Added by**: PowerApps Checker Solution

See msdyn_analysisresult Entity [msdyn_analysisresult_DuplicateMatchingRecord](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisresult_DuplicateBaseRecord"></a> msdyn_analysisresult_DuplicateBaseRecord

**Added by**: PowerApps Checker Solution

See msdyn_analysisresult Entity [msdyn_analysisresult_DuplicateBaseRecord](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisresultdetail_DuplicateMatchingRecord"></a> msdyn_analysisresultdetail_DuplicateMatchingRecord

**Added by**: PowerApps Checker Solution

See msdyn_analysisresultdetail Entity [msdyn_analysisresultdetail_DuplicateMatchingRecord](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisresultdetail_DuplicateBaseRecord"></a> msdyn_analysisresultdetail_DuplicateBaseRecord

**Added by**: PowerApps Checker Solution

See msdyn_analysisresultdetail Entity [msdyn_analysisresultdetail_DuplicateBaseRecord](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthrule_DuplicateMatchingRecord"></a> msdyn_solutionhealthrule_DuplicateMatchingRecord

**Added by**: PowerApps Checker Solution

See msdyn_solutionhealthrule Entity [msdyn_solutionhealthrule_DuplicateMatchingRecord](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthrule_DuplicateBaseRecord"></a> msdyn_solutionhealthrule_DuplicateBaseRecord

**Added by**: PowerApps Checker Solution

See msdyn_solutionhealthrule Entity [msdyn_solutionhealthrule_DuplicateBaseRecord](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthruleargument_DuplicateMatchingRecord"></a> msdyn_solutionhealthruleargument_DuplicateMatchingRecord

**Added by**: PowerApps Checker Solution

See msdyn_solutionhealthruleargument Entity [msdyn_solutionhealthruleargument_DuplicateMatchingRecord](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthruleargument_DuplicateBaseRecord"></a> msdyn_solutionhealthruleargument_DuplicateBaseRecord

**Added by**: PowerApps Checker Solution

See msdyn_solutionhealthruleargument Entity [msdyn_solutionhealthruleargument_DuplicateBaseRecord](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthruleset_DuplicateMatchingRecord"></a> msdyn_solutionhealthruleset_DuplicateMatchingRecord

**Added by**: PowerApps Checker Solution

See msdyn_solutionhealthruleset Entity [msdyn_solutionhealthruleset_DuplicateMatchingRecord](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthruleset_DuplicateBaseRecord"></a> msdyn_solutionhealthruleset_DuplicateBaseRecord

**Added by**: PowerApps Checker Solution

See msdyn_solutionhealthruleset Entity [msdyn_solutionhealthruleset_DuplicateBaseRecord](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_DuplicateBaseRecord) One-To-Many relationship.

### See also

[About the Entity Reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.duplicaterecord?text=duplicaterecord EntityType" />