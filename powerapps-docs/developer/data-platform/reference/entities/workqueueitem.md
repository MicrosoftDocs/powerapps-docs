---
title: "Work Queue Item (workqueueitem) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Work Queue Item (workqueueitem) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Work Queue Item (workqueueitem) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Work Queue Item (workqueueitem) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `AddWorkQueueItemProcessingHistoryEntry`<br />Event: False |<xref:Microsoft.Dynamics.CRM.AddWorkQueueItemProcessingHistoryEntry?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Assign`<br />Event: True |`PATCH` /workqueueitems(*workqueueitemid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /workqueueitems<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /workqueueitems(*workqueueitemid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /workqueueitems(*workqueueitemid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /workqueueitems<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /workqueueitems(*workqueueitemid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /workqueueitems(*workqueueitemid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /workqueueitems(*workqueueitemid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Work Queue Item (workqueueitem) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Work Queue Item** |
| **DisplayCollectionName** | **Work Queue Items** |
| **SchemaName** | `workqueueitem` |
| **CollectionSchemaName** | `workqueueitems` |
| **EntitySetName** | `workqueueitems`|
| **LogicalName** | `workqueueitem` |
| **LogicalCollectionName** | `workqueueitems` |
| **PrimaryIdAttribute** | `workqueueitemid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [completedon](#BKMK_completedon)
- [delayuntil](#BKMK_delayuntil)
- [executioncontext](#BKMK_executioncontext)
- [expirydate](#BKMK_expirydate)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [input](#BKMK_input)
- [IsCustomizable](#BKMK_IsCustomizable)
- [machineuser](#BKMK_machineuser)
- [name](#BKMK_name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [priority](#BKMK_priority)
- [processingduration](#BKMK_processingduration)
- [processingresult](#BKMK_processingresult)
- [processingstarttime](#BKMK_processingstarttime)
- [processinguser](#BKMK_processinguser)
- [processorid](#BKMK_processorid)
- [processortype](#BKMK_processortype)
- [requeuecount](#BKMK_requeuecount)
- [retrycount](#BKMK_retrycount)
- [slastatus](#BKMK_slastatus)
- [slathresholddate](#BKMK_slathresholddate)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [uniqueidbyqueue](#BKMK_uniqueidbyqueue)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [workqueueid](#BKMK_workqueueid)
- [workqueueitemId](#BKMK_workqueueitemId)

### <a name="BKMK_completedon"></a> completedon

|Property|Value|
|---|---|
|Description|**The date and time when the work queue item was completed.**|
|DisplayName|**Completed on**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`completedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_delayuntil"></a> delayuntil

|Property|Value|
|---|---|
|Description|**The date and time after which the work queue item can be dequeued again.**|
|DisplayName|**Delay until**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`delayuntil`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_executioncontext"></a> executioncontext

|Property|Value|
|---|---|
|Description|**The execution context contains a system-managed list of processing attempts, along with important debugging information.**|
|DisplayName|**Execution Context**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`executioncontext`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_expirydate"></a> expirydate

|Property|Value|
|---|---|
|Description|**The expiry date indicates the deadline when the work queue items has to be processed by.**|
|DisplayName|**Expiry Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`expirydate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

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

### <a name="BKMK_input"></a> input

|Property|Value|
|---|---|
|Description|**The input field contains the actual work item data used for processing by bots, humans, or integrations.**|
|DisplayName|**Input**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`input`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Is Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_machineuser"></a> machineuser

|Property|Value|
|---|---|
|Description|**Machine User that processed the item.**|
|DisplayName|**Machine User**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`machineuser`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_name"></a> name

|Property|Value|
|---|---|
|Description|**The name of the work queue item which is by default set to an auto number (e.g., 2023-02-13-000000001).**|
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

### <a name="BKMK_priority"></a> priority

|Property|Value|
|---|---|
|Description|**The priority value determines the pick and processing order for work queue items in a work queue. A lower value corresponds to a higher priority with 1 being the highest.**|
|DisplayName|**Priority**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`priority`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|1|

### <a name="BKMK_processingduration"></a> processingduration

|Property|Value|
|---|---|
|Description|**The duration of the processing in seconds.**|
|DisplayName|**Processing Duration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`processingduration`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_processingresult"></a> processingresult

|Property|Value|
|---|---|
|Description||
|DisplayName|**Processing Result**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`processingresult`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_processingstarttime"></a> processingstarttime

|Property|Value|
|---|---|
|Description|**The date and time when the processing has started.**|
|DisplayName|**Processing Start Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`processingstarttime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_processinguser"></a> processinguser

|Property|Value|
|---|---|
|Description|**Unique identifier for the user that processed the item.**|
|DisplayName|**Processing User**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`processinguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_processorid"></a> processorid

|Property|Value|
|---|---|
|Description|**Unique identifier for the processor (workflow, flowmachine, etc.) that processed the item.**|
|DisplayName|**Processor id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`processorid`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_processortype"></a> processortype

|Property|Value|
|---|---|
|Description|**The processor type allows to display if the item was processed through a cloud flow, a flow machine or another processor type.**|
|DisplayName|**Processor Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`processortype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`workqueueitem_processortype`|

#### processortype Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Cloud Flow**|
|2|**Flow Machine**|

### <a name="BKMK_requeuecount"></a> requeuecount

|Property|Value|
|---|---|
|Description|**The number of times the item has been requeued.**|
|DisplayName|**Requeue Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`requeuecount`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_retrycount"></a> retrycount

|Property|Value|
|---|---|
|Description|**The number of times the item has been retried.**|
|DisplayName|**Retry Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`retrycount`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_slastatus"></a> slastatus

|Property|Value|
|---|---|
|Description|**The SLA status provides more context for on the item processing status (In SLA, At Risk, Out of SLA).**|
|DisplayName|**SLA Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`slastatus`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`workqueueitem_slastatus`|

#### slastatus Choices/Options

|Value|Label|
|---|---|
|0|**NotSet**|
|1|**In**|
|2|**AtRisk**|
|3|**Out**|

### <a name="BKMK_slathresholddate"></a> slathresholddate

|Property|Value|
|---|---|
|Description|**Date and time on which the work queue item starts to be at risk of SLA violation.**|
|DisplayName|**SLA Threshold Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`slathresholddate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**The status of the work queue item (Queued, Processed, Exception etc.)**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`workqueueitem_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Queued**<br />DefaultStatus: 0<br />InvariantName: `Queued`|
|1|Label: **Processing**<br />DefaultStatus: 1<br />InvariantName: `Processing`|
|2|Label: **Processed**<br />DefaultStatus: 2<br />InvariantName: `Processed`|
|3|Label: **OnHold**<br />DefaultStatus: 3<br />InvariantName: `OnHold`|
|4|Label: **Error**<br />DefaultStatus: 4<br />InvariantName: `Error`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**The status reason provides more context for a set status (Queued, Processing, On hold etc.).**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`workqueueitem_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Queued**<br />State:0<br />TransitionData: None|
|1|Label: **Processing**<br />State:1<br />TransitionData: None|
|2|Label: **Processed**<br />State:2<br />TransitionData: None|
|3|Label: **Paused**<br />State:3<br />TransitionData: None|
|4|Label: **GenericException**<br />State:4<br />TransitionData: None|
|5|Label: **ITException**<br />State:4<br />TransitionData: None|
|6|Label: **BusinessException**<br />State:4<br />TransitionData: None|
|7|Label: **DeadLetter**<br />State:4<br />TransitionData: None|
|8|Label: **ProcessingTimeout**<br />State:4<br />TransitionData: None|

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

### <a name="BKMK_uniqueidbyqueue"></a> uniqueidbyqueue

|Property|Value|
|---|---|
|Description|**An identifier of the work queue item used to uniquely identify a work queue item inside a work queue.**|
|DisplayName|**Unique Id By Queue**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`uniqueidbyqueue`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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

### <a name="BKMK_workqueueid"></a> workqueueid

|Property|Value|
|---|---|
|Description|**The work queue id of the parent work queue record.**|
|DisplayName|**Work Queue Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`workqueueid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|workqueue|

### <a name="BKMK_workqueueitemId"></a> workqueueitemId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances.**|
|DisplayName|**Work Queue Item**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`workqueueitemid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentIdUnique"></a> ComponentIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Row id unique**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Component State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentstate`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`componentstate`|

#### ComponentState Choices/Options

|Value|Label|
|---|---|
|0|**Published**|
|1|**Unpublished**|
|2|**Deleted**|
|3|**Deleted Unpublished**|

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

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Indicates whether the solution component is part of a managed solution.**|
|DisplayName|**Is Managed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

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

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Record Overwrite Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overwritetime`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

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

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the associated solution.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`supportingsolutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

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

- [business_unit_workqueueitem](#BKMK_business_unit_workqueueitem)
- [lk_workqueueitem_createdby](#BKMK_lk_workqueueitem_createdby)
- [lk_workqueueitem_createdonbehalfby](#BKMK_lk_workqueueitem_createdonbehalfby)
- [lk_workqueueitem_modifiedby](#BKMK_lk_workqueueitem_modifiedby)
- [lk_workqueueitem_modifiedonbehalfby](#BKMK_lk_workqueueitem_modifiedonbehalfby)
- [owner_workqueueitem](#BKMK_owner_workqueueitem)
- [team_workqueueitem](#BKMK_team_workqueueitem)
- [user_workqueueitem](#BKMK_user_workqueueitem)
- [workqueue_workqueueitem](#BKMK_workqueue_workqueueitem)
- [workqueueitem_processinguser](#BKMK_workqueueitem_processinguser)

### <a name="BKMK_business_unit_workqueueitem"></a> business_unit_workqueueitem

One-To-Many Relationship: [businessunit business_unit_workqueueitem](businessunit.md#BKMK_business_unit_workqueueitem)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_workqueueitem_createdby"></a> lk_workqueueitem_createdby

One-To-Many Relationship: [systemuser lk_workqueueitem_createdby](systemuser.md#BKMK_lk_workqueueitem_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_workqueueitem_createdonbehalfby"></a> lk_workqueueitem_createdonbehalfby

One-To-Many Relationship: [systemuser lk_workqueueitem_createdonbehalfby](systemuser.md#BKMK_lk_workqueueitem_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_workqueueitem_modifiedby"></a> lk_workqueueitem_modifiedby

One-To-Many Relationship: [systemuser lk_workqueueitem_modifiedby](systemuser.md#BKMK_lk_workqueueitem_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_workqueueitem_modifiedonbehalfby"></a> lk_workqueueitem_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_workqueueitem_modifiedonbehalfby](systemuser.md#BKMK_lk_workqueueitem_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_workqueueitem"></a> owner_workqueueitem

One-To-Many Relationship: [owner owner_workqueueitem](owner.md#BKMK_owner_workqueueitem)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_workqueueitem"></a> team_workqueueitem

One-To-Many Relationship: [team team_workqueueitem](team.md#BKMK_team_workqueueitem)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_workqueueitem"></a> user_workqueueitem

One-To-Many Relationship: [systemuser user_workqueueitem](systemuser.md#BKMK_user_workqueueitem)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workqueue_workqueueitem"></a> workqueue_workqueueitem

One-To-Many Relationship: [workqueue workqueue_workqueueitem](workqueue.md#BKMK_workqueue_workqueueitem)

|Property|Value|
|---|---|
|ReferencedEntity|`workqueue`|
|ReferencedAttribute|`workqueueid`|
|ReferencingAttribute|`workqueueid`|
|ReferencingEntityNavigationPropertyName|`workqueueid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_workqueueitem_processinguser"></a> workqueueitem_processinguser

One-To-Many Relationship: [systemuser workqueueitem_processinguser](systemuser.md#BKMK_workqueueitem_processinguser)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`processinguser`|
|ReferencingEntityNavigationPropertyName|`processinguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [workqueueitem_AsyncOperations](#BKMK_workqueueitem_AsyncOperations)
- [workqueueitem_BulkDeleteFailures](#BKMK_workqueueitem_BulkDeleteFailures)
- [workqueueitem_DuplicateBaseRecord](#BKMK_workqueueitem_DuplicateBaseRecord)
- [workqueueitem_DuplicateMatchingRecord](#BKMK_workqueueitem_DuplicateMatchingRecord)
- [workqueueitem_flowlog_workqueueitemid](#BKMK_workqueueitem_flowlog_workqueueitemid)
- [workqueueitem_MailboxTrackingFolders](#BKMK_workqueueitem_MailboxTrackingFolders)
- [workqueueitem_PrincipalObjectAttributeAccesses](#BKMK_workqueueitem_PrincipalObjectAttributeAccesses)
- [workqueueitem_ProcessSession](#BKMK_workqueueitem_ProcessSession)
- [workqueueitem_SyncErrors](#BKMK_workqueueitem_SyncErrors)

### <a name="BKMK_workqueueitem_AsyncOperations"></a> workqueueitem_AsyncOperations

Many-To-One Relationship: [asyncoperation workqueueitem_AsyncOperations](asyncoperation.md#BKMK_workqueueitem_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`workqueueitem_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_workqueueitem_BulkDeleteFailures"></a> workqueueitem_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure workqueueitem_BulkDeleteFailures](bulkdeletefailure.md#BKMK_workqueueitem_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`workqueueitem_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_workqueueitem_DuplicateBaseRecord"></a> workqueueitem_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord workqueueitem_DuplicateBaseRecord](duplicaterecord.md#BKMK_workqueueitem_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`workqueueitem_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_workqueueitem_DuplicateMatchingRecord"></a> workqueueitem_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord workqueueitem_DuplicateMatchingRecord](duplicaterecord.md#BKMK_workqueueitem_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`workqueueitem_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_workqueueitem_flowlog_workqueueitemid"></a> workqueueitem_flowlog_workqueueitemid

Many-To-One Relationship: [flowlog workqueueitem_flowlog_workqueueitemid](flowlog.md#BKMK_workqueueitem_flowlog_workqueueitemid)

|Property|Value|
|---|---|
|ReferencingEntity|`flowlog`|
|ReferencingAttribute|`workqueueitemid`|
|ReferencedEntityNavigationPropertyName|`workqueueitem_flowlog_workqueueitemid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_workqueueitem_MailboxTrackingFolders"></a> workqueueitem_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder workqueueitem_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_workqueueitem_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`workqueueitem_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_workqueueitem_PrincipalObjectAttributeAccesses"></a> workqueueitem_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess workqueueitem_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_workqueueitem_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`workqueueitem_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_workqueueitem_ProcessSession"></a> workqueueitem_ProcessSession

Many-To-One Relationship: [processsession workqueueitem_ProcessSession](processsession.md#BKMK_workqueueitem_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`workqueueitem_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_workqueueitem_SyncErrors"></a> workqueueitem_SyncErrors

Many-To-One Relationship: [syncerror workqueueitem_SyncErrors](syncerror.md#BKMK_workqueueitem_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`workqueueitem_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.workqueueitem?displayProperty=fullName>
