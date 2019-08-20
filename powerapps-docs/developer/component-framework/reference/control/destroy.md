---
title: "destroy | MicrosoftDocs"
ms.topic: "reference"
applies_to: ""
ms.assetid: ba66b513-2a7b-4ba6-b2d5-446ea2b42fdb
author: "nkrb"
ms.author: "nabuthuk"
manager: kvivek
ms.date: 04/23/2019
---
# destroy

[!INCLUDE[./includes/destroy-description.md](./includes/destroy-description.md)]

## Available for 

Model-driven apps and canvas apps (experimental preview)

## Syntax

`destroy()`

## Example

```javascript
MyControl.prototype.destroy = function () {
 this.button.removeEventListener("click", this.onButtonClick);
};
```

### Related topics

[Control](../control.md)<br/>
[PowerApps component framework API Reference](../../reference/index.md)<br/>
[PowerApps component framework Overview](../../overview.md)