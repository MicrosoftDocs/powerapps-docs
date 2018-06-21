---
title: "KnowledgeSearchModel Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the KnowledgeSearchModel entity."

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
# KnowledgeSearchModel Entity Reference

Configuration for automatic suggestion of knowledge articles using text analytics and search

## Entity Properties

**DisplayName**: Knowledge Search Model<br />
**DisplayCollectionName**: Knowledge Search Model<br />
**SchemaName**: KnowledgeSearchModel<br />
**CollectionSchemaName**: KnowledgeSearchModels<br />
**LogicalName**: knowledgesearchmodel<br />
**LogicalCollectionName**: knowledgesearchmodels<br />
**EntitySetName**: knowledgesearchmodels<br />
**PrimaryIdAttribute**: knowledgesearchmodelid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AzureServiceConnectionId](#BKMK_AzureServiceConnectionId)
- [Description](#BKMK_Description)
- [Entity](#BKMK_Entity)
- [FetchXmlList](#BKMK_FetchXmlList)
- [KnowledgeSearchModelId](#BKMK_KnowledgeSearchModelId)
- [MaxKeyWords](#BKMK_MaxKeyWords)
- [Name](#BKMK_Name)
- [NgramSize](#BKMK_NgramSize)
- [SourceEntity](#BKMK_SourceEntity)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)


### <a name="BKMK_AzureServiceConnectionId"></a> AzureServiceConnectionId

**Description**: Unique identifier for AzureServiceConnection associated with KnowledgeSearchModel.<br />
**DisplayName**: Connection<br />
**LogicalName**: azureserviceconnectionid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Lookup<br />
**Targets**: azureserviceconnection


### <a name="BKMK_Description"></a> Description

**Description**: Enter a description for the search configuration<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_Entity"></a> Entity

**Description**: entity<br />
**DisplayName**: Entity<br />
**LogicalName**: entity<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_FetchXmlList"></a> FetchXmlList

**Description**: FetchXml.<br />
**DisplayName**: FetchXml<br />
**LogicalName**: fetchxmllist<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 500000


### <a name="BKMK_KnowledgeSearchModelId"></a> KnowledgeSearchModelId

**Description**: Unique identifier for entity instances<br />
**DisplayName**: Knowledge Search Model<br />
**LogicalName**: knowledgesearchmodelid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_MaxKeyWords"></a> MaxKeyWords

**Description**: Enter the maximum number of keywords or key phrases to be determined using text analytics.<br />
**DisplayName**: Maximum Number of Key Phrases<br />
**LogicalName**: maxkeywords<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000<br />
**MinValue**: 0


### <a name="BKMK_Name"></a> Name

**Description**: Type a logical name for the search configuration.<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_NgramSize"></a> NgramSize

**Description**: Enter the maximum number of key phrase words to use in a topic.<br />
**DisplayName**: Maximum Key Phrase Words<br />
**LogicalName**: ngramsize<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 3<br />
**MinValue**: 1


### <a name="BKMK_SourceEntity"></a> SourceEntity

**Description**: Enter an entity that articles are suggested for.<br />
**DisplayName**: Source Entity<br />
**LogicalName**: sourceentity<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_StateCode"></a> StateCode

**Description**: Status of the Knowledge Search Model<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Active **DefaultStatus**: 1 **InvariantName**: Active
- **Value**: 1 **Label**: Inactive **DefaultStatus**: 2 **InvariantName**: Inactive



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Reason for the status of the Knowledge Search Model<br />
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

- [AzureServiceConnectionIdName](#BKMK_AzureServiceConnectionIdName)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IsManaged](#BKMK_IsManaged)
- [KnowledgeSearchModelIdUnique](#BKMK_KnowledgeSearchModelIdUnique)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)


### <a name="BKMK_AzureServiceConnectionIdName"></a> AzureServiceConnectionIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: azureserviceconnectionidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


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

**Description**: Unique identifier of the user who created the Knowledge Search Model.<br />
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

**Description**: Date and time when the Knowledge Search Model was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the knowledge search Model.<br />
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

**Description**: Is Manageed<br />
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


### <a name="BKMK_KnowledgeSearchModelIdUnique"></a> KnowledgeSearchModelIdUnique

**Description**: Unique identifier of the Knowledge Search Model used when synchronizing customizations for the Microsoft Dynamics 365 client for Outlook<br />
**DisplayName**: Knowledge Search Model Unique Id<br />
**LogicalName**: knowledgesearchmodelidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who modified the Knowledge Search Model.<br />
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

**Description**: Date and time when the Knowledge Search model was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the knowledge search model.<br />
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

**Description**: Unique identifier of the organization associated with the Knowledge Search Model entity.<br />
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

**Description**: Date and time when the record was created.<br />
**DisplayName**: Created On<br />
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

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_knowledgesearchmodel_textanalyticsentitymapping"></a> knowledgesearchmodel_textanalyticsentitymapping

Same as textanalyticsentitymapping entity [knowledgesearchmodel_textanalyticsentitymapping](textanalyticsentitymapping.md#BKMK_knowledgesearchmodel_textanalyticsentitymapping) Many-To-One relationship.

**ReferencingEntity**: textanalyticsentitymapping<br />
**ReferencingAttribute**: knowledgesearchmodelid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: knowledgesearchmodel_textanalyticsentitymapping<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 1000

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

- [organization_knowledgesearchmodel](#BKMK_organization_knowledgesearchmodel)
- [lk_knowledgesearchmodel_createdby](#BKMK_lk_knowledgesearchmodel_createdby)
- [azureserviceconnection_knowledgesearchmodel](#BKMK_azureserviceconnection_knowledgesearchmodel)
- [lk_knowledgesearchmodel_modifiedby](#BKMK_lk_knowledgesearchmodel_modifiedby)
- [lk_knowledgesearchmodel_modifiedonbehalfby](#BKMK_lk_knowledgesearchmodel_modifiedonbehalfby)
- [lk_knowledgesearchmodel_createdonbehalfby](#BKMK_lk_knowledgesearchmodel_createdonbehalfby)


### <a name="BKMK_organization_knowledgesearchmodel"></a> organization_knowledgesearchmodel

See organization Entity [organization_knowledgesearchmodel](organization.md#BKMK_organization_knowledgesearchmodel) One-To-Many relationship.

### <a name="BKMK_lk_knowledgesearchmodel_createdby"></a> lk_knowledgesearchmodel_createdby

See systemuser Entity [lk_knowledgesearchmodel_createdby](systemuser.md#BKMK_lk_knowledgesearchmodel_createdby) One-To-Many relationship.

### <a name="BKMK_azureserviceconnection_knowledgesearchmodel"></a> azureserviceconnection_knowledgesearchmodel

See azureserviceconnection Entity [azureserviceconnection_knowledgesearchmodel](azureserviceconnection.md#BKMK_azureserviceconnection_knowledgesearchmodel) One-To-Many relationship.

### <a name="BKMK_lk_knowledgesearchmodel_modifiedby"></a> lk_knowledgesearchmodel_modifiedby

See systemuser Entity [lk_knowledgesearchmodel_modifiedby](systemuser.md#BKMK_lk_knowledgesearchmodel_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_knowledgesearchmodel_modifiedonbehalfby"></a> lk_knowledgesearchmodel_modifiedonbehalfby

See systemuser Entity [lk_knowledgesearchmodel_modifiedonbehalfby](systemuser.md#BKMK_lk_knowledgesearchmodel_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_knowledgesearchmodel_createdonbehalfby"></a> lk_knowledgesearchmodel_createdonbehalfby

See systemuser Entity [lk_knowledgesearchmodel_createdonbehalfby](systemuser.md#BKMK_lk_knowledgesearchmodel_createdonbehalfby) One-To-Many relationship.
knowledgesearchmodel

