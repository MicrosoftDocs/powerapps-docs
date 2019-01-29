---
title: " Localization API Control| Microsoft Docs" 
description: "Implementing localzation api control" 
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "NavaKiran" 
ms.author: "nkrb" 
manager: "" 
---
# Implementing localization API control

This sample showcases how localization can be done for custom controls. In this sample we use the [Increment control](increment-control.md) to localize the text that is displayed on the increment button based on the user’s selected language. 

PowerApps Control Framework (PCF) uses the concept of implementing String(resx) web resources that can be used to manage localized strings to be shown on any user interface. More information: [String(Resx) Webresources](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/resx-web-resources). 

> [!div class="mx-imgBorder"]
> ![Localization API Control](../media/localization-api-control.png "Localization API Control")

## Manifest 

```xml
<?xml version="1.0" encoding="utf-8" ?>
<manifest>
  <control namespace="SampleNamespace" constructor="TSLocalizationAPI" version="1.0.0" display-name-key="TS_LocalizationAPI_Display_Key" description-key="TS_LocalizationAPI_Desc_Key">
    <type-group name="numbers">
      <type>Whole.None</type>
      <type>Currency</type>
      <type>FP</type>
      <type>Decimal</type>
    </type-group>
    <property name="value" display-name-key="value_Display_Key" description-key="value_Desc_Key" of-type-group="numbers" usage="bound" required="true" hidden="true" />
    <resources>
      <code path="TS_LocalizationAPI.js" order="1" />
	    <css path="css/TS_LocalizationAPI.css" order="1" />
      <resx path="strings/TSLocalizationAPI.1033.resx" version="1.0.0" />
      <resx path="strings/TSLocalizationAPI.1035.resx" version="1.0.0" />
      <resx path="strings/TSLocalizationAPI.3082.resx" version="1.0.0" />
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
	'use strict';

 export class TSLocalizationAPI implements ControlFramework.StandardControl<InputsOutputs.IInputs, InputsOutputs.IOutputs> {
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
	this.button.innerHTML = context.resources.getString("PCF_LocalizationSample_ButtonLabel");
    this.button.classList.add("LocalizationSample_Button_Style");
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
 ** Called when any value in the property bag has changed. This includes field values, data-sets, global values such as container height and width, offline status, control metadata values such as label, visible, etc.
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
	this.label.classList.add("LocalizationSample_Input_Error_Style");
	}
else
 {
	this.label.classList.remove("LocalizationSample_Input_Error_Style");
	}
}

/** 
*  * It is called by the framework prior to a control receiving new data. 
* @returns an object based on nomenclature defined in manifest, expecting object[s] for property marked as “bound” or “output”
*/
public getOutputs(): InputsOutputs.IOutputs
 {
	// custom code goes here - remove the line below and return the correct output
	let result: InputsOutputs.IOutputs = {value: this._value};
	return result;
	}

/** 
* Called when the control is to be removed from the DOM tree. Controls should use this call for cleanup.
 * i.e. cancelling any pending remote calls, removing listeners, etc.
*/
public destroy(): void
		{
		}
	}
}
```

## Overview

To localize an existing project, all you need to do is to create additional resource(resx) files, one each for a specific language as mentioned in the string web resources and include them as part of the control’s manifest file under the [resources](../reference/resources.md) node.  

The PCF identifies the user’s language and returns the strings from that language specific resource file when you try to access a string using `context.resources.getString` method.

In this sample, two languages `Spanish` and `Finnish` which has the language codes 3082 and 1035 respectively are defined.

we have made a copy of the `Increment Control` sample and renamed it to `Localization API`. All the corresponding files including the files in the sub folders have been renamed accordingly.

As you can see in the strings folder under TS_LocalizationAPI, two additional resx files with the suffixes corresponding to Spanish and Finnish as 3082 and 1035 respectively are added. So, the new files that are created should have their file names ending as {filename}.3082.resx and {filename}.1035.resx because the framework relies on this naming convention to identify which resource file should be picked for reading the strings for the user.

Ensure that the keys used for strings in all these resource files share the same name across all the languages.

Now, when the control is being rendered on the UI, we see in the code that we retrieve the value to be displayed on the button using `context.resources.getString("PCF_LocalizationSample_ButtonLabel")`.

When this line of code is executed, the PCF automatically identifies the language of the user and picks up the value for the button label using the key provided in the corresponding language file we defined. Below is the text you see for each of the 3 languages we support for this sample control.
  
|LanguageCode |Value Displayed |
|---|---|
|3082 |Incremento |
|1033 |Increment |
|1035 |lisäys | 
