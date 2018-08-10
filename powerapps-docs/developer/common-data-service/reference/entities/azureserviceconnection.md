---
title: "AzureServiceConnection Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the AzureServiceConnection entity."

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
# AzureServiceConnection Entity Reference

Stores connection information for an Azure service

## Entity Properties

**DisplayName**: Azure Service Connection<br />
**DisplayCollectionName**: Azure Service Connections<br />
**SchemaName**: AzureServiceConnection<br />
**CollectionSchemaName**: AzureServiceConnections<br />
**LogicalName**: azureserviceconnection<br />
**LogicalCollectionName**: azureserviceconnections<br />
**EntitySetName**: azureserviceconnections<br />
**PrimaryIdAttribute**: azureserviceconnectionid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AccountKey](#BKMK_AccountKey)
- [AzureServiceConnectionId](#BKMK_AzureServiceConnectionId)
- [ConnectionType](#BKMK_ConnectionType)
- [Description](#BKMK_Description)
- [LastConnectionStatusCode](#BKMK_LastConnectionStatusCode)
- [LastConnectionTime](#BKMK_LastConnectionTime)
- [Name](#BKMK_Name)
- [ServiceUri](#BKMK_ServiceUri)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)


### <a name="BKMK_AccountKey"></a> AccountKey

**Description**: Type the Azure account key.<br />
**DisplayName**: Azure Account Key<br />
**LogicalName**: accountkey<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_AzureServiceConnectionId"></a> AzureServiceConnectionId

**Description**: Unique identifier of the Azure service connection.<br />
**DisplayName**: Azure Service Connection<br />
**LogicalName**: azureserviceconnectionid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ConnectionType"></a> ConnectionType

**Description**: Azure service connection type<br />
**DisplayName**: Connection Type<br />
**LogicalName**: connectiontype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Recommendation
- **Value**: 2 **Label**: Text Analytics



### <a name="BKMK_Description"></a> Description

**Description**: Enter a description of the Azure service connection.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_LastConnectionStatusCode"></a> LastConnectionStatusCode

**Description**: Shows the status of the last connection to the Azure service.<br />
**DisplayName**: Last Connection Status<br />
**LogicalName**: lastconnectionstatuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Success
- **Value**: 2 **Label**: Failure



### <a name="BKMK_LastConnectionTime"></a> LastConnectionTime

**Description**: shows the time of the last connection to the Azure service.<br />
**DisplayName**: Last Connection Time<br />
**LogicalName**: lastconnectiontime<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_Name"></a> Name

**Description**: Type a logical name for the connection.<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_ServiceUri"></a> ServiceUri

**Description**: Type the service URL for the Azure service.<br />
**DisplayName**: Azure Service URL<br />
**LogicalName**: serviceuri<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Url<br />
**IsLocalizable**: False<br />
**MaxLength**: 500


### <a name="BKMK_StateCode"></a> StateCode

**Description**: Shows whether the Azure service connection is active or inactive.<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Active **DefaultStatus**: 1 **InvariantName**: Active
- **Value**: 1 **Label**: Inactive **DefaultStatus**: 2 **InvariantName**: Inactive



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Select the Azure service connection's status.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Status<br />
**Options**:

- **Value**: 1 **Label**: Active **State**: 0
- **Value**: 2 **Label**: Inactive **State**: 1


<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the Azure service connection.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: True<br />
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

**Description**: Date and time when the Azure service connection was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the Azure service connection.<br />
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


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who modified the Azure service connection.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: True<br />
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

**Description**: Date and time when the Azure service connection was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the Azure service connection.<br />
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

**Description**: Unique identifier of the organization associated with the Azure service connection.<br />
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

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [azureserviceconnection_knowledgesearchmodel](#BKMK_azureserviceconnection_knowledgesearchmodel)
- [azureserviceconnection_advancedsimilarityrule](#BKMK_azureserviceconnection_advancedsimilarityrule)


### <a name="BKMK_azureserviceconnection_knowledgesearchmodel"></a> azureserviceconnection_knowledgesearchmodel

Same as knowledgesearchmodel entity [azureserviceconnection_knowledgesearchmodel](knowledgesearchmodel.md#BKMK_azureserviceconnection_knowledgesearchmodel) Many-To-One relationship.

**ReferencingEntity**: knowledgesearchmodel<br />
**ReferencingAttribute**: azureserviceconnectionid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: azureserviceconnection_knowledgesearchmodel<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 10000

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_azureserviceconnection_advancedsimilarityrule"></a> azureserviceconnection_advancedsimilarityrule

Same as advancedsimilarityrule entity [azureserviceconnection_advancedsimilarityrule](advancedsimilarityrule.md#BKMK_azureserviceconnection_advancedsimilarityrule) Many-To-One relationship.

**ReferencingEntity**: advancedsimilarityrule<br />
**ReferencingAttribute**: azureserviceconnectionid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: azureserviceconnection_advancedsimilarityrule<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 10000

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

- [lk_azureserviceconnection_modifiedonbehalfby](#BKMK_lk_azureserviceconnection_modifiedonbehalfby)
- [lk_azureserviceconnection_modifiedby](#BKMK_lk_azureserviceconnection_modifiedby)
- [lk_azureserviceconnection_createdby](#BKMK_lk_azureserviceconnection_createdby)
- [lk_azureserviceconnection_createdonbehalfby](#BKMK_lk_azureserviceconnection_createdonbehalfby)
- [organization_azureserviceconnection](#BKMK_organization_azureserviceconnection)


### <a name="BKMK_lk_azureserviceconnection_modifiedonbehalfby"></a> lk_azureserviceconnection_modifiedonbehalfby

See systemuser Entity [lk_azureserviceconnection_modifiedonbehalfby](systemuser.md#BKMK_lk_azureserviceconnection_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_azureserviceconnection_modifiedby"></a> lk_azureserviceconnection_modifiedby

See systemuser Entity [lk_azureserviceconnection_modifiedby](systemuser.md#BKMK_lk_azureserviceconnection_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_azureserviceconnection_createdby"></a> lk_azureserviceconnection_createdby

See systemuser Entity [lk_azureserviceconnection_createdby](systemuser.md#BKMK_lk_azureserviceconnection_createdby) One-To-Many relationship.

### <a name="BKMK_lk_azureserviceconnection_createdonbehalfby"></a> lk_azureserviceconnection_createdonbehalfby

See systemuser Entity [lk_azureserviceconnection_createdonbehalfby](systemuser.md#BKMK_lk_azureserviceconnection_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_azureserviceconnection"></a> organization_azureserviceconnection

See organization Entity [organization_azureserviceconnection](organization.md#BKMK_organization_azureserviceconnection) One-To-Many relationship.
azureserviceconnection

