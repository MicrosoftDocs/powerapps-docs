---
title: "Flow Log (flowlog) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Flow Log (flowlog) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Flow Log (flowlog) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Flow Log (flowlog) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /flowlogs<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /flowlogs(*flowlogid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `DeleteMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.DeleteMultiple?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /flowlogs(*flowlogid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /flowlogs<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /flowlogs(*flowlogid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: True |`PATCH` /flowlogs(*flowlogid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Flow Log (flowlog) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Flow Log** |
| **DisplayCollectionName** | **Flow Logs** |
| **SchemaName** | `flowlog` |
| **CollectionSchemaName** | `flowlogs` |
| **EntitySetName** | `flowlogs`|
| **LogicalName** | `flowlog` |
| **LogicalCollectionName** | `flowlogs` |
| **PrimaryIdAttribute** | `flowlogid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Elastic` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [cloudflowid](#BKMK_cloudflowid)
- [cloudflowrunid](#BKMK_cloudflowrunid)
- [cloudflowrunidPId](#BKMK_cloudflowrunidPId)
- [data](#BKMK_data)
- [desktopflowid](#BKMK_desktopflowid)
- [Duration](#BKMK_Duration)
- [flowlogId](#BKMK_flowlogId)
- [flowmachinegroupid](#BKMK_flowmachinegroupid)
- [flowmachineid](#BKMK_flowmachineid)
- [flowsessionid](#BKMK_flowsessionid)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [InputsLocalizedNames](#BKMK_InputsLocalizedNames)
- [level](#BKMK_level)
- [LogIndex](#BKMK_LogIndex)
- [Name](#BKMK_Name)
- [OutputsLocalizedNames](#BKMK_OutputsLocalizedNames)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [parentobjectid](#BKMK_parentobjectid)
- [parentobjectidIdType](#BKMK_parentobjectidIdType)
- [PartitionId](#BKMK_PartitionId)
- [TTLInSeconds](#BKMK_TTLInSeconds)
- [type](#BKMK_type)
- [workqueueid](#BKMK_workqueueid)
- [workqueueitemid](#BKMK_workqueueitemid)

### <a name="BKMK_cloudflowid"></a> cloudflowid

|Property|Value|
|---|---|
|Description|**The Power Automate Cloud Flow Id this log is linked to.**|
|DisplayName|**Cloud Flow Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cloudflowid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|workflow|

### <a name="BKMK_cloudflowrunid"></a> cloudflowrunid

|Property|Value|
|---|---|
|Description|**The Power Automate Cloud Flow run this log is linked to.**|
|DisplayName|**Cloud Flow Run Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cloudflowrunid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|flowrun|

### <a name="BKMK_cloudflowrunidPId"></a> cloudflowrunidPId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`cloudflowrunidpid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_data"></a> data

|Property|Value|
|---|---|
|Description|**The logged data.**|
|DisplayName|**Data**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`data`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Json|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_desktopflowid"></a> desktopflowid

|Property|Value|
|---|---|
|Description|**The Desktop Flow Id this log is linked to.**|
|DisplayName|**Desktop Flow Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`desktopflowid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|workflow|

### <a name="BKMK_Duration"></a> Duration

|Property|Value|
|---|---|
|Description|**Duration of the action in millisecond.**|
|DisplayName|**Duration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`duration`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_flowlogId"></a> flowlogId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Flow Log**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`flowlogid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_flowmachinegroupid"></a> flowmachinegroupid

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`flowmachinegroupid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|flowmachinegroup|

### <a name="BKMK_flowmachineid"></a> flowmachineid

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`flowmachineid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|flowmachine|

### <a name="BKMK_flowsessionid"></a> flowsessionid

|Property|Value|
|---|---|
|Description|**The Power Automate Desktop Flow Session this log belongs to.**|
|DisplayName|**Flow Session Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`flowsessionid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|flowsession|

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

### <a name="BKMK_InputsLocalizedNames"></a> InputsLocalizedNames

|Property|Value|
|---|---|
|Description|**Array of the names of the inputs.**|
|DisplayName|**InputsLocalizedNames**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`inputslocalizednames`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Json|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_level"></a> level

|Property|Value|
|---|---|
|Description|**The level of the log.**|
|DisplayName|**Level**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`level`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`flowlog_level`|

#### level Choices/Options

|Value|Label|
|---|---|
|100000000|**Verbose**|
|100000001|**Debug**|
|100000002|**Info**|
|100000003|**Warning**|
|100000004|**Error**|

### <a name="BKMK_LogIndex"></a> LogIndex

|Property|Value|
|---|---|
|Description|**Index of the log within the flow excution**|
|DisplayName|**LogIndex**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`logindex`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**The name of the log.**|
|DisplayName|**Log Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OutputsLocalizedNames"></a> OutputsLocalizedNames

|Property|Value|
|---|---|
|Description|**Array of the names of the outputs.**|
|DisplayName|**OutputsLocalizedNames**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`outputslocalizednames`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Json|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

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

### <a name="BKMK_parentobjectid"></a> parentobjectid

|Property|Value|
|---|---|
|Description|**The id of the parent object.**|
|DisplayName|**Parent Object Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentobjectid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|flowmachinegroup, flowsession, workqueue|

### <a name="BKMK_parentobjectidIdType"></a> parentobjectidIdType

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parentobjectididtype`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_PartitionId"></a> PartitionId

|Property|Value|
|---|---|
|Description|**Logical partition id. A logical partition consists of a set of records with same partition id.**|
|DisplayName|**Partition Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`partitionid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_TTLInSeconds"></a> TTLInSeconds

|Property|Value|
|---|---|
|Description|**Time to live in seconds.**|
|DisplayName|**Time to live**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ttlinseconds`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|1|

### <a name="BKMK_type"></a> type

|Property|Value|
|---|---|
|Description|**The type of the log.**|
|DisplayName|**Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`type`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`flowlog_type`|

#### type Choices/Options

|Value|Label|
|---|---|
|100000000|**CustomLog**|
|100000001|**DesktopFlowRunAction**|
|100000002|**DesktopFlowRunQueuePriorityChanged**|
|100000003|**DesktopFlowRunQueued**|
|100000004|**DesktopFlowRunQueueAssigned**|
|100000005|**DesktopFlowRunQueueAssignFailed**|
|100000006|**DesktopFlowRunQueueRunConfirmed**|
|100000007|**DesktopFlowRunQueueRunCompleted**|
|100000100|**DesktopFlowRunUnattendedRepairUISelectorRequest**|
|100000101|**DesktopFlowRunUnattendedRepairUISelectorResponse**|
|100000200|**WorkqueueFlowSession**|
|100000201|**WorkqueueProcessorLog**|
|100000300|**DesktopFlowOrchestrationRepairSessionMismatchRequest**|
|100000301|**DesktopFlowOrchestrationRepairSessionMismatchResponse**|
|100000310|**DesktopFlowOrchestrationRepairWindowsIdentityIncorrectRequest**|
|100000311|**DesktopFlowOrchestrationRepairWindowsIdentityIncorrectResponse**|

### <a name="BKMK_workqueueid"></a> workqueueid

|Property|Value|
|---|---|
|Description|**The Work Queue this log is linked to.**|
|DisplayName|**Work Queue Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`workqueueid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|workqueue|

### <a name="BKMK_workqueueitemid"></a> workqueueitemid

|Property|Value|
|---|---|
|Description|**The Work Queue Item this log is linked to.**|
|DisplayName|**Work Queue Item Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`workqueueitemid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|workqueueitem|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)

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
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

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
|Targets||

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
|Targets||

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
|Targets||

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

- [flowmachine_flowlog_flowmachineid](#BKMK_flowmachine_flowlog_flowmachineid)
- [flowmachinegroup_flowlog_flowmachinegroupid](#BKMK_flowmachinegroup_flowlog_flowmachinegroupid)
- [flowmachinegroup_flowlog_parentobjectid](#BKMK_flowmachinegroup_flowlog_parentobjectid)
- [flowrun_flowlog_cloudflowrunid](#BKMK_flowrun_flowlog_cloudflowrunid)
- [flowsession_flowlog_flowsessionid](#BKMK_flowsession_flowlog_flowsessionid)
- [flowsession_flowlog_parentobjectid](#BKMK_flowsession_flowlog_parentobjectid)
- [lk_flowlog_createdby](#BKMK_lk_flowlog_createdby)
- [lk_flowlog_createdonbehalfby](#BKMK_lk_flowlog_createdonbehalfby)
- [lk_flowlog_modifiedby](#BKMK_lk_flowlog_modifiedby)
- [lk_flowlog_modifiedonbehalfby](#BKMK_lk_flowlog_modifiedonbehalfby)
- [workflow_flowlog_cloudflowid](#BKMK_workflow_flowlog_cloudflowid)
- [workflow_flowlog_desktopflowid](#BKMK_workflow_flowlog_desktopflowid)
- [workqueue_flowlog_parentobjectid](#BKMK_workqueue_flowlog_parentobjectid)
- [workqueue_flowlog_workqueueid](#BKMK_workqueue_flowlog_workqueueid)
- [workqueueitem_flowlog_workqueueitemid](#BKMK_workqueueitem_flowlog_workqueueitemid)

### <a name="BKMK_flowmachine_flowlog_flowmachineid"></a> flowmachine_flowlog_flowmachineid

One-To-Many Relationship: [flowmachine flowmachine_flowlog_flowmachineid](flowmachine.md#BKMK_flowmachine_flowlog_flowmachineid)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachine`|
|ReferencedAttribute|`flowmachineid`|
|ReferencingAttribute|`flowmachineid`|
|ReferencingEntityNavigationPropertyName|`flowmachineid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinegroup_flowlog_flowmachinegroupid"></a> flowmachinegroup_flowlog_flowmachinegroupid

One-To-Many Relationship: [flowmachinegroup flowmachinegroup_flowlog_flowmachinegroupid](flowmachinegroup.md#BKMK_flowmachinegroup_flowlog_flowmachinegroupid)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinegroup`|
|ReferencedAttribute|`flowmachinegroupid`|
|ReferencingAttribute|`flowmachinegroupid`|
|ReferencingEntityNavigationPropertyName|`flowmachinegroupid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinegroup_flowlog_parentobjectid"></a> flowmachinegroup_flowlog_parentobjectid

One-To-Many Relationship: [flowmachinegroup flowmachinegroup_flowlog_parentobjectid](flowmachinegroup.md#BKMK_flowmachinegroup_flowlog_parentobjectid)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinegroup`|
|ReferencedAttribute|`flowmachinegroupid`|
|ReferencingAttribute|`parentobjectid`|
|ReferencingEntityNavigationPropertyName|`parentobjectid_flowmachinegroup`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowrun_flowlog_cloudflowrunid"></a> flowrun_flowlog_cloudflowrunid

One-To-Many Relationship: [flowrun flowrun_flowlog_cloudflowrunid](flowrun.md#BKMK_flowrun_flowlog_cloudflowrunid)

|Property|Value|
|---|---|
|ReferencedEntity|`flowrun`|
|ReferencedAttribute|`flowrunid`|
|ReferencingAttribute|`cloudflowrunid`|
|ReferencingEntityNavigationPropertyName|`cloudflowrunid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowsession_flowlog_flowsessionid"></a> flowsession_flowlog_flowsessionid

One-To-Many Relationship: [flowsession flowsession_flowlog_flowsessionid](flowsession.md#BKMK_flowsession_flowlog_flowsessionid)

|Property|Value|
|---|---|
|ReferencedEntity|`flowsession`|
|ReferencedAttribute|`flowsessionid`|
|ReferencingAttribute|`flowsessionid`|
|ReferencingEntityNavigationPropertyName|`flowsessionid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowsession_flowlog_parentobjectid"></a> flowsession_flowlog_parentobjectid

One-To-Many Relationship: [flowsession flowsession_flowlog_parentobjectid](flowsession.md#BKMK_flowsession_flowlog_parentobjectid)

|Property|Value|
|---|---|
|ReferencedEntity|`flowsession`|
|ReferencedAttribute|`flowsessionid`|
|ReferencingAttribute|`parentobjectid`|
|ReferencingEntityNavigationPropertyName|`parentobjectid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowlog_createdby"></a> lk_flowlog_createdby

One-To-Many Relationship: [systemuser lk_flowlog_createdby](systemuser.md#BKMK_lk_flowlog_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowlog_createdonbehalfby"></a> lk_flowlog_createdonbehalfby

One-To-Many Relationship: [systemuser lk_flowlog_createdonbehalfby](systemuser.md#BKMK_lk_flowlog_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowlog_modifiedby"></a> lk_flowlog_modifiedby

One-To-Many Relationship: [systemuser lk_flowlog_modifiedby](systemuser.md#BKMK_lk_flowlog_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowlog_modifiedonbehalfby"></a> lk_flowlog_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_flowlog_modifiedonbehalfby](systemuser.md#BKMK_lk_flowlog_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflow_flowlog_cloudflowid"></a> workflow_flowlog_cloudflowid

One-To-Many Relationship: [workflow workflow_flowlog_cloudflowid](workflow.md#BKMK_workflow_flowlog_cloudflowid)

|Property|Value|
|---|---|
|ReferencedEntity|`workflow`|
|ReferencedAttribute|`workflowid`|
|ReferencingAttribute|`cloudflowid`|
|ReferencingEntityNavigationPropertyName|`cloudflowid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflow_flowlog_desktopflowid"></a> workflow_flowlog_desktopflowid

One-To-Many Relationship: [workflow workflow_flowlog_desktopflowid](workflow.md#BKMK_workflow_flowlog_desktopflowid)

|Property|Value|
|---|---|
|ReferencedEntity|`workflow`|
|ReferencedAttribute|`workflowid`|
|ReferencingAttribute|`desktopflowid`|
|ReferencingEntityNavigationPropertyName|`desktopflowid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workqueue_flowlog_parentobjectid"></a> workqueue_flowlog_parentobjectid

One-To-Many Relationship: [workqueue workqueue_flowlog_parentobjectid](workqueue.md#BKMK_workqueue_flowlog_parentobjectid)

|Property|Value|
|---|---|
|ReferencedEntity|`workqueue`|
|ReferencedAttribute|`workqueueid`|
|ReferencingAttribute|`parentobjectid`|
|ReferencingEntityNavigationPropertyName|`parentobjectid_workqueue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workqueue_flowlog_workqueueid"></a> workqueue_flowlog_workqueueid

One-To-Many Relationship: [workqueue workqueue_flowlog_workqueueid](workqueue.md#BKMK_workqueue_flowlog_workqueueid)

|Property|Value|
|---|---|
|ReferencedEntity|`workqueue`|
|ReferencedAttribute|`workqueueid`|
|ReferencingAttribute|`workqueueid`|
|ReferencingEntityNavigationPropertyName|`workqueueid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workqueueitem_flowlog_workqueueitemid"></a> workqueueitem_flowlog_workqueueitemid

One-To-Many Relationship: [workqueueitem workqueueitem_flowlog_workqueueitemid](workqueueitem.md#BKMK_workqueueitem_flowlog_workqueueitemid)

|Property|Value|
|---|---|
|ReferencedEntity|`workqueueitem`|
|ReferencedAttribute|`workqueueitemid`|
|ReferencingAttribute|`workqueueitemid`|
|ReferencingEntityNavigationPropertyName|`workqueueitemid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.flowlog?displayProperty=fullName>
