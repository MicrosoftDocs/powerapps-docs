---
title: "Field Sharing (PrincipalObjectAttributeAccess)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Field Sharing (PrincipalObjectAttributeAccess)  table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Field Sharing (PrincipalObjectAttributeAccess)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Defines CRM security principals (users and teams) access rights to secured field for an entity instance.


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST /principalobjectattributeaccessset<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE /principalobjectattributeaccessset(*principalobjectattributeaccessid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET /principalobjectattributeaccessset(*principalobjectattributeaccessid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /principalobjectattributeaccessset<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH /principalobjectattributeaccessset(*principalobjectattributeaccessid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|PrincipalObjectAttributeAccesses|
|DisplayCollectionName|Field Sharing|
|DisplayName|Field Sharing|
|EntitySetName|principalobjectattributeaccessset|
|IsBPFEntity|False|
|LogicalCollectionName|principalobjectattributeaccesses|
|LogicalName|principalobjectattributeaccess|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|principalobjectattributeaccessid|
|PrimaryNameAttribute||
|SchemaName|PrincipalObjectAttributeAccess|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AttributeId](#BKMK_AttributeId)
- [ObjectId](#BKMK_ObjectId)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [PrincipalId](#BKMK_PrincipalId)
- [PrincipalIdType](#BKMK_PrincipalIdType)
- [PrincipalObjectAttributeAccessId](#BKMK_PrincipalObjectAttributeAccessId)
- [ReadAccess](#BKMK_ReadAccess)
- [UpdateAccess](#BKMK_UpdateAccess)


### <a name="BKMK_AttributeId"></a> AttributeId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the shared secured field|
|DisplayName|Secured field|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|attributeid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the entity instance with shared secured field|
|DisplayName|Entity instance|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|objectid|
|RequiredLevel|SystemRequired|
|Targets|account,activityfileattachment,appaction,appactionmigration,appactionrule,appelement,applicationuser,appmodulecomponentedge,appmodulecomponentnode,appointment,appsetting,appusersetting,archivecleanupinfo,archivecleanupoperation,attributeimageconfig,bot,botcomponent,bulkarchiveconfig,bulkarchivefailuredetail,bulkarchiveoperation,bulkarchiveoperationdetail,businessunit,canvasappextendedmetadata,card,cascadegrantrevokeaccessrecordstracker,cascadegrantrevokeaccessversiontracker,catalog,catalogassignment,channelaccessprofile,chat,comment,connection,connectioninstance,connectionreference,connector,contact,conversationtranscript,customapi,customapirequestparameter,customapiresponseproperty,customeraddress,datalakefolder,datalakefolderpermission,datalakeworkspace,datalakeworkspacepermission,dataprocessingconfiguration,delegatedauthorization,desktopflowbinary,desktopflowmodule,email,enablearchivalrequest,entityanalyticsconfig,entityimageconfig,entityindex,entityrecordfilter,environmentvariabledefinition,environmentvariablevalue,exportedexcel,exportsolutionupload,fax,featurecontrolsetting,feedback,flowmachine,flowmachinegroup,flowmachineimage,flowmachineimageversion,flowmachinenetwork,flowsession,fxexpression,goal,holidaywrapper,indexattributes,internalcatalogassignment,kbarticle,keyvaultreference,knowledgearticle,knowledgearticleviews,knowledgebaserecord,letter,mailmergetemplate,managedidentity,metadataforarchival,mobileofflineprofileextension,msdynce_botcontent,msdyn_aibdataset,msdyn_aibdatasetfile,msdyn_aibdatasetrecord,msdyn_aibdatasetscontainer,msdyn_aibfeedbackloop,msdyn_aibfile,msdyn_aibfileattacheddata,msdyn_aiconfiguration,msdyn_aievent,msdyn_aifptrainingdocument,msdyn_aimodel,msdyn_aiodimage,msdyn_aiodlabel,msdyn_aiodtrainingboundingbox,msdyn_aiodtrainingimage,msdyn_aitemplate,msdyn_analysiscomponent,msdyn_analysisjob,msdyn_analysisoverride,msdyn_analysisresult,msdyn_analysisresultdetail,msdyn_appinsightsmetadata,msdyn_customcontrolextendedsettings,msdyn_dataflow,msdyn_dataflowrefreshhistory,msdyn_dataflowtemplate,msdyn_dataflow_datalakefolder,msdyn_dmsrequest,msdyn_dmsrequeststatus,msdyn_entitylinkchatconfiguration,msdyn_entityrefreshhistory,msdyn_favoriteknowledgearticle,msdyn_federatedarticle,msdyn_federatedarticleincident,msdyn_fileupload,msdyn_helppage,msdyn_insightsstorevirtualentity,msdyn_integratedsearchprovider,msdyn_kalanguagesetting,msdyn_kbattachment,msdyn_kmfederatedsearchconfig,msdyn_kmpersonalizationsetting,msdyn_knowledgearticleimage,msdyn_knowledgearticletemplate,msdyn_knowledgeconfiguration,msdyn_knowledgeinteractioninsight,msdyn_knowledgemanagementsetting,msdyn_knowledgepersonalfilter,msdyn_knowledgesearchfilter,msdyn_knowledgesearchinsight,msdyn_mobileapp,msdyn_pmanalysishistory,msdyn_pmcalendar,msdyn_pmcalendarversion,msdyn_pminferredtask,msdyn_pmprocessextendedmetadataversion,msdyn_pmprocesstemplate,msdyn_pmprocessusersettings,msdyn_pmprocessversion,msdyn_pmrecording,msdyn_pmtemplate,msdyn_pmview,msdyn_richtextfile,msdyn_schedule,msdyn_serviceconfiguration,msdyn_slakpi,msdyn_solutionhealthrule,msdyn_solutionhealthruleargument,msdyn_solutionhealthruleset,msdyn_tour,msdyn_virtualtablecolumncandidate,msdyn_workflowactionstatus,msgraphresourcetosubscription,mspcat_catalogsubmissionfiles,mspcat_packagestore,organizationdatasyncfnostate,organizationdatasyncstate,organizationdatasyncsubscription,organizationdatasyncsubscriptionentity,organizationdatasyncsubscriptionfnotable,organizationsetting,package,pdfsetting,phonecall,pluginpackage,position,powerbidataset,powerbimashupparameter,powerbireport,powerfxrule,privilegesremovalsetting,processstageparameter,provisionlanguageforuser,queue,queueitem,reconciliationentityinfo,reconciliationinfo,recordfilter,recurringappointmentmaster,relationshipattribute,reportcategory,retaineddataexcel,retentioncleanupinfo,retentioncleanupoperation,retentionconfig,retentionfailuredetail,retentionoperation,retentionoperationdetail,revokeinheritedaccessrecordstracker,roleeditorlayout,searchattributesettings,searchcustomanalyzer,searchrelationshipsettings,serviceplan,serviceplanmapping,settingdefinition,sharedlinksetting,sharedobject,sharedworkspace,sharedworkspacepool,sharepointdocumentlocation,sharepointsite,socialactivity,socialprofile,solutioncomponentattributeconfiguration,solutioncomponentbatchconfiguration,solutioncomponentconfiguration,solutioncomponentrelationshipconfiguration,stagedentity,stagedentityattribute,stagesolutionupload,supportusertable,synapsedatabase,synapselinkexternaltablestate,synapselinkprofile,synapselinkprofileentity,synapselinkprofileentitystate,synapselinkschedule,systemuser,systemuserauthorizationchangetracker,task,tdsmetadata,team,teammobileofflineprofilemembership,territory,usermobileofflineprofilemembership,userrating,virtualentitymetadata,workflowbinary,workqueue,workqueueitem|
|Type|Lookup|


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|--------|-----|
|Description|Type of the record with shared secured field|
|DisplayName|Entity object type|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|objecttypecode|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_PrincipalId"></a> PrincipalId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the principal to which secured field is shared|
|DisplayName|Principal|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|principalid|
|RequiredLevel|SystemRequired|
|Targets|systemuser,team|
|Type|Lookup|


### <a name="BKMK_PrincipalIdType"></a> PrincipalIdType

|Property|Value|
|--------|-----|
|Description|Type of the principal to which secured field is shared|
|DisplayName|Principal type|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|principalidtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_PrincipalObjectAttributeAccessId"></a> PrincipalObjectAttributeAccessId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the shared secured field instance|
|DisplayName|Shared secured field|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|principalobjectattributeaccessid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ReadAccess"></a> ReadAccess

|Property|Value|
|--------|-----|
|Description|Read permission for secured field instance|
|DisplayName|Read permission|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|readaccess|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### ReadAccess Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_UpdateAccess"></a> UpdateAccess

|Property|Value|
|--------|-----|
|Description|Update permission for secured field instance|
|DisplayName|Update permission|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|updateaccess|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### UpdateAccess Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0


<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [PrincipalIdName](#BKMK_PrincipalIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the associated organization.|
|DisplayName|Organization|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|SystemRequired|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationidname|
|MaxLength|160|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_PrincipalIdName"></a> PrincipalIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|principalidname|
|MaxLength|160|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [account_principalobjectattributeaccess](#BKMK_account_principalobjectattributeaccess)
- [contact_principalobjectattributeaccess](#BKMK_contact_principalobjectattributeaccess)
- [lk_principalobjectattributeaccess_organizationid](#BKMK_lk_principalobjectattributeaccess_organizationid)
- [team_principalobjectattributeaccess_principalid](#BKMK_team_principalobjectattributeaccess_principalid)
- [systemuser_principalobjectattributeaccess_principalid](#BKMK_systemuser_principalobjectattributeaccess_principalid)
- [knowledgearticle_PrincipalObjectAttributeAccess](#BKMK_knowledgearticle_PrincipalObjectAttributeAccess)
- [KnowledgeBaseRecord_PrincipalObjectAttributeAccess](#BKMK_KnowledgeBaseRecord_PrincipalObjectAttributeAccess)
- [team_principalobjectattributeaccess](#BKMK_team_principalobjectattributeaccess)
- [reportcategory_principalobjectattributeaccess](#BKMK_reportcategory_principalobjectattributeaccess)
- [mailmergetemplate_principalobjectattributeaccess](#BKMK_mailmergetemplate_principalobjectattributeaccess)
- [fax_principalobjectattributeaccess](#BKMK_fax_principalobjectattributeaccess)
- [socialactivity_principalobjectattributeaccess](#BKMK_socialactivity_principalobjectattributeaccess)
- [kbarticle_principalobjectattributeaccess](#BKMK_kbarticle_principalobjectattributeaccess)
- [phonecall_principalobjectattributeaccess](#BKMK_phonecall_principalobjectattributeaccess)
- [position_principalobjectattributeaccess](#BKMK_position_principalobjectattributeaccess)
- [customeraddress_principalobjectattributeaccess](#BKMK_customeraddress_principalobjectattributeaccess)
- [sharepointsite_principalobjectattributeaccess](#BKMK_sharepointsite_principalobjectattributeaccess)
- [systemuser_principalobjectattributeaccess](#BKMK_systemuser_principalobjectattributeaccess)
- [connection_principalobjectattributeaccess](#BKMK_connection_principalobjectattributeaccess)
- [appointment_principalobjectattributeaccess](#BKMK_appointment_principalobjectattributeaccess)
- [goal_principalobjectattributeaccess](#BKMK_goal_principalobjectattributeaccess)
- [email_principalobjectattributeaccess](#BKMK_email_principalobjectattributeaccess)
- [knowledgearticleview_principalobjectattributeaccess](#BKMK_knowledgearticleview_principalobjectattributeaccess)
- [feedback_principalobjectattributeaccess](#BKMK_feedback_principalobjectattributeaccess)
- [businessunit_principalobjectattributeaccess](#BKMK_businessunit_principalobjectattributeaccess)
- [sharepointdocumentlocation_principalobjectattributeaccess](#BKMK_sharepointdocumentlocation_principalobjectattributeaccess)
- [queueitem_principalobjectattributeaccess](#BKMK_queueitem_principalobjectattributeaccess)
- [queue_principalobjectattributeaccess](#BKMK_queue_principalobjectattributeaccess)
- [recurringappointmentmaster_principalobjectattributeaccess](#BKMK_recurringappointmentmaster_principalobjectattributeaccess)
- [task_principalobjectattributeaccess](#BKMK_task_principalobjectattributeaccess)
- [letter_principalobjectattributeaccess](#BKMK_letter_principalobjectattributeaccess)
- [socialprofile_principalobjectattributeaccess](#BKMK_socialprofile_principalobjectattributeaccess)
- [solutioncomponentattributeconfiguration_PrincipalObjectAttributeAccesses](#BKMK_solutioncomponentattributeconfiguration_PrincipalObjectAttributeAccesses)
- [solutioncomponentbatchconfiguration_PrincipalObjectAttributeAccesses](#BKMK_solutioncomponentbatchconfiguration_PrincipalObjectAttributeAccesses)
- [solutioncomponentconfiguration_PrincipalObjectAttributeAccesses](#BKMK_solutioncomponentconfiguration_PrincipalObjectAttributeAccesses)
- [solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses](#BKMK_solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses)
- [package_PrincipalObjectAttributeAccesses](#BKMK_package_PrincipalObjectAttributeAccesses)
- [stagesolutionupload_PrincipalObjectAttributeAccesses](#BKMK_stagesolutionupload_PrincipalObjectAttributeAccesses)
- [exportsolutionupload_PrincipalObjectAttributeAccesses](#BKMK_exportsolutionupload_PrincipalObjectAttributeAccesses)
- [featurecontrolsetting_PrincipalObjectAttributeAccesses](#BKMK_featurecontrolsetting_PrincipalObjectAttributeAccesses)
- [attributeimageconfig_PrincipalObjectAttributeAccesses](#BKMK_attributeimageconfig_PrincipalObjectAttributeAccesses)
- [entityimageconfig_PrincipalObjectAttributeAccesses](#BKMK_entityimageconfig_PrincipalObjectAttributeAccesses)
- [relationshipattribute_PrincipalObjectAttributeAccesses](#BKMK_relationshipattribute_PrincipalObjectAttributeAccesses)
- [stagedentity_PrincipalObjectAttributeAccesses](#BKMK_stagedentity_PrincipalObjectAttributeAccesses)
- [stagedentityattribute_PrincipalObjectAttributeAccesses](#BKMK_stagedentityattribute_PrincipalObjectAttributeAccesses)
- [catalog_PrincipalObjectAttributeAccesses](#BKMK_catalog_PrincipalObjectAttributeAccesses)
- [catalogassignment_PrincipalObjectAttributeAccesses](#BKMK_catalogassignment_PrincipalObjectAttributeAccesses)
- [customapi_PrincipalObjectAttributeAccesses](#BKMK_customapi_PrincipalObjectAttributeAccesses)
- [customapirequestparameter_PrincipalObjectAttributeAccesses](#BKMK_customapirequestparameter_PrincipalObjectAttributeAccesses)
- [customapiresponseproperty_PrincipalObjectAttributeAccesses](#BKMK_customapiresponseproperty_PrincipalObjectAttributeAccesses)
- [provisionlanguageforuser_PrincipalObjectAttributeAccesses](#BKMK_provisionlanguageforuser_PrincipalObjectAttributeAccesses)
- [sharedobject_PrincipalObjectAttributeAccesses](#BKMK_sharedobject_PrincipalObjectAttributeAccesses)
- [sharedworkspace_PrincipalObjectAttributeAccesses](#BKMK_sharedworkspace_PrincipalObjectAttributeAccesses)
- [sharedworkspacepool_PrincipalObjectAttributeAccesses](#BKMK_sharedworkspacepool_PrincipalObjectAttributeAccesses)
- [entityanalyticsconfig_PrincipalObjectAttributeAccesses](#BKMK_entityanalyticsconfig_PrincipalObjectAttributeAccesses)
- [datalakefolder_PrincipalObjectAttributeAccesses](#BKMK_datalakefolder_PrincipalObjectAttributeAccesses)
- [datalakefolderpermission_PrincipalObjectAttributeAccesses](#BKMK_datalakefolderpermission_PrincipalObjectAttributeAccesses)
- [datalakeworkspace_PrincipalObjectAttributeAccesses](#BKMK_datalakeworkspace_PrincipalObjectAttributeAccesses)
- [datalakeworkspacepermission_PrincipalObjectAttributeAccesses](#BKMK_datalakeworkspacepermission_PrincipalObjectAttributeAccesses)
- [dataprocessingconfiguration_PrincipalObjectAttributeAccesses](#BKMK_dataprocessingconfiguration_PrincipalObjectAttributeAccesses)
- [exportedexcel_PrincipalObjectAttributeAccesses](#BKMK_exportedexcel_PrincipalObjectAttributeAccesses)
- [retaineddataexcel_PrincipalObjectAttributeAccesses](#BKMK_retaineddataexcel_PrincipalObjectAttributeAccesses)
- [synapsedatabase_PrincipalObjectAttributeAccesses](#BKMK_synapsedatabase_PrincipalObjectAttributeAccesses)
- [synapselinkexternaltablestate_PrincipalObjectAttributeAccesses](#BKMK_synapselinkexternaltablestate_PrincipalObjectAttributeAccesses)
- [synapselinkprofile_PrincipalObjectAttributeAccesses](#BKMK_synapselinkprofile_PrincipalObjectAttributeAccesses)
- [synapselinkprofileentity_PrincipalObjectAttributeAccesses](#BKMK_synapselinkprofileentity_PrincipalObjectAttributeAccesses)
- [synapselinkprofileentitystate_PrincipalObjectAttributeAccesses](#BKMK_synapselinkprofileentitystate_PrincipalObjectAttributeAccesses)
- [synapselinkschedule_PrincipalObjectAttributeAccesses](#BKMK_synapselinkschedule_PrincipalObjectAttributeAccesses)
- [msdyn_dataflow_PrincipalObjectAttributeAccesses](#BKMK_msdyn_dataflow_PrincipalObjectAttributeAccesses)
- [msdyn_dataflowrefreshhistory_PrincipalObjectAttributeAccesses](#BKMK_msdyn_dataflowrefreshhistory_PrincipalObjectAttributeAccesses)
- [msdyn_entityrefreshhistory_PrincipalObjectAttributeAccesses](#BKMK_msdyn_entityrefreshhistory_PrincipalObjectAttributeAccesses)
- [sharedlinksetting_PrincipalObjectAttributeAccesses](#BKMK_sharedlinksetting_PrincipalObjectAttributeAccesses)
- [entityrecordfilter_PrincipalObjectAttributeAccesses](#BKMK_entityrecordfilter_PrincipalObjectAttributeAccesses)
- [recordfilter_PrincipalObjectAttributeAccesses](#BKMK_recordfilter_PrincipalObjectAttributeAccesses)
- [delegatedauthorization_PrincipalObjectAttributeAccesses](#BKMK_delegatedauthorization_PrincipalObjectAttributeAccesses)
- [serviceplan_PrincipalObjectAttributeAccesses](#BKMK_serviceplan_PrincipalObjectAttributeAccesses)
- [serviceplanmapping_PrincipalObjectAttributeAccesses](#BKMK_serviceplanmapping_PrincipalObjectAttributeAccesses)
- [applicationuser_PrincipalObjectAttributeAccesses](#BKMK_applicationuser_PrincipalObjectAttributeAccesses)
- [connector_PrincipalObjectAttributeAccesses](#BKMK_connector_PrincipalObjectAttributeAccesses)
- [environmentvariabledefinition_PrincipalObjectAttributeAccesses](#BKMK_environmentvariabledefinition_PrincipalObjectAttributeAccesses)
- [environmentvariablevalue_PrincipalObjectAttributeAccesses](#BKMK_environmentvariablevalue_PrincipalObjectAttributeAccesses)
- [workflowbinary_PrincipalObjectAttributeAccesses](#BKMK_workflowbinary_PrincipalObjectAttributeAccesses)
- [desktopflowmodule_PrincipalObjectAttributeAccesses](#BKMK_desktopflowmodule_PrincipalObjectAttributeAccesses)
- [flowmachine_PrincipalObjectAttributeAccesses](#BKMK_flowmachine_PrincipalObjectAttributeAccesses)
- [flowmachinegroup_PrincipalObjectAttributeAccesses](#BKMK_flowmachinegroup_PrincipalObjectAttributeAccesses)
- [flowmachineimage_PrincipalObjectAttributeAccesses](#BKMK_flowmachineimage_PrincipalObjectAttributeAccesses)
- [flowmachineimageversion_PrincipalObjectAttributeAccesses](#BKMK_flowmachineimageversion_PrincipalObjectAttributeAccesses)
- [flowmachinenetwork_PrincipalObjectAttributeAccesses](#BKMK_flowmachinenetwork_PrincipalObjectAttributeAccesses)
- [processstageparameter_PrincipalObjectAttributeAccesses](#BKMK_processstageparameter_PrincipalObjectAttributeAccesses)
- [workqueue_PrincipalObjectAttributeAccesses](#BKMK_workqueue_PrincipalObjectAttributeAccesses)
- [workqueueitem_PrincipalObjectAttributeAccesses](#BKMK_workqueueitem_PrincipalObjectAttributeAccesses)
- [desktopflowbinary_PrincipalObjectAttributeAccesses](#BKMK_desktopflowbinary_PrincipalObjectAttributeAccesses)
- [flowsession_PrincipalObjectAttributeAccesses](#BKMK_flowsession_PrincipalObjectAttributeAccesses)
- [connectionreference_PrincipalObjectAttributeAccesses](#BKMK_connectionreference_PrincipalObjectAttributeAccesses)
- [connectioninstance_PrincipalObjectAttributeAccesses](#BKMK_connectioninstance_PrincipalObjectAttributeAccesses)
- [msdyn_helppage_PrincipalObjectAttributeAccesses](#BKMK_msdyn_helppage_PrincipalObjectAttributeAccesses)
- [msdyn_tour_PrincipalObjectAttributeAccesses](#BKMK_msdyn_tour_PrincipalObjectAttributeAccesses)
- [msdynce_botcontent_PrincipalObjectAttributeAccesses](#BKMK_msdynce_botcontent_PrincipalObjectAttributeAccesses)
- [conversationtranscript_PrincipalObjectAttributeAccesses](#BKMK_conversationtranscript_PrincipalObjectAttributeAccesses)
- [bot_PrincipalObjectAttributeAccesses](#BKMK_bot_PrincipalObjectAttributeAccesses)
- [botcomponent_PrincipalObjectAttributeAccesses](#BKMK_botcomponent_PrincipalObjectAttributeAccesses)
- [territory_principalobjectattributeaccess](#BKMK_territory_principalobjectattributeaccess)
- [activityfileattachment_PrincipalObjectAttributeAccesses](#BKMK_activityfileattachment_PrincipalObjectAttributeAccesses)
- [chat_PrincipalObjectAttributeAccesses](#BKMK_chat_PrincipalObjectAttributeAccesses)
- [msdyn_serviceconfiguration_PrincipalObjectAttributeAccesses](#BKMK_msdyn_serviceconfiguration_PrincipalObjectAttributeAccesses)
- [msdyn_slakpi_PrincipalObjectAttributeAccesses](#BKMK_msdyn_slakpi_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgemanagementsetting_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgemanagementsetting_PrincipalObjectAttributeAccesses)
- [msdyn_federatedarticle_PrincipalObjectAttributeAccesses](#BKMK_msdyn_federatedarticle_PrincipalObjectAttributeAccesses)
- [msdyn_federatedarticleincident_PrincipalObjectAttributeAccesses](#BKMK_msdyn_federatedarticleincident_PrincipalObjectAttributeAccesses)
- [msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses](#BKMK_msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses)
- [msdyn_kmfederatedsearchconfig_PrincipalObjectAttributeAccesses](#BKMK_msdyn_kmfederatedsearchconfig_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgearticleimage_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgearticleimage_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgeconfiguration_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgeconfiguration_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgeinteractioninsight_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgeinteractioninsight_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgesearchinsight_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgesearchinsight_PrincipalObjectAttributeAccesses)
- [msdyn_favoriteknowledgearticle_PrincipalObjectAttributeAccesses](#BKMK_msdyn_favoriteknowledgearticle_PrincipalObjectAttributeAccesses)
- [msdyn_kalanguagesetting_PrincipalObjectAttributeAccesses](#BKMK_msdyn_kalanguagesetting_PrincipalObjectAttributeAccesses)
- [msdyn_kbattachment_PrincipalObjectAttributeAccesses](#BKMK_msdyn_kbattachment_PrincipalObjectAttributeAccesses)
- [msdyn_kmpersonalizationsetting_PrincipalObjectAttributeAccesses](#BKMK_msdyn_kmpersonalizationsetting_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgepersonalfilter_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgepersonalfilter_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgesearchfilter_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgesearchfilter_PrincipalObjectAttributeAccesses)
- [pluginpackage_PrincipalObjectAttributeAccesses](#BKMK_pluginpackage_PrincipalObjectAttributeAccesses)
- [fxexpression_PrincipalObjectAttributeAccesses](#BKMK_fxexpression_PrincipalObjectAttributeAccesses)
- [powerfxrule_PrincipalObjectAttributeAccesses](#BKMK_powerfxrule_PrincipalObjectAttributeAccesses)
- [keyvaultreference_PrincipalObjectAttributeAccesses](#BKMK_keyvaultreference_PrincipalObjectAttributeAccesses)
- [managedidentity_PrincipalObjectAttributeAccesses](#BKMK_managedidentity_PrincipalObjectAttributeAccesses)
- [msgraphresourcetosubscription_PrincipalObjectAttributeAccesses](#BKMK_msgraphresourcetosubscription_PrincipalObjectAttributeAccesses)
- [virtualentitymetadata_PrincipalObjectAttributeAccesses](#BKMK_virtualentitymetadata_PrincipalObjectAttributeAccesses)
- [mobileofflineprofileextension_PrincipalObjectAttributeAccesses](#BKMK_mobileofflineprofileextension_PrincipalObjectAttributeAccesses)
- [teammobileofflineprofilemembership_PrincipalObjectAttributeAccesses](#BKMK_teammobileofflineprofilemembership_PrincipalObjectAttributeAccesses)
- [usermobileofflineprofilemembership_PrincipalObjectAttributeAccesses](#BKMK_usermobileofflineprofilemembership_PrincipalObjectAttributeAccesses)
- [organizationdatasyncsubscription_PrincipalObjectAttributeAccesses](#BKMK_organizationdatasyncsubscription_PrincipalObjectAttributeAccesses)
- [organizationdatasyncsubscriptionentity_PrincipalObjectAttributeAccesses](#BKMK_organizationdatasyncsubscriptionentity_PrincipalObjectAttributeAccesses)
- [organizationdatasyncsubscriptionfnotable_PrincipalObjectAttributeAccesses](#BKMK_organizationdatasyncsubscriptionfnotable_PrincipalObjectAttributeAccesses)
- [organizationdatasyncfnostate_PrincipalObjectAttributeAccesses](#BKMK_organizationdatasyncfnostate_PrincipalObjectAttributeAccesses)
- [organizationdatasyncstate_PrincipalObjectAttributeAccesses](#BKMK_organizationdatasyncstate_PrincipalObjectAttributeAccesses)
- [metadataforarchival_PrincipalObjectAttributeAccesses](#BKMK_metadataforarchival_PrincipalObjectAttributeAccesses)
- [retentionconfig_PrincipalObjectAttributeAccesses](#BKMK_retentionconfig_PrincipalObjectAttributeAccesses)
- [retentionfailuredetail_PrincipalObjectAttributeAccesses](#BKMK_retentionfailuredetail_PrincipalObjectAttributeAccesses)
- [retentionoperation_PrincipalObjectAttributeAccesses](#BKMK_retentionoperation_PrincipalObjectAttributeAccesses)
- [retentionoperationdetail_PrincipalObjectAttributeAccesses](#BKMK_retentionoperationdetail_PrincipalObjectAttributeAccesses)
- [msdyn_appinsightsmetadata_PrincipalObjectAttributeAccesses](#BKMK_msdyn_appinsightsmetadata_PrincipalObjectAttributeAccesses)
- [msdyn_dataflowtemplate_PrincipalObjectAttributeAccesses](#BKMK_msdyn_dataflowtemplate_PrincipalObjectAttributeAccesses)
- [msdyn_workflowactionstatus_PrincipalObjectAttributeAccesses](#BKMK_msdyn_workflowactionstatus_PrincipalObjectAttributeAccesses)
- [userrating_PrincipalObjectAttributeAccesses](#BKMK_userrating_PrincipalObjectAttributeAccesses)
- [msdyn_mobileapp_PrincipalObjectAttributeAccesses](#BKMK_msdyn_mobileapp_PrincipalObjectAttributeAccesses)
- [msdyn_insightsstorevirtualentity_PrincipalObjectAttributeAccesses](#BKMK_msdyn_insightsstorevirtualentity_PrincipalObjectAttributeAccesses)
- [roleeditorlayout_PrincipalObjectAttributeAccesses](#BKMK_roleeditorlayout_PrincipalObjectAttributeAccesses)
- [appaction_PrincipalObjectAttributeAccesses](#BKMK_appaction_PrincipalObjectAttributeAccesses)
- [appactionmigration_PrincipalObjectAttributeAccesses](#BKMK_appactionmigration_PrincipalObjectAttributeAccesses)
- [appactionrule_PrincipalObjectAttributeAccesses](#BKMK_appactionrule_PrincipalObjectAttributeAccesses)
- [card_PrincipalObjectAttributeAccesses](#BKMK_card_PrincipalObjectAttributeAccesses)
- [msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses](#BKMK_msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses)
- [msdyn_richtextfile_PrincipalObjectAttributeAccesses](#BKMK_msdyn_richtextfile_PrincipalObjectAttributeAccesses)
- [msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses](#BKMK_msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses)
- [searchrelationshipsettings_PrincipalObjectAttributeAccesses](#BKMK_searchrelationshipsettings_PrincipalObjectAttributeAccesses)
- [msdyn_virtualtablecolumncandidate_PrincipalObjectAttributeAccesses](#BKMK_msdyn_virtualtablecolumncandidate_PrincipalObjectAttributeAccesses)
- [msdyn_aiconfiguration_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aiconfiguration_PrincipalObjectAttributeAccesses)
- [msdyn_aievent_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aievent_PrincipalObjectAttributeAccesses)
- [msdyn_aimodel_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aimodel_PrincipalObjectAttributeAccesses)
- [msdyn_aitemplate_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aitemplate_PrincipalObjectAttributeAccesses)
- [msdyn_aibfeedbackloop_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aibfeedbackloop_PrincipalObjectAttributeAccesses)
- [msdyn_aifptrainingdocument_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aifptrainingdocument_PrincipalObjectAttributeAccesses)
- [msdyn_aiodimage_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aiodimage_PrincipalObjectAttributeAccesses)
- [msdyn_aiodlabel_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aiodlabel_PrincipalObjectAttributeAccesses)
- [msdyn_aiodtrainingboundingbox_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aiodtrainingboundingbox_PrincipalObjectAttributeAccesses)
- [msdyn_aiodtrainingimage_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aiodtrainingimage_PrincipalObjectAttributeAccesses)
- [msdyn_aibdataset_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aibdataset_PrincipalObjectAttributeAccesses)
- [msdyn_aibdatasetfile_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aibdatasetfile_PrincipalObjectAttributeAccesses)
- [msdyn_aibdatasetrecord_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aibdatasetrecord_PrincipalObjectAttributeAccesses)
- [msdyn_aibdatasetscontainer_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aibdatasetscontainer_PrincipalObjectAttributeAccesses)
- [msdyn_aibfile_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aibfile_PrincipalObjectAttributeAccesses)
- [msdyn_aibfileattacheddata_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aibfileattacheddata_PrincipalObjectAttributeAccesses)
- [msdyn_pmanalysishistory_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmanalysishistory_PrincipalObjectAttributeAccesses)
- [msdyn_pmcalendar_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmcalendar_PrincipalObjectAttributeAccesses)
- [msdyn_pmcalendarversion_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmcalendarversion_PrincipalObjectAttributeAccesses)
- [msdyn_pminferredtask_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pminferredtask_PrincipalObjectAttributeAccesses)
- [msdyn_pmprocessextendedmetadataversion_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmprocessextendedmetadataversion_PrincipalObjectAttributeAccesses)
- [msdyn_pmprocesstemplate_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmprocesstemplate_PrincipalObjectAttributeAccesses)
- [msdyn_pmprocessusersettings_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmprocessusersettings_PrincipalObjectAttributeAccesses)
- [msdyn_pmprocessversion_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmprocessversion_PrincipalObjectAttributeAccesses)
- [msdyn_pmrecording_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmrecording_PrincipalObjectAttributeAccesses)
- [msdyn_pmtemplate_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmtemplate_PrincipalObjectAttributeAccesses)
- [msdyn_pmview_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmview_PrincipalObjectAttributeAccesses)
- [msdyn_analysiscomponent_PrincipalObjectAttributeAccesses](#BKMK_msdyn_analysiscomponent_PrincipalObjectAttributeAccesses)
- [msdyn_analysisjob_PrincipalObjectAttributeAccesses](#BKMK_msdyn_analysisjob_PrincipalObjectAttributeAccesses)
- [msdyn_analysisoverride_PrincipalObjectAttributeAccesses](#BKMK_msdyn_analysisoverride_PrincipalObjectAttributeAccesses)
- [msdyn_analysisresult_PrincipalObjectAttributeAccesses](#BKMK_msdyn_analysisresult_PrincipalObjectAttributeAccesses)
- [msdyn_analysisresultdetail_PrincipalObjectAttributeAccesses](#BKMK_msdyn_analysisresultdetail_PrincipalObjectAttributeAccesses)
- [msdyn_solutionhealthrule_PrincipalObjectAttributeAccesses](#BKMK_msdyn_solutionhealthrule_PrincipalObjectAttributeAccesses)
- [msdyn_solutionhealthruleargument_PrincipalObjectAttributeAccesses](#BKMK_msdyn_solutionhealthruleargument_PrincipalObjectAttributeAccesses)
- [msdyn_solutionhealthruleset_PrincipalObjectAttributeAccesses](#BKMK_msdyn_solutionhealthruleset_PrincipalObjectAttributeAccesses)
- [powerbidataset_PrincipalObjectAttributeAccesses](#BKMK_powerbidataset_PrincipalObjectAttributeAccesses)
- [powerbimashupparameter_PrincipalObjectAttributeAccesses](#BKMK_powerbimashupparameter_PrincipalObjectAttributeAccesses)
- [powerbireport_PrincipalObjectAttributeAccesses](#BKMK_powerbireport_PrincipalObjectAttributeAccesses)
- [msdyn_fileupload_PrincipalObjectAttributeAccesses](#BKMK_msdyn_fileupload_PrincipalObjectAttributeAccesses)
- [mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses](#BKMK_mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses)
- [mspcat_packagestore_PrincipalObjectAttributeAccesses](#BKMK_mspcat_packagestore_PrincipalObjectAttributeAccesses)
- [msdyn_schedule_PrincipalObjectAttributeAccesses](#BKMK_msdyn_schedule_PrincipalObjectAttributeAccesses)
- [msdyn_dataflow_datalakefolder_PrincipalObjectAttributeAccesses](#BKMK_msdyn_dataflow_datalakefolder_PrincipalObjectAttributeAccesses)
- [msdyn_dmsrequest_PrincipalObjectAttributeAccesses](#BKMK_msdyn_dmsrequest_PrincipalObjectAttributeAccesses)
- [msdyn_dmsrequeststatus_PrincipalObjectAttributeAccesses](#BKMK_msdyn_dmsrequeststatus_PrincipalObjectAttributeAccesses)
- [searchattributesettings_PrincipalObjectAttributeAccesses](#BKMK_searchattributesettings_PrincipalObjectAttributeAccesses)
- [searchcustomanalyzer_PrincipalObjectAttributeAccesses](#BKMK_searchcustomanalyzer_PrincipalObjectAttributeAccesses)


### <a name="BKMK_account_principalobjectattributeaccess"></a> account_principalobjectattributeaccess

See the [account_principalobjectattributeaccess](account.md#BKMK_account_principalobjectattributeaccess) one-to-many relationship for the [account](account.md) table/entity.

### <a name="BKMK_contact_principalobjectattributeaccess"></a> contact_principalobjectattributeaccess

See the [contact_principalobjectattributeaccess](contact.md#BKMK_contact_principalobjectattributeaccess) one-to-many relationship for the [contact](contact.md) table/entity.

### <a name="BKMK_lk_principalobjectattributeaccess_organizationid"></a> lk_principalobjectattributeaccess_organizationid

See the [lk_principalobjectattributeaccess_organizationid](organization.md#BKMK_lk_principalobjectattributeaccess_organizationid) one-to-many relationship for the [organization](organization.md) table/entity.

### <a name="BKMK_team_principalobjectattributeaccess_principalid"></a> team_principalobjectattributeaccess_principalid

See the [team_principalobjectattributeaccess_principalid](team.md#BKMK_team_principalobjectattributeaccess_principalid) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_systemuser_principalobjectattributeaccess_principalid"></a> systemuser_principalobjectattributeaccess_principalid

See the [systemuser_principalobjectattributeaccess_principalid](systemuser.md#BKMK_systemuser_principalobjectattributeaccess_principalid) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_knowledgearticle_PrincipalObjectAttributeAccess"></a> knowledgearticle_PrincipalObjectAttributeAccess

See the [knowledgearticle_PrincipalObjectAttributeAccess](knowledgearticle.md#BKMK_knowledgearticle_PrincipalObjectAttributeAccess) one-to-many relationship for the [knowledgearticle](knowledgearticle.md) table/entity.

### <a name="BKMK_KnowledgeBaseRecord_PrincipalObjectAttributeAccess"></a> KnowledgeBaseRecord_PrincipalObjectAttributeAccess

See the [KnowledgeBaseRecord_PrincipalObjectAttributeAccess](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_PrincipalObjectAttributeAccess) one-to-many relationship for the [knowledgebaserecord](knowledgebaserecord.md) table/entity.

### <a name="BKMK_team_principalobjectattributeaccess"></a> team_principalobjectattributeaccess

See the [team_principalobjectattributeaccess](team.md#BKMK_team_principalobjectattributeaccess) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_reportcategory_principalobjectattributeaccess"></a> reportcategory_principalobjectattributeaccess

See the [reportcategory_principalobjectattributeaccess](reportcategory.md#BKMK_reportcategory_principalobjectattributeaccess) one-to-many relationship for the [reportcategory](reportcategory.md) table/entity.

### <a name="BKMK_mailmergetemplate_principalobjectattributeaccess"></a> mailmergetemplate_principalobjectattributeaccess

See the [mailmergetemplate_principalobjectattributeaccess](mailmergetemplate.md#BKMK_mailmergetemplate_principalobjectattributeaccess) one-to-many relationship for the [mailmergetemplate](mailmergetemplate.md) table/entity.

### <a name="BKMK_fax_principalobjectattributeaccess"></a> fax_principalobjectattributeaccess

See the [fax_principalobjectattributeaccess](fax.md#BKMK_fax_principalobjectattributeaccess) one-to-many relationship for the [fax](fax.md) table/entity.

### <a name="BKMK_socialactivity_principalobjectattributeaccess"></a> socialactivity_principalobjectattributeaccess

See the [socialactivity_principalobjectattributeaccess](socialactivity.md#BKMK_socialactivity_principalobjectattributeaccess) one-to-many relationship for the [socialactivity](socialactivity.md) table/entity.

### <a name="BKMK_kbarticle_principalobjectattributeaccess"></a> kbarticle_principalobjectattributeaccess

See the [kbarticle_principalobjectattributeaccess](kbarticle.md#BKMK_kbarticle_principalobjectattributeaccess) one-to-many relationship for the [kbarticle](kbarticle.md) table/entity.

### <a name="BKMK_phonecall_principalobjectattributeaccess"></a> phonecall_principalobjectattributeaccess

See the [phonecall_principalobjectattributeaccess](phonecall.md#BKMK_phonecall_principalobjectattributeaccess) one-to-many relationship for the [phonecall](phonecall.md) table/entity.

### <a name="BKMK_position_principalobjectattributeaccess"></a> position_principalobjectattributeaccess

See the [position_principalobjectattributeaccess](position.md#BKMK_position_principalobjectattributeaccess) one-to-many relationship for the [position](position.md) table/entity.

### <a name="BKMK_customeraddress_principalobjectattributeaccess"></a> customeraddress_principalobjectattributeaccess

See the [customeraddress_principalobjectattributeaccess](customeraddress.md#BKMK_customeraddress_principalobjectattributeaccess) one-to-many relationship for the [customeraddress](customeraddress.md) table/entity.

### <a name="BKMK_sharepointsite_principalobjectattributeaccess"></a> sharepointsite_principalobjectattributeaccess

See the [sharepointsite_principalobjectattributeaccess](sharepointsite.md#BKMK_sharepointsite_principalobjectattributeaccess) one-to-many relationship for the [sharepointsite](sharepointsite.md) table/entity.

### <a name="BKMK_systemuser_principalobjectattributeaccess"></a> systemuser_principalobjectattributeaccess

See the [systemuser_principalobjectattributeaccess](systemuser.md#BKMK_systemuser_principalobjectattributeaccess) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_connection_principalobjectattributeaccess"></a> connection_principalobjectattributeaccess

See the [connection_principalobjectattributeaccess](connection.md#BKMK_connection_principalobjectattributeaccess) one-to-many relationship for the [connection](connection.md) table/entity.

### <a name="BKMK_appointment_principalobjectattributeaccess"></a> appointment_principalobjectattributeaccess

See the [appointment_principalobjectattributeaccess](appointment.md#BKMK_appointment_principalobjectattributeaccess) one-to-many relationship for the [appointment](appointment.md) table/entity.

### <a name="BKMK_goal_principalobjectattributeaccess"></a> goal_principalobjectattributeaccess

See the [goal_principalobjectattributeaccess](goal.md#BKMK_goal_principalobjectattributeaccess) one-to-many relationship for the [goal](goal.md) table/entity.

### <a name="BKMK_email_principalobjectattributeaccess"></a> email_principalobjectattributeaccess

See the [email_principalobjectattributeaccess](email.md#BKMK_email_principalobjectattributeaccess) one-to-many relationship for the [email](email.md) table/entity.

### <a name="BKMK_knowledgearticleview_principalobjectattributeaccess"></a> knowledgearticleview_principalobjectattributeaccess

See the [knowledgearticleview_principalobjectattributeaccess](knowledgearticleviews.md#BKMK_knowledgearticleview_principalobjectattributeaccess) one-to-many relationship for the [knowledgearticleviews](knowledgearticleviews.md) table/entity.

### <a name="BKMK_feedback_principalobjectattributeaccess"></a> feedback_principalobjectattributeaccess

See the [feedback_principalobjectattributeaccess](feedback.md#BKMK_feedback_principalobjectattributeaccess) one-to-many relationship for the [feedback](feedback.md) table/entity.

### <a name="BKMK_businessunit_principalobjectattributeaccess"></a> businessunit_principalobjectattributeaccess

See the [businessunit_principalobjectattributeaccess](businessunit.md#BKMK_businessunit_principalobjectattributeaccess) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_sharepointdocumentlocation_principalobjectattributeaccess"></a> sharepointdocumentlocation_principalobjectattributeaccess

See the [sharepointdocumentlocation_principalobjectattributeaccess](sharepointdocumentlocation.md#BKMK_sharepointdocumentlocation_principalobjectattributeaccess) one-to-many relationship for the [sharepointdocumentlocation](sharepointdocumentlocation.md) table/entity.

### <a name="BKMK_queueitem_principalobjectattributeaccess"></a> queueitem_principalobjectattributeaccess

See the [queueitem_principalobjectattributeaccess](queueitem.md#BKMK_queueitem_principalobjectattributeaccess) one-to-many relationship for the [queueitem](queueitem.md) table/entity.

### <a name="BKMK_queue_principalobjectattributeaccess"></a> queue_principalobjectattributeaccess

See the [queue_principalobjectattributeaccess](queue.md#BKMK_queue_principalobjectattributeaccess) one-to-many relationship for the [queue](queue.md) table/entity.

### <a name="BKMK_recurringappointmentmaster_principalobjectattributeaccess"></a> recurringappointmentmaster_principalobjectattributeaccess

See the [recurringappointmentmaster_principalobjectattributeaccess](recurringappointmentmaster.md#BKMK_recurringappointmentmaster_principalobjectattributeaccess) one-to-many relationship for the [recurringappointmentmaster](recurringappointmentmaster.md) table/entity.

### <a name="BKMK_task_principalobjectattributeaccess"></a> task_principalobjectattributeaccess

See the [task_principalobjectattributeaccess](task.md#BKMK_task_principalobjectattributeaccess) one-to-many relationship for the [task](task.md) table/entity.

### <a name="BKMK_letter_principalobjectattributeaccess"></a> letter_principalobjectattributeaccess

See the [letter_principalobjectattributeaccess](letter.md#BKMK_letter_principalobjectattributeaccess) one-to-many relationship for the [letter](letter.md) table/entity.

### <a name="BKMK_socialprofile_principalobjectattributeaccess"></a> socialprofile_principalobjectattributeaccess

See the [socialprofile_principalobjectattributeaccess](socialprofile.md#BKMK_socialprofile_principalobjectattributeaccess) one-to-many relationship for the [socialprofile](socialprofile.md) table/entity.

### <a name="BKMK_solutioncomponentattributeconfiguration_PrincipalObjectAttributeAccesses"></a> solutioncomponentattributeconfiguration_PrincipalObjectAttributeAccesses

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentattributeconfiguration_PrincipalObjectAttributeAccesses](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_PrincipalObjectAttributeAccesses) one-to-many relationship for the [solutioncomponentattributeconfiguration](solutioncomponentattributeconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentbatchconfiguration_PrincipalObjectAttributeAccesses"></a> solutioncomponentbatchconfiguration_PrincipalObjectAttributeAccesses

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentbatchconfiguration_PrincipalObjectAttributeAccesses](solutioncomponentbatchconfiguration.md#BKMK_solutioncomponentbatchconfiguration_PrincipalObjectAttributeAccesses) one-to-many relationship for the [solutioncomponentbatchconfiguration](solutioncomponentbatchconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentconfiguration_PrincipalObjectAttributeAccesses"></a> solutioncomponentconfiguration_PrincipalObjectAttributeAccesses

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentconfiguration_PrincipalObjectAttributeAccesses](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_PrincipalObjectAttributeAccesses) one-to-many relationship for the [solutioncomponentconfiguration](solutioncomponentconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses"></a> solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses) one-to-many relationship for the [solutioncomponentrelationshipconfiguration](solutioncomponentrelationshipconfiguration.md) table/entity.

### <a name="BKMK_package_PrincipalObjectAttributeAccesses"></a> package_PrincipalObjectAttributeAccesses

**Added by**: msdyn_SolutionPackageMapping Solution

See the [package_PrincipalObjectAttributeAccesses](package.md#BKMK_package_PrincipalObjectAttributeAccesses) one-to-many relationship for the [package](package.md) table/entity.

### <a name="BKMK_stagesolutionupload_PrincipalObjectAttributeAccesses"></a> stagesolutionupload_PrincipalObjectAttributeAccesses

**Added by**: StageSolutionUpload Solution

See the [stagesolutionupload_PrincipalObjectAttributeAccesses](stagesolutionupload.md#BKMK_stagesolutionupload_PrincipalObjectAttributeAccesses) one-to-many relationship for the [stagesolutionupload](stagesolutionupload.md) table/entity.

### <a name="BKMK_exportsolutionupload_PrincipalObjectAttributeAccesses"></a> exportsolutionupload_PrincipalObjectAttributeAccesses

**Added by**: ExportSolutionUpload Solution

See the [exportsolutionupload_PrincipalObjectAttributeAccesses](exportsolutionupload.md#BKMK_exportsolutionupload_PrincipalObjectAttributeAccesses) one-to-many relationship for the [exportsolutionupload](exportsolutionupload.md) table/entity.

### <a name="BKMK_featurecontrolsetting_PrincipalObjectAttributeAccesses"></a> featurecontrolsetting_PrincipalObjectAttributeAccesses

**Added by**: msdyn_FeatureControlSetting Solution

See the [featurecontrolsetting_PrincipalObjectAttributeAccesses](featurecontrolsetting.md#BKMK_featurecontrolsetting_PrincipalObjectAttributeAccesses) one-to-many relationship for the [featurecontrolsetting](featurecontrolsetting.md) table/entity.

### <a name="BKMK_attributeimageconfig_PrincipalObjectAttributeAccesses"></a> attributeimageconfig_PrincipalObjectAttributeAccesses

**Added by**: Image Configuration Solution

See the [attributeimageconfig_PrincipalObjectAttributeAccesses](attributeimageconfig.md#BKMK_attributeimageconfig_PrincipalObjectAttributeAccesses) one-to-many relationship for the [attributeimageconfig](attributeimageconfig.md) table/entity.

### <a name="BKMK_entityimageconfig_PrincipalObjectAttributeAccesses"></a> entityimageconfig_PrincipalObjectAttributeAccesses

**Added by**: Image Configuration Solution

See the [entityimageconfig_PrincipalObjectAttributeAccesses](entityimageconfig.md#BKMK_entityimageconfig_PrincipalObjectAttributeAccesses) one-to-many relationship for the [entityimageconfig](entityimageconfig.md) table/entity.

### <a name="BKMK_relationshipattribute_PrincipalObjectAttributeAccesses"></a> relationshipattribute_PrincipalObjectAttributeAccesses

**Added by**: Metadata Extension Solution

See the [relationshipattribute_PrincipalObjectAttributeAccesses](relationshipattribute.md#BKMK_relationshipattribute_PrincipalObjectAttributeAccesses) one-to-many relationship for the [relationshipattribute](relationshipattribute.md) table/entity.

### <a name="BKMK_stagedentity_PrincipalObjectAttributeAccesses"></a> stagedentity_PrincipalObjectAttributeAccesses

**Added by**: Metadata Extension Solution

See the [stagedentity_PrincipalObjectAttributeAccesses](stagedentity.md#BKMK_stagedentity_PrincipalObjectAttributeAccesses) one-to-many relationship for the [stagedentity](stagedentity.md) table/entity.

### <a name="BKMK_stagedentityattribute_PrincipalObjectAttributeAccesses"></a> stagedentityattribute_PrincipalObjectAttributeAccesses

**Added by**: Metadata Extension Solution

See the [stagedentityattribute_PrincipalObjectAttributeAccesses](stagedentityattribute.md#BKMK_stagedentityattribute_PrincipalObjectAttributeAccesses) one-to-many relationship for the [stagedentityattribute](stagedentityattribute.md) table/entity.

### <a name="BKMK_catalog_PrincipalObjectAttributeAccesses"></a> catalog_PrincipalObjectAttributeAccesses

**Added by**: CatalogFramework Solution

See the [catalog_PrincipalObjectAttributeAccesses](catalog.md#BKMK_catalog_PrincipalObjectAttributeAccesses) one-to-many relationship for the [catalog](catalog.md) table/entity.

### <a name="BKMK_catalogassignment_PrincipalObjectAttributeAccesses"></a> catalogassignment_PrincipalObjectAttributeAccesses

**Added by**: CatalogFramework Solution

See the [catalogassignment_PrincipalObjectAttributeAccesses](catalogassignment.md#BKMK_catalogassignment_PrincipalObjectAttributeAccesses) one-to-many relationship for the [catalogassignment](catalogassignment.md) table/entity.

### <a name="BKMK_customapi_PrincipalObjectAttributeAccesses"></a> customapi_PrincipalObjectAttributeAccesses

**Added by**: Custom API Framework Solution

See the [customapi_PrincipalObjectAttributeAccesses](customapi.md#BKMK_customapi_PrincipalObjectAttributeAccesses) one-to-many relationship for the [customapi](customapi.md) table/entity.

### <a name="BKMK_customapirequestparameter_PrincipalObjectAttributeAccesses"></a> customapirequestparameter_PrincipalObjectAttributeAccesses

**Added by**: Custom API Framework Solution

See the [customapirequestparameter_PrincipalObjectAttributeAccesses](customapirequestparameter.md#BKMK_customapirequestparameter_PrincipalObjectAttributeAccesses) one-to-many relationship for the [customapirequestparameter](customapirequestparameter.md) table/entity.

### <a name="BKMK_customapiresponseproperty_PrincipalObjectAttributeAccesses"></a> customapiresponseproperty_PrincipalObjectAttributeAccesses

**Added by**: Custom API Framework Solution

See the [customapiresponseproperty_PrincipalObjectAttributeAccesses](customapiresponseproperty.md#BKMK_customapiresponseproperty_PrincipalObjectAttributeAccesses) one-to-many relationship for the [customapiresponseproperty](customapiresponseproperty.md) table/entity.

### <a name="BKMK_provisionlanguageforuser_PrincipalObjectAttributeAccesses"></a> provisionlanguageforuser_PrincipalObjectAttributeAccesses

**Added by**: msft_LocalizationExtension Solution

See the [provisionlanguageforuser_PrincipalObjectAttributeAccesses](provisionlanguageforuser.md#BKMK_provisionlanguageforuser_PrincipalObjectAttributeAccesses) one-to-many relationship for the [provisionlanguageforuser](provisionlanguageforuser.md) table/entity.

### <a name="BKMK_sharedobject_PrincipalObjectAttributeAccesses"></a> sharedobject_PrincipalObjectAttributeAccesses

**Added by**: Real-time Collaboration App Solution

See the [sharedobject_PrincipalObjectAttributeAccesses](sharedobject.md#BKMK_sharedobject_PrincipalObjectAttributeAccesses) one-to-many relationship for the [sharedobject](sharedobject.md) table/entity.

### <a name="BKMK_sharedworkspace_PrincipalObjectAttributeAccesses"></a> sharedworkspace_PrincipalObjectAttributeAccesses

**Added by**: Real-time Collaboration App Solution

See the [sharedworkspace_PrincipalObjectAttributeAccesses](sharedworkspace.md#BKMK_sharedworkspace_PrincipalObjectAttributeAccesses) one-to-many relationship for the [sharedworkspace](sharedworkspace.md) table/entity.

### <a name="BKMK_sharedworkspacepool_PrincipalObjectAttributeAccesses"></a> sharedworkspacepool_PrincipalObjectAttributeAccesses

**Added by**: Real-time Collaboration App Solution

See the [sharedworkspacepool_PrincipalObjectAttributeAccesses](sharedworkspacepool.md#BKMK_sharedworkspacepool_PrincipalObjectAttributeAccesses) one-to-many relationship for the [sharedworkspacepool](sharedworkspacepool.md) table/entity.

### <a name="BKMK_entityanalyticsconfig_PrincipalObjectAttributeAccesses"></a> entityanalyticsconfig_PrincipalObjectAttributeAccesses

**Added by**: Advanced Analytics Infrastructure Solution

See the [entityanalyticsconfig_PrincipalObjectAttributeAccesses](entityanalyticsconfig.md#BKMK_entityanalyticsconfig_PrincipalObjectAttributeAccesses) one-to-many relationship for the [entityanalyticsconfig](entityanalyticsconfig.md) table/entity.

### <a name="BKMK_datalakefolder_PrincipalObjectAttributeAccesses"></a> datalakefolder_PrincipalObjectAttributeAccesses

**Added by**: Data lake workspaces Solution

See the [datalakefolder_PrincipalObjectAttributeAccesses](datalakefolder.md#BKMK_datalakefolder_PrincipalObjectAttributeAccesses) one-to-many relationship for the [datalakefolder](datalakefolder.md) table/entity.

### <a name="BKMK_datalakefolderpermission_PrincipalObjectAttributeAccesses"></a> datalakefolderpermission_PrincipalObjectAttributeAccesses

**Added by**: Data lake workspaces Solution

See the [datalakefolderpermission_PrincipalObjectAttributeAccesses](datalakefolderpermission.md#BKMK_datalakefolderpermission_PrincipalObjectAttributeAccesses) one-to-many relationship for the [datalakefolderpermission](datalakefolderpermission.md) table/entity.

### <a name="BKMK_datalakeworkspace_PrincipalObjectAttributeAccesses"></a> datalakeworkspace_PrincipalObjectAttributeAccesses

**Added by**: Data lake workspaces Solution

See the [datalakeworkspace_PrincipalObjectAttributeAccesses](datalakeworkspace.md#BKMK_datalakeworkspace_PrincipalObjectAttributeAccesses) one-to-many relationship for the [datalakeworkspace](datalakeworkspace.md) table/entity.

### <a name="BKMK_datalakeworkspacepermission_PrincipalObjectAttributeAccesses"></a> datalakeworkspacepermission_PrincipalObjectAttributeAccesses

**Added by**: Data lake workspaces Solution

See the [datalakeworkspacepermission_PrincipalObjectAttributeAccesses](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_PrincipalObjectAttributeAccesses) one-to-many relationship for the [datalakeworkspacepermission](datalakeworkspacepermission.md) table/entity.

### <a name="BKMK_dataprocessingconfiguration_PrincipalObjectAttributeAccesses"></a> dataprocessingconfiguration_PrincipalObjectAttributeAccesses

**Added by**: Data lake workspaces Solution

See the [dataprocessingconfiguration_PrincipalObjectAttributeAccesses](dataprocessingconfiguration.md#BKMK_dataprocessingconfiguration_PrincipalObjectAttributeAccesses) one-to-many relationship for the [dataprocessingconfiguration](dataprocessingconfiguration.md) table/entity.

### <a name="BKMK_exportedexcel_PrincipalObjectAttributeAccesses"></a> exportedexcel_PrincipalObjectAttributeAccesses

**Added by**: Data lake workspaces Solution

See the [exportedexcel_PrincipalObjectAttributeAccesses](exportedexcel.md#BKMK_exportedexcel_PrincipalObjectAttributeAccesses) one-to-many relationship for the [exportedexcel](exportedexcel.md) table/entity.

### <a name="BKMK_retaineddataexcel_PrincipalObjectAttributeAccesses"></a> retaineddataexcel_PrincipalObjectAttributeAccesses

**Added by**: Data lake workspaces Solution

See the [retaineddataexcel_PrincipalObjectAttributeAccesses](retaineddataexcel.md#BKMK_retaineddataexcel_PrincipalObjectAttributeAccesses) one-to-many relationship for the [retaineddataexcel](retaineddataexcel.md) table/entity.

### <a name="BKMK_synapsedatabase_PrincipalObjectAttributeAccesses"></a> synapsedatabase_PrincipalObjectAttributeAccesses

**Added by**: Data lake workspaces Solution

See the [synapsedatabase_PrincipalObjectAttributeAccesses](synapsedatabase.md#BKMK_synapsedatabase_PrincipalObjectAttributeAccesses) one-to-many relationship for the [synapsedatabase](synapsedatabase.md) table/entity.

### <a name="BKMK_synapselinkexternaltablestate_PrincipalObjectAttributeAccesses"></a> synapselinkexternaltablestate_PrincipalObjectAttributeAccesses

**Added by**: Synapse Link Solution

See the [synapselinkexternaltablestate_PrincipalObjectAttributeAccesses](synapselinkexternaltablestate.md#BKMK_synapselinkexternaltablestate_PrincipalObjectAttributeAccesses) one-to-many relationship for the [synapselinkexternaltablestate](synapselinkexternaltablestate.md) table/entity.

### <a name="BKMK_synapselinkprofile_PrincipalObjectAttributeAccesses"></a> synapselinkprofile_PrincipalObjectAttributeAccesses

**Added by**: Synapse Link Solution

See the [synapselinkprofile_PrincipalObjectAttributeAccesses](synapselinkprofile.md#BKMK_synapselinkprofile_PrincipalObjectAttributeAccesses) one-to-many relationship for the [synapselinkprofile](synapselinkprofile.md) table/entity.

### <a name="BKMK_synapselinkprofileentity_PrincipalObjectAttributeAccesses"></a> synapselinkprofileentity_PrincipalObjectAttributeAccesses

**Added by**: Synapse Link Solution

See the [synapselinkprofileentity_PrincipalObjectAttributeAccesses](synapselinkprofileentity.md#BKMK_synapselinkprofileentity_PrincipalObjectAttributeAccesses) one-to-many relationship for the [synapselinkprofileentity](synapselinkprofileentity.md) table/entity.

### <a name="BKMK_synapselinkprofileentitystate_PrincipalObjectAttributeAccesses"></a> synapselinkprofileentitystate_PrincipalObjectAttributeAccesses

**Added by**: Synapse Link Solution

See the [synapselinkprofileentitystate_PrincipalObjectAttributeAccesses](synapselinkprofileentitystate.md#BKMK_synapselinkprofileentitystate_PrincipalObjectAttributeAccesses) one-to-many relationship for the [synapselinkprofileentitystate](synapselinkprofileentitystate.md) table/entity.

### <a name="BKMK_synapselinkschedule_PrincipalObjectAttributeAccesses"></a> synapselinkschedule_PrincipalObjectAttributeAccesses

**Added by**: Synapse Link Solution

See the [synapselinkschedule_PrincipalObjectAttributeAccesses](synapselinkschedule.md#BKMK_synapselinkschedule_PrincipalObjectAttributeAccesses) one-to-many relationship for the [synapselinkschedule](synapselinkschedule.md) table/entity.

### <a name="BKMK_msdyn_dataflow_PrincipalObjectAttributeAccesses"></a> msdyn_dataflow_PrincipalObjectAttributeAccesses

**Added by**: Dataflow Solution Solution

See the [msdyn_dataflow_PrincipalObjectAttributeAccesses](msdyn_dataflow.md#BKMK_msdyn_dataflow_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_dataflow](msdyn_dataflow.md) table/entity.

### <a name="BKMK_msdyn_dataflowrefreshhistory_PrincipalObjectAttributeAccesses"></a> msdyn_dataflowrefreshhistory_PrincipalObjectAttributeAccesses

**Added by**: Dataflow Solution Solution

See the [msdyn_dataflowrefreshhistory_PrincipalObjectAttributeAccesses](msdyn_dataflowrefreshhistory.md#BKMK_msdyn_dataflowrefreshhistory_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_dataflowrefreshhistory](msdyn_dataflowrefreshhistory.md) table/entity.

### <a name="BKMK_msdyn_entityrefreshhistory_PrincipalObjectAttributeAccesses"></a> msdyn_entityrefreshhistory_PrincipalObjectAttributeAccesses

**Added by**: Dataflow Solution Solution

See the [msdyn_entityrefreshhistory_PrincipalObjectAttributeAccesses](msdyn_entityrefreshhistory.md#BKMK_msdyn_entityrefreshhistory_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_entityrefreshhistory](msdyn_entityrefreshhistory.md) table/entity.

### <a name="BKMK_sharedlinksetting_PrincipalObjectAttributeAccesses"></a> sharedlinksetting_PrincipalObjectAttributeAccesses

**Added by**: Access Team Solution

See the [sharedlinksetting_PrincipalObjectAttributeAccesses](sharedlinksetting.md#BKMK_sharedlinksetting_PrincipalObjectAttributeAccesses) one-to-many relationship for the [sharedlinksetting](sharedlinksetting.md) table/entity.

### <a name="BKMK_entityrecordfilter_PrincipalObjectAttributeAccesses"></a> entityrecordfilter_PrincipalObjectAttributeAccesses

**Added by**: AuthorizationCore Solution

See the [entityrecordfilter_PrincipalObjectAttributeAccesses](entityrecordfilter.md#BKMK_entityrecordfilter_PrincipalObjectAttributeAccesses) one-to-many relationship for the [entityrecordfilter](entityrecordfilter.md) table/entity.

### <a name="BKMK_recordfilter_PrincipalObjectAttributeAccesses"></a> recordfilter_PrincipalObjectAttributeAccesses

**Added by**: AuthorizationCore Solution

See the [recordfilter_PrincipalObjectAttributeAccesses](recordfilter.md#BKMK_recordfilter_PrincipalObjectAttributeAccesses) one-to-many relationship for the [recordfilter](recordfilter.md) table/entity.

### <a name="BKMK_delegatedauthorization_PrincipalObjectAttributeAccesses"></a> delegatedauthorization_PrincipalObjectAttributeAccesses

**Added by**: Delegated Authorization Solution

See the [delegatedauthorization_PrincipalObjectAttributeAccesses](delegatedauthorization.md#BKMK_delegatedauthorization_PrincipalObjectAttributeAccesses) one-to-many relationship for the [delegatedauthorization](delegatedauthorization.md) table/entity.

### <a name="BKMK_serviceplan_PrincipalObjectAttributeAccesses"></a> serviceplan_PrincipalObjectAttributeAccesses

**Added by**: License Enforcement Solution

See the [serviceplan_PrincipalObjectAttributeAccesses](serviceplan.md#BKMK_serviceplan_PrincipalObjectAttributeAccesses) one-to-many relationship for the [serviceplan](serviceplan.md) table/entity.

### <a name="BKMK_serviceplanmapping_PrincipalObjectAttributeAccesses"></a> serviceplanmapping_PrincipalObjectAttributeAccesses

**Added by**: License Enforcement Solution

See the [serviceplanmapping_PrincipalObjectAttributeAccesses](serviceplanmapping.md#BKMK_serviceplanmapping_PrincipalObjectAttributeAccesses) one-to-many relationship for the [serviceplanmapping](serviceplanmapping.md) table/entity.

### <a name="BKMK_applicationuser_PrincipalObjectAttributeAccesses"></a> applicationuser_PrincipalObjectAttributeAccesses

**Added by**: ApplicationUserSolution Solution

See the [applicationuser_PrincipalObjectAttributeAccesses](applicationuser.md#BKMK_applicationuser_PrincipalObjectAttributeAccesses) one-to-many relationship for the [applicationuser](applicationuser.md) table/entity.

### <a name="BKMK_connector_PrincipalObjectAttributeAccesses"></a> connector_PrincipalObjectAttributeAccesses

**Added by**: Power Connector Solution Solution

See the [connector_PrincipalObjectAttributeAccesses](connector.md#BKMK_connector_PrincipalObjectAttributeAccesses) one-to-many relationship for the [connector](connector.md) table/entity.

### <a name="BKMK_environmentvariabledefinition_PrincipalObjectAttributeAccesses"></a> environmentvariabledefinition_PrincipalObjectAttributeAccesses

**Added by**: Environment Variables Solution

See the [environmentvariabledefinition_PrincipalObjectAttributeAccesses](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_PrincipalObjectAttributeAccesses) one-to-many relationship for the [environmentvariabledefinition](environmentvariabledefinition.md) table/entity.

### <a name="BKMK_environmentvariablevalue_PrincipalObjectAttributeAccesses"></a> environmentvariablevalue_PrincipalObjectAttributeAccesses

**Added by**: Environment Variables Solution

See the [environmentvariablevalue_PrincipalObjectAttributeAccesses](environmentvariablevalue.md#BKMK_environmentvariablevalue_PrincipalObjectAttributeAccesses) one-to-many relationship for the [environmentvariablevalue](environmentvariablevalue.md) table/entity.

### <a name="BKMK_workflowbinary_PrincipalObjectAttributeAccesses"></a> workflowbinary_PrincipalObjectAttributeAccesses

**Added by**: Power Automate Extensions Workflow Binary package Solution

See the [workflowbinary_PrincipalObjectAttributeAccesses](workflowbinary.md#BKMK_workflowbinary_PrincipalObjectAttributeAccesses) one-to-many relationship for the [workflowbinary](workflowbinary.md) table/entity.

### <a name="BKMK_desktopflowmodule_PrincipalObjectAttributeAccesses"></a> desktopflowmodule_PrincipalObjectAttributeAccesses

**Added by**: Power Automate Extensions core package Solution

See the [desktopflowmodule_PrincipalObjectAttributeAccesses](desktopflowmodule.md#BKMK_desktopflowmodule_PrincipalObjectAttributeAccesses) one-to-many relationship for the [desktopflowmodule](desktopflowmodule.md) table/entity.

### <a name="BKMK_flowmachine_PrincipalObjectAttributeAccesses"></a> flowmachine_PrincipalObjectAttributeAccesses

**Added by**: Power Automate Extensions core package Solution

See the [flowmachine_PrincipalObjectAttributeAccesses](flowmachine.md#BKMK_flowmachine_PrincipalObjectAttributeAccesses) one-to-many relationship for the [flowmachine](flowmachine.md) table/entity.

### <a name="BKMK_flowmachinegroup_PrincipalObjectAttributeAccesses"></a> flowmachinegroup_PrincipalObjectAttributeAccesses

**Added by**: Power Automate Extensions core package Solution

See the [flowmachinegroup_PrincipalObjectAttributeAccesses](flowmachinegroup.md#BKMK_flowmachinegroup_PrincipalObjectAttributeAccesses) one-to-many relationship for the [flowmachinegroup](flowmachinegroup.md) table/entity.

### <a name="BKMK_flowmachineimage_PrincipalObjectAttributeAccesses"></a> flowmachineimage_PrincipalObjectAttributeAccesses

**Added by**: Power Automate Extensions core package Solution

See the [flowmachineimage_PrincipalObjectAttributeAccesses](flowmachineimage.md#BKMK_flowmachineimage_PrincipalObjectAttributeAccesses) one-to-many relationship for the [flowmachineimage](flowmachineimage.md) table/entity.

### <a name="BKMK_flowmachineimageversion_PrincipalObjectAttributeAccesses"></a> flowmachineimageversion_PrincipalObjectAttributeAccesses

**Added by**: Power Automate Extensions core package Solution

See the [flowmachineimageversion_PrincipalObjectAttributeAccesses](flowmachineimageversion.md#BKMK_flowmachineimageversion_PrincipalObjectAttributeAccesses) one-to-many relationship for the [flowmachineimageversion](flowmachineimageversion.md) table/entity.

### <a name="BKMK_flowmachinenetwork_PrincipalObjectAttributeAccesses"></a> flowmachinenetwork_PrincipalObjectAttributeAccesses

**Added by**: Power Automate Extensions core package Solution

See the [flowmachinenetwork_PrincipalObjectAttributeAccesses](flowmachinenetwork.md#BKMK_flowmachinenetwork_PrincipalObjectAttributeAccesses) one-to-many relationship for the [flowmachinenetwork](flowmachinenetwork.md) table/entity.

### <a name="BKMK_processstageparameter_PrincipalObjectAttributeAccesses"></a> processstageparameter_PrincipalObjectAttributeAccesses

**Added by**: Power Automate Extensions core package Solution

See the [processstageparameter_PrincipalObjectAttributeAccesses](processstageparameter.md#BKMK_processstageparameter_PrincipalObjectAttributeAccesses) one-to-many relationship for the [processstageparameter](processstageparameter.md) table/entity.

### <a name="BKMK_workqueue_PrincipalObjectAttributeAccesses"></a> workqueue_PrincipalObjectAttributeAccesses

**Added by**: Power Automate Extensions core package Solution

See the [workqueue_PrincipalObjectAttributeAccesses](workqueue.md#BKMK_workqueue_PrincipalObjectAttributeAccesses) one-to-many relationship for the [workqueue](workqueue.md) table/entity.

### <a name="BKMK_workqueueitem_PrincipalObjectAttributeAccesses"></a> workqueueitem_PrincipalObjectAttributeAccesses

**Added by**: Power Automate Extensions core package Solution

See the [workqueueitem_PrincipalObjectAttributeAccesses](workqueueitem.md#BKMK_workqueueitem_PrincipalObjectAttributeAccesses) one-to-many relationship for the [workqueueitem](workqueueitem.md) table/entity.

### <a name="BKMK_desktopflowbinary_PrincipalObjectAttributeAccesses"></a> desktopflowbinary_PrincipalObjectAttributeAccesses

**Added by**: Power Automate Extensions core package Solution

See the [desktopflowbinary_PrincipalObjectAttributeAccesses](desktopflowbinary.md#BKMK_desktopflowbinary_PrincipalObjectAttributeAccesses) one-to-many relationship for the [desktopflowbinary](desktopflowbinary.md) table/entity.

### <a name="BKMK_flowsession_PrincipalObjectAttributeAccesses"></a> flowsession_PrincipalObjectAttributeAccesses

**Added by**: Power Automate Extensions core package Solution

See the [flowsession_PrincipalObjectAttributeAccesses](flowsession.md#BKMK_flowsession_PrincipalObjectAttributeAccesses) one-to-many relationship for the [flowsession](flowsession.md) table/entity.

### <a name="BKMK_connectionreference_PrincipalObjectAttributeAccesses"></a> connectionreference_PrincipalObjectAttributeAccesses

**Added by**: Power Platform Connection References Solution

See the [connectionreference_PrincipalObjectAttributeAccesses](connectionreference.md#BKMK_connectionreference_PrincipalObjectAttributeAccesses) one-to-many relationship for the [connectionreference](connectionreference.md) table/entity.

### <a name="BKMK_connectioninstance_PrincipalObjectAttributeAccesses"></a> connectioninstance_PrincipalObjectAttributeAccesses

**Added by**: Connection Instance Solution Solution

See the [connectioninstance_PrincipalObjectAttributeAccesses](connectioninstance.md#BKMK_connectioninstance_PrincipalObjectAttributeAccesses) one-to-many relationship for the [connectioninstance](connectioninstance.md) table/entity.

### <a name="BKMK_msdyn_helppage_PrincipalObjectAttributeAccesses"></a> msdyn_helppage_PrincipalObjectAttributeAccesses

**Added by**: Contextual Help Solution

See the [msdyn_helppage_PrincipalObjectAttributeAccesses](msdyn_helppage.md#BKMK_msdyn_helppage_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_helppage](msdyn_helppage.md) table/entity.

### <a name="BKMK_msdyn_tour_PrincipalObjectAttributeAccesses"></a> msdyn_tour_PrincipalObjectAttributeAccesses

**Added by**: Contextual Help Solution

See the [msdyn_tour_PrincipalObjectAttributeAccesses](msdyn_tour.md#BKMK_msdyn_tour_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_tour](msdyn_tour.md) table/entity.

### <a name="BKMK_msdynce_botcontent_PrincipalObjectAttributeAccesses"></a> msdynce_botcontent_PrincipalObjectAttributeAccesses

**Added by**: Customer Care Intelligence Bots Solution

See the [msdynce_botcontent_PrincipalObjectAttributeAccesses](msdynce_botcontent.md#BKMK_msdynce_botcontent_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdynce_botcontent](msdynce_botcontent.md) table/entity.

### <a name="BKMK_conversationtranscript_PrincipalObjectAttributeAccesses"></a> conversationtranscript_PrincipalObjectAttributeAccesses

**Added by**: Power Virtual Agents Common Solution

See the [conversationtranscript_PrincipalObjectAttributeAccesses](conversationtranscript.md#BKMK_conversationtranscript_PrincipalObjectAttributeAccesses) one-to-many relationship for the [conversationtranscript](conversationtranscript.md) table/entity.

### <a name="BKMK_bot_PrincipalObjectAttributeAccesses"></a> bot_PrincipalObjectAttributeAccesses

**Added by**: Power Virtual Agents Solution

See the [bot_PrincipalObjectAttributeAccesses](bot.md#BKMK_bot_PrincipalObjectAttributeAccesses) one-to-many relationship for the [bot](bot.md) table/entity.

### <a name="BKMK_botcomponent_PrincipalObjectAttributeAccesses"></a> botcomponent_PrincipalObjectAttributeAccesses

**Added by**: Power Virtual Agents Solution

See the [botcomponent_PrincipalObjectAttributeAccesses](botcomponent.md#BKMK_botcomponent_PrincipalObjectAttributeAccesses) one-to-many relationship for the [botcomponent](botcomponent.md) table/entity.

### <a name="BKMK_territory_principalobjectattributeaccess"></a> territory_principalobjectattributeaccess

**Added by**: Application Common Solution

See the [territory_principalobjectattributeaccess](territory.md#BKMK_territory_principalobjectattributeaccess) one-to-many relationship for the [territory](territory.md) table/entity.

### <a name="BKMK_activityfileattachment_PrincipalObjectAttributeAccesses"></a> activityfileattachment_PrincipalObjectAttributeAccesses

**Added by**: Activities Patch Solution

See the [activityfileattachment_PrincipalObjectAttributeAccesses](activityfileattachment.md#BKMK_activityfileattachment_PrincipalObjectAttributeAccesses) one-to-many relationship for the [activityfileattachment](activityfileattachment.md) table/entity.

### <a name="BKMK_chat_PrincipalObjectAttributeAccesses"></a> chat_PrincipalObjectAttributeAccesses

**Added by**: Activities Patch Solution

See the [chat_PrincipalObjectAttributeAccesses](chat.md#BKMK_chat_PrincipalObjectAttributeAccesses) one-to-many relationship for the [chat](chat.md) table/entity.

### <a name="BKMK_msdyn_serviceconfiguration_PrincipalObjectAttributeAccesses"></a> msdyn_serviceconfiguration_PrincipalObjectAttributeAccesses

**Added by**: Service Level Agreement (SLA) Extension Solution

See the [msdyn_serviceconfiguration_PrincipalObjectAttributeAccesses](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_serviceconfiguration](msdyn_serviceconfiguration.md) table/entity.

### <a name="BKMK_msdyn_slakpi_PrincipalObjectAttributeAccesses"></a> msdyn_slakpi_PrincipalObjectAttributeAccesses

**Added by**: Service Level Agreement (SLA) Extension Solution

See the [msdyn_slakpi_PrincipalObjectAttributeAccesses](msdyn_slakpi.md#BKMK_msdyn_slakpi_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_slakpi](msdyn_slakpi.md) table/entity.

### <a name="BKMK_msdyn_knowledgemanagementsetting_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgemanagementsetting_PrincipalObjectAttributeAccesses

**Added by**: Knowledge Management Patch Solution

See the [msdyn_knowledgemanagementsetting_PrincipalObjectAttributeAccesses](msdyn_knowledgemanagementsetting.md#BKMK_msdyn_knowledgemanagementsetting_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_knowledgemanagementsetting](msdyn_knowledgemanagementsetting.md) table/entity.

### <a name="BKMK_msdyn_federatedarticle_PrincipalObjectAttributeAccesses"></a> msdyn_federatedarticle_PrincipalObjectAttributeAccesses

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_federatedarticle_PrincipalObjectAttributeAccesses](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_federatedarticle](msdyn_federatedarticle.md) table/entity.

### <a name="BKMK_msdyn_federatedarticleincident_PrincipalObjectAttributeAccesses"></a> msdyn_federatedarticleincident_PrincipalObjectAttributeAccesses

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_federatedarticleincident_PrincipalObjectAttributeAccesses](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_federatedarticleincident](msdyn_federatedarticleincident.md) table/entity.

### <a name="BKMK_msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses"></a> msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses](msdyn_integratedsearchprovider.md#BKMK_msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_integratedsearchprovider](msdyn_integratedsearchprovider.md) table/entity.

### <a name="BKMK_msdyn_kmfederatedsearchconfig_PrincipalObjectAttributeAccesses"></a> msdyn_kmfederatedsearchconfig_PrincipalObjectAttributeAccesses

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_kmfederatedsearchconfig_PrincipalObjectAttributeAccesses](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_kmfederatedsearchconfig](msdyn_kmfederatedsearchconfig.md) table/entity.

### <a name="BKMK_msdyn_knowledgearticleimage_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgearticleimage_PrincipalObjectAttributeAccesses

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgearticleimage_PrincipalObjectAttributeAccesses](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_knowledgearticleimage](msdyn_knowledgearticleimage.md) table/entity.

### <a name="BKMK_msdyn_knowledgeconfiguration_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgeconfiguration_PrincipalObjectAttributeAccesses

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgeconfiguration_PrincipalObjectAttributeAccesses](msdyn_knowledgeconfiguration.md#BKMK_msdyn_knowledgeconfiguration_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_knowledgeconfiguration](msdyn_knowledgeconfiguration.md) table/entity.

### <a name="BKMK_msdyn_knowledgeinteractioninsight_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgeinteractioninsight_PrincipalObjectAttributeAccesses

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgeinteractioninsight_PrincipalObjectAttributeAccesses](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_knowledgeinteractioninsight](msdyn_knowledgeinteractioninsight.md) table/entity.

### <a name="BKMK_msdyn_knowledgesearchinsight_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgesearchinsight_PrincipalObjectAttributeAccesses

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgesearchinsight_PrincipalObjectAttributeAccesses](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_knowledgesearchinsight](msdyn_knowledgesearchinsight.md) table/entity.

### <a name="BKMK_msdyn_favoriteknowledgearticle_PrincipalObjectAttributeAccesses"></a> msdyn_favoriteknowledgearticle_PrincipalObjectAttributeAccesses

**Added by**: Knowledge Management Features Solution

See the [msdyn_favoriteknowledgearticle_PrincipalObjectAttributeAccesses](msdyn_favoriteknowledgearticle.md#BKMK_msdyn_favoriteknowledgearticle_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_favoriteknowledgearticle](msdyn_favoriteknowledgearticle.md) table/entity.

### <a name="BKMK_msdyn_kalanguagesetting_PrincipalObjectAttributeAccesses"></a> msdyn_kalanguagesetting_PrincipalObjectAttributeAccesses

**Added by**: Knowledge Management Features Solution

See the [msdyn_kalanguagesetting_PrincipalObjectAttributeAccesses](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_kalanguagesetting](msdyn_kalanguagesetting.md) table/entity.

### <a name="BKMK_msdyn_kbattachment_PrincipalObjectAttributeAccesses"></a> msdyn_kbattachment_PrincipalObjectAttributeAccesses

**Added by**: Knowledge Management Features Solution

See the [msdyn_kbattachment_PrincipalObjectAttributeAccesses](msdyn_kbattachment.md#BKMK_msdyn_kbattachment_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_kbattachment](msdyn_kbattachment.md) table/entity.

### <a name="BKMK_msdyn_kmpersonalizationsetting_PrincipalObjectAttributeAccesses"></a> msdyn_kmpersonalizationsetting_PrincipalObjectAttributeAccesses

**Added by**: Knowledge Management Features Solution

See the [msdyn_kmpersonalizationsetting_PrincipalObjectAttributeAccesses](msdyn_kmpersonalizationsetting.md#BKMK_msdyn_kmpersonalizationsetting_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_kmpersonalizationsetting](msdyn_kmpersonalizationsetting.md) table/entity.

### <a name="BKMK_msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_knowledgearticletemplate](msdyn_knowledgearticletemplate.md) table/entity.

### <a name="BKMK_msdyn_knowledgepersonalfilter_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgepersonalfilter_PrincipalObjectAttributeAccesses

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgepersonalfilter_PrincipalObjectAttributeAccesses](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_knowledgepersonalfilter](msdyn_knowledgepersonalfilter.md) table/entity.

### <a name="BKMK_msdyn_knowledgesearchfilter_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgesearchfilter_PrincipalObjectAttributeAccesses

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgesearchfilter_PrincipalObjectAttributeAccesses](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_knowledgesearchfilter](msdyn_knowledgesearchfilter.md) table/entity.

### <a name="BKMK_pluginpackage_PrincipalObjectAttributeAccesses"></a> pluginpackage_PrincipalObjectAttributeAccesses

**Added by**: Plugin Infrastructure Extension Solution

See the [pluginpackage_PrincipalObjectAttributeAccesses](pluginpackage.md#BKMK_pluginpackage_PrincipalObjectAttributeAccesses) one-to-many relationship for the [pluginpackage](pluginpackage.md) table/entity.

### <a name="BKMK_fxexpression_PrincipalObjectAttributeAccesses"></a> fxexpression_PrincipalObjectAttributeAccesses

**Added by**: msft_PowerfxRuleSolution Solution

See the [fxexpression_PrincipalObjectAttributeAccesses](fxexpression.md#BKMK_fxexpression_PrincipalObjectAttributeAccesses) one-to-many relationship for the [fxexpression](fxexpression.md) table/entity.

### <a name="BKMK_powerfxrule_PrincipalObjectAttributeAccesses"></a> powerfxrule_PrincipalObjectAttributeAccesses

**Added by**: msft_PowerfxRuleSolution Solution

See the [powerfxrule_PrincipalObjectAttributeAccesses](powerfxrule.md#BKMK_powerfxrule_PrincipalObjectAttributeAccesses) one-to-many relationship for the [powerfxrule](powerfxrule.md) table/entity.

### <a name="BKMK_keyvaultreference_PrincipalObjectAttributeAccesses"></a> keyvaultreference_PrincipalObjectAttributeAccesses

**Added by**: ManagedIdentityExtensions Solution

See the [keyvaultreference_PrincipalObjectAttributeAccesses](keyvaultreference.md#BKMK_keyvaultreference_PrincipalObjectAttributeAccesses) one-to-many relationship for the [keyvaultreference](keyvaultreference.md) table/entity.

### <a name="BKMK_managedidentity_PrincipalObjectAttributeAccesses"></a> managedidentity_PrincipalObjectAttributeAccesses

**Added by**: ManagedIdentityExtensions Solution

See the [managedidentity_PrincipalObjectAttributeAccesses](managedidentity.md#BKMK_managedidentity_PrincipalObjectAttributeAccesses) one-to-many relationship for the [managedidentity](managedidentity.md) table/entity.

### <a name="BKMK_msgraphresourcetosubscription_PrincipalObjectAttributeAccesses"></a> msgraphresourcetosubscription_PrincipalObjectAttributeAccesses

**Added by**: msft_ActivitiesInfra_Extensions Solution

See the [msgraphresourcetosubscription_PrincipalObjectAttributeAccesses](msgraphresourcetosubscription.md#BKMK_msgraphresourcetosubscription_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msgraphresourcetosubscription](msgraphresourcetosubscription.md) table/entity.

### <a name="BKMK_virtualentitymetadata_PrincipalObjectAttributeAccesses"></a> virtualentitymetadata_PrincipalObjectAttributeAccesses

**Added by**: RuntimeIntegration Solution

See the [virtualentitymetadata_PrincipalObjectAttributeAccesses](virtualentitymetadata.md#BKMK_virtualentitymetadata_PrincipalObjectAttributeAccesses) one-to-many relationship for the [virtualentitymetadata](virtualentitymetadata.md) table/entity.

### <a name="BKMK_mobileofflineprofileextension_PrincipalObjectAttributeAccesses"></a> mobileofflineprofileextension_PrincipalObjectAttributeAccesses

**Added by**: MobileOfflineProfileExtensionSolution Solution

See the [mobileofflineprofileextension_PrincipalObjectAttributeAccesses](mobileofflineprofileextension.md#BKMK_mobileofflineprofileextension_PrincipalObjectAttributeAccesses) one-to-many relationship for the [mobileofflineprofileextension](mobileofflineprofileextension.md) table/entity.

### <a name="BKMK_teammobileofflineprofilemembership_PrincipalObjectAttributeAccesses"></a> teammobileofflineprofilemembership_PrincipalObjectAttributeAccesses

**Added by**: MobileOfflineMembership Solution

See the [teammobileofflineprofilemembership_PrincipalObjectAttributeAccesses](teammobileofflineprofilemembership.md#BKMK_teammobileofflineprofilemembership_PrincipalObjectAttributeAccesses) one-to-many relationship for the [teammobileofflineprofilemembership](teammobileofflineprofilemembership.md) table/entity.

### <a name="BKMK_usermobileofflineprofilemembership_PrincipalObjectAttributeAccesses"></a> usermobileofflineprofilemembership_PrincipalObjectAttributeAccesses

**Added by**: MobileOfflineMembership Solution

See the [usermobileofflineprofilemembership_PrincipalObjectAttributeAccesses](usermobileofflineprofilemembership.md#BKMK_usermobileofflineprofilemembership_PrincipalObjectAttributeAccesses) one-to-many relationship for the [usermobileofflineprofilemembership](usermobileofflineprofilemembership.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscription_PrincipalObjectAttributeAccesses"></a> organizationdatasyncsubscription_PrincipalObjectAttributeAccesses

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscription_PrincipalObjectAttributeAccesses](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_PrincipalObjectAttributeAccesses) one-to-many relationship for the [organizationdatasyncsubscription](organizationdatasyncsubscription.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscriptionentity_PrincipalObjectAttributeAccesses"></a> organizationdatasyncsubscriptionentity_PrincipalObjectAttributeAccesses

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscriptionentity_PrincipalObjectAttributeAccesses](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_PrincipalObjectAttributeAccesses) one-to-many relationship for the [organizationdatasyncsubscriptionentity](organizationdatasyncsubscriptionentity.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_PrincipalObjectAttributeAccesses"></a> organizationdatasyncsubscriptionfnotable_PrincipalObjectAttributeAccesses

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscriptionfnotable_PrincipalObjectAttributeAccesses](organizationdatasyncsubscriptionfnotable.md#BKMK_organizationdatasyncsubscriptionfnotable_PrincipalObjectAttributeAccesses) one-to-many relationship for the [organizationdatasyncsubscriptionfnotable](organizationdatasyncsubscriptionfnotable.md) table/entity.

### <a name="BKMK_organizationdatasyncfnostate_PrincipalObjectAttributeAccesses"></a> organizationdatasyncfnostate_PrincipalObjectAttributeAccesses

**Added by**: DataSyncState Solution

See the [organizationdatasyncfnostate_PrincipalObjectAttributeAccesses](organizationdatasyncfnostate.md#BKMK_organizationdatasyncfnostate_PrincipalObjectAttributeAccesses) one-to-many relationship for the [organizationdatasyncfnostate](organizationdatasyncfnostate.md) table/entity.

### <a name="BKMK_organizationdatasyncstate_PrincipalObjectAttributeAccesses"></a> organizationdatasyncstate_PrincipalObjectAttributeAccesses

**Added by**: DataSyncState Solution

See the [organizationdatasyncstate_PrincipalObjectAttributeAccesses](organizationdatasyncstate.md#BKMK_organizationdatasyncstate_PrincipalObjectAttributeAccesses) one-to-many relationship for the [organizationdatasyncstate](organizationdatasyncstate.md) table/entity.

### <a name="BKMK_metadataforarchival_PrincipalObjectAttributeAccesses"></a> metadataforarchival_PrincipalObjectAttributeAccesses

**Added by**: Retention Base Components Solution

See the [metadataforarchival_PrincipalObjectAttributeAccesses](metadataforarchival.md#BKMK_metadataforarchival_PrincipalObjectAttributeAccesses) one-to-many relationship for the [metadataforarchival](metadataforarchival.md) table/entity.

### <a name="BKMK_retentionconfig_PrincipalObjectAttributeAccesses"></a> retentionconfig_PrincipalObjectAttributeAccesses

**Added by**: Retention Base Components Solution

See the [retentionconfig_PrincipalObjectAttributeAccesses](retentionconfig.md#BKMK_retentionconfig_PrincipalObjectAttributeAccesses) one-to-many relationship for the [retentionconfig](retentionconfig.md) table/entity.

### <a name="BKMK_retentionfailuredetail_PrincipalObjectAttributeAccesses"></a> retentionfailuredetail_PrincipalObjectAttributeAccesses

**Added by**: Retention Base Components Solution

See the [retentionfailuredetail_PrincipalObjectAttributeAccesses](retentionfailuredetail.md#BKMK_retentionfailuredetail_PrincipalObjectAttributeAccesses) one-to-many relationship for the [retentionfailuredetail](retentionfailuredetail.md) table/entity.

### <a name="BKMK_retentionoperation_PrincipalObjectAttributeAccesses"></a> retentionoperation_PrincipalObjectAttributeAccesses

**Added by**: Retention Base Components Solution

See the [retentionoperation_PrincipalObjectAttributeAccesses](retentionoperation.md#BKMK_retentionoperation_PrincipalObjectAttributeAccesses) one-to-many relationship for the [retentionoperation](retentionoperation.md) table/entity.

### <a name="BKMK_retentionoperationdetail_PrincipalObjectAttributeAccesses"></a> retentionoperationdetail_PrincipalObjectAttributeAccesses

**Added by**: Retention Base Components Solution

See the [retentionoperationdetail_PrincipalObjectAttributeAccesses](retentionoperationdetail.md#BKMK_retentionoperationdetail_PrincipalObjectAttributeAccesses) one-to-many relationship for the [retentionoperationdetail](retentionoperationdetail.md) table/entity.

### <a name="BKMK_msdyn_appinsightsmetadata_PrincipalObjectAttributeAccesses"></a> msdyn_appinsightsmetadata_PrincipalObjectAttributeAccesses

**Added by**: Insights App Platform Solution

See the [msdyn_appinsightsmetadata_PrincipalObjectAttributeAccesses](msdyn_appinsightsmetadata.md#BKMK_msdyn_appinsightsmetadata_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_appinsightsmetadata](msdyn_appinsightsmetadata.md) table/entity.

### <a name="BKMK_msdyn_dataflowtemplate_PrincipalObjectAttributeAccesses"></a> msdyn_dataflowtemplate_PrincipalObjectAttributeAccesses

**Added by**: Insights App Platform Solution

See the [msdyn_dataflowtemplate_PrincipalObjectAttributeAccesses](msdyn_dataflowtemplate.md#BKMK_msdyn_dataflowtemplate_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_dataflowtemplate](msdyn_dataflowtemplate.md) table/entity.

### <a name="BKMK_msdyn_workflowactionstatus_PrincipalObjectAttributeAccesses"></a> msdyn_workflowactionstatus_PrincipalObjectAttributeAccesses

**Added by**: Insights App Platform Solution

See the [msdyn_workflowactionstatus_PrincipalObjectAttributeAccesses](msdyn_workflowactionstatus.md#BKMK_msdyn_workflowactionstatus_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_workflowactionstatus](msdyn_workflowactionstatus.md) table/entity.

### <a name="BKMK_userrating_PrincipalObjectAttributeAccesses"></a> userrating_PrincipalObjectAttributeAccesses

**Added by**: User Rating Solution

See the [userrating_PrincipalObjectAttributeAccesses](userrating.md#BKMK_userrating_PrincipalObjectAttributeAccesses) one-to-many relationship for the [userrating](userrating.md) table/entity.

### <a name="BKMK_msdyn_mobileapp_PrincipalObjectAttributeAccesses"></a> msdyn_mobileapp_PrincipalObjectAttributeAccesses

**Added by**: Mobile Apps Solution Solution

See the [msdyn_mobileapp_PrincipalObjectAttributeAccesses](msdyn_mobileapp.md#BKMK_msdyn_mobileapp_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_mobileapp](msdyn_mobileapp.md) table/entity.

### <a name="BKMK_msdyn_insightsstorevirtualentity_PrincipalObjectAttributeAccesses"></a> msdyn_insightsstorevirtualentity_PrincipalObjectAttributeAccesses

**Added by**: Insights Store Data Provider Solution

See the [msdyn_insightsstorevirtualentity_PrincipalObjectAttributeAccesses](msdyn_insightsstorevirtualentity.md#BKMK_msdyn_insightsstorevirtualentity_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_insightsstorevirtualentity](msdyn_insightsstorevirtualentity.md) table/entity.

### <a name="BKMK_roleeditorlayout_PrincipalObjectAttributeAccesses"></a> roleeditorlayout_PrincipalObjectAttributeAccesses

**Added by**: Role Editor Solution

See the [roleeditorlayout_PrincipalObjectAttributeAccesses](roleeditorlayout.md#BKMK_roleeditorlayout_PrincipalObjectAttributeAccesses) one-to-many relationship for the [roleeditorlayout](roleeditorlayout.md) table/entity.

### <a name="BKMK_appaction_PrincipalObjectAttributeAccesses"></a> appaction_PrincipalObjectAttributeAccesses

**Added by**: Power Apps Actions Solution

See the [appaction_PrincipalObjectAttributeAccesses](appaction.md#BKMK_appaction_PrincipalObjectAttributeAccesses) one-to-many relationship for the [appaction](appaction.md) table/entity.

### <a name="BKMK_appactionmigration_PrincipalObjectAttributeAccesses"></a> appactionmigration_PrincipalObjectAttributeAccesses

**Added by**: Power Apps Actions Solution

See the [appactionmigration_PrincipalObjectAttributeAccesses](appactionmigration.md#BKMK_appactionmigration_PrincipalObjectAttributeAccesses) one-to-many relationship for the [appactionmigration](appactionmigration.md) table/entity.

### <a name="BKMK_appactionrule_PrincipalObjectAttributeAccesses"></a> appactionrule_PrincipalObjectAttributeAccesses

**Added by**: Power Apps Actions Solution

See the [appactionrule_PrincipalObjectAttributeAccesses](appactionrule.md#BKMK_appactionrule_PrincipalObjectAttributeAccesses) one-to-many relationship for the [appactionrule](appactionrule.md) table/entity.

### <a name="BKMK_card_PrincipalObjectAttributeAccesses"></a> card_PrincipalObjectAttributeAccesses

**Added by**: Power Apps cards Solution

See the [card_PrincipalObjectAttributeAccesses](card.md#BKMK_card_PrincipalObjectAttributeAccesses) one-to-many relationship for the [card](card.md) table/entity.

### <a name="BKMK_msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses"></a> msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses

**Added by**: Teams Chat Settings Solution Solution

See the [msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses](msdyn_entitylinkchatconfiguration.md#BKMK_msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_entitylinkchatconfiguration](msdyn_entitylinkchatconfiguration.md) table/entity.

### <a name="BKMK_msdyn_richtextfile_PrincipalObjectAttributeAccesses"></a> msdyn_richtextfile_PrincipalObjectAttributeAccesses

**Added by**: Rich Text Editor Solution

See the [msdyn_richtextfile_PrincipalObjectAttributeAccesses](msdyn_richtextfile.md#BKMK_msdyn_richtextfile_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_richtextfile](msdyn_richtextfile.md) table/entity.

### <a name="BKMK_msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses"></a> msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses

**Added by**: User Experiences Extended Settings Solution

See the [msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses](msdyn_customcontrolextendedsettings.md#BKMK_msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_customcontrolextendedsettings](msdyn_customcontrolextendedsettings.md) table/entity.

### <a name="BKMK_searchrelationshipsettings_PrincipalObjectAttributeAccesses"></a> searchrelationshipsettings_PrincipalObjectAttributeAccesses

**Added by**: msdyn_RelevanceSearch Solution

See the [searchrelationshipsettings_PrincipalObjectAttributeAccesses](searchrelationshipsettings.md#BKMK_searchrelationshipsettings_PrincipalObjectAttributeAccesses) one-to-many relationship for the [searchrelationshipsettings](searchrelationshipsettings.md) table/entity.

### <a name="BKMK_msdyn_virtualtablecolumncandidate_PrincipalObjectAttributeAccesses"></a> msdyn_virtualtablecolumncandidate_PrincipalObjectAttributeAccesses

**Added by**: Virtual Connector Provider Solution

See the [msdyn_virtualtablecolumncandidate_PrincipalObjectAttributeAccesses](msdyn_virtualtablecolumncandidate.md#BKMK_msdyn_virtualtablecolumncandidate_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_virtualtablecolumncandidate](msdyn_virtualtablecolumncandidate.md) table/entity.

### <a name="BKMK_msdyn_aiconfiguration_PrincipalObjectAttributeAccesses"></a> msdyn_aiconfiguration_PrincipalObjectAttributeAccesses

**Added by**: AISolution Solution

See the [msdyn_aiconfiguration_PrincipalObjectAttributeAccesses](msdyn_aiconfiguration.md#BKMK_msdyn_aiconfiguration_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_aiconfiguration](msdyn_aiconfiguration.md) table/entity.

### <a name="BKMK_msdyn_aievent_PrincipalObjectAttributeAccesses"></a> msdyn_aievent_PrincipalObjectAttributeAccesses

**Added by**: AISolution Solution

See the [msdyn_aievent_PrincipalObjectAttributeAccesses](msdyn_aievent.md#BKMK_msdyn_aievent_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_aievent](msdyn_aievent.md) table/entity.

### <a name="BKMK_msdyn_aimodel_PrincipalObjectAttributeAccesses"></a> msdyn_aimodel_PrincipalObjectAttributeAccesses

**Added by**: AISolution Solution

See the [msdyn_aimodel_PrincipalObjectAttributeAccesses](msdyn_aimodel.md#BKMK_msdyn_aimodel_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_aimodel](msdyn_aimodel.md) table/entity.

### <a name="BKMK_msdyn_aitemplate_PrincipalObjectAttributeAccesses"></a> msdyn_aitemplate_PrincipalObjectAttributeAccesses

**Added by**: AISolution Solution

See the [msdyn_aitemplate_PrincipalObjectAttributeAccesses](msdyn_aitemplate.md#BKMK_msdyn_aitemplate_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_aitemplate](msdyn_aitemplate.md) table/entity.

### <a name="BKMK_msdyn_aibfeedbackloop_PrincipalObjectAttributeAccesses"></a> msdyn_aibfeedbackloop_PrincipalObjectAttributeAccesses

**Added by**: AISolutionFullAdditions Solution

See the [msdyn_aibfeedbackloop_PrincipalObjectAttributeAccesses](msdyn_aibfeedbackloop.md#BKMK_msdyn_aibfeedbackloop_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_aibfeedbackloop](msdyn_aibfeedbackloop.md) table/entity.

### <a name="BKMK_msdyn_aifptrainingdocument_PrincipalObjectAttributeAccesses"></a> msdyn_aifptrainingdocument_PrincipalObjectAttributeAccesses

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aifptrainingdocument_PrincipalObjectAttributeAccesses](msdyn_aifptrainingdocument.md#BKMK_msdyn_aifptrainingdocument_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_aifptrainingdocument](msdyn_aifptrainingdocument.md) table/entity.

### <a name="BKMK_msdyn_aiodimage_PrincipalObjectAttributeAccesses"></a> msdyn_aiodimage_PrincipalObjectAttributeAccesses

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodimage_PrincipalObjectAttributeAccesses](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_aiodimage](msdyn_aiodimage.md) table/entity.

### <a name="BKMK_msdyn_aiodlabel_PrincipalObjectAttributeAccesses"></a> msdyn_aiodlabel_PrincipalObjectAttributeAccesses

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodlabel_PrincipalObjectAttributeAccesses](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_aiodlabel](msdyn_aiodlabel.md) table/entity.

### <a name="BKMK_msdyn_aiodtrainingboundingbox_PrincipalObjectAttributeAccesses"></a> msdyn_aiodtrainingboundingbox_PrincipalObjectAttributeAccesses

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodtrainingboundingbox_PrincipalObjectAttributeAccesses](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_aiodtrainingboundingbox](msdyn_aiodtrainingboundingbox.md) table/entity.

### <a name="BKMK_msdyn_aiodtrainingimage_PrincipalObjectAttributeAccesses"></a> msdyn_aiodtrainingimage_PrincipalObjectAttributeAccesses

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodtrainingimage_PrincipalObjectAttributeAccesses](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_aiodtrainingimage](msdyn_aiodtrainingimage.md) table/entity.

### <a name="BKMK_msdyn_aibdataset_PrincipalObjectAttributeAccesses"></a> msdyn_aibdataset_PrincipalObjectAttributeAccesses

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdataset_PrincipalObjectAttributeAccesses](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_aibdataset](msdyn_aibdataset.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetfile_PrincipalObjectAttributeAccesses"></a> msdyn_aibdatasetfile_PrincipalObjectAttributeAccesses

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetfile_PrincipalObjectAttributeAccesses](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_aibdatasetfile](msdyn_aibdatasetfile.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetrecord_PrincipalObjectAttributeAccesses"></a> msdyn_aibdatasetrecord_PrincipalObjectAttributeAccesses

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetrecord_PrincipalObjectAttributeAccesses](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_aibdatasetrecord](msdyn_aibdatasetrecord.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetscontainer_PrincipalObjectAttributeAccesses"></a> msdyn_aibdatasetscontainer_PrincipalObjectAttributeAccesses

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetscontainer_PrincipalObjectAttributeAccesses](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_aibdatasetscontainer](msdyn_aibdatasetscontainer.md) table/entity.

### <a name="BKMK_msdyn_aibfile_PrincipalObjectAttributeAccesses"></a> msdyn_aibfile_PrincipalObjectAttributeAccesses

**Added by**: AI Solution default templates Solution

See the [msdyn_aibfile_PrincipalObjectAttributeAccesses](msdyn_aibfile.md#BKMK_msdyn_aibfile_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_aibfile](msdyn_aibfile.md) table/entity.

### <a name="BKMK_msdyn_aibfileattacheddata_PrincipalObjectAttributeAccesses"></a> msdyn_aibfileattacheddata_PrincipalObjectAttributeAccesses

**Added by**: AI Solution default templates Solution

See the [msdyn_aibfileattacheddata_PrincipalObjectAttributeAccesses](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_aibfileattacheddata](msdyn_aibfileattacheddata.md) table/entity.

### <a name="BKMK_msdyn_pmanalysishistory_PrincipalObjectAttributeAccesses"></a> msdyn_pmanalysishistory_PrincipalObjectAttributeAccesses

**Added by**: Process Mining Solution

See the [msdyn_pmanalysishistory_PrincipalObjectAttributeAccesses](msdyn_pmanalysishistory.md#BKMK_msdyn_pmanalysishistory_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_pmanalysishistory](msdyn_pmanalysishistory.md) table/entity.

### <a name="BKMK_msdyn_pmcalendar_PrincipalObjectAttributeAccesses"></a> msdyn_pmcalendar_PrincipalObjectAttributeAccesses

**Added by**: Process Mining Solution

See the [msdyn_pmcalendar_PrincipalObjectAttributeAccesses](msdyn_pmcalendar.md#BKMK_msdyn_pmcalendar_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_pmcalendar](msdyn_pmcalendar.md) table/entity.

### <a name="BKMK_msdyn_pmcalendarversion_PrincipalObjectAttributeAccesses"></a> msdyn_pmcalendarversion_PrincipalObjectAttributeAccesses

**Added by**: Process Mining Solution

See the [msdyn_pmcalendarversion_PrincipalObjectAttributeAccesses](msdyn_pmcalendarversion.md#BKMK_msdyn_pmcalendarversion_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_pmcalendarversion](msdyn_pmcalendarversion.md) table/entity.

### <a name="BKMK_msdyn_pminferredtask_PrincipalObjectAttributeAccesses"></a> msdyn_pminferredtask_PrincipalObjectAttributeAccesses

**Added by**: Process Mining Solution

See the [msdyn_pminferredtask_PrincipalObjectAttributeAccesses](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_pminferredtask](msdyn_pminferredtask.md) table/entity.

### <a name="BKMK_msdyn_pmprocessextendedmetadataversion_PrincipalObjectAttributeAccesses"></a> msdyn_pmprocessextendedmetadataversion_PrincipalObjectAttributeAccesses

**Added by**: Process Mining Solution

See the [msdyn_pmprocessextendedmetadataversion_PrincipalObjectAttributeAccesses](msdyn_pmprocessextendedmetadataversion.md#BKMK_msdyn_pmprocessextendedmetadataversion_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_pmprocessextendedmetadataversion](msdyn_pmprocessextendedmetadataversion.md) table/entity.

### <a name="BKMK_msdyn_pmprocesstemplate_PrincipalObjectAttributeAccesses"></a> msdyn_pmprocesstemplate_PrincipalObjectAttributeAccesses

**Added by**: Process Mining Solution

See the [msdyn_pmprocesstemplate_PrincipalObjectAttributeAccesses](msdyn_pmprocesstemplate.md#BKMK_msdyn_pmprocesstemplate_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_pmprocesstemplate](msdyn_pmprocesstemplate.md) table/entity.

### <a name="BKMK_msdyn_pmprocessusersettings_PrincipalObjectAttributeAccesses"></a> msdyn_pmprocessusersettings_PrincipalObjectAttributeAccesses

**Added by**: Process Mining Solution

See the [msdyn_pmprocessusersettings_PrincipalObjectAttributeAccesses](msdyn_pmprocessusersettings.md#BKMK_msdyn_pmprocessusersettings_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_pmprocessusersettings](msdyn_pmprocessusersettings.md) table/entity.

### <a name="BKMK_msdyn_pmprocessversion_PrincipalObjectAttributeAccesses"></a> msdyn_pmprocessversion_PrincipalObjectAttributeAccesses

**Added by**: Process Mining Solution

See the [msdyn_pmprocessversion_PrincipalObjectAttributeAccesses](msdyn_pmprocessversion.md#BKMK_msdyn_pmprocessversion_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_pmprocessversion](msdyn_pmprocessversion.md) table/entity.

### <a name="BKMK_msdyn_pmrecording_PrincipalObjectAttributeAccesses"></a> msdyn_pmrecording_PrincipalObjectAttributeAccesses

**Added by**: Process Mining Solution

See the [msdyn_pmrecording_PrincipalObjectAttributeAccesses](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_pmrecording](msdyn_pmrecording.md) table/entity.

### <a name="BKMK_msdyn_pmtemplate_PrincipalObjectAttributeAccesses"></a> msdyn_pmtemplate_PrincipalObjectAttributeAccesses

**Added by**: Process Mining Solution

See the [msdyn_pmtemplate_PrincipalObjectAttributeAccesses](msdyn_pmtemplate.md#BKMK_msdyn_pmtemplate_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_pmtemplate](msdyn_pmtemplate.md) table/entity.

### <a name="BKMK_msdyn_pmview_PrincipalObjectAttributeAccesses"></a> msdyn_pmview_PrincipalObjectAttributeAccesses

**Added by**: Process Mining Solution

See the [msdyn_pmview_PrincipalObjectAttributeAccesses](msdyn_pmview.md#BKMK_msdyn_pmview_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_pmview](msdyn_pmview.md) table/entity.

### <a name="BKMK_msdyn_analysiscomponent_PrincipalObjectAttributeAccesses"></a> msdyn_analysiscomponent_PrincipalObjectAttributeAccesses

**Added by**: Power Apps Checker Solution

See the [msdyn_analysiscomponent_PrincipalObjectAttributeAccesses](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_analysiscomponent](msdyn_analysiscomponent.md) table/entity.

### <a name="BKMK_msdyn_analysisjob_PrincipalObjectAttributeAccesses"></a> msdyn_analysisjob_PrincipalObjectAttributeAccesses

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisjob_PrincipalObjectAttributeAccesses](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_analysisjob](msdyn_analysisjob.md) table/entity.

### <a name="BKMK_msdyn_analysisoverride_PrincipalObjectAttributeAccesses"></a> msdyn_analysisoverride_PrincipalObjectAttributeAccesses

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisoverride_PrincipalObjectAttributeAccesses](msdyn_analysisoverride.md#BKMK_msdyn_analysisoverride_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_analysisoverride](msdyn_analysisoverride.md) table/entity.

### <a name="BKMK_msdyn_analysisresult_PrincipalObjectAttributeAccesses"></a> msdyn_analysisresult_PrincipalObjectAttributeAccesses

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisresult_PrincipalObjectAttributeAccesses](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_analysisresult](msdyn_analysisresult.md) table/entity.

### <a name="BKMK_msdyn_analysisresultdetail_PrincipalObjectAttributeAccesses"></a> msdyn_analysisresultdetail_PrincipalObjectAttributeAccesses

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisresultdetail_PrincipalObjectAttributeAccesses](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_analysisresultdetail](msdyn_analysisresultdetail.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthrule_PrincipalObjectAttributeAccesses"></a> msdyn_solutionhealthrule_PrincipalObjectAttributeAccesses

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthrule_PrincipalObjectAttributeAccesses](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_solutionhealthrule](msdyn_solutionhealthrule.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthruleargument_PrincipalObjectAttributeAccesses"></a> msdyn_solutionhealthruleargument_PrincipalObjectAttributeAccesses

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthruleargument_PrincipalObjectAttributeAccesses](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_solutionhealthruleargument](msdyn_solutionhealthruleargument.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthruleset_PrincipalObjectAttributeAccesses"></a> msdyn_solutionhealthruleset_PrincipalObjectAttributeAccesses

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthruleset_PrincipalObjectAttributeAccesses](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_solutionhealthruleset](msdyn_solutionhealthruleset.md) table/entity.

### <a name="BKMK_powerbidataset_PrincipalObjectAttributeAccesses"></a> powerbidataset_PrincipalObjectAttributeAccesses

**Added by**: Power BI Entities Solution

See the [powerbidataset_PrincipalObjectAttributeAccesses](powerbidataset.md#BKMK_powerbidataset_PrincipalObjectAttributeAccesses) one-to-many relationship for the [powerbidataset](powerbidataset.md) table/entity.

### <a name="BKMK_powerbimashupparameter_PrincipalObjectAttributeAccesses"></a> powerbimashupparameter_PrincipalObjectAttributeAccesses

**Added by**: Power BI Entities Solution

See the [powerbimashupparameter_PrincipalObjectAttributeAccesses](powerbimashupparameter.md#BKMK_powerbimashupparameter_PrincipalObjectAttributeAccesses) one-to-many relationship for the [powerbimashupparameter](powerbimashupparameter.md) table/entity.

### <a name="BKMK_powerbireport_PrincipalObjectAttributeAccesses"></a> powerbireport_PrincipalObjectAttributeAccesses

**Added by**: Power BI Entities Solution

See the [powerbireport_PrincipalObjectAttributeAccesses](powerbireport.md#BKMK_powerbireport_PrincipalObjectAttributeAccesses) one-to-many relationship for the [powerbireport](powerbireport.md) table/entity.

### <a name="BKMK_msdyn_fileupload_PrincipalObjectAttributeAccesses"></a> msdyn_fileupload_PrincipalObjectAttributeAccesses

**Added by**: Smart Data Import Base Solution

See the [msdyn_fileupload_PrincipalObjectAttributeAccesses](msdyn_fileupload.md#BKMK_msdyn_fileupload_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_fileupload](msdyn_fileupload.md) table/entity.

### <a name="BKMK_mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses"></a> mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses

**Added by**: Power Platform Catalog Client Packaging Solution

See the [mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses](mspcat_catalogsubmissionfiles.md#BKMK_mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses) one-to-many relationship for the [mspcat_catalogsubmissionfiles](mspcat_catalogsubmissionfiles.md) table/entity.

### <a name="BKMK_mspcat_packagestore_PrincipalObjectAttributeAccesses"></a> mspcat_packagestore_PrincipalObjectAttributeAccesses

**Added by**: Power Platform Catalog Client Packaging Solution

See the [mspcat_packagestore_PrincipalObjectAttributeAccesses](mspcat_packagestore.md#BKMK_mspcat_packagestore_PrincipalObjectAttributeAccesses) one-to-many relationship for the [mspcat_packagestore](mspcat_packagestore.md) table/entity.

### <a name="BKMK_msdyn_schedule_PrincipalObjectAttributeAccesses"></a> msdyn_schedule_PrincipalObjectAttributeAccesses

**Added by**: Insights App Platform Solution

See the [msdyn_schedule_PrincipalObjectAttributeAccesses](msdyn_schedule.md#BKMK_msdyn_schedule_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_schedule](msdyn_schedule.md) table/entity.

### <a name="BKMK_msdyn_dataflow_datalakefolder_PrincipalObjectAttributeAccesses"></a> msdyn_dataflow_datalakefolder_PrincipalObjectAttributeAccesses

**Added by**: Insights App Platform Solution

See the [msdyn_dataflow_datalakefolder_PrincipalObjectAttributeAccesses](msdyn_dataflow_datalakefolder.md#BKMK_msdyn_dataflow_datalakefolder_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_dataflow_datalakefolder](msdyn_dataflow_datalakefolder.md) table/entity.

### <a name="BKMK_msdyn_dmsrequest_PrincipalObjectAttributeAccesses"></a> msdyn_dmsrequest_PrincipalObjectAttributeAccesses

**Added by**: Insights App Platform Solution

See the [msdyn_dmsrequest_PrincipalObjectAttributeAccesses](msdyn_dmsrequest.md#BKMK_msdyn_dmsrequest_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_dmsrequest](msdyn_dmsrequest.md) table/entity.

### <a name="BKMK_msdyn_dmsrequeststatus_PrincipalObjectAttributeAccesses"></a> msdyn_dmsrequeststatus_PrincipalObjectAttributeAccesses

**Added by**: Insights App Platform Solution

See the [msdyn_dmsrequeststatus_PrincipalObjectAttributeAccesses](msdyn_dmsrequeststatus.md#BKMK_msdyn_dmsrequeststatus_PrincipalObjectAttributeAccesses) one-to-many relationship for the [msdyn_dmsrequeststatus](msdyn_dmsrequeststatus.md) table/entity.

### <a name="BKMK_searchattributesettings_PrincipalObjectAttributeAccesses"></a> searchattributesettings_PrincipalObjectAttributeAccesses

**Added by**: msdyn_RelevanceSearch Solution

See the [searchattributesettings_PrincipalObjectAttributeAccesses](searchattributesettings.md#BKMK_searchattributesettings_PrincipalObjectAttributeAccesses) one-to-many relationship for the [searchattributesettings](searchattributesettings.md) table/entity.

### <a name="BKMK_searchcustomanalyzer_PrincipalObjectAttributeAccesses"></a> searchcustomanalyzer_PrincipalObjectAttributeAccesses

**Added by**: msdyn_RelevanceSearch Solution

See the [searchcustomanalyzer_PrincipalObjectAttributeAccesses](searchcustomanalyzer.md#BKMK_searchcustomanalyzer_PrincipalObjectAttributeAccesses) one-to-many relationship for the [searchcustomanalyzer](searchcustomanalyzer.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.principalobjectattributeaccess?text=principalobjectattributeaccess EntityType" />