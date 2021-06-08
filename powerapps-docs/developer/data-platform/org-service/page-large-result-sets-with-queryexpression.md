---
title: "Page large result sets with QueryExpression (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use the paging cookie feature to make paging in an application faster for large datasets." # 115-145 characters including spaces. This abstract displays in the search result.
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

# Page large result sets with QueryExpression

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

In Microsoft Dataverse, you can use the paging cookie feature to make paging in an application faster for large datasets. The feature is available in both FetchXML and <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> queries. When you use the paging cookie feature when querying a set of table rows (records), the result contains a value for the paging cookie. To improve system performance, you can then pass that value when you retrieve the next set of rows.  
  
 <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> and FetchXML use different formats for their paging cookies. If you convert from one query format to the other by using the <xref:Microsoft.Crm.Sdk.Messages.QueryExpressionToFetchXmlRequest> message or the <xref:Microsoft.Crm.Sdk.Messages.FetchXmlToQueryExpressionRequest> message, the paging cookie value is ignored. In addition, if you request nonconsecutive pages, the paging cookie value is ignored.  
  
<a name="QueryExpression"></a>

## Using a paging cookie with QueryExpression

 The following example shows how to use the paging cookie with a query expression. For the complete sample code, see [Sample: Use QueryExpression with a paging cookie](../org-service/samples/use-queryexpression-with-a-paging-cookie.md).  
  
```csharp
// Query using the paging cookie.
// Define the paging attributes.
// The number of records per page to retrieve.
int queryCount = 3;

// Initialize the page number.
int pageNumber = 1;

// Initialize the number of records.
int recordCount = 0;

// Define the condition expression for retrieving records.
ConditionExpression pagecondition = new ConditionExpression();
pagecondition.AttributeName = "parentaccountid";
pagecondition.Operator = ConditionOperator.Equal;
pagecondition.Values.Add(_parentAccountId);

// Define the order expression to retrieve the records.
OrderExpression order = new OrderExpression();
order.AttributeName = "name";
order.OrderType = OrderType.Ascending;

// Create the query expression and add condition.
QueryExpression pagequery = new QueryExpression();
pagequery.EntityName = "account";
pagequery.Criteria.AddCondition(pagecondition);
pagequery.Orders.Add(order);
pagequery.ColumnSet.AddColumns("name", "emailaddress1");                   

// Assign the pageinfo properties to the query expression.
pagequery.PageInfo = new PagingInfo();
pagequery.PageInfo.Count = queryCount;
pagequery.PageInfo.PageNumber = pageNumber;

// The current paging cookie. When retrieving the first page, 
// pagingCookie should be null.
pagequery.PageInfo.PagingCookie = null;
Console.WriteLine("Retrieving sample account records in pages...\n");
Console.WriteLine("#\tAccount Name\t\tEmail Address"); 

while (true)
{
    // Retrieve the page.
    EntityCollection results = _serviceProxy.RetrieveMultiple(pagequery);
    if (results.Entities != null)
    {
        // Retrieve all records from the result set.
        foreach (Account acct in results.Entities)
        {
            Console.WriteLine("{0}.\t{1}\t{2}", ++recordCount, acct.Name,
                               acct.EMailAddress1);
        }
    }

    // Check for more records, if it returns true.
    if (results.MoreRecords)
    {
        Console.WriteLine("\n****************\nPage number {0}\n****************", pagequery.PageInfo.PageNumber);
        Console.WriteLine("#\tAccount Name\t\tEmail Address");

        // Increment the page number to retrieve the next page.
        pagequery.PageInfo.PageNumber++;
        
        // Set the paging cookie to the paging cookie returned from current results.
        pagequery.PageInfo.PagingCookie = results.PagingCookie;
    }
    else
    {
        // If no more records are in the result nodes, exit the loop.
        break;
    }
}
```

### See also

 [Building queries with QueryExpression](build-queries-with-queryexpression.md)   
 [Sample: Use QueryExpression with a paging cookie](samples/use-queryexpression-with-a-paging-cookie.md)   
 [Sample: Retrieve with one-to-many relationship](/dynamics365/customer-engagement/developer/retrieve-with-one-to-many-relationship)   
 [Using the QueryExpression class](use-queryexpression-class.md)   
 [Page large result sets with FetchXML](page-large-result-sets-with-fetchxml.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]