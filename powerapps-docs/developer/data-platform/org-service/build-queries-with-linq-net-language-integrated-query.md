---
title: "Build queries with LINQ (.NET language-integrated query) (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to use .NET Language-Integrated Query (LINQ) to write queries for Microsoft Dataverse." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: pehecke
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
---

# Build queries with LINQ (.NET language-integrated query)

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

You can use .NET Language-Integrated Query (LINQ) to write queries for Microsoft Dataverse. You can use the <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext> class or a deriving class created by the [Power Platform CLI pac modelbuilder build command](/power-platform/developer/cli/reference/modelbuilder#pac-modelbuilder-build) to write [LINQ](/dotnet/csharp/programming-guide/concepts/linq/introduction-to-linq-queries) queries using the Organization service. The <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext> class contains an underlying LINQ query provider that translates LINQ queries from Visual C# or Visual Basic .NET syntax into the query API used by Dataverse.  
  
 When you use early-bound programming classes you can generate a class derived from the <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext> class if you specify the name of the class using the **serviceContextName** parameter when using the [Power Platform CLI pac modelbuilder build command](/power-platform/developer/cli/reference/modelbuilder#pac-modelbuilder-build). Use of this class allows for referencing an [IQueryable](/dotnet/api/system.linq.iqueryable) table set using the pattern `<table schema name>+Set`, for example **AccountSet** to reference the collection of `Account` table rows. All samples in the Dataverse Web Services, use **ServiceContext** as the name for this class but your code may use a different name. More information: [Generate early-bound classes for the Organization service)](generate-early-bound-classes.md).
  
### See Also

 [Use LINQ to construct a query](use-linq-construct-query.md)  
 [Use late-bound Entity class with a LINQ Query](use-late-bound-entity-class-linq-query.md)  
 [Use table lookup columns with LINQ](order-results-entity-attributes-linq.md)  
 [LINQ query examples](linq-query-examples.md)  
 [Generate early-bound classes for the Organization service](generate-early-bound-classes.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
