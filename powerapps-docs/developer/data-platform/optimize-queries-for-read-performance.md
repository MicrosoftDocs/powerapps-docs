---
title: Optimize queries for read performance
description: Best practices when composing queries to retrieve records from Dataverse.
author: dasuss
ms.topic: article
ms.date: 03/28/2024
ms.subservice: dataverse-developer
ms.author: dasuss
ms.reviewer: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# Optimize queries for read performance
<!-- #TODO: This needs to specify SQL Read performance. These tips do not apply to dataverse search -->

Composing optimized queries for Dataverse is vital to ensure applications provide a fast, responsive, and reliable experience. This article describes patterns to avoid and concepts to understand when composing queries for standard tables using the `RetrieveMultiple` message, or messages that have a parameter that inherits from the [QueryBase class](/dotnet/api/microsoft.xrm.sdk.query.querybase). The guidance here might not apply for [Elastic tables](elastic-tables.md) or when using [Dataverse Search](search/overview.md).

## Minimize the number of selected columns

Don't include columns you don't need in your query. Queries that return all columns or include a large number of columns can encounter performance issues due to the size of the dataset.

This practice is especially true for *logical columns*. A logical column contains values that are stored in different database tables. The [AttributeMetadata.IsLogical property](/dotnet/api/microsoft.xrm.sdk.metadata.attributemetadata.islogical) tells you whether a column is a logical column. Queries that contain many logical columns are slower because Dataverse needs to combine the data from other database tables.

<!-- 

David: Most lookups are not logical attributes. Lookups include several supporting attributes that are logical, but the API doesn't return data for many of these. I'm talking about the fields that end with *Name. 

Common Lookups that are also logical are OwningTeam or OwningUser, because they are special.

That's why I re-wrote the content below.

   Queries with many logical attributes (for example, lookups) can also cause queries to be slow because each logical attribute needs to be retrieved from a seperate entity which can make a simple query much more complex and slow. 

   We recommend customers to design their queries to select the bare minimum of columns needed.

-->

## Avoid leading wild cards in filter conditions

Queries that use conditions with leading wild cards (either explicitly, or implicitly with an operator like `ends-with`) can lead to bad performance. Dataverse can't take advantage of database indexes when a query using leading wild cards, which forces SQL to scan the entire table. Table scans can happen even if there are other nonleading wild card queries that limit the result set.

The following example is a FetchXml query that uses a leading wild card:

```xml
<fetch>
   <entity name='account'>
      <attribute name='accountid' />
      <attribute name='accountnumber' />
      <filter type='and'>
         <condition attribute='accountnumber'
            operator='like'
            value='%234' />
      </filter>
   </entity>
</fetch>
```


When queries using leading wild cards timeout, the following error is returned:

<!-- 

Can this link to the current failure text in https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/web-service-error-codes 

jdaly: No. You can't link to an item within a table.
-->
<!-- 

Also we should update the throttle page to link back to here for the different rules 

-->

> Name: `DataEngineLeadingWildcardQueryThrottling`<br />
> Code: `0x80048644`<br />
> Number: `-2147187132`<br />
> Message: `This query cannot be executed because it conflicts with Query Throttling; the query uses a leading wildcard value in a filter condition, which will cause the query to be throttled more aggressively. Please refer to this document: https://go.microsoft.com/fwlink/?linkid=2162952`

Dataverse heavily throttles leading wild card queries that are identified as a risk to the health of the org to help prevent outages. [Learn more about query throttling](query-throttling.md)

If you find yourself using leading wild card queries, look into these options:

- Use [Dataverse search](search/overview.md) instead.
- Change your data model to help people avoid needing leading wild cards.

[Learn more about using wildcard characters in conditions for string values](../data-platform/wildcard-characters.md) 

## Avoid using formula or calculated columns in filter conditions

[Formula and calculated column](calculated-rollup-attributes.md#formula-and-calculated-columns) values are calculated in real-time when they're retrieved. Queries that use filters on these columns force Dataverse to calculate the value for each possible record that can be returned so the filter can be applied. Queries are slower because Dataverse can't improve the performance of these queries using SQL.

When queries time out and this pattern is detected, Dataverse returns a unique error to help identify which queries are using this pattern:

> Name: `ComputedColumnCauseTimeout`<br />
> Code: `0x80048574`<br />
> Number: `-2147187340`<br />
> Message: `The database operation timed out; this may be due to a computed column being used in a filter condition. Please consider removing filter conditions on computed columns, as these filter conditions are expensive and may cause timeouts.`

To help prevent outages, Dataverse applies throttles on queries that have filters on calculated columns that are identified as a risk to the health of the environment. [Learn more about query throttling](query-throttling.md)


## Avoid ordering by choice columns

When you request query results be ordered on a choice column, the results are ordered by the localized label of the choice values. Ordering by the number value stored in the database wouldn't provide a good experience in your application. You should know that ordering on choice columns requires more compute resources to join and sort the rows by the localized label value. This extra work makes the query slower. If possible, try to avoid ordering results by choice column values.


<!-- 

jdaly: I don't think this example adds much here.

Do you want to mention the fetch element useraworderby attribute?
That might make for a good example

Example query ordering on the statecode choice column: 

``` xml
<fetch distinct='true'>
   <entity name='account'>
      <attribute name='accountnumber' />
      <order attribute='statecode' />
   </entity>
</fetch> 
```
-->

## Avoid ordering by columns in related tables

Ordering by columns on related tables makes the query slower because of the added complexity.

**David**: What is the special trick included in the FetchXml docs? Is it to [Process `link-entity` orders first](fetchxml/order-rows.md#process-link-entity-orders-first)?

That example is:

```xml
<fetch>
  <entity name='account'>
    <attribute name='name' />
    <attribute name='accountnumber' />
    <attribute name='createdon' />
    <link-entity name='account'
      from='accountid'
      to='parentaccountid'
      link-type='inner'
      alias='parentaccount'>
      <attribute name='name'
        alias='parentaccount' />
        <!-- The link-entity parentaccount name -->
      <order attribute='name' />
    </link-entity>
    <!-- The entity account name -->
    <order attribute='name' />
  </entity>
</fetch>
```


Ordering by related tables should only be done when needed to as described here: [Order rows using FetchXml](../data-platform/fetchxml/order-rows.md) 

<!-- This looks like a conventional order within a link-entity to me. Is there something special about it? -->

``` xml
<fetch>
   <entity name='account'>
      <attribute name='accountnumber' />
      <link-entity name='account'
         from='accountid'
         to='parentaccountid'
         link-type='outer'
         alias='oaccount'>
         <attribute name='createdby' />
         <order attribute='name' />
      </link-entity>
   </entity>
</fetch>
```


## Avoid using like conditions on large text columns

<!-- 

Dataverse has two types of text columns:

- StringAttributeMetadata where the MaxSupportedLength is 4000 characters
- MemoAttributeMetadata where the MaxSupportedLength is 1,048,576 characters

Description is usually a MemoAttributeMetadata with a MaxLength set to 2000.

But either of these could be configured with a MaxLength of 10. Are they different?

How do you define 'large'? 
Is there a specified length that makes a difference?
 -->

Columns like with a length greater than TBD are defined in Dataverse as large text fields. These fields are too large to effectively index, which leads to bad performance when included in a filter condition.

Dataverse search is a better choice to query data in these kinds of fields.

<!-- 
I don't think we need an example here.

Example fetchxml which searches on a large text column: 

``` xml 
<fetch>
   <entity name='account'>
      <attribute name='accountid' />
      <attribute name='accountnumber' />
      <filter type='and'>
         <condition attribute='description'
            operator='like'
            value='Sold%' />
      </filter>
   </entity>
</fetch>
``` -->