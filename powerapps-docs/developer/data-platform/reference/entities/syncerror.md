---
title: "SyncError table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the SyncError table/entity."
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

# SyncError table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Failure reason and other detailed information for a record that failed to sync.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/syncerrors(*syncerrorid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/syncerrors<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/syncerrors(*syncerrorid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/syncerrors(*syncerrorid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/syncerrors<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/syncerrors(*syncerrorid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/syncerrors(*syncerrorid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

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

|Value|Label|
|-----|-----|
|0|Conflict|
|1|Record not found|
|2|Record already exists|
|3|Others|



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
|Targets|account,activityfileattachment,activitymimeattachment,activityparty,annotation,appelement,applicationuser,appmodulecomponentedge,appmodulecomponentnode,appnotification,appointment,appsetting,appusersetting,attachment,attributeimageconfig,bot,botcomponent,businessdatalocalizedlabel,businessunit,canvasappextendedmetadata,cascadegrantrevokeaccessrecordstracker,cascadegrantrevokeaccessversiontracker,catalog,catalogassignment,category,channelaccessprofile,channelaccessprofilerule,channelaccessprofileruleitem,connection,connectionreference,connectionrole,connector,contact,conversationtranscript,customapi,customapirequestparameter,customapiresponseproperty,customeraddress,datalakefolder,datalakefolderpermission,datalakeworkspace,datalakeworkspacepermission,duplicaterule,duplicaterulecondition,email,emailserverprofile,entityanalyticsconfig,entityimageconfig,environmentvariabledefinition,environmentvariablevalue,expiredprocess,exportsolutionupload,externalparty,externalpartyitem,fax,feedback,fieldpermission,fieldsecurityprofile,fileattachment,flowmachine,flowmachinegroup,flowsession,goal,goalrollupquery,holidaywrapper,importmap,internaladdress,internalcatalogassignment,kbarticle,kbarticletemplate,keyvaultreference,knowledgearticle,knowledgearticleviews,knowledgebaserecord,letter,mailbox,mailmergetemplate,managedidentity,metric,msdynce_botcontent,msdyn_aibdataset,msdyn_aibdatasetfile,msdyn_aibdatasetrecord,msdyn_aibdatasetscontainer,msdyn_aibfile,msdyn_aibfileattacheddata,msdyn_aiconfiguration,msdyn_aifptrainingdocument,msdyn_aimodel,msdyn_aiodimage,msdyn_aiodlabel,msdyn_aiodtrainingboundingbox,msdyn_aiodtrainingimage,msdyn_aitemplate,msdyn_analysiscomponent,msdyn_analysisjob,msdyn_analysisresult,msdyn_analysisresultdetail,msdyn_dataflow,msdyn_federatedarticle,msdyn_federatedarticleincident,msdyn_helppage,msdyn_kalanguagesetting,msdyn_kmfederatedsearchconfig,msdyn_kmpersonalizationsetting,msdyn_knowledgearticleimage,msdyn_knowledgearticletemplate,msdyn_knowledgeinteractioninsight,msdyn_knowledgepersonalfilter,msdyn_knowledgesearchfilter,msdyn_knowledgesearchinsight,msdyn_pminferredtask,msdyn_pmrecording,msdyn_richtextfile,msdyn_serviceconfiguration,msdyn_slakpi,msdyn_solutionhealthrule,msdyn_solutionhealthruleargument,msdyn_solutionhealthruleset,newprocess,offlinecommanddefinition,organization,organizationdatasyncsubscription,organizationdatasyncsubscriptionentity,organizationsetting,package,pdfsetting,phonecall,position,postfollow,processsession,processstage,processstageparameter,processtrigger,provisionlanguageforuser,publisher,queue,queueitem,recurringappointmentmaster,relationshipattribute,report,reportcategory,revokeinheritedaccessrecordstracker,role,rollupfield,savedquery,savedqueryvisualization,serviceplan,settingdefinition,sharepointdocumentlocation,sharepointsite,sla,slaitem,slakpiinstance,socialactivity,socialprofile,solution,solutioncomponentattributeconfiguration,solutioncomponentconfiguration,solutioncomponentrelationshipconfiguration,stagesolutionupload,subject,syncerror,systemuser,systemuserauthorizationchangetracker,task,team,teammobileofflineprofilemembership,teamtemplate,template,territory,transactioncurrency,translationprocess,usermobileofflineprofilemembership,userquery,userqueryvisualization,workflow,workflowbinary|
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
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


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

Same as syncerror table [SyncError_SyncErrors](syncerror.md#BKMK_SyncError_SyncErrors) Many-To-One relationship.

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
- [solutioncomponentconfiguration_SyncErrors](#BKMK_solutioncomponentconfiguration_SyncErrors)
- [solutioncomponentrelationshipconfiguration_SyncErrors](#BKMK_solutioncomponentrelationshipconfiguration_SyncErrors)
- [package_SyncErrors](#BKMK_package_SyncErrors)
- [stagesolutionupload_SyncErrors](#BKMK_stagesolutionupload_SyncErrors)
- [exportsolutionupload_SyncErrors](#BKMK_exportsolutionupload_SyncErrors)
- [attributeimageconfig_SyncErrors](#BKMK_attributeimageconfig_SyncErrors)
- [entityimageconfig_SyncErrors](#BKMK_entityimageconfig_SyncErrors)
- [relationshipattribute_SyncErrors](#BKMK_relationshipattribute_SyncErrors)
- [provisionlanguageforuser_SyncErrors](#BKMK_provisionlanguageforuser_SyncErrors)
- [entityanalyticsconfig_SyncErrors](#BKMK_entityanalyticsconfig_SyncErrors)
- [datalakefolder_SyncErrors](#BKMK_datalakefolder_SyncErrors)
- [datalakefolderpermission_SyncErrors](#BKMK_datalakefolderpermission_SyncErrors)
- [datalakeworkspace_SyncErrors](#BKMK_datalakeworkspace_SyncErrors)
- [datalakeworkspacepermission_SyncErrors](#BKMK_datalakeworkspacepermission_SyncErrors)
- [msdyn_dataflow_SyncErrors](#BKMK_msdyn_dataflow_SyncErrors)
- [serviceplan_SyncErrors](#BKMK_serviceplan_SyncErrors)
- [applicationuser_SyncErrors](#BKMK_applicationuser_SyncErrors)
- [connector_SyncErrors](#BKMK_connector_SyncErrors)
- [environmentvariabledefinition_SyncErrors](#BKMK_environmentvariabledefinition_SyncErrors)
- [environmentvariablevalue_SyncErrors](#BKMK_environmentvariablevalue_SyncErrors)
- [flowmachine_SyncErrors](#BKMK_flowmachine_SyncErrors)
- [flowmachinegroup_SyncErrors](#BKMK_flowmachinegroup_SyncErrors)
- [processstageparameter_SyncErrors](#BKMK_processstageparameter_SyncErrors)
- [flowsession_SyncErrors](#BKMK_flowsession_SyncErrors)
- [workflowbinary_SyncErrors](#BKMK_workflowbinary_SyncErrors)
- [connectionreference_SyncErrors](#BKMK_connectionreference_SyncErrors)
- [msdyn_helppage_SyncErrors](#BKMK_msdyn_helppage_SyncErrors)
- [msdynce_botcontent_SyncErrors](#BKMK_msdynce_botcontent_SyncErrors)
- [conversationtranscript_SyncErrors](#BKMK_conversationtranscript_SyncErrors)
- [bot_SyncErrors](#BKMK_bot_SyncErrors)
- [botcomponent_SyncErrors](#BKMK_botcomponent_SyncErrors)
- [Territory_SyncErrors](#BKMK_Territory_SyncErrors)
- [activityfileattachment_SyncErrors](#BKMK_activityfileattachment_SyncErrors)
- [msdyn_serviceconfiguration_SyncErrors](#BKMK_msdyn_serviceconfiguration_SyncErrors)
- [msdyn_slakpi_SyncErrors](#BKMK_msdyn_slakpi_SyncErrors)
- [msdyn_federatedarticle_SyncErrors](#BKMK_msdyn_federatedarticle_SyncErrors)
- [msdyn_federatedarticleincident_SyncErrors](#BKMK_msdyn_federatedarticleincident_SyncErrors)
- [msdyn_kmfederatedsearchconfig_SyncErrors](#BKMK_msdyn_kmfederatedsearchconfig_SyncErrors)
- [msdyn_knowledgearticleimage_SyncErrors](#BKMK_msdyn_knowledgearticleimage_SyncErrors)
- [msdyn_knowledgeinteractioninsight_SyncErrors](#BKMK_msdyn_knowledgeinteractioninsight_SyncErrors)
- [msdyn_knowledgesearchinsight_SyncErrors](#BKMK_msdyn_knowledgesearchinsight_SyncErrors)
- [msdyn_kalanguagesetting_SyncErrors](#BKMK_msdyn_kalanguagesetting_SyncErrors)
- [msdyn_kmpersonalizationsetting_SyncErrors](#BKMK_msdyn_kmpersonalizationsetting_SyncErrors)
- [msdyn_knowledgearticletemplate_SyncErrors](#BKMK_msdyn_knowledgearticletemplate_SyncErrors)
- [msdyn_knowledgepersonalfilter_SyncErrors](#BKMK_msdyn_knowledgepersonalfilter_SyncErrors)
- [msdyn_knowledgesearchfilter_SyncErrors](#BKMK_msdyn_knowledgesearchfilter_SyncErrors)
- [keyvaultreference_SyncErrors](#BKMK_keyvaultreference_SyncErrors)
- [managedidentity_SyncErrors](#BKMK_managedidentity_SyncErrors)
- [catalog_SyncErrors](#BKMK_catalog_SyncErrors)
- [catalogassignment_SyncErrors](#BKMK_catalogassignment_SyncErrors)
- [customapi_SyncErrors](#BKMK_customapi_SyncErrors)
- [customapirequestparameter_SyncErrors](#BKMK_customapirequestparameter_SyncErrors)
- [customapiresponseproperty_SyncErrors](#BKMK_customapiresponseproperty_SyncErrors)
- [organizationdatasyncsubscription_SyncErrors](#BKMK_organizationdatasyncsubscription_SyncErrors)
- [organizationdatasyncsubscriptionentity_SyncErrors](#BKMK_organizationdatasyncsubscriptionentity_SyncErrors)
- [appnotification_SyncErrors](#BKMK_appnotification_SyncErrors)
- [msdyn_richtextfile_SyncErrors](#BKMK_msdyn_richtextfile_SyncErrors)
- [msdyn_aiconfiguration_SyncErrors](#BKMK_msdyn_aiconfiguration_SyncErrors)
- [msdyn_aimodel_SyncErrors](#BKMK_msdyn_aimodel_SyncErrors)
- [msdyn_aitemplate_SyncErrors](#BKMK_msdyn_aitemplate_SyncErrors)
- [msdyn_aibdataset_SyncErrors](#BKMK_msdyn_aibdataset_SyncErrors)
- [msdyn_aibdatasetfile_SyncErrors](#BKMK_msdyn_aibdatasetfile_SyncErrors)
- [msdyn_aibdatasetrecord_SyncErrors](#BKMK_msdyn_aibdatasetrecord_SyncErrors)
- [msdyn_aibdatasetscontainer_SyncErrors](#BKMK_msdyn_aibdatasetscontainer_SyncErrors)
- [msdyn_aibfile_SyncErrors](#BKMK_msdyn_aibfile_SyncErrors)
- [msdyn_aibfileattacheddata_SyncErrors](#BKMK_msdyn_aibfileattacheddata_SyncErrors)
- [msdyn_aifptrainingdocument_SyncErrors](#BKMK_msdyn_aifptrainingdocument_SyncErrors)
- [msdyn_aiodimage_SyncErrors](#BKMK_msdyn_aiodimage_SyncErrors)
- [msdyn_aiodlabel_SyncErrors](#BKMK_msdyn_aiodlabel_SyncErrors)
- [msdyn_aiodtrainingboundingbox_SyncErrors](#BKMK_msdyn_aiodtrainingboundingbox_SyncErrors)
- [msdyn_aiodtrainingimage_SyncErrors](#BKMK_msdyn_aiodtrainingimage_SyncErrors)
- [msdyn_pminferredtask_SyncErrors](#BKMK_msdyn_pminferredtask_SyncErrors)
- [msdyn_pmrecording_SyncErrors](#BKMK_msdyn_pmrecording_SyncErrors)
- [msdyn_analysiscomponent_SyncErrors](#BKMK_msdyn_analysiscomponent_SyncErrors)
- [msdyn_analysisjob_SyncErrors](#BKMK_msdyn_analysisjob_SyncErrors)
- [msdyn_analysisresult_SyncErrors](#BKMK_msdyn_analysisresult_SyncErrors)
- [msdyn_analysisresultdetail_SyncErrors](#BKMK_msdyn_analysisresultdetail_SyncErrors)
- [msdyn_solutionhealthrule_SyncErrors](#BKMK_msdyn_solutionhealthrule_SyncErrors)
- [msdyn_solutionhealthruleargument_SyncErrors](#BKMK_msdyn_solutionhealthruleargument_SyncErrors)
- [msdyn_solutionhealthruleset_SyncErrors](#BKMK_msdyn_solutionhealthruleset_SyncErrors)


### <a name="BKMK_KnowledgeBaseRecord_SyncErrors"></a> KnowledgeBaseRecord_SyncErrors

See knowledgebaserecord Table [KnowledgeBaseRecord_SyncErrors](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SocialProfile_SyncErrors"></a> SocialProfile_SyncErrors

See socialprofile Table [SocialProfile_SyncErrors](socialprofile.md#BKMK_SocialProfile_SyncErrors) One-To-Many relationship.

### <a name="BKMK_QueueItem_SyncErrors"></a> QueueItem_SyncErrors

See queueitem Table [QueueItem_SyncErrors](queueitem.md#BKMK_QueueItem_SyncErrors) One-To-Many relationship.

### <a name="BKMK_PostFollow_SyncErrors"></a> PostFollow_SyncErrors

See postfollow Table [PostFollow_SyncErrors](postfollow.md#BKMK_PostFollow_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SharePointSite_SyncErrors"></a> SharePointSite_SyncErrors

See sharepointsite Table [SharePointSite_SyncErrors](sharepointsite.md#BKMK_SharePointSite_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Goal_SyncErrors"></a> Goal_SyncErrors

See goal Table [Goal_SyncErrors](goal.md#BKMK_Goal_SyncErrors) One-To-Many relationship.

### <a name="BKMK_lk_syncerrorbase_createdby"></a> lk_syncerrorbase_createdby

See systemuser Table [lk_syncerrorbase_createdby](systemuser.md#BKMK_lk_syncerrorbase_createdby) One-To-Many relationship.

### <a name="BKMK_TranslationProcess_SyncErrors"></a> TranslationProcess_SyncErrors

See translationprocess Table [TranslationProcess_SyncErrors](translationprocess.md#BKMK_TranslationProcess_SyncErrors) One-To-Many relationship.

### <a name="BKMK_PhoneCall_SyncErrors"></a> PhoneCall_SyncErrors

See phonecall Table [PhoneCall_SyncErrors](phonecall.md#BKMK_PhoneCall_SyncErrors) One-To-Many relationship.

### <a name="BKMK_RecurringAppointmentMaster_SyncErrors"></a> RecurringAppointmentMaster_SyncErrors

See recurringappointmentmaster Table [RecurringAppointmentMaster_SyncErrors](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Publisher_SyncErrors"></a> Publisher_SyncErrors

See publisher Table [Publisher_SyncErrors](publisher.md#BKMK_Publisher_SyncErrors) One-To-Many relationship.

### <a name="BKMK_DuplicateRule_SyncErrors"></a> DuplicateRule_SyncErrors

See duplicaterule Table [DuplicateRule_SyncErrors](duplicaterule.md#BKMK_DuplicateRule_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Subject_SyncErrors"></a> Subject_SyncErrors

See subject Table [Subject_SyncErrors](subject.md#BKMK_Subject_SyncErrors) One-To-Many relationship.

### <a name="BKMK_UserQuery_SyncErrors"></a> UserQuery_SyncErrors

See userquery Table [UserQuery_SyncErrors](userquery.md#BKMK_UserQuery_SyncErrors) One-To-Many relationship.

### <a name="BKMK_MailMergeTemplate_SyncErrors"></a> MailMergeTemplate_SyncErrors

See mailmergetemplate Table [MailMergeTemplate_SyncErrors](mailmergetemplate.md#BKMK_MailMergeTemplate_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SyncError_SyncErrors"></a> SyncError_SyncErrors

See syncerror Table [SyncError_SyncErrors](syncerror.md#BKMK_SyncError_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SavedQuery_SyncErrors"></a> SavedQuery_SyncErrors

See savedquery Table [SavedQuery_SyncErrors](savedquery.md#BKMK_SavedQuery_SyncErrors) One-To-Many relationship.

### <a name="BKMK_lk_syncerrorbase_modifiedby"></a> lk_syncerrorbase_modifiedby

See systemuser Table [lk_syncerrorbase_modifiedby](systemuser.md#BKMK_lk_syncerrorbase_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_syncerrorbase_modifiedonbehalfby"></a> lk_syncerrorbase_modifiedonbehalfby

See systemuser Table [lk_syncerrorbase_modifiedonbehalfby](systemuser.md#BKMK_lk_syncerrorbase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_SyncErrors"></a> TransactionCurrency_SyncErrors

See transactioncurrency Table [TransactionCurrency_SyncErrors](transactioncurrency.md#BKMK_TransactionCurrency_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SocialActivity_SyncErrors"></a> SocialActivity_SyncErrors

See socialactivity Table [SocialActivity_SyncErrors](socialactivity.md#BKMK_SocialActivity_SyncErrors) One-To-Many relationship.

### <a name="BKMK_CustomerAddress_SyncErrors"></a> CustomerAddress_SyncErrors

See customeraddress Table [CustomerAddress_SyncErrors](customeraddress.md#BKMK_CustomerAddress_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Solution_SyncErrors"></a> Solution_SyncErrors

See solution Table [Solution_SyncErrors](solution.md#BKMK_Solution_SyncErrors) One-To-Many relationship.

### <a name="BKMK_team_SyncError"></a> team_SyncError

See team Table [team_SyncError](team.md#BKMK_team_SyncError) One-To-Many relationship.

### <a name="BKMK_TeamTemplate_SyncErrors"></a> TeamTemplate_SyncErrors

See teamtemplate Table [TeamTemplate_SyncErrors](teamtemplate.md#BKMK_TeamTemplate_SyncErrors) One-To-Many relationship.

### <a name="BKMK_ReportCategory_SyncErrors"></a> ReportCategory_SyncErrors

See reportcategory Table [ReportCategory_SyncErrors](reportcategory.md#BKMK_ReportCategory_SyncErrors) One-To-Many relationship.

### <a name="BKMK_lk_syncerrorbase_createdonbehalfby"></a> lk_syncerrorbase_createdonbehalfby

See systemuser Table [lk_syncerrorbase_createdonbehalfby](systemuser.md#BKMK_lk_syncerrorbase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_KbArticle_SyncErrors"></a> KbArticle_SyncErrors

See kbarticle Table [KbArticle_SyncErrors](kbarticle.md#BKMK_KbArticle_SyncErrors) One-To-Many relationship.

### <a name="BKMK_RollupField_SyncErrors"></a> RollupField_SyncErrors

See rollupfield Table [RollupField_SyncErrors](rollupfield.md#BKMK_RollupField_SyncErrors) One-To-Many relationship.

### <a name="BKMK_KbArticleTemplate_SyncErrors"></a> KbArticleTemplate_SyncErrors

See kbarticletemplate Table [KbArticleTemplate_SyncErrors](kbarticletemplate.md#BKMK_KbArticleTemplate_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Account_SyncErrors"></a> Account_SyncErrors

See account Table [Account_SyncErrors](account.md#BKMK_Account_SyncErrors) One-To-Many relationship.

### <a name="BKMK_FieldSecurityProfile_SyncErrors"></a> FieldSecurityProfile_SyncErrors

See fieldsecurityprofile Table [FieldSecurityProfile_SyncErrors](fieldsecurityprofile.md#BKMK_FieldSecurityProfile_SyncErrors) One-To-Many relationship.

### <a name="BKMK_UserQueryVisualization_SyncErrors"></a> UserQueryVisualization_SyncErrors

See userqueryvisualization Table [UserQueryVisualization_SyncErrors](userqueryvisualization.md#BKMK_UserQueryVisualization_SyncErrors) One-To-Many relationship.

### <a name="BKMK_FieldPermission_SyncErrors"></a> FieldPermission_SyncErrors

See fieldpermission Table [FieldPermission_SyncErrors](fieldpermission.md#BKMK_FieldPermission_SyncErrors) One-To-Many relationship.

### <a name="BKMK_DuplicateRuleCondition_SyncErrors"></a> DuplicateRuleCondition_SyncErrors

See duplicaterulecondition Table [DuplicateRuleCondition_SyncErrors](duplicaterulecondition.md#BKMK_DuplicateRuleCondition_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Team_SyncErrors"></a> Team_SyncErrors

See team Table [Team_SyncErrors](team.md#BKMK_Team_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SLAItem_SyncErrors"></a> SLAItem_SyncErrors

See slaitem Table [SLAItem_SyncErrors](slaitem.md#BKMK_SLAItem_SyncErrors) One-To-Many relationship.

### <a name="BKMK_KnowledgeArticleViews_SyncErrors"></a> KnowledgeArticleViews_SyncErrors

See knowledgearticleviews Table [KnowledgeArticleViews_SyncErrors](knowledgearticleviews.md#BKMK_KnowledgeArticleViews_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Appointment_SyncErrors"></a> Appointment_SyncErrors

See appointment Table [Appointment_SyncErrors](appointment.md#BKMK_Appointment_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SystemUser_SyncError"></a> SystemUser_SyncError

See systemuser Table [SystemUser_SyncError](systemuser.md#BKMK_SystemUser_SyncError) One-To-Many relationship.

### <a name="BKMK_Contact_SyncErrors"></a> Contact_SyncErrors

See contact Table [Contact_SyncErrors](contact.md#BKMK_Contact_SyncErrors) One-To-Many relationship.

### <a name="BKMK_ExpiredProcess_SyncErrors"></a> ExpiredProcess_SyncErrors

See expiredprocess Table [ExpiredProcess_SyncErrors](expiredprocess.md#BKMK_ExpiredProcess_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Workflow_SyncErrors"></a> Workflow_SyncErrors

See workflow Table [Workflow_SyncErrors](workflow.md#BKMK_Workflow_SyncErrors) One-To-Many relationship.

### <a name="BKMK_NewProcess_SyncErrors"></a> NewProcess_SyncErrors

See newprocess Table [NewProcess_SyncErrors](newprocess.md#BKMK_NewProcess_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Feedback_SyncErrors"></a> Feedback_SyncErrors

See feedback Table [Feedback_SyncErrors](feedback.md#BKMK_Feedback_SyncErrors) One-To-Many relationship.

### <a name="BKMK_ActivityParty_SyncErrors"></a> ActivityParty_SyncErrors

See activityparty Table [ActivityParty_SyncErrors](activityparty.md#BKMK_ActivityParty_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Annotation_SyncErrors"></a> Annotation_SyncErrors

See annotation Table [Annotation_SyncErrors](annotation.md#BKMK_Annotation_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Email_SyncErrors"></a> Email_SyncErrors

See email Table [Email_SyncErrors](email.md#BKMK_Email_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Organization_SyncErrors"></a> Organization_SyncErrors

See organization Table [Organization_SyncErrors](organization.md#BKMK_Organization_SyncErrors) One-To-Many relationship.

### <a name="BKMK_ActivityMimeAttachment_SyncErrors"></a> ActivityMimeAttachment_SyncErrors

See activitymimeattachment Table [ActivityMimeAttachment_SyncErrors](activitymimeattachment.md#BKMK_ActivityMimeAttachment_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Task_SyncErrors"></a> Task_SyncErrors

See task Table [Task_SyncErrors](task.md#BKMK_Task_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Letter_SyncErrors"></a> Letter_SyncErrors

See letter Table [Letter_SyncErrors](letter.md#BKMK_Letter_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Template_SyncErrors"></a> Template_SyncErrors

See template Table [Template_SyncErrors](template.md#BKMK_Template_SyncErrors) One-To-Many relationship.

### <a name="BKMK_ProcessStage_SyncErrors"></a> ProcessStage_SyncErrors

See processstage Table [ProcessStage_SyncErrors](processstage.md#BKMK_ProcessStage_SyncErrors) One-To-Many relationship.

### <a name="BKMK_KnowledgeArticle_SyncErrors"></a> KnowledgeArticle_SyncErrors

See knowledgearticle Table [KnowledgeArticle_SyncErrors](knowledgearticle.md#BKMK_KnowledgeArticle_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Position_SyncErrors"></a> Position_SyncErrors

See position Table [Position_SyncErrors](position.md#BKMK_Position_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SharePointDocumentLocation_SyncErrors"></a> SharePointDocumentLocation_SyncErrors

See sharepointdocumentlocation Table [SharePointDocumentLocation_SyncErrors](sharepointdocumentlocation.md#BKMK_SharePointDocumentLocation_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Report_SyncErrors"></a> Report_SyncErrors

See report Table [Report_SyncErrors](report.md#BKMK_Report_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Connection_SyncErrors"></a> Connection_SyncErrors

See connection Table [Connection_SyncErrors](connection.md#BKMK_Connection_SyncErrors) One-To-Many relationship.

### <a name="BKMK_ProcessSession_SyncErrors"></a> ProcessSession_SyncErrors

See processsession Table [ProcessSession_SyncErrors](processsession.md#BKMK_ProcessSession_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Category_SyncErrors"></a> Category_SyncErrors

See category Table [Category_SyncErrors](category.md#BKMK_Category_SyncErrors) One-To-Many relationship.

### <a name="BKMK_ConnectionRole_SyncErrors"></a> ConnectionRole_SyncErrors

See connectionrole Table [ConnectionRole_SyncErrors](connectionrole.md#BKMK_ConnectionRole_SyncErrors) One-To-Many relationship.

### <a name="BKMK_ProcessTrigger_SyncErrors"></a> ProcessTrigger_SyncErrors

See processtrigger Table [ProcessTrigger_SyncErrors](processtrigger.md#BKMK_ProcessTrigger_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Fax_SyncErrors"></a> Fax_SyncErrors

See fax Table [Fax_SyncErrors](fax.md#BKMK_Fax_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Mailbox_SyncErrors"></a> Mailbox_SyncErrors

See mailbox Table [Mailbox_SyncErrors](mailbox.md#BKMK_Mailbox_SyncErrors) One-To-Many relationship.

### <a name="BKMK_BusinessUnit_SyncErrors"></a> BusinessUnit_SyncErrors

See businessunit Table [BusinessUnit_SyncErrors](businessunit.md#BKMK_BusinessUnit_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Queue_SyncErrors"></a> Queue_SyncErrors

See queue Table [Queue_SyncErrors](queue.md#BKMK_Queue_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Role_SyncErrors"></a> Role_SyncErrors

See role Table [Role_SyncErrors](role.md#BKMK_Role_SyncErrors) One-To-Many relationship.

### <a name="BKMK_BusinessUnit_SyncError"></a> BusinessUnit_SyncError

See businessunit Table [BusinessUnit_SyncError](businessunit.md#BKMK_BusinessUnit_SyncError) One-To-Many relationship.

### <a name="BKMK_SystemUser_SyncErrors"></a> SystemUser_SyncErrors

See systemuser Table [SystemUser_SyncErrors](systemuser.md#BKMK_SystemUser_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SLAKPIInstance_SyncErrors"></a> SLAKPIInstance_SyncErrors

See slakpiinstance Table [SLAKPIInstance_SyncErrors](slakpiinstance.md#BKMK_SLAKPIInstance_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SLA_SyncErrors"></a> SLA_SyncErrors

See sla Table [SLA_SyncErrors](sla.md#BKMK_SLA_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SavedQueryVisualization_SyncErrors"></a> SavedQueryVisualization_SyncErrors

See savedqueryvisualization Table [SavedQueryVisualization_SyncErrors](savedqueryvisualization.md#BKMK_SavedQueryVisualization_SyncErrors) One-To-Many relationship.

### <a name="BKMK_GoalRollupQuery_SyncErrors"></a> GoalRollupQuery_SyncErrors

See goalrollupquery Table [GoalRollupQuery_SyncErrors](goalrollupquery.md#BKMK_GoalRollupQuery_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Metric_SyncErrors"></a> Metric_SyncErrors

See metric Table [Metric_SyncErrors](metric.md#BKMK_Metric_SyncErrors) One-To-Many relationship.

### <a name="BKMK_ImportMap_SyncErrors"></a> ImportMap_SyncErrors

See importmap Table [ImportMap_SyncErrors](importmap.md#BKMK_ImportMap_SyncErrors) One-To-Many relationship.

### <a name="BKMK_EmailServerProfile_SyncErrors"></a> EmailServerProfile_SyncErrors

See emailserverprofile Table [EmailServerProfile_SyncErrors](emailserverprofile.md#BKMK_EmailServerProfile_SyncErrors) One-To-Many relationship.

### <a name="BKMK_solutioncomponentattributeconfiguration_SyncErrors"></a> solutioncomponentattributeconfiguration_SyncErrors

**Added by**: Solution Component Configuration Solution

See solutioncomponentattributeconfiguration Table [solutioncomponentattributeconfiguration_SyncErrors](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_SyncErrors) One-To-Many relationship.

### <a name="BKMK_solutioncomponentconfiguration_SyncErrors"></a> solutioncomponentconfiguration_SyncErrors

**Added by**: Solution Component Configuration Solution

See solutioncomponentconfiguration Table [solutioncomponentconfiguration_SyncErrors](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_SyncErrors) One-To-Many relationship.

### <a name="BKMK_solutioncomponentrelationshipconfiguration_SyncErrors"></a> solutioncomponentrelationshipconfiguration_SyncErrors

**Added by**: Solution Component Configuration Solution

See solutioncomponentrelationshipconfiguration Table [solutioncomponentrelationshipconfiguration_SyncErrors](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_SyncErrors) One-To-Many relationship.

### <a name="BKMK_package_SyncErrors"></a> package_SyncErrors

**Added by**: msdyn_SolutionPackageMapping Solution

See package Table [package_SyncErrors](package.md#BKMK_package_SyncErrors) One-To-Many relationship.

### <a name="BKMK_stagesolutionupload_SyncErrors"></a> stagesolutionupload_SyncErrors

**Added by**: StageSolutionUpload Solution

See stagesolutionupload Table [stagesolutionupload_SyncErrors](stagesolutionupload.md#BKMK_stagesolutionupload_SyncErrors) One-To-Many relationship.

### <a name="BKMK_exportsolutionupload_SyncErrors"></a> exportsolutionupload_SyncErrors

**Added by**: ExportSolutionUpload Solution

See exportsolutionupload Table [exportsolutionupload_SyncErrors](exportsolutionupload.md#BKMK_exportsolutionupload_SyncErrors) One-To-Many relationship.

### <a name="BKMK_attributeimageconfig_SyncErrors"></a> attributeimageconfig_SyncErrors

**Added by**: Image Configuration Solution

See attributeimageconfig Table [attributeimageconfig_SyncErrors](attributeimageconfig.md#BKMK_attributeimageconfig_SyncErrors) One-To-Many relationship.

### <a name="BKMK_entityimageconfig_SyncErrors"></a> entityimageconfig_SyncErrors

**Added by**: Image Configuration Solution

See entityimageconfig Table [entityimageconfig_SyncErrors](entityimageconfig.md#BKMK_entityimageconfig_SyncErrors) One-To-Many relationship.

### <a name="BKMK_relationshipattribute_SyncErrors"></a> relationshipattribute_SyncErrors

**Added by**: Metadata Extension Solution

See relationshipattribute Table [relationshipattribute_SyncErrors](relationshipattribute.md#BKMK_relationshipattribute_SyncErrors) One-To-Many relationship.

### <a name="BKMK_provisionlanguageforuser_SyncErrors"></a> provisionlanguageforuser_SyncErrors

**Added by**: msft_LocalizationExtension Solution

See provisionlanguageforuser Table [provisionlanguageforuser_SyncErrors](provisionlanguageforuser.md#BKMK_provisionlanguageforuser_SyncErrors) One-To-Many relationship.

### <a name="BKMK_entityanalyticsconfig_SyncErrors"></a> entityanalyticsconfig_SyncErrors

**Added by**: Advanced Analytics Infrastructure Solution

See entityanalyticsconfig Table [entityanalyticsconfig_SyncErrors](entityanalyticsconfig.md#BKMK_entityanalyticsconfig_SyncErrors) One-To-Many relationship.

### <a name="BKMK_datalakefolder_SyncErrors"></a> datalakefolder_SyncErrors

**Added by**: Data lake workspaces Solution

See datalakefolder Table [datalakefolder_SyncErrors](datalakefolder.md#BKMK_datalakefolder_SyncErrors) One-To-Many relationship.

### <a name="BKMK_datalakefolderpermission_SyncErrors"></a> datalakefolderpermission_SyncErrors

**Added by**: Data lake workspaces Solution

See datalakefolderpermission Table [datalakefolderpermission_SyncErrors](datalakefolderpermission.md#BKMK_datalakefolderpermission_SyncErrors) One-To-Many relationship.

### <a name="BKMK_datalakeworkspace_SyncErrors"></a> datalakeworkspace_SyncErrors

**Added by**: Data lake workspaces Solution

See datalakeworkspace Table [datalakeworkspace_SyncErrors](datalakeworkspace.md#BKMK_datalakeworkspace_SyncErrors) One-To-Many relationship.

### <a name="BKMK_datalakeworkspacepermission_SyncErrors"></a> datalakeworkspacepermission_SyncErrors

**Added by**: Data lake workspaces Solution

See datalakeworkspacepermission Table [datalakeworkspacepermission_SyncErrors](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_dataflow_SyncErrors"></a> msdyn_dataflow_SyncErrors

**Added by**: Dataflow Solution Solution

See msdyn_dataflow Table [msdyn_dataflow_SyncErrors](msdyn_dataflow.md#BKMK_msdyn_dataflow_SyncErrors) One-To-Many relationship.

### <a name="BKMK_serviceplan_SyncErrors"></a> serviceplan_SyncErrors

**Added by**: License Enforcement Solution

See serviceplan Table [serviceplan_SyncErrors](serviceplan.md#BKMK_serviceplan_SyncErrors) One-To-Many relationship.

### <a name="BKMK_applicationuser_SyncErrors"></a> applicationuser_SyncErrors

**Added by**: ApplicationUserSolution Solution

See applicationuser Table [applicationuser_SyncErrors](applicationuser.md#BKMK_applicationuser_SyncErrors) One-To-Many relationship.

### <a name="BKMK_connector_SyncErrors"></a> connector_SyncErrors

**Added by**: Power Connector Solution Solution

See connector Table [connector_SyncErrors](connector.md#BKMK_connector_SyncErrors) One-To-Many relationship.

### <a name="BKMK_environmentvariabledefinition_SyncErrors"></a> environmentvariabledefinition_SyncErrors

**Added by**: Environment Variables Solution

See environmentvariabledefinition Table [environmentvariabledefinition_SyncErrors](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_SyncErrors) One-To-Many relationship.

### <a name="BKMK_environmentvariablevalue_SyncErrors"></a> environmentvariablevalue_SyncErrors

**Added by**: Environment Variables Solution

See environmentvariablevalue Table [environmentvariablevalue_SyncErrors](environmentvariablevalue.md#BKMK_environmentvariablevalue_SyncErrors) One-To-Many relationship.

### <a name="BKMK_flowmachine_SyncErrors"></a> flowmachine_SyncErrors

**Added by**: Power Automate Extensions core package Solution

See flowmachine Table [flowmachine_SyncErrors](flowmachine.md#BKMK_flowmachine_SyncErrors) One-To-Many relationship.

### <a name="BKMK_flowmachinegroup_SyncErrors"></a> flowmachinegroup_SyncErrors

**Added by**: Power Automate Extensions core package Solution

See flowmachinegroup Table [flowmachinegroup_SyncErrors](flowmachinegroup.md#BKMK_flowmachinegroup_SyncErrors) One-To-Many relationship.

### <a name="BKMK_processstageparameter_SyncErrors"></a> processstageparameter_SyncErrors

**Added by**: Power Automate Extensions core package Solution

See processstageparameter Table [processstageparameter_SyncErrors](processstageparameter.md#BKMK_processstageparameter_SyncErrors) One-To-Many relationship.

### <a name="BKMK_flowsession_SyncErrors"></a> flowsession_SyncErrors

**Added by**: Power Automate Extensions core package Solution

See flowsession Table [flowsession_SyncErrors](flowsession.md#BKMK_flowsession_SyncErrors) One-To-Many relationship.

### <a name="BKMK_workflowbinary_SyncErrors"></a> workflowbinary_SyncErrors

**Added by**: Power Automate Extensions core package Solution

See workflowbinary Table [workflowbinary_SyncErrors](workflowbinary.md#BKMK_workflowbinary_SyncErrors) One-To-Many relationship.

### <a name="BKMK_connectionreference_SyncErrors"></a> connectionreference_SyncErrors

**Added by**: Power Platform Connection References Solution

See connectionreference Table [connectionreference_SyncErrors](connectionreference.md#BKMK_connectionreference_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_helppage_SyncErrors"></a> msdyn_helppage_SyncErrors

**Added by**: Contextual Help Solution

See msdyn_helppage Table [msdyn_helppage_SyncErrors](msdyn_helppage.md#BKMK_msdyn_helppage_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdynce_botcontent_SyncErrors"></a> msdynce_botcontent_SyncErrors

**Added by**: Customer Care Intelligence Bots Solution

See msdynce_botcontent Table [msdynce_botcontent_SyncErrors](msdynce_botcontent.md#BKMK_msdynce_botcontent_SyncErrors) One-To-Many relationship.

### <a name="BKMK_conversationtranscript_SyncErrors"></a> conversationtranscript_SyncErrors

**Added by**: Power Virtual Agents Common Solution

See conversationtranscript Table [conversationtranscript_SyncErrors](conversationtranscript.md#BKMK_conversationtranscript_SyncErrors) One-To-Many relationship.

### <a name="BKMK_bot_SyncErrors"></a> bot_SyncErrors

**Added by**: Power Virtual Agents Solution

See bot Table [bot_SyncErrors](bot.md#BKMK_bot_SyncErrors) One-To-Many relationship.

### <a name="BKMK_botcomponent_SyncErrors"></a> botcomponent_SyncErrors

**Added by**: Power Virtual Agents Solution

See botcomponent Table [botcomponent_SyncErrors](botcomponent.md#BKMK_botcomponent_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Territory_SyncErrors"></a> Territory_SyncErrors

**Added by**: Application Common Solution

See territory Table [Territory_SyncErrors](territory.md#BKMK_Territory_SyncErrors) One-To-Many relationship.

### <a name="BKMK_activityfileattachment_SyncErrors"></a> activityfileattachment_SyncErrors

**Added by**: Activities Patch Solution

See activityfileattachment Table [activityfileattachment_SyncErrors](activityfileattachment.md#BKMK_activityfileattachment_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_serviceconfiguration_SyncErrors"></a> msdyn_serviceconfiguration_SyncErrors

**Added by**: Service Level Agreement (SLA) Extension Solution

See msdyn_serviceconfiguration Table [msdyn_serviceconfiguration_SyncErrors](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_slakpi_SyncErrors"></a> msdyn_slakpi_SyncErrors

**Added by**: Service Level Agreement (SLA) Extension Solution

See msdyn_slakpi Table [msdyn_slakpi_SyncErrors](msdyn_slakpi.md#BKMK_msdyn_slakpi_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_federatedarticle_SyncErrors"></a> msdyn_federatedarticle_SyncErrors

**Added by**: Knowledge Management Online Features Solution

See msdyn_federatedarticle Table [msdyn_federatedarticle_SyncErrors](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_federatedarticleincident_SyncErrors"></a> msdyn_federatedarticleincident_SyncErrors

**Added by**: Knowledge Management Online Features Solution

See msdyn_federatedarticleincident Table [msdyn_federatedarticleincident_SyncErrors](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_kmfederatedsearchconfig_SyncErrors"></a> msdyn_kmfederatedsearchconfig_SyncErrors

**Added by**: Knowledge Management Online Features Solution

See msdyn_kmfederatedsearchconfig Table [msdyn_kmfederatedsearchconfig_SyncErrors](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgearticleimage_SyncErrors"></a> msdyn_knowledgearticleimage_SyncErrors

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgearticleimage Table [msdyn_knowledgearticleimage_SyncErrors](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgeinteractioninsight_SyncErrors"></a> msdyn_knowledgeinteractioninsight_SyncErrors

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgeinteractioninsight Table [msdyn_knowledgeinteractioninsight_SyncErrors](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgesearchinsight_SyncErrors"></a> msdyn_knowledgesearchinsight_SyncErrors

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgesearchinsight Table [msdyn_knowledgesearchinsight_SyncErrors](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_kalanguagesetting_SyncErrors"></a> msdyn_kalanguagesetting_SyncErrors

**Added by**: Knowledge Management Features Solution

See msdyn_kalanguagesetting Table [msdyn_kalanguagesetting_SyncErrors](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_kmpersonalizationsetting_SyncErrors"></a> msdyn_kmpersonalizationsetting_SyncErrors

**Added by**: Knowledge Management Features Solution

See msdyn_kmpersonalizationsetting Table [msdyn_kmpersonalizationsetting_SyncErrors](msdyn_kmpersonalizationsetting.md#BKMK_msdyn_kmpersonalizationsetting_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgearticletemplate_SyncErrors"></a> msdyn_knowledgearticletemplate_SyncErrors

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgearticletemplate Table [msdyn_knowledgearticletemplate_SyncErrors](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgepersonalfilter_SyncErrors"></a> msdyn_knowledgepersonalfilter_SyncErrors

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgepersonalfilter Table [msdyn_knowledgepersonalfilter_SyncErrors](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgesearchfilter_SyncErrors"></a> msdyn_knowledgesearchfilter_SyncErrors

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgesearchfilter Table [msdyn_knowledgesearchfilter_SyncErrors](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_SyncErrors) One-To-Many relationship.

### <a name="BKMK_keyvaultreference_SyncErrors"></a> keyvaultreference_SyncErrors

**Added by**: ManagedIdentityExtensions Solution

See keyvaultreference Table [keyvaultreference_SyncErrors](keyvaultreference.md#BKMK_keyvaultreference_SyncErrors) One-To-Many relationship.

### <a name="BKMK_managedidentity_SyncErrors"></a> managedidentity_SyncErrors

**Added by**: ManagedIdentityExtensions Solution

See managedidentity Table [managedidentity_SyncErrors](managedidentity.md#BKMK_managedidentity_SyncErrors) One-To-Many relationship.

### <a name="BKMK_catalog_SyncErrors"></a> catalog_SyncErrors

**Added by**: CatalogFramework Solution

See catalog Table [catalog_SyncErrors](catalog.md#BKMK_catalog_SyncErrors) One-To-Many relationship.

### <a name="BKMK_catalogassignment_SyncErrors"></a> catalogassignment_SyncErrors

**Added by**: CatalogFramework Solution

See catalogassignment Table [catalogassignment_SyncErrors](catalogassignment.md#BKMK_catalogassignment_SyncErrors) One-To-Many relationship.

### <a name="BKMK_customapi_SyncErrors"></a> customapi_SyncErrors

**Added by**: Custom API Framework Solution

See customapi Table [customapi_SyncErrors](customapi.md#BKMK_customapi_SyncErrors) One-To-Many relationship.

### <a name="BKMK_customapirequestparameter_SyncErrors"></a> customapirequestparameter_SyncErrors

**Added by**: Custom API Framework Solution

See customapirequestparameter Table [customapirequestparameter_SyncErrors](customapirequestparameter.md#BKMK_customapirequestparameter_SyncErrors) One-To-Many relationship.

### <a name="BKMK_customapiresponseproperty_SyncErrors"></a> customapiresponseproperty_SyncErrors

**Added by**: Custom API Framework Solution

See customapiresponseproperty Table [customapiresponseproperty_SyncErrors](customapiresponseproperty.md#BKMK_customapiresponseproperty_SyncErrors) One-To-Many relationship.

### <a name="BKMK_organizationdatasyncsubscription_SyncErrors"></a> organizationdatasyncsubscription_SyncErrors

**Added by**: OrganizationDataSyncSolution Solution

See organizationdatasyncsubscription Table [organizationdatasyncsubscription_SyncErrors](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_SyncErrors) One-To-Many relationship.

### <a name="BKMK_organizationdatasyncsubscriptionentity_SyncErrors"></a> organizationdatasyncsubscriptionentity_SyncErrors

**Added by**: OrganizationDataSyncSolution Solution

See organizationdatasyncsubscriptionentity Table [organizationdatasyncsubscriptionentity_SyncErrors](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_SyncErrors) One-To-Many relationship.

### <a name="BKMK_appnotification_SyncErrors"></a> appnotification_SyncErrors

**Added by**: AppNotifications Solution

See appnotification Table [appnotification_SyncErrors](appnotification.md#BKMK_appnotification_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_richtextfile_SyncErrors"></a> msdyn_richtextfile_SyncErrors

**Added by**: Rich Text Editor Solution

See msdyn_richtextfile Table [msdyn_richtextfile_SyncErrors](msdyn_richtextfile.md#BKMK_msdyn_richtextfile_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_aiconfiguration_SyncErrors"></a> msdyn_aiconfiguration_SyncErrors

**Added by**: AISolution Solution

See msdyn_aiconfiguration Table [msdyn_aiconfiguration_SyncErrors](msdyn_aiconfiguration.md#BKMK_msdyn_aiconfiguration_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_aimodel_SyncErrors"></a> msdyn_aimodel_SyncErrors

**Added by**: AISolution Solution

See msdyn_aimodel Table [msdyn_aimodel_SyncErrors](msdyn_aimodel.md#BKMK_msdyn_aimodel_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_aitemplate_SyncErrors"></a> msdyn_aitemplate_SyncErrors

**Added by**: AISolution Solution

See msdyn_aitemplate Table [msdyn_aitemplate_SyncErrors](msdyn_aitemplate.md#BKMK_msdyn_aitemplate_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdataset_SyncErrors"></a> msdyn_aibdataset_SyncErrors

**Added by**: AI Solution default templates Solution

See msdyn_aibdataset Table [msdyn_aibdataset_SyncErrors](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdatasetfile_SyncErrors"></a> msdyn_aibdatasetfile_SyncErrors

**Added by**: AI Solution default templates Solution

See msdyn_aibdatasetfile Table [msdyn_aibdatasetfile_SyncErrors](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdatasetrecord_SyncErrors"></a> msdyn_aibdatasetrecord_SyncErrors

**Added by**: AI Solution default templates Solution

See msdyn_aibdatasetrecord Table [msdyn_aibdatasetrecord_SyncErrors](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdatasetscontainer_SyncErrors"></a> msdyn_aibdatasetscontainer_SyncErrors

**Added by**: AI Solution default templates Solution

See msdyn_aibdatasetscontainer Table [msdyn_aibdatasetscontainer_SyncErrors](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_aibfile_SyncErrors"></a> msdyn_aibfile_SyncErrors

**Added by**: AI Solution default templates Solution

See msdyn_aibfile Table [msdyn_aibfile_SyncErrors](msdyn_aibfile.md#BKMK_msdyn_aibfile_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_aibfileattacheddata_SyncErrors"></a> msdyn_aibfileattacheddata_SyncErrors

**Added by**: AI Solution default templates Solution

See msdyn_aibfileattacheddata Table [msdyn_aibfileattacheddata_SyncErrors](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_aifptrainingdocument_SyncErrors"></a> msdyn_aifptrainingdocument_SyncErrors

**Added by**: AI Solution default templates Solution

See msdyn_aifptrainingdocument Table [msdyn_aifptrainingdocument_SyncErrors](msdyn_aifptrainingdocument.md#BKMK_msdyn_aifptrainingdocument_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodimage_SyncErrors"></a> msdyn_aiodimage_SyncErrors

**Added by**: AI Solution default templates Solution

See msdyn_aiodimage Table [msdyn_aiodimage_SyncErrors](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodlabel_SyncErrors"></a> msdyn_aiodlabel_SyncErrors

**Added by**: AI Solution default templates Solution

See msdyn_aiodlabel Table [msdyn_aiodlabel_SyncErrors](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodtrainingboundingbox_SyncErrors"></a> msdyn_aiodtrainingboundingbox_SyncErrors

**Added by**: AI Solution default templates Solution

See msdyn_aiodtrainingboundingbox Table [msdyn_aiodtrainingboundingbox_SyncErrors](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodtrainingimage_SyncErrors"></a> msdyn_aiodtrainingimage_SyncErrors

**Added by**: AI Solution default templates Solution

See msdyn_aiodtrainingimage Table [msdyn_aiodtrainingimage_SyncErrors](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_pminferredtask_SyncErrors"></a> msdyn_pminferredtask_SyncErrors

**Added by**: Process Mining Solution

See msdyn_pminferredtask Table [msdyn_pminferredtask_SyncErrors](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_pmrecording_SyncErrors"></a> msdyn_pmrecording_SyncErrors

**Added by**: Process Mining Solution

See msdyn_pmrecording Table [msdyn_pmrecording_SyncErrors](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_analysiscomponent_SyncErrors"></a> msdyn_analysiscomponent_SyncErrors

**Added by**: Power Apps Checker Solution

See msdyn_analysiscomponent Table [msdyn_analysiscomponent_SyncErrors](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisjob_SyncErrors"></a> msdyn_analysisjob_SyncErrors

**Added by**: Power Apps Checker Solution

See msdyn_analysisjob Table [msdyn_analysisjob_SyncErrors](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisresult_SyncErrors"></a> msdyn_analysisresult_SyncErrors

**Added by**: Power Apps Checker Solution

See msdyn_analysisresult Table [msdyn_analysisresult_SyncErrors](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisresultdetail_SyncErrors"></a> msdyn_analysisresultdetail_SyncErrors

**Added by**: Power Apps Checker Solution

See msdyn_analysisresultdetail Table [msdyn_analysisresultdetail_SyncErrors](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthrule_SyncErrors"></a> msdyn_solutionhealthrule_SyncErrors

**Added by**: Power Apps Checker Solution

See msdyn_solutionhealthrule Table [msdyn_solutionhealthrule_SyncErrors](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthruleargument_SyncErrors"></a> msdyn_solutionhealthruleargument_SyncErrors

**Added by**: Power Apps Checker Solution

See msdyn_solutionhealthruleargument Table [msdyn_solutionhealthruleargument_SyncErrors](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_SyncErrors) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthruleset_SyncErrors"></a> msdyn_solutionhealthruleset_SyncErrors

**Added by**: Power Apps Checker Solution

See msdyn_solutionhealthruleset Table [msdyn_solutionhealthruleset_SyncErrors](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_SyncErrors) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.syncerror?text=syncerror EntityType" />