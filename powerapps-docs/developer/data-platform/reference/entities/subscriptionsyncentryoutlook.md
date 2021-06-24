---
title: "SubscriptionSyncEntryOutlook table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the SubscriptionSyncEntryOutlook table/entity."
ms.date: 03/04/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# SubscriptionSyncEntryOutlook table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Used for outlook sync, internal use only.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|SubscriptionSyncEntriesOutlook|
|DisplayCollectionName|Subscription Sync Entry Outlook|
|DisplayName|Subscription Sync Entry Outlook|
|EntitySetName|subscriptionsyncentriesoutlook|
|IsBPFEntity|False|
|LogicalCollectionName|subscriptionsyncentriesoutlook|
|LogicalName|subscriptionsyncentryoutlook|
|OwnershipType|None|
|PrimaryIdAttribute|subscriptionid|
|PrimaryNameAttribute||
|SchemaName|SubscriptionSyncEntryOutlook|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ObjectId](#BKMK_ObjectId)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [SubscriptionId](#BKMK_SubscriptionId)
- [SyncState](#BKMK_SyncState)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|--------|-----|
|Description|Object Id|
|DisplayName|ObjectId|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|objectid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|--------|-----|
|Description|Entity object type code|
|DisplayName|ObjectTypeCode|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|objecttypecode|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_SubscriptionId"></a> SubscriptionId

|Property|Value|
|--------|-----|
|Description|Subscription Id|
|DisplayName|SubscriptionId|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|subscriptionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SyncState"></a> SyncState

|Property|Value|
|--------|-----|
|Description|Sync state|
|DisplayName|SyncState|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|syncstate|
|MaxValue||
|MinValue||
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|Version number|
|DisplayName|VersionNumber|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|SystemRequired|
|Type|BigInt|



### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.subscriptionsyncentryoutlook?text=subscriptionsyncentryoutlook EntityType" />