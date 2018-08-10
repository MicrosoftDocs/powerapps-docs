---
title: "ServiceEndpoint Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the ServiceEndpoint entity."

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
# ServiceEndpoint Entity Reference

Service endpoint that can be contacted.

## Entity Properties

**DisplayName**: Service Endpoint<br />
**DisplayCollectionName**: Service Endpoints<br />
**SchemaName**: ServiceEndpoint<br />
**CollectionSchemaName**: ServiceEndpoints<br />
**LogicalName**: serviceendpoint<br />
**LogicalCollectionName**: serviceendpoints<br />
**EntitySetName**: serviceendpoints<br />
**PrimaryIdAttribute**: serviceendpointid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AuthType](#BKMK_AuthType)
- [AuthValue](#BKMK_AuthValue)
- [ConnectionMode](#BKMK_ConnectionMode)
- [Contract](#BKMK_Contract)
- [Description](#BKMK_Description)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCustomizable](#BKMK_IsCustomizable)
- [MessageFormat](#BKMK_MessageFormat)
- [Name](#BKMK_Name)
- [NamespaceAddress](#BKMK_NamespaceAddress)
- [NamespaceFormat](#BKMK_NamespaceFormat)
- [Path](#BKMK_Path)
- [SASKey](#BKMK_SASKey)
- [SASKeyName](#BKMK_SASKeyName)
- [SASToken](#BKMK_SASToken)
- [ServiceEndpointId](#BKMK_ServiceEndpointId)
- [SolutionNamespace](#BKMK_SolutionNamespace)
- [Url](#BKMK_Url)
- [UserClaim](#BKMK_UserClaim)


### <a name="BKMK_AuthType"></a> AuthType

**Description**: Specifies mode of authentication with SB<br />
**DisplayName**: Specifies mode of authentication with SB<br />
**LogicalName**: authtype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: ACS
- **Value**: 2 **Label**: SAS Key
- **Value**: 3 **Label**: SAS Token
- **Value**: 4 **Label**: Webhook Key
- **Value**: 5 **Label**: Http Header
- **Value**: 6 **Label**: Http Query String



### <a name="BKMK_AuthValue"></a> AuthValue

**Description**: Authentication Value<br />
**DisplayName**: Authentication Value<br />
**LogicalName**: authvalue<br />
**IsValidForForm**: True<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2048


### <a name="BKMK_ConnectionMode"></a> ConnectionMode

**Description**: Connection mode to contact the service endpoint.<br />
**DisplayName**: Connection Mode<br />
**LogicalName**: connectionmode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Normal
- **Value**: 2 **Label**: Federated



### <a name="BKMK_Contract"></a> Contract

**Description**: Type of the endpoint contract.<br />
**DisplayName**: Contract<br />
**LogicalName**: contract<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: OneWay
- **Value**: 2 **Label**: Queue
- **Value**: 3 **Label**: Rest
- **Value**: 4 **Label**: TwoWay
- **Value**: 5 **Label**: Topic
- **Value**: 6 **Label**: Queue (Persistent)
- **Value**: 7 **Label**: Event Hub
- **Value**: 8 **Label**: Webhook



### <a name="BKMK_Description"></a> Description

**Description**: Description of the service endpoint.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


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


### <a name="BKMK_MessageFormat"></a> MessageFormat

**Description**: Content type of the message<br />
**DisplayName**: Content type of the message<br />
**LogicalName**: messageformat<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Binary XML
- **Value**: 2 **Label**: Json
- **Value**: 3 **Label**: Text XML



### <a name="BKMK_Name"></a> Name

**Description**: Name of Service end point.<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_NamespaceAddress"></a> NamespaceAddress

**Description**: Full service endpoint address.<br />
**DisplayName**: Namespace Address<br />
**LogicalName**: namespaceaddress<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 255


### <a name="BKMK_NamespaceFormat"></a> NamespaceFormat

**Description**: Format of Service Bus Namespace<br />
**DisplayName**: Format of Service Bus Namespace<br />
**LogicalName**: namespaceformat<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Namespace Name
- **Value**: 2 **Label**: Namespace Address



### <a name="BKMK_Path"></a> Path

**Description**: Path to the service endpoint.<br />
**DisplayName**: Path<br />
**LogicalName**: path<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_SASKey"></a> SASKey

**Description**: Shared Access Key<br />
**DisplayName**: Shared Access Key<br />
**LogicalName**: saskey<br />
**IsValidForForm**: True<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_SASKeyName"></a> SASKeyName

**Description**: Shared Access Key Name<br />
**DisplayName**: Shared Access Key Name<br />
**LogicalName**: saskeyname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_SASToken"></a> SASToken

**Description**: Shared Access Token<br />
**DisplayName**: Shared Access Token<br />
**LogicalName**: sastoken<br />
**IsValidForForm**: True<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_ServiceEndpointId"></a> ServiceEndpointId

**Description**: Unique identifier of the service endpoint.<br />
**DisplayName**: <br />
**LogicalName**: serviceendpointid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SolutionNamespace"></a> SolutionNamespace

**Description**: Namespace of the App Fabric solution.<br />
**DisplayName**: Service Namespace<br />
**LogicalName**: solutionnamespace<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_Url"></a> Url

**Description**: Full service endpoint Url.<br />
**DisplayName**: Url Address<br />
**LogicalName**: url<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_UserClaim"></a> UserClaim

**Description**: Additional user claim value type.<br />
**DisplayName**: User Claim<br />
**LogicalName**: userclaim<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: None
- **Value**: 2 **Label**: UserId
- **Value**: 3 **Label**: UserInfo


<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IsAuthValueSet](#BKMK_IsAuthValueSet)
- [IsManaged](#BKMK_IsManaged)
- [IsSASKeySet](#BKMK_IsSASKeySet)
- [IsSASTokenSet](#BKMK_IsSASTokenSet)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [ServiceEndpointIdUnique](#BKMK_ServiceEndpointIdUnique)
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



### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the service endpoint.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the service endpoint was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the service endpoint.<br />
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


### <a name="BKMK_IsAuthValueSet"></a> IsAuthValueSet

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: isauthvalueset<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


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


### <a name="BKMK_IsSASKeySet"></a> IsSASKeySet

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: issaskeyset<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsSASTokenSet"></a> IsSASTokenSet

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: issastokenset<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the service endpoint.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the service endpoint was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who modified the service endpoint.<br />
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

**Description**: Unique identifier of the organization with which the service endpoint is associated.<br />
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


### <a name="BKMK_ServiceEndpointIdUnique"></a> ServiceEndpointIdUnique

**Description**: Unique identifier of the service endpoint.<br />
**DisplayName**: <br />
**LogicalName**: serviceendpointidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


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

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [userentityinstancedata_serviceendpoint](#BKMK_userentityinstancedata_serviceendpoint)
- [serviceendpoint_sdkmessageprocessingstep](#BKMK_serviceendpoint_sdkmessageprocessingstep)


### <a name="BKMK_userentityinstancedata_serviceendpoint"></a> userentityinstancedata_serviceendpoint

Same as userentityinstancedata entity [userentityinstancedata_serviceendpoint](userentityinstancedata.md#BKMK_userentityinstancedata_serviceendpoint) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_serviceendpoint<br />
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


### <a name="BKMK_serviceendpoint_sdkmessageprocessingstep"></a> serviceendpoint_sdkmessageprocessingstep

Same as sdkmessageprocessingstep entity [serviceendpoint_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_serviceendpoint_sdkmessageprocessingstep) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstep<br />
**ReferencingAttribute**: eventhandler<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: serviceendpoint_sdkmessageprocessingstep<br />
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

- [createdby_serviceendpoint](#BKMK_createdby_serviceendpoint)
- [lk_serviceendpointbase_modifiedonbehalfby](#BKMK_lk_serviceendpointbase_modifiedonbehalfby)
- [modifiedby_serviceendpoint](#BKMK_modifiedby_serviceendpoint)
- [organization_serviceendpoint](#BKMK_organization_serviceendpoint)
- [lk_serviceendpointbase_createdonbehalfby](#BKMK_lk_serviceendpointbase_createdonbehalfby)


### <a name="BKMK_createdby_serviceendpoint"></a> createdby_serviceendpoint

See systemuser Entity [createdby_serviceendpoint](systemuser.md#BKMK_createdby_serviceendpoint) One-To-Many relationship.

### <a name="BKMK_lk_serviceendpointbase_modifiedonbehalfby"></a> lk_serviceendpointbase_modifiedonbehalfby

See systemuser Entity [lk_serviceendpointbase_modifiedonbehalfby](systemuser.md#BKMK_lk_serviceendpointbase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_modifiedby_serviceendpoint"></a> modifiedby_serviceendpoint

See systemuser Entity [modifiedby_serviceendpoint](systemuser.md#BKMK_modifiedby_serviceendpoint) One-To-Many relationship.

### <a name="BKMK_organization_serviceendpoint"></a> organization_serviceendpoint

See organization Entity [organization_serviceendpoint](organization.md#BKMK_organization_serviceendpoint) One-To-Many relationship.

### <a name="BKMK_lk_serviceendpointbase_createdonbehalfby"></a> lk_serviceendpointbase_createdonbehalfby

See systemuser Entity [lk_serviceendpointbase_createdonbehalfby](systemuser.md#BKMK_lk_serviceendpointbase_createdonbehalfby) One-To-Many relationship.
serviceendpoint

