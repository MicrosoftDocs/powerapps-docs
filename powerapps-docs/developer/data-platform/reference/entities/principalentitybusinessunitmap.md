---
title: "PrincipalEntityBusinessUnitMap table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the PrincipalEntityBusinessUnitMap table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# PrincipalEntityBusinessUnitMap table/entity reference (Microsoft Dataverse)

Internal authorization table to track user authorization changes

## Messages

The following table lists the messages for the PrincipalEntityBusinessUnitMap table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|

## Properties

The following table lists selected properties for the PrincipalEntityBusinessUnitMap table.

|Property|Value|
| --- | --- |
| **DisplayName** | **PrincipalEntityBusinessUnitMap** |
| **DisplayCollectionName** | **PrincipalEntityBusinessUnitMaps** |
| **SchemaName** | `PrincipalEntityBusinessUnitMap` |
| **CollectionSchemaName** | `PrincipalEntityBusinessUnitMaps` |
| **EntitySetName** | `principalentitybusinessunitmaps`|
| **LogicalName** | `principalentitybusinessunitmap` |
| **LogicalCollectionName** | `principalentitybusinessunitmaps` |
| **PrimaryIdAttribute** | `principalentitybusinessunitmapid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

### <a name="BKMK_PrincipalEntityBusinessUnitMapId"></a> PrincipalEntityBusinessUnitMapId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`principalentitybusinessunitmapid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [BusinessUnitId](#BKMK_BusinessUnitId)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [PrincipalId](#BKMK_PrincipalId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`businessunitid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objecttypecode`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_PrincipalId"></a> PrincipalId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`principalid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [business_unit_principalentitybusinessunitmap](#BKMK_business_unit_principalentitybusinessunitmap)
- [owner_principalentitybusinessunitmap](#BKMK_owner_principalentitybusinessunitmap)

### <a name="BKMK_business_unit_principalentitybusinessunitmap"></a> business_unit_principalentitybusinessunitmap

One-To-Many Relationship: [businessunit business_unit_principalentitybusinessunitmap](businessunit.md#BKMK_business_unit_principalentitybusinessunitmap)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`businessunitid`|
|ReferencingEntityNavigationPropertyName|`businessunitid_businessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_principalentitybusinessunitmap"></a> owner_principalentitybusinessunitmap

One-To-Many Relationship: [owner owner_principalentitybusinessunitmap](owner.md#BKMK_owner_principalentitybusinessunitmap)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`principalid`|
|ReferencingEntityNavigationPropertyName|`principalid_owner`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.principalentitybusinessunitmap?displayProperty=fullName>
