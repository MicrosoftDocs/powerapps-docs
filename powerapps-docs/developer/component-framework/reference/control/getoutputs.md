---
title: "StandardControl.getOutputs (Power Apps component framework API reference) | MicrosoftDocs"
description: This method is called by the framework before a component receives the new data. Returns an object based on nomenclature defined in manifest, expecting objects[s] for the property marked as bound.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly

---
# StandardControl.getOutputs

[!INCLUDE[./includes/getoutputs-description.md](./includes/getoutputs-description.md)]

## Available for 

Model-driven apps, canvas apps, & portals.

## Syntax

`getOutputs()`

## Remarks

The output contains a value for each property with a usage as `bound` in the manifest.
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


### Related articles

[Control](../control.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
