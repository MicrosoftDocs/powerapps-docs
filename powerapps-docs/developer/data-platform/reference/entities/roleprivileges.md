---
title: "RolePrivileges table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the RolePrivileges table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# RolePrivileges table/entity reference (Microsoft Dataverse)

Group of privileges used to categorize users to provide appropriate access to entities.

## Messages

The following table lists the messages for the RolePrivileges table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `RetrieveMultiple`<br />Event: True |`GET` /roleprivilegescollection<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the RolePrivileges table.

|Property|Value|
| --- | --- |
| **SchemaName** | `RolePrivileges` |
| **EntitySetName** | `roleprivilegescollection`|
| **LogicalName** | `roleprivileges` |
| **PrimaryIdAttribute** | `roleprivilegeid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CanBeDeleted](#BKMK_CanBeDeleted)
- [PrivilegeDepthMask](#BKMK_PrivilegeDepthMask)
- [RecordFilterId](#BKMK_RecordFilterId)
- [RolePrivilegeId](#BKMK_RolePrivilegeId)

### <a name="BKMK_CanBeDeleted"></a> CanBeDeleted

|Property|Value|
|---|---|
|Description|**Tells whether the role privilege can be deleted.**|
|DisplayName|**Can Be Deleted**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`canbedeleted`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_PrivilegeDepthMask"></a> PrivilegeDepthMask

|Property|Value|
|---|---|
|Description|**System-generated attribute that stores the privileges associated with the role.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`privilegedepthmask`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_RecordFilterId"></a> RecordFilterId

|Property|Value|
|---|---|
|Description|**Unique identifier for Record Filter associated with role privilege.**|
|DisplayName|**Record Filter**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`recordfilterid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|recordfilter|

### <a name="BKMK_RolePrivilegeId"></a> RolePrivilegeId

|Property|Value|
|---|---|
|Description|**Unique identifier of the role privilege.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`roleprivilegeid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [IsManaged](#BKMK_IsManaged)
- [OverwriteTime](#BKMK_OverwriteTime)
- [PrivilegeId](#BKMK_PrivilegeId)
- [RoleId](#BKMK_RoleId)
- [RolePrivilegeIdUnique](#BKMK_RolePrivilegeIdUnique)
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

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description||
|DisplayName||
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

### <a name="BKMK_PrivilegeId"></a> PrivilegeId

|Property|Value|
|---|---|
|Description|**Unique identifier of the privilege associated with the role.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`privilegeid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_RoleId"></a> RoleId

|Property|Value|
|---|---|
|Description|**Unique identifier of the role that is associated with the role privilege.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`roleid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_RolePrivilegeIdUnique"></a> RolePrivilegeIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`roleprivilegeidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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

- [recordfilter_roleprivileges](#BKMK_recordfilter_roleprivileges)
- [solution_roleprivileges](#BKMK_solution_roleprivileges)

### <a name="BKMK_recordfilter_roleprivileges"></a> recordfilter_roleprivileges

One-To-Many Relationship: [recordfilter recordfilter_roleprivileges](recordfilter.md#BKMK_recordfilter_roleprivileges)

|Property|Value|
|---|---|
|ReferencedEntity|`recordfilter`|
|ReferencedAttribute|`recordfilterid`|
|ReferencingAttribute|`recordfilterid`|
|ReferencingEntityNavigationPropertyName|`RecordFilterId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solution_roleprivileges"></a> solution_roleprivileges

One-To-Many Relationship: [solution solution_roleprivileges](solution.md#BKMK_solution_roleprivileges)

|Property|Value|
|---|---|
|ReferencedEntity|`solution`|
|ReferencedAttribute|`solutionid`|
|ReferencingAttribute|`solutionid`|
|ReferencingEntityNavigationPropertyName|`solutionid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

### <a name="BKMK_roleprivileges_association"></a> roleprivileges_association


|Property|Value|
|---|---|
|IntersectEntityName|`roleprivileges`|
|IsCustomizable|False|
|SchemaName|`roleprivileges_association`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.roleprivileges?displayProperty=fullName>
