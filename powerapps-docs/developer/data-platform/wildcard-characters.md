---
title: Use wildcard characters in conditions for string values
description: Learn how to use wildcard characters in query conditions that use string values.
ms.date: 04/17/2023
ms.reviewer: jdaly
ms.topic: conceptual
author: mayadumesh
ms.author: mayadu
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
ms.custom: bap-template
---
# Use wildcard characters in conditions for string values

You can use wildcard characters with the following operators when you build queries that include conditions on string values:

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
`not endswith`<br/>

More information: [Use OData query functions](webapi/query-data-web-api.md#use-odata-query-functions)

---

When you use these condition operators, you can use certain characters to represent wildcards in your search criteria. The following table describes the characters you can use.

|Characters  |Description  |T-SQL Documentation and examples  |
|---------|---------|---------|
|`%`|Matches any string of zero or more characters. This wildcard character can be used as either a prefix or a suffix.|[Percent character (Wildcard - Character(s) to Match) (Transact-SQL)](/sql/t-sql/language-elements/percent-character-wildcard-character-s-to-match-transact-sql)|
|`_`|Matches any single character in a string comparison operation that involves pattern matching.|[_ (Wildcard - Match One Character) (Transact-SQL)](/sql/t-sql/language-elements/wildcard-match-one-character-transact-sql)|
|`[]`|Matches any single character in the range or set that's specified between square brackets.|[[ ] (Wildcard - Character(s) to Match) (Transact-SQL)](/sql/t-sql/language-elements/wildcard-character-s-to-match-transact-sql)|
|`[^]`|Matches any single character that isn't in the range or set that's specified between the square brackets.|[[^] (Wildcard - Character(s) Not to Match) (Transact-SQL)](/sql/t-sql/language-elements/wildcard-character-s-not-to-match-transact-sql)|


### Search for strings that contain wildcard characters

You can use the wildcard pattern matching characters as literal characters. To use a wildcard character as a literal character, enclose the wildcard character in brackets. More information: [Using Wildcard Characters As Literals](/sql/t-sql/language-elements/like-transact-sql#using-wildcard-characters-as-literals).

## Don't use trailing wild cards

Using trailing wildcards isn't supported.

# [FetchXml](#tab/fetchxml)

Don't use trailing wild cards in expressions using `begins-with`, `not-begin-with`, `ends-with`, or `not-end-with`.
Here are some examples of trailing wildcards:

|Bad Examples  |
|---------|
|`<condition attribute='name' operator='begins-with' value='%value' />`|
|`<condition attribute='name' operator='not-begins-with' value='%value' />`|
|`<condition attribute='name' operator='ends-with' value='value%' />`|
|`<condition attribute='name' operator='not-ends-with' value='value%' />`|

# [QueryExpression](#tab/queryexpression)

Don't use trailing wild cards in expressions using `BeginsWith`, `DoesNotBeginWith`, `EndsWith`, or `DoesNotEndWith`. 
Here are some examples of trailing wildcards:

|Bad Examples  |
|---------|
|`query.Criteria.AddCondition("name", ConditionOperator.BeginsWith, "%value");`|
|`query.Criteria.AddCondition("name", ConditionOperator.DoesNotBeginWith, "%value");`|
|`query.Criteria.AddCondition("name", ConditionOperator.EndsWith, "value%");`|
|`query.Criteria.AddCondition("name", ConditionOperator.DoesNotEndWith, "value%");`|

# [Web API](#tab/webapi)

Don't use trailing wild cards in expressions using `startswith`, `not startswith`, `endswith`, or `not endswith`.
Here are some examples of trailing wildcards:


|Bad Examples  |
|---------|
|`startswith(name,'%value')`|
|`not startswith(name,'%value')`|
|`endswith(name,'value%')`|
|`not endswith(name,'value%')`|

---

Queries that use these anti-patterns introduce performance problems because the queries can't be optimized.

### See also

[Use FetchXML to construct a query](use-fetchxml-construct-query.md)   
[Use the ConditionExpression class](org-service/use-conditionexpression-class.md)   
[Query data using the Web API](webapi/query-data-web-api.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
