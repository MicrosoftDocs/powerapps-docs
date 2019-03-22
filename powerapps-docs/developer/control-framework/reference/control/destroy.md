---
title: "destroy | MicrosoftDocs"
ms.topic: "reference"
applies_to: ""
ms.assetid: ba66b513-2a7b-4ba6-b2d5-446ea2b42fdb
author: "nkrb"
ms.author: "nabuthuk"
manager: kvivek
ms.date: 03/01/2019
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

