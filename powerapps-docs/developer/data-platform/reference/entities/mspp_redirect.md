---
title: "Redirect (mspp_redirect) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Redirect (mspp_redirect) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Redirect (mspp_redirect) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Redirect (mspp_redirect) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mspp_redirects<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mspp_redirects(*mspp_redirectid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /mspp_redirects(*mspp_redirectid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /mspp_redirects<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /mspp_redirects(*mspp_redirectid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mspp_redirects(*mspp_redirectid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Redirect (mspp_redirect) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Redirect (mspp_redirect) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Redirect** |
| **DisplayCollectionName** | **Redirects** |
| **SchemaName** | `mspp_redirect` |
| **CollectionSchemaName** | `mspp_redirects` |
| **EntitySetName** | `mspp_redirects`|
| **LogicalName** | `mspp_redirect` |
| **LogicalCollectionName** | `mspp_redirects` |
| **PrimaryIdAttribute** | `mspp_redirectid` |
| **PrimaryNameAttribute** |`mspp_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_inboundurl](#BKMK_mspp_inboundurl)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_redirectId](#BKMK_mspp_redirectId)
- [mspp_redirecturl](#BKMK_mspp_redirecturl)
- [mspp_sitemarkerid](#BKMK_mspp_sitemarkerid)
- [mspp_statuscode](#BKMK_mspp_statuscode)
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

### <a name="BKMK_mspp_inboundurl"></a> mspp_inboundurl

|Property|Value|
|---|---|
|Description|**The path to redirect visitors from**|
|DisplayName|**Inbound URL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_inboundurl`|
|RequiredLevel|ApplicationRequired|
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

### <a name="BKMK_mspp_redirectId"></a> mspp_redirectId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Redirect**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspp_redirectid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_mspp_redirecturl"></a> mspp_redirecturl

|Property|Value|
|---|---|
|Description|**The path to redirect visitors to**|
|DisplayName|**Redirect URL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_redirecturl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_sitemarkerid"></a> mspp_sitemarkerid

|Property|Value|
|---|---|
|Description|**Unique identifier for Site Marker associated with Redirect.**|
|DisplayName|**Site Marker**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_sitemarkerid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_sitemarker|

### <a name="BKMK_mspp_statuscode"></a> mspp_statuscode

|Property|Value|
|---|---|
|Description||
|DisplayName|**Status Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_statuscode`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|302|
|GlobalChoiceName|`mspp_redirect_mspp_statuscode`|

#### mspp_statuscode Choices/Options

|Value|Label|
|---|---|
|301|**301 (Permanent Redirect)**|
|302|**302 (Temporary Redirect)**|

### <a name="BKMK_mspp_webpageid"></a> mspp_webpageid

|Property|Value|
|---|---|
|Description|**Unique identifier for Web Page associated with Redirect.**|
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
|Description|**Unique identifier for Website associated with Redirect.**|
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
|Description|**Status of the Redirect**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`mspp_redirect_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Redirect**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`mspp_redirect_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|


## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [mspp_sitemarker_redirect](#BKMK_mspp_sitemarker_redirect)
- [mspp_systemuser_mspp_redirect_createdby](#BKMK_mspp_systemuser_mspp_redirect_createdby)
- [mspp_systemuser_mspp_redirect_modifiedby](#BKMK_mspp_systemuser_mspp_redirect_modifiedby)
- [mspp_webpage_redirect](#BKMK_mspp_webpage_redirect)
- [mspp_website_redirect](#BKMK_mspp_website_redirect)

### <a name="BKMK_mspp_sitemarker_redirect"></a> mspp_sitemarker_redirect

One-To-Many Relationship: [mspp_sitemarker mspp_sitemarker_redirect](mspp_sitemarker.md#BKMK_mspp_sitemarker_redirect)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_sitemarker`|
|ReferencedAttribute|`mspp_sitemarkerid`|
|ReferencingAttribute|`mspp_sitemarkerid`|
|ReferencingEntityNavigationPropertyName|`mspp_sitemarkerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_redirect_createdby"></a> mspp_systemuser_mspp_redirect_createdby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_redirect_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_redirect_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_createdby`|
|ReferencingEntityNavigationPropertyName|`mspp_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_redirect_modifiedby"></a> mspp_systemuser_mspp_redirect_modifiedby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_redirect_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_redirect_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_modifiedby`|
|ReferencingEntityNavigationPropertyName|`mspp_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webpage_redirect"></a> mspp_webpage_redirect

One-To-Many Relationship: [mspp_webpage mspp_webpage_redirect](mspp_webpage.md#BKMK_mspp_webpage_redirect)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webpage`|
|ReferencedAttribute|`mspp_webpageid`|
|ReferencingAttribute|`mspp_webpageid`|
|ReferencingEntityNavigationPropertyName|`mspp_webpageid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_website_redirect"></a> mspp_website_redirect

One-To-Many Relationship: [mspp_website mspp_website_redirect](mspp_website.md#BKMK_mspp_website_redirect)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_website`|
|ReferencedAttribute|`mspp_websiteid`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencingEntityNavigationPropertyName|`mspp_websiteid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [mspp_redirect_ActivityPointers](#BKMK_mspp_redirect_ActivityPointers)
- [mspp_redirect_adx_inviteredemptions](#BKMK_mspp_redirect_adx_inviteredemptions)
- [mspp_redirect_adx_portalcomments](#BKMK_mspp_redirect_adx_portalcomments)
- [mspp_redirect_Appointments](#BKMK_mspp_redirect_Appointments)
- [mspp_redirect_chats](#BKMK_mspp_redirect_chats)
- [mspp_redirect_Emails](#BKMK_mspp_redirect_Emails)
- [mspp_redirect_Faxes](#BKMK_mspp_redirect_Faxes)
- [mspp_redirect_Letters](#BKMK_mspp_redirect_Letters)
- [mspp_redirect_PhoneCalls](#BKMK_mspp_redirect_PhoneCalls)
- [mspp_redirect_RecurringAppointmentMasters](#BKMK_mspp_redirect_RecurringAppointmentMasters)
- [mspp_redirect_SocialActivities](#BKMK_mspp_redirect_SocialActivities)
- [mspp_redirect_Tasks](#BKMK_mspp_redirect_Tasks)

### <a name="BKMK_mspp_redirect_ActivityPointers"></a> mspp_redirect_ActivityPointers

Many-To-One Relationship: [activitypointer mspp_redirect_ActivityPointers](activitypointer.md#BKMK_mspp_redirect_ActivityPointers)

|Property|Value|
|---|---|
|ReferencingEntity|`activitypointer`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_redirect_ActivityPointers`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_redirect_adx_inviteredemptions"></a> mspp_redirect_adx_inviteredemptions

Many-To-One Relationship: [adx_inviteredemption mspp_redirect_adx_inviteredemptions](adx_inviteredemption.md#BKMK_mspp_redirect_adx_inviteredemptions)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_inviteredemption`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_redirect_adx_inviteredemptions`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_redirect_adx_portalcomments"></a> mspp_redirect_adx_portalcomments

Many-To-One Relationship: [adx_portalcomment mspp_redirect_adx_portalcomments](adx_portalcomment.md#BKMK_mspp_redirect_adx_portalcomments)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_portalcomment`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_redirect_adx_portalcomments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_redirect_Appointments"></a> mspp_redirect_Appointments

Many-To-One Relationship: [appointment mspp_redirect_Appointments](appointment.md#BKMK_mspp_redirect_Appointments)

|Property|Value|
|---|---|
|ReferencingEntity|`appointment`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_redirect_Appointments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_redirect_chats"></a> mspp_redirect_chats

Many-To-One Relationship: [chat mspp_redirect_chats](chat.md#BKMK_mspp_redirect_chats)

|Property|Value|
|---|---|
|ReferencingEntity|`chat`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_redirect_chats`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_redirect_Emails"></a> mspp_redirect_Emails

Many-To-One Relationship: [email mspp_redirect_Emails](email.md#BKMK_mspp_redirect_Emails)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_redirect_Emails`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_redirect_Faxes"></a> mspp_redirect_Faxes

Many-To-One Relationship: [fax mspp_redirect_Faxes](fax.md#BKMK_mspp_redirect_Faxes)

|Property|Value|
|---|---|
|ReferencingEntity|`fax`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_redirect_Faxes`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_redirect_Letters"></a> mspp_redirect_Letters

Many-To-One Relationship: [letter mspp_redirect_Letters](letter.md#BKMK_mspp_redirect_Letters)

|Property|Value|
|---|---|
|ReferencingEntity|`letter`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_redirect_Letters`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_redirect_PhoneCalls"></a> mspp_redirect_PhoneCalls

Many-To-One Relationship: [phonecall mspp_redirect_PhoneCalls](phonecall.md#BKMK_mspp_redirect_PhoneCalls)

|Property|Value|
|---|---|
|ReferencingEntity|`phonecall`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_redirect_PhoneCalls`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_redirect_RecurringAppointmentMasters"></a> mspp_redirect_RecurringAppointmentMasters

Many-To-One Relationship: [recurringappointmentmaster mspp_redirect_RecurringAppointmentMasters](recurringappointmentmaster.md#BKMK_mspp_redirect_RecurringAppointmentMasters)

|Property|Value|
|---|---|
|ReferencingEntity|`recurringappointmentmaster`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_redirect_RecurringAppointmentMasters`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_redirect_SocialActivities"></a> mspp_redirect_SocialActivities

Many-To-One Relationship: [socialactivity mspp_redirect_SocialActivities](socialactivity.md#BKMK_mspp_redirect_SocialActivities)

|Property|Value|
|---|---|
|ReferencingEntity|`socialactivity`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_redirect_SocialActivities`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_redirect_Tasks"></a> mspp_redirect_Tasks

Many-To-One Relationship: [task mspp_redirect_Tasks](task.md#BKMK_mspp_redirect_Tasks)

|Property|Value|
|---|---|
|ReferencingEntity|`task`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_redirect_Tasks`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mspp_redirect?displayProperty=fullName>
