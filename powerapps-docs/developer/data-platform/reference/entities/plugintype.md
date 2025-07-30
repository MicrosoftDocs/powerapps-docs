---
title: "Plug-in Type (PluginType) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Plug-in Type (PluginType) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Plug-in Type (PluginType) table/entity reference (Microsoft Dataverse)

Type that inherits from the IPlugin interface and is contained within a plug-in assembly.

## Messages

The following table lists the messages for the Plug-in Type (PluginType) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /plugintypes<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /plugintypes(*plugintypeid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /plugintypes(*plugintypeid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /plugintypes<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /plugintypes(*plugintypeid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /plugintypes(*plugintypeid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Plug-in Type (PluginType) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Plug-in Type** |
| **DisplayCollectionName** | **Plug-in Types** |
| **SchemaName** | `PluginType` |
| **CollectionSchemaName** | `PluginTypes` |
| **EntitySetName** | `plugintypes`|
| **LogicalName** | `plugintype` |
| **LogicalCollectionName** | `plugintypes` |
| **PrimaryIdAttribute** | `plugintypeid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Description](#BKMK_Description)
- [FriendlyName](#BKMK_FriendlyName)
- [Name](#BKMK_Name)
- [PluginAssemblyId](#BKMK_PluginAssemblyId)
- [PluginTypeExportKey](#BKMK_PluginTypeExportKey)
- [PluginTypeId](#BKMK_PluginTypeId)
- [TypeName](#BKMK_TypeName)
- [WorkflowActivityGroupName](#BKMK_WorkflowActivityGroupName)

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the plug-in type.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_FriendlyName"></a> FriendlyName

|Property|Value|
|---|---|
|Description|**User friendly name for the plug-in.**|
|DisplayName|**Display Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`friendlyname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the plug-in type.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_PluginAssemblyId"></a> PluginAssemblyId

|Property|Value|
|---|---|
|Description|**Unique identifier of the plug-in assembly that contains this plug-in type.**|
|DisplayName|**Plugin Assembly**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`pluginassemblyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|pluginassembly|

### <a name="BKMK_PluginTypeExportKey"></a> PluginTypeExportKey

|Property|Value|
|---|---|
|Description|**Uniquely identifies the plug-in type associated with a plugin package when exporting a solution.**|
|DisplayName|**Plugin Type export key**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`plugintypeexportkey`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_PluginTypeId"></a> PluginTypeId

|Property|Value|
|---|---|
|Description|**Unique identifier of the plug-in type.**|
|DisplayName|**Plug-in Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`plugintypeid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_TypeName"></a> TypeName

|Property|Value|
|---|---|
|Description|**Fully qualified type name of the plug-in type.**|
|DisplayName|**Type Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`typename`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_WorkflowActivityGroupName"></a> WorkflowActivityGroupName

|Property|Value|
|---|---|
|Description|**Group name of workflow custom activity.**|
|DisplayName|**Workflow Activity Group Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`workflowactivitygroupname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [AssemblyName](#BKMK_AssemblyName)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [Culture](#BKMK_Culture)
- [CustomizationLevel](#BKMK_CustomizationLevel)
- [CustomWorkflowActivityInfo](#BKMK_CustomWorkflowActivityInfo)
- [IsManaged](#BKMK_IsManaged)
- [IsWorkflowActivity](#BKMK_IsWorkflowActivity)
- [Major](#BKMK_Major)
- [Minor](#BKMK_Minor)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [PluginTypeIdUnique](#BKMK_PluginTypeIdUnique)
- [PublicKeyToken](#BKMK_PublicKeyToken)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [Version](#BKMK_Version)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_AssemblyName"></a> AssemblyName

|Property|Value|
|---|---|
|Description|**Full path name of the plug-in assembly.**|
|DisplayName|**Assembly Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`assemblyname`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the plug-in type.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the plug-in type was created.**|
|DisplayName|**Created On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who created the plugintype.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_Culture"></a> Culture

|Property|Value|
|---|---|
|Description|**Culture code for the plug-in assembly.**|
|DisplayName|**Culture**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`culture`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|32|

### <a name="BKMK_CustomizationLevel"></a> CustomizationLevel

|Property|Value|
|---|---|
|Description|**Customization level of the plug-in type.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`customizationlevel`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|255|
|MinValue|-255|

### <a name="BKMK_CustomWorkflowActivityInfo"></a> CustomWorkflowActivityInfo

|Property|Value|
|---|---|
|Description|**Serialized Custom Activity Type information, including required arguments. For more information, see SandboxCustomActivityInfo.**|
|DisplayName|**Custom Workflow Activity Info**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`customworkflowactivityinfo`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

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

### <a name="BKMK_IsWorkflowActivity"></a> IsWorkflowActivity

|Property|Value|
|---|---|
|Description|**Indicates if the plug-in is a custom activity for workflows.**|
|DisplayName|**Is Workflow Activity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isworkflowactivity`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`plugintype_isworkflowactivity`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Major"></a> Major

|Property|Value|
|---|---|
|Description|**Major of the version number of the assembly for the plug-in type.**|
|DisplayName|**Version major**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`major`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|65534|
|MinValue|0|

### <a name="BKMK_Minor"></a> Minor

|Property|Value|
|---|---|
|Description|**Minor of the version number of the assembly for the plug-in type.**|
|DisplayName|**Version minor**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`minor`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|65534|
|MinValue|0|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the plug-in type.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the plug-in type was last modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who last modified the plugintype.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization with which the plug-in type is associated.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

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

### <a name="BKMK_PluginTypeIdUnique"></a> PluginTypeIdUnique

|Property|Value|
|---|---|
|Description|**Unique identifier of the plug-in type.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`plugintypeidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_PublicKeyToken"></a> PublicKeyToken

|Property|Value|
|---|---|
|Description|**Public key token of the assembly for the plug-in type.**|
|DisplayName|**Public Key Token**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`publickeytoken`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|32|

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

### <a name="BKMK_Version"></a> Version

|Property|Value|
|---|---|
|Description|**Version number of the assembly for the plug-in type.**|
|DisplayName|**Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`version`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|VersionNumber|
|FormatName|VersionNumber|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|48|

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

- [createdby_plugintype](#BKMK_createdby_plugintype)
- [lk_plugintype_createdonbehalfby](#BKMK_lk_plugintype_createdonbehalfby)
- [lk_plugintype_modifiedonbehalfby](#BKMK_lk_plugintype_modifiedonbehalfby)
- [modifiedby_plugintype](#BKMK_modifiedby_plugintype)
- [organization_plugintype](#BKMK_organization_plugintype)
- [pluginassembly_plugintype](#BKMK_pluginassembly_plugintype)

### <a name="BKMK_createdby_plugintype"></a> createdby_plugintype

One-To-Many Relationship: [systemuser createdby_plugintype](systemuser.md#BKMK_createdby_plugintype)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_plugintype_createdonbehalfby"></a> lk_plugintype_createdonbehalfby

One-To-Many Relationship: [systemuser lk_plugintype_createdonbehalfby](systemuser.md#BKMK_lk_plugintype_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_plugintype_modifiedonbehalfby"></a> lk_plugintype_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_plugintype_modifiedonbehalfby](systemuser.md#BKMK_lk_plugintype_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_modifiedby_plugintype"></a> modifiedby_plugintype

One-To-Many Relationship: [systemuser modifiedby_plugintype](systemuser.md#BKMK_modifiedby_plugintype)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_plugintype"></a> organization_plugintype

One-To-Many Relationship: [organization organization_plugintype](organization.md#BKMK_organization_plugintype)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_pluginassembly_plugintype"></a> pluginassembly_plugintype

One-To-Many Relationship: [pluginassembly pluginassembly_plugintype](pluginassembly.md#BKMK_pluginassembly_plugintype)

|Property|Value|
|---|---|
|ReferencedEntity|`pluginassembly`|
|ReferencedAttribute|`pluginassemblyid`|
|ReferencingAttribute|`pluginassemblyid`|
|ReferencingEntityNavigationPropertyName|`pluginassemblyid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [plugintype_customapi](#BKMK_plugintype_customapi)
- [plugintype_plugintypestatistic](#BKMK_plugintype_plugintypestatistic)
- [plugintype_sdkmessageprocessingstep](#BKMK_plugintype_sdkmessageprocessingstep)
- [plugintypeid_sdkmessageprocessingstep](#BKMK_plugintypeid_sdkmessageprocessingstep)

### <a name="BKMK_plugintype_customapi"></a> plugintype_customapi

Many-To-One Relationship: [customapi plugintype_customapi](customapi.md#BKMK_plugintype_customapi)

|Property|Value|
|---|---|
|ReferencingEntity|`customapi`|
|ReferencingAttribute|`plugintypeid`|
|ReferencedEntityNavigationPropertyName|`CustomAPIId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_plugintype_plugintypestatistic"></a> plugintype_plugintypestatistic

Many-To-One Relationship: [plugintypestatistic plugintype_plugintypestatistic](plugintypestatistic.md#BKMK_plugintype_plugintypestatistic)

|Property|Value|
|---|---|
|ReferencingEntity|`plugintypestatistic`|
|ReferencingAttribute|`plugintypeid`|
|ReferencedEntityNavigationPropertyName|`plugintype_plugintypestatistic`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_plugintype_sdkmessageprocessingstep"></a> plugintype_sdkmessageprocessingstep

Many-To-One Relationship: [sdkmessageprocessingstep plugintype_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_plugintype_sdkmessageprocessingstep)

|Property|Value|
|---|---|
|ReferencingEntity|`sdkmessageprocessingstep`|
|ReferencingAttribute|`eventhandler`|
|ReferencedEntityNavigationPropertyName|`plugintype_sdkmessageprocessingstep`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_plugintypeid_sdkmessageprocessingstep"></a> plugintypeid_sdkmessageprocessingstep

Many-To-One Relationship: [sdkmessageprocessingstep plugintypeid_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_plugintypeid_sdkmessageprocessingstep)

|Property|Value|
|---|---|
|ReferencingEntity|`sdkmessageprocessingstep`|
|ReferencingAttribute|`plugintypeid`|
|ReferencedEntityNavigationPropertyName|`plugintypeid_sdkmessageprocessingstep`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.plugintype?displayProperty=fullName>
