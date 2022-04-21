---
title: "StandardControl.destroy | MicrosoftDocs"
description: This method is invoked when the component is to be removed from the DOM tree. Use it for the cleanup and to release any memory that the component is using.
ms.topic: "reference"
applies_to: ""
ms.author: jdaly
author: noazarur-microsoft
manager: kvivek
ms.date: 03/26/2022
ms.reviewer: jdaly

---
# StandardControl.destroy

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