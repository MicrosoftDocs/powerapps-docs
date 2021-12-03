---
title: "ProcessSession table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the ProcessSession table/entity."
ms.date: 10/05/2021
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

# ProcessSession table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Information that is generated when a dialog is run. Every time that you run a dialog, a dialog session is created.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/processsessions(*processsessionid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/processsessions<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/processsessions(*processsessionid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/processsessions(*processsessionid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/processsessions<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/processsessions(*processsessionid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/processsessions(*processsessionid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

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
|Targets|account,activityfileattachment,annotation,appaction,appelement,applicationuser,appmodulecomponentedge,appmodulecomponentnode,appointment,appsetting,appusersetting,bot,botcomponent,businessunit,businessunitnewsarticle,canvasappextendedmetadata,cascadegrantrevokeaccessrecordstracker,cascadegrantrevokeaccessversiontracker,catalog,catalogassignment,channelaccessprofile,channelaccessprofilerule,comment,connection,connectionreference,connectionrole,connector,contact,conversationtranscript,convertrule,customapi,customapirequestparameter,customapiresponseproperty,customeraddress,customerrelationship,datalakefolder,datalakefolderpermission,datalakeworkspace,datalakeworkspacepermission,email,environmentvariabledefinition,environmentvariablevalue,expiredprocess,exportsolutionupload,externalparty,externalpartyitem,fax,featurecontrolsetting,flowmachine,flowmachinegroup,goal,goalrollupquery,holidaywrapper,internalcatalogassignment,kbarticle,kbarticlecomment,kbarticletemplate,keyvaultreference,knowledgearticle,knowledgebaserecord,letter,mailbox,mailmergetemplate,managedidentity,metric,msdynce_botcontent,msdyn_aibdataset,msdyn_aibdatasetfile,msdyn_aibdatasetrecord,msdyn_aibdatasetscontainer,msdyn_aibfile,msdyn_aibfileattacheddata,msdyn_aiconfiguration,msdyn_aifptrainingdocument,msdyn_aimodel,msdyn_aiodimage,msdyn_aiodlabel,msdyn_aiodtrainingboundingbox,msdyn_aiodtrainingimage,msdyn_aitemplate,msdyn_analysiscomponent,msdyn_analysisjob,msdyn_analysisresult,msdyn_analysisresultdetail,msdyn_dataflow,msdyn_federatedarticle,msdyn_federatedarticleincident,msdyn_helppage,msdyn_kalanguagesetting,msdyn_kbattachment,msdyn_kmfederatedsearchconfig,msdyn_kmpersonalizationsetting,msdyn_knowledgearticleimage,msdyn_knowledgearticletemplate,msdyn_knowledgeinteractioninsight,msdyn_knowledgepersonalfilter,msdyn_knowledgesearchfilter,msdyn_knowledgesearchinsight,msdyn_pminferredtask,msdyn_pmrecording,msdyn_richtextfile,msdyn_serviceconfiguration,msdyn_slakpi,msdyn_solutionhealthrule,msdyn_solutionhealthruleargument,msdyn_solutionhealthruleset,msdyn_tour,newprocess,organizationdatasyncsubscription,organizationdatasyncsubscriptionentity,organizationsetting,package,pdfsetting,phonecall,position,processstageparameter,provisionlanguageforuser,queue,queueitem,recurringappointmentmaster,relationshiprole,report,revokeinheritedaccessrecordstracker,rollupfield,routingrule,routingruleitem,serviceplan,serviceplanmapping,settingdefinition,sharepointdocumentlocation,sharepointsite,sla,socialactivity,socialprofile,solutioncomponentattributeconfiguration,solutioncomponentbatchconfiguration,solutioncomponentconfiguration,solutioncomponentrelationshipconfiguration,stagesolutionupload,subject,systemuser,systemuserauthorizationchangetracker,task,team,teammobileofflineprofilemembership,template,territory,theme,transactioncurrency,translationprocess,usermapping,usermobileofflineprofilemembership,virtualentitymetadata,workflowbinary|
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
|MaxLength|800|
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
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


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

Same as workflowlog table [lk_workflowlog_processsession](workflowlog.md#BKMK_lk_workflowlog_processsession) Many-To-One relationship.

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

Same as workflowlog table [lk_workflowlog_processsession_childworkflow](workflowlog.md#BKMK_lk_workflowlog_processsession_childworkflow) Many-To-One relationship.

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

Same as processsession table [lk_processsession_previouslinkedsessionid](processsession.md#BKMK_lk_processsession_previouslinkedsessionid) Many-To-One relationship.

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

Same as processsession table [lk_processsession_nextlinkedsessionid](processsession.md#BKMK_lk_processsession_nextlinkedsessionid) Many-To-One relationship.

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

Same as processsession table [lk_processsession_originatingsessionid](processsession.md#BKMK_lk_processsession_originatingsessionid) Many-To-One relationship.

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

Same as connection table [processsession_connections2](connection.md#BKMK_processsession_connections2) Many-To-One relationship.

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

Same as syncerror table [ProcessSession_SyncErrors](syncerror.md#BKMK_ProcessSession_SyncErrors) Many-To-One relationship.

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

Same as connection table [processsession_connections1](connection.md#BKMK_processsession_connections1) Many-To-One relationship.

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

Same as postfollow table [processsession_PostFollows](postfollow.md#BKMK_processsession_PostFollows) Many-To-One relationship.

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
- [catalog_ProcessSession](#BKMK_catalog_ProcessSession)
- [catalogassignment_ProcessSession](#BKMK_catalogassignment_ProcessSession)
- [customapi_ProcessSession](#BKMK_customapi_ProcessSession)
- [customapirequestparameter_ProcessSession](#BKMK_customapirequestparameter_ProcessSession)
- [customapiresponseproperty_ProcessSession](#BKMK_customapiresponseproperty_ProcessSession)
- [provisionlanguageforuser_ProcessSession](#BKMK_provisionlanguageforuser_ProcessSession)
- [datalakefolder_ProcessSession](#BKMK_datalakefolder_ProcessSession)
- [datalakefolderpermission_ProcessSession](#BKMK_datalakefolderpermission_ProcessSession)
- [datalakeworkspace_ProcessSession](#BKMK_datalakeworkspace_ProcessSession)
- [datalakeworkspacepermission_ProcessSession](#BKMK_datalakeworkspacepermission_ProcessSession)
- [msdyn_dataflow_ProcessSession](#BKMK_msdyn_dataflow_ProcessSession)
- [serviceplan_ProcessSession](#BKMK_serviceplan_ProcessSession)
- [serviceplanmapping_ProcessSession](#BKMK_serviceplanmapping_ProcessSession)
- [applicationuser_ProcessSession](#BKMK_applicationuser_ProcessSession)
- [connector_ProcessSession](#BKMK_connector_ProcessSession)
- [environmentvariabledefinition_ProcessSession](#BKMK_environmentvariabledefinition_ProcessSession)
- [environmentvariablevalue_ProcessSession](#BKMK_environmentvariablevalue_ProcessSession)
- [flowmachine_ProcessSession](#BKMK_flowmachine_ProcessSession)
- [flowmachinegroup_ProcessSession](#BKMK_flowmachinegroup_ProcessSession)
- [processstageparameter_ProcessSession](#BKMK_processstageparameter_ProcessSession)
- [workflowbinary_ProcessSession](#BKMK_workflowbinary_ProcessSession)
- [connectionreference_ProcessSession](#BKMK_connectionreference_ProcessSession)
- [msdyn_aiconfiguration_ProcessSession](#BKMK_msdyn_aiconfiguration_ProcessSession)
- [msdyn_aimodel_ProcessSession](#BKMK_msdyn_aimodel_ProcessSession)
- [msdyn_aitemplate_ProcessSession](#BKMK_msdyn_aitemplate_ProcessSession)
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
- [msdyn_helppage_ProcessSession](#BKMK_msdyn_helppage_ProcessSession)
- [msdyn_tour_ProcessSession](#BKMK_msdyn_tour_ProcessSession)
- [msdynce_botcontent_ProcessSession](#BKMK_msdynce_botcontent_ProcessSession)
- [conversationtranscript_ProcessSession](#BKMK_conversationtranscript_ProcessSession)
- [bot_ProcessSession](#BKMK_bot_ProcessSession)
- [botcomponent_ProcessSession](#BKMK_botcomponent_ProcessSession)
- [Territory_ProcessSessions](#BKMK_Territory_ProcessSessions)
- [activityfileattachment_ProcessSession](#BKMK_activityfileattachment_ProcessSession)
- [msdyn_serviceconfiguration_ProcessSession](#BKMK_msdyn_serviceconfiguration_ProcessSession)
- [msdyn_slakpi_ProcessSession](#BKMK_msdyn_slakpi_ProcessSession)
- [msdyn_federatedarticle_ProcessSession](#BKMK_msdyn_federatedarticle_ProcessSession)
- [msdyn_federatedarticleincident_ProcessSession](#BKMK_msdyn_federatedarticleincident_ProcessSession)
- [msdyn_kmfederatedsearchconfig_ProcessSession](#BKMK_msdyn_kmfederatedsearchconfig_ProcessSession)
- [msdyn_knowledgearticleimage_ProcessSession](#BKMK_msdyn_knowledgearticleimage_ProcessSession)
- [msdyn_knowledgeinteractioninsight_ProcessSession](#BKMK_msdyn_knowledgeinteractioninsight_ProcessSession)
- [msdyn_knowledgesearchinsight_ProcessSession](#BKMK_msdyn_knowledgesearchinsight_ProcessSession)
- [msdyn_kalanguagesetting_ProcessSession](#BKMK_msdyn_kalanguagesetting_ProcessSession)
- [msdyn_kbattachment_ProcessSession](#BKMK_msdyn_kbattachment_ProcessSession)
- [msdyn_kmpersonalizationsetting_ProcessSession](#BKMK_msdyn_kmpersonalizationsetting_ProcessSession)
- [msdyn_knowledgearticletemplate_ProcessSession](#BKMK_msdyn_knowledgearticletemplate_ProcessSession)
- [msdyn_knowledgepersonalfilter_ProcessSession](#BKMK_msdyn_knowledgepersonalfilter_ProcessSession)
- [msdyn_knowledgesearchfilter_ProcessSession](#BKMK_msdyn_knowledgesearchfilter_ProcessSession)
- [keyvaultreference_ProcessSession](#BKMK_keyvaultreference_ProcessSession)
- [managedidentity_ProcessSession](#BKMK_managedidentity_ProcessSession)
- [virtualentitymetadata_ProcessSession](#BKMK_virtualentitymetadata_ProcessSession)
- [organizationdatasyncsubscription_ProcessSession](#BKMK_organizationdatasyncsubscription_ProcessSession)
- [organizationdatasyncsubscriptionentity_ProcessSession](#BKMK_organizationdatasyncsubscriptionentity_ProcessSession)
- [appaction_ProcessSession](#BKMK_appaction_ProcessSession)
- [msdyn_richtextfile_ProcessSession](#BKMK_msdyn_richtextfile_ProcessSession)
- [msdyn_pminferredtask_ProcessSession](#BKMK_msdyn_pminferredtask_ProcessSession)
- [msdyn_pmrecording_ProcessSession](#BKMK_msdyn_pmrecording_ProcessSession)
- [msdyn_analysiscomponent_ProcessSession](#BKMK_msdyn_analysiscomponent_ProcessSession)
- [msdyn_analysisjob_ProcessSession](#BKMK_msdyn_analysisjob_ProcessSession)
- [msdyn_analysisresult_ProcessSession](#BKMK_msdyn_analysisresult_ProcessSession)
- [msdyn_analysisresultdetail_ProcessSession](#BKMK_msdyn_analysisresultdetail_ProcessSession)
- [msdyn_solutionhealthrule_ProcessSession](#BKMK_msdyn_solutionhealthrule_ProcessSession)
- [msdyn_solutionhealthruleargument_ProcessSession](#BKMK_msdyn_solutionhealthruleargument_ProcessSession)
- [msdyn_solutionhealthruleset_ProcessSession](#BKMK_msdyn_solutionhealthruleset_ProcessSession)


### <a name="BKMK_theme_ProcessSession"></a> theme_ProcessSession

See theme Table [theme_ProcessSession](theme.md#BKMK_theme_ProcessSession) One-To-Many relationship.

### <a name="BKMK_usermapping_ProcessSession"></a> usermapping_ProcessSession

See usermapping Table [usermapping_ProcessSession](usermapping.md#BKMK_usermapping_ProcessSession) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_ProcessSession"></a> knowledgearticle_ProcessSession

See knowledgearticle Table [knowledgearticle_ProcessSession](knowledgearticle.md#BKMK_knowledgearticle_ProcessSession) One-To-Many relationship.

### <a name="BKMK_position_ProcessSession"></a> position_ProcessSession

See position Table [position_ProcessSession](position.md#BKMK_position_ProcessSession) One-To-Many relationship.

### <a name="BKMK_KnowledgeBaseRecord_ProcessSession"></a> KnowledgeBaseRecord_ProcessSession

See knowledgebaserecord Table [KnowledgeBaseRecord_ProcessSession](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_ProcessSession) One-To-Many relationship.

### <a name="BKMK_SharePointSite_ProcessSessions"></a> SharePointSite_ProcessSessions

See sharepointsite Table [SharePointSite_ProcessSessions](sharepointsite.md#BKMK_SharePointSite_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_MailMergeTemplate_ProcessSessions"></a> MailMergeTemplate_ProcessSessions

See mailmergetemplate Table [MailMergeTemplate_ProcessSessions](mailmergetemplate.md#BKMK_MailMergeTemplate_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Annotation_ProcessSessions"></a> Annotation_ProcessSessions

See annotation Table [Annotation_ProcessSessions](annotation.md#BKMK_Annotation_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_BusinessUnitNewsArticle_ProcessSessions"></a> BusinessUnitNewsArticle_ProcessSessions

See businessunitnewsarticle Table [BusinessUnitNewsArticle_ProcessSessions](businessunitnewsarticle.md#BKMK_BusinessUnitNewsArticle_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Appointment_ProcessSessions"></a> Appointment_ProcessSessions

See appointment Table [Appointment_ProcessSessions](appointment.md#BKMK_Appointment_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_QueueItem_ProcessSessions"></a> QueueItem_ProcessSessions

See queueitem Table [QueueItem_ProcessSessions](queueitem.md#BKMK_QueueItem_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_lk_processsession_previouslinkedsessionid"></a> lk_processsession_previouslinkedsessionid

See processsession Table [lk_processsession_previouslinkedsessionid](processsession.md#BKMK_lk_processsession_previouslinkedsessionid) One-To-Many relationship.

### <a name="BKMK_lk_processsession_nextlinkedsessionid"></a> lk_processsession_nextlinkedsessionid

See processsession Table [lk_processsession_nextlinkedsessionid](processsession.md#BKMK_lk_processsession_nextlinkedsessionid) One-To-Many relationship.

### <a name="BKMK_lk_processsession_originatingsessionid"></a> lk_processsession_originatingsessionid

See processsession Table [lk_processsession_originatingsessionid](processsession.md#BKMK_lk_processsession_originatingsessionid) One-To-Many relationship.

### <a name="BKMK_Team_ProcessSessions"></a> Team_ProcessSessions

See team Table [Team_ProcessSessions](team.md#BKMK_Team_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Goal_ProcessSessions"></a> Goal_ProcessSessions

See goal Table [Goal_ProcessSessions](goal.md#BKMK_Goal_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_mailbox_processsessions"></a> mailbox_processsessions

See mailbox Table [mailbox_processsessions](mailbox.md#BKMK_mailbox_processsessions) One-To-Many relationship.

### <a name="BKMK_TranslationProcess_ProcessSessions"></a> TranslationProcess_ProcessSessions

See translationprocess Table [TranslationProcess_ProcessSessions](translationprocess.md#BKMK_TranslationProcess_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_SystemUser_ProcessSessions"></a> SystemUser_ProcessSessions

See systemuser Table [SystemUser_ProcessSessions](systemuser.md#BKMK_SystemUser_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_BusinessUnit_ProcessSessions"></a> BusinessUnit_ProcessSessions

See businessunit Table [BusinessUnit_ProcessSessions](businessunit.md#BKMK_BusinessUnit_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_KbArticleComment_ProcessSessions"></a> KbArticleComment_ProcessSessions

See kbarticlecomment Table [KbArticleComment_ProcessSessions](kbarticlecomment.md#BKMK_KbArticleComment_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_lk_processsession_canceledby"></a> lk_processsession_canceledby

See systemuser Table [lk_processsession_canceledby](systemuser.md#BKMK_lk_processsession_canceledby) One-To-Many relationship.

### <a name="BKMK_goalrollupquery_ProcessSessions"></a> goalrollupquery_ProcessSessions

See goalrollupquery Table [goalrollupquery_ProcessSessions](goalrollupquery.md#BKMK_goalrollupquery_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_rollupfield_ProcessSessions"></a> rollupfield_ProcessSessions

See rollupfield Table [rollupfield_ProcessSessions](rollupfield.md#BKMK_rollupfield_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_SharePointDocumentLocation_ProcessSessions"></a> SharePointDocumentLocation_ProcessSessions

See sharepointdocumentlocation Table [SharePointDocumentLocation_ProcessSessions](sharepointdocumentlocation.md#BKMK_SharePointDocumentLocation_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_lk_processsession_startedby"></a> lk_processsession_startedby

See systemuser Table [lk_processsession_startedby](systemuser.md#BKMK_lk_processsession_startedby) One-To-Many relationship.

### <a name="BKMK_Account_ProcessSessions"></a> Account_ProcessSessions

See account Table [Account_ProcessSessions](account.md#BKMK_Account_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_PhoneCall_ProcessSessions"></a> PhoneCall_ProcessSessions

See phonecall Table [PhoneCall_ProcessSessions](phonecall.md#BKMK_PhoneCall_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_slabase_ProcessSessions"></a> slabase_ProcessSessions

See sla Table [slabase_ProcessSessions](sla.md#BKMK_slabase_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_lk_processsession_createdby"></a> lk_processsession_createdby

See systemuser Table [lk_processsession_createdby](systemuser.md#BKMK_lk_processsession_createdby) One-To-Many relationship.

### <a name="BKMK_lk_processsessionbase_modifiedonbehalfby"></a> lk_processsessionbase_modifiedonbehalfby

See systemuser Table [lk_processsessionbase_modifiedonbehalfby](systemuser.md#BKMK_lk_processsessionbase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_Template_ProcessSessions"></a> Template_ProcessSessions

See template Table [Template_ProcessSessions](template.md#BKMK_Template_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_NewProcess_ProcessSessions"></a> NewProcess_ProcessSessions

See newprocess Table [NewProcess_ProcessSessions](newprocess.md#BKMK_NewProcess_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Report_ProcessSessions"></a> Report_ProcessSessions

See report Table [Report_ProcessSessions](report.md#BKMK_Report_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Owning_businessunit_processsessions"></a> Owning_businessunit_processsessions

See businessunit Table [Owning_businessunit_processsessions](businessunit.md#BKMK_Owning_businessunit_processsessions) One-To-Many relationship.

### <a name="BKMK_CustomerAddress_ProcessSessions"></a> CustomerAddress_ProcessSessions

See customeraddress Table [CustomerAddress_ProcessSessions](customeraddress.md#BKMK_CustomerAddress_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Connection_ProcessSessions"></a> Connection_ProcessSessions

See connection Table [Connection_ProcessSessions](connection.md#BKMK_Connection_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_lk_processsession_executedby"></a> lk_processsession_executedby

See systemuser Table [lk_processsession_executedby](systemuser.md#BKMK_lk_processsession_executedby) One-To-Many relationship.

### <a name="BKMK_team_processsession"></a> team_processsession

See team Table [team_processsession](team.md#BKMK_team_processsession) One-To-Many relationship.

### <a name="BKMK_metric_ProcessSessions"></a> metric_ProcessSessions

See metric Table [metric_ProcessSessions](metric.md#BKMK_metric_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_ExpiredProcess_ProcessSessions"></a> ExpiredProcess_ProcessSessions

See expiredprocess Table [ExpiredProcess_ProcessSessions](expiredprocess.md#BKMK_ExpiredProcess_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_KbArticle_ProcessSessions"></a> KbArticle_ProcessSessions

See kbarticle Table [KbArticle_ProcessSessions](kbarticle.md#BKMK_KbArticle_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_SocialActivity_ProcessSessions"></a> SocialActivity_ProcessSessions

See socialactivity Table [SocialActivity_ProcessSessions](socialactivity.md#BKMK_SocialActivity_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Task_ProcessSessions"></a> Task_ProcessSessions

See task Table [Task_ProcessSessions](task.md#BKMK_Task_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_lk_processsession_processid"></a> lk_processsession_processid

See workflow Table [lk_processsession_processid](workflow.md#BKMK_lk_processsession_processid) One-To-Many relationship.

### <a name="BKMK_lk_processsession_modifiedby"></a> lk_processsession_modifiedby

See systemuser Table [lk_processsession_modifiedby](systemuser.md#BKMK_lk_processsession_modifiedby) One-To-Many relationship.

### <a name="BKMK_ConnectionRole_ProcessSessions"></a> ConnectionRole_ProcessSessions

See connectionrole Table [ConnectionRole_ProcessSessions](connectionrole.md#BKMK_ConnectionRole_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_ProcessSessions"></a> TransactionCurrency_ProcessSessions

See transactioncurrency Table [TransactionCurrency_ProcessSessions](transactioncurrency.md#BKMK_TransactionCurrency_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Fax_ProcessSessions"></a> Fax_ProcessSessions

See fax Table [Fax_ProcessSessions](fax.md#BKMK_Fax_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_KbArticleTemplate_ProcessSessions"></a> KbArticleTemplate_ProcessSessions

See kbarticletemplate Table [KbArticleTemplate_ProcessSessions](kbarticletemplate.md#BKMK_KbArticleTemplate_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Letter_ProcessSessions"></a> Letter_ProcessSessions

See letter Table [Letter_ProcessSessions](letter.md#BKMK_Letter_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_RecurringAppointmentMaster_ProcessSessions"></a> RecurringAppointmentMaster_ProcessSessions

See recurringappointmentmaster Table [RecurringAppointmentMaster_ProcessSessions](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Email_ProcessSessions"></a> Email_ProcessSessions

See email Table [Email_ProcessSessions](email.md#BKMK_Email_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_lk_processsession_completedby"></a> lk_processsession_completedby

See systemuser Table [lk_processsession_completedby](systemuser.md#BKMK_lk_processsession_completedby) One-To-Many relationship.

### <a name="BKMK_Contact_ProcessSessions"></a> Contact_ProcessSessions

See contact Table [Contact_ProcessSessions](contact.md#BKMK_Contact_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Queue_ProcessSessions"></a> Queue_ProcessSessions

See queue Table [Queue_ProcessSessions](queue.md#BKMK_Queue_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_lk_processsessionbase_createdonbehalfby"></a> lk_processsessionbase_createdonbehalfby

See systemuser Table [lk_processsessionbase_createdonbehalfby](systemuser.md#BKMK_lk_processsessionbase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_Subject_ProcessSessions"></a> Subject_ProcessSessions

See subject Table [Subject_ProcessSessions](subject.md#BKMK_Subject_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_SocialProfile_ProcessSessions"></a> SocialProfile_ProcessSessions

See socialprofile Table [SocialProfile_ProcessSessions](socialprofile.md#BKMK_SocialProfile_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_solutioncomponentattributeconfiguration_ProcessSession"></a> solutioncomponentattributeconfiguration_ProcessSession

**Added by**: Solution Component Configuration Solution

See solutioncomponentattributeconfiguration Table [solutioncomponentattributeconfiguration_ProcessSession](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_ProcessSession) One-To-Many relationship.

### <a name="BKMK_solutioncomponentbatchconfiguration_ProcessSession"></a> solutioncomponentbatchconfiguration_ProcessSession

**Added by**: Solution Component Configuration Solution

See solutioncomponentbatchconfiguration Table [solutioncomponentbatchconfiguration_ProcessSession](solutioncomponentbatchconfiguration.md#BKMK_solutioncomponentbatchconfiguration_ProcessSession) One-To-Many relationship.

### <a name="BKMK_solutioncomponentconfiguration_ProcessSession"></a> solutioncomponentconfiguration_ProcessSession

**Added by**: Solution Component Configuration Solution

See solutioncomponentconfiguration Table [solutioncomponentconfiguration_ProcessSession](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_ProcessSession) One-To-Many relationship.

### <a name="BKMK_solutioncomponentrelationshipconfiguration_ProcessSession"></a> solutioncomponentrelationshipconfiguration_ProcessSession

**Added by**: Solution Component Configuration Solution

See solutioncomponentrelationshipconfiguration Table [solutioncomponentrelationshipconfiguration_ProcessSession](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_ProcessSession) One-To-Many relationship.

### <a name="BKMK_package_ProcessSession"></a> package_ProcessSession

**Added by**: msdyn_SolutionPackageMapping Solution

See package Table [package_ProcessSession](package.md#BKMK_package_ProcessSession) One-To-Many relationship.

### <a name="BKMK_stagesolutionupload_ProcessSession"></a> stagesolutionupload_ProcessSession

**Added by**: StageSolutionUpload Solution

See stagesolutionupload Table [stagesolutionupload_ProcessSession](stagesolutionupload.md#BKMK_stagesolutionupload_ProcessSession) One-To-Many relationship.

### <a name="BKMK_exportsolutionupload_ProcessSession"></a> exportsolutionupload_ProcessSession

**Added by**: ExportSolutionUpload Solution

See exportsolutionupload Table [exportsolutionupload_ProcessSession](exportsolutionupload.md#BKMK_exportsolutionupload_ProcessSession) One-To-Many relationship.

### <a name="BKMK_featurecontrolsetting_ProcessSession"></a> featurecontrolsetting_ProcessSession

**Added by**: msdyn_FeatureControlSetting Solution

See featurecontrolsetting Table [featurecontrolsetting_ProcessSession](featurecontrolsetting.md#BKMK_featurecontrolsetting_ProcessSession) One-To-Many relationship.

### <a name="BKMK_catalog_ProcessSession"></a> catalog_ProcessSession

**Added by**: CatalogFramework Solution

See catalog Table [catalog_ProcessSession](catalog.md#BKMK_catalog_ProcessSession) One-To-Many relationship.

### <a name="BKMK_catalogassignment_ProcessSession"></a> catalogassignment_ProcessSession

**Added by**: CatalogFramework Solution

See catalogassignment Table [catalogassignment_ProcessSession](catalogassignment.md#BKMK_catalogassignment_ProcessSession) One-To-Many relationship.

### <a name="BKMK_customapi_ProcessSession"></a> customapi_ProcessSession

**Added by**: Custom API Framework Solution

See customapi Table [customapi_ProcessSession](customapi.md#BKMK_customapi_ProcessSession) One-To-Many relationship.

### <a name="BKMK_customapirequestparameter_ProcessSession"></a> customapirequestparameter_ProcessSession

**Added by**: Custom API Framework Solution

See customapirequestparameter Table [customapirequestparameter_ProcessSession](customapirequestparameter.md#BKMK_customapirequestparameter_ProcessSession) One-To-Many relationship.

### <a name="BKMK_customapiresponseproperty_ProcessSession"></a> customapiresponseproperty_ProcessSession

**Added by**: Custom API Framework Solution

See customapiresponseproperty Table [customapiresponseproperty_ProcessSession](customapiresponseproperty.md#BKMK_customapiresponseproperty_ProcessSession) One-To-Many relationship.

### <a name="BKMK_provisionlanguageforuser_ProcessSession"></a> provisionlanguageforuser_ProcessSession

**Added by**: msft_LocalizationExtension Solution

See provisionlanguageforuser Table [provisionlanguageforuser_ProcessSession](provisionlanguageforuser.md#BKMK_provisionlanguageforuser_ProcessSession) One-To-Many relationship.

### <a name="BKMK_datalakefolder_ProcessSession"></a> datalakefolder_ProcessSession

**Added by**: Data lake workspaces Solution

See datalakefolder Table [datalakefolder_ProcessSession](datalakefolder.md#BKMK_datalakefolder_ProcessSession) One-To-Many relationship.

### <a name="BKMK_datalakefolderpermission_ProcessSession"></a> datalakefolderpermission_ProcessSession

**Added by**: Data lake workspaces Solution

See datalakefolderpermission Table [datalakefolderpermission_ProcessSession](datalakefolderpermission.md#BKMK_datalakefolderpermission_ProcessSession) One-To-Many relationship.

### <a name="BKMK_datalakeworkspace_ProcessSession"></a> datalakeworkspace_ProcessSession

**Added by**: Data lake workspaces Solution

See datalakeworkspace Table [datalakeworkspace_ProcessSession](datalakeworkspace.md#BKMK_datalakeworkspace_ProcessSession) One-To-Many relationship.

### <a name="BKMK_datalakeworkspacepermission_ProcessSession"></a> datalakeworkspacepermission_ProcessSession

**Added by**: Data lake workspaces Solution

See datalakeworkspacepermission Table [datalakeworkspacepermission_ProcessSession](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_dataflow_ProcessSession"></a> msdyn_dataflow_ProcessSession

**Added by**: Dataflow Solution Solution

See msdyn_dataflow Table [msdyn_dataflow_ProcessSession](msdyn_dataflow.md#BKMK_msdyn_dataflow_ProcessSession) One-To-Many relationship.

### <a name="BKMK_serviceplan_ProcessSession"></a> serviceplan_ProcessSession

**Added by**: License Enforcement Solution

See serviceplan Table [serviceplan_ProcessSession](serviceplan.md#BKMK_serviceplan_ProcessSession) One-To-Many relationship.

### <a name="BKMK_serviceplanmapping_ProcessSession"></a> serviceplanmapping_ProcessSession

**Added by**: License Enforcement Solution

See serviceplanmapping Table [serviceplanmapping_ProcessSession](serviceplanmapping.md#BKMK_serviceplanmapping_ProcessSession) One-To-Many relationship.

### <a name="BKMK_applicationuser_ProcessSession"></a> applicationuser_ProcessSession

**Added by**: ApplicationUserSolution Solution

See applicationuser Table [applicationuser_ProcessSession](applicationuser.md#BKMK_applicationuser_ProcessSession) One-To-Many relationship.

### <a name="BKMK_connector_ProcessSession"></a> connector_ProcessSession

**Added by**: Power Connector Solution Solution

See connector Table [connector_ProcessSession](connector.md#BKMK_connector_ProcessSession) One-To-Many relationship.

### <a name="BKMK_environmentvariabledefinition_ProcessSession"></a> environmentvariabledefinition_ProcessSession

**Added by**: Environment Variables Solution

See environmentvariabledefinition Table [environmentvariabledefinition_ProcessSession](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_ProcessSession) One-To-Many relationship.

### <a name="BKMK_environmentvariablevalue_ProcessSession"></a> environmentvariablevalue_ProcessSession

**Added by**: Environment Variables Solution

See environmentvariablevalue Table [environmentvariablevalue_ProcessSession](environmentvariablevalue.md#BKMK_environmentvariablevalue_ProcessSession) One-To-Many relationship.

### <a name="BKMK_flowmachine_ProcessSession"></a> flowmachine_ProcessSession

**Added by**: Power Automate Extensions core package Solution

See flowmachine Table [flowmachine_ProcessSession](flowmachine.md#BKMK_flowmachine_ProcessSession) One-To-Many relationship.

### <a name="BKMK_flowmachinegroup_ProcessSession"></a> flowmachinegroup_ProcessSession

**Added by**: Power Automate Extensions core package Solution

See flowmachinegroup Table [flowmachinegroup_ProcessSession](flowmachinegroup.md#BKMK_flowmachinegroup_ProcessSession) One-To-Many relationship.

### <a name="BKMK_processstageparameter_ProcessSession"></a> processstageparameter_ProcessSession

**Added by**: Power Automate Extensions core package Solution

See processstageparameter Table [processstageparameter_ProcessSession](processstageparameter.md#BKMK_processstageparameter_ProcessSession) One-To-Many relationship.

### <a name="BKMK_workflowbinary_ProcessSession"></a> workflowbinary_ProcessSession

**Added by**: Power Automate Extensions core package Solution

See workflowbinary Table [workflowbinary_ProcessSession](workflowbinary.md#BKMK_workflowbinary_ProcessSession) One-To-Many relationship.

### <a name="BKMK_connectionreference_ProcessSession"></a> connectionreference_ProcessSession

**Added by**: Power Platform Connection References Solution

See connectionreference Table [connectionreference_ProcessSession](connectionreference.md#BKMK_connectionreference_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_aiconfiguration_ProcessSession"></a> msdyn_aiconfiguration_ProcessSession

**Added by**: AISolution Solution

See msdyn_aiconfiguration Table [msdyn_aiconfiguration_ProcessSession](msdyn_aiconfiguration.md#BKMK_msdyn_aiconfiguration_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_aimodel_ProcessSession"></a> msdyn_aimodel_ProcessSession

**Added by**: AISolution Solution

See msdyn_aimodel Table [msdyn_aimodel_ProcessSession](msdyn_aimodel.md#BKMK_msdyn_aimodel_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_aitemplate_ProcessSession"></a> msdyn_aitemplate_ProcessSession

**Added by**: AISolution Solution

See msdyn_aitemplate Table [msdyn_aitemplate_ProcessSession](msdyn_aitemplate.md#BKMK_msdyn_aitemplate_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_aifptrainingdocument_ProcessSession"></a> msdyn_aifptrainingdocument_ProcessSession

**Added by**: AI Solution deprecated templates Solution

See msdyn_aifptrainingdocument Table [msdyn_aifptrainingdocument_ProcessSession](msdyn_aifptrainingdocument.md#BKMK_msdyn_aifptrainingdocument_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodimage_ProcessSession"></a> msdyn_aiodimage_ProcessSession

**Added by**: AI Solution deprecated templates Solution

See msdyn_aiodimage Table [msdyn_aiodimage_ProcessSession](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodlabel_ProcessSession"></a> msdyn_aiodlabel_ProcessSession

**Added by**: AI Solution deprecated templates Solution

See msdyn_aiodlabel Table [msdyn_aiodlabel_ProcessSession](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodtrainingboundingbox_ProcessSession"></a> msdyn_aiodtrainingboundingbox_ProcessSession

**Added by**: AI Solution deprecated templates Solution

See msdyn_aiodtrainingboundingbox Table [msdyn_aiodtrainingboundingbox_ProcessSession](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodtrainingimage_ProcessSession"></a> msdyn_aiodtrainingimage_ProcessSession

**Added by**: AI Solution deprecated templates Solution

See msdyn_aiodtrainingimage Table [msdyn_aiodtrainingimage_ProcessSession](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdataset_ProcessSession"></a> msdyn_aibdataset_ProcessSession

**Added by**: AI Solution default templates Solution

See msdyn_aibdataset Table [msdyn_aibdataset_ProcessSession](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdatasetfile_ProcessSession"></a> msdyn_aibdatasetfile_ProcessSession

**Added by**: AI Solution default templates Solution

See msdyn_aibdatasetfile Table [msdyn_aibdatasetfile_ProcessSession](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdatasetrecord_ProcessSession"></a> msdyn_aibdatasetrecord_ProcessSession

**Added by**: AI Solution default templates Solution

See msdyn_aibdatasetrecord Table [msdyn_aibdatasetrecord_ProcessSession](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdatasetscontainer_ProcessSession"></a> msdyn_aibdatasetscontainer_ProcessSession

**Added by**: AI Solution default templates Solution

See msdyn_aibdatasetscontainer Table [msdyn_aibdatasetscontainer_ProcessSession](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_aibfile_ProcessSession"></a> msdyn_aibfile_ProcessSession

**Added by**: AI Solution default templates Solution

See msdyn_aibfile Table [msdyn_aibfile_ProcessSession](msdyn_aibfile.md#BKMK_msdyn_aibfile_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_aibfileattacheddata_ProcessSession"></a> msdyn_aibfileattacheddata_ProcessSession

**Added by**: AI Solution default templates Solution

See msdyn_aibfileattacheddata Table [msdyn_aibfileattacheddata_ProcessSession](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_helppage_ProcessSession"></a> msdyn_helppage_ProcessSession

**Added by**: Contextual Help Solution

See msdyn_helppage Table [msdyn_helppage_ProcessSession](msdyn_helppage.md#BKMK_msdyn_helppage_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_tour_ProcessSession"></a> msdyn_tour_ProcessSession

**Added by**: Contextual Help Solution

See msdyn_tour Table [msdyn_tour_ProcessSession](msdyn_tour.md#BKMK_msdyn_tour_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdynce_botcontent_ProcessSession"></a> msdynce_botcontent_ProcessSession

**Added by**: Customer Care Intelligence Bots Solution

See msdynce_botcontent Table [msdynce_botcontent_ProcessSession](msdynce_botcontent.md#BKMK_msdynce_botcontent_ProcessSession) One-To-Many relationship.

### <a name="BKMK_conversationtranscript_ProcessSession"></a> conversationtranscript_ProcessSession

**Added by**: Power Virtual Agents Common Solution

See conversationtranscript Table [conversationtranscript_ProcessSession](conversationtranscript.md#BKMK_conversationtranscript_ProcessSession) One-To-Many relationship.

### <a name="BKMK_bot_ProcessSession"></a> bot_ProcessSession

**Added by**: Power Virtual Agents Solution

See bot Table [bot_ProcessSession](bot.md#BKMK_bot_ProcessSession) One-To-Many relationship.

### <a name="BKMK_botcomponent_ProcessSession"></a> botcomponent_ProcessSession

**Added by**: Power Virtual Agents Solution

See botcomponent Table [botcomponent_ProcessSession](botcomponent.md#BKMK_botcomponent_ProcessSession) One-To-Many relationship.

### <a name="BKMK_Territory_ProcessSessions"></a> Territory_ProcessSessions

**Added by**: Application Common Solution

See territory Table [Territory_ProcessSessions](territory.md#BKMK_Territory_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_activityfileattachment_ProcessSession"></a> activityfileattachment_ProcessSession

**Added by**: Activities Patch Solution

See activityfileattachment Table [activityfileattachment_ProcessSession](activityfileattachment.md#BKMK_activityfileattachment_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_serviceconfiguration_ProcessSession"></a> msdyn_serviceconfiguration_ProcessSession

**Added by**: Service Level Agreement (SLA) Extension Solution

See msdyn_serviceconfiguration Table [msdyn_serviceconfiguration_ProcessSession](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_slakpi_ProcessSession"></a> msdyn_slakpi_ProcessSession

**Added by**: Service Level Agreement (SLA) Extension Solution

See msdyn_slakpi Table [msdyn_slakpi_ProcessSession](msdyn_slakpi.md#BKMK_msdyn_slakpi_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_federatedarticle_ProcessSession"></a> msdyn_federatedarticle_ProcessSession

**Added by**: Knowledge Management Online Features Solution

See msdyn_federatedarticle Table [msdyn_federatedarticle_ProcessSession](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_federatedarticleincident_ProcessSession"></a> msdyn_federatedarticleincident_ProcessSession

**Added by**: Knowledge Management Online Features Solution

See msdyn_federatedarticleincident Table [msdyn_federatedarticleincident_ProcessSession](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_kmfederatedsearchconfig_ProcessSession"></a> msdyn_kmfederatedsearchconfig_ProcessSession

**Added by**: Knowledge Management Online Features Solution

See msdyn_kmfederatedsearchconfig Table [msdyn_kmfederatedsearchconfig_ProcessSession](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgearticleimage_ProcessSession"></a> msdyn_knowledgearticleimage_ProcessSession

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgearticleimage Table [msdyn_knowledgearticleimage_ProcessSession](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgeinteractioninsight_ProcessSession"></a> msdyn_knowledgeinteractioninsight_ProcessSession

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgeinteractioninsight Table [msdyn_knowledgeinteractioninsight_ProcessSession](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgesearchinsight_ProcessSession"></a> msdyn_knowledgesearchinsight_ProcessSession

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgesearchinsight Table [msdyn_knowledgesearchinsight_ProcessSession](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_kalanguagesetting_ProcessSession"></a> msdyn_kalanguagesetting_ProcessSession

**Added by**: Knowledge Management Features Solution

See msdyn_kalanguagesetting Table [msdyn_kalanguagesetting_ProcessSession](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_kbattachment_ProcessSession"></a> msdyn_kbattachment_ProcessSession

**Added by**: Knowledge Management Features Solution

See msdyn_kbattachment Table [msdyn_kbattachment_ProcessSession](msdyn_kbattachment.md#BKMK_msdyn_kbattachment_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_kmpersonalizationsetting_ProcessSession"></a> msdyn_kmpersonalizationsetting_ProcessSession

**Added by**: Knowledge Management Features Solution

See msdyn_kmpersonalizationsetting Table [msdyn_kmpersonalizationsetting_ProcessSession](msdyn_kmpersonalizationsetting.md#BKMK_msdyn_kmpersonalizationsetting_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgearticletemplate_ProcessSession"></a> msdyn_knowledgearticletemplate_ProcessSession

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgearticletemplate Table [msdyn_knowledgearticletemplate_ProcessSession](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgepersonalfilter_ProcessSession"></a> msdyn_knowledgepersonalfilter_ProcessSession

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgepersonalfilter Table [msdyn_knowledgepersonalfilter_ProcessSession](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgesearchfilter_ProcessSession"></a> msdyn_knowledgesearchfilter_ProcessSession

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgesearchfilter Table [msdyn_knowledgesearchfilter_ProcessSession](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_ProcessSession) One-To-Many relationship.

### <a name="BKMK_keyvaultreference_ProcessSession"></a> keyvaultreference_ProcessSession

**Added by**: ManagedIdentityExtensions Solution

See keyvaultreference Table [keyvaultreference_ProcessSession](keyvaultreference.md#BKMK_keyvaultreference_ProcessSession) One-To-Many relationship.

### <a name="BKMK_managedidentity_ProcessSession"></a> managedidentity_ProcessSession

**Added by**: ManagedIdentityExtensions Solution

See managedidentity Table [managedidentity_ProcessSession](managedidentity.md#BKMK_managedidentity_ProcessSession) One-To-Many relationship.

### <a name="BKMK_virtualentitymetadata_ProcessSession"></a> virtualentitymetadata_ProcessSession

**Added by**: RuntimeIntegration Solution

See virtualentitymetadata Table [virtualentitymetadata_ProcessSession](virtualentitymetadata.md#BKMK_virtualentitymetadata_ProcessSession) One-To-Many relationship.

### <a name="BKMK_organizationdatasyncsubscription_ProcessSession"></a> organizationdatasyncsubscription_ProcessSession

**Added by**: OrganizationDataSyncSolution Solution

See organizationdatasyncsubscription Table [organizationdatasyncsubscription_ProcessSession](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_ProcessSession) One-To-Many relationship.

### <a name="BKMK_organizationdatasyncsubscriptionentity_ProcessSession"></a> organizationdatasyncsubscriptionentity_ProcessSession

**Added by**: OrganizationDataSyncSolution Solution

See organizationdatasyncsubscriptionentity Table [organizationdatasyncsubscriptionentity_ProcessSession](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_ProcessSession) One-To-Many relationship.

### <a name="BKMK_appaction_ProcessSession"></a> appaction_ProcessSession

**Added by**: Power Apps Actions Solution

See appaction Table [appaction_ProcessSession](appaction.md#BKMK_appaction_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_richtextfile_ProcessSession"></a> msdyn_richtextfile_ProcessSession

**Added by**: Rich Text Editor Solution

See msdyn_richtextfile Table [msdyn_richtextfile_ProcessSession](msdyn_richtextfile.md#BKMK_msdyn_richtextfile_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_pminferredtask_ProcessSession"></a> msdyn_pminferredtask_ProcessSession

**Added by**: Process Mining Solution

See msdyn_pminferredtask Table [msdyn_pminferredtask_ProcessSession](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_pmrecording_ProcessSession"></a> msdyn_pmrecording_ProcessSession

**Added by**: Process Mining Solution

See msdyn_pmrecording Table [msdyn_pmrecording_ProcessSession](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_analysiscomponent_ProcessSession"></a> msdyn_analysiscomponent_ProcessSession

**Added by**: Power Apps Checker Solution

See msdyn_analysiscomponent Table [msdyn_analysiscomponent_ProcessSession](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisjob_ProcessSession"></a> msdyn_analysisjob_ProcessSession

**Added by**: Power Apps Checker Solution

See msdyn_analysisjob Table [msdyn_analysisjob_ProcessSession](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisresult_ProcessSession"></a> msdyn_analysisresult_ProcessSession

**Added by**: Power Apps Checker Solution

See msdyn_analysisresult Table [msdyn_analysisresult_ProcessSession](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisresultdetail_ProcessSession"></a> msdyn_analysisresultdetail_ProcessSession

**Added by**: Power Apps Checker Solution

See msdyn_analysisresultdetail Table [msdyn_analysisresultdetail_ProcessSession](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthrule_ProcessSession"></a> msdyn_solutionhealthrule_ProcessSession

**Added by**: Power Apps Checker Solution

See msdyn_solutionhealthrule Table [msdyn_solutionhealthrule_ProcessSession](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthruleargument_ProcessSession"></a> msdyn_solutionhealthruleargument_ProcessSession

**Added by**: Power Apps Checker Solution

See msdyn_solutionhealthruleargument Table [msdyn_solutionhealthruleargument_ProcessSession](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_ProcessSession) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthruleset_ProcessSession"></a> msdyn_solutionhealthruleset_ProcessSession

**Added by**: Power Apps Checker Solution

See msdyn_solutionhealthruleset Table [msdyn_solutionhealthruleset_ProcessSession](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_ProcessSession) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.processsession?text=processsession EntityType" />