---
title: Optimize performance using FetchXml
description: Learn how to optimize performance when you retrieve data from Microsoft Dataverse using FetchXml.
ms.date: 01/31/2024
ms.reviewer: jdaly
ms.topic: how-to
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
search.audienceType: 
  - developer
---
# Optimize performance using FetchXml

This article describes ways you can optimize preformance when retrieving data using FetchXml.

## Late Materialize query

If select statement has many Lookup, computed comlumns, and you're experiencing performance issues you can try setting a `latematerialize = 'true'` attribute to the [fetch element](reference/fetch.md). Behind the scenes, this setting will break the query up into smaller parts and re-assemble the results before returning them to you.

Using the `latematerialize` attribute might not always provide a performance benefit. It may make simple queries run more slowly. It is most beneficial when your query:

- Has many joins
- Contains many columns lookup columns or computed columns 

## Query Hints

> [!IMPORTANT]
> Only apply these options when recommended by Microsoft technical support. Incorrect use of these options can damage the performance of a query.

Microsoft SQL Server supports a number of query hints to optimize queries. FetchXML
supports query hints and can pass these query options to SQL Server using the [fetch element](reference/fetch.md) [options](reference/fetch.md#options) attribute.

[!INCLUDE [fetch-options-table](reference/includes/fetch-options-table.md)]


## No lock

In earlier versions, the `no-lock` attribute used to prevent shared locks on records. It is no longer necessary to include this.


## Union Hint

You can improve performance when adding a [filter element](reference/filter.md) that sets the [condition](reference/condition.md) for columns in different tables by setting the `hint` attribute to `union`. But there are some restrictions:

- The [filter](reference/filter.md) must use the `or` filter type.
- Each query can contain only one `union` hint.
- If a filter with `union` hint is not at top level filter, Dataverse will transform the query and move the filter with a `union` hint to root filter.
- If a `union` hint is more than three levels deep, it will be ignored.

The following example sets a filter with the `union` hint on the `telephone1` column for both the [account](../reference/entities/account.md) and [contact](../reference/entities/contact.md) tables.

```xml
<fetch>
      <entity name="email">
            <attribute name="activityid" />
            <attribute name="subject" />
            <filter type="and">
                  <condition attribute="subject"
                        operator="like"
                        value="Alert:%" />
                  <condition attribute="statecode"
                        operator="eq"
                        value="0" />
                  <filter type="or"
                        hint="union">
                        <condition attribute="telephone1"
                              operator="eq"
                              value="425-425-4021"
                              entityname="ac" />
                        <condition attribute="telephone1"
                              operator="eq"
                              value="425-425-4021"
                              entityname="co" />
                  </filter>
            </filter>
            <link-entity name="account"
                  from="accountid"
                  to="regardingobjectid"
                  link-type="outer"
                  alias="ac" />
            <link-entity name="contact"
                  from="contactid"
                  to="regardingobjectid"
                  link-type="outer"
                  alias="co" />
      </entity>
</fetch>
```

<!-- TODO: Include other sections for more performance optimization capabilities and best practices. -->



### See also

[Query data using FetchXml](overview.md)  
[Select columns using FetchXml](select-columns.md)  
[Join tables using FetchXml](join-tables.md)  
[Order rows using FetchXml](order-rows.md)  
[Filter rows using FetchXml](filter-rows.md)  
[Page results using FetchXml](page-results.md)  
[Count rows using FetchXml](count-rows.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
