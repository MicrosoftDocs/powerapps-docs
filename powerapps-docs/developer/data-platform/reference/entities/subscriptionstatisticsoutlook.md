---
title: "Subscription Statistic Outlook (SubscriptionStatisticsOutlook) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Subscription Statistic Outlook (SubscriptionStatisticsOutlook) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: JimDaly
ms.author: jdaly
ms.reviewer: jdaly
search.audienceType: 
  - developer
---

# Subscription Statistic Outlook (SubscriptionStatisticsOutlook) table/entity reference (Microsoft Dataverse)

Subscription Statistic Outlook

## Messages

The following table lists the messages for the Subscription Statistic Outlook (SubscriptionStatisticsOutlook) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Restore`<br />Event: True |<xref:Microsoft.Dynamics.CRM.Restore?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Subscription Statistic Outlook (SubscriptionStatisticsOutlook) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Subscription Statistic Outlook** |
| **DisplayCollectionName** | **Subscription Statistics Outlook** |
| **SchemaName** | `SubscriptionStatisticsOutlook` |
| **CollectionSchemaName** | `SubscriptionStatisticsOutlook` |
| **EntitySetName** | `subscriptionstatisticsoutlookset`|
| **LogicalName** | `subscriptionstatisticsoutlook` |
| **LogicalCollectionName** | `subscriptionstatisticsoutlook` |
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


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_subscriptionstatisticsoutlook_DeletedItemReferences"></a> subscriptionstatisticsoutlook_DeletedItemReferences

Many-To-One Relationship: [deleteditemreference subscriptionstatisticsoutlook_DeletedItemReferences](deleteditemreference.md#BKMK_subscriptionstatisticsoutlook_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencingEntity|`deleteditemreference`|
|ReferencingAttribute|`deletedobject`|
|ReferencedEntityNavigationPropertyName|`subscriptionstatisticsoutlook_DeletedItemReferences`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.subscriptionstatisticsoutlook?displayProperty=fullName>
