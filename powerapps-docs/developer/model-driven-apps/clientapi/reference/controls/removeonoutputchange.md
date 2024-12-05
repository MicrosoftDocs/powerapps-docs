---
title: "removeOnOutputChange (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the control.removeOnOutputChange method.
author: MitiJ
ms.author: mijosh
ms.date: 08/17/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# removeOnOutputChange (Client API reference)

Removes an event handler from the [OnOutputChange](../events/onoutputchange.md) event.

## Control types supported

Standard control

## Syntax

```JavaScript
var control = formContext.getControl("<name>");
control.removeOnOutputChange(myFunction);
```

## Parameters

|Name | Type | Required | Description|
|----|----|----|----|
|`myFunction` |Function |Yes|The function to remove from the **OnOutputChange** event.| 

### Related articles

[addOnOutputChange](addonoutputchange.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
