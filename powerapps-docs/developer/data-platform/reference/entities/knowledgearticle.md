---
title: "KnowledgeArticle table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the KnowledgeArticle table/entity."
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

# KnowledgeArticle table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Organizational knowledge for internal and external use.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/knowledgearticles(*knowledgearticleid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/knowledgearticles<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateKnowledgeArticleTranslation|<xref href="Microsoft.Dynamics.CRM.CreateKnowledgeArticleTranslation?text=CreateKnowledgeArticleTranslation Action" />|<xref:Microsoft.Crm.Sdk.Messages.CreateKnowledgeArticleTranslationRequest>|
|CreateKnowledgeArticleVersion|<xref href="Microsoft.Dynamics.CRM.CreateKnowledgeArticleVersion?text=CreateKnowledgeArticleVersion Action" />|<xref:Microsoft.Crm.Sdk.Messages.CreateKnowledgeArticleVersionRequest>|
|Delete|DELETE [*org URI*]/api/data/v9.0/knowledgearticles(*knowledgearticleid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|FullTextSearchKnowledgeArticle|<xref href="Microsoft.Dynamics.CRM.FullTextSearchKnowledgeArticle?text=FullTextSearchKnowledgeArticle Action" />|<xref:Microsoft.Crm.Sdk.Messages.FullTextSearchKnowledgeArticleRequest>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/knowledgearticles(*knowledgearticleid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/knowledgearticles<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/knowledgearticles(*knowledgearticleid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/knowledgearticles(*knowledgearticleid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|KnowledgeArticles|
|DisplayCollectionName|Knowledge Articles|
|DisplayName|Knowledge Article|
|EntitySetName|knowledgearticles|
|IsBPFEntity|False|
|LogicalCollectionName|knowledgearticles|
|LogicalName|knowledgearticle|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|knowledgearticleid|
|PrimaryNameAttribute|title|
|SchemaName|KnowledgeArticle|

<a name="writable-attributes"></a>

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
- [msdyn_ingestedarticleurl](#BKMK_msdyn_ingestedarticleurl)
- [msdyn_isingestedarticle](#BKMK_msdyn_isingestedarticle)
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
|--------|-----|
|Description|Shows the automatically generated ID exposed to customers, partners, and other external users to reference and look up articles.|
|DisplayName|Article Public Number|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|articlepublicnumber|
|MaxLength|4000|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_Content"></a> Content

|Property|Value|
|--------|-----|
|Description|Shows the body of the article stored in HTML format.|
|DisplayName|Content|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|content|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|A short overview of the article, primarily used in search results and for search engine optimization.|
|DisplayName|Description|
|FormatName|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|155|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ExpirationDate"></a> ExpirationDate

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Enter an expiration date for the article. Leave this field blank for no expiration date.|
|DisplayName|Expiration Date|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|expirationdate|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ExpirationStateId"></a> ExpirationStateId

|Property|Value|
|--------|-----|
|Description|Contains the id of the expiration state of the entity.|
|DisplayName|Expiration State Id|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|expirationstateid|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ExpirationStatusId"></a> ExpirationStatusId

|Property|Value|
|--------|-----|
|Description|Contains the id of the expiration status of the entity.|
|DisplayName|Expired Status|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|expirationstatusid|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ExpiredReviewOptions"></a> ExpiredReviewOptions

|Property|Value|
|--------|-----|
|Description|Expired Review Options|
|DisplayName|Expired Review Options|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|expiredreviewoptions|
|RequiredLevel|None|
|Type|Picklist|

#### ExpiredReviewOptions Choices/Options

|Value|Label|
|-----|-----|
|0|Needs Updating|
|1|Republish|
|2|Archive|



### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|Sequence number of the import that created this record.|
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


### <a name="BKMK_IsInternal"></a> IsInternal

|Property|Value|
|--------|-----|
|Description|Shows whether this article is only visible internally.|
|DisplayName|Internal|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isinternal|
|RequiredLevel|None|
|Type|Boolean|

#### IsInternal Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsLatestVersion"></a> IsLatestVersion

|Property|Value|
|--------|-----|
|Description|Shows which version of the knowledge article is the latest version.|
|DisplayName|Is Latest Version|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|islatestversion|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsLatestVersion Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsPrimary"></a> IsPrimary

|Property|Value|
|--------|-----|
|Description|Select whether the article is the primary article.|
|DisplayName|Primary Article|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isprimary|
|RequiredLevel|None|
|Type|Boolean|

#### IsPrimary Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsRootArticle"></a> IsRootArticle

|Property|Value|
|--------|-----|
|Description|Select whether the article is the root article.|
|DisplayName|Root Article|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|isrootarticle|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsRootArticle Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_Keywords"></a> Keywords

|Property|Value|
|--------|-----|
|Description|Type keywords to be used for searches in knowledge base articles. Separate keywords by using commas.|
|DisplayName|Keywords|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|keywords|
|MaxLength|4000|
|RequiredLevel|Recommended|
|Type|Memo|


### <a name="BKMK_knowledgearticleId"></a> knowledgearticleId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Knowledge Article|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|knowledgearticleid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_LanguageLocaleId"></a> LanguageLocaleId

|Property|Value|
|--------|-----|
|Description|Select the language that the article's content is in.|
|DisplayName|Language|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|languagelocaleid|
|RequiredLevel|SystemRequired|
|Targets|languagelocale|
|Type|Lookup|


### <a name="BKMK_MajorVersionNumber"></a> MajorVersionNumber

|Property|Value|
|--------|-----|
|Description|Shows the major version number of this article's content.|
|DisplayName|Major Version Number|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|majorversionnumber|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_MinorVersionNumber"></a> MinorVersionNumber

|Property|Value|
|--------|-----|
|Description|Shows the minor version number of this article's content.|
|DisplayName|Minor Version Number|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|minorversionnumber|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_msdyn_ingestedarticleurl"></a> msdyn_ingestedarticleurl

**Added by**: Knowledge Management Patch Solution

|Property|Value|
|--------|-----|
|Description|Ingested article URL|
|DisplayName|Ingested Article URL|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_ingestedarticleurl|
|MaxLength|2048|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_isingestedarticle"></a> msdyn_isingestedarticle

**Added by**: Knowledge Management Patch Solution

|Property|Value|
|--------|-----|
|Description|Value is true for all Ingested articles|
|DisplayName|Is Ingested Article|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isingestedarticle|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_isingestedarticle Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



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


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user or team who owns the record.|
|DisplayName|Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Targets|systemuser,team|
|Type|Owner|


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|--------|-----|
|Description|Owner Id Type|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_ParentArticleContentId"></a> ParentArticleContentId

|Property|Value|
|--------|-----|
|Description|Contains the id of the parent article content associated with the entity.|
|DisplayName|Parent Article Content Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|parentarticlecontentid|
|RequiredLevel|None|
|Targets|knowledgearticle|
|Type|Lookup|


### <a name="BKMK_PreviousArticleContentId"></a> PreviousArticleContentId

|Property|Value|
|--------|-----|
|Description|Shows the version that the current article was restored from.|
|DisplayName|Previous Article Content ID|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|previousarticlecontentid|
|RequiredLevel|None|
|Targets|knowledgearticle|
|Type|Lookup|


### <a name="BKMK_primaryauthorid"></a> primaryauthorid

|Property|Value|
|--------|-----|
|Description|Contains the id of the primary author associated with the article.|
|DisplayName|Primary Author Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|primaryauthorid|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_processid"></a> processid

|Property|Value|
|--------|-----|
|Description|Contains the id of the process associated with the entity.|
|DisplayName|Process Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|processid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_PublishOn"></a> PublishOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was published.|
|DisplayName|Publish On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|publishon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_PublishStatusId"></a> PublishStatusId

|Property|Value|
|--------|-----|
|Description|Publish Status of the Article.|
|DisplayName|Published Status|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|publishstatusid|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ReadyForReview"></a> ReadyForReview

|Property|Value|
|--------|-----|
|Description|Ready For Review|
|DisplayName|Ready For Review|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|readyforreview|
|RequiredLevel|None|
|Type|Boolean|

#### ReadyForReview Choices/Options

|Value|Label|
|-----|-----|
|1|Completed|
|0|Mark Complete|

**DefaultValue**: False



### <a name="BKMK_Review"></a> Review

|Property|Value|
|--------|-----|
|Description|Review|
|DisplayName|Review|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|review|
|RequiredLevel|None|
|Type|Picklist|

#### Review Choices/Options

|Value|Label|
|-----|-----|
|0|Approved|
|1|Rejected|



### <a name="BKMK_RootArticleId"></a> RootArticleId

|Property|Value|
|--------|-----|
|Description|Contains the id of the root article.|
|DisplayName|Root Article Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|rootarticleid|
|RequiredLevel|None|
|Targets|knowledgearticle|
|Type|Lookup|


### <a name="BKMK_ScheduledStatusId"></a> ScheduledStatusId

|Property|Value|
|--------|-----|
|Description|Contains the id of the scheduled status of the entity.|
|DisplayName|Scheduled Status|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|scheduledstatusid|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_SetCategoryAssociations"></a> SetCategoryAssociations

|Property|Value|
|--------|-----|
|Description|Shows whether category associations have been set|
|DisplayName|Set Category Associations|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|setcategoryassociations|
|RequiredLevel|None|
|Type|Boolean|

#### SetCategoryAssociations Choices/Options

|Value|Label|
|-----|-----|
|1|Completed|
|0|Mark as Complete|

**DefaultValue**: False



### <a name="BKMK_stageid"></a> stageid

|Property|Value|
|--------|-----|
|Description|Contains the id of the stage where the entity is located.|
|DisplayName|Stage Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|stageid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|--------|-----|
|Description|Shows whether the article is a draft or is published, archived, or discarded. Draft articles aren't available externally and can be edited. Published articles are available externally, based on applicable permissions, but can't be edited. All metadata changes are reflected in the published version. Archived and discarded articles aren't available externally and can't be edited.|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### StateCode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Draft|1|Draft|
|1|Approved|5|Approved|
|2|Scheduled|6|Scheduled|
|3|Published|7|Published|
|4|Expired|10|Expired|
|5|Archived|12|Archived|
|6|Discarded|13|Discarded|



### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|--------|-----|
|Description|Select the article's status.|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### StatusCode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Proposed|0|
|2|Draft|0|
|3|Needs review|0|
|4|In review|0|
|5|Approved|1|
|6|Scheduled|2|
|7|Published|3|
|8|Needs review|3|
|9|Updating|3|
|10|Expired|4|
|11|Rejected|4|
|12|Archived|5|
|13|Discarded|6|
|14|Rejected|6|



### <a name="BKMK_SubjectId"></a> SubjectId

|Property|Value|
|--------|-----|
|Description|Choose the subject of the article to assist with article searches. You can configure subjects under Business Management in the Settings area.|
|DisplayName|Subject|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|subjectid|
|RequiredLevel|None|
|Targets|subject|
|Type|Lookup|


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
|Description|Type a title for the article.|
|DisplayName|Title|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|title|
|MaxLength|4000|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|--------|-----|
|Description|Exchange rate for the currency associated with the KnowledgeArticle with respect to the base currency.|
|DisplayName|Currency|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|transactioncurrencyid|
|RequiredLevel|None|
|Targets|transactioncurrency|
|Type|Lookup|


### <a name="BKMK_traversedpath"></a> traversedpath

|Property|Value|
|--------|-----|
|Description|A comma separated list of string values representing the unique identifiers of stages in a Business Process Flow Instance in the order that they occur.|
|DisplayName|(Deprecated) Traversed Path|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|traversedpath|
|MaxLength|1250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_UpdateContent"></a> UpdateContent

|Property|Value|
|--------|-----|
|Description|Update Content|
|DisplayName|Update Content|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|updatecontent|
|RequiredLevel|None|
|Type|Boolean|

#### UpdateContent Choices/Options

|Value|Label|
|-----|-----|
|1|Content Updated|
|0|Mark When Completed|

**DefaultValue**: False



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

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ExchangeRate](#BKMK_ExchangeRate)
- [KnowledgeArticleViews](#BKMK_KnowledgeArticleViews)
- [KnowledgeArticleViews_Date](#BKMK_KnowledgeArticleViews_Date)
- [KnowledgeArticleViews_State](#BKMK_KnowledgeArticleViews_State)
- [LanguageLocaleIdLocaleId](#BKMK_LanguageLocaleIdLocaleId)
- [LanguageLocaleIdName](#BKMK_LanguageLocaleIdName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [ParentArticleContentIdName](#BKMK_ParentArticleContentIdName)
- [PreviousArticleContentIdName](#BKMK_PreviousArticleContentIdName)
- [primaryauthoridName](#BKMK_primaryauthoridName)
- [Rating](#BKMK_Rating)
- [Rating_Count](#BKMK_Rating_Count)
- [Rating_Date](#BKMK_Rating_Date)
- [Rating_State](#BKMK_Rating_State)
- [Rating_Sum](#BKMK_Rating_Sum)
- [RootArticleIdName](#BKMK_RootArticleIdName)
- [SubjectIdDsc](#BKMK_SubjectIdDsc)
- [SubjectIdName](#BKMK_SubjectIdName)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the record.|
|DisplayName|Created By|
|IsValidForForm|True|
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
|Description|Date and time when the record was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the record.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
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


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|--------|-----|
|Description|Exchange rate for the currency associated with the KnowledgeArticle with respect to the base currency.|
|DisplayName|ExchangeRate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.0000000001|
|Precision|10|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_KnowledgeArticleViews"></a> KnowledgeArticleViews

|Property|Value|
|--------|-----|
|Description|Shows the total number of article views.|
|DisplayName|Knowledge Article Views|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|knowledgearticleviews|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_KnowledgeArticleViews_Date"></a> KnowledgeArticleViews_Date

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|The date time for Knowledge Article View.|
|DisplayName|Knowledge Article View(Last Updated Time)|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|knowledgearticleviews_date|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_KnowledgeArticleViews_State"></a> KnowledgeArticleViews_State

|Property|Value|
|--------|-----|
|Description|State of Knowledge Article View.|
|DisplayName|Knowledge Article View(State)|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|knowledgearticleviews_state|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_LanguageLocaleIdLocaleId"></a> LanguageLocaleIdLocaleId

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|languagelocaleidlocaleid|
|MaxValue|2147483647|
|MinValue|1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_LanguageLocaleIdName"></a> LanguageLocaleIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|languagelocaleidname|
|MaxLength|500|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who modified the record.|
|DisplayName|Modified By|
|IsValidForForm|True|
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
|Description|Date and time when the record was modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the record.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
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


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|--------|-----|
|Description|Name of the owner|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|--------|-----|
|Description|Yomi name of the owner|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|--------|-----|
|Description|Unique identifier for the business unit that owns the record|
|DisplayName|Owning Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|--------|-----|
|Description|Unique identifier for the team that owns the record.|
|DisplayName|Owning Team|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteam|
|RequiredLevel|None|
|Targets|team|
|Type|Lookup|


### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|--------|-----|
|Description|Unique identifier for the user that owns the record.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ParentArticleContentIdName"></a> ParentArticleContentIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentarticlecontentidname|
|MaxLength|500|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PreviousArticleContentIdName"></a> PreviousArticleContentIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|previousarticlecontentidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_primaryauthoridName"></a> primaryauthoridName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|primaryauthoridname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Rating"></a> Rating

|Property|Value|
|--------|-----|
|Description|Information which specifies how helpful the related record was.|
|DisplayName|Rating|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|rating|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|2|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_Rating_Count"></a> Rating_Count

|Property|Value|
|--------|-----|
|Description|Rating Count|
|DisplayName|Rating(Count)|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|rating_count|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_Rating_Date"></a> Rating_Date

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|The date time for Rating.|
|DisplayName|Rating(Last Updated Time)|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|rating_date|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_Rating_State"></a> Rating_State

|Property|Value|
|--------|-----|
|Description|State of Rating|
|DisplayName|Rating(State)|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|rating_state|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_Rating_Sum"></a> Rating_Sum

|Property|Value|
|--------|-----|
|Description|Total sum of Rating|
|DisplayName|Rating(sum)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|rating_sum|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_RootArticleIdName"></a> RootArticleIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|rootarticleidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SubjectIdDsc"></a> SubjectIdDsc

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|subjectiddsc|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_SubjectIdName"></a> SubjectIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|subjectidname|
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

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [knowledgearticle_connections1](#BKMK_knowledgearticle_connections1)
- [knowledgearticle_connections2](#BKMK_knowledgearticle_connections2)
- [knowledgearticle_DuplicateMatchingRecord](#BKMK_knowledgearticle_DuplicateMatchingRecord)
- [knowledgearticle_DuplicateBaseRecord](#BKMK_knowledgearticle_DuplicateBaseRecord)
- [knowledgearticle_SharePointDocumentLocations](#BKMK_knowledgearticle_SharePointDocumentLocations)
- [knowledgearticle_QueueItems](#BKMK_knowledgearticle_QueueItems)
- [knowledgearticle_Annotations](#BKMK_knowledgearticle_Annotations)
- [knowledgearticle_Teams](#BKMK_knowledgearticle_Teams)
- [knowledgearticle_AsyncOperations](#BKMK_knowledgearticle_AsyncOperations)
- [knowledgearticle_ProcessSession](#BKMK_knowledgearticle_ProcessSession)
- [knowledgearticle_BulkDeleteFailures](#BKMK_knowledgearticle_BulkDeleteFailures)
- [knowledgearticle_PrincipalObjectAttributeAccess](#BKMK_knowledgearticle_PrincipalObjectAttributeAccess)
- [KnowledgeArticle_SocialActivities](#BKMK_KnowledgeArticle_SocialActivities)
- [KnowledgeArticle_Letters](#BKMK_KnowledgeArticle_Letters)
- [KnowledgeArticle_Tasks](#BKMK_KnowledgeArticle_Tasks)
- [knowledgearticle_views](#BKMK_knowledgearticle_views)
- [KnowledgeArticle_Faxes](#BKMK_KnowledgeArticle_Faxes)
- [lk_expiredprocess_knowledgearticleid](#BKMK_lk_expiredprocess_knowledgearticleid)
- [KnowledgeArticle_Appointments](#BKMK_KnowledgeArticle_Appointments)
- [lk_newprocess_knowledgearticleid](#BKMK_lk_newprocess_knowledgearticleid)
- [knowledgearticle_rootarticle_id](#BKMK_knowledgearticle_rootarticle_id)
- [lk_translationprocess_knowledgearticleid](#BKMK_lk_translationprocess_knowledgearticleid)
- [KnowledgeArticle_RecurringAppointmentMasters](#BKMK_KnowledgeArticle_RecurringAppointmentMasters)
- [KnowledgeArticle_ActivityPointers](#BKMK_KnowledgeArticle_ActivityPointers)
- [KnowledgeArticle_SyncErrors](#BKMK_KnowledgeArticle_SyncErrors)
- [KnowledgeArticle_Feedback](#BKMK_KnowledgeArticle_Feedback)
- [knowledgearticle_previousarticle_contentid](#BKMK_knowledgearticle_previousarticle_contentid)
- [knowledgearticle_PostFollows](#BKMK_knowledgearticle_PostFollows)
- [knowledgearticle_activity_parties](#BKMK_knowledgearticle_activity_parties)
- [knowledgearticle_parentarticle_contentid](#BKMK_knowledgearticle_parentarticle_contentid)
- [KnowledgeArticle_Phonecalls](#BKMK_KnowledgeArticle_Phonecalls)
- [KnowledgeArticle_Emails](#BKMK_KnowledgeArticle_Emails)
- [msdyn_knowledgearticle_feedback_context](#BKMK_msdyn_knowledgearticle_feedback_context)


### <a name="BKMK_knowledgearticle_connections1"></a> knowledgearticle_connections1

Same as connection table [knowledgearticle_connections1](connection.md#BKMK_knowledgearticle_connections1) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record1id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|knowledgearticle_connections1|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_knowledgearticle_connections2"></a> knowledgearticle_connections2

Same as connection table [knowledgearticle_connections2](connection.md#BKMK_knowledgearticle_connections2) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record2id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|knowledgearticle_connections2|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_knowledgearticle_DuplicateMatchingRecord"></a> knowledgearticle_DuplicateMatchingRecord

Same as duplicaterecord table [knowledgearticle_DuplicateMatchingRecord](duplicaterecord.md#BKMK_knowledgearticle_DuplicateMatchingRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|knowledgearticle_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_knowledgearticle_DuplicateBaseRecord"></a> knowledgearticle_DuplicateBaseRecord

Same as duplicaterecord table [knowledgearticle_DuplicateBaseRecord](duplicaterecord.md#BKMK_knowledgearticle_DuplicateBaseRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|knowledgearticle_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_knowledgearticle_SharePointDocumentLocations"></a> knowledgearticle_SharePointDocumentLocations

Same as sharepointdocumentlocation table [knowledgearticle_SharePointDocumentLocations](sharepointdocumentlocation.md#BKMK_knowledgearticle_SharePointDocumentLocations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointdocumentlocation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|knowledgearticle_SharePointDocumentLocations|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_knowledgearticle_QueueItems"></a> knowledgearticle_QueueItems

Same as queueitem table [knowledgearticle_QueueItems](queueitem.md#BKMK_knowledgearticle_QueueItems) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|queueitem|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|knowledgearticle_QueueItems|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_knowledgearticle_Annotations"></a> knowledgearticle_Annotations

Same as annotation table [knowledgearticle_Annotations](annotation.md#BKMK_knowledgearticle_Annotations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|knowledgearticle_Annotations|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_knowledgearticle_Teams"></a> knowledgearticle_Teams

Same as team table [knowledgearticle_Teams](team.md#BKMK_knowledgearticle_Teams) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|team|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|knowledgearticle_Teams|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_knowledgearticle_AsyncOperations"></a> knowledgearticle_AsyncOperations

Same as asyncoperation table [knowledgearticle_AsyncOperations](asyncoperation.md#BKMK_knowledgearticle_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|knowledgearticle_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_knowledgearticle_ProcessSession"></a> knowledgearticle_ProcessSession

Same as processsession table [knowledgearticle_ProcessSession](processsession.md#BKMK_knowledgearticle_ProcessSession) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|knowledgearticle_ProcessSession|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_knowledgearticle_BulkDeleteFailures"></a> knowledgearticle_BulkDeleteFailures

Same as bulkdeletefailure table [knowledgearticle_BulkDeleteFailures](bulkdeletefailure.md#BKMK_knowledgearticle_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|knowledgearticle_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_knowledgearticle_PrincipalObjectAttributeAccess"></a> knowledgearticle_PrincipalObjectAttributeAccess

Same as principalobjectattributeaccess table [knowledgearticle_PrincipalObjectAttributeAccess](principalobjectattributeaccess.md#BKMK_knowledgearticle_PrincipalObjectAttributeAccess) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|knowledgearticle_PrincipalObjectAttributeAccess|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeArticle_SocialActivities"></a> KnowledgeArticle_SocialActivities

Same as socialactivity table [KnowledgeArticle_SocialActivities](socialactivity.md#BKMK_KnowledgeArticle_SocialActivities) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeArticle_SocialActivities|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_KnowledgeArticle_Letters"></a> KnowledgeArticle_Letters

Same as letter table [KnowledgeArticle_Letters](letter.md#BKMK_KnowledgeArticle_Letters) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|letter|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeArticle_Letters|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_KnowledgeArticle_Tasks"></a> KnowledgeArticle_Tasks

Same as task table [KnowledgeArticle_Tasks](task.md#BKMK_KnowledgeArticle_Tasks) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|task|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeArticle_Tasks|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_knowledgearticle_views"></a> knowledgearticle_views

Same as knowledgearticleviews table [knowledgearticle_views](knowledgearticleviews.md#BKMK_knowledgearticle_views) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgearticleviews|
|ReferencingAttribute|knowledgearticleid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|knowledgearticle_views|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeArticle_Faxes"></a> KnowledgeArticle_Faxes

Same as fax table [KnowledgeArticle_Faxes](fax.md#BKMK_KnowledgeArticle_Faxes) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fax|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeArticle_Faxes|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_lk_expiredprocess_knowledgearticleid"></a> lk_expiredprocess_knowledgearticleid

Same as expiredprocess table [lk_expiredprocess_knowledgearticleid](expiredprocess.md#BKMK_lk_expiredprocess_knowledgearticleid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|expiredprocess|
|ReferencingAttribute|knowledgearticleid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|knowledgearticle_expiredprocess|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeArticle_Appointments"></a> KnowledgeArticle_Appointments

Same as appointment table [KnowledgeArticle_Appointments](appointment.md#BKMK_KnowledgeArticle_Appointments) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appointment|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeArticle_Appointments|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_lk_newprocess_knowledgearticleid"></a> lk_newprocess_knowledgearticleid

Same as newprocess table [lk_newprocess_knowledgearticleid](newprocess.md#BKMK_lk_newprocess_knowledgearticleid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|newprocess|
|ReferencingAttribute|knowledgearticleid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|knowledgearticle_newprocess|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_knowledgearticle_rootarticle_id"></a> knowledgearticle_rootarticle_id

Same as knowledgearticle table [knowledgearticle_rootarticle_id](knowledgearticle.md#BKMK_knowledgearticle_rootarticle_id) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgearticle|
|ReferencingAttribute|rootarticleid|
|IsHierarchical|True|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|knowledgearticle_rootarticle_id|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_translationprocess_knowledgearticleid"></a> lk_translationprocess_knowledgearticleid

Same as translationprocess table [lk_translationprocess_knowledgearticleid](translationprocess.md#BKMK_lk_translationprocess_knowledgearticleid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|translationprocess|
|ReferencingAttribute|knowledgearticleid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|knowledgearticle_translationprocess|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeArticle_RecurringAppointmentMasters"></a> KnowledgeArticle_RecurringAppointmentMasters

Same as recurringappointmentmaster table [KnowledgeArticle_RecurringAppointmentMasters](recurringappointmentmaster.md#BKMK_KnowledgeArticle_RecurringAppointmentMasters) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurringappointmentmaster|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeArticle_RecurringAppointmentMasters|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_KnowledgeArticle_ActivityPointers"></a> KnowledgeArticle_ActivityPointers

Same as activitypointer table [KnowledgeArticle_ActivityPointers](activitypointer.md#BKMK_KnowledgeArticle_ActivityPointers) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitypointer|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|KnowledgeArticle_ActivityPointers|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeArticle_SyncErrors"></a> KnowledgeArticle_SyncErrors

Same as syncerror table [KnowledgeArticle_SyncErrors](syncerror.md#BKMK_KnowledgeArticle_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeArticle_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_KnowledgeArticle_Feedback"></a> KnowledgeArticle_Feedback

Same as feedback table [KnowledgeArticle_Feedback](feedback.md#BKMK_KnowledgeArticle_Feedback) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|feedback|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeArticle_Feedback|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 150|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_knowledgearticle_previousarticle_contentid"></a> knowledgearticle_previousarticle_contentid

Same as knowledgearticle table [knowledgearticle_previousarticle_contentid](knowledgearticle.md#BKMK_knowledgearticle_previousarticle_contentid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgearticle|
|ReferencingAttribute|previousarticlecontentid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|knowledgearticle_previousarticle_contentid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_knowledgearticle_PostFollows"></a> knowledgearticle_PostFollows

Same as postfollow table [knowledgearticle_PostFollows](postfollow.md#BKMK_knowledgearticle_PostFollows) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|postfollow|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|knowledgearticle_PostFollows|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_knowledgearticle_activity_parties"></a> knowledgearticle_activity_parties

Same as activityparty table [knowledgearticle_activity_parties](activityparty.md#BKMK_knowledgearticle_activity_parties) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activityparty|
|ReferencingAttribute|partyid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|knowledgearticle_activity_parties|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_knowledgearticle_parentarticle_contentid"></a> knowledgearticle_parentarticle_contentid

Same as knowledgearticle table [knowledgearticle_parentarticle_contentid](knowledgearticle.md#BKMK_knowledgearticle_parentarticle_contentid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgearticle|
|ReferencingAttribute|parentarticlecontentid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|knowledgearticle_parentarticle_contentid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeArticle_Phonecalls"></a> KnowledgeArticle_Phonecalls

Same as phonecall table [KnowledgeArticle_Phonecalls](phonecall.md#BKMK_KnowledgeArticle_Phonecalls) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|phonecall|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeArticle_Phonecalls|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_KnowledgeArticle_Emails"></a> KnowledgeArticle_Emails

Same as email table [KnowledgeArticle_Emails](email.md#BKMK_KnowledgeArticle_Emails) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeArticle_Emails|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_msdyn_knowledgearticle_feedback_context"></a> msdyn_knowledgearticle_feedback_context

**Added by**: Knowledge Management Patch Solution

Same as feedback table [msdyn_knowledgearticle_feedback_context](feedback.md#BKMK_msdyn_knowledgearticle_feedback_context) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|feedback|
|ReferencingAttribute|msdyn_contextobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgearticle_feedback_context|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_knowledgearticle_createdby](#BKMK_lk_knowledgearticle_createdby)
- [lk_knowledgearticle_createdonbehalfby](#BKMK_lk_knowledgearticle_createdonbehalfby)
- [lk_knowledgearticle_modifiedby](#BKMK_lk_knowledgearticle_modifiedby)
- [lk_knowledgearticle_modifiedonbehalfby](#BKMK_lk_knowledgearticle_modifiedonbehalfby)
- [user_knowledgearticle](#BKMK_user_knowledgearticle)
- [team_knowledgearticle](#BKMK_team_knowledgearticle)
- [business_unit_knowledgearticle](#BKMK_business_unit_knowledgearticle)
- [processstage_knowledgearticle](#BKMK_processstage_knowledgearticle)
- [knowledgearticle_languagelocaleid](#BKMK_knowledgearticle_languagelocaleid)
- [knowledgearticle_primaryauthorid](#BKMK_knowledgearticle_primaryauthorid)
- [knowledgearticle_parentarticle_contentid](#BKMK_knowledgearticle_parentarticle_contentid)
- [knowledgearticle_previousarticle_contentid](#BKMK_knowledgearticle_previousarticle_contentid)
- [subject_knowledgearticles](#BKMK_subject_knowledgearticles)
- [knowledgearticle_rootarticle_id](#BKMK_knowledgearticle_rootarticle_id)
- [TransactionCurrency_knowledgearticle](#BKMK_TransactionCurrency_knowledgearticle)


### <a name="BKMK_lk_knowledgearticle_createdby"></a> lk_knowledgearticle_createdby

See systemuser Table [lk_knowledgearticle_createdby](systemuser.md#BKMK_lk_knowledgearticle_createdby) One-To-Many relationship.

### <a name="BKMK_lk_knowledgearticle_createdonbehalfby"></a> lk_knowledgearticle_createdonbehalfby

See systemuser Table [lk_knowledgearticle_createdonbehalfby](systemuser.md#BKMK_lk_knowledgearticle_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_knowledgearticle_modifiedby"></a> lk_knowledgearticle_modifiedby

See systemuser Table [lk_knowledgearticle_modifiedby](systemuser.md#BKMK_lk_knowledgearticle_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_knowledgearticle_modifiedonbehalfby"></a> lk_knowledgearticle_modifiedonbehalfby

See systemuser Table [lk_knowledgearticle_modifiedonbehalfby](systemuser.md#BKMK_lk_knowledgearticle_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_user_knowledgearticle"></a> user_knowledgearticle

See systemuser Table [user_knowledgearticle](systemuser.md#BKMK_user_knowledgearticle) One-To-Many relationship.

### <a name="BKMK_team_knowledgearticle"></a> team_knowledgearticle

See team Table [team_knowledgearticle](team.md#BKMK_team_knowledgearticle) One-To-Many relationship.

### <a name="BKMK_business_unit_knowledgearticle"></a> business_unit_knowledgearticle

See businessunit Table [business_unit_knowledgearticle](businessunit.md#BKMK_business_unit_knowledgearticle) One-To-Many relationship.

### <a name="BKMK_processstage_knowledgearticle"></a> processstage_knowledgearticle

See processstage Table [processstage_knowledgearticle](processstage.md#BKMK_processstage_knowledgearticle) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_languagelocaleid"></a> knowledgearticle_languagelocaleid

See languagelocale Table [knowledgearticle_languagelocaleid](languagelocale.md#BKMK_knowledgearticle_languagelocaleid) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_primaryauthorid"></a> knowledgearticle_primaryauthorid

See systemuser Table [knowledgearticle_primaryauthorid](systemuser.md#BKMK_knowledgearticle_primaryauthorid) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_parentarticle_contentid"></a> knowledgearticle_parentarticle_contentid

See knowledgearticle Table [knowledgearticle_parentarticle_contentid](knowledgearticle.md#BKMK_knowledgearticle_parentarticle_contentid) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_previousarticle_contentid"></a> knowledgearticle_previousarticle_contentid

See knowledgearticle Table [knowledgearticle_previousarticle_contentid](knowledgearticle.md#BKMK_knowledgearticle_previousarticle_contentid) One-To-Many relationship.

### <a name="BKMK_subject_knowledgearticles"></a> subject_knowledgearticles

See subject Table [subject_knowledgearticles](subject.md#BKMK_subject_knowledgearticles) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_rootarticle_id"></a> knowledgearticle_rootarticle_id

See knowledgearticle Table [knowledgearticle_rootarticle_id](knowledgearticle.md#BKMK_knowledgearticle_rootarticle_id) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_knowledgearticle"></a> TransactionCurrency_knowledgearticle

See transactioncurrency Table [TransactionCurrency_knowledgearticle](transactioncurrency.md#BKMK_TransactionCurrency_knowledgearticle) One-To-Many relationship.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the KnowledgeArticle table is the first table in the relationship. Listed by **SchemaName**.


### <a name="BKMK_knowledgearticle_category"></a> knowledgearticle_category

IntersectEntityName: knowledgearticlescategories<br />
#### Table 1

|Property|Value|
|--------|-----|
|IntersectAttribute|knowledgearticleid|
|IsCustomizable|False|
|LogicalName|knowledgearticle|
|NavigationPropertyName|knowledgearticle_category|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|

#### Table 2

|Property|Value|
|--------|-----|
|LogicalName|category|
|IntersectAttribute|categoryid|
|NavigationPropertyName|knowledgearticle_category|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |


### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.knowledgearticle?text=knowledgearticle EntityType" />