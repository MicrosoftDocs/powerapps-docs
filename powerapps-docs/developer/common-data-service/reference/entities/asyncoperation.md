---
title: "AsyncOperation Entity Reference (Common Data Service)| MicrosoftDocs"
description: "Includes schema information and supported messages for the AsyncOperation entity in Common Data Service."
ms.date: 11/07/2019
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
---
# AsyncOperation Entity Reference

Process whose execution can proceed independently or in the background.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/asyncoperations<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/asyncoperations(*asyncoperationid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/asyncoperations(*asyncoperationid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/asyncoperations<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/asyncoperations(*asyncoperationid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Entity Properties

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

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AsyncOperationId](#BKMK_AsyncOperationId)
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
|IsValidForForm|False|
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

#### OperationType Options

|Value|Label|
|-----|-----|
|1|System Event|
|2|Bulk Email|
|3|Import File Parse|
|4|Transform Parse Data|
|5|Import|
|6|Activity Propagation|
|7|Duplicate Detection Rule Publish|
|8|Bulk Duplicate Detection|
|9|SQM Data Collection|
|10|Workflow|
|11|Quick Campaign|
|12|Matchcode Update|
|13|Bulk Delete|
|14|Deletion Service|
|15|Index Management|
|16|Collect Organization Statistics|
|17|Import Subprocess|
|18|Calculate Organization Storage Size|
|19|Collect Organization Database Statistics|
|20|Collection Organization Size Statistics|
|21|Database Tuning|
|22|Calculate Organization Maximum Storage Size|
|23|Bulk Delete Subprocess|
|24|Update Statistic Intervals|
|25|Organization Full Text Catalog Index|
|26|Database log backup|
|27|Update Contract States|
|28|DBCC SHRINKDATABASE maintenance job|
|29|DBCC SHRINKFILE maintenance job|
|30|Reindex all indices maintenance job|
|31|Storage Limit Notification|
|32|Cleanup inactive workflow assemblies|
|35|Recurring Series Expansion|
|38|Import Sample Data|
|40|Goal Roll Up|
|41|Audit Partition Creation|
|42|Check For Language Pack Updates|
|43|Provision Language Pack|
|44|Update Organization Database|
|45|Update Solution|
|46|Regenerate Entity Row Count Snapshot Data|
|47|Regenerate Read Share Snapshot Data|
|49|Post to Yammer|
|50|Outgoing Activity|
|51|Incoming Email Processing|
|52|Mailbox Test Access|
|53|Encryption Health Check|
|54|Execute Async Request|
|56|Update Entitlement States|
|57|Calculate Rollup Field|
|58|Mass Calculate Rollup Field|
|59|Import Translation|
|62|Convert Date And Time Behavior|
|63|EntityKey Index Creation|
|65|Update Knowledge Article States|
|68|Resource Booking Sync|
|69|Relationship Assistant Cards|
|71|Cleanup Solution Components|
|72|App Module Metadata Operation|
|73|ALM Anomaly Detection Operation|
|75|Flow Notification|
|76|Ribbon Client Metadata Operation|
|79|CallbackRegistration Expander Operation|
|90|CascadeAssign|
|91|CascadeDelete|
|92|Event Expander Operation|
|93|Import Solution Metadata|
|94|Bulk Delete File Attachment|
|95|Refresh Business Unit for Records Owned By Principal|
|96|Revoke Inherited Access|



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
|Targets|account,activitymimeattachment,activitypointer,annotation,annualfiscalcalendar,appointment,attributeimageconfig,attributemap,businessunit,businessunitnewsarticle,calendar,channelaccessprofile,channelaccessprofilerule,connection,connectionrole,connector,contact,convertrule,customeraddress,customerrelationship,displaystring,email,emailserverprofile,entityanalyticsconfig,entityimageconfig,entitymap,environmentvariabledefinition,environmentvariablevalue,externalparty,externalpartyitem,fax,fixedmonthlyfiscalcalendar,flowsession,goal,goalrollupquery,holidaywrapper,import,importdata,importfile,importlog,importmap,interactionforemail,isvconfig,kbarticle,kbarticlecomment,kbarticletemplate,knowledgearticle,knowledgebaserecord,letter,mailbox,mailmergetemplate,metric,monthlyfiscalcalendar,msdyn_aiconfiguration,msdyn_aifptrainingdocument,msdyn_aimodel,msdyn_aiodimage,msdyn_aiodlabel,msdyn_aiodtrainingboundingbox,msdyn_aiodtrainingimage,msdyn_aitemplate,msdyn_analysiscomponent,msdyn_analysisjob,msdyn_analysisresult,msdyn_analysisresultdetail,msdyn_knowledgearticleimage,msdyn_knowledgearticletemplate,msdyn_solutionhealthrule,msdyn_solutionhealthruleargument,msdyn_solutionhealthruleset,organization,phonecall,position,post,postfollow,privilege,quarterlyfiscalcalendar,queue,queueitem,recurringappointmentmaster,relationshiprole,relationshiprolemap,report,role,rollupfield,routingrule,routingruleitem,savedquery,semiannualfiscalcalendar,sharepointdocumentlocation,sharepointsite,similarityrule,sla,socialactivity,socialprofile,subject,systemform,systemuser,task,team,template,territory,theme,transactioncurrency,userform,usermapping,userquery,workflowbinary|
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
|MaxLength|256|
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
|MaxLength|160|
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

#### StateCode Options

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

#### StatusCode Options

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
|MaxLength|64|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only attributes

These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CompletedOn](#BKMK_CompletedOn)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
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

#### IsWaitingForEvent Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



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
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|SystemRequired|
|Targets|businessunit|
|Type|Lookup|


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

#### WorkflowIsBlocked Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



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

Same as mailboxtrackingfolder entity [AsyncOperation_MailboxTrackingFolder](mailboxtrackingfolder.md#BKMK_AsyncOperation_MailboxTrackingFolder) Many-To-One relationship.

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

Same as bulkdeleteoperation entity [AsyncOperation_BulkDeleteOperation](bulkdeleteoperation.md#BKMK_AsyncOperation_BulkDeleteOperation) Many-To-One relationship.

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

Same as workflowlog entity [lk_workflowlog_asyncoperation_childworkflow](workflowlog.md#BKMK_lk_workflowlog_asyncoperation_childworkflow) Many-To-One relationship.

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

Same as email entity [AsyncOperation_Emails](email.md#BKMK_AsyncOperation_Emails) Many-To-One relationship.

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

Same as duplicaterecord entity [AsyncOperation_DuplicateBaseRecord](duplicaterecord.md#BKMK_AsyncOperation_DuplicateBaseRecord) Many-To-One relationship.

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

Same as workflowlog entity [lk_workflowlog_asyncoperations](workflowlog.md#BKMK_lk_workflowlog_asyncoperations) Many-To-One relationship.

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

Same as socialactivity entity [AsyncOperation_SocialActivities](socialactivity.md#BKMK_AsyncOperation_SocialActivities) Many-To-One relationship.

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

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

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
- [Territory_AsyncOperations](#BKMK_Territory_AsyncOperations)
- [msdyn_knowledgearticleimage_AsyncOperations](#BKMK_msdyn_knowledgearticleimage_AsyncOperations)
- [msdyn_knowledgearticletemplate_AsyncOperations](#BKMK_msdyn_knowledgearticletemplate_AsyncOperations)
- [attributeimageconfig_AsyncOperations](#BKMK_attributeimageconfig_AsyncOperations)
- [entityimageconfig_AsyncOperations](#BKMK_entityimageconfig_AsyncOperations)
- [entityanalyticsconfig_AsyncOperations](#BKMK_entityanalyticsconfig_AsyncOperations)
- [connector_AsyncOperations](#BKMK_connector_AsyncOperations)
- [msdyn_aiconfiguration_AsyncOperations](#BKMK_msdyn_aiconfiguration_AsyncOperations)
- [msdyn_aimodel_AsyncOperations](#BKMK_msdyn_aimodel_AsyncOperations)
- [msdyn_aitemplate_AsyncOperations](#BKMK_msdyn_aitemplate_AsyncOperations)
- [msdyn_aifptrainingdocument_AsyncOperations](#BKMK_msdyn_aifptrainingdocument_AsyncOperations)
- [msdyn_aiodimage_AsyncOperations](#BKMK_msdyn_aiodimage_AsyncOperations)
- [msdyn_aiodlabel_AsyncOperations](#BKMK_msdyn_aiodlabel_AsyncOperations)
- [msdyn_aiodtrainingboundingbox_AsyncOperations](#BKMK_msdyn_aiodtrainingboundingbox_AsyncOperations)
- [msdyn_aiodtrainingimage_AsyncOperations](#BKMK_msdyn_aiodtrainingimage_AsyncOperations)
- [flowsession_AsyncOperations](#BKMK_flowsession_AsyncOperations)
- [workflowbinary_AsyncOperations](#BKMK_workflowbinary_AsyncOperations)
- [environmentvariabledefinition_AsyncOperations](#BKMK_environmentvariabledefinition_AsyncOperations)
- [environmentvariablevalue_AsyncOperations](#BKMK_environmentvariablevalue_AsyncOperations)
- [msdyn_analysiscomponent_AsyncOperations](#BKMK_msdyn_analysiscomponent_AsyncOperations)
- [msdyn_analysisjob_AsyncOperations](#BKMK_msdyn_analysisjob_AsyncOperations)
- [msdyn_analysisresult_AsyncOperations](#BKMK_msdyn_analysisresult_AsyncOperations)
- [msdyn_analysisresultdetail_AsyncOperations](#BKMK_msdyn_analysisresultdetail_AsyncOperations)
- [msdyn_solutionhealthrule_AsyncOperations](#BKMK_msdyn_solutionhealthrule_AsyncOperations)
- [msdyn_solutionhealthruleargument_AsyncOperations](#BKMK_msdyn_solutionhealthruleargument_AsyncOperations)
- [msdyn_solutionhealthruleset_AsyncOperations](#BKMK_msdyn_solutionhealthruleset_AsyncOperations)


### <a name="BKMK_theme_AsyncOperations"></a> theme_AsyncOperations

See theme Entity [theme_AsyncOperations](theme.md#BKMK_theme_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_usermapping_AsyncOperations"></a> usermapping_AsyncOperations

See usermapping Entity [usermapping_AsyncOperations](usermapping.md#BKMK_usermapping_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_interactionforemail_AsyncOperations"></a> interactionforemail_AsyncOperations

See interactionforemail Entity [interactionforemail_AsyncOperations](interactionforemail.md#BKMK_interactionforemail_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_AsyncOperations"></a> knowledgearticle_AsyncOperations

See knowledgearticle Entity [knowledgearticle_AsyncOperations](knowledgearticle.md#BKMK_knowledgearticle_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_post_AsyncOperations"></a> post_AsyncOperations

See post Entity [post_AsyncOperations](post.md#BKMK_post_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_position_AsyncOperations"></a> position_AsyncOperations

See position Entity [position_AsyncOperations](position.md#BKMK_position_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_KnowledgeBaseRecord_AsyncOperations"></a> KnowledgeBaseRecord_AsyncOperations

See knowledgebaserecord Entity [KnowledgeBaseRecord_AsyncOperations](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_lk_asyncoperation_createdby"></a> lk_asyncoperation_createdby

See systemuser Entity [lk_asyncoperation_createdby](systemuser.md#BKMK_lk_asyncoperation_createdby) One-To-Many relationship.

### <a name="BKMK_MonthlyFiscalCalendar_AsyncOperations"></a> MonthlyFiscalCalendar_AsyncOperations

See monthlyfiscalcalendar Entity [MonthlyFiscalCalendar_AsyncOperations](monthlyfiscalcalendar.md#BKMK_MonthlyFiscalCalendar_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_lk_asyncoperation_workflowactivationid"></a> lk_asyncoperation_workflowactivationid

See workflow Entity [lk_asyncoperation_workflowactivationid](workflow.md#BKMK_lk_asyncoperation_workflowactivationid) One-To-Many relationship.

### <a name="BKMK_Report_AsyncOperations"></a> Report_AsyncOperations

See report Entity [Report_AsyncOperations](report.md#BKMK_Report_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_SocialActivity_AsyncOperations"></a> SocialActivity_AsyncOperations

See socialactivity Entity [SocialActivity_AsyncOperations](socialactivity.md#BKMK_SocialActivity_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Connection_Role_AsyncOperations"></a> Connection_Role_AsyncOperations

See connectionrole Entity [Connection_Role_AsyncOperations](connectionrole.md#BKMK_Connection_Role_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Team_AsyncOperations"></a> Team_AsyncOperations

See team Entity [Team_AsyncOperations](team.md#BKMK_Team_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_AnnualFiscalCalendar_AsyncOperations"></a> AnnualFiscalCalendar_AsyncOperations

See annualfiscalcalendar Entity [AnnualFiscalCalendar_AsyncOperations](annualfiscalcalendar.md#BKMK_AnnualFiscalCalendar_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_SharePointDocumentLocation_AsyncOperations"></a> SharePointDocumentLocation_AsyncOperations

See sharepointdocumentlocation Entity [SharePointDocumentLocation_AsyncOperations](sharepointdocumentlocation.md#BKMK_SharePointDocumentLocation_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_PhoneCall_AsyncOperations"></a> PhoneCall_AsyncOperations

See phonecall Entity [PhoneCall_AsyncOperations](phonecall.md#BKMK_PhoneCall_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_mailbox_asyncoperations"></a> mailbox_asyncoperations

See mailbox Entity [mailbox_asyncoperations](mailbox.md#BKMK_mailbox_asyncoperations) One-To-Many relationship.

### <a name="BKMK_PostFollow_AsyncOperations"></a> PostFollow_AsyncOperations

See postfollow Entity [PostFollow_AsyncOperations](postfollow.md#BKMK_PostFollow_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Appointment_AsyncOperations"></a> Appointment_AsyncOperations

See appointment Entity [Appointment_AsyncOperations](appointment.md#BKMK_Appointment_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_slabase_AsyncOperations"></a> slabase_AsyncOperations

See sla Entity [slabase_AsyncOperations](sla.md#BKMK_slabase_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_SavedQuery_AsyncOperations"></a> SavedQuery_AsyncOperations

See savedquery Entity [SavedQuery_AsyncOperations](savedquery.md#BKMK_SavedQuery_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_DisplayString_AsyncOperations"></a> DisplayString_AsyncOperations

See displaystring Entity [DisplayString_AsyncOperations](displaystring.md#BKMK_DisplayString_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_KbArticleComment_AsyncOperations"></a> KbArticleComment_AsyncOperations

See kbarticlecomment Entity [KbArticleComment_AsyncOperations](kbarticlecomment.md#BKMK_KbArticleComment_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_ActivityPointer_AsyncOperations"></a> ActivityPointer_AsyncOperations

See activitypointer Entity [ActivityPointer_AsyncOperations](activitypointer.md#BKMK_ActivityPointer_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Subject_AsyncOperations"></a> Subject_AsyncOperations

See subject Entity [Subject_AsyncOperations](subject.md#BKMK_Subject_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_goalrollupquery_AsyncOperations"></a> goalrollupquery_AsyncOperations

See goalrollupquery Entity [goalrollupquery_AsyncOperations](goalrollupquery.md#BKMK_goalrollupquery_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Role_AsyncOperations"></a> Role_AsyncOperations

See role Entity [Role_AsyncOperations](role.md#BKMK_Role_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_SystemForm_AsyncOperations"></a> SystemForm_AsyncOperations

See systemform Entity [SystemForm_AsyncOperations](systemform.md#BKMK_SystemForm_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Annotation_AsyncOperations"></a> Annotation_AsyncOperations

See annotation Entity [Annotation_AsyncOperations](annotation.md#BKMK_Annotation_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Privilege_AsyncOperations"></a> Privilege_AsyncOperations

See privilege Entity [Privilege_AsyncOperations](privilege.md#BKMK_Privilege_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_ActivityMimeAttachment_AsyncOperations"></a> ActivityMimeAttachment_AsyncOperations

See activitymimeattachment Entity [ActivityMimeAttachment_AsyncOperations](activitymimeattachment.md#BKMK_ActivityMimeAttachment_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Goal_AsyncOperations"></a> Goal_AsyncOperations

See goal Entity [Goal_AsyncOperations](goal.md#BKMK_Goal_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Fax_AsyncOperations"></a> Fax_AsyncOperations

See fax Entity [Fax_AsyncOperations](fax.md#BKMK_Fax_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_QuarterlyFiscalCalendar_AsyncOperations"></a> QuarterlyFiscalCalendar_AsyncOperations

See quarterlyfiscalcalendar Entity [QuarterlyFiscalCalendar_AsyncOperations](quarterlyfiscalcalendar.md#BKMK_QuarterlyFiscalCalendar_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_SharePointSite_AsyncOperations"></a> SharePointSite_AsyncOperations

See sharepointsite Entity [SharePointSite_AsyncOperations](sharepointsite.md#BKMK_SharePointSite_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_UserQuery_AsyncOperations"></a> UserQuery_AsyncOperations

See userquery Entity [UserQuery_AsyncOperations](userquery.md#BKMK_UserQuery_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_ImportMap_AsyncOperations"></a> ImportMap_AsyncOperations

See importmap Entity [ImportMap_AsyncOperations](importmap.md#BKMK_ImportMap_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_BusinessUnit_AsyncOperations"></a> BusinessUnit_AsyncOperations

See businessunit Entity [BusinessUnit_AsyncOperations](businessunit.md#BKMK_BusinessUnit_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Queue_AsyncOperations"></a> Queue_AsyncOperations

See queue Entity [Queue_AsyncOperations](queue.md#BKMK_Queue_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_QueueItem_AsyncOperations"></a> QueueItem_AsyncOperations

See queueitem Entity [QueueItem_AsyncOperations](queueitem.md#BKMK_QueueItem_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_team_asyncoperation"></a> team_asyncoperation

See team Entity [team_asyncoperation](team.md#BKMK_team_asyncoperation) One-To-Many relationship.

### <a name="BKMK_lk_asyncoperation_modifiedby"></a> lk_asyncoperation_modifiedby

See systemuser Entity [lk_asyncoperation_modifiedby](systemuser.md#BKMK_lk_asyncoperation_modifiedby) One-To-Many relationship.

### <a name="BKMK_UserForm_AsyncOperations"></a> UserForm_AsyncOperations

See userform Entity [UserForm_AsyncOperations](userform.md#BKMK_UserForm_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_AsyncOperations"></a> TransactionCurrency_AsyncOperations

See transactioncurrency Entity [TransactionCurrency_AsyncOperations](transactioncurrency.md#BKMK_TransactionCurrency_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_rollupfield_AsyncOperations"></a> rollupfield_AsyncOperations

See rollupfield Entity [rollupfield_AsyncOperations](rollupfield.md#BKMK_rollupfield_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Letter_AsyncOperations"></a> Letter_AsyncOperations

See letter Entity [Letter_AsyncOperations](letter.md#BKMK_Letter_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_KbArticle_AsyncOperations"></a> KbArticle_AsyncOperations

See kbarticle Entity [KbArticle_AsyncOperations](kbarticle.md#BKMK_KbArticle_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_RecurringAppointmentMaster_AsyncOperations"></a> RecurringAppointmentMaster_AsyncOperations

See recurringappointmentmaster Entity [RecurringAppointmentMaster_AsyncOperations](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Task_AsyncOperations"></a> Task_AsyncOperations

See task Entity [Task_AsyncOperations](task.md#BKMK_Task_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_BusinessUnitNewsArticle_AsyncOperations"></a> BusinessUnitNewsArticle_AsyncOperations

See businessunitnewsarticle Entity [BusinessUnitNewsArticle_AsyncOperations](businessunitnewsarticle.md#BKMK_BusinessUnitNewsArticle_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Connection_AsyncOperations"></a> Connection_AsyncOperations

See connection Entity [Connection_AsyncOperations](connection.md#BKMK_Connection_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_SystemUser_AsyncOperations"></a> SystemUser_AsyncOperations

See systemuser Entity [SystemUser_AsyncOperations](systemuser.md#BKMK_SystemUser_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_KbArticleTemplate_AsyncOperations"></a> KbArticleTemplate_AsyncOperations

See kbarticletemplate Entity [KbArticleTemplate_AsyncOperations](kbarticletemplate.md#BKMK_KbArticleTemplate_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_SdkMessageProcessingStep_AsyncOperations"></a> SdkMessageProcessingStep_AsyncOperations

See sdkmessageprocessingstep Entity [SdkMessageProcessingStep_AsyncOperations](sdkmessageprocessingstep.md#BKMK_SdkMessageProcessingStep_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Template_AsyncOperations"></a> Template_AsyncOperations

See template Entity [Template_AsyncOperations](template.md#BKMK_Template_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_CustomerAddress_AsyncOperations"></a> CustomerAddress_AsyncOperations

See customeraddress Entity [CustomerAddress_AsyncOperations](customeraddress.md#BKMK_CustomerAddress_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Contact_AsyncOperations"></a> Contact_AsyncOperations

See contact Entity [Contact_AsyncOperations](contact.md#BKMK_Contact_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_emailserverprofile_asyncoperations"></a> emailserverprofile_asyncoperations

See emailserverprofile Entity [emailserverprofile_asyncoperations](emailserverprofile.md#BKMK_emailserverprofile_asyncoperations) One-To-Many relationship.

### <a name="BKMK_lk_asyncoperation_createdonbehalfby"></a> lk_asyncoperation_createdonbehalfby

See systemuser Entity [lk_asyncoperation_createdonbehalfby](systemuser.md#BKMK_lk_asyncoperation_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_Import_AsyncOperations"></a> Import_AsyncOperations

See import Entity [Import_AsyncOperations](import.md#BKMK_Import_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_system_user_asyncoperation"></a> system_user_asyncoperation

See systemuser Entity [system_user_asyncoperation](systemuser.md#BKMK_system_user_asyncoperation) One-To-Many relationship.

### <a name="BKMK_business_unit_asyncoperation"></a> business_unit_asyncoperation

See businessunit Entity [business_unit_asyncoperation](businessunit.md#BKMK_business_unit_asyncoperation) One-To-Many relationship.

### <a name="BKMK_ImportLog_AsyncOperations"></a> ImportLog_AsyncOperations

See importlog Entity [ImportLog_AsyncOperations](importlog.md#BKMK_ImportLog_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_metric_AsyncOperations"></a> metric_AsyncOperations

See metric Entity [metric_AsyncOperations](metric.md#BKMK_metric_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_SocialProfile_AsyncOperations"></a> SocialProfile_AsyncOperations

See socialprofile Entity [SocialProfile_AsyncOperations](socialprofile.md#BKMK_SocialProfile_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_lk_asyncoperation_modifiedonbehalfby"></a> lk_asyncoperation_modifiedonbehalfby

See systemuser Entity [lk_asyncoperation_modifiedonbehalfby](systemuser.md#BKMK_lk_asyncoperation_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_Account_AsyncOperations"></a> Account_AsyncOperations

See account Entity [Account_AsyncOperations](account.md#BKMK_Account_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Email_AsyncOperations"></a> Email_AsyncOperations

See email Entity [Email_AsyncOperations](email.md#BKMK_Email_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_FixedMonthlyFiscalCalendar_AsyncOperations"></a> FixedMonthlyFiscalCalendar_AsyncOperations

See fixedmonthlyfiscalcalendar Entity [FixedMonthlyFiscalCalendar_AsyncOperations](fixedmonthlyfiscalcalendar.md#BKMK_FixedMonthlyFiscalCalendar_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_SemiAnnualFiscalCalendar_AsyncOperations"></a> SemiAnnualFiscalCalendar_AsyncOperations

See semiannualfiscalcalendar Entity [SemiAnnualFiscalCalendar_AsyncOperations](semiannualfiscalcalendar.md#BKMK_SemiAnnualFiscalCalendar_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_MailMergeTemplate_AsyncOperations"></a> MailMergeTemplate_AsyncOperations

See mailmergetemplate Entity [MailMergeTemplate_AsyncOperations](mailmergetemplate.md#BKMK_MailMergeTemplate_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Organization_AsyncOperations"></a> Organization_AsyncOperations

See organization Entity [Organization_AsyncOperations](organization.md#BKMK_Organization_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Calendar_AsyncOperations"></a> Calendar_AsyncOperations

See calendar Entity [Calendar_AsyncOperations](calendar.md#BKMK_Calendar_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_ImportFile_AsyncOperations"></a> ImportFile_AsyncOperations

See importfile Entity [ImportFile_AsyncOperations](importfile.md#BKMK_ImportFile_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Territory_AsyncOperations"></a> Territory_AsyncOperations

**Added by**: Application Common Solution

See territory Entity [Territory_AsyncOperations](territory.md#BKMK_Territory_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgearticleimage_AsyncOperations"></a> msdyn_knowledgearticleimage_AsyncOperations

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgearticleimage Entity [msdyn_knowledgearticleimage_AsyncOperations](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgearticletemplate_AsyncOperations"></a> msdyn_knowledgearticletemplate_AsyncOperations

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgearticletemplate Entity [msdyn_knowledgearticletemplate_AsyncOperations](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_attributeimageconfig_AsyncOperations"></a> attributeimageconfig_AsyncOperations

**Added by**: Image Configuration Solution

See attributeimageconfig Entity [attributeimageconfig_AsyncOperations](attributeimageconfig.md#BKMK_attributeimageconfig_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_entityimageconfig_AsyncOperations"></a> entityimageconfig_AsyncOperations

**Added by**: Image Configuration Solution

See entityimageconfig Entity [entityimageconfig_AsyncOperations](entityimageconfig.md#BKMK_entityimageconfig_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_entityanalyticsconfig_AsyncOperations"></a> entityanalyticsconfig_AsyncOperations

**Added by**: Advanced Analytics Infrastructure Solution

See entityanalyticsconfig Entity [entityanalyticsconfig_AsyncOperations](entityanalyticsconfig.md#BKMK_entityanalyticsconfig_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_connector_AsyncOperations"></a> connector_AsyncOperations

**Added by**: Power Connector Solution Solution

See connector Entity [connector_AsyncOperations](connector.md#BKMK_connector_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_msdyn_aiconfiguration_AsyncOperations"></a> msdyn_aiconfiguration_AsyncOperations

**Added by**: AISolution Solution

See msdyn_aiconfiguration Entity [msdyn_aiconfiguration_AsyncOperations](msdyn_aiconfiguration.md#BKMK_msdyn_aiconfiguration_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_msdyn_aimodel_AsyncOperations"></a> msdyn_aimodel_AsyncOperations

**Added by**: AISolution Solution

See msdyn_aimodel Entity [msdyn_aimodel_AsyncOperations](msdyn_aimodel.md#BKMK_msdyn_aimodel_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_msdyn_aitemplate_AsyncOperations"></a> msdyn_aitemplate_AsyncOperations

**Added by**: AISolution Solution

See msdyn_aitemplate Entity [msdyn_aitemplate_AsyncOperations](msdyn_aitemplate.md#BKMK_msdyn_aitemplate_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_msdyn_aifptrainingdocument_AsyncOperations"></a> msdyn_aifptrainingdocument_AsyncOperations

**Added by**: AI Solution default templates Solution

See msdyn_aifptrainingdocument Entity [msdyn_aifptrainingdocument_AsyncOperations](msdyn_aifptrainingdocument.md#BKMK_msdyn_aifptrainingdocument_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodimage_AsyncOperations"></a> msdyn_aiodimage_AsyncOperations

**Added by**: AI Solution default templates Solution

See msdyn_aiodimage Entity [msdyn_aiodimage_AsyncOperations](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodlabel_AsyncOperations"></a> msdyn_aiodlabel_AsyncOperations

**Added by**: AI Solution default templates Solution

See msdyn_aiodlabel Entity [msdyn_aiodlabel_AsyncOperations](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodtrainingboundingbox_AsyncOperations"></a> msdyn_aiodtrainingboundingbox_AsyncOperations

**Added by**: AI Solution default templates Solution

See msdyn_aiodtrainingboundingbox Entity [msdyn_aiodtrainingboundingbox_AsyncOperations](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodtrainingimage_AsyncOperations"></a> msdyn_aiodtrainingimage_AsyncOperations

**Added by**: AI Solution default templates Solution

See msdyn_aiodtrainingimage Entity [msdyn_aiodtrainingimage_AsyncOperations](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_flowsession_AsyncOperations"></a> flowsession_AsyncOperations

**Added by**: Power Automate Extensions package Solution

See flowsession Entity [flowsession_AsyncOperations](flowsession.md#BKMK_flowsession_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_workflowbinary_AsyncOperations"></a> workflowbinary_AsyncOperations

**Added by**: Power Automate Extensions package Solution

See workflowbinary Entity [workflowbinary_AsyncOperations](workflowbinary.md#BKMK_workflowbinary_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_environmentvariabledefinition_AsyncOperations"></a> environmentvariabledefinition_AsyncOperations

**Added by**: Environment Variables Solution

See environmentvariabledefinition Entity [environmentvariabledefinition_AsyncOperations](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_environmentvariablevalue_AsyncOperations"></a> environmentvariablevalue_AsyncOperations

**Added by**: Environment Variables Solution

See environmentvariablevalue Entity [environmentvariablevalue_AsyncOperations](environmentvariablevalue.md#BKMK_environmentvariablevalue_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_msdyn_analysiscomponent_AsyncOperations"></a> msdyn_analysiscomponent_AsyncOperations

**Added by**: Power Apps Checker Solution

See msdyn_analysiscomponent Entity [msdyn_analysiscomponent_AsyncOperations](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisjob_AsyncOperations"></a> msdyn_analysisjob_AsyncOperations

**Added by**: Power Apps Checker Solution

See msdyn_analysisjob Entity [msdyn_analysisjob_AsyncOperations](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisresult_AsyncOperations"></a> msdyn_analysisresult_AsyncOperations

**Added by**: Power Apps Checker Solution

See msdyn_analysisresult Entity [msdyn_analysisresult_AsyncOperations](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisresultdetail_AsyncOperations"></a> msdyn_analysisresultdetail_AsyncOperations

**Added by**: Power Apps Checker Solution

See msdyn_analysisresultdetail Entity [msdyn_analysisresultdetail_AsyncOperations](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthrule_AsyncOperations"></a> msdyn_solutionhealthrule_AsyncOperations

**Added by**: Power Apps Checker Solution

See msdyn_solutionhealthrule Entity [msdyn_solutionhealthrule_AsyncOperations](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthruleargument_AsyncOperations"></a> msdyn_solutionhealthruleargument_AsyncOperations

**Added by**: Power Apps Checker Solution

See msdyn_solutionhealthruleargument Entity [msdyn_solutionhealthruleargument_AsyncOperations](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthruleset_AsyncOperations"></a> msdyn_solutionhealthruleset_AsyncOperations

**Added by**: Power Apps Checker Solution

See msdyn_solutionhealthruleset Entity [msdyn_solutionhealthruleset_AsyncOperations](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_AsyncOperations) One-To-Many relationship.

### See also

[About the Entity Reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.asyncoperation?text=asyncoperation EntityType" />