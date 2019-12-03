---
title: "init | MicrosoftDocs"
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.topic: "reference"
applies_to: ""
ms.assetid: 4485b7d4-c68f-4298-8676-1820eb33c1ad
ms.author: "nabuthuk"
author: Nkrb
---
# init

[!INCLUDE[./includes/init-description.md](./includes/init-description.md)]

## Available for 

Model-driven apps and canvas apps (public preview)

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

```JavaScript
MyNameSpace.JSHelloWorldControl.prototype.init = function (context, notifyOutputChanged, state, container) {
	this._labelElement = document.createElement("label");
	this._labelElement.setAttribute("class", "JS_HelloWorldColor");
	container.appendChild(this._labelElement);
};
```

### Related topics

[Control](../control.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)
