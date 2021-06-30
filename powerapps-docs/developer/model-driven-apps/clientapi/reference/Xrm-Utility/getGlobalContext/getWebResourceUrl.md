---
title: "getWebResourceUrl (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getWebResourceUrl method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
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

> [!NOTE]
> If you:
> - Use this method every time, you will have the latest version of the web resource and it will be cached for up to one year. 
> - Use this method once and save the URL, you will get the version, which was current at the time the URL was built, for next one year.
> - Don’t use this method and construct the URL yourself, the item returned won't be cached.

## Example

```JavaScript
var globalContext = Xrm.Utility.getGlobalContext();
globalContext.getWebResourceUrl("sample_webResource1.js");
```

This will return the web resource URL with the caching token:

`/%7b637199221580014143%7d/webresources/sample_webResource1.js`
 

### Related topics

[Xrm.Utility.getGlobalContext](../getGlobalContext.md)




[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]