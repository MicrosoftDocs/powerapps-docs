---
title: "RoleTemplatePrivileges table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the RoleTemplatePrivileges table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# RoleTemplatePrivileges table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the RoleTemplatePrivileges table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|

## Properties

The following table lists selected properties for the RoleTemplatePrivileges table.

|Property|Value|
| --- | --- |
| **SchemaName** | `RoleTemplatePrivileges` |
| **EntitySetName** | `roletemplateprivilegescollection`|
| **LogicalName** | `roletemplateprivileges` |
| **PrimaryIdAttribute** | `roletemplateprivilegeid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [IsBasic](#BKMK_IsBasic)
- [IsDeep](#BKMK_IsDeep)
- [IsGlobal](#BKMK_IsGlobal)
- [IsLocal](#BKMK_IsLocal)
- [RoleTemplatePrivilegeId](#BKMK_RoleTemplatePrivilegeId)

### <a name="BKMK_IsBasic"></a> IsBasic

|Property|Value|
|---|---|
|Description|**Information about whether the role in the template applies to the user, the user's team, or objects shared by the user.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isbasic`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`roletemplateprivileges_isbasic`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsDeep"></a> IsDeep

|Property|Value|
|---|---|
|Description|**Information about whether the role in the template applies to child business units of the business unit associated with the user.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isdeep`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`roletemplateprivileges_isdeep`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsGlobal"></a> IsGlobal

|Property|Value|
|---|---|
|Description|**Information about whether the role in the template applies to the entire organization.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isglobal`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`roletemplateprivileges_isglobal`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsLocal"></a> IsLocal

|Property|Value|
|---|---|
|Description|**Information about whether the role in the template applies to the user's business unit.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`islocal`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`roletemplateprivileges_islocal`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_RoleTemplatePrivilegeId"></a> RoleTemplatePrivilegeId

|Property|Value|
|---|---|
|Description|**Unique identifier of the role template privileges.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`roletemplateprivilegeid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [PrivilegeId](#BKMK_PrivilegeId)
- [RoleTemplateId](#BKMK_RoleTemplateId)
- [Upgrading](#BKMK_Upgrading)

### <a name="BKMK_PrivilegeId"></a> PrivilegeId

|Property|Value|
|---|---|
|Description|**Unique identifier of the privilege assigned to the role template.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`privilegeid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_RoleTemplateId"></a> RoleTemplateId

|Property|Value|
|---|---|
|Description|**Unique identifier of the role template that is associated with the role privilege.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`roletemplateid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Upgrading"></a> Upgrading

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`upgrading`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`roletemplateprivileges_upgrading`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

### <a name="BKMK_roletemplateprivileges_association"></a> roletemplateprivileges_association


|Property|Value|
|---|---|
|IntersectEntityName|`roletemplateprivileges`|
|IsCustomizable|False|
|SchemaName|`roletemplateprivileges_association`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.roletemplateprivileges?displayProperty=fullName>
