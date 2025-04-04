---
title: "Document Suggestions (RecommendedDocument) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Document Suggestions (RecommendedDocument) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Document Suggestions (RecommendedDocument) table/entity reference (Microsoft Dataverse)

Document Suggestions

## Messages

The following table lists the messages for the Document Suggestions (RecommendedDocument) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `RetrieveMultiple`<br />Event: True |`GET` /recommendeddocuments<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Document Suggestions (RecommendedDocument) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Document Suggestions** |
| **DisplayCollectionName** | **Document Suggestions** |
| **SchemaName** | `RecommendedDocument` |
| **CollectionSchemaName** | `RecommendedDocuments` |
| **EntitySetName** | `recommendeddocuments`|
| **LogicalName** | `recommendeddocument` |
| **LogicalCollectionName** | `recommendeddocuments` |
| **PrimaryIdAttribute** | `recommendeddocumentid` |
| **PrimaryNameAttribute** |`title` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AssociatedRecordName](#BKMK_AssociatedRecordName)
- [Author](#BKMK_Author)
- [ExternalDocumentId](#BKMK_ExternalDocumentId)
- [ExternalModifiedBy](#BKMK_ExternalModifiedBy)
- [RecommendedDocumentId](#BKMK_RecommendedDocumentId)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [Source](#BKMK_Source)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [Title](#BKMK_Title)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_AssociatedRecordName"></a> AssociatedRecordName

|Property|Value|
|---|---|
|Description|**Shows the associated record name of the recommended document.**|
|DisplayName|**Associated Record Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`associatedrecordname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_Author"></a> Author

|Property|Value|
|---|---|
|Description|**Shows the name of the author of the recommended document.**|
|DisplayName|**Author**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`author`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_ExternalDocumentId"></a> ExternalDocumentId

|Property|Value|
|---|---|
|Description|**Shows the external document.**|
|DisplayName|**External Document ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`externaldocumentid`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ExternalModifiedBy"></a> ExternalModifiedBy

|Property|Value|
|---|---|
|Description|**Shows who last updated the document record.**|
|DisplayName|**Modified by**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`externalmodifiedby`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_RecommendedDocumentId"></a> RecommendedDocumentId

|Property|Value|
|---|---|
|Description|**Shows the recommended document record.**|
|DisplayName|**Recommended Document**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`recommendeddocumentid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**Choose the parent record that the recommended document record is associated with.**|
|DisplayName|**Regarding**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets||

### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_Source"></a> Source

|Property|Value|
|---|---|
|Description|**Shows the source storage of the recommended document.**|
|DisplayName|**Source**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`source`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

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
|Description|**Type a title for the entity.**|
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
|MaxLength|160|

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Shows the exchange rate for the currency associated with the recommended document with respect to the base currency.**|
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
|Description|**Shows the time zone code that was in use when the record was created.**|
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

- [AbsoluteUrl](#BKMK_AbsoluteUrl)
- [ContentType](#BKMK_ContentType)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [EditUrl](#BKMK_EditUrl)
- [ExchangeRate](#BKMK_ExchangeRate)
- [FileSize](#BKMK_FileSize)
- [FileType](#BKMK_FileType)
- [FullName](#BKMK_FullName)
- [IconClassName](#BKMK_IconClassName)
- [Location](#BKMK_Location)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [ReadUrl](#BKMK_ReadUrl)
- [Version](#BKMK_Version)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_AbsoluteUrl"></a> AbsoluteUrl

|Property|Value|
|---|---|
|Description|**Type the URL where the recommended document is located.**|
|DisplayName|**Absolute URL**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`absoluteurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_ContentType"></a> ContentType

|Property|Value|
|---|---|
|Description|**Select the document content type.**|
|DisplayName|**Content Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`contenttype`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Shows the user who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
|DisplayName|**Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Shows who created the record on behalf of another user.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_EditUrl"></a> EditUrl

|Property|Value|
|---|---|
|Description|**Shows the Edit URL of the recommended document.**|
|DisplayName|**Edit Web App URL**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`editurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|---|---|
|Description|**Shows the exchange rate for the currency associated with the recommended document with respect to the base currency.**|
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

### <a name="BKMK_FileSize"></a> FileSize

|Property|Value|
|---|---|
|Description|**Shows the file size.**|
|DisplayName|**File Size**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`filesize`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_FileType"></a> FileType

|Property|Value|
|---|---|
|Description|**Shows the file type.**|
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
|MaxLength|200|

### <a name="BKMK_FullName"></a> FullName

|Property|Value|
|---|---|
|Description|**Shows the full name of the recommended document.**|
|DisplayName|**Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fullname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_IconClassName"></a> IconClassName

|Property|Value|
|---|---|
|Description|**Stores the Icon Class name of the recommended document.**|
|DisplayName|**Icon Class Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iconclassname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_Location"></a> Location

|Property|Value|
|---|---|
|Description|**Shows the location of the recommended document.**|
|DisplayName|**Path**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`location`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Shows who last updated the record.**|
|DisplayName|**Modified By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
|DisplayName|**Modified On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Shows who last updated the record on behalf of another user.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Shows the organization.**|
|DisplayName|**Organization ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_ReadUrl"></a> ReadUrl

|Property|Value|
|---|---|
|Description|**Shows the Read URL of the recommended document.**|
|DisplayName|**Read Web App URL**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`readurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_Version"></a> Version

|Property|Value|
|---|---|
|Description|**Shows the recommended document version.**|
|DisplayName|**Recommended Document Version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`version`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

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

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [lk_recommendeddocument_createdby](#BKMK_lk_recommendeddocument_createdby)
- [lk_recommendeddocument_createdonbehalfby](#BKMK_lk_recommendeddocument_createdonbehalfby)
- [lk_recommendeddocument_modifiedby](#BKMK_lk_recommendeddocument_modifiedby)
- [lk_recommendeddocument_modifiedonbehalfby](#BKMK_lk_recommendeddocument_modifiedonbehalfby)
- [organization_recommendeddocument](#BKMK_organization_recommendeddocument)
- [TransactionCurrency_recommendeddocument](#BKMK_TransactionCurrency_recommendeddocument)

### <a name="BKMK_lk_recommendeddocument_createdby"></a> lk_recommendeddocument_createdby

One-To-Many Relationship: [systemuser lk_recommendeddocument_createdby](systemuser.md#BKMK_lk_recommendeddocument_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdbyname`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_recommendeddocument_createdonbehalfby"></a> lk_recommendeddocument_createdonbehalfby

One-To-Many Relationship: [systemuser lk_recommendeddocument_createdonbehalfby](systemuser.md#BKMK_lk_recommendeddocument_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfbyname`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_recommendeddocument_modifiedby"></a> lk_recommendeddocument_modifiedby

One-To-Many Relationship: [systemuser lk_recommendeddocument_modifiedby](systemuser.md#BKMK_lk_recommendeddocument_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedbyname`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_recommendeddocument_modifiedonbehalfby"></a> lk_recommendeddocument_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_recommendeddocument_modifiedonbehalfby](systemuser.md#BKMK_lk_recommendeddocument_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfbyname`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_recommendeddocument"></a> organization_recommendeddocument

One-To-Many Relationship: [organization organization_recommendeddocument](organization.md#BKMK_organization_recommendeddocument)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_recommendeddocument"></a> TransactionCurrency_recommendeddocument

One-To-Many Relationship: [transactioncurrency TransactionCurrency_recommendeddocument](transactioncurrency.md#BKMK_TransactionCurrency_recommendeddocument)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencingEntityNavigationPropertyName|`transactioncurrencyidname`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.recommendeddocument?displayProperty=fullName>
