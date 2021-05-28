---
title: "Privilege table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Privilege table/entity."
ms.date: 05/20/2021
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

# Privilege table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Permission to perform an action in Microsoft CRM. The platform checks for the privilege and rejects the attempt if the user does not hold the privilege.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Retrieve|GET [*org URI*]/api/data/v9.0/privileges(*privilegeid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/privileges<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|Privileges|
|DisplayCollectionName|Privileges|
|DisplayName|Privilege|
|EntitySetName|privileges|
|IsBPFEntity|False|
|LogicalCollectionName|privileges|
|LogicalName|privilege|
|OwnershipType|None|
|PrimaryIdAttribute|privilegeid|
|PrimaryNameAttribute|name|
|SchemaName|Privilege|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AccessRight](#BKMK_AccessRight)
- [CanBeBasic](#BKMK_CanBeBasic)
- [CanBeDeep](#BKMK_CanBeDeep)
- [CanBeEntityReference](#BKMK_CanBeEntityReference)
- [CanBeGlobal](#BKMK_CanBeGlobal)
- [CanBeLocal](#BKMK_CanBeLocal)
- [CanBeParentEntityReference](#BKMK_CanBeParentEntityReference)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [Name](#BKMK_Name)
- [PrivilegeId](#BKMK_PrivilegeId)
- [PrivilegeRowId](#BKMK_PrivilegeRowId)


### <a name="BKMK_AccessRight"></a> AccessRight

|Property|Value|
|--------|-----|
|Description|Rights a user has to an instance of an entity.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|accessright|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_CanBeBasic"></a> CanBeBasic

|Property|Value|
|--------|-----|
|Description|Information that specifies whether the privilege applies to the user, the user's team, or objects shared by the user.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|canbebasic|
|RequiredLevel|None|
|Type|Boolean|

#### CanBeBasic Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_CanBeDeep"></a> CanBeDeep

|Property|Value|
|--------|-----|
|Description|Information that specifies whether the privilege applies to child business units of the business unit associated with the user.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|canbedeep|
|RequiredLevel|None|
|Type|Boolean|

#### CanBeDeep Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_CanBeEntityReference"></a> CanBeEntityReference

|Property|Value|
|--------|-----|
|Description|Information that specifies whether the privilege applies to the local reference of an external party.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|canbeentityreference|
|RequiredLevel|None|
|Type|Boolean|

#### CanBeEntityReference Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_CanBeGlobal"></a> CanBeGlobal

|Property|Value|
|--------|-----|
|Description|Information that specifies whether the privilege applies to the entire organization.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|canbeglobal|
|RequiredLevel|None|
|Type|Boolean|

#### CanBeGlobal Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_CanBeLocal"></a> CanBeLocal

|Property|Value|
|--------|-----|
|Description|Information that specifies whether the privilege applies to the user's business unit.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|canbelocal|
|RequiredLevel|None|
|Type|Boolean|

#### CanBeLocal Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_CanBeParentEntityReference"></a> CanBeParentEntityReference

|Property|Value|
|--------|-----|
|Description|Information that specifies whether the privilege applies to parent reference of the external party.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|canbeparententityreference|
|RequiredLevel|None|
|Type|Boolean|

#### CanBeParentEntityReference Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|--------|-----|
|Description|Version in which the component is introduced.|
|DisplayName|Introduced Version|
|FormatName|VersionNumber|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|introducedversion|
|MaxLength|48|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of the privilege.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PrivilegeId"></a> PrivilegeId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the privilege.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|privilegeid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_PrivilegeRowId"></a> PrivilegeRowId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the Privilege used when synchronizing customizations for the Microsoft Dynamics CRM client for Outlook|
|DisplayName|App Module Unique Id|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|privilegerowid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [IsDisabledWhenIntegrated](#BKMK_IsDisabledWhenIntegrated)
- [IsManaged](#BKMK_IsManaged)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Component State|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentstate|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ComponentState Choices/Options

|Value|Label|
|-----|-----|
|0|Published|
|1|Unpublished|
|2|Deleted|
|3|Deleted Unpublished|



### <a name="BKMK_IsDisabledWhenIntegrated"></a> IsDisabledWhenIntegrated

|Property|Value|
|--------|-----|
|Description|Specifies whether the privilege is disabled.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|isdisabledwhenintegrated|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsDisabledWhenIntegrated Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|--------|-----|
|Description|Information that specifies whether this component is managed.|
|DisplayName|State|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsManaged Choices/Options

|Value|Label|
|-----|-----|
|1|Managed|
|0|Unmanaged|

**DefaultValue**: False



### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Record Overwrite Time|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overwritetime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the associated solution.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|solutionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|supportingsolutionid|
|RequiredLevel|None|
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

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [Privilege_AsyncOperations](#BKMK_Privilege_AsyncOperations)
- [Privilege_BulkDeleteFailures](#BKMK_Privilege_BulkDeleteFailures)


### <a name="BKMK_Privilege_AsyncOperations"></a> Privilege_AsyncOperations

Same as asyncoperation table [Privilege_AsyncOperations](asyncoperation.md#BKMK_Privilege_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Privilege_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Privilege_BulkDeleteFailures"></a> Privilege_BulkDeleteFailures

Same as bulkdeletefailure table [Privilege_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Privilege_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Privilege_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.


### <a name="BKMK_solution_privilege"></a> solution_privilege

See solution Table [solution_privilege](solution.md#BKMK_solution_privilege) One-To-Many relationship.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the Privilege table is the first table in the relationship. Listed by **SchemaName**.


### <a name="BKMK_roleprivileges_association"></a> roleprivileges_association

IntersectEntityName: roleprivileges<br />
#### Table 1

|Property|Value|
|--------|-----|
|IntersectAttribute|privilegeid|
|IsCustomizable|False|
|LogicalName|privilege|
|NavigationPropertyName|roleprivileges_association|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |

#### Table 2

|Property|Value|
|--------|-----|
|LogicalName|role|
|IntersectAttribute|roleid|
|NavigationPropertyName|roleprivileges_association|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |


### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.privilege?text=privilege EntityType" />