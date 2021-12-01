---
title: "Document Suggestions (RecommendedDocument) table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Document Suggestions (RecommendedDocument) table/entity."
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

# Document Suggestions (RecommendedDocument) table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Document Suggestions


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/recommendeddocuments<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|RecommendedDocuments|
|DisplayCollectionName|Document Suggestions|
|DisplayName|Document Suggestions|
|EntitySetName|recommendeddocuments|
|IsBPFEntity|False|
|LogicalCollectionName|recommendeddocuments|
|LogicalName|recommendeddocument|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|recommendeddocumentid|
|PrimaryNameAttribute|title|
|SchemaName|RecommendedDocument|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AssociatedRecordName](#BKMK_AssociatedRecordName)
- [Author](#BKMK_Author)
- [ExternalDocumentId](#BKMK_ExternalDocumentId)
- [ExternalModifiedBy](#BKMK_ExternalModifiedBy)
- [RecommendedDocumentId](#BKMK_RecommendedDocumentId)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [Source](#BKMK_Source)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [Title](#BKMK_Title)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_AssociatedRecordName"></a> AssociatedRecordName

|Property|Value|
|--------|-----|
|Description|Shows the associated record name of the recommended document.|
|DisplayName|Associated Record Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|associatedrecordname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Author"></a> Author

|Property|Value|
|--------|-----|
|Description|Shows the name of the author of the recommended document.|
|DisplayName|Author|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|author|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ExternalDocumentId"></a> ExternalDocumentId

|Property|Value|
|--------|-----|
|Description|Shows the external document.|
|DisplayName|External Document ID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|externaldocumentid|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ExternalModifiedBy"></a> ExternalModifiedBy

|Property|Value|
|--------|-----|
|Description|Shows who last updated the document record.|
|DisplayName|Modified by|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|externalmodifiedby|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RecommendedDocumentId"></a> RecommendedDocumentId

|Property|Value|
|--------|-----|
|Description|Shows the recommended document record.|
|DisplayName|Recommended Document|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|recommendeddocumentid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|--------|-----|
|Description|Choose the parent record that the recommended document record is associated with.|
|DisplayName|Regarding|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjectid|
|RequiredLevel|None|
|Targets||
|Type|Lookup|


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjectidname|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjecttypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_Source"></a> Source

|Property|Value|
|--------|-----|
|Description|Shows the source storage of the recommended document.|
|DisplayName|Source|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|source|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


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
|Description|Type a title for the entity.|
|DisplayName|Title|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|title|
|MaxLength|160|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|--------|-----|
|Description|Shows the exchange rate for the currency associated with the recommended document with respect to the base currency.|
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
|Description|Shows the time zone code that was in use when the record was created.|
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

- [AbsoluteUrl](#BKMK_AbsoluteUrl)
- [ContentType](#BKMK_ContentType)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [EditUrl](#BKMK_EditUrl)
- [ExchangeRate](#BKMK_ExchangeRate)
- [FileSize](#BKMK_FileSize)
- [FileType](#BKMK_FileType)
- [FullName](#BKMK_FullName)
- [IconClassName](#BKMK_IconClassName)
- [Location](#BKMK_Location)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [ReadUrl](#BKMK_ReadUrl)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [Version](#BKMK_Version)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_AbsoluteUrl"></a> AbsoluteUrl

|Property|Value|
|--------|-----|
|Description|Type the URL where the recommended document is located.|
|DisplayName|Absolute URL|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|absoluteurl|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ContentType"></a> ContentType

|Property|Value|
|--------|-----|
|Description|Select the document content type.|
|DisplayName|Content Type|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|contenttype|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Shows the user who created the record.|
|DisplayName|Created By|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Shows who created the record on behalf of another user.|
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


### <a name="BKMK_EditUrl"></a> EditUrl

|Property|Value|
|--------|-----|
|Description|Shows the Edit URL of the recommended document.|
|DisplayName|Edit Web App URL|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|editurl|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|--------|-----|
|Description|Shows the exchange rate for the currency associated with the recommended document with respect to the base currency.|
|DisplayName|ExchangeRate|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.000000000001|
|Precision|12|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_FileSize"></a> FileSize

|Property|Value|
|--------|-----|
|Description|Shows the file size.|
|DisplayName|File Size|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|filesize|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_FileType"></a> FileType

|Property|Value|
|--------|-----|
|Description|Shows the file type.|
|DisplayName|File Type|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|filetype|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_FullName"></a> FullName

|Property|Value|
|--------|-----|
|Description|Shows the full name of the recommended document.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|fullname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IconClassName"></a> IconClassName

|Property|Value|
|--------|-----|
|Description|Stores the Icon Class name of the recommended document.|
|DisplayName|Icon Class Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iconclassname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Location"></a> Location

|Property|Value|
|--------|-----|
|Description|Shows the location of the recommended document.|
|DisplayName|Path|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|location|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Shows who last updated the record.|
|DisplayName|Modified By|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Shows who last updated the record on behalf of another user.|
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


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Shows the organization.|
|DisplayName|Organization ID|
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


### <a name="BKMK_ReadUrl"></a> ReadUrl

|Property|Value|
|--------|-----|
|Description|Shows the Read URL of the recommended document.|
|DisplayName|Read Web App URL|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|readurl|
|MaxLength|200|
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


### <a name="BKMK_Version"></a> Version

|Property|Value|
|--------|-----|
|Description|Shows the recommended document version.|
|DisplayName|Recommended Document Version|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|version|
|MaxLength|200|
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_recommendeddocument_createdby](#BKMK_lk_recommendeddocument_createdby)
- [lk_recommendeddocument_createdonbehalfby](#BKMK_lk_recommendeddocument_createdonbehalfby)
- [lk_recommendeddocument_modifiedby](#BKMK_lk_recommendeddocument_modifiedby)
- [lk_recommendeddocument_modifiedonbehalfby](#BKMK_lk_recommendeddocument_modifiedonbehalfby)
- [organization_recommendeddocument](#BKMK_organization_recommendeddocument)
- [TransactionCurrency_recommendeddocument](#BKMK_TransactionCurrency_recommendeddocument)


### <a name="BKMK_lk_recommendeddocument_createdby"></a> lk_recommendeddocument_createdby

See systemuser Table [lk_recommendeddocument_createdby](systemuser.md#BKMK_lk_recommendeddocument_createdby) One-To-Many relationship.

### <a name="BKMK_lk_recommendeddocument_createdonbehalfby"></a> lk_recommendeddocument_createdonbehalfby

See systemuser Table [lk_recommendeddocument_createdonbehalfby](systemuser.md#BKMK_lk_recommendeddocument_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_recommendeddocument_modifiedby"></a> lk_recommendeddocument_modifiedby

See systemuser Table [lk_recommendeddocument_modifiedby](systemuser.md#BKMK_lk_recommendeddocument_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_recommendeddocument_modifiedonbehalfby"></a> lk_recommendeddocument_modifiedonbehalfby

See systemuser Table [lk_recommendeddocument_modifiedonbehalfby](systemuser.md#BKMK_lk_recommendeddocument_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_recommendeddocument"></a> organization_recommendeddocument

See organization Table [organization_recommendeddocument](organization.md#BKMK_organization_recommendeddocument) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_recommendeddocument"></a> TransactionCurrency_recommendeddocument

See transactioncurrency Table [TransactionCurrency_recommendeddocument](transactioncurrency.md#BKMK_TransactionCurrency_recommendeddocument) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.recommendeddocument?text=recommendeddocument EntityType" />