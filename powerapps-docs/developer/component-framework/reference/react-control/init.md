---
title: "ReactControl.init (Power Apps component framework API reference) | MicrosoftDocs"
description: Used to initialize the component instance for a ReactControl. Components can kick off remote server calls and other initialization actions.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---
# ReactControl.init

[!INCLUDE[./includes/init-description.md](./includes/init-description.md)]

[trackContainerResize](../mode/trackcontainerresize.md) should be called once preferably in the component `init` method to notify that the component needs the layout information . This indicates the framework to populate `allocatedHeight` and `allocatedWidth` methods.

> [!NOTE]
> `trackContainerResize` should be called first before the `allocatedHeight` and `allocatedWidth` methods.

## Available for 

Model-driven and canvas apps

## Syntax

`init(context,notifyOutputChanged,state)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|context|[Context](../context.md)|yes|The *Input Properties* containing the parameters, component metadata and interface functions.|
|notifyOutputChanged|`function`|no|The method to notify the framework that it has new outputs|
|state|`Dictionary`|no|The component state that is saved from *setControlState* in the last session|

> [!NOTE]
> The ReactControl.init method doesn't have a `container` parameter with a `HTMLDivElement` like the [StandardControl.init](../control/init.md) method does. There is no container parameter because React controls do not render the DOM directly. Instead, the [ReactControl.updateView](updateview.md) method returns an ReactElement containing a description of the virtual control DOM.

## Example

```TypeScript
public init(
    context: ComponentFramework.Context<IInputs>,
    notifyOutputChanged: () => void,
    state: ComponentFramework.Dictionary
): void {
    this.notifyOutputChanged = notifyOutputChanged;
    this.context.mode.trackContainerResize(true);
}
```

### Related articles

[React controls & platform libraries (Preview) ](../../react-controls-platform-libraries.md)<br />
[ReactControl](../react-control.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
