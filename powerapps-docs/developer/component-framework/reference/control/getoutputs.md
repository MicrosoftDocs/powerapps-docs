---
title: "getOutputs | MicrosoftDocs"
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.topic: "reference"
applies_to: ""
ms.assetid: c83c3a09-f04e-4dc6-8ddf-ccd0b4cc080e
ms.author: "nabuthuk"
author: Nkrb
---
# getOutputs

[!INCLUDE[./includes/getoutputs-description.md](./includes/getoutputs-description.md)]

## Available for 

Model-driven apps and canvas apps (public preview)

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