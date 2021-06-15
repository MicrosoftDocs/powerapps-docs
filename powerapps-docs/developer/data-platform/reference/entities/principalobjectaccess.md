---
title: "PrincipalObjectAccess table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the PrincipalObjectAccess table/entity."
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

# PrincipalObjectAccess table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).




## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName||
|DisplayCollectionName||
|DisplayName||
|EntitySetName|principalobjectaccessset|
|IsBPFEntity|False|
|LogicalCollectionName||
|LogicalName|principalobjectaccess|
|OwnershipType|None|
|PrimaryIdAttribute|principalobjectaccessid|
|PrimaryNameAttribute||
|SchemaName|PrincipalObjectAccess|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AccessRightsMask](#BKMK_AccessRightsMask)
- [ChangedOn](#BKMK_ChangedOn)
- [InheritedAccessRightsMask](#BKMK_InheritedAccessRightsMask)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [PrincipalObjectAccessId](#BKMK_PrincipalObjectAccessId)
- [PrincipalTypeCode](#BKMK_PrincipalTypeCode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_AccessRightsMask"></a> AccessRightsMask

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|accessrightsmask|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ChangedOn"></a> ChangedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description||
|DisplayName||
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|changedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_InheritedAccessRightsMask"></a> InheritedAccessRightsMask

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|inheritedaccessrightsmask|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|objecttypecode|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_PrincipalObjectAccessId"></a> PrincipalObjectAccessId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the principal object access.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|principalobjectaccessid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_PrincipalTypeCode"></a> PrincipalTypeCode

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|principaltypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezoneruleversionnumber|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|--------|-----|
|Description|Time zone code that was in use when the record was created.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|utcconversiontimezonecode|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ObjectId](#BKMK_ObjectId)
- [PrincipalId](#BKMK_PrincipalId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|objectid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_PrincipalId"></a> PrincipalId

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|principalid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|



### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.principalobjectaccess?text=principalobjectaccess EntityType" />