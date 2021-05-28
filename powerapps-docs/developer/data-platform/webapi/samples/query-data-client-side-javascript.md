---
title: "Web API Query Data Sample (Client-side JavaScript) | Microsoft Docs"
ms.custom: ""
ms.date: 10/31/2018
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 6df7cccb-071d-4853-8acb-01bceef973ca
caps.latest.revision: 22
author: "JimDaly" # GitHub ID
ms.author: "jdaly"
ms.reviewer: "pehecke"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Web API Query Data Sample (Client-side JavaScript)

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample demonstrates how to perform basic query requests using the Microsoft Dataverse Web API using client-side JavaScript  
  
> [!NOTE]
>  This sample implements the operations detailed in the [Web API Query Data Sample](../web-api-query-data-sample.md) and uses the common  client-side JavaScript constructs described in [Web API Samples (Client-side JavaScript)](../web-api-samples-client-side-javascript.md)  
  
<a name="bkmk_prereq"></a>

## Prerequisites

 To run this sample, the following is required:  
  
- Access to Dataverse environment.  
  
- A user account with privileges to import solutions and perform CRUD operations, typically a system administrator or system customizer security role.  
  
<a name="bkmk_runsample"></a>

## Run this sample

To run this sample, go to  [Microsoft CRM Web API Query Data Sample (Client-side JavaScript)](/samples/browse/) and download the sample archive file: Microsoft CRM Web API Query Data Sample (Client-side JavaScript).zip. Extract the contents of the sample archieve and locate the WebAPIQueryData_1_0_0_0_managed.zip managed solution file. Import the managed solution into your Dataverse organization and run the sample. For instructions on how to import the sample solution, see [Web API Samples (Client-side JavaScript)](../web-api-samples-client-side-javascript.md).  
  
<a name="bkmk_codeSample"></a>

## Code sample

 This sample includes two web resources:  
  
- [WebAPIQuery.html](#bkmk_WebAPIQuery)  
  
- [WebAPIQuery.js](#bkmk_WebAPIQueryJS)  
  
<a name="bkmk_WebAPIQuery"></a>
  
### WebAPIQuery.html  

 The WebAPIQuery.html web resource provides the context in which the JavaScript code will run.  
  
```html  
<!DOCTYPE html>  
<html>  
<head>  
    <title>Microsoft CRM Web API Query Example</title>  
    <meta charset="utf-8" />  
    <script src="../ClientGlobalContext.js.aspx" type="text/javascript"></script>  
    <script src="scripts/es6promise.js"></script>  
    <script src="scripts/WebAPIQuery.js"></script>  
  
    <style type="text/css">  
        body {  
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;  
        }  
  
        #preferences {  
            border: inset;  
            padding: 10px 10px;  
        }  
  
        #output_area {  
            border: inset;  
            background-color: gainsboro;  
            padding: 10px 10px;  
        }  
    </style>  
</head>  
<body>  
    <h1>Microsoft CRM Web API Query Example</h1>  
    <p>This page demonstrates the CRM Web API's Query operations using JavaScript.</p>  
  
    <h2>Instructions</h2>  
    <p>Choose your preferences and run the JavaScript code.   
    Use your browser's developer tools to view the output written to the console (e.g.: in IE 11 or Microsoft Edge,   
    press F12 to load the Developer Tools).</p>  
    <form id="preferences">  
        <p>  
            Remove sample data (Choose whether you want to delete sample data created during this execution):  
            <br />  
            <input name="removesampledata" type="radio" value="yes" checked /> Yes  
            <input name="removesampledata" type="radio" value="no" /> No  
        </p>  
        <input type="button" name="start_samples" value="Start Sample" onclick="Sdk.startSample()" />  
    </form>  
  
</body>  
</html>
```  
  
<a name="bkmk_WebAPIQueryJS"></a>
 
### WebAPIQuery.js

The WebAPIQuery.js web resource is the JavaScript library that defines the operations this sample performs.  
  
```javascript  
"use strict";  
var Sdk = window.Sdk || {};  
/**  
 * @function getClientUrl   
 * @description Get the client URL.  
 * @returns {string} The client URL.  
 */  
Sdk.getClientUrl = function () {  
    var context;  
    // GetGlobalContext defined by including reference to   
    // ClientGlobalContext.js.aspx in the HTML page.  
    if (typeof GetGlobalContext != "undefined")  
    { context = GetGlobalContext(); }  
    else  
    {  
        if (typeof Xrm != "undefined") {  
            // Xrm.Page.context defined within the Xrm.Page object model for form scripts.  
            context = Xrm.Page.context;  
        }  
        else { throw new Error("Context is not available."); }  
    }  
    return context.getClientUrl();  
}  
  
// Global variables.  
var entitiesToDelete = [];              // Entity URIs to be deleted (if user chooses to delete sample data)  
var deleteData = true;                  // Delete data by default unless user chooses not to delete.  
var clientUrl = Sdk.getClientUrl();     // e.g.: https://org.crm.dynamics.com  
var webAPIPath = "/api/data/v8.1";      // Path to the web API.  
var account1Uri;                        // e.g.: Contoso Inc (sample)  
var contact1Uri;                        // e.g.: Yvonne McKey (sample)  
var page2Uri;                           // URI of next page in pagination sample.  
  
// Entity properties to select in a request.  
var contactProperties = ["fullname", "jobtitle", "annualincome"];  
var accountProperties = ["name"];  
var taskProperties = ["subject", "description"];  
  
/**  
 * @function request  
 * @description Generic helper function to handle basic XMLHttpRequest calls.  
 * @param {string} action - The request action. String is case-sensitive.  
 * @param {string} uri - An absolute or relative URI. Relative URI starts with a "/".  
 * @param {object} data - An object representing an entity. Required for create and update action.  
 * @param {boolean} formattedValue - If "true" then include formatted value; "false" otherwise.  
 *    For more info on formatted value, see:  
 *    https://msdn.microsoft.com/library/gg334767.aspx#bkmk_includeFormattedValues  
 * @param {number} maxPageSize - Indicate the page size. Default is 10 if not defined.  
 * @returns {Promise} - A Promise that returns either the request object or an error object.  
 */  
Sdk.request = function (action, uri, data, formattedValue, maxPageSize) {  
    if (!RegExp(action, "g").test("POST PATCH PUT GET DELETE")) { // Expected action verbs.  
        throw new Error("Sdk.request: action parameter must be one of the following: " +  
            "POST, PATCH, PUT, GET, or DELETE.");  
    }  
    if (!typeof uri === "string") {  
        throw new Error("Sdk.request: uri parameter must be a string.");  
    }  
    if ((RegExp(action, "g").test("POST PATCH PUT")) && (data === null || data === undefined)) {  
        throw new Error("Sdk.request: data parameter must not be null for operations that create or modify data.");  
    }  
    if (maxPageSize === null || maxPageSize === undefined) {  
        maxPageSize = 10; // Default limit is 10 entities per page.  
    }  
  
    // Construct a fully qualified URI if a relative URI is passed in.  
    if (uri.charAt(0) === "/") {  
        uri = clientUrl + webAPIPath + uri;  
    }  
  
    return new Promise(function (resolve, reject) {  
        var request = new XMLHttpRequest();   
        request.open(action, encodeURI(uri), true);  
        request.setRequestHeader("OData-MaxVersion", "4.0");  
        request.setRequestHeader("OData-Version", "4.0");  
        request.setRequestHeader("Accept", "application/json");  
        request.setRequestHeader("Content-Type", "application/json; charset=utf-8");  
        request.setRequestHeader("Prefer", "odata.maxpagesize=" + maxPageSize);  
        if (formattedValue) {  
            request.setRequestHeader("Prefer",  
                "odata.include-annotations=OData.Community.Display.V1.FormattedValue");  
        }  
        request.onreadystatechange = function () {  
            if (this.readyState === 4) {  
                request.onreadystatechange = null;  
                switch (this.status) {  
                    case 200: // Success with content returned in response body.  
                    case 204: // Success with no content returned in response body.  
                        resolve(this);  
                        break;  
                    default: // All other statuses are unexpected so are treated like errors.  
                        var error;  
                        try {  
                            error = JSON.parse(request.response).error;  
                        } catch (e) {  
                            error = new Error("Unexpected Error");  
                        }  
                        reject(error);  
                        break;  
                }  
            }  
        };  
        request.send(JSON.stringify(data));  
    });  
};  
  
/**  
 * @funnction output  
 * @description Generic helper function to output data to console.  
 * @param {array} collection - Array of entities.  
 * @param {string} label - Text label for what the collection contains.  
 * @param {array} properties - Array of properties appropriate for the collection.  
 */  
Sdk.output = function (collection, label, properties) {  
    console.log(label);  
    collection.forEach(function (row, i) {  
        var prop = [];  
        properties.forEach(function (p) {  
            var f = p + "@OData.Community.Display.V1.FormattedValue";  
            prop.push((row[f] ? row[f] : row[p])); // Get formatted value if one exists for this property.  
        })  
        console.log("\t%s) %s", i + 1, prop.join(", "));  
    });  
}  
  
/**  
 * @function startSample  
 * @description Runs the sample.   
 * This sample demonstrates basic query operations.   
 * Results are sent to the debugger's console window.  
 */  
Sdk.startSample = function () {  
    // Initializing...  
    deleteData = document.getElementsByName("removesampledata")[0].checked;  
    entitiesToDelete = []; //Reset the array.  
    account1Uri = "";  
    contact1Uri = "";  
    page2Uri = "";  
  
    console.log("-- Sample started --");  
    console.log("Create sample data:");  
    // Add some data to the CRM server so we can query against it.  
    // Using Deep Insert, we create all the sample data in one request.  
    // Data structure:  
    //   Accounts  
    //      |--- primarycontactid  
    //          |--- Contact_Tasks (3 tasks)  
    //      |--- Account_Tasks (3 tasks)  
    //      |--- contact_customer_accounts (9 child contacts, each with 3 tasks)  
    //          |--- Contacts  
    //              |--- Contact_Tasks  
    //  
    var sampleData = {  
        "name": "Contoso, Ltd. (sample)",  
        "primarycontactid": {  
            "firstname": "Yvonne", "lastname": "McKay (sample)", "jobtitle": "Coffee Master",  
            "annualincome": 45000, "Contact_Tasks": [  
            { "subject": "Task 1", "description": "Task 1 description" },  
            { "subject": "Task 2", "description": "Task 2 description" },  
            { "subject": "Task 3", "description": "Task 3 description" }  
            ]  
        }, "Account_Tasks": [  
        { "subject": "Task 1", "description": "Task 1 description" },  
        { "subject": "Task 2", "description": "Task 2 description" },  
        { "subject": "Task 3", "description": "Task 3 description" }  
        ],  
        "contact_customer_accounts": [  
            {  
                "firstname": "Susanna", "lastname": "Stubberod (sample)", "jobtitle": "Senior Purchaser",  
                "annualincome": 52000, "Contact_Tasks": [  
            { "subject": "Task 1", "description": "Task 1 description" },  
            { "subject": "Task 2", "description": "Task 2 description" },  
            { "subject": "Task 3", "description": "Task 3 description" }  
                ]  
            },  
            {  
                "firstname": "Nancy", "lastname": "Anderson (sample)", "jobtitle": "Activities Manager",  
                "annualincome": 55500, "Contact_Tasks": [  
                { "subject": "Task 1", "description": "Task 1 description" },  
                { "subject": "Task 2", "description": "Task 2 description" },  
                { "subject": "Task 3", "description": "Task 3 description" }  
                ]  
            },  
            {  
                "firstname": "Maria", "lastname": "Cambell (sample)", "jobtitle": "Accounts Manager",  
                "annualincome": 31000, "Contact_Tasks": [  
                { "subject": "Task 1", "description": "Task 1 description" },  
                { "subject": "Task 2", "description": "Task 2 description" },  
                { "subject": "Task 3", "description": "Task 3 description" }  
                ]  
            },  
            {  
                "firstname": "Nancy", "lastname": "Anderson (sample)", "jobtitle": "Logistics Specialist",  
                "annualincome": 63500, "Contact_Tasks": [  
                { "subject": "Task 1", "description": "Task 1 description" },  
                { "subject": "Task 2", "description": "Task 2 description" },  
                { "subject": "Task 3", "description": "Task 3 description" }  
                ]  
            },  
            {  
                "firstname": "Scott", "lastname": "Konersmann (sample)", "jobtitle": "Accounts Manager",  
                "annualincome": 38000, "Contact_Tasks": [  
                { "subject": "Task 1", "description": "Task 1 description" },  
                { "subject": "Task 2", "description": "Task 2 description" },  
                { "subject": "Task 3", "description": "Task 3 description" }  
                ]  
            },  
            {  
                "firstname": "Robert", "lastname": "Lyon (sample)", "jobtitle": "Senior Technician",  
                "annualincome": 78000, "Contact_Tasks": [  
                { "subject": "Task 1", "description": "Task 1 description" },  
                { "subject": "Task 2", "description": "Task 2 description" },  
                { "subject": "Task 3", "description": "Task 3 description" }  
                ]  
            },  
            {  
                "firstname": "Paul", "lastname": "Cannon (sample)", "jobtitle": "Ski Instructor",  
                "annualincome": 68500, "Contact_Tasks": [  
                { "subject": "Task 1", "description": "Task 1 description" },  
                { "subject": "Task 2", "description": "Task 2 description" },  
                { "subject": "Task 3", "description": "Task 3 description" }  
                ]  
            },  
            {  
                "firstname": "Rene", "lastname": "Valdes (sample)", "jobtitle": "Data Analyst III",  
                "annualincome": 86000, "Contact_Tasks": [  
                { "subject": "Task 1", "description": "Task 1 description" },  
                { "subject": "Task 2", "description": "Task 2 description" },  
                { "subject": "Task 3", "description": "Task 3 description" }  
                ]  
            },  
            {  
                "firstname": "Jim", "lastname": "Glynn (sample)", "jobtitle": "Senior International Sales Manager",  
                "annualincome": 81400, "Contact_Tasks": [  
                { "subject": "Task 1", "description": "Task 1 description" },  
                { "subject": "Task 2", "description": "Task 2 description" },  
                { "subject": "Task 3", "description": "Task 3 description" }  
                ]  
            }  
        ]  
    };  
  
    var uri = "/accounts"; // A relative URI to the account entity.  
    Sdk.request("POST", uri, sampleData) // Adding sample data so we can query against it.  
    .then(function (request) {  
        // Process request.  
        account1Uri = request.getResponseHeader("OData-EntityId");  
        entitiesToDelete.push(account1Uri); // To delete later.  
        console.log("Account 'Contoso, Ltd. (sample)' created with 1 primary contact and 9 associated contacts.");  
  
        // Get primary contact info.  
        // Most queries are done using this contact.  
        var uri = account1Uri + "/primarycontactid/$ref"; // Request for the URI only.  
        return Sdk.request("GET", uri);  
    })  
    .then(function (request) {  
        contact1Uri = JSON.parse(request.response)["@odata.id"];  
        entitiesToDelete.push(contact1Uri); // To delete later.  
        console.log("Has primary contact 'Yvonne McKay (sample)' with URI: %s\n", contact1Uri);  
  
        // Basic query:  
        // Query using $select option against a contact entity to get the properties you want.  
        // For performance best practice, always use $select otherwise all properties are returned.  
        console.log("-- Basic Query --");  
        var query = "?$select=" + contactProperties.join(); // Array defined in the global scope.  
        return Sdk.request("GET", contact1Uri + query, null, true);  
    })  
    .then(function (request) {  
        var contact1 = JSON.parse(request.response);  
        console.log("Contact basic info:\n\tFullname: '%s'\n\tJobtitle: '%s'\n\tAnnualincome: '%s' (unformatted)",  
            contact1.fullname, contact1.jobtitle, contact1.annualincome);  
        console.log("\tAnnualincome: %s (formatted)\n",  
            contact1["annualincome@OData.Community.Display.V1.FormattedValue"]);  
  
        // Filter criteria:  
        // Applying filters to get targeted data.  
        // 1) Using standard query functions (e.g.: contains, endswith, startswith)  
        // 2) Using CRM query functions (e.g.: LastXhours, Last7Days, Today, Between, In, ...)  
        // 3) Using filter operators and logical operators (e.g.: eq, ne, gt, and, or, etc…)  
        // 4) Set precedence using parenthesis (e.g.: ((criteria1) and (criteria2)) or (criteria3)  
        // For more info, see: https://msdn.microsoft.com/library/gg334767.aspx#bkmk_filter  
        console.log("-- Filter Criteria --");  
  
        // Filter 1: Using standard query functions to filter results.  
        // In this operation, we will query for all contacts with fullname containing the string "(sample)".  
        var filter = "&$filter=contains(fullname,'(sample)')";  
        var query = "?$select=" + contactProperties.join() + filter;  
        return Sdk.request("GET", "/contacts" + query, null, true);  
    })  
    .then(function (request) {  
        var collection = JSON.parse(request.response).value;  
        Sdk.output(collection, "Contacts filtered by fullname containing '(sample)':", contactProperties);  
  
        // Filter 2: Using CRM query functions to filter results.  
        // In this operation, we will query for all contacts that was created in the last hour.   
        // For complete list of CRM query functions, see:  
        // https://msdn.microsoft.com/library/mt607843.aspx  
        var filter = "&$filter=Microsoft.Dynamics.CRM.LastXHours(PropertyName='createdon',PropertyValue='1')";  
        var query = "?$select=" + contactProperties.join() + filter;  
        return Sdk.request("GET", "/contacts" + query, null, true); // Remember page size limit is set to 10.  
    })  
    .then(function(request){  
        var collection = JSON.parse(request.response).value;  
        Sdk.output(collection, "Contacts that were created within the last 1hr:", contactProperties);  
  
        // Filter 3: Using operators  
        // Building on the previous operation, we will further limit the results by the contact's income.  
        // For more info on standard filter operators, see:  
        // https://msdn.microsoft.com/library/gg334767.aspx#bkmk_filter  
        var filter = "&$filter=contains(fullname,'(sample)') and annualincome gt 55000";  
        var query = "?$select=" + contactProperties.join() + filter;  
        return Sdk.request("GET", "/contacts" + query, null, true);  
    })  
    .then(function (request) {  
        var collection = JSON.parse(request.response).value;  
        Sdk.output(collection, "Contacts filtered by fullname and annualincome (<$55,000):", contactProperties);  
  
        // Filter 4: Set precedence using parenthesis.  
        // Continue building on the previous operation, we will further limit results by job title.  
        // Parenthesis and the order of filter statements can impact results returned.  
        var filter = "&$filter=contains(fullname,'(sample)') " +  
            "and (contains(jobtitle,'senior') or contains(jobtitle,'specialist')) and annualincome gt 55000";  
        var query = "?$select=" + contactProperties.join() + filter;  
        return Sdk.request("GET", "/contacts" + query, null, true);  
    })  
    .then(function (request) {  
        var collection = JSON.parse(request.response).value;  
        Sdk.output(collection, "Contacts filtered by fullname, annualincome and jobtitle (Senior or Specialist):",  
            contactProperties);  
  
        // Order results:  
        // Filtered results can be order in descending or ascending order.  
        console.log("\n-- Order Results --");  
        var filter = "&$filter=contains(fullname,'(sample)') " +  
            "&$orderby=jobtitle asc, annualincome desc";  
        var query = "?$select=" + contactProperties.join() + filter;  
        return Sdk.request("GET", "/contacts" + query, null, true);  
    })  
    .then(function (request) {  
        var collection = JSON.parse(request.response).value;  
        Sdk.output(collection, "Contacts ordered by jobtitle (Ascending) and annualincome (descending):",  
            contactProperties);  
  
        // Parameterized Aliases.  
        // Aliases can be used as parameters in a query. These parameters can be used in $filter and $orderby options.  
        // Using the previous operation as basis, parameterizing the query will give us the same results.  
        // For more info, see: https://msdn.microsoft.com/library/gg309638.aspx#bkmk_passParametersToFunctions  
        console.log("\n-- Parameterized Aliases --");  
        var filter = "&$filter=contains(@p1,'(sample)') " +  
            "&$orderby=@p2 asc, @p3 desc&@p1=fullname&@p2=jobtitle&@p3=annualincome";  
        var query = "?$select=" + contactProperties.join() + filter;  
        return Sdk.request("GET", "/contacts" + query, null, true);  
    })  
    .then(function (request) {  
        var collection = JSON.parse(request.response).value;  
        Sdk.output(collection, "Contacts list using parameterized aliases:", contactProperties);  
  
        // Limit records returned.  
        // To further limit the records returned, use the $top query option.  
        // Specifying a limit number for $top will return at most that number of results per request.  
        // Extra results are ignored.  
        console.log("\n-- Top Results --");  
        var filter = "&$filter=contains(fullname,'(sample)')&$top=5";  
        var query = "?$select=" + contactProperties.join() + filter;  
        return Sdk.request("GET", "/contacts" + query, null, true);  
    })  
    .then(function (request) {  
        var collection = JSON.parse(request.response).value;  
        Sdk.output(collection, "Contacts top 5 results:", contactProperties);  
  
        // Result count.  
        // Count the number of results matching the filter criteria.  
        // 1) Get a count of a collection without the data.  
        // 2) Get a count along with the data.  
        // HINT: Use count together with the "odata.maxpagesize" to calculate the number of pages in the query.  
        // NOTE: CRM has a max record limit of 5000 records per response.  
        console.log("\n-- Result Count --");  
        return Sdk.request("GET", "/contacts/$count"); // Count is returned in response body.  
    })  
    .then(function (request) {  
        console.log("The contacts collection has %s contacts.", request.response); // Count maximum is 5000.  
  
        // 2) Get filtered result with a count  
        var filter = "&$filter=contains(jobtitle,'senior') or contains(jobtitle, 'manager')&$count=true";  
        var query = "?$select=" + contactProperties.join() + filter;  
        return Sdk.request("GET", "/contacts" + query, null, true);  
    })  
    .then(function (request) {  
        var count = JSON.parse(request.response)["@odata.count"];  
        console.log("%s contacts have either 'Manager' or 'Senior' designation in their jobtitle.", count);  
        var collection = JSON.parse(request.response).value;  
        Sdk.output(collection, "Manager or Senior:", contactProperties);  
  
        // Pagination:  
        // For large data sets, you can limit the number of records returned per page.  
        // Then offer a "next page" and "previous page" links for users to browse through all the data.  
        // NOTE: This is why you should not use $top with maxpagesize. $top will limit results returned   
        //       preventing you from accessing all possible results in the query.   
        //       For example: If your query has 10 entities in the result and you limit your result to $top=5  
        //       then, you can't get to the remaining 5 results; but with "maxpagesize" (without $top), you can.  
        // HINT: Save the URI of the current page so users can go "next" and "previous".  
        console.log("\n-- Pagination --");  
        var filter = "&$filter=contains(fullname,'(sample)')&$count=true";  
        var query = "?$select=" + contactProperties.join() + filter;  
        return Sdk.request("GET", "/contacts" + query, null, true, 4); // 4 records per page.  
    })  
    .then(function (request) {  
        var count = JSON.parse(request.response)["@odata.count"];  
        var maxpages = Math.ceil(count / 4);  
        console.log("Contacts total: %s \tContacts per page: %s.\tOutputting first 2 pages.", count, 4);  
        var collection = JSON.parse(request.response).value;  
        Sdk.output(collection, "Page 1 of " + maxpages + ":", contactProperties);  
  
        // Getting the next page.  
        page2Uri = JSON.parse(request.response)["@odata.nextLink"]; // This URI is already encoded.  
        return Sdk.request("GET", decodeURI(page2Uri), null, true, 4); // URI re-encoded in the request function.  
    })  
    .then(function (request) {  
        var count = JSON.parse(request.response)["@odata.count"];  
        var maxpages = Math.ceil(count / 4);  
        var collection = JSON.parse(request.response).value;  
        Sdk.output(collection, "Page 2 of " + maxpages + ":", contactProperties);  
  
        // Using expand option to retrieve additional information.  
        // It is common for entities to  have associations with other entities in the system and you might want   
        // to also retrieve this information in the same request. To retrieve information on associated entities,   
        // use the $expand query option on navigation properties.   
        // 1) Expand using single-valued navigation properties (e.g.: via the 'primarycontactid')  
        // 2) Expand using partner property (e.g.: from contact to account via the 'account_primary_contact')  
        // 3) Expand using collection-valued navigation properties (e.g.: via the 'contact_customer_accounts')  
        // 4) Expand using multiple navigation property types in a single request.  
        // NOTE: Expansions can only go 1 level deep.  
        //   For performance best practice, always use $select statement in an expand option.  
        console.log("\n-- Expanding Results --");  
  
        // 1) Expand using single-valued navigation properties (e.g.: via the 'primarycontactid')  
        var expand = "&$expand=primarycontactid($select=" + contactProperties.join() + ")";  
        var query = "?$select=" + accountProperties.join() + expand;  
        return Sdk.request("GET", account1Uri + query, null, true);  
    })  
    .then(function (request) {  
        var account = JSON.parse(request.response);  
        var str = "Account '%s' has the following primary contact person:\n\t" +  
            "Fullname: '%s' \n\tJobtitle: '%s' \n\tAnnualincome: '%s'";  
        console.log(str, account.name,  
            account.primarycontactid.fullname,  
            account.primarycontactid.jobtitle,  
            account.primarycontactid.annualincome);  
  
        // 2) Expand using partner property (e.g.: from contact to account via the 'account_primary_contact')  
        var expand = "&$expand=account_primary_contact($select=" + accountProperties.join() + ")";  
        var query = "?$select=" + contactProperties.join() + expand;  
        return Sdk.request("GET", contact1Uri + query, null, true);  
    })  
    .then(function (request) {  
        var contact = JSON.parse(request.response);  
        var label = "Contact '" + contact.fullname + "' is the primary contact for the following accounts:";  
        Sdk.output(contact.account_primary_contact, label, accountProperties);  
  
        // 3) Expand using collection-valued navigation properties (e.g.: via the 'contact_customer_accounts')  
        var expand = "&$expand=contact_customer_accounts($select=" + contactProperties.join() + ")"  
        var query = "?$select=" + accountProperties.join() + expand;  
        return Sdk.request("GET", account1Uri + query, null, true);  
    })  
    .then(function (request) {  
        var account = JSON.parse(request.response);  
        var label = "Account '" + account.name + "' has the following contact customers:";  
        var collection = account.contact_customer_accounts;  
        Sdk.output(collection, label, contactProperties);  
  
        // 4) Expand using multiple navigation property types in a single request.  
        //    For example: expanding on primiarycontactid, contact_customer_accounts, and Account_Tasks.  
        console.log("\n-- Expanding multiple property types in one request -- ");  
        var expand = "&$expand=primarycontactid($select=" + contactProperties.join() + ")," +  
            "contact_customer_accounts($select=" + contactProperties.join() + ")," +  
            "Account_Tasks($select=" + taskProperties.join() + ")";  
        var query = "?$select=" + accountProperties.join() + expand;  
        return Sdk.request("GET", account1Uri + query, null, true);  
    })  
    .then(function (request) {  
        var account = JSON.parse(request.response);  
        var label = "Account '%s' has the following primary contact person:\n\t" +  
            "Fullname: '%s' \n\tJobtitle: '%s' \n\tAnnualincome: '%s'";  
        console.log(label, account.name,  
            account.primarycontactid.fullname,  
            account.primarycontactid.jobtitle,  
            account.primarycontactid.annualincome);  
  
        // Handling each collection separately.  
        label = "Account '" + account.name + "' has the following related contacts:";  
        var collection = account.contact_customer_accounts;  
        Sdk.output(collection, label, contactProperties);  
  
        label = "Account '" + account.name + "' has the following tasks:";  
        collection = account.Account_Tasks;  
        Sdk.output(collection, label, taskProperties);  
  
        // FetchXML  
        // Using FetchXML to query for all contacts whose fullname contains '(sample)'.  
        // NOTE: XML string must be URI encoded.  
        // For more information, see: https://msdn.microsoft.com/library/gg328117.aspx  
        console.log("\n-- FetchXML -- ");  
        var fetchXML = "<fetch mapping=\"logical\" output-format=\"xml-platform\" version=\"1.0\" distinct=\"false\"> \  
  <entity name=\"contact\"> \  
    <attribute name=\"fullname\" /> \  
    <attribute name=\"jobtitle\" /> \  
    <attribute name=\"annualincome\" /> \  
    <order descending=\"true\" attribute=\"fullname\" /> \  
    <filter type=\"and\"> \  
      <condition value=\"%(sample)%\" attribute=\"fullname\" operator=\"like\" /> \  
    </filter> \  
  </entity> \  
</fetch> ";  
        return Sdk.request("GET", "/contacts?fetchXml=" + encodeURIComponent(fetchXML), null, true);  
    })  
    .then(function(request){  
        var collection = JSON.parse(request.response).value;  
        Sdk.output(collection, "Contacts Fetched by fullname containing '(sample)':", contactProperties);  
  
        // FetchXML pagination.   
        // Noticed the attribute "page=3" and "count=4" in this XML.   
        // We want to retrieve entities in page 3 but limit results to only 4 entities.  
        // If the result return zero records for the page, that means we have reached the end of the result set.  
        // For more info, see: https://msdn.microsoft.com/library/mt607533.aspx#bkmk_useFetchXML  
        var fetchXML = "<fetch mapping=\"logical\" output-format=\"xml-platform\" version=\"1.0\" \  
distinct=\"false\" page=\"3\" count=\"4\"> \  
  <entity name=\"contact\"> \  
    <attribute name=\"fullname\" /> \  
    <attribute name=\"jobtitle\" /> \  
    <attribute name=\"annualincome\" /> \  
    <order descending=\"true\" attribute=\"fullname\" /> \  
    <filter type=\"and\"> \  
      <condition value=\"%(sample)%\" attribute=\"fullname\" operator=\"like\" /> \  
    </filter> \  
  </entity> \  
</fetch> ";  
        return Sdk.request("GET", "/contacts?fetchXml=" + encodeURIComponent(fetchXML), null, true);  
    })  
    .then(function(request){  
        var collection = JSON.parse(request.response).value;  
        if (collection.length == 0) {  
            console.log("There are no records on this page."); // We have reached the end of our query result set.  
        } else {  
            Sdk.output(collection, "Contacts Fetched by fullname containing '(sample)' - Page 3:", contactProperties);  
        }  
  
        // Using predefined queries.  
        // 1) Saved query  
        // 2) User query  
        // For more info, see:   
        // https://msdn.microsoft.com/library/mt607533.aspx  
  
        // Saved Query  
        // Get the Saved Query "Active Accounts" and display results to output.  
        console.log("\n-- Saved Query -- ");  
        var filter = "&$filter=name eq 'Active Accounts'";  
        var query = "?$select=name,savedqueryid" + filter;  
        return Sdk.request("GET", "/savedqueries" + query, null, true); // Requesting for saved query GUID.  
    })  
    .then(function(request){  
        // Get the savedqueryid GUID and then use it to request for the entities in that query.  
        var activeAccount = JSON.parse(request.response).value[0]; // Get the first matched.  
        var savedqueryid = activeAccount.savedqueryid;  
  
        // Request for the saved query results  
        return Sdk.request("GET", "/accounts?savedQuery=" + savedqueryid, null, true);  
    })  
    .then (function (request){  
        var collection = JSON.parse(request.response).value;  
        Sdk.output(collection, "Saved Query (Active Accounts):", accountProperties);  
  
        // User Query  
        // Create a user query then get it from the server and execute that query for results.  
        // For more info, see: https://msdn.microsoft.com/library/gg509053.aspx  
        console.log("\n-- User Query -- ");  
        var userquery = {  
            "name": "My User Query",  
            "description": "User query to display contact info.",  
            "querytype": 0,  
            "returnedtypecode": "contact",  
            "fetchxml": "<fetch mapping=\"logical\" output-format=\"xml-platform\" version=\"1.0\" distinct=\"false\"> \  
  <entity name=\"contact\"> \  
    <attribute name=\"fullname\" /> \  
    <attribute name=\"contactid\" /> \  
    <attribute name=\"jobtitle\" /> \  
    <attribute name=\"annualincome\" /> \  
    <order descending=\"false\" attribute=\"fullname\" /> \  
    <filter type=\"and\"> \  
      <condition value=\"%(sample)%\" attribute=\"fullname\" operator=\"like\" /> \  
      <condition value=\"%Manager%\" attribute=\"jobtitle\" operator=\"like\" /> \  
      <condition value=\"55000\" attribute=\"annualincome\" operator=\"gt\" /> \  
    </filter> \  
  </entity> \  
</fetch> "  
        };  
  
        return Sdk.request("POST", "/userqueries", userquery, true); // Create the user query.  
    })  
    .then(function (request){  
        // Look up the user query we just created  
        // then use it to request for the entities in that query.  
        var filter = "&$filter=name eq 'My User Query'";  
        var query = "?$select=name,userqueryid," + filter;  
        return Sdk.request("GET", "/userqueries" + query, null, true);  
    })  
    .then(function (request) {  
        var userQuery = JSON.parse(request.response).value[0]; // Get the first matched.  
        var userqueryid = userQuery.userqueryid;  
        entitiesToDelete.push(clientUrl + webAPIPath + "/userqueries(" + userqueryid + ")");  
  
        // Request for the user query results  
        return Sdk.request("GET", "/contacts?userQuery=" + userqueryid, null, true);  
    })  
    .then(function (request) {  
        var collection = JSON.parse(request.response).value;  
        Sdk.output(collection, "Saved User Query:", contactProperties);  
  
        // House cleaning - deleting sample data  
        // For more info on cascading delete, see:   
        // https://msdn.microsoft.com/library/gg309412.aspx#BKMK_CascadingBehavior  
        console.log("\n-- Deleting Sample Data --");  
        if (deleteData) {  
            for (var i = 0; i < entitiesToDelete.length; i++) {  
                console.log("Deleting entity: " + entitiesToDelete[i]);  
                Sdk.request("DELETE", entitiesToDelete[i], null)  
                .catch(function (err) {  
                    console.log("ERROR: Delete failed --Reason: \n\t" + err.message);  
                });  
            }  
        } else {  
            console.log("Sample data not deleted.");  
        }  
    })  
    .catch(function (error) {  
        console.log(error.message);  
    });  
  
}  
```  
  
### See also

[Use the Dataverse Web API](../overview.md)<br />
[Query Data using the Web API](../query-data-web-api.md)<br />
[Web API Samples](../web-api-samples.md)<br />
[Web API Query Data Sample](../web-api-query-data-sample.md)<br />
[Web API Query Data Sample (C#)](cdswebapiservice-query-data.md)<br />
[Web API Samples (Client-side JavaScript)](../web-api-samples-client-side-javascript.md)<br />
[Web API Basic Operations Sample (Client-side JavaScript)](basic-operations-client-side-javascript.md)<br />
[Web API Conditional Operations Sample (Client-side JavaScript)](conditional-operations-client-side-javascript.md)<br />
[Web API Functions and Actions Sample (Client-side JavaScript)](functions-actions-client-side-javascript.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]