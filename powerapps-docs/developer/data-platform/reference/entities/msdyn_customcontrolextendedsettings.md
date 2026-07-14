---
title: "Custom Control Extended Setting (msdyn_customcontrolextendedsettings) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Custom Control Extended Setting (msdyn_customcontrolextendedsettings) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Custom Control Extended Setting (msdyn_customcontrolextendedsettings) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Custom Control Extended Setting (msdyn_customcontrolextendedsettings) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_customcontrolextendedsettingses(*msdyn_customcontrolextendedsettingsid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_customcontrolextendedsettingses<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_customcontrolextendedsettingses(*msdyn_customcontrolextendedsettingsid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `ReplicateCreate`<br />Event: True | |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ReplicateDelete`<br />Event: True | |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ReplicateUpdate`<br />Event: True | |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retrieve`<br />Event: True |`GET` /msdyn_customcontrolextendedsettingses(*msdyn_customcontrolextendedsettingsid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_customcontrolextendedsettingses<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_customcontrolextendedsettingses(*msdyn_customcontrolextendedsettingsid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_customcontrolextendedsettingses(*msdyn_customcontrolextendedsettingsid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_customcontrolextendedsettingses(*msdyn_customcontrolextendedsettingsid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Custom Control Extended Setting (msdyn_customcontrolextendedsettings) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Custom Control Extended Setting (msdyn_customcontrolextendedsettings) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Custom Control Extended Setting** |
| **DisplayCollectionName** | **CustomControl Extended Settings** |
| **SchemaName** | `msdyn_customcontrolextendedsettings` |
| **CollectionSchemaName** | `msdyn_customcontrolextendedsettingses` |
| **EntitySetName** | `msdyn_customcontrolextendedsettingses`|
| **LogicalName** | `msdyn_customcontrolextendedsettings` |
| **LogicalCollectionName** | `msdyn_customcontrolextendedsettingses` |
| **PrimaryIdAttribute** | `msdyn_customcontrolextendedsettingsid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_copilothub_settings](#BKMK_msdyn_copilothub_settings)
- [msdyn_customcontrolextendedsettingsId](#BKMK_msdyn_customcontrolextendedsettingsId)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_rte_userpersonalizationsettings](#BKMK_msdyn_rte_userpersonalizationsettings)
- [msdyn_timeline_displaylayoutoption](#BKMK_msdyn_timeline_displaylayoutoption)
- [msdyn_timelineWall_bookmarks](#BKMK_msdyn_timelineWall_bookmarks)
- [msdyn_timelineWall_isAutoExpanded](#BKMK_msdyn_timelineWall_isAutoExpanded)
- [msdyn_timelineWall_isFilterPaneOpen](#BKMK_msdyn_timelineWall_isFilterPaneOpen)
- [msdyn_timelineWall_isSortOrderNewerToOlder](#BKMK_msdyn_timelineWall_isSortOrderNewerToOlder)
- [msdyn_timelineWall_searchTermApplied](#BKMK_msdyn_timelineWall_searchTermApplied)
- [msdyn_timelineWall_userFilters](#BKMK_msdyn_timelineWall_userFilters)
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

### <a name="BKMK_msdyn_copilothub_settings"></a> msdyn_copilothub_settings

|Property|Value|
|---|---|
|Description|**User data for the Copilot Hub control**|
|DisplayName|**Copilot Hub settings**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_copilothub_settings`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|65536|

### <a name="BKMK_msdyn_customcontrolextendedsettingsId"></a> msdyn_customcontrolextendedsettingsId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Custom Control Extended Setting**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_customcontrolextendedsettingsid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
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
|MaxLength|100|

### <a name="BKMK_msdyn_rte_userpersonalizationsettings"></a> msdyn_rte_userpersonalizationsettings

|Property|Value|
|---|---|
|Description|**User configured personal settings for Rich Text Editor**|
|DisplayName|**RTE User Personalization Settings**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_rte_userpersonalizationsettings`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|65536|

### <a name="BKMK_msdyn_timeline_displaylayoutoption"></a> msdyn_timeline_displaylayoutoption

|Property|Value|
|---|---|
|Description|**User configured display layout option for the Timeline control**|
|DisplayName|**Timeline display layout options**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_timeline_displaylayoutoption`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|65536|

### <a name="BKMK_msdyn_timelineWall_bookmarks"></a> msdyn_timelineWall_bookmarks

|Property|Value|
|---|---|
|Description|**User configured filter settings for TimelineWall**|
|DisplayName|**Bookmarks**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_timelineWall_bookmarks`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|65536|

### <a name="BKMK_msdyn_timelineWall_isAutoExpanded"></a> msdyn_timelineWall_isAutoExpanded

|Property|Value|
|---|---|
|Description|**User configured expand state for TimelineWall**|
|DisplayName|**IsAutoExpanded**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_timelineWall_isAutoExpanded`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_customcontrolsettings_msdyn_timelinewall_isautoexpanded`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_timelineWall_isFilterPaneOpen"></a> msdyn_timelineWall_isFilterPaneOpen

|Property|Value|
|---|---|
|Description|**Will the filter pane open by default on TimelineWall load**|
|DisplayName|**Is Filter Pane Open**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_timelineWall_isFilterPaneOpen`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_customcontrolextendedsettings_msdyn_timelinewall_isfilterpaneopen`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_timelineWall_isSortOrderNewerToOlder"></a> msdyn_timelineWall_isSortOrderNewerToOlder

|Property|Value|
|---|---|
|Description|**Is TimelineWall set to sort by newer to older records**|
|DisplayName|**Is Sort Order Newer To Older for TimelineWall**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_timelineWall_isSortOrderNewerToOlder`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_customcontrolextendedsettings_msdyn_timelinewall_issortordernewertoolder`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_timelineWall_searchTermApplied"></a> msdyn_timelineWall_searchTermApplied

|Property|Value|
|---|---|
|Description|**Search term to be applied on TimelineWall load**|
|DisplayName|**Search Term Applied**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_timelineWall_searchTermApplied`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_msdyn_timelineWall_userFilters"></a> msdyn_timelineWall_userFilters

|Property|Value|
|---|---|
|Description|**User configured filter settings for TimelineWall**|
|DisplayName|**User Filters**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_timelineWall_userFilters`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|65536|

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
|Description|**Status of the Timeline Wall Extended Setting**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_customcontrolextendedsettings_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Timeline Wall Extended Setting**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_customcontrolextendedsettings_statuscode`|

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

- [business_unit_msdyn_customcontrolextendedsettings](#BKMK_business_unit_msdyn_customcontrolextendedsettings)
- [lk_msdyn_customcontrolextendedsettings_createdby](#BKMK_lk_msdyn_customcontrolextendedsettings_createdby)
- [lk_msdyn_customcontrolextendedsettings_createdonbehalfby](#BKMK_lk_msdyn_customcontrolextendedsettings_createdonbehalfby)
- [lk_msdyn_customcontrolextendedsettings_modifiedby](#BKMK_lk_msdyn_customcontrolextendedsettings_modifiedby)
- [lk_msdyn_customcontrolextendedsettings_modifiedonbehalfby](#BKMK_lk_msdyn_customcontrolextendedsettings_modifiedonbehalfby)
- [owner_msdyn_customcontrolextendedsettings](#BKMK_owner_msdyn_customcontrolextendedsettings)
- [team_msdyn_customcontrolextendedsettings](#BKMK_team_msdyn_customcontrolextendedsettings)
- [user_msdyn_customcontrolextendedsettings](#BKMK_user_msdyn_customcontrolextendedsettings)

### <a name="BKMK_business_unit_msdyn_customcontrolextendedsettings"></a> business_unit_msdyn_customcontrolextendedsettings

One-To-Many Relationship: [businessunit business_unit_msdyn_customcontrolextendedsettings](businessunit.md#BKMK_business_unit_msdyn_customcontrolextendedsettings)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_customcontrolextendedsettings_createdby"></a> lk_msdyn_customcontrolextendedsettings_createdby

One-To-Many Relationship: [systemuser lk_msdyn_customcontrolextendedsettings_createdby](systemuser.md#BKMK_lk_msdyn_customcontrolextendedsettings_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_customcontrolextendedsettings_createdonbehalfby"></a> lk_msdyn_customcontrolextendedsettings_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_customcontrolextendedsettings_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_customcontrolextendedsettings_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_customcontrolextendedsettings_modifiedby"></a> lk_msdyn_customcontrolextendedsettings_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_customcontrolextendedsettings_modifiedby](systemuser.md#BKMK_lk_msdyn_customcontrolextendedsettings_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_customcontrolextendedsettings_modifiedonbehalfby"></a> lk_msdyn_customcontrolextendedsettings_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_customcontrolextendedsettings_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_customcontrolextendedsettings_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_customcontrolextendedsettings"></a> owner_msdyn_customcontrolextendedsettings

One-To-Many Relationship: [owner owner_msdyn_customcontrolextendedsettings](owner.md#BKMK_owner_msdyn_customcontrolextendedsettings)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_customcontrolextendedsettings"></a> team_msdyn_customcontrolextendedsettings

One-To-Many Relationship: [team team_msdyn_customcontrolextendedsettings](team.md#BKMK_team_msdyn_customcontrolextendedsettings)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_customcontrolextendedsettings"></a> user_msdyn_customcontrolextendedsettings

One-To-Many Relationship: [systemuser user_msdyn_customcontrolextendedsettings](systemuser.md#BKMK_user_msdyn_customcontrolextendedsettings)

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

- [msdyn_customcontrolextendedsettings_AsyncOperations](#BKMK_msdyn_customcontrolextendedsettings_AsyncOperations)
- [msdyn_customcontrolextendedsettings_BulkDeleteFailures](#BKMK_msdyn_customcontrolextendedsettings_BulkDeleteFailures)
- [msdyn_customcontrolextendedsettings_DuplicateBaseRecord](#BKMK_msdyn_customcontrolextendedsettings_DuplicateBaseRecord)
- [msdyn_customcontrolextendedsettings_DuplicateMatchingRecord](#BKMK_msdyn_customcontrolextendedsettings_DuplicateMatchingRecord)
- [msdyn_customcontrolextendedsettings_MailboxTrackingFolders](#BKMK_msdyn_customcontrolextendedsettings_MailboxTrackingFolders)
- [msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses](#BKMK_msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses)
- [msdyn_customcontrolextendedsettings_ProcessSession](#BKMK_msdyn_customcontrolextendedsettings_ProcessSession)
- [msdyn_customcontrolextendedsettings_SyncErrors](#BKMK_msdyn_customcontrolextendedsettings_SyncErrors)

### <a name="BKMK_msdyn_customcontrolextendedsettings_AsyncOperations"></a> msdyn_customcontrolextendedsettings_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_customcontrolextendedsettings_AsyncOperations](asyncoperation.md#BKMK_msdyn_customcontrolextendedsettings_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_customcontrolextendedsettings_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_customcontrolextendedsettings_BulkDeleteFailures"></a> msdyn_customcontrolextendedsettings_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_customcontrolextendedsettings_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_customcontrolextendedsettings_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_customcontrolextendedsettings_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_customcontrolextendedsettings_DuplicateBaseRecord"></a> msdyn_customcontrolextendedsettings_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord msdyn_customcontrolextendedsettings_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_customcontrolextendedsettings_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_customcontrolextendedsettings_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_customcontrolextendedsettings_DuplicateMatchingRecord"></a> msdyn_customcontrolextendedsettings_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord msdyn_customcontrolextendedsettings_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_customcontrolextendedsettings_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_customcontrolextendedsettings_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_customcontrolextendedsettings_MailboxTrackingFolders"></a> msdyn_customcontrolextendedsettings_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_customcontrolextendedsettings_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_customcontrolextendedsettings_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_customcontrolextendedsettings_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses"></a> msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_customcontrolextendedsettings_ProcessSession"></a> msdyn_customcontrolextendedsettings_ProcessSession

Many-To-One Relationship: [processsession msdyn_customcontrolextendedsettings_ProcessSession](processsession.md#BKMK_msdyn_customcontrolextendedsettings_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_customcontrolextendedsettings_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_customcontrolextendedsettings_SyncErrors"></a> msdyn_customcontrolextendedsettings_SyncErrors

Many-To-One Relationship: [syncerror msdyn_customcontrolextendedsettings_SyncErrors](syncerror.md#BKMK_msdyn_customcontrolextendedsettings_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_customcontrolextendedsettings_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_customcontrolextendedsettings?displayProperty=fullName>
