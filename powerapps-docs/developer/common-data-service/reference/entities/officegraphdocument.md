---
title: "OfficeGraphDocument Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the OfficeGraphDocument entity."
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
# OfficeGraphDocument Entity Reference

Office Graph Documents Description

## Entity Properties

**DisplayName**: Office Graph Document<br />
**DisplayCollectionName**: Office Graph Documents<br />
**SchemaName**: OfficeGraphDocument<br />
**CollectionSchemaName**: OfficeGraphDocuments<br />
**LogicalName**: officegraphdocument<br />
**LogicalCollectionName**: officegraphdocuments<br />
**EntitySetName**: officegraphdocuments<br />
**PrimaryIdAttribute**: officegraphdocumentid<br />
**PrimaryNameAttribute**: title<br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [DocumentId](#BKMK_DocumentId)
- [OfficeGraphDocumentId](#BKMK_OfficeGraphDocumentId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [Title](#BKMK_Title)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_DocumentId"></a> DocumentId

**Description**: Document Id.<br />
**DisplayName**: Document Id<br />
**LogicalName**: documentid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OfficeGraphDocumentId"></a> OfficeGraphDocumentId

**Description**: Unique identifier for entity instances<br />
**DisplayName**: OfficeGraphDocument<br />
**LogicalName**: officegraphdocumentid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

**Description**: For internal use only.<br />
**DisplayName**: Time Zone Rule Version Number<br />
**LogicalName**: timezoneruleversionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_Title"></a> Title

**Description**: The title of the entity.<br />
**DisplayName**: Title<br />
**LogicalName**: title<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

**Description**: Exchange rate for the currency associated with the Office Graph Document with respect to the base currency.<br />
**DisplayName**: Currency<br />
**LogicalName**: transactioncurrencyid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: transactioncurrency


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

**Description**: Time zone code that was in use when the record was created.<br />
**DisplayName**: UTC Conversion Time Zone Code<br />
**LogicalName**: utcconversiontimezonecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AuthorNames](#BKMK_AuthorNames)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [CreatedTime](#BKMK_CreatedTime)
- [DocumentLastModifiedBy](#BKMK_DocumentLastModifiedBy)
- [DocumentLastModifiedOn](#BKMK_DocumentLastModifiedOn)
- [DocumentPreviewMetadata](#BKMK_DocumentPreviewMetadata)
- [ExchangeRate](#BKMK_ExchangeRate)
- [FileExtension](#BKMK_FileExtension)
- [FileType](#BKMK_FileType)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [ModifiedTime](#BKMK_ModifiedTime)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [PreviewImageUrl](#BKMK_PreviewImageUrl)
- [QueryType](#BKMK_QueryType)
- [Rank](#BKMK_Rank)
- [ReadUrl](#BKMK_ReadUrl)
- [SecondaryFileExtension](#BKMK_SecondaryFileExtension)
- [SiteTitle](#BKMK_SiteTitle)
- [SiteUrl](#BKMK_SiteUrl)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)
- [ViewCount](#BKMK_ViewCount)
- [WebLocationUrl](#BKMK_WebLocationUrl)


### <a name="BKMK_AuthorNames"></a> AuthorNames

**Description**: Shows Author Names of Office Graph Document.<br />
**DisplayName**: Author Names<br />
**LogicalName**: authornames<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Shows Created By of Office Graph Document.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


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


### <a name="BKMK_CreatedTime"></a> CreatedTime

**Description**: Date and time when the record was created.<br />
**DisplayName**: Created Time<br />
**LogicalName**: createdtime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_DocumentLastModifiedBy"></a> DocumentLastModifiedBy

**Description**: Document Last Modified By<br />
**DisplayName**: Document Last Modified By<br />
**LogicalName**: documentlastmodifiedby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_DocumentLastModifiedOn"></a> DocumentLastModifiedOn

**Description**: Document Last Modified On<br />
**DisplayName**: Document Last Modified On<br />
**LogicalName**: documentlastmodifiedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_DocumentPreviewMetadata"></a> DocumentPreviewMetadata

**Description**: document preview metadata<br />
**DisplayName**: document preview metadata<br />
**LogicalName**: documentpreviewmetadata<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

**Description**: Exchange rate for the currency associated with the Office Graph Document with respect to the base currency.<br />
**DisplayName**: ExchangeRate<br />
**LogicalName**: exchangerate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0.0000000001<br />
**Precision**: 10


### <a name="BKMK_FileExtension"></a> FileExtension

**Description**: File Extension of Office Graph Document.<br />
**DisplayName**: File Extension<br />
**LogicalName**: fileextension<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_FileType"></a> FileType

**Description**: Shows the File Type of Office Graph Document.<br />
**DisplayName**: File Type<br />
**LogicalName**: filetype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Shows modified by of Office Graph Document.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


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


### <a name="BKMK_ModifiedTime"></a> ModifiedTime

**Description**: Date and time when the record was modified.<br />
**DisplayName**: Modified Time<br />
**LogicalName**: modifiedtime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier for the organization<br />
**DisplayName**: Organization Id<br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
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


### <a name="BKMK_PreviewImageUrl"></a> PreviewImageUrl

**Description**: Shows the Preview Image Url Office Graph Document.<br />
**DisplayName**: Preview Image Url<br />
**LogicalName**: previewimageurl<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_QueryType"></a> QueryType

**Description**: Shows Query Type of child folders<br />
**DisplayName**: Query Type<br />
**LogicalName**: querytype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_Rank"></a> Rank

**Description**: The relevancy rank of the document retrieved<br />
**DisplayName**: Relevancy Rank of the Document<br />
**LogicalName**: rank<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_ReadUrl"></a> ReadUrl

**Description**: The online read url<br />
**DisplayName**: Read Url<br />
**LogicalName**: readurl<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_SecondaryFileExtension"></a> SecondaryFileExtension

**Description**: Secondary File Extension of Office Graph Document.<br />
**DisplayName**: Secondary File Extension<br />
**LogicalName**: secondaryfileextension<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_SiteTitle"></a> SiteTitle

**Description**: The title of the parent document site<br />
**DisplayName**: Parent Site Title<br />
**LogicalName**: sitetitle<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_SiteUrl"></a> SiteUrl

**Description**: The site url for the parent document site<br />
**DisplayName**: Site Url<br />
**LogicalName**: siteurl<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_TransactionCurrencyIdName"></a> TransactionCurrencyIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: transactioncurrencyidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
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


### <a name="BKMK_ViewCount"></a> ViewCount

**Description**: Shows View Count of child folders.<br />
**DisplayName**: View Count<br />
**LogicalName**: viewcount<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_WebLocationUrl"></a> WebLocationUrl

**Description**: Shows the Web Location Url of Office Graph Document.<br />
**DisplayName**: Web Location Url<br />
**LogicalName**: weblocationurl<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [lk_officegraphdocument_createdonbehalfby](#BKMK_lk_officegraphdocument_createdonbehalfby)
- [lk_officegraphdocument_modifiedonbehalfby](#BKMK_lk_officegraphdocument_modifiedonbehalfby)
- [organization_officegraphdocument](#BKMK_organization_officegraphdocument)
- [TransactionCurrency_officegraphdocument](#BKMK_TransactionCurrency_officegraphdocument)


### <a name="BKMK_lk_officegraphdocument_createdonbehalfby"></a> lk_officegraphdocument_createdonbehalfby

See systemuser Entity [lk_officegraphdocument_createdonbehalfby](systemuser.md#BKMK_lk_officegraphdocument_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_officegraphdocument_modifiedonbehalfby"></a> lk_officegraphdocument_modifiedonbehalfby

See systemuser Entity [lk_officegraphdocument_modifiedonbehalfby](systemuser.md#BKMK_lk_officegraphdocument_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_officegraphdocument"></a> organization_officegraphdocument

See organization Entity [organization_officegraphdocument](organization.md#BKMK_organization_officegraphdocument) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_officegraphdocument"></a> TransactionCurrency_officegraphdocument

See transactioncurrency Entity [TransactionCurrency_officegraphdocument](transactioncurrency.md#BKMK_TransactionCurrency_officegraphdocument) One-To-Many relationship.
officegraphdocument

