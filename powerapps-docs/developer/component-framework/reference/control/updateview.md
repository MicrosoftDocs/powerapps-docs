---
title: "StandardControl.updateView (Power Apps component framework API reference) | MicrosoftDocs"
description: This method is called for a StandardControl when any value in the property bag changes. 
author: anuitz
ms.author: anuitz
ms.date: 03/25/2024
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---
# StandardControl.updateView

[!INCLUDE[./includes/updateview-description.md](./includes/updateview-description.md)]

## Available for

Model-driven apps, canvas apps, & portals.

## Syntax

`updateView(context)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|context|`context`|yes|Contains values as configured by the customizer mapped to the name defined in the manifest, and in the utility functions|

## Example

```TypeScript
public updateView(context: ComponentFramework.Context<IInputs>): void
{
    this._labelElement.innerText = "Hello World! (TS)";
}
```

## Remarks

Set the value of the field component to the raw value from the configured field.

Values passed to this method may be null when data isn't ready. [Learn to manage temporarily null property values passed to `updateView`](../../code-components-best-practices.md#manage-temporarily-null-property-values-passed-to-updateview)


### Related articles

[Control](../control.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
