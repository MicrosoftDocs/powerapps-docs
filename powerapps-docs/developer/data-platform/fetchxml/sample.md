---
title: FetchXml Sample code
description: Try using FetchXML to retrieve Dataverse data using this sample code.
ms.date: 12/04/2024
ms.reviewer: jdaly
ms.topic: how-to
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - dmitmikh
 - dasussMS
 - apahwa-lab
 - DonaldlaGithub
---
# FetchXml sample code

To try using FetchXml with C#, you can use the `OutputFetchRequest` static methods in this article by adapting the respective quick start samples:

- [Quick Start: Execute an SDK for .NET request (C#)](../org-service/quick-start-org-service-console-app.md)
- [Quick Start: Web API sample (C#)](../webapi/quick-start-console-app-csharp.md)

> [!NOTE]
> See [Paging Cookie examples](page-results.md#paging-cookie-examples) for sample code to retrieve data in pages.

## [SDK for .NET](#tab/sdk)

You can use the following `OutputFetchRequest` static method to test FetchXml queries in a console application.

The `OutputFetchRequest` method demonstrates how to use the [FetchExpression class](xref:Microsoft.Xrm.Sdk.Query.FetchExpression) and the [IOrganizationService.RetrieveMultiple method](xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A) to return an [EntityCollection](xref:Microsoft.Xrm.Sdk.EntityCollection) containing the requested data.

The `OutputFetchRequest` method depends on the [ConsoleTables NuGet package](https://www.nuget.org/packages/ConsoleTables/2.5.0) and requires that all [entity](reference/entity.md) or [link-entity](reference/link-entity.md) element [attribute elements](reference/attribute.md) are included, which is a best practice.

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

    /// <summary>
    /// Get a list of column names from the FetchXml
    /// </summary>
    /// <param name="fetchXml">The fetchXml query</param>
    /// <returns></returns>
    static List<string> GetColumns(string fetchXml)
    {
        XDocument fetchDoc = XDocument.Parse(fetchXml);

        XElement fetchElement = fetchDoc.Root;

        bool isAggregate = !(fetchElement?.Attributes("aggregate") == null &&
            (fetchElement?.Attribute("aggregate")?.Value == "true" ||
            fetchElement?.Attribute("aggregate")?.Value == "1"));

        // There can only be one entity element
        XElement entityElement = fetchElement.Element("entity");

        // Get the columns from the entity and any related link-entity elements
        return GetColumnsFromElement(element: entityElement, isAggregate: isAggregate);

    }

    /// <summary>
    /// Recursive function to get all column names from an entity or nested link-entity elements
    /// </summary>
    /// <param name="element">The entity or link-entity element</param>
    /// <param name="isAggregate">Whether the query uses aggregation</param>
    /// <param name="alias">The alias of the link-entity element</param>
    /// <returns></returns>
    static List<string> GetColumnsFromElement(XElement element, bool isAggregate, string? alias = null)
    {
        List<string> columns = new();

        // Get the attributes from the element
        foreach (XElement attribute in element.Elements("attribute"))
        {
            StringBuilder sb = new();


            // Prepend the alias for non-aggregate link-entities
            if (!string.IsNullOrWhiteSpace(alias) && !isAggregate)
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
            columns.AddRange(GetColumnsFromElement(linkEntity, isAggregate, linkEntityName));
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
                if (entity.FormattedValues.ContainsKey(column) &&
                !string.IsNullOrWhiteSpace(entity.FormattedValues[column]))
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

You can adapt the [Quick Start: Execute an SDK for .NET request (C#)](../org-service/quick-start-org-service-console-app.md) sample to test queries with the following steps:

1. Install the [ConsoleTables NuGet package](https://www.nuget.org/packages/ConsoleTables/2.5.0)
1. Add the following using statements at the top of the `program.cs` file

    ```csharp
    using Microsoft.Xrm.Sdk;
    using Microsoft.Xrm.Sdk.Query;
    using System.Text;
    using System.Xml.Linq;
    ```

1. Copy and paste the `OutputFetchRequest` method below the `Main` method.
1. Edit the `Main` method to set your query and use the `OutputFetchRequest` method.

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

                    string fetchQuery = @"<fetch top='5'>
                        <entity name='account'>
                        <attribute name='accountclassificationcode' />
                        <attribute name='createdby' />
                        <attribute name='createdon' />
                        <attribute name='name' />
                        </entity>
                    </fetch>";

                    OutputFetchRequest(serviceClient, fetchQuery);
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
[!INCLUDE [cc-connection-string](../includes/cc-connection-string.md)]

## [Web API](#tab/webapi)

When using C#, you can use the following `OutputFetchRequest` static method to test FetchXml queries in a console application.

The `GetRecords` function demonstrates how to compose an [HttpRequestMessage](xref:System.Net.Http.HttpRequestMessage) to use with an authenticated [HttpClient](xref:System.Net.Http.HttpClient) to return a [JsonArray](xref:System.Text.Json.Nodes.JsonArray) containing the requested data.

The `OutputFetchRequest` method depends on the [ConsoleTables NuGet package](https://www.nuget.org/packages/ConsoleTables/2.5.0) and requires that all [entity](reference/entity.md) or [link-entity](reference/link-entity.md) element `attribute` elements are included, which is a best practice.

```csharp
/// <summary>
/// Renders the output of a query in a table for a console application
/// </summary>
/// <param name="client">The authenticated HttpClient instance to use.</param>
/// <param name="entitySetName">The entity set name for the table.</param>
/// <param name="fetchXml">The FetchXml query to use.</param>
private static async Task OutputFetchRequest(HttpClient client, string entitySetName, string fetchXml)
{
    // Retrieve the data from Dataverse
    JsonArray records = await GetRecords(client, entitySetName, fetchXml);

    // Get column names from the FetchXml
    List<string> columns = GetColumns(fetchXml);

    // Create the table using https://www.nuget.org/packages/ConsoleTables/2.5.0
    var table = new ConsoleTables.ConsoleTable(columns.ToArray());

    foreach (JsonObject record in records.Cast<JsonObject>())
    {
        table.Rows.Add(GetRowValues(columns, record).ToArray());
    }

    // Write the table to the console
    table.Write();

    /// <summary>
    /// Retrieves records from Dataverse
    /// </summary>
    /// <param name="client">The authenticated HttpClient instance to use.</param>
    /// <param name="entitySetName">The entity set name for the table.</param>
    /// <param name="fetchXml">The FetchXml query to use.</param>
    /// <returns>JsonArray of records</returns>
    static async Task<JsonArray> GetRecords(HttpClient client, string entitySetName, string fetchXml)
    {
        // Prepare the request
        HttpRequestMessage request = new()
        {
            Method = HttpMethod.Get,
            RequestUri = new Uri(
            uriString: $"{entitySetName}?fetchXml={WebUtility.UrlEncode(fetchXml.ToString())}",
            uriKind: UriKind.Relative),
        };
        // Add annotations to return formatted values
        request.Headers.Add("Prefer", "odata.include-annotations=\"*\"");

        // Send the request
        var response = await client.SendAsync(request);

        if (response.IsSuccessStatusCode)
        {
            string jsonContent = await response.Content.ReadAsStringAsync();

            // Using System.Text.Json
            JsonObject content = JsonNode.Parse(jsonContent)?.AsObject();

            // Records are in the value property
            content.TryGetPropertyValue("value", out JsonNode records);

            return records.AsArray();
        }
        else
        {
            throw new Exception($"Web API call failed. Status Code: {response.StatusCode}");
        }
    }


    /// <summary>
    /// Get a list of column names from the FetchXml
    /// </summary>
    /// <param name="fetchXml">The fetchXml query</param>
    /// <returns>List of column names</returns>
    static List<string> GetColumns(string fetchXml)
    {
        XDocument fetchDoc = XDocument.Parse(fetchXml);

        XElement fetchElement = fetchDoc.Root;

        bool isAggregate = !(fetchElement?.Attributes("aggregate") == null &&
            (fetchElement?.Attribute("aggregate")?.Value == "true" ||
            fetchElement?.Attribute("aggregate")?.Value == "1"));

        // There can only be one entity element
        XElement entityElement = fetchElement.Element("entity");

        // Get the columns from the entity and any related link-entity elements
        List<string> columns = GetColumnsFromElement(element: entityElement, isAggregate: isAggregate);

        return columns;
    }

    /// <summary>
    /// Recursive function to get all column names from an entity or nested link-entity elements
    /// </summary>
    /// <param name="element">The entity or link-entity element</param>
    /// <param name="alias">The alias of the link-entity element</param>
    /// <returns></returns>
    static List<string> GetColumnsFromElement(XElement element, bool isAggregate, string? alias = null)
    {
        List<string> columns = new();

        // Get the attributes from the element
        foreach (XElement attribute in element.Elements("attribute"))
        {
            StringBuilder sb = new();

            // Prepend the alias for non-aggregate link-entities
            if (!string.IsNullOrWhiteSpace(alias) && !isAggregate)
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
            columns.AddRange(GetColumnsFromElement(linkEntity, isAggregate, linkEntityName));
        }

        return columns;
    }

    /// <summary>
    /// Returns the values of a row as strings
    /// </summary>
    /// <param name="columns">The names of the columns</param>
    /// <param name="record">The record with the data</param>
    /// <returns></returns>
    static List<string> GetRowValues(List<string> columns, JsonObject record)
    {
        List<string> values = new();

        columns.ForEach(column =>
        {
            string lookupPropertyName = $"_{column}_value";
            bool isLookup = record.ContainsKey(lookupPropertyName);

            if (record.ContainsKey(column) || isLookup)
            {
                string formattedValueKey = string.Format("{0}@OData.Community.Display.V1.FormattedValue", 
                    isLookup ? lookupPropertyName : column);

                // Use the formatted value if it available and visible
                if (record.ContainsKey(formattedValueKey) && 
                !string.IsNullOrWhiteSpace((string)record[formattedValueKey]))
                {
                    values.Add($"{record[formattedValueKey]}");
                }
                else
                {
                    // Use the simple property value
                    values.Add($"{record[column]}");
                }
            }
            // Null values are not returned
            else
            {
                values.Add("NULL");
            }

        });
        return values;
    }
}
```

### Update Web API quick start sample

You can adapt the [Quick Start: Web API sample (C#)](../webapi/quick-start-console-app-csharp.md) sample to test queries with the following steps:

1. Install the [ConsoleTables NuGet package](https://www.nuget.org/packages/ConsoleTables/2.5.0)
1. Copy and paste the `OutputFetchRequest` method below the `Main` method.
1. Modify the `Main` method and replace the content of the `Web API call` region as shown below:

```csharp
#region Web API call

string fetchXml = @"<fetch top='5'>
    <entity name='account'>
    <attribute name='accountclassificationcode' />
    <attribute name='createdby' />
    <attribute name='createdon' />
    <attribute name='name' />
    </entity>
</fetch>";

await OutputFetchRequest(client: client, entitySetName: "accounts", fetchXml: fetchXml);

#endregion Web API call
```

> [!IMPORTANT]
> The `entitySetName` parameter must be the entity set name for the same table specified in the FetchXml [entity element](reference/entity.md) `name` attribute.

---

When you run the program using the `OutputFetchRequest` method, the output should look like this:

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

[Query data using FetchXml](overview.md)
[Use FetchXml to retrieve data](retrieve-data.md)
[Sample: Use FetchXML with a paging cookie](../org-service/samples/use-fetchxml-paging-cookie.md)
[Sample: Use aggregation in FetchXML](../org-service/samples/use-aggregation-fetchxml.md)
[Sample: Convert queries between FetchXML and QueryExpression](../org-service/samples/convert-queries-fetch-queryexpression.md)
