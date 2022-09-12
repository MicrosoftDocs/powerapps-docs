---
title: "Use a left outer join in QueryExpression to query for rows &quot;not in&quot; (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Read how to use a left outer join by using the QueryExpression class to perform a query that filters on the join table and build a query to find table rows &quot;not in&quot; a set." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: divka78
ms.author: dikamath
ms.reviewer: pehecke
ms.topic: "article"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
 - phecke
---

# Use a left outer join in QueryExpression to query for rows "not in"

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

You can use a left outer join by using the <xref:Microsoft.Crm.Sdk.Messages.SearchByKeywordsKbArticleRequest.QueryExpression> class to perform a query that filters on the join table, such as to find all contacts who did not have any campaign activities in the past two months. Another common use for this type of a query is to find table rows (records) “not in” a set, such as in these cases:  
  
- Find all leads that have no tasks  
- Find all accounts that have no contacts  
- Find all leads that have one or more tasks  
  
A left outer join returns each row that satisfies the join of the first input with the second input. It also returns any rows from the first input that had no matching rows in the second input. The nonmatching rows in the second input are returned as null values.  
  
You can perform a left outer join in `QueryExpression` by using the `entityname` column as a condition operator. The `entityname` column is valid in conditions, filters, and nested filters.  
  
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

[Build Queries with QueryExpression](build-queries-with-queryexpression.md)<br />
[Using the QueryExpression Class](use-queryexpression-class.md)<br />
[Using the QueryByAttribute Class](use-querybyattribute-class.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]