---
title: "Background Operation (backgroundoperation) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Background Operation (backgroundoperation) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Background Operation (backgroundoperation) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Background Operation (backgroundoperation) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /backgroundoperations<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /backgroundoperations(*backgroundoperationid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `DeleteMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.DeleteMultiple?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /backgroundoperations(*backgroundoperationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /backgroundoperations<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /backgroundoperations(*backgroundoperationid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: True |`PATCH` /backgroundoperations(*backgroundoperationid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Background Operation (backgroundoperation) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Background Operation** |
| **DisplayCollectionName** | **Background Operations** |
| **SchemaName** | `backgroundoperation` |
| **CollectionSchemaName** | `backgroundoperations` |
| **EntitySetName** | `backgroundoperations`|
| **LogicalName** | `backgroundoperation` |
| **LogicalCollectionName** | `backgroundoperations` |
| **PrimaryIdAttribute** | `backgroundoperationid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Elastic` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [backgroundoperationId](#BKMK_backgroundoperationId)
- [DisplayName](#BKMK_DisplayName)
- [EndTime](#BKMK_EndTime)
- [ErrorCode](#BKMK_ErrorCode)
- [ErrorMessage](#BKMK_ErrorMessage)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [InputParameters](#BKMK_InputParameters)
- [Name](#BKMK_Name)
- [OutputParameters](#BKMK_OutputParameters)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PartitionId](#BKMK_PartitionId)
- [Priority](#BKMK_Priority)
- [RetryCount](#BKMK_RetryCount)
- [RunAs](#BKMK_RunAs)
- [StartTime](#BKMK_StartTime)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [TTLInSeconds](#BKMK_TTLInSeconds)

### <a name="BKMK_backgroundoperationId"></a> backgroundoperationId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Background Operation**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`backgroundoperationid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_DisplayName"></a> DisplayName

|Property|Value|
|---|---|
|Description|**The is display name of background operation.**|
|DisplayName|**DisplayName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`displayname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|512|

### <a name="BKMK_EndTime"></a> EndTime

|Property|Value|
|---|---|
|Description|**The date time when background operation finished execution.**|
|DisplayName|**End Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`endtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_ErrorCode"></a> ErrorCode

|Property|Value|
|---|---|
|Description|**The error code of error for background operation in case of failure.**|
|DisplayName|**Error Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`errorcode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_ErrorMessage"></a> ErrorMessage

|Property|Value|
|---|---|
|Description|**The error message of error for background operation in case of failure.**|
|DisplayName|**Error Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`errormessage`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
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

### <a name="BKMK_InputParameters"></a> InputParameters

|Property|Value|
|---|---|
|Description|**The input parameters that were supplied to start background operation.**|
|DisplayName|**Input Parameters**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`inputparameters`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**The name of the background operation.**|
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
|MaxLength|512|

### <a name="BKMK_OutputParameters"></a> OutputParameters

|Property|Value|
|---|---|
|Description|**The response of background operation.**|
|DisplayName|**Output Parameters**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`outputparameters`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

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

### <a name="BKMK_Priority"></a> Priority

|Property|Value|
|---|---|
|Description|**The priority of background operation execution.**|
|DisplayName|**Priority**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`priority`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|10|
|MinValue|0|

### <a name="BKMK_RetryCount"></a> RetryCount

|Property|Value|
|---|---|
|Description|**The number of times background operation was retried.**|
|DisplayName|**Retry Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`retrycount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_RunAs"></a> RunAs

|Property|Value|
|---|---|
|Description|**The identity of user which was used to execute background operation.**|
|DisplayName|**Run As**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`runas`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|40|

### <a name="BKMK_StartTime"></a> StartTime

|Property|Value|
|---|---|
|Description|**The date time when background operation started execution.**|
|DisplayName|**Start Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`starttime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**The status of background operation.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`backgroundoperationstatecode`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`backgroundoperation_statecode`|

#### StateCode Choices/Options

|Value|Label|
|---|---|
|0|**Ready**|
|2|**Locked**|
|3|**Completed**|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**The status reason for background operation.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`backgroundoperationstatuscode`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`backgroundoperation_statuscode`|

#### StatusCode Choices/Options

|Value|Label|
|---|---|
|0|**Waiting For Resources**|
|20|**In Progress**|
|22|**Canceling**|
|30|**Succeeded**|
|31|**Failed**|
|32|**Canceled**|

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

- [lk_backgroundoperation_createdby](#BKMK_lk_backgroundoperation_createdby)
- [lk_backgroundoperation_createdonbehalfby](#BKMK_lk_backgroundoperation_createdonbehalfby)
- [lk_backgroundoperation_modifiedby](#BKMK_lk_backgroundoperation_modifiedby)
- [lk_backgroundoperation_modifiedonbehalfby](#BKMK_lk_backgroundoperation_modifiedonbehalfby)

### <a name="BKMK_lk_backgroundoperation_createdby"></a> lk_backgroundoperation_createdby

One-To-Many Relationship: [systemuser lk_backgroundoperation_createdby](systemuser.md#BKMK_lk_backgroundoperation_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_backgroundoperation_createdonbehalfby"></a> lk_backgroundoperation_createdonbehalfby

One-To-Many Relationship: [systemuser lk_backgroundoperation_createdonbehalfby](systemuser.md#BKMK_lk_backgroundoperation_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_backgroundoperation_modifiedby"></a> lk_backgroundoperation_modifiedby

One-To-Many Relationship: [systemuser lk_backgroundoperation_modifiedby](systemuser.md#BKMK_lk_backgroundoperation_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_backgroundoperation_modifiedonbehalfby"></a> lk_backgroundoperation_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_backgroundoperation_modifiedonbehalfby](systemuser.md#BKMK_lk_backgroundoperation_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.backgroundoperation?displayProperty=fullName>
