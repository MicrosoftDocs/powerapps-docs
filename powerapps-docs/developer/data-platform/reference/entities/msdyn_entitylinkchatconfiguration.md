---
title: "Entity link chat configuration (msdyn_entitylinkchatconfiguration) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Entity link chat configuration (msdyn_entitylinkchatconfiguration) table/entity with Microsoft Dataverse."
ms.date: 11/09/2024
ms.service: powerapps
ms.topic: reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Entity link chat configuration (msdyn_entitylinkchatconfiguration) table/entity reference



## Messages

The following table lists the messages for the Entity link chat configuration (msdyn_entitylinkchatconfiguration) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_entitylinkchatconfigurations(*msdyn_entitylinkchatconfigurationid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Create`<br />Event: True |`POST` /msdyn_entitylinkchatconfigurations<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_entitylinkchatconfigurations(*msdyn_entitylinkchatconfigurationid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msdyn_entitylinkchatconfigurations(*msdyn_entitylinkchatconfigurationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_entitylinkchatconfigurations<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_entitylinkchatconfigurations(*msdyn_entitylinkchatconfigurationid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_entitylinkchatconfigurations(*msdyn_entitylinkchatconfigurationid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_entitylinkchatconfigurations(*msdyn_entitylinkchatconfigurationid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Entity link chat configuration (msdyn_entitylinkchatconfiguration) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Entity link chat configuration (msdyn_entitylinkchatconfiguration) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Entity link chat configuration** |
| **DisplayCollectionName** | **Entity link chat configurations** |
| **SchemaName** | `msdyn_entitylinkchatconfiguration` |
| **CollectionSchemaName** | `msdyn_entitylinkchatconfigurations` |
| **EntitySetName** | `msdyn_entitylinkchatconfigurations`|
| **LogicalName** | `msdyn_entitylinkchatconfiguration` |
| **LogicalCollectionName** | `msdyn_entitylinkchatconfigurations` |
| **PrimaryIdAttribute** | `msdyn_entitylinkchatconfigurationid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [msdyn_ContextViewId](#BKMK_msdyn_ContextViewId)
- [msdyn_EnableAiIntroductionMessage](#BKMK_msdyn_EnableAiIntroductionMessage)
- [msdyn_EnableAiSuggestion](#BKMK_msdyn_EnableAiSuggestion)
- [msdyn_EnableAutoNameChats](#BKMK_msdyn_EnableAutoNameChats)
- [msdyn_EnableKickoffMessage](#BKMK_msdyn_EnableKickoffMessage)
- [msdyn_EnableLogicBasedSuggestion](#BKMK_msdyn_EnableLogicBasedSuggestion)
- [msdyn_entitylinkchatconfigurationId](#BKMK_msdyn_entitylinkchatconfigurationId)
- [msdyn_EntityType](#BKMK_msdyn_EntityType)
- [msdyn_filteringAttributes](#BKMK_msdyn_filteringAttributes)
- [msdyn_isEnabledForBot](#BKMK_msdyn_isEnabledForBot)
- [msdyn_Name](#BKMK_msdyn_Name)
- [msdyn_RecentChatLinkerCanUnlink](#BKMK_msdyn_RecentChatLinkerCanUnlink)
- [msdyn_RecordOwnerCanUnlink](#BKMK_msdyn_RecordOwnerCanUnlink)
- [msdyn_UniqueName](#BKMK_msdyn_UniqueName)
- [msdyn_UserCanJoinChat](#BKMK_msdyn_UserCanJoinChat)
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

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Is Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_msdyn_ContextViewId"></a> msdyn_ContextViewId

|Property|Value|
|---|---|
|Description|**The view id of the selected context view.**|
|DisplayName|**Context view id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_contextviewid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_EnableAiIntroductionMessage"></a> msdyn_EnableAiIntroductionMessage

|Property|Value|
|---|---|
|Description|**Value of Enable AI introduction message**|
|DisplayName|**Enable AI introduction message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_enableaiintroductionmessage`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_entitylinkchatconfiguration_msdyn_enableaiintroductionmessage`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_EnableAiSuggestion"></a> msdyn_EnableAiSuggestion

|Property|Value|
|---|---|
|Description|**Value of Enable AI suggestion**|
|DisplayName|**Enable AI suggestion**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_enableaisuggestion`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_entitylinkchatconfiguration_msdyn_enableaisuggestion`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_EnableAutoNameChats"></a> msdyn_EnableAutoNameChats

|Property|Value|
|---|---|
|Description|**Enable auto name chats**|
|DisplayName|**Enable auto name chats**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_enableautonamechats`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_entitylinkchatconfiguration_msdyn_enableautonamechats`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_EnableKickoffMessage"></a> msdyn_EnableKickoffMessage

|Property|Value|
|---|---|
|Description|**Enable kickoff message**|
|DisplayName|**Enable kickoff message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_enablekickoffmessage`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_entitylinkchatconfiguration_msdyn_enablekickoffmessage`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_EnableLogicBasedSuggestion"></a> msdyn_EnableLogicBasedSuggestion

|Property|Value|
|---|---|
|Description|**Enable logic-based suggestion**|
|DisplayName|**Enable logic-based suggestion**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_enablelogicbasedsuggestion`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_entitylinkchatconfiguration_msdyn_enablelogicbasedsuggestion`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_entitylinkchatconfigurationId"></a> msdyn_entitylinkchatconfigurationId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Entity link chat configuration**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_entitylinkchatconfigurationid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_EntityType"></a> msdyn_EntityType

|Property|Value|
|---|---|
|Description|**The entity setup for link team configuration.**|
|DisplayName|**Entity type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_entitytype`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|entity|

### <a name="BKMK_msdyn_filteringAttributes"></a> msdyn_filteringAttributes

|Property|Value|
|---|---|
|Description|**List of attributes that we want bot event updates on**|
|DisplayName|**Filtering Attributes**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_filteringattributes`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_msdyn_isEnabledForBot"></a> msdyn_isEnabledForBot

|Property|Value|
|---|---|
|Description|**To indicate whether bot event update is enabled for this record**|
|DisplayName|**Is Enabled For Bot updates**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isenabledforbot`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_entitylinkchatconfiguration_msdyn_isenabledforbot`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_Name"></a> msdyn_Name

|Property|Value|
|---|---|
|Description|**The name of link team configuration.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_msdyn_RecentChatLinkerCanUnlink"></a> msdyn_RecentChatLinkerCanUnlink

|Property|Value|
|---|---|
|Description|**Value of recent chat linker can unlink**|
|DisplayName|**Recent chat linker can unlink**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_recentchatlinkercanunlink`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_entitylinkchatconfiguration_msdyn_recentchatlinkercanunlink`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_RecordOwnerCanUnlink"></a> msdyn_RecordOwnerCanUnlink

|Property|Value|
|---|---|
|Description|**Value of record owner can unlink**|
|DisplayName|**Record owner can unlink**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_recordownercanunlink`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_entitylinkchatconfiguration_msdyn_recordownercanunlink`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_UniqueName"></a> msdyn_UniqueName

|Property|Value|
|---|---|
|Description|**Unique Name for the entity.**|
|DisplayName|**Unique Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_uniquename`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_msdyn_UserCanJoinChat"></a> msdyn_UserCanJoinChat

|Property|Value|
|---|---|
|Description|**Value of User can join chat**|
|DisplayName|**User can join chat**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_usercanjoinchat`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_entitylinkchatconfiguration_msdyn_usercanjoinchat`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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
|Description|**Status of the Entitylink chat configuration**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_entitylinkchatconfiguration_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Entitylink chat configuration**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_entitylinkchatconfiguration_statuscode`|

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

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentIdUnique"></a> ComponentIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Row id unique**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Component State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentstate`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`componentstate`|

#### ComponentState Choices/Options

|Value|Label|
|---|---|
|0|**Published**|
|1|**Unpublished**|
|2|**Deleted**|
|3|**Deleted Unpublished**|

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

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Indicates whether the solution component is part of a managed solution.**|
|DisplayName|**Is Managed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

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

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Record Overwrite Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overwritetime`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

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

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the associated solution.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`supportingsolutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

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

- [business_unit_msdyn_entitylinkchatconfiguration](#BKMK_business_unit_msdyn_entitylinkchatconfiguration)
- [lk_msdyn_entitylinkchatconfiguration_createdby](#BKMK_lk_msdyn_entitylinkchatconfiguration_createdby)
- [lk_msdyn_entitylinkchatconfiguration_createdonbehalfby](#BKMK_lk_msdyn_entitylinkchatconfiguration_createdonbehalfby)
- [lk_msdyn_entitylinkchatconfiguration_modifiedby](#BKMK_lk_msdyn_entitylinkchatconfiguration_modifiedby)
- [lk_msdyn_entitylinkchatconfiguration_modifiedonbehalfby](#BKMK_lk_msdyn_entitylinkchatconfiguration_modifiedonbehalfby)
- [msdyn_entity_msdyn_entitylinkchatconfiguration](#BKMK_msdyn_entity_msdyn_entitylinkchatconfiguration)
- [owner_msdyn_entitylinkchatconfiguration](#BKMK_owner_msdyn_entitylinkchatconfiguration)
- [team_msdyn_entitylinkchatconfiguration](#BKMK_team_msdyn_entitylinkchatconfiguration)
- [user_msdyn_entitylinkchatconfiguration](#BKMK_user_msdyn_entitylinkchatconfiguration)

### <a name="BKMK_business_unit_msdyn_entitylinkchatconfiguration"></a> business_unit_msdyn_entitylinkchatconfiguration

One-To-Many Relationship: [businessunit business_unit_msdyn_entitylinkchatconfiguration](businessunit.md#BKMK_business_unit_msdyn_entitylinkchatconfiguration)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_entitylinkchatconfiguration_createdby"></a> lk_msdyn_entitylinkchatconfiguration_createdby

One-To-Many Relationship: [systemuser lk_msdyn_entitylinkchatconfiguration_createdby](systemuser.md#BKMK_lk_msdyn_entitylinkchatconfiguration_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_entitylinkchatconfiguration_createdonbehalfby"></a> lk_msdyn_entitylinkchatconfiguration_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_entitylinkchatconfiguration_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_entitylinkchatconfiguration_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_entitylinkchatconfiguration_modifiedby"></a> lk_msdyn_entitylinkchatconfiguration_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_entitylinkchatconfiguration_modifiedby](systemuser.md#BKMK_lk_msdyn_entitylinkchatconfiguration_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_entitylinkchatconfiguration_modifiedonbehalfby"></a> lk_msdyn_entitylinkchatconfiguration_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_entitylinkchatconfiguration_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_entitylinkchatconfiguration_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_entity_msdyn_entitylinkchatconfiguration"></a> msdyn_entity_msdyn_entitylinkchatconfiguration

One-To-Many Relationship: [entity msdyn_entity_msdyn_entitylinkchatconfiguration](entity.md#BKMK_msdyn_entity_msdyn_entitylinkchatconfiguration)

|Property|Value|
|---|---|
|ReferencedEntity|`entity`|
|ReferencedAttribute|`entityid`|
|ReferencingAttribute|`msdyn_entitytype`|
|ReferencingEntityNavigationPropertyName|`msdyn_entitytype`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_entitylinkchatconfiguration"></a> owner_msdyn_entitylinkchatconfiguration

One-To-Many Relationship: [owner owner_msdyn_entitylinkchatconfiguration](owner.md#BKMK_owner_msdyn_entitylinkchatconfiguration)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_entitylinkchatconfiguration"></a> team_msdyn_entitylinkchatconfiguration

One-To-Many Relationship: [team team_msdyn_entitylinkchatconfiguration](team.md#BKMK_team_msdyn_entitylinkchatconfiguration)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_entitylinkchatconfiguration"></a> user_msdyn_entitylinkchatconfiguration

One-To-Many Relationship: [systemuser user_msdyn_entitylinkchatconfiguration](systemuser.md#BKMK_user_msdyn_entitylinkchatconfiguration)

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

- [msdyn_entitylinkchatconfiguration_AsyncOperations](#BKMK_msdyn_entitylinkchatconfiguration_AsyncOperations)
- [msdyn_entitylinkchatconfiguration_BulkDeleteFailures](#BKMK_msdyn_entitylinkchatconfiguration_BulkDeleteFailures)
- [msdyn_entitylinkchatconfiguration_DuplicateBaseRecord](#BKMK_msdyn_entitylinkchatconfiguration_DuplicateBaseRecord)
- [msdyn_entitylinkchatconfiguration_DuplicateMatchingRecord](#BKMK_msdyn_entitylinkchatconfiguration_DuplicateMatchingRecord)
- [msdyn_entitylinkchatconfiguration_MailboxTrackingFolders](#BKMK_msdyn_entitylinkchatconfiguration_MailboxTrackingFolders)
- [msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses](#BKMK_msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses)
- [msdyn_entitylinkchatconfiguration_ProcessSession](#BKMK_msdyn_entitylinkchatconfiguration_ProcessSession)
- [msdyn_entitylinkchatconfiguration_SyncErrors](#BKMK_msdyn_entitylinkchatconfiguration_SyncErrors)

### <a name="BKMK_msdyn_entitylinkchatconfiguration_AsyncOperations"></a> msdyn_entitylinkchatconfiguration_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_entitylinkchatconfiguration_AsyncOperations](asyncoperation.md#BKMK_msdyn_entitylinkchatconfiguration_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_entitylinkchatconfiguration_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_entitylinkchatconfiguration_BulkDeleteFailures"></a> msdyn_entitylinkchatconfiguration_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_entitylinkchatconfiguration_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_entitylinkchatconfiguration_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_entitylinkchatconfiguration_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_entitylinkchatconfiguration_DuplicateBaseRecord"></a> msdyn_entitylinkchatconfiguration_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord msdyn_entitylinkchatconfiguration_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_entitylinkchatconfiguration_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_entitylinkchatconfiguration_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_entitylinkchatconfiguration_DuplicateMatchingRecord"></a> msdyn_entitylinkchatconfiguration_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord msdyn_entitylinkchatconfiguration_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_entitylinkchatconfiguration_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_entitylinkchatconfiguration_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_entitylinkchatconfiguration_MailboxTrackingFolders"></a> msdyn_entitylinkchatconfiguration_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_entitylinkchatconfiguration_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_entitylinkchatconfiguration_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_entitylinkchatconfiguration_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses"></a> msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_entitylinkchatconfiguration_ProcessSession"></a> msdyn_entitylinkchatconfiguration_ProcessSession

Many-To-One Relationship: [processsession msdyn_entitylinkchatconfiguration_ProcessSession](processsession.md#BKMK_msdyn_entitylinkchatconfiguration_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_entitylinkchatconfiguration_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_entitylinkchatconfiguration_SyncErrors"></a> msdyn_entitylinkchatconfiguration_SyncErrors

Many-To-One Relationship: [syncerror msdyn_entitylinkchatconfiguration_SyncErrors](syncerror.md#BKMK_msdyn_entitylinkchatconfiguration_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_entitylinkchatconfiguration_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_entitylinkchatconfiguration?displayProperty=fullName>
