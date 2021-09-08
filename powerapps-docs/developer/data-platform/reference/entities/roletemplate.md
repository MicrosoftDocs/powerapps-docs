---
title: "RoleTemplate table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the RoleTemplate table/entity."
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

# RoleTemplate table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Template for a role. Defines initial attributes that will be used when creating a new role.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|RoleTemplates|
|DisplayCollectionName|Role Templates|
|DisplayName|Role Template|
|EntitySetName|roletemplates|
|IsBPFEntity|False|
|LogicalCollectionName|roletemplates|
|LogicalName|roletemplate|
|OwnershipType|None|
|PrimaryIdAttribute|roletemplateid|
|PrimaryNameAttribute|name|
|SchemaName|RoleTemplate|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Name](#BKMK_Name)
- [RoleTemplateId](#BKMK_RoleTemplateId)


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of the role template.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_RoleTemplateId"></a> RoleTemplateId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the role template.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|roletemplateid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.


### <a name="BKMK_Upgrading"></a> Upgrading

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|upgrading|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### Upgrading Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False


<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_role_template_roles"></a> role_template_roles

Same as role table [role_template_roles](role.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|role|
|ReferencingAttribute|roletemplateid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|role_template_roles|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the RoleTemplate table is the first table in the relationship. Listed by **SchemaName**.


### <a name="BKMK_roletemplateprivileges_association"></a> roletemplateprivileges_association

IntersectEntityName: roletemplateprivileges<br />
#### Table 1

|Property|Value|
|--------|-----|
|IntersectAttribute|roletemplateid|
|IsCustomizable|False|
|LogicalName|roletemplate|
|NavigationPropertyName|roletemplateprivileges_association|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |

#### Table 2

|Property|Value|
|--------|-----|
|LogicalName|privilege|
|IntersectAttribute|privilegeid|
|NavigationPropertyName|roletemplateprivileges_association|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |


### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.roletemplate?text=roletemplate EntityType" />