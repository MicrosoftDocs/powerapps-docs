---
title: "Page large result sets with FetchXML (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Read how you can page the results of a FetchXML query by using the paging cookie" # 115-145 characters including spaces. This abstract displays in the search result.
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
# Page large result sets with FetchXML

[!INCLUDE[cc-data-platform-banner](../../../includes/cc-data-platform-banner.md)]

You can page the results of a FetchXML query by using the paging cookie. The paging cookie is a performance feature that makes paging in the application faster for very large datasets. When you query for a set of records, the result will contain a value for the paging cookie. For better performance, you can pass that value when you retrieve the next set of records.  
  
 FetchXML and <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> use different formats for their paging cookies. If you convert from one query format to the other by using the <xref:Microsoft.Crm.Sdk.Messages.FetchXmlToQueryExpressionRequest> message or the <xref:Microsoft.Crm.Sdk.Messages.QueryExpressionToFetchXmlRequest> message, the paging cookie value is ignored. In addition, if you request nonconsecutive pages, the paging cookie value is ignored.  
  
 When you use the paging cookie with FetchXML, make sure that you use the correct encoding. The following example shows the correct encoding when using the paging cookie with FetchXML:  
  
```csharp  
strQueryXML = @"  
<fetch mapping='logical' paging-cookie='&lt;cookie page=&quot;1&quot;&gt;&lt;accountid last=&quot;{E062B974-7F8D-DC11-9048-0003FF27AC3B}&quot; first=&quot;{60B934EF-798D-DC11-9048-0003FF27AC3B}&quot;/&gt;&lt;/cookie&gt;' page='2' count='2'>  
 <entity name='account'>  
  <all-attributes/>  
 </entity>  
</fetch>";  
```  
  
## FetchXML and the Paging Cookie Example  
 The following example shows how to use the paging cookie with a FetchXML query. For the complete sample code, see [Sample: Use FetchXML with a Paging Cookie](samples/use-fetchxml-paging-cookie.md).  
  
```csharp
// Define the fetch attributes.
// Set the number of records per page to retrieve.
int fetchCount = 3;
// Initialize the page number.
int pageNumber = 1;
// Initialize the number of records.
int recordCount = 0;
// Specify the current paging cookie. For retrieving the first page, 
// pagingCookie should be null.
string pagingCookie = null;

// Create the FetchXml string for retrieving all child accounts to a parent account.
// This fetch query is using 1 placeholder to specify the parent account id 
// for filtering out required accounts. Filter query is optional.
// Fetch query also includes optional order criteria that, in this case, is used 
// to order the results in ascending order on the name data column.
string fetchXml = string.Format(@"<fetch version='1.0' 
                                mapping='logical' 
                                output-format='xml-platform'>
                                <entity name='account'>
                                    <attribute name='name' />
                                    <attribute name='emailaddress1' />
                                    <order attribute='name' descending='false'/>
                                    <filter type='and'>
                            <condition attribute='parentaccountid' 
                                            operator='eq' value='{0}' uiname='' uitype='' />
                                    </filter>
                                </entity>
                            </fetch>",
                                _parentAccountId);

Console.WriteLine("Retrieving data in pages\n"); 
Console.WriteLine("#\tAccount Name\t\t\tEmail Address");

while (true)
{
    // Build fetchXml string with the placeholders.
    string xml = CreateXml(fetchXml, pagingCookie, pageNumber, fetchCount);

    // Excute the fetch query and get the xml result.
    RetrieveMultipleRequest fetchRequest1 = new RetrieveMultipleRequest
    {
        Query = new FetchExpression(xml)
    };

    EntityCollection returnCollection = ((RetrieveMultipleResponse)_service.Execute(fetchRequest1)).EntityCollection;
    
    foreach (var c in returnCollection.Entities)
    {
        System.Console.WriteLine("{0}.\t{1}\t\t{2}", ++recordCount, c.Attributes["name"], c.Attributes["emailaddress1"] );
    }                        
    
    // Check for morerecords, if it returns 1.
    if (returnCollection.MoreRecords)
    {
        Console.WriteLine("\n****************\nPage number {0}\n****************", pageNumber);
        Console.WriteLine("#\tAccount Name\t\t\tEmail Address");
        
        // Increment the page number to retrieve the next page.
        pageNumber++;

        // Set the paging cookie to the paging cookie returned from current results.                            
        pagingCookie = returnCollection.PagingCookie;
    }
    else
    {
        // If no more records in the result nodes, exit the loop.
        break;
    }
}
```
  
### See also

 [Paging behaviors and ordering](paging-behaviors-and-ordering.md)  
 [Sample: Use FetchXML with a Paging Cookie](samples/use-fetchxml-paging-cookie.md)   
 [Building Queries with FetchXML](/dynamics365/customer-engagement/developer/org-service/build-queries-fetchxml)   
 [Fiscal date and older than datetime query operators in FetchXML](../use-fetchxml-fiscal-date-older-datetime-query-operators.md)   
 [Using FetchXML](../use-fetchxml-construct-query.md)   
 [Page large result sets with QueryExpression](page-large-result-sets-with-queryexpression.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]