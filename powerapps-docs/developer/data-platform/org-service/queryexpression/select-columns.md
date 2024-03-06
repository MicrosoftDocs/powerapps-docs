---
title: Select columns using QueryExpression
description: Learn how to use QueryExpression to select columns when you retrieve data from Microsoft Dataverse.
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
# Select columns using QueryExpression

As described in [Query data using QueryExpression](overview.md), start your query by selecting a table using the [QueryExpression.EntityName property](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.EntityName), typically with the [QueryExpression(String) constructor](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.-ctor#microsoft-xrm-sdk-query-queryexpression-ctor(system-string)).

Use the [ColumnSet class](xref:Microsoft.Xrm.Sdk.Query.ColumnSet) to specify the logical names for the columns to return with your query. For example:

```csharp
QueryExpression query = new("account")
{
    ColumnSet = new ColumnSet("name", "accountclassificationcode", "createdby", "createdon")
};
```

> [!IMPORTANT]
> We strongly discourage returning all columns in a table. Returning all columns will make your applications run slower and may cause timeout errors. You should specify the minimum number of columns to retrieve with your data. If you set the [ColumnSet.AllColumns property](xref:Microsoft.Xrm.Sdk.Query.ColumnSet.AllColumns) to true, data for all columns is returned. If you set no columns, only the primary key value for the record is returned.

If you are using early-bound classes generated using the [pac modelbuilder command](/power-platform/developer/cli/reference/modelbuilder) with the [emitfieldsclasses](/power-platform/developer/cli/reference/modelbuilder#--emitfieldsclasses--efc) switch enabled, you can use the generated constants for all the field names rather than using the logical names directly as strings.

```csharp
QueryExpression query = new(Account.EntityLogicalName)
{
   ColumnSet = new ColumnSet(
      Account.Fields.Name, 
      Account.Fields.AccountClassificationCode,
      Account.Fields.CreatedBy, Account.Fields.CreatedOn)
};
```

This helps avoid runtime errors. Learn more about:

- [Generating early-bound classes for the SDK for .NET](../generate-early-bound-classes.md) 
- [Late-bound and early-bound programming using the SDK for .NET](../early-bound-programming.md)

> [!NOTE]
> Unlike FetchXml, the `ColumnSet` class provides no capability to set arbitrary alias values for columns when retrieving data without aggregation. When aggregating data, you can specify aliases using the [ColumnSet.AttributeExpressions property](xref:Microsoft.Xrm.Sdk.Query.ColumnSet.AttributeExpressions). [Learn more about aggregating data using QueryExpression](aggregate-data.md)


<!-- 
   How to use ColumnSet
    - Using generated constants from pac modelbuilder
    - Using Formatted values
    - Column Aliases?

 -->