---
title: "Use late-bound Entity class with a LINQ query (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Read how you can use late binding with .NET Language-Integrated Query (LINQ) queries." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 06/08/2021
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

# Use late-bound Entity class with a LINQ query

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

In Microsoft Dataverse, you can use late binding with .NET Language-Integrated Query (LINQ) queries. Late binding uses the attribute logical name, and is resolved at runtime.  
  
<a name="usinglatebindingjoin"></a>   

## Using late binding in a JOIN clause  

 The following examples show how to use late binding in the `join` clause of a LINQ query.  
  
 Retrieve the full name of the contact that represents the primary contact for an account and the account name.  
  
 ```csharp
 using (OrganizationServiceContext orgSvcContext = new OrganizationServiceContext(_serviceProxy))
{
 var query_join2 = from c in orgSvcContext.CreateQuery("contact")
                   join a in orgSvcContext.CreateQuery("account")
                   on c["contactid"] equals a["primarycontactid"]
                   select new
                   {
                    contact_name = c["fullname"],
                    account_name = a["name"]
                   };
 foreach (var c in query_join2)
 {
  System.Console.WriteLine(c.contact_name + "  " + c.account_name);
 }
}
 ```

 Retrieve Contact, Account and Lead data where the Lead was the originating Lead and the Contact’s last name is not “Parker”  
  
 ```csharp
 using (OrganizationServiceContext orgSvcContext = new OrganizationServiceContext(_serviceProxy))
{
 var query_dejoin = from c in orgSvcContext.CreateQuery("contact")
                    join a in orgSvcContext.CreateQuery("account") 
                    on c["contactid"] equals a["primarycontactid"]
                    join l in orgSvcContext.CreateQuery("lead") 
                    on a["originatingleadid"] equals l["leadid"]
                    where (string)c["lastname"] != "Parker"
                    select new { Contact = c, Account = a, Lead = l };
 foreach (var c in query_dejoin)
 {
  System.Console.WriteLine(c.Account.Attributes["name"] + " " + 
   c.Contact.Attributes["fullname"] + " " + c.Lead.Attributes["leadid"]);
 }
}
 ```

<a name="Usinglatebindingleft"></a>

## Using late binding in a left JOIN  

 The following example shows how to retrieve a list of Contact and Account information using a left join. A left join is designed to return parents with and without children from two sources. There is a correlation between parent and child, but no child may actually exist.  
  
 ```csharp
 using (OrganizationServiceContext orgSvcContext = new OrganizationServiceContext(_serviceProxy))
{
 var query_join9 = from a in orgSvcContext.CreateQuery("account")
                   join c in orgSvcContext.CreateQuery("contact") 
                   on a["primarycontactid"] equals c["contactid"] into gr
                   from c_joined in gr.DefaultIfEmpty()
                   select new
                   {
                    account_name = a.Attributes["name"]
                   };
 foreach (var c in query_join9)
 {
  System.Console.WriteLine(c.account_name);
 }
}
 ```

<a name="contains"></a>

## Using late binding and the Contains method  

 The following example shows how to use late binding with the `Contains` method in a LINQ query.  
  
 ```csharp
 using (OrganizationServiceContext orgSvcContext = new OrganizationServiceContext(_serviceProxy))
{
 var query_contains3 = from c in orgSvcContext.CreateQuery("contact")
                       where ((string)c["description"]).Contains("Coho")
                       select new
                       {
                        firstname = c.Attributes["firstname"],
                        lastname = c.Attributes["lastname"]
                       };
 foreach (var c in query_contains3)
 {
  System.Console.WriteLine(c.firstname + " " + c.lastname);
 }
}
 ```

 <a name="notequals"></a>

## Using late binding and NOT Equals operator  

 The following example shows use of the not equals operator.  
  
 ```csharp
using (OrganizationServiceContext orgSvcContext = new OrganizationServiceContext(_serviceProxy))
{
 var query_ne3 = from c in orgSvcContext.CreateQuery("contact")
                 where !c["address1_city"].Equals(null)
                 select new
                 {
                  FirstName = c["firstname"],
                  LastName = c["lastname"],
                  Address1_City = c["address1_city"]
                 };
 foreach (var c in query_ne3)
 {
  System.Console.WriteLine(c.FirstName + " " + 
   c.LastName + " " + c.Address1_City);
 }
}
```

 <a name="getattribute"></a>

## Using the GetAttributeValue method  

 The following example shows how to retrieve Contact information using the `GetAttributeValue` method.  
  
 ```csharp
using (OrganizationServiceContext orgSvcContext = new OrganizationServiceContext(_serviceProxy))
{

 var list_getattrib1 = (from c in orgSvcContext.CreateQuery("contact")
                        where c.GetAttributeValue<Guid?>("contactid") != _contactId1
                        select new { 
                         FirstName = c.GetAttributeValue<string>("firstname"), 
                         LastName = c.GetAttributeValue<string>("lastname") 
                        }).ToList();
 foreach (var c in list_getattrib1)
 {
  System.Console.WriteLine(c.FirstName + " " + c.LastName);
 }
}
```
  
### See also

 [Build Queries with LINQ (.NET Language-Integrated Query)](build-queries-with-linq-net-language-integrated-query.md)   
 [Order results using table columns with LINQ](order-results-entity-attributes-linq.md)   
<xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext.CreateQuery%60%601>

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]