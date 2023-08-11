---
title: "Use the QueryExpression class (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use the QueryExpression class to build complex queries for use with the IOrganizationService.QueryBase method or the RetrieveMultipleRequest message." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/05/2023
author: divkamath
ms.author: dikamath
ms.reviewer: pehecke
ms.topic: "article"
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
---

# Use the QueryExpression class

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

In Microsoft Dataverse, you can use the <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> class to build complex queries for use with the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*> method or the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> message. You can set query parameters to the <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> by using the <xref:Microsoft.Xrm.Sdk.Query.ConditionExpression>, <xref:Microsoft.Xrm.Sdk.Query.ColumnSet>, and <xref:Microsoft.Xrm.Sdk.Query.FilterExpression> classes.  
  
 The <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> class lets you create complex queries. The <xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute> class is designed to be a simple way to search for table rows where columns match specified values.  
  
<a name="record_count"></a>   
## Record count  
 To find out how many records the query returned, set the <xref:Microsoft.Xrm.Sdk.Query.PagingInfo.ReturnTotalRecordCount> property to true before executing the query. When you do this, the <xref:Microsoft.Xrm.Sdk.EntityCollection.TotalRecordCount> will be set. Otherwise, this value will be -1.  
  
## Example  
 The following sample shows how to use the <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> class.  
  
```csharp  
//  Query using ConditionExpression and FilterExpression  
ConditionExpression condition1 = new ConditionExpression();  
condition1.AttributeName = "lastname";  
condition1.Operator = ConditionOperator.Equal;  
condition1.Values.Add("Brown");              
  
FilterExpression filter1 = new FilterExpression();  
filter1.Conditions.Add(condition1);  
  
QueryExpression query = new QueryExpression("contact");  
query.ColumnSet.AddColumns("firstname", "lastname");  
query.Criteria.AddFilter(filter1);  
  
EntityCollection result1 = _serviceProxy.RetrieveMultiple(query);  
Console.WriteLine();Console.WriteLine("Query using Query Expression with ConditionExpression and FilterExpression");  
Console.WriteLine("---------------------------------------");  
foreach (var a in result1.Entities)  
{  
    Console.WriteLine("Name: " + a.Attributes["firstname"] + " " + a.Attributes["lastname"]);  
}  
Console.WriteLine("---------------------------------------");  
```

## Use SQL hints in a query

The <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> class contains a property named <xref:Microsoft.Xrm.Sdk.Query.QueryExpression.QueryHints>. By setting this property to one of the supported string values shown below, you can provide a hint for generated SQL text which affects the query's execution.

|QueryHint value | SQL Query Option and Hint |
|---------|---------|
|OptimizeForUnknown | Optimize For Unknown|
|ForceOrder | Force Order |
|Recompile &nbsp;(see note)| Recompile |
|DisableRowGoal | use hint(‘Disable_Optimizer_RowGoal’) |
|EnableOptimizerHotfixes | use hint('ENABLE_QUERY_OPTIMIZER_HOTFIXES') |
|LoopJoin | Loop Join |
|MergeJoin | Merge Join |
|HashJoin | Hash Join |
|NO_PERFORMANCE_SPOOL | NO_PERFORMANCE_SPOOL |
|MaxRecursion | MAXRECURSION number |
|ENABLE_HIST_AMENDMENT_FOR_ASC_KEYS | ENABLE_HIST_AMENDMENT_FOR_ASC_KEYS |

> [!IMPORTANT]
> In general, the “Recompile” query hint should be avoided. This query hint will require extra computation and database resources for every execution of the query on the database. Please read Microsoft’s documentation on the “OPTION (RECOMPILE)” query hint, or work with Microsoft customer support, to find out more about the appropriate use cases of this query hint.

More information: [Hints (Transact-SQL) - Query](/sql/t-sql/queries/hints-transact-sql-query)

### See also

 [Building Queries with QueryExpression](build-queries-with-queryexpression.md)   
 [Use the ColumnSet Class](use-the-columnset-class.md)   
 [Using the ConditionExpression Class](use-conditionexpression-class.md)   
 [Using the FilterExpression Class](use-filterexpression-class.md)   
 <xref:Microsoft.Xrm.Sdk.Query.QueryExpression>

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
