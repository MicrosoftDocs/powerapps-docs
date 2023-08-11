---
title: Compose HTTP requests and handle errors
description: Learn about the HTTP methods and headers that form a part of HTTP requests for the Web API and how to identify and handle errors returned in the response.
ms.topic: how-to
ms.date: 04/19/2023
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
ms.custom: bap-template
---

# Compose HTTP requests and handle errors

You interact with the Web API by composing and sending HTTP requests. You need to know how to set the appropriate HTTP headers and handle any errors included in the response.

<a name="bkmk_url_versions"></a>

## Web API URL and versions

To find the Web API URL for your environment:

1. Sign into [Power Apps](https://make.powerapps.com/), and then select your environment in the upper-right corner.
1. Select the **Settings** button in the upper-right corner, and then select **Developer resources**.

   :::image type="content" source="../media/dev-resources-menu.png" alt-text="Developer resources menu":::

   From here, you can copy the value for the **Web API endpoint**. More information: [View developer resources](../view-download-developer-resources.md)


The following table describes the parts of the URL:

|Part|Description|
|--|--|
|Protocol| `https://`|
|Environment Name|The unique name that applies to your environment. If your company name is *Contoso*, then it may be `contoso`.|
|Region|Your environment is usually in a data center that is close to you geographically. For North America, it's `crm`. For South America `crm2`, For Japan `crm7`. For the complete list, see [Datacenter regions](/power-platform/admin/new-datacenter-regions)|
|Base URL|This is usually `dynamics.com.`, but some data centers use different values. See [Datacenter regions](/power-platform/admin/new-datacenter-regions).|
|Web API path|The path to the web API is `/api/data/`.|
|Version|The version is expressed this way: `v[Major_version].[Minor_version][PatchVersion]/`. The current version is `v9.2`.|
|Resource|The `EntitySetName` of the table, or the name of the function or action you want to use.|

The URL you use is made up of these parts:

Protocol + Environment Name + Region + Base URL + Web API path + Version + Resource.


<a name="version_compatiblity"></a>

### Version compatibility

This release introduces capabilities that aren't available in previous versions. Subsequent minor versions may provide more capabilities that won't be retroactively added to earlier minor versions. Your code written for v9.0 will continue to work in future versions when you reference v9.0 in your URL.

As new capabilities are introduced, they may conflict with earlier versions. These breaking changes are necessary to allow the service to become better. Most of the time, capabilities will remain the same between versions but you shouldn't assume they will.

> [!NOTE]
> Unlike the v8.x minor releases, new capabilities or other changes added to future versions won't be applied to earlier versions.
> Pay attention to the version of the service you use and test your code if you change the version used.

<a name="bkmk_methods"></a>

## HTTP methods

The following table lists the HTTP methods you can use with the Dataverse Web API.  
  
|Method|Usage|
|------------|-----------|
|`GET`|Use when retrieving data, including calling functions. The expected Status Code for a successful retrieve is `200 OK`.|
|`POST`|Use when creating entities or calling actions.|
|`PATCH`|Use when updating entities or performing upsert operations.|
|`DELETE`|Use when deleting entities or individual properties of entities.|
|`PUT`|Use in limited situations to update individual properties of entities. This method isn't recommended when updating most entities. Use `PUT` when updating table definitions. More information: [Use the Web API with table definitions](use-web-api-metadata.md)|
  
<a name="bkmk_headers"></a>

## HTTP headers

All HTTP requests should include at least the following headers.  
  
```http
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-None-Match: null
```  

Although the OData protocol allows for both JSON and ATOM format, the Web API only supports JSON. Every request should include the `Accept` header value of `application/json`, even when no response body is expected. Any error returned in the response is returned as JSON. While your code should work even if this header isn't included, we recommend including it as a best practice  
  
The current OData version is 4.0, but future versions may allow for new capabilities. To ensure that there's no ambiguity about the OData version that will be applied to your code in the future, you should always include an explicit statement of the current OData version and the maximum version to apply in your code. Use both `OData-Version` and `OData-MaxVersion` headers set to a value of `4.0`.  
 
Queries that expand collection-valued navigation properties may return cached data for those properties that don't reflect recent changes. Include `If-None-Match: null` header in the request body to override browser caching of Web API request. More information: [Hypertext Transfer Protocol (HTTP/1.1): Conditional Requests 3.2 : If-None-Match](https://tools.ietf.org/html/rfc7232#section-3.2).

Every request that includes JSON data in the request body must include a `Content-Type` header with a value of `application/json`.  
  
```http
Content-Type: application/json  
```  
  
You can use other headers to enable specific capabilities.  

### Prefer Headers

You can use the [Prefer](https://www.rfc-editor.org/rfc/rfc7240) header with the values below to specify preferences.


|Prefer value |Description |
|---------|---------|
|`return=representation`|Use this preference to return data on create (`POST`) or update (`PATCH`) operations for entities. When this preference is applied to a `POST` request, a successful response has status `201 Created` . For a `PATCH` request, a successful response has a status `200 OK.` Without this preference applied, both operations return status `204 No Content` to reflect that no data is returned in the body of the response by default. More information: [Create with data returned](create-entity-web-api.md#create-with-data-returned) & [Update with data returned](update-delete-entities-using-web-api.md#update-with-data-returned)|
|`odata.include-annotations`|See [Request annotations](#request-annotations)|
|`odata.maxpagesize`|Use this preference to specify how many pages you want to return in a query. More information: [Page results](query-data-web-api.md#page-results) |
|`odata.track-changes`|The change tracking feature allows you to keep the data synchronized in an efficient manner by detecting what data has changed since the data was initially extracted or last synchronized. More information: [Use change tracking to synchronize data with external systems](../use-change-tracking-synchronize-data-external-systems.md)|
|`respond-async`|Specifies that the request should be processed asynchronously. More information: [Background operations (preview)](../background-operations.md)|

> [!NOTE]
> Multiple Prefer headers can be specified using comma-separated values; for example:
> `Prefer: respond-async,odata.include-annotations="*"`


#### Request annotations

You can request different OData annotation data to be returned with the results using the `Prefer: odata.include-annotations` request header. You can choose to return all annotations, or specify specific annotations. The following table describes the annotations Dataverse Web API supports:


|Annotation|Description|
|---------|---------|
|`OData.Community.Display.V1.FormattedValue`| Returns formatted string values you can use in your application. More information: [Formatted values](query-data-web-api.md#formatted-values)|
|`Microsoft.Dynamics.CRM.associatednavigationproperty`<br />`Microsoft.Dynamics.CRM.lookuplogicalname`|Returns information about related lookup columns. More information:  [Lookup property data](query-data-web-api.md#lookup-property-data)|
|`Microsoft.Dynamics.CRM.totalrecordcount`<br />`Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded`|When you use the `$count` query option the `@odata.count` annotation tells the number of records, but only 5,000 records can be returned at a time. Request the `Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded` to get a boolean value that will tell you if the total number of records matching the query exceeds 5,000.  More information: [Count number of rows](query-data-web-api.md#count-number-of-rows) |
|`Microsoft.Dynamics.CRM.globalmetadataversion`|This annotation is returned on the request and you can cache it in your application. The value changes when any schema change occurs, indicating that you may need to refresh any schema data that your application has cached. More information: [Cache Schema data](../cache-schema-data.md)|
|`Microsoft.PowerApps.CDS.ErrorDetails.OperationStatus`<br />`Microsoft.PowerApps.CDS.ErrorDetails.SubErrorCode`<br />`Microsoft.PowerApps.CDS.HelpLink`<br />`Microsoft.PowerApps.CDS.TraceText`<br />`Microsoft.PowerApps.CDS.InnerError.Message`|These annotations provide more details when errors are returned. More information: [Include more details with errors](#include-more-details-with-errors)|

If you want only specific annotations, you can request them as comma-separated values. You can also use the '`*`' character as a wildcard.  For example, the following `Prefer` request header only includes the formatted values and any additional error detail annotations:

```
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue,Microsoft.PowerApps.CDS.ErrorDetails*"
```

> [!TIP]
> It's common to simply use the `Prefer: odata.include-annotations="*"` request header to return all annotations.

### Other headers

|Header|Value|Description|
|---------|---------|---------|
|`CallerObjectId`|User Azure Active Directory Object ID|Use this header to impersonate another user when the caller has the privileges to do so. Set the value to the Azure Active Directory Object ID of the user to impersonate. This data is in the [User (SystemUser) table/entity](../reference/entities/systemuser.md) [AzureActiveDirectoryObjectId](../reference/entities/systemuser.md#BKMK_AzureActiveDirectoryObjectId) attribute (column). More information: [Impersonate another user using the Web API](impersonate-another-user-web-api.md)|
|`If-Match`|`Etag` value<br /> or `*`|Use this header to apply optimistic concurrency to ensure that you don't overwrite changes that someone else applied on the server since you retrieved a record. More information: [Apply optimistic concurrency](perform-conditional-operations-using-web-api.md#bkmk_Applyoptimisticconcurrency) and [If-Match](https://tools.ietf.org/html/rfc7232#section-3.1)<br /> You can also use this header with `*` to prevent a `PATCH` operation from creating a record. More information: [Prevent create in upsert](perform-conditional-operations-using-web-api.md#prevent-create-in-upsert)|
|`If-None-Match`|`null`<br /> or `*`|This header should be used in all requests with a value of `null` as described in [HTTP headers](#http-headers), but it can also be used to prevent a `POST` operation from performing an update. More information: [Prevent update in upsert](perform-conditional-operations-using-web-api.md#prevent-update-in-upsert) and [If-None-Match](https://tools.ietf.org/html/rfc7232#section-3.2)|
|`MSCRM.SolutionUniqueName`|solution unique name|Use this header when you want to create a solution component and have it associated with an unmanaged solution. More information: [Create and update table definitions using the Web API](create-update-entity-definitions-using-web-api.md)|
|`MSCRM.SuppressDuplicateDetection`|`false` |Use this header with the value `false` to enable duplicate detection when creating or updating a record. More information: [Check for Duplicate records](create-entity-web-api.md#check-for-duplicate-records)|
|`MSCRM.BypassCustomPluginExecution`|`true`|Use this header when you want to by-pass custom plug-in code and the caller has the `prvBypassCustomPlugins` privilege. More information: [Bypass Custom Business Logic](../bypass-custom-business-logic.md)|
|`Consistency`|`Strong`|Use this header when you must have the most recent version of a cached item. Cached items include metadata definitions, labels, user permissions, and team permissions. For example, if you apply a change to some metadata definition, label, or permission and you have code that must use the latest definition within 30 seconds of the change, use this header to ensure you get the latest version. Using this header incurs a small performance penalty, so it shouldn't be used all the time.|

When you execute batch operations, you must apply many different headers in the request and with each part sent in the body. More information: [Execute batch operations using the Web API](execute-batch-operations-using-web-api.md).
  
<a name="bkmk_statusCodes"></a>

## Identify status codes

 Whether an HTTP request succeeds or fails, the response includes a status code. The following table describes the status codes returned by the Microsoft Dataverse Web API.  
  
|Code|Description|Type|  
|----------|-----------------|----------|  
|`200 OK`|Expect this status code when your operation returns data in the response body.|Success|  
|`201 Created`|Expect this status code when your entity POST operation succeeds and you've specified the `return=representation` preference in your request.|Success|  
|`204 No Content`|Expect this status code when your operation succeeds but doesn't return data in the response body.|Success|  
|`304 Not Modified`|Expect this status code when testing whether an entity has been modified since it was last retrieved. More information: [Conditional retrievals](perform-conditional-operations-using-web-api.md#bkmk_DetectIfChanged)|Redirection|  
|`403 Forbidden`|Expect this  status code for the following types of errors:<br /><br />- `AccessDenied`<br />- `AttributePermissionReadIsMissing`<br />- `AttributePermissionUpdateIsMissingDuringUpdate`<br />- `AttributePrivilegeCreateIsMissing`<br />-   `CannotActOnBehalfOfAnotherUser`<br />- `CannotAddOrActonBehalfAnotherUserPrivilege`<br />- `CrmSecurityError`<br />- `InvalidAccessRights`<br />- `PrincipalPrivilegeDenied`<br />- `PrivilegeCreateIsDisabledForOrganization`<br />- `PrivilegeDenied`<br />- `unManagedinvalidprincipal`<br />- `unManagedinvalidprivilegeedepth`|Client Error|  
|`401 Unauthorized`|Expect this status code for the following types of errors:<br /><br />- `BadAuthTicket`<br />- `ExpiredAuthTicket`<br />-   `InsufficientAuthTicket`<br />- `InvalidAuthTicket`<br />- `InvalidUserAuth`<br />- `MissingCrmAuthenticationToken`<br />- `MissingCrmAuthenticationTokenOrganizationName`<br />- `RequestIsNotAuthenticated`<br />- `TamperedAuthTicket`<br />- `UnauthorizedAccess`<br />-   `UnManagedInvalidSecurityPrincipal`|Client Error|  
|`413 Payload Too Large`|Expect this  status code when the request length is too large.|Client Error|  
|`400 BadRequest`|Expect this  status code when an argument is invalid.|Client Error|  
|`404 Not Found`|Expect this  status code when the resource doesn't exist.|Client Error|  
|`405 Method Not Allowed`|This error occurs for incorrect method and resource combinations. For example, you can't use DELETE or PATCH on a collection of entities.<br /><br /> Expect this for the following types of errors:<br /><br />- `CannotDeleteDueToAssociation`<br />-   `InvalidOperation`<br />- `NotSupported`|Client Error|  
|`412 Precondition Failed`|Expect this  status code for the following types of errors:<br /><br />- `ConcurrencyVersionMismatch`<br />-   `DuplicateRecord`|Client Error|
|`429 Too Many Requests`|Expect this  status code when API limits are exceeded. More information: [Service Protection API Limits](../api-limits.md)|Client Error|  
|`501 Not Implemented`|Expect this  status code when some requested operation isn't implemented.|Server Error|  
|`503 Service Unavailable`|Expect this  status code when the web API service isn't available.|Server Error|  
  
<a name="bkmk_parseErrors"></a>

## Parse errors from the response

Details about errors are included as JSON in the response in the following format.  
  
```json  
{  
 "error":{  
  "code": "<This code is not related to the http status code and is frequently empty>",  
  "message": "<A message describing the error>"  
 }  
}  
```

### Include more details with errors

Some errors can include more details using *annotations*. When a request includes the `Prefer: odata.include-annotations="*"` header, the response includes all the annotations that contain more details about errors and a URL that may direct you to specific guidance for the error.

Some of these details can be set by developers writing plug-ins. For example, let's say you have a plug-in that throws an error using the [InvalidPluginExecutionException(OperationStatus, Int32, String)](/dotnet/api/microsoft.xrm.sdk.invalidpluginexecutionexception.-ctor#Microsoft_Xrm_Sdk_InvalidPluginExecutionException__ctor_Microsoft_Xrm_Sdk_OperationStatus_System_Int32_System_String_) constructor. This constructor allows you to pass an OperationStatus value, a custom integer error code, and an error message.

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

When this plug-in is registered on the Create message of an account entity, and the request to create an account includes the `odata.include-annotations="*"` preference, the request and response look like the following example:

**Request:**

```http
POST https://yourorg.api.crm.dynamics.com/api/data/v9.1/accounts HTTP/1.1
Content-Type: application/json;
Prefer: odata.include-annotations="*"
{
    "name":"Example Account"
}

```

**Response:**

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

The following table describes the annotation in the response.

|Annotation and description|Value|
|---------|---------|
|`@Microsoft.PowerApps.CDS.ErrorDetails.OperationStatus`<br/>The value of the <xref:Microsoft.Xrm.Sdk.OperationStatus> set by the [InvalidPluginExecutionException(OperationStatus, Int32, String)](/dotnet/api/microsoft.xrm.sdk.invalidpluginexecutionexception.-ctor#Microsoft_Xrm_Sdk_InvalidPluginExecutionException__ctor_Microsoft_Xrm_Sdk_OperationStatus_System_Int32_System_String_) constructor.|`1`|
|`@Microsoft.PowerApps.CDS.ErrorDetails.SubErrorCode`<br/>The value of the `SubErrorCode` set by the [InvalidPluginExecutionException(OperationStatus, Int32, String)](/dotnet/api/microsoft.xrm.sdk.invalidpluginexecutionexception.-ctor#Microsoft_Xrm_Sdk_InvalidPluginExecutionException__ctor_Microsoft_Xrm_Sdk_OperationStatus_System_Int32_System_String_) constructor.|`12345`|
|`@Microsoft.PowerApps.CDS.HelpLink`<br/>A URL that contains information about the error that *may* redirect you to guidance about how to address the error.|`http://go.microsoft.com/fwlink/?LinkID=398563&error=Microsoft.Crm.CrmException%3a80040265&client=platform`|
|`@Microsoft.PowerApps.CDS.TraceText`<br/>Content written to the plug-in trace log using the [ITracingService.Trace(String, Object[]) Method](/dotnet/api/microsoft.xrm.sdk.itracingservice.trace). This annotation includes the stacktrace for the plug-in because the plug-in author logged it.|`[MyNamespace: MyNamespace.MyClass ]`<br/>`[52e2dbb9-85d3-ea11-a812-000d3a122b89: MyNamespace.MyClass :Create of account]`<br/><br/>`Entering MyClass plug-in.`<br/>`StackTrace:`<br/>`  at MyNamespace.MyClass.Execute(IServiceProvider serviceProvider)`|
|`@Microsoft.PowerApps.CDS.InnerError.Message`<br/>The error message found in the InnerError for the exception. This message should be the same as the error message except in certain special cases that are for internal use only.|`Example Error Message.`|

> [!NOTE]
> The `@Microsoft.PowerApps.CDS.HelpLink` isn't guaranteed to provide guidance for every error. Guidance *may* be provided proactively but most commonly it's provided reactively based on how frequently the link is used. Use the link. If it doesn't provide guidance, your use of the link helps us track that people need more guidance about the error. We can then prioritize including guidance to the errors that people need most. The resources that the link may direct you to may be documentation, links to community resources, or external sites.

If you don't want to receive all annotations in the response, you can specify which annotations you want to have returned. Rather than using `Prefer: odata.include-annotations="*"`, you can use the following value to receive only formatted values for operations that retrieve data and the help link if an error occurs:
`Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue,Microsoft.PowerApps.CDS.HelpLink"`.

More information: [Request annotations](#request-annotations)

## Add a shared variable from the Web API

You can set a string value that is available to plug-ins within the ExecutionContext in the `SharedVariables` collection. More information:

- [Add a shared variable to the plugin execution context](../optional-parameters.md#add-a-shared-variable-to-the-plugin-execution-context)
- [Shared variables](../understand-the-data-context.md#shared-variables)


### See also  

[Perform operations using the Web API](perform-operations-web-api.md)   
[Query data using the Web API](query-data-web-api.md)   
[Create a table row using the Web API](create-entity-web-api.md)   
[Retrieve a table row using the Web API](retrieve-entity-using-web-api.md)   
[Update and delete table rows using the Web API](update-delete-entities-using-web-api.md)   
[Associate and disassociate table rows using the Web API](associate-disassociate-entities-using-web-api.md)   
[Use Web API functions](use-web-api-functions.md)   
[Use Web API actions](use-web-api-actions.md)   
[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)   
[Impersonate another user using the Web API](impersonate-another-user-web-api.md)   
[Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
