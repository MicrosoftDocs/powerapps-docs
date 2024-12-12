---
title: Page results using QueryExpression
description: Learn how to use QueryExpression to page results when you retrieve data from Microsoft Dataverse.
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
---
# Page results using QueryExpression

You can specify a limit on the number of rows retrieved for each request by setting a page size. Using paging, you can retrieve consecutive pages of data representing all the records that match the criteria of a query in a performant manner.

The default and maximum page size is 5,000 rows. If you don't set a page size, Dataverse will return up to 5,000 rows of data at a time. To get more rows, you must send additional requests.

> [!NOTE]
>
> - Don't use the [QueryExpression.TopCount property](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.topcount) with paging. These different methods of limiting the results of a query are not compatible.
> - Ordering plays an important part in getting consistent paging results. [Learn more about ordering and paging](#ordering-and-paging)

## Paging models

Dataverse has two paging models: *simple* and using *paging cookies*:

:::row:::
   :::column span="":::
      **Simple**

      - Uses only the [QueryExpression.PageInfo](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.pageinfo) [Count](/dotnet/api/microsoft.xrm.sdk.query.paginginfo.count) and [PageNumber](/dotnet/api/microsoft.xrm.sdk.query.paginginfo.pagenumber) properties
      - Suitable for small data sets only
      - Can't return a data set larger than 50,000 records
      - Performance reduced as the number of rows increases
   :::column-end:::
   :::column span="":::
      **Paging cookies**

      - Uses the [QueryExpression.PageInfo](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.pageinfo), [Count](/dotnet/api/microsoft.xrm.sdk.query.paginginfo.count), [PageNumber](/dotnet/api/microsoft.xrm.sdk.query.paginginfo.pagenumber), and [PagingCookie](/dotnet/api/microsoft.xrm.sdk.query.paginginfo.pagingcookie) properties.
      - `PagingCookie` is null for the first request. For subsequent requests, set the `PagingCookie` property value to the value returned with previous page
      - Recommended for all data set sizes
      - [Some queries do not allow for paging cookies](#queries-that-dont-support-paging-cookies)
      - [Learn more about using paging cookies](#paging-cookies)
   :::column-end:::
:::row-end:::

## Simple paging

You can request to the first page by setting the [QueryExpression.PageInfo property](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.pageinfo) with a [PagingInfo class](/dotnet/api/microsoft.xrm.sdk.query.paginginfo) instance with the [PagingInfo.PageNumber](/dotnet/api/microsoft.xrm.sdk.query.paginginfo.pagenumber) to 1 and the [PagingInfo.Count](/dotnet/api/microsoft.xrm.sdk.query.paginginfo.count) to the page size before sending the request:

```csharp
var query = new QueryExpression(entityName: "account")
{
      ColumnSet = new ColumnSet("name"),
      PageInfo = new PagingInfo() { 
         Count = 3,
         PageNumber = 1
      }
};
query.AddOrder(attributeName:"name",orderType: OrderType.Ascending);
query.AddOrder(attributeName: "accountid", orderType: OrderType.Ascending);
```

To get the next three records, increment the `PageInfo.PageNumber` value and send another request.

```csharp
query.PageInfo.PageNumber++;
```

With simple paging, sometimes called *legacy paging*, Dataverse retrieves all the results of the query up to the current page, selects the number of records needed for the page and then ignores the rest. This allows for quickly paging backward and forward though the data or skipping to a specific page. However the total number of records is limited to 50,000 and there can be performance issues for complex queries and arbitrarily sorted distinct query results.

Simple paging works well for small data sets, but as the number of rows in the data set increases, performance suffers. For best performance in all cases, we recommend consistently using paging cookies.

## Paging cookies

When there are more rows to retrieve after requesting the first page, Dataverse [*usually*](#queries-that-dont-support-paging-cookies) returns a paging cookie to be used on the following requests for the next pages.

The paging cookie contains data about the first and last record in the results and helps Dataverse retrieve the next row of data as quickly as possible. A paging cookie should be used when returned by the previous page. You shouldn't modify the data in the paging cookie, just set the value to the [QueryExpression.PageInfo.PagingCookie](/dotnet/api/microsoft.xrm.sdk.query.paginginfo.pagingcookie) property and increment the `QueryExpression.PageInfo.PageNumber` value for subsequent requests.

### Queries that don't support paging cookies

Some queries do not support paging cookies. When paging cookies aren't supported by a query, no paging cookie value is returned with the result. For example, queries sorted using a `LinkEntity` column may not support paging cookies.

When Dataverse doesn't return a paging cookie, the paging model falls back to simple paging, with all the limitations that come with it.

## Paging cookie example

The following `RetrieveAll` static method will return all records that match the [QueryExpression](/dotnet/api/microsoft.xrm.sdk.query.queryexpression) query, sending multiple requests if the number of records exceeds the page size.

After each request, the method checks the [EntityCollection.MoreRecords property](xref:Microsoft.Xrm.Sdk.EntityCollection.MoreRecords) to determine if more records match the criteria. If there are more records, the method sets the value of the returned [EntityCollection.PagingCookie property](xref:Microsoft.Xrm.Sdk.EntityCollection.PagingCookie) to the `PageInfo.PagingCookie` property of the `QueryExpression` and sends another request.

```csharp
/// <summary>
/// Returns all records matching the criteria
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance.</param>
/// <param name="query">The QueryExpression query</param>
/// <param name="page">The page size to use. Defaults to 5000</param>
/// <returns>All the records that match the criteria</returns>
static EntityCollection RetrieveAll(IOrganizationService service, 
QueryExpression query,
int page = 5000)
{
    // The records to return
    List<Entity> entities = new();

    // Set the page
    query.PageInfo.PageNumber = 1;
    // Set the count
    query.PageInfo.Count = page;

    while (true)
    {
        // Get the records
        EntityCollection results = service.RetrieveMultiple(query);

        entities.AddRange(results.Entities);

        if (!results.MoreRecords)
        {
            //Stop if there are no more records
            break;
        }
        // Set the PagingCookie with the PagingCookie from the previous query
        query.PageInfo.PagingCookie = results.PagingCookie;

        // Update the PageNumber
        query.PageInfo.PageNumber++;
    }

    return new EntityCollection(entities);
}
```

You can adapt the [Quick Start: Execute an SDK for .NET request (C#)](../../org-service/quick-start-org-service-console-app.md)  sample to test `QueryExpression` queries with the following steps:

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

            QueryExpression query = new("contact")
            {
                ColumnSet = new ColumnSet("fullname", "jobtitle", "annualincome"),
                Orders = {
                    { 
                        new OrderExpression(
                            attributeName: "fullname", 
                            orderType: OrderType.Descending) 
                    }
                }
            };

            EntityCollection records = RetrieveAll(service: serviceClient,
                        query: query)

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

Read the following important information about using a connection string in application code.
[!INCLUDE [cc-connection-string](../../includes/cc-connection-string.md)]

<!-- ## Ordering and paging -->
[!INCLUDE [cc-ordering-paging](../../includes/cc-ordering-paging.md)]

## Next steps

Learn how to aggregate data.

> [!div class="nextstepaction"]
> [Aggregate data](aggregate-data.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
