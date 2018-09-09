---
title: "EntityDataSource Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the EntityDataSource entity."
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: kvivek
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
# EntityDataSource Entity Reference

Internal entity that stores data source information for all installed providers.

## Entity Properties

**DisplayName**: Virtual Entity Data Source<br />
**DisplayCollectionName**: Virtual Entity Data Sources<br />
**SchemaName**: EntityDataSource<br />
**CollectionSchemaName**: EntityDataSources<br />
**LogicalName**: entitydatasource<br />
**LogicalCollectionName**: entitydatasources<br />
**EntitySetName**: entitydatasources<br />
**PrimaryIdAttribute**: entitydatasourceid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ConnectionDefinition](#BKMK_ConnectionDefinition)
- [ConnectionDefinitionSecrets](#BKMK_ConnectionDefinitionSecrets)
- [Description](#BKMK_Description)
- [EntityDataProviderId](#BKMK_EntityDataProviderId)
- [EntityDataSourceId](#BKMK_EntityDataSourceId)
- [EntityName](#BKMK_EntityName)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCustomizable](#BKMK_IsCustomizable)
- [Name](#BKMK_Name)


### <a name="BKMK_ConnectionDefinition"></a> ConnectionDefinition

**Description**: JSON data representing values from a data source entity as individual fields.<br />
**DisplayName**: Data Source Values<br />
**LogicalName**: connectiondefinition<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_ConnectionDefinitionSecrets"></a> ConnectionDefinitionSecrets

**Description**: JSON data representing secrets in a data source entity as individual fields.<br />
**DisplayName**: Data Source Secrets<br />
**LogicalName**: connectiondefinitionsecrets<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_Description"></a> Description

**Description**: Enter additional information to describe the environment this data source targets and the purpose of this system.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1000


### <a name="BKMK_EntityDataProviderId"></a> EntityDataProviderId

**Description**: Choose the entity dataprovider for the entity datasource.<br />
**DisplayName**: Entity Provider<br />
**LogicalName**: entitydataproviderid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: contact


### <a name="BKMK_EntityDataSourceId"></a> EntityDataSourceId

**Description**: Unique identifier of the Data Source Id<br />
**DisplayName**: Data Source Id<br />
**LogicalName**: entitydatasourceid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_EntityName"></a> EntityName

**Description**: Entity Logical Name<br />
**DisplayName**: Entity Logical Name<br />
**LogicalName**: entityname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

**Description**: Version in which the form is introduced.<br />
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


### <a name="BKMK_IsCustomizable"></a> IsCustomizable

**Description**: Information that specifies whether this component can be customized.<br />
**DisplayName**: Customizable<br />
**LogicalName**: iscustomizable<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: ManagedProperty<br />


### <a name="BKMK_Name"></a> Name

**Description**: Name of this data source. This name appears in the data source drop-down when creating a new entity.<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [EntityDataProviderIdName](#BKMK_EntityDataProviderIdName)
- [EntityDataSourceIdUnique](#BKMK_EntityDataSourceIdUnique)
- [IsManaged](#BKMK_IsManaged)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)


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



### <a name="BKMK_EntityDataProviderIdName"></a> EntityDataProviderIdName

**Description**: <br />
**DisplayName**: Entity Provider Name<br />
**LogicalName**: entitydataprovideridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_EntityDataSourceIdUnique"></a> EntityDataSourceIdUnique

**Description**: For internal use only.<br />
**DisplayName**: Unique Id<br />
**LogicalName**: entitydatasourceidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_IsManaged"></a> IsManaged

**Description**: Indicates whether the solution component is part of a managed solution.<br />
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


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier for the organization.<br />
**DisplayName**: Organization Id<br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [entitydataprovider_datasource](#BKMK_entitydataprovider_datasource)
- [organization_entitydatasource](#BKMK_organization_entitydatasource)


### <a name="BKMK_entitydataprovider_datasource"></a> entitydataprovider_datasource

See entitydataprovider Entity [entitydataprovider_datasource](entitydataprovider.md#BKMK_entitydataprovider_datasource) One-To-Many relationship.

### <a name="BKMK_organization_entitydatasource"></a> organization_entitydatasource

See organization Entity [organization_entitydatasource](organization.md#BKMK_organization_entitydatasource) One-To-Many relationship.
entitydatasource

