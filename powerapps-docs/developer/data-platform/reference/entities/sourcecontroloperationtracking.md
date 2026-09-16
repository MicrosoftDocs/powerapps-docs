---
title: "Source Control Operation Tracking (SourceControlOperationTracking) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Source Control Operation Tracking (SourceControlOperationTracking) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: JimDaly
ms.author: jdaly
ms.reviewer: jdaly
search.audienceType: 
  - developer
---

# Source Control Operation Tracking (SourceControlOperationTracking) table/entity reference (Microsoft Dataverse)

Tracks the lifecycle of source control operations and their sub-operations in the org database.

## Messages

The following table lists the messages for the Source Control Operation Tracking (SourceControlOperationTracking) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /sourcecontroloperationtrackings<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /sourcecontroloperationtrackings(*sourcecontroloperationtrackingid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Restore`<br />Event: True |<xref:Microsoft.Dynamics.CRM.Restore?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retrieve`<br />Event: True |`GET` /sourcecontroloperationtrackings(*sourcecontroloperationtrackingid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /sourcecontroloperationtrackings<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /sourcecontroloperationtrackings(*sourcecontroloperationtrackingid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /sourcecontroloperationtrackings(*sourcecontroloperationtrackingid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /sourcecontroloperationtrackings(*sourcecontroloperationtrackingid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Source Control Operation Tracking (SourceControlOperationTracking) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Source Control Operation Tracking (SourceControlOperationTracking) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Source Control Operation Tracking** |
| **DisplayCollectionName** | **Source Control Operation Trackings** |
| **SchemaName** | `SourceControlOperationTracking` |
| **CollectionSchemaName** | `SourceControlOperationTrackings` |
| **EntitySetName** | `sourcecontroloperationtrackings`|
| **LogicalName** | `sourcecontroloperationtracking` |
| **LogicalCollectionName** | `sourcecontroloperationtrackings` |
| **PrimaryIdAttribute** | `sourcecontroloperationtrackingid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AdditionalInfo](#BKMK_AdditionalInfo)
- [AsyncOperationId](#BKMK_AsyncOperationId)
- [EndTime](#BKMK_EndTime)
- [Error](#BKMK_Error)
- [ErrorDetails](#BKMK_ErrorDetails)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [name](#BKMK_name)
- [OperationName](#BKMK_OperationName)
- [OperationType](#BKMK_OperationType)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [SolutionId](#BKMK_SolutionId)
- [SolutionName](#BKMK_SolutionName)
- [SourceControlOperationTrackingId](#BKMK_SourceControlOperationTrackingId)
- [StartTime](#BKMK_StartTime)
- [statecode](#BKMK_statecode)
- [Status](#BKMK_Status)
- [statuscode](#BKMK_statuscode)
- [SubOperationName](#BKMK_SubOperationName)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_AdditionalInfo"></a> AdditionalInfo

|Property|Value|
|---|---|
|Description|**JSON blob for operation-specific metadata not covered by other columns.**|
|DisplayName|**Additional Info**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`additionalinfo`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_AsyncOperationId"></a> AsyncOperationId

|Property|Value|
|---|---|
|Description|**Async Job OperationId.**|
|DisplayName|**Async Job OperationId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`asyncoperationid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_EndTime"></a> EndTime

|Property|Value|
|---|---|
|Description|**The end time of the operation/sub-operation.**|
|DisplayName|**End Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`endtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_Error"></a> Error

|Property|Value|
|---|---|
|Description|**The error message when the operation fails.**|
|DisplayName|**Error**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`error`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_ErrorDetails"></a> ErrorDetails

|Property|Value|
|---|---|
|Description|**The details for the failed operations.**|
|DisplayName|**Error Details**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`errordetails`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

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

### <a name="BKMK_name"></a> name

|Property|Value|
|---|---|
|Description|**The display name of the operation record.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|400|

### <a name="BKMK_OperationName"></a> OperationName

|Property|Value|
|---|---|
|Description|**Name of the source control operation.**|
|DisplayName|**Operation Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`operationname`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`sourcecontroloperationtracking_operationname`|

#### OperationName Choices/Options

|Value|Label|
|---|---|
|0|**Pull**|
|1|**InitialSync**|
|2|**Disconnect**|
|3|**Commit**|
|4|**Refresh**|
|5|**HandleComponentOperationAsync**|

### <a name="BKMK_OperationType"></a> OperationType

|Property|Value|
|---|---|
|Description|**Whether the operation runs synchronously or asynchronously.**|
|DisplayName|**Operation Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`operationtype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`sourcecontroloperationtracking_operationtype`|

#### OperationType Choices/Options

|Value|Label|
|---|---|
|0|**Sync**|
|1|**Async**|

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

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**The GUID of the solution this operation applies to.**|
|DisplayName|**Solution Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SolutionName"></a> SolutionName

|Property|Value|
|---|---|
|Description|**Denormalized solution unique name for display.**|
|DisplayName|**Solution Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`solutionname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_SourceControlOperationTrackingId"></a> SourceControlOperationTrackingId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Source Control Operation Tracking**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sourcecontroloperationtrackingid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_StartTime"></a> StartTime

|Property|Value|
|---|---|
|Description|**The start time of the operation/sub-operation.**|
|DisplayName|**Start Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`starttime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Source Control Operation Tracking**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`sourcecontroloperationtracking_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_Status"></a> Status

|Property|Value|
|---|---|
|Description|**The status of the operation/sub-operation.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`status`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`sourcecontroloperationtracking_status`|

#### Status Choices/Options

|Value|Label|
|---|---|
|0|**Not Started**|
|1|**Pending**|
|2|**Started**|
|3|**Completed**|
|4|**Failed**|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Source Control Operation Tracking**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`sourcecontroloperationtracking_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_SubOperationName"></a> SubOperationName

|Property|Value|
|---|---|
|Description|**Name of the source control sub-operation.**|
|DisplayName|**Sub-Operation Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`suboperationname`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`sourcecontroloperationtracking_suboperationname`|

#### SubOperationName Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Retrieve files to pull**|
|2|**Import components in environment**|
|3|**Post processing after import.**|
|4|**Create source control component records**|
|5|**Clean up source control records**|
|6|**Delete configuration**|
|7|**Prepare components for commit**|
|8|**Push changes to git**|
|9|**Update committed components**|
|10|**Retrieve git components**|
|11|**Compare and update component statuses**|
|12|**Process staged source control component**|

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

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
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

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier for the organization**|
|DisplayName|**Organization Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|organization|

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

- [lk_sourcecontroloperationtracking_createdby](#BKMK_lk_sourcecontroloperationtracking_createdby)
- [lk_sourcecontroloperationtracking_createdonbehalfby](#BKMK_lk_sourcecontroloperationtracking_createdonbehalfby)
- [lk_sourcecontroloperationtracking_modifiedby](#BKMK_lk_sourcecontroloperationtracking_modifiedby)
- [lk_sourcecontroloperationtracking_modifiedonbehalfby](#BKMK_lk_sourcecontroloperationtracking_modifiedonbehalfby)
- [organization_sourcecontroloperationtracking](#BKMK_organization_sourcecontroloperationtracking)

### <a name="BKMK_lk_sourcecontroloperationtracking_createdby"></a> lk_sourcecontroloperationtracking_createdby

One-To-Many Relationship: [systemuser lk_sourcecontroloperationtracking_createdby](systemuser.md#BKMK_lk_sourcecontroloperationtracking_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sourcecontroloperationtracking_createdonbehalfby"></a> lk_sourcecontroloperationtracking_createdonbehalfby

One-To-Many Relationship: [systemuser lk_sourcecontroloperationtracking_createdonbehalfby](systemuser.md#BKMK_lk_sourcecontroloperationtracking_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sourcecontroloperationtracking_modifiedby"></a> lk_sourcecontroloperationtracking_modifiedby

One-To-Many Relationship: [systemuser lk_sourcecontroloperationtracking_modifiedby](systemuser.md#BKMK_lk_sourcecontroloperationtracking_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sourcecontroloperationtracking_modifiedonbehalfby"></a> lk_sourcecontroloperationtracking_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_sourcecontroloperationtracking_modifiedonbehalfby](systemuser.md#BKMK_lk_sourcecontroloperationtracking_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_sourcecontroloperationtracking"></a> organization_sourcecontroloperationtracking

One-To-Many Relationship: [organization organization_sourcecontroloperationtracking](organization.md#BKMK_organization_sourcecontroloperationtracking)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [sourcecontroloperationtracking_AsyncOperations](#BKMK_sourcecontroloperationtracking_AsyncOperations)
- [sourcecontroloperationtracking_BulkDeleteFailures](#BKMK_sourcecontroloperationtracking_BulkDeleteFailures)
- [sourcecontroloperationtracking_DeletedItemReferences](#BKMK_sourcecontroloperationtracking_DeletedItemReferences)
- [sourcecontroloperationtracking_MailboxTrackingFolders](#BKMK_sourcecontroloperationtracking_MailboxTrackingFolders)
- [sourcecontroloperationtracking_PrincipalObjectAttributeAccesses](#BKMK_sourcecontroloperationtracking_PrincipalObjectAttributeAccesses)
- [sourcecontroloperationtracking_ProcessSession](#BKMK_sourcecontroloperationtracking_ProcessSession)
- [sourcecontroloperationtracking_SyncErrors](#BKMK_sourcecontroloperationtracking_SyncErrors)

### <a name="BKMK_sourcecontroloperationtracking_AsyncOperations"></a> sourcecontroloperationtracking_AsyncOperations

Many-To-One Relationship: [asyncoperation sourcecontroloperationtracking_AsyncOperations](asyncoperation.md#BKMK_sourcecontroloperationtracking_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`sourcecontroloperationtracking_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sourcecontroloperationtracking_BulkDeleteFailures"></a> sourcecontroloperationtracking_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure sourcecontroloperationtracking_BulkDeleteFailures](bulkdeletefailure.md#BKMK_sourcecontroloperationtracking_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`sourcecontroloperationtracking_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sourcecontroloperationtracking_DeletedItemReferences"></a> sourcecontroloperationtracking_DeletedItemReferences

Many-To-One Relationship: [deleteditemreference sourcecontroloperationtracking_DeletedItemReferences](deleteditemreference.md#BKMK_sourcecontroloperationtracking_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencingEntity|`deleteditemreference`|
|ReferencingAttribute|`deletedobject`|
|ReferencedEntityNavigationPropertyName|`sourcecontroloperationtracking_DeletedItemReferences`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sourcecontroloperationtracking_MailboxTrackingFolders"></a> sourcecontroloperationtracking_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder sourcecontroloperationtracking_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_sourcecontroloperationtracking_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`sourcecontroloperationtracking_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sourcecontroloperationtracking_PrincipalObjectAttributeAccesses"></a> sourcecontroloperationtracking_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess sourcecontroloperationtracking_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_sourcecontroloperationtracking_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`sourcecontroloperationtracking_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sourcecontroloperationtracking_ProcessSession"></a> sourcecontroloperationtracking_ProcessSession

Many-To-One Relationship: [processsession sourcecontroloperationtracking_ProcessSession](processsession.md#BKMK_sourcecontroloperationtracking_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`sourcecontroloperationtracking_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sourcecontroloperationtracking_SyncErrors"></a> sourcecontroloperationtracking_SyncErrors

Many-To-One Relationship: [syncerror sourcecontroloperationtracking_SyncErrors](syncerror.md#BKMK_sourcecontroloperationtracking_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`sourcecontroloperationtracking_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.sourcecontroloperationtracking?displayProperty=fullName>
