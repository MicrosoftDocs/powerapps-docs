---
title: "WebResource Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the WebResource entity."
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
# WebResource Entity Reference

Data equivalent to files used in Web development. Web resources provide client-side components that are used to provide custom user interface elements.

## Entity Properties

**DisplayName**: Web Resource<br />
**DisplayCollectionName**: Web Resources<br />
**SchemaName**: WebResource<br />
**CollectionSchemaName**: WebResources<br />
**LogicalName**: webresource<br />
**LogicalCollectionName**: webresources<br />
**EntitySetName**: webresourceset<br />
**PrimaryIdAttribute**: webresourceid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CanBeDeleted](#BKMK_CanBeDeleted)
- [Content](#BKMK_Content)
- [ContentJson](#BKMK_ContentJson)
- [DependencyXml](#BKMK_DependencyXml)
- [Description](#BKMK_Description)
- [DisplayName](#BKMK_DisplayName)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsAvailableForMobileOffline](#BKMK_IsAvailableForMobileOffline)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsEnabledForMobileClient](#BKMK_IsEnabledForMobileClient)
- [IsHidden](#BKMK_IsHidden)
- [LanguageCode](#BKMK_LanguageCode)
- [Name](#BKMK_Name)
- [SilverlightVersion](#BKMK_SilverlightVersion)
- [WebResourceId](#BKMK_WebResourceId)
- [WebResourceType](#BKMK_WebResourceType)


### <a name="BKMK_CanBeDeleted"></a> CanBeDeleted

**Description**: Information that specifies whether this component can be deleted.<br />
**DisplayName**: Can Be Deleted<br />
**LogicalName**: canbedeleted<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: ManagedProperty<br />


### <a name="BKMK_Content"></a> Content

**Description**: Bytes of the web resource, in Base64 format.<br />
**DisplayName**: <br />
**LogicalName**: content<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_ContentJson"></a> ContentJson

**Description**: Json representation of the content of the resource.<br />
**DisplayName**: <br />
**LogicalName**: contentjson<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_DependencyXml"></a> DependencyXml

**Description**: For internal use only.<br />
**DisplayName**: DependencyXML<br />
**LogicalName**: dependencyxml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 5000


### <a name="BKMK_Description"></a> Description

**Description**: Description of the web resource.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: True<br />
**MaxLength**: 2000


### <a name="BKMK_DisplayName"></a> DisplayName

**Description**: Display name of the web resource.<br />
**DisplayName**: Display Name<br />
**LogicalName**: displayname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: True<br />
**MaxLength**: 200


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


### <a name="BKMK_IsAvailableForMobileOffline"></a> IsAvailableForMobileOffline

**Description**: Information that specifies whether this web resource is available for mobile client in offline mode.<br />
**DisplayName**: Is Available For Mobile Offline<br />
**LogicalName**: isavailableformobileoffline<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
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


### <a name="BKMK_IsEnabledForMobileClient"></a> IsEnabledForMobileClient

**Description**: Information that specifies whether this web resource is enabled for mobile client.<br />
**DisplayName**: Is Enabled For Mobile Client<br />
**LogicalName**: isenabledformobileclient<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsHidden"></a> IsHidden

**Description**: Information that specifies whether this component should be hidden.<br />
**DisplayName**: Hidden<br />
**LogicalName**: ishidden<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: ManagedProperty<br />


### <a name="BKMK_LanguageCode"></a> LanguageCode

**Description**: Language of the web resource.<br />
**DisplayName**: Language<br />
**LogicalName**: languagecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: Language<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_Name"></a> Name

**Description**: Name of the web resource.<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_SilverlightVersion"></a> SilverlightVersion

**Description**: Silverlight runtime version number required by a silverlight web resource.<br />
**DisplayName**: Silverlight Version<br />
**LogicalName**: silverlightversion<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: True<br />
**MaxLength**: 20


### <a name="BKMK_WebResourceId"></a> WebResourceId

**Description**: Unique identifier of the web resource.<br />
**DisplayName**: Web Resource Identifier<br />
**LogicalName**: webresourceid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_WebResourceType"></a> WebResourceType

**Description**: Drop-down list for selecting the type of the web resource.<br />
**DisplayName**: Type<br />
**LogicalName**: webresourcetype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Webpage (HTML)
- **Value**: 2 **Label**: Style Sheet (CSS)
- **Value**: 3 **Label**: Script (JScript)
- **Value**: 4 **Label**: Data (XML)
- **Value**: 5 **Label**: PNG format
- **Value**: 6 **Label**: JPG format
- **Value**: 7 **Label**: GIF format
- **Value**: 8 **Label**: Silverlight (XAP)
- **Value**: 9 **Label**: Style Sheet (XSL)
- **Value**: 10 **Label**: ICO format
- **Value**: 11 **Label**: Vector format (SVG)
- **Value**: 12 **Label**: String (RESX)


<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)
- [WebResourceIdUnique](#BKMK_WebResourceIdUnique)


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

**Description**: Unique identifier of the user who created the web resource.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the web resource was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the web resource.<br />
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


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the web resource.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the web resource was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who modified the web resource.<br />
**DisplayName**: Created By (Delegate)<br />
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

**Description**: Unique identifier of the organization associated with the web resource.<br />
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


### <a name="BKMK_WebResourceIdUnique"></a> WebResourceIdUnique

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: webresourceidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [webresource_savedqueryvisualizations](#BKMK_webresource_savedqueryvisualizations)
- [userentityinstancedata_webresource](#BKMK_userentityinstancedata_webresource)
- [solution_configuration_webresource](#BKMK_solution_configuration_webresource)
- [webresource_userqueryvisualizations](#BKMK_webresource_userqueryvisualizations)
- [lk_theme_logoid](#BKMK_lk_theme_logoid)


### <a name="BKMK_webresource_savedqueryvisualizations"></a> webresource_savedqueryvisualizations

Same as savedqueryvisualization entity [webresource_savedqueryvisualizations](savedqueryvisualization.md#BKMK_webresource_savedqueryvisualizations) Many-To-One relationship.

**ReferencingEntity**: savedqueryvisualization<br />
**ReferencingAttribute**: webresourceid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: webresource_savedqueryvisualizations<br />
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


### <a name="BKMK_userentityinstancedata_webresource"></a> userentityinstancedata_webresource

Same as userentityinstancedata entity [userentityinstancedata_webresource](userentityinstancedata.md#BKMK_userentityinstancedata_webresource) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_webresource<br />
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


### <a name="BKMK_solution_configuration_webresource"></a> solution_configuration_webresource

Same as solution entity [solution_configuration_webresource](solution.md#BKMK_solution_configuration_webresource) Many-To-One relationship.

**ReferencingEntity**: solution<br />
**ReferencingAttribute**: configurationpageid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: solution_configuration_webresource<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_webresource_userqueryvisualizations"></a> webresource_userqueryvisualizations

Same as userqueryvisualization entity [webresource_userqueryvisualizations](userqueryvisualization.md#BKMK_webresource_userqueryvisualizations) Many-To-One relationship.

**ReferencingEntity**: userqueryvisualization<br />
**ReferencingAttribute**: webresourceid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: webresource_userqueryvisualizations<br />
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


### <a name="BKMK_lk_theme_logoid"></a> lk_theme_logoid

Same as theme entity [lk_theme_logoid](theme.md#BKMK_lk_theme_logoid) Many-To-One relationship.

**ReferencingEntity**: theme<br />
**ReferencingAttribute**: logoid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_theme_logoid<br />
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

- [lk_webresourcebase_modifiedonbehalfby](#BKMK_lk_webresourcebase_modifiedonbehalfby)
- [webresource_createdby](#BKMK_webresource_createdby)
- [lk_webresourcebase_createdonbehalfby](#BKMK_lk_webresourcebase_createdonbehalfby)
- [webresource_modifiedby](#BKMK_webresource_modifiedby)
- [webresource_organization](#BKMK_webresource_organization)


### <a name="BKMK_lk_webresourcebase_modifiedonbehalfby"></a> lk_webresourcebase_modifiedonbehalfby

See systemuser Entity [lk_webresourcebase_modifiedonbehalfby](systemuser.md#BKMK_lk_webresourcebase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_webresource_createdby"></a> webresource_createdby

See systemuser Entity [webresource_createdby](systemuser.md#BKMK_webresource_createdby) One-To-Many relationship.

### <a name="BKMK_lk_webresourcebase_createdonbehalfby"></a> lk_webresourcebase_createdonbehalfby

See systemuser Entity [lk_webresourcebase_createdonbehalfby](systemuser.md#BKMK_lk_webresourcebase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_webresource_modifiedby"></a> webresource_modifiedby

See systemuser Entity [webresource_modifiedby](systemuser.md#BKMK_webresource_modifiedby) One-To-Many relationship.

### <a name="BKMK_webresource_organization"></a> webresource_organization

See organization Entity [webresource_organization](organization.md#BKMK_webresource_organization) One-To-Many relationship.
webresource

