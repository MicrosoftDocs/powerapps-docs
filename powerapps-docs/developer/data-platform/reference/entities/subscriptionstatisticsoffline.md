---
title: "SubscriptionStatisticsOffline table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the SubscriptionStatisticsOffline table/entity."
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

# SubscriptionStatisticsOffline table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Subscription Statistic Offline


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|SubscriptionStatisticsOffline|
|DisplayCollectionName|Subscription Statistics Offline|
|DisplayName|Subscription Statistic Offline|
|EntitySetName|subscriptionstatisticsofflineset|
|IsBPFEntity|False|
|LogicalCollectionName|subscriptionstatisticsoffline|
|LogicalName|subscriptionstatisticsoffline|
|OwnershipType|None|
|PrimaryIdAttribute|subscriptionid|
|PrimaryNameAttribute||
|SchemaName|SubscriptionStatisticsOffline|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [FullSyncRequired](#BKMK_FullSyncRequired)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [SubscriptionId](#BKMK_SubscriptionId)


### <a name="BKMK_FullSyncRequired"></a> FullSyncRequired

|Property|Value|
|--------|-----|
|Description|Is full sync required or not|
|DisplayName|FullSyncRequired|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|fullsyncrequired|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### FullSyncRequired Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: True



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



### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.subscriptionstatisticsoffline?text=subscriptionstatisticsoffline EntityType" />