---
title: "BulkDeleteFailure table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the BulkDeleteFailure table/entity."
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

# BulkDeleteFailure table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Record that was not deleted during a bulk deletion job.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Retrieve|GET [*org URI*]/api/data/v9.0/bulkdeletefailures(*bulkdeletefailureid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/bulkdeletefailures<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|BulkDeleteFailures|
|DisplayCollectionName|Bulk Delete Failures|
|DisplayName|Bulk Delete Failure|
|EntitySetName|bulkdeletefailures|
|IsBPFEntity|False|
|LogicalCollectionName|bulkdeletefailures|
|LogicalName|bulkdeletefailure|
|OwnershipType|None|
|PrimaryIdAttribute|bulkdeletefailureid|
|PrimaryNameAttribute||
|SchemaName|BulkDeleteFailure|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.


### <a name="BKMK_RegardingObjectIdYomiName"></a> RegardingObjectIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|regardingobjectidyominame|
|MaxLength|800|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AsyncOperationId](#BKMK_AsyncOperationId)
- [BulkDeleteFailureId](#BKMK_BulkDeleteFailureId)
- [BulkDeleteOperationId](#BKMK_BulkDeleteOperationId)
- [ErrorDescription](#BKMK_ErrorDescription)
- [ErrorNumber](#BKMK_ErrorNumber)
- [OrderedQueryIndex](#BKMK_OrderedQueryIndex)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningUser](#BKMK_OwningUser)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)


### <a name="BKMK_AsyncOperationId"></a> AsyncOperationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the system job that created this record.|
|DisplayName|System Job|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|asyncoperationid|
|RequiredLevel|ApplicationRequired|
|Targets|asyncoperation|
|Type|Lookup|


### <a name="BKMK_BulkDeleteFailureId"></a> BulkDeleteFailureId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the bulk deletion failure record.|
|DisplayName|Bulk Deletion Failure|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|bulkdeletefailureid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_BulkDeleteOperationId"></a> BulkDeleteOperationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the bulk operation job which created this record|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|bulkdeleteoperationid|
|RequiredLevel|None|
|Targets|bulkdeleteoperation|
|Type|Lookup|


### <a name="BKMK_ErrorDescription"></a> ErrorDescription

|Property|Value|
|--------|-----|
|Description|Description of the error.|
|DisplayName|Error Description|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|errordescription|
|MaxLength|512|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ErrorNumber"></a> ErrorNumber

|Property|Value|
|--------|-----|
|Description|Error code for the failed bulk deletion.|
|DisplayName|Error Code|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|errornumber|
|MaxValue|1000000000|
|MinValue|-1000000000|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_OrderedQueryIndex"></a> OrderedQueryIndex

|Property|Value|
|--------|-----|
|Description|Index of the ordered query expression that retrieved this record.|
|DisplayName|Index|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|orderedqueryindex|
|MaxValue|1000000000|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user or team who owns the bulk operation log.|
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
|Description|Unique identifier of the business unit that owns the bulk deletion failure.|
|DisplayName|Owning Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who owns the bulk deletion failure record.
|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the record that can not be deleted.|
|DisplayName|Name|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|regardingobjectid|
|RequiredLevel|None|
|Targets|account,activityfileattachment,activitymimeattachment,activitypointer,annotation,annualfiscalcalendar,appelement,applicationuser,appmodulecomponentedge,appmodulecomponentnode,appnotification,appointment,appsetting,appusersetting,attributeimageconfig,attributemap,bot,botcomponent,businessunit,businessunitnewsarticle,calendar,canvasappextendedmetadata,cascadegrantrevokeaccessrecordstracker,cascadegrantrevokeaccessversiontracker,catalog,catalogassignment,channelaccessprofile,channelaccessprofilerule,connectionreference,connector,contact,conversationtranscript,customapi,customapirequestparameter,customapiresponseproperty,customeraddress,customerrelationship,datalakefolder,datalakefolderpermission,datalakeworkspace,datalakeworkspacepermission,displaystring,email,emailserverprofile,entityanalyticsconfig,entityimageconfig,entitymap,environmentvariabledefinition,environmentvariablevalue,exportsolutionupload,externalparty,externalpartyitem,fax,fixedmonthlyfiscalcalendar,flowmachine,flowmachinegroup,flowsession,holidaywrapper,import,importdata,importfile,importlog,importmap,internalcatalogassignment,isvconfig,kbarticle,kbarticlecomment,kbarticletemplate,keyvaultreference,knowledgearticle,knowledgebaserecord,letter,managedidentity,monthlyfiscalcalendar,msdynce_botcontent,msdyn_aibdataset,msdyn_aibdatasetfile,msdyn_aibdatasetrecord,msdyn_aibdatasetscontainer,msdyn_aibfile,msdyn_aibfileattacheddata,msdyn_aiconfiguration,msdyn_aifptrainingdocument,msdyn_aimodel,msdyn_aiodimage,msdyn_aiodlabel,msdyn_aiodtrainingboundingbox,msdyn_aiodtrainingimage,msdyn_aitemplate,msdyn_analysiscomponent,msdyn_analysisjob,msdyn_analysisresult,msdyn_analysisresultdetail,msdyn_dataflow,msdyn_federatedarticle,msdyn_federatedarticleincident,msdyn_helppage,msdyn_kalanguagesetting,msdyn_kmfederatedsearchconfig,msdyn_kmpersonalizationsetting,msdyn_knowledgearticleimage,msdyn_knowledgearticletemplate,msdyn_knowledgeinteractioninsight,msdyn_knowledgepersonalfilter,msdyn_knowledgesearchfilter,msdyn_knowledgesearchinsight,msdyn_pminferredtask,msdyn_pmrecording,msdyn_richtextfile,msdyn_serviceconfiguration,msdyn_slakpi,msdyn_solutionhealthrule,msdyn_solutionhealthruleargument,msdyn_solutionhealthruleset,organization,organizationdatasyncsubscription,organizationdatasyncsubscriptionentity,organizationsetting,package,pdfsetting,phonecall,post,privilege,processstageparameter,provisionlanguageforuser,quarterlyfiscalcalendar,queue,queueitem,recurringappointmentmaster,relationshipattribute,relationshiprole,relationshiprolemap,revokeinheritedaccessrecordstracker,role,routingrule,routingruleitem,savedquery,semiannualfiscalcalendar,serviceplan,settingdefinition,sla,socialactivity,solutioncomponentattributeconfiguration,solutioncomponentconfiguration,solutioncomponentrelationshipconfiguration,stagesolutionupload,subject,systemform,systemuser,systemuserauthorizationchangetracker,task,team,teammobileofflineprofilemembership,template,territory,theme,userform,usermapping,usermobileofflineprofilemembership,userquery,workflowbinary|
|Type|Lookup|


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjectidname|
|MaxLength|800|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjecttypecode|
|RequiredLevel|None|
|Type|EntityName|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [theme_BulkDeleteFailures](#BKMK_theme_BulkDeleteFailures)
- [usermapping_BulkDeleteFailures](#BKMK_usermapping_BulkDeleteFailures)
- [knowledgearticle_BulkDeleteFailures](#BKMK_knowledgearticle_BulkDeleteFailures)
- [post_BulkDeleteFailures](#BKMK_post_BulkDeleteFailures)
- [KnowledgeBaseRecord_BulkDeleteFailures](#BKMK_KnowledgeBaseRecord_BulkDeleteFailures)
- [Role_BulkDeleteFailures](#BKMK_Role_BulkDeleteFailures)
- [Subject_BulkDeleteFailures](#BKMK_Subject_BulkDeleteFailures)
- [Fax_BulkDeleteFailures](#BKMK_Fax_BulkDeleteFailures)
- [Privilege_BulkDeleteFailures](#BKMK_Privilege_BulkDeleteFailures)
- [KbArticle_BulkDeleteFailures](#BKMK_KbArticle_BulkDeleteFailures)
- [KbArticleComment_BulkDeleteFailures](#BKMK_KbArticleComment_BulkDeleteFailures)
- [AnnualFiscalCalendar_BulkDeleteFailures](#BKMK_AnnualFiscalCalendar_BulkDeleteFailures)
- [UserForm_BulkDeleteFailures](#BKMK_UserForm_BulkDeleteFailures)
- [Queue_BulkDeleteFailures](#BKMK_Queue_BulkDeleteFailures)
- [Contact_BulkDeleteFailures](#BKMK_Contact_BulkDeleteFailures)
- [emailserverprofile_bulkdeletefailures](#BKMK_emailserverprofile_bulkdeletefailures)
- [SavedQuery_BulkDeleteFailures](#BKMK_SavedQuery_BulkDeleteFailures)
- [Appointment_BulkDeleteFailures](#BKMK_Appointment_BulkDeleteFailures)
- [Template_BulkDeleteFailures](#BKMK_Template_BulkDeleteFailures)
- [Account_BulkDeleteFailures](#BKMK_Account_BulkDeleteFailures)
- [SystemUser_BulkDeleteFailures](#BKMK_SystemUser_BulkDeleteFailures)
- [QuarterlyFiscalCalendar_BulkDeleteFailures](#BKMK_QuarterlyFiscalCalendar_BulkDeleteFailures)
- [QueueItem_BulkDeleteFailures](#BKMK_QueueItem_BulkDeleteFailures)
- [DisplayString_BulkDeleteFailures](#BKMK_DisplayString_BulkDeleteFailures)
- [Calendar_BulkDeleteFailures](#BKMK_Calendar_BulkDeleteFailures)
- [Organization_BulkDeleteFailures](#BKMK_Organization_BulkDeleteFailures)
- [BusinessUnit_BulkDeleteFailures](#BKMK_BusinessUnit_BulkDeleteFailures)
- [Annotation_BulkDeleteFailures](#BKMK_Annotation_BulkDeleteFailures)
- [ImportLog_BulkDeleteFailures](#BKMK_ImportLog_BulkDeleteFailures)
- [Import_BulkDeleteFailures](#BKMK_Import_BulkDeleteFailures)
- [Letter_BulkDeleteFailures](#BKMK_Letter_BulkDeleteFailures)
- [UserQuery_BulkDeleteFailures](#BKMK_UserQuery_BulkDeleteFailures)
- [PhoneCall_BulkDeleteFailures](#BKMK_PhoneCall_BulkDeleteFailures)
- [Team_BulkDeleteFailures](#BKMK_Team_BulkDeleteFailures)
- [CustomerAddress_BulkDeleteFailures](#BKMK_CustomerAddress_BulkDeleteFailures)
- [SocialActivity_BulkDeleteFailures](#BKMK_SocialActivity_BulkDeleteFailures)
- [ImportFile_BulkDeleteFailures](#BKMK_ImportFile_BulkDeleteFailures)
- [SystemForm_BulkDeleteFailures](#BKMK_SystemForm_BulkDeleteFailures)
- [BusinessUnitNewsArticle_BulkDeleteFailures](#BKMK_BusinessUnitNewsArticle_BulkDeleteFailures)
- [ImportMap_BulkDeleteFailures](#BKMK_ImportMap_BulkDeleteFailures)
- [RecurringAppointmentMaster_BulkDeleteFailures](#BKMK_RecurringAppointmentMaster_BulkDeleteFailures)
- [Email_BulkDeleteFailures](#BKMK_Email_BulkDeleteFailures)
- [MonthlyFiscalCalendar_BulkDeleteFailures](#BKMK_MonthlyFiscalCalendar_BulkDeleteFailures)
- [KbArticleTemplate_BulkDeleteFailures](#BKMK_KbArticleTemplate_BulkDeleteFailures)
- [ActivityPointer_BulkDeleteFailures](#BKMK_ActivityPointer_BulkDeleteFailures)
- [slabase_BulkDeleteFailures](#BKMK_slabase_BulkDeleteFailures)
- [FixedMonthlyFiscalCalendar_BulkDeleteFailures](#BKMK_FixedMonthlyFiscalCalendar_BulkDeleteFailures)
- [Task_BulkDeleteFailures](#BKMK_Task_BulkDeleteFailures)
- [BulkDeleteOperation_BulkDeleteFailure](#BKMK_BulkDeleteOperation_BulkDeleteFailure)
- [ActivityMimeAttachment_BulkDeleteFailures](#BKMK_ActivityMimeAttachment_BulkDeleteFailures)
- [SemiAnnualFiscalCalendar_BulkDeleteFailures](#BKMK_SemiAnnualFiscalCalendar_BulkDeleteFailures)
- [solutioncomponentattributeconfiguration_BulkDeleteFailures](#BKMK_solutioncomponentattributeconfiguration_BulkDeleteFailures)
- [solutioncomponentconfiguration_BulkDeleteFailures](#BKMK_solutioncomponentconfiguration_BulkDeleteFailures)
- [solutioncomponentrelationshipconfiguration_BulkDeleteFailures](#BKMK_solutioncomponentrelationshipconfiguration_BulkDeleteFailures)
- [package_BulkDeleteFailures](#BKMK_package_BulkDeleteFailures)
- [stagesolutionupload_BulkDeleteFailures](#BKMK_stagesolutionupload_BulkDeleteFailures)
- [exportsolutionupload_BulkDeleteFailures](#BKMK_exportsolutionupload_BulkDeleteFailures)
- [attributeimageconfig_BulkDeleteFailures](#BKMK_attributeimageconfig_BulkDeleteFailures)
- [entityimageconfig_BulkDeleteFailures](#BKMK_entityimageconfig_BulkDeleteFailures)
- [relationshipattribute_BulkDeleteFailures](#BKMK_relationshipattribute_BulkDeleteFailures)
- [provisionlanguageforuser_BulkDeleteFailures](#BKMK_provisionlanguageforuser_BulkDeleteFailures)
- [entityanalyticsconfig_BulkDeleteFailures](#BKMK_entityanalyticsconfig_BulkDeleteFailures)
- [datalakefolder_BulkDeleteFailures](#BKMK_datalakefolder_BulkDeleteFailures)
- [datalakefolderpermission_BulkDeleteFailures](#BKMK_datalakefolderpermission_BulkDeleteFailures)
- [datalakeworkspace_BulkDeleteFailures](#BKMK_datalakeworkspace_BulkDeleteFailures)
- [datalakeworkspacepermission_BulkDeleteFailures](#BKMK_datalakeworkspacepermission_BulkDeleteFailures)
- [msdyn_dataflow_BulkDeleteFailures](#BKMK_msdyn_dataflow_BulkDeleteFailures)
- [serviceplan_BulkDeleteFailures](#BKMK_serviceplan_BulkDeleteFailures)
- [applicationuser_BulkDeleteFailures](#BKMK_applicationuser_BulkDeleteFailures)
- [connector_BulkDeleteFailures](#BKMK_connector_BulkDeleteFailures)
- [environmentvariabledefinition_BulkDeleteFailures](#BKMK_environmentvariabledefinition_BulkDeleteFailures)
- [environmentvariablevalue_BulkDeleteFailures](#BKMK_environmentvariablevalue_BulkDeleteFailures)
- [flowmachine_BulkDeleteFailures](#BKMK_flowmachine_BulkDeleteFailures)
- [flowmachinegroup_BulkDeleteFailures](#BKMK_flowmachinegroup_BulkDeleteFailures)
- [processstageparameter_BulkDeleteFailures](#BKMK_processstageparameter_BulkDeleteFailures)
- [flowsession_BulkDeleteFailures](#BKMK_flowsession_BulkDeleteFailures)
- [workflowbinary_BulkDeleteFailures](#BKMK_workflowbinary_BulkDeleteFailures)
- [connectionreference_BulkDeleteFailures](#BKMK_connectionreference_BulkDeleteFailures)
- [msdyn_helppage_BulkDeleteFailures](#BKMK_msdyn_helppage_BulkDeleteFailures)
- [msdynce_botcontent_BulkDeleteFailures](#BKMK_msdynce_botcontent_BulkDeleteFailures)
- [conversationtranscript_BulkDeleteFailures](#BKMK_conversationtranscript_BulkDeleteFailures)
- [bot_BulkDeleteFailures](#BKMK_bot_BulkDeleteFailures)
- [botcomponent_BulkDeleteFailures](#BKMK_botcomponent_BulkDeleteFailures)
- [Territory_BulkDeleteFailures](#BKMK_Territory_BulkDeleteFailures)
- [activityfileattachment_BulkDeleteFailures](#BKMK_activityfileattachment_BulkDeleteFailures)
- [msdyn_serviceconfiguration_BulkDeleteFailures](#BKMK_msdyn_serviceconfiguration_BulkDeleteFailures)
- [msdyn_slakpi_BulkDeleteFailures](#BKMK_msdyn_slakpi_BulkDeleteFailures)
- [msdyn_federatedarticle_BulkDeleteFailures](#BKMK_msdyn_federatedarticle_BulkDeleteFailures)
- [msdyn_federatedarticleincident_BulkDeleteFailures](#BKMK_msdyn_federatedarticleincident_BulkDeleteFailures)
- [msdyn_kmfederatedsearchconfig_BulkDeleteFailures](#BKMK_msdyn_kmfederatedsearchconfig_BulkDeleteFailures)
- [msdyn_knowledgearticleimage_BulkDeleteFailures](#BKMK_msdyn_knowledgearticleimage_BulkDeleteFailures)
- [msdyn_knowledgeinteractioninsight_BulkDeleteFailures](#BKMK_msdyn_knowledgeinteractioninsight_BulkDeleteFailures)
- [msdyn_knowledgesearchinsight_BulkDeleteFailures](#BKMK_msdyn_knowledgesearchinsight_BulkDeleteFailures)
- [msdyn_kalanguagesetting_BulkDeleteFailures](#BKMK_msdyn_kalanguagesetting_BulkDeleteFailures)
- [msdyn_kmpersonalizationsetting_BulkDeleteFailures](#BKMK_msdyn_kmpersonalizationsetting_BulkDeleteFailures)
- [msdyn_knowledgearticletemplate_BulkDeleteFailures](#BKMK_msdyn_knowledgearticletemplate_BulkDeleteFailures)
- [msdyn_knowledgepersonalfilter_BulkDeleteFailures](#BKMK_msdyn_knowledgepersonalfilter_BulkDeleteFailures)
- [msdyn_knowledgesearchfilter_BulkDeleteFailures](#BKMK_msdyn_knowledgesearchfilter_BulkDeleteFailures)
- [keyvaultreference_BulkDeleteFailures](#BKMK_keyvaultreference_BulkDeleteFailures)
- [managedidentity_BulkDeleteFailures](#BKMK_managedidentity_BulkDeleteFailures)
- [catalog_BulkDeleteFailures](#BKMK_catalog_BulkDeleteFailures)
- [catalogassignment_BulkDeleteFailures](#BKMK_catalogassignment_BulkDeleteFailures)
- [customapi_BulkDeleteFailures](#BKMK_customapi_BulkDeleteFailures)
- [customapirequestparameter_BulkDeleteFailures](#BKMK_customapirequestparameter_BulkDeleteFailures)
- [customapiresponseproperty_BulkDeleteFailures](#BKMK_customapiresponseproperty_BulkDeleteFailures)
- [organizationdatasyncsubscription_BulkDeleteFailures](#BKMK_organizationdatasyncsubscription_BulkDeleteFailures)
- [organizationdatasyncsubscriptionentity_BulkDeleteFailures](#BKMK_organizationdatasyncsubscriptionentity_BulkDeleteFailures)
- [appnotification_BulkDeleteFailures](#BKMK_appnotification_BulkDeleteFailures)
- [msdyn_richtextfile_BulkDeleteFailures](#BKMK_msdyn_richtextfile_BulkDeleteFailures)
- [msdyn_aiconfiguration_BulkDeleteFailures](#BKMK_msdyn_aiconfiguration_BulkDeleteFailures)
- [msdyn_aimodel_BulkDeleteFailures](#BKMK_msdyn_aimodel_BulkDeleteFailures)
- [msdyn_aitemplate_BulkDeleteFailures](#BKMK_msdyn_aitemplate_BulkDeleteFailures)
- [msdyn_aibdataset_BulkDeleteFailures](#BKMK_msdyn_aibdataset_BulkDeleteFailures)
- [msdyn_aibdatasetfile_BulkDeleteFailures](#BKMK_msdyn_aibdatasetfile_BulkDeleteFailures)
- [msdyn_aibdatasetrecord_BulkDeleteFailures](#BKMK_msdyn_aibdatasetrecord_BulkDeleteFailures)
- [msdyn_aibdatasetscontainer_BulkDeleteFailures](#BKMK_msdyn_aibdatasetscontainer_BulkDeleteFailures)
- [msdyn_aibfile_BulkDeleteFailures](#BKMK_msdyn_aibfile_BulkDeleteFailures)
- [msdyn_aibfileattacheddata_BulkDeleteFailures](#BKMK_msdyn_aibfileattacheddata_BulkDeleteFailures)
- [msdyn_aifptrainingdocument_BulkDeleteFailures](#BKMK_msdyn_aifptrainingdocument_BulkDeleteFailures)
- [msdyn_aiodimage_BulkDeleteFailures](#BKMK_msdyn_aiodimage_BulkDeleteFailures)
- [msdyn_aiodlabel_BulkDeleteFailures](#BKMK_msdyn_aiodlabel_BulkDeleteFailures)
- [msdyn_aiodtrainingboundingbox_BulkDeleteFailures](#BKMK_msdyn_aiodtrainingboundingbox_BulkDeleteFailures)
- [msdyn_aiodtrainingimage_BulkDeleteFailures](#BKMK_msdyn_aiodtrainingimage_BulkDeleteFailures)
- [msdyn_pminferredtask_BulkDeleteFailures](#BKMK_msdyn_pminferredtask_BulkDeleteFailures)
- [msdyn_pmrecording_BulkDeleteFailures](#BKMK_msdyn_pmrecording_BulkDeleteFailures)
- [msdyn_analysiscomponent_BulkDeleteFailures](#BKMK_msdyn_analysiscomponent_BulkDeleteFailures)
- [msdyn_analysisjob_BulkDeleteFailures](#BKMK_msdyn_analysisjob_BulkDeleteFailures)
- [msdyn_analysisresult_BulkDeleteFailures](#BKMK_msdyn_analysisresult_BulkDeleteFailures)
- [msdyn_analysisresultdetail_BulkDeleteFailures](#BKMK_msdyn_analysisresultdetail_BulkDeleteFailures)
- [msdyn_solutionhealthrule_BulkDeleteFailures](#BKMK_msdyn_solutionhealthrule_BulkDeleteFailures)
- [msdyn_solutionhealthruleargument_BulkDeleteFailures](#BKMK_msdyn_solutionhealthruleargument_BulkDeleteFailures)
- [msdyn_solutionhealthruleset_BulkDeleteFailures](#BKMK_msdyn_solutionhealthruleset_BulkDeleteFailures)


### <a name="BKMK_theme_BulkDeleteFailures"></a> theme_BulkDeleteFailures

See theme Table [theme_BulkDeleteFailures](theme.md#BKMK_theme_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_usermapping_BulkDeleteFailures"></a> usermapping_BulkDeleteFailures

See usermapping Table [usermapping_BulkDeleteFailures](usermapping.md#BKMK_usermapping_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_BulkDeleteFailures"></a> knowledgearticle_BulkDeleteFailures

See knowledgearticle Table [knowledgearticle_BulkDeleteFailures](knowledgearticle.md#BKMK_knowledgearticle_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_post_BulkDeleteFailures"></a> post_BulkDeleteFailures

See post Table [post_BulkDeleteFailures](post.md#BKMK_post_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_KnowledgeBaseRecord_BulkDeleteFailures"></a> KnowledgeBaseRecord_BulkDeleteFailures

See knowledgebaserecord Table [KnowledgeBaseRecord_BulkDeleteFailures](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_Role_BulkDeleteFailures"></a> Role_BulkDeleteFailures

See role Table [Role_BulkDeleteFailures](role.md#BKMK_Role_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_Subject_BulkDeleteFailures"></a> Subject_BulkDeleteFailures

See subject Table [Subject_BulkDeleteFailures](subject.md#BKMK_Subject_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_Fax_BulkDeleteFailures"></a> Fax_BulkDeleteFailures

See fax Table [Fax_BulkDeleteFailures](fax.md#BKMK_Fax_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_Privilege_BulkDeleteFailures"></a> Privilege_BulkDeleteFailures

See privilege Table [Privilege_BulkDeleteFailures](privilege.md#BKMK_Privilege_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_KbArticle_BulkDeleteFailures"></a> KbArticle_BulkDeleteFailures

See kbarticle Table [KbArticle_BulkDeleteFailures](kbarticle.md#BKMK_KbArticle_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_KbArticleComment_BulkDeleteFailures"></a> KbArticleComment_BulkDeleteFailures

See kbarticlecomment Table [KbArticleComment_BulkDeleteFailures](kbarticlecomment.md#BKMK_KbArticleComment_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_AnnualFiscalCalendar_BulkDeleteFailures"></a> AnnualFiscalCalendar_BulkDeleteFailures

See annualfiscalcalendar Table [AnnualFiscalCalendar_BulkDeleteFailures](annualfiscalcalendar.md#BKMK_AnnualFiscalCalendar_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_UserForm_BulkDeleteFailures"></a> UserForm_BulkDeleteFailures

See userform Table [UserForm_BulkDeleteFailures](userform.md#BKMK_UserForm_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_Queue_BulkDeleteFailures"></a> Queue_BulkDeleteFailures

See queue Table [Queue_BulkDeleteFailures](queue.md#BKMK_Queue_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_Contact_BulkDeleteFailures"></a> Contact_BulkDeleteFailures

See contact Table [Contact_BulkDeleteFailures](contact.md#BKMK_Contact_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_emailserverprofile_bulkdeletefailures"></a> emailserverprofile_bulkdeletefailures

See emailserverprofile Table [emailserverprofile_bulkdeletefailures](emailserverprofile.md#BKMK_emailserverprofile_bulkdeletefailures) One-To-Many relationship.

### <a name="BKMK_SavedQuery_BulkDeleteFailures"></a> SavedQuery_BulkDeleteFailures

See savedquery Table [SavedQuery_BulkDeleteFailures](savedquery.md#BKMK_SavedQuery_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_Appointment_BulkDeleteFailures"></a> Appointment_BulkDeleteFailures

See appointment Table [Appointment_BulkDeleteFailures](appointment.md#BKMK_Appointment_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_Template_BulkDeleteFailures"></a> Template_BulkDeleteFailures

See template Table [Template_BulkDeleteFailures](template.md#BKMK_Template_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_Account_BulkDeleteFailures"></a> Account_BulkDeleteFailures

See account Table [Account_BulkDeleteFailures](account.md#BKMK_Account_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_SystemUser_BulkDeleteFailures"></a> SystemUser_BulkDeleteFailures

See systemuser Table [SystemUser_BulkDeleteFailures](systemuser.md#BKMK_SystemUser_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_QuarterlyFiscalCalendar_BulkDeleteFailures"></a> QuarterlyFiscalCalendar_BulkDeleteFailures

See quarterlyfiscalcalendar Table [QuarterlyFiscalCalendar_BulkDeleteFailures](quarterlyfiscalcalendar.md#BKMK_QuarterlyFiscalCalendar_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_QueueItem_BulkDeleteFailures"></a> QueueItem_BulkDeleteFailures

See queueitem Table [QueueItem_BulkDeleteFailures](queueitem.md#BKMK_QueueItem_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_DisplayString_BulkDeleteFailures"></a> DisplayString_BulkDeleteFailures

See displaystring Table [DisplayString_BulkDeleteFailures](displaystring.md#BKMK_DisplayString_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_Calendar_BulkDeleteFailures"></a> Calendar_BulkDeleteFailures

See calendar Table [Calendar_BulkDeleteFailures](calendar.md#BKMK_Calendar_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_Organization_BulkDeleteFailures"></a> Organization_BulkDeleteFailures

See organization Table [Organization_BulkDeleteFailures](organization.md#BKMK_Organization_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_BusinessUnit_BulkDeleteFailures"></a> BusinessUnit_BulkDeleteFailures

See businessunit Table [BusinessUnit_BulkDeleteFailures](businessunit.md#BKMK_BusinessUnit_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_Annotation_BulkDeleteFailures"></a> Annotation_BulkDeleteFailures

See annotation Table [Annotation_BulkDeleteFailures](annotation.md#BKMK_Annotation_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_ImportLog_BulkDeleteFailures"></a> ImportLog_BulkDeleteFailures

See importlog Table [ImportLog_BulkDeleteFailures](importlog.md#BKMK_ImportLog_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_Import_BulkDeleteFailures"></a> Import_BulkDeleteFailures

See import Table [Import_BulkDeleteFailures](import.md#BKMK_Import_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_Letter_BulkDeleteFailures"></a> Letter_BulkDeleteFailures

See letter Table [Letter_BulkDeleteFailures](letter.md#BKMK_Letter_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_UserQuery_BulkDeleteFailures"></a> UserQuery_BulkDeleteFailures

See userquery Table [UserQuery_BulkDeleteFailures](userquery.md#BKMK_UserQuery_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_PhoneCall_BulkDeleteFailures"></a> PhoneCall_BulkDeleteFailures

See phonecall Table [PhoneCall_BulkDeleteFailures](phonecall.md#BKMK_PhoneCall_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_Team_BulkDeleteFailures"></a> Team_BulkDeleteFailures

See team Table [Team_BulkDeleteFailures](team.md#BKMK_Team_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_CustomerAddress_BulkDeleteFailures"></a> CustomerAddress_BulkDeleteFailures

See customeraddress Table [CustomerAddress_BulkDeleteFailures](customeraddress.md#BKMK_CustomerAddress_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_SocialActivity_BulkDeleteFailures"></a> SocialActivity_BulkDeleteFailures

See socialactivity Table [SocialActivity_BulkDeleteFailures](socialactivity.md#BKMK_SocialActivity_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_ImportFile_BulkDeleteFailures"></a> ImportFile_BulkDeleteFailures

See importfile Table [ImportFile_BulkDeleteFailures](importfile.md#BKMK_ImportFile_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_SystemForm_BulkDeleteFailures"></a> SystemForm_BulkDeleteFailures

See systemform Table [SystemForm_BulkDeleteFailures](systemform.md#BKMK_SystemForm_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_BusinessUnitNewsArticle_BulkDeleteFailures"></a> BusinessUnitNewsArticle_BulkDeleteFailures

See businessunitnewsarticle Table [BusinessUnitNewsArticle_BulkDeleteFailures](businessunitnewsarticle.md#BKMK_BusinessUnitNewsArticle_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_ImportMap_BulkDeleteFailures"></a> ImportMap_BulkDeleteFailures

See importmap Table [ImportMap_BulkDeleteFailures](importmap.md#BKMK_ImportMap_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_RecurringAppointmentMaster_BulkDeleteFailures"></a> RecurringAppointmentMaster_BulkDeleteFailures

See recurringappointmentmaster Table [RecurringAppointmentMaster_BulkDeleteFailures](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_Email_BulkDeleteFailures"></a> Email_BulkDeleteFailures

See email Table [Email_BulkDeleteFailures](email.md#BKMK_Email_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_MonthlyFiscalCalendar_BulkDeleteFailures"></a> MonthlyFiscalCalendar_BulkDeleteFailures

See monthlyfiscalcalendar Table [MonthlyFiscalCalendar_BulkDeleteFailures](monthlyfiscalcalendar.md#BKMK_MonthlyFiscalCalendar_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_KbArticleTemplate_BulkDeleteFailures"></a> KbArticleTemplate_BulkDeleteFailures

See kbarticletemplate Table [KbArticleTemplate_BulkDeleteFailures](kbarticletemplate.md#BKMK_KbArticleTemplate_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_ActivityPointer_BulkDeleteFailures"></a> ActivityPointer_BulkDeleteFailures

See activitypointer Table [ActivityPointer_BulkDeleteFailures](activitypointer.md#BKMK_ActivityPointer_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_slabase_BulkDeleteFailures"></a> slabase_BulkDeleteFailures

See sla Table [slabase_BulkDeleteFailures](sla.md#BKMK_slabase_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_FixedMonthlyFiscalCalendar_BulkDeleteFailures"></a> FixedMonthlyFiscalCalendar_BulkDeleteFailures

See fixedmonthlyfiscalcalendar Table [FixedMonthlyFiscalCalendar_BulkDeleteFailures](fixedmonthlyfiscalcalendar.md#BKMK_FixedMonthlyFiscalCalendar_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_Task_BulkDeleteFailures"></a> Task_BulkDeleteFailures

See task Table [Task_BulkDeleteFailures](task.md#BKMK_Task_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_BulkDeleteOperation_BulkDeleteFailure"></a> BulkDeleteOperation_BulkDeleteFailure

See bulkdeleteoperation Table [BulkDeleteOperation_BulkDeleteFailure](bulkdeleteoperation.md#BKMK_BulkDeleteOperation_BulkDeleteFailure) One-To-Many relationship.

### <a name="BKMK_ActivityMimeAttachment_BulkDeleteFailures"></a> ActivityMimeAttachment_BulkDeleteFailures

See activitymimeattachment Table [ActivityMimeAttachment_BulkDeleteFailures](activitymimeattachment.md#BKMK_ActivityMimeAttachment_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_SemiAnnualFiscalCalendar_BulkDeleteFailures"></a> SemiAnnualFiscalCalendar_BulkDeleteFailures

See semiannualfiscalcalendar Table [SemiAnnualFiscalCalendar_BulkDeleteFailures](semiannualfiscalcalendar.md#BKMK_SemiAnnualFiscalCalendar_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_solutioncomponentattributeconfiguration_BulkDeleteFailures"></a> solutioncomponentattributeconfiguration_BulkDeleteFailures

**Added by**: Solution Component Configuration Solution

See solutioncomponentattributeconfiguration Table [solutioncomponentattributeconfiguration_BulkDeleteFailures](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_solutioncomponentconfiguration_BulkDeleteFailures"></a> solutioncomponentconfiguration_BulkDeleteFailures

**Added by**: Solution Component Configuration Solution

See solutioncomponentconfiguration Table [solutioncomponentconfiguration_BulkDeleteFailures](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_solutioncomponentrelationshipconfiguration_BulkDeleteFailures"></a> solutioncomponentrelationshipconfiguration_BulkDeleteFailures

**Added by**: Solution Component Configuration Solution

See solutioncomponentrelationshipconfiguration Table [solutioncomponentrelationshipconfiguration_BulkDeleteFailures](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_package_BulkDeleteFailures"></a> package_BulkDeleteFailures

**Added by**: msdyn_SolutionPackageMapping Solution

See package Table [package_BulkDeleteFailures](package.md#BKMK_package_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_stagesolutionupload_BulkDeleteFailures"></a> stagesolutionupload_BulkDeleteFailures

**Added by**: StageSolutionUpload Solution

See stagesolutionupload Table [stagesolutionupload_BulkDeleteFailures](stagesolutionupload.md#BKMK_stagesolutionupload_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_exportsolutionupload_BulkDeleteFailures"></a> exportsolutionupload_BulkDeleteFailures

**Added by**: ExportSolutionUpload Solution

See exportsolutionupload Table [exportsolutionupload_BulkDeleteFailures](exportsolutionupload.md#BKMK_exportsolutionupload_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_attributeimageconfig_BulkDeleteFailures"></a> attributeimageconfig_BulkDeleteFailures

**Added by**: Image Configuration Solution

See attributeimageconfig Table [attributeimageconfig_BulkDeleteFailures](attributeimageconfig.md#BKMK_attributeimageconfig_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_entityimageconfig_BulkDeleteFailures"></a> entityimageconfig_BulkDeleteFailures

**Added by**: Image Configuration Solution

See entityimageconfig Table [entityimageconfig_BulkDeleteFailures](entityimageconfig.md#BKMK_entityimageconfig_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_relationshipattribute_BulkDeleteFailures"></a> relationshipattribute_BulkDeleteFailures

**Added by**: Metadata Extension Solution

See relationshipattribute Table [relationshipattribute_BulkDeleteFailures](relationshipattribute.md#BKMK_relationshipattribute_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_provisionlanguageforuser_BulkDeleteFailures"></a> provisionlanguageforuser_BulkDeleteFailures

**Added by**: msft_LocalizationExtension Solution

See provisionlanguageforuser Table [provisionlanguageforuser_BulkDeleteFailures](provisionlanguageforuser.md#BKMK_provisionlanguageforuser_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_entityanalyticsconfig_BulkDeleteFailures"></a> entityanalyticsconfig_BulkDeleteFailures

**Added by**: Advanced Analytics Infrastructure Solution

See entityanalyticsconfig Table [entityanalyticsconfig_BulkDeleteFailures](entityanalyticsconfig.md#BKMK_entityanalyticsconfig_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_datalakefolder_BulkDeleteFailures"></a> datalakefolder_BulkDeleteFailures

**Added by**: Data lake workspaces Solution

See datalakefolder Table [datalakefolder_BulkDeleteFailures](datalakefolder.md#BKMK_datalakefolder_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_datalakefolderpermission_BulkDeleteFailures"></a> datalakefolderpermission_BulkDeleteFailures

**Added by**: Data lake workspaces Solution

See datalakefolderpermission Table [datalakefolderpermission_BulkDeleteFailures](datalakefolderpermission.md#BKMK_datalakefolderpermission_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_datalakeworkspace_BulkDeleteFailures"></a> datalakeworkspace_BulkDeleteFailures

**Added by**: Data lake workspaces Solution

See datalakeworkspace Table [datalakeworkspace_BulkDeleteFailures](datalakeworkspace.md#BKMK_datalakeworkspace_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_datalakeworkspacepermission_BulkDeleteFailures"></a> datalakeworkspacepermission_BulkDeleteFailures

**Added by**: Data lake workspaces Solution

See datalakeworkspacepermission Table [datalakeworkspacepermission_BulkDeleteFailures](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_dataflow_BulkDeleteFailures"></a> msdyn_dataflow_BulkDeleteFailures

**Added by**: Dataflow Solution Solution

See msdyn_dataflow Table [msdyn_dataflow_BulkDeleteFailures](msdyn_dataflow.md#BKMK_msdyn_dataflow_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_serviceplan_BulkDeleteFailures"></a> serviceplan_BulkDeleteFailures

**Added by**: License Enforcement Solution

See serviceplan Table [serviceplan_BulkDeleteFailures](serviceplan.md#BKMK_serviceplan_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_applicationuser_BulkDeleteFailures"></a> applicationuser_BulkDeleteFailures

**Added by**: ApplicationUserSolution Solution

See applicationuser Table [applicationuser_BulkDeleteFailures](applicationuser.md#BKMK_applicationuser_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_connector_BulkDeleteFailures"></a> connector_BulkDeleteFailures

**Added by**: Power Connector Solution Solution

See connector Table [connector_BulkDeleteFailures](connector.md#BKMK_connector_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_environmentvariabledefinition_BulkDeleteFailures"></a> environmentvariabledefinition_BulkDeleteFailures

**Added by**: Environment Variables Solution

See environmentvariabledefinition Table [environmentvariabledefinition_BulkDeleteFailures](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_environmentvariablevalue_BulkDeleteFailures"></a> environmentvariablevalue_BulkDeleteFailures

**Added by**: Environment Variables Solution

See environmentvariablevalue Table [environmentvariablevalue_BulkDeleteFailures](environmentvariablevalue.md#BKMK_environmentvariablevalue_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_flowmachine_BulkDeleteFailures"></a> flowmachine_BulkDeleteFailures

**Added by**: Power Automate Extensions core package Solution

See flowmachine Table [flowmachine_BulkDeleteFailures](flowmachine.md#BKMK_flowmachine_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_flowmachinegroup_BulkDeleteFailures"></a> flowmachinegroup_BulkDeleteFailures

**Added by**: Power Automate Extensions core package Solution

See flowmachinegroup Table [flowmachinegroup_BulkDeleteFailures](flowmachinegroup.md#BKMK_flowmachinegroup_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_processstageparameter_BulkDeleteFailures"></a> processstageparameter_BulkDeleteFailures

**Added by**: Power Automate Extensions core package Solution

See processstageparameter Table [processstageparameter_BulkDeleteFailures](processstageparameter.md#BKMK_processstageparameter_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_flowsession_BulkDeleteFailures"></a> flowsession_BulkDeleteFailures

**Added by**: Power Automate Extensions core package Solution

See flowsession Table [flowsession_BulkDeleteFailures](flowsession.md#BKMK_flowsession_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_workflowbinary_BulkDeleteFailures"></a> workflowbinary_BulkDeleteFailures

**Added by**: Power Automate Extensions core package Solution

See workflowbinary Table [workflowbinary_BulkDeleteFailures](workflowbinary.md#BKMK_workflowbinary_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_connectionreference_BulkDeleteFailures"></a> connectionreference_BulkDeleteFailures

**Added by**: Power Platform Connection References Solution

See connectionreference Table [connectionreference_BulkDeleteFailures](connectionreference.md#BKMK_connectionreference_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_helppage_BulkDeleteFailures"></a> msdyn_helppage_BulkDeleteFailures

**Added by**: Contextual Help Solution

See msdyn_helppage Table [msdyn_helppage_BulkDeleteFailures](msdyn_helppage.md#BKMK_msdyn_helppage_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdynce_botcontent_BulkDeleteFailures"></a> msdynce_botcontent_BulkDeleteFailures

**Added by**: Customer Care Intelligence Bots Solution

See msdynce_botcontent Table [msdynce_botcontent_BulkDeleteFailures](msdynce_botcontent.md#BKMK_msdynce_botcontent_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_conversationtranscript_BulkDeleteFailures"></a> conversationtranscript_BulkDeleteFailures

**Added by**: Power Virtual Agents Common Solution

See conversationtranscript Table [conversationtranscript_BulkDeleteFailures](conversationtranscript.md#BKMK_conversationtranscript_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_bot_BulkDeleteFailures"></a> bot_BulkDeleteFailures

**Added by**: Power Virtual Agents Solution

See bot Table [bot_BulkDeleteFailures](bot.md#BKMK_bot_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_botcomponent_BulkDeleteFailures"></a> botcomponent_BulkDeleteFailures

**Added by**: Power Virtual Agents Solution

See botcomponent Table [botcomponent_BulkDeleteFailures](botcomponent.md#BKMK_botcomponent_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_Territory_BulkDeleteFailures"></a> Territory_BulkDeleteFailures

**Added by**: Application Common Solution

See territory Table [Territory_BulkDeleteFailures](territory.md#BKMK_Territory_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_activityfileattachment_BulkDeleteFailures"></a> activityfileattachment_BulkDeleteFailures

**Added by**: Activities Patch Solution

See activityfileattachment Table [activityfileattachment_BulkDeleteFailures](activityfileattachment.md#BKMK_activityfileattachment_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_serviceconfiguration_BulkDeleteFailures"></a> msdyn_serviceconfiguration_BulkDeleteFailures

**Added by**: Service Level Agreement (SLA) Extension Solution

See msdyn_serviceconfiguration Table [msdyn_serviceconfiguration_BulkDeleteFailures](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_slakpi_BulkDeleteFailures"></a> msdyn_slakpi_BulkDeleteFailures

**Added by**: Service Level Agreement (SLA) Extension Solution

See msdyn_slakpi Table [msdyn_slakpi_BulkDeleteFailures](msdyn_slakpi.md#BKMK_msdyn_slakpi_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_federatedarticle_BulkDeleteFailures"></a> msdyn_federatedarticle_BulkDeleteFailures

**Added by**: Knowledge Management Online Features Solution

See msdyn_federatedarticle Table [msdyn_federatedarticle_BulkDeleteFailures](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_federatedarticleincident_BulkDeleteFailures"></a> msdyn_federatedarticleincident_BulkDeleteFailures

**Added by**: Knowledge Management Online Features Solution

See msdyn_federatedarticleincident Table [msdyn_federatedarticleincident_BulkDeleteFailures](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_kmfederatedsearchconfig_BulkDeleteFailures"></a> msdyn_kmfederatedsearchconfig_BulkDeleteFailures

**Added by**: Knowledge Management Online Features Solution

See msdyn_kmfederatedsearchconfig Table [msdyn_kmfederatedsearchconfig_BulkDeleteFailures](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgearticleimage_BulkDeleteFailures"></a> msdyn_knowledgearticleimage_BulkDeleteFailures

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgearticleimage Table [msdyn_knowledgearticleimage_BulkDeleteFailures](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgeinteractioninsight_BulkDeleteFailures"></a> msdyn_knowledgeinteractioninsight_BulkDeleteFailures

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgeinteractioninsight Table [msdyn_knowledgeinteractioninsight_BulkDeleteFailures](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgesearchinsight_BulkDeleteFailures"></a> msdyn_knowledgesearchinsight_BulkDeleteFailures

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgesearchinsight Table [msdyn_knowledgesearchinsight_BulkDeleteFailures](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_kalanguagesetting_BulkDeleteFailures"></a> msdyn_kalanguagesetting_BulkDeleteFailures

**Added by**: Knowledge Management Features Solution

See msdyn_kalanguagesetting Table [msdyn_kalanguagesetting_BulkDeleteFailures](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_kmpersonalizationsetting_BulkDeleteFailures"></a> msdyn_kmpersonalizationsetting_BulkDeleteFailures

**Added by**: Knowledge Management Features Solution

See msdyn_kmpersonalizationsetting Table [msdyn_kmpersonalizationsetting_BulkDeleteFailures](msdyn_kmpersonalizationsetting.md#BKMK_msdyn_kmpersonalizationsetting_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgearticletemplate_BulkDeleteFailures"></a> msdyn_knowledgearticletemplate_BulkDeleteFailures

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgearticletemplate Table [msdyn_knowledgearticletemplate_BulkDeleteFailures](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgepersonalfilter_BulkDeleteFailures"></a> msdyn_knowledgepersonalfilter_BulkDeleteFailures

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgepersonalfilter Table [msdyn_knowledgepersonalfilter_BulkDeleteFailures](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgesearchfilter_BulkDeleteFailures"></a> msdyn_knowledgesearchfilter_BulkDeleteFailures

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgesearchfilter Table [msdyn_knowledgesearchfilter_BulkDeleteFailures](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_keyvaultreference_BulkDeleteFailures"></a> keyvaultreference_BulkDeleteFailures

**Added by**: ManagedIdentityExtensions Solution

See keyvaultreference Table [keyvaultreference_BulkDeleteFailures](keyvaultreference.md#BKMK_keyvaultreference_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_managedidentity_BulkDeleteFailures"></a> managedidentity_BulkDeleteFailures

**Added by**: ManagedIdentityExtensions Solution

See managedidentity Table [managedidentity_BulkDeleteFailures](managedidentity.md#BKMK_managedidentity_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_catalog_BulkDeleteFailures"></a> catalog_BulkDeleteFailures

**Added by**: CatalogFramework Solution

See catalog Table [catalog_BulkDeleteFailures](catalog.md#BKMK_catalog_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_catalogassignment_BulkDeleteFailures"></a> catalogassignment_BulkDeleteFailures

**Added by**: CatalogFramework Solution

See catalogassignment Table [catalogassignment_BulkDeleteFailures](catalogassignment.md#BKMK_catalogassignment_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_customapi_BulkDeleteFailures"></a> customapi_BulkDeleteFailures

**Added by**: Custom API Framework Solution

See customapi Table [customapi_BulkDeleteFailures](customapi.md#BKMK_customapi_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_customapirequestparameter_BulkDeleteFailures"></a> customapirequestparameter_BulkDeleteFailures

**Added by**: Custom API Framework Solution

See customapirequestparameter Table [customapirequestparameter_BulkDeleteFailures](customapirequestparameter.md#BKMK_customapirequestparameter_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_customapiresponseproperty_BulkDeleteFailures"></a> customapiresponseproperty_BulkDeleteFailures

**Added by**: Custom API Framework Solution

See customapiresponseproperty Table [customapiresponseproperty_BulkDeleteFailures](customapiresponseproperty.md#BKMK_customapiresponseproperty_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_organizationdatasyncsubscription_BulkDeleteFailures"></a> organizationdatasyncsubscription_BulkDeleteFailures

**Added by**: OrganizationDataSyncSolution Solution

See organizationdatasyncsubscription Table [organizationdatasyncsubscription_BulkDeleteFailures](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_organizationdatasyncsubscriptionentity_BulkDeleteFailures"></a> organizationdatasyncsubscriptionentity_BulkDeleteFailures

**Added by**: OrganizationDataSyncSolution Solution

See organizationdatasyncsubscriptionentity Table [organizationdatasyncsubscriptionentity_BulkDeleteFailures](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_appnotification_BulkDeleteFailures"></a> appnotification_BulkDeleteFailures

**Added by**: AppNotifications Solution

See appnotification Table [appnotification_BulkDeleteFailures](appnotification.md#BKMK_appnotification_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_richtextfile_BulkDeleteFailures"></a> msdyn_richtextfile_BulkDeleteFailures

**Added by**: Rich Text Editor Solution

See msdyn_richtextfile Table [msdyn_richtextfile_BulkDeleteFailures](msdyn_richtextfile.md#BKMK_msdyn_richtextfile_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_aiconfiguration_BulkDeleteFailures"></a> msdyn_aiconfiguration_BulkDeleteFailures

**Added by**: AISolution Solution

See msdyn_aiconfiguration Table [msdyn_aiconfiguration_BulkDeleteFailures](msdyn_aiconfiguration.md#BKMK_msdyn_aiconfiguration_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_aimodel_BulkDeleteFailures"></a> msdyn_aimodel_BulkDeleteFailures

**Added by**: AISolution Solution

See msdyn_aimodel Table [msdyn_aimodel_BulkDeleteFailures](msdyn_aimodel.md#BKMK_msdyn_aimodel_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_aitemplate_BulkDeleteFailures"></a> msdyn_aitemplate_BulkDeleteFailures

**Added by**: AISolution Solution

See msdyn_aitemplate Table [msdyn_aitemplate_BulkDeleteFailures](msdyn_aitemplate.md#BKMK_msdyn_aitemplate_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdataset_BulkDeleteFailures"></a> msdyn_aibdataset_BulkDeleteFailures

**Added by**: AI Solution default templates Solution

See msdyn_aibdataset Table [msdyn_aibdataset_BulkDeleteFailures](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdatasetfile_BulkDeleteFailures"></a> msdyn_aibdatasetfile_BulkDeleteFailures

**Added by**: AI Solution default templates Solution

See msdyn_aibdatasetfile Table [msdyn_aibdatasetfile_BulkDeleteFailures](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdatasetrecord_BulkDeleteFailures"></a> msdyn_aibdatasetrecord_BulkDeleteFailures

**Added by**: AI Solution default templates Solution

See msdyn_aibdatasetrecord Table [msdyn_aibdatasetrecord_BulkDeleteFailures](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdatasetscontainer_BulkDeleteFailures"></a> msdyn_aibdatasetscontainer_BulkDeleteFailures

**Added by**: AI Solution default templates Solution

See msdyn_aibdatasetscontainer Table [msdyn_aibdatasetscontainer_BulkDeleteFailures](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_aibfile_BulkDeleteFailures"></a> msdyn_aibfile_BulkDeleteFailures

**Added by**: AI Solution default templates Solution

See msdyn_aibfile Table [msdyn_aibfile_BulkDeleteFailures](msdyn_aibfile.md#BKMK_msdyn_aibfile_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_aibfileattacheddata_BulkDeleteFailures"></a> msdyn_aibfileattacheddata_BulkDeleteFailures

**Added by**: AI Solution default templates Solution

See msdyn_aibfileattacheddata Table [msdyn_aibfileattacheddata_BulkDeleteFailures](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_aifptrainingdocument_BulkDeleteFailures"></a> msdyn_aifptrainingdocument_BulkDeleteFailures

**Added by**: AI Solution default templates Solution

See msdyn_aifptrainingdocument Table [msdyn_aifptrainingdocument_BulkDeleteFailures](msdyn_aifptrainingdocument.md#BKMK_msdyn_aifptrainingdocument_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodimage_BulkDeleteFailures"></a> msdyn_aiodimage_BulkDeleteFailures

**Added by**: AI Solution default templates Solution

See msdyn_aiodimage Table [msdyn_aiodimage_BulkDeleteFailures](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodlabel_BulkDeleteFailures"></a> msdyn_aiodlabel_BulkDeleteFailures

**Added by**: AI Solution default templates Solution

See msdyn_aiodlabel Table [msdyn_aiodlabel_BulkDeleteFailures](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodtrainingboundingbox_BulkDeleteFailures"></a> msdyn_aiodtrainingboundingbox_BulkDeleteFailures

**Added by**: AI Solution default templates Solution

See msdyn_aiodtrainingboundingbox Table [msdyn_aiodtrainingboundingbox_BulkDeleteFailures](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodtrainingimage_BulkDeleteFailures"></a> msdyn_aiodtrainingimage_BulkDeleteFailures

**Added by**: AI Solution default templates Solution

See msdyn_aiodtrainingimage Table [msdyn_aiodtrainingimage_BulkDeleteFailures](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_pminferredtask_BulkDeleteFailures"></a> msdyn_pminferredtask_BulkDeleteFailures

**Added by**: Process Mining Solution

See msdyn_pminferredtask Table [msdyn_pminferredtask_BulkDeleteFailures](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_pmrecording_BulkDeleteFailures"></a> msdyn_pmrecording_BulkDeleteFailures

**Added by**: Process Mining Solution

See msdyn_pmrecording Table [msdyn_pmrecording_BulkDeleteFailures](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_analysiscomponent_BulkDeleteFailures"></a> msdyn_analysiscomponent_BulkDeleteFailures

**Added by**: Power Apps Checker Solution

See msdyn_analysiscomponent Table [msdyn_analysiscomponent_BulkDeleteFailures](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisjob_BulkDeleteFailures"></a> msdyn_analysisjob_BulkDeleteFailures

**Added by**: Power Apps Checker Solution

See msdyn_analysisjob Table [msdyn_analysisjob_BulkDeleteFailures](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisresult_BulkDeleteFailures"></a> msdyn_analysisresult_BulkDeleteFailures

**Added by**: Power Apps Checker Solution

See msdyn_analysisresult Table [msdyn_analysisresult_BulkDeleteFailures](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisresultdetail_BulkDeleteFailures"></a> msdyn_analysisresultdetail_BulkDeleteFailures

**Added by**: Power Apps Checker Solution

See msdyn_analysisresultdetail Table [msdyn_analysisresultdetail_BulkDeleteFailures](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthrule_BulkDeleteFailures"></a> msdyn_solutionhealthrule_BulkDeleteFailures

**Added by**: Power Apps Checker Solution

See msdyn_solutionhealthrule Table [msdyn_solutionhealthrule_BulkDeleteFailures](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthruleargument_BulkDeleteFailures"></a> msdyn_solutionhealthruleargument_BulkDeleteFailures

**Added by**: Power Apps Checker Solution

See msdyn_solutionhealthruleargument Table [msdyn_solutionhealthruleargument_BulkDeleteFailures](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_BulkDeleteFailures) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthruleset_BulkDeleteFailures"></a> msdyn_solutionhealthruleset_BulkDeleteFailures

**Added by**: Power Apps Checker Solution

See msdyn_solutionhealthruleset Table [msdyn_solutionhealthruleset_BulkDeleteFailures](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_BulkDeleteFailures) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.bulkdeletefailure?text=bulkdeletefailure EntityType" />