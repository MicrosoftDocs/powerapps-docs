---
title: "htmlDecode| MicrosoftDocs"
description: "The Client API method converts a string that has been HTML-encoded into a decoded string."
author: adrianorth
ms.author: aorth
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# htmlDecode (Client API reference)



[!INCLUDE[./includes/htmlDecode-description.md](./includes/htmlDecode-description.md)] 

## Syntax

`Xrm.Encoding.htmlDecode(arg)`

## Parameters

|Parameter Name | Type| Required  |Description  |
| --- |---|---|---|
|`arg`| String | Required  |HTML-encoded string to be decoded.  |


## Return Value

**Type**: String

**Description**: Decoded string.

## Related articles

[htmlEncode](htmlEncode.md)   
[htmlAttributeEncode](htmlAttributeEncode.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
