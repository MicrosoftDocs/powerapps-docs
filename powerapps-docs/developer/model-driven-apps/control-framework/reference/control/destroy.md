---
title: "destroy | MicrosoftDocs"
ms.date: 10/12/2018
ms.service: "powerapps"
ms.topic: "reference"
applies_to: ""
ms.assetid: ba66b513-2a7b-4ba6-b2d5-446ea2b42fdb
author: "nkrb"
ms.author: "nabuthuk"
manager: "jdaly"
---
# destroy

[!INCLUDE[./includes/destroy-description.md](./includes/destroy-description.md)]

## Syntax

`destroy()`

## Example

```javascript
MyControl.prototype.destroy = function () {
 this.button.removeEventListener("click", this.onButtonClick);
};
```

### Related topics

[Control](../control.md)<br />
[PowerApps Control Framework API Reference](../index.md)<br />
[PowerApps Control Framework Overview](../../powerapps-control-framework-overview.md)<br />
