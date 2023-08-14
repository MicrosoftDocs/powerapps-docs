---
title: Use FetchXml to query data
description: Learn to compose a query using FetchXml, a proprietary XML based language that is used in Microsoft Dataverse to retrieve data.
ms.date: 08/31/2023
ms.reviewer: jdaly
ms.topic: how-to
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
search.audienceType: 
  - developer
---
# Query data using FetchXml

FetchXml is a proprietary XML based query language used with Dataverse to retrieve data using either the Web API or the SDK for .NET. This article describes how to compose a query using FetchXml for both of these use cases. For more specific information, see the following articles:

|Use Case|More information|
|---------|---------|
|SDK for .NET|- [Query data using the SDK for .NET](../org-service/entity-operations-query-data.md) <br/>- [FetchExpression class](xref:Microsoft.Xrm.Sdk.Query.FetchExpression) <br/>- [RetrieveMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest) <br/>- [IOrganizationService.RetrieveMultiple method](xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A) <br/>|
|Web API|[Use FetchXml with Web API](../webapi/use-fetchxml-web-api.md)|

> [!NOTE]
> FetchXml is also used to define views for model-driven apps and some reporting capabilities. The [FetchXml schema](../fetchxml-schema.md) includes elements and attributes for these use cases which are not discussed here. More information: [Model-driven Apps developer guide: Customize views](../../model-driven-apps/customize-entity-views.md).

## Compose a query

All queries are based on a single table. When composing a query using FetchXml, the root element is [fetch](reference/fetch.md). Use the [entity element](reference/entity.md) to select the table the query will retrieve data from. The following example represents the simplest valid FetchXml query:

```xml
<fetch>
  <entity name='account' />
</fetch>
```

This query returns all columns of the first 5,000 rows from the [Account table](../reference/entities/account.md), using the table `LogicalName` to set the [entity](reference/entity.md) `name` attribute.

> [!NOTE]
> We strongly discourage returning all columns in a table. Returning all columns will make your applications run slower and may cause timeout errors.

After you have selected the table to start your query with, you need to refine the query to get the data you need. The following articles in this section explain how to complete your query.


|Article|Task|
|---------|---------|
|[Select columns](select-columns.md)|Specify which columns of data to return.|
|[Join tables](join-tables.md)|Specify which related tables to return in the results.|
|[Order rows](order-rows.md)|Specify the sort order of the rows to return.|
|[Filter rows](filter-rows.md)|Specify which rows of data to return.|
|[Page results](page-results.md)|Specify how many rows of data to return with each request.|
|[Aggregate data](aggregate-data.md)|How to group and aggregate the data returned.|
|[Count number of rows](count-rows.md)|How to get a count of the number of rows returned.|
|[Performance optimizations](optimize-performance.md)|How to optimize performance|

## Community tools

The [XrmToolbox](../community-tools.md#xrmtoolbox) [FetchXmlBuilder](https://fetchxmlbuilder.com/) is a free, essential tool to compose FetchXml requests.

> [!NOTE]
> Tools created by the community are not supported by Microsoft. If you have questions or issues with community tools, contact the publisher of the tool.

## Sample code

### [SDK for .NET](#tab/sdk)


With the SDK for .NET, you can use the following `OutputFetchRequest` static method, and the methods it depends on, to test FetchXml queries in a console application.

This method depends on the [ConsoleTables NuGet package](https://www.nuget.org/packages/ConsoleTables/2.5.0) and requires that every [entity](reference/entity.md) or [link-entity](reference/link-entity.md) element `attribute` elements are included, which is a best practice.

```csharp
/// <summary>
/// Renders the output of a query in a table for a console application
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance to use.</param>
/// <param name="fetchXml">The FetchXml query to use.</param>
static void OutputFetchRequest(IOrganizationService service, string fetchXml)
{
    FetchExpression fetchExpression = new(fetchXml);

    //Retrieve the data
    EntityCollection entityCollection = service.RetrieveMultiple(query: fetchExpression);

    // Get column names from the FetchXml
    List<string> columns = GetColumns(fetchXml);

    // Create the table using https://www.nuget.org/packages/ConsoleTables/2.5.0
    var table = new ConsoleTables.ConsoleTable(columns.ToArray());

    // Add the rows of the table
    entityCollection.Entities.ToList().ForEach(entity =>
    {
        table.Rows.Add(GetRowValues(columns, entity).ToArray());
    });

    // Write the table to the console
    table.Write();
}

/// <summary>
/// Get a list of column names from the FetchXml
/// </summary>
/// <param name="fetchXml">The fetchXml query</param>
/// <returns></returns>
/// <exception cref="Exception"></exception>
static List<string> GetColumns(string fetchXml)
{
    XDocument fetchDoc = XDocument.Parse(fetchXml);
           
    // There can only be one entity element
    XElement entityElement = fetchDoc.Root.Element("entity");

    // Get the columns from the entity and any related link-entity elements
    List<string> columns = GetColumnsFromElement(entityElement);

    return columns;
}

/// <summary>
/// Recursive function to get all column names from an entity or nested link-entity elements
/// </summary>
/// <param name="element">The entity or link-entity element</param>
/// <param name="alias">The alias of the link-entity element</param>
/// <returns></returns>
static List<string> GetColumnsFromElement(XElement element, string? alias = null)
{
    List<string> columns = new();

    // Get the attributes from the element
    foreach (XElement attribute in element.Elements("attribute"))
    {
        StringBuilder sb = new();

        // Prepend the alias for link-entities
        if (!string.IsNullOrWhiteSpace(alias))
        {
            sb.Append($"{alias}.");
        }

        // Use the attribute alias if there is one
        if (attribute.Attribute("alias") != null)
        {
            sb.Append(attribute.Attribute("alias")?.Value);
        }
        else
        {
            //Use the attribute name
            sb.Append(attribute.Attribute("name")?.Value);
        }

        columns.Add(sb.ToString());
    }

    // Whether the link-entity intersect attribute is true
    bool isIntersect = (element.Attribute("intersect") != null) &&
        (element.Attribute("intersect")?.Value == "true" ||
        element.Attribute("intersect")?.Value == "1");

    // The name of the element
    string elementName = element.Attribute("name")?.Value;
    // The type of element: 'entity' or 'link-entity'
    string elementType = element.Name.LocalName;

    // This method requires any non-intersect entity to have attributes
    if (columns.Count == 0 && !isIntersect)
    {
        // An non-intersect element with no attribute elements is technically valid,
        // but not supported by this method.
        throw new Exception($"No attribute elements in {elementType} element named '{elementName}'.");
    }

    // Look for any child link-entities
    foreach (XElement linkEntity in element.Elements("link-entity"))
    {
        // Use the alias if any
        string? linkEntityName;
        if (linkEntity.Attribute("alias") != null)
        {
            linkEntityName = linkEntity.Attribute("alias")?.Value;
        }
        else
        {
            linkEntityName = linkEntity.Attribute("name")?.Value;
        }

        // Recursive call for nested link-entity elements
        columns.AddRange(GetColumnsFromElement(linkEntity, linkEntityName));
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
                    // Use the simple attribut value
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
```

You can adapt the [Quickstart: Execute an Organization service request (C#)](../org-service/quick-start-org-service-console-app.md) sample to test FetchXml queries with the following steps:

1. Add the `OutputFetchRequest`, `GetColumns`, `GetColumnsFromElement`, and `GetRowValues` methods to the `Program` class.
1. Add a reference to the [ConsoleTables NuGet package](https://www.nuget.org/packages/ConsoleTables/2.5.0) to the project in Visual Studio.
1. Modify the `Main` method as shown below:

```csharp
static void Main(string[] args)
  {
      using (ServiceClient serviceClient = new(connectionString))
      {
          if (serviceClient.IsReady)
          {
            string fetchXml = @"<fetch>
                    <entity name='account'>
                      <attribute name='accountclassificationcode' />
                      <attribute name='createdby' />
                      <attribute name='createdon' />
                      <attribute name='name' />
                    </entity>
                  </fetch>";

            OutputFetchRequest(serviceClient, fetchXml);
          }
          else
          {
              Console.WriteLine(
                  "A web service connection was not established.");
          }
      }

      // Pause the console so it does not close.
      Console.WriteLine("Press any key to exit.");
      Console.ReadLine();
  }
```

When you run the program, the output should look something like this:

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
 | Default Value             | FirstName LastName | 3/25/2023 10:42 AM | Contoso Pharmaceuticals (sample) |
 ---------------------------------------------------------------------------------------------------------
 | Default Value             | FirstName LastName | 3/25/2023 10:42 AM | Alpine Ski House (sample)        |
 ---------------------------------------------------------------------------------------------------------
 | Default Value             | FirstName LastName | 3/25/2023 10:42 AM | A. Datum Corporation (sample)    |
 ---------------------------------------------------------------------------------------------------------
 | Default Value             | FirstName LastName | 3/25/2023 10:42 AM | Coho Winery (sample)             |
 ---------------------------------------------------------------------------------------------------------
```

### [Web API](#tab/webapi)

Content for Web API

---



## Next steps

Learn how to select columns.

> [!div class="nextstepaction"]
> [Select columns](select-columns.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
