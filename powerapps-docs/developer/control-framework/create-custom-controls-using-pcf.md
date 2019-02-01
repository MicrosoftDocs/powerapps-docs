---
title: Create custom controls using PowerApps Control Framework | Microsoft Docs
description: Start creating controls using the powerapps control Framework
keywords: PowerApps Control Framework, Custom Controls, Control Framework
ms.author: nabuthuk
manager: jdaly
ms.date: 06/4/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d2cbf58a-9112-45c2-b823-2c07a310714c
---

# Create Controls using PowerApps Control Framework

[!INCLUDE[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This topic showcases how to implement custom controls using **PowerApps Control Framework**. Custom controls provide enhanced user experience to view and work with data in forms, views.

Each custom control is comprised of the following key components:

1. Manifest
2. Control implementation library
3. Resources

## Manifest

The first step in implementing a custom control is to define a manifest file which defines various aspects of the control including namespace, version and dependent resource files.

### Sample Manifest

```xml
<?xml version="1.0" encoding="utf-8" ?>
<manifest>
	<control namespace="MyNameSpace" constructor="JSHelloWorldControl" version="1.0.0" display-name-key="JS_HelloWorldControl_Display_Key" description-key="JS_HelloWorldControl_Desc_Key" control-type="standard">
		<property name="myFirstProperty" display-name-key="myFirstProperty_Display_Key" description-key="myFirstProperty_Desc_Key" of-type="SingleLine.Text" usage="bound" required="true" />
		<resources>
			<code path="JS_HelloWorldControl.js" order="1" />
			<css path="css/JS_HelloWorldControl.css" order="1" />
		</resources>
	</control>
</manifest>
```

The different nodes in the manifest file defines various aspects of the control in a format that Model-driven apps can understand. More information: [Manifest](manifest-schema-reference/manifest.md).

## Control implementation library

[!INCLUDE [control-implementation-library](control-implementation-library.md)]

### Sample Code in JavaScript

```JavaScript
/*
This file is part of the Microsoft PowerApps code samples.
Copyright (C) Microsoft Corporation.  All rights reserved.
This source code is intended only as a supplement to Microsoft Development Tools and/or
on-line documentation.  See these other materials for detailed information regarding
Microsoft code samples.

THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER
EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
*/

"use strict";

var MyNameSpace = MyNameSpace || {};

MyNameSpace.JSHelloWorldControl = function(){
}


/**
* Used to initialize the control instance. Controls can kick off remote server calls and other initialization actions here.
* Data-set values are not initialized here, use updateView.
* @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to property names defined in the manifest, as well as utility functions.
* @param notifyOutputChanged A callback method to alert the framework that the control has new outputs ready to be retrieved asynchronously.
* @param state A piece of data that persists in one session for a single user. Can be set at any point in a controls life cycle by calling 'setControlState' in the Mode interface.
* @param container If a control is marked control-type='starndard', it will receive an empty div element within which it can render its content.
*/
MyNameSpace.JSHelloWorldControl.prototype.init = function (context, notifyOutputChanged, state, container) {
this._labelElement = document.createElement("label");
this._labelElement.setAttribute("class", "JS_HelloWorldColor");
container.appendChild(this._labelElement);
};

/**
* Called when any value in the property bag has changed. This includes field values, data-sets, global values such as container height and width, offline status, control metadata values such as label, visible, etc.
* @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to names defined in the manifest, as well as utility functions
*/
MyNameSpace.JSHelloWorldControl.prototype.updateView = function (context) {
this._labelElement.innerText = "Hello World! (JS)";
};

/**
* It is called by the framework prior to a control receiving new data.
* @returns an object based on nomenclature defined in manifest, expecting object[s] for property marked as “bound” or “output”
*/
MyNameSpace.JSHelloWorldControl.prototype.getOutputs = function () {
return {};
};

/**
* Called when the control is to be removed from the DOM tree. Controls should use this call for cleanup.
* i.e. cancelling any pending remote calls, removing listeners, etc.
*/
MyNameSpace.JSHelloWorldControl.prototype.destroy = function () {
};
```

### Sample code in TypeScript

```TypeScript
/*
This file is part of the Microsoft PowerApps code samples.
Copyright (C) Microsoft Corporation.  All rights reserved.
This source code is intended only as a supplement to Microsoft Development Tools and/or
on-line documentation.  See these other materials for detailed information regarding
Microsoft code samples.

THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER
EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
*/

/// <reference path="../../typing/ControlFramework.d.ts"/>
/// <reference path="./private_typing/inputsOutputs.d.ts"/>

module MyNameSpace
{
export class TSHelloWorldControl implements ControlFramework.StandardControl<InputsOutputs.IInputs, InputsOutputs.IOutputs> {

private _labelElement: HTMLLabelElement;

/**
* Used to initialize the control instance. Controls can kick off remote server calls and other initialization actions here.
* Data-set values are not initialized here, use updateView.
* @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to property names defined in the manifest, as well as utility functions.
* @param notifyOutputChanged A callback method to alert the framework that the control has new outputs ready to be retrieved asynchronously.
* @param state A piece of data that persists in one session for a single user. Can be set at any point in a controls life cycle by calling 'setControlState' in the Mode interface.
* @param container If a control is marked control-type='starndard', it will receive an empty div element within which it can render its content.
*/
public init(context: ControlFramework.Context<InputsOutputs.IInputs>, notifyOutputChanged: () => void, state: ControlFramework.Dictionary, container:HTMLDivElement)
{
this._labelElement = document.createElement("label");
this._labelElement.setAttribute("class", "TS_HelloWorldColor");
container.appendChild(this._labelElement);
}

/**
* Called when any value in the property bag has changed. This includes field values, data-sets, global values such as container height and width, offline status, control metadata values such as label, visible, etc.
* @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to names defined in the manifest, as well as utility functions
*/
public updateView(context: ControlFramework.Context<InputsOutputs.IInputs>,)
{
this._labelElement.innerText = "Hello World! (TS)";
}

/**
* It is called by the framework prior to a control receiving new data.
* @returns an object based on nomenclature defined in manifest, expecting object[s] for property marked as “bound” or “output”
*/
public getOutputs(): InputsOutputs.IOutputs
{
return {};
}

/**
* Called when the control is to be removed from the DOM tree. Controls should use this call for cleanup.
* i.e. cancelling any pending remote calls, removing listeners, etc.
*/
public destroy()
{

    }
  }
}
```

> [!NOTE]
> Developers need to transpile their code into `JavaScript` if you wish to implement the custom logic in `TypeScript` and add a reference to it in the manifest file.

## Resources

[!INCLUDE [resources-description](manifest-schema-reference/includes/resources-description.md)]
More information: [Resources](manifest-schema-reference/resources.md)


> [!div class="nextstepaction"]
> [How to import controls](import-custom-controls.md)


