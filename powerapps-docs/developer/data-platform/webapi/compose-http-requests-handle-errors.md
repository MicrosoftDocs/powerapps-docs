---
title: "Compose HTTP requests and handle errors (Microsoft Dataverse)| Microsoft Docs"
description: "Read about the HTTP methods and headers that form a part of HTTP requests for the Web API, and then learn how to identify and handle errors returned in the response"
ms.date: 08/17/2022
author: divka78
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors: 
  - JimDaly
---

# Compose HTTP requests and handle errors

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

You interact with the Web API by composing and sending HTTP requests. You need to know how to set the appropriate HTTP headers and handle any errors included in the response.  

<a name="bkmk_url_versions"></a>

## Web API URL and versions

To find the Web API URL for your environment:

1. Sign into [Power Apps](https://make.powerapps.com/), and select your environment from the top-right corner.
1. Select the **Settings** button in the top-right corner, and select **Developer resources**.

:::image type="content" source="../media/dev-resources-menu.png" alt-text="Developer resources menu":::

From here, you can copy the value for the **Web API endpoint**. More information: [View developer resources](../view-download-developer-resources.md)


The following table describes the parts of the URL:

|Part|Description|
|--|--|
|Protocol| `https://`|
|Environment Name|The unique name that applies to your environment. If your company name is *Contoso*, then it may be `contoso`.|
|Region|Your environment will usually be available in a data center that is close to you geographically. For North America, it is `crm`. For South America `crm2`, For Japan `crm7`. For the complete list, see [Datacenter regions](/power-platform/admin/new-datacenter-regions)|
|Base URL|This is usually `dynamics.com.`, but some data centers use different values. See [Datacenter regions](/power-platform/admin/new-datacenter-regions)|
|Web API path|The path to the web API is `/api/data/`.|
|Version|The version is expressed this way: `v[Major_version].[Minor_version][PatchVersion]/`. The current version is `v9.2`.|
|Resource|The `EntitySetName` of the table, or the name of the function or action you want to use.|

The URL you will use will be composed with these parts:

Protocol + Environment Name + Region + Base URL + Web API path + Version + Resource.


<a name="version_compatiblity"></a>

### Version compatibility

This release introduces capabilities which are not available in previous versions. Subsequent minor versions may provide additional capabilities which will not be back ported to earlier minor versions. Your code written for v9.0 will continue to work in future versions when you reference v9.0 in the URL you use.

As new capabilities are introduced they may conflict with earlier versions. This is necessary to allow the service to become better. Most of the time, capabilities will remain the same between versions but you should not assume they will.

> [!NOTE]
> Unlike the v8.x minor releases, new capabilities or other changes added to future versions will not be applied to earlier versions.
> You will need to pay attention to the version of the service you use and test your code if you change the version used.

<a name="bkmk_methods"></a>

## HTTP methods

 HTTP requests can apply a variety of different methods. When using the web API you will only use the methods listed in the following table.  
  
|Method|Usage|  
|------------|-----------|  
|`GET`|Use when retrieving data, including calling functions. The expected Status Code for a successful retrieve is 200 OK.|  
|`POST`|Use when creating entities or calling actions.|  
|`PATCH`|Use when updating entities or performing upsert operations.|  
|`DELETE`|Use when deleting entities or individual properties of entities.|  
|`PUT`|Use in limited situations to update individual properties of entities. This method isn't recommended when updating most entities. You'll use this when updating table definitions. More information: [Use the Web API with table definitions](use-web-api-metadata.md)|  
  
<a name="bkmk_headers"></a>

## HTTP headers

All HTTP requests should include at least the following headers.  
  
```http
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-None-Match: null
```  

Although the OData protocol allows for both JSON and ATOM format, the Web API only supports JSON. Every request should include the `Accept` header value of `application/json`, even when no response body is expected. Any error returned in the response will be returned as JSON. While your code should work even if this header isn't included, we recommend including it as a best practice  
  
The current OData version is 4.0, but future versions may allow for new capabilities. To ensure that there is no ambiguity about the OData version that will be applied to your code at that point in the future, you should always include an explicit statement of the current OData version and the maximum version to apply in your code. Use both `OData-Version` and `OData-MaxVersion` headers set to a value of `4.0`.  
 
Queries which expand collection-valued navigation properties may return cached data for those properties that don't reflect recent changes. Include `If-None-Match: null` header in the request body to override browser caching of Web API request. For more information see [Hypertext Transfer Protocol (HTTP/1.1): Conditional Requests 3.2 : If-None-Match](https://tools.ietf.org/html/rfc7232#section-3.2).

Every request that includes JSON data in the request body must include a `Content-Type` header with a value of `application/json`.  
  
```http
Content-Type: application/json  
```  
  
You can use additional headers to enable specific capabilities.  

### Prefer Headers

You can use the [Prefer](https://tools.ietf.org/html/rfc7240) header with the values below to specify preferences.


|Prefer value |Description |
|---------|---------|
|`return=representation`|Use this preference to return data on create (`POST`) or update (`PATCH`) operations for entities. When this preference is applied to a `POST` request, a successful response will have status `201 Created` . For a `PATCH` request, a successful response will have a status `200 OK.` Without this preference applied, both operations will return status `204 No Content` to reflect that no data is returned in the body of the response by default. More information: [Create with data returned](create-entity-web-api.md#create-with-data-returned) & [Update with data returned](update-delete-entities-using-web-api.md#update-with-data-returned)|
|`odata.include-annotations`|Use this preference with the value set to `OData.Community.Display.V1.FormattedValue` to return formatted values with a query. More information: [Include formatted values](query-data-web-api.md#bkmk_includeFormattedValues)<br /> You can also use this to specify additional error details that can be returned by a plug-in as described in [Include additional details with errors](#include-additional-details-with-errors) below.<br /> You can filter which annotations you want by including a wildcard character `*`, or you can specify to return all annotations using `Prefer: odata.include-annotations="*"`|
|`odata.maxpagesize`|Use this preference to specify how many pages you want to return in a query. More information: [Specify the number of rows to return in a page](query-data-web-api.md#bkmk_specifyNumber) |

### Other headers

|Header|Value|Description|
|---------|---------|---------|
|`CallerObjectId`|User Azure Active Directory Object Id|Use this header impersonate another user when the caller has the privileges to do so. Set the value to the Azure Active Directory Object Id of the user to impersonate. This data is in the [SystemUser table/entity](/reference/entities/systemuser) [AzureActiveDirectoryObjectId](/reference/entities/systemuser#BKMK_AzureActiveDirectoryObjectId) attribute (column). More information: [Impersonate another user using the Web API](impersonate-another-user-web-api.md)|
|`If-Match`|`Etag` value<br /> or `*`|Use this header to apply optimistic concurrency to ensure that you don't overwrite changes that someone else applied on the server since you retrieved a record. More information: [Apply optimistic concurrency](perform-conditional-operations-using-web-api.md#bkmk_Applyoptimisticconcurrency) & [If-Match](https://tools.ietf.org/html/rfc7232#section-3.1)<br /> You can also use this header with `*` to prevent a `PATCH` operation from creating a record. More information: [Prevent create in upsert](perform-conditional-operations-using-web-api.md#prevent-create-in-upsert)|
|`If-None-Match`|`null`<br /> or `*`|This header should be used in all requests with a value of `null` as described in [HTTP headers](#http-headers), but it can also be used to prevent a `POST` operation from performing an update. More information: [Prevent update in upsert](perform-conditional-operations-using-web-api.md#prevent-update-in-upsert) & [If-None-Match](https://tools.ietf.org/html/rfc7232#section-3.2)|
|`MSCRM.SolutionUniqueName`|solution unique name|Use this header when you want to create a solution component and have it associated with an unmanaged solution. More information: [Create and update table definitions using the Web API](create-update-entity-definitions-using-web-api.md)|
|`MSCRM.SuppressDuplicateDetection`|`false` |Use this header with the value `false` to enable duplicate detection when creating or updating a record. More information: [Check for Duplicate records](create-entity-web-api.md#check-for-duplicate-records)|
|`MSCRM.BypassCustomPluginExecution`|`true`|Use this header when you want to by-pass custom plug-in code and the caller has the `prvBypassCustomPlugins` privilege. More information: [Bypass Custom Business Logic](../bypass-custom-business-logic.md)|
|`Consistency`|`Strong`|Use this header when you must have the most recent version of a cached item. Cached items include: Metadata definitions, Labels, User permissions and team permissions. For example, if you apply a change to some metadata definition, label, or permission and you have code that must use the latest definition within 30 seconds of the change, you can use this header to ensure you get the latest version. This incurs a small performance penalty so it shouldn't be used all the time.|

When you execute batch operations, you must apply a number of different headers in the request and with each part sent in the body. More information: [Execute batch operations using the Web API](execute-batch-operations-using-web-api.md).
  
<a name="bkmk_statusCodes"></a>

## Identify status codes

 Whether an http request succeeds or fails, the response will include a status code. Status codes returned by the Microsoft Dataverse Web API include the following.  
  
|Code|Description|Type|  
|----------|-----------------|----------|  
|`200 OK`|Expect this when your operation will return data in the response body.|Success|  
|`201 Created`|Expect this when your entity POST operation succeeds and you have specified the `return=representation` preference in your request.|Success|  
|`204 No Content`|Expect this when your operation succeeds but does not return data in the response body.|Success|  
|`304 Not Modified`|Expect this when testing whether an entity has been modified since it was last retrieved. More information: [Conditional retrievals](perform-conditional-operations-using-web-api.md#bkmk_DetectIfChanged)|Redirection|  
|`403 Forbidden`|Expect this for the following types of errors:<br /><br /> -   AccessDenied<br />-   AttributePermissionReadIsMissing<br />-   AttributePermissionUpdateIsMissingDuringUpdate<br />-   AttributePrivilegeCreateIsMissing<br />-   CannotActOnBehalfOfAnotherUser<br />-   CannotAddOrActonBehalfAnotherUserPrivilege<br />-   CrmSecurityError<br />-   InvalidAccessRights<br />-   PrincipalPrivilegeDenied<br />-   PrivilegeCreateIsDisabledForOrganization<br />-   PrivilegeDenied<br />-   unManagedinvalidprincipal<br />-   unManagedinvalidprivilegeedepth|Client Error|  
|`401 Unauthorized`|Expect this for the following types of errors:<br /><br /> -   BadAuthTicket<br />-   ExpiredAuthTicket<br />-   InsufficientAuthTicket<br />-   InvalidAuthTicket<br />-   InvalidUserAuth<br />-   MissingCrmAuthenticationToken<br />-   MissingCrmAuthenticationTokenOrganizationName<br />-   RequestIsNotAuthenticated<br />-   TamperedAuthTicket<br />-   UnauthorizedAccess<br />-   UnManagedInvalidSecurityPrincipal|Client Error|  
|`413 Payload Too Large`|Expect this when the request length is too large.|Client Error|  
|`400 BadRequest`|Expect this when an argument is invalid.|Client Error|  
|`404 Not Found`|Expect this when the resource doesn't exist.|Client Error|  
|`405 Method Not Allowed`|This error occurs for incorrect method and resource combinations. For example, you can't use DELETE or PATCH on a collection of entities.<br /><br /> Expect this for the following types of errors:<br /><br /> -   CannotDeleteDueToAssociation<br />-   InvalidOperation<br />-   NotSupported|Client Error|  
|`412 Precondition Failed`|Expect this for the following types of errors:<br /><br /> -   ConcurrencyVersionMismatch<br />-   DuplicateRecord|Client Error|
|`429 Too Many Requests`|Expect this when API limits are exceeded. More information: [Service Protection API Limits](../api-limits.md)|Client Error|  
|`501 Not Implemented`|Expect this when some requested operation isn't implemented.|Server Error|  
|`503 Service Unavailable`|Expect this when the web API service isn't available.|Server Error|  
  
<a name="bkmk_parseErrors"></a>

## Parse errors from the response

Details about errors are included as JSON in the response. Errors will be in this format.  
  
```json  
{  
 "error":{  
  "code": "<This code is not related to the http status code and is frequently empty>",  
  "message": "<A message describing the error>"  
 }  
}  
```

### Include additional details with errors

Some errors can include additional details using *annotations*. When a request includes the `Prefer: odata.include-annotations="*"` header, the response will include all the annotations which will include additional details about errors and a URL that can be used to be directed to any specific guidance for the error.

Some of these details can be set by developers writing plug-ins. For example, let's say you have a plug-in that throws an error using the [InvalidPluginExecutionException(OperationStatus, Int32, String)](/dotnet/api/microsoft.xrm.sdk.invalidpluginexecutionexception.-ctor#Microsoft_Xrm_Sdk_InvalidPluginExecutionException__ctor_Microsoft_Xrm_Sdk_OperationStatus_System_Int32_System_String_) constructor. This allows you to pass an OperationStatus value, a custom integer error code, and an error message.

A simple plug-in might look like this:

```csharp
namespace MyNamespace
{
    public class MyClass : IPlugin
    {
        public void Execute(IServiceProvider serviceProvider)
        {

            // Obtain the tracing service
            ITracingService tracingService =
            (ITracingService)serviceProvider.GetService(typeof(ITracingService));

            tracingService.Trace("Entering MyClass plug-in.");

             try
            {
                throw new InvalidPluginExecutionException(OperationStatus.Canceled, 12345, "Example Error Message.");
            }
            catch (InvalidPluginExecutionException ex)
            {
                tracingService.Trace("StackTrace:");
                tracingService.Trace(ex.StackTrace);
                throw ex;
            }
        }
    }
}
```

When this plug-in is registered on the create of an account entity, and the request to create an account includes the `odata.include-annotations="*"` preference, the request and response will look like the following:

**Request**

```http
POST https://yourorg.api.crm.dynamics.com/api/data/v9.1/accounts HTTP/1.1
Content-Type: application/json;
Prefer: odata.include-annotations="*"
{
    "name":"Example Account"
}

```

**Response**

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json; odata.metadata=minimal
{
    "error": {
        "code": "0x80040265",
        "message": "Example Error Message.",
        "@Microsoft.PowerApps.CDS.ErrorDetails.OperationStatus": "1",
        "@Microsoft.PowerApps.CDS.ErrorDetails.SubErrorCode": "12345",
        "@Microsoft.PowerApps.CDS.HelpLink": "http://go.microsoft.com/fwlink/?LinkID=398563&error=Microsoft.Crm.CrmException%3a80040265&client=platform",
        "@Microsoft.PowerApps.CDS.TraceText": "\r\n[MyNamespace: MyNamespace.MyClass ]\r\n[52e2dbb9-85d3-ea11-a812-000d3a122b89: MyNamespace.MyClass : Create of account] \r\n\r\n Entering MyClass plug-in.\r\nStackTrace:\r\n   at MyNamespace.MyClass.Execute(IServiceProvider serviceProvider)\r\n\r\n"
        "@Microsoft.PowerApps.CDS.InnerError.Message": "Example Error Message."
    }
}
```

This response includes the following annotations:

|Annotation and Description  |Value  |
|---------|---------|
|`@Microsoft.PowerApps.CDS.ErrorDetails.OperationStatus`<br/>The value of the <xref:Microsoft.Xrm.Sdk.OperationStatus> set by the [InvalidPluginExecutionException(OperationStatus, Int32, String)](/dotnet/api/microsoft.xrm.sdk.invalidpluginexecutionexception.-ctor#Microsoft_Xrm_Sdk_InvalidPluginExecutionException__ctor_Microsoft_Xrm_Sdk_OperationStatus_System_Int32_System_String_) constructor.|`1`|
|`@Microsoft.PowerApps.CDS.ErrorDetails.SubErrorCode`<br/>The value of the `SubErrorCode` set by the [InvalidPluginExecutionException(OperationStatus, Int32, String)](/dotnet/api/microsoft.xrm.sdk.invalidpluginexecutionexception.-ctor#Microsoft_Xrm_Sdk_InvalidPluginExecutionException__ctor_Microsoft_Xrm_Sdk_OperationStatus_System_Int32_System_String_) constructor.|`12345`|
|`@Microsoft.PowerApps.CDS.HelpLink`<br/>A URL that contains information about the error which *may* re-direct you to guidance about how to address the error.|`http://go.microsoft.com/fwlink/?LinkID=398563&error=Microsoft.Crm.CrmException%3a80040265&client=platform`|
|`@Microsoft.PowerApps.CDS.TraceText`<br/>Content written to the Plug-in trace log using the [ITracingService.Trace(String, Object[]) Method](/dotnet/api/microsoft.xrm.sdk.itracingservice.trace). This includes the stacktrace for the plugin because the plug-in author logged it.|`[MyNamespace: MyNamespace.MyClass ]`<br/>`[52e2dbb9-85d3-ea11-a812-000d3a122b89: MyNamespace.MyClass :Create of account]`<br/><br/>`Entering MyClass plug-in.`<br/>`StackTrace:`<br/>`  at MyNamespace.MyClass.Execute(IServiceProvider serviceProvider)`|
|`@Microsoft.PowerApps.CDS.InnerError.Message`<br/>The error message found in the InnerError for the exception. This should be the same as the error message except in certain special cases that are for internal use only.|`Example Error Message.`|

> [!NOTE]
> The `@Microsoft.PowerApps.CDS.HelpLink` is not guaranteed to provide guidance for every error. Guidance *may* be provided proactively but most commonly it will be provided reactively based on how frequently the link is used. Please use the link. If it doesn't provide guidance, your use of the link helps us track that people need more guidance about the error. We can then prioritize including guidance to the errors that people need most. The resources that the link may direct you to may be documentation, links to community resources, or external sites.

If you do not want to receive all annotations in the response, you can specify which specific annotations you want to have returned. Rather than using `Prefer: odata.include-annotations="*"`, you can use the following to receive only formatted values for operations that retrieve data and the helplink if an error occurs:
`Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue,Microsoft.PowerApps.CDS.HelpLink"`.

## Add a Shared Variable from the Web API

You can set a string value that will be available to plug-ins within the ExecutionContext in the `SharedVariables` collection. More information: [Shared variables](../understand-the-data-context.md#shared-variables)

To pass this value using the Web API, simply use the `tag` query option.

For example: `?tag=This is a value passed.`

Will result in the following value within the `SharedVariables` collection when sent using a webhook.

```json
{
"key": "tag",
"value": "This is a value passed."
}
```
This can also be done using the Organization Service: [Add a Shared Variable from the Organization Service](../org-service/use-messages.md#add-a-shared-variable-from-the-organization-service)

### See also  

[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Query data using the Web API](query-data-web-api.md)<br />
[Create a table row using the Web API](create-entity-web-api.md)<br />
[Retrieve a table row using the Web API](retrieve-entity-using-web-api.md)<br />
[Update and delete table rows using the Web API](update-delete-entities-using-web-api.md)<br />
[Associate and disassociate table rows using the Web API](associate-disassociate-entities-using-web-api.md)<br />
[Use Web API functions](use-web-api-functions.md)<br />
[Use Web API actions](use-web-api-actions.md)<br />
[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)<br />
[Impersonate another user using the Web API](impersonate-another-user-web-api.md)<br />
[Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
