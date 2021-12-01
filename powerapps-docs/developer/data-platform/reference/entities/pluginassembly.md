---
title: "Plug-in Assembly (PluginAssembly) table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Plug-in Assembly (PluginAssembly) table/entity."
ms.date: 10/05/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "margoc"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Plug-in Assembly (PluginAssembly) table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Assembly that contains one or more plug-in types.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/pluginassemblies<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/pluginassemblies(*pluginassemblyid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/pluginassemblies(*pluginassemblyid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/pluginassemblies<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/pluginassemblies(*pluginassemblyid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|PluginAssemblies|
|DisplayCollectionName|Plug-in Assemblies|
|DisplayName|Plug-in Assembly|
|EntitySetName|pluginassemblies|
|IsBPFEntity|False|
|LogicalCollectionName|pluginassemblies|
|LogicalName|pluginassembly|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|pluginassemblyid|
|PrimaryNameAttribute|name|
|SchemaName|PluginAssembly|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description|Specifies mode of authentication with web sources like WebApp|
|DisplayName|Specifies mode of authentication with web sources|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|authtype|
|RequiredLevel|None|
|Type|Picklist|

#### AuthType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|BasicAuth||



### <a name="BKMK_Content"></a> Content

|Property|Value|
|--------|-----|
|Description|Bytes of the assembly, in Base64 format.|
|DisplayName||
|FormatName|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|content|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Culture"></a> Culture

|Property|Value|
|--------|-----|
|Description|Culture code for the plug-in assembly.|
|DisplayName|Culture|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|culture|
|MaxLength|32|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Description of the plug-in assembly.|
|DisplayName|Description|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|--------|-----|
|Description|Version in which the form is introduced.|
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


### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|--------|-----|
|Description|Information that specifies whether this component can be customized.|
|DisplayName|Customizable|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iscustomizable|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_IsHidden"></a> IsHidden

|Property|Value|
|--------|-----|
|Description|Information that specifies whether this component should be hidden.|
|DisplayName|Hidden|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ishidden|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_IsolationMode"></a> IsolationMode

|Property|Value|
|--------|-----|
|Description|Information about how the plugin assembly is to be isolated at execution time; None / Sandboxed.|
|DisplayName|Isolation Mode|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isolationmode|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### IsolationMode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|None||
|2|Sandbox||
|3|External||



### <a name="BKMK_ManagedIdentityId"></a> ManagedIdentityId

**Added by**: ManagedIdentityExtensions Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for managedidentity associated with pluginassembly.|
|DisplayName|ManagedIdentityId|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|managedidentityid|
|RequiredLevel|None|
|Targets|managedidentity|
|Type|Lookup|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of the plug-in assembly.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|256|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_PackageId"></a> PackageId

**Added by**: Plugin Infrastructure Extension Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for Plugin Package associated with Plug-in Assembly.|
|DisplayName|Package|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|packageid|
|RequiredLevel|None|
|Targets|pluginpackage|
|Type|Lookup|


### <a name="BKMK_Password"></a> Password

|Property|Value|
|--------|-----|
|Description|User Password|
|DisplayName|User Password|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|False|
|LogicalName|password|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Path"></a> Path

|Property|Value|
|--------|-----|
|Description|File name of the plug-in assembly. Used when the source type is set to 1.|
|DisplayName|Path|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|path|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PluginAssemblyId"></a> PluginAssemblyId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the plug-in assembly.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|pluginassemblyid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_PublicKeyToken"></a> PublicKeyToken

|Property|Value|
|--------|-----|
|Description|Public key token of the assembly. This value can be obtained from the assembly by using reflection.|
|DisplayName|Public Key Token|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|publickeytoken|
|MaxLength|32|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_SourceHash"></a> SourceHash

|Property|Value|
|--------|-----|
|Description|Hash of the source of the assembly.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|sourcehash|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SourceType"></a> SourceType

|Property|Value|
|--------|-----|
|Description|Location of the assembly, for example 0=database, 1=on-disk.|
|DisplayName|Source Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|sourcetype|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### SourceType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Database||
|1|Disk||
|2|Normal||
|3|AzureWebApp||



### <a name="BKMK_Url"></a> Url

|Property|Value|
|--------|-----|
|Description|Web Url|
|DisplayName|Web Url|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|url|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_UserName"></a> UserName

|Property|Value|
|--------|-----|
|Description|User Name|
|DisplayName|User Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|username|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Version"></a> Version

|Property|Value|
|--------|-----|
|Description|Version number of the assembly. The value can be obtained from the assembly through reflection.|
|DisplayName|Version|
|FormatName|VersionNumber|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|version|
|MaxLength|48|
|RequiredLevel|SystemRequired|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [CustomizationLevel](#BKMK_CustomizationLevel)
- [IsManaged](#BKMK_IsManaged)
- [IsPasswordSet](#BKMK_IsPasswordSet)
- [Major](#BKMK_Major)
- [managedidentityidName](#BKMK_managedidentityidName)
- [Minor](#BKMK_Minor)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [PackageIdName](#BKMK_PackageIdName)
- [PluginAssemblyIdUnique](#BKMK_PluginAssemblyIdUnique)
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

|Value|Label|Description|
|-----|-----|--------|
|0|Published||
|1|Unpublished||
|2|Deleted||
|3|Deleted Unpublished||



### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the plug-in assembly.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the plug-in assembly was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the pluginassembly.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CustomizationLevel"></a> CustomizationLevel

|Property|Value|
|--------|-----|
|Description|Customization Level.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|customizationlevel|
|MaxValue|255|
|MinValue|-255|
|RequiredLevel|SystemRequired|
|Type|Integer|


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

|Value|Label|Description|
|-----|-----|--------|
|1|Managed|
|0|Unmanaged|

**DefaultValue**: False



### <a name="BKMK_IsPasswordSet"></a> IsPasswordSet

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ispasswordset|
|RequiredLevel|None|
|Type|Boolean|

#### IsPasswordSet Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_Major"></a> Major

|Property|Value|
|--------|-----|
|Description|Major of the assembly version.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|major|
|MaxValue|65534|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_managedidentityidName"></a> managedidentityidName

**Added by**: ManagedIdentityExtensions Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|managedidentityidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Minor"></a> Minor

|Property|Value|
|--------|-----|
|Description|Minor of the assembly version.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|minor|
|MaxValue|65534|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the plug-in assembly.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the plug-in assembly was last modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who last modified the pluginassembly.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the organization with which the plug-in assembly is associated.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|SystemRequired|
|Targets|organization|
|Type|Lookup|


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


### <a name="BKMK_PackageIdName"></a> PackageIdName

**Added by**: Plugin Infrastructure Extension Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|packageidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PluginAssemblyIdUnique"></a> PluginAssemblyIdUnique

|Property|Value|
|--------|-----|
|Description|Unique identifier of the plug-in assembly.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|pluginassemblyidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


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


### <a name="BKMK_pluginassembly_plugintype"></a> pluginassembly_plugintype

Same as plugintype table [pluginassembly_plugintype](plugintype.md#BKMK_pluginassembly_plugintype) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|plugintype|
|ReferencingAttribute|pluginassemblyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|pluginassembly_plugintype|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [modifiedby_pluginassembly](#BKMK_modifiedby_pluginassembly)
- [createdby_pluginassembly](#BKMK_createdby_pluginassembly)
- [organization_pluginassembly](#BKMK_organization_pluginassembly)
- [lk_pluginassembly_modifiedonbehalfby](#BKMK_lk_pluginassembly_modifiedonbehalfby)
- [lk_pluginassembly_createdonbehalfby](#BKMK_lk_pluginassembly_createdonbehalfby)
- [pluginpackage_pluginassembly](#BKMK_pluginpackage_pluginassembly)
- [managedidentity_PluginAssembly](#BKMK_managedidentity_PluginAssembly)


### <a name="BKMK_modifiedby_pluginassembly"></a> modifiedby_pluginassembly

See systemuser Table [modifiedby_pluginassembly](systemuser.md#BKMK_modifiedby_pluginassembly) One-To-Many relationship.

### <a name="BKMK_createdby_pluginassembly"></a> createdby_pluginassembly

See systemuser Table [createdby_pluginassembly](systemuser.md#BKMK_createdby_pluginassembly) One-To-Many relationship.

### <a name="BKMK_organization_pluginassembly"></a> organization_pluginassembly

See organization Table [organization_pluginassembly](organization.md#BKMK_organization_pluginassembly) One-To-Many relationship.

### <a name="BKMK_lk_pluginassembly_modifiedonbehalfby"></a> lk_pluginassembly_modifiedonbehalfby

See systemuser Table [lk_pluginassembly_modifiedonbehalfby](systemuser.md#BKMK_lk_pluginassembly_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_pluginassembly_createdonbehalfby"></a> lk_pluginassembly_createdonbehalfby

See systemuser Table [lk_pluginassembly_createdonbehalfby](systemuser.md#BKMK_lk_pluginassembly_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_pluginpackage_pluginassembly"></a> pluginpackage_pluginassembly

**Added by**: Plugin Infrastructure Extension Solution

See pluginpackage Table [pluginpackage_pluginassembly](pluginpackage.md#BKMK_pluginpackage_pluginassembly) One-To-Many relationship.

### <a name="BKMK_managedidentity_PluginAssembly"></a> managedidentity_PluginAssembly

**Added by**: ManagedIdentityExtensions Solution

See managedidentity Table [managedidentity_PluginAssembly](managedidentity.md#BKMK_managedidentity_PluginAssembly) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.pluginassembly?text=pluginassembly EntityType" />