---
title: "Process Session (ProcessSession) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Process Session (ProcessSession) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Process Session (ProcessSession) table/entity reference (Microsoft Dataverse)

Information that is generated when a dialog is run. Every time that you run a dialog, a dialog session is created.

## Messages

The following table lists the messages for the Process Session (ProcessSession) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /processsessions(*processsessionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /processsessions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /processsessions(*processsessionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /processsessions(*processsessionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /processsessions<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /processsessions(*processsessionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /processsessions(*processsessionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /processsessions(*processsessionid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Process Session (ProcessSession) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Process Session** |
| **DisplayCollectionName** | **Process Sessions** |
| **SchemaName** | `ProcessSession` |
| **CollectionSchemaName** | `ProcessSession` |
| **EntitySetName** | `processsessions`|
| **LogicalName** | `processsession` |
| **LogicalCollectionName** | `processsessions` |
| **PrimaryIdAttribute** | `processsessionid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ActivityName](#BKMK_ActivityName)
- [CanceledOn](#BKMK_CanceledOn)
- [Comments](#BKMK_Comments)
- [CompletedOn](#BKMK_CompletedOn)
- [ErrorCode](#BKMK_ErrorCode)
- [ExecutedBy](#BKMK_ExecutedBy)
- [InputArguments](#BKMK_InputArguments)
- [Name](#BKMK_Name)
- [NextLinkedSessionId](#BKMK_NextLinkedSessionId)
- [OriginatingSessionId](#BKMK_OriginatingSessionId)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [PreviousLinkedSessionId](#BKMK_PreviousLinkedSessionId)
- [ProcessId](#BKMK_ProcessId)
- [ProcessSessionId](#BKMK_ProcessSessionId)
- [ProcessStageName](#BKMK_ProcessStageName)
- [ProcessState](#BKMK_ProcessState)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [StartedOn](#BKMK_StartedOn)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [StepName](#BKMK_StepName)

### <a name="BKMK_ActivityName"></a> ActivityName

|Property|Value|
|---|---|
|Description|**Name of the activity that is being executed.**|
|DisplayName|**Activity Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`activityname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_CanceledOn"></a> CanceledOn

|Property|Value|
|---|---|
|Description|**Date and time when the dialog session was canceled.**|
|DisplayName|**Canceled On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`canceledon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_Comments"></a> Comments

|Property|Value|
|---|---|
|Description|**User comments.**|
|DisplayName|**Comments**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`comments`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_CompletedOn"></a> CompletedOn

|Property|Value|
|---|---|
|Description|**Date and time when the dialog session was completed.**|
|DisplayName|**Completed On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`completedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ErrorCode"></a> ErrorCode

|Property|Value|
|---|---|
|Description|**Error code related to the dialog session.**|
|DisplayName|**Error Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`errorcode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_ExecutedBy"></a> ExecutedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who ran the dialog process.**|
|DisplayName|**Executed By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`executedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_InputArguments"></a> InputArguments

|Property|Value|
|---|---|
|Description|**Input arguments for the child dialog process.**|
|DisplayName|**Input Arguments**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`inputarguments`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the dialog session.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_NextLinkedSessionId"></a> NextLinkedSessionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the succeeding linked dialog session.**|
|DisplayName|**Next Linked Session**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`nextlinkedsessionid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|processsession|

### <a name="BKMK_OriginatingSessionId"></a> OriginatingSessionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the originating dialog session.**|
|DisplayName|**Originating Session**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`originatingsessionid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|processsession|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user or team who owns the dialog session.**|
|DisplayName|**Owner**|
|IsValidForForm|False|
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

### <a name="BKMK_PreviousLinkedSessionId"></a> PreviousLinkedSessionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the preceding linked dialog session.**|
|DisplayName|**Previous Linked Session**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`previouslinkedsessionid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|processsession|

### <a name="BKMK_ProcessId"></a> ProcessId

|Property|Value|
|---|---|
|Description|**Select the process activation record that is related to the dialog session.**|
|DisplayName|**Process**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|workflow|

### <a name="BKMK_ProcessSessionId"></a> ProcessSessionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the dialog session.**|
|DisplayName|**Dialog Session**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processsessionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ProcessStageName"></a> ProcessStageName

|Property|Value|
|---|---|
|Description|**Name of the dialog stage.**|
|DisplayName|**Dialog Stage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`processstagename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_ProcessState"></a> ProcessState

|Property|Value|
|---|---|
|Description|**State of the dialog process.**|
|DisplayName|**Process State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processstate`|
|RequiredLevel|None|
|Type|String|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**Unique identifier of the object with which the dialog session is associated.**|
|DisplayName|**Regarding**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account, activityfileattachment, adx_externalidentity, adx_invitation, adx_inviteredemption, adx_portalcomment, adx_setting, adx_webformsession, agentconversationmessage, agentconversationmessagefile, agentfeeditem, agenthubgoal, agenthubinsight, agenthubmetric, aicopilot, aiinsightcard, aiplugin, aipluginauth, aipluginconversationstarter, aipluginconversationstartermapping, aipluginexternalschema, aipluginexternalschemaproperty, aiplugingovernance, aiplugingovernanceext, aiplugininstance, aipluginoperation, aipluginoperationparameter, aipluginoperationresponsetemplate, aiplugintitle, aipluginusersetting, aiskillconfig, allowedmcpclient, annotation, appaction, appactionmigration, appactionrule, appelement, appentitysearchview, application, applicationuser, appmodulecomponentedge, appmodulecomponentnode, appointment, approvalprocess, approvalstageapproval, approvalstagecondition, approvalstageintelligent, approvalstageorder, appsetting, appusersetting, archivecleanupinfo, archivecleanupoperation, attributeclusterconfig, attributemaskingrule, bot, botcomponent, botcomponentcollection, bulkarchiveconfig, bulkarchivefailuredetail, bulkarchiveoperation, bulkarchiveoperationdetail, businessprocess, businessunit, businessunitnewsarticle, canvasappextendedmetadata, card, cascadegrantrevokeaccessrecordstracker, cascadegrantrevokeaccessversiontracker, catalog, catalogassignment, certificatecredential, channelaccessprofile, channelaccessprofilerule, chat, comment, connection, connectioninstance, connectionreference, connectionrole, connector, contact, conversationtranscript, convertrule, copilotexamplequestion, copilotglossaryterm, copilotsynonyms, credential, customapi, customapirequestparameter, customapiresponseproperty, customeraddress, customerrelationship, datalakefolder, datalakefolderpermission, datalakeworkspace, datalakeworkspacepermission, dataprocessingconfiguration, delegatedauthorization, deleteditemreference, desktopflowbinary, desktopflowmodule, dvfilesearch, dvfilesearchattribute, dvfilesearchentity, dvtablesearch, dvtablesearchattribute, dvtablesearchentity, email, enablearchivalrequest, entityclusterconfig, entityrecordfilter, environmentvariabledefinition, environmentvariablevalue, expiredprocess, exportedexcel, exportsolutionupload, externalparty, externalpartyitem, fabricaiskill, fax, featurecontrolsetting, federatedknowledgecitation, federatedknowledgeconfiguration, federatedknowledgeentityconfiguration, federatedknowledgemetadatarefresh, flowcapacityassignment, flowcredentialapplication, flowevent, flowmachine, flowmachinegroup, flowmachineimage, flowmachineimageversion, flowmachinenetwork, flowsessionbinary, fxexpression, goal, goalrollupquery, governanceconfiguration, holidaywrapper, internalcatalogassignment, kbarticle, kbarticlecomment, kbarticletemplate, keyvaultreference, knowledgearticle, knowledgebaserecord, knowledgefaq, knowledgesourceconsumer, knowledgesourceprofile, letter, mailbox, mailmergetemplate, mainfewshot, makerfewshot, managedidentity, maskingrule, mcpserver, mcptool, metadataforarchival, metric, mobileofflineprofileextension, msdynce_botcontent, msdyn_aibdataset, msdyn_aibdatasetfile, msdyn_aibdatasetrecord, msdyn_aibdatasetscontainer, msdyn_aibfeedbackloop, msdyn_aibfile, msdyn_aibfileattacheddata, msdyn_aiconfiguration, msdyn_aiconfigurationsearch, msdyn_aidataprocessingevent, msdyn_aidocumenttemplate, msdyn_aievaluationconfiguration, msdyn_aievaluationrun, msdyn_aievent, msdyn_aifptrainingdocument, msdyn_aimodel, msdyn_aimodelcatalog, msdyn_aiodimage, msdyn_aiodlabel, msdyn_aiodtrainingboundingbox, msdyn_aiodtrainingimage, msdyn_aioptimization, msdyn_aioptimizationprivatedata, msdyn_aitemplate, msdyn_aitestcase, msdyn_aitestcasedocument, msdyn_aitestcaseinput, msdyn_aitestrun, msdyn_aitestrunbatch, msdyn_analysiscomponent, msdyn_analysisjob, msdyn_analysisoverride, msdyn_analysisresult, msdyn_analysisresultdetail, msdyn_appinsightsmetadata, msdyn_copilotinteractions, msdyn_customcontrolextendedsettings, msdyn_dataflow, msdyn_dataflowconnectionreference, msdyn_dataflowrefreshhistory, msdyn_dataflowtemplate, msdyn_dataflow_datalakefolder, msdyn_dataworkspace, msdyn_dmsrequest, msdyn_dmsrequeststatus, msdyn_dmssyncrequest, msdyn_dmssyncstatus, msdyn_entitylinkchatconfiguration, msdyn_entityrefreshhistory, msdyn_favoriteknowledgearticle, msdyn_federatedarticle, msdyn_federatedarticleincident, msdyn_fileupload, msdyn_flow_actionapprovalmodel, msdyn_flow_approval, msdyn_flow_approvalrequest, msdyn_flow_approvalresponse, msdyn_flow_approvalstep, msdyn_flow_awaitallactionapprovalmodel, msdyn_flow_awaitallapprovalmodel, msdyn_flow_basicapprovalmodel, msdyn_flow_flowapproval, msdyn_formmapping, msdyn_function, msdyn_helppage, msdyn_historicalcaseharvestbatch, msdyn_historicalcaseharvestrun, msdyn_insightsstorevirtualentity, msdyn_integratedsearchprovider, msdyn_interimupdateknowledgearticle, msdyn_kalanguagesetting, msdyn_kbattachment, msdyn_kmfederatedsearchconfig, msdyn_kmpersonalizationsetting, msdyn_knowledgearticlecustomentity, msdyn_knowledgearticleimage, msdyn_knowledgearticletemplate, msdyn_knowledgeassetconfiguration, msdyn_knowledgeconfiguration, msdyn_knowledgeharvestjobrecord, msdyn_knowledgeinteractioninsight, msdyn_knowledgemanagementsetting, msdyn_knowledgepersonalfilter, msdyn_knowledgesearchfilter, msdyn_knowledgesearchinsight, msdyn_mobileapp, msdyn_modulerundetail, msdyn_plan, msdyn_planartifact, msdyn_planattachment, msdyn_pmanalysishistory, msdyn_pmbusinessruleautomationconfig, msdyn_pmcalendar, msdyn_pmcalendarversion, msdyn_pminferredtask, msdyn_pmprocessextendedmetadataversion, msdyn_pmprocesstemplate, msdyn_pmprocessusersettings, msdyn_pmprocessversion, msdyn_pmrecording, msdyn_pmsimulation, msdyn_pmtab, msdyn_pmtemplate, msdyn_pmview, msdyn_qna, msdyn_richtextfile, msdyn_salesforcestructuredobject, msdyn_salesforcestructuredqnaconfig, msdyn_schedule, msdyn_serviceconfiguration, msdyn_slakpi, msdyn_solutionhealthrule, msdyn_solutionhealthruleargument, msdyn_solutionhealthruleset, msdyn_tour, msdyn_virtualtablecolumncandidate, msdyn_workflowactionstatus, msgraphresourcetosubscription, mspcat_catalogsubmissionfiles, mspcat_packagestore, newprocess, organizationdatasyncfnostate, organizationdatasyncstate, organizationdatasyncsubscription, organizationdatasyncsubscriptionentity, organizationdatasyncsubscriptionfnotable, organizationsetting, package, packagehistory, pdfsetting, phonecall, plannerbusinessscenario, plannersyncaction, plugin, position, powerbidataset, powerbidatasetapdx, powerbimashupparameter, powerbireport, powerbireportapdx, powerfxrule, powerpagecomponent, powerpagesddosalert, powerpagesite, powerpagesitelanguage, powerpagesitepublished, powerpagesmanagedidentity, powerpagesscanreport, powerpagessourcefile, privilegecheckerlog, privilegecheckerrun, privilegesremovalsetting, processorregistration, processstageparameter, provisionlanguageforuser, purviewlabelinfo, purviewlabelsynccache, queue, queueitem, reconciliationentityinfo, reconciliationentitystepinfo, reconciliationinfo, recordfilter, recurringappointmentmaster, recyclebinconfig, relationshiprole, report, reportparameter, retaineddataexcel, retentioncleanupinfo, retentioncleanupoperation, retentionconfig, retentionfailuredetail, retentionoperation, retentionoperationdetail, retentionsuccessdetail, revokeinheritedaccessrecordstracker, roleeditorlayout, rollupfield, routingrule, routingruleitem, savingrule, sa_suggestedaction, sa_suggestedactioncriteria, searchattributesettings, searchcustomanalyzer, searchrelationshipsettings, sensitivitylabelattributemapping, serviceplan, serviceplancustomcontrol, serviceplanmapping, settingdefinition, sharedlinksetting, sharedobject, sharedworkspace, sharedworkspacepool, sharepointdocumentlocation, sharepointmanagedidentity, sharepointsite, sideloadedaiplugin, signalregistration, sla, socialactivity, socialprofile, solutioncomponentattributeconfiguration, solutioncomponentbatchconfiguration, solutioncomponentconfiguration, solutioncomponentrelationshipconfiguration, stagedattributelookupvalue, stagedattributepicklistvalue, stagedentity, stagedentityattribute, stagedentityrelationship, stagedentityrelationshiprelationships, stagedentityrelationshiprole, stagedmetadataasyncoperation, stagedoptionset, stagedrelationship, stagedrelationshipextracondition, stagedviewattribute, stagesolutionupload, subject, supportusertable, synapsedatabase, synapselinkexternaltablestate, synapselinkprofile, synapselinkprofileentity, synapselinkprofileentitystate, synapselinkschedule, systemuser, systemuserauthorizationchangetracker, tag, taggedflowsession, taggedprocess, task, tdsmetadata, team, teammobileofflineprofilemembership, template, territory, theme, toolinggateway, toolinggatewaymcpserver, traitregistration, transactioncurrency, translationprocess, unstructuredfilesearchentity, unstructuredfilesearchrecord, unstructuredfilesearchrecordstatus, usermapping, usermobileofflineprofilemembership, userrating, uxagentcomponent, uxagentcomponentrevision, uxagentproject, uxagentprojectfile, viewasexamplequestion, virtualentitymetadata, workflowbinary, workflowmetadata, workqueue, workqueueitem|

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

### <a name="BKMK_StartedOn"></a> StartedOn

|Property|Value|
|---|---|
|Description|**Date and time when the dialog session was started.**|
|DisplayName|**Started On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`startedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Status of the dialog session.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`processsession_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Incomplete**<br />DefaultStatus: 1<br />InvariantName: `Incomplete`|
|1|Label: **Complete**<br />DefaultStatus: 2<br />InvariantName: `Complete`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Reason for the status of the dialog session.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`processsession_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Not Started**<br />State:0<br />TransitionData: None|
|2|Label: **In Progress**<br />State:0<br />TransitionData: None|
|3|Label: **Paused**<br />State:0<br />TransitionData: None|
|4|Label: **Completed**<br />State:1<br />TransitionData: None|
|5|Label: **Canceled**<br />State:1<br />TransitionData: None|
|6|Label: **Failed**<br />State:1<br />TransitionData: None|

### <a name="BKMK_StepName"></a> StepName

|Property|Value|
|---|---|
|Description|**Name of the dialog step.**|
|DisplayName|**Step Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`stepname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CanceledBy](#BKMK_CanceledBy)
- [CompletedBy](#BKMK_CompletedBy)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ExecutedOn](#BKMK_ExecutedOn)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [ProtectionKey](#BKMK_ProtectionKey)
- [StartedBy](#BKMK_StartedBy)

### <a name="BKMK_CanceledBy"></a> CanceledBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who canceled the dialog session.**|
|DisplayName|**Canceled By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`canceledby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CompletedBy"></a> CompletedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who completed the dialog session.**|
|DisplayName|**Completed By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`completedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who started the dialog session.**|
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
|Description|**Date and time when the dialog session was created.**|
|DisplayName|**Created On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who created the dialog session.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ExecutedOn"></a> ExecutedOn

|Property|Value|
|---|---|
|Description|**Date and time when the dialog process was run.**|
|DisplayName|**Executed On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`executedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the dialog session.**|
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
|Description|**Date and time when the dialog session was last modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who modified the dialog session.**|
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
|Description|**Unique identifier of the business unit that owns the dialog session.**|
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
|Description|**Unique identifier of the team who owns the dialog session.**|
|DisplayName|**Owning Team**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningteam`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|team|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who owns the dialog session.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ProtectionKey"></a> ProtectionKey

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Protection Key**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`protectionkey`|
|RequiredLevel|None|
|Type|String|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_StartedBy"></a> StartedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who started the dialog session.**|
|DisplayName|**Started By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`startedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [Account_ProcessSessions](#BKMK_Account_ProcessSessions)
- [activityfileattachment_ProcessSession](#BKMK_activityfileattachment_ProcessSession)
- [adx_externalidentity_ProcessSession](#BKMK_adx_externalidentity_ProcessSession)
- [adx_invitation_ProcessSession](#BKMK_adx_invitation_ProcessSession)
- [adx_inviteredemption_ProcessSession](#BKMK_adx_inviteredemption_ProcessSession)
- [adx_portalcomment_ProcessSession](#BKMK_adx_portalcomment_ProcessSession)
- [adx_setting_ProcessSession](#BKMK_adx_setting_ProcessSession)
- [adx_webformsession_ProcessSession](#BKMK_adx_webformsession_ProcessSession)
- [aicopilot_ProcessSession](#BKMK_aicopilot_ProcessSession)
- [aiplugin_ProcessSession](#BKMK_aiplugin_ProcessSession)
- [aipluginauth_ProcessSession](#BKMK_aipluginauth_ProcessSession)
- [aipluginconversationstarter_ProcessSession](#BKMK_aipluginconversationstarter_ProcessSession)
- [aipluginconversationstartermapping_ProcessSession](#BKMK_aipluginconversationstartermapping_ProcessSession)
- [aipluginexternalschema_ProcessSession](#BKMK_aipluginexternalschema_ProcessSession)
- [aipluginexternalschemaproperty_ProcessSession](#BKMK_aipluginexternalschemaproperty_ProcessSession)
- [aiplugingovernance_ProcessSession](#BKMK_aiplugingovernance_ProcessSession)
- [aiplugingovernanceext_ProcessSession](#BKMK_aiplugingovernanceext_ProcessSession)
- [aiplugininstance_ProcessSession](#BKMK_aiplugininstance_ProcessSession)
- [aipluginoperation_ProcessSession](#BKMK_aipluginoperation_ProcessSession)
- [aipluginoperationparameter_ProcessSession](#BKMK_aipluginoperationparameter_ProcessSession)
- [aipluginoperationresponsetemplate_ProcessSession](#BKMK_aipluginoperationresponsetemplate_ProcessSession)
- [aiplugintitle_ProcessSession](#BKMK_aiplugintitle_ProcessSession)
- [aipluginusersetting_ProcessSession](#BKMK_aipluginusersetting_ProcessSession)
- [allowedmcpclient_ProcessSession](#BKMK_allowedmcpclient_ProcessSession)
- [Annotation_ProcessSessions](#BKMK_Annotation_ProcessSessions)
- [appaction_ProcessSession](#BKMK_appaction_ProcessSession)
- [appactionmigration_ProcessSession](#BKMK_appactionmigration_ProcessSession)
- [appactionrule_ProcessSession](#BKMK_appactionrule_ProcessSession)
- [application_ProcessSession](#BKMK_application_ProcessSession)
- [applicationuser_ProcessSession](#BKMK_applicationuser_ProcessSession)
- [Appointment_ProcessSessions](#BKMK_Appointment_ProcessSessions)
- [approvalprocess_ProcessSession](#BKMK_approvalprocess_ProcessSession)
- [approvalstageapproval_ProcessSession](#BKMK_approvalstageapproval_ProcessSession)
- [approvalstagecondition_ProcessSession](#BKMK_approvalstagecondition_ProcessSession)
- [approvalstageintelligent_ProcessSession](#BKMK_approvalstageintelligent_ProcessSession)
- [approvalstageorder_ProcessSession](#BKMK_approvalstageorder_ProcessSession)
- [attributeclusterconfig_ProcessSession](#BKMK_attributeclusterconfig_ProcessSession)
- [attributemaskingrule_ProcessSession](#BKMK_attributemaskingrule_ProcessSession)
- [bot_ProcessSession](#BKMK_bot_ProcessSession)
- [botcomponent_ProcessSession](#BKMK_botcomponent_ProcessSession)
- [botcomponentcollection_ProcessSession](#BKMK_botcomponentcollection_ProcessSession)
- [businessprocess_ProcessSession](#BKMK_businessprocess_ProcessSession)
- [BusinessUnit_ProcessSessions](#BKMK_BusinessUnit_ProcessSessions)
- [BusinessUnitNewsArticle_ProcessSessions](#BKMK_BusinessUnitNewsArticle_ProcessSessions)
- [card_ProcessSession](#BKMK_card_ProcessSession)
- [catalog_ProcessSession](#BKMK_catalog_ProcessSession)
- [catalogassignment_ProcessSession](#BKMK_catalogassignment_ProcessSession)
- [certificatecredential_ProcessSession](#BKMK_certificatecredential_ProcessSession)
- [chat_ProcessSession](#BKMK_chat_ProcessSession)
- [Connection_ProcessSessions](#BKMK_Connection_ProcessSessions)
- [connectioninstance_ProcessSession](#BKMK_connectioninstance_ProcessSession)
- [connectionreference_ProcessSession](#BKMK_connectionreference_ProcessSession)
- [ConnectionRole_ProcessSessions](#BKMK_ConnectionRole_ProcessSessions)
- [connector_ProcessSession](#BKMK_connector_ProcessSession)
- [Contact_ProcessSessions](#BKMK_Contact_ProcessSessions)
- [conversationtranscript_ProcessSession](#BKMK_conversationtranscript_ProcessSession)
- [copilotexamplequestion_ProcessSession](#BKMK_copilotexamplequestion_ProcessSession)
- [copilotglossaryterm_ProcessSession](#BKMK_copilotglossaryterm_ProcessSession)
- [copilotsynonyms_ProcessSession](#BKMK_copilotsynonyms_ProcessSession)
- [credential_ProcessSession](#BKMK_credential_ProcessSession)
- [customapi_ProcessSession](#BKMK_customapi_ProcessSession)
- [customapirequestparameter_ProcessSession](#BKMK_customapirequestparameter_ProcessSession)
- [customapiresponseproperty_ProcessSession](#BKMK_customapiresponseproperty_ProcessSession)
- [CustomerAddress_ProcessSessions](#BKMK_CustomerAddress_ProcessSessions)
- [datalakefolder_ProcessSession](#BKMK_datalakefolder_ProcessSession)
- [datalakefolderpermission_ProcessSession](#BKMK_datalakefolderpermission_ProcessSession)
- [datalakeworkspace_ProcessSession](#BKMK_datalakeworkspace_ProcessSession)
- [datalakeworkspacepermission_ProcessSession](#BKMK_datalakeworkspacepermission_ProcessSession)
- [dataprocessingconfiguration_ProcessSession](#BKMK_dataprocessingconfiguration_ProcessSession)
- [delegatedauthorization_ProcessSession](#BKMK_delegatedauthorization_ProcessSession)
- [desktopflowbinary_ProcessSession](#BKMK_desktopflowbinary_ProcessSession)
- [desktopflowmodule_ProcessSession](#BKMK_desktopflowmodule_ProcessSession)
- [dvfilesearch_ProcessSession](#BKMK_dvfilesearch_ProcessSession)
- [dvfilesearchattribute_ProcessSession](#BKMK_dvfilesearchattribute_ProcessSession)
- [dvfilesearchentity_ProcessSession](#BKMK_dvfilesearchentity_ProcessSession)
- [dvtablesearch_ProcessSession](#BKMK_dvtablesearch_ProcessSession)
- [dvtablesearchattribute_ProcessSession](#BKMK_dvtablesearchattribute_ProcessSession)
- [dvtablesearchentity_ProcessSession](#BKMK_dvtablesearchentity_ProcessSession)
- [Email_ProcessSessions](#BKMK_Email_ProcessSessions)
- [entityclusterconfig_ProcessSession](#BKMK_entityclusterconfig_ProcessSession)
- [entityrecordfilter_ProcessSession](#BKMK_entityrecordfilter_ProcessSession)
- [environmentvariabledefinition_ProcessSession](#BKMK_environmentvariabledefinition_ProcessSession)
- [environmentvariablevalue_ProcessSession](#BKMK_environmentvariablevalue_ProcessSession)
- [ExpiredProcess_ProcessSessions](#BKMK_ExpiredProcess_ProcessSessions)
- [exportedexcel_ProcessSession](#BKMK_exportedexcel_ProcessSession)
- [exportsolutionupload_ProcessSession](#BKMK_exportsolutionupload_ProcessSession)
- [fabricaiskill_ProcessSession](#BKMK_fabricaiskill_ProcessSession)
- [Fax_ProcessSessions](#BKMK_Fax_ProcessSessions)
- [featurecontrolsetting_ProcessSession](#BKMK_featurecontrolsetting_ProcessSession)
- [federatedknowledgeconfiguration_ProcessSession](#BKMK_federatedknowledgeconfiguration_ProcessSession)
- [federatedknowledgeentityconfiguration_ProcessSession](#BKMK_federatedknowledgeentityconfiguration_ProcessSession)
- [flowcapacityassignment_ProcessSession](#BKMK_flowcapacityassignment_ProcessSession)
- [flowcredentialapplication_ProcessSession](#BKMK_flowcredentialapplication_ProcessSession)
- [flowevent_ProcessSession](#BKMK_flowevent_ProcessSession)
- [flowmachine_ProcessSession](#BKMK_flowmachine_ProcessSession)
- [flowmachinegroup_ProcessSession](#BKMK_flowmachinegroup_ProcessSession)
- [flowmachineimage_ProcessSession](#BKMK_flowmachineimage_ProcessSession)
- [flowmachineimageversion_ProcessSession](#BKMK_flowmachineimageversion_ProcessSession)
- [flowmachinenetwork_ProcessSession](#BKMK_flowmachinenetwork_ProcessSession)
- [flowsessionbinary_ProcessSession](#BKMK_flowsessionbinary_ProcessSession)
- [fxexpression_ProcessSession](#BKMK_fxexpression_ProcessSession)
- [Goal_ProcessSessions](#BKMK_Goal_ProcessSessions)
- [goalrollupquery_ProcessSessions](#BKMK_goalrollupquery_ProcessSessions)
- [governanceconfiguration_ProcessSession](#BKMK_governanceconfiguration_ProcessSession)
- [KbArticle_ProcessSessions](#BKMK_KbArticle_ProcessSessions)
- [KbArticleComment_ProcessSessions](#BKMK_KbArticleComment_ProcessSessions)
- [KbArticleTemplate_ProcessSessions](#BKMK_KbArticleTemplate_ProcessSessions)
- [keyvaultreference_ProcessSession](#BKMK_keyvaultreference_ProcessSession)
- [knowledgearticle_ProcessSession](#BKMK_knowledgearticle_ProcessSession)
- [KnowledgeBaseRecord_ProcessSession](#BKMK_KnowledgeBaseRecord_ProcessSession)
- [knowledgefaq_ProcessSession](#BKMK_knowledgefaq_ProcessSession)
- [Letter_ProcessSessions](#BKMK_Letter_ProcessSessions)
- [lk_processsession_canceledby](#BKMK_lk_processsession_canceledby)
- [lk_processsession_completedby](#BKMK_lk_processsession_completedby)
- [lk_processsession_createdby](#BKMK_lk_processsession_createdby)
- [lk_processsession_executedby](#BKMK_lk_processsession_executedby)
- [lk_processsession_modifiedby](#BKMK_lk_processsession_modifiedby)
- [lk_processsession_nextlinkedsessionid](#BKMK_lk_processsession_nextlinkedsessionid-many-to-one)
- [lk_processsession_originatingsessionid](#BKMK_lk_processsession_originatingsessionid-many-to-one)
- [lk_processsession_previouslinkedsessionid](#BKMK_lk_processsession_previouslinkedsessionid-many-to-one)
- [lk_processsession_processid](#BKMK_lk_processsession_processid)
- [lk_processsession_startedby](#BKMK_lk_processsession_startedby)
- [lk_processsessionbase_createdonbehalfby](#BKMK_lk_processsessionbase_createdonbehalfby)
- [lk_processsessionbase_modifiedonbehalfby](#BKMK_lk_processsessionbase_modifiedonbehalfby)
- [mailbox_processsessions](#BKMK_mailbox_processsessions)
- [MailMergeTemplate_ProcessSessions](#BKMK_MailMergeTemplate_ProcessSessions)
- [mainfewshot_ProcessSession](#BKMK_mainfewshot_ProcessSession)
- [makerfewshot_ProcessSession](#BKMK_makerfewshot_ProcessSession)
- [managedidentity_ProcessSession](#BKMK_managedidentity_ProcessSession)
- [maskingrule_ProcessSession](#BKMK_maskingrule_ProcessSession)
- [mcpserver_ProcessSession](#BKMK_mcpserver_ProcessSession)
- [mcptool_ProcessSession](#BKMK_mcptool_ProcessSession)
- [metadataforarchival_ProcessSession](#BKMK_metadataforarchival_ProcessSession)
- [metric_ProcessSessions](#BKMK_metric_ProcessSessions)
- [mobileofflineprofileextension_ProcessSession](#BKMK_mobileofflineprofileextension_ProcessSession)
- [msdyn_aibdataset_ProcessSession](#BKMK_msdyn_aibdataset_ProcessSession)
- [msdyn_aibdatasetfile_ProcessSession](#BKMK_msdyn_aibdatasetfile_ProcessSession)
- [msdyn_aibdatasetrecord_ProcessSession](#BKMK_msdyn_aibdatasetrecord_ProcessSession)
- [msdyn_aibdatasetscontainer_ProcessSession](#BKMK_msdyn_aibdatasetscontainer_ProcessSession)
- [msdyn_aibfeedbackloop_ProcessSession](#BKMK_msdyn_aibfeedbackloop_ProcessSession)
- [msdyn_aibfile_ProcessSession](#BKMK_msdyn_aibfile_ProcessSession)
- [msdyn_aibfileattacheddata_ProcessSession](#BKMK_msdyn_aibfileattacheddata_ProcessSession)
- [msdyn_aiconfiguration_ProcessSession](#BKMK_msdyn_aiconfiguration_ProcessSession)
- [msdyn_aidataprocessingevent_ProcessSession](#BKMK_msdyn_aidataprocessingevent_ProcessSession)
- [msdyn_aidocumenttemplate_ProcessSession](#BKMK_msdyn_aidocumenttemplate_ProcessSession)
- [msdyn_aievaluationconfiguration_ProcessSession](#BKMK_msdyn_aievaluationconfiguration_ProcessSession)
- [msdyn_aievaluationrun_ProcessSession](#BKMK_msdyn_aievaluationrun_ProcessSession)
- [msdyn_aievent_ProcessSession](#BKMK_msdyn_aievent_ProcessSession)
- [msdyn_aifptrainingdocument_ProcessSession](#BKMK_msdyn_aifptrainingdocument_ProcessSession)
- [msdyn_aimodel_ProcessSession](#BKMK_msdyn_aimodel_ProcessSession)
- [msdyn_aiodimage_ProcessSession](#BKMK_msdyn_aiodimage_ProcessSession)
- [msdyn_aiodlabel_ProcessSession](#BKMK_msdyn_aiodlabel_ProcessSession)
- [msdyn_aiodtrainingboundingbox_ProcessSession](#BKMK_msdyn_aiodtrainingboundingbox_ProcessSession)
- [msdyn_aiodtrainingimage_ProcessSession](#BKMK_msdyn_aiodtrainingimage_ProcessSession)
- [msdyn_aitemplate_ProcessSession](#BKMK_msdyn_aitemplate_ProcessSession)
- [msdyn_aitestcase_ProcessSession](#BKMK_msdyn_aitestcase_ProcessSession)
- [msdyn_aitestcasedocument_ProcessSession](#BKMK_msdyn_aitestcasedocument_ProcessSession)
- [msdyn_aitestcaseinput_ProcessSession](#BKMK_msdyn_aitestcaseinput_ProcessSession)
- [msdyn_aitestrun_ProcessSession](#BKMK_msdyn_aitestrun_ProcessSession)
- [msdyn_aitestrunbatch_ProcessSession](#BKMK_msdyn_aitestrunbatch_ProcessSession)
- [msdyn_analysiscomponent_ProcessSession](#BKMK_msdyn_analysiscomponent_ProcessSession)
- [msdyn_analysisjob_ProcessSession](#BKMK_msdyn_analysisjob_ProcessSession)
- [msdyn_analysisoverride_ProcessSession](#BKMK_msdyn_analysisoverride_ProcessSession)
- [msdyn_analysisresult_ProcessSession](#BKMK_msdyn_analysisresult_ProcessSession)
- [msdyn_analysisresultdetail_ProcessSession](#BKMK_msdyn_analysisresultdetail_ProcessSession)
- [msdyn_appinsightsmetadata_ProcessSession](#BKMK_msdyn_appinsightsmetadata_ProcessSession)
- [msdyn_copilotinteractions_ProcessSession](#BKMK_msdyn_copilotinteractions_ProcessSession)
- [msdyn_customcontrolextendedsettings_ProcessSession](#BKMK_msdyn_customcontrolextendedsettings_ProcessSession)
- [msdyn_dataflow_datalakefolder_ProcessSession](#BKMK_msdyn_dataflow_datalakefolder_ProcessSession)
- [msdyn_dataflow_ProcessSession](#BKMK_msdyn_dataflow_ProcessSession)
- [msdyn_dataflowconnectionreference_ProcessSession](#BKMK_msdyn_dataflowconnectionreference_ProcessSession)
- [msdyn_dataflowrefreshhistory_ProcessSession](#BKMK_msdyn_dataflowrefreshhistory_ProcessSession)
- [msdyn_dataflowtemplate_ProcessSession](#BKMK_msdyn_dataflowtemplate_ProcessSession)
- [msdyn_dmsrequest_ProcessSession](#BKMK_msdyn_dmsrequest_ProcessSession)
- [msdyn_dmsrequeststatus_ProcessSession](#BKMK_msdyn_dmsrequeststatus_ProcessSession)
- [msdyn_dmssyncrequest_ProcessSession](#BKMK_msdyn_dmssyncrequest_ProcessSession)
- [msdyn_dmssyncstatus_ProcessSession](#BKMK_msdyn_dmssyncstatus_ProcessSession)
- [msdyn_entitylinkchatconfiguration_ProcessSession](#BKMK_msdyn_entitylinkchatconfiguration_ProcessSession)
- [msdyn_entityrefreshhistory_ProcessSession](#BKMK_msdyn_entityrefreshhistory_ProcessSession)
- [msdyn_favoriteknowledgearticle_ProcessSession](#BKMK_msdyn_favoriteknowledgearticle_ProcessSession)
- [msdyn_federatedarticle_ProcessSession](#BKMK_msdyn_federatedarticle_ProcessSession)
- [msdyn_federatedarticleincident_ProcessSession](#BKMK_msdyn_federatedarticleincident_ProcessSession)
- [msdyn_fileupload_ProcessSession](#BKMK_msdyn_fileupload_ProcessSession)
- [msdyn_flow_actionapprovalmodel_ProcessSession](#BKMK_msdyn_flow_actionapprovalmodel_ProcessSession)
- [msdyn_flow_approval_ProcessSession](#BKMK_msdyn_flow_approval_ProcessSession)
- [msdyn_flow_approvalrequest_ProcessSession](#BKMK_msdyn_flow_approvalrequest_ProcessSession)
- [msdyn_flow_approvalresponse_ProcessSession](#BKMK_msdyn_flow_approvalresponse_ProcessSession)
- [msdyn_flow_approvalstep_ProcessSession](#BKMK_msdyn_flow_approvalstep_ProcessSession)
- [msdyn_flow_awaitallactionapprovalmodel_ProcessSession](#BKMK_msdyn_flow_awaitallactionapprovalmodel_ProcessSession)
- [msdyn_flow_awaitallapprovalmodel_ProcessSession](#BKMK_msdyn_flow_awaitallapprovalmodel_ProcessSession)
- [msdyn_flow_basicapprovalmodel_ProcessSession](#BKMK_msdyn_flow_basicapprovalmodel_ProcessSession)
- [msdyn_flow_flowapproval_ProcessSession](#BKMK_msdyn_flow_flowapproval_ProcessSession)
- [msdyn_formmapping_ProcessSession](#BKMK_msdyn_formmapping_ProcessSession)
- [msdyn_function_ProcessSession](#BKMK_msdyn_function_ProcessSession)
- [msdyn_helppage_ProcessSession](#BKMK_msdyn_helppage_ProcessSession)
- [msdyn_historicalcaseharvestbatch_ProcessSession](#BKMK_msdyn_historicalcaseharvestbatch_ProcessSession)
- [msdyn_historicalcaseharvestrun_ProcessSession](#BKMK_msdyn_historicalcaseharvestrun_ProcessSession)
- [msdyn_insightsstorevirtualentity_ProcessSession](#BKMK_msdyn_insightsstorevirtualentity_ProcessSession)
- [msdyn_integratedsearchprovider_ProcessSession](#BKMK_msdyn_integratedsearchprovider_ProcessSession)
- [msdyn_kalanguagesetting_ProcessSession](#BKMK_msdyn_kalanguagesetting_ProcessSession)
- [msdyn_kbattachment_ProcessSession](#BKMK_msdyn_kbattachment_ProcessSession)
- [msdyn_kmfederatedsearchconfig_ProcessSession](#BKMK_msdyn_kmfederatedsearchconfig_ProcessSession)
- [msdyn_kmpersonalizationsetting_ProcessSession](#BKMK_msdyn_kmpersonalizationsetting_ProcessSession)
- [msdyn_knowledgearticleimage_ProcessSession](#BKMK_msdyn_knowledgearticleimage_ProcessSession)
- [msdyn_knowledgearticletemplate_ProcessSession](#BKMK_msdyn_knowledgearticletemplate_ProcessSession)
- [msdyn_knowledgeassetconfiguration_ProcessSession](#BKMK_msdyn_knowledgeassetconfiguration_ProcessSession)
- [msdyn_knowledgeconfiguration_ProcessSession](#BKMK_msdyn_knowledgeconfiguration_ProcessSession)
- [msdyn_knowledgeharvestjobrecord_ProcessSession](#BKMK_msdyn_knowledgeharvestjobrecord_ProcessSession)
- [msdyn_knowledgeinteractioninsight_ProcessSession](#BKMK_msdyn_knowledgeinteractioninsight_ProcessSession)
- [msdyn_knowledgemanagementsetting_ProcessSession](#BKMK_msdyn_knowledgemanagementsetting_ProcessSession)
- [msdyn_knowledgepersonalfilter_ProcessSession](#BKMK_msdyn_knowledgepersonalfilter_ProcessSession)
- [msdyn_knowledgesearchfilter_ProcessSession](#BKMK_msdyn_knowledgesearchfilter_ProcessSession)
- [msdyn_knowledgesearchinsight_ProcessSession](#BKMK_msdyn_knowledgesearchinsight_ProcessSession)
- [msdyn_mobileapp_ProcessSession](#BKMK_msdyn_mobileapp_ProcessSession)
- [msdyn_modulerundetail_ProcessSession](#BKMK_msdyn_modulerundetail_ProcessSession)
- [msdyn_pmanalysishistory_ProcessSession](#BKMK_msdyn_pmanalysishistory_ProcessSession)
- [msdyn_pmbusinessruleautomationconfig_ProcessSession](#BKMK_msdyn_pmbusinessruleautomationconfig_ProcessSession)
- [msdyn_pmcalendar_ProcessSession](#BKMK_msdyn_pmcalendar_ProcessSession)
- [msdyn_pmcalendarversion_ProcessSession](#BKMK_msdyn_pmcalendarversion_ProcessSession)
- [msdyn_pminferredtask_ProcessSession](#BKMK_msdyn_pminferredtask_ProcessSession)
- [msdyn_pmprocessextendedmetadataversion_ProcessSession](#BKMK_msdyn_pmprocessextendedmetadataversion_ProcessSession)
- [msdyn_pmprocesstemplate_ProcessSession](#BKMK_msdyn_pmprocesstemplate_ProcessSession)
- [msdyn_pmprocessusersettings_ProcessSession](#BKMK_msdyn_pmprocessusersettings_ProcessSession)
- [msdyn_pmprocessversion_ProcessSession](#BKMK_msdyn_pmprocessversion_ProcessSession)
- [msdyn_pmrecording_ProcessSession](#BKMK_msdyn_pmrecording_ProcessSession)
- [msdyn_pmsimulation_ProcessSession](#BKMK_msdyn_pmsimulation_ProcessSession)
- [msdyn_pmtab_ProcessSession](#BKMK_msdyn_pmtab_ProcessSession)
- [msdyn_pmtemplate_ProcessSession](#BKMK_msdyn_pmtemplate_ProcessSession)
- [msdyn_pmview_ProcessSession](#BKMK_msdyn_pmview_ProcessSession)
- [msdyn_qna_ProcessSession](#BKMK_msdyn_qna_ProcessSession)
- [msdyn_richtextfile_ProcessSession](#BKMK_msdyn_richtextfile_ProcessSession)
- [msdyn_salesforcestructuredobject_ProcessSession](#BKMK_msdyn_salesforcestructuredobject_ProcessSession)
- [msdyn_salesforcestructuredqnaconfig_ProcessSession](#BKMK_msdyn_salesforcestructuredqnaconfig_ProcessSession)
- [msdyn_schedule_ProcessSession](#BKMK_msdyn_schedule_ProcessSession)
- [msdyn_serviceconfiguration_ProcessSession](#BKMK_msdyn_serviceconfiguration_ProcessSession)
- [msdyn_slakpi_ProcessSession](#BKMK_msdyn_slakpi_ProcessSession)
- [msdyn_solutionhealthrule_ProcessSession](#BKMK_msdyn_solutionhealthrule_ProcessSession)
- [msdyn_solutionhealthruleargument_ProcessSession](#BKMK_msdyn_solutionhealthruleargument_ProcessSession)
- [msdyn_solutionhealthruleset_ProcessSession](#BKMK_msdyn_solutionhealthruleset_ProcessSession)
- [msdyn_tour_ProcessSession](#BKMK_msdyn_tour_ProcessSession)
- [msdyn_virtualtablecolumncandidate_ProcessSession](#BKMK_msdyn_virtualtablecolumncandidate_ProcessSession)
- [msdyn_workflowactionstatus_ProcessSession](#BKMK_msdyn_workflowactionstatus_ProcessSession)
- [msdynce_botcontent_ProcessSession](#BKMK_msdynce_botcontent_ProcessSession)
- [msgraphresourcetosubscription_ProcessSession](#BKMK_msgraphresourcetosubscription_ProcessSession)
- [mspcat_catalogsubmissionfiles_ProcessSession](#BKMK_mspcat_catalogsubmissionfiles_ProcessSession)
- [mspcat_packagestore_ProcessSession](#BKMK_mspcat_packagestore_ProcessSession)
- [NewProcess_ProcessSessions](#BKMK_NewProcess_ProcessSessions)
- [organizationdatasyncfnostate_ProcessSession](#BKMK_organizationdatasyncfnostate_ProcessSession)
- [organizationdatasyncstate_ProcessSession](#BKMK_organizationdatasyncstate_ProcessSession)
- [organizationdatasyncsubscription_ProcessSession](#BKMK_organizationdatasyncsubscription_ProcessSession)
- [organizationdatasyncsubscriptionentity_ProcessSession](#BKMK_organizationdatasyncsubscriptionentity_ProcessSession)
- [organizationdatasyncsubscriptionfnotable_ProcessSession](#BKMK_organizationdatasyncsubscriptionfnotable_ProcessSession)
- [owner_processsessions](#BKMK_owner_processsessions)
- [Owning_businessunit_processsessions](#BKMK_Owning_businessunit_processsessions)
- [package_ProcessSession](#BKMK_package_ProcessSession)
- [packagehistory_ProcessSession](#BKMK_packagehistory_ProcessSession)
- [PhoneCall_ProcessSessions](#BKMK_PhoneCall_ProcessSessions)
- [plannerbusinessscenario_ProcessSession](#BKMK_plannerbusinessscenario_ProcessSession)
- [plannersyncaction_ProcessSession](#BKMK_plannersyncaction_ProcessSession)
- [plugin_ProcessSession](#BKMK_plugin_ProcessSession)
- [position_ProcessSession](#BKMK_position_ProcessSession)
- [powerbidataset_ProcessSession](#BKMK_powerbidataset_ProcessSession)
- [powerbidatasetapdx_ProcessSession](#BKMK_powerbidatasetapdx_ProcessSession)
- [powerbimashupparameter_ProcessSession](#BKMK_powerbimashupparameter_ProcessSession)
- [powerbireport_ProcessSession](#BKMK_powerbireport_ProcessSession)
- [powerbireportapdx_ProcessSession](#BKMK_powerbireportapdx_ProcessSession)
- [powerfxrule_ProcessSession](#BKMK_powerfxrule_ProcessSession)
- [powerpagecomponent_ProcessSession](#BKMK_powerpagecomponent_ProcessSession)
- [powerpagesddosalert_ProcessSession](#BKMK_powerpagesddosalert_ProcessSession)
- [powerpagesite_ProcessSession](#BKMK_powerpagesite_ProcessSession)
- [powerpagesitelanguage_ProcessSession](#BKMK_powerpagesitelanguage_ProcessSession)
- [powerpagesitepublished_ProcessSession](#BKMK_powerpagesitepublished_ProcessSession)
- [powerpagesmanagedidentity_ProcessSession](#BKMK_powerpagesmanagedidentity_ProcessSession)
- [powerpagesscanreport_ProcessSession](#BKMK_powerpagesscanreport_ProcessSession)
- [powerpagessourcefile_ProcessSession](#BKMK_powerpagessourcefile_ProcessSession)
- [privilegecheckerlog_ProcessSession](#BKMK_privilegecheckerlog_ProcessSession)
- [privilegecheckerrun_ProcessSession](#BKMK_privilegecheckerrun_ProcessSession)
- [privilegesremovalsetting_ProcessSession](#BKMK_privilegesremovalsetting_ProcessSession)
- [processstageparameter_ProcessSession](#BKMK_processstageparameter_ProcessSession)
- [provisionlanguageforuser_ProcessSession](#BKMK_provisionlanguageforuser_ProcessSession)
- [purviewlabelinfo_ProcessSession](#BKMK_purviewlabelinfo_ProcessSession)
- [Queue_ProcessSessions](#BKMK_Queue_ProcessSessions)
- [QueueItem_ProcessSessions](#BKMK_QueueItem_ProcessSessions)
- [recordfilter_ProcessSession](#BKMK_recordfilter_ProcessSession)
- [RecurringAppointmentMaster_ProcessSessions](#BKMK_RecurringAppointmentMaster_ProcessSessions)
- [recyclebinconfig_ProcessSession](#BKMK_recyclebinconfig_ProcessSession)
- [Report_ProcessSessions](#BKMK_Report_ProcessSessions)
- [reportparameter_ProcessSession](#BKMK_reportparameter_ProcessSession)
- [retaineddataexcel_ProcessSession](#BKMK_retaineddataexcel_ProcessSession)
- [retentionconfig_ProcessSession](#BKMK_retentionconfig_ProcessSession)
- [retentionfailuredetail_ProcessSession](#BKMK_retentionfailuredetail_ProcessSession)
- [retentionoperation_ProcessSession](#BKMK_retentionoperation_ProcessSession)
- [retentionoperationdetail_ProcessSession](#BKMK_retentionoperationdetail_ProcessSession)
- [retentionsuccessdetail_ProcessSession](#BKMK_retentionsuccessdetail_ProcessSession)
- [roleeditorlayout_ProcessSession](#BKMK_roleeditorlayout_ProcessSession)
- [rollupfield_ProcessSessions](#BKMK_rollupfield_ProcessSessions)
- [sa_suggestedaction_ProcessSession](#BKMK_sa_suggestedaction_ProcessSession)
- [sa_suggestedactioncriteria_ProcessSession](#BKMK_sa_suggestedactioncriteria_ProcessSession)
- [savingrule_ProcessSession](#BKMK_savingrule_ProcessSession)
- [searchattributesettings_ProcessSession](#BKMK_searchattributesettings_ProcessSession)
- [searchcustomanalyzer_ProcessSession](#BKMK_searchcustomanalyzer_ProcessSession)
- [searchrelationshipsettings_ProcessSession](#BKMK_searchrelationshipsettings_ProcessSession)
- [sensitivitylabelattributemapping_ProcessSession](#BKMK_sensitivitylabelattributemapping_ProcessSession)
- [serviceplan_ProcessSession](#BKMK_serviceplan_ProcessSession)
- [serviceplanmapping_ProcessSession](#BKMK_serviceplanmapping_ProcessSession)
- [sharedlinksetting_ProcessSession](#BKMK_sharedlinksetting_ProcessSession)
- [sharedobject_ProcessSession](#BKMK_sharedobject_ProcessSession)
- [sharedworkspace_ProcessSession](#BKMK_sharedworkspace_ProcessSession)
- [sharedworkspacepool_ProcessSession](#BKMK_sharedworkspacepool_ProcessSession)
- [SharePointDocumentLocation_ProcessSessions](#BKMK_SharePointDocumentLocation_ProcessSessions)
- [sharepointmanagedidentity_ProcessSession](#BKMK_sharepointmanagedidentity_ProcessSession)
- [SharePointSite_ProcessSessions](#BKMK_SharePointSite_ProcessSessions)
- [sideloadedaiplugin_ProcessSession](#BKMK_sideloadedaiplugin_ProcessSession)
- [slabase_ProcessSessions](#BKMK_slabase_ProcessSessions)
- [SocialActivity_ProcessSessions](#BKMK_SocialActivity_ProcessSessions)
- [SocialProfile_ProcessSessions](#BKMK_SocialProfile_ProcessSessions)
- [solutioncomponentattributeconfiguration_ProcessSession](#BKMK_solutioncomponentattributeconfiguration_ProcessSession)
- [solutioncomponentbatchconfiguration_ProcessSession](#BKMK_solutioncomponentbatchconfiguration_ProcessSession)
- [solutioncomponentconfiguration_ProcessSession](#BKMK_solutioncomponentconfiguration_ProcessSession)
- [solutioncomponentrelationshipconfiguration_ProcessSession](#BKMK_solutioncomponentrelationshipconfiguration_ProcessSession)
- [stagedentity_ProcessSession](#BKMK_stagedentity_ProcessSession)
- [stagedentityattribute_ProcessSession](#BKMK_stagedentityattribute_ProcessSession)
- [stagedmetadataasyncoperation_ProcessSession](#BKMK_stagedmetadataasyncoperation_ProcessSession)
- [stagesolutionupload_ProcessSession](#BKMK_stagesolutionupload_ProcessSession)
- [Subject_ProcessSessions](#BKMK_Subject_ProcessSessions)
- [supportusertable_ProcessSession](#BKMK_supportusertable_ProcessSession)
- [synapsedatabase_ProcessSession](#BKMK_synapsedatabase_ProcessSession)
- [synapselinkexternaltablestate_ProcessSession](#BKMK_synapselinkexternaltablestate_ProcessSession)
- [synapselinkprofile_ProcessSession](#BKMK_synapselinkprofile_ProcessSession)
- [synapselinkprofileentity_ProcessSession](#BKMK_synapselinkprofileentity_ProcessSession)
- [synapselinkprofileentitystate_ProcessSession](#BKMK_synapselinkprofileentitystate_ProcessSession)
- [synapselinkschedule_ProcessSession](#BKMK_synapselinkschedule_ProcessSession)
- [SystemUser_ProcessSessions](#BKMK_SystemUser_ProcessSessions)
- [systemuserauthorizationchangetracker_ProcessSession](#BKMK_systemuserauthorizationchangetracker_ProcessSession)
- [tag_ProcessSession](#BKMK_tag_ProcessSession)
- [taggedflowsession_ProcessSession](#BKMK_taggedflowsession_ProcessSession)
- [taggedprocess_ProcessSession](#BKMK_taggedprocess_ProcessSession)
- [Task_ProcessSessions](#BKMK_Task_ProcessSessions)
- [team_processsession](#BKMK_team_processsession)
- [Team_ProcessSessions](#BKMK_Team_ProcessSessions)
- [teammobileofflineprofilemembership_ProcessSession](#BKMK_teammobileofflineprofilemembership_ProcessSession)
- [Template_ProcessSessions](#BKMK_Template_ProcessSessions)
- [Territory_ProcessSessions](#BKMK_Territory_ProcessSessions)
- [theme_ProcessSession](#BKMK_theme_ProcessSession)
- [TransactionCurrency_ProcessSessions](#BKMK_TransactionCurrency_ProcessSessions)
- [TranslationProcess_ProcessSessions](#BKMK_TranslationProcess_ProcessSessions)
- [unstructuredfilesearchentity_ProcessSession](#BKMK_unstructuredfilesearchentity_ProcessSession)
- [unstructuredfilesearchrecord_ProcessSession](#BKMK_unstructuredfilesearchrecord_ProcessSession)
- [usermapping_ProcessSession](#BKMK_usermapping_ProcessSession)
- [usermobileofflineprofilemembership_ProcessSession](#BKMK_usermobileofflineprofilemembership_ProcessSession)
- [userrating_ProcessSession](#BKMK_userrating_ProcessSession)
- [viewasexamplequestion_ProcessSession](#BKMK_viewasexamplequestion_ProcessSession)
- [virtualentitymetadata_ProcessSession](#BKMK_virtualentitymetadata_ProcessSession)
- [workflowbinary_ProcessSession](#BKMK_workflowbinary_ProcessSession)
- [workflowmetadata_ProcessSession](#BKMK_workflowmetadata_ProcessSession)
- [workqueue_ProcessSession](#BKMK_workqueue_ProcessSession)
- [workqueueitem_ProcessSession](#BKMK_workqueueitem_ProcessSession)

### <a name="BKMK_Account_ProcessSessions"></a> Account_ProcessSessions

One-To-Many Relationship: [account Account_ProcessSessions](account.md#BKMK_Account_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_account`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_activityfileattachment_ProcessSession"></a> activityfileattachment_ProcessSession

One-To-Many Relationship: [activityfileattachment activityfileattachment_ProcessSession](activityfileattachment.md#BKMK_activityfileattachment_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`activityfileattachment`|
|ReferencedAttribute|`activityfileattachmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_activityfileattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_externalidentity_ProcessSession"></a> adx_externalidentity_ProcessSession

One-To-Many Relationship: [adx_externalidentity adx_externalidentity_ProcessSession](adx_externalidentity.md#BKMK_adx_externalidentity_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_externalidentity`|
|ReferencedAttribute|`adx_externalidentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_externalidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_invitation_ProcessSession"></a> adx_invitation_ProcessSession

One-To-Many Relationship: [adx_invitation adx_invitation_ProcessSession](adx_invitation.md#BKMK_adx_invitation_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_invitation`|
|ReferencedAttribute|`adx_invitationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_invitation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_inviteredemption_ProcessSession"></a> adx_inviteredemption_ProcessSession

One-To-Many Relationship: [adx_inviteredemption adx_inviteredemption_ProcessSession](adx_inviteredemption.md#BKMK_adx_inviteredemption_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_inviteredemption`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_inviteredemption`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_portalcomment_ProcessSession"></a> adx_portalcomment_ProcessSession

One-To-Many Relationship: [adx_portalcomment adx_portalcomment_ProcessSession](adx_portalcomment.md#BKMK_adx_portalcomment_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_portalcomment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_portalcomment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_setting_ProcessSession"></a> adx_setting_ProcessSession

One-To-Many Relationship: [adx_setting adx_setting_ProcessSession](adx_setting.md#BKMK_adx_setting_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_setting`|
|ReferencedAttribute|`adx_settingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_setting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_webformsession_ProcessSession"></a> adx_webformsession_ProcessSession

One-To-Many Relationship: [adx_webformsession adx_webformsession_ProcessSession](adx_webformsession.md#BKMK_adx_webformsession_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_webformsession`|
|ReferencedAttribute|`adx_webformsessionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_webformsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aicopilot_ProcessSession"></a> aicopilot_ProcessSession

One-To-Many Relationship: [aicopilot aicopilot_ProcessSession](aicopilot.md#BKMK_aicopilot_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`aicopilot`|
|ReferencedAttribute|`aicopilotid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aicopilot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugin_ProcessSession"></a> aiplugin_ProcessSession

One-To-Many Relationship: [aiplugin aiplugin_ProcessSession](aiplugin.md#BKMK_aiplugin_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugin`|
|ReferencedAttribute|`aipluginid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugin`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginauth_ProcessSession"></a> aipluginauth_ProcessSession

One-To-Many Relationship: [aipluginauth aipluginauth_ProcessSession](aipluginauth.md#BKMK_aipluginauth_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginauth`|
|ReferencedAttribute|`aipluginauthid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginauth`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginconversationstarter_ProcessSession"></a> aipluginconversationstarter_ProcessSession

One-To-Many Relationship: [aipluginconversationstarter aipluginconversationstarter_ProcessSession](aipluginconversationstarter.md#BKMK_aipluginconversationstarter_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginconversationstarter`|
|ReferencedAttribute|`aipluginconversationstarterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginconversationstarter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginconversationstartermapping_ProcessSession"></a> aipluginconversationstartermapping_ProcessSession

One-To-Many Relationship: [aipluginconversationstartermapping aipluginconversationstartermapping_ProcessSession](aipluginconversationstartermapping.md#BKMK_aipluginconversationstartermapping_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginconversationstartermapping`|
|ReferencedAttribute|`aipluginconversationstartermappingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginconversationstartermapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginexternalschema_ProcessSession"></a> aipluginexternalschema_ProcessSession

One-To-Many Relationship: [aipluginexternalschema aipluginexternalschema_ProcessSession](aipluginexternalschema.md#BKMK_aipluginexternalschema_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginexternalschema`|
|ReferencedAttribute|`aipluginexternalschemaid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginexternalschema`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginexternalschemaproperty_ProcessSession"></a> aipluginexternalschemaproperty_ProcessSession

One-To-Many Relationship: [aipluginexternalschemaproperty aipluginexternalschemaproperty_ProcessSession](aipluginexternalschemaproperty.md#BKMK_aipluginexternalschemaproperty_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginexternalschemaproperty`|
|ReferencedAttribute|`aipluginexternalschemapropertyid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginexternalschemaproperty`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugingovernance_ProcessSession"></a> aiplugingovernance_ProcessSession

One-To-Many Relationship: [aiplugingovernance aiplugingovernance_ProcessSession](aiplugingovernance.md#BKMK_aiplugingovernance_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugingovernance`|
|ReferencedAttribute|`aiplugingovernanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugingovernance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugingovernanceext_ProcessSession"></a> aiplugingovernanceext_ProcessSession

One-To-Many Relationship: [aiplugingovernanceext aiplugingovernanceext_ProcessSession](aiplugingovernanceext.md#BKMK_aiplugingovernanceext_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugingovernanceext`|
|ReferencedAttribute|`aiplugingovernanceextid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugingovernanceext`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugininstance_ProcessSession"></a> aiplugininstance_ProcessSession

One-To-Many Relationship: [aiplugininstance aiplugininstance_ProcessSession](aiplugininstance.md#BKMK_aiplugininstance_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugininstance`|
|ReferencedAttribute|`aiplugininstanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugininstance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperation_ProcessSession"></a> aipluginoperation_ProcessSession

One-To-Many Relationship: [aipluginoperation aipluginoperation_ProcessSession](aipluginoperation.md#BKMK_aipluginoperation_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperation`|
|ReferencedAttribute|`aipluginoperationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperationparameter_ProcessSession"></a> aipluginoperationparameter_ProcessSession

One-To-Many Relationship: [aipluginoperationparameter aipluginoperationparameter_ProcessSession](aipluginoperationparameter.md#BKMK_aipluginoperationparameter_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperationparameter`|
|ReferencedAttribute|`aipluginoperationparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginoperationparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperationresponsetemplate_ProcessSession"></a> aipluginoperationresponsetemplate_ProcessSession

One-To-Many Relationship: [aipluginoperationresponsetemplate aipluginoperationresponsetemplate_ProcessSession](aipluginoperationresponsetemplate.md#BKMK_aipluginoperationresponsetemplate_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperationresponsetemplate`|
|ReferencedAttribute|`aipluginoperationresponsetemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginoperationresponsetemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugintitle_ProcessSession"></a> aiplugintitle_ProcessSession

One-To-Many Relationship: [aiplugintitle aiplugintitle_ProcessSession](aiplugintitle.md#BKMK_aiplugintitle_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugintitle`|
|ReferencedAttribute|`aiplugintitleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugintitle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginusersetting_ProcessSession"></a> aipluginusersetting_ProcessSession

One-To-Many Relationship: [aipluginusersetting aipluginusersetting_ProcessSession](aipluginusersetting.md#BKMK_aipluginusersetting_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginusersetting`|
|ReferencedAttribute|`aipluginusersettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginusersetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_allowedmcpclient_ProcessSession"></a> allowedmcpclient_ProcessSession

One-To-Many Relationship: [allowedmcpclient allowedmcpclient_ProcessSession](allowedmcpclient.md#BKMK_allowedmcpclient_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`allowedmcpclient`|
|ReferencedAttribute|`allowedmcpclientid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_allowedmcpclient`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Annotation_ProcessSessions"></a> Annotation_ProcessSessions

One-To-Many Relationship: [annotation Annotation_ProcessSessions](annotation.md#BKMK_Annotation_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`annotation`|
|ReferencedAttribute|`annotationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_annotation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appaction_ProcessSession"></a> appaction_ProcessSession

One-To-Many Relationship: [appaction appaction_ProcessSession](appaction.md#BKMK_appaction_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`appaction`|
|ReferencedAttribute|`appactionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_appaction`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appactionmigration_ProcessSession"></a> appactionmigration_ProcessSession

One-To-Many Relationship: [appactionmigration appactionmigration_ProcessSession](appactionmigration.md#BKMK_appactionmigration_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`appactionmigration`|
|ReferencedAttribute|`appactionmigrationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_appactionmigration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appactionrule_ProcessSession"></a> appactionrule_ProcessSession

One-To-Many Relationship: [appactionrule appactionrule_ProcessSession](appactionrule.md#BKMK_appactionrule_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`appactionrule`|
|ReferencedAttribute|`appactionruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_appactionrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_application_ProcessSession"></a> application_ProcessSession

One-To-Many Relationship: [application application_ProcessSession](application.md#BKMK_application_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`application`|
|ReferencedAttribute|`applicationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_application`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_applicationuser_ProcessSession"></a> applicationuser_ProcessSession

One-To-Many Relationship: [applicationuser applicationuser_ProcessSession](applicationuser.md#BKMK_applicationuser_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`applicationuser`|
|ReferencedAttribute|`applicationuserid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_applicationuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Appointment_ProcessSessions"></a> Appointment_ProcessSessions

One-To-Many Relationship: [appointment Appointment_ProcessSessions](appointment.md#BKMK_Appointment_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`appointment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalprocess_ProcessSession"></a> approvalprocess_ProcessSession

One-To-Many Relationship: [approvalprocess approvalprocess_ProcessSession](approvalprocess.md#BKMK_approvalprocess_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalprocess`|
|ReferencedAttribute|`approvalprocessid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageapproval_ProcessSession"></a> approvalstageapproval_ProcessSession

One-To-Many Relationship: [approvalstageapproval approvalstageapproval_ProcessSession](approvalstageapproval.md#BKMK_approvalstageapproval_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageapproval`|
|ReferencedAttribute|`approvalstageapprovalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalstageapproval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstagecondition_ProcessSession"></a> approvalstagecondition_ProcessSession

One-To-Many Relationship: [approvalstagecondition approvalstagecondition_ProcessSession](approvalstagecondition.md#BKMK_approvalstagecondition_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstagecondition`|
|ReferencedAttribute|`approvalstageconditionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalstagecondition`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageintelligent_ProcessSession"></a> approvalstageintelligent_ProcessSession

One-To-Many Relationship: [approvalstageintelligent approvalstageintelligent_ProcessSession](approvalstageintelligent.md#BKMK_approvalstageintelligent_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageintelligent`|
|ReferencedAttribute|`approvalstageintelligentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalstageintelligent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageorder_ProcessSession"></a> approvalstageorder_ProcessSession

One-To-Many Relationship: [approvalstageorder approvalstageorder_ProcessSession](approvalstageorder.md#BKMK_approvalstageorder_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageorder`|
|ReferencedAttribute|`approvalstageorderid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalstageorder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_attributeclusterconfig_ProcessSession"></a> attributeclusterconfig_ProcessSession

One-To-Many Relationship: [attributeclusterconfig attributeclusterconfig_ProcessSession](attributeclusterconfig.md#BKMK_attributeclusterconfig_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`attributeclusterconfig`|
|ReferencedAttribute|`attributeclusterconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_attributeclusterconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_attributemaskingrule_ProcessSession"></a> attributemaskingrule_ProcessSession

One-To-Many Relationship: [attributemaskingrule attributemaskingrule_ProcessSession](attributemaskingrule.md#BKMK_attributemaskingrule_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`attributemaskingrule`|
|ReferencedAttribute|`attributemaskingruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_attributemaskingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_bot_ProcessSession"></a> bot_ProcessSession

One-To-Many Relationship: [bot bot_ProcessSession](bot.md#BKMK_bot_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`bot`|
|ReferencedAttribute|`botid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_bot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_botcomponent_ProcessSession"></a> botcomponent_ProcessSession

One-To-Many Relationship: [botcomponent botcomponent_ProcessSession](botcomponent.md#BKMK_botcomponent_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`botcomponent`|
|ReferencedAttribute|`botcomponentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_botcomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_botcomponentcollection_ProcessSession"></a> botcomponentcollection_ProcessSession

One-To-Many Relationship: [botcomponentcollection botcomponentcollection_ProcessSession](botcomponentcollection.md#BKMK_botcomponentcollection_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`botcomponentcollection`|
|ReferencedAttribute|`botcomponentcollectionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_botcomponentcollection`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_businessprocess_ProcessSession"></a> businessprocess_ProcessSession

One-To-Many Relationship: [businessprocess businessprocess_ProcessSession](businessprocess.md#BKMK_businessprocess_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`businessprocess`|
|ReferencedAttribute|`businessprocessid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_businessprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_BusinessUnit_ProcessSessions"></a> BusinessUnit_ProcessSessions

One-To-Many Relationship: [businessunit BusinessUnit_ProcessSessions](businessunit.md#BKMK_BusinessUnit_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_businessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_BusinessUnitNewsArticle_ProcessSessions"></a> BusinessUnitNewsArticle_ProcessSessions

One-To-Many Relationship: [businessunitnewsarticle BusinessUnitNewsArticle_ProcessSessions](businessunitnewsarticle.md#BKMK_BusinessUnitNewsArticle_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunitnewsarticle`|
|ReferencedAttribute|`businessunitnewsarticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_businessunitnewsarticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_card_ProcessSession"></a> card_ProcessSession

One-To-Many Relationship: [card card_ProcessSession](card.md#BKMK_card_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`card`|
|ReferencedAttribute|`cardid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_card`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_catalog_ProcessSession"></a> catalog_ProcessSession

One-To-Many Relationship: [catalog catalog_ProcessSession](catalog.md#BKMK_catalog_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`catalog`|
|ReferencedAttribute|`catalogid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_catalog`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_catalogassignment_ProcessSession"></a> catalogassignment_ProcessSession

One-To-Many Relationship: [catalogassignment catalogassignment_ProcessSession](catalogassignment.md#BKMK_catalogassignment_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`catalogassignment`|
|ReferencedAttribute|`catalogassignmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_catalogassignment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_certificatecredential_ProcessSession"></a> certificatecredential_ProcessSession

One-To-Many Relationship: [certificatecredential certificatecredential_ProcessSession](certificatecredential.md#BKMK_certificatecredential_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`certificatecredential`|
|ReferencedAttribute|`certificatecredentialid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_certificatecredential`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_chat_ProcessSession"></a> chat_ProcessSession

One-To-Many Relationship: [chat chat_ProcessSession](chat.md#BKMK_chat_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`chat`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_chat`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Connection_ProcessSessions"></a> Connection_ProcessSessions

One-To-Many Relationship: [connection Connection_ProcessSessions](connection.md#BKMK_Connection_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`connection`|
|ReferencedAttribute|`connectionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_connection`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connectioninstance_ProcessSession"></a> connectioninstance_ProcessSession

One-To-Many Relationship: [connectioninstance connectioninstance_ProcessSession](connectioninstance.md#BKMK_connectioninstance_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`connectioninstance`|
|ReferencedAttribute|`connectioninstanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_connectioninstance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connectionreference_ProcessSession"></a> connectionreference_ProcessSession

One-To-Many Relationship: [connectionreference connectionreference_ProcessSession](connectionreference.md#BKMK_connectionreference_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`connectionreference`|
|ReferencedAttribute|`connectionreferenceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_connectionreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ConnectionRole_ProcessSessions"></a> ConnectionRole_ProcessSessions

One-To-Many Relationship: [connectionrole ConnectionRole_ProcessSessions](connectionrole.md#BKMK_ConnectionRole_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`connectionrole`|
|ReferencedAttribute|`connectionroleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_connectionrole`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connector_ProcessSession"></a> connector_ProcessSession

One-To-Many Relationship: [connector connector_ProcessSession](connector.md#BKMK_connector_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`connector`|
|ReferencedAttribute|`connectorid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_connector`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Contact_ProcessSessions"></a> Contact_ProcessSessions

One-To-Many Relationship: [contact Contact_ProcessSessions](contact.md#BKMK_Contact_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_contact`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_conversationtranscript_ProcessSession"></a> conversationtranscript_ProcessSession

One-To-Many Relationship: [conversationtranscript conversationtranscript_ProcessSession](conversationtranscript.md#BKMK_conversationtranscript_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`conversationtranscript`|
|ReferencedAttribute|`conversationtranscriptid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_conversationtranscript`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_copilotexamplequestion_ProcessSession"></a> copilotexamplequestion_ProcessSession

One-To-Many Relationship: [copilotexamplequestion copilotexamplequestion_ProcessSession](copilotexamplequestion.md#BKMK_copilotexamplequestion_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`copilotexamplequestion`|
|ReferencedAttribute|`copilotexamplequestionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_copilotexamplequestion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_copilotglossaryterm_ProcessSession"></a> copilotglossaryterm_ProcessSession

One-To-Many Relationship: [copilotglossaryterm copilotglossaryterm_ProcessSession](copilotglossaryterm.md#BKMK_copilotglossaryterm_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`copilotglossaryterm`|
|ReferencedAttribute|`copilotglossarytermid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_copilotglossaryterm`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_copilotsynonyms_ProcessSession"></a> copilotsynonyms_ProcessSession

One-To-Many Relationship: [copilotsynonyms copilotsynonyms_ProcessSession](copilotsynonyms.md#BKMK_copilotsynonyms_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`copilotsynonyms`|
|ReferencedAttribute|`copilotsynonymsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_copilotsynonyms`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_credential_ProcessSession"></a> credential_ProcessSession

One-To-Many Relationship: [credential credential_ProcessSession](credential.md#BKMK_credential_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`credential`|
|ReferencedAttribute|`credentialid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_credential`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_customapi_ProcessSession"></a> customapi_ProcessSession

One-To-Many Relationship: [customapi customapi_ProcessSession](customapi.md#BKMK_customapi_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`customapi`|
|ReferencedAttribute|`customapiid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_customapi`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_customapirequestparameter_ProcessSession"></a> customapirequestparameter_ProcessSession

One-To-Many Relationship: [customapirequestparameter customapirequestparameter_ProcessSession](customapirequestparameter.md#BKMK_customapirequestparameter_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`customapirequestparameter`|
|ReferencedAttribute|`customapirequestparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_customapirequestparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_customapiresponseproperty_ProcessSession"></a> customapiresponseproperty_ProcessSession

One-To-Many Relationship: [customapiresponseproperty customapiresponseproperty_ProcessSession](customapiresponseproperty.md#BKMK_customapiresponseproperty_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`customapiresponseproperty`|
|ReferencedAttribute|`customapiresponsepropertyid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_customapiresponseproperty`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_CustomerAddress_ProcessSessions"></a> CustomerAddress_ProcessSessions

One-To-Many Relationship: [customeraddress CustomerAddress_ProcessSessions](customeraddress.md#BKMK_CustomerAddress_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`customeraddress`|
|ReferencedAttribute|`customeraddressid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_customeraddress`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakefolder_ProcessSession"></a> datalakefolder_ProcessSession

One-To-Many Relationship: [datalakefolder datalakefolder_ProcessSession](datalakefolder.md#BKMK_datalakefolder_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakefolder`|
|ReferencedAttribute|`datalakefolderid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_datalakefolder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakefolderpermission_ProcessSession"></a> datalakefolderpermission_ProcessSession

One-To-Many Relationship: [datalakefolderpermission datalakefolderpermission_ProcessSession](datalakefolderpermission.md#BKMK_datalakefolderpermission_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakefolderpermission`|
|ReferencedAttribute|`datalakefolderpermissionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_datalakefolderpermission`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakeworkspace_ProcessSession"></a> datalakeworkspace_ProcessSession

One-To-Many Relationship: [datalakeworkspace datalakeworkspace_ProcessSession](datalakeworkspace.md#BKMK_datalakeworkspace_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakeworkspace`|
|ReferencedAttribute|`datalakeworkspaceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_datalakeworkspace`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakeworkspacepermission_ProcessSession"></a> datalakeworkspacepermission_ProcessSession

One-To-Many Relationship: [datalakeworkspacepermission datalakeworkspacepermission_ProcessSession](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakeworkspacepermission`|
|ReferencedAttribute|`datalakeworkspacepermissionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_datalakeworkspacepermission`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dataprocessingconfiguration_ProcessSession"></a> dataprocessingconfiguration_ProcessSession

One-To-Many Relationship: [dataprocessingconfiguration dataprocessingconfiguration_ProcessSession](dataprocessingconfiguration.md#BKMK_dataprocessingconfiguration_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`dataprocessingconfiguration`|
|ReferencedAttribute|`dataprocessingconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dataprocessingconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_delegatedauthorization_ProcessSession"></a> delegatedauthorization_ProcessSession

One-To-Many Relationship: [delegatedauthorization delegatedauthorization_ProcessSession](delegatedauthorization.md#BKMK_delegatedauthorization_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`delegatedauthorization`|
|ReferencedAttribute|`delegatedauthorizationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_delegatedauthorization`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_desktopflowbinary_ProcessSession"></a> desktopflowbinary_ProcessSession

One-To-Many Relationship: [desktopflowbinary desktopflowbinary_ProcessSession](desktopflowbinary.md#BKMK_desktopflowbinary_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`desktopflowbinary`|
|ReferencedAttribute|`desktopflowbinaryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_desktopflowbinary`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_desktopflowmodule_ProcessSession"></a> desktopflowmodule_ProcessSession

One-To-Many Relationship: [desktopflowmodule desktopflowmodule_ProcessSession](desktopflowmodule.md#BKMK_desktopflowmodule_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`desktopflowmodule`|
|ReferencedAttribute|`desktopflowmoduleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_desktopflowmodule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvfilesearch_ProcessSession"></a> dvfilesearch_ProcessSession

One-To-Many Relationship: [dvfilesearch dvfilesearch_ProcessSession](dvfilesearch.md#BKMK_dvfilesearch_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`dvfilesearch`|
|ReferencedAttribute|`dvfilesearchid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvfilesearch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvfilesearchattribute_ProcessSession"></a> dvfilesearchattribute_ProcessSession

One-To-Many Relationship: [dvfilesearchattribute dvfilesearchattribute_ProcessSession](dvfilesearchattribute.md#BKMK_dvfilesearchattribute_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`dvfilesearchattribute`|
|ReferencedAttribute|`dvfilesearchattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvfilesearchattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvfilesearchentity_ProcessSession"></a> dvfilesearchentity_ProcessSession

One-To-Many Relationship: [dvfilesearchentity dvfilesearchentity_ProcessSession](dvfilesearchentity.md#BKMK_dvfilesearchentity_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`dvfilesearchentity`|
|ReferencedAttribute|`dvfilesearchentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvfilesearchentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvtablesearch_ProcessSession"></a> dvtablesearch_ProcessSession

One-To-Many Relationship: [dvtablesearch dvtablesearch_ProcessSession](dvtablesearch.md#BKMK_dvtablesearch_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`dvtablesearch`|
|ReferencedAttribute|`dvtablesearchid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvtablesearch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvtablesearchattribute_ProcessSession"></a> dvtablesearchattribute_ProcessSession

One-To-Many Relationship: [dvtablesearchattribute dvtablesearchattribute_ProcessSession](dvtablesearchattribute.md#BKMK_dvtablesearchattribute_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`dvtablesearchattribute`|
|ReferencedAttribute|`dvtablesearchattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvtablesearchattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvtablesearchentity_ProcessSession"></a> dvtablesearchentity_ProcessSession

One-To-Many Relationship: [dvtablesearchentity dvtablesearchentity_ProcessSession](dvtablesearchentity.md#BKMK_dvtablesearchentity_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`dvtablesearchentity`|
|ReferencedAttribute|`dvtablesearchentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvtablesearchentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Email_ProcessSessions"></a> Email_ProcessSessions

One-To-Many Relationship: [email Email_ProcessSessions](email.md#BKMK_Email_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`email`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityclusterconfig_ProcessSession"></a> entityclusterconfig_ProcessSession

One-To-Many Relationship: [entityclusterconfig entityclusterconfig_ProcessSession](entityclusterconfig.md#BKMK_entityclusterconfig_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`entityclusterconfig`|
|ReferencedAttribute|`entityclusterconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityclusterconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityrecordfilter_ProcessSession"></a> entityrecordfilter_ProcessSession

One-To-Many Relationship: [entityrecordfilter entityrecordfilter_ProcessSession](entityrecordfilter.md#BKMK_entityrecordfilter_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`entityrecordfilter`|
|ReferencedAttribute|`entityrecordfilterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityrecordfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariabledefinition_ProcessSession"></a> environmentvariabledefinition_ProcessSession

One-To-Many Relationship: [environmentvariabledefinition environmentvariabledefinition_ProcessSession](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariabledefinition`|
|ReferencedAttribute|`environmentvariabledefinitionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_environmentvariabledefinition`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariablevalue_ProcessSession"></a> environmentvariablevalue_ProcessSession

One-To-Many Relationship: [environmentvariablevalue environmentvariablevalue_ProcessSession](environmentvariablevalue.md#BKMK_environmentvariablevalue_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariablevalue`|
|ReferencedAttribute|`environmentvariablevalueid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_environmentvariablevalue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ExpiredProcess_ProcessSessions"></a> ExpiredProcess_ProcessSessions

One-To-Many Relationship: [expiredprocess ExpiredProcess_ProcessSessions](expiredprocess.md#BKMK_ExpiredProcess_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`expiredprocess`|
|ReferencedAttribute|`businessprocessflowinstanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_expiredprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_exportedexcel_ProcessSession"></a> exportedexcel_ProcessSession

One-To-Many Relationship: [exportedexcel exportedexcel_ProcessSession](exportedexcel.md#BKMK_exportedexcel_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`exportedexcel`|
|ReferencedAttribute|`exportedexcelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_exportedexcel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_exportsolutionupload_ProcessSession"></a> exportsolutionupload_ProcessSession

One-To-Many Relationship: [exportsolutionupload exportsolutionupload_ProcessSession](exportsolutionupload.md#BKMK_exportsolutionupload_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`exportsolutionupload`|
|ReferencedAttribute|`exportsolutionuploadid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_exportsolutionupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fabricaiskill_ProcessSession"></a> fabricaiskill_ProcessSession

One-To-Many Relationship: [fabricaiskill fabricaiskill_ProcessSession](fabricaiskill.md#BKMK_fabricaiskill_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`fabricaiskill`|
|ReferencedAttribute|`fabricaiskillid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_fabricaiskill`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Fax_ProcessSessions"></a> Fax_ProcessSessions

One-To-Many Relationship: [fax Fax_ProcessSessions](fax.md#BKMK_Fax_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`fax`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_fax`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_featurecontrolsetting_ProcessSession"></a> featurecontrolsetting_ProcessSession

One-To-Many Relationship: [featurecontrolsetting featurecontrolsetting_ProcessSession](featurecontrolsetting.md#BKMK_featurecontrolsetting_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`featurecontrolsetting`|
|ReferencedAttribute|`featurecontrolsettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_featurecontrolsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_federatedknowledgeconfiguration_ProcessSession"></a> federatedknowledgeconfiguration_ProcessSession

One-To-Many Relationship: [federatedknowledgeconfiguration federatedknowledgeconfiguration_ProcessSession](federatedknowledgeconfiguration.md#BKMK_federatedknowledgeconfiguration_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`federatedknowledgeconfiguration`|
|ReferencedAttribute|`federatedknowledgeconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_federatedknowledgeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_federatedknowledgeentityconfiguration_ProcessSession"></a> federatedknowledgeentityconfiguration_ProcessSession

One-To-Many Relationship: [federatedknowledgeentityconfiguration federatedknowledgeentityconfiguration_ProcessSession](federatedknowledgeentityconfiguration.md#BKMK_federatedknowledgeentityconfiguration_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`federatedknowledgeentityconfiguration`|
|ReferencedAttribute|`federatedknowledgeentityconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_federatedknowledgeentityconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowcapacityassignment_ProcessSession"></a> flowcapacityassignment_ProcessSession

One-To-Many Relationship: [flowcapacityassignment flowcapacityassignment_ProcessSession](flowcapacityassignment.md#BKMK_flowcapacityassignment_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`flowcapacityassignment`|
|ReferencedAttribute|`flowcapacityassignmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowcapacityassignment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowcredentialapplication_ProcessSession"></a> flowcredentialapplication_ProcessSession

One-To-Many Relationship: [flowcredentialapplication flowcredentialapplication_ProcessSession](flowcredentialapplication.md#BKMK_flowcredentialapplication_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`flowcredentialapplication`|
|ReferencedAttribute|`flowcredentialapplicationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowcredentialapplication`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowevent_ProcessSession"></a> flowevent_ProcessSession

One-To-Many Relationship: [flowevent flowevent_ProcessSession](flowevent.md#BKMK_flowevent_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`flowevent`|
|ReferencedAttribute|`floweventid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowevent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachine_ProcessSession"></a> flowmachine_ProcessSession

One-To-Many Relationship: [flowmachine flowmachine_ProcessSession](flowmachine.md#BKMK_flowmachine_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachine`|
|ReferencedAttribute|`flowmachineid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachine`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinegroup_ProcessSession"></a> flowmachinegroup_ProcessSession

One-To-Many Relationship: [flowmachinegroup flowmachinegroup_ProcessSession](flowmachinegroup.md#BKMK_flowmachinegroup_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinegroup`|
|ReferencedAttribute|`flowmachinegroupid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachinegroup`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachineimage_ProcessSession"></a> flowmachineimage_ProcessSession

One-To-Many Relationship: [flowmachineimage flowmachineimage_ProcessSession](flowmachineimage.md#BKMK_flowmachineimage_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachineimage`|
|ReferencedAttribute|`flowmachineimageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachineimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachineimageversion_ProcessSession"></a> flowmachineimageversion_ProcessSession

One-To-Many Relationship: [flowmachineimageversion flowmachineimageversion_ProcessSession](flowmachineimageversion.md#BKMK_flowmachineimageversion_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachineimageversion`|
|ReferencedAttribute|`flowmachineimageversionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachineimageversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinenetwork_ProcessSession"></a> flowmachinenetwork_ProcessSession

One-To-Many Relationship: [flowmachinenetwork flowmachinenetwork_ProcessSession](flowmachinenetwork.md#BKMK_flowmachinenetwork_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinenetwork`|
|ReferencedAttribute|`flowmachinenetworkid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachinenetwork`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowsessionbinary_ProcessSession"></a> flowsessionbinary_ProcessSession

One-To-Many Relationship: [flowsessionbinary flowsessionbinary_ProcessSession](flowsessionbinary.md#BKMK_flowsessionbinary_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`flowsessionbinary`|
|ReferencedAttribute|`flowsessionbinaryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowsessionbinary`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fxexpression_ProcessSession"></a> fxexpression_ProcessSession

One-To-Many Relationship: [fxexpression fxexpression_ProcessSession](fxexpression.md#BKMK_fxexpression_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`fxexpression`|
|ReferencedAttribute|`fxexpressionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_fxexpression`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Goal_ProcessSessions"></a> Goal_ProcessSessions

One-To-Many Relationship: [goal Goal_ProcessSessions](goal.md#BKMK_Goal_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`goal`|
|ReferencedAttribute|`goalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_goal`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_goalrollupquery_ProcessSessions"></a> goalrollupquery_ProcessSessions

One-To-Many Relationship: [goalrollupquery goalrollupquery_ProcessSessions](goalrollupquery.md#BKMK_goalrollupquery_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`goalrollupquery`|
|ReferencedAttribute|`goalrollupqueryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_goalrollupquery`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_governanceconfiguration_ProcessSession"></a> governanceconfiguration_ProcessSession

One-To-Many Relationship: [governanceconfiguration governanceconfiguration_ProcessSession](governanceconfiguration.md#BKMK_governanceconfiguration_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`governanceconfiguration`|
|ReferencedAttribute|`governanceconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_governanceconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KbArticle_ProcessSessions"></a> KbArticle_ProcessSessions

One-To-Many Relationship: [kbarticle KbArticle_ProcessSessions](kbarticle.md#BKMK_KbArticle_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`kbarticle`|
|ReferencedAttribute|`kbarticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_kbarticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KbArticleComment_ProcessSessions"></a> KbArticleComment_ProcessSessions

One-To-Many Relationship: [kbarticlecomment KbArticleComment_ProcessSessions](kbarticlecomment.md#BKMK_KbArticleComment_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`kbarticlecomment`|
|ReferencedAttribute|`kbarticlecommentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_kbarticlecomment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KbArticleTemplate_ProcessSessions"></a> KbArticleTemplate_ProcessSessions

One-To-Many Relationship: [kbarticletemplate KbArticleTemplate_ProcessSessions](kbarticletemplate.md#BKMK_KbArticleTemplate_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`kbarticletemplate`|
|ReferencedAttribute|`kbarticletemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_kbarticletemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_keyvaultreference_ProcessSession"></a> keyvaultreference_ProcessSession

One-To-Many Relationship: [keyvaultreference keyvaultreference_ProcessSession](keyvaultreference.md#BKMK_keyvaultreference_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`keyvaultreference`|
|ReferencedAttribute|`keyvaultreferenceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_keyvaultreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgearticle_ProcessSession"></a> knowledgearticle_ProcessSession

One-To-Many Relationship: [knowledgearticle knowledgearticle_ProcessSession](knowledgearticle.md#BKMK_knowledgearticle_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KnowledgeBaseRecord_ProcessSession"></a> KnowledgeBaseRecord_ProcessSession

One-To-Many Relationship: [knowledgebaserecord KnowledgeBaseRecord_ProcessSession](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgebaserecord`|
|ReferencedAttribute|`knowledgebaserecordid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgebaserecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgefaq_ProcessSession"></a> knowledgefaq_ProcessSession

One-To-Many Relationship: [knowledgefaq knowledgefaq_ProcessSession](knowledgefaq.md#BKMK_knowledgefaq_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgefaq`|
|ReferencedAttribute|`knowledgefaqid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgefaq`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Letter_ProcessSessions"></a> Letter_ProcessSessions

One-To-Many Relationship: [letter Letter_ProcessSessions](letter.md#BKMK_Letter_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`letter`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_letter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_processsession_canceledby"></a> lk_processsession_canceledby

One-To-Many Relationship: [systemuser lk_processsession_canceledby](systemuser.md#BKMK_lk_processsession_canceledby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`canceledby`|
|ReferencingEntityNavigationPropertyName|`canceledby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_processsession_completedby"></a> lk_processsession_completedby

One-To-Many Relationship: [systemuser lk_processsession_completedby](systemuser.md#BKMK_lk_processsession_completedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`completedby`|
|ReferencingEntityNavigationPropertyName|`completedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_processsession_createdby"></a> lk_processsession_createdby

One-To-Many Relationship: [systemuser lk_processsession_createdby](systemuser.md#BKMK_lk_processsession_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_processsession_executedby"></a> lk_processsession_executedby

One-To-Many Relationship: [systemuser lk_processsession_executedby](systemuser.md#BKMK_lk_processsession_executedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`executedby`|
|ReferencingEntityNavigationPropertyName|`executedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_processsession_modifiedby"></a> lk_processsession_modifiedby

One-To-Many Relationship: [systemuser lk_processsession_modifiedby](systemuser.md#BKMK_lk_processsession_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_processsession_nextlinkedsessionid-many-to-one"></a> lk_processsession_nextlinkedsessionid

One-To-Many Relationship: [processsession lk_processsession_nextlinkedsessionid](#BKMK_lk_processsession_nextlinkedsessionid-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`processsession`|
|ReferencedAttribute|`processsessionid`|
|ReferencingAttribute|`nextlinkedsessionid`|
|ReferencingEntityNavigationPropertyName|`nextlinkedsessionid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_processsession_originatingsessionid-many-to-one"></a> lk_processsession_originatingsessionid

One-To-Many Relationship: [processsession lk_processsession_originatingsessionid](#BKMK_lk_processsession_originatingsessionid-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`processsession`|
|ReferencedAttribute|`processsessionid`|
|ReferencingAttribute|`originatingsessionid`|
|ReferencingEntityNavigationPropertyName|`originatingsessionid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_processsession_previouslinkedsessionid-many-to-one"></a> lk_processsession_previouslinkedsessionid

One-To-Many Relationship: [processsession lk_processsession_previouslinkedsessionid](#BKMK_lk_processsession_previouslinkedsessionid-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`processsession`|
|ReferencedAttribute|`processsessionid`|
|ReferencingAttribute|`previouslinkedsessionid`|
|ReferencingEntityNavigationPropertyName|`previouslinkedsessionid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_processsession_processid"></a> lk_processsession_processid

One-To-Many Relationship: [workflow lk_processsession_processid](workflow.md#BKMK_lk_processsession_processid)

|Property|Value|
|---|---|
|ReferencedEntity|`workflow`|
|ReferencedAttribute|`workflowid`|
|ReferencingAttribute|`processid`|
|ReferencingEntityNavigationPropertyName|`processid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_processsession_startedby"></a> lk_processsession_startedby

One-To-Many Relationship: [systemuser lk_processsession_startedby](systemuser.md#BKMK_lk_processsession_startedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`startedby`|
|ReferencingEntityNavigationPropertyName|`startedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_processsessionbase_createdonbehalfby"></a> lk_processsessionbase_createdonbehalfby

One-To-Many Relationship: [systemuser lk_processsessionbase_createdonbehalfby](systemuser.md#BKMK_lk_processsessionbase_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_processsessionbase_modifiedonbehalfby"></a> lk_processsessionbase_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_processsessionbase_modifiedonbehalfby](systemuser.md#BKMK_lk_processsessionbase_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mailbox_processsessions"></a> mailbox_processsessions

One-To-Many Relationship: [mailbox mailbox_processsessions](mailbox.md#BKMK_mailbox_processsessions)

|Property|Value|
|---|---|
|ReferencedEntity|`mailbox`|
|ReferencedAttribute|`mailboxid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mailbox`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_MailMergeTemplate_ProcessSessions"></a> MailMergeTemplate_ProcessSessions

One-To-Many Relationship: [mailmergetemplate MailMergeTemplate_ProcessSessions](mailmergetemplate.md#BKMK_MailMergeTemplate_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`mailmergetemplate`|
|ReferencedAttribute|`mailmergetemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mailmergetemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mainfewshot_ProcessSession"></a> mainfewshot_ProcessSession

One-To-Many Relationship: [mainfewshot mainfewshot_ProcessSession](mainfewshot.md#BKMK_mainfewshot_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`mainfewshot`|
|ReferencedAttribute|`mainfewshotid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mainfewshot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_makerfewshot_ProcessSession"></a> makerfewshot_ProcessSession

One-To-Many Relationship: [makerfewshot makerfewshot_ProcessSession](makerfewshot.md#BKMK_makerfewshot_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`makerfewshot`|
|ReferencedAttribute|`makerfewshotid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_makerfewshot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_managedidentity_ProcessSession"></a> managedidentity_ProcessSession

One-To-Many Relationship: [managedidentity managedidentity_ProcessSession](managedidentity.md#BKMK_managedidentity_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`managedidentity`|
|ReferencedAttribute|`managedidentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_managedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_maskingrule_ProcessSession"></a> maskingrule_ProcessSession

One-To-Many Relationship: [maskingrule maskingrule_ProcessSession](maskingrule.md#BKMK_maskingrule_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`maskingrule`|
|ReferencedAttribute|`maskingruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_maskingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mcpserver_ProcessSession"></a> mcpserver_ProcessSession

One-To-Many Relationship: [mcpserver mcpserver_ProcessSession](mcpserver.md#BKMK_mcpserver_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`mcpserver`|
|ReferencedAttribute|`mcpserverid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mcpserver`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mcptool_ProcessSession"></a> mcptool_ProcessSession

One-To-Many Relationship: [mcptool mcptool_ProcessSession](mcptool.md#BKMK_mcptool_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`mcptool`|
|ReferencedAttribute|`mcptoolid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mcptool`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_metadataforarchival_ProcessSession"></a> metadataforarchival_ProcessSession

One-To-Many Relationship: [metadataforarchival metadataforarchival_ProcessSession](metadataforarchival.md#BKMK_metadataforarchival_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`metadataforarchival`|
|ReferencedAttribute|`metadataforarchivalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_metadataforarchival`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_metric_ProcessSessions"></a> metric_ProcessSessions

One-To-Many Relationship: [metric metric_ProcessSessions](metric.md#BKMK_metric_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`metric`|
|ReferencedAttribute|`metricid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_metric`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mobileofflineprofileextension_ProcessSession"></a> mobileofflineprofileextension_ProcessSession

One-To-Many Relationship: [mobileofflineprofileextension mobileofflineprofileextension_ProcessSession](mobileofflineprofileextension.md#BKMK_mobileofflineprofileextension_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`mobileofflineprofileextension`|
|ReferencedAttribute|`mobileofflineprofileextensionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mobileofflineprofileextension`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdataset_ProcessSession"></a> msdyn_aibdataset_ProcessSession

One-To-Many Relationship: [msdyn_aibdataset msdyn_aibdataset_ProcessSession](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdataset`|
|ReferencedAttribute|`msdyn_aibdatasetid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibdataset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetfile_ProcessSession"></a> msdyn_aibdatasetfile_ProcessSession

One-To-Many Relationship: [msdyn_aibdatasetfile msdyn_aibdatasetfile_ProcessSession](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetfile`|
|ReferencedAttribute|`msdyn_aibdatasetfileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibdatasetfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetrecord_ProcessSession"></a> msdyn_aibdatasetrecord_ProcessSession

One-To-Many Relationship: [msdyn_aibdatasetrecord msdyn_aibdatasetrecord_ProcessSession](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetrecord`|
|ReferencedAttribute|`msdyn_aibdatasetrecordid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibdatasetrecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetscontainer_ProcessSession"></a> msdyn_aibdatasetscontainer_ProcessSession

One-To-Many Relationship: [msdyn_aibdatasetscontainer msdyn_aibdatasetscontainer_ProcessSession](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetscontainer`|
|ReferencedAttribute|`msdyn_aibdatasetscontainerid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibdatasetscontainer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfeedbackloop_ProcessSession"></a> msdyn_aibfeedbackloop_ProcessSession

One-To-Many Relationship: [msdyn_aibfeedbackloop msdyn_aibfeedbackloop_ProcessSession](msdyn_aibfeedbackloop.md#BKMK_msdyn_aibfeedbackloop_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfeedbackloop`|
|ReferencedAttribute|`msdyn_aibfeedbackloopid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibfeedbackloop`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfile_ProcessSession"></a> msdyn_aibfile_ProcessSession

One-To-Many Relationship: [msdyn_aibfile msdyn_aibfile_ProcessSession](msdyn_aibfile.md#BKMK_msdyn_aibfile_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfile`|
|ReferencedAttribute|`msdyn_aibfileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfileattacheddata_ProcessSession"></a> msdyn_aibfileattacheddata_ProcessSession

One-To-Many Relationship: [msdyn_aibfileattacheddata msdyn_aibfileattacheddata_ProcessSession](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfileattacheddata`|
|ReferencedAttribute|`msdyn_aibfileattacheddataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibfileattacheddata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiconfiguration_ProcessSession"></a> msdyn_aiconfiguration_ProcessSession

One-To-Many Relationship: [msdyn_aiconfiguration msdyn_aiconfiguration_ProcessSession](msdyn_aiconfiguration.md#BKMK_msdyn_aiconfiguration_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiconfiguration`|
|ReferencedAttribute|`msdyn_aiconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aidataprocessingevent_ProcessSession"></a> msdyn_aidataprocessingevent_ProcessSession

One-To-Many Relationship: [msdyn_aidataprocessingevent msdyn_aidataprocessingevent_ProcessSession](msdyn_aidataprocessingevent.md#BKMK_msdyn_aidataprocessingevent_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aidataprocessingevent`|
|ReferencedAttribute|`msdyn_aidataprocessingeventid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aidataprocessingevent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aidocumenttemplate_ProcessSession"></a> msdyn_aidocumenttemplate_ProcessSession

One-To-Many Relationship: [msdyn_aidocumenttemplate msdyn_aidocumenttemplate_ProcessSession](msdyn_aidocumenttemplate.md#BKMK_msdyn_aidocumenttemplate_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aidocumenttemplate`|
|ReferencedAttribute|`msdyn_aidocumenttemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aidocumenttemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievaluationconfiguration_ProcessSession"></a> msdyn_aievaluationconfiguration_ProcessSession

One-To-Many Relationship: [msdyn_aievaluationconfiguration msdyn_aievaluationconfiguration_ProcessSession](msdyn_aievaluationconfiguration.md#BKMK_msdyn_aievaluationconfiguration_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievaluationconfiguration`|
|ReferencedAttribute|`msdyn_aievaluationconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aievaluationconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievaluationrun_ProcessSession"></a> msdyn_aievaluationrun_ProcessSession

One-To-Many Relationship: [msdyn_aievaluationrun msdyn_aievaluationrun_ProcessSession](msdyn_aievaluationrun.md#BKMK_msdyn_aievaluationrun_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievaluationrun`|
|ReferencedAttribute|`msdyn_aievaluationrunid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aievaluationrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievent_ProcessSession"></a> msdyn_aievent_ProcessSession

One-To-Many Relationship: [msdyn_aievent msdyn_aievent_ProcessSession](msdyn_aievent.md#BKMK_msdyn_aievent_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievent`|
|ReferencedAttribute|`msdyn_aieventid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aievent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aifptrainingdocument_ProcessSession"></a> msdyn_aifptrainingdocument_ProcessSession

One-To-Many Relationship: [msdyn_aifptrainingdocument msdyn_aifptrainingdocument_ProcessSession](msdyn_aifptrainingdocument.md#BKMK_msdyn_aifptrainingdocument_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aifptrainingdocument`|
|ReferencedAttribute|`msdyn_aifptrainingdocumentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aifptrainingdocument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aimodel_ProcessSession"></a> msdyn_aimodel_ProcessSession

One-To-Many Relationship: [msdyn_aimodel msdyn_aimodel_ProcessSession](msdyn_aimodel.md#BKMK_msdyn_aimodel_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aimodel`|
|ReferencedAttribute|`msdyn_aimodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aimodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodimage_ProcessSession"></a> msdyn_aiodimage_ProcessSession

One-To-Many Relationship: [msdyn_aiodimage msdyn_aiodimage_ProcessSession](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodimage`|
|ReferencedAttribute|`msdyn_aiodimageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiodimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodlabel_ProcessSession"></a> msdyn_aiodlabel_ProcessSession

One-To-Many Relationship: [msdyn_aiodlabel msdyn_aiodlabel_ProcessSession](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodlabel`|
|ReferencedAttribute|`msdyn_aiodlabelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiodlabel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodtrainingboundingbox_ProcessSession"></a> msdyn_aiodtrainingboundingbox_ProcessSession

One-To-Many Relationship: [msdyn_aiodtrainingboundingbox msdyn_aiodtrainingboundingbox_ProcessSession](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodtrainingboundingbox`|
|ReferencedAttribute|`msdyn_aiodtrainingboundingboxid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiodtrainingboundingbox`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodtrainingimage_ProcessSession"></a> msdyn_aiodtrainingimage_ProcessSession

One-To-Many Relationship: [msdyn_aiodtrainingimage msdyn_aiodtrainingimage_ProcessSession](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodtrainingimage`|
|ReferencedAttribute|`msdyn_aiodtrainingimageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiodtrainingimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitemplate_ProcessSession"></a> msdyn_aitemplate_ProcessSession

One-To-Many Relationship: [msdyn_aitemplate msdyn_aitemplate_ProcessSession](msdyn_aitemplate.md#BKMK_msdyn_aitemplate_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitemplate`|
|ReferencedAttribute|`msdyn_aitemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestcase_ProcessSession"></a> msdyn_aitestcase_ProcessSession

One-To-Many Relationship: [msdyn_aitestcase msdyn_aitestcase_ProcessSession](msdyn_aitestcase.md#BKMK_msdyn_aitestcase_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestcase`|
|ReferencedAttribute|`msdyn_aitestcaseid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestcase`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestcasedocument_ProcessSession"></a> msdyn_aitestcasedocument_ProcessSession

One-To-Many Relationship: [msdyn_aitestcasedocument msdyn_aitestcasedocument_ProcessSession](msdyn_aitestcasedocument.md#BKMK_msdyn_aitestcasedocument_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestcasedocument`|
|ReferencedAttribute|`msdyn_aitestcasedocumentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestcasedocument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestcaseinput_ProcessSession"></a> msdyn_aitestcaseinput_ProcessSession

One-To-Many Relationship: [msdyn_aitestcaseinput msdyn_aitestcaseinput_ProcessSession](msdyn_aitestcaseinput.md#BKMK_msdyn_aitestcaseinput_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestcaseinput`|
|ReferencedAttribute|`msdyn_aitestcaseinputid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestcaseinput`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestrun_ProcessSession"></a> msdyn_aitestrun_ProcessSession

One-To-Many Relationship: [msdyn_aitestrun msdyn_aitestrun_ProcessSession](msdyn_aitestrun.md#BKMK_msdyn_aitestrun_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestrun`|
|ReferencedAttribute|`msdyn_aitestrunid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestrunbatch_ProcessSession"></a> msdyn_aitestrunbatch_ProcessSession

One-To-Many Relationship: [msdyn_aitestrunbatch msdyn_aitestrunbatch_ProcessSession](msdyn_aitestrunbatch.md#BKMK_msdyn_aitestrunbatch_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestrunbatch`|
|ReferencedAttribute|`msdyn_aitestrunbatchid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestrunbatch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysiscomponent_ProcessSession"></a> msdyn_analysiscomponent_ProcessSession

One-To-Many Relationship: [msdyn_analysiscomponent msdyn_analysiscomponent_ProcessSession](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysiscomponent`|
|ReferencedAttribute|`msdyn_analysiscomponentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysiscomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisjob_ProcessSession"></a> msdyn_analysisjob_ProcessSession

One-To-Many Relationship: [msdyn_analysisjob msdyn_analysisjob_ProcessSession](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisjob`|
|ReferencedAttribute|`msdyn_analysisjobid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysisjob`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisoverride_ProcessSession"></a> msdyn_analysisoverride_ProcessSession

One-To-Many Relationship: [msdyn_analysisoverride msdyn_analysisoverride_ProcessSession](msdyn_analysisoverride.md#BKMK_msdyn_analysisoverride_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisoverride`|
|ReferencedAttribute|`msdyn_analysisoverrideid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysisoverride`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisresult_ProcessSession"></a> msdyn_analysisresult_ProcessSession

One-To-Many Relationship: [msdyn_analysisresult msdyn_analysisresult_ProcessSession](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisresult`|
|ReferencedAttribute|`msdyn_analysisresultid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysisresult`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisresultdetail_ProcessSession"></a> msdyn_analysisresultdetail_ProcessSession

One-To-Many Relationship: [msdyn_analysisresultdetail msdyn_analysisresultdetail_ProcessSession](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisresultdetail`|
|ReferencedAttribute|`msdyn_analysisresultdetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysisresultdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_appinsightsmetadata_ProcessSession"></a> msdyn_appinsightsmetadata_ProcessSession

One-To-Many Relationship: [msdyn_appinsightsmetadata msdyn_appinsightsmetadata_ProcessSession](msdyn_appinsightsmetadata.md#BKMK_msdyn_appinsightsmetadata_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_appinsightsmetadata`|
|ReferencedAttribute|`msdyn_appinsightsmetadataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_appinsightsmetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_copilotinteractions_ProcessSession"></a> msdyn_copilotinteractions_ProcessSession

One-To-Many Relationship: [msdyn_copilotinteractions msdyn_copilotinteractions_ProcessSession](msdyn_copilotinteractions.md#BKMK_msdyn_copilotinteractions_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_copilotinteractions`|
|ReferencedAttribute|`msdyn_copilotinteractionsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_copilotinteractions`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_customcontrolextendedsettings_ProcessSession"></a> msdyn_customcontrolextendedsettings_ProcessSession

One-To-Many Relationship: [msdyn_customcontrolextendedsettings msdyn_customcontrolextendedsettings_ProcessSession](msdyn_customcontrolextendedsettings.md#BKMK_msdyn_customcontrolextendedsettings_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_customcontrolextendedsettings`|
|ReferencedAttribute|`msdyn_customcontrolextendedsettingsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_customcontrolextendedsettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflow_datalakefolder_ProcessSession"></a> msdyn_dataflow_datalakefolder_ProcessSession

One-To-Many Relationship: [msdyn_dataflow_datalakefolder msdyn_dataflow_datalakefolder_ProcessSession](msdyn_dataflow_datalakefolder.md#BKMK_msdyn_dataflow_datalakefolder_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflow_datalakefolder`|
|ReferencedAttribute|`msdyn_dataflow_datalakefolderid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflow_datalakefolder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflow_ProcessSession"></a> msdyn_dataflow_ProcessSession

One-To-Many Relationship: [msdyn_dataflow msdyn_dataflow_ProcessSession](msdyn_dataflow.md#BKMK_msdyn_dataflow_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflow`|
|ReferencedAttribute|`msdyn_dataflowid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflow`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowconnectionreference_ProcessSession"></a> msdyn_dataflowconnectionreference_ProcessSession

One-To-Many Relationship: [msdyn_dataflowconnectionreference msdyn_dataflowconnectionreference_ProcessSession](msdyn_dataflowconnectionreference.md#BKMK_msdyn_dataflowconnectionreference_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowconnectionreference`|
|ReferencedAttribute|`msdyn_dataflowconnectionreferenceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflowconnectionreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowrefreshhistory_ProcessSession"></a> msdyn_dataflowrefreshhistory_ProcessSession

One-To-Many Relationship: [msdyn_dataflowrefreshhistory msdyn_dataflowrefreshhistory_ProcessSession](msdyn_dataflowrefreshhistory.md#BKMK_msdyn_dataflowrefreshhistory_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowrefreshhistory`|
|ReferencedAttribute|`msdyn_dataflowrefreshhistoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflowrefreshhistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowtemplate_ProcessSession"></a> msdyn_dataflowtemplate_ProcessSession

One-To-Many Relationship: [msdyn_dataflowtemplate msdyn_dataflowtemplate_ProcessSession](msdyn_dataflowtemplate.md#BKMK_msdyn_dataflowtemplate_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowtemplate`|
|ReferencedAttribute|`msdyn_dataflowtemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflowtemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmsrequest_ProcessSession"></a> msdyn_dmsrequest_ProcessSession

One-To-Many Relationship: [msdyn_dmsrequest msdyn_dmsrequest_ProcessSession](msdyn_dmsrequest.md#BKMK_msdyn_dmsrequest_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmsrequest`|
|ReferencedAttribute|`msdyn_dmsrequestid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dmsrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmsrequeststatus_ProcessSession"></a> msdyn_dmsrequeststatus_ProcessSession

One-To-Many Relationship: [msdyn_dmsrequeststatus msdyn_dmsrequeststatus_ProcessSession](msdyn_dmsrequeststatus.md#BKMK_msdyn_dmsrequeststatus_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmsrequeststatus`|
|ReferencedAttribute|`msdyn_dmsrequeststatusid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dmsrequeststatus`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmssyncrequest_ProcessSession"></a> msdyn_dmssyncrequest_ProcessSession

One-To-Many Relationship: [msdyn_dmssyncrequest msdyn_dmssyncrequest_ProcessSession](msdyn_dmssyncrequest.md#BKMK_msdyn_dmssyncrequest_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmssyncrequest`|
|ReferencedAttribute|`msdyn_dmssyncrequestid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dmssyncrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmssyncstatus_ProcessSession"></a> msdyn_dmssyncstatus_ProcessSession

One-To-Many Relationship: [msdyn_dmssyncstatus msdyn_dmssyncstatus_ProcessSession](msdyn_dmssyncstatus.md#BKMK_msdyn_dmssyncstatus_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmssyncstatus`|
|ReferencedAttribute|`msdyn_dmssyncstatusid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dmssyncstatus`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_entitylinkchatconfiguration_ProcessSession"></a> msdyn_entitylinkchatconfiguration_ProcessSession

One-To-Many Relationship: [msdyn_entitylinkchatconfiguration msdyn_entitylinkchatconfiguration_ProcessSession](msdyn_entitylinkchatconfiguration.md#BKMK_msdyn_entitylinkchatconfiguration_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_entitylinkchatconfiguration`|
|ReferencedAttribute|`msdyn_entitylinkchatconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_entitylinkchatconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_entityrefreshhistory_ProcessSession"></a> msdyn_entityrefreshhistory_ProcessSession

One-To-Many Relationship: [msdyn_entityrefreshhistory msdyn_entityrefreshhistory_ProcessSession](msdyn_entityrefreshhistory.md#BKMK_msdyn_entityrefreshhistory_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_entityrefreshhistory`|
|ReferencedAttribute|`msdyn_entityrefreshhistoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_entityrefreshhistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_favoriteknowledgearticle_ProcessSession"></a> msdyn_favoriteknowledgearticle_ProcessSession

One-To-Many Relationship: [msdyn_favoriteknowledgearticle msdyn_favoriteknowledgearticle_ProcessSession](msdyn_favoriteknowledgearticle.md#BKMK_msdyn_favoriteknowledgearticle_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_favoriteknowledgearticle`|
|ReferencedAttribute|`msdyn_favoriteknowledgearticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_favoriteknowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_federatedarticle_ProcessSession"></a> msdyn_federatedarticle_ProcessSession

One-To-Many Relationship: [msdyn_federatedarticle msdyn_federatedarticle_ProcessSession](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_federatedarticle`|
|ReferencedAttribute|`msdyn_federatedarticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_federatedarticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_federatedarticleincident_ProcessSession"></a> msdyn_federatedarticleincident_ProcessSession

One-To-Many Relationship: [msdyn_federatedarticleincident msdyn_federatedarticleincident_ProcessSession](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_federatedarticleincident`|
|ReferencedAttribute|`msdyn_federatedarticleincidentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_federatedarticleincident`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_fileupload_ProcessSession"></a> msdyn_fileupload_ProcessSession

One-To-Many Relationship: [msdyn_fileupload msdyn_fileupload_ProcessSession](msdyn_fileupload.md#BKMK_msdyn_fileupload_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_fileupload`|
|ReferencedAttribute|`msdyn_fileuploadid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_fileupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_actionapprovalmodel_ProcessSession"></a> msdyn_flow_actionapprovalmodel_ProcessSession

One-To-Many Relationship: [msdyn_flow_actionapprovalmodel msdyn_flow_actionapprovalmodel_ProcessSession](msdyn_flow_actionapprovalmodel.md#BKMK_msdyn_flow_actionapprovalmodel_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_actionapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_actionapprovalmodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_actionapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approval_ProcessSession"></a> msdyn_flow_approval_ProcessSession

One-To-Many Relationship: [msdyn_flow_approval msdyn_flow_approval_ProcessSession](msdyn_flow_approval.md#BKMK_msdyn_flow_approval_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approval`|
|ReferencedAttribute|`msdyn_flow_approvalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_approval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalrequest_ProcessSession"></a> msdyn_flow_approvalrequest_ProcessSession

One-To-Many Relationship: [msdyn_flow_approvalrequest msdyn_flow_approvalrequest_ProcessSession](msdyn_flow_approvalrequest.md#BKMK_msdyn_flow_approvalrequest_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalrequest`|
|ReferencedAttribute|`msdyn_flow_approvalrequestid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_approvalrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalresponse_ProcessSession"></a> msdyn_flow_approvalresponse_ProcessSession

One-To-Many Relationship: [msdyn_flow_approvalresponse msdyn_flow_approvalresponse_ProcessSession](msdyn_flow_approvalresponse.md#BKMK_msdyn_flow_approvalresponse_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalresponse`|
|ReferencedAttribute|`msdyn_flow_approvalresponseid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_approvalresponse`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalstep_ProcessSession"></a> msdyn_flow_approvalstep_ProcessSession

One-To-Many Relationship: [msdyn_flow_approvalstep msdyn_flow_approvalstep_ProcessSession](msdyn_flow_approvalstep.md#BKMK_msdyn_flow_approvalstep_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalstep`|
|ReferencedAttribute|`msdyn_flow_approvalstepid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_approvalstep`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_awaitallactionapprovalmodel_ProcessSession"></a> msdyn_flow_awaitallactionapprovalmodel_ProcessSession

One-To-Many Relationship: [msdyn_flow_awaitallactionapprovalmodel msdyn_flow_awaitallactionapprovalmodel_ProcessSession](msdyn_flow_awaitallactionapprovalmodel.md#BKMK_msdyn_flow_awaitallactionapprovalmodel_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_awaitallactionapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_awaitallactionapprovalmodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_awaitallactionapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_awaitallapprovalmodel_ProcessSession"></a> msdyn_flow_awaitallapprovalmodel_ProcessSession

One-To-Many Relationship: [msdyn_flow_awaitallapprovalmodel msdyn_flow_awaitallapprovalmodel_ProcessSession](msdyn_flow_awaitallapprovalmodel.md#BKMK_msdyn_flow_awaitallapprovalmodel_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_awaitallapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_awaitallapprovalmodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_awaitallapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_basicapprovalmodel_ProcessSession"></a> msdyn_flow_basicapprovalmodel_ProcessSession

One-To-Many Relationship: [msdyn_flow_basicapprovalmodel msdyn_flow_basicapprovalmodel_ProcessSession](msdyn_flow_basicapprovalmodel.md#BKMK_msdyn_flow_basicapprovalmodel_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_basicapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_basicapprovalmodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_basicapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_flowapproval_ProcessSession"></a> msdyn_flow_flowapproval_ProcessSession

One-To-Many Relationship: [msdyn_flow_flowapproval msdyn_flow_flowapproval_ProcessSession](msdyn_flow_flowapproval.md#BKMK_msdyn_flow_flowapproval_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_flowapproval`|
|ReferencedAttribute|`msdyn_flow_flowapprovalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_flowapproval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_formmapping_ProcessSession"></a> msdyn_formmapping_ProcessSession

One-To-Many Relationship: [msdyn_formmapping msdyn_formmapping_ProcessSession](msdyn_formmapping.md#BKMK_msdyn_formmapping_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_formmapping`|
|ReferencedAttribute|`msdyn_formmappingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_formmapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_function_ProcessSession"></a> msdyn_function_ProcessSession

One-To-Many Relationship: [msdyn_function msdyn_function_ProcessSession](msdyn_function.md#BKMK_msdyn_function_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_function`|
|ReferencedAttribute|`msdyn_functionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_function`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_helppage_ProcessSession"></a> msdyn_helppage_ProcessSession

One-To-Many Relationship: [msdyn_helppage msdyn_helppage_ProcessSession](msdyn_helppage.md#BKMK_msdyn_helppage_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_helppage`|
|ReferencedAttribute|`msdyn_helppageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_helppage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_historicalcaseharvestbatch_ProcessSession"></a> msdyn_historicalcaseharvestbatch_ProcessSession

One-To-Many Relationship: [msdyn_historicalcaseharvestbatch msdyn_historicalcaseharvestbatch_ProcessSession](msdyn_historicalcaseharvestbatch.md#BKMK_msdyn_historicalcaseharvestbatch_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_historicalcaseharvestbatch`|
|ReferencedAttribute|`msdyn_historicalcaseharvestbatchid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_historicalcaseharvestbatch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_historicalcaseharvestrun_ProcessSession"></a> msdyn_historicalcaseharvestrun_ProcessSession

One-To-Many Relationship: [msdyn_historicalcaseharvestrun msdyn_historicalcaseharvestrun_ProcessSession](msdyn_historicalcaseharvestrun.md#BKMK_msdyn_historicalcaseharvestrun_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_historicalcaseharvestrun`|
|ReferencedAttribute|`msdyn_historicalcaseharvestrunid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_historicalcaseharvestrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_insightsstorevirtualentity_ProcessSession"></a> msdyn_insightsstorevirtualentity_ProcessSession

One-To-Many Relationship: [msdyn_insightsstorevirtualentity msdyn_insightsstorevirtualentity_ProcessSession](msdyn_insightsstorevirtualentity.md#BKMK_msdyn_insightsstorevirtualentity_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_insightsstorevirtualentity`|
|ReferencedAttribute|`msdyn_insightsstorevirtualentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_insightsstorevirtualentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_integratedsearchprovider_ProcessSession"></a> msdyn_integratedsearchprovider_ProcessSession

One-To-Many Relationship: [msdyn_integratedsearchprovider msdyn_integratedsearchprovider_ProcessSession](msdyn_integratedsearchprovider.md#BKMK_msdyn_integratedsearchprovider_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_integratedsearchprovider`|
|ReferencedAttribute|`msdyn_integratedsearchproviderid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_integratedsearchprovider`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kalanguagesetting_ProcessSession"></a> msdyn_kalanguagesetting_ProcessSession

One-To-Many Relationship: [msdyn_kalanguagesetting msdyn_kalanguagesetting_ProcessSession](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kalanguagesetting`|
|ReferencedAttribute|`msdyn_kalanguagesettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_kalanguagesetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kbattachment_ProcessSession"></a> msdyn_kbattachment_ProcessSession

One-To-Many Relationship: [msdyn_kbattachment msdyn_kbattachment_ProcessSession](msdyn_kbattachment.md#BKMK_msdyn_kbattachment_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kbattachment`|
|ReferencedAttribute|`msdyn_kbattachmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_kbattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kmfederatedsearchconfig_ProcessSession"></a> msdyn_kmfederatedsearchconfig_ProcessSession

One-To-Many Relationship: [msdyn_kmfederatedsearchconfig msdyn_kmfederatedsearchconfig_ProcessSession](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kmfederatedsearchconfig`|
|ReferencedAttribute|`msdyn_kmfederatedsearchconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_kmfederatedsearchconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kmpersonalizationsetting_ProcessSession"></a> msdyn_kmpersonalizationsetting_ProcessSession

One-To-Many Relationship: [msdyn_kmpersonalizationsetting msdyn_kmpersonalizationsetting_ProcessSession](msdyn_kmpersonalizationsetting.md#BKMK_msdyn_kmpersonalizationsetting_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kmpersonalizationsetting`|
|ReferencedAttribute|`msdyn_kmpersonalizationsettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_kmpersonalizationsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgearticleimage_ProcessSession"></a> msdyn_knowledgearticleimage_ProcessSession

One-To-Many Relationship: [msdyn_knowledgearticleimage msdyn_knowledgearticleimage_ProcessSession](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgearticleimage`|
|ReferencedAttribute|`msdyn_knowledgearticleimageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgearticleimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgearticletemplate_ProcessSession"></a> msdyn_knowledgearticletemplate_ProcessSession

One-To-Many Relationship: [msdyn_knowledgearticletemplate msdyn_knowledgearticletemplate_ProcessSession](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgearticletemplate`|
|ReferencedAttribute|`msdyn_knowledgearticletemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgearticletemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeassetconfiguration_ProcessSession"></a> msdyn_knowledgeassetconfiguration_ProcessSession

One-To-Many Relationship: [msdyn_knowledgeassetconfiguration msdyn_knowledgeassetconfiguration_ProcessSession](msdyn_knowledgeassetconfiguration.md#BKMK_msdyn_knowledgeassetconfiguration_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeassetconfiguration`|
|ReferencedAttribute|`msdyn_knowledgeassetconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgeassetconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeconfiguration_ProcessSession"></a> msdyn_knowledgeconfiguration_ProcessSession

One-To-Many Relationship: [msdyn_knowledgeconfiguration msdyn_knowledgeconfiguration_ProcessSession](msdyn_knowledgeconfiguration.md#BKMK_msdyn_knowledgeconfiguration_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeconfiguration`|
|ReferencedAttribute|`msdyn_knowledgeconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeharvestjobrecord_ProcessSession"></a> msdyn_knowledgeharvestjobrecord_ProcessSession

One-To-Many Relationship: [msdyn_knowledgeharvestjobrecord msdyn_knowledgeharvestjobrecord_ProcessSession](msdyn_knowledgeharvestjobrecord.md#BKMK_msdyn_knowledgeharvestjobrecord_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeharvestjobrecord`|
|ReferencedAttribute|`msdyn_knowledgeharvestjobrecordid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgeharvestjobrecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeinteractioninsight_ProcessSession"></a> msdyn_knowledgeinteractioninsight_ProcessSession

One-To-Many Relationship: [msdyn_knowledgeinteractioninsight msdyn_knowledgeinteractioninsight_ProcessSession](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeinteractioninsight`|
|ReferencedAttribute|`msdyn_knowledgeinteractioninsightid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgeinteractioninsight`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgemanagementsetting_ProcessSession"></a> msdyn_knowledgemanagementsetting_ProcessSession

One-To-Many Relationship: [msdyn_knowledgemanagementsetting msdyn_knowledgemanagementsetting_ProcessSession](msdyn_knowledgemanagementsetting.md#BKMK_msdyn_knowledgemanagementsetting_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgemanagementsetting`|
|ReferencedAttribute|`msdyn_knowledgemanagementsettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgemanagementsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgepersonalfilter_ProcessSession"></a> msdyn_knowledgepersonalfilter_ProcessSession

One-To-Many Relationship: [msdyn_knowledgepersonalfilter msdyn_knowledgepersonalfilter_ProcessSession](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgepersonalfilter`|
|ReferencedAttribute|`msdyn_knowledgepersonalfilterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgepersonalfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgesearchfilter_ProcessSession"></a> msdyn_knowledgesearchfilter_ProcessSession

One-To-Many Relationship: [msdyn_knowledgesearchfilter msdyn_knowledgesearchfilter_ProcessSession](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgesearchfilter`|
|ReferencedAttribute|`msdyn_knowledgesearchfilterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgesearchfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgesearchinsight_ProcessSession"></a> msdyn_knowledgesearchinsight_ProcessSession

One-To-Many Relationship: [msdyn_knowledgesearchinsight msdyn_knowledgesearchinsight_ProcessSession](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgesearchinsight`|
|ReferencedAttribute|`msdyn_knowledgesearchinsightid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgesearchinsight`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_mobileapp_ProcessSession"></a> msdyn_mobileapp_ProcessSession

One-To-Many Relationship: [msdyn_mobileapp msdyn_mobileapp_ProcessSession](msdyn_mobileapp.md#BKMK_msdyn_mobileapp_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_mobileapp`|
|ReferencedAttribute|`msdyn_mobileappid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_mobileapp`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_modulerundetail_ProcessSession"></a> msdyn_modulerundetail_ProcessSession

One-To-Many Relationship: [msdyn_modulerundetail msdyn_modulerundetail_ProcessSession](msdyn_modulerundetail.md#BKMK_msdyn_modulerundetail_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_modulerundetail`|
|ReferencedAttribute|`msdyn_modulerundetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_modulerundetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmanalysishistory_ProcessSession"></a> msdyn_pmanalysishistory_ProcessSession

One-To-Many Relationship: [msdyn_pmanalysishistory msdyn_pmanalysishistory_ProcessSession](msdyn_pmanalysishistory.md#BKMK_msdyn_pmanalysishistory_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmanalysishistory`|
|ReferencedAttribute|`msdyn_pmanalysishistoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmanalysishistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmbusinessruleautomationconfig_ProcessSession"></a> msdyn_pmbusinessruleautomationconfig_ProcessSession

One-To-Many Relationship: [msdyn_pmbusinessruleautomationconfig msdyn_pmbusinessruleautomationconfig_ProcessSession](msdyn_pmbusinessruleautomationconfig.md#BKMK_msdyn_pmbusinessruleautomationconfig_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmbusinessruleautomationconfig`|
|ReferencedAttribute|`msdyn_pmbusinessruleautomationconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmbusinessruleautomationconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmcalendar_ProcessSession"></a> msdyn_pmcalendar_ProcessSession

One-To-Many Relationship: [msdyn_pmcalendar msdyn_pmcalendar_ProcessSession](msdyn_pmcalendar.md#BKMK_msdyn_pmcalendar_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmcalendar`|
|ReferencedAttribute|`msdyn_pmcalendarid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmcalendar`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmcalendarversion_ProcessSession"></a> msdyn_pmcalendarversion_ProcessSession

One-To-Many Relationship: [msdyn_pmcalendarversion msdyn_pmcalendarversion_ProcessSession](msdyn_pmcalendarversion.md#BKMK_msdyn_pmcalendarversion_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmcalendarversion`|
|ReferencedAttribute|`msdyn_pmcalendarversionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmcalendarversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pminferredtask_ProcessSession"></a> msdyn_pminferredtask_ProcessSession

One-To-Many Relationship: [msdyn_pminferredtask msdyn_pminferredtask_ProcessSession](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pminferredtask`|
|ReferencedAttribute|`msdyn_pminferredtaskid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pminferredtask`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessextendedmetadataversion_ProcessSession"></a> msdyn_pmprocessextendedmetadataversion_ProcessSession

One-To-Many Relationship: [msdyn_pmprocessextendedmetadataversion msdyn_pmprocessextendedmetadataversion_ProcessSession](msdyn_pmprocessextendedmetadataversion.md#BKMK_msdyn_pmprocessextendedmetadataversion_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessextendedmetadataversion`|
|ReferencedAttribute|`msdyn_pmprocessextendedmetadataversionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmprocessextendedmetadataversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocesstemplate_ProcessSession"></a> msdyn_pmprocesstemplate_ProcessSession

One-To-Many Relationship: [msdyn_pmprocesstemplate msdyn_pmprocesstemplate_ProcessSession](msdyn_pmprocesstemplate.md#BKMK_msdyn_pmprocesstemplate_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocesstemplate`|
|ReferencedAttribute|`msdyn_pmprocesstemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmprocesstemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessusersettings_ProcessSession"></a> msdyn_pmprocessusersettings_ProcessSession

One-To-Many Relationship: [msdyn_pmprocessusersettings msdyn_pmprocessusersettings_ProcessSession](msdyn_pmprocessusersettings.md#BKMK_msdyn_pmprocessusersettings_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessusersettings`|
|ReferencedAttribute|`msdyn_pmprocessusersettingsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmprocessusersettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessversion_ProcessSession"></a> msdyn_pmprocessversion_ProcessSession

One-To-Many Relationship: [msdyn_pmprocessversion msdyn_pmprocessversion_ProcessSession](msdyn_pmprocessversion.md#BKMK_msdyn_pmprocessversion_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessversion`|
|ReferencedAttribute|`msdyn_pmprocessversionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmprocessversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmrecording_ProcessSession"></a> msdyn_pmrecording_ProcessSession

One-To-Many Relationship: [msdyn_pmrecording msdyn_pmrecording_ProcessSession](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmrecording`|
|ReferencedAttribute|`msdyn_pmrecordingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmrecording`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmsimulation_ProcessSession"></a> msdyn_pmsimulation_ProcessSession

One-To-Many Relationship: [msdyn_pmsimulation msdyn_pmsimulation_ProcessSession](msdyn_pmsimulation.md#BKMK_msdyn_pmsimulation_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmsimulation`|
|ReferencedAttribute|`msdyn_pmsimulationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmsimulation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmtab_ProcessSession"></a> msdyn_pmtab_ProcessSession

One-To-Many Relationship: [msdyn_pmtab msdyn_pmtab_ProcessSession](msdyn_pmtab.md#BKMK_msdyn_pmtab_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmtab`|
|ReferencedAttribute|`msdyn_pmtabid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmtab`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmtemplate_ProcessSession"></a> msdyn_pmtemplate_ProcessSession

One-To-Many Relationship: [msdyn_pmtemplate msdyn_pmtemplate_ProcessSession](msdyn_pmtemplate.md#BKMK_msdyn_pmtemplate_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmtemplate`|
|ReferencedAttribute|`msdyn_pmtemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmtemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmview_ProcessSession"></a> msdyn_pmview_ProcessSession

One-To-Many Relationship: [msdyn_pmview msdyn_pmview_ProcessSession](msdyn_pmview.md#BKMK_msdyn_pmview_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmview`|
|ReferencedAttribute|`msdyn_pmviewid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmview`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_qna_ProcessSession"></a> msdyn_qna_ProcessSession

One-To-Many Relationship: [msdyn_qna msdyn_qna_ProcessSession](msdyn_qna.md#BKMK_msdyn_qna_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_qna`|
|ReferencedAttribute|`msdyn_qnaid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_qna`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_richtextfile_ProcessSession"></a> msdyn_richtextfile_ProcessSession

One-To-Many Relationship: [msdyn_richtextfile msdyn_richtextfile_ProcessSession](msdyn_richtextfile.md#BKMK_msdyn_richtextfile_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_richtextfile`|
|ReferencedAttribute|`msdyn_richtextfileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_richtextfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_salesforcestructuredobject_ProcessSession"></a> msdyn_salesforcestructuredobject_ProcessSession

One-To-Many Relationship: [msdyn_salesforcestructuredobject msdyn_salesforcestructuredobject_ProcessSession](msdyn_salesforcestructuredobject.md#BKMK_msdyn_salesforcestructuredobject_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_salesforcestructuredobject`|
|ReferencedAttribute|`msdyn_salesforcestructuredobjectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_salesforcestructuredobject`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_salesforcestructuredqnaconfig_ProcessSession"></a> msdyn_salesforcestructuredqnaconfig_ProcessSession

One-To-Many Relationship: [msdyn_salesforcestructuredqnaconfig msdyn_salesforcestructuredqnaconfig_ProcessSession](msdyn_salesforcestructuredqnaconfig.md#BKMK_msdyn_salesforcestructuredqnaconfig_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_salesforcestructuredqnaconfig`|
|ReferencedAttribute|`msdyn_salesforcestructuredqnaconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_salesforcestructuredqnaconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_schedule_ProcessSession"></a> msdyn_schedule_ProcessSession

One-To-Many Relationship: [msdyn_schedule msdyn_schedule_ProcessSession](msdyn_schedule.md#BKMK_msdyn_schedule_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_schedule`|
|ReferencedAttribute|`msdyn_scheduleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_schedule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_serviceconfiguration_ProcessSession"></a> msdyn_serviceconfiguration_ProcessSession

One-To-Many Relationship: [msdyn_serviceconfiguration msdyn_serviceconfiguration_ProcessSession](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_serviceconfiguration`|
|ReferencedAttribute|`msdyn_serviceconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_serviceconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_slakpi_ProcessSession"></a> msdyn_slakpi_ProcessSession

One-To-Many Relationship: [msdyn_slakpi msdyn_slakpi_ProcessSession](msdyn_slakpi.md#BKMK_msdyn_slakpi_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_slakpi`|
|ReferencedAttribute|`msdyn_slakpiid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_slakpi`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthrule_ProcessSession"></a> msdyn_solutionhealthrule_ProcessSession

One-To-Many Relationship: [msdyn_solutionhealthrule msdyn_solutionhealthrule_ProcessSession](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthrule`|
|ReferencedAttribute|`msdyn_solutionhealthruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_solutionhealthrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthruleargument_ProcessSession"></a> msdyn_solutionhealthruleargument_ProcessSession

One-To-Many Relationship: [msdyn_solutionhealthruleargument msdyn_solutionhealthruleargument_ProcessSession](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthruleargument`|
|ReferencedAttribute|`msdyn_solutionhealthruleargumentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_solutionhealthruleargument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthruleset_ProcessSession"></a> msdyn_solutionhealthruleset_ProcessSession

One-To-Many Relationship: [msdyn_solutionhealthruleset msdyn_solutionhealthruleset_ProcessSession](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthruleset`|
|ReferencedAttribute|`msdyn_solutionhealthrulesetid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_solutionhealthruleset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_tour_ProcessSession"></a> msdyn_tour_ProcessSession

One-To-Many Relationship: [msdyn_tour msdyn_tour_ProcessSession](msdyn_tour.md#BKMK_msdyn_tour_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_tour`|
|ReferencedAttribute|`msdyn_tourid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_tour`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_virtualtablecolumncandidate_ProcessSession"></a> msdyn_virtualtablecolumncandidate_ProcessSession

One-To-Many Relationship: [msdyn_virtualtablecolumncandidate msdyn_virtualtablecolumncandidate_ProcessSession](msdyn_virtualtablecolumncandidate.md#BKMK_msdyn_virtualtablecolumncandidate_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_virtualtablecolumncandidate`|
|ReferencedAttribute|`msdyn_virtualtablecolumncandidateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_virtualtablecolumncandidate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_workflowactionstatus_ProcessSession"></a> msdyn_workflowactionstatus_ProcessSession

One-To-Many Relationship: [msdyn_workflowactionstatus msdyn_workflowactionstatus_ProcessSession](msdyn_workflowactionstatus.md#BKMK_msdyn_workflowactionstatus_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_workflowactionstatus`|
|ReferencedAttribute|`msdyn_workflowactionstatusid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_workflowactionstatus`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdynce_botcontent_ProcessSession"></a> msdynce_botcontent_ProcessSession

One-To-Many Relationship: [msdynce_botcontent msdynce_botcontent_ProcessSession](msdynce_botcontent.md#BKMK_msdynce_botcontent_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msdynce_botcontent`|
|ReferencedAttribute|`msdynce_botcontentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdynce_botcontent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msgraphresourcetosubscription_ProcessSession"></a> msgraphresourcetosubscription_ProcessSession

One-To-Many Relationship: [msgraphresourcetosubscription msgraphresourcetosubscription_ProcessSession](msgraphresourcetosubscription.md#BKMK_msgraphresourcetosubscription_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`msgraphresourcetosubscription`|
|ReferencedAttribute|`msgraphresourcetosubscriptionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msgraphresourcetosubscription`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspcat_catalogsubmissionfiles_ProcessSession"></a> mspcat_catalogsubmissionfiles_ProcessSession

One-To-Many Relationship: [mspcat_catalogsubmissionfiles mspcat_catalogsubmissionfiles_ProcessSession](mspcat_catalogsubmissionfiles.md#BKMK_mspcat_catalogsubmissionfiles_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`mspcat_catalogsubmissionfiles`|
|ReferencedAttribute|`mspcat_catalogsubmissionfilesid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspcat_catalogsubmissionfiles`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspcat_packagestore_ProcessSession"></a> mspcat_packagestore_ProcessSession

One-To-Many Relationship: [mspcat_packagestore mspcat_packagestore_ProcessSession](mspcat_packagestore.md#BKMK_mspcat_packagestore_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`mspcat_packagestore`|
|ReferencedAttribute|`mspcat_packagestoreid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspcat_packagestore`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_NewProcess_ProcessSessions"></a> NewProcess_ProcessSessions

One-To-Many Relationship: [newprocess NewProcess_ProcessSessions](newprocess.md#BKMK_NewProcess_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`newprocess`|
|ReferencedAttribute|`businessprocessflowinstanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_newprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncfnostate_ProcessSession"></a> organizationdatasyncfnostate_ProcessSession

One-To-Many Relationship: [organizationdatasyncfnostate organizationdatasyncfnostate_ProcessSession](organizationdatasyncfnostate.md#BKMK_organizationdatasyncfnostate_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncfnostate`|
|ReferencedAttribute|`organizationdatasyncfnostateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncfnostate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncstate_ProcessSession"></a> organizationdatasyncstate_ProcessSession

One-To-Many Relationship: [organizationdatasyncstate organizationdatasyncstate_ProcessSession](organizationdatasyncstate.md#BKMK_organizationdatasyncstate_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncstate`|
|ReferencedAttribute|`organizationdatasyncstateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncstate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscription_ProcessSession"></a> organizationdatasyncsubscription_ProcessSession

One-To-Many Relationship: [organizationdatasyncsubscription organizationdatasyncsubscription_ProcessSession](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscription`|
|ReferencedAttribute|`organizationdatasyncsubscriptionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncsubscription`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscriptionentity_ProcessSession"></a> organizationdatasyncsubscriptionentity_ProcessSession

One-To-Many Relationship: [organizationdatasyncsubscriptionentity organizationdatasyncsubscriptionentity_ProcessSession](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscriptionentity`|
|ReferencedAttribute|`organizationdatasyncsubscriptionentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncsubscriptionentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_ProcessSession"></a> organizationdatasyncsubscriptionfnotable_ProcessSession

One-To-Many Relationship: [organizationdatasyncsubscriptionfnotable organizationdatasyncsubscriptionfnotable_ProcessSession](organizationdatasyncsubscriptionfnotable.md#BKMK_organizationdatasyncsubscriptionfnotable_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscriptionfnotable`|
|ReferencedAttribute|`organizationdatasyncsubscriptionfnotableid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncsubscriptionfnotable`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_processsessions"></a> owner_processsessions

One-To-Many Relationship: [owner owner_processsessions](owner.md#BKMK_owner_processsessions)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Owning_businessunit_processsessions"></a> Owning_businessunit_processsessions

One-To-Many Relationship: [businessunit Owning_businessunit_processsessions](businessunit.md#BKMK_Owning_businessunit_processsessions)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_package_ProcessSession"></a> package_ProcessSession

One-To-Many Relationship: [package package_ProcessSession](package.md#BKMK_package_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`package`|
|ReferencedAttribute|`packageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_package`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_packagehistory_ProcessSession"></a> packagehistory_ProcessSession

One-To-Many Relationship: [packagehistory packagehistory_ProcessSession](packagehistory.md#BKMK_packagehistory_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`packagehistory`|
|ReferencedAttribute|`packagehistoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_packagehistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_PhoneCall_ProcessSessions"></a> PhoneCall_ProcessSessions

One-To-Many Relationship: [phonecall PhoneCall_ProcessSessions](phonecall.md#BKMK_PhoneCall_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`phonecall`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_phonecall`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plannerbusinessscenario_ProcessSession"></a> plannerbusinessscenario_ProcessSession

One-To-Many Relationship: [plannerbusinessscenario plannerbusinessscenario_ProcessSession](plannerbusinessscenario.md#BKMK_plannerbusinessscenario_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`plannerbusinessscenario`|
|ReferencedAttribute|`plannerbusinessscenarioid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_plannerbusinessscenario`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plannersyncaction_ProcessSession"></a> plannersyncaction_ProcessSession

One-To-Many Relationship: [plannersyncaction plannersyncaction_ProcessSession](plannersyncaction.md#BKMK_plannersyncaction_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`plannersyncaction`|
|ReferencedAttribute|`plannersyncactionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_plannersyncaction`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plugin_ProcessSession"></a> plugin_ProcessSession

One-To-Many Relationship: [plugin plugin_ProcessSession](plugin.md#BKMK_plugin_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`plugin`|
|ReferencedAttribute|`pluginid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_plugin`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_position_ProcessSession"></a> position_ProcessSession

One-To-Many Relationship: [position position_ProcessSession](position.md#BKMK_position_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`position`|
|ReferencedAttribute|`positionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_position`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbidataset_ProcessSession"></a> powerbidataset_ProcessSession

One-To-Many Relationship: [powerbidataset powerbidataset_ProcessSession](powerbidataset.md#BKMK_powerbidataset_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbidataset`|
|ReferencedAttribute|`powerbidatasetid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbidataset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbidatasetapdx_ProcessSession"></a> powerbidatasetapdx_ProcessSession

One-To-Many Relationship: [powerbidatasetapdx powerbidatasetapdx_ProcessSession](powerbidatasetapdx.md#BKMK_powerbidatasetapdx_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbidatasetapdx`|
|ReferencedAttribute|`powerbidatasetapdxid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbidatasetapdx`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbimashupparameter_ProcessSession"></a> powerbimashupparameter_ProcessSession

One-To-Many Relationship: [powerbimashupparameter powerbimashupparameter_ProcessSession](powerbimashupparameter.md#BKMK_powerbimashupparameter_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbimashupparameter`|
|ReferencedAttribute|`powerbimashupparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbimashupparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbireport_ProcessSession"></a> powerbireport_ProcessSession

One-To-Many Relationship: [powerbireport powerbireport_ProcessSession](powerbireport.md#BKMK_powerbireport_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbireport`|
|ReferencedAttribute|`powerbireportid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbireport`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbireportapdx_ProcessSession"></a> powerbireportapdx_ProcessSession

One-To-Many Relationship: [powerbireportapdx powerbireportapdx_ProcessSession](powerbireportapdx.md#BKMK_powerbireportapdx_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbireportapdx`|
|ReferencedAttribute|`powerbireportapdxid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbireportapdx`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerfxrule_ProcessSession"></a> powerfxrule_ProcessSession

One-To-Many Relationship: [powerfxrule powerfxrule_ProcessSession](powerfxrule.md#BKMK_powerfxrule_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`powerfxrule`|
|ReferencedAttribute|`powerfxruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerfxrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagecomponent_ProcessSession"></a> powerpagecomponent_ProcessSession

One-To-Many Relationship: [powerpagecomponent powerpagecomponent_ProcessSession](powerpagecomponent.md#BKMK_powerpagecomponent_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagecomponent`|
|ReferencedAttribute|`powerpagecomponentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagecomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesddosalert_ProcessSession"></a> powerpagesddosalert_ProcessSession

One-To-Many Relationship: [powerpagesddosalert powerpagesddosalert_ProcessSession](powerpagesddosalert.md#BKMK_powerpagesddosalert_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesddosalert`|
|ReferencedAttribute|`powerpagesddosalertid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesddosalert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesite_ProcessSession"></a> powerpagesite_ProcessSession

One-To-Many Relationship: [powerpagesite powerpagesite_ProcessSession](powerpagesite.md#BKMK_powerpagesite_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesite`|
|ReferencedAttribute|`powerpagesiteid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesite`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesitelanguage_ProcessSession"></a> powerpagesitelanguage_ProcessSession

One-To-Many Relationship: [powerpagesitelanguage powerpagesitelanguage_ProcessSession](powerpagesitelanguage.md#BKMK_powerpagesitelanguage_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesitelanguage`|
|ReferencedAttribute|`powerpagesitelanguageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesitelanguage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesitepublished_ProcessSession"></a> powerpagesitepublished_ProcessSession

One-To-Many Relationship: [powerpagesitepublished powerpagesitepublished_ProcessSession](powerpagesitepublished.md#BKMK_powerpagesitepublished_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesitepublished`|
|ReferencedAttribute|`powerpagesitepublishedid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesitepublished`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesmanagedidentity_ProcessSession"></a> powerpagesmanagedidentity_ProcessSession

One-To-Many Relationship: [powerpagesmanagedidentity powerpagesmanagedidentity_ProcessSession](powerpagesmanagedidentity.md#BKMK_powerpagesmanagedidentity_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesmanagedidentity`|
|ReferencedAttribute|`powerpagesmanagedidentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesmanagedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesscanreport_ProcessSession"></a> powerpagesscanreport_ProcessSession

One-To-Many Relationship: [powerpagesscanreport powerpagesscanreport_ProcessSession](powerpagesscanreport.md#BKMK_powerpagesscanreport_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesscanreport`|
|ReferencedAttribute|`powerpagesscanreportid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesscanreport`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagessourcefile_ProcessSession"></a> powerpagessourcefile_ProcessSession

One-To-Many Relationship: [powerpagessourcefile powerpagessourcefile_ProcessSession](powerpagessourcefile.md#BKMK_powerpagessourcefile_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagessourcefile`|
|ReferencedAttribute|`powerpagessourcefileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagessourcefile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegecheckerlog_ProcessSession"></a> privilegecheckerlog_ProcessSession

One-To-Many Relationship: [privilegecheckerlog privilegecheckerlog_ProcessSession](privilegecheckerlog.md#BKMK_privilegecheckerlog_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegecheckerlog`|
|ReferencedAttribute|`privilegecheckerlogid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_privilegecheckerlog`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegecheckerrun_ProcessSession"></a> privilegecheckerrun_ProcessSession

One-To-Many Relationship: [privilegecheckerrun privilegecheckerrun_ProcessSession](privilegecheckerrun.md#BKMK_privilegecheckerrun_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegecheckerrun`|
|ReferencedAttribute|`privilegecheckerrunid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_privilegecheckerrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegesremovalsetting_ProcessSession"></a> privilegesremovalsetting_ProcessSession

One-To-Many Relationship: [privilegesremovalsetting privilegesremovalsetting_ProcessSession](privilegesremovalsetting.md#BKMK_privilegesremovalsetting_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegesremovalsetting`|
|ReferencedAttribute|`privilegesremovalsettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_privilegesremovalsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_processstageparameter_ProcessSession"></a> processstageparameter_ProcessSession

One-To-Many Relationship: [processstageparameter processstageparameter_ProcessSession](processstageparameter.md#BKMK_processstageparameter_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`processstageparameter`|
|ReferencedAttribute|`processstageparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_processstageparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_provisionlanguageforuser_ProcessSession"></a> provisionlanguageforuser_ProcessSession

One-To-Many Relationship: [provisionlanguageforuser provisionlanguageforuser_ProcessSession](provisionlanguageforuser.md#BKMK_provisionlanguageforuser_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`provisionlanguageforuser`|
|ReferencedAttribute|`provisionlanguageforuserid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_provisionlanguageforuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_purviewlabelinfo_ProcessSession"></a> purviewlabelinfo_ProcessSession

One-To-Many Relationship: [purviewlabelinfo purviewlabelinfo_ProcessSession](purviewlabelinfo.md#BKMK_purviewlabelinfo_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`purviewlabelinfo`|
|ReferencedAttribute|`purviewlabelinfoid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_purviewlabelinfo`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Queue_ProcessSessions"></a> Queue_ProcessSessions

One-To-Many Relationship: [queue Queue_ProcessSessions](queue.md#BKMK_Queue_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`queue`|
|ReferencedAttribute|`queueid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_queue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_QueueItem_ProcessSessions"></a> QueueItem_ProcessSessions

One-To-Many Relationship: [queueitem QueueItem_ProcessSessions](queueitem.md#BKMK_QueueItem_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`queueitem`|
|ReferencedAttribute|`queueitemid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_queueitem`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recordfilter_ProcessSession"></a> recordfilter_ProcessSession

One-To-Many Relationship: [recordfilter recordfilter_ProcessSession](recordfilter.md#BKMK_recordfilter_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`recordfilter`|
|ReferencedAttribute|`recordfilterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_recordfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_RecurringAppointmentMaster_ProcessSessions"></a> RecurringAppointmentMaster_ProcessSessions

One-To-Many Relationship: [recurringappointmentmaster RecurringAppointmentMaster_ProcessSessions](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`recurringappointmentmaster`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recyclebinconfig_ProcessSession"></a> recyclebinconfig_ProcessSession

One-To-Many Relationship: [recyclebinconfig recyclebinconfig_ProcessSession](recyclebinconfig.md#BKMK_recyclebinconfig_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`recyclebinconfig`|
|ReferencedAttribute|`recyclebinconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_recyclebinconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Report_ProcessSessions"></a> Report_ProcessSessions

One-To-Many Relationship: [report Report_ProcessSessions](report.md#BKMK_Report_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`report`|
|ReferencedAttribute|`reportid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_report`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_reportparameter_ProcessSession"></a> reportparameter_ProcessSession

One-To-Many Relationship: [reportparameter reportparameter_ProcessSession](reportparameter.md#BKMK_reportparameter_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`reportparameter`|
|ReferencedAttribute|`reportparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_reportparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retaineddataexcel_ProcessSession"></a> retaineddataexcel_ProcessSession

One-To-Many Relationship: [retaineddataexcel retaineddataexcel_ProcessSession](retaineddataexcel.md#BKMK_retaineddataexcel_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`retaineddataexcel`|
|ReferencedAttribute|`retaineddataexcelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retaineddataexcel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionconfig_ProcessSession"></a> retentionconfig_ProcessSession

One-To-Many Relationship: [retentionconfig retentionconfig_ProcessSession](retentionconfig.md#BKMK_retentionconfig_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionconfig`|
|ReferencedAttribute|`retentionconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionfailuredetail_ProcessSession"></a> retentionfailuredetail_ProcessSession

One-To-Many Relationship: [retentionfailuredetail retentionfailuredetail_ProcessSession](retentionfailuredetail.md#BKMK_retentionfailuredetail_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionfailuredetail`|
|ReferencedAttribute|`retentionfailuredetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionfailuredetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionoperation_ProcessSession"></a> retentionoperation_ProcessSession

One-To-Many Relationship: [retentionoperation retentionoperation_ProcessSession](retentionoperation.md#BKMK_retentionoperation_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionoperation`|
|ReferencedAttribute|`retentionoperationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionoperationdetail_ProcessSession"></a> retentionoperationdetail_ProcessSession

One-To-Many Relationship: [retentionoperationdetail retentionoperationdetail_ProcessSession](retentionoperationdetail.md#BKMK_retentionoperationdetail_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionoperationdetail`|
|ReferencedAttribute|`retentionoperationdetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionoperationdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionsuccessdetail_ProcessSession"></a> retentionsuccessdetail_ProcessSession

One-To-Many Relationship: [retentionsuccessdetail retentionsuccessdetail_ProcessSession](retentionsuccessdetail.md#BKMK_retentionsuccessdetail_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionsuccessdetail`|
|ReferencedAttribute|`retentionsuccessdetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionsuccessdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_roleeditorlayout_ProcessSession"></a> roleeditorlayout_ProcessSession

One-To-Many Relationship: [roleeditorlayout roleeditorlayout_ProcessSession](roleeditorlayout.md#BKMK_roleeditorlayout_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`roleeditorlayout`|
|ReferencedAttribute|`roleeditorlayoutid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_roleeditorlayout`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_rollupfield_ProcessSessions"></a> rollupfield_ProcessSessions

One-To-Many Relationship: [rollupfield rollupfield_ProcessSessions](rollupfield.md#BKMK_rollupfield_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`rollupfield`|
|ReferencedAttribute|`rollupfieldid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_rollupfield`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sa_suggestedaction_ProcessSession"></a> sa_suggestedaction_ProcessSession

One-To-Many Relationship: [sa_suggestedaction sa_suggestedaction_ProcessSession](sa_suggestedaction.md#BKMK_sa_suggestedaction_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`sa_suggestedaction`|
|ReferencedAttribute|`sa_suggestedactionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sa_suggestedaction`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sa_suggestedactioncriteria_ProcessSession"></a> sa_suggestedactioncriteria_ProcessSession

One-To-Many Relationship: [sa_suggestedactioncriteria sa_suggestedactioncriteria_ProcessSession](sa_suggestedactioncriteria.md#BKMK_sa_suggestedactioncriteria_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`sa_suggestedactioncriteria`|
|ReferencedAttribute|`sa_suggestedactioncriteriaid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sa_suggestedactioncriteria`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_savingrule_ProcessSession"></a> savingrule_ProcessSession

One-To-Many Relationship: [savingrule savingrule_ProcessSession](savingrule.md#BKMK_savingrule_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`savingrule`|
|ReferencedAttribute|`savingruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_savingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchattributesettings_ProcessSession"></a> searchattributesettings_ProcessSession

One-To-Many Relationship: [searchattributesettings searchattributesettings_ProcessSession](searchattributesettings.md#BKMK_searchattributesettings_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`searchattributesettings`|
|ReferencedAttribute|`searchattributesettingsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_searchattributesettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchcustomanalyzer_ProcessSession"></a> searchcustomanalyzer_ProcessSession

One-To-Many Relationship: [searchcustomanalyzer searchcustomanalyzer_ProcessSession](searchcustomanalyzer.md#BKMK_searchcustomanalyzer_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`searchcustomanalyzer`|
|ReferencedAttribute|`searchcustomanalyzerid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_searchcustomanalyzer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchrelationshipsettings_ProcessSession"></a> searchrelationshipsettings_ProcessSession

One-To-Many Relationship: [searchrelationshipsettings searchrelationshipsettings_ProcessSession](searchrelationshipsettings.md#BKMK_searchrelationshipsettings_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`searchrelationshipsettings`|
|ReferencedAttribute|`searchrelationshipsettingsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_searchrelationshipsettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sensitivitylabelattributemapping_ProcessSession"></a> sensitivitylabelattributemapping_ProcessSession

One-To-Many Relationship: [sensitivitylabelattributemapping sensitivitylabelattributemapping_ProcessSession](sensitivitylabelattributemapping.md#BKMK_sensitivitylabelattributemapping_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`sensitivitylabelattributemapping`|
|ReferencedAttribute|`sensitivitylabelattributemappingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sensitivitylabelattributemapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_serviceplan_ProcessSession"></a> serviceplan_ProcessSession

One-To-Many Relationship: [serviceplan serviceplan_ProcessSession](serviceplan.md#BKMK_serviceplan_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`serviceplan`|
|ReferencedAttribute|`serviceplanid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_serviceplan`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_serviceplanmapping_ProcessSession"></a> serviceplanmapping_ProcessSession

One-To-Many Relationship: [serviceplanmapping serviceplanmapping_ProcessSession](serviceplanmapping.md#BKMK_serviceplanmapping_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`serviceplanmapping`|
|ReferencedAttribute|`serviceplanmappingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_serviceplanmapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedlinksetting_ProcessSession"></a> sharedlinksetting_ProcessSession

One-To-Many Relationship: [sharedlinksetting sharedlinksetting_ProcessSession](sharedlinksetting.md#BKMK_sharedlinksetting_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedlinksetting`|
|ReferencedAttribute|`sharedlinksettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharedlinksetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedobject_ProcessSession"></a> sharedobject_ProcessSession

One-To-Many Relationship: [sharedobject sharedobject_ProcessSession](sharedobject.md#BKMK_sharedobject_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedobject`|
|ReferencedAttribute|`sharedobjectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharedobject`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedworkspace_ProcessSession"></a> sharedworkspace_ProcessSession

One-To-Many Relationship: [sharedworkspace sharedworkspace_ProcessSession](sharedworkspace.md#BKMK_sharedworkspace_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedworkspace`|
|ReferencedAttribute|`sharedworkspaceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharedworkspace`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedworkspacepool_ProcessSession"></a> sharedworkspacepool_ProcessSession

One-To-Many Relationship: [sharedworkspacepool sharedworkspacepool_ProcessSession](sharedworkspacepool.md#BKMK_sharedworkspacepool_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedworkspacepool`|
|ReferencedAttribute|`sharedworkspacepoolid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharedworkspacepool`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SharePointDocumentLocation_ProcessSessions"></a> SharePointDocumentLocation_ProcessSessions

One-To-Many Relationship: [sharepointdocumentlocation SharePointDocumentLocation_ProcessSessions](sharepointdocumentlocation.md#BKMK_SharePointDocumentLocation_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`sharepointdocumentlocation`|
|ReferencedAttribute|`sharepointdocumentlocationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharepointdocumentlocation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharepointmanagedidentity_ProcessSession"></a> sharepointmanagedidentity_ProcessSession

One-To-Many Relationship: [sharepointmanagedidentity sharepointmanagedidentity_ProcessSession](sharepointmanagedidentity.md#BKMK_sharepointmanagedidentity_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`sharepointmanagedidentity`|
|ReferencedAttribute|`sharepointmanagedidentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharepointmanagedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SharePointSite_ProcessSessions"></a> SharePointSite_ProcessSessions

One-To-Many Relationship: [sharepointsite SharePointSite_ProcessSessions](sharepointsite.md#BKMK_SharePointSite_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`sharepointsite`|
|ReferencedAttribute|`sharepointsiteid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharepointsite`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sideloadedaiplugin_ProcessSession"></a> sideloadedaiplugin_ProcessSession

One-To-Many Relationship: [sideloadedaiplugin sideloadedaiplugin_ProcessSession](sideloadedaiplugin.md#BKMK_sideloadedaiplugin_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`sideloadedaiplugin`|
|ReferencedAttribute|`sideloadedaipluginid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sideloadedaiplugin`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_slabase_ProcessSessions"></a> slabase_ProcessSessions

One-To-Many Relationship: [sla slabase_ProcessSessions](sla.md#BKMK_slabase_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`sla`|
|ReferencedAttribute|`slaid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sla`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SocialActivity_ProcessSessions"></a> SocialActivity_ProcessSessions

One-To-Many Relationship: [socialactivity SocialActivity_ProcessSessions](socialactivity.md#BKMK_SocialActivity_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`socialactivity`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_socialactivity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SocialProfile_ProcessSessions"></a> SocialProfile_ProcessSessions

One-To-Many Relationship: [socialprofile SocialProfile_ProcessSessions](socialprofile.md#BKMK_SocialProfile_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`socialprofile`|
|ReferencedAttribute|`socialprofileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_socialprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentattributeconfiguration_ProcessSession"></a> solutioncomponentattributeconfiguration_ProcessSession

One-To-Many Relationship: [solutioncomponentattributeconfiguration solutioncomponentattributeconfiguration_ProcessSession](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentattributeconfiguration`|
|ReferencedAttribute|`solutioncomponentattributeconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_solutioncomponentattributeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentbatchconfiguration_ProcessSession"></a> solutioncomponentbatchconfiguration_ProcessSession

One-To-Many Relationship: [solutioncomponentbatchconfiguration solutioncomponentbatchconfiguration_ProcessSession](solutioncomponentbatchconfiguration.md#BKMK_solutioncomponentbatchconfiguration_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentbatchconfiguration`|
|ReferencedAttribute|`solutioncomponentbatchconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_solutioncomponentbatchconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentconfiguration_ProcessSession"></a> solutioncomponentconfiguration_ProcessSession

One-To-Many Relationship: [solutioncomponentconfiguration solutioncomponentconfiguration_ProcessSession](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentconfiguration`|
|ReferencedAttribute|`solutioncomponentconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_solutioncomponentconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentrelationshipconfiguration_ProcessSession"></a> solutioncomponentrelationshipconfiguration_ProcessSession

One-To-Many Relationship: [solutioncomponentrelationshipconfiguration solutioncomponentrelationshipconfiguration_ProcessSession](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentrelationshipconfiguration`|
|ReferencedAttribute|`solutioncomponentrelationshipconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_solutioncomponentrelationshipconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagedentity_ProcessSession"></a> stagedentity_ProcessSession

One-To-Many Relationship: [stagedentity stagedentity_ProcessSession](stagedentity.md#BKMK_stagedentity_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`stagedentity`|
|ReferencedAttribute|`stagedentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_stagedentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagedentityattribute_ProcessSession"></a> stagedentityattribute_ProcessSession

One-To-Many Relationship: [stagedentityattribute stagedentityattribute_ProcessSession](stagedentityattribute.md#BKMK_stagedentityattribute_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`stagedentityattribute`|
|ReferencedAttribute|`stagedentityattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_stagedentityattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagedmetadataasyncoperation_ProcessSession"></a> stagedmetadataasyncoperation_ProcessSession

One-To-Many Relationship: [stagedmetadataasyncoperation stagedmetadataasyncoperation_ProcessSession](stagedmetadataasyncoperation.md#BKMK_stagedmetadataasyncoperation_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`stagedmetadataasyncoperation`|
|ReferencedAttribute|`stagedmetadataasyncoperationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_stagedmetadataasyncoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagesolutionupload_ProcessSession"></a> stagesolutionupload_ProcessSession

One-To-Many Relationship: [stagesolutionupload stagesolutionupload_ProcessSession](stagesolutionupload.md#BKMK_stagesolutionupload_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`stagesolutionupload`|
|ReferencedAttribute|`stagesolutionuploadid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_stagesolutionupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Subject_ProcessSessions"></a> Subject_ProcessSessions

One-To-Many Relationship: [subject Subject_ProcessSessions](subject.md#BKMK_Subject_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`subject`|
|ReferencedAttribute|`subjectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_subject`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_supportusertable_ProcessSession"></a> supportusertable_ProcessSession

One-To-Many Relationship: [supportusertable supportusertable_ProcessSession](supportusertable.md#BKMK_supportusertable_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`supportusertable`|
|ReferencedAttribute|`supportusertableid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_supportusertable`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapsedatabase_ProcessSession"></a> synapsedatabase_ProcessSession

One-To-Many Relationship: [synapsedatabase synapsedatabase_ProcessSession](synapsedatabase.md#BKMK_synapsedatabase_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`synapsedatabase`|
|ReferencedAttribute|`synapsedatabaseid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapsedatabase`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkexternaltablestate_ProcessSession"></a> synapselinkexternaltablestate_ProcessSession

One-To-Many Relationship: [synapselinkexternaltablestate synapselinkexternaltablestate_ProcessSession](synapselinkexternaltablestate.md#BKMK_synapselinkexternaltablestate_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkexternaltablestate`|
|ReferencedAttribute|`synapselinkexternaltablestateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkexternaltablestate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofile_ProcessSession"></a> synapselinkprofile_ProcessSession

One-To-Many Relationship: [synapselinkprofile synapselinkprofile_ProcessSession](synapselinkprofile.md#BKMK_synapselinkprofile_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofile`|
|ReferencedAttribute|`synapselinkprofileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofileentity_ProcessSession"></a> synapselinkprofileentity_ProcessSession

One-To-Many Relationship: [synapselinkprofileentity synapselinkprofileentity_ProcessSession](synapselinkprofileentity.md#BKMK_synapselinkprofileentity_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofileentity`|
|ReferencedAttribute|`synapselinkprofileentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkprofileentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofileentitystate_ProcessSession"></a> synapselinkprofileentitystate_ProcessSession

One-To-Many Relationship: [synapselinkprofileentitystate synapselinkprofileentitystate_ProcessSession](synapselinkprofileentitystate.md#BKMK_synapselinkprofileentitystate_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofileentitystate`|
|ReferencedAttribute|`synapselinkprofileentitystateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkprofileentitystate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkschedule_ProcessSession"></a> synapselinkschedule_ProcessSession

One-To-Many Relationship: [synapselinkschedule synapselinkschedule_ProcessSession](synapselinkschedule.md#BKMK_synapselinkschedule_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkschedule`|
|ReferencedAttribute|`synapselinkscheduleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkschedule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SystemUser_ProcessSessions"></a> SystemUser_ProcessSessions

One-To-Many Relationship: [systemuser SystemUser_ProcessSessions](systemuser.md#BKMK_SystemUser_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_systemuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_systemuserauthorizationchangetracker_ProcessSession"></a> systemuserauthorizationchangetracker_ProcessSession

One-To-Many Relationship: [systemuserauthorizationchangetracker systemuserauthorizationchangetracker_ProcessSession](systemuserauthorizationchangetracker.md#BKMK_systemuserauthorizationchangetracker_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuserauthorizationchangetracker`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_systemuserauthorizationchangetracker`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_tag_ProcessSession"></a> tag_ProcessSession

One-To-Many Relationship: [tag tag_ProcessSession](tag.md#BKMK_tag_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`tag`|
|ReferencedAttribute|`tagid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_tag`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_taggedflowsession_ProcessSession"></a> taggedflowsession_ProcessSession

One-To-Many Relationship: [taggedflowsession taggedflowsession_ProcessSession](taggedflowsession.md#BKMK_taggedflowsession_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`taggedflowsession`|
|ReferencedAttribute|`taggedflowsessionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_taggedflowsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_taggedprocess_ProcessSession"></a> taggedprocess_ProcessSession

One-To-Many Relationship: [taggedprocess taggedprocess_ProcessSession](taggedprocess.md#BKMK_taggedprocess_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`taggedprocess`|
|ReferencedAttribute|`taggedprocessid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_taggedprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Task_ProcessSessions"></a> Task_ProcessSessions

One-To-Many Relationship: [task Task_ProcessSessions](task.md#BKMK_Task_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`task`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_task`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_processsession"></a> team_processsession

One-To-Many Relationship: [team team_processsession](team.md#BKMK_team_processsession)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Team_ProcessSessions"></a> Team_ProcessSessions

One-To-Many Relationship: [team Team_ProcessSessions](team.md#BKMK_Team_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_team`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_teammobileofflineprofilemembership_ProcessSession"></a> teammobileofflineprofilemembership_ProcessSession

One-To-Many Relationship: [teammobileofflineprofilemembership teammobileofflineprofilemembership_ProcessSession](teammobileofflineprofilemembership.md#BKMK_teammobileofflineprofilemembership_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`teammobileofflineprofilemembership`|
|ReferencedAttribute|`teammobileofflineprofilemembershipid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_teammobileofflineprofilemembership`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Template_ProcessSessions"></a> Template_ProcessSessions

One-To-Many Relationship: [template Template_ProcessSessions](template.md#BKMK_Template_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`template`|
|ReferencedAttribute|`templateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_template`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Territory_ProcessSessions"></a> Territory_ProcessSessions

One-To-Many Relationship: [territory Territory_ProcessSessions](territory.md#BKMK_Territory_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`territory`|
|ReferencedAttribute|`territoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_territory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_theme_ProcessSession"></a> theme_ProcessSession

One-To-Many Relationship: [theme theme_ProcessSession](theme.md#BKMK_theme_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`theme`|
|ReferencedAttribute|`themeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_theme`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_ProcessSessions"></a> TransactionCurrency_ProcessSessions

One-To-Many Relationship: [transactioncurrency TransactionCurrency_ProcessSessions](transactioncurrency.md#BKMK_TransactionCurrency_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_transactioncurrency`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TranslationProcess_ProcessSessions"></a> TranslationProcess_ProcessSessions

One-To-Many Relationship: [translationprocess TranslationProcess_ProcessSessions](translationprocess.md#BKMK_TranslationProcess_ProcessSessions)

|Property|Value|
|---|---|
|ReferencedEntity|`translationprocess`|
|ReferencedAttribute|`businessprocessflowinstanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_translationprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_unstructuredfilesearchentity_ProcessSession"></a> unstructuredfilesearchentity_ProcessSession

One-To-Many Relationship: [unstructuredfilesearchentity unstructuredfilesearchentity_ProcessSession](unstructuredfilesearchentity.md#BKMK_unstructuredfilesearchentity_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`unstructuredfilesearchentity`|
|ReferencedAttribute|`unstructuredfilesearchentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_unstructuredfilesearchentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_unstructuredfilesearchrecord_ProcessSession"></a> unstructuredfilesearchrecord_ProcessSession

One-To-Many Relationship: [unstructuredfilesearchrecord unstructuredfilesearchrecord_ProcessSession](unstructuredfilesearchrecord.md#BKMK_unstructuredfilesearchrecord_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`unstructuredfilesearchrecord`|
|ReferencedAttribute|`unstructuredfilesearchrecordid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_unstructuredfilesearchrecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_usermapping_ProcessSession"></a> usermapping_ProcessSession

One-To-Many Relationship: [usermapping usermapping_ProcessSession](usermapping.md#BKMK_usermapping_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`usermapping`|
|ReferencedAttribute|`usermappingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_usermapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_usermobileofflineprofilemembership_ProcessSession"></a> usermobileofflineprofilemembership_ProcessSession

One-To-Many Relationship: [usermobileofflineprofilemembership usermobileofflineprofilemembership_ProcessSession](usermobileofflineprofilemembership.md#BKMK_usermobileofflineprofilemembership_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`usermobileofflineprofilemembership`|
|ReferencedAttribute|`usermobileofflineprofilemembershipid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_usermobileofflineprofilemembership`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_userrating_ProcessSession"></a> userrating_ProcessSession

One-To-Many Relationship: [userrating userrating_ProcessSession](userrating.md#BKMK_userrating_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`userrating`|
|ReferencedAttribute|`userratingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_userrating`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_viewasexamplequestion_ProcessSession"></a> viewasexamplequestion_ProcessSession

One-To-Many Relationship: [viewasexamplequestion viewasexamplequestion_ProcessSession](viewasexamplequestion.md#BKMK_viewasexamplequestion_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`viewasexamplequestion`|
|ReferencedAttribute|`viewasexamplequestionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_viewasexamplequestion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_virtualentitymetadata_ProcessSession"></a> virtualentitymetadata_ProcessSession

One-To-Many Relationship: [virtualentitymetadata virtualentitymetadata_ProcessSession](virtualentitymetadata.md#BKMK_virtualentitymetadata_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`virtualentitymetadata`|
|ReferencedAttribute|`virtualentitymetadataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_virtualentitymetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflowbinary_ProcessSession"></a> workflowbinary_ProcessSession

One-To-Many Relationship: [workflowbinary workflowbinary_ProcessSession](workflowbinary.md#BKMK_workflowbinary_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`workflowbinary`|
|ReferencedAttribute|`workflowbinaryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_workflowbinary`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflowmetadata_ProcessSession"></a> workflowmetadata_ProcessSession

One-To-Many Relationship: [workflowmetadata workflowmetadata_ProcessSession](workflowmetadata.md#BKMK_workflowmetadata_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`workflowmetadata`|
|ReferencedAttribute|`workflowmetadataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_workflowmetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workqueue_ProcessSession"></a> workqueue_ProcessSession

One-To-Many Relationship: [workqueue workqueue_ProcessSession](workqueue.md#BKMK_workqueue_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`workqueue`|
|ReferencedAttribute|`workqueueid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_workqueue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workqueueitem_ProcessSession"></a> workqueueitem_ProcessSession

One-To-Many Relationship: [workqueueitem workqueueitem_ProcessSession](workqueueitem.md#BKMK_workqueueitem_ProcessSession)

|Property|Value|
|---|---|
|ReferencedEntity|`workqueueitem`|
|ReferencedAttribute|`workqueueitemid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_workqueueitem`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [lk_processsession_nextlinkedsessionid](#BKMK_lk_processsession_nextlinkedsessionid-one-to-many)
- [lk_processsession_originatingsessionid](#BKMK_lk_processsession_originatingsessionid-one-to-many)
- [lk_processsession_previouslinkedsessionid](#BKMK_lk_processsession_previouslinkedsessionid-one-to-many)
- [lk_workflowlog_processsession](#BKMK_lk_workflowlog_processsession)
- [lk_workflowlog_processsession_childworkflow](#BKMK_lk_workflowlog_processsession_childworkflow)
- [processsession_connections1](#BKMK_processsession_connections1)
- [processsession_connections2](#BKMK_processsession_connections2)
- [processsession_PostFollows](#BKMK_processsession_PostFollows)
- [processsession_PostRegardings](#BKMK_processsession_PostRegardings)
- [ProcessSession_SyncErrors](#BKMK_ProcessSession_SyncErrors)

### <a name="BKMK_lk_processsession_nextlinkedsessionid-one-to-many"></a> lk_processsession_nextlinkedsessionid

Many-To-One Relationship: [processsession lk_processsession_nextlinkedsessionid](#BKMK_lk_processsession_nextlinkedsessionid-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`nextlinkedsessionid`|
|ReferencedEntityNavigationPropertyName|`lk_processsession_nextlinkedsessionid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_processsession_originatingsessionid-one-to-many"></a> lk_processsession_originatingsessionid

Many-To-One Relationship: [processsession lk_processsession_originatingsessionid](#BKMK_lk_processsession_originatingsessionid-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`originatingsessionid`|
|ReferencedEntityNavigationPropertyName|`lk_processsession_originatingsessionid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_processsession_previouslinkedsessionid-one-to-many"></a> lk_processsession_previouslinkedsessionid

Many-To-One Relationship: [processsession lk_processsession_previouslinkedsessionid](#BKMK_lk_processsession_previouslinkedsessionid-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`previouslinkedsessionid`|
|ReferencedEntityNavigationPropertyName|`lk_processsession_previouslinkedsessionid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_workflowlog_processsession"></a> lk_workflowlog_processsession

Many-To-One Relationship: [workflowlog lk_workflowlog_processsession](workflowlog.md#BKMK_lk_workflowlog_processsession)

|Property|Value|
|---|---|
|ReferencingEntity|`workflowlog`|
|ReferencingAttribute|`asyncoperationid`|
|ReferencedEntityNavigationPropertyName|`lk_workflowlog_processsession`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_workflowlog_processsession_childworkflow"></a> lk_workflowlog_processsession_childworkflow

Many-To-One Relationship: [workflowlog lk_workflowlog_processsession_childworkflow](workflowlog.md#BKMK_lk_workflowlog_processsession_childworkflow)

|Property|Value|
|---|---|
|ReferencingEntity|`workflowlog`|
|ReferencingAttribute|`childworkflowinstanceid`|
|ReferencedEntityNavigationPropertyName|`lk_workflowlog_processsession_childworkflow`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_processsession_connections1"></a> processsession_connections1

Many-To-One Relationship: [connection processsession_connections1](connection.md#BKMK_processsession_connections1)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record1id`|
|ReferencedEntityNavigationPropertyName|`processsession_connections1`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_processsession_connections2"></a> processsession_connections2

Many-To-One Relationship: [connection processsession_connections2](connection.md#BKMK_processsession_connections2)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record2id`|
|ReferencedEntityNavigationPropertyName|`processsession_connections2`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_processsession_PostFollows"></a> processsession_PostFollows

Many-To-One Relationship: [postfollow processsession_PostFollows](postfollow.md#BKMK_processsession_PostFollows)

|Property|Value|
|---|---|
|ReferencingEntity|`postfollow`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`processsession_PostFollows`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_processsession_PostRegardings"></a> processsession_PostRegardings

Many-To-One Relationship: [postregarding processsession_PostRegardings](postregarding.md#BKMK_processsession_PostRegardings)

|Property|Value|
|---|---|
|ReferencingEntity|`postregarding`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`processsession_PostRegardings`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_ProcessSession_SyncErrors"></a> ProcessSession_SyncErrors

Many-To-One Relationship: [syncerror ProcessSession_SyncErrors](syncerror.md#BKMK_ProcessSession_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`ProcessSession_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.processsession?displayProperty=fullName>
