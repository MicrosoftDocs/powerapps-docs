---
title: "Use LINQ to construct a query (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Describes how to use the .NET Language-Integrated Query (LINQ) query provider to construct a Microsoft Dataverse query." # 115-145 characters including spaces. This abstract displays in the search result.
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

# Use LINQ to construct a query

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

The .NET Language-Integrated Query (LINQ) query provider in Microsoft Dataverse uses standard LINQ syntax. The first step in creating a LINQ query is to identify the relevant table types and the relationships between them. You can then specify the data source and the other query parameters.  

 The `from` clause is used to return a single “root” table. The query provider can only return rows of a single table type. The `orderby` and `select` clauses must reference this root table. You can use `join` clauses to add rows with a relationship to the “root” table.  

<a name="bkmk_operators"></a>   

## LINQ operators

 All LINQ query expressions have a similar format. The following table shows the most common clauses in a LINQ query expression when using the Dataverse LINQ query provider.  

### from

 When using the generated service context and early binding, use the `IQueryable` table set, such as `AccountSet`, in the generated context.  

 When not using the generated context, the `CreateQuery` method on the Organization service context object gives you access to Dataverse table rows.  

 Example:  

 Using the generated service context:  

```csharp  
var query1 = from c in context.ContactSet  
select c;  
```  

 Using the `CreateQuery` method:  

```csharp  
var query1 = from c in context.CreateQuery<Contact>()  
select c;  
```  

### join

 The `join` clause represents an inner join. You use the clause to work with two or more tables that can be joined with a common column value.

 Example:  

```csharp  
from c in context.ContactSet  
join a in context.AccountSet on c.ContactId equals a.PrimaryContactId.Id  
```  

### where

 The `where` clause applies a filter to the results, often using a Boolean expression. The filter specifies which elements to exclude from the source sequence. Each `where` clause can only contain conditions against a single table type. A composite condition involving multiple tables is not valid. Instead, each table should be filtered in separate `where` clauses.  

 Example:  

```csharp  
from a in context.AccountSet  
where (a.Name.StartsWith("Contoso") && a.Address1_StateOrProvince == "WA")  
```  

### orderby

 The `orderby` operator puts the returned query columns in a specified order.  

 Example:  

```csharp  
var query1 = from c in context.CreateQuery<Contact>()     
    orderby c.FullName ascending     
    select c;  
foreach ( var q in query1)     
{  
    Console.WriteLine(q.FirstName + " " + q.LastName);     
}  
```  

### select

 The `select` clause defines the form of the data returned. The clause creates a column set based on the query expression results. You can also define an instance of a new object to work with. The newly created object using the `select` clause is not created on the server, but is a local instance.  

 Example:  

```csharp  
select new Contact     
{  
    ContactId = c.ContactId,  
    FirstName = c.FirstName,  
    LastName = c.LastName,  
    Address1_Telephone1 = c.Address1_Telephone1     
};  
```  

<a name="limitations"></a>   

## LINQ limitations  

 The LINQ query provider supports a subset of the LINQ operators. Not all conditions that can be expressed in LINQ are supported. The following table shows some of the limitations of the basic LINQ operators.  


|   LINQ Operator   |                                                                                                                                              Limitations                                                                                                                                              |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      `join`       |                                                                                                                Represents an inner or outer join. Only left outer joins are supported.                                                                                                                |
|      `from`       |                                                                                                                                 Supports one `from` clause per query.                                                                                                                                 |
|      `where`      | The left side of the clause must be a column name and the right side of the clause must be a value. You cannot set the left side to a constant. Both the sides of the clause cannot be constants.<br /><br /> Supports the `String` functions `Contains`, `StartsWith`, `EndsWith`, and `Equals`. |
|     `groupBy`     |                               Not supported. FetchXML supports grouping options that are not available with the LINQ query provider. More information: [Use FetchXML Aggregation](/dynamics365/customer-engagement/developer/use-fetchxml-aggregation)                               |
|     `orderBy`     |                                                                                                                  Supports ordering by table columns, such as `Contact.FullName`.                                                                                                                  |
|     `select`      |                                                                                                                       Supports anonymous types, constructors, and initializers.                                                                                                                       |
|      `last`       |                                                                                                                                 The `last` operator is not supported.                                                                                                                                 |
| `skip` and `take` |                                                                                       Supports `skip` and `take` using server-side paging. The `skip` value must be greater than or equal to the `take` value.                                                                                        |
|    `aggregate`    |                             Not supported. FetchXML supports aggregation options that are not available with the LINQ query provider. More information: [Use FetchXML Aggregation](/dynamics365/customer-engagement/developer/use-fetchxml-aggregation)                              |

<a name="filter"></a>   

## Filter multiple tables 

 You can create complex .NET Language Integrated Query(LINQ) queries in Dataverse. You use multiple `Join` clauses with filter clauses to create a result that is filtered on columns from several tables.  

 The following sample shows how to create a LINQ query that works with two tables and filters the result based on values from each of the table rows.  

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

### See also

 [Sample: Create a LINQ Query](/dynamics365/customer-engagement/developer/org-service/sample-create-linq-query)   
 [Sample: LINQ query examples](/dynamics365/customer-engagement/developer/org-service/sample-complex-linq-queries)   
 [Build queries with LINQ (.NET Language-Integrated Query)](/dynamics365/customer-engagement/developer/org-service/build-queries-with-linq-net-language-integrated-query)   
 [Use late-bound Entity class with a LINQ query](/dynamics365/customer-engagement/developer/org-service/use-late-bound-entity-class-linq-query)   
 [Blog: LINQPad 4 driver for Dataverse Web API are available on CodePlex](https://blogs.msdn.com/b/crminthefield/archive/2015/06/11/linqpad-4-driver-for-dynamics-crm-rest-webapi-are-available-on-codeplex.aspx)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]