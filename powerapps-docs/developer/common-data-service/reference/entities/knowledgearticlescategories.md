---
title: "KnowledgeArticlesCategories Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the KnowledgeArticlesCategories entity."
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
ms.date: 10/31/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# KnowledgeArticlesCategories Entity Reference

Category for a Knowledge Article.

## Entity Properties

**DisplayName**: Knowledge Article Category<br />
**DisplayCollectionName**: KnowledgeArticle Categories<br />
**SchemaName**: KnowledgeArticlesCategories<br />
**CollectionSchemaName**: <br />
**LogicalName**: knowledgearticlescategories<br />
**LogicalCollectionName**: <br />
**EntitySetName**: KnowledgeArticleCategories<br />
**PrimaryIdAttribute**: knowledgearticlecategoryid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.


### <a name="BKMK_KnowledgeArticleCategoryId"></a> KnowledgeArticleCategoryId

**Description**: Unique identifier of the Category for the knowledge article.<br />
**DisplayName**: <br />
**LogicalName**: knowledgearticlecategoryid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CategoryId](#BKMK_CategoryId)
- [KnowledgeArticleId](#BKMK_KnowledgeArticleId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CategoryId"></a> CategoryId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: categoryid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_KnowledgeArticleId"></a> KnowledgeArticleId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: knowledgearticleid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


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

<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the KnowledgeArticlesCategories entity is the first entity in the relationship. Listed by **SchemaName**.


### <a name="BKMK_knowledgearticle_category"></a> knowledgearticle_category

See knowledgearticle Entity [knowledgearticle_category](knowledgearticle.md#BKMK_knowledgearticle_category) Many-To-Many Relationship.
knowledgearticlescategories

