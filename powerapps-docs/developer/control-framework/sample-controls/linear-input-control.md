---
title: " Linear Input Control| Microsoft Docs" 
description: "Implementing linear input control"
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "NavaKiran" 
ms.author: "nkrb" 
manager: "" 
---
# Implementing linear input control

The linear input control changes the user experience of interacting with numeric types on the form. Instead of keying in the numbers, this control provides a linear slider using which the value of the attribute can be set on the form.  

> [!div class="mx-imgBorder"]
> ![Linear Input Control](../media/linear_input_control.png "Linear Input Control")

## Manifest

```xml
<?xml version="1.0" encoding="utf-8" ?>
<manifest>
	<control namespace="SampleNamespace" constructor="TSLinearInputControl" version="1.0.0" display-name-key="TS_LinearInputControl" description-key="TS_LinearInputControl_Desc" control-type="standard">
		<type-group name="numbers">
			<type>Whole.None</type>
			<type>Currency</type>
			<type>FP</type>
			<type>Decimal</type>
		</type-group>
		<property name="controlValue" display-name-key="controlValue_Display_Key" description-key="controlValue_Desc_Key" of-type-group="numbers" usage="bound" required="true" />
		<resources>
			<code path="TS_LinearInputControl.js" order="1" />
			<css path="css/TS_LinearInputControl.css" order="1" />
		</resources>
	</control>
</manifest>
```
## Code
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

module SampleNamespace
{
    export class TSLinearInputControl implements ControlFramework.StandardControl<InputsOutputs.IInputBag, InputsOutputs.IOutputBag> {
	// Value of the field is stored and used inside the control 
	private _value: number;

	// PCF framework delegate which will be assigned to this object which would be called whenever any update happens. 
	private _notifyOutputChanged: () => void;

	// label element created as part of this control
    private labelElement: HTMLLabelElement;
        
    // input element that is used to create the range slider
    private inputElement: HTMLInputElement;
 
    // Reference to the control container HTMLDivElement
	// This element contains all elements of our custom control example
	private _container: HTMLDivElement;

	// Reference to ControlFramework Context object
    private _context: ControlFramework.Context<InputsOutputs.IInputBag>;
        
    // Event Handelr 'refreshData' reference
    private _refreshData: EventListenerOrEventListenerObject;
        

/**
* Used to initialize the control instance. Controls can kick off remote server calls and other initialization actions here.
* Data-set values are not initialized here, use updateView.
* @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to property names defined in the manifest, as well as utility functions.
* @param notifyOutputChanged A callback method to alert the framework that the control has new outputs ready to be retrieved asynchronously.
* @param state A piece of data that persists in one session for a single user. Can be set at any point in a controls life cycle by calling 'setControlState' in the Mode interface.
* @param container If a control is marked control-type='starndard', it will receive an empty div element within which it can render its content.
 */
public init(context: ControlFramework.Context<InputsOutputs.IInputBag>, notifyOutputChanged: () => void, state: ControlFramework.Dictionary, container:HTMLDivElement)
 {
    this._context = context;
    this._container = document.createElement("div");
    this._notifyOutputChanged = notifyOutputChanged;
    this._refreshData = this.refreshData.bind(this);


    // creating HTML elements for the input type range and binding it to the function which refreshes the control data
    this.inputElement = document.createElement("input");
    this.inputElement.setAttribute("type","range");
    this.inputElement.addEventListener("input",this._refreshData);

    //setting the max and min values for the control.
    this.inputElement.setAttribute("min","1");
    this.inputElement.setAttribute("max","1000");
    this.inputElement.setAttribute("class","linearslider");
    this.inputElement.setAttribute("id","linearrangeinput");
            
    // creating a HTML label element that shows the value that is set on the linear range control
    this.labelElement = document.createElement("label");
    this.labelElement.setAttribute("class", "TS_LinearRangeLabel");
    this.labelElement.setAttribute("id","lrclabel");

    // retrieving the latest value from the control and setting it to the HTMl elements.
    this._value = context.parameters.controlValue.raw;
    this.inputElement.setAttribute("value",context.parameters.controlValue.formatted ? context.parameters.controlValue.formatted : "0");
    this.labelElement.innerHTML = context.parameters.controlValue.formatted ? context.parameters.controlValue.formatted : "0";

    // appending the HTML elements to the control's HTML container element.
    this._container.appendChild(this.inputElement);
    this._container.appendChild(this.labelElement);
    container.appendChild(this._container);
        }
        
/**
 * * Updates the values to the internal value variable we are storing and also updates the html label that displays the value
* @param context : The "Input Properties" containing the parameters, control metadata and interface functions
 */
public refreshData(context: ControlFramework.Context<InputsOutputs.IInputBag>,)
 {
    this._value = (this.inputElement.value as any)as number;
    this.labelElement.innerHTML = this.inputElement.value;
    this._notifyOutputChanged();
    }

/**
* Called when any value in the property bag has changed. This includes field values, data-sets, global values such as container height and width, offline status, control metadata values such as label, visible, etc.
* @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to names defined in the manifest, as well as utility functions
*/
public updateView(context: ControlFramework.Context<InputsOutputs.IInputBag>,): void
 {
    // storing the latest context from the control.
    this._value = context.parameters.controlValue.raw;
    this._context = context;
    this.inputElement.setAttribute("value",context.parameters.controlValue.formatted ? context.parameters.controlValue.formatted : "");
    this.labelElement.innerHTML = context.parameters.controlValue.formatted ? context.parameters.controlValue.formatted : "";
    }

/** 
* It is called by the framework prior to a control receiving new data. 
* @returns an object based on nomenclature defined in manifest, expecting object[s] for property marked as “bound” or “output”
 */
public getOutputs(): InputsOutputs.IOutputBag
 {
    return {
             controlValue : this._value
            };
    }

/** 
* Called when the control is to be removed from the DOM tree. Controls should use this call for cleanup.
* i.e. cancelling any pending remote calls, removing listeners, etc.
*/
public destroy()
  {
     this.inputElement.removeEventListener("input", this._refreshData);
        }
    }
}
```

## Overview

In this sample we defined a type -group tag and called it as `numbers` and included decimal, whole, floating and currency value types into that group. We use this group to bind our control property. 
An input element of type range with min and max value set to 1 and 1000, respectively is created. 
Create a label element which shows the value that is relative to the position of the slider. Attach a function refreshData to the eventlistener on input of the control. 
Create a local variable for saving the [context](../reference/context.md) and `notifyOutputChanged`. Assign the context and notifyOutputChanged from the parameters that are passed as part of the init function. 
Implement the logic for the `refreshData` function. As you can see in the sample, we take the value from the `inputElement` and set the value of the control, `innerHTML` property of the `labelElement` and then call the `notifyOutputChanged` so that the changes are cascaded up above the framework layer. 

```TypeScript
public refreshData(context: ControlFramework.IPropBag<InputsOutputs.IInputBag>,) 
{ 
    this._value = (this.inputElement.value as any)as number; 
    this.labelElement.innerHTML = this.inputElement.value; 
    this._notifyOutputChanged(); 
} 
```
In the updateView method, we get the value of the attribute from the context.parameters and then set it to the value variable which stores the control value and also the input elements in the control. 

```TypeScript

public updateView(context: ControlFramework.IPropBag<InputsOutputs.IInputBag>,): void 
  { 
      this._value = context.parameters.controlValue.raw; 
      this._context = context; 
      this.inputElement.setAttribute("value",context.parameters.controlValue.formatted ? context.parameters.controlValue.formatted : ""); 
      this.labelElement.innerHTML = context.parameters.controlValue.formatted ? context.parameters.controlValue.formatted : ""; 
    } 
 ```

 ### Related topics

[PowerApps Control Framework Manifest Schema Reference](../manifest-schema-reference/index.md)<br />
[PowerApps Control Framework API Reference](../index.md)<br />
[PowerApps Control Framework Overview](../powerapps-control-framework-overview.md)
