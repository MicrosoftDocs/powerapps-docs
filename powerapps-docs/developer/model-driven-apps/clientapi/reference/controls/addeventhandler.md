---
title: "addEventHandler (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the addEventHandler method.
author: MitiJ
ms.author: mijosh
ms.date: 03/17/2025
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# addEventHandler (Client API reference)

Adds an event handler for the specified event

## Control types supported

Custom code components

## Syntax

```javascript
  const controlName1 = "cr116_personid";

  this.onLoad = function (executionContext) {
    const formContext = executionContext.getFormContext();

    const sampleControl1 = formContext.getControl(controlName1);
    sampleControl1.addEventHandler("customEvent1", this.onSampleControl1CustomEvent1);
    sampleControl1.addEventHandler("customEvent2", this.onSampleControl1CustomEvent2);
  }
```

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Parameters

|Name | Type | Required | Description|
|--|--|--|--|
|`name`|string|yes|The name of the custom event configured for the custom component.|
|`function` |Function |Yes|The function to add to the named event. The [execution context](../../clientapi-execution-context.md) is automatically passed as the first parameter to this function.|

### Related articles

[Define Events](../../../../component-framework/events.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
