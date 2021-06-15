---
title: "Linq query examples (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Browse code samples of LINQ queries." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 06/09/2021
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

# LINQ query examples using OrganizationServiceContext with Microsoft Dataverse

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

This topic contains many code samples of LINQ queries.  
  
<a name="SimpleWhereClause"></a>   
## Simple Where clause  
 The following sample shows how to retrieve a list of accounts where the Name contains “Contoso”.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_where1 = from a in svcContext.AccountSet
        where a.Name.Contains("Contoso")
        select a;
    foreach (var a in query_where1)
    {
        System.Console.WriteLine(a.Name + " " + a.Address1_City);
    }
}
```  
  
 The following sample shows how to retrieve a list of accounts where the Name contains “Contoso” and Address1_City is “Redmond”.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_where2 = from a in svcContext.AccountSet
                    where a.Name.Contains("Contoso")
                    where a.Address1_City == "Redmond"
                    select a;

    foreach (var a in query_where2)
    {
        System.Console.WriteLine(a.Name + " " + a.Address1_City);
    }
}
``` 
  
<a name="JoinandSimpleWhereClause"></a>   
## Join and simple Where clause  
 The following sample shows how to retrieve the account Name and the contact LastName where the account Name contains “Contoso” and the contact LastName contains “Smith” and the contact is the Primary Contact for the account.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_where3 = from c in svcContext.ContactSet
                    join a in svcContext.AccountSet
                    on c.ContactId equals a.PrimaryContactId.Id
                    where a.Name.Contains("Contoso")
                    where c.LastName.Contains("Smith")
                    select new
                    {
                     account_name = a.Name,
                     contact_name = c.LastName
                    };

    foreach (var c in query_where3)
    {
        System.Console.WriteLine("acct: " +
        c.account_name +
        "\t\t\t" +
        "contact: " +
        c.contact_name);
    }
}
```  
  
<a name="UsingtheDistinctOperator"></a>   
## Use the Distinct Operator  
 The following sample shows how to retrieve a distinct list of contact last names. Although there may be duplicates, each name will be listed only once.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_distinct = (from c in svcContext.ContactSet
                       select c.LastName).Distinct();
    foreach (var c in query_distinct)
    {
        System.Console.WriteLine(c);
    }
}
```
  
<a name="SimpleInnerJoin"></a>   
## Simple inner join  
The following sample shows how to retrieve information about an account and the contact listed as the primary contact for the account.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_join1 = from c in svcContext.ContactSet
                   join a in svcContext.AccountSet
                  on c.ContactId equals a.PrimaryContactId.Id
                   select new
                   {
                    c.FullName,
                    c.Address1_City,
                    a.Name,
                    a.Address1_Name
                   };
    foreach (var c in query_join1)
    {
        System.Console.WriteLine("acct: " +
        c.Name +
        "\t\t\t" +
        "contact: " +
        c.FullName);
    }
}
```  
  
<a name="SelfJoin"></a>   
## Self-join  
 The following sample shows how to retrieve information about accounts where an account is the parent account for an account.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_join5 = from a in svcContext.AccountSet
                   join a2 in svcContext.AccountSet
                   on a.ParentAccountId.Id equals a2.AccountId

                   select new
                   {
                    account_name = a.Name,
                    account_city = a.Address1_City
                   };
    foreach (var c in query_join5)
    {
        System.Console.WriteLine(c.account_name + "  " + c.account_city);
    }
}
```
  
<a name="DoubleJoin"></a>   
## Double and multiple joins  
 The following sample shows how to retrieve information from account, contact and lead where the contact is the primary contact for the account and the lead was the originating lead for the account.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_join4 = from a in svcContext.AccountSet
                   join c in svcContext.ContactSet
                   on a.PrimaryContactId.Id equals c.ContactId
                   join l in svcContext.LeadSet
                   on a.OriginatingLeadId.Id equals l.LeadId
                   select new
                   {
                    contact_name = c.FullName,
                    account_name = a.Name,
                    lead_name = l.FullName
                   };
    foreach (var c in query_join4)
    {
        System.Console.WriteLine(c.contact_name +
        "  " +
        c.account_name +
        "  " +
        c.lead_name);
    }
}
```  
  
 The following sample shows how to retrieve account and contact information where an account is the parent account for an account and the contact is the primary contact for the account.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_join6 = from c in svcContext.ContactSet
                   join a in svcContext.AccountSet
                   on c.ContactId equals a.PrimaryContactId.Id
                   join a2 in svcContext.AccountSet
                   on a.ParentAccountId.Id equals a2.AccountId
                   select new
                   {
                    contact_name = c.FullName,
                    account_name = a.Name
                   };
    foreach (var c in query_join6)
    {
        System.Console.WriteLine(c.contact_name + "  " + c.account_name);
    }
}
```
  
<a name="JoinUsingEntityFields"></a>

## Join using table column fields

 The following sample shows how to retrieve information about accounts from a list  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var list_join = (from a in svcContext.AccountSet
                  join c in svcContext.ContactSet
                  on a.PrimaryContactId.Id equals c.ContactId
                  where a.Name == "Contoso Ltd" &&
                  a.Address1_Name == "Contoso Pharmaceuticals"
                  select a).ToList();
    foreach (var c in list_join)
    {
        System.Console.WriteLine("Account " + list_join[0].Name
        + " and it's primary contact "
        + list_join[0].PrimaryContactId.Id);
    }
}
```  
  
<a name="LeftJoin"></a>   
## Late-binding left join  
 The following sample shows a left join. A left join is designed to return parents with and without children from two sources. There is a correlation between parent and child, but no child may actually exist.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_join8 = from a in svcContext.AccountSet
                   join c in svcContext.ContactSet
                   on a.PrimaryContactId.Id equals c.ContactId
                   into gr
                   from c_joined in gr.DefaultIfEmpty()
                   select new
                   {
                    contact_name = c_joined.FullName,
                    account_name = a.Name
                   };
    foreach (var c in query_join8)
    {
        System.Console.WriteLine(c.contact_name + "  " + c.account_name);
    }
}
``` 
  
<a name="UsingtheEqualsOperator"></a>   
## Use the Equals operator  
 The following sample shows how to retrieve a list of contacts where the FirstName is “Colin”.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_equals1 = from c in svcContext.ContactSet
                     where c.FirstName.Equals("Colin")
                     select new
                     {
                      c.FirstName,
                      c.LastName,
                      c.Address1_City
                     };
    foreach (var c in query_equals1)
    {
        System.Console.WriteLine(c.FirstName +
        " " + c.LastName +
        " " + c.Address1_City);
    }
}
``` 
  
 The following sample shows how to retrieve a list of contacts where the FamilyStatusCode is 3. This corresponds to the **Marital Status** choice of **Divorced**.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_equals2 = from c in svcContext.ContactSet
                     where c.FamilyStatusCode.Equals(3)
                     select new
                     {
                      c.FirstName,
                      c.LastName,
                      c.Address1_City
                     };
    foreach (var c in query_equals2)
    {
        System.Console.WriteLine(c.FirstName +
        " " + c.LastName +
        " " + c.Address1_City);
    }
}
``` 
  
<a name="UsingtheNotEqualsOperator"></a>   
## Use the Not Equals operator  
 The following sample shows how to retrieve a list of contacts where the Address1_City is not “Redmond”.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_ne1 = from c in svcContext.ContactSet
                 where c.Address1_City != "Redmond"
                 select new
                 {
                  c.FirstName,
                  c.LastName,
                  c.Address1_City
                 };
    foreach (var c in query_ne1)
    {
        System.Console.WriteLine(c.FirstName + " " +
        c.LastName + " " + c.Address1_City);
    }
}
```  
  
 The following sample shows how to retrieve a list of contacts where the FirstName is not “Colin”.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_ne2 = from c in svcContext.ContactSet
                 where !c.FirstName.Equals("Colin")
                 select new
                 {
                  c.FirstName,
                  c.LastName,
                  c.Address1_City
                 };

    foreach (var c in query_ne2)
    {
        System.Console.WriteLine(c.FirstName + " " +
        c.LastName + " " + c.Address1_City);
    }
}
```  
  
<a name="BKMK_UsingMethodBasedLINQQueryWithWhereClause"></a>   
## Use a method-based LINQ query with a Where clause  
 The following sample shows how to retrieve a list of contacts where the LastName is “Smith” or contains “Smi”.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var methodResults = svcContext.ContactSet
    .Where(a => a.LastName == "Smith");
    var methodResults2 = svcContext.ContactSet
    .Where(a => a.LastName.StartsWith("Smi"));
    Console.WriteLine();
    Console.WriteLine("Method query using Lambda expression");
    Console.WriteLine("---------------------------------------");
    foreach (var a in methodResults)
    {
        Console.WriteLine("Name: " + a.FirstName + " " + a.LastName);
    }
    Console.WriteLine("---------------------------------------");
    Console.WriteLine("Method query 2 using Lambda expression");
    Console.WriteLine("---------------------------------------");
    foreach (var a in methodResults2)
    {
        Console.WriteLine("Name: " + a.Attributes["firstname"] +
        " " + a.Attributes["lastname"]);
    }
}
``` 
  
<a name="BKMK_UsingGreaterThanOperator"></a>   
## Use the Greater Than operator  
 The following sample shows how to retrieve a list of contacts with an Anniversary date later than February 5, 2010.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_gt1 = from c in svcContext.ContactSet
                 where c.Anniversary > new DateTime(2010, 2, 5)
                 select new
                 {
                  c.FirstName,
                  c.LastName,
                  c.Address1_City
                 };

    foreach (var c in query_gt1)
    {
        System.Console.WriteLine(c.FirstName + " " +
        c.LastName + " " + c.Address1_City);
    }
}
``` 
  
 The following sample shows how to retrieve contacts with a CreditLimit greater than $20,000.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_gt2 = from c in svcContext.ContactSet
                 where c.CreditLimit.Value > 20000
                 select new
                 {
                  c.FirstName,
                  c.LastName,
                  c.Address1_City
                 };
    foreach (var c in query_gt2)
    {
        System.Console.WriteLine(c.FirstName + " " +
        c.LastName + " " + c.Address1_City);
    }
}
``` 
  
<a name="BKMK_UsingGreaterThanOrEqualsAndLessThanOrEqualsOperators"></a>   
## Use the Greater Than or Equals and Less Than or Equals operators  
 The following sample shows how to retrieve contacts with a CreditLimit greater than $200 and less than $400.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
 var query_gele1 = from c in svcContext.ContactSet
                   where c.CreditLimit.Value >= 200 &&
                   c.CreditLimit.Value <= 400
                   select new
                   {
                    c.FirstName,
                    c.LastName
                   };
 foreach (var c in query_gele1)
 {
  System.Console.WriteLine(c.FirstName + " " + c.LastName);
 }
}
``` 
  
<a name="BKMK_UsingContainsOperator"></a>   
## Use the Contains operator  
 The following sample shows how to retrieve contacts where the Description contains “Alpine”.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_contains1 = from c in svcContext.ContactSet
                       where c.Description.Contains("Alpine")
                       select new
                       {
                        c.FirstName,
                        c.LastName
                       };
    foreach (var c in query_contains1)
    {
        System.Console.WriteLine(c.FirstName + " " + c.LastName);
    }
}
```
  
<a name="BKMK_UsingDoesNotContainOperator"></a>   
## Use the Does Not Contain operator  
 The following sample shows how to retrieve contacts where the Description does not contain “Coho”.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_contains2 = from c in svcContext.ContactSet
                       where !c.Description.Contains("Coho")
                       select new
                       {
                        c.FirstName,
                        c.LastName
                       };
    foreach (var c in query_contains2)
    {
        System.Console.WriteLine(c.FirstName + " " + c.LastName);
    }
}
```  
  
<a name="BKMK_UsingEndsWithOperator"></a>   
## Use the StartsWith and EndsWith operators  
 The following sample shows how to retrieve contacts where FirstName starts with “Bri”.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_startswith1 = from c in svcContext.ContactSet
                         where c.FirstName.StartsWith("Bri")
                         select new
                         {
                          c.FirstName,
                          c.LastName
                         };
    foreach (var c in query_startswith1)
    {
        System.Console.WriteLine(c.FirstName + " " + c.LastName);
    }
}
```  

  
 The following sample shows how to retrieve contacts where LastName ends with “cox”.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_endswith1 = from c in svcContext.ContactSet
                       where c.LastName.EndsWith("cox")
                       select new
                       {
                        c.FirstName,
                        c.LastName
                       };
    foreach (var c in query_endswith1)
    {
        System.Console.WriteLine(c.FirstName + " " + c.LastName);
    }
}
```  

  
<a name="BKMK_UsingAndOrOperators"></a>   
## Use the And and Or operators  
 The following sample shows how to retrieve contacts where Address1_City is “Redmond” or “Bellevue” and a CreditLimit that is greater than $200.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_andor1 = from c in svcContext.ContactSet
                    where ((c.Address1_City == "Redmond" ||
                    c.Address1_City == "Bellevue") &&
                    (c.CreditLimit.Value != null &&
                    c.CreditLimit.Value >= 200))
                    select c;

    foreach (var c in query_andor1)
    {
        System.Console.WriteLine(c.LastName + ", " + c.FirstName + " " +
        c.Address1_City + " " + c.CreditLimit.Value);
    }
}
```  

  
<a name="BKMKUsingOrderByOperator"></a>   
## Use the OrderBy operator  
 The following sample shows how to retrieve contacts ordered by CreditLimit in descending order.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_orderby1 = from c in svcContext.ContactSet
                      where !c.CreditLimit.Equals(null)
                      orderby c.CreditLimit descending
                      select new
                      {
                       limit = c.CreditLimit,
                       first = c.FirstName,
                       last = c.LastName
                      };
    foreach (var c in query_orderby1)
    {
        System.Console.WriteLine(c.limit.Value + " " +
        c.last + ", " + c.first);
    }
}
```   

  
 The following sample shows how to retrieve contacts ordered by LastName in descending order and FirstName in ascending order.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_orderby2 = from c in svcContext.ContactSet
                      orderby c.LastName descending,
                      c.FirstName ascending
                      select new
                      {
                       first = c.FirstName,
                       last = c.LastName
                      };

    foreach (var c in query_orderby2)
    {
        System.Console.WriteLine(c.last + ", " + c.first);
    }
}
```  

  
<a name="BKMK_UsingFirstAndSingleOperators"></a>

## Use the First and Single operators

 The following sample shows how to retrieve only the first contact row returned and retrieve only one contact row that matches the criterion.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    Contact firstcontact = svcContext.ContactSet.First();

    Contact singlecontact = svcContext.ContactSet.Single(c => c.ContactId == _contactId1);
    System.Console.WriteLine(firstcontact.LastName + ", " +
    firstcontact.FirstName + " is the first contact");
    System.Console.WriteLine("==========================");
    System.Console.WriteLine(singlecontact.LastName + ", " +
    singlecontact.FirstName + " is the single contact");
}
```  

  
<a name="BKMK_RetrievingFormattedValues"></a>

## Retrieving formatted values

 The following sample shows how to retrieve the label for a choices option, in this case the value for the current row.
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var list_retrieve1 = from c in svcContext.ContactSet
                      where c.ContactId == _contactId1
                      select new { StatusReason = c.FormattedValues["statuscode"] };
    foreach (var c in list_retrieve1)
    {
        System.Console.WriteLine("Status: " + c.StatusReason);
    }
}
```  

  
<a name="BKMK_UsingTheSkipAndTakeOperatorsWithoutPaging"></a>   
## Use the Skip and Take operators without paging 

 The following sample shows how to retrieve just two rows after skipping two rows where the LastName is not “Parker” using the [Skip](/dotnet/api/system.linq.enumerable.skip) and [Take](/dotnet/api/system.linq.enumerable.take)operators.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{

    var query_skip = (from c in svcContext.ContactSet
                   where c.LastName != "Parker"
                   orderby c.FirstName
                   select new
                       {
                        last = c.LastName,
                        first = c.FirstName
                       }).Skip(2).Take(2);
    foreach (var c in query_skip)
    {
        System.Console.WriteLine(c.first + " " + c.last);
    }
}
```  

  
<a name="BKMK_UsingTheFirstOrDefaultAndSingleOrDefaultOperators"></a>   
## Use the FirstOrDefault and SingleOrDefault operators  
 The [FirstOrDefault](/dotnet/api/system.linq.enumerable.firstordefault) operator returns the first element of a sequence, or a default value if no element is found. The [SingleOrDefault](/dotnet/api/system.linq.enumerable.singleordefault) operator returns a single, specific element of a sequence, or a default value if that element is not found. The following sample shows how to use these operators.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{

    Contact firstorcontact = svcContext.ContactSet.FirstOrDefault();

    Contact singleorcontact = svcContext.ContactSet
        .SingleOrDefault(c => c.ContactId == _contactId1);


    System.Console.WriteLine(firstorcontact.FullName +
        " is the first contact");
    System.Console.WriteLine("==========================");
    System.Console.WriteLine(singleorcontact.FullName +
        " is the single contact");
}
```  

  
<a name="BKMK_UsingASelfJoinWithConditionOnLinkedEntity"></a>

## Use a self-join with a condition on the linked table row

 The following sample shows how to retrieve the names of two accounts where one account is the parent account of the other.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_joincond = from a1 in svcContext.AccountSet
                      join a2 in svcContext.AccountSet
                      on a1.ParentAccountId.Id equals a2.AccountId
                      where a2.AccountId == _accountId1
                      select new { Account = a1, Parent = a2 };
    foreach (var a in query_joincond)
    {
        System.Console.WriteLine(a.Account.Name + " " + a.Parent.Name);
    }
}
```  

  
<a name="BKMK_UsingTransformationInTheWhereClause"></a>   
## Use a transformation in the Where Clause  
 The following sample shows how to retrieve a specific contact where the anniversary date is later than January 1, 2010.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_wheretrans = from c in svcContext.ContactSet
                        where c.ContactId == _contactId1 &&
                        c.Anniversary > DateTime.Parse("1/1/2010")
                        select new
                        {
                         c.FirstName,
                         c.LastName
                        };
    foreach (var c in query_wheretrans)
    {
        System.Console.WriteLine(c.FirstName + " " + c.LastName);
    }
}
```  

  
<a name="BKMK_UsingAPagingSort"></a>   
## Use a paging sort  
 The following sample shows a multi-column sort with an extra condition.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_pagingsort1 = (from c in svcContext.ContactSet
                          where c.LastName != "Parker"
                          orderby c.LastName ascending,
                          c.FirstName descending
                          select new { c.FirstName, c.LastName })
                          .Skip(2).Take(2);
    foreach (var c in query_pagingsort1)
    {
        System.Console.WriteLine(c.FirstName + " " + c.LastName);
    }
}
```  

  
 The following sample shows a paging sort where the column being sorted is different from the column being retrieved.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_pagingsort2 = (from c in svcContext.ContactSet
                          where c.LastName != "Parker"
                          orderby c.FirstName descending
                          select new { c.FirstName }).Skip(2).Take(2);
    foreach (var c in query_pagingsort2)
    {
        System.Console.WriteLine(c.FirstName);
    }
}
```  

  
 The following sample shows how to retrieve just the first 10 rows.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_pagingsort3 = (from c in svcContext.ContactSet
                          where c.LastName.StartsWith("W")
                          orderby c.MiddleName ascending,
                          c.FirstName descending
                          select new
                          {
                           c.FirstName,
                           c.MiddleName,
                           c.LastName
                          }).Take(10);
    foreach (var c in query_pagingsort3)
    {
        System.Console.WriteLine(c.FirstName + " " +
            c.MiddleName + " " + c.LastName);
    }
}
```  

  
<a name="BKMK_RetrievingRelatedEntityColumns"></a>

## Retrieve related table row columns for 1 to N relationships  

 The following sample shows how to retrieve columns from related account and contact rows.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
     var query_retrieve1 = from c in svcContext.ContactSet
                       join a in svcContext.AccountSet
                       on c.ContactId equals a.PrimaryContactId.Id
                       where c.ContactId != _contactId1
                       select new { Contact = c, Account = a };
     foreach (var c in query_retrieve1)
    {
          System.Console.WriteLine("Acct: " + c.Account.Name +
           "\t\t" + "Contact: " + c.Contact.FullName);
     }
}
```  
  
<a name="BKMK_UsingValueToRetrieveTheValueOfAnAttribute"></a>

## Use .value to retrieve the value of a column (attribute)

 The following sample shows usage of Value to access the value of an attribute.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{

     var query_value = from c in svcContext.ContactSet
                   where c.ContactId != _contactId2
                   select new
                   {
                    ContactId = c.ContactId != null ?
                     c.ContactId.Value : Guid.Empty,
                    NumberOfChildren = c.NumberOfChildren != null ?
                     c.NumberOfChildren.Value : default(int),
                    CreditOnHold = c.CreditOnHold != null ?
                     c.CreditOnHold.Value : default(bool),
                    Anniversary = c.Anniversary != null ?
                     c.Anniversary.Value : default(DateTime)
                   };

     foreach (var c in query_value)
     {
      System.Console.WriteLine(c.ContactId + " " + c.NumberOfChildren + 
           " " + c.CreditOnHold + " " + c.Anniversary);
     }
}
```  
  
<a name="BKMK_MultipleProjectionsNewDataTypeCastingToDifferentTypes"></a>   
## Multiple projections, new data type casting to different types  
 The following sample shows multiple projections and how to cast values to a different type.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
     var query_projections = from c in svcContext.ContactSet
                         where c.ContactId == _contactId1
                         && c.NumberOfChildren != null && 
                         c.Anniversary.Value != null
                         select new
                         {
                          Contact = new Contact { 
                           LastName = c.LastName, 
                           NumberOfChildren = c.NumberOfChildren 
                          },
                          NumberOfChildren = (double)c.NumberOfChildren,
                          Anniversary = c.Anniversary.Value.AddYears(1),
                         };
     foreach (var c in query_projections)
     {
          System.Console.WriteLine(c.Contact.LastName + " " + 
               c.NumberOfChildren + " " + c.Anniversary);
     }
}
```  
  
<a name="BKMK_UsingTheGetAttributeValueMethod"></a>

## Use the GetAttributeValue method

 The following sample shows how to use the <xref:Microsoft.Xrm.Sdk.Entity.GetAttributeValue``1(System.String)> method.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_getattrib = from c in svcContext.ContactSet
                       where c.GetAttributeValue<Guid>("contactid") != _contactId1
                       select new
                       {
                        ContactId = c.GetAttributeValue<Guid?>("contactid"),
                        NumberOfChildren = c.GetAttributeValue<int?>("numberofchildren"),
                        CreditOnHold = c.GetAttributeValue<bool?>("creditonhold"),
                        Anniversary = c.GetAttributeValue<DateTime?>("anniversary"),
                       };

    foreach (var c in query_getattrib)
    {
        System.Console.WriteLine(c.ContactId + " " + c.NumberOfChildren + 
            " " + c.CreditOnHold + " " + c.Anniversary);
    }
}
```  
  
<a name="mathoperators"></a>   
## Use Math methods  
 The following sample shows how to use various [Math](/dotnet/api/system.math) methods.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_math = from c in svcContext.ContactSet
                  where c.ContactId != _contactId2
                  && c.Address1_Latitude != null && 
                  c.Address1_Longitude != null
                  select new
                  {
                   Round = Math.Round(c.Address1_Latitude.Value),
                   Floor = Math.Floor(c.Address1_Latitude.Value),
                   Ceiling = Math.Ceiling(c.Address1_Latitude.Value),
                   Abs = Math.Abs(c.Address1_Latitude.Value),
                  };
    foreach (var c in query_math)
    {
        System.Console.WriteLine(c.Round + " " + c.Floor + 
            " " + c.Ceiling + " " + c.Abs);
    }
}
```  
  
<a name="BKMK_UsingMultipleSelectAndWhereClauses"></a>   
## Use Multiple Select and Where clauses  
 The following sample shows multiple select and where clauses using a method-based query syntax.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_multiselect = svcContext.IncidentSet
                        .Where(i => i.IncidentId != _incidentId1)
                        .Select(i => i.incident_customer_accounts)
                        .Where(a => a.AccountId != _accountId2)
                        .Select(a => a.account_primary_contact)
                        .OrderBy(c => c.FirstName)
                        .Select(c => c.ContactId);
    foreach (var c in query_multiselect)
    {
        System.Console.WriteLine(c.GetValueOrDefault());
    }
}
```  
  
<a name="BKMK_UsingSelectMany"></a>   
## Use SelectMany  
 The following sample shows how to use the [SelectMany Method](/dotnet/api/system.linq.enumerable.selectmany).  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_selectmany = svcContext.ContactSet
                        .Where(c => c.ContactId != _contactId2)
                        .SelectMany(c => c.account_primary_contact)
                        .OrderBy(a => a.Name);
    foreach (var c in query_selectmany)
    {
        System.Console.WriteLine(c.AccountId + " " + c.Name);    
    }
}
```
  
<a name="BKMK_UsingStringOperations"></a>   
## Use string operations  
 The following sample shows how to use various String methods.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_string = from c in svcContext.ContactSet
                    where c.ContactId == _contactId2
                    select new
                    {
                     IndexOf = c.FirstName.IndexOf("contact"),
                     Insert = c.FirstName.Insert(1, "Insert"),
                     Remove = c.FirstName.Remove(1, 1),
                     Substring = c.FirstName.Substring(1, 1),
                     ToUpper = c.FirstName.ToUpper(),
                     ToLower = c.FirstName.ToLower(),
                     TrimStart = c.FirstName.TrimStart(),
                     TrimEnd = c.FirstName.TrimEnd(),
                    };

    foreach (var c in query_string)
    {
        System.Console.WriteLine(c.IndexOf + "\n" + c.Insert + "\n" + 
            c.Remove + "\n" + c.Substring + "\n"
            + c.ToUpper + "\n" + c.ToLower + 
            "\n" + c.TrimStart + " " + c.TrimEnd);
    }
}
```
  
<a name="BKMK_UsingTwoWhereClauses"></a>   
## Use two Where clauses  
 The following sample shows how to use two Where clauses.  
  
```csharp
using (ServiceContext svcContext = new ServiceContext(_serviceProxy))
{
    var query_twowhere = from a in svcContext.AccountSet
                      join c in svcContext.ContactSet 
                      on a.PrimaryContactId.Id equals c.ContactId
                      where c.LastName == "Smith" && c.CreditOnHold != null
                      where a.Name == "Contoso Ltd"
                      orderby a.Name
                      select a;
    foreach (var c in query_twowhere)
    {
         System.Console.WriteLine(c.AccountId + " " + c.Name);
    }
}
``` 
  
<a name="BKMK_UseLoadProperty"></a>

## Use LoadProperty to retrieve related rows

 The following sample shows how to [Relationship)]<xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext.LoadProperty(Microsoft.Xrm.Sdk.Entity,Microsoft.Xrm.Sdk.Relationship)> to access related rows.  
  
```csharp
Contact benAndrews = svcContext.ContactSet.Where(c => c.FullName == "Ben Andrews").FirstOrDefault();
if (benAndrews != null)
{
     //benAndrews.Contact_Tasks is null until LoadProperty is used.
     svcContext.LoadProperty(benAndrews, "Contact_Tasks");
     Task benAndrewsFirstTask = benAndrews.Contact_Tasks.FirstOrDefault();
     if (benAndrewsFirstTask != null)
     {
          Console.WriteLine("Ben Andrews first task with Subject: '{0}' retrieved.", benAndrewsFirstTask.Subject);
     }
}
```
  


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]