---
title: " Increment Control| Microsoft Docs" 
description: "Implementing a increment control" 
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "NavaKiran" 
ms.author: "nkrb" 
manager: "" 
---
# Implementing increment control

The increment control shows how to bind data with PowerApps Control Framework, and error handling. 

This control renders as a textbox with a `Increment` button in run time. The text box shows the current value and the `Increment` button is clickable. Whenever you click on the button, the value within the textbox will be increased by 1. The increment value can be changed to any number you wish.

> [!div class="mx-imgBorder"]
> ![Increment Control](../media/increment_control.png "Increment Control")

## Manifest

```xml

<?xml version="1.0" encoding="utf-8" ?>
<manifest>
  <control namespace="SampleNamespace" constructor="TSIncrementControl" version="1.0.0" display-name-key="TS_IncrementControl">
    <type-group name="numbers">
      <type>Whole.None</type>
      <type>Currency</type>
      <type>FP</type>
      <type>Decimal</type>
    </type-group>
    <property name="value" display-name-key="value_Display_Key" description-key="value_Desc_Key" of-type-group="numbers" usage="bound" required="true" hidden="true" />
    <resources>
      <code path="TS_IncrementControl.js" order="1" />
	    <css path="css/TS_IncrementControl.css" order="1" />
      <resx path="strings/TSIncrementControl.1033.resx" version="1.0.0" />
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

/// <reference path="./private_typing/inputsOutputs.d.ts"/>
/// <reference path="../../typing/ControlFramework.d.ts"/>

module SampleNamespace
{
 'use strict';

 export class TSIncrementControl implements ControlFramework.StandardControl<InputsOutputs.IInputs, InputsOutputs.IOutputs> {
 // Value of the field is stored and used inside the control 
	private _value: number;

// PCF framework delegate which will be assigned to this object which would be called whenever any update happens. 
	private _notifyOutputChanged: () => void;

// label element created as part of this control
	private label: HTMLInputElement;

// button element created as part of this control
	private button: HTMLButtonElement;

// Reference to the control container HTMLDivElement
// This element contains all elements of our custom control example
	private _container: HTMLDivElement;

/**
 * Empty constructor.
*/
  constructor()
	{

	 }

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
	 // Creating the label for the control and setting the relevant values.
		this.label = document.createElement("input");
		this.label.setAttribute("type", "label");
		this.label.addEventListener("blur", this.onInputBlur.bind(this));
			
//Create a button to increment the value by 1.
	this.button = document.createElement("button");
			
// Get the localized string from localized string 
	this.button.innerHTML = context.resources.getString("TS_IncrementControl_ButtonLabel");
	this.button.classList.add("SimpleIncrement_Button_Style");
	this._notifyOutputChanged = notifyOutputChanged;
//this.button.addEventListener("click", (event) => { this._value = this._value + 1; this._notifyOutputChanged();});
	this.button.addEventListener("click", this.onButtonClick.bind(this));

// Adding the label and button created to the container DIV.
	this._container = document.createElement("div");
	this._container.appendChild(this.label);
	this._container.appendChild(this.button);
	container.appendChild(this._container);
		}

/**
* Button Event handler for the button created as part of this control
 * @param event
*/
	private onButtonClick(event: Event): void {
			this._value = this._value + 1;
			this._notifyOutputChanged();
		}

/**
* Input Blur Event handler for the input created as part of this control
* @param event
 */
	private onInputBlur(event: Event): void {
	let inputNumber = Number(this.label.value);
	this._value = isNaN(inputNumber) ? (this.label.value as any) as number: inputNumber;
	this._notifyOutputChanged();
	}

/**
* Called when any value in the property bag has changed. This includes field values, data-sets, global values such as container height and width, offline status, control metadata values such as label, visible, etc.
* @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to names defined in the manifest, as well as utility functions
*/

  public updateView(context: ControlFramework.Context<InputsOutputs.IInputs>): void
	{
	 // This method would rerender the control with the updated values after we call NotifyOutputChanged
	//set the value of the field control to the raw value from the configured field
	 this._value = context.parameters.value.raw;
	 this.label.value = this._value != null ? this._value.toString(): "";

	if(context.parameters.value.error)
		{
			this.label.classList.add("SimpleIncrement_Input_Error_Style");
		}
	else
		{
			this.label.classList.remove("SimpleIncrement_Input_Error_Style");
		}
	}

/** 
* It is called by the framework prior to a control receiving new data. 
 * @returns an object based on nomenclature defined in manifest, expecting object[s] for property marked as “bound” or “output”
*/
	public getOutputs(): InputsOutputs.IOutputs
	 {
		// custom code goes here - remove the line below and return the correct output
		let result: InputsOutputs.IOutputs = {
		value: this._value
		};
			return result;
	}

/** 
 * * Called when the control is to be removed from the DOM tree. Controls should use this call for cleanup.
* i.e. cancelling any pending remote calls, removing listeners, etc.
*/
 public destroy(): void
		{
		}
	}
}
```

## Overview

When you click on the button, the value in the text box will be increased by 1. The updated value will flow to PowerApps Control Framework through `notifyOutputChanged`. 
> [!NOTE]
> You can change the increment value when you  are configuring the control to the field on the form.

Edit the value in the text box, if it is a valid integer, then it will update the value to PowerApps Control Framework. 
One could continue click `Increment` button and update it .If it’s an invalid integer, error message will pop out. 
