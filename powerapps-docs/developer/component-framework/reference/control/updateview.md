---
title: "updateView| MicrosoftDocs"
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 899d6eb3-62b4-4c1f-947c-aed1f8643caa
ms.author: "nabuthuk"
author: Nkrb
---
# updateView

[!INCLUDE[./includes/updateview-description.md](./includes/updateview-description.md)]

## Available for 

Model-driven apps and canvas apps (public preview)

## Syntax

`updateView(context)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|context|`context`|yes|Contains values as set up by the customizer mapped to the name defined in the manifest, as well as in the utility functions|

## Example

```TypeScript
public updateView(context: ComponentFramework.Context<IInputs>): void
{
    this._labelElement.innerText = "Hello World! (TS)";
}
```

## Remarks

Set the value of the field component to the raw value from the configured field


### Related topics

[Control](../control.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]