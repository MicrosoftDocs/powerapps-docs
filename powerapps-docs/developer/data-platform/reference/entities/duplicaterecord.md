---
title: "Duplicate Record (DuplicateRecord) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Duplicate Record (DuplicateRecord) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Duplicate Record (DuplicateRecord) table/entity reference (Microsoft Dataverse)

Potential duplicate record.

## Messages

The following table lists the messages for the Duplicate Record (DuplicateRecord) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /duplicaterecords(*duplicateid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /duplicaterecords<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Duplicate Record (DuplicateRecord) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Duplicate Record** |
| **DisplayCollectionName** | **Duplicate Records** |
| **SchemaName** | `DuplicateRecord` |
| **CollectionSchemaName** | `DuplicateRecords` |
| **EntitySetName** | `duplicaterecords`|
| **LogicalName** | `duplicaterecord` |
| **LogicalCollectionName** | `duplicaterecords` |
| **PrimaryIdAttribute** | `duplicateid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

### <a name="BKMK_DuplicateId"></a> DuplicateId

|Property|Value|
|---|---|
|Description|**Unique identifier of the duplicate record.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`duplicateid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [AsyncOperationId](#BKMK_AsyncOperationId)
- [BaseRecordId](#BKMK_BaseRecordId)
- [BaseRecordIdTypeCode](#BKMK_BaseRecordIdTypeCode)
- [CreatedOn](#BKMK_CreatedOn)
- [DuplicateRecordId](#BKMK_DuplicateRecordId)
- [DuplicateRecordIdTypeCode](#BKMK_DuplicateRecordIdTypeCode)
- [DuplicateRuleId](#BKMK_DuplicateRuleId)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningUser](#BKMK_OwningUser)

### <a name="BKMK_AsyncOperationId"></a> AsyncOperationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the system job that created this record.**|
|DisplayName|**System Job**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`asyncoperationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|asyncoperation|

### <a name="BKMK_BaseRecordId"></a> BaseRecordId

|Property|Value|
|---|---|
|Description|**Unique identifier of the base record.**|
|DisplayName|**Base Record ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`baserecordid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account, activityfileattachment, adx_invitation, adx_inviteredemption, aicopilot, aipluginauth, aipluginoperationparameter, aipluginoperationresponsetemplate, aiplugintitle, aipluginusersetting, applicationuser, appointment, approvalprocess, approvalstageapproval, approvalstagecondition, approvalstageintelligent, approvalstageorder, archivecleanupinfo, archivecleanupoperation, bulkarchiveconfig, bulkarchivefailuredetail, bulkarchiveoperation, businessprocess, canvasappextendedmetadata, card, cascadegrantrevokeaccessrecordstracker, cascadegrantrevokeaccessversiontracker, catalogassignment, certificatecredential, channelaccessprofile, connectioninstance, connector, contact, conversationtranscript, credential, datalakefolder, datalakefolderpermission, datalakeworkspace, datalakeworkspacepermission, dataprocessingconfiguration, deleteditemreference, desktopflowmodule, email, emailserverprofile, enablearchivalrequest, entityrecordfilter, environmentvariabledefinition, environmentvariablevalue, exportedexcel, exportsolutionupload, fax, featurecontrolsetting, federatedknowledgecitation, federatedknowledgemetadatarefresh, feedback, flowcredentialapplication, flowevent, flowmachinegroup, flowmachineimage, flowmachineimageversion, flowmachinenetwork, flowsessionbinary, fxexpression, goal, goalrollupquery, governanceconfiguration, kbarticle, keyvaultreference, knowledgearticle, knowledgebaserecord, knowledgesourceconsumer, knowledgesourceprofile, letter, managedidentity, maskingrule, msdyn_aibdataset, msdyn_aibdatasetfile, msdyn_aibdatasetrecord, msdyn_aibdatasetscontainer, msdyn_aibfeedbackloop, msdyn_aibfile, msdyn_aibfileattacheddata, msdyn_aiconfigurationsearch, msdyn_aievent, msdyn_aimodelcatalog, msdyn_aiodimage, msdyn_aiodlabel, msdyn_aiodtrainingboundingbox, msdyn_aiodtrainingimage, msdyn_aioptimization, msdyn_aioptimizationprivatedata, msdyn_aitestrunbatch, msdyn_analysiscomponent, msdyn_analysisjob, msdyn_analysisoverride, msdyn_analysisresult, msdyn_analysisresultdetail, msdyn_appinsightsmetadata, msdyn_copilotinteractions, msdyn_customcontrolextendedsettings, msdyn_dataflow, msdyn_dataflowconnectionreference, msdyn_dataflowrefreshhistory, msdyn_dataflow_datalakefolder, msdyn_dmsrequest, msdyn_dmsrequeststatus, msdyn_entitylinkchatconfiguration, msdyn_entityrefreshhistory, msdyn_favoriteknowledgearticle, msdyn_federatedarticle, msdyn_federatedarticleincident, msdyn_fileupload, msdyn_flow_actionapprovalmodel, msdyn_flow_approval, msdyn_flow_approvalrequest, msdyn_flow_approvalresponse, msdyn_flow_approvalstep, msdyn_flow_awaitallactionapprovalmodel, msdyn_flow_awaitallapprovalmodel, msdyn_flow_basicapprovalmodel, msdyn_flow_flowapproval, msdyn_formmapping, msdyn_function, msdyn_integratedsearchprovider, msdyn_kalanguagesetting, msdyn_kbattachment, msdyn_kmfederatedsearchconfig, msdyn_knowledgearticleimage, msdyn_knowledgearticletemplate, msdyn_knowledgeconfiguration, msdyn_knowledgeinteractioninsight, msdyn_knowledgemanagementsetting, msdyn_knowledgepersonalfilter, msdyn_knowledgesearchfilter, msdyn_knowledgesearchinsight, msdyn_mobileapp, msdyn_modulerundetail, msdyn_pmanalysishistory, msdyn_pmbusinessruleautomationconfig, msdyn_pmcalendar, msdyn_pmcalendarversion, msdyn_pminferredtask, msdyn_pmprocessextendedmetadataversion, msdyn_pmprocesstemplate, msdyn_pmprocessusersettings, msdyn_pmprocessversion, msdyn_pmrecording, msdyn_pmsimulation, msdyn_pmtab, msdyn_pmtemplate, msdyn_pmview, msdyn_qna, msdyn_schedule, msdyn_serviceconfiguration, msdyn_slakpi, msdyn_solutionhealthrule, msdyn_solutionhealthruleargument, msdyn_solutionhealthruleset, msdyn_virtualtablecolumncandidate, mspcat_catalogsubmissionfiles, mspcat_packagestore, organizationdatasyncfnostate, organizationdatasyncstate, organizationdatasyncsubscription, organizationdatasyncsubscriptionentity, organizationdatasyncsubscriptionfnotable, package, packagehistory, phonecall, powerbidataset, powerbidatasetapdx, powerbimashupparameter, powerbireport, powerbireportapdx, powerfxrule, powerpagesddosalert, powerpagesmanagedidentity, powerpagesscanreport, privilegesremovalsetting, publisher, purviewlabelinfo, purviewlabelsynccache, queue, reconciliationinfo, recordfilter, recurringappointmentmaster, reportparameter, retaineddataexcel, retentioncleanupinfo, retentioncleanupoperation, retentionconfig, retentionfailuredetail, retentionoperation, retentionsuccessdetail, revokeinheritedaccessrecordstracker, roleeditorlayout, savingrule, searchattributesettings, searchcustomanalyzer, searchrelationshipsettings, sensitivitylabelattributemapping, serviceplan, serviceplancustomcontrol, serviceplanmapping, sharedlinksetting, sharepointdocumentlocation, sharepointsite, socialactivity, socialprofile, solutioncomponentattributeconfiguration, solutioncomponentbatchconfiguration, solutioncomponentconfiguration, solutioncomponentrelationshipconfiguration, stagesolutionupload, supportusertable, synapsedatabase, synapselinkexternaltablestate, synapselinkprofile, synapselinkprofileentity, synapselinkprofileentitystate, synapselinkschedule, systemuser, task, tdsmetadata, team, transactioncurrency, unstructuredfilesearchentity, unstructuredfilesearchrecord, userrating, workflowmetadata, workqueue, workqueueitem|

### <a name="BKMK_BaseRecordIdTypeCode"></a> BaseRecordIdTypeCode

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`baserecordidtypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the duplicate record was created.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_DuplicateRecordId"></a> DuplicateRecordId

|Property|Value|
|---|---|
|Description|**Unique identifier of the potential duplicate record.**|
|DisplayName|**Duplicate Record ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`duplicaterecordid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account, activityfileattachment, adx_invitation, adx_inviteredemption, aicopilot, aipluginauth, aipluginoperationparameter, aipluginoperationresponsetemplate, aiplugintitle, aipluginusersetting, applicationuser, appointment, approvalprocess, approvalstageapproval, approvalstagecondition, approvalstageintelligent, approvalstageorder, archivecleanupinfo, archivecleanupoperation, bulkarchiveconfig, bulkarchivefailuredetail, bulkarchiveoperation, businessprocess, canvasappextendedmetadata, card, cascadegrantrevokeaccessrecordstracker, cascadegrantrevokeaccessversiontracker, catalogassignment, certificatecredential, channelaccessprofile, connectioninstance, connector, contact, conversationtranscript, credential, datalakefolder, datalakefolderpermission, datalakeworkspace, datalakeworkspacepermission, dataprocessingconfiguration, deleteditemreference, desktopflowmodule, email, emailserverprofile, enablearchivalrequest, entityrecordfilter, environmentvariabledefinition, environmentvariablevalue, exportedexcel, exportsolutionupload, fax, featurecontrolsetting, federatedknowledgecitation, federatedknowledgemetadatarefresh, feedback, flowcredentialapplication, flowevent, flowmachinegroup, flowmachineimage, flowmachineimageversion, flowmachinenetwork, flowsessionbinary, fxexpression, goal, goalrollupquery, governanceconfiguration, kbarticle, keyvaultreference, knowledgearticle, knowledgebaserecord, knowledgesourceconsumer, knowledgesourceprofile, letter, managedidentity, maskingrule, msdyn_aibdataset, msdyn_aibdatasetfile, msdyn_aibdatasetrecord, msdyn_aibdatasetscontainer, msdyn_aibfeedbackloop, msdyn_aibfile, msdyn_aibfileattacheddata, msdyn_aiconfigurationsearch, msdyn_aievent, msdyn_aimodelcatalog, msdyn_aiodimage, msdyn_aiodlabel, msdyn_aiodtrainingboundingbox, msdyn_aiodtrainingimage, msdyn_aioptimization, msdyn_aioptimizationprivatedata, msdyn_aitestrunbatch, msdyn_analysiscomponent, msdyn_analysisjob, msdyn_analysisoverride, msdyn_analysisresult, msdyn_analysisresultdetail, msdyn_appinsightsmetadata, msdyn_copilotinteractions, msdyn_customcontrolextendedsettings, msdyn_dataflow, msdyn_dataflowconnectionreference, msdyn_dataflowrefreshhistory, msdyn_dataflow_datalakefolder, msdyn_dmsrequest, msdyn_dmsrequeststatus, msdyn_entitylinkchatconfiguration, msdyn_entityrefreshhistory, msdyn_favoriteknowledgearticle, msdyn_federatedarticle, msdyn_federatedarticleincident, msdyn_fileupload, msdyn_flow_actionapprovalmodel, msdyn_flow_approval, msdyn_flow_approvalrequest, msdyn_flow_approvalresponse, msdyn_flow_approvalstep, msdyn_flow_awaitallactionapprovalmodel, msdyn_flow_awaitallapprovalmodel, msdyn_flow_basicapprovalmodel, msdyn_flow_flowapproval, msdyn_formmapping, msdyn_function, msdyn_integratedsearchprovider, msdyn_kalanguagesetting, msdyn_kbattachment, msdyn_kmfederatedsearchconfig, msdyn_knowledgearticleimage, msdyn_knowledgearticletemplate, msdyn_knowledgeconfiguration, msdyn_knowledgeinteractioninsight, msdyn_knowledgemanagementsetting, msdyn_knowledgepersonalfilter, msdyn_knowledgesearchfilter, msdyn_knowledgesearchinsight, msdyn_mobileapp, msdyn_modulerundetail, msdyn_pmanalysishistory, msdyn_pmbusinessruleautomationconfig, msdyn_pmcalendar, msdyn_pmcalendarversion, msdyn_pminferredtask, msdyn_pmprocessextendedmetadataversion, msdyn_pmprocesstemplate, msdyn_pmprocessusersettings, msdyn_pmprocessversion, msdyn_pmrecording, msdyn_pmsimulation, msdyn_pmtab, msdyn_pmtemplate, msdyn_pmview, msdyn_qna, msdyn_schedule, msdyn_serviceconfiguration, msdyn_slakpi, msdyn_solutionhealthrule, msdyn_solutionhealthruleargument, msdyn_solutionhealthruleset, msdyn_virtualtablecolumncandidate, mspcat_catalogsubmissionfiles, mspcat_packagestore, organizationdatasyncfnostate, organizationdatasyncstate, organizationdatasyncsubscription, organizationdatasyncsubscriptionentity, organizationdatasyncsubscriptionfnotable, package, packagehistory, phonecall, powerbidataset, powerbidatasetapdx, powerbimashupparameter, powerbireport, powerbireportapdx, powerfxrule, powerpagesddosalert, powerpagesmanagedidentity, powerpagesscanreport, privilegesremovalsetting, publisher, purviewlabelinfo, purviewlabelsynccache, queue, reconciliationinfo, recordfilter, recurringappointmentmaster, reportparameter, retaineddataexcel, retentioncleanupinfo, retentioncleanupoperation, retentionconfig, retentionfailuredetail, retentionoperation, retentionsuccessdetail, revokeinheritedaccessrecordstracker, roleeditorlayout, savingrule, searchattributesettings, searchcustomanalyzer, searchrelationshipsettings, sensitivitylabelattributemapping, serviceplan, serviceplancustomcontrol, serviceplanmapping, sharedlinksetting, sharepointdocumentlocation, sharepointsite, socialactivity, socialprofile, solutioncomponentattributeconfiguration, solutioncomponentbatchconfiguration, solutioncomponentconfiguration, solutioncomponentrelationshipconfiguration, stagesolutionupload, supportusertable, synapsedatabase, synapselinkexternaltablestate, synapselinkprofile, synapselinkprofileentity, synapselinkprofileentitystate, synapselinkschedule, systemuser, task, tdsmetadata, team, transactioncurrency, unstructuredfilesearchentity, unstructuredfilesearchrecord, userrating, workflowmetadata, workqueue, workqueueitem|

### <a name="BKMK_DuplicateRecordIdTypeCode"></a> DuplicateRecordIdTypeCode

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`duplicaterecordidtypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_DuplicateRuleId"></a> DuplicateRuleId

|Property|Value|
|---|---|
|Description|**Unique identifier of the duplicate rule against which this duplicate was found.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`duplicateruleid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|duplicaterule|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user or team who owns the duplicate record.**|
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
|Description|**Unique identifier of the business unit that owns the duplicate record.**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who owns the duplicate record.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [Account_DuplicateBaseRecord](#BKMK_Account_DuplicateBaseRecord)
- [Account_DuplicateMatchingRecord](#BKMK_Account_DuplicateMatchingRecord)
- [activityfileattachment_DuplicateBaseRecord](#BKMK_activityfileattachment_DuplicateBaseRecord)
- [activityfileattachment_DuplicateMatchingRecord](#BKMK_activityfileattachment_DuplicateMatchingRecord)
- [adx_invitation_DuplicateBaseRecord](#BKMK_adx_invitation_DuplicateBaseRecord)
- [adx_invitation_DuplicateMatchingRecord](#BKMK_adx_invitation_DuplicateMatchingRecord)
- [adx_inviteredemption_DuplicateBaseRecord](#BKMK_adx_inviteredemption_DuplicateBaseRecord)
- [adx_inviteredemption_DuplicateMatchingRecord](#BKMK_adx_inviteredemption_DuplicateMatchingRecord)
- [aicopilot_DuplicateBaseRecord](#BKMK_aicopilot_DuplicateBaseRecord)
- [aicopilot_DuplicateMatchingRecord](#BKMK_aicopilot_DuplicateMatchingRecord)
- [aipluginauth_DuplicateBaseRecord](#BKMK_aipluginauth_DuplicateBaseRecord)
- [aipluginauth_DuplicateMatchingRecord](#BKMK_aipluginauth_DuplicateMatchingRecord)
- [aipluginoperationparameter_DuplicateBaseRecord](#BKMK_aipluginoperationparameter_DuplicateBaseRecord)
- [aipluginoperationparameter_DuplicateMatchingRecord](#BKMK_aipluginoperationparameter_DuplicateMatchingRecord)
- [aipluginoperationresponsetemplate_DuplicateBaseRecord](#BKMK_aipluginoperationresponsetemplate_DuplicateBaseRecord)
- [aipluginoperationresponsetemplate_DuplicateMatchingRecord](#BKMK_aipluginoperationresponsetemplate_DuplicateMatchingRecord)
- [aiplugintitle_DuplicateBaseRecord](#BKMK_aiplugintitle_DuplicateBaseRecord)
- [aiplugintitle_DuplicateMatchingRecord](#BKMK_aiplugintitle_DuplicateMatchingRecord)
- [aipluginusersetting_DuplicateBaseRecord](#BKMK_aipluginusersetting_DuplicateBaseRecord)
- [aipluginusersetting_DuplicateMatchingRecord](#BKMK_aipluginusersetting_DuplicateMatchingRecord)
- [applicationuser_DuplicateBaseRecord](#BKMK_applicationuser_DuplicateBaseRecord)
- [applicationuser_DuplicateMatchingRecord](#BKMK_applicationuser_DuplicateMatchingRecord)
- [Appointment_DuplicateBaseRecord](#BKMK_Appointment_DuplicateBaseRecord)
- [Appointment_DuplicateMatchingRecord](#BKMK_Appointment_DuplicateMatchingRecord)
- [approvalprocess_DuplicateBaseRecord](#BKMK_approvalprocess_DuplicateBaseRecord)
- [approvalprocess_DuplicateMatchingRecord](#BKMK_approvalprocess_DuplicateMatchingRecord)
- [approvalstageapproval_DuplicateBaseRecord](#BKMK_approvalstageapproval_DuplicateBaseRecord)
- [approvalstageapproval_DuplicateMatchingRecord](#BKMK_approvalstageapproval_DuplicateMatchingRecord)
- [approvalstagecondition_DuplicateBaseRecord](#BKMK_approvalstagecondition_DuplicateBaseRecord)
- [approvalstagecondition_DuplicateMatchingRecord](#BKMK_approvalstagecondition_DuplicateMatchingRecord)
- [approvalstageintelligent_DuplicateBaseRecord](#BKMK_approvalstageintelligent_DuplicateBaseRecord)
- [approvalstageintelligent_DuplicateMatchingRecord](#BKMK_approvalstageintelligent_DuplicateMatchingRecord)
- [approvalstageorder_DuplicateBaseRecord](#BKMK_approvalstageorder_DuplicateBaseRecord)
- [approvalstageorder_DuplicateMatchingRecord](#BKMK_approvalstageorder_DuplicateMatchingRecord)
- [AsyncOperation_DuplicateBaseRecord](#BKMK_AsyncOperation_DuplicateBaseRecord)
- [businessprocess_DuplicateBaseRecord](#BKMK_businessprocess_DuplicateBaseRecord)
- [businessprocess_DuplicateMatchingRecord](#BKMK_businessprocess_DuplicateMatchingRecord)
- [card_DuplicateBaseRecord](#BKMK_card_DuplicateBaseRecord)
- [card_DuplicateMatchingRecord](#BKMK_card_DuplicateMatchingRecord)
- [catalogassignment_DuplicateBaseRecord](#BKMK_catalogassignment_DuplicateBaseRecord)
- [catalogassignment_DuplicateMatchingRecord](#BKMK_catalogassignment_DuplicateMatchingRecord)
- [certificatecredential_DuplicateBaseRecord](#BKMK_certificatecredential_DuplicateBaseRecord)
- [certificatecredential_DuplicateMatchingRecord](#BKMK_certificatecredential_DuplicateMatchingRecord)
- [connectioninstance_DuplicateBaseRecord](#BKMK_connectioninstance_DuplicateBaseRecord)
- [connectioninstance_DuplicateMatchingRecord](#BKMK_connectioninstance_DuplicateMatchingRecord)
- [connector_DuplicateBaseRecord](#BKMK_connector_DuplicateBaseRecord)
- [connector_DuplicateMatchingRecord](#BKMK_connector_DuplicateMatchingRecord)
- [Contact_DuplicateBaseRecord](#BKMK_Contact_DuplicateBaseRecord)
- [Contact_DuplicateMatchingRecord](#BKMK_Contact_DuplicateMatchingRecord)
- [conversationtranscript_DuplicateBaseRecord](#BKMK_conversationtranscript_DuplicateBaseRecord)
- [conversationtranscript_DuplicateMatchingRecord](#BKMK_conversationtranscript_DuplicateMatchingRecord)
- [credential_DuplicateBaseRecord](#BKMK_credential_DuplicateBaseRecord)
- [credential_DuplicateMatchingRecord](#BKMK_credential_DuplicateMatchingRecord)
- [datalakefolder_DuplicateBaseRecord](#BKMK_datalakefolder_DuplicateBaseRecord)
- [datalakefolder_DuplicateMatchingRecord](#BKMK_datalakefolder_DuplicateMatchingRecord)
- [datalakefolderpermission_DuplicateBaseRecord](#BKMK_datalakefolderpermission_DuplicateBaseRecord)
- [datalakefolderpermission_DuplicateMatchingRecord](#BKMK_datalakefolderpermission_DuplicateMatchingRecord)
- [datalakeworkspace_DuplicateBaseRecord](#BKMK_datalakeworkspace_DuplicateBaseRecord)
- [datalakeworkspace_DuplicateMatchingRecord](#BKMK_datalakeworkspace_DuplicateMatchingRecord)
- [datalakeworkspacepermission_DuplicateBaseRecord](#BKMK_datalakeworkspacepermission_DuplicateBaseRecord)
- [datalakeworkspacepermission_DuplicateMatchingRecord](#BKMK_datalakeworkspacepermission_DuplicateMatchingRecord)
- [dataprocessingconfiguration_DuplicateBaseRecord](#BKMK_dataprocessingconfiguration_DuplicateBaseRecord)
- [dataprocessingconfiguration_DuplicateMatchingRecord](#BKMK_dataprocessingconfiguration_DuplicateMatchingRecord)
- [desktopflowmodule_DuplicateBaseRecord](#BKMK_desktopflowmodule_DuplicateBaseRecord)
- [desktopflowmodule_DuplicateMatchingRecord](#BKMK_desktopflowmodule_DuplicateMatchingRecord)
- [DuplicateRule_DuplicateBaseRecord](#BKMK_DuplicateRule_DuplicateBaseRecord)
- [Email_DuplicateBaseRecord](#BKMK_Email_DuplicateBaseRecord)
- [Email_DuplicateMatchingRecord](#BKMK_Email_DuplicateMatchingRecord)
- [emailserverprofile_duplicatebaserecord](#BKMK_emailserverprofile_duplicatebaserecord)
- [emailserverprofile_duplicatematchingrecord](#BKMK_emailserverprofile_duplicatematchingrecord)
- [entityrecordfilter_DuplicateBaseRecord](#BKMK_entityrecordfilter_DuplicateBaseRecord)
- [entityrecordfilter_DuplicateMatchingRecord](#BKMK_entityrecordfilter_DuplicateMatchingRecord)
- [environmentvariabledefinition_DuplicateBaseRecord](#BKMK_environmentvariabledefinition_DuplicateBaseRecord)
- [environmentvariabledefinition_DuplicateMatchingRecord](#BKMK_environmentvariabledefinition_DuplicateMatchingRecord)
- [environmentvariablevalue_DuplicateBaseRecord](#BKMK_environmentvariablevalue_DuplicateBaseRecord)
- [environmentvariablevalue_DuplicateMatchingRecord](#BKMK_environmentvariablevalue_DuplicateMatchingRecord)
- [exportedexcel_DuplicateBaseRecord](#BKMK_exportedexcel_DuplicateBaseRecord)
- [exportedexcel_DuplicateMatchingRecord](#BKMK_exportedexcel_DuplicateMatchingRecord)
- [exportsolutionupload_DuplicateBaseRecord](#BKMK_exportsolutionupload_DuplicateBaseRecord)
- [exportsolutionupload_DuplicateMatchingRecord](#BKMK_exportsolutionupload_DuplicateMatchingRecord)
- [Fax_DuplicateBaseRecord](#BKMK_Fax_DuplicateBaseRecord)
- [Fax_DuplicateMatchingRecord](#BKMK_Fax_DuplicateMatchingRecord)
- [featurecontrolsetting_DuplicateBaseRecord](#BKMK_featurecontrolsetting_DuplicateBaseRecord)
- [featurecontrolsetting_DuplicateMatchingRecord](#BKMK_featurecontrolsetting_DuplicateMatchingRecord)
- [feedback_DuplicateBaseRecord](#BKMK_feedback_DuplicateBaseRecord)
- [feedback_DuplicateMatchingRecord](#BKMK_feedback_DuplicateMatchingRecord)
- [flowcredentialapplication_DuplicateBaseRecord](#BKMK_flowcredentialapplication_DuplicateBaseRecord)
- [flowcredentialapplication_DuplicateMatchingRecord](#BKMK_flowcredentialapplication_DuplicateMatchingRecord)
- [flowevent_DuplicateBaseRecord](#BKMK_flowevent_DuplicateBaseRecord)
- [flowevent_DuplicateMatchingRecord](#BKMK_flowevent_DuplicateMatchingRecord)
- [flowmachinegroup_DuplicateBaseRecord](#BKMK_flowmachinegroup_DuplicateBaseRecord)
- [flowmachinegroup_DuplicateMatchingRecord](#BKMK_flowmachinegroup_DuplicateMatchingRecord)
- [flowmachineimage_DuplicateBaseRecord](#BKMK_flowmachineimage_DuplicateBaseRecord)
- [flowmachineimage_DuplicateMatchingRecord](#BKMK_flowmachineimage_DuplicateMatchingRecord)
- [flowmachineimageversion_DuplicateBaseRecord](#BKMK_flowmachineimageversion_DuplicateBaseRecord)
- [flowmachineimageversion_DuplicateMatchingRecord](#BKMK_flowmachineimageversion_DuplicateMatchingRecord)
- [flowmachinenetwork_DuplicateBaseRecord](#BKMK_flowmachinenetwork_DuplicateBaseRecord)
- [flowmachinenetwork_DuplicateMatchingRecord](#BKMK_flowmachinenetwork_DuplicateMatchingRecord)
- [flowsessionbinary_DuplicateBaseRecord](#BKMK_flowsessionbinary_DuplicateBaseRecord)
- [flowsessionbinary_DuplicateMatchingRecord](#BKMK_flowsessionbinary_DuplicateMatchingRecord)
- [fxexpression_DuplicateBaseRecord](#BKMK_fxexpression_DuplicateBaseRecord)
- [fxexpression_DuplicateMatchingRecord](#BKMK_fxexpression_DuplicateMatchingRecord)
- [Goal_DuplicateBaseRecord](#BKMK_Goal_DuplicateBaseRecord)
- [Goal_DuplicateMatchingRecord](#BKMK_Goal_DuplicateMatchingRecord)
- [GoalRollupQuery_DuplicateBaseRecord](#BKMK_GoalRollupQuery_DuplicateBaseRecord)
- [GoalRollupQuery_DuplicateMatchingRecord](#BKMK_GoalRollupQuery_DuplicateMatchingRecord)
- [governanceconfiguration_DuplicateBaseRecord](#BKMK_governanceconfiguration_DuplicateBaseRecord)
- [governanceconfiguration_DuplicateMatchingRecord](#BKMK_governanceconfiguration_DuplicateMatchingRecord)
- [KbArticle_DuplicateBaseRecord](#BKMK_KbArticle_DuplicateBaseRecord)
- [KbArticle_DuplicateMatchingRecord](#BKMK_KbArticle_DuplicateMatchingRecord)
- [keyvaultreference_DuplicateBaseRecord](#BKMK_keyvaultreference_DuplicateBaseRecord)
- [keyvaultreference_DuplicateMatchingRecord](#BKMK_keyvaultreference_DuplicateMatchingRecord)
- [knowledgearticle_DuplicateBaseRecord](#BKMK_knowledgearticle_DuplicateBaseRecord)
- [knowledgearticle_DuplicateMatchingRecord](#BKMK_knowledgearticle_DuplicateMatchingRecord)
- [KnowledgeBaseRecord_DuplicateBaseRecord](#BKMK_KnowledgeBaseRecord_DuplicateBaseRecord)
- [KnowledgeBaseRecord_DuplicateMatchingRecord](#BKMK_KnowledgeBaseRecord_DuplicateMatchingRecord)
- [knowledgesourceconsumer_DuplicateBaseRecord](#BKMK_knowledgesourceconsumer_DuplicateBaseRecord)
- [knowledgesourceconsumer_DuplicateMatchingRecord](#BKMK_knowledgesourceconsumer_DuplicateMatchingRecord)
- [knowledgesourceprofile_DuplicateBaseRecord](#BKMK_knowledgesourceprofile_DuplicateBaseRecord)
- [knowledgesourceprofile_DuplicateMatchingRecord](#BKMK_knowledgesourceprofile_DuplicateMatchingRecord)
- [Letter_DuplicateBaseRecord](#BKMK_Letter_DuplicateBaseRecord)
- [Letter_DuplicateMatchingRecord](#BKMK_Letter_DuplicateMatchingRecord)
- [managedidentity_DuplicateBaseRecord](#BKMK_managedidentity_DuplicateBaseRecord)
- [managedidentity_DuplicateMatchingRecord](#BKMK_managedidentity_DuplicateMatchingRecord)
- [maskingrule_DuplicateBaseRecord](#BKMK_maskingrule_DuplicateBaseRecord)
- [maskingrule_DuplicateMatchingRecord](#BKMK_maskingrule_DuplicateMatchingRecord)
- [msdyn_aibdataset_DuplicateBaseRecord](#BKMK_msdyn_aibdataset_DuplicateBaseRecord)
- [msdyn_aibdataset_DuplicateMatchingRecord](#BKMK_msdyn_aibdataset_DuplicateMatchingRecord)
- [msdyn_aibdatasetfile_DuplicateBaseRecord](#BKMK_msdyn_aibdatasetfile_DuplicateBaseRecord)
- [msdyn_aibdatasetfile_DuplicateMatchingRecord](#BKMK_msdyn_aibdatasetfile_DuplicateMatchingRecord)
- [msdyn_aibdatasetrecord_DuplicateBaseRecord](#BKMK_msdyn_aibdatasetrecord_DuplicateBaseRecord)
- [msdyn_aibdatasetrecord_DuplicateMatchingRecord](#BKMK_msdyn_aibdatasetrecord_DuplicateMatchingRecord)
- [msdyn_aibdatasetscontainer_DuplicateBaseRecord](#BKMK_msdyn_aibdatasetscontainer_DuplicateBaseRecord)
- [msdyn_aibdatasetscontainer_DuplicateMatchingRecord](#BKMK_msdyn_aibdatasetscontainer_DuplicateMatchingRecord)
- [msdyn_aibfeedbackloop_DuplicateBaseRecord](#BKMK_msdyn_aibfeedbackloop_DuplicateBaseRecord)
- [msdyn_aibfeedbackloop_DuplicateMatchingRecord](#BKMK_msdyn_aibfeedbackloop_DuplicateMatchingRecord)
- [msdyn_aibfile_DuplicateBaseRecord](#BKMK_msdyn_aibfile_DuplicateBaseRecord)
- [msdyn_aibfile_DuplicateMatchingRecord](#BKMK_msdyn_aibfile_DuplicateMatchingRecord)
- [msdyn_aibfileattacheddata_DuplicateBaseRecord](#BKMK_msdyn_aibfileattacheddata_DuplicateBaseRecord)
- [msdyn_aibfileattacheddata_DuplicateMatchingRecord](#BKMK_msdyn_aibfileattacheddata_DuplicateMatchingRecord)
- [msdyn_aiconfigurationsearch_DuplicateBaseRecord](#BKMK_msdyn_aiconfigurationsearch_DuplicateBaseRecord)
- [msdyn_aiconfigurationsearch_DuplicateMatchingRecord](#BKMK_msdyn_aiconfigurationsearch_DuplicateMatchingRecord)
- [msdyn_aievent_DuplicateBaseRecord](#BKMK_msdyn_aievent_DuplicateBaseRecord)
- [msdyn_aievent_DuplicateMatchingRecord](#BKMK_msdyn_aievent_DuplicateMatchingRecord)
- [msdyn_aiodimage_DuplicateBaseRecord](#BKMK_msdyn_aiodimage_DuplicateBaseRecord)
- [msdyn_aiodimage_DuplicateMatchingRecord](#BKMK_msdyn_aiodimage_DuplicateMatchingRecord)
- [msdyn_aiodlabel_DuplicateBaseRecord](#BKMK_msdyn_aiodlabel_DuplicateBaseRecord)
- [msdyn_aiodlabel_DuplicateMatchingRecord](#BKMK_msdyn_aiodlabel_DuplicateMatchingRecord)
- [msdyn_aiodtrainingboundingbox_DuplicateBaseRecord](#BKMK_msdyn_aiodtrainingboundingbox_DuplicateBaseRecord)
- [msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord](#BKMK_msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord)
- [msdyn_aiodtrainingimage_DuplicateBaseRecord](#BKMK_msdyn_aiodtrainingimage_DuplicateBaseRecord)
- [msdyn_aiodtrainingimage_DuplicateMatchingRecord](#BKMK_msdyn_aiodtrainingimage_DuplicateMatchingRecord)
- [msdyn_aioptimization_DuplicateBaseRecord](#BKMK_msdyn_aioptimization_DuplicateBaseRecord)
- [msdyn_aioptimization_DuplicateMatchingRecord](#BKMK_msdyn_aioptimization_DuplicateMatchingRecord)
- [msdyn_aioptimizationprivatedata_DuplicateBaseRecord](#BKMK_msdyn_aioptimizationprivatedata_DuplicateBaseRecord)
- [msdyn_aioptimizationprivatedata_DuplicateMatchingRecord](#BKMK_msdyn_aioptimizationprivatedata_DuplicateMatchingRecord)
- [msdyn_aitestrunbatch_DuplicateBaseRecord](#BKMK_msdyn_aitestrunbatch_DuplicateBaseRecord)
- [msdyn_aitestrunbatch_DuplicateMatchingRecord](#BKMK_msdyn_aitestrunbatch_DuplicateMatchingRecord)
- [msdyn_analysiscomponent_DuplicateBaseRecord](#BKMK_msdyn_analysiscomponent_DuplicateBaseRecord)
- [msdyn_analysiscomponent_DuplicateMatchingRecord](#BKMK_msdyn_analysiscomponent_DuplicateMatchingRecord)
- [msdyn_analysisjob_DuplicateBaseRecord](#BKMK_msdyn_analysisjob_DuplicateBaseRecord)
- [msdyn_analysisjob_DuplicateMatchingRecord](#BKMK_msdyn_analysisjob_DuplicateMatchingRecord)
- [msdyn_analysisoverride_DuplicateBaseRecord](#BKMK_msdyn_analysisoverride_DuplicateBaseRecord)
- [msdyn_analysisoverride_DuplicateMatchingRecord](#BKMK_msdyn_analysisoverride_DuplicateMatchingRecord)
- [msdyn_analysisresult_DuplicateBaseRecord](#BKMK_msdyn_analysisresult_DuplicateBaseRecord)
- [msdyn_analysisresult_DuplicateMatchingRecord](#BKMK_msdyn_analysisresult_DuplicateMatchingRecord)
- [msdyn_analysisresultdetail_DuplicateBaseRecord](#BKMK_msdyn_analysisresultdetail_DuplicateBaseRecord)
- [msdyn_analysisresultdetail_DuplicateMatchingRecord](#BKMK_msdyn_analysisresultdetail_DuplicateMatchingRecord)
- [msdyn_appinsightsmetadata_DuplicateBaseRecord](#BKMK_msdyn_appinsightsmetadata_DuplicateBaseRecord)
- [msdyn_appinsightsmetadata_DuplicateMatchingRecord](#BKMK_msdyn_appinsightsmetadata_DuplicateMatchingRecord)
- [msdyn_copilotinteractions_DuplicateBaseRecord](#BKMK_msdyn_copilotinteractions_DuplicateBaseRecord)
- [msdyn_copilotinteractions_DuplicateMatchingRecord](#BKMK_msdyn_copilotinteractions_DuplicateMatchingRecord)
- [msdyn_customcontrolextendedsettings_DuplicateBaseRecord](#BKMK_msdyn_customcontrolextendedsettings_DuplicateBaseRecord)
- [msdyn_customcontrolextendedsettings_DuplicateMatchingRecord](#BKMK_msdyn_customcontrolextendedsettings_DuplicateMatchingRecord)
- [msdyn_dataflow_datalakefolder_DuplicateBaseRecord](#BKMK_msdyn_dataflow_datalakefolder_DuplicateBaseRecord)
- [msdyn_dataflow_datalakefolder_DuplicateMatchingRecord](#BKMK_msdyn_dataflow_datalakefolder_DuplicateMatchingRecord)
- [msdyn_dataflow_DuplicateBaseRecord](#BKMK_msdyn_dataflow_DuplicateBaseRecord)
- [msdyn_dataflow_DuplicateMatchingRecord](#BKMK_msdyn_dataflow_DuplicateMatchingRecord)
- [msdyn_dataflowconnectionreference_DuplicateBaseRecord](#BKMK_msdyn_dataflowconnectionreference_DuplicateBaseRecord)
- [msdyn_dataflowconnectionreference_DuplicateMatchingRecord](#BKMK_msdyn_dataflowconnectionreference_DuplicateMatchingRecord)
- [msdyn_dataflowrefreshhistory_DuplicateBaseRecord](#BKMK_msdyn_dataflowrefreshhistory_DuplicateBaseRecord)
- [msdyn_dataflowrefreshhistory_DuplicateMatchingRecord](#BKMK_msdyn_dataflowrefreshhistory_DuplicateMatchingRecord)
- [msdyn_dmsrequest_DuplicateBaseRecord](#BKMK_msdyn_dmsrequest_DuplicateBaseRecord)
- [msdyn_dmsrequest_DuplicateMatchingRecord](#BKMK_msdyn_dmsrequest_DuplicateMatchingRecord)
- [msdyn_dmsrequeststatus_DuplicateBaseRecord](#BKMK_msdyn_dmsrequeststatus_DuplicateBaseRecord)
- [msdyn_dmsrequeststatus_DuplicateMatchingRecord](#BKMK_msdyn_dmsrequeststatus_DuplicateMatchingRecord)
- [msdyn_entitylinkchatconfiguration_DuplicateBaseRecord](#BKMK_msdyn_entitylinkchatconfiguration_DuplicateBaseRecord)
- [msdyn_entitylinkchatconfiguration_DuplicateMatchingRecord](#BKMK_msdyn_entitylinkchatconfiguration_DuplicateMatchingRecord)
- [msdyn_entityrefreshhistory_DuplicateBaseRecord](#BKMK_msdyn_entityrefreshhistory_DuplicateBaseRecord)
- [msdyn_entityrefreshhistory_DuplicateMatchingRecord](#BKMK_msdyn_entityrefreshhistory_DuplicateMatchingRecord)
- [msdyn_favoriteknowledgearticle_DuplicateBaseRecord](#BKMK_msdyn_favoriteknowledgearticle_DuplicateBaseRecord)
- [msdyn_favoriteknowledgearticle_DuplicateMatchingRecord](#BKMK_msdyn_favoriteknowledgearticle_DuplicateMatchingRecord)
- [msdyn_federatedarticle_DuplicateBaseRecord](#BKMK_msdyn_federatedarticle_DuplicateBaseRecord)
- [msdyn_federatedarticle_DuplicateMatchingRecord](#BKMK_msdyn_federatedarticle_DuplicateMatchingRecord)
- [msdyn_federatedarticleincident_DuplicateBaseRecord](#BKMK_msdyn_federatedarticleincident_DuplicateBaseRecord)
- [msdyn_federatedarticleincident_DuplicateMatchingRecord](#BKMK_msdyn_federatedarticleincident_DuplicateMatchingRecord)
- [msdyn_fileupload_DuplicateBaseRecord](#BKMK_msdyn_fileupload_DuplicateBaseRecord)
- [msdyn_fileupload_DuplicateMatchingRecord](#BKMK_msdyn_fileupload_DuplicateMatchingRecord)
- [msdyn_flow_actionapprovalmodel_DuplicateBaseRecord](#BKMK_msdyn_flow_actionapprovalmodel_DuplicateBaseRecord)
- [msdyn_flow_actionapprovalmodel_DuplicateMatchingRecord](#BKMK_msdyn_flow_actionapprovalmodel_DuplicateMatchingRecord)
- [msdyn_flow_approval_DuplicateBaseRecord](#BKMK_msdyn_flow_approval_DuplicateBaseRecord)
- [msdyn_flow_approval_DuplicateMatchingRecord](#BKMK_msdyn_flow_approval_DuplicateMatchingRecord)
- [msdyn_flow_approvalrequest_DuplicateBaseRecord](#BKMK_msdyn_flow_approvalrequest_DuplicateBaseRecord)
- [msdyn_flow_approvalrequest_DuplicateMatchingRecord](#BKMK_msdyn_flow_approvalrequest_DuplicateMatchingRecord)
- [msdyn_flow_approvalresponse_DuplicateBaseRecord](#BKMK_msdyn_flow_approvalresponse_DuplicateBaseRecord)
- [msdyn_flow_approvalresponse_DuplicateMatchingRecord](#BKMK_msdyn_flow_approvalresponse_DuplicateMatchingRecord)
- [msdyn_flow_approvalstep_DuplicateBaseRecord](#BKMK_msdyn_flow_approvalstep_DuplicateBaseRecord)
- [msdyn_flow_approvalstep_DuplicateMatchingRecord](#BKMK_msdyn_flow_approvalstep_DuplicateMatchingRecord)
- [msdyn_flow_awaitallactionapprovalmodel_DuplicateBaseRecord](#BKMK_msdyn_flow_awaitallactionapprovalmodel_DuplicateBaseRecord)
- [msdyn_flow_awaitallactionapprovalmodel_DuplicateMatchingRecord](#BKMK_msdyn_flow_awaitallactionapprovalmodel_DuplicateMatchingRecord)
- [msdyn_flow_awaitallapprovalmodel_DuplicateBaseRecord](#BKMK_msdyn_flow_awaitallapprovalmodel_DuplicateBaseRecord)
- [msdyn_flow_awaitallapprovalmodel_DuplicateMatchingRecord](#BKMK_msdyn_flow_awaitallapprovalmodel_DuplicateMatchingRecord)
- [msdyn_flow_basicapprovalmodel_DuplicateBaseRecord](#BKMK_msdyn_flow_basicapprovalmodel_DuplicateBaseRecord)
- [msdyn_flow_basicapprovalmodel_DuplicateMatchingRecord](#BKMK_msdyn_flow_basicapprovalmodel_DuplicateMatchingRecord)
- [msdyn_flow_flowapproval_DuplicateBaseRecord](#BKMK_msdyn_flow_flowapproval_DuplicateBaseRecord)
- [msdyn_flow_flowapproval_DuplicateMatchingRecord](#BKMK_msdyn_flow_flowapproval_DuplicateMatchingRecord)
- [msdyn_formmapping_DuplicateBaseRecord](#BKMK_msdyn_formmapping_DuplicateBaseRecord)
- [msdyn_formmapping_DuplicateMatchingRecord](#BKMK_msdyn_formmapping_DuplicateMatchingRecord)
- [msdyn_function_DuplicateBaseRecord](#BKMK_msdyn_function_DuplicateBaseRecord)
- [msdyn_function_DuplicateMatchingRecord](#BKMK_msdyn_function_DuplicateMatchingRecord)
- [msdyn_integratedsearchprovider_DuplicateBaseRecord](#BKMK_msdyn_integratedsearchprovider_DuplicateBaseRecord)
- [msdyn_integratedsearchprovider_DuplicateMatchingRecord](#BKMK_msdyn_integratedsearchprovider_DuplicateMatchingRecord)
- [msdyn_kalanguagesetting_DuplicateBaseRecord](#BKMK_msdyn_kalanguagesetting_DuplicateBaseRecord)
- [msdyn_kalanguagesetting_DuplicateMatchingRecord](#BKMK_msdyn_kalanguagesetting_DuplicateMatchingRecord)
- [msdyn_kbattachment_DuplicateBaseRecord](#BKMK_msdyn_kbattachment_DuplicateBaseRecord)
- [msdyn_kbattachment_DuplicateMatchingRecord](#BKMK_msdyn_kbattachment_DuplicateMatchingRecord)
- [msdyn_kmfederatedsearchconfig_DuplicateBaseRecord](#BKMK_msdyn_kmfederatedsearchconfig_DuplicateBaseRecord)
- [msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord](#BKMK_msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord)
- [msdyn_knowledgearticleimage_DuplicateBaseRecord](#BKMK_msdyn_knowledgearticleimage_DuplicateBaseRecord)
- [msdyn_knowledgearticleimage_DuplicateMatchingRecord](#BKMK_msdyn_knowledgearticleimage_DuplicateMatchingRecord)
- [msdyn_knowledgearticletemplate_DuplicateBaseRecord](#BKMK_msdyn_knowledgearticletemplate_DuplicateBaseRecord)
- [msdyn_knowledgearticletemplate_DuplicateMatchingRecord](#BKMK_msdyn_knowledgearticletemplate_DuplicateMatchingRecord)
- [msdyn_knowledgeconfiguration_DuplicateBaseRecord](#BKMK_msdyn_knowledgeconfiguration_DuplicateBaseRecord)
- [msdyn_knowledgeconfiguration_DuplicateMatchingRecord](#BKMK_msdyn_knowledgeconfiguration_DuplicateMatchingRecord)
- [msdyn_knowledgeinteractioninsight_DuplicateBaseRecord](#BKMK_msdyn_knowledgeinteractioninsight_DuplicateBaseRecord)
- [msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord](#BKMK_msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord)
- [msdyn_knowledgemanagementsetting_DuplicateBaseRecord](#BKMK_msdyn_knowledgemanagementsetting_DuplicateBaseRecord)
- [msdyn_knowledgemanagementsetting_DuplicateMatchingRecord](#BKMK_msdyn_knowledgemanagementsetting_DuplicateMatchingRecord)
- [msdyn_knowledgepersonalfilter_DuplicateBaseRecord](#BKMK_msdyn_knowledgepersonalfilter_DuplicateBaseRecord)
- [msdyn_knowledgepersonalfilter_DuplicateMatchingRecord](#BKMK_msdyn_knowledgepersonalfilter_DuplicateMatchingRecord)
- [msdyn_knowledgesearchfilter_DuplicateBaseRecord](#BKMK_msdyn_knowledgesearchfilter_DuplicateBaseRecord)
- [msdyn_knowledgesearchfilter_DuplicateMatchingRecord](#BKMK_msdyn_knowledgesearchfilter_DuplicateMatchingRecord)
- [msdyn_knowledgesearchinsight_DuplicateBaseRecord](#BKMK_msdyn_knowledgesearchinsight_DuplicateBaseRecord)
- [msdyn_knowledgesearchinsight_DuplicateMatchingRecord](#BKMK_msdyn_knowledgesearchinsight_DuplicateMatchingRecord)
- [msdyn_mobileapp_DuplicateBaseRecord](#BKMK_msdyn_mobileapp_DuplicateBaseRecord)
- [msdyn_mobileapp_DuplicateMatchingRecord](#BKMK_msdyn_mobileapp_DuplicateMatchingRecord)
- [msdyn_modulerundetail_DuplicateBaseRecord](#BKMK_msdyn_modulerundetail_DuplicateBaseRecord)
- [msdyn_modulerundetail_DuplicateMatchingRecord](#BKMK_msdyn_modulerundetail_DuplicateMatchingRecord)
- [msdyn_pmanalysishistory_DuplicateBaseRecord](#BKMK_msdyn_pmanalysishistory_DuplicateBaseRecord)
- [msdyn_pmanalysishistory_DuplicateMatchingRecord](#BKMK_msdyn_pmanalysishistory_DuplicateMatchingRecord)
- [msdyn_pmbusinessruleautomationconfig_DuplicateBaseRecord](#BKMK_msdyn_pmbusinessruleautomationconfig_DuplicateBaseRecord)
- [msdyn_pmbusinessruleautomationconfig_DuplicateMatchingRecord](#BKMK_msdyn_pmbusinessruleautomationconfig_DuplicateMatchingRecord)
- [msdyn_pmcalendar_DuplicateBaseRecord](#BKMK_msdyn_pmcalendar_DuplicateBaseRecord)
- [msdyn_pmcalendar_DuplicateMatchingRecord](#BKMK_msdyn_pmcalendar_DuplicateMatchingRecord)
- [msdyn_pmcalendarversion_DuplicateBaseRecord](#BKMK_msdyn_pmcalendarversion_DuplicateBaseRecord)
- [msdyn_pmcalendarversion_DuplicateMatchingRecord](#BKMK_msdyn_pmcalendarversion_DuplicateMatchingRecord)
- [msdyn_pminferredtask_DuplicateBaseRecord](#BKMK_msdyn_pminferredtask_DuplicateBaseRecord)
- [msdyn_pminferredtask_DuplicateMatchingRecord](#BKMK_msdyn_pminferredtask_DuplicateMatchingRecord)
- [msdyn_pmprocessextendedmetadataversion_DuplicateBaseRecord](#BKMK_msdyn_pmprocessextendedmetadataversion_DuplicateBaseRecord)
- [msdyn_pmprocessextendedmetadataversion_DuplicateMatchingRecord](#BKMK_msdyn_pmprocessextendedmetadataversion_DuplicateMatchingRecord)
- [msdyn_pmprocesstemplate_DuplicateBaseRecord](#BKMK_msdyn_pmprocesstemplate_DuplicateBaseRecord)
- [msdyn_pmprocesstemplate_DuplicateMatchingRecord](#BKMK_msdyn_pmprocesstemplate_DuplicateMatchingRecord)
- [msdyn_pmprocessusersettings_DuplicateBaseRecord](#BKMK_msdyn_pmprocessusersettings_DuplicateBaseRecord)
- [msdyn_pmprocessusersettings_DuplicateMatchingRecord](#BKMK_msdyn_pmprocessusersettings_DuplicateMatchingRecord)
- [msdyn_pmprocessversion_DuplicateBaseRecord](#BKMK_msdyn_pmprocessversion_DuplicateBaseRecord)
- [msdyn_pmprocessversion_DuplicateMatchingRecord](#BKMK_msdyn_pmprocessversion_DuplicateMatchingRecord)
- [msdyn_pmrecording_DuplicateBaseRecord](#BKMK_msdyn_pmrecording_DuplicateBaseRecord)
- [msdyn_pmrecording_DuplicateMatchingRecord](#BKMK_msdyn_pmrecording_DuplicateMatchingRecord)
- [msdyn_pmsimulation_DuplicateBaseRecord](#BKMK_msdyn_pmsimulation_DuplicateBaseRecord)
- [msdyn_pmsimulation_DuplicateMatchingRecord](#BKMK_msdyn_pmsimulation_DuplicateMatchingRecord)
- [msdyn_pmtab_DuplicateBaseRecord](#BKMK_msdyn_pmtab_DuplicateBaseRecord)
- [msdyn_pmtab_DuplicateMatchingRecord](#BKMK_msdyn_pmtab_DuplicateMatchingRecord)
- [msdyn_pmtemplate_DuplicateBaseRecord](#BKMK_msdyn_pmtemplate_DuplicateBaseRecord)
- [msdyn_pmtemplate_DuplicateMatchingRecord](#BKMK_msdyn_pmtemplate_DuplicateMatchingRecord)
- [msdyn_pmview_DuplicateBaseRecord](#BKMK_msdyn_pmview_DuplicateBaseRecord)
- [msdyn_pmview_DuplicateMatchingRecord](#BKMK_msdyn_pmview_DuplicateMatchingRecord)
- [msdyn_qna_DuplicateBaseRecord](#BKMK_msdyn_qna_DuplicateBaseRecord)
- [msdyn_qna_DuplicateMatchingRecord](#BKMK_msdyn_qna_DuplicateMatchingRecord)
- [msdyn_schedule_DuplicateBaseRecord](#BKMK_msdyn_schedule_DuplicateBaseRecord)
- [msdyn_schedule_DuplicateMatchingRecord](#BKMK_msdyn_schedule_DuplicateMatchingRecord)
- [msdyn_serviceconfiguration_DuplicateBaseRecord](#BKMK_msdyn_serviceconfiguration_DuplicateBaseRecord)
- [msdyn_serviceconfiguration_DuplicateMatchingRecord](#BKMK_msdyn_serviceconfiguration_DuplicateMatchingRecord)
- [msdyn_slakpi_DuplicateBaseRecord](#BKMK_msdyn_slakpi_DuplicateBaseRecord)
- [msdyn_slakpi_DuplicateMatchingRecord](#BKMK_msdyn_slakpi_DuplicateMatchingRecord)
- [msdyn_solutionhealthrule_DuplicateBaseRecord](#BKMK_msdyn_solutionhealthrule_DuplicateBaseRecord)
- [msdyn_solutionhealthrule_DuplicateMatchingRecord](#BKMK_msdyn_solutionhealthrule_DuplicateMatchingRecord)
- [msdyn_solutionhealthruleargument_DuplicateBaseRecord](#BKMK_msdyn_solutionhealthruleargument_DuplicateBaseRecord)
- [msdyn_solutionhealthruleargument_DuplicateMatchingRecord](#BKMK_msdyn_solutionhealthruleargument_DuplicateMatchingRecord)
- [msdyn_solutionhealthruleset_DuplicateBaseRecord](#BKMK_msdyn_solutionhealthruleset_DuplicateBaseRecord)
- [msdyn_solutionhealthruleset_DuplicateMatchingRecord](#BKMK_msdyn_solutionhealthruleset_DuplicateMatchingRecord)
- [msdyn_virtualtablecolumncandidate_DuplicateBaseRecord](#BKMK_msdyn_virtualtablecolumncandidate_DuplicateBaseRecord)
- [msdyn_virtualtablecolumncandidate_DuplicateMatchingRecord](#BKMK_msdyn_virtualtablecolumncandidate_DuplicateMatchingRecord)
- [mspcat_catalogsubmissionfiles_DuplicateBaseRecord](#BKMK_mspcat_catalogsubmissionfiles_DuplicateBaseRecord)
- [mspcat_catalogsubmissionfiles_DuplicateMatchingRecord](#BKMK_mspcat_catalogsubmissionfiles_DuplicateMatchingRecord)
- [mspcat_packagestore_DuplicateBaseRecord](#BKMK_mspcat_packagestore_DuplicateBaseRecord)
- [mspcat_packagestore_DuplicateMatchingRecord](#BKMK_mspcat_packagestore_DuplicateMatchingRecord)
- [organizationdatasyncfnostate_DuplicateBaseRecord](#BKMK_organizationdatasyncfnostate_DuplicateBaseRecord)
- [organizationdatasyncfnostate_DuplicateMatchingRecord](#BKMK_organizationdatasyncfnostate_DuplicateMatchingRecord)
- [organizationdatasyncstate_DuplicateBaseRecord](#BKMK_organizationdatasyncstate_DuplicateBaseRecord)
- [organizationdatasyncstate_DuplicateMatchingRecord](#BKMK_organizationdatasyncstate_DuplicateMatchingRecord)
- [organizationdatasyncsubscription_DuplicateBaseRecord](#BKMK_organizationdatasyncsubscription_DuplicateBaseRecord)
- [organizationdatasyncsubscription_DuplicateMatchingRecord](#BKMK_organizationdatasyncsubscription_DuplicateMatchingRecord)
- [organizationdatasyncsubscriptionentity_DuplicateBaseRecord](#BKMK_organizationdatasyncsubscriptionentity_DuplicateBaseRecord)
- [organizationdatasyncsubscriptionentity_DuplicateMatchingRecord](#BKMK_organizationdatasyncsubscriptionentity_DuplicateMatchingRecord)
- [organizationdatasyncsubscriptionfnotable_DuplicateBaseRecord](#BKMK_organizationdatasyncsubscriptionfnotable_DuplicateBaseRecord)
- [organizationdatasyncsubscriptionfnotable_DuplicateMatchingRecord](#BKMK_organizationdatasyncsubscriptionfnotable_DuplicateMatchingRecord)
- [package_DuplicateBaseRecord](#BKMK_package_DuplicateBaseRecord)
- [package_DuplicateMatchingRecord](#BKMK_package_DuplicateMatchingRecord)
- [packagehistory_DuplicateBaseRecord](#BKMK_packagehistory_DuplicateBaseRecord)
- [packagehistory_DuplicateMatchingRecord](#BKMK_packagehistory_DuplicateMatchingRecord)
- [PhoneCall_DuplicateBaseRecord](#BKMK_PhoneCall_DuplicateBaseRecord)
- [PhoneCall_DuplicateMatchingRecord](#BKMK_PhoneCall_DuplicateMatchingRecord)
- [powerbidataset_DuplicateBaseRecord](#BKMK_powerbidataset_DuplicateBaseRecord)
- [powerbidataset_DuplicateMatchingRecord](#BKMK_powerbidataset_DuplicateMatchingRecord)
- [powerbidatasetapdx_DuplicateBaseRecord](#BKMK_powerbidatasetapdx_DuplicateBaseRecord)
- [powerbidatasetapdx_DuplicateMatchingRecord](#BKMK_powerbidatasetapdx_DuplicateMatchingRecord)
- [powerbimashupparameter_DuplicateBaseRecord](#BKMK_powerbimashupparameter_DuplicateBaseRecord)
- [powerbimashupparameter_DuplicateMatchingRecord](#BKMK_powerbimashupparameter_DuplicateMatchingRecord)
- [powerbireport_DuplicateBaseRecord](#BKMK_powerbireport_DuplicateBaseRecord)
- [powerbireport_DuplicateMatchingRecord](#BKMK_powerbireport_DuplicateMatchingRecord)
- [powerbireportapdx_DuplicateBaseRecord](#BKMK_powerbireportapdx_DuplicateBaseRecord)
- [powerbireportapdx_DuplicateMatchingRecord](#BKMK_powerbireportapdx_DuplicateMatchingRecord)
- [powerfxrule_DuplicateBaseRecord](#BKMK_powerfxrule_DuplicateBaseRecord)
- [powerfxrule_DuplicateMatchingRecord](#BKMK_powerfxrule_DuplicateMatchingRecord)
- [powerpagesddosalert_DuplicateBaseRecord](#BKMK_powerpagesddosalert_DuplicateBaseRecord)
- [powerpagesddosalert_DuplicateMatchingRecord](#BKMK_powerpagesddosalert_DuplicateMatchingRecord)
- [powerpagesmanagedidentity_DuplicateBaseRecord](#BKMK_powerpagesmanagedidentity_DuplicateBaseRecord)
- [powerpagesmanagedidentity_DuplicateMatchingRecord](#BKMK_powerpagesmanagedidentity_DuplicateMatchingRecord)
- [powerpagesscanreport_DuplicateBaseRecord](#BKMK_powerpagesscanreport_DuplicateBaseRecord)
- [powerpagesscanreport_DuplicateMatchingRecord](#BKMK_powerpagesscanreport_DuplicateMatchingRecord)
- [privilegesremovalsetting_DuplicateBaseRecord](#BKMK_privilegesremovalsetting_DuplicateBaseRecord)
- [privilegesremovalsetting_DuplicateMatchingRecord](#BKMK_privilegesremovalsetting_DuplicateMatchingRecord)
- [Publisher_DuplicateBaseRecord](#BKMK_Publisher_DuplicateBaseRecord)
- [Publisher_DuplicateMatchingRecord](#BKMK_Publisher_DuplicateMatchingRecord)
- [purviewlabelinfo_DuplicateBaseRecord](#BKMK_purviewlabelinfo_DuplicateBaseRecord)
- [purviewlabelinfo_DuplicateMatchingRecord](#BKMK_purviewlabelinfo_DuplicateMatchingRecord)
- [purviewlabelsynccache_DuplicateBaseRecord](#BKMK_purviewlabelsynccache_DuplicateBaseRecord)
- [purviewlabelsynccache_DuplicateMatchingRecord](#BKMK_purviewlabelsynccache_DuplicateMatchingRecord)
- [Queue_DuplicateBaseRecord](#BKMK_Queue_DuplicateBaseRecord)
- [Queue_DuplicateMatchingRecord](#BKMK_Queue_DuplicateMatchingRecord)
- [recordfilter_DuplicateBaseRecord](#BKMK_recordfilter_DuplicateBaseRecord)
- [recordfilter_DuplicateMatchingRecord](#BKMK_recordfilter_DuplicateMatchingRecord)
- [RecurringAppointmentMaster_DuplicateBaseRecord](#BKMK_RecurringAppointmentMaster_DuplicateBaseRecord)
- [RecurringAppointmentMaster_DuplicateMatchingRecord](#BKMK_RecurringAppointmentMaster_DuplicateMatchingRecord)
- [reportparameter_DuplicateBaseRecord](#BKMK_reportparameter_DuplicateBaseRecord)
- [reportparameter_DuplicateMatchingRecord](#BKMK_reportparameter_DuplicateMatchingRecord)
- [retaineddataexcel_DuplicateBaseRecord](#BKMK_retaineddataexcel_DuplicateBaseRecord)
- [retaineddataexcel_DuplicateMatchingRecord](#BKMK_retaineddataexcel_DuplicateMatchingRecord)
- [retentionconfig_DuplicateBaseRecord](#BKMK_retentionconfig_DuplicateBaseRecord)
- [retentionconfig_DuplicateMatchingRecord](#BKMK_retentionconfig_DuplicateMatchingRecord)
- [retentionfailuredetail_DuplicateBaseRecord](#BKMK_retentionfailuredetail_DuplicateBaseRecord)
- [retentionfailuredetail_DuplicateMatchingRecord](#BKMK_retentionfailuredetail_DuplicateMatchingRecord)
- [retentionoperation_DuplicateBaseRecord](#BKMK_retentionoperation_DuplicateBaseRecord)
- [retentionoperation_DuplicateMatchingRecord](#BKMK_retentionoperation_DuplicateMatchingRecord)
- [retentionsuccessdetail_DuplicateBaseRecord](#BKMK_retentionsuccessdetail_DuplicateBaseRecord)
- [retentionsuccessdetail_DuplicateMatchingRecord](#BKMK_retentionsuccessdetail_DuplicateMatchingRecord)
- [roleeditorlayout_DuplicateBaseRecord](#BKMK_roleeditorlayout_DuplicateBaseRecord)
- [roleeditorlayout_DuplicateMatchingRecord](#BKMK_roleeditorlayout_DuplicateMatchingRecord)
- [savingrule_DuplicateBaseRecord](#BKMK_savingrule_DuplicateBaseRecord)
- [savingrule_DuplicateMatchingRecord](#BKMK_savingrule_DuplicateMatchingRecord)
- [searchattributesettings_DuplicateBaseRecord](#BKMK_searchattributesettings_DuplicateBaseRecord)
- [searchattributesettings_DuplicateMatchingRecord](#BKMK_searchattributesettings_DuplicateMatchingRecord)
- [searchcustomanalyzer_DuplicateBaseRecord](#BKMK_searchcustomanalyzer_DuplicateBaseRecord)
- [searchcustomanalyzer_DuplicateMatchingRecord](#BKMK_searchcustomanalyzer_DuplicateMatchingRecord)
- [searchrelationshipsettings_DuplicateBaseRecord](#BKMK_searchrelationshipsettings_DuplicateBaseRecord)
- [searchrelationshipsettings_DuplicateMatchingRecord](#BKMK_searchrelationshipsettings_DuplicateMatchingRecord)
- [sensitivitylabelattributemapping_DuplicateBaseRecord](#BKMK_sensitivitylabelattributemapping_DuplicateBaseRecord)
- [sensitivitylabelattributemapping_DuplicateMatchingRecord](#BKMK_sensitivitylabelattributemapping_DuplicateMatchingRecord)
- [serviceplan_DuplicateBaseRecord](#BKMK_serviceplan_DuplicateBaseRecord)
- [serviceplan_DuplicateMatchingRecord](#BKMK_serviceplan_DuplicateMatchingRecord)
- [serviceplanmapping_DuplicateBaseRecord](#BKMK_serviceplanmapping_DuplicateBaseRecord)
- [serviceplanmapping_DuplicateMatchingRecord](#BKMK_serviceplanmapping_DuplicateMatchingRecord)
- [sharedlinksetting_DuplicateBaseRecord](#BKMK_sharedlinksetting_DuplicateBaseRecord)
- [sharedlinksetting_DuplicateMatchingRecord](#BKMK_sharedlinksetting_DuplicateMatchingRecord)
- [SharePointDocumentLocation_DuplicateBaseRecord](#BKMK_SharePointDocumentLocation_DuplicateBaseRecord)
- [SharePointDocumentLocation_DuplicateMatchingRecord](#BKMK_SharePointDocumentLocation_DuplicateMatchingRecord)
- [SharePointSite_DuplicateBaseRecord](#BKMK_SharePointSite_DuplicateBaseRecord)
- [SharePointSite_DuplicateMatchingRecord](#BKMK_SharePointSite_DuplicateMatchingRecord)
- [SocialActivity_DuplicateBaseRecord](#BKMK_SocialActivity_DuplicateBaseRecord)
- [SocialActivity_DuplicateMatchingRecord](#BKMK_SocialActivity_DuplicateMatchingRecord)
- [SocialProfile_DuplicateBaseRecord](#BKMK_SocialProfile_DuplicateBaseRecord)
- [SocialProfile_DuplicateMatchingRecord](#BKMK_SocialProfile_DuplicateMatchingRecord)
- [solutioncomponentattributeconfiguration_DuplicateBaseRecord](#BKMK_solutioncomponentattributeconfiguration_DuplicateBaseRecord)
- [solutioncomponentattributeconfiguration_DuplicateMatchingRecord](#BKMK_solutioncomponentattributeconfiguration_DuplicateMatchingRecord)
- [solutioncomponentbatchconfiguration_DuplicateBaseRecord](#BKMK_solutioncomponentbatchconfiguration_DuplicateBaseRecord)
- [solutioncomponentbatchconfiguration_DuplicateMatchingRecord](#BKMK_solutioncomponentbatchconfiguration_DuplicateMatchingRecord)
- [solutioncomponentconfiguration_DuplicateBaseRecord](#BKMK_solutioncomponentconfiguration_DuplicateBaseRecord)
- [solutioncomponentconfiguration_DuplicateMatchingRecord](#BKMK_solutioncomponentconfiguration_DuplicateMatchingRecord)
- [solutioncomponentrelationshipconfiguration_DuplicateBaseRecord](#BKMK_solutioncomponentrelationshipconfiguration_DuplicateBaseRecord)
- [solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord](#BKMK_solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord)
- [stagesolutionupload_DuplicateBaseRecord](#BKMK_stagesolutionupload_DuplicateBaseRecord)
- [stagesolutionupload_DuplicateMatchingRecord](#BKMK_stagesolutionupload_DuplicateMatchingRecord)
- [supportusertable_DuplicateBaseRecord](#BKMK_supportusertable_DuplicateBaseRecord)
- [supportusertable_DuplicateMatchingRecord](#BKMK_supportusertable_DuplicateMatchingRecord)
- [synapsedatabase_DuplicateBaseRecord](#BKMK_synapsedatabase_DuplicateBaseRecord)
- [synapsedatabase_DuplicateMatchingRecord](#BKMK_synapsedatabase_DuplicateMatchingRecord)
- [synapselinkexternaltablestate_DuplicateBaseRecord](#BKMK_synapselinkexternaltablestate_DuplicateBaseRecord)
- [synapselinkexternaltablestate_DuplicateMatchingRecord](#BKMK_synapselinkexternaltablestate_DuplicateMatchingRecord)
- [synapselinkprofile_DuplicateBaseRecord](#BKMK_synapselinkprofile_DuplicateBaseRecord)
- [synapselinkprofile_DuplicateMatchingRecord](#BKMK_synapselinkprofile_DuplicateMatchingRecord)
- [synapselinkprofileentity_DuplicateBaseRecord](#BKMK_synapselinkprofileentity_DuplicateBaseRecord)
- [synapselinkprofileentity_DuplicateMatchingRecord](#BKMK_synapselinkprofileentity_DuplicateMatchingRecord)
- [synapselinkprofileentitystate_DuplicateBaseRecord](#BKMK_synapselinkprofileentitystate_DuplicateBaseRecord)
- [synapselinkprofileentitystate_DuplicateMatchingRecord](#BKMK_synapselinkprofileentitystate_DuplicateMatchingRecord)
- [synapselinkschedule_DuplicateBaseRecord](#BKMK_synapselinkschedule_DuplicateBaseRecord)
- [synapselinkschedule_DuplicateMatchingRecord](#BKMK_synapselinkschedule_DuplicateMatchingRecord)
- [SystemUser_DuplicateBaseRecord](#BKMK_SystemUser_DuplicateBaseRecord)
- [SystemUser_DuplicateMatchingRecord](#BKMK_SystemUser_DuplicateMatchingRecord)
- [Task_DuplicateBaseRecord](#BKMK_Task_DuplicateBaseRecord)
- [Task_DuplicateMatchingRecord](#BKMK_Task_DuplicateMatchingRecord)
- [Team_DuplicateBaseRecord](#BKMK_Team_DuplicateBaseRecord)
- [Team_DuplicateMatchingRecord](#BKMK_Team_DuplicateMatchingRecord)
- [TransactionCurrency_DuplicateBaseRecord](#BKMK_TransactionCurrency_DuplicateBaseRecord)
- [TransactionCurrency_DuplicateMatchingRecord](#BKMK_TransactionCurrency_DuplicateMatchingRecord)
- [unstructuredfilesearchentity_DuplicateBaseRecord](#BKMK_unstructuredfilesearchentity_DuplicateBaseRecord)
- [unstructuredfilesearchentity_DuplicateMatchingRecord](#BKMK_unstructuredfilesearchentity_DuplicateMatchingRecord)
- [unstructuredfilesearchrecord_DuplicateBaseRecord](#BKMK_unstructuredfilesearchrecord_DuplicateBaseRecord)
- [unstructuredfilesearchrecord_DuplicateMatchingRecord](#BKMK_unstructuredfilesearchrecord_DuplicateMatchingRecord)
- [userrating_DuplicateBaseRecord](#BKMK_userrating_DuplicateBaseRecord)
- [userrating_DuplicateMatchingRecord](#BKMK_userrating_DuplicateMatchingRecord)
- [workflowmetadata_DuplicateBaseRecord](#BKMK_workflowmetadata_DuplicateBaseRecord)
- [workflowmetadata_DuplicateMatchingRecord](#BKMK_workflowmetadata_DuplicateMatchingRecord)
- [workqueue_DuplicateBaseRecord](#BKMK_workqueue_DuplicateBaseRecord)
- [workqueue_DuplicateMatchingRecord](#BKMK_workqueue_DuplicateMatchingRecord)
- [workqueueitem_DuplicateBaseRecord](#BKMK_workqueueitem_DuplicateBaseRecord)
- [workqueueitem_DuplicateMatchingRecord](#BKMK_workqueueitem_DuplicateMatchingRecord)

### <a name="BKMK_Account_DuplicateBaseRecord"></a> Account_DuplicateBaseRecord

One-To-Many Relationship: [account Account_DuplicateBaseRecord](account.md#BKMK_Account_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_account`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Account_DuplicateMatchingRecord"></a> Account_DuplicateMatchingRecord

One-To-Many Relationship: [account Account_DuplicateMatchingRecord](account.md#BKMK_Account_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_account`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_activityfileattachment_DuplicateBaseRecord"></a> activityfileattachment_DuplicateBaseRecord

One-To-Many Relationship: [activityfileattachment activityfileattachment_DuplicateBaseRecord](activityfileattachment.md#BKMK_activityfileattachment_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`activityfileattachment`|
|ReferencedAttribute|`activityfileattachmentid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_activityfileattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_activityfileattachment_DuplicateMatchingRecord"></a> activityfileattachment_DuplicateMatchingRecord

One-To-Many Relationship: [activityfileattachment activityfileattachment_DuplicateMatchingRecord](activityfileattachment.md#BKMK_activityfileattachment_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`activityfileattachment`|
|ReferencedAttribute|`activityfileattachmentid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_activityfileattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_invitation_DuplicateBaseRecord"></a> adx_invitation_DuplicateBaseRecord

One-To-Many Relationship: [adx_invitation adx_invitation_DuplicateBaseRecord](adx_invitation.md#BKMK_adx_invitation_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_invitation`|
|ReferencedAttribute|`adx_invitationid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_adx_invitation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_invitation_DuplicateMatchingRecord"></a> adx_invitation_DuplicateMatchingRecord

One-To-Many Relationship: [adx_invitation adx_invitation_DuplicateMatchingRecord](adx_invitation.md#BKMK_adx_invitation_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_invitation`|
|ReferencedAttribute|`adx_invitationid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_adx_invitation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_inviteredemption_DuplicateBaseRecord"></a> adx_inviteredemption_DuplicateBaseRecord

One-To-Many Relationship: [adx_inviteredemption adx_inviteredemption_DuplicateBaseRecord](adx_inviteredemption.md#BKMK_adx_inviteredemption_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_inviteredemption`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_adx_inviteredemption`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_inviteredemption_DuplicateMatchingRecord"></a> adx_inviteredemption_DuplicateMatchingRecord

One-To-Many Relationship: [adx_inviteredemption adx_inviteredemption_DuplicateMatchingRecord](adx_inviteredemption.md#BKMK_adx_inviteredemption_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_inviteredemption`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_adx_inviteredemption`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aicopilot_DuplicateBaseRecord"></a> aicopilot_DuplicateBaseRecord

One-To-Many Relationship: [aicopilot aicopilot_DuplicateBaseRecord](aicopilot.md#BKMK_aicopilot_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`aicopilot`|
|ReferencedAttribute|`aicopilotid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_aicopilot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aicopilot_DuplicateMatchingRecord"></a> aicopilot_DuplicateMatchingRecord

One-To-Many Relationship: [aicopilot aicopilot_DuplicateMatchingRecord](aicopilot.md#BKMK_aicopilot_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`aicopilot`|
|ReferencedAttribute|`aicopilotid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_aicopilot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginauth_DuplicateBaseRecord"></a> aipluginauth_DuplicateBaseRecord

One-To-Many Relationship: [aipluginauth aipluginauth_DuplicateBaseRecord](aipluginauth.md#BKMK_aipluginauth_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginauth`|
|ReferencedAttribute|`aipluginauthid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_aipluginauth`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginauth_DuplicateMatchingRecord"></a> aipluginauth_DuplicateMatchingRecord

One-To-Many Relationship: [aipluginauth aipluginauth_DuplicateMatchingRecord](aipluginauth.md#BKMK_aipluginauth_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginauth`|
|ReferencedAttribute|`aipluginauthid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_aipluginauth`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperationparameter_DuplicateBaseRecord"></a> aipluginoperationparameter_DuplicateBaseRecord

One-To-Many Relationship: [aipluginoperationparameter aipluginoperationparameter_DuplicateBaseRecord](aipluginoperationparameter.md#BKMK_aipluginoperationparameter_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperationparameter`|
|ReferencedAttribute|`aipluginoperationparameterid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_aipluginoperationparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperationparameter_DuplicateMatchingRecord"></a> aipluginoperationparameter_DuplicateMatchingRecord

One-To-Many Relationship: [aipluginoperationparameter aipluginoperationparameter_DuplicateMatchingRecord](aipluginoperationparameter.md#BKMK_aipluginoperationparameter_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperationparameter`|
|ReferencedAttribute|`aipluginoperationparameterid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_aipluginoperationparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperationresponsetemplate_DuplicateBaseRecord"></a> aipluginoperationresponsetemplate_DuplicateBaseRecord

One-To-Many Relationship: [aipluginoperationresponsetemplate aipluginoperationresponsetemplate_DuplicateBaseRecord](aipluginoperationresponsetemplate.md#BKMK_aipluginoperationresponsetemplate_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperationresponsetemplate`|
|ReferencedAttribute|`aipluginoperationresponsetemplateid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_aipluginoperationresponsetemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperationresponsetemplate_DuplicateMatchingRecord"></a> aipluginoperationresponsetemplate_DuplicateMatchingRecord

One-To-Many Relationship: [aipluginoperationresponsetemplate aipluginoperationresponsetemplate_DuplicateMatchingRecord](aipluginoperationresponsetemplate.md#BKMK_aipluginoperationresponsetemplate_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperationresponsetemplate`|
|ReferencedAttribute|`aipluginoperationresponsetemplateid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_aipluginoperationresponsetemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugintitle_DuplicateBaseRecord"></a> aiplugintitle_DuplicateBaseRecord

One-To-Many Relationship: [aiplugintitle aiplugintitle_DuplicateBaseRecord](aiplugintitle.md#BKMK_aiplugintitle_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugintitle`|
|ReferencedAttribute|`aiplugintitleid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_aiplugintitle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugintitle_DuplicateMatchingRecord"></a> aiplugintitle_DuplicateMatchingRecord

One-To-Many Relationship: [aiplugintitle aiplugintitle_DuplicateMatchingRecord](aiplugintitle.md#BKMK_aiplugintitle_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugintitle`|
|ReferencedAttribute|`aiplugintitleid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_aiplugintitle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginusersetting_DuplicateBaseRecord"></a> aipluginusersetting_DuplicateBaseRecord

One-To-Many Relationship: [aipluginusersetting aipluginusersetting_DuplicateBaseRecord](aipluginusersetting.md#BKMK_aipluginusersetting_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginusersetting`|
|ReferencedAttribute|`aipluginusersettingid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_aipluginusersetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginusersetting_DuplicateMatchingRecord"></a> aipluginusersetting_DuplicateMatchingRecord

One-To-Many Relationship: [aipluginusersetting aipluginusersetting_DuplicateMatchingRecord](aipluginusersetting.md#BKMK_aipluginusersetting_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginusersetting`|
|ReferencedAttribute|`aipluginusersettingid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_aipluginusersetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_applicationuser_DuplicateBaseRecord"></a> applicationuser_DuplicateBaseRecord

One-To-Many Relationship: [applicationuser applicationuser_DuplicateBaseRecord](applicationuser.md#BKMK_applicationuser_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`applicationuser`|
|ReferencedAttribute|`applicationuserid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_applicationuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_applicationuser_DuplicateMatchingRecord"></a> applicationuser_DuplicateMatchingRecord

One-To-Many Relationship: [applicationuser applicationuser_DuplicateMatchingRecord](applicationuser.md#BKMK_applicationuser_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`applicationuser`|
|ReferencedAttribute|`applicationuserid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_applicationuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Appointment_DuplicateBaseRecord"></a> Appointment_DuplicateBaseRecord

One-To-Many Relationship: [appointment Appointment_DuplicateBaseRecord](appointment.md#BKMK_Appointment_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`appointment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Appointment_DuplicateMatchingRecord"></a> Appointment_DuplicateMatchingRecord

One-To-Many Relationship: [appointment Appointment_DuplicateMatchingRecord](appointment.md#BKMK_Appointment_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`appointment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalprocess_DuplicateBaseRecord"></a> approvalprocess_DuplicateBaseRecord

One-To-Many Relationship: [approvalprocess approvalprocess_DuplicateBaseRecord](approvalprocess.md#BKMK_approvalprocess_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalprocess`|
|ReferencedAttribute|`approvalprocessid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_approvalprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalprocess_DuplicateMatchingRecord"></a> approvalprocess_DuplicateMatchingRecord

One-To-Many Relationship: [approvalprocess approvalprocess_DuplicateMatchingRecord](approvalprocess.md#BKMK_approvalprocess_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalprocess`|
|ReferencedAttribute|`approvalprocessid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_approvalprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageapproval_DuplicateBaseRecord"></a> approvalstageapproval_DuplicateBaseRecord

One-To-Many Relationship: [approvalstageapproval approvalstageapproval_DuplicateBaseRecord](approvalstageapproval.md#BKMK_approvalstageapproval_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageapproval`|
|ReferencedAttribute|`approvalstageapprovalid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_approvalstageapproval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageapproval_DuplicateMatchingRecord"></a> approvalstageapproval_DuplicateMatchingRecord

One-To-Many Relationship: [approvalstageapproval approvalstageapproval_DuplicateMatchingRecord](approvalstageapproval.md#BKMK_approvalstageapproval_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageapproval`|
|ReferencedAttribute|`approvalstageapprovalid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_approvalstageapproval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstagecondition_DuplicateBaseRecord"></a> approvalstagecondition_DuplicateBaseRecord

One-To-Many Relationship: [approvalstagecondition approvalstagecondition_DuplicateBaseRecord](approvalstagecondition.md#BKMK_approvalstagecondition_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstagecondition`|
|ReferencedAttribute|`approvalstageconditionid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_approvalstagecondition`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstagecondition_DuplicateMatchingRecord"></a> approvalstagecondition_DuplicateMatchingRecord

One-To-Many Relationship: [approvalstagecondition approvalstagecondition_DuplicateMatchingRecord](approvalstagecondition.md#BKMK_approvalstagecondition_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstagecondition`|
|ReferencedAttribute|`approvalstageconditionid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_approvalstagecondition`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageintelligent_DuplicateBaseRecord"></a> approvalstageintelligent_DuplicateBaseRecord

One-To-Many Relationship: [approvalstageintelligent approvalstageintelligent_DuplicateBaseRecord](approvalstageintelligent.md#BKMK_approvalstageintelligent_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageintelligent`|
|ReferencedAttribute|`approvalstageintelligentid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_approvalstageintelligent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageintelligent_DuplicateMatchingRecord"></a> approvalstageintelligent_DuplicateMatchingRecord

One-To-Many Relationship: [approvalstageintelligent approvalstageintelligent_DuplicateMatchingRecord](approvalstageintelligent.md#BKMK_approvalstageintelligent_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageintelligent`|
|ReferencedAttribute|`approvalstageintelligentid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_approvalstageintelligent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageorder_DuplicateBaseRecord"></a> approvalstageorder_DuplicateBaseRecord

One-To-Many Relationship: [approvalstageorder approvalstageorder_DuplicateBaseRecord](approvalstageorder.md#BKMK_approvalstageorder_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageorder`|
|ReferencedAttribute|`approvalstageorderid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_approvalstageorder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageorder_DuplicateMatchingRecord"></a> approvalstageorder_DuplicateMatchingRecord

One-To-Many Relationship: [approvalstageorder approvalstageorder_DuplicateMatchingRecord](approvalstageorder.md#BKMK_approvalstageorder_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageorder`|
|ReferencedAttribute|`approvalstageorderid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_approvalstageorder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_AsyncOperation_DuplicateBaseRecord"></a> AsyncOperation_DuplicateBaseRecord

One-To-Many Relationship: [asyncoperation AsyncOperation_DuplicateBaseRecord](asyncoperation.md#BKMK_AsyncOperation_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`asyncoperation`|
|ReferencedAttribute|`asyncoperationid`|
|ReferencingAttribute|`asyncoperationid`|
|ReferencingEntityNavigationPropertyName|`asyncoperationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_businessprocess_DuplicateBaseRecord"></a> businessprocess_DuplicateBaseRecord

One-To-Many Relationship: [businessprocess businessprocess_DuplicateBaseRecord](businessprocess.md#BKMK_businessprocess_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`businessprocess`|
|ReferencedAttribute|`businessprocessid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_businessprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_businessprocess_DuplicateMatchingRecord"></a> businessprocess_DuplicateMatchingRecord

One-To-Many Relationship: [businessprocess businessprocess_DuplicateMatchingRecord](businessprocess.md#BKMK_businessprocess_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`businessprocess`|
|ReferencedAttribute|`businessprocessid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_businessprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_card_DuplicateBaseRecord"></a> card_DuplicateBaseRecord

One-To-Many Relationship: [card card_DuplicateBaseRecord](card.md#BKMK_card_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`card`|
|ReferencedAttribute|`cardid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_card`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_card_DuplicateMatchingRecord"></a> card_DuplicateMatchingRecord

One-To-Many Relationship: [card card_DuplicateMatchingRecord](card.md#BKMK_card_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`card`|
|ReferencedAttribute|`cardid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_card`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_catalogassignment_DuplicateBaseRecord"></a> catalogassignment_DuplicateBaseRecord

One-To-Many Relationship: [catalogassignment catalogassignment_DuplicateBaseRecord](catalogassignment.md#BKMK_catalogassignment_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`catalogassignment`|
|ReferencedAttribute|`catalogassignmentid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_catalogassignment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_catalogassignment_DuplicateMatchingRecord"></a> catalogassignment_DuplicateMatchingRecord

One-To-Many Relationship: [catalogassignment catalogassignment_DuplicateMatchingRecord](catalogassignment.md#BKMK_catalogassignment_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`catalogassignment`|
|ReferencedAttribute|`catalogassignmentid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_catalogassignment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_certificatecredential_DuplicateBaseRecord"></a> certificatecredential_DuplicateBaseRecord

One-To-Many Relationship: [certificatecredential certificatecredential_DuplicateBaseRecord](certificatecredential.md#BKMK_certificatecredential_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`certificatecredential`|
|ReferencedAttribute|`certificatecredentialid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_certificatecredential`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_certificatecredential_DuplicateMatchingRecord"></a> certificatecredential_DuplicateMatchingRecord

One-To-Many Relationship: [certificatecredential certificatecredential_DuplicateMatchingRecord](certificatecredential.md#BKMK_certificatecredential_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`certificatecredential`|
|ReferencedAttribute|`certificatecredentialid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_certificatecredential`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connectioninstance_DuplicateBaseRecord"></a> connectioninstance_DuplicateBaseRecord

One-To-Many Relationship: [connectioninstance connectioninstance_DuplicateBaseRecord](connectioninstance.md#BKMK_connectioninstance_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`connectioninstance`|
|ReferencedAttribute|`connectioninstanceid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_connectioninstance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connectioninstance_DuplicateMatchingRecord"></a> connectioninstance_DuplicateMatchingRecord

One-To-Many Relationship: [connectioninstance connectioninstance_DuplicateMatchingRecord](connectioninstance.md#BKMK_connectioninstance_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`connectioninstance`|
|ReferencedAttribute|`connectioninstanceid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_connectioninstance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connector_DuplicateBaseRecord"></a> connector_DuplicateBaseRecord

One-To-Many Relationship: [connector connector_DuplicateBaseRecord](connector.md#BKMK_connector_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`connector`|
|ReferencedAttribute|`connectorid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_connector`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connector_DuplicateMatchingRecord"></a> connector_DuplicateMatchingRecord

One-To-Many Relationship: [connector connector_DuplicateMatchingRecord](connector.md#BKMK_connector_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`connector`|
|ReferencedAttribute|`connectorid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_connector`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Contact_DuplicateBaseRecord"></a> Contact_DuplicateBaseRecord

One-To-Many Relationship: [contact Contact_DuplicateBaseRecord](contact.md#BKMK_Contact_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_contact`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Contact_DuplicateMatchingRecord"></a> Contact_DuplicateMatchingRecord

One-To-Many Relationship: [contact Contact_DuplicateMatchingRecord](contact.md#BKMK_Contact_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_contact`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_conversationtranscript_DuplicateBaseRecord"></a> conversationtranscript_DuplicateBaseRecord

One-To-Many Relationship: [conversationtranscript conversationtranscript_DuplicateBaseRecord](conversationtranscript.md#BKMK_conversationtranscript_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`conversationtranscript`|
|ReferencedAttribute|`conversationtranscriptid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_conversationtranscript`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_conversationtranscript_DuplicateMatchingRecord"></a> conversationtranscript_DuplicateMatchingRecord

One-To-Many Relationship: [conversationtranscript conversationtranscript_DuplicateMatchingRecord](conversationtranscript.md#BKMK_conversationtranscript_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`conversationtranscript`|
|ReferencedAttribute|`conversationtranscriptid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_conversationtranscript`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_credential_DuplicateBaseRecord"></a> credential_DuplicateBaseRecord

One-To-Many Relationship: [credential credential_DuplicateBaseRecord](credential.md#BKMK_credential_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`credential`|
|ReferencedAttribute|`credentialid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_credential`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_credential_DuplicateMatchingRecord"></a> credential_DuplicateMatchingRecord

One-To-Many Relationship: [credential credential_DuplicateMatchingRecord](credential.md#BKMK_credential_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`credential`|
|ReferencedAttribute|`credentialid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_credential`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakefolder_DuplicateBaseRecord"></a> datalakefolder_DuplicateBaseRecord

One-To-Many Relationship: [datalakefolder datalakefolder_DuplicateBaseRecord](datalakefolder.md#BKMK_datalakefolder_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakefolder`|
|ReferencedAttribute|`datalakefolderid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_datalakefolder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakefolder_DuplicateMatchingRecord"></a> datalakefolder_DuplicateMatchingRecord

One-To-Many Relationship: [datalakefolder datalakefolder_DuplicateMatchingRecord](datalakefolder.md#BKMK_datalakefolder_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakefolder`|
|ReferencedAttribute|`datalakefolderid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_datalakefolder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakefolderpermission_DuplicateBaseRecord"></a> datalakefolderpermission_DuplicateBaseRecord

One-To-Many Relationship: [datalakefolderpermission datalakefolderpermission_DuplicateBaseRecord](datalakefolderpermission.md#BKMK_datalakefolderpermission_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakefolderpermission`|
|ReferencedAttribute|`datalakefolderpermissionid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_datalakefolderpermission`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakefolderpermission_DuplicateMatchingRecord"></a> datalakefolderpermission_DuplicateMatchingRecord

One-To-Many Relationship: [datalakefolderpermission datalakefolderpermission_DuplicateMatchingRecord](datalakefolderpermission.md#BKMK_datalakefolderpermission_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakefolderpermission`|
|ReferencedAttribute|`datalakefolderpermissionid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_datalakefolderpermission`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakeworkspace_DuplicateBaseRecord"></a> datalakeworkspace_DuplicateBaseRecord

One-To-Many Relationship: [datalakeworkspace datalakeworkspace_DuplicateBaseRecord](datalakeworkspace.md#BKMK_datalakeworkspace_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakeworkspace`|
|ReferencedAttribute|`datalakeworkspaceid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_datalakeworkspace`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakeworkspace_DuplicateMatchingRecord"></a> datalakeworkspace_DuplicateMatchingRecord

One-To-Many Relationship: [datalakeworkspace datalakeworkspace_DuplicateMatchingRecord](datalakeworkspace.md#BKMK_datalakeworkspace_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakeworkspace`|
|ReferencedAttribute|`datalakeworkspaceid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_datalakeworkspace`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakeworkspacepermission_DuplicateBaseRecord"></a> datalakeworkspacepermission_DuplicateBaseRecord

One-To-Many Relationship: [datalakeworkspacepermission datalakeworkspacepermission_DuplicateBaseRecord](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakeworkspacepermission`|
|ReferencedAttribute|`datalakeworkspacepermissionid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_datalakeworkspacepermission`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakeworkspacepermission_DuplicateMatchingRecord"></a> datalakeworkspacepermission_DuplicateMatchingRecord

One-To-Many Relationship: [datalakeworkspacepermission datalakeworkspacepermission_DuplicateMatchingRecord](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakeworkspacepermission`|
|ReferencedAttribute|`datalakeworkspacepermissionid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_datalakeworkspacepermission`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dataprocessingconfiguration_DuplicateBaseRecord"></a> dataprocessingconfiguration_DuplicateBaseRecord

One-To-Many Relationship: [dataprocessingconfiguration dataprocessingconfiguration_DuplicateBaseRecord](dataprocessingconfiguration.md#BKMK_dataprocessingconfiguration_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`dataprocessingconfiguration`|
|ReferencedAttribute|`dataprocessingconfigurationid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_dataprocessingconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dataprocessingconfiguration_DuplicateMatchingRecord"></a> dataprocessingconfiguration_DuplicateMatchingRecord

One-To-Many Relationship: [dataprocessingconfiguration dataprocessingconfiguration_DuplicateMatchingRecord](dataprocessingconfiguration.md#BKMK_dataprocessingconfiguration_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`dataprocessingconfiguration`|
|ReferencedAttribute|`dataprocessingconfigurationid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_dataprocessingconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_desktopflowmodule_DuplicateBaseRecord"></a> desktopflowmodule_DuplicateBaseRecord

One-To-Many Relationship: [desktopflowmodule desktopflowmodule_DuplicateBaseRecord](desktopflowmodule.md#BKMK_desktopflowmodule_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`desktopflowmodule`|
|ReferencedAttribute|`desktopflowmoduleid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_desktopflowmodule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_desktopflowmodule_DuplicateMatchingRecord"></a> desktopflowmodule_DuplicateMatchingRecord

One-To-Many Relationship: [desktopflowmodule desktopflowmodule_DuplicateMatchingRecord](desktopflowmodule.md#BKMK_desktopflowmodule_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`desktopflowmodule`|
|ReferencedAttribute|`desktopflowmoduleid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_desktopflowmodule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_DuplicateRule_DuplicateBaseRecord"></a> DuplicateRule_DuplicateBaseRecord

One-To-Many Relationship: [duplicaterule DuplicateRule_DuplicateBaseRecord](duplicaterule.md#BKMK_DuplicateRule_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`duplicaterule`|
|ReferencedAttribute|`duplicateruleid`|
|ReferencingAttribute|`duplicateruleid`|
|ReferencingEntityNavigationPropertyName|`duplicateruleid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Email_DuplicateBaseRecord"></a> Email_DuplicateBaseRecord

One-To-Many Relationship: [email Email_DuplicateBaseRecord](email.md#BKMK_Email_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`email`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Email_DuplicateMatchingRecord"></a> Email_DuplicateMatchingRecord

One-To-Many Relationship: [email Email_DuplicateMatchingRecord](email.md#BKMK_Email_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`email`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_emailserverprofile_duplicatebaserecord"></a> emailserverprofile_duplicatebaserecord

One-To-Many Relationship: [emailserverprofile emailserverprofile_duplicatebaserecord](emailserverprofile.md#BKMK_emailserverprofile_duplicatebaserecord)

|Property|Value|
|---|---|
|ReferencedEntity|`emailserverprofile`|
|ReferencedAttribute|`emailserverprofileid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_emailserverprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_emailserverprofile_duplicatematchingrecord"></a> emailserverprofile_duplicatematchingrecord

One-To-Many Relationship: [emailserverprofile emailserverprofile_duplicatematchingrecord](emailserverprofile.md#BKMK_emailserverprofile_duplicatematchingrecord)

|Property|Value|
|---|---|
|ReferencedEntity|`emailserverprofile`|
|ReferencedAttribute|`emailserverprofileid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_emailserverprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityrecordfilter_DuplicateBaseRecord"></a> entityrecordfilter_DuplicateBaseRecord

One-To-Many Relationship: [entityrecordfilter entityrecordfilter_DuplicateBaseRecord](entityrecordfilter.md#BKMK_entityrecordfilter_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`entityrecordfilter`|
|ReferencedAttribute|`entityrecordfilterid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_entityrecordfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityrecordfilter_DuplicateMatchingRecord"></a> entityrecordfilter_DuplicateMatchingRecord

One-To-Many Relationship: [entityrecordfilter entityrecordfilter_DuplicateMatchingRecord](entityrecordfilter.md#BKMK_entityrecordfilter_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`entityrecordfilter`|
|ReferencedAttribute|`entityrecordfilterid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_entityrecordfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariabledefinition_DuplicateBaseRecord"></a> environmentvariabledefinition_DuplicateBaseRecord

One-To-Many Relationship: [environmentvariabledefinition environmentvariabledefinition_DuplicateBaseRecord](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariabledefinition`|
|ReferencedAttribute|`environmentvariabledefinitionid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_environmentvariabledefinition`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariabledefinition_DuplicateMatchingRecord"></a> environmentvariabledefinition_DuplicateMatchingRecord

One-To-Many Relationship: [environmentvariabledefinition environmentvariabledefinition_DuplicateMatchingRecord](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariabledefinition`|
|ReferencedAttribute|`environmentvariabledefinitionid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_environmentvariabledefinition`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariablevalue_DuplicateBaseRecord"></a> environmentvariablevalue_DuplicateBaseRecord

One-To-Many Relationship: [environmentvariablevalue environmentvariablevalue_DuplicateBaseRecord](environmentvariablevalue.md#BKMK_environmentvariablevalue_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariablevalue`|
|ReferencedAttribute|`environmentvariablevalueid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_environmentvariablevalue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariablevalue_DuplicateMatchingRecord"></a> environmentvariablevalue_DuplicateMatchingRecord

One-To-Many Relationship: [environmentvariablevalue environmentvariablevalue_DuplicateMatchingRecord](environmentvariablevalue.md#BKMK_environmentvariablevalue_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariablevalue`|
|ReferencedAttribute|`environmentvariablevalueid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_environmentvariablevalue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_exportedexcel_DuplicateBaseRecord"></a> exportedexcel_DuplicateBaseRecord

One-To-Many Relationship: [exportedexcel exportedexcel_DuplicateBaseRecord](exportedexcel.md#BKMK_exportedexcel_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`exportedexcel`|
|ReferencedAttribute|`exportedexcelid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_exportedexcel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_exportedexcel_DuplicateMatchingRecord"></a> exportedexcel_DuplicateMatchingRecord

One-To-Many Relationship: [exportedexcel exportedexcel_DuplicateMatchingRecord](exportedexcel.md#BKMK_exportedexcel_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`exportedexcel`|
|ReferencedAttribute|`exportedexcelid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_exportedexcel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_exportsolutionupload_DuplicateBaseRecord"></a> exportsolutionupload_DuplicateBaseRecord

One-To-Many Relationship: [exportsolutionupload exportsolutionupload_DuplicateBaseRecord](exportsolutionupload.md#BKMK_exportsolutionupload_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`exportsolutionupload`|
|ReferencedAttribute|`exportsolutionuploadid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_exportsolutionupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_exportsolutionupload_DuplicateMatchingRecord"></a> exportsolutionupload_DuplicateMatchingRecord

One-To-Many Relationship: [exportsolutionupload exportsolutionupload_DuplicateMatchingRecord](exportsolutionupload.md#BKMK_exportsolutionupload_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`exportsolutionupload`|
|ReferencedAttribute|`exportsolutionuploadid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_exportsolutionupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Fax_DuplicateBaseRecord"></a> Fax_DuplicateBaseRecord

One-To-Many Relationship: [fax Fax_DuplicateBaseRecord](fax.md#BKMK_Fax_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`fax`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_fax`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Fax_DuplicateMatchingRecord"></a> Fax_DuplicateMatchingRecord

One-To-Many Relationship: [fax Fax_DuplicateMatchingRecord](fax.md#BKMK_Fax_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`fax`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_fax`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_featurecontrolsetting_DuplicateBaseRecord"></a> featurecontrolsetting_DuplicateBaseRecord

One-To-Many Relationship: [featurecontrolsetting featurecontrolsetting_DuplicateBaseRecord](featurecontrolsetting.md#BKMK_featurecontrolsetting_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`featurecontrolsetting`|
|ReferencedAttribute|`featurecontrolsettingid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_featurecontrolsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_featurecontrolsetting_DuplicateMatchingRecord"></a> featurecontrolsetting_DuplicateMatchingRecord

One-To-Many Relationship: [featurecontrolsetting featurecontrolsetting_DuplicateMatchingRecord](featurecontrolsetting.md#BKMK_featurecontrolsetting_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`featurecontrolsetting`|
|ReferencedAttribute|`featurecontrolsettingid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_featurecontrolsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_feedback_DuplicateBaseRecord"></a> feedback_DuplicateBaseRecord

One-To-Many Relationship: [feedback feedback_DuplicateBaseRecord](feedback.md#BKMK_feedback_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`feedback`|
|ReferencedAttribute|`feedbackid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_feedback`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_feedback_DuplicateMatchingRecord"></a> feedback_DuplicateMatchingRecord

One-To-Many Relationship: [feedback feedback_DuplicateMatchingRecord](feedback.md#BKMK_feedback_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`feedback`|
|ReferencedAttribute|`feedbackid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_feedback`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowcredentialapplication_DuplicateBaseRecord"></a> flowcredentialapplication_DuplicateBaseRecord

One-To-Many Relationship: [flowcredentialapplication flowcredentialapplication_DuplicateBaseRecord](flowcredentialapplication.md#BKMK_flowcredentialapplication_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`flowcredentialapplication`|
|ReferencedAttribute|`flowcredentialapplicationid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_flowcredentialapplication`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowcredentialapplication_DuplicateMatchingRecord"></a> flowcredentialapplication_DuplicateMatchingRecord

One-To-Many Relationship: [flowcredentialapplication flowcredentialapplication_DuplicateMatchingRecord](flowcredentialapplication.md#BKMK_flowcredentialapplication_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`flowcredentialapplication`|
|ReferencedAttribute|`flowcredentialapplicationid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_flowcredentialapplication`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowevent_DuplicateBaseRecord"></a> flowevent_DuplicateBaseRecord

One-To-Many Relationship: [flowevent flowevent_DuplicateBaseRecord](flowevent.md#BKMK_flowevent_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`flowevent`|
|ReferencedAttribute|`floweventid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_flowevent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowevent_DuplicateMatchingRecord"></a> flowevent_DuplicateMatchingRecord

One-To-Many Relationship: [flowevent flowevent_DuplicateMatchingRecord](flowevent.md#BKMK_flowevent_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`flowevent`|
|ReferencedAttribute|`floweventid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_flowevent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinegroup_DuplicateBaseRecord"></a> flowmachinegroup_DuplicateBaseRecord

One-To-Many Relationship: [flowmachinegroup flowmachinegroup_DuplicateBaseRecord](flowmachinegroup.md#BKMK_flowmachinegroup_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinegroup`|
|ReferencedAttribute|`flowmachinegroupid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_flowmachinegroup`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinegroup_DuplicateMatchingRecord"></a> flowmachinegroup_DuplicateMatchingRecord

One-To-Many Relationship: [flowmachinegroup flowmachinegroup_DuplicateMatchingRecord](flowmachinegroup.md#BKMK_flowmachinegroup_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinegroup`|
|ReferencedAttribute|`flowmachinegroupid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_flowmachinegroup`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachineimage_DuplicateBaseRecord"></a> flowmachineimage_DuplicateBaseRecord

One-To-Many Relationship: [flowmachineimage flowmachineimage_DuplicateBaseRecord](flowmachineimage.md#BKMK_flowmachineimage_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachineimage`|
|ReferencedAttribute|`flowmachineimageid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_flowmachineimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachineimage_DuplicateMatchingRecord"></a> flowmachineimage_DuplicateMatchingRecord

One-To-Many Relationship: [flowmachineimage flowmachineimage_DuplicateMatchingRecord](flowmachineimage.md#BKMK_flowmachineimage_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachineimage`|
|ReferencedAttribute|`flowmachineimageid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_flowmachineimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachineimageversion_DuplicateBaseRecord"></a> flowmachineimageversion_DuplicateBaseRecord

One-To-Many Relationship: [flowmachineimageversion flowmachineimageversion_DuplicateBaseRecord](flowmachineimageversion.md#BKMK_flowmachineimageversion_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachineimageversion`|
|ReferencedAttribute|`flowmachineimageversionid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_flowmachineimageversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachineimageversion_DuplicateMatchingRecord"></a> flowmachineimageversion_DuplicateMatchingRecord

One-To-Many Relationship: [flowmachineimageversion flowmachineimageversion_DuplicateMatchingRecord](flowmachineimageversion.md#BKMK_flowmachineimageversion_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachineimageversion`|
|ReferencedAttribute|`flowmachineimageversionid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_flowmachineimageversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinenetwork_DuplicateBaseRecord"></a> flowmachinenetwork_DuplicateBaseRecord

One-To-Many Relationship: [flowmachinenetwork flowmachinenetwork_DuplicateBaseRecord](flowmachinenetwork.md#BKMK_flowmachinenetwork_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinenetwork`|
|ReferencedAttribute|`flowmachinenetworkid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_flowmachinenetwork`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinenetwork_DuplicateMatchingRecord"></a> flowmachinenetwork_DuplicateMatchingRecord

One-To-Many Relationship: [flowmachinenetwork flowmachinenetwork_DuplicateMatchingRecord](flowmachinenetwork.md#BKMK_flowmachinenetwork_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinenetwork`|
|ReferencedAttribute|`flowmachinenetworkid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_flowmachinenetwork`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowsessionbinary_DuplicateBaseRecord"></a> flowsessionbinary_DuplicateBaseRecord

One-To-Many Relationship: [flowsessionbinary flowsessionbinary_DuplicateBaseRecord](flowsessionbinary.md#BKMK_flowsessionbinary_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`flowsessionbinary`|
|ReferencedAttribute|`flowsessionbinaryid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_flowsessionbinary`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowsessionbinary_DuplicateMatchingRecord"></a> flowsessionbinary_DuplicateMatchingRecord

One-To-Many Relationship: [flowsessionbinary flowsessionbinary_DuplicateMatchingRecord](flowsessionbinary.md#BKMK_flowsessionbinary_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`flowsessionbinary`|
|ReferencedAttribute|`flowsessionbinaryid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_flowsessionbinary`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fxexpression_DuplicateBaseRecord"></a> fxexpression_DuplicateBaseRecord

One-To-Many Relationship: [fxexpression fxexpression_DuplicateBaseRecord](fxexpression.md#BKMK_fxexpression_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`fxexpression`|
|ReferencedAttribute|`fxexpressionid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_fxexpression`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fxexpression_DuplicateMatchingRecord"></a> fxexpression_DuplicateMatchingRecord

One-To-Many Relationship: [fxexpression fxexpression_DuplicateMatchingRecord](fxexpression.md#BKMK_fxexpression_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`fxexpression`|
|ReferencedAttribute|`fxexpressionid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_fxexpression`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Goal_DuplicateBaseRecord"></a> Goal_DuplicateBaseRecord

One-To-Many Relationship: [goal Goal_DuplicateBaseRecord](goal.md#BKMK_Goal_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`goal`|
|ReferencedAttribute|`goalid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_goal`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Goal_DuplicateMatchingRecord"></a> Goal_DuplicateMatchingRecord

One-To-Many Relationship: [goal Goal_DuplicateMatchingRecord](goal.md#BKMK_Goal_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`goal`|
|ReferencedAttribute|`goalid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_goal`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_GoalRollupQuery_DuplicateBaseRecord"></a> GoalRollupQuery_DuplicateBaseRecord

One-To-Many Relationship: [goalrollupquery GoalRollupQuery_DuplicateBaseRecord](goalrollupquery.md#BKMK_GoalRollupQuery_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`goalrollupquery`|
|ReferencedAttribute|`goalrollupqueryid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_goalrollupquery`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_GoalRollupQuery_DuplicateMatchingRecord"></a> GoalRollupQuery_DuplicateMatchingRecord

One-To-Many Relationship: [goalrollupquery GoalRollupQuery_DuplicateMatchingRecord](goalrollupquery.md#BKMK_GoalRollupQuery_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`goalrollupquery`|
|ReferencedAttribute|`goalrollupqueryid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_goalrollupquery`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_governanceconfiguration_DuplicateBaseRecord"></a> governanceconfiguration_DuplicateBaseRecord

One-To-Many Relationship: [governanceconfiguration governanceconfiguration_DuplicateBaseRecord](governanceconfiguration.md#BKMK_governanceconfiguration_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`governanceconfiguration`|
|ReferencedAttribute|`governanceconfigurationid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_governanceconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_governanceconfiguration_DuplicateMatchingRecord"></a> governanceconfiguration_DuplicateMatchingRecord

One-To-Many Relationship: [governanceconfiguration governanceconfiguration_DuplicateMatchingRecord](governanceconfiguration.md#BKMK_governanceconfiguration_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`governanceconfiguration`|
|ReferencedAttribute|`governanceconfigurationid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_governanceconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KbArticle_DuplicateBaseRecord"></a> KbArticle_DuplicateBaseRecord

One-To-Many Relationship: [kbarticle KbArticle_DuplicateBaseRecord](kbarticle.md#BKMK_KbArticle_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`kbarticle`|
|ReferencedAttribute|`kbarticleid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_kbarticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KbArticle_DuplicateMatchingRecord"></a> KbArticle_DuplicateMatchingRecord

One-To-Many Relationship: [kbarticle KbArticle_DuplicateMatchingRecord](kbarticle.md#BKMK_KbArticle_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`kbarticle`|
|ReferencedAttribute|`kbarticleid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_kbarticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_keyvaultreference_DuplicateBaseRecord"></a> keyvaultreference_DuplicateBaseRecord

One-To-Many Relationship: [keyvaultreference keyvaultreference_DuplicateBaseRecord](keyvaultreference.md#BKMK_keyvaultreference_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`keyvaultreference`|
|ReferencedAttribute|`keyvaultreferenceid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_keyvaultreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_keyvaultreference_DuplicateMatchingRecord"></a> keyvaultreference_DuplicateMatchingRecord

One-To-Many Relationship: [keyvaultreference keyvaultreference_DuplicateMatchingRecord](keyvaultreference.md#BKMK_keyvaultreference_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`keyvaultreference`|
|ReferencedAttribute|`keyvaultreferenceid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_keyvaultreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgearticle_DuplicateBaseRecord"></a> knowledgearticle_DuplicateBaseRecord

One-To-Many Relationship: [knowledgearticle knowledgearticle_DuplicateBaseRecord](knowledgearticle.md#BKMK_knowledgearticle_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_knowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgearticle_DuplicateMatchingRecord"></a> knowledgearticle_DuplicateMatchingRecord

One-To-Many Relationship: [knowledgearticle knowledgearticle_DuplicateMatchingRecord](knowledgearticle.md#BKMK_knowledgearticle_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_knowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KnowledgeBaseRecord_DuplicateBaseRecord"></a> KnowledgeBaseRecord_DuplicateBaseRecord

One-To-Many Relationship: [knowledgebaserecord KnowledgeBaseRecord_DuplicateBaseRecord](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgebaserecord`|
|ReferencedAttribute|`knowledgebaserecordid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_knowledgebaserecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KnowledgeBaseRecord_DuplicateMatchingRecord"></a> KnowledgeBaseRecord_DuplicateMatchingRecord

One-To-Many Relationship: [knowledgebaserecord KnowledgeBaseRecord_DuplicateMatchingRecord](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgebaserecord`|
|ReferencedAttribute|`knowledgebaserecordid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_knowledgebaserecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgesourceconsumer_DuplicateBaseRecord"></a> knowledgesourceconsumer_DuplicateBaseRecord

One-To-Many Relationship: [knowledgesourceconsumer knowledgesourceconsumer_DuplicateBaseRecord](knowledgesourceconsumer.md#BKMK_knowledgesourceconsumer_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgesourceconsumer`|
|ReferencedAttribute|`knowledgesourceconsumerid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_knowledgesourceconsumer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgesourceconsumer_DuplicateMatchingRecord"></a> knowledgesourceconsumer_DuplicateMatchingRecord

One-To-Many Relationship: [knowledgesourceconsumer knowledgesourceconsumer_DuplicateMatchingRecord](knowledgesourceconsumer.md#BKMK_knowledgesourceconsumer_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgesourceconsumer`|
|ReferencedAttribute|`knowledgesourceconsumerid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_knowledgesourceconsumer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgesourceprofile_DuplicateBaseRecord"></a> knowledgesourceprofile_DuplicateBaseRecord

One-To-Many Relationship: [knowledgesourceprofile knowledgesourceprofile_DuplicateBaseRecord](knowledgesourceprofile.md#BKMK_knowledgesourceprofile_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgesourceprofile`|
|ReferencedAttribute|`knowledgesourceprofileid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_knowledgesourceprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgesourceprofile_DuplicateMatchingRecord"></a> knowledgesourceprofile_DuplicateMatchingRecord

One-To-Many Relationship: [knowledgesourceprofile knowledgesourceprofile_DuplicateMatchingRecord](knowledgesourceprofile.md#BKMK_knowledgesourceprofile_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgesourceprofile`|
|ReferencedAttribute|`knowledgesourceprofileid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_knowledgesourceprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Letter_DuplicateBaseRecord"></a> Letter_DuplicateBaseRecord

One-To-Many Relationship: [letter Letter_DuplicateBaseRecord](letter.md#BKMK_Letter_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`letter`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_letter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Letter_DuplicateMatchingRecord"></a> Letter_DuplicateMatchingRecord

One-To-Many Relationship: [letter Letter_DuplicateMatchingRecord](letter.md#BKMK_Letter_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`letter`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_letter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_managedidentity_DuplicateBaseRecord"></a> managedidentity_DuplicateBaseRecord

One-To-Many Relationship: [managedidentity managedidentity_DuplicateBaseRecord](managedidentity.md#BKMK_managedidentity_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`managedidentity`|
|ReferencedAttribute|`managedidentityid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_managedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_managedidentity_DuplicateMatchingRecord"></a> managedidentity_DuplicateMatchingRecord

One-To-Many Relationship: [managedidentity managedidentity_DuplicateMatchingRecord](managedidentity.md#BKMK_managedidentity_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`managedidentity`|
|ReferencedAttribute|`managedidentityid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_managedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_maskingrule_DuplicateBaseRecord"></a> maskingrule_DuplicateBaseRecord

One-To-Many Relationship: [maskingrule maskingrule_DuplicateBaseRecord](maskingrule.md#BKMK_maskingrule_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`maskingrule`|
|ReferencedAttribute|`maskingruleid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_maskingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_maskingrule_DuplicateMatchingRecord"></a> maskingrule_DuplicateMatchingRecord

One-To-Many Relationship: [maskingrule maskingrule_DuplicateMatchingRecord](maskingrule.md#BKMK_maskingrule_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`maskingrule`|
|ReferencedAttribute|`maskingruleid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_maskingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdataset_DuplicateBaseRecord"></a> msdyn_aibdataset_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_aibdataset msdyn_aibdataset_DuplicateBaseRecord](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdataset`|
|ReferencedAttribute|`msdyn_aibdatasetid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_aibdataset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdataset_DuplicateMatchingRecord"></a> msdyn_aibdataset_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_aibdataset msdyn_aibdataset_DuplicateMatchingRecord](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdataset`|
|ReferencedAttribute|`msdyn_aibdatasetid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_aibdataset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetfile_DuplicateBaseRecord"></a> msdyn_aibdatasetfile_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_aibdatasetfile msdyn_aibdatasetfile_DuplicateBaseRecord](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetfile`|
|ReferencedAttribute|`msdyn_aibdatasetfileid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_aibdatasetfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetfile_DuplicateMatchingRecord"></a> msdyn_aibdatasetfile_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_aibdatasetfile msdyn_aibdatasetfile_DuplicateMatchingRecord](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetfile`|
|ReferencedAttribute|`msdyn_aibdatasetfileid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_aibdatasetfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetrecord_DuplicateBaseRecord"></a> msdyn_aibdatasetrecord_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_aibdatasetrecord msdyn_aibdatasetrecord_DuplicateBaseRecord](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetrecord`|
|ReferencedAttribute|`msdyn_aibdatasetrecordid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_aibdatasetrecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetrecord_DuplicateMatchingRecord"></a> msdyn_aibdatasetrecord_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_aibdatasetrecord msdyn_aibdatasetrecord_DuplicateMatchingRecord](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetrecord`|
|ReferencedAttribute|`msdyn_aibdatasetrecordid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_aibdatasetrecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetscontainer_DuplicateBaseRecord"></a> msdyn_aibdatasetscontainer_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_aibdatasetscontainer msdyn_aibdatasetscontainer_DuplicateBaseRecord](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetscontainer`|
|ReferencedAttribute|`msdyn_aibdatasetscontainerid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_aibdatasetscontainer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetscontainer_DuplicateMatchingRecord"></a> msdyn_aibdatasetscontainer_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_aibdatasetscontainer msdyn_aibdatasetscontainer_DuplicateMatchingRecord](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetscontainer`|
|ReferencedAttribute|`msdyn_aibdatasetscontainerid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_aibdatasetscontainer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfeedbackloop_DuplicateBaseRecord"></a> msdyn_aibfeedbackloop_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_aibfeedbackloop msdyn_aibfeedbackloop_DuplicateBaseRecord](msdyn_aibfeedbackloop.md#BKMK_msdyn_aibfeedbackloop_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfeedbackloop`|
|ReferencedAttribute|`msdyn_aibfeedbackloopid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_aibfeedbackloop`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfeedbackloop_DuplicateMatchingRecord"></a> msdyn_aibfeedbackloop_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_aibfeedbackloop msdyn_aibfeedbackloop_DuplicateMatchingRecord](msdyn_aibfeedbackloop.md#BKMK_msdyn_aibfeedbackloop_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfeedbackloop`|
|ReferencedAttribute|`msdyn_aibfeedbackloopid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_aibfeedbackloop`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfile_DuplicateBaseRecord"></a> msdyn_aibfile_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_aibfile msdyn_aibfile_DuplicateBaseRecord](msdyn_aibfile.md#BKMK_msdyn_aibfile_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfile`|
|ReferencedAttribute|`msdyn_aibfileid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_aibfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfile_DuplicateMatchingRecord"></a> msdyn_aibfile_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_aibfile msdyn_aibfile_DuplicateMatchingRecord](msdyn_aibfile.md#BKMK_msdyn_aibfile_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfile`|
|ReferencedAttribute|`msdyn_aibfileid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_aibfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfileattacheddata_DuplicateBaseRecord"></a> msdyn_aibfileattacheddata_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_aibfileattacheddata msdyn_aibfileattacheddata_DuplicateBaseRecord](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfileattacheddata`|
|ReferencedAttribute|`msdyn_aibfileattacheddataid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_aibfileattacheddata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfileattacheddata_DuplicateMatchingRecord"></a> msdyn_aibfileattacheddata_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_aibfileattacheddata msdyn_aibfileattacheddata_DuplicateMatchingRecord](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfileattacheddata`|
|ReferencedAttribute|`msdyn_aibfileattacheddataid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_aibfileattacheddata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiconfigurationsearch_DuplicateBaseRecord"></a> msdyn_aiconfigurationsearch_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_aiconfigurationsearch msdyn_aiconfigurationsearch_DuplicateBaseRecord](msdyn_aiconfigurationsearch.md#BKMK_msdyn_aiconfigurationsearch_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiconfigurationsearch`|
|ReferencedAttribute|`msdyn_aiconfigurationsearchid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_aiconfigurationsearch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiconfigurationsearch_DuplicateMatchingRecord"></a> msdyn_aiconfigurationsearch_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_aiconfigurationsearch msdyn_aiconfigurationsearch_DuplicateMatchingRecord](msdyn_aiconfigurationsearch.md#BKMK_msdyn_aiconfigurationsearch_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiconfigurationsearch`|
|ReferencedAttribute|`msdyn_aiconfigurationsearchid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_aiconfigurationsearch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievent_DuplicateBaseRecord"></a> msdyn_aievent_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_aievent msdyn_aievent_DuplicateBaseRecord](msdyn_aievent.md#BKMK_msdyn_aievent_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievent`|
|ReferencedAttribute|`msdyn_aieventid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_aievent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievent_DuplicateMatchingRecord"></a> msdyn_aievent_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_aievent msdyn_aievent_DuplicateMatchingRecord](msdyn_aievent.md#BKMK_msdyn_aievent_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievent`|
|ReferencedAttribute|`msdyn_aieventid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_aievent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodimage_DuplicateBaseRecord"></a> msdyn_aiodimage_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_aiodimage msdyn_aiodimage_DuplicateBaseRecord](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodimage`|
|ReferencedAttribute|`msdyn_aiodimageid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_aiodimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodimage_DuplicateMatchingRecord"></a> msdyn_aiodimage_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_aiodimage msdyn_aiodimage_DuplicateMatchingRecord](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodimage`|
|ReferencedAttribute|`msdyn_aiodimageid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_aiodimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodlabel_DuplicateBaseRecord"></a> msdyn_aiodlabel_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_aiodlabel msdyn_aiodlabel_DuplicateBaseRecord](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodlabel`|
|ReferencedAttribute|`msdyn_aiodlabelid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_aiodlabel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodlabel_DuplicateMatchingRecord"></a> msdyn_aiodlabel_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_aiodlabel msdyn_aiodlabel_DuplicateMatchingRecord](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodlabel`|
|ReferencedAttribute|`msdyn_aiodlabelid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_aiodlabel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodtrainingboundingbox_DuplicateBaseRecord"></a> msdyn_aiodtrainingboundingbox_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_aiodtrainingboundingbox msdyn_aiodtrainingboundingbox_DuplicateBaseRecord](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodtrainingboundingbox`|
|ReferencedAttribute|`msdyn_aiodtrainingboundingboxid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_aiodtrainingboundingbox`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord"></a> msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_aiodtrainingboundingbox msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodtrainingboundingbox`|
|ReferencedAttribute|`msdyn_aiodtrainingboundingboxid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_aiodtrainingboundingbox`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodtrainingimage_DuplicateBaseRecord"></a> msdyn_aiodtrainingimage_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_aiodtrainingimage msdyn_aiodtrainingimage_DuplicateBaseRecord](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodtrainingimage`|
|ReferencedAttribute|`msdyn_aiodtrainingimageid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_aiodtrainingimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodtrainingimage_DuplicateMatchingRecord"></a> msdyn_aiodtrainingimage_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_aiodtrainingimage msdyn_aiodtrainingimage_DuplicateMatchingRecord](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodtrainingimage`|
|ReferencedAttribute|`msdyn_aiodtrainingimageid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_aiodtrainingimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aioptimization_DuplicateBaseRecord"></a> msdyn_aioptimization_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_aioptimization msdyn_aioptimization_DuplicateBaseRecord](msdyn_aioptimization.md#BKMK_msdyn_aioptimization_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aioptimization`|
|ReferencedAttribute|`msdyn_aioptimizationid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_aioptimization`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aioptimization_DuplicateMatchingRecord"></a> msdyn_aioptimization_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_aioptimization msdyn_aioptimization_DuplicateMatchingRecord](msdyn_aioptimization.md#BKMK_msdyn_aioptimization_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aioptimization`|
|ReferencedAttribute|`msdyn_aioptimizationid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_aioptimization`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aioptimizationprivatedata_DuplicateBaseRecord"></a> msdyn_aioptimizationprivatedata_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_aioptimizationprivatedata msdyn_aioptimizationprivatedata_DuplicateBaseRecord](msdyn_aioptimizationprivatedata.md#BKMK_msdyn_aioptimizationprivatedata_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aioptimizationprivatedata`|
|ReferencedAttribute|`msdyn_aioptimizationprivatedataid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_aioptimizationprivatedata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aioptimizationprivatedata_DuplicateMatchingRecord"></a> msdyn_aioptimizationprivatedata_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_aioptimizationprivatedata msdyn_aioptimizationprivatedata_DuplicateMatchingRecord](msdyn_aioptimizationprivatedata.md#BKMK_msdyn_aioptimizationprivatedata_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aioptimizationprivatedata`|
|ReferencedAttribute|`msdyn_aioptimizationprivatedataid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_aioptimizationprivatedata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestrunbatch_DuplicateBaseRecord"></a> msdyn_aitestrunbatch_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_aitestrunbatch msdyn_aitestrunbatch_DuplicateBaseRecord](msdyn_aitestrunbatch.md#BKMK_msdyn_aitestrunbatch_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestrunbatch`|
|ReferencedAttribute|`msdyn_aitestrunbatchid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_aitestrunbatch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestrunbatch_DuplicateMatchingRecord"></a> msdyn_aitestrunbatch_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_aitestrunbatch msdyn_aitestrunbatch_DuplicateMatchingRecord](msdyn_aitestrunbatch.md#BKMK_msdyn_aitestrunbatch_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestrunbatch`|
|ReferencedAttribute|`msdyn_aitestrunbatchid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_aitestrunbatch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysiscomponent_DuplicateBaseRecord"></a> msdyn_analysiscomponent_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_analysiscomponent msdyn_analysiscomponent_DuplicateBaseRecord](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysiscomponent`|
|ReferencedAttribute|`msdyn_analysiscomponentid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_analysiscomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysiscomponent_DuplicateMatchingRecord"></a> msdyn_analysiscomponent_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_analysiscomponent msdyn_analysiscomponent_DuplicateMatchingRecord](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysiscomponent`|
|ReferencedAttribute|`msdyn_analysiscomponentid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_analysiscomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisjob_DuplicateBaseRecord"></a> msdyn_analysisjob_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_analysisjob msdyn_analysisjob_DuplicateBaseRecord](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisjob`|
|ReferencedAttribute|`msdyn_analysisjobid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_analysisjob`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisjob_DuplicateMatchingRecord"></a> msdyn_analysisjob_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_analysisjob msdyn_analysisjob_DuplicateMatchingRecord](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisjob`|
|ReferencedAttribute|`msdyn_analysisjobid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_analysisjob`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisoverride_DuplicateBaseRecord"></a> msdyn_analysisoverride_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_analysisoverride msdyn_analysisoverride_DuplicateBaseRecord](msdyn_analysisoverride.md#BKMK_msdyn_analysisoverride_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisoverride`|
|ReferencedAttribute|`msdyn_analysisoverrideid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_analysisoverride`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisoverride_DuplicateMatchingRecord"></a> msdyn_analysisoverride_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_analysisoverride msdyn_analysisoverride_DuplicateMatchingRecord](msdyn_analysisoverride.md#BKMK_msdyn_analysisoverride_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisoverride`|
|ReferencedAttribute|`msdyn_analysisoverrideid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_analysisoverride`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisresult_DuplicateBaseRecord"></a> msdyn_analysisresult_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_analysisresult msdyn_analysisresult_DuplicateBaseRecord](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisresult`|
|ReferencedAttribute|`msdyn_analysisresultid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_analysisresult`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisresult_DuplicateMatchingRecord"></a> msdyn_analysisresult_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_analysisresult msdyn_analysisresult_DuplicateMatchingRecord](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisresult`|
|ReferencedAttribute|`msdyn_analysisresultid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_analysisresult`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisresultdetail_DuplicateBaseRecord"></a> msdyn_analysisresultdetail_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_analysisresultdetail msdyn_analysisresultdetail_DuplicateBaseRecord](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisresultdetail`|
|ReferencedAttribute|`msdyn_analysisresultdetailid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_analysisresultdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisresultdetail_DuplicateMatchingRecord"></a> msdyn_analysisresultdetail_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_analysisresultdetail msdyn_analysisresultdetail_DuplicateMatchingRecord](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisresultdetail`|
|ReferencedAttribute|`msdyn_analysisresultdetailid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_analysisresultdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_appinsightsmetadata_DuplicateBaseRecord"></a> msdyn_appinsightsmetadata_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_appinsightsmetadata msdyn_appinsightsmetadata_DuplicateBaseRecord](msdyn_appinsightsmetadata.md#BKMK_msdyn_appinsightsmetadata_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_appinsightsmetadata`|
|ReferencedAttribute|`msdyn_appinsightsmetadataid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_appinsightsmetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_appinsightsmetadata_DuplicateMatchingRecord"></a> msdyn_appinsightsmetadata_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_appinsightsmetadata msdyn_appinsightsmetadata_DuplicateMatchingRecord](msdyn_appinsightsmetadata.md#BKMK_msdyn_appinsightsmetadata_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_appinsightsmetadata`|
|ReferencedAttribute|`msdyn_appinsightsmetadataid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_appinsightsmetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_copilotinteractions_DuplicateBaseRecord"></a> msdyn_copilotinteractions_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_copilotinteractions msdyn_copilotinteractions_DuplicateBaseRecord](msdyn_copilotinteractions.md#BKMK_msdyn_copilotinteractions_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_copilotinteractions`|
|ReferencedAttribute|`msdyn_copilotinteractionsid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_copilotinteractions`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_copilotinteractions_DuplicateMatchingRecord"></a> msdyn_copilotinteractions_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_copilotinteractions msdyn_copilotinteractions_DuplicateMatchingRecord](msdyn_copilotinteractions.md#BKMK_msdyn_copilotinteractions_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_copilotinteractions`|
|ReferencedAttribute|`msdyn_copilotinteractionsid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_copilotinteractions`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_customcontrolextendedsettings_DuplicateBaseRecord"></a> msdyn_customcontrolextendedsettings_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_customcontrolextendedsettings msdyn_customcontrolextendedsettings_DuplicateBaseRecord](msdyn_customcontrolextendedsettings.md#BKMK_msdyn_customcontrolextendedsettings_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_customcontrolextendedsettings`|
|ReferencedAttribute|`msdyn_customcontrolextendedsettingsid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_customcontrolextendedsettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_customcontrolextendedsettings_DuplicateMatchingRecord"></a> msdyn_customcontrolextendedsettings_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_customcontrolextendedsettings msdyn_customcontrolextendedsettings_DuplicateMatchingRecord](msdyn_customcontrolextendedsettings.md#BKMK_msdyn_customcontrolextendedsettings_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_customcontrolextendedsettings`|
|ReferencedAttribute|`msdyn_customcontrolextendedsettingsid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_customcontrolextendedsettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflow_datalakefolder_DuplicateBaseRecord"></a> msdyn_dataflow_datalakefolder_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_dataflow_datalakefolder msdyn_dataflow_datalakefolder_DuplicateBaseRecord](msdyn_dataflow_datalakefolder.md#BKMK_msdyn_dataflow_datalakefolder_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflow_datalakefolder`|
|ReferencedAttribute|`msdyn_dataflow_datalakefolderid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_dataflow_datalakefolder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflow_datalakefolder_DuplicateMatchingRecord"></a> msdyn_dataflow_datalakefolder_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_dataflow_datalakefolder msdyn_dataflow_datalakefolder_DuplicateMatchingRecord](msdyn_dataflow_datalakefolder.md#BKMK_msdyn_dataflow_datalakefolder_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflow_datalakefolder`|
|ReferencedAttribute|`msdyn_dataflow_datalakefolderid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_dataflow_datalakefolder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflow_DuplicateBaseRecord"></a> msdyn_dataflow_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_dataflow msdyn_dataflow_DuplicateBaseRecord](msdyn_dataflow.md#BKMK_msdyn_dataflow_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflow`|
|ReferencedAttribute|`msdyn_dataflowid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_dataflow`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflow_DuplicateMatchingRecord"></a> msdyn_dataflow_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_dataflow msdyn_dataflow_DuplicateMatchingRecord](msdyn_dataflow.md#BKMK_msdyn_dataflow_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflow`|
|ReferencedAttribute|`msdyn_dataflowid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_dataflow`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowconnectionreference_DuplicateBaseRecord"></a> msdyn_dataflowconnectionreference_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_dataflowconnectionreference msdyn_dataflowconnectionreference_DuplicateBaseRecord](msdyn_dataflowconnectionreference.md#BKMK_msdyn_dataflowconnectionreference_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowconnectionreference`|
|ReferencedAttribute|`msdyn_dataflowconnectionreferenceid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_dataflowconnectionreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowconnectionreference_DuplicateMatchingRecord"></a> msdyn_dataflowconnectionreference_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_dataflowconnectionreference msdyn_dataflowconnectionreference_DuplicateMatchingRecord](msdyn_dataflowconnectionreference.md#BKMK_msdyn_dataflowconnectionreference_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowconnectionreference`|
|ReferencedAttribute|`msdyn_dataflowconnectionreferenceid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_dataflowconnectionreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowrefreshhistory_DuplicateBaseRecord"></a> msdyn_dataflowrefreshhistory_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_dataflowrefreshhistory msdyn_dataflowrefreshhistory_DuplicateBaseRecord](msdyn_dataflowrefreshhistory.md#BKMK_msdyn_dataflowrefreshhistory_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowrefreshhistory`|
|ReferencedAttribute|`msdyn_dataflowrefreshhistoryid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_dataflowrefreshhistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowrefreshhistory_DuplicateMatchingRecord"></a> msdyn_dataflowrefreshhistory_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_dataflowrefreshhistory msdyn_dataflowrefreshhistory_DuplicateMatchingRecord](msdyn_dataflowrefreshhistory.md#BKMK_msdyn_dataflowrefreshhistory_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowrefreshhistory`|
|ReferencedAttribute|`msdyn_dataflowrefreshhistoryid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_dataflowrefreshhistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmsrequest_DuplicateBaseRecord"></a> msdyn_dmsrequest_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_dmsrequest msdyn_dmsrequest_DuplicateBaseRecord](msdyn_dmsrequest.md#BKMK_msdyn_dmsrequest_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmsrequest`|
|ReferencedAttribute|`msdyn_dmsrequestid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_dmsrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmsrequest_DuplicateMatchingRecord"></a> msdyn_dmsrequest_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_dmsrequest msdyn_dmsrequest_DuplicateMatchingRecord](msdyn_dmsrequest.md#BKMK_msdyn_dmsrequest_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmsrequest`|
|ReferencedAttribute|`msdyn_dmsrequestid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_dmsrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmsrequeststatus_DuplicateBaseRecord"></a> msdyn_dmsrequeststatus_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_dmsrequeststatus msdyn_dmsrequeststatus_DuplicateBaseRecord](msdyn_dmsrequeststatus.md#BKMK_msdyn_dmsrequeststatus_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmsrequeststatus`|
|ReferencedAttribute|`msdyn_dmsrequeststatusid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_dmsrequeststatus`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmsrequeststatus_DuplicateMatchingRecord"></a> msdyn_dmsrequeststatus_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_dmsrequeststatus msdyn_dmsrequeststatus_DuplicateMatchingRecord](msdyn_dmsrequeststatus.md#BKMK_msdyn_dmsrequeststatus_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmsrequeststatus`|
|ReferencedAttribute|`msdyn_dmsrequeststatusid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_dmsrequeststatus`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_entitylinkchatconfiguration_DuplicateBaseRecord"></a> msdyn_entitylinkchatconfiguration_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_entitylinkchatconfiguration msdyn_entitylinkchatconfiguration_DuplicateBaseRecord](msdyn_entitylinkchatconfiguration.md#BKMK_msdyn_entitylinkchatconfiguration_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_entitylinkchatconfiguration`|
|ReferencedAttribute|`msdyn_entitylinkchatconfigurationid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_entitylinkchatconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_entitylinkchatconfiguration_DuplicateMatchingRecord"></a> msdyn_entitylinkchatconfiguration_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_entitylinkchatconfiguration msdyn_entitylinkchatconfiguration_DuplicateMatchingRecord](msdyn_entitylinkchatconfiguration.md#BKMK_msdyn_entitylinkchatconfiguration_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_entitylinkchatconfiguration`|
|ReferencedAttribute|`msdyn_entitylinkchatconfigurationid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_entitylinkchatconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_entityrefreshhistory_DuplicateBaseRecord"></a> msdyn_entityrefreshhistory_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_entityrefreshhistory msdyn_entityrefreshhistory_DuplicateBaseRecord](msdyn_entityrefreshhistory.md#BKMK_msdyn_entityrefreshhistory_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_entityrefreshhistory`|
|ReferencedAttribute|`msdyn_entityrefreshhistoryid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_entityrefreshhistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_entityrefreshhistory_DuplicateMatchingRecord"></a> msdyn_entityrefreshhistory_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_entityrefreshhistory msdyn_entityrefreshhistory_DuplicateMatchingRecord](msdyn_entityrefreshhistory.md#BKMK_msdyn_entityrefreshhistory_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_entityrefreshhistory`|
|ReferencedAttribute|`msdyn_entityrefreshhistoryid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_entityrefreshhistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_favoriteknowledgearticle_DuplicateBaseRecord"></a> msdyn_favoriteknowledgearticle_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_favoriteknowledgearticle msdyn_favoriteknowledgearticle_DuplicateBaseRecord](msdyn_favoriteknowledgearticle.md#BKMK_msdyn_favoriteknowledgearticle_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_favoriteknowledgearticle`|
|ReferencedAttribute|`msdyn_favoriteknowledgearticleid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_favoriteknowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_favoriteknowledgearticle_DuplicateMatchingRecord"></a> msdyn_favoriteknowledgearticle_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_favoriteknowledgearticle msdyn_favoriteknowledgearticle_DuplicateMatchingRecord](msdyn_favoriteknowledgearticle.md#BKMK_msdyn_favoriteknowledgearticle_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_favoriteknowledgearticle`|
|ReferencedAttribute|`msdyn_favoriteknowledgearticleid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_favoriteknowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_federatedarticle_DuplicateBaseRecord"></a> msdyn_federatedarticle_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_federatedarticle msdyn_federatedarticle_DuplicateBaseRecord](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_federatedarticle`|
|ReferencedAttribute|`msdyn_federatedarticleid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_federatedarticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_federatedarticle_DuplicateMatchingRecord"></a> msdyn_federatedarticle_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_federatedarticle msdyn_federatedarticle_DuplicateMatchingRecord](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_federatedarticle`|
|ReferencedAttribute|`msdyn_federatedarticleid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_federatedarticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_federatedarticleincident_DuplicateBaseRecord"></a> msdyn_federatedarticleincident_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_federatedarticleincident msdyn_federatedarticleincident_DuplicateBaseRecord](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_federatedarticleincident`|
|ReferencedAttribute|`msdyn_federatedarticleincidentid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_federatedarticleincident`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_federatedarticleincident_DuplicateMatchingRecord"></a> msdyn_federatedarticleincident_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_federatedarticleincident msdyn_federatedarticleincident_DuplicateMatchingRecord](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_federatedarticleincident`|
|ReferencedAttribute|`msdyn_federatedarticleincidentid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_federatedarticleincident`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_fileupload_DuplicateBaseRecord"></a> msdyn_fileupload_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_fileupload msdyn_fileupload_DuplicateBaseRecord](msdyn_fileupload.md#BKMK_msdyn_fileupload_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_fileupload`|
|ReferencedAttribute|`msdyn_fileuploadid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_fileupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_fileupload_DuplicateMatchingRecord"></a> msdyn_fileupload_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_fileupload msdyn_fileupload_DuplicateMatchingRecord](msdyn_fileupload.md#BKMK_msdyn_fileupload_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_fileupload`|
|ReferencedAttribute|`msdyn_fileuploadid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_fileupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_actionapprovalmodel_DuplicateBaseRecord"></a> msdyn_flow_actionapprovalmodel_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_flow_actionapprovalmodel msdyn_flow_actionapprovalmodel_DuplicateBaseRecord](msdyn_flow_actionapprovalmodel.md#BKMK_msdyn_flow_actionapprovalmodel_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_actionapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_actionapprovalmodelid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_flow_actionapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_actionapprovalmodel_DuplicateMatchingRecord"></a> msdyn_flow_actionapprovalmodel_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_flow_actionapprovalmodel msdyn_flow_actionapprovalmodel_DuplicateMatchingRecord](msdyn_flow_actionapprovalmodel.md#BKMK_msdyn_flow_actionapprovalmodel_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_actionapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_actionapprovalmodelid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_flow_actionapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approval_DuplicateBaseRecord"></a> msdyn_flow_approval_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_flow_approval msdyn_flow_approval_DuplicateBaseRecord](msdyn_flow_approval.md#BKMK_msdyn_flow_approval_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approval`|
|ReferencedAttribute|`msdyn_flow_approvalid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_flow_approval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approval_DuplicateMatchingRecord"></a> msdyn_flow_approval_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_flow_approval msdyn_flow_approval_DuplicateMatchingRecord](msdyn_flow_approval.md#BKMK_msdyn_flow_approval_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approval`|
|ReferencedAttribute|`msdyn_flow_approvalid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_flow_approval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalrequest_DuplicateBaseRecord"></a> msdyn_flow_approvalrequest_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_flow_approvalrequest msdyn_flow_approvalrequest_DuplicateBaseRecord](msdyn_flow_approvalrequest.md#BKMK_msdyn_flow_approvalrequest_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalrequest`|
|ReferencedAttribute|`msdyn_flow_approvalrequestid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_flow_approvalrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalrequest_DuplicateMatchingRecord"></a> msdyn_flow_approvalrequest_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_flow_approvalrequest msdyn_flow_approvalrequest_DuplicateMatchingRecord](msdyn_flow_approvalrequest.md#BKMK_msdyn_flow_approvalrequest_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalrequest`|
|ReferencedAttribute|`msdyn_flow_approvalrequestid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_flow_approvalrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalresponse_DuplicateBaseRecord"></a> msdyn_flow_approvalresponse_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_flow_approvalresponse msdyn_flow_approvalresponse_DuplicateBaseRecord](msdyn_flow_approvalresponse.md#BKMK_msdyn_flow_approvalresponse_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalresponse`|
|ReferencedAttribute|`msdyn_flow_approvalresponseid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_flow_approvalresponse`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalresponse_DuplicateMatchingRecord"></a> msdyn_flow_approvalresponse_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_flow_approvalresponse msdyn_flow_approvalresponse_DuplicateMatchingRecord](msdyn_flow_approvalresponse.md#BKMK_msdyn_flow_approvalresponse_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalresponse`|
|ReferencedAttribute|`msdyn_flow_approvalresponseid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_flow_approvalresponse`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalstep_DuplicateBaseRecord"></a> msdyn_flow_approvalstep_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_flow_approvalstep msdyn_flow_approvalstep_DuplicateBaseRecord](msdyn_flow_approvalstep.md#BKMK_msdyn_flow_approvalstep_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalstep`|
|ReferencedAttribute|`msdyn_flow_approvalstepid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_flow_approvalstep`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalstep_DuplicateMatchingRecord"></a> msdyn_flow_approvalstep_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_flow_approvalstep msdyn_flow_approvalstep_DuplicateMatchingRecord](msdyn_flow_approvalstep.md#BKMK_msdyn_flow_approvalstep_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalstep`|
|ReferencedAttribute|`msdyn_flow_approvalstepid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_flow_approvalstep`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_awaitallactionapprovalmodel_DuplicateBaseRecord"></a> msdyn_flow_awaitallactionapprovalmodel_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_flow_awaitallactionapprovalmodel msdyn_flow_awaitallactionapprovalmodel_DuplicateBaseRecord](msdyn_flow_awaitallactionapprovalmodel.md#BKMK_msdyn_flow_awaitallactionapprovalmodel_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_awaitallactionapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_awaitallactionapprovalmodelid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_flow_awaitallactionapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_awaitallactionapprovalmodel_DuplicateMatchingRecord"></a> msdyn_flow_awaitallactionapprovalmodel_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_flow_awaitallactionapprovalmodel msdyn_flow_awaitallactionapprovalmodel_DuplicateMatchingRecord](msdyn_flow_awaitallactionapprovalmodel.md#BKMK_msdyn_flow_awaitallactionapprovalmodel_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_awaitallactionapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_awaitallactionapprovalmodelid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_flow_awaitallactionapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_awaitallapprovalmodel_DuplicateBaseRecord"></a> msdyn_flow_awaitallapprovalmodel_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_flow_awaitallapprovalmodel msdyn_flow_awaitallapprovalmodel_DuplicateBaseRecord](msdyn_flow_awaitallapprovalmodel.md#BKMK_msdyn_flow_awaitallapprovalmodel_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_awaitallapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_awaitallapprovalmodelid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_flow_awaitallapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_awaitallapprovalmodel_DuplicateMatchingRecord"></a> msdyn_flow_awaitallapprovalmodel_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_flow_awaitallapprovalmodel msdyn_flow_awaitallapprovalmodel_DuplicateMatchingRecord](msdyn_flow_awaitallapprovalmodel.md#BKMK_msdyn_flow_awaitallapprovalmodel_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_awaitallapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_awaitallapprovalmodelid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_flow_awaitallapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_basicapprovalmodel_DuplicateBaseRecord"></a> msdyn_flow_basicapprovalmodel_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_flow_basicapprovalmodel msdyn_flow_basicapprovalmodel_DuplicateBaseRecord](msdyn_flow_basicapprovalmodel.md#BKMK_msdyn_flow_basicapprovalmodel_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_basicapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_basicapprovalmodelid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_flow_basicapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_basicapprovalmodel_DuplicateMatchingRecord"></a> msdyn_flow_basicapprovalmodel_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_flow_basicapprovalmodel msdyn_flow_basicapprovalmodel_DuplicateMatchingRecord](msdyn_flow_basicapprovalmodel.md#BKMK_msdyn_flow_basicapprovalmodel_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_basicapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_basicapprovalmodelid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_flow_basicapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_flowapproval_DuplicateBaseRecord"></a> msdyn_flow_flowapproval_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_flow_flowapproval msdyn_flow_flowapproval_DuplicateBaseRecord](msdyn_flow_flowapproval.md#BKMK_msdyn_flow_flowapproval_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_flowapproval`|
|ReferencedAttribute|`msdyn_flow_flowapprovalid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_flow_flowapproval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_flowapproval_DuplicateMatchingRecord"></a> msdyn_flow_flowapproval_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_flow_flowapproval msdyn_flow_flowapproval_DuplicateMatchingRecord](msdyn_flow_flowapproval.md#BKMK_msdyn_flow_flowapproval_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_flowapproval`|
|ReferencedAttribute|`msdyn_flow_flowapprovalid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_flow_flowapproval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_formmapping_DuplicateBaseRecord"></a> msdyn_formmapping_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_formmapping msdyn_formmapping_DuplicateBaseRecord](msdyn_formmapping.md#BKMK_msdyn_formmapping_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_formmapping`|
|ReferencedAttribute|`msdyn_formmappingid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_formmapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_formmapping_DuplicateMatchingRecord"></a> msdyn_formmapping_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_formmapping msdyn_formmapping_DuplicateMatchingRecord](msdyn_formmapping.md#BKMK_msdyn_formmapping_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_formmapping`|
|ReferencedAttribute|`msdyn_formmappingid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_formmapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_function_DuplicateBaseRecord"></a> msdyn_function_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_function msdyn_function_DuplicateBaseRecord](msdyn_function.md#BKMK_msdyn_function_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_function`|
|ReferencedAttribute|`msdyn_functionid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_function`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_function_DuplicateMatchingRecord"></a> msdyn_function_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_function msdyn_function_DuplicateMatchingRecord](msdyn_function.md#BKMK_msdyn_function_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_function`|
|ReferencedAttribute|`msdyn_functionid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_function`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_integratedsearchprovider_DuplicateBaseRecord"></a> msdyn_integratedsearchprovider_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_integratedsearchprovider msdyn_integratedsearchprovider_DuplicateBaseRecord](msdyn_integratedsearchprovider.md#BKMK_msdyn_integratedsearchprovider_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_integratedsearchprovider`|
|ReferencedAttribute|`msdyn_integratedsearchproviderid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_integratedsearchprovider`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_integratedsearchprovider_DuplicateMatchingRecord"></a> msdyn_integratedsearchprovider_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_integratedsearchprovider msdyn_integratedsearchprovider_DuplicateMatchingRecord](msdyn_integratedsearchprovider.md#BKMK_msdyn_integratedsearchprovider_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_integratedsearchprovider`|
|ReferencedAttribute|`msdyn_integratedsearchproviderid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_integratedsearchprovider`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kalanguagesetting_DuplicateBaseRecord"></a> msdyn_kalanguagesetting_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_kalanguagesetting msdyn_kalanguagesetting_DuplicateBaseRecord](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kalanguagesetting`|
|ReferencedAttribute|`msdyn_kalanguagesettingid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_kalanguagesetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kalanguagesetting_DuplicateMatchingRecord"></a> msdyn_kalanguagesetting_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_kalanguagesetting msdyn_kalanguagesetting_DuplicateMatchingRecord](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kalanguagesetting`|
|ReferencedAttribute|`msdyn_kalanguagesettingid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_kalanguagesetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kbattachment_DuplicateBaseRecord"></a> msdyn_kbattachment_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_kbattachment msdyn_kbattachment_DuplicateBaseRecord](msdyn_kbattachment.md#BKMK_msdyn_kbattachment_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kbattachment`|
|ReferencedAttribute|`msdyn_kbattachmentid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_kbattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kbattachment_DuplicateMatchingRecord"></a> msdyn_kbattachment_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_kbattachment msdyn_kbattachment_DuplicateMatchingRecord](msdyn_kbattachment.md#BKMK_msdyn_kbattachment_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kbattachment`|
|ReferencedAttribute|`msdyn_kbattachmentid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_kbattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kmfederatedsearchconfig_DuplicateBaseRecord"></a> msdyn_kmfederatedsearchconfig_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_kmfederatedsearchconfig msdyn_kmfederatedsearchconfig_DuplicateBaseRecord](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kmfederatedsearchconfig`|
|ReferencedAttribute|`msdyn_kmfederatedsearchconfigid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_kmfederatedsearchconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord"></a> msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_kmfederatedsearchconfig msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kmfederatedsearchconfig`|
|ReferencedAttribute|`msdyn_kmfederatedsearchconfigid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_kmfederatedsearchconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgearticleimage_DuplicateBaseRecord"></a> msdyn_knowledgearticleimage_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_knowledgearticleimage msdyn_knowledgearticleimage_DuplicateBaseRecord](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgearticleimage`|
|ReferencedAttribute|`msdyn_knowledgearticleimageid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_knowledgearticleimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgearticleimage_DuplicateMatchingRecord"></a> msdyn_knowledgearticleimage_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_knowledgearticleimage msdyn_knowledgearticleimage_DuplicateMatchingRecord](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgearticleimage`|
|ReferencedAttribute|`msdyn_knowledgearticleimageid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_knowledgearticleimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgearticletemplate_DuplicateBaseRecord"></a> msdyn_knowledgearticletemplate_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_knowledgearticletemplate msdyn_knowledgearticletemplate_DuplicateBaseRecord](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgearticletemplate`|
|ReferencedAttribute|`msdyn_knowledgearticletemplateid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_knowledgearticletemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgearticletemplate_DuplicateMatchingRecord"></a> msdyn_knowledgearticletemplate_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_knowledgearticletemplate msdyn_knowledgearticletemplate_DuplicateMatchingRecord](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgearticletemplate`|
|ReferencedAttribute|`msdyn_knowledgearticletemplateid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_knowledgearticletemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeconfiguration_DuplicateBaseRecord"></a> msdyn_knowledgeconfiguration_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_knowledgeconfiguration msdyn_knowledgeconfiguration_DuplicateBaseRecord](msdyn_knowledgeconfiguration.md#BKMK_msdyn_knowledgeconfiguration_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeconfiguration`|
|ReferencedAttribute|`msdyn_knowledgeconfigurationid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_knowledgeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeconfiguration_DuplicateMatchingRecord"></a> msdyn_knowledgeconfiguration_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_knowledgeconfiguration msdyn_knowledgeconfiguration_DuplicateMatchingRecord](msdyn_knowledgeconfiguration.md#BKMK_msdyn_knowledgeconfiguration_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeconfiguration`|
|ReferencedAttribute|`msdyn_knowledgeconfigurationid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_knowledgeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeinteractioninsight_DuplicateBaseRecord"></a> msdyn_knowledgeinteractioninsight_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_knowledgeinteractioninsight msdyn_knowledgeinteractioninsight_DuplicateBaseRecord](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeinteractioninsight`|
|ReferencedAttribute|`msdyn_knowledgeinteractioninsightid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_knowledgeinteractioninsight`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord"></a> msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_knowledgeinteractioninsight msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeinteractioninsight`|
|ReferencedAttribute|`msdyn_knowledgeinteractioninsightid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_knowledgeinteractioninsight`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgemanagementsetting_DuplicateBaseRecord"></a> msdyn_knowledgemanagementsetting_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_knowledgemanagementsetting msdyn_knowledgemanagementsetting_DuplicateBaseRecord](msdyn_knowledgemanagementsetting.md#BKMK_msdyn_knowledgemanagementsetting_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgemanagementsetting`|
|ReferencedAttribute|`msdyn_knowledgemanagementsettingid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_knowledgemanagementsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgemanagementsetting_DuplicateMatchingRecord"></a> msdyn_knowledgemanagementsetting_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_knowledgemanagementsetting msdyn_knowledgemanagementsetting_DuplicateMatchingRecord](msdyn_knowledgemanagementsetting.md#BKMK_msdyn_knowledgemanagementsetting_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgemanagementsetting`|
|ReferencedAttribute|`msdyn_knowledgemanagementsettingid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_knowledgemanagementsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgepersonalfilter_DuplicateBaseRecord"></a> msdyn_knowledgepersonalfilter_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_knowledgepersonalfilter msdyn_knowledgepersonalfilter_DuplicateBaseRecord](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgepersonalfilter`|
|ReferencedAttribute|`msdyn_knowledgepersonalfilterid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_knowledgepersonalfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgepersonalfilter_DuplicateMatchingRecord"></a> msdyn_knowledgepersonalfilter_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_knowledgepersonalfilter msdyn_knowledgepersonalfilter_DuplicateMatchingRecord](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgepersonalfilter`|
|ReferencedAttribute|`msdyn_knowledgepersonalfilterid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_knowledgepersonalfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgesearchfilter_DuplicateBaseRecord"></a> msdyn_knowledgesearchfilter_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_knowledgesearchfilter msdyn_knowledgesearchfilter_DuplicateBaseRecord](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgesearchfilter`|
|ReferencedAttribute|`msdyn_knowledgesearchfilterid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_knowledgesearchfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgesearchfilter_DuplicateMatchingRecord"></a> msdyn_knowledgesearchfilter_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_knowledgesearchfilter msdyn_knowledgesearchfilter_DuplicateMatchingRecord](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgesearchfilter`|
|ReferencedAttribute|`msdyn_knowledgesearchfilterid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_knowledgesearchfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgesearchinsight_DuplicateBaseRecord"></a> msdyn_knowledgesearchinsight_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_knowledgesearchinsight msdyn_knowledgesearchinsight_DuplicateBaseRecord](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgesearchinsight`|
|ReferencedAttribute|`msdyn_knowledgesearchinsightid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_knowledgesearchinsight`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgesearchinsight_DuplicateMatchingRecord"></a> msdyn_knowledgesearchinsight_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_knowledgesearchinsight msdyn_knowledgesearchinsight_DuplicateMatchingRecord](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgesearchinsight`|
|ReferencedAttribute|`msdyn_knowledgesearchinsightid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_knowledgesearchinsight`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_mobileapp_DuplicateBaseRecord"></a> msdyn_mobileapp_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_mobileapp msdyn_mobileapp_DuplicateBaseRecord](msdyn_mobileapp.md#BKMK_msdyn_mobileapp_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_mobileapp`|
|ReferencedAttribute|`msdyn_mobileappid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_mobileapp`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_mobileapp_DuplicateMatchingRecord"></a> msdyn_mobileapp_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_mobileapp msdyn_mobileapp_DuplicateMatchingRecord](msdyn_mobileapp.md#BKMK_msdyn_mobileapp_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_mobileapp`|
|ReferencedAttribute|`msdyn_mobileappid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_mobileapp`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_modulerundetail_DuplicateBaseRecord"></a> msdyn_modulerundetail_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_modulerundetail msdyn_modulerundetail_DuplicateBaseRecord](msdyn_modulerundetail.md#BKMK_msdyn_modulerundetail_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_modulerundetail`|
|ReferencedAttribute|`msdyn_modulerundetailid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_modulerundetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_modulerundetail_DuplicateMatchingRecord"></a> msdyn_modulerundetail_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_modulerundetail msdyn_modulerundetail_DuplicateMatchingRecord](msdyn_modulerundetail.md#BKMK_msdyn_modulerundetail_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_modulerundetail`|
|ReferencedAttribute|`msdyn_modulerundetailid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_modulerundetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmanalysishistory_DuplicateBaseRecord"></a> msdyn_pmanalysishistory_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_pmanalysishistory msdyn_pmanalysishistory_DuplicateBaseRecord](msdyn_pmanalysishistory.md#BKMK_msdyn_pmanalysishistory_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmanalysishistory`|
|ReferencedAttribute|`msdyn_pmanalysishistoryid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_pmanalysishistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmanalysishistory_DuplicateMatchingRecord"></a> msdyn_pmanalysishistory_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_pmanalysishistory msdyn_pmanalysishistory_DuplicateMatchingRecord](msdyn_pmanalysishistory.md#BKMK_msdyn_pmanalysishistory_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmanalysishistory`|
|ReferencedAttribute|`msdyn_pmanalysishistoryid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_pmanalysishistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmbusinessruleautomationconfig_DuplicateBaseRecord"></a> msdyn_pmbusinessruleautomationconfig_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_pmbusinessruleautomationconfig msdyn_pmbusinessruleautomationconfig_DuplicateBaseRecord](msdyn_pmbusinessruleautomationconfig.md#BKMK_msdyn_pmbusinessruleautomationconfig_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmbusinessruleautomationconfig`|
|ReferencedAttribute|`msdyn_pmbusinessruleautomationconfigid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_pmbusinessruleautomationconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmbusinessruleautomationconfig_DuplicateMatchingRecord"></a> msdyn_pmbusinessruleautomationconfig_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_pmbusinessruleautomationconfig msdyn_pmbusinessruleautomationconfig_DuplicateMatchingRecord](msdyn_pmbusinessruleautomationconfig.md#BKMK_msdyn_pmbusinessruleautomationconfig_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmbusinessruleautomationconfig`|
|ReferencedAttribute|`msdyn_pmbusinessruleautomationconfigid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_pmbusinessruleautomationconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmcalendar_DuplicateBaseRecord"></a> msdyn_pmcalendar_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_pmcalendar msdyn_pmcalendar_DuplicateBaseRecord](msdyn_pmcalendar.md#BKMK_msdyn_pmcalendar_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmcalendar`|
|ReferencedAttribute|`msdyn_pmcalendarid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_pmcalendar`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmcalendar_DuplicateMatchingRecord"></a> msdyn_pmcalendar_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_pmcalendar msdyn_pmcalendar_DuplicateMatchingRecord](msdyn_pmcalendar.md#BKMK_msdyn_pmcalendar_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmcalendar`|
|ReferencedAttribute|`msdyn_pmcalendarid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_pmcalendar`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmcalendarversion_DuplicateBaseRecord"></a> msdyn_pmcalendarversion_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_pmcalendarversion msdyn_pmcalendarversion_DuplicateBaseRecord](msdyn_pmcalendarversion.md#BKMK_msdyn_pmcalendarversion_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmcalendarversion`|
|ReferencedAttribute|`msdyn_pmcalendarversionid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_pmcalendarversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmcalendarversion_DuplicateMatchingRecord"></a> msdyn_pmcalendarversion_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_pmcalendarversion msdyn_pmcalendarversion_DuplicateMatchingRecord](msdyn_pmcalendarversion.md#BKMK_msdyn_pmcalendarversion_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmcalendarversion`|
|ReferencedAttribute|`msdyn_pmcalendarversionid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_pmcalendarversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pminferredtask_DuplicateBaseRecord"></a> msdyn_pminferredtask_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_pminferredtask msdyn_pminferredtask_DuplicateBaseRecord](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pminferredtask`|
|ReferencedAttribute|`msdyn_pminferredtaskid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_pminferredtask`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pminferredtask_DuplicateMatchingRecord"></a> msdyn_pminferredtask_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_pminferredtask msdyn_pminferredtask_DuplicateMatchingRecord](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pminferredtask`|
|ReferencedAttribute|`msdyn_pminferredtaskid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_pminferredtask`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessextendedmetadataversion_DuplicateBaseRecord"></a> msdyn_pmprocessextendedmetadataversion_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_pmprocessextendedmetadataversion msdyn_pmprocessextendedmetadataversion_DuplicateBaseRecord](msdyn_pmprocessextendedmetadataversion.md#BKMK_msdyn_pmprocessextendedmetadataversion_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessextendedmetadataversion`|
|ReferencedAttribute|`msdyn_pmprocessextendedmetadataversionid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_pmprocessextendedmetadataversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessextendedmetadataversion_DuplicateMatchingRecord"></a> msdyn_pmprocessextendedmetadataversion_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_pmprocessextendedmetadataversion msdyn_pmprocessextendedmetadataversion_DuplicateMatchingRecord](msdyn_pmprocessextendedmetadataversion.md#BKMK_msdyn_pmprocessextendedmetadataversion_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessextendedmetadataversion`|
|ReferencedAttribute|`msdyn_pmprocessextendedmetadataversionid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_pmprocessextendedmetadataversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocesstemplate_DuplicateBaseRecord"></a> msdyn_pmprocesstemplate_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_pmprocesstemplate msdyn_pmprocesstemplate_DuplicateBaseRecord](msdyn_pmprocesstemplate.md#BKMK_msdyn_pmprocesstemplate_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocesstemplate`|
|ReferencedAttribute|`msdyn_pmprocesstemplateid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_pmprocesstemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocesstemplate_DuplicateMatchingRecord"></a> msdyn_pmprocesstemplate_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_pmprocesstemplate msdyn_pmprocesstemplate_DuplicateMatchingRecord](msdyn_pmprocesstemplate.md#BKMK_msdyn_pmprocesstemplate_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocesstemplate`|
|ReferencedAttribute|`msdyn_pmprocesstemplateid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_pmprocesstemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessusersettings_DuplicateBaseRecord"></a> msdyn_pmprocessusersettings_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_pmprocessusersettings msdyn_pmprocessusersettings_DuplicateBaseRecord](msdyn_pmprocessusersettings.md#BKMK_msdyn_pmprocessusersettings_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessusersettings`|
|ReferencedAttribute|`msdyn_pmprocessusersettingsid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_pmprocessusersettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessusersettings_DuplicateMatchingRecord"></a> msdyn_pmprocessusersettings_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_pmprocessusersettings msdyn_pmprocessusersettings_DuplicateMatchingRecord](msdyn_pmprocessusersettings.md#BKMK_msdyn_pmprocessusersettings_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessusersettings`|
|ReferencedAttribute|`msdyn_pmprocessusersettingsid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_pmprocessusersettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessversion_DuplicateBaseRecord"></a> msdyn_pmprocessversion_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_pmprocessversion msdyn_pmprocessversion_DuplicateBaseRecord](msdyn_pmprocessversion.md#BKMK_msdyn_pmprocessversion_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessversion`|
|ReferencedAttribute|`msdyn_pmprocessversionid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_pmprocessversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessversion_DuplicateMatchingRecord"></a> msdyn_pmprocessversion_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_pmprocessversion msdyn_pmprocessversion_DuplicateMatchingRecord](msdyn_pmprocessversion.md#BKMK_msdyn_pmprocessversion_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessversion`|
|ReferencedAttribute|`msdyn_pmprocessversionid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_pmprocessversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmrecording_DuplicateBaseRecord"></a> msdyn_pmrecording_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_pmrecording msdyn_pmrecording_DuplicateBaseRecord](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmrecording`|
|ReferencedAttribute|`msdyn_pmrecordingid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_pmrecording`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmrecording_DuplicateMatchingRecord"></a> msdyn_pmrecording_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_pmrecording msdyn_pmrecording_DuplicateMatchingRecord](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmrecording`|
|ReferencedAttribute|`msdyn_pmrecordingid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_pmrecording`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmsimulation_DuplicateBaseRecord"></a> msdyn_pmsimulation_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_pmsimulation msdyn_pmsimulation_DuplicateBaseRecord](msdyn_pmsimulation.md#BKMK_msdyn_pmsimulation_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmsimulation`|
|ReferencedAttribute|`msdyn_pmsimulationid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_pmsimulation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmsimulation_DuplicateMatchingRecord"></a> msdyn_pmsimulation_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_pmsimulation msdyn_pmsimulation_DuplicateMatchingRecord](msdyn_pmsimulation.md#BKMK_msdyn_pmsimulation_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmsimulation`|
|ReferencedAttribute|`msdyn_pmsimulationid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_pmsimulation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmtab_DuplicateBaseRecord"></a> msdyn_pmtab_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_pmtab msdyn_pmtab_DuplicateBaseRecord](msdyn_pmtab.md#BKMK_msdyn_pmtab_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmtab`|
|ReferencedAttribute|`msdyn_pmtabid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_pmtab`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmtab_DuplicateMatchingRecord"></a> msdyn_pmtab_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_pmtab msdyn_pmtab_DuplicateMatchingRecord](msdyn_pmtab.md#BKMK_msdyn_pmtab_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmtab`|
|ReferencedAttribute|`msdyn_pmtabid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_pmtab`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmtemplate_DuplicateBaseRecord"></a> msdyn_pmtemplate_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_pmtemplate msdyn_pmtemplate_DuplicateBaseRecord](msdyn_pmtemplate.md#BKMK_msdyn_pmtemplate_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmtemplate`|
|ReferencedAttribute|`msdyn_pmtemplateid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_pmtemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmtemplate_DuplicateMatchingRecord"></a> msdyn_pmtemplate_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_pmtemplate msdyn_pmtemplate_DuplicateMatchingRecord](msdyn_pmtemplate.md#BKMK_msdyn_pmtemplate_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmtemplate`|
|ReferencedAttribute|`msdyn_pmtemplateid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_pmtemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmview_DuplicateBaseRecord"></a> msdyn_pmview_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_pmview msdyn_pmview_DuplicateBaseRecord](msdyn_pmview.md#BKMK_msdyn_pmview_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmview`|
|ReferencedAttribute|`msdyn_pmviewid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_pmview`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmview_DuplicateMatchingRecord"></a> msdyn_pmview_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_pmview msdyn_pmview_DuplicateMatchingRecord](msdyn_pmview.md#BKMK_msdyn_pmview_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmview`|
|ReferencedAttribute|`msdyn_pmviewid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_pmview`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_qna_DuplicateBaseRecord"></a> msdyn_qna_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_qna msdyn_qna_DuplicateBaseRecord](msdyn_qna.md#BKMK_msdyn_qna_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_qna`|
|ReferencedAttribute|`msdyn_qnaid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_qna`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_qna_DuplicateMatchingRecord"></a> msdyn_qna_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_qna msdyn_qna_DuplicateMatchingRecord](msdyn_qna.md#BKMK_msdyn_qna_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_qna`|
|ReferencedAttribute|`msdyn_qnaid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_qna`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_schedule_DuplicateBaseRecord"></a> msdyn_schedule_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_schedule msdyn_schedule_DuplicateBaseRecord](msdyn_schedule.md#BKMK_msdyn_schedule_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_schedule`|
|ReferencedAttribute|`msdyn_scheduleid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_schedule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_schedule_DuplicateMatchingRecord"></a> msdyn_schedule_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_schedule msdyn_schedule_DuplicateMatchingRecord](msdyn_schedule.md#BKMK_msdyn_schedule_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_schedule`|
|ReferencedAttribute|`msdyn_scheduleid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_schedule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_serviceconfiguration_DuplicateBaseRecord"></a> msdyn_serviceconfiguration_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_serviceconfiguration msdyn_serviceconfiguration_DuplicateBaseRecord](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_serviceconfiguration`|
|ReferencedAttribute|`msdyn_serviceconfigurationid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_serviceconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_serviceconfiguration_DuplicateMatchingRecord"></a> msdyn_serviceconfiguration_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_serviceconfiguration msdyn_serviceconfiguration_DuplicateMatchingRecord](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_serviceconfiguration`|
|ReferencedAttribute|`msdyn_serviceconfigurationid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_serviceconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_slakpi_DuplicateBaseRecord"></a> msdyn_slakpi_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_slakpi msdyn_slakpi_DuplicateBaseRecord](msdyn_slakpi.md#BKMK_msdyn_slakpi_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_slakpi`|
|ReferencedAttribute|`msdyn_slakpiid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_slakpi`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_slakpi_DuplicateMatchingRecord"></a> msdyn_slakpi_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_slakpi msdyn_slakpi_DuplicateMatchingRecord](msdyn_slakpi.md#BKMK_msdyn_slakpi_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_slakpi`|
|ReferencedAttribute|`msdyn_slakpiid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_slakpi`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthrule_DuplicateBaseRecord"></a> msdyn_solutionhealthrule_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_solutionhealthrule msdyn_solutionhealthrule_DuplicateBaseRecord](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthrule`|
|ReferencedAttribute|`msdyn_solutionhealthruleid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_solutionhealthrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthrule_DuplicateMatchingRecord"></a> msdyn_solutionhealthrule_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_solutionhealthrule msdyn_solutionhealthrule_DuplicateMatchingRecord](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthrule`|
|ReferencedAttribute|`msdyn_solutionhealthruleid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_solutionhealthrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthruleargument_DuplicateBaseRecord"></a> msdyn_solutionhealthruleargument_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_solutionhealthruleargument msdyn_solutionhealthruleargument_DuplicateBaseRecord](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthruleargument`|
|ReferencedAttribute|`msdyn_solutionhealthruleargumentid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_solutionhealthruleargument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthruleargument_DuplicateMatchingRecord"></a> msdyn_solutionhealthruleargument_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_solutionhealthruleargument msdyn_solutionhealthruleargument_DuplicateMatchingRecord](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthruleargument`|
|ReferencedAttribute|`msdyn_solutionhealthruleargumentid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_solutionhealthruleargument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthruleset_DuplicateBaseRecord"></a> msdyn_solutionhealthruleset_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_solutionhealthruleset msdyn_solutionhealthruleset_DuplicateBaseRecord](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthruleset`|
|ReferencedAttribute|`msdyn_solutionhealthrulesetid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_solutionhealthruleset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthruleset_DuplicateMatchingRecord"></a> msdyn_solutionhealthruleset_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_solutionhealthruleset msdyn_solutionhealthruleset_DuplicateMatchingRecord](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthruleset`|
|ReferencedAttribute|`msdyn_solutionhealthrulesetid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_solutionhealthruleset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_virtualtablecolumncandidate_DuplicateBaseRecord"></a> msdyn_virtualtablecolumncandidate_DuplicateBaseRecord

One-To-Many Relationship: [msdyn_virtualtablecolumncandidate msdyn_virtualtablecolumncandidate_DuplicateBaseRecord](msdyn_virtualtablecolumncandidate.md#BKMK_msdyn_virtualtablecolumncandidate_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_virtualtablecolumncandidate`|
|ReferencedAttribute|`msdyn_virtualtablecolumncandidateid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_msdyn_virtualtablecolumncandidate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_virtualtablecolumncandidate_DuplicateMatchingRecord"></a> msdyn_virtualtablecolumncandidate_DuplicateMatchingRecord

One-To-Many Relationship: [msdyn_virtualtablecolumncandidate msdyn_virtualtablecolumncandidate_DuplicateMatchingRecord](msdyn_virtualtablecolumncandidate.md#BKMK_msdyn_virtualtablecolumncandidate_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_virtualtablecolumncandidate`|
|ReferencedAttribute|`msdyn_virtualtablecolumncandidateid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_msdyn_virtualtablecolumncandidate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspcat_catalogsubmissionfiles_DuplicateBaseRecord"></a> mspcat_catalogsubmissionfiles_DuplicateBaseRecord

One-To-Many Relationship: [mspcat_catalogsubmissionfiles mspcat_catalogsubmissionfiles_DuplicateBaseRecord](mspcat_catalogsubmissionfiles.md#BKMK_mspcat_catalogsubmissionfiles_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`mspcat_catalogsubmissionfiles`|
|ReferencedAttribute|`mspcat_catalogsubmissionfilesid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_mspcat_catalogsubmissionfiles`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspcat_catalogsubmissionfiles_DuplicateMatchingRecord"></a> mspcat_catalogsubmissionfiles_DuplicateMatchingRecord

One-To-Many Relationship: [mspcat_catalogsubmissionfiles mspcat_catalogsubmissionfiles_DuplicateMatchingRecord](mspcat_catalogsubmissionfiles.md#BKMK_mspcat_catalogsubmissionfiles_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`mspcat_catalogsubmissionfiles`|
|ReferencedAttribute|`mspcat_catalogsubmissionfilesid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_mspcat_catalogsubmissionfiles`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspcat_packagestore_DuplicateBaseRecord"></a> mspcat_packagestore_DuplicateBaseRecord

One-To-Many Relationship: [mspcat_packagestore mspcat_packagestore_DuplicateBaseRecord](mspcat_packagestore.md#BKMK_mspcat_packagestore_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`mspcat_packagestore`|
|ReferencedAttribute|`mspcat_packagestoreid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_mspcat_packagestore`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspcat_packagestore_DuplicateMatchingRecord"></a> mspcat_packagestore_DuplicateMatchingRecord

One-To-Many Relationship: [mspcat_packagestore mspcat_packagestore_DuplicateMatchingRecord](mspcat_packagestore.md#BKMK_mspcat_packagestore_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`mspcat_packagestore`|
|ReferencedAttribute|`mspcat_packagestoreid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_mspcat_packagestore`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncfnostate_DuplicateBaseRecord"></a> organizationdatasyncfnostate_DuplicateBaseRecord

One-To-Many Relationship: [organizationdatasyncfnostate organizationdatasyncfnostate_DuplicateBaseRecord](organizationdatasyncfnostate.md#BKMK_organizationdatasyncfnostate_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncfnostate`|
|ReferencedAttribute|`organizationdatasyncfnostateid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_organizationdatasyncfnostate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncfnostate_DuplicateMatchingRecord"></a> organizationdatasyncfnostate_DuplicateMatchingRecord

One-To-Many Relationship: [organizationdatasyncfnostate organizationdatasyncfnostate_DuplicateMatchingRecord](organizationdatasyncfnostate.md#BKMK_organizationdatasyncfnostate_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncfnostate`|
|ReferencedAttribute|`organizationdatasyncfnostateid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_organizationdatasyncfnostate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncstate_DuplicateBaseRecord"></a> organizationdatasyncstate_DuplicateBaseRecord

One-To-Many Relationship: [organizationdatasyncstate organizationdatasyncstate_DuplicateBaseRecord](organizationdatasyncstate.md#BKMK_organizationdatasyncstate_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncstate`|
|ReferencedAttribute|`organizationdatasyncstateid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_organizationdatasyncstate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncstate_DuplicateMatchingRecord"></a> organizationdatasyncstate_DuplicateMatchingRecord

One-To-Many Relationship: [organizationdatasyncstate organizationdatasyncstate_DuplicateMatchingRecord](organizationdatasyncstate.md#BKMK_organizationdatasyncstate_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncstate`|
|ReferencedAttribute|`organizationdatasyncstateid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_organizationdatasyncstate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscription_DuplicateBaseRecord"></a> organizationdatasyncsubscription_DuplicateBaseRecord

One-To-Many Relationship: [organizationdatasyncsubscription organizationdatasyncsubscription_DuplicateBaseRecord](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscription`|
|ReferencedAttribute|`organizationdatasyncsubscriptionid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_organizationdatasyncsubscription`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscription_DuplicateMatchingRecord"></a> organizationdatasyncsubscription_DuplicateMatchingRecord

One-To-Many Relationship: [organizationdatasyncsubscription organizationdatasyncsubscription_DuplicateMatchingRecord](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscription`|
|ReferencedAttribute|`organizationdatasyncsubscriptionid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_organizationdatasyncsubscription`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscriptionentity_DuplicateBaseRecord"></a> organizationdatasyncsubscriptionentity_DuplicateBaseRecord

One-To-Many Relationship: [organizationdatasyncsubscriptionentity organizationdatasyncsubscriptionentity_DuplicateBaseRecord](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscriptionentity`|
|ReferencedAttribute|`organizationdatasyncsubscriptionentityid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_organizationdatasyncsubscriptionentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscriptionentity_DuplicateMatchingRecord"></a> organizationdatasyncsubscriptionentity_DuplicateMatchingRecord

One-To-Many Relationship: [organizationdatasyncsubscriptionentity organizationdatasyncsubscriptionentity_DuplicateMatchingRecord](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscriptionentity`|
|ReferencedAttribute|`organizationdatasyncsubscriptionentityid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_organizationdatasyncsubscriptionentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_DuplicateBaseRecord"></a> organizationdatasyncsubscriptionfnotable_DuplicateBaseRecord

One-To-Many Relationship: [organizationdatasyncsubscriptionfnotable organizationdatasyncsubscriptionfnotable_DuplicateBaseRecord](organizationdatasyncsubscriptionfnotable.md#BKMK_organizationdatasyncsubscriptionfnotable_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscriptionfnotable`|
|ReferencedAttribute|`organizationdatasyncsubscriptionfnotableid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_organizationdatasyncsubscriptionfnotable`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_DuplicateMatchingRecord"></a> organizationdatasyncsubscriptionfnotable_DuplicateMatchingRecord

One-To-Many Relationship: [organizationdatasyncsubscriptionfnotable organizationdatasyncsubscriptionfnotable_DuplicateMatchingRecord](organizationdatasyncsubscriptionfnotable.md#BKMK_organizationdatasyncsubscriptionfnotable_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscriptionfnotable`|
|ReferencedAttribute|`organizationdatasyncsubscriptionfnotableid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_organizationdatasyncsubscriptionfnotable`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_package_DuplicateBaseRecord"></a> package_DuplicateBaseRecord

One-To-Many Relationship: [package package_DuplicateBaseRecord](package.md#BKMK_package_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`package`|
|ReferencedAttribute|`packageid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_package`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_package_DuplicateMatchingRecord"></a> package_DuplicateMatchingRecord

One-To-Many Relationship: [package package_DuplicateMatchingRecord](package.md#BKMK_package_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`package`|
|ReferencedAttribute|`packageid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_package`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_packagehistory_DuplicateBaseRecord"></a> packagehistory_DuplicateBaseRecord

One-To-Many Relationship: [packagehistory packagehistory_DuplicateBaseRecord](packagehistory.md#BKMK_packagehistory_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`packagehistory`|
|ReferencedAttribute|`packagehistoryid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_packagehistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_packagehistory_DuplicateMatchingRecord"></a> packagehistory_DuplicateMatchingRecord

One-To-Many Relationship: [packagehistory packagehistory_DuplicateMatchingRecord](packagehistory.md#BKMK_packagehistory_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`packagehistory`|
|ReferencedAttribute|`packagehistoryid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_packagehistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_PhoneCall_DuplicateBaseRecord"></a> PhoneCall_DuplicateBaseRecord

One-To-Many Relationship: [phonecall PhoneCall_DuplicateBaseRecord](phonecall.md#BKMK_PhoneCall_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`phonecall`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_phonecall`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_PhoneCall_DuplicateMatchingRecord"></a> PhoneCall_DuplicateMatchingRecord

One-To-Many Relationship: [phonecall PhoneCall_DuplicateMatchingRecord](phonecall.md#BKMK_PhoneCall_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`phonecall`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_phonecall`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbidataset_DuplicateBaseRecord"></a> powerbidataset_DuplicateBaseRecord

One-To-Many Relationship: [powerbidataset powerbidataset_DuplicateBaseRecord](powerbidataset.md#BKMK_powerbidataset_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbidataset`|
|ReferencedAttribute|`powerbidatasetid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_powerbidataset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbidataset_DuplicateMatchingRecord"></a> powerbidataset_DuplicateMatchingRecord

One-To-Many Relationship: [powerbidataset powerbidataset_DuplicateMatchingRecord](powerbidataset.md#BKMK_powerbidataset_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbidataset`|
|ReferencedAttribute|`powerbidatasetid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_powerbidataset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbidatasetapdx_DuplicateBaseRecord"></a> powerbidatasetapdx_DuplicateBaseRecord

One-To-Many Relationship: [powerbidatasetapdx powerbidatasetapdx_DuplicateBaseRecord](powerbidatasetapdx.md#BKMK_powerbidatasetapdx_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbidatasetapdx`|
|ReferencedAttribute|`powerbidatasetapdxid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_powerbidatasetapdx`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbidatasetapdx_DuplicateMatchingRecord"></a> powerbidatasetapdx_DuplicateMatchingRecord

One-To-Many Relationship: [powerbidatasetapdx powerbidatasetapdx_DuplicateMatchingRecord](powerbidatasetapdx.md#BKMK_powerbidatasetapdx_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbidatasetapdx`|
|ReferencedAttribute|`powerbidatasetapdxid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_powerbidatasetapdx`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbimashupparameter_DuplicateBaseRecord"></a> powerbimashupparameter_DuplicateBaseRecord

One-To-Many Relationship: [powerbimashupparameter powerbimashupparameter_DuplicateBaseRecord](powerbimashupparameter.md#BKMK_powerbimashupparameter_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbimashupparameter`|
|ReferencedAttribute|`powerbimashupparameterid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_powerbimashupparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbimashupparameter_DuplicateMatchingRecord"></a> powerbimashupparameter_DuplicateMatchingRecord

One-To-Many Relationship: [powerbimashupparameter powerbimashupparameter_DuplicateMatchingRecord](powerbimashupparameter.md#BKMK_powerbimashupparameter_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbimashupparameter`|
|ReferencedAttribute|`powerbimashupparameterid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_powerbimashupparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbireport_DuplicateBaseRecord"></a> powerbireport_DuplicateBaseRecord

One-To-Many Relationship: [powerbireport powerbireport_DuplicateBaseRecord](powerbireport.md#BKMK_powerbireport_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbireport`|
|ReferencedAttribute|`powerbireportid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_powerbireport`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbireport_DuplicateMatchingRecord"></a> powerbireport_DuplicateMatchingRecord

One-To-Many Relationship: [powerbireport powerbireport_DuplicateMatchingRecord](powerbireport.md#BKMK_powerbireport_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbireport`|
|ReferencedAttribute|`powerbireportid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_powerbireport`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbireportapdx_DuplicateBaseRecord"></a> powerbireportapdx_DuplicateBaseRecord

One-To-Many Relationship: [powerbireportapdx powerbireportapdx_DuplicateBaseRecord](powerbireportapdx.md#BKMK_powerbireportapdx_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbireportapdx`|
|ReferencedAttribute|`powerbireportapdxid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_powerbireportapdx`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbireportapdx_DuplicateMatchingRecord"></a> powerbireportapdx_DuplicateMatchingRecord

One-To-Many Relationship: [powerbireportapdx powerbireportapdx_DuplicateMatchingRecord](powerbireportapdx.md#BKMK_powerbireportapdx_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbireportapdx`|
|ReferencedAttribute|`powerbireportapdxid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_powerbireportapdx`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerfxrule_DuplicateBaseRecord"></a> powerfxrule_DuplicateBaseRecord

One-To-Many Relationship: [powerfxrule powerfxrule_DuplicateBaseRecord](powerfxrule.md#BKMK_powerfxrule_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`powerfxrule`|
|ReferencedAttribute|`powerfxruleid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_powerfxrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerfxrule_DuplicateMatchingRecord"></a> powerfxrule_DuplicateMatchingRecord

One-To-Many Relationship: [powerfxrule powerfxrule_DuplicateMatchingRecord](powerfxrule.md#BKMK_powerfxrule_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`powerfxrule`|
|ReferencedAttribute|`powerfxruleid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_powerfxrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesddosalert_DuplicateBaseRecord"></a> powerpagesddosalert_DuplicateBaseRecord

One-To-Many Relationship: [powerpagesddosalert powerpagesddosalert_DuplicateBaseRecord](powerpagesddosalert.md#BKMK_powerpagesddosalert_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesddosalert`|
|ReferencedAttribute|`powerpagesddosalertid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_powerpagesddosalert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesddosalert_DuplicateMatchingRecord"></a> powerpagesddosalert_DuplicateMatchingRecord

One-To-Many Relationship: [powerpagesddosalert powerpagesddosalert_DuplicateMatchingRecord](powerpagesddosalert.md#BKMK_powerpagesddosalert_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesddosalert`|
|ReferencedAttribute|`powerpagesddosalertid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_powerpagesddosalert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesmanagedidentity_DuplicateBaseRecord"></a> powerpagesmanagedidentity_DuplicateBaseRecord

One-To-Many Relationship: [powerpagesmanagedidentity powerpagesmanagedidentity_DuplicateBaseRecord](powerpagesmanagedidentity.md#BKMK_powerpagesmanagedidentity_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesmanagedidentity`|
|ReferencedAttribute|`powerpagesmanagedidentityid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_powerpagesmanagedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesmanagedidentity_DuplicateMatchingRecord"></a> powerpagesmanagedidentity_DuplicateMatchingRecord

One-To-Many Relationship: [powerpagesmanagedidentity powerpagesmanagedidentity_DuplicateMatchingRecord](powerpagesmanagedidentity.md#BKMK_powerpagesmanagedidentity_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesmanagedidentity`|
|ReferencedAttribute|`powerpagesmanagedidentityid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_powerpagesmanagedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesscanreport_DuplicateBaseRecord"></a> powerpagesscanreport_DuplicateBaseRecord

One-To-Many Relationship: [powerpagesscanreport powerpagesscanreport_DuplicateBaseRecord](powerpagesscanreport.md#BKMK_powerpagesscanreport_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesscanreport`|
|ReferencedAttribute|`powerpagesscanreportid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_powerpagesscanreport`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesscanreport_DuplicateMatchingRecord"></a> powerpagesscanreport_DuplicateMatchingRecord

One-To-Many Relationship: [powerpagesscanreport powerpagesscanreport_DuplicateMatchingRecord](powerpagesscanreport.md#BKMK_powerpagesscanreport_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesscanreport`|
|ReferencedAttribute|`powerpagesscanreportid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_powerpagesscanreport`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegesremovalsetting_DuplicateBaseRecord"></a> privilegesremovalsetting_DuplicateBaseRecord

One-To-Many Relationship: [privilegesremovalsetting privilegesremovalsetting_DuplicateBaseRecord](privilegesremovalsetting.md#BKMK_privilegesremovalsetting_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegesremovalsetting`|
|ReferencedAttribute|`privilegesremovalsettingid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_privilegesremovalsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegesremovalsetting_DuplicateMatchingRecord"></a> privilegesremovalsetting_DuplicateMatchingRecord

One-To-Many Relationship: [privilegesremovalsetting privilegesremovalsetting_DuplicateMatchingRecord](privilegesremovalsetting.md#BKMK_privilegesremovalsetting_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegesremovalsetting`|
|ReferencedAttribute|`privilegesremovalsettingid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_privilegesremovalsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Publisher_DuplicateBaseRecord"></a> Publisher_DuplicateBaseRecord

One-To-Many Relationship: [publisher Publisher_DuplicateBaseRecord](publisher.md#BKMK_Publisher_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`publisher`|
|ReferencedAttribute|`publisherid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_publisher`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Publisher_DuplicateMatchingRecord"></a> Publisher_DuplicateMatchingRecord

One-To-Many Relationship: [publisher Publisher_DuplicateMatchingRecord](publisher.md#BKMK_Publisher_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`publisher`|
|ReferencedAttribute|`publisherid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_publisher`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_purviewlabelinfo_DuplicateBaseRecord"></a> purviewlabelinfo_DuplicateBaseRecord

One-To-Many Relationship: [purviewlabelinfo purviewlabelinfo_DuplicateBaseRecord](purviewlabelinfo.md#BKMK_purviewlabelinfo_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`purviewlabelinfo`|
|ReferencedAttribute|`purviewlabelinfoid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_purviewlabelinfo`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_purviewlabelinfo_DuplicateMatchingRecord"></a> purviewlabelinfo_DuplicateMatchingRecord

One-To-Many Relationship: [purviewlabelinfo purviewlabelinfo_DuplicateMatchingRecord](purviewlabelinfo.md#BKMK_purviewlabelinfo_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`purviewlabelinfo`|
|ReferencedAttribute|`purviewlabelinfoid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_purviewlabelinfo`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_purviewlabelsynccache_DuplicateBaseRecord"></a> purviewlabelsynccache_DuplicateBaseRecord

One-To-Many Relationship: [purviewlabelsynccache purviewlabelsynccache_DuplicateBaseRecord](purviewlabelsynccache.md#BKMK_purviewlabelsynccache_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`purviewlabelsynccache`|
|ReferencedAttribute|`purviewlabelsynccacheid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_purviewlabelsynccache`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_purviewlabelsynccache_DuplicateMatchingRecord"></a> purviewlabelsynccache_DuplicateMatchingRecord

One-To-Many Relationship: [purviewlabelsynccache purviewlabelsynccache_DuplicateMatchingRecord](purviewlabelsynccache.md#BKMK_purviewlabelsynccache_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`purviewlabelsynccache`|
|ReferencedAttribute|`purviewlabelsynccacheid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_purviewlabelsynccache`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Queue_DuplicateBaseRecord"></a> Queue_DuplicateBaseRecord

One-To-Many Relationship: [queue Queue_DuplicateBaseRecord](queue.md#BKMK_Queue_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`queue`|
|ReferencedAttribute|`queueid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_queue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Queue_DuplicateMatchingRecord"></a> Queue_DuplicateMatchingRecord

One-To-Many Relationship: [queue Queue_DuplicateMatchingRecord](queue.md#BKMK_Queue_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`queue`|
|ReferencedAttribute|`queueid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_queue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recordfilter_DuplicateBaseRecord"></a> recordfilter_DuplicateBaseRecord

One-To-Many Relationship: [recordfilter recordfilter_DuplicateBaseRecord](recordfilter.md#BKMK_recordfilter_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`recordfilter`|
|ReferencedAttribute|`recordfilterid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_recordfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recordfilter_DuplicateMatchingRecord"></a> recordfilter_DuplicateMatchingRecord

One-To-Many Relationship: [recordfilter recordfilter_DuplicateMatchingRecord](recordfilter.md#BKMK_recordfilter_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`recordfilter`|
|ReferencedAttribute|`recordfilterid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_recordfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_RecurringAppointmentMaster_DuplicateBaseRecord"></a> RecurringAppointmentMaster_DuplicateBaseRecord

One-To-Many Relationship: [recurringappointmentmaster RecurringAppointmentMaster_DuplicateBaseRecord](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`recurringappointmentmaster`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_RecurringAppointmentMaster_DuplicateMatchingRecord"></a> RecurringAppointmentMaster_DuplicateMatchingRecord

One-To-Many Relationship: [recurringappointmentmaster RecurringAppointmentMaster_DuplicateMatchingRecord](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`recurringappointmentmaster`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_reportparameter_DuplicateBaseRecord"></a> reportparameter_DuplicateBaseRecord

One-To-Many Relationship: [reportparameter reportparameter_DuplicateBaseRecord](reportparameter.md#BKMK_reportparameter_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`reportparameter`|
|ReferencedAttribute|`reportparameterid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_reportparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_reportparameter_DuplicateMatchingRecord"></a> reportparameter_DuplicateMatchingRecord

One-To-Many Relationship: [reportparameter reportparameter_DuplicateMatchingRecord](reportparameter.md#BKMK_reportparameter_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`reportparameter`|
|ReferencedAttribute|`reportparameterid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_reportparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retaineddataexcel_DuplicateBaseRecord"></a> retaineddataexcel_DuplicateBaseRecord

One-To-Many Relationship: [retaineddataexcel retaineddataexcel_DuplicateBaseRecord](retaineddataexcel.md#BKMK_retaineddataexcel_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`retaineddataexcel`|
|ReferencedAttribute|`retaineddataexcelid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_retaineddataexcel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retaineddataexcel_DuplicateMatchingRecord"></a> retaineddataexcel_DuplicateMatchingRecord

One-To-Many Relationship: [retaineddataexcel retaineddataexcel_DuplicateMatchingRecord](retaineddataexcel.md#BKMK_retaineddataexcel_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`retaineddataexcel`|
|ReferencedAttribute|`retaineddataexcelid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_retaineddataexcel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionconfig_DuplicateBaseRecord"></a> retentionconfig_DuplicateBaseRecord

One-To-Many Relationship: [retentionconfig retentionconfig_DuplicateBaseRecord](retentionconfig.md#BKMK_retentionconfig_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionconfig`|
|ReferencedAttribute|`retentionconfigid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_retentionconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionconfig_DuplicateMatchingRecord"></a> retentionconfig_DuplicateMatchingRecord

One-To-Many Relationship: [retentionconfig retentionconfig_DuplicateMatchingRecord](retentionconfig.md#BKMK_retentionconfig_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionconfig`|
|ReferencedAttribute|`retentionconfigid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_retentionconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionfailuredetail_DuplicateBaseRecord"></a> retentionfailuredetail_DuplicateBaseRecord

One-To-Many Relationship: [retentionfailuredetail retentionfailuredetail_DuplicateBaseRecord](retentionfailuredetail.md#BKMK_retentionfailuredetail_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionfailuredetail`|
|ReferencedAttribute|`retentionfailuredetailid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_retentionfailuredetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionfailuredetail_DuplicateMatchingRecord"></a> retentionfailuredetail_DuplicateMatchingRecord

One-To-Many Relationship: [retentionfailuredetail retentionfailuredetail_DuplicateMatchingRecord](retentionfailuredetail.md#BKMK_retentionfailuredetail_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionfailuredetail`|
|ReferencedAttribute|`retentionfailuredetailid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_retentionfailuredetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionoperation_DuplicateBaseRecord"></a> retentionoperation_DuplicateBaseRecord

One-To-Many Relationship: [retentionoperation retentionoperation_DuplicateBaseRecord](retentionoperation.md#BKMK_retentionoperation_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionoperation`|
|ReferencedAttribute|`retentionoperationid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_retentionoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionoperation_DuplicateMatchingRecord"></a> retentionoperation_DuplicateMatchingRecord

One-To-Many Relationship: [retentionoperation retentionoperation_DuplicateMatchingRecord](retentionoperation.md#BKMK_retentionoperation_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionoperation`|
|ReferencedAttribute|`retentionoperationid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_retentionoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionsuccessdetail_DuplicateBaseRecord"></a> retentionsuccessdetail_DuplicateBaseRecord

One-To-Many Relationship: [retentionsuccessdetail retentionsuccessdetail_DuplicateBaseRecord](retentionsuccessdetail.md#BKMK_retentionsuccessdetail_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionsuccessdetail`|
|ReferencedAttribute|`retentionsuccessdetailid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_retentionsuccessdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionsuccessdetail_DuplicateMatchingRecord"></a> retentionsuccessdetail_DuplicateMatchingRecord

One-To-Many Relationship: [retentionsuccessdetail retentionsuccessdetail_DuplicateMatchingRecord](retentionsuccessdetail.md#BKMK_retentionsuccessdetail_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionsuccessdetail`|
|ReferencedAttribute|`retentionsuccessdetailid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_retentionsuccessdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_roleeditorlayout_DuplicateBaseRecord"></a> roleeditorlayout_DuplicateBaseRecord

One-To-Many Relationship: [roleeditorlayout roleeditorlayout_DuplicateBaseRecord](roleeditorlayout.md#BKMK_roleeditorlayout_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`roleeditorlayout`|
|ReferencedAttribute|`roleeditorlayoutid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_roleeditorlayout`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_roleeditorlayout_DuplicateMatchingRecord"></a> roleeditorlayout_DuplicateMatchingRecord

One-To-Many Relationship: [roleeditorlayout roleeditorlayout_DuplicateMatchingRecord](roleeditorlayout.md#BKMK_roleeditorlayout_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`roleeditorlayout`|
|ReferencedAttribute|`roleeditorlayoutid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_roleeditorlayout`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_savingrule_DuplicateBaseRecord"></a> savingrule_DuplicateBaseRecord

One-To-Many Relationship: [savingrule savingrule_DuplicateBaseRecord](savingrule.md#BKMK_savingrule_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`savingrule`|
|ReferencedAttribute|`savingruleid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_savingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_savingrule_DuplicateMatchingRecord"></a> savingrule_DuplicateMatchingRecord

One-To-Many Relationship: [savingrule savingrule_DuplicateMatchingRecord](savingrule.md#BKMK_savingrule_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`savingrule`|
|ReferencedAttribute|`savingruleid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_savingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchattributesettings_DuplicateBaseRecord"></a> searchattributesettings_DuplicateBaseRecord

One-To-Many Relationship: [searchattributesettings searchattributesettings_DuplicateBaseRecord](searchattributesettings.md#BKMK_searchattributesettings_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`searchattributesettings`|
|ReferencedAttribute|`searchattributesettingsid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_searchattributesettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchattributesettings_DuplicateMatchingRecord"></a> searchattributesettings_DuplicateMatchingRecord

One-To-Many Relationship: [searchattributesettings searchattributesettings_DuplicateMatchingRecord](searchattributesettings.md#BKMK_searchattributesettings_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`searchattributesettings`|
|ReferencedAttribute|`searchattributesettingsid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_searchattributesettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchcustomanalyzer_DuplicateBaseRecord"></a> searchcustomanalyzer_DuplicateBaseRecord

One-To-Many Relationship: [searchcustomanalyzer searchcustomanalyzer_DuplicateBaseRecord](searchcustomanalyzer.md#BKMK_searchcustomanalyzer_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`searchcustomanalyzer`|
|ReferencedAttribute|`searchcustomanalyzerid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_searchcustomanalyzer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchcustomanalyzer_DuplicateMatchingRecord"></a> searchcustomanalyzer_DuplicateMatchingRecord

One-To-Many Relationship: [searchcustomanalyzer searchcustomanalyzer_DuplicateMatchingRecord](searchcustomanalyzer.md#BKMK_searchcustomanalyzer_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`searchcustomanalyzer`|
|ReferencedAttribute|`searchcustomanalyzerid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_searchcustomanalyzer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchrelationshipsettings_DuplicateBaseRecord"></a> searchrelationshipsettings_DuplicateBaseRecord

One-To-Many Relationship: [searchrelationshipsettings searchrelationshipsettings_DuplicateBaseRecord](searchrelationshipsettings.md#BKMK_searchrelationshipsettings_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`searchrelationshipsettings`|
|ReferencedAttribute|`searchrelationshipsettingsid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_searchrelationshipsettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchrelationshipsettings_DuplicateMatchingRecord"></a> searchrelationshipsettings_DuplicateMatchingRecord

One-To-Many Relationship: [searchrelationshipsettings searchrelationshipsettings_DuplicateMatchingRecord](searchrelationshipsettings.md#BKMK_searchrelationshipsettings_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`searchrelationshipsettings`|
|ReferencedAttribute|`searchrelationshipsettingsid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_searchrelationshipsettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sensitivitylabelattributemapping_DuplicateBaseRecord"></a> sensitivitylabelattributemapping_DuplicateBaseRecord

One-To-Many Relationship: [sensitivitylabelattributemapping sensitivitylabelattributemapping_DuplicateBaseRecord](sensitivitylabelattributemapping.md#BKMK_sensitivitylabelattributemapping_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`sensitivitylabelattributemapping`|
|ReferencedAttribute|`sensitivitylabelattributemappingid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_sensitivitylabelattributemapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sensitivitylabelattributemapping_DuplicateMatchingRecord"></a> sensitivitylabelattributemapping_DuplicateMatchingRecord

One-To-Many Relationship: [sensitivitylabelattributemapping sensitivitylabelattributemapping_DuplicateMatchingRecord](sensitivitylabelattributemapping.md#BKMK_sensitivitylabelattributemapping_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`sensitivitylabelattributemapping`|
|ReferencedAttribute|`sensitivitylabelattributemappingid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_sensitivitylabelattributemapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_serviceplan_DuplicateBaseRecord"></a> serviceplan_DuplicateBaseRecord

One-To-Many Relationship: [serviceplan serviceplan_DuplicateBaseRecord](serviceplan.md#BKMK_serviceplan_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`serviceplan`|
|ReferencedAttribute|`serviceplanid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_serviceplan`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_serviceplan_DuplicateMatchingRecord"></a> serviceplan_DuplicateMatchingRecord

One-To-Many Relationship: [serviceplan serviceplan_DuplicateMatchingRecord](serviceplan.md#BKMK_serviceplan_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`serviceplan`|
|ReferencedAttribute|`serviceplanid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_serviceplan`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_serviceplanmapping_DuplicateBaseRecord"></a> serviceplanmapping_DuplicateBaseRecord

One-To-Many Relationship: [serviceplanmapping serviceplanmapping_DuplicateBaseRecord](serviceplanmapping.md#BKMK_serviceplanmapping_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`serviceplanmapping`|
|ReferencedAttribute|`serviceplanmappingid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_serviceplanmapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_serviceplanmapping_DuplicateMatchingRecord"></a> serviceplanmapping_DuplicateMatchingRecord

One-To-Many Relationship: [serviceplanmapping serviceplanmapping_DuplicateMatchingRecord](serviceplanmapping.md#BKMK_serviceplanmapping_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`serviceplanmapping`|
|ReferencedAttribute|`serviceplanmappingid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_serviceplanmapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedlinksetting_DuplicateBaseRecord"></a> sharedlinksetting_DuplicateBaseRecord

One-To-Many Relationship: [sharedlinksetting sharedlinksetting_DuplicateBaseRecord](sharedlinksetting.md#BKMK_sharedlinksetting_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedlinksetting`|
|ReferencedAttribute|`sharedlinksettingid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_sharedlinksetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedlinksetting_DuplicateMatchingRecord"></a> sharedlinksetting_DuplicateMatchingRecord

One-To-Many Relationship: [sharedlinksetting sharedlinksetting_DuplicateMatchingRecord](sharedlinksetting.md#BKMK_sharedlinksetting_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedlinksetting`|
|ReferencedAttribute|`sharedlinksettingid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_sharedlinksetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SharePointDocumentLocation_DuplicateBaseRecord"></a> SharePointDocumentLocation_DuplicateBaseRecord

One-To-Many Relationship: [sharepointdocumentlocation SharePointDocumentLocation_DuplicateBaseRecord](sharepointdocumentlocation.md#BKMK_SharePointDocumentLocation_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`sharepointdocumentlocation`|
|ReferencedAttribute|`sharepointdocumentlocationid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_sharepointdocumentlocation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SharePointDocumentLocation_DuplicateMatchingRecord"></a> SharePointDocumentLocation_DuplicateMatchingRecord

One-To-Many Relationship: [sharepointdocumentlocation SharePointDocumentLocation_DuplicateMatchingRecord](sharepointdocumentlocation.md#BKMK_SharePointDocumentLocation_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`sharepointdocumentlocation`|
|ReferencedAttribute|`sharepointdocumentlocationid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_sharepointdocumentlocation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SharePointSite_DuplicateBaseRecord"></a> SharePointSite_DuplicateBaseRecord

One-To-Many Relationship: [sharepointsite SharePointSite_DuplicateBaseRecord](sharepointsite.md#BKMK_SharePointSite_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`sharepointsite`|
|ReferencedAttribute|`sharepointsiteid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_sharepointsite`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SharePointSite_DuplicateMatchingRecord"></a> SharePointSite_DuplicateMatchingRecord

One-To-Many Relationship: [sharepointsite SharePointSite_DuplicateMatchingRecord](sharepointsite.md#BKMK_SharePointSite_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`sharepointsite`|
|ReferencedAttribute|`sharepointsiteid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_sharepointsite`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SocialActivity_DuplicateBaseRecord"></a> SocialActivity_DuplicateBaseRecord

One-To-Many Relationship: [socialactivity SocialActivity_DuplicateBaseRecord](socialactivity.md#BKMK_SocialActivity_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`socialactivity`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_socialactivity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SocialActivity_DuplicateMatchingRecord"></a> SocialActivity_DuplicateMatchingRecord

One-To-Many Relationship: [socialactivity SocialActivity_DuplicateMatchingRecord](socialactivity.md#BKMK_SocialActivity_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`socialactivity`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_socialactivity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SocialProfile_DuplicateBaseRecord"></a> SocialProfile_DuplicateBaseRecord

One-To-Many Relationship: [socialprofile SocialProfile_DuplicateBaseRecord](socialprofile.md#BKMK_SocialProfile_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`socialprofile`|
|ReferencedAttribute|`socialprofileid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_socialprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SocialProfile_DuplicateMatchingRecord"></a> SocialProfile_DuplicateMatchingRecord

One-To-Many Relationship: [socialprofile SocialProfile_DuplicateMatchingRecord](socialprofile.md#BKMK_SocialProfile_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`socialprofile`|
|ReferencedAttribute|`socialprofileid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_socialprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentattributeconfiguration_DuplicateBaseRecord"></a> solutioncomponentattributeconfiguration_DuplicateBaseRecord

One-To-Many Relationship: [solutioncomponentattributeconfiguration solutioncomponentattributeconfiguration_DuplicateBaseRecord](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentattributeconfiguration`|
|ReferencedAttribute|`solutioncomponentattributeconfigurationid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_solutioncomponentattributeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentattributeconfiguration_DuplicateMatchingRecord"></a> solutioncomponentattributeconfiguration_DuplicateMatchingRecord

One-To-Many Relationship: [solutioncomponentattributeconfiguration solutioncomponentattributeconfiguration_DuplicateMatchingRecord](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentattributeconfiguration`|
|ReferencedAttribute|`solutioncomponentattributeconfigurationid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_solutioncomponentattributeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentbatchconfiguration_DuplicateBaseRecord"></a> solutioncomponentbatchconfiguration_DuplicateBaseRecord

One-To-Many Relationship: [solutioncomponentbatchconfiguration solutioncomponentbatchconfiguration_DuplicateBaseRecord](solutioncomponentbatchconfiguration.md#BKMK_solutioncomponentbatchconfiguration_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentbatchconfiguration`|
|ReferencedAttribute|`solutioncomponentbatchconfigurationid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_solutioncomponentbatchconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentbatchconfiguration_DuplicateMatchingRecord"></a> solutioncomponentbatchconfiguration_DuplicateMatchingRecord

One-To-Many Relationship: [solutioncomponentbatchconfiguration solutioncomponentbatchconfiguration_DuplicateMatchingRecord](solutioncomponentbatchconfiguration.md#BKMK_solutioncomponentbatchconfiguration_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentbatchconfiguration`|
|ReferencedAttribute|`solutioncomponentbatchconfigurationid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_solutioncomponentbatchconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentconfiguration_DuplicateBaseRecord"></a> solutioncomponentconfiguration_DuplicateBaseRecord

One-To-Many Relationship: [solutioncomponentconfiguration solutioncomponentconfiguration_DuplicateBaseRecord](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentconfiguration`|
|ReferencedAttribute|`solutioncomponentconfigurationid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_solutioncomponentconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentconfiguration_DuplicateMatchingRecord"></a> solutioncomponentconfiguration_DuplicateMatchingRecord

One-To-Many Relationship: [solutioncomponentconfiguration solutioncomponentconfiguration_DuplicateMatchingRecord](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentconfiguration`|
|ReferencedAttribute|`solutioncomponentconfigurationid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_solutioncomponentconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentrelationshipconfiguration_DuplicateBaseRecord"></a> solutioncomponentrelationshipconfiguration_DuplicateBaseRecord

One-To-Many Relationship: [solutioncomponentrelationshipconfiguration solutioncomponentrelationshipconfiguration_DuplicateBaseRecord](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentrelationshipconfiguration`|
|ReferencedAttribute|`solutioncomponentrelationshipconfigurationid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_solutioncomponentrelationshipconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord"></a> solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord

One-To-Many Relationship: [solutioncomponentrelationshipconfiguration solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentrelationshipconfiguration`|
|ReferencedAttribute|`solutioncomponentrelationshipconfigurationid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_solutioncomponentrelationshipconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagesolutionupload_DuplicateBaseRecord"></a> stagesolutionupload_DuplicateBaseRecord

One-To-Many Relationship: [stagesolutionupload stagesolutionupload_DuplicateBaseRecord](stagesolutionupload.md#BKMK_stagesolutionupload_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`stagesolutionupload`|
|ReferencedAttribute|`stagesolutionuploadid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_stagesolutionupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagesolutionupload_DuplicateMatchingRecord"></a> stagesolutionupload_DuplicateMatchingRecord

One-To-Many Relationship: [stagesolutionupload stagesolutionupload_DuplicateMatchingRecord](stagesolutionupload.md#BKMK_stagesolutionupload_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`stagesolutionupload`|
|ReferencedAttribute|`stagesolutionuploadid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_stagesolutionupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_supportusertable_DuplicateBaseRecord"></a> supportusertable_DuplicateBaseRecord

One-To-Many Relationship: [supportusertable supportusertable_DuplicateBaseRecord](supportusertable.md#BKMK_supportusertable_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`supportusertable`|
|ReferencedAttribute|`supportusertableid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_supportusertable`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_supportusertable_DuplicateMatchingRecord"></a> supportusertable_DuplicateMatchingRecord

One-To-Many Relationship: [supportusertable supportusertable_DuplicateMatchingRecord](supportusertable.md#BKMK_supportusertable_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`supportusertable`|
|ReferencedAttribute|`supportusertableid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_supportusertable`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapsedatabase_DuplicateBaseRecord"></a> synapsedatabase_DuplicateBaseRecord

One-To-Many Relationship: [synapsedatabase synapsedatabase_DuplicateBaseRecord](synapsedatabase.md#BKMK_synapsedatabase_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`synapsedatabase`|
|ReferencedAttribute|`synapsedatabaseid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_synapsedatabase`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapsedatabase_DuplicateMatchingRecord"></a> synapsedatabase_DuplicateMatchingRecord

One-To-Many Relationship: [synapsedatabase synapsedatabase_DuplicateMatchingRecord](synapsedatabase.md#BKMK_synapsedatabase_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`synapsedatabase`|
|ReferencedAttribute|`synapsedatabaseid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_synapsedatabase`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkexternaltablestate_DuplicateBaseRecord"></a> synapselinkexternaltablestate_DuplicateBaseRecord

One-To-Many Relationship: [synapselinkexternaltablestate synapselinkexternaltablestate_DuplicateBaseRecord](synapselinkexternaltablestate.md#BKMK_synapselinkexternaltablestate_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkexternaltablestate`|
|ReferencedAttribute|`synapselinkexternaltablestateid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_synapselinkexternaltablestate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkexternaltablestate_DuplicateMatchingRecord"></a> synapselinkexternaltablestate_DuplicateMatchingRecord

One-To-Many Relationship: [synapselinkexternaltablestate synapselinkexternaltablestate_DuplicateMatchingRecord](synapselinkexternaltablestate.md#BKMK_synapselinkexternaltablestate_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkexternaltablestate`|
|ReferencedAttribute|`synapselinkexternaltablestateid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_synapselinkexternaltablestate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofile_DuplicateBaseRecord"></a> synapselinkprofile_DuplicateBaseRecord

One-To-Many Relationship: [synapselinkprofile synapselinkprofile_DuplicateBaseRecord](synapselinkprofile.md#BKMK_synapselinkprofile_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofile`|
|ReferencedAttribute|`synapselinkprofileid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_synapselinkprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofile_DuplicateMatchingRecord"></a> synapselinkprofile_DuplicateMatchingRecord

One-To-Many Relationship: [synapselinkprofile synapselinkprofile_DuplicateMatchingRecord](synapselinkprofile.md#BKMK_synapselinkprofile_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofile`|
|ReferencedAttribute|`synapselinkprofileid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_synapselinkprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofileentity_DuplicateBaseRecord"></a> synapselinkprofileentity_DuplicateBaseRecord

One-To-Many Relationship: [synapselinkprofileentity synapselinkprofileentity_DuplicateBaseRecord](synapselinkprofileentity.md#BKMK_synapselinkprofileentity_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofileentity`|
|ReferencedAttribute|`synapselinkprofileentityid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_synapselinkprofileentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofileentity_DuplicateMatchingRecord"></a> synapselinkprofileentity_DuplicateMatchingRecord

One-To-Many Relationship: [synapselinkprofileentity synapselinkprofileentity_DuplicateMatchingRecord](synapselinkprofileentity.md#BKMK_synapselinkprofileentity_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofileentity`|
|ReferencedAttribute|`synapselinkprofileentityid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_synapselinkprofileentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofileentitystate_DuplicateBaseRecord"></a> synapselinkprofileentitystate_DuplicateBaseRecord

One-To-Many Relationship: [synapselinkprofileentitystate synapselinkprofileentitystate_DuplicateBaseRecord](synapselinkprofileentitystate.md#BKMK_synapselinkprofileentitystate_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofileentitystate`|
|ReferencedAttribute|`synapselinkprofileentitystateid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_synapselinkprofileentitystate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofileentitystate_DuplicateMatchingRecord"></a> synapselinkprofileentitystate_DuplicateMatchingRecord

One-To-Many Relationship: [synapselinkprofileentitystate synapselinkprofileentitystate_DuplicateMatchingRecord](synapselinkprofileentitystate.md#BKMK_synapselinkprofileentitystate_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofileentitystate`|
|ReferencedAttribute|`synapselinkprofileentitystateid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_synapselinkprofileentitystate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkschedule_DuplicateBaseRecord"></a> synapselinkschedule_DuplicateBaseRecord

One-To-Many Relationship: [synapselinkschedule synapselinkschedule_DuplicateBaseRecord](synapselinkschedule.md#BKMK_synapselinkschedule_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkschedule`|
|ReferencedAttribute|`synapselinkscheduleid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_synapselinkschedule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkschedule_DuplicateMatchingRecord"></a> synapselinkschedule_DuplicateMatchingRecord

One-To-Many Relationship: [synapselinkschedule synapselinkschedule_DuplicateMatchingRecord](synapselinkschedule.md#BKMK_synapselinkschedule_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkschedule`|
|ReferencedAttribute|`synapselinkscheduleid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_synapselinkschedule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SystemUser_DuplicateBaseRecord"></a> SystemUser_DuplicateBaseRecord

One-To-Many Relationship: [systemuser SystemUser_DuplicateBaseRecord](systemuser.md#BKMK_SystemUser_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_systemuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SystemUser_DuplicateMatchingRecord"></a> SystemUser_DuplicateMatchingRecord

One-To-Many Relationship: [systemuser SystemUser_DuplicateMatchingRecord](systemuser.md#BKMK_SystemUser_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_systemuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Task_DuplicateBaseRecord"></a> Task_DuplicateBaseRecord

One-To-Many Relationship: [task Task_DuplicateBaseRecord](task.md#BKMK_Task_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`task`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_task`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Task_DuplicateMatchingRecord"></a> Task_DuplicateMatchingRecord

One-To-Many Relationship: [task Task_DuplicateMatchingRecord](task.md#BKMK_Task_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`task`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_task`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Team_DuplicateBaseRecord"></a> Team_DuplicateBaseRecord

One-To-Many Relationship: [team Team_DuplicateBaseRecord](team.md#BKMK_Team_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_team`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Team_DuplicateMatchingRecord"></a> Team_DuplicateMatchingRecord

One-To-Many Relationship: [team Team_DuplicateMatchingRecord](team.md#BKMK_Team_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_team`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_DuplicateBaseRecord"></a> TransactionCurrency_DuplicateBaseRecord

One-To-Many Relationship: [transactioncurrency TransactionCurrency_DuplicateBaseRecord](transactioncurrency.md#BKMK_TransactionCurrency_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_transactioncurrency`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_DuplicateMatchingRecord"></a> TransactionCurrency_DuplicateMatchingRecord

One-To-Many Relationship: [transactioncurrency TransactionCurrency_DuplicateMatchingRecord](transactioncurrency.md#BKMK_TransactionCurrency_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_transactioncurrency`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_unstructuredfilesearchentity_DuplicateBaseRecord"></a> unstructuredfilesearchentity_DuplicateBaseRecord

One-To-Many Relationship: [unstructuredfilesearchentity unstructuredfilesearchentity_DuplicateBaseRecord](unstructuredfilesearchentity.md#BKMK_unstructuredfilesearchentity_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`unstructuredfilesearchentity`|
|ReferencedAttribute|`unstructuredfilesearchentityid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_unstructuredfilesearchentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_unstructuredfilesearchentity_DuplicateMatchingRecord"></a> unstructuredfilesearchentity_DuplicateMatchingRecord

One-To-Many Relationship: [unstructuredfilesearchentity unstructuredfilesearchentity_DuplicateMatchingRecord](unstructuredfilesearchentity.md#BKMK_unstructuredfilesearchentity_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`unstructuredfilesearchentity`|
|ReferencedAttribute|`unstructuredfilesearchentityid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_unstructuredfilesearchentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_unstructuredfilesearchrecord_DuplicateBaseRecord"></a> unstructuredfilesearchrecord_DuplicateBaseRecord

One-To-Many Relationship: [unstructuredfilesearchrecord unstructuredfilesearchrecord_DuplicateBaseRecord](unstructuredfilesearchrecord.md#BKMK_unstructuredfilesearchrecord_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`unstructuredfilesearchrecord`|
|ReferencedAttribute|`unstructuredfilesearchrecordid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_unstructuredfilesearchrecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_unstructuredfilesearchrecord_DuplicateMatchingRecord"></a> unstructuredfilesearchrecord_DuplicateMatchingRecord

One-To-Many Relationship: [unstructuredfilesearchrecord unstructuredfilesearchrecord_DuplicateMatchingRecord](unstructuredfilesearchrecord.md#BKMK_unstructuredfilesearchrecord_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`unstructuredfilesearchrecord`|
|ReferencedAttribute|`unstructuredfilesearchrecordid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_unstructuredfilesearchrecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_userrating_DuplicateBaseRecord"></a> userrating_DuplicateBaseRecord

One-To-Many Relationship: [userrating userrating_DuplicateBaseRecord](userrating.md#BKMK_userrating_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`userrating`|
|ReferencedAttribute|`userratingid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_userrating`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_userrating_DuplicateMatchingRecord"></a> userrating_DuplicateMatchingRecord

One-To-Many Relationship: [userrating userrating_DuplicateMatchingRecord](userrating.md#BKMK_userrating_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`userrating`|
|ReferencedAttribute|`userratingid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_userrating`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflowmetadata_DuplicateBaseRecord"></a> workflowmetadata_DuplicateBaseRecord

One-To-Many Relationship: [workflowmetadata workflowmetadata_DuplicateBaseRecord](workflowmetadata.md#BKMK_workflowmetadata_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`workflowmetadata`|
|ReferencedAttribute|`workflowmetadataid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_workflowmetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflowmetadata_DuplicateMatchingRecord"></a> workflowmetadata_DuplicateMatchingRecord

One-To-Many Relationship: [workflowmetadata workflowmetadata_DuplicateMatchingRecord](workflowmetadata.md#BKMK_workflowmetadata_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`workflowmetadata`|
|ReferencedAttribute|`workflowmetadataid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_workflowmetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workqueue_DuplicateBaseRecord"></a> workqueue_DuplicateBaseRecord

One-To-Many Relationship: [workqueue workqueue_DuplicateBaseRecord](workqueue.md#BKMK_workqueue_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`workqueue`|
|ReferencedAttribute|`workqueueid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_workqueue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workqueue_DuplicateMatchingRecord"></a> workqueue_DuplicateMatchingRecord

One-To-Many Relationship: [workqueue workqueue_DuplicateMatchingRecord](workqueue.md#BKMK_workqueue_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`workqueue`|
|ReferencedAttribute|`workqueueid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_workqueue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workqueueitem_DuplicateBaseRecord"></a> workqueueitem_DuplicateBaseRecord

One-To-Many Relationship: [workqueueitem workqueueitem_DuplicateBaseRecord](workqueueitem.md#BKMK_workqueueitem_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`workqueueitem`|
|ReferencedAttribute|`workqueueitemid`|
|ReferencingAttribute|`baserecordid`|
|ReferencingEntityNavigationPropertyName|`baserecordid_workqueueitem`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workqueueitem_DuplicateMatchingRecord"></a> workqueueitem_DuplicateMatchingRecord

One-To-Many Relationship: [workqueueitem workqueueitem_DuplicateMatchingRecord](workqueueitem.md#BKMK_workqueueitem_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`workqueueitem`|
|ReferencedAttribute|`workqueueitemid`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencingEntityNavigationPropertyName|`duplicaterecordid_workqueueitem`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.duplicaterecord?displayProperty=fullName>
