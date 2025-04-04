---
title: "Rollup Query (GoalRollupQuery) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Rollup Query (GoalRollupQuery) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Rollup Query (GoalRollupQuery) table/entity reference (Microsoft Dataverse)

Query that is used to filter the results of the goal rollup.

## Messages

The following table lists the messages for the Rollup Query (GoalRollupQuery) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /goalrollupqueries(*goalrollupqueryid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /goalrollupqueries<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /goalrollupqueries(*goalrollupqueryid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /goalrollupqueries(*goalrollupqueryid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /goalrollupqueries<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /goalrollupqueries(*goalrollupqueryid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /goalrollupqueries(*goalrollupqueryid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /goalrollupqueries(*goalrollupqueryid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Rollup Query (GoalRollupQuery) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Rollup Query** |
| **DisplayCollectionName** | **Rollup Queries** |
| **SchemaName** | `GoalRollupQuery` |
| **CollectionSchemaName** | `goalrollupqueries` |
| **EntitySetName** | `goalrollupqueries`|
| **LogicalName** | `goalrollupquery` |
| **LogicalCollectionName** | `goalrollupqueries` |
| **PrimaryIdAttribute** | `goalrollupqueryid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [FetchXml](#BKMK_FetchXml)
- [GoalRollupQueryId](#BKMK_GoalRollupQueryId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [QueryEntityType](#BKMK_QueryEntityType)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_FetchXml"></a> FetchXml

|Property|Value|
|---|---|
|Description|**String that specifies the condition criteria in FetchXML.**|
|DisplayName|**Condition Criteria**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fetchxml`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_GoalRollupQueryId"></a> GoalRollupQueryId

|Property|Value|
|---|---|
|Description|**Unique identifier of the rollup query.**|
|DisplayName|**Goal Rollup Query**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`goalrollupqueryid`|
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
|Description|**Type a descriptive name for the goal rollup query.**|
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
|Description|**Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.**|
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

### <a name="BKMK_QueryEntityType"></a> QueryEntityType

|Property|Value|
|---|---|
|Description|**Enter the record type of the rollup query.**|
|DisplayName|**Entity Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`queryentitytype`|
|RequiredLevel|ApplicationRequired|
|Type|EntityName|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Shows whether the goal rollup query is active or inactive.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`goalrollupquery_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 0<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 1<br />InvariantName: `Inactive`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Select the goal rollup query's status.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`goalrollupquery_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Open**<br />State:0<br />TransitionData: None|
|1|Label: **Closed**<br />State:1<br />TransitionData: None|

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
|Description|**Unique identifier of the business unit that owns the record.**|
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
|Description|**Unique identifier of the team who owns the record.**|
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
|Description|**Unique identifier of the user who owns the record.**|
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
|Description|**Version number of the goal rollup query.**|
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

- [business_unit_goalrollupquery](#BKMK_business_unit_goalrollupquery)
- [lk_goalrollupquery_createdby](#BKMK_lk_goalrollupquery_createdby)
- [lk_goalrollupquery_createdonbehalfby](#BKMK_lk_goalrollupquery_createdonbehalfby)
- [lk_goalrollupquery_modifiedby](#BKMK_lk_goalrollupquery_modifiedby)
- [lk_goalrollupquery_modifiedonbehalfby](#BKMK_lk_goalrollupquery_modifiedonbehalfby)
- [owner_goalrollupquery](#BKMK_owner_goalrollupquery)
- [team_goalrollupquery](#BKMK_team_goalrollupquery)

### <a name="BKMK_business_unit_goalrollupquery"></a> business_unit_goalrollupquery

One-To-Many Relationship: [businessunit business_unit_goalrollupquery](businessunit.md#BKMK_business_unit_goalrollupquery)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_goalrollupquery_createdby"></a> lk_goalrollupquery_createdby

One-To-Many Relationship: [systemuser lk_goalrollupquery_createdby](systemuser.md#BKMK_lk_goalrollupquery_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_goalrollupquery_createdonbehalfby"></a> lk_goalrollupquery_createdonbehalfby

One-To-Many Relationship: [systemuser lk_goalrollupquery_createdonbehalfby](systemuser.md#BKMK_lk_goalrollupquery_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_goalrollupquery_modifiedby"></a> lk_goalrollupquery_modifiedby

One-To-Many Relationship: [systemuser lk_goalrollupquery_modifiedby](systemuser.md#BKMK_lk_goalrollupquery_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_goalrollupquery_modifiedonbehalfby"></a> lk_goalrollupquery_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_goalrollupquery_modifiedonbehalfby](systemuser.md#BKMK_lk_goalrollupquery_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_goalrollupquery"></a> owner_goalrollupquery

One-To-Many Relationship: [owner owner_goalrollupquery](owner.md#BKMK_owner_goalrollupquery)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_goalrollupquery"></a> team_goalrollupquery

One-To-Many Relationship: [team team_goalrollupquery](team.md#BKMK_team_goalrollupquery)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [goal_rollupquery_actualdecimal](#BKMK_goal_rollupquery_actualdecimal)
- [goal_rollupquery_actualmoney](#BKMK_goal_rollupquery_actualmoney)
- [goal_rollupquery_customdecimal](#BKMK_goal_rollupquery_customdecimal)
- [goal_rollupquery_customint](#BKMK_goal_rollupquery_customint)
- [goal_rollupquery_custommoney](#BKMK_goal_rollupquery_custommoney)
- [goal_rollupquery_inprogressdecimal](#BKMK_goal_rollupquery_inprogressdecimal)
- [goal_rollupquery_inprogressint](#BKMK_goal_rollupquery_inprogressint)
- [goal_rollupquery_inprogressmoney](#BKMK_goal_rollupquery_inprogressmoney)
- [goalrollupquery_actualint](#BKMK_goalrollupquery_actualint)
- [goalrollupquery_AsyncOperations](#BKMK_goalrollupquery_AsyncOperations)
- [GoalRollupQuery_DuplicateBaseRecord](#BKMK_GoalRollupQuery_DuplicateBaseRecord)
- [GoalRollupQuery_DuplicateMatchingRecord](#BKMK_GoalRollupQuery_DuplicateMatchingRecord)
- [goalrollupquery_ProcessSessions](#BKMK_goalrollupquery_ProcessSessions)
- [GoalRollupQuery_SyncErrors](#BKMK_GoalRollupQuery_SyncErrors)

### <a name="BKMK_goal_rollupquery_actualdecimal"></a> goal_rollupquery_actualdecimal

Many-To-One Relationship: [goal goal_rollupquery_actualdecimal](goal.md#BKMK_goal_rollupquery_actualdecimal)

|Property|Value|
|---|---|
|ReferencingEntity|`goal`|
|ReferencingAttribute|`rollupqueryactualdecimalid`|
|ReferencedEntityNavigationPropertyName|`goal_rollupquery_actualdecimal`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_goal_rollupquery_actualmoney"></a> goal_rollupquery_actualmoney

Many-To-One Relationship: [goal goal_rollupquery_actualmoney](goal.md#BKMK_goal_rollupquery_actualmoney)

|Property|Value|
|---|---|
|ReferencingEntity|`goal`|
|ReferencingAttribute|`rollupqueryactualmoneyid`|
|ReferencedEntityNavigationPropertyName|`goal_rollupquery_actualmoney`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_goal_rollupquery_customdecimal"></a> goal_rollupquery_customdecimal

Many-To-One Relationship: [goal goal_rollupquery_customdecimal](goal.md#BKMK_goal_rollupquery_customdecimal)

|Property|Value|
|---|---|
|ReferencingEntity|`goal`|
|ReferencingAttribute|`rollupquerycustomdecimalid`|
|ReferencedEntityNavigationPropertyName|`goal_rollupquery_customdecimal`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_goal_rollupquery_customint"></a> goal_rollupquery_customint

Many-To-One Relationship: [goal goal_rollupquery_customint](goal.md#BKMK_goal_rollupquery_customint)

|Property|Value|
|---|---|
|ReferencingEntity|`goal`|
|ReferencingAttribute|`rollupquerycustomintegerid`|
|ReferencedEntityNavigationPropertyName|`goal_rollupquery_customint`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_goal_rollupquery_custommoney"></a> goal_rollupquery_custommoney

Many-To-One Relationship: [goal goal_rollupquery_custommoney](goal.md#BKMK_goal_rollupquery_custommoney)

|Property|Value|
|---|---|
|ReferencingEntity|`goal`|
|ReferencingAttribute|`rollupquerycustommoneyid`|
|ReferencedEntityNavigationPropertyName|`goal_rollupquery_custommoney`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_goal_rollupquery_inprogressdecimal"></a> goal_rollupquery_inprogressdecimal

Many-To-One Relationship: [goal goal_rollupquery_inprogressdecimal](goal.md#BKMK_goal_rollupquery_inprogressdecimal)

|Property|Value|
|---|---|
|ReferencingEntity|`goal`|
|ReferencingAttribute|`rollupqueryinprogressdecimalid`|
|ReferencedEntityNavigationPropertyName|`goal_rollupquery_inprogressdecimal`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_goal_rollupquery_inprogressint"></a> goal_rollupquery_inprogressint

Many-To-One Relationship: [goal goal_rollupquery_inprogressint](goal.md#BKMK_goal_rollupquery_inprogressint)

|Property|Value|
|---|---|
|ReferencingEntity|`goal`|
|ReferencingAttribute|`rollupqueryinprogressintegerid`|
|ReferencedEntityNavigationPropertyName|`goal_rollupquery_inprogressint`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_goal_rollupquery_inprogressmoney"></a> goal_rollupquery_inprogressmoney

Many-To-One Relationship: [goal goal_rollupquery_inprogressmoney](goal.md#BKMK_goal_rollupquery_inprogressmoney)

|Property|Value|
|---|---|
|ReferencingEntity|`goal`|
|ReferencingAttribute|`rollupqueryinprogressmoneyid`|
|ReferencedEntityNavigationPropertyName|`goal_rollupquery_inprogressmoney`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_goalrollupquery_actualint"></a> goalrollupquery_actualint

Many-To-One Relationship: [goal goalrollupquery_actualint](goal.md#BKMK_goalrollupquery_actualint)

|Property|Value|
|---|---|
|ReferencingEntity|`goal`|
|ReferencingAttribute|`rollupqueryactualintegerid`|
|ReferencedEntityNavigationPropertyName|`goalrollupquery_actualint`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_goalrollupquery_AsyncOperations"></a> goalrollupquery_AsyncOperations

Many-To-One Relationship: [asyncoperation goalrollupquery_AsyncOperations](asyncoperation.md#BKMK_goalrollupquery_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`goalrollupquery_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_GoalRollupQuery_DuplicateBaseRecord"></a> GoalRollupQuery_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord GoalRollupQuery_DuplicateBaseRecord](duplicaterecord.md#BKMK_GoalRollupQuery_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`GoalRollupQuery_DuplicateBaseRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_GoalRollupQuery_DuplicateMatchingRecord"></a> GoalRollupQuery_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord GoalRollupQuery_DuplicateMatchingRecord](duplicaterecord.md#BKMK_GoalRollupQuery_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`GoalRollupQuery_DuplicateMatchingRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_goalrollupquery_ProcessSessions"></a> goalrollupquery_ProcessSessions

Many-To-One Relationship: [processsession goalrollupquery_ProcessSessions](processsession.md#BKMK_goalrollupquery_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`goalrollupquery_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_GoalRollupQuery_SyncErrors"></a> GoalRollupQuery_SyncErrors

Many-To-One Relationship: [syncerror GoalRollupQuery_SyncErrors](syncerror.md#BKMK_GoalRollupQuery_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`GoalRollupQuery_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.goalrollupquery?displayProperty=fullName>
