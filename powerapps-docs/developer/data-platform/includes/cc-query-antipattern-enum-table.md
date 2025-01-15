The `{0}` part of the exception message lists the anti-pattern that the query is using. If there are multiple anti-patterns used by the query, they're comma separated. For example, if a query is filtering on a large text column and is also selecting a large number of columns, the exception message contains the string `PerformanceLargeColumnSearch,LargeAmountOfAttributes`. The following table lists the anti-patterns with links to explanations:

|Anti-pattern identifier|Explanation link|
|---|---|
|`PerformanceLeadingWildCard`|[Avoid leading wild cards in filter conditions](../query-antipatterns.md#PerformanceLeadingWildCard)|
|`PerformanceLargeColumnSearch`|[Avoid using conditions on large text columns](../query-antipatterns.md#PerformanceLargeColumnSearch)|
|`OrderOnEnumAttribute`|[Avoid ordering by choice columns](../query-antipatterns.md#OrderOnEnumAttribute)|
|`OrderOnPropertiesFromJoinedTables`|[Avoid ordering by columns in related tables](../query-antipatterns.md#OrderOnPropertiesFromJoinedTables)|
|`LargeAmountOfAttributes`|[Minimize the number of selected columns](../query-antipatterns.md#LargeAmountOfAttributes)|
|`LargeAmountOfLogicalAttributes`|[Minimize the number of selected logical columns](../query-antipatterns.md#LargeAmountOfLogicalAttributes)|
|`FilteringOnCalculatedColumns`|[Avoid using formula or calculated columns in filter conditions](../query-antipatterns.md#FilteringOnCalculatedColumns)|
