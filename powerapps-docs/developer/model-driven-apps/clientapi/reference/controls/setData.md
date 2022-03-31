---
title: "setData (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the setData method.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# setData (Client API reference)

Sets the value of the data query string parameter passed to a Silverlight web resource.

## Control types supported

webresource 

## Syntax

`formContext.getControl(arg).setData(string);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|string|String|Yes|The data value to pass to the Silverlight web resource.|

## Related topics

[getData](getData.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]