---
title: "PlannerSyncAction table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the PlannerSyncAction table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# PlannerSyncAction table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

The Planner Sync Action to be executed.

**Added by**: PlannerSync_Extensions Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /plannersyncactions(*plannersyncactionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST /plannersyncactions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /plannersyncactions(*plannersyncactionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET /plannersyncactions(*plannersyncactionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /plannersyncactions<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH /plannersyncactions(*plannersyncactionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /plannersyncactions(*plannersyncactionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|PlannerSyncActions|
|DisplayCollectionName|Planner Sync Actions|
|DisplayName|Planner Sync Action|
|EntitySetName|plannersyncactions|
|IsBPFEntity|False|
|LogicalCollectionName|plannersyncactions|
|LogicalName|plannersyncaction|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|plannersyncactionid|
|PrimaryNameAttribute|title|
|SchemaName|PlannerSyncAction|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description||
|DisplayName|Assignments|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|assignments|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_DueDateTime"></a> DueDateTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|TimeZoneIndependent|
|Description|Date and time when the planner task is due.|
|DisplayName|Due Date Time|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|duedatetime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ExternalBucketId"></a> ExternalBucketId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|External Bucket Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|externalbucketid|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ExternalReferences"></a> ExternalReferences

|Property|Value|
|--------|-----|
|Description||
|DisplayName|External References|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|externalreferences|
|MaxLength|2000|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_GroupId"></a> GroupId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Group Id|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|groupid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|Sequence number of the import that created this record.|
|DisplayName|Import Sequence Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|importsequencenumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_LastAttemptedOn"></a> LastAttemptedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|TimeZoneIndependent|
|Description|For internal use only. Date and time when the action was last attempted.|
|DisplayName|Last Attempted On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|lastattemptedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_LastSyncError"></a> LastSyncError

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Last Sync Error|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|lastsyncerror|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Notes"></a> Notes

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Notes|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|notes|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time that the record was migrated.|
|DisplayName|Record Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_OwnerId"></a> OwnerId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Owner Id|
|DisplayName|Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Targets|systemuser,team|
|Type|Owner|


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Owner Id Type|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_PendingAttempts"></a> PendingAttempts

|Property|Value|
|--------|-----|
|Description|The attempts available for processing the planner sync action.|
|DisplayName|Pending Attempts|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|pendingattempts|
|MaxValue|5|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_PercentComplete"></a> PercentComplete

|Property|Value|
|--------|-----|
|Description|The percentage of completion for the planner task.|
|DisplayName|Percent Complete|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|percentcomplete|
|MaxValue|100|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_PlannerBusinessScenarioId"></a> PlannerBusinessScenarioId

|Property|Value|
|--------|-----|
|Description|Id of the Business Scenario in Planner.|
|DisplayName|Planner Business Scenario Id|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|plannerbusinessscenarioid|
|RequiredLevel|SystemRequired|
|Targets|plannerbusinessscenario|
|Type|Lookup|


### <a name="BKMK_PlannerSyncActionId"></a> PlannerSyncActionId

|Property|Value|
|--------|-----|
|Description|Planner Sync Action Id|
|DisplayName|Planner Sync Action Id|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|plannersyncactionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_Priority"></a> Priority

|Property|Value|
|--------|-----|
|Description|The priority of the planner task.|
|DisplayName|Priority|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|priority|
|MaxValue|10|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_QueuedOn"></a> QueuedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|TimeZoneIndependent|
|Description|For internal use only. Date and time when the action was queued.|
|DisplayName|Queued On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|queuedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_SourceRecordEntityLogicalName"></a> SourceRecordEntityLogicalName

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Source Record Entity Logical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|sourcerecordentitylogicalname|
|MaxLength|50|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_SourceRecordId"></a> SourceRecordId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Source Record Id|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|sourcerecordid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_StartDateTime"></a> StartDateTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|TimeZoneIndependent|
|Description|Date and time when the planner task was started.|
|DisplayName|Start Date Time|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|startdatetime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Planner Sync Action|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### statecode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|1|Active|
|1|Inactive|2|Inactive|



### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the Planner Sync Action|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### statuscode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Active|0|
|2|Inactive|1|



### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Time Zone Rule Version Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezoneruleversionnumber|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_Title"></a> Title

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Title|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|title|
|MaxLength|200|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|--------|-----|
|Description|Time zone code that was in use when the record was created.|
|DisplayName|UTC Conversion Time Zone Code|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|utcconversiontimezonecode|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [plannerbusinessscenarioidName](#BKMK_plannerbusinessscenarioidName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Name of the owner|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Yomi name of the owner|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the business unit that owns the record|
|DisplayName|Owning Business Unit|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|SystemRequired|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningBusinessUnitName"></a> OwningBusinessUnitName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunitname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the team that owns the record.|
|DisplayName|Owning Team|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteam|
|RequiredLevel|None|
|Targets|team|
|Type|Lookup|


### <a name="BKMK_OwningUser"></a> OwningUser

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the user that owns the record.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_plannerbusinessscenarioidName"></a> plannerbusinessscenarioidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|plannerbusinessscenarioidname|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Version Number|
|DisplayName|Version Number|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [plannersyncaction_SyncErrors](#BKMK_plannersyncaction_SyncErrors)
- [plannersyncaction_AsyncOperations](#BKMK_plannersyncaction_AsyncOperations)
- [plannersyncaction_MailboxTrackingFolders](#BKMK_plannersyncaction_MailboxTrackingFolders)
- [plannersyncaction_ProcessSession](#BKMK_plannersyncaction_ProcessSession)
- [plannersyncaction_BulkDeleteFailures](#BKMK_plannersyncaction_BulkDeleteFailures)
- [plannersyncaction_PrincipalObjectAttributeAccesses](#BKMK_plannersyncaction_PrincipalObjectAttributeAccesses)


### <a name="BKMK_plannersyncaction_SyncErrors"></a> plannersyncaction_SyncErrors

**Added by**: System Solution Solution

Same as the [plannersyncaction_SyncErrors](syncerror.md#BKMK_plannersyncaction_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|plannersyncaction_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_plannersyncaction_AsyncOperations"></a> plannersyncaction_AsyncOperations

**Added by**: System Solution Solution

Same as the [plannersyncaction_AsyncOperations](asyncoperation.md#BKMK_plannersyncaction_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|plannersyncaction_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_plannersyncaction_MailboxTrackingFolders"></a> plannersyncaction_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [plannersyncaction_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_plannersyncaction_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|plannersyncaction_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_plannersyncaction_ProcessSession"></a> plannersyncaction_ProcessSession

**Added by**: System Solution Solution

Same as the [plannersyncaction_ProcessSession](processsession.md#BKMK_plannersyncaction_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|plannersyncaction_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_plannersyncaction_BulkDeleteFailures"></a> plannersyncaction_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [plannersyncaction_BulkDeleteFailures](bulkdeletefailure.md#BKMK_plannersyncaction_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|plannersyncaction_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_plannersyncaction_PrincipalObjectAttributeAccesses"></a> plannersyncaction_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [plannersyncaction_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_plannersyncaction_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|plannersyncaction_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [user_plannersyncaction](#BKMK_user_plannersyncaction)
- [team_plannersyncaction](#BKMK_team_plannersyncaction)
- [business_unit_plannersyncaction](#BKMK_business_unit_plannersyncaction)
- [plannerbusinessscenario_plannersyncaction_plannerbusinessscenarioid](#BKMK_plannerbusinessscenario_plannersyncaction_plannerbusinessscenarioid)


### <a name="BKMK_user_plannersyncaction"></a> user_plannersyncaction

**Added by**: System Solution Solution

See the [user_plannersyncaction](systemuser.md#BKMK_user_plannersyncaction) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_team_plannersyncaction"></a> team_plannersyncaction

**Added by**: System Solution Solution

See the [team_plannersyncaction](team.md#BKMK_team_plannersyncaction) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_business_unit_plannersyncaction"></a> business_unit_plannersyncaction

**Added by**: System Solution Solution

See the [business_unit_plannersyncaction](businessunit.md#BKMK_business_unit_plannersyncaction) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_plannerbusinessscenario_plannersyncaction_plannerbusinessscenarioid"></a> plannerbusinessscenario_plannersyncaction_plannerbusinessscenarioid

See the [plannerbusinessscenario_plannersyncaction_plannerbusinessscenarioid](plannerbusinessscenario.md#BKMK_plannerbusinessscenario_plannersyncaction_plannerbusinessscenarioid) one-to-many relationship for the [plannerbusinessscenario](plannerbusinessscenario.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.plannersyncaction?text=plannersyncaction EntityType" />