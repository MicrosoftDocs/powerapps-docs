---
title: "destroy | MicrosoftDocs"
description: This method is invoked when the component is to be removed from the DOM tree. Use it for the cleanup and to release any memory that the component is using.
ms.topic: "reference"
applies_to: ""
ms.assetid: ba66b513-2a7b-4ba6-b2d5-446ea2b42fdb
author: "nkrb"
ms.author: "nabuthuk"
manager: kvivek
ms.date: 10/01/2019
ms.service: powerapps
---
# destroy

[!INCLUDE[./includes/destroy-description.md](./includes/destroy-description.md)]

## Available for 

Model-driven and canvas apps

## Syntax

`destroy()`

## Example

```TypeScript
public destroy(): void
{
    this.button.removeEventListener("click", this.onButtonClick);
}
```

### Related topics

[Control](../control.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]