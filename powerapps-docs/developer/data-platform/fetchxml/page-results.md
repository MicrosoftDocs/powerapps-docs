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
  </entity>
</fetch>
```

To get the next three records, increment the `page` value and send another request.

```xml
<fetch count='3' page='2'>
  <entity name='account'>
    <attribute name='name' />
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
-->

## Next steps

Learn how to aggregate data.

> [!div class="nextstepaction"]
> [Aggregate data](aggregate-data.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]