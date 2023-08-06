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

FetchXml is a proprietary XML based query language used with Dataverse to retrieve data using either the Web API or the SDK for .NET. This article describes how to compose a query using FetchXml for both of these use cases. For more specific information, see the following articles:

|Use Case|More information|
|---------|---------|
|SDK for .NET|- [Query data using the SDK for .NET](../org-service/entity-operations-query-data.md) <br/>- [FetchExpression class](xref:Microsoft.Xrm.Sdk.Query.FetchExpression) <br/>- [RetrieveMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest) <br/>- [IOrganizationService.RetrieveMultiple method](xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A) <br/>|
|Web API|[Use FetchXml with Web API](../webapi/use-fetchxml-web-api.md)|

> [!NOTE]
> FetchXml is also used to define views for model-driven apps and some reporting capabilities. The [FetchXml schema](../fetchxml-schema.md) includes elements and attributes for these use cases which are not discussed here. More information: [Model-driven Apps developer guide: Customize views](../../model-driven-apps/customize-entity-views.md).

## Compose a query

All queries are based on a single table. When composing a query using FetchXml, the root element is [fetch](reference/fetch.md). Use the [entity element](reference/entity.md) to select the table the query will retrieve data from. The following example represents the simplest valid FetchXml query:

```xml
<fetch>
  <entity name='account' />
</fetch>
```

This query returns all columns of the first 5,000 rows from the [Account table](../reference/entities/account.md), using the table `LogicalName` to set the [entity](reference/entity.md) `name` attribute.

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


## Next steps

Learn how to select columns.

> [!div class="nextstepaction"]
> [Select columns](select-columns.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
