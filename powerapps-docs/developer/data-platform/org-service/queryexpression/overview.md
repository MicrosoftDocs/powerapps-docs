---
title: Use QueryExpression to query data
description: Learn to compose a query using QueryExpression, an object model that is used in Microsoft Dataverse to compose queries to retrieve data.
ms.date: 02/29/2024
ms.reviewer: jdaly
ms.topic: how-to
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Query data using QueryExpression
<!-- Does not replace entity-operations-query-data.md -->
<!-- Replaces build-queries-with-queryexpression.md -->

The [QueryExpression class](xref:Microsoft.Xrm.Sdk.Query.QueryExpression), together with other classes in the [Microsoft.Xrm.Sdk.Query namespace](xref:Microsoft.Xrm.Sdk.Query), provides an object model to compose queries to retrieve records from Dataverse. [Compare options when querying data using the SDK for .NET](../entity-operations-query-data.md)


## Compose a query

Use the object model `QueryExpression` provides to compose queries that you can manipulate without depending on string manipulation using FetchXml.

All queries are based on a single table. Use the `QueryExpression` class to select the table the query retrieves data from. The following example represents a simple `QueryExpression` query:

```csharp
QueryExpression query = new("account")
{
      ColumnSet = new ColumnSet("name"),
      TopCount = 5
};

EntityCollection results = service.RetrieveMultiple(query);
```

This query returns the [Name column](../../reference/entities/account.md#BKMK_Name) of the first five rows from the [Account table](../../reference/entities/account.md).

- Specify the table as the [QueryExpression.EntityName property](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.EntityName)  using the <xref:Microsoft.Xrm.Sdk.Query.QueryExpression(System.String)?displayProperty=fullName> constructor.
- Specify the columns to return by setting the [QueryExpression.ColumnSet](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.ColumnSet) by instantiating a new [ColumnSet](xref:Microsoft.Xrm.Sdk.Query.ColumnSet) and passing one or more column [LogicalName](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.LogicalName) values to the <xref:Microsoft.Xrm.Sdk.Query.ColumnSet.%23ctor%2A?displayProperty=fullName> constructor.
- Limit the number of records returned by setting the [QueryExpression.TopCount property](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.TopCount)

You can compose the same query without the <xref:Microsoft.Xrm.Sdk.Query.QueryExpression(System.String)?displayProperty=fullName> constructor or object initialization pattern and just set the properties to the instantiated instance as shown in the following example:

```csharp
QueryExpression query = new();
query.EntityName = "account";
query.ColumnSet = new ColumnSet();
query.ColumnSet.AddColumn("name");
query.TopCount = 5;
```

This example uses the [ColumnSet.AddColumn method](xref:Microsoft.Xrm.Sdk.Query.ColumnSet.AddColumn*). Classes in the [Microsoft.Xrm.Sdk.Query namespace](xref:Microsoft.Xrm.Sdk.Query) frequently have methods like this to enable common operations.

Examples in our documentation will use a combination of both patterns. As queries become more complex, the object initialization pattern can become unwieldy. You can always define the query properties separately and add them to the query by setting the properties or using the available methods.

## Limit the number of rows

## Return distinct results

## Retrieve Data

## Refine your query

## Limitations

<!-- Include the things that Query Expression can't do compared to FetchXml -->

## Community tools

## Use QueryExpression as a message parameter

## Next steps
