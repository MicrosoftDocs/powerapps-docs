---
title: "SdkMessageFilter Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the SdkMessageFilter entity."
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
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# SdkMessageFilter Entity Reference

Filter that defines which SDK messages are valid for each type of entity.

## Entity Properties

**DisplayName**: Sdk Message Filter<br />
**DisplayCollectionName**: Sdk Message Filters<br />
**SchemaName**: SdkMessageFilter<br />
**CollectionSchemaName**: SdkMessageFilters<br />
**LogicalName**: sdkmessagefilter<br />
**LogicalCollectionName**: sdkmessagefilters<br />
**EntitySetName**: sdkmessagefilters<br />
**PrimaryIdAttribute**: sdkmessagefilterid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Availability](#BKMK_Availability)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCustomProcessingStepAllowed](#BKMK_IsCustomProcessingStepAllowed)
- [RestrictionLevel](#BKMK_RestrictionLevel)
- [SdkMessageFilterId](#BKMK_SdkMessageFilterId)
- [SdkMessageId](#BKMK_SdkMessageId)


### <a name="BKMK_Availability"></a> Availability

**Description**: Identifies where a method will be exposed. 0 - Server, 1 - Client, 2 - both.<br />
**DisplayName**: Availability<br />
**LogicalName**: availability<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

**Description**: Version in which the component is introduced.<br />
**DisplayName**: Introduced Version<br />
**LogicalName**: introducedversion<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: VersionNumber<br />
**IsLocalizable**: False<br />
**MaxLength**: 48


### <a name="BKMK_IsCustomProcessingStepAllowed"></a> IsCustomProcessingStepAllowed

**Description**: Indicates whether a custom SDK message processing step is allowed.<br />
**DisplayName**: Custom Processing Step Allowed<br />
**LogicalName**: iscustomprocessingstepallowed<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_RestrictionLevel"></a> RestrictionLevel

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: restrictionlevel<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 255<br />
**MinValue**: 0


### <a name="BKMK_SdkMessageFilterId"></a> SdkMessageFilterId

**Description**: Unique identifier of the SDK message filter entity.<br />
**DisplayName**: <br />
**LogicalName**: sdkmessagefilterid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SdkMessageId"></a> SdkMessageId

**Description**: Unique identifier of the related SDK message.<br />
**DisplayName**: SDK Message ID<br />
**LogicalName**: sdkmessageid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: sdkmessage

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [CustomizationLevel](#BKMK_CustomizationLevel)
- [IsManaged](#BKMK_IsManaged)
- [IsVisible](#BKMK_IsVisible)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [PrimaryObjectTypeCode](#BKMK_PrimaryObjectTypeCode)
- [SdkMessageFilterIdUnique](#BKMK_SdkMessageFilterIdUnique)
- [SdkMessageIdName](#BKMK_SdkMessageIdName)
- [SecondaryObjectTypeCode](#BKMK_SecondaryObjectTypeCode)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)
- [WorkflowSdkStepEnabled](#BKMK_WorkflowSdkStepEnabled)


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

**Description**: Unique identifier of the user who created the SDK message filter.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: False<br />
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

**Description**: Date and time when the SDK message filter was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the sdkmessagefilter.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: False<br />
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


### <a name="BKMK_CustomizationLevel"></a> CustomizationLevel

**Description**: Customization level of the SDK message filter.<br />
**DisplayName**: <br />
**LogicalName**: customizationlevel<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 255<br />
**MinValue**: -255


### <a name="BKMK_IsManaged"></a> IsManaged

**Description**: Information that specifies whether this component is managed.<br />
**DisplayName**: State<br />
**LogicalName**: ismanaged<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Managed
- **FalseOption Value**: 0 **Label**: Unmanaged

**DefaultValue**: False


### <a name="BKMK_IsVisible"></a> IsVisible

**Description**: Indicates whether the filter should be visible.<br />
**DisplayName**: <br />
**LogicalName**: isvisible<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the SDK message filter.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: False<br />
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

**Description**: Date and time when the SDK message filter was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the sdkmessagefilter.<br />
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

**Description**: Unique identifier of the organization with which the SDK message filter is associated.<br />
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


### <a name="BKMK_PrimaryObjectTypeCode"></a> PrimaryObjectTypeCode

**Description**: Type of entity with which the SDK message filter is primarily associated.<br />
**DisplayName**: Primary Object Type Code<br />
**LogicalName**: primaryobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_SdkMessageFilterIdUnique"></a> SdkMessageFilterIdUnique

**Description**: Unique identifier of the SDK message filter.<br />
**DisplayName**: <br />
**LogicalName**: sdkmessagefilteridunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SdkMessageIdName"></a> SdkMessageIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: sdkmessageidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_SecondaryObjectTypeCode"></a> SecondaryObjectTypeCode

**Description**: Type of entity with which the SDK message filter is secondarily associated.<br />
**DisplayName**: Secondary Object Type Code<br />
**LogicalName**: secondaryobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


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


### <a name="BKMK_WorkflowSdkStepEnabled"></a> WorkflowSdkStepEnabled

**Description**: Whether or not the SDK message can be called from a workflow.<br />
**DisplayName**: WorkflowSdkStepEnabled<br />
**LogicalName**: workflowsdkstepenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [sdkmessagefilterid_sdkmessageprocessingstep](#BKMK_sdkmessagefilterid_sdkmessageprocessingstep)
- [userentityinstancedata_sdkmessagefilter](#BKMK_userentityinstancedata_sdkmessagefilter)


### <a name="BKMK_sdkmessagefilterid_sdkmessageprocessingstep"></a> sdkmessagefilterid_sdkmessageprocessingstep

Same as sdkmessageprocessingstep entity [sdkmessagefilterid_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_sdkmessagefilterid_sdkmessageprocessingstep) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstep<br />
**ReferencingAttribute**: sdkmessagefilterid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: sdkmessagefilterid_sdkmessageprocessingstep<br />
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


### <a name="BKMK_userentityinstancedata_sdkmessagefilter"></a> userentityinstancedata_sdkmessagefilter

Same as userentityinstancedata entity [userentityinstancedata_sdkmessagefilter](userentityinstancedata.md#BKMK_userentityinstancedata_sdkmessagefilter) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_sdkmessagefilter<br />
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [createdby_sdkmessagefilter](#BKMK_createdby_sdkmessagefilter)
- [modifiedby_sdkmessagefilter](#BKMK_modifiedby_sdkmessagefilter)
- [sdkmessageid_sdkmessagefilter](#BKMK_sdkmessageid_sdkmessagefilter)
- [lk_sdkmessagefilter_createdonbehalfby](#BKMK_lk_sdkmessagefilter_createdonbehalfby)
- [organization_sdkmessagefilter](#BKMK_organization_sdkmessagefilter)
- [lk_sdkmessagefilter_modifiedonbehalfby](#BKMK_lk_sdkmessagefilter_modifiedonbehalfby)


### <a name="BKMK_createdby_sdkmessagefilter"></a> createdby_sdkmessagefilter

See systemuser Entity [createdby_sdkmessagefilter](systemuser.md#BKMK_createdby_sdkmessagefilter) One-To-Many relationship.

### <a name="BKMK_modifiedby_sdkmessagefilter"></a> modifiedby_sdkmessagefilter

See systemuser Entity [modifiedby_sdkmessagefilter](systemuser.md#BKMK_modifiedby_sdkmessagefilter) One-To-Many relationship.

### <a name="BKMK_sdkmessageid_sdkmessagefilter"></a> sdkmessageid_sdkmessagefilter

See sdkmessage Entity [sdkmessageid_sdkmessagefilter](sdkmessage.md#BKMK_sdkmessageid_sdkmessagefilter) One-To-Many relationship.

### <a name="BKMK_lk_sdkmessagefilter_createdonbehalfby"></a> lk_sdkmessagefilter_createdonbehalfby

See systemuser Entity [lk_sdkmessagefilter_createdonbehalfby](systemuser.md#BKMK_lk_sdkmessagefilter_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_sdkmessagefilter"></a> organization_sdkmessagefilter

See organization Entity [organization_sdkmessagefilter](organization.md#BKMK_organization_sdkmessagefilter) One-To-Many relationship.

### <a name="BKMK_lk_sdkmessagefilter_modifiedonbehalfby"></a> lk_sdkmessagefilter_modifiedonbehalfby

See systemuser Entity [lk_sdkmessagefilter_modifiedonbehalfby](systemuser.md#BKMK_lk_sdkmessagefilter_modifiedonbehalfby) One-To-Many relationship.
sdkmessagefilter

