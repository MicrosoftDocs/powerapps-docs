---
title: "WebApiService class library (C#) (Microsoft Dataverse) | Microsoft Docs"
description: "This sample .NET 6.0 class library project that demonstrates several important capabilities that you should include when you use the Dataverse Web API"
ms.date: 08/29/2022
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# WebAPIService class library (C#)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

WebAPIService is a sample .NET 6.0 class library project that demonstrates several important capabilities that you should include when you use the Dataverse Web API.

This library demonstrates:

- Managing Dataverse [service protection limits](../../api-limits.md) with the .NET resilience and transient fault handling library [Polly](https://github.com/App-vNext/Polly).
- Managing an [HttpClient](/dotnet/api/system.net.http.httpclient) in .NET using [IHttpClientFactory](/dotnet/api/system.net.http.ihttpclientfactory).
- Using configuration data to manage the behavior of the client.
- Managing errors returned by Dataverse Web API.
- A pattern of code reuse by:
  - Creating classes that inherit from [HttpRequestMessage](/dotnet/api/system.net.http.httprequestmessage?view=net-6.0&preserve-view=true) and [HttpResponseMessage](/dotnet/api/system.net.http.httpresponsemessage?view=net-6.0&preserve-view=true).
  - Methods that use those classes.
  - A modular pattern for adding new capabilities as needed.

> [!NOTE]
> This sample library is a helper that is used by all the Dataverse C# Web API samples, but it is not an SDK. It is tested only to confirm that the samples that use it run successfully. This sample code is provided 'as-is' with no warranty for reuse.

This library doesn't:

- **Manage authentication**. It depends on a function passed from an application that will provide the access token to use. All Web API samples depend on a shared [App class](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/C%23-NETx/App.cs) that manages authentication using the [Microsoft Authentication Library (MSAL)](/azure/active-directory/develop/msal-overview). MSAL supports several different types of authentication flows. These samples use the [Username/password (ROPC)](/azure/active-directory/develop/msal-authentication-flows) flow for simplicity but this isn't recommended. For your apps, you should use one of the other flows. More information: [Authentication flow support in the Microsoft Authentication Library](/azure/active-directory/develop/msal-authentication-flows).
- **Provide for any code generation capabilities**. All classes used in the samples are written by hand. All business entity data uses the well-known [Json.NET JObject Class](https://www.newtonsoft.com/json/help/html/t_newtonsoft_json_linq_jobject.htm) rather than a class representing the entity type.
- **Provide an object model for composing OData queries**. All queries show the OData query syntax as query parameters.

## Code

You can find the WebApiService class library source code and Visual Studio solution at [PowerApps-Samples/dataverse/webapi/C#-NETx/WebAPIService](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/C%23-NETx/WebAPIService)

## Class list

The following are classes included in the WebAPIService.

### Service Class

The `Service` class provides methods to send requests to Dataverse through an [HttpClient](/dotnet/api/system.net.http.httpclient) managed using [IHttpClientFactory](/dotnet/api/system.net.http.ihttpclientfactory).

The `Service` is the core component for all samples and can be used by itself to complete any operations demonstrated with sample code. Everything else that is included in the WebAPIService or any of the samples using it provides for reuse of code and allows for the capabilities of the Dataverse Web API to be demonstrated at a higher level.

The `Service` constructor accepts a [Config](#config-class) class instance, which contains two required properties: `GetAccessToken` and `Url`. All the other properties represent options that have defaults.

The constructor uses dependency injection to create an `IHttpClientFactory` that can return a named `HttpClient` with the properties specified in the `ConfigureHttpClient` function. Whether or not this client will use cookies is based on whether the `Config.DisableCookies` parameter is set. In the constructor the policy defined by the static `GetRetryPolicy` method that controls how transient errors and Dataverse service protection limits will be managed.

#### Service Methods

The `Service` class has the following methods:

##### SendAsync Method

This is the single method ultimately responsible for all operations.

This method:

- Has an [HttpRequestMessage](/dotnet/api/system.net.http.httprequestmessage?view=net-6.0&preserve-view=true) parameter.
- Returns `Task<HttpResponseMessage>`
- Exposes the same signature as the [HttpClient.SendAsync(HttpRequestMessage) Method](/dotnet/api/system.net.http.httpclient.sendasync?view=net-6.0&preserve-view=true) and can be used in the same way.
- Calls the function set in the `Config.GetAccessToken` method to set the `Authorization` header value for the request.
- Uses the [IHttpClientFactory.CreateClient Method](/dotnet/api/system.net.http.ihttpclientfactory.createclient?view=dotnet-plat-ext-6.0&preserve-view=true) to get the named `HttpClient` to send the request.
- Will throw a [ServiceException](#serviceexception) if the [HttpResponseMessage.IsSuccessStatusCode Property](/dotnet/api/system.net.http.httpresponsemessage.issuccessstatuscode?view=net-6.0&preserve-view=true) is false, so you don't need to check this when using this method.

##### SendAsync&lt;T&gt; Method

This method facilitates returning a class that includes properties found in the ComplexTypes returned by OData Actions and Functions in Dataverse Web API.

- Has an [HttpRequestMessage](/dotnet/api/system.net.http.httprequestmessage?view=net-6.0&preserve-view=true) parameter. When using this method it's expected, but not required, that the request parameter is one of the [*Response classes](#response-classes) that derive from `HttpResponseMessage`.
- Returns `Task<T>` where `T` is a class derived from `HttpResponseMessage`. See [*Response classes](#response-classes) for more information.
- Calls the [SendAsync Method](#sendasync-method).
- Uses the [HttpResponseMessage As&lt;T&gt;](#httpresponsemessage-ast) extension method to return the requested type.

The following example shows use with the <xref:Microsoft.Dynamics.CRM.WhoAmI?text=WhoAmI function>:

```csharp
static async Task WhoAmI(Service service)
{
   var response = await service.SendAsync<WhoAmIResponse>(new WhoAmIRequest());

   Console.WriteLine($"Your user ID is {response.UserId}");
}
```

##### ParseError Method

This method will parse the content of an `HttpResponseMessage` for an unsuccessful `HttpRequestMessage` to return an [ServiceException](#serviceexception). It's used within the [SendAsync method](#sendasync-method) when the [HttpResponseMessage.IsSuccessStatusCode Property](/dotnet/api/system.net.http.httpresponsemessage.issuccessstatuscode?view=net-6.0&preserve-view=true) is false. You can also use it to extract error information from `HttpResponseMessage` instances returned by `BatchResponse.HttpResponseMessages` when the `BatchRequest.ContinueOnError` property is set to true. More information: [Batch](#batch)

#### Service Properties

Service has a single property: `BaseAddress`.

##### BaseAddress Property

This property returns the base URL set in the `Config.Url`. This is needed when instantiating the [BatchRequest](#batchrequest) class and to append to a relative URL anytime an absolute URL is required.

### Config Class

The Config class contains properties that control the behavior of the application as shown in the table below:

|Property|Type|Description|
|---------|---------|---------|
|`GetAccessToken`|`Func<Task<string>>`|A function provided by the client application to return an access token.|
|`Url`|`string?`|The base Url of the environment. that is: `https://org.api.crm.dynamics.com`|
|`CallerObjectId`|`Guid`|The [SystemUser.ActiveDirectoryGuid](../../reference/entities/systemuser.md#BKMK_ActiveDirectoryGuid) value to apply for impersonation. Default is [Guid.Empty](/dotnet/api/system.guid.empty)<br /> More information: [Impersonate another user using the Web API](../impersonate-another-user-web-api.md)|
|`TimeoutInSeconds`|`ushort`|How long to wait for a timeout. Default is 120 seconds.|
|`MaxRetries`|`byte`|Maximum number of times to retry when service protection limits occur. Default is 3.|
|`Version`|`string`|The version of the service to use. Default is `v9.2`|
|`DisableCookies`|`bool`|Whether to disable cookies to gain performance in bulk data load scenarios. More information: [Server affinity](../../send-parallel-requests.md#server-affinity)|

### EntityReference Class

The EntityReference class represents a reference to a record in a Dataverse table. In OData resources are identified by a URL. EntityReference provides methods to make it easier create and access properties of Urls.

#### EntityReference Constructors

Use the following constructors to instantiate an EntityReference.

##### EntityReference(string entitySetName, Guid? ID)

Creates an entity reference using the `EntitySetName` and a `Guid`.

##### EntityReference(string uri)

Parses an absolute or relative url to create an entity reference, including Urls that use alternate keys.

##### EntityReference(string setName, Dictionary&lt;string, string&gt;? keyAttributes)

Use this constructor to instantiate an entity reference using an alternate key.

> [!NOTE]
> The key values must be string values. This does not convert other types to appropriate strings.

#### EntityReference Properties

EntityReference has the following public properties:

|Property  |Type   |Description  |
|---------|---------|---------|
|`Id`|`Guid?`|The primary key value of the record when not using an alternate key.|
|`KeyAttributes`|`Dictionary<string, string>`|The string values that represent alternate key values used in a url.|
|`SetName`|`string`|The `EntitySetName` of the entity type.|
|`Path`|`string`|A relative url to the record.|

#### EntityReference Methods

EntityReference has the following public methods. Neither of them require any parameters.

|Method Name|Return Type|Description|
|---------|---------|---------|
|`AsODataId`|`string`|Returns a string formatted for use as a parameter reference to a record in the URL for an OData Function.|
|`AsJObject`|`JObject`|Returns a JObject that can be used as a parameter reference to a record in an OData Action.|

### Error Classes

`ODataError`, `Error`, and `ODataException` are classes used to deserialize errors returned by the service. You won't need to work with them directly.

#### ServiceException

ServiceException is an [Exception class](/dotnet/api/system.exception?view=net-6.0&preserve-view=true) that contains properties of the error returned by the service. Use the [ParseError Method](#parseerror-method) to get an instance of this exception.

## Extensions

WebAPIService has one extension method from a .NET type.

### HttpResponseMessage As&lt;T&gt;

This extension instantiates an instance of `T` where `T` is derived from [HttpResponseMessage](/dotnet/api/system.net.http.httpresponsemessage?view=net-6.0&preserve-view=true) and copies the properties of the `HttpResponseMessage` to the derived class. It's used by the `Service` [SendAsync&lt;T&gt; Method](#sendasynct-method) but can also be used separately. For example, when using the [BatchRequest](#batchrequest) class, the items in the `BatchResponse.HttpResponseMessages` will be `HttpResponseMessage` types. You can use this extension to convert them to the appropriate derived class to facilitate accessing any properties.

## Messages

The `Messages` folder includes classes that inherit from [HttpRequestMessage](/dotnet/api/system.net.http.httprequestmessage?view=net-6.0&preserve-view=true) or [HttpResponseMessage](/dotnet/api/system.net.http.httpresponsemessage?view=net-6.0&preserve-view=true).

These classes provide reusable definitions of requests and responses that correspond to OData operations you can use in any Dataverse environment.

These classes also provide examples of specific operations that can be applied using `HttpRequestMessage` and `HttpResponseMessage` without deriving from those types.

Within an application, you may also create custom messages, for example representing a custom API in your environment, using the same pattern. These are modular classes and aren't required to be included in the `WebAPIService.Messages` folder.

For example, the [Web API Functions and Actions Sample (C#)](webapiservice-functions-and-actions.md) uses a custom API that isn't included in Dataverse until a solution containing the custom API is installed. The definition for the corresponding classes to use this message are located in the sample application that uses it:

- [FunctionsAndActions/Messages/IsSystemAdminRequest.cs](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/C%23-NETx/FunctionsAndActions/Messages/IsSystemAdminRequest.cs)
- [FunctionsAndActions/Messages/IsSystemAdminResponse.cs](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/C%23-NETx/FunctionsAndActions/Messages/IsSystemAdminResponse.cs)

### *Request classes

These classes will generally have a constructor with parameters that will instantiate a [HttpRequestMessage](/dotnet/api/system.net.http.httprequestmessage?view=net-6.0&preserve-view=true) with the data needed to perform the operation. They may have separate properties as appropriate.

The most simple example of this pattern is the `WhoAmIRequest` class.

```csharp
namespace PowerApps.Samples.Messages
{
    /// <summary>
    /// Contains the data to perform the WhoAmI function
    /// </summary>
    public sealed class WhoAmIRequest : HttpRequestMessage
    {
        /// <summary>
        /// Initializes the WhoAmIRequest
        /// </summary>
        public WhoAmIRequest()
        {
            Method = HttpMethod.Get;
            RequestUri = new Uri(
                uriString: "WhoAmI", 
                uriKind: UriKind.Relative);
        }
    }
}
```

The names of these classes may align with the classes in the Dataverse SDK <xref:Microsoft.Xrm.Sdk.Messages?text=Microsoft.Xrm.Sdk.Messages Namespace> but aren't limited to those operations. Web API provides for performing some operations that can't be done with the SDK, for example `CreateRetrieveRequest` is message that will create a record and retrieve it. The Dataverse SDK doesn't provide this capability in a single request.

### *Response classes

When \*Request classes returns a value there will be a corresponding \*Response class to access the returned properties. If the \*Request returns `204 No Content`, the operation will return an [HttpResponseMessage](/dotnet/api/system.net.http.httpresponsemessage?view=net-6.0&preserve-view=true) but there will be no derived class. Use the [SendAsync method](#sendasync-method) to send these requests.

\*Response classes provide typed properties that access the `HttpResponseMessage` `Headers` or `Content` properties and parse them to provide access to the Complex Type returned by the operation.

An example of this is the WhoAmIResponse class. Within this class you can find all the code needed to extract the properties of the <xref:Microsoft.Dynamics.CRM.WhoAmIResponse?text=WhoAmIResponse ComplexType>.

```csharp
using Newtonsoft.Json.Linq;

namespace PowerApps.Samples.Messages
{
    // This class must be instantiated by either:
    // - The Service.SendAsync<T> method
    // - The HttpResponseMessage.As<T> extension in Extensions.cs

    /// <summary>
    /// Contains the response from the WhoAmIRequest
    /// </summary>
    public sealed class WhoAmIResponse : HttpResponseMessage
    {

        // Cache the async content
        private string? _content;

        //Provides JObject for property getters
        private JObject _jObject
        {
            get
            {
                _content ??= Content.ReadAsStringAsync().GetAwaiter().GetResult();

                return JObject.Parse(_content);
            }
        }

        /// <summary>
        /// Gets the ID of the business to which the logged on user belongs.
        /// </summary>
        public Guid BusinessUnitId => (Guid)_jObject.GetValue(nameof(BusinessUnitId));

        /// <summary>
        /// Gets ID of the user who is logged on.
        /// </summary>
        public Guid UserId => (Guid)_jObject.GetValue(nameof(UserId));

        /// <summary>
        /// Gets ID of the organization that the user belongs to.
        /// </summary>
        public Guid OrganizationId => (Guid)_jObject.GetValue(nameof(OrganizationId));
    }
}

```

These classes can only be properly instantiated when returned by the [SendAsync&lt;T&gt; Method](#sendasynct-method) or by using the [HttpResponseMessage As&lt;T&gt;](#httpresponsemessage-ast) extension on an `HttpResponseMessage` that was returned by a `BatchResponse.HttpResponseMessages` property.

## Batch

The `Batch` folder contains three classes to manage sending OData $`batch` requests. More information: [Execute batch operations using the Web API](../execute-batch-operations-using-web-api.md).

### BatchRequest

The `BatchRequest` constructor initializes an `HttpRequestMessage` that can be used with [SendAsync&lt;T&gt; Method](#sendasynct-method) to send requests in batches. The constructor requires the `Service.BaseAddress` value to be passed as a parameter.

`BatchRequest` has the following properties.

|Property|Type|Description|
|---------|---------|---------|
|`ContinueOnError`|`Bool`|Controls whether the batch operation should continue when an error occurs.|
|`ChangeSets` |`List<ChangeSet>`|One or more change sets to be included in the batch.|
|`Requests`|`List<HttpRequestMessage>` |One or more `HttpMessageRequest` to be sent outside of any `ChangeSet`. |

When `ChangeSets` or `Requests` are set they're encapsulated into [HttpMessageContent](/previous-versions/aspnet/hh834416(v=vs.118)) and added to the `Content` of the request. The private `ToMessageContent` method applies the required changes to headers and returns the `HttpMessageContent` for both `ChangeSets` and `Requests` properties.

### ChangeSet

A change set represents a group of requests that must complete within a transaction.

It contains a single property:

|Property|Type|Description|
|---------|---------|---------|
|`Requests`|`List<HttpRequestMessage>`|One or more `HttpMessageRequest` to be performed within the transaction. |

### BatchResponse

`BatchResponse` has a single property:

|Property|Type|Description|
|---------|---------|---------|
|`HttpResponseMessages`|`List<HttpResponseMessage>`|The responses from the `$batch` operation. |

`BatchResponse` has a private `ParseMultipartContent` method used by the `HttpResponseMessages` property getter to parse the `MultipartContent` returned into individual `HttpResponseMessage`.

To access type properties of the `HttpResponseMessage` instances returned, you can use the [HttpResponseMessage As&lt;T&gt;](#httpresponsemessage-ast) extension method.

## Methods

For operations that are frequently performed, the `Methods` folder contains extensions of the `Service` class. These allow for using the corresponding *Request classes in a single line.

The following methods are included:

|Method |Return Type |Description |
|---------|---------|---------|
|`Create`|`Task<EntityReference>`|Creates a new record.|
|`CreateRetrieve` |`Task<JObject>`|Creates a new record and retrieves it.|
|`Delete`|`Task`|Deletes a record. |
|`FetchXml`|`Task<FetchXmlResponse>`|Retrieves the results of a FetchXml query. Request is sent with `POST` using `$batch` to mitigate issues where long URLs sent with `GET` can exceed limits.|
|`GetColumnValue<T>`|`Task<T>`|Retrieves a single column value from a table row.|
|`Retrieve` |`Task<JObject>`|Retrieves a record.|
|`RetrieveMultiple` |`Task<RetrieveMultipleResponse>`|Retrieves multiple records. |
|`SetColumnValue<T>`|`Task`|Sets the value of a column for a table row.|
|`Update` |`Task`|Updates a record. |
|`Upsert` |`Task<UpsertResponse>`|Performs an Upsert on a record.|

Within an a sample application using WebAPIService when the operation doesn't represent an API found in Dataverse by default, the method will be defined in the application rather than in the WebAPIService.

For example, the [Web API Functions and Actions Sample (C#)](webapiservice-functions-and-actions.md) uses a custom API that isn't included in Dataverse until a solution containing the custom API is installed. The definition for this method is located in the sample application that uses it: [FunctionsAndActions/Methods/IsSystemAdmin.cs](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/C%23-NETx/FunctionsAndActions/Methods/IsSystemAdmin.cs)

## Types

The `Types` folder contains any classes or enums that correspond to <xref:Microsoft.Dynamics.CRM.ComplexTypeIndex?text=ComplexTypes>  or <xref:Microsoft.Dynamics.CRM.EnumTypeIndex?text=EnumTypes> needed as parameters or response properties for messages.

## Metadata

The `Metadata` folder contains `Messages` and `Types` specific to operations that work with Dataverse Schema definitions. These are frequently classes with many properties that return complex types. These types are used in the [Web API Metadata Operations Sample (C#)](webapiservice-metadata-operations.md).

### See also

[Web API Basic Operations Sample (C#)](webapiservice-basic-operations.md)<br />
[Web API Query Data sample (C#)](webapiservice-query-data.md)<br />
[Web API Conditional Operations sample (C#)](webapiservice-conditional-operations.md)<br />
[Web API Functions and Actions Sample (C#)](webapiservice-functions-and-actions.md)<br />
[Web API Metadata Operations Sample (C#)](webapiservice-metadata-operations.md)<br />
[Web API WebApiService Parallel Operations Sample (C#)](webapiservice-parallel-operations.md)<br />
[Web API Parallel Operations with TPL Dataflow components Sample (C#)](webapiservice-tpl-dataflow-parallel-operations.md)<br />

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
