---
title: "DuplicateRecord table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the DuplicateRecord table/entity."
ms.date: 05/20/2021
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
  - D365CE
---

# DuplicateRecord table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Potential duplicate record.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Retrieve|GET [*org URI*]/api/data/v9.0/duplicaterecords(*duplicateid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/duplicaterecords<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

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

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.


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

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

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
|Targets|account,activityfileattachment,applicationuser,appnotification,appointment,canvasappextendedmetadata,cascadegrantrevokeaccessrecordstracker,cascadegrantrevokeaccessversiontracker,catalogassignment,channelaccessprofile,connector,contact,conversationtranscript,datalakefolder,datalakefolderpermission,datalakeworkspace,datalakeworkspacepermission,email,emailserverprofile,environmentvariabledefinition,environmentvariablevalue,exportsolutionupload,fax,feedback,flowmachinegroup,goal,goalrollupquery,kbarticle,keyvaultreference,knowledgearticle,knowledgebaserecord,letter,managedidentity,msdyn_aibdataset,msdyn_aibdatasetfile,msdyn_aibdatasetrecord,msdyn_aibdatasetscontainer,msdyn_aibfile,msdyn_aibfileattacheddata,msdyn_aiodimage,msdyn_aiodlabel,msdyn_aiodtrainingboundingbox,msdyn_aiodtrainingimage,msdyn_analysiscomponent,msdyn_analysisjob,msdyn_analysisresult,msdyn_analysisresultdetail,msdyn_dataflow,msdyn_federatedarticle,msdyn_federatedarticleincident,msdyn_kalanguagesetting,msdyn_kmfederatedsearchconfig,msdyn_knowledgearticleimage,msdyn_knowledgearticletemplate,msdyn_knowledgeinteractioninsight,msdyn_knowledgepersonalfilter,msdyn_knowledgesearchfilter,msdyn_knowledgesearchinsight,msdyn_pminferredtask,msdyn_pmrecording,msdyn_serviceconfiguration,msdyn_slakpi,msdyn_solutionhealthrule,msdyn_solutionhealthruleargument,msdyn_solutionhealthruleset,organizationdatasyncsubscription,organizationdatasyncsubscriptionentity,package,phonecall,publisher,queue,recurringappointmentmaster,revokeinheritedaccessrecordstracker,serviceplan,sharepointdocumentlocation,sharepointsite,socialactivity,socialprofile,solutioncomponentattributeconfiguration,solutioncomponentconfiguration,solutioncomponentrelationshipconfiguration,stagesolutionupload,systemuser,task,team,transactioncurrency|
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
|MaxLength|800|
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
|MaxLength|800|
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
|Targets|account,activityfileattachment,applicationuser,appnotification,appointment,canvasappextendedmetadata,cascadegrantrevokeaccessrecordstracker,cascadegrantrevokeaccessversiontracker,catalogassignment,channelaccessprofile,connector,contact,conversationtranscript,datalakefolder,datalakefolderpermission,datalakeworkspace,datalakeworkspacepermission,email,emailserverprofile,environmentvariabledefinition,environmentvariablevalue,exportsolutionupload,fax,feedback,flowmachinegroup,goal,goalrollupquery,kbarticle,keyvaultreference,knowledgearticle,knowledgebaserecord,letter,managedidentity,msdyn_aibdataset,msdyn_aibdatasetfile,msdyn_aibdatasetrecord,msdyn_aibdatasetscontainer,msdyn_aibfile,msdyn_aibfileattacheddata,msdyn_aiodimage,msdyn_aiodlabel,msdyn_aiodtrainingboundingbox,msdyn_aiodtrainingimage,msdyn_analysiscomponent,msdyn_analysisjob,msdyn_analysisresult,msdyn_analysisresultdetail,msdyn_dataflow,msdyn_federatedarticle,msdyn_federatedarticleincident,msdyn_kalanguagesetting,msdyn_kmfederatedsearchconfig,msdyn_knowledgearticleimage,msdyn_knowledgearticletemplate,msdyn_knowledgeinteractioninsight,msdyn_knowledgepersonalfilter,msdyn_knowledgesearchfilter,msdyn_knowledgesearchinsight,msdyn_pminferredtask,msdyn_pmrecording,msdyn_serviceconfiguration,msdyn_slakpi,msdyn_solutionhealthrule,msdyn_solutionhealthruleargument,msdyn_solutionhealthruleset,organizationdatasyncsubscription,organizationdatasyncsubscriptionentity,package,phonecall,publisher,queue,recurringappointmentmaster,revokeinheritedaccessrecordstracker,serviceplan,sharepointdocumentlocation,sharepointsite,socialactivity,socialprofile,solutioncomponentattributeconfiguration,solutioncomponentconfiguration,solutioncomponentrelationshipconfiguration,stagesolutionupload,systemuser,task,team,transactioncurrency|
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
|MaxLength|800|
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
|MaxLength|800|
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

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

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
- [feedback_DuplicateBaseRecord](#BKMK_feedback_DuplicateBaseRecord)
- [feedback_DuplicateMatchingRecord](#BKMK_feedback_DuplicateMatchingRecord)
- [solutioncomponentattributeconfiguration_DuplicateMatchingRecord](#BKMK_solutioncomponentattributeconfiguration_DuplicateMatchingRecord)
- [solutioncomponentattributeconfiguration_DuplicateBaseRecord](#BKMK_solutioncomponentattributeconfiguration_DuplicateBaseRecord)
- [solutioncomponentconfiguration_DuplicateMatchingRecord](#BKMK_solutioncomponentconfiguration_DuplicateMatchingRecord)
- [solutioncomponentconfiguration_DuplicateBaseRecord](#BKMK_solutioncomponentconfiguration_DuplicateBaseRecord)
- [solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord](#BKMK_solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord)
- [solutioncomponentrelationshipconfiguration_DuplicateBaseRecord](#BKMK_solutioncomponentrelationshipconfiguration_DuplicateBaseRecord)
- [package_DuplicateMatchingRecord](#BKMK_package_DuplicateMatchingRecord)
- [package_DuplicateBaseRecord](#BKMK_package_DuplicateBaseRecord)
- [stagesolutionupload_DuplicateMatchingRecord](#BKMK_stagesolutionupload_DuplicateMatchingRecord)
- [stagesolutionupload_DuplicateBaseRecord](#BKMK_stagesolutionupload_DuplicateBaseRecord)
- [exportsolutionupload_DuplicateMatchingRecord](#BKMK_exportsolutionupload_DuplicateMatchingRecord)
- [exportsolutionupload_DuplicateBaseRecord](#BKMK_exportsolutionupload_DuplicateBaseRecord)
- [datalakefolder_DuplicateMatchingRecord](#BKMK_datalakefolder_DuplicateMatchingRecord)
- [datalakefolder_DuplicateBaseRecord](#BKMK_datalakefolder_DuplicateBaseRecord)
- [datalakefolderpermission_DuplicateMatchingRecord](#BKMK_datalakefolderpermission_DuplicateMatchingRecord)
- [datalakefolderpermission_DuplicateBaseRecord](#BKMK_datalakefolderpermission_DuplicateBaseRecord)
- [datalakeworkspace_DuplicateMatchingRecord](#BKMK_datalakeworkspace_DuplicateMatchingRecord)
- [datalakeworkspace_DuplicateBaseRecord](#BKMK_datalakeworkspace_DuplicateBaseRecord)
- [datalakeworkspacepermission_DuplicateMatchingRecord](#BKMK_datalakeworkspacepermission_DuplicateMatchingRecord)
- [datalakeworkspacepermission_DuplicateBaseRecord](#BKMK_datalakeworkspacepermission_DuplicateBaseRecord)
- [msdyn_dataflow_DuplicateMatchingRecord](#BKMK_msdyn_dataflow_DuplicateMatchingRecord)
- [msdyn_dataflow_DuplicateBaseRecord](#BKMK_msdyn_dataflow_DuplicateBaseRecord)
- [serviceplan_DuplicateMatchingRecord](#BKMK_serviceplan_DuplicateMatchingRecord)
- [serviceplan_DuplicateBaseRecord](#BKMK_serviceplan_DuplicateBaseRecord)
- [applicationuser_DuplicateMatchingRecord](#BKMK_applicationuser_DuplicateMatchingRecord)
- [applicationuser_DuplicateBaseRecord](#BKMK_applicationuser_DuplicateBaseRecord)
- [connector_DuplicateMatchingRecord](#BKMK_connector_DuplicateMatchingRecord)
- [connector_DuplicateBaseRecord](#BKMK_connector_DuplicateBaseRecord)
- [environmentvariabledefinition_DuplicateMatchingRecord](#BKMK_environmentvariabledefinition_DuplicateMatchingRecord)
- [environmentvariabledefinition_DuplicateBaseRecord](#BKMK_environmentvariabledefinition_DuplicateBaseRecord)
- [environmentvariablevalue_DuplicateMatchingRecord](#BKMK_environmentvariablevalue_DuplicateMatchingRecord)
- [environmentvariablevalue_DuplicateBaseRecord](#BKMK_environmentvariablevalue_DuplicateBaseRecord)
- [flowmachinegroup_DuplicateMatchingRecord](#BKMK_flowmachinegroup_DuplicateMatchingRecord)
- [flowmachinegroup_DuplicateBaseRecord](#BKMK_flowmachinegroup_DuplicateBaseRecord)
- [conversationtranscript_DuplicateMatchingRecord](#BKMK_conversationtranscript_DuplicateMatchingRecord)
- [conversationtranscript_DuplicateBaseRecord](#BKMK_conversationtranscript_DuplicateBaseRecord)
- [activityfileattachment_DuplicateMatchingRecord](#BKMK_activityfileattachment_DuplicateMatchingRecord)
- [activityfileattachment_DuplicateBaseRecord](#BKMK_activityfileattachment_DuplicateBaseRecord)
- [msdyn_serviceconfiguration_DuplicateMatchingRecord](#BKMK_msdyn_serviceconfiguration_DuplicateMatchingRecord)
- [msdyn_serviceconfiguration_DuplicateBaseRecord](#BKMK_msdyn_serviceconfiguration_DuplicateBaseRecord)
- [msdyn_slakpi_DuplicateMatchingRecord](#BKMK_msdyn_slakpi_DuplicateMatchingRecord)
- [msdyn_slakpi_DuplicateBaseRecord](#BKMK_msdyn_slakpi_DuplicateBaseRecord)
- [msdyn_federatedarticle_DuplicateMatchingRecord](#BKMK_msdyn_federatedarticle_DuplicateMatchingRecord)
- [msdyn_federatedarticle_DuplicateBaseRecord](#BKMK_msdyn_federatedarticle_DuplicateBaseRecord)
- [msdyn_federatedarticleincident_DuplicateMatchingRecord](#BKMK_msdyn_federatedarticleincident_DuplicateMatchingRecord)
- [msdyn_federatedarticleincident_DuplicateBaseRecord](#BKMK_msdyn_federatedarticleincident_DuplicateBaseRecord)
- [msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord](#BKMK_msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord)
- [msdyn_kmfederatedsearchconfig_DuplicateBaseRecord](#BKMK_msdyn_kmfederatedsearchconfig_DuplicateBaseRecord)
- [msdyn_knowledgearticleimage_DuplicateMatchingRecord](#BKMK_msdyn_knowledgearticleimage_DuplicateMatchingRecord)
- [msdyn_knowledgearticleimage_DuplicateBaseRecord](#BKMK_msdyn_knowledgearticleimage_DuplicateBaseRecord)
- [msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord](#BKMK_msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord)
- [msdyn_knowledgeinteractioninsight_DuplicateBaseRecord](#BKMK_msdyn_knowledgeinteractioninsight_DuplicateBaseRecord)
- [msdyn_knowledgesearchinsight_DuplicateMatchingRecord](#BKMK_msdyn_knowledgesearchinsight_DuplicateMatchingRecord)
- [msdyn_knowledgesearchinsight_DuplicateBaseRecord](#BKMK_msdyn_knowledgesearchinsight_DuplicateBaseRecord)
- [msdyn_kalanguagesetting_DuplicateMatchingRecord](#BKMK_msdyn_kalanguagesetting_DuplicateMatchingRecord)
- [msdyn_kalanguagesetting_DuplicateBaseRecord](#BKMK_msdyn_kalanguagesetting_DuplicateBaseRecord)
- [msdyn_knowledgearticletemplate_DuplicateMatchingRecord](#BKMK_msdyn_knowledgearticletemplate_DuplicateMatchingRecord)
- [msdyn_knowledgearticletemplate_DuplicateBaseRecord](#BKMK_msdyn_knowledgearticletemplate_DuplicateBaseRecord)
- [msdyn_knowledgepersonalfilter_DuplicateMatchingRecord](#BKMK_msdyn_knowledgepersonalfilter_DuplicateMatchingRecord)
- [msdyn_knowledgepersonalfilter_DuplicateBaseRecord](#BKMK_msdyn_knowledgepersonalfilter_DuplicateBaseRecord)
- [msdyn_knowledgesearchfilter_DuplicateMatchingRecord](#BKMK_msdyn_knowledgesearchfilter_DuplicateMatchingRecord)
- [msdyn_knowledgesearchfilter_DuplicateBaseRecord](#BKMK_msdyn_knowledgesearchfilter_DuplicateBaseRecord)
- [keyvaultreference_DuplicateMatchingRecord](#BKMK_keyvaultreference_DuplicateMatchingRecord)
- [keyvaultreference_DuplicateBaseRecord](#BKMK_keyvaultreference_DuplicateBaseRecord)
- [managedidentity_DuplicateMatchingRecord](#BKMK_managedidentity_DuplicateMatchingRecord)
- [managedidentity_DuplicateBaseRecord](#BKMK_managedidentity_DuplicateBaseRecord)
- [catalogassignment_DuplicateMatchingRecord](#BKMK_catalogassignment_DuplicateMatchingRecord)
- [catalogassignment_DuplicateBaseRecord](#BKMK_catalogassignment_DuplicateBaseRecord)
- [organizationdatasyncsubscription_DuplicateMatchingRecord](#BKMK_organizationdatasyncsubscription_DuplicateMatchingRecord)
- [organizationdatasyncsubscription_DuplicateBaseRecord](#BKMK_organizationdatasyncsubscription_DuplicateBaseRecord)
- [organizationdatasyncsubscriptionentity_DuplicateMatchingRecord](#BKMK_organizationdatasyncsubscriptionentity_DuplicateMatchingRecord)
- [organizationdatasyncsubscriptionentity_DuplicateBaseRecord](#BKMK_organizationdatasyncsubscriptionentity_DuplicateBaseRecord)
- [appnotification_DuplicateMatchingRecord](#BKMK_appnotification_DuplicateMatchingRecord)
- [appnotification_DuplicateBaseRecord](#BKMK_appnotification_DuplicateBaseRecord)
- [msdyn_aibdataset_DuplicateMatchingRecord](#BKMK_msdyn_aibdataset_DuplicateMatchingRecord)
- [msdyn_aibdataset_DuplicateBaseRecord](#BKMK_msdyn_aibdataset_DuplicateBaseRecord)
- [msdyn_aibdatasetfile_DuplicateMatchingRecord](#BKMK_msdyn_aibdatasetfile_DuplicateMatchingRecord)
- [msdyn_aibdatasetfile_DuplicateBaseRecord](#BKMK_msdyn_aibdatasetfile_DuplicateBaseRecord)
- [msdyn_aibdatasetrecord_DuplicateMatchingRecord](#BKMK_msdyn_aibdatasetrecord_DuplicateMatchingRecord)
- [msdyn_aibdatasetrecord_DuplicateBaseRecord](#BKMK_msdyn_aibdatasetrecord_DuplicateBaseRecord)
- [msdyn_aibdatasetscontainer_DuplicateMatchingRecord](#BKMK_msdyn_aibdatasetscontainer_DuplicateMatchingRecord)
- [msdyn_aibdatasetscontainer_DuplicateBaseRecord](#BKMK_msdyn_aibdatasetscontainer_DuplicateBaseRecord)
- [msdyn_aibfile_DuplicateMatchingRecord](#BKMK_msdyn_aibfile_DuplicateMatchingRecord)
- [msdyn_aibfile_DuplicateBaseRecord](#BKMK_msdyn_aibfile_DuplicateBaseRecord)
- [msdyn_aibfileattacheddata_DuplicateMatchingRecord](#BKMK_msdyn_aibfileattacheddata_DuplicateMatchingRecord)
- [msdyn_aibfileattacheddata_DuplicateBaseRecord](#BKMK_msdyn_aibfileattacheddata_DuplicateBaseRecord)
- [msdyn_aiodimage_DuplicateMatchingRecord](#BKMK_msdyn_aiodimage_DuplicateMatchingRecord)
- [msdyn_aiodimage_DuplicateBaseRecord](#BKMK_msdyn_aiodimage_DuplicateBaseRecord)
- [msdyn_aiodlabel_DuplicateMatchingRecord](#BKMK_msdyn_aiodlabel_DuplicateMatchingRecord)
- [msdyn_aiodlabel_DuplicateBaseRecord](#BKMK_msdyn_aiodlabel_DuplicateBaseRecord)
- [msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord](#BKMK_msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord)
- [msdyn_aiodtrainingboundingbox_DuplicateBaseRecord](#BKMK_msdyn_aiodtrainingboundingbox_DuplicateBaseRecord)
- [msdyn_aiodtrainingimage_DuplicateMatchingRecord](#BKMK_msdyn_aiodtrainingimage_DuplicateMatchingRecord)
- [msdyn_aiodtrainingimage_DuplicateBaseRecord](#BKMK_msdyn_aiodtrainingimage_DuplicateBaseRecord)
- [msdyn_pminferredtask_DuplicateMatchingRecord](#BKMK_msdyn_pminferredtask_DuplicateMatchingRecord)
- [msdyn_pminferredtask_DuplicateBaseRecord](#BKMK_msdyn_pminferredtask_DuplicateBaseRecord)
- [msdyn_pmrecording_DuplicateMatchingRecord](#BKMK_msdyn_pmrecording_DuplicateMatchingRecord)
- [msdyn_pmrecording_DuplicateBaseRecord](#BKMK_msdyn_pmrecording_DuplicateBaseRecord)
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


### <a name="BKMK_knowledgearticle_DuplicateMatchingRecord"></a> knowledgearticle_DuplicateMatchingRecord

See knowledgearticle Table [knowledgearticle_DuplicateMatchingRecord](knowledgearticle.md#BKMK_knowledgearticle_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_DuplicateBaseRecord"></a> knowledgearticle_DuplicateBaseRecord

See knowledgearticle Table [knowledgearticle_DuplicateBaseRecord](knowledgearticle.md#BKMK_knowledgearticle_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_KnowledgeBaseRecord_DuplicateMatchingRecord"></a> KnowledgeBaseRecord_DuplicateMatchingRecord

See knowledgebaserecord Table [KnowledgeBaseRecord_DuplicateMatchingRecord](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_KnowledgeBaseRecord_DuplicateBaseRecord"></a> KnowledgeBaseRecord_DuplicateBaseRecord

See knowledgebaserecord Table [KnowledgeBaseRecord_DuplicateBaseRecord](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Email_DuplicateMatchingRecord"></a> Email_DuplicateMatchingRecord

See email Table [Email_DuplicateMatchingRecord](email.md#BKMK_Email_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_Publisher_DuplicateMatchingRecord"></a> Publisher_DuplicateMatchingRecord

See publisher Table [Publisher_DuplicateMatchingRecord](publisher.md#BKMK_Publisher_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_Queue_DuplicateBaseRecord"></a> Queue_DuplicateBaseRecord

See queue Table [Queue_DuplicateBaseRecord](queue.md#BKMK_Queue_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Letter_DuplicateBaseRecord"></a> Letter_DuplicateBaseRecord

See letter Table [Letter_DuplicateBaseRecord](letter.md#BKMK_Letter_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Team_DuplicateBaseRecord"></a> Team_DuplicateBaseRecord

See team Table [Team_DuplicateBaseRecord](team.md#BKMK_Team_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_KbArticle_DuplicateMatchingRecord"></a> KbArticle_DuplicateMatchingRecord

See kbarticle Table [KbArticle_DuplicateMatchingRecord](kbarticle.md#BKMK_KbArticle_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_Appointment_DuplicateBaseRecord"></a> Appointment_DuplicateBaseRecord

See appointment Table [Appointment_DuplicateBaseRecord](appointment.md#BKMK_Appointment_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Account_DuplicateBaseRecord"></a> Account_DuplicateBaseRecord

See account Table [Account_DuplicateBaseRecord](account.md#BKMK_Account_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_DuplicateRule_DuplicateBaseRecord"></a> DuplicateRule_DuplicateBaseRecord

See duplicaterule Table [DuplicateRule_DuplicateBaseRecord](duplicaterule.md#BKMK_DuplicateRule_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_SharePointSite_DuplicateBaseRecord"></a> SharePointSite_DuplicateBaseRecord

See sharepointsite Table [SharePointSite_DuplicateBaseRecord](sharepointsite.md#BKMK_SharePointSite_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_KbArticle_DuplicateBaseRecord"></a> KbArticle_DuplicateBaseRecord

See kbarticle Table [KbArticle_DuplicateBaseRecord](kbarticle.md#BKMK_KbArticle_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Task_DuplicateMatchingRecord"></a> Task_DuplicateMatchingRecord

See task Table [Task_DuplicateMatchingRecord](task.md#BKMK_Task_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_SocialProfile_DuplicateMatchingRecord"></a> SocialProfile_DuplicateMatchingRecord

See socialprofile Table [SocialProfile_DuplicateMatchingRecord](socialprofile.md#BKMK_SocialProfile_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_PhoneCall_DuplicateBaseRecord"></a> PhoneCall_DuplicateBaseRecord

See phonecall Table [PhoneCall_DuplicateBaseRecord](phonecall.md#BKMK_PhoneCall_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_DuplicateMatchingRecord"></a> TransactionCurrency_DuplicateMatchingRecord

See transactioncurrency Table [TransactionCurrency_DuplicateMatchingRecord](transactioncurrency.md#BKMK_TransactionCurrency_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_Goal_DuplicateMatchingRecord"></a> Goal_DuplicateMatchingRecord

See goal Table [Goal_DuplicateMatchingRecord](goal.md#BKMK_Goal_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_SharePointSite_DuplicateMatchingRecord"></a> SharePointSite_DuplicateMatchingRecord

See sharepointsite Table [SharePointSite_DuplicateMatchingRecord](sharepointsite.md#BKMK_SharePointSite_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_emailserverprofile_duplicatebaserecord"></a> emailserverprofile_duplicatebaserecord

See emailserverprofile Table [emailserverprofile_duplicatebaserecord](emailserverprofile.md#BKMK_emailserverprofile_duplicatebaserecord) One-To-Many relationship.

### <a name="BKMK_Publisher_DuplicateBaseRecord"></a> Publisher_DuplicateBaseRecord

See publisher Table [Publisher_DuplicateBaseRecord](publisher.md#BKMK_Publisher_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_SystemUser_DuplicateBaseRecord"></a> SystemUser_DuplicateBaseRecord

See systemuser Table [SystemUser_DuplicateBaseRecord](systemuser.md#BKMK_SystemUser_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_SocialActivity_DuplicateBaseRecord"></a> SocialActivity_DuplicateBaseRecord

See socialactivity Table [SocialActivity_DuplicateBaseRecord](socialactivity.md#BKMK_SocialActivity_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Contact_DuplicateMatchingRecord"></a> Contact_DuplicateMatchingRecord

See contact Table [Contact_DuplicateMatchingRecord](contact.md#BKMK_Contact_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_GoalRollupQuery_DuplicateMatchingRecord"></a> GoalRollupQuery_DuplicateMatchingRecord

See goalrollupquery Table [GoalRollupQuery_DuplicateMatchingRecord](goalrollupquery.md#BKMK_GoalRollupQuery_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_Contact_DuplicateBaseRecord"></a> Contact_DuplicateBaseRecord

See contact Table [Contact_DuplicateBaseRecord](contact.md#BKMK_Contact_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_DuplicateBaseRecord"></a> TransactionCurrency_DuplicateBaseRecord

See transactioncurrency Table [TransactionCurrency_DuplicateBaseRecord](transactioncurrency.md#BKMK_TransactionCurrency_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Email_DuplicateBaseRecord"></a> Email_DuplicateBaseRecord

See email Table [Email_DuplicateBaseRecord](email.md#BKMK_Email_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_PhoneCall_DuplicateMatchingRecord"></a> PhoneCall_DuplicateMatchingRecord

See phonecall Table [PhoneCall_DuplicateMatchingRecord](phonecall.md#BKMK_PhoneCall_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_Team_DuplicateMatchingRecord"></a> Team_DuplicateMatchingRecord

See team Table [Team_DuplicateMatchingRecord](team.md#BKMK_Team_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_SystemUser_DuplicateMatchingRecord"></a> SystemUser_DuplicateMatchingRecord

See systemuser Table [SystemUser_DuplicateMatchingRecord](systemuser.md#BKMK_SystemUser_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_Appointment_DuplicateMatchingRecord"></a> Appointment_DuplicateMatchingRecord

See appointment Table [Appointment_DuplicateMatchingRecord](appointment.md#BKMK_Appointment_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_Account_DuplicateMatchingRecord"></a> Account_DuplicateMatchingRecord

See account Table [Account_DuplicateMatchingRecord](account.md#BKMK_Account_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_Fax_DuplicateBaseRecord"></a> Fax_DuplicateBaseRecord

See fax Table [Fax_DuplicateBaseRecord](fax.md#BKMK_Fax_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Letter_DuplicateMatchingRecord"></a> Letter_DuplicateMatchingRecord

See letter Table [Letter_DuplicateMatchingRecord](letter.md#BKMK_Letter_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_emailserverprofile_duplicatematchingrecord"></a> emailserverprofile_duplicatematchingrecord

See emailserverprofile Table [emailserverprofile_duplicatematchingrecord](emailserverprofile.md#BKMK_emailserverprofile_duplicatematchingrecord) One-To-Many relationship.

### <a name="BKMK_SharePointDocumentLocation_DuplicateBaseRecord"></a> SharePointDocumentLocation_DuplicateBaseRecord

See sharepointdocumentlocation Table [SharePointDocumentLocation_DuplicateBaseRecord](sharepointdocumentlocation.md#BKMK_SharePointDocumentLocation_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Goal_DuplicateBaseRecord"></a> Goal_DuplicateBaseRecord

See goal Table [Goal_DuplicateBaseRecord](goal.md#BKMK_Goal_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_RecurringAppointmentMaster_DuplicateMatchingRecord"></a> RecurringAppointmentMaster_DuplicateMatchingRecord

See recurringappointmentmaster Table [RecurringAppointmentMaster_DuplicateMatchingRecord](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_Task_DuplicateBaseRecord"></a> Task_DuplicateBaseRecord

See task Table [Task_DuplicateBaseRecord](task.md#BKMK_Task_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_RecurringAppointmentMaster_DuplicateBaseRecord"></a> RecurringAppointmentMaster_DuplicateBaseRecord

See recurringappointmentmaster Table [RecurringAppointmentMaster_DuplicateBaseRecord](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Queue_DuplicateMatchingRecord"></a> Queue_DuplicateMatchingRecord

See queue Table [Queue_DuplicateMatchingRecord](queue.md#BKMK_Queue_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_SocialProfile_DuplicateBaseRecord"></a> SocialProfile_DuplicateBaseRecord

See socialprofile Table [SocialProfile_DuplicateBaseRecord](socialprofile.md#BKMK_SocialProfile_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_SharePointDocumentLocation_DuplicateMatchingRecord"></a> SharePointDocumentLocation_DuplicateMatchingRecord

See sharepointdocumentlocation Table [SharePointDocumentLocation_DuplicateMatchingRecord](sharepointdocumentlocation.md#BKMK_SharePointDocumentLocation_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_GoalRollupQuery_DuplicateBaseRecord"></a> GoalRollupQuery_DuplicateBaseRecord

See goalrollupquery Table [GoalRollupQuery_DuplicateBaseRecord](goalrollupquery.md#BKMK_GoalRollupQuery_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_AsyncOperation_DuplicateBaseRecord"></a> AsyncOperation_DuplicateBaseRecord

See asyncoperation Table [AsyncOperation_DuplicateBaseRecord](asyncoperation.md#BKMK_AsyncOperation_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_Fax_DuplicateMatchingRecord"></a> Fax_DuplicateMatchingRecord

See fax Table [Fax_DuplicateMatchingRecord](fax.md#BKMK_Fax_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_SocialActivity_DuplicateMatchingRecord"></a> SocialActivity_DuplicateMatchingRecord

See socialactivity Table [SocialActivity_DuplicateMatchingRecord](socialactivity.md#BKMK_SocialActivity_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_feedback_DuplicateBaseRecord"></a> feedback_DuplicateBaseRecord

See feedback Table [feedback_DuplicateBaseRecord](feedback.md#BKMK_feedback_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_feedback_DuplicateMatchingRecord"></a> feedback_DuplicateMatchingRecord

See feedback Table [feedback_DuplicateMatchingRecord](feedback.md#BKMK_feedback_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_solutioncomponentattributeconfiguration_DuplicateMatchingRecord"></a> solutioncomponentattributeconfiguration_DuplicateMatchingRecord

**Added by**: Solution Component Configuration Solution

See solutioncomponentattributeconfiguration Table [solutioncomponentattributeconfiguration_DuplicateMatchingRecord](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_solutioncomponentattributeconfiguration_DuplicateBaseRecord"></a> solutioncomponentattributeconfiguration_DuplicateBaseRecord

**Added by**: Solution Component Configuration Solution

See solutioncomponentattributeconfiguration Table [solutioncomponentattributeconfiguration_DuplicateBaseRecord](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_solutioncomponentconfiguration_DuplicateMatchingRecord"></a> solutioncomponentconfiguration_DuplicateMatchingRecord

**Added by**: Solution Component Configuration Solution

See solutioncomponentconfiguration Table [solutioncomponentconfiguration_DuplicateMatchingRecord](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_solutioncomponentconfiguration_DuplicateBaseRecord"></a> solutioncomponentconfiguration_DuplicateBaseRecord

**Added by**: Solution Component Configuration Solution

See solutioncomponentconfiguration Table [solutioncomponentconfiguration_DuplicateBaseRecord](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord"></a> solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord

**Added by**: Solution Component Configuration Solution

See solutioncomponentrelationshipconfiguration Table [solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_solutioncomponentrelationshipconfiguration_DuplicateBaseRecord"></a> solutioncomponentrelationshipconfiguration_DuplicateBaseRecord

**Added by**: Solution Component Configuration Solution

See solutioncomponentrelationshipconfiguration Table [solutioncomponentrelationshipconfiguration_DuplicateBaseRecord](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_package_DuplicateMatchingRecord"></a> package_DuplicateMatchingRecord

**Added by**: msdyn_SolutionPackageMapping Solution

See package Table [package_DuplicateMatchingRecord](package.md#BKMK_package_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_package_DuplicateBaseRecord"></a> package_DuplicateBaseRecord

**Added by**: msdyn_SolutionPackageMapping Solution

See package Table [package_DuplicateBaseRecord](package.md#BKMK_package_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_stagesolutionupload_DuplicateMatchingRecord"></a> stagesolutionupload_DuplicateMatchingRecord

**Added by**: StageSolutionUpload Solution

See stagesolutionupload Table [stagesolutionupload_DuplicateMatchingRecord](stagesolutionupload.md#BKMK_stagesolutionupload_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_stagesolutionupload_DuplicateBaseRecord"></a> stagesolutionupload_DuplicateBaseRecord

**Added by**: StageSolutionUpload Solution

See stagesolutionupload Table [stagesolutionupload_DuplicateBaseRecord](stagesolutionupload.md#BKMK_stagesolutionupload_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_exportsolutionupload_DuplicateMatchingRecord"></a> exportsolutionupload_DuplicateMatchingRecord

**Added by**: ExportSolutionUpload Solution

See exportsolutionupload Table [exportsolutionupload_DuplicateMatchingRecord](exportsolutionupload.md#BKMK_exportsolutionupload_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_exportsolutionupload_DuplicateBaseRecord"></a> exportsolutionupload_DuplicateBaseRecord

**Added by**: ExportSolutionUpload Solution

See exportsolutionupload Table [exportsolutionupload_DuplicateBaseRecord](exportsolutionupload.md#BKMK_exportsolutionupload_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_datalakefolder_DuplicateMatchingRecord"></a> datalakefolder_DuplicateMatchingRecord

**Added by**: Data lake workspaces Solution

See datalakefolder Table [datalakefolder_DuplicateMatchingRecord](datalakefolder.md#BKMK_datalakefolder_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_datalakefolder_DuplicateBaseRecord"></a> datalakefolder_DuplicateBaseRecord

**Added by**: Data lake workspaces Solution

See datalakefolder Table [datalakefolder_DuplicateBaseRecord](datalakefolder.md#BKMK_datalakefolder_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_datalakefolderpermission_DuplicateMatchingRecord"></a> datalakefolderpermission_DuplicateMatchingRecord

**Added by**: Data lake workspaces Solution

See datalakefolderpermission Table [datalakefolderpermission_DuplicateMatchingRecord](datalakefolderpermission.md#BKMK_datalakefolderpermission_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_datalakefolderpermission_DuplicateBaseRecord"></a> datalakefolderpermission_DuplicateBaseRecord

**Added by**: Data lake workspaces Solution

See datalakefolderpermission Table [datalakefolderpermission_DuplicateBaseRecord](datalakefolderpermission.md#BKMK_datalakefolderpermission_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_datalakeworkspace_DuplicateMatchingRecord"></a> datalakeworkspace_DuplicateMatchingRecord

**Added by**: Data lake workspaces Solution

See datalakeworkspace Table [datalakeworkspace_DuplicateMatchingRecord](datalakeworkspace.md#BKMK_datalakeworkspace_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_datalakeworkspace_DuplicateBaseRecord"></a> datalakeworkspace_DuplicateBaseRecord

**Added by**: Data lake workspaces Solution

See datalakeworkspace Table [datalakeworkspace_DuplicateBaseRecord](datalakeworkspace.md#BKMK_datalakeworkspace_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_datalakeworkspacepermission_DuplicateMatchingRecord"></a> datalakeworkspacepermission_DuplicateMatchingRecord

**Added by**: Data lake workspaces Solution

See datalakeworkspacepermission Table [datalakeworkspacepermission_DuplicateMatchingRecord](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_datalakeworkspacepermission_DuplicateBaseRecord"></a> datalakeworkspacepermission_DuplicateBaseRecord

**Added by**: Data lake workspaces Solution

See datalakeworkspacepermission Table [datalakeworkspacepermission_DuplicateBaseRecord](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_dataflow_DuplicateMatchingRecord"></a> msdyn_dataflow_DuplicateMatchingRecord

**Added by**: Dataflow Solution Solution

See msdyn_dataflow Table [msdyn_dataflow_DuplicateMatchingRecord](msdyn_dataflow.md#BKMK_msdyn_dataflow_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_dataflow_DuplicateBaseRecord"></a> msdyn_dataflow_DuplicateBaseRecord

**Added by**: Dataflow Solution Solution

See msdyn_dataflow Table [msdyn_dataflow_DuplicateBaseRecord](msdyn_dataflow.md#BKMK_msdyn_dataflow_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_serviceplan_DuplicateMatchingRecord"></a> serviceplan_DuplicateMatchingRecord

**Added by**: License Enforcement Solution

See serviceplan Table [serviceplan_DuplicateMatchingRecord](serviceplan.md#BKMK_serviceplan_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_serviceplan_DuplicateBaseRecord"></a> serviceplan_DuplicateBaseRecord

**Added by**: License Enforcement Solution

See serviceplan Table [serviceplan_DuplicateBaseRecord](serviceplan.md#BKMK_serviceplan_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_applicationuser_DuplicateMatchingRecord"></a> applicationuser_DuplicateMatchingRecord

**Added by**: ApplicationUserSolution Solution

See applicationuser Table [applicationuser_DuplicateMatchingRecord](applicationuser.md#BKMK_applicationuser_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_applicationuser_DuplicateBaseRecord"></a> applicationuser_DuplicateBaseRecord

**Added by**: ApplicationUserSolution Solution

See applicationuser Table [applicationuser_DuplicateBaseRecord](applicationuser.md#BKMK_applicationuser_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_connector_DuplicateMatchingRecord"></a> connector_DuplicateMatchingRecord

**Added by**: Power Connector Solution Solution

See connector Table [connector_DuplicateMatchingRecord](connector.md#BKMK_connector_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_connector_DuplicateBaseRecord"></a> connector_DuplicateBaseRecord

**Added by**: Power Connector Solution Solution

See connector Table [connector_DuplicateBaseRecord](connector.md#BKMK_connector_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_environmentvariabledefinition_DuplicateMatchingRecord"></a> environmentvariabledefinition_DuplicateMatchingRecord

**Added by**: Environment Variables Solution

See environmentvariabledefinition Table [environmentvariabledefinition_DuplicateMatchingRecord](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_environmentvariabledefinition_DuplicateBaseRecord"></a> environmentvariabledefinition_DuplicateBaseRecord

**Added by**: Environment Variables Solution

See environmentvariabledefinition Table [environmentvariabledefinition_DuplicateBaseRecord](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_environmentvariablevalue_DuplicateMatchingRecord"></a> environmentvariablevalue_DuplicateMatchingRecord

**Added by**: Environment Variables Solution

See environmentvariablevalue Table [environmentvariablevalue_DuplicateMatchingRecord](environmentvariablevalue.md#BKMK_environmentvariablevalue_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_environmentvariablevalue_DuplicateBaseRecord"></a> environmentvariablevalue_DuplicateBaseRecord

**Added by**: Environment Variables Solution

See environmentvariablevalue Table [environmentvariablevalue_DuplicateBaseRecord](environmentvariablevalue.md#BKMK_environmentvariablevalue_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_flowmachinegroup_DuplicateMatchingRecord"></a> flowmachinegroup_DuplicateMatchingRecord

**Added by**: Power Automate Extensions core package Solution

See flowmachinegroup Table [flowmachinegroup_DuplicateMatchingRecord](flowmachinegroup.md#BKMK_flowmachinegroup_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_flowmachinegroup_DuplicateBaseRecord"></a> flowmachinegroup_DuplicateBaseRecord

**Added by**: Power Automate Extensions core package Solution

See flowmachinegroup Table [flowmachinegroup_DuplicateBaseRecord](flowmachinegroup.md#BKMK_flowmachinegroup_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_conversationtranscript_DuplicateMatchingRecord"></a> conversationtranscript_DuplicateMatchingRecord

**Added by**: Power Virtual Agents Common Solution

See conversationtranscript Table [conversationtranscript_DuplicateMatchingRecord](conversationtranscript.md#BKMK_conversationtranscript_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_conversationtranscript_DuplicateBaseRecord"></a> conversationtranscript_DuplicateBaseRecord

**Added by**: Power Virtual Agents Common Solution

See conversationtranscript Table [conversationtranscript_DuplicateBaseRecord](conversationtranscript.md#BKMK_conversationtranscript_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_activityfileattachment_DuplicateMatchingRecord"></a> activityfileattachment_DuplicateMatchingRecord

**Added by**: Activities Patch Solution

See activityfileattachment Table [activityfileattachment_DuplicateMatchingRecord](activityfileattachment.md#BKMK_activityfileattachment_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_activityfileattachment_DuplicateBaseRecord"></a> activityfileattachment_DuplicateBaseRecord

**Added by**: Activities Patch Solution

See activityfileattachment Table [activityfileattachment_DuplicateBaseRecord](activityfileattachment.md#BKMK_activityfileattachment_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_serviceconfiguration_DuplicateMatchingRecord"></a> msdyn_serviceconfiguration_DuplicateMatchingRecord

**Added by**: Service Level Agreement (SLA) Extension Solution

See msdyn_serviceconfiguration Table [msdyn_serviceconfiguration_DuplicateMatchingRecord](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_serviceconfiguration_DuplicateBaseRecord"></a> msdyn_serviceconfiguration_DuplicateBaseRecord

**Added by**: Service Level Agreement (SLA) Extension Solution

See msdyn_serviceconfiguration Table [msdyn_serviceconfiguration_DuplicateBaseRecord](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_slakpi_DuplicateMatchingRecord"></a> msdyn_slakpi_DuplicateMatchingRecord

**Added by**: Service Level Agreement (SLA) Extension Solution

See msdyn_slakpi Table [msdyn_slakpi_DuplicateMatchingRecord](msdyn_slakpi.md#BKMK_msdyn_slakpi_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_slakpi_DuplicateBaseRecord"></a> msdyn_slakpi_DuplicateBaseRecord

**Added by**: Service Level Agreement (SLA) Extension Solution

See msdyn_slakpi Table [msdyn_slakpi_DuplicateBaseRecord](msdyn_slakpi.md#BKMK_msdyn_slakpi_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_federatedarticle_DuplicateMatchingRecord"></a> msdyn_federatedarticle_DuplicateMatchingRecord

**Added by**: Knowledge Management Online Features Solution

See msdyn_federatedarticle Table [msdyn_federatedarticle_DuplicateMatchingRecord](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_federatedarticle_DuplicateBaseRecord"></a> msdyn_federatedarticle_DuplicateBaseRecord

**Added by**: Knowledge Management Online Features Solution

See msdyn_federatedarticle Table [msdyn_federatedarticle_DuplicateBaseRecord](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_federatedarticleincident_DuplicateMatchingRecord"></a> msdyn_federatedarticleincident_DuplicateMatchingRecord

**Added by**: Knowledge Management Online Features Solution

See msdyn_federatedarticleincident Table [msdyn_federatedarticleincident_DuplicateMatchingRecord](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_federatedarticleincident_DuplicateBaseRecord"></a> msdyn_federatedarticleincident_DuplicateBaseRecord

**Added by**: Knowledge Management Online Features Solution

See msdyn_federatedarticleincident Table [msdyn_federatedarticleincident_DuplicateBaseRecord](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord"></a> msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord

**Added by**: Knowledge Management Online Features Solution

See msdyn_kmfederatedsearchconfig Table [msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_kmfederatedsearchconfig_DuplicateBaseRecord"></a> msdyn_kmfederatedsearchconfig_DuplicateBaseRecord

**Added by**: Knowledge Management Online Features Solution

See msdyn_kmfederatedsearchconfig Table [msdyn_kmfederatedsearchconfig_DuplicateBaseRecord](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgearticleimage_DuplicateMatchingRecord"></a> msdyn_knowledgearticleimage_DuplicateMatchingRecord

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgearticleimage Table [msdyn_knowledgearticleimage_DuplicateMatchingRecord](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgearticleimage_DuplicateBaseRecord"></a> msdyn_knowledgearticleimage_DuplicateBaseRecord

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgearticleimage Table [msdyn_knowledgearticleimage_DuplicateBaseRecord](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord"></a> msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgeinteractioninsight Table [msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgeinteractioninsight_DuplicateBaseRecord"></a> msdyn_knowledgeinteractioninsight_DuplicateBaseRecord

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgeinteractioninsight Table [msdyn_knowledgeinteractioninsight_DuplicateBaseRecord](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgesearchinsight_DuplicateMatchingRecord"></a> msdyn_knowledgesearchinsight_DuplicateMatchingRecord

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgesearchinsight Table [msdyn_knowledgesearchinsight_DuplicateMatchingRecord](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgesearchinsight_DuplicateBaseRecord"></a> msdyn_knowledgesearchinsight_DuplicateBaseRecord

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgesearchinsight Table [msdyn_knowledgesearchinsight_DuplicateBaseRecord](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_kalanguagesetting_DuplicateMatchingRecord"></a> msdyn_kalanguagesetting_DuplicateMatchingRecord

**Added by**: Knowledge Management Features Solution

See msdyn_kalanguagesetting Table [msdyn_kalanguagesetting_DuplicateMatchingRecord](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_kalanguagesetting_DuplicateBaseRecord"></a> msdyn_kalanguagesetting_DuplicateBaseRecord

**Added by**: Knowledge Management Features Solution

See msdyn_kalanguagesetting Table [msdyn_kalanguagesetting_DuplicateBaseRecord](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgearticletemplate_DuplicateMatchingRecord"></a> msdyn_knowledgearticletemplate_DuplicateMatchingRecord

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgearticletemplate Table [msdyn_knowledgearticletemplate_DuplicateMatchingRecord](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgearticletemplate_DuplicateBaseRecord"></a> msdyn_knowledgearticletemplate_DuplicateBaseRecord

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgearticletemplate Table [msdyn_knowledgearticletemplate_DuplicateBaseRecord](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgepersonalfilter_DuplicateMatchingRecord"></a> msdyn_knowledgepersonalfilter_DuplicateMatchingRecord

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgepersonalfilter Table [msdyn_knowledgepersonalfilter_DuplicateMatchingRecord](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgepersonalfilter_DuplicateBaseRecord"></a> msdyn_knowledgepersonalfilter_DuplicateBaseRecord

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgepersonalfilter Table [msdyn_knowledgepersonalfilter_DuplicateBaseRecord](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgesearchfilter_DuplicateMatchingRecord"></a> msdyn_knowledgesearchfilter_DuplicateMatchingRecord

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgesearchfilter Table [msdyn_knowledgesearchfilter_DuplicateMatchingRecord](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgesearchfilter_DuplicateBaseRecord"></a> msdyn_knowledgesearchfilter_DuplicateBaseRecord

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgesearchfilter Table [msdyn_knowledgesearchfilter_DuplicateBaseRecord](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_keyvaultreference_DuplicateMatchingRecord"></a> keyvaultreference_DuplicateMatchingRecord

**Added by**: ManagedIdentityExtensions Solution

See keyvaultreference Table [keyvaultreference_DuplicateMatchingRecord](keyvaultreference.md#BKMK_keyvaultreference_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_keyvaultreference_DuplicateBaseRecord"></a> keyvaultreference_DuplicateBaseRecord

**Added by**: ManagedIdentityExtensions Solution

See keyvaultreference Table [keyvaultreference_DuplicateBaseRecord](keyvaultreference.md#BKMK_keyvaultreference_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_managedidentity_DuplicateMatchingRecord"></a> managedidentity_DuplicateMatchingRecord

**Added by**: ManagedIdentityExtensions Solution

See managedidentity Table [managedidentity_DuplicateMatchingRecord](managedidentity.md#BKMK_managedidentity_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_managedidentity_DuplicateBaseRecord"></a> managedidentity_DuplicateBaseRecord

**Added by**: ManagedIdentityExtensions Solution

See managedidentity Table [managedidentity_DuplicateBaseRecord](managedidentity.md#BKMK_managedidentity_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_catalogassignment_DuplicateMatchingRecord"></a> catalogassignment_DuplicateMatchingRecord

**Added by**: CatalogFramework Solution

See catalogassignment Table [catalogassignment_DuplicateMatchingRecord](catalogassignment.md#BKMK_catalogassignment_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_catalogassignment_DuplicateBaseRecord"></a> catalogassignment_DuplicateBaseRecord

**Added by**: CatalogFramework Solution

See catalogassignment Table [catalogassignment_DuplicateBaseRecord](catalogassignment.md#BKMK_catalogassignment_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_organizationdatasyncsubscription_DuplicateMatchingRecord"></a> organizationdatasyncsubscription_DuplicateMatchingRecord

**Added by**: OrganizationDataSyncSolution Solution

See organizationdatasyncsubscription Table [organizationdatasyncsubscription_DuplicateMatchingRecord](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_organizationdatasyncsubscription_DuplicateBaseRecord"></a> organizationdatasyncsubscription_DuplicateBaseRecord

**Added by**: OrganizationDataSyncSolution Solution

See organizationdatasyncsubscription Table [organizationdatasyncsubscription_DuplicateBaseRecord](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_organizationdatasyncsubscriptionentity_DuplicateMatchingRecord"></a> organizationdatasyncsubscriptionentity_DuplicateMatchingRecord

**Added by**: OrganizationDataSyncSolution Solution

See organizationdatasyncsubscriptionentity Table [organizationdatasyncsubscriptionentity_DuplicateMatchingRecord](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_organizationdatasyncsubscriptionentity_DuplicateBaseRecord"></a> organizationdatasyncsubscriptionentity_DuplicateBaseRecord

**Added by**: OrganizationDataSyncSolution Solution

See organizationdatasyncsubscriptionentity Table [organizationdatasyncsubscriptionentity_DuplicateBaseRecord](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_appnotification_DuplicateMatchingRecord"></a> appnotification_DuplicateMatchingRecord

**Added by**: AppNotifications Solution

See appnotification Table [appnotification_DuplicateMatchingRecord](appnotification.md#BKMK_appnotification_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_appnotification_DuplicateBaseRecord"></a> appnotification_DuplicateBaseRecord

**Added by**: AppNotifications Solution

See appnotification Table [appnotification_DuplicateBaseRecord](appnotification.md#BKMK_appnotification_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdataset_DuplicateMatchingRecord"></a> msdyn_aibdataset_DuplicateMatchingRecord

**Added by**: AI Solution default templates Solution

See msdyn_aibdataset Table [msdyn_aibdataset_DuplicateMatchingRecord](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdataset_DuplicateBaseRecord"></a> msdyn_aibdataset_DuplicateBaseRecord

**Added by**: AI Solution default templates Solution

See msdyn_aibdataset Table [msdyn_aibdataset_DuplicateBaseRecord](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdatasetfile_DuplicateMatchingRecord"></a> msdyn_aibdatasetfile_DuplicateMatchingRecord

**Added by**: AI Solution default templates Solution

See msdyn_aibdatasetfile Table [msdyn_aibdatasetfile_DuplicateMatchingRecord](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdatasetfile_DuplicateBaseRecord"></a> msdyn_aibdatasetfile_DuplicateBaseRecord

**Added by**: AI Solution default templates Solution

See msdyn_aibdatasetfile Table [msdyn_aibdatasetfile_DuplicateBaseRecord](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdatasetrecord_DuplicateMatchingRecord"></a> msdyn_aibdatasetrecord_DuplicateMatchingRecord

**Added by**: AI Solution default templates Solution

See msdyn_aibdatasetrecord Table [msdyn_aibdatasetrecord_DuplicateMatchingRecord](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdatasetrecord_DuplicateBaseRecord"></a> msdyn_aibdatasetrecord_DuplicateBaseRecord

**Added by**: AI Solution default templates Solution

See msdyn_aibdatasetrecord Table [msdyn_aibdatasetrecord_DuplicateBaseRecord](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdatasetscontainer_DuplicateMatchingRecord"></a> msdyn_aibdatasetscontainer_DuplicateMatchingRecord

**Added by**: AI Solution default templates Solution

See msdyn_aibdatasetscontainer Table [msdyn_aibdatasetscontainer_DuplicateMatchingRecord](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdatasetscontainer_DuplicateBaseRecord"></a> msdyn_aibdatasetscontainer_DuplicateBaseRecord

**Added by**: AI Solution default templates Solution

See msdyn_aibdatasetscontainer Table [msdyn_aibdatasetscontainer_DuplicateBaseRecord](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aibfile_DuplicateMatchingRecord"></a> msdyn_aibfile_DuplicateMatchingRecord

**Added by**: AI Solution default templates Solution

See msdyn_aibfile Table [msdyn_aibfile_DuplicateMatchingRecord](msdyn_aibfile.md#BKMK_msdyn_aibfile_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aibfile_DuplicateBaseRecord"></a> msdyn_aibfile_DuplicateBaseRecord

**Added by**: AI Solution default templates Solution

See msdyn_aibfile Table [msdyn_aibfile_DuplicateBaseRecord](msdyn_aibfile.md#BKMK_msdyn_aibfile_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aibfileattacheddata_DuplicateMatchingRecord"></a> msdyn_aibfileattacheddata_DuplicateMatchingRecord

**Added by**: AI Solution default templates Solution

See msdyn_aibfileattacheddata Table [msdyn_aibfileattacheddata_DuplicateMatchingRecord](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aibfileattacheddata_DuplicateBaseRecord"></a> msdyn_aibfileattacheddata_DuplicateBaseRecord

**Added by**: AI Solution default templates Solution

See msdyn_aibfileattacheddata Table [msdyn_aibfileattacheddata_DuplicateBaseRecord](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodimage_DuplicateMatchingRecord"></a> msdyn_aiodimage_DuplicateMatchingRecord

**Added by**: AI Solution default templates Solution

See msdyn_aiodimage Table [msdyn_aiodimage_DuplicateMatchingRecord](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodimage_DuplicateBaseRecord"></a> msdyn_aiodimage_DuplicateBaseRecord

**Added by**: AI Solution default templates Solution

See msdyn_aiodimage Table [msdyn_aiodimage_DuplicateBaseRecord](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodlabel_DuplicateMatchingRecord"></a> msdyn_aiodlabel_DuplicateMatchingRecord

**Added by**: AI Solution default templates Solution

See msdyn_aiodlabel Table [msdyn_aiodlabel_DuplicateMatchingRecord](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodlabel_DuplicateBaseRecord"></a> msdyn_aiodlabel_DuplicateBaseRecord

**Added by**: AI Solution default templates Solution

See msdyn_aiodlabel Table [msdyn_aiodlabel_DuplicateBaseRecord](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord"></a> msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord

**Added by**: AI Solution default templates Solution

See msdyn_aiodtrainingboundingbox Table [msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodtrainingboundingbox_DuplicateBaseRecord"></a> msdyn_aiodtrainingboundingbox_DuplicateBaseRecord

**Added by**: AI Solution default templates Solution

See msdyn_aiodtrainingboundingbox Table [msdyn_aiodtrainingboundingbox_DuplicateBaseRecord](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodtrainingimage_DuplicateMatchingRecord"></a> msdyn_aiodtrainingimage_DuplicateMatchingRecord

**Added by**: AI Solution default templates Solution

See msdyn_aiodtrainingimage Table [msdyn_aiodtrainingimage_DuplicateMatchingRecord](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodtrainingimage_DuplicateBaseRecord"></a> msdyn_aiodtrainingimage_DuplicateBaseRecord

**Added by**: AI Solution default templates Solution

See msdyn_aiodtrainingimage Table [msdyn_aiodtrainingimage_DuplicateBaseRecord](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_pminferredtask_DuplicateMatchingRecord"></a> msdyn_pminferredtask_DuplicateMatchingRecord

**Added by**: Process Mining Solution

See msdyn_pminferredtask Table [msdyn_pminferredtask_DuplicateMatchingRecord](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_pminferredtask_DuplicateBaseRecord"></a> msdyn_pminferredtask_DuplicateBaseRecord

**Added by**: Process Mining Solution

See msdyn_pminferredtask Table [msdyn_pminferredtask_DuplicateBaseRecord](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_pmrecording_DuplicateMatchingRecord"></a> msdyn_pmrecording_DuplicateMatchingRecord

**Added by**: Process Mining Solution

See msdyn_pmrecording Table [msdyn_pmrecording_DuplicateMatchingRecord](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_pmrecording_DuplicateBaseRecord"></a> msdyn_pmrecording_DuplicateBaseRecord

**Added by**: Process Mining Solution

See msdyn_pmrecording Table [msdyn_pmrecording_DuplicateBaseRecord](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_analysiscomponent_DuplicateMatchingRecord"></a> msdyn_analysiscomponent_DuplicateMatchingRecord

**Added by**: Power Apps Checker Solution

See msdyn_analysiscomponent Table [msdyn_analysiscomponent_DuplicateMatchingRecord](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_analysiscomponent_DuplicateBaseRecord"></a> msdyn_analysiscomponent_DuplicateBaseRecord

**Added by**: Power Apps Checker Solution

See msdyn_analysiscomponent Table [msdyn_analysiscomponent_DuplicateBaseRecord](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisjob_DuplicateMatchingRecord"></a> msdyn_analysisjob_DuplicateMatchingRecord

**Added by**: Power Apps Checker Solution

See msdyn_analysisjob Table [msdyn_analysisjob_DuplicateMatchingRecord](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisjob_DuplicateBaseRecord"></a> msdyn_analysisjob_DuplicateBaseRecord

**Added by**: Power Apps Checker Solution

See msdyn_analysisjob Table [msdyn_analysisjob_DuplicateBaseRecord](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisresult_DuplicateMatchingRecord"></a> msdyn_analysisresult_DuplicateMatchingRecord

**Added by**: Power Apps Checker Solution

See msdyn_analysisresult Table [msdyn_analysisresult_DuplicateMatchingRecord](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisresult_DuplicateBaseRecord"></a> msdyn_analysisresult_DuplicateBaseRecord

**Added by**: Power Apps Checker Solution

See msdyn_analysisresult Table [msdyn_analysisresult_DuplicateBaseRecord](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisresultdetail_DuplicateMatchingRecord"></a> msdyn_analysisresultdetail_DuplicateMatchingRecord

**Added by**: Power Apps Checker Solution

See msdyn_analysisresultdetail Table [msdyn_analysisresultdetail_DuplicateMatchingRecord](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisresultdetail_DuplicateBaseRecord"></a> msdyn_analysisresultdetail_DuplicateBaseRecord

**Added by**: Power Apps Checker Solution

See msdyn_analysisresultdetail Table [msdyn_analysisresultdetail_DuplicateBaseRecord](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthrule_DuplicateMatchingRecord"></a> msdyn_solutionhealthrule_DuplicateMatchingRecord

**Added by**: Power Apps Checker Solution

See msdyn_solutionhealthrule Table [msdyn_solutionhealthrule_DuplicateMatchingRecord](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthrule_DuplicateBaseRecord"></a> msdyn_solutionhealthrule_DuplicateBaseRecord

**Added by**: Power Apps Checker Solution

See msdyn_solutionhealthrule Table [msdyn_solutionhealthrule_DuplicateBaseRecord](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthruleargument_DuplicateMatchingRecord"></a> msdyn_solutionhealthruleargument_DuplicateMatchingRecord

**Added by**: Power Apps Checker Solution

See msdyn_solutionhealthruleargument Table [msdyn_solutionhealthruleargument_DuplicateMatchingRecord](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthruleargument_DuplicateBaseRecord"></a> msdyn_solutionhealthruleargument_DuplicateBaseRecord

**Added by**: Power Apps Checker Solution

See msdyn_solutionhealthruleargument Table [msdyn_solutionhealthruleargument_DuplicateBaseRecord](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_DuplicateBaseRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthruleset_DuplicateMatchingRecord"></a> msdyn_solutionhealthruleset_DuplicateMatchingRecord

**Added by**: Power Apps Checker Solution

See msdyn_solutionhealthruleset Table [msdyn_solutionhealthruleset_DuplicateMatchingRecord](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_DuplicateMatchingRecord) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthruleset_DuplicateBaseRecord"></a> msdyn_solutionhealthruleset_DuplicateBaseRecord

**Added by**: Power Apps Checker Solution

See msdyn_solutionhealthruleset Table [msdyn_solutionhealthruleset_DuplicateBaseRecord](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_DuplicateBaseRecord) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.duplicaterecord?text=duplicaterecord EntityType" />