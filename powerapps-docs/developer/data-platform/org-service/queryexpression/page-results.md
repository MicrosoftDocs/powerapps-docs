---
title: Page results using QueryExpression
description: Learn how to use QueryExpression to page results when you retrieve data from Microsoft Dataverse.
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
# Page results using QueryExpression

You can specify a limit on the number of rows retrieved for each request by setting a page size. Using paging, you can retrieve consecutive pages of data representing all the records that match the criteria of a query in a performant manner.

The default and maximum page size is 5,000 rows. If you don't set a page size, Dataverse will return up to 5,000 rows of data at a time. To get more rows, you must send additional requests.

> [!NOTE]
> - Don't use the [fetch element](reference/fetch.md) `top` attribute with paging. These different methods of limiting the results of a query are not compatible.
> - Ordering plays an important part in getting consistent paging results. [Learn more about ordering and paging](order-rows.md#ordering-and-paging)

## Paging models

Dataverse has two paging models: *simple* and using *paging cookies*:

:::row:::
   :::column span="":::
      **Simple**

      - Uses only the [fetch element](reference/fetch.md) `count` and `page` attributes
      - Suitable for small data sets only
      - Can't return a data set larger than 50,000 records
      - Performance reduced as the number of rows increases
   :::column-end:::
   :::column span="":::
      **Paging cookies**

      - Uses the [fetch element](reference/fetch.md) `count`, `page`, and `paging-cookie` attributes
      - Set the `paging-cookie` attribute value to the value returned with previous page
      - Recommended for all data set sizes
      - [Some queries do not allow for paging cookies](#queries-that-dont-support-paging-cookies)
      - [Learn more about using paging cookies](#paging-cookies)
   :::column-end:::
:::row-end:::

## Simple paging

You can request to the first page by setting the [fetch element](reference/fetch.md) `page` attribute to 1 and the `count` attribute to the page size before sending the request:

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

With simple paging, sometimes called *legacy paging*, Dataverse retrieves all the results of the query up to the current page, selects the number of records needed for the page and then ignores the rest. This allows for quickly paging backward and forward though the data or skipping to a specific page. However the total number of records is limited to 50,000 and there can be performance issues for complex queries and arbitrarily sorted distinct query results.

Simple paging works well for small data sets, but as the number of rows in the data set increases, performance suffers. The total number of rows that can be retrieved using simple paging is 50,000. For best performance in all cases, we recommend consistently using paging cookies.

## Paging cookies

When there are more rows to retrieve after requesting the first page, Dataverse [*usually*](#queries-that-dont-support-paging-cookies) returns a paging cookie to be used on the following requests for the next pages.

The paging cookie contains data about the first and last record in the results and helps Dataverse retrieve the next row of data as quickly as possible and should be used when provided. You shouldn't modify the data in the paging cookie, just set the value to the [fetch element](reference/fetch.md) `paging-cookie` attribute and increment the `page` attribute value for subsequent requests.

### Queries that don't support paging cookies

Some queries do not support paging cookies. When paging cookies aren't supported by a query, no paging cookie value is returned with the result. For example, queries sorted using a `link-entity` attribute may not support paging cookies.

When Dataverse doesn't return a paging cookie, the paging model falls back to simple paging, with all the limitations that come with it.

## Paging cookie examples

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

        fetchNode.SetAttributeValue("page", page++);
    }
    return new EntityCollection(entities);
}
```

You can adapt the [Quick Start: Execute an SDK for .NET request (C#)](../org-service/quick-start-org-service-console-app.md)  sample to test FetchXml queries with the following steps:

1. Add the `RetrieveAll` static method to the `Program` class.
1. Modify the `Main` method as shown below:

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

> [!IMPORTANT]
> This query will return ALL records that match the criteria. Make sure you include filter elements to limit the results.


<!-- ## Ordering and paging -->
[!INCLUDE [cc-ordering-paging](../../includes/cc-ordering-paging.md)]

## Next steps

Learn how to aggregate data.

> [!div class="nextstepaction"]
> [Aggregate data](aggregate-data.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]