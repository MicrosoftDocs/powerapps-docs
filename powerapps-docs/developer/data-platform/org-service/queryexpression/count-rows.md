---
title: Count rows using QueryExpression
description: Learn how to use QueryExpression to count rows from Microsoft Dataverse tables.
ms.date: 05/12/2024
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
# Count rows using QueryExpression

Use the boolean [QueryExpression.PageInfo.ReturnTotalRecordCount property](/dotnet/api/microsoft.xrm.sdk.query.paginginfo.returntotalrecordcount) to specify that the result include a count of all the records that meet the filter criteria, up to 5000. Use this when retrieving paged results to estimate the total number of pages to display.

You can't use the [QueryExpression.TopCount property](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.topcount) together with `ReturnTotalRecordCount`..

## Example

When the [ReturnTotalRecordCount property](/dotnet/api/microsoft.xrm.sdk.query.paginginfo.returntotalrecordcount) value is `true`, the <xref:Microsoft.Xrm.Sdk.EntityCollection> returned from the [RetrieveMultiple](xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A)  method includes values for the following properties:


|Property|Description|
|---------|---------|
|<xref:Microsoft.Xrm.Sdk.EntityCollection.TotalRecordCount>|The total number of records up to 5000; otherwise the value is -1.|
|<xref:Microsoft.Xrm.Sdk.EntityCollection.TotalRecordCountLimitExceeded>|`true` if the results of the query exceeds the total record count; otherwise, `false`.|


The <xref:Microsoft.Xrm.Sdk.EntityCollection.TotalRecordCountLimitExceeded> value is useful when you need to calculate how many more paged requests you need to send to get all the results when <xref:Microsoft.Xrm.Sdk.EntityCollection.TotalRecordCount> equals 5000.

If your page size is less than the maximum and <xref:Microsoft.Xrm.Sdk.EntityCollection.TotalRecordCount> is equal to or less than 5000, you can calculate how many more paged requests you must send to get all the records.

When <xref:Microsoft.Xrm.Sdk.EntityCollection.TotalRecordCountLimitExceeded> is `true` and <xref:Microsoft.Xrm.Sdk.EntityCollection.TotalRecordCount> equals 5000, you can't perform this calculation.


> [!TIP]
> If you want to get a total count of records with no filter, use the [RetrieveTotalRecordCountRequest class](xref:Microsoft.Crm.Sdk.Messages.RetrieveTotalRecordCountRequest). The data retrieved will be from a snapshot within the last 24 hours.


## Next steps

Learn how to optimize performance.

> [!div class="nextstepaction"]
> [Optimize performance](optimize-performance.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]