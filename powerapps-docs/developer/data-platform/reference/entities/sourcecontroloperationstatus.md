---
title: "Source Control Operation Status (SourceControlOperationStatus) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Source Control Operation Status (SourceControlOperationStatus) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: JimDaly
ms.author: jdaly
ms.reviewer: jdaly
search.audienceType: 
  - developer
---

# Source Control Operation Status (SourceControlOperationStatus) table/entity reference (Microsoft Dataverse)

Stores the status of source control individual operations and their sub-operations.

## Messages

The following table lists the messages for the Source Control Operation Status (SourceControlOperationStatus) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /sourcecontroloperationstatuses<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /sourcecontroloperationstatuses(*sourcecontroloperationstatusid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `DeleteMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.DeleteMultiple?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /sourcecontroloperationstatuses(*sourcecontroloperationstatusid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /sourcecontroloperationstatuses<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /sourcecontroloperationstatuses(*sourcecontroloperationstatusid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: True |`PATCH` /sourcecontroloperationstatuses(*sourcecontroloperationstatusid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Source Control Operation Status (SourceControlOperationStatus) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Source Control Operation Status** |
| **DisplayCollectionName** | **Source Control Operations Status** |
| **SchemaName** | `SourceControlOperationStatus` |
| **CollectionSchemaName** | `SourceControlOperationStatuses` |
| **EntitySetName** | `sourcecontroloperationstatuses`|
| **LogicalName** | `sourcecontroloperationstatus` |
| **LogicalCollectionName** | `sourcecontroloperationstatuses` |
| **PrimaryIdAttribute** | `sourcecontroloperationstatusid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Elastic` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AsyncOperationId](#BKMK_AsyncOperationId)
- [Details](#BKMK_Details)
- [EndTime](#BKMK_EndTime)
- [Error](#BKMK_Error)
- [ErrorDetails](#BKMK_ErrorDetails)
- [ErrorMessage](#BKMK_ErrorMessage)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [name](#BKMK_name)
- [OperationName](#BKMK_OperationName)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PartitionId](#BKMK_PartitionId)
- [SolutionId](#BKMK_SolutionId)
- [SolutionName](#BKMK_SolutionName)
- [SourceControlOperationStatusId](#BKMK_SourceControlOperationStatusId)
- [StartedBy](#BKMK_StartedBy)
- [StartTime](#BKMK_StartTime)
- [Status](#BKMK_Status)
- [SubOperationName](#BKMK_SubOperationName)
- [TTLInSeconds](#BKMK_TTLInSeconds)

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

### <a name="BKMK_Details"></a> Details

|Property|Value|
|---|---|
|Description|**The details for the failed operations.**|
|DisplayName|**Details**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`details`|
|RequiredLevel|None|
|Type|String|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

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

### <a name="BKMK_ErrorMessage"></a> ErrorMessage

|Property|Value|
|---|---|
|Description|**The error message when the operation fails.**|
|DisplayName|**Error Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`errormessage`|
|RequiredLevel|None|
|Type|String|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

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
|Description|**The name of the custom entity.**|
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
|GlobalChoiceName|`sourcecontroloperationstatus_operationname`|

#### OperationName Choices/Options

|Value|Label|
|---|---|
|0|**Pull**|

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

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**Solution Id**|
|DisplayName|**Solution Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_SolutionName"></a> SolutionName

|Property|Value|
|---|---|
|Description|**Name of the solution.**|
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
|MaxLength|200|

### <a name="BKMK_SourceControlOperationStatusId"></a> SourceControlOperationStatusId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Source Control Operation Status**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sourcecontroloperationstatusid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_StartedBy"></a> StartedBy

|Property|Value|
|---|---|
|Description|**The user who initiated the source control operation**|
|DisplayName|**Started By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`startedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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
|GlobalChoiceName|`sourcecontroloperationstatus_status`|

#### Status Choices/Options

|Value|Label|
|---|---|
|0|**Not Started**|
|1|**Pending**|
|2|**Started**|
|3|**Completed**|
|4|**Failed**|

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
|GlobalChoiceName|`sourcecontroloperationstatus_suboperationname`|

#### SubOperationName Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Retrieve files to pull**|
|2|**Import components in environment**|
|3|**Post processing after import.**|

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


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
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

- [lk_sourcecontroloperationstatus_createdby](#BKMK_lk_sourcecontroloperationstatus_createdby)
- [lk_sourcecontroloperationstatus_createdonbehalfby](#BKMK_lk_sourcecontroloperationstatus_createdonbehalfby)
- [lk_sourcecontroloperationstatus_modifiedby](#BKMK_lk_sourcecontroloperationstatus_modifiedby)
- [lk_sourcecontroloperationstatus_modifiedonbehalfby](#BKMK_lk_sourcecontroloperationstatus_modifiedonbehalfby)
- [systemuser_sourcecontroloperationstatus_StartedBy](#BKMK_systemuser_sourcecontroloperationstatus_StartedBy)

### <a name="BKMK_lk_sourcecontroloperationstatus_createdby"></a> lk_sourcecontroloperationstatus_createdby

One-To-Many Relationship: [systemuser lk_sourcecontroloperationstatus_createdby](systemuser.md#BKMK_lk_sourcecontroloperationstatus_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sourcecontroloperationstatus_createdonbehalfby"></a> lk_sourcecontroloperationstatus_createdonbehalfby

One-To-Many Relationship: [systemuser lk_sourcecontroloperationstatus_createdonbehalfby](systemuser.md#BKMK_lk_sourcecontroloperationstatus_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sourcecontroloperationstatus_modifiedby"></a> lk_sourcecontroloperationstatus_modifiedby

One-To-Many Relationship: [systemuser lk_sourcecontroloperationstatus_modifiedby](systemuser.md#BKMK_lk_sourcecontroloperationstatus_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sourcecontroloperationstatus_modifiedonbehalfby"></a> lk_sourcecontroloperationstatus_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_sourcecontroloperationstatus_modifiedonbehalfby](systemuser.md#BKMK_lk_sourcecontroloperationstatus_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_systemuser_sourcecontroloperationstatus_StartedBy"></a> systemuser_sourcecontroloperationstatus_StartedBy

One-To-Many Relationship: [systemuser systemuser_sourcecontroloperationstatus_StartedBy](systemuser.md#BKMK_systemuser_sourcecontroloperationstatus_StartedBy)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`startedby`|
|ReferencingEntityNavigationPropertyName|`StartedBy`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.sourcecontroloperationstatus?displayProperty=fullName>
