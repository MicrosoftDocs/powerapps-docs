---
title: Methods to access results
description: Methods to access results
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

# Methods to access results

A stored procedure can return a code, values from Out parameters or the results of queries. To access these results, use the following patterns:

## Formulas for different controls

Typical formulas for views and stored procedures

| Control | Property |  Formula| Description |
| --- | --- | --- | --- | 
|Gallery or Table |Items  |`Data Source`|This is your view data source can be further refined with a [Filter](/power-platform/power-fx/reference/function-filter-lookup) and a [StartsWith](/power-platform/power-fx/reference/function-startswith).  The other generated query clauses are ‘anded’ onto the existing query.
|Form |DataSource  |`Data Source`|The **view data source**..
|Submit Button/Icon on a form|[OnSelect](/power-apps/maker/canvas-apps/controls/properties-core)  |`Data source’.dboSPName({ args}); Refresh (‘Data Source’)`|The first Data Source in this formula is the **stored procedure data source** – the one that holds your stored procedure.  The Data Source in the refresh formula is the view data source.  .
|Delete Button/Icon on a form.  |[OnSelect](/power-apps/maker/canvas-apps/controls/properties-core)  |`SP Data source’.dboSPName({ args}); Refresh (‘View Data Source’)`|The first Data Source in this formula is the **stored procedure data source** – the one that holds your stored procedure. The Data Source in the refresh formula is the **view data source**.  

## Return code

```power-fx
<datasourceName>.<StoredprocedureName>({<paramName1: value, paramName2: value, ... >}).ReturnCode
```

Use this for accessing the results of a return statement.

## Output parameters

```power-fx
<datasourceName>.<StoredprocedureName>({<paramName1: value, paramName2: value, ... >}).OutputParameters.<parameterName>
```

Take note to use the parameter name as it appears in the JSON payload.

## Result Sets

```power-fx
<datasourceName>.<StoredprocedureName>({<paramName1: value, paramName2: value, ... >}).ResultSets.Table1
```

Other tables can be accessed via their name (for example, Table1, Table2, Table3, ... )

## Untyped results

Some complicated stored procedures return an untyped result. These results aren't accessible directly. You must first provide a type. You can access the data using the following pattern.

In this example, we first pull the results into a variable named "MyUntypedObject". Then we pull `Table1` from that variable and put it into a variable named `table1`. This step isn't strictly necessary. It's useful however to put all the results in a variable at a point in time and then pull out the parts you need. Then, we iterate through table1 and extract the JSON elements in named value pairs. Be sure to match the names with the names that are returned in the JSON payload. To validate, open a Power Apps monitor and look at the body section the data node for a record.

```power-fx
Set(
    <MyUntypedObject>,
    <datasourceName>.<StoredprocedureName>( 
      { <paramName1>: "someString" }
    ).ResultSets
);
Set(
    table1,
    <MyUntypedObject>.Table1
);
Set(
    TypedTable,
    ForAll(
        table1,
        {
            BookID: Value(ThisRecord.BookID),
            BookName: Text(ThisRecord.BookName)
        }
    )
);

```

