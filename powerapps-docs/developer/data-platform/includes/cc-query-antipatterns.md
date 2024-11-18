## Patterns to avoid

Composing optimized queries for Dataverse is vital to ensure applications provide a fast, responsive, and reliable experience. This section describes patterns to avoid and concepts to understand when composing queries for standard tables using the `RetrieveMultiple` message, or messages that have a parameter that inherits from the [QueryBase class](/dotnet/api/microsoft.xrm.sdk.query.querybase). This guidance also applies when sending a `GET` request against a collection of records using OData. The guidance here might not apply for [Elastic tables](../elastic-tables.md) or when using [Dataverse Search](../search/overview.md).


### Minimize the number of selected columns

Don't include columns you don't need in your query. Queries that return all columns or include a large number of columns can encounter performance issues due to the size of the dataset or complexity of the query.

This practice is especially true for *logical columns*. A logical column contains values that are stored in different database tables. The [AttributeMetadata.IsLogical property](/dotnet/api/microsoft.xrm.sdk.metadata.attributemetadata.islogical) tells you whether a column is a logical column. Queries that contain many logical columns are slower because Dataverse needs to combine the data from other database tables.


### Avoid leading wild cards in filter conditions

Queries that use conditions with leading wild cards (either explicitly, or implicitly with an operator like `ends-with`) can lead to bad performance. Dataverse can't take advantage of database indexes when a query using leading wild cards, which forces SQL to scan the entire table. Table scans can happen even if there are other nonleading wild card queries that limit the result set.

The following example is a FetchXml [condition element](../fetchxml/reference/condition.md) that uses a leading wild card:

```xml
<condition attribute='accountnumber'
   operator='like'
   value='%234' />
```

The following example is a [QueryExpression](xref:Microsoft.Xrm.Sdk.Query.QueryExpression) [ConditionExpression](xref:Microsoft.Xrm.Sdk.Query.ConditionExpression) that uses a leading wild card:

```csharp
new ConditionExpression("accountnumber", ConditionOperator.Like, "%234")
```

The following example is a OData query that uses a leading wild card:

```http
$filter=startswith(accountnumber,'%234')
```

When queries time out and this pattern is detected, Dataverse returns a unique error to help identify which queries are using this pattern:

> Name: `LeadingWildcardCauseTimeout`<br />
> Code: `0x80048573`<br />
> Number: `-2147187341`<br />
> Message: `The database operation timed out; this may be due to a leading wildcard value being used in a filter condition. Please consider removing filter conditions on leading wildcard values, as these filter conditions are expensive and may cause timeouts.`

Dataverse heavily throttles leading wild card queries that are identified as a risk to the health of the org to help prevent outages. [Learn more about query throttling](../query-throttling.md)

If you find yourself using leading wild card queries, look into these options:

- Use [Dataverse search](../search/overview.md) instead.
- Change your data model to help people avoid needing leading wild cards.

#### Other wildcard characters

As described in [Use wildcard characters in conditions for string values](../wildcard-characters.md), other characters beyond the percent sign ('%') character can act like a wildcard. Following are two example query strings that also behave like leading wildcards:

- `_234%`
- `[^a]234%`

Dataverse heavily throttles queries with search strings that start with these other leading wildcard special characters.

#### Hyphen character

Database collation unicode sorting rules make some search strings that start with a hyphen ('-') perform like leading wildcard searches. Search strings that start with a hyphen can't take advantage of database indexes if the search string doesn't contain a nonwildcard character before the occurrence of the '%' character in the string. For example, `-%` and `-%234` can't efficiently use database indexes, while `-234%` can. Dataverse heavily throttles inefficient search strings that start with hyphens. To understand more about the database collation unicode sorting rules for hyphens, see [SQL Server collations](/sql/relational-databases/collations/collation-and-unicode-support#SQL-collations).

### Avoid using formula or calculated columns in filter conditions

[Formula and calculated column](../calculated-rollup-attributes.md#formula-and-calculated-columns) values are calculated in real-time when they're retrieved. Queries that use filters on these columns force Dataverse to calculate the value for each possible record that can be returned so the filter can be applied. Queries are slower because Dataverse can't improve the performance of these queries using SQL.

When queries time out and this pattern is detected, Dataverse returns a unique error to help identify which queries are using this pattern:

> Name: `ComputedColumnCauseTimeout`<br />
> Code: `0x80048574`<br />
> Number: `-2147187340`<br />
> Message: `The database operation timed out; this may be due to a computed column being used in a filter condition. Please consider removing filter conditions on computed columns, as these filter conditions are expensive and may cause timeouts.`

To help prevent outages, Dataverse applies throttles on queries that have filters on calculated columns that are identified as a risk to the health of the environment. [Learn more about query throttling](../query-throttling.md)


### Avoid ordering by choice columns

When you use [FetchXml](../fetchxml/order-rows.md#choice-columns) or [QueryExpression](../org-service/queryexpression/order-rows.md#choice-columns), when you order query results using a choice column, the results are sorted using the localized label for each choice option. Ordering by the number value stored in the database wouldn't provide a good experience in your application. You should know that ordering on choice columns requires more compute resources to join and sort the rows by the localized label value. This extra work makes the query slower. If possible, try to avoid ordering results by choice column values.

> [!NOTE]
> OData is different. With the Dataverse Web API, `$orderby` sorts rows using the integer value of the choice column rather than the localized label.



### Avoid ordering by columns in related tables

Ordering by columns on related tables makes the query slower because of the added complexity.

Ordering by related tables should only be done when needed to as described here:

- [Order rows using FetchXml](../fetchxml/order-rows.md)
- [Order rows using QueryExpression](../org-service/queryexpression/order-rows.md)
- [Order rows using OData](../webapi/query/order-rows.md)

### Avoid using conditions on large text columns

Dataverse has two types of columns that can store large strings of text:

- [StringAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.stringattributemetadata) can store up to 4,000 characters.
- [MemoAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.memoattributemetadata) can store a higher number.

The limit for both of these columns is specified using the `MaxLength` property.

You can use conditions on string columns that have a `MaxLength` configured for fewer than 850 characters.

All memo columns or string columns with a `MaxLength` greater than 850 are defined in Dataverse as large text columns. Large text columns are too large to effectively index, which leads to bad performance when included in a filter condition.

[Dataverse search](../search/overview.md) is a better choice to query data in these kinds of columns.