---
title: "Web API  Data operations  Samples (C#) (Microsoft Dataverse)| Microsoft Docs"
description: "This topic provides a description of various Web API samples that are implemented using C#"
ms.custom: ""
ms.date: 10/31/2018
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 66e26684-819e-45f7-bec4-c250be4d6fed
caps.latest.revision: 14
author: "JimDaly" # GitHub ID
ms.author: "jdaly"
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Web API Data operations Samples (C#)

[!INCLUDE[cc-data-platform-banner](../../../includes/cc-data-platform-banner.md)]

This topic provides information about the Web API samples implemented with C#. While each sample focuses on a different aspect of the Microsoft Dataverse Web API, they share similar characteristics and structure.  
  
> [!NOTE]
> This implementation approach uses low-level object creation and explicit HTTP message calls. This approach allows for control and demonstration  of the low level object properties which control the behavior of the Web API. This is intended to help you understand the inner workings  but doesn't necessarily represent an approach which will provide the best developer productivity experience.  
>
> In contrast, higher-level libraries, such as the [OData Library](https://msdn.microsoft.com/library/hh525392\(v=vs.103\).aspx), abstract away much of this low-level client logic.  The [OData T4 Template](https://blogs.msdn.microsoft.com/odatateam/2012/07/02/trying-out-the-prerelease-odata-client-t4-template/) can optionally be used in conjunction with the OData Library to auto-generate client entity classes.  

<a name="bkmk_prerequisites"></a>
   
## Prerequisites

The following is required to build and run the Dataverse Web API C# samples :  
  
- A version of Microsoft Visual Studio 2015 or later.  A free version, [Visual Studio Community](https://www.visualstudio.com/products/visual-studio-community-vs.aspx), is available for download [here](https://www.visualstudio.com/downloads/download-visual-studio-vs.aspx).  

- Access to  Dataverse with privileges to perform CRUD operations.  
 
- In order to run samples against Dataverse, you must register your application with Azure Active Directory to obtain a client ID and redirect URL. For more information, see [Walkthrough: Register a Dataverse app with Azure Active Directory](../walkthrough-register-app-azure-active-directory.md).

> [!NOTE]
> These samples require version 2.x of assembly [Microsoft.IdentityModel.Client.ActiveDirectory](/dotnet/api/microsoft.identitymodel.clients.activedirectory?view=azure-dotnet) for OAuth based authentication.
  
<a name="bkmk_webApiSamplesListing"></a>

## Web API samples listing (C#)

The following table lists the samples implemented in C#.  Each sample is described in a more general manner in a corresponding sample group topic that focuses on the HTTP request and response messages, as detailed in the topic [Web API Samples](web-api-samples.md).  
  
|Sample|Sample Group|Description|  
|------------|------------------|-----------------|  
|[Web API Basic Operations Sample (C#)](samples/cdswebapiservice-basic-operations.md)|[Web API Basic Operations Sample](web-api-basic-operations-sample.md)|Demonstrates how to create, retrieve, update, delete, associate and disassociate Dataverse entity records.|  
|[Web API Query Data Sample (C#)](samples/cdswebapiservice-query-data.md)|[Web API Query Data Sample](web-api-query-data-sample.md)|Demonstrates how to use OData v4 query syntax and functions as well as Dataverse query functions. Includes examples of working with pre-defined queries and using FetchXML to perform queries.|  
|[Web API Conditional Operations Sample (C#)](samples/cdswebapiservice-conditional-operations.md)|[Web API Conditional Operations Sample](web-api-conditional-operations-sample.md)|Demonstrates how to perform conditional operations you specify with ETag criteria.|  
|[Web API Functions and Actions Sample (C#)](samples/functions-actions-csharp.md)|[Web API Functions and Actions Sample](web-api-functions-actions-sample.md)|Demonstrates how to use bound and unbound functions and actions, including custom actions.|  
  
<a name="bkmk_howDownloadRun"></a>

## How to download and run the samples
  
The source code for each sample is available on [GitHub](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/webapi/C%23). You can download the repository as a zip file which contains the solution files for the samples. For more information, see the **How to run this sample** section in each sample topic.  
  
### Utilized libraries and frameworks

This C# implementation depends upon the following:
  
- The standard .NET Framework HTTP messaging classes that are contained in the  [System.Net.Http namespace](/dotnet/api/system.net.http), particularly [HttpClient](/dotnet/api/system.net.http.httpclient), [HttpRequestMessage](/dotnet/api/system.net.http.httprequestmessage), and [HttpResponseMessage](/dotnet/api/system.net.http.httpresponsemessage), are used for HTTP messaging.  
  
- The Newtonsoft [Json.NET](https://www.newtonsoft.com/json) library which supports the JSON data format.  
  
#### Json.NET Library

Because C# and most other managed languages do not natively support the JSON data format, the best current approach is to use a library for this functionality. For more information, see [An Introduction to JavaScript Object Notation (JSON) in JavaScript and .NET](/previous-versions/dotnet/articles/bb299886(v=msdn.10)). Json.NET is a popular choice for .NET projects. It provides a robust, performant, open-source ([MIT licensed](https://opensource.org/licenses/MIT)) framework for serializing, converting, parsing, querying, and formatting JSON data. For more information, see the [Json.NET documentation](https://www.newtonsoft.com/json/help/html/Introduction.htm).  
  
In the C# samples, this library is primarily used to serialize data between .NET objects and HTTP message bodies. Although the library provides several methods to accomplish this task, the approach used by the samples is to create individual [JObject](https://www.newtonsoft.com/json/help/html/T_Newtonsoft_Json_Linq_JObject.htm) instances to represent Dataverse entity instances (records).  For example, the following code creates the variable `contact1` that represents a Dataverse <xref href="Microsoft.Dynamics.CRM.contact?text=contact EntityType" /> instance, then supplies values for a select set of properties for this type.  
  
```csharp  
  
JObject contact1 = new JObject();  
contact1.Add("firstname", "Peter");  
contact1.Add("lastname", "Cambel");  
contact1.Add("annualincome", 80000);  
contact1["jobtitle"] = "Junior Developer";  
  
```  
  
 The use of the bracket notation in the last statement is equivalent to the [Add](https://www.newtonsoft.com/json/help/html/M_Newtonsoft_Json_Linq_JObject_Add.htm) method. This instantiation could also be accomplished through the use of the [Parse](https://www.newtonsoft.com/json/help/html/M_Newtonsoft_Json_Linq_JObject_Parse.htm) static method:  
  
```csharp  
  
JObject contact1 = JObject.Parse(@"{firstname: 'Peter', lastname: 'Cambel', "  
+ @"annualincome: 80000, jobtitle: 'Junior Developer'}");  
  
```  
  
 Because `JObject` represents a general JSON type, its use precludes much runtime type checking.  For example, while the following statement is syntactically valid, it will potentially lead to runtime errors because the <xref href="Microsoft.Dynamics.CRM.contact?text=contact EntityType" /> does not contain an `age` property.  
  
 `contact1.Add("age", 37);    //Possible error--no age property exists in contact!`  
  
 Once the entity variable has been initialized, it can then be sent in a message body, with assistance from several System.Net.Http classes, for example:  
  
```csharp  
  
HttpRequestMessage createrequest1 = new HttpRequestMessage(HttpMethod.Post, client.BaseAddress + "contacts");
createrequest1.Content = new StringContent(contact1.ToString());
createrequest1.Content.Headers.ContentType = MediaTypeHeaderValue.Parse("application/json");
HttpResponseMessage createResponse1 = client.SendAsync(createrequest1, HttpCompletionOption.ResponseHeadersRead).Result; 
  
```  
  
 You can also create JObject instances by deserializing entity instances during retrieval operations, for example:  
  
```csharp  
  
//contact2Uri contains a reference to an existing CRM contact instance.  
string queryOptions = "?$select=fullname,annualincome,jobtitle,description";
HttpResponseMessage retrieveResponse1 = client.GetAsync(contact1Uri + queryOptions, HttpCompletionOption.ResponseHeadersRead).Result;
if (retrieveResponse1.IsSuccessStatusCode) //200
   {
     retrievedcontact1 = JObject.Parse(retrieveResponse1.Content.ReadAsStringAsync().Result);
     Console.WriteLine("Contact '{0}' retrieved: \n\tAnnual income: {1}" + "\n\tJob title: {2} \n\tDescription: {3}.",

// Can use either indexer or GetValue method (or a mix of two)
retrievedcontact1.GetValue("fullname"),
retrievedcontact1["annualincome"],
retrievedcontact1["jobtitle"],
retrievedcontact1["description"]);   //description is initialized empty.
    }
else
{
Console.WriteLine("Failed to retrieve contact for reason: {0}",retrieveResponse1.ReasonPhrase);
throw new Exception(string.Format("Failed to retrieve contact for reason: {0}", retrieveResponse1.Content));
 } 

```
  
### Response success and error handling

In general, the samples take a straightforward approach to processing HTTP responses. If the request succeeds, information about the operation is typically output to the console. If the response also carries a JSON payload or useful headers, this information is only processed upon success. And lastly, if a Dataverse entity was created, the `entityUris` collection is updated with the URI of that resource. The `DeleteRequiredRecords` method uses this collection to optionally delete data created by the sample from your Dataverse server.  
  
If the request failed, the program outputs a contextual message about the operation that failed, and then it throws a custom exception of type `Exception`. The exception-handler outputs more information about the exception and then control passes to a `finally` block that includes cleanup logic, again including a call to `DeleteRequiredRecords`. The following code demonstrates this error-handling approach on a POST request to create a record.  
  
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
throw new Exception(string.Format(" Operation Failed", response.Content));  
}  
  
```  

 [HttpStatusCode](/previous-versions/windows/embedded/hh435235(v=msdn.10)).NoContent is equivalent to an HTTP status code 204, “No content”. Here, this status code indicates that the POST request succeeded. For more information, see [Compose HTTP requests and handle errors](/previous-versions/dynamicscrm-2016/developers-guide/gg334391(v=crm.8)).  
  
### Characteristics and methods
  
Most of the samples have the same general architectural pattern, with the following characteristics:  
  
- All of the pertinent C# sample code is contained in the primary source file named `SampleProgram.cs`, which contains a single class with the same name as the sample project.  
  
- The samples are liberally commented: summaries are provided at the class and method levels, and most key individual statements have associated same- or single-line comments.  Supplemental files, such as the application configuration file `App.config`, also often contain important comments.  
   
### See also  

[Use the Dataverse Web API](overview.md)<br />
[Web API Samples](web-api-samples.md)<br />
[Web API Samples (Client-side JavaScript)](web-api-samples-client-side-javascript.md)<br />
[Web API Basic Operations Sample (C#)](samples/cdswebapiservice-basic-operations.md)<br />
[Web API Query Data Sample (C#)](samples/cdswebapiservice-query-data.md)<br />
[Web API Conditional Operations Sample (C#)](samples/cdswebapiservice-conditional-operations.md)<br />
[Web API Functions and Actions Sample (C#)](samples/functions-actions-csharp.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]