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

> [!IMPORTANT]
> We strongly discourage returning all columns in a table. Returning all columns will make your applications run slower and may cause timeout errors. You should specify the minimum number of columns to retrieve with your data. If you set the [ColumnSet.AllColumns property](xref:Microsoft.Xrm.Sdk.Query.ColumnSet.AllColumns) to true, data for all columns is returned. If you set no columns, only the primary key value for the record is returned. This is [opposite of the behavior using FetchXml, where all columns are returned if you don't specify any](../../fetchxml/select-columns.md).

Use the [ColumnSet class](xref:Microsoft.Xrm.Sdk.Query.ColumnSet) to specify the names for the columns to return with your query. Use the [AttributeMetadata.LogicalName](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.LogicalName) value for each column. These are always lower-case.

You can specify the columns with the [ColumnSet(String[]) constructor](/dotnet/api/microsoft.xrm.sdk.query.columnset.-ctor#microsoft-xrm-sdk-query-columnset-ctor(system-string())) when you initialize the `QueryExpression`.

```csharp
QueryExpression query = new("account")
{
    ColumnSet = new ColumnSet("name", "accountclassificationcode", "createdby", "createdon")
};
```

And you can use the [ColumnSet.AddColumn](xref:Microsoft.Xrm.Sdk.Query.ColumnSet.AddColumn%2A) or [ColumnSet.AddColumns](xref:Microsoft.Xrm.Sdk.Query.ColumnSet.AddColumns%2A) methods to add additional columns to the [QueryExpression.ColumnSet property](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.ColumnSet) after the `QueryExpression` is initialized.

```csharp
QueryExpression query = new("account");
query.ColumnSet.AddColumn("name");
query.ColumnSet.AddColumns("accountclassificationcode", "createdby", "createdon");
```

> [!NOTE]
> Some columns are not valid for read. The [AttributeMetadata.IsValidForRead](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.IsValidForRead) indicates whether a columns is valid for read. If you include the names for these columns, no values are returned.
> 
> The [ColumnSet.Columns property](xref:Microsoft.Xrm.Sdk.Query.ColumnSet.Columns) is a [Microsoft.Xrm.Sdk.DataCollection&lt;string&gt;](xref:Microsoft.Xrm.Sdk.DataCollection%601) that extends [System.Collections.ObjectModel.Collection&lt;T&gt; class](xref:System.Collections.ObjectModel.Collection%601), so you can also use the methods of those classes to interact with the strings in the collection.
> 
> Unlike FetchXml, the `ColumnSet` class provides no capability to set arbitrary alias values for columns when retrieving data without aggregation. When aggregating data, you can specify aliases using the [ColumnSet.AttributeExpressions property](xref:Microsoft.Xrm.Sdk.Query.ColumnSet.AttributeExpressions). [Learn more about aggregating data using QueryExpression](aggregate-data.md)


## Early bound field classes

If you are using early-bound field classes generated using the [pac modelbuilder command](/power-platform/developer/cli/reference/modelbuilder) with the [emitfieldsclasses](/power-platform/developer/cli/reference/modelbuilder#--emitfieldsclasses--efc) switch enabled, you can use the generated constants for all the field names rather than using the logical names directly as strings.

```csharp
QueryExpression query = new(Account.EntityLogicalName)
{
   ColumnSet = new ColumnSet(
      Account.Fields.Name, 
      Account.Fields.AccountClassificationCode,
      Account.Fields.CreatedBy, Account.Fields.CreatedOn)
};
```

This helps avoid runtime errors due to typing the wrong name. Learn more about:

- [Generating early-bound classes for the SDK for .NET](../generate-early-bound-classes.md) 
- [Late-bound and early-bound programming using the SDK for .NET](../early-bound-programming.md)



<!-- 
   How to use ColumnSet
    - Using generated constants from pac modelbuilder
    - Using Formatted values
    - Column Aliases?

 -->