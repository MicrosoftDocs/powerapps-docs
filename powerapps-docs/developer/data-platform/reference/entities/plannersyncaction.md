---
title: "Planner Sync Action (PlannerSyncAction) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Planner Sync Action (PlannerSyncAction) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Planner Sync Action (PlannerSyncAction) table/entity reference (Microsoft Dataverse)

The Planner Sync Action to be executed.

## Messages

The following table lists the messages for the Planner Sync Action (PlannerSyncAction) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /plannersyncactions(*plannersyncactionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /plannersyncactions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /plannersyncactions(*plannersyncactionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /plannersyncactions(*plannersyncactionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /plannersyncactions<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /plannersyncactions(*plannersyncactionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /plannersyncactions(*plannersyncactionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /plannersyncactions(*plannersyncactionid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Planner Sync Action (PlannerSyncAction) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Planner Sync Action** |
| **DisplayCollectionName** | **Planner Sync Actions** |
| **SchemaName** | `PlannerSyncAction` |
| **CollectionSchemaName** | `PlannerSyncActions` |
| **EntitySetName** | `plannersyncactions`|
| **LogicalName** | `plannersyncaction` |
| **LogicalCollectionName** | `plannersyncactions` |
| **PrimaryIdAttribute** | `plannersyncactionid` |
| **PrimaryNameAttribute** |`title` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Assignments](#BKMK_Assignments)
- [DueDateTime](#BKMK_DueDateTime)
- [ExternalBucketId](#BKMK_ExternalBucketId)
- [ExternalReferences](#BKMK_ExternalReferences)
- [GroupId](#BKMK_GroupId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [LastAttemptedOn](#BKMK_LastAttemptedOn)
- [LastSyncError](#BKMK_LastSyncError)
- [Notes](#BKMK_Notes)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [PendingAttempts](#BKMK_PendingAttempts)
- [PercentComplete](#BKMK_PercentComplete)
- [PlannerBusinessScenarioId](#BKMK_PlannerBusinessScenarioId)
- [PlannerSyncActionId](#BKMK_PlannerSyncActionId)
- [Priority](#BKMK_Priority)
- [QueuedOn](#BKMK_QueuedOn)
- [SourceRecordEntityLogicalName](#BKMK_SourceRecordEntityLogicalName)
- [SourceRecordId](#BKMK_SourceRecordId)
- [StartDateTime](#BKMK_StartDateTime)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [Title](#BKMK_Title)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_Assignments"></a> Assignments

|Property|Value|
|---|---|
|Description||
|DisplayName|**Assignments**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`assignments`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_DueDateTime"></a> DueDateTime

|Property|Value|
|---|---|
|Description|**Date and time when the planner task is due.**|
|DisplayName|**Due Date Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`duedatetime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|TimeZoneIndependent|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_ExternalBucketId"></a> ExternalBucketId

|Property|Value|
|---|---|
|Description||
|DisplayName|**External Bucket Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`externalbucketid`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ExternalReferences"></a> ExternalReferences

|Property|Value|
|---|---|
|Description||
|DisplayName|**External References**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`externalreferences`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_GroupId"></a> GroupId

|Property|Value|
|---|---|
|Description||
|DisplayName|**Group Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`groupid`|
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

### <a name="BKMK_LastAttemptedOn"></a> LastAttemptedOn

|Property|Value|
|---|---|
|Description|**For internal use only. Date and time when the action was last attempted.**|
|DisplayName|**Last Attempted On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastattemptedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|TimeZoneIndependent|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_LastSyncError"></a> LastSyncError

|Property|Value|
|---|---|
|Description||
|DisplayName|**Last Sync Error**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastsyncerror`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_Notes"></a> Notes

|Property|Value|
|---|---|
|Description||
|DisplayName|**Notes**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`notes`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

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

### <a name="BKMK_PendingAttempts"></a> PendingAttempts

|Property|Value|
|---|---|
|Description|**The attempts available for processing the planner sync action.**|
|DisplayName|**Pending Attempts**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`pendingattempts`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|5|
|MinValue|0|

### <a name="BKMK_PercentComplete"></a> PercentComplete

|Property|Value|
|---|---|
|Description|**The percentage of completion for the planner task.**|
|DisplayName|**Percent Complete**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`percentcomplete`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|100|
|MinValue|0|

### <a name="BKMK_PlannerBusinessScenarioId"></a> PlannerBusinessScenarioId

|Property|Value|
|---|---|
|Description|**Id of the Business Scenario in Planner.**|
|DisplayName|**Planner Business Scenario Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`plannerbusinessscenarioid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|plannerbusinessscenario|

### <a name="BKMK_PlannerSyncActionId"></a> PlannerSyncActionId

|Property|Value|
|---|---|
|Description|**Planner Sync Action Id**|
|DisplayName|**Planner Sync Action Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`plannersyncactionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Priority"></a> Priority

|Property|Value|
|---|---|
|Description|**The priority of the planner task.**|
|DisplayName|**Priority**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`priority`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|10|
|MinValue|0|

### <a name="BKMK_QueuedOn"></a> QueuedOn

|Property|Value|
|---|---|
|Description|**For internal use only. Date and time when the action was queued.**|
|DisplayName|**Queued On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`queuedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|TimeZoneIndependent|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_SourceRecordEntityLogicalName"></a> SourceRecordEntityLogicalName

|Property|Value|
|---|---|
|Description||
|DisplayName|**Source Record Entity Logical Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sourcerecordentitylogicalname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_SourceRecordId"></a> SourceRecordId

|Property|Value|
|---|---|
|Description||
|DisplayName|**Source Record Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sourcerecordid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_StartDateTime"></a> StartDateTime

|Property|Value|
|---|---|
|Description|**Date and time when the planner task was started.**|
|DisplayName|**Start Date Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`startdatetime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|TimeZoneIndependent|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Planner Sync Action**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`plannersyncaction_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Planner Sync Action**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`plannersyncaction_statuscode`|

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

### <a name="BKMK_Title"></a> Title

|Property|Value|
|---|---|
|Description||
|DisplayName|**Title**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`title`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

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

- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)

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

- [business_unit_plannersyncaction](#BKMK_business_unit_plannersyncaction)
- [owner_plannersyncaction](#BKMK_owner_plannersyncaction)
- [plannerbusinessscenario_plannersyncaction_plannerbusinessscenarioid](#BKMK_plannerbusinessscenario_plannersyncaction_plannerbusinessscenarioid)
- [team_plannersyncaction](#BKMK_team_plannersyncaction)
- [user_plannersyncaction](#BKMK_user_plannersyncaction)

### <a name="BKMK_business_unit_plannersyncaction"></a> business_unit_plannersyncaction

One-To-Many Relationship: [businessunit business_unit_plannersyncaction](businessunit.md#BKMK_business_unit_plannersyncaction)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_plannersyncaction"></a> owner_plannersyncaction

One-To-Many Relationship: [owner owner_plannersyncaction](owner.md#BKMK_owner_plannersyncaction)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plannerbusinessscenario_plannersyncaction_plannerbusinessscenarioid"></a> plannerbusinessscenario_plannersyncaction_plannerbusinessscenarioid

One-To-Many Relationship: [plannerbusinessscenario plannerbusinessscenario_plannersyncaction_plannerbusinessscenarioid](plannerbusinessscenario.md#BKMK_plannerbusinessscenario_plannersyncaction_plannerbusinessscenarioid)

|Property|Value|
|---|---|
|ReferencedEntity|`plannerbusinessscenario`|
|ReferencedAttribute|`plannerbusinessscenarioid`|
|ReferencingAttribute|`plannerbusinessscenarioid`|
|ReferencingEntityNavigationPropertyName|`plannerbusinessscenarioid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_plannersyncaction"></a> team_plannersyncaction

One-To-Many Relationship: [team team_plannersyncaction](team.md#BKMK_team_plannersyncaction)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_plannersyncaction"></a> user_plannersyncaction

One-To-Many Relationship: [systemuser user_plannersyncaction](systemuser.md#BKMK_user_plannersyncaction)

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

- [plannersyncaction_AsyncOperations](#BKMK_plannersyncaction_AsyncOperations)
- [plannersyncaction_BulkDeleteFailures](#BKMK_plannersyncaction_BulkDeleteFailures)
- [plannersyncaction_MailboxTrackingFolders](#BKMK_plannersyncaction_MailboxTrackingFolders)
- [plannersyncaction_PrincipalObjectAttributeAccesses](#BKMK_plannersyncaction_PrincipalObjectAttributeAccesses)
- [plannersyncaction_ProcessSession](#BKMK_plannersyncaction_ProcessSession)
- [plannersyncaction_SyncErrors](#BKMK_plannersyncaction_SyncErrors)

### <a name="BKMK_plannersyncaction_AsyncOperations"></a> plannersyncaction_AsyncOperations

Many-To-One Relationship: [asyncoperation plannersyncaction_AsyncOperations](asyncoperation.md#BKMK_plannersyncaction_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`plannersyncaction_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_plannersyncaction_BulkDeleteFailures"></a> plannersyncaction_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure plannersyncaction_BulkDeleteFailures](bulkdeletefailure.md#BKMK_plannersyncaction_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`plannersyncaction_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_plannersyncaction_MailboxTrackingFolders"></a> plannersyncaction_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder plannersyncaction_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_plannersyncaction_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`plannersyncaction_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_plannersyncaction_PrincipalObjectAttributeAccesses"></a> plannersyncaction_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess plannersyncaction_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_plannersyncaction_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`plannersyncaction_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_plannersyncaction_ProcessSession"></a> plannersyncaction_ProcessSession

Many-To-One Relationship: [processsession plannersyncaction_ProcessSession](processsession.md#BKMK_plannersyncaction_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`plannersyncaction_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_plannersyncaction_SyncErrors"></a> plannersyncaction_SyncErrors

Many-To-One Relationship: [syncerror plannersyncaction_SyncErrors](syncerror.md#BKMK_plannersyncaction_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`plannersyncaction_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.plannersyncaction?displayProperty=fullName>
