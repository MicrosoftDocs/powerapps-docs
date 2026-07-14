---
title: "Privilege table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Privilege table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Privilege table/entity reference (Microsoft Dataverse)

Permission to perform an action in Microsoft CRM. The platform checks for the privilege and rejects the attempt if the user does not hold the privilege.

## Messages

The following table lists the messages for the Privilege table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /privileges(*privilegeid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /privileges<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Privilege table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Privilege** |
| **DisplayCollectionName** | **Privileges** |
| **SchemaName** | `Privilege` |
| **CollectionSchemaName** | `Privileges` |
| **EntitySetName** | `privileges`|
| **LogicalName** | `privilege` |
| **LogicalCollectionName** | `privileges` |
| **PrimaryIdAttribute** | `privilegeid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AccessRight](#BKMK_AccessRight)
- [CanBeBasic](#BKMK_CanBeBasic)
- [CanBeDeep](#BKMK_CanBeDeep)
- [CanBeEntityReference](#BKMK_CanBeEntityReference)
- [CanBeGlobal](#BKMK_CanBeGlobal)
- [CanBeLocal](#BKMK_CanBeLocal)
- [CanBeParentEntityReference](#BKMK_CanBeParentEntityReference)
- [CanBeRecordFilter](#BKMK_CanBeRecordFilter)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCustomizable](#BKMK_IsCustomizable)
- [Name](#BKMK_Name)
- [PrivilegeId](#BKMK_PrivilegeId)
- [PrivilegeRowId](#BKMK_PrivilegeRowId)

### <a name="BKMK_AccessRight"></a> AccessRight

|Property|Value|
|---|---|
|Description|**Rights a user has to an instance of an entity.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`accessright`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_CanBeBasic"></a> CanBeBasic

|Property|Value|
|---|---|
|Description|**Information that specifies whether the privilege applies to the user, the user's team, or objects shared by the user.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`canbebasic`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`privilege_canbebasic`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_CanBeDeep"></a> CanBeDeep

|Property|Value|
|---|---|
|Description|**Information that specifies whether the privilege applies to child business units of the business unit associated with the user.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`canbedeep`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`privilege_canbedeep`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_CanBeEntityReference"></a> CanBeEntityReference

|Property|Value|
|---|---|
|Description|**Information that specifies whether the privilege applies to the local reference of an external party.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`canbeentityreference`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`privilege_canbeentityreference`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_CanBeGlobal"></a> CanBeGlobal

|Property|Value|
|---|---|
|Description|**Information that specifies whether the privilege applies to the entire organization.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`canbeglobal`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`privilege_canbeglobal`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_CanBeLocal"></a> CanBeLocal

|Property|Value|
|---|---|
|Description|**Information that specifies whether the privilege applies to the user's business unit.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`canbelocal`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`privilege_canbelocal`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_CanBeParentEntityReference"></a> CanBeParentEntityReference

|Property|Value|
|---|---|
|Description|**Information that specifies whether the privilege applies to parent reference of the external party.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`canbeparententityreference`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`privilege_canbeparententityreference`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_CanBeRecordFilter"></a> CanBeRecordFilter

|Property|Value|
|---|---|
|Description|**Information that specifies whether the privilege applies to the record filters.**|
|DisplayName|**Can Be Record Filter**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`canberecordfilter`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`privilege_canberecordfilter`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Version in which the component is introduced.**|
|DisplayName|**Introduced Version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`introducedversion`|
|RequiredLevel|None|
|Type|String|
|Format|VersionNumber|
|FormatName|VersionNumber|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|48|

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**Information that specifies whether this component can be customized.**|
|DisplayName|**Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the privilege.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_PrivilegeId"></a> PrivilegeId

|Property|Value|
|---|---|
|Description|**Unique identifier of the privilege.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`privilegeid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_PrivilegeRowId"></a> PrivilegeRowId

|Property|Value|
|---|---|
|Description|**Unique identifier of the Privilege used when synchronizing customizations for the Microsoft Dynamics CRM client for Outlook**|
|DisplayName|**App Module Unique Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`privilegerowid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [IsDisabledWhenIntegrated](#BKMK_IsDisabledWhenIntegrated)
- [IsManaged](#BKMK_IsManaged)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Component State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentstate`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`componentstate`|

#### ComponentState Choices/Options

|Value|Label|
|---|---|
|0|**Published**|
|1|**Unpublished**|
|2|**Deleted**|
|3|**Deleted Unpublished**|

### <a name="BKMK_IsDisabledWhenIntegrated"></a> IsDisabledWhenIntegrated

|Property|Value|
|---|---|
|Description|**Specifies whether the privilege is disabled.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`isdisabledwhenintegrated`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`privilege_isdisabledwhenintegrated`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Information that specifies whether this component is managed.**|
|DisplayName|**State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Record Overwrite Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overwritetime`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the associated solution.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`supportingsolutionid`|
|RequiredLevel|None|
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

### <a name="BKMK_solution_privilege"></a> solution_privilege

One-To-Many Relationship: [solution solution_privilege](solution.md#BKMK_solution_privilege)

|Property|Value|
|---|---|
|ReferencedEntity|`solution`|
|ReferencedAttribute|`solutionid`|
|ReferencingAttribute|`solutionid`|
|ReferencingEntityNavigationPropertyName|`solution_privilege`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [Privilege_AsyncOperations](#BKMK_Privilege_AsyncOperations)
- [Privilege_BulkDeleteFailures](#BKMK_Privilege_BulkDeleteFailures)
- [privilegecheckerlog_CheckedPrivilege](#BKMK_privilegecheckerlog_CheckedPrivilege)

### <a name="BKMK_Privilege_AsyncOperations"></a> Privilege_AsyncOperations

Many-To-One Relationship: [asyncoperation Privilege_AsyncOperations](asyncoperation.md#BKMK_Privilege_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Privilege_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Privilege_BulkDeleteFailures"></a> Privilege_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure Privilege_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Privilege_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Privilege_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_privilegecheckerlog_CheckedPrivilege"></a> privilegecheckerlog_CheckedPrivilege

Many-To-One Relationship: [privilegecheckerlog privilegecheckerlog_CheckedPrivilege](privilegecheckerlog.md#BKMK_privilegecheckerlog_CheckedPrivilege)

|Property|Value|
|---|---|
|ReferencingEntity|`privilegecheckerlog`|
|ReferencingAttribute|`checkedprivilege`|
|ReferencedEntityNavigationPropertyName|`privilegecheckerlog_CheckedPrivilege`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

- [roleprivileges_association](#BKMK_roleprivileges_association)
- [roletemplateprivileges_association](#BKMK_roletemplateprivileges_association)

### <a name="BKMK_roleprivileges_association"></a> roleprivileges_association

See [role roleprivileges_association Many-To-Many Relationship](role.md#BKMK_roleprivileges_association)

|Property|Value|
|---|---|
|IntersectEntityName|`roleprivileges`|
|IsCustomizable|False|
|SchemaName|`roleprivileges_association`|
|IntersectAttribute|`privilegeid`|
|NavigationPropertyName|`roleprivileges_association`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_roletemplateprivileges_association"></a> roletemplateprivileges_association

See [roletemplate roletemplateprivileges_association Many-To-Many Relationship](roletemplate.md#BKMK_roletemplateprivileges_association)

|Property|Value|
|---|---|
|IntersectEntityName|`roletemplateprivileges`|
|IsCustomizable|False|
|SchemaName|`roletemplateprivileges_association`|
|IntersectAttribute|`privilegeid`|
|NavigationPropertyName|`roletemplateprivileges_association`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.privilege?displayProperty=fullName>
