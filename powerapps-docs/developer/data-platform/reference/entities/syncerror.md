---
title: "SyncError table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the SyncError table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# SyncError table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Failure reason and other detailed information for a record that failed to sync.


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /syncerrors(*syncerrorid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST /syncerrors<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE /syncerrors(*syncerrorid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET /syncerrors(*syncerrorid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /syncerrors<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|SetState|PATCH /syncerrors(*syncerrorid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /syncerrors(*syncerrorid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|SyncErrors|
|DisplayCollectionName|Sync Errors|
|DisplayName|Sync Error|
|EntitySetName|syncerrors|
|IsBPFEntity|False|
|LogicalCollectionName|syncerrors|
|LogicalName|syncerror|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|syncerrorid|
|PrimaryNameAttribute|name|
|SchemaName|SyncError|

<a name="writable-attributes"></a>

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
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [RequestData](#BKMK_RequestData)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [SyncErrorId](#BKMK_SyncErrorId)


### <a name="BKMK_Action"></a> Action

|Property|Value|
|--------|-----|
|Description|Action Name for which sync error has occurred|
|DisplayName|Action|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|action|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ActionData"></a> ActionData

|Property|Value|
|--------|-----|
|Description|Show the action data|
|DisplayName|Action Data|
|FormatName|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|actiondata|
|MaxLength|10000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Enter a short description of the sync error.|
|DisplayName|Description|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|4000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_ErrorCode"></a> ErrorCode

|Property|Value|
|--------|-----|
|Description|Displays the error code.|
|DisplayName|Error Code|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|errorcode|
|MaxLength|100|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_ErrorDetail"></a> ErrorDetail

|Property|Value|
|--------|-----|
|Description|Error description from the exception|
|DisplayName|Error Detail|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|errordetail|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_ErrorMessage"></a> ErrorMessage

|Property|Value|
|--------|-----|
|Description|Error Message of the exception|
|DisplayName|Error Message|
|FormatName|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|errormessage|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ErrorTime"></a> ErrorTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the upsync request was executed on CRM server|
|DisplayName|Error Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|errortime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_ErrorType"></a> ErrorType

|Property|Value|
|--------|-----|
|Description|Select the preferred error type.|
|DisplayName|Error Type|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|errortype|
|RequiredLevel|None|
|Type|Picklist|

#### ErrorType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Conflict||
|1|Record not found||
|2|Record already exists||
|3|Others||



### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Entity name of the record for which sync error has occurred|
|DisplayName|Entity|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|name|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user or team who owns the sync error.|
|DisplayName|Owner|
|IsValidForForm|True|
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


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|--------|-----|
|Description|Choose the record that the sync error relates to.|
|DisplayName|Record|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|regardingobjectid|
|RequiredLevel|None|
|Targets|account,activityfileattachment,activitymimeattachment,activityparty,annotation,appaction,appactionmigration,appactionrule,appelement,applicationuser,appmodulecomponentedge,appmodulecomponentnode,appointment,appsetting,appusersetting,archivecleanupinfo,archivecleanupoperation,attachment,attributeimageconfig,bot,botcomponent,bulkarchiveconfig,bulkarchivefailuredetail,bulkarchiveoperation,bulkarchiveoperationdetail,businessdatalocalizedlabel,businessunit,canvasappextendedmetadata,card,cascadegrantrevokeaccessrecordstracker,cascadegrantrevokeaccessversiontracker,catalog,catalogassignment,category,channelaccessprofile,channelaccessprofilerule,channelaccessprofileruleitem,chat,comment,connection,connectioninstance,connectionreference,connectionrole,connector,contact,conversationtranscript,customapi,customapirequestparameter,customapiresponseproperty,customeraddress,datalakefolder,datalakefolderpermission,datalakeworkspace,datalakeworkspacepermission,dataprocessingconfiguration,delegatedauthorization,desktopflowbinary,desktopflowmodule,duplicaterule,duplicaterulecondition,email,emailserverprofile,enablearchivalrequest,entityanalyticsconfig,entityimageconfig,entityindex,entityrecordfilter,environmentvariabledefinition,environmentvariablevalue,expiredprocess,exportedexcel,exportsolutionupload,externalparty,externalpartyitem,fax,featurecontrolsetting,feedback,fieldpermission,fieldsecurityprofile,fileattachment,flowmachine,flowmachinegroup,flowmachineimage,flowmachineimageversion,flowmachinenetwork,flowsession,fxexpression,goal,goalrollupquery,holidaywrapper,importmap,indexattributes,internaladdress,internalcatalogassignment,kbarticle,kbarticletemplate,keyvaultreference,knowledgearticle,knowledgearticleviews,knowledgebaserecord,letter,mailbox,mailmergetemplate,managedidentity,metadataforarchival,metric,mobileofflineprofileextension,msdynce_botcontent,msdyn_aibdataset,msdyn_aibdatasetfile,msdyn_aibdatasetrecord,msdyn_aibdatasetscontainer,msdyn_aibfeedbackloop,msdyn_aibfile,msdyn_aibfileattacheddata,msdyn_aiconfiguration,msdyn_aievent,msdyn_aifptrainingdocument,msdyn_aimodel,msdyn_aiodimage,msdyn_aiodlabel,msdyn_aiodtrainingboundingbox,msdyn_aiodtrainingimage,msdyn_aitemplate,msdyn_analysiscomponent,msdyn_analysisjob,msdyn_analysisoverride,msdyn_analysisresult,msdyn_analysisresultdetail,msdyn_appinsightsmetadata,msdyn_customcontrolextendedsettings,msdyn_dataflow,msdyn_dataflowrefreshhistory,msdyn_dataflowtemplate,msdyn_dataflow_datalakefolder,msdyn_dmsrequest,msdyn_dmsrequeststatus,msdyn_entitylinkchatconfiguration,msdyn_entityrefreshhistory,msdyn_favoriteknowledgearticle,msdyn_federatedarticle,msdyn_federatedarticleincident,msdyn_fileupload,msdyn_helppage,msdyn_insightsstorevirtualentity,msdyn_integratedsearchprovider,msdyn_kalanguagesetting,msdyn_kbattachment,msdyn_kmfederatedsearchconfig,msdyn_kmpersonalizationsetting,msdyn_knowledgearticleimage,msdyn_knowledgearticletemplate,msdyn_knowledgeconfiguration,msdyn_knowledgeinteractioninsight,msdyn_knowledgemanagementsetting,msdyn_knowledgepersonalfilter,msdyn_knowledgesearchfilter,msdyn_knowledgesearchinsight,msdyn_mobileapp,msdyn_pmanalysishistory,msdyn_pmcalendar,msdyn_pmcalendarversion,msdyn_pminferredtask,msdyn_pmprocessextendedmetadataversion,msdyn_pmprocesstemplate,msdyn_pmprocessusersettings,msdyn_pmprocessversion,msdyn_pmrecording,msdyn_pmtemplate,msdyn_pmview,msdyn_richtextfile,msdyn_schedule,msdyn_serviceconfiguration,msdyn_slakpi,msdyn_solutionhealthrule,msdyn_solutionhealthruleargument,msdyn_solutionhealthruleset,msdyn_tour,msdyn_virtualtablecolumncandidate,msdyn_workflowactionstatus,msgraphresourcetosubscription,mspcat_catalogsubmissionfiles,mspcat_packagestore,newprocess,offlinecommanddefinition,organization,organizationdatasyncfnostate,organizationdatasyncstate,organizationdatasyncsubscription,organizationdatasyncsubscriptionentity,organizationdatasyncsubscriptionfnotable,organizationsetting,package,pdfsetting,phonecall,pluginpackage,position,postfollow,powerbidataset,powerbimashupparameter,powerbireport,powerfxrule,privilegesremovalsetting,processsession,processstage,processstageparameter,processtrigger,provisionlanguageforuser,publisher,queue,queueitem,reconciliationentityinfo,reconciliationinfo,recordfilter,recurringappointmentmaster,relationshipattribute,report,reportcategory,retaineddataexcel,retentioncleanupinfo,retentioncleanupoperation,retentionconfig,retentionfailuredetail,retentionoperation,retentionoperationdetail,revokeinheritedaccessrecordstracker,role,roleeditorlayout,rollupfield,savedquery,savedqueryvisualization,searchattributesettings,searchcustomanalyzer,searchrelationshipsettings,serviceplan,serviceplanmapping,settingdefinition,sharedlinksetting,sharedobject,sharedworkspace,sharedworkspacepool,sharepointdocumentlocation,sharepointsite,sla,slaitem,slakpiinstance,socialactivity,socialprofile,solution,solutioncomponentattributeconfiguration,solutioncomponentbatchconfiguration,solutioncomponentconfiguration,solutioncomponentrelationshipconfiguration,stagedentity,stagedentityattribute,stagesolutionupload,subject,supportusertable,synapsedatabase,synapselinkexternaltablestate,synapselinkprofile,synapselinkprofileentity,synapselinkprofileentitystate,synapselinkschedule,syncerror,systemuser,systemuserauthorizationchangetracker,task,tdsmetadata,team,teammobileofflineprofilemembership,teamtemplate,template,territory,transactioncurrency,translationprocess,usermobileofflineprofilemembership,userquery,userqueryvisualization,userrating,virtualentitymetadata,workflow,workflowbinary,workqueue,workqueueitem|
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
|MaxLength|4000|
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


### <a name="BKMK_RequestData"></a> RequestData

|Property|Value|
|--------|-----|
|Description|Request data for the entity that had the sync error.|
|DisplayName|Request Data|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|requestdata|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|--------|-----|
|Description|Shows whether the sync error is active or resolved.|
|DisplayName|State|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### StateCode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|0|Active|
|1|Resolved|1|Resolved|



### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|--------|-----|
|Description|Select the sync error status.|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### StatusCode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|0|Active|0|
|1|Fixed|1|



### <a name="BKMK_SyncErrorId"></a> SyncErrorId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the sync error.|
|DisplayName|Sync Error Id|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|syncerrorid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [RegardingObjectIdYomiName](#BKMK_RegardingObjectIdYomiName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the sync error.|
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
|Description|Date and time when the sync Error was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the sync error.|
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


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the sync error.|
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
|Description|Date and time when the sync error was last modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who last modified the sync error.|
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
|Description|Business unit that owns the sync error.|
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
|Description|Unique identifier of the team who owns the sync error.|
|DisplayName|Owning Team|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|owningteam|
|RequiredLevel|None|
|Targets|team|
|Type|Lookup|


### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who owns the sync error.|
|DisplayName|Owning User|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_RegardingObjectIdYomiName"></a> RegardingObjectIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjectidyominame|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|Shows the version number of the sync error.|
|DisplayName|Version Number|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_SyncError_SyncErrors"></a> SyncError_SyncErrors

Same as the [SyncError_SyncErrors](syncerror.md#BKMK_SyncError_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|SyncError_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [KnowledgeBaseRecord_SyncErrors](#BKMK_KnowledgeBaseRecord_SyncErrors)
- [SocialProfile_SyncErrors](#BKMK_SocialProfile_SyncErrors)
- [QueueItem_SyncErrors](#BKMK_QueueItem_SyncErrors)
- [PostFollow_SyncErrors](#BKMK_PostFollow_SyncErrors)
- [SharePointSite_SyncErrors](#BKMK_SharePointSite_SyncErrors)
- [Goal_SyncErrors](#BKMK_Goal_SyncErrors)
- [lk_syncerrorbase_createdby](#BKMK_lk_syncerrorbase_createdby)
- [TranslationProcess_SyncErrors](#BKMK_TranslationProcess_SyncErrors)
- [PhoneCall_SyncErrors](#BKMK_PhoneCall_SyncErrors)
- [RecurringAppointmentMaster_SyncErrors](#BKMK_RecurringAppointmentMaster_SyncErrors)
- [Publisher_SyncErrors](#BKMK_Publisher_SyncErrors)
- [DuplicateRule_SyncErrors](#BKMK_DuplicateRule_SyncErrors)
- [Subject_SyncErrors](#BKMK_Subject_SyncErrors)
- [UserQuery_SyncErrors](#BKMK_UserQuery_SyncErrors)
- [MailMergeTemplate_SyncErrors](#BKMK_MailMergeTemplate_SyncErrors)
- [SyncError_SyncErrors](#BKMK_SyncError_SyncErrors)
- [SavedQuery_SyncErrors](#BKMK_SavedQuery_SyncErrors)
- [lk_syncerrorbase_modifiedby](#BKMK_lk_syncerrorbase_modifiedby)
- [lk_syncerrorbase_modifiedonbehalfby](#BKMK_lk_syncerrorbase_modifiedonbehalfby)
- [TransactionCurrency_SyncErrors](#BKMK_TransactionCurrency_SyncErrors)
- [SocialActivity_SyncErrors](#BKMK_SocialActivity_SyncErrors)
- [CustomerAddress_SyncErrors](#BKMK_CustomerAddress_SyncErrors)
- [Solution_SyncErrors](#BKMK_Solution_SyncErrors)
- [team_SyncError](#BKMK_team_SyncError)
- [TeamTemplate_SyncErrors](#BKMK_TeamTemplate_SyncErrors)
- [ReportCategory_SyncErrors](#BKMK_ReportCategory_SyncErrors)
- [lk_syncerrorbase_createdonbehalfby](#BKMK_lk_syncerrorbase_createdonbehalfby)
- [KbArticle_SyncErrors](#BKMK_KbArticle_SyncErrors)
- [RollupField_SyncErrors](#BKMK_RollupField_SyncErrors)
- [KbArticleTemplate_SyncErrors](#BKMK_KbArticleTemplate_SyncErrors)
- [Account_SyncErrors](#BKMK_Account_SyncErrors)
- [FieldSecurityProfile_SyncErrors](#BKMK_FieldSecurityProfile_SyncErrors)
- [UserQueryVisualization_SyncErrors](#BKMK_UserQueryVisualization_SyncErrors)
- [FieldPermission_SyncErrors](#BKMK_FieldPermission_SyncErrors)
- [DuplicateRuleCondition_SyncErrors](#BKMK_DuplicateRuleCondition_SyncErrors)
- [Team_SyncErrors](#BKMK_Team_SyncErrors)
- [SLAItem_SyncErrors](#BKMK_SLAItem_SyncErrors)
- [KnowledgeArticleViews_SyncErrors](#BKMK_KnowledgeArticleViews_SyncErrors)
- [Appointment_SyncErrors](#BKMK_Appointment_SyncErrors)
- [SystemUser_SyncError](#BKMK_SystemUser_SyncError)
- [Contact_SyncErrors](#BKMK_Contact_SyncErrors)
- [ExpiredProcess_SyncErrors](#BKMK_ExpiredProcess_SyncErrors)
- [Workflow_SyncErrors](#BKMK_Workflow_SyncErrors)
- [NewProcess_SyncErrors](#BKMK_NewProcess_SyncErrors)
- [Feedback_SyncErrors](#BKMK_Feedback_SyncErrors)
- [ActivityParty_SyncErrors](#BKMK_ActivityParty_SyncErrors)
- [Annotation_SyncErrors](#BKMK_Annotation_SyncErrors)
- [Email_SyncErrors](#BKMK_Email_SyncErrors)
- [Organization_SyncErrors](#BKMK_Organization_SyncErrors)
- [ActivityMimeAttachment_SyncErrors](#BKMK_ActivityMimeAttachment_SyncErrors)
- [Task_SyncErrors](#BKMK_Task_SyncErrors)
- [Letter_SyncErrors](#BKMK_Letter_SyncErrors)
- [Template_SyncErrors](#BKMK_Template_SyncErrors)
- [ProcessStage_SyncErrors](#BKMK_ProcessStage_SyncErrors)
- [KnowledgeArticle_SyncErrors](#BKMK_KnowledgeArticle_SyncErrors)
- [Position_SyncErrors](#BKMK_Position_SyncErrors)
- [SharePointDocumentLocation_SyncErrors](#BKMK_SharePointDocumentLocation_SyncErrors)
- [Report_SyncErrors](#BKMK_Report_SyncErrors)
- [Connection_SyncErrors](#BKMK_Connection_SyncErrors)
- [ProcessSession_SyncErrors](#BKMK_ProcessSession_SyncErrors)
- [Category_SyncErrors](#BKMK_Category_SyncErrors)
- [ConnectionRole_SyncErrors](#BKMK_ConnectionRole_SyncErrors)
- [ProcessTrigger_SyncErrors](#BKMK_ProcessTrigger_SyncErrors)
- [Fax_SyncErrors](#BKMK_Fax_SyncErrors)
- [Mailbox_SyncErrors](#BKMK_Mailbox_SyncErrors)
- [BusinessUnit_SyncErrors](#BKMK_BusinessUnit_SyncErrors)
- [Queue_SyncErrors](#BKMK_Queue_SyncErrors)
- [Role_SyncErrors](#BKMK_Role_SyncErrors)
- [BusinessUnit_SyncError](#BKMK_BusinessUnit_SyncError)
- [SystemUser_SyncErrors](#BKMK_SystemUser_SyncErrors)
- [SLAKPIInstance_SyncErrors](#BKMK_SLAKPIInstance_SyncErrors)
- [SLA_SyncErrors](#BKMK_SLA_SyncErrors)
- [SavedQueryVisualization_SyncErrors](#BKMK_SavedQueryVisualization_SyncErrors)
- [GoalRollupQuery_SyncErrors](#BKMK_GoalRollupQuery_SyncErrors)
- [Metric_SyncErrors](#BKMK_Metric_SyncErrors)
- [ImportMap_SyncErrors](#BKMK_ImportMap_SyncErrors)
- [EmailServerProfile_SyncErrors](#BKMK_EmailServerProfile_SyncErrors)
- [solutioncomponentattributeconfiguration_SyncErrors](#BKMK_solutioncomponentattributeconfiguration_SyncErrors)
- [solutioncomponentbatchconfiguration_SyncErrors](#BKMK_solutioncomponentbatchconfiguration_SyncErrors)
- [solutioncomponentconfiguration_SyncErrors](#BKMK_solutioncomponentconfiguration_SyncErrors)
- [solutioncomponentrelationshipconfiguration_SyncErrors](#BKMK_solutioncomponentrelationshipconfiguration_SyncErrors)
- [package_SyncErrors](#BKMK_package_SyncErrors)
- [stagesolutionupload_SyncErrors](#BKMK_stagesolutionupload_SyncErrors)
- [exportsolutionupload_SyncErrors](#BKMK_exportsolutionupload_SyncErrors)
- [featurecontrolsetting_SyncErrors](#BKMK_featurecontrolsetting_SyncErrors)
- [attributeimageconfig_SyncErrors](#BKMK_attributeimageconfig_SyncErrors)
- [entityimageconfig_SyncErrors](#BKMK_entityimageconfig_SyncErrors)
- [relationshipattribute_SyncErrors](#BKMK_relationshipattribute_SyncErrors)
- [stagedentity_SyncErrors](#BKMK_stagedentity_SyncErrors)
- [stagedentityattribute_SyncErrors](#BKMK_stagedentityattribute_SyncErrors)
- [catalog_SyncErrors](#BKMK_catalog_SyncErrors)
- [catalogassignment_SyncErrors](#BKMK_catalogassignment_SyncErrors)
- [customapi_SyncErrors](#BKMK_customapi_SyncErrors)
- [customapirequestparameter_SyncErrors](#BKMK_customapirequestparameter_SyncErrors)
- [customapiresponseproperty_SyncErrors](#BKMK_customapiresponseproperty_SyncErrors)
- [provisionlanguageforuser_SyncErrors](#BKMK_provisionlanguageforuser_SyncErrors)
- [sharedobject_SyncErrors](#BKMK_sharedobject_SyncErrors)
- [sharedworkspace_SyncErrors](#BKMK_sharedworkspace_SyncErrors)
- [sharedworkspacepool_SyncErrors](#BKMK_sharedworkspacepool_SyncErrors)
- [entityanalyticsconfig_SyncErrors](#BKMK_entityanalyticsconfig_SyncErrors)
- [datalakefolder_SyncErrors](#BKMK_datalakefolder_SyncErrors)
- [datalakefolderpermission_SyncErrors](#BKMK_datalakefolderpermission_SyncErrors)
- [datalakeworkspace_SyncErrors](#BKMK_datalakeworkspace_SyncErrors)
- [datalakeworkspacepermission_SyncErrors](#BKMK_datalakeworkspacepermission_SyncErrors)
- [dataprocessingconfiguration_SyncErrors](#BKMK_dataprocessingconfiguration_SyncErrors)
- [exportedexcel_SyncErrors](#BKMK_exportedexcel_SyncErrors)
- [retaineddataexcel_SyncErrors](#BKMK_retaineddataexcel_SyncErrors)
- [synapsedatabase_SyncErrors](#BKMK_synapsedatabase_SyncErrors)
- [synapselinkexternaltablestate_SyncErrors](#BKMK_synapselinkexternaltablestate_SyncErrors)
- [synapselinkprofile_SyncErrors](#BKMK_synapselinkprofile_SyncErrors)
- [synapselinkprofileentity_SyncErrors](#BKMK_synapselinkprofileentity_SyncErrors)
- [synapselinkprofileentitystate_SyncErrors](#BKMK_synapselinkprofileentitystate_SyncErrors)
- [synapselinkschedule_SyncErrors](#BKMK_synapselinkschedule_SyncErrors)
- [msdyn_dataflow_SyncErrors](#BKMK_msdyn_dataflow_SyncErrors)
- [msdyn_dataflowrefreshhistory_SyncErrors](#BKMK_msdyn_dataflowrefreshhistory_SyncErrors)
- [msdyn_entityrefreshhistory_SyncErrors](#BKMK_msdyn_entityrefreshhistory_SyncErrors)
- [sharedlinksetting_SyncErrors](#BKMK_sharedlinksetting_SyncErrors)
- [entityrecordfilter_SyncErrors](#BKMK_entityrecordfilter_SyncErrors)
- [recordfilter_SyncErrors](#BKMK_recordfilter_SyncErrors)
- [delegatedauthorization_SyncErrors](#BKMK_delegatedauthorization_SyncErrors)
- [serviceplan_SyncErrors](#BKMK_serviceplan_SyncErrors)
- [serviceplanmapping_SyncErrors](#BKMK_serviceplanmapping_SyncErrors)
- [applicationuser_SyncErrors](#BKMK_applicationuser_SyncErrors)
- [connector_SyncErrors](#BKMK_connector_SyncErrors)
- [environmentvariabledefinition_SyncErrors](#BKMK_environmentvariabledefinition_SyncErrors)
- [environmentvariablevalue_SyncErrors](#BKMK_environmentvariablevalue_SyncErrors)
- [workflowbinary_SyncErrors](#BKMK_workflowbinary_SyncErrors)
- [desktopflowmodule_SyncErrors](#BKMK_desktopflowmodule_SyncErrors)
- [flowmachine_SyncErrors](#BKMK_flowmachine_SyncErrors)
- [flowmachinegroup_SyncErrors](#BKMK_flowmachinegroup_SyncErrors)
- [flowmachineimage_SyncErrors](#BKMK_flowmachineimage_SyncErrors)
- [flowmachineimageversion_SyncErrors](#BKMK_flowmachineimageversion_SyncErrors)
- [flowmachinenetwork_SyncErrors](#BKMK_flowmachinenetwork_SyncErrors)
- [processstageparameter_SyncErrors](#BKMK_processstageparameter_SyncErrors)
- [workqueue_SyncErrors](#BKMK_workqueue_SyncErrors)
- [workqueueitem_SyncErrors](#BKMK_workqueueitem_SyncErrors)
- [desktopflowbinary_SyncErrors](#BKMK_desktopflowbinary_SyncErrors)
- [flowsession_SyncErrors](#BKMK_flowsession_SyncErrors)
- [connectionreference_SyncErrors](#BKMK_connectionreference_SyncErrors)
- [connectioninstance_SyncErrors](#BKMK_connectioninstance_SyncErrors)
- [msdyn_helppage_SyncErrors](#BKMK_msdyn_helppage_SyncErrors)
- [msdyn_tour_SyncErrors](#BKMK_msdyn_tour_SyncErrors)
- [msdynce_botcontent_SyncErrors](#BKMK_msdynce_botcontent_SyncErrors)
- [conversationtranscript_SyncErrors](#BKMK_conversationtranscript_SyncErrors)
- [bot_SyncErrors](#BKMK_bot_SyncErrors)
- [botcomponent_SyncErrors](#BKMK_botcomponent_SyncErrors)
- [Territory_SyncErrors](#BKMK_Territory_SyncErrors)
- [activityfileattachment_SyncErrors](#BKMK_activityfileattachment_SyncErrors)
- [chat_SyncErrors](#BKMK_chat_SyncErrors)
- [msdyn_serviceconfiguration_SyncErrors](#BKMK_msdyn_serviceconfiguration_SyncErrors)
- [msdyn_slakpi_SyncErrors](#BKMK_msdyn_slakpi_SyncErrors)
- [msdyn_knowledgemanagementsetting_SyncErrors](#BKMK_msdyn_knowledgemanagementsetting_SyncErrors)
- [msdyn_federatedarticle_SyncErrors](#BKMK_msdyn_federatedarticle_SyncErrors)
- [msdyn_federatedarticleincident_SyncErrors](#BKMK_msdyn_federatedarticleincident_SyncErrors)
- [msdyn_integratedsearchprovider_SyncErrors](#BKMK_msdyn_integratedsearchprovider_SyncErrors)
- [msdyn_kmfederatedsearchconfig_SyncErrors](#BKMK_msdyn_kmfederatedsearchconfig_SyncErrors)
- [msdyn_knowledgearticleimage_SyncErrors](#BKMK_msdyn_knowledgearticleimage_SyncErrors)
- [msdyn_knowledgeconfiguration_SyncErrors](#BKMK_msdyn_knowledgeconfiguration_SyncErrors)
- [msdyn_knowledgeinteractioninsight_SyncErrors](#BKMK_msdyn_knowledgeinteractioninsight_SyncErrors)
- [msdyn_knowledgesearchinsight_SyncErrors](#BKMK_msdyn_knowledgesearchinsight_SyncErrors)
- [msdyn_favoriteknowledgearticle_SyncErrors](#BKMK_msdyn_favoriteknowledgearticle_SyncErrors)
- [msdyn_kalanguagesetting_SyncErrors](#BKMK_msdyn_kalanguagesetting_SyncErrors)
- [msdyn_kbattachment_SyncErrors](#BKMK_msdyn_kbattachment_SyncErrors)
- [msdyn_kmpersonalizationsetting_SyncErrors](#BKMK_msdyn_kmpersonalizationsetting_SyncErrors)
- [msdyn_knowledgearticletemplate_SyncErrors](#BKMK_msdyn_knowledgearticletemplate_SyncErrors)
- [msdyn_knowledgepersonalfilter_SyncErrors](#BKMK_msdyn_knowledgepersonalfilter_SyncErrors)
- [msdyn_knowledgesearchfilter_SyncErrors](#BKMK_msdyn_knowledgesearchfilter_SyncErrors)
- [pluginpackage_SyncErrors](#BKMK_pluginpackage_SyncErrors)
- [fxexpression_SyncErrors](#BKMK_fxexpression_SyncErrors)
- [powerfxrule_SyncErrors](#BKMK_powerfxrule_SyncErrors)
- [keyvaultreference_SyncErrors](#BKMK_keyvaultreference_SyncErrors)
- [managedidentity_SyncErrors](#BKMK_managedidentity_SyncErrors)
- [msgraphresourcetosubscription_SyncErrors](#BKMK_msgraphresourcetosubscription_SyncErrors)
- [virtualentitymetadata_SyncErrors](#BKMK_virtualentitymetadata_SyncErrors)
- [mobileofflineprofileextension_SyncErrors](#BKMK_mobileofflineprofileextension_SyncErrors)
- [teammobileofflineprofilemembership_SyncErrors](#BKMK_teammobileofflineprofilemembership_SyncErrors)
- [usermobileofflineprofilemembership_SyncErrors](#BKMK_usermobileofflineprofilemembership_SyncErrors)
- [organizationdatasyncsubscription_SyncErrors](#BKMK_organizationdatasyncsubscription_SyncErrors)
- [organizationdatasyncsubscriptionentity_SyncErrors](#BKMK_organizationdatasyncsubscriptionentity_SyncErrors)
- [organizationdatasyncsubscriptionfnotable_SyncErrors](#BKMK_organizationdatasyncsubscriptionfnotable_SyncErrors)
- [organizationdatasyncfnostate_SyncErrors](#BKMK_organizationdatasyncfnostate_SyncErrors)
- [organizationdatasyncstate_SyncErrors](#BKMK_organizationdatasyncstate_SyncErrors)
- [metadataforarchival_SyncErrors](#BKMK_metadataforarchival_SyncErrors)
- [retentionconfig_SyncErrors](#BKMK_retentionconfig_SyncErrors)
- [retentionfailuredetail_SyncErrors](#BKMK_retentionfailuredetail_SyncErrors)
- [retentionoperation_SyncErrors](#BKMK_retentionoperation_SyncErrors)
- [retentionoperationdetail_SyncErrors](#BKMK_retentionoperationdetail_SyncErrors)
- [msdyn_appinsightsmetadata_SyncErrors](#BKMK_msdyn_appinsightsmetadata_SyncErrors)
- [msdyn_dataflowtemplate_SyncErrors](#BKMK_msdyn_dataflowtemplate_SyncErrors)
- [msdyn_workflowactionstatus_SyncErrors](#BKMK_msdyn_workflowactionstatus_SyncErrors)
- [userrating_SyncErrors](#BKMK_userrating_SyncErrors)
- [msdyn_mobileapp_SyncErrors](#BKMK_msdyn_mobileapp_SyncErrors)
- [msdyn_insightsstorevirtualentity_SyncErrors](#BKMK_msdyn_insightsstorevirtualentity_SyncErrors)
- [roleeditorlayout_SyncErrors](#BKMK_roleeditorlayout_SyncErrors)
- [appaction_SyncErrors](#BKMK_appaction_SyncErrors)
- [appactionmigration_SyncErrors](#BKMK_appactionmigration_SyncErrors)
- [appactionrule_SyncErrors](#BKMK_appactionrule_SyncErrors)
- [card_SyncErrors](#BKMK_card_SyncErrors)
- [msdyn_entitylinkchatconfiguration_SyncErrors](#BKMK_msdyn_entitylinkchatconfiguration_SyncErrors)
- [msdyn_richtextfile_SyncErrors](#BKMK_msdyn_richtextfile_SyncErrors)
- [msdyn_customcontrolextendedsettings_SyncErrors](#BKMK_msdyn_customcontrolextendedsettings_SyncErrors)
- [searchrelationshipsettings_SyncErrors](#BKMK_searchrelationshipsettings_SyncErrors)
- [msdyn_virtualtablecolumncandidate_SyncErrors](#BKMK_msdyn_virtualtablecolumncandidate_SyncErrors)
- [msdyn_aiconfiguration_SyncErrors](#BKMK_msdyn_aiconfiguration_SyncErrors)
- [msdyn_aievent_SyncErrors](#BKMK_msdyn_aievent_SyncErrors)
- [msdyn_aimodel_SyncErrors](#BKMK_msdyn_aimodel_SyncErrors)
- [msdyn_aitemplate_SyncErrors](#BKMK_msdyn_aitemplate_SyncErrors)
- [msdyn_aibfeedbackloop_SyncErrors](#BKMK_msdyn_aibfeedbackloop_SyncErrors)
- [msdyn_aifptrainingdocument_SyncErrors](#BKMK_msdyn_aifptrainingdocument_SyncErrors)
- [msdyn_aiodimage_SyncErrors](#BKMK_msdyn_aiodimage_SyncErrors)
- [msdyn_aiodlabel_SyncErrors](#BKMK_msdyn_aiodlabel_SyncErrors)
- [msdyn_aiodtrainingboundingbox_SyncErrors](#BKMK_msdyn_aiodtrainingboundingbox_SyncErrors)
- [msdyn_aiodtrainingimage_SyncErrors](#BKMK_msdyn_aiodtrainingimage_SyncErrors)
- [msdyn_aibdataset_SyncErrors](#BKMK_msdyn_aibdataset_SyncErrors)
- [msdyn_aibdatasetfile_SyncErrors](#BKMK_msdyn_aibdatasetfile_SyncErrors)
- [msdyn_aibdatasetrecord_SyncErrors](#BKMK_msdyn_aibdatasetrecord_SyncErrors)
- [msdyn_aibdatasetscontainer_SyncErrors](#BKMK_msdyn_aibdatasetscontainer_SyncErrors)
- [msdyn_aibfile_SyncErrors](#BKMK_msdyn_aibfile_SyncErrors)
- [msdyn_aibfileattacheddata_SyncErrors](#BKMK_msdyn_aibfileattacheddata_SyncErrors)
- [msdyn_pmanalysishistory_SyncErrors](#BKMK_msdyn_pmanalysishistory_SyncErrors)
- [msdyn_pmcalendar_SyncErrors](#BKMK_msdyn_pmcalendar_SyncErrors)
- [msdyn_pmcalendarversion_SyncErrors](#BKMK_msdyn_pmcalendarversion_SyncErrors)
- [msdyn_pminferredtask_SyncErrors](#BKMK_msdyn_pminferredtask_SyncErrors)
- [msdyn_pmprocessextendedmetadataversion_SyncErrors](#BKMK_msdyn_pmprocessextendedmetadataversion_SyncErrors)
- [msdyn_pmprocesstemplate_SyncErrors](#BKMK_msdyn_pmprocesstemplate_SyncErrors)
- [msdyn_pmprocessusersettings_SyncErrors](#BKMK_msdyn_pmprocessusersettings_SyncErrors)
- [msdyn_pmprocessversion_SyncErrors](#BKMK_msdyn_pmprocessversion_SyncErrors)
- [msdyn_pmrecording_SyncErrors](#BKMK_msdyn_pmrecording_SyncErrors)
- [msdyn_pmtemplate_SyncErrors](#BKMK_msdyn_pmtemplate_SyncErrors)
- [msdyn_pmview_SyncErrors](#BKMK_msdyn_pmview_SyncErrors)
- [msdyn_analysiscomponent_SyncErrors](#BKMK_msdyn_analysiscomponent_SyncErrors)
- [msdyn_analysisjob_SyncErrors](#BKMK_msdyn_analysisjob_SyncErrors)
- [msdyn_analysisoverride_SyncErrors](#BKMK_msdyn_analysisoverride_SyncErrors)
- [msdyn_analysisresult_SyncErrors](#BKMK_msdyn_analysisresult_SyncErrors)
- [msdyn_analysisresultdetail_SyncErrors](#BKMK_msdyn_analysisresultdetail_SyncErrors)
- [msdyn_solutionhealthrule_SyncErrors](#BKMK_msdyn_solutionhealthrule_SyncErrors)
- [msdyn_solutionhealthruleargument_SyncErrors](#BKMK_msdyn_solutionhealthruleargument_SyncErrors)
- [msdyn_solutionhealthruleset_SyncErrors](#BKMK_msdyn_solutionhealthruleset_SyncErrors)
- [powerbidataset_SyncErrors](#BKMK_powerbidataset_SyncErrors)
- [powerbimashupparameter_SyncErrors](#BKMK_powerbimashupparameter_SyncErrors)
- [powerbireport_SyncErrors](#BKMK_powerbireport_SyncErrors)
- [msdyn_fileupload_SyncErrors](#BKMK_msdyn_fileupload_SyncErrors)
- [mspcat_catalogsubmissionfiles_SyncErrors](#BKMK_mspcat_catalogsubmissionfiles_SyncErrors)
- [mspcat_packagestore_SyncErrors](#BKMK_mspcat_packagestore_SyncErrors)
- [msdyn_schedule_SyncErrors](#BKMK_msdyn_schedule_SyncErrors)
- [msdyn_dataflow_datalakefolder_SyncErrors](#BKMK_msdyn_dataflow_datalakefolder_SyncErrors)
- [msdyn_dmsrequest_SyncErrors](#BKMK_msdyn_dmsrequest_SyncErrors)
- [msdyn_dmsrequeststatus_SyncErrors](#BKMK_msdyn_dmsrequeststatus_SyncErrors)
- [searchattributesettings_SyncErrors](#BKMK_searchattributesettings_SyncErrors)
- [searchcustomanalyzer_SyncErrors](#BKMK_searchcustomanalyzer_SyncErrors)


### <a name="BKMK_KnowledgeBaseRecord_SyncErrors"></a> KnowledgeBaseRecord_SyncErrors

See the [KnowledgeBaseRecord_SyncErrors](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_SyncErrors) one-to-many relationship for the [knowledgebaserecord](knowledgebaserecord.md) table/entity.

### <a name="BKMK_SocialProfile_SyncErrors"></a> SocialProfile_SyncErrors

See the [SocialProfile_SyncErrors](socialprofile.md#BKMK_SocialProfile_SyncErrors) one-to-many relationship for the [socialprofile](socialprofile.md) table/entity.

### <a name="BKMK_QueueItem_SyncErrors"></a> QueueItem_SyncErrors

See the [QueueItem_SyncErrors](queueitem.md#BKMK_QueueItem_SyncErrors) one-to-many relationship for the [queueitem](queueitem.md) table/entity.

### <a name="BKMK_PostFollow_SyncErrors"></a> PostFollow_SyncErrors

See the [PostFollow_SyncErrors](postfollow.md#BKMK_PostFollow_SyncErrors) one-to-many relationship for the [postfollow](postfollow.md) table/entity.

### <a name="BKMK_SharePointSite_SyncErrors"></a> SharePointSite_SyncErrors

See the [SharePointSite_SyncErrors](sharepointsite.md#BKMK_SharePointSite_SyncErrors) one-to-many relationship for the [sharepointsite](sharepointsite.md) table/entity.

### <a name="BKMK_Goal_SyncErrors"></a> Goal_SyncErrors

See the [Goal_SyncErrors](goal.md#BKMK_Goal_SyncErrors) one-to-many relationship for the [goal](goal.md) table/entity.

### <a name="BKMK_lk_syncerrorbase_createdby"></a> lk_syncerrorbase_createdby

See the [lk_syncerrorbase_createdby](systemuser.md#BKMK_lk_syncerrorbase_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_TranslationProcess_SyncErrors"></a> TranslationProcess_SyncErrors

See the [TranslationProcess_SyncErrors](translationprocess.md#BKMK_TranslationProcess_SyncErrors) one-to-many relationship for the [translationprocess](translationprocess.md) table/entity.

### <a name="BKMK_PhoneCall_SyncErrors"></a> PhoneCall_SyncErrors

See the [PhoneCall_SyncErrors](phonecall.md#BKMK_PhoneCall_SyncErrors) one-to-many relationship for the [phonecall](phonecall.md) table/entity.

### <a name="BKMK_RecurringAppointmentMaster_SyncErrors"></a> RecurringAppointmentMaster_SyncErrors

See the [RecurringAppointmentMaster_SyncErrors](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_SyncErrors) one-to-many relationship for the [recurringappointmentmaster](recurringappointmentmaster.md) table/entity.

### <a name="BKMK_Publisher_SyncErrors"></a> Publisher_SyncErrors

See the [Publisher_SyncErrors](publisher.md#BKMK_Publisher_SyncErrors) one-to-many relationship for the [publisher](publisher.md) table/entity.

### <a name="BKMK_DuplicateRule_SyncErrors"></a> DuplicateRule_SyncErrors

See the [DuplicateRule_SyncErrors](duplicaterule.md#BKMK_DuplicateRule_SyncErrors) one-to-many relationship for the [duplicaterule](duplicaterule.md) table/entity.

### <a name="BKMK_Subject_SyncErrors"></a> Subject_SyncErrors

See the [Subject_SyncErrors](subject.md#BKMK_Subject_SyncErrors) one-to-many relationship for the [subject](subject.md) table/entity.

### <a name="BKMK_UserQuery_SyncErrors"></a> UserQuery_SyncErrors

See the [UserQuery_SyncErrors](userquery.md#BKMK_UserQuery_SyncErrors) one-to-many relationship for the [userquery](userquery.md) table/entity.

### <a name="BKMK_MailMergeTemplate_SyncErrors"></a> MailMergeTemplate_SyncErrors

See the [MailMergeTemplate_SyncErrors](mailmergetemplate.md#BKMK_MailMergeTemplate_SyncErrors) one-to-many relationship for the [mailmergetemplate](mailmergetemplate.md) table/entity.

### <a name="BKMK_SyncError_SyncErrors"></a> SyncError_SyncErrors

See the [SyncError_SyncErrors](syncerror.md#BKMK_SyncError_SyncErrors) one-to-many relationship for the [syncerror](syncerror.md) table/entity.

### <a name="BKMK_SavedQuery_SyncErrors"></a> SavedQuery_SyncErrors

See the [SavedQuery_SyncErrors](savedquery.md#BKMK_SavedQuery_SyncErrors) one-to-many relationship for the [savedquery](savedquery.md) table/entity.

### <a name="BKMK_lk_syncerrorbase_modifiedby"></a> lk_syncerrorbase_modifiedby

See the [lk_syncerrorbase_modifiedby](systemuser.md#BKMK_lk_syncerrorbase_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_syncerrorbase_modifiedonbehalfby"></a> lk_syncerrorbase_modifiedonbehalfby

See the [lk_syncerrorbase_modifiedonbehalfby](systemuser.md#BKMK_lk_syncerrorbase_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_TransactionCurrency_SyncErrors"></a> TransactionCurrency_SyncErrors

See the [TransactionCurrency_SyncErrors](transactioncurrency.md#BKMK_TransactionCurrency_SyncErrors) one-to-many relationship for the [transactioncurrency](transactioncurrency.md) table/entity.

### <a name="BKMK_SocialActivity_SyncErrors"></a> SocialActivity_SyncErrors

See the [SocialActivity_SyncErrors](socialactivity.md#BKMK_SocialActivity_SyncErrors) one-to-many relationship for the [socialactivity](socialactivity.md) table/entity.

### <a name="BKMK_CustomerAddress_SyncErrors"></a> CustomerAddress_SyncErrors

See the [CustomerAddress_SyncErrors](customeraddress.md#BKMK_CustomerAddress_SyncErrors) one-to-many relationship for the [customeraddress](customeraddress.md) table/entity.

### <a name="BKMK_Solution_SyncErrors"></a> Solution_SyncErrors

See the [Solution_SyncErrors](solution.md#BKMK_Solution_SyncErrors) one-to-many relationship for the [solution](solution.md) table/entity.

### <a name="BKMK_team_SyncError"></a> team_SyncError

See the [team_SyncError](team.md#BKMK_team_SyncError) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_TeamTemplate_SyncErrors"></a> TeamTemplate_SyncErrors

See the [TeamTemplate_SyncErrors](teamtemplate.md#BKMK_TeamTemplate_SyncErrors) one-to-many relationship for the [teamtemplate](teamtemplate.md) table/entity.

### <a name="BKMK_ReportCategory_SyncErrors"></a> ReportCategory_SyncErrors

See the [ReportCategory_SyncErrors](reportcategory.md#BKMK_ReportCategory_SyncErrors) one-to-many relationship for the [reportcategory](reportcategory.md) table/entity.

### <a name="BKMK_lk_syncerrorbase_createdonbehalfby"></a> lk_syncerrorbase_createdonbehalfby

See the [lk_syncerrorbase_createdonbehalfby](systemuser.md#BKMK_lk_syncerrorbase_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_KbArticle_SyncErrors"></a> KbArticle_SyncErrors

See the [KbArticle_SyncErrors](kbarticle.md#BKMK_KbArticle_SyncErrors) one-to-many relationship for the [kbarticle](kbarticle.md) table/entity.

### <a name="BKMK_RollupField_SyncErrors"></a> RollupField_SyncErrors

See the [RollupField_SyncErrors](rollupfield.md#BKMK_RollupField_SyncErrors) one-to-many relationship for the [rollupfield](rollupfield.md) table/entity.

### <a name="BKMK_KbArticleTemplate_SyncErrors"></a> KbArticleTemplate_SyncErrors

See the [KbArticleTemplate_SyncErrors](kbarticletemplate.md#BKMK_KbArticleTemplate_SyncErrors) one-to-many relationship for the [kbarticletemplate](kbarticletemplate.md) table/entity.

### <a name="BKMK_Account_SyncErrors"></a> Account_SyncErrors

See the [Account_SyncErrors](account.md#BKMK_Account_SyncErrors) one-to-many relationship for the [account](account.md) table/entity.

### <a name="BKMK_FieldSecurityProfile_SyncErrors"></a> FieldSecurityProfile_SyncErrors

See the [FieldSecurityProfile_SyncErrors](fieldsecurityprofile.md#BKMK_FieldSecurityProfile_SyncErrors) one-to-many relationship for the [fieldsecurityprofile](fieldsecurityprofile.md) table/entity.

### <a name="BKMK_UserQueryVisualization_SyncErrors"></a> UserQueryVisualization_SyncErrors

See the [UserQueryVisualization_SyncErrors](userqueryvisualization.md#BKMK_UserQueryVisualization_SyncErrors) one-to-many relationship for the [userqueryvisualization](userqueryvisualization.md) table/entity.

### <a name="BKMK_FieldPermission_SyncErrors"></a> FieldPermission_SyncErrors

See the [FieldPermission_SyncErrors](fieldpermission.md#BKMK_FieldPermission_SyncErrors) one-to-many relationship for the [fieldpermission](fieldpermission.md) table/entity.

### <a name="BKMK_DuplicateRuleCondition_SyncErrors"></a> DuplicateRuleCondition_SyncErrors

See the [DuplicateRuleCondition_SyncErrors](duplicaterulecondition.md#BKMK_DuplicateRuleCondition_SyncErrors) one-to-many relationship for the [duplicaterulecondition](duplicaterulecondition.md) table/entity.

### <a name="BKMK_Team_SyncErrors"></a> Team_SyncErrors

See the [Team_SyncErrors](team.md#BKMK_Team_SyncErrors) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_SLAItem_SyncErrors"></a> SLAItem_SyncErrors

See the [SLAItem_SyncErrors](slaitem.md#BKMK_SLAItem_SyncErrors) one-to-many relationship for the [slaitem](slaitem.md) table/entity.

### <a name="BKMK_KnowledgeArticleViews_SyncErrors"></a> KnowledgeArticleViews_SyncErrors

See the [KnowledgeArticleViews_SyncErrors](knowledgearticleviews.md#BKMK_KnowledgeArticleViews_SyncErrors) one-to-many relationship for the [knowledgearticleviews](knowledgearticleviews.md) table/entity.

### <a name="BKMK_Appointment_SyncErrors"></a> Appointment_SyncErrors

See the [Appointment_SyncErrors](appointment.md#BKMK_Appointment_SyncErrors) one-to-many relationship for the [appointment](appointment.md) table/entity.

### <a name="BKMK_SystemUser_SyncError"></a> SystemUser_SyncError

See the [SystemUser_SyncError](systemuser.md#BKMK_SystemUser_SyncError) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_Contact_SyncErrors"></a> Contact_SyncErrors

See the [Contact_SyncErrors](contact.md#BKMK_Contact_SyncErrors) one-to-many relationship for the [contact](contact.md) table/entity.

### <a name="BKMK_ExpiredProcess_SyncErrors"></a> ExpiredProcess_SyncErrors

See the [ExpiredProcess_SyncErrors](expiredprocess.md#BKMK_ExpiredProcess_SyncErrors) one-to-many relationship for the [expiredprocess](expiredprocess.md) table/entity.

### <a name="BKMK_Workflow_SyncErrors"></a> Workflow_SyncErrors

See the [Workflow_SyncErrors](workflow.md#BKMK_Workflow_SyncErrors) one-to-many relationship for the [workflow](workflow.md) table/entity.

### <a name="BKMK_NewProcess_SyncErrors"></a> NewProcess_SyncErrors

See the [NewProcess_SyncErrors](newprocess.md#BKMK_NewProcess_SyncErrors) one-to-many relationship for the [newprocess](newprocess.md) table/entity.

### <a name="BKMK_Feedback_SyncErrors"></a> Feedback_SyncErrors

See the [Feedback_SyncErrors](feedback.md#BKMK_Feedback_SyncErrors) one-to-many relationship for the [feedback](feedback.md) table/entity.

### <a name="BKMK_ActivityParty_SyncErrors"></a> ActivityParty_SyncErrors

See the [ActivityParty_SyncErrors](activityparty.md#BKMK_ActivityParty_SyncErrors) one-to-many relationship for the [activityparty](activityparty.md) table/entity.

### <a name="BKMK_Annotation_SyncErrors"></a> Annotation_SyncErrors

See the [Annotation_SyncErrors](annotation.md#BKMK_Annotation_SyncErrors) one-to-many relationship for the [annotation](annotation.md) table/entity.

### <a name="BKMK_Email_SyncErrors"></a> Email_SyncErrors

See the [Email_SyncErrors](email.md#BKMK_Email_SyncErrors) one-to-many relationship for the [email](email.md) table/entity.

### <a name="BKMK_Organization_SyncErrors"></a> Organization_SyncErrors

See the [Organization_SyncErrors](organization.md#BKMK_Organization_SyncErrors) one-to-many relationship for the [organization](organization.md) table/entity.

### <a name="BKMK_ActivityMimeAttachment_SyncErrors"></a> ActivityMimeAttachment_SyncErrors

See the [ActivityMimeAttachment_SyncErrors](activitymimeattachment.md#BKMK_ActivityMimeAttachment_SyncErrors) one-to-many relationship for the [activitymimeattachment](activitymimeattachment.md) table/entity.

### <a name="BKMK_Task_SyncErrors"></a> Task_SyncErrors

See the [Task_SyncErrors](task.md#BKMK_Task_SyncErrors) one-to-many relationship for the [task](task.md) table/entity.

### <a name="BKMK_Letter_SyncErrors"></a> Letter_SyncErrors

See the [Letter_SyncErrors](letter.md#BKMK_Letter_SyncErrors) one-to-many relationship for the [letter](letter.md) table/entity.

### <a name="BKMK_Template_SyncErrors"></a> Template_SyncErrors

See the [Template_SyncErrors](template.md#BKMK_Template_SyncErrors) one-to-many relationship for the [template](template.md) table/entity.

### <a name="BKMK_ProcessStage_SyncErrors"></a> ProcessStage_SyncErrors

See the [ProcessStage_SyncErrors](processstage.md#BKMK_ProcessStage_SyncErrors) one-to-many relationship for the [processstage](processstage.md) table/entity.

### <a name="BKMK_KnowledgeArticle_SyncErrors"></a> KnowledgeArticle_SyncErrors

See the [KnowledgeArticle_SyncErrors](knowledgearticle.md#BKMK_KnowledgeArticle_SyncErrors) one-to-many relationship for the [knowledgearticle](knowledgearticle.md) table/entity.

### <a name="BKMK_Position_SyncErrors"></a> Position_SyncErrors

See the [Position_SyncErrors](position.md#BKMK_Position_SyncErrors) one-to-many relationship for the [position](position.md) table/entity.

### <a name="BKMK_SharePointDocumentLocation_SyncErrors"></a> SharePointDocumentLocation_SyncErrors

See the [SharePointDocumentLocation_SyncErrors](sharepointdocumentlocation.md#BKMK_SharePointDocumentLocation_SyncErrors) one-to-many relationship for the [sharepointdocumentlocation](sharepointdocumentlocation.md) table/entity.

### <a name="BKMK_Report_SyncErrors"></a> Report_SyncErrors

See the [Report_SyncErrors](report.md#BKMK_Report_SyncErrors) one-to-many relationship for the [report](report.md) table/entity.

### <a name="BKMK_Connection_SyncErrors"></a> Connection_SyncErrors

See the [Connection_SyncErrors](connection.md#BKMK_Connection_SyncErrors) one-to-many relationship for the [connection](connection.md) table/entity.

### <a name="BKMK_ProcessSession_SyncErrors"></a> ProcessSession_SyncErrors

See the [ProcessSession_SyncErrors](processsession.md#BKMK_ProcessSession_SyncErrors) one-to-many relationship for the [processsession](processsession.md) table/entity.

### <a name="BKMK_Category_SyncErrors"></a> Category_SyncErrors

See the [Category_SyncErrors](category.md#BKMK_Category_SyncErrors) one-to-many relationship for the [category](category.md) table/entity.

### <a name="BKMK_ConnectionRole_SyncErrors"></a> ConnectionRole_SyncErrors

See the [ConnectionRole_SyncErrors](connectionrole.md#BKMK_ConnectionRole_SyncErrors) one-to-many relationship for the [connectionrole](connectionrole.md) table/entity.

### <a name="BKMK_ProcessTrigger_SyncErrors"></a> ProcessTrigger_SyncErrors

See the [ProcessTrigger_SyncErrors](processtrigger.md#BKMK_ProcessTrigger_SyncErrors) one-to-many relationship for the [processtrigger](processtrigger.md) table/entity.

### <a name="BKMK_Fax_SyncErrors"></a> Fax_SyncErrors

See the [Fax_SyncErrors](fax.md#BKMK_Fax_SyncErrors) one-to-many relationship for the [fax](fax.md) table/entity.

### <a name="BKMK_Mailbox_SyncErrors"></a> Mailbox_SyncErrors

See the [Mailbox_SyncErrors](mailbox.md#BKMK_Mailbox_SyncErrors) one-to-many relationship for the [mailbox](mailbox.md) table/entity.

### <a name="BKMK_BusinessUnit_SyncErrors"></a> BusinessUnit_SyncErrors

See the [BusinessUnit_SyncErrors](businessunit.md#BKMK_BusinessUnit_SyncErrors) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_Queue_SyncErrors"></a> Queue_SyncErrors

See the [Queue_SyncErrors](queue.md#BKMK_Queue_SyncErrors) one-to-many relationship for the [queue](queue.md) table/entity.

### <a name="BKMK_Role_SyncErrors"></a> Role_SyncErrors

See the [Role_SyncErrors](role.md#BKMK_Role_SyncErrors) one-to-many relationship for the [role](role.md) table/entity.

### <a name="BKMK_BusinessUnit_SyncError"></a> BusinessUnit_SyncError

See the [BusinessUnit_SyncError](businessunit.md#BKMK_BusinessUnit_SyncError) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_SystemUser_SyncErrors"></a> SystemUser_SyncErrors

See the [SystemUser_SyncErrors](systemuser.md#BKMK_SystemUser_SyncErrors) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_SLAKPIInstance_SyncErrors"></a> SLAKPIInstance_SyncErrors

See the [SLAKPIInstance_SyncErrors](slakpiinstance.md#BKMK_SLAKPIInstance_SyncErrors) one-to-many relationship for the [slakpiinstance](slakpiinstance.md) table/entity.

### <a name="BKMK_SLA_SyncErrors"></a> SLA_SyncErrors

See the [SLA_SyncErrors](sla.md#BKMK_SLA_SyncErrors) one-to-many relationship for the [sla](sla.md) table/entity.

### <a name="BKMK_SavedQueryVisualization_SyncErrors"></a> SavedQueryVisualization_SyncErrors

See the [SavedQueryVisualization_SyncErrors](savedqueryvisualization.md#BKMK_SavedQueryVisualization_SyncErrors) one-to-many relationship for the [savedqueryvisualization](savedqueryvisualization.md) table/entity.

### <a name="BKMK_GoalRollupQuery_SyncErrors"></a> GoalRollupQuery_SyncErrors

See the [GoalRollupQuery_SyncErrors](goalrollupquery.md#BKMK_GoalRollupQuery_SyncErrors) one-to-many relationship for the [goalrollupquery](goalrollupquery.md) table/entity.

### <a name="BKMK_Metric_SyncErrors"></a> Metric_SyncErrors

See the [Metric_SyncErrors](metric.md#BKMK_Metric_SyncErrors) one-to-many relationship for the [metric](metric.md) table/entity.

### <a name="BKMK_ImportMap_SyncErrors"></a> ImportMap_SyncErrors

See the [ImportMap_SyncErrors](importmap.md#BKMK_ImportMap_SyncErrors) one-to-many relationship for the [importmap](importmap.md) table/entity.

### <a name="BKMK_EmailServerProfile_SyncErrors"></a> EmailServerProfile_SyncErrors

See the [EmailServerProfile_SyncErrors](emailserverprofile.md#BKMK_EmailServerProfile_SyncErrors) one-to-many relationship for the [emailserverprofile](emailserverprofile.md) table/entity.

### <a name="BKMK_solutioncomponentattributeconfiguration_SyncErrors"></a> solutioncomponentattributeconfiguration_SyncErrors

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentattributeconfiguration_SyncErrors](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_SyncErrors) one-to-many relationship for the [solutioncomponentattributeconfiguration](solutioncomponentattributeconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentbatchconfiguration_SyncErrors"></a> solutioncomponentbatchconfiguration_SyncErrors

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentbatchconfiguration_SyncErrors](solutioncomponentbatchconfiguration.md#BKMK_solutioncomponentbatchconfiguration_SyncErrors) one-to-many relationship for the [solutioncomponentbatchconfiguration](solutioncomponentbatchconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentconfiguration_SyncErrors"></a> solutioncomponentconfiguration_SyncErrors

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentconfiguration_SyncErrors](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_SyncErrors) one-to-many relationship for the [solutioncomponentconfiguration](solutioncomponentconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentrelationshipconfiguration_SyncErrors"></a> solutioncomponentrelationshipconfiguration_SyncErrors

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentrelationshipconfiguration_SyncErrors](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_SyncErrors) one-to-many relationship for the [solutioncomponentrelationshipconfiguration](solutioncomponentrelationshipconfiguration.md) table/entity.

### <a name="BKMK_package_SyncErrors"></a> package_SyncErrors

**Added by**: msdyn_SolutionPackageMapping Solution

See the [package_SyncErrors](package.md#BKMK_package_SyncErrors) one-to-many relationship for the [package](package.md) table/entity.

### <a name="BKMK_stagesolutionupload_SyncErrors"></a> stagesolutionupload_SyncErrors

**Added by**: StageSolutionUpload Solution

See the [stagesolutionupload_SyncErrors](stagesolutionupload.md#BKMK_stagesolutionupload_SyncErrors) one-to-many relationship for the [stagesolutionupload](stagesolutionupload.md) table/entity.

### <a name="BKMK_exportsolutionupload_SyncErrors"></a> exportsolutionupload_SyncErrors

**Added by**: ExportSolutionUpload Solution

See the [exportsolutionupload_SyncErrors](exportsolutionupload.md#BKMK_exportsolutionupload_SyncErrors) one-to-many relationship for the [exportsolutionupload](exportsolutionupload.md) table/entity.

### <a name="BKMK_featurecontrolsetting_SyncErrors"></a> featurecontrolsetting_SyncErrors

**Added by**: msdyn_FeatureControlSetting Solution

See the [featurecontrolsetting_SyncErrors](featurecontrolsetting.md#BKMK_featurecontrolsetting_SyncErrors) one-to-many relationship for the [featurecontrolsetting](featurecontrolsetting.md) table/entity.

### <a name="BKMK_attributeimageconfig_SyncErrors"></a> attributeimageconfig_SyncErrors

**Added by**: Image Configuration Solution

See the [attributeimageconfig_SyncErrors](attributeimageconfig.md#BKMK_attributeimageconfig_SyncErrors) one-to-many relationship for the [attributeimageconfig](attributeimageconfig.md) table/entity.

### <a name="BKMK_entityimageconfig_SyncErrors"></a> entityimageconfig_SyncErrors

**Added by**: Image Configuration Solution

See the [entityimageconfig_SyncErrors](entityimageconfig.md#BKMK_entityimageconfig_SyncErrors) one-to-many relationship for the [entityimageconfig](entityimageconfig.md) table/entity.

### <a name="BKMK_relationshipattribute_SyncErrors"></a> relationshipattribute_SyncErrors

**Added by**: Metadata Extension Solution

See the [relationshipattribute_SyncErrors](relationshipattribute.md#BKMK_relationshipattribute_SyncErrors) one-to-many relationship for the [relationshipattribute](relationshipattribute.md) table/entity.

### <a name="BKMK_stagedentity_SyncErrors"></a> stagedentity_SyncErrors

**Added by**: Metadata Extension Solution

See the [stagedentity_SyncErrors](stagedentity.md#BKMK_stagedentity_SyncErrors) one-to-many relationship for the [stagedentity](stagedentity.md) table/entity.

### <a name="BKMK_stagedentityattribute_SyncErrors"></a> stagedentityattribute_SyncErrors

**Added by**: Metadata Extension Solution

See the [stagedentityattribute_SyncErrors](stagedentityattribute.md#BKMK_stagedentityattribute_SyncErrors) one-to-many relationship for the [stagedentityattribute](stagedentityattribute.md) table/entity.

### <a name="BKMK_catalog_SyncErrors"></a> catalog_SyncErrors

**Added by**: CatalogFramework Solution

See the [catalog_SyncErrors](catalog.md#BKMK_catalog_SyncErrors) one-to-many relationship for the [catalog](catalog.md) table/entity.

### <a name="BKMK_catalogassignment_SyncErrors"></a> catalogassignment_SyncErrors

**Added by**: CatalogFramework Solution

See the [catalogassignment_SyncErrors](catalogassignment.md#BKMK_catalogassignment_SyncErrors) one-to-many relationship for the [catalogassignment](catalogassignment.md) table/entity.

### <a name="BKMK_customapi_SyncErrors"></a> customapi_SyncErrors

**Added by**: Custom API Framework Solution

See the [customapi_SyncErrors](customapi.md#BKMK_customapi_SyncErrors) one-to-many relationship for the [customapi](customapi.md) table/entity.

### <a name="BKMK_customapirequestparameter_SyncErrors"></a> customapirequestparameter_SyncErrors

**Added by**: Custom API Framework Solution

See the [customapirequestparameter_SyncErrors](customapirequestparameter.md#BKMK_customapirequestparameter_SyncErrors) one-to-many relationship for the [customapirequestparameter](customapirequestparameter.md) table/entity.

### <a name="BKMK_customapiresponseproperty_SyncErrors"></a> customapiresponseproperty_SyncErrors

**Added by**: Custom API Framework Solution

See the [customapiresponseproperty_SyncErrors](customapiresponseproperty.md#BKMK_customapiresponseproperty_SyncErrors) one-to-many relationship for the [customapiresponseproperty](customapiresponseproperty.md) table/entity.

### <a name="BKMK_provisionlanguageforuser_SyncErrors"></a> provisionlanguageforuser_SyncErrors

**Added by**: msft_LocalizationExtension Solution

See the [provisionlanguageforuser_SyncErrors](provisionlanguageforuser.md#BKMK_provisionlanguageforuser_SyncErrors) one-to-many relationship for the [provisionlanguageforuser](provisionlanguageforuser.md) table/entity.

### <a name="BKMK_sharedobject_SyncErrors"></a> sharedobject_SyncErrors

**Added by**: Real-time Collaboration App Solution

See the [sharedobject_SyncErrors](sharedobject.md#BKMK_sharedobject_SyncErrors) one-to-many relationship for the [sharedobject](sharedobject.md) table/entity.

### <a name="BKMK_sharedworkspace_SyncErrors"></a> sharedworkspace_SyncErrors

**Added by**: Real-time Collaboration App Solution

See the [sharedworkspace_SyncErrors](sharedworkspace.md#BKMK_sharedworkspace_SyncErrors) one-to-many relationship for the [sharedworkspace](sharedworkspace.md) table/entity.

### <a name="BKMK_sharedworkspacepool_SyncErrors"></a> sharedworkspacepool_SyncErrors

**Added by**: Real-time Collaboration App Solution

See the [sharedworkspacepool_SyncErrors](sharedworkspacepool.md#BKMK_sharedworkspacepool_SyncErrors) one-to-many relationship for the [sharedworkspacepool](sharedworkspacepool.md) table/entity.

### <a name="BKMK_entityanalyticsconfig_SyncErrors"></a> entityanalyticsconfig_SyncErrors

**Added by**: Advanced Analytics Infrastructure Solution

See the [entityanalyticsconfig_SyncErrors](entityanalyticsconfig.md#BKMK_entityanalyticsconfig_SyncErrors) one-to-many relationship for the [entityanalyticsconfig](entityanalyticsconfig.md) table/entity.

### <a name="BKMK_datalakefolder_SyncErrors"></a> datalakefolder_SyncErrors

**Added by**: Data lake workspaces Solution

See the [datalakefolder_SyncErrors](datalakefolder.md#BKMK_datalakefolder_SyncErrors) one-to-many relationship for the [datalakefolder](datalakefolder.md) table/entity.

### <a name="BKMK_datalakefolderpermission_SyncErrors"></a> datalakefolderpermission_SyncErrors

**Added by**: Data lake workspaces Solution

See the [datalakefolderpermission_SyncErrors](datalakefolderpermission.md#BKMK_datalakefolderpermission_SyncErrors) one-to-many relationship for the [datalakefolderpermission](datalakefolderpermission.md) table/entity.

### <a name="BKMK_datalakeworkspace_SyncErrors"></a> datalakeworkspace_SyncErrors

**Added by**: Data lake workspaces Solution

See the [datalakeworkspace_SyncErrors](datalakeworkspace.md#BKMK_datalakeworkspace_SyncErrors) one-to-many relationship for the [datalakeworkspace](datalakeworkspace.md) table/entity.

### <a name="BKMK_datalakeworkspacepermission_SyncErrors"></a> datalakeworkspacepermission_SyncErrors

**Added by**: Data lake workspaces Solution

See the [datalakeworkspacepermission_SyncErrors](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_SyncErrors) one-to-many relationship for the [datalakeworkspacepermission](datalakeworkspacepermission.md) table/entity.

### <a name="BKMK_dataprocessingconfiguration_SyncErrors"></a> dataprocessingconfiguration_SyncErrors

**Added by**: Data lake workspaces Solution

See the [dataprocessingconfiguration_SyncErrors](dataprocessingconfiguration.md#BKMK_dataprocessingconfiguration_SyncErrors) one-to-many relationship for the [dataprocessingconfiguration](dataprocessingconfiguration.md) table/entity.

### <a name="BKMK_exportedexcel_SyncErrors"></a> exportedexcel_SyncErrors

**Added by**: Data lake workspaces Solution

See the [exportedexcel_SyncErrors](exportedexcel.md#BKMK_exportedexcel_SyncErrors) one-to-many relationship for the [exportedexcel](exportedexcel.md) table/entity.

### <a name="BKMK_retaineddataexcel_SyncErrors"></a> retaineddataexcel_SyncErrors

**Added by**: Data lake workspaces Solution

See the [retaineddataexcel_SyncErrors](retaineddataexcel.md#BKMK_retaineddataexcel_SyncErrors) one-to-many relationship for the [retaineddataexcel](retaineddataexcel.md) table/entity.

### <a name="BKMK_synapsedatabase_SyncErrors"></a> synapsedatabase_SyncErrors

**Added by**: Data lake workspaces Solution

See the [synapsedatabase_SyncErrors](synapsedatabase.md#BKMK_synapsedatabase_SyncErrors) one-to-many relationship for the [synapsedatabase](synapsedatabase.md) table/entity.

### <a name="BKMK_synapselinkexternaltablestate_SyncErrors"></a> synapselinkexternaltablestate_SyncErrors

**Added by**: Synapse Link Solution

See the [synapselinkexternaltablestate_SyncErrors](synapselinkexternaltablestate.md#BKMK_synapselinkexternaltablestate_SyncErrors) one-to-many relationship for the [synapselinkexternaltablestate](synapselinkexternaltablestate.md) table/entity.

### <a name="BKMK_synapselinkprofile_SyncErrors"></a> synapselinkprofile_SyncErrors

**Added by**: Synapse Link Solution

See the [synapselinkprofile_SyncErrors](synapselinkprofile.md#BKMK_synapselinkprofile_SyncErrors) one-to-many relationship for the [synapselinkprofile](synapselinkprofile.md) table/entity.

### <a name="BKMK_synapselinkprofileentity_SyncErrors"></a> synapselinkprofileentity_SyncErrors

**Added by**: Synapse Link Solution

See the [synapselinkprofileentity_SyncErrors](synapselinkprofileentity.md#BKMK_synapselinkprofileentity_SyncErrors) one-to-many relationship for the [synapselinkprofileentity](synapselinkprofileentity.md) table/entity.

### <a name="BKMK_synapselinkprofileentitystate_SyncErrors"></a> synapselinkprofileentitystate_SyncErrors

**Added by**: Synapse Link Solution

See the [synapselinkprofileentitystate_SyncErrors](synapselinkprofileentitystate.md#BKMK_synapselinkprofileentitystate_SyncErrors) one-to-many relationship for the [synapselinkprofileentitystate](synapselinkprofileentitystate.md) table/entity.

### <a name="BKMK_synapselinkschedule_SyncErrors"></a> synapselinkschedule_SyncErrors

**Added by**: Synapse Link Solution

See the [synapselinkschedule_SyncErrors](synapselinkschedule.md#BKMK_synapselinkschedule_SyncErrors) one-to-many relationship for the [synapselinkschedule](synapselinkschedule.md) table/entity.

### <a name="BKMK_msdyn_dataflow_SyncErrors"></a> msdyn_dataflow_SyncErrors

**Added by**: Dataflow Solution Solution

See the [msdyn_dataflow_SyncErrors](msdyn_dataflow.md#BKMK_msdyn_dataflow_SyncErrors) one-to-many relationship for the [msdyn_dataflow](msdyn_dataflow.md) table/entity.

### <a name="BKMK_msdyn_dataflowrefreshhistory_SyncErrors"></a> msdyn_dataflowrefreshhistory_SyncErrors

**Added by**: Dataflow Solution Solution

See the [msdyn_dataflowrefreshhistory_SyncErrors](msdyn_dataflowrefreshhistory.md#BKMK_msdyn_dataflowrefreshhistory_SyncErrors) one-to-many relationship for the [msdyn_dataflowrefreshhistory](msdyn_dataflowrefreshhistory.md) table/entity.

### <a name="BKMK_msdyn_entityrefreshhistory_SyncErrors"></a> msdyn_entityrefreshhistory_SyncErrors

**Added by**: Dataflow Solution Solution

See the [msdyn_entityrefreshhistory_SyncErrors](msdyn_entityrefreshhistory.md#BKMK_msdyn_entityrefreshhistory_SyncErrors) one-to-many relationship for the [msdyn_entityrefreshhistory](msdyn_entityrefreshhistory.md) table/entity.

### <a name="BKMK_sharedlinksetting_SyncErrors"></a> sharedlinksetting_SyncErrors

**Added by**: Access Team Solution

See the [sharedlinksetting_SyncErrors](sharedlinksetting.md#BKMK_sharedlinksetting_SyncErrors) one-to-many relationship for the [sharedlinksetting](sharedlinksetting.md) table/entity.

### <a name="BKMK_entityrecordfilter_SyncErrors"></a> entityrecordfilter_SyncErrors

**Added by**: AuthorizationCore Solution

See the [entityrecordfilter_SyncErrors](entityrecordfilter.md#BKMK_entityrecordfilter_SyncErrors) one-to-many relationship for the [entityrecordfilter](entityrecordfilter.md) table/entity.

### <a name="BKMK_recordfilter_SyncErrors"></a> recordfilter_SyncErrors

**Added by**: AuthorizationCore Solution

See the [recordfilter_SyncErrors](recordfilter.md#BKMK_recordfilter_SyncErrors) one-to-many relationship for the [recordfilter](recordfilter.md) table/entity.

### <a name="BKMK_delegatedauthorization_SyncErrors"></a> delegatedauthorization_SyncErrors

**Added by**: Delegated Authorization Solution

See the [delegatedauthorization_SyncErrors](delegatedauthorization.md#BKMK_delegatedauthorization_SyncErrors) one-to-many relationship for the [delegatedauthorization](delegatedauthorization.md) table/entity.

### <a name="BKMK_serviceplan_SyncErrors"></a> serviceplan_SyncErrors

**Added by**: License Enforcement Solution

See the [serviceplan_SyncErrors](serviceplan.md#BKMK_serviceplan_SyncErrors) one-to-many relationship for the [serviceplan](serviceplan.md) table/entity.

### <a name="BKMK_serviceplanmapping_SyncErrors"></a> serviceplanmapping_SyncErrors

**Added by**: License Enforcement Solution

See the [serviceplanmapping_SyncErrors](serviceplanmapping.md#BKMK_serviceplanmapping_SyncErrors) one-to-many relationship for the [serviceplanmapping](serviceplanmapping.md) table/entity.

### <a name="BKMK_applicationuser_SyncErrors"></a> applicationuser_SyncErrors

**Added by**: ApplicationUserSolution Solution

See the [applicationuser_SyncErrors](applicationuser.md#BKMK_applicationuser_SyncErrors) one-to-many relationship for the [applicationuser](applicationuser.md) table/entity.

### <a name="BKMK_connector_SyncErrors"></a> connector_SyncErrors

**Added by**: Power Connector Solution Solution

See the [connector_SyncErrors](connector.md#BKMK_connector_SyncErrors) one-to-many relationship for the [connector](connector.md) table/entity.

### <a name="BKMK_environmentvariabledefinition_SyncErrors"></a> environmentvariabledefinition_SyncErrors

**Added by**: Environment Variables Solution

See the [environmentvariabledefinition_SyncErrors](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_SyncErrors) one-to-many relationship for the [environmentvariabledefinition](environmentvariabledefinition.md) table/entity.

### <a name="BKMK_environmentvariablevalue_SyncErrors"></a> environmentvariablevalue_SyncErrors

**Added by**: Environment Variables Solution

See the [environmentvariablevalue_SyncErrors](environmentvariablevalue.md#BKMK_environmentvariablevalue_SyncErrors) one-to-many relationship for the [environmentvariablevalue](environmentvariablevalue.md) table/entity.

### <a name="BKMK_workflowbinary_SyncErrors"></a> workflowbinary_SyncErrors

**Added by**: Power Automate Extensions Workflow Binary package Solution

See the [workflowbinary_SyncErrors](workflowbinary.md#BKMK_workflowbinary_SyncErrors) one-to-many relationship for the [workflowbinary](workflowbinary.md) table/entity.

### <a name="BKMK_desktopflowmodule_SyncErrors"></a> desktopflowmodule_SyncErrors

**Added by**: Power Automate Extensions core package Solution

See the [desktopflowmodule_SyncErrors](desktopflowmodule.md#BKMK_desktopflowmodule_SyncErrors) one-to-many relationship for the [desktopflowmodule](desktopflowmodule.md) table/entity.

### <a name="BKMK_flowmachine_SyncErrors"></a> flowmachine_SyncErrors

**Added by**: Power Automate Extensions core package Solution

See the [flowmachine_SyncErrors](flowmachine.md#BKMK_flowmachine_SyncErrors) one-to-many relationship for the [flowmachine](flowmachine.md) table/entity.

### <a name="BKMK_flowmachinegroup_SyncErrors"></a> flowmachinegroup_SyncErrors

**Added by**: Power Automate Extensions core package Solution

See the [flowmachinegroup_SyncErrors](flowmachinegroup.md#BKMK_flowmachinegroup_SyncErrors) one-to-many relationship for the [flowmachinegroup](flowmachinegroup.md) table/entity.

### <a name="BKMK_flowmachineimage_SyncErrors"></a> flowmachineimage_SyncErrors

**Added by**: Power Automate Extensions core package Solution

See the [flowmachineimage_SyncErrors](flowmachineimage.md#BKMK_flowmachineimage_SyncErrors) one-to-many relationship for the [flowmachineimage](flowmachineimage.md) table/entity.

### <a name="BKMK_flowmachineimageversion_SyncErrors"></a> flowmachineimageversion_SyncErrors

**Added by**: Power Automate Extensions core package Solution

See the [flowmachineimageversion_SyncErrors](flowmachineimageversion.md#BKMK_flowmachineimageversion_SyncErrors) one-to-many relationship for the [flowmachineimageversion](flowmachineimageversion.md) table/entity.

### <a name="BKMK_flowmachinenetwork_SyncErrors"></a> flowmachinenetwork_SyncErrors

**Added by**: Power Automate Extensions core package Solution

See the [flowmachinenetwork_SyncErrors](flowmachinenetwork.md#BKMK_flowmachinenetwork_SyncErrors) one-to-many relationship for the [flowmachinenetwork](flowmachinenetwork.md) table/entity.

### <a name="BKMK_processstageparameter_SyncErrors"></a> processstageparameter_SyncErrors

**Added by**: Power Automate Extensions core package Solution

See the [processstageparameter_SyncErrors](processstageparameter.md#BKMK_processstageparameter_SyncErrors) one-to-many relationship for the [processstageparameter](processstageparameter.md) table/entity.

### <a name="BKMK_workqueue_SyncErrors"></a> workqueue_SyncErrors

**Added by**: Power Automate Extensions core package Solution

See the [workqueue_SyncErrors](workqueue.md#BKMK_workqueue_SyncErrors) one-to-many relationship for the [workqueue](workqueue.md) table/entity.

### <a name="BKMK_workqueueitem_SyncErrors"></a> workqueueitem_SyncErrors

**Added by**: Power Automate Extensions core package Solution

See the [workqueueitem_SyncErrors](workqueueitem.md#BKMK_workqueueitem_SyncErrors) one-to-many relationship for the [workqueueitem](workqueueitem.md) table/entity.

### <a name="BKMK_desktopflowbinary_SyncErrors"></a> desktopflowbinary_SyncErrors

**Added by**: Power Automate Extensions core package Solution

See the [desktopflowbinary_SyncErrors](desktopflowbinary.md#BKMK_desktopflowbinary_SyncErrors) one-to-many relationship for the [desktopflowbinary](desktopflowbinary.md) table/entity.

### <a name="BKMK_flowsession_SyncErrors"></a> flowsession_SyncErrors

**Added by**: Power Automate Extensions core package Solution

See the [flowsession_SyncErrors](flowsession.md#BKMK_flowsession_SyncErrors) one-to-many relationship for the [flowsession](flowsession.md) table/entity.

### <a name="BKMK_connectionreference_SyncErrors"></a> connectionreference_SyncErrors

**Added by**: Power Platform Connection References Solution

See the [connectionreference_SyncErrors](connectionreference.md#BKMK_connectionreference_SyncErrors) one-to-many relationship for the [connectionreference](connectionreference.md) table/entity.

### <a name="BKMK_connectioninstance_SyncErrors"></a> connectioninstance_SyncErrors

**Added by**: Connection Instance Solution Solution

See the [connectioninstance_SyncErrors](connectioninstance.md#BKMK_connectioninstance_SyncErrors) one-to-many relationship for the [connectioninstance](connectioninstance.md) table/entity.

### <a name="BKMK_msdyn_helppage_SyncErrors"></a> msdyn_helppage_SyncErrors

**Added by**: Contextual Help Solution

See the [msdyn_helppage_SyncErrors](msdyn_helppage.md#BKMK_msdyn_helppage_SyncErrors) one-to-many relationship for the [msdyn_helppage](msdyn_helppage.md) table/entity.

### <a name="BKMK_msdyn_tour_SyncErrors"></a> msdyn_tour_SyncErrors

**Added by**: Contextual Help Solution

See the [msdyn_tour_SyncErrors](msdyn_tour.md#BKMK_msdyn_tour_SyncErrors) one-to-many relationship for the [msdyn_tour](msdyn_tour.md) table/entity.

### <a name="BKMK_msdynce_botcontent_SyncErrors"></a> msdynce_botcontent_SyncErrors

**Added by**: Customer Care Intelligence Bots Solution

See the [msdynce_botcontent_SyncErrors](msdynce_botcontent.md#BKMK_msdynce_botcontent_SyncErrors) one-to-many relationship for the [msdynce_botcontent](msdynce_botcontent.md) table/entity.

### <a name="BKMK_conversationtranscript_SyncErrors"></a> conversationtranscript_SyncErrors

**Added by**: Power Virtual Agents Common Solution

See the [conversationtranscript_SyncErrors](conversationtranscript.md#BKMK_conversationtranscript_SyncErrors) one-to-many relationship for the [conversationtranscript](conversationtranscript.md) table/entity.

### <a name="BKMK_bot_SyncErrors"></a> bot_SyncErrors

**Added by**: Power Virtual Agents Solution

See the [bot_SyncErrors](bot.md#BKMK_bot_SyncErrors) one-to-many relationship for the [bot](bot.md) table/entity.

### <a name="BKMK_botcomponent_SyncErrors"></a> botcomponent_SyncErrors

**Added by**: Power Virtual Agents Solution

See the [botcomponent_SyncErrors](botcomponent.md#BKMK_botcomponent_SyncErrors) one-to-many relationship for the [botcomponent](botcomponent.md) table/entity.

### <a name="BKMK_Territory_SyncErrors"></a> Territory_SyncErrors

**Added by**: Application Common Solution

See the [Territory_SyncErrors](territory.md#BKMK_Territory_SyncErrors) one-to-many relationship for the [territory](territory.md) table/entity.

### <a name="BKMK_activityfileattachment_SyncErrors"></a> activityfileattachment_SyncErrors

**Added by**: Activities Patch Solution

See the [activityfileattachment_SyncErrors](activityfileattachment.md#BKMK_activityfileattachment_SyncErrors) one-to-many relationship for the [activityfileattachment](activityfileattachment.md) table/entity.

### <a name="BKMK_chat_SyncErrors"></a> chat_SyncErrors

**Added by**: Activities Patch Solution

See the [chat_SyncErrors](chat.md#BKMK_chat_SyncErrors) one-to-many relationship for the [chat](chat.md) table/entity.

### <a name="BKMK_msdyn_serviceconfiguration_SyncErrors"></a> msdyn_serviceconfiguration_SyncErrors

**Added by**: Service Level Agreement (SLA) Extension Solution

See the [msdyn_serviceconfiguration_SyncErrors](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_SyncErrors) one-to-many relationship for the [msdyn_serviceconfiguration](msdyn_serviceconfiguration.md) table/entity.

### <a name="BKMK_msdyn_slakpi_SyncErrors"></a> msdyn_slakpi_SyncErrors

**Added by**: Service Level Agreement (SLA) Extension Solution

See the [msdyn_slakpi_SyncErrors](msdyn_slakpi.md#BKMK_msdyn_slakpi_SyncErrors) one-to-many relationship for the [msdyn_slakpi](msdyn_slakpi.md) table/entity.

### <a name="BKMK_msdyn_knowledgemanagementsetting_SyncErrors"></a> msdyn_knowledgemanagementsetting_SyncErrors

**Added by**: Knowledge Management Patch Solution

See the [msdyn_knowledgemanagementsetting_SyncErrors](msdyn_knowledgemanagementsetting.md#BKMK_msdyn_knowledgemanagementsetting_SyncErrors) one-to-many relationship for the [msdyn_knowledgemanagementsetting](msdyn_knowledgemanagementsetting.md) table/entity.

### <a name="BKMK_msdyn_federatedarticle_SyncErrors"></a> msdyn_federatedarticle_SyncErrors

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_federatedarticle_SyncErrors](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_SyncErrors) one-to-many relationship for the [msdyn_federatedarticle](msdyn_federatedarticle.md) table/entity.

### <a name="BKMK_msdyn_federatedarticleincident_SyncErrors"></a> msdyn_federatedarticleincident_SyncErrors

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_federatedarticleincident_SyncErrors](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_SyncErrors) one-to-many relationship for the [msdyn_federatedarticleincident](msdyn_federatedarticleincident.md) table/entity.

### <a name="BKMK_msdyn_integratedsearchprovider_SyncErrors"></a> msdyn_integratedsearchprovider_SyncErrors

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_integratedsearchprovider_SyncErrors](msdyn_integratedsearchprovider.md#BKMK_msdyn_integratedsearchprovider_SyncErrors) one-to-many relationship for the [msdyn_integratedsearchprovider](msdyn_integratedsearchprovider.md) table/entity.

### <a name="BKMK_msdyn_kmfederatedsearchconfig_SyncErrors"></a> msdyn_kmfederatedsearchconfig_SyncErrors

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_kmfederatedsearchconfig_SyncErrors](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_SyncErrors) one-to-many relationship for the [msdyn_kmfederatedsearchconfig](msdyn_kmfederatedsearchconfig.md) table/entity.

### <a name="BKMK_msdyn_knowledgearticleimage_SyncErrors"></a> msdyn_knowledgearticleimage_SyncErrors

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgearticleimage_SyncErrors](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_SyncErrors) one-to-many relationship for the [msdyn_knowledgearticleimage](msdyn_knowledgearticleimage.md) table/entity.

### <a name="BKMK_msdyn_knowledgeconfiguration_SyncErrors"></a> msdyn_knowledgeconfiguration_SyncErrors

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgeconfiguration_SyncErrors](msdyn_knowledgeconfiguration.md#BKMK_msdyn_knowledgeconfiguration_SyncErrors) one-to-many relationship for the [msdyn_knowledgeconfiguration](msdyn_knowledgeconfiguration.md) table/entity.

### <a name="BKMK_msdyn_knowledgeinteractioninsight_SyncErrors"></a> msdyn_knowledgeinteractioninsight_SyncErrors

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgeinteractioninsight_SyncErrors](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_SyncErrors) one-to-many relationship for the [msdyn_knowledgeinteractioninsight](msdyn_knowledgeinteractioninsight.md) table/entity.

### <a name="BKMK_msdyn_knowledgesearchinsight_SyncErrors"></a> msdyn_knowledgesearchinsight_SyncErrors

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgesearchinsight_SyncErrors](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_SyncErrors) one-to-many relationship for the [msdyn_knowledgesearchinsight](msdyn_knowledgesearchinsight.md) table/entity.

### <a name="BKMK_msdyn_favoriteknowledgearticle_SyncErrors"></a> msdyn_favoriteknowledgearticle_SyncErrors

**Added by**: Knowledge Management Features Solution

See the [msdyn_favoriteknowledgearticle_SyncErrors](msdyn_favoriteknowledgearticle.md#BKMK_msdyn_favoriteknowledgearticle_SyncErrors) one-to-many relationship for the [msdyn_favoriteknowledgearticle](msdyn_favoriteknowledgearticle.md) table/entity.

### <a name="BKMK_msdyn_kalanguagesetting_SyncErrors"></a> msdyn_kalanguagesetting_SyncErrors

**Added by**: Knowledge Management Features Solution

See the [msdyn_kalanguagesetting_SyncErrors](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_SyncErrors) one-to-many relationship for the [msdyn_kalanguagesetting](msdyn_kalanguagesetting.md) table/entity.

### <a name="BKMK_msdyn_kbattachment_SyncErrors"></a> msdyn_kbattachment_SyncErrors

**Added by**: Knowledge Management Features Solution

See the [msdyn_kbattachment_SyncErrors](msdyn_kbattachment.md#BKMK_msdyn_kbattachment_SyncErrors) one-to-many relationship for the [msdyn_kbattachment](msdyn_kbattachment.md) table/entity.

### <a name="BKMK_msdyn_kmpersonalizationsetting_SyncErrors"></a> msdyn_kmpersonalizationsetting_SyncErrors

**Added by**: Knowledge Management Features Solution

See the [msdyn_kmpersonalizationsetting_SyncErrors](msdyn_kmpersonalizationsetting.md#BKMK_msdyn_kmpersonalizationsetting_SyncErrors) one-to-many relationship for the [msdyn_kmpersonalizationsetting](msdyn_kmpersonalizationsetting.md) table/entity.

### <a name="BKMK_msdyn_knowledgearticletemplate_SyncErrors"></a> msdyn_knowledgearticletemplate_SyncErrors

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgearticletemplate_SyncErrors](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_SyncErrors) one-to-many relationship for the [msdyn_knowledgearticletemplate](msdyn_knowledgearticletemplate.md) table/entity.

### <a name="BKMK_msdyn_knowledgepersonalfilter_SyncErrors"></a> msdyn_knowledgepersonalfilter_SyncErrors

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgepersonalfilter_SyncErrors](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_SyncErrors) one-to-many relationship for the [msdyn_knowledgepersonalfilter](msdyn_knowledgepersonalfilter.md) table/entity.

### <a name="BKMK_msdyn_knowledgesearchfilter_SyncErrors"></a> msdyn_knowledgesearchfilter_SyncErrors

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgesearchfilter_SyncErrors](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_SyncErrors) one-to-many relationship for the [msdyn_knowledgesearchfilter](msdyn_knowledgesearchfilter.md) table/entity.

### <a name="BKMK_pluginpackage_SyncErrors"></a> pluginpackage_SyncErrors

**Added by**: Plugin Infrastructure Extension Solution

See the [pluginpackage_SyncErrors](pluginpackage.md#BKMK_pluginpackage_SyncErrors) one-to-many relationship for the [pluginpackage](pluginpackage.md) table/entity.

### <a name="BKMK_fxexpression_SyncErrors"></a> fxexpression_SyncErrors

**Added by**: msft_PowerfxRuleSolution Solution

See the [fxexpression_SyncErrors](fxexpression.md#BKMK_fxexpression_SyncErrors) one-to-many relationship for the [fxexpression](fxexpression.md) table/entity.

### <a name="BKMK_powerfxrule_SyncErrors"></a> powerfxrule_SyncErrors

**Added by**: msft_PowerfxRuleSolution Solution

See the [powerfxrule_SyncErrors](powerfxrule.md#BKMK_powerfxrule_SyncErrors) one-to-many relationship for the [powerfxrule](powerfxrule.md) table/entity.

### <a name="BKMK_keyvaultreference_SyncErrors"></a> keyvaultreference_SyncErrors

**Added by**: ManagedIdentityExtensions Solution

See the [keyvaultreference_SyncErrors](keyvaultreference.md#BKMK_keyvaultreference_SyncErrors) one-to-many relationship for the [keyvaultreference](keyvaultreference.md) table/entity.

### <a name="BKMK_managedidentity_SyncErrors"></a> managedidentity_SyncErrors

**Added by**: ManagedIdentityExtensions Solution

See the [managedidentity_SyncErrors](managedidentity.md#BKMK_managedidentity_SyncErrors) one-to-many relationship for the [managedidentity](managedidentity.md) table/entity.

### <a name="BKMK_msgraphresourcetosubscription_SyncErrors"></a> msgraphresourcetosubscription_SyncErrors

**Added by**: msft_ActivitiesInfra_Extensions Solution

See the [msgraphresourcetosubscription_SyncErrors](msgraphresourcetosubscription.md#BKMK_msgraphresourcetosubscription_SyncErrors) one-to-many relationship for the [msgraphresourcetosubscription](msgraphresourcetosubscription.md) table/entity.

### <a name="BKMK_virtualentitymetadata_SyncErrors"></a> virtualentitymetadata_SyncErrors

**Added by**: RuntimeIntegration Solution

See the [virtualentitymetadata_SyncErrors](virtualentitymetadata.md#BKMK_virtualentitymetadata_SyncErrors) one-to-many relationship for the [virtualentitymetadata](virtualentitymetadata.md) table/entity.

### <a name="BKMK_mobileofflineprofileextension_SyncErrors"></a> mobileofflineprofileextension_SyncErrors

**Added by**: MobileOfflineProfileExtensionSolution Solution

See the [mobileofflineprofileextension_SyncErrors](mobileofflineprofileextension.md#BKMK_mobileofflineprofileextension_SyncErrors) one-to-many relationship for the [mobileofflineprofileextension](mobileofflineprofileextension.md) table/entity.

### <a name="BKMK_teammobileofflineprofilemembership_SyncErrors"></a> teammobileofflineprofilemembership_SyncErrors

**Added by**: MobileOfflineMembership Solution

See the [teammobileofflineprofilemembership_SyncErrors](teammobileofflineprofilemembership.md#BKMK_teammobileofflineprofilemembership_SyncErrors) one-to-many relationship for the [teammobileofflineprofilemembership](teammobileofflineprofilemembership.md) table/entity.

### <a name="BKMK_usermobileofflineprofilemembership_SyncErrors"></a> usermobileofflineprofilemembership_SyncErrors

**Added by**: MobileOfflineMembership Solution

See the [usermobileofflineprofilemembership_SyncErrors](usermobileofflineprofilemembership.md#BKMK_usermobileofflineprofilemembership_SyncErrors) one-to-many relationship for the [usermobileofflineprofilemembership](usermobileofflineprofilemembership.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscription_SyncErrors"></a> organizationdatasyncsubscription_SyncErrors

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscription_SyncErrors](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_SyncErrors) one-to-many relationship for the [organizationdatasyncsubscription](organizationdatasyncsubscription.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscriptionentity_SyncErrors"></a> organizationdatasyncsubscriptionentity_SyncErrors

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscriptionentity_SyncErrors](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_SyncErrors) one-to-many relationship for the [organizationdatasyncsubscriptionentity](organizationdatasyncsubscriptionentity.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_SyncErrors"></a> organizationdatasyncsubscriptionfnotable_SyncErrors

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscriptionfnotable_SyncErrors](organizationdatasyncsubscriptionfnotable.md#BKMK_organizationdatasyncsubscriptionfnotable_SyncErrors) one-to-many relationship for the [organizationdatasyncsubscriptionfnotable](organizationdatasyncsubscriptionfnotable.md) table/entity.

### <a name="BKMK_organizationdatasyncfnostate_SyncErrors"></a> organizationdatasyncfnostate_SyncErrors

**Added by**: DataSyncState Solution

See the [organizationdatasyncfnostate_SyncErrors](organizationdatasyncfnostate.md#BKMK_organizationdatasyncfnostate_SyncErrors) one-to-many relationship for the [organizationdatasyncfnostate](organizationdatasyncfnostate.md) table/entity.

### <a name="BKMK_organizationdatasyncstate_SyncErrors"></a> organizationdatasyncstate_SyncErrors

**Added by**: DataSyncState Solution

See the [organizationdatasyncstate_SyncErrors](organizationdatasyncstate.md#BKMK_organizationdatasyncstate_SyncErrors) one-to-many relationship for the [organizationdatasyncstate](organizationdatasyncstate.md) table/entity.

### <a name="BKMK_metadataforarchival_SyncErrors"></a> metadataforarchival_SyncErrors

**Added by**: Retention Base Components Solution

See the [metadataforarchival_SyncErrors](metadataforarchival.md#BKMK_metadataforarchival_SyncErrors) one-to-many relationship for the [metadataforarchival](metadataforarchival.md) table/entity.

### <a name="BKMK_retentionconfig_SyncErrors"></a> retentionconfig_SyncErrors

**Added by**: Retention Base Components Solution

See the [retentionconfig_SyncErrors](retentionconfig.md#BKMK_retentionconfig_SyncErrors) one-to-many relationship for the [retentionconfig](retentionconfig.md) table/entity.

### <a name="BKMK_retentionfailuredetail_SyncErrors"></a> retentionfailuredetail_SyncErrors

**Added by**: Retention Base Components Solution

See the [retentionfailuredetail_SyncErrors](retentionfailuredetail.md#BKMK_retentionfailuredetail_SyncErrors) one-to-many relationship for the [retentionfailuredetail](retentionfailuredetail.md) table/entity.

### <a name="BKMK_retentionoperation_SyncErrors"></a> retentionoperation_SyncErrors

**Added by**: Retention Base Components Solution

See the [retentionoperation_SyncErrors](retentionoperation.md#BKMK_retentionoperation_SyncErrors) one-to-many relationship for the [retentionoperation](retentionoperation.md) table/entity.

### <a name="BKMK_retentionoperationdetail_SyncErrors"></a> retentionoperationdetail_SyncErrors

**Added by**: Retention Base Components Solution

See the [retentionoperationdetail_SyncErrors](retentionoperationdetail.md#BKMK_retentionoperationdetail_SyncErrors) one-to-many relationship for the [retentionoperationdetail](retentionoperationdetail.md) table/entity.

### <a name="BKMK_msdyn_appinsightsmetadata_SyncErrors"></a> msdyn_appinsightsmetadata_SyncErrors

**Added by**: Insights App Platform Solution

See the [msdyn_appinsightsmetadata_SyncErrors](msdyn_appinsightsmetadata.md#BKMK_msdyn_appinsightsmetadata_SyncErrors) one-to-many relationship for the [msdyn_appinsightsmetadata](msdyn_appinsightsmetadata.md) table/entity.

### <a name="BKMK_msdyn_dataflowtemplate_SyncErrors"></a> msdyn_dataflowtemplate_SyncErrors

**Added by**: Insights App Platform Solution

See the [msdyn_dataflowtemplate_SyncErrors](msdyn_dataflowtemplate.md#BKMK_msdyn_dataflowtemplate_SyncErrors) one-to-many relationship for the [msdyn_dataflowtemplate](msdyn_dataflowtemplate.md) table/entity.

### <a name="BKMK_msdyn_workflowactionstatus_SyncErrors"></a> msdyn_workflowactionstatus_SyncErrors

**Added by**: Insights App Platform Solution

See the [msdyn_workflowactionstatus_SyncErrors](msdyn_workflowactionstatus.md#BKMK_msdyn_workflowactionstatus_SyncErrors) one-to-many relationship for the [msdyn_workflowactionstatus](msdyn_workflowactionstatus.md) table/entity.

### <a name="BKMK_userrating_SyncErrors"></a> userrating_SyncErrors

**Added by**: User Rating Solution

See the [userrating_SyncErrors](userrating.md#BKMK_userrating_SyncErrors) one-to-many relationship for the [userrating](userrating.md) table/entity.

### <a name="BKMK_msdyn_mobileapp_SyncErrors"></a> msdyn_mobileapp_SyncErrors

**Added by**: Mobile Apps Solution Solution

See the [msdyn_mobileapp_SyncErrors](msdyn_mobileapp.md#BKMK_msdyn_mobileapp_SyncErrors) one-to-many relationship for the [msdyn_mobileapp](msdyn_mobileapp.md) table/entity.

### <a name="BKMK_msdyn_insightsstorevirtualentity_SyncErrors"></a> msdyn_insightsstorevirtualentity_SyncErrors

**Added by**: Insights Store Data Provider Solution

See the [msdyn_insightsstorevirtualentity_SyncErrors](msdyn_insightsstorevirtualentity.md#BKMK_msdyn_insightsstorevirtualentity_SyncErrors) one-to-many relationship for the [msdyn_insightsstorevirtualentity](msdyn_insightsstorevirtualentity.md) table/entity.

### <a name="BKMK_roleeditorlayout_SyncErrors"></a> roleeditorlayout_SyncErrors

**Added by**: Role Editor Solution

See the [roleeditorlayout_SyncErrors](roleeditorlayout.md#BKMK_roleeditorlayout_SyncErrors) one-to-many relationship for the [roleeditorlayout](roleeditorlayout.md) table/entity.

### <a name="BKMK_appaction_SyncErrors"></a> appaction_SyncErrors

**Added by**: Power Apps Actions Solution

See the [appaction_SyncErrors](appaction.md#BKMK_appaction_SyncErrors) one-to-many relationship for the [appaction](appaction.md) table/entity.

### <a name="BKMK_appactionmigration_SyncErrors"></a> appactionmigration_SyncErrors

**Added by**: Power Apps Actions Solution

See the [appactionmigration_SyncErrors](appactionmigration.md#BKMK_appactionmigration_SyncErrors) one-to-many relationship for the [appactionmigration](appactionmigration.md) table/entity.

### <a name="BKMK_appactionrule_SyncErrors"></a> appactionrule_SyncErrors

**Added by**: Power Apps Actions Solution

See the [appactionrule_SyncErrors](appactionrule.md#BKMK_appactionrule_SyncErrors) one-to-many relationship for the [appactionrule](appactionrule.md) table/entity.

### <a name="BKMK_card_SyncErrors"></a> card_SyncErrors

**Added by**: Power Apps cards Solution

See the [card_SyncErrors](card.md#BKMK_card_SyncErrors) one-to-many relationship for the [card](card.md) table/entity.

### <a name="BKMK_msdyn_entitylinkchatconfiguration_SyncErrors"></a> msdyn_entitylinkchatconfiguration_SyncErrors

**Added by**: Teams Chat Settings Solution Solution

See the [msdyn_entitylinkchatconfiguration_SyncErrors](msdyn_entitylinkchatconfiguration.md#BKMK_msdyn_entitylinkchatconfiguration_SyncErrors) one-to-many relationship for the [msdyn_entitylinkchatconfiguration](msdyn_entitylinkchatconfiguration.md) table/entity.

### <a name="BKMK_msdyn_richtextfile_SyncErrors"></a> msdyn_richtextfile_SyncErrors

**Added by**: Rich Text Editor Solution

See the [msdyn_richtextfile_SyncErrors](msdyn_richtextfile.md#BKMK_msdyn_richtextfile_SyncErrors) one-to-many relationship for the [msdyn_richtextfile](msdyn_richtextfile.md) table/entity.

### <a name="BKMK_msdyn_customcontrolextendedsettings_SyncErrors"></a> msdyn_customcontrolextendedsettings_SyncErrors

**Added by**: User Experiences Extended Settings Solution

See the [msdyn_customcontrolextendedsettings_SyncErrors](msdyn_customcontrolextendedsettings.md#BKMK_msdyn_customcontrolextendedsettings_SyncErrors) one-to-many relationship for the [msdyn_customcontrolextendedsettings](msdyn_customcontrolextendedsettings.md) table/entity.

### <a name="BKMK_searchrelationshipsettings_SyncErrors"></a> searchrelationshipsettings_SyncErrors

**Added by**: msdyn_RelevanceSearch Solution

See the [searchrelationshipsettings_SyncErrors](searchrelationshipsettings.md#BKMK_searchrelationshipsettings_SyncErrors) one-to-many relationship for the [searchrelationshipsettings](searchrelationshipsettings.md) table/entity.

### <a name="BKMK_msdyn_virtualtablecolumncandidate_SyncErrors"></a> msdyn_virtualtablecolumncandidate_SyncErrors

**Added by**: Virtual Connector Provider Solution

See the [msdyn_virtualtablecolumncandidate_SyncErrors](msdyn_virtualtablecolumncandidate.md#BKMK_msdyn_virtualtablecolumncandidate_SyncErrors) one-to-many relationship for the [msdyn_virtualtablecolumncandidate](msdyn_virtualtablecolumncandidate.md) table/entity.

### <a name="BKMK_msdyn_aiconfiguration_SyncErrors"></a> msdyn_aiconfiguration_SyncErrors

**Added by**: AISolution Solution

See the [msdyn_aiconfiguration_SyncErrors](msdyn_aiconfiguration.md#BKMK_msdyn_aiconfiguration_SyncErrors) one-to-many relationship for the [msdyn_aiconfiguration](msdyn_aiconfiguration.md) table/entity.

### <a name="BKMK_msdyn_aievent_SyncErrors"></a> msdyn_aievent_SyncErrors

**Added by**: AISolution Solution

See the [msdyn_aievent_SyncErrors](msdyn_aievent.md#BKMK_msdyn_aievent_SyncErrors) one-to-many relationship for the [msdyn_aievent](msdyn_aievent.md) table/entity.

### <a name="BKMK_msdyn_aimodel_SyncErrors"></a> msdyn_aimodel_SyncErrors

**Added by**: AISolution Solution

See the [msdyn_aimodel_SyncErrors](msdyn_aimodel.md#BKMK_msdyn_aimodel_SyncErrors) one-to-many relationship for the [msdyn_aimodel](msdyn_aimodel.md) table/entity.

### <a name="BKMK_msdyn_aitemplate_SyncErrors"></a> msdyn_aitemplate_SyncErrors

**Added by**: AISolution Solution

See the [msdyn_aitemplate_SyncErrors](msdyn_aitemplate.md#BKMK_msdyn_aitemplate_SyncErrors) one-to-many relationship for the [msdyn_aitemplate](msdyn_aitemplate.md) table/entity.

### <a name="BKMK_msdyn_aibfeedbackloop_SyncErrors"></a> msdyn_aibfeedbackloop_SyncErrors

**Added by**: AISolutionFullAdditions Solution

See the [msdyn_aibfeedbackloop_SyncErrors](msdyn_aibfeedbackloop.md#BKMK_msdyn_aibfeedbackloop_SyncErrors) one-to-many relationship for the [msdyn_aibfeedbackloop](msdyn_aibfeedbackloop.md) table/entity.

### <a name="BKMK_msdyn_aifptrainingdocument_SyncErrors"></a> msdyn_aifptrainingdocument_SyncErrors

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aifptrainingdocument_SyncErrors](msdyn_aifptrainingdocument.md#BKMK_msdyn_aifptrainingdocument_SyncErrors) one-to-many relationship for the [msdyn_aifptrainingdocument](msdyn_aifptrainingdocument.md) table/entity.

### <a name="BKMK_msdyn_aiodimage_SyncErrors"></a> msdyn_aiodimage_SyncErrors

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodimage_SyncErrors](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_SyncErrors) one-to-many relationship for the [msdyn_aiodimage](msdyn_aiodimage.md) table/entity.

### <a name="BKMK_msdyn_aiodlabel_SyncErrors"></a> msdyn_aiodlabel_SyncErrors

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodlabel_SyncErrors](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_SyncErrors) one-to-many relationship for the [msdyn_aiodlabel](msdyn_aiodlabel.md) table/entity.

### <a name="BKMK_msdyn_aiodtrainingboundingbox_SyncErrors"></a> msdyn_aiodtrainingboundingbox_SyncErrors

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodtrainingboundingbox_SyncErrors](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_SyncErrors) one-to-many relationship for the [msdyn_aiodtrainingboundingbox](msdyn_aiodtrainingboundingbox.md) table/entity.

### <a name="BKMK_msdyn_aiodtrainingimage_SyncErrors"></a> msdyn_aiodtrainingimage_SyncErrors

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodtrainingimage_SyncErrors](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_SyncErrors) one-to-many relationship for the [msdyn_aiodtrainingimage](msdyn_aiodtrainingimage.md) table/entity.

### <a name="BKMK_msdyn_aibdataset_SyncErrors"></a> msdyn_aibdataset_SyncErrors

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdataset_SyncErrors](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_SyncErrors) one-to-many relationship for the [msdyn_aibdataset](msdyn_aibdataset.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetfile_SyncErrors"></a> msdyn_aibdatasetfile_SyncErrors

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetfile_SyncErrors](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_SyncErrors) one-to-many relationship for the [msdyn_aibdatasetfile](msdyn_aibdatasetfile.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetrecord_SyncErrors"></a> msdyn_aibdatasetrecord_SyncErrors

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetrecord_SyncErrors](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_SyncErrors) one-to-many relationship for the [msdyn_aibdatasetrecord](msdyn_aibdatasetrecord.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetscontainer_SyncErrors"></a> msdyn_aibdatasetscontainer_SyncErrors

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetscontainer_SyncErrors](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_SyncErrors) one-to-many relationship for the [msdyn_aibdatasetscontainer](msdyn_aibdatasetscontainer.md) table/entity.

### <a name="BKMK_msdyn_aibfile_SyncErrors"></a> msdyn_aibfile_SyncErrors

**Added by**: AI Solution default templates Solution

See the [msdyn_aibfile_SyncErrors](msdyn_aibfile.md#BKMK_msdyn_aibfile_SyncErrors) one-to-many relationship for the [msdyn_aibfile](msdyn_aibfile.md) table/entity.

### <a name="BKMK_msdyn_aibfileattacheddata_SyncErrors"></a> msdyn_aibfileattacheddata_SyncErrors

**Added by**: AI Solution default templates Solution

See the [msdyn_aibfileattacheddata_SyncErrors](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_SyncErrors) one-to-many relationship for the [msdyn_aibfileattacheddata](msdyn_aibfileattacheddata.md) table/entity.

### <a name="BKMK_msdyn_pmanalysishistory_SyncErrors"></a> msdyn_pmanalysishistory_SyncErrors

**Added by**: Process Mining Solution

See the [msdyn_pmanalysishistory_SyncErrors](msdyn_pmanalysishistory.md#BKMK_msdyn_pmanalysishistory_SyncErrors) one-to-many relationship for the [msdyn_pmanalysishistory](msdyn_pmanalysishistory.md) table/entity.

### <a name="BKMK_msdyn_pmcalendar_SyncErrors"></a> msdyn_pmcalendar_SyncErrors

**Added by**: Process Mining Solution

See the [msdyn_pmcalendar_SyncErrors](msdyn_pmcalendar.md#BKMK_msdyn_pmcalendar_SyncErrors) one-to-many relationship for the [msdyn_pmcalendar](msdyn_pmcalendar.md) table/entity.

### <a name="BKMK_msdyn_pmcalendarversion_SyncErrors"></a> msdyn_pmcalendarversion_SyncErrors

**Added by**: Process Mining Solution

See the [msdyn_pmcalendarversion_SyncErrors](msdyn_pmcalendarversion.md#BKMK_msdyn_pmcalendarversion_SyncErrors) one-to-many relationship for the [msdyn_pmcalendarversion](msdyn_pmcalendarversion.md) table/entity.

### <a name="BKMK_msdyn_pminferredtask_SyncErrors"></a> msdyn_pminferredtask_SyncErrors

**Added by**: Process Mining Solution

See the [msdyn_pminferredtask_SyncErrors](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_SyncErrors) one-to-many relationship for the [msdyn_pminferredtask](msdyn_pminferredtask.md) table/entity.

### <a name="BKMK_msdyn_pmprocessextendedmetadataversion_SyncErrors"></a> msdyn_pmprocessextendedmetadataversion_SyncErrors

**Added by**: Process Mining Solution

See the [msdyn_pmprocessextendedmetadataversion_SyncErrors](msdyn_pmprocessextendedmetadataversion.md#BKMK_msdyn_pmprocessextendedmetadataversion_SyncErrors) one-to-many relationship for the [msdyn_pmprocessextendedmetadataversion](msdyn_pmprocessextendedmetadataversion.md) table/entity.

### <a name="BKMK_msdyn_pmprocesstemplate_SyncErrors"></a> msdyn_pmprocesstemplate_SyncErrors

**Added by**: Process Mining Solution

See the [msdyn_pmprocesstemplate_SyncErrors](msdyn_pmprocesstemplate.md#BKMK_msdyn_pmprocesstemplate_SyncErrors) one-to-many relationship for the [msdyn_pmprocesstemplate](msdyn_pmprocesstemplate.md) table/entity.

### <a name="BKMK_msdyn_pmprocessusersettings_SyncErrors"></a> msdyn_pmprocessusersettings_SyncErrors

**Added by**: Process Mining Solution

See the [msdyn_pmprocessusersettings_SyncErrors](msdyn_pmprocessusersettings.md#BKMK_msdyn_pmprocessusersettings_SyncErrors) one-to-many relationship for the [msdyn_pmprocessusersettings](msdyn_pmprocessusersettings.md) table/entity.

### <a name="BKMK_msdyn_pmprocessversion_SyncErrors"></a> msdyn_pmprocessversion_SyncErrors

**Added by**: Process Mining Solution

See the [msdyn_pmprocessversion_SyncErrors](msdyn_pmprocessversion.md#BKMK_msdyn_pmprocessversion_SyncErrors) one-to-many relationship for the [msdyn_pmprocessversion](msdyn_pmprocessversion.md) table/entity.

### <a name="BKMK_msdyn_pmrecording_SyncErrors"></a> msdyn_pmrecording_SyncErrors

**Added by**: Process Mining Solution

See the [msdyn_pmrecording_SyncErrors](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_SyncErrors) one-to-many relationship for the [msdyn_pmrecording](msdyn_pmrecording.md) table/entity.

### <a name="BKMK_msdyn_pmtemplate_SyncErrors"></a> msdyn_pmtemplate_SyncErrors

**Added by**: Process Mining Solution

See the [msdyn_pmtemplate_SyncErrors](msdyn_pmtemplate.md#BKMK_msdyn_pmtemplate_SyncErrors) one-to-many relationship for the [msdyn_pmtemplate](msdyn_pmtemplate.md) table/entity.

### <a name="BKMK_msdyn_pmview_SyncErrors"></a> msdyn_pmview_SyncErrors

**Added by**: Process Mining Solution

See the [msdyn_pmview_SyncErrors](msdyn_pmview.md#BKMK_msdyn_pmview_SyncErrors) one-to-many relationship for the [msdyn_pmview](msdyn_pmview.md) table/entity.

### <a name="BKMK_msdyn_analysiscomponent_SyncErrors"></a> msdyn_analysiscomponent_SyncErrors

**Added by**: Power Apps Checker Solution

See the [msdyn_analysiscomponent_SyncErrors](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_SyncErrors) one-to-many relationship for the [msdyn_analysiscomponent](msdyn_analysiscomponent.md) table/entity.

### <a name="BKMK_msdyn_analysisjob_SyncErrors"></a> msdyn_analysisjob_SyncErrors

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisjob_SyncErrors](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_SyncErrors) one-to-many relationship for the [msdyn_analysisjob](msdyn_analysisjob.md) table/entity.

### <a name="BKMK_msdyn_analysisoverride_SyncErrors"></a> msdyn_analysisoverride_SyncErrors

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisoverride_SyncErrors](msdyn_analysisoverride.md#BKMK_msdyn_analysisoverride_SyncErrors) one-to-many relationship for the [msdyn_analysisoverride](msdyn_analysisoverride.md) table/entity.

### <a name="BKMK_msdyn_analysisresult_SyncErrors"></a> msdyn_analysisresult_SyncErrors

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisresult_SyncErrors](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_SyncErrors) one-to-many relationship for the [msdyn_analysisresult](msdyn_analysisresult.md) table/entity.

### <a name="BKMK_msdyn_analysisresultdetail_SyncErrors"></a> msdyn_analysisresultdetail_SyncErrors

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisresultdetail_SyncErrors](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_SyncErrors) one-to-many relationship for the [msdyn_analysisresultdetail](msdyn_analysisresultdetail.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthrule_SyncErrors"></a> msdyn_solutionhealthrule_SyncErrors

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthrule_SyncErrors](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_SyncErrors) one-to-many relationship for the [msdyn_solutionhealthrule](msdyn_solutionhealthrule.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthruleargument_SyncErrors"></a> msdyn_solutionhealthruleargument_SyncErrors

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthruleargument_SyncErrors](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_SyncErrors) one-to-many relationship for the [msdyn_solutionhealthruleargument](msdyn_solutionhealthruleargument.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthruleset_SyncErrors"></a> msdyn_solutionhealthruleset_SyncErrors

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthruleset_SyncErrors](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_SyncErrors) one-to-many relationship for the [msdyn_solutionhealthruleset](msdyn_solutionhealthruleset.md) table/entity.

### <a name="BKMK_powerbidataset_SyncErrors"></a> powerbidataset_SyncErrors

**Added by**: Power BI Entities Solution

See the [powerbidataset_SyncErrors](powerbidataset.md#BKMK_powerbidataset_SyncErrors) one-to-many relationship for the [powerbidataset](powerbidataset.md) table/entity.

### <a name="BKMK_powerbimashupparameter_SyncErrors"></a> powerbimashupparameter_SyncErrors

**Added by**: Power BI Entities Solution

See the [powerbimashupparameter_SyncErrors](powerbimashupparameter.md#BKMK_powerbimashupparameter_SyncErrors) one-to-many relationship for the [powerbimashupparameter](powerbimashupparameter.md) table/entity.

### <a name="BKMK_powerbireport_SyncErrors"></a> powerbireport_SyncErrors

**Added by**: Power BI Entities Solution

See the [powerbireport_SyncErrors](powerbireport.md#BKMK_powerbireport_SyncErrors) one-to-many relationship for the [powerbireport](powerbireport.md) table/entity.

### <a name="BKMK_msdyn_fileupload_SyncErrors"></a> msdyn_fileupload_SyncErrors

**Added by**: Smart Data Import Base Solution

See the [msdyn_fileupload_SyncErrors](msdyn_fileupload.md#BKMK_msdyn_fileupload_SyncErrors) one-to-many relationship for the [msdyn_fileupload](msdyn_fileupload.md) table/entity.

### <a name="BKMK_mspcat_catalogsubmissionfiles_SyncErrors"></a> mspcat_catalogsubmissionfiles_SyncErrors

**Added by**: Power Platform Catalog Client Packaging Solution

See the [mspcat_catalogsubmissionfiles_SyncErrors](mspcat_catalogsubmissionfiles.md#BKMK_mspcat_catalogsubmissionfiles_SyncErrors) one-to-many relationship for the [mspcat_catalogsubmissionfiles](mspcat_catalogsubmissionfiles.md) table/entity.

### <a name="BKMK_mspcat_packagestore_SyncErrors"></a> mspcat_packagestore_SyncErrors

**Added by**: Power Platform Catalog Client Packaging Solution

See the [mspcat_packagestore_SyncErrors](mspcat_packagestore.md#BKMK_mspcat_packagestore_SyncErrors) one-to-many relationship for the [mspcat_packagestore](mspcat_packagestore.md) table/entity.

### <a name="BKMK_msdyn_schedule_SyncErrors"></a> msdyn_schedule_SyncErrors

**Added by**: Insights App Platform Solution

See the [msdyn_schedule_SyncErrors](msdyn_schedule.md#BKMK_msdyn_schedule_SyncErrors) one-to-many relationship for the [msdyn_schedule](msdyn_schedule.md) table/entity.

### <a name="BKMK_msdyn_dataflow_datalakefolder_SyncErrors"></a> msdyn_dataflow_datalakefolder_SyncErrors

**Added by**: Insights App Platform Solution

See the [msdyn_dataflow_datalakefolder_SyncErrors](msdyn_dataflow_datalakefolder.md#BKMK_msdyn_dataflow_datalakefolder_SyncErrors) one-to-many relationship for the [msdyn_dataflow_datalakefolder](msdyn_dataflow_datalakefolder.md) table/entity.

### <a name="BKMK_msdyn_dmsrequest_SyncErrors"></a> msdyn_dmsrequest_SyncErrors

**Added by**: Insights App Platform Solution

See the [msdyn_dmsrequest_SyncErrors](msdyn_dmsrequest.md#BKMK_msdyn_dmsrequest_SyncErrors) one-to-many relationship for the [msdyn_dmsrequest](msdyn_dmsrequest.md) table/entity.

### <a name="BKMK_msdyn_dmsrequeststatus_SyncErrors"></a> msdyn_dmsrequeststatus_SyncErrors

**Added by**: Insights App Platform Solution

See the [msdyn_dmsrequeststatus_SyncErrors](msdyn_dmsrequeststatus.md#BKMK_msdyn_dmsrequeststatus_SyncErrors) one-to-many relationship for the [msdyn_dmsrequeststatus](msdyn_dmsrequeststatus.md) table/entity.

### <a name="BKMK_searchattributesettings_SyncErrors"></a> searchattributesettings_SyncErrors

**Added by**: msdyn_RelevanceSearch Solution

See the [searchattributesettings_SyncErrors](searchattributesettings.md#BKMK_searchattributesettings_SyncErrors) one-to-many relationship for the [searchattributesettings](searchattributesettings.md) table/entity.

### <a name="BKMK_searchcustomanalyzer_SyncErrors"></a> searchcustomanalyzer_SyncErrors

**Added by**: msdyn_RelevanceSearch Solution

See the [searchcustomanalyzer_SyncErrors](searchcustomanalyzer.md#BKMK_searchcustomanalyzer_SyncErrors) one-to-many relationship for the [searchcustomanalyzer](searchcustomanalyzer.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.syncerror?text=syncerror EntityType" />