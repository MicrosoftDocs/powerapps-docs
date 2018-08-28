---
title: "Solution Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the Solution entity."
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
# Solution Entity Reference

A solution which contains CRM customizations.

## Entity Properties

**DisplayName**: Solution<br />
**DisplayCollectionName**: Solutions<br />
**SchemaName**: Solution<br />
**CollectionSchemaName**: Solutions<br />
**LogicalName**: solution<br />
**LogicalCollectionName**: solutions<br />
**EntitySetName**: solutions<br />
**PrimaryIdAttribute**: solutionid<br />
**PrimaryNameAttribute**: friendlyname<br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ConfigurationPageId](#BKMK_ConfigurationPageId)
- [Description](#BKMK_Description)
- [FriendlyName](#BKMK_FriendlyName)
- [PublisherId](#BKMK_PublisherId)
- [SolutionId](#BKMK_SolutionId)
- [SolutionPackageVersion](#BKMK_SolutionPackageVersion)
- [SolutionType](#BKMK_SolutionType)
- [UniqueName](#BKMK_UniqueName)
- [Version](#BKMK_Version)


### <a name="BKMK_ConfigurationPageId"></a> ConfigurationPageId

**Description**: A link to an optional configuration page for this solution.<br />
**DisplayName**: Configuration Page<br />
**LogicalName**: configurationpageid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: webresource


### <a name="BKMK_Description"></a> Description

**Description**: Description of the solution.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: TextArea<br />
**IsLocalizable**: True<br />
**MaxLength**: 2000


### <a name="BKMK_FriendlyName"></a> FriendlyName

**Description**: User display name for the solution.<br />
**DisplayName**: Display Name<br />
**LogicalName**: friendlyname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: True<br />
**MaxLength**: 256


### <a name="BKMK_PublisherId"></a> PublisherId

**Description**: Unique identifier of the publisher.<br />
**DisplayName**: Publisher<br />
**LogicalName**: publisherid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: publisher


### <a name="BKMK_SolutionId"></a> SolutionId

**Description**: Unique identifier of the solution.<br />
**DisplayName**: Solution Identifier<br />
**LogicalName**: solutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SolutionPackageVersion"></a> SolutionPackageVersion

**Description**: Solution package source organization version<br />
**DisplayName**: Solution Package Version<br />
**LogicalName**: solutionpackageversion<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: VersionNumber<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_SolutionType"></a> SolutionType

**Description**: Solution Type<br />
**DisplayName**: Solution Type<br />
**LogicalName**: solutiontype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: None
- **Value**: 1 **Label**: Snapshot
- **Value**: 2 **Label**: Internal



### <a name="BKMK_UniqueName"></a> UniqueName

**Description**: The unique name of this solution<br />
**DisplayName**: Name<br />
**LogicalName**: uniquename<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 65


### <a name="BKMK_Version"></a> Version

**Description**: Solution version, used to identify a solution for upgrades and hotfixes.<br />
**DisplayName**: Version<br />
**LogicalName**: version<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: VersionNumber<br />
**IsLocalizable**: False<br />
**MaxLength**: 256

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ConfigurationPageIdName](#BKMK_ConfigurationPageIdName)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [InstalledOn](#BKMK_InstalledOn)
- [IsInternal](#BKMK_IsInternal)
- [IsManaged](#BKMK_IsManaged)
- [IsVisible](#BKMK_IsVisible)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [ParentSolutionId](#BKMK_ParentSolutionId)
- [ParentSolutionIdName](#BKMK_ParentSolutionIdName)
- [PinpointAssetId](#BKMK_PinpointAssetId)
- [PinpointPublisherId](#BKMK_PinpointPublisherId)
- [PinpointSolutionDefaultLocale](#BKMK_PinpointSolutionDefaultLocale)
- [PinpointSolutionId](#BKMK_PinpointSolutionId)
- [PublisherIdName](#BKMK_PublisherIdName)
- [PublisherIdOptionValuePrefix](#BKMK_PublisherIdOptionValuePrefix)
- [PublisherIdPrefix](#BKMK_PublisherIdPrefix)
- [UpdatedOn](#BKMK_UpdatedOn)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ConfigurationPageIdName"></a> ConfigurationPageIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: configurationpageidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the solution.<br />
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

**Description**: Date and time when the solution was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the solution.<br />
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


### <a name="BKMK_InstalledOn"></a> InstalledOn

**Description**: Date and time when the solution was installed/upgraded.<br />
**DisplayName**: Installed On<br />
**LogicalName**: installedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_IsInternal"></a> IsInternal

**Description**: Indicates whether the solution is internal or not.<br />
**DisplayName**: Is internal solution<br />
**LogicalName**: isinternal<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsManaged"></a> IsManaged

**Description**: Indicates whether the solution is managed or unmanaged.<br />
**DisplayName**: Package Type<br />
**LogicalName**: ismanaged<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Managed
- **FalseOption Value**: 0 **Label**: Unmanaged

**DefaultValue**: False


### <a name="BKMK_IsVisible"></a> IsVisible

**Description**: Indicates whether the solution is visible outside of the platform.<br />
**DisplayName**: Is Visible Outside Platform<br />
**LogicalName**: isvisible<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the solution.<br />
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

**Description**: Date and time when the solution was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who modified the solution.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: True<br />
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

**Description**: Unique identifier of the organization associated with the solution.<br />
**DisplayName**: Organization<br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: organization


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: organizationidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ParentSolutionId"></a> ParentSolutionId

**Description**: Unique identifier of the parent solution. Should only be non-null if this solution is a patch.<br />
**DisplayName**: Parent Solution<br />
**LogicalName**: parentsolutionid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: solution


### <a name="BKMK_ParentSolutionIdName"></a> ParentSolutionIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: parentsolutionidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_PinpointAssetId"></a> PinpointAssetId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: pinpointassetid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 255


### <a name="BKMK_PinpointPublisherId"></a> PinpointPublisherId

**Description**: Identifier of the publisher of this solution in Microsoft Pinpoint.<br />
**DisplayName**: <br />
**LogicalName**: pinpointpublisherid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />


### <a name="BKMK_PinpointSolutionDefaultLocale"></a> PinpointSolutionDefaultLocale

**Description**: Default locale of the solution in Microsoft Pinpoint.<br />
**DisplayName**: <br />
**LogicalName**: pinpointsolutiondefaultlocale<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 16


### <a name="BKMK_PinpointSolutionId"></a> PinpointSolutionId

**Description**: Identifier of the solution in Microsoft Pinpoint.<br />
**DisplayName**: <br />
**LogicalName**: pinpointsolutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />


### <a name="BKMK_PublisherIdName"></a> PublisherIdName

**Description**: name of the publisher.<br />
**DisplayName**: Publisher<br />
**LogicalName**: publisheridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_PublisherIdOptionValuePrefix"></a> PublisherIdOptionValuePrefix

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: publisheridoptionvalueprefix<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_PublisherIdPrefix"></a> PublisherIdPrefix

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: publisheridprefix<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_UpdatedOn"></a> UpdatedOn

**Description**: Date and time when the solution was updated.<br />
**DisplayName**: Updated On<br />
**LogicalName**: updatedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


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

- [solution_solutioncomponent](#BKMK_solution_solutioncomponent)
- [solution_parent_solution](#BKMK_solution_parent_solution)
- [Solution_SyncErrors](#BKMK_Solution_SyncErrors)
- [userentityinstancedata_solution](#BKMK_userentityinstancedata_solution)


### <a name="BKMK_solution_solutioncomponent"></a> solution_solutioncomponent

Same as solutioncomponent entity [solution_solutioncomponent](solutioncomponent.md#BKMK_solution_solutioncomponent) Many-To-One relationship.

**ReferencingEntity**: solutioncomponent<br />
**ReferencingAttribute**: solutionid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: solution_solutioncomponent<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_solution_parent_solution"></a> solution_parent_solution

Same as solution entity [solution_parent_solution](solution.md#BKMK_solution_parent_solution) Many-To-One relationship.

**ReferencingEntity**: solution<br />
**ReferencingAttribute**: parentsolutionid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: solution_parent_solution<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_Solution_SyncErrors"></a> Solution_SyncErrors

Same as syncerror entity [Solution_SyncErrors](syncerror.md#BKMK_Solution_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: Solution_SyncErrors<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_userentityinstancedata_solution"></a> userentityinstancedata_solution

Same as userentityinstancedata entity [userentityinstancedata_solution](userentityinstancedata.md#BKMK_userentityinstancedata_solution) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_solution<br />
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

- [lk_solution_createdby](#BKMK_lk_solution_createdby)
- [lk_solution_modifiedby](#BKMK_lk_solution_modifiedby)
- [solution_parent_solution](#BKMK_solution_parent_solution)
- [solution_configuration_webresource](#BKMK_solution_configuration_webresource)
- [lk_solutionbase_modifiedonbehalfby](#BKMK_lk_solutionbase_modifiedonbehalfby)
- [organization_solution](#BKMK_organization_solution)
- [lk_solutionbase_createdonbehalfby](#BKMK_lk_solutionbase_createdonbehalfby)
- [publisher_solution](#BKMK_publisher_solution)


### <a name="BKMK_lk_solution_createdby"></a> lk_solution_createdby

See systemuser Entity [lk_solution_createdby](systemuser.md#BKMK_lk_solution_createdby) One-To-Many relationship.

### <a name="BKMK_lk_solution_modifiedby"></a> lk_solution_modifiedby

See systemuser Entity [lk_solution_modifiedby](systemuser.md#BKMK_lk_solution_modifiedby) One-To-Many relationship.

### <a name="BKMK_solution_parent_solution"></a> solution_parent_solution

See solution Entity [solution_parent_solution](solution.md#BKMK_solution_parent_solution) One-To-Many relationship.

### <a name="BKMK_solution_configuration_webresource"></a> solution_configuration_webresource

See webresource Entity [solution_configuration_webresource](webresource.md#BKMK_solution_configuration_webresource) One-To-Many relationship.

### <a name="BKMK_lk_solutionbase_modifiedonbehalfby"></a> lk_solutionbase_modifiedonbehalfby

See systemuser Entity [lk_solutionbase_modifiedonbehalfby](systemuser.md#BKMK_lk_solutionbase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_solution"></a> organization_solution

See organization Entity [organization_solution](organization.md#BKMK_organization_solution) One-To-Many relationship.

### <a name="BKMK_lk_solutionbase_createdonbehalfby"></a> lk_solutionbase_createdonbehalfby

See systemuser Entity [lk_solutionbase_createdonbehalfby](systemuser.md#BKMK_lk_solutionbase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_publisher_solution"></a> publisher_solution

See publisher Entity [publisher_solution](publisher.md#BKMK_publisher_solution) One-To-Many relationship.
solution

