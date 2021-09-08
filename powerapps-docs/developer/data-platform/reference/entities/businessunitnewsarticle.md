---
title: "BusinessUnitNewsArticle table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the BusinessUnitNewsArticle table/entity."
ms.date: 05/20/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# BusinessUnitNewsArticle table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Announcement associated with an organization.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/businessunitnewsarticles<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/businessunitnewsarticles(*businessunitnewsarticleid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/businessunitnewsarticles(*businessunitnewsarticleid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/businessunitnewsarticles<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/businessunitnewsarticles(*businessunitnewsarticleid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|BusinessUnitNewsArticles|
|DisplayCollectionName|Announcements|
|DisplayName|Announcement|
|EntitySetName|businessunitnewsarticles|
|IsBPFEntity|False|
|LogicalCollectionName|businessunitnewsarticles|
|LogicalName|businessunitnewsarticle|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|businessunitnewsarticleid|
|PrimaryNameAttribute|articletitle|
|SchemaName|BusinessUnitNewsArticle|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ActiveOn](#BKMK_ActiveOn)
- [ActiveUntil](#BKMK_ActiveUntil)
- [ArticleTitle](#BKMK_ArticleTitle)
- [ArticleTypeCode](#BKMK_ArticleTypeCode)
- [ArticleUrl](#BKMK_ArticleUrl)
- [BusinessUnitNewsArticleId](#BKMK_BusinessUnitNewsArticleId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [NewsArticle](#BKMK_NewsArticle)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [ShowOnHomepage](#BKMK_ShowOnHomepage)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_ActiveOn"></a> ActiveOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time for the announcement to become active.|
|DisplayName|Active On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|activeon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ActiveUntil"></a> ActiveUntil

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time of the last day the announcement is active.|
|DisplayName|Expiration Date|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|activeuntil|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ArticleTitle"></a> ArticleTitle

|Property|Value|
|--------|-----|
|Description|Title of the announcement.|
|DisplayName|Title|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|articletitle|
|MaxLength|300|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_ArticleTypeCode"></a> ArticleTypeCode

|Property|Value|
|--------|-----|
|Description|Type of announcement.|
|DisplayName|Visible To|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|articletypecode|
|RequiredLevel|None|
|Type|Picklist|

#### ArticleTypeCode Choices/Options

|Value|Label|
|-----|-----|
|1|All Users|
|2|Sales Users|
|3|Service Users|



### <a name="BKMK_ArticleUrl"></a> ArticleUrl

|Property|Value|
|--------|-----|
|Description|URL for the Website on which the announcement is located.|
|DisplayName|More Information URL|
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|articleurl|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_BusinessUnitNewsArticleId"></a> BusinessUnitNewsArticleId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the announcement.|
|DisplayName|Announcement|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|businessunitnewsarticleid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|Unique identifier of the data import or data migration that created this record.|
|DisplayName|Import Sequence Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|importsequencenumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_NewsArticle"></a> NewsArticle

|Property|Value|
|--------|-----|
|Description|Text for the announcement.|
|DisplayName|Description|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|newsarticle|
|MaxLength|1073741823|
|RequiredLevel|ApplicationRequired|
|Type|Memo|


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time that the record was migrated.|
|DisplayName|Record Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ShowOnHomepage"></a> ShowOnHomepage

|Property|Value|
|--------|-----|
|Description|Information about whether to show the announcement on the Website home page.|
|DisplayName|Show in Workplace|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|showonhomepage|
|RequiredLevel|None|
|Type|Boolean|

#### ShowOnHomepage Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezoneruleversionnumber|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|--------|-----|
|Description|Time zone code that was in use when the record was created.|
|DisplayName||
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

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the announcement.|
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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the announcement was created.|
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
|Description|Unique identifier of the delegate user who created the businessunitnewsarticle.|
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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the announcement.|
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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the announcement was last modified.|
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
|Description|Unique identifier of the delegate user who last modified the businessunitnewsarticle.|
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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the organization associated with the announcement.|
|DisplayName|Organization|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|SystemRequired|
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

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [BusinessUnitNewsArticle_ProcessSessions](#BKMK_BusinessUnitNewsArticle_ProcessSessions)
- [BusinessUnitNewsArticle_AsyncOperations](#BKMK_BusinessUnitNewsArticle_AsyncOperations)
- [BusinessUnitNewsArticle_BulkDeleteFailures](#BKMK_BusinessUnitNewsArticle_BulkDeleteFailures)


### <a name="BKMK_BusinessUnitNewsArticle_ProcessSessions"></a> BusinessUnitNewsArticle_ProcessSessions

Same as processsession table [BusinessUnitNewsArticle_ProcessSessions](processsession.md#BKMK_BusinessUnitNewsArticle_ProcessSessions) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|BusinessUnitNewsArticle_ProcessSessions|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 110|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_BusinessUnitNewsArticle_AsyncOperations"></a> BusinessUnitNewsArticle_AsyncOperations

Same as asyncoperation table [BusinessUnitNewsArticle_AsyncOperations](asyncoperation.md#BKMK_BusinessUnitNewsArticle_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|BusinessUnitNewsArticle_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_BusinessUnitNewsArticle_BulkDeleteFailures"></a> BusinessUnitNewsArticle_BulkDeleteFailures

Same as bulkdeletefailure table [BusinessUnitNewsArticle_BulkDeleteFailures](bulkdeletefailure.md#BKMK_BusinessUnitNewsArticle_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|BusinessUnitNewsArticle_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_businessunitnewsarticle_createdonbehalfby](#BKMK_lk_businessunitnewsarticle_createdonbehalfby)
- [organization_business_unit_news_articles](#BKMK_organization_business_unit_news_articles)
- [lk_businessunitnewsarticle_modifiedonbehalfby](#BKMK_lk_businessunitnewsarticle_modifiedonbehalfby)
- [lk_businessunitnewsarticlebase_createdby](#BKMK_lk_businessunitnewsarticlebase_createdby)
- [lk_businessunitnewsarticlebase_modifiedby](#BKMK_lk_businessunitnewsarticlebase_modifiedby)


### <a name="BKMK_lk_businessunitnewsarticle_createdonbehalfby"></a> lk_businessunitnewsarticle_createdonbehalfby

See systemuser Table [lk_businessunitnewsarticle_createdonbehalfby](systemuser.md#BKMK_lk_businessunitnewsarticle_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_business_unit_news_articles"></a> organization_business_unit_news_articles

See organization Table [organization_business_unit_news_articles](organization.md#BKMK_organization_business_unit_news_articles) One-To-Many relationship.

### <a name="BKMK_lk_businessunitnewsarticle_modifiedonbehalfby"></a> lk_businessunitnewsarticle_modifiedonbehalfby

See systemuser Table [lk_businessunitnewsarticle_modifiedonbehalfby](systemuser.md#BKMK_lk_businessunitnewsarticle_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_businessunitnewsarticlebase_createdby"></a> lk_businessunitnewsarticlebase_createdby

See systemuser Table [lk_businessunitnewsarticlebase_createdby](systemuser.md#BKMK_lk_businessunitnewsarticlebase_createdby) One-To-Many relationship.

### <a name="BKMK_lk_businessunitnewsarticlebase_modifiedby"></a> lk_businessunitnewsarticlebase_modifiedby

See systemuser Table [lk_businessunitnewsarticlebase_modifiedby](systemuser.md#BKMK_lk_businessunitnewsarticlebase_modifiedby) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.businessunitnewsarticle?text=businessunitnewsarticle EntityType" />