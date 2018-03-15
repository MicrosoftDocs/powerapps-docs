---
title: "SdkMessageRequest Entity Reference (Common Data Service for Apps)| MicrosoftDocs"
description: "Includes schema information and supported messages for the SdkMessageRequest entity."

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
# SdkMessageRequest Entity Reference

For internal use only.

## Entity Properties

**DisplayName**: Sdk Message Request<br />
**DisplayCollectionName**: Sdk Message Requests<br />
**SchemaName**: SdkMessageRequest<br />
**CollectionSchemaName**: SdkMessageRequests<br />
**LogicalName**: sdkmessagerequest<br />
**LogicalCollectionName**: sdkmessagerequests<br />
**EntitySetName**: sdkmessagerequests<br />
**PrimaryIdAttribute**: sdkmessagerequestid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [IntroducedVersion](#BKMK_IntroducedVersion)
- [Name](#BKMK_Name)
- [SdkMessageRequestId](#BKMK_SdkMessageRequestId)


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


### <a name="BKMK_Name"></a> Name

**Description**: Name of the SDK message request.<br />
**DisplayName**: <br />
**LogicalName**: name<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_SdkMessageRequestId"></a> SdkMessageRequestId

**Description**: Unique identifier of the SDK message request entity.<br />
**DisplayName**: <br />
**LogicalName**: sdkmessagerequestid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [CustomizationLevel](#BKMK_CustomizationLevel)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [PrimaryObjectTypeCode](#BKMK_PrimaryObjectTypeCode)
- [SdkMessagePairId](#BKMK_SdkMessagePairId)
- [SdkMessageRequestIdUnique](#BKMK_SdkMessageRequestIdUnique)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


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

**Description**: Unique identifier of the user who created the SDK message request.<br />
**DisplayName**: <br />
**LogicalName**: createdby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the SDK message request was created.<br />
**DisplayName**: <br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the sdkmessagerequest.<br />
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

**Description**: Customization level of the SDK message request.<br />
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


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the SDK message request.<br />
**DisplayName**: <br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the SDK message request was last modified.<br />
**DisplayName**: <br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the sdkmessagerequest.<br />
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

**Description**: Unique identifier of the organization with which the SDK message request is associated.<br />
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

**Description**: Type of entity with which the SDK request is associated.<br />
**DisplayName**: <br />
**LogicalName**: primaryobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_SdkMessagePairId"></a> SdkMessagePairId

**Description**: Unique identifier of the message pair with which the SDK message request is associated.<br />
**DisplayName**: <br />
**LogicalName**: sdkmessagepairid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: sdkmessagepair


### <a name="BKMK_SdkMessageRequestIdUnique"></a> SdkMessageRequestIdUnique

**Description**: Unique identifier of the SDK message request.<br />
**DisplayName**: <br />
**LogicalName**: sdkmessagerequestidunique<br />
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

- [messagerequest_sdkmessageresponse](#BKMK_messagerequest_sdkmessageresponse)
- [messagerequest_sdkmessagerequestfield](#BKMK_messagerequest_sdkmessagerequestfield)
- [userentityinstancedata_sdkmessagerequest](#BKMK_userentityinstancedata_sdkmessagerequest)


### <a name="BKMK_messagerequest_sdkmessageresponse"></a> messagerequest_sdkmessageresponse

Same as sdkmessageresponse entity [messagerequest_sdkmessageresponse](sdkmessageresponse.md#BKMK_messagerequest_sdkmessageresponse) Many-To-One relationship.

**ReferencingEntity**: sdkmessageresponse<br />
**ReferencingAttribute**: sdkmessagerequestid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: messagerequest_sdkmessageresponse<br />
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


### <a name="BKMK_messagerequest_sdkmessagerequestfield"></a> messagerequest_sdkmessagerequestfield

Same as sdkmessagerequestfield entity [messagerequest_sdkmessagerequestfield](sdkmessagerequestfield.md#BKMK_messagerequest_sdkmessagerequestfield) Many-To-One relationship.

**ReferencingEntity**: sdkmessagerequestfield<br />
**ReferencingAttribute**: sdkmessagerequestid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: messagerequest_sdkmessagerequestfield<br />
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


### <a name="BKMK_userentityinstancedata_sdkmessagerequest"></a> userentityinstancedata_sdkmessagerequest

Same as userentityinstancedata entity [userentityinstancedata_sdkmessagerequest](userentityinstancedata.md#BKMK_userentityinstancedata_sdkmessagerequest) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_sdkmessagerequest<br />
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

- [lk_sdkmessagerequest_modifiedonbehalfby](#BKMK_lk_sdkmessagerequest_modifiedonbehalfby)
- [modifiedby_sdkmessagerequest](#BKMK_modifiedby_sdkmessagerequest)
- [lk_sdkmessagerequest_createdonbehalfby](#BKMK_lk_sdkmessagerequest_createdonbehalfby)
- [createdby_sdkmessagerequest](#BKMK_createdby_sdkmessagerequest)
- [organization_sdkmessagerequest](#BKMK_organization_sdkmessagerequest)
- [messagepair_sdkmessagerequest](#BKMK_messagepair_sdkmessagerequest)


### <a name="BKMK_lk_sdkmessagerequest_modifiedonbehalfby"></a> lk_sdkmessagerequest_modifiedonbehalfby

See systemuser Entity [lk_sdkmessagerequest_modifiedonbehalfby](systemuser.md#BKMK_lk_sdkmessagerequest_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_modifiedby_sdkmessagerequest"></a> modifiedby_sdkmessagerequest

See systemuser Entity [modifiedby_sdkmessagerequest](systemuser.md#BKMK_modifiedby_sdkmessagerequest) One-To-Many relationship.

### <a name="BKMK_lk_sdkmessagerequest_createdonbehalfby"></a> lk_sdkmessagerequest_createdonbehalfby

See systemuser Entity [lk_sdkmessagerequest_createdonbehalfby](systemuser.md#BKMK_lk_sdkmessagerequest_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_createdby_sdkmessagerequest"></a> createdby_sdkmessagerequest

See systemuser Entity [createdby_sdkmessagerequest](systemuser.md#BKMK_createdby_sdkmessagerequest) One-To-Many relationship.

### <a name="BKMK_organization_sdkmessagerequest"></a> organization_sdkmessagerequest

See organization Entity [organization_sdkmessagerequest](organization.md#BKMK_organization_sdkmessagerequest) One-To-Many relationship.

### <a name="BKMK_messagepair_sdkmessagerequest"></a> messagepair_sdkmessagerequest

See sdkmessagepair Entity [messagepair_sdkmessagerequest](sdkmessagepair.md#BKMK_messagepair_sdkmessagerequest) One-To-Many relationship.
sdkmessagerequest

