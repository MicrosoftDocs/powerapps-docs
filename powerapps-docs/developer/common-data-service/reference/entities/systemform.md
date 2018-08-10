---
title: "SystemForm Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the SystemForm entity."

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
---
# SystemForm Entity Reference

Organization-owned entity customizations including form layout and dashboards.

## Entity Properties

**DisplayName**: System Form<br />
**DisplayCollectionName**: System Forms<br />
**SchemaName**: SystemForm<br />
**CollectionSchemaName**: SystemForms<br />
**LogicalName**: systemform<br />
**LogicalCollectionName**: systemforms<br />
**EntitySetName**: systemforms<br />
**PrimaryIdAttribute**: formid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AncestorFormId](#BKMK_AncestorFormId)
- [CanBeDeleted](#BKMK_CanBeDeleted)
- [Description](#BKMK_Description)
- [FormActivationState](#BKMK_FormActivationState)
- [FormId](#BKMK_FormId)
- [FormJson](#BKMK_FormJson)
- [FormPresentation](#BKMK_FormPresentation)
- [FormXml](#BKMK_FormXml)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsAIRMerged](#BKMK_IsAIRMerged)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsDefault](#BKMK_IsDefault)
- [IsDesktopEnabled](#BKMK_IsDesktopEnabled)
- [IsTabletEnabled](#BKMK_IsTabletEnabled)
- [Name](#BKMK_Name)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [Type](#BKMK_Type)
- [UniqueName](#BKMK_UniqueName)
- [Version](#BKMK_Version)


### <a name="BKMK_AncestorFormId"></a> AncestorFormId

**Description**: Unique identifier of the parent form.<br />
**DisplayName**: Parent Form<br />
**LogicalName**: ancestorformid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: systemform


### <a name="BKMK_CanBeDeleted"></a> CanBeDeleted

**Description**: Information that specifies whether this component can be deleted.<br />
**DisplayName**: Can Be Deleted<br />
**LogicalName**: canbedeleted<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: ManagedProperty<br />


### <a name="BKMK_Description"></a> Description

**Description**: Description of the form or dashboard.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: Text<br />
**IsLocalizable**: True<br />
**MaxLength**: 2000


### <a name="BKMK_FormActivationState"></a> FormActivationState

**Description**: Specifies the state of the form.<br />
**DisplayName**: Form State<br />
**LogicalName**: formactivationstate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Inactive
- **Value**: 1 **Label**: Active



### <a name="BKMK_FormId"></a> FormId

**Description**: Unique identifier of the record type form.<br />
**DisplayName**: <br />
**LogicalName**: formid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_FormJson"></a> FormJson

**Description**: Json representation of the form layout.<br />
**DisplayName**: <br />
**LogicalName**: formjson<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_FormPresentation"></a> FormPresentation

**Description**: Specifies whether this form is in the updated UI layout in Microsoft Dynamics CRM 2015 or Microsoft Dynamics CRM Online 2015 Update.<br />
**DisplayName**: AIR Refreshed<br />
**LogicalName**: formpresentation<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: ClassicForm
- **Value**: 1 **Label**: AirForm
- **Value**: 2 **Label**: ConvertedICForm



### <a name="BKMK_FormXml"></a> FormXml

**Description**: XML representation of the form layout.<br />
**DisplayName**: <br />
**LogicalName**: formxml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


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


### <a name="BKMK_IsAIRMerged"></a> IsAIRMerged

**Description**: Specifies whether this form is merged with the updated UI layout in Microsoft Dynamics CRM 2015 or Microsoft Dynamics CRM Online 2015 Update.<br />
**DisplayName**: Refreshed<br />
**LogicalName**: isairmerged<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsCustomizable"></a> IsCustomizable

**Description**: Information that specifies whether this component can be customized.<br />
**DisplayName**: Customizable<br />
**LogicalName**: iscustomizable<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: ManagedProperty<br />


### <a name="BKMK_IsDefault"></a> IsDefault

**Description**: Information that specifies whether the form or the dashboard is the system default.<br />
**DisplayName**: Default Form<br />
**LogicalName**: isdefault<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsDesktopEnabled"></a> IsDesktopEnabled

**Description**: Information that specifies whether the dashboard is enabled for desktop.<br />
**DisplayName**: Is Desktop Enabled<br />
**LogicalName**: isdesktopenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsTabletEnabled"></a> IsTabletEnabled

**Description**: Information that specifies whether the dashboard is enabled for tablet.<br />
**DisplayName**: Is Tablet Enabled<br />
**LogicalName**: istabletenabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_Name"></a> Name

**Description**: Name of the form.<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: True<br />
**MaxLength**: 100


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

**Description**: Code that represents the record type.<br />
**DisplayName**: Entity Name<br />
**LogicalName**: objecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_Type"></a> Type

**Description**: Type of the form, for example, Dashboard or Preview.<br />
**DisplayName**: Form Type<br />
**LogicalName**: type<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Dashboard
- **Value**: 1 **Label**: AppointmentBook
- **Value**: 2 **Label**: Main
- **Value**: 3 **Label**: MiniCampaignBO
- **Value**: 4 **Label**: Preview
- **Value**: 5 **Label**: Mobile - Express
- **Value**: 6 **Label**: Quick View Form
- **Value**: 7 **Label**: Quick Create
- **Value**: 8 **Label**: Dialog
- **Value**: 9 **Label**: Task Flow Form
- **Value**: 10 **Label**: InteractionCentricDashboard
- **Value**: 11 **Label**: Card
- **Value**: 12 **Label**: Main - Interactive experience
- **Value**: 100 **Label**: Other
- **Value**: 101 **Label**: MainBackup
- **Value**: 102 **Label**: AppointmentBookBackup
- **Value**: 103 **Label**: Power BI Dashboard



### <a name="BKMK_UniqueName"></a> UniqueName

**Description**: Unique Name<br />
**DisplayName**: Unique Name<br />
**LogicalName**: uniquename<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_Version"></a> Version

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: version<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AncestorFormIdName](#BKMK_AncestorFormIdName)
- [ComponentState](#BKMK_ComponentState)
- [FormIdUnique](#BKMK_FormIdUnique)
- [FormXmlManaged](#BKMK_FormXmlManaged)
- [IsManaged](#BKMK_IsManaged)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [PublishedOn](#BKMK_PublishedOn)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_AncestorFormIdName"></a> AncestorFormIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: ancestorformidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


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



### <a name="BKMK_FormIdUnique"></a> FormIdUnique

**Description**: Unique identifier of the form used when synchronizing customizations for the Microsoft Dynamics 365 client for Outlook.<br />
**DisplayName**: <br />
**LogicalName**: formidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_FormXmlManaged"></a> FormXmlManaged

**Description**: formXml diff as in a managed solution. for internal use only<br />
**DisplayName**: <br />
**LogicalName**: formxmlmanaged<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_IsManaged"></a> IsManaged

**Description**: <br />
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

**Description**: Unique identifier of the organization.<br />
**DisplayName**: <br />
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


### <a name="BKMK_PublishedOn"></a> PublishedOn

**Description**: <br />
**DisplayName**: Published On<br />
**LogicalName**: publishedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


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

**Description**: Represents a version of customizations to be synchronized with the Microsoft Dynamics 365 client for Outlook.<br />
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

- [socialinsightsconfiguration_systemform](#BKMK_socialinsightsconfiguration_systemform)
- [form_ancestor_form](#BKMK_form_ancestor_form)
- [SystemForm_AsyncOperations](#BKMK_SystemForm_AsyncOperations)
- [processtrigger_systemform](#BKMK_processtrigger_systemform)
- [SystemForm_BulkDeleteFailures](#BKMK_SystemForm_BulkDeleteFailures)


### <a name="BKMK_socialinsightsconfiguration_systemform"></a> socialinsightsconfiguration_systemform

Same as socialinsightsconfiguration entity [socialinsightsconfiguration_systemform](socialinsightsconfiguration.md#BKMK_socialinsightsconfiguration_systemform) Many-To-One relationship.

**ReferencingEntity**: socialinsightsconfiguration<br />
**ReferencingAttribute**: formid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: socialinsightsconfiguration_systemform<br />
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


### <a name="BKMK_form_ancestor_form"></a> form_ancestor_form

Same as systemform entity [form_ancestor_form](systemform.md#BKMK_form_ancestor_form) Many-To-One relationship.

**ReferencingEntity**: systemform<br />
**ReferencingAttribute**: ancestorformid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: form_ancestor_form<br />
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


### <a name="BKMK_SystemForm_AsyncOperations"></a> SystemForm_AsyncOperations

Same as asyncoperation entity [SystemForm_AsyncOperations](asyncoperation.md#BKMK_SystemForm_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: SystemForm_AsyncOperations<br />
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


### <a name="BKMK_processtrigger_systemform"></a> processtrigger_systemform

Same as processtrigger entity [processtrigger_systemform](processtrigger.md#BKMK_processtrigger_systemform) Many-To-One relationship.

**ReferencingEntity**: processtrigger<br />
**ReferencingAttribute**: formid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: processtrigger_systemform<br />
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


### <a name="BKMK_SystemForm_BulkDeleteFailures"></a> SystemForm_BulkDeleteFailures

Same as bulkdeletefailure entity [SystemForm_BulkDeleteFailures](bulkdeletefailure.md#BKMK_SystemForm_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: SystemForm_BulkDeleteFailures<br />
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

- [form_ancestor_form](#BKMK_form_ancestor_form)
- [organization_systemforms](#BKMK_organization_systemforms)


### <a name="BKMK_form_ancestor_form"></a> form_ancestor_form

See systemform Entity [form_ancestor_form](systemform.md#BKMK_form_ancestor_form) One-To-Many relationship.

### <a name="BKMK_organization_systemforms"></a> organization_systemforms

See organization Entity [organization_systemforms](organization.md#BKMK_organization_systemforms) One-To-Many relationship.
systemform

