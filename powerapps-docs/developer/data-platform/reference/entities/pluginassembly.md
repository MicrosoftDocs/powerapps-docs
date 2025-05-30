---
title: "Plug-in Assembly (PluginAssembly) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Plug-in Assembly (PluginAssembly) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Plug-in Assembly (PluginAssembly) table/entity reference (Microsoft Dataverse)

Assembly that contains one or more plug-in types.

## Messages

The following table lists the messages for the Plug-in Assembly (PluginAssembly) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /pluginassemblies<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /pluginassemblies(*pluginassemblyid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /pluginassemblies(*pluginassemblyid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /pluginassemblies<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /pluginassemblies(*pluginassemblyid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /pluginassemblies(*pluginassemblyid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Plug-in Assembly (PluginAssembly) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Plug-in Assembly** |
| **DisplayCollectionName** | **Plug-in Assemblies** |
| **SchemaName** | `PluginAssembly` |
| **CollectionSchemaName** | `PluginAssemblies` |
| **EntitySetName** | `pluginassemblies`|
| **LogicalName** | `pluginassembly` |
| **LogicalCollectionName** | `pluginassemblies` |
| **PrimaryIdAttribute** | `pluginassemblyid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AuthType](#BKMK_AuthType)
- [Content](#BKMK_Content)
- [Culture](#BKMK_Culture)
- [Description](#BKMK_Description)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsHidden](#BKMK_IsHidden)
- [IsolationMode](#BKMK_IsolationMode)
- [ManagedIdentityId](#BKMK_ManagedIdentityId)
- [Name](#BKMK_Name)
- [PackageId](#BKMK_PackageId)
- [Password](#BKMK_Password)
- [Path](#BKMK_Path)
- [PluginAssemblyId](#BKMK_PluginAssemblyId)
- [PublicKeyToken](#BKMK_PublicKeyToken)
- [SourceHash](#BKMK_SourceHash)
- [SourceType](#BKMK_SourceType)
- [Url](#BKMK_Url)
- [UserName](#BKMK_UserName)
- [Version](#BKMK_Version)

### <a name="BKMK_AuthType"></a> AuthType

|Property|Value|
|---|---|
|Description|**Specifies mode of authentication with web sources like WebApp**|
|DisplayName|**Specifies mode of authentication with web sources**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`authtype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`pluginassembly_authtype`|

#### AuthType Choices/Options

|Value|Label|
|---|---|
|0|**BasicAuth**|

### <a name="BKMK_Content"></a> Content

|Property|Value|
|---|---|
|Description|**Bytes of the assembly, in Base64 format.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`content`|
|RequiredLevel|None|
|Type|String|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_Culture"></a> Culture

|Property|Value|
|---|---|
|Description|**Culture code for the plug-in assembly.**|
|DisplayName|**Culture**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`culture`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|32|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the plug-in assembly.**|
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

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Version in which the form is introduced.**|
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

### <a name="BKMK_IsHidden"></a> IsHidden

|Property|Value|
|---|---|
|Description|**Information that specifies whether this component should be hidden.**|
|DisplayName|**Hidden**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ishidden`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_IsolationMode"></a> IsolationMode

|Property|Value|
|---|---|
|Description|**Information about how the plugin assembly is to be isolated at execution time; None / Sandboxed.**|
|DisplayName|**Isolation Mode**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isolationmode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`pluginassembly_isolationmode`|

#### IsolationMode Choices/Options

|Value|Label|
|---|---|
|1|**None**|
|2|**Sandbox**|
|3|**External**|

### <a name="BKMK_ManagedIdentityId"></a> ManagedIdentityId

|Property|Value|
|---|---|
|Description|**Unique identifier for managedidentity associated with pluginassembly.**|
|DisplayName|**ManagedIdentityId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`managedidentityid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|managedidentity|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the plug-in assembly.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_PackageId"></a> PackageId

|Property|Value|
|---|---|
|Description|**Unique identifier for Plugin Package associated with Plug-in Assembly.**|
|DisplayName|**Package**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`packageid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|pluginpackage|

### <a name="BKMK_Password"></a> Password

|Property|Value|
|---|---|
|Description|**User Password**|
|DisplayName|**User Password**|
|IsValidForForm|True|
|IsValidForRead|False|
|LogicalName|`password`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_Path"></a> Path

|Property|Value|
|---|---|
|Description|**File name of the plug-in assembly. Used when the source type is set to 1.**|
|DisplayName|**Path**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`path`|
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
|Description|**Unique identifier of the plug-in assembly.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`pluginassemblyid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_PublicKeyToken"></a> PublicKeyToken

|Property|Value|
|---|---|
|Description|**Public key token of the assembly. This value can be obtained from the assembly by using reflection.**|
|DisplayName|**Public Key Token**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`publickeytoken`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|32|

### <a name="BKMK_SourceHash"></a> SourceHash

|Property|Value|
|---|---|
|Description|**Hash of the source of the assembly.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sourcehash`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_SourceType"></a> SourceType

|Property|Value|
|---|---|
|Description|**Location of the assembly, for example 0=database, 1=on-disk.**|
|DisplayName|**Source Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sourcetype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`pluginassembly_sourcetype`|

#### SourceType Choices/Options

|Value|Label|
|---|---|
|0|**Database**|
|1|**Disk**|
|2|**Normal**|
|3|**AzureWebApp**|
|4|**File Store**|

### <a name="BKMK_Url"></a> Url

|Property|Value|
|---|---|
|Description|**Web Url**|
|DisplayName|**Web Url**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`url`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_UserName"></a> UserName

|Property|Value|
|---|---|
|Description|**User Name**|
|DisplayName|**User Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`username`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_Version"></a> Version

|Property|Value|
|---|---|
|Description|**Version number of the assembly. The value can be obtained from the assembly through reflection.**|
|DisplayName|**Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`version`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|VersionNumber|
|FormatName|VersionNumber|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|48|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CustomizationLevel](#BKMK_CustomizationLevel)
- [IsManaged](#BKMK_IsManaged)
- [IsPasswordSet](#BKMK_IsPasswordSet)
- [Major](#BKMK_Major)
- [Minor](#BKMK_Minor)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [PluginAssemblyIdUnique](#BKMK_PluginAssemblyIdUnique)
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

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the plug-in assembly.**|
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
|Description|**Date and time when the plug-in assembly was created.**|
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
|Description|**Unique identifier of the delegate user who created the pluginassembly.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CustomizationLevel"></a> CustomizationLevel

|Property|Value|
|---|---|
|Description|**Customization Level.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`customizationlevel`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|255|
|MinValue|-255|

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

### <a name="BKMK_IsPasswordSet"></a> IsPasswordSet

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ispasswordset`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`isencryptedattributevalueset`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Major"></a> Major

|Property|Value|
|---|---|
|Description|**Major of the assembly version.**|
|DisplayName||
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
|Description|**Minor of the assembly version.**|
|DisplayName||
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
|Description|**Unique identifier of the user who last modified the plug-in assembly.**|
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
|Description|**Date and time when the plug-in assembly was last modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the pluginassembly.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization with which the plug-in assembly is associated.**|
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

### <a name="BKMK_PluginAssemblyIdUnique"></a> PluginAssemblyIdUnique

|Property|Value|
|---|---|
|Description|**Unique identifier of the plug-in assembly.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`pluginassemblyidunique`|
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

- [createdby_pluginassembly](#BKMK_createdby_pluginassembly)
- [lk_pluginassembly_createdonbehalfby](#BKMK_lk_pluginassembly_createdonbehalfby)
- [lk_pluginassembly_modifiedonbehalfby](#BKMK_lk_pluginassembly_modifiedonbehalfby)
- [managedidentity_PluginAssembly](#BKMK_managedidentity_PluginAssembly)
- [modifiedby_pluginassembly](#BKMK_modifiedby_pluginassembly)
- [organization_pluginassembly](#BKMK_organization_pluginassembly)
- [pluginpackage_pluginassembly](#BKMK_pluginpackage_pluginassembly)

### <a name="BKMK_createdby_pluginassembly"></a> createdby_pluginassembly

One-To-Many Relationship: [systemuser createdby_pluginassembly](systemuser.md#BKMK_createdby_pluginassembly)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_pluginassembly_createdonbehalfby"></a> lk_pluginassembly_createdonbehalfby

One-To-Many Relationship: [systemuser lk_pluginassembly_createdonbehalfby](systemuser.md#BKMK_lk_pluginassembly_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_pluginassembly_modifiedonbehalfby"></a> lk_pluginassembly_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_pluginassembly_modifiedonbehalfby](systemuser.md#BKMK_lk_pluginassembly_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_managedidentity_PluginAssembly"></a> managedidentity_PluginAssembly

One-To-Many Relationship: [managedidentity managedidentity_PluginAssembly](managedidentity.md#BKMK_managedidentity_PluginAssembly)

|Property|Value|
|---|---|
|ReferencedEntity|`managedidentity`|
|ReferencedAttribute|`managedidentityid`|
|ReferencingAttribute|`managedidentityid`|
|ReferencingEntityNavigationPropertyName|`managedidentityid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_modifiedby_pluginassembly"></a> modifiedby_pluginassembly

One-To-Many Relationship: [systemuser modifiedby_pluginassembly](systemuser.md#BKMK_modifiedby_pluginassembly)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_pluginassembly"></a> organization_pluginassembly

One-To-Many Relationship: [organization organization_pluginassembly](organization.md#BKMK_organization_pluginassembly)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_pluginpackage_pluginassembly"></a> pluginpackage_pluginassembly

One-To-Many Relationship: [pluginpackage pluginpackage_pluginassembly](pluginpackage.md#BKMK_pluginpackage_pluginassembly)

|Property|Value|
|---|---|
|ReferencedEntity|`pluginpackage`|
|ReferencedAttribute|`pluginpackageid`|
|ReferencingAttribute|`packageid`|
|ReferencingEntityNavigationPropertyName|`PackageId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_pluginassembly_plugintype"></a> pluginassembly_plugintype

Many-To-One Relationship: [plugintype pluginassembly_plugintype](plugintype.md#BKMK_pluginassembly_plugintype)

|Property|Value|
|---|---|
|ReferencingEntity|`plugintype`|
|ReferencingAttribute|`pluginassemblyid`|
|ReferencedEntityNavigationPropertyName|`pluginassembly_plugintype`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.pluginassembly?displayProperty=fullName>
