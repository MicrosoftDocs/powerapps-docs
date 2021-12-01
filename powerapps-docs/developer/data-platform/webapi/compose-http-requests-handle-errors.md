---
title: "Compose HTTP requests and handle errors (Microsoft Dataverse)| Microsoft Docs"
description: "Read about the HTTP methods and headers that form a part of HTTP requests for the Web API, and then learn how to identify and handle errors returned in the response"
ms.custom: ""
ms.date: 10/15/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 64a39182-25de-4d31-951c-852025a75811
caps.latest.revision: 13
author: "JimDaly" # GitHub ID
ms.author: "pehecke"
ms.reviewer: "pehecke"
manager: "sunilg"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Compose HTTP requests and handle errors

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

You interact with the Web API by composing and sending HTTP requests. You need to know how to set the appropriate HTTP headers and handle any errors included in the response.  

<a name="bkmk_url_versions"></a>

## Web API URL and versions

To access the Web API you must compose a URL using the parts in the following table.

|Part|Description|
|--|--|
|Protocol| `https://`|
|Environment Name|The unique name that applies to your environment. If your company name is *Contoso*, then it may be `contoso`.|
|Region|Your environment will usually be available in a data center that is close to you geographically.<br />North America: `crm`<br />South America: `crm2`<br />Canada: `crm3`<br />Europe, Middle East and Africa (EMEA): `crm4`<br />Asia Pacific Area (APAC): `crm5`<br />Oceania: `crm6`<br />Japan: `crm7`<br />India: `crm8`<br />North America 2: `crm9`<br />United Kingdom: `crm11`<br />France: `crm12`<br />More values will be added over time as new data center regions are opened.|
|Base URL|`dynamics.com.`|
|Web API path|The path to the web API is `/api/data/`.|
|Version|    The version is expressed this way: `v[Major_version].[Minor_version][PatchVersion]/`. The valid version for this release is `v9.1`.|
|Resource|The name of the entity (table), function, or action you want to use.|

The URL you will use will be composed with these parts: Protocol + Environment Name + Region + Base URL + Web API path + Version + Resource. You can find these values mentioned in the above table by navigating your browser to the Power Apps [portal](https://make.powerapps.com), selecting the settings (gear) icon in the top toolbar, and choosing **Developer resources** in the menu.

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
|GET|Use when retrieving data, including calling functions. The expected Status Code for a successful retrieve is 200 OK.|  
|POST|Use when creating entities or calling actions.|  
|PATCH|Use when updating entities or performing upsert operations.|  
|DELETE|Use when deleting entities or individual properties of entities.|  
|PUT|Use in limited situations to update individual properties of entities. This method isn't recommended when updating most entities. You'll use this when updating table definitions.|  
  
<a name="bkmk_headers"></a>

## HTTP headers

Although the OData protocol allows for both JSON and ATOM format, the web API only supports JSON. Therefore the following headers can be applied.  
  
Every request should include the `Accept` header value of `application/json`, even when no response body is expected. Any error returned in the response will be returned as JSON. While your code should work even if this header isn't included, we recommend including it as a best practice  
  
The current OData version is 4.0, but future versions may allow for new capabilities. To ensure that there is no ambiguity about the OData version that will be applied to your code at that point in the future, you should always include an explicit statement of the current OData version and the Maximum version to apply in your code. Use both `OData-Version` and `OData-MaxVersion` headers set to a value of `4.0`.  
 
Queries which expand collection-valued navigation properties may return cached data for those properties that doesn't reflect recent changes. Include `If-None-Match: null` header in the request body to override browser caching of Web API request. For more information see [Hypertext Transfer Protocol (HTTP/1.1): Conditional Requests 3.2 : If-None-Match](https://tools.ietf.org/html/rfc7232#section-3.2).
 
All HTTP requests should include at least the following headers.  
  
```
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-None-Match: null
```  
  
Every request that includes JSON data in the request body must include a `Content-Type` header with a value of `application/json`.  
  
```  
Content-Type: application/json  
```  
  
You can use additional headers to enable specific capabilities.  
  
-   To return data on create (POST) or update (PATCH) operations for entities, include the `return=representation` preference. When this preference is applied to a POST request, a successful response will have status 201 (Created) . For a PATCH request, a successful response will have a status 200 (OK). Without this preference applied, both operations will return status 204 (No Content) to reflect that no data is returned in the body of the response by default.  
  
-   To return formatted values with a query, include the odata.include-annotations preference set to `Microsoft.Dynamics.CRM.formattedvalue` using the [Prefer](https://tools.ietf.org/html/rfc7240) header. More information:[Include formatted values](query-data-web-api.md#bkmk_includeFormattedValues)  
  
-   You also use the `Prefer` header with the `odata.maxpagesize` option to specify how many pages you want to return. More information:[Specify the number of tables (entities) to return in a page](query-data-web-api.md#bkmk_specifyNumber)  
  
-   To impersonate another user when the caller has the privileges to do so, add the `CallerObjectId` header with the user's Azure Active Directory Object Id value of the user to impersonate. This data is in the [SystemUser table/entity](/reference/entities/systemuser) [AzureActiveDirectoryObjectId](/reference/entities/systemuser#BKMK_AzureActiveDirectoryObjectId) attribute (column). More information:[Impersonate another user using the Web API](impersonate-another-user-web-api.md).  
  
-   To apply optimistic concurrency, you can apply the [If-Match](https://tools.ietf.org/html/rfc7232#section-3.1) header with an `Etag` value. More information:[Apply optimistic concurrency](perform-conditional-operations-using-web-api.md#bkmk_Applyoptimisticconcurrency).  
  
-   To control whether an upsert operation should actually create or update an entity, you can also use the `If-Match` and [If-None-Match](https://tools.ietf.org/html/rfc7232#section-3.2) headers. More information:[Upsert a table (entity)](update-delete-entities-using-web-api.md#bkmk_upsert).  
  
-   When you execute batch operations, you must apply a number of different headers in the request and with each part sent in the body. More information: [Execute batch operations using the Web API](execute-batch-operations-using-web-api.md).  

- When you create a solution component and want to associate it with a solution, use the `MSCRM.SolutionUniqueName` request header and set the value to the unique name of the solution.

- When you want to enable duplicate detection when creating a new entity record, set the `MSCRM.SuppressDuplicateDetection` request header value to false. More information: [Check for Duplicate records](create-entity-web-api.md#check-for-duplicate-records)

- When you want to by-pass custom plug-in code and the caller has the `prvBypassCustomPlugins` privilege, set the `MSCRM.BypassCustomPluginExecution` request header to `true`. More information: [Bypass Custom Business Logic](../bypass-custom-business-logic.md)
  
<a name="bkmk_statusCodes"></a>

## Identify status codes

 Whether an http request succeeds or fails, the response will include a status code. Status codes returned by the Microsoft Dataverse Web API include the following.  
  
|Code|Description|Type|  
|----------|-----------------|----------|  
|200 OK|Expect this when your operation will return data in the response body.|Success|  
|201 Created|Expect this when your entity POST operation succeeds and you have specified the `return=representation` preference in your request.|Success|  
|204 No Content|Expect this when your operation succeeds but does not return data in the response body.|Success|  
|304 Not Modified|Expect this when testing whether an entity has been modified since it was last retrieved. More information: [Conditional retrievals](perform-conditional-operations-using-web-api.md#bkmk_DetectIfChanged)|Redirection|  
|403 Forbidden|Expect this for the following types of errors:<br /><br /> -   AccessDenied<br />-   AttributePermissionReadIsMissing<br />-   AttributePermissionUpdateIsMissingDuringUpdate<br />-   AttributePrivilegeCreateIsMissing<br />-   CannotActOnBehalfOfAnotherUser<br />-   CannotAddOrActonBehalfAnotherUserPrivilege<br />-   CrmSecurityError<br />-   InvalidAccessRights<br />-   PrincipalPrivilegeDenied<br />-   PrivilegeCreateIsDisabledForOrganization<br />-   PrivilegeDenied<br />-   unManagedinvalidprincipal<br />-   unManagedinvalidprivilegeedepth|Client Error|  
|401 Unauthorized|Expect this for the following types of errors:<br /><br /> -   BadAuthTicket<br />-   ExpiredAuthTicket<br />-   InsufficientAuthTicket<br />-   InvalidAuthTicket<br />-   InvalidUserAuth<br />-   MissingCrmAuthenticationToken<br />-   MissingCrmAuthenticationTokenOrganizationName<br />-   RequestIsNotAuthenticated<br />-   TamperedAuthTicket<br />-   UnauthorizedAccess<br />-   UnManagedInvalidSecurityPrincipal|Client Error|  
|413 Payload Too Large|Expect this when the request length is too large.|Client Error|  
|400 BadRequest|Expect this when an argument is invalid.|Client Error|  
|404 Not Found|Expect this when the resource doesn't exist.|Client Error|  
|405 Method Not Allowed|This error occurs for incorrect method and resource combinations. For example, you can't use DELETE or PATCH on a collection of entities.<br /><br /> Expect this for the following types of errors:<br /><br /> -   CannotDeleteDueToAssociation<br />-   InvalidOperation<br />-   NotSupported|Client Error|  
|412 Precondition Failed|Expect this for the following types of errors:<br /><br /> -   ConcurrencyVersionMismatch<br />-   DuplicateRecord|Client Error|
|429 Too Many Requests|Expect this when API limits are exceeded. More information: [Service Protection API Limits](../api-limits.md)|Client Error|  
|501 Not Implemented|Expect this when some requested operation isn't implemented.|Server Error|  
|503 Service Unavailable|Expect this when the web API service isn't available.|Server Error|  
  
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

> [!IMPORTANT]
> The structure of the error messages is changing. This change is expected to be deployed to different regions over a period starting in August through October 2020.
> 
> Before this change, the errors returned were in this format:
> 
> ```json  
> {  
>  "error":{  
>   "code": "<This code is not related to the http status code and is frequently empty>",  
>   "message": "<A message describing the error>",  
>   "innererror": {  
>    "message": "<A message describing the error, this is frequently the same as the outer message>",  
>    "type": "Microsoft.Crm.CrmHttpException",  
>    "stacktrace": "<Details from the server about where the error occurred>"  
>   }  
>  }  
> }  
> ```
> 
> We are removing the `innererror` property of the error message. You should remove any code that expects to parse this property.
>
> The OData [Error Response guidance](https://docs.oasis-open.org/odata/odata-json-format/v4.0/os/odata-json-format-v4.0-os.html#_Toc372793091) states "*The innererror name/value pair SHOULD only be used in development environments in order to guard against potential security concerns around information disclosure.*". To align with this guidance we are removing this property.
> 
> If you find that an application you use has a dependency on this property after this change is deployed, you can contact support and request that the change be temporarily removed for your environment. This will provide time for the application developer to make appropriate changes to remove this dependency.

### Include additional details with errors

Some errors can include additional details using *annotations*. When a request includes the `Prefer: odata.include-annotations="*"` header, the response will include all the annotations which will include additional details about errors and a URL that can be used to be directed to any specific guidance for the error.

Some of these details can be set by developers writing plug-ins. For example, let’s say you have a plug-in that throws an error using the [InvalidPluginExecutionException(OperationStatus, Int32, String)](/dotnet/api/microsoft.xrm.sdk.invalidpluginexecutionexception.-ctor#Microsoft_Xrm_Sdk_InvalidPluginExecutionException__ctor_Microsoft_Xrm_Sdk_OperationStatus_System_Int32_System_String_) constructor. This allows you to pass an OperationStatus value, a custom integer error code, and an error message.

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
[Create a table (entity) using the Web API](create-entity-web-api.md)<br />
[Retrieve a table (entity) using the Web API](retrieve-entity-using-web-api.md)<br />
[Update and delete tables (entities) using the Web API](update-delete-entities-using-web-api.md)<br />
[Associate and disassociate tables (entities) using the Web API](associate-disassociate-entities-using-web-api.md)<br />
[Use Web API functions](use-web-api-functions.md)<br />
[Use Web API actions](use-web-api-actions.md)<br />
[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)<br />
[Impersonate another user using the Web API](impersonate-another-user-web-api.md)<br />
[Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
