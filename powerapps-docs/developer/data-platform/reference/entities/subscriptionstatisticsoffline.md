---
title: "Subscription Statistic Offline (SubscriptionStatisticsOffline) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Subscription Statistic Offline (SubscriptionStatisticsOffline) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Subscription Statistic Offline (SubscriptionStatisticsOffline) table/entity reference (Microsoft Dataverse)

Subscription Statistic Offline

## Properties

The following table lists selected properties for the Subscription Statistic Offline (SubscriptionStatisticsOffline) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Subscription Statistic Offline** |
| **DisplayCollectionName** | **Subscription Statistics Offline** |
| **SchemaName** | `SubscriptionStatisticsOffline` |
| **CollectionSchemaName** | `SubscriptionStatisticsOffline` |
| **EntitySetName** | `subscriptionstatisticsofflineset`|
| **LogicalName** | `subscriptionstatisticsoffline` |
| **LogicalCollectionName** | `subscriptionstatisticsoffline` |
| **PrimaryIdAttribute** | `subscriptionid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [FullSyncRequired](#BKMK_FullSyncRequired)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [SubscriptionId](#BKMK_SubscriptionId)

### <a name="BKMK_FullSyncRequired"></a> FullSyncRequired

|Property|Value|
|---|---|
|Description|**Is full sync required or not**|
|DisplayName|**FullSyncRequired**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fullsyncrequired`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`subscriptionstatisticsoffline_fullsyncrequired`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

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




### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.subscriptionstatisticsoffline?displayProperty=fullName>
