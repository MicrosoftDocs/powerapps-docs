---
title: Use wildcard characters in conditions for string values
description: Learn how to use wildcard characters in query conditions that use string values.
ms.date: 08/05/2026
ms.reviewer: jdaly
ms.topic: article
author: abhia-msft
ms.author: abhia
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
ms.custom: bap-template
---
# Use wildcard characters in conditions for string values

Use wildcard characters with the following operators when you build queries that include conditions on string values:

## [FetchXml](#tab/fetchxml)

[`like`](fetchxml/reference/operators.md#like)<br/>
[`not-like`](fetchxml/reference/operators.md#like)<br/>
[`begins-with`](fetchxml/reference/operators.md#like)<br/>
[`not-begin-with`](fetchxml/reference/operators.md#like)<br/>
[`ends-with`](fetchxml/reference/operators.md#like)<br/>
[`not-end-with`](fetchxml/reference/operators.md#like)<br/>

For more information, see [Query data using FetchXml](fetchxml/overview.md).


## [QueryExpression](#tab/queryexpression)

<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator>.`Like`<br/>
<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator>.`NotLike`<br/>
<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator>.`BeginsWith`<br/>
<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator>.`DoesNotBeginWith`<br/>
<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator>.`EndsWith`<br/>
<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator>.`DoesNotEndWith`<br/>

For more information, see [Filter rows using QueryExpression](org-service/queryexpression/filter-rows.md).

## [Web API](#tab/webapi)

`contains`<br/>
`not contains`<br/>
`startswith`<br/>
`not startswith`<br/>
`endswith`<br/>
`not endswith`<br/>

For more information, see [Use OData query functions](webapi/query/filter-rows.md#use-odata-query-functions).

---

When you use these condition operators, you can use certain characters to represent wildcards in your search criteria. The following table describes the characters you can use.

|Characters  |Description  |T-SQL Documentation and examples  |
|---------|---------|---------|
|`%`|Matches any string of zero or more characters. You can use this wildcard character as either a prefix or a suffix.|[`%` wildcard: character(s) to match](/sql/t-sql/language-elements/percent-character-wildcard-character-s-to-match-transact-sql)|
|`_`|Matches any single character in a string comparison operation that involves pattern matching.|[`_` wildcard: match one character](/sql/t-sql/language-elements/wildcard-match-one-character-transact-sql)|
|`[]`|Matches any single character in the range or set that you specify between square brackets.|[`[ ]` wildcard: characters to match](/sql/t-sql/language-elements/wildcard-character-s-to-match-transact-sql)|
|`[^]`|Matches any single character that isn't in the range or set that you specify between the square brackets.|[`[^]` wildcard: characters not to match](/sql/t-sql/language-elements/wildcard-character-s-not-to-match-transact-sql)|


### Search for strings that contain wildcard characters

You can use the wildcard pattern matching characters as literal characters. To use a wildcard character as a literal character, enclose the wildcard character in brackets. For more information, see [Use wildcard characters as literals](/sql/t-sql/language-elements/like-transact-sql#use-wildcard-characters-as-literals).

## Don't use leading wild cards

Queries that use condition operators with implicit leading wild cards, such as `ends-with`, or explicit leading wild cards, perform less efficiently. In certain scenarios, these wild cards can cause poor performance across the organization. For more information, see: 
- [Optimize performance using FetchXml](fetchxml/optimize-performance.md)
- [Optimize performance using QueryExpression](org-service/queryexpression/optimize-performance.md)

These anti-patterns introduce performance problems because the query optimizer can't optimize the query.

### [FetchXml](#tab/fetchxml)

Don't use trailing wild cards in expressions that use `like`, `begins-with`, `not-begin-with`, `ends-with`, or `not-end-with`. Here are some examples of trailing wild cards:

|Bad Examples  |
|---------|
|`<condition attribute='name' operator='like' value='%value' />`|
|`<condition attribute='name' operator='begins-with' value='%value' />`|
|`<condition attribute='name' operator='not-begins-with' value='%value' />`|
|`<condition attribute='name' operator='ends-with' value='value' />`|
|`<condition attribute='name' operator='not-ends-with' value='value' />`|

### [QueryExpression](#tab/queryexpression)

Don't use leading wild cards in expressions that use `Like`, `BeginsWith`, `DoesNotBeginWith`, `EndsWith`, or `DoesNotEndWith`. Here are some examples of excess wildcards:

|Bad Examples  |
|---------|
|`query.Criteria.AddCondition("name", ConditionOperator.Like, "%value");`|
|`query.Criteria.AddCondition("name", ConditionOperator.BeginsWith, "%value");`|
|`query.Criteria.AddCondition("name", ConditionOperator.DoesNotBeginWith, "%value");`|
|`query.Criteria.AddCondition("name", ConditionOperator.EndsWith, "value");`|
|`query.Criteria.AddCondition("name", ConditionOperator.DoesNotEndWith, "value");`|

### [Web API](#tab/webapi)

Don't use leading wild cards in expressions that use `like`, `startswith`, `not startswith`, `endswith`, or `not endswith`. Here are some examples of excess wildcards:


|Bad Examples  |
|---------|
|`like(name,'%value')`|
|`startswith(name,'%value')`|
|`not startswith(name,'%value')`|
|`endswith(name,'value%')`|
|`not endswith(name,'value%')`|

---

### See also

[Filter rows using FetchXml](fetchxml/filter-rows.md)   
[Filter rows using QueryExpression](org-service/queryexpression/filter-rows.md)   
[Query data using the Web API](webapi/query/overview.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
