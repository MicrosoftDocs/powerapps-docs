---
title: "CustomerRelationship Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the CustomerRelationship entity."
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
# CustomerRelationship Entity Reference

Relationship between a customer and a partner in which either can be an account or contact.

## Entity Properties

**DisplayName**: Customer Relationship<br />
**DisplayCollectionName**: Customer Relationships<br />
**SchemaName**: CustomerRelationship<br />
**CollectionSchemaName**: CustomerRelationships<br />
**LogicalName**: customerrelationship<br />
**LogicalCollectionName**: customerrelationships<br />
**EntitySetName**: customerrelationships<br />
**PrimaryIdAttribute**: customerrelationshipid<br />
**PrimaryNameAttribute**: customerroleidname<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ConverseRelationshipId](#BKMK_ConverseRelationshipId)
- [CustomerId](#BKMK_CustomerId)
- [CustomerIdType](#BKMK_CustomerIdType)
- [CustomerRelationshipId](#BKMK_CustomerRelationshipId)
- [CustomerRoleDescription](#BKMK_CustomerRoleDescription)
- [CustomerRoleId](#BKMK_CustomerRoleId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [PartnerId](#BKMK_PartnerId)
- [PartnerIdType](#BKMK_PartnerIdType)
- [PartnerRoleDescription](#BKMK_PartnerRoleDescription)
- [PartnerRoleId](#BKMK_PartnerRoleId)


### <a name="BKMK_ConverseRelationshipId"></a> ConverseRelationshipId

**Description**: Unique identifier of the converse relationship of the customer relationship.<br />
**DisplayName**: Converse Relationship<br />
**LogicalName**: converserelationshipid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: customerrelationship


### <a name="BKMK_CustomerId"></a> CustomerId

**Description**: Select the primary account or contact involved in the customer relationship.<br />
**DisplayName**: Party 1<br />
**LogicalName**: customerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Customer<br />
**Targets**: account,contact


### <a name="BKMK_CustomerIdType"></a> CustomerIdType

**Description**: Type of the primary customer in the relationship, such as account or contact.<br />
**DisplayName**: Party 1 Type<br />
**LogicalName**: customeridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_CustomerRelationshipId"></a> CustomerRelationshipId

**Description**: Unique identifier of the customer relationship.<br />
**DisplayName**: Customer Relationship<br />
**LogicalName**: customerrelationshipid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_CustomerRoleDescription"></a> CustomerRoleDescription

**Description**: Type additional information about the primary party's role in the customer relationship, such as the length or quality of the relationship.<br />
**DisplayName**: Description 1<br />
**LogicalName**: customerroledescription<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_CustomerRoleId"></a> CustomerRoleId

**Description**: Choose the primary party's role or nature of the relationship the customer has with the second party. The field is read-only until both parties have been selected. Administrators can configure role values under Business Management in the Settings area.<br />
**DisplayName**: Role 1<br />
**LogicalName**: customerroleid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: relationshiprole


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


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: Type of the owner of the customer relationship, such as user, team, or business unit.<br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_PartnerId"></a> PartnerId

**Description**: Select the secondary account or contact involved in the customer relationship.<br />
**DisplayName**: Party 2<br />
**LogicalName**: partnerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Customer<br />
**Targets**: account,contact


### <a name="BKMK_PartnerIdType"></a> PartnerIdType

**Description**: Type of the secondary customer in the relationship, such as account or contact.<br />
**DisplayName**: Party 2 Type<br />
**LogicalName**: partneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_PartnerRoleDescription"></a> PartnerRoleDescription

**Description**: Type additional information about the secondary party's role in the customer relationship, such as the length or quality of the relationship.<br />
**DisplayName**: Description 2<br />
**LogicalName**: partnerroledescription<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_PartnerRoleId"></a> PartnerRoleId

**Description**: Choose the secondary party's role or nature of the relationship the customer has with the primary party. The field is read-only until both parties have been selected. Administrators can configure role values under Business Management in the Settings area.<br />
**DisplayName**: Role 2<br />
**LogicalName**: partnerroleid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: relationshiprole

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [CustomerIdName](#BKMK_CustomerIdName)
- [CustomerIdYomiName](#BKMK_CustomerIdYomiName)
- [CustomerRoleIdName](#BKMK_CustomerRoleIdName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [PartnerIdName](#BKMK_PartnerIdName)
- [PartnerIdYomiName](#BKMK_PartnerIdYomiName)
- [PartnerRoleIdName](#BKMK_PartnerRoleIdName)
- [UniqueDscId](#BKMK_UniqueDscId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Shows who created the record.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Description**: Name of the user who created the customer relationship.<br />
**DisplayName**: <br />
**LogicalName**: createdbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

**Description**: YomiName of the user who created the customer relationship.<br />
**DisplayName**: <br />
**LogicalName**: createdbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Shows the date and time when the customer relationship was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Shows who created the record on behalf of another user.<br />
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


### <a name="BKMK_CustomerIdName"></a> CustomerIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: customeridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_CustomerIdYomiName"></a> CustomerIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: customeridyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 450


### <a name="BKMK_CustomerRoleIdName"></a> CustomerRoleIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: customerroleidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Shows who last updated the record.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Description**: Name of the user who last modified the customer relationship.<br />
**DisplayName**: <br />
**LogicalName**: modifiedbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

**Description**: YomiName of the user who last modified the customer relationship.<br />
**DisplayName**: <br />
**LogicalName**: modifiedbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Shows who created the record on behalf of another user.<br />
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


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Description**: Name of the owner of the customer relationship.<br />
**DisplayName**: <br />
**LogicalName**: owneridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Description**: Unique identifier of the business unit that owns the customer relationship.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier of the team who owns the customer relationship.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns the customer relationship.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_PartnerIdName"></a> PartnerIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: partneridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_PartnerIdYomiName"></a> PartnerIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: partneridyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 450


### <a name="BKMK_PartnerRoleIdName"></a> PartnerRoleIdName

**Description**: Name of the relationship role of the secondary customer.<br />
**DisplayName**: <br />
**LogicalName**: partnerroleidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_UniqueDscId"></a> UniqueDscId

**Description**: For internal use only.<br />
**DisplayName**: UniqueDscId<br />
**LogicalName**: uniquedscid<br />
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

- [CustomerRelationship_AsyncOperations](#BKMK_CustomerRelationship_AsyncOperations)
- [CustomerRelationship_BulkDeleteFailures](#BKMK_CustomerRelationship_BulkDeleteFailures)
- [userentityinstancedata_customerrelationship](#BKMK_userentityinstancedata_customerrelationship)
- [CustomerRelationship_ProcessSessions](#BKMK_CustomerRelationship_ProcessSessions)
- [customer_relationship_converse_relationship](#BKMK_customer_relationship_converse_relationship)


### <a name="BKMK_CustomerRelationship_AsyncOperations"></a> CustomerRelationship_AsyncOperations

Same as asyncoperation entity [CustomerRelationship_AsyncOperations](asyncoperation.md#BKMK_CustomerRelationship_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: CustomerRelationship_AsyncOperations<br />
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


### <a name="BKMK_CustomerRelationship_BulkDeleteFailures"></a> CustomerRelationship_BulkDeleteFailures

Same as bulkdeletefailure entity [CustomerRelationship_BulkDeleteFailures](bulkdeletefailure.md#BKMK_CustomerRelationship_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: CustomerRelationship_BulkDeleteFailures<br />
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


### <a name="BKMK_userentityinstancedata_customerrelationship"></a> userentityinstancedata_customerrelationship

Same as userentityinstancedata entity [userentityinstancedata_customerrelationship](userentityinstancedata.md#BKMK_userentityinstancedata_customerrelationship) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_customerrelationship<br />
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


### <a name="BKMK_CustomerRelationship_ProcessSessions"></a> CustomerRelationship_ProcessSessions

Same as processsession entity [CustomerRelationship_ProcessSessions](processsession.md#BKMK_CustomerRelationship_ProcessSessions) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: CustomerRelationship_ProcessSessions<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 110

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_customer_relationship_converse_relationship"></a> customer_relationship_converse_relationship

Same as customerrelationship entity [customer_relationship_converse_relationship](customerrelationship.md#BKMK_customer_relationship_converse_relationship) Many-To-One relationship.

**ReferencingEntity**: customerrelationship<br />
**ReferencingAttribute**: converserelationshipid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: customer_relationship_converse_relationship<br />
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [team_customer_relationship](#BKMK_team_customer_relationship)
- [contact_customer_relationship_partner](#BKMK_contact_customer_relationship_partner)
- [business_unit_customer_relationship](#BKMK_business_unit_customer_relationship)
- [modifiedonbehalfby_customer_relationship](#BKMK_modifiedonbehalfby_customer_relationship)
- [createdby_customer_relationship](#BKMK_createdby_customer_relationship)
- [relationship_role_customer_role](#BKMK_relationship_role_customer_role)
- [account_customer_relationship_customer](#BKMK_account_customer_relationship_customer)
- [customer_relationship_converse_relationship](#BKMK_customer_relationship_converse_relationship)
- [account_customer_relationship_partner](#BKMK_account_customer_relationship_partner)
- [relationship_role_partner_role](#BKMK_relationship_role_partner_role)
- [createdonbehalfby_customer_relationship](#BKMK_createdonbehalfby_customer_relationship)
- [modifiedby_customer_relationship](#BKMK_modifiedby_customer_relationship)
- [user_customer_relationship](#BKMK_user_customer_relationship)
- [contact_customer_relationship_customer](#BKMK_contact_customer_relationship_customer)


### <a name="BKMK_team_customer_relationship"></a> team_customer_relationship

See team Entity [team_customer_relationship](team.md#BKMK_team_customer_relationship) One-To-Many relationship.

### <a name="BKMK_contact_customer_relationship_partner"></a> contact_customer_relationship_partner

See contact Entity [contact_customer_relationship_partner](contact.md#BKMK_contact_customer_relationship_partner) One-To-Many relationship.

### <a name="BKMK_business_unit_customer_relationship"></a> business_unit_customer_relationship

See businessunit Entity [business_unit_customer_relationship](businessunit.md#BKMK_business_unit_customer_relationship) One-To-Many relationship.

### <a name="BKMK_modifiedonbehalfby_customer_relationship"></a> modifiedonbehalfby_customer_relationship

See systemuser Entity [modifiedonbehalfby_customer_relationship](systemuser.md#BKMK_modifiedonbehalfby_customer_relationship) One-To-Many relationship.

### <a name="BKMK_createdby_customer_relationship"></a> createdby_customer_relationship

See systemuser Entity [createdby_customer_relationship](systemuser.md#BKMK_createdby_customer_relationship) One-To-Many relationship.

### <a name="BKMK_relationship_role_customer_role"></a> relationship_role_customer_role

See relationshiprole Entity [relationship_role_customer_role](relationshiprole.md#BKMK_relationship_role_customer_role) One-To-Many relationship.

### <a name="BKMK_account_customer_relationship_customer"></a> account_customer_relationship_customer

See account Entity [account_customer_relationship_customer](account.md#BKMK_account_customer_relationship_customer) One-To-Many relationship.

### <a name="BKMK_customer_relationship_converse_relationship"></a> customer_relationship_converse_relationship

See customerrelationship Entity [customer_relationship_converse_relationship](customerrelationship.md#BKMK_customer_relationship_converse_relationship) One-To-Many relationship.

### <a name="BKMK_account_customer_relationship_partner"></a> account_customer_relationship_partner

See account Entity [account_customer_relationship_partner](account.md#BKMK_account_customer_relationship_partner) One-To-Many relationship.

### <a name="BKMK_relationship_role_partner_role"></a> relationship_role_partner_role

See relationshiprole Entity [relationship_role_partner_role](relationshiprole.md#BKMK_relationship_role_partner_role) One-To-Many relationship.

### <a name="BKMK_createdonbehalfby_customer_relationship"></a> createdonbehalfby_customer_relationship

See systemuser Entity [createdonbehalfby_customer_relationship](systemuser.md#BKMK_createdonbehalfby_customer_relationship) One-To-Many relationship.

### <a name="BKMK_modifiedby_customer_relationship"></a> modifiedby_customer_relationship

See systemuser Entity [modifiedby_customer_relationship](systemuser.md#BKMK_modifiedby_customer_relationship) One-To-Many relationship.

### <a name="BKMK_user_customer_relationship"></a> user_customer_relationship

See systemuser Entity [user_customer_relationship](systemuser.md#BKMK_user_customer_relationship) One-To-Many relationship.

### <a name="BKMK_contact_customer_relationship_customer"></a> contact_customer_relationship_customer

See contact Entity [contact_customer_relationship_customer](contact.md#BKMK_contact_customer_relationship_customer) One-To-Many relationship.
customerrelationship

