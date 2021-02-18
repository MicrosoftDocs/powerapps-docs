---
title: "Build queries with LINQ (.NET language-integrated query) (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Read how to use .NET Language-Integrated Query (LINQ) to write queries in Microsoft Dataverse" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
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
# Build queries with LINQ (.NET language-integrated query)

[!INCLUDE[cc-data-platform-banner](../../../includes/cc-data-platform-banner.md)]

You can use .NET Language-Integrated Query (LINQ) to write queries in Microsoft Dataverse. You can use the <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext> class or a deriving class created by the CrmSvcUtil tool to write [LINQ](https://msdn.microsoft.com/library/bb397897.aspx) queries that access the SOAP endpoint (Organization.svc). The <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext> class contains an underlying LINQ query provider that translates LINQ queries from Visual C# or Visual Basic .NET syntax into the query API used by Dataverse.  
  
 When you use early-bound programming classes you can generate a class derived from the <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext> class if you specify the name of the class using the **servicecontextname** parameter when using the Code Generation Tool (CrmSvcUtil.exe). Use of this class allows for referencing an [IQueryable](https://msdn.microsoft.com/library/system.linq.iqueryable.aspx) entity set using the pattern `<entity schema name>+Set`, for example **AccountSet** to reference the collection of `Account` entity records. All samples in the Dataverse Web Services, use **ServiceContext** as the name for this class but your code may use a different name. More information: [Generate early-bound classes for the Organization service)](generate-early-bound-classes.md).
  
### See Also

 [Use LINQ to Construct a Query](use-linq-construct-query.md)  
  
 [Use Late-Bound Entity Class with a LINQ Query](use-late-bound-entity-class-linq-query.md)  
  
 [Use Entity Lookup Attributes with LINQ](order-results-entity-attributes-linq.md)  

 [LINQ query examples](linq-query-examples.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]