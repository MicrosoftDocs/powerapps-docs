---
title: "AsyncOperation Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the AsyncOperation entity."
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/07/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# AsyncOperation Entity Reference

Process whose execution can proceed independently or in the background.

## Entity Properties

**DisplayName**: System Job<br />
**DisplayCollectionName**: System Jobs<br />
**SchemaName**: AsyncOperation<br />
**CollectionSchemaName**: AsyncOperations<br />
**LogicalName**: asyncoperation<br />
**LogicalCollectionName**: asyncoperations<br />
**EntitySetName**: asyncoperations<br />
**PrimaryIdAttribute**: asyncoperationid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AsyncOperationId](#BKMK_AsyncOperationId)
- [CorrelationId](#BKMK_CorrelationId)
- [CorrelationUpdatedTime](#BKMK_CorrelationUpdatedTime)
- [Data](#BKMK_Data)
- [DependencyToken](#BKMK_DependencyToken)
- [Depth](#BKMK_Depth)
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


### <a name="BKMK_AsyncOperationId"></a> AsyncOperationId

**Description**: Unique identifier of the system job.<br />
**DisplayName**: System Job<br />
**LogicalName**: asyncoperationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_CorrelationId"></a> CorrelationId

**Description**: Unique identifier used to correlate between multiple SDK requests and system jobs.<br />
**DisplayName**: Correlation Id<br />
**LogicalName**: correlationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_CorrelationUpdatedTime"></a> CorrelationUpdatedTime

**Description**: Last time the correlation depth was updated.<br />
**DisplayName**: Correlation Updated Time<br />
**LogicalName**: correlationupdatedtime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_Data"></a> Data

**Description**: Unstructured data associated with the system job.<br />
**DisplayName**: Data<br />
**LogicalName**: data<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_DependencyToken"></a> DependencyToken

**Description**: Execution of all operations with the same dependency token is serialized.<br />
**DisplayName**: Dependency Token<br />
**LogicalName**: dependencytoken<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_Depth"></a> Depth

**Description**: Number of SDK calls made since the first call.<br />
**DisplayName**: Depth<br />
**LogicalName**: depth<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_FriendlyMessage"></a> FriendlyMessage

**Description**: Message provided by the system job.<br />
**DisplayName**: Friendly message<br />
**LogicalName**: friendlymessage<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Memo<br />
**Format**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100000


### <a name="BKMK_HostId"></a> HostId

**Description**: Unique identifier of the host that owns this system job.<br />
**DisplayName**: Host<br />
**LogicalName**: hostid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_MessageName"></a> MessageName

**Description**: Name of the message that started this system job.<br />
**DisplayName**: Message Name<br />
**LogicalName**: messagename<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_Name"></a> Name

**Description**: Name of the system job.<br />
**DisplayName**: System Job Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_OperationType"></a> OperationType

**Description**: Type of the system job.<br />
**DisplayName**: System Job Type<br />
**LogicalName**: operationtype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: System Event
- **Value**: 2 **Label**: Bulk Email
- **Value**: 3 **Label**: Import File Parse
- **Value**: 4 **Label**: Transform Parse Data
- **Value**: 5 **Label**: Import
- **Value**: 6 **Label**: Activity Propagation
- **Value**: 7 **Label**: Duplicate Detection Rule Publish
- **Value**: 8 **Label**: Bulk Duplicate Detection
- **Value**: 9 **Label**: SQM Data Collection
- **Value**: 10 **Label**: Workflow
- **Value**: 11 **Label**: Quick Campaign
- **Value**: 12 **Label**: Matchcode Update
- **Value**: 13 **Label**: Bulk Delete
- **Value**: 14 **Label**: Deletion Service
- **Value**: 15 **Label**: Index Management
- **Value**: 16 **Label**: Collect Organization Statistics
- **Value**: 17 **Label**: Import Subprocess
- **Value**: 18 **Label**: Calculate Organization Storage Size
- **Value**: 19 **Label**: Collect Organization Database Statistics
- **Value**: 20 **Label**: Collection Organization Size Statistics
- **Value**: 21 **Label**: Database Tuning
- **Value**: 22 **Label**: Calculate Organization Maximum Storage Size
- **Value**: 23 **Label**: Bulk Delete Subprocess
- **Value**: 24 **Label**: Update Statistic Intervals
- **Value**: 25 **Label**: Organization Full Text Catalog Index
- **Value**: 26 **Label**: Database log backup
- **Value**: 27 **Label**: Update Contract States
- **Value**: 28 **Label**: DBCC SHRINKDATABASE maintenance job
- **Value**: 29 **Label**: DBCC SHRINKFILE maintenance job
- **Value**: 30 **Label**: Reindex all indices maintenance job
- **Value**: 31 **Label**: Storage Limit Notification
- **Value**: 32 **Label**: Cleanup inactive workflow assemblies
- **Value**: 35 **Label**: Recurring Series Expansion
- **Value**: 38 **Label**: Import Sample Data
- **Value**: 40 **Label**: Goal Roll Up
- **Value**: 41 **Label**: Audit Partition Creation
- **Value**: 42 **Label**: Check For Language Pack Updates
- **Value**: 43 **Label**: Provision Language Pack
- **Value**: 44 **Label**: Update Organization Database
- **Value**: 45 **Label**: Update Solution
- **Value**: 46 **Label**: Regenerate Entity Row Count Snapshot Data
- **Value**: 47 **Label**: Regenerate Read Share Snapshot Data
- **Value**: 49 **Label**: Post to Yammer
- **Value**: 50 **Label**: Outgoing Activity
- **Value**: 51 **Label**: Incoming Email Processing
- **Value**: 52 **Label**: Mailbox Test Access
- **Value**: 53 **Label**: Encryption Health Check
- **Value**: 54 **Label**: Execute Async Request
- **Value**: 56 **Label**: Update Entitlement States
- **Value**: 57 **Label**: Calculate Rollup Field
- **Value**: 58 **Label**: Mass Calculate Rollup Field
- **Value**: 59 **Label**: Import Translation
- **Value**: 62 **Label**: Convert Date And Time Behavior
- **Value**: 63 **Label**: EntityKey Index Creation
- **Value**: 65 **Label**: Update Knowledge Article States
- **Value**: 68 **Label**: Resource Booking Sync
- **Value**: 69 **Label**: Relationship Assistant Cards
- **Value**: 71 **Label**: Cleanup Solution Components
- **Value**: 72 **Label**: App Module Metadata Operation
- **Value**: 73 **Label**: ALM Anomaly Detection Operation



### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Unique identifier of the user or team who owns the system job.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_OwningExtensionId"></a> OwningExtensionId

**Description**: Unique identifier of the owning extension with which the system job is associated.<br />
**DisplayName**: Owning Extension<br />
**LogicalName**: owningextensionid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: sdkmessageprocessingstep


### <a name="BKMK_OwningExtensionIdName"></a> OwningExtensionIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owningextensionidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_OwningExtensionTypeCode"></a> OwningExtensionTypeCode

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owningextensiontypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_ParentPluginExecutionId"></a> ParentPluginExecutionId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: parentpluginexecutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_PostponeUntil"></a> PostponeUntil

**Description**: Indicates whether the system job should run only after the specified date and time.<br />
**DisplayName**: Postpone Until<br />
**LogicalName**: postponeuntil<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_PrimaryEntityType"></a> PrimaryEntityType

**Description**: Type of entity with which the system job is primarily associated.<br />
**DisplayName**: Primary Entity Type<br />
**LogicalName**: primaryentitytype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_RecurrencePattern"></a> RecurrencePattern

**Description**: Pattern of the system job's recurrence.<br />
**DisplayName**: Recurrence Pattern<br />
**LogicalName**: recurrencepattern<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_RecurrenceStartTime"></a> RecurrenceStartTime

**Description**: Starting time in UTC for the recurrence pattern.<br />
**DisplayName**: Recurrence Start<br />
**LogicalName**: recurrencestarttime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

**Description**: Unique identifier of the object with which the system job is associated.<br />
**DisplayName**: Regarding<br />
**LogicalName**: regardingobjectid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: account,activitymimeattachment,activitypointer,annotation,annualfiscalcalendar,appointment,attributemap,businessunit,businessunitnewsarticle,calendar,channelaccessprofile,channelaccessprofilerule,connection,connectionrole,contact,convertrule,customeraddress,customerrelationship,displaystring,email,emailserverprofile,entitymap,externalparty,externalpartyitem,fax,fixedmonthlyfiscalcalendar,goal,goalrollupquery,import,importdata,importfile,importlog,importmap,interactionforemail,isvconfig,kbarticle,kbarticlecomment,kbarticletemplate,knowledgearticle,knowledgebaserecord,letter,mailbox,mailmergetemplate,metric,monthlyfiscalcalendar,organization,phonecall,position,post,postfollow,privilege,quarterlyfiscalcalendar,queue,queueitem,recurringappointmentmaster,relationshiprole,relationshiprolemap,report,role,rollupfield,routingrule,routingruleitem,savedquery,semiannualfiscalcalendar,sharepointdocumentlocation,sharepointsite,similarityrule,sla,socialactivity,socialprofile,subject,systemform,systemuser,task,team,template,territory,theme,transactioncurrency,userform,usermapping,userquery


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjectidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_RegardingObjectIdYomiName"></a> RegardingObjectIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjectidyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_RequestId"></a> RequestId

**Description**: Unique identifier of the request that generated the system job.<br />
**DisplayName**: Request<br />
**LogicalName**: requestid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_RootExecutionContext"></a> RootExecutionContext

**Description**: Root execution context of the job that trigerred async job.<br />
**DisplayName**: RootExecutionContext<br />
**LogicalName**: rootexecutioncontext<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_StateCode"></a> StateCode

**Description**: Status of the system job.<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Ready **DefaultStatus**: 0 **InvariantName**: Ready
- **Value**: 1 **Label**: Suspended **DefaultStatus**: 10 **InvariantName**: Suspended
- **Value**: 2 **Label**: Locked **DefaultStatus**: 20 **InvariantName**: Locked
- **Value**: 3 **Label**: Completed **DefaultStatus**: 30 **InvariantName**: Completed



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Reason for the status of the system job.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Status<br />
**Options**:

- **Value**: 0 **Label**: Waiting For Resources **State**: 0
- **Value**: 10 **Label**: Waiting **State**: 1
- **Value**: 20 **Label**: In Progress **State**: 2
- **Value**: 21 **Label**: Pausing **State**: 2
- **Value**: 22 **Label**: Canceling **State**: 2
- **Value**: 30 **Label**: Succeeded **State**: 3
- **Value**: 31 **Label**: Failed **State**: 3
- **Value**: 32 **Label**: Canceled **State**: 3



### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: timezoneruleversionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

**Description**: Time zone code that was in use when the record was created.<br />
**DisplayName**: <br />
**LogicalName**: utcconversiontimezonecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_WorkflowActivationId"></a> WorkflowActivationId

**Description**: Unique identifier of the workflow activation related to the system job.<br />
**DisplayName**: Workflow Activation Id<br />
**LogicalName**: workflowactivationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: workflow

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

**Description**: Date and time when the system job was completed.<br />
**DisplayName**: Completed On<br />
**LogicalName**: completedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the system job.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the system job was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the asyncoperation.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ErrorCode"></a> ErrorCode

**Description**: Error code returned from a canceled system job.<br />
**DisplayName**: Error Code<br />
**LogicalName**: errorcode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_ExecutionTimeSpan"></a> ExecutionTimeSpan

**Description**: Time that the system job has taken to execute.<br />
**DisplayName**: ExecutionTimeSpan<br />
**LogicalName**: executiontimespan<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Double<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0<br />
**Precision**: 2


### <a name="BKMK_IsWaitingForEvent"></a> IsWaitingForEvent

**Description**: Indicates that the system job is waiting for an event.<br />
**DisplayName**: Waiting for Event<br />
**LogicalName**: iswaitingforevent<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_Message"></a> Message

**Description**: Message related to the system job.<br />
**DisplayName**: Message<br />
**LogicalName**: message<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100000


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the system job.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Description**: Name of the user who last modified the record.<br />
**DisplayName**: <br />
**LogicalName**: modifiedbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

**Description**: YomiName of the user who last modified the record.<br />
**DisplayName**: <br />
**LogicalName**: modifiedbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the system job was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the asyncoperation.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Description**: Unique identifier of the business unit that owns the system job.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier of the team who owns the record.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns the record.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_RetryCount"></a> RetryCount

**Description**: Number of times to retry the system job.<br />
**DisplayName**: Retry Count<br />
**LogicalName**: retrycount<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_Sequence"></a> Sequence

**Description**: Order in which operations were submitted.<br />
**DisplayName**: Sequence<br />
**LogicalName**: sequence<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />


### <a name="BKMK_StartedOn"></a> StartedOn

**Description**: Date and time when the system job was started.<br />
**DisplayName**: Started On<br />
**LogicalName**: startedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_Subtype"></a> Subtype

**Description**: The Subtype of the Async Job<br />
**DisplayName**: Subtype<br />
**LogicalName**: subtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 255<br />
**MinValue**: 0


### <a name="BKMK_WorkflowActivationIdName"></a> WorkflowActivationIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: workflowactivationidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_WorkflowIsBlocked"></a> WorkflowIsBlocked

**Description**: Indicates whether the workflow instance was blocked when it was persisted.<br />
**DisplayName**: Workflow Is Blocked<br />
**LogicalName**: workflowisblocked<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_WorkflowStageName"></a> WorkflowStageName

**Description**: Name of a workflow stage.<br />
**DisplayName**: Workflow Stage<br />
**LogicalName**: workflowstagename<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_WorkflowState"></a> WorkflowState

**Description**: State of the workflow job.<br />
**DisplayName**: Workflow State<br />
**LogicalName**: workflowstate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823

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
- [userentityinstancedata_asyncoperation](#BKMK_userentityinstancedata_asyncoperation)


### <a name="BKMK_AsyncOperation_MailboxTrackingFolder"></a> AsyncOperation_MailboxTrackingFolder

Same as mailboxtrackingfolder entity [AsyncOperation_MailboxTrackingFolder](mailboxtrackingfolder.md#BKMK_AsyncOperation_MailboxTrackingFolder) Many-To-One relationship.

**ReferencingEntity**: mailboxtrackingfolder<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: AsyncOperation_MailboxTrackingFolder<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_AsyncOperation_BulkDeleteOperation"></a> AsyncOperation_BulkDeleteOperation

Same as bulkdeleteoperation entity [AsyncOperation_BulkDeleteOperation](bulkdeleteoperation.md#BKMK_AsyncOperation_BulkDeleteOperation) Many-To-One relationship.

**ReferencingEntity**: bulkdeleteoperation<br />
**ReferencingAttribute**: asyncoperationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: AsyncOperation_BulkDeleteOperation<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_lk_workflowlog_asyncoperation_childworkflow"></a> lk_workflowlog_asyncoperation_childworkflow

Same as workflowlog entity [lk_workflowlog_asyncoperation_childworkflow](workflowlog.md#BKMK_lk_workflowlog_asyncoperation_childworkflow) Many-To-One relationship.

**ReferencingEntity**: workflowlog<br />
**ReferencingAttribute**: childworkflowinstanceid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_workflowlog_asyncoperation_childworkflow<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_AsyncOperation_Emails"></a> AsyncOperation_Emails

Same as email entity [AsyncOperation_Emails](email.md#BKMK_AsyncOperation_Emails) Many-To-One relationship.

**ReferencingEntity**: email<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: AsyncOperation_Emails<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_AsyncOperation_DuplicateBaseRecord"></a> AsyncOperation_DuplicateBaseRecord

Same as duplicaterecord entity [AsyncOperation_DuplicateBaseRecord](duplicaterecord.md#BKMK_AsyncOperation_DuplicateBaseRecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: asyncoperationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: AsyncOperation_DuplicateBaseRecord<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_lk_workflowlog_asyncoperations"></a> lk_workflowlog_asyncoperations

Same as workflowlog entity [lk_workflowlog_asyncoperations](workflowlog.md#BKMK_lk_workflowlog_asyncoperations) Many-To-One relationship.

**ReferencingEntity**: workflowlog<br />
**ReferencingAttribute**: asyncoperationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_workflowlog_asyncoperations<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_AsyncOperation_SocialActivities"></a> AsyncOperation_SocialActivities

Same as socialactivity entity [AsyncOperation_SocialActivities](socialactivity.md#BKMK_AsyncOperation_SocialActivities) Many-To-One relationship.

**ReferencingEntity**: socialactivity<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: AsyncOperation_SocialActivities<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_userentityinstancedata_asyncoperation"></a> userentityinstancedata_asyncoperation

Same as userentityinstancedata entity [userentityinstancedata_asyncoperation](userentityinstancedata.md#BKMK_userentityinstancedata_asyncoperation) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_asyncoperation<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [Territory_AsyncOperations](#BKMK_Territory_AsyncOperations)
- [theme_AsyncOperations](#BKMK_theme_AsyncOperations)
- [usermapping_AsyncOperations](#BKMK_usermapping_AsyncOperations)
- [interactionforemail_AsyncOperations](#BKMK_interactionforemail_AsyncOperations)
- [knowledgearticle_AsyncOperations](#BKMK_knowledgearticle_AsyncOperations)
- [post_AsyncOperations](#BKMK_post_AsyncOperations)
- [position_AsyncOperations](#BKMK_position_AsyncOperations)
- [channelaccessprofile_AsyncOperations](#BKMK_channelaccessprofile_AsyncOperations)
- [externalparty_AsyncOperations](#BKMK_externalparty_AsyncOperations)
- [profilerule_AsyncOperations](#BKMK_profilerule_AsyncOperations)
- [KnowledgeBaseRecord_AsyncOperations](#BKMK_KnowledgeBaseRecord_AsyncOperations)
- [lk_asyncoperation_createdby](#BKMK_lk_asyncoperation_createdby)
- [MonthlyFiscalCalendar_AsyncOperations](#BKMK_MonthlyFiscalCalendar_AsyncOperations)
- [lk_asyncoperation_workflowactivationid](#BKMK_lk_asyncoperation_workflowactivationid)
- [Report_AsyncOperations](#BKMK_Report_AsyncOperations)
- [SocialActivity_AsyncOperations](#BKMK_SocialActivity_AsyncOperations)
- [Connection_Role_AsyncOperations](#BKMK_Connection_Role_AsyncOperations)
- [routingruleitem_AsyncOperations](#BKMK_routingruleitem_AsyncOperations)
- [Team_AsyncOperations](#BKMK_Team_AsyncOperations)
- [AnnualFiscalCalendar_AsyncOperations](#BKMK_AnnualFiscalCalendar_AsyncOperations)
- [SharePointDocumentLocation_AsyncOperations](#BKMK_SharePointDocumentLocation_AsyncOperations)
- [PhoneCall_AsyncOperations](#BKMK_PhoneCall_AsyncOperations)
- [Convertrule_AsyncOperations](#BKMK_Convertrule_AsyncOperations)
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
- [routingrule_AsyncOperations](#BKMK_routingrule_AsyncOperations)
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
- [RelationshipRoleMap_AsyncOperations](#BKMK_RelationshipRoleMap_AsyncOperations)
- [team_asyncoperation](#BKMK_team_asyncoperation)
- [lk_asyncoperation_modifiedby](#BKMK_lk_asyncoperation_modifiedby)
- [CustomerRelationship_AsyncOperations](#BKMK_CustomerRelationship_AsyncOperations)
- [UserForm_AsyncOperations](#BKMK_UserForm_AsyncOperations)
- [RelationshipRole_AsyncOperations](#BKMK_RelationshipRole_AsyncOperations)
- [TransactionCurrency_AsyncOperations](#BKMK_TransactionCurrency_AsyncOperations)
- [rollupfield_AsyncOperations](#BKMK_rollupfield_AsyncOperations)
- [Letter_AsyncOperations](#BKMK_Letter_AsyncOperations)
- [KbArticle_AsyncOperations](#BKMK_KbArticle_AsyncOperations)
- [EntityMap_AsyncOperations](#BKMK_EntityMap_AsyncOperations)
- [RecurringAppointmentMaster_AsyncOperations](#BKMK_RecurringAppointmentMaster_AsyncOperations)
- [IsvConfig_AsyncOperations](#BKMK_IsvConfig_AsyncOperations)
- [Task_AsyncOperations](#BKMK_Task_AsyncOperations)
- [BusinessUnitNewsArticle_AsyncOperations](#BKMK_BusinessUnitNewsArticle_AsyncOperations)
- [AttributeMap_AsyncOperations](#BKMK_AttributeMap_AsyncOperations)
- [Connection_AsyncOperations](#BKMK_Connection_AsyncOperations)
- [SystemUser_AsyncOperations](#BKMK_SystemUser_AsyncOperations)
- [KbArticleTemplate_AsyncOperations](#BKMK_KbArticleTemplate_AsyncOperations)
- [SdkMessageProcessingStep_AsyncOperations](#BKMK_SdkMessageProcessingStep_AsyncOperations)
- [externalpartyitem_AsyncOperations](#BKMK_externalpartyitem_AsyncOperations)
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


### <a name="BKMK_Territory_AsyncOperations"></a> Territory_AsyncOperations

See territory Entity [Territory_AsyncOperations](territory.md#BKMK_Territory_AsyncOperations) One-To-Many relationship.

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

### <a name="BKMK_channelaccessprofile_AsyncOperations"></a> channelaccessprofile_AsyncOperations

See channelaccessprofile Entity [channelaccessprofile_AsyncOperations](channelaccessprofile.md#BKMK_channelaccessprofile_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_externalparty_AsyncOperations"></a> externalparty_AsyncOperations

See externalparty Entity [externalparty_AsyncOperations](externalparty.md#BKMK_externalparty_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_profilerule_AsyncOperations"></a> profilerule_AsyncOperations

See channelaccessprofilerule Entity [profilerule_AsyncOperations](channelaccessprofilerule.md#BKMK_profilerule_AsyncOperations) One-To-Many relationship.

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

### <a name="BKMK_routingruleitem_AsyncOperations"></a> routingruleitem_AsyncOperations

See routingruleitem Entity [routingruleitem_AsyncOperations](routingruleitem.md#BKMK_routingruleitem_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Team_AsyncOperations"></a> Team_AsyncOperations

See team Entity [Team_AsyncOperations](team.md#BKMK_Team_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_AnnualFiscalCalendar_AsyncOperations"></a> AnnualFiscalCalendar_AsyncOperations

See annualfiscalcalendar Entity [AnnualFiscalCalendar_AsyncOperations](annualfiscalcalendar.md#BKMK_AnnualFiscalCalendar_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_SharePointDocumentLocation_AsyncOperations"></a> SharePointDocumentLocation_AsyncOperations

See sharepointdocumentlocation Entity [SharePointDocumentLocation_AsyncOperations](sharepointdocumentlocation.md#BKMK_SharePointDocumentLocation_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_PhoneCall_AsyncOperations"></a> PhoneCall_AsyncOperations

See phonecall Entity [PhoneCall_AsyncOperations](phonecall.md#BKMK_PhoneCall_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Convertrule_AsyncOperations"></a> Convertrule_AsyncOperations

See convertrule Entity [Convertrule_AsyncOperations](convertrule.md#BKMK_Convertrule_AsyncOperations) One-To-Many relationship.

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

### <a name="BKMK_routingrule_AsyncOperations"></a> routingrule_AsyncOperations

See routingrule Entity [routingrule_AsyncOperations](routingrule.md#BKMK_routingrule_AsyncOperations) One-To-Many relationship.

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

### <a name="BKMK_RelationshipRoleMap_AsyncOperations"></a> RelationshipRoleMap_AsyncOperations

See relationshiprolemap Entity [RelationshipRoleMap_AsyncOperations](relationshiprolemap.md#BKMK_RelationshipRoleMap_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_team_asyncoperation"></a> team_asyncoperation

See team Entity [team_asyncoperation](team.md#BKMK_team_asyncoperation) One-To-Many relationship.

### <a name="BKMK_lk_asyncoperation_modifiedby"></a> lk_asyncoperation_modifiedby

See systemuser Entity [lk_asyncoperation_modifiedby](systemuser.md#BKMK_lk_asyncoperation_modifiedby) One-To-Many relationship.

### <a name="BKMK_CustomerRelationship_AsyncOperations"></a> CustomerRelationship_AsyncOperations

See customerrelationship Entity [CustomerRelationship_AsyncOperations](customerrelationship.md#BKMK_CustomerRelationship_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_UserForm_AsyncOperations"></a> UserForm_AsyncOperations

See userform Entity [UserForm_AsyncOperations](userform.md#BKMK_UserForm_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_RelationshipRole_AsyncOperations"></a> RelationshipRole_AsyncOperations

See relationshiprole Entity [RelationshipRole_AsyncOperations](relationshiprole.md#BKMK_RelationshipRole_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_AsyncOperations"></a> TransactionCurrency_AsyncOperations

See transactioncurrency Entity [TransactionCurrency_AsyncOperations](transactioncurrency.md#BKMK_TransactionCurrency_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_rollupfield_AsyncOperations"></a> rollupfield_AsyncOperations

See rollupfield Entity [rollupfield_AsyncOperations](rollupfield.md#BKMK_rollupfield_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Letter_AsyncOperations"></a> Letter_AsyncOperations

See letter Entity [Letter_AsyncOperations](letter.md#BKMK_Letter_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_KbArticle_AsyncOperations"></a> KbArticle_AsyncOperations

See kbarticle Entity [KbArticle_AsyncOperations](kbarticle.md#BKMK_KbArticle_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_EntityMap_AsyncOperations"></a> EntityMap_AsyncOperations

See entitymap Entity [EntityMap_AsyncOperations](entitymap.md#BKMK_EntityMap_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_RecurringAppointmentMaster_AsyncOperations"></a> RecurringAppointmentMaster_AsyncOperations

See recurringappointmentmaster Entity [RecurringAppointmentMaster_AsyncOperations](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_IsvConfig_AsyncOperations"></a> IsvConfig_AsyncOperations

See isvconfig Entity [IsvConfig_AsyncOperations](isvconfig.md#BKMK_IsvConfig_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Task_AsyncOperations"></a> Task_AsyncOperations

See task Entity [Task_AsyncOperations](task.md#BKMK_Task_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_BusinessUnitNewsArticle_AsyncOperations"></a> BusinessUnitNewsArticle_AsyncOperations

See businessunitnewsarticle Entity [BusinessUnitNewsArticle_AsyncOperations](businessunitnewsarticle.md#BKMK_BusinessUnitNewsArticle_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_AttributeMap_AsyncOperations"></a> AttributeMap_AsyncOperations

See attributemap Entity [AttributeMap_AsyncOperations](attributemap.md#BKMK_AttributeMap_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_Connection_AsyncOperations"></a> Connection_AsyncOperations

See connection Entity [Connection_AsyncOperations](connection.md#BKMK_Connection_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_SystemUser_AsyncOperations"></a> SystemUser_AsyncOperations

See systemuser Entity [SystemUser_AsyncOperations](systemuser.md#BKMK_SystemUser_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_KbArticleTemplate_AsyncOperations"></a> KbArticleTemplate_AsyncOperations

See kbarticletemplate Entity [KbArticleTemplate_AsyncOperations](kbarticletemplate.md#BKMK_KbArticleTemplate_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_SdkMessageProcessingStep_AsyncOperations"></a> SdkMessageProcessingStep_AsyncOperations

See sdkmessageprocessingstep Entity [SdkMessageProcessingStep_AsyncOperations](sdkmessageprocessingstep.md#BKMK_SdkMessageProcessingStep_AsyncOperations) One-To-Many relationship.

### <a name="BKMK_externalpartyitem_AsyncOperations"></a> externalpartyitem_AsyncOperations

See externalpartyitem Entity [externalpartyitem_AsyncOperations](externalpartyitem.md#BKMK_externalpartyitem_AsyncOperations) One-To-Many relationship.

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
asyncoperation

