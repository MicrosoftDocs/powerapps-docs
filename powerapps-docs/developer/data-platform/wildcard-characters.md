---
title: "Use wildcard characters in conditions for string values in Microsoft Dataverse (PowerApps) | Microsoft Docs" 
description: "You can use wildcard characters when querying for conditions using string values." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 03/13/2022
ms.reviewer: "jdaly"
ms.topic: "article"
author: "mayadumesh" # GitHub ID Temp owner
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Use wildcard characters in conditions for string values

You can use wildcard characters when you construct queries using conditions on string values with the following operators:

# [FetchXml](#tab/fetchxml)

`like`<br/>
`not-like`<br/>
`begins-with`<br/>
`not-begin-with`<br/>
`ends-with`<br/>
`not-end-with`<br/>

More information: [Use FetchXML to construct a query](use-fetchxml-construct-query.md)


# [QueryExpression](#tab/queryexpression)

<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator>.`Like`<br/>
<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator>.`NotLike`<br/>
<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator>.`BeginsWith`<br/>
<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator>.`DoesNotBeginWith`<br/>
<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator>.`EndsWith`<br/>
<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator>.`DoesNotEndWith`<br/>

More information: [Use the ConditionExpression class](org-service/use-conditionexpression-class.md)

# [Web API](#tab/webapi)

`contains`<br/>
`not contains`<br/>
`startswith`<br/>
`not startswith`<br/>
`endswith`<br/>
`notendswith`<br/>

More information: [Standard query functions](webapi/query-data-web-api.md#standard-query-functions)

---

When using these condition operators you can use certain characters to represent wildcards in your search criteria.

These characters are described in the following table: 

|Characters  |Description  |T-SQL Documentation and examples  |
|---------|---------|---------|
|`%  `   |Matches any string of zero or more characters. This wildcard character can be used as either a prefix or a suffix.|[Percent character (Wildcard - Character(s) to Match) (Transact-SQL)](/sql/t-sql/language-elements/percent-character-wildcard-character-s-to-match-transact-sql)|
|`_ `    |Use the underscore character to match any single character in a string comparison operation that involves pattern matching.|[_ (Wildcard - Match One Character) (Transact-SQL)](/sql/t-sql/language-elements/wildcard-match-one-character-transact-sql)|
|`[]`     |Matches any single character within the specified range or set that is specified between brackets.|[[ ] (Wildcard - Character(s) to Match) (Transact-SQL)](/sql/t-sql/language-elements/wildcard-character-s-to-match-transact-sql)|
|`[^]`     |Matches any single character that is not within the range or set specified between the square brackets.|[[^] (Wildcard - Character(s) Not to Match) (Transact-SQL)](/sql/t-sql/language-elements/wildcard-character-s-not-to-match-transact-sql)|


### Search for strings that contain wildcard characters

You can use the wildcard pattern matching characters as literal characters. To use a wildcard character as a literal character, enclose the wildcard character in brackets. More information: [Using Wildcard Characters As Literals](/sql/t-sql/language-elements/like-transact-sql#using-wildcard-characters-as-literals).

## Do not use trailing wild cards

Using trailing wildcards is not supported.

# [FetchXml](#tab/fetchxml)

> [!IMPORTANT]
> Do not use trailing wild cards in expressions using `begins-with`, `not-begin-with`, `ends-with` or `not-end-with`. The following table gives some examples of trailing wildcards:

|Bad Examples  |
|---------|
|`<condition attribute='name' operator='begins-with' value='%value' />`|
|`<condition attribute='name' operator='not-begins-with' value='%value' />`|
|`<condition attribute='name' operator='ends-with' value='value%' />`|
|`<condition attribute='name' operator='not-ends-with' value='value%' />`|

# [QueryExpression](#tab/queryexpression)

> [!IMPORTANT]
> Do not use trailing wild cards in expressions using `BeginsWith`, `DoesNotBeginWith`, `EndsWith` or `DoesNotEndWith`. The following table gives some examples of trailing wildcards:

|Bad Examples  |
|---------|
|`query.Criteria.AddCondition("name", ConditionOperator.BeginsWith, "%value");`|
|`query.Criteria.AddCondition("name", ConditionOperator.DoesNotBeginWith, "%value");`|
|`query.Criteria.AddCondition("name", ConditionOperator.EndsWith, "value%");`|
|`query.Criteria.AddCondition("name", ConditionOperator.DoesNotEndWith, "value%");`|

# [Web API](#tab/webapi)

> [!IMPORTANT]
> Do not use trailing wild cards in expressions using `startswith`, `not startswith`, `endswith` or `not endswith`. The following table gives some examples of trailing wildcards:


|Bad Examples  |
|---------|
|`startswith(name,'%value')`|
|`not startswith(name,'%value')`|
|`endswith(name,'value%')`|
|`not endswith(name,'value%')`|

---

Queries using these anti-patterns introduce performance problems because the queries cannot be optimized.

### See also

[Use FetchXML to construct a query](use-fetchxml-construct-query.md)<br /> 
[Use the ConditionExpression class](org-service/use-conditionexpression-class.md)<br />
[Query data using the Web API](webapi/query-data-web-api.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]