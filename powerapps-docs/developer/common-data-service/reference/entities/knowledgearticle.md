---
title: "KnowledgeArticle Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the KnowledgeArticle entity."

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
---
# KnowledgeArticle Entity Reference

Organizational knowledge for internal and external use.

## Entity Properties

**DisplayName**: Knowledge Article<br />
**DisplayCollectionName**: Knowledge Articles<br />
**SchemaName**: KnowledgeArticle<br />
**CollectionSchemaName**: KnowledgeArticles<br />
**LogicalName**: knowledgearticle<br />
**LogicalCollectionName**: knowledgearticles<br />
**EntitySetName**: knowledgearticles<br />
**PrimaryIdAttribute**: knowledgearticleid<br />
**PrimaryNameAttribute**: title<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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

**Description**: Shows the automatically generated ID exposed to customers, partners, and other external users to reference and look up articles.<br />
**DisplayName**: Article Public Number<br />
**LogicalName**: articlepublicnumber<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 4000


### <a name="BKMK_Content"></a> Content

**Description**: Shows the body of the article stored in HTML format.<br />
**DisplayName**: Content<br />
**LogicalName**: content<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_Description"></a> Description

**Description**: A short overview of the article, primarily used in search results and for search engine optimization.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 155


### <a name="BKMK_ExpirationDate"></a> ExpirationDate

**Description**: Enter an expiration date for the article. Leave this field blank for no expiration date.<br />
**DisplayName**: Expiration Date<br />
**LogicalName**: expirationdate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ExpirationStateId"></a> ExpirationStateId

**Description**: Contains the id of the expiration state of the entity.<br />
**DisplayName**: Expiration State Id<br />
**LogicalName**: expirationstateid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_ExpirationStatusId"></a> ExpirationStatusId

**Description**: Contains the id of the expiration status of the entity.<br />
**DisplayName**: Expired Status<br />
**LogicalName**: expirationstatusid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_ExpiredReviewOptions"></a> ExpiredReviewOptions

**Description**: Expired Review Options<br />
**DisplayName**: Expired Review Options<br />
**LogicalName**: expiredreviewoptions<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Needs Updating
- **Value**: 1 **Label**: Republish
- **Value**: 2 **Label**: Archive



### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

**Description**: Sequence number of the import that created this record.<br />
**DisplayName**: Import Sequence Number<br />
**LogicalName**: importsequencenumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_IsInternal"></a> IsInternal

**Description**: Shows whether this article is only visible internally.<br />
**DisplayName**: Internal<br />
**LogicalName**: isinternal<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsLatestVersion"></a> IsLatestVersion

**Description**: Shows which version of the knowledge article is the latest version.<br />
**DisplayName**: Is Latest Version<br />
**LogicalName**: islatestversion<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsPrimary"></a> IsPrimary

**Description**: Select whether the article is the primary article.<br />
**DisplayName**: Primary Article<br />
**LogicalName**: isprimary<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsRootArticle"></a> IsRootArticle

**Description**: Select whether the article is the root article.<br />
**DisplayName**: Root Article<br />
**LogicalName**: isrootarticle<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_Keywords"></a> Keywords

**Description**: Type keywords to be used for searches in knowledge base articles. Separate keywords by using commas.<br />
**DisplayName**: Keywords<br />
**LogicalName**: keywords<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: Recommended<br />
**Type**: Memo<br />
**Format**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 4000


### <a name="BKMK_knowledgearticleId"></a> knowledgearticleId

**Description**: Unique identifier for entity instances<br />
**DisplayName**: Knowledge Article<br />
**LogicalName**: knowledgearticleid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_LanguageLocaleId"></a> LanguageLocaleId

**Description**: Select the language that the article's content is in.<br />
**DisplayName**: Language<br />
**LogicalName**: languagelocaleid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: languagelocale


### <a name="BKMK_MajorVersionNumber"></a> MajorVersionNumber

**Description**: Shows the major version number of this article's content.<br />
**DisplayName**: Major Version Number<br />
**LogicalName**: majorversionnumber<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_MinorVersionNumber"></a> MinorVersionNumber

**Description**: Shows the minor version number of this article's content.<br />
**DisplayName**: Minor Version Number<br />
**LogicalName**: minorversionnumber<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

**Description**: Date and time that the record was migrated.<br />
**DisplayName**: Record Created On<br />
**LogicalName**: overriddencreatedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Unique identifier of the user or team who owns the record.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: Owner Id Type<br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_ParentArticleContentId"></a> ParentArticleContentId

**Description**: Contains the id of the parent article content associated with the entity.<br />
**DisplayName**: Parent Article Content Id<br />
**LogicalName**: parentarticlecontentid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: knowledgearticle


### <a name="BKMK_PreviousArticleContentId"></a> PreviousArticleContentId

**Description**: Shows the version that the current article was restored from.<br />
**DisplayName**: Previous Article Content ID<br />
**LogicalName**: previousarticlecontentid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: knowledgearticle


### <a name="BKMK_primaryauthorid"></a> primaryauthorid

**Description**: Contains the id of the primary author associated with the article.<br />
**DisplayName**: Primary Author Id<br />
**LogicalName**: primaryauthorid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_processid"></a> processid

**Description**: Contains the id of the process associated with the entity.<br />
**DisplayName**: Process Id<br />
**LogicalName**: processid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_PublishOn"></a> PublishOn

**Description**: Date and time when the record was published.<br />
**DisplayName**: Publish On<br />
**LogicalName**: publishon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_PublishStatusId"></a> PublishStatusId

**Description**: Publish Status of the Article.<br />
**DisplayName**: Published Status<br />
**LogicalName**: publishstatusid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_ReadyForReview"></a> ReadyForReview

**Description**: Ready For Review<br />
**DisplayName**: Ready For Review<br />
**LogicalName**: readyforreview<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Completed
- **FalseOption Value**: 0 **Label**: Mark Complete

**DefaultValue**: False


### <a name="BKMK_Review"></a> Review

**Description**: Review<br />
**DisplayName**: Review<br />
**LogicalName**: review<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Approved
- **Value**: 1 **Label**: Rejected



### <a name="BKMK_RootArticleId"></a> RootArticleId

**Description**: Contains the id of the root article.<br />
**DisplayName**: Root Article Id<br />
**LogicalName**: rootarticleid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: knowledgearticle


### <a name="BKMK_ScheduledStatusId"></a> ScheduledStatusId

**Description**: Contains the id of the scheduled status of the entity.<br />
**DisplayName**: Scheduled Status<br />
**LogicalName**: scheduledstatusid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_SetCategoryAssociations"></a> SetCategoryAssociations

**Description**: Shows whether category associations have been set<br />
**DisplayName**: Set Category Associations<br />
**LogicalName**: setcategoryassociations<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Completed
- **FalseOption Value**: 0 **Label**: Mark as Complete

**DefaultValue**: False


### <a name="BKMK_stageid"></a> stageid

**Description**: Contains the id of the stage where the entity is located.<br />
**DisplayName**: Stage Id<br />
**LogicalName**: stageid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_StateCode"></a> StateCode

**Description**: Shows whether the article is a draft or is published, archived, or discarded. Draft articles aren't available externally and can be edited. Published articles are available externally, based on applicable permissions, but can't be edited. All metadata changes are reflected in the published version. Archived and discarded articles aren't available externally and can't be edited.<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Draft **DefaultStatus**: 1 **InvariantName**: Draft
- **Value**: 1 **Label**: Approved **DefaultStatus**: 5 **InvariantName**: Approved
- **Value**: 2 **Label**: Scheduled **DefaultStatus**: 6 **InvariantName**: Scheduled
- **Value**: 3 **Label**: Published **DefaultStatus**: 7 **InvariantName**: Published
- **Value**: 4 **Label**: Expired **DefaultStatus**: 10 **InvariantName**: Expired
- **Value**: 5 **Label**: Archived **DefaultStatus**: 12 **InvariantName**: Archived
- **Value**: 6 **Label**: Discarded **DefaultStatus**: 13 **InvariantName**: Discarded



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Select the article's status.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Status<br />
**Options**:

- **Value**: 1 **Label**: Proposed **State**: 0
- **Value**: 2 **Label**: Draft **State**: 0
- **Value**: 3 **Label**: Needs review **State**: 0
- **Value**: 4 **Label**: In review **State**: 0
- **Value**: 5 **Label**: Approved **State**: 1
- **Value**: 6 **Label**: Scheduled **State**: 2
- **Value**: 7 **Label**: Published **State**: 3
- **Value**: 8 **Label**: Needs review **State**: 3
- **Value**: 9 **Label**: Updating **State**: 3
- **Value**: 10 **Label**: Expired **State**: 4
- **Value**: 11 **Label**: Rejected **State**: 4
- **Value**: 12 **Label**: Archived **State**: 5
- **Value**: 13 **Label**: Discarded **State**: 6
- **Value**: 14 **Label**: Rejected **State**: 6



### <a name="BKMK_SubjectId"></a> SubjectId

**Description**: Choose the subject of the article to assist with article searches. You can configure subjects under Business Management in the Settings area.<br />
**DisplayName**: Subject<br />
**LogicalName**: subjectid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: subject


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

**Description**: Type a title for the article.<br />
**DisplayName**: Title<br />
**LogicalName**: title<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 4000


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

**Description**: Exchange rate for the currency associated with the KnowledgeArticle with respect to the base currency.<br />
**DisplayName**: Currency<br />
**LogicalName**: transactioncurrencyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: transactioncurrency


### <a name="BKMK_traversedpath"></a> traversedpath

**Description**: A comma separated list of string values representing the unique identifiers of stages in a Business Process Flow Instance in the order that they occur.<br />
**DisplayName**: Traversed Path<br />
**LogicalName**: traversedpath<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1250


### <a name="BKMK_UpdateContent"></a> UpdateContent

**Description**: Update Content<br />
**DisplayName**: Update Content<br />
**LogicalName**: updatecontent<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Content Updated
- **FalseOption Value**: 0 **Label**: Mark When Completed

**DefaultValue**: False


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

**Description**: Unique identifier of the user who created the record.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: True<br />
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


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the record was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the record.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: True<br />
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


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

**Description**: Exchange rate for the currency associated with the KnowledgeArticle with respect to the base currency.<br />
**DisplayName**: ExchangeRate<br />
**LogicalName**: exchangerate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0.0000000001<br />
**Precision**: 10


### <a name="BKMK_KnowledgeArticleViews"></a> KnowledgeArticleViews

**Description**: Shows the total number of article views.<br />
**DisplayName**: Knowledge Article Views<br />
**LogicalName**: knowledgearticleviews<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_KnowledgeArticleViews_Date"></a> KnowledgeArticleViews_Date

**Description**: The date time for Knowledge Article View.<br />
**DisplayName**: Knowledge Article View(Last Updated Time)<br />
**LogicalName**: knowledgearticleviews_date<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_KnowledgeArticleViews_State"></a> KnowledgeArticleViews_State

**Description**: State of Knowledge Article View.<br />
**DisplayName**: Knowledge Article View(State)<br />
**LogicalName**: knowledgearticleviews_state<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_LanguageLocaleIdLocaleId"></a> LanguageLocaleIdLocaleId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: languagelocaleidlocaleid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 1


### <a name="BKMK_LanguageLocaleIdName"></a> LanguageLocaleIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: languagelocaleidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 500


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who modified the record.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: True<br />
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


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the record was modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who modified the record.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: True<br />
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


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Description**: Name of the owner<br />
**DisplayName**: <br />
**LogicalName**: owneridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

**Description**: Yomi name of the owner<br />
**DisplayName**: <br />
**LogicalName**: owneridyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Description**: Unique identifier for the business unit that owns the record<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier for the team that owns the record.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier for the user that owns the record.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ParentArticleContentIdName"></a> ParentArticleContentIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: parentarticlecontentidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 500


### <a name="BKMK_PreviousArticleContentIdName"></a> PreviousArticleContentIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: previousarticlecontentidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_primaryauthoridName"></a> primaryauthoridName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: primaryauthoridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_Rating"></a> Rating

**Description**: Information which specifies how helpful the related record was.<br />
**DisplayName**: Rating<br />
**LogicalName**: rating<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: -100000000000<br />
**Precision**: 2


### <a name="BKMK_Rating_Count"></a> Rating_Count

**Description**: Rating Count<br />
**DisplayName**: Rating(Count)<br />
**LogicalName**: rating_count<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_Rating_Date"></a> Rating_Date

**Description**: The date time for Rating.<br />
**DisplayName**: Rating(Last Updated Time)<br />
**LogicalName**: rating_date<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_Rating_State"></a> Rating_State

**Description**: State of Rating<br />
**DisplayName**: Rating(State)<br />
**LogicalName**: rating_state<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_Rating_Sum"></a> Rating_Sum

**Description**: Total sum of Rating<br />
**DisplayName**: Rating(sum)<br />
**LogicalName**: rating_sum<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0<br />
**Precision**: 2


### <a name="BKMK_RootArticleIdName"></a> RootArticleIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: rootarticleidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_SubjectIdDsc"></a> SubjectIdDsc

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: subjectiddsc<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_SubjectIdName"></a> SubjectIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: subjectidname<br />
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
- [knowledgearticle_UserEntityInstanceDatas](#BKMK_knowledgearticle_UserEntityInstanceDatas)
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


### <a name="BKMK_knowledgearticle_connections1"></a> knowledgearticle_connections1

Same as connection entity [knowledgearticle_connections1](connection.md#BKMK_knowledgearticle_connections1) Many-To-One relationship.

**ReferencingEntity**: connection<br />
**ReferencingAttribute**: record1id<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_connections1<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 100

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_knowledgearticle_connections2"></a> knowledgearticle_connections2

Same as connection entity [knowledgearticle_connections2](connection.md#BKMK_knowledgearticle_connections2) Many-To-One relationship.

**ReferencingEntity**: connection<br />
**ReferencingAttribute**: record2id<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_connections2<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_knowledgearticle_DuplicateMatchingRecord"></a> knowledgearticle_DuplicateMatchingRecord

Same as duplicaterecord entity [knowledgearticle_DuplicateMatchingRecord](duplicaterecord.md#BKMK_knowledgearticle_DuplicateMatchingRecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: duplicaterecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_DuplicateMatchingRecord<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_knowledgearticle_DuplicateBaseRecord"></a> knowledgearticle_DuplicateBaseRecord

Same as duplicaterecord entity [knowledgearticle_DuplicateBaseRecord](duplicaterecord.md#BKMK_knowledgearticle_DuplicateBaseRecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: baserecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_DuplicateBaseRecord<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_knowledgearticle_SharePointDocumentLocations"></a> knowledgearticle_SharePointDocumentLocations

Same as sharepointdocumentlocation entity [knowledgearticle_SharePointDocumentLocations](sharepointdocumentlocation.md#BKMK_knowledgearticle_SharePointDocumentLocations) Many-To-One relationship.

**ReferencingEntity**: sharepointdocumentlocation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_SharePointDocumentLocations<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_knowledgearticle_QueueItems"></a> knowledgearticle_QueueItems

Same as queueitem entity [knowledgearticle_QueueItems](queueitem.md#BKMK_knowledgearticle_QueueItems) Many-To-One relationship.

**ReferencingEntity**: queueitem<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_QueueItems<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_knowledgearticle_Annotations"></a> knowledgearticle_Annotations

Same as annotation entity [knowledgearticle_Annotations](annotation.md#BKMK_knowledgearticle_Annotations) Many-To-One relationship.

**ReferencingEntity**: annotation<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_Annotations<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_knowledgearticle_Teams"></a> knowledgearticle_Teams

Same as team entity [knowledgearticle_Teams](team.md#BKMK_knowledgearticle_Teams) Many-To-One relationship.

**ReferencingEntity**: team<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_Teams<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_knowledgearticle_AsyncOperations"></a> knowledgearticle_AsyncOperations

Same as asyncoperation entity [knowledgearticle_AsyncOperations](asyncoperation.md#BKMK_knowledgearticle_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_AsyncOperations<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_knowledgearticle_UserEntityInstanceDatas"></a> knowledgearticle_UserEntityInstanceDatas

Same as userentityinstancedata entity [knowledgearticle_UserEntityInstanceDatas](userentityinstancedata.md#BKMK_knowledgearticle_UserEntityInstanceDatas) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_UserEntityInstanceDatas<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_knowledgearticle_ProcessSession"></a> knowledgearticle_ProcessSession

Same as processsession entity [knowledgearticle_ProcessSession](processsession.md#BKMK_knowledgearticle_ProcessSession) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_ProcessSession<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_knowledgearticle_BulkDeleteFailures"></a> knowledgearticle_BulkDeleteFailures

Same as bulkdeletefailure entity [knowledgearticle_BulkDeleteFailures](bulkdeletefailure.md#BKMK_knowledgearticle_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_BulkDeleteFailures<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_knowledgearticle_PrincipalObjectAttributeAccess"></a> knowledgearticle_PrincipalObjectAttributeAccess

Same as principalobjectattributeaccess entity [knowledgearticle_PrincipalObjectAttributeAccess](principalobjectattributeaccess.md#BKMK_knowledgearticle_PrincipalObjectAttributeAccess) Many-To-One relationship.

**ReferencingEntity**: principalobjectattributeaccess<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_PrincipalObjectAttributeAccess<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_KnowledgeArticle_SocialActivities"></a> KnowledgeArticle_SocialActivities

Same as socialactivity entity [KnowledgeArticle_SocialActivities](socialactivity.md#BKMK_KnowledgeArticle_SocialActivities) Many-To-One relationship.

**ReferencingEntity**: socialactivity<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: KnowledgeArticle_SocialActivities<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_KnowledgeArticle_Letters"></a> KnowledgeArticle_Letters

Same as letter entity [KnowledgeArticle_Letters](letter.md#BKMK_KnowledgeArticle_Letters) Many-To-One relationship.

**ReferencingEntity**: letter<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: KnowledgeArticle_Letters<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_KnowledgeArticle_Tasks"></a> KnowledgeArticle_Tasks

Same as task entity [KnowledgeArticle_Tasks](task.md#BKMK_KnowledgeArticle_Tasks) Many-To-One relationship.

**ReferencingEntity**: task<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: KnowledgeArticle_Tasks<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_knowledgearticle_views"></a> knowledgearticle_views

Same as knowledgearticleviews entity [knowledgearticle_views](knowledgearticleviews.md#BKMK_knowledgearticle_views) Many-To-One relationship.

**ReferencingEntity**: knowledgearticleviews<br />
**ReferencingAttribute**: knowledgearticleid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_views<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 10

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_KnowledgeArticle_Faxes"></a> KnowledgeArticle_Faxes

Same as fax entity [KnowledgeArticle_Faxes](fax.md#BKMK_KnowledgeArticle_Faxes) Many-To-One relationship.

**ReferencingEntity**: fax<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: KnowledgeArticle_Faxes<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_lk_expiredprocess_knowledgearticleid"></a> lk_expiredprocess_knowledgearticleid

Same as expiredprocess entity [lk_expiredprocess_knowledgearticleid](expiredprocess.md#BKMK_lk_expiredprocess_knowledgearticleid) Many-To-One relationship.

**ReferencingEntity**: expiredprocess<br />
**ReferencingAttribute**: knowledgearticleid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_expiredprocess<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_KnowledgeArticle_Appointments"></a> KnowledgeArticle_Appointments

Same as appointment entity [KnowledgeArticle_Appointments](appointment.md#BKMK_KnowledgeArticle_Appointments) Many-To-One relationship.

**ReferencingEntity**: appointment<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: KnowledgeArticle_Appointments<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_lk_newprocess_knowledgearticleid"></a> lk_newprocess_knowledgearticleid

Same as newprocess entity [lk_newprocess_knowledgearticleid](newprocess.md#BKMK_lk_newprocess_knowledgearticleid) Many-To-One relationship.

**ReferencingEntity**: newprocess<br />
**ReferencingAttribute**: knowledgearticleid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_newprocess<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_knowledgearticle_rootarticle_id"></a> knowledgearticle_rootarticle_id

Same as knowledgearticle entity [knowledgearticle_rootarticle_id](knowledgearticle.md#BKMK_knowledgearticle_rootarticle_id) Many-To-One relationship.

**ReferencingEntity**: knowledgearticle<br />
**ReferencingAttribute**: rootarticleid<br />
**IsHierarchical**: True<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_rootarticle_id<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_lk_translationprocess_knowledgearticleid"></a> lk_translationprocess_knowledgearticleid

Same as translationprocess entity [lk_translationprocess_knowledgearticleid](translationprocess.md#BKMK_lk_translationprocess_knowledgearticleid) Many-To-One relationship.

**ReferencingEntity**: translationprocess<br />
**ReferencingAttribute**: knowledgearticleid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_translationprocess<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_KnowledgeArticle_RecurringAppointmentMasters"></a> KnowledgeArticle_RecurringAppointmentMasters

Same as recurringappointmentmaster entity [KnowledgeArticle_RecurringAppointmentMasters](recurringappointmentmaster.md#BKMK_KnowledgeArticle_RecurringAppointmentMasters) Many-To-One relationship.

**ReferencingEntity**: recurringappointmentmaster<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: KnowledgeArticle_RecurringAppointmentMasters<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_KnowledgeArticle_ActivityPointers"></a> KnowledgeArticle_ActivityPointers

Same as activitypointer entity [KnowledgeArticle_ActivityPointers](activitypointer.md#BKMK_KnowledgeArticle_ActivityPointers) Many-To-One relationship.

**ReferencingEntity**: activitypointer<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: KnowledgeArticle_ActivityPointers<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 10

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_KnowledgeArticle_SyncErrors"></a> KnowledgeArticle_SyncErrors

Same as syncerror entity [KnowledgeArticle_SyncErrors](syncerror.md#BKMK_KnowledgeArticle_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: KnowledgeArticle_SyncErrors<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_KnowledgeArticle_Feedback"></a> KnowledgeArticle_Feedback

Same as feedback entity [KnowledgeArticle_Feedback](feedback.md#BKMK_KnowledgeArticle_Feedback) Many-To-One relationship.

**ReferencingEntity**: feedback<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: KnowledgeArticle_Feedback<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 150

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_knowledgearticle_previousarticle_contentid"></a> knowledgearticle_previousarticle_contentid

Same as knowledgearticle entity [knowledgearticle_previousarticle_contentid](knowledgearticle.md#BKMK_knowledgearticle_previousarticle_contentid) Many-To-One relationship.

**ReferencingEntity**: knowledgearticle<br />
**ReferencingAttribute**: previousarticlecontentid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_previousarticle_contentid<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_knowledgearticle_PostFollows"></a> knowledgearticle_PostFollows

Same as postfollow entity [knowledgearticle_PostFollows](postfollow.md#BKMK_knowledgearticle_PostFollows) Many-To-One relationship.

**ReferencingEntity**: postfollow<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_PostFollows<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_knowledgearticle_activity_parties"></a> knowledgearticle_activity_parties

Same as activityparty entity [knowledgearticle_activity_parties](activityparty.md#BKMK_knowledgearticle_activity_parties) Many-To-One relationship.

**ReferencingEntity**: activityparty<br />
**ReferencingAttribute**: partyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_activity_parties<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_knowledgearticle_parentarticle_contentid"></a> knowledgearticle_parentarticle_contentid

Same as knowledgearticle entity [knowledgearticle_parentarticle_contentid](knowledgearticle.md#BKMK_knowledgearticle_parentarticle_contentid) Many-To-One relationship.

**ReferencingEntity**: knowledgearticle<br />
**ReferencingAttribute**: parentarticlecontentid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_parentarticle_contentid<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_KnowledgeArticle_Phonecalls"></a> KnowledgeArticle_Phonecalls

Same as phonecall entity [KnowledgeArticle_Phonecalls](phonecall.md#BKMK_KnowledgeArticle_Phonecalls) Many-To-One relationship.

**ReferencingEntity**: phonecall<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: KnowledgeArticle_Phonecalls<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_KnowledgeArticle_Emails"></a> KnowledgeArticle_Emails

Same as email entity [KnowledgeArticle_Emails](email.md#BKMK_KnowledgeArticle_Emails) Many-To-One relationship.

**ReferencingEntity**: email<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: KnowledgeArticle_Emails<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

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

See systemuser Entity [lk_knowledgearticle_createdby](systemuser.md#BKMK_lk_knowledgearticle_createdby) One-To-Many relationship.

### <a name="BKMK_lk_knowledgearticle_createdonbehalfby"></a> lk_knowledgearticle_createdonbehalfby

See systemuser Entity [lk_knowledgearticle_createdonbehalfby](systemuser.md#BKMK_lk_knowledgearticle_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_knowledgearticle_modifiedby"></a> lk_knowledgearticle_modifiedby

See systemuser Entity [lk_knowledgearticle_modifiedby](systemuser.md#BKMK_lk_knowledgearticle_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_knowledgearticle_modifiedonbehalfby"></a> lk_knowledgearticle_modifiedonbehalfby

See systemuser Entity [lk_knowledgearticle_modifiedonbehalfby](systemuser.md#BKMK_lk_knowledgearticle_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_user_knowledgearticle"></a> user_knowledgearticle

See systemuser Entity [user_knowledgearticle](systemuser.md#BKMK_user_knowledgearticle) One-To-Many relationship.

### <a name="BKMK_team_knowledgearticle"></a> team_knowledgearticle

See team Entity [team_knowledgearticle](team.md#BKMK_team_knowledgearticle) One-To-Many relationship.

### <a name="BKMK_business_unit_knowledgearticle"></a> business_unit_knowledgearticle

See businessunit Entity [business_unit_knowledgearticle](businessunit.md#BKMK_business_unit_knowledgearticle) One-To-Many relationship.

### <a name="BKMK_processstage_knowledgearticle"></a> processstage_knowledgearticle

See processstage Entity [processstage_knowledgearticle](processstage.md#BKMK_processstage_knowledgearticle) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_languagelocaleid"></a> knowledgearticle_languagelocaleid

See languagelocale Entity [knowledgearticle_languagelocaleid](languagelocale.md#BKMK_knowledgearticle_languagelocaleid) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_primaryauthorid"></a> knowledgearticle_primaryauthorid

See systemuser Entity [knowledgearticle_primaryauthorid](systemuser.md#BKMK_knowledgearticle_primaryauthorid) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_parentarticle_contentid"></a> knowledgearticle_parentarticle_contentid

See knowledgearticle Entity [knowledgearticle_parentarticle_contentid](knowledgearticle.md#BKMK_knowledgearticle_parentarticle_contentid) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_previousarticle_contentid"></a> knowledgearticle_previousarticle_contentid

See knowledgearticle Entity [knowledgearticle_previousarticle_contentid](knowledgearticle.md#BKMK_knowledgearticle_previousarticle_contentid) One-To-Many relationship.

### <a name="BKMK_subject_knowledgearticles"></a> subject_knowledgearticles

See subject Entity [subject_knowledgearticles](subject.md#BKMK_subject_knowledgearticles) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_rootarticle_id"></a> knowledgearticle_rootarticle_id

See knowledgearticle Entity [knowledgearticle_rootarticle_id](knowledgearticle.md#BKMK_knowledgearticle_rootarticle_id) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_knowledgearticle"></a> TransactionCurrency_knowledgearticle

See transactioncurrency Entity [TransactionCurrency_knowledgearticle](transactioncurrency.md#BKMK_TransactionCurrency_knowledgearticle) One-To-Many relationship.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the KnowledgeArticle entity is the first entity in the relationship. Listed by **SchemaName**.


### <a name="BKMK_knowledgearticle_category"></a> knowledgearticle_category

**IntersectEntityName**: knowledgearticlescategories<br />
**Entity1LogicalName**: knowledgearticle<br />

- **Entity1IntersectAttribute**: knowledgearticleid
- **Entity1NavigationPropertyName**: knowledgearticle_category
- **Entity1AssociatedMenuConfiguration**:

  - **Behavior**: DoNotDisplay
  - **Group**: Details
  - **Label**: 
  - **Order**: 10000

**Entity2LogicalName**: [category](category.md)<br />

- **Entity2IntersectAttribute**: categoryid
- **Entity2NavigationPropertyName**: knowledgearticle_category
- **Entity2AssociatedMenuConfiguration**:

  - **Behavior**: DoNotDisplay
  - **Group**: Details
  - **Label**: 
  - **Order**: 

**IsCustomizable**: False<br />
knowledgearticle

