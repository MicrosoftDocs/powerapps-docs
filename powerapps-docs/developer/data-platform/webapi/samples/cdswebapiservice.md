---
title: "CDSWebApiService class library (C#) (Microsoft Dataverse) | Microsoft Docs"
description: "This .NET Framework class library provides an easier to use API for HTTP messaging with the the Microsoft Dataverse Web API."
ms.custom: ""
ms.date: 07/14/2021
ms.service: powerapps
applies_to: 
  - "Dynamics 365 (online)"
author: "JimDaly"
ms.author: "pehecke"
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# CDSWebApiService class library (C#)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

A .NET Framework sample class library that uses JSON objects and common HTTP messaging operations with the Microsoft Dataverse Web API. Use of these class methods result in less complicated application code, implementation of performance best practices, and improved error processing.

This class library demonstrates how to:

- Make your code '[DRY](/dotnet/architecture/modern-web-apps-azure/architectural-principles#dont-repeat-yourself-dry)'er by wrapping common operations by Http methods.
- Manage an <xref:System.Net.Http.HttpClient> in a thread-safe manner.
- Manage Service Protection Limit API [429 Too Many Requests](https://developer.mozilla.org/docs/Web/HTTP/Status/429) errors that a client application should expect.
    - More information: [Service Protection API Limits](../../api-limits.md)

Using the provided Visual Studio project, you can build a class library and include this functionality in your own application code. You can find the CDSWebApiService class library source code and Visual Studio solution at [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples)/cds/webapi/C#/CDSWebApiService.

## Example

This example shows how to instantiate a CDSWebAPIService instance and create a contact row.

This example expects that the connection string is set in the App.config file as shown below.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
  <startup>
    <supportedRuntime version="v4.0"
                      sku=".NETFramework,Version=v4.7.2" />
  </startup>
  <connectionStrings>
    <add name="Connect"
         connectionString="Url=https://yourorg.api.crm.dynamics.com;
         Authority=null;
         ClientId=51f81489-12ee-4a9e-aaae-a2591f45987d;
         RedirectUrl=app://58145B91-0C36-4500-8554-080854F2AC97;
         UserPrincipalName=you@yourorg.onmicrosoft.com;
         Password=y0urp455w0rd;
         CallerObjectId=null;
         Version=9.1;
         MaxRetries=3;
         TimeoutInSeconds=180;
         "/>
  </connectionStrings>
</configuration>
```
The code will access the connection string to instantiate the CDSWebApiService.

```csharp
//Get configuration data from App.config connectionStrings
static readonly string connectionString = ConfigurationManager.ConnectionStrings["Connect"].ConnectionString;
static readonly ServiceConfig config = new ServiceConfig(connectionString);

    using (CDSWebApiService svc = new CDSWebApiService(config))
    {
        //Create a contact
        var contact1 = new JObject
            {
                { "firstname", "Rafel" },
                { "lastname", "Shillo" }
            };
        Uri contact1Uri = svc.PostCreate("contacts", contact1);
    }
```

## Properties

This class exposes only the **BaseAddress** property. This is the configured <xref:System.Net.Http.HttpClient.BaseAddress> used by the <xref:System.Net.Http.HttpClient>. It can be useful to build complete URIs when needed since most cases will expect relative URIs.

## Methods

This class provides the following public methods:

## PostCreate

Creates a table row (entity record) synchronously and returns the URI.

### Parameters

|Name  |Type  |Description  |
|---------|---------|---------|
|entitySetName|<xref:System.String>|The entity set name of the type of entity to create. |
|body|[JObject](https://www.newtonsoft.com/json/help/html/T_Newtonsoft_Json_Linq_JObject.htm)|Contains the data for the entity to create|

### Return Value

The <xref:System.Uri> of the created table row (entity record)

### Remarks

This method is provided because creating entities is a common operation and the URI is returned in the `OData-EntityId` header. Having this specialized method allows for less code than having only the [Post](#post) method, which returns only a [JObject](https://www.newtonsoft.com/json/help/html/T_Newtonsoft_Json_Linq_JObject.htm).

More information: [Create a table row using the Web API](../create-entity-web-api.md).

## PostCreateAsync

The asynchronous version of [PostCreate](#postcreate).

## Post

Sends a `POST` request synchronously and returns the response as a [JObject](https://www.newtonsoft.com/json/help/html/T_Newtonsoft_Json_Linq_JObject.htm).

### Parameters

|Name  |Type  |Description  |
|---------|---------|---------|
|path|<xref:System.String>|The relative path to send the request. Frequently the name of an action or an entity set name.|
|body|[JObject](https://www.newtonsoft.com/json/help/html/T_Newtonsoft_Json_Linq_JObject.htm)|The payload to `POST`|
|headers|`Dictionary<string, List<string>>`|(Optional) Any headers needed to apply special behaviors|

### Return Value

A [JObject](https://www.newtonsoft.com/json/help/html/T_Newtonsoft_Json_Linq_JObject.htm) containing the response.

### Remarks

This method can be used for any operation using the `POST` http method, but it only includes the response content. Use [PostCreate](#postcreate) to create table rows (entity records) and return only the URI of the created row.

More information:

- [Create with data returned](../create-entity-web-api.md#create-with-data-returned)
- [Use Web API actions](../use-web-api-actions.md)


## PostAsync

The asynchronous version of [Post](#post).

## Patch

Sends a `PATCH` request synchronously.

### Parameters

|Name  |Type  |Description  |
|---------|---------|---------|
|uri|<xref:System.Uri>|The relative path to send the request. Frequently the Uri for a specific table row (entity record)|
|body|[JObject](https://www.newtonsoft.com/json/help/html/T_Newtonsoft_Json_Linq_JObject.htm)|The payload to send|
|headers|`Dictionary<string, List<string>>`|(Optional) Any headers needed to apply special behaviors|

### Remarks

Patch is frequently used to Update or Upsert table rows.

More information:

- [Basic update](../update-delete-entities-using-web-api.md#basic-update)
- [Upsert a table](../update-delete-entities-using-web-api.md#upsert-a-table)

## PatchAsync

The asynchronous version of [Patch](#patch).

## Get

Sends a `GET` request synchronously and returns data

### Parameters

|Name  |Type  |Description  |
|---------|---------|---------|
|path|<xref:System.String>|The relative path of the resource to return |
|headers|`Dictionary<string, List<string>>`|(Optional) Any headers needed to apply special behaviors|

### Return Value

A [JToken](https://www.newtonsoft.com/json/help/html/T_Newtonsoft_Json_Linq_JToken.htm) representing the requested data.

### Remarks

More information:

- [Query Data using the Web API](../query-data-web-api.md)
- [Retrieve a table row using the Web API](../retrieve-entity-using-web-api.md)
- [Use Web API functions](../use-web-api-functions.md)


## GetAsync

The asynchronous version of [Get](#get).

## Delete

Sends a `DELETE` request synchronously.

### Parameters

|Name  |Type  |Description  |
|---------|---------|---------|
|uri|<xref:System.Uri>|The relative path of the resource to delete |
|headers|`Dictionary<string, List<string>>`|(Optional) Any headers needed to apply special behaviors|

### Remarks

More information:

- [Basic delete](../update-delete-entities-using-web-api.md#basic-delete)
- [Remove a reference to a table](../associate-disassociate-entities-using-web-api.md#remove-a-reference-to-a-table-row)
- [Delete a single property value](../update-delete-entities-using-web-api.md#delete-a-single-property-value)

## DeleteAsync

The asynchronous version of [Delete](#delete).

## Put

Sends a `PUT` request synchronously.

### Parameters

|Name  |Type  |Description  |
|---------|---------|---------|
|uri|<xref:System.Uri>|The relative path to the resource to update.|
|property|<xref:System.String>|The name of the column to update|
|value|<xref:System.String>|The value to set|

### Remarks

Put is used to update specific table columns.

**Note**: The Http `PUT` method is also used to update table or column definitions (metadata). This method cannot be used for that purpose. It is specifically for business data.

More information: 

- [Update a single property value](../update-delete-entities-using-web-api.md#update-a-single-property-value)
- [Change the reference in a single-valued navigation property](../associate-disassociate-entities-using-web-api.md#change-the-reference-in-a-single-valued-navigation-property)


## PutAsync

The asynchronous version of [Put](#put).

## Private SendAsync method

All of the methods above route their requests through the private `SendAsync` method. This is where the low level common logic occurs.

This method contains the logic to manage any Service Protection API 429 errors and re-try them for a number of times configurable in the service.

In order to do this, it sends a copy of the request rather than the actual request because the request will be disposed and cannot be sent again if an error is returned.

The copy of the request is available because of the custom <xref:System.Net.Http.HttpRequestMessage> `Clone` method defined in the Extensions.cs file.

## OAuthMessageHandler

When the internal <xref:System.Net.Http.HttpClient> is initialized in the CDSWebApiService constructor, an instance of this class is set as an <xref:System.Net.Http.HttpMessageHandler>. This class works with the ADAL libraries to ensure that the `accessToken` will be refreshed each time a request is sent. If the `accessToken` expires, the ADAL library methods will automatically refresh it.

More information: [Example demonstrating a DelegatingHandler](../../authenticate-oauth.md#example-demonstrating-a-delegatinghandler)

## ServiceConfig

The CDSWebApiService class should be initialized with a connection string via the ServiceConfig class.

The ServiceConfig constructor accepts a connection string, typically from the App.config configuration, and the data defined there is parsed into a ServiceConfig instance which the CDSWebApiService constructor requires.

### Properties

The following are the properties of the ServiceConfig class.

|Name|Type|Description|
|---------|---------|---------|
|Authority|<xref:System.String>|The authority to use to authorize user. Default is 'https://login.microsoftonline.com/common'|
|CallerObjectId|<xref:System.Guid>|The Azure AD ObjectId for the user to impersonate other users.|
|ClientId|<xref:System.String>|The id of the application registered with Azure AD|
|MaxRetries|<xref:System.Byte>|The maximum number of attempts to retry a request blocked by service protection limits. Default is 3.|
|Password|<xref:System.Security.SecureString>|The password for the user principal|
|RedirectUrl|<xref:System.String>|The Redirect Url of the application registered with Azure AD|
|TimeoutInSeconds|`ushort`|The amount of time to try completing a request before it will be cancelled. Default is 120 (2 minutes)|
|Url|<xref:System.String>|The Url to the Dataverse environment, i.e "https://yourorg.api.crm.dynamics.com"|
|UserPrincipalName|<xref:System.String>|The user principal name of the user. i.e. you@yourorg.onmicrosoft.com|
|Version|<xref:System.String>|The version of the Web API to use. Default is '9.1'|

### Example connection string

Each of the samples that use CDSWebApiService include a reference to a common App.config and code to read a connection string value named '`Connect`'. The following is an example of that App.config:

```xml
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
  <startup>
    <supportedRuntime version="v4.0"
                      sku=".NETFramework,Version=v4.7.2" />
  </startup>
  <connectionStrings>
    <add name="Connect"
         connectionString="Url=https://yourorg.api.crm.dynamics.com;
         Authority=null;
         ClientId=51f81489-12ee-4a9e-aaae-a2591f45987d;
         RedirectUrl=app://58145B91-0C36-4500-8554-080854F2AC97;
         UserPrincipalName=you@yourorg.onmicrosoft.com;
         Password=y0urp455w0rd;
         CallerObjectId=null;
         Version=9.1;
         MaxRetries=3;
         TimeoutInSeconds=180;
         "/>
  </connectionStrings>
</configuration>
```

The **ClientId** and **RedirectUrl** values are for sample applications. You can use these to run the samples, but you should register your own applications and enter the corresponding values for these properties. 

More information: [Walkthrough: Register an app with Azure Active Directory](../../walkthrough-register-app-azure-active-directory.md)

## ServiceException

This class simply extends <xref:System.Exception> and provides additional properties from an error response.

### Properties

|Name  |Type  |Description  |
|---------|---------|---------|
|Message|<xref:System.String>|The message returned by the platform|
|ErrorCode|<xref:System.Int32>|The error code returned by the platform|
|StatusCode|<xref:System.Int32>|The <xref:System.Net.Http.HttpResponseMessage>.<xref:System.Net.Http.HttpResponseMessage.StatusCode>|
|ReasonPhrase|<xref:System.String>|The <xref:System.Net.Http.HttpResponseMessage>.<xref:System.Net.Http.HttpResponseMessage.ReasonPhrase>|

## Samples using this class

The following C# samples use this class:

- [Basic Operations Sample (C#)](cdswebapiservice-basic-operations.md)
- [Parallel Operations Sample (C#)](cdswebapiservice-parallel-operations.md)
- [Async Parallel Operations Sample (C#)](cdswebapiservice-async-parallel-operations.md)
- [Conditional Operations sample (C#)](cdswebapiservice-conditional-operations.md)
- [Query Data sample (C#)](cdswebapiservice-query-data.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
