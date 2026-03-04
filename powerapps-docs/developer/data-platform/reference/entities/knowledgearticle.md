---
title: "Knowledge Article (KnowledgeArticle) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Knowledge Article (KnowledgeArticle) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Knowledge Article (KnowledgeArticle) table/entity reference (Microsoft Dataverse)

Organizational knowledge for internal and external use.

## Messages

The following table lists the messages for the Knowledge Article (KnowledgeArticle) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /knowledgearticles(*knowledgearticleid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /knowledgearticles<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateKnowledgeArticleTranslation`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateKnowledgeArticleTranslation?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.CreateKnowledgeArticleTranslationRequest>|
| `CreateKnowledgeArticleVersion`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateKnowledgeArticleVersion?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.CreateKnowledgeArticleVersionRequest>|
| `Delete`<br />Event: True |`DELETE` /knowledgearticles(*knowledgearticleid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `FullTextSearchKnowledgeArticle`<br />Event: False |<xref:Microsoft.Dynamics.CRM.FullTextSearchKnowledgeArticle?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.FullTextSearchKnowledgeArticleRequest>|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /knowledgearticles(*knowledgearticleid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /knowledgearticles<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /knowledgearticles(*knowledgearticleid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /knowledgearticles(*knowledgearticleid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /knowledgearticles(*knowledgearticleid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Knowledge Article (KnowledgeArticle) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Knowledge Article** |
| **DisplayCollectionName** | **Knowledge Articles** |
| **SchemaName** | `KnowledgeArticle` |
| **CollectionSchemaName** | `KnowledgeArticles` |
| **EntitySetName** | `knowledgearticles`|
| **LogicalName** | `knowledgearticle` |
| **LogicalCollectionName** | `knowledgearticles` |
| **PrimaryIdAttribute** | `knowledgearticleid` |
| **PrimaryNameAttribute** |`title` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ArticlePublicNumber](#BKMK_ArticlePublicNumber)
- [Content](#BKMK_Content)
- [Description](#BKMK_Description)
- [ExpirationDate](#BKMK_ExpirationDate)
- [ExpirationStateId](#BKMK_ExpirationStateId)
- [ExpirationStatusId](#BKMK_ExpirationStatusId)
- [ExpiredReviewOptions](#BKMK_ExpiredReviewOptions)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsInternal](#BKMK_IsInternal)
- [IsLatestVersion](#BKMK_IsLatestVersion)
- [IsPrimary](#BKMK_IsPrimary)
- [IsRootArticle](#BKMK_IsRootArticle)
- [Keywords](#BKMK_Keywords)
- [knowledgearticleId](#BKMK_knowledgearticleId)
- [LanguageLocaleId](#BKMK_LanguageLocaleId)
- [MajorVersionNumber](#BKMK_MajorVersionNumber)
- [MinorVersionNumber](#BKMK_MinorVersionNumber)
- [msdyn_agentreviewstatus](#BKMK_msdyn_agentreviewstatus)
- [msdyn_compliancestatecode](#BKMK_msdyn_compliancestatecode)
- [msdyn_creationmode](#BKMK_msdyn_creationmode)
- [msdyn_externalreferenceid](#BKMK_msdyn_externalreferenceid)
- [msdyn_harvestsourceentity](#BKMK_msdyn_harvestsourceentity)
- [msdyn_ingestedarticleurl](#BKMK_msdyn_ingestedarticleurl)
- [msdyn_integratedsearchproviderid](#BKMK_msdyn_integratedsearchproviderid)
- [msdyn_iscontentsyncedtostore](#BKMK_msdyn_iscontentsyncedtostore)
- [msdyn_isingestedarticle](#BKMK_msdyn_isingestedarticle)
- [msdyn_keywordsdescsuggestioncontrol](#BKMK_msdyn_keywordsdescsuggestioncontrol)
- [msdyn_languagecode](#BKMK_msdyn_languagecode)
- [msdyn_retrycountformigrationtocontentstore](#BKMK_msdyn_retrycountformigrationtocontentstore)
- [msdyn_sourceofcreation](#BKMK_msdyn_sourceofcreation)
- [msdyn_totalcasesimpacted](#BKMK_msdyn_totalcasesimpacted)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [ParentArticleContentId](#BKMK_ParentArticleContentId)
- [PreviousArticleContentId](#BKMK_PreviousArticleContentId)
- [primaryauthorid](#BKMK_primaryauthorid)
- [processid](#BKMK_processid)
- [PublishOn](#BKMK_PublishOn)
- [PublishStatusId](#BKMK_PublishStatusId)
- [ReadyForReview](#BKMK_ReadyForReview)
- [Review](#BKMK_Review)
- [RootArticleId](#BKMK_RootArticleId)
- [ScheduledStatusId](#BKMK_ScheduledStatusId)
- [SetCategoryAssociations](#BKMK_SetCategoryAssociations)
- [stageid](#BKMK_stageid)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [SubjectId](#BKMK_SubjectId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [Title](#BKMK_Title)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [traversedpath](#BKMK_traversedpath)
- [UpdateContent](#BKMK_UpdateContent)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_ArticlePublicNumber"></a> ArticlePublicNumber

|Property|Value|
|---|---|
|Description|**Shows the automatically generated ID exposed to customers, partners, and other external users to reference and look up articles.**|
|DisplayName|**Article Public Number**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`articlepublicnumber`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_Content"></a> Content

|Property|Value|
|---|---|
|Description|**Shows the body of the article stored in HTML format.**|
|DisplayName|**Content**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`content`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**A short overview of the article, primarily used in search results and for search engine optimization.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|String|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|155|

### <a name="BKMK_ExpirationDate"></a> ExpirationDate

|Property|Value|
|---|---|
|Description|**Enter an expiration date for the article. Leave this field blank for no expiration date.**|
|DisplayName|**Expiration Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`expirationdate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_ExpirationStateId"></a> ExpirationStateId

|Property|Value|
|---|---|
|Description|**Contains the id of the expiration state of the entity.**|
|DisplayName|**Expiration State Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`expirationstateid`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ExpirationStatusId"></a> ExpirationStatusId

|Property|Value|
|---|---|
|Description|**Contains the id of the expiration status of the entity.**|
|DisplayName|**Expired Status**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`expirationstatusid`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ExpiredReviewOptions"></a> ExpiredReviewOptions

|Property|Value|
|---|---|
|Description|**Expired Review Options**|
|DisplayName|**Expired Review Options**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`expiredreviewoptions`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`knowledgearticle_expiredreviewoptions`|

#### ExpiredReviewOptions Choices/Options

|Value|Label|
|---|---|
|0|**Needs Updating**|
|1|**Republish**|
|2|**Archive**|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Sequence number of the import that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_IsInternal"></a> IsInternal

|Property|Value|
|---|---|
|Description|**Shows whether this article is only visible internally.**|
|DisplayName|**Internal**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isinternal`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`knowledgearticle_isinternal`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsLatestVersion"></a> IsLatestVersion

|Property|Value|
|---|---|
|Description|**Shows which version of the knowledge article is the latest version.**|
|DisplayName|**Is Latest Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`islatestversion`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`knowledgearticle_islatestversion`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsPrimary"></a> IsPrimary

|Property|Value|
|---|---|
|Description|**Select whether the article is the primary article.**|
|DisplayName|**Primary Article**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isprimary`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`knowledgearticle_isprimary`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsRootArticle"></a> IsRootArticle

|Property|Value|
|---|---|
|Description|**Select whether the article is the root article.**|
|DisplayName|**Root Article**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isrootarticle`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`knowledgearticle_isrootarticle`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Keywords"></a> Keywords

|Property|Value|
|---|---|
|Description|**Type keywords to be used for searches in knowledge base articles. Separate keywords by using commas.**|
|DisplayName|**Keywords**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`keywords`|
|RequiredLevel|Recommended|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_knowledgearticleId"></a> knowledgearticleId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Knowledge Article**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`knowledgearticleid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_LanguageLocaleId"></a> LanguageLocaleId

|Property|Value|
|---|---|
|Description|**Select the language that the article's content is in.**|
|DisplayName|**Language**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`languagelocaleid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|languagelocale|

### <a name="BKMK_MajorVersionNumber"></a> MajorVersionNumber

|Property|Value|
|---|---|
|Description|**Shows the major version number of this article's content.**|
|DisplayName|**Major Version Number**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`majorversionnumber`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_MinorVersionNumber"></a> MinorVersionNumber

|Property|Value|
|---|---|
|Description|**Shows the minor version number of this article's content.**|
|DisplayName|**Minor Version Number**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`minorversionnumber`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_agentreviewstatus"></a> msdyn_agentreviewstatus

|Property|Value|
|---|---|
|Description|**field to indicate the representative review status of the article**|
|DisplayName|**Representative Review**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_agentreviewstatus`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|100000000|
|GlobalChoiceName|`msdyn_knowledgearticle_msdyn_agentreviewstatus`|

#### msdyn_agentreviewstatus Choices/Options

|Value|Label|
|---|---|
|100000000|**Not Reviewed**|
|100000001|**Reviewed**|

### <a name="BKMK_msdyn_compliancestatecode"></a> msdyn_compliancestatecode

|Property|Value|
|---|---|
|Description|**field to indicate the compliance state of an article**|
|DisplayName|**Compliance State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_compliancestatecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msdyn_knowledgearticle_msdyn_compliancestatecode`|

#### msdyn_compliancestatecode Choices/Options

|Value|Label|
|---|---|
|100000000|**Compliant**|
|100000001|**Non Compliant**|
|100000002|**Pending**|

### <a name="BKMK_msdyn_creationmode"></a> msdyn_creationmode

|Property|Value|
|---|---|
|Description|**Opiton set to hold details about article if it is generated by AI or manually created**|
|DisplayName|**Creation Mode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_creationmode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`msdyn_knowledgearticle_msdyn_creationmode`|

#### msdyn_creationmode Choices/Options

|Value|Label|
|---|---|
|0|**Manual**|
|1|**Copilot**|

### <a name="BKMK_msdyn_externalreferenceid"></a> msdyn_externalreferenceid

|Property|Value|
|---|---|
|Description|**External Reference Id**|
|DisplayName|**External Reference Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_externalreferenceid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|450|

### <a name="BKMK_msdyn_harvestsourceentity"></a> msdyn_harvestsourceentity

|Property|Value|
|---|---|
|Description||
|DisplayName|**Knowledge Harvest Source Entity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_harvestsourceentity`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_ingestedarticleurl"></a> msdyn_ingestedarticleurl

|Property|Value|
|---|---|
|Description|**Ingested article URL**|
|DisplayName|**Ingested Article URL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_ingestedarticleurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2048|

### <a name="BKMK_msdyn_integratedsearchproviderid"></a> msdyn_integratedsearchproviderid

|Property|Value|
|---|---|
|Description|**Integrated Search Dataprovider Id**|
|DisplayName|**Integrated Search Dataprovider Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_integratedsearchproviderid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msdyn_integratedsearchprovider|

### <a name="BKMK_msdyn_iscontentsyncedtostore"></a> msdyn_iscontentsyncedtostore

|Property|Value|
|---|---|
|Description|**Sets whether the article content is synced to file storage**|
|DisplayName|**Is content synced to file storage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_iscontentsyncedtostore`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_knowledgearticle_msdyn_iscontentsyncedtostore`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_isingestedarticle"></a> msdyn_isingestedarticle

|Property|Value|
|---|---|
|Description|**Value is true for all Ingested articles**|
|DisplayName|**Is Ingested Article**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isingestedarticle`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_knowledgearticle_msdyn_isingestedarticle`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_keywordsdescsuggestioncontrol"></a> msdyn_keywordsdescsuggestioncontrol

|Property|Value|
|---|---|
|Description||
|DisplayName|**Keywords and Description Suggestion control**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_keywordsdescsuggestioncontrol`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_knowledgearticle_msdyn_keywordsdescsuggestioncontrol`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_languagecode"></a> msdyn_languagecode

|Property|Value|
|---|---|
|Description|**The Language Code that the article's content is in.**|
|DisplayName|**Language Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_languagecode`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_retrycountformigrationtocontentstore"></a> msdyn_retrycountformigrationtocontentstore

|Property|Value|
|---|---|
|Description|**Displays the number of times migration to file storage retry is attempted for an article**|
|DisplayName|**File storage migration retry count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_retrycountformigrationtocontentstore`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_sourceofcreation"></a> msdyn_sourceofcreation

|Property|Value|
|---|---|
|Description|**Option set to hold details about article origin, if it is generated from Real Time Harvesting/ Bulk Harvesting/ knowledge draft assist/ Manual**|
|DisplayName|**Source of Creation**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_sourceofcreation`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`msdyn_knowledgearticle_msdyn_sourceofcreation`|

#### msdyn_sourceofcreation Choices/Options

|Value|Label|
|---|---|
|0|**Manual**|
|1|**DraftAssist**|
|2|**RealTimeHarvest**|
|3|**BulkHarvest**|
|4|**RealTimeHarvest-Conversation**|

### <a name="BKMK_msdyn_totalcasesimpacted"></a> msdyn_totalcasesimpacted

|Property|Value|
|---|---|
|Description||
|DisplayName|**Total Cases Impacted**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_totalcasesimpacted`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

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

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user or team who owns the record.**|
|DisplayName|**Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description|**Owner Id Type**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_ParentArticleContentId"></a> ParentArticleContentId

|Property|Value|
|---|---|
|Description|**Contains the id of the parent article content associated with the entity.**|
|DisplayName|**Parent Article Content Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentarticlecontentid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|knowledgearticle|

### <a name="BKMK_PreviousArticleContentId"></a> PreviousArticleContentId

|Property|Value|
|---|---|
|Description|**Shows the version that the current article was restored from.**|
|DisplayName|**Previous Article Content ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`previousarticlecontentid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|knowledgearticle|

### <a name="BKMK_primaryauthorid"></a> primaryauthorid

|Property|Value|
|---|---|
|Description|**Contains the id of the primary author associated with the article.**|
|DisplayName|**Primary Author Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`primaryauthorid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_processid"></a> processid

|Property|Value|
|---|---|
|Description|**Contains the id of the process associated with the entity.**|
|DisplayName|**Process Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_PublishOn"></a> PublishOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was published.**|
|DisplayName|**Publish On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`publishon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_PublishStatusId"></a> PublishStatusId

|Property|Value|
|---|---|
|Description|**Publish Status of the Article.**|
|DisplayName|**Published Status**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`publishstatusid`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_ReadyForReview"></a> ReadyForReview

|Property|Value|
|---|---|
|Description|**Ready For Review**|
|DisplayName|**Ready For Review**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`readyforreview`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`knowledgearticle_readyforreview`|
|DefaultValue|False|
|True Label|Completed|
|False Label|Mark Complete|

### <a name="BKMK_Review"></a> Review

|Property|Value|
|---|---|
|Description|**Review**|
|DisplayName|**Review**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`review`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`knowledgearticle_review`|

#### Review Choices/Options

|Value|Label|
|---|---|
|0|**Approved**|
|1|**Rejected**|

### <a name="BKMK_RootArticleId"></a> RootArticleId

|Property|Value|
|---|---|
|Description|**Contains the id of the root article.**|
|DisplayName|**Root Article Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`rootarticleid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|knowledgearticle|

### <a name="BKMK_ScheduledStatusId"></a> ScheduledStatusId

|Property|Value|
|---|---|
|Description|**Contains the id of the scheduled status of the entity.**|
|DisplayName|**Scheduled Status**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`scheduledstatusid`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_SetCategoryAssociations"></a> SetCategoryAssociations

|Property|Value|
|---|---|
|Description|**Shows whether category associations have been set**|
|DisplayName|**Set Category Associations**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`setcategoryassociations`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`knowledgearticle_setcategoryassociations`|
|DefaultValue|False|
|True Label|Completed|
|False Label|Mark as Complete|

### <a name="BKMK_stageid"></a> stageid

|Property|Value|
|---|---|
|Description|**Contains the id of the stage where the entity is located.**|
|DisplayName|**Stage Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`stageid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Shows whether the article is a draft or is published, archived, or discarded. Draft articles aren't available externally and can be edited. Published articles are available externally, based on applicable permissions, but can't be edited. All metadata changes are reflected in the published version. Archived and discarded articles aren't available externally and can't be edited.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`knowledgearticle_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Draft**<br />DefaultStatus: 1<br />InvariantName: `Draft`|
|1|Label: **Approved**<br />DefaultStatus: 5<br />InvariantName: `Approved`|
|2|Label: **Scheduled**<br />DefaultStatus: 6<br />InvariantName: `Scheduled`|
|3|Label: **Published**<br />DefaultStatus: 7<br />InvariantName: `Published`|
|4|Label: **Expired**<br />DefaultStatus: 10<br />InvariantName: `Expired`|
|5|Label: **Archived**<br />DefaultStatus: 12<br />InvariantName: `Archived`|
|6|Label: **Discarded**<br />DefaultStatus: 13<br />InvariantName: `Discarded`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Select the article's status.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`knowledgearticle_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Proposed**<br />State:0<br />TransitionData: None|
|2|Label: **Draft**<br />State:0<br />TransitionData: None|
|3|Label: **Needs review**<br />State:0<br />TransitionData: None|
|4|Label: **In review**<br />State:0<br />TransitionData: None|
|5|Label: **Approved**<br />State:1<br />TransitionData: None|
|6|Label: **Scheduled**<br />State:2<br />TransitionData: None|
|7|Label: **Published**<br />State:3<br />TransitionData: None|
|8|Label: **Needs review**<br />State:3<br />TransitionData: None|
|9|Label: **Updating**<br />State:3<br />TransitionData: None|
|10|Label: **Expired**<br />State:4<br />TransitionData: None|
|11|Label: **Rejected**<br />State:4<br />TransitionData: None|
|12|Label: **Archived**<br />State:5<br />TransitionData: None|
|13|Label: **Discarded**<br />State:6<br />TransitionData: None|
|14|Label: **Rejected**<br />State:6<br />TransitionData: None|

### <a name="BKMK_SubjectId"></a> SubjectId

|Property|Value|
|---|---|
|Description|**Choose the subject of the article to assist with article searches. You can configure subjects under Business Management in the Settings area.**|
|DisplayName|**Subject**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`subjectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|subject|

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
|Description|**Type a title for the article.**|
|DisplayName|**Title**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`title`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Exchange rate for the currency associated with the KnowledgeArticle with respect to the base currency.**|
|DisplayName|**Currency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`transactioncurrencyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|transactioncurrency|

### <a name="BKMK_traversedpath"></a> traversedpath

|Property|Value|
|---|---|
|Description|**A comma separated list of string values representing the unique identifiers of stages in a Business Process Flow Instance in the order that they occur.**|
|DisplayName|**(Deprecated) Traversed Path**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`traversedpath`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1250|

### <a name="BKMK_UpdateContent"></a> UpdateContent

|Property|Value|
|---|---|
|Description|**Update Content**|
|DisplayName|**Update Content**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`updatecontent`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`knowledgearticle_updatecontent`|
|DefaultValue|False|
|True Label|Content Updated|
|False Label|Mark When Completed|

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

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ExchangeRate](#BKMK_ExchangeRate)
- [KnowledgeArticleViews](#BKMK_KnowledgeArticleViews)
- [KnowledgeArticleViews_Date](#BKMK_KnowledgeArticleViews_Date)
- [KnowledgeArticleViews_State](#BKMK_KnowledgeArticleViews_State)
- [LanguageLocaleIdLocaleId](#BKMK_LanguageLocaleIdLocaleId)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [msdyn_contentstore](#BKMK_msdyn_contentstore)
- [msdyn_contentstore_Name](#BKMK_msdyn_contentstore_Name)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [Rating](#BKMK_Rating)
- [Rating_Count](#BKMK_Rating_Count)
- [Rating_Date](#BKMK_Rating_Date)
- [Rating_State](#BKMK_Rating_State)
- [Rating_Sum](#BKMK_Rating_Sum)
- [SubjectIdDsc](#BKMK_SubjectIdDsc)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was created.**|
|DisplayName|**Created On**|
|IsValidForForm|True|
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
|Description|**Unique identifier of the delegate user who created the record.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|---|---|
|Description|**Exchange rate for the currency associated with the KnowledgeArticle with respect to the base currency.**|
|DisplayName|**ExchangeRate**|
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

### <a name="BKMK_KnowledgeArticleViews"></a> KnowledgeArticleViews

|Property|Value|
|---|---|
|Description|**Shows the total number of article views.**|
|DisplayName|**Knowledge Article Views**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`knowledgearticleviews`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_KnowledgeArticleViews_Date"></a> KnowledgeArticleViews_Date

|Property|Value|
|---|---|
|Description|**The date time for Knowledge Article View.**|
|DisplayName|**Knowledge Article View(Last Updated Time)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`knowledgearticleviews_date`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_KnowledgeArticleViews_State"></a> KnowledgeArticleViews_State

|Property|Value|
|---|---|
|Description|**State of Knowledge Article View.**|
|DisplayName|**Knowledge Article View(State)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`knowledgearticleviews_state`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_LanguageLocaleIdLocaleId"></a> LanguageLocaleIdLocaleId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`languagelocaleidlocaleid`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|1|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who modified the record.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
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
|Description|**Unique identifier of the delegate user who modified the record.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_msdyn_contentstore"></a> msdyn_contentstore

|Property|Value|
|---|---|
|Description|**Stores the reference to content in file store**|
|DisplayName|**File storage content reference**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_contentstore`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_contentstore_Name"></a> msdyn_contentstore_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_contentstore_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description|**Name of the owner**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|---|---|
|Description|**Yomi name of the owner**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridyominame`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Unique identifier for the business unit that owns the record**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|---|---|
|Description|**Unique identifier for the team that owns the record.**|
|DisplayName|**Owning Team**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningteam`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|team|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier for the user that owns the record.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_Rating"></a> Rating

|Property|Value|
|---|---|
|Description|**Information which specifies how helpful the related record was.**|
|DisplayName|**Rating**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`rating`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Auto|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|2|
|SourceTypeMask|0|

### <a name="BKMK_Rating_Count"></a> Rating_Count

|Property|Value|
|---|---|
|Description|**Rating Count**|
|DisplayName|**Rating(Count)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`rating_count`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_Rating_Date"></a> Rating_Date

|Property|Value|
|---|---|
|Description|**The date time for Rating.**|
|DisplayName|**Rating(Last Updated Time)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`rating_date`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_Rating_State"></a> Rating_State

|Property|Value|
|---|---|
|Description|**State of Rating**|
|DisplayName|**Rating(State)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`rating_state`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_Rating_Sum"></a> Rating_Sum

|Property|Value|
|---|---|
|Description|**Total sum of Rating**|
|DisplayName|**Rating(sum)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`rating_sum`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Disabled|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|
|SourceTypeMask|0|

### <a name="BKMK_SubjectIdDsc"></a> SubjectIdDsc

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`subjectiddsc`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

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

- [business_unit_knowledgearticle](#BKMK_business_unit_knowledgearticle)
- [FileAttachment_KnowledgeArticle_msdyn_contentstore](#BKMK_FileAttachment_KnowledgeArticle_msdyn_contentstore)
- [knowledgearticle_languagelocaleid](#BKMK_knowledgearticle_languagelocaleid)
- [knowledgearticle_parentarticle_contentid](#BKMK_knowledgearticle_parentarticle_contentid-many-to-one)
- [knowledgearticle_previousarticle_contentid](#BKMK_knowledgearticle_previousarticle_contentid-many-to-one)
- [knowledgearticle_primaryauthorid](#BKMK_knowledgearticle_primaryauthorid)
- [knowledgearticle_rootarticle_id](#BKMK_knowledgearticle_rootarticle_id-many-to-one)
- [lk_knowledgearticle_createdby](#BKMK_lk_knowledgearticle_createdby)
- [lk_knowledgearticle_createdonbehalfby](#BKMK_lk_knowledgearticle_createdonbehalfby)
- [lk_knowledgearticle_modifiedby](#BKMK_lk_knowledgearticle_modifiedby)
- [lk_knowledgearticle_modifiedonbehalfby](#BKMK_lk_knowledgearticle_modifiedonbehalfby)
- [msdyn_knowledgearticle_integratedsearchprovider](#BKMK_msdyn_knowledgearticle_integratedsearchprovider)
- [owner_knowledgearticle](#BKMK_owner_knowledgearticle)
- [processstage_knowledgearticle](#BKMK_processstage_knowledgearticle)
- [subject_knowledgearticles](#BKMK_subject_knowledgearticles)
- [team_knowledgearticle](#BKMK_team_knowledgearticle)
- [TransactionCurrency_knowledgearticle](#BKMK_TransactionCurrency_knowledgearticle)
- [user_knowledgearticle](#BKMK_user_knowledgearticle)

### <a name="BKMK_business_unit_knowledgearticle"></a> business_unit_knowledgearticle

One-To-Many Relationship: [businessunit business_unit_knowledgearticle](businessunit.md#BKMK_business_unit_knowledgearticle)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_KnowledgeArticle_msdyn_contentstore"></a> FileAttachment_KnowledgeArticle_msdyn_contentstore

One-To-Many Relationship: [fileattachment FileAttachment_KnowledgeArticle_msdyn_contentstore](fileattachment.md#BKMK_FileAttachment_KnowledgeArticle_msdyn_contentstore)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_contentstore`|
|ReferencingEntityNavigationPropertyName|`msdyn_contentstore`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgearticle_languagelocaleid"></a> knowledgearticle_languagelocaleid

One-To-Many Relationship: [languagelocale knowledgearticle_languagelocaleid](languagelocale.md#BKMK_knowledgearticle_languagelocaleid)

|Property|Value|
|---|---|
|ReferencedEntity|`languagelocale`|
|ReferencedAttribute|`languagelocaleid`|
|ReferencingAttribute|`languagelocaleid`|
|ReferencingEntityNavigationPropertyName|`languagelocaleid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgearticle_parentarticle_contentid-many-to-one"></a> knowledgearticle_parentarticle_contentid

One-To-Many Relationship: [knowledgearticle knowledgearticle_parentarticle_contentid](#BKMK_knowledgearticle_parentarticle_contentid-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`parentarticlecontentid`|
|ReferencingEntityNavigationPropertyName|`ParentArticleContentId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgearticle_previousarticle_contentid-many-to-one"></a> knowledgearticle_previousarticle_contentid

One-To-Many Relationship: [knowledgearticle knowledgearticle_previousarticle_contentid](#BKMK_knowledgearticle_previousarticle_contentid-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`previousarticlecontentid`|
|ReferencingEntityNavigationPropertyName|`PreviousArticleContentId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgearticle_primaryauthorid"></a> knowledgearticle_primaryauthorid

One-To-Many Relationship: [systemuser knowledgearticle_primaryauthorid](systemuser.md#BKMK_knowledgearticle_primaryauthorid)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`primaryauthorid`|
|ReferencingEntityNavigationPropertyName|`primaryauthorid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgearticle_rootarticle_id-many-to-one"></a> knowledgearticle_rootarticle_id

One-To-Many Relationship: [knowledgearticle knowledgearticle_rootarticle_id](#BKMK_knowledgearticle_rootarticle_id-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`rootarticleid`|
|ReferencingEntityNavigationPropertyName|`RootArticleId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_knowledgearticle_createdby"></a> lk_knowledgearticle_createdby

One-To-Many Relationship: [systemuser lk_knowledgearticle_createdby](systemuser.md#BKMK_lk_knowledgearticle_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_knowledgearticle_createdonbehalfby"></a> lk_knowledgearticle_createdonbehalfby

One-To-Many Relationship: [systemuser lk_knowledgearticle_createdonbehalfby](systemuser.md#BKMK_lk_knowledgearticle_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_knowledgearticle_modifiedby"></a> lk_knowledgearticle_modifiedby

One-To-Many Relationship: [systemuser lk_knowledgearticle_modifiedby](systemuser.md#BKMK_lk_knowledgearticle_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_knowledgearticle_modifiedonbehalfby"></a> lk_knowledgearticle_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_knowledgearticle_modifiedonbehalfby](systemuser.md#BKMK_lk_knowledgearticle_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgearticle_integratedsearchprovider"></a> msdyn_knowledgearticle_integratedsearchprovider

One-To-Many Relationship: [msdyn_integratedsearchprovider msdyn_knowledgearticle_integratedsearchprovider](msdyn_integratedsearchprovider.md#BKMK_msdyn_knowledgearticle_integratedsearchprovider)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_integratedsearchprovider`|
|ReferencedAttribute|`msdyn_integratedsearchproviderid`|
|ReferencingAttribute|`msdyn_integratedsearchproviderid`|
|ReferencingEntityNavigationPropertyName|`msdyn_integratedsearchproviderid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_knowledgearticle"></a> owner_knowledgearticle

One-To-Many Relationship: [owner owner_knowledgearticle](owner.md#BKMK_owner_knowledgearticle)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_processstage_knowledgearticle"></a> processstage_knowledgearticle

One-To-Many Relationship: [processstage processstage_knowledgearticle](processstage.md#BKMK_processstage_knowledgearticle)

|Property|Value|
|---|---|
|ReferencedEntity|`processstage`|
|ReferencedAttribute|`processstageid`|
|ReferencingAttribute|`stageid`|
|ReferencingEntityNavigationPropertyName|`stageid_processstage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_subject_knowledgearticles"></a> subject_knowledgearticles

One-To-Many Relationship: [subject subject_knowledgearticles](subject.md#BKMK_subject_knowledgearticles)

|Property|Value|
|---|---|
|ReferencedEntity|`subject`|
|ReferencedAttribute|`subjectid`|
|ReferencingAttribute|`subjectid`|
|ReferencingEntityNavigationPropertyName|`subjectid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_knowledgearticle"></a> team_knowledgearticle

One-To-Many Relationship: [team team_knowledgearticle](team.md#BKMK_team_knowledgearticle)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_knowledgearticle"></a> TransactionCurrency_knowledgearticle

One-To-Many Relationship: [transactioncurrency TransactionCurrency_knowledgearticle](transactioncurrency.md#BKMK_TransactionCurrency_knowledgearticle)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencingEntityNavigationPropertyName|`transactioncurrencyid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_knowledgearticle"></a> user_knowledgearticle

One-To-Many Relationship: [systemuser user_knowledgearticle](systemuser.md#BKMK_user_knowledgearticle)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [knowledgearticle_activity_parties](#BKMK_knowledgearticle_activity_parties)
- [KnowledgeArticle_ActivityPointers](#BKMK_KnowledgeArticle_ActivityPointers)
- [knowledgearticle_adx_inviteredemptions](#BKMK_knowledgearticle_adx_inviteredemptions)
- [knowledgearticle_adx_portalcomments](#BKMK_knowledgearticle_adx_portalcomments)
- [knowledgearticle_Annotations](#BKMK_knowledgearticle_Annotations)
- [KnowledgeArticle_Appointments](#BKMK_KnowledgeArticle_Appointments)
- [knowledgearticle_AsyncOperations](#BKMK_knowledgearticle_AsyncOperations)
- [knowledgearticle_BulkDeleteFailures](#BKMK_knowledgearticle_BulkDeleteFailures)
- [knowledgearticle_chats](#BKMK_knowledgearticle_chats)
- [knowledgearticle_connections1](#BKMK_knowledgearticle_connections1)
- [knowledgearticle_connections2](#BKMK_knowledgearticle_connections2)
- [knowledgearticle_DuplicateBaseRecord](#BKMK_knowledgearticle_DuplicateBaseRecord)
- [knowledgearticle_DuplicateMatchingRecord](#BKMK_knowledgearticle_DuplicateMatchingRecord)
- [KnowledgeArticle_Emails](#BKMK_KnowledgeArticle_Emails)
- [KnowledgeArticle_Faxes](#BKMK_KnowledgeArticle_Faxes)
- [KnowledgeArticle_Feedback](#BKMK_KnowledgeArticle_Feedback)
- [knowledgearticle_FileAttachments](#BKMK_knowledgearticle_FileAttachments)
- [KnowledgeArticle_Letters](#BKMK_KnowledgeArticle_Letters)
- [knowledgearticle_parentarticle_contentid](#BKMK_knowledgearticle_parentarticle_contentid-one-to-many)
- [KnowledgeArticle_Phonecalls](#BKMK_KnowledgeArticle_Phonecalls)
- [knowledgearticle_PostFollows](#BKMK_knowledgearticle_PostFollows)
- [knowledgearticle_PostRegardings](#BKMK_knowledgearticle_PostRegardings)
- [knowledgearticle_previousarticle_contentid](#BKMK_knowledgearticle_previousarticle_contentid-one-to-many)
- [knowledgearticle_PrincipalObjectAttributeAccess](#BKMK_knowledgearticle_PrincipalObjectAttributeAccess)
- [knowledgearticle_ProcessSession](#BKMK_knowledgearticle_ProcessSession)
- [knowledgearticle_QueueItems](#BKMK_knowledgearticle_QueueItems)
- [KnowledgeArticle_RecurringAppointmentMasters](#BKMK_KnowledgeArticle_RecurringAppointmentMasters)
- [knowledgearticle_rootarticle_id](#BKMK_knowledgearticle_rootarticle_id-one-to-many)
- [knowledgearticle_SharePointDocumentLocations](#BKMK_knowledgearticle_SharePointDocumentLocations)
- [KnowledgeArticle_SocialActivities](#BKMK_KnowledgeArticle_SocialActivities)
- [KnowledgeArticle_SyncErrors](#BKMK_KnowledgeArticle_SyncErrors)
- [KnowledgeArticle_Tasks](#BKMK_KnowledgeArticle_Tasks)
- [knowledgearticle_Teams](#BKMK_knowledgearticle_Teams)
- [knowledgearticle_views](#BKMK_knowledgearticle_views)
- [lk_expiredprocess_knowledgearticleid](#BKMK_lk_expiredprocess_knowledgearticleid)
- [lk_newprocess_knowledgearticleid](#BKMK_lk_newprocess_knowledgearticleid)
- [lk_translationprocess_knowledgearticleid](#BKMK_lk_translationprocess_knowledgearticleid)
- [msdyn_knowledgearticle_favoriteknowledgearticle](#BKMK_msdyn_knowledgearticle_favoriteknowledgearticle)
- [msdyn_knowledgearticle_feedback_context](#BKMK_msdyn_knowledgearticle_feedback_context)
- [msdyn_knowledgearticleimage_parentknowledgearticleid](#BKMK_msdyn_knowledgearticleimage_parentknowledgearticleid)

### <a name="BKMK_knowledgearticle_activity_parties"></a> knowledgearticle_activity_parties

Many-To-One Relationship: [activityparty knowledgearticle_activity_parties](activityparty.md#BKMK_knowledgearticle_activity_parties)

|Property|Value|
|---|---|
|ReferencingEntity|`activityparty`|
|ReferencingAttribute|`partyid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_activity_parties`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeArticle_ActivityPointers"></a> KnowledgeArticle_ActivityPointers

Many-To-One Relationship: [activitypointer KnowledgeArticle_ActivityPointers](activitypointer.md#BKMK_KnowledgeArticle_ActivityPointers)

|Property|Value|
|---|---|
|ReferencingEntity|`activitypointer`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeArticle_ActivityPointers`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10<br />QueryApi: `CRMActivity.RetrieveByObject`<br />ViewId: `00000000-0000-0000-00aa-000010001903`|

### <a name="BKMK_knowledgearticle_adx_inviteredemptions"></a> knowledgearticle_adx_inviteredemptions

Many-To-One Relationship: [adx_inviteredemption knowledgearticle_adx_inviteredemptions](adx_inviteredemption.md#BKMK_knowledgearticle_adx_inviteredemptions)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_inviteredemption`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_adx_inviteredemptions`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: `CRMActivity.RetrieveByObject`<br />ViewId: `00000000-0000-0000-00aa-000010001903`|

### <a name="BKMK_knowledgearticle_adx_portalcomments"></a> knowledgearticle_adx_portalcomments

Many-To-One Relationship: [adx_portalcomment knowledgearticle_adx_portalcomments](adx_portalcomment.md#BKMK_knowledgearticle_adx_portalcomments)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_portalcomment`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_adx_portalcomments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: `CRMActivity.RetrieveByObject`<br />ViewId: `00000000-0000-0000-00aa-000010001903`|

### <a name="BKMK_knowledgearticle_Annotations"></a> knowledgearticle_Annotations

Many-To-One Relationship: [annotation knowledgearticle_Annotations](annotation.md#BKMK_knowledgearticle_Annotations)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_Annotations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeArticle_Appointments"></a> KnowledgeArticle_Appointments

Many-To-One Relationship: [appointment KnowledgeArticle_Appointments](appointment.md#BKMK_KnowledgeArticle_Appointments)

|Property|Value|
|---|---|
|ReferencingEntity|`appointment`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeArticle_Appointments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_knowledgearticle_AsyncOperations"></a> knowledgearticle_AsyncOperations

Many-To-One Relationship: [asyncoperation knowledgearticle_AsyncOperations](asyncoperation.md#BKMK_knowledgearticle_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_knowledgearticle_BulkDeleteFailures"></a> knowledgearticle_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure knowledgearticle_BulkDeleteFailures](bulkdeletefailure.md#BKMK_knowledgearticle_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_knowledgearticle_chats"></a> knowledgearticle_chats

Many-To-One Relationship: [chat knowledgearticle_chats](chat.md#BKMK_knowledgearticle_chats)

|Property|Value|
|---|---|
|ReferencingEntity|`chat`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_chats`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: `CRMActivity.RetrieveByObject`<br />ViewId: `00000000-0000-0000-00aa-000010001903`|

### <a name="BKMK_knowledgearticle_connections1"></a> knowledgearticle_connections1

Many-To-One Relationship: [connection knowledgearticle_connections1](connection.md#BKMK_knowledgearticle_connections1)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record1id`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_connections1`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_knowledgearticle_connections2"></a> knowledgearticle_connections2

Many-To-One Relationship: [connection knowledgearticle_connections2](connection.md#BKMK_knowledgearticle_connections2)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record2id`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_connections2`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_knowledgearticle_DuplicateBaseRecord"></a> knowledgearticle_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord knowledgearticle_DuplicateBaseRecord](duplicaterecord.md#BKMK_knowledgearticle_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_knowledgearticle_DuplicateMatchingRecord"></a> knowledgearticle_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord knowledgearticle_DuplicateMatchingRecord](duplicaterecord.md#BKMK_knowledgearticle_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeArticle_Emails"></a> KnowledgeArticle_Emails

Many-To-One Relationship: [email KnowledgeArticle_Emails](email.md#BKMK_KnowledgeArticle_Emails)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeArticle_Emails`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeArticle_Faxes"></a> KnowledgeArticle_Faxes

Many-To-One Relationship: [fax KnowledgeArticle_Faxes](fax.md#BKMK_KnowledgeArticle_Faxes)

|Property|Value|
|---|---|
|ReferencingEntity|`fax`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeArticle_Faxes`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeArticle_Feedback"></a> KnowledgeArticle_Feedback

Many-To-One Relationship: [feedback KnowledgeArticle_Feedback](feedback.md#BKMK_KnowledgeArticle_Feedback)

|Property|Value|
|---|---|
|ReferencingEntity|`feedback`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeArticle_Feedback`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 150<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_knowledgearticle_FileAttachments"></a> knowledgearticle_FileAttachments

Many-To-One Relationship: [fileattachment knowledgearticle_FileAttachments](fileattachment.md#BKMK_knowledgearticle_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeArticle_Letters"></a> KnowledgeArticle_Letters

Many-To-One Relationship: [letter KnowledgeArticle_Letters](letter.md#BKMK_KnowledgeArticle_Letters)

|Property|Value|
|---|---|
|ReferencingEntity|`letter`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeArticle_Letters`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_knowledgearticle_parentarticle_contentid-one-to-many"></a> knowledgearticle_parentarticle_contentid

Many-To-One Relationship: [knowledgearticle knowledgearticle_parentarticle_contentid](#BKMK_knowledgearticle_parentarticle_contentid-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`knowledgearticle`|
|ReferencingAttribute|`parentarticlecontentid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_parentarticle_contentid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeArticle_Phonecalls"></a> KnowledgeArticle_Phonecalls

Many-To-One Relationship: [phonecall KnowledgeArticle_Phonecalls](phonecall.md#BKMK_KnowledgeArticle_Phonecalls)

|Property|Value|
|---|---|
|ReferencingEntity|`phonecall`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeArticle_Phonecalls`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_knowledgearticle_PostFollows"></a> knowledgearticle_PostFollows

Many-To-One Relationship: [postfollow knowledgearticle_PostFollows](postfollow.md#BKMK_knowledgearticle_PostFollows)

|Property|Value|
|---|---|
|ReferencingEntity|`postfollow`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_PostFollows`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_knowledgearticle_PostRegardings"></a> knowledgearticle_PostRegardings

Many-To-One Relationship: [postregarding knowledgearticle_PostRegardings](postregarding.md#BKMK_knowledgearticle_PostRegardings)

|Property|Value|
|---|---|
|ReferencingEntity|`postregarding`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_PostRegardings`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_knowledgearticle_previousarticle_contentid-one-to-many"></a> knowledgearticle_previousarticle_contentid

Many-To-One Relationship: [knowledgearticle knowledgearticle_previousarticle_contentid](#BKMK_knowledgearticle_previousarticle_contentid-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`knowledgearticle`|
|ReferencingAttribute|`previousarticlecontentid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_previousarticle_contentid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_knowledgearticle_PrincipalObjectAttributeAccess"></a> knowledgearticle_PrincipalObjectAttributeAccess

Many-To-One Relationship: [principalobjectattributeaccess knowledgearticle_PrincipalObjectAttributeAccess](principalobjectattributeaccess.md#BKMK_knowledgearticle_PrincipalObjectAttributeAccess)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_PrincipalObjectAttributeAccess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_knowledgearticle_ProcessSession"></a> knowledgearticle_ProcessSession

Many-To-One Relationship: [processsession knowledgearticle_ProcessSession](processsession.md#BKMK_knowledgearticle_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_knowledgearticle_QueueItems"></a> knowledgearticle_QueueItems

Many-To-One Relationship: [queueitem knowledgearticle_QueueItems](queueitem.md#BKMK_knowledgearticle_QueueItems)

|Property|Value|
|---|---|
|ReferencingEntity|`queueitem`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_QueueItems`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeArticle_RecurringAppointmentMasters"></a> KnowledgeArticle_RecurringAppointmentMasters

Many-To-One Relationship: [recurringappointmentmaster KnowledgeArticle_RecurringAppointmentMasters](recurringappointmentmaster.md#BKMK_KnowledgeArticle_RecurringAppointmentMasters)

|Property|Value|
|---|---|
|ReferencingEntity|`recurringappointmentmaster`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeArticle_RecurringAppointmentMasters`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_knowledgearticle_rootarticle_id-one-to-many"></a> knowledgearticle_rootarticle_id

Many-To-One Relationship: [knowledgearticle knowledgearticle_rootarticle_id](#BKMK_knowledgearticle_rootarticle_id-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`knowledgearticle`|
|ReferencingAttribute|`rootarticleid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_rootarticle_id`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_knowledgearticle_SharePointDocumentLocations"></a> knowledgearticle_SharePointDocumentLocations

Many-To-One Relationship: [sharepointdocumentlocation knowledgearticle_SharePointDocumentLocations](sharepointdocumentlocation.md#BKMK_knowledgearticle_SharePointDocumentLocations)

|Property|Value|
|---|---|
|ReferencingEntity|`sharepointdocumentlocation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_SharePointDocumentLocations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeArticle_SocialActivities"></a> KnowledgeArticle_SocialActivities

Many-To-One Relationship: [socialactivity KnowledgeArticle_SocialActivities](socialactivity.md#BKMK_KnowledgeArticle_SocialActivities)

|Property|Value|
|---|---|
|ReferencingEntity|`socialactivity`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeArticle_SocialActivities`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeArticle_SyncErrors"></a> KnowledgeArticle_SyncErrors

Many-To-One Relationship: [syncerror KnowledgeArticle_SyncErrors](syncerror.md#BKMK_KnowledgeArticle_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeArticle_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeArticle_Tasks"></a> KnowledgeArticle_Tasks

Many-To-One Relationship: [task KnowledgeArticle_Tasks](task.md#BKMK_KnowledgeArticle_Tasks)

|Property|Value|
|---|---|
|ReferencingEntity|`task`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeArticle_Tasks`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_knowledgearticle_Teams"></a> knowledgearticle_Teams

Many-To-One Relationship: [team knowledgearticle_Teams](team.md#BKMK_knowledgearticle_Teams)

|Property|Value|
|---|---|
|ReferencingEntity|`team`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_Teams`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_knowledgearticle_views"></a> knowledgearticle_views

Many-To-One Relationship: [knowledgearticleviews knowledgearticle_views](knowledgearticleviews.md#BKMK_knowledgearticle_views)

|Property|Value|
|---|---|
|ReferencingEntity|`knowledgearticleviews`|
|ReferencingAttribute|`knowledgearticleid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_views`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10<br />QueryApi: null<br />ViewId: `23173e88-b4cf-4cfa-93e4-9fc1320a7b01`|

### <a name="BKMK_lk_expiredprocess_knowledgearticleid"></a> lk_expiredprocess_knowledgearticleid

Many-To-One Relationship: [expiredprocess lk_expiredprocess_knowledgearticleid](expiredprocess.md#BKMK_lk_expiredprocess_knowledgearticleid)

|Property|Value|
|---|---|
|ReferencingEntity|`expiredprocess`|
|ReferencingAttribute|`knowledgearticleid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_expiredprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_newprocess_knowledgearticleid"></a> lk_newprocess_knowledgearticleid

Many-To-One Relationship: [newprocess lk_newprocess_knowledgearticleid](newprocess.md#BKMK_lk_newprocess_knowledgearticleid)

|Property|Value|
|---|---|
|ReferencingEntity|`newprocess`|
|ReferencingAttribute|`knowledgearticleid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_newprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_translationprocess_knowledgearticleid"></a> lk_translationprocess_knowledgearticleid

Many-To-One Relationship: [translationprocess lk_translationprocess_knowledgearticleid](translationprocess.md#BKMK_lk_translationprocess_knowledgearticleid)

|Property|Value|
|---|---|
|ReferencingEntity|`translationprocess`|
|ReferencingAttribute|`knowledgearticleid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_translationprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgearticle_favoriteknowledgearticle"></a> msdyn_knowledgearticle_favoriteknowledgearticle

Many-To-One Relationship: [msdyn_favoriteknowledgearticle msdyn_knowledgearticle_favoriteknowledgearticle](msdyn_favoriteknowledgearticle.md#BKMK_msdyn_knowledgearticle_favoriteknowledgearticle)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_favoriteknowledgearticle`|
|ReferencingAttribute|`msdyn_knowledgearticleid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticle_favoriteknowledgearticle`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: Id of Knowledge Article<br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgearticle_feedback_context"></a> msdyn_knowledgearticle_feedback_context

Many-To-One Relationship: [feedback msdyn_knowledgearticle_feedback_context](feedback.md#BKMK_msdyn_knowledgearticle_feedback_context)

|Property|Value|
|---|---|
|ReferencingEntity|`feedback`|
|ReferencingAttribute|`msdyn_contextobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticle_feedback_context`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgearticleimage_parentknowledgearticleid"></a> msdyn_knowledgearticleimage_parentknowledgearticleid

Many-To-One Relationship: [msdyn_knowledgearticleimage msdyn_knowledgearticleimage_parentknowledgearticleid](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_parentknowledgearticleid)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgearticleimage`|
|ReferencingAttribute|`msdyn_parentknowledgearticleid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticleimage_parentknowledgearticleid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

- [knowledgearticle_category](#BKMK_knowledgearticle_category)
- [msdyn_msdyn_kbattachment_knowledgearticle](#BKMK_msdyn_msdyn_kbattachment_knowledgearticle)

### <a name="BKMK_knowledgearticle_category"></a> knowledgearticle_category

See [category knowledgearticle_category Many-To-Many Relationship](category.md#BKMK_knowledgearticle_category)

|Property|Value|
|---|---|
|IntersectEntityName|`knowledgearticlescategories`|
|IsCustomizable|False|
|SchemaName|`knowledgearticle_category`|
|IntersectAttribute|`knowledgearticleid`|
|NavigationPropertyName|`knowledgearticle_category`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_msdyn_kbattachment_knowledgearticle"></a> msdyn_msdyn_kbattachment_knowledgearticle

See [msdyn_kbattachment msdyn_msdyn_kbattachment_knowledgearticle Many-To-Many Relationship](msdyn_kbattachment.md#BKMK_msdyn_msdyn_kbattachment_knowledgearticle)

|Property|Value|
|---|---|
|IntersectEntityName|`msdyn_msdyn_kbattachment_knowledgearticle`|
|IsCustomizable|True|
|SchemaName|`msdyn_msdyn_kbattachment_knowledgearticle`|
|IntersectAttribute|`knowledgearticleid`|
|NavigationPropertyName|`msdyn_msdyn_kbattachment_knowledgearticle`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.knowledgearticle?displayProperty=fullName>
