---
title: "Ms Graph Resource To Subscription (MsGraphResourceToSubscription) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Ms Graph Resource To Subscription (MsGraphResourceToSubscription) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Ms Graph Resource To Subscription (MsGraphResourceToSubscription) table/entity reference (Microsoft Dataverse)

For internal use only. The mapping between Ms Graph Resources and Subscriptions.

## Messages

The following table lists the messages for the Ms Graph Resource To Subscription (MsGraphResourceToSubscription) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msgraphresourcetosubscriptions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /msgraphresourcetosubscriptions(*msgraphresourcetosubscriptionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /msgraphresourcetosubscriptions(*msgraphresourcetosubscriptionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msgraphresourcetosubscriptions<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /msgraphresourcetosubscriptions(*msgraphresourcetosubscriptionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /msgraphresourcetosubscriptions(*msgraphresourcetosubscriptionid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Ms Graph Resource To Subscription (MsGraphResourceToSubscription) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Ms Graph Resource To Subscription** |
| **DisplayCollectionName** | **Ms Graph Resource To Subscriptions** |
| **SchemaName** | `MsGraphResourceToSubscription` |
| **CollectionSchemaName** | `MsGraphResourceToSubscriptions` |
| **EntitySetName** | `msgraphresourcetosubscriptions`|
| **LogicalName** | `msgraphresourcetosubscription` |
| **LogicalCollectionName** | `msgraphresourcetosubscriptions` |
| **PrimaryIdAttribute** | `msgraphresourcetosubscriptionid` |
| **PrimaryNameAttribute** |`resourceid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CreatedInGraphOn](#BKMK_CreatedInGraphOn)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [MsGraphResourceToSubscriptionId](#BKMK_MsGraphResourceToSubscriptionId)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [ResourceId](#BKMK_ResourceId)
- [ResourceType](#BKMK_ResourceType)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [SubscriptionId](#BKMK_SubscriptionId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_CreatedInGraphOn"></a> CreatedInGraphOn

|Property|Value|
|---|---|
|Description|**For internal use only. Date and time when the record was created in Graph.**|
|DisplayName|**Created In Graph On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdingraphon`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|TimeZoneIndependent|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

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

### <a name="BKMK_MsGraphResourceToSubscriptionId"></a> MsGraphResourceToSubscriptionId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Ms Graph Resource To Subscription**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msgraphresourcetosubscriptionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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

### <a name="BKMK_ResourceId"></a> ResourceId

|Property|Value|
|---|---|
|Description||
|DisplayName|**Resource Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`resourceid`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ResourceType"></a> ResourceType

|Property|Value|
|---|---|
|Description|**For internal use only. Shows the different options for resource type.**|
|DisplayName|**Resource Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`resourcetype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msgraphresourcetosubscription_resourcetype`|

#### ResourceType Choices/Options

|Value|Label|
|---|---|
|0|**Teams Chat Messages**|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Ms Graph Resource To Subscription**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msgraphresourcetosubscription_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Ms Graph Resource To Subscription**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msgraphresourcetosubscription_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_SubscriptionId"></a> SubscriptionId

|Property|Value|
|---|---|
|Description||
|DisplayName|**Subscription Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`subscriptionid`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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

## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [msgraphresourcetosubscription_AsyncOperations](#BKMK_msgraphresourcetosubscription_AsyncOperations)
- [msgraphresourcetosubscription_BulkDeleteFailures](#BKMK_msgraphresourcetosubscription_BulkDeleteFailures)
- [msgraphresourcetosubscription_MailboxTrackingFolders](#BKMK_msgraphresourcetosubscription_MailboxTrackingFolders)
- [msgraphresourcetosubscription_PrincipalObjectAttributeAccesses](#BKMK_msgraphresourcetosubscription_PrincipalObjectAttributeAccesses)
- [msgraphresourcetosubscription_ProcessSession](#BKMK_msgraphresourcetosubscription_ProcessSession)
- [msgraphresourcetosubscription_SyncErrors](#BKMK_msgraphresourcetosubscription_SyncErrors)

### <a name="BKMK_msgraphresourcetosubscription_AsyncOperations"></a> msgraphresourcetosubscription_AsyncOperations

Many-To-One Relationship: [asyncoperation msgraphresourcetosubscription_AsyncOperations](asyncoperation.md#BKMK_msgraphresourcetosubscription_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msgraphresourcetosubscription_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msgraphresourcetosubscription_BulkDeleteFailures"></a> msgraphresourcetosubscription_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msgraphresourcetosubscription_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msgraphresourcetosubscription_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msgraphresourcetosubscription_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msgraphresourcetosubscription_MailboxTrackingFolders"></a> msgraphresourcetosubscription_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msgraphresourcetosubscription_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msgraphresourcetosubscription_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msgraphresourcetosubscription_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msgraphresourcetosubscription_PrincipalObjectAttributeAccesses"></a> msgraphresourcetosubscription_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msgraphresourcetosubscription_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msgraphresourcetosubscription_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msgraphresourcetosubscription_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msgraphresourcetosubscription_ProcessSession"></a> msgraphresourcetosubscription_ProcessSession

Many-To-One Relationship: [processsession msgraphresourcetosubscription_ProcessSession](processsession.md#BKMK_msgraphresourcetosubscription_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msgraphresourcetosubscription_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msgraphresourcetosubscription_SyncErrors"></a> msgraphresourcetosubscription_SyncErrors

Many-To-One Relationship: [syncerror msgraphresourcetosubscription_SyncErrors](syncerror.md#BKMK_msgraphresourcetosubscription_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msgraphresourcetosubscription_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msgraphresourcetosubscription?displayProperty=fullName>
