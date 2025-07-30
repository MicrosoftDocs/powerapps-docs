---
title: "Bulk Delete Operation (BulkDeleteOperation) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Bulk Delete Operation (BulkDeleteOperation) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Bulk Delete Operation (BulkDeleteOperation) table/entity reference (Microsoft Dataverse)

User-submitted bulk deletion job.

## Messages

The following table lists the messages for the Bulk Delete Operation (BulkDeleteOperation) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Delete`<br />Event: False |`DELETE` /bulkdeleteoperations(*bulkdeleteoperationid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /bulkdeleteoperations(*bulkdeleteoperationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /bulkdeleteoperations<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Bulk Delete Operation (BulkDeleteOperation) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Bulk Delete Operation** |
| **DisplayCollectionName** | **Bulk Delete Operations** |
| **SchemaName** | `BulkDeleteOperation` |
| **CollectionSchemaName** | `BulkDeleteOperations` |
| **EntitySetName** | `bulkdeleteoperations`|
| **LogicalName** | `bulkdeleteoperation` |
| **LogicalCollectionName** | `bulkdeleteoperations` |
| **PrimaryIdAttribute** | `bulkdeleteoperationid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
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
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`utcconversiontimezonecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [AsyncOperationId](#BKMK_AsyncOperationId)
- [BulkDeleteOperationId](#BKMK_BulkDeleteOperationId)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [FailureCount](#BKMK_FailureCount)
- [IsRecurring](#BKMK_IsRecurring)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [Name](#BKMK_Name)
- [NextRun](#BKMK_NextRun)
- [OrderedQuerySetXml](#BKMK_OrderedQuerySetXml)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningUser](#BKMK_OwningUser)
- [ProcessingQEIndex](#BKMK_ProcessingQEIndex)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [SuccessCount](#BKMK_SuccessCount)

### <a name="BKMK_AsyncOperationId"></a> AsyncOperationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the system job that created this record**|
|DisplayName|**System Job**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`asyncoperationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|asyncoperation|

### <a name="BKMK_BulkDeleteOperationId"></a> BulkDeleteOperationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the bulk deletion job.**|
|DisplayName|**Bulk Deletion Job**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`bulkdeleteoperationid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the bulk deletion job.**|
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
|Description|**Date and time when the bulk deletion job was created.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who created the bulkdeleteoperation.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_FailureCount"></a> FailureCount

|Property|Value|
|---|---|
|Description|**Number of records that could not be deleted by the bulk deletion job.**|
|DisplayName|**Failures**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`failurecount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

### <a name="BKMK_IsRecurring"></a> IsRecurring

|Property|Value|
|---|---|
|Description|**Information about if recurrence is defined for the bulk deletion job.**|
|DisplayName|**Is Recurring**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isrecurring`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`bulkdeleteoperation_isrecurring`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the bulk deletion job.**|
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
|Description|**Date and time when the bulk deletion job record was last modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the bulkdeleteoperation.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the bulk deletion job.**|
|DisplayName|**System Job Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_NextRun"></a> NextRun

|Property|Value|
|---|---|
|Description|**Next scheduled time for the bulk deletion job to run.**|
|DisplayName|**Next Run**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`nextrun`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_OrderedQuerySetXml"></a> OrderedQuerySetXml

|Property|Value|
|---|---|
|Description|**Fetch XML of the ordered query set.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`orderedquerysetxml`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user or team who owns the bulk delete operation.**|
|DisplayName|**Owner**|
|IsValidForForm|False|
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
|Description|**Business unit that owns the bulk deletion job.**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Business user what owns the bulk delete operation.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ProcessingQEIndex"></a> ProcessingQEIndex

|Property|Value|
|---|---|
|Description|**Index of the ordered query expression that defines the deletion set.**|
|DisplayName|**Query Index**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processingqeindex`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Status of the bulk deletion job.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`bulkdeleteoperation_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Ready**<br />DefaultStatus: 1<br />InvariantName: `Ready`|
|1|Label: **Suspended**<br />DefaultStatus: 2<br />InvariantName: `Suspended`|
|2|Label: **Locked**<br />DefaultStatus: 2<br />InvariantName: `Locked`|
|3|Label: **Completed**<br />DefaultStatus: 2<br />InvariantName: `Completed`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Reason for the status of the bulk deletion job.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`bulkdeleteoperation_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Waiting For Resources**<br />State:0<br />TransitionData: None|
|10|Label: **Waiting**<br />State:1<br />TransitionData: None|
|11|Label: **Retrying**<br />State:1<br />TransitionData: None|
|12|Label: **Paused**<br />State:1<br />TransitionData: None|
|20|Label: **In Progress**<br />State:2<br />TransitionData: None|
|21|Label: **Pausing**<br />State:2<br />TransitionData: None|
|22|Label: **Canceling**<br />State:2<br />TransitionData: None|
|30|Label: **Succeeded**<br />State:3<br />TransitionData: None|
|31|Label: **Failed**<br />State:3<br />TransitionData: None|
|32|Label: **Canceled**<br />State:3<br />TransitionData: None|

### <a name="BKMK_SuccessCount"></a> SuccessCount

|Property|Value|
|---|---|
|Description|**Number of records deleted by the bulk deletion job.**|
|DisplayName|**Deleted**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`successcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [AsyncOperation_BulkDeleteOperation](#BKMK_AsyncOperation_BulkDeleteOperation)
- [BulkDeleteOperation_BusinessUnit](#BKMK_BulkDeleteOperation_BusinessUnit)
- [lk_bulkdeleteoperation_createdonbehalfby](#BKMK_lk_bulkdeleteoperation_createdonbehalfby)
- [lk_bulkdeleteoperation_modifiedonbehalfby](#BKMK_lk_bulkdeleteoperation_modifiedonbehalfby)
- [lk_bulkdeleteoperationbase_createdby](#BKMK_lk_bulkdeleteoperationbase_createdby)
- [lk_bulkdeleteoperationbase_modifiedby](#BKMK_lk_bulkdeleteoperationbase_modifiedby)

### <a name="BKMK_AsyncOperation_BulkDeleteOperation"></a> AsyncOperation_BulkDeleteOperation

One-To-Many Relationship: [asyncoperation AsyncOperation_BulkDeleteOperation](asyncoperation.md#BKMK_AsyncOperation_BulkDeleteOperation)

|Property|Value|
|---|---|
|ReferencedEntity|`asyncoperation`|
|ReferencedAttribute|`asyncoperationid`|
|ReferencingAttribute|`asyncoperationid`|
|ReferencingEntityNavigationPropertyName|`asyncoperationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_BulkDeleteOperation_BusinessUnit"></a> BulkDeleteOperation_BusinessUnit

One-To-Many Relationship: [businessunit BulkDeleteOperation_BusinessUnit](businessunit.md#BKMK_BulkDeleteOperation_BusinessUnit)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_bulkdeleteoperation_createdonbehalfby"></a> lk_bulkdeleteoperation_createdonbehalfby

One-To-Many Relationship: [systemuser lk_bulkdeleteoperation_createdonbehalfby](systemuser.md#BKMK_lk_bulkdeleteoperation_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_bulkdeleteoperation_modifiedonbehalfby"></a> lk_bulkdeleteoperation_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_bulkdeleteoperation_modifiedonbehalfby](systemuser.md#BKMK_lk_bulkdeleteoperation_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_bulkdeleteoperationbase_createdby"></a> lk_bulkdeleteoperationbase_createdby

One-To-Many Relationship: [systemuser lk_bulkdeleteoperationbase_createdby](systemuser.md#BKMK_lk_bulkdeleteoperationbase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_bulkdeleteoperationbase_modifiedby"></a> lk_bulkdeleteoperationbase_modifiedby

One-To-Many Relationship: [systemuser lk_bulkdeleteoperationbase_modifiedby](systemuser.md#BKMK_lk_bulkdeleteoperationbase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_BulkDeleteOperation_BulkDeleteFailure"></a> BulkDeleteOperation_BulkDeleteFailure

Many-To-One Relationship: [bulkdeletefailure BulkDeleteOperation_BulkDeleteFailure](bulkdeletefailure.md#BKMK_BulkDeleteOperation_BulkDeleteFailure)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`bulkdeleteoperationid`|
|ReferencedEntityNavigationPropertyName|`BulkDeleteOperation_BulkDeleteFailure`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.bulkdeleteoperation?displayProperty=fullName>
