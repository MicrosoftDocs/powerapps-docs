---
title: "Process Log (WorkflowLog) table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Process Log (WorkflowLog) table/entity."
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

# Process Log (WorkflowLog) table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Log used to track process execution.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/workflowlogs<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/workflowlogs(*workflowlogid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/workflowlogs(*workflowlogid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/workflowlogs<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/workflowlogs(*workflowlogid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|WorkflowLogs|
|DisplayCollectionName|Process Logs|
|DisplayName|Process Log|
|EntitySetName|workflowlogs|
|IsBPFEntity|False|
|LogicalCollectionName|workflowlogs|
|LogicalName|workflowlog|
|OwnershipType|None|
|PrimaryIdAttribute|workflowlogid|
|PrimaryNameAttribute||
|SchemaName|WorkflowLog|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ActivityName](#BKMK_ActivityName)
- [AsyncOperationId](#BKMK_AsyncOperationId)
- [ChildWorkflowInstanceId](#BKMK_ChildWorkflowInstanceId)
- [ChildWorkflowInstanceObjectTypeCode](#BKMK_ChildWorkflowInstanceObjectTypeCode)
- [CompletedOn](#BKMK_CompletedOn)
- [Description](#BKMK_Description)
- [ErrorCode](#BKMK_ErrorCode)
- [ErrorText](#BKMK_ErrorText)
- [InteractionActivityResult](#BKMK_InteractionActivityResult)
- [IterationCount](#BKMK_IterationCount)
- [Message](#BKMK_Message)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectIdYomiName](#BKMK_RegardingObjectIdYomiName)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [RepetitionCount](#BKMK_RepetitionCount)
- [RepetitionId](#BKMK_RepetitionId)
- [StageName](#BKMK_StageName)
- [StartedOn](#BKMK_StartedOn)
- [Status](#BKMK_Status)
- [StepName](#BKMK_StepName)
- [WorkflowLogId](#BKMK_WorkflowLogId)


### <a name="BKMK_ActivityName"></a> ActivityName

|Property|Value|
|--------|-----|
|Description|Name of the activity which the process step is currently processing.|
|DisplayName|Activity Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|activityname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_AsyncOperationId"></a> AsyncOperationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the parent record.|
|DisplayName|Parent record|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|asyncoperationid|
|RequiredLevel|SystemRequired|
|Targets|asyncoperation,processsession|
|Type|Lookup|


### <a name="BKMK_ChildWorkflowInstanceId"></a> ChildWorkflowInstanceId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the system job.|
|DisplayName|Child Workflow System Job|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|childworkflowinstanceid|
|RequiredLevel|None|
|Targets|asyncoperation,processsession|
|Type|Lookup|


### <a name="BKMK_ChildWorkflowInstanceObjectTypeCode"></a> ChildWorkflowInstanceObjectTypeCode

|Property|Value|
|--------|-----|
|Description|Object Type Code of the entity that is associated with the child workflow.|
|DisplayName|Entity|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|childworkflowinstanceobjecttypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_CompletedOn"></a> CompletedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the operation was completed.|
|DisplayName|Completed On|
|Format|DateAndTime|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|completedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Description of the process step.|
|DisplayName|Step Description|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_ErrorCode"></a> ErrorCode

|Property|Value|
|--------|-----|
|Description|Error code related to process.|
|DisplayName|Error Message|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|errorcode|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ErrorText"></a> ErrorText

**Added by**: Power Automate Extensions core package Solution

|Property|Value|
|--------|-----|
|Description|The string representation of the error.|
|DisplayName|ErrorText|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|errortext|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_InteractionActivityResult"></a> InteractionActivityResult

|Property|Value|
|--------|-----|
|Description|String specifying the result of an interaction activity.|
|DisplayName|Interaction Activity Result|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|interactionactivityresult|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_IterationCount"></a> IterationCount

**Added by**: Power Automate Extensions core package Solution

|Property|Value|
|--------|-----|
|Description|The iteration count for the action when in a do until loop.|
|DisplayName|IterationCount|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|iterationcount|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_Message"></a> Message

|Property|Value|
|--------|-----|
|Description|Message related to process.|
|DisplayName|Message|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|message|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|--------|-----|
|Description|Type of entity with which the process is associated.|
|DisplayName|Entity|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|objecttypecode|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the associated record.|
|DisplayName|Regarding|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|regardingobjectid|
|RequiredLevel|None|
|Targets||
|Type|Lookup|


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Regarding Object Id Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjectidname|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RegardingObjectIdYomiName"></a> RegardingObjectIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Regarding Object Id Yomi Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjectidyominame|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Regarding Object Type Code|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjecttypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_RepetitionCount"></a> RepetitionCount

**Added by**: Power Automate Extensions core package Solution

|Property|Value|
|--------|-----|
|Description|The count of repetitions of the action when in a loop.|
|DisplayName|RepetitionCount|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|repetitioncount|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_RepetitionId"></a> RepetitionId

**Added by**: Power Automate Extensions core package Solution

|Property|Value|
|--------|-----|
|Description|The string representation of the repetition and iteration / level of the action.|
|DisplayName|RepetitionId|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|repetitionid|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_StageName"></a> StageName

|Property|Value|
|--------|-----|
|Description|Name of the process stage.|
|DisplayName|Process Stage|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|stagename|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_StartedOn"></a> StartedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the operation was started.|
|DisplayName|Started On|
|Format|DateAndTime|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|startedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_Status"></a> Status

|Property|Value|
|--------|-----|
|Description|Status of the process step for which process log record has been created: In Progress, Successfully Completed, or Failed.|
|DisplayName|Status|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|status|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### Status Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|In Progress||
|2|Succeeded||
|3|Failed||
|4|Canceled||
|5|Waiting||



### <a name="BKMK_StepName"></a> StepName

|Property|Value|
|--------|-----|
|Description|Name of the process step.|
|DisplayName|Step Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|stepname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_WorkflowLogId"></a> WorkflowLogId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the process log entry.|
|DisplayName|Process Log|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|workflowlogid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AsyncOperationIdName](#BKMK_AsyncOperationIdName)
- [ChildWorkflowInstanceIdName](#BKMK_ChildWorkflowInstanceIdName)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [Duration](#BKMK_Duration)
- [Inputs_Name](#BKMK_Inputs_Name)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [Outputs_Name](#BKMK_Outputs_Name)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)


### <a name="BKMK_AsyncOperationIdName"></a> AsyncOperationIdName

|Property|Value|
|--------|-----|
|Description|Name of the parent record.|
|DisplayName|Parent record|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|asyncoperationidname|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ChildWorkflowInstanceIdName"></a> ChildWorkflowInstanceIdName

|Property|Value|
|--------|-----|
|Description|Name of the async operation.|
|DisplayName|Child Async Operation Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|childworkflowinstanceidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the process log entry.|
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
|DisplayName|Created By Name|
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
|DisplayName|Created By Yomi Name|
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
|Description|Date and time when the process log entry was created.|
|DisplayName|Started On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the process log.|
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
|DisplayName|Created By(Delegate) Name|
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
|DisplayName|Created By(Delegate) Yomi Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Duration"></a> Duration

|Property|Value|
|--------|-----|
|Description|Duration between completed on and started on, used by business process flow.|
|DisplayName|Duration|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|duration|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_Inputs_Name"></a> Inputs_Name

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|inputs_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the process log entry.|
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
|Description|Name of the user who last modified the operation.|
|DisplayName|Modified By Name|
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
|Description|YomiName of the user who last modified the operation.|
|DisplayName|Modified By Yomi Name|
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
|Description|Date and time when the process log entry was last modified.|
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
|Description|Unique identifier of the delegate user who last modified the process log.|
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
|DisplayName|Modified On Behalf By Name|
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
|DisplayName|Modified On Behalf By Yomi Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Outputs_Name"></a> Outputs_Name

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|outputs_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user or team who owns the process log.|
|DisplayName|Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|ApplicationRequired|
|Targets|systemuser,team|
|Type|Owner|


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Owner Id Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|--------|-----|
|Description|Unique identifier of the business unit that owns the process.|
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
|Description|Unique identifier of the team who owns the process log.|
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
|Description|Unique identifier of the user who owns the process.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [business_unit_workflowlogs](#BKMK_business_unit_workflowlogs)
- [lk_workflowlog_createdby](#BKMK_lk_workflowlog_createdby)
- [lk_workflowlog_processsession](#BKMK_lk_workflowlog_processsession)
- [lk_workflowlog_processsession_childworkflow](#BKMK_lk_workflowlog_processsession_childworkflow)
- [lk_workflowlog_asyncoperation_childworkflow](#BKMK_lk_workflowlog_asyncoperation_childworkflow)
- [lk_workflowlog_asyncoperations](#BKMK_lk_workflowlog_asyncoperations)
- [lk_workflowlog_modifiedby](#BKMK_lk_workflowlog_modifiedby)
- [lk_newprocess_workflowlogs](#BKMK_lk_newprocess_workflowlogs)
- [team_workflowlog](#BKMK_team_workflowlog)
- [lk_workflowlog_createdonbehalfby](#BKMK_lk_workflowlog_createdonbehalfby)
- [lk_translationprocess_workflowlogs](#BKMK_lk_translationprocess_workflowlogs)
- [lk_expiredprocess_workflowlogs](#BKMK_lk_expiredprocess_workflowlogs)
- [lk_workflowlog_modifiedonbehalfby](#BKMK_lk_workflowlog_modifiedonbehalfby)


### <a name="BKMK_business_unit_workflowlogs"></a> business_unit_workflowlogs

See businessunit Table [business_unit_workflowlogs](businessunit.md#BKMK_business_unit_workflowlogs) One-To-Many relationship.

### <a name="BKMK_lk_workflowlog_createdby"></a> lk_workflowlog_createdby

See systemuser Table [lk_workflowlog_createdby](systemuser.md#BKMK_lk_workflowlog_createdby) One-To-Many relationship.

### <a name="BKMK_lk_workflowlog_processsession"></a> lk_workflowlog_processsession

See processsession Table [lk_workflowlog_processsession](processsession.md#BKMK_lk_workflowlog_processsession) One-To-Many relationship.

### <a name="BKMK_lk_workflowlog_processsession_childworkflow"></a> lk_workflowlog_processsession_childworkflow

See processsession Table [lk_workflowlog_processsession_childworkflow](processsession.md#BKMK_lk_workflowlog_processsession_childworkflow) One-To-Many relationship.

### <a name="BKMK_lk_workflowlog_asyncoperation_childworkflow"></a> lk_workflowlog_asyncoperation_childworkflow

See asyncoperation Table [lk_workflowlog_asyncoperation_childworkflow](asyncoperation.md#BKMK_lk_workflowlog_asyncoperation_childworkflow) One-To-Many relationship.

### <a name="BKMK_lk_workflowlog_asyncoperations"></a> lk_workflowlog_asyncoperations

See asyncoperation Table [lk_workflowlog_asyncoperations](asyncoperation.md#BKMK_lk_workflowlog_asyncoperations) One-To-Many relationship.

### <a name="BKMK_lk_workflowlog_modifiedby"></a> lk_workflowlog_modifiedby

See systemuser Table [lk_workflowlog_modifiedby](systemuser.md#BKMK_lk_workflowlog_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_newprocess_workflowlogs"></a> lk_newprocess_workflowlogs

See newprocess Table [lk_newprocess_workflowlogs](newprocess.md#BKMK_lk_newprocess_workflowlogs) One-To-Many relationship.

### <a name="BKMK_team_workflowlog"></a> team_workflowlog

See team Table [team_workflowlog](team.md#BKMK_team_workflowlog) One-To-Many relationship.

### <a name="BKMK_lk_workflowlog_createdonbehalfby"></a> lk_workflowlog_createdonbehalfby

See systemuser Table [lk_workflowlog_createdonbehalfby](systemuser.md#BKMK_lk_workflowlog_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_translationprocess_workflowlogs"></a> lk_translationprocess_workflowlogs

See translationprocess Table [lk_translationprocess_workflowlogs](translationprocess.md#BKMK_lk_translationprocess_workflowlogs) One-To-Many relationship.

### <a name="BKMK_lk_expiredprocess_workflowlogs"></a> lk_expiredprocess_workflowlogs

See expiredprocess Table [lk_expiredprocess_workflowlogs](expiredprocess.md#BKMK_lk_expiredprocess_workflowlogs) One-To-Many relationship.

### <a name="BKMK_lk_workflowlog_modifiedonbehalfby"></a> lk_workflowlog_modifiedonbehalfby

See systemuser Table [lk_workflowlog_modifiedonbehalfby](systemuser.md#BKMK_lk_workflowlog_modifiedonbehalfby) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.workflowlog?text=workflowlog EntityType" />