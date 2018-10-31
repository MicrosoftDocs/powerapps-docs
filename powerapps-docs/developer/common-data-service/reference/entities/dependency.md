---
title: "Dependency Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the Dependency entity."
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
ms.date: 10/31/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Dependency Entity Reference

A component dependency in CRM.

## Entity Properties

**DisplayName**: Dependency<br />
**DisplayCollectionName**: Dependency<br />
**SchemaName**: Dependency<br />
**CollectionSchemaName**: Dependency<br />
**LogicalName**: dependency<br />
**LogicalCollectionName**: dependencies<br />
**EntitySetName**: dependencies<br />
**PrimaryIdAttribute**: dependencyid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [DependencyId](#BKMK_DependencyId)
- [DependencyType](#BKMK_DependencyType)
- [DependentComponentBaseSolutionId](#BKMK_DependentComponentBaseSolutionId)
- [DependentComponentNodeId](#BKMK_DependentComponentNodeId)
- [DependentComponentObjectId](#BKMK_DependentComponentObjectId)
- [DependentComponentParentId](#BKMK_DependentComponentParentId)
- [DependentComponentType](#BKMK_DependentComponentType)
- [RequiredComponentBaseSolutionId](#BKMK_RequiredComponentBaseSolutionId)
- [RequiredComponentIntroducedVersion](#BKMK_RequiredComponentIntroducedVersion)
- [RequiredComponentNodeId](#BKMK_RequiredComponentNodeId)
- [RequiredComponentObjectId](#BKMK_RequiredComponentObjectId)
- [RequiredComponentParentId](#BKMK_RequiredComponentParentId)
- [RequiredComponentType](#BKMK_RequiredComponentType)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_DependencyId"></a> DependencyId

**Description**: Unique identifier of a dependency.<br />
**DisplayName**: Dependency Identifier<br />
**LogicalName**: dependencyid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_DependencyType"></a> DependencyType

**Description**: The dependency type of the dependency.<br />
**DisplayName**: Dependency Type<br />
**LogicalName**: dependencytype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: None
- **Value**: 1 **Label**: Solution Internal
- **Value**: 2 **Label**: Published
- **Value**: 4 **Label**: Unpublished



### <a name="BKMK_DependentComponentBaseSolutionId"></a> DependentComponentBaseSolutionId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: dependentcomponentbasesolutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_DependentComponentNodeId"></a> DependentComponentNodeId

**Description**: Unique identifier of the dependent component's node.<br />
**DisplayName**: Dependent Component<br />
**LogicalName**: dependentcomponentnodeid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Lookup<br />
**Targets**: dependencynode


### <a name="BKMK_DependentComponentObjectId"></a> DependentComponentObjectId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: dependentcomponentobjectid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_DependentComponentParentId"></a> DependentComponentParentId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: dependentcomponentparentid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_DependentComponentType"></a> DependentComponentType

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: dependentcomponenttype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
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



### <a name="BKMK_RequiredComponentBaseSolutionId"></a> RequiredComponentBaseSolutionId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: requiredcomponentbasesolutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_RequiredComponentIntroducedVersion"></a> RequiredComponentIntroducedVersion

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: requiredcomponentintroducedversion<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Double<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0<br />
**Precision**: 2


### <a name="BKMK_RequiredComponentNodeId"></a> RequiredComponentNodeId

**Description**: Unique identifier of the required component's node<br />
**DisplayName**: Required Component<br />
**LogicalName**: requiredcomponentnodeid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Lookup<br />
**Targets**: dependencynode


### <a name="BKMK_RequiredComponentObjectId"></a> RequiredComponentObjectId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: requiredcomponentobjectid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_RequiredComponentParentId"></a> RequiredComponentParentId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: requiredcomponentparentid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_RequiredComponentType"></a> RequiredComponentType

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: requiredcomponenttype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
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


### <a name="BKMK_userentityinstancedata_dependency"></a> userentityinstancedata_dependency

Same as userentityinstancedata entity [userentityinstancedata_dependency](userentityinstancedata.md#BKMK_userentityinstancedata_dependency) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_dependency<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade

dependency

