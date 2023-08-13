---
title: Aggregate data using FetchXml
description: Learn how to use FetchXml to retrieve aggregated data from Microsoft Dataverse.
ms.date: 08/31/2023
ms.reviewer: jdaly
ms.topic: how-to
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
search.audienceType: 
  - developer
---
# Aggregate data using FetchXml

FetchXML includes grouping and aggregation features that let you calculate sum, average, min, max and count.

## Limitations

Queries that return aggregate values are limited to 50,000 records. This limit helps maintain system performance and reliability. If the filter criteria in your query includes more than 50,000 records you will get the following error:

> Error code: `-2147164125`
> Hexadecimal error code: `8004E023`
> Platform error message: `AggregateQueryRecordLimit exceeded. Cannot perform this operation.`
> Client error message: The maximum record limit is exceeded. Reduce the number of records.

To avoid this error add appropriate filters to your query to ensure that it will not need to evaluate more than 50,000 records. Then run your query multiple times and combine the results.

> [!TIP]
> If you want to get a total count of records with no filter, use the `RetrieveTotalRecordCount` message with either the Web API [RetrieveTotalRecordCount Function](xref:Microsoft.Dynamics.CRM.RetrieveTotalRecordCount) or with the SDK for .NET [RetrieveTotalRecordCountRequest class](xref:Microsoft.Crm.Sdk.Messages.RetrieveTotalRecordCountRequest) message class. The data retrieved will be from a snapshot within the last 24 hours.

## Examples

## Next steps

Learn how to count rows.

> [!div class="nextstepaction"]
> [Count rows](count-rows.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]