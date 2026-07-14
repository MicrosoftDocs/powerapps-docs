---
title: "Shortcut (mspp_shortcut) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Shortcut (mspp_shortcut) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Shortcut (mspp_shortcut) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Shortcut (mspp_shortcut) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mspp_shortcuts<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mspp_shortcuts(*mspp_shortcutid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /mspp_shortcuts(*mspp_shortcutid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /mspp_shortcuts<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /mspp_shortcuts(*mspp_shortcutid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mspp_shortcuts(*mspp_shortcutid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Shortcut (mspp_shortcut) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Shortcut (mspp_shortcut) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Shortcut** |
| **DisplayCollectionName** | **Shortcuts** |
| **SchemaName** | `mspp_shortcut` |
| **CollectionSchemaName** | `mspp_shortcuts` |
| **EntitySetName** | `mspp_shortcuts`|
| **LogicalName** | `mspp_shortcut` |
| **LogicalCollectionName** | `mspp_shortcuts` |
| **PrimaryIdAttribute** | `mspp_shortcutid` |
| **PrimaryNameAttribute** |`mspp_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_description](#BKMK_mspp_description)
- [mspp_disabletargetvalidation](#BKMK_mspp_disabletargetvalidation)
- [mspp_displayorder](#BKMK_mspp_displayorder)
- [mspp_externalurl](#BKMK_mspp_externalurl)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_parentpage_webpageid](#BKMK_mspp_parentpage_webpageid)
- [mspp_shortcutId](#BKMK_mspp_shortcutId)
- [mspp_title](#BKMK_mspp_title)
- [mspp_webfileid](#BKMK_mspp_webfileid)
- [mspp_webpageid](#BKMK_mspp_webpageid)
- [mspp_websiteid](#BKMK_mspp_websiteid)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)

### <a name="BKMK_mspp_createdby"></a> mspp_createdby

|Property|Value|
|---|---|
|Description|**Shows who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_mspp_createdon"></a> mspp_createdon

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was created.**|
|DisplayName|**Created On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_createdon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_mspp_description"></a> mspp_description

|Property|Value|
|---|---|
|Description||
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_mspp_disabletargetvalidation"></a> mspp_disabletargetvalidation

|Property|Value|
|---|---|
|Description||
|DisplayName|**Disable Shortcut Target Validation**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_disabletargetvalidation`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_shortcut_mspp_disabletargetvalidation`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_displayorder"></a> mspp_displayorder

|Property|Value|
|---|---|
|Description||
|DisplayName|**Display Order**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_displayorder`|
|RequiredLevel|Recommended|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_mspp_externalurl"></a> mspp_externalurl

|Property|Value|
|---|---|
|Description||
|DisplayName|**External URL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_externalurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_modifiedby"></a> mspp_modifiedby

|Property|Value|
|---|---|
|Description|**Shows who last updated the record.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_mspp_modifiedon"></a> mspp_modifiedon

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_modifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_mspp_name"></a> mspp_name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_parentpage_webpageid"></a> mspp_parentpage_webpageid

|Property|Value|
|---|---|
|Description|**Unique identifier for Web Page associated with Shortcut.**|
|DisplayName|**Parent Page**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_parentpage_webpageid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_webpage|

### <a name="BKMK_mspp_shortcutId"></a> mspp_shortcutId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Shortcut**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspp_shortcutid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_mspp_title"></a> mspp_title

|Property|Value|
|---|---|
|Description||
|DisplayName|**Title**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_title`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_webfileid"></a> mspp_webfileid

|Property|Value|
|---|---|
|Description|**Web File that is pointed to by the shortcut**|
|DisplayName|**Web File**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_webfileid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_webfile|

### <a name="BKMK_mspp_webpageid"></a> mspp_webpageid

|Property|Value|
|---|---|
|Description|**The web page that the shortcut points to**|
|DisplayName|**Web Page**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_webpageid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_webpage|

### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|---|---|
|Description|**Unique identifier for Website associated with Shortcut.**|
|DisplayName|**Website**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_websiteid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_website|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Shortcut**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`mspp_shortcut_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Shortcut**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`mspp_shortcut_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|


## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [mspp_parentwebpage_shortcut](#BKMK_mspp_parentwebpage_shortcut)
- [mspp_systemuser_mspp_shortcut_createdby](#BKMK_mspp_systemuser_mspp_shortcut_createdby)
- [mspp_systemuser_mspp_shortcut_modifiedby](#BKMK_mspp_systemuser_mspp_shortcut_modifiedby)
- [mspp_webfile_shortcut](#BKMK_mspp_webfile_shortcut)
- [mspp_webpage_shortcut](#BKMK_mspp_webpage_shortcut)
- [mspp_website_shortcut](#BKMK_mspp_website_shortcut)

### <a name="BKMK_mspp_parentwebpage_shortcut"></a> mspp_parentwebpage_shortcut

One-To-Many Relationship: [mspp_webpage mspp_parentwebpage_shortcut](mspp_webpage.md#BKMK_mspp_parentwebpage_shortcut)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webpage`|
|ReferencedAttribute|`mspp_webpageid`|
|ReferencingAttribute|`mspp_parentpage_webpageid`|
|ReferencingEntityNavigationPropertyName|`mspp_ParentPage_webpageId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_shortcut_createdby"></a> mspp_systemuser_mspp_shortcut_createdby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_shortcut_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_shortcut_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_createdby`|
|ReferencingEntityNavigationPropertyName|`mspp_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_shortcut_modifiedby"></a> mspp_systemuser_mspp_shortcut_modifiedby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_shortcut_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_shortcut_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_modifiedby`|
|ReferencingEntityNavigationPropertyName|`mspp_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webfile_shortcut"></a> mspp_webfile_shortcut

One-To-Many Relationship: [mspp_webfile mspp_webfile_shortcut](mspp_webfile.md#BKMK_mspp_webfile_shortcut)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webfile`|
|ReferencedAttribute|`mspp_webfileid`|
|ReferencingAttribute|`mspp_webfileid`|
|ReferencingEntityNavigationPropertyName|`mspp_WebFileId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webpage_shortcut"></a> mspp_webpage_shortcut

One-To-Many Relationship: [mspp_webpage mspp_webpage_shortcut](mspp_webpage.md#BKMK_mspp_webpage_shortcut)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webpage`|
|ReferencedAttribute|`mspp_webpageid`|
|ReferencingAttribute|`mspp_webpageid`|
|ReferencingEntityNavigationPropertyName|`mspp_WebPageId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_website_shortcut"></a> mspp_website_shortcut

One-To-Many Relationship: [mspp_website mspp_website_shortcut](mspp_website.md#BKMK_mspp_website_shortcut)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_website`|
|ReferencedAttribute|`mspp_websiteid`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencingEntityNavigationPropertyName|`mspp_WebsiteId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [mspp_shortcut_ActivityPointers](#BKMK_mspp_shortcut_ActivityPointers)
- [mspp_shortcut_adx_inviteredemptions](#BKMK_mspp_shortcut_adx_inviteredemptions)
- [mspp_shortcut_adx_portalcomments](#BKMK_mspp_shortcut_adx_portalcomments)
- [mspp_shortcut_Appointments](#BKMK_mspp_shortcut_Appointments)
- [mspp_shortcut_chats](#BKMK_mspp_shortcut_chats)
- [mspp_shortcut_connections1](#BKMK_mspp_shortcut_connections1)
- [mspp_shortcut_connections2](#BKMK_mspp_shortcut_connections2)
- [mspp_shortcut_Emails](#BKMK_mspp_shortcut_Emails)
- [mspp_shortcut_Faxes](#BKMK_mspp_shortcut_Faxes)
- [mspp_shortcut_Letters](#BKMK_mspp_shortcut_Letters)
- [mspp_shortcut_PhoneCalls](#BKMK_mspp_shortcut_PhoneCalls)
- [mspp_shortcut_RecurringAppointmentMasters](#BKMK_mspp_shortcut_RecurringAppointmentMasters)
- [mspp_shortcut_SocialActivities](#BKMK_mspp_shortcut_SocialActivities)
- [mspp_shortcut_Tasks](#BKMK_mspp_shortcut_Tasks)

### <a name="BKMK_mspp_shortcut_ActivityPointers"></a> mspp_shortcut_ActivityPointers

Many-To-One Relationship: [activitypointer mspp_shortcut_ActivityPointers](activitypointer.md#BKMK_mspp_shortcut_ActivityPointers)

|Property|Value|
|---|---|
|ReferencingEntity|`activitypointer`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_shortcut_ActivityPointers`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_shortcut_adx_inviteredemptions"></a> mspp_shortcut_adx_inviteredemptions

Many-To-One Relationship: [adx_inviteredemption mspp_shortcut_adx_inviteredemptions](adx_inviteredemption.md#BKMK_mspp_shortcut_adx_inviteredemptions)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_inviteredemption`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_shortcut_adx_inviteredemptions`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_shortcut_adx_portalcomments"></a> mspp_shortcut_adx_portalcomments

Many-To-One Relationship: [adx_portalcomment mspp_shortcut_adx_portalcomments](adx_portalcomment.md#BKMK_mspp_shortcut_adx_portalcomments)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_portalcomment`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_shortcut_adx_portalcomments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_shortcut_Appointments"></a> mspp_shortcut_Appointments

Many-To-One Relationship: [appointment mspp_shortcut_Appointments](appointment.md#BKMK_mspp_shortcut_Appointments)

|Property|Value|
|---|---|
|ReferencingEntity|`appointment`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_shortcut_Appointments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_shortcut_chats"></a> mspp_shortcut_chats

Many-To-One Relationship: [chat mspp_shortcut_chats](chat.md#BKMK_mspp_shortcut_chats)

|Property|Value|
|---|---|
|ReferencingEntity|`chat`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_shortcut_chats`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_shortcut_connections1"></a> mspp_shortcut_connections1

Many-To-One Relationship: [connection mspp_shortcut_connections1](connection.md#BKMK_mspp_shortcut_connections1)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record1id`|
|ReferencedEntityNavigationPropertyName|`mspp_shortcut_connections1`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_shortcut_connections2"></a> mspp_shortcut_connections2

Many-To-One Relationship: [connection mspp_shortcut_connections2](connection.md#BKMK_mspp_shortcut_connections2)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record2id`|
|ReferencedEntityNavigationPropertyName|`mspp_shortcut_connections2`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_shortcut_Emails"></a> mspp_shortcut_Emails

Many-To-One Relationship: [email mspp_shortcut_Emails](email.md#BKMK_mspp_shortcut_Emails)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_shortcut_Emails`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_shortcut_Faxes"></a> mspp_shortcut_Faxes

Many-To-One Relationship: [fax mspp_shortcut_Faxes](fax.md#BKMK_mspp_shortcut_Faxes)

|Property|Value|
|---|---|
|ReferencingEntity|`fax`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_shortcut_Faxes`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_shortcut_Letters"></a> mspp_shortcut_Letters

Many-To-One Relationship: [letter mspp_shortcut_Letters](letter.md#BKMK_mspp_shortcut_Letters)

|Property|Value|
|---|---|
|ReferencingEntity|`letter`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_shortcut_Letters`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_shortcut_PhoneCalls"></a> mspp_shortcut_PhoneCalls

Many-To-One Relationship: [phonecall mspp_shortcut_PhoneCalls](phonecall.md#BKMK_mspp_shortcut_PhoneCalls)

|Property|Value|
|---|---|
|ReferencingEntity|`phonecall`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_shortcut_PhoneCalls`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_shortcut_RecurringAppointmentMasters"></a> mspp_shortcut_RecurringAppointmentMasters

Many-To-One Relationship: [recurringappointmentmaster mspp_shortcut_RecurringAppointmentMasters](recurringappointmentmaster.md#BKMK_mspp_shortcut_RecurringAppointmentMasters)

|Property|Value|
|---|---|
|ReferencingEntity|`recurringappointmentmaster`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_shortcut_RecurringAppointmentMasters`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_shortcut_SocialActivities"></a> mspp_shortcut_SocialActivities

Many-To-One Relationship: [socialactivity mspp_shortcut_SocialActivities](socialactivity.md#BKMK_mspp_shortcut_SocialActivities)

|Property|Value|
|---|---|
|ReferencingEntity|`socialactivity`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_shortcut_SocialActivities`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_shortcut_Tasks"></a> mspp_shortcut_Tasks

Many-To-One Relationship: [task mspp_shortcut_Tasks](task.md#BKMK_mspp_shortcut_Tasks)

|Property|Value|
|---|---|
|ReferencingEntity|`task`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_shortcut_Tasks`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mspp_shortcut?displayProperty=fullName>
