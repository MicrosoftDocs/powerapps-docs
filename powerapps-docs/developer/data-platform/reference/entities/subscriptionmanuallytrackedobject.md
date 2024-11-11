---
title: "Subscription Manually Tracked Object (SubscriptionManuallyTrackedObject) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Subscription Manually Tracked Object (SubscriptionManuallyTrackedObject) table/entity with Microsoft Dataverse."
ms.date: 11/09/2024
ms.service: powerapps
ms.topic: reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Subscription Manually Tracked Object (SubscriptionManuallyTrackedObject) table/entity reference

For internal use only.

## Properties

The following table lists selected properties for the Subscription Manually Tracked Object (SubscriptionManuallyTrackedObject) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Subscription Manually Tracked Object** |
| **DisplayCollectionName** | **Subscription Manually Tracked Objects** |
| **SchemaName** | `SubscriptionManuallyTrackedObject` |
| **CollectionSchemaName** | `SubscriptionManuallyTrackedObjects` |
| **EntitySetName** | `subscriptionmanuallytrackedobjects`|
| **LogicalName** | `subscriptionmanuallytrackedobject` |
| **LogicalCollectionName** | `subscriptionmanuallytrackedobjects` |
| **PrimaryIdAttribute** | `subscriptionmanuallytrackedobjectid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ObjectId](#BKMK_ObjectId)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [SubscriptionId](#BKMK_SubscriptionId)
- [SubscriptionManuallyTrackedObjectId](#BKMK_SubscriptionManuallyTrackedObjectId)
- [Track](#BKMK_Track)

### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|---|---|
|Description|**Unique identifier of the object with which the subscription is associated.**|
|DisplayName|**Object Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objectid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|---|---|
|Description|**Type code of the object with which the subscription is associated.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_SubscriptionId"></a> SubscriptionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the subscription.**|
|DisplayName|**Subscription Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`subscriptionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SubscriptionManuallyTrackedObjectId"></a> SubscriptionManuallyTrackedObjectId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`subscriptionmanuallytrackedobjectid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Track"></a> Track

|Property|Value|
|---|---|
|Description|**Information that specifies if the object is tracked.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`track`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`subscriptionmanuallytrackedobject_track`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the subscription manually tracked object.**|
|DisplayName|**Version number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|



### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.subscriptionmanuallytrackedobject?displayProperty=fullName>
