---
title: "Flow Capacity Assignment (flowcapacityassignment) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Flow Capacity Assignment (flowcapacityassignment) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Flow Capacity Assignment (flowcapacityassignment) table/entity reference (Microsoft Dataverse)

Capacity assignment for usage in Power Automate

## Messages

The following table lists the messages for the Flow Capacity Assignment (flowcapacityassignment) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /flowcapacityassignments(*flowcapacityassignmentid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /flowcapacityassignments<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /flowcapacityassignments(*flowcapacityassignmentid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /flowcapacityassignments(*flowcapacityassignmentid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /flowcapacityassignments<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /flowcapacityassignments(*flowcapacityassignmentid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /flowcapacityassignments(*flowcapacityassignmentid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /flowcapacityassignments(*flowcapacityassignmentid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Flow Capacity Assignment (flowcapacityassignment) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Flow Capacity Assignment** |
| **DisplayCollectionName** | **Flow Capacity Assignments** |
| **SchemaName** | `flowcapacityassignment` |
| **CollectionSchemaName** | `flowcapacityassignments` |
| **EntitySetName** | `flowcapacityassignments`|
| **LogicalName** | `flowcapacityassignment` |
| **LogicalCollectionName** | `flowcapacityassignments` |
| **PrimaryIdAttribute** | `flowcapacityassignmentid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AllocationOrigin](#BKMK_AllocationOrigin)
- [AllowAutoAllocation](#BKMK_AllowAutoAllocation)
- [CapacityOverage](#BKMK_CapacityOverage)
- [CapacitySource](#BKMK_CapacitySource)
- [CapacityType](#BKMK_CapacityType)
- [Count](#BKMK_Count)
- [flowcapacityassignmentId](#BKMK_flowcapacityassignmentId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [regarding](#BKMK_regarding)
- [regardingIdType](#BKMK_regardingIdType)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_AllocationOrigin"></a> AllocationOrigin

|Property|Value|
|---|---|
|Description|**Origin of the capacity assigned to a target entity.**|
|DisplayName|**Allocation Origin**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`allocationorigin`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`flowcapacityassignment_allocationorigin`|

#### AllocationOrigin Choices/Options

|Value|Label|
|---|---|
|0|**User**|
|1|**System**|

### <a name="BKMK_AllowAutoAllocation"></a> AllowAutoAllocation

|Property|Value|
|---|---|
|Description|**Indicates whether the capacity auto-allocation feature is allowed for the target record. Default value is Yes.**|
|DisplayName|**Allow capacity auto-allocation for the target record.**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`allowautoallocation`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`flowcapacityassignment_allowautoallocation`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_CapacityOverage"></a> CapacityOverage

|Property|Value|
|---|---|
|Description|**Number of missing add-ons to be compliant**|
|DisplayName|**CapacityOverage**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`capacityoverage`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_CapacitySource"></a> CapacitySource

|Property|Value|
|---|---|
|Description|**Source of the capacity assigned to a target entity.**|
|DisplayName|**CapacitySource**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`capacitysource`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`flowcapacityassignment_capacitysource`|

#### CapacitySource Choices/Options

|Value|Label|
|---|---|
|0|**AddOn**|
|1|**ViralAdoption**|
|2|**UserTrial**|
|3|**FailOpen**|

### <a name="BKMK_CapacityType"></a> CapacityType

|Property|Value|
|---|---|
|Description|**Type of the capacity assigned to a target entity**|
|DisplayName|**CapacityType**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`capacitytype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`flowcapacityassignment_capacitytype`|

#### CapacityType Choices/Options

|Value|Label|
|---|---|
|0|**PowerAutomateHostedRpa**|
|1|**PowerAutomatePerProcess**|
|2|**PowerAutomateProcessMining**|

### <a name="BKMK_Count"></a> Count

|Property|Value|
|---|---|
|Description|**Number of units assigned**|
|DisplayName|**Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`count`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_flowcapacityassignmentId"></a> flowcapacityassignmentId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Flow Capacity Assignment**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`flowcapacityassignmentid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description||
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

### <a name="BKMK_regarding"></a> regarding

|Property|Value|
|---|---|
|Description|**The target of the capacity assignment**|
|DisplayName|**Assignment target**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`regarding`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|flowmachine, flowmachinegroup, msdyn_pminferredtask, workflow|

### <a name="BKMK_regardingIdType"></a> regardingIdType

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingidtype`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Flow Capacity Assignment**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`flowcapacityassignment_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Flow Capacity Assignment**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`flowcapacityassignment_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

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
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
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

- [business_unit_flowcapacityassignment](#BKMK_business_unit_flowcapacityassignment)
- [flowcapacityassignment_flowmachine](#BKMK_flowcapacityassignment_flowmachine)
- [flowcapacityassignment_flowmachinegroup](#BKMK_flowcapacityassignment_flowmachinegroup)
- [flowcapacityassignment_msdyn_pminferredtask](#BKMK_flowcapacityassignment_msdyn_pminferredtask)
- [flowcapacityassignment_workflow](#BKMK_flowcapacityassignment_workflow)
- [lk_flowcapacityassignment_createdby](#BKMK_lk_flowcapacityassignment_createdby)
- [lk_flowcapacityassignment_createdonbehalfby](#BKMK_lk_flowcapacityassignment_createdonbehalfby)
- [lk_flowcapacityassignment_modifiedby](#BKMK_lk_flowcapacityassignment_modifiedby)
- [lk_flowcapacityassignment_modifiedonbehalfby](#BKMK_lk_flowcapacityassignment_modifiedonbehalfby)
- [owner_flowcapacityassignment](#BKMK_owner_flowcapacityassignment)
- [team_flowcapacityassignment](#BKMK_team_flowcapacityassignment)
- [user_flowcapacityassignment](#BKMK_user_flowcapacityassignment)

### <a name="BKMK_business_unit_flowcapacityassignment"></a> business_unit_flowcapacityassignment

One-To-Many Relationship: [businessunit business_unit_flowcapacityassignment](businessunit.md#BKMK_business_unit_flowcapacityassignment)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowcapacityassignment_flowmachine"></a> flowcapacityassignment_flowmachine

One-To-Many Relationship: [flowmachine flowcapacityassignment_flowmachine](flowmachine.md#BKMK_flowcapacityassignment_flowmachine)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachine`|
|ReferencedAttribute|`flowmachineid`|
|ReferencingAttribute|`regarding`|
|ReferencingEntityNavigationPropertyName|`regarding_flowmachine`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Cascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_flowcapacityassignment_flowmachinegroup"></a> flowcapacityassignment_flowmachinegroup

One-To-Many Relationship: [flowmachinegroup flowcapacityassignment_flowmachinegroup](flowmachinegroup.md#BKMK_flowcapacityassignment_flowmachinegroup)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinegroup`|
|ReferencedAttribute|`flowmachinegroupid`|
|ReferencingAttribute|`regarding`|
|ReferencingEntityNavigationPropertyName|`regarding_flowmachinegroup`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Cascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_flowcapacityassignment_msdyn_pminferredtask"></a> flowcapacityassignment_msdyn_pminferredtask

One-To-Many Relationship: [msdyn_pminferredtask flowcapacityassignment_msdyn_pminferredtask](msdyn_pminferredtask.md#BKMK_flowcapacityassignment_msdyn_pminferredtask)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pminferredtask`|
|ReferencedAttribute|`msdyn_pminferredtaskid`|
|ReferencingAttribute|`regarding`|
|ReferencingEntityNavigationPropertyName|`regarding_msdyn_pminferredtask`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Cascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_flowcapacityassignment_workflow"></a> flowcapacityassignment_workflow

One-To-Many Relationship: [workflow flowcapacityassignment_workflow](workflow.md#BKMK_flowcapacityassignment_workflow)

|Property|Value|
|---|---|
|ReferencedEntity|`workflow`|
|ReferencedAttribute|`workflowid`|
|ReferencingAttribute|`regarding`|
|ReferencingEntityNavigationPropertyName|`regarding_workflow`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Cascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_lk_flowcapacityassignment_createdby"></a> lk_flowcapacityassignment_createdby

One-To-Many Relationship: [systemuser lk_flowcapacityassignment_createdby](systemuser.md#BKMK_lk_flowcapacityassignment_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowcapacityassignment_createdonbehalfby"></a> lk_flowcapacityassignment_createdonbehalfby

One-To-Many Relationship: [systemuser lk_flowcapacityassignment_createdonbehalfby](systemuser.md#BKMK_lk_flowcapacityassignment_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowcapacityassignment_modifiedby"></a> lk_flowcapacityassignment_modifiedby

One-To-Many Relationship: [systemuser lk_flowcapacityassignment_modifiedby](systemuser.md#BKMK_lk_flowcapacityassignment_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowcapacityassignment_modifiedonbehalfby"></a> lk_flowcapacityassignment_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_flowcapacityassignment_modifiedonbehalfby](systemuser.md#BKMK_lk_flowcapacityassignment_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_flowcapacityassignment"></a> owner_flowcapacityassignment

One-To-Many Relationship: [owner owner_flowcapacityassignment](owner.md#BKMK_owner_flowcapacityassignment)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_flowcapacityassignment"></a> team_flowcapacityassignment

One-To-Many Relationship: [team team_flowcapacityassignment](team.md#BKMK_team_flowcapacityassignment)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_flowcapacityassignment"></a> user_flowcapacityassignment

One-To-Many Relationship: [systemuser user_flowcapacityassignment](systemuser.md#BKMK_user_flowcapacityassignment)

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

- [flowcapacityassignment_AsyncOperations](#BKMK_flowcapacityassignment_AsyncOperations)
- [flowcapacityassignment_BulkDeleteFailures](#BKMK_flowcapacityassignment_BulkDeleteFailures)
- [flowcapacityassignment_MailboxTrackingFolders](#BKMK_flowcapacityassignment_MailboxTrackingFolders)
- [flowcapacityassignment_PrincipalObjectAttributeAccesses](#BKMK_flowcapacityassignment_PrincipalObjectAttributeAccesses)
- [flowcapacityassignment_ProcessSession](#BKMK_flowcapacityassignment_ProcessSession)
- [flowcapacityassignment_SyncErrors](#BKMK_flowcapacityassignment_SyncErrors)

### <a name="BKMK_flowcapacityassignment_AsyncOperations"></a> flowcapacityassignment_AsyncOperations

Many-To-One Relationship: [asyncoperation flowcapacityassignment_AsyncOperations](asyncoperation.md#BKMK_flowcapacityassignment_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowcapacityassignment_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowcapacityassignment_BulkDeleteFailures"></a> flowcapacityassignment_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure flowcapacityassignment_BulkDeleteFailures](bulkdeletefailure.md#BKMK_flowcapacityassignment_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowcapacityassignment_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowcapacityassignment_MailboxTrackingFolders"></a> flowcapacityassignment_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder flowcapacityassignment_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_flowcapacityassignment_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowcapacityassignment_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowcapacityassignment_PrincipalObjectAttributeAccesses"></a> flowcapacityassignment_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess flowcapacityassignment_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_flowcapacityassignment_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`flowcapacityassignment_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowcapacityassignment_ProcessSession"></a> flowcapacityassignment_ProcessSession

Many-To-One Relationship: [processsession flowcapacityassignment_ProcessSession](processsession.md#BKMK_flowcapacityassignment_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowcapacityassignment_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowcapacityassignment_SyncErrors"></a> flowcapacityassignment_SyncErrors

Many-To-One Relationship: [syncerror flowcapacityassignment_SyncErrors](syncerror.md#BKMK_flowcapacityassignment_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowcapacityassignment_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.flowcapacityassignment?displayProperty=fullName>
