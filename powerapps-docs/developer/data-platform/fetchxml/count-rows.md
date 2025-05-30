---
title: Count rows using FetchXml
description: Learn how to use FetchXml to count rows from Microsoft Dataverse tables.
ms.date: 02/29/2024
ms.reviewer: jdaly
ms.topic: how-to
author: MsSQLGirl
ms.author: jukoesma
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - dmitmikh
 - dasussMS
 - apahwa-lab
 - DonaldlaGithub
---
# Count rows using FetchXml

Use the [fetch element](reference/fetch.md) boolean `returntotalrecordcount` attribute to specify that the result include a count of all the records that meet the filter criteria, up to 5,000 for standard tables, 500 for elastic tables. Use this when retrieving paged results to estimate the total number of pages to display.

You can't apply the [fetch element](reference/fetch.md) `top` attribute together with `returntotalrecordcount`.

The behavior you can expect depends on whether you are using the SDK for .NET or Web API.

## [SDK for .NET](#tab/sdk)

When the `returntotalrecordcount` attribute value is `true`, the <xref:Microsoft.Xrm.Sdk.EntityCollection> returned from the [RetrieveMultiple](xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A)  method includes values for the following properties:


|Property|Description|
|---------|---------|
|<xref:Microsoft.Xrm.Sdk.EntityCollection.TotalRecordCount>|The total number of records up to 5,000; otherwise the value is -1.|
|<xref:Microsoft.Xrm.Sdk.EntityCollection.TotalRecordCountLimitExceeded>|`true` if the results of the query exceeds the total record count; otherwise, `false`.|



## [Web API](#tab/webapi)

Setting the `returntotalrecordcount` attribute value to `true` has the same result as setting the OData `$count` query option. You can append `&$count=true` to your FetchXml query to get the same results. [Learn more about the OData $count query option](../webapi/query/count-rows.md).

When you set the `returntotalrecordcount` attribute (or use the `$count` query option) the data returned includes the `@odata.count` annotation with the total number of records that match the filter criteria, up to 5,000 for standard tables, 500 for elastic tables.

If you include either of these request headers:

```
Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.totalrecordcount,Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded"
   OR for all annotations:
Prefer: odata.include-annotations="*"
```

The following annotations will be returned:

|Property|Description|
|---------|---------|
|`@Microsoft.Dynamics.CRM.totalrecordcount`|The total number of records up to 5,000; otherwise the value is -1. The value is the same as the `@odata.count` annotation.|
|`@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded`|`true` if the results of the query exceeds the total record count; otherwise, `false`.|

---

The (<xref:Microsoft.Xrm.Sdk.EntityCollection.TotalRecordCountLimitExceeded> or `@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded`) value is useful when you need to calculate how many more paged requests you need to send to get all the results when (<xref:Microsoft.Xrm.Sdk.EntityCollection.TotalRecordCount> or `@Microsoft.Dynamics.CRM.totalrecordcount`) equals the maximum page size for the type of table you are working with.

If your page size is less than the maximum and (<xref:Microsoft.Xrm.Sdk.EntityCollection.TotalRecordCount> or `@Microsoft.Dynamics.CRM.totalrecordcount`) is equal to or less than maximum, you can calculate how many more paged requests you must send to get all the records.

When (<xref:Microsoft.Xrm.Sdk.EntityCollection.TotalRecordCountLimitExceeded> or `@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded`) is `true` and (<xref:Microsoft.Xrm.Sdk.EntityCollection.TotalRecordCount> or `@Microsoft.Dynamics.CRM.totalrecordcount`) equals the maximum, you can't perform this calculation.


> [!TIP]
> If you want to get a total count of records with no filter, use the `RetrieveTotalRecordCount` message with either the Web API [RetrieveTotalRecordCount Function](xref:Microsoft.Dynamics.CRM.RetrieveTotalRecordCount) or with the SDK for .NET [RetrieveTotalRecordCountRequest class](xref:Microsoft.Crm.Sdk.Messages.RetrieveTotalRecordCountRequest). The data retrieved will be from a snapshot within the last 24 hours.


## Next steps

Learn how to optimize performance.

> [!div class="nextstepaction"]
> [Optimize performance](optimize-performance.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]