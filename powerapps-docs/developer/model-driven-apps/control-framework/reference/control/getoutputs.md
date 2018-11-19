---
title: "getOutputs | MicrosoftDocs"
ms.date: 01/12/2018
ms.service: "powerapps"
ms.topic: "reference"
applies_to: ""
ms.assetid: c83c3a09-f04e-4dc6-8ddf-ccd0b4cc080e
author: "nkrb"
ms.author: "nabuthuk"
manager: "jdaly"
---
# getOutputs

[!INCLUDE[./includes/getoutputs-description.md](./includes/getoutputs-description.md)]

## Syntax

`getOutputs()`

## Remarks

The output will contain a value for each property marked as `input-output` or `bound` in the manifest.
For example, if the manifest has a property `value` that is an `input-output`, and you want to set that to the local variable `myvalue` you should return:

```javascript
{
    value: myvalue
}
```

## Example

```javascript
MyControl.prototype.getOutputs = function () {
    var result = {
        value: this._value
    };
    return result;
};
```

### Related topics

[Control](../control.md)<br />
[PowerApps Control Framework API Reference](../index.md)<br />
[PowerApps Control Framework Overview](../../powerapps-control-framework-overview.md)<br />
