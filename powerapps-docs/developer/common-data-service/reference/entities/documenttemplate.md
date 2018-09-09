---
title: "DocumentTemplate Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the DocumentTemplate entity."
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
# DocumentTemplate Entity Reference

Used to store Document Templates in database in binary format.

## Entity Properties

**DisplayName**: Document Template<br />
**DisplayCollectionName**: Document Templates<br />
**SchemaName**: DocumentTemplate<br />
**CollectionSchemaName**: DocumentTemplates<br />
**LogicalName**: documenttemplate<br />
**LogicalCollectionName**: documenttemplates<br />
**EntitySetName**: documenttemplates<br />
**PrimaryIdAttribute**: documenttemplateid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AssociatedEntityTypeCode](#BKMK_AssociatedEntityTypeCode)
- [ClientData](#BKMK_ClientData)
- [Content](#BKMK_Content)
- [Description](#BKMK_Description)
- [DocumentTemplateId](#BKMK_DocumentTemplateId)
- [DocumentType](#BKMK_DocumentType)
- [LanguageCode](#BKMK_LanguageCode)
- [Name](#BKMK_Name)
- [Status](#BKMK_Status)


### <a name="BKMK_AssociatedEntityTypeCode"></a> AssociatedEntityTypeCode

**Description**: Associated Entity Type Code.<br />
**DisplayName**: Associated Entity Type Code<br />
**LogicalName**: associatedentitytypecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_ClientData"></a> ClientData

**Description**: Client data regarding this document template.<br />
**DisplayName**: Client Data<br />
**LogicalName**: clientdata<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_Content"></a> Content

**Description**: Bytes of the document template.<br />
**DisplayName**: Content<br />
**LogicalName**: content<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_Description"></a> Description

**Description**: Additional information to describe the Document Template<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_DocumentTemplateId"></a> DocumentTemplateId

**Description**: Unique identifier of the document template.<br />
**DisplayName**: Document Template Identifier<br />
**LogicalName**: documenttemplateid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_DocumentType"></a> DocumentType

**Description**: Option set for selecting the type of the document template<br />
**DisplayName**: Type<br />
**LogicalName**: documenttype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Microsoft Excel
- **Value**: 2 **Label**: Microsoft Word



### <a name="BKMK_LanguageCode"></a> LanguageCode

**Description**: Language of Document Template.<br />
**DisplayName**: Language<br />
**LogicalName**: languagecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: Language<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_Name"></a> Name

**Description**: Name of the document template.<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_Status"></a> Status

**Description**: Information about whether the document template is active.<br />
**DisplayName**: Status<br />
**LogicalName**: status<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Draft
- **FalseOption Value**: 0 **Label**: Activated

**DefaultValue**: False

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
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the document template.<br />
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

**Description**: Date and time when the document template was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the document template.<br />
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


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the document template.<br />
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

**Description**: Date and time when the document template was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who modified the document template.<br />
**DisplayName**: Created By (Delegate)<br />
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [lk_documenttemplatebase_modifiedonbehalfby](#BKMK_lk_documenttemplatebase_modifiedonbehalfby)
- [lk_documenttemplatebase_createdby](#BKMK_lk_documenttemplatebase_createdby)
- [lk_documenttemplatebase_modifiedby](#BKMK_lk_documenttemplatebase_modifiedby)
- [lk_documenttemplatebase_createdonbehalfby](#BKMK_lk_documenttemplatebase_createdonbehalfby)
- [lk_documenttemplatebase_organization](#BKMK_lk_documenttemplatebase_organization)


### <a name="BKMK_lk_documenttemplatebase_modifiedonbehalfby"></a> lk_documenttemplatebase_modifiedonbehalfby

See systemuser Entity [lk_documenttemplatebase_modifiedonbehalfby](systemuser.md#BKMK_lk_documenttemplatebase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_documenttemplatebase_createdby"></a> lk_documenttemplatebase_createdby

See systemuser Entity [lk_documenttemplatebase_createdby](systemuser.md#BKMK_lk_documenttemplatebase_createdby) One-To-Many relationship.

### <a name="BKMK_lk_documenttemplatebase_modifiedby"></a> lk_documenttemplatebase_modifiedby

See systemuser Entity [lk_documenttemplatebase_modifiedby](systemuser.md#BKMK_lk_documenttemplatebase_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_documenttemplatebase_createdonbehalfby"></a> lk_documenttemplatebase_createdonbehalfby

See systemuser Entity [lk_documenttemplatebase_createdonbehalfby](systemuser.md#BKMK_lk_documenttemplatebase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_documenttemplatebase_organization"></a> lk_documenttemplatebase_organization

See organization Entity [lk_documenttemplatebase_organization](organization.md#BKMK_lk_documenttemplatebase_organization) One-To-Many relationship.
documenttemplate

