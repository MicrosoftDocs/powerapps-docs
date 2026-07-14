---
title: "Sync Error (SyncError) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Sync Error (SyncError) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Sync Error (SyncError) table/entity reference (Microsoft Dataverse)

Failure reason and other detailed information for a record that failed to sync.

## Messages

The following table lists the messages for the Sync Error (SyncError) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: False |`PATCH` /syncerrors(*syncerrorid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /syncerrors<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /syncerrors(*syncerrorid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /syncerrors(*syncerrorid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /syncerrors<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `SetState`<br />Event: False |`PATCH` /syncerrors(*syncerrorid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: False |`PATCH` /syncerrors(*syncerrorid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /syncerrors(*syncerrorid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Sync Error (SyncError) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Sync Error** |
| **DisplayCollectionName** | **Sync Errors** |
| **SchemaName** | `SyncError` |
| **CollectionSchemaName** | `SyncErrors` |
| **EntitySetName** | `syncerrors`|
| **LogicalName** | `syncerror` |
| **LogicalCollectionName** | `syncerrors` |
| **PrimaryIdAttribute** | `syncerrorid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Action](#BKMK_Action)
- [ActionData](#BKMK_ActionData)
- [Description](#BKMK_Description)
- [ErrorCode](#BKMK_ErrorCode)
- [ErrorDetail](#BKMK_ErrorDetail)
- [ErrorMessage](#BKMK_ErrorMessage)
- [ErrorTime](#BKMK_ErrorTime)
- [ErrorType](#BKMK_ErrorType)
- [Name](#BKMK_Name)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [RequestData](#BKMK_RequestData)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [SyncErrorId](#BKMK_SyncErrorId)

### <a name="BKMK_Action"></a> Action

|Property|Value|
|---|---|
|Description|**Action Name for which sync error has occurred**|
|DisplayName|**Action**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`action`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ActionData"></a> ActionData

|Property|Value|
|---|---|
|Description|**Show the action data**|
|DisplayName|**Action Data**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`actiondata`|
|RequiredLevel|None|
|Type|String|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Enter a short description of the sync error.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_ErrorCode"></a> ErrorCode

|Property|Value|
|---|---|
|Description|**Displays the error code.**|
|DisplayName|**Error Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`errorcode`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ErrorDetail"></a> ErrorDetail

|Property|Value|
|---|---|
|Description|**Error description from the exception**|
|DisplayName|**Error Detail**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`errordetail`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_ErrorMessage"></a> ErrorMessage

|Property|Value|
|---|---|
|Description|**Error Message of the exception**|
|DisplayName|**Error Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`errormessage`|
|RequiredLevel|None|
|Type|String|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_ErrorTime"></a> ErrorTime

|Property|Value|
|---|---|
|Description|**Date and time when the upsync request was executed on CRM server**|
|DisplayName|**Error Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`errortime`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ErrorType"></a> ErrorType

|Property|Value|
|---|---|
|Description|**Select the preferred error type.**|
|DisplayName|**Error Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`errortype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`errortype_errortypecategory`|

#### ErrorType Choices/Options

|Value|Label|
|---|---|
|0|**Conflict**|
|1|**Record not found**|
|2|**Record already exists**|
|3|**Others**|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Entity name of the record for which sync error has occurred**|
|DisplayName|**Entity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user or team who owns the sync error.**|
|DisplayName|**Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
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

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**Choose the record that the sync error relates to.**|
|DisplayName|**Record**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`regardingobjectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account, activityfileattachment, activitymimeattachment, activityparty, adx_externalidentity, adx_invitation, adx_inviteredemption, adx_portalcomment, adx_setting, adx_webformsession, agentconversationmessage, agentconversationmessagefile, agentfeeditem, agenthubgoal, agenthubinsight, agenthubmetric, aicopilot, aiinsightcard, aiplugin, aipluginauth, aipluginconversationstarter, aipluginconversationstartermapping, aipluginexternalschema, aipluginexternalschemaproperty, aiplugingovernance, aiplugingovernanceext, aiplugininstance, aipluginoperation, aipluginoperationparameter, aipluginoperationresponsetemplate, aiplugintitle, aipluginusersetting, aiskillconfig, allowedmcpclient, annotation, appaction, appactionmigration, appactionrule, appelement, appentitysearchview, application, applicationuser, appmodulecomponentedge, appmodulecomponentnode, appointment, approvalprocess, approvalstageapproval, approvalstagecondition, approvalstageintelligent, approvalstageorder, appsetting, appusersetting, archivecleanupinfo, archivecleanupoperation, attachment, attributeclusterconfig, attributeimageconfig, attributemaskingrule, attributepicklistvalue, bot, botcomponent, botcomponentcollection, bulkarchiveconfig, bulkarchivefailuredetail, bulkarchiveoperation, bulkarchiveoperationdetail, businessdatalocalizedlabel, businessprocess, businessunit, canvasappextendedmetadata, card, cascadegrantrevokeaccessrecordstracker, cascadegrantrevokeaccessversiontracker, catalog, catalogassignment, category, certificatecredential, channelaccessprofile, channelaccessprofilerule, channelaccessprofileruleitem, chat, comment, connection, connectioninstance, connectionreference, connectionrole, connector, contact, conversationtranscript, copilotexamplequestion, copilotglossaryterm, copilotsynonyms, credential, customapi, customapirequestparameter, customapiresponseproperty, customeraddress, datalakefolder, datalakefolderpermission, datalakeworkspace, datalakeworkspacepermission, dataprocessingconfiguration, delegatedauthorization, deleteditemreference, desktopflowbinary, desktopflowmodule, duplicaterule, duplicaterulecondition, dvfilesearch, dvfilesearchattribute, dvfilesearchentity, dvtablesearch, dvtablesearchattribute, dvtablesearchentity, email, emailaddressconfiguration, emailserverprofile, enablearchivalrequest, entityanalyticsconfig, entityclusterconfig, entityimageconfig, entityindex, entityrecordfilter, environmentvariabledefinition, environmentvariablevalue, expiredprocess, exportedexcel, exportsolutionupload, externalparty, externalpartyitem, fabricaiskill, fax, featurecontrolsetting, federatedknowledgecitation, federatedknowledgeconfiguration, federatedknowledgeentityconfiguration, federatedknowledgemetadatarefresh, feedback, fieldpermission, fieldsecurityprofile, fileattachment, flowcapacityassignment, flowcredentialapplication, flowevent, flowmachine, flowmachinegroup, flowmachineimage, flowmachineimageversion, flowmachinenetwork, flowsession, flowsessionbinary, fxexpression, goal, goalrollupquery, governanceconfiguration, holidaywrapper, importmap, indexattributes, internaladdress, internalcatalogassignment, kbarticle, kbarticletemplate, keyvaultreference, knowledgearticle, knowledgearticleviews, knowledgebaserecord, knowledgefaq, knowledgesourceconsumer, knowledgesourceprofile, letter, mailbox, mailmergetemplate, mainfewshot, makerfewshot, managedidentity, maskingrule, mcpserver, mcptool, metadataforarchival, metric, mobileofflineprofileextension, msdynce_botcontent, msdyn_aibdataset, msdyn_aibdatasetfile, msdyn_aibdatasetrecord, msdyn_aibdatasetscontainer, msdyn_aibfeedbackloop, msdyn_aibfile, msdyn_aibfileattacheddata, msdyn_aiconfiguration, msdyn_aiconfigurationsearch, msdyn_aidataprocessingevent, msdyn_aidocumenttemplate, msdyn_aievaluationconfiguration, msdyn_aievaluationrun, msdyn_aievent, msdyn_aifptrainingdocument, msdyn_aimodel, msdyn_aimodelcatalog, msdyn_aiodimage, msdyn_aiodlabel, msdyn_aiodtrainingboundingbox, msdyn_aiodtrainingimage, msdyn_aioptimization, msdyn_aioptimizationprivatedata, msdyn_aitemplate, msdyn_aitestcase, msdyn_aitestcasedocument, msdyn_aitestcaseinput, msdyn_aitestrun, msdyn_aitestrunbatch, msdyn_analysiscomponent, msdyn_analysisjob, msdyn_analysisoverride, msdyn_analysisresult, msdyn_analysisresultdetail, msdyn_appinsightsmetadata, msdyn_copilotinteractions, msdyn_customcontrolextendedsettings, msdyn_dataflow, msdyn_dataflowconnectionreference, msdyn_dataflowrefreshhistory, msdyn_dataflowtemplate, msdyn_dataflow_datalakefolder, msdyn_dataworkspace, msdyn_dmsrequest, msdyn_dmsrequeststatus, msdyn_dmssyncrequest, msdyn_dmssyncstatus, msdyn_entitylinkchatconfiguration, msdyn_entityrefreshhistory, msdyn_favoriteknowledgearticle, msdyn_federatedarticle, msdyn_federatedarticleincident, msdyn_fileupload, msdyn_flow_actionapprovalmodel, msdyn_flow_approval, msdyn_flow_approvalrequest, msdyn_flow_approvalresponse, msdyn_flow_approvalstep, msdyn_flow_awaitallactionapprovalmodel, msdyn_flow_awaitallapprovalmodel, msdyn_flow_basicapprovalmodel, msdyn_flow_flowapproval, msdyn_formmapping, msdyn_function, msdyn_helppage, msdyn_historicalcaseharvestbatch, msdyn_historicalcaseharvestrun, msdyn_insightsstorevirtualentity, msdyn_integratedsearchprovider, msdyn_interimupdateknowledgearticle, msdyn_kalanguagesetting, msdyn_kbattachment, msdyn_kmfederatedsearchconfig, msdyn_kmpersonalizationsetting, msdyn_knowledgearticlecustomentity, msdyn_knowledgearticleimage, msdyn_knowledgearticletemplate, msdyn_knowledgeassetconfiguration, msdyn_knowledgeconfiguration, msdyn_knowledgeharvestjobrecord, msdyn_knowledgeinteractioninsight, msdyn_knowledgemanagementsetting, msdyn_knowledgepersonalfilter, msdyn_knowledgesearchfilter, msdyn_knowledgesearchinsight, msdyn_mobileapp, msdyn_modulerundetail, msdyn_plan, msdyn_planartifact, msdyn_planattachment, msdyn_pmanalysishistory, msdyn_pmbusinessruleautomationconfig, msdyn_pmcalendar, msdyn_pmcalendarversion, msdyn_pminferredtask, msdyn_pmprocessextendedmetadataversion, msdyn_pmprocesstemplate, msdyn_pmprocessusersettings, msdyn_pmprocessversion, msdyn_pmrecording, msdyn_pmsimulation, msdyn_pmtab, msdyn_pmtemplate, msdyn_pmview, msdyn_qna, msdyn_richtextfile, msdyn_salesforcestructuredobject, msdyn_salesforcestructuredqnaconfig, msdyn_schedule, msdyn_serviceconfiguration, msdyn_slakpi, msdyn_solutionhealthrule, msdyn_solutionhealthruleargument, msdyn_solutionhealthruleset, msdyn_tour, msdyn_virtualtablecolumncandidate, msdyn_workflowactionstatus, msgraphresourcetosubscription, mspcat_catalogsubmissionfiles, mspcat_packagestore, newprocess, offlinecommanddefinition, organization, organizationdatasyncfnostate, organizationdatasyncstate, organizationdatasyncsubscription, organizationdatasyncsubscriptionentity, organizationdatasyncsubscriptionfnotable, organizationsetting, package, packagehistory, pdfsetting, phonecall, plannerbusinessscenario, plannersyncaction, plugin, pluginpackage, position, postfollow, powerbidataset, powerbidatasetapdx, powerbimashupparameter, powerbireport, powerbireportapdx, powerfxrule, powerpagecomponent, powerpagesddosalert, powerpagesite, powerpagesitelanguage, powerpagesitepublished, powerpagesmanagedidentity, powerpagesscanreport, powerpagessourcefile, privilegecheckerlog, privilegecheckerrun, privilegesremovalsetting, processorregistration, processsession, processstage, processstageparameter, processtrigger, provisionlanguageforuser, publisher, purviewlabelinfo, purviewlabelsynccache, queue, queueitem, reconciliationentityinfo, reconciliationentitystepinfo, reconciliationinfo, recordfilter, recurringappointmentmaster, recyclebinconfig, relationshipattribute, report, reportcategory, reportparameter, retaineddataexcel, retentioncleanupinfo, retentioncleanupoperation, retentionconfig, retentionfailuredetail, retentionoperation, retentionoperationdetail, retentionsuccessdetail, revokeinheritedaccessrecordstracker, role, roleeditorlayout, rollupfield, savedquery, savedqueryvisualization, savingrule, sa_suggestedaction, sa_suggestedactioncriteria, searchattributesettings, searchcustomanalyzer, searchrelationshipsettings, sensitivitylabelattributemapping, serviceplan, serviceplanmapping, settingdefinition, sharedlinksetting, sharedobject, sharedworkspace, sharedworkspacepool, sharepointdocumentlocation, sharepointmanagedidentity, sharepointsite, sideloadedaiplugin, signalregistration, sla, slaitem, slakpiinstance, socialactivity, socialprofile, solution, solutioncomponentattributeconfiguration, solutioncomponentbatchconfiguration, solutioncomponentconfiguration, solutioncomponentrelationshipconfiguration, stagedattributelookupvalue, stagedattributepicklistvalue, stagedentity, stagedentityattribute, stagedentityrelationship, stagedentityrelationshiprelationships, stagedentityrelationshiprole, stagedmetadataasyncoperation, stagedoptionset, stagedrelationship, stagedrelationshipextracondition, stagedviewattribute, stagesolutionupload, subject, supportusertable, synapsedatabase, synapselinkexternaltablestate, synapselinkprofile, synapselinkprofileentity, synapselinkprofileentitystate, synapselinkschedule, syncerror, systemuser, systemuserauthorizationchangetracker, tag, taggedflowsession, taggedprocess, task, tdsmetadata, team, teammobileofflineprofilemembership, teamtemplate, template, territory, toolinggateway, toolinggatewaymcpserver, traitregistration, transactioncurrency, translationprocess, unstructuredfilesearchentity, unstructuredfilesearchrecord, unstructuredfilesearchrecordstatus, usermobileofflineprofilemembership, userquery, userqueryvisualization, userrating, uxagentcomponent, uxagentcomponentrevision, uxagentproject, uxagentprojectfile, viewasexamplequestion, virtualentitymetadata, workflow, workflowbinary, workflowmetadata, workqueue, workqueueitem|

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

### <a name="BKMK_RequestData"></a> RequestData

|Property|Value|
|---|---|
|Description|**Request data for the entity that had the sync error.**|
|DisplayName|**Request Data**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`requestdata`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Shows whether the sync error is active or resolved.**|
|DisplayName|**State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`syncerror_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 0<br />InvariantName: `Active`|
|1|Label: **Resolved**<br />DefaultStatus: 1<br />InvariantName: `Resolved`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Select the sync error status.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue|0|
|GlobalChoiceName|`syncerror_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />State:0<br />TransitionData: None|
|1|Label: **Fixed**<br />State:1<br />TransitionData: None|

### <a name="BKMK_SyncErrorId"></a> SyncErrorId

|Property|Value|
|---|---|
|Description|**Unique identifier of the sync error.**|
|DisplayName|**Sync Error Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`syncerrorid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the sync error.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the sync Error was created.**|
|DisplayName|**Created On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who created the sync error.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the sync error.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the sync error was last modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedon`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who last modified the sync error.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridyominame`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Business unit that owns the sync error.**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|---|---|
|Description|**Unique identifier of the team who owns the sync error.**|
|DisplayName|**Owning Team**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`owningteam`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|team|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who owns the sync error.**|
|DisplayName|**Owning User**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Shows the version number of the sync error.**|
|DisplayName|**Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [Account_SyncErrors](#BKMK_Account_SyncErrors)
- [activityfileattachment_SyncErrors](#BKMK_activityfileattachment_SyncErrors)
- [ActivityMimeAttachment_SyncErrors](#BKMK_ActivityMimeAttachment_SyncErrors)
- [ActivityParty_SyncErrors](#BKMK_ActivityParty_SyncErrors)
- [adx_externalidentity_SyncErrors](#BKMK_adx_externalidentity_SyncErrors)
- [adx_invitation_SyncErrors](#BKMK_adx_invitation_SyncErrors)
- [adx_inviteredemption_SyncErrors](#BKMK_adx_inviteredemption_SyncErrors)
- [adx_portalcomment_SyncErrors](#BKMK_adx_portalcomment_SyncErrors)
- [adx_setting_SyncErrors](#BKMK_adx_setting_SyncErrors)
- [adx_webformsession_SyncErrors](#BKMK_adx_webformsession_SyncErrors)
- [aicopilot_SyncErrors](#BKMK_aicopilot_SyncErrors)
- [aiplugin_SyncErrors](#BKMK_aiplugin_SyncErrors)
- [aipluginauth_SyncErrors](#BKMK_aipluginauth_SyncErrors)
- [aipluginconversationstarter_SyncErrors](#BKMK_aipluginconversationstarter_SyncErrors)
- [aipluginconversationstartermapping_SyncErrors](#BKMK_aipluginconversationstartermapping_SyncErrors)
- [aipluginexternalschema_SyncErrors](#BKMK_aipluginexternalschema_SyncErrors)
- [aipluginexternalschemaproperty_SyncErrors](#BKMK_aipluginexternalschemaproperty_SyncErrors)
- [aiplugingovernance_SyncErrors](#BKMK_aiplugingovernance_SyncErrors)
- [aiplugingovernanceext_SyncErrors](#BKMK_aiplugingovernanceext_SyncErrors)
- [aiplugininstance_SyncErrors](#BKMK_aiplugininstance_SyncErrors)
- [aipluginoperation_SyncErrors](#BKMK_aipluginoperation_SyncErrors)
- [aipluginoperationparameter_SyncErrors](#BKMK_aipluginoperationparameter_SyncErrors)
- [aipluginoperationresponsetemplate_SyncErrors](#BKMK_aipluginoperationresponsetemplate_SyncErrors)
- [aiplugintitle_SyncErrors](#BKMK_aiplugintitle_SyncErrors)
- [aipluginusersetting_SyncErrors](#BKMK_aipluginusersetting_SyncErrors)
- [allowedmcpclient_SyncErrors](#BKMK_allowedmcpclient_SyncErrors)
- [Annotation_SyncErrors](#BKMK_Annotation_SyncErrors)
- [appaction_SyncErrors](#BKMK_appaction_SyncErrors)
- [appactionmigration_SyncErrors](#BKMK_appactionmigration_SyncErrors)
- [appactionrule_SyncErrors](#BKMK_appactionrule_SyncErrors)
- [application_SyncErrors](#BKMK_application_SyncErrors)
- [applicationuser_SyncErrors](#BKMK_applicationuser_SyncErrors)
- [Appointment_SyncErrors](#BKMK_Appointment_SyncErrors)
- [approvalprocess_SyncErrors](#BKMK_approvalprocess_SyncErrors)
- [approvalstageapproval_SyncErrors](#BKMK_approvalstageapproval_SyncErrors)
- [approvalstagecondition_SyncErrors](#BKMK_approvalstagecondition_SyncErrors)
- [approvalstageintelligent_SyncErrors](#BKMK_approvalstageintelligent_SyncErrors)
- [approvalstageorder_SyncErrors](#BKMK_approvalstageorder_SyncErrors)
- [Attachment_SyncErrors](#BKMK_Attachment_SyncErrors)
- [attributeclusterconfig_SyncErrors](#BKMK_attributeclusterconfig_SyncErrors)
- [attributeimageconfig_SyncErrors](#BKMK_attributeimageconfig_SyncErrors)
- [attributemaskingrule_SyncErrors](#BKMK_attributemaskingrule_SyncErrors)
- [attributepicklistvalue_SyncErrors](#BKMK_attributepicklistvalue_SyncErrors)
- [bot_SyncErrors](#BKMK_bot_SyncErrors)
- [botcomponent_SyncErrors](#BKMK_botcomponent_SyncErrors)
- [botcomponentcollection_SyncErrors](#BKMK_botcomponentcollection_SyncErrors)
- [businessprocess_SyncErrors](#BKMK_businessprocess_SyncErrors)
- [BusinessUnit_SyncError](#BKMK_BusinessUnit_SyncError)
- [BusinessUnit_SyncErrors](#BKMK_BusinessUnit_SyncErrors)
- [card_SyncErrors](#BKMK_card_SyncErrors)
- [catalog_SyncErrors](#BKMK_catalog_SyncErrors)
- [catalogassignment_SyncErrors](#BKMK_catalogassignment_SyncErrors)
- [Category_SyncErrors](#BKMK_Category_SyncErrors)
- [certificatecredential_SyncErrors](#BKMK_certificatecredential_SyncErrors)
- [chat_SyncErrors](#BKMK_chat_SyncErrors)
- [Connection_SyncErrors](#BKMK_Connection_SyncErrors)
- [connectioninstance_SyncErrors](#BKMK_connectioninstance_SyncErrors)
- [connectionreference_SyncErrors](#BKMK_connectionreference_SyncErrors)
- [ConnectionRole_SyncErrors](#BKMK_ConnectionRole_SyncErrors)
- [connector_SyncErrors](#BKMK_connector_SyncErrors)
- [Contact_SyncErrors](#BKMK_Contact_SyncErrors)
- [conversationtranscript_SyncErrors](#BKMK_conversationtranscript_SyncErrors)
- [copilotexamplequestion_SyncErrors](#BKMK_copilotexamplequestion_SyncErrors)
- [copilotglossaryterm_SyncErrors](#BKMK_copilotglossaryterm_SyncErrors)
- [copilotsynonyms_SyncErrors](#BKMK_copilotsynonyms_SyncErrors)
- [credential_SyncErrors](#BKMK_credential_SyncErrors)
- [customapi_SyncErrors](#BKMK_customapi_SyncErrors)
- [customapirequestparameter_SyncErrors](#BKMK_customapirequestparameter_SyncErrors)
- [customapiresponseproperty_SyncErrors](#BKMK_customapiresponseproperty_SyncErrors)
- [CustomerAddress_SyncErrors](#BKMK_CustomerAddress_SyncErrors)
- [datalakefolder_SyncErrors](#BKMK_datalakefolder_SyncErrors)
- [datalakefolderpermission_SyncErrors](#BKMK_datalakefolderpermission_SyncErrors)
- [datalakeworkspace_SyncErrors](#BKMK_datalakeworkspace_SyncErrors)
- [datalakeworkspacepermission_SyncErrors](#BKMK_datalakeworkspacepermission_SyncErrors)
- [dataprocessingconfiguration_SyncErrors](#BKMK_dataprocessingconfiguration_SyncErrors)
- [delegatedauthorization_SyncErrors](#BKMK_delegatedauthorization_SyncErrors)
- [desktopflowbinary_SyncErrors](#BKMK_desktopflowbinary_SyncErrors)
- [desktopflowmodule_SyncErrors](#BKMK_desktopflowmodule_SyncErrors)
- [DuplicateRule_SyncErrors](#BKMK_DuplicateRule_SyncErrors)
- [DuplicateRuleCondition_SyncErrors](#BKMK_DuplicateRuleCondition_SyncErrors)
- [dvfilesearch_SyncErrors](#BKMK_dvfilesearch_SyncErrors)
- [dvfilesearchattribute_SyncErrors](#BKMK_dvfilesearchattribute_SyncErrors)
- [dvfilesearchentity_SyncErrors](#BKMK_dvfilesearchentity_SyncErrors)
- [dvtablesearch_SyncErrors](#BKMK_dvtablesearch_SyncErrors)
- [dvtablesearchattribute_SyncErrors](#BKMK_dvtablesearchattribute_SyncErrors)
- [dvtablesearchentity_SyncErrors](#BKMK_dvtablesearchentity_SyncErrors)
- [Email_SyncErrors](#BKMK_Email_SyncErrors)
- [emailaddressconfiguration_SyncErrors](#BKMK_emailaddressconfiguration_SyncErrors)
- [EmailServerProfile_SyncErrors](#BKMK_EmailServerProfile_SyncErrors)
- [entityanalyticsconfig_SyncErrors](#BKMK_entityanalyticsconfig_SyncErrors)
- [entityclusterconfig_SyncErrors](#BKMK_entityclusterconfig_SyncErrors)
- [entityimageconfig_SyncErrors](#BKMK_entityimageconfig_SyncErrors)
- [entityindex_SyncErrors](#BKMK_entityindex_SyncErrors)
- [entityrecordfilter_SyncErrors](#BKMK_entityrecordfilter_SyncErrors)
- [environmentvariabledefinition_SyncErrors](#BKMK_environmentvariabledefinition_SyncErrors)
- [environmentvariablevalue_SyncErrors](#BKMK_environmentvariablevalue_SyncErrors)
- [ExpiredProcess_SyncErrors](#BKMK_ExpiredProcess_SyncErrors)
- [exportedexcel_SyncErrors](#BKMK_exportedexcel_SyncErrors)
- [exportsolutionupload_SyncErrors](#BKMK_exportsolutionupload_SyncErrors)
- [fabricaiskill_SyncErrors](#BKMK_fabricaiskill_SyncErrors)
- [Fax_SyncErrors](#BKMK_Fax_SyncErrors)
- [featurecontrolsetting_SyncErrors](#BKMK_featurecontrolsetting_SyncErrors)
- [federatedknowledgeconfiguration_SyncErrors](#BKMK_federatedknowledgeconfiguration_SyncErrors)
- [federatedknowledgeentityconfiguration_SyncErrors](#BKMK_federatedknowledgeentityconfiguration_SyncErrors)
- [Feedback_SyncErrors](#BKMK_Feedback_SyncErrors)
- [FieldPermission_SyncErrors](#BKMK_FieldPermission_SyncErrors)
- [FieldSecurityProfile_SyncErrors](#BKMK_FieldSecurityProfile_SyncErrors)
- [FileAttachment_SyncErrors](#BKMK_FileAttachment_SyncErrors)
- [flowcapacityassignment_SyncErrors](#BKMK_flowcapacityassignment_SyncErrors)
- [flowcredentialapplication_SyncErrors](#BKMK_flowcredentialapplication_SyncErrors)
- [flowevent_SyncErrors](#BKMK_flowevent_SyncErrors)
- [flowmachine_SyncErrors](#BKMK_flowmachine_SyncErrors)
- [flowmachinegroup_SyncErrors](#BKMK_flowmachinegroup_SyncErrors)
- [flowmachineimage_SyncErrors](#BKMK_flowmachineimage_SyncErrors)
- [flowmachineimageversion_SyncErrors](#BKMK_flowmachineimageversion_SyncErrors)
- [flowmachinenetwork_SyncErrors](#BKMK_flowmachinenetwork_SyncErrors)
- [flowsession_SyncErrors](#BKMK_flowsession_SyncErrors)
- [flowsessionbinary_SyncErrors](#BKMK_flowsessionbinary_SyncErrors)
- [fxexpression_SyncErrors](#BKMK_fxexpression_SyncErrors)
- [Goal_SyncErrors](#BKMK_Goal_SyncErrors)
- [GoalRollupQuery_SyncErrors](#BKMK_GoalRollupQuery_SyncErrors)
- [governanceconfiguration_SyncErrors](#BKMK_governanceconfiguration_SyncErrors)
- [ImportMap_SyncErrors](#BKMK_ImportMap_SyncErrors)
- [indexattributes_SyncErrors](#BKMK_indexattributes_SyncErrors)
- [KbArticle_SyncErrors](#BKMK_KbArticle_SyncErrors)
- [KbArticleTemplate_SyncErrors](#BKMK_KbArticleTemplate_SyncErrors)
- [keyvaultreference_SyncErrors](#BKMK_keyvaultreference_SyncErrors)
- [KnowledgeArticle_SyncErrors](#BKMK_KnowledgeArticle_SyncErrors)
- [KnowledgeArticleViews_SyncErrors](#BKMK_KnowledgeArticleViews_SyncErrors)
- [KnowledgeBaseRecord_SyncErrors](#BKMK_KnowledgeBaseRecord_SyncErrors)
- [knowledgefaq_SyncErrors](#BKMK_knowledgefaq_SyncErrors)
- [Letter_SyncErrors](#BKMK_Letter_SyncErrors)
- [lk_syncerrorbase_createdby](#BKMK_lk_syncerrorbase_createdby)
- [lk_syncerrorbase_createdonbehalfby](#BKMK_lk_syncerrorbase_createdonbehalfby)
- [lk_syncerrorbase_modifiedby](#BKMK_lk_syncerrorbase_modifiedby)
- [lk_syncerrorbase_modifiedonbehalfby](#BKMK_lk_syncerrorbase_modifiedonbehalfby)
- [Mailbox_SyncErrors](#BKMK_Mailbox_SyncErrors)
- [MailMergeTemplate_SyncErrors](#BKMK_MailMergeTemplate_SyncErrors)
- [mainfewshot_SyncErrors](#BKMK_mainfewshot_SyncErrors)
- [makerfewshot_SyncErrors](#BKMK_makerfewshot_SyncErrors)
- [managedidentity_SyncErrors](#BKMK_managedidentity_SyncErrors)
- [maskingrule_SyncErrors](#BKMK_maskingrule_SyncErrors)
- [mcpserver_SyncErrors](#BKMK_mcpserver_SyncErrors)
- [mcptool_SyncErrors](#BKMK_mcptool_SyncErrors)
- [metadataforarchival_SyncErrors](#BKMK_metadataforarchival_SyncErrors)
- [Metric_SyncErrors](#BKMK_Metric_SyncErrors)
- [mobileofflineprofileextension_SyncErrors](#BKMK_mobileofflineprofileextension_SyncErrors)
- [msdyn_aibdataset_SyncErrors](#BKMK_msdyn_aibdataset_SyncErrors)
- [msdyn_aibdatasetfile_SyncErrors](#BKMK_msdyn_aibdatasetfile_SyncErrors)
- [msdyn_aibdatasetrecord_SyncErrors](#BKMK_msdyn_aibdatasetrecord_SyncErrors)
- [msdyn_aibdatasetscontainer_SyncErrors](#BKMK_msdyn_aibdatasetscontainer_SyncErrors)
- [msdyn_aibfeedbackloop_SyncErrors](#BKMK_msdyn_aibfeedbackloop_SyncErrors)
- [msdyn_aibfile_SyncErrors](#BKMK_msdyn_aibfile_SyncErrors)
- [msdyn_aibfileattacheddata_SyncErrors](#BKMK_msdyn_aibfileattacheddata_SyncErrors)
- [msdyn_aiconfiguration_SyncErrors](#BKMK_msdyn_aiconfiguration_SyncErrors)
- [msdyn_aidataprocessingevent_SyncErrors](#BKMK_msdyn_aidataprocessingevent_SyncErrors)
- [msdyn_aidocumenttemplate_SyncErrors](#BKMK_msdyn_aidocumenttemplate_SyncErrors)
- [msdyn_aievaluationconfiguration_SyncErrors](#BKMK_msdyn_aievaluationconfiguration_SyncErrors)
- [msdyn_aievaluationrun_SyncErrors](#BKMK_msdyn_aievaluationrun_SyncErrors)
- [msdyn_aievent_SyncErrors](#BKMK_msdyn_aievent_SyncErrors)
- [msdyn_aifptrainingdocument_SyncErrors](#BKMK_msdyn_aifptrainingdocument_SyncErrors)
- [msdyn_aimodel_SyncErrors](#BKMK_msdyn_aimodel_SyncErrors)
- [msdyn_aiodimage_SyncErrors](#BKMK_msdyn_aiodimage_SyncErrors)
- [msdyn_aiodlabel_SyncErrors](#BKMK_msdyn_aiodlabel_SyncErrors)
- [msdyn_aiodtrainingboundingbox_SyncErrors](#BKMK_msdyn_aiodtrainingboundingbox_SyncErrors)
- [msdyn_aiodtrainingimage_SyncErrors](#BKMK_msdyn_aiodtrainingimage_SyncErrors)
- [msdyn_aitemplate_SyncErrors](#BKMK_msdyn_aitemplate_SyncErrors)
- [msdyn_aitestcase_SyncErrors](#BKMK_msdyn_aitestcase_SyncErrors)
- [msdyn_aitestcasedocument_SyncErrors](#BKMK_msdyn_aitestcasedocument_SyncErrors)
- [msdyn_aitestcaseinput_SyncErrors](#BKMK_msdyn_aitestcaseinput_SyncErrors)
- [msdyn_aitestrun_SyncErrors](#BKMK_msdyn_aitestrun_SyncErrors)
- [msdyn_aitestrunbatch_SyncErrors](#BKMK_msdyn_aitestrunbatch_SyncErrors)
- [msdyn_analysiscomponent_SyncErrors](#BKMK_msdyn_analysiscomponent_SyncErrors)
- [msdyn_analysisjob_SyncErrors](#BKMK_msdyn_analysisjob_SyncErrors)
- [msdyn_analysisoverride_SyncErrors](#BKMK_msdyn_analysisoverride_SyncErrors)
- [msdyn_analysisresult_SyncErrors](#BKMK_msdyn_analysisresult_SyncErrors)
- [msdyn_analysisresultdetail_SyncErrors](#BKMK_msdyn_analysisresultdetail_SyncErrors)
- [msdyn_appinsightsmetadata_SyncErrors](#BKMK_msdyn_appinsightsmetadata_SyncErrors)
- [msdyn_copilotinteractions_SyncErrors](#BKMK_msdyn_copilotinteractions_SyncErrors)
- [msdyn_customcontrolextendedsettings_SyncErrors](#BKMK_msdyn_customcontrolextendedsettings_SyncErrors)
- [msdyn_dataflow_datalakefolder_SyncErrors](#BKMK_msdyn_dataflow_datalakefolder_SyncErrors)
- [msdyn_dataflow_SyncErrors](#BKMK_msdyn_dataflow_SyncErrors)
- [msdyn_dataflowconnectionreference_SyncErrors](#BKMK_msdyn_dataflowconnectionreference_SyncErrors)
- [msdyn_dataflowrefreshhistory_SyncErrors](#BKMK_msdyn_dataflowrefreshhistory_SyncErrors)
- [msdyn_dataflowtemplate_SyncErrors](#BKMK_msdyn_dataflowtemplate_SyncErrors)
- [msdyn_dmsrequest_SyncErrors](#BKMK_msdyn_dmsrequest_SyncErrors)
- [msdyn_dmsrequeststatus_SyncErrors](#BKMK_msdyn_dmsrequeststatus_SyncErrors)
- [msdyn_dmssyncrequest_SyncErrors](#BKMK_msdyn_dmssyncrequest_SyncErrors)
- [msdyn_dmssyncstatus_SyncErrors](#BKMK_msdyn_dmssyncstatus_SyncErrors)
- [msdyn_entitylinkchatconfiguration_SyncErrors](#BKMK_msdyn_entitylinkchatconfiguration_SyncErrors)
- [msdyn_entityrefreshhistory_SyncErrors](#BKMK_msdyn_entityrefreshhistory_SyncErrors)
- [msdyn_favoriteknowledgearticle_SyncErrors](#BKMK_msdyn_favoriteknowledgearticle_SyncErrors)
- [msdyn_federatedarticle_SyncErrors](#BKMK_msdyn_federatedarticle_SyncErrors)
- [msdyn_federatedarticleincident_SyncErrors](#BKMK_msdyn_federatedarticleincident_SyncErrors)
- [msdyn_fileupload_SyncErrors](#BKMK_msdyn_fileupload_SyncErrors)
- [msdyn_flow_actionapprovalmodel_SyncErrors](#BKMK_msdyn_flow_actionapprovalmodel_SyncErrors)
- [msdyn_flow_approval_SyncErrors](#BKMK_msdyn_flow_approval_SyncErrors)
- [msdyn_flow_approvalrequest_SyncErrors](#BKMK_msdyn_flow_approvalrequest_SyncErrors)
- [msdyn_flow_approvalresponse_SyncErrors](#BKMK_msdyn_flow_approvalresponse_SyncErrors)
- [msdyn_flow_approvalstep_SyncErrors](#BKMK_msdyn_flow_approvalstep_SyncErrors)
- [msdyn_flow_awaitallactionapprovalmodel_SyncErrors](#BKMK_msdyn_flow_awaitallactionapprovalmodel_SyncErrors)
- [msdyn_flow_awaitallapprovalmodel_SyncErrors](#BKMK_msdyn_flow_awaitallapprovalmodel_SyncErrors)
- [msdyn_flow_basicapprovalmodel_SyncErrors](#BKMK_msdyn_flow_basicapprovalmodel_SyncErrors)
- [msdyn_flow_flowapproval_SyncErrors](#BKMK_msdyn_flow_flowapproval_SyncErrors)
- [msdyn_formmapping_SyncErrors](#BKMK_msdyn_formmapping_SyncErrors)
- [msdyn_function_SyncErrors](#BKMK_msdyn_function_SyncErrors)
- [msdyn_helppage_SyncErrors](#BKMK_msdyn_helppage_SyncErrors)
- [msdyn_historicalcaseharvestbatch_SyncErrors](#BKMK_msdyn_historicalcaseharvestbatch_SyncErrors)
- [msdyn_historicalcaseharvestrun_SyncErrors](#BKMK_msdyn_historicalcaseharvestrun_SyncErrors)
- [msdyn_insightsstorevirtualentity_SyncErrors](#BKMK_msdyn_insightsstorevirtualentity_SyncErrors)
- [msdyn_integratedsearchprovider_SyncErrors](#BKMK_msdyn_integratedsearchprovider_SyncErrors)
- [msdyn_kalanguagesetting_SyncErrors](#BKMK_msdyn_kalanguagesetting_SyncErrors)
- [msdyn_kbattachment_SyncErrors](#BKMK_msdyn_kbattachment_SyncErrors)
- [msdyn_kmfederatedsearchconfig_SyncErrors](#BKMK_msdyn_kmfederatedsearchconfig_SyncErrors)
- [msdyn_kmpersonalizationsetting_SyncErrors](#BKMK_msdyn_kmpersonalizationsetting_SyncErrors)
- [msdyn_knowledgearticleimage_SyncErrors](#BKMK_msdyn_knowledgearticleimage_SyncErrors)
- [msdyn_knowledgearticletemplate_SyncErrors](#BKMK_msdyn_knowledgearticletemplate_SyncErrors)
- [msdyn_knowledgeassetconfiguration_SyncErrors](#BKMK_msdyn_knowledgeassetconfiguration_SyncErrors)
- [msdyn_knowledgeconfiguration_SyncErrors](#BKMK_msdyn_knowledgeconfiguration_SyncErrors)
- [msdyn_knowledgeharvestjobrecord_SyncErrors](#BKMK_msdyn_knowledgeharvestjobrecord_SyncErrors)
- [msdyn_knowledgeinteractioninsight_SyncErrors](#BKMK_msdyn_knowledgeinteractioninsight_SyncErrors)
- [msdyn_knowledgemanagementsetting_SyncErrors](#BKMK_msdyn_knowledgemanagementsetting_SyncErrors)
- [msdyn_knowledgepersonalfilter_SyncErrors](#BKMK_msdyn_knowledgepersonalfilter_SyncErrors)
- [msdyn_knowledgesearchfilter_SyncErrors](#BKMK_msdyn_knowledgesearchfilter_SyncErrors)
- [msdyn_knowledgesearchinsight_SyncErrors](#BKMK_msdyn_knowledgesearchinsight_SyncErrors)
- [msdyn_mobileapp_SyncErrors](#BKMK_msdyn_mobileapp_SyncErrors)
- [msdyn_modulerundetail_SyncErrors](#BKMK_msdyn_modulerundetail_SyncErrors)
- [msdyn_pmanalysishistory_SyncErrors](#BKMK_msdyn_pmanalysishistory_SyncErrors)
- [msdyn_pmbusinessruleautomationconfig_SyncErrors](#BKMK_msdyn_pmbusinessruleautomationconfig_SyncErrors)
- [msdyn_pmcalendar_SyncErrors](#BKMK_msdyn_pmcalendar_SyncErrors)
- [msdyn_pmcalendarversion_SyncErrors](#BKMK_msdyn_pmcalendarversion_SyncErrors)
- [msdyn_pminferredtask_SyncErrors](#BKMK_msdyn_pminferredtask_SyncErrors)
- [msdyn_pmprocessextendedmetadataversion_SyncErrors](#BKMK_msdyn_pmprocessextendedmetadataversion_SyncErrors)
- [msdyn_pmprocesstemplate_SyncErrors](#BKMK_msdyn_pmprocesstemplate_SyncErrors)
- [msdyn_pmprocessusersettings_SyncErrors](#BKMK_msdyn_pmprocessusersettings_SyncErrors)
- [msdyn_pmprocessversion_SyncErrors](#BKMK_msdyn_pmprocessversion_SyncErrors)
- [msdyn_pmrecording_SyncErrors](#BKMK_msdyn_pmrecording_SyncErrors)
- [msdyn_pmsimulation_SyncErrors](#BKMK_msdyn_pmsimulation_SyncErrors)
- [msdyn_pmtab_SyncErrors](#BKMK_msdyn_pmtab_SyncErrors)
- [msdyn_pmtemplate_SyncErrors](#BKMK_msdyn_pmtemplate_SyncErrors)
- [msdyn_pmview_SyncErrors](#BKMK_msdyn_pmview_SyncErrors)
- [msdyn_qna_SyncErrors](#BKMK_msdyn_qna_SyncErrors)
- [msdyn_richtextfile_SyncErrors](#BKMK_msdyn_richtextfile_SyncErrors)
- [msdyn_salesforcestructuredobject_SyncErrors](#BKMK_msdyn_salesforcestructuredobject_SyncErrors)
- [msdyn_salesforcestructuredqnaconfig_SyncErrors](#BKMK_msdyn_salesforcestructuredqnaconfig_SyncErrors)
- [msdyn_schedule_SyncErrors](#BKMK_msdyn_schedule_SyncErrors)
- [msdyn_serviceconfiguration_SyncErrors](#BKMK_msdyn_serviceconfiguration_SyncErrors)
- [msdyn_slakpi_SyncErrors](#BKMK_msdyn_slakpi_SyncErrors)
- [msdyn_solutionhealthrule_SyncErrors](#BKMK_msdyn_solutionhealthrule_SyncErrors)
- [msdyn_solutionhealthruleargument_SyncErrors](#BKMK_msdyn_solutionhealthruleargument_SyncErrors)
- [msdyn_solutionhealthruleset_SyncErrors](#BKMK_msdyn_solutionhealthruleset_SyncErrors)
- [msdyn_tour_SyncErrors](#BKMK_msdyn_tour_SyncErrors)
- [msdyn_virtualtablecolumncandidate_SyncErrors](#BKMK_msdyn_virtualtablecolumncandidate_SyncErrors)
- [msdyn_workflowactionstatus_SyncErrors](#BKMK_msdyn_workflowactionstatus_SyncErrors)
- [msdynce_botcontent_SyncErrors](#BKMK_msdynce_botcontent_SyncErrors)
- [msgraphresourcetosubscription_SyncErrors](#BKMK_msgraphresourcetosubscription_SyncErrors)
- [mspcat_catalogsubmissionfiles_SyncErrors](#BKMK_mspcat_catalogsubmissionfiles_SyncErrors)
- [mspcat_packagestore_SyncErrors](#BKMK_mspcat_packagestore_SyncErrors)
- [NewProcess_SyncErrors](#BKMK_NewProcess_SyncErrors)
- [Organization_SyncErrors](#BKMK_Organization_SyncErrors)
- [organizationdatasyncfnostate_SyncErrors](#BKMK_organizationdatasyncfnostate_SyncErrors)
- [organizationdatasyncstate_SyncErrors](#BKMK_organizationdatasyncstate_SyncErrors)
- [organizationdatasyncsubscription_SyncErrors](#BKMK_organizationdatasyncsubscription_SyncErrors)
- [organizationdatasyncsubscriptionentity_SyncErrors](#BKMK_organizationdatasyncsubscriptionentity_SyncErrors)
- [organizationdatasyncsubscriptionfnotable_SyncErrors](#BKMK_organizationdatasyncsubscriptionfnotable_SyncErrors)
- [owner_SyncError](#BKMK_owner_SyncError)
- [package_SyncErrors](#BKMK_package_SyncErrors)
- [packagehistory_SyncErrors](#BKMK_packagehistory_SyncErrors)
- [PhoneCall_SyncErrors](#BKMK_PhoneCall_SyncErrors)
- [plannerbusinessscenario_SyncErrors](#BKMK_plannerbusinessscenario_SyncErrors)
- [plannersyncaction_SyncErrors](#BKMK_plannersyncaction_SyncErrors)
- [plugin_SyncErrors](#BKMK_plugin_SyncErrors)
- [pluginpackage_SyncErrors](#BKMK_pluginpackage_SyncErrors)
- [Position_SyncErrors](#BKMK_Position_SyncErrors)
- [PostFollow_SyncErrors](#BKMK_PostFollow_SyncErrors)
- [powerbidataset_SyncErrors](#BKMK_powerbidataset_SyncErrors)
- [powerbidatasetapdx_SyncErrors](#BKMK_powerbidatasetapdx_SyncErrors)
- [powerbimashupparameter_SyncErrors](#BKMK_powerbimashupparameter_SyncErrors)
- [powerbireport_SyncErrors](#BKMK_powerbireport_SyncErrors)
- [powerbireportapdx_SyncErrors](#BKMK_powerbireportapdx_SyncErrors)
- [powerfxrule_SyncErrors](#BKMK_powerfxrule_SyncErrors)
- [powerpagecomponent_SyncErrors](#BKMK_powerpagecomponent_SyncErrors)
- [powerpagesddosalert_SyncErrors](#BKMK_powerpagesddosalert_SyncErrors)
- [powerpagesite_SyncErrors](#BKMK_powerpagesite_SyncErrors)
- [powerpagesitelanguage_SyncErrors](#BKMK_powerpagesitelanguage_SyncErrors)
- [powerpagesitepublished_SyncErrors](#BKMK_powerpagesitepublished_SyncErrors)
- [powerpagesmanagedidentity_SyncErrors](#BKMK_powerpagesmanagedidentity_SyncErrors)
- [powerpagesscanreport_SyncErrors](#BKMK_powerpagesscanreport_SyncErrors)
- [powerpagessourcefile_SyncErrors](#BKMK_powerpagessourcefile_SyncErrors)
- [privilegecheckerlog_SyncErrors](#BKMK_privilegecheckerlog_SyncErrors)
- [privilegecheckerrun_SyncErrors](#BKMK_privilegecheckerrun_SyncErrors)
- [privilegesremovalsetting_SyncErrors](#BKMK_privilegesremovalsetting_SyncErrors)
- [ProcessSession_SyncErrors](#BKMK_ProcessSession_SyncErrors)
- [ProcessStage_SyncErrors](#BKMK_ProcessStage_SyncErrors)
- [processstageparameter_SyncErrors](#BKMK_processstageparameter_SyncErrors)
- [ProcessTrigger_SyncErrors](#BKMK_ProcessTrigger_SyncErrors)
- [provisionlanguageforuser_SyncErrors](#BKMK_provisionlanguageforuser_SyncErrors)
- [Publisher_SyncErrors](#BKMK_Publisher_SyncErrors)
- [purviewlabelinfo_SyncErrors](#BKMK_purviewlabelinfo_SyncErrors)
- [Queue_SyncErrors](#BKMK_Queue_SyncErrors)
- [QueueItem_SyncErrors](#BKMK_QueueItem_SyncErrors)
- [recordfilter_SyncErrors](#BKMK_recordfilter_SyncErrors)
- [RecurringAppointmentMaster_SyncErrors](#BKMK_RecurringAppointmentMaster_SyncErrors)
- [recyclebinconfig_SyncErrors](#BKMK_recyclebinconfig_SyncErrors)
- [relationshipattribute_SyncErrors](#BKMK_relationshipattribute_SyncErrors)
- [Report_SyncErrors](#BKMK_Report_SyncErrors)
- [ReportCategory_SyncErrors](#BKMK_ReportCategory_SyncErrors)
- [reportparameter_SyncErrors](#BKMK_reportparameter_SyncErrors)
- [retaineddataexcel_SyncErrors](#BKMK_retaineddataexcel_SyncErrors)
- [retentionconfig_SyncErrors](#BKMK_retentionconfig_SyncErrors)
- [retentionfailuredetail_SyncErrors](#BKMK_retentionfailuredetail_SyncErrors)
- [retentionoperation_SyncErrors](#BKMK_retentionoperation_SyncErrors)
- [retentionoperationdetail_SyncErrors](#BKMK_retentionoperationdetail_SyncErrors)
- [retentionsuccessdetail_SyncErrors](#BKMK_retentionsuccessdetail_SyncErrors)
- [Role_SyncErrors](#BKMK_Role_SyncErrors)
- [roleeditorlayout_SyncErrors](#BKMK_roleeditorlayout_SyncErrors)
- [RollupField_SyncErrors](#BKMK_RollupField_SyncErrors)
- [sa_suggestedaction_SyncErrors](#BKMK_sa_suggestedaction_SyncErrors)
- [sa_suggestedactioncriteria_SyncErrors](#BKMK_sa_suggestedactioncriteria_SyncErrors)
- [SavedQuery_SyncErrors](#BKMK_SavedQuery_SyncErrors)
- [SavedQueryVisualization_SyncErrors](#BKMK_SavedQueryVisualization_SyncErrors)
- [savingrule_SyncErrors](#BKMK_savingrule_SyncErrors)
- [searchattributesettings_SyncErrors](#BKMK_searchattributesettings_SyncErrors)
- [searchcustomanalyzer_SyncErrors](#BKMK_searchcustomanalyzer_SyncErrors)
- [searchrelationshipsettings_SyncErrors](#BKMK_searchrelationshipsettings_SyncErrors)
- [sensitivitylabelattributemapping_SyncErrors](#BKMK_sensitivitylabelattributemapping_SyncErrors)
- [serviceplan_SyncErrors](#BKMK_serviceplan_SyncErrors)
- [serviceplanmapping_SyncErrors](#BKMK_serviceplanmapping_SyncErrors)
- [sharedlinksetting_SyncErrors](#BKMK_sharedlinksetting_SyncErrors)
- [sharedobject_SyncErrors](#BKMK_sharedobject_SyncErrors)
- [sharedworkspace_SyncErrors](#BKMK_sharedworkspace_SyncErrors)
- [sharedworkspacepool_SyncErrors](#BKMK_sharedworkspacepool_SyncErrors)
- [SharePointDocumentLocation_SyncErrors](#BKMK_SharePointDocumentLocation_SyncErrors)
- [sharepointmanagedidentity_SyncErrors](#BKMK_sharepointmanagedidentity_SyncErrors)
- [SharePointSite_SyncErrors](#BKMK_SharePointSite_SyncErrors)
- [sideloadedaiplugin_SyncErrors](#BKMK_sideloadedaiplugin_SyncErrors)
- [SLA_SyncErrors](#BKMK_SLA_SyncErrors)
- [SLAItem_SyncErrors](#BKMK_SLAItem_SyncErrors)
- [SLAKPIInstance_SyncErrors](#BKMK_SLAKPIInstance_SyncErrors)
- [SocialActivity_SyncErrors](#BKMK_SocialActivity_SyncErrors)
- [SocialProfile_SyncErrors](#BKMK_SocialProfile_SyncErrors)
- [Solution_SyncErrors](#BKMK_Solution_SyncErrors)
- [solutioncomponentattributeconfiguration_SyncErrors](#BKMK_solutioncomponentattributeconfiguration_SyncErrors)
- [solutioncomponentbatchconfiguration_SyncErrors](#BKMK_solutioncomponentbatchconfiguration_SyncErrors)
- [solutioncomponentconfiguration_SyncErrors](#BKMK_solutioncomponentconfiguration_SyncErrors)
- [solutioncomponentrelationshipconfiguration_SyncErrors](#BKMK_solutioncomponentrelationshipconfiguration_SyncErrors)
- [stagedentity_SyncErrors](#BKMK_stagedentity_SyncErrors)
- [stagedentityattribute_SyncErrors](#BKMK_stagedentityattribute_SyncErrors)
- [stagedmetadataasyncoperation_SyncErrors](#BKMK_stagedmetadataasyncoperation_SyncErrors)
- [stagesolutionupload_SyncErrors](#BKMK_stagesolutionupload_SyncErrors)
- [Subject_SyncErrors](#BKMK_Subject_SyncErrors)
- [supportusertable_SyncErrors](#BKMK_supportusertable_SyncErrors)
- [synapsedatabase_SyncErrors](#BKMK_synapsedatabase_SyncErrors)
- [synapselinkexternaltablestate_SyncErrors](#BKMK_synapselinkexternaltablestate_SyncErrors)
- [synapselinkprofile_SyncErrors](#BKMK_synapselinkprofile_SyncErrors)
- [synapselinkprofileentity_SyncErrors](#BKMK_synapselinkprofileentity_SyncErrors)
- [synapselinkprofileentitystate_SyncErrors](#BKMK_synapselinkprofileentitystate_SyncErrors)
- [synapselinkschedule_SyncErrors](#BKMK_synapselinkschedule_SyncErrors)
- [SyncError_SyncErrors](#BKMK_SyncError_SyncErrors-many-to-one)
- [SystemUser_SyncError](#BKMK_SystemUser_SyncError)
- [SystemUser_SyncErrors](#BKMK_SystemUser_SyncErrors)
- [systemuserauthorizationchangetracker_SyncErrors](#BKMK_systemuserauthorizationchangetracker_SyncErrors)
- [tag_SyncErrors](#BKMK_tag_SyncErrors)
- [taggedflowsession_SyncErrors](#BKMK_taggedflowsession_SyncErrors)
- [taggedprocess_SyncErrors](#BKMK_taggedprocess_SyncErrors)
- [Task_SyncErrors](#BKMK_Task_SyncErrors)
- [team_SyncError](#BKMK_team_SyncError)
- [Team_SyncErrors](#BKMK_Team_SyncErrors)
- [teammobileofflineprofilemembership_SyncErrors](#BKMK_teammobileofflineprofilemembership_SyncErrors)
- [TeamTemplate_SyncErrors](#BKMK_TeamTemplate_SyncErrors)
- [Template_SyncErrors](#BKMK_Template_SyncErrors)
- [Territory_SyncErrors](#BKMK_Territory_SyncErrors)
- [TransactionCurrency_SyncErrors](#BKMK_TransactionCurrency_SyncErrors)
- [TranslationProcess_SyncErrors](#BKMK_TranslationProcess_SyncErrors)
- [unstructuredfilesearchentity_SyncErrors](#BKMK_unstructuredfilesearchentity_SyncErrors)
- [unstructuredfilesearchrecord_SyncErrors](#BKMK_unstructuredfilesearchrecord_SyncErrors)
- [usermobileofflineprofilemembership_SyncErrors](#BKMK_usermobileofflineprofilemembership_SyncErrors)
- [UserQuery_SyncErrors](#BKMK_UserQuery_SyncErrors)
- [UserQueryVisualization_SyncErrors](#BKMK_UserQueryVisualization_SyncErrors)
- [userrating_SyncErrors](#BKMK_userrating_SyncErrors)
- [viewasexamplequestion_SyncErrors](#BKMK_viewasexamplequestion_SyncErrors)
- [virtualentitymetadata_SyncErrors](#BKMK_virtualentitymetadata_SyncErrors)
- [Workflow_SyncErrors](#BKMK_Workflow_SyncErrors)
- [workflowbinary_SyncErrors](#BKMK_workflowbinary_SyncErrors)
- [workflowmetadata_SyncErrors](#BKMK_workflowmetadata_SyncErrors)
- [workqueue_SyncErrors](#BKMK_workqueue_SyncErrors)
- [workqueueitem_SyncErrors](#BKMK_workqueueitem_SyncErrors)

### <a name="BKMK_Account_SyncErrors"></a> Account_SyncErrors

One-To-Many Relationship: [account Account_SyncErrors](account.md#BKMK_Account_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_account_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_activityfileattachment_SyncErrors"></a> activityfileattachment_SyncErrors

One-To-Many Relationship: [activityfileattachment activityfileattachment_SyncErrors](activityfileattachment.md#BKMK_activityfileattachment_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`activityfileattachment`|
|ReferencedAttribute|`activityfileattachmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_activityfileattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ActivityMimeAttachment_SyncErrors"></a> ActivityMimeAttachment_SyncErrors

One-To-Many Relationship: [activitymimeattachment ActivityMimeAttachment_SyncErrors](activitymimeattachment.md#BKMK_ActivityMimeAttachment_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`activitymimeattachment`|
|ReferencedAttribute|`activitymimeattachmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_activitymimeattachment_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_ActivityParty_SyncErrors"></a> ActivityParty_SyncErrors

One-To-Many Relationship: [activityparty ActivityParty_SyncErrors](activityparty.md#BKMK_ActivityParty_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`activityparty`|
|ReferencedAttribute|`activitypartyid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_activityparty_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_adx_externalidentity_SyncErrors"></a> adx_externalidentity_SyncErrors

One-To-Many Relationship: [adx_externalidentity adx_externalidentity_SyncErrors](adx_externalidentity.md#BKMK_adx_externalidentity_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_externalidentity`|
|ReferencedAttribute|`adx_externalidentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_externalidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_invitation_SyncErrors"></a> adx_invitation_SyncErrors

One-To-Many Relationship: [adx_invitation adx_invitation_SyncErrors](adx_invitation.md#BKMK_adx_invitation_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_invitation`|
|ReferencedAttribute|`adx_invitationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_invitation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_inviteredemption_SyncErrors"></a> adx_inviteredemption_SyncErrors

One-To-Many Relationship: [adx_inviteredemption adx_inviteredemption_SyncErrors](adx_inviteredemption.md#BKMK_adx_inviteredemption_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_inviteredemption`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_inviteredemption`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_portalcomment_SyncErrors"></a> adx_portalcomment_SyncErrors

One-To-Many Relationship: [adx_portalcomment adx_portalcomment_SyncErrors](adx_portalcomment.md#BKMK_adx_portalcomment_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_portalcomment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_portalcomment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_setting_SyncErrors"></a> adx_setting_SyncErrors

One-To-Many Relationship: [adx_setting adx_setting_SyncErrors](adx_setting.md#BKMK_adx_setting_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_setting`|
|ReferencedAttribute|`adx_settingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_setting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_webformsession_SyncErrors"></a> adx_webformsession_SyncErrors

One-To-Many Relationship: [adx_webformsession adx_webformsession_SyncErrors](adx_webformsession.md#BKMK_adx_webformsession_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_webformsession`|
|ReferencedAttribute|`adx_webformsessionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_webformsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aicopilot_SyncErrors"></a> aicopilot_SyncErrors

One-To-Many Relationship: [aicopilot aicopilot_SyncErrors](aicopilot.md#BKMK_aicopilot_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`aicopilot`|
|ReferencedAttribute|`aicopilotid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aicopilot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugin_SyncErrors"></a> aiplugin_SyncErrors

One-To-Many Relationship: [aiplugin aiplugin_SyncErrors](aiplugin.md#BKMK_aiplugin_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugin`|
|ReferencedAttribute|`aipluginid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugin`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginauth_SyncErrors"></a> aipluginauth_SyncErrors

One-To-Many Relationship: [aipluginauth aipluginauth_SyncErrors](aipluginauth.md#BKMK_aipluginauth_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginauth`|
|ReferencedAttribute|`aipluginauthid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginauth`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginconversationstarter_SyncErrors"></a> aipluginconversationstarter_SyncErrors

One-To-Many Relationship: [aipluginconversationstarter aipluginconversationstarter_SyncErrors](aipluginconversationstarter.md#BKMK_aipluginconversationstarter_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginconversationstarter`|
|ReferencedAttribute|`aipluginconversationstarterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginconversationstarter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginconversationstartermapping_SyncErrors"></a> aipluginconversationstartermapping_SyncErrors

One-To-Many Relationship: [aipluginconversationstartermapping aipluginconversationstartermapping_SyncErrors](aipluginconversationstartermapping.md#BKMK_aipluginconversationstartermapping_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginconversationstartermapping`|
|ReferencedAttribute|`aipluginconversationstartermappingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginconversationstartermapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginexternalschema_SyncErrors"></a> aipluginexternalschema_SyncErrors

One-To-Many Relationship: [aipluginexternalschema aipluginexternalschema_SyncErrors](aipluginexternalschema.md#BKMK_aipluginexternalschema_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginexternalschema`|
|ReferencedAttribute|`aipluginexternalschemaid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginexternalschema`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginexternalschemaproperty_SyncErrors"></a> aipluginexternalschemaproperty_SyncErrors

One-To-Many Relationship: [aipluginexternalschemaproperty aipluginexternalschemaproperty_SyncErrors](aipluginexternalschemaproperty.md#BKMK_aipluginexternalschemaproperty_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginexternalschemaproperty`|
|ReferencedAttribute|`aipluginexternalschemapropertyid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginexternalschemaproperty`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugingovernance_SyncErrors"></a> aiplugingovernance_SyncErrors

One-To-Many Relationship: [aiplugingovernance aiplugingovernance_SyncErrors](aiplugingovernance.md#BKMK_aiplugingovernance_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugingovernance`|
|ReferencedAttribute|`aiplugingovernanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugingovernance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugingovernanceext_SyncErrors"></a> aiplugingovernanceext_SyncErrors

One-To-Many Relationship: [aiplugingovernanceext aiplugingovernanceext_SyncErrors](aiplugingovernanceext.md#BKMK_aiplugingovernanceext_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugingovernanceext`|
|ReferencedAttribute|`aiplugingovernanceextid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugingovernanceext`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugininstance_SyncErrors"></a> aiplugininstance_SyncErrors

One-To-Many Relationship: [aiplugininstance aiplugininstance_SyncErrors](aiplugininstance.md#BKMK_aiplugininstance_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugininstance`|
|ReferencedAttribute|`aiplugininstanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugininstance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperation_SyncErrors"></a> aipluginoperation_SyncErrors

One-To-Many Relationship: [aipluginoperation aipluginoperation_SyncErrors](aipluginoperation.md#BKMK_aipluginoperation_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperation`|
|ReferencedAttribute|`aipluginoperationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperationparameter_SyncErrors"></a> aipluginoperationparameter_SyncErrors

One-To-Many Relationship: [aipluginoperationparameter aipluginoperationparameter_SyncErrors](aipluginoperationparameter.md#BKMK_aipluginoperationparameter_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperationparameter`|
|ReferencedAttribute|`aipluginoperationparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginoperationparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperationresponsetemplate_SyncErrors"></a> aipluginoperationresponsetemplate_SyncErrors

One-To-Many Relationship: [aipluginoperationresponsetemplate aipluginoperationresponsetemplate_SyncErrors](aipluginoperationresponsetemplate.md#BKMK_aipluginoperationresponsetemplate_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperationresponsetemplate`|
|ReferencedAttribute|`aipluginoperationresponsetemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginoperationresponsetemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugintitle_SyncErrors"></a> aiplugintitle_SyncErrors

One-To-Many Relationship: [aiplugintitle aiplugintitle_SyncErrors](aiplugintitle.md#BKMK_aiplugintitle_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugintitle`|
|ReferencedAttribute|`aiplugintitleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugintitle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginusersetting_SyncErrors"></a> aipluginusersetting_SyncErrors

One-To-Many Relationship: [aipluginusersetting aipluginusersetting_SyncErrors](aipluginusersetting.md#BKMK_aipluginusersetting_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginusersetting`|
|ReferencedAttribute|`aipluginusersettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginusersetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_allowedmcpclient_SyncErrors"></a> allowedmcpclient_SyncErrors

One-To-Many Relationship: [allowedmcpclient allowedmcpclient_SyncErrors](allowedmcpclient.md#BKMK_allowedmcpclient_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`allowedmcpclient`|
|ReferencedAttribute|`allowedmcpclientid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_allowedmcpclient`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Annotation_SyncErrors"></a> Annotation_SyncErrors

One-To-Many Relationship: [annotation Annotation_SyncErrors](annotation.md#BKMK_Annotation_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`annotation`|
|ReferencedAttribute|`annotationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_annotation_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_appaction_SyncErrors"></a> appaction_SyncErrors

One-To-Many Relationship: [appaction appaction_SyncErrors](appaction.md#BKMK_appaction_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`appaction`|
|ReferencedAttribute|`appactionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_appaction`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appactionmigration_SyncErrors"></a> appactionmigration_SyncErrors

One-To-Many Relationship: [appactionmigration appactionmigration_SyncErrors](appactionmigration.md#BKMK_appactionmigration_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`appactionmigration`|
|ReferencedAttribute|`appactionmigrationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_appactionmigration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appactionrule_SyncErrors"></a> appactionrule_SyncErrors

One-To-Many Relationship: [appactionrule appactionrule_SyncErrors](appactionrule.md#BKMK_appactionrule_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`appactionrule`|
|ReferencedAttribute|`appactionruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_appactionrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_application_SyncErrors"></a> application_SyncErrors

One-To-Many Relationship: [application application_SyncErrors](application.md#BKMK_application_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`application`|
|ReferencedAttribute|`applicationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_application`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_applicationuser_SyncErrors"></a> applicationuser_SyncErrors

One-To-Many Relationship: [applicationuser applicationuser_SyncErrors](applicationuser.md#BKMK_applicationuser_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`applicationuser`|
|ReferencedAttribute|`applicationuserid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_applicationuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Appointment_SyncErrors"></a> Appointment_SyncErrors

One-To-Many Relationship: [appointment Appointment_SyncErrors](appointment.md#BKMK_Appointment_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`appointment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_appointment_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_approvalprocess_SyncErrors"></a> approvalprocess_SyncErrors

One-To-Many Relationship: [approvalprocess approvalprocess_SyncErrors](approvalprocess.md#BKMK_approvalprocess_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalprocess`|
|ReferencedAttribute|`approvalprocessid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageapproval_SyncErrors"></a> approvalstageapproval_SyncErrors

One-To-Many Relationship: [approvalstageapproval approvalstageapproval_SyncErrors](approvalstageapproval.md#BKMK_approvalstageapproval_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageapproval`|
|ReferencedAttribute|`approvalstageapprovalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalstageapproval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstagecondition_SyncErrors"></a> approvalstagecondition_SyncErrors

One-To-Many Relationship: [approvalstagecondition approvalstagecondition_SyncErrors](approvalstagecondition.md#BKMK_approvalstagecondition_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstagecondition`|
|ReferencedAttribute|`approvalstageconditionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalstagecondition`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageintelligent_SyncErrors"></a> approvalstageintelligent_SyncErrors

One-To-Many Relationship: [approvalstageintelligent approvalstageintelligent_SyncErrors](approvalstageintelligent.md#BKMK_approvalstageintelligent_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageintelligent`|
|ReferencedAttribute|`approvalstageintelligentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalstageintelligent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageorder_SyncErrors"></a> approvalstageorder_SyncErrors

One-To-Many Relationship: [approvalstageorder approvalstageorder_SyncErrors](approvalstageorder.md#BKMK_approvalstageorder_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageorder`|
|ReferencedAttribute|`approvalstageorderid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalstageorder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Attachment_SyncErrors"></a> Attachment_SyncErrors

One-To-Many Relationship: [attachment Attachment_SyncErrors](attachment.md#BKMK_Attachment_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`attachment`|
|ReferencedAttribute|`attachmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_attachment_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_attributeclusterconfig_SyncErrors"></a> attributeclusterconfig_SyncErrors

One-To-Many Relationship: [attributeclusterconfig attributeclusterconfig_SyncErrors](attributeclusterconfig.md#BKMK_attributeclusterconfig_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`attributeclusterconfig`|
|ReferencedAttribute|`attributeclusterconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_attributeclusterconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_attributeimageconfig_SyncErrors"></a> attributeimageconfig_SyncErrors

One-To-Many Relationship: [attributeimageconfig attributeimageconfig_SyncErrors](attributeimageconfig.md#BKMK_attributeimageconfig_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`attributeimageconfig`|
|ReferencedAttribute|`attributeimageconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_attributeimageconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_attributemaskingrule_SyncErrors"></a> attributemaskingrule_SyncErrors

One-To-Many Relationship: [attributemaskingrule attributemaskingrule_SyncErrors](attributemaskingrule.md#BKMK_attributemaskingrule_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`attributemaskingrule`|
|ReferencedAttribute|`attributemaskingruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_attributemaskingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_attributepicklistvalue_SyncErrors"></a> attributepicklistvalue_SyncErrors

One-To-Many Relationship: [attributepicklistvalue attributepicklistvalue_SyncErrors](attributepicklistvalue.md#BKMK_attributepicklistvalue_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`attributepicklistvalue`|
|ReferencedAttribute|`attributepicklistvalueid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_attributepicklistvalue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_bot_SyncErrors"></a> bot_SyncErrors

One-To-Many Relationship: [bot bot_SyncErrors](bot.md#BKMK_bot_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`bot`|
|ReferencedAttribute|`botid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_bot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_botcomponent_SyncErrors"></a> botcomponent_SyncErrors

One-To-Many Relationship: [botcomponent botcomponent_SyncErrors](botcomponent.md#BKMK_botcomponent_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`botcomponent`|
|ReferencedAttribute|`botcomponentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_botcomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_botcomponentcollection_SyncErrors"></a> botcomponentcollection_SyncErrors

One-To-Many Relationship: [botcomponentcollection botcomponentcollection_SyncErrors](botcomponentcollection.md#BKMK_botcomponentcollection_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`botcomponentcollection`|
|ReferencedAttribute|`botcomponentcollectionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_botcomponentcollection`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_businessprocess_SyncErrors"></a> businessprocess_SyncErrors

One-To-Many Relationship: [businessprocess businessprocess_SyncErrors](businessprocess.md#BKMK_businessprocess_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`businessprocess`|
|ReferencedAttribute|`businessprocessid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_businessprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_BusinessUnit_SyncError"></a> BusinessUnit_SyncError

One-To-Many Relationship: [businessunit BusinessUnit_SyncError](businessunit.md#BKMK_BusinessUnit_SyncError)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_BusinessUnit_SyncErrors"></a> BusinessUnit_SyncErrors

One-To-Many Relationship: [businessunit BusinessUnit_SyncErrors](businessunit.md#BKMK_BusinessUnit_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_businessunit_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `NoCascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_card_SyncErrors"></a> card_SyncErrors

One-To-Many Relationship: [card card_SyncErrors](card.md#BKMK_card_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`card`|
|ReferencedAttribute|`cardid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_card`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_catalog_SyncErrors"></a> catalog_SyncErrors

One-To-Many Relationship: [catalog catalog_SyncErrors](catalog.md#BKMK_catalog_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`catalog`|
|ReferencedAttribute|`catalogid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_catalog`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_catalogassignment_SyncErrors"></a> catalogassignment_SyncErrors

One-To-Many Relationship: [catalogassignment catalogassignment_SyncErrors](catalogassignment.md#BKMK_catalogassignment_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`catalogassignment`|
|ReferencedAttribute|`catalogassignmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_catalogassignment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Category_SyncErrors"></a> Category_SyncErrors

One-To-Many Relationship: [category Category_SyncErrors](category.md#BKMK_Category_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`category`|
|ReferencedAttribute|`categoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_category_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_certificatecredential_SyncErrors"></a> certificatecredential_SyncErrors

One-To-Many Relationship: [certificatecredential certificatecredential_SyncErrors](certificatecredential.md#BKMK_certificatecredential_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`certificatecredential`|
|ReferencedAttribute|`certificatecredentialid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_certificatecredential`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_chat_SyncErrors"></a> chat_SyncErrors

One-To-Many Relationship: [chat chat_SyncErrors](chat.md#BKMK_chat_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`chat`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_chat`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Connection_SyncErrors"></a> Connection_SyncErrors

One-To-Many Relationship: [connection Connection_SyncErrors](connection.md#BKMK_Connection_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`connection`|
|ReferencedAttribute|`connectionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_connection_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_connectioninstance_SyncErrors"></a> connectioninstance_SyncErrors

One-To-Many Relationship: [connectioninstance connectioninstance_SyncErrors](connectioninstance.md#BKMK_connectioninstance_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`connectioninstance`|
|ReferencedAttribute|`connectioninstanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_connectioninstance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connectionreference_SyncErrors"></a> connectionreference_SyncErrors

One-To-Many Relationship: [connectionreference connectionreference_SyncErrors](connectionreference.md#BKMK_connectionreference_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`connectionreference`|
|ReferencedAttribute|`connectionreferenceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_connectionreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ConnectionRole_SyncErrors"></a> ConnectionRole_SyncErrors

One-To-Many Relationship: [connectionrole ConnectionRole_SyncErrors](connectionrole.md#BKMK_ConnectionRole_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`connectionrole`|
|ReferencedAttribute|`connectionroleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_connectionrole_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_connector_SyncErrors"></a> connector_SyncErrors

One-To-Many Relationship: [connector connector_SyncErrors](connector.md#BKMK_connector_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`connector`|
|ReferencedAttribute|`connectorid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_connector`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Contact_SyncErrors"></a> Contact_SyncErrors

One-To-Many Relationship: [contact Contact_SyncErrors](contact.md#BKMK_Contact_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_contact_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_conversationtranscript_SyncErrors"></a> conversationtranscript_SyncErrors

One-To-Many Relationship: [conversationtranscript conversationtranscript_SyncErrors](conversationtranscript.md#BKMK_conversationtranscript_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`conversationtranscript`|
|ReferencedAttribute|`conversationtranscriptid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_conversationtranscript`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_copilotexamplequestion_SyncErrors"></a> copilotexamplequestion_SyncErrors

One-To-Many Relationship: [copilotexamplequestion copilotexamplequestion_SyncErrors](copilotexamplequestion.md#BKMK_copilotexamplequestion_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`copilotexamplequestion`|
|ReferencedAttribute|`copilotexamplequestionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_copilotexamplequestion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_copilotglossaryterm_SyncErrors"></a> copilotglossaryterm_SyncErrors

One-To-Many Relationship: [copilotglossaryterm copilotglossaryterm_SyncErrors](copilotglossaryterm.md#BKMK_copilotglossaryterm_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`copilotglossaryterm`|
|ReferencedAttribute|`copilotglossarytermid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_copilotglossaryterm`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_copilotsynonyms_SyncErrors"></a> copilotsynonyms_SyncErrors

One-To-Many Relationship: [copilotsynonyms copilotsynonyms_SyncErrors](copilotsynonyms.md#BKMK_copilotsynonyms_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`copilotsynonyms`|
|ReferencedAttribute|`copilotsynonymsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_copilotsynonyms`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_credential_SyncErrors"></a> credential_SyncErrors

One-To-Many Relationship: [credential credential_SyncErrors](credential.md#BKMK_credential_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`credential`|
|ReferencedAttribute|`credentialid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_credential`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_customapi_SyncErrors"></a> customapi_SyncErrors

One-To-Many Relationship: [customapi customapi_SyncErrors](customapi.md#BKMK_customapi_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`customapi`|
|ReferencedAttribute|`customapiid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_customapi`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_customapirequestparameter_SyncErrors"></a> customapirequestparameter_SyncErrors

One-To-Many Relationship: [customapirequestparameter customapirequestparameter_SyncErrors](customapirequestparameter.md#BKMK_customapirequestparameter_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`customapirequestparameter`|
|ReferencedAttribute|`customapirequestparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_customapirequestparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_customapiresponseproperty_SyncErrors"></a> customapiresponseproperty_SyncErrors

One-To-Many Relationship: [customapiresponseproperty customapiresponseproperty_SyncErrors](customapiresponseproperty.md#BKMK_customapiresponseproperty_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`customapiresponseproperty`|
|ReferencedAttribute|`customapiresponsepropertyid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_customapiresponseproperty`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_CustomerAddress_SyncErrors"></a> CustomerAddress_SyncErrors

One-To-Many Relationship: [customeraddress CustomerAddress_SyncErrors](customeraddress.md#BKMK_CustomerAddress_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`customeraddress`|
|ReferencedAttribute|`customeraddressid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_customeraddress_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_datalakefolder_SyncErrors"></a> datalakefolder_SyncErrors

One-To-Many Relationship: [datalakefolder datalakefolder_SyncErrors](datalakefolder.md#BKMK_datalakefolder_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakefolder`|
|ReferencedAttribute|`datalakefolderid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_datalakefolder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakefolderpermission_SyncErrors"></a> datalakefolderpermission_SyncErrors

One-To-Many Relationship: [datalakefolderpermission datalakefolderpermission_SyncErrors](datalakefolderpermission.md#BKMK_datalakefolderpermission_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakefolderpermission`|
|ReferencedAttribute|`datalakefolderpermissionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_datalakefolderpermission`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakeworkspace_SyncErrors"></a> datalakeworkspace_SyncErrors

One-To-Many Relationship: [datalakeworkspace datalakeworkspace_SyncErrors](datalakeworkspace.md#BKMK_datalakeworkspace_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakeworkspace`|
|ReferencedAttribute|`datalakeworkspaceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_datalakeworkspace`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakeworkspacepermission_SyncErrors"></a> datalakeworkspacepermission_SyncErrors

One-To-Many Relationship: [datalakeworkspacepermission datalakeworkspacepermission_SyncErrors](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakeworkspacepermission`|
|ReferencedAttribute|`datalakeworkspacepermissionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_datalakeworkspacepermission`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dataprocessingconfiguration_SyncErrors"></a> dataprocessingconfiguration_SyncErrors

One-To-Many Relationship: [dataprocessingconfiguration dataprocessingconfiguration_SyncErrors](dataprocessingconfiguration.md#BKMK_dataprocessingconfiguration_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`dataprocessingconfiguration`|
|ReferencedAttribute|`dataprocessingconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dataprocessingconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_delegatedauthorization_SyncErrors"></a> delegatedauthorization_SyncErrors

One-To-Many Relationship: [delegatedauthorization delegatedauthorization_SyncErrors](delegatedauthorization.md#BKMK_delegatedauthorization_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`delegatedauthorization`|
|ReferencedAttribute|`delegatedauthorizationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_delegatedauthorization`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_desktopflowbinary_SyncErrors"></a> desktopflowbinary_SyncErrors

One-To-Many Relationship: [desktopflowbinary desktopflowbinary_SyncErrors](desktopflowbinary.md#BKMK_desktopflowbinary_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`desktopflowbinary`|
|ReferencedAttribute|`desktopflowbinaryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_desktopflowbinary`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_desktopflowmodule_SyncErrors"></a> desktopflowmodule_SyncErrors

One-To-Many Relationship: [desktopflowmodule desktopflowmodule_SyncErrors](desktopflowmodule.md#BKMK_desktopflowmodule_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`desktopflowmodule`|
|ReferencedAttribute|`desktopflowmoduleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_desktopflowmodule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_DuplicateRule_SyncErrors"></a> DuplicateRule_SyncErrors

One-To-Many Relationship: [duplicaterule DuplicateRule_SyncErrors](duplicaterule.md#BKMK_DuplicateRule_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`duplicaterule`|
|ReferencedAttribute|`duplicateruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_duplicaterule_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_DuplicateRuleCondition_SyncErrors"></a> DuplicateRuleCondition_SyncErrors

One-To-Many Relationship: [duplicaterulecondition DuplicateRuleCondition_SyncErrors](duplicaterulecondition.md#BKMK_DuplicateRuleCondition_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`duplicaterulecondition`|
|ReferencedAttribute|`duplicateruleconditionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_duplicaterulecondition_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_dvfilesearch_SyncErrors"></a> dvfilesearch_SyncErrors

One-To-Many Relationship: [dvfilesearch dvfilesearch_SyncErrors](dvfilesearch.md#BKMK_dvfilesearch_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`dvfilesearch`|
|ReferencedAttribute|`dvfilesearchid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvfilesearch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvfilesearchattribute_SyncErrors"></a> dvfilesearchattribute_SyncErrors

One-To-Many Relationship: [dvfilesearchattribute dvfilesearchattribute_SyncErrors](dvfilesearchattribute.md#BKMK_dvfilesearchattribute_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`dvfilesearchattribute`|
|ReferencedAttribute|`dvfilesearchattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvfilesearchattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvfilesearchentity_SyncErrors"></a> dvfilesearchentity_SyncErrors

One-To-Many Relationship: [dvfilesearchentity dvfilesearchentity_SyncErrors](dvfilesearchentity.md#BKMK_dvfilesearchentity_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`dvfilesearchentity`|
|ReferencedAttribute|`dvfilesearchentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvfilesearchentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvtablesearch_SyncErrors"></a> dvtablesearch_SyncErrors

One-To-Many Relationship: [dvtablesearch dvtablesearch_SyncErrors](dvtablesearch.md#BKMK_dvtablesearch_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`dvtablesearch`|
|ReferencedAttribute|`dvtablesearchid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvtablesearch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvtablesearchattribute_SyncErrors"></a> dvtablesearchattribute_SyncErrors

One-To-Many Relationship: [dvtablesearchattribute dvtablesearchattribute_SyncErrors](dvtablesearchattribute.md#BKMK_dvtablesearchattribute_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`dvtablesearchattribute`|
|ReferencedAttribute|`dvtablesearchattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvtablesearchattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvtablesearchentity_SyncErrors"></a> dvtablesearchentity_SyncErrors

One-To-Many Relationship: [dvtablesearchentity dvtablesearchentity_SyncErrors](dvtablesearchentity.md#BKMK_dvtablesearchentity_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`dvtablesearchentity`|
|ReferencedAttribute|`dvtablesearchentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvtablesearchentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Email_SyncErrors"></a> Email_SyncErrors

One-To-Many Relationship: [email Email_SyncErrors](email.md#BKMK_Email_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`email`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_email_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_emailaddressconfiguration_SyncErrors"></a> emailaddressconfiguration_SyncErrors

One-To-Many Relationship: [emailaddressconfiguration emailaddressconfiguration_SyncErrors](emailaddressconfiguration.md#BKMK_emailaddressconfiguration_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`emailaddressconfiguration`|
|ReferencedAttribute|`emailaddressconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_emailaddressconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_EmailServerProfile_SyncErrors"></a> EmailServerProfile_SyncErrors

One-To-Many Relationship: [emailserverprofile EmailServerProfile_SyncErrors](emailserverprofile.md#BKMK_EmailServerProfile_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`emailserverprofile`|
|ReferencedAttribute|`emailserverprofileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_emailserverprofile_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_entityanalyticsconfig_SyncErrors"></a> entityanalyticsconfig_SyncErrors

One-To-Many Relationship: [entityanalyticsconfig entityanalyticsconfig_SyncErrors](entityanalyticsconfig.md#BKMK_entityanalyticsconfig_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`entityanalyticsconfig`|
|ReferencedAttribute|`entityanalyticsconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityanalyticsconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityclusterconfig_SyncErrors"></a> entityclusterconfig_SyncErrors

One-To-Many Relationship: [entityclusterconfig entityclusterconfig_SyncErrors](entityclusterconfig.md#BKMK_entityclusterconfig_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`entityclusterconfig`|
|ReferencedAttribute|`entityclusterconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityclusterconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityimageconfig_SyncErrors"></a> entityimageconfig_SyncErrors

One-To-Many Relationship: [entityimageconfig entityimageconfig_SyncErrors](entityimageconfig.md#BKMK_entityimageconfig_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`entityimageconfig`|
|ReferencedAttribute|`entityimageconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityimageconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityindex_SyncErrors"></a> entityindex_SyncErrors

One-To-Many Relationship: [entityindex entityindex_SyncErrors](entityindex.md#BKMK_entityindex_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`entityindex`|
|ReferencedAttribute|`indexid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityindex`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityrecordfilter_SyncErrors"></a> entityrecordfilter_SyncErrors

One-To-Many Relationship: [entityrecordfilter entityrecordfilter_SyncErrors](entityrecordfilter.md#BKMK_entityrecordfilter_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`entityrecordfilter`|
|ReferencedAttribute|`entityrecordfilterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityrecordfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariabledefinition_SyncErrors"></a> environmentvariabledefinition_SyncErrors

One-To-Many Relationship: [environmentvariabledefinition environmentvariabledefinition_SyncErrors](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariabledefinition`|
|ReferencedAttribute|`environmentvariabledefinitionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_environmentvariabledefinition`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariablevalue_SyncErrors"></a> environmentvariablevalue_SyncErrors

One-To-Many Relationship: [environmentvariablevalue environmentvariablevalue_SyncErrors](environmentvariablevalue.md#BKMK_environmentvariablevalue_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariablevalue`|
|ReferencedAttribute|`environmentvariablevalueid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_environmentvariablevalue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ExpiredProcess_SyncErrors"></a> ExpiredProcess_SyncErrors

One-To-Many Relationship: [expiredprocess ExpiredProcess_SyncErrors](expiredprocess.md#BKMK_ExpiredProcess_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`expiredprocess`|
|ReferencedAttribute|`businessprocessflowinstanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_ExpiredProcess_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_exportedexcel_SyncErrors"></a> exportedexcel_SyncErrors

One-To-Many Relationship: [exportedexcel exportedexcel_SyncErrors](exportedexcel.md#BKMK_exportedexcel_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`exportedexcel`|
|ReferencedAttribute|`exportedexcelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_exportedexcel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_exportsolutionupload_SyncErrors"></a> exportsolutionupload_SyncErrors

One-To-Many Relationship: [exportsolutionupload exportsolutionupload_SyncErrors](exportsolutionupload.md#BKMK_exportsolutionupload_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`exportsolutionupload`|
|ReferencedAttribute|`exportsolutionuploadid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_exportsolutionupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fabricaiskill_SyncErrors"></a> fabricaiskill_SyncErrors

One-To-Many Relationship: [fabricaiskill fabricaiskill_SyncErrors](fabricaiskill.md#BKMK_fabricaiskill_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`fabricaiskill`|
|ReferencedAttribute|`fabricaiskillid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_fabricaiskill`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Fax_SyncErrors"></a> Fax_SyncErrors

One-To-Many Relationship: [fax Fax_SyncErrors](fax.md#BKMK_Fax_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`fax`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_fax_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_featurecontrolsetting_SyncErrors"></a> featurecontrolsetting_SyncErrors

One-To-Many Relationship: [featurecontrolsetting featurecontrolsetting_SyncErrors](featurecontrolsetting.md#BKMK_featurecontrolsetting_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`featurecontrolsetting`|
|ReferencedAttribute|`featurecontrolsettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_featurecontrolsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_federatedknowledgeconfiguration_SyncErrors"></a> federatedknowledgeconfiguration_SyncErrors

One-To-Many Relationship: [federatedknowledgeconfiguration federatedknowledgeconfiguration_SyncErrors](federatedknowledgeconfiguration.md#BKMK_federatedknowledgeconfiguration_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`federatedknowledgeconfiguration`|
|ReferencedAttribute|`federatedknowledgeconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_federatedknowledgeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_federatedknowledgeentityconfiguration_SyncErrors"></a> federatedknowledgeentityconfiguration_SyncErrors

One-To-Many Relationship: [federatedknowledgeentityconfiguration federatedknowledgeentityconfiguration_SyncErrors](federatedknowledgeentityconfiguration.md#BKMK_federatedknowledgeentityconfiguration_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`federatedknowledgeentityconfiguration`|
|ReferencedAttribute|`federatedknowledgeentityconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_federatedknowledgeentityconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Feedback_SyncErrors"></a> Feedback_SyncErrors

One-To-Many Relationship: [feedback Feedback_SyncErrors](feedback.md#BKMK_Feedback_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`feedback`|
|ReferencedAttribute|`feedbackid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_feedback_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_FieldPermission_SyncErrors"></a> FieldPermission_SyncErrors

One-To-Many Relationship: [fieldpermission FieldPermission_SyncErrors](fieldpermission.md#BKMK_FieldPermission_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`fieldpermission`|
|ReferencedAttribute|`fieldpermissionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_fieldpermission_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_FieldSecurityProfile_SyncErrors"></a> FieldSecurityProfile_SyncErrors

One-To-Many Relationship: [fieldsecurityprofile FieldSecurityProfile_SyncErrors](fieldsecurityprofile.md#BKMK_FieldSecurityProfile_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`fieldsecurityprofile`|
|ReferencedAttribute|`fieldsecurityprofileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_fieldsecurityprofile_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_FileAttachment_SyncErrors"></a> FileAttachment_SyncErrors

One-To-Many Relationship: [fileattachment FileAttachment_SyncErrors](fileattachment.md#BKMK_FileAttachment_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_fileattachment_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_flowcapacityassignment_SyncErrors"></a> flowcapacityassignment_SyncErrors

One-To-Many Relationship: [flowcapacityassignment flowcapacityassignment_SyncErrors](flowcapacityassignment.md#BKMK_flowcapacityassignment_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`flowcapacityassignment`|
|ReferencedAttribute|`flowcapacityassignmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowcapacityassignment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowcredentialapplication_SyncErrors"></a> flowcredentialapplication_SyncErrors

One-To-Many Relationship: [flowcredentialapplication flowcredentialapplication_SyncErrors](flowcredentialapplication.md#BKMK_flowcredentialapplication_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`flowcredentialapplication`|
|ReferencedAttribute|`flowcredentialapplicationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowcredentialapplication`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowevent_SyncErrors"></a> flowevent_SyncErrors

One-To-Many Relationship: [flowevent flowevent_SyncErrors](flowevent.md#BKMK_flowevent_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`flowevent`|
|ReferencedAttribute|`floweventid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowevent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachine_SyncErrors"></a> flowmachine_SyncErrors

One-To-Many Relationship: [flowmachine flowmachine_SyncErrors](flowmachine.md#BKMK_flowmachine_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachine`|
|ReferencedAttribute|`flowmachineid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachine`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinegroup_SyncErrors"></a> flowmachinegroup_SyncErrors

One-To-Many Relationship: [flowmachinegroup flowmachinegroup_SyncErrors](flowmachinegroup.md#BKMK_flowmachinegroup_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinegroup`|
|ReferencedAttribute|`flowmachinegroupid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachinegroup`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachineimage_SyncErrors"></a> flowmachineimage_SyncErrors

One-To-Many Relationship: [flowmachineimage flowmachineimage_SyncErrors](flowmachineimage.md#BKMK_flowmachineimage_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachineimage`|
|ReferencedAttribute|`flowmachineimageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachineimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachineimageversion_SyncErrors"></a> flowmachineimageversion_SyncErrors

One-To-Many Relationship: [flowmachineimageversion flowmachineimageversion_SyncErrors](flowmachineimageversion.md#BKMK_flowmachineimageversion_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachineimageversion`|
|ReferencedAttribute|`flowmachineimageversionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachineimageversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinenetwork_SyncErrors"></a> flowmachinenetwork_SyncErrors

One-To-Many Relationship: [flowmachinenetwork flowmachinenetwork_SyncErrors](flowmachinenetwork.md#BKMK_flowmachinenetwork_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinenetwork`|
|ReferencedAttribute|`flowmachinenetworkid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachinenetwork`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowsession_SyncErrors"></a> flowsession_SyncErrors

One-To-Many Relationship: [flowsession flowsession_SyncErrors](flowsession.md#BKMK_flowsession_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`flowsession`|
|ReferencedAttribute|`flowsessionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowsessionbinary_SyncErrors"></a> flowsessionbinary_SyncErrors

One-To-Many Relationship: [flowsessionbinary flowsessionbinary_SyncErrors](flowsessionbinary.md#BKMK_flowsessionbinary_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`flowsessionbinary`|
|ReferencedAttribute|`flowsessionbinaryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowsessionbinary`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fxexpression_SyncErrors"></a> fxexpression_SyncErrors

One-To-Many Relationship: [fxexpression fxexpression_SyncErrors](fxexpression.md#BKMK_fxexpression_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`fxexpression`|
|ReferencedAttribute|`fxexpressionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_fxexpression`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Goal_SyncErrors"></a> Goal_SyncErrors

One-To-Many Relationship: [goal Goal_SyncErrors](goal.md#BKMK_Goal_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`goal`|
|ReferencedAttribute|`goalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_goal_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_GoalRollupQuery_SyncErrors"></a> GoalRollupQuery_SyncErrors

One-To-Many Relationship: [goalrollupquery GoalRollupQuery_SyncErrors](goalrollupquery.md#BKMK_GoalRollupQuery_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`goalrollupquery`|
|ReferencedAttribute|`goalrollupqueryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_goalrollupquery_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_governanceconfiguration_SyncErrors"></a> governanceconfiguration_SyncErrors

One-To-Many Relationship: [governanceconfiguration governanceconfiguration_SyncErrors](governanceconfiguration.md#BKMK_governanceconfiguration_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`governanceconfiguration`|
|ReferencedAttribute|`governanceconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_governanceconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ImportMap_SyncErrors"></a> ImportMap_SyncErrors

One-To-Many Relationship: [importmap ImportMap_SyncErrors](importmap.md#BKMK_ImportMap_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`importmap`|
|ReferencedAttribute|`importmapid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_importmap_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_indexattributes_SyncErrors"></a> indexattributes_SyncErrors

One-To-Many Relationship: [indexattributes indexattributes_SyncErrors](indexattributes.md#BKMK_indexattributes_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`indexattributes`|
|ReferencedAttribute|`indexattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_indexattributes`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KbArticle_SyncErrors"></a> KbArticle_SyncErrors

One-To-Many Relationship: [kbarticle KbArticle_SyncErrors](kbarticle.md#BKMK_KbArticle_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`kbarticle`|
|ReferencedAttribute|`kbarticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_kbarticle_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_KbArticleTemplate_SyncErrors"></a> KbArticleTemplate_SyncErrors

One-To-Many Relationship: [kbarticletemplate KbArticleTemplate_SyncErrors](kbarticletemplate.md#BKMK_KbArticleTemplate_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`kbarticletemplate`|
|ReferencedAttribute|`kbarticletemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_kbarticletemplate_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_keyvaultreference_SyncErrors"></a> keyvaultreference_SyncErrors

One-To-Many Relationship: [keyvaultreference keyvaultreference_SyncErrors](keyvaultreference.md#BKMK_keyvaultreference_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`keyvaultreference`|
|ReferencedAttribute|`keyvaultreferenceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_keyvaultreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KnowledgeArticle_SyncErrors"></a> KnowledgeArticle_SyncErrors

One-To-Many Relationship: [knowledgearticle KnowledgeArticle_SyncErrors](knowledgearticle.md#BKMK_KnowledgeArticle_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgearticle_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_KnowledgeArticleViews_SyncErrors"></a> KnowledgeArticleViews_SyncErrors

One-To-Many Relationship: [knowledgearticleviews KnowledgeArticleViews_SyncErrors](knowledgearticleviews.md#BKMK_KnowledgeArticleViews_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticleviews`|
|ReferencedAttribute|`knowledgearticleviewsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgearticleviews_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_KnowledgeBaseRecord_SyncErrors"></a> KnowledgeBaseRecord_SyncErrors

One-To-Many Relationship: [knowledgebaserecord KnowledgeBaseRecord_SyncErrors](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgebaserecord`|
|ReferencedAttribute|`knowledgebaserecordid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgebaserecord_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_knowledgefaq_SyncErrors"></a> knowledgefaq_SyncErrors

One-To-Many Relationship: [knowledgefaq knowledgefaq_SyncErrors](knowledgefaq.md#BKMK_knowledgefaq_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgefaq`|
|ReferencedAttribute|`knowledgefaqid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgefaq`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Letter_SyncErrors"></a> Letter_SyncErrors

One-To-Many Relationship: [letter Letter_SyncErrors](letter.md#BKMK_Letter_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`letter`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_letter_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_lk_syncerrorbase_createdby"></a> lk_syncerrorbase_createdby

One-To-Many Relationship: [systemuser lk_syncerrorbase_createdby](systemuser.md#BKMK_lk_syncerrorbase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_syncerrorbase_createdonbehalfby"></a> lk_syncerrorbase_createdonbehalfby

One-To-Many Relationship: [systemuser lk_syncerrorbase_createdonbehalfby](systemuser.md#BKMK_lk_syncerrorbase_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_syncerrorbase_modifiedby"></a> lk_syncerrorbase_modifiedby

One-To-Many Relationship: [systemuser lk_syncerrorbase_modifiedby](systemuser.md#BKMK_lk_syncerrorbase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_syncerrorbase_modifiedonbehalfby"></a> lk_syncerrorbase_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_syncerrorbase_modifiedonbehalfby](systemuser.md#BKMK_lk_syncerrorbase_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Mailbox_SyncErrors"></a> Mailbox_SyncErrors

One-To-Many Relationship: [mailbox Mailbox_SyncErrors](mailbox.md#BKMK_Mailbox_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`mailbox`|
|ReferencedAttribute|`mailboxid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mailbox_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_MailMergeTemplate_SyncErrors"></a> MailMergeTemplate_SyncErrors

One-To-Many Relationship: [mailmergetemplate MailMergeTemplate_SyncErrors](mailmergetemplate.md#BKMK_MailMergeTemplate_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`mailmergetemplate`|
|ReferencedAttribute|`mailmergetemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mailmergetemplate_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_mainfewshot_SyncErrors"></a> mainfewshot_SyncErrors

One-To-Many Relationship: [mainfewshot mainfewshot_SyncErrors](mainfewshot.md#BKMK_mainfewshot_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`mainfewshot`|
|ReferencedAttribute|`mainfewshotid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mainfewshot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_makerfewshot_SyncErrors"></a> makerfewshot_SyncErrors

One-To-Many Relationship: [makerfewshot makerfewshot_SyncErrors](makerfewshot.md#BKMK_makerfewshot_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`makerfewshot`|
|ReferencedAttribute|`makerfewshotid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_makerfewshot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_managedidentity_SyncErrors"></a> managedidentity_SyncErrors

One-To-Many Relationship: [managedidentity managedidentity_SyncErrors](managedidentity.md#BKMK_managedidentity_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`managedidentity`|
|ReferencedAttribute|`managedidentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_managedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_maskingrule_SyncErrors"></a> maskingrule_SyncErrors

One-To-Many Relationship: [maskingrule maskingrule_SyncErrors](maskingrule.md#BKMK_maskingrule_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`maskingrule`|
|ReferencedAttribute|`maskingruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_maskingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mcpserver_SyncErrors"></a> mcpserver_SyncErrors

One-To-Many Relationship: [mcpserver mcpserver_SyncErrors](mcpserver.md#BKMK_mcpserver_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`mcpserver`|
|ReferencedAttribute|`mcpserverid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mcpserver`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mcptool_SyncErrors"></a> mcptool_SyncErrors

One-To-Many Relationship: [mcptool mcptool_SyncErrors](mcptool.md#BKMK_mcptool_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`mcptool`|
|ReferencedAttribute|`mcptoolid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mcptool`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_metadataforarchival_SyncErrors"></a> metadataforarchival_SyncErrors

One-To-Many Relationship: [metadataforarchival metadataforarchival_SyncErrors](metadataforarchival.md#BKMK_metadataforarchival_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`metadataforarchival`|
|ReferencedAttribute|`metadataforarchivalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_metadataforarchival`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Metric_SyncErrors"></a> Metric_SyncErrors

One-To-Many Relationship: [metric Metric_SyncErrors](metric.md#BKMK_Metric_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`metric`|
|ReferencedAttribute|`metricid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_metric_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_mobileofflineprofileextension_SyncErrors"></a> mobileofflineprofileextension_SyncErrors

One-To-Many Relationship: [mobileofflineprofileextension mobileofflineprofileextension_SyncErrors](mobileofflineprofileextension.md#BKMK_mobileofflineprofileextension_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`mobileofflineprofileextension`|
|ReferencedAttribute|`mobileofflineprofileextensionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mobileofflineprofileextension`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdataset_SyncErrors"></a> msdyn_aibdataset_SyncErrors

One-To-Many Relationship: [msdyn_aibdataset msdyn_aibdataset_SyncErrors](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdataset`|
|ReferencedAttribute|`msdyn_aibdatasetid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibdataset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetfile_SyncErrors"></a> msdyn_aibdatasetfile_SyncErrors

One-To-Many Relationship: [msdyn_aibdatasetfile msdyn_aibdatasetfile_SyncErrors](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetfile`|
|ReferencedAttribute|`msdyn_aibdatasetfileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibdatasetfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetrecord_SyncErrors"></a> msdyn_aibdatasetrecord_SyncErrors

One-To-Many Relationship: [msdyn_aibdatasetrecord msdyn_aibdatasetrecord_SyncErrors](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetrecord`|
|ReferencedAttribute|`msdyn_aibdatasetrecordid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibdatasetrecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetscontainer_SyncErrors"></a> msdyn_aibdatasetscontainer_SyncErrors

One-To-Many Relationship: [msdyn_aibdatasetscontainer msdyn_aibdatasetscontainer_SyncErrors](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetscontainer`|
|ReferencedAttribute|`msdyn_aibdatasetscontainerid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibdatasetscontainer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfeedbackloop_SyncErrors"></a> msdyn_aibfeedbackloop_SyncErrors

One-To-Many Relationship: [msdyn_aibfeedbackloop msdyn_aibfeedbackloop_SyncErrors](msdyn_aibfeedbackloop.md#BKMK_msdyn_aibfeedbackloop_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfeedbackloop`|
|ReferencedAttribute|`msdyn_aibfeedbackloopid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibfeedbackloop`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfile_SyncErrors"></a> msdyn_aibfile_SyncErrors

One-To-Many Relationship: [msdyn_aibfile msdyn_aibfile_SyncErrors](msdyn_aibfile.md#BKMK_msdyn_aibfile_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfile`|
|ReferencedAttribute|`msdyn_aibfileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfileattacheddata_SyncErrors"></a> msdyn_aibfileattacheddata_SyncErrors

One-To-Many Relationship: [msdyn_aibfileattacheddata msdyn_aibfileattacheddata_SyncErrors](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfileattacheddata`|
|ReferencedAttribute|`msdyn_aibfileattacheddataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibfileattacheddata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiconfiguration_SyncErrors"></a> msdyn_aiconfiguration_SyncErrors

One-To-Many Relationship: [msdyn_aiconfiguration msdyn_aiconfiguration_SyncErrors](msdyn_aiconfiguration.md#BKMK_msdyn_aiconfiguration_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiconfiguration`|
|ReferencedAttribute|`msdyn_aiconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aidataprocessingevent_SyncErrors"></a> msdyn_aidataprocessingevent_SyncErrors

One-To-Many Relationship: [msdyn_aidataprocessingevent msdyn_aidataprocessingevent_SyncErrors](msdyn_aidataprocessingevent.md#BKMK_msdyn_aidataprocessingevent_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aidataprocessingevent`|
|ReferencedAttribute|`msdyn_aidataprocessingeventid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aidataprocessingevent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aidocumenttemplate_SyncErrors"></a> msdyn_aidocumenttemplate_SyncErrors

One-To-Many Relationship: [msdyn_aidocumenttemplate msdyn_aidocumenttemplate_SyncErrors](msdyn_aidocumenttemplate.md#BKMK_msdyn_aidocumenttemplate_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aidocumenttemplate`|
|ReferencedAttribute|`msdyn_aidocumenttemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aidocumenttemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievaluationconfiguration_SyncErrors"></a> msdyn_aievaluationconfiguration_SyncErrors

One-To-Many Relationship: [msdyn_aievaluationconfiguration msdyn_aievaluationconfiguration_SyncErrors](msdyn_aievaluationconfiguration.md#BKMK_msdyn_aievaluationconfiguration_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievaluationconfiguration`|
|ReferencedAttribute|`msdyn_aievaluationconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aievaluationconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievaluationrun_SyncErrors"></a> msdyn_aievaluationrun_SyncErrors

One-To-Many Relationship: [msdyn_aievaluationrun msdyn_aievaluationrun_SyncErrors](msdyn_aievaluationrun.md#BKMK_msdyn_aievaluationrun_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievaluationrun`|
|ReferencedAttribute|`msdyn_aievaluationrunid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aievaluationrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievent_SyncErrors"></a> msdyn_aievent_SyncErrors

One-To-Many Relationship: [msdyn_aievent msdyn_aievent_SyncErrors](msdyn_aievent.md#BKMK_msdyn_aievent_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievent`|
|ReferencedAttribute|`msdyn_aieventid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aievent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aifptrainingdocument_SyncErrors"></a> msdyn_aifptrainingdocument_SyncErrors

One-To-Many Relationship: [msdyn_aifptrainingdocument msdyn_aifptrainingdocument_SyncErrors](msdyn_aifptrainingdocument.md#BKMK_msdyn_aifptrainingdocument_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aifptrainingdocument`|
|ReferencedAttribute|`msdyn_aifptrainingdocumentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aifptrainingdocument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aimodel_SyncErrors"></a> msdyn_aimodel_SyncErrors

One-To-Many Relationship: [msdyn_aimodel msdyn_aimodel_SyncErrors](msdyn_aimodel.md#BKMK_msdyn_aimodel_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aimodel`|
|ReferencedAttribute|`msdyn_aimodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aimodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodimage_SyncErrors"></a> msdyn_aiodimage_SyncErrors

One-To-Many Relationship: [msdyn_aiodimage msdyn_aiodimage_SyncErrors](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodimage`|
|ReferencedAttribute|`msdyn_aiodimageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiodimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodlabel_SyncErrors"></a> msdyn_aiodlabel_SyncErrors

One-To-Many Relationship: [msdyn_aiodlabel msdyn_aiodlabel_SyncErrors](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodlabel`|
|ReferencedAttribute|`msdyn_aiodlabelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiodlabel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodtrainingboundingbox_SyncErrors"></a> msdyn_aiodtrainingboundingbox_SyncErrors

One-To-Many Relationship: [msdyn_aiodtrainingboundingbox msdyn_aiodtrainingboundingbox_SyncErrors](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodtrainingboundingbox`|
|ReferencedAttribute|`msdyn_aiodtrainingboundingboxid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiodtrainingboundingbox`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodtrainingimage_SyncErrors"></a> msdyn_aiodtrainingimage_SyncErrors

One-To-Many Relationship: [msdyn_aiodtrainingimage msdyn_aiodtrainingimage_SyncErrors](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodtrainingimage`|
|ReferencedAttribute|`msdyn_aiodtrainingimageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiodtrainingimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitemplate_SyncErrors"></a> msdyn_aitemplate_SyncErrors

One-To-Many Relationship: [msdyn_aitemplate msdyn_aitemplate_SyncErrors](msdyn_aitemplate.md#BKMK_msdyn_aitemplate_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitemplate`|
|ReferencedAttribute|`msdyn_aitemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestcase_SyncErrors"></a> msdyn_aitestcase_SyncErrors

One-To-Many Relationship: [msdyn_aitestcase msdyn_aitestcase_SyncErrors](msdyn_aitestcase.md#BKMK_msdyn_aitestcase_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestcase`|
|ReferencedAttribute|`msdyn_aitestcaseid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestcase`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestcasedocument_SyncErrors"></a> msdyn_aitestcasedocument_SyncErrors

One-To-Many Relationship: [msdyn_aitestcasedocument msdyn_aitestcasedocument_SyncErrors](msdyn_aitestcasedocument.md#BKMK_msdyn_aitestcasedocument_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestcasedocument`|
|ReferencedAttribute|`msdyn_aitestcasedocumentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestcasedocument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestcaseinput_SyncErrors"></a> msdyn_aitestcaseinput_SyncErrors

One-To-Many Relationship: [msdyn_aitestcaseinput msdyn_aitestcaseinput_SyncErrors](msdyn_aitestcaseinput.md#BKMK_msdyn_aitestcaseinput_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestcaseinput`|
|ReferencedAttribute|`msdyn_aitestcaseinputid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestcaseinput`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestrun_SyncErrors"></a> msdyn_aitestrun_SyncErrors

One-To-Many Relationship: [msdyn_aitestrun msdyn_aitestrun_SyncErrors](msdyn_aitestrun.md#BKMK_msdyn_aitestrun_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestrun`|
|ReferencedAttribute|`msdyn_aitestrunid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestrunbatch_SyncErrors"></a> msdyn_aitestrunbatch_SyncErrors

One-To-Many Relationship: [msdyn_aitestrunbatch msdyn_aitestrunbatch_SyncErrors](msdyn_aitestrunbatch.md#BKMK_msdyn_aitestrunbatch_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestrunbatch`|
|ReferencedAttribute|`msdyn_aitestrunbatchid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestrunbatch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysiscomponent_SyncErrors"></a> msdyn_analysiscomponent_SyncErrors

One-To-Many Relationship: [msdyn_analysiscomponent msdyn_analysiscomponent_SyncErrors](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysiscomponent`|
|ReferencedAttribute|`msdyn_analysiscomponentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysiscomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisjob_SyncErrors"></a> msdyn_analysisjob_SyncErrors

One-To-Many Relationship: [msdyn_analysisjob msdyn_analysisjob_SyncErrors](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisjob`|
|ReferencedAttribute|`msdyn_analysisjobid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysisjob`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisoverride_SyncErrors"></a> msdyn_analysisoverride_SyncErrors

One-To-Many Relationship: [msdyn_analysisoverride msdyn_analysisoverride_SyncErrors](msdyn_analysisoverride.md#BKMK_msdyn_analysisoverride_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisoverride`|
|ReferencedAttribute|`msdyn_analysisoverrideid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysisoverride`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisresult_SyncErrors"></a> msdyn_analysisresult_SyncErrors

One-To-Many Relationship: [msdyn_analysisresult msdyn_analysisresult_SyncErrors](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisresult`|
|ReferencedAttribute|`msdyn_analysisresultid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysisresult`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisresultdetail_SyncErrors"></a> msdyn_analysisresultdetail_SyncErrors

One-To-Many Relationship: [msdyn_analysisresultdetail msdyn_analysisresultdetail_SyncErrors](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisresultdetail`|
|ReferencedAttribute|`msdyn_analysisresultdetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysisresultdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_appinsightsmetadata_SyncErrors"></a> msdyn_appinsightsmetadata_SyncErrors

One-To-Many Relationship: [msdyn_appinsightsmetadata msdyn_appinsightsmetadata_SyncErrors](msdyn_appinsightsmetadata.md#BKMK_msdyn_appinsightsmetadata_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_appinsightsmetadata`|
|ReferencedAttribute|`msdyn_appinsightsmetadataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_appinsightsmetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_copilotinteractions_SyncErrors"></a> msdyn_copilotinteractions_SyncErrors

One-To-Many Relationship: [msdyn_copilotinteractions msdyn_copilotinteractions_SyncErrors](msdyn_copilotinteractions.md#BKMK_msdyn_copilotinteractions_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_copilotinteractions`|
|ReferencedAttribute|`msdyn_copilotinteractionsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_copilotinteractions`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_customcontrolextendedsettings_SyncErrors"></a> msdyn_customcontrolextendedsettings_SyncErrors

One-To-Many Relationship: [msdyn_customcontrolextendedsettings msdyn_customcontrolextendedsettings_SyncErrors](msdyn_customcontrolextendedsettings.md#BKMK_msdyn_customcontrolextendedsettings_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_customcontrolextendedsettings`|
|ReferencedAttribute|`msdyn_customcontrolextendedsettingsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_customcontrolextendedsettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflow_datalakefolder_SyncErrors"></a> msdyn_dataflow_datalakefolder_SyncErrors

One-To-Many Relationship: [msdyn_dataflow_datalakefolder msdyn_dataflow_datalakefolder_SyncErrors](msdyn_dataflow_datalakefolder.md#BKMK_msdyn_dataflow_datalakefolder_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflow_datalakefolder`|
|ReferencedAttribute|`msdyn_dataflow_datalakefolderid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflow_datalakefolder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflow_SyncErrors"></a> msdyn_dataflow_SyncErrors

One-To-Many Relationship: [msdyn_dataflow msdyn_dataflow_SyncErrors](msdyn_dataflow.md#BKMK_msdyn_dataflow_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflow`|
|ReferencedAttribute|`msdyn_dataflowid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflow`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowconnectionreference_SyncErrors"></a> msdyn_dataflowconnectionreference_SyncErrors

One-To-Many Relationship: [msdyn_dataflowconnectionreference msdyn_dataflowconnectionreference_SyncErrors](msdyn_dataflowconnectionreference.md#BKMK_msdyn_dataflowconnectionreference_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowconnectionreference`|
|ReferencedAttribute|`msdyn_dataflowconnectionreferenceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflowconnectionreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowrefreshhistory_SyncErrors"></a> msdyn_dataflowrefreshhistory_SyncErrors

One-To-Many Relationship: [msdyn_dataflowrefreshhistory msdyn_dataflowrefreshhistory_SyncErrors](msdyn_dataflowrefreshhistory.md#BKMK_msdyn_dataflowrefreshhistory_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowrefreshhistory`|
|ReferencedAttribute|`msdyn_dataflowrefreshhistoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflowrefreshhistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowtemplate_SyncErrors"></a> msdyn_dataflowtemplate_SyncErrors

One-To-Many Relationship: [msdyn_dataflowtemplate msdyn_dataflowtemplate_SyncErrors](msdyn_dataflowtemplate.md#BKMK_msdyn_dataflowtemplate_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowtemplate`|
|ReferencedAttribute|`msdyn_dataflowtemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflowtemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmsrequest_SyncErrors"></a> msdyn_dmsrequest_SyncErrors

One-To-Many Relationship: [msdyn_dmsrequest msdyn_dmsrequest_SyncErrors](msdyn_dmsrequest.md#BKMK_msdyn_dmsrequest_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmsrequest`|
|ReferencedAttribute|`msdyn_dmsrequestid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dmsrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmsrequeststatus_SyncErrors"></a> msdyn_dmsrequeststatus_SyncErrors

One-To-Many Relationship: [msdyn_dmsrequeststatus msdyn_dmsrequeststatus_SyncErrors](msdyn_dmsrequeststatus.md#BKMK_msdyn_dmsrequeststatus_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmsrequeststatus`|
|ReferencedAttribute|`msdyn_dmsrequeststatusid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dmsrequeststatus`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmssyncrequest_SyncErrors"></a> msdyn_dmssyncrequest_SyncErrors

One-To-Many Relationship: [msdyn_dmssyncrequest msdyn_dmssyncrequest_SyncErrors](msdyn_dmssyncrequest.md#BKMK_msdyn_dmssyncrequest_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmssyncrequest`|
|ReferencedAttribute|`msdyn_dmssyncrequestid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dmssyncrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmssyncstatus_SyncErrors"></a> msdyn_dmssyncstatus_SyncErrors

One-To-Many Relationship: [msdyn_dmssyncstatus msdyn_dmssyncstatus_SyncErrors](msdyn_dmssyncstatus.md#BKMK_msdyn_dmssyncstatus_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmssyncstatus`|
|ReferencedAttribute|`msdyn_dmssyncstatusid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dmssyncstatus`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_entitylinkchatconfiguration_SyncErrors"></a> msdyn_entitylinkchatconfiguration_SyncErrors

One-To-Many Relationship: [msdyn_entitylinkchatconfiguration msdyn_entitylinkchatconfiguration_SyncErrors](msdyn_entitylinkchatconfiguration.md#BKMK_msdyn_entitylinkchatconfiguration_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_entitylinkchatconfiguration`|
|ReferencedAttribute|`msdyn_entitylinkchatconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_entitylinkchatconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_entityrefreshhistory_SyncErrors"></a> msdyn_entityrefreshhistory_SyncErrors

One-To-Many Relationship: [msdyn_entityrefreshhistory msdyn_entityrefreshhistory_SyncErrors](msdyn_entityrefreshhistory.md#BKMK_msdyn_entityrefreshhistory_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_entityrefreshhistory`|
|ReferencedAttribute|`msdyn_entityrefreshhistoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_entityrefreshhistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_favoriteknowledgearticle_SyncErrors"></a> msdyn_favoriteknowledgearticle_SyncErrors

One-To-Many Relationship: [msdyn_favoriteknowledgearticle msdyn_favoriteknowledgearticle_SyncErrors](msdyn_favoriteknowledgearticle.md#BKMK_msdyn_favoriteknowledgearticle_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_favoriteknowledgearticle`|
|ReferencedAttribute|`msdyn_favoriteknowledgearticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_favoriteknowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_federatedarticle_SyncErrors"></a> msdyn_federatedarticle_SyncErrors

One-To-Many Relationship: [msdyn_federatedarticle msdyn_federatedarticle_SyncErrors](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_federatedarticle`|
|ReferencedAttribute|`msdyn_federatedarticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_federatedarticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_federatedarticleincident_SyncErrors"></a> msdyn_federatedarticleincident_SyncErrors

One-To-Many Relationship: [msdyn_federatedarticleincident msdyn_federatedarticleincident_SyncErrors](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_federatedarticleincident`|
|ReferencedAttribute|`msdyn_federatedarticleincidentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_federatedarticleincident`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_fileupload_SyncErrors"></a> msdyn_fileupload_SyncErrors

One-To-Many Relationship: [msdyn_fileupload msdyn_fileupload_SyncErrors](msdyn_fileupload.md#BKMK_msdyn_fileupload_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_fileupload`|
|ReferencedAttribute|`msdyn_fileuploadid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_fileupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_actionapprovalmodel_SyncErrors"></a> msdyn_flow_actionapprovalmodel_SyncErrors

One-To-Many Relationship: [msdyn_flow_actionapprovalmodel msdyn_flow_actionapprovalmodel_SyncErrors](msdyn_flow_actionapprovalmodel.md#BKMK_msdyn_flow_actionapprovalmodel_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_actionapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_actionapprovalmodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_actionapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approval_SyncErrors"></a> msdyn_flow_approval_SyncErrors

One-To-Many Relationship: [msdyn_flow_approval msdyn_flow_approval_SyncErrors](msdyn_flow_approval.md#BKMK_msdyn_flow_approval_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approval`|
|ReferencedAttribute|`msdyn_flow_approvalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_approval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalrequest_SyncErrors"></a> msdyn_flow_approvalrequest_SyncErrors

One-To-Many Relationship: [msdyn_flow_approvalrequest msdyn_flow_approvalrequest_SyncErrors](msdyn_flow_approvalrequest.md#BKMK_msdyn_flow_approvalrequest_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalrequest`|
|ReferencedAttribute|`msdyn_flow_approvalrequestid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_approvalrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalresponse_SyncErrors"></a> msdyn_flow_approvalresponse_SyncErrors

One-To-Many Relationship: [msdyn_flow_approvalresponse msdyn_flow_approvalresponse_SyncErrors](msdyn_flow_approvalresponse.md#BKMK_msdyn_flow_approvalresponse_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalresponse`|
|ReferencedAttribute|`msdyn_flow_approvalresponseid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_approvalresponse`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalstep_SyncErrors"></a> msdyn_flow_approvalstep_SyncErrors

One-To-Many Relationship: [msdyn_flow_approvalstep msdyn_flow_approvalstep_SyncErrors](msdyn_flow_approvalstep.md#BKMK_msdyn_flow_approvalstep_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalstep`|
|ReferencedAttribute|`msdyn_flow_approvalstepid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_approvalstep`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_awaitallactionapprovalmodel_SyncErrors"></a> msdyn_flow_awaitallactionapprovalmodel_SyncErrors

One-To-Many Relationship: [msdyn_flow_awaitallactionapprovalmodel msdyn_flow_awaitallactionapprovalmodel_SyncErrors](msdyn_flow_awaitallactionapprovalmodel.md#BKMK_msdyn_flow_awaitallactionapprovalmodel_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_awaitallactionapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_awaitallactionapprovalmodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_awaitallactionapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_awaitallapprovalmodel_SyncErrors"></a> msdyn_flow_awaitallapprovalmodel_SyncErrors

One-To-Many Relationship: [msdyn_flow_awaitallapprovalmodel msdyn_flow_awaitallapprovalmodel_SyncErrors](msdyn_flow_awaitallapprovalmodel.md#BKMK_msdyn_flow_awaitallapprovalmodel_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_awaitallapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_awaitallapprovalmodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_awaitallapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_basicapprovalmodel_SyncErrors"></a> msdyn_flow_basicapprovalmodel_SyncErrors

One-To-Many Relationship: [msdyn_flow_basicapprovalmodel msdyn_flow_basicapprovalmodel_SyncErrors](msdyn_flow_basicapprovalmodel.md#BKMK_msdyn_flow_basicapprovalmodel_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_basicapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_basicapprovalmodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_basicapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_flowapproval_SyncErrors"></a> msdyn_flow_flowapproval_SyncErrors

One-To-Many Relationship: [msdyn_flow_flowapproval msdyn_flow_flowapproval_SyncErrors](msdyn_flow_flowapproval.md#BKMK_msdyn_flow_flowapproval_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_flowapproval`|
|ReferencedAttribute|`msdyn_flow_flowapprovalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_flowapproval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_formmapping_SyncErrors"></a> msdyn_formmapping_SyncErrors

One-To-Many Relationship: [msdyn_formmapping msdyn_formmapping_SyncErrors](msdyn_formmapping.md#BKMK_msdyn_formmapping_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_formmapping`|
|ReferencedAttribute|`msdyn_formmappingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_formmapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_function_SyncErrors"></a> msdyn_function_SyncErrors

One-To-Many Relationship: [msdyn_function msdyn_function_SyncErrors](msdyn_function.md#BKMK_msdyn_function_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_function`|
|ReferencedAttribute|`msdyn_functionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_function`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_helppage_SyncErrors"></a> msdyn_helppage_SyncErrors

One-To-Many Relationship: [msdyn_helppage msdyn_helppage_SyncErrors](msdyn_helppage.md#BKMK_msdyn_helppage_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_helppage`|
|ReferencedAttribute|`msdyn_helppageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_helppage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_historicalcaseharvestbatch_SyncErrors"></a> msdyn_historicalcaseharvestbatch_SyncErrors

One-To-Many Relationship: [msdyn_historicalcaseharvestbatch msdyn_historicalcaseharvestbatch_SyncErrors](msdyn_historicalcaseharvestbatch.md#BKMK_msdyn_historicalcaseharvestbatch_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_historicalcaseharvestbatch`|
|ReferencedAttribute|`msdyn_historicalcaseharvestbatchid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_historicalcaseharvestbatch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_historicalcaseharvestrun_SyncErrors"></a> msdyn_historicalcaseharvestrun_SyncErrors

One-To-Many Relationship: [msdyn_historicalcaseharvestrun msdyn_historicalcaseharvestrun_SyncErrors](msdyn_historicalcaseharvestrun.md#BKMK_msdyn_historicalcaseharvestrun_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_historicalcaseharvestrun`|
|ReferencedAttribute|`msdyn_historicalcaseharvestrunid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_historicalcaseharvestrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_insightsstorevirtualentity_SyncErrors"></a> msdyn_insightsstorevirtualentity_SyncErrors

One-To-Many Relationship: [msdyn_insightsstorevirtualentity msdyn_insightsstorevirtualentity_SyncErrors](msdyn_insightsstorevirtualentity.md#BKMK_msdyn_insightsstorevirtualentity_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_insightsstorevirtualentity`|
|ReferencedAttribute|`msdyn_insightsstorevirtualentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_insightsstorevirtualentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_integratedsearchprovider_SyncErrors"></a> msdyn_integratedsearchprovider_SyncErrors

One-To-Many Relationship: [msdyn_integratedsearchprovider msdyn_integratedsearchprovider_SyncErrors](msdyn_integratedsearchprovider.md#BKMK_msdyn_integratedsearchprovider_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_integratedsearchprovider`|
|ReferencedAttribute|`msdyn_integratedsearchproviderid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_integratedsearchprovider`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kalanguagesetting_SyncErrors"></a> msdyn_kalanguagesetting_SyncErrors

One-To-Many Relationship: [msdyn_kalanguagesetting msdyn_kalanguagesetting_SyncErrors](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kalanguagesetting`|
|ReferencedAttribute|`msdyn_kalanguagesettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_kalanguagesetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kbattachment_SyncErrors"></a> msdyn_kbattachment_SyncErrors

One-To-Many Relationship: [msdyn_kbattachment msdyn_kbattachment_SyncErrors](msdyn_kbattachment.md#BKMK_msdyn_kbattachment_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kbattachment`|
|ReferencedAttribute|`msdyn_kbattachmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_kbattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kmfederatedsearchconfig_SyncErrors"></a> msdyn_kmfederatedsearchconfig_SyncErrors

One-To-Many Relationship: [msdyn_kmfederatedsearchconfig msdyn_kmfederatedsearchconfig_SyncErrors](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kmfederatedsearchconfig`|
|ReferencedAttribute|`msdyn_kmfederatedsearchconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_kmfederatedsearchconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kmpersonalizationsetting_SyncErrors"></a> msdyn_kmpersonalizationsetting_SyncErrors

One-To-Many Relationship: [msdyn_kmpersonalizationsetting msdyn_kmpersonalizationsetting_SyncErrors](msdyn_kmpersonalizationsetting.md#BKMK_msdyn_kmpersonalizationsetting_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kmpersonalizationsetting`|
|ReferencedAttribute|`msdyn_kmpersonalizationsettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_kmpersonalizationsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgearticleimage_SyncErrors"></a> msdyn_knowledgearticleimage_SyncErrors

One-To-Many Relationship: [msdyn_knowledgearticleimage msdyn_knowledgearticleimage_SyncErrors](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgearticleimage`|
|ReferencedAttribute|`msdyn_knowledgearticleimageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgearticleimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgearticletemplate_SyncErrors"></a> msdyn_knowledgearticletemplate_SyncErrors

One-To-Many Relationship: [msdyn_knowledgearticletemplate msdyn_knowledgearticletemplate_SyncErrors](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgearticletemplate`|
|ReferencedAttribute|`msdyn_knowledgearticletemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgearticletemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeassetconfiguration_SyncErrors"></a> msdyn_knowledgeassetconfiguration_SyncErrors

One-To-Many Relationship: [msdyn_knowledgeassetconfiguration msdyn_knowledgeassetconfiguration_SyncErrors](msdyn_knowledgeassetconfiguration.md#BKMK_msdyn_knowledgeassetconfiguration_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeassetconfiguration`|
|ReferencedAttribute|`msdyn_knowledgeassetconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgeassetconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeconfiguration_SyncErrors"></a> msdyn_knowledgeconfiguration_SyncErrors

One-To-Many Relationship: [msdyn_knowledgeconfiguration msdyn_knowledgeconfiguration_SyncErrors](msdyn_knowledgeconfiguration.md#BKMK_msdyn_knowledgeconfiguration_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeconfiguration`|
|ReferencedAttribute|`msdyn_knowledgeconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeharvestjobrecord_SyncErrors"></a> msdyn_knowledgeharvestjobrecord_SyncErrors

One-To-Many Relationship: [msdyn_knowledgeharvestjobrecord msdyn_knowledgeharvestjobrecord_SyncErrors](msdyn_knowledgeharvestjobrecord.md#BKMK_msdyn_knowledgeharvestjobrecord_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeharvestjobrecord`|
|ReferencedAttribute|`msdyn_knowledgeharvestjobrecordid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgeharvestjobrecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeinteractioninsight_SyncErrors"></a> msdyn_knowledgeinteractioninsight_SyncErrors

One-To-Many Relationship: [msdyn_knowledgeinteractioninsight msdyn_knowledgeinteractioninsight_SyncErrors](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeinteractioninsight`|
|ReferencedAttribute|`msdyn_knowledgeinteractioninsightid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgeinteractioninsight`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgemanagementsetting_SyncErrors"></a> msdyn_knowledgemanagementsetting_SyncErrors

One-To-Many Relationship: [msdyn_knowledgemanagementsetting msdyn_knowledgemanagementsetting_SyncErrors](msdyn_knowledgemanagementsetting.md#BKMK_msdyn_knowledgemanagementsetting_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgemanagementsetting`|
|ReferencedAttribute|`msdyn_knowledgemanagementsettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgemanagementsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgepersonalfilter_SyncErrors"></a> msdyn_knowledgepersonalfilter_SyncErrors

One-To-Many Relationship: [msdyn_knowledgepersonalfilter msdyn_knowledgepersonalfilter_SyncErrors](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgepersonalfilter`|
|ReferencedAttribute|`msdyn_knowledgepersonalfilterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgepersonalfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgesearchfilter_SyncErrors"></a> msdyn_knowledgesearchfilter_SyncErrors

One-To-Many Relationship: [msdyn_knowledgesearchfilter msdyn_knowledgesearchfilter_SyncErrors](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgesearchfilter`|
|ReferencedAttribute|`msdyn_knowledgesearchfilterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgesearchfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgesearchinsight_SyncErrors"></a> msdyn_knowledgesearchinsight_SyncErrors

One-To-Many Relationship: [msdyn_knowledgesearchinsight msdyn_knowledgesearchinsight_SyncErrors](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgesearchinsight`|
|ReferencedAttribute|`msdyn_knowledgesearchinsightid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgesearchinsight`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_mobileapp_SyncErrors"></a> msdyn_mobileapp_SyncErrors

One-To-Many Relationship: [msdyn_mobileapp msdyn_mobileapp_SyncErrors](msdyn_mobileapp.md#BKMK_msdyn_mobileapp_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_mobileapp`|
|ReferencedAttribute|`msdyn_mobileappid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_mobileapp`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_modulerundetail_SyncErrors"></a> msdyn_modulerundetail_SyncErrors

One-To-Many Relationship: [msdyn_modulerundetail msdyn_modulerundetail_SyncErrors](msdyn_modulerundetail.md#BKMK_msdyn_modulerundetail_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_modulerundetail`|
|ReferencedAttribute|`msdyn_modulerundetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_modulerundetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmanalysishistory_SyncErrors"></a> msdyn_pmanalysishistory_SyncErrors

One-To-Many Relationship: [msdyn_pmanalysishistory msdyn_pmanalysishistory_SyncErrors](msdyn_pmanalysishistory.md#BKMK_msdyn_pmanalysishistory_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmanalysishistory`|
|ReferencedAttribute|`msdyn_pmanalysishistoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmanalysishistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmbusinessruleautomationconfig_SyncErrors"></a> msdyn_pmbusinessruleautomationconfig_SyncErrors

One-To-Many Relationship: [msdyn_pmbusinessruleautomationconfig msdyn_pmbusinessruleautomationconfig_SyncErrors](msdyn_pmbusinessruleautomationconfig.md#BKMK_msdyn_pmbusinessruleautomationconfig_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmbusinessruleautomationconfig`|
|ReferencedAttribute|`msdyn_pmbusinessruleautomationconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmbusinessruleautomationconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmcalendar_SyncErrors"></a> msdyn_pmcalendar_SyncErrors

One-To-Many Relationship: [msdyn_pmcalendar msdyn_pmcalendar_SyncErrors](msdyn_pmcalendar.md#BKMK_msdyn_pmcalendar_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmcalendar`|
|ReferencedAttribute|`msdyn_pmcalendarid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmcalendar`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmcalendarversion_SyncErrors"></a> msdyn_pmcalendarversion_SyncErrors

One-To-Many Relationship: [msdyn_pmcalendarversion msdyn_pmcalendarversion_SyncErrors](msdyn_pmcalendarversion.md#BKMK_msdyn_pmcalendarversion_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmcalendarversion`|
|ReferencedAttribute|`msdyn_pmcalendarversionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmcalendarversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pminferredtask_SyncErrors"></a> msdyn_pminferredtask_SyncErrors

One-To-Many Relationship: [msdyn_pminferredtask msdyn_pminferredtask_SyncErrors](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pminferredtask`|
|ReferencedAttribute|`msdyn_pminferredtaskid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pminferredtask`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessextendedmetadataversion_SyncErrors"></a> msdyn_pmprocessextendedmetadataversion_SyncErrors

One-To-Many Relationship: [msdyn_pmprocessextendedmetadataversion msdyn_pmprocessextendedmetadataversion_SyncErrors](msdyn_pmprocessextendedmetadataversion.md#BKMK_msdyn_pmprocessextendedmetadataversion_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessextendedmetadataversion`|
|ReferencedAttribute|`msdyn_pmprocessextendedmetadataversionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmprocessextendedmetadataversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocesstemplate_SyncErrors"></a> msdyn_pmprocesstemplate_SyncErrors

One-To-Many Relationship: [msdyn_pmprocesstemplate msdyn_pmprocesstemplate_SyncErrors](msdyn_pmprocesstemplate.md#BKMK_msdyn_pmprocesstemplate_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocesstemplate`|
|ReferencedAttribute|`msdyn_pmprocesstemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmprocesstemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessusersettings_SyncErrors"></a> msdyn_pmprocessusersettings_SyncErrors

One-To-Many Relationship: [msdyn_pmprocessusersettings msdyn_pmprocessusersettings_SyncErrors](msdyn_pmprocessusersettings.md#BKMK_msdyn_pmprocessusersettings_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessusersettings`|
|ReferencedAttribute|`msdyn_pmprocessusersettingsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmprocessusersettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessversion_SyncErrors"></a> msdyn_pmprocessversion_SyncErrors

One-To-Many Relationship: [msdyn_pmprocessversion msdyn_pmprocessversion_SyncErrors](msdyn_pmprocessversion.md#BKMK_msdyn_pmprocessversion_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessversion`|
|ReferencedAttribute|`msdyn_pmprocessversionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmprocessversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmrecording_SyncErrors"></a> msdyn_pmrecording_SyncErrors

One-To-Many Relationship: [msdyn_pmrecording msdyn_pmrecording_SyncErrors](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmrecording`|
|ReferencedAttribute|`msdyn_pmrecordingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmrecording`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmsimulation_SyncErrors"></a> msdyn_pmsimulation_SyncErrors

One-To-Many Relationship: [msdyn_pmsimulation msdyn_pmsimulation_SyncErrors](msdyn_pmsimulation.md#BKMK_msdyn_pmsimulation_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmsimulation`|
|ReferencedAttribute|`msdyn_pmsimulationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmsimulation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmtab_SyncErrors"></a> msdyn_pmtab_SyncErrors

One-To-Many Relationship: [msdyn_pmtab msdyn_pmtab_SyncErrors](msdyn_pmtab.md#BKMK_msdyn_pmtab_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmtab`|
|ReferencedAttribute|`msdyn_pmtabid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmtab`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmtemplate_SyncErrors"></a> msdyn_pmtemplate_SyncErrors

One-To-Many Relationship: [msdyn_pmtemplate msdyn_pmtemplate_SyncErrors](msdyn_pmtemplate.md#BKMK_msdyn_pmtemplate_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmtemplate`|
|ReferencedAttribute|`msdyn_pmtemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmtemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmview_SyncErrors"></a> msdyn_pmview_SyncErrors

One-To-Many Relationship: [msdyn_pmview msdyn_pmview_SyncErrors](msdyn_pmview.md#BKMK_msdyn_pmview_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmview`|
|ReferencedAttribute|`msdyn_pmviewid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmview`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_qna_SyncErrors"></a> msdyn_qna_SyncErrors

One-To-Many Relationship: [msdyn_qna msdyn_qna_SyncErrors](msdyn_qna.md#BKMK_msdyn_qna_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_qna`|
|ReferencedAttribute|`msdyn_qnaid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_qna`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_richtextfile_SyncErrors"></a> msdyn_richtextfile_SyncErrors

One-To-Many Relationship: [msdyn_richtextfile msdyn_richtextfile_SyncErrors](msdyn_richtextfile.md#BKMK_msdyn_richtextfile_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_richtextfile`|
|ReferencedAttribute|`msdyn_richtextfileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_richtextfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_salesforcestructuredobject_SyncErrors"></a> msdyn_salesforcestructuredobject_SyncErrors

One-To-Many Relationship: [msdyn_salesforcestructuredobject msdyn_salesforcestructuredobject_SyncErrors](msdyn_salesforcestructuredobject.md#BKMK_msdyn_salesforcestructuredobject_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_salesforcestructuredobject`|
|ReferencedAttribute|`msdyn_salesforcestructuredobjectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_salesforcestructuredobject`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_salesforcestructuredqnaconfig_SyncErrors"></a> msdyn_salesforcestructuredqnaconfig_SyncErrors

One-To-Many Relationship: [msdyn_salesforcestructuredqnaconfig msdyn_salesforcestructuredqnaconfig_SyncErrors](msdyn_salesforcestructuredqnaconfig.md#BKMK_msdyn_salesforcestructuredqnaconfig_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_salesforcestructuredqnaconfig`|
|ReferencedAttribute|`msdyn_salesforcestructuredqnaconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_salesforcestructuredqnaconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_schedule_SyncErrors"></a> msdyn_schedule_SyncErrors

One-To-Many Relationship: [msdyn_schedule msdyn_schedule_SyncErrors](msdyn_schedule.md#BKMK_msdyn_schedule_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_schedule`|
|ReferencedAttribute|`msdyn_scheduleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_schedule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_serviceconfiguration_SyncErrors"></a> msdyn_serviceconfiguration_SyncErrors

One-To-Many Relationship: [msdyn_serviceconfiguration msdyn_serviceconfiguration_SyncErrors](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_serviceconfiguration`|
|ReferencedAttribute|`msdyn_serviceconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_serviceconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_slakpi_SyncErrors"></a> msdyn_slakpi_SyncErrors

One-To-Many Relationship: [msdyn_slakpi msdyn_slakpi_SyncErrors](msdyn_slakpi.md#BKMK_msdyn_slakpi_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_slakpi`|
|ReferencedAttribute|`msdyn_slakpiid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_slakpi`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthrule_SyncErrors"></a> msdyn_solutionhealthrule_SyncErrors

One-To-Many Relationship: [msdyn_solutionhealthrule msdyn_solutionhealthrule_SyncErrors](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthrule`|
|ReferencedAttribute|`msdyn_solutionhealthruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_solutionhealthrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthruleargument_SyncErrors"></a> msdyn_solutionhealthruleargument_SyncErrors

One-To-Many Relationship: [msdyn_solutionhealthruleargument msdyn_solutionhealthruleargument_SyncErrors](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthruleargument`|
|ReferencedAttribute|`msdyn_solutionhealthruleargumentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_solutionhealthruleargument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthruleset_SyncErrors"></a> msdyn_solutionhealthruleset_SyncErrors

One-To-Many Relationship: [msdyn_solutionhealthruleset msdyn_solutionhealthruleset_SyncErrors](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthruleset`|
|ReferencedAttribute|`msdyn_solutionhealthrulesetid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_solutionhealthruleset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_tour_SyncErrors"></a> msdyn_tour_SyncErrors

One-To-Many Relationship: [msdyn_tour msdyn_tour_SyncErrors](msdyn_tour.md#BKMK_msdyn_tour_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_tour`|
|ReferencedAttribute|`msdyn_tourid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_tour`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_virtualtablecolumncandidate_SyncErrors"></a> msdyn_virtualtablecolumncandidate_SyncErrors

One-To-Many Relationship: [msdyn_virtualtablecolumncandidate msdyn_virtualtablecolumncandidate_SyncErrors](msdyn_virtualtablecolumncandidate.md#BKMK_msdyn_virtualtablecolumncandidate_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_virtualtablecolumncandidate`|
|ReferencedAttribute|`msdyn_virtualtablecolumncandidateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_virtualtablecolumncandidate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_workflowactionstatus_SyncErrors"></a> msdyn_workflowactionstatus_SyncErrors

One-To-Many Relationship: [msdyn_workflowactionstatus msdyn_workflowactionstatus_SyncErrors](msdyn_workflowactionstatus.md#BKMK_msdyn_workflowactionstatus_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_workflowactionstatus`|
|ReferencedAttribute|`msdyn_workflowactionstatusid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_workflowactionstatus`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdynce_botcontent_SyncErrors"></a> msdynce_botcontent_SyncErrors

One-To-Many Relationship: [msdynce_botcontent msdynce_botcontent_SyncErrors](msdynce_botcontent.md#BKMK_msdynce_botcontent_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msdynce_botcontent`|
|ReferencedAttribute|`msdynce_botcontentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdynce_botcontent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msgraphresourcetosubscription_SyncErrors"></a> msgraphresourcetosubscription_SyncErrors

One-To-Many Relationship: [msgraphresourcetosubscription msgraphresourcetosubscription_SyncErrors](msgraphresourcetosubscription.md#BKMK_msgraphresourcetosubscription_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`msgraphresourcetosubscription`|
|ReferencedAttribute|`msgraphresourcetosubscriptionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msgraphresourcetosubscription`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspcat_catalogsubmissionfiles_SyncErrors"></a> mspcat_catalogsubmissionfiles_SyncErrors

One-To-Many Relationship: [mspcat_catalogsubmissionfiles mspcat_catalogsubmissionfiles_SyncErrors](mspcat_catalogsubmissionfiles.md#BKMK_mspcat_catalogsubmissionfiles_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`mspcat_catalogsubmissionfiles`|
|ReferencedAttribute|`mspcat_catalogsubmissionfilesid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspcat_catalogsubmissionfiles`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspcat_packagestore_SyncErrors"></a> mspcat_packagestore_SyncErrors

One-To-Many Relationship: [mspcat_packagestore mspcat_packagestore_SyncErrors](mspcat_packagestore.md#BKMK_mspcat_packagestore_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`mspcat_packagestore`|
|ReferencedAttribute|`mspcat_packagestoreid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspcat_packagestore`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_NewProcess_SyncErrors"></a> NewProcess_SyncErrors

One-To-Many Relationship: [newprocess NewProcess_SyncErrors](newprocess.md#BKMK_NewProcess_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`newprocess`|
|ReferencedAttribute|`businessprocessflowinstanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_NewProcess_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_Organization_SyncErrors"></a> Organization_SyncErrors

One-To-Many Relationship: [organization Organization_SyncErrors](organization.md#BKMK_Organization_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organization_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `NoCascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_organizationdatasyncfnostate_SyncErrors"></a> organizationdatasyncfnostate_SyncErrors

One-To-Many Relationship: [organizationdatasyncfnostate organizationdatasyncfnostate_SyncErrors](organizationdatasyncfnostate.md#BKMK_organizationdatasyncfnostate_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncfnostate`|
|ReferencedAttribute|`organizationdatasyncfnostateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncfnostate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncstate_SyncErrors"></a> organizationdatasyncstate_SyncErrors

One-To-Many Relationship: [organizationdatasyncstate organizationdatasyncstate_SyncErrors](organizationdatasyncstate.md#BKMK_organizationdatasyncstate_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncstate`|
|ReferencedAttribute|`organizationdatasyncstateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncstate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscription_SyncErrors"></a> organizationdatasyncsubscription_SyncErrors

One-To-Many Relationship: [organizationdatasyncsubscription organizationdatasyncsubscription_SyncErrors](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscription`|
|ReferencedAttribute|`organizationdatasyncsubscriptionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncsubscription`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscriptionentity_SyncErrors"></a> organizationdatasyncsubscriptionentity_SyncErrors

One-To-Many Relationship: [organizationdatasyncsubscriptionentity organizationdatasyncsubscriptionentity_SyncErrors](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscriptionentity`|
|ReferencedAttribute|`organizationdatasyncsubscriptionentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncsubscriptionentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_SyncErrors"></a> organizationdatasyncsubscriptionfnotable_SyncErrors

One-To-Many Relationship: [organizationdatasyncsubscriptionfnotable organizationdatasyncsubscriptionfnotable_SyncErrors](organizationdatasyncsubscriptionfnotable.md#BKMK_organizationdatasyncsubscriptionfnotable_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscriptionfnotable`|
|ReferencedAttribute|`organizationdatasyncsubscriptionfnotableid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncsubscriptionfnotable`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_SyncError"></a> owner_SyncError

One-To-Many Relationship: [owner owner_SyncError](owner.md#BKMK_owner_SyncError)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_package_SyncErrors"></a> package_SyncErrors

One-To-Many Relationship: [package package_SyncErrors](package.md#BKMK_package_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`package`|
|ReferencedAttribute|`packageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_package`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_packagehistory_SyncErrors"></a> packagehistory_SyncErrors

One-To-Many Relationship: [packagehistory packagehistory_SyncErrors](packagehistory.md#BKMK_packagehistory_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`packagehistory`|
|ReferencedAttribute|`packagehistoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_packagehistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_PhoneCall_SyncErrors"></a> PhoneCall_SyncErrors

One-To-Many Relationship: [phonecall PhoneCall_SyncErrors](phonecall.md#BKMK_PhoneCall_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`phonecall`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_phonecall_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_plannerbusinessscenario_SyncErrors"></a> plannerbusinessscenario_SyncErrors

One-To-Many Relationship: [plannerbusinessscenario plannerbusinessscenario_SyncErrors](plannerbusinessscenario.md#BKMK_plannerbusinessscenario_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`plannerbusinessscenario`|
|ReferencedAttribute|`plannerbusinessscenarioid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_plannerbusinessscenario`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plannersyncaction_SyncErrors"></a> plannersyncaction_SyncErrors

One-To-Many Relationship: [plannersyncaction plannersyncaction_SyncErrors](plannersyncaction.md#BKMK_plannersyncaction_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`plannersyncaction`|
|ReferencedAttribute|`plannersyncactionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_plannersyncaction`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plugin_SyncErrors"></a> plugin_SyncErrors

One-To-Many Relationship: [plugin plugin_SyncErrors](plugin.md#BKMK_plugin_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`plugin`|
|ReferencedAttribute|`pluginid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_plugin`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_pluginpackage_SyncErrors"></a> pluginpackage_SyncErrors

One-To-Many Relationship: [pluginpackage pluginpackage_SyncErrors](pluginpackage.md#BKMK_pluginpackage_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`pluginpackage`|
|ReferencedAttribute|`pluginpackageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_pluginpackage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Position_SyncErrors"></a> Position_SyncErrors

One-To-Many Relationship: [position Position_SyncErrors](position.md#BKMK_Position_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`position`|
|ReferencedAttribute|`positionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_position_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_PostFollow_SyncErrors"></a> PostFollow_SyncErrors

One-To-Many Relationship: [postfollow PostFollow_SyncErrors](postfollow.md#BKMK_PostFollow_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`postfollow`|
|ReferencedAttribute|`postfollowid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_postfollow_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_powerbidataset_SyncErrors"></a> powerbidataset_SyncErrors

One-To-Many Relationship: [powerbidataset powerbidataset_SyncErrors](powerbidataset.md#BKMK_powerbidataset_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbidataset`|
|ReferencedAttribute|`powerbidatasetid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbidataset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbidatasetapdx_SyncErrors"></a> powerbidatasetapdx_SyncErrors

One-To-Many Relationship: [powerbidatasetapdx powerbidatasetapdx_SyncErrors](powerbidatasetapdx.md#BKMK_powerbidatasetapdx_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbidatasetapdx`|
|ReferencedAttribute|`powerbidatasetapdxid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbidatasetapdx`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbimashupparameter_SyncErrors"></a> powerbimashupparameter_SyncErrors

One-To-Many Relationship: [powerbimashupparameter powerbimashupparameter_SyncErrors](powerbimashupparameter.md#BKMK_powerbimashupparameter_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbimashupparameter`|
|ReferencedAttribute|`powerbimashupparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbimashupparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbireport_SyncErrors"></a> powerbireport_SyncErrors

One-To-Many Relationship: [powerbireport powerbireport_SyncErrors](powerbireport.md#BKMK_powerbireport_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbireport`|
|ReferencedAttribute|`powerbireportid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbireport`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbireportapdx_SyncErrors"></a> powerbireportapdx_SyncErrors

One-To-Many Relationship: [powerbireportapdx powerbireportapdx_SyncErrors](powerbireportapdx.md#BKMK_powerbireportapdx_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbireportapdx`|
|ReferencedAttribute|`powerbireportapdxid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbireportapdx`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerfxrule_SyncErrors"></a> powerfxrule_SyncErrors

One-To-Many Relationship: [powerfxrule powerfxrule_SyncErrors](powerfxrule.md#BKMK_powerfxrule_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`powerfxrule`|
|ReferencedAttribute|`powerfxruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerfxrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagecomponent_SyncErrors"></a> powerpagecomponent_SyncErrors

One-To-Many Relationship: [powerpagecomponent powerpagecomponent_SyncErrors](powerpagecomponent.md#BKMK_powerpagecomponent_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagecomponent`|
|ReferencedAttribute|`powerpagecomponentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagecomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesddosalert_SyncErrors"></a> powerpagesddosalert_SyncErrors

One-To-Many Relationship: [powerpagesddosalert powerpagesddosalert_SyncErrors](powerpagesddosalert.md#BKMK_powerpagesddosalert_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesddosalert`|
|ReferencedAttribute|`powerpagesddosalertid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesddosalert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesite_SyncErrors"></a> powerpagesite_SyncErrors

One-To-Many Relationship: [powerpagesite powerpagesite_SyncErrors](powerpagesite.md#BKMK_powerpagesite_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesite`|
|ReferencedAttribute|`powerpagesiteid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesite`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesitelanguage_SyncErrors"></a> powerpagesitelanguage_SyncErrors

One-To-Many Relationship: [powerpagesitelanguage powerpagesitelanguage_SyncErrors](powerpagesitelanguage.md#BKMK_powerpagesitelanguage_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesitelanguage`|
|ReferencedAttribute|`powerpagesitelanguageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesitelanguage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesitepublished_SyncErrors"></a> powerpagesitepublished_SyncErrors

One-To-Many Relationship: [powerpagesitepublished powerpagesitepublished_SyncErrors](powerpagesitepublished.md#BKMK_powerpagesitepublished_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesitepublished`|
|ReferencedAttribute|`powerpagesitepublishedid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesitepublished`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesmanagedidentity_SyncErrors"></a> powerpagesmanagedidentity_SyncErrors

One-To-Many Relationship: [powerpagesmanagedidentity powerpagesmanagedidentity_SyncErrors](powerpagesmanagedidentity.md#BKMK_powerpagesmanagedidentity_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesmanagedidentity`|
|ReferencedAttribute|`powerpagesmanagedidentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesmanagedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesscanreport_SyncErrors"></a> powerpagesscanreport_SyncErrors

One-To-Many Relationship: [powerpagesscanreport powerpagesscanreport_SyncErrors](powerpagesscanreport.md#BKMK_powerpagesscanreport_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesscanreport`|
|ReferencedAttribute|`powerpagesscanreportid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesscanreport`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagessourcefile_SyncErrors"></a> powerpagessourcefile_SyncErrors

One-To-Many Relationship: [powerpagessourcefile powerpagessourcefile_SyncErrors](powerpagessourcefile.md#BKMK_powerpagessourcefile_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagessourcefile`|
|ReferencedAttribute|`powerpagessourcefileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagessourcefile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegecheckerlog_SyncErrors"></a> privilegecheckerlog_SyncErrors

One-To-Many Relationship: [privilegecheckerlog privilegecheckerlog_SyncErrors](privilegecheckerlog.md#BKMK_privilegecheckerlog_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegecheckerlog`|
|ReferencedAttribute|`privilegecheckerlogid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_privilegecheckerlog`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegecheckerrun_SyncErrors"></a> privilegecheckerrun_SyncErrors

One-To-Many Relationship: [privilegecheckerrun privilegecheckerrun_SyncErrors](privilegecheckerrun.md#BKMK_privilegecheckerrun_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegecheckerrun`|
|ReferencedAttribute|`privilegecheckerrunid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_privilegecheckerrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegesremovalsetting_SyncErrors"></a> privilegesremovalsetting_SyncErrors

One-To-Many Relationship: [privilegesremovalsetting privilegesremovalsetting_SyncErrors](privilegesremovalsetting.md#BKMK_privilegesremovalsetting_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegesremovalsetting`|
|ReferencedAttribute|`privilegesremovalsettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_privilegesremovalsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ProcessSession_SyncErrors"></a> ProcessSession_SyncErrors

One-To-Many Relationship: [processsession ProcessSession_SyncErrors](processsession.md#BKMK_ProcessSession_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`processsession`|
|ReferencedAttribute|`processsessionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_processsession_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_ProcessStage_SyncErrors"></a> ProcessStage_SyncErrors

One-To-Many Relationship: [processstage ProcessStage_SyncErrors](processstage.md#BKMK_ProcessStage_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`processstage`|
|ReferencedAttribute|`processstageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_processstage_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_processstageparameter_SyncErrors"></a> processstageparameter_SyncErrors

One-To-Many Relationship: [processstageparameter processstageparameter_SyncErrors](processstageparameter.md#BKMK_processstageparameter_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`processstageparameter`|
|ReferencedAttribute|`processstageparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_processstageparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ProcessTrigger_SyncErrors"></a> ProcessTrigger_SyncErrors

One-To-Many Relationship: [processtrigger ProcessTrigger_SyncErrors](processtrigger.md#BKMK_ProcessTrigger_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`processtrigger`|
|ReferencedAttribute|`processtriggerid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_processtrigger_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_provisionlanguageforuser_SyncErrors"></a> provisionlanguageforuser_SyncErrors

One-To-Many Relationship: [provisionlanguageforuser provisionlanguageforuser_SyncErrors](provisionlanguageforuser.md#BKMK_provisionlanguageforuser_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`provisionlanguageforuser`|
|ReferencedAttribute|`provisionlanguageforuserid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_provisionlanguageforuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Publisher_SyncErrors"></a> Publisher_SyncErrors

One-To-Many Relationship: [publisher Publisher_SyncErrors](publisher.md#BKMK_Publisher_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`publisher`|
|ReferencedAttribute|`publisherid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_publisher_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_purviewlabelinfo_SyncErrors"></a> purviewlabelinfo_SyncErrors

One-To-Many Relationship: [purviewlabelinfo purviewlabelinfo_SyncErrors](purviewlabelinfo.md#BKMK_purviewlabelinfo_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`purviewlabelinfo`|
|ReferencedAttribute|`purviewlabelinfoid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_purviewlabelinfo`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Queue_SyncErrors"></a> Queue_SyncErrors

One-To-Many Relationship: [queue Queue_SyncErrors](queue.md#BKMK_Queue_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`queue`|
|ReferencedAttribute|`queueid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_queue_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_QueueItem_SyncErrors"></a> QueueItem_SyncErrors

One-To-Many Relationship: [queueitem QueueItem_SyncErrors](queueitem.md#BKMK_QueueItem_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`queueitem`|
|ReferencedAttribute|`queueitemid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_queueitem_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_recordfilter_SyncErrors"></a> recordfilter_SyncErrors

One-To-Many Relationship: [recordfilter recordfilter_SyncErrors](recordfilter.md#BKMK_recordfilter_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`recordfilter`|
|ReferencedAttribute|`recordfilterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_recordfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_RecurringAppointmentMaster_SyncErrors"></a> RecurringAppointmentMaster_SyncErrors

One-To-Many Relationship: [recurringappointmentmaster RecurringAppointmentMaster_SyncErrors](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`recurringappointmentmaster`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_recurringappointmentmaster_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_recyclebinconfig_SyncErrors"></a> recyclebinconfig_SyncErrors

One-To-Many Relationship: [recyclebinconfig recyclebinconfig_SyncErrors](recyclebinconfig.md#BKMK_recyclebinconfig_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`recyclebinconfig`|
|ReferencedAttribute|`recyclebinconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_recyclebinconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_relationshipattribute_SyncErrors"></a> relationshipattribute_SyncErrors

One-To-Many Relationship: [relationshipattribute relationshipattribute_SyncErrors](relationshipattribute.md#BKMK_relationshipattribute_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`relationshipattribute`|
|ReferencedAttribute|`relationshipattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_relationshipattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Report_SyncErrors"></a> Report_SyncErrors

One-To-Many Relationship: [report Report_SyncErrors](report.md#BKMK_Report_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`report`|
|ReferencedAttribute|`reportid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_report_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_ReportCategory_SyncErrors"></a> ReportCategory_SyncErrors

One-To-Many Relationship: [reportcategory ReportCategory_SyncErrors](reportcategory.md#BKMK_ReportCategory_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`reportcategory`|
|ReferencedAttribute|`reportcategoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_reportcategory_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_reportparameter_SyncErrors"></a> reportparameter_SyncErrors

One-To-Many Relationship: [reportparameter reportparameter_SyncErrors](reportparameter.md#BKMK_reportparameter_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`reportparameter`|
|ReferencedAttribute|`reportparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_reportparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retaineddataexcel_SyncErrors"></a> retaineddataexcel_SyncErrors

One-To-Many Relationship: [retaineddataexcel retaineddataexcel_SyncErrors](retaineddataexcel.md#BKMK_retaineddataexcel_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`retaineddataexcel`|
|ReferencedAttribute|`retaineddataexcelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retaineddataexcel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionconfig_SyncErrors"></a> retentionconfig_SyncErrors

One-To-Many Relationship: [retentionconfig retentionconfig_SyncErrors](retentionconfig.md#BKMK_retentionconfig_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionconfig`|
|ReferencedAttribute|`retentionconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionfailuredetail_SyncErrors"></a> retentionfailuredetail_SyncErrors

One-To-Many Relationship: [retentionfailuredetail retentionfailuredetail_SyncErrors](retentionfailuredetail.md#BKMK_retentionfailuredetail_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionfailuredetail`|
|ReferencedAttribute|`retentionfailuredetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionfailuredetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionoperation_SyncErrors"></a> retentionoperation_SyncErrors

One-To-Many Relationship: [retentionoperation retentionoperation_SyncErrors](retentionoperation.md#BKMK_retentionoperation_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionoperation`|
|ReferencedAttribute|`retentionoperationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionoperationdetail_SyncErrors"></a> retentionoperationdetail_SyncErrors

One-To-Many Relationship: [retentionoperationdetail retentionoperationdetail_SyncErrors](retentionoperationdetail.md#BKMK_retentionoperationdetail_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionoperationdetail`|
|ReferencedAttribute|`retentionoperationdetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionoperationdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionsuccessdetail_SyncErrors"></a> retentionsuccessdetail_SyncErrors

One-To-Many Relationship: [retentionsuccessdetail retentionsuccessdetail_SyncErrors](retentionsuccessdetail.md#BKMK_retentionsuccessdetail_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionsuccessdetail`|
|ReferencedAttribute|`retentionsuccessdetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionsuccessdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Role_SyncErrors"></a> Role_SyncErrors

One-To-Many Relationship: [role Role_SyncErrors](role.md#BKMK_Role_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`role`|
|ReferencedAttribute|`roleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_role_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_roleeditorlayout_SyncErrors"></a> roleeditorlayout_SyncErrors

One-To-Many Relationship: [roleeditorlayout roleeditorlayout_SyncErrors](roleeditorlayout.md#BKMK_roleeditorlayout_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`roleeditorlayout`|
|ReferencedAttribute|`roleeditorlayoutid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_roleeditorlayout`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_RollupField_SyncErrors"></a> RollupField_SyncErrors

One-To-Many Relationship: [rollupfield RollupField_SyncErrors](rollupfield.md#BKMK_RollupField_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`rollupfield`|
|ReferencedAttribute|`rollupfieldid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_rollupfield_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_sa_suggestedaction_SyncErrors"></a> sa_suggestedaction_SyncErrors

One-To-Many Relationship: [sa_suggestedaction sa_suggestedaction_SyncErrors](sa_suggestedaction.md#BKMK_sa_suggestedaction_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`sa_suggestedaction`|
|ReferencedAttribute|`sa_suggestedactionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sa_suggestedaction`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sa_suggestedactioncriteria_SyncErrors"></a> sa_suggestedactioncriteria_SyncErrors

One-To-Many Relationship: [sa_suggestedactioncriteria sa_suggestedactioncriteria_SyncErrors](sa_suggestedactioncriteria.md#BKMK_sa_suggestedactioncriteria_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`sa_suggestedactioncriteria`|
|ReferencedAttribute|`sa_suggestedactioncriteriaid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sa_suggestedactioncriteria`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SavedQuery_SyncErrors"></a> SavedQuery_SyncErrors

One-To-Many Relationship: [savedquery SavedQuery_SyncErrors](savedquery.md#BKMK_SavedQuery_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`savedquery`|
|ReferencedAttribute|`savedqueryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_savedquery_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_SavedQueryVisualization_SyncErrors"></a> SavedQueryVisualization_SyncErrors

One-To-Many Relationship: [savedqueryvisualization SavedQueryVisualization_SyncErrors](savedqueryvisualization.md#BKMK_SavedQueryVisualization_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`savedqueryvisualization`|
|ReferencedAttribute|`savedqueryvisualizationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_savedqueryvisualization_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_savingrule_SyncErrors"></a> savingrule_SyncErrors

One-To-Many Relationship: [savingrule savingrule_SyncErrors](savingrule.md#BKMK_savingrule_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`savingrule`|
|ReferencedAttribute|`savingruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_savingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchattributesettings_SyncErrors"></a> searchattributesettings_SyncErrors

One-To-Many Relationship: [searchattributesettings searchattributesettings_SyncErrors](searchattributesettings.md#BKMK_searchattributesettings_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`searchattributesettings`|
|ReferencedAttribute|`searchattributesettingsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_searchattributesettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchcustomanalyzer_SyncErrors"></a> searchcustomanalyzer_SyncErrors

One-To-Many Relationship: [searchcustomanalyzer searchcustomanalyzer_SyncErrors](searchcustomanalyzer.md#BKMK_searchcustomanalyzer_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`searchcustomanalyzer`|
|ReferencedAttribute|`searchcustomanalyzerid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_searchcustomanalyzer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchrelationshipsettings_SyncErrors"></a> searchrelationshipsettings_SyncErrors

One-To-Many Relationship: [searchrelationshipsettings searchrelationshipsettings_SyncErrors](searchrelationshipsettings.md#BKMK_searchrelationshipsettings_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`searchrelationshipsettings`|
|ReferencedAttribute|`searchrelationshipsettingsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_searchrelationshipsettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sensitivitylabelattributemapping_SyncErrors"></a> sensitivitylabelattributemapping_SyncErrors

One-To-Many Relationship: [sensitivitylabelattributemapping sensitivitylabelattributemapping_SyncErrors](sensitivitylabelattributemapping.md#BKMK_sensitivitylabelattributemapping_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`sensitivitylabelattributemapping`|
|ReferencedAttribute|`sensitivitylabelattributemappingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sensitivitylabelattributemapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_serviceplan_SyncErrors"></a> serviceplan_SyncErrors

One-To-Many Relationship: [serviceplan serviceplan_SyncErrors](serviceplan.md#BKMK_serviceplan_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`serviceplan`|
|ReferencedAttribute|`serviceplanid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_serviceplan`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_serviceplanmapping_SyncErrors"></a> serviceplanmapping_SyncErrors

One-To-Many Relationship: [serviceplanmapping serviceplanmapping_SyncErrors](serviceplanmapping.md#BKMK_serviceplanmapping_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`serviceplanmapping`|
|ReferencedAttribute|`serviceplanmappingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_serviceplanmapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedlinksetting_SyncErrors"></a> sharedlinksetting_SyncErrors

One-To-Many Relationship: [sharedlinksetting sharedlinksetting_SyncErrors](sharedlinksetting.md#BKMK_sharedlinksetting_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedlinksetting`|
|ReferencedAttribute|`sharedlinksettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharedlinksetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedobject_SyncErrors"></a> sharedobject_SyncErrors

One-To-Many Relationship: [sharedobject sharedobject_SyncErrors](sharedobject.md#BKMK_sharedobject_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedobject`|
|ReferencedAttribute|`sharedobjectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharedobject`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedworkspace_SyncErrors"></a> sharedworkspace_SyncErrors

One-To-Many Relationship: [sharedworkspace sharedworkspace_SyncErrors](sharedworkspace.md#BKMK_sharedworkspace_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedworkspace`|
|ReferencedAttribute|`sharedworkspaceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharedworkspace`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedworkspacepool_SyncErrors"></a> sharedworkspacepool_SyncErrors

One-To-Many Relationship: [sharedworkspacepool sharedworkspacepool_SyncErrors](sharedworkspacepool.md#BKMK_sharedworkspacepool_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedworkspacepool`|
|ReferencedAttribute|`sharedworkspacepoolid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharedworkspacepool`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SharePointDocumentLocation_SyncErrors"></a> SharePointDocumentLocation_SyncErrors

One-To-Many Relationship: [sharepointdocumentlocation SharePointDocumentLocation_SyncErrors](sharepointdocumentlocation.md#BKMK_SharePointDocumentLocation_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`sharepointdocumentlocation`|
|ReferencedAttribute|`sharepointdocumentlocationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharepointdocumentlocation_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_sharepointmanagedidentity_SyncErrors"></a> sharepointmanagedidentity_SyncErrors

One-To-Many Relationship: [sharepointmanagedidentity sharepointmanagedidentity_SyncErrors](sharepointmanagedidentity.md#BKMK_sharepointmanagedidentity_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`sharepointmanagedidentity`|
|ReferencedAttribute|`sharepointmanagedidentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharepointmanagedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SharePointSite_SyncErrors"></a> SharePointSite_SyncErrors

One-To-Many Relationship: [sharepointsite SharePointSite_SyncErrors](sharepointsite.md#BKMK_SharePointSite_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`sharepointsite`|
|ReferencedAttribute|`sharepointsiteid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharepointsite_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_sideloadedaiplugin_SyncErrors"></a> sideloadedaiplugin_SyncErrors

One-To-Many Relationship: [sideloadedaiplugin sideloadedaiplugin_SyncErrors](sideloadedaiplugin.md#BKMK_sideloadedaiplugin_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`sideloadedaiplugin`|
|ReferencedAttribute|`sideloadedaipluginid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sideloadedaiplugin`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SLA_SyncErrors"></a> SLA_SyncErrors

One-To-Many Relationship: [sla SLA_SyncErrors](sla.md#BKMK_SLA_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`sla`|
|ReferencedAttribute|`slaid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sla_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_SLAItem_SyncErrors"></a> SLAItem_SyncErrors

One-To-Many Relationship: [slaitem SLAItem_SyncErrors](slaitem.md#BKMK_SLAItem_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`slaitem`|
|ReferencedAttribute|`slaitemid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_slaitem_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_SLAKPIInstance_SyncErrors"></a> SLAKPIInstance_SyncErrors

One-To-Many Relationship: [slakpiinstance SLAKPIInstance_SyncErrors](slakpiinstance.md#BKMK_SLAKPIInstance_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`slakpiinstance`|
|ReferencedAttribute|`slakpiinstanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_slakpiinstance_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_SocialActivity_SyncErrors"></a> SocialActivity_SyncErrors

One-To-Many Relationship: [socialactivity SocialActivity_SyncErrors](socialactivity.md#BKMK_SocialActivity_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`socialactivity`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_socialactivity_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_SocialProfile_SyncErrors"></a> SocialProfile_SyncErrors

One-To-Many Relationship: [socialprofile SocialProfile_SyncErrors](socialprofile.md#BKMK_SocialProfile_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`socialprofile`|
|ReferencedAttribute|`socialprofileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_socialprofile_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_Solution_SyncErrors"></a> Solution_SyncErrors

One-To-Many Relationship: [solution Solution_SyncErrors](solution.md#BKMK_Solution_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`solution`|
|ReferencedAttribute|`solutionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_solution_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_solutioncomponentattributeconfiguration_SyncErrors"></a> solutioncomponentattributeconfiguration_SyncErrors

One-To-Many Relationship: [solutioncomponentattributeconfiguration solutioncomponentattributeconfiguration_SyncErrors](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentattributeconfiguration`|
|ReferencedAttribute|`solutioncomponentattributeconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_solutioncomponentattributeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentbatchconfiguration_SyncErrors"></a> solutioncomponentbatchconfiguration_SyncErrors

One-To-Many Relationship: [solutioncomponentbatchconfiguration solutioncomponentbatchconfiguration_SyncErrors](solutioncomponentbatchconfiguration.md#BKMK_solutioncomponentbatchconfiguration_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentbatchconfiguration`|
|ReferencedAttribute|`solutioncomponentbatchconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_solutioncomponentbatchconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentconfiguration_SyncErrors"></a> solutioncomponentconfiguration_SyncErrors

One-To-Many Relationship: [solutioncomponentconfiguration solutioncomponentconfiguration_SyncErrors](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentconfiguration`|
|ReferencedAttribute|`solutioncomponentconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_solutioncomponentconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentrelationshipconfiguration_SyncErrors"></a> solutioncomponentrelationshipconfiguration_SyncErrors

One-To-Many Relationship: [solutioncomponentrelationshipconfiguration solutioncomponentrelationshipconfiguration_SyncErrors](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentrelationshipconfiguration`|
|ReferencedAttribute|`solutioncomponentrelationshipconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_solutioncomponentrelationshipconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagedentity_SyncErrors"></a> stagedentity_SyncErrors

One-To-Many Relationship: [stagedentity stagedentity_SyncErrors](stagedentity.md#BKMK_stagedentity_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`stagedentity`|
|ReferencedAttribute|`stagedentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_stagedentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagedentityattribute_SyncErrors"></a> stagedentityattribute_SyncErrors

One-To-Many Relationship: [stagedentityattribute stagedentityattribute_SyncErrors](stagedentityattribute.md#BKMK_stagedentityattribute_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`stagedentityattribute`|
|ReferencedAttribute|`stagedentityattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_stagedentityattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagedmetadataasyncoperation_SyncErrors"></a> stagedmetadataasyncoperation_SyncErrors

One-To-Many Relationship: [stagedmetadataasyncoperation stagedmetadataasyncoperation_SyncErrors](stagedmetadataasyncoperation.md#BKMK_stagedmetadataasyncoperation_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`stagedmetadataasyncoperation`|
|ReferencedAttribute|`stagedmetadataasyncoperationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_stagedmetadataasyncoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagesolutionupload_SyncErrors"></a> stagesolutionupload_SyncErrors

One-To-Many Relationship: [stagesolutionupload stagesolutionupload_SyncErrors](stagesolutionupload.md#BKMK_stagesolutionupload_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`stagesolutionupload`|
|ReferencedAttribute|`stagesolutionuploadid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_stagesolutionupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Subject_SyncErrors"></a> Subject_SyncErrors

One-To-Many Relationship: [subject Subject_SyncErrors](subject.md#BKMK_Subject_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`subject`|
|ReferencedAttribute|`subjectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_subject_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_supportusertable_SyncErrors"></a> supportusertable_SyncErrors

One-To-Many Relationship: [supportusertable supportusertable_SyncErrors](supportusertable.md#BKMK_supportusertable_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`supportusertable`|
|ReferencedAttribute|`supportusertableid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_supportusertable`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapsedatabase_SyncErrors"></a> synapsedatabase_SyncErrors

One-To-Many Relationship: [synapsedatabase synapsedatabase_SyncErrors](synapsedatabase.md#BKMK_synapsedatabase_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`synapsedatabase`|
|ReferencedAttribute|`synapsedatabaseid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapsedatabase`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkexternaltablestate_SyncErrors"></a> synapselinkexternaltablestate_SyncErrors

One-To-Many Relationship: [synapselinkexternaltablestate synapselinkexternaltablestate_SyncErrors](synapselinkexternaltablestate.md#BKMK_synapselinkexternaltablestate_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkexternaltablestate`|
|ReferencedAttribute|`synapselinkexternaltablestateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkexternaltablestate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofile_SyncErrors"></a> synapselinkprofile_SyncErrors

One-To-Many Relationship: [synapselinkprofile synapselinkprofile_SyncErrors](synapselinkprofile.md#BKMK_synapselinkprofile_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofile`|
|ReferencedAttribute|`synapselinkprofileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofileentity_SyncErrors"></a> synapselinkprofileentity_SyncErrors

One-To-Many Relationship: [synapselinkprofileentity synapselinkprofileentity_SyncErrors](synapselinkprofileentity.md#BKMK_synapselinkprofileentity_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofileentity`|
|ReferencedAttribute|`synapselinkprofileentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkprofileentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofileentitystate_SyncErrors"></a> synapselinkprofileentitystate_SyncErrors

One-To-Many Relationship: [synapselinkprofileentitystate synapselinkprofileentitystate_SyncErrors](synapselinkprofileentitystate.md#BKMK_synapselinkprofileentitystate_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofileentitystate`|
|ReferencedAttribute|`synapselinkprofileentitystateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkprofileentitystate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkschedule_SyncErrors"></a> synapselinkschedule_SyncErrors

One-To-Many Relationship: [synapselinkschedule synapselinkschedule_SyncErrors](synapselinkschedule.md#BKMK_synapselinkschedule_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkschedule`|
|ReferencedAttribute|`synapselinkscheduleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkschedule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SyncError_SyncErrors-many-to-one"></a> SyncError_SyncErrors

One-To-Many Relationship: [syncerror SyncError_SyncErrors](#BKMK_SyncError_SyncErrors-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`syncerror`|
|ReferencedAttribute|`syncerrorid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_syncerror_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_SystemUser_SyncError"></a> SystemUser_SyncError

One-To-Many Relationship: [systemuser SystemUser_SyncError](systemuser.md#BKMK_SystemUser_SyncError)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_systemuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SystemUser_SyncErrors"></a> SystemUser_SyncErrors

One-To-Many Relationship: [systemuser SystemUser_SyncErrors](systemuser.md#BKMK_SystemUser_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_systemuser_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_systemuserauthorizationchangetracker_SyncErrors"></a> systemuserauthorizationchangetracker_SyncErrors

One-To-Many Relationship: [systemuserauthorizationchangetracker systemuserauthorizationchangetracker_SyncErrors](systemuserauthorizationchangetracker.md#BKMK_systemuserauthorizationchangetracker_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuserauthorizationchangetracker`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_systemuserauthorizationchangetracker`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_tag_SyncErrors"></a> tag_SyncErrors

One-To-Many Relationship: [tag tag_SyncErrors](tag.md#BKMK_tag_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`tag`|
|ReferencedAttribute|`tagid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_tag`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_taggedflowsession_SyncErrors"></a> taggedflowsession_SyncErrors

One-To-Many Relationship: [taggedflowsession taggedflowsession_SyncErrors](taggedflowsession.md#BKMK_taggedflowsession_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`taggedflowsession`|
|ReferencedAttribute|`taggedflowsessionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_taggedflowsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_taggedprocess_SyncErrors"></a> taggedprocess_SyncErrors

One-To-Many Relationship: [taggedprocess taggedprocess_SyncErrors](taggedprocess.md#BKMK_taggedprocess_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`taggedprocess`|
|ReferencedAttribute|`taggedprocessid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_taggedprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Task_SyncErrors"></a> Task_SyncErrors

One-To-Many Relationship: [task Task_SyncErrors](task.md#BKMK_Task_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`task`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_task_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_team_SyncError"></a> team_SyncError

One-To-Many Relationship: [team team_SyncError](team.md#BKMK_team_SyncError)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Team_SyncErrors"></a> Team_SyncErrors

One-To-Many Relationship: [team Team_SyncErrors](team.md#BKMK_Team_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_team_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_teammobileofflineprofilemembership_SyncErrors"></a> teammobileofflineprofilemembership_SyncErrors

One-To-Many Relationship: [teammobileofflineprofilemembership teammobileofflineprofilemembership_SyncErrors](teammobileofflineprofilemembership.md#BKMK_teammobileofflineprofilemembership_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`teammobileofflineprofilemembership`|
|ReferencedAttribute|`teammobileofflineprofilemembershipid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_teammobileofflineprofilemembership`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TeamTemplate_SyncErrors"></a> TeamTemplate_SyncErrors

One-To-Many Relationship: [teamtemplate TeamTemplate_SyncErrors](teamtemplate.md#BKMK_TeamTemplate_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`teamtemplate`|
|ReferencedAttribute|`teamtemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_teamtemplate_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_Template_SyncErrors"></a> Template_SyncErrors

One-To-Many Relationship: [template Template_SyncErrors](template.md#BKMK_Template_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`template`|
|ReferencedAttribute|`templateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_template_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_Territory_SyncErrors"></a> Territory_SyncErrors

One-To-Many Relationship: [territory Territory_SyncErrors](territory.md#BKMK_Territory_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`territory`|
|ReferencedAttribute|`territoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_territory_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_TransactionCurrency_SyncErrors"></a> TransactionCurrency_SyncErrors

One-To-Many Relationship: [transactioncurrency TransactionCurrency_SyncErrors](transactioncurrency.md#BKMK_TransactionCurrency_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_transactioncurrency_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_TranslationProcess_SyncErrors"></a> TranslationProcess_SyncErrors

One-To-Many Relationship: [translationprocess TranslationProcess_SyncErrors](translationprocess.md#BKMK_TranslationProcess_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`translationprocess`|
|ReferencedAttribute|`businessprocessflowinstanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_TranslationProcess_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_unstructuredfilesearchentity_SyncErrors"></a> unstructuredfilesearchentity_SyncErrors

One-To-Many Relationship: [unstructuredfilesearchentity unstructuredfilesearchentity_SyncErrors](unstructuredfilesearchentity.md#BKMK_unstructuredfilesearchentity_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`unstructuredfilesearchentity`|
|ReferencedAttribute|`unstructuredfilesearchentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_unstructuredfilesearchentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_unstructuredfilesearchrecord_SyncErrors"></a> unstructuredfilesearchrecord_SyncErrors

One-To-Many Relationship: [unstructuredfilesearchrecord unstructuredfilesearchrecord_SyncErrors](unstructuredfilesearchrecord.md#BKMK_unstructuredfilesearchrecord_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`unstructuredfilesearchrecord`|
|ReferencedAttribute|`unstructuredfilesearchrecordid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_unstructuredfilesearchrecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_usermobileofflineprofilemembership_SyncErrors"></a> usermobileofflineprofilemembership_SyncErrors

One-To-Many Relationship: [usermobileofflineprofilemembership usermobileofflineprofilemembership_SyncErrors](usermobileofflineprofilemembership.md#BKMK_usermobileofflineprofilemembership_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`usermobileofflineprofilemembership`|
|ReferencedAttribute|`usermobileofflineprofilemembershipid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_usermobileofflineprofilemembership`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_UserQuery_SyncErrors"></a> UserQuery_SyncErrors

One-To-Many Relationship: [userquery UserQuery_SyncErrors](userquery.md#BKMK_UserQuery_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`userquery`|
|ReferencedAttribute|`userqueryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_userquery_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_UserQueryVisualization_SyncErrors"></a> UserQueryVisualization_SyncErrors

One-To-Many Relationship: [userqueryvisualization UserQueryVisualization_SyncErrors](userqueryvisualization.md#BKMK_UserQueryVisualization_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`userqueryvisualization`|
|ReferencedAttribute|`userqueryvisualizationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_userqueryvisualization_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_userrating_SyncErrors"></a> userrating_SyncErrors

One-To-Many Relationship: [userrating userrating_SyncErrors](userrating.md#BKMK_userrating_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`userrating`|
|ReferencedAttribute|`userratingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_userrating`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_viewasexamplequestion_SyncErrors"></a> viewasexamplequestion_SyncErrors

One-To-Many Relationship: [viewasexamplequestion viewasexamplequestion_SyncErrors](viewasexamplequestion.md#BKMK_viewasexamplequestion_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`viewasexamplequestion`|
|ReferencedAttribute|`viewasexamplequestionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_viewasexamplequestion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_virtualentitymetadata_SyncErrors"></a> virtualentitymetadata_SyncErrors

One-To-Many Relationship: [virtualentitymetadata virtualentitymetadata_SyncErrors](virtualentitymetadata.md#BKMK_virtualentitymetadata_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`virtualentitymetadata`|
|ReferencedAttribute|`virtualentitymetadataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_virtualentitymetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Workflow_SyncErrors"></a> Workflow_SyncErrors

One-To-Many Relationship: [workflow Workflow_SyncErrors](workflow.md#BKMK_Workflow_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`workflow`|
|ReferencedAttribute|`workflowid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_workflow_syncerror`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_workflowbinary_SyncErrors"></a> workflowbinary_SyncErrors

One-To-Many Relationship: [workflowbinary workflowbinary_SyncErrors](workflowbinary.md#BKMK_workflowbinary_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`workflowbinary`|
|ReferencedAttribute|`workflowbinaryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_workflowbinary`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflowmetadata_SyncErrors"></a> workflowmetadata_SyncErrors

One-To-Many Relationship: [workflowmetadata workflowmetadata_SyncErrors](workflowmetadata.md#BKMK_workflowmetadata_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`workflowmetadata`|
|ReferencedAttribute|`workflowmetadataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_workflowmetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workqueue_SyncErrors"></a> workqueue_SyncErrors

One-To-Many Relationship: [workqueue workqueue_SyncErrors](workqueue.md#BKMK_workqueue_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`workqueue`|
|ReferencedAttribute|`workqueueid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_workqueue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workqueueitem_SyncErrors"></a> workqueueitem_SyncErrors

One-To-Many Relationship: [workqueueitem workqueueitem_SyncErrors](workqueueitem.md#BKMK_workqueueitem_SyncErrors)

|Property|Value|
|---|---|
|ReferencedEntity|`workqueueitem`|
|ReferencedAttribute|`workqueueitemid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_workqueueitem`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_SyncError_SyncErrors-one-to-many"></a> SyncError_SyncErrors

Many-To-One Relationship: [syncerror SyncError_SyncErrors](#BKMK_SyncError_SyncErrors-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`SyncError_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.syncerror?displayProperty=fullName>
