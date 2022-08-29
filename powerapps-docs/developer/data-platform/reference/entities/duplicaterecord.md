---
title: "DuplicateRecord table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the DuplicateRecord table/entity."
ms.date: 06/30/2022
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "margoc"
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
|Targets|account,activityfileattachment,applicationuser,appointment,canvasappextendedmetadata,cascadegrantrevokeaccessrecordstracker,cascadegrantrevokeaccessversiontracker,catalogassignment,channelaccessprofile,chat,connector,contact,conversationtranscript,datalakefolder,datalakefolderpermission,datalakeworkspace,datalakeworkspacepermission,dataprocessingconfiguration,email,emailserverprofile,environmentvariabledefinition,environmentvariablevalue,exportsolutionupload,fax,featurecontrolsetting,feedback,flowmachinegroup,flowmachineimage,flowmachineimageversion,goal,goalrollupquery,kbarticle,keyvaultreference,knowledgearticle,knowledgebaserecord,letter,managedidentity,msdyn_aibdataset,msdyn_aibdatasetfile,msdyn_aibdatasetrecord,msdyn_aibdatasetscontainer,msdyn_aibfeedbackloop,msdyn_aibfile,msdyn_aibfileattacheddata,msdyn_aiodimage,msdyn_aiodlabel,msdyn_aiodtrainingboundingbox,msdyn_aiodtrainingimage,msdyn_analysiscomponent,msdyn_analysisjob,msdyn_analysisresult,msdyn_analysisresultdetail,msdyn_customcontrolextendedsettings,msdyn_dataflow,msdyn_dataflowrefreshhistory,msdyn_entityrefreshhistory,msdyn_federatedarticle,msdyn_federatedarticleincident,msdyn_kalanguagesetting,msdyn_kbattachment,msdyn_kmfederatedsearchconfig,msdyn_knowledgearticleimage,msdyn_knowledgearticletemplate,msdyn_knowledgeinteractioninsight,msdyn_knowledgemanagementsetting,msdyn_knowledgepersonalfilter,msdyn_knowledgesearchfilter,msdyn_knowledgesearchinsight,msdyn_pmanalysishistory,msdyn_pminferredtask,msdyn_pmrecording,msdyn_pmtemplate,msdyn_serviceconfiguration,msdyn_slakpi,msdyn_solutionhealthrule,msdyn_solutionhealthruleargument,msdyn_solutionhealthruleset,organizationdatasyncstate,organizationdatasyncsubscription,organizationdatasyncsubscriptionentity,package,phonecall,privilegesremovalsetting,publisher,queue,recurringappointmentmaster,revokeinheritedaccessrecordstracker,serviceplan,serviceplanmapping,sharedlinksetting,sharepointdocumentlocation,sharepointsite,socialactivity,socialprofile,solutioncomponentattributeconfiguration,solutioncomponentbatchconfiguration,solutioncomponentconfiguration,solutioncomponentrelationshipconfiguration,stagesolutionupload,synapsedatabase,synapselinkexternaltablestate,synapselinkprofile,synapselinkprofileentity,synapselinkprofileentitystate,synapselinkschedule,systemuser,task,team,transactioncurrency,userrating|
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
|Targets|account,activityfileattachment,applicationuser,appointment,canvasappextendedmetadata,cascadegrantrevokeaccessrecordstracker,cascadegrantrevokeaccessversiontracker,catalogassignment,channelaccessprofile,chat,connector,contact,conversationtranscript,datalakefolder,datalakefolderpermission,datalakeworkspace,datalakeworkspacepermission,dataprocessingconfiguration,email,emailserverprofile,environmentvariabledefinition,environmentvariablevalue,exportsolutionupload,fax,featurecontrolsetting,feedback,flowmachinegroup,flowmachineimage,flowmachineimageversion,goal,goalrollupquery,kbarticle,keyvaultreference,knowledgearticle,knowledgebaserecord,letter,managedidentity,msdyn_aibdataset,msdyn_aibdatasetfile,msdyn_aibdatasetrecord,msdyn_aibdatasetscontainer,msdyn_aibfeedbackloop,msdyn_aibfile,msdyn_aibfileattacheddata,msdyn_aiodimage,msdyn_aiodlabel,msdyn_aiodtrainingboundingbox,msdyn_aiodtrainingimage,msdyn_analysiscomponent,msdyn_analysisjob,msdyn_analysisresult,msdyn_analysisresultdetail,msdyn_customcontrolextendedsettings,msdyn_dataflow,msdyn_dataflowrefreshhistory,msdyn_entityrefreshhistory,msdyn_federatedarticle,msdyn_federatedarticleincident,msdyn_kalanguagesetting,msdyn_kbattachment,msdyn_kmfederatedsearchconfig,msdyn_knowledgearticleimage,msdyn_knowledgearticletemplate,msdyn_knowledgeinteractioninsight,msdyn_knowledgemanagementsetting,msdyn_knowledgepersonalfilter,msdyn_knowledgesearchfilter,msdyn_knowledgesearchinsight,msdyn_pmanalysishistory,msdyn_pminferredtask,msdyn_pmrecording,msdyn_pmtemplate,msdyn_serviceconfiguration,msdyn_slakpi,msdyn_solutionhealthrule,msdyn_solutionhealthruleargument,msdyn_solutionhealthruleset,organizationdatasyncstate,organizationdatasyncsubscription,organizationdatasyncsubscriptionentity,package,phonecall,privilegesremovalsetting,publisher,queue,recurringappointmentmaster,revokeinheritedaccessrecordstracker,serviceplan,serviceplanmapping,sharedlinksetting,sharepointdocumentlocation,sharepointsite,socialactivity,socialprofile,solutioncomponentattributeconfiguration,solutioncomponentbatchconfiguration,solutioncomponentconfiguration,solutioncomponentrelationshipconfiguration,stagesolutionupload,synapsedatabase,synapselinkexternaltablestate,synapselinkprofile,synapselinkprofileentity,synapselinkprofileentitystate,synapselinkschedule,systemuser,task,team,transactioncurrency,userrating|
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
- [solutioncomponentbatchconfiguration_DuplicateMatchingRecord](#BKMK_solutioncomponentbatchconfiguration_DuplicateMatchingRecord)
- [solutioncomponentbatchconfiguration_DuplicateBaseRecord](#BKMK_solutioncomponentbatchconfiguration_DuplicateBaseRecord)
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
- [featurecontrolsetting_DuplicateMatchingRecord](#BKMK_featurecontrolsetting_DuplicateMatchingRecord)
- [featurecontrolsetting_DuplicateBaseRecord](#BKMK_featurecontrolsetting_DuplicateBaseRecord)
- [catalogassignment_DuplicateMatchingRecord](#BKMK_catalogassignment_DuplicateMatchingRecord)
- [catalogassignment_DuplicateBaseRecord](#BKMK_catalogassignment_DuplicateBaseRecord)
- [datalakefolder_DuplicateMatchingRecord](#BKMK_datalakefolder_DuplicateMatchingRecord)
- [datalakefolder_DuplicateBaseRecord](#BKMK_datalakefolder_DuplicateBaseRecord)
- [datalakefolderpermission_DuplicateMatchingRecord](#BKMK_datalakefolderpermission_DuplicateMatchingRecord)
- [datalakefolderpermission_DuplicateBaseRecord](#BKMK_datalakefolderpermission_DuplicateBaseRecord)
- [datalakeworkspace_DuplicateMatchingRecord](#BKMK_datalakeworkspace_DuplicateMatchingRecord)
- [datalakeworkspace_DuplicateBaseRecord](#BKMK_datalakeworkspace_DuplicateBaseRecord)
- [datalakeworkspacepermission_DuplicateMatchingRecord](#BKMK_datalakeworkspacepermission_DuplicateMatchingRecord)
- [datalakeworkspacepermission_DuplicateBaseRecord](#BKMK_datalakeworkspacepermission_DuplicateBaseRecord)
- [dataprocessingconfiguration_DuplicateMatchingRecord](#BKMK_dataprocessingconfiguration_DuplicateMatchingRecord)
- [dataprocessingconfiguration_DuplicateBaseRecord](#BKMK_dataprocessingconfiguration_DuplicateBaseRecord)
- [synapsedatabase_DuplicateMatchingRecord](#BKMK_synapsedatabase_DuplicateMatchingRecord)
- [synapsedatabase_DuplicateBaseRecord](#BKMK_synapsedatabase_DuplicateBaseRecord)
- [synapselinkexternaltablestate_DuplicateMatchingRecord](#BKMK_synapselinkexternaltablestate_DuplicateMatchingRecord)
- [synapselinkexternaltablestate_DuplicateBaseRecord](#BKMK_synapselinkexternaltablestate_DuplicateBaseRecord)
- [synapselinkprofile_DuplicateMatchingRecord](#BKMK_synapselinkprofile_DuplicateMatchingRecord)
- [synapselinkprofile_DuplicateBaseRecord](#BKMK_synapselinkprofile_DuplicateBaseRecord)
- [synapselinkprofileentity_DuplicateMatchingRecord](#BKMK_synapselinkprofileentity_DuplicateMatchingRecord)
- [synapselinkprofileentity_DuplicateBaseRecord](#BKMK_synapselinkprofileentity_DuplicateBaseRecord)
- [synapselinkprofileentitystate_DuplicateMatchingRecord](#BKMK_synapselinkprofileentitystate_DuplicateMatchingRecord)
- [synapselinkprofileentitystate_DuplicateBaseRecord](#BKMK_synapselinkprofileentitystate_DuplicateBaseRecord)
- [synapselinkschedule_DuplicateMatchingRecord](#BKMK_synapselinkschedule_DuplicateMatchingRecord)
- [synapselinkschedule_DuplicateBaseRecord](#BKMK_synapselinkschedule_DuplicateBaseRecord)
- [msdyn_dataflow_DuplicateMatchingRecord](#BKMK_msdyn_dataflow_DuplicateMatchingRecord)
- [msdyn_dataflow_DuplicateBaseRecord](#BKMK_msdyn_dataflow_DuplicateBaseRecord)
- [msdyn_dataflowrefreshhistory_DuplicateMatchingRecord](#BKMK_msdyn_dataflowrefreshhistory_DuplicateMatchingRecord)
- [msdyn_dataflowrefreshhistory_DuplicateBaseRecord](#BKMK_msdyn_dataflowrefreshhistory_DuplicateBaseRecord)
- [msdyn_entityrefreshhistory_DuplicateMatchingRecord](#BKMK_msdyn_entityrefreshhistory_DuplicateMatchingRecord)
- [msdyn_entityrefreshhistory_DuplicateBaseRecord](#BKMK_msdyn_entityrefreshhistory_DuplicateBaseRecord)
- [sharedlinksetting_DuplicateMatchingRecord](#BKMK_sharedlinksetting_DuplicateMatchingRecord)
- [sharedlinksetting_DuplicateBaseRecord](#BKMK_sharedlinksetting_DuplicateBaseRecord)
- [serviceplan_DuplicateMatchingRecord](#BKMK_serviceplan_DuplicateMatchingRecord)
- [serviceplan_DuplicateBaseRecord](#BKMK_serviceplan_DuplicateBaseRecord)
- [serviceplanmapping_DuplicateMatchingRecord](#BKMK_serviceplanmapping_DuplicateMatchingRecord)
- [serviceplanmapping_DuplicateBaseRecord](#BKMK_serviceplanmapping_DuplicateBaseRecord)
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
- [flowmachineimage_DuplicateMatchingRecord](#BKMK_flowmachineimage_DuplicateMatchingRecord)
- [flowmachineimage_DuplicateBaseRecord](#BKMK_flowmachineimage_DuplicateBaseRecord)
- [flowmachineimageversion_DuplicateMatchingRecord](#BKMK_flowmachineimageversion_DuplicateMatchingRecord)
- [flowmachineimageversion_DuplicateBaseRecord](#BKMK_flowmachineimageversion_DuplicateBaseRecord)
- [msdyn_aibfeedbackloop_DuplicateMatchingRecord](#BKMK_msdyn_aibfeedbackloop_DuplicateMatchingRecord)
- [msdyn_aibfeedbackloop_DuplicateBaseRecord](#BKMK_msdyn_aibfeedbackloop_DuplicateBaseRecord)
- [msdyn_aiodimage_DuplicateMatchingRecord](#BKMK_msdyn_aiodimage_DuplicateMatchingRecord)
- [msdyn_aiodimage_DuplicateBaseRecord](#BKMK_msdyn_aiodimage_DuplicateBaseRecord)
- [msdyn_aiodlabel_DuplicateMatchingRecord](#BKMK_msdyn_aiodlabel_DuplicateMatchingRecord)
- [msdyn_aiodlabel_DuplicateBaseRecord](#BKMK_msdyn_aiodlabel_DuplicateBaseRecord)
- [msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord](#BKMK_msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord)
- [msdyn_aiodtrainingboundingbox_DuplicateBaseRecord](#BKMK_msdyn_aiodtrainingboundingbox_DuplicateBaseRecord)
- [msdyn_aiodtrainingimage_DuplicateMatchingRecord](#BKMK_msdyn_aiodtrainingimage_DuplicateMatchingRecord)
- [msdyn_aiodtrainingimage_DuplicateBaseRecord](#BKMK_msdyn_aiodtrainingimage_DuplicateBaseRecord)
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
- [conversationtranscript_DuplicateMatchingRecord](#BKMK_conversationtranscript_DuplicateMatchingRecord)
- [conversationtranscript_DuplicateBaseRecord](#BKMK_conversationtranscript_DuplicateBaseRecord)
- [activityfileattachment_DuplicateMatchingRecord](#BKMK_activityfileattachment_DuplicateMatchingRecord)
- [activityfileattachment_DuplicateBaseRecord](#BKMK_activityfileattachment_DuplicateBaseRecord)
- [chat_DuplicateMatchingRecord](#BKMK_chat_DuplicateMatchingRecord)
- [chat_DuplicateBaseRecord](#BKMK_chat_DuplicateBaseRecord)
- [msdyn_serviceconfiguration_DuplicateMatchingRecord](#BKMK_msdyn_serviceconfiguration_DuplicateMatchingRecord)
- [msdyn_serviceconfiguration_DuplicateBaseRecord](#BKMK_msdyn_serviceconfiguration_DuplicateBaseRecord)
- [msdyn_slakpi_DuplicateMatchingRecord](#BKMK_msdyn_slakpi_DuplicateMatchingRecord)
- [msdyn_slakpi_DuplicateBaseRecord](#BKMK_msdyn_slakpi_DuplicateBaseRecord)
- [msdyn_knowledgemanagementsetting_DuplicateMatchingRecord](#BKMK_msdyn_knowledgemanagementsetting_DuplicateMatchingRecord)
- [msdyn_knowledgemanagementsetting_DuplicateBaseRecord](#BKMK_msdyn_knowledgemanagementsetting_DuplicateBaseRecord)
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
- [msdyn_kbattachment_DuplicateMatchingRecord](#BKMK_msdyn_kbattachment_DuplicateMatchingRecord)
- [msdyn_kbattachment_DuplicateBaseRecord](#BKMK_msdyn_kbattachment_DuplicateBaseRecord)
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
- [organizationdatasyncsubscription_DuplicateMatchingRecord](#BKMK_organizationdatasyncsubscription_DuplicateMatchingRecord)
- [organizationdatasyncsubscription_DuplicateBaseRecord](#BKMK_organizationdatasyncsubscription_DuplicateBaseRecord)
- [organizationdatasyncsubscriptionentity_DuplicateMatchingRecord](#BKMK_organizationdatasyncsubscriptionentity_DuplicateMatchingRecord)
- [organizationdatasyncsubscriptionentity_DuplicateBaseRecord](#BKMK_organizationdatasyncsubscriptionentity_DuplicateBaseRecord)
- [organizationdatasyncstate_DuplicateMatchingRecord](#BKMK_organizationdatasyncstate_DuplicateMatchingRecord)
- [organizationdatasyncstate_DuplicateBaseRecord](#BKMK_organizationdatasyncstate_DuplicateBaseRecord)
- [userrating_DuplicateMatchingRecord](#BKMK_userrating_DuplicateMatchingRecord)
- [userrating_DuplicateBaseRecord](#BKMK_userrating_DuplicateBaseRecord)
- [msdyn_customcontrolextendedsettings_DuplicateMatchingRecord](#BKMK_msdyn_customcontrolextendedsettings_DuplicateMatchingRecord)
- [msdyn_customcontrolextendedsettings_DuplicateBaseRecord](#BKMK_msdyn_customcontrolextendedsettings_DuplicateBaseRecord)
- [msdyn_pmanalysishistory_DuplicateMatchingRecord](#BKMK_msdyn_pmanalysishistory_DuplicateMatchingRecord)
- [msdyn_pmanalysishistory_DuplicateBaseRecord](#BKMK_msdyn_pmanalysishistory_DuplicateBaseRecord)
- [msdyn_pminferredtask_DuplicateMatchingRecord](#BKMK_msdyn_pminferredtask_DuplicateMatchingRecord)
- [msdyn_pminferredtask_DuplicateBaseRecord](#BKMK_msdyn_pminferredtask_DuplicateBaseRecord)
- [msdyn_pmrecording_DuplicateMatchingRecord](#BKMK_msdyn_pmrecording_DuplicateMatchingRecord)
- [msdyn_pmrecording_DuplicateBaseRecord](#BKMK_msdyn_pmrecording_DuplicateBaseRecord)
- [msdyn_pmtemplate_DuplicateMatchingRecord](#BKMK_msdyn_pmtemplate_DuplicateMatchingRecord)
- [msdyn_pmtemplate_DuplicateBaseRecord](#BKMK_msdyn_pmtemplate_DuplicateBaseRecord)
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

See the [knowledgearticle_DuplicateMatchingRecord](knowledgearticle.md#BKMK_knowledgearticle_DuplicateMatchingRecord) one-to-many relationship for the [knowledgearticle](knowledgearticle.md) table/entity.

### <a name="BKMK_knowledgearticle_DuplicateBaseRecord"></a> knowledgearticle_DuplicateBaseRecord

See the [knowledgearticle_DuplicateBaseRecord](knowledgearticle.md#BKMK_knowledgearticle_DuplicateBaseRecord) one-to-many relationship for the [knowledgearticle](knowledgearticle.md) table/entity.

### <a name="BKMK_KnowledgeBaseRecord_DuplicateMatchingRecord"></a> KnowledgeBaseRecord_DuplicateMatchingRecord

See the [KnowledgeBaseRecord_DuplicateMatchingRecord](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_DuplicateMatchingRecord) one-to-many relationship for the [knowledgebaserecord](knowledgebaserecord.md) table/entity.

### <a name="BKMK_KnowledgeBaseRecord_DuplicateBaseRecord"></a> KnowledgeBaseRecord_DuplicateBaseRecord

See the [KnowledgeBaseRecord_DuplicateBaseRecord](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_DuplicateBaseRecord) one-to-many relationship for the [knowledgebaserecord](knowledgebaserecord.md) table/entity.

### <a name="BKMK_Email_DuplicateMatchingRecord"></a> Email_DuplicateMatchingRecord

See the [Email_DuplicateMatchingRecord](email.md#BKMK_Email_DuplicateMatchingRecord) one-to-many relationship for the [email](email.md) table/entity.

### <a name="BKMK_Publisher_DuplicateMatchingRecord"></a> Publisher_DuplicateMatchingRecord

See the [Publisher_DuplicateMatchingRecord](publisher.md#BKMK_Publisher_DuplicateMatchingRecord) one-to-many relationship for the [publisher](publisher.md) table/entity.

### <a name="BKMK_Queue_DuplicateBaseRecord"></a> Queue_DuplicateBaseRecord

See the [Queue_DuplicateBaseRecord](queue.md#BKMK_Queue_DuplicateBaseRecord) one-to-many relationship for the [queue](queue.md) table/entity.

### <a name="BKMK_Letter_DuplicateBaseRecord"></a> Letter_DuplicateBaseRecord

See the [Letter_DuplicateBaseRecord](letter.md#BKMK_Letter_DuplicateBaseRecord) one-to-many relationship for the [letter](letter.md) table/entity.

### <a name="BKMK_Team_DuplicateBaseRecord"></a> Team_DuplicateBaseRecord

See the [Team_DuplicateBaseRecord](team.md#BKMK_Team_DuplicateBaseRecord) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_KbArticle_DuplicateMatchingRecord"></a> KbArticle_DuplicateMatchingRecord

See the [KbArticle_DuplicateMatchingRecord](kbarticle.md#BKMK_KbArticle_DuplicateMatchingRecord) one-to-many relationship for the [kbarticle](kbarticle.md) table/entity.

### <a name="BKMK_Appointment_DuplicateBaseRecord"></a> Appointment_DuplicateBaseRecord

See the [Appointment_DuplicateBaseRecord](appointment.md#BKMK_Appointment_DuplicateBaseRecord) one-to-many relationship for the [appointment](appointment.md) table/entity.

### <a name="BKMK_Account_DuplicateBaseRecord"></a> Account_DuplicateBaseRecord

See the [Account_DuplicateBaseRecord](account.md#BKMK_Account_DuplicateBaseRecord) one-to-many relationship for the [account](account.md) table/entity.

### <a name="BKMK_DuplicateRule_DuplicateBaseRecord"></a> DuplicateRule_DuplicateBaseRecord

See the [DuplicateRule_DuplicateBaseRecord](duplicaterule.md#BKMK_DuplicateRule_DuplicateBaseRecord) one-to-many relationship for the [duplicaterule](duplicaterule.md) table/entity.

### <a name="BKMK_SharePointSite_DuplicateBaseRecord"></a> SharePointSite_DuplicateBaseRecord

See the [SharePointSite_DuplicateBaseRecord](sharepointsite.md#BKMK_SharePointSite_DuplicateBaseRecord) one-to-many relationship for the [sharepointsite](sharepointsite.md) table/entity.

### <a name="BKMK_KbArticle_DuplicateBaseRecord"></a> KbArticle_DuplicateBaseRecord

See the [KbArticle_DuplicateBaseRecord](kbarticle.md#BKMK_KbArticle_DuplicateBaseRecord) one-to-many relationship for the [kbarticle](kbarticle.md) table/entity.

### <a name="BKMK_Task_DuplicateMatchingRecord"></a> Task_DuplicateMatchingRecord

See the [Task_DuplicateMatchingRecord](task.md#BKMK_Task_DuplicateMatchingRecord) one-to-many relationship for the [task](task.md) table/entity.

### <a name="BKMK_SocialProfile_DuplicateMatchingRecord"></a> SocialProfile_DuplicateMatchingRecord

See the [SocialProfile_DuplicateMatchingRecord](socialprofile.md#BKMK_SocialProfile_DuplicateMatchingRecord) one-to-many relationship for the [socialprofile](socialprofile.md) table/entity.

### <a name="BKMK_PhoneCall_DuplicateBaseRecord"></a> PhoneCall_DuplicateBaseRecord

See the [PhoneCall_DuplicateBaseRecord](phonecall.md#BKMK_PhoneCall_DuplicateBaseRecord) one-to-many relationship for the [phonecall](phonecall.md) table/entity.

### <a name="BKMK_TransactionCurrency_DuplicateMatchingRecord"></a> TransactionCurrency_DuplicateMatchingRecord

See the [TransactionCurrency_DuplicateMatchingRecord](transactioncurrency.md#BKMK_TransactionCurrency_DuplicateMatchingRecord) one-to-many relationship for the [transactioncurrency](transactioncurrency.md) table/entity.

### <a name="BKMK_Goal_DuplicateMatchingRecord"></a> Goal_DuplicateMatchingRecord

See the [Goal_DuplicateMatchingRecord](goal.md#BKMK_Goal_DuplicateMatchingRecord) one-to-many relationship for the [goal](goal.md) table/entity.

### <a name="BKMK_SharePointSite_DuplicateMatchingRecord"></a> SharePointSite_DuplicateMatchingRecord

See the [SharePointSite_DuplicateMatchingRecord](sharepointsite.md#BKMK_SharePointSite_DuplicateMatchingRecord) one-to-many relationship for the [sharepointsite](sharepointsite.md) table/entity.

### <a name="BKMK_emailserverprofile_duplicatebaserecord"></a> emailserverprofile_duplicatebaserecord

See the [emailserverprofile_duplicatebaserecord](emailserverprofile.md#BKMK_emailserverprofile_duplicatebaserecord) one-to-many relationship for the [emailserverprofile](emailserverprofile.md) table/entity.

### <a name="BKMK_Publisher_DuplicateBaseRecord"></a> Publisher_DuplicateBaseRecord

See the [Publisher_DuplicateBaseRecord](publisher.md#BKMK_Publisher_DuplicateBaseRecord) one-to-many relationship for the [publisher](publisher.md) table/entity.

### <a name="BKMK_SystemUser_DuplicateBaseRecord"></a> SystemUser_DuplicateBaseRecord

See the [SystemUser_DuplicateBaseRecord](systemuser.md#BKMK_SystemUser_DuplicateBaseRecord) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_SocialActivity_DuplicateBaseRecord"></a> SocialActivity_DuplicateBaseRecord

See the [SocialActivity_DuplicateBaseRecord](socialactivity.md#BKMK_SocialActivity_DuplicateBaseRecord) one-to-many relationship for the [socialactivity](socialactivity.md) table/entity.

### <a name="BKMK_Contact_DuplicateMatchingRecord"></a> Contact_DuplicateMatchingRecord

See the [Contact_DuplicateMatchingRecord](contact.md#BKMK_Contact_DuplicateMatchingRecord) one-to-many relationship for the [contact](contact.md) table/entity.

### <a name="BKMK_GoalRollupQuery_DuplicateMatchingRecord"></a> GoalRollupQuery_DuplicateMatchingRecord

See the [GoalRollupQuery_DuplicateMatchingRecord](goalrollupquery.md#BKMK_GoalRollupQuery_DuplicateMatchingRecord) one-to-many relationship for the [goalrollupquery](goalrollupquery.md) table/entity.

### <a name="BKMK_Contact_DuplicateBaseRecord"></a> Contact_DuplicateBaseRecord

See the [Contact_DuplicateBaseRecord](contact.md#BKMK_Contact_DuplicateBaseRecord) one-to-many relationship for the [contact](contact.md) table/entity.

### <a name="BKMK_TransactionCurrency_DuplicateBaseRecord"></a> TransactionCurrency_DuplicateBaseRecord

See the [TransactionCurrency_DuplicateBaseRecord](transactioncurrency.md#BKMK_TransactionCurrency_DuplicateBaseRecord) one-to-many relationship for the [transactioncurrency](transactioncurrency.md) table/entity.

### <a name="BKMK_Email_DuplicateBaseRecord"></a> Email_DuplicateBaseRecord

See the [Email_DuplicateBaseRecord](email.md#BKMK_Email_DuplicateBaseRecord) one-to-many relationship for the [email](email.md) table/entity.

### <a name="BKMK_PhoneCall_DuplicateMatchingRecord"></a> PhoneCall_DuplicateMatchingRecord

See the [PhoneCall_DuplicateMatchingRecord](phonecall.md#BKMK_PhoneCall_DuplicateMatchingRecord) one-to-many relationship for the [phonecall](phonecall.md) table/entity.

### <a name="BKMK_Team_DuplicateMatchingRecord"></a> Team_DuplicateMatchingRecord

See the [Team_DuplicateMatchingRecord](team.md#BKMK_Team_DuplicateMatchingRecord) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_SystemUser_DuplicateMatchingRecord"></a> SystemUser_DuplicateMatchingRecord

See the [SystemUser_DuplicateMatchingRecord](systemuser.md#BKMK_SystemUser_DuplicateMatchingRecord) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_Appointment_DuplicateMatchingRecord"></a> Appointment_DuplicateMatchingRecord

See the [Appointment_DuplicateMatchingRecord](appointment.md#BKMK_Appointment_DuplicateMatchingRecord) one-to-many relationship for the [appointment](appointment.md) table/entity.

### <a name="BKMK_Account_DuplicateMatchingRecord"></a> Account_DuplicateMatchingRecord

See the [Account_DuplicateMatchingRecord](account.md#BKMK_Account_DuplicateMatchingRecord) one-to-many relationship for the [account](account.md) table/entity.

### <a name="BKMK_Fax_DuplicateBaseRecord"></a> Fax_DuplicateBaseRecord

See the [Fax_DuplicateBaseRecord](fax.md#BKMK_Fax_DuplicateBaseRecord) one-to-many relationship for the [fax](fax.md) table/entity.

### <a name="BKMK_Letter_DuplicateMatchingRecord"></a> Letter_DuplicateMatchingRecord

See the [Letter_DuplicateMatchingRecord](letter.md#BKMK_Letter_DuplicateMatchingRecord) one-to-many relationship for the [letter](letter.md) table/entity.

### <a name="BKMK_emailserverprofile_duplicatematchingrecord"></a> emailserverprofile_duplicatematchingrecord

See the [emailserverprofile_duplicatematchingrecord](emailserverprofile.md#BKMK_emailserverprofile_duplicatematchingrecord) one-to-many relationship for the [emailserverprofile](emailserverprofile.md) table/entity.

### <a name="BKMK_SharePointDocumentLocation_DuplicateBaseRecord"></a> SharePointDocumentLocation_DuplicateBaseRecord

See the [SharePointDocumentLocation_DuplicateBaseRecord](sharepointdocumentlocation.md#BKMK_SharePointDocumentLocation_DuplicateBaseRecord) one-to-many relationship for the [sharepointdocumentlocation](sharepointdocumentlocation.md) table/entity.

### <a name="BKMK_Goal_DuplicateBaseRecord"></a> Goal_DuplicateBaseRecord

See the [Goal_DuplicateBaseRecord](goal.md#BKMK_Goal_DuplicateBaseRecord) one-to-many relationship for the [goal](goal.md) table/entity.

### <a name="BKMK_RecurringAppointmentMaster_DuplicateMatchingRecord"></a> RecurringAppointmentMaster_DuplicateMatchingRecord

See the [RecurringAppointmentMaster_DuplicateMatchingRecord](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_DuplicateMatchingRecord) one-to-many relationship for the [recurringappointmentmaster](recurringappointmentmaster.md) table/entity.

### <a name="BKMK_Task_DuplicateBaseRecord"></a> Task_DuplicateBaseRecord

See the [Task_DuplicateBaseRecord](task.md#BKMK_Task_DuplicateBaseRecord) one-to-many relationship for the [task](task.md) table/entity.

### <a name="BKMK_RecurringAppointmentMaster_DuplicateBaseRecord"></a> RecurringAppointmentMaster_DuplicateBaseRecord

See the [RecurringAppointmentMaster_DuplicateBaseRecord](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_DuplicateBaseRecord) one-to-many relationship for the [recurringappointmentmaster](recurringappointmentmaster.md) table/entity.

### <a name="BKMK_Queue_DuplicateMatchingRecord"></a> Queue_DuplicateMatchingRecord

See the [Queue_DuplicateMatchingRecord](queue.md#BKMK_Queue_DuplicateMatchingRecord) one-to-many relationship for the [queue](queue.md) table/entity.

### <a name="BKMK_SocialProfile_DuplicateBaseRecord"></a> SocialProfile_DuplicateBaseRecord

See the [SocialProfile_DuplicateBaseRecord](socialprofile.md#BKMK_SocialProfile_DuplicateBaseRecord) one-to-many relationship for the [socialprofile](socialprofile.md) table/entity.

### <a name="BKMK_SharePointDocumentLocation_DuplicateMatchingRecord"></a> SharePointDocumentLocation_DuplicateMatchingRecord

See the [SharePointDocumentLocation_DuplicateMatchingRecord](sharepointdocumentlocation.md#BKMK_SharePointDocumentLocation_DuplicateMatchingRecord) one-to-many relationship for the [sharepointdocumentlocation](sharepointdocumentlocation.md) table/entity.

### <a name="BKMK_GoalRollupQuery_DuplicateBaseRecord"></a> GoalRollupQuery_DuplicateBaseRecord

See the [GoalRollupQuery_DuplicateBaseRecord](goalrollupquery.md#BKMK_GoalRollupQuery_DuplicateBaseRecord) one-to-many relationship for the [goalrollupquery](goalrollupquery.md) table/entity.

### <a name="BKMK_AsyncOperation_DuplicateBaseRecord"></a> AsyncOperation_DuplicateBaseRecord

See the [AsyncOperation_DuplicateBaseRecord](asyncoperation.md#BKMK_AsyncOperation_DuplicateBaseRecord) one-to-many relationship for the [asyncoperation](asyncoperation.md) table/entity.

### <a name="BKMK_Fax_DuplicateMatchingRecord"></a> Fax_DuplicateMatchingRecord

See the [Fax_DuplicateMatchingRecord](fax.md#BKMK_Fax_DuplicateMatchingRecord) one-to-many relationship for the [fax](fax.md) table/entity.

### <a name="BKMK_SocialActivity_DuplicateMatchingRecord"></a> SocialActivity_DuplicateMatchingRecord

See the [SocialActivity_DuplicateMatchingRecord](socialactivity.md#BKMK_SocialActivity_DuplicateMatchingRecord) one-to-many relationship for the [socialactivity](socialactivity.md) table/entity.

### <a name="BKMK_feedback_DuplicateBaseRecord"></a> feedback_DuplicateBaseRecord

See the [feedback_DuplicateBaseRecord](feedback.md#BKMK_feedback_DuplicateBaseRecord) one-to-many relationship for the [feedback](feedback.md) table/entity.

### <a name="BKMK_feedback_DuplicateMatchingRecord"></a> feedback_DuplicateMatchingRecord

See the [feedback_DuplicateMatchingRecord](feedback.md#BKMK_feedback_DuplicateMatchingRecord) one-to-many relationship for the [feedback](feedback.md) table/entity.

### <a name="BKMK_solutioncomponentattributeconfiguration_DuplicateMatchingRecord"></a> solutioncomponentattributeconfiguration_DuplicateMatchingRecord

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentattributeconfiguration_DuplicateMatchingRecord](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_DuplicateMatchingRecord) one-to-many relationship for the [solutioncomponentattributeconfiguration](solutioncomponentattributeconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentattributeconfiguration_DuplicateBaseRecord"></a> solutioncomponentattributeconfiguration_DuplicateBaseRecord

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentattributeconfiguration_DuplicateBaseRecord](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_DuplicateBaseRecord) one-to-many relationship for the [solutioncomponentattributeconfiguration](solutioncomponentattributeconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentbatchconfiguration_DuplicateMatchingRecord"></a> solutioncomponentbatchconfiguration_DuplicateMatchingRecord

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentbatchconfiguration_DuplicateMatchingRecord](solutioncomponentbatchconfiguration.md#BKMK_solutioncomponentbatchconfiguration_DuplicateMatchingRecord) one-to-many relationship for the [solutioncomponentbatchconfiguration](solutioncomponentbatchconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentbatchconfiguration_DuplicateBaseRecord"></a> solutioncomponentbatchconfiguration_DuplicateBaseRecord

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentbatchconfiguration_DuplicateBaseRecord](solutioncomponentbatchconfiguration.md#BKMK_solutioncomponentbatchconfiguration_DuplicateBaseRecord) one-to-many relationship for the [solutioncomponentbatchconfiguration](solutioncomponentbatchconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentconfiguration_DuplicateMatchingRecord"></a> solutioncomponentconfiguration_DuplicateMatchingRecord

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentconfiguration_DuplicateMatchingRecord](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_DuplicateMatchingRecord) one-to-many relationship for the [solutioncomponentconfiguration](solutioncomponentconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentconfiguration_DuplicateBaseRecord"></a> solutioncomponentconfiguration_DuplicateBaseRecord

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentconfiguration_DuplicateBaseRecord](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_DuplicateBaseRecord) one-to-many relationship for the [solutioncomponentconfiguration](solutioncomponentconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord"></a> solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord) one-to-many relationship for the [solutioncomponentrelationshipconfiguration](solutioncomponentrelationshipconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentrelationshipconfiguration_DuplicateBaseRecord"></a> solutioncomponentrelationshipconfiguration_DuplicateBaseRecord

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentrelationshipconfiguration_DuplicateBaseRecord](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_DuplicateBaseRecord) one-to-many relationship for the [solutioncomponentrelationshipconfiguration](solutioncomponentrelationshipconfiguration.md) table/entity.

### <a name="BKMK_package_DuplicateMatchingRecord"></a> package_DuplicateMatchingRecord

**Added by**: msdyn_SolutionPackageMapping Solution

See the [package_DuplicateMatchingRecord](package.md#BKMK_package_DuplicateMatchingRecord) one-to-many relationship for the [package](package.md) table/entity.

### <a name="BKMK_package_DuplicateBaseRecord"></a> package_DuplicateBaseRecord

**Added by**: msdyn_SolutionPackageMapping Solution

See the [package_DuplicateBaseRecord](package.md#BKMK_package_DuplicateBaseRecord) one-to-many relationship for the [package](package.md) table/entity.

### <a name="BKMK_stagesolutionupload_DuplicateMatchingRecord"></a> stagesolutionupload_DuplicateMatchingRecord

**Added by**: StageSolutionUpload Solution

See the [stagesolutionupload_DuplicateMatchingRecord](stagesolutionupload.md#BKMK_stagesolutionupload_DuplicateMatchingRecord) one-to-many relationship for the [stagesolutionupload](stagesolutionupload.md) table/entity.

### <a name="BKMK_stagesolutionupload_DuplicateBaseRecord"></a> stagesolutionupload_DuplicateBaseRecord

**Added by**: StageSolutionUpload Solution

See the [stagesolutionupload_DuplicateBaseRecord](stagesolutionupload.md#BKMK_stagesolutionupload_DuplicateBaseRecord) one-to-many relationship for the [stagesolutionupload](stagesolutionupload.md) table/entity.

### <a name="BKMK_exportsolutionupload_DuplicateMatchingRecord"></a> exportsolutionupload_DuplicateMatchingRecord

**Added by**: ExportSolutionUpload Solution

See the [exportsolutionupload_DuplicateMatchingRecord](exportsolutionupload.md#BKMK_exportsolutionupload_DuplicateMatchingRecord) one-to-many relationship for the [exportsolutionupload](exportsolutionupload.md) table/entity.

### <a name="BKMK_exportsolutionupload_DuplicateBaseRecord"></a> exportsolutionupload_DuplicateBaseRecord

**Added by**: ExportSolutionUpload Solution

See the [exportsolutionupload_DuplicateBaseRecord](exportsolutionupload.md#BKMK_exportsolutionupload_DuplicateBaseRecord) one-to-many relationship for the [exportsolutionupload](exportsolutionupload.md) table/entity.

### <a name="BKMK_featurecontrolsetting_DuplicateMatchingRecord"></a> featurecontrolsetting_DuplicateMatchingRecord

**Added by**: msdyn_FeatureControlSetting Solution

See the [featurecontrolsetting_DuplicateMatchingRecord](featurecontrolsetting.md#BKMK_featurecontrolsetting_DuplicateMatchingRecord) one-to-many relationship for the [featurecontrolsetting](featurecontrolsetting.md) table/entity.

### <a name="BKMK_featurecontrolsetting_DuplicateBaseRecord"></a> featurecontrolsetting_DuplicateBaseRecord

**Added by**: msdyn_FeatureControlSetting Solution

See the [featurecontrolsetting_DuplicateBaseRecord](featurecontrolsetting.md#BKMK_featurecontrolsetting_DuplicateBaseRecord) one-to-many relationship for the [featurecontrolsetting](featurecontrolsetting.md) table/entity.

### <a name="BKMK_catalogassignment_DuplicateMatchingRecord"></a> catalogassignment_DuplicateMatchingRecord

**Added by**: CatalogFramework Solution

See the [catalogassignment_DuplicateMatchingRecord](catalogassignment.md#BKMK_catalogassignment_DuplicateMatchingRecord) one-to-many relationship for the [catalogassignment](catalogassignment.md) table/entity.

### <a name="BKMK_catalogassignment_DuplicateBaseRecord"></a> catalogassignment_DuplicateBaseRecord

**Added by**: CatalogFramework Solution

See the [catalogassignment_DuplicateBaseRecord](catalogassignment.md#BKMK_catalogassignment_DuplicateBaseRecord) one-to-many relationship for the [catalogassignment](catalogassignment.md) table/entity.

### <a name="BKMK_datalakefolder_DuplicateMatchingRecord"></a> datalakefolder_DuplicateMatchingRecord

**Added by**: Data lake workspaces Solution

See the [datalakefolder_DuplicateMatchingRecord](datalakefolder.md#BKMK_datalakefolder_DuplicateMatchingRecord) one-to-many relationship for the [datalakefolder](datalakefolder.md) table/entity.

### <a name="BKMK_datalakefolder_DuplicateBaseRecord"></a> datalakefolder_DuplicateBaseRecord

**Added by**: Data lake workspaces Solution

See the [datalakefolder_DuplicateBaseRecord](datalakefolder.md#BKMK_datalakefolder_DuplicateBaseRecord) one-to-many relationship for the [datalakefolder](datalakefolder.md) table/entity.

### <a name="BKMK_datalakefolderpermission_DuplicateMatchingRecord"></a> datalakefolderpermission_DuplicateMatchingRecord

**Added by**: Data lake workspaces Solution

See the [datalakefolderpermission_DuplicateMatchingRecord](datalakefolderpermission.md#BKMK_datalakefolderpermission_DuplicateMatchingRecord) one-to-many relationship for the [datalakefolderpermission](datalakefolderpermission.md) table/entity.

### <a name="BKMK_datalakefolderpermission_DuplicateBaseRecord"></a> datalakefolderpermission_DuplicateBaseRecord

**Added by**: Data lake workspaces Solution

See the [datalakefolderpermission_DuplicateBaseRecord](datalakefolderpermission.md#BKMK_datalakefolderpermission_DuplicateBaseRecord) one-to-many relationship for the [datalakefolderpermission](datalakefolderpermission.md) table/entity.

### <a name="BKMK_datalakeworkspace_DuplicateMatchingRecord"></a> datalakeworkspace_DuplicateMatchingRecord

**Added by**: Data lake workspaces Solution

See the [datalakeworkspace_DuplicateMatchingRecord](datalakeworkspace.md#BKMK_datalakeworkspace_DuplicateMatchingRecord) one-to-many relationship for the [datalakeworkspace](datalakeworkspace.md) table/entity.

### <a name="BKMK_datalakeworkspace_DuplicateBaseRecord"></a> datalakeworkspace_DuplicateBaseRecord

**Added by**: Data lake workspaces Solution

See the [datalakeworkspace_DuplicateBaseRecord](datalakeworkspace.md#BKMK_datalakeworkspace_DuplicateBaseRecord) one-to-many relationship for the [datalakeworkspace](datalakeworkspace.md) table/entity.

### <a name="BKMK_datalakeworkspacepermission_DuplicateMatchingRecord"></a> datalakeworkspacepermission_DuplicateMatchingRecord

**Added by**: Data lake workspaces Solution

See the [datalakeworkspacepermission_DuplicateMatchingRecord](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_DuplicateMatchingRecord) one-to-many relationship for the [datalakeworkspacepermission](datalakeworkspacepermission.md) table/entity.

### <a name="BKMK_datalakeworkspacepermission_DuplicateBaseRecord"></a> datalakeworkspacepermission_DuplicateBaseRecord

**Added by**: Data lake workspaces Solution

See the [datalakeworkspacepermission_DuplicateBaseRecord](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_DuplicateBaseRecord) one-to-many relationship for the [datalakeworkspacepermission](datalakeworkspacepermission.md) table/entity.

### <a name="BKMK_dataprocessingconfiguration_DuplicateMatchingRecord"></a> dataprocessingconfiguration_DuplicateMatchingRecord

**Added by**: Data lake workspaces Solution

See the [dataprocessingconfiguration_DuplicateMatchingRecord](dataprocessingconfiguration.md#BKMK_dataprocessingconfiguration_DuplicateMatchingRecord) one-to-many relationship for the [dataprocessingconfiguration](dataprocessingconfiguration.md) table/entity.

### <a name="BKMK_dataprocessingconfiguration_DuplicateBaseRecord"></a> dataprocessingconfiguration_DuplicateBaseRecord

**Added by**: Data lake workspaces Solution

See the [dataprocessingconfiguration_DuplicateBaseRecord](dataprocessingconfiguration.md#BKMK_dataprocessingconfiguration_DuplicateBaseRecord) one-to-many relationship for the [dataprocessingconfiguration](dataprocessingconfiguration.md) table/entity.

### <a name="BKMK_synapsedatabase_DuplicateMatchingRecord"></a> synapsedatabase_DuplicateMatchingRecord

**Added by**: Data lake workspaces Solution

See the [synapsedatabase_DuplicateMatchingRecord](synapsedatabase.md#BKMK_synapsedatabase_DuplicateMatchingRecord) one-to-many relationship for the [synapsedatabase](synapsedatabase.md) table/entity.

### <a name="BKMK_synapsedatabase_DuplicateBaseRecord"></a> synapsedatabase_DuplicateBaseRecord

**Added by**: Data lake workspaces Solution

See the [synapsedatabase_DuplicateBaseRecord](synapsedatabase.md#BKMK_synapsedatabase_DuplicateBaseRecord) one-to-many relationship for the [synapsedatabase](synapsedatabase.md) table/entity.

### <a name="BKMK_synapselinkexternaltablestate_DuplicateMatchingRecord"></a> synapselinkexternaltablestate_DuplicateMatchingRecord

**Added by**: Synapse Link Solution

See the [synapselinkexternaltablestate_DuplicateMatchingRecord](synapselinkexternaltablestate.md#BKMK_synapselinkexternaltablestate_DuplicateMatchingRecord) one-to-many relationship for the [synapselinkexternaltablestate](synapselinkexternaltablestate.md) table/entity.

### <a name="BKMK_synapselinkexternaltablestate_DuplicateBaseRecord"></a> synapselinkexternaltablestate_DuplicateBaseRecord

**Added by**: Synapse Link Solution

See the [synapselinkexternaltablestate_DuplicateBaseRecord](synapselinkexternaltablestate.md#BKMK_synapselinkexternaltablestate_DuplicateBaseRecord) one-to-many relationship for the [synapselinkexternaltablestate](synapselinkexternaltablestate.md) table/entity.

### <a name="BKMK_synapselinkprofile_DuplicateMatchingRecord"></a> synapselinkprofile_DuplicateMatchingRecord

**Added by**: Synapse Link Solution

See the [synapselinkprofile_DuplicateMatchingRecord](synapselinkprofile.md#BKMK_synapselinkprofile_DuplicateMatchingRecord) one-to-many relationship for the [synapselinkprofile](synapselinkprofile.md) table/entity.

### <a name="BKMK_synapselinkprofile_DuplicateBaseRecord"></a> synapselinkprofile_DuplicateBaseRecord

**Added by**: Synapse Link Solution

See the [synapselinkprofile_DuplicateBaseRecord](synapselinkprofile.md#BKMK_synapselinkprofile_DuplicateBaseRecord) one-to-many relationship for the [synapselinkprofile](synapselinkprofile.md) table/entity.

### <a name="BKMK_synapselinkprofileentity_DuplicateMatchingRecord"></a> synapselinkprofileentity_DuplicateMatchingRecord

**Added by**: Synapse Link Solution

See the [synapselinkprofileentity_DuplicateMatchingRecord](synapselinkprofileentity.md#BKMK_synapselinkprofileentity_DuplicateMatchingRecord) one-to-many relationship for the [synapselinkprofileentity](synapselinkprofileentity.md) table/entity.

### <a name="BKMK_synapselinkprofileentity_DuplicateBaseRecord"></a> synapselinkprofileentity_DuplicateBaseRecord

**Added by**: Synapse Link Solution

See the [synapselinkprofileentity_DuplicateBaseRecord](synapselinkprofileentity.md#BKMK_synapselinkprofileentity_DuplicateBaseRecord) one-to-many relationship for the [synapselinkprofileentity](synapselinkprofileentity.md) table/entity.

### <a name="BKMK_synapselinkprofileentitystate_DuplicateMatchingRecord"></a> synapselinkprofileentitystate_DuplicateMatchingRecord

**Added by**: Synapse Link Solution

See the [synapselinkprofileentitystate_DuplicateMatchingRecord](synapselinkprofileentitystate.md#BKMK_synapselinkprofileentitystate_DuplicateMatchingRecord) one-to-many relationship for the [synapselinkprofileentitystate](synapselinkprofileentitystate.md) table/entity.

### <a name="BKMK_synapselinkprofileentitystate_DuplicateBaseRecord"></a> synapselinkprofileentitystate_DuplicateBaseRecord

**Added by**: Synapse Link Solution

See the [synapselinkprofileentitystate_DuplicateBaseRecord](synapselinkprofileentitystate.md#BKMK_synapselinkprofileentitystate_DuplicateBaseRecord) one-to-many relationship for the [synapselinkprofileentitystate](synapselinkprofileentitystate.md) table/entity.

### <a name="BKMK_synapselinkschedule_DuplicateMatchingRecord"></a> synapselinkschedule_DuplicateMatchingRecord

**Added by**: Synapse Link Solution

See the [synapselinkschedule_DuplicateMatchingRecord](synapselinkschedule.md#BKMK_synapselinkschedule_DuplicateMatchingRecord) one-to-many relationship for the [synapselinkschedule](synapselinkschedule.md) table/entity.

### <a name="BKMK_synapselinkschedule_DuplicateBaseRecord"></a> synapselinkschedule_DuplicateBaseRecord

**Added by**: Synapse Link Solution

See the [synapselinkschedule_DuplicateBaseRecord](synapselinkschedule.md#BKMK_synapselinkschedule_DuplicateBaseRecord) one-to-many relationship for the [synapselinkschedule](synapselinkschedule.md) table/entity.

### <a name="BKMK_msdyn_dataflow_DuplicateMatchingRecord"></a> msdyn_dataflow_DuplicateMatchingRecord

**Added by**: Dataflow Solution Solution

See the [msdyn_dataflow_DuplicateMatchingRecord](msdyn_dataflow.md#BKMK_msdyn_dataflow_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_dataflow](msdyn_dataflow.md) table/entity.

### <a name="BKMK_msdyn_dataflow_DuplicateBaseRecord"></a> msdyn_dataflow_DuplicateBaseRecord

**Added by**: Dataflow Solution Solution

See the [msdyn_dataflow_DuplicateBaseRecord](msdyn_dataflow.md#BKMK_msdyn_dataflow_DuplicateBaseRecord) one-to-many relationship for the [msdyn_dataflow](msdyn_dataflow.md) table/entity.

### <a name="BKMK_msdyn_dataflowrefreshhistory_DuplicateMatchingRecord"></a> msdyn_dataflowrefreshhistory_DuplicateMatchingRecord

**Added by**: Dataflow Solution Solution

See the [msdyn_dataflowrefreshhistory_DuplicateMatchingRecord](msdyn_dataflowrefreshhistory.md#BKMK_msdyn_dataflowrefreshhistory_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_dataflowrefreshhistory](msdyn_dataflowrefreshhistory.md) table/entity.

### <a name="BKMK_msdyn_dataflowrefreshhistory_DuplicateBaseRecord"></a> msdyn_dataflowrefreshhistory_DuplicateBaseRecord

**Added by**: Dataflow Solution Solution

See the [msdyn_dataflowrefreshhistory_DuplicateBaseRecord](msdyn_dataflowrefreshhistory.md#BKMK_msdyn_dataflowrefreshhistory_DuplicateBaseRecord) one-to-many relationship for the [msdyn_dataflowrefreshhistory](msdyn_dataflowrefreshhistory.md) table/entity.

### <a name="BKMK_msdyn_entityrefreshhistory_DuplicateMatchingRecord"></a> msdyn_entityrefreshhistory_DuplicateMatchingRecord

**Added by**: Dataflow Solution Solution

See the [msdyn_entityrefreshhistory_DuplicateMatchingRecord](msdyn_entityrefreshhistory.md#BKMK_msdyn_entityrefreshhistory_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_entityrefreshhistory](msdyn_entityrefreshhistory.md) table/entity.

### <a name="BKMK_msdyn_entityrefreshhistory_DuplicateBaseRecord"></a> msdyn_entityrefreshhistory_DuplicateBaseRecord

**Added by**: Dataflow Solution Solution

See the [msdyn_entityrefreshhistory_DuplicateBaseRecord](msdyn_entityrefreshhistory.md#BKMK_msdyn_entityrefreshhistory_DuplicateBaseRecord) one-to-many relationship for the [msdyn_entityrefreshhistory](msdyn_entityrefreshhistory.md) table/entity.

### <a name="BKMK_sharedlinksetting_DuplicateMatchingRecord"></a> sharedlinksetting_DuplicateMatchingRecord

**Added by**: Access Team Solution

See the [sharedlinksetting_DuplicateMatchingRecord](sharedlinksetting.md#BKMK_sharedlinksetting_DuplicateMatchingRecord) one-to-many relationship for the [sharedlinksetting](sharedlinksetting.md) table/entity.

### <a name="BKMK_sharedlinksetting_DuplicateBaseRecord"></a> sharedlinksetting_DuplicateBaseRecord

**Added by**: Access Team Solution

See the [sharedlinksetting_DuplicateBaseRecord](sharedlinksetting.md#BKMK_sharedlinksetting_DuplicateBaseRecord) one-to-many relationship for the [sharedlinksetting](sharedlinksetting.md) table/entity.

### <a name="BKMK_serviceplan_DuplicateMatchingRecord"></a> serviceplan_DuplicateMatchingRecord

**Added by**: License Enforcement Solution

See the [serviceplan_DuplicateMatchingRecord](serviceplan.md#BKMK_serviceplan_DuplicateMatchingRecord) one-to-many relationship for the [serviceplan](serviceplan.md) table/entity.

### <a name="BKMK_serviceplan_DuplicateBaseRecord"></a> serviceplan_DuplicateBaseRecord

**Added by**: License Enforcement Solution

See the [serviceplan_DuplicateBaseRecord](serviceplan.md#BKMK_serviceplan_DuplicateBaseRecord) one-to-many relationship for the [serviceplan](serviceplan.md) table/entity.

### <a name="BKMK_serviceplanmapping_DuplicateMatchingRecord"></a> serviceplanmapping_DuplicateMatchingRecord

**Added by**: License Enforcement Solution

See the [serviceplanmapping_DuplicateMatchingRecord](serviceplanmapping.md#BKMK_serviceplanmapping_DuplicateMatchingRecord) one-to-many relationship for the [serviceplanmapping](serviceplanmapping.md) table/entity.

### <a name="BKMK_serviceplanmapping_DuplicateBaseRecord"></a> serviceplanmapping_DuplicateBaseRecord

**Added by**: License Enforcement Solution

See the [serviceplanmapping_DuplicateBaseRecord](serviceplanmapping.md#BKMK_serviceplanmapping_DuplicateBaseRecord) one-to-many relationship for the [serviceplanmapping](serviceplanmapping.md) table/entity.

### <a name="BKMK_applicationuser_DuplicateMatchingRecord"></a> applicationuser_DuplicateMatchingRecord

**Added by**: ApplicationUserSolution Solution

See the [applicationuser_DuplicateMatchingRecord](applicationuser.md#BKMK_applicationuser_DuplicateMatchingRecord) one-to-many relationship for the [applicationuser](applicationuser.md) table/entity.

### <a name="BKMK_applicationuser_DuplicateBaseRecord"></a> applicationuser_DuplicateBaseRecord

**Added by**: ApplicationUserSolution Solution

See the [applicationuser_DuplicateBaseRecord](applicationuser.md#BKMK_applicationuser_DuplicateBaseRecord) one-to-many relationship for the [applicationuser](applicationuser.md) table/entity.

### <a name="BKMK_connector_DuplicateMatchingRecord"></a> connector_DuplicateMatchingRecord

**Added by**: Power Connector Solution Solution

See the [connector_DuplicateMatchingRecord](connector.md#BKMK_connector_DuplicateMatchingRecord) one-to-many relationship for the [connector](connector.md) table/entity.

### <a name="BKMK_connector_DuplicateBaseRecord"></a> connector_DuplicateBaseRecord

**Added by**: Power Connector Solution Solution

See the [connector_DuplicateBaseRecord](connector.md#BKMK_connector_DuplicateBaseRecord) one-to-many relationship for the [connector](connector.md) table/entity.

### <a name="BKMK_environmentvariabledefinition_DuplicateMatchingRecord"></a> environmentvariabledefinition_DuplicateMatchingRecord

**Added by**: Environment Variables Solution

See the [environmentvariabledefinition_DuplicateMatchingRecord](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_DuplicateMatchingRecord) one-to-many relationship for the [environmentvariabledefinition](environmentvariabledefinition.md) table/entity.

### <a name="BKMK_environmentvariabledefinition_DuplicateBaseRecord"></a> environmentvariabledefinition_DuplicateBaseRecord

**Added by**: Environment Variables Solution

See the [environmentvariabledefinition_DuplicateBaseRecord](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_DuplicateBaseRecord) one-to-many relationship for the [environmentvariabledefinition](environmentvariabledefinition.md) table/entity.

### <a name="BKMK_environmentvariablevalue_DuplicateMatchingRecord"></a> environmentvariablevalue_DuplicateMatchingRecord

**Added by**: Environment Variables Solution

See the [environmentvariablevalue_DuplicateMatchingRecord](environmentvariablevalue.md#BKMK_environmentvariablevalue_DuplicateMatchingRecord) one-to-many relationship for the [environmentvariablevalue](environmentvariablevalue.md) table/entity.

### <a name="BKMK_environmentvariablevalue_DuplicateBaseRecord"></a> environmentvariablevalue_DuplicateBaseRecord

**Added by**: Environment Variables Solution

See the [environmentvariablevalue_DuplicateBaseRecord](environmentvariablevalue.md#BKMK_environmentvariablevalue_DuplicateBaseRecord) one-to-many relationship for the [environmentvariablevalue](environmentvariablevalue.md) table/entity.

### <a name="BKMK_flowmachinegroup_DuplicateMatchingRecord"></a> flowmachinegroup_DuplicateMatchingRecord

**Added by**: Power Automate Extensions core package Solution

See the [flowmachinegroup_DuplicateMatchingRecord](flowmachinegroup.md#BKMK_flowmachinegroup_DuplicateMatchingRecord) one-to-many relationship for the [flowmachinegroup](flowmachinegroup.md) table/entity.

### <a name="BKMK_flowmachinegroup_DuplicateBaseRecord"></a> flowmachinegroup_DuplicateBaseRecord

**Added by**: Power Automate Extensions core package Solution

See the [flowmachinegroup_DuplicateBaseRecord](flowmachinegroup.md#BKMK_flowmachinegroup_DuplicateBaseRecord) one-to-many relationship for the [flowmachinegroup](flowmachinegroup.md) table/entity.

### <a name="BKMK_flowmachineimage_DuplicateMatchingRecord"></a> flowmachineimage_DuplicateMatchingRecord

**Added by**: Power Automate Extensions core package Solution

See the [flowmachineimage_DuplicateMatchingRecord](flowmachineimage.md#BKMK_flowmachineimage_DuplicateMatchingRecord) one-to-many relationship for the [flowmachineimage](flowmachineimage.md) table/entity.

### <a name="BKMK_flowmachineimage_DuplicateBaseRecord"></a> flowmachineimage_DuplicateBaseRecord

**Added by**: Power Automate Extensions core package Solution

See the [flowmachineimage_DuplicateBaseRecord](flowmachineimage.md#BKMK_flowmachineimage_DuplicateBaseRecord) one-to-many relationship for the [flowmachineimage](flowmachineimage.md) table/entity.

### <a name="BKMK_flowmachineimageversion_DuplicateMatchingRecord"></a> flowmachineimageversion_DuplicateMatchingRecord

**Added by**: Power Automate Extensions core package Solution

See the [flowmachineimageversion_DuplicateMatchingRecord](flowmachineimageversion.md#BKMK_flowmachineimageversion_DuplicateMatchingRecord) one-to-many relationship for the [flowmachineimageversion](flowmachineimageversion.md) table/entity.

### <a name="BKMK_flowmachineimageversion_DuplicateBaseRecord"></a> flowmachineimageversion_DuplicateBaseRecord

**Added by**: Power Automate Extensions core package Solution

See the [flowmachineimageversion_DuplicateBaseRecord](flowmachineimageversion.md#BKMK_flowmachineimageversion_DuplicateBaseRecord) one-to-many relationship for the [flowmachineimageversion](flowmachineimageversion.md) table/entity.

### <a name="BKMK_msdyn_aibfeedbackloop_DuplicateMatchingRecord"></a> msdyn_aibfeedbackloop_DuplicateMatchingRecord

**Added by**: AISolutionFullAdditions Solution

See the [msdyn_aibfeedbackloop_DuplicateMatchingRecord](msdyn_aibfeedbackloop.md#BKMK_msdyn_aibfeedbackloop_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_aibfeedbackloop](msdyn_aibfeedbackloop.md) table/entity.

### <a name="BKMK_msdyn_aibfeedbackloop_DuplicateBaseRecord"></a> msdyn_aibfeedbackloop_DuplicateBaseRecord

**Added by**: AISolutionFullAdditions Solution

See the [msdyn_aibfeedbackloop_DuplicateBaseRecord](msdyn_aibfeedbackloop.md#BKMK_msdyn_aibfeedbackloop_DuplicateBaseRecord) one-to-many relationship for the [msdyn_aibfeedbackloop](msdyn_aibfeedbackloop.md) table/entity.

### <a name="BKMK_msdyn_aiodimage_DuplicateMatchingRecord"></a> msdyn_aiodimage_DuplicateMatchingRecord

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodimage_DuplicateMatchingRecord](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_aiodimage](msdyn_aiodimage.md) table/entity.

### <a name="BKMK_msdyn_aiodimage_DuplicateBaseRecord"></a> msdyn_aiodimage_DuplicateBaseRecord

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodimage_DuplicateBaseRecord](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_DuplicateBaseRecord) one-to-many relationship for the [msdyn_aiodimage](msdyn_aiodimage.md) table/entity.

### <a name="BKMK_msdyn_aiodlabel_DuplicateMatchingRecord"></a> msdyn_aiodlabel_DuplicateMatchingRecord

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodlabel_DuplicateMatchingRecord](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_aiodlabel](msdyn_aiodlabel.md) table/entity.

### <a name="BKMK_msdyn_aiodlabel_DuplicateBaseRecord"></a> msdyn_aiodlabel_DuplicateBaseRecord

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodlabel_DuplicateBaseRecord](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_DuplicateBaseRecord) one-to-many relationship for the [msdyn_aiodlabel](msdyn_aiodlabel.md) table/entity.

### <a name="BKMK_msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord"></a> msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_aiodtrainingboundingbox](msdyn_aiodtrainingboundingbox.md) table/entity.

### <a name="BKMK_msdyn_aiodtrainingboundingbox_DuplicateBaseRecord"></a> msdyn_aiodtrainingboundingbox_DuplicateBaseRecord

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodtrainingboundingbox_DuplicateBaseRecord](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_DuplicateBaseRecord) one-to-many relationship for the [msdyn_aiodtrainingboundingbox](msdyn_aiodtrainingboundingbox.md) table/entity.

### <a name="BKMK_msdyn_aiodtrainingimage_DuplicateMatchingRecord"></a> msdyn_aiodtrainingimage_DuplicateMatchingRecord

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodtrainingimage_DuplicateMatchingRecord](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_aiodtrainingimage](msdyn_aiodtrainingimage.md) table/entity.

### <a name="BKMK_msdyn_aiodtrainingimage_DuplicateBaseRecord"></a> msdyn_aiodtrainingimage_DuplicateBaseRecord

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodtrainingimage_DuplicateBaseRecord](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_DuplicateBaseRecord) one-to-many relationship for the [msdyn_aiodtrainingimage](msdyn_aiodtrainingimage.md) table/entity.

### <a name="BKMK_msdyn_aibdataset_DuplicateMatchingRecord"></a> msdyn_aibdataset_DuplicateMatchingRecord

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdataset_DuplicateMatchingRecord](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_aibdataset](msdyn_aibdataset.md) table/entity.

### <a name="BKMK_msdyn_aibdataset_DuplicateBaseRecord"></a> msdyn_aibdataset_DuplicateBaseRecord

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdataset_DuplicateBaseRecord](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_DuplicateBaseRecord) one-to-many relationship for the [msdyn_aibdataset](msdyn_aibdataset.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetfile_DuplicateMatchingRecord"></a> msdyn_aibdatasetfile_DuplicateMatchingRecord

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetfile_DuplicateMatchingRecord](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_aibdatasetfile](msdyn_aibdatasetfile.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetfile_DuplicateBaseRecord"></a> msdyn_aibdatasetfile_DuplicateBaseRecord

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetfile_DuplicateBaseRecord](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_DuplicateBaseRecord) one-to-many relationship for the [msdyn_aibdatasetfile](msdyn_aibdatasetfile.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetrecord_DuplicateMatchingRecord"></a> msdyn_aibdatasetrecord_DuplicateMatchingRecord

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetrecord_DuplicateMatchingRecord](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_aibdatasetrecord](msdyn_aibdatasetrecord.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetrecord_DuplicateBaseRecord"></a> msdyn_aibdatasetrecord_DuplicateBaseRecord

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetrecord_DuplicateBaseRecord](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_DuplicateBaseRecord) one-to-many relationship for the [msdyn_aibdatasetrecord](msdyn_aibdatasetrecord.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetscontainer_DuplicateMatchingRecord"></a> msdyn_aibdatasetscontainer_DuplicateMatchingRecord

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetscontainer_DuplicateMatchingRecord](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_aibdatasetscontainer](msdyn_aibdatasetscontainer.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetscontainer_DuplicateBaseRecord"></a> msdyn_aibdatasetscontainer_DuplicateBaseRecord

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetscontainer_DuplicateBaseRecord](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_DuplicateBaseRecord) one-to-many relationship for the [msdyn_aibdatasetscontainer](msdyn_aibdatasetscontainer.md) table/entity.

### <a name="BKMK_msdyn_aibfile_DuplicateMatchingRecord"></a> msdyn_aibfile_DuplicateMatchingRecord

**Added by**: AI Solution default templates Solution

See the [msdyn_aibfile_DuplicateMatchingRecord](msdyn_aibfile.md#BKMK_msdyn_aibfile_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_aibfile](msdyn_aibfile.md) table/entity.

### <a name="BKMK_msdyn_aibfile_DuplicateBaseRecord"></a> msdyn_aibfile_DuplicateBaseRecord

**Added by**: AI Solution default templates Solution

See the [msdyn_aibfile_DuplicateBaseRecord](msdyn_aibfile.md#BKMK_msdyn_aibfile_DuplicateBaseRecord) one-to-many relationship for the [msdyn_aibfile](msdyn_aibfile.md) table/entity.

### <a name="BKMK_msdyn_aibfileattacheddata_DuplicateMatchingRecord"></a> msdyn_aibfileattacheddata_DuplicateMatchingRecord

**Added by**: AI Solution default templates Solution

See the [msdyn_aibfileattacheddata_DuplicateMatchingRecord](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_aibfileattacheddata](msdyn_aibfileattacheddata.md) table/entity.

### <a name="BKMK_msdyn_aibfileattacheddata_DuplicateBaseRecord"></a> msdyn_aibfileattacheddata_DuplicateBaseRecord

**Added by**: AI Solution default templates Solution

See the [msdyn_aibfileattacheddata_DuplicateBaseRecord](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_DuplicateBaseRecord) one-to-many relationship for the [msdyn_aibfileattacheddata](msdyn_aibfileattacheddata.md) table/entity.

### <a name="BKMK_conversationtranscript_DuplicateMatchingRecord"></a> conversationtranscript_DuplicateMatchingRecord

**Added by**: Power Virtual Agents Common Solution

See the [conversationtranscript_DuplicateMatchingRecord](conversationtranscript.md#BKMK_conversationtranscript_DuplicateMatchingRecord) one-to-many relationship for the [conversationtranscript](conversationtranscript.md) table/entity.

### <a name="BKMK_conversationtranscript_DuplicateBaseRecord"></a> conversationtranscript_DuplicateBaseRecord

**Added by**: Power Virtual Agents Common Solution

See the [conversationtranscript_DuplicateBaseRecord](conversationtranscript.md#BKMK_conversationtranscript_DuplicateBaseRecord) one-to-many relationship for the [conversationtranscript](conversationtranscript.md) table/entity.

### <a name="BKMK_activityfileattachment_DuplicateMatchingRecord"></a> activityfileattachment_DuplicateMatchingRecord

**Added by**: Activities Patch Solution

See the [activityfileattachment_DuplicateMatchingRecord](activityfileattachment.md#BKMK_activityfileattachment_DuplicateMatchingRecord) one-to-many relationship for the [activityfileattachment](activityfileattachment.md) table/entity.

### <a name="BKMK_activityfileattachment_DuplicateBaseRecord"></a> activityfileattachment_DuplicateBaseRecord

**Added by**: Activities Patch Solution

See the [activityfileattachment_DuplicateBaseRecord](activityfileattachment.md#BKMK_activityfileattachment_DuplicateBaseRecord) one-to-many relationship for the [activityfileattachment](activityfileattachment.md) table/entity.

### <a name="BKMK_chat_DuplicateMatchingRecord"></a> chat_DuplicateMatchingRecord

**Added by**: Activities Patch Solution

See the [chat_DuplicateMatchingRecord](chat.md#BKMK_chat_DuplicateMatchingRecord) one-to-many relationship for the [chat](chat.md) table/entity.

### <a name="BKMK_chat_DuplicateBaseRecord"></a> chat_DuplicateBaseRecord

**Added by**: Activities Patch Solution

See the [chat_DuplicateBaseRecord](chat.md#BKMK_chat_DuplicateBaseRecord) one-to-many relationship for the [chat](chat.md) table/entity.

### <a name="BKMK_msdyn_serviceconfiguration_DuplicateMatchingRecord"></a> msdyn_serviceconfiguration_DuplicateMatchingRecord

**Added by**: Service Level Agreement (SLA) Extension Solution

See the [msdyn_serviceconfiguration_DuplicateMatchingRecord](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_serviceconfiguration](msdyn_serviceconfiguration.md) table/entity.

### <a name="BKMK_msdyn_serviceconfiguration_DuplicateBaseRecord"></a> msdyn_serviceconfiguration_DuplicateBaseRecord

**Added by**: Service Level Agreement (SLA) Extension Solution

See the [msdyn_serviceconfiguration_DuplicateBaseRecord](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_DuplicateBaseRecord) one-to-many relationship for the [msdyn_serviceconfiguration](msdyn_serviceconfiguration.md) table/entity.

### <a name="BKMK_msdyn_slakpi_DuplicateMatchingRecord"></a> msdyn_slakpi_DuplicateMatchingRecord

**Added by**: Service Level Agreement (SLA) Extension Solution

See the [msdyn_slakpi_DuplicateMatchingRecord](msdyn_slakpi.md#BKMK_msdyn_slakpi_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_slakpi](msdyn_slakpi.md) table/entity.

### <a name="BKMK_msdyn_slakpi_DuplicateBaseRecord"></a> msdyn_slakpi_DuplicateBaseRecord

**Added by**: Service Level Agreement (SLA) Extension Solution

See the [msdyn_slakpi_DuplicateBaseRecord](msdyn_slakpi.md#BKMK_msdyn_slakpi_DuplicateBaseRecord) one-to-many relationship for the [msdyn_slakpi](msdyn_slakpi.md) table/entity.

### <a name="BKMK_msdyn_knowledgemanagementsetting_DuplicateMatchingRecord"></a> msdyn_knowledgemanagementsetting_DuplicateMatchingRecord

**Added by**: Knowledge Management Patch Solution

See the [msdyn_knowledgemanagementsetting_DuplicateMatchingRecord](msdyn_knowledgemanagementsetting.md#BKMK_msdyn_knowledgemanagementsetting_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_knowledgemanagementsetting](msdyn_knowledgemanagementsetting.md) table/entity.

### <a name="BKMK_msdyn_knowledgemanagementsetting_DuplicateBaseRecord"></a> msdyn_knowledgemanagementsetting_DuplicateBaseRecord

**Added by**: Knowledge Management Patch Solution

See the [msdyn_knowledgemanagementsetting_DuplicateBaseRecord](msdyn_knowledgemanagementsetting.md#BKMK_msdyn_knowledgemanagementsetting_DuplicateBaseRecord) one-to-many relationship for the [msdyn_knowledgemanagementsetting](msdyn_knowledgemanagementsetting.md) table/entity.

### <a name="BKMK_msdyn_federatedarticle_DuplicateMatchingRecord"></a> msdyn_federatedarticle_DuplicateMatchingRecord

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_federatedarticle_DuplicateMatchingRecord](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_federatedarticle](msdyn_federatedarticle.md) table/entity.

### <a name="BKMK_msdyn_federatedarticle_DuplicateBaseRecord"></a> msdyn_federatedarticle_DuplicateBaseRecord

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_federatedarticle_DuplicateBaseRecord](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_DuplicateBaseRecord) one-to-many relationship for the [msdyn_federatedarticle](msdyn_federatedarticle.md) table/entity.

### <a name="BKMK_msdyn_federatedarticleincident_DuplicateMatchingRecord"></a> msdyn_federatedarticleincident_DuplicateMatchingRecord

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_federatedarticleincident_DuplicateMatchingRecord](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_federatedarticleincident](msdyn_federatedarticleincident.md) table/entity.

### <a name="BKMK_msdyn_federatedarticleincident_DuplicateBaseRecord"></a> msdyn_federatedarticleincident_DuplicateBaseRecord

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_federatedarticleincident_DuplicateBaseRecord](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_DuplicateBaseRecord) one-to-many relationship for the [msdyn_federatedarticleincident](msdyn_federatedarticleincident.md) table/entity.

### <a name="BKMK_msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord"></a> msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_kmfederatedsearchconfig](msdyn_kmfederatedsearchconfig.md) table/entity.

### <a name="BKMK_msdyn_kmfederatedsearchconfig_DuplicateBaseRecord"></a> msdyn_kmfederatedsearchconfig_DuplicateBaseRecord

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_kmfederatedsearchconfig_DuplicateBaseRecord](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_DuplicateBaseRecord) one-to-many relationship for the [msdyn_kmfederatedsearchconfig](msdyn_kmfederatedsearchconfig.md) table/entity.

### <a name="BKMK_msdyn_knowledgearticleimage_DuplicateMatchingRecord"></a> msdyn_knowledgearticleimage_DuplicateMatchingRecord

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgearticleimage_DuplicateMatchingRecord](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_knowledgearticleimage](msdyn_knowledgearticleimage.md) table/entity.

### <a name="BKMK_msdyn_knowledgearticleimage_DuplicateBaseRecord"></a> msdyn_knowledgearticleimage_DuplicateBaseRecord

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgearticleimage_DuplicateBaseRecord](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_DuplicateBaseRecord) one-to-many relationship for the [msdyn_knowledgearticleimage](msdyn_knowledgearticleimage.md) table/entity.

### <a name="BKMK_msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord"></a> msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_knowledgeinteractioninsight](msdyn_knowledgeinteractioninsight.md) table/entity.

### <a name="BKMK_msdyn_knowledgeinteractioninsight_DuplicateBaseRecord"></a> msdyn_knowledgeinteractioninsight_DuplicateBaseRecord

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgeinteractioninsight_DuplicateBaseRecord](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_DuplicateBaseRecord) one-to-many relationship for the [msdyn_knowledgeinteractioninsight](msdyn_knowledgeinteractioninsight.md) table/entity.

### <a name="BKMK_msdyn_knowledgesearchinsight_DuplicateMatchingRecord"></a> msdyn_knowledgesearchinsight_DuplicateMatchingRecord

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgesearchinsight_DuplicateMatchingRecord](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_knowledgesearchinsight](msdyn_knowledgesearchinsight.md) table/entity.

### <a name="BKMK_msdyn_knowledgesearchinsight_DuplicateBaseRecord"></a> msdyn_knowledgesearchinsight_DuplicateBaseRecord

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgesearchinsight_DuplicateBaseRecord](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_DuplicateBaseRecord) one-to-many relationship for the [msdyn_knowledgesearchinsight](msdyn_knowledgesearchinsight.md) table/entity.

### <a name="BKMK_msdyn_kalanguagesetting_DuplicateMatchingRecord"></a> msdyn_kalanguagesetting_DuplicateMatchingRecord

**Added by**: Knowledge Management Features Solution

See the [msdyn_kalanguagesetting_DuplicateMatchingRecord](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_kalanguagesetting](msdyn_kalanguagesetting.md) table/entity.

### <a name="BKMK_msdyn_kalanguagesetting_DuplicateBaseRecord"></a> msdyn_kalanguagesetting_DuplicateBaseRecord

**Added by**: Knowledge Management Features Solution

See the [msdyn_kalanguagesetting_DuplicateBaseRecord](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_DuplicateBaseRecord) one-to-many relationship for the [msdyn_kalanguagesetting](msdyn_kalanguagesetting.md) table/entity.

### <a name="BKMK_msdyn_kbattachment_DuplicateMatchingRecord"></a> msdyn_kbattachment_DuplicateMatchingRecord

**Added by**: Knowledge Management Features Solution

See the [msdyn_kbattachment_DuplicateMatchingRecord](msdyn_kbattachment.md#BKMK_msdyn_kbattachment_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_kbattachment](msdyn_kbattachment.md) table/entity.

### <a name="BKMK_msdyn_kbattachment_DuplicateBaseRecord"></a> msdyn_kbattachment_DuplicateBaseRecord

**Added by**: Knowledge Management Features Solution

See the [msdyn_kbattachment_DuplicateBaseRecord](msdyn_kbattachment.md#BKMK_msdyn_kbattachment_DuplicateBaseRecord) one-to-many relationship for the [msdyn_kbattachment](msdyn_kbattachment.md) table/entity.

### <a name="BKMK_msdyn_knowledgearticletemplate_DuplicateMatchingRecord"></a> msdyn_knowledgearticletemplate_DuplicateMatchingRecord

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgearticletemplate_DuplicateMatchingRecord](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_knowledgearticletemplate](msdyn_knowledgearticletemplate.md) table/entity.

### <a name="BKMK_msdyn_knowledgearticletemplate_DuplicateBaseRecord"></a> msdyn_knowledgearticletemplate_DuplicateBaseRecord

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgearticletemplate_DuplicateBaseRecord](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_DuplicateBaseRecord) one-to-many relationship for the [msdyn_knowledgearticletemplate](msdyn_knowledgearticletemplate.md) table/entity.

### <a name="BKMK_msdyn_knowledgepersonalfilter_DuplicateMatchingRecord"></a> msdyn_knowledgepersonalfilter_DuplicateMatchingRecord

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgepersonalfilter_DuplicateMatchingRecord](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_knowledgepersonalfilter](msdyn_knowledgepersonalfilter.md) table/entity.

### <a name="BKMK_msdyn_knowledgepersonalfilter_DuplicateBaseRecord"></a> msdyn_knowledgepersonalfilter_DuplicateBaseRecord

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgepersonalfilter_DuplicateBaseRecord](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_DuplicateBaseRecord) one-to-many relationship for the [msdyn_knowledgepersonalfilter](msdyn_knowledgepersonalfilter.md) table/entity.

### <a name="BKMK_msdyn_knowledgesearchfilter_DuplicateMatchingRecord"></a> msdyn_knowledgesearchfilter_DuplicateMatchingRecord

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgesearchfilter_DuplicateMatchingRecord](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_knowledgesearchfilter](msdyn_knowledgesearchfilter.md) table/entity.

### <a name="BKMK_msdyn_knowledgesearchfilter_DuplicateBaseRecord"></a> msdyn_knowledgesearchfilter_DuplicateBaseRecord

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgesearchfilter_DuplicateBaseRecord](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_DuplicateBaseRecord) one-to-many relationship for the [msdyn_knowledgesearchfilter](msdyn_knowledgesearchfilter.md) table/entity.

### <a name="BKMK_keyvaultreference_DuplicateMatchingRecord"></a> keyvaultreference_DuplicateMatchingRecord

**Added by**: ManagedIdentityExtensions Solution

See the [keyvaultreference_DuplicateMatchingRecord](keyvaultreference.md#BKMK_keyvaultreference_DuplicateMatchingRecord) one-to-many relationship for the [keyvaultreference](keyvaultreference.md) table/entity.

### <a name="BKMK_keyvaultreference_DuplicateBaseRecord"></a> keyvaultreference_DuplicateBaseRecord

**Added by**: ManagedIdentityExtensions Solution

See the [keyvaultreference_DuplicateBaseRecord](keyvaultreference.md#BKMK_keyvaultreference_DuplicateBaseRecord) one-to-many relationship for the [keyvaultreference](keyvaultreference.md) table/entity.

### <a name="BKMK_managedidentity_DuplicateMatchingRecord"></a> managedidentity_DuplicateMatchingRecord

**Added by**: ManagedIdentityExtensions Solution

See the [managedidentity_DuplicateMatchingRecord](managedidentity.md#BKMK_managedidentity_DuplicateMatchingRecord) one-to-many relationship for the [managedidentity](managedidentity.md) table/entity.

### <a name="BKMK_managedidentity_DuplicateBaseRecord"></a> managedidentity_DuplicateBaseRecord

**Added by**: ManagedIdentityExtensions Solution

See the [managedidentity_DuplicateBaseRecord](managedidentity.md#BKMK_managedidentity_DuplicateBaseRecord) one-to-many relationship for the [managedidentity](managedidentity.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscription_DuplicateMatchingRecord"></a> organizationdatasyncsubscription_DuplicateMatchingRecord

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscription_DuplicateMatchingRecord](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_DuplicateMatchingRecord) one-to-many relationship for the [organizationdatasyncsubscription](organizationdatasyncsubscription.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscription_DuplicateBaseRecord"></a> organizationdatasyncsubscription_DuplicateBaseRecord

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscription_DuplicateBaseRecord](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_DuplicateBaseRecord) one-to-many relationship for the [organizationdatasyncsubscription](organizationdatasyncsubscription.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscriptionentity_DuplicateMatchingRecord"></a> organizationdatasyncsubscriptionentity_DuplicateMatchingRecord

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscriptionentity_DuplicateMatchingRecord](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_DuplicateMatchingRecord) one-to-many relationship for the [organizationdatasyncsubscriptionentity](organizationdatasyncsubscriptionentity.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscriptionentity_DuplicateBaseRecord"></a> organizationdatasyncsubscriptionentity_DuplicateBaseRecord

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscriptionentity_DuplicateBaseRecord](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_DuplicateBaseRecord) one-to-many relationship for the [organizationdatasyncsubscriptionentity](organizationdatasyncsubscriptionentity.md) table/entity.

### <a name="BKMK_organizationdatasyncstate_DuplicateMatchingRecord"></a> organizationdatasyncstate_DuplicateMatchingRecord

**Added by**: DataSyncState Solution

See the [organizationdatasyncstate_DuplicateMatchingRecord](organizationdatasyncstate.md#BKMK_organizationdatasyncstate_DuplicateMatchingRecord) one-to-many relationship for the [organizationdatasyncstate](organizationdatasyncstate.md) table/entity.

### <a name="BKMK_organizationdatasyncstate_DuplicateBaseRecord"></a> organizationdatasyncstate_DuplicateBaseRecord

**Added by**: DataSyncState Solution

See the [organizationdatasyncstate_DuplicateBaseRecord](organizationdatasyncstate.md#BKMK_organizationdatasyncstate_DuplicateBaseRecord) one-to-many relationship for the [organizationdatasyncstate](organizationdatasyncstate.md) table/entity.

### <a name="BKMK_userrating_DuplicateMatchingRecord"></a> userrating_DuplicateMatchingRecord

**Added by**: User Rating Solution

See the [userrating_DuplicateMatchingRecord](userrating.md#BKMK_userrating_DuplicateMatchingRecord) one-to-many relationship for the [userrating](userrating.md) table/entity.

### <a name="BKMK_userrating_DuplicateBaseRecord"></a> userrating_DuplicateBaseRecord

**Added by**: User Rating Solution

See the [userrating_DuplicateBaseRecord](userrating.md#BKMK_userrating_DuplicateBaseRecord) one-to-many relationship for the [userrating](userrating.md) table/entity.

### <a name="BKMK_msdyn_customcontrolextendedsettings_DuplicateMatchingRecord"></a> msdyn_customcontrolextendedsettings_DuplicateMatchingRecord

**Added by**: User Experiences Extended Settings Solution

See the [msdyn_customcontrolextendedsettings_DuplicateMatchingRecord](msdyn_customcontrolextendedsettings.md#BKMK_msdyn_customcontrolextendedsettings_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_customcontrolextendedsettings](msdyn_customcontrolextendedsettings.md) table/entity.

### <a name="BKMK_msdyn_customcontrolextendedsettings_DuplicateBaseRecord"></a> msdyn_customcontrolextendedsettings_DuplicateBaseRecord

**Added by**: User Experiences Extended Settings Solution

See the [msdyn_customcontrolextendedsettings_DuplicateBaseRecord](msdyn_customcontrolextendedsettings.md#BKMK_msdyn_customcontrolextendedsettings_DuplicateBaseRecord) one-to-many relationship for the [msdyn_customcontrolextendedsettings](msdyn_customcontrolextendedsettings.md) table/entity.

### <a name="BKMK_msdyn_pmanalysishistory_DuplicateMatchingRecord"></a> msdyn_pmanalysishistory_DuplicateMatchingRecord

**Added by**: Process Mining Solution

See the [msdyn_pmanalysishistory_DuplicateMatchingRecord](msdyn_pmanalysishistory.md#BKMK_msdyn_pmanalysishistory_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_pmanalysishistory](msdyn_pmanalysishistory.md) table/entity.

### <a name="BKMK_msdyn_pmanalysishistory_DuplicateBaseRecord"></a> msdyn_pmanalysishistory_DuplicateBaseRecord

**Added by**: Process Mining Solution

See the [msdyn_pmanalysishistory_DuplicateBaseRecord](msdyn_pmanalysishistory.md#BKMK_msdyn_pmanalysishistory_DuplicateBaseRecord) one-to-many relationship for the [msdyn_pmanalysishistory](msdyn_pmanalysishistory.md) table/entity.

### <a name="BKMK_msdyn_pminferredtask_DuplicateMatchingRecord"></a> msdyn_pminferredtask_DuplicateMatchingRecord

**Added by**: Process Mining Solution

See the [msdyn_pminferredtask_DuplicateMatchingRecord](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_pminferredtask](msdyn_pminferredtask.md) table/entity.

### <a name="BKMK_msdyn_pminferredtask_DuplicateBaseRecord"></a> msdyn_pminferredtask_DuplicateBaseRecord

**Added by**: Process Mining Solution

See the [msdyn_pminferredtask_DuplicateBaseRecord](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_DuplicateBaseRecord) one-to-many relationship for the [msdyn_pminferredtask](msdyn_pminferredtask.md) table/entity.

### <a name="BKMK_msdyn_pmrecording_DuplicateMatchingRecord"></a> msdyn_pmrecording_DuplicateMatchingRecord

**Added by**: Process Mining Solution

See the [msdyn_pmrecording_DuplicateMatchingRecord](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_pmrecording](msdyn_pmrecording.md) table/entity.

### <a name="BKMK_msdyn_pmrecording_DuplicateBaseRecord"></a> msdyn_pmrecording_DuplicateBaseRecord

**Added by**: Process Mining Solution

See the [msdyn_pmrecording_DuplicateBaseRecord](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_DuplicateBaseRecord) one-to-many relationship for the [msdyn_pmrecording](msdyn_pmrecording.md) table/entity.

### <a name="BKMK_msdyn_pmtemplate_DuplicateMatchingRecord"></a> msdyn_pmtemplate_DuplicateMatchingRecord

**Added by**: Process Mining Solution

See the [msdyn_pmtemplate_DuplicateMatchingRecord](msdyn_pmtemplate.md#BKMK_msdyn_pmtemplate_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_pmtemplate](msdyn_pmtemplate.md) table/entity.

### <a name="BKMK_msdyn_pmtemplate_DuplicateBaseRecord"></a> msdyn_pmtemplate_DuplicateBaseRecord

**Added by**: Process Mining Solution

See the [msdyn_pmtemplate_DuplicateBaseRecord](msdyn_pmtemplate.md#BKMK_msdyn_pmtemplate_DuplicateBaseRecord) one-to-many relationship for the [msdyn_pmtemplate](msdyn_pmtemplate.md) table/entity.

### <a name="BKMK_msdyn_analysiscomponent_DuplicateMatchingRecord"></a> msdyn_analysiscomponent_DuplicateMatchingRecord

**Added by**: Power Apps Checker Solution

See the [msdyn_analysiscomponent_DuplicateMatchingRecord](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_analysiscomponent](msdyn_analysiscomponent.md) table/entity.

### <a name="BKMK_msdyn_analysiscomponent_DuplicateBaseRecord"></a> msdyn_analysiscomponent_DuplicateBaseRecord

**Added by**: Power Apps Checker Solution

See the [msdyn_analysiscomponent_DuplicateBaseRecord](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_DuplicateBaseRecord) one-to-many relationship for the [msdyn_analysiscomponent](msdyn_analysiscomponent.md) table/entity.

### <a name="BKMK_msdyn_analysisjob_DuplicateMatchingRecord"></a> msdyn_analysisjob_DuplicateMatchingRecord

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisjob_DuplicateMatchingRecord](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_analysisjob](msdyn_analysisjob.md) table/entity.

### <a name="BKMK_msdyn_analysisjob_DuplicateBaseRecord"></a> msdyn_analysisjob_DuplicateBaseRecord

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisjob_DuplicateBaseRecord](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_DuplicateBaseRecord) one-to-many relationship for the [msdyn_analysisjob](msdyn_analysisjob.md) table/entity.

### <a name="BKMK_msdyn_analysisresult_DuplicateMatchingRecord"></a> msdyn_analysisresult_DuplicateMatchingRecord

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisresult_DuplicateMatchingRecord](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_analysisresult](msdyn_analysisresult.md) table/entity.

### <a name="BKMK_msdyn_analysisresult_DuplicateBaseRecord"></a> msdyn_analysisresult_DuplicateBaseRecord

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisresult_DuplicateBaseRecord](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_DuplicateBaseRecord) one-to-many relationship for the [msdyn_analysisresult](msdyn_analysisresult.md) table/entity.

### <a name="BKMK_msdyn_analysisresultdetail_DuplicateMatchingRecord"></a> msdyn_analysisresultdetail_DuplicateMatchingRecord

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisresultdetail_DuplicateMatchingRecord](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_analysisresultdetail](msdyn_analysisresultdetail.md) table/entity.

### <a name="BKMK_msdyn_analysisresultdetail_DuplicateBaseRecord"></a> msdyn_analysisresultdetail_DuplicateBaseRecord

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisresultdetail_DuplicateBaseRecord](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_DuplicateBaseRecord) one-to-many relationship for the [msdyn_analysisresultdetail](msdyn_analysisresultdetail.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthrule_DuplicateMatchingRecord"></a> msdyn_solutionhealthrule_DuplicateMatchingRecord

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthrule_DuplicateMatchingRecord](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_solutionhealthrule](msdyn_solutionhealthrule.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthrule_DuplicateBaseRecord"></a> msdyn_solutionhealthrule_DuplicateBaseRecord

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthrule_DuplicateBaseRecord](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_DuplicateBaseRecord) one-to-many relationship for the [msdyn_solutionhealthrule](msdyn_solutionhealthrule.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthruleargument_DuplicateMatchingRecord"></a> msdyn_solutionhealthruleargument_DuplicateMatchingRecord

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthruleargument_DuplicateMatchingRecord](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_solutionhealthruleargument](msdyn_solutionhealthruleargument.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthruleargument_DuplicateBaseRecord"></a> msdyn_solutionhealthruleargument_DuplicateBaseRecord

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthruleargument_DuplicateBaseRecord](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_DuplicateBaseRecord) one-to-many relationship for the [msdyn_solutionhealthruleargument](msdyn_solutionhealthruleargument.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthruleset_DuplicateMatchingRecord"></a> msdyn_solutionhealthruleset_DuplicateMatchingRecord

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthruleset_DuplicateMatchingRecord](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_DuplicateMatchingRecord) one-to-many relationship for the [msdyn_solutionhealthruleset](msdyn_solutionhealthruleset.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthruleset_DuplicateBaseRecord"></a> msdyn_solutionhealthruleset_DuplicateBaseRecord

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthruleset_DuplicateBaseRecord](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_DuplicateBaseRecord) one-to-many relationship for the [msdyn_solutionhealthruleset](msdyn_solutionhealthruleset.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.duplicaterecord?text=duplicaterecord EntityType" />