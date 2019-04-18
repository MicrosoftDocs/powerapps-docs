---
title: "init | MicrosoftDocs"
manager: kvivek
ms.date: 03/01/2019
ms.service: "powerapps"
ms.topic: "reference"
applies_to: ""
ms.assetid: 4485b7d4-c68f-4298-8676-1820eb33c1ad
ms.author: "nabuthuk"
---
# init

[!INCLUDE[./includes/init-description.md](./includes/init-description.md)]

## Syntax

`init(context,notifyOutputChanged,state,container)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|context|[Context](../context.md)|yes|The *Input Properties* containing the parameters, control metadata and interface functions.|
|notifyOutputChanged|`function`|no|The method to notify the framework that it has new outputs|
|state|`Dictionary`|no|The control state that is saved from *setControlState* in the last session|
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
[PowerApps Component Framework API Reference](../reference/index.md)<br/>
[PowerApps Component Framework Overview](../overview.md)
