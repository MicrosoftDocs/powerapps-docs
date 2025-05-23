---
title: "attribute.getOptions (Client API reference)"
description: Includes description and supported parameters for the attribute.getOptions method.
author: clromano
ms.author: clromano
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# attribute.getOptions (Client API reference)

Returns an array of option objects representing valid options for a column. 

## Column types supported

Choice, Choices

## Syntax

`formContext.getAttribute(arg).getOptions()`

## Return Value

**Type**: Array of option objects.

**Description**: The array of option objects representing valid options.

Options have two properties:

|Property|Type|Description|
|--------|----|-----------|
|`text`|string|The localized label for the option.|
|`value`|number|The integer value of the option.|

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
