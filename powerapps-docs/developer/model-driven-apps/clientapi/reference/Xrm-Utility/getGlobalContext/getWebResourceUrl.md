---
title: "getWebResourceUrl (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 03/17/2020
ms.service: powerapps
ms.topic: "reference"
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getWebResourceUrl (Client API reference)

Returns the relative URL with the caching token for the specified web resource.

## Syntax

```JavaScript
var globalContext = Xrm.Utility.getGlobalContext();
globalContext.getWebResourceUrl(webResourceName);
```

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|webResourceName |String |Yes |Name of the web resource. |

## Return Value

**Type**: String

**Description**: The relative URL, including the caching token, for the specified web resource.

## Example

```JavaScript
var globalContext = Xrm.Utility.getGlobalContext();
globalContext.getWebResourceUrl("sample_webResource1.js");
```

This will return the web resource URL with the caching token:

`/%7b637199221580014143%7d/webresources/sample_webResource1.js`

> [!NOTE]
> The caching token in the URL ensures that the web resource is cached for one year from the current date. You must use the URL with the caching token for a web resource to ensure that the latest cached version of the specified web resource is used.

### Related topics

[Xrm.Utility.getGlobalContext](../getGlobalContext.md)


