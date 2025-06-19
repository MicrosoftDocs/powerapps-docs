---
title: View results in SQL Server
description: "Learn more about how to view the results of stored procedures from SQL Server in Microsoft Power Apps."
author: lancedMicrosoft

ms.topic: reference
ms.custom: canvas
ms.date: 10/25/2024
ms.subservice: canvas-maker
ms.author: lanced
ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
  - lancedmicrosoft
---

# View results in SQL Server

If you're using a direct table access pattern or a view, the query result is bound to the control or table. Power Fx automatically enables the paging of data in your app into the gallery or table. However, stored procedures can return a query result, a return code, or values from `Out` parameters.

To use these varying result types in your application, use the following patterns.

## Formulas for different controls

Typical formulas for views and stored procedures:

| Control | Property |  Formula| Description |
| ------- | -------- | ------- | ----------- |
| Gallery or Table | Items | `DataSource` | The table or view data source can be further refined with a [Filter](/power-platform/power-fx/reference/function-filter-lookup) and a [StartsWith](/power-platform/power-fx/reference/function-startswith). The other generated query clauses are appended onto the existing query. |
| Form | DataSource | `DataSource` | The table or view data source |
| Submit button on a form | [OnSelect](/power-apps/maker/canvas-apps/controls/properties-core) | `DataSource.dboSPName({ args}); Refresh (‘DataSource’)` | The first `DataSource` in this formula is the stored procedure data source—the one that holds your stored procedure. The `DataSource` in the refresh formula is the view data source. |
| Delete button on a form | [OnSelect](/power-apps/maker/canvas-apps/controls/properties-core) | `SP DataSource.dboSPName({ args}); Refresh (‘View DataSource’)` | The first `DataSource` in this formula is the stored procedure data source—the one that holds your stored procedure. The `DataSource` in the refresh formula is the view data source. |

## Return code

Use this return code for accessing the results of a return statement.

```power-fx
<datasourceName>.<StoredprocedureName>({<paramName1: value, paramName2: value, ... >}).ReturnCode
```

## Output parameters

Use the parameter name as it appears in the JSON payload.

```power-fx
<datasourceName>.<StoredprocedureName>({<paramName1: value, paramName2: value, ... >}).OutputParameters.<parameterName>
```

## Result Sets

Other tables can be accessed through their name, for example, `Table1`, `Table2`, or `Table3`.

```power-fx
<datasourceName>.<StoredprocedureName>({<paramName1: value, paramName2: value, ... >}).ResultSets.Table1
```

## Dynamic results

Some complicated stored procedures return dynamic results. This result is common for stored procedures that use temporary tables. Power Apps can't easily determine the results ahead of time. Therefore, the return is marked as *dynamic* and you can't access these results directly. You must first provide a type.

You can access the data with the following data access example pattern.

### Data access example

1. Pull the results into a variable named `MyDynamicValue`.
1. Pull `Table1` from that variable and put it into a variable named `table1`.

   > [!TIP]
   > This step isn't strictly necessary. It's useful however to put all the results in a variable and then pull out the parts you need, later.
1. Iterate through `table1` and extract the JSON elements in named value pairs.
1. Match the names with names returned in the JSON payload.
1. To validate, open a Power Apps monitor and look at the body section of the data node for a record.

```power-fx
Set(
    <MyDynamicValue>, // pull results into variable
    <datasourceName>.<StoredprocedureName>( 
      { <paramName1>: "someString" }
    ).ResultSets
);
Set(
    table1, // put Table1 into table1
    <MyDynamicValue>.Table1
);
Set(
    TypedTable,
    ForAll(
        table1, // extract JSON from table1
        {
            BookID: Value(ThisRecord.BookID),
            BookName: Text(ThisRecord.BookName)
        }
    )
);

```
