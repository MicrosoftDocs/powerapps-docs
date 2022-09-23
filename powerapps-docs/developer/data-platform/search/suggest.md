---
title: "Dataverse Search suggest (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use Dataverse search suggest to provide suggestions as the user enters text into a form field." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 09/12/2022
ms.reviewer: jdaly
ms.topic: article
author: mspilde # GitHub ID
ms.author: mspilde # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
---
# Dataverse Search suggest

Typically, you will use this API to support a richer search box experience. For example, as the user enters each character of their search term, you'd call this API and populate the search box's dropdown list with the suggested query results. 



## Examples

### Example: TODO

This is a template for an example
#### [Search endpoint](#tab/search)

**Request**

```http
POST [Organization URI]/api/search/v1.0/status HTTP/1.1
```

**Response**

```http
HTTP/1.1 200 OK

{}
```

#### [SDK for .NET](#tab/sdk)

```csharp
static void SDKExampleMethod(IOrganizationService service){
 TODO
}
```
**Output**

```
TODO: The output of the SDK Sample
```

#### [Web API](#tab/webapi)

**Request**

```http
GET [Organization URI]/api/data/v9.2/searchquery HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response**

```http
HTTP/1.1 200 OK

{}
```
---


### See also

[Search for Dataverse records](overview.md)<br />
[Dataverse Search query](query.md)<br />
[Dataverse Search autocomplete](autocomplete.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]