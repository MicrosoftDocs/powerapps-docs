---
title: "Office Graph Document (OfficeGraphDocument) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Office Graph Document (OfficeGraphDocument) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Office Graph Document (OfficeGraphDocument) table/entity reference (Microsoft Dataverse)

Office Graph Documents Description

## Messages

The following table lists the messages for the Office Graph Document (OfficeGraphDocument) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `RetrieveMultiple`<br />Event: True |`GET` /officegraphdocuments<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Office Graph Document (OfficeGraphDocument) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Office Graph Document** |
| **DisplayCollectionName** | **Office Graph Documents** |
| **SchemaName** | `OfficeGraphDocument` |
| **CollectionSchemaName** | `OfficeGraphDocuments` |
| **EntitySetName** | `officegraphdocuments`|
| **LogicalName** | `officegraphdocument` |
| **LogicalCollectionName** | `officegraphdocuments` |
| **PrimaryIdAttribute** | `officegraphdocumentid` |
| **PrimaryNameAttribute** |`title` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

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
|---|---|
|Description|**Document Id.**|
|DisplayName|**Document Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`documentid`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OfficeGraphDocumentId"></a> OfficeGraphDocumentId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**OfficeGraphDocument**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`officegraphdocumentid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Time Zone Rule Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezoneruleversionnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_Title"></a> Title

|Property|Value|
|---|---|
|Description|**The title of the entity.**|
|DisplayName|**Title**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`title`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Exchange rate for the currency associated with the Office Graph Document with respect to the base currency.**|
|DisplayName|**Currency**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`transactioncurrencyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|transactioncurrency|

### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|---|---|
|Description|**Time zone code that was in use when the record was created.**|
|DisplayName|**UTC Conversion Time Zone Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`utcconversiontimezonecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [AuthorNames](#BKMK_AuthorNames)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedTime](#BKMK_CreatedTime)
- [DocumentLastModifiedBy](#BKMK_DocumentLastModifiedBy)
- [DocumentLastModifiedOn](#BKMK_DocumentLastModifiedOn)
- [DocumentPreviewMetadata](#BKMK_DocumentPreviewMetadata)
- [ExchangeRate](#BKMK_ExchangeRate)
- [FileExtension](#BKMK_FileExtension)
- [FileType](#BKMK_FileType)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedTime](#BKMK_ModifiedTime)
- [OrganizationId](#BKMK_OrganizationId)
- [PreviewImageUrl](#BKMK_PreviewImageUrl)
- [QueryType](#BKMK_QueryType)
- [Rank](#BKMK_Rank)
- [ReadUrl](#BKMK_ReadUrl)
- [SecondaryFileExtension](#BKMK_SecondaryFileExtension)
- [SiteTitle](#BKMK_SiteTitle)
- [SiteUrl](#BKMK_SiteUrl)
- [VersionNumber](#BKMK_VersionNumber)
- [ViewCount](#BKMK_ViewCount)
- [WebLocationUrl](#BKMK_WebLocationUrl)

### <a name="BKMK_AuthorNames"></a> AuthorNames

|Property|Value|
|---|---|
|Description|**Shows Author Names of Office Graph Document.**|
|DisplayName|**Author Names**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`authornames`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Shows Created By of Office Graph Document.**|
|DisplayName|**Created By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who created the record.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedTime"></a> CreatedTime

|Property|Value|
|---|---|
|Description|**Date and time when the record was created.**|
|DisplayName|**Created Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_DocumentLastModifiedBy"></a> DocumentLastModifiedBy

|Property|Value|
|---|---|
|Description|**Document Last Modified By**|
|DisplayName|**Document Last Modified By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`documentlastmodifiedby`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_DocumentLastModifiedOn"></a> DocumentLastModifiedOn

|Property|Value|
|---|---|
|Description|**Document Last Modified On**|
|DisplayName|**Document Last Modified On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`documentlastmodifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_DocumentPreviewMetadata"></a> DocumentPreviewMetadata

|Property|Value|
|---|---|
|Description|**document preview metadata**|
|DisplayName|**document preview metadata**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`documentpreviewmetadata`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|---|---|
|Description|**Exchange rate for the currency associated with the Office Graph Document with respect to the base currency.**|
|DisplayName|**ExchangeRate**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`exchangerate`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Disabled|
|MaxValue|100000000000|
|MinValue|1E-12|
|Precision|12|
|SourceTypeMask|0|

### <a name="BKMK_FileExtension"></a> FileExtension

|Property|Value|
|---|---|
|Description|**File Extension of Office Graph Document.**|
|DisplayName|**File Extension**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fileextension`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_FileType"></a> FileType

|Property|Value|
|---|---|
|Description|**Shows the File Type of Office Graph Document.**|
|DisplayName|**File Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`filetype`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Shows modified by of Office Graph Document.**|
|DisplayName|**Modified By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who modified the record.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedTime"></a> ModifiedTime

|Property|Value|
|---|---|
|Description|**Date and time when the record was modified.**|
|DisplayName|**Modified Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier for the organization**|
|DisplayName|**Organization Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_PreviewImageUrl"></a> PreviewImageUrl

|Property|Value|
|---|---|
|Description|**Shows the Preview Image Url Office Graph Document.**|
|DisplayName|**Preview Image Url**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`previewimageurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_QueryType"></a> QueryType

|Property|Value|
|---|---|
|Description|**Shows Query Type of child folders**|
|DisplayName|**Query Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`querytype`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_Rank"></a> Rank

|Property|Value|
|---|---|
|Description|**The relevancy rank of the document retrieved**|
|DisplayName|**Relevancy Rank of the Document**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`rank`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_ReadUrl"></a> ReadUrl

|Property|Value|
|---|---|
|Description|**The online read url**|
|DisplayName|**Read Url**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`readurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_SecondaryFileExtension"></a> SecondaryFileExtension

|Property|Value|
|---|---|
|Description|**Secondary File Extension of Office Graph Document.**|
|DisplayName|**Secondary File Extension**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`secondaryfileextension`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_SiteTitle"></a> SiteTitle

|Property|Value|
|---|---|
|Description|**The title of the parent document site**|
|DisplayName|**Parent Site Title**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sitetitle`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_SiteUrl"></a> SiteUrl

|Property|Value|
|---|---|
|Description|**The site url for the parent document site**|
|DisplayName|**Site Url**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`siteurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_ViewCount"></a> ViewCount

|Property|Value|
|---|---|
|Description|**Shows View Count of child folders.**|
|DisplayName|**View Count**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`viewcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_WebLocationUrl"></a> WebLocationUrl

|Property|Value|
|---|---|
|Description|**Shows the Web Location Url of Office Graph Document.**|
|DisplayName|**Web Location Url**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`weblocationurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [lk_officegraphdocument_createdonbehalfby](#BKMK_lk_officegraphdocument_createdonbehalfby)
- [lk_officegraphdocument_modifiedonbehalfby](#BKMK_lk_officegraphdocument_modifiedonbehalfby)
- [organization_officegraphdocument](#BKMK_organization_officegraphdocument)
- [TransactionCurrency_officegraphdocument](#BKMK_TransactionCurrency_officegraphdocument)

### <a name="BKMK_lk_officegraphdocument_createdonbehalfby"></a> lk_officegraphdocument_createdonbehalfby

One-To-Many Relationship: [systemuser lk_officegraphdocument_createdonbehalfby](systemuser.md#BKMK_lk_officegraphdocument_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_officegraphdocument_modifiedonbehalfby"></a> lk_officegraphdocument_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_officegraphdocument_modifiedonbehalfby](systemuser.md#BKMK_lk_officegraphdocument_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_officegraphdocument"></a> organization_officegraphdocument

One-To-Many Relationship: [organization organization_officegraphdocument](organization.md#BKMK_organization_officegraphdocument)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_officegraphdocument"></a> TransactionCurrency_officegraphdocument

One-To-Many Relationship: [transactioncurrency TransactionCurrency_officegraphdocument](transactioncurrency.md#BKMK_TransactionCurrency_officegraphdocument)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencingEntityNavigationPropertyName|`transactioncurrencyid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.officegraphdocument?displayProperty=fullName>
