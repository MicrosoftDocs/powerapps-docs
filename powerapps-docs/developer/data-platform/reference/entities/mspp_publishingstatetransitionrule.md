---
title: "Publishing State Transition Rule (mspp_publishingstatetransitionrule) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Publishing State Transition Rule (mspp_publishingstatetransitionrule) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Publishing State Transition Rule (mspp_publishingstatetransitionrule) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Publishing State Transition Rule (mspp_publishingstatetransitionrule) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mspp_publishingstatetransitionrules<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mspp_publishingstatetransitionrules(*mspp_publishingstatetransitionruleid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /mspp_publishingstatetransitionrules(*mspp_publishingstatetransitionruleid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /mspp_publishingstatetransitionrules<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /mspp_publishingstatetransitionrules(*mspp_publishingstatetransitionruleid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mspp_publishingstatetransitionrules(*mspp_publishingstatetransitionruleid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Publishing State Transition Rule (mspp_publishingstatetransitionrule) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Publishing State Transition Rule (mspp_publishingstatetransitionrule) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Publishing State Transition Rule** |
| **DisplayCollectionName** | **Publishing State Transition Rules** |
| **SchemaName** | `mspp_publishingstatetransitionrule` |
| **CollectionSchemaName** | `mspp_publishingstatetransitionrules` |
| **EntitySetName** | `mspp_publishingstatetransitionrules`|
| **LogicalName** | `mspp_publishingstatetransitionrule` |
| **LogicalCollectionName** | `mspp_publishingstatetransitionrules` |
| **PrimaryIdAttribute** | `mspp_publishingstatetransitionruleid` |
| **PrimaryNameAttribute** |`mspp_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_fromstate_publishingstateid](#BKMK_mspp_fromstate_publishingstateid)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_publishingstatetransitionruleId](#BKMK_mspp_publishingstatetransitionruleId)
- [mspp_tostate_publishingstateid](#BKMK_mspp_tostate_publishingstateid)
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

### <a name="BKMK_mspp_fromstate_publishingstateid"></a> mspp_fromstate_publishingstateid

|Property|Value|
|---|---|
|Description|**Unique identifier for Publishing State associated with Publishing State Transition Rule.**|
|DisplayName|**From State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_fromstate_publishingstateid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_publishingstate|

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

### <a name="BKMK_mspp_publishingstatetransitionruleId"></a> mspp_publishingstatetransitionruleId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Publishing State Transition Rule**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspp_publishingstatetransitionruleid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_mspp_tostate_publishingstateid"></a> mspp_tostate_publishingstateid

|Property|Value|
|---|---|
|Description|**Unique identifier for Publishing State associated with Publishing State Transition Rule.**|
|DisplayName|**To State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_tostate_publishingstateid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_publishingstate|

### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|---|---|
|Description|**Unique identifier for Website associated with Publishing State Transition Rule.**|
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
|Description|**Status of the Publishing State Transition Rule**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`mspp_publishingstatetransitionrule_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Publishing State Transition Rule**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`mspp_publishingstatetransitionrule_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|


## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [mspp_frompublishingstate_statetransition](#BKMK_mspp_frompublishingstate_statetransition)
- [mspp_systemuser_mspp_publishingstatetransitionrule_createdby](#BKMK_mspp_systemuser_mspp_publishingstatetransitionrule_createdby)
- [mspp_systemuser_mspp_publishingstatetransitionrule_modifiedby](#BKMK_mspp_systemuser_mspp_publishingstatetransitionrule_modifiedby)
- [mspp_topublishingstate_statetransition](#BKMK_mspp_topublishingstate_statetransition)
- [mspp_website_publishingstatetransition](#BKMK_mspp_website_publishingstatetransition)

### <a name="BKMK_mspp_frompublishingstate_statetransition"></a> mspp_frompublishingstate_statetransition

One-To-Many Relationship: [mspp_publishingstate mspp_frompublishingstate_statetransition](mspp_publishingstate.md#BKMK_mspp_frompublishingstate_statetransition)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_publishingstate`|
|ReferencedAttribute|`mspp_publishingstateid`|
|ReferencingAttribute|`mspp_fromstate_publishingstateid`|
|ReferencingEntityNavigationPropertyName|`mspp_FromState_PublishingStateId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_publishingstatetransitionrule_createdby"></a> mspp_systemuser_mspp_publishingstatetransitionrule_createdby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_publishingstatetransitionrule_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_publishingstatetransitionrule_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_createdby`|
|ReferencingEntityNavigationPropertyName|`mspp_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_publishingstatetransitionrule_modifiedby"></a> mspp_systemuser_mspp_publishingstatetransitionrule_modifiedby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_publishingstatetransitionrule_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_publishingstatetransitionrule_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_modifiedby`|
|ReferencingEntityNavigationPropertyName|`mspp_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_topublishingstate_statetransition"></a> mspp_topublishingstate_statetransition

One-To-Many Relationship: [mspp_publishingstate mspp_topublishingstate_statetransition](mspp_publishingstate.md#BKMK_mspp_topublishingstate_statetransition)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_publishingstate`|
|ReferencedAttribute|`mspp_publishingstateid`|
|ReferencingAttribute|`mspp_tostate_publishingstateid`|
|ReferencingEntityNavigationPropertyName|`mspp_ToState_PublishingStateId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_website_publishingstatetransition"></a> mspp_website_publishingstatetransition

One-To-Many Relationship: [mspp_website mspp_website_publishingstatetransition](mspp_website.md#BKMK_mspp_website_publishingstatetransition)

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

- [mspp_publishingstatetransitionrule_ActivityPointers](#BKMK_mspp_publishingstatetransitionrule_ActivityPointers)
- [mspp_publishingstatetransitionrule_adx_inviteredemptions](#BKMK_mspp_publishingstatetransitionrule_adx_inviteredemptions)
- [mspp_publishingstatetransitionrule_adx_portalcomments](#BKMK_mspp_publishingstatetransitionrule_adx_portalcomments)
- [mspp_publishingstatetransitionrule_Appointments](#BKMK_mspp_publishingstatetransitionrule_Appointments)
- [mspp_publishingstatetransitionrule_chats](#BKMK_mspp_publishingstatetransitionrule_chats)
- [mspp_publishingstatetransitionrule_connections1](#BKMK_mspp_publishingstatetransitionrule_connections1)
- [mspp_publishingstatetransitionrule_connections2](#BKMK_mspp_publishingstatetransitionrule_connections2)
- [mspp_publishingstatetransitionrule_Emails](#BKMK_mspp_publishingstatetransitionrule_Emails)
- [mspp_publishingstatetransitionrule_Faxes](#BKMK_mspp_publishingstatetransitionrule_Faxes)
- [mspp_publishingstatetransitionrule_Letters](#BKMK_mspp_publishingstatetransitionrule_Letters)
- [mspp_publishingstatetransitionrule_PhoneCalls](#BKMK_mspp_publishingstatetransitionrule_PhoneCalls)
- [mspp_publishingstatetransitionrule_RecurringAppointmentMasters](#BKMK_mspp_publishingstatetransitionrule_RecurringAppointmentMasters)
- [mspp_publishingstatetransitionrule_SocialActivities](#BKMK_mspp_publishingstatetransitionrule_SocialActivities)
- [mspp_publishingstatetransitionrule_Tasks](#BKMK_mspp_publishingstatetransitionrule_Tasks)

### <a name="BKMK_mspp_publishingstatetransitionrule_ActivityPointers"></a> mspp_publishingstatetransitionrule_ActivityPointers

Many-To-One Relationship: [activitypointer mspp_publishingstatetransitionrule_ActivityPointers](activitypointer.md#BKMK_mspp_publishingstatetransitionrule_ActivityPointers)

|Property|Value|
|---|---|
|ReferencingEntity|`activitypointer`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_publishingstatetransitionrule_ActivityPointers`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_publishingstatetransitionrule_adx_inviteredemptions"></a> mspp_publishingstatetransitionrule_adx_inviteredemptions

Many-To-One Relationship: [adx_inviteredemption mspp_publishingstatetransitionrule_adx_inviteredemptions](adx_inviteredemption.md#BKMK_mspp_publishingstatetransitionrule_adx_inviteredemptions)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_inviteredemption`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_publishingstatetransitionrule_adx_inviteredemptions`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_publishingstatetransitionrule_adx_portalcomments"></a> mspp_publishingstatetransitionrule_adx_portalcomments

Many-To-One Relationship: [adx_portalcomment mspp_publishingstatetransitionrule_adx_portalcomments](adx_portalcomment.md#BKMK_mspp_publishingstatetransitionrule_adx_portalcomments)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_portalcomment`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_publishingstatetransitionrule_adx_portalcomments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_publishingstatetransitionrule_Appointments"></a> mspp_publishingstatetransitionrule_Appointments

Many-To-One Relationship: [appointment mspp_publishingstatetransitionrule_Appointments](appointment.md#BKMK_mspp_publishingstatetransitionrule_Appointments)

|Property|Value|
|---|---|
|ReferencingEntity|`appointment`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_publishingstatetransitionrule_Appointments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_publishingstatetransitionrule_chats"></a> mspp_publishingstatetransitionrule_chats

Many-To-One Relationship: [chat mspp_publishingstatetransitionrule_chats](chat.md#BKMK_mspp_publishingstatetransitionrule_chats)

|Property|Value|
|---|---|
|ReferencingEntity|`chat`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_publishingstatetransitionrule_chats`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_publishingstatetransitionrule_connections1"></a> mspp_publishingstatetransitionrule_connections1

Many-To-One Relationship: [connection mspp_publishingstatetransitionrule_connections1](connection.md#BKMK_mspp_publishingstatetransitionrule_connections1)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record1id`|
|ReferencedEntityNavigationPropertyName|`mspp_publishingstatetransitionrule_connections1`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_publishingstatetransitionrule_connections2"></a> mspp_publishingstatetransitionrule_connections2

Many-To-One Relationship: [connection mspp_publishingstatetransitionrule_connections2](connection.md#BKMK_mspp_publishingstatetransitionrule_connections2)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record2id`|
|ReferencedEntityNavigationPropertyName|`mspp_publishingstatetransitionrule_connections2`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_publishingstatetransitionrule_Emails"></a> mspp_publishingstatetransitionrule_Emails

Many-To-One Relationship: [email mspp_publishingstatetransitionrule_Emails](email.md#BKMK_mspp_publishingstatetransitionrule_Emails)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_publishingstatetransitionrule_Emails`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_publishingstatetransitionrule_Faxes"></a> mspp_publishingstatetransitionrule_Faxes

Many-To-One Relationship: [fax mspp_publishingstatetransitionrule_Faxes](fax.md#BKMK_mspp_publishingstatetransitionrule_Faxes)

|Property|Value|
|---|---|
|ReferencingEntity|`fax`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_publishingstatetransitionrule_Faxes`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_publishingstatetransitionrule_Letters"></a> mspp_publishingstatetransitionrule_Letters

Many-To-One Relationship: [letter mspp_publishingstatetransitionrule_Letters](letter.md#BKMK_mspp_publishingstatetransitionrule_Letters)

|Property|Value|
|---|---|
|ReferencingEntity|`letter`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_publishingstatetransitionrule_Letters`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_publishingstatetransitionrule_PhoneCalls"></a> mspp_publishingstatetransitionrule_PhoneCalls

Many-To-One Relationship: [phonecall mspp_publishingstatetransitionrule_PhoneCalls](phonecall.md#BKMK_mspp_publishingstatetransitionrule_PhoneCalls)

|Property|Value|
|---|---|
|ReferencingEntity|`phonecall`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_publishingstatetransitionrule_PhoneCalls`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_publishingstatetransitionrule_RecurringAppointmentMasters"></a> mspp_publishingstatetransitionrule_RecurringAppointmentMasters

Many-To-One Relationship: [recurringappointmentmaster mspp_publishingstatetransitionrule_RecurringAppointmentMasters](recurringappointmentmaster.md#BKMK_mspp_publishingstatetransitionrule_RecurringAppointmentMasters)

|Property|Value|
|---|---|
|ReferencingEntity|`recurringappointmentmaster`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_publishingstatetransitionrule_RecurringAppointmentMasters`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_publishingstatetransitionrule_SocialActivities"></a> mspp_publishingstatetransitionrule_SocialActivities

Many-To-One Relationship: [socialactivity mspp_publishingstatetransitionrule_SocialActivities](socialactivity.md#BKMK_mspp_publishingstatetransitionrule_SocialActivities)

|Property|Value|
|---|---|
|ReferencingEntity|`socialactivity`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_publishingstatetransitionrule_SocialActivities`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_publishingstatetransitionrule_Tasks"></a> mspp_publishingstatetransitionrule_Tasks

Many-To-One Relationship: [task mspp_publishingstatetransitionrule_Tasks](task.md#BKMK_mspp_publishingstatetransitionrule_Tasks)

|Property|Value|
|---|---|
|ReferencingEntity|`task`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_publishingstatetransitionrule_Tasks`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

### <a name="BKMK_mspp_publishingstatetransitionrule_webrole"></a> mspp_publishingstatetransitionrule_webrole

See [mspp_webrole mspp_publishingstatetransitionrule_webrole Many-To-Many Relationship](mspp_webrole.md#BKMK_mspp_publishingstatetransitionrule_webrole)

|Property|Value|
|---|---|
|IntersectEntityName|`mspp_publishingstatetransitionrule_webrole`|
|IsCustomizable|False|
|SchemaName|`mspp_publishingstatetransitionrule_webrole`|
|IntersectAttribute|`mspp_publishingstatetransitionruleid`|
|NavigationPropertyName|`mspp_publishingstatetransitionrule_webrole`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mspp_publishingstatetransitionrule?displayProperty=fullName>
