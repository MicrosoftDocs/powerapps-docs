---
title: Page Results Using FetchXml
description: Learn how to use FetchXml to page results when you retrieve data from Microsoft Dataverse. Explore simple paging and paging cookies for efficient data retrieval.
author: MsSQLGirl
ms.author: jukoesma
ms.date: 03/12/2026
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - dmitmikh
 - dasussMS
 - apahwa-lab
 - DonaldlaGithub
 - tdashworth
---
# Page results using FetchXML

You can limit the number of rows retrieved for each request by setting a page size. By using paging, you can retrieve consecutive pages of data, so you efficiently get all the records that match the criteria of a query.

The default and maximum page size is 5,000 for standard tables and 500 for elastic tables. If you don't set a page size, Dataverse returns either 5,000 or 500 rows of data at a time, depending on the type of table. To get more rows, you must send additional requests.

> [!NOTE]
>
> - Don't use the [fetch element](reference/fetch.md) `top` attribute with paging. These different methods of limiting the results of a query aren't compatible.
> - Ordering plays an important part in getting consistent paging results. [Learn more about ordering and paging](order-rows.md#ordering-and-paging).

## FetchXml paging models

FetchXml has two paging models: *simple* and *paging cookies*:

:::row:::
   :::column span="":::
      **Simple**

      - Uses only the [fetch element](reference/fetch.md) `count` and `page` attributes
      - Suitable for small datasets only
      - Can't return a dataset larger than 50,000 records
      - Performance reduces as the number of rows increases
   :::column-end:::
   :::column span="":::
      **Paging cookies**

      - Uses the [fetch element](reference/fetch.md) `count`, `page`, and `paging-cookie` attributes
      - Set the `paging-cookie` attribute value to the value returned with previous page
      - Recommended for all dataset sizes
      - [Some queries don't support paging cookies](#queries-that-dont-support-paging-cookies)
      - [Learn more about using paging cookies](#paging-cookies)
   :::column-end:::
:::row-end:::

## Simple paging

Request the first page by setting the [fetch element](reference/fetch.md) `page` attribute to 1 and the `count` attribute to the page size before sending the request:

```xml
<fetch count='3' page='1'>
  <entity name='account'>
    <attribute name='name' />
    <order attribute='name' />
    <order attribute='accountid' />
  </entity>
</fetch>
```

To get the next three records, increment the `page` value and send another request.

```xml
<fetch count='3' page='2'>
  <entity name='account'>
    <attribute name='name' />
    <order attribute='name' />
    <order attribute='accountid' />    
  </entity>
</fetch>
```

By using simple paging, sometimes called *legacy paging*, Dataverse retrieves all the results of the query up to the current page. It selects the number of records needed for the page and then ignores the rest. This method makes it easy to page backward and forward through the data or skip to a specific page. However, the total number of records is limited to 50,000. Also, complex queries and arbitrarily sorted distinct query results can cause performance problems.

Simple paging works well for small data sets. But as the number of rows in the data set increases, performance suffers. The total number of rows that you can retrieve by using simple paging is 50,000. For best performance in all cases, use paging cookies consistently.

## Paging cookies

When there are more rows to retrieve after requesting the first page, Dataverse [*usually*](#queries-that-dont-support-paging-cookies) returns a paging cookie to use in the following requests for the next pages.

The paging cookie contains data about the first and last record in the results. It helps Dataverse retrieve the next row of data as quickly as possible. Use the paging cookie when it's available. Don't modify the data in the paging cookie. Set the value to the [fetch element](reference/fetch.md) `paging-cookie` attribute and increment the `page` attribute value for subsequent requests.

### Queries that don't support paging cookies

Some queries don't support paging cookies. When a query doesn't support paging cookies, the query doesn't return a paging cookie value with the result. For example, queries sorted by using a `link-entity` attribute might not support paging cookies.

When Dataverse doesn't return a paging cookie, the paging model falls back to simple paging, with all the limitations that come with it.

## Paging cookie examples

How you use paging cookies depends on whether you're using the SDK for .NET or Web API.

### [SDK for .NET](#tab/sdk)

The following `RetrieveAll` static method returns all records that match the FetchXML query. It sends multiple requests if the number of records exceeds the page size.

After each request, the method checks the [EntityCollection.MoreRecords property](xref:Microsoft.Xrm.Sdk.EntityCollection.MoreRecords) to see if more records match the criteria. If there are more records, the method sets the value of the returned [EntityCollection.PagingCookie property](xref:Microsoft.Xrm.Sdk.EntityCollection.PagingCookie) to the `paging-cookie` attribute of the [fetch element](reference/fetch.md) and sends another request.

```csharp
/// <summary>
/// Returns all records matching the criteria
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance.</param>
/// <param name="fetchXml">The fetchXml Query string</param>
/// <param name="pageSize">The page size to use. Default is 5,000</param>
/// <returns>All the records that match the criteria</returns>
static EntityCollection RetrieveAll(IOrganizationService service, string fetchXml, int pageSize = 5000)
{

    // The records to return
    List<Entity> entities = new();

    XElement fetchNode = XElement.Parse(fetchXml);

    int page = 1; //Start with page 1

    //Set the page
    fetchNode.SetAttributeValue("page", page);

    // Set the page size
    fetchNode.SetAttributeValue("count", pageSize);

    while (true)
    {
        // Get the page
        EntityCollection results = service.RetrieveMultiple(new FetchExpression(fetchNode.ToString()));

        entities.AddRange(results.Entities);

        if (!results.MoreRecords)
        {
            break;
        }

        // Set the fetch paging-cookie attribute with the paging cookie from the previous query
        fetchNode.SetAttributeValue("paging-cookie", results.PagingCookie);

        fetchNode.SetAttributeValue("page", ++page);
    }
    return new EntityCollection(entities);
}
```

To test FetchXML queries, adapt the sample in [Quick Start: Execute an SDK for .NET request (C#)](../org-service/quick-start-org-service-console-app.md) by using the following steps:

1. Add the `RetrieveAll` static method to the `Program` class.
1. Modify the `Main` method as shown in the following code:

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

            string fetchQuery = @"<fetch count='3' page='1'>
                <entity name='contact'>
                    <attribute name='fullname'/>
                    <attribute name='jobtitle'/>
                    <attribute name='annualincome'/>
                    <order descending='true' attribute='fullname'/>
                </entity>
        </fetch>";

            EntityCollection records = RetrieveAll(service: serviceClient,
                        fetchXml: fetchQuery,
                        pageSize: 25);

            Console.WriteLine($"Success: {records.Entities.Count}");
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

> [!NOTE]
> This query returns all records that match the criteria. Make sure you include filter elements to limit the results.

Read the following important information about using a connection string in application code.
[!INCLUDE [cc-connection-string](../includes/cc-connection-string.md)]

### [Web API](#tab/webapi)

By using the Web API, you can request a paging cookie as an annotation. Use either of these request headers:

```
Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.fetchxmlpagingcookie,Microsoft.Dynamics.CRM.morerecords"
```

OR for all annotations:

```
Prefer: odata.include-annotations="*"
```


The result returns these annotations:

- `@Microsoft.Dynamics.CRM.fetchxmlpagingcookie`
- `@Microsoft.Dynamics.CRM.morerecords`

The following series of FetchXML requests show the use of paging cookies. For brevity, this example uses a small `count` value (3).

```xml
<fetch count='3' page='1'>
  <entity name='contact'>
    <attribute name='fullname' />
    <attribute name='jobtitle' />
    <attribute name='annualincome' />
    <order descending='true' attribute='fullname' />
  </entity>
</fetch>
```

### First page

Send the first page with the `page` value set to `'1'`.

Use this request header:

```
Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.fetchxmlpagingcookie,Microsoft.Dynamics.CRM.morerecords"
```

To make sure the response includes the paging cookie and more records annotations.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts?fetchXml=%3Cfetch%20count%3D%273%27%20page%3D%271%27%3E%0D%0A%3Centity%20name%3D%27contact%27%3E%0D%0A%3Cattribute%20name%3D%27fullname%27%2F%3E%0D%0A%3Cattribute%20name%3D%27jobtitle%27%2F%3E%0D%0A%3Cattribute%20name%3D%27annualincome%27%2F%3E%0D%0A%3Corder%20descending%3D%27true%27%20attribute%3D%27fullname%27%2F%3E%0D%0A%3C%2Fentity%3E%0D%0A%3C%2Ffetch%3E&$count=true
Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.fetchxmlpagingcookie,Microsoft.Dynamics.CRM.morerecords"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="Microsoft.Dynamics.CRM.fetchxmlpagingcookie,Microsoft.Dynamics.CRM.morerecords"

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#contacts(fullname,jobtitle,annualincome,_transactioncurrencyid_value,transactioncurrencyid,contactid,transactioncurrencyid())",
    "@Microsoft.Dynamics.CRM.fetchxmlpagingcookie": "<cookie pagenumber=\"2\" pagingcookie=\"%253ccookie%2520page%253d%25221%2522%253e%253cfullname%2520last%253d%2522Susanna%2520Stubberod%2520%2528sample%2529%2522%2520first%253d%2522Yvonne%2520McKay%2520%2528sample%2529%2522%2520%252f%253e%253ccontactid%2520last%253d%2522%257b70BF4D48-34CB-ED11-B596-0022481D68CD%257d%2522%2520first%253d%2522%257b49B0BE2E-D01C-ED11-B83E-000D3A572421%257d%2522%2520%252f%253e%253c%252fcookie%253e\" istracking=\"False\" />",
    "@Microsoft.Dynamics.CRM.morerecords": true,
    "value": [
        {
            "@odata.etag": "W/\"72201545\"",
            "fullname": "Yvonne McKay (sample)",
            "jobtitle": "Coffee Master",
            "annualincome": 45000.0000,
            "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
            "contactid": "49b0be2e-d01c-ed11-b83e-000d3a572421"
        },
        {
            "@odata.etag": "W/\"80648856\"",
            "fullname": "Thomas Andersen (sample)",
            "jobtitle": "Purchasing Manager",
            "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
            "contactid": "86bf4d48-34cb-ed11-b596-0022481d68cd"
        },
        {
            "@odata.etag": "W/\"80648695\"",
            "fullname": "Susanna Stubberod (sample)",
            "jobtitle": "Purchasing Manager",
            "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
            "contactid": "70bf4d48-34cb-ed11-b596-0022481d68cd"
        }
    ]
}
```

In the response, the `@Microsoft.Dynamics.CRM.morerecords` annotation value indicates that more records exist that match the criteria.

The `@Microsoft.Dynamics.CRM.fetchxmlpagingcookie` annotation value provides the paging information about the record returned. The `@Microsoft.Dynamics.CRM.fetchxmlpagingcookie` value is an XML element. You need to use the `pagingcookie` attribute value of that element in the next request.

The `pagingcookie` attribute value is URL-encoded *twice*. Although you don't need to check this value, the decoded and formatted value in this example looks like this:

```xml
<cookie page="1">
  <fullname last="Susanna Stubberod (sample)"
    first="Yvonne McKay (sample)" />
  <contactid last="{70BF4D48-34CB-ED11-B596-0022481D68CD}"
    first="{49B0BE2E-D01C-ED11-B83E-000D3A572421}" />
</cookie>
```

### Following pages

In all subsequent requests where the previous page has the `@Microsoft.Dynamics.CRM.morerecords` annotation value of `true`, you need to:

1. Increment the `fetch` element `page` attribute value.
1. URL-decode the `pagingcookie` attribute value twice.
1. XML-encode the decoded `pagingcookie` attribute value and set it as the value of a `paging-cookie` attribute on the `fetch` element.

    > [!NOTE]
    > Whether you must explicitly XML-encode the value might depend on the technology you use. In .NET, it might be done for you when you set the XML value to an attribute of another XML element.

1. URL-encode the entire FetchXML value as you did in the first request.

In the following request, the FetchXML looks like this before it's URL-encoded:

```xml
<fetch count='3' page='2' paging-cookie='&lt;cookie page="1"&gt;&lt;fullname last="Susanna Stubberod (sample)" first="Yvonne McKay (sample)" /&gt;&lt;contactid last="{70BF4D48-34CB-ED11-B596-0022481D68CD}" first="{49B0BE2E-D01C-ED11-B83E-000D3A572421}" /&gt;&lt;/cookie&gt;'>
  <entity name='contact'>
    <attribute name='fullname' />
    <attribute name='jobtitle' />
    <attribute name='annualincome' />
    <order descending='true' attribute='fullname' />
  </entity>
</fetch>
```

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts?fetchXml=%3Cfetch%20count%3D%273%27%20page%3D%272%27%20paging-cookie%3D%27%26lt%3Bcookie%20page%3D%221%22%26gt%3B%26lt%3Bfullname%20last%3D%22Susanna%20Stubberod%20%28sample%29%22%20first%3D%22Yvonne%20McKay%20%28sample%29%22%20%2F%26gt%3B%26lt%3Bcontactid%20last%3D%22%7B70BF4D48-34CB-ED11-B596-0022481D68CD%7D%22%20first%3D%22%7B49B0BE2E-D01C-ED11-B83E-000D3A572421%7D%22%20%2F%26gt%3B%26lt%3B%2Fcookie%26gt%3B%27%3E%0D%0A%3Centity%20name%3D%27contact%27%3E%0D%0A%3Cattribute%20name%3D%27fullname%27%2F%3E%0D%0A%3Cattribute%20name%3D%27jobtitle%27%2F%3E%0D%0A%3Cattribute%20name%3D%27annualincome%27%2F%3E%0D%0A%3Corder%20descending%3D%27true%27%20attribute%3D%27fullname%27%2F%3E%0D%0A%3C%2Fentity%3E%0D%0A%3C%2Ffetch%3E
Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.fetchxmlpagingcookie,Microsoft.Dynamics.CRM.morerecords"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="Microsoft.Dynamics.CRM.fetchxmlpagingcookie,Microsoft.Dynamics.CRM.morerecords"

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#contacts(fullname,jobtitle,_transactioncurrencyid_value,transactioncurrencyid,contactid,annualincome,transactioncurrencyid())",
    "@Microsoft.Dynamics.CRM.fetchxmlpagingcookie": "<cookie pagenumber=\"2\" pagingcookie=\"%253ccookie%2520page%253d%25222%2522%253e%253cfullname%2520last%253d%2522Scott%2520Konersmann%2520%2528sample%2529%2522%2520first%253d%2522Susan%2520Burk%2520%2528sample%2529%2522%2520%252f%253e%253ccontactid%2520last%253d%2522%257b78BF4D48-34CB-ED11-B596-0022481D68CD%257d%2522%2520first%253d%2522%257b84BF4D48-34CB-ED11-B596-0022481D68CD%257d%2522%2520%252f%253e%253c%252fcookie%253e\" istracking=\"False\" />",
    "@Microsoft.Dynamics.CRM.morerecords": true,
    "value": [
        {
            "@odata.etag": "W/\"80648842\"",
            "fullname": "Susan Burk (sample)",
            "jobtitle": "Owner",
            "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
            "contactid": "84bf4d48-34cb-ed11-b596-0022481d68cd"
        },
        {
            "@odata.etag": "W/\"80648744\"",
            "fullname": "Sidney Higa (sample)",
            "jobtitle": "Owner",
            "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
            "contactid": "76bf4d48-34cb-ed11-b596-0022481d68cd"
        },
        {
            "@odata.etag": "W/\"80648758\"",
            "fullname": "Scott Konersmann (sample)",
            "jobtitle": "Purchasing Manager",
            "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
            "contactid": "78bf4d48-34cb-ed11-b596-0022481d68cd"
        }
    ]
}
```

### Last page

On the final page, the response doesn't include the `@Microsoft.Dynamics.CRM.morerecords` and `@Microsoft.Dynamics.CRM.fetchxmlpagingcookie` annotations.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts?fetchXml=%3Cfetch%20count%3D%273%27%20page%3D%275%27%20paging-cookie%3D%27%26lt%3Bcookie%20page%3D%224%22%26gt%3B%26lt%3Bfullname%20last%3D%22Maria%20Campbell%20%28sample%29%22%20first%3D%22Patrick%20Sands%20%28sample%29%22%20%2F%26gt%3B%26lt%3Bcontactid%20last%3D%22%7B74BF4D48-34CB-ED11-B596-0022481D68CD%7D%22%20first%3D%22%7B82BF4D48-34CB-ED11-B596-0022481D68CD%7D%22%20%2F%26gt%3B%26lt%3B%2Fcookie%26gt%3B%27%3E%0D%0A%3Centity%20name%3D%27contact%27%3E%0D%0A%3Cattribute%20name%3D%27fullname%27%2F%3E%0D%0A%3Cattribute%20name%3D%27jobtitle%27%2F%3E%0D%0A%3Cattribute%20name%3D%27annualincome%27%2F%3E%0D%0A%3Corder%20descending%3D%27true%27%20attribute%3D%27fullname%27%2F%3E%0D%0A%3C%2Fentity%3E%0D%0A%3C%2Ffetch%3E
Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.fetchxmlpagingcookie,Microsoft.Dynamics.CRM.morerecords"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#contacts(fullname,jobtitle,_transactioncurrencyid_value,transactioncurrencyid,contactid,annualincome,transactioncurrencyid())",
    "value": [
        {
            "@odata.etag": "W/\"87523026\"",
            "fullname": "Jim Glynn (sample)",
            "jobtitle": "Owner",
            "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
            "contactid": "80bf4d48-34cb-ed11-b596-0022481d68cd"
        }
    ]
}
```

### Web API paging example

When you use C# with [HttpClient](xref:System.Net.Http.HttpClient), the following `RetrieveAll` static method returns all records that match the FetchXml query. It sends multiple requests if the number of records exceeds the page size.

```csharp
/// <summary>
/// Returns all records matching the criteria
/// </summary>
/// <param name="client">The authenticated HttpClient instance.</param>
/// <param name="entitySetName">The EntitySetName for the table used in the fetchXml</param>
/// <param name="fetchXml">The FetchXml query string</param>
/// <param name="pageSize">The page size to use. Default is 5,000</param>
/// <returns>All the records that match the criteria</returns>
/// <exception cref="Exception"></exception>
static async Task<List<JsonObject>> RetrieveAll(HttpClient client, 
   string entitySetName, 
   string fetchXml, 
   int pageSize = 5000)
{

    List<JsonObject> entities = new();

    XElement fetchNode = XElement.Parse(fetchXml);

    int page = 1; //Start with page 1

    // Set the fetch page attribute
    fetchNode.SetAttributeValue("page", page);

    // Set the fetch count attribute
    fetchNode.SetAttributeValue("count", pageSize);

    while (true)
    {
        bool moreRecords;
        string pagingCookie = null;

        // Prepare the request
        HttpRequestMessage request = new()
        {
            Method = HttpMethod.Get,
            RequestUri = new Uri(
            uriString: $"{entitySetName}?fetchXml={HttpUtility.UrlEncode(fetchNode.ToString())}",
            uriKind: UriKind.Relative),
        };
        // Add annotations to return formatted values
        request.Headers.Add("Prefer", "odata.include-annotations=" + 
            "\"Microsoft.Dynamics.CRM.fetchxmlpagingcookie," +
            "Microsoft.Dynamics.CRM.morerecords\"");

        // Send the request
        var response = await client.SendAsync(request);
               
        if (response.IsSuccessStatusCode)
        {
            string jsonContent = await response.Content.ReadAsStringAsync();

            // Using System.Text.Json.Nodes
            JsonObject content = JsonNode.Parse(jsonContent)?.AsObject();

            // Records are in the 'value' property
            content.TryGetPropertyValue("value", out JsonNode records);

            // Add records to the list
            entities.AddRange(records.AsArray().Cast<JsonObject>());

            // Detect if there are more records
            moreRecords = content.
               TryGetPropertyValue("@Microsoft.Dynamics.CRM.morerecords", out _);
            if (moreRecords)
            {
                // Get the paging cookie value
                if (content.
                     TryGetPropertyValue("@Microsoft.Dynamics.CRM.fetchxmlpagingcookie", 
                        out JsonNode fetchxmlpagingcookie))
                {
                    pagingCookie = fetchxmlpagingcookie.AsValue().ToString();
                }
            }
        }
        else
        {
            throw new Exception($"Web API call failed. Status Code: {response.StatusCode}");
        }

        if (!moreRecords)
        {
            // Stop sending requests
            break;
        }

        XElement cookieElement = XElement.Parse(pagingCookie);
        // Extract the pagingcookie attribute
        XAttribute pagingcookieAttribute = cookieElement.Attribute("pagingcookie");
        // Decode the pagingcookie attribute twice
        pagingCookie = HttpUtility.UrlDecode(HttpUtility.UrlDecode(pagingcookieAttribute.Value));

        // Set the fetch paging-cookie attribute with the paging cookie from the previous query
        fetchNode.SetAttributeValue("paging-cookie", pagingCookie);

        // Increment the fetch page attribute value
        fetchNode.SetAttributeValue("page", ++page);
    }

    // Return the records from all requests
    return entities;
}
```

You can adapt the [Quick Start: Web API sample (C#)](../webapi/quick-start-console-app-csharp.md) sample to test FetchXml queries by using the following steps:

1. Add the `RetrieveAll` static method to the `Program` class.
1. Modify the `Main` method and replace the content of the `Web API call` region as shown in the following code sample:

```csharp
#region Web API call

string fetchXml = @"<fetch>
      <entity name='contact'>
         <attribute name='fullname'/>
         <attribute name='jobtitle'/>
         <attribute name='annualincome'/>
         <order descending='true' attribute='fullname'/>
      </entity>
</fetch>";

List<JsonObject> records = await RetrieveAll(client: client, 
   entitySetName: "contacts", 
   fetchXml: fetchXml, 
   pageSize: 3);

Console.WriteLine($"Success: {records.Count}");

#endregion Web API call
```

> [!IMPORTANT]
> This query returns all records that match the criteria. Make sure you include filter elements to limit the results.
>
> The `entitySetName` parameter must be the [entity set name](../webapi/web-api-service-documents.md#entity-set-name) for the same table specified in the FetchXml [entity element](reference/entity.md) `name` attribute.

---

[!INCLUDE [cc-ordering-paging](../includes/cc-ordering-paging.md)]

## Next steps

Learn how to aggregate data.

> [!div class="nextstepaction"]
> [Aggregate data](aggregate-data.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
