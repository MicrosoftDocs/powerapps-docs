---
title: "Web API Samples (Client-side JavaScript) (Common Data Service for Apps)| Microsoft Docs"
description: "This topic provides a description of various Web API samples that are implemented using Client-side JavaScript"
ms.custom: ""
ms.date: 06/15/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: a32e9a04-7bc1-41dd-b9af-bb4f21a613c6
caps.latest.revision: 15
author: "brandonsimons" # GitHub ID
ms.author: "jdaly"
manager: "amyla"
---
# Web API Samples (Client-side JavaScript)



<!-- TODO: > [!NOTE]
> ![This page is under construction. Check back soon!](../../media/under_construction.png "Coming soon") [!INCLUDE[cc-under-construction](../../includes/cc-under-construction.md)]

With the availability of the new [Xrm.WebApi](../clientapi/reference/xrm-webapi.md) client API methods, we are working on updating the client-side JavaScript samples to use the new client API methods. Check back soon. -->

If you are using an earlier version of Common Data Service for Apps Customer Engagement, see [Web API Samples (Client-side JavaScript)](https://msdn.microsoft.com/library/mt770370.aspx)

<!--This topic provides common understanding about Web API samples using client-side JavaScript. While each sample focuses on a different aspect of Common Data Service for Apps Web API, they all follow similar process and structure described in this topic.  

<a name="bkmk_listOfSamples"></a>   
## Web API Samples using client-side JavaScript  
 The following samples use the patterns described here:  
  
|Sample|Sample Group|Description|  
|------------|------------------|-----------------|  
|[Web API Basic Operations Sample (Client-side JavaScript)](samples/basic-operations-client-side-javascript.md)|[Web API Basic Operations Sample](web-api-basic-operations-sample.md)|Demonstrates how to create, retrieve, update, delete, associate and disassociate CDS for Apps entity records.|  
|[Web API Query Data Sample (Client-side JavaScript)](samples/query-data-client-side-javascript.md)|[Web API Query Data Sample](web-api-query-data-sample.md)|Demonstrates how to use OData v4 query syntax and functions as well as Common Data Service for Apps query functions. Includes demonstration of working with pre-defined queries and using FetchXML to perform  queries.|  
|[Web API Conditional Operations Sample (Client-side JavaScript)](samples/conditional-operations-client-side-javascript.md)|[Web API Conditional Operations Sample](web-api-conditional-operations-sample.md)|Demonstrates how to perform conditional operations. The behavior of these operations depends on criteria you specify.|  
|[Web API Functions and Actions Sample (Client-side JavaScript)](samples/functions-actions-client-side-javascript.md)|[Web API Functions and Actions Sample](web-api-functions-actions-sample.md)|Demonstrates how to use bound and unbound functions and actions, including custom actions.|  
  
<a name="bkmk_howToDownload"></a>   
## How to download the source code for the sample.  
 The source code for each sample is available on [MSDN Code Gallery](https://code.msdn.microsoft.com/site/search?f%5b0%5d.type=user&f%5b0%5d.value=microsoft%20dynamics%20crm%20sdk%20documentation%20team). The link to download each sample is included in the individual page for that sample.  
  
 After you download the sample, extract the compressed file. Find the [!INCLUDE[pn_visual_studio_2015](../../includes/pn-visual-studio-2015.md)] solution for each sample within the C# folder because the project is an empty [!INCLUDE[pn_ASP.NET_short](../../includes/pn-asp-net-short.md)] web application project. A CDS for Apps solution is also provided in the download that you can import and run.  
  
> [!NOTE]
>  Neither Visual Studio or [!INCLUDE[pn_ASP.NET_short](../../includes/pn-asp-net-short.md)] is required to develop  client-side JavaScript for CDS for Apps, however the MSDN Code Gallery site requires files be included in a Visual Studio as a container.  However, Visual Studio does provide a good experience for writing JavaScript.  
  
<a name="bkmk_HowToImport"></a>   
## How to import the Common Data Service for Apps solution that contains the sample.  
 Within each project you will find a Common Data Service for Apps managed solution file. The name of this file will depend on the sample's project name, but the file name will end with `_managed.zip`.  
  
 To import the CDS for Apps solution to your CDS for Apps server, do the following:  
  
1.  Extract the contents of the downloaded zip file and locate the CDS for Apps solution file, which will also be a zip file. For example, if you downloaded the `Basic Operations` sample, look for the CDS for Apps solution zip file with the name `WebAPIBasicOperations\WebAPIBasicOperations_1_0_0_0_managed.zip`.  
  
2.  In the CDS for Apps UI, go to **Settings > Solutions**. This page lists all solutions on your CDS for Apps server. After you finished importing this solution, the solution name for that sample will appear in this list (e.g.: **Web API Basics Operations**).  
  
3.  Click **Import** and follow the instructions on the import dialog to complete this action.  
  
<a name="bkmk_howToRunSample"></a>   
## How to run the sample to see the script in action  
 The sample program runs as a web resource within CDS for Apps. The imported solution provides a configuration page that gives you an option to keep or delete sample data and a button to start the sample program.  For the `Basic Operations` sample, this interface looks like the following.  
  
 ![Common Data Service for Apps Web API Sample Configuration page](../media/crm-web-api-js-sample-configuration.png "Common Data Service for Apps Web API Sample Configuration page")  
  
 To run the sample, do the following:  
  
1.  From the **All Solutions** page in CDS for Apps, click the solution name (e.g.: **Web API Basics Operations** link). This will open the solution's properties in a new window.  
  
2.  From the left navigation menu, click **Configuration**.  
  
3.  Click **Start Sample** button to execute the sample code.  
  
<a name="bkmk_commonElements"></a>   
## Common elements found in each sample  
 The following list highlights some common elements found in each of these samples.  
  
-   The `Sdk.startSample` function is called when a user clicks the **Start Sample** button from the  HTML page. The `Sdk.startSample` function initializes global variables and kicks off the first operation in the chain.  
  
-   Program output and error messages are sent to the browser’s debugger console. To see these output, open the console window first before running the sample.  Press F12 to access the developer tools, including the console window, in the [!INCLUDE[pn_Windows_Internet_Explorer](../../includes/pn-windows-internet-explorer.md)] and [!INCLUDE[pn_microsoft_edge](../../includes/pn-microsoft-edge.md)] browsers.  
  
-   These samples use the browser native [ES6-Promise](https://msdn.microsoft.com/en-us/library/dn802826\(v=vs.94\).aspx) implementation for modern browsers that support it. For [!INCLUDE[pn_ie_11](../../includes/pn-ie-11.md)], this sample uses the [ES6-Promise polyfill](https://github.com/stefanpenner/es6-promise) because [!INCLUDE[pn_ie_11](../../includes/pn-ie-11.md)] is the only browser supported by Common Data Service for Apps which does not have native support for this feature.  
  
     Promises are not required. Similar interactions can be performed using callback functions. For more information, see [Create a re-usable function using promises](get-started-web-api-client-side-javascript.md#bkmk_createPromiseFunction).  
  
-   The `Sdk.request` function handles the request based on the information passed in as parameters. Depending on the need of each sample, the parameters passed in may be different. See the source code of that sample for more details.  
  
    ```javascript  
    /**  
     * @function request  
     * @description Generic helper function to handle basic XMLHttpRequest calls.  
     * @param {string} action - The request action. String is case-sensitive.  
     * @param {string} uri - An absolute or relative URI. Relative URI starts with a "/".  
     * @param {object} data - An object representing an entity. Required for create and update actions.  
     * @returns {Promise} - A Promise that returns either the request object or an error object.  
     */  
    Sdk.request = function (action, uri, data) {  
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
    ```  
  
     The `Sdk.request` function returns a promise. When the request wrapped by the promise is completed, the promise is either resolved or rejected. If it is resolved, the function in the following `then` method will be called. If it is rejected, the function in the following `catch` method will be called. If the function within the `then` method itself returns a promise, the chain of operations within consecutive `then` methods can continue. Returning a promise allows us to chain these sample operations together in a way that is preferred by many developers to traditional callback functions. For more information about promise, see [JavaScript Promise](https://msdn.microsoft.com/en-us/library/dn802826\(v=vs.94\).aspx).-->  
  
### See also

[Use the Common Data Service for Apps Web API](overview.md)<br />
[Web API Samples](web-api-samples.md)<br />
[Web API Samples (C#)](web-api-samples-csharp.md)   
 
