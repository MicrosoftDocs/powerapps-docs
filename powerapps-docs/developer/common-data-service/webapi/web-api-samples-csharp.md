---
title: "Web API Samples (C#) (Common Data Service for Apps)| Microsoft Docs"
description: "This topic provides a description of various Web API samples that are implemented using C#"
ms.custom: ""
ms.date: 06/15/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 66e26684-819e-45f7-bec4-c250be4d6fed
caps.latest.revision: 14
author: "JimDaly"
ms.author: "jdaly"
---
# Web API Samples (C#)

This topic provides information about the Web API samples implemented with C#. While each sample focuses on a different aspect of the Common Data Service for Apps Web API, they share similar characteristics and structure.  
  
> [!NOTE]
>  This implementation approach uses low-level object creation and explicit HTTP message calls. This approach allows for control and demonstration  of the low level object properties which control the behavior of the Web API. This is intended to help you understand the inner workings  but doesn't necessarily represent an approach which will provide the best developer productivity experience.  
>   
>  In contrast, higher-level libraries, such as the [OData Library](https://msdn.microsoft.com/library/hh525392\(v=vs.103\).aspx), abstract away much of this low-level client logic.  The [OData T4 Template](https://blogs.msdn.microsoft.com/odatateam/2012/07/02/trying-out-the-prerelease-odata-client-t4-template/) can optionally be used in conjunction with the OData Library to auto-generate client entity classes.  

<a name="bkmk_prerequisites"></a>
   
## Prerequisites

The following is required to build and run the Common Data Service for Apps Web API C# samples :  
  
-   A version of Microsoft Visual Studio 2015 or later.  A free version, [Visual Studio Community](https://www.visualstudio.com/products/visual-studio-community-vs.aspx), is available for download [here](https://www.visualstudio.com/downloads/download-visual-studio-vs.aspx).  
  
-   An Internet connection to download and update the referenced NuGet packages.  
  
-   Access to  Common Data Service for Apps Online or on-premises (or later). For all Common Data Service for Apps installation types, a user account with privileges to perform CRUD operations is required.  
  
<!-- TODO:
-   In order to run samples against CDS for Apps, you must register your application with Azure Active Directory to obtain a client ID and redirect URL. For more information, see [Walkthrough: Register a Common Data Service for Apps app with Azure Active Directory](../walkthrough-register-app-azure-active-directory.md).   -->

> [!NOTE]
> These samples require version 2.x of assembly [Microsoft.IdentityModel.Client.ActiveDirectory](https://docs.microsoft.com/en-us/dotnet/api/microsoft.identitymodel.clients.activedirectory?view=azure-dotnet) for OAuth based authentication.
  
<a name="bkmk_webApiSamplesListing"></a>

## Web API samples listing (C#)

The following table lists the samples implemented in C#.  Each sample is described in a more general manner in a corresponding sample group topic that focuses on the HTTP request and response messages, as detailed in the topic [Web API Samples](web-api-samples.md).  
  
|Sample|Sample Group|Description|  
|------------|------------------|-----------------|  
|[Web API Basic Operations Sample (C#)](samples/basic-operations-csharp.md)|[Web API Basic Operations Sample](web-api-basic-operations-sample.md)|Demonstrates how to create, retrieve, update, delete, associate and disassociate Common Data Service for Apps entity records.|  
|[Web API Query Data Sample (C#)](samples/query-data-csharp.md)|[Web API Query Data Sample](web-api-query-data-sample.md)|Demonstrates how to use OData v4 query syntax and functions as well as Common Data Service for Apps query functions. Includes examples of working with pre-defined queries and using FetchXML to perform queries.|  
|[Web API Conditional Operations Sample (C#)](samples/conditional-operations-csharp.md)|[Web API Conditional Operations Sample](web-api-conditional-operations-sample.md)|Demonstrates how to perform conditional operations you specify with ETag criteria.|  
|[Web API Functions and Actions Sample (C#)](samples/functions-actions-csharp.md)|[Web API Functions and Actions Sample](web-api-functions-actions-sample.md)|Demonstrates how to use bound and unbound functions and actions, including custom actions.|  
  
<a name="bkmk_howDownloadRun"></a>

## How to download and run the samples
  
The source code for each sample is available on [MSDN Code Gallery](https://code.msdn.microsoft.com/site/search?f%5b0%5d.type=user&f%5b0%5d.value=microsoft%20dynamics%20crm%20sdk%20documentation%20team). The link to download each sample is included in the sample topic. The sample download is a compressed .zip file, which contains the Visual Studio 2015 solution files for the sample. For more information, see the **Run this sample** section in each sample topic.  
  
<a name="bkmk_commonElements"></a>

## Common elements found in each sample

Most of the samples have a similar structure and contain common methods and resources, typically to provide the basic infrastructure for a Web API C# program.  
  
Many of these common elements are also present when creating a new solution that will access the Common Data Service for Apps Web API. For more information, see [Start a Web API project in Visual Studio (C#)](start-web-api-project-visual-studio-csharp.md).  
  
### Utilized libraries and frameworks
 
This C# implementation depends upon the following helper code for HTTP communication, application configuration, authentication, error handling, and JSON serialization.  
  
-   The standard .NET Framework HTTP messaging classes that are contained in the  [System.Net.Http namespace](/dotnet/api/system.net.http), particularly [HttpClient](/dotnet/api/system.net.http.httpclient), [HttpRequestMessage](/dotnet/api/system.net.http.httprequestmessage), and [HttpResponseMessage](/dotnet/api/system.net.http.httpresponsemessage), are used for HTTP messaging.  
  
-   The Common Data Service for Apps Web API Helper Library is used to read the application configuration file, authenticate with the Common Data Service for Apps server, and assist in operation error handling.  For more information, see [Use the Common Data Service for Apps Web API Helper Library (C#)](use-microsoft-dynamics-365-web-api-helper-library-csharp.md).  
  
-   The Newtonsoft [Json.NET](http://www.newtonsoft.com/json) library supports the JSON data format.  
  
#### Json.NET Library

Because C# and most other managed languages do not natively support the JSON data format, the best current approach is to use a library for this functionality. For more information, see [An Introduction to JavaScript Object Notation (JSON) in JavaScript and .NET](https://msdn.microsoft.com/library/bb299886.aspx). Json.NET is a popular choice for .NET projects. It provides a robust, performant, open-source ([MIT licensed](https://opensource.org/licenses/MIT)) framework for serializing, converting, parsing, querying, and formatting JSON data. For more information, see the [Json.NET documentation](http://www.newtonsoft.com/json/help/html/Introduction.htm).  
  
In the C# samples, this library is primarily used to serialize data between .NET objects and HTTP message bodies. Although the library provides several methods to accomplish this task, the approach used by the samples is to create individual [JObject](http://www.newtonsoft.com/json/help/html/T_Newtonsoft_Json_Linq_JObject.htm) instances to represent Common Data Service for Apps entity instances (records).  For example, the following code creates the variable `contact1` that represents a Common Data Service for Apps <xref href="Microsoft.Dynamics.CRM.contact?text=contact EntityType" /> instance, then supplies values for a select set of properties for this type.  
  
```csharp  
  
JObject contact1 = new JObject();  
contact1.Add("firstname", "Peter");  
contact1.Add("lastname", "Cambel");  
contact1.Add("annualincome", 80000);  
contact1["jobtitle"] = "Junior Developer";  
  
```  
  
 The use of the bracket notation in the last statement is equivalent to the [Add](http://www.newtonsoft.com/json/help/html/M_Newtonsoft_Json_Linq_JObject_Add.htm) method. This instantiation could also be accomplished through the use of the [Parse](http://www.newtonsoft.com/json/help/html/M_Newtonsoft_Json_Linq_JObject_Parse.htm) static method:  
  
```csharp  
  
JObject contact1 = JObject.Parse(@"{firstname: 'Peter', lastname: 'Cambel', "  
+ @"annualincome: 80000, jobtitle: 'Junior Developer'}");  
  
```  
  
 Because `JObject` represents a general JSON type, its use precludes much runtime type checking.  For example, while the following statement is syntactically valid, it will potentially lead to runtime errors because the <xref href="Microsoft.Dynamics.CRM.contact?text=contact EntityType" /> does not contain an `age` property.  
  
 `contact1.Add("age", 37);    //Possible error--no age property exists in contact!`  
  
 Once the entity variable has been initialized, it can then be sent in a message body, with assistance from several System.Net.Http classes, for example:  
  
```csharp  
  
HttpRequestMessage request = new HttpRequestMessage(HttpMethod.Post, "contacts");  
request.Content = new StringContent(contact1.ToString(), Encoding.UTF8, "application/json");  
HttpResponseMessage response = await httpClient.SendAsync(request1);  
  
```  
  
 You can also create JObject instances by deserializing entity instances during retrieval operations, for example:  
  
```csharp  
  
//contact2Uri contains a reference to an existing CRM contact instance.  
string queryOptions = "?$select=fullname,annualincome,jobtitle,description";  
HttpResponseMessage response = await httpClient.GetAsync(contact2Uri + queryOptions);  
JObject contact2 = JsonConvert.DeserializeObject<JObject>(await response.Content.ReadAsStringAsync());  
  
```  
  
### Response success and error handling

In general, the samples take a straightforward approach to processing HTTP responses. If the request succeeds, information about the operation is typically output to the console. If the response also carries a JSON payload or useful headers, this information is only processed upon success. And lastly, if a Common Data Service for Apps entity was created, the `entityUris` collection is updated with the URI of that resource. The [DeleteRequiredRecords](#bkmk_deleteRequiredRecords) method uses this collection to optionally delete data created by the sample from your Common Data Service for Apps server.  
  
If the request failed, the program outputs a contextual message about the operation that failed, and then it throws a custom exception of type `CrmHttpResponseException`. The exception-handler outputs more information about the exception and then control passes to a `finally` block that includes cleanup logic, again including a call to `DeleteRequiredRecords`. The following code demonstrates this error-handling approach on a POST request to create a record.  
  
```csharp  
  
if (response.StatusCode == HttpStatusCode.NoContent)  //204  
{  
Console.WriteLine("POST succeeded, entity created!");  
//optionally process response message headers or body here, for example:  
entityUri = response.Headers.GetValues("OData-EntityId").FirstOrDefault();  
entityUris.Add(entityUri);  
}  
else  
{  
Console.WriteLine("Operation failed: {0}", response.ReasonPhrase);  
throw new CrmHttpResponseException(response.Content);  
}  
  
```  
  
 [HttpStatusCode](https://msdn.microsoft.com/library/hh435235.aspx).NoContent is equivalent to an HTTP status code 204, “No content”. Here, this status code indicates that the POST request succeeded. For more information, see [Compose HTTP requests and handle errors](https://msdn.microsoft.com/en-us/library/gg334391.aspx).  
  
### Characteristics and methods
  
Most of the samples have the same general architectural pattern, with the following characteristics:  
  
- All of the pertinent C# sample code is contained in the primary source file named `Program.cs`, which contains a single class with the same name as the sample project.  
  
- The sample classes, as well as the [Common Data Service for Apps Web API Helper Library](use-microsoft-dynamics-365-web-api-helper-library-csharp.md), is contained in the namespace `Microsoft.Crm.Sdk.Samples`.  
  
- The samples are liberally commented: summaries are provided at the class and method levels, and most key individual statements have associated same- or single-line comments.  Supplemental files, such as the application configuration file `App.config`, also often contain important comments.  
  
- The primary sample class is typically structured to contain the following common set of methods: [Main](#bkmk_main), [ConnectToCRM](#bkmk_connectToCrm), [CreateRequiredRecords](#bkmk_createRequiredRecords), [RunAsync](#bkmk_runAsync), [DisplayException](#bkmk_displayException), and [DeleteRequiredRecords](#bkmk_deleteRequiredRecords).  
  
<a name="bkmk_main"></a>
   
#### Main method

By definition, this method begins execution of the sample.  It only contains high-level control flow and exception-handling logic, often exactly the following code:  
  
```csharp  
  
static void Main(string[] args)  
{  
FunctionsAndActions app = new FunctionsAndActions();  
try  
{  
//Read configuration file and connect to specified CRM server.  
app.ConnectToCRM(args);  
app.CreateRequiredRecords();  
Task.WaitAll(Task.Run(async () => await app.RunAsync()));  
}  
catch (System.Exception ex) { DisplayException(ex);  
}  
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
  
```  
  
<a name="bkmk_connectToCrm"></a>

#### ConnectToCRM method
 
This method calls upon the helper libraries to read the application configuration file and then establishes a connection to the specified Common Data Service for Apps server. The result of these steps is the initialization of a [HttpClient](https://msdn.microsoft.com/en-us/library/system.net.http.httpclient\(v=vs.110\).aspx) class property that is used throughout the program to send web requests and receive responses.  Note the following properties are set on this object:  
  
```csharp  
  
//Define the Web API address, the max period of execute time, the Odata  
// version, and the expected response payload format.  
httpClient.BaseAddress = new Uri(config.ServiceUrl + "api/data/v8.1/");  
httpClient.Timeout = new TimeSpan(0, 2, 0);  // 2 minute timeout  
httpClient.DefaultRequestHeaders.Add("OData-MaxVersion", "4.0");  
httpClient.DefaultRequestHeaders.Add("OData-Version", "4.0");  
httpClient.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));  
  
```  
  
 For more information about sample application configuration and authentication, see [Use the Common Data Service for Apps Web API Helper Library (C#)](use-microsoft-dynamics-365-web-api-helper-library-csharp.md).  
  
<a name="bkmk_createRequiredRecords"></a>

#### CreateRequiredRecords method
 
This method creates and initializes entity records required by the sample, only when these operations are not of primary interest in the sample.  For example, the [Web API Basic Operations Sample (C#)](samples/basic-operations-csharp.md) does not contain this method because record creation is a primary consideration of the sample.  
  
<a name="bkmk_runAsync"></a>

#### RunAsync method

This asynchronous method either contains the pertinent source code or, for longer programs, calls methods that group the pertinent sample code. The contained code is explained by embedded comments and commentary located in the **Remarks** section of  each corresponding sample topic.  
  
<a name="bkmk_displayException"></a>
  
#### DisplayException method

This helper method displays exception information, including for inner exceptions, to the standard console.  
  
<a name="bkmk_deleteRequiredRecords"></a>
  
#### DeleteRequiredRecords method

This companion method optionally deletes sample records and other Common Data Service for Apps server resources created in the program and particularly by the [CreateRequiredRecords](#bkmk_createRequiredRecords) method. It queries the user for verification of this operation, then it iterates through the `entityUris` collection and attempts to delete each element with a HTTP DELETE message.  
  
### See also  

[Use the Common Data Service for Apps Web API](overview.md)<br />
[Web API Samples](web-api-samples.md)<br />
[Web API Samples (Client-side JavaScript)](web-api-samples-client-side-javascript.md)<br />
[Web API Basic Operations Sample (C#)](samples/basic-operations-csharp.md)<br />
[Web API Query Data Sample (C#)](samples/query-data-csharp.md)<br />
[Web API Conditional Operations Sample (C#)](samples/conditional-operations-csharp.md)<br />
[Web API Functions and Actions Sample (C#)](samples/functions-actions-csharp.md)
