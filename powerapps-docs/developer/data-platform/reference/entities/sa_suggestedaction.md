---
title: "Suggested Action (sa_SuggestedAction) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Suggested Action (sa_SuggestedAction) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Suggested Action (sa_SuggestedAction) table/entity reference (Microsoft Dataverse)

This table contains records of suggested actions with execution details.

## Messages

The following table lists the messages for the Suggested Action (sa_SuggestedAction) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /sa_suggestedactions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /sa_suggestedactions(*sa_suggestedactionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Retrieve`<br />Event: True |`GET` /sa_suggestedactions(*sa_suggestedactionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /sa_suggestedactions<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /sa_suggestedactions(*sa_suggestedactionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /sa_suggestedactions(*sa_suggestedactionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /sa_suggestedactions(*sa_suggestedactionid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Suggested Action (sa_SuggestedAction) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Suggested Action (sa_SuggestedAction) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Suggested Action** |
| **DisplayCollectionName** | **Suggested Actions** |
| **SchemaName** | `sa_SuggestedAction` |
| **CollectionSchemaName** | `sa_SuggestedActions` |
| **EntitySetName** | `sa_suggestedactions`|
| **LogicalName** | `sa_suggestedaction` |
| **LogicalCollectionName** | `sa_suggestedactions` |
| **PrimaryIdAttribute** | `sa_suggestedactionid` |
| **PrimaryNameAttribute** |`sa_actiontitle` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [sa_ActionExecutionSteps](#BKMK_sa_ActionExecutionSteps)
- [sa_ActionTitle](#BKMK_sa_ActionTitle)
- [sa_AppId](#BKMK_sa_AppId)
- [sa_CompletedBy](#BKMK_sa_CompletedBy)
- [sa_CompletedOn](#BKMK_sa_CompletedOn)
- [sa_CriteriaId](#BKMK_sa_CriteriaId)
- [sa_GeneratorTag](#BKMK_sa_GeneratorTag)
- [sa_MakerActionName](#BKMK_sa_MakerActionName)
- [sa_Rationale](#BKMK_sa_Rationale)
- [sa_RowID](#BKMK_sa_RowID)
- [sa_SuggestedActionId](#BKMK_sa_SuggestedActionId)
- [sa_TableID](#BKMK_sa_TableID)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

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

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier for the organization**|
|DisplayName|**Organization Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|organization|

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

### <a name="BKMK_sa_ActionExecutionSteps"></a> sa_ActionExecutionSteps

|Property|Value|
|---|---|
|Description||
|DisplayName|**Action Execution Steps**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sa_actionexecutionsteps`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_sa_ActionTitle"></a> sa_ActionTitle

|Property|Value|
|---|---|
|Description||
|DisplayName|**Action Title**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sa_actiontitle`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_sa_AppId"></a> sa_AppId

|Property|Value|
|---|---|
|Description||
|DisplayName|**App Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sa_appid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_sa_CompletedBy"></a> sa_CompletedBy

|Property|Value|
|---|---|
|Description||
|DisplayName|**Completed By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sa_completedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_sa_CompletedOn"></a> sa_CompletedOn

|Property|Value|
|---|---|
|Description||
|DisplayName|**Completed On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sa_completedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_sa_CriteriaId"></a> sa_CriteriaId

|Property|Value|
|---|---|
|Description||
|DisplayName|**CriteriaId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sa_criteriaid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|sa_suggestedactioncriteria|

### <a name="BKMK_sa_GeneratorTag"></a> sa_GeneratorTag

|Property|Value|
|---|---|
|Description||
|DisplayName|**Generator Tag**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sa_generatortag`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_sa_MakerActionName"></a> sa_MakerActionName

|Property|Value|
|---|---|
|Description||
|DisplayName|**Maker Action Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sa_makeractionname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_sa_Rationale"></a> sa_Rationale

|Property|Value|
|---|---|
|Description||
|DisplayName|**Rationale**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sa_rationale`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_sa_RowID"></a> sa_RowID

|Property|Value|
|---|---|
|Description||
|DisplayName|**Row ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sa_rowid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_sa_SuggestedActionId"></a> sa_SuggestedActionId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**SuggestedAction**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sa_suggestedactionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_sa_TableID"></a> sa_TableID

|Property|Value|
|---|---|
|Description||
|DisplayName|**Table ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sa_tableid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the SuggestedAction**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`sa_suggestedaction_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the SuggestedAction**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`sa_suggestedaction_statuscode`|

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

- [lk_sa_suggestedaction_createdby](#BKMK_lk_sa_suggestedaction_createdby)
- [lk_sa_suggestedaction_createdonbehalfby](#BKMK_lk_sa_suggestedaction_createdonbehalfby)
- [lk_sa_suggestedaction_modifiedby](#BKMK_lk_sa_suggestedaction_modifiedby)
- [lk_sa_suggestedaction_modifiedonbehalfby](#BKMK_lk_sa_suggestedaction_modifiedonbehalfby)
- [organization_sa_suggestedaction](#BKMK_organization_sa_suggestedaction)
- [sa_suggestedaction_CompletedBy_systemuser](#BKMK_sa_suggestedaction_CompletedBy_systemuser)
- [sa_suggestedaction_CriteriaId_sa_suggestedactioncriteria](#BKMK_sa_suggestedaction_CriteriaId_sa_suggestedactioncriteria)

### <a name="BKMK_lk_sa_suggestedaction_createdby"></a> lk_sa_suggestedaction_createdby

One-To-Many Relationship: [systemuser lk_sa_suggestedaction_createdby](systemuser.md#BKMK_lk_sa_suggestedaction_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sa_suggestedaction_createdonbehalfby"></a> lk_sa_suggestedaction_createdonbehalfby

One-To-Many Relationship: [systemuser lk_sa_suggestedaction_createdonbehalfby](systemuser.md#BKMK_lk_sa_suggestedaction_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sa_suggestedaction_modifiedby"></a> lk_sa_suggestedaction_modifiedby

One-To-Many Relationship: [systemuser lk_sa_suggestedaction_modifiedby](systemuser.md#BKMK_lk_sa_suggestedaction_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sa_suggestedaction_modifiedonbehalfby"></a> lk_sa_suggestedaction_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_sa_suggestedaction_modifiedonbehalfby](systemuser.md#BKMK_lk_sa_suggestedaction_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_sa_suggestedaction"></a> organization_sa_suggestedaction

One-To-Many Relationship: [organization organization_sa_suggestedaction](organization.md#BKMK_organization_sa_suggestedaction)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sa_suggestedaction_CompletedBy_systemuser"></a> sa_suggestedaction_CompletedBy_systemuser

One-To-Many Relationship: [systemuser sa_suggestedaction_CompletedBy_systemuser](systemuser.md#BKMK_sa_suggestedaction_CompletedBy_systemuser)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`sa_completedby`|
|ReferencingEntityNavigationPropertyName|`sa_CompletedBy`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sa_suggestedaction_CriteriaId_sa_suggestedactioncriteria"></a> sa_suggestedaction_CriteriaId_sa_suggestedactioncriteria

One-To-Many Relationship: [sa_suggestedactioncriteria sa_suggestedaction_CriteriaId_sa_suggestedactioncriteria](sa_suggestedactioncriteria.md#BKMK_sa_suggestedaction_CriteriaId_sa_suggestedactioncriteria)

|Property|Value|
|---|---|
|ReferencedEntity|`sa_suggestedactioncriteria`|
|ReferencedAttribute|`sa_suggestedactioncriteriaid`|
|ReferencingAttribute|`sa_criteriaid`|
|ReferencingEntityNavigationPropertyName|`sa_CriteriaId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [sa_suggestedaction_AsyncOperations](#BKMK_sa_suggestedaction_AsyncOperations)
- [sa_suggestedaction_BulkDeleteFailures](#BKMK_sa_suggestedaction_BulkDeleteFailures)
- [sa_suggestedaction_MailboxTrackingFolders](#BKMK_sa_suggestedaction_MailboxTrackingFolders)
- [sa_suggestedaction_PrincipalObjectAttributeAccesses](#BKMK_sa_suggestedaction_PrincipalObjectAttributeAccesses)
- [sa_suggestedaction_ProcessSession](#BKMK_sa_suggestedaction_ProcessSession)
- [sa_suggestedaction_SyncErrors](#BKMK_sa_suggestedaction_SyncErrors)

### <a name="BKMK_sa_suggestedaction_AsyncOperations"></a> sa_suggestedaction_AsyncOperations

Many-To-One Relationship: [asyncoperation sa_suggestedaction_AsyncOperations](asyncoperation.md#BKMK_sa_suggestedaction_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`sa_suggestedaction_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sa_suggestedaction_BulkDeleteFailures"></a> sa_suggestedaction_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure sa_suggestedaction_BulkDeleteFailures](bulkdeletefailure.md#BKMK_sa_suggestedaction_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`sa_suggestedaction_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sa_suggestedaction_MailboxTrackingFolders"></a> sa_suggestedaction_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder sa_suggestedaction_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_sa_suggestedaction_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`sa_suggestedaction_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sa_suggestedaction_PrincipalObjectAttributeAccesses"></a> sa_suggestedaction_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess sa_suggestedaction_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_sa_suggestedaction_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`sa_suggestedaction_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sa_suggestedaction_ProcessSession"></a> sa_suggestedaction_ProcessSession

Many-To-One Relationship: [processsession sa_suggestedaction_ProcessSession](processsession.md#BKMK_sa_suggestedaction_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`sa_suggestedaction_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sa_suggestedaction_SyncErrors"></a> sa_suggestedaction_SyncErrors

Many-To-One Relationship: [syncerror sa_suggestedaction_SyncErrors](syncerror.md#BKMK_sa_suggestedaction_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`sa_suggestedaction_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.sa_suggestedaction?displayProperty=fullName>
