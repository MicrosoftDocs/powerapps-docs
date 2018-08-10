---
title: "Use a left outer join in QueryExpression to query for records &quot;not in&quot; (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Read how to use a left outer join by using the QueryExpression class to perform a query that filters on the join table and build a query to find records &quot;not in&quot; a set" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Use a left outer join in QueryExpression to query for records "not in"

You can use a left outer join by using the <xref:Microsoft.Crm.Sdk.Messages.SearchByKeywordsKbArticleRequest.QueryExpression> class to perform a query that filters on the join table, such as to find all contacts who did not have any campaign activities in the past two months. Another common use for this type of a query is to find records “not in” a set, such as in these cases:  
  
- Find all leads that have no tasks  
  
- Find all accounts that have no contacts  
  
- Find all leads that have one or more tasks  
  
  A left outer join returns each row that satisfies the join of the first input with the second input. It also returns any rows from the first input that had no matching rows in the second input. The nonmatching rows in the second input are returned as null values.  
  
  You can perform a left outer join in `QueryExpression` by using the `entityname` attribute as a condition operator. The `entityname` attribute is valid in conditions, filters, and nested filters.  
  
## Find all leads that have no tasks, using an alias  

The following example shows how to construct this query:  
  
```csharp
QueryExpression qx = new QueryExpression("lead");  
qx.ColumnSet.AddColumn("subject");  
  
LinkEntity link = qx.AddLink("task", "leadid", "regardingobjectid", JoinOperator.LeftOuter);  
link.Columns.AddColumn("subject");  
link.EntityAlias = "tsk";  
  
qx.Criteria = new FilterExpression();  
qx.Criteria.AddCondition("tsk", "activityid", ConditionOperator.Null);
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
 [Build Queries with QueryExpression](build-queries-with-queryexpression.md)   
 [Test for a Null Value](test-null-value.md)   
 [Using the QueryExpression Class](use-queryexpression-class.md)   
 [Using the QueryByAttribute Class](use-querybyattribute-class.md)