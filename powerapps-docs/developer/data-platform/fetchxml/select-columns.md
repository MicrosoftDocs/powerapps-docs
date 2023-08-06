---
title: Select columns using FetchXml
description: Learn how to use FetchXml to select columns when you retrieve data from Microsoft Dataverse.
ms.date: 08/31/2023
ms.reviewer: jdaly
ms.topic: how-to
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
search.audienceType: 
  - developer
---
# Select columns using FetchXml

As described in [Query data using FetchXml](overview.md), start your query by selecting a table using the [entity element](reference/entity.md).

Use the [attribute element](reference/attribute.md) to select the columns to return with your query. For example:

```xml
<fetch>
  <entity name='account'>
    <attribute name='accountclassificationcode' />
    <attribute name='createdby' />
    <attribute name='createdon' />
    <attribute name='name' />
  </entity>
</fetch>
```

This query returns the [AccountClassificationCode](../reference/entities/account.md#BKMK_AccountClassificationCode), [CreatedBy](../reference/entities/account.md#BKMK_CreatedBy), [CreatedOn](../reference/entities/account.md#BKMK_CreatedOn), and [Name](../reference/entities/account.md#BKMK_Name) columns of the first 5,000 rows from the [Account table](../reference/entities/account.md). If you need more rows than this, see [Page results](page-results.md)

For each attribute you want returned, add an [attribute element](reference/attribute.md) and set the `name` attribute value to the `LogicalName` of the column.

Use the [attribute element](reference/attribute.md) to select the columns for the [entity](reference/entity.md) of your query and any tables joined using the [link-entity element](reference/link-entity.md). More information: [Join Tables](join-tables.md)

## Performance considerations

We strongly recommend that you specify the minimum number of columns to retrieve with your data. If you do not specify columns, or you use the [all-attributes element](reference/all-attributes.md), data for all columns is returned. Returning all columns will make your applications run slower and may cause timeout errors.


## Formatted values

If you view the results of the example query above, the results look something like this:

|accountclassificationcode|createdby|createdon|name|
|---|---|---|---|
|1|4026be43-6b69-e111-8f65-78e7d1620f5e|3/25/2023 5:42 PM|Litware, Inc. (sample)|
|1|4026be43-6b69-e111-8f65-78e7d1620f5e|3/25/2023 5:42 PM|Adventure Works (sample)|
|1|4026be43-6b69-e111-8f65-78e7d1620f5e|3/25/2023 5:42 PM|Fabrikam, Inc. (sample)|

The values returned represent what is saved in the database. This data doesn't seem to include data you may need, such as the label for the `accountclassificationcode` choice column or the name of the user for the `createdby` column. The `createdon` value represents the UTC value, where you may want to display the value in the user's time zone.

Remember that when you execute this query using the SDK for .NET or Web API, the results returned include *formatted values* that provide user-friendly string values for these columns that you can use in your application. More information:

- [SDK for .NET Query data: Access formatted values](../org-service/entity-operations-query-data.md#access-formatted-values)
- [Web API Query data: Formatted values](../webapi/query-data-web-api.md#formatted-values)


## Column aliases

You can use the [attribute](reference/attribute.md) `alias` attribute to specify any unique column name you want for the results returned.

Each column returned must have a unique name. By default, the column names returned for the entity of your query are the column `LogicalName` values. All column logical names are unique for each table, so there can't be any duplicate names within that set.

When you use a [link-entity element](reference/link-entity.md), the default column names follow this naming convention: `{Linked table LogicalName}.{Column LogicalName}`.  This prevents any duplicate column names. You can override this by using a unique alias.

## Next steps

Learn how to join tables.

> [!div class="nextstepaction"]
> [Join tables](join-tables.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]