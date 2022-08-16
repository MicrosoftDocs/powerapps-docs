---
title: "ReactControl.getOutputSchema| MicrosoftDocs"
description: This method will be called for a ReactControl to get the output schema for the output properties of the control. 
ms.author: noazarur
author: noazarur-microsoft
ms.date: 08/10/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---
# ReactControl.getOutputSchema

[!INCLUDE[./includes/updateview-description.md](./includes/updateview-description.md)]

## Available for

Canvas apps

## Syntax

`getOutputSchema()`

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

[React controls & platform libraries (Preview) ](../../react-controls-platform-libraries.md)<br />
[ReactControl](../react-control.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]