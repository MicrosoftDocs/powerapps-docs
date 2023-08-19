---
title: "StandardControl.init (Power Apps component framework API reference) | MicrosoftDocs"
description: Used to initialize the component instance. Components can kick off remote server calls and other initialization actions.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---
# StandardControl.init

[!INCLUDE[./includes/init-description.md](./includes/init-description.md)]

[trackContainerResize](../mode/trackcontainerresize.md) should be called once, preferably in the component `init` method to notify that the component needs the layout information. Use this method to tell the framework to populate `allocatedHeight` and `allocatedWidth` methods.

> [!NOTE]
> tractContainerResize should be called first before the `allocatedHeight` and `allocatedWidth` methods.

## Available for 

Model-driven apps, canvas apps, & portals.

## Syntax

`init(context,notifyOutputChanged,state,container)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|context|[Context](../context.md)|yes|The *Input Properties* containing the parameters, component metadata, and interface functions.|
|notifyOutputChanged|`function`|no|The method to notify the framework that it has new outputs|
|state|`Dictionary`|no|The component state that is saved from *setControlState* in the last session|
|container|[HTMLDivElement](https://developer.mozilla.org/docs/Web/API/HTMLDivElement)|no|The div element to render|

## Example

```TypeScript
public init(context: ComponentFramework.Context<IInputs>, notifyOutputChanged: () => void, state: ComponentFramework.Dictionary, container:HTMLDivElement)
{
    this._labelElement = document.createElement("label");
    this._labelElement.setAttribute("class", "HelloWorldColor");
    container.appendChild(this._labelElement);
}
```

### Related articles

[Control](../control.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
