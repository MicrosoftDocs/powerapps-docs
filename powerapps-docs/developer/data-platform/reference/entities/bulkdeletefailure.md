---
title: "BulkDeleteFailure table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the BulkDeleteFailure table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# BulkDeleteFailure table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Record that was not deleted during a bulk deletion job.


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Retrieve|GET /bulkdeletefailures(*bulkdeletefailureid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /bulkdeletefailures<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

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
|MaxLength|850|
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
|Targets|account,activityfileattachment,activitymimeattachment,activitypointer,annotation,annualfiscalcalendar,appaction,appactionmigration,appactionrule,appelement,applicationuser,appmodulecomponentedge,appmodulecomponentnode,appointment,appsetting,appusersetting,archivecleanupinfo,archivecleanupoperation,attributeimageconfig,attributemap,bot,botcomponent,bulkarchiveconfig,bulkarchivefailuredetail,bulkarchiveoperation,bulkarchiveoperationdetail,businessunit,businessunitnewsarticle,calendar,canvasappextendedmetadata,card,cascadegrantrevokeaccessrecordstracker,cascadegrantrevokeaccessversiontracker,catalog,catalogassignment,channelaccessprofile,channelaccessprofilerule,chat,comment,connectioninstance,connectionreference,connector,contact,conversationtranscript,customapi,customapirequestparameter,customapiresponseproperty,customeraddress,customerrelationship,datalakefolder,datalakefolderpermission,datalakeworkspace,datalakeworkspacepermission,dataprocessingconfiguration,delegatedauthorization,desktopflowbinary,desktopflowmodule,displaystring,email,emailserverprofile,enablearchivalrequest,entityanalyticsconfig,entityimageconfig,entityindex,entitymap,entityrecordfilter,environmentvariabledefinition,environmentvariablevalue,exportedexcel,exportsolutionupload,externalparty,externalpartyitem,fax,featurecontrolsetting,fixedmonthlyfiscalcalendar,flowmachine,flowmachinegroup,flowmachineimage,flowmachineimageversion,flowmachinenetwork,flowsession,fxexpression,holidaywrapper,import,importdata,importfile,importlog,importmap,indexattributes,internalcatalogassignment,isvconfig,kbarticle,kbarticlecomment,kbarticletemplate,keyvaultreference,knowledgearticle,knowledgebaserecord,letter,managedidentity,metadataforarchival,mobileofflineprofileextension,monthlyfiscalcalendar,msdynce_botcontent,msdyn_aibdataset,msdyn_aibdatasetfile,msdyn_aibdatasetrecord,msdyn_aibdatasetscontainer,msdyn_aibfeedbackloop,msdyn_aibfile,msdyn_aibfileattacheddata,msdyn_aiconfiguration,msdyn_aievent,msdyn_aifptrainingdocument,msdyn_aimodel,msdyn_aiodimage,msdyn_aiodlabel,msdyn_aiodtrainingboundingbox,msdyn_aiodtrainingimage,msdyn_aitemplate,msdyn_analysiscomponent,msdyn_analysisjob,msdyn_analysisoverride,msdyn_analysisresult,msdyn_analysisresultdetail,msdyn_appinsightsmetadata,msdyn_customcontrolextendedsettings,msdyn_dataflow,msdyn_dataflowrefreshhistory,msdyn_dataflowtemplate,msdyn_dataflow_datalakefolder,msdyn_dmsrequest,msdyn_dmsrequeststatus,msdyn_entitylinkchatconfiguration,msdyn_entityrefreshhistory,msdyn_favoriteknowledgearticle,msdyn_federatedarticle,msdyn_federatedarticleincident,msdyn_fileupload,msdyn_helppage,msdyn_insightsstorevirtualentity,msdyn_integratedsearchprovider,msdyn_kalanguagesetting,msdyn_kbattachment,msdyn_kmfederatedsearchconfig,msdyn_kmpersonalizationsetting,msdyn_knowledgearticleimage,msdyn_knowledgearticletemplate,msdyn_knowledgeconfiguration,msdyn_knowledgeinteractioninsight,msdyn_knowledgemanagementsetting,msdyn_knowledgepersonalfilter,msdyn_knowledgesearchfilter,msdyn_knowledgesearchinsight,msdyn_mobileapp,msdyn_pmanalysishistory,msdyn_pmcalendar,msdyn_pmcalendarversion,msdyn_pminferredtask,msdyn_pmprocessextendedmetadataversion,msdyn_pmprocesstemplate,msdyn_pmprocessusersettings,msdyn_pmprocessversion,msdyn_pmrecording,msdyn_pmtemplate,msdyn_pmview,msdyn_richtextfile,msdyn_schedule,msdyn_serviceconfiguration,msdyn_slakpi,msdyn_solutionhealthrule,msdyn_solutionhealthruleargument,msdyn_solutionhealthruleset,msdyn_tour,msdyn_virtualtablecolumncandidate,msdyn_workflowactionstatus,msgraphresourcetosubscription,mspcat_catalogsubmissionfiles,mspcat_packagestore,organization,organizationdatasyncfnostate,organizationdatasyncstate,organizationdatasyncsubscription,organizationdatasyncsubscriptionentity,organizationdatasyncsubscriptionfnotable,organizationsetting,package,pdfsetting,phonecall,pluginpackage,post,powerbidataset,powerbimashupparameter,powerbireport,powerfxrule,privilege,privilegesremovalsetting,processstageparameter,provisionlanguageforuser,quarterlyfiscalcalendar,queue,queueitem,reconciliationentityinfo,reconciliationinfo,recordfilter,recurringappointmentmaster,relationshipattribute,relationshiprole,relationshiprolemap,retaineddataexcel,retentioncleanupinfo,retentioncleanupoperation,retentionconfig,retentionfailuredetail,retentionoperation,retentionoperationdetail,revokeinheritedaccessrecordstracker,role,roleeditorlayout,routingrule,routingruleitem,savedquery,searchattributesettings,searchcustomanalyzer,searchrelationshipsettings,semiannualfiscalcalendar,serviceplan,serviceplanmapping,settingdefinition,sharedlinksetting,sharedobject,sharedworkspace,sharedworkspacepool,sla,socialactivity,solutioncomponentattributeconfiguration,solutioncomponentbatchconfiguration,solutioncomponentconfiguration,solutioncomponentrelationshipconfiguration,stagedentity,stagedentityattribute,stagesolutionupload,subject,supportusertable,synapsedatabase,synapselinkexternaltablestate,synapselinkprofile,synapselinkprofileentity,synapselinkprofileentitystate,synapselinkschedule,systemform,systemuser,systemuserauthorizationchangetracker,task,tdsmetadata,team,teammobileofflineprofilemembership,template,territory,theme,userform,usermapping,usermobileofflineprofilemembership,userquery,userrating,virtualentitymetadata,workflowbinary,workqueue,workqueueitem|
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
|MaxLength|850|
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
- [solutioncomponentbatchconfiguration_BulkDeleteFailures](#BKMK_solutioncomponentbatchconfiguration_BulkDeleteFailures)
- [solutioncomponentconfiguration_BulkDeleteFailures](#BKMK_solutioncomponentconfiguration_BulkDeleteFailures)
- [solutioncomponentrelationshipconfiguration_BulkDeleteFailures](#BKMK_solutioncomponentrelationshipconfiguration_BulkDeleteFailures)
- [package_BulkDeleteFailures](#BKMK_package_BulkDeleteFailures)
- [stagesolutionupload_BulkDeleteFailures](#BKMK_stagesolutionupload_BulkDeleteFailures)
- [exportsolutionupload_BulkDeleteFailures](#BKMK_exportsolutionupload_BulkDeleteFailures)
- [featurecontrolsetting_BulkDeleteFailures](#BKMK_featurecontrolsetting_BulkDeleteFailures)
- [attributeimageconfig_BulkDeleteFailures](#BKMK_attributeimageconfig_BulkDeleteFailures)
- [entityimageconfig_BulkDeleteFailures](#BKMK_entityimageconfig_BulkDeleteFailures)
- [relationshipattribute_BulkDeleteFailures](#BKMK_relationshipattribute_BulkDeleteFailures)
- [stagedentity_BulkDeleteFailures](#BKMK_stagedentity_BulkDeleteFailures)
- [stagedentityattribute_BulkDeleteFailures](#BKMK_stagedentityattribute_BulkDeleteFailures)
- [catalog_BulkDeleteFailures](#BKMK_catalog_BulkDeleteFailures)
- [catalogassignment_BulkDeleteFailures](#BKMK_catalogassignment_BulkDeleteFailures)
- [customapi_BulkDeleteFailures](#BKMK_customapi_BulkDeleteFailures)
- [customapirequestparameter_BulkDeleteFailures](#BKMK_customapirequestparameter_BulkDeleteFailures)
- [customapiresponseproperty_BulkDeleteFailures](#BKMK_customapiresponseproperty_BulkDeleteFailures)
- [provisionlanguageforuser_BulkDeleteFailures](#BKMK_provisionlanguageforuser_BulkDeleteFailures)
- [sharedobject_BulkDeleteFailures](#BKMK_sharedobject_BulkDeleteFailures)
- [sharedworkspace_BulkDeleteFailures](#BKMK_sharedworkspace_BulkDeleteFailures)
- [sharedworkspacepool_BulkDeleteFailures](#BKMK_sharedworkspacepool_BulkDeleteFailures)
- [entityanalyticsconfig_BulkDeleteFailures](#BKMK_entityanalyticsconfig_BulkDeleteFailures)
- [datalakefolder_BulkDeleteFailures](#BKMK_datalakefolder_BulkDeleteFailures)
- [datalakefolderpermission_BulkDeleteFailures](#BKMK_datalakefolderpermission_BulkDeleteFailures)
- [datalakeworkspace_BulkDeleteFailures](#BKMK_datalakeworkspace_BulkDeleteFailures)
- [datalakeworkspacepermission_BulkDeleteFailures](#BKMK_datalakeworkspacepermission_BulkDeleteFailures)
- [dataprocessingconfiguration_BulkDeleteFailures](#BKMK_dataprocessingconfiguration_BulkDeleteFailures)
- [exportedexcel_BulkDeleteFailures](#BKMK_exportedexcel_BulkDeleteFailures)
- [retaineddataexcel_BulkDeleteFailures](#BKMK_retaineddataexcel_BulkDeleteFailures)
- [synapsedatabase_BulkDeleteFailures](#BKMK_synapsedatabase_BulkDeleteFailures)
- [synapselinkexternaltablestate_BulkDeleteFailures](#BKMK_synapselinkexternaltablestate_BulkDeleteFailures)
- [synapselinkprofile_BulkDeleteFailures](#BKMK_synapselinkprofile_BulkDeleteFailures)
- [synapselinkprofileentity_BulkDeleteFailures](#BKMK_synapselinkprofileentity_BulkDeleteFailures)
- [synapselinkprofileentitystate_BulkDeleteFailures](#BKMK_synapselinkprofileentitystate_BulkDeleteFailures)
- [synapselinkschedule_BulkDeleteFailures](#BKMK_synapselinkschedule_BulkDeleteFailures)
- [msdyn_dataflow_BulkDeleteFailures](#BKMK_msdyn_dataflow_BulkDeleteFailures)
- [msdyn_dataflowrefreshhistory_BulkDeleteFailures](#BKMK_msdyn_dataflowrefreshhistory_BulkDeleteFailures)
- [msdyn_entityrefreshhistory_BulkDeleteFailures](#BKMK_msdyn_entityrefreshhistory_BulkDeleteFailures)
- [sharedlinksetting_BulkDeleteFailures](#BKMK_sharedlinksetting_BulkDeleteFailures)
- [entityrecordfilter_BulkDeleteFailures](#BKMK_entityrecordfilter_BulkDeleteFailures)
- [recordfilter_BulkDeleteFailures](#BKMK_recordfilter_BulkDeleteFailures)
- [delegatedauthorization_BulkDeleteFailures](#BKMK_delegatedauthorization_BulkDeleteFailures)
- [serviceplan_BulkDeleteFailures](#BKMK_serviceplan_BulkDeleteFailures)
- [serviceplanmapping_BulkDeleteFailures](#BKMK_serviceplanmapping_BulkDeleteFailures)
- [applicationuser_BulkDeleteFailures](#BKMK_applicationuser_BulkDeleteFailures)
- [connector_BulkDeleteFailures](#BKMK_connector_BulkDeleteFailures)
- [environmentvariabledefinition_BulkDeleteFailures](#BKMK_environmentvariabledefinition_BulkDeleteFailures)
- [environmentvariablevalue_BulkDeleteFailures](#BKMK_environmentvariablevalue_BulkDeleteFailures)
- [workflowbinary_BulkDeleteFailures](#BKMK_workflowbinary_BulkDeleteFailures)
- [desktopflowmodule_BulkDeleteFailures](#BKMK_desktopflowmodule_BulkDeleteFailures)
- [flowmachine_BulkDeleteFailures](#BKMK_flowmachine_BulkDeleteFailures)
- [flowmachinegroup_BulkDeleteFailures](#BKMK_flowmachinegroup_BulkDeleteFailures)
- [flowmachineimage_BulkDeleteFailures](#BKMK_flowmachineimage_BulkDeleteFailures)
- [flowmachineimageversion_BulkDeleteFailures](#BKMK_flowmachineimageversion_BulkDeleteFailures)
- [flowmachinenetwork_BulkDeleteFailures](#BKMK_flowmachinenetwork_BulkDeleteFailures)
- [processstageparameter_BulkDeleteFailures](#BKMK_processstageparameter_BulkDeleteFailures)
- [workqueue_BulkDeleteFailures](#BKMK_workqueue_BulkDeleteFailures)
- [workqueueitem_BulkDeleteFailures](#BKMK_workqueueitem_BulkDeleteFailures)
- [desktopflowbinary_BulkDeleteFailures](#BKMK_desktopflowbinary_BulkDeleteFailures)
- [flowsession_BulkDeleteFailures](#BKMK_flowsession_BulkDeleteFailures)
- [connectionreference_BulkDeleteFailures](#BKMK_connectionreference_BulkDeleteFailures)
- [connectioninstance_BulkDeleteFailures](#BKMK_connectioninstance_BulkDeleteFailures)
- [msdyn_helppage_BulkDeleteFailures](#BKMK_msdyn_helppage_BulkDeleteFailures)
- [msdyn_tour_BulkDeleteFailures](#BKMK_msdyn_tour_BulkDeleteFailures)
- [msdynce_botcontent_BulkDeleteFailures](#BKMK_msdynce_botcontent_BulkDeleteFailures)
- [conversationtranscript_BulkDeleteFailures](#BKMK_conversationtranscript_BulkDeleteFailures)
- [bot_BulkDeleteFailures](#BKMK_bot_BulkDeleteFailures)
- [botcomponent_BulkDeleteFailures](#BKMK_botcomponent_BulkDeleteFailures)
- [Territory_BulkDeleteFailures](#BKMK_Territory_BulkDeleteFailures)
- [activityfileattachment_BulkDeleteFailures](#BKMK_activityfileattachment_BulkDeleteFailures)
- [chat_BulkDeleteFailures](#BKMK_chat_BulkDeleteFailures)
- [msdyn_serviceconfiguration_BulkDeleteFailures](#BKMK_msdyn_serviceconfiguration_BulkDeleteFailures)
- [msdyn_slakpi_BulkDeleteFailures](#BKMK_msdyn_slakpi_BulkDeleteFailures)
- [msdyn_knowledgemanagementsetting_BulkDeleteFailures](#BKMK_msdyn_knowledgemanagementsetting_BulkDeleteFailures)
- [msdyn_federatedarticle_BulkDeleteFailures](#BKMK_msdyn_federatedarticle_BulkDeleteFailures)
- [msdyn_federatedarticleincident_BulkDeleteFailures](#BKMK_msdyn_federatedarticleincident_BulkDeleteFailures)
- [msdyn_integratedsearchprovider_BulkDeleteFailures](#BKMK_msdyn_integratedsearchprovider_BulkDeleteFailures)
- [msdyn_kmfederatedsearchconfig_BulkDeleteFailures](#BKMK_msdyn_kmfederatedsearchconfig_BulkDeleteFailures)
- [msdyn_knowledgearticleimage_BulkDeleteFailures](#BKMK_msdyn_knowledgearticleimage_BulkDeleteFailures)
- [msdyn_knowledgeconfiguration_BulkDeleteFailures](#BKMK_msdyn_knowledgeconfiguration_BulkDeleteFailures)
- [msdyn_knowledgeinteractioninsight_BulkDeleteFailures](#BKMK_msdyn_knowledgeinteractioninsight_BulkDeleteFailures)
- [msdyn_knowledgesearchinsight_BulkDeleteFailures](#BKMK_msdyn_knowledgesearchinsight_BulkDeleteFailures)
- [msdyn_favoriteknowledgearticle_BulkDeleteFailures](#BKMK_msdyn_favoriteknowledgearticle_BulkDeleteFailures)
- [msdyn_kalanguagesetting_BulkDeleteFailures](#BKMK_msdyn_kalanguagesetting_BulkDeleteFailures)
- [msdyn_kbattachment_BulkDeleteFailures](#BKMK_msdyn_kbattachment_BulkDeleteFailures)
- [msdyn_kmpersonalizationsetting_BulkDeleteFailures](#BKMK_msdyn_kmpersonalizationsetting_BulkDeleteFailures)
- [msdyn_knowledgearticletemplate_BulkDeleteFailures](#BKMK_msdyn_knowledgearticletemplate_BulkDeleteFailures)
- [msdyn_knowledgepersonalfilter_BulkDeleteFailures](#BKMK_msdyn_knowledgepersonalfilter_BulkDeleteFailures)
- [msdyn_knowledgesearchfilter_BulkDeleteFailures](#BKMK_msdyn_knowledgesearchfilter_BulkDeleteFailures)
- [pluginpackage_BulkDeleteFailures](#BKMK_pluginpackage_BulkDeleteFailures)
- [fxexpression_BulkDeleteFailures](#BKMK_fxexpression_BulkDeleteFailures)
- [powerfxrule_BulkDeleteFailures](#BKMK_powerfxrule_BulkDeleteFailures)
- [keyvaultreference_BulkDeleteFailures](#BKMK_keyvaultreference_BulkDeleteFailures)
- [managedidentity_BulkDeleteFailures](#BKMK_managedidentity_BulkDeleteFailures)
- [msgraphresourcetosubscription_BulkDeleteFailures](#BKMK_msgraphresourcetosubscription_BulkDeleteFailures)
- [virtualentitymetadata_BulkDeleteFailures](#BKMK_virtualentitymetadata_BulkDeleteFailures)
- [mobileofflineprofileextension_BulkDeleteFailures](#BKMK_mobileofflineprofileextension_BulkDeleteFailures)
- [teammobileofflineprofilemembership_BulkDeleteFailures](#BKMK_teammobileofflineprofilemembership_BulkDeleteFailures)
- [usermobileofflineprofilemembership_BulkDeleteFailures](#BKMK_usermobileofflineprofilemembership_BulkDeleteFailures)
- [organizationdatasyncsubscription_BulkDeleteFailures](#BKMK_organizationdatasyncsubscription_BulkDeleteFailures)
- [organizationdatasyncsubscriptionentity_BulkDeleteFailures](#BKMK_organizationdatasyncsubscriptionentity_BulkDeleteFailures)
- [organizationdatasyncsubscriptionfnotable_BulkDeleteFailures](#BKMK_organizationdatasyncsubscriptionfnotable_BulkDeleteFailures)
- [organizationdatasyncfnostate_BulkDeleteFailures](#BKMK_organizationdatasyncfnostate_BulkDeleteFailures)
- [organizationdatasyncstate_BulkDeleteFailures](#BKMK_organizationdatasyncstate_BulkDeleteFailures)
- [metadataforarchival_BulkDeleteFailures](#BKMK_metadataforarchival_BulkDeleteFailures)
- [retentionconfig_BulkDeleteFailures](#BKMK_retentionconfig_BulkDeleteFailures)
- [retentionfailuredetail_BulkDeleteFailures](#BKMK_retentionfailuredetail_BulkDeleteFailures)
- [retentionoperation_BulkDeleteFailures](#BKMK_retentionoperation_BulkDeleteFailures)
- [retentionoperationdetail_BulkDeleteFailures](#BKMK_retentionoperationdetail_BulkDeleteFailures)
- [msdyn_appinsightsmetadata_BulkDeleteFailures](#BKMK_msdyn_appinsightsmetadata_BulkDeleteFailures)
- [msdyn_dataflowtemplate_BulkDeleteFailures](#BKMK_msdyn_dataflowtemplate_BulkDeleteFailures)
- [msdyn_workflowactionstatus_BulkDeleteFailures](#BKMK_msdyn_workflowactionstatus_BulkDeleteFailures)
- [userrating_BulkDeleteFailures](#BKMK_userrating_BulkDeleteFailures)
- [msdyn_mobileapp_BulkDeleteFailures](#BKMK_msdyn_mobileapp_BulkDeleteFailures)
- [msdyn_insightsstorevirtualentity_BulkDeleteFailures](#BKMK_msdyn_insightsstorevirtualentity_BulkDeleteFailures)
- [roleeditorlayout_BulkDeleteFailures](#BKMK_roleeditorlayout_BulkDeleteFailures)
- [appaction_BulkDeleteFailures](#BKMK_appaction_BulkDeleteFailures)
- [appactionmigration_BulkDeleteFailures](#BKMK_appactionmigration_BulkDeleteFailures)
- [appactionrule_BulkDeleteFailures](#BKMK_appactionrule_BulkDeleteFailures)
- [card_BulkDeleteFailures](#BKMK_card_BulkDeleteFailures)
- [msdyn_entitylinkchatconfiguration_BulkDeleteFailures](#BKMK_msdyn_entitylinkchatconfiguration_BulkDeleteFailures)
- [msdyn_richtextfile_BulkDeleteFailures](#BKMK_msdyn_richtextfile_BulkDeleteFailures)
- [msdyn_customcontrolextendedsettings_BulkDeleteFailures](#BKMK_msdyn_customcontrolextendedsettings_BulkDeleteFailures)
- [searchrelationshipsettings_BulkDeleteFailures](#BKMK_searchrelationshipsettings_BulkDeleteFailures)
- [msdyn_virtualtablecolumncandidate_BulkDeleteFailures](#BKMK_msdyn_virtualtablecolumncandidate_BulkDeleteFailures)
- [msdyn_aiconfiguration_BulkDeleteFailures](#BKMK_msdyn_aiconfiguration_BulkDeleteFailures)
- [msdyn_aievent_BulkDeleteFailures](#BKMK_msdyn_aievent_BulkDeleteFailures)
- [msdyn_aimodel_BulkDeleteFailures](#BKMK_msdyn_aimodel_BulkDeleteFailures)
- [msdyn_aitemplate_BulkDeleteFailures](#BKMK_msdyn_aitemplate_BulkDeleteFailures)
- [msdyn_aibfeedbackloop_BulkDeleteFailures](#BKMK_msdyn_aibfeedbackloop_BulkDeleteFailures)
- [msdyn_aifptrainingdocument_BulkDeleteFailures](#BKMK_msdyn_aifptrainingdocument_BulkDeleteFailures)
- [msdyn_aiodimage_BulkDeleteFailures](#BKMK_msdyn_aiodimage_BulkDeleteFailures)
- [msdyn_aiodlabel_BulkDeleteFailures](#BKMK_msdyn_aiodlabel_BulkDeleteFailures)
- [msdyn_aiodtrainingboundingbox_BulkDeleteFailures](#BKMK_msdyn_aiodtrainingboundingbox_BulkDeleteFailures)
- [msdyn_aiodtrainingimage_BulkDeleteFailures](#BKMK_msdyn_aiodtrainingimage_BulkDeleteFailures)
- [msdyn_aibdataset_BulkDeleteFailures](#BKMK_msdyn_aibdataset_BulkDeleteFailures)
- [msdyn_aibdatasetfile_BulkDeleteFailures](#BKMK_msdyn_aibdatasetfile_BulkDeleteFailures)
- [msdyn_aibdatasetrecord_BulkDeleteFailures](#BKMK_msdyn_aibdatasetrecord_BulkDeleteFailures)
- [msdyn_aibdatasetscontainer_BulkDeleteFailures](#BKMK_msdyn_aibdatasetscontainer_BulkDeleteFailures)
- [msdyn_aibfile_BulkDeleteFailures](#BKMK_msdyn_aibfile_BulkDeleteFailures)
- [msdyn_aibfileattacheddata_BulkDeleteFailures](#BKMK_msdyn_aibfileattacheddata_BulkDeleteFailures)
- [msdyn_pmanalysishistory_BulkDeleteFailures](#BKMK_msdyn_pmanalysishistory_BulkDeleteFailures)
- [msdyn_pmcalendar_BulkDeleteFailures](#BKMK_msdyn_pmcalendar_BulkDeleteFailures)
- [msdyn_pmcalendarversion_BulkDeleteFailures](#BKMK_msdyn_pmcalendarversion_BulkDeleteFailures)
- [msdyn_pminferredtask_BulkDeleteFailures](#BKMK_msdyn_pminferredtask_BulkDeleteFailures)
- [msdyn_pmprocessextendedmetadataversion_BulkDeleteFailures](#BKMK_msdyn_pmprocessextendedmetadataversion_BulkDeleteFailures)
- [msdyn_pmprocesstemplate_BulkDeleteFailures](#BKMK_msdyn_pmprocesstemplate_BulkDeleteFailures)
- [msdyn_pmprocessusersettings_BulkDeleteFailures](#BKMK_msdyn_pmprocessusersettings_BulkDeleteFailures)
- [msdyn_pmprocessversion_BulkDeleteFailures](#BKMK_msdyn_pmprocessversion_BulkDeleteFailures)
- [msdyn_pmrecording_BulkDeleteFailures](#BKMK_msdyn_pmrecording_BulkDeleteFailures)
- [msdyn_pmtemplate_BulkDeleteFailures](#BKMK_msdyn_pmtemplate_BulkDeleteFailures)
- [msdyn_pmview_BulkDeleteFailures](#BKMK_msdyn_pmview_BulkDeleteFailures)
- [msdyn_analysiscomponent_BulkDeleteFailures](#BKMK_msdyn_analysiscomponent_BulkDeleteFailures)
- [msdyn_analysisjob_BulkDeleteFailures](#BKMK_msdyn_analysisjob_BulkDeleteFailures)
- [msdyn_analysisoverride_BulkDeleteFailures](#BKMK_msdyn_analysisoverride_BulkDeleteFailures)
- [msdyn_analysisresult_BulkDeleteFailures](#BKMK_msdyn_analysisresult_BulkDeleteFailures)
- [msdyn_analysisresultdetail_BulkDeleteFailures](#BKMK_msdyn_analysisresultdetail_BulkDeleteFailures)
- [msdyn_solutionhealthrule_BulkDeleteFailures](#BKMK_msdyn_solutionhealthrule_BulkDeleteFailures)
- [msdyn_solutionhealthruleargument_BulkDeleteFailures](#BKMK_msdyn_solutionhealthruleargument_BulkDeleteFailures)
- [msdyn_solutionhealthruleset_BulkDeleteFailures](#BKMK_msdyn_solutionhealthruleset_BulkDeleteFailures)
- [powerbidataset_BulkDeleteFailures](#BKMK_powerbidataset_BulkDeleteFailures)
- [powerbimashupparameter_BulkDeleteFailures](#BKMK_powerbimashupparameter_BulkDeleteFailures)
- [powerbireport_BulkDeleteFailures](#BKMK_powerbireport_BulkDeleteFailures)
- [msdyn_fileupload_BulkDeleteFailures](#BKMK_msdyn_fileupload_BulkDeleteFailures)
- [mspcat_catalogsubmissionfiles_BulkDeleteFailures](#BKMK_mspcat_catalogsubmissionfiles_BulkDeleteFailures)
- [mspcat_packagestore_BulkDeleteFailures](#BKMK_mspcat_packagestore_BulkDeleteFailures)
- [msdyn_schedule_BulkDeleteFailures](#BKMK_msdyn_schedule_BulkDeleteFailures)
- [msdyn_dataflow_datalakefolder_BulkDeleteFailures](#BKMK_msdyn_dataflow_datalakefolder_BulkDeleteFailures)
- [msdyn_dmsrequest_BulkDeleteFailures](#BKMK_msdyn_dmsrequest_BulkDeleteFailures)
- [msdyn_dmsrequeststatus_BulkDeleteFailures](#BKMK_msdyn_dmsrequeststatus_BulkDeleteFailures)
- [searchattributesettings_BulkDeleteFailures](#BKMK_searchattributesettings_BulkDeleteFailures)
- [searchcustomanalyzer_BulkDeleteFailures](#BKMK_searchcustomanalyzer_BulkDeleteFailures)


### <a name="BKMK_theme_BulkDeleteFailures"></a> theme_BulkDeleteFailures

See the [theme_BulkDeleteFailures](theme.md#BKMK_theme_BulkDeleteFailures) one-to-many relationship for the [theme](theme.md) table/entity.

### <a name="BKMK_usermapping_BulkDeleteFailures"></a> usermapping_BulkDeleteFailures

See the [usermapping_BulkDeleteFailures](usermapping.md#BKMK_usermapping_BulkDeleteFailures) one-to-many relationship for the [usermapping](usermapping.md) table/entity.

### <a name="BKMK_knowledgearticle_BulkDeleteFailures"></a> knowledgearticle_BulkDeleteFailures

See the [knowledgearticle_BulkDeleteFailures](knowledgearticle.md#BKMK_knowledgearticle_BulkDeleteFailures) one-to-many relationship for the [knowledgearticle](knowledgearticle.md) table/entity.

### <a name="BKMK_post_BulkDeleteFailures"></a> post_BulkDeleteFailures

See the [post_BulkDeleteFailures](post.md#BKMK_post_BulkDeleteFailures) one-to-many relationship for the [post](post.md) table/entity.

### <a name="BKMK_KnowledgeBaseRecord_BulkDeleteFailures"></a> KnowledgeBaseRecord_BulkDeleteFailures

See the [KnowledgeBaseRecord_BulkDeleteFailures](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_BulkDeleteFailures) one-to-many relationship for the [knowledgebaserecord](knowledgebaserecord.md) table/entity.

### <a name="BKMK_Role_BulkDeleteFailures"></a> Role_BulkDeleteFailures

See the [Role_BulkDeleteFailures](role.md#BKMK_Role_BulkDeleteFailures) one-to-many relationship for the [role](role.md) table/entity.

### <a name="BKMK_Subject_BulkDeleteFailures"></a> Subject_BulkDeleteFailures

See the [Subject_BulkDeleteFailures](subject.md#BKMK_Subject_BulkDeleteFailures) one-to-many relationship for the [subject](subject.md) table/entity.

### <a name="BKMK_Fax_BulkDeleteFailures"></a> Fax_BulkDeleteFailures

See the [Fax_BulkDeleteFailures](fax.md#BKMK_Fax_BulkDeleteFailures) one-to-many relationship for the [fax](fax.md) table/entity.

### <a name="BKMK_Privilege_BulkDeleteFailures"></a> Privilege_BulkDeleteFailures

See the [Privilege_BulkDeleteFailures](privilege.md#BKMK_Privilege_BulkDeleteFailures) one-to-many relationship for the [privilege](privilege.md) table/entity.

### <a name="BKMK_KbArticle_BulkDeleteFailures"></a> KbArticle_BulkDeleteFailures

See the [KbArticle_BulkDeleteFailures](kbarticle.md#BKMK_KbArticle_BulkDeleteFailures) one-to-many relationship for the [kbarticle](kbarticle.md) table/entity.

### <a name="BKMK_KbArticleComment_BulkDeleteFailures"></a> KbArticleComment_BulkDeleteFailures

See the [KbArticleComment_BulkDeleteFailures](kbarticlecomment.md#BKMK_KbArticleComment_BulkDeleteFailures) one-to-many relationship for the [kbarticlecomment](kbarticlecomment.md) table/entity.

### <a name="BKMK_AnnualFiscalCalendar_BulkDeleteFailures"></a> AnnualFiscalCalendar_BulkDeleteFailures

See the [AnnualFiscalCalendar_BulkDeleteFailures](annualfiscalcalendar.md#BKMK_AnnualFiscalCalendar_BulkDeleteFailures) one-to-many relationship for the [annualfiscalcalendar](annualfiscalcalendar.md) table/entity.

### <a name="BKMK_UserForm_BulkDeleteFailures"></a> UserForm_BulkDeleteFailures

See the [UserForm_BulkDeleteFailures](userform.md#BKMK_UserForm_BulkDeleteFailures) one-to-many relationship for the [userform](userform.md) table/entity.

### <a name="BKMK_Queue_BulkDeleteFailures"></a> Queue_BulkDeleteFailures

See the [Queue_BulkDeleteFailures](queue.md#BKMK_Queue_BulkDeleteFailures) one-to-many relationship for the [queue](queue.md) table/entity.

### <a name="BKMK_Contact_BulkDeleteFailures"></a> Contact_BulkDeleteFailures

See the [Contact_BulkDeleteFailures](contact.md#BKMK_Contact_BulkDeleteFailures) one-to-many relationship for the [contact](contact.md) table/entity.

### <a name="BKMK_emailserverprofile_bulkdeletefailures"></a> emailserverprofile_bulkdeletefailures

See the [emailserverprofile_bulkdeletefailures](emailserverprofile.md#BKMK_emailserverprofile_bulkdeletefailures) one-to-many relationship for the [emailserverprofile](emailserverprofile.md) table/entity.

### <a name="BKMK_SavedQuery_BulkDeleteFailures"></a> SavedQuery_BulkDeleteFailures

See the [SavedQuery_BulkDeleteFailures](savedquery.md#BKMK_SavedQuery_BulkDeleteFailures) one-to-many relationship for the [savedquery](savedquery.md) table/entity.

### <a name="BKMK_Appointment_BulkDeleteFailures"></a> Appointment_BulkDeleteFailures

See the [Appointment_BulkDeleteFailures](appointment.md#BKMK_Appointment_BulkDeleteFailures) one-to-many relationship for the [appointment](appointment.md) table/entity.

### <a name="BKMK_Template_BulkDeleteFailures"></a> Template_BulkDeleteFailures

See the [Template_BulkDeleteFailures](template.md#BKMK_Template_BulkDeleteFailures) one-to-many relationship for the [template](template.md) table/entity.

### <a name="BKMK_Account_BulkDeleteFailures"></a> Account_BulkDeleteFailures

See the [Account_BulkDeleteFailures](account.md#BKMK_Account_BulkDeleteFailures) one-to-many relationship for the [account](account.md) table/entity.

### <a name="BKMK_SystemUser_BulkDeleteFailures"></a> SystemUser_BulkDeleteFailures

See the [SystemUser_BulkDeleteFailures](systemuser.md#BKMK_SystemUser_BulkDeleteFailures) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_QuarterlyFiscalCalendar_BulkDeleteFailures"></a> QuarterlyFiscalCalendar_BulkDeleteFailures

See the [QuarterlyFiscalCalendar_BulkDeleteFailures](quarterlyfiscalcalendar.md#BKMK_QuarterlyFiscalCalendar_BulkDeleteFailures) one-to-many relationship for the [quarterlyfiscalcalendar](quarterlyfiscalcalendar.md) table/entity.

### <a name="BKMK_QueueItem_BulkDeleteFailures"></a> QueueItem_BulkDeleteFailures

See the [QueueItem_BulkDeleteFailures](queueitem.md#BKMK_QueueItem_BulkDeleteFailures) one-to-many relationship for the [queueitem](queueitem.md) table/entity.

### <a name="BKMK_DisplayString_BulkDeleteFailures"></a> DisplayString_BulkDeleteFailures

See the [DisplayString_BulkDeleteFailures](displaystring.md#BKMK_DisplayString_BulkDeleteFailures) one-to-many relationship for the [displaystring](displaystring.md) table/entity.

### <a name="BKMK_Calendar_BulkDeleteFailures"></a> Calendar_BulkDeleteFailures

See the [Calendar_BulkDeleteFailures](calendar.md#BKMK_Calendar_BulkDeleteFailures) one-to-many relationship for the [calendar](calendar.md) table/entity.

### <a name="BKMK_Organization_BulkDeleteFailures"></a> Organization_BulkDeleteFailures

See the [Organization_BulkDeleteFailures](organization.md#BKMK_Organization_BulkDeleteFailures) one-to-many relationship for the [organization](organization.md) table/entity.

### <a name="BKMK_BusinessUnit_BulkDeleteFailures"></a> BusinessUnit_BulkDeleteFailures

See the [BusinessUnit_BulkDeleteFailures](businessunit.md#BKMK_BusinessUnit_BulkDeleteFailures) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_Annotation_BulkDeleteFailures"></a> Annotation_BulkDeleteFailures

See the [Annotation_BulkDeleteFailures](annotation.md#BKMK_Annotation_BulkDeleteFailures) one-to-many relationship for the [annotation](annotation.md) table/entity.

### <a name="BKMK_ImportLog_BulkDeleteFailures"></a> ImportLog_BulkDeleteFailures

See the [ImportLog_BulkDeleteFailures](importlog.md#BKMK_ImportLog_BulkDeleteFailures) one-to-many relationship for the [importlog](importlog.md) table/entity.

### <a name="BKMK_Import_BulkDeleteFailures"></a> Import_BulkDeleteFailures

See the [Import_BulkDeleteFailures](import.md#BKMK_Import_BulkDeleteFailures) one-to-many relationship for the [import](import.md) table/entity.

### <a name="BKMK_Letter_BulkDeleteFailures"></a> Letter_BulkDeleteFailures

See the [Letter_BulkDeleteFailures](letter.md#BKMK_Letter_BulkDeleteFailures) one-to-many relationship for the [letter](letter.md) table/entity.

### <a name="BKMK_UserQuery_BulkDeleteFailures"></a> UserQuery_BulkDeleteFailures

See the [UserQuery_BulkDeleteFailures](userquery.md#BKMK_UserQuery_BulkDeleteFailures) one-to-many relationship for the [userquery](userquery.md) table/entity.

### <a name="BKMK_PhoneCall_BulkDeleteFailures"></a> PhoneCall_BulkDeleteFailures

See the [PhoneCall_BulkDeleteFailures](phonecall.md#BKMK_PhoneCall_BulkDeleteFailures) one-to-many relationship for the [phonecall](phonecall.md) table/entity.

### <a name="BKMK_Team_BulkDeleteFailures"></a> Team_BulkDeleteFailures

See the [Team_BulkDeleteFailures](team.md#BKMK_Team_BulkDeleteFailures) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_CustomerAddress_BulkDeleteFailures"></a> CustomerAddress_BulkDeleteFailures

See the [CustomerAddress_BulkDeleteFailures](customeraddress.md#BKMK_CustomerAddress_BulkDeleteFailures) one-to-many relationship for the [customeraddress](customeraddress.md) table/entity.

### <a name="BKMK_SocialActivity_BulkDeleteFailures"></a> SocialActivity_BulkDeleteFailures

See the [SocialActivity_BulkDeleteFailures](socialactivity.md#BKMK_SocialActivity_BulkDeleteFailures) one-to-many relationship for the [socialactivity](socialactivity.md) table/entity.

### <a name="BKMK_ImportFile_BulkDeleteFailures"></a> ImportFile_BulkDeleteFailures

See the [ImportFile_BulkDeleteFailures](importfile.md#BKMK_ImportFile_BulkDeleteFailures) one-to-many relationship for the [importfile](importfile.md) table/entity.

### <a name="BKMK_SystemForm_BulkDeleteFailures"></a> SystemForm_BulkDeleteFailures

See the [SystemForm_BulkDeleteFailures](systemform.md#BKMK_SystemForm_BulkDeleteFailures) one-to-many relationship for the [systemform](systemform.md) table/entity.

### <a name="BKMK_BusinessUnitNewsArticle_BulkDeleteFailures"></a> BusinessUnitNewsArticle_BulkDeleteFailures

See the [BusinessUnitNewsArticle_BulkDeleteFailures](businessunitnewsarticle.md#BKMK_BusinessUnitNewsArticle_BulkDeleteFailures) one-to-many relationship for the [businessunitnewsarticle](businessunitnewsarticle.md) table/entity.

### <a name="BKMK_ImportMap_BulkDeleteFailures"></a> ImportMap_BulkDeleteFailures

See the [ImportMap_BulkDeleteFailures](importmap.md#BKMK_ImportMap_BulkDeleteFailures) one-to-many relationship for the [importmap](importmap.md) table/entity.

### <a name="BKMK_RecurringAppointmentMaster_BulkDeleteFailures"></a> RecurringAppointmentMaster_BulkDeleteFailures

See the [RecurringAppointmentMaster_BulkDeleteFailures](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_BulkDeleteFailures) one-to-many relationship for the [recurringappointmentmaster](recurringappointmentmaster.md) table/entity.

### <a name="BKMK_Email_BulkDeleteFailures"></a> Email_BulkDeleteFailures

See the [Email_BulkDeleteFailures](email.md#BKMK_Email_BulkDeleteFailures) one-to-many relationship for the [email](email.md) table/entity.

### <a name="BKMK_MonthlyFiscalCalendar_BulkDeleteFailures"></a> MonthlyFiscalCalendar_BulkDeleteFailures

See the [MonthlyFiscalCalendar_BulkDeleteFailures](monthlyfiscalcalendar.md#BKMK_MonthlyFiscalCalendar_BulkDeleteFailures) one-to-many relationship for the [monthlyfiscalcalendar](monthlyfiscalcalendar.md) table/entity.

### <a name="BKMK_KbArticleTemplate_BulkDeleteFailures"></a> KbArticleTemplate_BulkDeleteFailures

See the [KbArticleTemplate_BulkDeleteFailures](kbarticletemplate.md#BKMK_KbArticleTemplate_BulkDeleteFailures) one-to-many relationship for the [kbarticletemplate](kbarticletemplate.md) table/entity.

### <a name="BKMK_ActivityPointer_BulkDeleteFailures"></a> ActivityPointer_BulkDeleteFailures

See the [ActivityPointer_BulkDeleteFailures](activitypointer.md#BKMK_ActivityPointer_BulkDeleteFailures) one-to-many relationship for the [activitypointer](activitypointer.md) table/entity.

### <a name="BKMK_slabase_BulkDeleteFailures"></a> slabase_BulkDeleteFailures

See the [slabase_BulkDeleteFailures](sla.md#BKMK_slabase_BulkDeleteFailures) one-to-many relationship for the [sla](sla.md) table/entity.

### <a name="BKMK_FixedMonthlyFiscalCalendar_BulkDeleteFailures"></a> FixedMonthlyFiscalCalendar_BulkDeleteFailures

See the [FixedMonthlyFiscalCalendar_BulkDeleteFailures](fixedmonthlyfiscalcalendar.md#BKMK_FixedMonthlyFiscalCalendar_BulkDeleteFailures) one-to-many relationship for the [fixedmonthlyfiscalcalendar](fixedmonthlyfiscalcalendar.md) table/entity.

### <a name="BKMK_Task_BulkDeleteFailures"></a> Task_BulkDeleteFailures

See the [Task_BulkDeleteFailures](task.md#BKMK_Task_BulkDeleteFailures) one-to-many relationship for the [task](task.md) table/entity.

### <a name="BKMK_BulkDeleteOperation_BulkDeleteFailure"></a> BulkDeleteOperation_BulkDeleteFailure

See the [BulkDeleteOperation_BulkDeleteFailure](bulkdeleteoperation.md#BKMK_BulkDeleteOperation_BulkDeleteFailure) one-to-many relationship for the [bulkdeleteoperation](bulkdeleteoperation.md) table/entity.

### <a name="BKMK_ActivityMimeAttachment_BulkDeleteFailures"></a> ActivityMimeAttachment_BulkDeleteFailures

See the [ActivityMimeAttachment_BulkDeleteFailures](activitymimeattachment.md#BKMK_ActivityMimeAttachment_BulkDeleteFailures) one-to-many relationship for the [activitymimeattachment](activitymimeattachment.md) table/entity.

### <a name="BKMK_SemiAnnualFiscalCalendar_BulkDeleteFailures"></a> SemiAnnualFiscalCalendar_BulkDeleteFailures

See the [SemiAnnualFiscalCalendar_BulkDeleteFailures](semiannualfiscalcalendar.md#BKMK_SemiAnnualFiscalCalendar_BulkDeleteFailures) one-to-many relationship for the [semiannualfiscalcalendar](semiannualfiscalcalendar.md) table/entity.

### <a name="BKMK_solutioncomponentattributeconfiguration_BulkDeleteFailures"></a> solutioncomponentattributeconfiguration_BulkDeleteFailures

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentattributeconfiguration_BulkDeleteFailures](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_BulkDeleteFailures) one-to-many relationship for the [solutioncomponentattributeconfiguration](solutioncomponentattributeconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentbatchconfiguration_BulkDeleteFailures"></a> solutioncomponentbatchconfiguration_BulkDeleteFailures

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentbatchconfiguration_BulkDeleteFailures](solutioncomponentbatchconfiguration.md#BKMK_solutioncomponentbatchconfiguration_BulkDeleteFailures) one-to-many relationship for the [solutioncomponentbatchconfiguration](solutioncomponentbatchconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentconfiguration_BulkDeleteFailures"></a> solutioncomponentconfiguration_BulkDeleteFailures

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentconfiguration_BulkDeleteFailures](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_BulkDeleteFailures) one-to-many relationship for the [solutioncomponentconfiguration](solutioncomponentconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentrelationshipconfiguration_BulkDeleteFailures"></a> solutioncomponentrelationshipconfiguration_BulkDeleteFailures

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentrelationshipconfiguration_BulkDeleteFailures](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_BulkDeleteFailures) one-to-many relationship for the [solutioncomponentrelationshipconfiguration](solutioncomponentrelationshipconfiguration.md) table/entity.

### <a name="BKMK_package_BulkDeleteFailures"></a> package_BulkDeleteFailures

**Added by**: msdyn_SolutionPackageMapping Solution

See the [package_BulkDeleteFailures](package.md#BKMK_package_BulkDeleteFailures) one-to-many relationship for the [package](package.md) table/entity.

### <a name="BKMK_stagesolutionupload_BulkDeleteFailures"></a> stagesolutionupload_BulkDeleteFailures

**Added by**: StageSolutionUpload Solution

See the [stagesolutionupload_BulkDeleteFailures](stagesolutionupload.md#BKMK_stagesolutionupload_BulkDeleteFailures) one-to-many relationship for the [stagesolutionupload](stagesolutionupload.md) table/entity.

### <a name="BKMK_exportsolutionupload_BulkDeleteFailures"></a> exportsolutionupload_BulkDeleteFailures

**Added by**: ExportSolutionUpload Solution

See the [exportsolutionupload_BulkDeleteFailures](exportsolutionupload.md#BKMK_exportsolutionupload_BulkDeleteFailures) one-to-many relationship for the [exportsolutionupload](exportsolutionupload.md) table/entity.

### <a name="BKMK_featurecontrolsetting_BulkDeleteFailures"></a> featurecontrolsetting_BulkDeleteFailures

**Added by**: msdyn_FeatureControlSetting Solution

See the [featurecontrolsetting_BulkDeleteFailures](featurecontrolsetting.md#BKMK_featurecontrolsetting_BulkDeleteFailures) one-to-many relationship for the [featurecontrolsetting](featurecontrolsetting.md) table/entity.

### <a name="BKMK_attributeimageconfig_BulkDeleteFailures"></a> attributeimageconfig_BulkDeleteFailures

**Added by**: Image Configuration Solution

See the [attributeimageconfig_BulkDeleteFailures](attributeimageconfig.md#BKMK_attributeimageconfig_BulkDeleteFailures) one-to-many relationship for the [attributeimageconfig](attributeimageconfig.md) table/entity.

### <a name="BKMK_entityimageconfig_BulkDeleteFailures"></a> entityimageconfig_BulkDeleteFailures

**Added by**: Image Configuration Solution

See the [entityimageconfig_BulkDeleteFailures](entityimageconfig.md#BKMK_entityimageconfig_BulkDeleteFailures) one-to-many relationship for the [entityimageconfig](entityimageconfig.md) table/entity.

### <a name="BKMK_relationshipattribute_BulkDeleteFailures"></a> relationshipattribute_BulkDeleteFailures

**Added by**: Metadata Extension Solution

See the [relationshipattribute_BulkDeleteFailures](relationshipattribute.md#BKMK_relationshipattribute_BulkDeleteFailures) one-to-many relationship for the [relationshipattribute](relationshipattribute.md) table/entity.

### <a name="BKMK_stagedentity_BulkDeleteFailures"></a> stagedentity_BulkDeleteFailures

**Added by**: Metadata Extension Solution

See the [stagedentity_BulkDeleteFailures](stagedentity.md#BKMK_stagedentity_BulkDeleteFailures) one-to-many relationship for the [stagedentity](stagedentity.md) table/entity.

### <a name="BKMK_stagedentityattribute_BulkDeleteFailures"></a> stagedentityattribute_BulkDeleteFailures

**Added by**: Metadata Extension Solution

See the [stagedentityattribute_BulkDeleteFailures](stagedentityattribute.md#BKMK_stagedentityattribute_BulkDeleteFailures) one-to-many relationship for the [stagedentityattribute](stagedentityattribute.md) table/entity.

### <a name="BKMK_catalog_BulkDeleteFailures"></a> catalog_BulkDeleteFailures

**Added by**: CatalogFramework Solution

See the [catalog_BulkDeleteFailures](catalog.md#BKMK_catalog_BulkDeleteFailures) one-to-many relationship for the [catalog](catalog.md) table/entity.

### <a name="BKMK_catalogassignment_BulkDeleteFailures"></a> catalogassignment_BulkDeleteFailures

**Added by**: CatalogFramework Solution

See the [catalogassignment_BulkDeleteFailures](catalogassignment.md#BKMK_catalogassignment_BulkDeleteFailures) one-to-many relationship for the [catalogassignment](catalogassignment.md) table/entity.

### <a name="BKMK_customapi_BulkDeleteFailures"></a> customapi_BulkDeleteFailures

**Added by**: Custom API Framework Solution

See the [customapi_BulkDeleteFailures](customapi.md#BKMK_customapi_BulkDeleteFailures) one-to-many relationship for the [customapi](customapi.md) table/entity.

### <a name="BKMK_customapirequestparameter_BulkDeleteFailures"></a> customapirequestparameter_BulkDeleteFailures

**Added by**: Custom API Framework Solution

See the [customapirequestparameter_BulkDeleteFailures](customapirequestparameter.md#BKMK_customapirequestparameter_BulkDeleteFailures) one-to-many relationship for the [customapirequestparameter](customapirequestparameter.md) table/entity.

### <a name="BKMK_customapiresponseproperty_BulkDeleteFailures"></a> customapiresponseproperty_BulkDeleteFailures

**Added by**: Custom API Framework Solution

See the [customapiresponseproperty_BulkDeleteFailures](customapiresponseproperty.md#BKMK_customapiresponseproperty_BulkDeleteFailures) one-to-many relationship for the [customapiresponseproperty](customapiresponseproperty.md) table/entity.

### <a name="BKMK_provisionlanguageforuser_BulkDeleteFailures"></a> provisionlanguageforuser_BulkDeleteFailures

**Added by**: msft_LocalizationExtension Solution

See the [provisionlanguageforuser_BulkDeleteFailures](provisionlanguageforuser.md#BKMK_provisionlanguageforuser_BulkDeleteFailures) one-to-many relationship for the [provisionlanguageforuser](provisionlanguageforuser.md) table/entity.

### <a name="BKMK_sharedobject_BulkDeleteFailures"></a> sharedobject_BulkDeleteFailures

**Added by**: Real-time Collaboration App Solution

See the [sharedobject_BulkDeleteFailures](sharedobject.md#BKMK_sharedobject_BulkDeleteFailures) one-to-many relationship for the [sharedobject](sharedobject.md) table/entity.

### <a name="BKMK_sharedworkspace_BulkDeleteFailures"></a> sharedworkspace_BulkDeleteFailures

**Added by**: Real-time Collaboration App Solution

See the [sharedworkspace_BulkDeleteFailures](sharedworkspace.md#BKMK_sharedworkspace_BulkDeleteFailures) one-to-many relationship for the [sharedworkspace](sharedworkspace.md) table/entity.

### <a name="BKMK_sharedworkspacepool_BulkDeleteFailures"></a> sharedworkspacepool_BulkDeleteFailures

**Added by**: Real-time Collaboration App Solution

See the [sharedworkspacepool_BulkDeleteFailures](sharedworkspacepool.md#BKMK_sharedworkspacepool_BulkDeleteFailures) one-to-many relationship for the [sharedworkspacepool](sharedworkspacepool.md) table/entity.

### <a name="BKMK_entityanalyticsconfig_BulkDeleteFailures"></a> entityanalyticsconfig_BulkDeleteFailures

**Added by**: Advanced Analytics Infrastructure Solution

See the [entityanalyticsconfig_BulkDeleteFailures](entityanalyticsconfig.md#BKMK_entityanalyticsconfig_BulkDeleteFailures) one-to-many relationship for the [entityanalyticsconfig](entityanalyticsconfig.md) table/entity.

### <a name="BKMK_datalakefolder_BulkDeleteFailures"></a> datalakefolder_BulkDeleteFailures

**Added by**: Data lake workspaces Solution

See the [datalakefolder_BulkDeleteFailures](datalakefolder.md#BKMK_datalakefolder_BulkDeleteFailures) one-to-many relationship for the [datalakefolder](datalakefolder.md) table/entity.

### <a name="BKMK_datalakefolderpermission_BulkDeleteFailures"></a> datalakefolderpermission_BulkDeleteFailures

**Added by**: Data lake workspaces Solution

See the [datalakefolderpermission_BulkDeleteFailures](datalakefolderpermission.md#BKMK_datalakefolderpermission_BulkDeleteFailures) one-to-many relationship for the [datalakefolderpermission](datalakefolderpermission.md) table/entity.

### <a name="BKMK_datalakeworkspace_BulkDeleteFailures"></a> datalakeworkspace_BulkDeleteFailures

**Added by**: Data lake workspaces Solution

See the [datalakeworkspace_BulkDeleteFailures](datalakeworkspace.md#BKMK_datalakeworkspace_BulkDeleteFailures) one-to-many relationship for the [datalakeworkspace](datalakeworkspace.md) table/entity.

### <a name="BKMK_datalakeworkspacepermission_BulkDeleteFailures"></a> datalakeworkspacepermission_BulkDeleteFailures

**Added by**: Data lake workspaces Solution

See the [datalakeworkspacepermission_BulkDeleteFailures](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_BulkDeleteFailures) one-to-many relationship for the [datalakeworkspacepermission](datalakeworkspacepermission.md) table/entity.

### <a name="BKMK_dataprocessingconfiguration_BulkDeleteFailures"></a> dataprocessingconfiguration_BulkDeleteFailures

**Added by**: Data lake workspaces Solution

See the [dataprocessingconfiguration_BulkDeleteFailures](dataprocessingconfiguration.md#BKMK_dataprocessingconfiguration_BulkDeleteFailures) one-to-many relationship for the [dataprocessingconfiguration](dataprocessingconfiguration.md) table/entity.

### <a name="BKMK_exportedexcel_BulkDeleteFailures"></a> exportedexcel_BulkDeleteFailures

**Added by**: Data lake workspaces Solution

See the [exportedexcel_BulkDeleteFailures](exportedexcel.md#BKMK_exportedexcel_BulkDeleteFailures) one-to-many relationship for the [exportedexcel](exportedexcel.md) table/entity.

### <a name="BKMK_retaineddataexcel_BulkDeleteFailures"></a> retaineddataexcel_BulkDeleteFailures

**Added by**: Data lake workspaces Solution

See the [retaineddataexcel_BulkDeleteFailures](retaineddataexcel.md#BKMK_retaineddataexcel_BulkDeleteFailures) one-to-many relationship for the [retaineddataexcel](retaineddataexcel.md) table/entity.

### <a name="BKMK_synapsedatabase_BulkDeleteFailures"></a> synapsedatabase_BulkDeleteFailures

**Added by**: Data lake workspaces Solution

See the [synapsedatabase_BulkDeleteFailures](synapsedatabase.md#BKMK_synapsedatabase_BulkDeleteFailures) one-to-many relationship for the [synapsedatabase](synapsedatabase.md) table/entity.

### <a name="BKMK_synapselinkexternaltablestate_BulkDeleteFailures"></a> synapselinkexternaltablestate_BulkDeleteFailures

**Added by**: Synapse Link Solution

See the [synapselinkexternaltablestate_BulkDeleteFailures](synapselinkexternaltablestate.md#BKMK_synapselinkexternaltablestate_BulkDeleteFailures) one-to-many relationship for the [synapselinkexternaltablestate](synapselinkexternaltablestate.md) table/entity.

### <a name="BKMK_synapselinkprofile_BulkDeleteFailures"></a> synapselinkprofile_BulkDeleteFailures

**Added by**: Synapse Link Solution

See the [synapselinkprofile_BulkDeleteFailures](synapselinkprofile.md#BKMK_synapselinkprofile_BulkDeleteFailures) one-to-many relationship for the [synapselinkprofile](synapselinkprofile.md) table/entity.

### <a name="BKMK_synapselinkprofileentity_BulkDeleteFailures"></a> synapselinkprofileentity_BulkDeleteFailures

**Added by**: Synapse Link Solution

See the [synapselinkprofileentity_BulkDeleteFailures](synapselinkprofileentity.md#BKMK_synapselinkprofileentity_BulkDeleteFailures) one-to-many relationship for the [synapselinkprofileentity](synapselinkprofileentity.md) table/entity.

### <a name="BKMK_synapselinkprofileentitystate_BulkDeleteFailures"></a> synapselinkprofileentitystate_BulkDeleteFailures

**Added by**: Synapse Link Solution

See the [synapselinkprofileentitystate_BulkDeleteFailures](synapselinkprofileentitystate.md#BKMK_synapselinkprofileentitystate_BulkDeleteFailures) one-to-many relationship for the [synapselinkprofileentitystate](synapselinkprofileentitystate.md) table/entity.

### <a name="BKMK_synapselinkschedule_BulkDeleteFailures"></a> synapselinkschedule_BulkDeleteFailures

**Added by**: Synapse Link Solution

See the [synapselinkschedule_BulkDeleteFailures](synapselinkschedule.md#BKMK_synapselinkschedule_BulkDeleteFailures) one-to-many relationship for the [synapselinkschedule](synapselinkschedule.md) table/entity.

### <a name="BKMK_msdyn_dataflow_BulkDeleteFailures"></a> msdyn_dataflow_BulkDeleteFailures

**Added by**: Dataflow Solution Solution

See the [msdyn_dataflow_BulkDeleteFailures](msdyn_dataflow.md#BKMK_msdyn_dataflow_BulkDeleteFailures) one-to-many relationship for the [msdyn_dataflow](msdyn_dataflow.md) table/entity.

### <a name="BKMK_msdyn_dataflowrefreshhistory_BulkDeleteFailures"></a> msdyn_dataflowrefreshhistory_BulkDeleteFailures

**Added by**: Dataflow Solution Solution

See the [msdyn_dataflowrefreshhistory_BulkDeleteFailures](msdyn_dataflowrefreshhistory.md#BKMK_msdyn_dataflowrefreshhistory_BulkDeleteFailures) one-to-many relationship for the [msdyn_dataflowrefreshhistory](msdyn_dataflowrefreshhistory.md) table/entity.

### <a name="BKMK_msdyn_entityrefreshhistory_BulkDeleteFailures"></a> msdyn_entityrefreshhistory_BulkDeleteFailures

**Added by**: Dataflow Solution Solution

See the [msdyn_entityrefreshhistory_BulkDeleteFailures](msdyn_entityrefreshhistory.md#BKMK_msdyn_entityrefreshhistory_BulkDeleteFailures) one-to-many relationship for the [msdyn_entityrefreshhistory](msdyn_entityrefreshhistory.md) table/entity.

### <a name="BKMK_sharedlinksetting_BulkDeleteFailures"></a> sharedlinksetting_BulkDeleteFailures

**Added by**: Access Team Solution

See the [sharedlinksetting_BulkDeleteFailures](sharedlinksetting.md#BKMK_sharedlinksetting_BulkDeleteFailures) one-to-many relationship for the [sharedlinksetting](sharedlinksetting.md) table/entity.

### <a name="BKMK_entityrecordfilter_BulkDeleteFailures"></a> entityrecordfilter_BulkDeleteFailures

**Added by**: AuthorizationCore Solution

See the [entityrecordfilter_BulkDeleteFailures](entityrecordfilter.md#BKMK_entityrecordfilter_BulkDeleteFailures) one-to-many relationship for the [entityrecordfilter](entityrecordfilter.md) table/entity.

### <a name="BKMK_recordfilter_BulkDeleteFailures"></a> recordfilter_BulkDeleteFailures

**Added by**: AuthorizationCore Solution

See the [recordfilter_BulkDeleteFailures](recordfilter.md#BKMK_recordfilter_BulkDeleteFailures) one-to-many relationship for the [recordfilter](recordfilter.md) table/entity.

### <a name="BKMK_delegatedauthorization_BulkDeleteFailures"></a> delegatedauthorization_BulkDeleteFailures

**Added by**: Delegated Authorization Solution

See the [delegatedauthorization_BulkDeleteFailures](delegatedauthorization.md#BKMK_delegatedauthorization_BulkDeleteFailures) one-to-many relationship for the [delegatedauthorization](delegatedauthorization.md) table/entity.

### <a name="BKMK_serviceplan_BulkDeleteFailures"></a> serviceplan_BulkDeleteFailures

**Added by**: License Enforcement Solution

See the [serviceplan_BulkDeleteFailures](serviceplan.md#BKMK_serviceplan_BulkDeleteFailures) one-to-many relationship for the [serviceplan](serviceplan.md) table/entity.

### <a name="BKMK_serviceplanmapping_BulkDeleteFailures"></a> serviceplanmapping_BulkDeleteFailures

**Added by**: License Enforcement Solution

See the [serviceplanmapping_BulkDeleteFailures](serviceplanmapping.md#BKMK_serviceplanmapping_BulkDeleteFailures) one-to-many relationship for the [serviceplanmapping](serviceplanmapping.md) table/entity.

### <a name="BKMK_applicationuser_BulkDeleteFailures"></a> applicationuser_BulkDeleteFailures

**Added by**: ApplicationUserSolution Solution

See the [applicationuser_BulkDeleteFailures](applicationuser.md#BKMK_applicationuser_BulkDeleteFailures) one-to-many relationship for the [applicationuser](applicationuser.md) table/entity.

### <a name="BKMK_connector_BulkDeleteFailures"></a> connector_BulkDeleteFailures

**Added by**: Power Connector Solution Solution

See the [connector_BulkDeleteFailures](connector.md#BKMK_connector_BulkDeleteFailures) one-to-many relationship for the [connector](connector.md) table/entity.

### <a name="BKMK_environmentvariabledefinition_BulkDeleteFailures"></a> environmentvariabledefinition_BulkDeleteFailures

**Added by**: Environment Variables Solution

See the [environmentvariabledefinition_BulkDeleteFailures](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_BulkDeleteFailures) one-to-many relationship for the [environmentvariabledefinition](environmentvariabledefinition.md) table/entity.

### <a name="BKMK_environmentvariablevalue_BulkDeleteFailures"></a> environmentvariablevalue_BulkDeleteFailures

**Added by**: Environment Variables Solution

See the [environmentvariablevalue_BulkDeleteFailures](environmentvariablevalue.md#BKMK_environmentvariablevalue_BulkDeleteFailures) one-to-many relationship for the [environmentvariablevalue](environmentvariablevalue.md) table/entity.

### <a name="BKMK_workflowbinary_BulkDeleteFailures"></a> workflowbinary_BulkDeleteFailures

**Added by**: Power Automate Extensions Workflow Binary package Solution

See the [workflowbinary_BulkDeleteFailures](workflowbinary.md#BKMK_workflowbinary_BulkDeleteFailures) one-to-many relationship for the [workflowbinary](workflowbinary.md) table/entity.

### <a name="BKMK_desktopflowmodule_BulkDeleteFailures"></a> desktopflowmodule_BulkDeleteFailures

**Added by**: Power Automate Extensions core package Solution

See the [desktopflowmodule_BulkDeleteFailures](desktopflowmodule.md#BKMK_desktopflowmodule_BulkDeleteFailures) one-to-many relationship for the [desktopflowmodule](desktopflowmodule.md) table/entity.

### <a name="BKMK_flowmachine_BulkDeleteFailures"></a> flowmachine_BulkDeleteFailures

**Added by**: Power Automate Extensions core package Solution

See the [flowmachine_BulkDeleteFailures](flowmachine.md#BKMK_flowmachine_BulkDeleteFailures) one-to-many relationship for the [flowmachine](flowmachine.md) table/entity.

### <a name="BKMK_flowmachinegroup_BulkDeleteFailures"></a> flowmachinegroup_BulkDeleteFailures

**Added by**: Power Automate Extensions core package Solution

See the [flowmachinegroup_BulkDeleteFailures](flowmachinegroup.md#BKMK_flowmachinegroup_BulkDeleteFailures) one-to-many relationship for the [flowmachinegroup](flowmachinegroup.md) table/entity.

### <a name="BKMK_flowmachineimage_BulkDeleteFailures"></a> flowmachineimage_BulkDeleteFailures

**Added by**: Power Automate Extensions core package Solution

See the [flowmachineimage_BulkDeleteFailures](flowmachineimage.md#BKMK_flowmachineimage_BulkDeleteFailures) one-to-many relationship for the [flowmachineimage](flowmachineimage.md) table/entity.

### <a name="BKMK_flowmachineimageversion_BulkDeleteFailures"></a> flowmachineimageversion_BulkDeleteFailures

**Added by**: Power Automate Extensions core package Solution

See the [flowmachineimageversion_BulkDeleteFailures](flowmachineimageversion.md#BKMK_flowmachineimageversion_BulkDeleteFailures) one-to-many relationship for the [flowmachineimageversion](flowmachineimageversion.md) table/entity.

### <a name="BKMK_flowmachinenetwork_BulkDeleteFailures"></a> flowmachinenetwork_BulkDeleteFailures

**Added by**: Power Automate Extensions core package Solution

See the [flowmachinenetwork_BulkDeleteFailures](flowmachinenetwork.md#BKMK_flowmachinenetwork_BulkDeleteFailures) one-to-many relationship for the [flowmachinenetwork](flowmachinenetwork.md) table/entity.

### <a name="BKMK_processstageparameter_BulkDeleteFailures"></a> processstageparameter_BulkDeleteFailures

**Added by**: Power Automate Extensions core package Solution

See the [processstageparameter_BulkDeleteFailures](processstageparameter.md#BKMK_processstageparameter_BulkDeleteFailures) one-to-many relationship for the [processstageparameter](processstageparameter.md) table/entity.

### <a name="BKMK_workqueue_BulkDeleteFailures"></a> workqueue_BulkDeleteFailures

**Added by**: Power Automate Extensions core package Solution

See the [workqueue_BulkDeleteFailures](workqueue.md#BKMK_workqueue_BulkDeleteFailures) one-to-many relationship for the [workqueue](workqueue.md) table/entity.

### <a name="BKMK_workqueueitem_BulkDeleteFailures"></a> workqueueitem_BulkDeleteFailures

**Added by**: Power Automate Extensions core package Solution

See the [workqueueitem_BulkDeleteFailures](workqueueitem.md#BKMK_workqueueitem_BulkDeleteFailures) one-to-many relationship for the [workqueueitem](workqueueitem.md) table/entity.

### <a name="BKMK_desktopflowbinary_BulkDeleteFailures"></a> desktopflowbinary_BulkDeleteFailures

**Added by**: Power Automate Extensions core package Solution

See the [desktopflowbinary_BulkDeleteFailures](desktopflowbinary.md#BKMK_desktopflowbinary_BulkDeleteFailures) one-to-many relationship for the [desktopflowbinary](desktopflowbinary.md) table/entity.

### <a name="BKMK_flowsession_BulkDeleteFailures"></a> flowsession_BulkDeleteFailures

**Added by**: Power Automate Extensions core package Solution

See the [flowsession_BulkDeleteFailures](flowsession.md#BKMK_flowsession_BulkDeleteFailures) one-to-many relationship for the [flowsession](flowsession.md) table/entity.

### <a name="BKMK_connectionreference_BulkDeleteFailures"></a> connectionreference_BulkDeleteFailures

**Added by**: Power Platform Connection References Solution

See the [connectionreference_BulkDeleteFailures](connectionreference.md#BKMK_connectionreference_BulkDeleteFailures) one-to-many relationship for the [connectionreference](connectionreference.md) table/entity.

### <a name="BKMK_connectioninstance_BulkDeleteFailures"></a> connectioninstance_BulkDeleteFailures

**Added by**: Connection Instance Solution Solution

See the [connectioninstance_BulkDeleteFailures](connectioninstance.md#BKMK_connectioninstance_BulkDeleteFailures) one-to-many relationship for the [connectioninstance](connectioninstance.md) table/entity.

### <a name="BKMK_msdyn_helppage_BulkDeleteFailures"></a> msdyn_helppage_BulkDeleteFailures

**Added by**: Contextual Help Solution

See the [msdyn_helppage_BulkDeleteFailures](msdyn_helppage.md#BKMK_msdyn_helppage_BulkDeleteFailures) one-to-many relationship for the [msdyn_helppage](msdyn_helppage.md) table/entity.

### <a name="BKMK_msdyn_tour_BulkDeleteFailures"></a> msdyn_tour_BulkDeleteFailures

**Added by**: Contextual Help Solution

See the [msdyn_tour_BulkDeleteFailures](msdyn_tour.md#BKMK_msdyn_tour_BulkDeleteFailures) one-to-many relationship for the [msdyn_tour](msdyn_tour.md) table/entity.

### <a name="BKMK_msdynce_botcontent_BulkDeleteFailures"></a> msdynce_botcontent_BulkDeleteFailures

**Added by**: Customer Care Intelligence Bots Solution

See the [msdynce_botcontent_BulkDeleteFailures](msdynce_botcontent.md#BKMK_msdynce_botcontent_BulkDeleteFailures) one-to-many relationship for the [msdynce_botcontent](msdynce_botcontent.md) table/entity.

### <a name="BKMK_conversationtranscript_BulkDeleteFailures"></a> conversationtranscript_BulkDeleteFailures

**Added by**: Power Virtual Agents Common Solution

See the [conversationtranscript_BulkDeleteFailures](conversationtranscript.md#BKMK_conversationtranscript_BulkDeleteFailures) one-to-many relationship for the [conversationtranscript](conversationtranscript.md) table/entity.

### <a name="BKMK_bot_BulkDeleteFailures"></a> bot_BulkDeleteFailures

**Added by**: Power Virtual Agents Solution

See the [bot_BulkDeleteFailures](bot.md#BKMK_bot_BulkDeleteFailures) one-to-many relationship for the [bot](bot.md) table/entity.

### <a name="BKMK_botcomponent_BulkDeleteFailures"></a> botcomponent_BulkDeleteFailures

**Added by**: Power Virtual Agents Solution

See the [botcomponent_BulkDeleteFailures](botcomponent.md#BKMK_botcomponent_BulkDeleteFailures) one-to-many relationship for the [botcomponent](botcomponent.md) table/entity.

### <a name="BKMK_Territory_BulkDeleteFailures"></a> Territory_BulkDeleteFailures

**Added by**: Application Common Solution

See the [Territory_BulkDeleteFailures](territory.md#BKMK_Territory_BulkDeleteFailures) one-to-many relationship for the [territory](territory.md) table/entity.

### <a name="BKMK_activityfileattachment_BulkDeleteFailures"></a> activityfileattachment_BulkDeleteFailures

**Added by**: Activities Patch Solution

See the [activityfileattachment_BulkDeleteFailures](activityfileattachment.md#BKMK_activityfileattachment_BulkDeleteFailures) one-to-many relationship for the [activityfileattachment](activityfileattachment.md) table/entity.

### <a name="BKMK_chat_BulkDeleteFailures"></a> chat_BulkDeleteFailures

**Added by**: Activities Patch Solution

See the [chat_BulkDeleteFailures](chat.md#BKMK_chat_BulkDeleteFailures) one-to-many relationship for the [chat](chat.md) table/entity.

### <a name="BKMK_msdyn_serviceconfiguration_BulkDeleteFailures"></a> msdyn_serviceconfiguration_BulkDeleteFailures

**Added by**: Service Level Agreement (SLA) Extension Solution

See the [msdyn_serviceconfiguration_BulkDeleteFailures](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_BulkDeleteFailures) one-to-many relationship for the [msdyn_serviceconfiguration](msdyn_serviceconfiguration.md) table/entity.

### <a name="BKMK_msdyn_slakpi_BulkDeleteFailures"></a> msdyn_slakpi_BulkDeleteFailures

**Added by**: Service Level Agreement (SLA) Extension Solution

See the [msdyn_slakpi_BulkDeleteFailures](msdyn_slakpi.md#BKMK_msdyn_slakpi_BulkDeleteFailures) one-to-many relationship for the [msdyn_slakpi](msdyn_slakpi.md) table/entity.

### <a name="BKMK_msdyn_knowledgemanagementsetting_BulkDeleteFailures"></a> msdyn_knowledgemanagementsetting_BulkDeleteFailures

**Added by**: Knowledge Management Patch Solution

See the [msdyn_knowledgemanagementsetting_BulkDeleteFailures](msdyn_knowledgemanagementsetting.md#BKMK_msdyn_knowledgemanagementsetting_BulkDeleteFailures) one-to-many relationship for the [msdyn_knowledgemanagementsetting](msdyn_knowledgemanagementsetting.md) table/entity.

### <a name="BKMK_msdyn_federatedarticle_BulkDeleteFailures"></a> msdyn_federatedarticle_BulkDeleteFailures

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_federatedarticle_BulkDeleteFailures](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_BulkDeleteFailures) one-to-many relationship for the [msdyn_federatedarticle](msdyn_federatedarticle.md) table/entity.

### <a name="BKMK_msdyn_federatedarticleincident_BulkDeleteFailures"></a> msdyn_federatedarticleincident_BulkDeleteFailures

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_federatedarticleincident_BulkDeleteFailures](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_BulkDeleteFailures) one-to-many relationship for the [msdyn_federatedarticleincident](msdyn_federatedarticleincident.md) table/entity.

### <a name="BKMK_msdyn_integratedsearchprovider_BulkDeleteFailures"></a> msdyn_integratedsearchprovider_BulkDeleteFailures

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_integratedsearchprovider_BulkDeleteFailures](msdyn_integratedsearchprovider.md#BKMK_msdyn_integratedsearchprovider_BulkDeleteFailures) one-to-many relationship for the [msdyn_integratedsearchprovider](msdyn_integratedsearchprovider.md) table/entity.

### <a name="BKMK_msdyn_kmfederatedsearchconfig_BulkDeleteFailures"></a> msdyn_kmfederatedsearchconfig_BulkDeleteFailures

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_kmfederatedsearchconfig_BulkDeleteFailures](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_BulkDeleteFailures) one-to-many relationship for the [msdyn_kmfederatedsearchconfig](msdyn_kmfederatedsearchconfig.md) table/entity.

### <a name="BKMK_msdyn_knowledgearticleimage_BulkDeleteFailures"></a> msdyn_knowledgearticleimage_BulkDeleteFailures

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgearticleimage_BulkDeleteFailures](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_BulkDeleteFailures) one-to-many relationship for the [msdyn_knowledgearticleimage](msdyn_knowledgearticleimage.md) table/entity.

### <a name="BKMK_msdyn_knowledgeconfiguration_BulkDeleteFailures"></a> msdyn_knowledgeconfiguration_BulkDeleteFailures

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgeconfiguration_BulkDeleteFailures](msdyn_knowledgeconfiguration.md#BKMK_msdyn_knowledgeconfiguration_BulkDeleteFailures) one-to-many relationship for the [msdyn_knowledgeconfiguration](msdyn_knowledgeconfiguration.md) table/entity.

### <a name="BKMK_msdyn_knowledgeinteractioninsight_BulkDeleteFailures"></a> msdyn_knowledgeinteractioninsight_BulkDeleteFailures

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgeinteractioninsight_BulkDeleteFailures](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_BulkDeleteFailures) one-to-many relationship for the [msdyn_knowledgeinteractioninsight](msdyn_knowledgeinteractioninsight.md) table/entity.

### <a name="BKMK_msdyn_knowledgesearchinsight_BulkDeleteFailures"></a> msdyn_knowledgesearchinsight_BulkDeleteFailures

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgesearchinsight_BulkDeleteFailures](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_BulkDeleteFailures) one-to-many relationship for the [msdyn_knowledgesearchinsight](msdyn_knowledgesearchinsight.md) table/entity.

### <a name="BKMK_msdyn_favoriteknowledgearticle_BulkDeleteFailures"></a> msdyn_favoriteknowledgearticle_BulkDeleteFailures

**Added by**: Knowledge Management Features Solution

See the [msdyn_favoriteknowledgearticle_BulkDeleteFailures](msdyn_favoriteknowledgearticle.md#BKMK_msdyn_favoriteknowledgearticle_BulkDeleteFailures) one-to-many relationship for the [msdyn_favoriteknowledgearticle](msdyn_favoriteknowledgearticle.md) table/entity.

### <a name="BKMK_msdyn_kalanguagesetting_BulkDeleteFailures"></a> msdyn_kalanguagesetting_BulkDeleteFailures

**Added by**: Knowledge Management Features Solution

See the [msdyn_kalanguagesetting_BulkDeleteFailures](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_BulkDeleteFailures) one-to-many relationship for the [msdyn_kalanguagesetting](msdyn_kalanguagesetting.md) table/entity.

### <a name="BKMK_msdyn_kbattachment_BulkDeleteFailures"></a> msdyn_kbattachment_BulkDeleteFailures

**Added by**: Knowledge Management Features Solution

See the [msdyn_kbattachment_BulkDeleteFailures](msdyn_kbattachment.md#BKMK_msdyn_kbattachment_BulkDeleteFailures) one-to-many relationship for the [msdyn_kbattachment](msdyn_kbattachment.md) table/entity.

### <a name="BKMK_msdyn_kmpersonalizationsetting_BulkDeleteFailures"></a> msdyn_kmpersonalizationsetting_BulkDeleteFailures

**Added by**: Knowledge Management Features Solution

See the [msdyn_kmpersonalizationsetting_BulkDeleteFailures](msdyn_kmpersonalizationsetting.md#BKMK_msdyn_kmpersonalizationsetting_BulkDeleteFailures) one-to-many relationship for the [msdyn_kmpersonalizationsetting](msdyn_kmpersonalizationsetting.md) table/entity.

### <a name="BKMK_msdyn_knowledgearticletemplate_BulkDeleteFailures"></a> msdyn_knowledgearticletemplate_BulkDeleteFailures

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgearticletemplate_BulkDeleteFailures](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_BulkDeleteFailures) one-to-many relationship for the [msdyn_knowledgearticletemplate](msdyn_knowledgearticletemplate.md) table/entity.

### <a name="BKMK_msdyn_knowledgepersonalfilter_BulkDeleteFailures"></a> msdyn_knowledgepersonalfilter_BulkDeleteFailures

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgepersonalfilter_BulkDeleteFailures](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_BulkDeleteFailures) one-to-many relationship for the [msdyn_knowledgepersonalfilter](msdyn_knowledgepersonalfilter.md) table/entity.

### <a name="BKMK_msdyn_knowledgesearchfilter_BulkDeleteFailures"></a> msdyn_knowledgesearchfilter_BulkDeleteFailures

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgesearchfilter_BulkDeleteFailures](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_BulkDeleteFailures) one-to-many relationship for the [msdyn_knowledgesearchfilter](msdyn_knowledgesearchfilter.md) table/entity.

### <a name="BKMK_pluginpackage_BulkDeleteFailures"></a> pluginpackage_BulkDeleteFailures

**Added by**: Plugin Infrastructure Extension Solution

See the [pluginpackage_BulkDeleteFailures](pluginpackage.md#BKMK_pluginpackage_BulkDeleteFailures) one-to-many relationship for the [pluginpackage](pluginpackage.md) table/entity.

### <a name="BKMK_fxexpression_BulkDeleteFailures"></a> fxexpression_BulkDeleteFailures

**Added by**: msft_PowerfxRuleSolution Solution

See the [fxexpression_BulkDeleteFailures](fxexpression.md#BKMK_fxexpression_BulkDeleteFailures) one-to-many relationship for the [fxexpression](fxexpression.md) table/entity.

### <a name="BKMK_powerfxrule_BulkDeleteFailures"></a> powerfxrule_BulkDeleteFailures

**Added by**: msft_PowerfxRuleSolution Solution

See the [powerfxrule_BulkDeleteFailures](powerfxrule.md#BKMK_powerfxrule_BulkDeleteFailures) one-to-many relationship for the [powerfxrule](powerfxrule.md) table/entity.

### <a name="BKMK_keyvaultreference_BulkDeleteFailures"></a> keyvaultreference_BulkDeleteFailures

**Added by**: ManagedIdentityExtensions Solution

See the [keyvaultreference_BulkDeleteFailures](keyvaultreference.md#BKMK_keyvaultreference_BulkDeleteFailures) one-to-many relationship for the [keyvaultreference](keyvaultreference.md) table/entity.

### <a name="BKMK_managedidentity_BulkDeleteFailures"></a> managedidentity_BulkDeleteFailures

**Added by**: ManagedIdentityExtensions Solution

See the [managedidentity_BulkDeleteFailures](managedidentity.md#BKMK_managedidentity_BulkDeleteFailures) one-to-many relationship for the [managedidentity](managedidentity.md) table/entity.

### <a name="BKMK_msgraphresourcetosubscription_BulkDeleteFailures"></a> msgraphresourcetosubscription_BulkDeleteFailures

**Added by**: msft_ActivitiesInfra_Extensions Solution

See the [msgraphresourcetosubscription_BulkDeleteFailures](msgraphresourcetosubscription.md#BKMK_msgraphresourcetosubscription_BulkDeleteFailures) one-to-many relationship for the [msgraphresourcetosubscription](msgraphresourcetosubscription.md) table/entity.

### <a name="BKMK_virtualentitymetadata_BulkDeleteFailures"></a> virtualentitymetadata_BulkDeleteFailures

**Added by**: RuntimeIntegration Solution

See the [virtualentitymetadata_BulkDeleteFailures](virtualentitymetadata.md#BKMK_virtualentitymetadata_BulkDeleteFailures) one-to-many relationship for the [virtualentitymetadata](virtualentitymetadata.md) table/entity.

### <a name="BKMK_mobileofflineprofileextension_BulkDeleteFailures"></a> mobileofflineprofileextension_BulkDeleteFailures

**Added by**: MobileOfflineProfileExtensionSolution Solution

See the [mobileofflineprofileextension_BulkDeleteFailures](mobileofflineprofileextension.md#BKMK_mobileofflineprofileextension_BulkDeleteFailures) one-to-many relationship for the [mobileofflineprofileextension](mobileofflineprofileextension.md) table/entity.

### <a name="BKMK_teammobileofflineprofilemembership_BulkDeleteFailures"></a> teammobileofflineprofilemembership_BulkDeleteFailures

**Added by**: MobileOfflineMembership Solution

See the [teammobileofflineprofilemembership_BulkDeleteFailures](teammobileofflineprofilemembership.md#BKMK_teammobileofflineprofilemembership_BulkDeleteFailures) one-to-many relationship for the [teammobileofflineprofilemembership](teammobileofflineprofilemembership.md) table/entity.

### <a name="BKMK_usermobileofflineprofilemembership_BulkDeleteFailures"></a> usermobileofflineprofilemembership_BulkDeleteFailures

**Added by**: MobileOfflineMembership Solution

See the [usermobileofflineprofilemembership_BulkDeleteFailures](usermobileofflineprofilemembership.md#BKMK_usermobileofflineprofilemembership_BulkDeleteFailures) one-to-many relationship for the [usermobileofflineprofilemembership](usermobileofflineprofilemembership.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscription_BulkDeleteFailures"></a> organizationdatasyncsubscription_BulkDeleteFailures

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscription_BulkDeleteFailures](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_BulkDeleteFailures) one-to-many relationship for the [organizationdatasyncsubscription](organizationdatasyncsubscription.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscriptionentity_BulkDeleteFailures"></a> organizationdatasyncsubscriptionentity_BulkDeleteFailures

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscriptionentity_BulkDeleteFailures](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_BulkDeleteFailures) one-to-many relationship for the [organizationdatasyncsubscriptionentity](organizationdatasyncsubscriptionentity.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_BulkDeleteFailures"></a> organizationdatasyncsubscriptionfnotable_BulkDeleteFailures

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscriptionfnotable_BulkDeleteFailures](organizationdatasyncsubscriptionfnotable.md#BKMK_organizationdatasyncsubscriptionfnotable_BulkDeleteFailures) one-to-many relationship for the [organizationdatasyncsubscriptionfnotable](organizationdatasyncsubscriptionfnotable.md) table/entity.

### <a name="BKMK_organizationdatasyncfnostate_BulkDeleteFailures"></a> organizationdatasyncfnostate_BulkDeleteFailures

**Added by**: DataSyncState Solution

See the [organizationdatasyncfnostate_BulkDeleteFailures](organizationdatasyncfnostate.md#BKMK_organizationdatasyncfnostate_BulkDeleteFailures) one-to-many relationship for the [organizationdatasyncfnostate](organizationdatasyncfnostate.md) table/entity.

### <a name="BKMK_organizationdatasyncstate_BulkDeleteFailures"></a> organizationdatasyncstate_BulkDeleteFailures

**Added by**: DataSyncState Solution

See the [organizationdatasyncstate_BulkDeleteFailures](organizationdatasyncstate.md#BKMK_organizationdatasyncstate_BulkDeleteFailures) one-to-many relationship for the [organizationdatasyncstate](organizationdatasyncstate.md) table/entity.

### <a name="BKMK_metadataforarchival_BulkDeleteFailures"></a> metadataforarchival_BulkDeleteFailures

**Added by**: Retention Base Components Solution

See the [metadataforarchival_BulkDeleteFailures](metadataforarchival.md#BKMK_metadataforarchival_BulkDeleteFailures) one-to-many relationship for the [metadataforarchival](metadataforarchival.md) table/entity.

### <a name="BKMK_retentionconfig_BulkDeleteFailures"></a> retentionconfig_BulkDeleteFailures

**Added by**: Retention Base Components Solution

See the [retentionconfig_BulkDeleteFailures](retentionconfig.md#BKMK_retentionconfig_BulkDeleteFailures) one-to-many relationship for the [retentionconfig](retentionconfig.md) table/entity.

### <a name="BKMK_retentionfailuredetail_BulkDeleteFailures"></a> retentionfailuredetail_BulkDeleteFailures

**Added by**: Retention Base Components Solution

See the [retentionfailuredetail_BulkDeleteFailures](retentionfailuredetail.md#BKMK_retentionfailuredetail_BulkDeleteFailures) one-to-many relationship for the [retentionfailuredetail](retentionfailuredetail.md) table/entity.

### <a name="BKMK_retentionoperation_BulkDeleteFailures"></a> retentionoperation_BulkDeleteFailures

**Added by**: Retention Base Components Solution

See the [retentionoperation_BulkDeleteFailures](retentionoperation.md#BKMK_retentionoperation_BulkDeleteFailures) one-to-many relationship for the [retentionoperation](retentionoperation.md) table/entity.

### <a name="BKMK_retentionoperationdetail_BulkDeleteFailures"></a> retentionoperationdetail_BulkDeleteFailures

**Added by**: Retention Base Components Solution

See the [retentionoperationdetail_BulkDeleteFailures](retentionoperationdetail.md#BKMK_retentionoperationdetail_BulkDeleteFailures) one-to-many relationship for the [retentionoperationdetail](retentionoperationdetail.md) table/entity.

### <a name="BKMK_msdyn_appinsightsmetadata_BulkDeleteFailures"></a> msdyn_appinsightsmetadata_BulkDeleteFailures

**Added by**: Insights App Platform Solution

See the [msdyn_appinsightsmetadata_BulkDeleteFailures](msdyn_appinsightsmetadata.md#BKMK_msdyn_appinsightsmetadata_BulkDeleteFailures) one-to-many relationship for the [msdyn_appinsightsmetadata](msdyn_appinsightsmetadata.md) table/entity.

### <a name="BKMK_msdyn_dataflowtemplate_BulkDeleteFailures"></a> msdyn_dataflowtemplate_BulkDeleteFailures

**Added by**: Insights App Platform Solution

See the [msdyn_dataflowtemplate_BulkDeleteFailures](msdyn_dataflowtemplate.md#BKMK_msdyn_dataflowtemplate_BulkDeleteFailures) one-to-many relationship for the [msdyn_dataflowtemplate](msdyn_dataflowtemplate.md) table/entity.

### <a name="BKMK_msdyn_workflowactionstatus_BulkDeleteFailures"></a> msdyn_workflowactionstatus_BulkDeleteFailures

**Added by**: Insights App Platform Solution

See the [msdyn_workflowactionstatus_BulkDeleteFailures](msdyn_workflowactionstatus.md#BKMK_msdyn_workflowactionstatus_BulkDeleteFailures) one-to-many relationship for the [msdyn_workflowactionstatus](msdyn_workflowactionstatus.md) table/entity.

### <a name="BKMK_userrating_BulkDeleteFailures"></a> userrating_BulkDeleteFailures

**Added by**: User Rating Solution

See the [userrating_BulkDeleteFailures](userrating.md#BKMK_userrating_BulkDeleteFailures) one-to-many relationship for the [userrating](userrating.md) table/entity.

### <a name="BKMK_msdyn_mobileapp_BulkDeleteFailures"></a> msdyn_mobileapp_BulkDeleteFailures

**Added by**: Mobile Apps Solution Solution

See the [msdyn_mobileapp_BulkDeleteFailures](msdyn_mobileapp.md#BKMK_msdyn_mobileapp_BulkDeleteFailures) one-to-many relationship for the [msdyn_mobileapp](msdyn_mobileapp.md) table/entity.

### <a name="BKMK_msdyn_insightsstorevirtualentity_BulkDeleteFailures"></a> msdyn_insightsstorevirtualentity_BulkDeleteFailures

**Added by**: Insights Store Data Provider Solution

See the [msdyn_insightsstorevirtualentity_BulkDeleteFailures](msdyn_insightsstorevirtualentity.md#BKMK_msdyn_insightsstorevirtualentity_BulkDeleteFailures) one-to-many relationship for the [msdyn_insightsstorevirtualentity](msdyn_insightsstorevirtualentity.md) table/entity.

### <a name="BKMK_roleeditorlayout_BulkDeleteFailures"></a> roleeditorlayout_BulkDeleteFailures

**Added by**: Role Editor Solution

See the [roleeditorlayout_BulkDeleteFailures](roleeditorlayout.md#BKMK_roleeditorlayout_BulkDeleteFailures) one-to-many relationship for the [roleeditorlayout](roleeditorlayout.md) table/entity.

### <a name="BKMK_appaction_BulkDeleteFailures"></a> appaction_BulkDeleteFailures

**Added by**: Power Apps Actions Solution

See the [appaction_BulkDeleteFailures](appaction.md#BKMK_appaction_BulkDeleteFailures) one-to-many relationship for the [appaction](appaction.md) table/entity.

### <a name="BKMK_appactionmigration_BulkDeleteFailures"></a> appactionmigration_BulkDeleteFailures

**Added by**: Power Apps Actions Solution

See the [appactionmigration_BulkDeleteFailures](appactionmigration.md#BKMK_appactionmigration_BulkDeleteFailures) one-to-many relationship for the [appactionmigration](appactionmigration.md) table/entity.

### <a name="BKMK_appactionrule_BulkDeleteFailures"></a> appactionrule_BulkDeleteFailures

**Added by**: Power Apps Actions Solution

See the [appactionrule_BulkDeleteFailures](appactionrule.md#BKMK_appactionrule_BulkDeleteFailures) one-to-many relationship for the [appactionrule](appactionrule.md) table/entity.

### <a name="BKMK_card_BulkDeleteFailures"></a> card_BulkDeleteFailures

**Added by**: Power Apps cards Solution

See the [card_BulkDeleteFailures](card.md#BKMK_card_BulkDeleteFailures) one-to-many relationship for the [card](card.md) table/entity.

### <a name="BKMK_msdyn_entitylinkchatconfiguration_BulkDeleteFailures"></a> msdyn_entitylinkchatconfiguration_BulkDeleteFailures

**Added by**: Teams Chat Settings Solution Solution

See the [msdyn_entitylinkchatconfiguration_BulkDeleteFailures](msdyn_entitylinkchatconfiguration.md#BKMK_msdyn_entitylinkchatconfiguration_BulkDeleteFailures) one-to-many relationship for the [msdyn_entitylinkchatconfiguration](msdyn_entitylinkchatconfiguration.md) table/entity.

### <a name="BKMK_msdyn_richtextfile_BulkDeleteFailures"></a> msdyn_richtextfile_BulkDeleteFailures

**Added by**: Rich Text Editor Solution

See the [msdyn_richtextfile_BulkDeleteFailures](msdyn_richtextfile.md#BKMK_msdyn_richtextfile_BulkDeleteFailures) one-to-many relationship for the [msdyn_richtextfile](msdyn_richtextfile.md) table/entity.

### <a name="BKMK_msdyn_customcontrolextendedsettings_BulkDeleteFailures"></a> msdyn_customcontrolextendedsettings_BulkDeleteFailures

**Added by**: User Experiences Extended Settings Solution

See the [msdyn_customcontrolextendedsettings_BulkDeleteFailures](msdyn_customcontrolextendedsettings.md#BKMK_msdyn_customcontrolextendedsettings_BulkDeleteFailures) one-to-many relationship for the [msdyn_customcontrolextendedsettings](msdyn_customcontrolextendedsettings.md) table/entity.

### <a name="BKMK_searchrelationshipsettings_BulkDeleteFailures"></a> searchrelationshipsettings_BulkDeleteFailures

**Added by**: msdyn_RelevanceSearch Solution

See the [searchrelationshipsettings_BulkDeleteFailures](searchrelationshipsettings.md#BKMK_searchrelationshipsettings_BulkDeleteFailures) one-to-many relationship for the [searchrelationshipsettings](searchrelationshipsettings.md) table/entity.

### <a name="BKMK_msdyn_virtualtablecolumncandidate_BulkDeleteFailures"></a> msdyn_virtualtablecolumncandidate_BulkDeleteFailures

**Added by**: Virtual Connector Provider Solution

See the [msdyn_virtualtablecolumncandidate_BulkDeleteFailures](msdyn_virtualtablecolumncandidate.md#BKMK_msdyn_virtualtablecolumncandidate_BulkDeleteFailures) one-to-many relationship for the [msdyn_virtualtablecolumncandidate](msdyn_virtualtablecolumncandidate.md) table/entity.

### <a name="BKMK_msdyn_aiconfiguration_BulkDeleteFailures"></a> msdyn_aiconfiguration_BulkDeleteFailures

**Added by**: AISolution Solution

See the [msdyn_aiconfiguration_BulkDeleteFailures](msdyn_aiconfiguration.md#BKMK_msdyn_aiconfiguration_BulkDeleteFailures) one-to-many relationship for the [msdyn_aiconfiguration](msdyn_aiconfiguration.md) table/entity.

### <a name="BKMK_msdyn_aievent_BulkDeleteFailures"></a> msdyn_aievent_BulkDeleteFailures

**Added by**: AISolution Solution

See the [msdyn_aievent_BulkDeleteFailures](msdyn_aievent.md#BKMK_msdyn_aievent_BulkDeleteFailures) one-to-many relationship for the [msdyn_aievent](msdyn_aievent.md) table/entity.

### <a name="BKMK_msdyn_aimodel_BulkDeleteFailures"></a> msdyn_aimodel_BulkDeleteFailures

**Added by**: AISolution Solution

See the [msdyn_aimodel_BulkDeleteFailures](msdyn_aimodel.md#BKMK_msdyn_aimodel_BulkDeleteFailures) one-to-many relationship for the [msdyn_aimodel](msdyn_aimodel.md) table/entity.

### <a name="BKMK_msdyn_aitemplate_BulkDeleteFailures"></a> msdyn_aitemplate_BulkDeleteFailures

**Added by**: AISolution Solution

See the [msdyn_aitemplate_BulkDeleteFailures](msdyn_aitemplate.md#BKMK_msdyn_aitemplate_BulkDeleteFailures) one-to-many relationship for the [msdyn_aitemplate](msdyn_aitemplate.md) table/entity.

### <a name="BKMK_msdyn_aibfeedbackloop_BulkDeleteFailures"></a> msdyn_aibfeedbackloop_BulkDeleteFailures

**Added by**: AISolutionFullAdditions Solution

See the [msdyn_aibfeedbackloop_BulkDeleteFailures](msdyn_aibfeedbackloop.md#BKMK_msdyn_aibfeedbackloop_BulkDeleteFailures) one-to-many relationship for the [msdyn_aibfeedbackloop](msdyn_aibfeedbackloop.md) table/entity.

### <a name="BKMK_msdyn_aifptrainingdocument_BulkDeleteFailures"></a> msdyn_aifptrainingdocument_BulkDeleteFailures

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aifptrainingdocument_BulkDeleteFailures](msdyn_aifptrainingdocument.md#BKMK_msdyn_aifptrainingdocument_BulkDeleteFailures) one-to-many relationship for the [msdyn_aifptrainingdocument](msdyn_aifptrainingdocument.md) table/entity.

### <a name="BKMK_msdyn_aiodimage_BulkDeleteFailures"></a> msdyn_aiodimage_BulkDeleteFailures

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodimage_BulkDeleteFailures](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_BulkDeleteFailures) one-to-many relationship for the [msdyn_aiodimage](msdyn_aiodimage.md) table/entity.

### <a name="BKMK_msdyn_aiodlabel_BulkDeleteFailures"></a> msdyn_aiodlabel_BulkDeleteFailures

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodlabel_BulkDeleteFailures](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_BulkDeleteFailures) one-to-many relationship for the [msdyn_aiodlabel](msdyn_aiodlabel.md) table/entity.

### <a name="BKMK_msdyn_aiodtrainingboundingbox_BulkDeleteFailures"></a> msdyn_aiodtrainingboundingbox_BulkDeleteFailures

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodtrainingboundingbox_BulkDeleteFailures](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_BulkDeleteFailures) one-to-many relationship for the [msdyn_aiodtrainingboundingbox](msdyn_aiodtrainingboundingbox.md) table/entity.

### <a name="BKMK_msdyn_aiodtrainingimage_BulkDeleteFailures"></a> msdyn_aiodtrainingimage_BulkDeleteFailures

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodtrainingimage_BulkDeleteFailures](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_BulkDeleteFailures) one-to-many relationship for the [msdyn_aiodtrainingimage](msdyn_aiodtrainingimage.md) table/entity.

### <a name="BKMK_msdyn_aibdataset_BulkDeleteFailures"></a> msdyn_aibdataset_BulkDeleteFailures

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdataset_BulkDeleteFailures](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_BulkDeleteFailures) one-to-many relationship for the [msdyn_aibdataset](msdyn_aibdataset.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetfile_BulkDeleteFailures"></a> msdyn_aibdatasetfile_BulkDeleteFailures

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetfile_BulkDeleteFailures](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_BulkDeleteFailures) one-to-many relationship for the [msdyn_aibdatasetfile](msdyn_aibdatasetfile.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetrecord_BulkDeleteFailures"></a> msdyn_aibdatasetrecord_BulkDeleteFailures

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetrecord_BulkDeleteFailures](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_BulkDeleteFailures) one-to-many relationship for the [msdyn_aibdatasetrecord](msdyn_aibdatasetrecord.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetscontainer_BulkDeleteFailures"></a> msdyn_aibdatasetscontainer_BulkDeleteFailures

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetscontainer_BulkDeleteFailures](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_BulkDeleteFailures) one-to-many relationship for the [msdyn_aibdatasetscontainer](msdyn_aibdatasetscontainer.md) table/entity.

### <a name="BKMK_msdyn_aibfile_BulkDeleteFailures"></a> msdyn_aibfile_BulkDeleteFailures

**Added by**: AI Solution default templates Solution

See the [msdyn_aibfile_BulkDeleteFailures](msdyn_aibfile.md#BKMK_msdyn_aibfile_BulkDeleteFailures) one-to-many relationship for the [msdyn_aibfile](msdyn_aibfile.md) table/entity.

### <a name="BKMK_msdyn_aibfileattacheddata_BulkDeleteFailures"></a> msdyn_aibfileattacheddata_BulkDeleteFailures

**Added by**: AI Solution default templates Solution

See the [msdyn_aibfileattacheddata_BulkDeleteFailures](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_BulkDeleteFailures) one-to-many relationship for the [msdyn_aibfileattacheddata](msdyn_aibfileattacheddata.md) table/entity.

### <a name="BKMK_msdyn_pmanalysishistory_BulkDeleteFailures"></a> msdyn_pmanalysishistory_BulkDeleteFailures

**Added by**: Process Mining Solution

See the [msdyn_pmanalysishistory_BulkDeleteFailures](msdyn_pmanalysishistory.md#BKMK_msdyn_pmanalysishistory_BulkDeleteFailures) one-to-many relationship for the [msdyn_pmanalysishistory](msdyn_pmanalysishistory.md) table/entity.

### <a name="BKMK_msdyn_pmcalendar_BulkDeleteFailures"></a> msdyn_pmcalendar_BulkDeleteFailures

**Added by**: Process Mining Solution

See the [msdyn_pmcalendar_BulkDeleteFailures](msdyn_pmcalendar.md#BKMK_msdyn_pmcalendar_BulkDeleteFailures) one-to-many relationship for the [msdyn_pmcalendar](msdyn_pmcalendar.md) table/entity.

### <a name="BKMK_msdyn_pmcalendarversion_BulkDeleteFailures"></a> msdyn_pmcalendarversion_BulkDeleteFailures

**Added by**: Process Mining Solution

See the [msdyn_pmcalendarversion_BulkDeleteFailures](msdyn_pmcalendarversion.md#BKMK_msdyn_pmcalendarversion_BulkDeleteFailures) one-to-many relationship for the [msdyn_pmcalendarversion](msdyn_pmcalendarversion.md) table/entity.

### <a name="BKMK_msdyn_pminferredtask_BulkDeleteFailures"></a> msdyn_pminferredtask_BulkDeleteFailures

**Added by**: Process Mining Solution

See the [msdyn_pminferredtask_BulkDeleteFailures](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_BulkDeleteFailures) one-to-many relationship for the [msdyn_pminferredtask](msdyn_pminferredtask.md) table/entity.

### <a name="BKMK_msdyn_pmprocessextendedmetadataversion_BulkDeleteFailures"></a> msdyn_pmprocessextendedmetadataversion_BulkDeleteFailures

**Added by**: Process Mining Solution

See the [msdyn_pmprocessextendedmetadataversion_BulkDeleteFailures](msdyn_pmprocessextendedmetadataversion.md#BKMK_msdyn_pmprocessextendedmetadataversion_BulkDeleteFailures) one-to-many relationship for the [msdyn_pmprocessextendedmetadataversion](msdyn_pmprocessextendedmetadataversion.md) table/entity.

### <a name="BKMK_msdyn_pmprocesstemplate_BulkDeleteFailures"></a> msdyn_pmprocesstemplate_BulkDeleteFailures

**Added by**: Process Mining Solution

See the [msdyn_pmprocesstemplate_BulkDeleteFailures](msdyn_pmprocesstemplate.md#BKMK_msdyn_pmprocesstemplate_BulkDeleteFailures) one-to-many relationship for the [msdyn_pmprocesstemplate](msdyn_pmprocesstemplate.md) table/entity.

### <a name="BKMK_msdyn_pmprocessusersettings_BulkDeleteFailures"></a> msdyn_pmprocessusersettings_BulkDeleteFailures

**Added by**: Process Mining Solution

See the [msdyn_pmprocessusersettings_BulkDeleteFailures](msdyn_pmprocessusersettings.md#BKMK_msdyn_pmprocessusersettings_BulkDeleteFailures) one-to-many relationship for the [msdyn_pmprocessusersettings](msdyn_pmprocessusersettings.md) table/entity.

### <a name="BKMK_msdyn_pmprocessversion_BulkDeleteFailures"></a> msdyn_pmprocessversion_BulkDeleteFailures

**Added by**: Process Mining Solution

See the [msdyn_pmprocessversion_BulkDeleteFailures](msdyn_pmprocessversion.md#BKMK_msdyn_pmprocessversion_BulkDeleteFailures) one-to-many relationship for the [msdyn_pmprocessversion](msdyn_pmprocessversion.md) table/entity.

### <a name="BKMK_msdyn_pmrecording_BulkDeleteFailures"></a> msdyn_pmrecording_BulkDeleteFailures

**Added by**: Process Mining Solution

See the [msdyn_pmrecording_BulkDeleteFailures](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_BulkDeleteFailures) one-to-many relationship for the [msdyn_pmrecording](msdyn_pmrecording.md) table/entity.

### <a name="BKMK_msdyn_pmtemplate_BulkDeleteFailures"></a> msdyn_pmtemplate_BulkDeleteFailures

**Added by**: Process Mining Solution

See the [msdyn_pmtemplate_BulkDeleteFailures](msdyn_pmtemplate.md#BKMK_msdyn_pmtemplate_BulkDeleteFailures) one-to-many relationship for the [msdyn_pmtemplate](msdyn_pmtemplate.md) table/entity.

### <a name="BKMK_msdyn_pmview_BulkDeleteFailures"></a> msdyn_pmview_BulkDeleteFailures

**Added by**: Process Mining Solution

See the [msdyn_pmview_BulkDeleteFailures](msdyn_pmview.md#BKMK_msdyn_pmview_BulkDeleteFailures) one-to-many relationship for the [msdyn_pmview](msdyn_pmview.md) table/entity.

### <a name="BKMK_msdyn_analysiscomponent_BulkDeleteFailures"></a> msdyn_analysiscomponent_BulkDeleteFailures

**Added by**: Power Apps Checker Solution

See the [msdyn_analysiscomponent_BulkDeleteFailures](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_BulkDeleteFailures) one-to-many relationship for the [msdyn_analysiscomponent](msdyn_analysiscomponent.md) table/entity.

### <a name="BKMK_msdyn_analysisjob_BulkDeleteFailures"></a> msdyn_analysisjob_BulkDeleteFailures

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisjob_BulkDeleteFailures](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_BulkDeleteFailures) one-to-many relationship for the [msdyn_analysisjob](msdyn_analysisjob.md) table/entity.

### <a name="BKMK_msdyn_analysisoverride_BulkDeleteFailures"></a> msdyn_analysisoverride_BulkDeleteFailures

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisoverride_BulkDeleteFailures](msdyn_analysisoverride.md#BKMK_msdyn_analysisoverride_BulkDeleteFailures) one-to-many relationship for the [msdyn_analysisoverride](msdyn_analysisoverride.md) table/entity.

### <a name="BKMK_msdyn_analysisresult_BulkDeleteFailures"></a> msdyn_analysisresult_BulkDeleteFailures

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisresult_BulkDeleteFailures](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_BulkDeleteFailures) one-to-many relationship for the [msdyn_analysisresult](msdyn_analysisresult.md) table/entity.

### <a name="BKMK_msdyn_analysisresultdetail_BulkDeleteFailures"></a> msdyn_analysisresultdetail_BulkDeleteFailures

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisresultdetail_BulkDeleteFailures](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_BulkDeleteFailures) one-to-many relationship for the [msdyn_analysisresultdetail](msdyn_analysisresultdetail.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthrule_BulkDeleteFailures"></a> msdyn_solutionhealthrule_BulkDeleteFailures

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthrule_BulkDeleteFailures](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_BulkDeleteFailures) one-to-many relationship for the [msdyn_solutionhealthrule](msdyn_solutionhealthrule.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthruleargument_BulkDeleteFailures"></a> msdyn_solutionhealthruleargument_BulkDeleteFailures

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthruleargument_BulkDeleteFailures](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_BulkDeleteFailures) one-to-many relationship for the [msdyn_solutionhealthruleargument](msdyn_solutionhealthruleargument.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthruleset_BulkDeleteFailures"></a> msdyn_solutionhealthruleset_BulkDeleteFailures

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthruleset_BulkDeleteFailures](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_BulkDeleteFailures) one-to-many relationship for the [msdyn_solutionhealthruleset](msdyn_solutionhealthruleset.md) table/entity.

### <a name="BKMK_powerbidataset_BulkDeleteFailures"></a> powerbidataset_BulkDeleteFailures

**Added by**: Power BI Entities Solution

See the [powerbidataset_BulkDeleteFailures](powerbidataset.md#BKMK_powerbidataset_BulkDeleteFailures) one-to-many relationship for the [powerbidataset](powerbidataset.md) table/entity.

### <a name="BKMK_powerbimashupparameter_BulkDeleteFailures"></a> powerbimashupparameter_BulkDeleteFailures

**Added by**: Power BI Entities Solution

See the [powerbimashupparameter_BulkDeleteFailures](powerbimashupparameter.md#BKMK_powerbimashupparameter_BulkDeleteFailures) one-to-many relationship for the [powerbimashupparameter](powerbimashupparameter.md) table/entity.

### <a name="BKMK_powerbireport_BulkDeleteFailures"></a> powerbireport_BulkDeleteFailures

**Added by**: Power BI Entities Solution

See the [powerbireport_BulkDeleteFailures](powerbireport.md#BKMK_powerbireport_BulkDeleteFailures) one-to-many relationship for the [powerbireport](powerbireport.md) table/entity.

### <a name="BKMK_msdyn_fileupload_BulkDeleteFailures"></a> msdyn_fileupload_BulkDeleteFailures

**Added by**: Smart Data Import Base Solution

See the [msdyn_fileupload_BulkDeleteFailures](msdyn_fileupload.md#BKMK_msdyn_fileupload_BulkDeleteFailures) one-to-many relationship for the [msdyn_fileupload](msdyn_fileupload.md) table/entity.

### <a name="BKMK_mspcat_catalogsubmissionfiles_BulkDeleteFailures"></a> mspcat_catalogsubmissionfiles_BulkDeleteFailures

**Added by**: Power Platform Catalog Client Packaging Solution

See the [mspcat_catalogsubmissionfiles_BulkDeleteFailures](mspcat_catalogsubmissionfiles.md#BKMK_mspcat_catalogsubmissionfiles_BulkDeleteFailures) one-to-many relationship for the [mspcat_catalogsubmissionfiles](mspcat_catalogsubmissionfiles.md) table/entity.

### <a name="BKMK_mspcat_packagestore_BulkDeleteFailures"></a> mspcat_packagestore_BulkDeleteFailures

**Added by**: Power Platform Catalog Client Packaging Solution

See the [mspcat_packagestore_BulkDeleteFailures](mspcat_packagestore.md#BKMK_mspcat_packagestore_BulkDeleteFailures) one-to-many relationship for the [mspcat_packagestore](mspcat_packagestore.md) table/entity.

### <a name="BKMK_msdyn_schedule_BulkDeleteFailures"></a> msdyn_schedule_BulkDeleteFailures

**Added by**: Insights App Platform Solution

See the [msdyn_schedule_BulkDeleteFailures](msdyn_schedule.md#BKMK_msdyn_schedule_BulkDeleteFailures) one-to-many relationship for the [msdyn_schedule](msdyn_schedule.md) table/entity.

### <a name="BKMK_msdyn_dataflow_datalakefolder_BulkDeleteFailures"></a> msdyn_dataflow_datalakefolder_BulkDeleteFailures

**Added by**: Insights App Platform Solution

See the [msdyn_dataflow_datalakefolder_BulkDeleteFailures](msdyn_dataflow_datalakefolder.md#BKMK_msdyn_dataflow_datalakefolder_BulkDeleteFailures) one-to-many relationship for the [msdyn_dataflow_datalakefolder](msdyn_dataflow_datalakefolder.md) table/entity.

### <a name="BKMK_msdyn_dmsrequest_BulkDeleteFailures"></a> msdyn_dmsrequest_BulkDeleteFailures

**Added by**: Insights App Platform Solution

See the [msdyn_dmsrequest_BulkDeleteFailures](msdyn_dmsrequest.md#BKMK_msdyn_dmsrequest_BulkDeleteFailures) one-to-many relationship for the [msdyn_dmsrequest](msdyn_dmsrequest.md) table/entity.

### <a name="BKMK_msdyn_dmsrequeststatus_BulkDeleteFailures"></a> msdyn_dmsrequeststatus_BulkDeleteFailures

**Added by**: Insights App Platform Solution

See the [msdyn_dmsrequeststatus_BulkDeleteFailures](msdyn_dmsrequeststatus.md#BKMK_msdyn_dmsrequeststatus_BulkDeleteFailures) one-to-many relationship for the [msdyn_dmsrequeststatus](msdyn_dmsrequeststatus.md) table/entity.

### <a name="BKMK_searchattributesettings_BulkDeleteFailures"></a> searchattributesettings_BulkDeleteFailures

**Added by**: msdyn_RelevanceSearch Solution

See the [searchattributesettings_BulkDeleteFailures](searchattributesettings.md#BKMK_searchattributesettings_BulkDeleteFailures) one-to-many relationship for the [searchattributesettings](searchattributesettings.md) table/entity.

### <a name="BKMK_searchcustomanalyzer_BulkDeleteFailures"></a> searchcustomanalyzer_BulkDeleteFailures

**Added by**: msdyn_RelevanceSearch Solution

See the [searchcustomanalyzer_BulkDeleteFailures](searchcustomanalyzer.md#BKMK_searchcustomanalyzer_BulkDeleteFailures) one-to-many relationship for the [searchcustomanalyzer](searchcustomanalyzer.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.bulkdeletefailure?text=bulkdeletefailure EntityType" />