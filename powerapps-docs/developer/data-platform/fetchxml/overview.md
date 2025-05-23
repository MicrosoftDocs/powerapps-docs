---
title: Use FetchXml to query data
description: Learn to compose a query using FetchXml, a proprietary XML based language that is used in Microsoft Dataverse to retrieve data.
ms.date: 03/05/2024
ms.reviewer: jdaly
ms.topic: how-to
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - dmitmikh
 - dasussMS
 - apahwa-lab
 - DonaldlaGithub
---
# Query data using FetchXml

FetchXml is a proprietary XML based query language used to retrieve data from Dataverse. See [FetchXml reference](reference/index.md) for the elements used to retrieve data.

> [!NOTE]
> FetchXml is also used to define views for model-driven apps and some reporting capabilities. Elements and attributes for those use cases are not included here. [Learn more about customizing model-driven app views with code](../../model-driven-apps/customize-entity-views.md).

## Compose a query

All queries are based on a single table. The root element is [fetch](reference/fetch.md). Use the [entity element](reference/entity.md) to select the table the query retrieves data from. The following example represents a simple FetchXml query:

```xml
<fetch top='5'>
  <entity name='account'>
      <attribute name='name' />
  </entity>
</fetch>
```

This query returns the [Name column](../reference/entities/account.md#BKMK_Name) of the first five rows from the [Account table](../reference/entities/account.md), using the [LogicalName](../org-service/entity-operations.md#entitylogicalname) of the table to set the [entity](reference/entity.md) `name` attribute.

## Limit the number of rows

To limit the number of rows returned, use the [fetch element](reference/fetch.md) `top` attribute. Without the `top` attribute, Dataverse returns up to 5,000 rows.

Alternatively, specify a number of records to return using *paging*. Don't use the `top` attribute when you request pages of data. [Learn how to request paged results](page-results.md)

You can't use `top` when you request a count of rows using the `returntotalrecordcount` attribute. [Learn to count rows](count-rows.md)

## Return distinct results

Use the [fetch element](reference/fetch.md) `distinct` attribute to require the query to exclude any duplicate values in the results.

If you use the `distinct` attribute, you must add at least one [order element](reference/order.md) to have consistent paging.

When you use the `distinct` attribute, the results returned don't include primary key values for each record because they represent an aggregation of all the distinct values.

## Retrieve Data

To get results from your query, you need to send your request to Dataverse. [Learn to retrieve data from Dataverse using FetchXml](retrieve-data.md)


## Refine your query

After you select the table to start your query with, refine the query to get the data you need. The following articles explain how to complete your query.


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

The [XrmToolbox](../community-tools.md#xrmtoolbox) [FetchXmlBuilder](https://fetchxmlbuilder.com/) is a free tool to compose and test FetchXml requests.

> [!NOTE]
> Tools created by the community are not supported by Microsoft. If you have questions or issues with community tools, contact the publisher of the tool.

## Use FetchXml as a message parameter

You also use FetchXml as a parameter for Dataverse operations such as the following messages:

|Message Name|SDK for .NET Request class|Web API Operation|
|---------|---------|---------|
|`BackgroundSendEmail`|[BackgroundSendEmailRequest](xref:Microsoft.Crm.Sdk.Messages.BackgroundSendEmailRequest)|[BackgroundSendEmail action](xref:Microsoft.Dynamics.CRM.BackgroundSendEmail)|
|`BulkDetectDuplicates`|[BulkDetectDuplicatesRequest](xref:Microsoft.Crm.Sdk.Messages.BulkDetectDuplicatesRequest)|[BulkDetectDuplicates action](xref:Microsoft.Dynamics.CRM.BulkDetectDuplicates)|
|`FullTextSearchKnowledgeArticle`|[FullTextSearchKnowledgeArticleRequest](xref:Microsoft.Crm.Sdk.Messages.FullTextSearchKnowledgeArticleRequest)|[FullTextSearchKnowledgeArticle action](xref:Microsoft.Dynamics.CRM.FullTextSearchKnowledgeArticle)|
|`FetchXmlToQueryExpression`|[FetchXmlToQueryExpressionRequest](xref:Microsoft.Crm.Sdk.Messages.FetchXmlToQueryExpressionRequest)|[FetchXmlToQueryExpression Function](xref:Microsoft.Dynamics.CRM.FetchXmlToQueryExpression)|
|`SendBulkMail`|[SendBulkMailRequest](xref:Microsoft.Crm.Sdk.Messages.SendBulkMailRequest)|[SendBulkMail action](xref:Microsoft.Dynamics.CRM.SendBulkMail)|
|`Rollup`|[RollupRequest](xref:Microsoft.Crm.Sdk.Messages.RollupRequest)|[Rollup function](xref:Microsoft.Dynamics.CRM.Rollup)|


## Next steps

Learn how to select columns.

> [!div class="nextstepaction"]
> [Select columns](select-columns.md)

Learn how to retrieve data with FetchXml.

> [!div class="nextstepaction"]
> [Retrieve data with FetchXml](retrieve-data.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
