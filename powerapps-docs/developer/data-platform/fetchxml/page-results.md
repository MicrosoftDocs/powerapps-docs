---
title: Page results using FetchXml
description: Learn how to use FetchXml to page results when you retrieve data from Microsoft Dataverse.
ms.date: 08/31/2023
ms.reviewer: jdaly
ms.topic: how-to
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
search.audienceType: 
  - developer
---
# Page results using FetchXml

Dataverse will return up to 5,000 rows of data with each request. If you need to get more rows of data, you need to send additional requests for subsequent pages. If you want your application to efficiently retrieve smaller set of data, you can use paging to specify the number of records to return.

Don't use the [fetch element](reference/fetch.md) `top` attribute to limit results with paging.

## Set order when paging

The choices you make in determining the order of the results can effect whether the rows in each page of data you retrieve overlaps with other pages. Without proper ordering, the same record can appear in more than one page. [Learn more about best practices for orders when paging data](order-rows.md#best-practices-for-orders-when-paging-data).

<!-- TODO: Update examples to include ordering best practices -->

## Simple paging

<!-- 
TODO: Clarify 'Legacy Paging'

Is Legacy Paging = Simple paging?
Docs suggest that no paging cookie returned with legacy paging.

 -->

You can implement simple client-side paging using FetchXml by setting the [fetch element](reference/fetch.md) `page` and `count` attributes together. Set the `count` to the number of records and the `page` number you want.

To get the first three records:

```xml
<fetch count='3' page='1'>
  <entity name='account'>
    <attribute name='name' />
    <order attribute='name' />
    <order attribute='accountid' />
  </entity>
</fetch>
```

The results of the query will tell you if there are more records that meet the filter criteria. These results depend on whether you use the SDK for .NET or Web API.

# [SDK for .NET](#tab/sdk)

The [MoreRecords property](xref:Microsoft.Xrm.Sdk.EntityCollection.MoreRecords) of the [EntityCollection](xref:Microsoft.Xrm.Sdk.EntityCollection) object returned by the `RetrieveMultiple` operation will be `true`.

# [Web API](#tab/webapi)

When you include the `Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.morerecords"` (or `Prefer: odata.include-annotations="*"` for all annotations) request header, the boolean `@Microsoft.Dynamics.CRM.morerecords` annotation value will be `true`.

---

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

Simple paging works well for small data sets, but as the size of the data set increases, performance suffers. For this reason, you can only retrieve up to 50,000 total records using simple paging. For best performance in all cases, we recommend consistently using the *paging cookie*.

## PagingCookie

A paging cookie is additional data that is returned when you retrieve multiple records. When you request the next page of record, set the paging cookie value returned from the previous page. The paging cookie contains information about the first and last records of the previous request. This allows Dataverse to more efficiently retrieve the next page, improving performance.

<!-- 
TODO: 
 - Should people cache the paging cookie if their application enables navigation from one page to the next?
 - Or is mostly for people to get all the records that match the criteria, regardless of how many records there are? 
 - Update this sample: https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/UseFetchXMLWithPaging
   - Add a RetrieveAll function that will apply paging to a FetchExpression.Query
   - Parameters:
      - FetchXml
      - PageSize (optional)
   
   Should we have a more advanced example with a class to manage paged results with methods like GetPage(N), GetNextPage(), GetLastPage()?
-->

### [SDK for .NET](#tab/sdk)

The following `RetrieveAll` static method will return all records that match the FetchXml query, sending multiple requests if the number of records exceeds the page size.

After each request, the method checks the [EntityCollection.MoreRecords property](xref:Microsoft.Xrm.Sdk.EntityCollection.MoreRecords) to determine if more records match the criteria. If there are more records, the method sets the value of the returned [EntityCollection.PagingCookie property](xref:Microsoft.Xrm.Sdk.EntityCollection.PagingCookie) to the `paging-cookie` attribute of the [fetch element](reference/fetch.md) and sends another request.

```csharp
/// <summary>
/// Returns all records matching the criteria
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance.</param>
/// <param name="fetchXml">The fetchXml Query string</param>
/// <param name="pageSize">The page size to use. Default is 5000</param>
/// <returns>All the records that match the criteria</returns>
static EntityCollection RetrieveAll(IOrganizationService service, string fetchXml, int pageSize = 5000)
{

    // The records to return
    List<Entity> entities = new();

    XElement fetchNode = XElement.Parse(fetchXml);

    int page = 1; //Start with page 1

    //Set the fetch page attribute
    SetPage(fetchNode, page);

    // Set the fetch count attribute
    SetCount(fetchNode, pageSize);

    while (true)
    {
        // Retrieve records
        EntityCollection results = service.RetrieveMultiple(new FetchExpression(fetchNode.ToString()));

        entities.AddRange(results.Entities);

        if (!results.MoreRecords)
        {
         // Stop sending requests
            break;
        }

        // Set the fetch paging-cookie attribute with the paging cookie from the previous query
        SetPagingCookie(fetchNode, results);

        page++;

        // Set the fetch page attribute
        SetPage(fetchNode, page);
    }

    // Return the records from all requests
    return new EntityCollection(entities);

    // Sets the fetch page attribute value
    void SetPage(XElement fetchNode, int page)
    {

        if (fetchNode.Attribute("page") != null)
        {
            // Set the value if attribute exists
            fetchNode.Attribute("page").SetValue(page);
        }
        else
        {
            // Add the attribute if it doesn't
            fetchNode.Add(new XAttribute("page", page));
        }
    }
   
   // Sets the fetch count attribute value
    void SetCount(XElement fetchNode, int count)
    {
        if (fetchNode.Attribute("count") != null)
        {
            // Set the value if attribute exists
            fetchNode.Attribute("count").SetValue(count);
        }
        else
        {
            // Add the attribute if it doesn't
            fetchNode.Add(new XAttribute("count", count));
        }
    }

    // Sets the fetch paging-cookie attribute value
    void SetPagingCookie(XElement fetchNode, EntityCollection results)
    {
        if (fetchNode.Attribute("paging-cookie") != null)
        {
            // Set the value if attribute exists
            fetchNode.Attribute("paging-cookie").SetValue(results.PagingCookie);
        }
        else
        {
            // Add the attribute if it doesn't
            fetchNode.Add(new XAttribute("paging-cookie", results.PagingCookie));
        }
    }
}
```

> [!IMPORTANT]
> This query will return ALL records that match the criteria. Make sure you include filter elements to limit the results.

### [Web API](#tab/webapi)

<!-- This content comes from https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/use-fetchxml-web-api#paging-with-fetchxml -->

With the Web API you must request a paging cookie as an annotation. Use the `prefer: odata.include-annotations="Microsoft.Dynamics.CRM.fetchxmlpagingcookie,Microsoft.Dynamics.CRM.morerecords"` request header (or `prefer: odata.include-annotations="*"` for all annotations) and `@Microsoft.Dynamics.CRM.fetchxmlpagingcookie` and `@Microsoft.Dynamics.CRM.morerecords` annotations are returned with the result.

The following series of FetchXML requests show the use of paging cookies. This example uses a small `count` value (3) for brevity. Normally you wouldn't use paging cookies for such small page sizes.

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

### First Page

Send the first page with the `page` value set to `'1'`. Use the `Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.fetchxmlpagingcookie,Microsoft.Dynamics.CRM.morerecords"` request header (or `Prefer: odata.include-annotations="*"` for all annotations) to make sure the paging cookie and more records annotations in the response are returned.

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

The `pagingcookie` attribute value is URL-encoded twice. The decoded value looks like this:

```xml
<cookie page="1"><fullname last="Susanna Stubberod (sample)" first="Yvonne McKay (sample)" /><contactid last="{70BF4D48-34CB-ED11-B596-0022481D68CD}" first="{49B0BE2E-D01C-ED11-B83E-000D3A572421}" /></cookie>
```

### Following Pages

In all subsequent requests where the previous page `@Microsoft.Dynamics.CRM.morerecords` annotation value indicates that more records exist, you need to:

1. Increment the `fetch` element `page` attribute value.
1. URL-decode the `pagingcookie` attribute value twice.
1. XML-encode the decoded `pagingcookie` attribute value and set it as the value of a `paging-cookie` attribute on the `fetch` element.

    Whether you must explicitly XML-encode the value may depend on the technology you use. In .NET, it might be done for you when you set the XML value to an attribute of another XML element.

1. URL Encode the entire FetchXml value as you did in the first request.

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

### Last Page

On the final page, the `@Microsoft.Dynamics.CRM.morerecords` and `@Microsoft.Dynamics.CRM.fetchxmlpagingcookie` annotations aren't included in the response.

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

When using C#, the following `RetrieveAll` static method will return all records that match the FetchXml query, sending multiple requests if the number of records exceeds the page size.

```csharp
/// <summary>
/// Returns all records matching the criteria
/// </summary>
/// <param name="client">The authenticated HttpClient instance.</param>
/// <param name="entitySetName">The EntitySetName for the table used in the fetchXml</param>
/// <param name="fetchXml">The FetchXml query string</param>
/// <param name="pageSize">The page size to use. Default is 5000</param>
/// <returns>All the records that match the criteria</returns>
/// <exception cref="Exception"></exception>
static async Task<List<JsonObject>> RetrieveAll(HttpClient client, string entitySetName, string fetchXml, int pageSize = 5000)
{

    List<JsonObject> entities = new();

    XElement fetchNode = XElement.Parse(fetchXml);

    int page = 1; //Start with page 1

    // Set the fetch page attribute
    SetPage(fetchNode, page);

    // Set the fetch count attribute
    SetCount(fetchNode, pageSize);

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
        request.Headers.Add("Prefer", "odata.include-annotations=\"Microsoft.Dynamics.CRM.fetchxmlpagingcookie," +
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
            moreRecords = content.TryGetPropertyValue("@Microsoft.Dynamics.CRM.morerecords", out _);
            if (moreRecords)
            {
                // Get the paging cookie value
                if (content.TryGetPropertyValue("@Microsoft.Dynamics.CRM.fetchxmlpagingcookie", out JsonNode fetchxmlpagingcookie))
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

        // Set the fetch paging-cookie attribute with the paging cookie from the previous query
        SetPagingCookie(fetchNode, pagingCookie);

        page++;
        // Increment the fetch page attribute value
        SetPage(fetchNode, page);
    }

    // Return the records from all requests
    return entities;

    // Sets the fetch page attribute value
    void SetPage(XElement fetchNode, int page)
    {
        if (fetchNode.Attribute("page") != null)
        {
            // Set the value if attribute exists
            fetchNode.Attribute("page").SetValue(page);
        }
        else
        {
            // Add the attribute if it doesn't
            fetchNode.Add(new XAttribute("page", page));
        }
    }

    // Sets the fetch count attribute value
    void SetCount(XElement fetchNode, int count)
    {
        if (fetchNode.Attribute("count") != null)
        {
            // Set the value if attribute exists
            fetchNode.Attribute("count").SetValue(count);
        }
        else
        {
            // Add the attribute if it doesn't
            fetchNode.Add(new XAttribute("count", count));
        }
    }

    // Sets the fetch paging-cookie attribute value
    void SetPagingCookie(XElement fetchNode, string fetchxmlpagingcookie)
    {
        XElement cookieElement = XElement.Parse(fetchxmlpagingcookie);
        // Extract the pagingcookie attribute
        XAttribute pagingcookieAttribute = cookieElement.Attribute("pagingcookie");
        // Decode the pagingcookie attribute twice
        string pagingCookie = HttpUtility.UrlDecode(HttpUtility.UrlDecode(pagingcookieAttribute.Value));

        if (fetchNode.Attribute("paging-cookie") != null)
        {
            // Set the value if attribute exists, XML encodes value
            fetchNode.Attribute("paging-cookie").SetValue(pagingCookie);
        }
        else
        {
            // Add the attribute if it doesn't exist, XML encodes value
            fetchNode.Add(new XAttribute("paging-cookie", pagingCookie));
        }
    }
}
```

You can adapt the [Quick Start: Web API sample (C#)](../webapi/quick-start-console-app-csharp.md) sample to test FetchXml queries with the following steps:

1. Add the `RetrieveAll` static method to the `Program` class.
1. Modify the `Main` method and replace the content of the `Web API call` region as shown below:

```csharp
#region Web API call

string fetchXml = @"<fetch count='3' page='1'>
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
> This query will return ALL records that match the criteria. Make sure you include filter elements to limit the results.
> 
> The `entitySetName` parameter must be the entity set name for the same table specified in the FetchXml [entity element](reference/entity.md) `name` attribute.

---
## Next steps

Learn how to aggregate data.

> [!div class="nextstepaction"]
> [Aggregate data](aggregate-data.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]