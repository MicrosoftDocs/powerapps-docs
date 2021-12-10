---
title: "Test for a null value (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to test for a null value by using the FilterExpression and QueryByAttribute classes"
ms.custom: ""
ms.date: 05/03/2019
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "KumarVivek" # GitHub ID
ms.author: "kvivek" # MSFT alias of Microsoft employees only
manager: "annbe" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Test for a null value

[!INCLUDE[cc-data-platform-banner](../../../includes/cc-data-platform-banner.md)]

The following code example shows how to test for a null value by using the <xref:Microsoft.Xrm.Sdk.Query.FilterExpression> and <xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute> classes.  
  
## FilterExpression example  
 Use this code to test for equality by using the <xref:Microsoft.Xrm.Sdk.Query.FilterExpression> class.  
  
```csharp  
FilterExpression null_filter = new FilterExpression(LogicalOperator.And);   
null_filter.FilterOperator = LogicalOperator.And;   
null_filter.AddCondition("leadid", ConditionOperator.Null);  
  
```  
  
## Another FilterExpression example  
 Use this code to test for inequality by using the <xref:Microsoft.Xrm.Sdk.Query.FilterExpression> class.  
  
```csharp  
  
FilterExpression filter = new FilterExpression(LogicalOperator.And);   
filter.FilterOperator = LogicalOperator.And;   
filter.AddCondition("leadid", ConditionOperator.NotNull);  
```  
  
## QueryByAttribute example  
 Use this code to test for equality by using the <xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute> class.  
  
```csharp  
  
QueryByAttribute qba = new QueryByAttribute("account");   
qba.ColumnSet = new ColumnSet("name","address1_stateorprovince");   
qba.AddAttributeValue("donotfax", null);  
```  
  
### See also  
 [Build Queries with QueryExpression](build-queries-with-queryexpression.md)   
 [Page large result sets with FetchXML](page-large-result-sets-with-fetchxml.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]