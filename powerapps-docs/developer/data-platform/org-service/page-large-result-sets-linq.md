---
title: "Page large result sets with LINQ (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Read how you can page the results of a large .NET Language-Integrated Query (LINQ) query by using the Take and Skip operators." # 115-145 characters including spaces. This abstract displays in the search result.
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

# Page large result sets with LINQ

In Microsoft Dataverse, you can page the results of a large .NET Language-Integrated Query (LINQ) query by using the `Take` and `Skip` operators. The `Take` operator retrieves a specified number of results and the `Skip` operator skips over a specified number of results.  
  
## LINQ paging example  

The following example shows how to page the results of a LINQ query by using the `Take` and `Skip` operators:  
  
```csharp
int pageSize = 5;

var accountsByPage = (from a in svcContext.AccountSet
                      select new Account
                      {
                       Name = a.Name,
                      });
System.Console.WriteLine("Skip 10 accounts, then Take 5 accounts");
System.Console.WriteLine("======================================");
foreach (var a in accountsByPage.Skip(2 * pageSize).Take(pageSize))
{
 System.Console.WriteLine(a.Name);
}

```
  
### See also  
 [Build queries with LINQ (.NET Language-Integrated Query)](build-queries-with-linq-net-language-integrated-query.md)   
 [LINQ query examples](linq-query-examples.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]