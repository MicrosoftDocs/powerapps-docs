---
title: "addOnOutputChange (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the control.addOnOutputChange method.
ms.author: noazarur
author: noazarur-microsoft

ms.date: 08/17/2022
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
# addOnOutputChange (Client API reference)

Adds an event handler to the [OnOutputChange](../events/onoutputchange.md) event. 

## Control types supported

Standard controls

## Syntax

```JavaScript
var control = formContext.getControl("<name>");
control.addOnOutputChange(myFunction);
```
[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Parameters

|Name | Type | Required | Description|
|--|--|--|--|
|myFunction |Function |Yes|The function to add to the **OnOutputChange** event. The [execution context](../../clientapi-execution-context.md) is automatically passed as the first parameter to this function.|

### Related topics

[OnOutputChange event](../events/onoutputchange.md)

[removeOnOutputChange](removeonoutputchange.md) 

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
