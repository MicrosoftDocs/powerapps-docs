---
title: "init | MicrosoftDocs"
description: Used to initialize the component instance. Components can kick off remote server calls and other initialization actions.
manager: kvivek
ms.date: 06/08/2021
ms.service: "powerapps"
ms.topic: "reference"
applies_to: ""
ms.assetid: 4485b7d4-c68f-4298-8676-1820eb33c1ad
ms.author: "nabuthuk"
author: Nkrb
---
# init

[!INCLUDE[./includes/init-description.md](./includes/init-description.md)]

[trackContainerResize](../mode/trackcontainerresize.md) should be called once preferably in the component `init` method to notify that the component needs the layout information . This indicates the framework to populate `allocatedHeight` and `allocatedWidth` methods.

> [!NOTE]
> tractContainerResize should be called first before the `allocatedHeight` and `allocatedWidth` methods.

## Available for 

Model-driven and canvas apps

## Syntax

`init(context,notifyOutputChanged,state,container)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|context|[Context](../context.md)|yes|The *Input Properties* containing the parameters, component metadata and interface functions.|
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

### Related topics

[Control](../control.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]