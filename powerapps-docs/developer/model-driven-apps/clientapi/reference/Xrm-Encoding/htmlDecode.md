---
title: "htmlDecode| MicrosoftDocs"
description: "The Client API method converts a string that has been HTML-encoded into a decoded string."
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 4ef7160b-ac01-4d08-8a98-f8e3012ef20b
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# htmlDecode (Client API reference)



[!INCLUDE[./includes/htmlDecode-description.md](./includes/htmlDecode-description.md)] 

## Syntax

`Xrm.Encoding.htmlDecode(arg)`

## Parameters

|Parameter Name        | Type           | Required  |Description  |
| ------------- |-------------| -----|-----|
|arg        | String           | Required  |HTML-encoded string to be decoded.  |


## Return Value

**Type**: String

**Description**: Decoded string.

## Related topics

[htmlEncode](htmlEncode.md)

[htmlAttributeEncode](htmlAttributeEncode.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]