---
title: "Article (KbArticle) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Article (KbArticle) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Article (KbArticle) table/entity reference (Microsoft Dataverse)

Structured content that is part of the knowledge base.

## Messages

The following table lists the messages for the Article (KbArticle) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /kbarticles<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /kbarticles(*kbarticleid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /kbarticles(*kbarticleid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveByTopIncidentProductKbArticle`<br />Event: False | |<xref:Microsoft.Crm.Sdk.Messages.RetrieveByTopIncidentProductKbArticleRequest>|
| `RetrieveByTopIncidentSubjectKbArticle`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveByTopIncidentSubjectKbArticle?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveByTopIncidentSubjectKbArticleRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /kbarticles<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SearchByBodyKbArticle`<br />Event: False |<xref:Microsoft.Dynamics.CRM.SearchByBodyKbArticle?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.SearchByBodyKbArticleRequest>|
| `SearchByKeywordsKbArticle`<br />Event: False |<xref:Microsoft.Dynamics.CRM.SearchByKeywordsKbArticle?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.SearchByKeywordsKbArticleRequest>|
| `SearchByTitleKbArticle`<br />Event: False |<xref:Microsoft.Dynamics.CRM.SearchByTitleKbArticle?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.SearchByTitleKbArticleRequest>|
| `SetState`<br />Event: True |`PATCH` /kbarticles(*kbarticleid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /kbarticles(*kbarticleid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /kbarticles(*kbarticleid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Article (KbArticle) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Article** |
| **DisplayCollectionName** | **Articles** |
| **SchemaName** | `KbArticle` |
| **CollectionSchemaName** | `KbArticles` |
| **EntitySetName** | `kbarticles`|
| **LogicalName** | `kbarticle` |
| **LogicalCollectionName** | `kbarticles` |
| **PrimaryIdAttribute** | `kbarticleid` |
| **PrimaryNameAttribute** |`title` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [adx_averagerating](#BKMK_adx_averagerating)
- [adx_averagerating_int](#BKMK_adx_averagerating_int)
- [adx_downvotes](#BKMK_adx_downvotes)
- [adx_ratingcount](#BKMK_adx_ratingcount)
- [adx_ratingsum](#BKMK_adx_ratingsum)
- [adx_upvotes](#BKMK_adx_upvotes)
- [ArticleXml](#BKMK_ArticleXml)
- [Comments](#BKMK_Comments)
- [Description](#BKMK_Description)
- [EntityImage](#BKMK_EntityImage)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [KbArticleId](#BKMK_KbArticleId)
- [KbArticleTemplateId](#BKMK_KbArticleTemplateId)
- [KeyWords](#BKMK_KeyWords)
- [LanguageCode](#BKMK_LanguageCode)
- [msa_publishtoweb](#BKMK_msa_publishtoweb)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [SubjectId](#BKMK_SubjectId)
- [Title](#BKMK_Title)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)

### <a name="BKMK_adx_averagerating"></a> adx_averagerating

|Property|Value|
|---|---|
|Description|**The average rating of this article.**|
|DisplayName|**Average Rating**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_averagerating`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Auto|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|

### <a name="BKMK_adx_averagerating_int"></a> adx_averagerating_int

|Property|Value|
|---|---|
|Description|**The average rating of this article, rounded to a whole number (positive integer).**|
|DisplayName|**Average Rating (Whole Number)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_averagerating_int`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_adx_downvotes"></a> adx_downvotes

|Property|Value|
|---|---|
|Description|**The number of negative vote ratings applied to this article.**|
|DisplayName|**Downvotes**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_downvotes`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_adx_ratingcount"></a> adx_ratingcount

|Property|Value|
|---|---|
|Description||
|DisplayName|**Rating Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_ratingcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_adx_ratingsum"></a> adx_ratingsum

|Property|Value|
|---|---|
|Description|**The sum of the values of all ratings applied to this article.**|
|DisplayName|**Rating Sum**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_ratingsum`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_adx_upvotes"></a> adx_upvotes

|Property|Value|
|---|---|
|Description|**The number of positive vote ratings applied to this article.**|
|DisplayName|**Upvotes**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_upvotes`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ArticleXml"></a> ArticleXml

|Property|Value|
|---|---|
|Description|**Shows the article content and formatting, stored as XML.**|
|DisplayName|**Article XML**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`articlexml`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_Comments"></a> Comments

|Property|Value|
|---|---|
|Description|**Comments regarding the knowledge base article.**|
|DisplayName|**Comments**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`comments`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Type additional information that describes the knowledge base article.**|
|DisplayName|**Description**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_EntityImage"></a> EntityImage

|Property|Value|
|---|---|
|Description|**The default image for the entity.**|
|DisplayName|**Entity Image**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimage`|
|RequiredLevel|None|
|Type|Image|
|CanStoreFullImage|False|
|IsPrimaryImage|True|
|MaxHeight|144|
|MaxSizeInKB|10240|
|MaxWidth|144|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Unique identifier of the data import or data migration that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_KbArticleId"></a> KbArticleId

|Property|Value|
|---|---|
|Description|**Shows the ID of the article.**|
|DisplayName|**Article**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`kbarticleid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_KbArticleTemplateId"></a> KbArticleTemplateId

|Property|Value|
|---|---|
|Description|**Choose the template that you want to use as a base for creating the new article.**|
|DisplayName|**Base Template**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`kbarticletemplateid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|kbarticletemplate|

### <a name="BKMK_KeyWords"></a> KeyWords

|Property|Value|
|---|---|
|Description|**Keywords to be used for searches in knowledge base articles.**|
|DisplayName|**Key Words**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`keywords`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_LanguageCode"></a> LanguageCode

|Property|Value|
|---|---|
|Description|**Select which language the article must be available in. This list is based on the list of language packs that are installed in your Microsoft Dynamics 365 environment.**|
|DisplayName|**Language**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`languagecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msa_publishtoweb"></a> msa_publishtoweb

|Property|Value|
|---|---|
|Description|**If set to Yes, the article will be visible and searchable on portals connected to this organization.**|
|DisplayName|**Publish to Web**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msa_publishtoweb`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msa_publishtoweb_kbarticle`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|---|---|
|Description|**Date and time that the record was migrated.**|
|DisplayName|**Record Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overriddencreatedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Shows whether the knowledge base article is in draft, unapproved, or published status. Published articles are read-only and can't be edited unless they are unpublished.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|1|
|GlobalChoiceName|`kbarticle_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Draft**<br />DefaultStatus: 1<br />InvariantName: `Draft`|
|2|Label: **Unapproved**<br />DefaultStatus: 2<br />InvariantName: `Unapproved`|
|3|Label: **Published**<br />DefaultStatus: 3<br />InvariantName: `Published`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Select the article's status.**|
|DisplayName|**Status Reason**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`kbarticle_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Draft**<br />State:1<br />TransitionData: None|
|2|Label: **Unapproved**<br />State:2<br />TransitionData: None|
|3|Label: **Published**<br />State:3<br />TransitionData: None|

### <a name="BKMK_SubjectId"></a> SubjectId

|Property|Value|
|---|---|
|Description|**Choose the subject of the article to assist with article searches. You can configure subjects under Business Management in the Settings area.**|
|DisplayName|**Subject**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`subjectid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|subject|

### <a name="BKMK_Title"></a> Title

|Property|Value|
|---|---|
|Description|**Type a subject or descriptive name for the article to assist with article searches.**|
|DisplayName|**Title**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`title`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Choose the local currency for the record to make sure budgets are reported in the correct currency.**|
|DisplayName|**Currency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`transactioncurrencyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|transactioncurrency|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [Content](#BKMK_Content)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [ExchangeRate](#BKMK_ExchangeRate)
- [KbArticleTemplateIdTitle](#BKMK_KbArticleTemplateIdTitle)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [Number](#BKMK_Number)
- [OrganizationId](#BKMK_OrganizationId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_Content"></a> Content

|Property|Value|
|---|---|
|Description|**Description of the content of the knowledge base article.**|
|DisplayName|**Content**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`content`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the knowledge base article.**|
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
|Description|**Date and time when the knowledge base article was created.**|
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
|Description|**Unique identifier of the delegate user who created the article.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_EntityImage_Timestamp"></a> EntityImage_Timestamp

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimage_timestamp`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_EntityImage_URL"></a> EntityImage_URL

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimage_url`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_EntityImageId"></a> EntityImageId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Entity Image Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimageid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|---|---|
|Description|**Shows the conversion rate of the record's currency. The exchange rate is used to convert all money fields in the record from the local currency to the system's default currency.**|
|DisplayName|**Exchange Rate**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`exchangerate`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Disabled|
|MaxValue|100000000000|
|MinValue|1E-12|
|Precision|12|
|SourceTypeMask|0|

### <a name="BKMK_KbArticleTemplateIdTitle"></a> KbArticleTemplateIdTitle

|Property|Value|
|---|---|
|Description|**Title of the associated knowledge base article template.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`kbarticletemplateidtitle`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the knowledge base article.**|
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
|Description|**Date and time when the knowledge base article was last modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the kbarticle.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_Number"></a> Number

|Property|Value|
|---|---|
|Description|**Knowledge base article number.**|
|DisplayName|**Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`number`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization associated with the article.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Title of the knowledge base article.**|
|DisplayName|**Title**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [kb_article_template_kb_articles](#BKMK_kb_article_template_kb_articles)
- [lk_kbarticle_createdonbehalfby](#BKMK_lk_kbarticle_createdonbehalfby)
- [lk_kbarticle_modifiedonbehalfby](#BKMK_lk_kbarticle_modifiedonbehalfby)
- [lk_kbarticlebase_createdby](#BKMK_lk_kbarticlebase_createdby)
- [lk_kbarticlebase_modifiedby](#BKMK_lk_kbarticlebase_modifiedby)
- [organization_kb_articles](#BKMK_organization_kb_articles)
- [subject_kb_articles](#BKMK_subject_kb_articles)
- [TransactionCurrency_KbArticle](#BKMK_TransactionCurrency_KbArticle)

### <a name="BKMK_kb_article_template_kb_articles"></a> kb_article_template_kb_articles

One-To-Many Relationship: [kbarticletemplate kb_article_template_kb_articles](kbarticletemplate.md#BKMK_kb_article_template_kb_articles)

|Property|Value|
|---|---|
|ReferencedEntity|`kbarticletemplate`|
|ReferencedAttribute|`kbarticletemplateid`|
|ReferencingAttribute|`kbarticletemplateid`|
|ReferencingEntityNavigationPropertyName|`kbarticletemplateid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_kbarticle_createdonbehalfby"></a> lk_kbarticle_createdonbehalfby

One-To-Many Relationship: [systemuser lk_kbarticle_createdonbehalfby](systemuser.md#BKMK_lk_kbarticle_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_kbarticle_modifiedonbehalfby"></a> lk_kbarticle_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_kbarticle_modifiedonbehalfby](systemuser.md#BKMK_lk_kbarticle_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_kbarticlebase_createdby"></a> lk_kbarticlebase_createdby

One-To-Many Relationship: [systemuser lk_kbarticlebase_createdby](systemuser.md#BKMK_lk_kbarticlebase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_kbarticlebase_modifiedby"></a> lk_kbarticlebase_modifiedby

One-To-Many Relationship: [systemuser lk_kbarticlebase_modifiedby](systemuser.md#BKMK_lk_kbarticlebase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_kb_articles"></a> organization_kb_articles

One-To-Many Relationship: [organization organization_kb_articles](organization.md#BKMK_organization_kb_articles)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_subject_kb_articles"></a> subject_kb_articles

One-To-Many Relationship: [subject subject_kb_articles](subject.md#BKMK_subject_kb_articles)

|Property|Value|
|---|---|
|ReferencedEntity|`subject`|
|ReferencedAttribute|`subjectid`|
|ReferencingAttribute|`subjectid`|
|ReferencingEntityNavigationPropertyName|`subjectid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_KbArticle"></a> TransactionCurrency_KbArticle

One-To-Many Relationship: [transactioncurrency TransactionCurrency_KbArticle](transactioncurrency.md#BKMK_TransactionCurrency_KbArticle)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencingEntityNavigationPropertyName|`transactioncurrencyid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [KbArticle_Annotation](#BKMK_KbArticle_Annotation)
- [KbArticle_AsyncOperations](#BKMK_KbArticle_AsyncOperations)
- [KbArticle_BulkDeleteFailures](#BKMK_KbArticle_BulkDeleteFailures)
- [kbarticle_comments](#BKMK_kbarticle_comments)
- [KbArticle_DuplicateBaseRecord](#BKMK_KbArticle_DuplicateBaseRecord)
- [KbArticle_DuplicateMatchingRecord](#BKMK_KbArticle_DuplicateMatchingRecord)
- [kbarticle_principalobjectattributeaccess](#BKMK_kbarticle_principalobjectattributeaccess)
- [KbArticle_ProcessSessions](#BKMK_KbArticle_ProcessSessions)
- [KbArticle_SharepointDocumentLocation](#BKMK_KbArticle_SharepointDocumentLocation)
- [KbArticle_SyncErrors](#BKMK_KbArticle_SyncErrors)

### <a name="BKMK_KbArticle_Annotation"></a> KbArticle_Annotation

Many-To-One Relationship: [annotation KbArticle_Annotation](annotation.md#BKMK_KbArticle_Annotation)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`KbArticle_Annotation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KbArticle_AsyncOperations"></a> KbArticle_AsyncOperations

Many-To-One Relationship: [asyncoperation KbArticle_AsyncOperations](asyncoperation.md#BKMK_KbArticle_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KbArticle_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KbArticle_BulkDeleteFailures"></a> KbArticle_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure KbArticle_BulkDeleteFailures](bulkdeletefailure.md#BKMK_KbArticle_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KbArticle_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_kbarticle_comments"></a> kbarticle_comments

Many-To-One Relationship: [kbarticlecomment kbarticle_comments](kbarticlecomment.md#BKMK_kbarticle_comments)

|Property|Value|
|---|---|
|ReferencingEntity|`kbarticlecomment`|
|ReferencingAttribute|`kbarticleid`|
|ReferencedEntityNavigationPropertyName|`kbarticle_comments`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KbArticle_DuplicateBaseRecord"></a> KbArticle_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord KbArticle_DuplicateBaseRecord](duplicaterecord.md#BKMK_KbArticle_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`KbArticle_DuplicateBaseRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KbArticle_DuplicateMatchingRecord"></a> KbArticle_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord KbArticle_DuplicateMatchingRecord](duplicaterecord.md#BKMK_KbArticle_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`KbArticle_DuplicateMatchingRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_kbarticle_principalobjectattributeaccess"></a> kbarticle_principalobjectattributeaccess

Many-To-One Relationship: [principalobjectattributeaccess kbarticle_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_kbarticle_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`kbarticle_principalobjectattributeaccess`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KbArticle_ProcessSessions"></a> KbArticle_ProcessSessions

Many-To-One Relationship: [processsession KbArticle_ProcessSessions](processsession.md#BKMK_KbArticle_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KbArticle_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KbArticle_SharepointDocumentLocation"></a> KbArticle_SharepointDocumentLocation

Many-To-One Relationship: [sharepointdocumentlocation KbArticle_SharepointDocumentLocation](sharepointdocumentlocation.md#BKMK_KbArticle_SharepointDocumentLocation)

|Property|Value|
|---|---|
|ReferencingEntity|`sharepointdocumentlocation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KbArticle_SharepointDocumentLocation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KbArticle_SyncErrors"></a> KbArticle_SyncErrors

Many-To-One Relationship: [syncerror KbArticle_SyncErrors](syncerror.md#BKMK_KbArticle_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KbArticle_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

### <a name="BKMK_adx_kbarticle_kbarticle"></a> adx_kbarticle_kbarticle

This is a self-referencing many-to-many relationship.

|Property|Value|
|---|---|
|IntersectEntityName|`adx_kbarticle_kbarticle`|
|IsCustomizable|True|
|SchemaName|`adx_kbarticle_kbarticle`|
|Entity1IntersectAttribute|`kbarticleidone`|
|Entity2IntersectAttribute|`kbarticleidtwo`|
|Entity1NavigationPropertyName|`adx_kbarticle_kbarticle`|
|Entity2NavigationPropertyName|`adx_kbarticle_kbarticle`|
|Entity1AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseLabel`<br />Group: `Details`<br />Label: Related Articles<br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|
|Entity2AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.kbarticle?displayProperty=fullName>
