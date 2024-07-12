---
title: Select columns using QueryExpression
description: Learn how to use QueryExpression to select columns when you retrieve data from Microsoft Dataverse.
ms.date: 05/12/2024
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
> We strongly discourage returning all columns in a table with your query. Returning all columns will make your applications run slower and may cause timeout errors. You should specify the minimum number of columns to retrieve with your data. If you set the [ColumnSet.AllColumns property](xref:Microsoft.Xrm.Sdk.Query.ColumnSet.AllColumns) to true, data for all columns is returned. If you set no columns, only the primary key value for the record is returned. This is [opposite of the behavior using FetchXml, where all columns are returned if you don't specify any](../../fetchxml/select-columns.md).

Use the [ColumnSet class](xref:Microsoft.Xrm.Sdk.Query.ColumnSet) to specify the names for the columns to return with your query. Use the [AttributeMetadata.LogicalName](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.LogicalName) value for each column. Logical name values are always lower-case.

You can specify the columns with the [ColumnSet(String[]) constructor](/dotnet/api/microsoft.xrm.sdk.query.columnset.-ctor#microsoft-xrm-sdk-query-columnset-ctor(system-string())) when you initialize the `QueryExpression`:

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
> Some columns are not valid for read. The [AttributeMetadata.IsValidForRead property](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.IsValidForRead) indicates whether a column is valid for read. If you include the names for these columns, no values are returned.
> 
> The [ColumnSet.Columns property](xref:Microsoft.Xrm.Sdk.Query.ColumnSet.Columns) is a [Microsoft.Xrm.Sdk.DataCollection&lt;string&gt;](xref:Microsoft.Xrm.Sdk.DataCollection%601) that extends [System.Collections.ObjectModel.Collection&lt;T&gt; class](xref:System.Collections.ObjectModel.Collection%601), so you can also use the methods of those base classes to interact with the strings in the collection.

### Select columns for joined tables

When you [Join tables using QueryExpression](join-tables.md), you use the [LinkEntity class](xref:Microsoft.Xrm.Sdk.Query.LinkEntity). The [LinkEntity.Columns property](xref:Microsoft.Xrm.Sdk.Query.LinkEntity.Columns) property is a [ColumnSet](xref:Microsoft.Xrm.Sdk.Query.ColumnSet), so you will define the columns to return for the joined tables in the same way.

## Early bound field classes

If you are using early-bound field classes generated using the [pac modelbuilder command](/power-platform/developer/cli/reference/modelbuilder) with the [emitfieldsclasses](/power-platform/developer/cli/reference/modelbuilder#--emitfieldsclasses--efc) switch enabled, you can use the generated constants for all the field names rather than using the logical names directly as strings.

```csharp
QueryExpression query = new(Account.EntityLogicalName)
{
   ColumnSet = new ColumnSet(
      Account.Fields.Name, 
      Account.Fields.AccountClassificationCode,
      Account.Fields.CreatedBy, 
      Account.Fields.CreatedOn)
};
```

This helps avoid runtime errors due to typing the wrong name. Learn more about:

- [Generating early-bound classes for the SDK for .NET](../generate-early-bound-classes.md) 
- [Late-bound and early-bound programming using the SDK for .NET](../early-bound-programming.md)


## Column aliases

Column aliases are typically used for [aggregate operations](aggregate-data.md), but they also work to retrieve rows, so we can introduce them here.

Add [XrmAttributeExpression](/dotnet/api/microsoft.xrm.sdk.query.xrmattributeexpression) instances to the [ColumnSet.AttributeExpressions](/dotnet/api/microsoft.xrm.sdk.query.columnset.attributeexpressions) collection to specify a unique column name for the results returned. For each instance, set these properties: 


|Property|Description|
|---------|---------|
|[AttributeName](/dotnet/api/microsoft.xrm.sdk.query.xrmattributeexpression.attributename)|The logical name of the column|
|[Alias](/dotnet/api/microsoft.xrm.sdk.query.xrmattributeexpression.alias)|A unique name for the column to appear in the results|
|[AggregateType](/dotnet/api/microsoft.xrm.sdk.query.xrmattributeexpression.aggregatetype)|When not aggregating data, use the [XrmAggregateType](/dotnet/api/microsoft.xrm.sdk.query.xrmaggregatetype)`.None` member. This is the default value, so you don't need to set it if you are not using aggregation. [Learn more about aggregating data with QueryExpression](aggregate-data.md)|

Each column returned must have a unique name. By default, the column names returned for the table of your query are the column `LogicalName` values. All column logical names are unique for each table, so there can't be any duplicate names within that set.

When you use a [LinkEntity](/dotnet/api/microsoft.xrm.sdk.query.linkentity) to [join tables](join-tables.md), you can set the [EntityAlias property](/dotnet/api/microsoft.xrm.sdk.query.linkentity.entityalias) for the `LinkEntity` representing the joined table. The column names in the [LinkEntity.Columns property](/dotnet/api/microsoft.xrm.sdk.query.linkentity.columns) follow this naming convention: `{Linked table LogicalName or alias}.{Column LogicalName}`. This prevents any duplicate column names.

However, when you specify a column alias using [XrmAttributeExpression.Alias property](/dotnet/api/microsoft.xrm.sdk.query.xrmattributeexpression.alias), the `LinkEntity.EntityAlias` or table logical name  value is not prepended to the alias value. You must make sure that the alias value is unique. If the value isn't unique, you can expect this error:

> Name: `QueryBuilderDuplicateAlias`<br />
> Code: `0x80041130`<br />
> Number: `-2147217104`<br />
> Message: `< alias value > is not a unique alias. It clashes with an autogenerated alias or user provided alias`

### Column aliases example

This `SimpleAliasOutput` example method uses aliases and logical names of the columns. Because of this, the results that use aliases are returned as <xref:Microsoft.Xrm.Sdk.AliasedValue>. To access the value of types like [OptionSetValue](xref:Microsoft.Xrm.Sdk.OptionSetValue) or [EntityReference](xref:Microsoft.Xrm.Sdk.EntityReference), you have to cast the value. 

In this example, aliases are specified only for the `accountclassificationcode`, `createdby`, and `createdon` columns. The `name` column doesn't use an alias. This method depends on the [ConsoleTables NuGet package](https://www.nuget.org/packages/ConsoleTables) to render the table.

```csharp
/// <summary>
/// Output the entity attribute values with aliases
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance</param>
static void SimpleAliasOutput(IOrganizationService service)
{
    QueryExpression query = new("account")
    {
        TopCount = 3,
        ColumnSet = new ColumnSet("name")
        {
            AttributeExpressions = {
                new XrmAttributeExpression{
                    AttributeName = "accountclassificationcode",
                    Alias = "classificationcode"
                 },
                 new XrmAttributeExpression{
                    AttributeName = "createdby",
                    Alias = "whocreated"
                 },
                 new XrmAttributeExpression{
                    AttributeName = "createdon",
                    Alias = "whencreated"
                 }
            }
        }
    };

    //Retrieve the data
    EntityCollection entityCollection = service.RetrieveMultiple(query: query);

    var table = new ConsoleTables.ConsoleTable("classificationcode", "whocreated", "whencreated", "name");

    foreach (var entity in entityCollection.Entities)
    {

        var code = ((OptionSetValue)entity.GetAttributeValue<AliasedValue>("classificationcode").Value).Value;
        var whocreated = ((EntityReference)entity.GetAttributeValue<AliasedValue>("whocreated").Value).Name;
        var whencreated = entity.GetAttributeValue<AliasedValue>("whencreated").Value;
        var companyname = entity.GetAttributeValue<string>("name");

        table.AddRow(code, whocreated, whencreated, companyname);

    }
    table.Write();
}
```

Output:

```text
 ----------------------------------------------------------------------------------
 | code | whocreated           | whencreated           | companyname              |
 ----------------------------------------------------------------------------------
 | 1    | FirstName LastName   | 8/13/2023 10:30:08 PM | Fourth Coffee (sample)   |
 ----------------------------------------------------------------------------------
 | 1    | FirstName LastName   | 8/13/2023 10:30:10 PM | Litware, Inc. (sample)   |
 ----------------------------------------------------------------------------------
 | 1    | FirstName LastName   | 8/13/2023 10:30:10 PM | Adventure Works (sample) |
 ----------------------------------------------------------------------------------
```

The [AliasedValue class](xref:Microsoft.Xrm.Sdk.AliasedValue) has two properties that tell you the original [EntityLogicalName](xref:Microsoft.Xrm.Sdk.AliasedValue.EntityLogicalName) and [AttributeLogicalName](xref:Microsoft.Xrm.Sdk.AliasedValue.AttributeLogicalName) if you need them.

## Aliased and formatted values example

[Columns that use an an alias return an AliasedValue](../entity-operations-query-data.md#columns-that-use-an-an-alias-return-an-aliasedvalue). As explained in [Access formatted values](../entity-operations-query-data.md#formatted-values-are-returned-for-some-columns), for some column types, formatted string values are also returned using the [Entity.FormattedValues collection](/dotnet/api/microsoft.xrm.sdk.entity.formattedvalues) to provide string values suitable for display in an application.

The following static `OutputQueryExpression` example method demonstrates how to extract string values for each row of data. This function uses the `QueryExpression.ColumnSet` data to know which columns are requested, and then processes the results to find the best way to display the record data in an app, in this case, a console application using the [ConsoleTables NuGet package](https://www.nuget.org/packages/ConsoleTables) to render a table.

```csharp
/// <summary>
/// Renders the output of a query in a table for a console application
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance to use.</param>
/// <param name="query">The query to use</param>
/// <exception cref="Exception">
/// OutputQueryExpression requires all LinkEntity instances that contain columns specify an EntityAlias property.
/// </exception>
static void OutputQueryExpression(IOrganizationService service, QueryExpression query)
{
    //Retrieve the data
    EntityCollection entityCollection = service.RetrieveMultiple(query: query);

    var columns = GetQueryExpressionColumns(query);

    // Create the table using https://www.nuget.org/packages/ConsoleTables/2.5.0
    var table = new ConsoleTables.ConsoleTable(columns.ToArray());

    // Add the rows of the table
    entityCollection.Entities.ToList().ForEach(entity =>
    {
        table.Rows.Add(GetRowValues(columns, entity).ToArray());
    });

    // Write the table to the console
    table.Write();

    List<string> GetQueryExpressionColumns(QueryExpression query)
    {
        List<string> columns = new();

        columns.AddRange(GetColumns(query.ColumnSet));

        foreach (LinkEntity linkEntity in query.LinkEntities)
        {
            columns.AddRange(GetLinkEntityColumns(linkEntity));
        }

        return columns;
    }

    List<string> GetLinkEntityColumns(LinkEntity linkEntity)
    {
        if (string.IsNullOrWhiteSpace(linkEntity.EntityAlias))
        {
            if (linkEntity.Columns.Columns.Count != 0)
            {
                string message = "OutputQueryExpression method requires all ";
                message += "LinkEntity instances that contain columns ";
                message += "specify an EntityAlias property.";

                throw new Exception(message);
            }
        }

        List<string> columns = new();

        columns.AddRange(GetColumns(linkEntity.Columns, linkEntity.EntityAlias));

        foreach (LinkEntity le in linkEntity.LinkEntities)
        {
            columns.AddRange(GetColumns(le.Columns, le.EntityAlias));
        }
        return columns;
    }

    List<string> GetColumns(ColumnSet columnset, string alias = null)
    {
        List<string> columns = new();

        foreach (string column in columnset.Columns)
        {
            columns.Add(string.IsNullOrWhiteSpace(alias) ? column : $"{alias}.{column}");
        }

        foreach (XrmAttributeExpression item in columnset.AttributeExpressions)
        {
            columns.Add(item.Alias ?? item.AttributeName);
        }

        return columns;
    }

    List<string> GetRowValues(List<string> columns, Entity entity)
    {
        List<string> values = new();
        columns.ForEach(column =>
        {
            if (entity.Attributes.ContainsKey(column))
            {
                // Use the formatted value if it available
                if (entity.FormattedValues.ContainsKey(column))
                {
                    values.Add($"{entity.FormattedValues[column]}");
                }
                else
                {
                    // When an alias is used, the Aliased value must be converted
                    if (entity.Attributes[column] is AliasedValue aliasedValue)
                    {
                        values.Add($"{aliasedValue.Value}");
                    }
                    else
                    {
                        // Use the simple attribute value
                        values.Add($"{entity.Attributes[column]}");
                    }
                }
            }
            // Null values are not in the Attributes collection
            else
            {
                values.Add("NULL");
            }

        });
        return values;
    }
}
```

You can use this function to show the output of any `QueryExpression` query with the only requirement being that any [LinkEntity](xref:Microsoft.Xrm.Sdk.Query.LinkEntity) used to join tables specify an alias. For example the following query includes aliased and formatted values with a joined table:

```csharp
static void OutputQueryExpressionExample(IOrganizationService service)
{
    // Specify a query:
    QueryExpression query = new("account")
    {
        TopCount = 3,
        ColumnSet = new ColumnSet("name")
        {
            AttributeExpressions = {
                new XrmAttributeExpression{
                    AttributeName = "accountclassificationcode",
                    Alias = "classificationcode"
                 }
            }
        },
        LinkEntities = {
            new LinkEntity()
            {
                LinkFromEntityName = "account",
                LinkToEntityName = "contact",
                LinkFromAttributeName = "primarycontactid",
                LinkToAttributeName = "contactid",
                JoinOperator = JoinOperator.Inner,
                EntityAlias = "person",
                Columns = new ColumnSet("fullname"){
                    AttributeExpressions = {
                    new XrmAttributeExpression{
                        AttributeName = "accountrolecode",
                        Alias = "role"
                        }
                    }
                }
            }
        }
    };

    // Use OutputQueryExpression
    OutputQueryExpression(service, query);
}
```

The results of this query might look like this:

```
 ----------------------------------------------------------------------------
 | name             | classificationcode | person.fullname | role           |
 ----------------------------------------------------------------------------
 | Fourth Coffee    | Large              | Susie Curtis    | Influencer     |
 ----------------------------------------------------------------------------
 | Litware, Inc.    | Medium             | Adele Vance     | Decision Maker |
 ----------------------------------------------------------------------------
 | Adventure Works  | Small              | Rafel Shillo    | Employee       |
 ----------------------------------------------------------------------------
```

## Next steps

Learn how to join tables.

> [!div class="nextstepaction"]
> [Join tables](join-tables.md)
