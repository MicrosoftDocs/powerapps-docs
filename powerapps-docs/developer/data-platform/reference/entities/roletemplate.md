---
title: "Role Template (RoleTemplate) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Role Template (RoleTemplate) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Role Template (RoleTemplate) table/entity reference (Microsoft Dataverse)

Template for a role. Defines initial attributes that will be used when creating a new role.

## Messages

The following table lists the messages for the Role Template (RoleTemplate) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|

## Properties

The following table lists selected properties for the Role Template (RoleTemplate) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Role Template** |
| **DisplayCollectionName** | **Role Templates** |
| **SchemaName** | `RoleTemplate` |
| **CollectionSchemaName** | `RoleTemplates` |
| **EntitySetName** | `roletemplates`|
| **LogicalName** | `roletemplate` |
| **LogicalCollectionName** | `roletemplates` |
| **PrimaryIdAttribute** | `roletemplateid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Name](#BKMK_Name)
- [RoleTemplateId](#BKMK_RoleTemplateId)

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the role template.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_RoleTemplateId"></a> RoleTemplateId

|Property|Value|
|---|---|
|Description|**Unique identifier of the role template.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`roletemplateid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

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
|GlobalChoiceName|`roletemplate_upgrading`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_role_template_roles"></a> role_template_roles

Many-To-One Relationship: [role role_template_roles](role.md#BKMK_role_template_roles)

|Property|Value|
|---|---|
|ReferencingEntity|`role`|
|ReferencingAttribute|`roletemplateid`|
|ReferencedEntityNavigationPropertyName|`role_template_roles`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

### <a name="BKMK_roletemplateprivileges_association"></a> roletemplateprivileges_association

See [privilege roletemplateprivileges_association Many-To-Many Relationship](privilege.md#BKMK_roletemplateprivileges_association)

|Property|Value|
|---|---|
|IntersectEntityName|`roletemplateprivileges`|
|IsCustomizable|False|
|SchemaName|`roletemplateprivileges_association`|
|IntersectAttribute|`roletemplateid`|
|NavigationPropertyName|`roletemplateprivileges_association`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.roletemplate?displayProperty=fullName>
