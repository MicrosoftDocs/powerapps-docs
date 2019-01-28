---
title: " Image Upload Control| Microsoft Docs" 
description: "Implementing image upload control using typescript" 
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "NavaKiran" 
ms.author: "nkrb" 
manager: "" 
---
# Implementing a image upload control

This sample control renders as an `Upload` button to upload image and a default image when the control loads for the first time. When you click on the `Upload`, a file explorer will pop up to pick an image.   
 
The selected image will be rendered within the control. Meanwhile, the `Remove` button will show in case we need to reset. When you click on the `Remove` button, the default image is displayed.  

> [!div class="mx-imgBorder"]
> ![Image Upload Control](../media/image-upload-control.png "Image Upload Control")

## Manifest

```xml
<?xml version="1.0" encoding="utf-8" ?>
<manifest>
  <control namespace="SampleNamespace" constructor="TSImageUploadControl" version="1.0.0" display-name-key="TS_ImageUploadControl">
    <property name="value" display-name-key="value_Display_Key" description-key="value_Desc_Key" of-type="Multiple" usage="bound" required="true" hidden="true" />
    <resources>
      <code path="TS_ImageUploadControl.js" order="1" />
	    <css path="css/TS_ImageUploadControl.css" order="1" />
      <img path="img/default.png" />
      <resx path="strings/TSImageUploadControl.1033.resx" version="1.0.0" />
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
// Define const here

// Default Image FileName
const DefaultImageFileName:string = "default.png";

// Show Error css classname
const ShowErrorClassName = "ShowError";

// No Image css classname
const NoImageClassName = "NoImage";

// 'RemoveButton' css class name
const RemoveButtonClassName = "RemoveButton";


export class TSImageUploadControl implements ControlFramework.StandardControl<InputsOutputs.IInputs, InputsOutputs.IOutputs>
{
// Value of the field is stored and used inside the control
private _value: string | null;

// PCF framework context, "Input Properties" containing the parameters, control metadata and interface functions.
private _context: ControlFramework.Context<InputsOutputs.IInputs>;

// PCF framework delegate which will be assigned to this object which would be called whenever any update happens.
private _notifyOutputChanged: () => void;

// Control's container
private controlContainer: HTMLDivElement;

// button element created as part of this control
private uploadButton: HTMLButtonElement;

// button element created as part of this control
private removeButton: HTMLButtonElement;

// label element created as part of this control
private imgElement: HTMLImageElement;

// label element created as part of this control
private errorLabelElement: HTMLLabelElement;

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
this._context = context;
this._notifyOutputChanged = notifyOutputChanged;
this.controlContainer = document.createElement("div");

//Create an upload button to upload the image
this.uploadButton = document.createElement("button");
// Get the localized string from localized string
this.uploadButton.innerHTML = context.resources.getString("PCF_ImageUploadControl_Upload_ButtonLabel");
this.uploadButton.addEventListener("click", this.onUploadButtonClick.bind(this));

// Creating the label for the control and setting the relevant values.
this.imgElement = document.createElement("img");

//Create a remove button to reset the image
this.removeButton = document.createElement("button");
this.removeButton.classList.add(RemoveButtonClassName);
// Get the localized string from localized string
this.removeButton.innerHTML = context.resources.getString("PCF_ImageUploadControl_Remove_ButtonLabel");
this.removeButton.addEventListener("click", this.onRemoveButtonClick.bind(this));

// Create an error label element
this.errorLabelElement = document.createElement("label");

// If there is a raw value bound means there already have an image
if(this._context.parameters.value.raw)
{
this.imgElement.src = context.parameters.value.raw;
}
else
{
this.setDefaultImage();
}

// Adding the label and button created to the container DIV.
this.controlContainer.appendChild(this.uploadButton);
this.controlContainer.appendChild(this.imgElement);
this.controlContainer.appendChild(this.removeButton);
this.controlContainer.appendChild(this.errorLabelElement);
container.appendChild(this.controlContainer);
}

/**
* Called when any value in the property bag has changed. This includes field values, data-sets, global values such as container height and width, offline status, control metadata values such as label, visible, etc.
* @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to names defined in the manifest, as well as utility functions
*/
public updateView(context: ControlFramework.Context<InputsOutputs.IInputs>): void
{
// Always need to update the _context obj
this._context = context;
}

/**
* Button Event handler for the button created as part of this control
* @param event
*/
private onUploadButtonClick(event: Event): void
{
// context.device.pickFile(successCallback, errorCallback) is used to initiate the File Explorer
// successCallback will be triggered if there successfully pick a file
// errorCallback will be triggered if there is an error
this._context.device.pickFile().then(this.processFile.bind(this), this.showError.bind(this));
}

/**
* Button Event handler for the button created as part of this control
* @param event
*/
private onRemoveButtonClick(event: Event): void
{
this.setDefaultImage();
}

/**
*
* @param files
*/
private processFile(files: ControlFramework.FileObject[]): void
{
if(files.length > 0)
{
let file: ControlFramework.FileObject = files[0];

try
{
let fileExtension :string|undefined;

if(file && file.fileName)
{
fileExtension = file.fileName.split('.').pop();
}

if(fileExtension)
{
this.setImage(true, fileExtension, file.fileContent);
this.controlContainer.classList.remove(NoImageClassName);
}
else
{
this.showError();
}
}
catch(err)
{
this.showError();
}
}
}

/**
* Set Default Image
*/
private setDefaultImage():void
{
this._context.resources.getResource(DefaultImageFileName, this.setImage.bind(this, false, "png"), this.showError.bind(this));
this.controlContainer.classList.add(NoImageClassName);

// If it already has value, we need to update the output
if(this._context.parameters.value.raw)
{
this._value = null;
this._notifyOutputChanged();
}
}

/**
* Set the Image content
* @param shouldUpdateOutput indicate if needs to inform the infra of the change
* @param fileType file extension name like "png", "gif", "jpg"
* @param fileContent file content, base64 format
*/
private setImage(shouldUpdateOutput:boolean, fileType: string, fileContent: string): void
{
let imageUrl:string = this.generateImageSrcUrl(fileType, fileContent);
this.imgElement.src = imageUrl;

if(shouldUpdateOutput)
{
this.controlContainer.classList.remove(ShowErrorClassName);
this._value = imageUrl;
this._notifyOutputChanged();
}
}

/**
* Genereate Image Element src url
* @param fileType file extension
* @param fileContent file content, base 64 format
*/
private generateImageSrcUrl(fileType: string, fileContent: string): string
{
return  "data:image/" + fileType + ";base64, " + fileContent;
}

/**
*  Show Error Message
*/
private showError(): void
{
this.errorLabelElement.innerText = this._context.resources.getString("PCF_ImageUploadControl_Can_Not_Find_File");
this.controlContainer.classList.add(ShowErrorClassName);
}

/**
* It is called by the framework prior to a control receiving new data.
* @returns an object based on nomenclature defined in manifest, expecting object[s] for property marked as “bound” or “output”
*/
public getOutputs(): InputsOutputs.IOutputs
{
// return outputs
let result: InputsOutputs.IOutputs =
{
value: this._value
};

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
This sample shows how to create an image picker and showcases the device API and resources API to load the image defined in Manifest. Image content is stored in base64 encoding and could be saved and visited again.  

The  `resources.getResource`method takes the input as the webresource name defined in the control manifest and loads that webresource. Control renders an `Upload` button and the default image for initial rendering. Images are defined in the manifest’s [resource](../reference/resources.md) node.  

```xml
    <resources>  
      <code path="TS_ImageUploadControl.js" order="1" />  
      <css path="css/TS_ImageUploadControl.css" order="1" />  
      <img path="img/default.png" />  
      <resx path="strings/TS_ImageUploadControl.1033.resx" version="1.0.1" />  
    </resources> 
 ```
 
The `successCallback` will be triggered and the resource content will be injected in the `successCallback`. Then you use the image element 'src' points to the content and the default image loads.
 
The `device.pickFile` method opens a dialog box to select files from your computer (web client) or mobile device (mobile clients). For desktop, it opens the file explorer, for mobile client, it opens the library of the photo. When you click on the `upload` button, the device API `pickFile` will be triggered and user will pick up the file. Once file is successfully picked, the file's filename, file content will be injected in the `successCallback`. 

> [!NOTE]
> If the same form/entity is also used on legacy web client, then the field will show out-of-box text control on legacy web client, where there might have UX issues.  To make it hidden on legacy web client, we could uncheck the ‘Visibility’ checkbox and check ‘Hide Default Control’ checkbox together.   
