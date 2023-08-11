---
title: "System Job (AsyncOperation)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the System Job (AsyncOperation)  table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# System Job (AsyncOperation)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Process whose execution can proceed independently or in the background.


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST /asyncoperations<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE /asyncoperations(*asyncoperationid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET /asyncoperations(*asyncoperationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /asyncoperations<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|Update|PATCH /asyncoperations(*asyncoperationid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|AsyncOperations|
|DisplayCollectionName|System Jobs|
|DisplayName|System Job|
|EntitySetName|asyncoperations|
|IsBPFEntity|False|
|LogicalCollectionName|asyncoperations|
|LogicalName|asyncoperation|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|asyncoperationid|
|PrimaryNameAttribute|name|
|SchemaName|AsyncOperation|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AsyncOperationId](#BKMK_AsyncOperationId)
- [BreadcrumbId](#BKMK_BreadcrumbId)
- [CallerOrigin](#BKMK_CallerOrigin)
- [CorrelationId](#BKMK_CorrelationId)
- [CorrelationUpdatedTime](#BKMK_CorrelationUpdatedTime)
- [Data](#BKMK_Data)
- [DependencyToken](#BKMK_DependencyToken)
- [Depth](#BKMK_Depth)
- [ExpanderStartTime](#BKMK_ExpanderStartTime)
- [FriendlyMessage](#BKMK_FriendlyMessage)
- [HostId](#BKMK_HostId)
- [MessageName](#BKMK_MessageName)
- [Name](#BKMK_Name)
- [OperationType](#BKMK_OperationType)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningExtensionId](#BKMK_OwningExtensionId)
- [OwningExtensionIdName](#BKMK_OwningExtensionIdName)
- [OwningExtensionTypeCode](#BKMK_OwningExtensionTypeCode)
- [ParentPluginExecutionId](#BKMK_ParentPluginExecutionId)
- [PostponeUntil](#BKMK_PostponeUntil)
- [PrimaryEntityType](#BKMK_PrimaryEntityType)
- [RecurrencePattern](#BKMK_RecurrencePattern)
- [RecurrenceStartTime](#BKMK_RecurrenceStartTime)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectIdYomiName](#BKMK_RegardingObjectIdYomiName)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [RequestId](#BKMK_RequestId)
- [RetainJobHistory](#BKMK_RetainJobHistory)
- [RootExecutionContext](#BKMK_RootExecutionContext)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [WorkflowActivationId](#BKMK_WorkflowActivationId)
- [Workload](#BKMK_Workload)


### <a name="BKMK_AsyncOperationId"></a> AsyncOperationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the system job.|
|DisplayName|System Job|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|asyncoperationid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_BreadcrumbId"></a> BreadcrumbId

|Property|Value|
|--------|-----|
|Description|The breadcrumb record ID.|
|DisplayName|Breadcrumb ID|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|breadcrumbid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_CallerOrigin"></a> CallerOrigin

|Property|Value|
|--------|-----|
|Description|The origin of the caller.|
|DisplayName|Caller Origin|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|callerorigin|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CorrelationId"></a> CorrelationId

|Property|Value|
|--------|-----|
|Description|Unique identifier used to correlate between multiple SDK requests and system jobs.|
|DisplayName|Correlation Id|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|correlationid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_CorrelationUpdatedTime"></a> CorrelationUpdatedTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Last time the correlation depth was updated.|
|DisplayName|Correlation Updated Time|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|correlationupdatedtime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_Data"></a> Data

|Property|Value|
|--------|-----|
|Description|Unstructured data associated with the system job.|
|DisplayName|Data|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|data|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_DependencyToken"></a> DependencyToken

|Property|Value|
|--------|-----|
|Description|Execution of all operations with the same dependency token is serialized.|
|DisplayName|Dependency Token|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|dependencytoken|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Depth"></a> Depth

|Property|Value|
|--------|-----|
|Description|Number of SDK calls made since the first call.|
|DisplayName|Depth|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|depth|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_ExpanderStartTime"></a> ExpanderStartTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|The datetime when the Expander pipeline started.|
|DisplayName|Expander Start Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|expanderstarttime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_FriendlyMessage"></a> FriendlyMessage

|Property|Value|
|--------|-----|
|Description|Message provided by the system job.|
|DisplayName|Friendly message|
|Format|Text|
|IsLocalizable|False|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|friendlymessage|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_HostId"></a> HostId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the host that owns this system job.|
|DisplayName|Host|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|hostid|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_MessageName"></a> MessageName

|Property|Value|
|--------|-----|
|Description|Name of the message that started this system job.|
|DisplayName|Message Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|messagename|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of the system job.|
|DisplayName|System Job Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|name|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OperationType"></a> OperationType

|Property|Value|
|--------|-----|
|Description|Type of the system job.|
|DisplayName|System Job Type|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|operationtype|
|RequiredLevel|None|
|Type|Picklist|

#### OperationType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|System Event||
|2|Bulk Email||
|3|Import File Parse||
|4|Transform Parse Data||
|5|Import||
|6|Activity Propagation||
|7|Duplicate Detection Rule Publish||
|8|Bulk Duplicate Detection||
|9|SQM Data Collection||
|10|Workflow||
|11|Quick Campaign||
|12|Matchcode Update||
|13|Bulk Delete||
|14|Deletion Service||
|15|Index Management||
|16|Collect Organization Statistics||
|17|Import Subprocess||
|18|Calculate Organization Storage Size||
|19|Collect Organization Database Statistics||
|20|Collection Organization Size Statistics||
|21|Database Tuning||
|22|Calculate Organization Maximum Storage Size||
|23|Bulk Delete Subprocess||
|24|Update Statistic Intervals||
|25|Organization Full Text Catalog Index||
|26|Database log backup||
|27|Update Contract States||
|28|DBCC SHRINKDATABASE maintenance job||
|29|DBCC SHRINKFILE maintenance job||
|30|Reindex all indices maintenance job||
|31|Storage Limit Notification||
|32|Cleanup inactive workflow assemblies||
|35|Recurring Series Expansion||
|38|Import Sample Data||
|40|Goal Roll Up||
|41|Audit Partition Creation||
|42|Check For Language Pack Updates||
|43|Provision Language Pack||
|44|Update Organization Database||
|45|Update Solution||
|46|Regenerate Entity Row Count Snapshot Data||
|47|Regenerate Read Share Snapshot Data||
|49|Post to Yammer||
|50|Outgoing Activity||
|51|Incoming Email Processing||
|52|Mailbox Test Access||
|53|Encryption Health Check||
|54|Execute Async Request||
|56|Update Entitlement States||
|57|Calculate Rollup Field||
|58|Mass Calculate Rollup Field||
|59|Import Translation||
|62|Convert Date And Time Behavior||
|63|EntityKey Index Creation||
|65|Update Knowledge Article States||
|68|Resource Booking Sync||
|69|Relationship Assistant Cards||
|71|Cleanup Solution Components||
|72|App Module Metadata Operation||
|73|ALM Anomaly Detection Operation||
|75|Flow Notification||
|76|Ribbon Client Metadata Operation||
|79|CallbackRegistration Expander Operation||
|85|Migrate notes to attachments job||
|86|Migrate article content to file storage||
|87|Updated Deactived On for Resolved Cases job||
|89|Cascade Merge Async Operation||
|90|CascadeAssign||
|91|CascadeDelete||
|92|Event Expander Operation||
|93|Import Solution Metadata||
|94|Bulk Delete File Attachment||
|95|Refresh Business Unit for Records Owned By Principal||
|96|Revoke Inherited Access||
|98|Create Or Refresh Virtual Entity||
|100|Cascade FlowSession Permissions Async Operation||
|101|Update Modern Flow Async Operation||
|102|AsyncArchive Async Operation||
|103|Cancel Async Operations (System)||
|201|Provision language for user||
|202|Export Solution Async Operation||
|203|Import Solution Async Operation||
|204|PublishAll Async Operation||
|207|DeleteAndPromote Async Operation||
|208|UninstallSolution Async Operation||
|209|ProvisionLanguage Async Operation||
|210|ImportTranslation Async Operation||
|211|StageAndUpgrade Async Operation||
|239|Denormalization Async Operation||
|250|Refresh Runtime Integration Components Async Operation||
|300|Bulk Archive Operation||
|301|Archive Execution Async Operation||
|302|FinOps Deployment Async Operation||
|304|Purge Archived Content Operation||
|305|Register Offering Async Operation||
|306|Execute DataProcessing Configuration||
|307|Sync Synapse Tables Schema||
|308|FinOps DB Sync Async Operation||
|309|FinOps Unit Test Async Operation||
|320|Catalog Service Generate Package Async Operation||
|321|Catalog Service Submit Approval Request Async Operation||
|322|Catalog Service Install Request Async Operation||
|12801|Cascade Grant or Revoke Access Version Tracking Async Operation||
|190690091|AI Builder Training Events||
|190690092|AI Builder Prediction Events||



### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user or team who owns the system job.|
|DisplayName|Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
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


### <a name="BKMK_OwningExtensionId"></a> OwningExtensionId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the owning extension with which the system job is associated.|
|DisplayName|Owning Extension|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|owningextensionid|
|RequiredLevel|None|
|Targets|sdkmessageprocessingstep|
|Type|Lookup|


### <a name="BKMK_OwningExtensionIdName"></a> OwningExtensionIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|owningextensionidname|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OwningExtensionTypeCode"></a> OwningExtensionTypeCode

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|owningextensiontypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_ParentPluginExecutionId"></a> ParentPluginExecutionId

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|parentpluginexecutionid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_PostponeUntil"></a> PostponeUntil

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Indicates whether the system job should run only after the specified date and time.|
|DisplayName|Postpone Until|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|postponeuntil|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_PrimaryEntityType"></a> PrimaryEntityType

|Property|Value|
|--------|-----|
|Description|Type of entity with which the system job is primarily associated.|
|DisplayName|Primary Entity Type|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|primaryentitytype|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_RecurrencePattern"></a> RecurrencePattern

|Property|Value|
|--------|-----|
|Description|Pattern of the system job's recurrence.|
|DisplayName|Recurrence Pattern|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|recurrencepattern|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RecurrenceStartTime"></a> RecurrenceStartTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Starting time in UTC for the recurrence pattern.|
|DisplayName|Recurrence Start|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|recurrencestarttime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the object with which the system job is associated.|
|DisplayName|Regarding|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|regardingobjectid|
|RequiredLevel|None|
|Targets|account,activityfileattachment,activitymimeattachment,activitypointer,annotation,annualfiscalcalendar,appaction,appactionmigration,appactionrule,appelement,applicationuser,appmodulecomponentedge,appmodulecomponentnode,appointment,appsetting,appusersetting,archivecleanupinfo,archivecleanupoperation,attributeimageconfig,attributemap,bot,botcomponent,bulkarchiveconfig,bulkarchivefailuredetail,bulkarchiveoperation,bulkarchiveoperationdetail,businessunit,businessunitnewsarticle,calendar,canvasappextendedmetadata,card,cascadegrantrevokeaccessrecordstracker,cascadegrantrevokeaccessversiontracker,catalog,catalogassignment,channelaccessprofile,channelaccessprofilerule,chat,comment,connection,connectioninstance,connectionreference,connectionrole,connector,contact,conversationtranscript,convertrule,customapi,customapirequestparameter,customapiresponseproperty,customeraddress,customerrelationship,datalakefolder,datalakefolderpermission,datalakeworkspace,datalakeworkspacepermission,dataprocessingconfiguration,delegatedauthorization,desktopflowbinary,desktopflowmodule,displaystring,email,emailserverprofile,enablearchivalrequest,entityanalyticsconfig,entityimageconfig,entityindex,entitymap,entityrecordfilter,environmentvariabledefinition,environmentvariablevalue,exportedexcel,exportsolutionupload,externalparty,externalpartyitem,fax,featurecontrolsetting,fixedmonthlyfiscalcalendar,flowmachine,flowmachinegroup,flowmachineimage,flowmachineimageversion,flowmachinenetwork,flowsession,fxexpression,goal,goalrollupquery,holidaywrapper,import,importdata,importfile,importlog,importmap,indexattributes,interactionforemail,internalcatalogassignment,isvconfig,kbarticle,kbarticlecomment,kbarticletemplate,keyvaultreference,knowledgearticle,knowledgebaserecord,letter,mailbox,mailmergetemplate,managedidentity,metadataforarchival,metric,mobileofflineprofileextension,monthlyfiscalcalendar,msdynce_botcontent,msdyn_aibdataset,msdyn_aibdatasetfile,msdyn_aibdatasetrecord,msdyn_aibdatasetscontainer,msdyn_aibfeedbackloop,msdyn_aibfile,msdyn_aibfileattacheddata,msdyn_aiconfiguration,msdyn_aievent,msdyn_aifptrainingdocument,msdyn_aimodel,msdyn_aiodimage,msdyn_aiodlabel,msdyn_aiodtrainingboundingbox,msdyn_aiodtrainingimage,msdyn_aitemplate,msdyn_analysiscomponent,msdyn_analysisjob,msdyn_analysisoverride,msdyn_analysisresult,msdyn_analysisresultdetail,msdyn_appinsightsmetadata,msdyn_customcontrolextendedsettings,msdyn_dataflow,msdyn_dataflowrefreshhistory,msdyn_dataflowtemplate,msdyn_dataflow_datalakefolder,msdyn_dmsrequest,msdyn_dmsrequeststatus,msdyn_entitylinkchatconfiguration,msdyn_entityrefreshhistory,msdyn_favoriteknowledgearticle,msdyn_federatedarticle,msdyn_federatedarticleincident,msdyn_fileupload,msdyn_helppage,msdyn_insightsstorevirtualentity,msdyn_integratedsearchprovider,msdyn_kalanguagesetting,msdyn_kbattachment,msdyn_kmfederatedsearchconfig,msdyn_kmpersonalizationsetting,msdyn_knowledgearticleimage,msdyn_knowledgearticletemplate,msdyn_knowledgeconfiguration,msdyn_knowledgeinteractioninsight,msdyn_knowledgemanagementsetting,msdyn_knowledgepersonalfilter,msdyn_knowledgesearchfilter,msdyn_knowledgesearchinsight,msdyn_mobileapp,msdyn_pmanalysishistory,msdyn_pmcalendar,msdyn_pmcalendarversion,msdyn_pminferredtask,msdyn_pmprocessextendedmetadataversion,msdyn_pmprocesstemplate,msdyn_pmprocessusersettings,msdyn_pmprocessversion,msdyn_pmrecording,msdyn_pmtemplate,msdyn_pmview,msdyn_richtextfile,msdyn_schedule,msdyn_serviceconfiguration,msdyn_slakpi,msdyn_solutionhealthrule,msdyn_solutionhealthruleargument,msdyn_solutionhealthruleset,msdyn_tour,msdyn_virtualtablecolumncandidate,msdyn_workflowactionstatus,msgraphresourcetosubscription,mspcat_catalogsubmissionfiles,mspcat_packagestore,organization,organizationdatasyncfnostate,organizationdatasyncstate,organizationdatasyncsubscription,organizationdatasyncsubscriptionentity,organizationdatasyncsubscriptionfnotable,organizationsetting,package,pdfsetting,phonecall,pluginpackage,position,post,postfollow,powerbidataset,powerbimashupparameter,powerbireport,powerfxrule,privilege,privilegesremovalsetting,processstageparameter,provisionlanguageforuser,quarterlyfiscalcalendar,queue,queueitem,reconciliationentityinfo,reconciliationinfo,recordfilter,recurringappointmentmaster,relationshipattribute,relationshiprole,relationshiprolemap,report,retaineddataexcel,retentioncleanupinfo,retentioncleanupoperation,retentionconfig,retentionfailuredetail,retentionoperation,retentionoperationdetail,revokeinheritedaccessrecordstracker,role,roleeditorlayout,rollupfield,routingrule,routingruleitem,savedquery,searchattributesettings,searchcustomanalyzer,searchrelationshipsettings,semiannualfiscalcalendar,serviceplan,serviceplanmapping,settingdefinition,sharedlinksetting,sharedobject,sharedworkspace,sharedworkspacepool,sharepointdocumentlocation,sharepointsite,similarityrule,sla,socialactivity,socialprofile,solutioncomponentattributeconfiguration,solutioncomponentbatchconfiguration,solutioncomponentconfiguration,solutioncomponentrelationshipconfiguration,stagedentity,stagedentityattribute,stagesolutionupload,subject,supportusertable,synapsedatabase,synapselinkexternaltablestate,synapselinkprofile,synapselinkprofileentity,synapselinkprofileentitystate,synapselinkschedule,systemform,systemuser,systemuserauthorizationchangetracker,task,tdsmetadata,team,teammobileofflineprofilemembership,template,territory,theme,transactioncurrency,userform,usermapping,usermobileofflineprofilemembership,userquery,userrating,virtualentitymetadata,workflowbinary,workqueue,workqueueitem|
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


### <a name="BKMK_RequestId"></a> RequestId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the request that generated the system job.|
|DisplayName|Request|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|requestid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_RetainJobHistory"></a> RetainJobHistory

|Property|Value|
|--------|-----|
|Description|Retain job history.|
|DisplayName|Retain Job History|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|retainjobhistory|
|RequiredLevel|None|
|Type|Boolean|

#### RetainJobHistory Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_RootExecutionContext"></a> RootExecutionContext

|Property|Value|
|--------|-----|
|Description|Root execution context of the job that trigerred async job.|
|DisplayName|RootExecutionContext|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|rootexecutioncontext|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|--------|-----|
|Description|Status of the system job.|
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
|0|Ready|0|Ready|
|1|Suspended|10|Suspended|
|2|Locked|20|Locked|
|3|Completed|30|Completed|



### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the system job.|
|DisplayName|Status Reason|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### StatusCode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|0|Waiting For Resources|0|
|10|Waiting|1|
|20|In Progress|2|
|21|Pausing|2|
|22|Canceling|2|
|30|Succeeded|3|
|31|Failed|3|
|32|Canceled|3|



### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|timezoneruleversionnumber|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|--------|-----|
|Description|Time zone code that was in use when the record was created.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|utcconversiontimezonecode|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_WorkflowActivationId"></a> WorkflowActivationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the workflow activation related to the system job.|
|DisplayName|Workflow Activation Id|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|workflowactivationid|
|RequiredLevel|None|
|Targets|workflow|
|Type|Lookup|


### <a name="BKMK_Workload"></a> Workload

|Property|Value|
|--------|-----|
|Description|The workload name.|
|DisplayName|Workload|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|workload|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CompletedOn](#BKMK_CompletedOn)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [DataBlobId](#BKMK_DataBlobId)
- [DataBlobId_Name](#BKMK_DataBlobId_Name)
- [ErrorCode](#BKMK_ErrorCode)
- [ExecutionTimeSpan](#BKMK_ExecutionTimeSpan)
- [IsWaitingForEvent](#BKMK_IsWaitingForEvent)
- [Message](#BKMK_Message)
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
- [RetryCount](#BKMK_RetryCount)
- [Sequence](#BKMK_Sequence)
- [StartedOn](#BKMK_StartedOn)
- [Subtype](#BKMK_Subtype)
- [WorkflowActivationIdName](#BKMK_WorkflowActivationIdName)
- [WorkflowIsBlocked](#BKMK_WorkflowIsBlocked)
- [WorkflowStageName](#BKMK_WorkflowStageName)
- [WorkflowState](#BKMK_WorkflowState)


### <a name="BKMK_CompletedOn"></a> CompletedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the system job was completed.|
|DisplayName|Completed On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|completedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the system job.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|SystemRequired|
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
|MaxLength|160|
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
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the system job was created.|
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
|Description|Unique identifier of the delegate user who created the asyncoperation.|
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


### <a name="BKMK_DataBlobId"></a> DataBlobId

**Added by**: DataEngine Schema Changes Solution

|Property|Value|
|--------|-----|
|Description|File Id for the blob url used for file storage.|
|DisplayName|Data File Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|datablobid|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_DataBlobId_Name"></a> DataBlobId_Name

**Added by**: DataEngine Schema Changes Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|datablobid_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ErrorCode"></a> ErrorCode

|Property|Value|
|--------|-----|
|Description|Error code returned from a canceled system job.|
|DisplayName|Error Code|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|errorcode|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ExecutionTimeSpan"></a> ExecutionTimeSpan

|Property|Value|
|--------|-----|
|Description|Time that the system job has taken to execute.|
|DisplayName|ExecutionTimeSpan|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|executiontimespan|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|
|RequiredLevel|SystemRequired|
|Type|Double|


### <a name="BKMK_IsWaitingForEvent"></a> IsWaitingForEvent

|Property|Value|
|--------|-----|
|Description|Indicates that the system job is waiting for an event.|
|DisplayName|Waiting for Event|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iswaitingforevent|
|RequiredLevel|None|
|Type|Boolean|

#### IsWaitingForEvent Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_Message"></a> Message

|Property|Value|
|--------|-----|
|Description|Message related to the system job.|
|DisplayName|Message|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|message|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the system job.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|SystemRequired|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

|Property|Value|
|--------|-----|
|Description|Name of the user who last modified the record.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

|Property|Value|
|--------|-----|
|Description|YomiName of the user who last modified the record.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyyominame|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the system job was last modified.|
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
|Description|Unique identifier of the delegate user who last modified the asyncoperation.|
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
|MaxLength|160|
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
|MaxLength|160|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|--------|-----|
|Description|Unique identifier of the business unit that owns the system job.|
|DisplayName|Owning Business Unit|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|SystemRequired|
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
|Description|Unique identifier of the team who owns the record.|
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
|Description|Unique identifier of the user who owns the record.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_RetryCount"></a> RetryCount

|Property|Value|
|--------|-----|
|Description|Number of times to retry the system job.|
|DisplayName|Retry Count|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|retrycount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_Sequence"></a> Sequence

|Property|Value|
|--------|-----|
|Description|Order in which operations were submitted.|
|DisplayName|Sequence|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|sequence|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|SystemRequired|
|Type|BigInt|


### <a name="BKMK_StartedOn"></a> StartedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the system job was started.|
|DisplayName|Started On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|startedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_Subtype"></a> Subtype

|Property|Value|
|--------|-----|
|Description|The Subtype of the Async Job|
|DisplayName|Subtype|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|subtype|
|MaxValue|255|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_WorkflowActivationIdName"></a> WorkflowActivationIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|workflowactivationidname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_WorkflowIsBlocked"></a> WorkflowIsBlocked

|Property|Value|
|--------|-----|
|Description|Indicates whether the workflow instance was blocked when it was persisted.|
|DisplayName|Workflow Is Blocked|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|workflowisblocked|
|RequiredLevel|None|
|Type|Boolean|

#### WorkflowIsBlocked Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_WorkflowStageName"></a> WorkflowStageName

|Property|Value|
|--------|-----|
|Description|Name of a workflow stage.|
|DisplayName|Workflow Stage|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|workflowstagename|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_WorkflowState"></a> WorkflowState

|Property|Value|
|--------|-----|
|Description|State of the workflow job.|
|DisplayName|Workflow State|
|FormatName|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|workflowstate|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [AsyncOperation_MailboxTrackingFolder](#BKMK_AsyncOperation_MailboxTrackingFolder)
- [AsyncOperation_BulkDeleteOperation](#BKMK_AsyncOperation_BulkDeleteOperation)
- [lk_workflowlog_asyncoperation_childworkflow](#BKMK_lk_workflowlog_asyncoperation_childworkflow)
- [AsyncOperation_Emails](#BKMK_AsyncOperation_Emails)
- [AsyncOperation_DuplicateBaseRecord](#BKMK_AsyncOperation_DuplicateBaseRecord)
- [lk_workflowlog_asyncoperations](#BKMK_lk_workflowlog_asyncoperations)
- [AsyncOperation_SocialActivities](#BKMK_AsyncOperation_SocialActivities)


### <a name="BKMK_AsyncOperation_MailboxTrackingFolder"></a> AsyncOperation_MailboxTrackingFolder

Same as the [AsyncOperation_MailboxTrackingFolder](mailboxtrackingfolder.md#BKMK_AsyncOperation_MailboxTrackingFolder) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|AsyncOperation_MailboxTrackingFolder|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_AsyncOperation_BulkDeleteOperation"></a> AsyncOperation_BulkDeleteOperation

Same as the [AsyncOperation_BulkDeleteOperation](bulkdeleteoperation.md#BKMK_AsyncOperation_BulkDeleteOperation) many-to-one relationship for the [bulkdeleteoperation](bulkdeleteoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeleteoperation|
|ReferencingAttribute|asyncoperationid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|AsyncOperation_BulkDeleteOperation|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_workflowlog_asyncoperation_childworkflow"></a> lk_workflowlog_asyncoperation_childworkflow

Same as the [lk_workflowlog_asyncoperation_childworkflow](workflowlog.md#BKMK_lk_workflowlog_asyncoperation_childworkflow) many-to-one relationship for the [workflowlog](workflowlog.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflowlog|
|ReferencingAttribute|childworkflowinstanceid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_workflowlog_asyncoperation_childworkflow|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_AsyncOperation_Emails"></a> AsyncOperation_Emails

Same as the [AsyncOperation_Emails](email.md#BKMK_AsyncOperation_Emails) many-to-one relationship for the [email](email.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|AsyncOperation_Emails|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_AsyncOperation_DuplicateBaseRecord"></a> AsyncOperation_DuplicateBaseRecord

Same as the [AsyncOperation_DuplicateBaseRecord](duplicaterecord.md#BKMK_AsyncOperation_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|asyncoperationid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|AsyncOperation_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_workflowlog_asyncoperations"></a> lk_workflowlog_asyncoperations

Same as the [lk_workflowlog_asyncoperations](workflowlog.md#BKMK_lk_workflowlog_asyncoperations) many-to-one relationship for the [workflowlog](workflowlog.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflowlog|
|ReferencingAttribute|asyncoperationid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_workflowlog_asyncoperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_AsyncOperation_SocialActivities"></a> AsyncOperation_SocialActivities

Same as the [AsyncOperation_SocialActivities](socialactivity.md#BKMK_AsyncOperation_SocialActivities) many-to-one relationship for the [socialactivity](socialactivity.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|AsyncOperation_SocialActivities|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [theme_AsyncOperations](#BKMK_theme_AsyncOperations)
- [usermapping_AsyncOperations](#BKMK_usermapping_AsyncOperations)
- [interactionforemail_AsyncOperations](#BKMK_interactionforemail_AsyncOperations)
- [knowledgearticle_AsyncOperations](#BKMK_knowledgearticle_AsyncOperations)
- [post_AsyncOperations](#BKMK_post_AsyncOperations)
- [position_AsyncOperations](#BKMK_position_AsyncOperations)
- [KnowledgeBaseRecord_AsyncOperations](#BKMK_KnowledgeBaseRecord_AsyncOperations)
- [lk_asyncoperation_createdby](#BKMK_lk_asyncoperation_createdby)
- [MonthlyFiscalCalendar_AsyncOperations](#BKMK_MonthlyFiscalCalendar_AsyncOperations)
- [lk_asyncoperation_workflowactivationid](#BKMK_lk_asyncoperation_workflowactivationid)
- [Report_AsyncOperations](#BKMK_Report_AsyncOperations)
- [SocialActivity_AsyncOperations](#BKMK_SocialActivity_AsyncOperations)
- [Connection_Role_AsyncOperations](#BKMK_Connection_Role_AsyncOperations)
- [Team_AsyncOperations](#BKMK_Team_AsyncOperations)
- [AnnualFiscalCalendar_AsyncOperations](#BKMK_AnnualFiscalCalendar_AsyncOperations)
- [SharePointDocumentLocation_AsyncOperations](#BKMK_SharePointDocumentLocation_AsyncOperations)
- [PhoneCall_AsyncOperations](#BKMK_PhoneCall_AsyncOperations)
- [mailbox_asyncoperations](#BKMK_mailbox_asyncoperations)
- [PostFollow_AsyncOperations](#BKMK_PostFollow_AsyncOperations)
- [Appointment_AsyncOperations](#BKMK_Appointment_AsyncOperations)
- [slabase_AsyncOperations](#BKMK_slabase_AsyncOperations)
- [SavedQuery_AsyncOperations](#BKMK_SavedQuery_AsyncOperations)
- [DisplayString_AsyncOperations](#BKMK_DisplayString_AsyncOperations)
- [KbArticleComment_AsyncOperations](#BKMK_KbArticleComment_AsyncOperations)
- [ActivityPointer_AsyncOperations](#BKMK_ActivityPointer_AsyncOperations)
- [Subject_AsyncOperations](#BKMK_Subject_AsyncOperations)
- [goalrollupquery_AsyncOperations](#BKMK_goalrollupquery_AsyncOperations)
- [Role_AsyncOperations](#BKMK_Role_AsyncOperations)
- [SystemForm_AsyncOperations](#BKMK_SystemForm_AsyncOperations)
- [Annotation_AsyncOperations](#BKMK_Annotation_AsyncOperations)
- [Privilege_AsyncOperations](#BKMK_Privilege_AsyncOperations)
- [ActivityMimeAttachment_AsyncOperations](#BKMK_ActivityMimeAttachment_AsyncOperations)
- [Goal_AsyncOperations](#BKMK_Goal_AsyncOperations)
- [Fax_AsyncOperations](#BKMK_Fax_AsyncOperations)
- [QuarterlyFiscalCalendar_AsyncOperations](#BKMK_QuarterlyFiscalCalendar_AsyncOperations)
- [SharePointSite_AsyncOperations](#BKMK_SharePointSite_AsyncOperations)
- [UserQuery_AsyncOperations](#BKMK_UserQuery_AsyncOperations)
- [ImportMap_AsyncOperations](#BKMK_ImportMap_AsyncOperations)
- [BusinessUnit_AsyncOperations](#BKMK_BusinessUnit_AsyncOperations)
- [Queue_AsyncOperations](#BKMK_Queue_AsyncOperations)
- [QueueItem_AsyncOperations](#BKMK_QueueItem_AsyncOperations)
- [team_asyncoperation](#BKMK_team_asyncoperation)
- [lk_asyncoperation_modifiedby](#BKMK_lk_asyncoperation_modifiedby)
- [UserForm_AsyncOperations](#BKMK_UserForm_AsyncOperations)
- [TransactionCurrency_AsyncOperations](#BKMK_TransactionCurrency_AsyncOperations)
- [rollupfield_AsyncOperations](#BKMK_rollupfield_AsyncOperations)
- [Letter_AsyncOperations](#BKMK_Letter_AsyncOperations)
- [KbArticle_AsyncOperations](#BKMK_KbArticle_AsyncOperations)
- [RecurringAppointmentMaster_AsyncOperations](#BKMK_RecurringAppointmentMaster_AsyncOperations)
- [Task_AsyncOperations](#BKMK_Task_AsyncOperations)
- [BusinessUnitNewsArticle_AsyncOperations](#BKMK_BusinessUnitNewsArticle_AsyncOperations)
- [Connection_AsyncOperations](#BKMK_Connection_AsyncOperations)
- [SystemUser_AsyncOperations](#BKMK_SystemUser_AsyncOperations)
- [KbArticleTemplate_AsyncOperations](#BKMK_KbArticleTemplate_AsyncOperations)
- [SdkMessageProcessingStep_AsyncOperations](#BKMK_SdkMessageProcessingStep_AsyncOperations)
- [Template_AsyncOperations](#BKMK_Template_AsyncOperations)
- [CustomerAddress_AsyncOperations](#BKMK_CustomerAddress_AsyncOperations)
- [Contact_AsyncOperations](#BKMK_Contact_AsyncOperations)
- [emailserverprofile_asyncoperations](#BKMK_emailserverprofile_asyncoperations)
- [lk_asyncoperation_createdonbehalfby](#BKMK_lk_asyncoperation_createdonbehalfby)
- [Import_AsyncOperations](#BKMK_Import_AsyncOperations)
- [system_user_asyncoperation](#BKMK_system_user_asyncoperation)
- [business_unit_asyncoperation](#BKMK_business_unit_asyncoperation)
- [ImportLog_AsyncOperations](#BKMK_ImportLog_AsyncOperations)
- [metric_AsyncOperations](#BKMK_metric_AsyncOperations)
- [SocialProfile_AsyncOperations](#BKMK_SocialProfile_AsyncOperations)
- [lk_asyncoperation_modifiedonbehalfby](#BKMK_lk_asyncoperation_modifiedonbehalfby)
- [Account_AsyncOperations](#BKMK_Account_AsyncOperations)
- [Email_AsyncOperations](#BKMK_Email_AsyncOperations)
- [FixedMonthlyFiscalCalendar_AsyncOperations](#BKMK_FixedMonthlyFiscalCalendar_AsyncOperations)
- [SemiAnnualFiscalCalendar_AsyncOperations](#BKMK_SemiAnnualFiscalCalendar_AsyncOperations)
- [MailMergeTemplate_AsyncOperations](#BKMK_MailMergeTemplate_AsyncOperations)
- [Organization_AsyncOperations](#BKMK_Organization_AsyncOperations)
- [Calendar_AsyncOperations](#BKMK_Calendar_AsyncOperations)
- [ImportFile_AsyncOperations](#BKMK_ImportFile_AsyncOperations)
- [solutioncomponentattributeconfiguration_AsyncOperations](#BKMK_solutioncomponentattributeconfiguration_AsyncOperations)
- [solutioncomponentbatchconfiguration_AsyncOperations](#BKMK_solutioncomponentbatchconfiguration_AsyncOperations)
- [solutioncomponentconfiguration_AsyncOperations](#BKMK_solutioncomponentconfiguration_AsyncOperations)
- [solutioncomponentrelationshipconfiguration_AsyncOperations](#BKMK_solutioncomponentrelationshipconfiguration_AsyncOperations)
- [package_AsyncOperations](#BKMK_package_AsyncOperations)
- [stagesolutionupload_AsyncOperations](#BKMK_stagesolutionupload_AsyncOperations)
- [exportsolutionupload_AsyncOperations](#BKMK_exportsolutionupload_AsyncOperations)
- [featurecontrolsetting_AsyncOperations](#BKMK_featurecontrolsetting_AsyncOperations)
- [attributeimageconfig_AsyncOperations](#BKMK_attributeimageconfig_AsyncOperations)
- [entityimageconfig_AsyncOperations](#BKMK_entityimageconfig_AsyncOperations)
- [relationshipattribute_AsyncOperations](#BKMK_relationshipattribute_AsyncOperations)
- [stagedentity_AsyncOperations](#BKMK_stagedentity_AsyncOperations)
- [stagedentityattribute_AsyncOperations](#BKMK_stagedentityattribute_AsyncOperations)
- [catalog_AsyncOperations](#BKMK_catalog_AsyncOperations)
- [catalogassignment_AsyncOperations](#BKMK_catalogassignment_AsyncOperations)
- [customapi_AsyncOperations](#BKMK_customapi_AsyncOperations)
- [customapirequestparameter_AsyncOperations](#BKMK_customapirequestparameter_AsyncOperations)
- [customapiresponseproperty_AsyncOperations](#BKMK_customapiresponseproperty_AsyncOperations)
- [provisionlanguageforuser_AsyncOperations](#BKMK_provisionlanguageforuser_AsyncOperations)
- [sharedobject_AsyncOperations](#BKMK_sharedobject_AsyncOperations)
- [sharedworkspace_AsyncOperations](#BKMK_sharedworkspace_AsyncOperations)
- [sharedworkspacepool_AsyncOperations](#BKMK_sharedworkspacepool_AsyncOperations)
- [entityanalyticsconfig_AsyncOperations](#BKMK_entityanalyticsconfig_AsyncOperations)
- [datalakefolder_AsyncOperations](#BKMK_datalakefolder_AsyncOperations)
- [datalakefolderpermission_AsyncOperations](#BKMK_datalakefolderpermission_AsyncOperations)
- [datalakeworkspace_AsyncOperations](#BKMK_datalakeworkspace_AsyncOperations)
- [datalakeworkspacepermission_AsyncOperations](#BKMK_datalakeworkspacepermission_AsyncOperations)
- [dataprocessingconfiguration_AsyncOperations](#BKMK_dataprocessingconfiguration_AsyncOperations)
- [exportedexcel_AsyncOperations](#BKMK_exportedexcel_AsyncOperations)
- [retaineddataexcel_AsyncOperations](#BKMK_retaineddataexcel_AsyncOperations)
- [synapsedatabase_AsyncOperations](#BKMK_synapsedatabase_AsyncOperations)
- [synapselinkexternaltablestate_AsyncOperations](#BKMK_synapselinkexternaltablestate_AsyncOperations)
- [synapselinkprofile_AsyncOperations](#BKMK_synapselinkprofile_AsyncOperations)
- [synapselinkprofileentity_AsyncOperations](#BKMK_synapselinkprofileentity_AsyncOperations)
- [synapselinkprofileentitystate_AsyncOperations](#BKMK_synapselinkprofileentitystate_AsyncOperations)
- [synapselinkschedule_AsyncOperations](#BKMK_synapselinkschedule_AsyncOperations)
- [msdyn_dataflow_AsyncOperations](#BKMK_msdyn_dataflow_AsyncOperations)
- [msdyn_dataflowrefreshhistory_AsyncOperations](#BKMK_msdyn_dataflowrefreshhistory_AsyncOperations)
- [msdyn_entityrefreshhistory_AsyncOperations](#BKMK_msdyn_entityrefreshhistory_AsyncOperations)
- [sharedlinksetting_AsyncOperations](#BKMK_sharedlinksetting_AsyncOperations)
- [entityrecordfilter_AsyncOperations](#BKMK_entityrecordfilter_AsyncOperations)
- [recordfilter_AsyncOperations](#BKMK_recordfilter_AsyncOperations)
- [delegatedauthorization_AsyncOperations](#BKMK_delegatedauthorization_AsyncOperations)
- [serviceplan_AsyncOperations](#BKMK_serviceplan_AsyncOperations)
- [serviceplanmapping_AsyncOperations](#BKMK_serviceplanmapping_AsyncOperations)
- [applicationuser_AsyncOperations](#BKMK_applicationuser_AsyncOperations)
- [connector_AsyncOperations](#BKMK_connector_AsyncOperations)
- [environmentvariabledefinition_AsyncOperations](#BKMK_environmentvariabledefinition_AsyncOperations)
- [environmentvariablevalue_AsyncOperations](#BKMK_environmentvariablevalue_AsyncOperations)
- [workflowbinary_AsyncOperations](#BKMK_workflowbinary_AsyncOperations)
- [desktopflowmodule_AsyncOperations](#BKMK_desktopflowmodule_AsyncOperations)
- [flowmachine_AsyncOperations](#BKMK_flowmachine_AsyncOperations)
- [flowmachinegroup_AsyncOperations](#BKMK_flowmachinegroup_AsyncOperations)
- [flowmachineimage_AsyncOperations](#BKMK_flowmachineimage_AsyncOperations)
- [flowmachineimageversion_AsyncOperations](#BKMK_flowmachineimageversion_AsyncOperations)
- [flowmachinenetwork_AsyncOperations](#BKMK_flowmachinenetwork_AsyncOperations)
- [processstageparameter_AsyncOperations](#BKMK_processstageparameter_AsyncOperations)
- [workqueue_AsyncOperations](#BKMK_workqueue_AsyncOperations)
- [workqueueitem_AsyncOperations](#BKMK_workqueueitem_AsyncOperations)
- [desktopflowbinary_AsyncOperations](#BKMK_desktopflowbinary_AsyncOperations)
- [flowsession_AsyncOperations](#BKMK_flowsession_AsyncOperations)
- [connectionreference_AsyncOperations](#BKMK_connectionreference_AsyncOperations)
- [connectioninstance_AsyncOperations](#BKMK_connectioninstance_AsyncOperations)
- [msdyn_helppage_AsyncOperations](#BKMK_msdyn_helppage_AsyncOperations)
- [msdyn_tour_AsyncOperations](#BKMK_msdyn_tour_AsyncOperations)
- [msdynce_botcontent_AsyncOperations](#BKMK_msdynce_botcontent_AsyncOperations)
- [conversationtranscript_AsyncOperations](#BKMK_conversationtranscript_AsyncOperations)
- [bot_AsyncOperations](#BKMK_bot_AsyncOperations)
- [botcomponent_AsyncOperations](#BKMK_botcomponent_AsyncOperations)
- [Territory_AsyncOperations](#BKMK_Territory_AsyncOperations)
- [activityfileattachment_AsyncOperations](#BKMK_activityfileattachment_AsyncOperations)
- [chat_AsyncOperations](#BKMK_chat_AsyncOperations)
- [msdyn_serviceconfiguration_AsyncOperations](#BKMK_msdyn_serviceconfiguration_AsyncOperations)
- [msdyn_slakpi_AsyncOperations](#BKMK_msdyn_slakpi_AsyncOperations)
- [msdyn_knowledgemanagementsetting_AsyncOperations](#BKMK_msdyn_knowledgemanagementsetting_AsyncOperations)
- [msdyn_federatedarticle_AsyncOperations](#BKMK_msdyn_federatedarticle_AsyncOperations)
- [msdyn_federatedarticleincident_AsyncOperations](#BKMK_msdyn_federatedarticleincident_AsyncOperations)
- [msdyn_integratedsearchprovider_AsyncOperations](#BKMK_msdyn_integratedsearchprovider_AsyncOperations)
- [msdyn_kmfederatedsearchconfig_AsyncOperations](#BKMK_msdyn_kmfederatedsearchconfig_AsyncOperations)
- [msdyn_knowledgearticleimage_AsyncOperations](#BKMK_msdyn_knowledgearticleimage_AsyncOperations)
- [msdyn_knowledgeconfiguration_AsyncOperations](#BKMK_msdyn_knowledgeconfiguration_AsyncOperations)
- [msdyn_knowledgeinteractioninsight_AsyncOperations](#BKMK_msdyn_knowledgeinteractioninsight_AsyncOperations)
- [msdyn_knowledgesearchinsight_AsyncOperations](#BKMK_msdyn_knowledgesearchinsight_AsyncOperations)
- [msdyn_favoriteknowledgearticle_AsyncOperations](#BKMK_msdyn_favoriteknowledgearticle_AsyncOperations)
- [msdyn_kalanguagesetting_AsyncOperations](#BKMK_msdyn_kalanguagesetting_AsyncOperations)
- [msdyn_kbattachment_AsyncOperations](#BKMK_msdyn_kbattachment_AsyncOperations)
- [msdyn_kmpersonalizationsetting_AsyncOperations](#BKMK_msdyn_kmpersonalizationsetting_AsyncOperations)
- [msdyn_knowledgearticletemplate_AsyncOperations](#BKMK_msdyn_knowledgearticletemplate_AsyncOperations)
- [msdyn_knowledgepersonalfilter_AsyncOperations](#BKMK_msdyn_knowledgepersonalfilter_AsyncOperations)
- [msdyn_knowledgesearchfilter_AsyncOperations](#BKMK_msdyn_knowledgesearchfilter_AsyncOperations)
- [pluginpackage_AsyncOperations](#BKMK_pluginpackage_AsyncOperations)
- [fxexpression_AsyncOperations](#BKMK_fxexpression_AsyncOperations)
- [powerfxrule_AsyncOperations](#BKMK_powerfxrule_AsyncOperations)
- [keyvaultreference_AsyncOperations](#BKMK_keyvaultreference_AsyncOperations)
- [managedidentity_AsyncOperations](#BKMK_managedidentity_AsyncOperations)
- [msgraphresourcetosubscription_AsyncOperations](#BKMK_msgraphresourcetosubscription_AsyncOperations)
- [virtualentitymetadata_AsyncOperations](#BKMK_virtualentitymetadata_AsyncOperations)
- [mobileofflineprofileextension_AsyncOperations](#BKMK_mobileofflineprofileextension_AsyncOperations)
- [teammobileofflineprofilemembership_AsyncOperations](#BKMK_teammobileofflineprofilemembership_AsyncOperations)
- [usermobileofflineprofilemembership_AsyncOperations](#BKMK_usermobileofflineprofilemembership_AsyncOperations)
- [organizationdatasyncsubscription_AsyncOperations](#BKMK_organizationdatasyncsubscription_AsyncOperations)
- [organizationdatasyncsubscriptionentity_AsyncOperations](#BKMK_organizationdatasyncsubscriptionentity_AsyncOperations)
- [organizationdatasyncsubscriptionfnotable_AsyncOperations](#BKMK_organizationdatasyncsubscriptionfnotable_AsyncOperations)
- [organizationdatasyncfnostate_AsyncOperations](#BKMK_organizationdatasyncfnostate_AsyncOperations)
- [organizationdatasyncstate_AsyncOperations](#BKMK_organizationdatasyncstate_AsyncOperations)
- [metadataforarchival_AsyncOperations](#BKMK_metadataforarchival_AsyncOperations)
- [retentionconfig_AsyncOperations](#BKMK_retentionconfig_AsyncOperations)
- [retentionfailuredetail_AsyncOperations](#BKMK_retentionfailuredetail_AsyncOperations)
- [retentionoperation_AsyncOperations](#BKMK_retentionoperation_AsyncOperations)
- [retentionoperationdetail_AsyncOperations](#BKMK_retentionoperationdetail_AsyncOperations)
- [msdyn_appinsightsmetadata_AsyncOperations](#BKMK_msdyn_appinsightsmetadata_AsyncOperations)
- [msdyn_dataflowtemplate_AsyncOperations](#BKMK_msdyn_dataflowtemplate_AsyncOperations)
- [msdyn_workflowactionstatus_AsyncOperations](#BKMK_msdyn_workflowactionstatus_AsyncOperations)
- [userrating_AsyncOperations](#BKMK_userrating_AsyncOperations)
- [msdyn_mobileapp_AsyncOperations](#BKMK_msdyn_mobileapp_AsyncOperations)
- [msdyn_insightsstorevirtualentity_AsyncOperations](#BKMK_msdyn_insightsstorevirtualentity_AsyncOperations)
- [roleeditorlayout_AsyncOperations](#BKMK_roleeditorlayout_AsyncOperations)
- [appaction_AsyncOperations](#BKMK_appaction_AsyncOperations)
- [appactionmigration_AsyncOperations](#BKMK_appactionmigration_AsyncOperations)
- [appactionrule_AsyncOperations](#BKMK_appactionrule_AsyncOperations)
- [card_AsyncOperations](#BKMK_card_AsyncOperations)
- [msdyn_entitylinkchatconfiguration_AsyncOperations](#BKMK_msdyn_entitylinkchatconfiguration_AsyncOperations)
- [msdyn_richtextfile_AsyncOperations](#BKMK_msdyn_richtextfile_AsyncOperations)
- [msdyn_customcontrolextendedsettings_AsyncOperations](#BKMK_msdyn_customcontrolextendedsettings_AsyncOperations)
- [searchrelationshipsettings_AsyncOperations](#BKMK_searchrelationshipsettings_AsyncOperations)
- [msdyn_virtualtablecolumncandidate_AsyncOperations](#BKMK_msdyn_virtualtablecolumncandidate_AsyncOperations)
- [msdyn_aiconfiguration_AsyncOperations](#BKMK_msdyn_aiconfiguration_AsyncOperations)
- [msdyn_aievent_AsyncOperations](#BKMK_msdyn_aievent_AsyncOperations)
- [msdyn_aimodel_AsyncOperations](#BKMK_msdyn_aimodel_AsyncOperations)
- [msdyn_aitemplate_AsyncOperations](#BKMK_msdyn_aitemplate_AsyncOperations)
- [msdyn_aibfeedbackloop_AsyncOperations](#BKMK_msdyn_aibfeedbackloop_AsyncOperations)
- [msdyn_aifptrainingdocument_AsyncOperations](#BKMK_msdyn_aifptrainingdocument_AsyncOperations)
- [msdyn_aiodimage_AsyncOperations](#BKMK_msdyn_aiodimage_AsyncOperations)
- [msdyn_aiodlabel_AsyncOperations](#BKMK_msdyn_aiodlabel_AsyncOperations)
- [msdyn_aiodtrainingboundingbox_AsyncOperations](#BKMK_msdyn_aiodtrainingboundingbox_AsyncOperations)
- [msdyn_aiodtrainingimage_AsyncOperations](#BKMK_msdyn_aiodtrainingimage_AsyncOperations)
- [msdyn_aibdataset_AsyncOperations](#BKMK_msdyn_aibdataset_AsyncOperations)
- [msdyn_aibdatasetfile_AsyncOperations](#BKMK_msdyn_aibdatasetfile_AsyncOperations)
- [msdyn_aibdatasetrecord_AsyncOperations](#BKMK_msdyn_aibdatasetrecord_AsyncOperations)
- [msdyn_aibdatasetscontainer_AsyncOperations](#BKMK_msdyn_aibdatasetscontainer_AsyncOperations)
- [msdyn_aibfile_AsyncOperations](#BKMK_msdyn_aibfile_AsyncOperations)
- [msdyn_aibfileattacheddata_AsyncOperations](#BKMK_msdyn_aibfileattacheddata_AsyncOperations)
- [msdyn_pmanalysishistory_AsyncOperations](#BKMK_msdyn_pmanalysishistory_AsyncOperations)
- [msdyn_pmcalendar_AsyncOperations](#BKMK_msdyn_pmcalendar_AsyncOperations)
- [msdyn_pmcalendarversion_AsyncOperations](#BKMK_msdyn_pmcalendarversion_AsyncOperations)
- [msdyn_pminferredtask_AsyncOperations](#BKMK_msdyn_pminferredtask_AsyncOperations)
- [msdyn_pmprocessextendedmetadataversion_AsyncOperations](#BKMK_msdyn_pmprocessextendedmetadataversion_AsyncOperations)
- [msdyn_pmprocesstemplate_AsyncOperations](#BKMK_msdyn_pmprocesstemplate_AsyncOperations)
- [msdyn_pmprocessusersettings_AsyncOperations](#BKMK_msdyn_pmprocessusersettings_AsyncOperations)
- [msdyn_pmprocessversion_AsyncOperations](#BKMK_msdyn_pmprocessversion_AsyncOperations)
- [msdyn_pmrecording_AsyncOperations](#BKMK_msdyn_pmrecording_AsyncOperations)
- [msdyn_pmtemplate_AsyncOperations](#BKMK_msdyn_pmtemplate_AsyncOperations)
- [msdyn_pmview_AsyncOperations](#BKMK_msdyn_pmview_AsyncOperations)
- [msdyn_analysiscomponent_AsyncOperations](#BKMK_msdyn_analysiscomponent_AsyncOperations)
- [msdyn_analysisjob_AsyncOperations](#BKMK_msdyn_analysisjob_AsyncOperations)
- [msdyn_analysisoverride_AsyncOperations](#BKMK_msdyn_analysisoverride_AsyncOperations)
- [msdyn_analysisresult_AsyncOperations](#BKMK_msdyn_analysisresult_AsyncOperations)
- [msdyn_analysisresultdetail_AsyncOperations](#BKMK_msdyn_analysisresultdetail_AsyncOperations)
- [msdyn_solutionhealthrule_AsyncOperations](#BKMK_msdyn_solutionhealthrule_AsyncOperations)
- [msdyn_solutionhealthruleargument_AsyncOperations](#BKMK_msdyn_solutionhealthruleargument_AsyncOperations)
- [msdyn_solutionhealthruleset_AsyncOperations](#BKMK_msdyn_solutionhealthruleset_AsyncOperations)
- [powerbidataset_AsyncOperations](#BKMK_powerbidataset_AsyncOperations)
- [powerbimashupparameter_AsyncOperations](#BKMK_powerbimashupparameter_AsyncOperations)
- [powerbireport_AsyncOperations](#BKMK_powerbireport_AsyncOperations)
- [msdyn_fileupload_AsyncOperations](#BKMK_msdyn_fileupload_AsyncOperations)
- [mspcat_catalogsubmissionfiles_AsyncOperations](#BKMK_mspcat_catalogsubmissionfiles_AsyncOperations)
- [mspcat_packagestore_AsyncOperations](#BKMK_mspcat_packagestore_AsyncOperations)
- [msdyn_schedule_AsyncOperations](#BKMK_msdyn_schedule_AsyncOperations)
- [msdyn_dataflow_datalakefolder_AsyncOperations](#BKMK_msdyn_dataflow_datalakefolder_AsyncOperations)
- [msdyn_dmsrequest_AsyncOperations](#BKMK_msdyn_dmsrequest_AsyncOperations)
- [msdyn_dmsrequeststatus_AsyncOperations](#BKMK_msdyn_dmsrequeststatus_AsyncOperations)
- [searchattributesettings_AsyncOperations](#BKMK_searchattributesettings_AsyncOperations)
- [searchcustomanalyzer_AsyncOperations](#BKMK_searchcustomanalyzer_AsyncOperations)


### <a name="BKMK_theme_AsyncOperations"></a> theme_AsyncOperations

See the [theme_AsyncOperations](theme.md#BKMK_theme_AsyncOperations) one-to-many relationship for the [theme](theme.md) table/entity.

### <a name="BKMK_usermapping_AsyncOperations"></a> usermapping_AsyncOperations

See the [usermapping_AsyncOperations](usermapping.md#BKMK_usermapping_AsyncOperations) one-to-many relationship for the [usermapping](usermapping.md) table/entity.

### <a name="BKMK_interactionforemail_AsyncOperations"></a> interactionforemail_AsyncOperations

See the [interactionforemail_AsyncOperations](interactionforemail.md#BKMK_interactionforemail_AsyncOperations) one-to-many relationship for the [interactionforemail](interactionforemail.md) table/entity.

### <a name="BKMK_knowledgearticle_AsyncOperations"></a> knowledgearticle_AsyncOperations

See the [knowledgearticle_AsyncOperations](knowledgearticle.md#BKMK_knowledgearticle_AsyncOperations) one-to-many relationship for the [knowledgearticle](knowledgearticle.md) table/entity.

### <a name="BKMK_post_AsyncOperations"></a> post_AsyncOperations

See the [post_AsyncOperations](post.md#BKMK_post_AsyncOperations) one-to-many relationship for the [post](post.md) table/entity.

### <a name="BKMK_position_AsyncOperations"></a> position_AsyncOperations

See the [position_AsyncOperations](position.md#BKMK_position_AsyncOperations) one-to-many relationship for the [position](position.md) table/entity.

### <a name="BKMK_KnowledgeBaseRecord_AsyncOperations"></a> KnowledgeBaseRecord_AsyncOperations

See the [KnowledgeBaseRecord_AsyncOperations](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_AsyncOperations) one-to-many relationship for the [knowledgebaserecord](knowledgebaserecord.md) table/entity.

### <a name="BKMK_lk_asyncoperation_createdby"></a> lk_asyncoperation_createdby

See the [lk_asyncoperation_createdby](systemuser.md#BKMK_lk_asyncoperation_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_MonthlyFiscalCalendar_AsyncOperations"></a> MonthlyFiscalCalendar_AsyncOperations

See the [MonthlyFiscalCalendar_AsyncOperations](monthlyfiscalcalendar.md#BKMK_MonthlyFiscalCalendar_AsyncOperations) one-to-many relationship for the [monthlyfiscalcalendar](monthlyfiscalcalendar.md) table/entity.

### <a name="BKMK_lk_asyncoperation_workflowactivationid"></a> lk_asyncoperation_workflowactivationid

See the [lk_asyncoperation_workflowactivationid](workflow.md#BKMK_lk_asyncoperation_workflowactivationid) one-to-many relationship for the [workflow](workflow.md) table/entity.

### <a name="BKMK_Report_AsyncOperations"></a> Report_AsyncOperations

See the [Report_AsyncOperations](report.md#BKMK_Report_AsyncOperations) one-to-many relationship for the [report](report.md) table/entity.

### <a name="BKMK_SocialActivity_AsyncOperations"></a> SocialActivity_AsyncOperations

See the [SocialActivity_AsyncOperations](socialactivity.md#BKMK_SocialActivity_AsyncOperations) one-to-many relationship for the [socialactivity](socialactivity.md) table/entity.

### <a name="BKMK_Connection_Role_AsyncOperations"></a> Connection_Role_AsyncOperations

See the [Connection_Role_AsyncOperations](connectionrole.md#BKMK_Connection_Role_AsyncOperations) one-to-many relationship for the [connectionrole](connectionrole.md) table/entity.

### <a name="BKMK_Team_AsyncOperations"></a> Team_AsyncOperations

See the [Team_AsyncOperations](team.md#BKMK_Team_AsyncOperations) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_AnnualFiscalCalendar_AsyncOperations"></a> AnnualFiscalCalendar_AsyncOperations

See the [AnnualFiscalCalendar_AsyncOperations](annualfiscalcalendar.md#BKMK_AnnualFiscalCalendar_AsyncOperations) one-to-many relationship for the [annualfiscalcalendar](annualfiscalcalendar.md) table/entity.

### <a name="BKMK_SharePointDocumentLocation_AsyncOperations"></a> SharePointDocumentLocation_AsyncOperations

See the [SharePointDocumentLocation_AsyncOperations](sharepointdocumentlocation.md#BKMK_SharePointDocumentLocation_AsyncOperations) one-to-many relationship for the [sharepointdocumentlocation](sharepointdocumentlocation.md) table/entity.

### <a name="BKMK_PhoneCall_AsyncOperations"></a> PhoneCall_AsyncOperations

See the [PhoneCall_AsyncOperations](phonecall.md#BKMK_PhoneCall_AsyncOperations) one-to-many relationship for the [phonecall](phonecall.md) table/entity.

### <a name="BKMK_mailbox_asyncoperations"></a> mailbox_asyncoperations

See the [mailbox_asyncoperations](mailbox.md#BKMK_mailbox_asyncoperations) one-to-many relationship for the [mailbox](mailbox.md) table/entity.

### <a name="BKMK_PostFollow_AsyncOperations"></a> PostFollow_AsyncOperations

See the [PostFollow_AsyncOperations](postfollow.md#BKMK_PostFollow_AsyncOperations) one-to-many relationship for the [postfollow](postfollow.md) table/entity.

### <a name="BKMK_Appointment_AsyncOperations"></a> Appointment_AsyncOperations

See the [Appointment_AsyncOperations](appointment.md#BKMK_Appointment_AsyncOperations) one-to-many relationship for the [appointment](appointment.md) table/entity.

### <a name="BKMK_slabase_AsyncOperations"></a> slabase_AsyncOperations

See the [slabase_AsyncOperations](sla.md#BKMK_slabase_AsyncOperations) one-to-many relationship for the [sla](sla.md) table/entity.

### <a name="BKMK_SavedQuery_AsyncOperations"></a> SavedQuery_AsyncOperations

See the [SavedQuery_AsyncOperations](savedquery.md#BKMK_SavedQuery_AsyncOperations) one-to-many relationship for the [savedquery](savedquery.md) table/entity.

### <a name="BKMK_DisplayString_AsyncOperations"></a> DisplayString_AsyncOperations

See the [DisplayString_AsyncOperations](displaystring.md#BKMK_DisplayString_AsyncOperations) one-to-many relationship for the [displaystring](displaystring.md) table/entity.

### <a name="BKMK_KbArticleComment_AsyncOperations"></a> KbArticleComment_AsyncOperations

See the [KbArticleComment_AsyncOperations](kbarticlecomment.md#BKMK_KbArticleComment_AsyncOperations) one-to-many relationship for the [kbarticlecomment](kbarticlecomment.md) table/entity.

### <a name="BKMK_ActivityPointer_AsyncOperations"></a> ActivityPointer_AsyncOperations

See the [ActivityPointer_AsyncOperations](activitypointer.md#BKMK_ActivityPointer_AsyncOperations) one-to-many relationship for the [activitypointer](activitypointer.md) table/entity.

### <a name="BKMK_Subject_AsyncOperations"></a> Subject_AsyncOperations

See the [Subject_AsyncOperations](subject.md#BKMK_Subject_AsyncOperations) one-to-many relationship for the [subject](subject.md) table/entity.

### <a name="BKMK_goalrollupquery_AsyncOperations"></a> goalrollupquery_AsyncOperations

See the [goalrollupquery_AsyncOperations](goalrollupquery.md#BKMK_goalrollupquery_AsyncOperations) one-to-many relationship for the [goalrollupquery](goalrollupquery.md) table/entity.

### <a name="BKMK_Role_AsyncOperations"></a> Role_AsyncOperations

See the [Role_AsyncOperations](role.md#BKMK_Role_AsyncOperations) one-to-many relationship for the [role](role.md) table/entity.

### <a name="BKMK_SystemForm_AsyncOperations"></a> SystemForm_AsyncOperations

See the [SystemForm_AsyncOperations](systemform.md#BKMK_SystemForm_AsyncOperations) one-to-many relationship for the [systemform](systemform.md) table/entity.

### <a name="BKMK_Annotation_AsyncOperations"></a> Annotation_AsyncOperations

See the [Annotation_AsyncOperations](annotation.md#BKMK_Annotation_AsyncOperations) one-to-many relationship for the [annotation](annotation.md) table/entity.

### <a name="BKMK_Privilege_AsyncOperations"></a> Privilege_AsyncOperations

See the [Privilege_AsyncOperations](privilege.md#BKMK_Privilege_AsyncOperations) one-to-many relationship for the [privilege](privilege.md) table/entity.

### <a name="BKMK_ActivityMimeAttachment_AsyncOperations"></a> ActivityMimeAttachment_AsyncOperations

See the [ActivityMimeAttachment_AsyncOperations](activitymimeattachment.md#BKMK_ActivityMimeAttachment_AsyncOperations) one-to-many relationship for the [activitymimeattachment](activitymimeattachment.md) table/entity.

### <a name="BKMK_Goal_AsyncOperations"></a> Goal_AsyncOperations

See the [Goal_AsyncOperations](goal.md#BKMK_Goal_AsyncOperations) one-to-many relationship for the [goal](goal.md) table/entity.

### <a name="BKMK_Fax_AsyncOperations"></a> Fax_AsyncOperations

See the [Fax_AsyncOperations](fax.md#BKMK_Fax_AsyncOperations) one-to-many relationship for the [fax](fax.md) table/entity.

### <a name="BKMK_QuarterlyFiscalCalendar_AsyncOperations"></a> QuarterlyFiscalCalendar_AsyncOperations

See the [QuarterlyFiscalCalendar_AsyncOperations](quarterlyfiscalcalendar.md#BKMK_QuarterlyFiscalCalendar_AsyncOperations) one-to-many relationship for the [quarterlyfiscalcalendar](quarterlyfiscalcalendar.md) table/entity.

### <a name="BKMK_SharePointSite_AsyncOperations"></a> SharePointSite_AsyncOperations

See the [SharePointSite_AsyncOperations](sharepointsite.md#BKMK_SharePointSite_AsyncOperations) one-to-many relationship for the [sharepointsite](sharepointsite.md) table/entity.

### <a name="BKMK_UserQuery_AsyncOperations"></a> UserQuery_AsyncOperations

See the [UserQuery_AsyncOperations](userquery.md#BKMK_UserQuery_AsyncOperations) one-to-many relationship for the [userquery](userquery.md) table/entity.

### <a name="BKMK_ImportMap_AsyncOperations"></a> ImportMap_AsyncOperations

See the [ImportMap_AsyncOperations](importmap.md#BKMK_ImportMap_AsyncOperations) one-to-many relationship for the [importmap](importmap.md) table/entity.

### <a name="BKMK_BusinessUnit_AsyncOperations"></a> BusinessUnit_AsyncOperations

See the [BusinessUnit_AsyncOperations](businessunit.md#BKMK_BusinessUnit_AsyncOperations) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_Queue_AsyncOperations"></a> Queue_AsyncOperations

See the [Queue_AsyncOperations](queue.md#BKMK_Queue_AsyncOperations) one-to-many relationship for the [queue](queue.md) table/entity.

### <a name="BKMK_QueueItem_AsyncOperations"></a> QueueItem_AsyncOperations

See the [QueueItem_AsyncOperations](queueitem.md#BKMK_QueueItem_AsyncOperations) one-to-many relationship for the [queueitem](queueitem.md) table/entity.

### <a name="BKMK_team_asyncoperation"></a> team_asyncoperation

See the [team_asyncoperation](team.md#BKMK_team_asyncoperation) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_lk_asyncoperation_modifiedby"></a> lk_asyncoperation_modifiedby

See the [lk_asyncoperation_modifiedby](systemuser.md#BKMK_lk_asyncoperation_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_UserForm_AsyncOperations"></a> UserForm_AsyncOperations

See the [UserForm_AsyncOperations](userform.md#BKMK_UserForm_AsyncOperations) one-to-many relationship for the [userform](userform.md) table/entity.

### <a name="BKMK_TransactionCurrency_AsyncOperations"></a> TransactionCurrency_AsyncOperations

See the [TransactionCurrency_AsyncOperations](transactioncurrency.md#BKMK_TransactionCurrency_AsyncOperations) one-to-many relationship for the [transactioncurrency](transactioncurrency.md) table/entity.

### <a name="BKMK_rollupfield_AsyncOperations"></a> rollupfield_AsyncOperations

See the [rollupfield_AsyncOperations](rollupfield.md#BKMK_rollupfield_AsyncOperations) one-to-many relationship for the [rollupfield](rollupfield.md) table/entity.

### <a name="BKMK_Letter_AsyncOperations"></a> Letter_AsyncOperations

See the [Letter_AsyncOperations](letter.md#BKMK_Letter_AsyncOperations) one-to-many relationship for the [letter](letter.md) table/entity.

### <a name="BKMK_KbArticle_AsyncOperations"></a> KbArticle_AsyncOperations

See the [KbArticle_AsyncOperations](kbarticle.md#BKMK_KbArticle_AsyncOperations) one-to-many relationship for the [kbarticle](kbarticle.md) table/entity.

### <a name="BKMK_RecurringAppointmentMaster_AsyncOperations"></a> RecurringAppointmentMaster_AsyncOperations

See the [RecurringAppointmentMaster_AsyncOperations](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_AsyncOperations) one-to-many relationship for the [recurringappointmentmaster](recurringappointmentmaster.md) table/entity.

### <a name="BKMK_Task_AsyncOperations"></a> Task_AsyncOperations

See the [Task_AsyncOperations](task.md#BKMK_Task_AsyncOperations) one-to-many relationship for the [task](task.md) table/entity.

### <a name="BKMK_BusinessUnitNewsArticle_AsyncOperations"></a> BusinessUnitNewsArticle_AsyncOperations

See the [BusinessUnitNewsArticle_AsyncOperations](businessunitnewsarticle.md#BKMK_BusinessUnitNewsArticle_AsyncOperations) one-to-many relationship for the [businessunitnewsarticle](businessunitnewsarticle.md) table/entity.

### <a name="BKMK_Connection_AsyncOperations"></a> Connection_AsyncOperations

See the [Connection_AsyncOperations](connection.md#BKMK_Connection_AsyncOperations) one-to-many relationship for the [connection](connection.md) table/entity.

### <a name="BKMK_SystemUser_AsyncOperations"></a> SystemUser_AsyncOperations

See the [SystemUser_AsyncOperations](systemuser.md#BKMK_SystemUser_AsyncOperations) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_KbArticleTemplate_AsyncOperations"></a> KbArticleTemplate_AsyncOperations

See the [KbArticleTemplate_AsyncOperations](kbarticletemplate.md#BKMK_KbArticleTemplate_AsyncOperations) one-to-many relationship for the [kbarticletemplate](kbarticletemplate.md) table/entity.

### <a name="BKMK_SdkMessageProcessingStep_AsyncOperations"></a> SdkMessageProcessingStep_AsyncOperations

See the [SdkMessageProcessingStep_AsyncOperations](sdkmessageprocessingstep.md#BKMK_SdkMessageProcessingStep_AsyncOperations) one-to-many relationship for the [sdkmessageprocessingstep](sdkmessageprocessingstep.md) table/entity.

### <a name="BKMK_Template_AsyncOperations"></a> Template_AsyncOperations

See the [Template_AsyncOperations](template.md#BKMK_Template_AsyncOperations) one-to-many relationship for the [template](template.md) table/entity.

### <a name="BKMK_CustomerAddress_AsyncOperations"></a> CustomerAddress_AsyncOperations

See the [CustomerAddress_AsyncOperations](customeraddress.md#BKMK_CustomerAddress_AsyncOperations) one-to-many relationship for the [customeraddress](customeraddress.md) table/entity.

### <a name="BKMK_Contact_AsyncOperations"></a> Contact_AsyncOperations

See the [Contact_AsyncOperations](contact.md#BKMK_Contact_AsyncOperations) one-to-many relationship for the [contact](contact.md) table/entity.

### <a name="BKMK_emailserverprofile_asyncoperations"></a> emailserverprofile_asyncoperations

See the [emailserverprofile_asyncoperations](emailserverprofile.md#BKMK_emailserverprofile_asyncoperations) one-to-many relationship for the [emailserverprofile](emailserverprofile.md) table/entity.

### <a name="BKMK_lk_asyncoperation_createdonbehalfby"></a> lk_asyncoperation_createdonbehalfby

See the [lk_asyncoperation_createdonbehalfby](systemuser.md#BKMK_lk_asyncoperation_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_Import_AsyncOperations"></a> Import_AsyncOperations

See the [Import_AsyncOperations](import.md#BKMK_Import_AsyncOperations) one-to-many relationship for the [import](import.md) table/entity.

### <a name="BKMK_system_user_asyncoperation"></a> system_user_asyncoperation

See the [system_user_asyncoperation](systemuser.md#BKMK_system_user_asyncoperation) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_business_unit_asyncoperation"></a> business_unit_asyncoperation

See the [business_unit_asyncoperation](businessunit.md#BKMK_business_unit_asyncoperation) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_ImportLog_AsyncOperations"></a> ImportLog_AsyncOperations

See the [ImportLog_AsyncOperations](importlog.md#BKMK_ImportLog_AsyncOperations) one-to-many relationship for the [importlog](importlog.md) table/entity.

### <a name="BKMK_metric_AsyncOperations"></a> metric_AsyncOperations

See the [metric_AsyncOperations](metric.md#BKMK_metric_AsyncOperations) one-to-many relationship for the [metric](metric.md) table/entity.

### <a name="BKMK_SocialProfile_AsyncOperations"></a> SocialProfile_AsyncOperations

See the [SocialProfile_AsyncOperations](socialprofile.md#BKMK_SocialProfile_AsyncOperations) one-to-many relationship for the [socialprofile](socialprofile.md) table/entity.

### <a name="BKMK_lk_asyncoperation_modifiedonbehalfby"></a> lk_asyncoperation_modifiedonbehalfby

See the [lk_asyncoperation_modifiedonbehalfby](systemuser.md#BKMK_lk_asyncoperation_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_Account_AsyncOperations"></a> Account_AsyncOperations

See the [Account_AsyncOperations](account.md#BKMK_Account_AsyncOperations) one-to-many relationship for the [account](account.md) table/entity.

### <a name="BKMK_Email_AsyncOperations"></a> Email_AsyncOperations

See the [Email_AsyncOperations](email.md#BKMK_Email_AsyncOperations) one-to-many relationship for the [email](email.md) table/entity.

### <a name="BKMK_FixedMonthlyFiscalCalendar_AsyncOperations"></a> FixedMonthlyFiscalCalendar_AsyncOperations

See the [FixedMonthlyFiscalCalendar_AsyncOperations](fixedmonthlyfiscalcalendar.md#BKMK_FixedMonthlyFiscalCalendar_AsyncOperations) one-to-many relationship for the [fixedmonthlyfiscalcalendar](fixedmonthlyfiscalcalendar.md) table/entity.

### <a name="BKMK_SemiAnnualFiscalCalendar_AsyncOperations"></a> SemiAnnualFiscalCalendar_AsyncOperations

See the [SemiAnnualFiscalCalendar_AsyncOperations](semiannualfiscalcalendar.md#BKMK_SemiAnnualFiscalCalendar_AsyncOperations) one-to-many relationship for the [semiannualfiscalcalendar](semiannualfiscalcalendar.md) table/entity.

### <a name="BKMK_MailMergeTemplate_AsyncOperations"></a> MailMergeTemplate_AsyncOperations

See the [MailMergeTemplate_AsyncOperations](mailmergetemplate.md#BKMK_MailMergeTemplate_AsyncOperations) one-to-many relationship for the [mailmergetemplate](mailmergetemplate.md) table/entity.

### <a name="BKMK_Organization_AsyncOperations"></a> Organization_AsyncOperations

See the [Organization_AsyncOperations](organization.md#BKMK_Organization_AsyncOperations) one-to-many relationship for the [organization](organization.md) table/entity.

### <a name="BKMK_Calendar_AsyncOperations"></a> Calendar_AsyncOperations

See the [Calendar_AsyncOperations](calendar.md#BKMK_Calendar_AsyncOperations) one-to-many relationship for the [calendar](calendar.md) table/entity.

### <a name="BKMK_ImportFile_AsyncOperations"></a> ImportFile_AsyncOperations

See the [ImportFile_AsyncOperations](importfile.md#BKMK_ImportFile_AsyncOperations) one-to-many relationship for the [importfile](importfile.md) table/entity.

### <a name="BKMK_solutioncomponentattributeconfiguration_AsyncOperations"></a> solutioncomponentattributeconfiguration_AsyncOperations

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentattributeconfiguration_AsyncOperations](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_AsyncOperations) one-to-many relationship for the [solutioncomponentattributeconfiguration](solutioncomponentattributeconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentbatchconfiguration_AsyncOperations"></a> solutioncomponentbatchconfiguration_AsyncOperations

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentbatchconfiguration_AsyncOperations](solutioncomponentbatchconfiguration.md#BKMK_solutioncomponentbatchconfiguration_AsyncOperations) one-to-many relationship for the [solutioncomponentbatchconfiguration](solutioncomponentbatchconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentconfiguration_AsyncOperations"></a> solutioncomponentconfiguration_AsyncOperations

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentconfiguration_AsyncOperations](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_AsyncOperations) one-to-many relationship for the [solutioncomponentconfiguration](solutioncomponentconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentrelationshipconfiguration_AsyncOperations"></a> solutioncomponentrelationshipconfiguration_AsyncOperations

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentrelationshipconfiguration_AsyncOperations](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_AsyncOperations) one-to-many relationship for the [solutioncomponentrelationshipconfiguration](solutioncomponentrelationshipconfiguration.md) table/entity.

### <a name="BKMK_package_AsyncOperations"></a> package_AsyncOperations

**Added by**: msdyn_SolutionPackageMapping Solution

See the [package_AsyncOperations](package.md#BKMK_package_AsyncOperations) one-to-many relationship for the [package](package.md) table/entity.

### <a name="BKMK_stagesolutionupload_AsyncOperations"></a> stagesolutionupload_AsyncOperations

**Added by**: StageSolutionUpload Solution

See the [stagesolutionupload_AsyncOperations](stagesolutionupload.md#BKMK_stagesolutionupload_AsyncOperations) one-to-many relationship for the [stagesolutionupload](stagesolutionupload.md) table/entity.

### <a name="BKMK_exportsolutionupload_AsyncOperations"></a> exportsolutionupload_AsyncOperations

**Added by**: ExportSolutionUpload Solution

See the [exportsolutionupload_AsyncOperations](exportsolutionupload.md#BKMK_exportsolutionupload_AsyncOperations) one-to-many relationship for the [exportsolutionupload](exportsolutionupload.md) table/entity.

### <a name="BKMK_featurecontrolsetting_AsyncOperations"></a> featurecontrolsetting_AsyncOperations

**Added by**: msdyn_FeatureControlSetting Solution

See the [featurecontrolsetting_AsyncOperations](featurecontrolsetting.md#BKMK_featurecontrolsetting_AsyncOperations) one-to-many relationship for the [featurecontrolsetting](featurecontrolsetting.md) table/entity.

### <a name="BKMK_attributeimageconfig_AsyncOperations"></a> attributeimageconfig_AsyncOperations

**Added by**: Image Configuration Solution

See the [attributeimageconfig_AsyncOperations](attributeimageconfig.md#BKMK_attributeimageconfig_AsyncOperations) one-to-many relationship for the [attributeimageconfig](attributeimageconfig.md) table/entity.

### <a name="BKMK_entityimageconfig_AsyncOperations"></a> entityimageconfig_AsyncOperations

**Added by**: Image Configuration Solution

See the [entityimageconfig_AsyncOperations](entityimageconfig.md#BKMK_entityimageconfig_AsyncOperations) one-to-many relationship for the [entityimageconfig](entityimageconfig.md) table/entity.

### <a name="BKMK_relationshipattribute_AsyncOperations"></a> relationshipattribute_AsyncOperations

**Added by**: Metadata Extension Solution

See the [relationshipattribute_AsyncOperations](relationshipattribute.md#BKMK_relationshipattribute_AsyncOperations) one-to-many relationship for the [relationshipattribute](relationshipattribute.md) table/entity.

### <a name="BKMK_stagedentity_AsyncOperations"></a> stagedentity_AsyncOperations

**Added by**: Metadata Extension Solution

See the [stagedentity_AsyncOperations](stagedentity.md#BKMK_stagedentity_AsyncOperations) one-to-many relationship for the [stagedentity](stagedentity.md) table/entity.

### <a name="BKMK_stagedentityattribute_AsyncOperations"></a> stagedentityattribute_AsyncOperations

**Added by**: Metadata Extension Solution

See the [stagedentityattribute_AsyncOperations](stagedentityattribute.md#BKMK_stagedentityattribute_AsyncOperations) one-to-many relationship for the [stagedentityattribute](stagedentityattribute.md) table/entity.

### <a name="BKMK_catalog_AsyncOperations"></a> catalog_AsyncOperations

**Added by**: CatalogFramework Solution

See the [catalog_AsyncOperations](catalog.md#BKMK_catalog_AsyncOperations) one-to-many relationship for the [catalog](catalog.md) table/entity.

### <a name="BKMK_catalogassignment_AsyncOperations"></a> catalogassignment_AsyncOperations

**Added by**: CatalogFramework Solution

See the [catalogassignment_AsyncOperations](catalogassignment.md#BKMK_catalogassignment_AsyncOperations) one-to-many relationship for the [catalogassignment](catalogassignment.md) table/entity.

### <a name="BKMK_customapi_AsyncOperations"></a> customapi_AsyncOperations

**Added by**: Custom API Framework Solution

See the [customapi_AsyncOperations](customapi.md#BKMK_customapi_AsyncOperations) one-to-many relationship for the [customapi](customapi.md) table/entity.

### <a name="BKMK_customapirequestparameter_AsyncOperations"></a> customapirequestparameter_AsyncOperations

**Added by**: Custom API Framework Solution

See the [customapirequestparameter_AsyncOperations](customapirequestparameter.md#BKMK_customapirequestparameter_AsyncOperations) one-to-many relationship for the [customapirequestparameter](customapirequestparameter.md) table/entity.

### <a name="BKMK_customapiresponseproperty_AsyncOperations"></a> customapiresponseproperty_AsyncOperations

**Added by**: Custom API Framework Solution

See the [customapiresponseproperty_AsyncOperations](customapiresponseproperty.md#BKMK_customapiresponseproperty_AsyncOperations) one-to-many relationship for the [customapiresponseproperty](customapiresponseproperty.md) table/entity.

### <a name="BKMK_provisionlanguageforuser_AsyncOperations"></a> provisionlanguageforuser_AsyncOperations

**Added by**: msft_LocalizationExtension Solution

See the [provisionlanguageforuser_AsyncOperations](provisionlanguageforuser.md#BKMK_provisionlanguageforuser_AsyncOperations) one-to-many relationship for the [provisionlanguageforuser](provisionlanguageforuser.md) table/entity.

### <a name="BKMK_sharedobject_AsyncOperations"></a> sharedobject_AsyncOperations

**Added by**: Real-time Collaboration App Solution

See the [sharedobject_AsyncOperations](sharedobject.md#BKMK_sharedobject_AsyncOperations) one-to-many relationship for the [sharedobject](sharedobject.md) table/entity.

### <a name="BKMK_sharedworkspace_AsyncOperations"></a> sharedworkspace_AsyncOperations

**Added by**: Real-time Collaboration App Solution

See the [sharedworkspace_AsyncOperations](sharedworkspace.md#BKMK_sharedworkspace_AsyncOperations) one-to-many relationship for the [sharedworkspace](sharedworkspace.md) table/entity.

### <a name="BKMK_sharedworkspacepool_AsyncOperations"></a> sharedworkspacepool_AsyncOperations

**Added by**: Real-time Collaboration App Solution

See the [sharedworkspacepool_AsyncOperations](sharedworkspacepool.md#BKMK_sharedworkspacepool_AsyncOperations) one-to-many relationship for the [sharedworkspacepool](sharedworkspacepool.md) table/entity.

### <a name="BKMK_entityanalyticsconfig_AsyncOperations"></a> entityanalyticsconfig_AsyncOperations

**Added by**: Advanced Analytics Infrastructure Solution

See the [entityanalyticsconfig_AsyncOperations](entityanalyticsconfig.md#BKMK_entityanalyticsconfig_AsyncOperations) one-to-many relationship for the [entityanalyticsconfig](entityanalyticsconfig.md) table/entity.

### <a name="BKMK_datalakefolder_AsyncOperations"></a> datalakefolder_AsyncOperations

**Added by**: Data lake workspaces Solution

See the [datalakefolder_AsyncOperations](datalakefolder.md#BKMK_datalakefolder_AsyncOperations) one-to-many relationship for the [datalakefolder](datalakefolder.md) table/entity.

### <a name="BKMK_datalakefolderpermission_AsyncOperations"></a> datalakefolderpermission_AsyncOperations

**Added by**: Data lake workspaces Solution

See the [datalakefolderpermission_AsyncOperations](datalakefolderpermission.md#BKMK_datalakefolderpermission_AsyncOperations) one-to-many relationship for the [datalakefolderpermission](datalakefolderpermission.md) table/entity.

### <a name="BKMK_datalakeworkspace_AsyncOperations"></a> datalakeworkspace_AsyncOperations

**Added by**: Data lake workspaces Solution

See the [datalakeworkspace_AsyncOperations](datalakeworkspace.md#BKMK_datalakeworkspace_AsyncOperations) one-to-many relationship for the [datalakeworkspace](datalakeworkspace.md) table/entity.

### <a name="BKMK_datalakeworkspacepermission_AsyncOperations"></a> datalakeworkspacepermission_AsyncOperations

**Added by**: Data lake workspaces Solution

See the [datalakeworkspacepermission_AsyncOperations](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_AsyncOperations) one-to-many relationship for the [datalakeworkspacepermission](datalakeworkspacepermission.md) table/entity.

### <a name="BKMK_dataprocessingconfiguration_AsyncOperations"></a> dataprocessingconfiguration_AsyncOperations

**Added by**: Data lake workspaces Solution

See the [dataprocessingconfiguration_AsyncOperations](dataprocessingconfiguration.md#BKMK_dataprocessingconfiguration_AsyncOperations) one-to-many relationship for the [dataprocessingconfiguration](dataprocessingconfiguration.md) table/entity.

### <a name="BKMK_exportedexcel_AsyncOperations"></a> exportedexcel_AsyncOperations

**Added by**: Data lake workspaces Solution

See the [exportedexcel_AsyncOperations](exportedexcel.md#BKMK_exportedexcel_AsyncOperations) one-to-many relationship for the [exportedexcel](exportedexcel.md) table/entity.

### <a name="BKMK_retaineddataexcel_AsyncOperations"></a> retaineddataexcel_AsyncOperations

**Added by**: Data lake workspaces Solution

See the [retaineddataexcel_AsyncOperations](retaineddataexcel.md#BKMK_retaineddataexcel_AsyncOperations) one-to-many relationship for the [retaineddataexcel](retaineddataexcel.md) table/entity.

### <a name="BKMK_synapsedatabase_AsyncOperations"></a> synapsedatabase_AsyncOperations

**Added by**: Data lake workspaces Solution

See the [synapsedatabase_AsyncOperations](synapsedatabase.md#BKMK_synapsedatabase_AsyncOperations) one-to-many relationship for the [synapsedatabase](synapsedatabase.md) table/entity.

### <a name="BKMK_synapselinkexternaltablestate_AsyncOperations"></a> synapselinkexternaltablestate_AsyncOperations

**Added by**: Synapse Link Solution

See the [synapselinkexternaltablestate_AsyncOperations](synapselinkexternaltablestate.md#BKMK_synapselinkexternaltablestate_AsyncOperations) one-to-many relationship for the [synapselinkexternaltablestate](synapselinkexternaltablestate.md) table/entity.

### <a name="BKMK_synapselinkprofile_AsyncOperations"></a> synapselinkprofile_AsyncOperations

**Added by**: Synapse Link Solution

See the [synapselinkprofile_AsyncOperations](synapselinkprofile.md#BKMK_synapselinkprofile_AsyncOperations) one-to-many relationship for the [synapselinkprofile](synapselinkprofile.md) table/entity.

### <a name="BKMK_synapselinkprofileentity_AsyncOperations"></a> synapselinkprofileentity_AsyncOperations

**Added by**: Synapse Link Solution

See the [synapselinkprofileentity_AsyncOperations](synapselinkprofileentity.md#BKMK_synapselinkprofileentity_AsyncOperations) one-to-many relationship for the [synapselinkprofileentity](synapselinkprofileentity.md) table/entity.

### <a name="BKMK_synapselinkprofileentitystate_AsyncOperations"></a> synapselinkprofileentitystate_AsyncOperations

**Added by**: Synapse Link Solution

See the [synapselinkprofileentitystate_AsyncOperations](synapselinkprofileentitystate.md#BKMK_synapselinkprofileentitystate_AsyncOperations) one-to-many relationship for the [synapselinkprofileentitystate](synapselinkprofileentitystate.md) table/entity.

### <a name="BKMK_synapselinkschedule_AsyncOperations"></a> synapselinkschedule_AsyncOperations

**Added by**: Synapse Link Solution

See the [synapselinkschedule_AsyncOperations](synapselinkschedule.md#BKMK_synapselinkschedule_AsyncOperations) one-to-many relationship for the [synapselinkschedule](synapselinkschedule.md) table/entity.

### <a name="BKMK_msdyn_dataflow_AsyncOperations"></a> msdyn_dataflow_AsyncOperations

**Added by**: Dataflow Solution Solution

See the [msdyn_dataflow_AsyncOperations](msdyn_dataflow.md#BKMK_msdyn_dataflow_AsyncOperations) one-to-many relationship for the [msdyn_dataflow](msdyn_dataflow.md) table/entity.

### <a name="BKMK_msdyn_dataflowrefreshhistory_AsyncOperations"></a> msdyn_dataflowrefreshhistory_AsyncOperations

**Added by**: Dataflow Solution Solution

See the [msdyn_dataflowrefreshhistory_AsyncOperations](msdyn_dataflowrefreshhistory.md#BKMK_msdyn_dataflowrefreshhistory_AsyncOperations) one-to-many relationship for the [msdyn_dataflowrefreshhistory](msdyn_dataflowrefreshhistory.md) table/entity.

### <a name="BKMK_msdyn_entityrefreshhistory_AsyncOperations"></a> msdyn_entityrefreshhistory_AsyncOperations

**Added by**: Dataflow Solution Solution

See the [msdyn_entityrefreshhistory_AsyncOperations](msdyn_entityrefreshhistory.md#BKMK_msdyn_entityrefreshhistory_AsyncOperations) one-to-many relationship for the [msdyn_entityrefreshhistory](msdyn_entityrefreshhistory.md) table/entity.

### <a name="BKMK_sharedlinksetting_AsyncOperations"></a> sharedlinksetting_AsyncOperations

**Added by**: Access Team Solution

See the [sharedlinksetting_AsyncOperations](sharedlinksetting.md#BKMK_sharedlinksetting_AsyncOperations) one-to-many relationship for the [sharedlinksetting](sharedlinksetting.md) table/entity.

### <a name="BKMK_entityrecordfilter_AsyncOperations"></a> entityrecordfilter_AsyncOperations

**Added by**: AuthorizationCore Solution

See the [entityrecordfilter_AsyncOperations](entityrecordfilter.md#BKMK_entityrecordfilter_AsyncOperations) one-to-many relationship for the [entityrecordfilter](entityrecordfilter.md) table/entity.

### <a name="BKMK_recordfilter_AsyncOperations"></a> recordfilter_AsyncOperations

**Added by**: AuthorizationCore Solution

See the [recordfilter_AsyncOperations](recordfilter.md#BKMK_recordfilter_AsyncOperations) one-to-many relationship for the [recordfilter](recordfilter.md) table/entity.

### <a name="BKMK_delegatedauthorization_AsyncOperations"></a> delegatedauthorization_AsyncOperations

**Added by**: Delegated Authorization Solution

See the [delegatedauthorization_AsyncOperations](delegatedauthorization.md#BKMK_delegatedauthorization_AsyncOperations) one-to-many relationship for the [delegatedauthorization](delegatedauthorization.md) table/entity.

### <a name="BKMK_serviceplan_AsyncOperations"></a> serviceplan_AsyncOperations

**Added by**: License Enforcement Solution

See the [serviceplan_AsyncOperations](serviceplan.md#BKMK_serviceplan_AsyncOperations) one-to-many relationship for the [serviceplan](serviceplan.md) table/entity.

### <a name="BKMK_serviceplanmapping_AsyncOperations"></a> serviceplanmapping_AsyncOperations

**Added by**: License Enforcement Solution

See the [serviceplanmapping_AsyncOperations](serviceplanmapping.md#BKMK_serviceplanmapping_AsyncOperations) one-to-many relationship for the [serviceplanmapping](serviceplanmapping.md) table/entity.

### <a name="BKMK_applicationuser_AsyncOperations"></a> applicationuser_AsyncOperations

**Added by**: ApplicationUserSolution Solution

See the [applicationuser_AsyncOperations](applicationuser.md#BKMK_applicationuser_AsyncOperations) one-to-many relationship for the [applicationuser](applicationuser.md) table/entity.

### <a name="BKMK_connector_AsyncOperations"></a> connector_AsyncOperations

**Added by**: Power Connector Solution Solution

See the [connector_AsyncOperations](connector.md#BKMK_connector_AsyncOperations) one-to-many relationship for the [connector](connector.md) table/entity.

### <a name="BKMK_environmentvariabledefinition_AsyncOperations"></a> environmentvariabledefinition_AsyncOperations

**Added by**: Environment Variables Solution

See the [environmentvariabledefinition_AsyncOperations](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_AsyncOperations) one-to-many relationship for the [environmentvariabledefinition](environmentvariabledefinition.md) table/entity.

### <a name="BKMK_environmentvariablevalue_AsyncOperations"></a> environmentvariablevalue_AsyncOperations

**Added by**: Environment Variables Solution

See the [environmentvariablevalue_AsyncOperations](environmentvariablevalue.md#BKMK_environmentvariablevalue_AsyncOperations) one-to-many relationship for the [environmentvariablevalue](environmentvariablevalue.md) table/entity.

### <a name="BKMK_workflowbinary_AsyncOperations"></a> workflowbinary_AsyncOperations

**Added by**: Power Automate Extensions Workflow Binary package Solution

See the [workflowbinary_AsyncOperations](workflowbinary.md#BKMK_workflowbinary_AsyncOperations) one-to-many relationship for the [workflowbinary](workflowbinary.md) table/entity.

### <a name="BKMK_desktopflowmodule_AsyncOperations"></a> desktopflowmodule_AsyncOperations

**Added by**: Power Automate Extensions core package Solution

See the [desktopflowmodule_AsyncOperations](desktopflowmodule.md#BKMK_desktopflowmodule_AsyncOperations) one-to-many relationship for the [desktopflowmodule](desktopflowmodule.md) table/entity.

### <a name="BKMK_flowmachine_AsyncOperations"></a> flowmachine_AsyncOperations

**Added by**: Power Automate Extensions core package Solution

See the [flowmachine_AsyncOperations](flowmachine.md#BKMK_flowmachine_AsyncOperations) one-to-many relationship for the [flowmachine](flowmachine.md) table/entity.

### <a name="BKMK_flowmachinegroup_AsyncOperations"></a> flowmachinegroup_AsyncOperations

**Added by**: Power Automate Extensions core package Solution

See the [flowmachinegroup_AsyncOperations](flowmachinegroup.md#BKMK_flowmachinegroup_AsyncOperations) one-to-many relationship for the [flowmachinegroup](flowmachinegroup.md) table/entity.

### <a name="BKMK_flowmachineimage_AsyncOperations"></a> flowmachineimage_AsyncOperations

**Added by**: Power Automate Extensions core package Solution

See the [flowmachineimage_AsyncOperations](flowmachineimage.md#BKMK_flowmachineimage_AsyncOperations) one-to-many relationship for the [flowmachineimage](flowmachineimage.md) table/entity.

### <a name="BKMK_flowmachineimageversion_AsyncOperations"></a> flowmachineimageversion_AsyncOperations

**Added by**: Power Automate Extensions core package Solution

See the [flowmachineimageversion_AsyncOperations](flowmachineimageversion.md#BKMK_flowmachineimageversion_AsyncOperations) one-to-many relationship for the [flowmachineimageversion](flowmachineimageversion.md) table/entity.

### <a name="BKMK_flowmachinenetwork_AsyncOperations"></a> flowmachinenetwork_AsyncOperations

**Added by**: Power Automate Extensions core package Solution

See the [flowmachinenetwork_AsyncOperations](flowmachinenetwork.md#BKMK_flowmachinenetwork_AsyncOperations) one-to-many relationship for the [flowmachinenetwork](flowmachinenetwork.md) table/entity.

### <a name="BKMK_processstageparameter_AsyncOperations"></a> processstageparameter_AsyncOperations

**Added by**: Power Automate Extensions core package Solution

See the [processstageparameter_AsyncOperations](processstageparameter.md#BKMK_processstageparameter_AsyncOperations) one-to-many relationship for the [processstageparameter](processstageparameter.md) table/entity.

### <a name="BKMK_workqueue_AsyncOperations"></a> workqueue_AsyncOperations

**Added by**: Power Automate Extensions core package Solution

See the [workqueue_AsyncOperations](workqueue.md#BKMK_workqueue_AsyncOperations) one-to-many relationship for the [workqueue](workqueue.md) table/entity.

### <a name="BKMK_workqueueitem_AsyncOperations"></a> workqueueitem_AsyncOperations

**Added by**: Power Automate Extensions core package Solution

See the [workqueueitem_AsyncOperations](workqueueitem.md#BKMK_workqueueitem_AsyncOperations) one-to-many relationship for the [workqueueitem](workqueueitem.md) table/entity.

### <a name="BKMK_desktopflowbinary_AsyncOperations"></a> desktopflowbinary_AsyncOperations

**Added by**: Power Automate Extensions core package Solution

See the [desktopflowbinary_AsyncOperations](desktopflowbinary.md#BKMK_desktopflowbinary_AsyncOperations) one-to-many relationship for the [desktopflowbinary](desktopflowbinary.md) table/entity.

### <a name="BKMK_flowsession_AsyncOperations"></a> flowsession_AsyncOperations

**Added by**: Power Automate Extensions core package Solution

See the [flowsession_AsyncOperations](flowsession.md#BKMK_flowsession_AsyncOperations) one-to-many relationship for the [flowsession](flowsession.md) table/entity.

### <a name="BKMK_connectionreference_AsyncOperations"></a> connectionreference_AsyncOperations

**Added by**: Power Platform Connection References Solution

See the [connectionreference_AsyncOperations](connectionreference.md#BKMK_connectionreference_AsyncOperations) one-to-many relationship for the [connectionreference](connectionreference.md) table/entity.

### <a name="BKMK_connectioninstance_AsyncOperations"></a> connectioninstance_AsyncOperations

**Added by**: Connection Instance Solution Solution

See the [connectioninstance_AsyncOperations](connectioninstance.md#BKMK_connectioninstance_AsyncOperations) one-to-many relationship for the [connectioninstance](connectioninstance.md) table/entity.

### <a name="BKMK_msdyn_helppage_AsyncOperations"></a> msdyn_helppage_AsyncOperations

**Added by**: Contextual Help Solution

See the [msdyn_helppage_AsyncOperations](msdyn_helppage.md#BKMK_msdyn_helppage_AsyncOperations) one-to-many relationship for the [msdyn_helppage](msdyn_helppage.md) table/entity.

### <a name="BKMK_msdyn_tour_AsyncOperations"></a> msdyn_tour_AsyncOperations

**Added by**: Contextual Help Solution

See the [msdyn_tour_AsyncOperations](msdyn_tour.md#BKMK_msdyn_tour_AsyncOperations) one-to-many relationship for the [msdyn_tour](msdyn_tour.md) table/entity.

### <a name="BKMK_msdynce_botcontent_AsyncOperations"></a> msdynce_botcontent_AsyncOperations

**Added by**: Customer Care Intelligence Bots Solution

See the [msdynce_botcontent_AsyncOperations](msdynce_botcontent.md#BKMK_msdynce_botcontent_AsyncOperations) one-to-many relationship for the [msdynce_botcontent](msdynce_botcontent.md) table/entity.

### <a name="BKMK_conversationtranscript_AsyncOperations"></a> conversationtranscript_AsyncOperations

**Added by**: Power Virtual Agents Common Solution

See the [conversationtranscript_AsyncOperations](conversationtranscript.md#BKMK_conversationtranscript_AsyncOperations) one-to-many relationship for the [conversationtranscript](conversationtranscript.md) table/entity.

### <a name="BKMK_bot_AsyncOperations"></a> bot_AsyncOperations

**Added by**: Power Virtual Agents Solution

See the [bot_AsyncOperations](bot.md#BKMK_bot_AsyncOperations) one-to-many relationship for the [bot](bot.md) table/entity.

### <a name="BKMK_botcomponent_AsyncOperations"></a> botcomponent_AsyncOperations

**Added by**: Power Virtual Agents Solution

See the [botcomponent_AsyncOperations](botcomponent.md#BKMK_botcomponent_AsyncOperations) one-to-many relationship for the [botcomponent](botcomponent.md) table/entity.

### <a name="BKMK_Territory_AsyncOperations"></a> Territory_AsyncOperations

**Added by**: Application Common Solution

See the [Territory_AsyncOperations](territory.md#BKMK_Territory_AsyncOperations) one-to-many relationship for the [territory](territory.md) table/entity.

### <a name="BKMK_activityfileattachment_AsyncOperations"></a> activityfileattachment_AsyncOperations

**Added by**: Activities Patch Solution

See the [activityfileattachment_AsyncOperations](activityfileattachment.md#BKMK_activityfileattachment_AsyncOperations) one-to-many relationship for the [activityfileattachment](activityfileattachment.md) table/entity.

### <a name="BKMK_chat_AsyncOperations"></a> chat_AsyncOperations

**Added by**: Activities Patch Solution

See the [chat_AsyncOperations](chat.md#BKMK_chat_AsyncOperations) one-to-many relationship for the [chat](chat.md) table/entity.

### <a name="BKMK_msdyn_serviceconfiguration_AsyncOperations"></a> msdyn_serviceconfiguration_AsyncOperations

**Added by**: Service Level Agreement (SLA) Extension Solution

See the [msdyn_serviceconfiguration_AsyncOperations](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_AsyncOperations) one-to-many relationship for the [msdyn_serviceconfiguration](msdyn_serviceconfiguration.md) table/entity.

### <a name="BKMK_msdyn_slakpi_AsyncOperations"></a> msdyn_slakpi_AsyncOperations

**Added by**: Service Level Agreement (SLA) Extension Solution

See the [msdyn_slakpi_AsyncOperations](msdyn_slakpi.md#BKMK_msdyn_slakpi_AsyncOperations) one-to-many relationship for the [msdyn_slakpi](msdyn_slakpi.md) table/entity.

### <a name="BKMK_msdyn_knowledgemanagementsetting_AsyncOperations"></a> msdyn_knowledgemanagementsetting_AsyncOperations

**Added by**: Knowledge Management Patch Solution

See the [msdyn_knowledgemanagementsetting_AsyncOperations](msdyn_knowledgemanagementsetting.md#BKMK_msdyn_knowledgemanagementsetting_AsyncOperations) one-to-many relationship for the [msdyn_knowledgemanagementsetting](msdyn_knowledgemanagementsetting.md) table/entity.

### <a name="BKMK_msdyn_federatedarticle_AsyncOperations"></a> msdyn_federatedarticle_AsyncOperations

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_federatedarticle_AsyncOperations](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_AsyncOperations) one-to-many relationship for the [msdyn_federatedarticle](msdyn_federatedarticle.md) table/entity.

### <a name="BKMK_msdyn_federatedarticleincident_AsyncOperations"></a> msdyn_federatedarticleincident_AsyncOperations

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_federatedarticleincident_AsyncOperations](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_AsyncOperations) one-to-many relationship for the [msdyn_federatedarticleincident](msdyn_federatedarticleincident.md) table/entity.

### <a name="BKMK_msdyn_integratedsearchprovider_AsyncOperations"></a> msdyn_integratedsearchprovider_AsyncOperations

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_integratedsearchprovider_AsyncOperations](msdyn_integratedsearchprovider.md#BKMK_msdyn_integratedsearchprovider_AsyncOperations) one-to-many relationship for the [msdyn_integratedsearchprovider](msdyn_integratedsearchprovider.md) table/entity.

### <a name="BKMK_msdyn_kmfederatedsearchconfig_AsyncOperations"></a> msdyn_kmfederatedsearchconfig_AsyncOperations

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_kmfederatedsearchconfig_AsyncOperations](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_AsyncOperations) one-to-many relationship for the [msdyn_kmfederatedsearchconfig](msdyn_kmfederatedsearchconfig.md) table/entity.

### <a name="BKMK_msdyn_knowledgearticleimage_AsyncOperations"></a> msdyn_knowledgearticleimage_AsyncOperations

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgearticleimage_AsyncOperations](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_AsyncOperations) one-to-many relationship for the [msdyn_knowledgearticleimage](msdyn_knowledgearticleimage.md) table/entity.

### <a name="BKMK_msdyn_knowledgeconfiguration_AsyncOperations"></a> msdyn_knowledgeconfiguration_AsyncOperations

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgeconfiguration_AsyncOperations](msdyn_knowledgeconfiguration.md#BKMK_msdyn_knowledgeconfiguration_AsyncOperations) one-to-many relationship for the [msdyn_knowledgeconfiguration](msdyn_knowledgeconfiguration.md) table/entity.

### <a name="BKMK_msdyn_knowledgeinteractioninsight_AsyncOperations"></a> msdyn_knowledgeinteractioninsight_AsyncOperations

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgeinteractioninsight_AsyncOperations](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_AsyncOperations) one-to-many relationship for the [msdyn_knowledgeinteractioninsight](msdyn_knowledgeinteractioninsight.md) table/entity.

### <a name="BKMK_msdyn_knowledgesearchinsight_AsyncOperations"></a> msdyn_knowledgesearchinsight_AsyncOperations

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgesearchinsight_AsyncOperations](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_AsyncOperations) one-to-many relationship for the [msdyn_knowledgesearchinsight](msdyn_knowledgesearchinsight.md) table/entity.

### <a name="BKMK_msdyn_favoriteknowledgearticle_AsyncOperations"></a> msdyn_favoriteknowledgearticle_AsyncOperations

**Added by**: Knowledge Management Features Solution

See the [msdyn_favoriteknowledgearticle_AsyncOperations](msdyn_favoriteknowledgearticle.md#BKMK_msdyn_favoriteknowledgearticle_AsyncOperations) one-to-many relationship for the [msdyn_favoriteknowledgearticle](msdyn_favoriteknowledgearticle.md) table/entity.

### <a name="BKMK_msdyn_kalanguagesetting_AsyncOperations"></a> msdyn_kalanguagesetting_AsyncOperations

**Added by**: Knowledge Management Features Solution

See the [msdyn_kalanguagesetting_AsyncOperations](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_AsyncOperations) one-to-many relationship for the [msdyn_kalanguagesetting](msdyn_kalanguagesetting.md) table/entity.

### <a name="BKMK_msdyn_kbattachment_AsyncOperations"></a> msdyn_kbattachment_AsyncOperations

**Added by**: Knowledge Management Features Solution

See the [msdyn_kbattachment_AsyncOperations](msdyn_kbattachment.md#BKMK_msdyn_kbattachment_AsyncOperations) one-to-many relationship for the [msdyn_kbattachment](msdyn_kbattachment.md) table/entity.

### <a name="BKMK_msdyn_kmpersonalizationsetting_AsyncOperations"></a> msdyn_kmpersonalizationsetting_AsyncOperations

**Added by**: Knowledge Management Features Solution

See the [msdyn_kmpersonalizationsetting_AsyncOperations](msdyn_kmpersonalizationsetting.md#BKMK_msdyn_kmpersonalizationsetting_AsyncOperations) one-to-many relationship for the [msdyn_kmpersonalizationsetting](msdyn_kmpersonalizationsetting.md) table/entity.

### <a name="BKMK_msdyn_knowledgearticletemplate_AsyncOperations"></a> msdyn_knowledgearticletemplate_AsyncOperations

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgearticletemplate_AsyncOperations](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_AsyncOperations) one-to-many relationship for the [msdyn_knowledgearticletemplate](msdyn_knowledgearticletemplate.md) table/entity.

### <a name="BKMK_msdyn_knowledgepersonalfilter_AsyncOperations"></a> msdyn_knowledgepersonalfilter_AsyncOperations

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgepersonalfilter_AsyncOperations](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_AsyncOperations) one-to-many relationship for the [msdyn_knowledgepersonalfilter](msdyn_knowledgepersonalfilter.md) table/entity.

### <a name="BKMK_msdyn_knowledgesearchfilter_AsyncOperations"></a> msdyn_knowledgesearchfilter_AsyncOperations

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgesearchfilter_AsyncOperations](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_AsyncOperations) one-to-many relationship for the [msdyn_knowledgesearchfilter](msdyn_knowledgesearchfilter.md) table/entity.

### <a name="BKMK_pluginpackage_AsyncOperations"></a> pluginpackage_AsyncOperations

**Added by**: Plugin Infrastructure Extension Solution

See the [pluginpackage_AsyncOperations](pluginpackage.md#BKMK_pluginpackage_AsyncOperations) one-to-many relationship for the [pluginpackage](pluginpackage.md) table/entity.

### <a name="BKMK_fxexpression_AsyncOperations"></a> fxexpression_AsyncOperations

**Added by**: msft_PowerfxRuleSolution Solution

See the [fxexpression_AsyncOperations](fxexpression.md#BKMK_fxexpression_AsyncOperations) one-to-many relationship for the [fxexpression](fxexpression.md) table/entity.

### <a name="BKMK_powerfxrule_AsyncOperations"></a> powerfxrule_AsyncOperations

**Added by**: msft_PowerfxRuleSolution Solution

See the [powerfxrule_AsyncOperations](powerfxrule.md#BKMK_powerfxrule_AsyncOperations) one-to-many relationship for the [powerfxrule](powerfxrule.md) table/entity.

### <a name="BKMK_keyvaultreference_AsyncOperations"></a> keyvaultreference_AsyncOperations

**Added by**: ManagedIdentityExtensions Solution

See the [keyvaultreference_AsyncOperations](keyvaultreference.md#BKMK_keyvaultreference_AsyncOperations) one-to-many relationship for the [keyvaultreference](keyvaultreference.md) table/entity.

### <a name="BKMK_managedidentity_AsyncOperations"></a> managedidentity_AsyncOperations

**Added by**: ManagedIdentityExtensions Solution

See the [managedidentity_AsyncOperations](managedidentity.md#BKMK_managedidentity_AsyncOperations) one-to-many relationship for the [managedidentity](managedidentity.md) table/entity.

### <a name="BKMK_msgraphresourcetosubscription_AsyncOperations"></a> msgraphresourcetosubscription_AsyncOperations

**Added by**: msft_ActivitiesInfra_Extensions Solution

See the [msgraphresourcetosubscription_AsyncOperations](msgraphresourcetosubscription.md#BKMK_msgraphresourcetosubscription_AsyncOperations) one-to-many relationship for the [msgraphresourcetosubscription](msgraphresourcetosubscription.md) table/entity.

### <a name="BKMK_virtualentitymetadata_AsyncOperations"></a> virtualentitymetadata_AsyncOperations

**Added by**: RuntimeIntegration Solution

See the [virtualentitymetadata_AsyncOperations](virtualentitymetadata.md#BKMK_virtualentitymetadata_AsyncOperations) one-to-many relationship for the [virtualentitymetadata](virtualentitymetadata.md) table/entity.

### <a name="BKMK_mobileofflineprofileextension_AsyncOperations"></a> mobileofflineprofileextension_AsyncOperations

**Added by**: MobileOfflineProfileExtensionSolution Solution

See the [mobileofflineprofileextension_AsyncOperations](mobileofflineprofileextension.md#BKMK_mobileofflineprofileextension_AsyncOperations) one-to-many relationship for the [mobileofflineprofileextension](mobileofflineprofileextension.md) table/entity.

### <a name="BKMK_teammobileofflineprofilemembership_AsyncOperations"></a> teammobileofflineprofilemembership_AsyncOperations

**Added by**: MobileOfflineMembership Solution

See the [teammobileofflineprofilemembership_AsyncOperations](teammobileofflineprofilemembership.md#BKMK_teammobileofflineprofilemembership_AsyncOperations) one-to-many relationship for the [teammobileofflineprofilemembership](teammobileofflineprofilemembership.md) table/entity.

### <a name="BKMK_usermobileofflineprofilemembership_AsyncOperations"></a> usermobileofflineprofilemembership_AsyncOperations

**Added by**: MobileOfflineMembership Solution

See the [usermobileofflineprofilemembership_AsyncOperations](usermobileofflineprofilemembership.md#BKMK_usermobileofflineprofilemembership_AsyncOperations) one-to-many relationship for the [usermobileofflineprofilemembership](usermobileofflineprofilemembership.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscription_AsyncOperations"></a> organizationdatasyncsubscription_AsyncOperations

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscription_AsyncOperations](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_AsyncOperations) one-to-many relationship for the [organizationdatasyncsubscription](organizationdatasyncsubscription.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscriptionentity_AsyncOperations"></a> organizationdatasyncsubscriptionentity_AsyncOperations

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscriptionentity_AsyncOperations](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_AsyncOperations) one-to-many relationship for the [organizationdatasyncsubscriptionentity](organizationdatasyncsubscriptionentity.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_AsyncOperations"></a> organizationdatasyncsubscriptionfnotable_AsyncOperations

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscriptionfnotable_AsyncOperations](organizationdatasyncsubscriptionfnotable.md#BKMK_organizationdatasyncsubscriptionfnotable_AsyncOperations) one-to-many relationship for the [organizationdatasyncsubscriptionfnotable](organizationdatasyncsubscriptionfnotable.md) table/entity.

### <a name="BKMK_organizationdatasyncfnostate_AsyncOperations"></a> organizationdatasyncfnostate_AsyncOperations

**Added by**: DataSyncState Solution

See the [organizationdatasyncfnostate_AsyncOperations](organizationdatasyncfnostate.md#BKMK_organizationdatasyncfnostate_AsyncOperations) one-to-many relationship for the [organizationdatasyncfnostate](organizationdatasyncfnostate.md) table/entity.

### <a name="BKMK_organizationdatasyncstate_AsyncOperations"></a> organizationdatasyncstate_AsyncOperations

**Added by**: DataSyncState Solution

See the [organizationdatasyncstate_AsyncOperations](organizationdatasyncstate.md#BKMK_organizationdatasyncstate_AsyncOperations) one-to-many relationship for the [organizationdatasyncstate](organizationdatasyncstate.md) table/entity.

### <a name="BKMK_metadataforarchival_AsyncOperations"></a> metadataforarchival_AsyncOperations

**Added by**: Retention Base Components Solution

See the [metadataforarchival_AsyncOperations](metadataforarchival.md#BKMK_metadataforarchival_AsyncOperations) one-to-many relationship for the [metadataforarchival](metadataforarchival.md) table/entity.

### <a name="BKMK_retentionconfig_AsyncOperations"></a> retentionconfig_AsyncOperations

**Added by**: Retention Base Components Solution

See the [retentionconfig_AsyncOperations](retentionconfig.md#BKMK_retentionconfig_AsyncOperations) one-to-many relationship for the [retentionconfig](retentionconfig.md) table/entity.

### <a name="BKMK_retentionfailuredetail_AsyncOperations"></a> retentionfailuredetail_AsyncOperations

**Added by**: Retention Base Components Solution

See the [retentionfailuredetail_AsyncOperations](retentionfailuredetail.md#BKMK_retentionfailuredetail_AsyncOperations) one-to-many relationship for the [retentionfailuredetail](retentionfailuredetail.md) table/entity.

### <a name="BKMK_retentionoperation_AsyncOperations"></a> retentionoperation_AsyncOperations

**Added by**: Retention Base Components Solution

See the [retentionoperation_AsyncOperations](retentionoperation.md#BKMK_retentionoperation_AsyncOperations) one-to-many relationship for the [retentionoperation](retentionoperation.md) table/entity.

### <a name="BKMK_retentionoperationdetail_AsyncOperations"></a> retentionoperationdetail_AsyncOperations

**Added by**: Retention Base Components Solution

See the [retentionoperationdetail_AsyncOperations](retentionoperationdetail.md#BKMK_retentionoperationdetail_AsyncOperations) one-to-many relationship for the [retentionoperationdetail](retentionoperationdetail.md) table/entity.

### <a name="BKMK_msdyn_appinsightsmetadata_AsyncOperations"></a> msdyn_appinsightsmetadata_AsyncOperations

**Added by**: Insights App Platform Solution

See the [msdyn_appinsightsmetadata_AsyncOperations](msdyn_appinsightsmetadata.md#BKMK_msdyn_appinsightsmetadata_AsyncOperations) one-to-many relationship for the [msdyn_appinsightsmetadata](msdyn_appinsightsmetadata.md) table/entity.

### <a name="BKMK_msdyn_dataflowtemplate_AsyncOperations"></a> msdyn_dataflowtemplate_AsyncOperations

**Added by**: Insights App Platform Solution

See the [msdyn_dataflowtemplate_AsyncOperations](msdyn_dataflowtemplate.md#BKMK_msdyn_dataflowtemplate_AsyncOperations) one-to-many relationship for the [msdyn_dataflowtemplate](msdyn_dataflowtemplate.md) table/entity.

### <a name="BKMK_msdyn_workflowactionstatus_AsyncOperations"></a> msdyn_workflowactionstatus_AsyncOperations

**Added by**: Insights App Platform Solution

See the [msdyn_workflowactionstatus_AsyncOperations](msdyn_workflowactionstatus.md#BKMK_msdyn_workflowactionstatus_AsyncOperations) one-to-many relationship for the [msdyn_workflowactionstatus](msdyn_workflowactionstatus.md) table/entity.

### <a name="BKMK_userrating_AsyncOperations"></a> userrating_AsyncOperations

**Added by**: User Rating Solution

See the [userrating_AsyncOperations](userrating.md#BKMK_userrating_AsyncOperations) one-to-many relationship for the [userrating](userrating.md) table/entity.

### <a name="BKMK_msdyn_mobileapp_AsyncOperations"></a> msdyn_mobileapp_AsyncOperations

**Added by**: Mobile Apps Solution Solution

See the [msdyn_mobileapp_AsyncOperations](msdyn_mobileapp.md#BKMK_msdyn_mobileapp_AsyncOperations) one-to-many relationship for the [msdyn_mobileapp](msdyn_mobileapp.md) table/entity.

### <a name="BKMK_msdyn_insightsstorevirtualentity_AsyncOperations"></a> msdyn_insightsstorevirtualentity_AsyncOperations

**Added by**: Insights Store Data Provider Solution

See the [msdyn_insightsstorevirtualentity_AsyncOperations](msdyn_insightsstorevirtualentity.md#BKMK_msdyn_insightsstorevirtualentity_AsyncOperations) one-to-many relationship for the [msdyn_insightsstorevirtualentity](msdyn_insightsstorevirtualentity.md) table/entity.

### <a name="BKMK_roleeditorlayout_AsyncOperations"></a> roleeditorlayout_AsyncOperations

**Added by**: Role Editor Solution

See the [roleeditorlayout_AsyncOperations](roleeditorlayout.md#BKMK_roleeditorlayout_AsyncOperations) one-to-many relationship for the [roleeditorlayout](roleeditorlayout.md) table/entity.

### <a name="BKMK_appaction_AsyncOperations"></a> appaction_AsyncOperations

**Added by**: Power Apps Actions Solution

See the [appaction_AsyncOperations](appaction.md#BKMK_appaction_AsyncOperations) one-to-many relationship for the [appaction](appaction.md) table/entity.

### <a name="BKMK_appactionmigration_AsyncOperations"></a> appactionmigration_AsyncOperations

**Added by**: Power Apps Actions Solution

See the [appactionmigration_AsyncOperations](appactionmigration.md#BKMK_appactionmigration_AsyncOperations) one-to-many relationship for the [appactionmigration](appactionmigration.md) table/entity.

### <a name="BKMK_appactionrule_AsyncOperations"></a> appactionrule_AsyncOperations

**Added by**: Power Apps Actions Solution

See the [appactionrule_AsyncOperations](appactionrule.md#BKMK_appactionrule_AsyncOperations) one-to-many relationship for the [appactionrule](appactionrule.md) table/entity.

### <a name="BKMK_card_AsyncOperations"></a> card_AsyncOperations

**Added by**: Power Apps cards Solution

See the [card_AsyncOperations](card.md#BKMK_card_AsyncOperations) one-to-many relationship for the [card](card.md) table/entity.

### <a name="BKMK_msdyn_entitylinkchatconfiguration_AsyncOperations"></a> msdyn_entitylinkchatconfiguration_AsyncOperations

**Added by**: Teams Chat Settings Solution Solution

See the [msdyn_entitylinkchatconfiguration_AsyncOperations](msdyn_entitylinkchatconfiguration.md#BKMK_msdyn_entitylinkchatconfiguration_AsyncOperations) one-to-many relationship for the [msdyn_entitylinkchatconfiguration](msdyn_entitylinkchatconfiguration.md) table/entity.

### <a name="BKMK_msdyn_richtextfile_AsyncOperations"></a> msdyn_richtextfile_AsyncOperations

**Added by**: Rich Text Editor Solution

See the [msdyn_richtextfile_AsyncOperations](msdyn_richtextfile.md#BKMK_msdyn_richtextfile_AsyncOperations) one-to-many relationship for the [msdyn_richtextfile](msdyn_richtextfile.md) table/entity.

### <a name="BKMK_msdyn_customcontrolextendedsettings_AsyncOperations"></a> msdyn_customcontrolextendedsettings_AsyncOperations

**Added by**: User Experiences Extended Settings Solution

See the [msdyn_customcontrolextendedsettings_AsyncOperations](msdyn_customcontrolextendedsettings.md#BKMK_msdyn_customcontrolextendedsettings_AsyncOperations) one-to-many relationship for the [msdyn_customcontrolextendedsettings](msdyn_customcontrolextendedsettings.md) table/entity.

### <a name="BKMK_searchrelationshipsettings_AsyncOperations"></a> searchrelationshipsettings_AsyncOperations

**Added by**: msdyn_RelevanceSearch Solution

See the [searchrelationshipsettings_AsyncOperations](searchrelationshipsettings.md#BKMK_searchrelationshipsettings_AsyncOperations) one-to-many relationship for the [searchrelationshipsettings](searchrelationshipsettings.md) table/entity.

### <a name="BKMK_msdyn_virtualtablecolumncandidate_AsyncOperations"></a> msdyn_virtualtablecolumncandidate_AsyncOperations

**Added by**: Virtual Connector Provider Solution

See the [msdyn_virtualtablecolumncandidate_AsyncOperations](msdyn_virtualtablecolumncandidate.md#BKMK_msdyn_virtualtablecolumncandidate_AsyncOperations) one-to-many relationship for the [msdyn_virtualtablecolumncandidate](msdyn_virtualtablecolumncandidate.md) table/entity.

### <a name="BKMK_msdyn_aiconfiguration_AsyncOperations"></a> msdyn_aiconfiguration_AsyncOperations

**Added by**: AISolution Solution

See the [msdyn_aiconfiguration_AsyncOperations](msdyn_aiconfiguration.md#BKMK_msdyn_aiconfiguration_AsyncOperations) one-to-many relationship for the [msdyn_aiconfiguration](msdyn_aiconfiguration.md) table/entity.

### <a name="BKMK_msdyn_aievent_AsyncOperations"></a> msdyn_aievent_AsyncOperations

**Added by**: AISolution Solution

See the [msdyn_aievent_AsyncOperations](msdyn_aievent.md#BKMK_msdyn_aievent_AsyncOperations) one-to-many relationship for the [msdyn_aievent](msdyn_aievent.md) table/entity.

### <a name="BKMK_msdyn_aimodel_AsyncOperations"></a> msdyn_aimodel_AsyncOperations

**Added by**: AISolution Solution

See the [msdyn_aimodel_AsyncOperations](msdyn_aimodel.md#BKMK_msdyn_aimodel_AsyncOperations) one-to-many relationship for the [msdyn_aimodel](msdyn_aimodel.md) table/entity.

### <a name="BKMK_msdyn_aitemplate_AsyncOperations"></a> msdyn_aitemplate_AsyncOperations

**Added by**: AISolution Solution

See the [msdyn_aitemplate_AsyncOperations](msdyn_aitemplate.md#BKMK_msdyn_aitemplate_AsyncOperations) one-to-many relationship for the [msdyn_aitemplate](msdyn_aitemplate.md) table/entity.

### <a name="BKMK_msdyn_aibfeedbackloop_AsyncOperations"></a> msdyn_aibfeedbackloop_AsyncOperations

**Added by**: AISolutionFullAdditions Solution

See the [msdyn_aibfeedbackloop_AsyncOperations](msdyn_aibfeedbackloop.md#BKMK_msdyn_aibfeedbackloop_AsyncOperations) one-to-many relationship for the [msdyn_aibfeedbackloop](msdyn_aibfeedbackloop.md) table/entity.

### <a name="BKMK_msdyn_aifptrainingdocument_AsyncOperations"></a> msdyn_aifptrainingdocument_AsyncOperations

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aifptrainingdocument_AsyncOperations](msdyn_aifptrainingdocument.md#BKMK_msdyn_aifptrainingdocument_AsyncOperations) one-to-many relationship for the [msdyn_aifptrainingdocument](msdyn_aifptrainingdocument.md) table/entity.

### <a name="BKMK_msdyn_aiodimage_AsyncOperations"></a> msdyn_aiodimage_AsyncOperations

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodimage_AsyncOperations](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_AsyncOperations) one-to-many relationship for the [msdyn_aiodimage](msdyn_aiodimage.md) table/entity.

### <a name="BKMK_msdyn_aiodlabel_AsyncOperations"></a> msdyn_aiodlabel_AsyncOperations

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodlabel_AsyncOperations](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_AsyncOperations) one-to-many relationship for the [msdyn_aiodlabel](msdyn_aiodlabel.md) table/entity.

### <a name="BKMK_msdyn_aiodtrainingboundingbox_AsyncOperations"></a> msdyn_aiodtrainingboundingbox_AsyncOperations

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodtrainingboundingbox_AsyncOperations](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_AsyncOperations) one-to-many relationship for the [msdyn_aiodtrainingboundingbox](msdyn_aiodtrainingboundingbox.md) table/entity.

### <a name="BKMK_msdyn_aiodtrainingimage_AsyncOperations"></a> msdyn_aiodtrainingimage_AsyncOperations

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodtrainingimage_AsyncOperations](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_AsyncOperations) one-to-many relationship for the [msdyn_aiodtrainingimage](msdyn_aiodtrainingimage.md) table/entity.

### <a name="BKMK_msdyn_aibdataset_AsyncOperations"></a> msdyn_aibdataset_AsyncOperations

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdataset_AsyncOperations](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_AsyncOperations) one-to-many relationship for the [msdyn_aibdataset](msdyn_aibdataset.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetfile_AsyncOperations"></a> msdyn_aibdatasetfile_AsyncOperations

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetfile_AsyncOperations](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_AsyncOperations) one-to-many relationship for the [msdyn_aibdatasetfile](msdyn_aibdatasetfile.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetrecord_AsyncOperations"></a> msdyn_aibdatasetrecord_AsyncOperations

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetrecord_AsyncOperations](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_AsyncOperations) one-to-many relationship for the [msdyn_aibdatasetrecord](msdyn_aibdatasetrecord.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetscontainer_AsyncOperations"></a> msdyn_aibdatasetscontainer_AsyncOperations

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetscontainer_AsyncOperations](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_AsyncOperations) one-to-many relationship for the [msdyn_aibdatasetscontainer](msdyn_aibdatasetscontainer.md) table/entity.

### <a name="BKMK_msdyn_aibfile_AsyncOperations"></a> msdyn_aibfile_AsyncOperations

**Added by**: AI Solution default templates Solution

See the [msdyn_aibfile_AsyncOperations](msdyn_aibfile.md#BKMK_msdyn_aibfile_AsyncOperations) one-to-many relationship for the [msdyn_aibfile](msdyn_aibfile.md) table/entity.

### <a name="BKMK_msdyn_aibfileattacheddata_AsyncOperations"></a> msdyn_aibfileattacheddata_AsyncOperations

**Added by**: AI Solution default templates Solution

See the [msdyn_aibfileattacheddata_AsyncOperations](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_AsyncOperations) one-to-many relationship for the [msdyn_aibfileattacheddata](msdyn_aibfileattacheddata.md) table/entity.

### <a name="BKMK_msdyn_pmanalysishistory_AsyncOperations"></a> msdyn_pmanalysishistory_AsyncOperations

**Added by**: Process Mining Solution

See the [msdyn_pmanalysishistory_AsyncOperations](msdyn_pmanalysishistory.md#BKMK_msdyn_pmanalysishistory_AsyncOperations) one-to-many relationship for the [msdyn_pmanalysishistory](msdyn_pmanalysishistory.md) table/entity.

### <a name="BKMK_msdyn_pmcalendar_AsyncOperations"></a> msdyn_pmcalendar_AsyncOperations

**Added by**: Process Mining Solution

See the [msdyn_pmcalendar_AsyncOperations](msdyn_pmcalendar.md#BKMK_msdyn_pmcalendar_AsyncOperations) one-to-many relationship for the [msdyn_pmcalendar](msdyn_pmcalendar.md) table/entity.

### <a name="BKMK_msdyn_pmcalendarversion_AsyncOperations"></a> msdyn_pmcalendarversion_AsyncOperations

**Added by**: Process Mining Solution

See the [msdyn_pmcalendarversion_AsyncOperations](msdyn_pmcalendarversion.md#BKMK_msdyn_pmcalendarversion_AsyncOperations) one-to-many relationship for the [msdyn_pmcalendarversion](msdyn_pmcalendarversion.md) table/entity.

### <a name="BKMK_msdyn_pminferredtask_AsyncOperations"></a> msdyn_pminferredtask_AsyncOperations

**Added by**: Process Mining Solution

See the [msdyn_pminferredtask_AsyncOperations](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_AsyncOperations) one-to-many relationship for the [msdyn_pminferredtask](msdyn_pminferredtask.md) table/entity.

### <a name="BKMK_msdyn_pmprocessextendedmetadataversion_AsyncOperations"></a> msdyn_pmprocessextendedmetadataversion_AsyncOperations

**Added by**: Process Mining Solution

See the [msdyn_pmprocessextendedmetadataversion_AsyncOperations](msdyn_pmprocessextendedmetadataversion.md#BKMK_msdyn_pmprocessextendedmetadataversion_AsyncOperations) one-to-many relationship for the [msdyn_pmprocessextendedmetadataversion](msdyn_pmprocessextendedmetadataversion.md) table/entity.

### <a name="BKMK_msdyn_pmprocesstemplate_AsyncOperations"></a> msdyn_pmprocesstemplate_AsyncOperations

**Added by**: Process Mining Solution

See the [msdyn_pmprocesstemplate_AsyncOperations](msdyn_pmprocesstemplate.md#BKMK_msdyn_pmprocesstemplate_AsyncOperations) one-to-many relationship for the [msdyn_pmprocesstemplate](msdyn_pmprocesstemplate.md) table/entity.

### <a name="BKMK_msdyn_pmprocessusersettings_AsyncOperations"></a> msdyn_pmprocessusersettings_AsyncOperations

**Added by**: Process Mining Solution

See the [msdyn_pmprocessusersettings_AsyncOperations](msdyn_pmprocessusersettings.md#BKMK_msdyn_pmprocessusersettings_AsyncOperations) one-to-many relationship for the [msdyn_pmprocessusersettings](msdyn_pmprocessusersettings.md) table/entity.

### <a name="BKMK_msdyn_pmprocessversion_AsyncOperations"></a> msdyn_pmprocessversion_AsyncOperations

**Added by**: Process Mining Solution

See the [msdyn_pmprocessversion_AsyncOperations](msdyn_pmprocessversion.md#BKMK_msdyn_pmprocessversion_AsyncOperations) one-to-many relationship for the [msdyn_pmprocessversion](msdyn_pmprocessversion.md) table/entity.

### <a name="BKMK_msdyn_pmrecording_AsyncOperations"></a> msdyn_pmrecording_AsyncOperations

**Added by**: Process Mining Solution

See the [msdyn_pmrecording_AsyncOperations](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_AsyncOperations) one-to-many relationship for the [msdyn_pmrecording](msdyn_pmrecording.md) table/entity.

### <a name="BKMK_msdyn_pmtemplate_AsyncOperations"></a> msdyn_pmtemplate_AsyncOperations

**Added by**: Process Mining Solution

See the [msdyn_pmtemplate_AsyncOperations](msdyn_pmtemplate.md#BKMK_msdyn_pmtemplate_AsyncOperations) one-to-many relationship for the [msdyn_pmtemplate](msdyn_pmtemplate.md) table/entity.

### <a name="BKMK_msdyn_pmview_AsyncOperations"></a> msdyn_pmview_AsyncOperations

**Added by**: Process Mining Solution

See the [msdyn_pmview_AsyncOperations](msdyn_pmview.md#BKMK_msdyn_pmview_AsyncOperations) one-to-many relationship for the [msdyn_pmview](msdyn_pmview.md) table/entity.

### <a name="BKMK_msdyn_analysiscomponent_AsyncOperations"></a> msdyn_analysiscomponent_AsyncOperations

**Added by**: Power Apps Checker Solution

See the [msdyn_analysiscomponent_AsyncOperations](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_AsyncOperations) one-to-many relationship for the [msdyn_analysiscomponent](msdyn_analysiscomponent.md) table/entity.

### <a name="BKMK_msdyn_analysisjob_AsyncOperations"></a> msdyn_analysisjob_AsyncOperations

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisjob_AsyncOperations](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_AsyncOperations) one-to-many relationship for the [msdyn_analysisjob](msdyn_analysisjob.md) table/entity.

### <a name="BKMK_msdyn_analysisoverride_AsyncOperations"></a> msdyn_analysisoverride_AsyncOperations

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisoverride_AsyncOperations](msdyn_analysisoverride.md#BKMK_msdyn_analysisoverride_AsyncOperations) one-to-many relationship for the [msdyn_analysisoverride](msdyn_analysisoverride.md) table/entity.

### <a name="BKMK_msdyn_analysisresult_AsyncOperations"></a> msdyn_analysisresult_AsyncOperations

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisresult_AsyncOperations](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_AsyncOperations) one-to-many relationship for the [msdyn_analysisresult](msdyn_analysisresult.md) table/entity.

### <a name="BKMK_msdyn_analysisresultdetail_AsyncOperations"></a> msdyn_analysisresultdetail_AsyncOperations

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisresultdetail_AsyncOperations](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_AsyncOperations) one-to-many relationship for the [msdyn_analysisresultdetail](msdyn_analysisresultdetail.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthrule_AsyncOperations"></a> msdyn_solutionhealthrule_AsyncOperations

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthrule_AsyncOperations](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_AsyncOperations) one-to-many relationship for the [msdyn_solutionhealthrule](msdyn_solutionhealthrule.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthruleargument_AsyncOperations"></a> msdyn_solutionhealthruleargument_AsyncOperations

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthruleargument_AsyncOperations](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_AsyncOperations) one-to-many relationship for the [msdyn_solutionhealthruleargument](msdyn_solutionhealthruleargument.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthruleset_AsyncOperations"></a> msdyn_solutionhealthruleset_AsyncOperations

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthruleset_AsyncOperations](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_AsyncOperations) one-to-many relationship for the [msdyn_solutionhealthruleset](msdyn_solutionhealthruleset.md) table/entity.

### <a name="BKMK_powerbidataset_AsyncOperations"></a> powerbidataset_AsyncOperations

**Added by**: Power BI Entities Solution

See the [powerbidataset_AsyncOperations](powerbidataset.md#BKMK_powerbidataset_AsyncOperations) one-to-many relationship for the [powerbidataset](powerbidataset.md) table/entity.

### <a name="BKMK_powerbimashupparameter_AsyncOperations"></a> powerbimashupparameter_AsyncOperations

**Added by**: Power BI Entities Solution

See the [powerbimashupparameter_AsyncOperations](powerbimashupparameter.md#BKMK_powerbimashupparameter_AsyncOperations) one-to-many relationship for the [powerbimashupparameter](powerbimashupparameter.md) table/entity.

### <a name="BKMK_powerbireport_AsyncOperations"></a> powerbireport_AsyncOperations

**Added by**: Power BI Entities Solution

See the [powerbireport_AsyncOperations](powerbireport.md#BKMK_powerbireport_AsyncOperations) one-to-many relationship for the [powerbireport](powerbireport.md) table/entity.

### <a name="BKMK_msdyn_fileupload_AsyncOperations"></a> msdyn_fileupload_AsyncOperations

**Added by**: Smart Data Import Base Solution

See the [msdyn_fileupload_AsyncOperations](msdyn_fileupload.md#BKMK_msdyn_fileupload_AsyncOperations) one-to-many relationship for the [msdyn_fileupload](msdyn_fileupload.md) table/entity.

### <a name="BKMK_mspcat_catalogsubmissionfiles_AsyncOperations"></a> mspcat_catalogsubmissionfiles_AsyncOperations

**Added by**: Power Platform Catalog Client Packaging Solution

See the [mspcat_catalogsubmissionfiles_AsyncOperations](mspcat_catalogsubmissionfiles.md#BKMK_mspcat_catalogsubmissionfiles_AsyncOperations) one-to-many relationship for the [mspcat_catalogsubmissionfiles](mspcat_catalogsubmissionfiles.md) table/entity.

### <a name="BKMK_mspcat_packagestore_AsyncOperations"></a> mspcat_packagestore_AsyncOperations

**Added by**: Power Platform Catalog Client Packaging Solution

See the [mspcat_packagestore_AsyncOperations](mspcat_packagestore.md#BKMK_mspcat_packagestore_AsyncOperations) one-to-many relationship for the [mspcat_packagestore](mspcat_packagestore.md) table/entity.

### <a name="BKMK_msdyn_schedule_AsyncOperations"></a> msdyn_schedule_AsyncOperations

**Added by**: Insights App Platform Solution

See the [msdyn_schedule_AsyncOperations](msdyn_schedule.md#BKMK_msdyn_schedule_AsyncOperations) one-to-many relationship for the [msdyn_schedule](msdyn_schedule.md) table/entity.

### <a name="BKMK_msdyn_dataflow_datalakefolder_AsyncOperations"></a> msdyn_dataflow_datalakefolder_AsyncOperations

**Added by**: Insights App Platform Solution

See the [msdyn_dataflow_datalakefolder_AsyncOperations](msdyn_dataflow_datalakefolder.md#BKMK_msdyn_dataflow_datalakefolder_AsyncOperations) one-to-many relationship for the [msdyn_dataflow_datalakefolder](msdyn_dataflow_datalakefolder.md) table/entity.

### <a name="BKMK_msdyn_dmsrequest_AsyncOperations"></a> msdyn_dmsrequest_AsyncOperations

**Added by**: Insights App Platform Solution

See the [msdyn_dmsrequest_AsyncOperations](msdyn_dmsrequest.md#BKMK_msdyn_dmsrequest_AsyncOperations) one-to-many relationship for the [msdyn_dmsrequest](msdyn_dmsrequest.md) table/entity.

### <a name="BKMK_msdyn_dmsrequeststatus_AsyncOperations"></a> msdyn_dmsrequeststatus_AsyncOperations

**Added by**: Insights App Platform Solution

See the [msdyn_dmsrequeststatus_AsyncOperations](msdyn_dmsrequeststatus.md#BKMK_msdyn_dmsrequeststatus_AsyncOperations) one-to-many relationship for the [msdyn_dmsrequeststatus](msdyn_dmsrequeststatus.md) table/entity.

### <a name="BKMK_searchattributesettings_AsyncOperations"></a> searchattributesettings_AsyncOperations

**Added by**: msdyn_RelevanceSearch Solution

See the [searchattributesettings_AsyncOperations](searchattributesettings.md#BKMK_searchattributesettings_AsyncOperations) one-to-many relationship for the [searchattributesettings](searchattributesettings.md) table/entity.

### <a name="BKMK_searchcustomanalyzer_AsyncOperations"></a> searchcustomanalyzer_AsyncOperations

**Added by**: msdyn_RelevanceSearch Solution

See the [searchcustomanalyzer_AsyncOperations](searchcustomanalyzer.md#BKMK_searchcustomanalyzer_AsyncOperations) one-to-many relationship for the [searchcustomanalyzer](searchcustomanalyzer.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.asyncoperation?text=asyncoperation EntityType" />