---
title: "Process Log (WorkflowLog) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Process Log (WorkflowLog) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Process Log (WorkflowLog) table/entity reference (Microsoft Dataverse)

Log used to track process execution.

## Messages

The following table lists the messages for the Process Log (WorkflowLog) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /workflowlogs<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /workflowlogs(*workflowlogid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /workflowlogs(*workflowlogid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /workflowlogs<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /workflowlogs(*workflowlogid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /workflowlogs(*workflowlogid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Process Log (WorkflowLog) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Process Log** |
| **DisplayCollectionName** | **Process Logs** |
| **SchemaName** | `WorkflowLog` |
| **CollectionSchemaName** | `WorkflowLogs` |
| **EntitySetName** | `workflowlogs`|
| **LogicalName** | `workflowlog` |
| **LogicalCollectionName** | `workflowlogs` |
| **PrimaryIdAttribute** | `workflowlogid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

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
|---|---|
|Description|**Name of the activity which the process step is currently processing.**|
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
|MaxLength|160|

### <a name="BKMK_AsyncOperationId"></a> AsyncOperationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the parent record.**|
|DisplayName|**Parent record**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`asyncoperationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|asyncoperation, processsession|

### <a name="BKMK_ChildWorkflowInstanceId"></a> ChildWorkflowInstanceId

|Property|Value|
|---|---|
|Description|**Unique identifier of the system job.**|
|DisplayName|**Child Workflow System Job**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`childworkflowinstanceid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|asyncoperation, processsession|

### <a name="BKMK_ChildWorkflowInstanceObjectTypeCode"></a> ChildWorkflowInstanceObjectTypeCode

|Property|Value|
|---|---|
|Description|**Object Type Code of the entity that is associated with the child workflow.**|
|DisplayName|**Entity**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`childworkflowinstanceobjecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_CompletedOn"></a> CompletedOn

|Property|Value|
|---|---|
|Description|**Date and time when the operation was completed.**|
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

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the process step.**|
|DisplayName|**Step Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_ErrorCode"></a> ErrorCode

|Property|Value|
|---|---|
|Description|**Error code related to process.**|
|DisplayName|**Error Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`errorcode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_ErrorText"></a> ErrorText

|Property|Value|
|---|---|
|Description|**The string representation of the error.**|
|DisplayName|**ErrorText**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`errortext`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_InteractionActivityResult"></a> InteractionActivityResult

|Property|Value|
|---|---|
|Description|**String specifying the result of an interaction activity.**|
|DisplayName|**Interaction Activity Result**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`interactionactivityresult`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_IterationCount"></a> IterationCount

|Property|Value|
|---|---|
|Description|**The iteration count for the action when in a do until loop.**|
|DisplayName|**IterationCount**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`iterationcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_Message"></a> Message

|Property|Value|
|---|---|
|Description|**Message related to process.**|
|DisplayName|**Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`message`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|---|---|
|Description|**Type of entity with which the process is associated.**|
|DisplayName|**Entity**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objecttypecode`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**Unique identifier of the associated record.**|
|DisplayName|**Regarding**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`regardingobjectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets||

### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|---|---|
|Description||
|DisplayName|**Regarding Object Type Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_RepetitionCount"></a> RepetitionCount

|Property|Value|
|---|---|
|Description|**The count of repetitions of the action when in a loop.**|
|DisplayName|**RepetitionCount**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`repetitioncount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_RepetitionId"></a> RepetitionId

|Property|Value|
|---|---|
|Description|**The string representation of the repetition and iteration / level of the action.**|
|DisplayName|**RepetitionId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`repetitionid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_StageName"></a> StageName

|Property|Value|
|---|---|
|Description|**Name of the process stage.**|
|DisplayName|**Process Stage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`stagename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_StartedOn"></a> StartedOn

|Property|Value|
|---|---|
|Description|**Date and time when the operation was started.**|
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

### <a name="BKMK_Status"></a> Status

|Property|Value|
|---|---|
|Description|**Status of the process step for which process log record has been created: In Progress, Successfully Completed, or Failed.**|
|DisplayName|**Status**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`status`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`workflowlog_status`|

#### Status Choices/Options

|Value|Label|
|---|---|
|1|**In Progress**|
|2|**Succeeded**|
|3|**Failed**|
|4|**Canceled**|
|5|**Waiting**|

### <a name="BKMK_StepName"></a> StepName

|Property|Value|
|---|---|
|Description|**Name of the process step.**|
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
|MaxLength|160|

### <a name="BKMK_WorkflowLogId"></a> WorkflowLogId

|Property|Value|
|---|---|
|Description|**Unique identifier of the process log entry.**|
|DisplayName|**Process Log**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`workflowlogid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [Duration](#BKMK_Duration)
- [Inputs](#BKMK_Inputs)
- [Inputs_Name](#BKMK_Inputs_Name)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [Outputs](#BKMK_Outputs)
- [Outputs_Name](#BKMK_Outputs_Name)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the process log entry.**|
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
|Description|**Date and time when the process log entry was created.**|
|DisplayName|**Started On**|
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
|Description|**Unique identifier of the delegate user who created the process log.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_Duration"></a> Duration

|Property|Value|
|---|---|
|Description|**Duration between completed on and started on, used by business process flow.**|
|DisplayName|**Duration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`duration`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_Inputs"></a> Inputs

|Property|Value|
|---|---|
|Description|**Inputs required by the workflow step.**|
|DisplayName|**Inputs**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`inputs`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_Inputs_Name"></a> Inputs_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`inputs_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the process log entry.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the process log entry was last modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the process log.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_Outputs"></a> Outputs

|Property|Value|
|---|---|
|Description|**Outputs generated by the workflow step.**|
|DisplayName|**Outputs**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`outputs`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_Outputs_Name"></a> Outputs_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`outputs_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user or team who owns the process log.**|
|DisplayName|**Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|ApplicationRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description||
|DisplayName|**Owner Id Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Unique identifier of the business unit that owns the process.**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|---|---|
|Description|**Unique identifier of the team who owns the process log.**|
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
|Description|**Unique identifier of the user who owns the process.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [business_unit_workflowlogs](#BKMK_business_unit_workflowlogs)
- [FileAttachment_WorkflowLog_Inputs](#BKMK_FileAttachment_WorkflowLog_Inputs)
- [FileAttachment_WorkflowLog_Outputs](#BKMK_FileAttachment_WorkflowLog_Outputs)
- [lk_expiredprocess_workflowlogs](#BKMK_lk_expiredprocess_workflowlogs)
- [lk_newprocess_workflowlogs](#BKMK_lk_newprocess_workflowlogs)
- [lk_translationprocess_workflowlogs](#BKMK_lk_translationprocess_workflowlogs)
- [lk_workflowlog_asyncoperation_childworkflow](#BKMK_lk_workflowlog_asyncoperation_childworkflow)
- [lk_workflowlog_asyncoperations](#BKMK_lk_workflowlog_asyncoperations)
- [lk_workflowlog_createdby](#BKMK_lk_workflowlog_createdby)
- [lk_workflowlog_createdonbehalfby](#BKMK_lk_workflowlog_createdonbehalfby)
- [lk_workflowlog_modifiedby](#BKMK_lk_workflowlog_modifiedby)
- [lk_workflowlog_modifiedonbehalfby](#BKMK_lk_workflowlog_modifiedonbehalfby)
- [lk_workflowlog_processsession](#BKMK_lk_workflowlog_processsession)
- [lk_workflowlog_processsession_childworkflow](#BKMK_lk_workflowlog_processsession_childworkflow)
- [team_workflowlog](#BKMK_team_workflowlog)

### <a name="BKMK_business_unit_workflowlogs"></a> business_unit_workflowlogs

One-To-Many Relationship: [businessunit business_unit_workflowlogs](businessunit.md#BKMK_business_unit_workflowlogs)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_WorkflowLog_Inputs"></a> FileAttachment_WorkflowLog_Inputs

One-To-Many Relationship: [fileattachment FileAttachment_WorkflowLog_Inputs](fileattachment.md#BKMK_FileAttachment_WorkflowLog_Inputs)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`inputs`|
|ReferencingEntityNavigationPropertyName|`inputs`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_WorkflowLog_Outputs"></a> FileAttachment_WorkflowLog_Outputs

One-To-Many Relationship: [fileattachment FileAttachment_WorkflowLog_Outputs](fileattachment.md#BKMK_FileAttachment_WorkflowLog_Outputs)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`outputs`|
|ReferencingEntityNavigationPropertyName|`outputs`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_expiredprocess_workflowlogs"></a> lk_expiredprocess_workflowlogs

One-To-Many Relationship: [expiredprocess lk_expiredprocess_workflowlogs](expiredprocess.md#BKMK_lk_expiredprocess_workflowlogs)

|Property|Value|
|---|---|
|ReferencedEntity|`expiredprocess`|
|ReferencedAttribute|`businessprocessflowinstanceid`|
|ReferencingAttribute|`asyncoperationid`|
|ReferencingEntityNavigationPropertyName|`ExpiredProcess_asyncoperationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_lk_newprocess_workflowlogs"></a> lk_newprocess_workflowlogs

One-To-Many Relationship: [newprocess lk_newprocess_workflowlogs](newprocess.md#BKMK_lk_newprocess_workflowlogs)

|Property|Value|
|---|---|
|ReferencedEntity|`newprocess`|
|ReferencedAttribute|`businessprocessflowinstanceid`|
|ReferencingAttribute|`asyncoperationid`|
|ReferencingEntityNavigationPropertyName|`NewProcess_asyncoperationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_lk_translationprocess_workflowlogs"></a> lk_translationprocess_workflowlogs

One-To-Many Relationship: [translationprocess lk_translationprocess_workflowlogs](translationprocess.md#BKMK_lk_translationprocess_workflowlogs)

|Property|Value|
|---|---|
|ReferencedEntity|`translationprocess`|
|ReferencedAttribute|`businessprocessflowinstanceid`|
|ReferencingAttribute|`asyncoperationid`|
|ReferencingEntityNavigationPropertyName|`TranslationProcess_asyncoperationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_lk_workflowlog_asyncoperation_childworkflow"></a> lk_workflowlog_asyncoperation_childworkflow

One-To-Many Relationship: [asyncoperation lk_workflowlog_asyncoperation_childworkflow](asyncoperation.md#BKMK_lk_workflowlog_asyncoperation_childworkflow)

|Property|Value|
|---|---|
|ReferencedEntity|`asyncoperation`|
|ReferencedAttribute|`asyncoperationid`|
|ReferencingAttribute|`childworkflowinstanceid`|
|ReferencingEntityNavigationPropertyName|`childworkflowinstanceid_asyncoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_workflowlog_asyncoperations"></a> lk_workflowlog_asyncoperations

One-To-Many Relationship: [asyncoperation lk_workflowlog_asyncoperations](asyncoperation.md#BKMK_lk_workflowlog_asyncoperations)

|Property|Value|
|---|---|
|ReferencedEntity|`asyncoperation`|
|ReferencedAttribute|`asyncoperationid`|
|ReferencingAttribute|`asyncoperationid`|
|ReferencingEntityNavigationPropertyName|`asyncoperationid_asyncoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_lk_workflowlog_createdby"></a> lk_workflowlog_createdby

One-To-Many Relationship: [systemuser lk_workflowlog_createdby](systemuser.md#BKMK_lk_workflowlog_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_workflowlog_createdonbehalfby"></a> lk_workflowlog_createdonbehalfby

One-To-Many Relationship: [systemuser lk_workflowlog_createdonbehalfby](systemuser.md#BKMK_lk_workflowlog_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_workflowlog_modifiedby"></a> lk_workflowlog_modifiedby

One-To-Many Relationship: [systemuser lk_workflowlog_modifiedby](systemuser.md#BKMK_lk_workflowlog_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_workflowlog_modifiedonbehalfby"></a> lk_workflowlog_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_workflowlog_modifiedonbehalfby](systemuser.md#BKMK_lk_workflowlog_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_workflowlog_processsession"></a> lk_workflowlog_processsession

One-To-Many Relationship: [processsession lk_workflowlog_processsession](processsession.md#BKMK_lk_workflowlog_processsession)

|Property|Value|
|---|---|
|ReferencedEntity|`processsession`|
|ReferencedAttribute|`processsessionid`|
|ReferencingAttribute|`asyncoperationid`|
|ReferencingEntityNavigationPropertyName|`asyncoperationid_processsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_lk_workflowlog_processsession_childworkflow"></a> lk_workflowlog_processsession_childworkflow

One-To-Many Relationship: [processsession lk_workflowlog_processsession_childworkflow](processsession.md#BKMK_lk_workflowlog_processsession_childworkflow)

|Property|Value|
|---|---|
|ReferencedEntity|`processsession`|
|ReferencedAttribute|`processsessionid`|
|ReferencingAttribute|`childworkflowinstanceid`|
|ReferencingEntityNavigationPropertyName|`childworkflowinstanceid_processsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_workflowlog"></a> team_workflowlog

One-To-Many Relationship: [team team_workflowlog](team.md#BKMK_team_workflowlog)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_workflowlog_FileAttachments"></a> workflowlog_FileAttachments

Many-To-One Relationship: [fileattachment workflowlog_FileAttachments](fileattachment.md#BKMK_workflowlog_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`workflowlog_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.workflowlog?displayProperty=fullName>
