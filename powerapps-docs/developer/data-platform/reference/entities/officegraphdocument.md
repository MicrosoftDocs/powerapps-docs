---
title: "OfficeGraphDocument table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the OfficeGraphDocument table/entity."
ms.date: 10/05/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "margoc"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# OfficeGraphDocument table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Office Graph Documents Description


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/officegraphdocuments<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|OfficeGraphDocuments|
|DisplayCollectionName|Office Graph Documents|
|DisplayName|Office Graph Document|
|EntitySetName|officegraphdocuments|
|IsBPFEntity|False|
|LogicalCollectionName|officegraphdocuments|
|LogicalName|officegraphdocument|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|officegraphdocumentid|
|PrimaryNameAttribute|title|
|SchemaName|OfficeGraphDocument|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [DocumentId](#BKMK_DocumentId)
- [OfficeGraphDocumentId](#BKMK_OfficeGraphDocumentId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [Title](#BKMK_Title)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_DocumentId"></a> DocumentId

|Property|Value|
|--------|-----|
|Description|Document Id.|
|DisplayName|Document Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|documentid|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OfficeGraphDocumentId"></a> OfficeGraphDocumentId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|OfficeGraphDocument|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|officegraphdocumentid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Time Zone Rule Version Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezoneruleversionnumber|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_Title"></a> Title

|Property|Value|
|--------|-----|
|Description|The title of the entity.|
|DisplayName|Title|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|title|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|--------|-----|
|Description|Exchange rate for the currency associated with the Office Graph Document with respect to the base currency.|
|DisplayName|Currency|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|transactioncurrencyid|
|RequiredLevel|None|
|Targets|transactioncurrency|
|Type|Lookup|


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|--------|-----|
|Description|Time zone code that was in use when the record was created.|
|DisplayName|UTC Conversion Time Zone Code|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|utcconversiontimezonecode|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

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

|Property|Value|
|--------|-----|
|Description|Shows Author Names of Office Graph Document.|
|DisplayName|Author Names|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|authornames|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Shows Created By of Office Graph Document.|
|DisplayName|Created By|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdby|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the record.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_CreatedTime"></a> CreatedTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was created.|
|DisplayName|Created Time|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_DocumentLastModifiedBy"></a> DocumentLastModifiedBy

|Property|Value|
|--------|-----|
|Description|Document Last Modified By|
|DisplayName|Document Last Modified By|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|documentlastmodifiedby|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_DocumentLastModifiedOn"></a> DocumentLastModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Document Last Modified On|
|DisplayName|Document Last Modified On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|documentlastmodifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_DocumentPreviewMetadata"></a> DocumentPreviewMetadata

|Property|Value|
|--------|-----|
|Description|document preview metadata|
|DisplayName|document preview metadata|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|documentpreviewmetadata|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|--------|-----|
|Description|Exchange rate for the currency associated with the Office Graph Document with respect to the base currency.|
|DisplayName|ExchangeRate|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.000000000001|
|Precision|12|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_FileExtension"></a> FileExtension

|Property|Value|
|--------|-----|
|Description|File Extension of Office Graph Document.|
|DisplayName|File Extension|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|fileextension|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_FileType"></a> FileType

|Property|Value|
|--------|-----|
|Description|Shows the File Type of Office Graph Document.|
|DisplayName|File Type|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|filetype|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Shows modified by of Office Graph Document.|
|DisplayName|Modified By|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedby|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the record.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ModifiedTime"></a> ModifiedTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was modified.|
|DisplayName|Modified Time|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier for the organization|
|DisplayName|Organization Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|None|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_PreviewImageUrl"></a> PreviewImageUrl

|Property|Value|
|--------|-----|
|Description|Shows the Preview Image Url Office Graph Document.|
|DisplayName|Preview Image Url|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|previewimageurl|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_QueryType"></a> QueryType

|Property|Value|
|--------|-----|
|Description|Shows Query Type of child folders|
|DisplayName|Query Type|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|querytype|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_Rank"></a> Rank

|Property|Value|
|--------|-----|
|Description|The relevancy rank of the document retrieved|
|DisplayName|Relevancy Rank of the Document|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|rank|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ReadUrl"></a> ReadUrl

|Property|Value|
|--------|-----|
|Description|The online read url|
|DisplayName|Read Url|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|readurl|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SecondaryFileExtension"></a> SecondaryFileExtension

|Property|Value|
|--------|-----|
|Description|Secondary File Extension of Office Graph Document.|
|DisplayName|Secondary File Extension|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|secondaryfileextension|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SiteTitle"></a> SiteTitle

|Property|Value|
|--------|-----|
|Description|The title of the parent document site|
|DisplayName|Parent Site Title|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|sitetitle|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SiteUrl"></a> SiteUrl

|Property|Value|
|--------|-----|
|Description|The site url for the parent document site|
|DisplayName|Site Url|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|siteurl|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TransactionCurrencyIdName"></a> TransactionCurrencyIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|transactioncurrencyidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|


### <a name="BKMK_ViewCount"></a> ViewCount

|Property|Value|
|--------|-----|
|Description|Shows View Count of child folders.|
|DisplayName|View Count|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|viewcount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_WebLocationUrl"></a> WebLocationUrl

|Property|Value|
|--------|-----|
|Description|Shows the Web Location Url of Office Graph Document.|
|DisplayName|Web Location Url|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|weblocationurl|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_officegraphdocument_createdonbehalfby](#BKMK_lk_officegraphdocument_createdonbehalfby)
- [lk_officegraphdocument_modifiedonbehalfby](#BKMK_lk_officegraphdocument_modifiedonbehalfby)
- [organization_officegraphdocument](#BKMK_organization_officegraphdocument)
- [TransactionCurrency_officegraphdocument](#BKMK_TransactionCurrency_officegraphdocument)


### <a name="BKMK_lk_officegraphdocument_createdonbehalfby"></a> lk_officegraphdocument_createdonbehalfby

See systemuser Table [lk_officegraphdocument_createdonbehalfby](systemuser.md#BKMK_lk_officegraphdocument_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_officegraphdocument_modifiedonbehalfby"></a> lk_officegraphdocument_modifiedonbehalfby

See systemuser Table [lk_officegraphdocument_modifiedonbehalfby](systemuser.md#BKMK_lk_officegraphdocument_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_officegraphdocument"></a> organization_officegraphdocument

See organization Table [organization_officegraphdocument](organization.md#BKMK_organization_officegraphdocument) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_officegraphdocument"></a> TransactionCurrency_officegraphdocument

See transactioncurrency Table [TransactionCurrency_officegraphdocument](transactioncurrency.md#BKMK_TransactionCurrency_officegraphdocument) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.officegraphdocument?text=officegraphdocument EntityType" />