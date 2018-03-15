---
title: "InvalidDependency Entity Reference (Common Data Service for Apps)| MicrosoftDocs"
description: "Includes schema information and supported messages for the InvalidDependency entity."

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
# InvalidDependency Entity Reference

An invalid dependency in the CRM system.

## Entity Properties

**DisplayName**: Invalid Dependency<br />
**DisplayCollectionName**: Invalid Dependencies<br />
**SchemaName**: InvalidDependency<br />
**CollectionSchemaName**: InvalidDependencies<br />
**LogicalName**: invaliddependency<br />
**LogicalCollectionName**: invaliddependencies<br />
**EntitySetName**: invaliddependencies<br />
**PrimaryIdAttribute**: invaliddependencyid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.


### <a name="BKMK_MissingComponentId"></a> MissingComponentId

**Description**: Unique identifier of the missing component.<br />
**DisplayName**: Regarding<br />
**LogicalName**: missingcomponentid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Uniqueidentifier<br />

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ExistingComponentId](#BKMK_ExistingComponentId)
- [ExistingComponentType](#BKMK_ExistingComponentType)
- [ExistingDependencyType](#BKMK_ExistingDependencyType)
- [InvalidDependencyId](#BKMK_InvalidDependencyId)
- [IsExistingNodeRequiredComponent](#BKMK_IsExistingNodeRequiredComponent)
- [MissingComponentInfo](#BKMK_MissingComponentInfo)
- [MissingComponentLookupType](#BKMK_MissingComponentLookupType)
- [MissingComponentType](#BKMK_MissingComponentType)


### <a name="BKMK_ExistingComponentId"></a> ExistingComponentId

**Description**: Unique identifier of the object that has an invalid dependency<br />
**DisplayName**: Existing Object Id<br />
**LogicalName**: existingcomponentid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ExistingComponentType"></a> ExistingComponentType

**Description**: Component type of the object that has an invalid dependency<br />
**DisplayName**: Existing Object's Component Type<br />
**LogicalName**: existingcomponenttype<br />
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



### <a name="BKMK_ExistingDependencyType"></a> ExistingDependencyType

**Description**: The dependency type of the invalid dependency.<br />
**DisplayName**: Weight<br />
**LogicalName**: existingdependencytype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: None
- **Value**: 1 **Label**: Solution Internal
- **Value**: 2 **Label**: Published
- **Value**: 4 **Label**: Unpublished



### <a name="BKMK_InvalidDependencyId"></a> InvalidDependencyId

**Description**: Unique identifier of the invalid dependency.<br />
**DisplayName**: Invalid Dependency Identifier<br />
**LogicalName**: invaliddependencyid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_IsExistingNodeRequiredComponent"></a> IsExistingNodeRequiredComponent

**Description**: Indicates whether the existing node is the required component in the dependency<br />
**DisplayName**: Is this node the required component<br />
**LogicalName**: isexistingnoderequiredcomponent<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Ancestor
- **FalseOption Value**: 0 **Label**: Descendent

**DefaultValue**: True


### <a name="BKMK_MissingComponentInfo"></a> MissingComponentInfo

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: missingcomponentinfo<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_MissingComponentLookupType"></a> MissingComponentLookupType

**Description**: The lookup type of the missing component.<br />
**DisplayName**: Lookup Type<br />
**LogicalName**: missingcomponentlookuptype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_MissingComponentType"></a> MissingComponentType

**Description**: The object type code of the missing component.<br />
**DisplayName**: Type Code<br />
**LogicalName**: missingcomponenttype<br />
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


<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_userentityinstancedata_invaliddependency"></a> userentityinstancedata_invaliddependency

Same as userentityinstancedata entity [userentityinstancedata_invaliddependency](userentityinstancedata.md#BKMK_userentityinstancedata_invaliddependency) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_invaliddependency<br />
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

invaliddependency

