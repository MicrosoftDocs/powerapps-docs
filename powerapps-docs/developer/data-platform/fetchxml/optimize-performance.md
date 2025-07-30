---
title: Optimize performance using FetchXml
description: Learn how to optimize performance when you retrieve data from Microsoft Dataverse using FetchXml.
ms.date: 01/06/2025
ms.reviewer: jdaly
ms.topic: how-to
author: MsSQLGirl
ms.subservice: dataverse-developer
ms.author: jukoesma
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - dmitmikh
 - dasussMS
 - apahwa-lab
 - DonaldlaGithub
---
# Optimize performance using FetchXml

> [!NOTE]
> For guidance about general things to avoid when composing Dataverse queries, see [Query anti-patterns](../query-antipatterns.md). The following sections are specific to FetchXml.

## Late Materialize query

If you select many lookup and computed columns, and you're experiencing performance issues, you can try setting the [fetch element](reference/fetch.md) boolean `latematerialize` attribute. Behind the scenes, this setting breaks the query into smaller parts and reassembles the results before returning them to you.

Using the `latematerialize` attribute might not always provide a performance benefit. It might make simple queries run more slowly. It's most beneficial when your query:

- Has many joins
- Contains many lookup or computed columns

## Query Hints

> [!IMPORTANT]
> Only apply these options when recommended by Microsoft technical support. Incorrect use of these options can damage the performance of a query.

Microsoft SQL Server supports many query hints to optimize queries. FetchXML
supports query hints and can pass these query options to SQL Server using the [fetch element](reference/fetch.md) [options](reference/fetch.md#options) attribute.

[!INCLUDE [cc-query-options](../includes/cc-query-options.md)]


## No lock

In earlier versions, the `no-lock` attribute used to prevent shared locks on records. It's no longer necessary to include this attribute.


## Union Hint

You can improve performance when adding a [filter element](reference/filter.md) that sets the [condition](reference/condition.md) for columns in different tables by setting the `hint` attribute to `union`. But there are some restrictions:

- The [filter](reference/filter.md) must use the `or` filter type.
- Each query can contain only one `union` hint.
- If a filter with `union` hint isn't at top level filter, Dataverse transforms the query and move the filter with a `union` hint to root filter.
- If a `union` hint is more than three levels deep, it's ignored.

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
               value="555-123-4567"
               entityname="ac" />
            <condition attribute="telephone1"
               operator="eq"
               value="555-123-4567"
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



### See also

[Query data using FetchXml](overview.md)   
[Use FetchXml to retrieve data](retrieve-data.md)   
[Select columns using FetchXml](select-columns.md)  
[Join tables using FetchXml](join-tables.md)  
[Order rows using FetchXml](order-rows.md)  
[Filter rows using FetchXml](filter-rows.md)  
[Page results using FetchXml](page-results.md)   
[Aggregate data using FetchXml](aggregate-data.md)   
[Count rows using FetchXml](count-rows.md)  
[FetchXml reference](reference/index.md)   
[FetchXml sample code](sample.md)   
[Query anti-patterns](../query-antipatterns.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
