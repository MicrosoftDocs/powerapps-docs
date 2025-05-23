## Limitations

Queries that return aggregate values are limited to 50,000 records. This limit helps maintain system performance and reliability. If the filter criteria in your query returns more than 50,000 records, you get the following error:

> Number: `-2147164125`  
> Code: `8004E023`  
> Message: `AggregateQueryRecordLimit exceeded. Cannot perform this operation.`  
> Client error message: The maximum record limit is exceeded. Reduce the number of records.

To avoid this error, add appropriate filters to your query to make sure it doesn't evaluate more than 50,000 records. Then run your query multiple times and combine the results. Appropriate filters depend on the nature of your data, but they could be a date range or a subset of values in a choice column.