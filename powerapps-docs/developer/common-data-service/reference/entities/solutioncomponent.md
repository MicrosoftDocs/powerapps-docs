---
title: "SolutionComponent Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the SolutionComponent entity."

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
# SolutionComponent Entity Reference

A component of a CRM solution.

## Entity Properties

**DisplayName**: Solution Component<br />
**DisplayCollectionName**: Solution Components<br />
**SchemaName**: SolutionComponent<br />
**CollectionSchemaName**: SolutionComponents<br />
**LogicalName**: solutioncomponent<br />
**LogicalCollectionName**: solutioncomponentss<br />
**EntitySetName**: solutioncomponents<br />
**PrimaryIdAttribute**: solutioncomponentid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentType](#BKMK_ComponentType)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IsMetadata](#BKMK_IsMetadata)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [ObjectId](#BKMK_ObjectId)
- [RootComponentBehavior](#BKMK_RootComponentBehavior)
- [RootSolutionComponentId](#BKMK_RootSolutionComponentId)
- [SolutionComponentId](#BKMK_SolutionComponentId)
- [SolutionId](#BKMK_SolutionId)
- [SolutionIdName](#BKMK_SolutionIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ComponentType"></a> ComponentType

**Description**: The object type code of the component.<br />
**DisplayName**: Object Type Code<br />
**LogicalName**: componenttype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Entity
- **Value**: 2 **Label**: Attribute
- **Value**: 3 **Label**: Relationship
- **Value**: 4 **Label**: Attribute Picklist Value
- **Value**: 5 **Label**: Attribute Lookup Value
- **Value**: 6 **Label**: View Attribute
- **Value**: 7 **Label**: Localized Label
- **Value**: 8 **Label**: Relationship Extra Condition
- **Value**: 9 **Label**: Option Set
- **Value**: 10 **Label**: Entity Relationship
- **Value**: 11 **Label**: Entity Relationship Role
- **Value**: 12 **Label**: Entity Relationship Relationships
- **Value**: 13 **Label**: Managed Property
- **Value**: 14 **Label**: Entity Key
- **Value**: 16 **Label**: Privilege
- **Value**: 17 **Label**: PrivilegeObjectTypeCode
- **Value**: 18 **Label**: Index
- **Value**: 20 **Label**: Role
- **Value**: 21 **Label**: Role Privilege
- **Value**: 22 **Label**: Display String
- **Value**: 23 **Label**: Display String Map
- **Value**: 24 **Label**: Form
- **Value**: 25 **Label**: Organization
- **Value**: 26 **Label**: Saved Query
- **Value**: 29 **Label**: Workflow
- **Value**: 31 **Label**: Report
- **Value**: 32 **Label**: Report Entity
- **Value**: 33 **Label**: Report Category
- **Value**: 34 **Label**: Report Visibility
- **Value**: 35 **Label**: Attachment
- **Value**: 36 **Label**: Email Template
- **Value**: 37 **Label**: Contract Template
- **Value**: 38 **Label**: KB Article Template
- **Value**: 39 **Label**: Mail Merge Template
- **Value**: 44 **Label**: Duplicate Rule
- **Value**: 45 **Label**: Duplicate Rule Condition
- **Value**: 46 **Label**: Entity Map
- **Value**: 47 **Label**: Attribute Map
- **Value**: 48 **Label**: Ribbon Command
- **Value**: 49 **Label**: Ribbon Context Group
- **Value**: 50 **Label**: Ribbon Customization
- **Value**: 52 **Label**: Ribbon Rule
- **Value**: 53 **Label**: Ribbon Tab To Command Map
- **Value**: 55 **Label**: Ribbon Diff
- **Value**: 59 **Label**: Saved Query Visualization
- **Value**: 60 **Label**: System Form
- **Value**: 61 **Label**: Web Resource
- **Value**: 62 **Label**: Site Map
- **Value**: 63 **Label**: Connection Role
- **Value**: 64 **Label**: Complex Control
- **Value**: 65 **Label**: Hierarchy Rule
- **Value**: 66 **Label**: Custom Control
- **Value**: 68 **Label**: Custom Control Default Config
- **Value**: 70 **Label**: Field Security Profile
- **Value**: 71 **Label**: Field Permission
- **Value**: 90 **Label**: Plugin Type
- **Value**: 91 **Label**: Plugin Assembly
- **Value**: 92 **Label**: SDK Message Processing Step
- **Value**: 93 **Label**: SDK Message Processing Step Image
- **Value**: 95 **Label**: Service Endpoint
- **Value**: 150 **Label**: Routing Rule
- **Value**: 151 **Label**: Routing Rule Item
- **Value**: 152 **Label**: SLA
- **Value**: 153 **Label**: SLA Item
- **Value**: 154 **Label**: Convert Rule
- **Value**: 155 **Label**: Convert Rule Item
- **Value**: 161 **Label**: Mobile Offline Profile
- **Value**: 162 **Label**: Mobile Offline Profile Item
- **Value**: 165 **Label**: Similarity Rule
- **Value**: 166 **Label**: Data Source Mapping
- **Value**: 201 **Label**: SDKMessage
- **Value**: 202 **Label**: SDKMessageFilter
- **Value**: 203 **Label**: SdkMessagePair
- **Value**: 204 **Label**: SdkMessageRequest
- **Value**: 205 **Label**: SdkMessageRequestField
- **Value**: 206 **Label**: SdkMessageResponse
- **Value**: 207 **Label**: SdkMessageResponseField
- **Value**: 208 **Label**: Import Map
- **Value**: 210 **Label**: WebWizard



### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the solution<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the solution was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
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


### <a name="BKMK_IsMetadata"></a> IsMetadata

**Description**: Indicates whether this component is metadata or data.<br />
**DisplayName**: Is this component metadata<br />
**LogicalName**: ismetadata<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Metadata
- **FalseOption Value**: 0 **Label**: Data

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


### <a name="BKMK_ObjectId"></a> ObjectId

**Description**: Unique identifier of the object with which the component is associated.<br />
**DisplayName**: Regarding<br />
**LogicalName**: objectid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_RootComponentBehavior"></a> RootComponentBehavior

**Description**: Indicates the include behavior of the root component.<br />
**DisplayName**: Root Component Behavior<br />
**LogicalName**: rootcomponentbehavior<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Include Subcomponents
- **Value**: 1 **Label**: Do not include subcomponents
- **Value**: 2 **Label**: Include As Shell Only



### <a name="BKMK_RootSolutionComponentId"></a> RootSolutionComponentId

**Description**: The parent ID of the subcomponent, which will be a root<br />
**DisplayName**: Root Solution Component ID<br />
**LogicalName**: rootsolutioncomponentid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SolutionComponentId"></a> SolutionComponentId

**Description**: Unique identifier of the solution component.<br />
**DisplayName**: Solution Component Identifier<br />
**LogicalName**: solutioncomponentid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SolutionId"></a> SolutionId

**Description**: Unique identifier of the solution.<br />
**DisplayName**: Solution<br />
**LogicalName**: solutionid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: solution


### <a name="BKMK_SolutionIdName"></a> SolutionIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: solutionidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


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

- [solutioncomponent_parent_solutioncomponent](#BKMK_solutioncomponent_parent_solutioncomponent)
- [userentityinstancedata_solutioncomponent](#BKMK_userentityinstancedata_solutioncomponent)


### <a name="BKMK_solutioncomponent_parent_solutioncomponent"></a> solutioncomponent_parent_solutioncomponent

Same as solutioncomponent entity [solutioncomponent_parent_solutioncomponent](solutioncomponent.md#BKMK_solutioncomponent_parent_solutioncomponent) Many-To-One relationship.

**ReferencingEntity**: solutioncomponent<br />
**ReferencingAttribute**: rootsolutioncomponentid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: solutioncomponent_parent_solutioncomponent<br />
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


### <a name="BKMK_userentityinstancedata_solutioncomponent"></a> userentityinstancedata_solutioncomponent

Same as userentityinstancedata entity [userentityinstancedata_solutioncomponent](userentityinstancedata.md#BKMK_userentityinstancedata_solutioncomponent) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_solutioncomponent<br />
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

- [lk_solutioncomponentbase_modifiedonbehalfby](#BKMK_lk_solutioncomponentbase_modifiedonbehalfby)
- [solutioncomponent_parent_solutioncomponent](#BKMK_solutioncomponent_parent_solutioncomponent)
- [lk_solutioncomponentbase_createdonbehalfby](#BKMK_lk_solutioncomponentbase_createdonbehalfby)
- [solution_solutioncomponent](#BKMK_solution_solutioncomponent)


### <a name="BKMK_lk_solutioncomponentbase_modifiedonbehalfby"></a> lk_solutioncomponentbase_modifiedonbehalfby

See systemuser Entity [lk_solutioncomponentbase_modifiedonbehalfby](systemuser.md#BKMK_lk_solutioncomponentbase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_solutioncomponent_parent_solutioncomponent"></a> solutioncomponent_parent_solutioncomponent

See solutioncomponent Entity [solutioncomponent_parent_solutioncomponent](solutioncomponent.md#BKMK_solutioncomponent_parent_solutioncomponent) One-To-Many relationship.

### <a name="BKMK_lk_solutioncomponentbase_createdonbehalfby"></a> lk_solutioncomponentbase_createdonbehalfby

See systemuser Entity [lk_solutioncomponentbase_createdonbehalfby](systemuser.md#BKMK_lk_solutioncomponentbase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_solution_solutioncomponent"></a> solution_solutioncomponent

See solution Entity [solution_solutioncomponent](solution.md#BKMK_solution_solutioncomponent) One-To-Many relationship.
solutioncomponent

