---
title: " Flip Control| Microsoft Docs" 
description: "Implementing IFRAME control" 
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "NavaKiran" 
ms.author: "nkrb" 
manager: "" 
---
# Implementing a IFRAME control

This sample describes how to bind a custom control to different fields on the form and use the value of these fields as input properties to the control.  

## Manifest

```xml
<?xml version="1.0" encoding="utf-8" ?>
<manifest>
	<control namespace="SampleNamespace" constructor="TSIFrameControl" version="1.0.0" display-name-key="TS_IFrameControl" description-key="TS_IFrameControl_Desc" control-type="standard">
		<property name="stringProperty" display-name-key="stringProperty_Display_Key" description-key="stringProperty_Desc_Key" of-type="SingleLine.Text" usage="bound" required="true" />
		<property name="latitudeValue" display-name-key="Bing_Maps_Latitude_Value" description-key="latitude" of-type="FP" usage="bound" required="true" />
		<property name="longitudeValue" display-name-key="Bing_Maps_Longitude_Value" description-key="longitude" of-type="FP" usage="bound" required="true" />
		<resources>
			<code path="TS_IFrameControl.js" order="1" />
			<css path="css/TS_IFrameControl.css" order="2" />
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
    export class TSIFrameControl implements ControlFramework.StandardControl<InputsOutputs.IInputs, InputsOutputs.IOutputs> 
    {
        // Reference to Bing Map IFrame HTMLElement
        private _bingMapIFrame: HTMLElement;

		// Reference to the control container HTMLDivElement
		// This element contains all elements of our custom control example
        private _container: HTMLDivElement;

        // Flag if control view has been rendered
        private _controlViewRendered: Boolean;
        
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
            this._container = container;
            this._controlViewRendered = false;
        }

		/**
		 * Called when any value in the property bag has changed. This includes field values, data-sets, global values such as container height and width, offline status, control metadata values such as label, visible, etc.
		 * @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to names defined in the manifest, as well as utility functions
		 */
        public updateView(context: ControlFramework.Context<InputsOutputs.IInputs>,)
        {
            if (!this._controlViewRendered)
			{
                this._controlViewRendered = true;
                this.renderBingMapIFrame();
            }

            let latitude: number = context.parameters.latitudeValue.raw;
            let longitude: number = context.parameters.longitudeValue.raw;
            this.updateBingMapURL(latitude, longitude);
        }

        /** 
         * Render IFrame HTML Element that hosts the Bing Map and appends the IFrame to the control container 
         */
        private renderBingMapIFrame(): void
        {
            this._bingMapIFrame = this.createIFrameElement();
            this._container.appendChild(this._bingMapIFrame);
        }

        /**
         * Updates the URL of the Bing Map IFrame to display the updated lat/long coordinates
         * @param latitude : latitude of center point of Bing map
         * @param longitude : longitude of center point of Bing map
         */
        private updateBingMapURL(latitude:number, longitude:number): void
        {
            // Bing Map API:
            // https://msdn.microsoft.com/en-us/library/dn217138.aspx

            // Provide bing map query string parameters to format and style map view
            let bingMapUrlPrefix = "https://www.bing.com/maps/embed?h=400&w=300&cp=";
            let bingMapUrlPostfix = "&lvl=12&typ=d&sty=o&src=SHELL&FORM=MBEDV8";

            // Build the entire URL with the user provided latitude and longitude
            let iFrameSrc:string = bingMapUrlPrefix + latitude + "~"+ longitude + bingMapUrlPostfix;

            // Update the IFrame to point to the updated URL
            this._bingMapIFrame.setAttribute("src", iFrameSrc);
        }

        /** 
         * Helper method to create an IFrame HTML Element
         */
        private createIFrameElement(): HTMLElement
        {
            let iFrameElement:HTMLElement = document.createElement("iframe")
			iFrameElement.setAttribute("class", "TS_SampleControl_IFrame");
            return iFrameElement
        }

		/** 
		 * It is called by the framework prior to a control receiving new data. 
		 * @returns an object based on nomenclature defined in manifest, expecting object[s] for property marked as “bound” or “output”
		 */
        public getOutputs(): InputsOutputs.IOutputs
        {
         	// no-op: method not leveraged by this example custom control
            return {};
        }

		/** 
 		 * Called when the control is to be removed from the DOM tree. Controls should use this call for cleanup.
		 * i.e. cancelling any pending remote calls, removing listeners, etc.
		 */
        public destroy()
        {
            // no-op: method not leveraged by this example custom control
        }
    }
}
```

> [!NOTE]
> Composite fields are not yet supported by PCF, so you will not be able to bind this control to the out of the box latitude and longitude address fields. You will need to bind the custom control to different floating-point field.


## Overview

This sample control renders an `IFRAME` which displays `Bing Maps URL`. The control is bound to two floating point fields on the form, which are passed as parameters to the control and injected into the `IFRAME URL` to update the Bing Map to the latitude and longitude of the provided inputs.  
Update the ControlManifest file to include binding to two additional fields on the form.  
This change informs the PowerApps Control Framework (PCF) that these bound fields need to be passed to the control during initialization and whenever one of the values is updated.
  
```xml
<property name="latitudeValue" display-name-key="Bing_Maps_Latitude_Value" description-key="latitude" of-type="FP" usage="bound" required="true" />  
<property name="longitudeValue" display-name-key="Bing_Maps_Longitude_Value" description-key="longitude" of-type="FP" usage="bound" required="true" />  
```

Additional bound properties may be required or not. This will be enforced during control configuration when the control is being bound to the form. This can be configured by the `required` attribute of the property node in the control Manifest. Set the value to false if you don't want to require the control property be bound to a field.  
ControlFramework.d.ts needs to be updated to add two fields to IInputs interface. This is the format the PCF will pass the field values in. Adding these values to the IInputs interface allows your TypeScript file to reference the values and compile successfully.  

```TypeScript
    export interface IInputs   
    { latitudeValue: ControlFramework.PropertyTypes.NumberProperty;  
        longitudeValue: ControlFramework.PropertyTypes.NumberProperty;  
    }  
    ```
The initial rendering generates an `IFRAME` element and appends it to the controls container. This `IFRAME` is used to display the Bing Map. The URL of the `IFRAME` is set to a `Bing Map URL` and includes the bound fields (latitudeValue and longitudeValue) in the URL to center the map at the provided location. 

The [updateView](../reference/control/updateview.md) method is invoked whenever one of these fields are updated on the form. This method updates the URL of the Bing Map IFRAME to use the new latitude and longitude values passed to the control. 
To view this control in run time, bind the control to a field on the form like any other custom control.

### Related topics

[PowerApps Control Framework Manifest Schema Reference](../manifest-schema-reference/index.md)<br />
[PowerApps Control Framework API Reference](../index.md)<br />
[PowerApps Control Framework Overview](../powerapps-control-framework-overview.md)


