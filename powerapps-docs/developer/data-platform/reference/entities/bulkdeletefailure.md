---
title: "Bulk Delete Failure (BulkDeleteFailure) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Bulk Delete Failure (BulkDeleteFailure) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Bulk Delete Failure (BulkDeleteFailure) table/entity reference (Microsoft Dataverse)

Record that was not deleted during a bulk deletion job.

## Messages

The following table lists the messages for the Bulk Delete Failure (BulkDeleteFailure) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /bulkdeletefailures(*bulkdeletefailureid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /bulkdeletefailures<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Bulk Delete Failure (BulkDeleteFailure) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Bulk Delete Failure** |
| **DisplayCollectionName** | **Bulk Delete Failures** |
| **SchemaName** | `BulkDeleteFailure` |
| **CollectionSchemaName** | `BulkDeleteFailures` |
| **EntitySetName** | `bulkdeletefailures`|
| **LogicalName** | `bulkdeletefailure` |
| **LogicalCollectionName** | `bulkdeletefailures` |
| **PrimaryIdAttribute** | `bulkdeletefailureid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

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
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)

### <a name="BKMK_AsyncOperationId"></a> AsyncOperationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the system job that created this record.**|
|DisplayName|**System Job**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`asyncoperationid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|asyncoperation|

### <a name="BKMK_BulkDeleteFailureId"></a> BulkDeleteFailureId

|Property|Value|
|---|---|
|Description|**Unique identifier of the bulk deletion failure record.**|
|DisplayName|**Bulk Deletion Failure**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`bulkdeletefailureid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_BulkDeleteOperationId"></a> BulkDeleteOperationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the bulk operation job which created this record**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`bulkdeleteoperationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|bulkdeleteoperation|

### <a name="BKMK_ErrorDescription"></a> ErrorDescription

|Property|Value|
|---|---|
|Description|**Description of the error.**|
|DisplayName|**Error Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`errordescription`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|512|

### <a name="BKMK_ErrorNumber"></a> ErrorNumber

|Property|Value|
|---|---|
|Description|**Error code for the failed bulk deletion.**|
|DisplayName|**Error Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`errornumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|-1000000000|

### <a name="BKMK_OrderedQueryIndex"></a> OrderedQueryIndex

|Property|Value|
|---|---|
|Description|**Index of the ordered query expression that retrieved this record.**|
|DisplayName|**Index**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`orderedqueryindex`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user or team who owns the bulk operation log.**|
|DisplayName|**Owner**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|ApplicationRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Unique identifier of the business unit that owns the bulk deletion failure.**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who owns the bulk deletion failure record.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**Unique identifier of the record that can not be deleted.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`regardingobjectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account, activityfileattachment, activitymimeattachment, activitypointer, adx_externalidentity, adx_invitation, adx_inviteredemption, adx_portalcomment, adx_setting, adx_webformsession, agentconversationmessage, agentconversationmessagefile, agentfeeditem, agenthubgoal, agenthubinsight, agenthubmetric, aicopilot, aiinsightcard, aiplugin, aipluginauth, aipluginconversationstarter, aipluginconversationstartermapping, aipluginexternalschema, aipluginexternalschemaproperty, aiplugingovernance, aiplugingovernanceext, aiplugininstance, aipluginoperation, aipluginoperationparameter, aipluginoperationresponsetemplate, aiplugintitle, aipluginusersetting, aiskillconfig, allowedmcpclient, annotation, annualfiscalcalendar, appaction, appactionmigration, appactionrule, appelement, appentitysearchview, application, applicationuser, appmodulecomponentedge, appmodulecomponentnode, appointment, approvalprocess, approvalstageapproval, approvalstagecondition, approvalstageintelligent, approvalstageorder, appsetting, appusersetting, archivecleanupinfo, archivecleanupoperation, attributeclusterconfig, attributeimageconfig, attributemap, attributemaskingrule, attributepicklistvalue, bot, botcomponent, botcomponentcollection, bulkarchiveconfig, bulkarchivefailuredetail, bulkarchiveoperation, bulkarchiveoperationdetail, businessprocess, businessunit, businessunitnewsarticle, calendar, canvasappextendedmetadata, card, cascadegrantrevokeaccessrecordstracker, cascadegrantrevokeaccessversiontracker, catalog, catalogassignment, certificatecredential, channelaccessprofile, channelaccessprofilerule, chat, comment, connectioninstance, connectionreference, connector, contact, conversationtranscript, copilotexamplequestion, copilotglossaryterm, copilotsynonyms, credential, customapi, customapirequestparameter, customapiresponseproperty, customeraddress, customerrelationship, datalakefolder, datalakefolderpermission, datalakeworkspace, datalakeworkspacepermission, dataprocessingconfiguration, delegatedauthorization, deleteditemreference, desktopflowbinary, desktopflowmodule, displaystring, dvfilesearch, dvfilesearchattribute, dvfilesearchentity, dvtablesearch, dvtablesearchattribute, dvtablesearchentity, email, emailaddressconfiguration, emailserverprofile, enablearchivalrequest, entityanalyticsconfig, entityclusterconfig, entityimageconfig, entityindex, entitymap, entityrecordfilter, environmentvariabledefinition, environmentvariablevalue, exportedexcel, exportsolutionupload, externalparty, externalpartyitem, fabricaiskill, fax, featurecontrolsetting, federatedknowledgecitation, federatedknowledgeconfiguration, federatedknowledgeentityconfiguration, federatedknowledgemetadatarefresh, fixedmonthlyfiscalcalendar, flowcapacityassignment, flowcredentialapplication, flowevent, flowmachine, flowmachinegroup, flowmachineimage, flowmachineimageversion, flowmachinenetwork, flowsession, flowsessionbinary, fxexpression, governanceconfiguration, holidaywrapper, import, importdata, importfile, importlog, importmap, indexattributes, internalcatalogassignment, isvconfig, kbarticle, kbarticlecomment, kbarticletemplate, keyvaultreference, knowledgearticle, knowledgebaserecord, knowledgefaq, knowledgesourceconsumer, knowledgesourceprofile, letter, mainfewshot, makerfewshot, managedidentity, maskingrule, mcpserver, mcptool, metadataforarchival, mobileofflineprofileextension, monthlyfiscalcalendar, msdynce_botcontent, msdyn_aibdataset, msdyn_aibdatasetfile, msdyn_aibdatasetrecord, msdyn_aibdatasetscontainer, msdyn_aibfeedbackloop, msdyn_aibfile, msdyn_aibfileattacheddata, msdyn_aiconfiguration, msdyn_aiconfigurationsearch, msdyn_aidataprocessingevent, msdyn_aidocumenttemplate, msdyn_aievaluationconfiguration, msdyn_aievaluationrun, msdyn_aievent, msdyn_aifptrainingdocument, msdyn_aimodel, msdyn_aimodelcatalog, msdyn_aiodimage, msdyn_aiodlabel, msdyn_aiodtrainingboundingbox, msdyn_aiodtrainingimage, msdyn_aioptimization, msdyn_aioptimizationprivatedata, msdyn_aitemplate, msdyn_aitestcase, msdyn_aitestcasedocument, msdyn_aitestcaseinput, msdyn_aitestrun, msdyn_aitestrunbatch, msdyn_analysiscomponent, msdyn_analysisjob, msdyn_analysisoverride, msdyn_analysisresult, msdyn_analysisresultdetail, msdyn_appinsightsmetadata, msdyn_copilotinteractions, msdyn_customcontrolextendedsettings, msdyn_dataflow, msdyn_dataflowconnectionreference, msdyn_dataflowrefreshhistory, msdyn_dataflowtemplate, msdyn_dataflow_datalakefolder, msdyn_dataworkspace, msdyn_dmsrequest, msdyn_dmsrequeststatus, msdyn_dmssyncrequest, msdyn_dmssyncstatus, msdyn_entitylinkchatconfiguration, msdyn_entityrefreshhistory, msdyn_favoriteknowledgearticle, msdyn_federatedarticle, msdyn_federatedarticleincident, msdyn_fileupload, msdyn_flow_actionapprovalmodel, msdyn_flow_approval, msdyn_flow_approvalrequest, msdyn_flow_approvalresponse, msdyn_flow_approvalstep, msdyn_flow_awaitallactionapprovalmodel, msdyn_flow_awaitallapprovalmodel, msdyn_flow_basicapprovalmodel, msdyn_flow_flowapproval, msdyn_formmapping, msdyn_function, msdyn_helppage, msdyn_historicalcaseharvestbatch, msdyn_historicalcaseharvestrun, msdyn_insightsstorevirtualentity, msdyn_integratedsearchprovider, msdyn_interimupdateknowledgearticle, msdyn_kalanguagesetting, msdyn_kbattachment, msdyn_kmfederatedsearchconfig, msdyn_kmpersonalizationsetting, msdyn_knowledgearticlecustomentity, msdyn_knowledgearticleimage, msdyn_knowledgearticletemplate, msdyn_knowledgeassetconfiguration, msdyn_knowledgeconfiguration, msdyn_knowledgeharvestjobrecord, msdyn_knowledgeinteractioninsight, msdyn_knowledgemanagementsetting, msdyn_knowledgepersonalfilter, msdyn_knowledgesearchfilter, msdyn_knowledgesearchinsight, msdyn_mobileapp, msdyn_modulerundetail, msdyn_plan, msdyn_planartifact, msdyn_planattachment, msdyn_pmanalysishistory, msdyn_pmbusinessruleautomationconfig, msdyn_pmcalendar, msdyn_pmcalendarversion, msdyn_pminferredtask, msdyn_pmprocessextendedmetadataversion, msdyn_pmprocesstemplate, msdyn_pmprocessusersettings, msdyn_pmprocessversion, msdyn_pmrecording, msdyn_pmsimulation, msdyn_pmtab, msdyn_pmtemplate, msdyn_pmview, msdyn_qna, msdyn_richtextfile, msdyn_salesforcestructuredobject, msdyn_salesforcestructuredqnaconfig, msdyn_schedule, msdyn_serviceconfiguration, msdyn_slakpi, msdyn_solutionhealthrule, msdyn_solutionhealthruleargument, msdyn_solutionhealthruleset, msdyn_tour, msdyn_virtualtablecolumncandidate, msdyn_workflowactionstatus, msgraphresourcetosubscription, mspcat_catalogsubmissionfiles, mspcat_packagestore, organization, organizationdatasyncfnostate, organizationdatasyncstate, organizationdatasyncsubscription, organizationdatasyncsubscriptionentity, organizationdatasyncsubscriptionfnotable, organizationsetting, package, packagehistory, pdfsetting, phonecall, plannerbusinessscenario, plannersyncaction, plugin, pluginpackage, post, powerbidataset, powerbidatasetapdx, powerbimashupparameter, powerbireport, powerbireportapdx, powerfxrule, powerpagecomponent, powerpagesddosalert, powerpagesite, powerpagesitelanguage, powerpagesitepublished, powerpagesmanagedidentity, powerpagesscanreport, powerpagessourcefile, privilege, privilegecheckerlog, privilegecheckerrun, privilegesremovalsetting, processorregistration, processstageparameter, provisionlanguageforuser, purviewlabelinfo, purviewlabelsynccache, quarterlyfiscalcalendar, queue, queueitem, reconciliationentityinfo, reconciliationentitystepinfo, reconciliationinfo, recordfilter, recurringappointmentmaster, recyclebinconfig, relationshipattribute, relationshiprole, relationshiprolemap, reportparameter, retaineddataexcel, retentioncleanupinfo, retentioncleanupoperation, retentionconfig, retentionfailuredetail, retentionoperation, retentionoperationdetail, retentionsuccessdetail, revokeinheritedaccessrecordstracker, role, roleeditorlayout, routingrule, routingruleitem, savedquery, savingrule, sa_suggestedaction, sa_suggestedactioncriteria, searchattributesettings, searchcustomanalyzer, searchrelationshipsettings, semiannualfiscalcalendar, sensitivitylabelattributemapping, serviceplan, serviceplancustomcontrol, serviceplanmapping, settingdefinition, sharedlinksetting, sharedobject, sharedworkspace, sharedworkspacepool, sharepointmanagedidentity, sideloadedaiplugin, signalregistration, sla, socialactivity, solutioncomponentattributeconfiguration, solutioncomponentbatchconfiguration, solutioncomponentconfiguration, solutioncomponentrelationshipconfiguration, stagedattributelookupvalue, stagedattributepicklistvalue, stagedentity, stagedentityattribute, stagedentityrelationship, stagedentityrelationshiprelationships, stagedentityrelationshiprole, stagedmetadataasyncoperation, stagedoptionset, stagedrelationship, stagedrelationshipextracondition, stagedviewattribute, stagesolutionupload, subject, supportusertable, synapsedatabase, synapselinkexternaltablestate, synapselinkprofile, synapselinkprofileentity, synapselinkprofileentitystate, synapselinkschedule, systemform, systemuser, systemuserauthorizationchangetracker, tag, taggedflowsession, taggedprocess, task, tdsmetadata, team, teammobileofflineprofilemembership, template, territory, theme, toolinggateway, toolinggatewaymcpserver, traitregistration, unstructuredfilesearchentity, unstructuredfilesearchrecord, unstructuredfilesearchrecordstatus, userform, usermapping, usermobileofflineprofilemembership, userquery, userrating, uxagentcomponent, uxagentcomponentrevision, uxagentproject, uxagentprojectfile, viewasexamplequestion, virtualentitymetadata, workflowbinary, workflowmetadata, workqueue, workqueueitem|

### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [Account_BulkDeleteFailures](#BKMK_Account_BulkDeleteFailures)
- [activityfileattachment_BulkDeleteFailures](#BKMK_activityfileattachment_BulkDeleteFailures)
- [ActivityMimeAttachment_BulkDeleteFailures](#BKMK_ActivityMimeAttachment_BulkDeleteFailures)
- [ActivityPointer_BulkDeleteFailures](#BKMK_ActivityPointer_BulkDeleteFailures)
- [adx_externalidentity_BulkDeleteFailures](#BKMK_adx_externalidentity_BulkDeleteFailures)
- [adx_invitation_BulkDeleteFailures](#BKMK_adx_invitation_BulkDeleteFailures)
- [adx_inviteredemption_BulkDeleteFailures](#BKMK_adx_inviteredemption_BulkDeleteFailures)
- [adx_portalcomment_BulkDeleteFailures](#BKMK_adx_portalcomment_BulkDeleteFailures)
- [adx_setting_BulkDeleteFailures](#BKMK_adx_setting_BulkDeleteFailures)
- [adx_webformsession_BulkDeleteFailures](#BKMK_adx_webformsession_BulkDeleteFailures)
- [aicopilot_BulkDeleteFailures](#BKMK_aicopilot_BulkDeleteFailures)
- [aiplugin_BulkDeleteFailures](#BKMK_aiplugin_BulkDeleteFailures)
- [aipluginauth_BulkDeleteFailures](#BKMK_aipluginauth_BulkDeleteFailures)
- [aipluginconversationstarter_BulkDeleteFailures](#BKMK_aipluginconversationstarter_BulkDeleteFailures)
- [aipluginconversationstartermapping_BulkDeleteFailures](#BKMK_aipluginconversationstartermapping_BulkDeleteFailures)
- [aipluginexternalschema_BulkDeleteFailures](#BKMK_aipluginexternalschema_BulkDeleteFailures)
- [aipluginexternalschemaproperty_BulkDeleteFailures](#BKMK_aipluginexternalschemaproperty_BulkDeleteFailures)
- [aiplugingovernance_BulkDeleteFailures](#BKMK_aiplugingovernance_BulkDeleteFailures)
- [aiplugingovernanceext_BulkDeleteFailures](#BKMK_aiplugingovernanceext_BulkDeleteFailures)
- [aiplugininstance_BulkDeleteFailures](#BKMK_aiplugininstance_BulkDeleteFailures)
- [aipluginoperation_BulkDeleteFailures](#BKMK_aipluginoperation_BulkDeleteFailures)
- [aipluginoperationparameter_BulkDeleteFailures](#BKMK_aipluginoperationparameter_BulkDeleteFailures)
- [aipluginoperationresponsetemplate_BulkDeleteFailures](#BKMK_aipluginoperationresponsetemplate_BulkDeleteFailures)
- [aiplugintitle_BulkDeleteFailures](#BKMK_aiplugintitle_BulkDeleteFailures)
- [aipluginusersetting_BulkDeleteFailures](#BKMK_aipluginusersetting_BulkDeleteFailures)
- [allowedmcpclient_BulkDeleteFailures](#BKMK_allowedmcpclient_BulkDeleteFailures)
- [Annotation_BulkDeleteFailures](#BKMK_Annotation_BulkDeleteFailures)
- [AnnualFiscalCalendar_BulkDeleteFailures](#BKMK_AnnualFiscalCalendar_BulkDeleteFailures)
- [appaction_BulkDeleteFailures](#BKMK_appaction_BulkDeleteFailures)
- [appactionmigration_BulkDeleteFailures](#BKMK_appactionmigration_BulkDeleteFailures)
- [appactionrule_BulkDeleteFailures](#BKMK_appactionrule_BulkDeleteFailures)
- [application_BulkDeleteFailures](#BKMK_application_BulkDeleteFailures)
- [applicationuser_BulkDeleteFailures](#BKMK_applicationuser_BulkDeleteFailures)
- [Appointment_BulkDeleteFailures](#BKMK_Appointment_BulkDeleteFailures)
- [approvalprocess_BulkDeleteFailures](#BKMK_approvalprocess_BulkDeleteFailures)
- [approvalstageapproval_BulkDeleteFailures](#BKMK_approvalstageapproval_BulkDeleteFailures)
- [approvalstagecondition_BulkDeleteFailures](#BKMK_approvalstagecondition_BulkDeleteFailures)
- [approvalstageintelligent_BulkDeleteFailures](#BKMK_approvalstageintelligent_BulkDeleteFailures)
- [approvalstageorder_BulkDeleteFailures](#BKMK_approvalstageorder_BulkDeleteFailures)
- [attributeclusterconfig_BulkDeleteFailures](#BKMK_attributeclusterconfig_BulkDeleteFailures)
- [attributeimageconfig_BulkDeleteFailures](#BKMK_attributeimageconfig_BulkDeleteFailures)
- [attributemaskingrule_BulkDeleteFailures](#BKMK_attributemaskingrule_BulkDeleteFailures)
- [attributepicklistvalue_BulkDeleteFailures](#BKMK_attributepicklistvalue_BulkDeleteFailures)
- [bot_BulkDeleteFailures](#BKMK_bot_BulkDeleteFailures)
- [botcomponent_BulkDeleteFailures](#BKMK_botcomponent_BulkDeleteFailures)
- [botcomponentcollection_BulkDeleteFailures](#BKMK_botcomponentcollection_BulkDeleteFailures)
- [BulkDeleteOperation_BulkDeleteFailure](#BKMK_BulkDeleteOperation_BulkDeleteFailure)
- [businessprocess_BulkDeleteFailures](#BKMK_businessprocess_BulkDeleteFailures)
- [BusinessUnit_BulkDeleteFailures](#BKMK_BusinessUnit_BulkDeleteFailures)
- [BusinessUnitNewsArticle_BulkDeleteFailures](#BKMK_BusinessUnitNewsArticle_BulkDeleteFailures)
- [Calendar_BulkDeleteFailures](#BKMK_Calendar_BulkDeleteFailures)
- [card_BulkDeleteFailures](#BKMK_card_BulkDeleteFailures)
- [catalog_BulkDeleteFailures](#BKMK_catalog_BulkDeleteFailures)
- [catalogassignment_BulkDeleteFailures](#BKMK_catalogassignment_BulkDeleteFailures)
- [certificatecredential_BulkDeleteFailures](#BKMK_certificatecredential_BulkDeleteFailures)
- [chat_BulkDeleteFailures](#BKMK_chat_BulkDeleteFailures)
- [connectioninstance_BulkDeleteFailures](#BKMK_connectioninstance_BulkDeleteFailures)
- [connectionreference_BulkDeleteFailures](#BKMK_connectionreference_BulkDeleteFailures)
- [connector_BulkDeleteFailures](#BKMK_connector_BulkDeleteFailures)
- [Contact_BulkDeleteFailures](#BKMK_Contact_BulkDeleteFailures)
- [conversationtranscript_BulkDeleteFailures](#BKMK_conversationtranscript_BulkDeleteFailures)
- [copilotexamplequestion_BulkDeleteFailures](#BKMK_copilotexamplequestion_BulkDeleteFailures)
- [copilotglossaryterm_BulkDeleteFailures](#BKMK_copilotglossaryterm_BulkDeleteFailures)
- [copilotsynonyms_BulkDeleteFailures](#BKMK_copilotsynonyms_BulkDeleteFailures)
- [credential_BulkDeleteFailures](#BKMK_credential_BulkDeleteFailures)
- [customapi_BulkDeleteFailures](#BKMK_customapi_BulkDeleteFailures)
- [customapirequestparameter_BulkDeleteFailures](#BKMK_customapirequestparameter_BulkDeleteFailures)
- [customapiresponseproperty_BulkDeleteFailures](#BKMK_customapiresponseproperty_BulkDeleteFailures)
- [CustomerAddress_BulkDeleteFailures](#BKMK_CustomerAddress_BulkDeleteFailures)
- [datalakefolder_BulkDeleteFailures](#BKMK_datalakefolder_BulkDeleteFailures)
- [datalakefolderpermission_BulkDeleteFailures](#BKMK_datalakefolderpermission_BulkDeleteFailures)
- [datalakeworkspace_BulkDeleteFailures](#BKMK_datalakeworkspace_BulkDeleteFailures)
- [datalakeworkspacepermission_BulkDeleteFailures](#BKMK_datalakeworkspacepermission_BulkDeleteFailures)
- [dataprocessingconfiguration_BulkDeleteFailures](#BKMK_dataprocessingconfiguration_BulkDeleteFailures)
- [delegatedauthorization_BulkDeleteFailures](#BKMK_delegatedauthorization_BulkDeleteFailures)
- [desktopflowbinary_BulkDeleteFailures](#BKMK_desktopflowbinary_BulkDeleteFailures)
- [desktopflowmodule_BulkDeleteFailures](#BKMK_desktopflowmodule_BulkDeleteFailures)
- [DisplayString_BulkDeleteFailures](#BKMK_DisplayString_BulkDeleteFailures)
- [dvfilesearch_BulkDeleteFailures](#BKMK_dvfilesearch_BulkDeleteFailures)
- [dvfilesearchattribute_BulkDeleteFailures](#BKMK_dvfilesearchattribute_BulkDeleteFailures)
- [dvfilesearchentity_BulkDeleteFailures](#BKMK_dvfilesearchentity_BulkDeleteFailures)
- [dvtablesearch_BulkDeleteFailures](#BKMK_dvtablesearch_BulkDeleteFailures)
- [dvtablesearchattribute_BulkDeleteFailures](#BKMK_dvtablesearchattribute_BulkDeleteFailures)
- [dvtablesearchentity_BulkDeleteFailures](#BKMK_dvtablesearchentity_BulkDeleteFailures)
- [Email_BulkDeleteFailures](#BKMK_Email_BulkDeleteFailures)
- [emailaddressconfiguration_BulkDeleteFailures](#BKMK_emailaddressconfiguration_BulkDeleteFailures)
- [emailserverprofile_bulkdeletefailures](#BKMK_emailserverprofile_bulkdeletefailures)
- [entityanalyticsconfig_BulkDeleteFailures](#BKMK_entityanalyticsconfig_BulkDeleteFailures)
- [entityclusterconfig_BulkDeleteFailures](#BKMK_entityclusterconfig_BulkDeleteFailures)
- [entityimageconfig_BulkDeleteFailures](#BKMK_entityimageconfig_BulkDeleteFailures)
- [entityindex_BulkDeleteFailures](#BKMK_entityindex_BulkDeleteFailures)
- [entityrecordfilter_BulkDeleteFailures](#BKMK_entityrecordfilter_BulkDeleteFailures)
- [environmentvariabledefinition_BulkDeleteFailures](#BKMK_environmentvariabledefinition_BulkDeleteFailures)
- [environmentvariablevalue_BulkDeleteFailures](#BKMK_environmentvariablevalue_BulkDeleteFailures)
- [exportedexcel_BulkDeleteFailures](#BKMK_exportedexcel_BulkDeleteFailures)
- [exportsolutionupload_BulkDeleteFailures](#BKMK_exportsolutionupload_BulkDeleteFailures)
- [fabricaiskill_BulkDeleteFailures](#BKMK_fabricaiskill_BulkDeleteFailures)
- [Fax_BulkDeleteFailures](#BKMK_Fax_BulkDeleteFailures)
- [featurecontrolsetting_BulkDeleteFailures](#BKMK_featurecontrolsetting_BulkDeleteFailures)
- [federatedknowledgeconfiguration_BulkDeleteFailures](#BKMK_federatedknowledgeconfiguration_BulkDeleteFailures)
- [federatedknowledgeentityconfiguration_BulkDeleteFailures](#BKMK_federatedknowledgeentityconfiguration_BulkDeleteFailures)
- [FixedMonthlyFiscalCalendar_BulkDeleteFailures](#BKMK_FixedMonthlyFiscalCalendar_BulkDeleteFailures)
- [flowcapacityassignment_BulkDeleteFailures](#BKMK_flowcapacityassignment_BulkDeleteFailures)
- [flowcredentialapplication_BulkDeleteFailures](#BKMK_flowcredentialapplication_BulkDeleteFailures)
- [flowevent_BulkDeleteFailures](#BKMK_flowevent_BulkDeleteFailures)
- [flowmachine_BulkDeleteFailures](#BKMK_flowmachine_BulkDeleteFailures)
- [flowmachinegroup_BulkDeleteFailures](#BKMK_flowmachinegroup_BulkDeleteFailures)
- [flowmachineimage_BulkDeleteFailures](#BKMK_flowmachineimage_BulkDeleteFailures)
- [flowmachineimageversion_BulkDeleteFailures](#BKMK_flowmachineimageversion_BulkDeleteFailures)
- [flowmachinenetwork_BulkDeleteFailures](#BKMK_flowmachinenetwork_BulkDeleteFailures)
- [flowsession_BulkDeleteFailures](#BKMK_flowsession_BulkDeleteFailures)
- [flowsessionbinary_BulkDeleteFailures](#BKMK_flowsessionbinary_BulkDeleteFailures)
- [fxexpression_BulkDeleteFailures](#BKMK_fxexpression_BulkDeleteFailures)
- [governanceconfiguration_BulkDeleteFailures](#BKMK_governanceconfiguration_BulkDeleteFailures)
- [Import_BulkDeleteFailures](#BKMK_Import_BulkDeleteFailures)
- [ImportData_BulkDeleteFailures](#BKMK_ImportData_BulkDeleteFailures)
- [ImportFile_BulkDeleteFailures](#BKMK_ImportFile_BulkDeleteFailures)
- [ImportLog_BulkDeleteFailures](#BKMK_ImportLog_BulkDeleteFailures)
- [ImportMap_BulkDeleteFailures](#BKMK_ImportMap_BulkDeleteFailures)
- [indexattributes_BulkDeleteFailures](#BKMK_indexattributes_BulkDeleteFailures)
- [KbArticle_BulkDeleteFailures](#BKMK_KbArticle_BulkDeleteFailures)
- [KbArticleComment_BulkDeleteFailures](#BKMK_KbArticleComment_BulkDeleteFailures)
- [KbArticleTemplate_BulkDeleteFailures](#BKMK_KbArticleTemplate_BulkDeleteFailures)
- [keyvaultreference_BulkDeleteFailures](#BKMK_keyvaultreference_BulkDeleteFailures)
- [knowledgearticle_BulkDeleteFailures](#BKMK_knowledgearticle_BulkDeleteFailures)
- [KnowledgeBaseRecord_BulkDeleteFailures](#BKMK_KnowledgeBaseRecord_BulkDeleteFailures)
- [knowledgefaq_BulkDeleteFailures](#BKMK_knowledgefaq_BulkDeleteFailures)
- [Letter_BulkDeleteFailures](#BKMK_Letter_BulkDeleteFailures)
- [mainfewshot_BulkDeleteFailures](#BKMK_mainfewshot_BulkDeleteFailures)
- [makerfewshot_BulkDeleteFailures](#BKMK_makerfewshot_BulkDeleteFailures)
- [managedidentity_BulkDeleteFailures](#BKMK_managedidentity_BulkDeleteFailures)
- [maskingrule_BulkDeleteFailures](#BKMK_maskingrule_BulkDeleteFailures)
- [mcpserver_BulkDeleteFailures](#BKMK_mcpserver_BulkDeleteFailures)
- [mcptool_BulkDeleteFailures](#BKMK_mcptool_BulkDeleteFailures)
- [metadataforarchival_BulkDeleteFailures](#BKMK_metadataforarchival_BulkDeleteFailures)
- [mobileofflineprofileextension_BulkDeleteFailures](#BKMK_mobileofflineprofileextension_BulkDeleteFailures)
- [MonthlyFiscalCalendar_BulkDeleteFailures](#BKMK_MonthlyFiscalCalendar_BulkDeleteFailures)
- [msdyn_aibdataset_BulkDeleteFailures](#BKMK_msdyn_aibdataset_BulkDeleteFailures)
- [msdyn_aibdatasetfile_BulkDeleteFailures](#BKMK_msdyn_aibdatasetfile_BulkDeleteFailures)
- [msdyn_aibdatasetrecord_BulkDeleteFailures](#BKMK_msdyn_aibdatasetrecord_BulkDeleteFailures)
- [msdyn_aibdatasetscontainer_BulkDeleteFailures](#BKMK_msdyn_aibdatasetscontainer_BulkDeleteFailures)
- [msdyn_aibfeedbackloop_BulkDeleteFailures](#BKMK_msdyn_aibfeedbackloop_BulkDeleteFailures)
- [msdyn_aibfile_BulkDeleteFailures](#BKMK_msdyn_aibfile_BulkDeleteFailures)
- [msdyn_aibfileattacheddata_BulkDeleteFailures](#BKMK_msdyn_aibfileattacheddata_BulkDeleteFailures)
- [msdyn_aiconfiguration_BulkDeleteFailures](#BKMK_msdyn_aiconfiguration_BulkDeleteFailures)
- [msdyn_aidataprocessingevent_BulkDeleteFailures](#BKMK_msdyn_aidataprocessingevent_BulkDeleteFailures)
- [msdyn_aidocumenttemplate_BulkDeleteFailures](#BKMK_msdyn_aidocumenttemplate_BulkDeleteFailures)
- [msdyn_aievaluationconfiguration_BulkDeleteFailures](#BKMK_msdyn_aievaluationconfiguration_BulkDeleteFailures)
- [msdyn_aievaluationrun_BulkDeleteFailures](#BKMK_msdyn_aievaluationrun_BulkDeleteFailures)
- [msdyn_aievent_BulkDeleteFailures](#BKMK_msdyn_aievent_BulkDeleteFailures)
- [msdyn_aifptrainingdocument_BulkDeleteFailures](#BKMK_msdyn_aifptrainingdocument_BulkDeleteFailures)
- [msdyn_aimodel_BulkDeleteFailures](#BKMK_msdyn_aimodel_BulkDeleteFailures)
- [msdyn_aiodimage_BulkDeleteFailures](#BKMK_msdyn_aiodimage_BulkDeleteFailures)
- [msdyn_aiodlabel_BulkDeleteFailures](#BKMK_msdyn_aiodlabel_BulkDeleteFailures)
- [msdyn_aiodtrainingboundingbox_BulkDeleteFailures](#BKMK_msdyn_aiodtrainingboundingbox_BulkDeleteFailures)
- [msdyn_aiodtrainingimage_BulkDeleteFailures](#BKMK_msdyn_aiodtrainingimage_BulkDeleteFailures)
- [msdyn_aitemplate_BulkDeleteFailures](#BKMK_msdyn_aitemplate_BulkDeleteFailures)
- [msdyn_aitestcase_BulkDeleteFailures](#BKMK_msdyn_aitestcase_BulkDeleteFailures)
- [msdyn_aitestcasedocument_BulkDeleteFailures](#BKMK_msdyn_aitestcasedocument_BulkDeleteFailures)
- [msdyn_aitestcaseinput_BulkDeleteFailures](#BKMK_msdyn_aitestcaseinput_BulkDeleteFailures)
- [msdyn_aitestrun_BulkDeleteFailures](#BKMK_msdyn_aitestrun_BulkDeleteFailures)
- [msdyn_aitestrunbatch_BulkDeleteFailures](#BKMK_msdyn_aitestrunbatch_BulkDeleteFailures)
- [msdyn_analysiscomponent_BulkDeleteFailures](#BKMK_msdyn_analysiscomponent_BulkDeleteFailures)
- [msdyn_analysisjob_BulkDeleteFailures](#BKMK_msdyn_analysisjob_BulkDeleteFailures)
- [msdyn_analysisoverride_BulkDeleteFailures](#BKMK_msdyn_analysisoverride_BulkDeleteFailures)
- [msdyn_analysisresult_BulkDeleteFailures](#BKMK_msdyn_analysisresult_BulkDeleteFailures)
- [msdyn_analysisresultdetail_BulkDeleteFailures](#BKMK_msdyn_analysisresultdetail_BulkDeleteFailures)
- [msdyn_appinsightsmetadata_BulkDeleteFailures](#BKMK_msdyn_appinsightsmetadata_BulkDeleteFailures)
- [msdyn_copilotinteractions_BulkDeleteFailures](#BKMK_msdyn_copilotinteractions_BulkDeleteFailures)
- [msdyn_customcontrolextendedsettings_BulkDeleteFailures](#BKMK_msdyn_customcontrolextendedsettings_BulkDeleteFailures)
- [msdyn_dataflow_BulkDeleteFailures](#BKMK_msdyn_dataflow_BulkDeleteFailures)
- [msdyn_dataflow_datalakefolder_BulkDeleteFailures](#BKMK_msdyn_dataflow_datalakefolder_BulkDeleteFailures)
- [msdyn_dataflowconnectionreference_BulkDeleteFailures](#BKMK_msdyn_dataflowconnectionreference_BulkDeleteFailures)
- [msdyn_dataflowrefreshhistory_BulkDeleteFailures](#BKMK_msdyn_dataflowrefreshhistory_BulkDeleteFailures)
- [msdyn_dataflowtemplate_BulkDeleteFailures](#BKMK_msdyn_dataflowtemplate_BulkDeleteFailures)
- [msdyn_dmsrequest_BulkDeleteFailures](#BKMK_msdyn_dmsrequest_BulkDeleteFailures)
- [msdyn_dmsrequeststatus_BulkDeleteFailures](#BKMK_msdyn_dmsrequeststatus_BulkDeleteFailures)
- [msdyn_dmssyncrequest_BulkDeleteFailures](#BKMK_msdyn_dmssyncrequest_BulkDeleteFailures)
- [msdyn_dmssyncstatus_BulkDeleteFailures](#BKMK_msdyn_dmssyncstatus_BulkDeleteFailures)
- [msdyn_entitylinkchatconfiguration_BulkDeleteFailures](#BKMK_msdyn_entitylinkchatconfiguration_BulkDeleteFailures)
- [msdyn_entityrefreshhistory_BulkDeleteFailures](#BKMK_msdyn_entityrefreshhistory_BulkDeleteFailures)
- [msdyn_favoriteknowledgearticle_BulkDeleteFailures](#BKMK_msdyn_favoriteknowledgearticle_BulkDeleteFailures)
- [msdyn_federatedarticle_BulkDeleteFailures](#BKMK_msdyn_federatedarticle_BulkDeleteFailures)
- [msdyn_federatedarticleincident_BulkDeleteFailures](#BKMK_msdyn_federatedarticleincident_BulkDeleteFailures)
- [msdyn_fileupload_BulkDeleteFailures](#BKMK_msdyn_fileupload_BulkDeleteFailures)
- [msdyn_flow_actionapprovalmodel_BulkDeleteFailures](#BKMK_msdyn_flow_actionapprovalmodel_BulkDeleteFailures)
- [msdyn_flow_approval_BulkDeleteFailures](#BKMK_msdyn_flow_approval_BulkDeleteFailures)
- [msdyn_flow_approvalrequest_BulkDeleteFailures](#BKMK_msdyn_flow_approvalrequest_BulkDeleteFailures)
- [msdyn_flow_approvalresponse_BulkDeleteFailures](#BKMK_msdyn_flow_approvalresponse_BulkDeleteFailures)
- [msdyn_flow_approvalstep_BulkDeleteFailures](#BKMK_msdyn_flow_approvalstep_BulkDeleteFailures)
- [msdyn_flow_awaitallactionapprovalmodel_BulkDeleteFailures](#BKMK_msdyn_flow_awaitallactionapprovalmodel_BulkDeleteFailures)
- [msdyn_flow_awaitallapprovalmodel_BulkDeleteFailures](#BKMK_msdyn_flow_awaitallapprovalmodel_BulkDeleteFailures)
- [msdyn_flow_basicapprovalmodel_BulkDeleteFailures](#BKMK_msdyn_flow_basicapprovalmodel_BulkDeleteFailures)
- [msdyn_flow_flowapproval_BulkDeleteFailures](#BKMK_msdyn_flow_flowapproval_BulkDeleteFailures)
- [msdyn_formmapping_BulkDeleteFailures](#BKMK_msdyn_formmapping_BulkDeleteFailures)
- [msdyn_function_BulkDeleteFailures](#BKMK_msdyn_function_BulkDeleteFailures)
- [msdyn_helppage_BulkDeleteFailures](#BKMK_msdyn_helppage_BulkDeleteFailures)
- [msdyn_historicalcaseharvestbatch_BulkDeleteFailures](#BKMK_msdyn_historicalcaseharvestbatch_BulkDeleteFailures)
- [msdyn_historicalcaseharvestrun_BulkDeleteFailures](#BKMK_msdyn_historicalcaseharvestrun_BulkDeleteFailures)
- [msdyn_insightsstorevirtualentity_BulkDeleteFailures](#BKMK_msdyn_insightsstorevirtualentity_BulkDeleteFailures)
- [msdyn_integratedsearchprovider_BulkDeleteFailures](#BKMK_msdyn_integratedsearchprovider_BulkDeleteFailures)
- [msdyn_kalanguagesetting_BulkDeleteFailures](#BKMK_msdyn_kalanguagesetting_BulkDeleteFailures)
- [msdyn_kbattachment_BulkDeleteFailures](#BKMK_msdyn_kbattachment_BulkDeleteFailures)
- [msdyn_kmfederatedsearchconfig_BulkDeleteFailures](#BKMK_msdyn_kmfederatedsearchconfig_BulkDeleteFailures)
- [msdyn_kmpersonalizationsetting_BulkDeleteFailures](#BKMK_msdyn_kmpersonalizationsetting_BulkDeleteFailures)
- [msdyn_knowledgearticleimage_BulkDeleteFailures](#BKMK_msdyn_knowledgearticleimage_BulkDeleteFailures)
- [msdyn_knowledgearticletemplate_BulkDeleteFailures](#BKMK_msdyn_knowledgearticletemplate_BulkDeleteFailures)
- [msdyn_knowledgeassetconfiguration_BulkDeleteFailures](#BKMK_msdyn_knowledgeassetconfiguration_BulkDeleteFailures)
- [msdyn_knowledgeconfiguration_BulkDeleteFailures](#BKMK_msdyn_knowledgeconfiguration_BulkDeleteFailures)
- [msdyn_knowledgeharvestjobrecord_BulkDeleteFailures](#BKMK_msdyn_knowledgeharvestjobrecord_BulkDeleteFailures)
- [msdyn_knowledgeinteractioninsight_BulkDeleteFailures](#BKMK_msdyn_knowledgeinteractioninsight_BulkDeleteFailures)
- [msdyn_knowledgemanagementsetting_BulkDeleteFailures](#BKMK_msdyn_knowledgemanagementsetting_BulkDeleteFailures)
- [msdyn_knowledgepersonalfilter_BulkDeleteFailures](#BKMK_msdyn_knowledgepersonalfilter_BulkDeleteFailures)
- [msdyn_knowledgesearchfilter_BulkDeleteFailures](#BKMK_msdyn_knowledgesearchfilter_BulkDeleteFailures)
- [msdyn_knowledgesearchinsight_BulkDeleteFailures](#BKMK_msdyn_knowledgesearchinsight_BulkDeleteFailures)
- [msdyn_mobileapp_BulkDeleteFailures](#BKMK_msdyn_mobileapp_BulkDeleteFailures)
- [msdyn_modulerundetail_BulkDeleteFailures](#BKMK_msdyn_modulerundetail_BulkDeleteFailures)
- [msdyn_pmanalysishistory_BulkDeleteFailures](#BKMK_msdyn_pmanalysishistory_BulkDeleteFailures)
- [msdyn_pmbusinessruleautomationconfig_BulkDeleteFailures](#BKMK_msdyn_pmbusinessruleautomationconfig_BulkDeleteFailures)
- [msdyn_pmcalendar_BulkDeleteFailures](#BKMK_msdyn_pmcalendar_BulkDeleteFailures)
- [msdyn_pmcalendarversion_BulkDeleteFailures](#BKMK_msdyn_pmcalendarversion_BulkDeleteFailures)
- [msdyn_pminferredtask_BulkDeleteFailures](#BKMK_msdyn_pminferredtask_BulkDeleteFailures)
- [msdyn_pmprocessextendedmetadataversion_BulkDeleteFailures](#BKMK_msdyn_pmprocessextendedmetadataversion_BulkDeleteFailures)
- [msdyn_pmprocesstemplate_BulkDeleteFailures](#BKMK_msdyn_pmprocesstemplate_BulkDeleteFailures)
- [msdyn_pmprocessusersettings_BulkDeleteFailures](#BKMK_msdyn_pmprocessusersettings_BulkDeleteFailures)
- [msdyn_pmprocessversion_BulkDeleteFailures](#BKMK_msdyn_pmprocessversion_BulkDeleteFailures)
- [msdyn_pmrecording_BulkDeleteFailures](#BKMK_msdyn_pmrecording_BulkDeleteFailures)
- [msdyn_pmsimulation_BulkDeleteFailures](#BKMK_msdyn_pmsimulation_BulkDeleteFailures)
- [msdyn_pmtab_BulkDeleteFailures](#BKMK_msdyn_pmtab_BulkDeleteFailures)
- [msdyn_pmtemplate_BulkDeleteFailures](#BKMK_msdyn_pmtemplate_BulkDeleteFailures)
- [msdyn_pmview_BulkDeleteFailures](#BKMK_msdyn_pmview_BulkDeleteFailures)
- [msdyn_qna_BulkDeleteFailures](#BKMK_msdyn_qna_BulkDeleteFailures)
- [msdyn_richtextfile_BulkDeleteFailures](#BKMK_msdyn_richtextfile_BulkDeleteFailures)
- [msdyn_salesforcestructuredobject_BulkDeleteFailures](#BKMK_msdyn_salesforcestructuredobject_BulkDeleteFailures)
- [msdyn_salesforcestructuredqnaconfig_BulkDeleteFailures](#BKMK_msdyn_salesforcestructuredqnaconfig_BulkDeleteFailures)
- [msdyn_schedule_BulkDeleteFailures](#BKMK_msdyn_schedule_BulkDeleteFailures)
- [msdyn_serviceconfiguration_BulkDeleteFailures](#BKMK_msdyn_serviceconfiguration_BulkDeleteFailures)
- [msdyn_slakpi_BulkDeleteFailures](#BKMK_msdyn_slakpi_BulkDeleteFailures)
- [msdyn_solutionhealthrule_BulkDeleteFailures](#BKMK_msdyn_solutionhealthrule_BulkDeleteFailures)
- [msdyn_solutionhealthruleargument_BulkDeleteFailures](#BKMK_msdyn_solutionhealthruleargument_BulkDeleteFailures)
- [msdyn_solutionhealthruleset_BulkDeleteFailures](#BKMK_msdyn_solutionhealthruleset_BulkDeleteFailures)
- [msdyn_tour_BulkDeleteFailures](#BKMK_msdyn_tour_BulkDeleteFailures)
- [msdyn_virtualtablecolumncandidate_BulkDeleteFailures](#BKMK_msdyn_virtualtablecolumncandidate_BulkDeleteFailures)
- [msdyn_workflowactionstatus_BulkDeleteFailures](#BKMK_msdyn_workflowactionstatus_BulkDeleteFailures)
- [msdynce_botcontent_BulkDeleteFailures](#BKMK_msdynce_botcontent_BulkDeleteFailures)
- [msgraphresourcetosubscription_BulkDeleteFailures](#BKMK_msgraphresourcetosubscription_BulkDeleteFailures)
- [mspcat_catalogsubmissionfiles_BulkDeleteFailures](#BKMK_mspcat_catalogsubmissionfiles_BulkDeleteFailures)
- [mspcat_packagestore_BulkDeleteFailures](#BKMK_mspcat_packagestore_BulkDeleteFailures)
- [Organization_BulkDeleteFailures](#BKMK_Organization_BulkDeleteFailures)
- [organizationdatasyncfnostate_BulkDeleteFailures](#BKMK_organizationdatasyncfnostate_BulkDeleteFailures)
- [organizationdatasyncstate_BulkDeleteFailures](#BKMK_organizationdatasyncstate_BulkDeleteFailures)
- [organizationdatasyncsubscription_BulkDeleteFailures](#BKMK_organizationdatasyncsubscription_BulkDeleteFailures)
- [organizationdatasyncsubscriptionentity_BulkDeleteFailures](#BKMK_organizationdatasyncsubscriptionentity_BulkDeleteFailures)
- [organizationdatasyncsubscriptionfnotable_BulkDeleteFailures](#BKMK_organizationdatasyncsubscriptionfnotable_BulkDeleteFailures)
- [package_BulkDeleteFailures](#BKMK_package_BulkDeleteFailures)
- [packagehistory_BulkDeleteFailures](#BKMK_packagehistory_BulkDeleteFailures)
- [PhoneCall_BulkDeleteFailures](#BKMK_PhoneCall_BulkDeleteFailures)
- [plannerbusinessscenario_BulkDeleteFailures](#BKMK_plannerbusinessscenario_BulkDeleteFailures)
- [plannersyncaction_BulkDeleteFailures](#BKMK_plannersyncaction_BulkDeleteFailures)
- [plugin_BulkDeleteFailures](#BKMK_plugin_BulkDeleteFailures)
- [pluginpackage_BulkDeleteFailures](#BKMK_pluginpackage_BulkDeleteFailures)
- [post_BulkDeleteFailures](#BKMK_post_BulkDeleteFailures)
- [powerbidataset_BulkDeleteFailures](#BKMK_powerbidataset_BulkDeleteFailures)
- [powerbidatasetapdx_BulkDeleteFailures](#BKMK_powerbidatasetapdx_BulkDeleteFailures)
- [powerbimashupparameter_BulkDeleteFailures](#BKMK_powerbimashupparameter_BulkDeleteFailures)
- [powerbireport_BulkDeleteFailures](#BKMK_powerbireport_BulkDeleteFailures)
- [powerbireportapdx_BulkDeleteFailures](#BKMK_powerbireportapdx_BulkDeleteFailures)
- [powerfxrule_BulkDeleteFailures](#BKMK_powerfxrule_BulkDeleteFailures)
- [powerpagecomponent_BulkDeleteFailures](#BKMK_powerpagecomponent_BulkDeleteFailures)
- [powerpagesddosalert_BulkDeleteFailures](#BKMK_powerpagesddosalert_BulkDeleteFailures)
- [powerpagesite_BulkDeleteFailures](#BKMK_powerpagesite_BulkDeleteFailures)
- [powerpagesitelanguage_BulkDeleteFailures](#BKMK_powerpagesitelanguage_BulkDeleteFailures)
- [powerpagesitepublished_BulkDeleteFailures](#BKMK_powerpagesitepublished_BulkDeleteFailures)
- [powerpagesmanagedidentity_BulkDeleteFailures](#BKMK_powerpagesmanagedidentity_BulkDeleteFailures)
- [powerpagesscanreport_BulkDeleteFailures](#BKMK_powerpagesscanreport_BulkDeleteFailures)
- [powerpagessourcefile_BulkDeleteFailures](#BKMK_powerpagessourcefile_BulkDeleteFailures)
- [Privilege_BulkDeleteFailures](#BKMK_Privilege_BulkDeleteFailures)
- [privilegecheckerlog_BulkDeleteFailures](#BKMK_privilegecheckerlog_BulkDeleteFailures)
- [privilegecheckerrun_BulkDeleteFailures](#BKMK_privilegecheckerrun_BulkDeleteFailures)
- [privilegesremovalsetting_BulkDeleteFailures](#BKMK_privilegesremovalsetting_BulkDeleteFailures)
- [processstageparameter_BulkDeleteFailures](#BKMK_processstageparameter_BulkDeleteFailures)
- [provisionlanguageforuser_BulkDeleteFailures](#BKMK_provisionlanguageforuser_BulkDeleteFailures)
- [purviewlabelinfo_BulkDeleteFailures](#BKMK_purviewlabelinfo_BulkDeleteFailures)
- [QuarterlyFiscalCalendar_BulkDeleteFailures](#BKMK_QuarterlyFiscalCalendar_BulkDeleteFailures)
- [Queue_BulkDeleteFailures](#BKMK_Queue_BulkDeleteFailures)
- [QueueItem_BulkDeleteFailures](#BKMK_QueueItem_BulkDeleteFailures)
- [recordfilter_BulkDeleteFailures](#BKMK_recordfilter_BulkDeleteFailures)
- [RecurringAppointmentMaster_BulkDeleteFailures](#BKMK_RecurringAppointmentMaster_BulkDeleteFailures)
- [recyclebinconfig_BulkDeleteFailures](#BKMK_recyclebinconfig_BulkDeleteFailures)
- [relationshipattribute_BulkDeleteFailures](#BKMK_relationshipattribute_BulkDeleteFailures)
- [reportparameter_BulkDeleteFailures](#BKMK_reportparameter_BulkDeleteFailures)
- [retaineddataexcel_BulkDeleteFailures](#BKMK_retaineddataexcel_BulkDeleteFailures)
- [retentionconfig_BulkDeleteFailures](#BKMK_retentionconfig_BulkDeleteFailures)
- [retentionfailuredetail_BulkDeleteFailures](#BKMK_retentionfailuredetail_BulkDeleteFailures)
- [retentionoperation_BulkDeleteFailures](#BKMK_retentionoperation_BulkDeleteFailures)
- [retentionoperationdetail_BulkDeleteFailures](#BKMK_retentionoperationdetail_BulkDeleteFailures)
- [retentionsuccessdetail_BulkDeleteFailures](#BKMK_retentionsuccessdetail_BulkDeleteFailures)
- [Role_BulkDeleteFailures](#BKMK_Role_BulkDeleteFailures)
- [roleeditorlayout_BulkDeleteFailures](#BKMK_roleeditorlayout_BulkDeleteFailures)
- [sa_suggestedaction_BulkDeleteFailures](#BKMK_sa_suggestedaction_BulkDeleteFailures)
- [sa_suggestedactioncriteria_BulkDeleteFailures](#BKMK_sa_suggestedactioncriteria_BulkDeleteFailures)
- [SavedQuery_BulkDeleteFailures](#BKMK_SavedQuery_BulkDeleteFailures)
- [savingrule_BulkDeleteFailures](#BKMK_savingrule_BulkDeleteFailures)
- [searchattributesettings_BulkDeleteFailures](#BKMK_searchattributesettings_BulkDeleteFailures)
- [searchcustomanalyzer_BulkDeleteFailures](#BKMK_searchcustomanalyzer_BulkDeleteFailures)
- [searchrelationshipsettings_BulkDeleteFailures](#BKMK_searchrelationshipsettings_BulkDeleteFailures)
- [SemiAnnualFiscalCalendar_BulkDeleteFailures](#BKMK_SemiAnnualFiscalCalendar_BulkDeleteFailures)
- [sensitivitylabelattributemapping_BulkDeleteFailures](#BKMK_sensitivitylabelattributemapping_BulkDeleteFailures)
- [serviceplan_BulkDeleteFailures](#BKMK_serviceplan_BulkDeleteFailures)
- [serviceplanmapping_BulkDeleteFailures](#BKMK_serviceplanmapping_BulkDeleteFailures)
- [sharedlinksetting_BulkDeleteFailures](#BKMK_sharedlinksetting_BulkDeleteFailures)
- [sharedobject_BulkDeleteFailures](#BKMK_sharedobject_BulkDeleteFailures)
- [sharedworkspace_BulkDeleteFailures](#BKMK_sharedworkspace_BulkDeleteFailures)
- [sharedworkspacepool_BulkDeleteFailures](#BKMK_sharedworkspacepool_BulkDeleteFailures)
- [sharepointmanagedidentity_BulkDeleteFailures](#BKMK_sharepointmanagedidentity_BulkDeleteFailures)
- [sideloadedaiplugin_BulkDeleteFailures](#BKMK_sideloadedaiplugin_BulkDeleteFailures)
- [slabase_BulkDeleteFailures](#BKMK_slabase_BulkDeleteFailures)
- [SocialActivity_BulkDeleteFailures](#BKMK_SocialActivity_BulkDeleteFailures)
- [solutioncomponentattributeconfiguration_BulkDeleteFailures](#BKMK_solutioncomponentattributeconfiguration_BulkDeleteFailures)
- [solutioncomponentbatchconfiguration_BulkDeleteFailures](#BKMK_solutioncomponentbatchconfiguration_BulkDeleteFailures)
- [solutioncomponentconfiguration_BulkDeleteFailures](#BKMK_solutioncomponentconfiguration_BulkDeleteFailures)
- [solutioncomponentrelationshipconfiguration_BulkDeleteFailures](#BKMK_solutioncomponentrelationshipconfiguration_BulkDeleteFailures)
- [stagedentity_BulkDeleteFailures](#BKMK_stagedentity_BulkDeleteFailures)
- [stagedentityattribute_BulkDeleteFailures](#BKMK_stagedentityattribute_BulkDeleteFailures)
- [stagedmetadataasyncoperation_BulkDeleteFailures](#BKMK_stagedmetadataasyncoperation_BulkDeleteFailures)
- [stagesolutionupload_BulkDeleteFailures](#BKMK_stagesolutionupload_BulkDeleteFailures)
- [Subject_BulkDeleteFailures](#BKMK_Subject_BulkDeleteFailures)
- [supportusertable_BulkDeleteFailures](#BKMK_supportusertable_BulkDeleteFailures)
- [synapsedatabase_BulkDeleteFailures](#BKMK_synapsedatabase_BulkDeleteFailures)
- [synapselinkexternaltablestate_BulkDeleteFailures](#BKMK_synapselinkexternaltablestate_BulkDeleteFailures)
- [synapselinkprofile_BulkDeleteFailures](#BKMK_synapselinkprofile_BulkDeleteFailures)
- [synapselinkprofileentity_BulkDeleteFailures](#BKMK_synapselinkprofileentity_BulkDeleteFailures)
- [synapselinkprofileentitystate_BulkDeleteFailures](#BKMK_synapselinkprofileentitystate_BulkDeleteFailures)
- [synapselinkschedule_BulkDeleteFailures](#BKMK_synapselinkschedule_BulkDeleteFailures)
- [SystemForm_BulkDeleteFailures](#BKMK_SystemForm_BulkDeleteFailures)
- [SystemUser_BulkDeleteFailures](#BKMK_SystemUser_BulkDeleteFailures)
- [systemuserauthorizationchangetracker_BulkDeleteFailures](#BKMK_systemuserauthorizationchangetracker_BulkDeleteFailures)
- [tag_BulkDeleteFailures](#BKMK_tag_BulkDeleteFailures)
- [taggedflowsession_BulkDeleteFailures](#BKMK_taggedflowsession_BulkDeleteFailures)
- [taggedprocess_BulkDeleteFailures](#BKMK_taggedprocess_BulkDeleteFailures)
- [Task_BulkDeleteFailures](#BKMK_Task_BulkDeleteFailures)
- [Team_BulkDeleteFailures](#BKMK_Team_BulkDeleteFailures)
- [teammobileofflineprofilemembership_BulkDeleteFailures](#BKMK_teammobileofflineprofilemembership_BulkDeleteFailures)
- [Template_BulkDeleteFailures](#BKMK_Template_BulkDeleteFailures)
- [Territory_BulkDeleteFailures](#BKMK_Territory_BulkDeleteFailures)
- [theme_BulkDeleteFailures](#BKMK_theme_BulkDeleteFailures)
- [unstructuredfilesearchentity_BulkDeleteFailures](#BKMK_unstructuredfilesearchentity_BulkDeleteFailures)
- [unstructuredfilesearchrecord_BulkDeleteFailures](#BKMK_unstructuredfilesearchrecord_BulkDeleteFailures)
- [UserForm_BulkDeleteFailures](#BKMK_UserForm_BulkDeleteFailures)
- [usermapping_BulkDeleteFailures](#BKMK_usermapping_BulkDeleteFailures)
- [usermobileofflineprofilemembership_BulkDeleteFailures](#BKMK_usermobileofflineprofilemembership_BulkDeleteFailures)
- [UserQuery_BulkDeleteFailures](#BKMK_UserQuery_BulkDeleteFailures)
- [userrating_BulkDeleteFailures](#BKMK_userrating_BulkDeleteFailures)
- [viewasexamplequestion_BulkDeleteFailures](#BKMK_viewasexamplequestion_BulkDeleteFailures)
- [virtualentitymetadata_BulkDeleteFailures](#BKMK_virtualentitymetadata_BulkDeleteFailures)
- [workflowbinary_BulkDeleteFailures](#BKMK_workflowbinary_BulkDeleteFailures)
- [workflowmetadata_BulkDeleteFailures](#BKMK_workflowmetadata_BulkDeleteFailures)
- [workqueue_BulkDeleteFailures](#BKMK_workqueue_BulkDeleteFailures)
- [workqueueitem_BulkDeleteFailures](#BKMK_workqueueitem_BulkDeleteFailures)

### <a name="BKMK_Account_BulkDeleteFailures"></a> Account_BulkDeleteFailures

One-To-Many Relationship: [account Account_BulkDeleteFailures](account.md#BKMK_Account_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_account`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_activityfileattachment_BulkDeleteFailures"></a> activityfileattachment_BulkDeleteFailures

One-To-Many Relationship: [activityfileattachment activityfileattachment_BulkDeleteFailures](activityfileattachment.md#BKMK_activityfileattachment_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`activityfileattachment`|
|ReferencedAttribute|`activityfileattachmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_activityfileattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ActivityMimeAttachment_BulkDeleteFailures"></a> ActivityMimeAttachment_BulkDeleteFailures

One-To-Many Relationship: [activitymimeattachment ActivityMimeAttachment_BulkDeleteFailures](activitymimeattachment.md#BKMK_ActivityMimeAttachment_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`activitymimeattachment`|
|ReferencedAttribute|`activitymimeattachmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_activitymimeattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ActivityPointer_BulkDeleteFailures"></a> ActivityPointer_BulkDeleteFailures

One-To-Many Relationship: [activitypointer ActivityPointer_BulkDeleteFailures](activitypointer.md#BKMK_ActivityPointer_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`activitypointer`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_activitypointer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_externalidentity_BulkDeleteFailures"></a> adx_externalidentity_BulkDeleteFailures

One-To-Many Relationship: [adx_externalidentity adx_externalidentity_BulkDeleteFailures](adx_externalidentity.md#BKMK_adx_externalidentity_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_externalidentity`|
|ReferencedAttribute|`adx_externalidentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_externalidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_invitation_BulkDeleteFailures"></a> adx_invitation_BulkDeleteFailures

One-To-Many Relationship: [adx_invitation adx_invitation_BulkDeleteFailures](adx_invitation.md#BKMK_adx_invitation_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_invitation`|
|ReferencedAttribute|`adx_invitationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_invitation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_inviteredemption_BulkDeleteFailures"></a> adx_inviteredemption_BulkDeleteFailures

One-To-Many Relationship: [adx_inviteredemption adx_inviteredemption_BulkDeleteFailures](adx_inviteredemption.md#BKMK_adx_inviteredemption_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_inviteredemption`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_inviteredemption`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_portalcomment_BulkDeleteFailures"></a> adx_portalcomment_BulkDeleteFailures

One-To-Many Relationship: [adx_portalcomment adx_portalcomment_BulkDeleteFailures](adx_portalcomment.md#BKMK_adx_portalcomment_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_portalcomment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_portalcomment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_setting_BulkDeleteFailures"></a> adx_setting_BulkDeleteFailures

One-To-Many Relationship: [adx_setting adx_setting_BulkDeleteFailures](adx_setting.md#BKMK_adx_setting_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_setting`|
|ReferencedAttribute|`adx_settingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_setting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_webformsession_BulkDeleteFailures"></a> adx_webformsession_BulkDeleteFailures

One-To-Many Relationship: [adx_webformsession adx_webformsession_BulkDeleteFailures](adx_webformsession.md#BKMK_adx_webformsession_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_webformsession`|
|ReferencedAttribute|`adx_webformsessionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_webformsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aicopilot_BulkDeleteFailures"></a> aicopilot_BulkDeleteFailures

One-To-Many Relationship: [aicopilot aicopilot_BulkDeleteFailures](aicopilot.md#BKMK_aicopilot_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`aicopilot`|
|ReferencedAttribute|`aicopilotid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aicopilot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugin_BulkDeleteFailures"></a> aiplugin_BulkDeleteFailures

One-To-Many Relationship: [aiplugin aiplugin_BulkDeleteFailures](aiplugin.md#BKMK_aiplugin_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugin`|
|ReferencedAttribute|`aipluginid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugin`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginauth_BulkDeleteFailures"></a> aipluginauth_BulkDeleteFailures

One-To-Many Relationship: [aipluginauth aipluginauth_BulkDeleteFailures](aipluginauth.md#BKMK_aipluginauth_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginauth`|
|ReferencedAttribute|`aipluginauthid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginauth`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginconversationstarter_BulkDeleteFailures"></a> aipluginconversationstarter_BulkDeleteFailures

One-To-Many Relationship: [aipluginconversationstarter aipluginconversationstarter_BulkDeleteFailures](aipluginconversationstarter.md#BKMK_aipluginconversationstarter_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginconversationstarter`|
|ReferencedAttribute|`aipluginconversationstarterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginconversationstarter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginconversationstartermapping_BulkDeleteFailures"></a> aipluginconversationstartermapping_BulkDeleteFailures

One-To-Many Relationship: [aipluginconversationstartermapping aipluginconversationstartermapping_BulkDeleteFailures](aipluginconversationstartermapping.md#BKMK_aipluginconversationstartermapping_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginconversationstartermapping`|
|ReferencedAttribute|`aipluginconversationstartermappingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginconversationstartermapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginexternalschema_BulkDeleteFailures"></a> aipluginexternalschema_BulkDeleteFailures

One-To-Many Relationship: [aipluginexternalschema aipluginexternalschema_BulkDeleteFailures](aipluginexternalschema.md#BKMK_aipluginexternalschema_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginexternalschema`|
|ReferencedAttribute|`aipluginexternalschemaid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginexternalschema`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginexternalschemaproperty_BulkDeleteFailures"></a> aipluginexternalschemaproperty_BulkDeleteFailures

One-To-Many Relationship: [aipluginexternalschemaproperty aipluginexternalschemaproperty_BulkDeleteFailures](aipluginexternalschemaproperty.md#BKMK_aipluginexternalschemaproperty_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginexternalschemaproperty`|
|ReferencedAttribute|`aipluginexternalschemapropertyid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginexternalschemaproperty`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugingovernance_BulkDeleteFailures"></a> aiplugingovernance_BulkDeleteFailures

One-To-Many Relationship: [aiplugingovernance aiplugingovernance_BulkDeleteFailures](aiplugingovernance.md#BKMK_aiplugingovernance_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugingovernance`|
|ReferencedAttribute|`aiplugingovernanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugingovernance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugingovernanceext_BulkDeleteFailures"></a> aiplugingovernanceext_BulkDeleteFailures

One-To-Many Relationship: [aiplugingovernanceext aiplugingovernanceext_BulkDeleteFailures](aiplugingovernanceext.md#BKMK_aiplugingovernanceext_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugingovernanceext`|
|ReferencedAttribute|`aiplugingovernanceextid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugingovernanceext`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugininstance_BulkDeleteFailures"></a> aiplugininstance_BulkDeleteFailures

One-To-Many Relationship: [aiplugininstance aiplugininstance_BulkDeleteFailures](aiplugininstance.md#BKMK_aiplugininstance_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugininstance`|
|ReferencedAttribute|`aiplugininstanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugininstance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperation_BulkDeleteFailures"></a> aipluginoperation_BulkDeleteFailures

One-To-Many Relationship: [aipluginoperation aipluginoperation_BulkDeleteFailures](aipluginoperation.md#BKMK_aipluginoperation_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperation`|
|ReferencedAttribute|`aipluginoperationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperationparameter_BulkDeleteFailures"></a> aipluginoperationparameter_BulkDeleteFailures

One-To-Many Relationship: [aipluginoperationparameter aipluginoperationparameter_BulkDeleteFailures](aipluginoperationparameter.md#BKMK_aipluginoperationparameter_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperationparameter`|
|ReferencedAttribute|`aipluginoperationparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginoperationparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperationresponsetemplate_BulkDeleteFailures"></a> aipluginoperationresponsetemplate_BulkDeleteFailures

One-To-Many Relationship: [aipluginoperationresponsetemplate aipluginoperationresponsetemplate_BulkDeleteFailures](aipluginoperationresponsetemplate.md#BKMK_aipluginoperationresponsetemplate_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperationresponsetemplate`|
|ReferencedAttribute|`aipluginoperationresponsetemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginoperationresponsetemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugintitle_BulkDeleteFailures"></a> aiplugintitle_BulkDeleteFailures

One-To-Many Relationship: [aiplugintitle aiplugintitle_BulkDeleteFailures](aiplugintitle.md#BKMK_aiplugintitle_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugintitle`|
|ReferencedAttribute|`aiplugintitleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugintitle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginusersetting_BulkDeleteFailures"></a> aipluginusersetting_BulkDeleteFailures

One-To-Many Relationship: [aipluginusersetting aipluginusersetting_BulkDeleteFailures](aipluginusersetting.md#BKMK_aipluginusersetting_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginusersetting`|
|ReferencedAttribute|`aipluginusersettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginusersetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_allowedmcpclient_BulkDeleteFailures"></a> allowedmcpclient_BulkDeleteFailures

One-To-Many Relationship: [allowedmcpclient allowedmcpclient_BulkDeleteFailures](allowedmcpclient.md#BKMK_allowedmcpclient_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`allowedmcpclient`|
|ReferencedAttribute|`allowedmcpclientid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_allowedmcpclient`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Annotation_BulkDeleteFailures"></a> Annotation_BulkDeleteFailures

One-To-Many Relationship: [annotation Annotation_BulkDeleteFailures](annotation.md#BKMK_Annotation_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`annotation`|
|ReferencedAttribute|`annotationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_annotation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_AnnualFiscalCalendar_BulkDeleteFailures"></a> AnnualFiscalCalendar_BulkDeleteFailures

One-To-Many Relationship: [annualfiscalcalendar AnnualFiscalCalendar_BulkDeleteFailures](annualfiscalcalendar.md#BKMK_AnnualFiscalCalendar_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`annualfiscalcalendar`|
|ReferencedAttribute|`userfiscalcalendarid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_annualfiscalcalendar`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appaction_BulkDeleteFailures"></a> appaction_BulkDeleteFailures

One-To-Many Relationship: [appaction appaction_BulkDeleteFailures](appaction.md#BKMK_appaction_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`appaction`|
|ReferencedAttribute|`appactionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_appaction`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appactionmigration_BulkDeleteFailures"></a> appactionmigration_BulkDeleteFailures

One-To-Many Relationship: [appactionmigration appactionmigration_BulkDeleteFailures](appactionmigration.md#BKMK_appactionmigration_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`appactionmigration`|
|ReferencedAttribute|`appactionmigrationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_appactionmigration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appactionrule_BulkDeleteFailures"></a> appactionrule_BulkDeleteFailures

One-To-Many Relationship: [appactionrule appactionrule_BulkDeleteFailures](appactionrule.md#BKMK_appactionrule_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`appactionrule`|
|ReferencedAttribute|`appactionruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_appactionrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_application_BulkDeleteFailures"></a> application_BulkDeleteFailures

One-To-Many Relationship: [application application_BulkDeleteFailures](application.md#BKMK_application_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`application`|
|ReferencedAttribute|`applicationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_application`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_applicationuser_BulkDeleteFailures"></a> applicationuser_BulkDeleteFailures

One-To-Many Relationship: [applicationuser applicationuser_BulkDeleteFailures](applicationuser.md#BKMK_applicationuser_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`applicationuser`|
|ReferencedAttribute|`applicationuserid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_applicationuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Appointment_BulkDeleteFailures"></a> Appointment_BulkDeleteFailures

One-To-Many Relationship: [appointment Appointment_BulkDeleteFailures](appointment.md#BKMK_Appointment_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`appointment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalprocess_BulkDeleteFailures"></a> approvalprocess_BulkDeleteFailures

One-To-Many Relationship: [approvalprocess approvalprocess_BulkDeleteFailures](approvalprocess.md#BKMK_approvalprocess_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalprocess`|
|ReferencedAttribute|`approvalprocessid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageapproval_BulkDeleteFailures"></a> approvalstageapproval_BulkDeleteFailures

One-To-Many Relationship: [approvalstageapproval approvalstageapproval_BulkDeleteFailures](approvalstageapproval.md#BKMK_approvalstageapproval_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageapproval`|
|ReferencedAttribute|`approvalstageapprovalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalstageapproval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstagecondition_BulkDeleteFailures"></a> approvalstagecondition_BulkDeleteFailures

One-To-Many Relationship: [approvalstagecondition approvalstagecondition_BulkDeleteFailures](approvalstagecondition.md#BKMK_approvalstagecondition_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstagecondition`|
|ReferencedAttribute|`approvalstageconditionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalstagecondition`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageintelligent_BulkDeleteFailures"></a> approvalstageintelligent_BulkDeleteFailures

One-To-Many Relationship: [approvalstageintelligent approvalstageintelligent_BulkDeleteFailures](approvalstageintelligent.md#BKMK_approvalstageintelligent_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageintelligent`|
|ReferencedAttribute|`approvalstageintelligentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalstageintelligent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageorder_BulkDeleteFailures"></a> approvalstageorder_BulkDeleteFailures

One-To-Many Relationship: [approvalstageorder approvalstageorder_BulkDeleteFailures](approvalstageorder.md#BKMK_approvalstageorder_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageorder`|
|ReferencedAttribute|`approvalstageorderid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalstageorder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_attributeclusterconfig_BulkDeleteFailures"></a> attributeclusterconfig_BulkDeleteFailures

One-To-Many Relationship: [attributeclusterconfig attributeclusterconfig_BulkDeleteFailures](attributeclusterconfig.md#BKMK_attributeclusterconfig_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`attributeclusterconfig`|
|ReferencedAttribute|`attributeclusterconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_attributeclusterconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_attributeimageconfig_BulkDeleteFailures"></a> attributeimageconfig_BulkDeleteFailures

One-To-Many Relationship: [attributeimageconfig attributeimageconfig_BulkDeleteFailures](attributeimageconfig.md#BKMK_attributeimageconfig_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`attributeimageconfig`|
|ReferencedAttribute|`attributeimageconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_attributeimageconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_attributemaskingrule_BulkDeleteFailures"></a> attributemaskingrule_BulkDeleteFailures

One-To-Many Relationship: [attributemaskingrule attributemaskingrule_BulkDeleteFailures](attributemaskingrule.md#BKMK_attributemaskingrule_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`attributemaskingrule`|
|ReferencedAttribute|`attributemaskingruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_attributemaskingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_attributepicklistvalue_BulkDeleteFailures"></a> attributepicklistvalue_BulkDeleteFailures

One-To-Many Relationship: [attributepicklistvalue attributepicklistvalue_BulkDeleteFailures](attributepicklistvalue.md#BKMK_attributepicklistvalue_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`attributepicklistvalue`|
|ReferencedAttribute|`attributepicklistvalueid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_attributepicklistvalue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_bot_BulkDeleteFailures"></a> bot_BulkDeleteFailures

One-To-Many Relationship: [bot bot_BulkDeleteFailures](bot.md#BKMK_bot_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`bot`|
|ReferencedAttribute|`botid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_bot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_botcomponent_BulkDeleteFailures"></a> botcomponent_BulkDeleteFailures

One-To-Many Relationship: [botcomponent botcomponent_BulkDeleteFailures](botcomponent.md#BKMK_botcomponent_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`botcomponent`|
|ReferencedAttribute|`botcomponentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_botcomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_botcomponentcollection_BulkDeleteFailures"></a> botcomponentcollection_BulkDeleteFailures

One-To-Many Relationship: [botcomponentcollection botcomponentcollection_BulkDeleteFailures](botcomponentcollection.md#BKMK_botcomponentcollection_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`botcomponentcollection`|
|ReferencedAttribute|`botcomponentcollectionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_botcomponentcollection`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_BulkDeleteOperation_BulkDeleteFailure"></a> BulkDeleteOperation_BulkDeleteFailure

One-To-Many Relationship: [bulkdeleteoperation BulkDeleteOperation_BulkDeleteFailure](bulkdeleteoperation.md#BKMK_BulkDeleteOperation_BulkDeleteFailure)

|Property|Value|
|---|---|
|ReferencedEntity|`bulkdeleteoperation`|
|ReferencedAttribute|`bulkdeleteoperationid`|
|ReferencingAttribute|`bulkdeleteoperationid`|
|ReferencingEntityNavigationPropertyName|`bulkdeleteoperationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_businessprocess_BulkDeleteFailures"></a> businessprocess_BulkDeleteFailures

One-To-Many Relationship: [businessprocess businessprocess_BulkDeleteFailures](businessprocess.md#BKMK_businessprocess_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`businessprocess`|
|ReferencedAttribute|`businessprocessid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_businessprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_BusinessUnit_BulkDeleteFailures"></a> BusinessUnit_BulkDeleteFailures

One-To-Many Relationship: [businessunit BusinessUnit_BulkDeleteFailures](businessunit.md#BKMK_BusinessUnit_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_businessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_BusinessUnitNewsArticle_BulkDeleteFailures"></a> BusinessUnitNewsArticle_BulkDeleteFailures

One-To-Many Relationship: [businessunitnewsarticle BusinessUnitNewsArticle_BulkDeleteFailures](businessunitnewsarticle.md#BKMK_BusinessUnitNewsArticle_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunitnewsarticle`|
|ReferencedAttribute|`businessunitnewsarticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_businessunitnewsarticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Calendar_BulkDeleteFailures"></a> Calendar_BulkDeleteFailures

One-To-Many Relationship: [calendar Calendar_BulkDeleteFailures](calendar.md#BKMK_Calendar_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`calendar`|
|ReferencedAttribute|`calendarid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_calendar`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_card_BulkDeleteFailures"></a> card_BulkDeleteFailures

One-To-Many Relationship: [card card_BulkDeleteFailures](card.md#BKMK_card_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`card`|
|ReferencedAttribute|`cardid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_card`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_catalog_BulkDeleteFailures"></a> catalog_BulkDeleteFailures

One-To-Many Relationship: [catalog catalog_BulkDeleteFailures](catalog.md#BKMK_catalog_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`catalog`|
|ReferencedAttribute|`catalogid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_catalog`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_catalogassignment_BulkDeleteFailures"></a> catalogassignment_BulkDeleteFailures

One-To-Many Relationship: [catalogassignment catalogassignment_BulkDeleteFailures](catalogassignment.md#BKMK_catalogassignment_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`catalogassignment`|
|ReferencedAttribute|`catalogassignmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_catalogassignment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_certificatecredential_BulkDeleteFailures"></a> certificatecredential_BulkDeleteFailures

One-To-Many Relationship: [certificatecredential certificatecredential_BulkDeleteFailures](certificatecredential.md#BKMK_certificatecredential_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`certificatecredential`|
|ReferencedAttribute|`certificatecredentialid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_certificatecredential`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_chat_BulkDeleteFailures"></a> chat_BulkDeleteFailures

One-To-Many Relationship: [chat chat_BulkDeleteFailures](chat.md#BKMK_chat_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`chat`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_chat`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connectioninstance_BulkDeleteFailures"></a> connectioninstance_BulkDeleteFailures

One-To-Many Relationship: [connectioninstance connectioninstance_BulkDeleteFailures](connectioninstance.md#BKMK_connectioninstance_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`connectioninstance`|
|ReferencedAttribute|`connectioninstanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_connectioninstance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connectionreference_BulkDeleteFailures"></a> connectionreference_BulkDeleteFailures

One-To-Many Relationship: [connectionreference connectionreference_BulkDeleteFailures](connectionreference.md#BKMK_connectionreference_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`connectionreference`|
|ReferencedAttribute|`connectionreferenceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_connectionreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connector_BulkDeleteFailures"></a> connector_BulkDeleteFailures

One-To-Many Relationship: [connector connector_BulkDeleteFailures](connector.md#BKMK_connector_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`connector`|
|ReferencedAttribute|`connectorid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_connector`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Contact_BulkDeleteFailures"></a> Contact_BulkDeleteFailures

One-To-Many Relationship: [contact Contact_BulkDeleteFailures](contact.md#BKMK_Contact_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_contact`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_conversationtranscript_BulkDeleteFailures"></a> conversationtranscript_BulkDeleteFailures

One-To-Many Relationship: [conversationtranscript conversationtranscript_BulkDeleteFailures](conversationtranscript.md#BKMK_conversationtranscript_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`conversationtranscript`|
|ReferencedAttribute|`conversationtranscriptid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_conversationtranscript`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_copilotexamplequestion_BulkDeleteFailures"></a> copilotexamplequestion_BulkDeleteFailures

One-To-Many Relationship: [copilotexamplequestion copilotexamplequestion_BulkDeleteFailures](copilotexamplequestion.md#BKMK_copilotexamplequestion_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`copilotexamplequestion`|
|ReferencedAttribute|`copilotexamplequestionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_copilotexamplequestion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_copilotglossaryterm_BulkDeleteFailures"></a> copilotglossaryterm_BulkDeleteFailures

One-To-Many Relationship: [copilotglossaryterm copilotglossaryterm_BulkDeleteFailures](copilotglossaryterm.md#BKMK_copilotglossaryterm_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`copilotglossaryterm`|
|ReferencedAttribute|`copilotglossarytermid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_copilotglossaryterm`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_copilotsynonyms_BulkDeleteFailures"></a> copilotsynonyms_BulkDeleteFailures

One-To-Many Relationship: [copilotsynonyms copilotsynonyms_BulkDeleteFailures](copilotsynonyms.md#BKMK_copilotsynonyms_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`copilotsynonyms`|
|ReferencedAttribute|`copilotsynonymsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_copilotsynonyms`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_credential_BulkDeleteFailures"></a> credential_BulkDeleteFailures

One-To-Many Relationship: [credential credential_BulkDeleteFailures](credential.md#BKMK_credential_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`credential`|
|ReferencedAttribute|`credentialid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_credential`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_customapi_BulkDeleteFailures"></a> customapi_BulkDeleteFailures

One-To-Many Relationship: [customapi customapi_BulkDeleteFailures](customapi.md#BKMK_customapi_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`customapi`|
|ReferencedAttribute|`customapiid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_customapi`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_customapirequestparameter_BulkDeleteFailures"></a> customapirequestparameter_BulkDeleteFailures

One-To-Many Relationship: [customapirequestparameter customapirequestparameter_BulkDeleteFailures](customapirequestparameter.md#BKMK_customapirequestparameter_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`customapirequestparameter`|
|ReferencedAttribute|`customapirequestparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_customapirequestparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_customapiresponseproperty_BulkDeleteFailures"></a> customapiresponseproperty_BulkDeleteFailures

One-To-Many Relationship: [customapiresponseproperty customapiresponseproperty_BulkDeleteFailures](customapiresponseproperty.md#BKMK_customapiresponseproperty_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`customapiresponseproperty`|
|ReferencedAttribute|`customapiresponsepropertyid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_customapiresponseproperty`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_CustomerAddress_BulkDeleteFailures"></a> CustomerAddress_BulkDeleteFailures

One-To-Many Relationship: [customeraddress CustomerAddress_BulkDeleteFailures](customeraddress.md#BKMK_CustomerAddress_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`customeraddress`|
|ReferencedAttribute|`customeraddressid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_customeraddress`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakefolder_BulkDeleteFailures"></a> datalakefolder_BulkDeleteFailures

One-To-Many Relationship: [datalakefolder datalakefolder_BulkDeleteFailures](datalakefolder.md#BKMK_datalakefolder_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakefolder`|
|ReferencedAttribute|`datalakefolderid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_datalakefolder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakefolderpermission_BulkDeleteFailures"></a> datalakefolderpermission_BulkDeleteFailures

One-To-Many Relationship: [datalakefolderpermission datalakefolderpermission_BulkDeleteFailures](datalakefolderpermission.md#BKMK_datalakefolderpermission_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakefolderpermission`|
|ReferencedAttribute|`datalakefolderpermissionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_datalakefolderpermission`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakeworkspace_BulkDeleteFailures"></a> datalakeworkspace_BulkDeleteFailures

One-To-Many Relationship: [datalakeworkspace datalakeworkspace_BulkDeleteFailures](datalakeworkspace.md#BKMK_datalakeworkspace_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakeworkspace`|
|ReferencedAttribute|`datalakeworkspaceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_datalakeworkspace`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakeworkspacepermission_BulkDeleteFailures"></a> datalakeworkspacepermission_BulkDeleteFailures

One-To-Many Relationship: [datalakeworkspacepermission datalakeworkspacepermission_BulkDeleteFailures](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakeworkspacepermission`|
|ReferencedAttribute|`datalakeworkspacepermissionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_datalakeworkspacepermission`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dataprocessingconfiguration_BulkDeleteFailures"></a> dataprocessingconfiguration_BulkDeleteFailures

One-To-Many Relationship: [dataprocessingconfiguration dataprocessingconfiguration_BulkDeleteFailures](dataprocessingconfiguration.md#BKMK_dataprocessingconfiguration_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`dataprocessingconfiguration`|
|ReferencedAttribute|`dataprocessingconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dataprocessingconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_delegatedauthorization_BulkDeleteFailures"></a> delegatedauthorization_BulkDeleteFailures

One-To-Many Relationship: [delegatedauthorization delegatedauthorization_BulkDeleteFailures](delegatedauthorization.md#BKMK_delegatedauthorization_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`delegatedauthorization`|
|ReferencedAttribute|`delegatedauthorizationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_delegatedauthorization`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_desktopflowbinary_BulkDeleteFailures"></a> desktopflowbinary_BulkDeleteFailures

One-To-Many Relationship: [desktopflowbinary desktopflowbinary_BulkDeleteFailures](desktopflowbinary.md#BKMK_desktopflowbinary_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`desktopflowbinary`|
|ReferencedAttribute|`desktopflowbinaryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_desktopflowbinary`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_desktopflowmodule_BulkDeleteFailures"></a> desktopflowmodule_BulkDeleteFailures

One-To-Many Relationship: [desktopflowmodule desktopflowmodule_BulkDeleteFailures](desktopflowmodule.md#BKMK_desktopflowmodule_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`desktopflowmodule`|
|ReferencedAttribute|`desktopflowmoduleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_desktopflowmodule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_DisplayString_BulkDeleteFailures"></a> DisplayString_BulkDeleteFailures

One-To-Many Relationship: [displaystring DisplayString_BulkDeleteFailures](displaystring.md#BKMK_DisplayString_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`displaystring`|
|ReferencedAttribute|`displaystringid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_displaystring`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvfilesearch_BulkDeleteFailures"></a> dvfilesearch_BulkDeleteFailures

One-To-Many Relationship: [dvfilesearch dvfilesearch_BulkDeleteFailures](dvfilesearch.md#BKMK_dvfilesearch_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`dvfilesearch`|
|ReferencedAttribute|`dvfilesearchid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvfilesearch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvfilesearchattribute_BulkDeleteFailures"></a> dvfilesearchattribute_BulkDeleteFailures

One-To-Many Relationship: [dvfilesearchattribute dvfilesearchattribute_BulkDeleteFailures](dvfilesearchattribute.md#BKMK_dvfilesearchattribute_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`dvfilesearchattribute`|
|ReferencedAttribute|`dvfilesearchattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvfilesearchattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvfilesearchentity_BulkDeleteFailures"></a> dvfilesearchentity_BulkDeleteFailures

One-To-Many Relationship: [dvfilesearchentity dvfilesearchentity_BulkDeleteFailures](dvfilesearchentity.md#BKMK_dvfilesearchentity_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`dvfilesearchentity`|
|ReferencedAttribute|`dvfilesearchentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvfilesearchentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvtablesearch_BulkDeleteFailures"></a> dvtablesearch_BulkDeleteFailures

One-To-Many Relationship: [dvtablesearch dvtablesearch_BulkDeleteFailures](dvtablesearch.md#BKMK_dvtablesearch_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`dvtablesearch`|
|ReferencedAttribute|`dvtablesearchid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvtablesearch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvtablesearchattribute_BulkDeleteFailures"></a> dvtablesearchattribute_BulkDeleteFailures

One-To-Many Relationship: [dvtablesearchattribute dvtablesearchattribute_BulkDeleteFailures](dvtablesearchattribute.md#BKMK_dvtablesearchattribute_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`dvtablesearchattribute`|
|ReferencedAttribute|`dvtablesearchattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvtablesearchattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvtablesearchentity_BulkDeleteFailures"></a> dvtablesearchentity_BulkDeleteFailures

One-To-Many Relationship: [dvtablesearchentity dvtablesearchentity_BulkDeleteFailures](dvtablesearchentity.md#BKMK_dvtablesearchentity_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`dvtablesearchentity`|
|ReferencedAttribute|`dvtablesearchentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvtablesearchentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Email_BulkDeleteFailures"></a> Email_BulkDeleteFailures

One-To-Many Relationship: [email Email_BulkDeleteFailures](email.md#BKMK_Email_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`email`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_emailaddressconfiguration_BulkDeleteFailures"></a> emailaddressconfiguration_BulkDeleteFailures

One-To-Many Relationship: [emailaddressconfiguration emailaddressconfiguration_BulkDeleteFailures](emailaddressconfiguration.md#BKMK_emailaddressconfiguration_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`emailaddressconfiguration`|
|ReferencedAttribute|`emailaddressconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_emailaddressconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_emailserverprofile_bulkdeletefailures"></a> emailserverprofile_bulkdeletefailures

One-To-Many Relationship: [emailserverprofile emailserverprofile_bulkdeletefailures](emailserverprofile.md#BKMK_emailserverprofile_bulkdeletefailures)

|Property|Value|
|---|---|
|ReferencedEntity|`emailserverprofile`|
|ReferencedAttribute|`emailserverprofileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_emailserverprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityanalyticsconfig_BulkDeleteFailures"></a> entityanalyticsconfig_BulkDeleteFailures

One-To-Many Relationship: [entityanalyticsconfig entityanalyticsconfig_BulkDeleteFailures](entityanalyticsconfig.md#BKMK_entityanalyticsconfig_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`entityanalyticsconfig`|
|ReferencedAttribute|`entityanalyticsconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityanalyticsconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityclusterconfig_BulkDeleteFailures"></a> entityclusterconfig_BulkDeleteFailures

One-To-Many Relationship: [entityclusterconfig entityclusterconfig_BulkDeleteFailures](entityclusterconfig.md#BKMK_entityclusterconfig_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`entityclusterconfig`|
|ReferencedAttribute|`entityclusterconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityclusterconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityimageconfig_BulkDeleteFailures"></a> entityimageconfig_BulkDeleteFailures

One-To-Many Relationship: [entityimageconfig entityimageconfig_BulkDeleteFailures](entityimageconfig.md#BKMK_entityimageconfig_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`entityimageconfig`|
|ReferencedAttribute|`entityimageconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityimageconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityindex_BulkDeleteFailures"></a> entityindex_BulkDeleteFailures

One-To-Many Relationship: [entityindex entityindex_BulkDeleteFailures](entityindex.md#BKMK_entityindex_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`entityindex`|
|ReferencedAttribute|`indexid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityindex`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityrecordfilter_BulkDeleteFailures"></a> entityrecordfilter_BulkDeleteFailures

One-To-Many Relationship: [entityrecordfilter entityrecordfilter_BulkDeleteFailures](entityrecordfilter.md#BKMK_entityrecordfilter_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`entityrecordfilter`|
|ReferencedAttribute|`entityrecordfilterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityrecordfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariabledefinition_BulkDeleteFailures"></a> environmentvariabledefinition_BulkDeleteFailures

One-To-Many Relationship: [environmentvariabledefinition environmentvariabledefinition_BulkDeleteFailures](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariabledefinition`|
|ReferencedAttribute|`environmentvariabledefinitionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_environmentvariabledefinition`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariablevalue_BulkDeleteFailures"></a> environmentvariablevalue_BulkDeleteFailures

One-To-Many Relationship: [environmentvariablevalue environmentvariablevalue_BulkDeleteFailures](environmentvariablevalue.md#BKMK_environmentvariablevalue_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariablevalue`|
|ReferencedAttribute|`environmentvariablevalueid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_environmentvariablevalue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_exportedexcel_BulkDeleteFailures"></a> exportedexcel_BulkDeleteFailures

One-To-Many Relationship: [exportedexcel exportedexcel_BulkDeleteFailures](exportedexcel.md#BKMK_exportedexcel_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`exportedexcel`|
|ReferencedAttribute|`exportedexcelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_exportedexcel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_exportsolutionupload_BulkDeleteFailures"></a> exportsolutionupload_BulkDeleteFailures

One-To-Many Relationship: [exportsolutionupload exportsolutionupload_BulkDeleteFailures](exportsolutionupload.md#BKMK_exportsolutionupload_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`exportsolutionupload`|
|ReferencedAttribute|`exportsolutionuploadid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_exportsolutionupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fabricaiskill_BulkDeleteFailures"></a> fabricaiskill_BulkDeleteFailures

One-To-Many Relationship: [fabricaiskill fabricaiskill_BulkDeleteFailures](fabricaiskill.md#BKMK_fabricaiskill_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`fabricaiskill`|
|ReferencedAttribute|`fabricaiskillid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_fabricaiskill`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Fax_BulkDeleteFailures"></a> Fax_BulkDeleteFailures

One-To-Many Relationship: [fax Fax_BulkDeleteFailures](fax.md#BKMK_Fax_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`fax`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_fax`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_featurecontrolsetting_BulkDeleteFailures"></a> featurecontrolsetting_BulkDeleteFailures

One-To-Many Relationship: [featurecontrolsetting featurecontrolsetting_BulkDeleteFailures](featurecontrolsetting.md#BKMK_featurecontrolsetting_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`featurecontrolsetting`|
|ReferencedAttribute|`featurecontrolsettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_featurecontrolsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_federatedknowledgeconfiguration_BulkDeleteFailures"></a> federatedknowledgeconfiguration_BulkDeleteFailures

One-To-Many Relationship: [federatedknowledgeconfiguration federatedknowledgeconfiguration_BulkDeleteFailures](federatedknowledgeconfiguration.md#BKMK_federatedknowledgeconfiguration_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`federatedknowledgeconfiguration`|
|ReferencedAttribute|`federatedknowledgeconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_federatedknowledgeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_federatedknowledgeentityconfiguration_BulkDeleteFailures"></a> federatedknowledgeentityconfiguration_BulkDeleteFailures

One-To-Many Relationship: [federatedknowledgeentityconfiguration federatedknowledgeentityconfiguration_BulkDeleteFailures](federatedknowledgeentityconfiguration.md#BKMK_federatedknowledgeentityconfiguration_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`federatedknowledgeentityconfiguration`|
|ReferencedAttribute|`federatedknowledgeentityconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_federatedknowledgeentityconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FixedMonthlyFiscalCalendar_BulkDeleteFailures"></a> FixedMonthlyFiscalCalendar_BulkDeleteFailures

One-To-Many Relationship: [fixedmonthlyfiscalcalendar FixedMonthlyFiscalCalendar_BulkDeleteFailures](fixedmonthlyfiscalcalendar.md#BKMK_FixedMonthlyFiscalCalendar_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`fixedmonthlyfiscalcalendar`|
|ReferencedAttribute|`userfiscalcalendarid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_fixedmonthlyfiscalcalendar`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowcapacityassignment_BulkDeleteFailures"></a> flowcapacityassignment_BulkDeleteFailures

One-To-Many Relationship: [flowcapacityassignment flowcapacityassignment_BulkDeleteFailures](flowcapacityassignment.md#BKMK_flowcapacityassignment_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`flowcapacityassignment`|
|ReferencedAttribute|`flowcapacityassignmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowcapacityassignment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowcredentialapplication_BulkDeleteFailures"></a> flowcredentialapplication_BulkDeleteFailures

One-To-Many Relationship: [flowcredentialapplication flowcredentialapplication_BulkDeleteFailures](flowcredentialapplication.md#BKMK_flowcredentialapplication_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`flowcredentialapplication`|
|ReferencedAttribute|`flowcredentialapplicationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowcredentialapplication`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowevent_BulkDeleteFailures"></a> flowevent_BulkDeleteFailures

One-To-Many Relationship: [flowevent flowevent_BulkDeleteFailures](flowevent.md#BKMK_flowevent_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`flowevent`|
|ReferencedAttribute|`floweventid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowevent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachine_BulkDeleteFailures"></a> flowmachine_BulkDeleteFailures

One-To-Many Relationship: [flowmachine flowmachine_BulkDeleteFailures](flowmachine.md#BKMK_flowmachine_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachine`|
|ReferencedAttribute|`flowmachineid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachine`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinegroup_BulkDeleteFailures"></a> flowmachinegroup_BulkDeleteFailures

One-To-Many Relationship: [flowmachinegroup flowmachinegroup_BulkDeleteFailures](flowmachinegroup.md#BKMK_flowmachinegroup_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinegroup`|
|ReferencedAttribute|`flowmachinegroupid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachinegroup`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachineimage_BulkDeleteFailures"></a> flowmachineimage_BulkDeleteFailures

One-To-Many Relationship: [flowmachineimage flowmachineimage_BulkDeleteFailures](flowmachineimage.md#BKMK_flowmachineimage_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachineimage`|
|ReferencedAttribute|`flowmachineimageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachineimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachineimageversion_BulkDeleteFailures"></a> flowmachineimageversion_BulkDeleteFailures

One-To-Many Relationship: [flowmachineimageversion flowmachineimageversion_BulkDeleteFailures](flowmachineimageversion.md#BKMK_flowmachineimageversion_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachineimageversion`|
|ReferencedAttribute|`flowmachineimageversionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachineimageversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinenetwork_BulkDeleteFailures"></a> flowmachinenetwork_BulkDeleteFailures

One-To-Many Relationship: [flowmachinenetwork flowmachinenetwork_BulkDeleteFailures](flowmachinenetwork.md#BKMK_flowmachinenetwork_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinenetwork`|
|ReferencedAttribute|`flowmachinenetworkid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachinenetwork`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowsession_BulkDeleteFailures"></a> flowsession_BulkDeleteFailures

One-To-Many Relationship: [flowsession flowsession_BulkDeleteFailures](flowsession.md#BKMK_flowsession_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`flowsession`|
|ReferencedAttribute|`flowsessionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowsessionbinary_BulkDeleteFailures"></a> flowsessionbinary_BulkDeleteFailures

One-To-Many Relationship: [flowsessionbinary flowsessionbinary_BulkDeleteFailures](flowsessionbinary.md#BKMK_flowsessionbinary_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`flowsessionbinary`|
|ReferencedAttribute|`flowsessionbinaryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowsessionbinary`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fxexpression_BulkDeleteFailures"></a> fxexpression_BulkDeleteFailures

One-To-Many Relationship: [fxexpression fxexpression_BulkDeleteFailures](fxexpression.md#BKMK_fxexpression_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`fxexpression`|
|ReferencedAttribute|`fxexpressionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_fxexpression`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_governanceconfiguration_BulkDeleteFailures"></a> governanceconfiguration_BulkDeleteFailures

One-To-Many Relationship: [governanceconfiguration governanceconfiguration_BulkDeleteFailures](governanceconfiguration.md#BKMK_governanceconfiguration_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`governanceconfiguration`|
|ReferencedAttribute|`governanceconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_governanceconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Import_BulkDeleteFailures"></a> Import_BulkDeleteFailures

One-To-Many Relationship: [import Import_BulkDeleteFailures](import.md#BKMK_Import_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`import`|
|ReferencedAttribute|`importid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_import`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ImportData_BulkDeleteFailures"></a> ImportData_BulkDeleteFailures

One-To-Many Relationship: [importdata ImportData_BulkDeleteFailures](importdata.md#BKMK_ImportData_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`importdata`|
|ReferencedAttribute|`importdataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_importdata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ImportFile_BulkDeleteFailures"></a> ImportFile_BulkDeleteFailures

One-To-Many Relationship: [importfile ImportFile_BulkDeleteFailures](importfile.md#BKMK_ImportFile_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`importfile`|
|ReferencedAttribute|`importfileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_importfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ImportLog_BulkDeleteFailures"></a> ImportLog_BulkDeleteFailures

One-To-Many Relationship: [importlog ImportLog_BulkDeleteFailures](importlog.md#BKMK_ImportLog_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`importlog`|
|ReferencedAttribute|`importlogid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_importlog`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ImportMap_BulkDeleteFailures"></a> ImportMap_BulkDeleteFailures

One-To-Many Relationship: [importmap ImportMap_BulkDeleteFailures](importmap.md#BKMK_ImportMap_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`importmap`|
|ReferencedAttribute|`importmapid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_importmap`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_indexattributes_BulkDeleteFailures"></a> indexattributes_BulkDeleteFailures

One-To-Many Relationship: [indexattributes indexattributes_BulkDeleteFailures](indexattributes.md#BKMK_indexattributes_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`indexattributes`|
|ReferencedAttribute|`indexattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_indexattributes`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KbArticle_BulkDeleteFailures"></a> KbArticle_BulkDeleteFailures

One-To-Many Relationship: [kbarticle KbArticle_BulkDeleteFailures](kbarticle.md#BKMK_KbArticle_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`kbarticle`|
|ReferencedAttribute|`kbarticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_kbarticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KbArticleComment_BulkDeleteFailures"></a> KbArticleComment_BulkDeleteFailures

One-To-Many Relationship: [kbarticlecomment KbArticleComment_BulkDeleteFailures](kbarticlecomment.md#BKMK_KbArticleComment_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`kbarticlecomment`|
|ReferencedAttribute|`kbarticlecommentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_kbarticlecomment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KbArticleTemplate_BulkDeleteFailures"></a> KbArticleTemplate_BulkDeleteFailures

One-To-Many Relationship: [kbarticletemplate KbArticleTemplate_BulkDeleteFailures](kbarticletemplate.md#BKMK_KbArticleTemplate_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`kbarticletemplate`|
|ReferencedAttribute|`kbarticletemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_kbarticletemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_keyvaultreference_BulkDeleteFailures"></a> keyvaultreference_BulkDeleteFailures

One-To-Many Relationship: [keyvaultreference keyvaultreference_BulkDeleteFailures](keyvaultreference.md#BKMK_keyvaultreference_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`keyvaultreference`|
|ReferencedAttribute|`keyvaultreferenceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_keyvaultreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgearticle_BulkDeleteFailures"></a> knowledgearticle_BulkDeleteFailures

One-To-Many Relationship: [knowledgearticle knowledgearticle_BulkDeleteFailures](knowledgearticle.md#BKMK_knowledgearticle_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KnowledgeBaseRecord_BulkDeleteFailures"></a> KnowledgeBaseRecord_BulkDeleteFailures

One-To-Many Relationship: [knowledgebaserecord KnowledgeBaseRecord_BulkDeleteFailures](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgebaserecord`|
|ReferencedAttribute|`knowledgebaserecordid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgebaserecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgefaq_BulkDeleteFailures"></a> knowledgefaq_BulkDeleteFailures

One-To-Many Relationship: [knowledgefaq knowledgefaq_BulkDeleteFailures](knowledgefaq.md#BKMK_knowledgefaq_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgefaq`|
|ReferencedAttribute|`knowledgefaqid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgefaq`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Letter_BulkDeleteFailures"></a> Letter_BulkDeleteFailures

One-To-Many Relationship: [letter Letter_BulkDeleteFailures](letter.md#BKMK_Letter_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`letter`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_letter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mainfewshot_BulkDeleteFailures"></a> mainfewshot_BulkDeleteFailures

One-To-Many Relationship: [mainfewshot mainfewshot_BulkDeleteFailures](mainfewshot.md#BKMK_mainfewshot_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`mainfewshot`|
|ReferencedAttribute|`mainfewshotid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mainfewshot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_makerfewshot_BulkDeleteFailures"></a> makerfewshot_BulkDeleteFailures

One-To-Many Relationship: [makerfewshot makerfewshot_BulkDeleteFailures](makerfewshot.md#BKMK_makerfewshot_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`makerfewshot`|
|ReferencedAttribute|`makerfewshotid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_makerfewshot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_managedidentity_BulkDeleteFailures"></a> managedidentity_BulkDeleteFailures

One-To-Many Relationship: [managedidentity managedidentity_BulkDeleteFailures](managedidentity.md#BKMK_managedidentity_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`managedidentity`|
|ReferencedAttribute|`managedidentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_managedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_maskingrule_BulkDeleteFailures"></a> maskingrule_BulkDeleteFailures

One-To-Many Relationship: [maskingrule maskingrule_BulkDeleteFailures](maskingrule.md#BKMK_maskingrule_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`maskingrule`|
|ReferencedAttribute|`maskingruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_maskingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mcpserver_BulkDeleteFailures"></a> mcpserver_BulkDeleteFailures

One-To-Many Relationship: [mcpserver mcpserver_BulkDeleteFailures](mcpserver.md#BKMK_mcpserver_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`mcpserver`|
|ReferencedAttribute|`mcpserverid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mcpserver`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mcptool_BulkDeleteFailures"></a> mcptool_BulkDeleteFailures

One-To-Many Relationship: [mcptool mcptool_BulkDeleteFailures](mcptool.md#BKMK_mcptool_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`mcptool`|
|ReferencedAttribute|`mcptoolid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mcptool`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_metadataforarchival_BulkDeleteFailures"></a> metadataforarchival_BulkDeleteFailures

One-To-Many Relationship: [metadataforarchival metadataforarchival_BulkDeleteFailures](metadataforarchival.md#BKMK_metadataforarchival_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`metadataforarchival`|
|ReferencedAttribute|`metadataforarchivalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_metadataforarchival`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mobileofflineprofileextension_BulkDeleteFailures"></a> mobileofflineprofileextension_BulkDeleteFailures

One-To-Many Relationship: [mobileofflineprofileextension mobileofflineprofileextension_BulkDeleteFailures](mobileofflineprofileextension.md#BKMK_mobileofflineprofileextension_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`mobileofflineprofileextension`|
|ReferencedAttribute|`mobileofflineprofileextensionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mobileofflineprofileextension`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_MonthlyFiscalCalendar_BulkDeleteFailures"></a> MonthlyFiscalCalendar_BulkDeleteFailures

One-To-Many Relationship: [monthlyfiscalcalendar MonthlyFiscalCalendar_BulkDeleteFailures](monthlyfiscalcalendar.md#BKMK_MonthlyFiscalCalendar_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`monthlyfiscalcalendar`|
|ReferencedAttribute|`userfiscalcalendarid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_monthlyfiscalcalendar`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdataset_BulkDeleteFailures"></a> msdyn_aibdataset_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aibdataset msdyn_aibdataset_BulkDeleteFailures](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdataset`|
|ReferencedAttribute|`msdyn_aibdatasetid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibdataset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetfile_BulkDeleteFailures"></a> msdyn_aibdatasetfile_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aibdatasetfile msdyn_aibdatasetfile_BulkDeleteFailures](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetfile`|
|ReferencedAttribute|`msdyn_aibdatasetfileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibdatasetfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetrecord_BulkDeleteFailures"></a> msdyn_aibdatasetrecord_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aibdatasetrecord msdyn_aibdatasetrecord_BulkDeleteFailures](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetrecord`|
|ReferencedAttribute|`msdyn_aibdatasetrecordid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibdatasetrecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetscontainer_BulkDeleteFailures"></a> msdyn_aibdatasetscontainer_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aibdatasetscontainer msdyn_aibdatasetscontainer_BulkDeleteFailures](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetscontainer`|
|ReferencedAttribute|`msdyn_aibdatasetscontainerid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibdatasetscontainer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfeedbackloop_BulkDeleteFailures"></a> msdyn_aibfeedbackloop_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aibfeedbackloop msdyn_aibfeedbackloop_BulkDeleteFailures](msdyn_aibfeedbackloop.md#BKMK_msdyn_aibfeedbackloop_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfeedbackloop`|
|ReferencedAttribute|`msdyn_aibfeedbackloopid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibfeedbackloop`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfile_BulkDeleteFailures"></a> msdyn_aibfile_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aibfile msdyn_aibfile_BulkDeleteFailures](msdyn_aibfile.md#BKMK_msdyn_aibfile_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfile`|
|ReferencedAttribute|`msdyn_aibfileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfileattacheddata_BulkDeleteFailures"></a> msdyn_aibfileattacheddata_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aibfileattacheddata msdyn_aibfileattacheddata_BulkDeleteFailures](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfileattacheddata`|
|ReferencedAttribute|`msdyn_aibfileattacheddataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibfileattacheddata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiconfiguration_BulkDeleteFailures"></a> msdyn_aiconfiguration_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aiconfiguration msdyn_aiconfiguration_BulkDeleteFailures](msdyn_aiconfiguration.md#BKMK_msdyn_aiconfiguration_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiconfiguration`|
|ReferencedAttribute|`msdyn_aiconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aidataprocessingevent_BulkDeleteFailures"></a> msdyn_aidataprocessingevent_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aidataprocessingevent msdyn_aidataprocessingevent_BulkDeleteFailures](msdyn_aidataprocessingevent.md#BKMK_msdyn_aidataprocessingevent_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aidataprocessingevent`|
|ReferencedAttribute|`msdyn_aidataprocessingeventid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aidataprocessingevent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aidocumenttemplate_BulkDeleteFailures"></a> msdyn_aidocumenttemplate_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aidocumenttemplate msdyn_aidocumenttemplate_BulkDeleteFailures](msdyn_aidocumenttemplate.md#BKMK_msdyn_aidocumenttemplate_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aidocumenttemplate`|
|ReferencedAttribute|`msdyn_aidocumenttemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aidocumenttemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievaluationconfiguration_BulkDeleteFailures"></a> msdyn_aievaluationconfiguration_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aievaluationconfiguration msdyn_aievaluationconfiguration_BulkDeleteFailures](msdyn_aievaluationconfiguration.md#BKMK_msdyn_aievaluationconfiguration_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievaluationconfiguration`|
|ReferencedAttribute|`msdyn_aievaluationconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aievaluationconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievaluationrun_BulkDeleteFailures"></a> msdyn_aievaluationrun_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aievaluationrun msdyn_aievaluationrun_BulkDeleteFailures](msdyn_aievaluationrun.md#BKMK_msdyn_aievaluationrun_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievaluationrun`|
|ReferencedAttribute|`msdyn_aievaluationrunid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aievaluationrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievent_BulkDeleteFailures"></a> msdyn_aievent_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aievent msdyn_aievent_BulkDeleteFailures](msdyn_aievent.md#BKMK_msdyn_aievent_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievent`|
|ReferencedAttribute|`msdyn_aieventid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aievent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aifptrainingdocument_BulkDeleteFailures"></a> msdyn_aifptrainingdocument_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aifptrainingdocument msdyn_aifptrainingdocument_BulkDeleteFailures](msdyn_aifptrainingdocument.md#BKMK_msdyn_aifptrainingdocument_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aifptrainingdocument`|
|ReferencedAttribute|`msdyn_aifptrainingdocumentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aifptrainingdocument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aimodel_BulkDeleteFailures"></a> msdyn_aimodel_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aimodel msdyn_aimodel_BulkDeleteFailures](msdyn_aimodel.md#BKMK_msdyn_aimodel_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aimodel`|
|ReferencedAttribute|`msdyn_aimodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aimodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodimage_BulkDeleteFailures"></a> msdyn_aiodimage_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aiodimage msdyn_aiodimage_BulkDeleteFailures](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodimage`|
|ReferencedAttribute|`msdyn_aiodimageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiodimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodlabel_BulkDeleteFailures"></a> msdyn_aiodlabel_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aiodlabel msdyn_aiodlabel_BulkDeleteFailures](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodlabel`|
|ReferencedAttribute|`msdyn_aiodlabelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiodlabel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodtrainingboundingbox_BulkDeleteFailures"></a> msdyn_aiodtrainingboundingbox_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aiodtrainingboundingbox msdyn_aiodtrainingboundingbox_BulkDeleteFailures](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodtrainingboundingbox`|
|ReferencedAttribute|`msdyn_aiodtrainingboundingboxid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiodtrainingboundingbox`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodtrainingimage_BulkDeleteFailures"></a> msdyn_aiodtrainingimage_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aiodtrainingimage msdyn_aiodtrainingimage_BulkDeleteFailures](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodtrainingimage`|
|ReferencedAttribute|`msdyn_aiodtrainingimageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiodtrainingimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitemplate_BulkDeleteFailures"></a> msdyn_aitemplate_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aitemplate msdyn_aitemplate_BulkDeleteFailures](msdyn_aitemplate.md#BKMK_msdyn_aitemplate_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitemplate`|
|ReferencedAttribute|`msdyn_aitemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestcase_BulkDeleteFailures"></a> msdyn_aitestcase_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aitestcase msdyn_aitestcase_BulkDeleteFailures](msdyn_aitestcase.md#BKMK_msdyn_aitestcase_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestcase`|
|ReferencedAttribute|`msdyn_aitestcaseid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestcase`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestcasedocument_BulkDeleteFailures"></a> msdyn_aitestcasedocument_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aitestcasedocument msdyn_aitestcasedocument_BulkDeleteFailures](msdyn_aitestcasedocument.md#BKMK_msdyn_aitestcasedocument_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestcasedocument`|
|ReferencedAttribute|`msdyn_aitestcasedocumentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestcasedocument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestcaseinput_BulkDeleteFailures"></a> msdyn_aitestcaseinput_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aitestcaseinput msdyn_aitestcaseinput_BulkDeleteFailures](msdyn_aitestcaseinput.md#BKMK_msdyn_aitestcaseinput_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestcaseinput`|
|ReferencedAttribute|`msdyn_aitestcaseinputid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestcaseinput`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestrun_BulkDeleteFailures"></a> msdyn_aitestrun_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aitestrun msdyn_aitestrun_BulkDeleteFailures](msdyn_aitestrun.md#BKMK_msdyn_aitestrun_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestrun`|
|ReferencedAttribute|`msdyn_aitestrunid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestrunbatch_BulkDeleteFailures"></a> msdyn_aitestrunbatch_BulkDeleteFailures

One-To-Many Relationship: [msdyn_aitestrunbatch msdyn_aitestrunbatch_BulkDeleteFailures](msdyn_aitestrunbatch.md#BKMK_msdyn_aitestrunbatch_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestrunbatch`|
|ReferencedAttribute|`msdyn_aitestrunbatchid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestrunbatch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysiscomponent_BulkDeleteFailures"></a> msdyn_analysiscomponent_BulkDeleteFailures

One-To-Many Relationship: [msdyn_analysiscomponent msdyn_analysiscomponent_BulkDeleteFailures](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysiscomponent`|
|ReferencedAttribute|`msdyn_analysiscomponentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysiscomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisjob_BulkDeleteFailures"></a> msdyn_analysisjob_BulkDeleteFailures

One-To-Many Relationship: [msdyn_analysisjob msdyn_analysisjob_BulkDeleteFailures](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisjob`|
|ReferencedAttribute|`msdyn_analysisjobid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysisjob`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisoverride_BulkDeleteFailures"></a> msdyn_analysisoverride_BulkDeleteFailures

One-To-Many Relationship: [msdyn_analysisoverride msdyn_analysisoverride_BulkDeleteFailures](msdyn_analysisoverride.md#BKMK_msdyn_analysisoverride_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisoverride`|
|ReferencedAttribute|`msdyn_analysisoverrideid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysisoverride`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisresult_BulkDeleteFailures"></a> msdyn_analysisresult_BulkDeleteFailures

One-To-Many Relationship: [msdyn_analysisresult msdyn_analysisresult_BulkDeleteFailures](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisresult`|
|ReferencedAttribute|`msdyn_analysisresultid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysisresult`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisresultdetail_BulkDeleteFailures"></a> msdyn_analysisresultdetail_BulkDeleteFailures

One-To-Many Relationship: [msdyn_analysisresultdetail msdyn_analysisresultdetail_BulkDeleteFailures](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisresultdetail`|
|ReferencedAttribute|`msdyn_analysisresultdetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysisresultdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_appinsightsmetadata_BulkDeleteFailures"></a> msdyn_appinsightsmetadata_BulkDeleteFailures

One-To-Many Relationship: [msdyn_appinsightsmetadata msdyn_appinsightsmetadata_BulkDeleteFailures](msdyn_appinsightsmetadata.md#BKMK_msdyn_appinsightsmetadata_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_appinsightsmetadata`|
|ReferencedAttribute|`msdyn_appinsightsmetadataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_appinsightsmetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_copilotinteractions_BulkDeleteFailures"></a> msdyn_copilotinteractions_BulkDeleteFailures

One-To-Many Relationship: [msdyn_copilotinteractions msdyn_copilotinteractions_BulkDeleteFailures](msdyn_copilotinteractions.md#BKMK_msdyn_copilotinteractions_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_copilotinteractions`|
|ReferencedAttribute|`msdyn_copilotinteractionsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_copilotinteractions`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_customcontrolextendedsettings_BulkDeleteFailures"></a> msdyn_customcontrolextendedsettings_BulkDeleteFailures

One-To-Many Relationship: [msdyn_customcontrolextendedsettings msdyn_customcontrolextendedsettings_BulkDeleteFailures](msdyn_customcontrolextendedsettings.md#BKMK_msdyn_customcontrolextendedsettings_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_customcontrolextendedsettings`|
|ReferencedAttribute|`msdyn_customcontrolextendedsettingsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_customcontrolextendedsettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflow_BulkDeleteFailures"></a> msdyn_dataflow_BulkDeleteFailures

One-To-Many Relationship: [msdyn_dataflow msdyn_dataflow_BulkDeleteFailures](msdyn_dataflow.md#BKMK_msdyn_dataflow_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflow`|
|ReferencedAttribute|`msdyn_dataflowid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflow`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflow_datalakefolder_BulkDeleteFailures"></a> msdyn_dataflow_datalakefolder_BulkDeleteFailures

One-To-Many Relationship: [msdyn_dataflow_datalakefolder msdyn_dataflow_datalakefolder_BulkDeleteFailures](msdyn_dataflow_datalakefolder.md#BKMK_msdyn_dataflow_datalakefolder_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflow_datalakefolder`|
|ReferencedAttribute|`msdyn_dataflow_datalakefolderid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflow_datalakefolder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowconnectionreference_BulkDeleteFailures"></a> msdyn_dataflowconnectionreference_BulkDeleteFailures

One-To-Many Relationship: [msdyn_dataflowconnectionreference msdyn_dataflowconnectionreference_BulkDeleteFailures](msdyn_dataflowconnectionreference.md#BKMK_msdyn_dataflowconnectionreference_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowconnectionreference`|
|ReferencedAttribute|`msdyn_dataflowconnectionreferenceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflowconnectionreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowrefreshhistory_BulkDeleteFailures"></a> msdyn_dataflowrefreshhistory_BulkDeleteFailures

One-To-Many Relationship: [msdyn_dataflowrefreshhistory msdyn_dataflowrefreshhistory_BulkDeleteFailures](msdyn_dataflowrefreshhistory.md#BKMK_msdyn_dataflowrefreshhistory_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowrefreshhistory`|
|ReferencedAttribute|`msdyn_dataflowrefreshhistoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflowrefreshhistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowtemplate_BulkDeleteFailures"></a> msdyn_dataflowtemplate_BulkDeleteFailures

One-To-Many Relationship: [msdyn_dataflowtemplate msdyn_dataflowtemplate_BulkDeleteFailures](msdyn_dataflowtemplate.md#BKMK_msdyn_dataflowtemplate_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowtemplate`|
|ReferencedAttribute|`msdyn_dataflowtemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflowtemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmsrequest_BulkDeleteFailures"></a> msdyn_dmsrequest_BulkDeleteFailures

One-To-Many Relationship: [msdyn_dmsrequest msdyn_dmsrequest_BulkDeleteFailures](msdyn_dmsrequest.md#BKMK_msdyn_dmsrequest_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmsrequest`|
|ReferencedAttribute|`msdyn_dmsrequestid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dmsrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmsrequeststatus_BulkDeleteFailures"></a> msdyn_dmsrequeststatus_BulkDeleteFailures

One-To-Many Relationship: [msdyn_dmsrequeststatus msdyn_dmsrequeststatus_BulkDeleteFailures](msdyn_dmsrequeststatus.md#BKMK_msdyn_dmsrequeststatus_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmsrequeststatus`|
|ReferencedAttribute|`msdyn_dmsrequeststatusid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dmsrequeststatus`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmssyncrequest_BulkDeleteFailures"></a> msdyn_dmssyncrequest_BulkDeleteFailures

One-To-Many Relationship: [msdyn_dmssyncrequest msdyn_dmssyncrequest_BulkDeleteFailures](msdyn_dmssyncrequest.md#BKMK_msdyn_dmssyncrequest_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmssyncrequest`|
|ReferencedAttribute|`msdyn_dmssyncrequestid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dmssyncrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmssyncstatus_BulkDeleteFailures"></a> msdyn_dmssyncstatus_BulkDeleteFailures

One-To-Many Relationship: [msdyn_dmssyncstatus msdyn_dmssyncstatus_BulkDeleteFailures](msdyn_dmssyncstatus.md#BKMK_msdyn_dmssyncstatus_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmssyncstatus`|
|ReferencedAttribute|`msdyn_dmssyncstatusid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dmssyncstatus`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_entitylinkchatconfiguration_BulkDeleteFailures"></a> msdyn_entitylinkchatconfiguration_BulkDeleteFailures

One-To-Many Relationship: [msdyn_entitylinkchatconfiguration msdyn_entitylinkchatconfiguration_BulkDeleteFailures](msdyn_entitylinkchatconfiguration.md#BKMK_msdyn_entitylinkchatconfiguration_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_entitylinkchatconfiguration`|
|ReferencedAttribute|`msdyn_entitylinkchatconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_entitylinkchatconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_entityrefreshhistory_BulkDeleteFailures"></a> msdyn_entityrefreshhistory_BulkDeleteFailures

One-To-Many Relationship: [msdyn_entityrefreshhistory msdyn_entityrefreshhistory_BulkDeleteFailures](msdyn_entityrefreshhistory.md#BKMK_msdyn_entityrefreshhistory_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_entityrefreshhistory`|
|ReferencedAttribute|`msdyn_entityrefreshhistoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_entityrefreshhistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_favoriteknowledgearticle_BulkDeleteFailures"></a> msdyn_favoriteknowledgearticle_BulkDeleteFailures

One-To-Many Relationship: [msdyn_favoriteknowledgearticle msdyn_favoriteknowledgearticle_BulkDeleteFailures](msdyn_favoriteknowledgearticle.md#BKMK_msdyn_favoriteknowledgearticle_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_favoriteknowledgearticle`|
|ReferencedAttribute|`msdyn_favoriteknowledgearticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_favoriteknowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_federatedarticle_BulkDeleteFailures"></a> msdyn_federatedarticle_BulkDeleteFailures

One-To-Many Relationship: [msdyn_federatedarticle msdyn_federatedarticle_BulkDeleteFailures](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_federatedarticle`|
|ReferencedAttribute|`msdyn_federatedarticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_federatedarticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_federatedarticleincident_BulkDeleteFailures"></a> msdyn_federatedarticleincident_BulkDeleteFailures

One-To-Many Relationship: [msdyn_federatedarticleincident msdyn_federatedarticleincident_BulkDeleteFailures](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_federatedarticleincident`|
|ReferencedAttribute|`msdyn_federatedarticleincidentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_federatedarticleincident`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_fileupload_BulkDeleteFailures"></a> msdyn_fileupload_BulkDeleteFailures

One-To-Many Relationship: [msdyn_fileupload msdyn_fileupload_BulkDeleteFailures](msdyn_fileupload.md#BKMK_msdyn_fileupload_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_fileupload`|
|ReferencedAttribute|`msdyn_fileuploadid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_fileupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_actionapprovalmodel_BulkDeleteFailures"></a> msdyn_flow_actionapprovalmodel_BulkDeleteFailures

One-To-Many Relationship: [msdyn_flow_actionapprovalmodel msdyn_flow_actionapprovalmodel_BulkDeleteFailures](msdyn_flow_actionapprovalmodel.md#BKMK_msdyn_flow_actionapprovalmodel_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_actionapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_actionapprovalmodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_actionapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approval_BulkDeleteFailures"></a> msdyn_flow_approval_BulkDeleteFailures

One-To-Many Relationship: [msdyn_flow_approval msdyn_flow_approval_BulkDeleteFailures](msdyn_flow_approval.md#BKMK_msdyn_flow_approval_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approval`|
|ReferencedAttribute|`msdyn_flow_approvalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_approval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalrequest_BulkDeleteFailures"></a> msdyn_flow_approvalrequest_BulkDeleteFailures

One-To-Many Relationship: [msdyn_flow_approvalrequest msdyn_flow_approvalrequest_BulkDeleteFailures](msdyn_flow_approvalrequest.md#BKMK_msdyn_flow_approvalrequest_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalrequest`|
|ReferencedAttribute|`msdyn_flow_approvalrequestid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_approvalrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalresponse_BulkDeleteFailures"></a> msdyn_flow_approvalresponse_BulkDeleteFailures

One-To-Many Relationship: [msdyn_flow_approvalresponse msdyn_flow_approvalresponse_BulkDeleteFailures](msdyn_flow_approvalresponse.md#BKMK_msdyn_flow_approvalresponse_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalresponse`|
|ReferencedAttribute|`msdyn_flow_approvalresponseid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_approvalresponse`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalstep_BulkDeleteFailures"></a> msdyn_flow_approvalstep_BulkDeleteFailures

One-To-Many Relationship: [msdyn_flow_approvalstep msdyn_flow_approvalstep_BulkDeleteFailures](msdyn_flow_approvalstep.md#BKMK_msdyn_flow_approvalstep_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalstep`|
|ReferencedAttribute|`msdyn_flow_approvalstepid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_approvalstep`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_awaitallactionapprovalmodel_BulkDeleteFailures"></a> msdyn_flow_awaitallactionapprovalmodel_BulkDeleteFailures

One-To-Many Relationship: [msdyn_flow_awaitallactionapprovalmodel msdyn_flow_awaitallactionapprovalmodel_BulkDeleteFailures](msdyn_flow_awaitallactionapprovalmodel.md#BKMK_msdyn_flow_awaitallactionapprovalmodel_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_awaitallactionapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_awaitallactionapprovalmodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_awaitallactionapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_awaitallapprovalmodel_BulkDeleteFailures"></a> msdyn_flow_awaitallapprovalmodel_BulkDeleteFailures

One-To-Many Relationship: [msdyn_flow_awaitallapprovalmodel msdyn_flow_awaitallapprovalmodel_BulkDeleteFailures](msdyn_flow_awaitallapprovalmodel.md#BKMK_msdyn_flow_awaitallapprovalmodel_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_awaitallapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_awaitallapprovalmodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_awaitallapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_basicapprovalmodel_BulkDeleteFailures"></a> msdyn_flow_basicapprovalmodel_BulkDeleteFailures

One-To-Many Relationship: [msdyn_flow_basicapprovalmodel msdyn_flow_basicapprovalmodel_BulkDeleteFailures](msdyn_flow_basicapprovalmodel.md#BKMK_msdyn_flow_basicapprovalmodel_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_basicapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_basicapprovalmodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_basicapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_flowapproval_BulkDeleteFailures"></a> msdyn_flow_flowapproval_BulkDeleteFailures

One-To-Many Relationship: [msdyn_flow_flowapproval msdyn_flow_flowapproval_BulkDeleteFailures](msdyn_flow_flowapproval.md#BKMK_msdyn_flow_flowapproval_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_flowapproval`|
|ReferencedAttribute|`msdyn_flow_flowapprovalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_flowapproval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_formmapping_BulkDeleteFailures"></a> msdyn_formmapping_BulkDeleteFailures

One-To-Many Relationship: [msdyn_formmapping msdyn_formmapping_BulkDeleteFailures](msdyn_formmapping.md#BKMK_msdyn_formmapping_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_formmapping`|
|ReferencedAttribute|`msdyn_formmappingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_formmapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_function_BulkDeleteFailures"></a> msdyn_function_BulkDeleteFailures

One-To-Many Relationship: [msdyn_function msdyn_function_BulkDeleteFailures](msdyn_function.md#BKMK_msdyn_function_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_function`|
|ReferencedAttribute|`msdyn_functionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_function`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_helppage_BulkDeleteFailures"></a> msdyn_helppage_BulkDeleteFailures

One-To-Many Relationship: [msdyn_helppage msdyn_helppage_BulkDeleteFailures](msdyn_helppage.md#BKMK_msdyn_helppage_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_helppage`|
|ReferencedAttribute|`msdyn_helppageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_helppage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_historicalcaseharvestbatch_BulkDeleteFailures"></a> msdyn_historicalcaseharvestbatch_BulkDeleteFailures

One-To-Many Relationship: [msdyn_historicalcaseharvestbatch msdyn_historicalcaseharvestbatch_BulkDeleteFailures](msdyn_historicalcaseharvestbatch.md#BKMK_msdyn_historicalcaseharvestbatch_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_historicalcaseharvestbatch`|
|ReferencedAttribute|`msdyn_historicalcaseharvestbatchid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_historicalcaseharvestbatch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_historicalcaseharvestrun_BulkDeleteFailures"></a> msdyn_historicalcaseharvestrun_BulkDeleteFailures

One-To-Many Relationship: [msdyn_historicalcaseharvestrun msdyn_historicalcaseharvestrun_BulkDeleteFailures](msdyn_historicalcaseharvestrun.md#BKMK_msdyn_historicalcaseharvestrun_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_historicalcaseharvestrun`|
|ReferencedAttribute|`msdyn_historicalcaseharvestrunid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_historicalcaseharvestrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_insightsstorevirtualentity_BulkDeleteFailures"></a> msdyn_insightsstorevirtualentity_BulkDeleteFailures

One-To-Many Relationship: [msdyn_insightsstorevirtualentity msdyn_insightsstorevirtualentity_BulkDeleteFailures](msdyn_insightsstorevirtualentity.md#BKMK_msdyn_insightsstorevirtualentity_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_insightsstorevirtualentity`|
|ReferencedAttribute|`msdyn_insightsstorevirtualentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_insightsstorevirtualentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_integratedsearchprovider_BulkDeleteFailures"></a> msdyn_integratedsearchprovider_BulkDeleteFailures

One-To-Many Relationship: [msdyn_integratedsearchprovider msdyn_integratedsearchprovider_BulkDeleteFailures](msdyn_integratedsearchprovider.md#BKMK_msdyn_integratedsearchprovider_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_integratedsearchprovider`|
|ReferencedAttribute|`msdyn_integratedsearchproviderid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_integratedsearchprovider`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kalanguagesetting_BulkDeleteFailures"></a> msdyn_kalanguagesetting_BulkDeleteFailures

One-To-Many Relationship: [msdyn_kalanguagesetting msdyn_kalanguagesetting_BulkDeleteFailures](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kalanguagesetting`|
|ReferencedAttribute|`msdyn_kalanguagesettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_kalanguagesetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kbattachment_BulkDeleteFailures"></a> msdyn_kbattachment_BulkDeleteFailures

One-To-Many Relationship: [msdyn_kbattachment msdyn_kbattachment_BulkDeleteFailures](msdyn_kbattachment.md#BKMK_msdyn_kbattachment_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kbattachment`|
|ReferencedAttribute|`msdyn_kbattachmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_kbattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kmfederatedsearchconfig_BulkDeleteFailures"></a> msdyn_kmfederatedsearchconfig_BulkDeleteFailures

One-To-Many Relationship: [msdyn_kmfederatedsearchconfig msdyn_kmfederatedsearchconfig_BulkDeleteFailures](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kmfederatedsearchconfig`|
|ReferencedAttribute|`msdyn_kmfederatedsearchconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_kmfederatedsearchconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kmpersonalizationsetting_BulkDeleteFailures"></a> msdyn_kmpersonalizationsetting_BulkDeleteFailures

One-To-Many Relationship: [msdyn_kmpersonalizationsetting msdyn_kmpersonalizationsetting_BulkDeleteFailures](msdyn_kmpersonalizationsetting.md#BKMK_msdyn_kmpersonalizationsetting_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kmpersonalizationsetting`|
|ReferencedAttribute|`msdyn_kmpersonalizationsettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_kmpersonalizationsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgearticleimage_BulkDeleteFailures"></a> msdyn_knowledgearticleimage_BulkDeleteFailures

One-To-Many Relationship: [msdyn_knowledgearticleimage msdyn_knowledgearticleimage_BulkDeleteFailures](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgearticleimage`|
|ReferencedAttribute|`msdyn_knowledgearticleimageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgearticleimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgearticletemplate_BulkDeleteFailures"></a> msdyn_knowledgearticletemplate_BulkDeleteFailures

One-To-Many Relationship: [msdyn_knowledgearticletemplate msdyn_knowledgearticletemplate_BulkDeleteFailures](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgearticletemplate`|
|ReferencedAttribute|`msdyn_knowledgearticletemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgearticletemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeassetconfiguration_BulkDeleteFailures"></a> msdyn_knowledgeassetconfiguration_BulkDeleteFailures

One-To-Many Relationship: [msdyn_knowledgeassetconfiguration msdyn_knowledgeassetconfiguration_BulkDeleteFailures](msdyn_knowledgeassetconfiguration.md#BKMK_msdyn_knowledgeassetconfiguration_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeassetconfiguration`|
|ReferencedAttribute|`msdyn_knowledgeassetconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgeassetconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeconfiguration_BulkDeleteFailures"></a> msdyn_knowledgeconfiguration_BulkDeleteFailures

One-To-Many Relationship: [msdyn_knowledgeconfiguration msdyn_knowledgeconfiguration_BulkDeleteFailures](msdyn_knowledgeconfiguration.md#BKMK_msdyn_knowledgeconfiguration_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeconfiguration`|
|ReferencedAttribute|`msdyn_knowledgeconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeharvestjobrecord_BulkDeleteFailures"></a> msdyn_knowledgeharvestjobrecord_BulkDeleteFailures

One-To-Many Relationship: [msdyn_knowledgeharvestjobrecord msdyn_knowledgeharvestjobrecord_BulkDeleteFailures](msdyn_knowledgeharvestjobrecord.md#BKMK_msdyn_knowledgeharvestjobrecord_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeharvestjobrecord`|
|ReferencedAttribute|`msdyn_knowledgeharvestjobrecordid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgeharvestjobrecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeinteractioninsight_BulkDeleteFailures"></a> msdyn_knowledgeinteractioninsight_BulkDeleteFailures

One-To-Many Relationship: [msdyn_knowledgeinteractioninsight msdyn_knowledgeinteractioninsight_BulkDeleteFailures](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeinteractioninsight`|
|ReferencedAttribute|`msdyn_knowledgeinteractioninsightid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgeinteractioninsight`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgemanagementsetting_BulkDeleteFailures"></a> msdyn_knowledgemanagementsetting_BulkDeleteFailures

One-To-Many Relationship: [msdyn_knowledgemanagementsetting msdyn_knowledgemanagementsetting_BulkDeleteFailures](msdyn_knowledgemanagementsetting.md#BKMK_msdyn_knowledgemanagementsetting_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgemanagementsetting`|
|ReferencedAttribute|`msdyn_knowledgemanagementsettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgemanagementsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgepersonalfilter_BulkDeleteFailures"></a> msdyn_knowledgepersonalfilter_BulkDeleteFailures

One-To-Many Relationship: [msdyn_knowledgepersonalfilter msdyn_knowledgepersonalfilter_BulkDeleteFailures](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgepersonalfilter`|
|ReferencedAttribute|`msdyn_knowledgepersonalfilterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgepersonalfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgesearchfilter_BulkDeleteFailures"></a> msdyn_knowledgesearchfilter_BulkDeleteFailures

One-To-Many Relationship: [msdyn_knowledgesearchfilter msdyn_knowledgesearchfilter_BulkDeleteFailures](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgesearchfilter`|
|ReferencedAttribute|`msdyn_knowledgesearchfilterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgesearchfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgesearchinsight_BulkDeleteFailures"></a> msdyn_knowledgesearchinsight_BulkDeleteFailures

One-To-Many Relationship: [msdyn_knowledgesearchinsight msdyn_knowledgesearchinsight_BulkDeleteFailures](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgesearchinsight`|
|ReferencedAttribute|`msdyn_knowledgesearchinsightid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgesearchinsight`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_mobileapp_BulkDeleteFailures"></a> msdyn_mobileapp_BulkDeleteFailures

One-To-Many Relationship: [msdyn_mobileapp msdyn_mobileapp_BulkDeleteFailures](msdyn_mobileapp.md#BKMK_msdyn_mobileapp_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_mobileapp`|
|ReferencedAttribute|`msdyn_mobileappid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_mobileapp`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_modulerundetail_BulkDeleteFailures"></a> msdyn_modulerundetail_BulkDeleteFailures

One-To-Many Relationship: [msdyn_modulerundetail msdyn_modulerundetail_BulkDeleteFailures](msdyn_modulerundetail.md#BKMK_msdyn_modulerundetail_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_modulerundetail`|
|ReferencedAttribute|`msdyn_modulerundetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_modulerundetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmanalysishistory_BulkDeleteFailures"></a> msdyn_pmanalysishistory_BulkDeleteFailures

One-To-Many Relationship: [msdyn_pmanalysishistory msdyn_pmanalysishistory_BulkDeleteFailures](msdyn_pmanalysishistory.md#BKMK_msdyn_pmanalysishistory_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmanalysishistory`|
|ReferencedAttribute|`msdyn_pmanalysishistoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmanalysishistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmbusinessruleautomationconfig_BulkDeleteFailures"></a> msdyn_pmbusinessruleautomationconfig_BulkDeleteFailures

One-To-Many Relationship: [msdyn_pmbusinessruleautomationconfig msdyn_pmbusinessruleautomationconfig_BulkDeleteFailures](msdyn_pmbusinessruleautomationconfig.md#BKMK_msdyn_pmbusinessruleautomationconfig_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmbusinessruleautomationconfig`|
|ReferencedAttribute|`msdyn_pmbusinessruleautomationconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmbusinessruleautomationconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmcalendar_BulkDeleteFailures"></a> msdyn_pmcalendar_BulkDeleteFailures

One-To-Many Relationship: [msdyn_pmcalendar msdyn_pmcalendar_BulkDeleteFailures](msdyn_pmcalendar.md#BKMK_msdyn_pmcalendar_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmcalendar`|
|ReferencedAttribute|`msdyn_pmcalendarid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmcalendar`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmcalendarversion_BulkDeleteFailures"></a> msdyn_pmcalendarversion_BulkDeleteFailures

One-To-Many Relationship: [msdyn_pmcalendarversion msdyn_pmcalendarversion_BulkDeleteFailures](msdyn_pmcalendarversion.md#BKMK_msdyn_pmcalendarversion_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmcalendarversion`|
|ReferencedAttribute|`msdyn_pmcalendarversionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmcalendarversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pminferredtask_BulkDeleteFailures"></a> msdyn_pminferredtask_BulkDeleteFailures

One-To-Many Relationship: [msdyn_pminferredtask msdyn_pminferredtask_BulkDeleteFailures](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pminferredtask`|
|ReferencedAttribute|`msdyn_pminferredtaskid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pminferredtask`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessextendedmetadataversion_BulkDeleteFailures"></a> msdyn_pmprocessextendedmetadataversion_BulkDeleteFailures

One-To-Many Relationship: [msdyn_pmprocessextendedmetadataversion msdyn_pmprocessextendedmetadataversion_BulkDeleteFailures](msdyn_pmprocessextendedmetadataversion.md#BKMK_msdyn_pmprocessextendedmetadataversion_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessextendedmetadataversion`|
|ReferencedAttribute|`msdyn_pmprocessextendedmetadataversionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmprocessextendedmetadataversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocesstemplate_BulkDeleteFailures"></a> msdyn_pmprocesstemplate_BulkDeleteFailures

One-To-Many Relationship: [msdyn_pmprocesstemplate msdyn_pmprocesstemplate_BulkDeleteFailures](msdyn_pmprocesstemplate.md#BKMK_msdyn_pmprocesstemplate_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocesstemplate`|
|ReferencedAttribute|`msdyn_pmprocesstemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmprocesstemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessusersettings_BulkDeleteFailures"></a> msdyn_pmprocessusersettings_BulkDeleteFailures

One-To-Many Relationship: [msdyn_pmprocessusersettings msdyn_pmprocessusersettings_BulkDeleteFailures](msdyn_pmprocessusersettings.md#BKMK_msdyn_pmprocessusersettings_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessusersettings`|
|ReferencedAttribute|`msdyn_pmprocessusersettingsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmprocessusersettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessversion_BulkDeleteFailures"></a> msdyn_pmprocessversion_BulkDeleteFailures

One-To-Many Relationship: [msdyn_pmprocessversion msdyn_pmprocessversion_BulkDeleteFailures](msdyn_pmprocessversion.md#BKMK_msdyn_pmprocessversion_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessversion`|
|ReferencedAttribute|`msdyn_pmprocessversionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmprocessversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmrecording_BulkDeleteFailures"></a> msdyn_pmrecording_BulkDeleteFailures

One-To-Many Relationship: [msdyn_pmrecording msdyn_pmrecording_BulkDeleteFailures](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmrecording`|
|ReferencedAttribute|`msdyn_pmrecordingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmrecording`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmsimulation_BulkDeleteFailures"></a> msdyn_pmsimulation_BulkDeleteFailures

One-To-Many Relationship: [msdyn_pmsimulation msdyn_pmsimulation_BulkDeleteFailures](msdyn_pmsimulation.md#BKMK_msdyn_pmsimulation_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmsimulation`|
|ReferencedAttribute|`msdyn_pmsimulationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmsimulation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmtab_BulkDeleteFailures"></a> msdyn_pmtab_BulkDeleteFailures

One-To-Many Relationship: [msdyn_pmtab msdyn_pmtab_BulkDeleteFailures](msdyn_pmtab.md#BKMK_msdyn_pmtab_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmtab`|
|ReferencedAttribute|`msdyn_pmtabid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmtab`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmtemplate_BulkDeleteFailures"></a> msdyn_pmtemplate_BulkDeleteFailures

One-To-Many Relationship: [msdyn_pmtemplate msdyn_pmtemplate_BulkDeleteFailures](msdyn_pmtemplate.md#BKMK_msdyn_pmtemplate_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmtemplate`|
|ReferencedAttribute|`msdyn_pmtemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmtemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmview_BulkDeleteFailures"></a> msdyn_pmview_BulkDeleteFailures

One-To-Many Relationship: [msdyn_pmview msdyn_pmview_BulkDeleteFailures](msdyn_pmview.md#BKMK_msdyn_pmview_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmview`|
|ReferencedAttribute|`msdyn_pmviewid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmview`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_qna_BulkDeleteFailures"></a> msdyn_qna_BulkDeleteFailures

One-To-Many Relationship: [msdyn_qna msdyn_qna_BulkDeleteFailures](msdyn_qna.md#BKMK_msdyn_qna_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_qna`|
|ReferencedAttribute|`msdyn_qnaid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_qna`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_richtextfile_BulkDeleteFailures"></a> msdyn_richtextfile_BulkDeleteFailures

One-To-Many Relationship: [msdyn_richtextfile msdyn_richtextfile_BulkDeleteFailures](msdyn_richtextfile.md#BKMK_msdyn_richtextfile_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_richtextfile`|
|ReferencedAttribute|`msdyn_richtextfileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_richtextfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_salesforcestructuredobject_BulkDeleteFailures"></a> msdyn_salesforcestructuredobject_BulkDeleteFailures

One-To-Many Relationship: [msdyn_salesforcestructuredobject msdyn_salesforcestructuredobject_BulkDeleteFailures](msdyn_salesforcestructuredobject.md#BKMK_msdyn_salesforcestructuredobject_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_salesforcestructuredobject`|
|ReferencedAttribute|`msdyn_salesforcestructuredobjectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_salesforcestructuredobject`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_salesforcestructuredqnaconfig_BulkDeleteFailures"></a> msdyn_salesforcestructuredqnaconfig_BulkDeleteFailures

One-To-Many Relationship: [msdyn_salesforcestructuredqnaconfig msdyn_salesforcestructuredqnaconfig_BulkDeleteFailures](msdyn_salesforcestructuredqnaconfig.md#BKMK_msdyn_salesforcestructuredqnaconfig_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_salesforcestructuredqnaconfig`|
|ReferencedAttribute|`msdyn_salesforcestructuredqnaconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_salesforcestructuredqnaconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_schedule_BulkDeleteFailures"></a> msdyn_schedule_BulkDeleteFailures

One-To-Many Relationship: [msdyn_schedule msdyn_schedule_BulkDeleteFailures](msdyn_schedule.md#BKMK_msdyn_schedule_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_schedule`|
|ReferencedAttribute|`msdyn_scheduleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_schedule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_serviceconfiguration_BulkDeleteFailures"></a> msdyn_serviceconfiguration_BulkDeleteFailures

One-To-Many Relationship: [msdyn_serviceconfiguration msdyn_serviceconfiguration_BulkDeleteFailures](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_serviceconfiguration`|
|ReferencedAttribute|`msdyn_serviceconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_serviceconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_slakpi_BulkDeleteFailures"></a> msdyn_slakpi_BulkDeleteFailures

One-To-Many Relationship: [msdyn_slakpi msdyn_slakpi_BulkDeleteFailures](msdyn_slakpi.md#BKMK_msdyn_slakpi_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_slakpi`|
|ReferencedAttribute|`msdyn_slakpiid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_slakpi`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthrule_BulkDeleteFailures"></a> msdyn_solutionhealthrule_BulkDeleteFailures

One-To-Many Relationship: [msdyn_solutionhealthrule msdyn_solutionhealthrule_BulkDeleteFailures](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthrule`|
|ReferencedAttribute|`msdyn_solutionhealthruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_solutionhealthrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthruleargument_BulkDeleteFailures"></a> msdyn_solutionhealthruleargument_BulkDeleteFailures

One-To-Many Relationship: [msdyn_solutionhealthruleargument msdyn_solutionhealthruleargument_BulkDeleteFailures](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthruleargument`|
|ReferencedAttribute|`msdyn_solutionhealthruleargumentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_solutionhealthruleargument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthruleset_BulkDeleteFailures"></a> msdyn_solutionhealthruleset_BulkDeleteFailures

One-To-Many Relationship: [msdyn_solutionhealthruleset msdyn_solutionhealthruleset_BulkDeleteFailures](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthruleset`|
|ReferencedAttribute|`msdyn_solutionhealthrulesetid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_solutionhealthruleset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_tour_BulkDeleteFailures"></a> msdyn_tour_BulkDeleteFailures

One-To-Many Relationship: [msdyn_tour msdyn_tour_BulkDeleteFailures](msdyn_tour.md#BKMK_msdyn_tour_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_tour`|
|ReferencedAttribute|`msdyn_tourid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_tour`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_virtualtablecolumncandidate_BulkDeleteFailures"></a> msdyn_virtualtablecolumncandidate_BulkDeleteFailures

One-To-Many Relationship: [msdyn_virtualtablecolumncandidate msdyn_virtualtablecolumncandidate_BulkDeleteFailures](msdyn_virtualtablecolumncandidate.md#BKMK_msdyn_virtualtablecolumncandidate_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_virtualtablecolumncandidate`|
|ReferencedAttribute|`msdyn_virtualtablecolumncandidateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_virtualtablecolumncandidate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_workflowactionstatus_BulkDeleteFailures"></a> msdyn_workflowactionstatus_BulkDeleteFailures

One-To-Many Relationship: [msdyn_workflowactionstatus msdyn_workflowactionstatus_BulkDeleteFailures](msdyn_workflowactionstatus.md#BKMK_msdyn_workflowactionstatus_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_workflowactionstatus`|
|ReferencedAttribute|`msdyn_workflowactionstatusid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_workflowactionstatus`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdynce_botcontent_BulkDeleteFailures"></a> msdynce_botcontent_BulkDeleteFailures

One-To-Many Relationship: [msdynce_botcontent msdynce_botcontent_BulkDeleteFailures](msdynce_botcontent.md#BKMK_msdynce_botcontent_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msdynce_botcontent`|
|ReferencedAttribute|`msdynce_botcontentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdynce_botcontent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msgraphresourcetosubscription_BulkDeleteFailures"></a> msgraphresourcetosubscription_BulkDeleteFailures

One-To-Many Relationship: [msgraphresourcetosubscription msgraphresourcetosubscription_BulkDeleteFailures](msgraphresourcetosubscription.md#BKMK_msgraphresourcetosubscription_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`msgraphresourcetosubscription`|
|ReferencedAttribute|`msgraphresourcetosubscriptionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msgraphresourcetosubscription`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspcat_catalogsubmissionfiles_BulkDeleteFailures"></a> mspcat_catalogsubmissionfiles_BulkDeleteFailures

One-To-Many Relationship: [mspcat_catalogsubmissionfiles mspcat_catalogsubmissionfiles_BulkDeleteFailures](mspcat_catalogsubmissionfiles.md#BKMK_mspcat_catalogsubmissionfiles_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`mspcat_catalogsubmissionfiles`|
|ReferencedAttribute|`mspcat_catalogsubmissionfilesid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspcat_catalogsubmissionfiles`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspcat_packagestore_BulkDeleteFailures"></a> mspcat_packagestore_BulkDeleteFailures

One-To-Many Relationship: [mspcat_packagestore mspcat_packagestore_BulkDeleteFailures](mspcat_packagestore.md#BKMK_mspcat_packagestore_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`mspcat_packagestore`|
|ReferencedAttribute|`mspcat_packagestoreid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspcat_packagestore`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Organization_BulkDeleteFailures"></a> Organization_BulkDeleteFailures

One-To-Many Relationship: [organization Organization_BulkDeleteFailures](organization.md#BKMK_Organization_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organization`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncfnostate_BulkDeleteFailures"></a> organizationdatasyncfnostate_BulkDeleteFailures

One-To-Many Relationship: [organizationdatasyncfnostate organizationdatasyncfnostate_BulkDeleteFailures](organizationdatasyncfnostate.md#BKMK_organizationdatasyncfnostate_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncfnostate`|
|ReferencedAttribute|`organizationdatasyncfnostateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncfnostate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncstate_BulkDeleteFailures"></a> organizationdatasyncstate_BulkDeleteFailures

One-To-Many Relationship: [organizationdatasyncstate organizationdatasyncstate_BulkDeleteFailures](organizationdatasyncstate.md#BKMK_organizationdatasyncstate_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncstate`|
|ReferencedAttribute|`organizationdatasyncstateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncstate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscription_BulkDeleteFailures"></a> organizationdatasyncsubscription_BulkDeleteFailures

One-To-Many Relationship: [organizationdatasyncsubscription organizationdatasyncsubscription_BulkDeleteFailures](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscription`|
|ReferencedAttribute|`organizationdatasyncsubscriptionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncsubscription`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscriptionentity_BulkDeleteFailures"></a> organizationdatasyncsubscriptionentity_BulkDeleteFailures

One-To-Many Relationship: [organizationdatasyncsubscriptionentity organizationdatasyncsubscriptionentity_BulkDeleteFailures](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscriptionentity`|
|ReferencedAttribute|`organizationdatasyncsubscriptionentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncsubscriptionentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_BulkDeleteFailures"></a> organizationdatasyncsubscriptionfnotable_BulkDeleteFailures

One-To-Many Relationship: [organizationdatasyncsubscriptionfnotable organizationdatasyncsubscriptionfnotable_BulkDeleteFailures](organizationdatasyncsubscriptionfnotable.md#BKMK_organizationdatasyncsubscriptionfnotable_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscriptionfnotable`|
|ReferencedAttribute|`organizationdatasyncsubscriptionfnotableid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncsubscriptionfnotable`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_package_BulkDeleteFailures"></a> package_BulkDeleteFailures

One-To-Many Relationship: [package package_BulkDeleteFailures](package.md#BKMK_package_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`package`|
|ReferencedAttribute|`packageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_package`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_packagehistory_BulkDeleteFailures"></a> packagehistory_BulkDeleteFailures

One-To-Many Relationship: [packagehistory packagehistory_BulkDeleteFailures](packagehistory.md#BKMK_packagehistory_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`packagehistory`|
|ReferencedAttribute|`packagehistoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_packagehistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_PhoneCall_BulkDeleteFailures"></a> PhoneCall_BulkDeleteFailures

One-To-Many Relationship: [phonecall PhoneCall_BulkDeleteFailures](phonecall.md#BKMK_PhoneCall_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`phonecall`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_phonecall`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plannerbusinessscenario_BulkDeleteFailures"></a> plannerbusinessscenario_BulkDeleteFailures

One-To-Many Relationship: [plannerbusinessscenario plannerbusinessscenario_BulkDeleteFailures](plannerbusinessscenario.md#BKMK_plannerbusinessscenario_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`plannerbusinessscenario`|
|ReferencedAttribute|`plannerbusinessscenarioid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_plannerbusinessscenario`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plannersyncaction_BulkDeleteFailures"></a> plannersyncaction_BulkDeleteFailures

One-To-Many Relationship: [plannersyncaction plannersyncaction_BulkDeleteFailures](plannersyncaction.md#BKMK_plannersyncaction_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`plannersyncaction`|
|ReferencedAttribute|`plannersyncactionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_plannersyncaction`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plugin_BulkDeleteFailures"></a> plugin_BulkDeleteFailures

One-To-Many Relationship: [plugin plugin_BulkDeleteFailures](plugin.md#BKMK_plugin_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`plugin`|
|ReferencedAttribute|`pluginid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_plugin`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_pluginpackage_BulkDeleteFailures"></a> pluginpackage_BulkDeleteFailures

One-To-Many Relationship: [pluginpackage pluginpackage_BulkDeleteFailures](pluginpackage.md#BKMK_pluginpackage_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`pluginpackage`|
|ReferencedAttribute|`pluginpackageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_pluginpackage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_post_BulkDeleteFailures"></a> post_BulkDeleteFailures

One-To-Many Relationship: [post post_BulkDeleteFailures](post.md#BKMK_post_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`post`|
|ReferencedAttribute|`postid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_post`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbidataset_BulkDeleteFailures"></a> powerbidataset_BulkDeleteFailures

One-To-Many Relationship: [powerbidataset powerbidataset_BulkDeleteFailures](powerbidataset.md#BKMK_powerbidataset_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbidataset`|
|ReferencedAttribute|`powerbidatasetid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbidataset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbidatasetapdx_BulkDeleteFailures"></a> powerbidatasetapdx_BulkDeleteFailures

One-To-Many Relationship: [powerbidatasetapdx powerbidatasetapdx_BulkDeleteFailures](powerbidatasetapdx.md#BKMK_powerbidatasetapdx_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbidatasetapdx`|
|ReferencedAttribute|`powerbidatasetapdxid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbidatasetapdx`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbimashupparameter_BulkDeleteFailures"></a> powerbimashupparameter_BulkDeleteFailures

One-To-Many Relationship: [powerbimashupparameter powerbimashupparameter_BulkDeleteFailures](powerbimashupparameter.md#BKMK_powerbimashupparameter_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbimashupparameter`|
|ReferencedAttribute|`powerbimashupparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbimashupparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbireport_BulkDeleteFailures"></a> powerbireport_BulkDeleteFailures

One-To-Many Relationship: [powerbireport powerbireport_BulkDeleteFailures](powerbireport.md#BKMK_powerbireport_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbireport`|
|ReferencedAttribute|`powerbireportid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbireport`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbireportapdx_BulkDeleteFailures"></a> powerbireportapdx_BulkDeleteFailures

One-To-Many Relationship: [powerbireportapdx powerbireportapdx_BulkDeleteFailures](powerbireportapdx.md#BKMK_powerbireportapdx_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbireportapdx`|
|ReferencedAttribute|`powerbireportapdxid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbireportapdx`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerfxrule_BulkDeleteFailures"></a> powerfxrule_BulkDeleteFailures

One-To-Many Relationship: [powerfxrule powerfxrule_BulkDeleteFailures](powerfxrule.md#BKMK_powerfxrule_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`powerfxrule`|
|ReferencedAttribute|`powerfxruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerfxrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagecomponent_BulkDeleteFailures"></a> powerpagecomponent_BulkDeleteFailures

One-To-Many Relationship: [powerpagecomponent powerpagecomponent_BulkDeleteFailures](powerpagecomponent.md#BKMK_powerpagecomponent_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagecomponent`|
|ReferencedAttribute|`powerpagecomponentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagecomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesddosalert_BulkDeleteFailures"></a> powerpagesddosalert_BulkDeleteFailures

One-To-Many Relationship: [powerpagesddosalert powerpagesddosalert_BulkDeleteFailures](powerpagesddosalert.md#BKMK_powerpagesddosalert_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesddosalert`|
|ReferencedAttribute|`powerpagesddosalertid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesddosalert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesite_BulkDeleteFailures"></a> powerpagesite_BulkDeleteFailures

One-To-Many Relationship: [powerpagesite powerpagesite_BulkDeleteFailures](powerpagesite.md#BKMK_powerpagesite_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesite`|
|ReferencedAttribute|`powerpagesiteid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesite`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesitelanguage_BulkDeleteFailures"></a> powerpagesitelanguage_BulkDeleteFailures

One-To-Many Relationship: [powerpagesitelanguage powerpagesitelanguage_BulkDeleteFailures](powerpagesitelanguage.md#BKMK_powerpagesitelanguage_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesitelanguage`|
|ReferencedAttribute|`powerpagesitelanguageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesitelanguage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesitepublished_BulkDeleteFailures"></a> powerpagesitepublished_BulkDeleteFailures

One-To-Many Relationship: [powerpagesitepublished powerpagesitepublished_BulkDeleteFailures](powerpagesitepublished.md#BKMK_powerpagesitepublished_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesitepublished`|
|ReferencedAttribute|`powerpagesitepublishedid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesitepublished`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesmanagedidentity_BulkDeleteFailures"></a> powerpagesmanagedidentity_BulkDeleteFailures

One-To-Many Relationship: [powerpagesmanagedidentity powerpagesmanagedidentity_BulkDeleteFailures](powerpagesmanagedidentity.md#BKMK_powerpagesmanagedidentity_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesmanagedidentity`|
|ReferencedAttribute|`powerpagesmanagedidentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesmanagedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesscanreport_BulkDeleteFailures"></a> powerpagesscanreport_BulkDeleteFailures

One-To-Many Relationship: [powerpagesscanreport powerpagesscanreport_BulkDeleteFailures](powerpagesscanreport.md#BKMK_powerpagesscanreport_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesscanreport`|
|ReferencedAttribute|`powerpagesscanreportid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesscanreport`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagessourcefile_BulkDeleteFailures"></a> powerpagessourcefile_BulkDeleteFailures

One-To-Many Relationship: [powerpagessourcefile powerpagessourcefile_BulkDeleteFailures](powerpagessourcefile.md#BKMK_powerpagessourcefile_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagessourcefile`|
|ReferencedAttribute|`powerpagessourcefileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagessourcefile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Privilege_BulkDeleteFailures"></a> Privilege_BulkDeleteFailures

One-To-Many Relationship: [privilege Privilege_BulkDeleteFailures](privilege.md#BKMK_Privilege_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`privilege`|
|ReferencedAttribute|`privilegeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_privilege`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegecheckerlog_BulkDeleteFailures"></a> privilegecheckerlog_BulkDeleteFailures

One-To-Many Relationship: [privilegecheckerlog privilegecheckerlog_BulkDeleteFailures](privilegecheckerlog.md#BKMK_privilegecheckerlog_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegecheckerlog`|
|ReferencedAttribute|`privilegecheckerlogid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_privilegecheckerlog`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegecheckerrun_BulkDeleteFailures"></a> privilegecheckerrun_BulkDeleteFailures

One-To-Many Relationship: [privilegecheckerrun privilegecheckerrun_BulkDeleteFailures](privilegecheckerrun.md#BKMK_privilegecheckerrun_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegecheckerrun`|
|ReferencedAttribute|`privilegecheckerrunid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_privilegecheckerrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegesremovalsetting_BulkDeleteFailures"></a> privilegesremovalsetting_BulkDeleteFailures

One-To-Many Relationship: [privilegesremovalsetting privilegesremovalsetting_BulkDeleteFailures](privilegesremovalsetting.md#BKMK_privilegesremovalsetting_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegesremovalsetting`|
|ReferencedAttribute|`privilegesremovalsettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_privilegesremovalsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_processstageparameter_BulkDeleteFailures"></a> processstageparameter_BulkDeleteFailures

One-To-Many Relationship: [processstageparameter processstageparameter_BulkDeleteFailures](processstageparameter.md#BKMK_processstageparameter_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`processstageparameter`|
|ReferencedAttribute|`processstageparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_processstageparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_provisionlanguageforuser_BulkDeleteFailures"></a> provisionlanguageforuser_BulkDeleteFailures

One-To-Many Relationship: [provisionlanguageforuser provisionlanguageforuser_BulkDeleteFailures](provisionlanguageforuser.md#BKMK_provisionlanguageforuser_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`provisionlanguageforuser`|
|ReferencedAttribute|`provisionlanguageforuserid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_provisionlanguageforuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_purviewlabelinfo_BulkDeleteFailures"></a> purviewlabelinfo_BulkDeleteFailures

One-To-Many Relationship: [purviewlabelinfo purviewlabelinfo_BulkDeleteFailures](purviewlabelinfo.md#BKMK_purviewlabelinfo_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`purviewlabelinfo`|
|ReferencedAttribute|`purviewlabelinfoid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_purviewlabelinfo`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_QuarterlyFiscalCalendar_BulkDeleteFailures"></a> QuarterlyFiscalCalendar_BulkDeleteFailures

One-To-Many Relationship: [quarterlyfiscalcalendar QuarterlyFiscalCalendar_BulkDeleteFailures](quarterlyfiscalcalendar.md#BKMK_QuarterlyFiscalCalendar_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`quarterlyfiscalcalendar`|
|ReferencedAttribute|`userfiscalcalendarid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_quarterlyfiscalcalendar`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Queue_BulkDeleteFailures"></a> Queue_BulkDeleteFailures

One-To-Many Relationship: [queue Queue_BulkDeleteFailures](queue.md#BKMK_Queue_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`queue`|
|ReferencedAttribute|`queueid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_queue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_QueueItem_BulkDeleteFailures"></a> QueueItem_BulkDeleteFailures

One-To-Many Relationship: [queueitem QueueItem_BulkDeleteFailures](queueitem.md#BKMK_QueueItem_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`queueitem`|
|ReferencedAttribute|`queueitemid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_queueitem`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recordfilter_BulkDeleteFailures"></a> recordfilter_BulkDeleteFailures

One-To-Many Relationship: [recordfilter recordfilter_BulkDeleteFailures](recordfilter.md#BKMK_recordfilter_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`recordfilter`|
|ReferencedAttribute|`recordfilterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_recordfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_RecurringAppointmentMaster_BulkDeleteFailures"></a> RecurringAppointmentMaster_BulkDeleteFailures

One-To-Many Relationship: [recurringappointmentmaster RecurringAppointmentMaster_BulkDeleteFailures](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`recurringappointmentmaster`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recyclebinconfig_BulkDeleteFailures"></a> recyclebinconfig_BulkDeleteFailures

One-To-Many Relationship: [recyclebinconfig recyclebinconfig_BulkDeleteFailures](recyclebinconfig.md#BKMK_recyclebinconfig_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`recyclebinconfig`|
|ReferencedAttribute|`recyclebinconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_recyclebinconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_relationshipattribute_BulkDeleteFailures"></a> relationshipattribute_BulkDeleteFailures

One-To-Many Relationship: [relationshipattribute relationshipattribute_BulkDeleteFailures](relationshipattribute.md#BKMK_relationshipattribute_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`relationshipattribute`|
|ReferencedAttribute|`relationshipattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_relationshipattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_reportparameter_BulkDeleteFailures"></a> reportparameter_BulkDeleteFailures

One-To-Many Relationship: [reportparameter reportparameter_BulkDeleteFailures](reportparameter.md#BKMK_reportparameter_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`reportparameter`|
|ReferencedAttribute|`reportparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_reportparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retaineddataexcel_BulkDeleteFailures"></a> retaineddataexcel_BulkDeleteFailures

One-To-Many Relationship: [retaineddataexcel retaineddataexcel_BulkDeleteFailures](retaineddataexcel.md#BKMK_retaineddataexcel_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`retaineddataexcel`|
|ReferencedAttribute|`retaineddataexcelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retaineddataexcel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionconfig_BulkDeleteFailures"></a> retentionconfig_BulkDeleteFailures

One-To-Many Relationship: [retentionconfig retentionconfig_BulkDeleteFailures](retentionconfig.md#BKMK_retentionconfig_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionconfig`|
|ReferencedAttribute|`retentionconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionfailuredetail_BulkDeleteFailures"></a> retentionfailuredetail_BulkDeleteFailures

One-To-Many Relationship: [retentionfailuredetail retentionfailuredetail_BulkDeleteFailures](retentionfailuredetail.md#BKMK_retentionfailuredetail_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionfailuredetail`|
|ReferencedAttribute|`retentionfailuredetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionfailuredetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionoperation_BulkDeleteFailures"></a> retentionoperation_BulkDeleteFailures

One-To-Many Relationship: [retentionoperation retentionoperation_BulkDeleteFailures](retentionoperation.md#BKMK_retentionoperation_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionoperation`|
|ReferencedAttribute|`retentionoperationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionoperationdetail_BulkDeleteFailures"></a> retentionoperationdetail_BulkDeleteFailures

One-To-Many Relationship: [retentionoperationdetail retentionoperationdetail_BulkDeleteFailures](retentionoperationdetail.md#BKMK_retentionoperationdetail_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionoperationdetail`|
|ReferencedAttribute|`retentionoperationdetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionoperationdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionsuccessdetail_BulkDeleteFailures"></a> retentionsuccessdetail_BulkDeleteFailures

One-To-Many Relationship: [retentionsuccessdetail retentionsuccessdetail_BulkDeleteFailures](retentionsuccessdetail.md#BKMK_retentionsuccessdetail_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionsuccessdetail`|
|ReferencedAttribute|`retentionsuccessdetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionsuccessdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Role_BulkDeleteFailures"></a> Role_BulkDeleteFailures

One-To-Many Relationship: [role Role_BulkDeleteFailures](role.md#BKMK_Role_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`role`|
|ReferencedAttribute|`roleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_role`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_roleeditorlayout_BulkDeleteFailures"></a> roleeditorlayout_BulkDeleteFailures

One-To-Many Relationship: [roleeditorlayout roleeditorlayout_BulkDeleteFailures](roleeditorlayout.md#BKMK_roleeditorlayout_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`roleeditorlayout`|
|ReferencedAttribute|`roleeditorlayoutid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_roleeditorlayout`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sa_suggestedaction_BulkDeleteFailures"></a> sa_suggestedaction_BulkDeleteFailures

One-To-Many Relationship: [sa_suggestedaction sa_suggestedaction_BulkDeleteFailures](sa_suggestedaction.md#BKMK_sa_suggestedaction_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`sa_suggestedaction`|
|ReferencedAttribute|`sa_suggestedactionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sa_suggestedaction`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sa_suggestedactioncriteria_BulkDeleteFailures"></a> sa_suggestedactioncriteria_BulkDeleteFailures

One-To-Many Relationship: [sa_suggestedactioncriteria sa_suggestedactioncriteria_BulkDeleteFailures](sa_suggestedactioncriteria.md#BKMK_sa_suggestedactioncriteria_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`sa_suggestedactioncriteria`|
|ReferencedAttribute|`sa_suggestedactioncriteriaid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sa_suggestedactioncriteria`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SavedQuery_BulkDeleteFailures"></a> SavedQuery_BulkDeleteFailures

One-To-Many Relationship: [savedquery SavedQuery_BulkDeleteFailures](savedquery.md#BKMK_SavedQuery_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`savedquery`|
|ReferencedAttribute|`savedqueryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_savedquery`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_savingrule_BulkDeleteFailures"></a> savingrule_BulkDeleteFailures

One-To-Many Relationship: [savingrule savingrule_BulkDeleteFailures](savingrule.md#BKMK_savingrule_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`savingrule`|
|ReferencedAttribute|`savingruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_savingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchattributesettings_BulkDeleteFailures"></a> searchattributesettings_BulkDeleteFailures

One-To-Many Relationship: [searchattributesettings searchattributesettings_BulkDeleteFailures](searchattributesettings.md#BKMK_searchattributesettings_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`searchattributesettings`|
|ReferencedAttribute|`searchattributesettingsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_searchattributesettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchcustomanalyzer_BulkDeleteFailures"></a> searchcustomanalyzer_BulkDeleteFailures

One-To-Many Relationship: [searchcustomanalyzer searchcustomanalyzer_BulkDeleteFailures](searchcustomanalyzer.md#BKMK_searchcustomanalyzer_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`searchcustomanalyzer`|
|ReferencedAttribute|`searchcustomanalyzerid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_searchcustomanalyzer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchrelationshipsettings_BulkDeleteFailures"></a> searchrelationshipsettings_BulkDeleteFailures

One-To-Many Relationship: [searchrelationshipsettings searchrelationshipsettings_BulkDeleteFailures](searchrelationshipsettings.md#BKMK_searchrelationshipsettings_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`searchrelationshipsettings`|
|ReferencedAttribute|`searchrelationshipsettingsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_searchrelationshipsettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SemiAnnualFiscalCalendar_BulkDeleteFailures"></a> SemiAnnualFiscalCalendar_BulkDeleteFailures

One-To-Many Relationship: [semiannualfiscalcalendar SemiAnnualFiscalCalendar_BulkDeleteFailures](semiannualfiscalcalendar.md#BKMK_SemiAnnualFiscalCalendar_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`semiannualfiscalcalendar`|
|ReferencedAttribute|`userfiscalcalendarid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_semiannualfiscalcalendar`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sensitivitylabelattributemapping_BulkDeleteFailures"></a> sensitivitylabelattributemapping_BulkDeleteFailures

One-To-Many Relationship: [sensitivitylabelattributemapping sensitivitylabelattributemapping_BulkDeleteFailures](sensitivitylabelattributemapping.md#BKMK_sensitivitylabelattributemapping_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`sensitivitylabelattributemapping`|
|ReferencedAttribute|`sensitivitylabelattributemappingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sensitivitylabelattributemapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_serviceplan_BulkDeleteFailures"></a> serviceplan_BulkDeleteFailures

One-To-Many Relationship: [serviceplan serviceplan_BulkDeleteFailures](serviceplan.md#BKMK_serviceplan_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`serviceplan`|
|ReferencedAttribute|`serviceplanid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_serviceplan`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_serviceplanmapping_BulkDeleteFailures"></a> serviceplanmapping_BulkDeleteFailures

One-To-Many Relationship: [serviceplanmapping serviceplanmapping_BulkDeleteFailures](serviceplanmapping.md#BKMK_serviceplanmapping_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`serviceplanmapping`|
|ReferencedAttribute|`serviceplanmappingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_serviceplanmapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedlinksetting_BulkDeleteFailures"></a> sharedlinksetting_BulkDeleteFailures

One-To-Many Relationship: [sharedlinksetting sharedlinksetting_BulkDeleteFailures](sharedlinksetting.md#BKMK_sharedlinksetting_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedlinksetting`|
|ReferencedAttribute|`sharedlinksettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharedlinksetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedobject_BulkDeleteFailures"></a> sharedobject_BulkDeleteFailures

One-To-Many Relationship: [sharedobject sharedobject_BulkDeleteFailures](sharedobject.md#BKMK_sharedobject_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedobject`|
|ReferencedAttribute|`sharedobjectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharedobject`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedworkspace_BulkDeleteFailures"></a> sharedworkspace_BulkDeleteFailures

One-To-Many Relationship: [sharedworkspace sharedworkspace_BulkDeleteFailures](sharedworkspace.md#BKMK_sharedworkspace_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedworkspace`|
|ReferencedAttribute|`sharedworkspaceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharedworkspace`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedworkspacepool_BulkDeleteFailures"></a> sharedworkspacepool_BulkDeleteFailures

One-To-Many Relationship: [sharedworkspacepool sharedworkspacepool_BulkDeleteFailures](sharedworkspacepool.md#BKMK_sharedworkspacepool_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedworkspacepool`|
|ReferencedAttribute|`sharedworkspacepoolid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharedworkspacepool`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharepointmanagedidentity_BulkDeleteFailures"></a> sharepointmanagedidentity_BulkDeleteFailures

One-To-Many Relationship: [sharepointmanagedidentity sharepointmanagedidentity_BulkDeleteFailures](sharepointmanagedidentity.md#BKMK_sharepointmanagedidentity_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`sharepointmanagedidentity`|
|ReferencedAttribute|`sharepointmanagedidentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharepointmanagedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sideloadedaiplugin_BulkDeleteFailures"></a> sideloadedaiplugin_BulkDeleteFailures

One-To-Many Relationship: [sideloadedaiplugin sideloadedaiplugin_BulkDeleteFailures](sideloadedaiplugin.md#BKMK_sideloadedaiplugin_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`sideloadedaiplugin`|
|ReferencedAttribute|`sideloadedaipluginid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sideloadedaiplugin`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_slabase_BulkDeleteFailures"></a> slabase_BulkDeleteFailures

One-To-Many Relationship: [sla slabase_BulkDeleteFailures](sla.md#BKMK_slabase_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`sla`|
|ReferencedAttribute|`slaid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sla`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SocialActivity_BulkDeleteFailures"></a> SocialActivity_BulkDeleteFailures

One-To-Many Relationship: [socialactivity SocialActivity_BulkDeleteFailures](socialactivity.md#BKMK_SocialActivity_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`socialactivity`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_socialactivity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentattributeconfiguration_BulkDeleteFailures"></a> solutioncomponentattributeconfiguration_BulkDeleteFailures

One-To-Many Relationship: [solutioncomponentattributeconfiguration solutioncomponentattributeconfiguration_BulkDeleteFailures](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentattributeconfiguration`|
|ReferencedAttribute|`solutioncomponentattributeconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_solutioncomponentattributeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentbatchconfiguration_BulkDeleteFailures"></a> solutioncomponentbatchconfiguration_BulkDeleteFailures

One-To-Many Relationship: [solutioncomponentbatchconfiguration solutioncomponentbatchconfiguration_BulkDeleteFailures](solutioncomponentbatchconfiguration.md#BKMK_solutioncomponentbatchconfiguration_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentbatchconfiguration`|
|ReferencedAttribute|`solutioncomponentbatchconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_solutioncomponentbatchconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentconfiguration_BulkDeleteFailures"></a> solutioncomponentconfiguration_BulkDeleteFailures

One-To-Many Relationship: [solutioncomponentconfiguration solutioncomponentconfiguration_BulkDeleteFailures](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentconfiguration`|
|ReferencedAttribute|`solutioncomponentconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_solutioncomponentconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentrelationshipconfiguration_BulkDeleteFailures"></a> solutioncomponentrelationshipconfiguration_BulkDeleteFailures

One-To-Many Relationship: [solutioncomponentrelationshipconfiguration solutioncomponentrelationshipconfiguration_BulkDeleteFailures](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentrelationshipconfiguration`|
|ReferencedAttribute|`solutioncomponentrelationshipconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_solutioncomponentrelationshipconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagedentity_BulkDeleteFailures"></a> stagedentity_BulkDeleteFailures

One-To-Many Relationship: [stagedentity stagedentity_BulkDeleteFailures](stagedentity.md#BKMK_stagedentity_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`stagedentity`|
|ReferencedAttribute|`stagedentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_stagedentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagedentityattribute_BulkDeleteFailures"></a> stagedentityattribute_BulkDeleteFailures

One-To-Many Relationship: [stagedentityattribute stagedentityattribute_BulkDeleteFailures](stagedentityattribute.md#BKMK_stagedentityattribute_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`stagedentityattribute`|
|ReferencedAttribute|`stagedentityattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_stagedentityattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagedmetadataasyncoperation_BulkDeleteFailures"></a> stagedmetadataasyncoperation_BulkDeleteFailures

One-To-Many Relationship: [stagedmetadataasyncoperation stagedmetadataasyncoperation_BulkDeleteFailures](stagedmetadataasyncoperation.md#BKMK_stagedmetadataasyncoperation_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`stagedmetadataasyncoperation`|
|ReferencedAttribute|`stagedmetadataasyncoperationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_stagedmetadataasyncoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagesolutionupload_BulkDeleteFailures"></a> stagesolutionupload_BulkDeleteFailures

One-To-Many Relationship: [stagesolutionupload stagesolutionupload_BulkDeleteFailures](stagesolutionupload.md#BKMK_stagesolutionupload_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`stagesolutionupload`|
|ReferencedAttribute|`stagesolutionuploadid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_stagesolutionupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Subject_BulkDeleteFailures"></a> Subject_BulkDeleteFailures

One-To-Many Relationship: [subject Subject_BulkDeleteFailures](subject.md#BKMK_Subject_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`subject`|
|ReferencedAttribute|`subjectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_subject`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_supportusertable_BulkDeleteFailures"></a> supportusertable_BulkDeleteFailures

One-To-Many Relationship: [supportusertable supportusertable_BulkDeleteFailures](supportusertable.md#BKMK_supportusertable_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`supportusertable`|
|ReferencedAttribute|`supportusertableid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_supportusertable`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapsedatabase_BulkDeleteFailures"></a> synapsedatabase_BulkDeleteFailures

One-To-Many Relationship: [synapsedatabase synapsedatabase_BulkDeleteFailures](synapsedatabase.md#BKMK_synapsedatabase_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`synapsedatabase`|
|ReferencedAttribute|`synapsedatabaseid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapsedatabase`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkexternaltablestate_BulkDeleteFailures"></a> synapselinkexternaltablestate_BulkDeleteFailures

One-To-Many Relationship: [synapselinkexternaltablestate synapselinkexternaltablestate_BulkDeleteFailures](synapselinkexternaltablestate.md#BKMK_synapselinkexternaltablestate_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkexternaltablestate`|
|ReferencedAttribute|`synapselinkexternaltablestateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkexternaltablestate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofile_BulkDeleteFailures"></a> synapselinkprofile_BulkDeleteFailures

One-To-Many Relationship: [synapselinkprofile synapselinkprofile_BulkDeleteFailures](synapselinkprofile.md#BKMK_synapselinkprofile_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofile`|
|ReferencedAttribute|`synapselinkprofileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofileentity_BulkDeleteFailures"></a> synapselinkprofileentity_BulkDeleteFailures

One-To-Many Relationship: [synapselinkprofileentity synapselinkprofileentity_BulkDeleteFailures](synapselinkprofileentity.md#BKMK_synapselinkprofileentity_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofileentity`|
|ReferencedAttribute|`synapselinkprofileentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkprofileentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofileentitystate_BulkDeleteFailures"></a> synapselinkprofileentitystate_BulkDeleteFailures

One-To-Many Relationship: [synapselinkprofileentitystate synapselinkprofileentitystate_BulkDeleteFailures](synapselinkprofileentitystate.md#BKMK_synapselinkprofileentitystate_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofileentitystate`|
|ReferencedAttribute|`synapselinkprofileentitystateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkprofileentitystate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkschedule_BulkDeleteFailures"></a> synapselinkschedule_BulkDeleteFailures

One-To-Many Relationship: [synapselinkschedule synapselinkschedule_BulkDeleteFailures](synapselinkschedule.md#BKMK_synapselinkschedule_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkschedule`|
|ReferencedAttribute|`synapselinkscheduleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkschedule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SystemForm_BulkDeleteFailures"></a> SystemForm_BulkDeleteFailures

One-To-Many Relationship: [systemform SystemForm_BulkDeleteFailures](systemform.md#BKMK_SystemForm_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`systemform`|
|ReferencedAttribute|`formid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_systemform`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SystemUser_BulkDeleteFailures"></a> SystemUser_BulkDeleteFailures

One-To-Many Relationship: [systemuser SystemUser_BulkDeleteFailures](systemuser.md#BKMK_SystemUser_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_systemuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_systemuserauthorizationchangetracker_BulkDeleteFailures"></a> systemuserauthorizationchangetracker_BulkDeleteFailures

One-To-Many Relationship: [systemuserauthorizationchangetracker systemuserauthorizationchangetracker_BulkDeleteFailures](systemuserauthorizationchangetracker.md#BKMK_systemuserauthorizationchangetracker_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuserauthorizationchangetracker`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_systemuserauthorizationchangetracker`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_tag_BulkDeleteFailures"></a> tag_BulkDeleteFailures

One-To-Many Relationship: [tag tag_BulkDeleteFailures](tag.md#BKMK_tag_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`tag`|
|ReferencedAttribute|`tagid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_tag`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_taggedflowsession_BulkDeleteFailures"></a> taggedflowsession_BulkDeleteFailures

One-To-Many Relationship: [taggedflowsession taggedflowsession_BulkDeleteFailures](taggedflowsession.md#BKMK_taggedflowsession_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`taggedflowsession`|
|ReferencedAttribute|`taggedflowsessionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_taggedflowsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_taggedprocess_BulkDeleteFailures"></a> taggedprocess_BulkDeleteFailures

One-To-Many Relationship: [taggedprocess taggedprocess_BulkDeleteFailures](taggedprocess.md#BKMK_taggedprocess_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`taggedprocess`|
|ReferencedAttribute|`taggedprocessid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_taggedprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Task_BulkDeleteFailures"></a> Task_BulkDeleteFailures

One-To-Many Relationship: [task Task_BulkDeleteFailures](task.md#BKMK_Task_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`task`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_task`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Team_BulkDeleteFailures"></a> Team_BulkDeleteFailures

One-To-Many Relationship: [team Team_BulkDeleteFailures](team.md#BKMK_Team_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_team`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_teammobileofflineprofilemembership_BulkDeleteFailures"></a> teammobileofflineprofilemembership_BulkDeleteFailures

One-To-Many Relationship: [teammobileofflineprofilemembership teammobileofflineprofilemembership_BulkDeleteFailures](teammobileofflineprofilemembership.md#BKMK_teammobileofflineprofilemembership_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`teammobileofflineprofilemembership`|
|ReferencedAttribute|`teammobileofflineprofilemembershipid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_teammobileofflineprofilemembership`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Template_BulkDeleteFailures"></a> Template_BulkDeleteFailures

One-To-Many Relationship: [template Template_BulkDeleteFailures](template.md#BKMK_Template_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`template`|
|ReferencedAttribute|`templateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_template`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Territory_BulkDeleteFailures"></a> Territory_BulkDeleteFailures

One-To-Many Relationship: [territory Territory_BulkDeleteFailures](territory.md#BKMK_Territory_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`territory`|
|ReferencedAttribute|`territoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_territory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_theme_BulkDeleteFailures"></a> theme_BulkDeleteFailures

One-To-Many Relationship: [theme theme_BulkDeleteFailures](theme.md#BKMK_theme_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`theme`|
|ReferencedAttribute|`themeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_theme`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_unstructuredfilesearchentity_BulkDeleteFailures"></a> unstructuredfilesearchentity_BulkDeleteFailures

One-To-Many Relationship: [unstructuredfilesearchentity unstructuredfilesearchentity_BulkDeleteFailures](unstructuredfilesearchentity.md#BKMK_unstructuredfilesearchentity_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`unstructuredfilesearchentity`|
|ReferencedAttribute|`unstructuredfilesearchentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_unstructuredfilesearchentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_unstructuredfilesearchrecord_BulkDeleteFailures"></a> unstructuredfilesearchrecord_BulkDeleteFailures

One-To-Many Relationship: [unstructuredfilesearchrecord unstructuredfilesearchrecord_BulkDeleteFailures](unstructuredfilesearchrecord.md#BKMK_unstructuredfilesearchrecord_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`unstructuredfilesearchrecord`|
|ReferencedAttribute|`unstructuredfilesearchrecordid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_unstructuredfilesearchrecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_UserForm_BulkDeleteFailures"></a> UserForm_BulkDeleteFailures

One-To-Many Relationship: [userform UserForm_BulkDeleteFailures](userform.md#BKMK_UserForm_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`userform`|
|ReferencedAttribute|`userformid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_userform`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_usermapping_BulkDeleteFailures"></a> usermapping_BulkDeleteFailures

One-To-Many Relationship: [usermapping usermapping_BulkDeleteFailures](usermapping.md#BKMK_usermapping_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`usermapping`|
|ReferencedAttribute|`usermappingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_usermapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_usermobileofflineprofilemembership_BulkDeleteFailures"></a> usermobileofflineprofilemembership_BulkDeleteFailures

One-To-Many Relationship: [usermobileofflineprofilemembership usermobileofflineprofilemembership_BulkDeleteFailures](usermobileofflineprofilemembership.md#BKMK_usermobileofflineprofilemembership_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`usermobileofflineprofilemembership`|
|ReferencedAttribute|`usermobileofflineprofilemembershipid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_usermobileofflineprofilemembership`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_UserQuery_BulkDeleteFailures"></a> UserQuery_BulkDeleteFailures

One-To-Many Relationship: [userquery UserQuery_BulkDeleteFailures](userquery.md#BKMK_UserQuery_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`userquery`|
|ReferencedAttribute|`userqueryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_userquery`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_userrating_BulkDeleteFailures"></a> userrating_BulkDeleteFailures

One-To-Many Relationship: [userrating userrating_BulkDeleteFailures](userrating.md#BKMK_userrating_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`userrating`|
|ReferencedAttribute|`userratingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_userrating`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_viewasexamplequestion_BulkDeleteFailures"></a> viewasexamplequestion_BulkDeleteFailures

One-To-Many Relationship: [viewasexamplequestion viewasexamplequestion_BulkDeleteFailures](viewasexamplequestion.md#BKMK_viewasexamplequestion_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`viewasexamplequestion`|
|ReferencedAttribute|`viewasexamplequestionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_viewasexamplequestion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_virtualentitymetadata_BulkDeleteFailures"></a> virtualentitymetadata_BulkDeleteFailures

One-To-Many Relationship: [virtualentitymetadata virtualentitymetadata_BulkDeleteFailures](virtualentitymetadata.md#BKMK_virtualentitymetadata_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`virtualentitymetadata`|
|ReferencedAttribute|`virtualentitymetadataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_virtualentitymetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflowbinary_BulkDeleteFailures"></a> workflowbinary_BulkDeleteFailures

One-To-Many Relationship: [workflowbinary workflowbinary_BulkDeleteFailures](workflowbinary.md#BKMK_workflowbinary_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`workflowbinary`|
|ReferencedAttribute|`workflowbinaryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_workflowbinary`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflowmetadata_BulkDeleteFailures"></a> workflowmetadata_BulkDeleteFailures

One-To-Many Relationship: [workflowmetadata workflowmetadata_BulkDeleteFailures](workflowmetadata.md#BKMK_workflowmetadata_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`workflowmetadata`|
|ReferencedAttribute|`workflowmetadataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_workflowmetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workqueue_BulkDeleteFailures"></a> workqueue_BulkDeleteFailures

One-To-Many Relationship: [workqueue workqueue_BulkDeleteFailures](workqueue.md#BKMK_workqueue_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`workqueue`|
|ReferencedAttribute|`workqueueid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_workqueue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workqueueitem_BulkDeleteFailures"></a> workqueueitem_BulkDeleteFailures

One-To-Many Relationship: [workqueueitem workqueueitem_BulkDeleteFailures](workqueueitem.md#BKMK_workqueueitem_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencedEntity|`workqueueitem`|
|ReferencedAttribute|`workqueueitemid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_workqueueitem`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.bulkdeletefailure?displayProperty=fullName>
