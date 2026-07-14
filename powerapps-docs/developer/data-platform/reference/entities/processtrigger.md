---
title: "Process Trigger (ProcessTrigger) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Process Trigger (ProcessTrigger) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Process Trigger (ProcessTrigger) table/entity reference (Microsoft Dataverse)

Trigger that invoke a rule.

## Messages

The following table lists the messages for the Process Trigger (ProcessTrigger) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /processtriggers<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /processtriggers(*processtriggerid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /processtriggers(*processtriggerid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /processtriggers<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /processtriggers(*processtriggerid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /processtriggers(*processtriggerid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Process Trigger (ProcessTrigger) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Process Trigger** |
| **DisplayCollectionName** | **Process Triggers** |
| **SchemaName** | `ProcessTrigger` |
| **CollectionSchemaName** | `ProcessTriggers` |
| **EntitySetName** | `processtriggers`|
| **LogicalName** | `processtrigger` |
| **LogicalCollectionName** | `processtriggers` |
| **PrimaryIdAttribute** | `processtriggerid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ControlName](#BKMK_ControlName)
- [ControlType](#BKMK_ControlType)
- [Event](#BKMK_Event)
- [FormId](#BKMK_FormId)
- [IsCustomizable](#BKMK_IsCustomizable)
- [MethodId](#BKMK_MethodId)
- [PipelineStage](#BKMK_PipelineStage)
- [PrimaryEntityTypeCode](#BKMK_PrimaryEntityTypeCode)
- [ProcessId](#BKMK_ProcessId)
- [ProcessTriggerId](#BKMK_ProcessTriggerId)
- [Scope](#BKMK_Scope)

### <a name="BKMK_ControlName"></a> ControlName

|Property|Value|
|---|---|
|Description|**Name of the control.**|
|DisplayName|**Control Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`controlname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ControlType"></a> ControlType

|Property|Value|
|---|---|
|Description|**Type of the control to which this trigger is bound**|
|DisplayName|**Control Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`controltype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`processtrigger_controltype`|

#### ControlType Choices/Options

|Value|Label|
|---|---|
|1|**Attribute**|
|2|**Form Tab**|

### <a name="BKMK_Event"></a> Event

|Property|Value|
|---|---|
|Description|**Indicates the event.**|
|DisplayName|**Event**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`event`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_FormId"></a> FormId

|Property|Value|
|---|---|
|Description|**Unique identifier of the form associated with the trigger.**|
|DisplayName|**Form**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`formid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemform|

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**Indicates whether this component can be customized.**|
|DisplayName|**Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_MethodId"></a> MethodId

|Property|Value|
|---|---|
|Description|**Displays StageID to which the PBL rule belongs to**|
|DisplayName|**MethodId**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`methodid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_PipelineStage"></a> PipelineStage

|Property|Value|
|---|---|
|Description|**Pipeline Stage to Execute Workflow Event Plugin.**|
|DisplayName|**PipelineStage**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`pipelinestage`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`processtrigger_pipelinestage`|

#### PipelineStage Choices/Options

|Value|Label|
|---|---|
|0|**Default Value**|
|20|**Before Main Operation**|
|40|**After Main Operation**|

### <a name="BKMK_PrimaryEntityTypeCode"></a> PrimaryEntityTypeCode

|Property|Value|
|---|---|
|Description|**Primary entity for the process which is invoked by the event.**|
|DisplayName|**Primary Entity**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`primaryentitytypecode`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_ProcessId"></a> ProcessId

|Property|Value|
|---|---|
|Description|**Shows the ID of the process.**|
|DisplayName|**Process**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|workflow|

### <a name="BKMK_ProcessTriggerId"></a> ProcessTriggerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the process trigger record.**|
|DisplayName|**Process Trigger**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processtriggerid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Scope"></a> Scope

|Property|Value|
|---|---|
|Description|**Scope level for PBL rules.**|
|DisplayName|**Scope**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`scope`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`pbl_scope`|

#### Scope Choices/Options

|Value|Label|
|---|---|
|1|**Form**|
|2|**Entity**|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningUser](#BKMK_OwningUser)
- [ProcessTriggerIdUnique](#BKMK_ProcessTriggerIdUnique)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

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
|DefaultFormValue|-1|
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
|Description|**Shows who created the record.**|
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
|Description|**Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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
|Description|**Shows who created the record on behalf of another user.**|
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
|Description|**Shows who last updated the record.**|
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
|Description|**Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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
|Description|**Shows who last updated the record on behalf of another user.**|
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
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.**|
|DisplayName|**Owner**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|ApplicationRequired|
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
|Description|**Select the business unit that owns the record.**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier for the user that owns the record.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ProcessTriggerIdUnique"></a> ProcessTriggerIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Process Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processtriggeridunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [lk_processtriggerbase_createdby](#BKMK_lk_processtriggerbase_createdby)
- [lk_processtriggerbase_createdonbehalfby](#BKMK_lk_processtriggerbase_createdonbehalfby)
- [lk_processtriggerbase_modifiedby](#BKMK_lk_processtriggerbase_modifiedby)
- [lk_processtriggerbase_modifiedonbehalfby](#BKMK_lk_processtriggerbase_modifiedonbehalfby)
- [process_processtrigger](#BKMK_process_processtrigger)
- [processtrigger_systemform](#BKMK_processtrigger_systemform)

### <a name="BKMK_lk_processtriggerbase_createdby"></a> lk_processtriggerbase_createdby

One-To-Many Relationship: [systemuser lk_processtriggerbase_createdby](systemuser.md#BKMK_lk_processtriggerbase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_processtriggerbase_createdonbehalfby"></a> lk_processtriggerbase_createdonbehalfby

One-To-Many Relationship: [systemuser lk_processtriggerbase_createdonbehalfby](systemuser.md#BKMK_lk_processtriggerbase_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_processtriggerbase_modifiedby"></a> lk_processtriggerbase_modifiedby

One-To-Many Relationship: [systemuser lk_processtriggerbase_modifiedby](systemuser.md#BKMK_lk_processtriggerbase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_processtriggerbase_modifiedonbehalfby"></a> lk_processtriggerbase_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_processtriggerbase_modifiedonbehalfby](systemuser.md#BKMK_lk_processtriggerbase_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_process_processtrigger"></a> process_processtrigger

One-To-Many Relationship: [workflow process_processtrigger](workflow.md#BKMK_process_processtrigger)

|Property|Value|
|---|---|
|ReferencedEntity|`workflow`|
|ReferencedAttribute|`workflowid`|
|ReferencingAttribute|`processid`|
|ReferencingEntityNavigationPropertyName|`processid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_processtrigger_systemform"></a> processtrigger_systemform

One-To-Many Relationship: [systemform processtrigger_systemform](systemform.md#BKMK_processtrigger_systemform)

|Property|Value|
|---|---|
|ReferencedEntity|`systemform`|
|ReferencedAttribute|`formid`|
|ReferencingAttribute|`formid`|
|ReferencingEntityNavigationPropertyName|`formid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_ProcessTrigger_SyncErrors"></a> ProcessTrigger_SyncErrors

Many-To-One Relationship: [syncerror ProcessTrigger_SyncErrors](syncerror.md#BKMK_ProcessTrigger_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`ProcessTrigger_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.processtrigger?displayProperty=fullName>
