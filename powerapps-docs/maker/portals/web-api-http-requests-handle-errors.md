---
title: Use the Web API for portals | Microsoft Docs
description: Learn how to use the portals Web API to create, read, update and delete Common Data Service entities.
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/05/2020
ms.author: tapanm
ms.reviewer:
---

# Portals Web API

## Web API URL and versioning

https://docs.microsoft.com/powerapps/developer/common-data-service/webapi/compose-http-requests-handle-errors#web-api-url-and-versions

Construct the Web API URL with the following format:

| Part | Description |
| - | - |
| Protocol | https://                                 |
| Base URL | \<portal name\>                          |
| Web API Path | \_api                                    |
| Versioning | v[major].[minor][patch]                  |
| Resource     | Name of entity or action you want to use |

For example, use this format when referring a case: https://contoso.powerappsportal.com/api/data/v1.0/case.

@Neeraj - how can we know all available versions?

For entity resources [portal’s entity
permission](https://docs.microsoft.com/dynamics365/portals/assign-entity-permissions)
configuration will be owner. <br> @Neeraj - please explain or elaborate above sentence.

### Getting portal base URL

Use `GetAPIBaseURL()` JavaScript Client API to get your portal's base URL for API endpoint. For example, the result of a *Get* request is: `https://\<portal name\>/_api`.

#### HTTP methods

| Method | Usage |
| - | - |
| Get    | Use when retrieving data. |
| Post   | Creating entities and calling actions. |
| Patch  | Use when updating entities or performing upsert operation. |
| Delete | Use when deleting entities or individual properties of entities. |
| Put    | @Neeraj - need description/usage |

### HTTP headers

Web API only supports JSON. Each HTTP headers must include:

- *Accept* header value of *application/json*, even when no response body is expected.
- *If-None-Match* null header in the request body to override browser
caching of Web API request.
- If the request includes JSON data in the request body, you must include a
*Content-Type* header with a value of `application/json`.

The current OData version is 4.0, but future versions may allow for new
capabilities. To ensure that there is no ambiguity about the OData version that will be applied to your code at that point in the future. 
<br> @Neeraj - what's the above OData version/future versions note regarding?

#### Syntax

```http
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-None-Match: null
```

##### Example: Get entity data

```http
var portalUrl = GetAPIBaseURL(); //Returns portal’s Data API base URL
var xhttp = new XMLHttpRequest()
xhttp.open("GET", encodeURI(portalUrl + "/_api/entityname(GUID)"), true);
xhttp.setRequestHeader("Accept", "application/json");
xhttp.setRequestHeader("OData-MaxVersion", "4.0");
xhttp.setRequestHeader("OData-Version", "4.0");
xhttp.send();
```

##### Example: Create entity data

```http
var portalUrl = GetAPIBaseURL(); //Returns portal’s Data API base URL
var xhttp = new XMLHttpRequest()
xhttp.open("POST", encodeURI(portalUrl + "/_api/entityname"), true);
xhttp.setRequestHeader("Accept", "application/json");
xhttp.setRequestHeader("Content-Type", "application/json; charset=utf-8");
xhttp.setRequestHeader("OData-MaxVersion", "4.0");
xhttp.setRequestHeader("OData-Version", "4.0");
var body = JSON.stringify ({
    "name": "Sample entity name",
    "creditonhold": false,
    "address1_latitude": 47.639583,
    "description": "This is the description of the sample account",
    "revenue": 5000000,
    "accountcategorycode": 1
});
xhttp.send(body);
```

### Identify status codes

https://docs.microsoft.com/powerapps/developer/common-data-service/webapi/compose-http-requests-handle-errors#identify-status-codes

| Code | Description | Type |
| - | - | - |
| 200 OK | Expect this when your operation will return data in the response body. | Success |
| 204 No Content | Expect this when your operation succeeds, but doesn't return data in the response body. | Success |
| 403 Forbidden | Expect this for the following types of errors: <br> - AccessDenied <br> - AttributePermissionIsMissing <br> - EntityPermissionWriteIsMissingDuringUpdate <br> - EntityPermissionCreateIsMissing <br> - EntityPermissionDeleteIsMissing <br> - EntityPermissionAppendIsMissngDuringAssociationChange - <br> - EntityPermissionAppendToIsMissingDuringAssociateChange | Client Error |
| 401 Unauthorized | Expect this for the following types of errors: <br> - MissingPortalRequestVerificationToken <br> - MissingPortalSessionCookie | Client Error |
| 413 Payload Too Large | Expect this when the request length is too large. | Client Error |
| 400 BadRequest | Expect this when an argument is invalid. <br> InvalidAttribute | Client Error |
| 404 Not Found | - Expect this when the resource doesn’t exist. <br> - Entity is not expose for web api. | Client Error |
| 405 Method Not Allowed | This error occurs for incorrect method and resource combinations. For example, you can’t use DELETE or PATCH on a collection of entities. This situation can happen for the following types of errors: <br> - CannotDeleteDueToAssociation <br> - InvalidOperation <br> - NotSupported | Client Error |
| 429 Too Many Requests  | Expect this when API limits are exceeded. More information: [Service Protection API Limits](../../developer/common-data-service/api-limits.md). | Client Error |
| 501 Not Implemented | Expect this when some requested operation isn't implemented. | Server Error |
| 503 Service Unavailable | Expect this when the web API service isn’t available. | Server Error |

@Neeraj: need more information about what the following table illustrates: (I've formatted table anyways but needs elaboration)

| Header Name | Is CDS specific? |
| - | - |
| cache-control: no-cache | No |
| allow: OPTIONS,GET,HEAD,POST | No |
| expires: -1 | No |
| --location: https://YourOrg.crm.dynamics.com/_api/v9.1/entityName(GUID) | Yes |
| --x-ms-service-request-id: GUID, GUID | Yes |
| strict-transport-security: max-age=31536000; includeSubDomains | No |
| req_id: GUID | No |
| access-control-allow-origin: * | No |
| access-control-expose-headers: Preference-Applied,OData-EntityId,Location,ETag,OData-Version,Content-Encoding,Transfer-Encoding,Content-Length,Retry-After | No |
| --authactivityid: GUID | Yes |
| odata-version: 4.0 | No |
| --odata-entityid: https://YourOrg.crm.dynamics.com/_api/v9.1/entityName(GUID) | Yes |
| --x-ms-ratelimit-burst-remaining-xrm-requests: 5993 | Yes |
| --x-ms-ratelimit-time-remaining-xrm-requests: 1,199.46 | Yes |
| public: OPTIONS,GET,HEAD,POST | No |
| timing-allow-origin: * | No |
| x-source: 1274022621962271406513018456102176233138130371162212021413319206254117391372519213849 | No |
| date: Mon, 18 May 2020 10:38:54 GMT | No |
| X-Firefox-Spdy: h2 | No |

### Parse errors from the response 

The property [*innererror*](../../developer/common-data-service/webapi/compose-http-requests-handle-errors.md#parse-errors-from-the-response) is going to be deprecated. 

Consider the following example response that still includes the innererror:

```json
{
  "error":{
    "code": "\<This code is not related to the http status code and is frequently empty\>",
    "message": "\<A message describing the error\>",
    "innererror": {
        “code”: “800xxxx”,
        "message": "\<A message describing the error, this is frequently the same as the outer message\>",
        "type": "Microsoft.Crm.CrmHttpException",
        "stacktrace": "\<Details from the server about where the error occurred\>"
      }
    }
  }
```
In the above example, Common Data Service shows the following error:

```json
{
  "error":{
  "code": "800XXX
  "message": " error message
  }
}
```

Portals Web API error response includes:

```json
{
  "error":{
  "code": "9004010D"
  "message": "CDS error occurred",
  “cdscode”: “800xxx”,
  "innererror": {
      "code": "800XXX
      "message": " error message
    }
  }
}
```

## Error codes

@Neeraj - errors are shown in HTTP responses? And do errors only show code, or message are displayed too?

Error codes are displayed in hexadecimal format for all handled scenarios. The following table explains the error code, and the respective error name and message.

| **Error Code** | **Error Name** | **Error Message** |
|-|-|-|
| 900400FF | NoAttributesForEntityCreate | No attributes for Create Entity action. |
| 90040100 | InvalidAttribute | Attribute {0} cannot be found for entity {1}. |
| 90040101 | AttributePermissionIsMissing | Attribute {0} in entity {1} is not enabled for Web Api. |
| 90040102 | EntityPermissionWriteIsMissingDuringUpdate | You don’t have permission to update {0} entity. |
| 90040103 | EntityPermissionCreateIsMissing | You don’t have permission to create {0} entity. |
| 90040104 | EntityPermissionDeleteIsMissing | You don’t have permission to delete {0) entity. |
| 90040105 | EntityPermissionAppendIsMissngDuringAssociationChange | You don’t have permission to associate or disassociate entity {0} with {1}. |
| 90040106 | EntityPermissionAppendToIsMissingDuringAssociationChange | You don’t have permission to associate or disassociate entity {1} to {0} |
| 90040107 | CannotDeleteDueToAssociation | The object you tried to delete is associated with another object and cannot be deleted. |
| 90040108 | MissingPortalRequestVerificationToken | An invalid request verification token was passed. |
| 90040109 | MissingPortalSessionCookie | An Invalid session token was passed into the throwing method. |
| 9004010A | InvalidOperation | Invalid Operation performed. |
| 9004010B | NotSupported | This action is not supported. |
| 9004010C | ResourceDoesNotExists | Resource not found for the segment '{0}'. |
| 9004010D | CDSError | CDS error occurred. |

Response for unhandled errors with HTTP status code 500 will return the error *An unexpected error occurred while processing the request*.

## Next steps

[Web API samples](web-api-samples.md)

### See also

- [Web API overview](web-api-overview.md)
- [Perform Web API operations](web-api-perform-operations.md)
- [Compose HTTP requests and handle errors](web-api-http-requests-handle-errors.md)
