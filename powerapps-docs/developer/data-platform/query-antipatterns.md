---
title: "Query Anti-Patterns to Avoid (Microsoft Dataverse)"
description: "Learn which query anti-patterns to avoid in Microsoft Dataverse to prevent timeouts and throttling. Optimize your queries for faster, more reliable apps."
ms.date: 10/26/2026
ms.topic: how-to
author: manasmams
ms.author: manasma
ms.reviewer: jdaly
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
---

# Query anti-patterns to avoid in Dataverse

Composing optimized queries for Dataverse is vital to ensure applications provide a fast, responsive, and reliable experience. Learn about query anti-patterns to avoid when composing queries for standard tables by using the `RetrieveMultiple` message or messages that have a parameter that inherits from the [QueryBase class](xref:Microsoft.Xrm.Sdk.Query.QueryBase). [This guidance also applies when sending a `GET` request against a collection of records by using OData](webapi/query/overview.md). 

> [!NOTE]
> The guidance in this article might not apply for [Elastic tables](elastic-tables.md) or when using [Dataverse Search](search/overview.md).


## <a name="LargeAmountOfAttributes"></a> Minimize the number of selected columns

Don't include columns you don't need in your query. Queries that return all columns or include a large number of columns can encounter performance problems due to the size of the dataset or complexity of the query.

## <a name="LargeAmountOfLogicalAttributes"></a> Minimize the number of selected logical columns

Avoid requesting too many columns, especially *logical columns*. A logical column contains values that are stored in different database tables. The [AttributeMetadata.IsLogical property](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.IsLogical) tells you whether a column is a logical column. Queries that contain many logical columns are slower because Dataverse needs to combine the data from other database tables.


## <a name="PerformanceLeadingWildCard"></a> Avoid leading wildcards in filter conditions

Queries that use conditions with leading wildcards (either explicitly, or implicitly with an operator like `ends-with`) can lead to bad performance. Dataverse can't take advantage of database indexes when a query uses leading wildcards, which forces SQL to scan the entire table. Table scans can happen even if there are other nonleading wildcard queries that limit the result set.

### [FetchXml](#tab/fetchxml)

The following example is a FetchXml [condition element](fetchxml/reference/condition.md) that uses a leading wildcard:

```xml
<condition attribute='accountnumber'
   operator='like'
   value='%234' />
```

### [QueryExpression](#tab/qe)

The following example is a [QueryExpression](xref:Microsoft.Xrm.Sdk.Query.QueryExpression) [ConditionExpression](xref:Microsoft.Xrm.Sdk.Query.ConditionExpression) that uses a leading wildcard:

```csharp
new ConditionExpression("accountnumber", ConditionOperator.Like, "%234")
```

### [OData](#tab/odata)

The following example is an OData query that uses a leading wildcard:

```http
$filter=startswith(accountnumber,'%234')
```

---

When queries time out and this pattern is detected, Dataverse returns a unique error to help identify which queries use this pattern:

> Name: `LeadingWildcardCauseTimeout`<br />
> Code: `0x80048573`<br />
> Number: `-2147187341`<br />
> Message: `The database operation timed out; this may be due to a leading wildcard value being used in a filter condition. Please consider removing filter conditions on leading wildcard values, as these filter conditions are expensive and may cause timeouts.`

Dataverse [heavily throttles](query-throttling.md) leading wildcard queries that are identified as a risk to the health of the environment to help prevent outages. When a query fails due to throttling and this pattern is detected, Dataverse returns a unique error:

> Name: `DataEngineLeadingWildcardQueryThrottling`<br />
> Code: `0x80048644`<br />
> Number: `-2147187132`<br />
> Message: `This query cannot be executed because it conflicts with Query Throttling; the query uses a leading wildcard value in a filter condition, which will cause the query to be throttled more aggressively.`<br />or <br /> `This query is throttled as it negatively impacts the database health; the query uses a leading wildcard value in a filter condition, which will cause the query to be throttled more aggressively.`

If you use leading wildcard queries, consider these options:

- Use [Dataverse search](search/overview.md) instead.
- Change your data model to help people avoid needing leading wildcard values.

### Other wildcard characters

As described in [Use wildcard characters in conditions for string values](wildcard-characters.md), other characters beyond the percent sign (`%`) character can act like a wildcard. The following query strings also behave like leading wildcards:

- `_234%`
- `[^a]234%`

Dataverse heavily throttles queries with search strings that start with these other leading wildcard special characters.

### Hyphen and apostrophe (single quote) characters

Database collation Unicode sorting rules make some search strings that start with a hyphen (`-`) or an apostrophe (`'`) perform like leading wildcard searches. Search strings that start with a hyphen or apostrophe can't take advantage of database indexes if the search string doesn't contain a nonwildcard character before the occurrence of the `%` character in the string. For example, `-%`, `-%234`, `'%`, and `'%751` can't efficiently use database indexes, while `-234%` and `'751%` can. Dataverse heavily throttles inefficient search strings that start with hyphens or apostrophes. To understand more about the database collation Unicode sorting rules for hyphens and apostrophes, see [SQL Server collations](/sql/relational-databases/collations/collation-and-unicode-support#SQL-collations).

## <a name="FilteringOnCalculatedColumns"></a> Avoid using formula or calculated columns in filter conditions

[Formula and calculated column](specialized-columns.md#formula-and-calculated-columns) values are calculated in real-time when you retrieve them. Queries that use filters on these columns force Dataverse to calculate the value for each possible record that can be returned so the filter can be applied. Queries are slower because Dataverse can't improve the performance of these queries by using SQL.

When queries time out and this pattern is detected, Dataverse returns a unique error to help identify which queries use this pattern:

> Name: `ComputedColumnCauseTimeout`<br />
> Code: `0x80048574`<br />
> Number: `-2147187340`<br />
> Message: `The database operation timed out; this may be due to a computed column being used in a filter condition. Please consider removing filter conditions on computed columns, as these filter conditions are expensive and may cause timeouts.`

Dataverse [heavily throttles](query-throttling.md) queries that have filters on calculated columns that are identified as a risk to the health of the environment to help prevent outages. When a query fails due to throttling and this pattern is detected, Dataverse returns a unique error:

> Name: `DataEngineComputedColumnQueryThrottling`<br />
> Code: `0x80048744`<br />
> Number: `-2147186876`<br />
> Message: `This query cannot be executed because it conflicts with Query Throttling; the query uses a computed column in a filter condition, which will cause the query to be throttled more aggressively.`<br />or <br /> `This query is throttled as it negatively impacts the database health; the query uses a computed column in a filter condition, which will cause the query to be throttled more aggressively.`

## <a name="OrderOnEnumAttribute"></a> Avoid ordering by choice columns

When you use [FetchXml](fetchxml/order-rows.md#choice-columns) or [QueryExpression](org-service/queryexpression/order-rows.md#choice-columns), and you order query results by a choice column, you sort the results by the localized label for each choice option. Ordering by the number value stored in the database doesn't provide a good experience in your application. Ordering on choice columns requires more compute resources to join and sort the rows by the localized label value. This extra work makes the query slower. If possible, try to avoid ordering results by choice column values.

> [!NOTE]
> OData is different. By using the Dataverse Web API, `$orderby` sorts rows by the integer value of the choice column rather than the localized label.

## <a name="OrderOnPropertiesFromJoinedTables"></a> Avoid ordering by columns in related tables

Ordering by columns on related tables makes the query slower because of the added complexity.

Ordering by related tables should only be done when needed to as described in the following sections:

### [FetchXml](#tab/fetchxml)

[Order rows](fetchxml/order-rows.md)

### [QueryExpression](#tab/qe)

[Order rows](org-service/queryexpression/order-rows.md)

### [OData](#tab/odata)

[Order rows](webapi/query/order-rows.md)

---


## <a name="PerformanceLargeColumnSearch"></a> Avoid using conditions on large text columns

Dataverse has two types of columns that can store large strings of text:

- [StringAttributeMetadata](xref:Microsoft.Xrm.Sdk.Metadata.StringAttributeMetadata) can store up to 4,000 characters.
- [MemoAttributeMetadata](xref:Microsoft.Xrm.Sdk.Metadata.MemoAttributeMetadata) can store a higher number.

The limit for both of these columns is specified by the `MaxLength` property.

Use conditions on string columns that have a `MaxLength` set to fewer than 850 characters.

All memo columns or string columns with a `MaxLength` greater than 850 are defined in Dataverse as large text columns. Large text columns are too large to effectively index, which leads to bad performance when included in a filter condition.

[Dataverse search](search/overview.md) is a better choice to query data in these kinds of columns.

## <a name="PerformanceValidationIssuesCauseTimeout"></a> Dataverse error for query timeouts caused by anti-patterns

When a query times out and uses one of the anti-patterns detailed on this page, Dataverse returns the following unique error. This error helps you identify which anti-patterns the query uses:

> Name: `PerformanceValidationIssuesCauseTimeout`<br />
> Code: `0x80048575`<br />
> Number: `-2147187339`<br />
> Message: `The database operation timed out; this may be due to the query performance issues identified in a query executed on this request. Please optimize the query by addressing the following identified performance issues: {0}. Please reference this document for guidance: https://go.microsoft.com/fwlink/?linkid=2300520`

[!INCLUDE [cc-query-antipattern-enum-table](includes/cc-query-antipattern-enum-table.md)]

Use the guidance on this page to understand the anti-patterns. Modify the query to avoid using these anti-patterns.

> [!NOTE]
> If a query contains either the `PerformanceLeadingWildCard` or the `FilteringOnCalculatedColumns` anti-pattern, Dataverse throws a different error. Queries that use the `PerformanceLeadingWildCard` anti-pattern throw the `LeadingWildcardCauseTimeout` error mentioned on this page. Queries that use the `FilteringOnCalculatedColumns` anti-pattern throw the `ComputedColumnCauseTimeout` error mentioned on this page. 
> 
> The `LeadingWildcardCauseTimeout` and `ComputedColumnCauseTimeout` errors predate the `PerformanceValidationIssuesCauseTimeout` error. To maintain backward compatibility, Dataverse continues to throw `LeadingWildcardCauseTimeout` and `ComputedColumnCauseTimeout`.  

### Related articles

[Query throttling](query-throttling.md)   
[Use wildcard characters in conditions for string values](wildcard-characters.md)   
[Query data using FetchXml](fetchxml/overview.md)   
[Query data using QueryExpression](org-service/queryexpression/overview.md)   
[Use OData to query data](webapi/query/overview.md)
