---
title: "Use the ColumnSet class (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to use the ColumnSet class to specify columns returned in query results." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 06/02/2021
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

# Use the ColumnSet class

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

In Microsoft Dataverse, you can use the <xref:Microsoft.Xrm.Sdk.Query.ColumnSet> class to specify what columns (attributes) to return from a query defined using the <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> and <xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute> classes. It is also a parameter for the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*> method and it is used as a property in a number of message request classes which return data in an <xref:Microsoft.Xrm.Sdk.EntityCollection>.

> [!NOTE]
> The <xref:Microsoft.Xrm.Sdk.Query.ColumnSet> class has an <xref:Microsoft.Xrm.Sdk.Query.ColumnSet.AllColumns> property which specifies that all columns of the table should be returned. As a performance best practice, you should not use this for production code. More information: [Do not retrieve all table columns via query APIs](/dynamics365/customer-engagement/guidance/data/retrieve-specific-columns-entity-via-query-apis)

The following code example shows how to use the `ColumnSet` class to specify what columns to return from a query expression.  
  
```csharp  
QueryExpression contactquery = new QueryExpression   
{  
   EntityName="contact",  
   ColumnSet = new ColumnSet("firstname", "lastname", "contactid")   
};  
```  
  
### See also  

[Using the QueryExpression Class](use-queryexpression-class.md)<br />
[Building Queries with QueryExpression](build-queries-with-queryexpression.md)<br />
[Use the ConditionExpression Class](use-conditionexpression-class.md)<br /> 
<xref:Microsoft.Xrm.Sdk.Query.QueryExpression> class <br />
<xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute> class <br />


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]