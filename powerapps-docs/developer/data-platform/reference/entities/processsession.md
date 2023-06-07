---
title: "ProcessSession table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the ProcessSession table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# ProcessSession table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Information that is generated when a dialog is run. Every time that you run a dialog, a dialog session is created.


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /processsessions(*processsessionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST /processsessions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE /processsessions(*processsessionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET /processsessions(*processsessionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /processsessions<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH /processsessions(*processsessionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /processsessions(*processsessionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|ProcessSession|
|DisplayCollectionName|Process Sessions|
|DisplayName|Process Session|
|EntitySetName|processsessions|
|IsBPFEntity|False|
|LogicalCollectionName|processsessions|
|LogicalName|processsession|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|processsessionid|
|PrimaryNameAttribute|name|
|SchemaName|ProcessSession|

<a name="writable-attributes"></a>

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
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectIdYomiName](#BKMK_RegardingObjectIdYomiName)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [StartedOn](#BKMK_StartedOn)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [StepName](#BKMK_StepName)


### <a name="BKMK_ActivityName"></a> ActivityName

|Property|Value|
|--------|-----|
|Description|Name of the activity that is being executed.|
|DisplayName|Activity Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|activityname|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CanceledOn"></a> CanceledOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the dialog session was canceled.|
|DisplayName|Canceled On|
|Format|DateAndTime|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|canceledon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_Comments"></a> Comments

|Property|Value|
|--------|-----|
|Description|User comments.|
|DisplayName|Comments|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|comments|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_CompletedOn"></a> CompletedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the dialog session was completed.|
|DisplayName|Completed On|
|Format|DateAndTime|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|completedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ErrorCode"></a> ErrorCode

|Property|Value|
|--------|-----|
|Description|Error code related to the dialog session.|
|DisplayName|Error Code|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|errorcode|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ExecutedBy"></a> ExecutedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who ran the dialog process.|
|DisplayName|Executed By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|executedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_InputArguments"></a> InputArguments

|Property|Value|
|--------|-----|
|Description|Input arguments for the child dialog process.|
|DisplayName|Input Arguments|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|inputarguments|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of the dialog session.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_NextLinkedSessionId"></a> NextLinkedSessionId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the succeeding linked dialog session.|
|DisplayName|Next Linked Session|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|nextlinkedsessionid|
|RequiredLevel|None|
|Targets|processsession|
|Type|Lookup|


### <a name="BKMK_OriginatingSessionId"></a> OriginatingSessionId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the originating dialog session.|
|DisplayName|Originating Session|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|originatingsessionid|
|RequiredLevel|None|
|Targets|processsession|
|Type|Lookup|


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user or team who owns the dialog session.|
|DisplayName|Owner|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
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


### <a name="BKMK_PreviousLinkedSessionId"></a> PreviousLinkedSessionId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the preceding linked dialog session.|
|DisplayName|Previous Linked Session|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|previouslinkedsessionid|
|RequiredLevel|None|
|Targets|processsession|
|Type|Lookup|


### <a name="BKMK_ProcessId"></a> ProcessId

|Property|Value|
|--------|-----|
|Description|Select the process activation record that is related to the dialog session.|
|DisplayName|Process|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|processid|
|RequiredLevel|None|
|Targets|workflow|
|Type|Lookup|


### <a name="BKMK_ProcessSessionId"></a> ProcessSessionId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the dialog session.|
|DisplayName|Dialog Session|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|processsessionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ProcessStageName"></a> ProcessStageName

|Property|Value|
|--------|-----|
|Description|Name of the dialog stage.|
|DisplayName|Dialog Stage|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|processstagename|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ProcessState"></a> ProcessState

|Property|Value|
|--------|-----|
|Description|State of the dialog process.|
|DisplayName|Process State|
|FormatName|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|processstate|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the object with which the dialog session is associated.|
|DisplayName|Regarding|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|regardingobjectid|
|RequiredLevel|None|
|Targets|account,activityfileattachment,annotation,appaction,appactionmigration,appactionrule,appelement,applicationuser,appmodulecomponentedge,appmodulecomponentnode,appointment,appsetting,appusersetting,archivecleanupinfo,archivecleanupoperation,bot,botcomponent,bulkarchiveconfig,bulkarchivefailuredetail,bulkarchiveoperation,bulkarchiveoperationdetail,businessunit,businessunitnewsarticle,canvasappextendedmetadata,card,cascadegrantrevokeaccessrecordstracker,cascadegrantrevokeaccessversiontracker,catalog,catalogassignment,channelaccessprofile,channelaccessprofilerule,chat,comment,connection,connectioninstance,connectionreference,connectionrole,connector,contact,conversationtranscript,convertrule,customapi,customapirequestparameter,customapiresponseproperty,customeraddress,customerrelationship,datalakefolder,datalakefolderpermission,datalakeworkspace,datalakeworkspacepermission,dataprocessingconfiguration,delegatedauthorization,desktopflowbinary,desktopflowmodule,email,enablearchivalrequest,entityrecordfilter,environmentvariabledefinition,environmentvariablevalue,expiredprocess,exportedexcel,exportsolutionupload,externalparty,externalpartyitem,fax,featurecontrolsetting,flowmachine,flowmachinegroup,flowmachineimage,flowmachineimageversion,flowmachinenetwork,fxexpression,goal,goalrollupquery,holidaywrapper,internalcatalogassignment,kbarticle,kbarticlecomment,kbarticletemplate,keyvaultreference,knowledgearticle,knowledgebaserecord,letter,mailbox,mailmergetemplate,managedidentity,metadataforarchival,metric,mobileofflineprofileextension,msdynce_botcontent,msdyn_aibdataset,msdyn_aibdatasetfile,msdyn_aibdatasetrecord,msdyn_aibdatasetscontainer,msdyn_aibfeedbackloop,msdyn_aibfile,msdyn_aibfileattacheddata,msdyn_aiconfiguration,msdyn_aievent,msdyn_aifptrainingdocument,msdyn_aimodel,msdyn_aiodimage,msdyn_aiodlabel,msdyn_aiodtrainingboundingbox,msdyn_aiodtrainingimage,msdyn_aitemplate,msdyn_analysiscomponent,msdyn_analysisjob,msdyn_analysisoverride,msdyn_analysisresult,msdyn_analysisresultdetail,msdyn_appinsightsmetadata,msdyn_customcontrolextendedsettings,msdyn_dataflow,msdyn_dataflowrefreshhistory,msdyn_dataflowtemplate,msdyn_dataflow_datalakefolder,msdyn_dmsrequest,msdyn_dmsrequeststatus,msdyn_entitylinkchatconfiguration,msdyn_entityrefreshhistory,msdyn_favoriteknowledgearticle,msdyn_federatedarticle,msdyn_federatedarticleincident,msdyn_fileupload,msdyn_helppage,msdyn_insightsstorevirtualentity,msdyn_integratedsearchprovider,msdyn_kalanguagesetting,msdyn_kbattachment,msdyn_kmfederatedsearchconfig,msdyn_kmpersonalizationsetting,msdyn_knowledgearticleimage,msdyn_knowledgearticletemplate,msdyn_knowledgeconfiguration,msdyn_knowledgeinteractioninsight,msdyn_knowledgemanagementsetting,msdyn_knowledgepersonalfilter,msdyn_knowledgesearchfilter,msdyn_knowledgesearchinsight,msdyn_mobileapp,msdyn_pmanalysishistory,msdyn_pmcalendar,msdyn_pmcalendarversion,msdyn_pminferredtask,msdyn_pmprocessextendedmetadataversion,msdyn_pmprocesstemplate,msdyn_pmprocessusersettings,msdyn_pmprocessversion,msdyn_pmrecording,msdyn_pmtemplate,msdyn_pmview,msdyn_richtextfile,msdyn_schedule,msdyn_serviceconfiguration,msdyn_slakpi,msdyn_solutionhealthrule,msdyn_solutionhealthruleargument,msdyn_solutionhealthruleset,msdyn_tour,msdyn_virtualtablecolumncandidate,msdyn_workflowactionstatus,msgraphresourcetosubscription,mspcat_catalogsubmissionfiles,mspcat_packagestore,newprocess,organizationdatasyncfnostate,organizationdatasyncstate,organizationdatasyncsubscription,organizationdatasyncsubscriptionentity,organizationdatasyncsubscriptionfnotable,organizationsetting,package,pdfsetting,phonecall,position,powerbidataset,powerbimashupparameter,powerbireport,powerfxrule,privilegesremovalsetting,processstageparameter,provisionlanguageforuser,queue,queueitem,reconciliationentityinfo,reconciliationinfo,recordfilter,recurringappointmentmaster,relationshiprole,report,retaineddataexcel,retentioncleanupinfo,retentioncleanupoperation,retentionconfig,retentionfailuredetail,retentionoperation,retentionoperationdetail,revokeinheritedaccessrecordstracker,roleeditorlayout,rollupfield,routingrule,routingruleitem,searchattributesettings,searchcustomanalyzer,searchrelationshipsettings,serviceplan,serviceplanmapping,settingdefinition,sharedlinksetting,sharedobject,sharedworkspace,sharedworkspacepool,sharepointdocumentlocation,sharepointsite,sla,socialactivity,socialprofile,solutioncomponentattributeconfiguration,solutioncomponentbatchconfiguration,solutioncomponentconfiguration,solutioncomponentrelationshipconfiguration,stagedentity,stagedentityattribute,stagesolutionupload,subject,supportusertable,synapsedatabase,synapselinkexternaltablestate,synapselinkprofile,synapselinkprofileentity,synapselinkprofileentitystate,synapselinkschedule,systemuser,systemuserauthorizationchangetracker,task,tdsmetadata,team,teammobileofflineprofilemembership,template,territory,theme,transactioncurrency,translationprocess,usermapping,usermobileofflineprofilemembership,userrating,virtualentitymetadata,workflowbinary,workqueue,workqueueitem|
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
|IsValidForUpdate|False|
|LogicalName|regardingobjectidname|
|MaxLength|850|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|regardingobjecttypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_StartedOn"></a> StartedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the dialog session was started.|
|DisplayName|Started On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|startedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|--------|-----|
|Description|Status of the dialog session.|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### StateCode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Incomplete|1|Incomplete|
|1|Complete|2|Complete|



### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the dialog session.|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### StatusCode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Not Started|0|
|2|In Progress|0|
|3|Paused|0|
|4|Completed|1|
|5|Canceled|1|
|6|Failed|1|



### <a name="BKMK_StepName"></a> StepName

|Property|Value|
|--------|-----|
|Description|Name of the dialog step.|
|DisplayName|Step Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|stepname|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CanceledBy](#BKMK_CanceledBy)
- [CanceledByName](#BKMK_CanceledByName)
- [CanceledByYomiName](#BKMK_CanceledByYomiName)
- [CompletedBy](#BKMK_CompletedBy)
- [CompletedByName](#BKMK_CompletedByName)
- [CompletedByYomiName](#BKMK_CompletedByYomiName)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ExecutedByName](#BKMK_ExecutedByName)
- [ExecutedByYomiName](#BKMK_ExecutedByYomiName)
- [ExecutedOn](#BKMK_ExecutedOn)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [NextLinkedSessionIdName](#BKMK_NextLinkedSessionIdName)
- [OriginatingSessionIdName](#BKMK_OriginatingSessionIdName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [PreviousLinkedSessionIdName](#BKMK_PreviousLinkedSessionIdName)
- [ProcessIdName](#BKMK_ProcessIdName)
- [ProtectionKey](#BKMK_ProtectionKey)
- [StartedBy](#BKMK_StartedBy)
- [StartedByName](#BKMK_StartedByName)
- [StartedByYomiName](#BKMK_StartedByYomiName)


### <a name="BKMK_CanceledBy"></a> CanceledBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who canceled the dialog session.|
|DisplayName|Canceled By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|canceledby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CanceledByName"></a> CanceledByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|canceledbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CanceledByYomiName"></a> CanceledByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|canceledbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CompletedBy"></a> CompletedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who completed the dialog session.|
|DisplayName|Completed By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|completedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CompletedByName"></a> CompletedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|completedbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CompletedByYomiName"></a> CompletedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|completedbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who started the dialog session.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the dialog session was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the dialog session.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ExecutedByName"></a> ExecutedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|executedbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ExecutedByYomiName"></a> ExecutedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|executedbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ExecutedOn"></a> ExecutedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the dialog process was run.|
|DisplayName|Executed On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|executedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the dialog session.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the dialog session was last modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the dialog session.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_NextLinkedSessionIdName"></a> NextLinkedSessionIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|nextlinkedsessionidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OriginatingSessionIdName"></a> OriginatingSessionIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|originatingsessionidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|--------|-----|
|Description|Unique identifier of the business unit that owns the dialog session.|
|DisplayName|Owning Business Unit|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningBusinessUnitName"></a> OwningBusinessUnitName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunitname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|--------|-----|
|Description|Unique identifier of the team who owns the dialog session.|
|DisplayName|Owning Team|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteam|
|RequiredLevel|None|
|Targets|team|
|Type|Lookup|


### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who owns the dialog session.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_PreviousLinkedSessionIdName"></a> PreviousLinkedSessionIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|previouslinkedsessionidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ProcessIdName"></a> ProcessIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|processidname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ProtectionKey"></a> ProtectionKey

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Protection Key|
|FormatName|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|protectionkey|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_StartedBy"></a> StartedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who started the dialog session.|
|DisplayName|Started By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|startedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_StartedByName"></a> StartedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|startedbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_StartedByYomiName"></a> StartedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|startedbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [lk_workflowlog_processsession](#BKMK_lk_workflowlog_processsession)
- [lk_workflowlog_processsession_childworkflow](#BKMK_lk_workflowlog_processsession_childworkflow)
- [lk_processsession_previouslinkedsessionid](#BKMK_lk_processsession_previouslinkedsessionid)
- [lk_processsession_nextlinkedsessionid](#BKMK_lk_processsession_nextlinkedsessionid)
- [lk_processsession_originatingsessionid](#BKMK_lk_processsession_originatingsessionid)
- [processsession_connections2](#BKMK_processsession_connections2)
- [ProcessSession_SyncErrors](#BKMK_ProcessSession_SyncErrors)
- [processsession_connections1](#BKMK_processsession_connections1)
- [processsession_PostFollows](#BKMK_processsession_PostFollows)


### <a name="BKMK_lk_workflowlog_processsession"></a> lk_workflowlog_processsession

Same as the [lk_workflowlog_processsession](workflowlog.md#BKMK_lk_workflowlog_processsession) many-to-one relationship for the [workflowlog](workflowlog.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflowlog|
|ReferencingAttribute|asyncoperationid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_workflowlog_processsession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_lk_workflowlog_processsession_childworkflow"></a> lk_workflowlog_processsession_childworkflow

Same as the [lk_workflowlog_processsession_childworkflow](workflowlog.md#BKMK_lk_workflowlog_processsession_childworkflow) many-to-one relationship for the [workflowlog](workflowlog.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflowlog|
|ReferencingAttribute|childworkflowinstanceid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_workflowlog_processsession_childworkflow|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_processsession_previouslinkedsessionid"></a> lk_processsession_previouslinkedsessionid

Same as the [lk_processsession_previouslinkedsessionid](processsession.md#BKMK_lk_processsession_previouslinkedsessionid) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|previouslinkedsessionid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_processsession_previouslinkedsessionid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_processsession_nextlinkedsessionid"></a> lk_processsession_nextlinkedsessionid

Same as the [lk_processsession_nextlinkedsessionid](processsession.md#BKMK_lk_processsession_nextlinkedsessionid) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|nextlinkedsessionid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_processsession_nextlinkedsessionid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_processsession_originatingsessionid"></a> lk_processsession_originatingsessionid

Same as the [lk_processsession_originatingsessionid](processsession.md#BKMK_lk_processsession_originatingsessionid) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|originatingsessionid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_processsession_originatingsessionid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_processsession_connections2"></a> processsession_connections2

Same as the [processsession_connections2](connection.md#BKMK_processsession_connections2) many-to-one relationship for the [connection](connection.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record2id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|processsession_connections2|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_ProcessSession_SyncErrors"></a> ProcessSession_SyncErrors

Same as the [ProcessSession_SyncErrors](syncerror.md#BKMK_ProcessSession_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|ProcessSession_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_processsession_connections1"></a> processsession_connections1

Same as the [processsession_connections1](connection.md#BKMK_processsession_connections1) many-to-one relationship for the [connection](connection.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record1id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|processsession_connections1|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_processsession_PostFollows"></a> processsession_PostFollows

Same as the [processsession_PostFollows](postfollow.md#BKMK_processsession_PostFollows) many-to-one relationship for the [postfollow](postfollow.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|postfollow|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|processsession_PostFollows|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [theme_ProcessSession](#BKMK_theme_ProcessSession)
- [usermapping_ProcessSession](#BKMK_usermapping_ProcessSession)
- [knowledgearticle_ProcessSession](#BKMK_knowledgearticle_ProcessSession)
- [position_ProcessSession](#BKMK_position_ProcessSession)
- [KnowledgeBaseRecord_ProcessSession](#BKMK_KnowledgeBaseRecord_ProcessSession)
- [SharePointSite_ProcessSessions](#BKMK_SharePointSite_ProcessSessions)
- [MailMergeTemplate_ProcessSessions](#BKMK_MailMergeTemplate_ProcessSessions)
- [Annotation_ProcessSessions](#BKMK_Annotation_ProcessSessions)
- [BusinessUnitNewsArticle_ProcessSessions](#BKMK_BusinessUnitNewsArticle_ProcessSessions)
- [Appointment_ProcessSessions](#BKMK_Appointment_ProcessSessions)
- [QueueItem_ProcessSessions](#BKMK_QueueItem_ProcessSessions)
- [lk_processsession_previouslinkedsessionid](#BKMK_lk_processsession_previouslinkedsessionid)
- [lk_processsession_nextlinkedsessionid](#BKMK_lk_processsession_nextlinkedsessionid)
- [lk_processsession_originatingsessionid](#BKMK_lk_processsession_originatingsessionid)
- [Team_ProcessSessions](#BKMK_Team_ProcessSessions)
- [Goal_ProcessSessions](#BKMK_Goal_ProcessSessions)
- [mailbox_processsessions](#BKMK_mailbox_processsessions)
- [TranslationProcess_ProcessSessions](#BKMK_TranslationProcess_ProcessSessions)
- [SystemUser_ProcessSessions](#BKMK_SystemUser_ProcessSessions)
- [BusinessUnit_ProcessSessions](#BKMK_BusinessUnit_ProcessSessions)
- [KbArticleComment_ProcessSessions](#BKMK_KbArticleComment_ProcessSessions)
- [lk_processsession_canceledby](#BKMK_lk_processsession_canceledby)
- [goalrollupquery_ProcessSessions](#BKMK_goalrollupquery_ProcessSessions)
- [rollupfield_ProcessSessions](#BKMK_rollupfield_ProcessSessions)
- [SharePointDocumentLocation_ProcessSessions](#BKMK_SharePointDocumentLocation_ProcessSessions)
- [lk_processsession_startedby](#BKMK_lk_processsession_startedby)
- [Account_ProcessSessions](#BKMK_Account_ProcessSessions)
- [PhoneCall_ProcessSessions](#BKMK_PhoneCall_ProcessSessions)
- [slabase_ProcessSessions](#BKMK_slabase_ProcessSessions)
- [lk_processsession_createdby](#BKMK_lk_processsession_createdby)
- [lk_processsessionbase_modifiedonbehalfby](#BKMK_lk_processsessionbase_modifiedonbehalfby)
- [Template_ProcessSessions](#BKMK_Template_ProcessSessions)
- [NewProcess_ProcessSessions](#BKMK_NewProcess_ProcessSessions)
- [Report_ProcessSessions](#BKMK_Report_ProcessSessions)
- [Owning_businessunit_processsessions](#BKMK_Owning_businessunit_processsessions)
- [CustomerAddress_ProcessSessions](#BKMK_CustomerAddress_ProcessSessions)
- [Connection_ProcessSessions](#BKMK_Connection_ProcessSessions)
- [lk_processsession_executedby](#BKMK_lk_processsession_executedby)
- [team_processsession](#BKMK_team_processsession)
- [metric_ProcessSessions](#BKMK_metric_ProcessSessions)
- [ExpiredProcess_ProcessSessions](#BKMK_ExpiredProcess_ProcessSessions)
- [KbArticle_ProcessSessions](#BKMK_KbArticle_ProcessSessions)
- [SocialActivity_ProcessSessions](#BKMK_SocialActivity_ProcessSessions)
- [Task_ProcessSessions](#BKMK_Task_ProcessSessions)
- [lk_processsession_processid](#BKMK_lk_processsession_processid)
- [lk_processsession_modifiedby](#BKMK_lk_processsession_modifiedby)
- [ConnectionRole_ProcessSessions](#BKMK_ConnectionRole_ProcessSessions)
- [TransactionCurrency_ProcessSessions](#BKMK_TransactionCurrency_ProcessSessions)
- [Fax_ProcessSessions](#BKMK_Fax_ProcessSessions)
- [KbArticleTemplate_ProcessSessions](#BKMK_KbArticleTemplate_ProcessSessions)
- [Letter_ProcessSessions](#BKMK_Letter_ProcessSessions)
- [RecurringAppointmentMaster_ProcessSessions](#BKMK_RecurringAppointmentMaster_ProcessSessions)
- [Email_ProcessSessions](#BKMK_Email_ProcessSessions)
- [lk_processsession_completedby](#BKMK_lk_processsession_completedby)
- [Contact_ProcessSessions](#BKMK_Contact_ProcessSessions)
- [Queue_ProcessSessions](#BKMK_Queue_ProcessSessions)
- [lk_processsessionbase_createdonbehalfby](#BKMK_lk_processsessionbase_createdonbehalfby)
- [Subject_ProcessSessions](#BKMK_Subject_ProcessSessions)
- [SocialProfile_ProcessSessions](#BKMK_SocialProfile_ProcessSessions)
- [solutioncomponentattributeconfiguration_ProcessSession](#BKMK_solutioncomponentattributeconfiguration_ProcessSession)
- [solutioncomponentbatchconfiguration_ProcessSession](#BKMK_solutioncomponentbatchconfiguration_ProcessSession)
- [solutioncomponentconfiguration_ProcessSession](#BKMK_solutioncomponentconfiguration_ProcessSession)
- [solutioncomponentrelationshipconfiguration_ProcessSession](#BKMK_solutioncomponentrelationshipconfiguration_ProcessSession)
- [package_ProcessSession](#BKMK_package_ProcessSession)
- [stagesolutionupload_ProcessSession](#BKMK_stagesolutionupload_ProcessSession)
- [exportsolutionupload_ProcessSession](#BKMK_exportsolutionupload_ProcessSession)
- [featurecontrolsetting_ProcessSession](#BKMK_featurecontrolsetting_ProcessSession)
- [stagedentity_ProcessSession](#BKMK_stagedentity_ProcessSession)
- [stagedentityattribute_ProcessSession](#BKMK_stagedentityattribute_ProcessSession)
- [catalog_ProcessSession](#BKMK_catalog_ProcessSession)
- [catalogassignment_ProcessSession](#BKMK_catalogassignment_ProcessSession)
- [customapi_ProcessSession](#BKMK_customapi_ProcessSession)
- [customapirequestparameter_ProcessSession](#BKMK_customapirequestparameter_ProcessSession)
- [customapiresponseproperty_ProcessSession](#BKMK_customapiresponseproperty_ProcessSession)
- [provisionlanguageforuser_ProcessSession](#BKMK_provisionlanguageforuser_ProcessSession)
- [sharedobject_ProcessSession](#BKMK_sharedobject_ProcessSession)
- [sharedworkspace_ProcessSession](#BKMK_sharedworkspace_ProcessSession)
- [sharedworkspacepool_ProcessSession](#BKMK_sharedworkspacepool_ProcessSession)
- [datalakefolder_ProcessSession](#BKMK_datalakefolder_ProcessSession)
- [datalakefolderpermission_ProcessSession](#BKMK_datalakefolderpermission_ProcessSession)
- [datalakeworkspace_ProcessSession](#BKMK_datalakeworkspace_ProcessSession)
- [datalakeworkspacepermission_ProcessSession](#BKMK_datalakeworkspacepermission_ProcessSession)
- [dataprocessingconfiguration_ProcessSession](#BKMK_dataprocessingconfiguration_ProcessSession)
- [exportedexcel_ProcessSession](#BKMK_exportedexcel_ProcessSession)
- [retaineddataexcel_ProcessSession](#BKMK_retaineddataexcel_ProcessSession)
- [synapsedatabase_ProcessSession](#BKMK_synapsedatabase_ProcessSession)
- [synapselinkexternaltablestate_ProcessSession](#BKMK_synapselinkexternaltablestate_ProcessSession)
- [synapselinkprofile_ProcessSession](#BKMK_synapselinkprofile_ProcessSession)
- [synapselinkprofileentity_ProcessSession](#BKMK_synapselinkprofileentity_ProcessSession)
- [synapselinkprofileentitystate_ProcessSession](#BKMK_synapselinkprofileentitystate_ProcessSession)
- [synapselinkschedule_ProcessSession](#BKMK_synapselinkschedule_ProcessSession)
- [msdyn_dataflow_ProcessSession](#BKMK_msdyn_dataflow_ProcessSession)
- [msdyn_dataflowrefreshhistory_ProcessSession](#BKMK_msdyn_dataflowrefreshhistory_ProcessSession)
- [msdyn_entityrefreshhistory_ProcessSession](#BKMK_msdyn_entityrefreshhistory_ProcessSession)
- [sharedlinksetting_ProcessSession](#BKMK_sharedlinksetting_ProcessSession)
- [entityrecordfilter_ProcessSession](#BKMK_entityrecordfilter_ProcessSession)
- [recordfilter_ProcessSession](#BKMK_recordfilter_ProcessSession)
- [delegatedauthorization_ProcessSession](#BKMK_delegatedauthorization_ProcessSession)
- [serviceplan_ProcessSession](#BKMK_serviceplan_ProcessSession)
- [serviceplanmapping_ProcessSession](#BKMK_serviceplanmapping_ProcessSession)
- [applicationuser_ProcessSession](#BKMK_applicationuser_ProcessSession)
- [connector_ProcessSession](#BKMK_connector_ProcessSession)
- [environmentvariabledefinition_ProcessSession](#BKMK_environmentvariabledefinition_ProcessSession)
- [environmentvariablevalue_ProcessSession](#BKMK_environmentvariablevalue_ProcessSession)
- [workflowbinary_ProcessSession](#BKMK_workflowbinary_ProcessSession)
- [desktopflowmodule_ProcessSession](#BKMK_desktopflowmodule_ProcessSession)
- [flowmachine_ProcessSession](#BKMK_flowmachine_ProcessSession)
- [flowmachinegroup_ProcessSession](#BKMK_flowmachinegroup_ProcessSession)
- [flowmachineimage_ProcessSession](#BKMK_flowmachineimage_ProcessSession)
- [flowmachineimageversion_ProcessSession](#BKMK_flowmachineimageversion_ProcessSession)
- [flowmachinenetwork_ProcessSession](#BKMK_flowmachinenetwork_ProcessSession)
- [processstageparameter_ProcessSession](#BKMK_processstageparameter_ProcessSession)
- [workqueue_ProcessSession](#BKMK_workqueue_ProcessSession)
- [workqueueitem_ProcessSession](#BKMK_workqueueitem_ProcessSession)
- [desktopflowbinary_ProcessSession](#BKMK_desktopflowbinary_ProcessSession)
- [connectionreference_ProcessSession](#BKMK_connectionreference_ProcessSession)
- [connectioninstance_ProcessSession](#BKMK_connectioninstance_ProcessSession)
- [msdyn_helppage_ProcessSession](#BKMK_msdyn_helppage_ProcessSession)
- [msdyn_tour_ProcessSession](#BKMK_msdyn_tour_ProcessSession)
- [msdynce_botcontent_ProcessSession](#BKMK_msdynce_botcontent_ProcessSession)
- [conversationtranscript_ProcessSession](#BKMK_conversationtranscript_ProcessSession)
- [bot_ProcessSession](#BKMK_bot_ProcessSession)
- [botcomponent_ProcessSession](#BKMK_botcomponent_ProcessSession)
- [Territory_ProcessSessions](#BKMK_Territory_ProcessSessions)
- [activityfileattachment_ProcessSession](#BKMK_activityfileattachment_ProcessSession)
- [chat_ProcessSession](#BKMK_chat_ProcessSession)
- [msdyn_serviceconfiguration_ProcessSession](#BKMK_msdyn_serviceconfiguration_ProcessSession)
- [msdyn_slakpi_ProcessSession](#BKMK_msdyn_slakpi_ProcessSession)
- [msdyn_knowledgemanagementsetting_ProcessSession](#BKMK_msdyn_knowledgemanagementsetting_ProcessSession)
- [msdyn_federatedarticle_ProcessSession](#BKMK_msdyn_federatedarticle_ProcessSession)
- [msdyn_federatedarticleincident_ProcessSession](#BKMK_msdyn_federatedarticleincident_ProcessSession)
- [msdyn_integratedsearchprovider_ProcessSession](#BKMK_msdyn_integratedsearchprovider_ProcessSession)
- [msdyn_kmfederatedsearchconfig_ProcessSession](#BKMK_msdyn_kmfederatedsearchconfig_ProcessSession)
- [msdyn_knowledgearticleimage_ProcessSession](#BKMK_msdyn_knowledgearticleimage_ProcessSession)
- [msdyn_knowledgeconfiguration_ProcessSession](#BKMK_msdyn_knowledgeconfiguration_ProcessSession)
- [msdyn_knowledgeinteractioninsight_ProcessSession](#BKMK_msdyn_knowledgeinteractioninsight_ProcessSession)
- [msdyn_knowledgesearchinsight_ProcessSession](#BKMK_msdyn_knowledgesearchinsight_ProcessSession)
- [msdyn_favoriteknowledgearticle_ProcessSession](#BKMK_msdyn_favoriteknowledgearticle_ProcessSession)
- [msdyn_kalanguagesetting_ProcessSession](#BKMK_msdyn_kalanguagesetting_ProcessSession)
- [msdyn_kbattachment_ProcessSession](#BKMK_msdyn_kbattachment_ProcessSession)
- [msdyn_kmpersonalizationsetting_ProcessSession](#BKMK_msdyn_kmpersonalizationsetting_ProcessSession)
- [msdyn_knowledgearticletemplate_ProcessSession](#BKMK_msdyn_knowledgearticletemplate_ProcessSession)
- [msdyn_knowledgepersonalfilter_ProcessSession](#BKMK_msdyn_knowledgepersonalfilter_ProcessSession)
- [msdyn_knowledgesearchfilter_ProcessSession](#BKMK_msdyn_knowledgesearchfilter_ProcessSession)
- [fxexpression_ProcessSession](#BKMK_fxexpression_ProcessSession)
- [powerfxrule_ProcessSession](#BKMK_powerfxrule_ProcessSession)
- [keyvaultreference_ProcessSession](#BKMK_keyvaultreference_ProcessSession)
- [managedidentity_ProcessSession](#BKMK_managedidentity_ProcessSession)
- [msgraphresourcetosubscription_ProcessSession](#BKMK_msgraphresourcetosubscription_ProcessSession)
- [virtualentitymetadata_ProcessSession](#BKMK_virtualentitymetadata_ProcessSession)
- [mobileofflineprofileextension_ProcessSession](#BKMK_mobileofflineprofileextension_ProcessSession)
- [teammobileofflineprofilemembership_ProcessSession](#BKMK_teammobileofflineprofilemembership_ProcessSession)
- [usermobileofflineprofilemembership_ProcessSession](#BKMK_usermobileofflineprofilemembership_ProcessSession)
- [organizationdatasyncsubscription_ProcessSession](#BKMK_organizationdatasyncsubscription_ProcessSession)
- [organizationdatasyncsubscriptionentity_ProcessSession](#BKMK_organizationdatasyncsubscriptionentity_ProcessSession)
- [organizationdatasyncsubscriptionfnotable_ProcessSession](#BKMK_organizationdatasyncsubscriptionfnotable_ProcessSession)
- [organizationdatasyncfnostate_ProcessSession](#BKMK_organizationdatasyncfnostate_ProcessSession)
- [organizationdatasyncstate_ProcessSession](#BKMK_organizationdatasyncstate_ProcessSession)
- [metadataforarchival_ProcessSession](#BKMK_metadataforarchival_ProcessSession)
- [retentionconfig_ProcessSession](#BKMK_retentionconfig_ProcessSession)
- [retentionfailuredetail_ProcessSession](#BKMK_retentionfailuredetail_ProcessSession)
- [retentionoperation_ProcessSession](#BKMK_retentionoperation_ProcessSession)
- [retentionoperationdetail_ProcessSession](#BKMK_retentionoperationdetail_ProcessSession)
- [msdyn_appinsightsmetadata_ProcessSession](#BKMK_msdyn_appinsightsmetadata_ProcessSession)
- [msdyn_dataflowtemplate_ProcessSession](#BKMK_msdyn_dataflowtemplate_ProcessSession)
- [msdyn_workflowactionstatus_ProcessSession](#BKMK_msdyn_workflowactionstatus_ProcessSession)
- [userrating_ProcessSession](#BKMK_userrating_ProcessSession)
- [msdyn_mobileapp_ProcessSession](#BKMK_msdyn_mobileapp_ProcessSession)
- [msdyn_insightsstorevirtualentity_ProcessSession](#BKMK_msdyn_insightsstorevirtualentity_ProcessSession)
- [roleeditorlayout_ProcessSession](#BKMK_roleeditorlayout_ProcessSession)
- [appaction_ProcessSession](#BKMK_appaction_ProcessSession)
- [appactionmigration_ProcessSession](#BKMK_appactionmigration_ProcessSession)
- [appactionrule_ProcessSession](#BKMK_appactionrule_ProcessSession)
- [card_ProcessSession](#BKMK_card_ProcessSession)
- [msdyn_entitylinkchatconfiguration_ProcessSession](#BKMK_msdyn_entitylinkchatconfiguration_ProcessSession)
- [msdyn_richtextfile_ProcessSession](#BKMK_msdyn_richtextfile_ProcessSession)
- [msdyn_customcontrolextendedsettings_ProcessSession](#BKMK_msdyn_customcontrolextendedsettings_ProcessSession)
- [searchrelationshipsettings_ProcessSession](#BKMK_searchrelationshipsettings_ProcessSession)
- [msdyn_virtualtablecolumncandidate_ProcessSession](#BKMK_msdyn_virtualtablecolumncandidate_ProcessSession)
- [msdyn_aiconfiguration_ProcessSession](#BKMK_msdyn_aiconfiguration_ProcessSession)
- [msdyn_aievent_ProcessSession](#BKMK_msdyn_aievent_ProcessSession)
- [msdyn_aimodel_ProcessSession](#BKMK_msdyn_aimodel_ProcessSession)
- [msdyn_aitemplate_ProcessSession](#BKMK_msdyn_aitemplate_ProcessSession)
- [msdyn_aibfeedbackloop_ProcessSession](#BKMK_msdyn_aibfeedbackloop_ProcessSession)
- [msdyn_aifptrainingdocument_ProcessSession](#BKMK_msdyn_aifptrainingdocument_ProcessSession)
- [msdyn_aiodimage_ProcessSession](#BKMK_msdyn_aiodimage_ProcessSession)
- [msdyn_aiodlabel_ProcessSession](#BKMK_msdyn_aiodlabel_ProcessSession)
- [msdyn_aiodtrainingboundingbox_ProcessSession](#BKMK_msdyn_aiodtrainingboundingbox_ProcessSession)
- [msdyn_aiodtrainingimage_ProcessSession](#BKMK_msdyn_aiodtrainingimage_ProcessSession)
- [msdyn_aibdataset_ProcessSession](#BKMK_msdyn_aibdataset_ProcessSession)
- [msdyn_aibdatasetfile_ProcessSession](#BKMK_msdyn_aibdatasetfile_ProcessSession)
- [msdyn_aibdatasetrecord_ProcessSession](#BKMK_msdyn_aibdatasetrecord_ProcessSession)
- [msdyn_aibdatasetscontainer_ProcessSession](#BKMK_msdyn_aibdatasetscontainer_ProcessSession)
- [msdyn_aibfile_ProcessSession](#BKMK_msdyn_aibfile_ProcessSession)
- [msdyn_aibfileattacheddata_ProcessSession](#BKMK_msdyn_aibfileattacheddata_ProcessSession)
- [msdyn_pmanalysishistory_ProcessSession](#BKMK_msdyn_pmanalysishistory_ProcessSession)
- [msdyn_pmcalendar_ProcessSession](#BKMK_msdyn_pmcalendar_ProcessSession)
- [msdyn_pmcalendarversion_ProcessSession](#BKMK_msdyn_pmcalendarversion_ProcessSession)
- [msdyn_pminferredtask_ProcessSession](#BKMK_msdyn_pminferredtask_ProcessSession)
- [msdyn_pmprocessextendedmetadataversion_ProcessSession](#BKMK_msdyn_pmprocessextendedmetadataversion_ProcessSession)
- [msdyn_pmprocesstemplate_ProcessSession](#BKMK_msdyn_pmprocesstemplate_ProcessSession)
- [msdyn_pmprocessusersettings_ProcessSession](#BKMK_msdyn_pmprocessusersettings_ProcessSession)
- [msdyn_pmprocessversion_ProcessSession](#BKMK_msdyn_pmprocessversion_ProcessSession)
- [msdyn_pmrecording_ProcessSession](#BKMK_msdyn_pmrecording_ProcessSession)
- [msdyn_pmtemplate_ProcessSession](#BKMK_msdyn_pmtemplate_ProcessSession)
- [msdyn_pmview_ProcessSession](#BKMK_msdyn_pmview_ProcessSession)
- [msdyn_analysiscomponent_ProcessSession](#BKMK_msdyn_analysiscomponent_ProcessSession)
- [msdyn_analysisjob_ProcessSession](#BKMK_msdyn_analysisjob_ProcessSession)
- [msdyn_analysisoverride_ProcessSession](#BKMK_msdyn_analysisoverride_ProcessSession)
- [msdyn_analysisresult_ProcessSession](#BKMK_msdyn_analysisresult_ProcessSession)
- [msdyn_analysisresultdetail_ProcessSession](#BKMK_msdyn_analysisresultdetail_ProcessSession)
- [msdyn_solutionhealthrule_ProcessSession](#BKMK_msdyn_solutionhealthrule_ProcessSession)
- [msdyn_solutionhealthruleargument_ProcessSession](#BKMK_msdyn_solutionhealthruleargument_ProcessSession)
- [msdyn_solutionhealthruleset_ProcessSession](#BKMK_msdyn_solutionhealthruleset_ProcessSession)
- [powerbidataset_ProcessSession](#BKMK_powerbidataset_ProcessSession)
- [powerbimashupparameter_ProcessSession](#BKMK_powerbimashupparameter_ProcessSession)
- [powerbireport_ProcessSession](#BKMK_powerbireport_ProcessSession)
- [msdyn_fileupload_ProcessSession](#BKMK_msdyn_fileupload_ProcessSession)
- [mspcat_catalogsubmissionfiles_ProcessSession](#BKMK_mspcat_catalogsubmissionfiles_ProcessSession)
- [mspcat_packagestore_ProcessSession](#BKMK_mspcat_packagestore_ProcessSession)
- [msdyn_schedule_ProcessSession](#BKMK_msdyn_schedule_ProcessSession)
- [msdyn_dataflow_datalakefolder_ProcessSession](#BKMK_msdyn_dataflow_datalakefolder_ProcessSession)
- [msdyn_dmsrequest_ProcessSession](#BKMK_msdyn_dmsrequest_ProcessSession)
- [msdyn_dmsrequeststatus_ProcessSession](#BKMK_msdyn_dmsrequeststatus_ProcessSession)
- [searchattributesettings_ProcessSession](#BKMK_searchattributesettings_ProcessSession)
- [searchcustomanalyzer_ProcessSession](#BKMK_searchcustomanalyzer_ProcessSession)


### <a name="BKMK_theme_ProcessSession"></a> theme_ProcessSession

See the [theme_ProcessSession](theme.md#BKMK_theme_ProcessSession) one-to-many relationship for the [theme](theme.md) table/entity.

### <a name="BKMK_usermapping_ProcessSession"></a> usermapping_ProcessSession

See the [usermapping_ProcessSession](usermapping.md#BKMK_usermapping_ProcessSession) one-to-many relationship for the [usermapping](usermapping.md) table/entity.

### <a name="BKMK_knowledgearticle_ProcessSession"></a> knowledgearticle_ProcessSession

See the [knowledgearticle_ProcessSession](knowledgearticle.md#BKMK_knowledgearticle_ProcessSession) one-to-many relationship for the [knowledgearticle](knowledgearticle.md) table/entity.

### <a name="BKMK_position_ProcessSession"></a> position_ProcessSession

See the [position_ProcessSession](position.md#BKMK_position_ProcessSession) one-to-many relationship for the [position](position.md) table/entity.

### <a name="BKMK_KnowledgeBaseRecord_ProcessSession"></a> KnowledgeBaseRecord_ProcessSession

See the [KnowledgeBaseRecord_ProcessSession](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_ProcessSession) one-to-many relationship for the [knowledgebaserecord](knowledgebaserecord.md) table/entity.

### <a name="BKMK_SharePointSite_ProcessSessions"></a> SharePointSite_ProcessSessions

See the [SharePointSite_ProcessSessions](sharepointsite.md#BKMK_SharePointSite_ProcessSessions) one-to-many relationship for the [sharepointsite](sharepointsite.md) table/entity.

### <a name="BKMK_MailMergeTemplate_ProcessSessions"></a> MailMergeTemplate_ProcessSessions

See the [MailMergeTemplate_ProcessSessions](mailmergetemplate.md#BKMK_MailMergeTemplate_ProcessSessions) one-to-many relationship for the [mailmergetemplate](mailmergetemplate.md) table/entity.

### <a name="BKMK_Annotation_ProcessSessions"></a> Annotation_ProcessSessions

See the [Annotation_ProcessSessions](annotation.md#BKMK_Annotation_ProcessSessions) one-to-many relationship for the [annotation](annotation.md) table/entity.

### <a name="BKMK_BusinessUnitNewsArticle_ProcessSessions"></a> BusinessUnitNewsArticle_ProcessSessions

See the [BusinessUnitNewsArticle_ProcessSessions](businessunitnewsarticle.md#BKMK_BusinessUnitNewsArticle_ProcessSessions) one-to-many relationship for the [businessunitnewsarticle](businessunitnewsarticle.md) table/entity.

### <a name="BKMK_Appointment_ProcessSessions"></a> Appointment_ProcessSessions

See the [Appointment_ProcessSessions](appointment.md#BKMK_Appointment_ProcessSessions) one-to-many relationship for the [appointment](appointment.md) table/entity.

### <a name="BKMK_QueueItem_ProcessSessions"></a> QueueItem_ProcessSessions

See the [QueueItem_ProcessSessions](queueitem.md#BKMK_QueueItem_ProcessSessions) one-to-many relationship for the [queueitem](queueitem.md) table/entity.

### <a name="BKMK_lk_processsession_previouslinkedsessionid"></a> lk_processsession_previouslinkedsessionid

See the [lk_processsession_previouslinkedsessionid](processsession.md#BKMK_lk_processsession_previouslinkedsessionid) one-to-many relationship for the [processsession](processsession.md) table/entity.

### <a name="BKMK_lk_processsession_nextlinkedsessionid"></a> lk_processsession_nextlinkedsessionid

See the [lk_processsession_nextlinkedsessionid](processsession.md#BKMK_lk_processsession_nextlinkedsessionid) one-to-many relationship for the [processsession](processsession.md) table/entity.

### <a name="BKMK_lk_processsession_originatingsessionid"></a> lk_processsession_originatingsessionid

See the [lk_processsession_originatingsessionid](processsession.md#BKMK_lk_processsession_originatingsessionid) one-to-many relationship for the [processsession](processsession.md) table/entity.

### <a name="BKMK_Team_ProcessSessions"></a> Team_ProcessSessions

See the [Team_ProcessSessions](team.md#BKMK_Team_ProcessSessions) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_Goal_ProcessSessions"></a> Goal_ProcessSessions

See the [Goal_ProcessSessions](goal.md#BKMK_Goal_ProcessSessions) one-to-many relationship for the [goal](goal.md) table/entity.

### <a name="BKMK_mailbox_processsessions"></a> mailbox_processsessions

See the [mailbox_processsessions](mailbox.md#BKMK_mailbox_processsessions) one-to-many relationship for the [mailbox](mailbox.md) table/entity.

### <a name="BKMK_TranslationProcess_ProcessSessions"></a> TranslationProcess_ProcessSessions

See the [TranslationProcess_ProcessSessions](translationprocess.md#BKMK_TranslationProcess_ProcessSessions) one-to-many relationship for the [translationprocess](translationprocess.md) table/entity.

### <a name="BKMK_SystemUser_ProcessSessions"></a> SystemUser_ProcessSessions

See the [SystemUser_ProcessSessions](systemuser.md#BKMK_SystemUser_ProcessSessions) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_BusinessUnit_ProcessSessions"></a> BusinessUnit_ProcessSessions

See the [BusinessUnit_ProcessSessions](businessunit.md#BKMK_BusinessUnit_ProcessSessions) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_KbArticleComment_ProcessSessions"></a> KbArticleComment_ProcessSessions

See the [KbArticleComment_ProcessSessions](kbarticlecomment.md#BKMK_KbArticleComment_ProcessSessions) one-to-many relationship for the [kbarticlecomment](kbarticlecomment.md) table/entity.

### <a name="BKMK_lk_processsession_canceledby"></a> lk_processsession_canceledby

See the [lk_processsession_canceledby](systemuser.md#BKMK_lk_processsession_canceledby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_goalrollupquery_ProcessSessions"></a> goalrollupquery_ProcessSessions

See the [goalrollupquery_ProcessSessions](goalrollupquery.md#BKMK_goalrollupquery_ProcessSessions) one-to-many relationship for the [goalrollupquery](goalrollupquery.md) table/entity.

### <a name="BKMK_rollupfield_ProcessSessions"></a> rollupfield_ProcessSessions

See the [rollupfield_ProcessSessions](rollupfield.md#BKMK_rollupfield_ProcessSessions) one-to-many relationship for the [rollupfield](rollupfield.md) table/entity.

### <a name="BKMK_SharePointDocumentLocation_ProcessSessions"></a> SharePointDocumentLocation_ProcessSessions

See the [SharePointDocumentLocation_ProcessSessions](sharepointdocumentlocation.md#BKMK_SharePointDocumentLocation_ProcessSessions) one-to-many relationship for the [sharepointdocumentlocation](sharepointdocumentlocation.md) table/entity.

### <a name="BKMK_lk_processsession_startedby"></a> lk_processsession_startedby

See the [lk_processsession_startedby](systemuser.md#BKMK_lk_processsession_startedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_Account_ProcessSessions"></a> Account_ProcessSessions

See the [Account_ProcessSessions](account.md#BKMK_Account_ProcessSessions) one-to-many relationship for the [account](account.md) table/entity.

### <a name="BKMK_PhoneCall_ProcessSessions"></a> PhoneCall_ProcessSessions

See the [PhoneCall_ProcessSessions](phonecall.md#BKMK_PhoneCall_ProcessSessions) one-to-many relationship for the [phonecall](phonecall.md) table/entity.

### <a name="BKMK_slabase_ProcessSessions"></a> slabase_ProcessSessions

See the [slabase_ProcessSessions](sla.md#BKMK_slabase_ProcessSessions) one-to-many relationship for the [sla](sla.md) table/entity.

### <a name="BKMK_lk_processsession_createdby"></a> lk_processsession_createdby

See the [lk_processsession_createdby](systemuser.md#BKMK_lk_processsession_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_processsessionbase_modifiedonbehalfby"></a> lk_processsessionbase_modifiedonbehalfby

See the [lk_processsessionbase_modifiedonbehalfby](systemuser.md#BKMK_lk_processsessionbase_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_Template_ProcessSessions"></a> Template_ProcessSessions

See the [Template_ProcessSessions](template.md#BKMK_Template_ProcessSessions) one-to-many relationship for the [template](template.md) table/entity.

### <a name="BKMK_NewProcess_ProcessSessions"></a> NewProcess_ProcessSessions

See the [NewProcess_ProcessSessions](newprocess.md#BKMK_NewProcess_ProcessSessions) one-to-many relationship for the [newprocess](newprocess.md) table/entity.

### <a name="BKMK_Report_ProcessSessions"></a> Report_ProcessSessions

See the [Report_ProcessSessions](report.md#BKMK_Report_ProcessSessions) one-to-many relationship for the [report](report.md) table/entity.

### <a name="BKMK_Owning_businessunit_processsessions"></a> Owning_businessunit_processsessions

See the [Owning_businessunit_processsessions](businessunit.md#BKMK_Owning_businessunit_processsessions) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_CustomerAddress_ProcessSessions"></a> CustomerAddress_ProcessSessions

See the [CustomerAddress_ProcessSessions](customeraddress.md#BKMK_CustomerAddress_ProcessSessions) one-to-many relationship for the [customeraddress](customeraddress.md) table/entity.

### <a name="BKMK_Connection_ProcessSessions"></a> Connection_ProcessSessions

See the [Connection_ProcessSessions](connection.md#BKMK_Connection_ProcessSessions) one-to-many relationship for the [connection](connection.md) table/entity.

### <a name="BKMK_lk_processsession_executedby"></a> lk_processsession_executedby

See the [lk_processsession_executedby](systemuser.md#BKMK_lk_processsession_executedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_team_processsession"></a> team_processsession

See the [team_processsession](team.md#BKMK_team_processsession) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_metric_ProcessSessions"></a> metric_ProcessSessions

See the [metric_ProcessSessions](metric.md#BKMK_metric_ProcessSessions) one-to-many relationship for the [metric](metric.md) table/entity.

### <a name="BKMK_ExpiredProcess_ProcessSessions"></a> ExpiredProcess_ProcessSessions

See the [ExpiredProcess_ProcessSessions](expiredprocess.md#BKMK_ExpiredProcess_ProcessSessions) one-to-many relationship for the [expiredprocess](expiredprocess.md) table/entity.

### <a name="BKMK_KbArticle_ProcessSessions"></a> KbArticle_ProcessSessions

See the [KbArticle_ProcessSessions](kbarticle.md#BKMK_KbArticle_ProcessSessions) one-to-many relationship for the [kbarticle](kbarticle.md) table/entity.

### <a name="BKMK_SocialActivity_ProcessSessions"></a> SocialActivity_ProcessSessions

See the [SocialActivity_ProcessSessions](socialactivity.md#BKMK_SocialActivity_ProcessSessions) one-to-many relationship for the [socialactivity](socialactivity.md) table/entity.

### <a name="BKMK_Task_ProcessSessions"></a> Task_ProcessSessions

See the [Task_ProcessSessions](task.md#BKMK_Task_ProcessSessions) one-to-many relationship for the [task](task.md) table/entity.

### <a name="BKMK_lk_processsession_processid"></a> lk_processsession_processid

See the [lk_processsession_processid](workflow.md#BKMK_lk_processsession_processid) one-to-many relationship for the [workflow](workflow.md) table/entity.

### <a name="BKMK_lk_processsession_modifiedby"></a> lk_processsession_modifiedby

See the [lk_processsession_modifiedby](systemuser.md#BKMK_lk_processsession_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_ConnectionRole_ProcessSessions"></a> ConnectionRole_ProcessSessions

See the [ConnectionRole_ProcessSessions](connectionrole.md#BKMK_ConnectionRole_ProcessSessions) one-to-many relationship for the [connectionrole](connectionrole.md) table/entity.

### <a name="BKMK_TransactionCurrency_ProcessSessions"></a> TransactionCurrency_ProcessSessions

See the [TransactionCurrency_ProcessSessions](transactioncurrency.md#BKMK_TransactionCurrency_ProcessSessions) one-to-many relationship for the [transactioncurrency](transactioncurrency.md) table/entity.

### <a name="BKMK_Fax_ProcessSessions"></a> Fax_ProcessSessions

See the [Fax_ProcessSessions](fax.md#BKMK_Fax_ProcessSessions) one-to-many relationship for the [fax](fax.md) table/entity.

### <a name="BKMK_KbArticleTemplate_ProcessSessions"></a> KbArticleTemplate_ProcessSessions

See the [KbArticleTemplate_ProcessSessions](kbarticletemplate.md#BKMK_KbArticleTemplate_ProcessSessions) one-to-many relationship for the [kbarticletemplate](kbarticletemplate.md) table/entity.

### <a name="BKMK_Letter_ProcessSessions"></a> Letter_ProcessSessions

See the [Letter_ProcessSessions](letter.md#BKMK_Letter_ProcessSessions) one-to-many relationship for the [letter](letter.md) table/entity.

### <a name="BKMK_RecurringAppointmentMaster_ProcessSessions"></a> RecurringAppointmentMaster_ProcessSessions

See the [RecurringAppointmentMaster_ProcessSessions](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_ProcessSessions) one-to-many relationship for the [recurringappointmentmaster](recurringappointmentmaster.md) table/entity.

### <a name="BKMK_Email_ProcessSessions"></a> Email_ProcessSessions

See the [Email_ProcessSessions](email.md#BKMK_Email_ProcessSessions) one-to-many relationship for the [email](email.md) table/entity.

### <a name="BKMK_lk_processsession_completedby"></a> lk_processsession_completedby

See the [lk_processsession_completedby](systemuser.md#BKMK_lk_processsession_completedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_Contact_ProcessSessions"></a> Contact_ProcessSessions

See the [Contact_ProcessSessions](contact.md#BKMK_Contact_ProcessSessions) one-to-many relationship for the [contact](contact.md) table/entity.

### <a name="BKMK_Queue_ProcessSessions"></a> Queue_ProcessSessions

See the [Queue_ProcessSessions](queue.md#BKMK_Queue_ProcessSessions) one-to-many relationship for the [queue](queue.md) table/entity.

### <a name="BKMK_lk_processsessionbase_createdonbehalfby"></a> lk_processsessionbase_createdonbehalfby

See the [lk_processsessionbase_createdonbehalfby](systemuser.md#BKMK_lk_processsessionbase_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_Subject_ProcessSessions"></a> Subject_ProcessSessions

See the [Subject_ProcessSessions](subject.md#BKMK_Subject_ProcessSessions) one-to-many relationship for the [subject](subject.md) table/entity.

### <a name="BKMK_SocialProfile_ProcessSessions"></a> SocialProfile_ProcessSessions

See the [SocialProfile_ProcessSessions](socialprofile.md#BKMK_SocialProfile_ProcessSessions) one-to-many relationship for the [socialprofile](socialprofile.md) table/entity.

### <a name="BKMK_solutioncomponentattributeconfiguration_ProcessSession"></a> solutioncomponentattributeconfiguration_ProcessSession

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentattributeconfiguration_ProcessSession](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_ProcessSession) one-to-many relationship for the [solutioncomponentattributeconfiguration](solutioncomponentattributeconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentbatchconfiguration_ProcessSession"></a> solutioncomponentbatchconfiguration_ProcessSession

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentbatchconfiguration_ProcessSession](solutioncomponentbatchconfiguration.md#BKMK_solutioncomponentbatchconfiguration_ProcessSession) one-to-many relationship for the [solutioncomponentbatchconfiguration](solutioncomponentbatchconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentconfiguration_ProcessSession"></a> solutioncomponentconfiguration_ProcessSession

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentconfiguration_ProcessSession](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_ProcessSession) one-to-many relationship for the [solutioncomponentconfiguration](solutioncomponentconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentrelationshipconfiguration_ProcessSession"></a> solutioncomponentrelationshipconfiguration_ProcessSession

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentrelationshipconfiguration_ProcessSession](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_ProcessSession) one-to-many relationship for the [solutioncomponentrelationshipconfiguration](solutioncomponentrelationshipconfiguration.md) table/entity.

### <a name="BKMK_package_ProcessSession"></a> package_ProcessSession

**Added by**: msdyn_SolutionPackageMapping Solution

See the [package_ProcessSession](package.md#BKMK_package_ProcessSession) one-to-many relationship for the [package](package.md) table/entity.

### <a name="BKMK_stagesolutionupload_ProcessSession"></a> stagesolutionupload_ProcessSession

**Added by**: StageSolutionUpload Solution

See the [stagesolutionupload_ProcessSession](stagesolutionupload.md#BKMK_stagesolutionupload_ProcessSession) one-to-many relationship for the [stagesolutionupload](stagesolutionupload.md) table/entity.

### <a name="BKMK_exportsolutionupload_ProcessSession"></a> exportsolutionupload_ProcessSession

**Added by**: ExportSolutionUpload Solution

See the [exportsolutionupload_ProcessSession](exportsolutionupload.md#BKMK_exportsolutionupload_ProcessSession) one-to-many relationship for the [exportsolutionupload](exportsolutionupload.md) table/entity.

### <a name="BKMK_featurecontrolsetting_ProcessSession"></a> featurecontrolsetting_ProcessSession

**Added by**: msdyn_FeatureControlSetting Solution

See the [featurecontrolsetting_ProcessSession](featurecontrolsetting.md#BKMK_featurecontrolsetting_ProcessSession) one-to-many relationship for the [featurecontrolsetting](featurecontrolsetting.md) table/entity.

### <a name="BKMK_stagedentity_ProcessSession"></a> stagedentity_ProcessSession

**Added by**: Metadata Extension Solution

See the [stagedentity_ProcessSession](stagedentity.md#BKMK_stagedentity_ProcessSession) one-to-many relationship for the [stagedentity](stagedentity.md) table/entity.

### <a name="BKMK_stagedentityattribute_ProcessSession"></a> stagedentityattribute_ProcessSession

**Added by**: Metadata Extension Solution

See the [stagedentityattribute_ProcessSession](stagedentityattribute.md#BKMK_stagedentityattribute_ProcessSession) one-to-many relationship for the [stagedentityattribute](stagedentityattribute.md) table/entity.

### <a name="BKMK_catalog_ProcessSession"></a> catalog_ProcessSession

**Added by**: CatalogFramework Solution

See the [catalog_ProcessSession](catalog.md#BKMK_catalog_ProcessSession) one-to-many relationship for the [catalog](catalog.md) table/entity.

### <a name="BKMK_catalogassignment_ProcessSession"></a> catalogassignment_ProcessSession

**Added by**: CatalogFramework Solution

See the [catalogassignment_ProcessSession](catalogassignment.md#BKMK_catalogassignment_ProcessSession) one-to-many relationship for the [catalogassignment](catalogassignment.md) table/entity.

### <a name="BKMK_customapi_ProcessSession"></a> customapi_ProcessSession

**Added by**: Custom API Framework Solution

See the [customapi_ProcessSession](customapi.md#BKMK_customapi_ProcessSession) one-to-many relationship for the [customapi](customapi.md) table/entity.

### <a name="BKMK_customapirequestparameter_ProcessSession"></a> customapirequestparameter_ProcessSession

**Added by**: Custom API Framework Solution

See the [customapirequestparameter_ProcessSession](customapirequestparameter.md#BKMK_customapirequestparameter_ProcessSession) one-to-many relationship for the [customapirequestparameter](customapirequestparameter.md) table/entity.

### <a name="BKMK_customapiresponseproperty_ProcessSession"></a> customapiresponseproperty_ProcessSession

**Added by**: Custom API Framework Solution

See the [customapiresponseproperty_ProcessSession](customapiresponseproperty.md#BKMK_customapiresponseproperty_ProcessSession) one-to-many relationship for the [customapiresponseproperty](customapiresponseproperty.md) table/entity.

### <a name="BKMK_provisionlanguageforuser_ProcessSession"></a> provisionlanguageforuser_ProcessSession

**Added by**: msft_LocalizationExtension Solution

See the [provisionlanguageforuser_ProcessSession](provisionlanguageforuser.md#BKMK_provisionlanguageforuser_ProcessSession) one-to-many relationship for the [provisionlanguageforuser](provisionlanguageforuser.md) table/entity.

### <a name="BKMK_sharedobject_ProcessSession"></a> sharedobject_ProcessSession

**Added by**: Real-time Collaboration App Solution

See the [sharedobject_ProcessSession](sharedobject.md#BKMK_sharedobject_ProcessSession) one-to-many relationship for the [sharedobject](sharedobject.md) table/entity.

### <a name="BKMK_sharedworkspace_ProcessSession"></a> sharedworkspace_ProcessSession

**Added by**: Real-time Collaboration App Solution

See the [sharedworkspace_ProcessSession](sharedworkspace.md#BKMK_sharedworkspace_ProcessSession) one-to-many relationship for the [sharedworkspace](sharedworkspace.md) table/entity.

### <a name="BKMK_sharedworkspacepool_ProcessSession"></a> sharedworkspacepool_ProcessSession

**Added by**: Real-time Collaboration App Solution

See the [sharedworkspacepool_ProcessSession](sharedworkspacepool.md#BKMK_sharedworkspacepool_ProcessSession) one-to-many relationship for the [sharedworkspacepool](sharedworkspacepool.md) table/entity.

### <a name="BKMK_datalakefolder_ProcessSession"></a> datalakefolder_ProcessSession

**Added by**: Data lake workspaces Solution

See the [datalakefolder_ProcessSession](datalakefolder.md#BKMK_datalakefolder_ProcessSession) one-to-many relationship for the [datalakefolder](datalakefolder.md) table/entity.

### <a name="BKMK_datalakefolderpermission_ProcessSession"></a> datalakefolderpermission_ProcessSession

**Added by**: Data lake workspaces Solution

See the [datalakefolderpermission_ProcessSession](datalakefolderpermission.md#BKMK_datalakefolderpermission_ProcessSession) one-to-many relationship for the [datalakefolderpermission](datalakefolderpermission.md) table/entity.

### <a name="BKMK_datalakeworkspace_ProcessSession"></a> datalakeworkspace_ProcessSession

**Added by**: Data lake workspaces Solution

See the [datalakeworkspace_ProcessSession](datalakeworkspace.md#BKMK_datalakeworkspace_ProcessSession) one-to-many relationship for the [datalakeworkspace](datalakeworkspace.md) table/entity.

### <a name="BKMK_datalakeworkspacepermission_ProcessSession"></a> datalakeworkspacepermission_ProcessSession

**Added by**: Data lake workspaces Solution

See the [datalakeworkspacepermission_ProcessSession](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_ProcessSession) one-to-many relationship for the [datalakeworkspacepermission](datalakeworkspacepermission.md) table/entity.

### <a name="BKMK_dataprocessingconfiguration_ProcessSession"></a> dataprocessingconfiguration_ProcessSession

**Added by**: Data lake workspaces Solution

See the [dataprocessingconfiguration_ProcessSession](dataprocessingconfiguration.md#BKMK_dataprocessingconfiguration_ProcessSession) one-to-many relationship for the [dataprocessingconfiguration](dataprocessingconfiguration.md) table/entity.

### <a name="BKMK_exportedexcel_ProcessSession"></a> exportedexcel_ProcessSession

**Added by**: Data lake workspaces Solution

See the [exportedexcel_ProcessSession](exportedexcel.md#BKMK_exportedexcel_ProcessSession) one-to-many relationship for the [exportedexcel](exportedexcel.md) table/entity.

### <a name="BKMK_retaineddataexcel_ProcessSession"></a> retaineddataexcel_ProcessSession

**Added by**: Data lake workspaces Solution

See the [retaineddataexcel_ProcessSession](retaineddataexcel.md#BKMK_retaineddataexcel_ProcessSession) one-to-many relationship for the [retaineddataexcel](retaineddataexcel.md) table/entity.

### <a name="BKMK_synapsedatabase_ProcessSession"></a> synapsedatabase_ProcessSession

**Added by**: Data lake workspaces Solution

See the [synapsedatabase_ProcessSession](synapsedatabase.md#BKMK_synapsedatabase_ProcessSession) one-to-many relationship for the [synapsedatabase](synapsedatabase.md) table/entity.

### <a name="BKMK_synapselinkexternaltablestate_ProcessSession"></a> synapselinkexternaltablestate_ProcessSession

**Added by**: Synapse Link Solution

See the [synapselinkexternaltablestate_ProcessSession](synapselinkexternaltablestate.md#BKMK_synapselinkexternaltablestate_ProcessSession) one-to-many relationship for the [synapselinkexternaltablestate](synapselinkexternaltablestate.md) table/entity.

### <a name="BKMK_synapselinkprofile_ProcessSession"></a> synapselinkprofile_ProcessSession

**Added by**: Synapse Link Solution

See the [synapselinkprofile_ProcessSession](synapselinkprofile.md#BKMK_synapselinkprofile_ProcessSession) one-to-many relationship for the [synapselinkprofile](synapselinkprofile.md) table/entity.

### <a name="BKMK_synapselinkprofileentity_ProcessSession"></a> synapselinkprofileentity_ProcessSession

**Added by**: Synapse Link Solution

See the [synapselinkprofileentity_ProcessSession](synapselinkprofileentity.md#BKMK_synapselinkprofileentity_ProcessSession) one-to-many relationship for the [synapselinkprofileentity](synapselinkprofileentity.md) table/entity.

### <a name="BKMK_synapselinkprofileentitystate_ProcessSession"></a> synapselinkprofileentitystate_ProcessSession

**Added by**: Synapse Link Solution

See the [synapselinkprofileentitystate_ProcessSession](synapselinkprofileentitystate.md#BKMK_synapselinkprofileentitystate_ProcessSession) one-to-many relationship for the [synapselinkprofileentitystate](synapselinkprofileentitystate.md) table/entity.

### <a name="BKMK_synapselinkschedule_ProcessSession"></a> synapselinkschedule_ProcessSession

**Added by**: Synapse Link Solution

See the [synapselinkschedule_ProcessSession](synapselinkschedule.md#BKMK_synapselinkschedule_ProcessSession) one-to-many relationship for the [synapselinkschedule](synapselinkschedule.md) table/entity.

### <a name="BKMK_msdyn_dataflow_ProcessSession"></a> msdyn_dataflow_ProcessSession

**Added by**: Dataflow Solution Solution

See the [msdyn_dataflow_ProcessSession](msdyn_dataflow.md#BKMK_msdyn_dataflow_ProcessSession) one-to-many relationship for the [msdyn_dataflow](msdyn_dataflow.md) table/entity.

### <a name="BKMK_msdyn_dataflowrefreshhistory_ProcessSession"></a> msdyn_dataflowrefreshhistory_ProcessSession

**Added by**: Dataflow Solution Solution

See the [msdyn_dataflowrefreshhistory_ProcessSession](msdyn_dataflowrefreshhistory.md#BKMK_msdyn_dataflowrefreshhistory_ProcessSession) one-to-many relationship for the [msdyn_dataflowrefreshhistory](msdyn_dataflowrefreshhistory.md) table/entity.

### <a name="BKMK_msdyn_entityrefreshhistory_ProcessSession"></a> msdyn_entityrefreshhistory_ProcessSession

**Added by**: Dataflow Solution Solution

See the [msdyn_entityrefreshhistory_ProcessSession](msdyn_entityrefreshhistory.md#BKMK_msdyn_entityrefreshhistory_ProcessSession) one-to-many relationship for the [msdyn_entityrefreshhistory](msdyn_entityrefreshhistory.md) table/entity.

### <a name="BKMK_sharedlinksetting_ProcessSession"></a> sharedlinksetting_ProcessSession

**Added by**: Access Team Solution

See the [sharedlinksetting_ProcessSession](sharedlinksetting.md#BKMK_sharedlinksetting_ProcessSession) one-to-many relationship for the [sharedlinksetting](sharedlinksetting.md) table/entity.

### <a name="BKMK_entityrecordfilter_ProcessSession"></a> entityrecordfilter_ProcessSession

**Added by**: AuthorizationCore Solution

See the [entityrecordfilter_ProcessSession](entityrecordfilter.md#BKMK_entityrecordfilter_ProcessSession) one-to-many relationship for the [entityrecordfilter](entityrecordfilter.md) table/entity.

### <a name="BKMK_recordfilter_ProcessSession"></a> recordfilter_ProcessSession

**Added by**: AuthorizationCore Solution

See the [recordfilter_ProcessSession](recordfilter.md#BKMK_recordfilter_ProcessSession) one-to-many relationship for the [recordfilter](recordfilter.md) table/entity.

### <a name="BKMK_delegatedauthorization_ProcessSession"></a> delegatedauthorization_ProcessSession

**Added by**: Delegated Authorization Solution

See the [delegatedauthorization_ProcessSession](delegatedauthorization.md#BKMK_delegatedauthorization_ProcessSession) one-to-many relationship for the [delegatedauthorization](delegatedauthorization.md) table/entity.

### <a name="BKMK_serviceplan_ProcessSession"></a> serviceplan_ProcessSession

**Added by**: License Enforcement Solution

See the [serviceplan_ProcessSession](serviceplan.md#BKMK_serviceplan_ProcessSession) one-to-many relationship for the [serviceplan](serviceplan.md) table/entity.

### <a name="BKMK_serviceplanmapping_ProcessSession"></a> serviceplanmapping_ProcessSession

**Added by**: License Enforcement Solution

See the [serviceplanmapping_ProcessSession](serviceplanmapping.md#BKMK_serviceplanmapping_ProcessSession) one-to-many relationship for the [serviceplanmapping](serviceplanmapping.md) table/entity.

### <a name="BKMK_applicationuser_ProcessSession"></a> applicationuser_ProcessSession

**Added by**: ApplicationUserSolution Solution

See the [applicationuser_ProcessSession](applicationuser.md#BKMK_applicationuser_ProcessSession) one-to-many relationship for the [applicationuser](applicationuser.md) table/entity.

### <a name="BKMK_connector_ProcessSession"></a> connector_ProcessSession

**Added by**: Power Connector Solution Solution

See the [connector_ProcessSession](connector.md#BKMK_connector_ProcessSession) one-to-many relationship for the [connector](connector.md) table/entity.

### <a name="BKMK_environmentvariabledefinition_ProcessSession"></a> environmentvariabledefinition_ProcessSession

**Added by**: Environment Variables Solution

See the [environmentvariabledefinition_ProcessSession](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_ProcessSession) one-to-many relationship for the [environmentvariabledefinition](environmentvariabledefinition.md) table/entity.

### <a name="BKMK_environmentvariablevalue_ProcessSession"></a> environmentvariablevalue_ProcessSession

**Added by**: Environment Variables Solution

See the [environmentvariablevalue_ProcessSession](environmentvariablevalue.md#BKMK_environmentvariablevalue_ProcessSession) one-to-many relationship for the [environmentvariablevalue](environmentvariablevalue.md) table/entity.

### <a name="BKMK_workflowbinary_ProcessSession"></a> workflowbinary_ProcessSession

**Added by**: Power Automate Extensions Workflow Binary package Solution

See the [workflowbinary_ProcessSession](workflowbinary.md#BKMK_workflowbinary_ProcessSession) one-to-many relationship for the [workflowbinary](workflowbinary.md) table/entity.

### <a name="BKMK_desktopflowmodule_ProcessSession"></a> desktopflowmodule_ProcessSession

**Added by**: Power Automate Extensions core package Solution

See the [desktopflowmodule_ProcessSession](desktopflowmodule.md#BKMK_desktopflowmodule_ProcessSession) one-to-many relationship for the [desktopflowmodule](desktopflowmodule.md) table/entity.

### <a name="BKMK_flowmachine_ProcessSession"></a> flowmachine_ProcessSession

**Added by**: Power Automate Extensions core package Solution

See the [flowmachine_ProcessSession](flowmachine.md#BKMK_flowmachine_ProcessSession) one-to-many relationship for the [flowmachine](flowmachine.md) table/entity.

### <a name="BKMK_flowmachinegroup_ProcessSession"></a> flowmachinegroup_ProcessSession

**Added by**: Power Automate Extensions core package Solution

See the [flowmachinegroup_ProcessSession](flowmachinegroup.md#BKMK_flowmachinegroup_ProcessSession) one-to-many relationship for the [flowmachinegroup](flowmachinegroup.md) table/entity.

### <a name="BKMK_flowmachineimage_ProcessSession"></a> flowmachineimage_ProcessSession

**Added by**: Power Automate Extensions core package Solution

See the [flowmachineimage_ProcessSession](flowmachineimage.md#BKMK_flowmachineimage_ProcessSession) one-to-many relationship for the [flowmachineimage](flowmachineimage.md) table/entity.

### <a name="BKMK_flowmachineimageversion_ProcessSession"></a> flowmachineimageversion_ProcessSession

**Added by**: Power Automate Extensions core package Solution

See the [flowmachineimageversion_ProcessSession](flowmachineimageversion.md#BKMK_flowmachineimageversion_ProcessSession) one-to-many relationship for the [flowmachineimageversion](flowmachineimageversion.md) table/entity.

### <a name="BKMK_flowmachinenetwork_ProcessSession"></a> flowmachinenetwork_ProcessSession

**Added by**: Power Automate Extensions core package Solution

See the [flowmachinenetwork_ProcessSession](flowmachinenetwork.md#BKMK_flowmachinenetwork_ProcessSession) one-to-many relationship for the [flowmachinenetwork](flowmachinenetwork.md) table/entity.

### <a name="BKMK_processstageparameter_ProcessSession"></a> processstageparameter_ProcessSession

**Added by**: Power Automate Extensions core package Solution

See the [processstageparameter_ProcessSession](processstageparameter.md#BKMK_processstageparameter_ProcessSession) one-to-many relationship for the [processstageparameter](processstageparameter.md) table/entity.

### <a name="BKMK_workqueue_ProcessSession"></a> workqueue_ProcessSession

**Added by**: Power Automate Extensions core package Solution

See the [workqueue_ProcessSession](workqueue.md#BKMK_workqueue_ProcessSession) one-to-many relationship for the [workqueue](workqueue.md) table/entity.

### <a name="BKMK_workqueueitem_ProcessSession"></a> workqueueitem_ProcessSession

**Added by**: Power Automate Extensions core package Solution

See the [workqueueitem_ProcessSession](workqueueitem.md#BKMK_workqueueitem_ProcessSession) one-to-many relationship for the [workqueueitem](workqueueitem.md) table/entity.

### <a name="BKMK_desktopflowbinary_ProcessSession"></a> desktopflowbinary_ProcessSession

**Added by**: Power Automate Extensions core package Solution

See the [desktopflowbinary_ProcessSession](desktopflowbinary.md#BKMK_desktopflowbinary_ProcessSession) one-to-many relationship for the [desktopflowbinary](desktopflowbinary.md) table/entity.

### <a name="BKMK_connectionreference_ProcessSession"></a> connectionreference_ProcessSession

**Added by**: Power Platform Connection References Solution

See the [connectionreference_ProcessSession](connectionreference.md#BKMK_connectionreference_ProcessSession) one-to-many relationship for the [connectionreference](connectionreference.md) table/entity.

### <a name="BKMK_connectioninstance_ProcessSession"></a> connectioninstance_ProcessSession

**Added by**: Connection Instance Solution Solution

See the [connectioninstance_ProcessSession](connectioninstance.md#BKMK_connectioninstance_ProcessSession) one-to-many relationship for the [connectioninstance](connectioninstance.md) table/entity.

### <a name="BKMK_msdyn_helppage_ProcessSession"></a> msdyn_helppage_ProcessSession

**Added by**: Contextual Help Solution

See the [msdyn_helppage_ProcessSession](msdyn_helppage.md#BKMK_msdyn_helppage_ProcessSession) one-to-many relationship for the [msdyn_helppage](msdyn_helppage.md) table/entity.

### <a name="BKMK_msdyn_tour_ProcessSession"></a> msdyn_tour_ProcessSession

**Added by**: Contextual Help Solution

See the [msdyn_tour_ProcessSession](msdyn_tour.md#BKMK_msdyn_tour_ProcessSession) one-to-many relationship for the [msdyn_tour](msdyn_tour.md) table/entity.

### <a name="BKMK_msdynce_botcontent_ProcessSession"></a> msdynce_botcontent_ProcessSession

**Added by**: Customer Care Intelligence Bots Solution

See the [msdynce_botcontent_ProcessSession](msdynce_botcontent.md#BKMK_msdynce_botcontent_ProcessSession) one-to-many relationship for the [msdynce_botcontent](msdynce_botcontent.md) table/entity.

### <a name="BKMK_conversationtranscript_ProcessSession"></a> conversationtranscript_ProcessSession

**Added by**: Power Virtual Agents Common Solution

See the [conversationtranscript_ProcessSession](conversationtranscript.md#BKMK_conversationtranscript_ProcessSession) one-to-many relationship for the [conversationtranscript](conversationtranscript.md) table/entity.

### <a name="BKMK_bot_ProcessSession"></a> bot_ProcessSession

**Added by**: Power Virtual Agents Solution

See the [bot_ProcessSession](bot.md#BKMK_bot_ProcessSession) one-to-many relationship for the [bot](bot.md) table/entity.

### <a name="BKMK_botcomponent_ProcessSession"></a> botcomponent_ProcessSession

**Added by**: Power Virtual Agents Solution

See the [botcomponent_ProcessSession](botcomponent.md#BKMK_botcomponent_ProcessSession) one-to-many relationship for the [botcomponent](botcomponent.md) table/entity.

### <a name="BKMK_Territory_ProcessSessions"></a> Territory_ProcessSessions

**Added by**: Application Common Solution

See the [Territory_ProcessSessions](territory.md#BKMK_Territory_ProcessSessions) one-to-many relationship for the [territory](territory.md) table/entity.

### <a name="BKMK_activityfileattachment_ProcessSession"></a> activityfileattachment_ProcessSession

**Added by**: Activities Patch Solution

See the [activityfileattachment_ProcessSession](activityfileattachment.md#BKMK_activityfileattachment_ProcessSession) one-to-many relationship for the [activityfileattachment](activityfileattachment.md) table/entity.

### <a name="BKMK_chat_ProcessSession"></a> chat_ProcessSession

**Added by**: Activities Patch Solution

See the [chat_ProcessSession](chat.md#BKMK_chat_ProcessSession) one-to-many relationship for the [chat](chat.md) table/entity.

### <a name="BKMK_msdyn_serviceconfiguration_ProcessSession"></a> msdyn_serviceconfiguration_ProcessSession

**Added by**: Service Level Agreement (SLA) Extension Solution

See the [msdyn_serviceconfiguration_ProcessSession](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_ProcessSession) one-to-many relationship for the [msdyn_serviceconfiguration](msdyn_serviceconfiguration.md) table/entity.

### <a name="BKMK_msdyn_slakpi_ProcessSession"></a> msdyn_slakpi_ProcessSession

**Added by**: Service Level Agreement (SLA) Extension Solution

See the [msdyn_slakpi_ProcessSession](msdyn_slakpi.md#BKMK_msdyn_slakpi_ProcessSession) one-to-many relationship for the [msdyn_slakpi](msdyn_slakpi.md) table/entity.

### <a name="BKMK_msdyn_knowledgemanagementsetting_ProcessSession"></a> msdyn_knowledgemanagementsetting_ProcessSession

**Added by**: Knowledge Management Patch Solution

See the [msdyn_knowledgemanagementsetting_ProcessSession](msdyn_knowledgemanagementsetting.md#BKMK_msdyn_knowledgemanagementsetting_ProcessSession) one-to-many relationship for the [msdyn_knowledgemanagementsetting](msdyn_knowledgemanagementsetting.md) table/entity.

### <a name="BKMK_msdyn_federatedarticle_ProcessSession"></a> msdyn_federatedarticle_ProcessSession

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_federatedarticle_ProcessSession](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_ProcessSession) one-to-many relationship for the [msdyn_federatedarticle](msdyn_federatedarticle.md) table/entity.

### <a name="BKMK_msdyn_federatedarticleincident_ProcessSession"></a> msdyn_federatedarticleincident_ProcessSession

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_federatedarticleincident_ProcessSession](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_ProcessSession) one-to-many relationship for the [msdyn_federatedarticleincident](msdyn_federatedarticleincident.md) table/entity.

### <a name="BKMK_msdyn_integratedsearchprovider_ProcessSession"></a> msdyn_integratedsearchprovider_ProcessSession

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_integratedsearchprovider_ProcessSession](msdyn_integratedsearchprovider.md#BKMK_msdyn_integratedsearchprovider_ProcessSession) one-to-many relationship for the [msdyn_integratedsearchprovider](msdyn_integratedsearchprovider.md) table/entity.

### <a name="BKMK_msdyn_kmfederatedsearchconfig_ProcessSession"></a> msdyn_kmfederatedsearchconfig_ProcessSession

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_kmfederatedsearchconfig_ProcessSession](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_ProcessSession) one-to-many relationship for the [msdyn_kmfederatedsearchconfig](msdyn_kmfederatedsearchconfig.md) table/entity.

### <a name="BKMK_msdyn_knowledgearticleimage_ProcessSession"></a> msdyn_knowledgearticleimage_ProcessSession

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgearticleimage_ProcessSession](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_ProcessSession) one-to-many relationship for the [msdyn_knowledgearticleimage](msdyn_knowledgearticleimage.md) table/entity.

### <a name="BKMK_msdyn_knowledgeconfiguration_ProcessSession"></a> msdyn_knowledgeconfiguration_ProcessSession

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgeconfiguration_ProcessSession](msdyn_knowledgeconfiguration.md#BKMK_msdyn_knowledgeconfiguration_ProcessSession) one-to-many relationship for the [msdyn_knowledgeconfiguration](msdyn_knowledgeconfiguration.md) table/entity.

### <a name="BKMK_msdyn_knowledgeinteractioninsight_ProcessSession"></a> msdyn_knowledgeinteractioninsight_ProcessSession

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgeinteractioninsight_ProcessSession](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_ProcessSession) one-to-many relationship for the [msdyn_knowledgeinteractioninsight](msdyn_knowledgeinteractioninsight.md) table/entity.

### <a name="BKMK_msdyn_knowledgesearchinsight_ProcessSession"></a> msdyn_knowledgesearchinsight_ProcessSession

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgesearchinsight_ProcessSession](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_ProcessSession) one-to-many relationship for the [msdyn_knowledgesearchinsight](msdyn_knowledgesearchinsight.md) table/entity.

### <a name="BKMK_msdyn_favoriteknowledgearticle_ProcessSession"></a> msdyn_favoriteknowledgearticle_ProcessSession

**Added by**: Knowledge Management Features Solution

See the [msdyn_favoriteknowledgearticle_ProcessSession](msdyn_favoriteknowledgearticle.md#BKMK_msdyn_favoriteknowledgearticle_ProcessSession) one-to-many relationship for the [msdyn_favoriteknowledgearticle](msdyn_favoriteknowledgearticle.md) table/entity.

### <a name="BKMK_msdyn_kalanguagesetting_ProcessSession"></a> msdyn_kalanguagesetting_ProcessSession

**Added by**: Knowledge Management Features Solution

See the [msdyn_kalanguagesetting_ProcessSession](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_ProcessSession) one-to-many relationship for the [msdyn_kalanguagesetting](msdyn_kalanguagesetting.md) table/entity.

### <a name="BKMK_msdyn_kbattachment_ProcessSession"></a> msdyn_kbattachment_ProcessSession

**Added by**: Knowledge Management Features Solution

See the [msdyn_kbattachment_ProcessSession](msdyn_kbattachment.md#BKMK_msdyn_kbattachment_ProcessSession) one-to-many relationship for the [msdyn_kbattachment](msdyn_kbattachment.md) table/entity.

### <a name="BKMK_msdyn_kmpersonalizationsetting_ProcessSession"></a> msdyn_kmpersonalizationsetting_ProcessSession

**Added by**: Knowledge Management Features Solution

See the [msdyn_kmpersonalizationsetting_ProcessSession](msdyn_kmpersonalizationsetting.md#BKMK_msdyn_kmpersonalizationsetting_ProcessSession) one-to-many relationship for the [msdyn_kmpersonalizationsetting](msdyn_kmpersonalizationsetting.md) table/entity.

### <a name="BKMK_msdyn_knowledgearticletemplate_ProcessSession"></a> msdyn_knowledgearticletemplate_ProcessSession

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgearticletemplate_ProcessSession](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_ProcessSession) one-to-many relationship for the [msdyn_knowledgearticletemplate](msdyn_knowledgearticletemplate.md) table/entity.

### <a name="BKMK_msdyn_knowledgepersonalfilter_ProcessSession"></a> msdyn_knowledgepersonalfilter_ProcessSession

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgepersonalfilter_ProcessSession](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_ProcessSession) one-to-many relationship for the [msdyn_knowledgepersonalfilter](msdyn_knowledgepersonalfilter.md) table/entity.

### <a name="BKMK_msdyn_knowledgesearchfilter_ProcessSession"></a> msdyn_knowledgesearchfilter_ProcessSession

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgesearchfilter_ProcessSession](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_ProcessSession) one-to-many relationship for the [msdyn_knowledgesearchfilter](msdyn_knowledgesearchfilter.md) table/entity.

### <a name="BKMK_fxexpression_ProcessSession"></a> fxexpression_ProcessSession

**Added by**: msft_PowerfxRuleSolution Solution

See the [fxexpression_ProcessSession](fxexpression.md#BKMK_fxexpression_ProcessSession) one-to-many relationship for the [fxexpression](fxexpression.md) table/entity.

### <a name="BKMK_powerfxrule_ProcessSession"></a> powerfxrule_ProcessSession

**Added by**: msft_PowerfxRuleSolution Solution

See the [powerfxrule_ProcessSession](powerfxrule.md#BKMK_powerfxrule_ProcessSession) one-to-many relationship for the [powerfxrule](powerfxrule.md) table/entity.

### <a name="BKMK_keyvaultreference_ProcessSession"></a> keyvaultreference_ProcessSession

**Added by**: ManagedIdentityExtensions Solution

See the [keyvaultreference_ProcessSession](keyvaultreference.md#BKMK_keyvaultreference_ProcessSession) one-to-many relationship for the [keyvaultreference](keyvaultreference.md) table/entity.

### <a name="BKMK_managedidentity_ProcessSession"></a> managedidentity_ProcessSession

**Added by**: ManagedIdentityExtensions Solution

See the [managedidentity_ProcessSession](managedidentity.md#BKMK_managedidentity_ProcessSession) one-to-many relationship for the [managedidentity](managedidentity.md) table/entity.

### <a name="BKMK_msgraphresourcetosubscription_ProcessSession"></a> msgraphresourcetosubscription_ProcessSession

**Added by**: msft_ActivitiesInfra_Extensions Solution

See the [msgraphresourcetosubscription_ProcessSession](msgraphresourcetosubscription.md#BKMK_msgraphresourcetosubscription_ProcessSession) one-to-many relationship for the [msgraphresourcetosubscription](msgraphresourcetosubscription.md) table/entity.

### <a name="BKMK_virtualentitymetadata_ProcessSession"></a> virtualentitymetadata_ProcessSession

**Added by**: RuntimeIntegration Solution

See the [virtualentitymetadata_ProcessSession](virtualentitymetadata.md#BKMK_virtualentitymetadata_ProcessSession) one-to-many relationship for the [virtualentitymetadata](virtualentitymetadata.md) table/entity.

### <a name="BKMK_mobileofflineprofileextension_ProcessSession"></a> mobileofflineprofileextension_ProcessSession

**Added by**: MobileOfflineProfileExtensionSolution Solution

See the [mobileofflineprofileextension_ProcessSession](mobileofflineprofileextension.md#BKMK_mobileofflineprofileextension_ProcessSession) one-to-many relationship for the [mobileofflineprofileextension](mobileofflineprofileextension.md) table/entity.

### <a name="BKMK_teammobileofflineprofilemembership_ProcessSession"></a> teammobileofflineprofilemembership_ProcessSession

**Added by**: MobileOfflineMembership Solution

See the [teammobileofflineprofilemembership_ProcessSession](teammobileofflineprofilemembership.md#BKMK_teammobileofflineprofilemembership_ProcessSession) one-to-many relationship for the [teammobileofflineprofilemembership](teammobileofflineprofilemembership.md) table/entity.

### <a name="BKMK_usermobileofflineprofilemembership_ProcessSession"></a> usermobileofflineprofilemembership_ProcessSession

**Added by**: MobileOfflineMembership Solution

See the [usermobileofflineprofilemembership_ProcessSession](usermobileofflineprofilemembership.md#BKMK_usermobileofflineprofilemembership_ProcessSession) one-to-many relationship for the [usermobileofflineprofilemembership](usermobileofflineprofilemembership.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscription_ProcessSession"></a> organizationdatasyncsubscription_ProcessSession

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscription_ProcessSession](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_ProcessSession) one-to-many relationship for the [organizationdatasyncsubscription](organizationdatasyncsubscription.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscriptionentity_ProcessSession"></a> organizationdatasyncsubscriptionentity_ProcessSession

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscriptionentity_ProcessSession](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_ProcessSession) one-to-many relationship for the [organizationdatasyncsubscriptionentity](organizationdatasyncsubscriptionentity.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_ProcessSession"></a> organizationdatasyncsubscriptionfnotable_ProcessSession

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscriptionfnotable_ProcessSession](organizationdatasyncsubscriptionfnotable.md#BKMK_organizationdatasyncsubscriptionfnotable_ProcessSession) one-to-many relationship for the [organizationdatasyncsubscriptionfnotable](organizationdatasyncsubscriptionfnotable.md) table/entity.

### <a name="BKMK_organizationdatasyncfnostate_ProcessSession"></a> organizationdatasyncfnostate_ProcessSession

**Added by**: DataSyncState Solution

See the [organizationdatasyncfnostate_ProcessSession](organizationdatasyncfnostate.md#BKMK_organizationdatasyncfnostate_ProcessSession) one-to-many relationship for the [organizationdatasyncfnostate](organizationdatasyncfnostate.md) table/entity.

### <a name="BKMK_organizationdatasyncstate_ProcessSession"></a> organizationdatasyncstate_ProcessSession

**Added by**: DataSyncState Solution

See the [organizationdatasyncstate_ProcessSession](organizationdatasyncstate.md#BKMK_organizationdatasyncstate_ProcessSession) one-to-many relationship for the [organizationdatasyncstate](organizationdatasyncstate.md) table/entity.

### <a name="BKMK_metadataforarchival_ProcessSession"></a> metadataforarchival_ProcessSession

**Added by**: Retention Base Components Solution

See the [metadataforarchival_ProcessSession](metadataforarchival.md#BKMK_metadataforarchival_ProcessSession) one-to-many relationship for the [metadataforarchival](metadataforarchival.md) table/entity.

### <a name="BKMK_retentionconfig_ProcessSession"></a> retentionconfig_ProcessSession

**Added by**: Retention Base Components Solution

See the [retentionconfig_ProcessSession](retentionconfig.md#BKMK_retentionconfig_ProcessSession) one-to-many relationship for the [retentionconfig](retentionconfig.md) table/entity.

### <a name="BKMK_retentionfailuredetail_ProcessSession"></a> retentionfailuredetail_ProcessSession

**Added by**: Retention Base Components Solution

See the [retentionfailuredetail_ProcessSession](retentionfailuredetail.md#BKMK_retentionfailuredetail_ProcessSession) one-to-many relationship for the [retentionfailuredetail](retentionfailuredetail.md) table/entity.

### <a name="BKMK_retentionoperation_ProcessSession"></a> retentionoperation_ProcessSession

**Added by**: Retention Base Components Solution

See the [retentionoperation_ProcessSession](retentionoperation.md#BKMK_retentionoperation_ProcessSession) one-to-many relationship for the [retentionoperation](retentionoperation.md) table/entity.

### <a name="BKMK_retentionoperationdetail_ProcessSession"></a> retentionoperationdetail_ProcessSession

**Added by**: Retention Base Components Solution

See the [retentionoperationdetail_ProcessSession](retentionoperationdetail.md#BKMK_retentionoperationdetail_ProcessSession) one-to-many relationship for the [retentionoperationdetail](retentionoperationdetail.md) table/entity.

### <a name="BKMK_msdyn_appinsightsmetadata_ProcessSession"></a> msdyn_appinsightsmetadata_ProcessSession

**Added by**: Insights App Platform Solution

See the [msdyn_appinsightsmetadata_ProcessSession](msdyn_appinsightsmetadata.md#BKMK_msdyn_appinsightsmetadata_ProcessSession) one-to-many relationship for the [msdyn_appinsightsmetadata](msdyn_appinsightsmetadata.md) table/entity.

### <a name="BKMK_msdyn_dataflowtemplate_ProcessSession"></a> msdyn_dataflowtemplate_ProcessSession

**Added by**: Insights App Platform Solution

See the [msdyn_dataflowtemplate_ProcessSession](msdyn_dataflowtemplate.md#BKMK_msdyn_dataflowtemplate_ProcessSession) one-to-many relationship for the [msdyn_dataflowtemplate](msdyn_dataflowtemplate.md) table/entity.

### <a name="BKMK_msdyn_workflowactionstatus_ProcessSession"></a> msdyn_workflowactionstatus_ProcessSession

**Added by**: Insights App Platform Solution

See the [msdyn_workflowactionstatus_ProcessSession](msdyn_workflowactionstatus.md#BKMK_msdyn_workflowactionstatus_ProcessSession) one-to-many relationship for the [msdyn_workflowactionstatus](msdyn_workflowactionstatus.md) table/entity.

### <a name="BKMK_userrating_ProcessSession"></a> userrating_ProcessSession

**Added by**: User Rating Solution

See the [userrating_ProcessSession](userrating.md#BKMK_userrating_ProcessSession) one-to-many relationship for the [userrating](userrating.md) table/entity.

### <a name="BKMK_msdyn_mobileapp_ProcessSession"></a> msdyn_mobileapp_ProcessSession

**Added by**: Mobile Apps Solution Solution

See the [msdyn_mobileapp_ProcessSession](msdyn_mobileapp.md#BKMK_msdyn_mobileapp_ProcessSession) one-to-many relationship for the [msdyn_mobileapp](msdyn_mobileapp.md) table/entity.

### <a name="BKMK_msdyn_insightsstorevirtualentity_ProcessSession"></a> msdyn_insightsstorevirtualentity_ProcessSession

**Added by**: Insights Store Data Provider Solution

See the [msdyn_insightsstorevirtualentity_ProcessSession](msdyn_insightsstorevirtualentity.md#BKMK_msdyn_insightsstorevirtualentity_ProcessSession) one-to-many relationship for the [msdyn_insightsstorevirtualentity](msdyn_insightsstorevirtualentity.md) table/entity.

### <a name="BKMK_roleeditorlayout_ProcessSession"></a> roleeditorlayout_ProcessSession

**Added by**: Role Editor Solution

See the [roleeditorlayout_ProcessSession](roleeditorlayout.md#BKMK_roleeditorlayout_ProcessSession) one-to-many relationship for the [roleeditorlayout](roleeditorlayout.md) table/entity.

### <a name="BKMK_appaction_ProcessSession"></a> appaction_ProcessSession

**Added by**: Power Apps Actions Solution

See the [appaction_ProcessSession](appaction.md#BKMK_appaction_ProcessSession) one-to-many relationship for the [appaction](appaction.md) table/entity.

### <a name="BKMK_appactionmigration_ProcessSession"></a> appactionmigration_ProcessSession

**Added by**: Power Apps Actions Solution

See the [appactionmigration_ProcessSession](appactionmigration.md#BKMK_appactionmigration_ProcessSession) one-to-many relationship for the [appactionmigration](appactionmigration.md) table/entity.

### <a name="BKMK_appactionrule_ProcessSession"></a> appactionrule_ProcessSession

**Added by**: Power Apps Actions Solution

See the [appactionrule_ProcessSession](appactionrule.md#BKMK_appactionrule_ProcessSession) one-to-many relationship for the [appactionrule](appactionrule.md) table/entity.

### <a name="BKMK_card_ProcessSession"></a> card_ProcessSession

**Added by**: Power Apps cards Solution

See the [card_ProcessSession](card.md#BKMK_card_ProcessSession) one-to-many relationship for the [card](card.md) table/entity.

### <a name="BKMK_msdyn_entitylinkchatconfiguration_ProcessSession"></a> msdyn_entitylinkchatconfiguration_ProcessSession

**Added by**: Teams Chat Settings Solution Solution

See the [msdyn_entitylinkchatconfiguration_ProcessSession](msdyn_entitylinkchatconfiguration.md#BKMK_msdyn_entitylinkchatconfiguration_ProcessSession) one-to-many relationship for the [msdyn_entitylinkchatconfiguration](msdyn_entitylinkchatconfiguration.md) table/entity.

### <a name="BKMK_msdyn_richtextfile_ProcessSession"></a> msdyn_richtextfile_ProcessSession

**Added by**: Rich Text Editor Solution

See the [msdyn_richtextfile_ProcessSession](msdyn_richtextfile.md#BKMK_msdyn_richtextfile_ProcessSession) one-to-many relationship for the [msdyn_richtextfile](msdyn_richtextfile.md) table/entity.

### <a name="BKMK_msdyn_customcontrolextendedsettings_ProcessSession"></a> msdyn_customcontrolextendedsettings_ProcessSession

**Added by**: User Experiences Extended Settings Solution

See the [msdyn_customcontrolextendedsettings_ProcessSession](msdyn_customcontrolextendedsettings.md#BKMK_msdyn_customcontrolextendedsettings_ProcessSession) one-to-many relationship for the [msdyn_customcontrolextendedsettings](msdyn_customcontrolextendedsettings.md) table/entity.

### <a name="BKMK_searchrelationshipsettings_ProcessSession"></a> searchrelationshipsettings_ProcessSession

**Added by**: msdyn_RelevanceSearch Solution

See the [searchrelationshipsettings_ProcessSession](searchrelationshipsettings.md#BKMK_searchrelationshipsettings_ProcessSession) one-to-many relationship for the [searchrelationshipsettings](searchrelationshipsettings.md) table/entity.

### <a name="BKMK_msdyn_virtualtablecolumncandidate_ProcessSession"></a> msdyn_virtualtablecolumncandidate_ProcessSession

**Added by**: Virtual Connector Provider Solution

See the [msdyn_virtualtablecolumncandidate_ProcessSession](msdyn_virtualtablecolumncandidate.md#BKMK_msdyn_virtualtablecolumncandidate_ProcessSession) one-to-many relationship for the [msdyn_virtualtablecolumncandidate](msdyn_virtualtablecolumncandidate.md) table/entity.

### <a name="BKMK_msdyn_aiconfiguration_ProcessSession"></a> msdyn_aiconfiguration_ProcessSession

**Added by**: AISolution Solution

See the [msdyn_aiconfiguration_ProcessSession](msdyn_aiconfiguration.md#BKMK_msdyn_aiconfiguration_ProcessSession) one-to-many relationship for the [msdyn_aiconfiguration](msdyn_aiconfiguration.md) table/entity.

### <a name="BKMK_msdyn_aievent_ProcessSession"></a> msdyn_aievent_ProcessSession

**Added by**: AISolution Solution

See the [msdyn_aievent_ProcessSession](msdyn_aievent.md#BKMK_msdyn_aievent_ProcessSession) one-to-many relationship for the [msdyn_aievent](msdyn_aievent.md) table/entity.

### <a name="BKMK_msdyn_aimodel_ProcessSession"></a> msdyn_aimodel_ProcessSession

**Added by**: AISolution Solution

See the [msdyn_aimodel_ProcessSession](msdyn_aimodel.md#BKMK_msdyn_aimodel_ProcessSession) one-to-many relationship for the [msdyn_aimodel](msdyn_aimodel.md) table/entity.

### <a name="BKMK_msdyn_aitemplate_ProcessSession"></a> msdyn_aitemplate_ProcessSession

**Added by**: AISolution Solution

See the [msdyn_aitemplate_ProcessSession](msdyn_aitemplate.md#BKMK_msdyn_aitemplate_ProcessSession) one-to-many relationship for the [msdyn_aitemplate](msdyn_aitemplate.md) table/entity.

### <a name="BKMK_msdyn_aibfeedbackloop_ProcessSession"></a> msdyn_aibfeedbackloop_ProcessSession

**Added by**: AISolutionFullAdditions Solution

See the [msdyn_aibfeedbackloop_ProcessSession](msdyn_aibfeedbackloop.md#BKMK_msdyn_aibfeedbackloop_ProcessSession) one-to-many relationship for the [msdyn_aibfeedbackloop](msdyn_aibfeedbackloop.md) table/entity.

### <a name="BKMK_msdyn_aifptrainingdocument_ProcessSession"></a> msdyn_aifptrainingdocument_ProcessSession

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aifptrainingdocument_ProcessSession](msdyn_aifptrainingdocument.md#BKMK_msdyn_aifptrainingdocument_ProcessSession) one-to-many relationship for the [msdyn_aifptrainingdocument](msdyn_aifptrainingdocument.md) table/entity.

### <a name="BKMK_msdyn_aiodimage_ProcessSession"></a> msdyn_aiodimage_ProcessSession

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodimage_ProcessSession](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_ProcessSession) one-to-many relationship for the [msdyn_aiodimage](msdyn_aiodimage.md) table/entity.

### <a name="BKMK_msdyn_aiodlabel_ProcessSession"></a> msdyn_aiodlabel_ProcessSession

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodlabel_ProcessSession](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_ProcessSession) one-to-many relationship for the [msdyn_aiodlabel](msdyn_aiodlabel.md) table/entity.

### <a name="BKMK_msdyn_aiodtrainingboundingbox_ProcessSession"></a> msdyn_aiodtrainingboundingbox_ProcessSession

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodtrainingboundingbox_ProcessSession](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_ProcessSession) one-to-many relationship for the [msdyn_aiodtrainingboundingbox](msdyn_aiodtrainingboundingbox.md) table/entity.

### <a name="BKMK_msdyn_aiodtrainingimage_ProcessSession"></a> msdyn_aiodtrainingimage_ProcessSession

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodtrainingimage_ProcessSession](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_ProcessSession) one-to-many relationship for the [msdyn_aiodtrainingimage](msdyn_aiodtrainingimage.md) table/entity.

### <a name="BKMK_msdyn_aibdataset_ProcessSession"></a> msdyn_aibdataset_ProcessSession

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdataset_ProcessSession](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_ProcessSession) one-to-many relationship for the [msdyn_aibdataset](msdyn_aibdataset.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetfile_ProcessSession"></a> msdyn_aibdatasetfile_ProcessSession

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetfile_ProcessSession](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_ProcessSession) one-to-many relationship for the [msdyn_aibdatasetfile](msdyn_aibdatasetfile.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetrecord_ProcessSession"></a> msdyn_aibdatasetrecord_ProcessSession

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetrecord_ProcessSession](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_ProcessSession) one-to-many relationship for the [msdyn_aibdatasetrecord](msdyn_aibdatasetrecord.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetscontainer_ProcessSession"></a> msdyn_aibdatasetscontainer_ProcessSession

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetscontainer_ProcessSession](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_ProcessSession) one-to-many relationship for the [msdyn_aibdatasetscontainer](msdyn_aibdatasetscontainer.md) table/entity.

### <a name="BKMK_msdyn_aibfile_ProcessSession"></a> msdyn_aibfile_ProcessSession

**Added by**: AI Solution default templates Solution

See the [msdyn_aibfile_ProcessSession](msdyn_aibfile.md#BKMK_msdyn_aibfile_ProcessSession) one-to-many relationship for the [msdyn_aibfile](msdyn_aibfile.md) table/entity.

### <a name="BKMK_msdyn_aibfileattacheddata_ProcessSession"></a> msdyn_aibfileattacheddata_ProcessSession

**Added by**: AI Solution default templates Solution

See the [msdyn_aibfileattacheddata_ProcessSession](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_ProcessSession) one-to-many relationship for the [msdyn_aibfileattacheddata](msdyn_aibfileattacheddata.md) table/entity.

### <a name="BKMK_msdyn_pmanalysishistory_ProcessSession"></a> msdyn_pmanalysishistory_ProcessSession

**Added by**: Process Mining Solution

See the [msdyn_pmanalysishistory_ProcessSession](msdyn_pmanalysishistory.md#BKMK_msdyn_pmanalysishistory_ProcessSession) one-to-many relationship for the [msdyn_pmanalysishistory](msdyn_pmanalysishistory.md) table/entity.

### <a name="BKMK_msdyn_pmcalendar_ProcessSession"></a> msdyn_pmcalendar_ProcessSession

**Added by**: Process Mining Solution

See the [msdyn_pmcalendar_ProcessSession](msdyn_pmcalendar.md#BKMK_msdyn_pmcalendar_ProcessSession) one-to-many relationship for the [msdyn_pmcalendar](msdyn_pmcalendar.md) table/entity.

### <a name="BKMK_msdyn_pmcalendarversion_ProcessSession"></a> msdyn_pmcalendarversion_ProcessSession

**Added by**: Process Mining Solution

See the [msdyn_pmcalendarversion_ProcessSession](msdyn_pmcalendarversion.md#BKMK_msdyn_pmcalendarversion_ProcessSession) one-to-many relationship for the [msdyn_pmcalendarversion](msdyn_pmcalendarversion.md) table/entity.

### <a name="BKMK_msdyn_pminferredtask_ProcessSession"></a> msdyn_pminferredtask_ProcessSession

**Added by**: Process Mining Solution

See the [msdyn_pminferredtask_ProcessSession](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_ProcessSession) one-to-many relationship for the [msdyn_pminferredtask](msdyn_pminferredtask.md) table/entity.

### <a name="BKMK_msdyn_pmprocessextendedmetadataversion_ProcessSession"></a> msdyn_pmprocessextendedmetadataversion_ProcessSession

**Added by**: Process Mining Solution

See the [msdyn_pmprocessextendedmetadataversion_ProcessSession](msdyn_pmprocessextendedmetadataversion.md#BKMK_msdyn_pmprocessextendedmetadataversion_ProcessSession) one-to-many relationship for the [msdyn_pmprocessextendedmetadataversion](msdyn_pmprocessextendedmetadataversion.md) table/entity.

### <a name="BKMK_msdyn_pmprocesstemplate_ProcessSession"></a> msdyn_pmprocesstemplate_ProcessSession

**Added by**: Process Mining Solution

See the [msdyn_pmprocesstemplate_ProcessSession](msdyn_pmprocesstemplate.md#BKMK_msdyn_pmprocesstemplate_ProcessSession) one-to-many relationship for the [msdyn_pmprocesstemplate](msdyn_pmprocesstemplate.md) table/entity.

### <a name="BKMK_msdyn_pmprocessusersettings_ProcessSession"></a> msdyn_pmprocessusersettings_ProcessSession

**Added by**: Process Mining Solution

See the [msdyn_pmprocessusersettings_ProcessSession](msdyn_pmprocessusersettings.md#BKMK_msdyn_pmprocessusersettings_ProcessSession) one-to-many relationship for the [msdyn_pmprocessusersettings](msdyn_pmprocessusersettings.md) table/entity.

### <a name="BKMK_msdyn_pmprocessversion_ProcessSession"></a> msdyn_pmprocessversion_ProcessSession

**Added by**: Process Mining Solution

See the [msdyn_pmprocessversion_ProcessSession](msdyn_pmprocessversion.md#BKMK_msdyn_pmprocessversion_ProcessSession) one-to-many relationship for the [msdyn_pmprocessversion](msdyn_pmprocessversion.md) table/entity.

### <a name="BKMK_msdyn_pmrecording_ProcessSession"></a> msdyn_pmrecording_ProcessSession

**Added by**: Process Mining Solution

See the [msdyn_pmrecording_ProcessSession](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_ProcessSession) one-to-many relationship for the [msdyn_pmrecording](msdyn_pmrecording.md) table/entity.

### <a name="BKMK_msdyn_pmtemplate_ProcessSession"></a> msdyn_pmtemplate_ProcessSession

**Added by**: Process Mining Solution

See the [msdyn_pmtemplate_ProcessSession](msdyn_pmtemplate.md#BKMK_msdyn_pmtemplate_ProcessSession) one-to-many relationship for the [msdyn_pmtemplate](msdyn_pmtemplate.md) table/entity.

### <a name="BKMK_msdyn_pmview_ProcessSession"></a> msdyn_pmview_ProcessSession

**Added by**: Process Mining Solution

See the [msdyn_pmview_ProcessSession](msdyn_pmview.md#BKMK_msdyn_pmview_ProcessSession) one-to-many relationship for the [msdyn_pmview](msdyn_pmview.md) table/entity.

### <a name="BKMK_msdyn_analysiscomponent_ProcessSession"></a> msdyn_analysiscomponent_ProcessSession

**Added by**: Power Apps Checker Solution

See the [msdyn_analysiscomponent_ProcessSession](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_ProcessSession) one-to-many relationship for the [msdyn_analysiscomponent](msdyn_analysiscomponent.md) table/entity.

### <a name="BKMK_msdyn_analysisjob_ProcessSession"></a> msdyn_analysisjob_ProcessSession

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisjob_ProcessSession](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_ProcessSession) one-to-many relationship for the [msdyn_analysisjob](msdyn_analysisjob.md) table/entity.

### <a name="BKMK_msdyn_analysisoverride_ProcessSession"></a> msdyn_analysisoverride_ProcessSession

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisoverride_ProcessSession](msdyn_analysisoverride.md#BKMK_msdyn_analysisoverride_ProcessSession) one-to-many relationship for the [msdyn_analysisoverride](msdyn_analysisoverride.md) table/entity.

### <a name="BKMK_msdyn_analysisresult_ProcessSession"></a> msdyn_analysisresult_ProcessSession

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisresult_ProcessSession](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_ProcessSession) one-to-many relationship for the [msdyn_analysisresult](msdyn_analysisresult.md) table/entity.

### <a name="BKMK_msdyn_analysisresultdetail_ProcessSession"></a> msdyn_analysisresultdetail_ProcessSession

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisresultdetail_ProcessSession](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_ProcessSession) one-to-many relationship for the [msdyn_analysisresultdetail](msdyn_analysisresultdetail.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthrule_ProcessSession"></a> msdyn_solutionhealthrule_ProcessSession

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthrule_ProcessSession](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_ProcessSession) one-to-many relationship for the [msdyn_solutionhealthrule](msdyn_solutionhealthrule.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthruleargument_ProcessSession"></a> msdyn_solutionhealthruleargument_ProcessSession

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthruleargument_ProcessSession](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_ProcessSession) one-to-many relationship for the [msdyn_solutionhealthruleargument](msdyn_solutionhealthruleargument.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthruleset_ProcessSession"></a> msdyn_solutionhealthruleset_ProcessSession

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthruleset_ProcessSession](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_ProcessSession) one-to-many relationship for the [msdyn_solutionhealthruleset](msdyn_solutionhealthruleset.md) table/entity.

### <a name="BKMK_powerbidataset_ProcessSession"></a> powerbidataset_ProcessSession

**Added by**: Power BI Entities Solution

See the [powerbidataset_ProcessSession](powerbidataset.md#BKMK_powerbidataset_ProcessSession) one-to-many relationship for the [powerbidataset](powerbidataset.md) table/entity.

### <a name="BKMK_powerbimashupparameter_ProcessSession"></a> powerbimashupparameter_ProcessSession

**Added by**: Power BI Entities Solution

See the [powerbimashupparameter_ProcessSession](powerbimashupparameter.md#BKMK_powerbimashupparameter_ProcessSession) one-to-many relationship for the [powerbimashupparameter](powerbimashupparameter.md) table/entity.

### <a name="BKMK_powerbireport_ProcessSession"></a> powerbireport_ProcessSession

**Added by**: Power BI Entities Solution

See the [powerbireport_ProcessSession](powerbireport.md#BKMK_powerbireport_ProcessSession) one-to-many relationship for the [powerbireport](powerbireport.md) table/entity.

### <a name="BKMK_msdyn_fileupload_ProcessSession"></a> msdyn_fileupload_ProcessSession

**Added by**: Smart Data Import Base Solution

See the [msdyn_fileupload_ProcessSession](msdyn_fileupload.md#BKMK_msdyn_fileupload_ProcessSession) one-to-many relationship for the [msdyn_fileupload](msdyn_fileupload.md) table/entity.

### <a name="BKMK_mspcat_catalogsubmissionfiles_ProcessSession"></a> mspcat_catalogsubmissionfiles_ProcessSession

**Added by**: Power Platform Catalog Client Packaging Solution

See the [mspcat_catalogsubmissionfiles_ProcessSession](mspcat_catalogsubmissionfiles.md#BKMK_mspcat_catalogsubmissionfiles_ProcessSession) one-to-many relationship for the [mspcat_catalogsubmissionfiles](mspcat_catalogsubmissionfiles.md) table/entity.

### <a name="BKMK_mspcat_packagestore_ProcessSession"></a> mspcat_packagestore_ProcessSession

**Added by**: Power Platform Catalog Client Packaging Solution

See the [mspcat_packagestore_ProcessSession](mspcat_packagestore.md#BKMK_mspcat_packagestore_ProcessSession) one-to-many relationship for the [mspcat_packagestore](mspcat_packagestore.md) table/entity.

### <a name="BKMK_msdyn_schedule_ProcessSession"></a> msdyn_schedule_ProcessSession

**Added by**: Insights App Platform Solution

See the [msdyn_schedule_ProcessSession](msdyn_schedule.md#BKMK_msdyn_schedule_ProcessSession) one-to-many relationship for the [msdyn_schedule](msdyn_schedule.md) table/entity.

### <a name="BKMK_msdyn_dataflow_datalakefolder_ProcessSession"></a> msdyn_dataflow_datalakefolder_ProcessSession

**Added by**: Insights App Platform Solution

See the [msdyn_dataflow_datalakefolder_ProcessSession](msdyn_dataflow_datalakefolder.md#BKMK_msdyn_dataflow_datalakefolder_ProcessSession) one-to-many relationship for the [msdyn_dataflow_datalakefolder](msdyn_dataflow_datalakefolder.md) table/entity.

### <a name="BKMK_msdyn_dmsrequest_ProcessSession"></a> msdyn_dmsrequest_ProcessSession

**Added by**: Insights App Platform Solution

See the [msdyn_dmsrequest_ProcessSession](msdyn_dmsrequest.md#BKMK_msdyn_dmsrequest_ProcessSession) one-to-many relationship for the [msdyn_dmsrequest](msdyn_dmsrequest.md) table/entity.

### <a name="BKMK_msdyn_dmsrequeststatus_ProcessSession"></a> msdyn_dmsrequeststatus_ProcessSession

**Added by**: Insights App Platform Solution

See the [msdyn_dmsrequeststatus_ProcessSession](msdyn_dmsrequeststatus.md#BKMK_msdyn_dmsrequeststatus_ProcessSession) one-to-many relationship for the [msdyn_dmsrequeststatus](msdyn_dmsrequeststatus.md) table/entity.

### <a name="BKMK_searchattributesettings_ProcessSession"></a> searchattributesettings_ProcessSession

**Added by**: msdyn_RelevanceSearch Solution

See the [searchattributesettings_ProcessSession](searchattributesettings.md#BKMK_searchattributesettings_ProcessSession) one-to-many relationship for the [searchattributesettings](searchattributesettings.md) table/entity.

### <a name="BKMK_searchcustomanalyzer_ProcessSession"></a> searchcustomanalyzer_ProcessSession

**Added by**: msdyn_RelevanceSearch Solution

See the [searchcustomanalyzer_ProcessSession](searchcustomanalyzer.md#BKMK_searchcustomanalyzer_ProcessSession) one-to-many relationship for the [searchcustomanalyzer](searchcustomanalyzer.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.processsession?text=processsession EntityType" />