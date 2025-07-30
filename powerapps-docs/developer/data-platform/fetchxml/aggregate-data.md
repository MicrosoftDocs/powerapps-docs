---
title: Aggregate data using FetchXml
description: Learn how to use FetchXml to retrieve aggregated data from Microsoft Dataverse.
ms.date: 02/29/2024
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
# Aggregate data using FetchXml

FetchXML includes grouping and aggregation features that let you calculate sum, average, min, max, and count across multiple rows of data.

To return an aggregate value, you must:

- Set the [fetch element](reference/fetch.md) `aggregate` attribute to true.
- Set the `alias` attribute for each [attribute element](reference/attribute.md).
- Set the `aggregate` attribute for each [attribute element](reference/attribute.md) to one of these aggregate functions:

   [!INCLUDE [aggregate-function-table](reference/includes/aggregate-function-table.md)]

Note the following points:

- Null values aren't considered when calculating aggregate values.
- You can use data from tables joined using the [link-entity element](reference/link-entity.md).
- You can [apply filters](filter-rows.md) to limit the results as with any query.

## Example

Let's say you have 10 account records with the following data:

|Number of Employees|Name|Address 1 City|Created On|
|---------|---------|---------|---------|
|NULL|Example Account|NULL|8/25/2023|
|1,500|Contoso Pharmaceuticals (sample)|Redmond|3/25/2023|
|2,700|Fabrikam, Inc. (sample)|Lynnwood|3/25/2023|
|2,900|Blue Yonder Airlines (sample)|Los Angeles|3/25/2023|
|2,900|City Power & Light (sample)|Redmond|3/25/2023|
|3,900|Coho Winery (sample)|Phoenix|3/25/2023|
|4,300|Adventure Works (sample)|Santa Cruz|3/25/2023|
|4,800|Alpine Ski House (sample)|Missoula|3/25/2023|
|6,000|Litware, Inc. (sample)|Dallas|3/25/2023|
|6,200|A. Datum Corporation (sample)|Redmond|3/25/2023|

The following query returns aggregate data for the `numberofemployees` column.

```xml
<fetch aggregate='true'>
  <entity name='account'>
    <attribute name='numberofemployees'
      alias='Average'
      aggregate='avg' />
    <attribute name='numberofemployees'
      alias='Count'
      aggregate='count' />
    <attribute name='numberofemployees'
      alias='ColumnCount'
      aggregate='countcolumn' />
    <attribute name='numberofemployees'
      alias='Maximum'
      aggregate='max' />
    <attribute name='numberofemployees'
      alias='Minimum'
      aggregate='min' />
    <attribute name='numberofemployees'
      alias='Sum'
      aggregate='sum' />
  </entity>
</fetch>
```

The results are a single row:

```text
 --------------------------------------------------------------
 | Average | Count | ColumnCount | Maximum | Minimum | Sum    |
 --------------------------------------------------------------
 | 3,911   | 10    | 9           | 6,200   | 1,500   | 35,200 |
 --------------------------------------------------------------
```

## Distinct column values

When using the `countcolumn` aggregate function, you can set the `distinct` attribute to return a count of unique values for the column.

```xml
<attribute name='numberofemployees' 
   alias='ColumnCount' 
   aggregate='countcolumn' 
   distinct='true' />
```

When set for the previous query, the results return 8 rather than 9 because two rows in the data set have 2,900 as the number of employees value.

## Grouping

Group the results of an aggregate query by adding an [attribute element](reference/attribute.md) with the `groupby` attribute rather than the `aggregate` attribute. When grouping, you should specify an [order element](reference/order.md) with an `alias` value set to the `alias` of the group.

For example the following query returns the sum of employees, and count by city:

```xml
<fetch aggregate='true'>
   <entity name='account'>
      <attribute name='numberofemployees'
         alias='Total'
         aggregate='sum' />
      <attribute name='address1_city'
         alias='Count'
         aggregate='count' />
      <attribute name='address1_city'
         alias='City'
         groupby='true' />
      <order alias='City' />
   </entity>
</fetch>
```

The query groups the results by City value, combining the results for the three rows where city is 'Redmond'.

| Total  | Count | City        |
|--------|-------|-------------|
| 0      | 1     | NULL        |
| 6,000  | 1     | Dallas      |
| 2,900  | 1     | Los Angeles |
| 2,700  | 1     | Lynnwood    |
| 4,800  | 1     | Missoula    |
| 3,900  | 1     | Phoenix     |
| 10,600 | 3     | Redmond     |
| 4,300  | 1     | Santa Cruz  |


### Grouping by parts of a date

You can select which part of the date to use when grouping by date. Set [attribute element](reference/attribute.md) `dategrouping` attribute to one of the following values:

[!INCLUDE [dategrouping-table](reference/includes/dategrouping-table.md)]

By default date groupings use the user's time zone. Set the [attribute element](reference/attribute.md) `usertimezone` attribute to `"false"` to specify that the UTC time zone be used instead.

The following query groups account records showing number of employees by when the records were created:

```xml
<fetch aggregate='true'>
   <entity name='account'>
      <attribute name='numberofemployees'
         alias='Total'
         aggregate='sum' />
      <attribute name='createdon'
         alias='Day'
         groupby='true'
         dategrouping='day' />
      <attribute name='createdon'
         alias='Week'
         groupby='true'
         dategrouping='week' />
      <attribute name='createdon'
         alias='Month'
         groupby='true'
         dategrouping='month' />
      <attribute name='createdon'
         alias='Year'
         groupby='true'
         dategrouping='year' />
      <attribute name='createdon'
         alias='FiscalPeriod'
         groupby='true'
         dategrouping='fiscal-period' />
      <attribute name='createdon'
         alias='FiscalYear'
         groupby='true'
         dategrouping='fiscal-year' />
      <order alias='Month' />
   </entity>
</fetch>
```

The following table shows the result using the [example](#example) data set mentioned previously:

```text
 -----------------------------------------------------------------------
 | Total  | Day | Week | Month | Year  | FiscalPeriod     | FiscalYear |
 -----------------------------------------------------------------------
 | 35,200 | 25  | 12   | 3     | 2,023 | Quarter 1 FY2023 | FY2023     |
 -----------------------------------------------------------------------
 | 0      | 27  | 35   | 8     | 2,023 | Quarter 3 FY2023 | FY2023     |
 -----------------------------------------------------------------------
```

#### Fiscal period date grouping example

The following example shows a FetchXML aggregation expression that sums the total number of orders fulfilled and groups the result by fiscal semester and fiscal year.

```xml
<fetch aggregate="true">
   <entity name="order">
      <attribute name="totalamount"
         aggregate="sum"
         alias="total" />
      <attribute name="datefulfilled"
         groupby="true"
         dategrouping="fiscal-period" />
   </entity>
</fetch>
```

## Row aggregate

When a table has a [hierarchical relationship defined](../../../maker/data-platform/query-visualize-hierarchical-data.md), you can return a row aggregate on the lookup column for the hierarchical relationship.

The following example returns the number of related accounts in a column named `CountChildren` when the child account records `parentaccountid` column equals the current account `accountid` column.

```xml
<fetch top='5'>
   <entity name='account'>
      <attribute name='name' />
      <attribute name='accountid'
         alias='numberOfChildren'
         rowaggregate='CountChildren' />
      <order attribute='accountid'
         descending='true' />
   </entity>
</fetch>
```

[!INCLUDE [cc-query-aggregation-limitations](../includes/cc-query-aggregation-limitations.md)]

### Per query limit

Even with the default limit for aggregate queries applied, the query might take some time to complete. You can use the `aggregatelimit` attribute in a query to apply a custom lower limit that returns the `AggregateQueryRecordLimit exceeded` error if the results are higher than your custom limit.

In this example, the custom maximum rows limit is 10:

```xml
<fetch aggregate='true'
   aggregatelimit = '10'>
   <entity name='opportunity'>
      <attribute name='name'
         alias='opportunity_count'
         aggregate='count' />
   </entity>
</fetch>
```

The per query limit can't exceed default aggregate limit.

## Next steps

Learn how to count rows.

> [!div class="nextstepaction"]
> [Count rows](count-rows.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
