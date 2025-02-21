---
title: "htmlDecode (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the htmlDecode method.
author: sriharibs-msft
ms.author: srihas
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
