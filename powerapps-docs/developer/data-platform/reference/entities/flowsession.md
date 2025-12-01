---
title: "Flow Session (flowsession) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Flow Session (flowsession) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Flow Session (flowsession) table/entity reference (Microsoft Dataverse)

Entity to store the information that is generated when a Power Automate Desktop flow runs.

## Messages

The following table lists the messages for the Flow Session (flowsession) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /flowsessions(*flowsessionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `CancelDesktopFlowRun`<br />Event: False |<xref:Microsoft.Dynamics.CRM.CancelDesktopFlowRun?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Create`<br />Event: True |`POST` /flowsessions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /flowsessions(*flowsessionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /flowsessions(*flowsessionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /flowsessions<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /flowsessions(*flowsessionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `TriggerDesktopFlowRunCallback`<br />Event: False |<xref:Microsoft.Dynamics.CRM.TriggerDesktopFlowRunCallback?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Update`<br />Event: True |`PATCH` /flowsessions(*flowsessionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /flowsessions(*flowsessionid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Flow Session (flowsession) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Flow Session** |
| **DisplayCollectionName** | **Flow Sessions** |
| **SchemaName** | `flowsession` |
| **CollectionSchemaName** | `flowsessions` |
| **EntitySetName** | `flowsessions`|
| **LogicalName** | `flowsession` |
| **LogicalCollectionName** | `flowsessions` |
| **PrimaryIdAttribute** | `flowsessionid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CallbackUrl](#BKMK_CallbackUrl)
- [ClientTrackingId](#BKMK_ClientTrackingId)
- [CompletedOn](#BKMK_CompletedOn)
- [ConnectionId](#BKMK_ConnectionId)
- [Context](#BKMK_Context)
- [CorrelationId](#BKMK_CorrelationId)
- [Credentials](#BKMK_Credentials)
- [ErrorCode](#BKMK_ErrorCode)
- [ErrorDetails](#BKMK_ErrorDetails)
- [ErrorInnerError](#BKMK_ErrorInnerError)
- [ErrorMessage](#BKMK_ErrorMessage)
- [flowsessionId](#BKMK_flowsessionId)
- [Gateway](#BKMK_Gateway)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [MachineGroupId](#BKMK_MachineGroupId)
- [MachineId](#BKMK_MachineId)
- [MachinePercentCpuUsage](#BKMK_MachinePercentCpuUsage)
- [MachinePercentRamUsage](#BKMK_MachinePercentRamUsage)
- [MachineRamUsage](#BKMK_MachineRamUsage)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [ParentCloudFlowRunSequenceId](#BKMK_ParentCloudFlowRunSequenceId)
- [ParentDesktopFlowRunId](#BKMK_ParentDesktopFlowRunId)
- [ParentWorkflowId](#BKMK_ParentWorkflowId)
- [ProcessVersion](#BKMK_ProcessVersion)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [RunDetails](#BKMK_RunDetails)
- [RunDuration](#BKMK_RunDuration)
- [RunExecutionDuration](#BKMK_RunExecutionDuration)
- [RunMode](#BKMK_RunMode)
- [RunSessionMode](#BKMK_RunSessionMode)
- [RunWaitDuration](#BKMK_RunWaitDuration)
- [SessionUsername](#BKMK_SessionUsername)
- [SessionUserSID](#BKMK_SessionUserSID)
- [StartedOn](#BKMK_StartedOn)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [SubCategory](#BKMK_SubCategory)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [TriggerType](#BKMK_TriggerType)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_CallbackUrl"></a> CallbackUrl

|Property|Value|
|---|---|
|Description|**URL that will be called once the flow session is complete.**|
|DisplayName|**Callback URL**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`callbackurl`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_ClientTrackingId"></a> ClientTrackingId

|Property|Value|
|---|---|
|Description|**The client tracking id of the run**|
|DisplayName|**Client Tracking Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`clienttrackingid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|255|

### <a name="BKMK_CompletedOn"></a> CompletedOn

|Property|Value|
|---|---|
|Description|**The date and time at which the flow session was completed.**|
|DisplayName|**Completed On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`completedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_ConnectionId"></a> ConnectionId

|Property|Value|
|---|---|
|Description|**The id of the connection used in the Desktop Flow run.**|
|DisplayName|**Connection Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`connectionid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Context"></a> Context

|Property|Value|
|---|---|
|Description|**Context about flow session.**|
|DisplayName|**Context**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`context`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_CorrelationId"></a> CorrelationId

|Property|Value|
|---|---|
|Description|**Unique identifier used to correlate between multiple SDK requests and flow executions.**|
|DisplayName|**CorrelationId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`correlationid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Credentials"></a> Credentials

|Property|Value|
|---|---|
|Description|**Credentials related to this run.**|
|DisplayName|**Credentials**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`credentials`|
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
|Description|**Error code describing the failure in flow session execution.**|
|DisplayName|**ErrorCode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`errorcode`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_ErrorDetails"></a> ErrorDetails

|Property|Value|
|---|---|
|Description|**Details of the failure in flow session execution.**|
|DisplayName|**ErrorDetails**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`errordetails`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_ErrorInnerError"></a> ErrorInnerError

|Property|Value|
|---|---|
|Description|**Specific information about the failure in flow session execution.**|
|DisplayName|**ErrorInnerError**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`errorinnererror`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_ErrorMessage"></a> ErrorMessage

|Property|Value|
|---|---|
|Description|**Message describing the failure in flow session execution.**|
|DisplayName|**ErrorMessage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`errormessage`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_flowsessionId"></a> flowsessionId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**FlowSession**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`flowsessionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Gateway"></a> Gateway

|Property|Value|
|---|---|
|Description|**The name of the gateway used.**|
|DisplayName|**Gateway**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`gateway`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Sequence number of the import that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_MachineGroupId"></a> MachineGroupId

|Property|Value|
|---|---|
|Description||
|DisplayName|**Flow Machine Group**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`machinegroupid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|flowmachinegroup|

### <a name="BKMK_MachineId"></a> MachineId

|Property|Value|
|---|---|
|Description||
|DisplayName|**Flow Machine**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`machineid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|flowmachine|

### <a name="BKMK_MachinePercentCpuUsage"></a> MachinePercentCpuUsage

|Property|Value|
|---|---|
|Description|**The percentage of CPU utilization by the machine**|
|DisplayName|**Machine CPU usage percentage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`machinepercentcpuusage`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Auto|
|MaxValue|100|
|MinValue|0|
|Precision|2|

### <a name="BKMK_MachinePercentRamUsage"></a> MachinePercentRamUsage

|Property|Value|
|---|---|
|Description|**The percentage of RAM utilization by the machine**|
|DisplayName|**Machine RAM usage percentage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`machinepercentramusage`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Auto|
|MaxValue|100|
|MinValue|0|
|Precision|2|

### <a name="BKMK_MachineRamUsage"></a> MachineRamUsage

|Property|Value|
|---|---|
|Description|**The machine RAM usage in Mo**|
|DisplayName|**Machine RAM usage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`machineramusage`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|---|---|
|Description|**Date and time that the record was migrated.**|
|DisplayName|**Record Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overriddencreatedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Owner Id**|
|DisplayName|**Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description|**Owner Id Type**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_ParentCloudFlowRunSequenceId"></a> ParentCloudFlowRunSequenceId

|Property|Value|
|---|---|
|Description|**The sequence id of the parent cloud flow run, only used when the Desktop Flow was run by a cloud flow.**|
|DisplayName|**Parent Cloud Flow Run Sequence Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentcloudflowrunsequenceid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_ParentDesktopFlowRunId"></a> ParentDesktopFlowRunId

|Property|Value|
|---|---|
|Description|**The run id of the parent desktop flow run, only used when the Desktop Flow was run by a desktop flow.**|
|DisplayName|**Parent Desktop Flow Run Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentdesktopflowrunid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|flowsession|

### <a name="BKMK_ParentWorkflowId"></a> ParentWorkflowId

|Property|Value|
|---|---|
|Description|**Id of the parent workflow, cloud flow or desktop flow.**|
|DisplayName|**ParentWorkflowId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentworkflowid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ProcessVersion"></a> ProcessVersion

|Property|Value|
|---|---|
|Description|**The version of the process with which the flow session is associated.**|
|DisplayName|**Process Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`processversion`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**Unique identifier of the process with which the flow session is associated.**|
|DisplayName|**Regarding**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`regardingobjectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|workflow|

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

### <a name="BKMK_RunDetails"></a> RunDetails

|Property|Value|
|---|---|
|Description|**Details about the run.**|
|DisplayName|**RunDetails**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`rundetails`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_RunDuration"></a> RunDuration

|Property|Value|
|---|---|
|Description|**Duration of the run.**|
|DisplayName|**RunDuration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`runduration`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_RunExecutionDuration"></a> RunExecutionDuration

|Property|Value|
|---|---|
|Description|**Duration of the run execution.**|
|DisplayName|**RunExecutionDuration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`runexecutionduration`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_RunMode"></a> RunMode

|Property|Value|
|---|---|
|Description|**Indicates the run mode of the desktop flow run.**|
|DisplayName|**Run mode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`runmode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`flowsession_runmode`|

#### RunMode Choices/Options

|Value|Label|
|---|---|
|0|**Local**|
|1|**Attended**|
|2|**Unattended**|

### <a name="BKMK_RunSessionMode"></a> RunSessionMode

|Property|Value|
|---|---|
|Description|**Indicates the run session mode of the desktop flow run.**|
|DisplayName|**Run session mode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`runsessionmode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`flowsession_runsessionmode`|

#### RunSessionMode Choices/Options

|Value|Label|
|---|---|
|0|**Unapplicable**|
|1|**Default**|
|2|**PictureInPicture**|

### <a name="BKMK_RunWaitDuration"></a> RunWaitDuration

|Property|Value|
|---|---|
|Description|**Time the run spent waiting.**|
|DisplayName|**RunWaitDuration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`runwaitduration`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_SessionUsername"></a> SessionUsername

|Property|Value|
|---|---|
|Description|**The username used in the Desktop Flow run.**|
|DisplayName|**Session Username**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sessionusername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_SessionUserSID"></a> SessionUserSID

|Property|Value|
|---|---|
|Description|**The SID of the user used in the Desktop Flow run.**|
|DisplayName|**Session User SID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sessionusersid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_StartedOn"></a> StartedOn

|Property|Value|
|---|---|
|Description|**The date and time at which the flow session was started.**|
|DisplayName|**Started On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`startedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the FlowSession**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`flowsession_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the FlowSession**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`flowsession_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|0|Label: **NotSpecified**<br />State:1<br />TransitionData: None|
|1|Label: **Paused**<br />State:0<br />TransitionData: None|
|2|Label: **Running**<br />State:0<br />TransitionData: None|
|3|Label: **Waiting**<br />State:0<br />TransitionData: None|
|4|Label: **Succeeded**<br />State:0<br />TransitionData: None|
|5|Label: **Skipped**<br />State:0<br />TransitionData: None|
|6|Label: **Suspended**<br />State:0<br />TransitionData: None|
|7|Label: **Cancelled**<br />State:0<br />TransitionData: None|
|8|Label: **Failed**<br />State:0<br />TransitionData: None|
|9|Label: **Faulted**<br />State:0<br />TransitionData: None|
|10|Label: **TimedOut**<br />State:0<br />TransitionData: None|
|11|Label: **Aborted**<br />State:0<br />TransitionData: None|
|12|Label: **Ignored**<br />State:0<br />TransitionData: None|
|13|Label: **Deleted**<br />State:1<br />TransitionData: None|
|14|Label: **Terminated**<br />State:1<br />TransitionData: None|

### <a name="BKMK_SubCategory"></a> SubCategory

|Property|Value|
|---|---|
|Description|**Sub-Category of the flow session.**|
|DisplayName|**Sub-Category**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`subcategory`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`flowsession_subcategory`|

#### SubCategory Choices/Options

|Value|Label|
|---|---|
|0|**Default**|
|1|**Test**|

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Time Zone Rule Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezoneruleversionnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_TriggerType"></a> TriggerType

|Property|Value|
|---|---|
|Description|**Indicates the type of trigger used to run the desktop flow.**|
|DisplayName|**Trigger type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`triggertype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`flowsession_triggertype`|

#### TriggerType Choices/Options

|Value|Label|
|---|---|
|0|**ApiFlow**|
|1|**DesktopFlow**|
|2|**Local**|
|3|**RunDesktopFlowDataverseApi**|
|4|**Cua**|

### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|---|---|
|Description|**Time zone code that was in use when the record was created.**|
|DisplayName|**UTC Conversion Time Zone Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`utcconversiontimezonecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [AdditionalContext](#BKMK_AdditionalContext)
- [AdditionalContext_Name](#BKMK_AdditionalContext_Name)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [Inputs](#BKMK_Inputs)
- [Inputs_Name](#BKMK_Inputs_Name)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [Outputs](#BKMK_Outputs)
- [Outputs_Name](#BKMK_Outputs_Name)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_AdditionalContext"></a> AdditionalContext

|Property|Value|
|---|---|
|Description|**Additional context about flow session.**|
|DisplayName|**AdditionalContext**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`additionalcontext`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_AdditionalContext_Name"></a> AdditionalContext_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`additionalcontext_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the record.**|
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
|Description|**Date and time when the record was created.**|
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
|Description|**Unique identifier of the delegate user who created the record.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_Inputs"></a> Inputs

|Property|Value|
|---|---|
|Description|**Inputs provided for the flow session execution.**|
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
|Description|**Unique identifier of the user who modified the record.**|
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
|Description|**Date and time when the record was modified.**|
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
|Description|**Unique identifier of the delegate user who modified the record.**|
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
|Description|**Outputs generated by the flow session execution.**|
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

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description|**Name of the owner**|
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
|Description|**Yomi name of the owner**|
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
|Description|**Unique identifier for the business unit that owns the record**|
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
|Description|**Unique identifier for the team that owns the record.**|
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
|Description|**Unique identifier for the user that owns the record.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version Number**|
|DisplayName|**Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [business_unit_flowsession](#BKMK_business_unit_flowsession)
- [FileAttachment_FlowSession_AdditionalContext](#BKMK_FileAttachment_FlowSession_AdditionalContext)
- [FileAttachment_FlowSession_Inputs](#BKMK_FileAttachment_FlowSession_Inputs)
- [FileAttachment_FlowSession_Outputs](#BKMK_FileAttachment_FlowSession_Outputs)
- [flowmachine_flowsession_MachineId](#BKMK_flowmachine_flowsession_MachineId)
- [flowmachinegroup_flowsession_MachineGroupId](#BKMK_flowmachinegroup_flowsession_MachineGroupId)
- [flowsession_flowsession_parentdesktopflowrunid](#BKMK_flowsession_flowsession_parentdesktopflowrunid-many-to-one)
- [lk_flowsession_createdby](#BKMK_lk_flowsession_createdby)
- [lk_flowsession_createdonbehalfby](#BKMK_lk_flowsession_createdonbehalfby)
- [lk_flowsession_modifiedby](#BKMK_lk_flowsession_modifiedby)
- [lk_flowsession_modifiedonbehalfby](#BKMK_lk_flowsession_modifiedonbehalfby)
- [owner_flowsession](#BKMK_owner_flowsession)
- [regardingobjectid_process](#BKMK_regardingobjectid_process)
- [team_flowsession](#BKMK_team_flowsession)
- [user_flowsession](#BKMK_user_flowsession)

### <a name="BKMK_business_unit_flowsession"></a> business_unit_flowsession

One-To-Many Relationship: [businessunit business_unit_flowsession](businessunit.md#BKMK_business_unit_flowsession)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_FlowSession_AdditionalContext"></a> FileAttachment_FlowSession_AdditionalContext

One-To-Many Relationship: [fileattachment FileAttachment_FlowSession_AdditionalContext](fileattachment.md#BKMK_FileAttachment_FlowSession_AdditionalContext)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`additionalcontext`|
|ReferencingEntityNavigationPropertyName|`additionalcontext`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_FlowSession_Inputs"></a> FileAttachment_FlowSession_Inputs

One-To-Many Relationship: [fileattachment FileAttachment_FlowSession_Inputs](fileattachment.md#BKMK_FileAttachment_FlowSession_Inputs)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`inputs`|
|ReferencingEntityNavigationPropertyName|`inputs`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_FlowSession_Outputs"></a> FileAttachment_FlowSession_Outputs

One-To-Many Relationship: [fileattachment FileAttachment_FlowSession_Outputs](fileattachment.md#BKMK_FileAttachment_FlowSession_Outputs)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`outputs`|
|ReferencingEntityNavigationPropertyName|`outputs`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachine_flowsession_MachineId"></a> flowmachine_flowsession_MachineId

One-To-Many Relationship: [flowmachine flowmachine_flowsession_MachineId](flowmachine.md#BKMK_flowmachine_flowsession_MachineId)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachine`|
|ReferencedAttribute|`flowmachineid`|
|ReferencingAttribute|`machineid`|
|ReferencingEntityNavigationPropertyName|`MachineId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinegroup_flowsession_MachineGroupId"></a> flowmachinegroup_flowsession_MachineGroupId

One-To-Many Relationship: [flowmachinegroup flowmachinegroup_flowsession_MachineGroupId](flowmachinegroup.md#BKMK_flowmachinegroup_flowsession_MachineGroupId)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinegroup`|
|ReferencedAttribute|`flowmachinegroupid`|
|ReferencingAttribute|`machinegroupid`|
|ReferencingEntityNavigationPropertyName|`MachineGroupId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowsession_flowsession_parentdesktopflowrunid-many-to-one"></a> flowsession_flowsession_parentdesktopflowrunid

One-To-Many Relationship: [flowsession flowsession_flowsession_parentdesktopflowrunid](#BKMK_flowsession_flowsession_parentdesktopflowrunid-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`flowsession`|
|ReferencedAttribute|`flowsessionid`|
|ReferencingAttribute|`parentdesktopflowrunid`|
|ReferencingEntityNavigationPropertyName|`parentdesktopflowrunid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowsession_createdby"></a> lk_flowsession_createdby

One-To-Many Relationship: [systemuser lk_flowsession_createdby](systemuser.md#BKMK_lk_flowsession_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowsession_createdonbehalfby"></a> lk_flowsession_createdonbehalfby

One-To-Many Relationship: [systemuser lk_flowsession_createdonbehalfby](systemuser.md#BKMK_lk_flowsession_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowsession_modifiedby"></a> lk_flowsession_modifiedby

One-To-Many Relationship: [systemuser lk_flowsession_modifiedby](systemuser.md#BKMK_lk_flowsession_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowsession_modifiedonbehalfby"></a> lk_flowsession_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_flowsession_modifiedonbehalfby](systemuser.md#BKMK_lk_flowsession_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_flowsession"></a> owner_flowsession

One-To-Many Relationship: [owner owner_flowsession](owner.md#BKMK_owner_flowsession)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_regardingobjectid_process"></a> regardingobjectid_process

One-To-Many Relationship: [workflow regardingobjectid_process](workflow.md#BKMK_regardingobjectid_process)

|Property|Value|
|---|---|
|ReferencedEntity|`workflow`|
|ReferencedAttribute|`workflowid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_process`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_flowsession"></a> team_flowsession

One-To-Many Relationship: [team team_flowsession](team.md#BKMK_team_flowsession)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_flowsession"></a> user_flowsession

One-To-Many Relationship: [systemuser user_flowsession](systemuser.md#BKMK_user_flowsession)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [flowevent_flowsession](#BKMK_flowevent_flowsession)
- [flowsession_AsyncOperations](#BKMK_flowsession_AsyncOperations)
- [flowsession_BulkDeleteFailures](#BKMK_flowsession_BulkDeleteFailures)
- [flowsession_FileAttachments](#BKMK_flowsession_FileAttachments)
- [flowsession_flowlog_flowsessionid](#BKMK_flowsession_flowlog_flowsessionid)
- [flowsession_flowlog_parentobjectid](#BKMK_flowsession_flowlog_parentobjectid)
- [flowsession_flowsession_parentdesktopflowrunid](#BKMK_flowsession_flowsession_parentdesktopflowrunid-one-to-many)
- [flowsession_flowsessionbinary_FlowSessionId](#BKMK_flowsession_flowsessionbinary_FlowSessionId)
- [flowsession_MailboxTrackingFolders](#BKMK_flowsession_MailboxTrackingFolders)
- [flowsession_PrincipalObjectAttributeAccesses](#BKMK_flowsession_PrincipalObjectAttributeAccesses)
- [flowsession_SyncErrors](#BKMK_flowsession_SyncErrors)
- [flowsession_workflowbinary_FlowSessionId](#BKMK_flowsession_workflowbinary_FlowSessionId)
- [taggedflowsession_FlowSession_flowsession](#BKMK_taggedflowsession_FlowSession_flowsession)

### <a name="BKMK_flowevent_flowsession"></a> flowevent_flowsession

Many-To-One Relationship: [flowevent flowevent_flowsession](flowevent.md#BKMK_flowevent_flowsession)

|Property|Value|
|---|---|
|ReferencingEntity|`flowevent`|
|ReferencingAttribute|`parentobjectid`|
|ReferencedEntityNavigationPropertyName|`flowevent_flowsession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowsession_AsyncOperations"></a> flowsession_AsyncOperations

Many-To-One Relationship: [asyncoperation flowsession_AsyncOperations](asyncoperation.md#BKMK_flowsession_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowsession_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowsession_BulkDeleteFailures"></a> flowsession_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure flowsession_BulkDeleteFailures](bulkdeletefailure.md#BKMK_flowsession_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowsession_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowsession_FileAttachments"></a> flowsession_FileAttachments

Many-To-One Relationship: [fileattachment flowsession_FileAttachments](fileattachment.md#BKMK_flowsession_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`flowsession_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowsession_flowlog_flowsessionid"></a> flowsession_flowlog_flowsessionid

Many-To-One Relationship: [flowlog flowsession_flowlog_flowsessionid](flowlog.md#BKMK_flowsession_flowlog_flowsessionid)

|Property|Value|
|---|---|
|ReferencingEntity|`flowlog`|
|ReferencingAttribute|`flowsessionid`|
|ReferencedEntityNavigationPropertyName|`flowsession_flowlog_flowsessionid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowsession_flowlog_parentobjectid"></a> flowsession_flowlog_parentobjectid

Many-To-One Relationship: [flowlog flowsession_flowlog_parentobjectid](flowlog.md#BKMK_flowsession_flowlog_parentobjectid)

|Property|Value|
|---|---|
|ReferencingEntity|`flowlog`|
|ReferencingAttribute|`parentobjectid`|
|ReferencedEntityNavigationPropertyName|`flowsession_flowlog_parentobjectid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowsession_flowsession_parentdesktopflowrunid-one-to-many"></a> flowsession_flowsession_parentdesktopflowrunid

Many-To-One Relationship: [flowsession flowsession_flowsession_parentdesktopflowrunid](#BKMK_flowsession_flowsession_parentdesktopflowrunid-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`flowsession`|
|ReferencingAttribute|`parentdesktopflowrunid`|
|ReferencedEntityNavigationPropertyName|`flowsession_flowsession_parentdesktopflowrunid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowsession_flowsessionbinary_FlowSessionId"></a> flowsession_flowsessionbinary_FlowSessionId

Many-To-One Relationship: [flowsessionbinary flowsession_flowsessionbinary_FlowSessionId](flowsessionbinary.md#BKMK_flowsession_flowsessionbinary_FlowSessionId)

|Property|Value|
|---|---|
|ReferencingEntity|`flowsessionbinary`|
|ReferencingAttribute|`flowsessionid`|
|ReferencedEntityNavigationPropertyName|`flowsession_flowsessionbinary_flowsessionid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowsession_MailboxTrackingFolders"></a> flowsession_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder flowsession_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_flowsession_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowsession_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowsession_PrincipalObjectAttributeAccesses"></a> flowsession_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess flowsession_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_flowsession_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`flowsession_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowsession_SyncErrors"></a> flowsession_SyncErrors

Many-To-One Relationship: [syncerror flowsession_SyncErrors](syncerror.md#BKMK_flowsession_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowsession_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowsession_workflowbinary_FlowSessionId"></a> flowsession_workflowbinary_FlowSessionId

Many-To-One Relationship: [workflowbinary flowsession_workflowbinary_FlowSessionId](workflowbinary.md#BKMK_flowsession_workflowbinary_FlowSessionId)

|Property|Value|
|---|---|
|ReferencingEntity|`workflowbinary`|
|ReferencingAttribute|`flowsessionid`|
|ReferencedEntityNavigationPropertyName|`flowsession_workflowbinary_FlowSessionId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_taggedflowsession_FlowSession_flowsession"></a> taggedflowsession_FlowSession_flowsession

Many-To-One Relationship: [taggedflowsession taggedflowsession_FlowSession_flowsession](taggedflowsession.md#BKMK_taggedflowsession_FlowSession_flowsession)

|Property|Value|
|---|---|
|ReferencingEntity|`taggedflowsession`|
|ReferencingAttribute|`flowsession`|
|ReferencedEntityNavigationPropertyName|`taggedflowsession_FlowSession_flowsession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.flowsession?displayProperty=fullName>
