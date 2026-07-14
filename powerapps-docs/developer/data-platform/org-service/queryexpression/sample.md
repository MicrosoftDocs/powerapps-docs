---
title: QueryExpression Sample code
description: Try using QueryExpression to retrieve Dataverse data using this sample code.
ms.date: 12/04/2024
ms.reviewer: jdaly
ms.topic: how-to
author: MsSQLGirl
ms.subservice: dataverse-developer
ms.author: jukoesma
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - dmitmikh
 - dasussMS
---
# QueryExpression sample code

To try using QueryExpression with C#, you can use the `OutputQueryExpression` static method in this article by adapting the [Quickstart: Execute an SDK for .NET request (C#)](../quick-start-org-service-console-app.md).

> [!NOTE]
> See [Paging Cookie example](page-results.md#paging-cookie-example) for sample code to retrieve data in pages.

You can use the following `OutputQueryExpression` static method to test QueryExpression queries in a console application.

The `OutputQueryExpression` method demonstrates how to use the [QueryExpression class](xref:Microsoft.Xrm.Sdk.Query.QueryExpression) and the [IOrganizationService.RetrieveMultiple method](xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A) to return an [EntityCollection](xref:Microsoft.Xrm.Sdk.EntityCollection) containing the requested data.

The `OutputQueryExpression` method depends on the [ConsoleTables NuGet package](https://www.nuget.org/packages/ConsoleTables/2.5.0) and requires that all all [LinkEntity](xref:Microsoft.Xrm.Sdk.Query.LinkEntity) instances that contain columns specify an [EntityAlias](xref:Microsoft.Xrm.Sdk.Query.LinkEntity.EntityAlias).

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

    //Get column names from the query
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

    // Get a list of column names from the query
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

    // Get column names from any linked tables
    List<string> GetLinkEntityColumns(LinkEntity linkEntity)
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

        columns.AddRange(GetColumns(linkEntity.Columns, linkEntity.EntityAlias));

        foreach (LinkEntity le in linkEntity.LinkEntities)
        {
            columns.AddRange(GetColumns(le.Columns, le.EntityAlias));
        }
        return columns;
    }

    // Get columns from a columnset
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

    // Get the values of a row as strings
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
                        // When an EntityReference doesn't have a Name, show the Id
                        if (aliasedValue.Value is EntityReference lookup &&
                        string.IsNullOrWhiteSpace(lookup.Name))
                        {
                            values.Add($"{lookup.Id:B}");
                        }
                        else
                        {
                            values.Add($"{aliasedValue.Value}");
                        }
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

### Update SDK for .NET quick start sample

You can adapt the [Quick Start: Execute an SDK for .NET request (C#)](../quick-start-org-service-console-app.md) sample to test queries with the following steps:

1. Install the [ConsoleTables NuGet package](https://www.nuget.org/packages/ConsoleTables/2.5.0)
1. Add the following using statements at the top of the `program.cs` file

    ```csharp
    using Microsoft.Xrm.Sdk;
    using Microsoft.Xrm.Sdk.Query;
    using System.Text;
    using System.Xml.Linq;
    ```

1. Copy and paste the `OutputQueryExpression` method below the `Main` method.
1. Edit the `Main` method to set your query and use the `OutputQueryExpression` method.

    ```csharp
        static void Main(string[] args)
        {
            using (ServiceClient serviceClient = new(connectionString))
            {
                if (serviceClient.IsReady)
                {
                    //WhoAmIResponse response = 
                    //    (WhoAmIResponse)serviceClient.Execute(new WhoAmIRequest());

                    //Console.WriteLine("User ID is {0}.", response.UserId);

                     QueryExpression query = new("account")
                     {
                        TopCount = 5,
                        ColumnSet = new ColumnSet(
                           "accountclassificationcode", 
                           "createdby", 
                           "createdon", 
                           "name")
                     };

                    OutputQueryExpression(serviceClient, query);
                }
                else
                {
                    Console.WriteLine(
                        "A web service connection was not established.");
                }
            }

            // Pause the console so it does not close.
            Console.WriteLine("Press the <Enter> key to exit.");
            Console.ReadLine();
        }
    ```

Read the following important information about using a connection string in application code.
[!INCLUDE [cc-connection-string](../../includes/cc-connection-string.md)]

When you run the program using the `OutputQueryExpression` method, the output should look like this:

```text
 ---------------------------------------------------------------------------------------------------------
 | accountclassificationcode | createdby          | createdon          | name                             |
 ---------------------------------------------------------------------------------------------------------
 | Default Value             | FirstName LastName | 3/25/2023 10:42 AM | Litware, Inc. (sample)           |
 ---------------------------------------------------------------------------------------------------------
 | Default Value             | FirstName LastName | 3/25/2023 10:42 AM | Adventure Works (sample)         |
 ---------------------------------------------------------------------------------------------------------
 | Default Value             | FirstName LastName | 3/25/2023 10:42 AM | Fabrikam, Inc. (sample)          |
 ---------------------------------------------------------------------------------------------------------
 | Default Value             | FirstName LastName | 3/25/2023 10:42 AM | Blue Yonder Airlines (sample)    |
 ---------------------------------------------------------------------------------------------------------
 | Default Value             | FirstName LastName | 3/25/2023 10:42 AM | City Power & Light (sample)      |
 ---------------------------------------------------------------------------------------------------------
```

### Related articles

[Query data using QueryExpression](overview.md)  
[Sample: Retrieve multiple with the QueryExpression class](../samples/retrieve-multiple-queryexpression-class.md)  
[Sample: Use QueryExpression with a paging cookie](../samples/use-queryexpression-with-a-paging-cookie.md)
