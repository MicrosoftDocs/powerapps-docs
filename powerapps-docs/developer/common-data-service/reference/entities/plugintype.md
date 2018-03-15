---
title: "PluginType Entity Reference (Common Data Service for Apps)| MicrosoftDocs"
description: "Includes schema information and supported messages for the PluginType entity."

services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/07/2018
ms.author: jdaly
---
# PluginType Entity Reference

Type that inherits from the IPlugin interface and is contained within a plug-in assembly.

## Entity Properties

**DisplayName**: Plug-in Type<br />
**DisplayCollectionName**: Plug-in Types<br />
**SchemaName**: PluginType<br />
**CollectionSchemaName**: PluginTypes<br />
**LogicalName**: plugintype<br />
**LogicalCollectionName**: plugintypes<br />
**EntitySetName**: plugintypes<br />
**PrimaryIdAttribute**: plugintypeid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Description](#BKMK_Description)
- [FriendlyName](#BKMK_FriendlyName)
- [Name](#BKMK_Name)
- [PluginAssemblyId](#BKMK_PluginAssemblyId)
- [PluginTypeId](#BKMK_PluginTypeId)
- [TypeName](#BKMK_TypeName)
- [WorkflowActivityGroupName](#BKMK_WorkflowActivityGroupName)


### <a name="BKMK_Description"></a> Description

**Description**: Description of the plug-in type.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_FriendlyName"></a> FriendlyName

**Description**: User friendly name for the plug-in.<br />
**DisplayName**: Display Name<br />
**LogicalName**: friendlyname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_Name"></a> Name

**Description**: Name of the plug-in type.<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_PluginAssemblyId"></a> PluginAssemblyId

**Description**: Unique identifier of the plug-in assembly that contains this plug-in type.<br />
**DisplayName**: Plugin Assembly<br />
**LogicalName**: pluginassemblyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: pluginassembly


### <a name="BKMK_PluginTypeId"></a> PluginTypeId

**Description**: Unique identifier of the plug-in type.<br />
**DisplayName**: Plug-in Type<br />
**LogicalName**: plugintypeid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_TypeName"></a> TypeName

**Description**: Fully qualified type name of the plug-in type.<br />
**DisplayName**: Type Name<br />
**LogicalName**: typename<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_WorkflowActivityGroupName"></a> WorkflowActivityGroupName

**Description**: Group name of workflow custom activity.<br />
**DisplayName**: Workflow Activity Group Name<br />
**LogicalName**: workflowactivitygroupname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AssemblyName](#BKMK_AssemblyName)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [Culture](#BKMK_Culture)
- [CustomizationLevel](#BKMK_CustomizationLevel)
- [CustomWorkflowActivityInfo](#BKMK_CustomWorkflowActivityInfo)
- [IsManaged](#BKMK_IsManaged)
- [IsWorkflowActivity](#BKMK_IsWorkflowActivity)
- [Major](#BKMK_Major)
- [Minor](#BKMK_Minor)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [PluginAssemblyIdName](#BKMK_PluginAssemblyIdName)
- [PluginTypeIdUnique](#BKMK_PluginTypeIdUnique)
- [PublicKeyToken](#BKMK_PublicKeyToken)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [Version](#BKMK_Version)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_AssemblyName"></a> AssemblyName

**Description**: Full path name of the plug-in assembly.<br />
**DisplayName**: Assembly Name<br />
**LogicalName**: assemblyname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ComponentState"></a> ComponentState

**Description**: For internal use only.<br />
**DisplayName**: Component State<br />
**LogicalName**: componentstate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Published
- **Value**: 1 **Label**: Unpublished
- **Value**: 2 **Label**: Deleted
- **Value**: 3 **Label**: Deleted Unpublished



### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the plug-in type.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the plug-in type was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the plugintype.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_Culture"></a> Culture

**Description**: Culture code for the plug-in assembly.<br />
**DisplayName**: Culture<br />
**LogicalName**: culture<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 32


### <a name="BKMK_CustomizationLevel"></a> CustomizationLevel

**Description**: Customization level of the plug-in type.<br />
**DisplayName**: <br />
**LogicalName**: customizationlevel<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 255<br />
**MinValue**: -255


### <a name="BKMK_CustomWorkflowActivityInfo"></a> CustomWorkflowActivityInfo

**Description**: Serialized Custom Activity Type information, including required arguments. For more information, see SandboxCustomActivityInfo.<br />
**DisplayName**: Custom Workflow Activity Info<br />
**LogicalName**: customworkflowactivityinfo<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1048576


### <a name="BKMK_IsManaged"></a> IsManaged

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: ismanaged<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Managed
- **FalseOption Value**: 0 **Label**: Unmanaged

**DefaultValue**: False


### <a name="BKMK_IsWorkflowActivity"></a> IsWorkflowActivity

**Description**: Indicates if the plug-in is a custom activity for workflows.<br />
**DisplayName**: Is Workflow Activity<br />
**LogicalName**: isworkflowactivity<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_Major"></a> Major

**Description**: Major of the version number of the assembly for the plug-in type.<br />
**DisplayName**: Version major<br />
**LogicalName**: major<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 65534<br />
**MinValue**: 0


### <a name="BKMK_Minor"></a> Minor

**Description**: Minor of the version number of the assembly for the plug-in type.<br />
**DisplayName**: Version minor<br />
**LogicalName**: minor<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 65534<br />
**MinValue**: 0


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the plug-in type.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the plug-in type was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the plugintype.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization with which the plug-in type is associated.<br />
**DisplayName**: <br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: organization


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

**Description**: For internal use only.<br />
**DisplayName**: Record Overwrite Time<br />
**LogicalName**: overwritetime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_PluginAssemblyIdName"></a> PluginAssemblyIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: pluginassemblyidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_PluginTypeIdUnique"></a> PluginTypeIdUnique

**Description**: Unique identifier of the plug-in type.<br />
**DisplayName**: <br />
**LogicalName**: plugintypeidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_PublicKeyToken"></a> PublicKeyToken

**Description**: Public key token of the assembly for the plug-in type.<br />
**DisplayName**: Public Key Token<br />
**LogicalName**: publickeytoken<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 32


### <a name="BKMK_SolutionId"></a> SolutionId

**Description**: Unique identifier of the associated solution.<br />
**DisplayName**: Solution<br />
**LogicalName**: solutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

**Description**: For internal use only.<br />
**DisplayName**: Solution<br />
**LogicalName**: supportingsolutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_Version"></a> Version

**Description**: Version number of the assembly for the plug-in type.<br />
**DisplayName**: Version<br />
**LogicalName**: version<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: VersionNumber<br />
**IsLocalizable**: False<br />
**MaxLength**: 48


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: versionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [plugintype_sdkmessageprocessingstep](#BKMK_plugintype_sdkmessageprocessingstep)
- [plugintype_plugintypestatistic](#BKMK_plugintype_plugintypestatistic)
- [userentityinstancedata_plugintype](#BKMK_userentityinstancedata_plugintype)
- [plugintypeid_sdkmessageprocessingstep](#BKMK_plugintypeid_sdkmessageprocessingstep)


### <a name="BKMK_plugintype_sdkmessageprocessingstep"></a> plugintype_sdkmessageprocessingstep

Same as sdkmessageprocessingstep entity [plugintype_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_plugintype_sdkmessageprocessingstep) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstep<br />
**ReferencingAttribute**: eventhandler<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: plugintype_sdkmessageprocessingstep<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_plugintype_plugintypestatistic"></a> plugintype_plugintypestatistic

Same as plugintypestatistic entity [plugintype_plugintypestatistic](plugintypestatistic.md#BKMK_plugintype_plugintypestatistic) Many-To-One relationship.

**ReferencingEntity**: plugintypestatistic<br />
**ReferencingAttribute**: plugintypeid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: plugintype_plugintypestatistic<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_userentityinstancedata_plugintype"></a> userentityinstancedata_plugintype

Same as userentityinstancedata entity [userentityinstancedata_plugintype](userentityinstancedata.md#BKMK_userentityinstancedata_plugintype) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_plugintype<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_plugintypeid_sdkmessageprocessingstep"></a> plugintypeid_sdkmessageprocessingstep

Same as sdkmessageprocessingstep entity [plugintypeid_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_plugintypeid_sdkmessageprocessingstep) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstep<br />
**ReferencingAttribute**: plugintypeid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: plugintypeid_sdkmessageprocessingstep<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [pluginassembly_plugintype](#BKMK_pluginassembly_plugintype)
- [lk_plugintype_createdonbehalfby](#BKMK_lk_plugintype_createdonbehalfby)
- [organization_plugintype](#BKMK_organization_plugintype)
- [modifiedby_plugintype](#BKMK_modifiedby_plugintype)
- [createdby_plugintype](#BKMK_createdby_plugintype)
- [lk_plugintype_modifiedonbehalfby](#BKMK_lk_plugintype_modifiedonbehalfby)


### <a name="BKMK_pluginassembly_plugintype"></a> pluginassembly_plugintype

See pluginassembly Entity [pluginassembly_plugintype](pluginassembly.md#BKMK_pluginassembly_plugintype) One-To-Many relationship.

### <a name="BKMK_lk_plugintype_createdonbehalfby"></a> lk_plugintype_createdonbehalfby

See systemuser Entity [lk_plugintype_createdonbehalfby](systemuser.md#BKMK_lk_plugintype_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_plugintype"></a> organization_plugintype

See organization Entity [organization_plugintype](organization.md#BKMK_organization_plugintype) One-To-Many relationship.

### <a name="BKMK_modifiedby_plugintype"></a> modifiedby_plugintype

See systemuser Entity [modifiedby_plugintype](systemuser.md#BKMK_modifiedby_plugintype) One-To-Many relationship.

### <a name="BKMK_createdby_plugintype"></a> createdby_plugintype

See systemuser Entity [createdby_plugintype](systemuser.md#BKMK_createdby_plugintype) One-To-Many relationship.

### <a name="BKMK_lk_plugintype_modifiedonbehalfby"></a> lk_plugintype_modifiedonbehalfby

See systemuser Entity [lk_plugintype_modifiedonbehalfby](systemuser.md#BKMK_lk_plugintype_modifiedonbehalfby) One-To-Many relationship.
plugintype

