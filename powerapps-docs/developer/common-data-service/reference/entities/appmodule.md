---
title: "AppModule Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the AppModule entity."
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
# AppModule Entity Reference

A role-based, modular business app that provides task-based functionality for a particular area of work.

## Entity Properties

**DisplayName**: App<br />
**DisplayCollectionName**: Apps<br />
**SchemaName**: AppModule<br />
**CollectionSchemaName**: AppModules<br />
**LogicalName**: appmodule<br />
**LogicalCollectionName**: appmodules<br />
**EntitySetName**: appmodules<br />
**PrimaryIdAttribute**: appmoduleid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AppModuleId](#BKMK_AppModuleId)
- [AppModuleIdUnique](#BKMK_AppModuleIdUnique)
- [AppModuleVersion](#BKMK_AppModuleVersion)
- [AppModuleXmlManaged](#BKMK_AppModuleXmlManaged)
- [ClientType](#BKMK_ClientType)
- [ConfigXML](#BKMK_ConfigXML)
- [Description](#BKMK_Description)
- [FormFactor](#BKMK_FormFactor)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsDefault](#BKMK_IsDefault)
- [IsFeatured](#BKMK_IsFeatured)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PublishedOn](#BKMK_PublishedOn)
- [PublisherId](#BKMK_PublisherId)
- [UniqueName](#BKMK_UniqueName)
- [URL](#BKMK_URL)
- [WebResourceId](#BKMK_WebResourceId)
- [WelcomePageId](#BKMK_WelcomePageId)


### <a name="BKMK_AppModuleId"></a> AppModuleId

**Description**: Unique identifier for entity instances<br />
**DisplayName**: AppModuleId<br />
**LogicalName**: appmoduleid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_AppModuleIdUnique"></a> AppModuleIdUnique

**Description**: Unique identifier of the App Module used when synchronizing customizations for the Microsoft Dynamics 365 client for Outlook<br />
**DisplayName**: App Module Unique Id<br />
**LogicalName**: appmoduleidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_AppModuleVersion"></a> AppModuleVersion

**Description**: App Module Version<br />
**DisplayName**: App Module Version<br />
**LogicalName**: appmoduleversion<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: VersionNumber<br />
**IsLocalizable**: False<br />
**MaxLength**: 48


### <a name="BKMK_AppModuleXmlManaged"></a> AppModuleXmlManaged

**Description**: App Module Xml Managed<br />
**DisplayName**: <br />
**LogicalName**: appmodulexmlmanaged<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_ClientType"></a> ClientType

**Description**: Client Type such as Web or UCI<br />
**DisplayName**: Client Type<br />
**LogicalName**: clienttype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 31<br />
**MinValue**: 1


### <a name="BKMK_ConfigXML"></a> ConfigXML

**Description**: Contains configuration XML<br />
**DisplayName**: <br />
**LogicalName**: configxml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_Description"></a> Description

**Description**: Description for entity<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: True<br />
**MaxLength**: 2000


### <a name="BKMK_FormFactor"></a> FormFactor

**Description**: Form Factor<br />
**DisplayName**: Form Factor<br />
**LogicalName**: formfactor<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 8<br />
**MinValue**: 1


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

**Description**: Unique identifier of the data import or data migration that created this record.<br />
**DisplayName**: Import Sequence Number<br />
**LogicalName**: importsequencenumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

**Description**: Version in which the similarity rule is introduced.<br />
**DisplayName**: Introduced Version<br />
**LogicalName**: introducedversion<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: VersionNumber<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_IsDefault"></a> IsDefault

**Description**: Is Default<br />
**DisplayName**: Is Default<br />
**LogicalName**: isdefault<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsFeatured"></a> IsFeatured

**Description**: Is Featured<br />
**DisplayName**: IsFeatured<br />
**LogicalName**: isfeatured<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_Name"></a> Name

**Description**: Name of App Module<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: True<br />
**MaxLength**: 100


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

**Description**: Date and time that the record was migrated.<br />
**DisplayName**: Record Created On<br />
**LogicalName**: overriddencreatedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_PublishedOn"></a> PublishedOn

**Description**: Date and time when the record was published.<br />
**DisplayName**: Published On<br />
**LogicalName**: publishedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_PublisherId"></a> PublisherId

**Description**: Unique identifier of the publisher.<br />
**DisplayName**: Publisher<br />
**LogicalName**: publisherid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Lookup<br />
**Targets**: publisher


### <a name="BKMK_UniqueName"></a> UniqueName

**Description**: Unique Name of App Module<br />
**DisplayName**: Unique Name<br />
**LogicalName**: uniquename<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_URL"></a> URL

**Description**: Contains URL<br />
**DisplayName**: URL<br />
**LogicalName**: url<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_WebResourceId"></a> WebResourceId

**Description**: Unique identifier of the Web Resource<br />
**DisplayName**: Web Resource Id<br />
**LogicalName**: webresourceid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_WelcomePageId"></a> WelcomePageId

**Description**: Unique identifier of the Web Resource as Welcome Page Id<br />
**DisplayName**: Welcome Page Id<br />
**LogicalName**: welcomepageid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />

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
- [Descriptor](#BKMK_Descriptor)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [PublisherIdName](#BKMK_PublisherIdName)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ComponentState"></a> ComponentState

**Description**: For internal use only<br />
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

**Description**: Unique identifier of the user who created the record.<br />
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

**Description**: Date and time when the record was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the record.<br />
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
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_Descriptor"></a> Descriptor

**Description**: App Module Descriptor<br />
**DisplayName**: Descriptor<br />
**LogicalName**: descriptor<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_IsManaged"></a> IsManaged

**Description**: Is Managed<br />
**DisplayName**: IsManaged<br />
**LogicalName**: ismanaged<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Managed
- **FalseOption Value**: 0 **Label**: Unmanaged

**DefaultValue**: False


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who modified the record.<br />
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

**Description**: Date and time when the record was modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who modified the record.<br />
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
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization associated with the app.<br />
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


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

**Description**: Internal use only<br />
**DisplayName**: Overwrite Time<br />
**LogicalName**: overwritetime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


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

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [appmodule_appconfig](#BKMK_appmodule_appconfig)
- [appmodule_appmodulecomponent](#BKMK_appmodule_appmodulecomponent)


### <a name="BKMK_appmodule_appconfig"></a> appmodule_appconfig

Same as appconfig entity [appmodule_appconfig](appconfig.md#BKMK_appmodule_appconfig) Many-To-One relationship.

**ReferencingEntity**: appconfig<br />
**ReferencingAttribute**: appmoduleid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: appmodule_appconfig<br />
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


### <a name="BKMK_appmodule_appmodulecomponent"></a> appmodule_appmodulecomponent

Same as appmodulecomponent entity [appmodule_appmodulecomponent](appmodulecomponent.md#BKMK_appmodule_appmodulecomponent) Many-To-One relationship.

**ReferencingEntity**: appmodulecomponent<br />
**ReferencingAttribute**: appmoduleidunique<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: appmodule_appmodulecomponent<br />
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [organization_appmodule](#BKMK_organization_appmodule)
- [lk_appmodule_modifiedby](#BKMK_lk_appmodule_modifiedby)
- [publisher_appmodule](#BKMK_publisher_appmodule)
- [lk_appmodule_modifiedonbehalfby](#BKMK_lk_appmodule_modifiedonbehalfby)
- [lk_appmodule_createdby](#BKMK_lk_appmodule_createdby)
- [lk_appmodule_createdonbehalfby](#BKMK_lk_appmodule_createdonbehalfby)


### <a name="BKMK_organization_appmodule"></a> organization_appmodule

See organization Entity [organization_appmodule](organization.md#BKMK_organization_appmodule) One-To-Many relationship.

### <a name="BKMK_lk_appmodule_modifiedby"></a> lk_appmodule_modifiedby

See systemuser Entity [lk_appmodule_modifiedby](systemuser.md#BKMK_lk_appmodule_modifiedby) One-To-Many relationship.

### <a name="BKMK_publisher_appmodule"></a> publisher_appmodule

See publisher Entity [publisher_appmodule](publisher.md#BKMK_publisher_appmodule) One-To-Many relationship.

### <a name="BKMK_lk_appmodule_modifiedonbehalfby"></a> lk_appmodule_modifiedonbehalfby

See systemuser Entity [lk_appmodule_modifiedonbehalfby](systemuser.md#BKMK_lk_appmodule_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_appmodule_createdby"></a> lk_appmodule_createdby

See systemuser Entity [lk_appmodule_createdby](systemuser.md#BKMK_lk_appmodule_createdby) One-To-Many relationship.

### <a name="BKMK_lk_appmodule_createdonbehalfby"></a> lk_appmodule_createdonbehalfby

See systemuser Entity [lk_appmodule_createdonbehalfby](systemuser.md#BKMK_lk_appmodule_createdonbehalfby) One-To-Many relationship.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the AppModule entity is the first entity in the relationship. Listed by **SchemaName**.


### <a name="BKMK_appmoduleroles_association"></a> appmoduleroles_association

**IntersectEntityName**: appmoduleroles<br />
**Entity1LogicalName**: appmodule<br />

- **Entity1IntersectAttribute**: appmoduleid
- **Entity1NavigationPropertyName**: appmoduleroles_association
- **Entity1AssociatedMenuConfiguration**:

  - **Behavior**: DoNotDisplay
  - **Group**: Details
  - **Label**: 
  - **Order**: 

**Entity2LogicalName**: [role](role.md)<br />

- **Entity2IntersectAttribute**: roleid
- **Entity2NavigationPropertyName**: appmoduleroles_association
- **Entity2AssociatedMenuConfiguration**:

  - **Behavior**: DoNotDisplay
  - **Group**: Details
  - **Label**: 
  - **Order**: 

**IsCustomizable**: False<br />
appmodule

