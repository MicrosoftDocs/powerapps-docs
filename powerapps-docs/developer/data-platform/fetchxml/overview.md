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

FetchXml is a proprietary XML based query language used to retrieve data from Dataverse. See [FetchXml reference](reference/index.md) for the elements used to retrieve data.

> [!NOTE]
> FetchXml is also used to define views for model-driven apps and some reporting capabilities. The [FetchXml schema](../fetchxml-schema.md) includes elements and attributes for these use cases. [Learn more about customizing model-driven app views with code](../../model-driven-apps/customize-entity-views.md).

## Compose a query

All queries are based on a single table. When composing a query using FetchXml, the root element is [fetch](reference/fetch.md). Use the [entity element](reference/entity.md) to select the table the query will retrieve data from. The following example represents the simplest valid FetchXml query:

```xml
<fetch>
  <entity name='account' />
</fetch>
```

This query returns all columns of the first 5,000 rows from the [Account table](../reference/entities/account.md), using the table `LogicalName` to set the [entity](reference/entity.md) `name` attribute.

> [!IMPORTANT]
> We strongly discourage returning all columns in a table. Returning all columns will make your applications run slower and may cause timeout errors. You should [select which columns to return](select-columns.md).

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

## Use FetchXml to retrieve data

You can use FetchXml to retrieve data using either the SDK for .NET or Web API. With Power Automate, you can retrieve data using the Web API using the [Fetch Xml Query parameter of the List Rows command](/power-automate/dataverse/list-rows#fetch-xml-query).

### [SDK for .NET](#tab/sdk)

Use the [FetchExpression class](xref:Microsoft.Xrm.Sdk.Query.FetchExpression) to hold pass the FetchXml query as a string. `FetchExpression` is derived from the common [QueryBase class](xref:Microsoft.Xrm.Sdk.Query.QueryBase) type, so you can use it when that type is a method parameter or class property.

You should use the [IOrganizationService.RetrieveMultiple method](xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A) for most cases.

```csharp
static EntityCollection RetrieveMultipleExample(IOrganizationService service, string fetchXml)
{
   return service.RetrieveMultiple(new FetchExpression(fetchXml));
}
```

You can also use the [RetrieveMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest) with the [IOrganizationService.Execute method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A), but there are few scenarios where this is necessary.

```csharp
static EntityCollection RetrieveMultipleRequestExample(IOrganizationService service, string fetchXml)
{
   var request = new RetrieveMultipleRequest()
   {
         Query = new FetchExpression(fetchXml)
   };

   var response = (RetrieveMultipleResponse)service.Execute(request);

   return response.EntityCollection;
}
```

[Learn more about using messages with the SDK for .NET](../org-service/use-messages.md)

### [Web API](#tab/webapi)

Pass your FetchXml query as a URL-encoded string value to the entity set collection using the `fetchXml` query parameter.

> [!NOTE]
> Unlike queries that use the OData syntax, FetchXML queries sent using Web API don't return properties with null values.

For example, if you want to retrieve data from the [account entity set](xref:Microsoft.Dynamics.CRM.account), you will compose a fetchXml query setting the [entity element](reference/entity.md) `name` parameter to the `account`.

```xml
<fetch top='5'>
  <entity name='account'>
    <attribute name='name' />
  </entity>
</fetch>
```

Then, URL-encode the value.  Most programming languages include a function to URL-encode a string.

- In JavaScript, you use the [encodeURI function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent).
- In .NET, you can use the [System.NET.WebUtility.UrlEncode(String) method](xref:System.Net.WebUtility.UrlEncode(System.String))

> [!TIP]
> The [XrmToolbox](../community-tools.md#xrmtoolbox) [FetchXmlBuilder](https://fetchxmlbuilder.com/) provides an option to escape the fetchxml.

The URL-encoded string for the previous query example looks like this:

```text
%3Cfetch%20top%3D%275%27%3E%0D%0A%3Centity%20name%3D%27account%27%3E%0D%0A%3Cattribute%20name%3D%27name%27%2F%3E%0D%0A%3C%2Fentity%3E%0D%0A%3C%2Ffetch%3E
```

Then send your request to the `accounts` entity set with the `fetchXml` parameter in the URL.

**Request**:

```http
GET [Organization URI]/api/data/v9.2/accounts?fetchXml=%3Cfetch%20top%3D%275%27%3E%0D%0A%3Centity%20name%3D%27account%27%3E%0D%0A%3Cattribute%20name%3D%27name%27%2F%3E%0D%0A%3C%2Fentity%3E%0D%0A%3C%2Ffetch%3E
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**Response**:

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,accountid)",
    "value": [
        {
            "@odata.etag": "W/\"81359849\"",
            "name": "Litware, Inc. (sample)",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd"
        },
        {
            "@odata.etag": "W/\"80649580\"",
            "name": "Adventure Works (sample)",
            "accountid": "7a914942-34cb-ed11-b596-0022481d68cd"
        },
        {
            "@odata.etag": "W/\"84077591\"",
            "name": "Fabrikam, Inc. (sample)",
            "accountid": "7c914942-34cb-ed11-b596-0022481d68cd"
        },
        {
            "@odata.etag": "W/\"84174320\"",
            "name": "Blue Yonder Airlines (sample)",
            "accountid": "7e914942-34cb-ed11-b596-0022481d68cd"
        },
        {
            "@odata.etag": "W/\"80649588\"",
            "name": "City Power & Light (sample)",
            "accountid": "80914942-34cb-ed11-b596-0022481d68cd"
        }
    ]
}
```

---


## Sample code

To try using FetchXml with C#, you can use the `OutputFetchRequest` static methods in this section by adapting the respective quick start samples:

- [Quick Start: Execute an SDK for .NET request (C#)](../org-service/quick-start-org-service-console-app.md)
- [Quick Start: Web API sample (C#)](../webapi/quick-start-console-app-csharp.md)

> [!NOTE]
> See [PagingCookie example](page-results.md#pagingcookie-example) for sample code to retrieve data in pages.

### [SDK for .NET](#tab/sdk)

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

#### Update SDK for .NET quick start sample

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


### [Web API](#tab/webapi)

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
                string formattedValueKey = string.Format("{0}@OData.Community.Display.V1.FormattedValue", isLookup ? lookupPropertyName : column);


                // Use the formatted value if it available
                if (record.ContainsKey(formattedValueKey))
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

#### Update Web API quick start sample

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



## Next steps

Learn how to select columns.

> [!div class="nextstepaction"]
> [Select columns](select-columns.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
