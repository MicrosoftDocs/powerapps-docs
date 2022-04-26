---
title: "StandardControl.getOutputs | MicrosoftDocs"
description: It is called by the framework prior to a component receiving the new data. Returns an object based on nomenclature defined in manifest, expecting objects[s] for the property marked as bound.
ms.author: jdaly
author: noazarur-microsoft
manager: kvivek
ms.date: 03/26/2022
ms.reviewer: jdaly

ms.topic: "reference"
applies_to: ""

---
# StandardControl.getOutputs

[!INCLUDE[./includes/getoutputs-description.md](./includes/getoutputs-description.md)]

## Available for 

Model-driven and canvas apps

## Syntax

`getOutputs()`

## Remarks

The output will contain a value for each property with a usage as `bound` in the manifest.
For example, if the manifest has a property named `value` that has usage as `bound`, and you want to set that to the local variable `myvalue` then you should return:

```TypeScript
{
    value: myvalue
}
```

## Example

```TypeScript
public getOutputs(): IOutputs
{
    return {
        value: this._value
    };
}
```


### Related topics

[Control](../control.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]