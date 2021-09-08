---
title: "Use a left outer join in FetchXML to query for records 	&bdquo;not in&bdquo; (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Read how to use a left outer join in FetchXML to perform a query that filters on the join table and build a query to find records “not in” a set." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/25/2021
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

# Use a left outer join in FetchXML to query for records "not in"

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

You can use a left outer join in FetchXML to perform a query that filters on the join table, such as to find all contacts who did not have any campaign activities in the past two months. Another common use for this type of a query is to find records “not in” a set, such as in these cases:  
  
- Find all leads that have no tasks  
  
- Find all accounts that have no contacts  
  
- Find all leads that have one or more tasks  
  
  A left outer join returns each row that satisfies the join of the first input with the second input. It also returns any rows from the first input that had no matching rows in the second input. The non-matching rows in the second input are returned as null values.  
  
  You can perform a left outer join in FetchXML by using the `entityname` column as a condition operator. The `entityname` column is valid in conditions, filters, and nested filters.  
  
  You can create a query using a left outer join programmatically and execute the query using the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest>, and you can save the query by creating a `SavedQuery` record. You can open a saved query that contains a left outer join in the Advanced Find or Saved Query editors in the web application and execute and view results, but some editor functionality is disabled. Those editors will allow modifications to the query, such as to change the columns returned, but the editor does not support changing the left outer join.  
  
## Example: Find all accounts that have no leads

 The following shows how to construct the query in FetchXML:  
  
```xml  
<fetch mapping='logical'>  
 <entity name='account'>  
  <attribute name='name'/>  
  <link-entity name='lead'  
               from='leadid'  
               to='originatingleadid'  
               link-type='outer'/>  
  <filter type='and'>  
   <condition entityname='lead'  
              attribute='leadid'  
              operator='null'/>  
  </filter>  
 </entity>  
</fetch>  
  
```  
  
## Example: Find all leads that have no tasks, using an alias

 The following shows how to construct the query in FetchXML:  
  
```xml  
<fetch version="1.0" output-format="xml-platform" mapping="logical" distinct="true">  
  <entity name="lead">  
    <attribute name="fullname" />  
    <link-entity name="task" from="regardingobjectid" to="leadid" alias="ab" link-type="outer">  
       <attribute name="regardingobjectid" />  
    </link-entity>  
    <filter type="and">  
        <condition entityname="ab" attribute="regardingobjectid" operator="null" />  
    </filter>  
  </entity>  
<fetch/>  
  
```  
  
 This is equivalent to the following SQL:  
  
```sql  
SELECT lead.FullName  
FROM Leads as lead  
LEFT OUTER JOIN Tasks as ab  
ON (lead.leadId  =  ab.RegardingObjectId)  
WHERE ab.RegardingObjectId is null  
  
```  
  
### See also

 [Build queries with FetchXML](/dynamics365/customer-engagement/developer/org-service/build-queries-fetchxml)   
 [Sample: Use aggregation in FetchXML](org-service/samples/use-aggregation-fetchxml.md)   
 [Use FetchXML to construct a query](use-fetchxml-construct-query.md)   
 [Sample: Validate and execute a saved query](org-service/samples/validate-execute-saved-query.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]