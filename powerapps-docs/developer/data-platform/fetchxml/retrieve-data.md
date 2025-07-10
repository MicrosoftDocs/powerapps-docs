---
title: Use FetchXml to retrieve data
description: Learn how to use the Dataverse SDK for .NET or Web API to send a request to retrieve data using FetchXml
ms.date: 01/26/2025
ms.reviewer: jdaly
ms.topic: how-to
author: MsSQLGirl
ms.subservice: dataverse-developer
ms.author: jukoesma
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - dmitmikh
 - dasussMS
 - apahwa-lab
 - DonaldlaGithub
---
# Use FetchXml to retrieve data

You can use FetchXml to retrieve data using either the SDK for .NET or Web API. With Power Automate, you can retrieve data using the Web API using the [Fetch Xml Query parameter of the List Rows command](/power-automate/dataverse/list-rows#fetch-xml-query). With PAC CLI, use the [pac env fetch](/power-platform/developer/cli/reference/env#pac-env-fetch) command.

You may also want to use [Community tools](overview.md#community-tools), like the [FetchXML Builder](https://fetchxmlbuilder.com/) in the [XrmToolBox](../community-tools.md#xrmtoolbox).

How you retrieve data depends on whether you are using the [SDK for .NET](../org-service/overview.md) or [Dataverse Web API](../webapi/overview.md).

## [SDK for .NET](#tab/sdk)

Use the [FetchExpression class](xref:Microsoft.Xrm.Sdk.Query.FetchExpression) to hold the FetchXml query as a string. `FetchExpression` is derived from the common [QueryBase class](xref:Microsoft.Xrm.Sdk.Query.QueryBase) type, so you can use it when that type is a method parameter or class property.

You should use the [IOrganizationService.RetrieveMultiple method](xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A) for most cases.

```csharp
static EntityCollection RetrieveMultipleExample(IOrganizationService service, string fetchXml)
{
   return service.RetrieveMultiple(new FetchExpression(fetchXml));
}
```

You can also use the [RetrieveMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest) with the [IOrganizationService.Execute method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A), but there are few scenarios where this is necessary.

```csharp
static EntityCollection RetrieveMultipleRequestExample(IOrganizationService service, string fetchXml)
{
   var request = new RetrieveMultipleRequest()
   {
         Query = new FetchExpression(fetchXml)
   };

   var response = (RetrieveMultipleResponse)service.Execute(request);

   return response.EntityCollection;
}
```

[Quickstart: Execute an SDK for .NET request (C#)](../org-service/quick-start-org-service-console-app.md)   
[Learn more about using messages with the SDK for .NET](../org-service/use-messages.md)

## [Web API](#tab/webapi)

Pass your FetchXml query as a URL-encoded string value to the entity set collection using the `fetchXml` query parameter.

> [!NOTE]
> Unlike queries that use the OData syntax, FetchXML queries sent using Web API don't return properties with null values. [Learn more about this behavior](#null-column-values-are-not-returned)

For example, if you want to retrieve data from the [account entity set](xref:Microsoft.Dynamics.CRM.account), you will compose a fetchXml query setting the [entity element](reference/entity.md) `name` parameter to the `account`.

```xml
<fetch top='5'>
  <entity name='account'>
    <attribute name='name' />
  </entity>
</fetch>
```

Then, URL-encode the value.  Most programming languages include a function to URL-encode a string.

- In JavaScript, you use the [encodeURI function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent).
- In .NET, you can use the [System.NET.WebUtility.UrlEncode(String) method](xref:System.Net.WebUtility.UrlEncode(System.String))

> [!TIP]
> The [XrmToolBox](../community-tools.md#xrmtoolbox) tool [FetchXML Builder](https://fetchxmlbuilder.com/) provides an option to escape the fetchxml.

The URL-encoded string for the previous query example looks like this:

```text
%3Cfetch%20top%3D%275%27%3E%0D%0A%3Centity%20name%3D%27account%27%3E%0D%0A%3Cattribute%20name%3D%27name%27%2F%3E%0D%0A%3C%2Fentity%3E%0D%0A%3C%2Ffetch%3E
```

Then send your request to the `accounts` entity set with the `fetchXml` parameter in the URL.

**Request**:

```http
GET [Organization URI]/api/data/v9.2/accounts?fetchXml=%3Cfetch%20top%3D%275%27%3E%0D%0A%3Centity%20name%3D%27account%27%3E%0D%0A%3Cattribute%20name%3D%27name%27%2F%3E%0D%0A%3C%2Fentity%3E%0D%0A%3C%2Ffetch%3E
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**Response**:

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,accountid)",
    "value": [
        {
            "@odata.etag": "W/\"81359849\"",
            "name": "Litware, Inc. (sample)",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd"
        },
        {
            "@odata.etag": "W/\"80649580\"",
            "name": "Adventure Works (sample)",
            "accountid": "7a914942-34cb-ed11-b596-0022481d68cd"
        },
        {
            "@odata.etag": "W/\"84077591\"",
            "name": "Fabrikam, Inc. (sample)",
            "accountid": "7c914942-34cb-ed11-b596-0022481d68cd"
        },
        {
            "@odata.etag": "W/\"84174320\"",
            "name": "Blue Yonder Airlines (sample)",
            "accountid": "7e914942-34cb-ed11-b596-0022481d68cd"
        },
        {
            "@odata.etag": "W/\"80649588\"",
            "name": "City Power & Light (sample)",
            "accountid": "80914942-34cb-ed11-b596-0022481d68cd"
        }
    ]
}
```

## Use FetchXML within a batch request

The length of a URL in a `GET` request [is limited to 32 KB (32,768 characters)](../webapi/compose-http-requests-handle-errors.md#maximum-url-length). Including FetchXML as a parameter in the URL can reach the limit. You can execute a `$batch` operation using a `POST` request as a way to move the FetchXML out of the URL and into the body of the request where the limit doesn't apply. Sending a `GET` request within a `$batch` allows for URLs up to 64 KB (65,536 characters) in length. More than with a normal `GET` request, but it isn't unlimited. More information: [Execute batch operations using the Web API](../webapi/execute-batch-operations-using-web-api.md).


[Quick Start: Web API sample (C#)](../webapi/quick-start-console-app-csharp.md)   
[Use the Microsoft Dataverse Web API](../webapi/overview.md)

---

## Null column values are not returned

When a table column contains a null value, or if the column wasn't requested, the record returned won't include the value. There isn't a key to access it or a value to return. The absence of the attribute indicates that it's null. This is the behavior using the SDK for .NET. [Learn more about this behavior](../org-service/entity-operations-query-data.md#null-column-values-are-not-returned)

Columns that are not valid for read always return null values. The definition of these columns have the [AttributeMetadata.IsValidForRead](/dotnet/api/microsoft.xrm.sdk.metadata.attributemetadata.isvalidforread) property set to false.

## Next steps

Learn how to select columns.

> [!div class="nextstepaction"]
> [Select columns](select-columns.md)

Try some sample code

> [!div class="nextstepaction"]
> [FetchXml Sample code](sample.md)

