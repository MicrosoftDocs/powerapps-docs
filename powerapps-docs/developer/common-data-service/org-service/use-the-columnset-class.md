---
title: "Use the ColumnSet class (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Use the ColumnSet class

In Common Data Service for Apps, you can use the <xref:Microsoft.Xrm.Sdk.Query.ColumnSet> class to specify what attributes to return from a query defined using the <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> and <xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute> classes. It is also a parameter for the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*> method and it is used as a property in a number of message request classes which return data in an <xref:Microsoft.Xrm.Sdk.EntityCollection>.

> [!NOTE]
> The <xref:Microsoft.Xrm.Sdk.Query.ColumnSet> class has an <xref:Microsoft.Xrm.Sdk.Query.ColumnSet.AllColumns> property which specifies that all columns of the entity should be returned. As a performance best practice, you should not use this for production code. More information: [Do not retrieve Entity all columns via query APIs](/dynamics365/customer-engagement/guidance/data/retrieve-specific-columns-entity-via-query-apis)

The following code example shows how to use the `ColumnSet` class to specify what attributes to return from a query expression.  
  
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