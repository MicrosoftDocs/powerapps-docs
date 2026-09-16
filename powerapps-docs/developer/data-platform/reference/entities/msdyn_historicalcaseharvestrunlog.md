---
title: "Historical Case Harvest Run Log (msdyn_historicalcaseharvestrunlog) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Historical Case Harvest Run Log (msdyn_historicalcaseharvestrunlog) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: JimDaly
ms.author: jdaly
ms.reviewer: jdaly
search.audienceType: 
  - developer
---

# Historical Case Harvest Run Log (msdyn_historicalcaseharvestrunlog) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Historical Case Harvest Run Log (msdyn_historicalcaseharvestrunlog) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_historicalcaseharvestrunlogs(*msdyn_historicalcaseharvestrunlogid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_historicalcaseharvestrunlogs<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_historicalcaseharvestrunlogs(*msdyn_historicalcaseharvestrunlogid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Restore`<br />Event: True |<xref:Microsoft.Dynamics.CRM.Restore?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retrieve`<br />Event: True |`GET` /msdyn_historicalcaseharvestrunlogs(*msdyn_historicalcaseharvestrunlogid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_historicalcaseharvestrunlogs<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_historicalcaseharvestrunlogs(*msdyn_historicalcaseharvestrunlogid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_historicalcaseharvestrunlogs(*msdyn_historicalcaseharvestrunlogid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_historicalcaseharvestrunlogs(*msdyn_historicalcaseharvestrunlogid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Historical Case Harvest Run Log (msdyn_historicalcaseharvestrunlog) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Historical Case Harvest Run Log (msdyn_historicalcaseharvestrunlog) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Historical Case Harvest Run Log** |
| **DisplayCollectionName** | **Historical Case Harvest Run Logs** |
| **SchemaName** | `msdyn_historicalcaseharvestrunlog` |
| **CollectionSchemaName** | `msdyn_historicalcaseharvestrunlogs` |
| **EntitySetName** | `msdyn_historicalcaseharvestrunlogs`|
| **LogicalName** | `msdyn_historicalcaseharvestrunlog` |
| **LogicalCollectionName** | `msdyn_historicalcaseharvestrunlogs` |
| **PrimaryIdAttribute** | `msdyn_historicalcaseharvestrunlogid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_articlescreated](#BKMK_msdyn_articlescreated)
- [msdyn_casesalreadycovered](#BKMK_msdyn_casesalreadycovered)
- [msdyn_casesskipped](#BKMK_msdyn_casesskipped)
- [msdyn_historicalcaseharvestrunid](#BKMK_msdyn_historicalcaseharvestrunid)
- [msdyn_historicalcaseharvestrunlogId](#BKMK_msdyn_historicalcaseharvestrunlogId)
- [msdyn_logtime](#BKMK_msdyn_logtime)
- [msdyn_name](#BKMK_msdyn_name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

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

### <a name="BKMK_msdyn_articlescreated"></a> msdyn_articlescreated

|Property|Value|
|---|---|
|Description||
|DisplayName|**Articles Created**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_articlescreated`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_casesalreadycovered"></a> msdyn_casesalreadycovered

|Property|Value|
|---|---|
|Description||
|DisplayName|**Cases Already Covered**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_casesalreadycovered`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_casesskipped"></a> msdyn_casesskipped

|Property|Value|
|---|---|
|Description||
|DisplayName|**Cases Skipped**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_casesskipped`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_historicalcaseharvestrunid"></a> msdyn_historicalcaseharvestrunid

|Property|Value|
|---|---|
|Description||
|DisplayName|**Historical Case Harvest Run**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_historicalcaseharvestrunid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|msdyn_historicalcaseharvestrun|

### <a name="BKMK_msdyn_historicalcaseharvestrunlogId"></a> msdyn_historicalcaseharvestrunlogId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**historicalcaseharvestrunlog**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_historicalcaseharvestrunlogid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_logtime"></a> msdyn_logtime

|Property|Value|
|---|---|
|Description||
|DisplayName|**Log Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_logtime`|
|RequiredLevel|ApplicationRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|---|---|
|Description||
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|850|

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

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the historicalcaseharvestrunlog**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_historicalcaseharvestrunlog_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the historicalcaseharvestrunlog**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_historicalcaseharvestrunlog_statuscode`|

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

- [business_unit_msdyn_historicalcaseharvestrunlog](#BKMK_business_unit_msdyn_historicalcaseharvestrunlog)
- [lk_msdyn_historicalcaseharvestrunlog_createdby](#BKMK_lk_msdyn_historicalcaseharvestrunlog_createdby)
- [lk_msdyn_historicalcaseharvestrunlog_createdonbehalfby](#BKMK_lk_msdyn_historicalcaseharvestrunlog_createdonbehalfby)
- [lk_msdyn_historicalcaseharvestrunlog_modifiedby](#BKMK_lk_msdyn_historicalcaseharvestrunlog_modifiedby)
- [lk_msdyn_historicalcaseharvestrunlog_modifiedonbehalfby](#BKMK_lk_msdyn_historicalcaseharvestrunlog_modifiedonbehalfby)
- [msdyn_historicalcaseharvestrunlog_msdyn_historicalcaseharvestrun](#BKMK_msdyn_historicalcaseharvestrunlog_msdyn_historicalcaseharvestrun)
- [owner_msdyn_historicalcaseharvestrunlog](#BKMK_owner_msdyn_historicalcaseharvestrunlog)
- [team_msdyn_historicalcaseharvestrunlog](#BKMK_team_msdyn_historicalcaseharvestrunlog)
- [user_msdyn_historicalcaseharvestrunlog](#BKMK_user_msdyn_historicalcaseharvestrunlog)

### <a name="BKMK_business_unit_msdyn_historicalcaseharvestrunlog"></a> business_unit_msdyn_historicalcaseharvestrunlog

One-To-Many Relationship: [businessunit business_unit_msdyn_historicalcaseharvestrunlog](businessunit.md#BKMK_business_unit_msdyn_historicalcaseharvestrunlog)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_historicalcaseharvestrunlog_createdby"></a> lk_msdyn_historicalcaseharvestrunlog_createdby

One-To-Many Relationship: [systemuser lk_msdyn_historicalcaseharvestrunlog_createdby](systemuser.md#BKMK_lk_msdyn_historicalcaseharvestrunlog_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_historicalcaseharvestrunlog_createdonbehalfby"></a> lk_msdyn_historicalcaseharvestrunlog_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_historicalcaseharvestrunlog_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_historicalcaseharvestrunlog_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_historicalcaseharvestrunlog_modifiedby"></a> lk_msdyn_historicalcaseharvestrunlog_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_historicalcaseharvestrunlog_modifiedby](systemuser.md#BKMK_lk_msdyn_historicalcaseharvestrunlog_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_historicalcaseharvestrunlog_modifiedonbehalfby"></a> lk_msdyn_historicalcaseharvestrunlog_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_historicalcaseharvestrunlog_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_historicalcaseharvestrunlog_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_historicalcaseharvestrunlog_msdyn_historicalcaseharvestrun"></a> msdyn_historicalcaseharvestrunlog_msdyn_historicalcaseharvestrun

One-To-Many Relationship: [msdyn_historicalcaseharvestrun msdyn_historicalcaseharvestrunlog_msdyn_historicalcaseharvestrun](msdyn_historicalcaseharvestrun.md#BKMK_msdyn_historicalcaseharvestrunlog_msdyn_historicalcaseharvestrun)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_historicalcaseharvestrun`|
|ReferencedAttribute|`msdyn_historicalcaseharvestrunid`|
|ReferencingAttribute|`msdyn_historicalcaseharvestrunid`|
|ReferencingEntityNavigationPropertyName|`msdyn_historicalcaseharvestrunid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_owner_msdyn_historicalcaseharvestrunlog"></a> owner_msdyn_historicalcaseharvestrunlog

One-To-Many Relationship: [owner owner_msdyn_historicalcaseharvestrunlog](owner.md#BKMK_owner_msdyn_historicalcaseharvestrunlog)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_historicalcaseharvestrunlog"></a> team_msdyn_historicalcaseharvestrunlog

One-To-Many Relationship: [team team_msdyn_historicalcaseharvestrunlog](team.md#BKMK_team_msdyn_historicalcaseharvestrunlog)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_historicalcaseharvestrunlog"></a> user_msdyn_historicalcaseharvestrunlog

One-To-Many Relationship: [systemuser user_msdyn_historicalcaseharvestrunlog](systemuser.md#BKMK_user_msdyn_historicalcaseharvestrunlog)

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

- [msdyn_historicalcaseharvestrunlog_AsyncOperations](#BKMK_msdyn_historicalcaseharvestrunlog_AsyncOperations)
- [msdyn_historicalcaseharvestrunlog_BulkDeleteFailures](#BKMK_msdyn_historicalcaseharvestrunlog_BulkDeleteFailures)
- [msdyn_historicalcaseharvestrunlog_DeletedItemReferences](#BKMK_msdyn_historicalcaseharvestrunlog_DeletedItemReferences)
- [msdyn_historicalcaseharvestrunlog_DuplicateBaseRecord](#BKMK_msdyn_historicalcaseharvestrunlog_DuplicateBaseRecord)
- [msdyn_historicalcaseharvestrunlog_DuplicateMatchingRecord](#BKMK_msdyn_historicalcaseharvestrunlog_DuplicateMatchingRecord)
- [msdyn_historicalcaseharvestrunlog_MailboxTrackingFolders](#BKMK_msdyn_historicalcaseharvestrunlog_MailboxTrackingFolders)
- [msdyn_historicalcaseharvestrunlog_PrincipalObjectAttributeAccesses](#BKMK_msdyn_historicalcaseharvestrunlog_PrincipalObjectAttributeAccesses)
- [msdyn_historicalcaseharvestrunlog_ProcessSession](#BKMK_msdyn_historicalcaseharvestrunlog_ProcessSession)
- [msdyn_historicalcaseharvestrunlog_SyncErrors](#BKMK_msdyn_historicalcaseharvestrunlog_SyncErrors)

### <a name="BKMK_msdyn_historicalcaseharvestrunlog_AsyncOperations"></a> msdyn_historicalcaseharvestrunlog_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_historicalcaseharvestrunlog_AsyncOperations](asyncoperation.md#BKMK_msdyn_historicalcaseharvestrunlog_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestrunlog_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_historicalcaseharvestrunlog_BulkDeleteFailures"></a> msdyn_historicalcaseharvestrunlog_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_historicalcaseharvestrunlog_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_historicalcaseharvestrunlog_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestrunlog_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_historicalcaseharvestrunlog_DeletedItemReferences"></a> msdyn_historicalcaseharvestrunlog_DeletedItemReferences

Many-To-One Relationship: [deleteditemreference msdyn_historicalcaseharvestrunlog_DeletedItemReferences](deleteditemreference.md#BKMK_msdyn_historicalcaseharvestrunlog_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencingEntity|`deleteditemreference`|
|ReferencingAttribute|`deletedobject`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestrunlog_DeletedItemReferences`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_historicalcaseharvestrunlog_DuplicateBaseRecord"></a> msdyn_historicalcaseharvestrunlog_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord msdyn_historicalcaseharvestrunlog_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_historicalcaseharvestrunlog_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestrunlog_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_historicalcaseharvestrunlog_DuplicateMatchingRecord"></a> msdyn_historicalcaseharvestrunlog_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord msdyn_historicalcaseharvestrunlog_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_historicalcaseharvestrunlog_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestrunlog_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_historicalcaseharvestrunlog_MailboxTrackingFolders"></a> msdyn_historicalcaseharvestrunlog_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_historicalcaseharvestrunlog_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_historicalcaseharvestrunlog_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestrunlog_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_historicalcaseharvestrunlog_PrincipalObjectAttributeAccesses"></a> msdyn_historicalcaseharvestrunlog_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_historicalcaseharvestrunlog_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_historicalcaseharvestrunlog_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestrunlog_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_historicalcaseharvestrunlog_ProcessSession"></a> msdyn_historicalcaseharvestrunlog_ProcessSession

Many-To-One Relationship: [processsession msdyn_historicalcaseharvestrunlog_ProcessSession](processsession.md#BKMK_msdyn_historicalcaseharvestrunlog_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestrunlog_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_historicalcaseharvestrunlog_SyncErrors"></a> msdyn_historicalcaseharvestrunlog_SyncErrors

Many-To-One Relationship: [syncerror msdyn_historicalcaseharvestrunlog_SyncErrors](syncerror.md#BKMK_msdyn_historicalcaseharvestrunlog_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestrunlog_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_historicalcaseharvestrunlog?displayProperty=fullName>
