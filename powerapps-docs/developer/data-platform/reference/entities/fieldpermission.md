---
title: "Field Permission (FieldPermission) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Field Permission (FieldPermission) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Field Permission (FieldPermission) table/entity reference (Microsoft Dataverse)

Group of privileges used to categorize users to provide appropriate access to secured columns.

## Messages

The following table lists the messages for the Field Permission (FieldPermission) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /fieldpermissions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /fieldpermissions(*fieldpermissionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /fieldpermissions(*fieldpermissionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /fieldpermissions<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /fieldpermissions(*fieldpermissionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /fieldpermissions(*fieldpermissionid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Field Permission (FieldPermission) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Field Permission** |
| **DisplayCollectionName** | **Field Permissions** |
| **SchemaName** | `FieldPermission` |
| **CollectionSchemaName** | `FieldPermissions` |
| **EntitySetName** | `fieldpermissions`|
| **LogicalName** | `fieldpermission` |
| **LogicalCollectionName** | `fieldpermissions` |
| **PrimaryIdAttribute** | `fieldpermissionid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AttributeLogicalName](#BKMK_AttributeLogicalName)
- [CanCreate](#BKMK_CanCreate)
- [CanRead](#BKMK_CanRead)
- [CanReadUnMasked](#BKMK_CanReadUnMasked)
- [CanUpdate](#BKMK_CanUpdate)
- [EntityName](#BKMK_EntityName)
- [FieldPermissionId](#BKMK_FieldPermissionId)
- [FieldSecurityProfileId](#BKMK_FieldSecurityProfileId)

### <a name="BKMK_AttributeLogicalName"></a> AttributeLogicalName

|Property|Value|
|---|---|
|Description|**Attribute Name.**|
|DisplayName|**Name of the attribute for which this privilege is defined**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`attributelogicalname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_CanCreate"></a> CanCreate

|Property|Value|
|---|---|
|Description|**Can this Profile create the attribute**|
|DisplayName|**Can create the attribute**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cancreate`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`field_security_permission_type`|

#### CanCreate Choices/Options

|Value|Label|
|---|---|
|0|**Not Allowed**|
|4|**Allowed**|

### <a name="BKMK_CanRead"></a> CanRead

|Property|Value|
|---|---|
|Description|**Can this Profile read the attribute**|
|DisplayName|**Can Read the attribute**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`canread`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`field_security_permission_type`|

#### CanRead Choices/Options

|Value|Label|
|---|---|
|0|**Not Allowed**|
|4|**Allowed**|

### <a name="BKMK_CanReadUnMasked"></a> CanReadUnMasked

|Property|Value|
|---|---|
|Description||
|DisplayName|**Can this profile read unmasked value of attribute**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`canreadunmasked`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`field_security_permission_readunmasked`|

#### CanReadUnMasked Choices/Options

|Value|Label|
|---|---|
|0|**Not Allowed**|
|1|**One Record**|
|3|**All Records**|

### <a name="BKMK_CanUpdate"></a> CanUpdate

|Property|Value|
|---|---|
|Description|**Can this Profile update the attribute**|
|DisplayName|**Can Update the attribute**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`canupdate`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`field_security_permission_type`|

#### CanUpdate Choices/Options

|Value|Label|
|---|---|
|0|**Not Allowed**|
|4|**Allowed**|

### <a name="BKMK_EntityName"></a> EntityName

|Property|Value|
|---|---|
|Description|**Entity name.**|
|DisplayName|**Name of the Entity for which this privilege is defined**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityname`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_FieldPermissionId"></a> FieldPermissionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the Field Permission.**|
|DisplayName|**Field Permission**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fieldpermissionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_FieldSecurityProfileId"></a> FieldSecurityProfileId

|Property|Value|
|---|---|
|Description|**Unique identifier of profile to which this privilege belongs.**|
|DisplayName|**Profile**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`fieldsecurityprofileid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|fieldsecurityprofile|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [FieldPermissionIdUnique](#BKMK_FieldPermissionIdUnique)
- [IsManaged](#BKMK_IsManaged)
- [OrganizationId](#BKMK_OrganizationId)
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

### <a name="BKMK_FieldPermissionIdUnique"></a> FieldPermissionIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Field Permission**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fieldpermissionidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Indicates whether the solution component is part of a managed solution.**|
|DisplayName|**Is Managed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier for the organization**|
|DisplayName|**Organization Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets||

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

- [lk_fieldpermission_fieldsecurityprofileid](#BKMK_lk_fieldpermission_fieldsecurityprofileid)
- [solution_fieldpermission](#BKMK_solution_fieldpermission)

### <a name="BKMK_lk_fieldpermission_fieldsecurityprofileid"></a> lk_fieldpermission_fieldsecurityprofileid

One-To-Many Relationship: [fieldsecurityprofile lk_fieldpermission_fieldsecurityprofileid](fieldsecurityprofile.md#BKMK_lk_fieldpermission_fieldsecurityprofileid)

|Property|Value|
|---|---|
|ReferencedEntity|`fieldsecurityprofile`|
|ReferencedAttribute|`fieldsecurityprofileid`|
|ReferencingAttribute|`fieldsecurityprofileid`|
|ReferencingEntityNavigationPropertyName|`fieldsecurityprofileid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solution_fieldpermission"></a> solution_fieldpermission

One-To-Many Relationship: [solution solution_fieldpermission](solution.md#BKMK_solution_fieldpermission)

|Property|Value|
|---|---|
|ReferencedEntity|`solution`|
|ReferencedAttribute|`solutionid`|
|ReferencingAttribute|`solutionid`|
|ReferencingEntityNavigationPropertyName|`solution_fieldpermission`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_FieldPermission_SyncErrors"></a> FieldPermission_SyncErrors

Many-To-One Relationship: [syncerror FieldPermission_SyncErrors](syncerror.md#BKMK_FieldPermission_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`FieldPermission_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.fieldpermission?displayProperty=fullName>
