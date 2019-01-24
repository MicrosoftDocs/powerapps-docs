---
title: " Navigation API Control| Microsoft Docs" 
description: "Implementing navigation api control" 
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "NavaKiran" 
ms.author: "nkrb" 
manager: "" 
---

# Implementing Navigation API  control

The Navigation API control explores the various methods available as part of the PowerApps Control Framework’s navigation API.  
In this sample we create a series of input elements of type buttons which call into the respective methods of the PCF’s navigation API that matches with the value displayed.  

> [!div class="mx-imgBorder"]
> ![Navigation API Control](../media/navigation_api_control.png "Navigation API Control")

## Manifest
```xml
<?xml version="1.0" encoding="utf-8" ?>
<manifest>
	<control namespace="SampleNamespace" constructor="TSNavigationAPI" version="1.0.0" display-name-key="TS_NavigationAPI" description-key="TS_NavigationAPI_Desc" control-type="standard">
		<type-group name="numbers">
			<type>Whole.None</type>
			<type>Currency</type>
			<type>FP</type>
			<type>Decimal</type>
		</type-group>
		<property name="controlValue" display-name-key="controlValue_Display_Key" description-key="controlValue_Desc_Key" of-type-group="numbers" usage="bound" required="true" />
		<resources>
			<code path="TS_NavigationAPI.js" order="1" />
			<css path="css/TS_NavigationAPI.css" order="1" />
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
    export class TSNavigationAPI implements ControlFramework.StandardControl<InputsOutputs.IInputBag, InputsOutputs.IOutputBag> {

		// PCF framework delegate which will be assigned to this object which would be called whenever any update happens. 
        private _notifyOutputChanged: () => void;

		// Reference to the div element that hold together all the HTML elements that we are creating as part of this control
        private divElement: HTMLDivElement;

        // Reference to the button that invokes the openAlertDialog command
        private openAlertDialogButton: HTMLButtonElement;

        // Reference to the button that invokes the openConfirmDialog command
        private openConfirmDialogButton: HTMLButtonElement;

        // Reference to the button that invokes the openFile command
        private openFileButton: HTMLButtonElement;

        // Reference to the button that invokes the openUrl command
        private openUrlButton: HTMLButtonElement;

        // Reference to the control container HTMLDivElement
		// This element contains all elements of our custom control example
		private _container: HTMLDivElement;

        // Reference to ControlFramework Context object
        private _context : ControlFramework.Context<InputsOutputs.IInputBag>;
        

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
            this._notifyOutputChanged = notifyOutputChanged;
            this._context = context;
            this._container = container;

            this.divElement = document.createElement("div");
            this.divElement.setAttribute("class","TSNavigationAPI");

            // Create the HTML button elements for openAlertDialog button
            this.openAlertDialogButton = document.createElement("button");
            this.openAlertDialogButton.setAttribute("id","openAlertDialogButton");
            this.openAlertDialogButton.innerHTML = "openAlertDialogButton";
            
            // Create the HTML button elements for openConfirmDialog button
            this.openConfirmDialogButton = document.createElement("button");
            this.openConfirmDialogButton.setAttribute("id","openConfirmDialogButton");
            this.openConfirmDialogButton.innerHTML = "openConfirmDialogButton";

            // Create the HTML button elements for openFile button
            this.openFileButton = document.createElement("button");
            this.openFileButton.setAttribute("id","openFileButton");
            this.openFileButton.innerHTML = "openFileButton";

            // Create the HTML button elements for openUrl button
            this.openUrlButton = document.createElement("button");
            this.openUrlButton.setAttribute("id","openUrlButton");
            this.openUrlButton.innerHTML = "openUrlButton";

            // bind the function which invokes the respective API's to each of the buttons
            this.openAlertDialogButton.addEventListener("click",this.raiseEvent.bind(this));
            this.openConfirmDialogButton.addEventListener("click",this.raiseEvent.bind(this));
            this.openFileButton.addEventListener("click",this.raiseEvent.bind(this));
            this.openUrlButton.addEventListener("click",this.raiseEvent.bind(this));

            // append all the button elements to the parent div element for control.
            this.divElement.appendChild(this.openAlertDialogButton);
            this.divElement.appendChild(this.openConfirmDialogButton);
            this.divElement.appendChild(this.openFileButton);
            this.divElement.appendChild(this.openUrlButton);

            // append the parent div element in the control to the control's container
            this._container.appendChild(this.divElement);
        }

        /**
		 * Handles the events raised by each of the buttons that are binded according to their id
		 * @param event : event object that contains all the properties regarding the raised event
		 */
        public raiseEvent(event: Event,)
        {
            var inputSource = event.srcElement.id; 
            switch(inputSource)
            {
                case "openAlertDialogButton": this._context.navigation.openAlertDialog({text:"This is an alert.", confirmButtonLabel : "Yes",}).then(
                    function success()
                    {
                        document.getElementById("openAlertDialogButton").innerHTML = "Alert dialog closed";
                    },
                    function()
                    {
                        document.getElementById("openAlertDialogButton").innerHTML = "Error in Alert Dialog";
                    }
                );
                break;

                case "openConfirmDialogButton": this._context.navigation.openConfirmDialog({title:"Confirmation Dialog", text:"This is a confirmation.",},{height:200, width:450}).then(
                    function(success)
                    {
                        if(success.confirmed)
                        {
                            document.getElementById("openConfirmDialogButton").innerHTML = "Ok button clicked.";
                        }
                        else
                        {
                            document.getElementById("openConfirmDialogButton").innerHTML = "Cancel or X button clicked.";
                        }
                    }
                );
                break;

                case "openFileButton": 
                    var file = {
                                fileContent: "U2FtcGxlIGNvbnRlbnQgZm9yIERlbW8=", //Contents of the file in base64 encoded format. 
                                fileName: "Sample.txt", //Name of the file.
                                fileSize: 29, //Size of the file in KB.
                                mimeType: "text/plain" //MIME type of the file.
                                };
                    this._context.navigation.openFile(file,{openMode:2});
                break;

                case "openUrlButton": this._context.navigation.openUrl("https://www.microsoft.com");
                break;
            };
            
            //this._notifyOutputChanged();
        }

		/**
		 * Called when any value in the property bag has changed. This includes field values, data-sets, global values such as container height and width, offline status, control metadata values such as label, visible, etc.
		 * @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to names defined in the manifest, as well as utility functions
		 */
        public updateView(context: ControlFramework.Context<InputsOutputs.IInputBag>,): void
        {
            this._context = context;
        }

		/** 
		 * It is called by the framework prior to a control receiving new data. 
		 * @returns an object based on nomenclature defined in manifest, expecting object[s] for property marked as “bound” or “output”
		 */
        public getOutputs(): InputsOutputs.IOutputBag
        {
            // no-op: method not leveraged by this example custom control
            return { };
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

## Overview

The `openAlertDialog` method provides the capability to display an alert dialog containing a message and a button. You can also implement callback methods when the alert dialog is closed or on if an error is encountered when loading the dialog. 
  
In this sample when you click on the `openAlertDialogButton` a alert dialog pops up and sets the value of it to `Alert dialog closed` when the dialog is closed either using the `OK` button or the `X` button.

> [!NOTE]
> This is similar to calling the Xrm.Navigation.openAlertDialog method in ClientAPI.  

The `openConfirmDialog` method provides the ability to display an alert dialog containing a message and two buttons. You can use this method to implement different logics based on the button clicked. You can implement the success callback which is called when the dialog is closed by clicking either of the buttons.
  
This sample shows you a confirm dialog when you click on the `openConfirmDialogButton` and sets the value of it to `Ok` button clicked or `Cancel or X` button clicked depending on the button that was clicked.

> [!NOTE]
> This is similar to calling the Xrm.Navigation.openConfirmDialog method in ClientAPI.
  
The openFile method provides the ability to open a file. You’d need to pass in the file object which has the filename, content, mimetype and the filesize. You can also pass in the optional parameter of the mode you want to open the file as 1 or 2, 1 being the default which opens the file in read/open mode.
  
This sample opens a file named `SampleDemo.txt` in save mode on clicking the `openFileButton`.

> [!NOTE]
> This is similar to calling the Xrm.Navigation.openFile method in ClientAPI.

The openUrl method provides the ability to open a URL. You’d need to pass the URL as a string to the method and also pass the optional parameters of height, width and openInNewWindow as true if you want the url to be opened in a new window.
  
This sample opens a new window and loads the microsoft.com home page on clicking the `openUrlButton`.

> [!NOTE]
> This is similar to calling the Xrm.Navigation.openUrl method in ClientAPI.

### Related topics

[PowerApps Control Framework Manifest Schema Reference](../manifest-schema-reference/index.md)<br />
[PowerApps Control Framework API Reference](../index.md)<br />
[PowerApps Control Framework Overview](../powerapps-control-framework-overview.md)
