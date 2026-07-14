---
title: "Subscription Sync Entry Offline (SubscriptionSyncEntryOffline) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Subscription Sync Entry Offline (SubscriptionSyncEntryOffline) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Subscription Sync Entry Offline (SubscriptionSyncEntryOffline) table/entity reference (Microsoft Dataverse)

Used for offline sync, internal use only.

## Properties

The following table lists selected properties for the Subscription Sync Entry Offline (SubscriptionSyncEntryOffline) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Subscription Sync Entry Offline** |
| **DisplayCollectionName** | **Subscription Sync Entry Offline** |
| **SchemaName** | `SubscriptionSyncEntryOffline` |
| **CollectionSchemaName** | `SubscriptionSyncEntriesOffline` |
| **EntitySetName** | `subscriptionsyncentriesoffline`|
| **LogicalName** | `subscriptionsyncentryoffline` |
| **LogicalCollectionName** | `subscriptionsyncentriesoffline` |
| **PrimaryIdAttribute** | `subscriptionid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ObjectId](#BKMK_ObjectId)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [SubscriptionId](#BKMK_SubscriptionId)
- [SyncState](#BKMK_SyncState)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|---|---|
|Description|**Object Id**|
|DisplayName|**ObjectId**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objectid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|---|---|
|Description|**Entity object type code**|
|DisplayName|**ObjectTypeCode**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objecttypecode`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_SubscriptionId"></a> SubscriptionId

|Property|Value|
|---|---|
|Description|**Subscription Id**|
|DisplayName|**SubscriptionId**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`subscriptionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SyncState"></a> SyncState

|Property|Value|
|---|---|
|Description|**Sync state**|
|DisplayName|**SyncState**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`syncstate`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number**|
|DisplayName|**VersionNumber**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|SystemRequired|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|




### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.subscriptionsyncentryoffline?displayProperty=fullName>
