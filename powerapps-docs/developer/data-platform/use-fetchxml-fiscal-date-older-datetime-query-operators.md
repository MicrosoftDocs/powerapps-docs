---
title: "Fiscal date and older than datetime query operators in FetchXML (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Find out how to use FetchXML fiscal data conditional operators and &quot;older than&quot; clauses for date and time values." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/25/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Fiscal date and older than datetime query operators in FetchXML

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

A FetchXML query in Microsoft Dataverse can use special fiscal date values and *older than* clauses for date and time values in queries. For example, a FetchXML query can find all orders fulfilled in the last fiscal month or urgent cases with high severity that are older than 15 minutes.  
  
> [!NOTE]
> For all fiscal date queries, the FetchXML query uses the organization’s fiscal year settings.  
  
<a name="FiscalDate"></a>

## Using FetchXML fiscal date conditional operators

 The following example shows a FetchXML expression that finds all orders fulfilled in the last fiscal period, according to the organization’s fiscal year settings. For example, if the organization uses fiscal months, the query returns orders fulfilled in the last fiscal month. If the organization uses fiscal quarters, the query returns orders fulfilled in the last fiscal quarter. If the organization uses fiscal semesters, orders fulfilled in the last fiscal semester are returned.  
  
```xml  
<fetch>  
 <entity name="order">  
  <attribute name="name"/>  
  <filter type="and">  
   <condition attribute="datefulfilled" operator="last-fiscal-period"/>  
  </filter>  
 </entity>  
</fetch>  
```  
  
 The following example shows a FetchXML expression that finds all accounts created in fiscal year 2013.  
  
```xml  
<fetch>  
 <entity name="account">  
  <attribute name="name"/>  
  <filter type="and">  
   <condition attribute="createdon" operator="in-fiscal-year" value="2013"/>  
  </filter>  
 </entity>  
</fetch>  
```  
  
 The following example shows a FetchXML expression that finds all opportunities with an estimated close date in the next three fiscal years, based on the organization’s fiscal year settings. The value for `x` is specified in the value column of the condition tag.  
  
```xml  
<fetch>  
 <entity name="opportunity">  
  <attribute name="name"/>  
  <filter type="and">  
   <condition attribute="estimatedclosedate" operator="next-x-fiscal-years" value="3"/>  
  </filter>  
 </entity>  
</fetch>  
```  
  
 The following example shows a FetchXML expression that finds all orders fulfilled in period three of any fiscal year, according to the organization’s fiscal year settings. The fiscal period value is specified in the value column of the condition tag. If the organization uses fiscal months, the query returns results from month three. If the organization uses fiscal quarters, the query returns results from quarter three. If the organization uses fiscal semesters, no results are returned; there are only two semesters, and the value supplied is therefore out-of-range.  
  
```xml  
<fetch>  
 <entity name="order">  
  <attribute name="name"/>  
  <filter type="and">  
   <condition attribute="datefulfilled" operator="in-fiscal-period" value="3"/>  
  </filter>  
 </entity>  
</fetch>  
```  
  
 The following example shows a FetchXML expression that finds all orders fulfilled in period three of fiscal year 2013, according to the organization’s fiscal year settings. If the organization uses fiscal months, the query returns results from month three. If the organization uses fiscal quarters, the query returns results from quarter three. If the organization uses fiscal semesters, no results are returned; there are only two semesters, and the value supplied is therefore out-of-range.  
  
```xml  
<fetch>  
 <entity name="order">  
  <attribute name="name"/>  
  <filter type="and">  
   <condition attribute="datefulfilled" operator="in-fiscal-period-and-year">  
    <value>3</value>  
    <value>2013</value>  
   </condition>  
  </filter>  
 </entity>  
</fetch>  
```  
  
 The following example shows a FetchXML aggregation expression that sums the total amount of orders fulfilled and groups the result by fiscal semester and fiscal year.  
  
```xml  
<fetch aggregate="true">  
 <entity name="order">  
  <attribute name="totalamount" aggregate="sum" alias="total"/>  
  <attribute name="datefulfilled" groupby="true" dategrouping="fiscal-period"/>  
 </entity>  
</fetch>  
```  
  
<a name="OlderThan"></a>   
## Using “older than” clauses for date and time values  
 The following example shows a FetchXML that finds incidents that are older than 30 minutes.  
  
```xml  
<fetch>  
  <entity name="incident">  
    <attribute name="title" />  
    <attribute name="ticketnumber" />  
    <attribute name="createdon" />  
    <attribute name="incidentid" />  
    <filter type="and">  
      <condition attribute="createdon" operator="olderthan-x-minutes" value="30" />  
    </filter>  
  </entity>  
</fetch>  
```  
  
 Use the following syntax to specify variious *older than* clauses in a FetchXML expression.  
  
 Older than X minutes  
 ```xml  
<condition attribute="<AttributeName>" operator="olderthan-x-minutes" value="<VALUE>" />  
```  
  
> [!NOTE]
> This clause is not supported for date and time columns with `DateOnly` behavior. More information: [Date and time query operators not supported for DateOnly behavior](/dynamics365/customer-engagement/developer/behavior-format-date-time-attribute#date-and-time-query-operators-not-supported-for-dateonly-behavior)
  
 Older than X hours  
 ```xml  
<condition attribute="<AttributeName>" operator="olderthan-x-hours" value="<VALUE>" />  
```  
  
> [!NOTE]
>  This clause is not supported for date and time columns with `DateOnly` behavior. More information: [Date and time query operators not supported for DateOnly behavior](/dynamics365/customer-engagement/developer/behavior-format-date-time-attribute#date-and-time-query-operators-not-supported-for-dateonly-behavior)  
  
 Older than X days  
 ```xml  
<condition attribute="<AttributeName>" operator="olderthan-x-days" value="<VALUE>" />  
```  
  
 Older than X weeks  
 ```xml  
<condition attribute="<AttributeName>" operator="olderthan-x-weeks" value="<VALUE>" />  
```  
  
 Older than X months  
 ```xml  
<condition attribute="<AttributeName>" operator="olderthan-x-months" value="<VALUE>" />  
```  
  
 Older than X years  
 ```xml  
<condition attribute="<AttributeName>" operator="olderthan-x-years" value="<VALUE>" />  
```

### See also  
 [Create Queries to Retrieve Data](/dynamics365/customer-engagement/developer/org-service/retrieve-data-queries-sdk-assemblies)   
 [Building Queries with FetchXML](/dynamics365/customer-engagement/developer/org-service/build-queries-fetchxml)   
 [Use a left outer join in FetchXML to query for records "not in"](/dynamics365/customer-engagement/developer/use-left-outer-join-fetchxml-query-records-not-in)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]