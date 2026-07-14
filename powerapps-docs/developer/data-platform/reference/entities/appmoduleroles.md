---
title: "App Module Roles (AppModuleRoles) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the App Module Roles (AppModuleRoles) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# App Module Roles (AppModuleRoles) table/entity reference (Microsoft Dataverse)

Security roles that have access to a business app.

## Messages

The following table lists the messages for the App Module Roles (AppModuleRoles) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `RetrieveMultiple`<br />Event: True |`GET` /appmodulerolescollection<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the App Module Roles (AppModuleRoles) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **App Module Roles** |
| **DisplayCollectionName** | **App Module Roles** |
| **SchemaName** | `AppModuleRoles` |
| **EntitySetName** | `appmodulerolescollection`|
| **LogicalName** | `appmoduleroles` |
| **PrimaryIdAttribute** | `appmoduleroleid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AppModuleRoleId](#BKMK_AppModuleRoleId)
- [AppModuleRoleIdUnique](#BKMK_AppModuleRoleIdUnique)
- [IntroducedVersion](#BKMK_IntroducedVersion)

### <a name="BKMK_AppModuleRoleId"></a> AppModuleRoleId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appmoduleroleid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_AppModuleRoleIdUnique"></a> AppModuleRoleIdUnique

|Property|Value|
|---|---|
|Description|**Unique identifier of the App Module Roles used when synchronizing customizations for the Microsoft Dynamics 365 client for Outlook**|
|DisplayName|**App Module Role Unique Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appmoduleroleidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Version in which the similarity rule is introduced.**|
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
|MaxLength|100|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [AppModuleId](#BKMK_AppModuleId)
- [ComponentState](#BKMK_ComponentState)
- [IsManaged](#BKMK_IsManaged)
- [OverwriteTime](#BKMK_OverwriteTime)
- [RoleId](#BKMK_RoleId)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_AppModuleId"></a> AppModuleId

|Property|Value|
|---|---|
|Description|**Unique identifier of the app module.**|
|DisplayName|**AppModule**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appmoduleid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|appmodule|

### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|---|---|
|Description|**For internal use only**|
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
|Description|**Is Managed**|
|DisplayName|**IsManaged**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**Internal use only**|
|DisplayName|**Overwrite Time**|
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

### <a name="BKMK_RoleId"></a> RoleId

|Property|Value|
|---|---|
|Description||
|DisplayName|**Role**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`roleid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|role|

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

## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

### <a name="BKMK_appmoduleroles_association"></a> appmoduleroles_association


|Property|Value|
|---|---|
|IntersectEntityName|`appmoduleroles`|
|IsCustomizable|False|
|SchemaName|`appmoduleroles_association`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.appmoduleroles?displayProperty=fullName>
