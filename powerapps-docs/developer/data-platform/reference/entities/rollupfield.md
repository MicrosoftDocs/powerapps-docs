---
title: "Rollup Field (RollupField) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Rollup Field (RollupField) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Rollup Field (RollupField) table/entity reference (Microsoft Dataverse)

Field to be rolled up to calculate the actual and in-progress values against the goal.

## Messages

The following table lists the messages for the Rollup Field (RollupField) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /rollupfields<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /rollupfields(*rollupfieldid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /rollupfields(*rollupfieldid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /rollupfields<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /rollupfields(*rollupfieldid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /rollupfields(*rollupfieldid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Rollup Field (RollupField) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Rollup Field** |
| **DisplayCollectionName** | **Rollup Fields** |
| **SchemaName** | `RollupField` |
| **CollectionSchemaName** | `RollupFields` |
| **EntitySetName** | `rollupfields`|
| **LogicalName** | `rollupfield` |
| **LogicalCollectionName** | `rollupfields` |
| **PrimaryIdAttribute** | `rollupfieldid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [DateAttribute](#BKMK_DateAttribute)
- [EntityForDateAttribute](#BKMK_EntityForDateAttribute)
- [GoalAttribute](#BKMK_GoalAttribute)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsStateParentEntityAttribute](#BKMK_IsStateParentEntityAttribute)
- [MetricId](#BKMK_MetricId)
- [RollupFieldId](#BKMK_RollupFieldId)
- [SourceAttribute](#BKMK_SourceAttribute)
- [SourceEntity](#BKMK_SourceEntity)
- [SourceState](#BKMK_SourceState)
- [SourceStatus](#BKMK_SourceStatus)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_DateAttribute"></a> DateAttribute

|Property|Value|
|---|---|
|Description|**Select a date field for the selected record type, such as Actual Closed Date for the Opportunity record type. A record participates in the goal rollup, if the selected date falls between the start date and the end date for the goal.**|
|DisplayName|**Date Field**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`dateattribute`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_EntityForDateAttribute"></a> EntityForDateAttribute

|Property|Value|
|---|---|
|Description|**Select the record type that contains the date field that will be considered while rolling up data to the goal.**|
|DisplayName|**Record Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entityfordateattribute`|
|RequiredLevel|ApplicationRequired|
|Type|EntityName|

### <a name="BKMK_GoalAttribute"></a> GoalAttribute

|Property|Value|
|---|---|
|Description|**Select a rollup field where the metric rollup data will be displayed in the goal. The options are an integer or money, depending on the Metric Type you chose for the goal metric.**|
|DisplayName|**Rollup Field**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`goalattribute`|
|RequiredLevel|ApplicationRequired|
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

### <a name="BKMK_IsStateParentEntityAttribute"></a> IsStateParentEntityAttribute

|Property|Value|
|---|---|
|Description|**Tells whether the state or status belongs to the parent entity.**|
|DisplayName|**Is State/Status From Parent Entity**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isstateparententityattribute`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`rollupfield_isstatefromparent`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_MetricId"></a> MetricId

|Property|Value|
|---|---|
|Description|**Unique identifier of the goal metric associated with the rollup field.**|
|DisplayName|**Goal Metric**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`metricid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|metric|

### <a name="BKMK_RollupFieldId"></a> RollupFieldId

|Property|Value|
|---|---|
|Description|**Unique identifier of the rollup field.**|
|DisplayName|**Rollup Field**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`rollupfieldid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SourceAttribute"></a> SourceAttribute

|Property|Value|
|---|---|
|Description|**Type the name of the field that the data for the goal rolls up from.**|
|DisplayName|**Source Field**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sourceattribute`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_SourceEntity"></a> SourceEntity

|Property|Value|
|---|---|
|Description|**Type the name of the record type (entity) that the data for the goal must roll up from.**|
|DisplayName|**Source Record Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sourceentity`|
|RequiredLevel|ApplicationRequired|
|Type|EntityName|

### <a name="BKMK_SourceState"></a> SourceState

|Property|Value|
|---|---|
|Description|**Select the state of the records you want to use as the source of the rollup data for the metric.**|
|DisplayName|**Source Record Type State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sourcestate`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_SourceStatus"></a> SourceStatus

|Property|Value|
|---|---|
|Description|**Select the status of the records you want to use as the source of the rollup data for the metric.**|
|DisplayName|**Source Record Type Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sourcestatus`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

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

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Choose the ID of the organization that the record is associated with.**|
|DisplayName|**Organization Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets||

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the rollup field.**|
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

- [lk_rollupfield_createdby](#BKMK_lk_rollupfield_createdby)
- [lk_rollupfield_createdonbehalfby](#BKMK_lk_rollupfield_createdonbehalfby)
- [lk_rollupfield_modifiedby](#BKMK_lk_rollupfield_modifiedby)
- [lk_rollupfield_modifiedonbehalfby](#BKMK_lk_rollupfield_modifiedonbehalfby)
- [metric_rollupfield](#BKMK_metric_rollupfield)

### <a name="BKMK_lk_rollupfield_createdby"></a> lk_rollupfield_createdby

One-To-Many Relationship: [systemuser lk_rollupfield_createdby](systemuser.md#BKMK_lk_rollupfield_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_rollupfield_createdonbehalfby"></a> lk_rollupfield_createdonbehalfby

One-To-Many Relationship: [systemuser lk_rollupfield_createdonbehalfby](systemuser.md#BKMK_lk_rollupfield_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_rollupfield_modifiedby"></a> lk_rollupfield_modifiedby

One-To-Many Relationship: [systemuser lk_rollupfield_modifiedby](systemuser.md#BKMK_lk_rollupfield_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_rollupfield_modifiedonbehalfby"></a> lk_rollupfield_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_rollupfield_modifiedonbehalfby](systemuser.md#BKMK_lk_rollupfield_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_metric_rollupfield"></a> metric_rollupfield

One-To-Many Relationship: [metric metric_rollupfield](metric.md#BKMK_metric_rollupfield)

|Property|Value|
|---|---|
|ReferencedEntity|`metric`|
|ReferencedAttribute|`metricid`|
|ReferencingAttribute|`metricid`|
|ReferencingEntityNavigationPropertyName|`metricid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [rollupfield_AsyncOperations](#BKMK_rollupfield_AsyncOperations)
- [rollupfield_ProcessSessions](#BKMK_rollupfield_ProcessSessions)
- [RollupField_SyncErrors](#BKMK_RollupField_SyncErrors)

### <a name="BKMK_rollupfield_AsyncOperations"></a> rollupfield_AsyncOperations

Many-To-One Relationship: [asyncoperation rollupfield_AsyncOperations](asyncoperation.md#BKMK_rollupfield_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`rollupfield_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_rollupfield_ProcessSessions"></a> rollupfield_ProcessSessions

Many-To-One Relationship: [processsession rollupfield_ProcessSessions](processsession.md#BKMK_rollupfield_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`rollupfield_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_RollupField_SyncErrors"></a> RollupField_SyncErrors

Many-To-One Relationship: [syncerror RollupField_SyncErrors](syncerror.md#BKMK_RollupField_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`RollupField_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.rollupfield?displayProperty=fullName>
