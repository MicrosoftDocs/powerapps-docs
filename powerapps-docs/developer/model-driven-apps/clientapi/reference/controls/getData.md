---
title: "control.getData (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the control.getData method.
author: chmoncay
ms.author: chmoncay
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# control.getData (Client API reference)

Returns the value of the data query string parameter passed to a Silverlight web resource. 

## Control types supported

Web resource

## Syntax
 
`formContext.getControl(arg).getData();`

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Return Value

**Type**: String

**Description**: The data value passed to the Silverlight web resource.


### Related topics

[setData](setData.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]