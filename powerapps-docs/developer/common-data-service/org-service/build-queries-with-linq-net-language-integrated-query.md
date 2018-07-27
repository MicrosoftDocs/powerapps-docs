---
title: "Build queries with LINQ (.NET language-integrated query) (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Read how to use .NET Language-Integrated Query (LINQ) to write queries in Common Data Service for Apps" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 07/24/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Build queries with LINQ (.NET language-integrated query)

You can use .NET Language-Integrated Query (LINQ) to write queries in Common Data Service for Apps. You can use the <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext> class or a deriving class created by the CrmSvcUtil tool to write [LINQ](https://msdn.microsoft.com/library/bb397897.aspx) queries that access the SOAP endpoint (Organization.svc). The <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext> class contains an underlying LINQ query provider that translates LINQ queries from Visual C# or Visual Basic .NET syntax into the query API used by CDS for Apps.  
  
 When you use early-bound programming classes you can generate a class derived from the <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext> class if you specify the name of the class using the **servicecontextname** parameter when using the Code Generation Tool (CrmSvcUtil.exe). Use of this class allows for referencing an [IQueryable](https://msdn.microsoft.com/library/system.linq.iqueryable.aspx) entity set using the pattern `<entity schema name>+Set`, for example **AccountSet** to reference the collection of `Account` entity records. All samples in the CDS for Apps Web Services, use **ServiceContext** as the name for this class but your code may use a different name. More information: [Create Early Bound Entity Classes with the Code Generation Tool (CrmSvcUtil.exe)](create-early-bound-entity-classes-code-generation-tool.md) 
  
## In This Section  
 [Use LINQ to Construct a Query](use-linq-construct-query.md)  
  
 [Use Late-Bound Entity Class with a LINQ Query](use-late-bound-entity-class-linq-query.md)  
  
 [Use Entity Lookup Attributes with LINQ](order-results-entity-attributes-linq.md)  
  
 [Order Results Using Entity Attributes with LINQ](order-results-entity-attributes-linq.md)  
  
 [Paging Large Result Sets with LINQ](page-large-result-sets-linq.md)  
  
 [LINQ Query Examples](linq-query-examples.md)  
  
 [Sample: Create a LINQ Query](sample-create-linq-query.md)  
  
 [Sample: LINQ Query Examples](sample-complex-linq-queries.md)  
  
 [Sample: RetrieveMultiple With Condition Operators Using LINQ](sample-retrieve-multiple-with-condition-operators-using-linq.md)  
  
 [Sample: More LINQ Query Examples](dynamics365/customer-engagement/developer/sample-more-linq-query-examples.md)  
  
 [Sample: Use LINQ with Late Binding](sample-create-linq-query-late-binding.md)