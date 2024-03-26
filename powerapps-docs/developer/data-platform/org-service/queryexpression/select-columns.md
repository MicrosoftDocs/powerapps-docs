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
> We strongly discourage returning all columns in a table with your query. Returning all columns will make your applications run slower and may cause timeout errors. You should specify the minimum number of columns to retrieve with your data. If you set the [ColumnSet.AllColumns property](xref:Microsoft.Xrm.Sdk.Query.ColumnSet.AllColumns) to true, data for all columns is returned. If you set no columns, only the primary key value for the record is returned. This is [opposite of the behavior using FetchXml, where all columns are returned if you don't specify any](../../fetchxml/select-columns.md).

Use the [ColumnSet class](xref:Microsoft.Xrm.Sdk.Query.ColumnSet) to specify the names for the columns to return with your query. Use the [AttributeMetadata.LogicalName](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.LogicalName) value for each column. Logical Name values are always lower-case.

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
> Some columns are not valid for read. The [AttributeMetadata.IsValidForRead](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.IsValidForRead) indicates whether a columns is valid for read. If you include the names for these columns, no values are returned.
> 
> The [ColumnSet.Columns property](xref:Microsoft.Xrm.Sdk.Query.ColumnSet.Columns) is a [Microsoft.Xrm.Sdk.DataCollection&lt;string&gt;](xref:Microsoft.Xrm.Sdk.DataCollection%601) that extends [System.Collections.ObjectModel.Collection&lt;T&gt; class](xref:System.Collections.ObjectModel.Collection%601), so you can also use the methods of those base classes to interact with the strings in the collection.
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
      Account.Fields.CreatedBy, 
      Account.Fields.CreatedOn)
};
```

This helps avoid runtime errors due to typing the wrong name. Learn more about:

- [Generating early-bound classes for the SDK for .NET](../generate-early-bound-classes.md) 
- [Late-bound and early-bound programming using the SDK for .NET](../early-bound-programming.md)

## Select columns for joined tables

When you [Join tables using QueryExpression](join-tables.md), you use the [LinkEntity class](xref:Microsoft.Xrm.Sdk.Query.LinkEntity). The [LinkEntity.Columns property](xref:Microsoft.Xrm.Sdk.Query.LinkEntity.Columns) property is a [ColumnSet](xref:Microsoft.Xrm.Sdk.Query.ColumnSet), so you will define the columns to return for the joined tables in the same way.

## Formatted values

The typed data returned may not be suitable to display in your application. Formatted values are string values returned with the request that you can display in your application.

Let's look at the results *without* using formatted values first.

This `SimpleOutput` method only accesses values in the [Entity.Attributes collection](xref:Microsoft.Xrm.Sdk.Entity.Attributes).

```csharp
/// <summary>
/// Output the entity attribute values
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance</param>
static void SimpleOutput(IOrganizationService service)
{
    QueryExpression query = new("account")
    {
        TopCount = 3,
        ColumnSet = new ColumnSet("accountclassificationcode", "createdby", "createdon", "name")
    };

    //Retrieve the data
    EntityCollection entityCollection = service.RetrieveMultiple(query: query);

    var table = new ConsoleTables.ConsoleTable("classificationcode", "createdby", "createdon", "name");

    foreach (var entity in entityCollection.Entities)
    {
        var accountclassificationcode = entity.GetAttributeValue<OptionSetValue>("accountclassificationcode").Value;
        var createdby = entity.GetAttributeValue<EntityReference>("createdby").Name;
        var createdon = entity.GetAttributeValue<DateTime>("createdon");
        var name = entity.GetAttributeValue<string>("name");

        table.AddRow(accountclassificationcode, createdby, createdon, name);

    }
    table.Write();
}
```

**Output**:

```text
 ----------------------------------------------------------------------------------------------
 | classificationcode | createdby           | createdon             | name                    |
 ----------------------------------------------------------------------------------------------
 | 1                  | FirstName LastName  | 8/13/2023 10:30:08 PM | Fourth Coffee (sample)  |
 ----------------------------------------------------------------------------------------------
 | 1                  | FirstName LastName  | 8/13/2023 10:30:10 PM | Litware, Inc. (sample)  |
 ----------------------------------------------------------------------------------------------
 | 1                  | FirstName LastName  | 8/13/2023 10:30:10 PM | Adventure Works (sample)|
 ----------------------------------------------------------------------------------------------
```

These values may not be the user-friendly values you need to display in an application.

- The `accountclassificationcode` choice column returns the integer value.
- The SDK reference to `createdby` must use the [EntityReference.Name property](xref:Microsoft.Xrm.Sdk.EntityReference.Name)

To get the user-friendly values you want, you need to access *formatted values* that can be returned by Dataverse. This static `OutputQueryExpressionRequest` method shows how to access the formatted values. It uses the [ConsoleTables NuGet package](https://www.nuget.org/packages/ConsoleTables/) to show the table in a console application and should render the results of any query you pass to it.

```csharp
/// <summary>
/// Renders the output of a query in a table for a console application
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance to use.</param>
/// <param name="query">The query to use</param>
/// <exception cref="Exception">OutputQueryExpressionRequest requires all LinkEntity instances that contain columns specify an EntityAlias property.</exception>
static void OutputQueryExpressionRequest(IOrganizationService service, QueryExpression query)
{
    //Retrieve the data
    EntityCollection entityCollection = service.RetrieveMultiple(query: query);

    var columns = GetColumnsFromQueryExpression(query);

    // Create the table using https://www.nuget.org/packages/ConsoleTables/2.5.0
    var table = new ConsoleTables.ConsoleTable(columns.ToArray());

    // Add the rows of the table
    entityCollection.Entities.ToList().ForEach(entity =>
    {
        table.Rows.Add(GetRowValues(columns, entity).ToArray());
    });

    // Write the table to the console
    table.Write();

    static List<string> GetColumnsFromQueryExpression(QueryExpression query)
    {
        List<string> columns = new();

        if (query.ColumnSet.AttributeExpressions.Count == 0)
        {
            columns.AddRange(query.ColumnSet.Columns.ToList());

            foreach (LinkEntity linkEntity in query.LinkEntities)
            {

                columns.AddRange(GetColumnsFromLinkEntity(linkEntity));
            }
        }
        else
        {
            foreach (XrmAttributeExpression item in query.ColumnSet.AttributeExpressions)
            {
                if (item.Alias != null)
                {
                    columns.Add(item.Alias);
                }
                else
                {
                    columns.Add(item.AttributeName);
                }
            }
        }
        return columns;
    }

    static List<string> GetColumnsFromLinkEntity(LinkEntity linkEntity)
    {
        if (string.IsNullOrWhiteSpace(linkEntity.EntityAlias))
        {
            if (linkEntity.Columns.Columns.Count != 0)
            {
                string message = "OutputQueryExpressionRequest requires all ";
                message += "LinkEntity instances that contain columns ";
                message += "specify an EntityAlias property.";

                throw new Exception(message);
            }

        }

        List<string> columns = new();

        foreach (string column in linkEntity.Columns.Columns)
        {
            columns.Add($"{linkEntity.EntityAlias}.{column}");
        }

        foreach (LinkEntity le in linkEntity.LinkEntities)
        {
            columns.AddRange(GetColumnsFromLinkEntity(le));
        }
        return columns;

    }

    /// <summary>
    /// Returns the values of a row as strings
    /// </summary>
    /// <param name="columns">The names of the columns</param>
    /// <param name="entity">The entity with the data</param>
    /// <returns></returns>
    static List<string> GetRowValues(List<string> columns, Entity entity)
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

The `GetRowValues` method extracts a list of string values for a record from the [Entity.FormattedValues](xref:Microsoft.Xrm.Sdk.Entity.FormattedValues) when they are available.

With this method, the results of the query look like this:

```text
 --------------------------------------------------------------------------------------------------
 | accountclassificationcode | createdby           | createdon          | name                    |
 --------------------------------------------------------------------------------------------------
 | Default Value             | FirstName LastName  | 8/13/2023 10:30 PM | Fourth Coffee (sample)  |
 --------------------------------------------------------------------------------------------------
 | Default Value             | FirstName LastName  | 8/13/2023 10:30 PM | Litware, Inc. (sample)  |
 --------------------------------------------------------------------------------------------------
 | Default Value             | FirstName LastName  | 8/13/2023 10:30 PM | Adventure Works (sample)|
 --------------------------------------------------------------------------------------------------
```

[Learn more about formatted values](../entity-operations-query-data.md#access-formatted-values)


## Column aliases

Column aliases are typically used for [aggregate operations](aggregate-data.md), but they also work for simple select operations, so we can introduce them here.

Add [XrmAttributeExpression](/dotnet/api/microsoft.xrm.sdk.query.xrmattributeexpression) instances to the [ColumnSet.AttributeExpressions](/dotnet/api/microsoft.xrm.sdk.query.columnset.attributeexpressions) collection to specify a unique column name for the results returned. For each instance, set these properties: 

- [XrmAttributeExpression.AttributeName](/dotnet/api/microsoft.xrm.sdk.query.xrmattributeexpression.attributename): The logical name of the column
- [XrmAttributeExpression.Alias](/dotnet/api/microsoft.xrm.sdk.query.xrmattributeexpression.alias): The unique name for the column.
- [XrmAttributeExpression.AggregateType](/dotnet/api/microsoft.xrm.sdk.query.xrmattributeexpression.aggregatetype): When not aggregating data, use the [XrmAggregateType](/dotnet/api/microsoft.xrm.sdk.query.xrmaggregatetype)`.None` member. This is the default value, so you don't need to set it if you are not using aggregation.

Each column returned must have a unique name. By default, the column names returned for the table of your query are the column `LogicalName` values. All column logical names are unique for each table, so there can't be any duplicate names within that set.

When you use a [LinkEntity](/dotnet/api/microsoft.xrm.sdk.query.linkentity) to [join tables](join-tables.md), the default column names follow this naming convention: `{Linked table LogicalName}.{Column LogicalName}`.  This prevents any duplicate column names. You can override this by using a unique alias. You can also set the [EntityAlias](/dotnet/api/microsoft.xrm.sdk.query.linkentity.entityalias) property for the `LinkEntity` representing the joined table.

This `SimpleAliasOutput` method uses aliases rather than the logical names of the columns. Because of this, the results are returned as <xref:Microsoft.Xrm.Sdk.AliasedValue>. To access the value of complex types like [OptionSetValue](xref:Microsoft.Xrm.Sdk.OptionSetValue) or [EntityReference](xref:Microsoft.Xrm.Sdk.EntityReference), you have to cast the value.

This method uses the [ConsoleTables NuGet package](https://www.nuget.org/packages/ConsoleTables) .

```csharp
/// <summary>
/// Output the entity attribute values with aliases
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance</param>
static void SimpleAliasOutputQE(IOrganizationService service)
{
    QueryExpression query = new("account")
    {
        TopCount = 3,
        ColumnSet = new ColumnSet()
        {
            AttributeExpressions = {
                 new XrmAttributeExpression{
                    AttributeName = "accountclassificationcode",
                    Alias = "code"
                 },
                 new XrmAttributeExpression{
                    AttributeName = "createdby",
                    Alias = "whocreated"
                 },
                 new XrmAttributeExpression{
                    AttributeName = "createdon",
                    Alias = "whencreated"
                 },
                 new XrmAttributeExpression{
                    AttributeName = "name",
                    Alias = "companyname"
                 }
            }
        }
    };

    //Retrieve the data
    EntityCollection entityCollection = service.RetrieveMultiple(query: query);

    var table = new ConsoleTables.ConsoleTable("code", "whocreated", "whencreated", "companyname");

    foreach (var entity in entityCollection.Entities)
    {

        var code = ((OptionSetValue)entity.GetAttributeValue<AliasedValue>("code").Value).Value;
        var whocreated = ((EntityReference)entity.GetAttributeValue<AliasedValue>("whocreated").Value).Name;
        var whencreated = entity.GetAttributeValue<AliasedValue>("whencreated").Value;
        var companyname = entity.GetAttributeValue<AliasedValue>("companyname").Value;

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

> [!NOTE]
> The [AliasedValue class](xref:Microsoft.Xrm.Sdk.AliasedValue) has two properties that tell you the original [EntityLogicalName](xref:Microsoft.Xrm.Sdk.AliasedValue.EntityLogicalName) and [AttributeLogicalName](xref:Microsoft.Xrm.Sdk.AliasedValue.AttributeLogicalName) if you need them.

## Next steps

Learn how to join tables.

> [!div class="nextstepaction"]
> [Join tables](join-tables.md)
