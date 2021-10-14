---
title: "Use FetchXML aggregation (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about the grouping and aggregation features of FetchXML that let you calculate sum, average min, max and count." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 09/27/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Use FetchXML aggregation

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

In Microsoft Dataverse, `FetchXML` includes grouping and aggregation features that let you calculate sum, average min, max and count.  
  
 The following aggregate functions are supported:  
  
- sum  
- avg  
- min  
- max  
- count(*)  
- count(*attribute name*)
  
<a name="Aggregation"></a>

## About aggregation

To create an aggregate column (attribute), set the keyword `aggregate` to `true`, then specify a valid *entity name*, *attribute name*, and *alias* (variable name). You must also specify the type of aggregation you want to perform.  
  
The following example shows a simple aggregate column in `FetchXML`.  
  
```xml  
<fetch distinct='false' mapping='logical' aggregate='true'>   
   <entity name='entity name'>   
      <attribute name='attribute name' aggregate='count' alias='alias name'/>   
   </entity>   
</fetch>
```  
  
The result of a query with an aggregate column is different from the results of a standard query. The alias value is used as the tag identifier for the aggregate result.  
  
The following example shows the format of the result of an aggregate query.  
  
```xml
<resultset morerecords="0"'>   
   <result>  
      <alias>aggregate value</alias>  
   </result>  
</resultset>
```  
  
The following example shows the results of a query when the alias variable is set to `account_count`.  
  
```xml
<resultset morerecords="0"'>   
   <result>  
      <account_count>20</account_count>  
   </result>  
</resultset>
```  

<a name="Limitations"></a>

## Limitations

Queries that return aggregate values are limited to 50,000 records. This limit helps maintain system performance and reliability. If the filter criteria in your query includes more than 50,000 records you will get the following error:

Error code: `-2147164125`<br />
Hexadecimal error code: `8004E023`<br />
Platform error message: `AggregateQueryRecordLimit exceeded. Cannot perform this operation.`<br />
Client error message: The maximum record limit is exceeded. Reduce the number of records.<br />

To avoid this error add appropriate filters to your query to ensure that it will not need to evaluate more than 50,000 records. Then run you query multiple times and combine the results.

> [!TIP]
> If you want to get a total count of records with no filter, use the `RetrieveTotalRecordCount` message with either the Web API <xref href="Microsoft.Dynamics.CRM.RetrieveTotalRecordCount?text=RetrieveTotalRecordCount Function" /> or with the Organization service <xref:Microsoft.Crm.Sdk.Messages.RetrieveTotalRecordCountRequest> message class. The data retrieved will be from a snapshot within the last 24 hours.
  
<a name="AVG"></a>

## Avg

 The following example shows how to use the `avg` `aggregate` column.  
  
 ```csharp
// Fetch the average of estimatedvalue for all opportunities.  This is the equivalent of 
// SELECT AVG(estimatedvalue) AS estimatedvalue_avg ... in SQL.
string estimatedvalue_avg = @" 
<fetch distinct='false' mapping='logical' aggregate='true'> 
    <entity name='opportunity'> 
       <attribute name='estimatedvalue' alias='estimatedvalue_avg' aggregate='avg' /> 
    </entity> 
</fetch>";

EntityCollection estimatedvalue_avg_result = _serviceProxy.RetrieveMultiple(new FetchExpression(estimatedvalue_avg));

foreach (var c in estimatedvalue_avg_result.Entities)
{
    decimal aggregate1 = ((Money)((AliasedValue)c["estimatedvalue_avg"]).Value).Value;
    System.Console.WriteLine("Average estimated value: " + aggregate1);

}
```
  
### Limitation with null values while computing average

**Null** values are not considered when Dataverse computes the average of data. However, zero (0) is used.  
  
In the following example, with the following data, the average for Account 1 (two entries) is shown as 250 whereas the average for Account 2 (two entries) is shown as 125.  
  
|Topic|Potential Customer|Estimated value|  
|-----|------------------|---------------|  
|Opportunity 1|Account 1|null|  
|Opportunity 2|Account 1|250|  
|Opportunity 3|Account 2|0|  
|Opportunity 4|Account 2|250|  
  
<a name="count"></a>

## Count

The following example shows how to use the `count` `aggregate` column.  
  
 ```csharp
// *****************************************************************************************************************
//                FetchXML      opportunity_count   Aggregate 2
// *****************************************************************************************************************
// Fetch the count of all opportunities.  This is the equivalent of
// SELECT COUNT(*) AS opportunity_count ... in SQL.
string opportunity_count = @" 
<fetch distinct='false' mapping='logical' aggregate='true'> 
    <entity name='opportunity'> 
       <attribute name='name' alias='opportunity_count' aggregate='count'/> 
    </entity> 
</fetch>";

EntityCollection opportunity_count_result = _serviceProxy.RetrieveMultiple(new FetchExpression(opportunity_count));

foreach (var c in opportunity_count_result.Entities)
{
    Int32 aggregate2 = (Int32)((AliasedValue)c["opportunity_count"]).Value;
    System.Console.WriteLine("Count of all opportunities: " + aggregate2); 

}
```
  
<a name="count_column"></a>

### CountColumn

The following example shows how to use the `countcolumn` `aggregate` column to count columns.  
  
 ```csharp
// *****************************************************************************************************************
//                FetchXML      opportunity_colcount   Aggregate 3
// *****************************************************************************************************************
// Fetch the count of all opportunities.  This is the equivalent of 
// SELECT COUNT(name) AS opportunity_count ... in SQL.
string opportunity_colcount = @" 
<fetch distinct='false' mapping='logical' aggregate='true'> 
    <entity name='opportunity'> 
       <attribute name='name' alias='opportunity_colcount' aggregate='countcolumn'/> 
    </entity> 
</fetch>";

EntityCollection opportunity_colcount_result = _serviceProxy.RetrieveMultiple(new FetchExpression(opportunity_colcount));

foreach (var c in opportunity_colcount_result.Entities)
{
    Int32 aggregate3 = (Int32)((AliasedValue)c["opportunity_colcount"]).Value;
    System.Console.WriteLine("Column count of all opportunities: " + aggregate3);

}
```
  
<a name="count_distinct"></a>
 
### Count distinct columns

The following example shows how to use the `countcolumn` `aggregate` column with the `distinct` column to count distinct columns.  
  
 ```csharp
// *****************************************************************************************************************
//                FetchXML      opportunity_distcount   Aggregate 4
// *****************************************************************************************************************
// Fetch the count of distinct names for opportunities.  This is the equivalent of 
// SELECT COUNT(DISTINCT name) AS opportunity_count ... in SQL.
string opportunity_distcount = @" 
<fetch distinct='false' mapping='logical' aggregate='true'> 
    <entity name='opportunity'> 
       <attribute name='name' alias='opportunity_distcount' aggregate='countcolumn' distinct='true'/> 
    </entity> 
</fetch>";

EntityCollection opportunity_distcount_result = _serviceProxy.RetrieveMultiple(new FetchExpression(opportunity_distcount));

foreach (var c in opportunity_distcount_result.Entities)
{
    Int32 aggregate4 = (Int32)((AliasedValue)c["opportunity_distcount"]).Value;
    System.Console.WriteLine("Distinct name count of all opportunities: " + aggregate4);

}
```
  
<a name="max"></a>

## Max

**Null** values are not considered when Dataverse computes the maximum of data. However, zero (0) is used.  
  
The following example shows how to use the `max` `aggregate` column.  
  
 ```csharp
// *****************************************************************************************************************
//                FetchXML      estimatedvalue_max   Aggregate 5
// *****************************************************************************************************************
// Fetch the maximum estimatedvalue of all opportunities.  This is the equivalent of 
// SELECT MAX(estimatedvalue) AS estimatedvalue_max ... in SQL.
string estimatedvalue_max = @" 
<fetch distinct='false' mapping='logical' aggregate='true'> 
    <entity name='opportunity'> 
        <attribute name='estimatedvalue' alias='estimatedvalue_max' aggregate='max' /> 
    </entity> 
</fetch>";

EntityCollection estimatedvalue_max_result = service.RetrieveMultiple(new FetchExpression(estimatedvalue_max));

foreach (var c in estimatedvalue_max_result.Entities)
{
    decimal aggregate5 = ((Money)((AliasedValue)c["estimatedvalue_max"]).Value).Value;
    Console.WriteLine("Max estimated value of all opportunities: " + aggregate5);

}
```
  
<a name="min"></a>
 
## Min

**Null** values are not considered when Dataverse computes the minimum of data. However, zero (0) is used.  
  
The following example shows how to use the `min``aggregate` column.  
  
 ```csharp
// *****************************************************************************************************************
//                FetchXML      estimatedvalue_min   Aggregate 6
// *****************************************************************************************************************
// Fetch the minimum estimatedvalue of all opportunities.  This is the equivalent of 
// SELECT MIN(estimatedvalue) AS estimatedvalue_min ... in SQL.
string estimatedvalue_min = @" 
<fetch distinct='false' mapping='logical' aggregate='true'> 
    <entity name='opportunity'> 
       <attribute name='estimatedvalue' alias='estimatedvalue_min' aggregate='min' /> 
    </entity> 
</fetch>";

EntityCollection estimatedvalue_min_result = _serviceProxy.RetrieveMultiple(new FetchExpression(estimatedvalue_min));

foreach (var c in estimatedvalue_min_result.Entities)
{
    decimal aggregate6 = ((Money)((AliasedValue)c["estimatedvalue_min"]).Value).Value;
    System.Console.WriteLine("Minimum estimated value of all opportunities: " + aggregate6);

}
```
  
<a name="sum"></a>

## Sum

The following example shows how to use the `sum``aggregate` column.  
  
 ```csharp
// *****************************************************************************************************************
//                FetchXML      estimatedvalue_sum   Aggregate 7
// *****************************************************************************************************************
// Fetch the sum of estimatedvalue for all opportunities.  This is the equivalent of 
// SELECT SUM(estimatedvalue) AS estimatedvalue_sum ... in SQL.
string estimatedvalue_sum = @" 
<fetch distinct='false' mapping='logical' aggregate='true'> 
    <entity name='opportunity'> 
       <attribute name='estimatedvalue' alias='estimatedvalue_sum' aggregate='sum' /> 
    </entity> 
</fetch>";

EntityCollection estimatedvalue_sum_result = _serviceProxy.RetrieveMultiple(new FetchExpression(estimatedvalue_sum));

foreach (var c in estimatedvalue_sum_result.Entities)
{
    decimal aggregate7 = ((Money)((AliasedValue)c["estimatedvalue_sum"]).Value).Value;
    System.Console.WriteLine("Sum of estimated value of all opportunities: " + aggregate7);

}
```
  
<a name="mult_agg"></a>
 
## Multiple aggregates

The following example shows how to use multiple `aggregate` columns to set a minimum and maximum.  
  
 ```csharp
// *****************************************************************************************************************
//                FetchXML      estimatedvalue_avg, estimatedvalue_sum   Aggregate 8
// *****************************************************************************************************************
// Fetch multiple aggregate values within a single query.
string estimatedvalue_avg2 = @" 
<fetch distinct='false' mapping='logical' aggregate='true'> 
    <entity name='opportunity'> 
       <attribute name='opportunityid' alias='opportunity_count' aggregate='count'/> 
       <attribute name='estimatedvalue' alias='estimatedvalue_sum' aggregate='sum'/> 
       <attribute name='estimatedvalue' alias='estimatedvalue_avg' aggregate='avg'/> 
    </entity> 
</fetch>";

EntityCollection estimatedvalue_avg2_result = _serviceProxy.RetrieveMultiple(new FetchExpression(estimatedvalue_avg2));

foreach (var c in estimatedvalue_avg2_result.Entities)
{
    Int32 aggregate8a = (Int32)((AliasedValue)c["opportunity_count"]).Value;
    System.Console.WriteLine("Count of all opportunities: " + aggregate8a);
    decimal aggregate8b = ((Money)((AliasedValue)c["estimatedvalue_sum"]).Value).Value;
    System.Console.WriteLine("Sum of estimated value of all opportunities: " + aggregate8b);
    decimal aggregate8c = ((Money)((AliasedValue)c["estimatedvalue_avg"]).Value).Value;
    System.Console.WriteLine("Average of estimated value of all opportunities: " + aggregate8c);

}
```
  
<a name="groupby"></a>
 
## Group by

The following example shows how to use multiple `aggregate` columns and a linked `groupby` column.  
  
 ```csharp
// *****************************************************************************************************************
//                FetchXML      groupby1   Aggregate 9
// *****************************************************************************************************************
// Fetch a list of users with a count of all the opportunities they own using groupby.
string groupby1 = @" 
<fetch distinct='false' mapping='logical' aggregate='true'> 
    <entity name='opportunity'> 
       <attribute name='name' alias='opportunity_count' aggregate='countcolumn' /> 
       <attribute name='ownerid' alias='ownerid' groupby='true' /> 
    </entity> 
</fetch>";

EntityCollection groupby1_result = _serviceProxy.RetrieveMultiple(new FetchExpression(groupby1));

foreach (var c in groupby1_result.Entities)
{
    Int32 aggregate9a = (Int32)((AliasedValue)c["opportunity_count"]).Value;
    System.Console.WriteLine("Count of all opportunities: " + aggregate9a + "\n");
    string aggregate9b = ((EntityReference)((AliasedValue)c["ownerid"]).Value).Name;
    System.Console.WriteLine("Owner: " + aggregate9b);
    string aggregate9c = (string)((AliasedValue)c["ownerid_owneridyominame"]).Value;
    System.Console.WriteLine("Owner: " + aggregate9c);
    string aggregate9d = (string)((AliasedValue)c["ownerid_owneridyominame"]).Value;
    System.Console.WriteLine("Owner: " + aggregate9d);
}
```
  
The samples below show the following group by examples:  
  
- [Group by with linked entity](use-fetchxml-aggregation.md#groupby_linked)
- [Group by year](use-fetchxml-aggregation.md#groupby_year)
- [Group by quarter](use-fetchxml-aggregation.md#groupby_quarter)
- [Group by month](use-fetchxml-aggregation.md#groupby_month)
- [Group by week](use-fetchxml-aggregation.md#groupby_week)  
- [Group by day](use-fetchxml-aggregation.md#groupby_day)  
- [Multiple group by](use-fetchxml-aggregation.md#Multiple_GroupBy)  
  
<a name="groupby_linked"></a>

### Group by with linked entity

The following example shows how to use the `sum``aggregate` columns to sum linked table values.  
  
 ```csharp
// *****************************************************************************************************************
//                FetchXML      groupby2   Aggregate 10
// *****************************************************************************************************************
// Fetch the number of opportunities each manager's direct reports 
// own using a groupby within a link-entity.
string groupby2 = @" 
<fetch distinct='false' mapping='logical' aggregate='true'> 
    <entity name='opportunity'> 
       <attribute name='name' alias='opportunity_count' aggregate='countcolumn' /> 
       <link-entity name='systemuser' from='systemuserid' to='ownerid'>
           <attribute name='parentsystemuserid' alias='managerid' groupby='true' />
       </link-entity> 
    </entity> 
</fetch>";

EntityCollection groupby2_result = _serviceProxy.RetrieveMultiple(new FetchExpression(groupby2));

foreach (var c in groupby2_result.Entities)
{

      int? aggregate10a = (int?)((AliasedValue)c["opportunity_count"]).Value;
      System.Console.WriteLine("Count of all opportunities: " + aggregate10a + "\n");
}
```
  
<a name="groupby_year"></a>

### Group by year

Group By for dates uses the day, week, month, quarter, or year value. The following example shows how to use the `aggregate` column and the `groupby` column to group the results by year.  
  
 ```csharp

// *****************************************************************************************************************
//                FetchXML      byyear   Aggregate 11           
// *****************************************************************************************************************
// Fetch aggregate information about the opportunities that have 
// been won by year.
string byyear = @" 
<fetch distinct='false' mapping='logical' aggregate='true'> 
    <entity name='opportunity'> 
       <attribute name='opportunityid' alias='opportunity_count' aggregate='count'/> 
       <attribute name='estimatedvalue' alias='estimatedvalue_sum' aggregate='sum'/> 
       <attribute name='estimatedvalue' alias='estimatedvalue_avg' aggregate='avg'/> 
       <attribute name='actualclosedate' groupby='true' dategrouping='year' alias='year' />
       <filter type='and'>
           <condition attribute='statecode' operator='eq' value='Won' />
       </filter>
    </entity> 
</fetch>";

EntityCollection byyear_result = _serviceProxy.RetrieveMultiple(new FetchExpression(byyear));

foreach (var c in byyear_result.Entities)
{
    Int32 aggregate11 = (Int32)((AliasedValue)c["year"]).Value;
    System.Console.WriteLine("Year: " + aggregate11);                      
    Int32 aggregate11a = (Int32)((AliasedValue)c["opportunity_count"]).Value;
    System.Console.WriteLine("Count of all opportunities: " + aggregate11a);
    decimal aggregate11b = ((Money)((AliasedValue)c["estimatedvalue_sum"]).Value).Value;
    System.Console.WriteLine("Sum of estimated value of all opportunities: " + aggregate11b);
    decimal aggregate11c = ((Money)((AliasedValue)c["estimatedvalue_avg"]).Value).Value;
    System.Console.WriteLine("Average of estimated value of all opportunities: " + aggregate11c);
    System.Console.WriteLine("----------------------------------------------");
}
```
  
<a name="groupby_quarter"></a>
 
### Group by quarter

The following example shows how to use the `aggregate` column and the `groupby` column to group the results by quarter.  
  
 ```csharp
 // *****************************************************************************************************************
 //                FetchXML      byquarter   Aggregate 12           
 // *****************************************************************************************************************
// Fetch aggregate information about the opportunities that have 
 // been won by quarter.(returns 1-4)
 string byquarter = @" 
 <fetch distinct='false' mapping='logical' aggregate='true'> 
     <entity name='opportunity'> 
        <attribute name='opportunityid' alias='opportunity_count' aggregate='count'/> 
        <attribute name='estimatedvalue' alias='estimatedvalue_sum' aggregate='sum'/> 
        <attribute name='estimatedvalue' alias='estimatedvalue_avg' aggregate='avg'/> 
        <attribute name='actualclosedate' groupby='true' dategrouping='quarter' alias='quarter' />
        <filter type='and'>
            <condition attribute='statecode' operator='eq' value='Won' />
        </filter>
     </entity> 
 </fetch>";

 EntityCollection byquarter_result = _serviceProxy.RetrieveMultiple(new FetchExpression(byquarter));

 foreach (var c in byquarter_result.Entities)
 {
     Int32 aggregate12 = (Int32)((AliasedValue)c["quarter"]).Value;
     System.Console.WriteLine("Quarter: " + aggregate12);
     Int32 aggregate12a = (Int32)((AliasedValue)c["opportunity_count"]).Value;
     System.Console.WriteLine("Count of all opportunities: " + aggregate12a);
     decimal aggregate12b = ((Money)((AliasedValue)c["estimatedvalue_sum"]).Value).Value;
     System.Console.WriteLine("Sum of estimated value of all opportunities: " + aggregate12b);
     decimal aggregate12c = ((Money)((AliasedValue)c["estimatedvalue_avg"]).Value).Value;
     System.Console.WriteLine("Average of estimated value of all opportunities: " + aggregate12c);
     System.Console.WriteLine("----------------------------------------------");
 }
```
  
<a name="groupby_month"></a>

### Group by month

The following example shows how to use the `aggregate` column and the `groupby` column to group the results by month.  
  
```csharp
// *****************************************************************************************************************
//                FetchXML      bymonth   Aggregate 13           
// *****************************************************************************************************************
// Fetch aggregate information about the opportunities that have 
// been won by month. (returns 1-12)
string bymonth = @" 
<fetch distinct='false' mapping='logical' aggregate='true'> 
    <entity name='opportunity'> 
       <attribute name='opportunityid' alias='opportunity_count' aggregate='count'/> 
       <attribute name='estimatedvalue' alias='estimatedvalue_sum' aggregate='sum'/> 
       <attribute name='estimatedvalue' alias='estimatedvalue_avg' aggregate='avg'/> 
       <attribute name='actualclosedate' groupby='true' dategrouping='month' alias='month' />
       <filter type='and'>
           <condition attribute='statecode' operator='eq' value='Won' />
       </filter>
    </entity> 
</fetch>";

EntityCollection bymonth_result = _serviceProxy.RetrieveMultiple(new FetchExpression(bymonth));

foreach (var c in bymonth_result.Entities)
{
    Int32 aggregate13 = (Int32)((AliasedValue)c["month"]).Value;
    System.Console.WriteLine("Month: " + aggregate13);
    Int32 aggregate13a = (Int32)((AliasedValue)c["opportunity_count"]).Value;
    System.Console.WriteLine("Count of all opportunities: " + aggregate13a);
    decimal aggregate13b = ((Money)((AliasedValue)c["estimatedvalue_sum"]).Value).Value;
    System.Console.WriteLine("Sum of estimated value of all opportunities: " + aggregate13b);
    decimal aggregate13c = ((Money)((AliasedValue)c["estimatedvalue_avg"]).Value).Value;
    System.Console.WriteLine("Average of estimated value of all opportunities: " + aggregate13c);
    System.Console.WriteLine("----------------------------------------------");
}
``` 

<a name="groupby_week"></a>

### Group by week

The following example shows how to use the `aggregate` column and the `groupby` column to group the results by week.  
  
 ```csharp
// *****************************************************************************************************************
//                FetchXML      byweek   Aggregate 14           
// *****************************************************************************************************************
// Fetch aggregate information about the opportunities that have 
// been won by week. (Returns 1-52)
string byweek = @" 
<fetch distinct='false' mapping='logical' aggregate='true'> 
    <entity name='opportunity'> 
       <attribute name='opportunityid' alias='opportunity_count' aggregate='count'/> 
       <attribute name='estimatedvalue' alias='estimatedvalue_sum' aggregate='sum'/> 
       <attribute name='estimatedvalue' alias='estimatedvalue_avg' aggregate='avg'/> 
       <attribute name='actualclosedate' groupby='true' dategrouping='week' alias='week' />
       <filter type='and'>
           <condition attribute='statecode' operator='eq' value='Won' />
       </filter>
    </entity> 
</fetch>";

EntityCollection byweek_result = _serviceProxy.RetrieveMultiple(new FetchExpression(byweek));

foreach (var c in byweek_result.Entities)
{
    Int32 aggregate14 = (Int32)((AliasedValue)c["week"]).Value;
    System.Console.WriteLine("Week: " + aggregate14);
    Int32 aggregate14a = (Int32)((AliasedValue)c["opportunity_count"]).Value;
    System.Console.WriteLine("Count of all opportunities: " + aggregate14a);
    decimal aggregate14b = ((Money)((AliasedValue)c["estimatedvalue_sum"]).Value).Value;
    System.Console.WriteLine("Sum of estimated value of all opportunities: " + aggregate14b);
    decimal aggregate14c = ((Money)((AliasedValue)c["estimatedvalue_avg"]).Value).Value;
    System.Console.WriteLine("Average of estimated value of all opportunities: " + aggregate14c);
    System.Console.WriteLine("----------------------------------------------");
}
```
  
<a name="groupby_day"></a>

### Group by day

 The following example shows how to use the `aggregate` column and the `groupby` column to group the results by day.  
  
 ```csharp
// *****************************************************************************************************************
//                FetchXML      byday   Aggregate 15           
// *****************************************************************************************************************
// Fetch aggregate information about the opportunities that have 
// been won by day. (Returns 1-31)
string byday = @" 
<fetch distinct='false' mapping='logical' aggregate='true'> 
    <entity name='opportunity'> 
       <attribute name='opportunityid' alias='opportunity_count' aggregate='count'/> 
       <attribute name='estimatedvalue' alias='estimatedvalue_sum' aggregate='sum'/> 
       <attribute name='estimatedvalue' alias='estimatedvalue_avg' aggregate='avg'/> 
       <attribute name='actualclosedate' groupby='true' dategrouping='day' alias='day' />
       <filter type='and'>
           <condition attribute='statecode' operator='eq' value='Won' />
       </filter>
    </entity> 
</fetch>";

EntityCollection byday_result = _serviceProxy.RetrieveMultiple(new FetchExpression(byday));

foreach (var c in byday_result.Entities)
{
    Int32 aggregate15 = (Int32)((AliasedValue)c["day"]).Value;
    System.Console.WriteLine("Day: " + aggregate15);
    Int32 aggregate15a = (Int32)((AliasedValue)c["opportunity_count"]).Value;
    System.Console.WriteLine("Count of all opportunities: " + aggregate15a);
    decimal aggregate15b = ((Money)((AliasedValue)c["estimatedvalue_sum"]).Value).Value;
    System.Console.WriteLine("Sum of estimated value of all opportunities: " + aggregate15b);
    decimal aggregate15c = ((Money)((AliasedValue)c["estimatedvalue_avg"]).Value).Value;
    System.Console.WriteLine("Average of estimated value of all opportunities: " + aggregate15c);
    System.Console.WriteLine("----------------------------------------------");
}
```
  
<a name="Multiple_GroupBy"></a>
 
### Multiple group by

The following example shows how to use the `aggregate` column and multiple `groupby` clauses.  
  
 ```csharp
// *****************************************************************************************************************
//                FetchXML      byyrqtr   Aggregate 16           
// *****************************************************************************************************************
// Fetch aggregate information about the opportunities that have 
// been won by year and quarter.
string byyrqtr = @" 
<fetch distinct='false' mapping='logical' aggregate='true'> 
    <entity name='opportunity'> 
       <attribute name='opportunityid' alias='opportunity_count' aggregate='count'/> 
       <attribute name='estimatedvalue' alias='estimatedvalue_sum' aggregate='sum'/> 
       <attribute name='estimatedvalue' alias='estimatedvalue_avg' aggregate='avg'/> 
       <attribute name='actualclosedate' groupby='true' dategrouping='quarter' alias='quarter' />
       <attribute name='actualclosedate' groupby='true' dategrouping='year' alias='year' />
       <filter type='and'>
           <condition attribute='statecode' operator='eq' value='Won' />
       </filter>
    </entity> 
</fetch>";

EntityCollection byyrqtr_result = _serviceProxy.RetrieveMultiple(new FetchExpression(byyrqtr));

foreach (var c in byyrqtr_result.Entities)
{
    Int32 aggregate16d = (Int32)((AliasedValue)c["year"]).Value;
    System.Console.WriteLine("Year: " + aggregate16d);
    Int32 aggregate16 = (Int32)((AliasedValue)c["quarter"]).Value;
    System.Console.WriteLine("Quarter: " + aggregate16);
    Int32 aggregate16a = (Int32)((AliasedValue)c["opportunity_count"]).Value;
    System.Console.WriteLine("Count of all opportunities: " + aggregate16a);
    decimal aggregate16b = ((Money)((AliasedValue)c["estimatedvalue_sum"]).Value).Value;
    System.Console.WriteLine("Sum of estimated value of all opportunities: " + aggregate16b);
    decimal aggregate16c = ((Money)((AliasedValue)c["estimatedvalue_avg"]).Value).Value;
    System.Console.WriteLine("Average of estimated value of all opportunities: " + aggregate16c);
    System.Console.WriteLine("----------------------------------------------");
}
```
  
<a name="orderby_aggregate"></a>

## Order by

The following example shows how to use the `aggregate` column and multiple `orderby` clauses.  
  
 ```csharp
// *****************************************************************************************************************
//                FetchXML      byyrqtr2   Aggregate 17           
// *****************************************************************************************************************
// Specify the result order for the previous sample.  Order by year, then quarter.
string byyrqtr2 = @" 
<fetch distinct='false' mapping='logical' aggregate='true'> 
    <entity name='opportunity'> 
       <attribute name='opportunityid' alias='opportunity_count' aggregate='count'/> 
       <attribute name='estimatedvalue' alias='estimatedvalue_sum' aggregate='sum'/> 
       <attribute name='estimatedvalue' alias='estimatedvalue_avg' aggregate='avg'/> 
       <attribute name='actualclosedate' groupby='true' dategrouping='quarter' alias='quarter' />
       <attribute name='actualclosedate' groupby='true' dategrouping='year' alias='year' />
       <order alias='year' descending='false' />
       <order alias='quarter' descending='false' />
       <filter type='and'>
           <condition attribute='statecode' operator='eq' value='Won' />
       </filter>
    </entity> 
</fetch>";

EntityCollection byyrqtr2_result = _serviceProxy.RetrieveMultiple(new FetchExpression(byyrqtr2));

foreach (var c in byyrqtr2_result.Entities)
{
    Int32 aggregate17 = (Int32)((AliasedValue)c["quarter"]).Value;
    System.Console.WriteLine("Quarter: " + aggregate17);
    Int32 aggregate17d = (Int32)((AliasedValue)c["year"]).Value;
    System.Console.WriteLine("Year: " + aggregate17d);
    Int32 aggregate17a = (Int32)((AliasedValue)c["opportunity_count"]).Value;
    System.Console.WriteLine("Count of all opportunities: " + aggregate17a);
    decimal aggregate17b = ((Money)((AliasedValue)c["estimatedvalue_sum"]).Value).Value;
    System.Console.WriteLine("Sum of estimated value of all opportunities: " + aggregate17b);
    decimal aggregate17c = ((Money)((AliasedValue)c["estimatedvalue_avg"]).Value).Value;
    System.Console.WriteLine("Average of estimated value of all opportunities: " + aggregate17c);
    System.Console.WriteLine("----------------------------------------------");
}
```
  
### See also

[Page large result sets with FetchXML](org-service/page-large-result-sets-with-fetchxml.md)<br />
[Fetch XML schema](fetchxml-schema.md)<br />
<xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*><br />
<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest><br />
<xref:Microsoft.Xrm.Sdk.Query.FetchExpression>

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
