---
title: Aggregate data using QueryExpression
description: Learn how to use QueryExpression to retrieve aggregated data from Microsoft Dataverse.
ms.date: 04/11/2025
ms.reviewer: jdaly
ms.topic: how-to
author: olegovanesyan
ms.subservice: dataverse-developer
ms.author: olegov
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - daryllabar
---
# Aggregate data using QueryExpression

[QueryExpression](xref:Microsoft.Xrm.Sdk.Query.QueryExpression) includes grouping and aggregation features that let you calculate sum, average, min, max, and count across multiple rows of data.

To return an aggregate value, you must:

- Leave the [ColumnSet.AllColumns property](xref:Microsoft.Xrm.Sdk.Query.ColumnSet.AllColumns) set to `false`. Don't set it using the [ColumnSet(Boolean) constructor](xref:Microsoft.Xrm.Sdk.Query.ColumnSet.%23ctor(System.Boolean)).
- Add instances of the [XrmAttributeExpression class](xref:Microsoft.Xrm.Sdk.Query.XrmAttributeExpression) to the [ColumnSet.AttributeExpressions](xref:Microsoft.Xrm.Sdk.Query.ColumnSet.AttributeExpressions) collection
- For each column that you want to return, set these properties:

   |XrmAttributeExpression Property|Description|
   |---------|---------|
   |[AttributeName](xref:Microsoft.Xrm.Sdk.Query.XrmAttributeExpression.AttributeName)|The `LogicalName` of the column|
   |[Alias](xref:Microsoft.Xrm.Sdk.Query.XrmAttributeExpression.Alias)|The alias value for the column|

- For each column that you want to aggregate, set the [AggregateType](xref:Microsoft.Xrm.Sdk.Query.XrmAttributeExpression.AggregateType) to the type of aggregation you want to perform. [Learn about types of aggregation](#types-of-aggregation)

- For each column that you want to group the results by, set these properties:

   |XrmAttributeExpression Property|Description|
   |---------|---------|
   [AggregateType](xref:Microsoft.Xrm.Sdk.Query.XrmAttributeExpression.AggregateType)|Set to [XrmAggregateType](xref:Microsoft.Xrm.Sdk.Query.XrmAggregateType.None)`.None`|
   |[HasGroupBy](xref:Microsoft.Xrm.Sdk.Query.XrmAttributeExpression.HasGroupBy)|Set to `true`.|
   |[DateTimeGrouping](xref:Microsoft.Xrm.Sdk.Query.XrmAttributeExpression.DateTimeGrouping)|When the grouping involves datetime values, specify the type of datetime grouping to apply using the [XrmDateTimeGrouping enum](xref:Microsoft.Dynamics.CRM.XrmDateTimeGrouping) members. [Learn about grouping by parts of a date](#grouping-by-parts-of-a-date)|

## Types of aggregation

The types of aggregation you can do are members of the [XrmAggregateType enum](xref:Microsoft.Xrm.Sdk.Query.XrmAggregateType).


|XrmAggregateType member|Description |
|---------|---------|
|`Avg`|The average value of the column values with data.|
|`Count`|The number of rows.|
|`CountColumn`|The number of rows with data in that column.|
|`Max`|The maximum value of the rows in that column.|
|`Min`|The minimum value of the rows in that column.|
|`None`|Use this when the column is used to group the aggregated data. The [HasGroupBy](xref:Microsoft.Xrm.Sdk.Query.XrmAttributeExpression.HasGroupBy) value must be set to `true`.|
|`Sum`|The total value of the column values with data.|


Note the following points:

- Null values aren't considered when calculating aggregate values.
- Aggregated data is returned as an [AliasedValue](xref:Microsoft.Xrm.Sdk.AliasedValue).
- You can use data from tables joined using the [LinkEntity class](xref:Microsoft.Xrm.Sdk.Query.LinkEntity).
- You can apply filters to limit the results as with any query.

## Example

Let's say you have 10 account records with the following data:

|Number of Employees|Name|Address 1 City|Created On|
|---------|---------|---------|---------|
|NULL|Example Account|NULL|8/27/2023|
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

```csharp
QueryExpression query = new()
{
    EntityName = "account",
    ColumnSet = new ColumnSet(false)
    {
        AttributeExpressions = {
            {
                new XrmAttributeExpression(
                    attributeName: "numberofemployees",
                    alias: "Average",
                    aggregateType: XrmAggregateType.Avg)
            },
            {
                new XrmAttributeExpression(
                    attributeName: "numberofemployees",
                    alias: "Count",
                    aggregateType: XrmAggregateType.Count)
            },
            {
                new XrmAttributeExpression(
                    attributeName: "numberofemployees",
                    alias: "ColumnCount",
                    aggregateType: XrmAggregateType.CountColumn)
            },
            {
                new XrmAttributeExpression(
                    attributeName: "numberofemployees",
                    alias: "Maximum",
                    aggregateType: XrmAggregateType.Max)
            },
            {
                new XrmAttributeExpression(
                    attributeName: "numberofemployees",
                    alias: "Minimum",
                    aggregateType: XrmAggregateType.Min)
            },
            {
                new XrmAttributeExpression(
                    attributeName: "numberofemployees",
                    alias: "Sum",
                    aggregateType: XrmAggregateType.Sum)
            }
        }
    }
};
```

The results are a single row:

```text
 --------------------------------------------------------------
 | Average | Count | ColumnCount | Maximum | Minimum | Sum    |
 --------------------------------------------------------------
 | 3,911   | 10    | 9           | 6,200   | 1,500   | 35,200 |
 --------------------------------------------------------------
```

## Grouping

Group the results of an aggregate query by adding an [XrmAttributeExpression](xref:Microsoft.Xrm.Sdk.Query.XrmAttributeExpression) with the [HasGroupBy property](xref:Microsoft.Xrm.Sdk.Query.XrmAttributeExpression.HasGroupBy) [AggregateType](xref:Microsoft.Xrm.Sdk.Query.XrmAttributeExpression.AggregateType) set to [XrmAggregateType](xref:Microsoft.Xrm.Sdk.Query.XrmAggregateType)`.None`.

When grouping, you should specify a [QueryExpression.Orders](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.Orders) with an [OrderExpression](xref:Microsoft.Xrm.Sdk.Query.OrderExpression) that has the [Alias property](xref:Microsoft.Xrm.Sdk.Query.OrderExpression.Alias) set to the alias of the group.

If a grouped by value is null, it doesn't appear in the results.


For example the following query returns the sum of employees, and count by city:

```csharp
QueryExpression query = new()
{
      EntityName = "account",
      ColumnSet = new ColumnSet(false)
   {
         AttributeExpressions = {
            {
                  new XrmAttributeExpression(
                     attributeName: "numberofemployees",
                     alias: "Total",
                     aggregateType: XrmAggregateType.Sum)
            },
            {
                  new XrmAttributeExpression(
                     attributeName: "address1_city",
                     alias: "Count",
                     aggregateType: XrmAggregateType.Count)
            },
            {
                  new XrmAttributeExpression(
                     attributeName: "address1_city",
                     alias: "City",
                     aggregateType: XrmAggregateType.None){
                     HasGroupBy = true
            }
         }
      }
   }
};
query.Orders.Add(new OrderExpression(
            attributeName: "address1_city",
            alias: "City",
            orderType: OrderType.Ascending));
```


The query groups the results by `City` value, combining the results for the three rows where city is 'Redmond'.

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

You can select which part of the date to use when grouping by date. Set the [XrmAttributeExpression.DateTimeGrouping](xref:Microsoft.Xrm.Sdk.Query.XrmAttributeExpression.DateTimeGrouping) to one of the [XrmDateTimeGrouping enum](xref:Microsoft.Xrm.Sdk.Query.XrmDateTimeGrouping) members.

|XrmDateTimeGrouping member|Description |
|---------|---------|
|`None`|No DateTime grouping|
|`Day`|Group by Day|
|`Week`|Group by Week|
|`Month`|Group by Month|
|`Quarter`|Group by Quarter|
|`Year`|Group by Year|
|`FiscalPeriod`|Group by FiscalPeriod|
|`FiscalYear`|Group by FiscalYear|

The following query groups account records showing number of employees by when the records were created:

```csharp
QueryExpression query = new()
{
    EntityName = "account",
    ColumnSet = new ColumnSet(false)
    {
        AttributeExpressions = {
            {
                new XrmAttributeExpression(
                    attributeName: "numberofemployees",
                    alias: "Total",
                    aggregateType: XrmAggregateType.Sum)
            },
            {
                new XrmAttributeExpression(
                    attributeName: "createdon",
                    alias: "Day",
                    aggregateType: XrmAggregateType.None){
                    HasGroupBy = true,
                    DateTimeGrouping = XrmDateTimeGrouping.Day
                }
            },
            {
                new XrmAttributeExpression(
                    attributeName: "createdon",
                    alias: "Week",
                    aggregateType: XrmAggregateType.None){
                    HasGroupBy = true,
                    DateTimeGrouping = XrmDateTimeGrouping.Week
                }
            },
                                    {
                new XrmAttributeExpression(
                    attributeName: "createdon",
                    alias: "Month",
                    aggregateType: XrmAggregateType.None){
                    HasGroupBy = true,
                    DateTimeGrouping = XrmDateTimeGrouping.Month
                }
            },
            {
                new XrmAttributeExpression(
                    attributeName: "createdon",
                    alias: "Year",
                    aggregateType: XrmAggregateType.None){
                    HasGroupBy = true,
                    DateTimeGrouping = XrmDateTimeGrouping.Year
                }
            },
            {
                new XrmAttributeExpression(
                    attributeName: "createdon",
                    alias: "FiscalPeriod",
                    aggregateType: XrmAggregateType.None){
                    HasGroupBy = true,
                    DateTimeGrouping = XrmDateTimeGrouping.FiscalPeriod
                }
            },
            {
                new XrmAttributeExpression(
                    attributeName: "createdon",
                    alias: "FiscalYear",
                    aggregateType: XrmAggregateType.None){
                    HasGroupBy = true,
                    DateTimeGrouping = XrmDateTimeGrouping.FiscalYear
                }
            }
        }
    }
};
query.Orders.Add(new OrderExpression(
            attributeName: "createdon",
            alias: "Month",
            orderType: OrderType.Ascending));
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

The following example shows a [QueryExpression](xref:Microsoft.Xrm.Sdk.Query.QueryExpression) that sums the total number of orders fulfilled and groups the result by fiscal semester and fiscal year.

```csharp
QueryExpression query = new()
{
    EntityName = "salesorder",
    ColumnSet = new ColumnSet(false)
    {
        AttributeExpressions = {
            {
                new XrmAttributeExpression(
                    attributeName: "totalamount",
                    alias: "total",
                    aggregateType: XrmAggregateType.Sum)
            },
            {
                new XrmAttributeExpression(
                    attributeName: "datefulfilled",
                    alias: "date",
                    aggregateType: XrmAggregateType.None){
                    HasGroupBy = true,
                    DateTimeGrouping = XrmDateTimeGrouping.FiscalPeriod
                }
            }
        }
    }
};
query.Orders.Add(new OrderExpression(
            attributeName: "datefulfilled",
            alias: "Date",
            orderType: OrderType.Ascending));
```



## QueryExpression aggregation limitations

This section describes capabilities that are available using aggregation with FetchXml that are not currently available using [QueryExpression](xref:Microsoft.Xrm.Sdk.Query.QueryExpression).

### Get distinct number with CountColumn

You can't get a distinct number of values using [CountColumn](xref:Microsoft.Xrm.Sdk.Query.XrmAggregateType.CountColumn) with QueryExpression. [Learn about distinct column values using FetchXml](../../fetchxml/aggregate-data.md#distinct-column-values)


### Time zone when grouping by date

Grouping by parts of a date always uses UTC time and there is no way to specify that the user's time zone should be used instead [available in FetchXml](../../fetchxml/aggregate-data.md#grouping-by-parts-of-a-date)


### Row aggregate

When a table has a [hierarchical relationship defined](../../../../maker/data-platform/query-visualize-hierarchical-data.md), you can't return a row aggregate on the lookup column for the hierarchical relationship. [Learn about row aggregates using FetchXml](../../fetchxml/aggregate-data.md#row-aggregate)



### Per query limit

There is no way to specify a configurable aggregate limit. [Learn about per query limits using FetchXml](../../fetchxml/aggregate-data.md#per-query-limit)


[!INCLUDE [cc-query-aggregation-limitations](../../includes/cc-query-aggregation-limitations.md)]

## Next steps

Learn how to count rows.

> [!div class="nextstepaction"]
> [Count rows](count-rows.md)


[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
