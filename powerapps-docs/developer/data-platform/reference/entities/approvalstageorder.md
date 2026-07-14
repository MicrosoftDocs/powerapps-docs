---
title: "Approval Stage Order (approvalstageorder) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Approval Stage Order (approvalstageorder) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Approval Stage Order (approvalstageorder) table/entity reference (Microsoft Dataverse)

The order of the stages in multi-stage approvals.

## Messages

The following table lists the messages for the Approval Stage Order (approvalstageorder) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /approvalstageorders(*approvalstageorderid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /approvalstageorders<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /approvalstageorders(*approvalstageorderid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /approvalstageorders(*approvalstageorderid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /approvalstageorders<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /approvalstageorders(*approvalstageorderid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /approvalstageorders(*approvalstageorderid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /approvalstageorders(*approvalstageorderid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Approval Stage Order (approvalstageorder) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Approval Stage Order** |
| **DisplayCollectionName** | **Approval Stage Orders** |
| **SchemaName** | `approvalstageorder` |
| **CollectionSchemaName** | `approvalstageorders` |
| **EntitySetName** | `approvalstageorders`|
| **LogicalName** | `approvalstageorder` |
| **LogicalCollectionName** | `approvalstageorders` |
| **PrimaryIdAttribute** | `approvalstageorderid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Approval](#BKMK_Approval)
- [approvalstageorderId](#BKMK_approvalstageorderId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [Name](#BKMK_Name)
- [OrderNumber](#BKMK_OrderNumber)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [StageApproval](#BKMK_StageApproval)
- [StageCondition](#BKMK_StageCondition)
- [StageIntelligent](#BKMK_StageIntelligent)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [Type](#BKMK_Type)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_Approval"></a> Approval

|Property|Value|
|---|---|
|Description|**The linked approval**|
|DisplayName|**Approval**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`approval`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|msdyn_flow_approval|

### <a name="BKMK_approvalstageorderId"></a> approvalstageorderId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Approval Stage Order**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`approvalstageorderid`|
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
|Description|**Name of the stage**|
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
|MaxLength|850|

### <a name="BKMK_OrderNumber"></a> OrderNumber

|Property|Value|
|---|---|
|Description|**The order number of the stage**|
|DisplayName|**Order Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ordernumber`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

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

### <a name="BKMK_StageApproval"></a> StageApproval

|Property|Value|
|---|---|
|Description|**The linked stage approval**|
|DisplayName|**Stage Approval**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`stageapproval`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|approvalstageapproval|

### <a name="BKMK_StageCondition"></a> StageCondition

|Property|Value|
|---|---|
|Description|**The linked condition**|
|DisplayName|**Stage Condition**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`stagecondition`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|approvalstagecondition|

### <a name="BKMK_StageIntelligent"></a> StageIntelligent

|Property|Value|
|---|---|
|Description|**The linked intelligent stage**|
|DisplayName|**Stage Intelligent**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`stageintelligent`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|approvalstageintelligent|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Approval Stage Order**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`approvalstageorder_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 192350001<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Approval Stage Order**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`approvalstageorder_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|
|192350001|Label: **Initialized**<br />State:0<br />TransitionData: None|
|192350002|Label: **Completed**<br />State:1<br />TransitionData: None|
|192350003|Label: **Skipped**<br />State:1<br />TransitionData: None|

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

### <a name="BKMK_Type"></a> Type

|Property|Value|
|---|---|
|Description|**The type of the stage**|
|DisplayName|**Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`type`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`approvalstageorder_type`|

#### Type Choices/Options

|Value|Label|
|---|---|
|192350000|**Approval**|
|192350001|**Condition**|
|192350002|**AI**|

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
|RequiredLevel|SystemRequired|
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

- [approvalstageorder_approval_msdyn_flow_approval](#BKMK_approvalstageorder_approval_msdyn_flow_approval)
- [approvalstageorder_stageapproval_approvalstageapproval](#BKMK_approvalstageorder_stageapproval_approvalstageapproval)
- [approvalstageorder_stagecondition_approvalstagecondition](#BKMK_approvalstageorder_stagecondition_approvalstagecondition)
- [approvalstageorder_stageintelligent_approvalstageintelligent](#BKMK_approvalstageorder_stageintelligent_approvalstageintelligent)
- [business_unit_approvalstageorder](#BKMK_business_unit_approvalstageorder)
- [lk_approvalstageorder_createdby](#BKMK_lk_approvalstageorder_createdby)
- [lk_approvalstageorder_createdonbehalfby](#BKMK_lk_approvalstageorder_createdonbehalfby)
- [lk_approvalstageorder_modifiedby](#BKMK_lk_approvalstageorder_modifiedby)
- [lk_approvalstageorder_modifiedonbehalfby](#BKMK_lk_approvalstageorder_modifiedonbehalfby)
- [owner_approvalstageorder](#BKMK_owner_approvalstageorder)
- [team_approvalstageorder](#BKMK_team_approvalstageorder)
- [user_approvalstageorder](#BKMK_user_approvalstageorder)

### <a name="BKMK_approvalstageorder_approval_msdyn_flow_approval"></a> approvalstageorder_approval_msdyn_flow_approval

One-To-Many Relationship: [msdyn_flow_approval approvalstageorder_approval_msdyn_flow_approval](msdyn_flow_approval.md#BKMK_approvalstageorder_approval_msdyn_flow_approval)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approval`|
|ReferencedAttribute|`msdyn_flow_approvalid`|
|ReferencingAttribute|`approval`|
|ReferencingEntityNavigationPropertyName|`approval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Cascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageorder_stageapproval_approvalstageapproval"></a> approvalstageorder_stageapproval_approvalstageapproval

One-To-Many Relationship: [approvalstageapproval approvalstageorder_stageapproval_approvalstageapproval](approvalstageapproval.md#BKMK_approvalstageorder_stageapproval_approvalstageapproval)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageapproval`|
|ReferencedAttribute|`approvalstageapprovalid`|
|ReferencingAttribute|`stageapproval`|
|ReferencingEntityNavigationPropertyName|`stageapproval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Cascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageorder_stagecondition_approvalstagecondition"></a> approvalstageorder_stagecondition_approvalstagecondition

One-To-Many Relationship: [approvalstagecondition approvalstageorder_stagecondition_approvalstagecondition](approvalstagecondition.md#BKMK_approvalstageorder_stagecondition_approvalstagecondition)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstagecondition`|
|ReferencedAttribute|`approvalstageconditionid`|
|ReferencingAttribute|`stagecondition`|
|ReferencingEntityNavigationPropertyName|`stagecondition`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Cascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageorder_stageintelligent_approvalstageintelligent"></a> approvalstageorder_stageintelligent_approvalstageintelligent

One-To-Many Relationship: [approvalstageintelligent approvalstageorder_stageintelligent_approvalstageintelligent](approvalstageintelligent.md#BKMK_approvalstageorder_stageintelligent_approvalstageintelligent)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageintelligent`|
|ReferencedAttribute|`approvalstageintelligentid`|
|ReferencingAttribute|`stageintelligent`|
|ReferencingEntityNavigationPropertyName|`stageintelligent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Cascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_business_unit_approvalstageorder"></a> business_unit_approvalstageorder

One-To-Many Relationship: [businessunit business_unit_approvalstageorder](businessunit.md#BKMK_business_unit_approvalstageorder)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_approvalstageorder_createdby"></a> lk_approvalstageorder_createdby

One-To-Many Relationship: [systemuser lk_approvalstageorder_createdby](systemuser.md#BKMK_lk_approvalstageorder_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_approvalstageorder_createdonbehalfby"></a> lk_approvalstageorder_createdonbehalfby

One-To-Many Relationship: [systemuser lk_approvalstageorder_createdonbehalfby](systemuser.md#BKMK_lk_approvalstageorder_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_approvalstageorder_modifiedby"></a> lk_approvalstageorder_modifiedby

One-To-Many Relationship: [systemuser lk_approvalstageorder_modifiedby](systemuser.md#BKMK_lk_approvalstageorder_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_approvalstageorder_modifiedonbehalfby"></a> lk_approvalstageorder_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_approvalstageorder_modifiedonbehalfby](systemuser.md#BKMK_lk_approvalstageorder_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_approvalstageorder"></a> owner_approvalstageorder

One-To-Many Relationship: [owner owner_approvalstageorder](owner.md#BKMK_owner_approvalstageorder)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_approvalstageorder"></a> team_approvalstageorder

One-To-Many Relationship: [team team_approvalstageorder](team.md#BKMK_team_approvalstageorder)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_approvalstageorder"></a> user_approvalstageorder

One-To-Many Relationship: [systemuser user_approvalstageorder](systemuser.md#BKMK_user_approvalstageorder)

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

- [approvalstageorder_AsyncOperations](#BKMK_approvalstageorder_AsyncOperations)
- [approvalstageorder_BulkDeleteFailures](#BKMK_approvalstageorder_BulkDeleteFailures)
- [approvalstageorder_DuplicateBaseRecord](#BKMK_approvalstageorder_DuplicateBaseRecord)
- [approvalstageorder_DuplicateMatchingRecord](#BKMK_approvalstageorder_DuplicateMatchingRecord)
- [approvalstageorder_MailboxTrackingFolders](#BKMK_approvalstageorder_MailboxTrackingFolders)
- [approvalstageorder_PrincipalObjectAttributeAccesses](#BKMK_approvalstageorder_PrincipalObjectAttributeAccesses)
- [approvalstageorder_ProcessSession](#BKMK_approvalstageorder_ProcessSession)
- [approvalstageorder_SyncErrors](#BKMK_approvalstageorder_SyncErrors)
- [msdyn_flow_approval_currentstage_approvalstageorder](#BKMK_msdyn_flow_approval_currentstage_approvalstageorder)

### <a name="BKMK_approvalstageorder_AsyncOperations"></a> approvalstageorder_AsyncOperations

Many-To-One Relationship: [asyncoperation approvalstageorder_AsyncOperations](asyncoperation.md#BKMK_approvalstageorder_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`approvalstageorder_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_approvalstageorder_BulkDeleteFailures"></a> approvalstageorder_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure approvalstageorder_BulkDeleteFailures](bulkdeletefailure.md#BKMK_approvalstageorder_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`approvalstageorder_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_approvalstageorder_DuplicateBaseRecord"></a> approvalstageorder_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord approvalstageorder_DuplicateBaseRecord](duplicaterecord.md#BKMK_approvalstageorder_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`approvalstageorder_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_approvalstageorder_DuplicateMatchingRecord"></a> approvalstageorder_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord approvalstageorder_DuplicateMatchingRecord](duplicaterecord.md#BKMK_approvalstageorder_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`approvalstageorder_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_approvalstageorder_MailboxTrackingFolders"></a> approvalstageorder_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder approvalstageorder_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_approvalstageorder_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`approvalstageorder_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_approvalstageorder_PrincipalObjectAttributeAccesses"></a> approvalstageorder_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess approvalstageorder_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_approvalstageorder_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`approvalstageorder_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_approvalstageorder_ProcessSession"></a> approvalstageorder_ProcessSession

Many-To-One Relationship: [processsession approvalstageorder_ProcessSession](processsession.md#BKMK_approvalstageorder_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`approvalstageorder_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_approvalstageorder_SyncErrors"></a> approvalstageorder_SyncErrors

Many-To-One Relationship: [syncerror approvalstageorder_SyncErrors](syncerror.md#BKMK_approvalstageorder_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`approvalstageorder_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_approval_currentstage_approvalstageorder"></a> msdyn_flow_approval_currentstage_approvalstageorder

Many-To-One Relationship: [msdyn_flow_approval msdyn_flow_approval_currentstage_approvalstageorder](msdyn_flow_approval.md#BKMK_msdyn_flow_approval_currentstage_approvalstageorder)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_approval`|
|ReferencingAttribute|`currentstage`|
|ReferencedEntityNavigationPropertyName|`msdyn_flow_approval_currentstage_approvalstageorder`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.approvalstageorder?displayProperty=fullName>
