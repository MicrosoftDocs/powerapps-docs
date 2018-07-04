---
title: "Web API Query Data Sample (C#) (Common Data Service for Apps)| Microsoft Docs"
description: "This sample demonstrates how to perform basic query requests using the Common Data Service for Apps Web API and C#"
ms.custom: ""
ms.date: 06/15/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 91183105-bc99-4e34-a1b3-1085e1a51f82
caps.latest.revision: 16
author: "JimDaly"
ms.author: "jdaly"
---
# Web API Query Data Sample (C#)

This sample demonstrates how to perform basic query requests using the Common Data Service for Apps Web API with C#.  
  
> [!NOTE]
>  This sample implements the Common Data Service for Apps operations and console output detailed in [Web API Query Data Sample](web-api-query-data-sample.md) and uses the common C# constructs described in [Web API Samples (C#)](web-api-samples-csharp.md).  
  
<a name="bkmk_prerequisites"></a>

## Prerequisites

Prerequisites for all Common Data Service for Apps Web API C# samples are detailed in the [Prerequisites](web-api-samples-csharp.md#bkmk_prerequisites) section of the parent topic [Web API Samples (C#)](web-api-samples-csharp.md).  
  
<a name="bkmk_runSample"></a>

## Run this sample
  
First go to [Microsoft CRM Web API Query Data Sample (C#)](http://go.microsoft.com/fwlink/p/?LinkId=824049), download the sample archive file, Microsoft CRM Web API Query Data Sample (CS).zip, and extract its contents into a local folder. This folder should contain the following files:  
  
|File|Purpose/Description|  
|----------|--------------------------|  
|Program.cs|Contains the primary source code for this sample.|  
|App.config|The application configuration file, which contains placeholder Common Data Service for Apps server connection information.|  
|Authentication.cs<br />Configuration.cs<br />Exceptions.cs|Located in the folder **Web API Helper Code**, these files comprise the supplemental library detailed in [Use the Common Data Service for Apps Web API Helper Library (C#)](use-microsoft-dynamics-365-web-api-helper-library-csharp.md).|  
|QueryData.sln <br />QueryData.csproj <br />Packages.config <br />AssemblyInfo.cs|The standard Visual Studio 2015 solution, project, NuGet package configuration, and assembly information files for this sample.|  
  
Next, use the following procedure to run this sample.  
  
1.  Locate and double-click on the solution file, QueryData.sln, to load the solution into Visual Studio. Build the **QueryData** solution.  This should automatically download and install all the required NuGet packages that are either missing or need to be updated.  
2.  Edit the application configuration file, App.config, to specify connection information for your Common Data Service for Apps server.  For more information, see [Helper code: Configuration classes](web-api-helper-code-configuration-classes.md).  
3.  Run the **QueryData** project from within Visual Studio.  All sample solutions are configured to run in debug mode by default.  
  
<a name="bkmk_codeListing"></a>
  
## Code listing

The most current source for this file  is found in sample download package.  
  
 `Program.cs`  
  
```csharp  
  
using Microsoft.Crm.Sdk.Samples.HelperCode;  
using Newtonsoft.Json;  
using Newtonsoft.Json.Linq;  
using System;  
using System.Net;  
using System.Linq;  
using System.Text;  
using System.Collections.Generic;  
using System.Net.Http;  
using System.Net.Http.Headers;  
using System.Threading.Tasks;  
  
namespace Microsoft.Crm.Sdk.Samples  
{  
    /// <summary>  
    /// This program demonstrates queries using Web API calls in Dynamics CRM or later.   
    /// </summary>  
    /// <remarks>  
    /// This program demonstrates the following query capabilities:  
    /// - Using “$select” option to request specific properties   
    /// - Requesting formatted values  
    /// - Using filter option to refine results  
    /// - Setting “$orderby” preferences on results  
    /// - Limiting the number of records returned in results  
    /// - Requesting a count of the returned entries matching the filter  
    /// - Setting pagination preferences  
    /// - Requesting additional data using the “$expand” option  
    ///  
    /// Before building this application, you must first modify the following configuration   
    /// information in the app.config file:  
    ///   - All deployments: Provide connection string service URL's for your organization.  
    ///   - CRM (online): Replace the application settings with the correct values for your    
    ///                 Azure app registration.   
    /// See the provided app.config file for more information.   
    /// </remarks>  
    class QueryData  
    {  
        //centralized collection of absolute URIs for created entity instances  
        private List<string> entityUris = new List<string>();  
        private HttpClient httpClient;  //Client to CRM server communication  
        //account1 represents 'Contoso Ltd (sample)' and   
        // contact1 represents 'Yvonne McKey (sample)'.  
        JObject account1, contact1;  
        string account1Uri, contact1Uri;  
  
        /// <summary> Contains primary Web API code for the sample. </summary>  
        public async Task RunAsync()  
        {  
            string queryOptions;  //select, expand and filter clauses  
            //Entity properties to select in a request and display.  
            string[] contactProperties = { "fullname", "jobtitle", "annualincome" };  
            string[] accountProperties = { "name" };  
            string[] taskProperties = { "subject", "description" };  
            HttpRequestMessage request;  
            HttpResponseMessage response;  
  
            #region Selecting specific properties  
            // Basic query: Query using $select against a contact entity to get the properties you want.  
            // For performance best practice, always use $select, otherwise all properties are returned.  
            Console.WriteLine("-- Basic Query --");  
            queryOptions = "?$select=" + String.Join(",", contactProperties);  
            //Request formatted values be returned (in addition to standard unformatted values).  
            response = await SendCrmRequestAsync(HttpMethod.Get, contact1Uri + queryOptions, true);  
            if (response.StatusCode == HttpStatusCode.OK) //200  
            {  
                contact1 = JsonConvert.DeserializeObject<JObject>(  
                    response.Content.ReadAsStringAsync().Result);  
                Console.WriteLine(  
                 "Contact basic info:\n\tFullname: {0}\n\tJobtitle: {1}\n\tAnnualincome: {2} (unformatted)",  
                  contact1["fullname"], contact1["jobtitle"], contact1["annualincome"]);  
                Console.WriteLine("\tAnnualincome: {0} (formatted)\n",  
                    contact1["annualincome@OData.Community.Display.V1.FormattedValue"]);  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
            #endregion Selecting specific properties  
  
            #region Using query functions  
            // Filter criteria:  
            // Applying filters to get targeted data.  
            // 1) Using standard query functions (e.g.: contains, endswith, startswith)  
            // 2) Using CRM query functions (e.g.: LastXhours, Last7Days, Today, Between, In, ...)  
            // 3) Using filter operators and logical operators (e.g.: eq, ne, gt, and, or, etc…)  
            // 4) Set precedence using parenthesis (e.g.: ((criteria1) and (criteria2)) or (criteria3)  
            // For more info, see: https://msdn.microsoft.com/en-us/library/gg334767.aspx#bkmk_filter  
            Console.WriteLine("-- Filter Criteria --");  
            JObject collection;  
  
            //Filter 1: Using standard query functions to filter results.  In this operation, we   
            //will query for all contacts with fullname containing the string "(sample)".  
            string filter = @"&$filter=contains(fullname,'(sample)')";  
            queryOptions = "?$select=" + String.Join(",", contactProperties) + filter;  
            response = await SendCrmRequestAsync(HttpMethod.Get, "contacts" + queryOptions, true);  
            if (response.StatusCode == HttpStatusCode.OK) //200  
            {  
                collection = JsonConvert.DeserializeObject<JObject>(response.Content.ReadAsStringAsync().Result);  
                DisplayFormattedEntities("Contacts filtered by fullname containing '(sample)':",  
                    collection, contactProperties);  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
  
            //Filter 2: Using CRM query functions to filter results. In this operation, we will query  
            //for all contacts that were created in the last hour. For complete list of CRM query    
            //functions, see: https://msdn.microsoft.com/en-us/library/mt607843.aspx  
            filter = "&$filter=Microsoft.Dynamics.CRM.LastXHours(PropertyName='createdon',PropertyValue='1')";  
            queryOptions = "?$select=" + String.Join(",", contactProperties) + filter;  
            response = await SendCrmRequestAsync(HttpMethod.Get, "contacts" + queryOptions, true);  
            if (response.StatusCode == HttpStatusCode.OK) //200  
            {  
                collection = JsonConvert.DeserializeObject<JObject>(response.Content.ReadAsStringAsync().Result);  
                DisplayFormattedEntities("Contacts that were created within the last 1hr:",  
                    collection, contactProperties);  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
  
            //Filter 3: Using operators. Building on the previous operation, we further limit  
            //the results by the contact's income. For more info on standard filter operators,   
            //https://msdn.microsoft.com/en-us/library/gg334767.aspx#bkmk_filter  
            filter = "&$filter=contains(fullname,'(sample)') and annualincome gt 55000";  
            queryOptions = "?$select=" + String.Join(",", contactProperties) + filter;  
            response = await SendCrmRequestAsync(HttpMethod.Get, "contacts" + queryOptions, true);  
            if (response.StatusCode == HttpStatusCode.OK) //200  
            {  
                collection = JsonConvert.DeserializeObject<JObject>(response.Content.ReadAsStringAsync().Result);  
                DisplayFormattedEntities("Contacts filtered by fullname and annualincome (<$55,000):",  
                    collection, contactProperties);  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
  
            //Filter 4: Set precedence using parenthesis. Continue building on the previous   
            //operation, we further limit results by job title. Parenthesis and the order of   
            //filter statements can impact results returned.  
            filter = "&$filter=contains(fullname,'(sample)') and(contains(jobtitle, 'senior')" +  
            " or contains(jobtitle,'specialist')) and annualincome gt 55000";  
            queryOptions = "?$select=" + String.Join(",", contactProperties) + filter;  
            response = await SendCrmRequestAsync(HttpMethod.Get, "contacts" + queryOptions, true);  
            if (response.StatusCode == HttpStatusCode.OK) //200  
            {  
                collection = JsonConvert.DeserializeObject<JObject>(response.Content.ReadAsStringAsync().Result);  
                DisplayFormattedEntities("Contacts filtered by fullname, annualincome and jobtitle " +  
                    "(Senior or Specialist):", collection, contactProperties);  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
            #endregion Using query functions  
  
            #region Ordering and aliases  
            //Results can be ordered in descending or ascending order.  
            Console.WriteLine("\n-- Order Results --");  
            filter = @"&$filter=contains(fullname,'(sample)') &$orderby=jobtitle asc, annualincome desc";  
            queryOptions = "?$select=" + String.Join(",", contactProperties) + filter;  
            response = await SendCrmRequestAsync(HttpMethod.Get, "contacts" + queryOptions, true);  
            if (response.StatusCode == HttpStatusCode.OK) //200  
            {  
                collection = JsonConvert.DeserializeObject<JObject>(response.Content.ReadAsStringAsync().Result);  
                DisplayFormattedEntities("Contacts ordered by jobtitle (Ascending) and annualincome (descending):",  
                    collection, contactProperties);  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
  
            //Parameterized aliases can be used as parameters in a query. These parameters can be used   
            //in $filter and $orderby options. Using the previous operation as basis, parameterizing the   
            //query will give us the same results. For more info, see:   
            //https://msdn.microsoft.com/en-us/library/gg309638.aspx#bkmk_passParametersToFunctions  
            Console.WriteLine("\n-- Parameterized Aliases --");  
            filter = "&$filter=contains(@p1,'(sample)') &$orderby=@p2 asc, " +  
                "@p3 desc&@p1=fullname&@p2=jobtitle&@p3=annualincome";  
            queryOptions = "?$select=" + String.Join(",", contactProperties) + filter;  
            response = await SendCrmRequestAsync(HttpMethod.Get, "contacts" + queryOptions, true);  
            if (response.StatusCode == HttpStatusCode.OK) //200  
            {  
                collection = JsonConvert.DeserializeObject<JObject>(response.Content.ReadAsStringAsync().Result);  
                DisplayFormattedEntities("Contacts list using parameterized aliases:",  
                    collection, contactProperties);  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
            #endregion Ordering and aliases  
  
            #region Limit results  
            //To limit records returned, use the $top query option.  Specifying a limit number for $top   
            //returns at most that number of results per request. Extra results are ignored.  
            //For more information, see: https://msdn.microsoft.com/en-us/library/gg334767.aspx#bkmk_limits  
            Console.WriteLine("\n-- Top Results --");  
            filter = "&$filter=contains(fullname,'(sample)')&$top=5";  
            queryOptions = "?$select=" + String.Join(",", contactProperties) + filter;  
            response = await SendCrmRequestAsync(HttpMethod.Get, "contacts" + queryOptions, true);  
            if (response.StatusCode == HttpStatusCode.OK) //200  
            {  
                collection = JsonConvert.DeserializeObject<JObject>(response.Content.ReadAsStringAsync().Result);  
                DisplayFormattedEntities("Contacts top 5 results:", collection, contactProperties);  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
  
            //Result count - count the number of results matching the filter criteria.  
            //Tip: Use count together with the "odata.maxpagesize" to calculate the number of pages in  
            //the query.  Note: CRM has a max record limit of 5000 records per response.  
            Console.WriteLine("\n-- Result Count --");  
            string count;  
            //  1) Get a count of a collection without the data.  
            response = await httpClient.GetAsync("contacts/$count"); // Count is returned in response body.  
            if (response.StatusCode == HttpStatusCode.OK) //200  
            {  
                count = JsonConvert.DeserializeObject<JValue>  
                        (response.Content.ReadAsStringAsync().Result).ToString();  
                Console.WriteLine("The contacts collection has {0} contacts.", count);  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
  
            //  2) Get a count along with the data.  
            filter = "&$filter=contains(jobtitle,'senior') or contains(jobtitle, 'manager')&$count=true";  
            queryOptions = "?$select=" + String.Join(",", contactProperties) + filter;  
            response = await SendCrmRequestAsync(HttpMethod.Get, "contacts" + queryOptions, true);  
            if (response.StatusCode == HttpStatusCode.OK) //200  
            {  
                collection = JsonConvert.DeserializeObject<JObject>(response.Content.ReadAsStringAsync().Result);  
                count = collection["@odata.count"].ToString();  
                Console.WriteLine("{0} contacts have either 'Manager' or 'Senior' designation " +  
                    "in their jobtitle.", count);  
                DisplayFormattedEntities("Manager or Senior:", collection, contactProperties);  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
  
            //Pagination: for large data sets, you can limit the number of records returned per page, then  
            //offer a "next page" and "previous page" links for users to browse through all the data.  
            //Note: Typically you do no use $top with maxpagesize because it prevents you from accessing    
            // all possible results in a query. For example, if your query has 10 entities in the result  
            // and you limit your result to $top=5, then you can't get to the remaining 5 results, but  
            // with "maxpagesize" (without $top), you can.  
            //Tip: Save the URI of the current page so users can go "next" and "previous".  
            Console.WriteLine("\n-- Pagination --");  
            string page2Uri;  
            int maxPageSize = 4; //four record per page  
            int maxpages;  
            filter = "&$filter=contains(fullname,'(sample)')&$count=true";  
            queryOptions = "?$select=" + String.Join(",", contactProperties) + filter;  
            response = await SendCrmRequestAsync(HttpMethod.Get, "contacts" + queryOptions, true, maxPageSize);  
            if (response.StatusCode == HttpStatusCode.OK) //200  
            {  
                collection = JsonConvert.DeserializeObject<JObject>(response.Content.ReadAsStringAsync().Result);  
                count = collection["@odata.count"].ToString();  
                maxpages = (int)Math.Ceiling(Convert.ToInt32(count) / 4.0);  
                Console.WriteLine("Contacts total: {0} \tContacts per page: {1}.\tOutputting first 2 pages.",  
                    count, 4);  
                DisplayFormattedEntities("Page 1 of " + maxpages + ":", collection, contactProperties);  
                //Get the next page reference.  
                page2Uri = collection["@odata.nextLink"].ToString(); //This URI is already encoded.  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
            //Retrieve and display the second page of results. The URI was retrieved encoded.  
            response = await SendCrmRequestAsync(HttpMethod.Get, page2Uri, true, maxPageSize);  
            if (response.StatusCode == HttpStatusCode.OK) //200  
            {  
                collection = JsonConvert.DeserializeObject<JObject>(response.Content.ReadAsStringAsync().Result);  
                DisplayFormattedEntities("Page 2 of " + maxpages + ":", collection, contactProperties);  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
            #endregion Limit results  
  
            #region Expanding results  
            //The expand option retrieves related information.    
            //To retrieve information on associated entities in the same request, use the $expand   
            //query option on navigation properties.   
            //  1) Expand using single-valued navigation properties (e.g.: via the 'primarycontactid')  
            //  2) Expand using partner property (e.g.: from contact to account via the 'account_primary_contact')  
            //  3) Expand using collection-valued navigation properties (e.g.: via the 'contact_customer_accounts')  
            //  4) Expand using multiple navigation property types in a single request.  
            // Note: Expansions can only go 1 level deep.  
            // Tip: For performance best practice, always use $select statement in an expand option.  
            Console.WriteLine("\n-- Expanding Results --");  
            string expand;  //expansion portion of query  
  
            //1) Expand using the 'primarycontactid' single-valued navigation property of account1.  
            expand = "&$expand=primarycontactid($select=" + String.Join(",", contactProperties) + ")";  
            queryOptions = "?$select=" + String.Join(",", accountProperties) + expand;  
            response = await SendCrmRequestAsync(HttpMethod.Get, account1Uri + queryOptions, true);  
            if (response.StatusCode == HttpStatusCode.OK) //200  
            {  
                JObject account = JsonConvert.DeserializeObject<JObject>  
                        (response.Content.ReadAsStringAsync().Result);  
                Console.WriteLine("Account {0} has the following primary contact person:\n\t" +  
                    "Fullname: {1} \n\tJobtitle: {2} \n\tAnnualincome: {3}",  
                    account["name"],  
                    account["primarycontactid"]["fullname"],  
                    account["primarycontactid"]["jobtitle"],  
                    account["primarycontactid"]["annualincome"]);  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
  
            //2) Expand using the 'account_primary_contact' partner property.  
            expand = "&$expand=account_primary_contact($select=" + String.Join(",", accountProperties) + ")";  
            queryOptions = "?$select=" + String.Join(",", contactProperties) + expand;  
            response = await SendCrmRequestAsync(HttpMethod.Get, contact1Uri + queryOptions, true);  
            if (response.StatusCode == HttpStatusCode.OK) //200  
            {  
                JObject contact = JsonConvert.DeserializeObject<JObject>  
                        (response.Content.ReadAsStringAsync().Result);  
                string label = "Contact '" + contact["fullname"] +  
                    "' is the primary contact for the following accounts:";  
                DisplayFormattedEntities(label, (JArray)contact["account_primary_contact"], accountProperties);  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
  
            //3) Expand using the collection-valued 'contact_customer_accounts' navigation property.   
            expand = "&$expand=contact_customer_accounts($select=" + String.Join(",", contactProperties) + ")";  
            queryOptions = "?$select=" + String.Join(",", accountProperties) + expand;  
            response = await SendCrmRequestAsync(HttpMethod.Get, account1Uri + queryOptions, true);  
            if (response.StatusCode == HttpStatusCode.OK) //200  
            {  
                JObject account = JsonConvert.DeserializeObject<JObject>  
                        (response.Content.ReadAsStringAsync().Result);  
                string label = "Account '" + account["name"] + "' has the following contact customers:";  
                DisplayFormattedEntities(label, (JArray)account["contact_customer_accounts"], contactProperties);  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
  
            //4) Expand using multiple navigation property types in a single request, specifically:  
            //   primiarycontactid, contact_customer_accounts, and Account_Tasks.  
            Console.WriteLine("\n-- Expanding multiple property types in one request -- ");  
            expand = "&$expand=primarycontactid($select=" + String.Join(",", contactProperties) + ")," +  
                "contact_customer_accounts($select=" + String.Join(",", contactProperties) + ")," +  
                "Account_Tasks($select=" + String.Join(",", taskProperties) + ")";  
            queryOptions = "?$select=" + String.Join(",", accountProperties) + expand;  
            response = await SendCrmRequestAsync(HttpMethod.Get, account1Uri + queryOptions, true);  
            if (response.StatusCode == HttpStatusCode.OK) //200  
            {  
                JObject account = JsonConvert.DeserializeObject<JObject>  
                        (response.Content.ReadAsStringAsync().Result);  
                string label = "Account {0} has the following primary contact person:\n\t" +  
                    "Fullname: {1} \n\tJobtitle: {2} \n\tAnnualincome: {3}";  
                Console.WriteLine(label, account["name"],  
                    account["primarycontactid"]["fullname"],  
                    account["primarycontactid"]["jobtitle"],  
                    account["primarycontactid"]["annualincome"]);  
  
                //Output each collection separately.  
                label = "Account '" + account["name"] + "' has the following related contacts:";  
                DisplayFormattedEntities(label, (JArray)account["contact_customer_accounts"], contactProperties);  
                label = "Account '" + account["name"] + "' has the following tasks:";  
                DisplayFormattedEntities(label, (JArray)account["Account_Tasks"], taskProperties);  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
            #endregion Expanding results  
  
            #region FetchXML queries  
            //Use FetchXML to query for all contacts whose fullname contains '(sample)'.  
            //Note: XML string must be URI encoded. For more information, see:   
            //https://msdn.microsoft.com/en-us/library/gg328117.aspx  
            Console.WriteLine("\n-- FetchXML -- ");  
            string fetchXmlQuery =  
                "<fetch mapping='logical' output-format='xml-platform' version='1.0' distinct='false'>" +  
                  "<entity name ='contact'>" +  
                    "<attribute name ='fullname' />" +  
                    "<attribute name ='jobtitle' />" +  
                    "<attribute name ='annualincome' />" +  
                    "<order descending ='true' attribute='fullname' />" +  
                    "<filter type ='and'>" +  
                      "<condition value ='%(sample)%' attribute='fullname' operator='like' />" +  
                    "</filter>" +  
                  "</entity>" +  
                "</fetch>";  
            //Must encode the FetchXML query because it's a part of the request (GET) string .  
            response = await SendCrmRequestAsync(HttpMethod.Get, "contacts?fetchXml=" +  
                WebUtility.UrlEncode(fetchXmlQuery), true);  
            if (response.StatusCode == HttpStatusCode.OK) //200  
            {  
                collection = JsonConvert.DeserializeObject<JObject>(response.Content.ReadAsStringAsync().Result);  
                DisplayFormattedEntities("Contacts Fetched by fullname containing '(sample)':",  
                    collection, contactProperties);  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
            #endregion FetchXML queries  
  
            #region Using predefined queries  
            //Use predefined queries of the following two types:  
            //  1) Saved query (system view)  
            //  2) User query (saved view)  
            //For more info, see: https://msdn.microsoft.com/en-us/library/mt607533.aspx  
  
            //1) Saved Query - retrieve "Active Accounts", run it, then display the results.  
            Console.WriteLine("\n-- Saved Query -- ");  
            filter = "&$filter=name eq 'Active Accounts'";  
            queryOptions = "?$select=name,savedqueryid" + filter;  
            //Retrieve the saved query GUID then execute it.  
            response = httpClient.GetAsync("savedqueries" + queryOptions).Result;  
            if (response.StatusCode == HttpStatusCode.OK) //200  
            {  
                JObject body = JsonConvert.DeserializeObject<JObject>  
                        (response.Content.ReadAsStringAsync().Result);  
                JObject activeAccount = (JObject)body["value"][0]; // Get the first matched.  
                string savedQueryId = activeAccount["savedqueryid"].ToString();  
                //Now execute the query and display the results.  
                response = await SendCrmRequestAsync(HttpMethod.Get, "accounts?savedQuery="+savedQueryId, true);  
                if (response.StatusCode == HttpStatusCode.OK) //200  
                {  
                    collection = JsonConvert.DeserializeObject<JObject>  
                            (response.Content.ReadAsStringAsync().Result);  
                    DisplayFormattedEntities("Saved query (Active Accounts):", collection, accountProperties);  
                }  
                else  
                { throw new CrmHttpResponseException(response.Content); }  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
  
            //2) Create a user query, then retrieve and execute it to display its results.  
            //For more info, see: https://msdn.microsoft.com/en-us/library/gg509053.aspx  
            Console.WriteLine("\n-- User Query -- ");  
  
            string userQueryRep = "{ " +  
              "\"name\": \"My User Query\", " +  
              "\"description\": \"User query to display contact info.\", " +  
              "\"querytype\": 0, " +  
              "\"returnedtypecode\": \"contact\", " +  
              "\"fetchxml\": " +  
              "\"<fetch mapping='logical' output-format='xml-platform' version='1.0' distinct='false'>" +  
                "<entity name ='contact'>" +  
                  "<attribute name ='fullname' />" +  
                  "<attribute name ='contactid' />" +  
                  "<attribute name ='jobtitle' />" +  
                  "<attribute name ='annualincome' />" +  
                  "<order descending ='false' attribute='fullname' />" +  
                  "<filter type ='and'>" +  
                    "<condition value ='%(sample)%' attribute='fullname' operator='like' />" +  
                    "<condition value ='%Manager%' attribute='jobtitle' operator='like' />" +  
                    "<condition value ='55000' attribute='annualincome' operator='gt' />" +  
                  "</filter>" +  
                "</entity>" +  
              "</fetch>\"" +  
              "}";  
  
            //Create the user query on server.  
            request = new HttpRequestMessage(HttpMethod.Post, "userqueries");  
            request.Content = new StringContent(userQueryRep, Encoding.UTF8, "application/json");  
            response = await httpClient.SendAsync(request);  
            if (response.StatusCode != HttpStatusCode.NoContent) //200  
            { throw new CrmHttpResponseException(response.Content); }  
  
            //Retrieve this new user query.  
            string userQueryId;  
            filter = "&$filter=name eq 'My User Query'";  
            queryOptions = "?$select=name,userqueryid," + filter;  
            response = await httpClient.GetAsync("userqueries" + queryOptions);  
            if (response.StatusCode == HttpStatusCode.OK) //200  
            {  
                JObject body = JsonConvert.DeserializeObject<JObject>  
                        (response.Content.ReadAsStringAsync().Result);  
                JObject userQuery = (JObject)body["value"][0]; //Use the first match.  
                userQueryId = userQuery["userqueryid"].ToString();  
                entityUris.Add(httpClient.BaseAddress + "/userqueries(" + userQueryId + ")");  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
  
            //Finally, execute retrieved query and display results.  
            response = await SendCrmRequestAsync(HttpMethod.Get, "contacts?userQuery=" + userQueryId, true);  
            if (response.StatusCode == HttpStatusCode.OK) //200  
            {  
                collection = JsonConvert.DeserializeObject<JObject>(response.Content.ReadAsStringAsync().Result);  
                DisplayFormattedEntities("Saved user query:", collection, contactProperties);  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
            #endregion Using predefined queries  
        }  
  
        /// <summary> Creates the CRM entity instances used by this sample. </summary>  
        /// <remarks> Using deep insert, this method creates the following set of related  
        ///  records in one request.  
        /// Accounts:   
        ///   account1 (Contoso Ltd)  
        ///      |--- primiarycontactid   
        ///         |----contact1 (Yvonne McKay)  
        ///      |--- Account_Tasks   
        ///         |--- task1, task2, task3 (3 tasks)  
        ///      |--- contact_customer_accounts   
        ///          |--- Contacts (9 contacts)  
        ///</remarks>  
        private void CreateRequiredRecords()  
        {  
            Console.WriteLine("Create sample data:");  
            //Create reusable JSON strings for various account and contact tasks.  
            string task1Json = @"{subject: 'Task 1', description: 'Task 1 description'}";  
            string task2Json = @"{subject: 'Task 2', description: 'Task 2 description'}";  
            string task3Json = @"{subject: 'Task 3', description: 'Task 3 description'}";  
            //Define the JSON representation for the account and related records    
            account1 = JObject.Parse(  
              "{ " +  
                "name: 'Contoso, Ltd. (sample)', " +  
                "primarycontactid: " +  
                "{ " +  
                    "firstname: 'Yvonne', lastname: 'McKay(sample)', jobtitle: 'Coffee Master'," +  
                        " annualincome: 45000, " +  
                    "Contact_Tasks: [" +  
                        task1Json + "," +  
                        task2Json + "," +  
                        task3Json + "]" +  
                "}, " +  
                "Account_Tasks: [" +  
                    task1Json + "," +  
                    task2Json + "," +  
                    task3Json + "]," +  
                "contact_customer_accounts: [ " +  
                "{" +  
                    "firstname: 'Susanna', lastname: 'Stubberod (sample)', jobtitle: 'Senior Purchaser'," +  
                        " annualincome: 52000, " +  
                    "Contact_Tasks: [" +  
                        task1Json + "," +  
                        task2Json + "," +  
                        task3Json + "]," +  
                "}, " +  
                "{" +  
                    "firstname: 'Nancy', lastname: 'Anderson (sample)', jobtitle: 'Activities Manager'," +  
                        " annualincome: 55500, " +  
                    "Contact_Tasks: [" +  
                        task1Json + "," +  
                        task2Json + "," +  
                        task3Json + "]," +  
                "}, " +  
                "{" +  
                    "firstname: 'Maria', lastname: 'Cambell (sample)', jobtitle: 'Accounts Manager'," +  
                        " annualincome: 31000, " +  
                    "Contact_Tasks: [" +  
                        task1Json + "," +  
                        task2Json + "," +  
                        task3Json + "]," +  
                "}, " +  
                "{" +  
                    "firstname: 'Nancy', lastname: 'Anderson (sample)', jobtitle: 'Logistics Specialist'," +  
                        " annualincome: 63500, " +  
                    "Contact_Tasks: [" +  
                        task1Json + "," +  
                        task2Json + "," +  
                        task3Json + "]," +  
                "}, " +  
                "{" +  
                    "firstname: 'Scott', lastname: 'Konersmann (sample)', jobtitle: 'Accounts Manager'," +  
                        " annualincome: 38000, " +  
                    "Contact_Tasks: [" +  
                        task1Json + "," +  
                        task2Json + "," +  
                        task3Json + "]," +  
                "}, " +  
                "{" +  
                    "firstname: 'Robert', lastname: 'Lyon (sample)', jobtitle: 'Senior Technician'," +   
                        " annualincome: 78000, " +  
                    "Contact_Tasks: [" +  
                        task1Json + "," +  
                        task2Json + "," +  
                        task3Json + "]," +  
                "}, " +  
                "{" +  
                    "firstname: 'Paul', lastname: 'Cannon (sample)', jobtitle: 'Ski Instructor'," +  
                        " annualincome: 68500, " +  
                    "Contact_Tasks: [" +  
                        task1Json + "," +  
                        task2Json + "," +  
                        task3Json + "]," +  
                "}, " +  
                "{" +  
                    "firstname: 'Rene', lastname: 'Valdes (sample)', jobtitle: 'Data Analyst III'," +  
                        " annualincome: 86000, " +  
                    "Contact_Tasks: [" +  
                        task1Json + "," +  
                        task2Json + "," +  
                        task3Json + "]," +  
                "}, " +  
                "{" +  
                    "firstname: 'Jim', lastname: 'Glynn (sample)', jobtitle: " +  
                        "'Senior International Sales Manager', annualincome: 81400, " +  
                    "Contact_Tasks: [" +  
                        task1Json + "," +  
                        task2Json + "," +  
                        task3Json + "]," +  
                "} ]" +  
              "}"  
            );  
            //Create account and related records with deep insert request  
            HttpResponseMessage response = SendAsJsonAsync(httpClient, HttpMethod.Post,  
                "accounts", account1).Result;  
            if (response.StatusCode == HttpStatusCode.NoContent)  
            {  
                account1Uri = response.Headers.GetValues("OData-EntityId").FirstOrDefault();  
                entityUris.Add(account1Uri);  
                Console.WriteLine("Account 'Contoso, Ltd. (sample)' created with 1 primary " +  
                    "contact and 9 associated contacts.");  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
  
            //Retrieve primary contact record and uri.  Most of the subsequent queries are   
            //performed using this contact.  
            string uri = account1Uri + "/primarycontactid/$ref";  //Retrieve the account URI only.  
            response = httpClient.GetAsync(uri).Result;  
            if (response.StatusCode == HttpStatusCode.OK) //200  
            {  
                JObject contactRef = JsonConvert.DeserializeObject<JObject>(  
                    response.Content.ReadAsStringAsync().Result);  
                contact1Uri = contactRef["@odata.id"].ToString();  
                entityUris.Add(contact1Uri);  
                Console.WriteLine("Has primary contact 'Yvonne McKay (sample)' with URI: {0}\n", contact1Uri);  
            }  
            else  
            { throw new CrmHttpResponseException(response.Content); }  
        }  
  
        static void Main(string[] args)  
        {  
            QueryData app = new QueryData();  
            Console.WriteLine("-- Sample started --");  
            try  
            {  
                //Read configuration file and connect to specified CRM server.  
                app.ConnectToCRM(args);  
                app.CreateRequiredRecords();  
                Task.WaitAll(Task.Run(async () => await app.RunAsync()));  
            }  
            catch (System.Exception ex)  
            { DisplayException(ex); }  
            finally  
            {  
                if (app.httpClient != null)  
                {  
                    app.DeleteRequiredRecords(true);  
                    app.httpClient.Dispose();  
                }  
                Console.WriteLine("Press <Enter> to exit the program.");  
                Console.ReadLine();  
            }  
        }  
  
        /// <summary>  
        /// Obtains the connection information from the application's configuration file,  
        /// then uses this info to connect to the specified CRM service.  
        /// </summary>  
        /// <param name="args">Command line arguments</param>  
        private void ConnectToCRM(String[] cmdargs)  
        {  
            //Create a helper object to read app.config for service URL and application   
            // registration settings.  
            Configuration config = null;  
            if (cmdargs.Length > 0)  
                config = new FileConfiguration(cmdargs[0]);  
            else  
                config = new FileConfiguration(null);  
            //Create a helper object to authenticate the user with this connection info.  
            Authentication auth = new Authentication(config);  
            //Next use a HttpClient object to connect to specified CRM Web service.  
            httpClient = new HttpClient(auth.ClientHandler, true);  
            //Define the Web API base address, the max period of execute time, the   
            // default OData version, and the default response payload format.  
            httpClient.BaseAddress = new Uri(config.ServiceUrl + "api/data/v8.1/");  
            httpClient.Timeout = new TimeSpan(0, 2, 0);  
            httpClient.DefaultRequestHeaders.Add("OData-MaxVersion", "4.0");  
            httpClient.DefaultRequestHeaders.Add("OData-Version", "4.0");  
            httpClient.DefaultRequestHeaders.Accept.Add(  
                new MediaTypeWithQualityHeaderValue("application/json"));  
        }  
  
        /// <summary> Deletes the CRM entity instance sample data created by this sample. </summary>  
        /// <param name="prompt">True to prompt the user for confirmation and display results;   
        ///   otherwise False to execute silently.</param>  
        /// <returns>Number of entity instances deleted</returns>  
        private int DeleteRequiredRecords(bool prompt)  
        {  
            if (entityUris.Count == 0) return 0;  
            if (prompt)  
            {  
                Console.Write("\nDo you want these sample entity records deleted? (y/n) [y]: ");  
                String answer = Console.ReadLine();  
                answer = answer.Trim();  
                if (!(answer.StartsWith("y") || answer.StartsWith("Y") ||  
                    answer == String.Empty))  
                { return 0; }  
            }  
            HttpResponseMessage response;  
            int successCnt = 0, failCnt = 0;  
            HttpContent lastBadResponseContent = null;  
            foreach (string ent in entityUris)  
            {  
                response = httpClient.DeleteAsync(ent).Result;  
                if (response.IsSuccessStatusCode) //200-299  
                { successCnt++; }  
                else if (response.StatusCode == HttpStatusCode.NotFound) //404  
                {; } //Entity may have been deleted by another user or via cascade delete.  
                else //Failed to delete  
                {  
                    failCnt++;  
                    lastBadResponseContent = response.Content;  
                }  
            }  
            entityUris.Clear();  
            if (failCnt > 0)  
            {  
                //Throw last failure.  
                throw new CrmHttpResponseException(lastBadResponseContent);  
            }  
            if (prompt)  
            { Console.WriteLine("Deleted {0} records!", successCnt); }  
            return successCnt;  
        }  
  
        ///<summary> Sends an HTTP request to the current CRM service. </summary>  
        ///<param name="method">The HTTP method to invoke</param>  
        ///<param name="query">The HTTP query to execute (base URL is provided by client)</param>  
        ///<param name="formatted">True to include formatted values in response; default is false.</param>  
        ///<param name="maxPageSize">Number of records to display per output "page".</param>  
        ///<returns>An HTTP response message</returns>  
        private async Task<HttpResponseMessage> SendCrmRequestAsync(  
                    HttpMethod method, string query, Boolean formatted=false, int maxPageSize=10)  
        {  
            HttpRequestMessage request = new HttpRequestMessage(method, query);  
            request.Headers.Add("Prefer", "odata.maxpagesize=" + maxPageSize.ToString());  
            if (formatted)  
                request.Headers.Add("Prefer",   
                    "odata.include-annotations=OData.Community.Display.V1.FormattedValue");  
            return await httpClient.SendAsync(request);  
        }  
  
        ///<summary> Sends an HTTP message containing a JSON payload to the target URL. </summary>  
        ///<typeparam name="T">Type of the data to send in the message content (payload)</typeparam>  
        ///<param name="client">A preconfigured HTTP client</param>  
        ///<param name="method">The HTTP method to invoke</param>  
        ///<param name="requestUri">The relative URL of the message request</param>  
        ///<param name="value">The data to send in the payload. The data will be converted to a   
        /// serialized JSON payload. </param>  
        ///<returns>An HTTP response message</returns>  
        private async Task<HttpResponseMessage> SendAsJsonAsync<T>(HttpClient client,  
            HttpMethod method, string requestUri, T value)  
        {  
            string content;  
            if (value.GetType().Name.Equals("JObject"))  
            { content = value.ToString(); }  
            else  
            {  
                content = JsonConvert.SerializeObject(value, new JsonSerializerSettings()  
                { DefaultValueHandling = DefaultValueHandling.Ignore });  
            }  
            HttpRequestMessage request = new HttpRequestMessage(method, requestUri);  
            request.Content = new StringContent(content);  
            request.Content.Headers.ContentType = MediaTypeHeaderValue.Parse("application/json");  
            return await client.SendAsync(request);  
        }  
  
        /// <summary> Displays formatted entity collections to the console. </summary>  
        /// <param name="label">Descriptive text output before collection contents </param>  
        /// <param name="collection"> JObject containing array of entities to output by property </param>  
        /// <param name="properties"> Array of properties within each entity to output. </param>  
        private void DisplayFormattedEntities(string label, JArray entities, string[] properties)  
        {  
            Console.Write(label);  
            int lineNum = 0;  
            foreach (JObject entity in entities)  
            {  
                lineNum++;  
                List<string> propsOutput = new List<string>();  
                //Iterate through each requested property and output either formatted value if one   
                //exists, otherwise output plain value.  
                foreach (string prop in properties)  
                {  
                    string propValue;  
                    string formattedProp = prop + "@OData.Community.Display.V1.FormattedValue";  
                    if (null != entity[formattedProp])  
                    { propValue = entity[formattedProp].ToString(); }  
                    else  
                    { propValue = entity[prop].ToString(); }  
                    propsOutput.Add(propValue);  
                }  
                Console.Write("\n\t{0}) {1}", lineNum, String.Join(", ", propsOutput));  
            }  
            Console.Write("\n");  
        }  
        ///<summary>Overloaded helper version of method that unpacks 'collection' parameter.</summary>  
        private void DisplayFormattedEntities(string label, JObject collection, string[] properties)  
        {  
            JToken valArray;  
            //Parameter collection contains an array of entities in 'value' member.  
            if (collection.TryGetValue("value", out valArray))  
            {  
                DisplayFormattedEntities(label, (JArray)valArray, properties);  
            }  
            //Otherwise it just represents a single entity.  
            else  
            {  
                JArray singleton = new JArray(collection);  
                DisplayFormattedEntities(label, singleton, properties);  
            }  
        }  
  
        /// <summary> Displays exception information to the console. </summary>  
        /// <param name="ex">The exception to output</param>  
        private static void DisplayException(Exception ex)  
        {  
            Console.WriteLine("The application terminated with an error.");  
            Console.WriteLine(ex.Message);  
            while (ex.InnerException != null)  
            {  
                Console.WriteLine("\t* {0}", ex.InnerException.Message);  
                ex = ex.InnerException;  
            }  
        }  
    }  
}  
  
```  
  
### See also 
 
[Use the Common Data Service for Apps Web API](overview.md)<br />
[Query Data using the Web API](query-data-web-api.md)<br />
[Web API Samples](web-api-samples.md)<br />
[Web API Query Data Sample](web-api-query-data-sample.md)<br />
[Web API Query Data Sample (Client-side JavaScript)](samples/query-data-client-side-javascript.md)<br />
[Web API Basic Operations Sample (C#)](samples/basic-operations-csharp.md)<br />
[Web API Conditional Operations Sample (C#)](samples/conditional-operations-csharp.md)<br />
[Web API Functions and Actions Sample (C#)](samples/functions-actions-csharp.md)
