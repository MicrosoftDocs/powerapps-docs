---
title: Compose HTTP requests and handle errors for the portals Web API | Microsoft Docs
description: Learn how to construct HTTP requests, headers, and handle errors for the portals Web API.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 07/16/2020
ms.author: nenandw
ms.reviewer: tapanm
---

# Compose HTTP requests and handle errors for the portals Web API (Preview)

[This article is pre-release documentation and is subject to change.]

Interacting with the Web API includes composing HTTP requests with required headers and handling HTTP responses, including any errors.

> [!IMPORTANT]
> - **Your portal version must be 9.2.6.41 or later for this feature to work.**
> - This feature is in preview. More information: [Understand experimental, preview, and deprecated features in Power Apps](../canvas-apps/working-with-experimental-preview.md)

## Web API URL and versioning

Construct the Web API URL by using the format in the following table.

| Part | Description |
| - | - |
| Protocol | https://                                 |
| Base URL | \<portal URL\>                          |
| Web API Path | \_api                                    |
| Resource     | Name of the entity you want to use |

For example, use this format when referring a case:

`https://contoso.powerappsportals.com/_api/case`

All Web API resources will follow the respective [portal entity permissions](https://docs.microsoft.com/dynamics365/portals/assign-entity-permissions) in context with Web Roles.

## HTTP methods

HTTP requests can use different kinds of methods. However, the portals Web API only supports the methods in the following table.

| Method | Usage |
| - | - |
| Post   | Creating entities and calling actions. |
| Patch  | Use when updating entities or doing upsert operations. |
| Delete | Use when deleting entities or individual properties of entities. |
| Put    | Use in limited situations to update individual properties of entities. |

## HTTP headers

The Web API only supports JSON. Each HTTP header must include:

- An *Accept* header value of *application/json*, even when no response body is expected.
- If the request includes JSON data in the request body, you must include a
*Content-Type* header with a value of `application/json`.

The current OData version is 4.0, but future versions might allow for new capabilities. Use the following syntax to ensure that there's no ambiguity about the OData version that will be applied to your code in the future.

### Syntax

```http
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
```

### Example: Wrapper AJAX function for the CSRF token

```javascript
	(function(webapi, $){
		function safeAjax(ajaxOptions) {
			var deferredAjax = $.Deferred();
	
			shell.getTokenDeferred().done(function (token) {
				// add headers for ajax
				if (!ajaxOptions.headers) {
					$.extend(ajaxOptions, {
						headers: {
							"__RequestVerificationToken": token
						}
					}); 
				} else {
					ajaxOptions.headers["__RequestVerificationToken"] = token;
				}
				$.ajax(ajaxOptions)
					.done(function(data, textStatus, jqXHR) {
						validateLoginSession(data, textStatus, jqXHR, deferredAjax.resolve);
					}).fail(deferredAjax.reject); //ajax
			}).fail(function () {
				deferredAjax.rejectWith(this, arguments); // on token failure, pass the token ajax and args
			});
	
			return deferredAjax.promise();	
		}
		webapi.safeAjax = safeAjax;
})(window.webapi = window.webapi || {}, jQuery)
```

### Example: Create entity data

```javascript
	webapi.safeAjax({
		type: "POST",
		url: "/_api/accounts",
		contentType: "application/json",
		data: JSON.stringify({
			"name": "Sample Account"
		}),
		success: function (res, status, xhr) {
			console.log("entityID: "+ xhr.getResponseHeader("entityid"))
		}
	});
```

### Example: Update entity data

```javascript
		webapi.safeAjax({
		type: "PATCH",
		url: "/_api/accounts(00000000-0000-0000-0000-000000000001)",
		contentType: "application/json",
		data: JSON.stringify({
			"name": "Sample Account - Updated"
		}),
		success: function (res) {
			console.log(res);
		}
	});
```

### Example: Delete entity data

```javascript
		webapi.safeAjax({
		type: "DELETE",
		url: "/_api/accounts(00000000-0000-0000-0000-000000000001)",
		contentType: "application/json",
		success: function (res) {
			console.log(res);
		}
	});
```

## Identify status codes

Each HTTP request response includes a status code. Status codes returned by the portals Web API include the following.

| Code | Description | Type |
| - | - | - |
| 200 OK | Expect this response when your operation will return data in the response body. | Success |
| 204 No Content | Expect this response when your operation succeeds, but doesn't return data in the response body. | Success |
| 403 Forbidden | Expect this response for the following types of errors: <ul><li>AccessDenied</li><li>AttributePermissionIsMissing</li><li>EntityPermissionWriteIsMissingDuringUpdate</li><li>EntityPermissionCreateIsMissing</li><li>EntityPermissionDeleteIsMissing</li><li>EntityPermissionAppendIsMissngDuringAssociationChange</li><li>EntityPermissionAppendToIsMissingDuringAssociateChange</li></ul> | Client error |
| 401 Unauthorized | Expect this response for the following types of errors:<ul><li>MissingPortalRequestVerificationToken </li><li>MissingPortalSessionCookie</li></ul> | Client error |
| 413 Payload Too Large | Expect this response when the request length is too large. | Client error |
| 400 BadRequest | Expect this response when an argument is invalid. <br> InvalidAttribute | Client error |
| 404 Not Found | Expect this response when the resource doesn't exist. <br>The entity isn't exposed for the Web API. | Client Error |
| 405 Method Not Allowed | This error occurs for incorrect method and resource combinations. For example, you can't use DELETE or PATCH on a collection of entities. This situation can happen for the following types of errors:<ul><li>InvalidOperation</li><li>NotSupported</li></ul> | Client error |
| 501 Not Implemented | Expect this response when some requested operation isn't implemented. | Server error |
| 503 Service Unavailable | Expect this response when the Web API service isn't available. | Server error |

## Parse errors from the response

Consider the following example HTTP response that still includes the inner error.

```json
{
  "error":{
    "code": "This code is not related to the http status code and is frequently empty",
    "message": "A message describing the error",
    "cdscode": "Dataverse error code",
    "innererror": {
        "code": "800xxxx",
        "message": "A message describing the error. This is frequently the same as the outer message.."
      }
    }
  }
```

## Error codes

Error codes are displayed in hexadecimal format for all handled scenarios. The following table lists each error code with its respective name and message.

| **Error code** | **Error name** | **Error message** |
|-|-|-|
| 900400FF | NoAttributesForEntityCreate | No attributes for Create Entity action. |
| 90040100 | InvalidAttribute | Attribute {0} cannot be found for entity {1}. |
| 90040101 | AttributePermissionIsMissing | Attribute {0} in entity {1} is not enabled for Web Api. |
| 90040102 | EntityPermissionWriteIsMissingDuringUpdate | You don't have permission to update {0} entity. |
| 90040103 | EntityPermissionCreateIsMissing | You don't have permission to create {0} entity. |
| 90040104 | EntityPermissionDeleteIsMissing | You don't have permission to delete {0) entity. |
| 90040105 | EntityPermissionAppendIsMissngDuringAssociationChange | You don't have permission to associate or disassociate entity {0} with {1}. |
| 90040106 | EntityPermissionAppendToIsMissingDuringAssociationChange | You don't have permission to associate or disassociate entity {1} to {0} |
| 90040107 | HttpAntiForgeryException | The anti-forgery cookie token and form field token do not match. |
| 90040109 | MissingPortalSessionCookie | An Invalid session token was passed into the throwing method. |
| 9004010C | ResourceDoesNotExists | Resource not found for the segment '{0}'. |
| 9004010D | CDSError | CDS error occurred. |

Response for unhandled errors with HTTP status code 500 will return the error "An unexpected error occurred while processing the request."

### See also

[Web API overview](web-api-overview.md)  
[Perform Web API operations](web-api-perform-operations.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]