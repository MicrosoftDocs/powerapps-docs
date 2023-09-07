---
title: "ReactControl.destroy (Power Apps component framework API reference) | MicrosoftDocs"
description: This method is invoked in a ReactControl when the component is to be removed from the DOM tree. Use it for the cleanup and to release any memory that the component is using.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly

---
# ReactControl.destroy

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

### Related articles

[React controls & platform libraries (Preview) ](../../react-controls-platform-libraries.md)<br />
[ReactControl](../react-control.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
