---
title: "Order results using table columns with LINQ (Microsoft Dataverse) | Microsoft Docs" 
description: "Read how you can use lookup or choices (picklist) columns to order results within a LINQ query."
ms.date: 04/03/2022
author: kkanakas
ms.author: kartikka
manager: pemikkel
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

# Order results using table columns with LINQ

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

In Microsoft Dataverse you can use lookup or choices (picklist) columns to order results within a LINQ query. This topic shows several examples of this type of query.  
  
## Using a lookup value to Order By  

The following sample shows use the lookup column `PrimaryContactId` in an `Order By` clause.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
 var query_orderbylookup = from a in svcContext.AccountSet
                           where a.Address1_Name == "Contoso Pharmaceuticals"
                           orderby a.PrimaryContactId
                           select new
                           {
                            a.Name,
                            a.Address1_City
                           };
 foreach (var a in query_orderbylookup)
 {
  System.Console.WriteLine(a.Name + " " + a.Address1_City);
 }
}

```
  
## Using choices to Order By  

The following sample shows use of a choices (picklist) value to order by.  
  
```csharp

using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
 var query_orderbypicklist = from c in svcContext.ContactSet
                             where c.LastName != "Parker" &&
                             c.AccountRoleCode != null
                             orderby c.AccountRoleCode, c.FirstName
                             select new
                             {
                              AccountRole = c.FormattedValues["accountrolecode"],
                              c.FirstName,
                              c.LastName
                             };
 foreach (var c in query_orderbypicklist)
 {
  System.Console.WriteLine(c.AccountRole + " " +
   c.FirstName + " " + c.LastName);
 }
}
```
  
### See also

 [Build queries with LINQ (.NET Language-Integrated Query)](build-queries-with-linq-net-language-integrated-query.md)   
 [Page large result sets with LINQ](page-large-result-sets-linq.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]