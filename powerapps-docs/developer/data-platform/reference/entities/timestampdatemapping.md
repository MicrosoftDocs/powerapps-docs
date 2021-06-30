---
title: "TimeStampDateMapping table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the TimeStampDateMapping table/entity."
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

# TimeStampDateMapping table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

For internal use only.`


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|TimeStampDateMappings|
|DisplayCollectionName|Time Stamp Date Mappings|
|DisplayName|Time Stamp Date Mapping|
|EntitySetName|timestampdatemappings|
|IsBPFEntity|False|
|LogicalCollectionName|timestampdatemappings|
|LogicalName|timestampdatemapping|
|OwnershipType|None|
|PrimaryIdAttribute|timestampdatemappingid|
|PrimaryNameAttribute||
|SchemaName|TimeStampDateMapping|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.


### <a name="BKMK_TimeStampDateMappingId"></a> TimeStampDateMappingId

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|timestampdatemappingid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [Date](#BKMK_Date)
- [TimeStamp](#BKMK_TimeStamp)


### <a name="BKMK_Date"></a> Date

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description||
|DisplayName||
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|date|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_TimeStamp"></a> TimeStamp

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timestamp|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|SystemRequired|
|Type|BigInt|



### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.timestampdatemapping?text=timestampdatemapping EntityType" />