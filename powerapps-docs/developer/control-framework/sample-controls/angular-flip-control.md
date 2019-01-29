---
title: " Flip Control| Microsoft Docs" 
description: "Implementing a Flip control using Angular JS" 
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "NavaKiran" 
ms.author: "nkrb" 
manager: "" 
---
# Implementing Flip Control

This sample shows how to use third-party libraries to create controls in **PowerApps Control Framework**.  

The control is based on angular.js, angular-ui, angular-animate, angular-sanitize, bootstrap for sampling purpose only. The code may not reveal the best practices for the mentioned third-party libraries.

> [!div class="mx-imgBorder"]
> ![Angular Flip](../media/angular-flip.png "Angular Flip")

## Manifest

```XML
<?xml version="1.0" encoding="utf-8" ?>
<manifest>
	<control namespace="SampleNamespace" constructor="JSAngularJSFlipControl" version="1.0.0" display-name-key="JS_AngularJSFlipControl" description-key="JS_AngularJSFlipControl_Desc" control-type="standard">
		<property name="flipModel" display-name-key="flipModel_Display_Key" description-key="flipModel_Desc_Key" of-type="TwoOptions" usage="bound" required="true" />
		<resources>
			<library name="AngularJSCore" version=">=1" order="1">
				<packaged_library path="libs/angular.min.js" version="1.5.8" />
			</library>
			<library name="AngularJSAnimate" version=">=1" order="2">
				<packaged_library path="libs/angular-animate.min.js" version="1.6.6" />
			</library>
			<library name="AngularJSSanitize " version=">=1" order="3">
				<packaged_library path="libs/angular-sanitize.min.js" version="1.5.5" />
			</library>
			<library name="AngularUIBootstrap" version=">=1" order="4">
				<packaged_library path="libs/ui-bootstrap-tpls.min.js" version="1.3.3" />
			</library>
			<code path="JS_AngularJSFlipControl.js" order="5" />
			<css path="css/bootstrap-associated.css" order="1" />
		</resources>
	</control>
</manifest>
```

## Overview

This sample provides examples on how to add dependencies for third-party libraries, showcasing how to perform data-binding between PowerApps Control Framework, control model and third party inner data model in bi-direction. 

The flip control sample consists of a label and a button. When you click on the button, the text on the label will toggle. 

- When the control is loaded, the label shows the text based on the bind attribute value. The `context.parameters.[property_name].attributes` contains the associated metadata. 
- For TwoOptions, `context.parameters.[property_name].Options` will include both true and false value option. 
- Clicking on the Flip button, the label will update value using **notifyOutputEvents** method [getOutputs](../reference/control/getoutputs.md) method will be called asynchronously and will flow to PowerApps Control Framework. 
- ClientAPI updates the bind attribute value, the updated value will flow to the control label. You could also use ClientAPI to update an attribute value and it will trigger control’s [updateView](../reference/control/updateview.md). Then control could then update third-party model and the label will be updated. 


## Code

```JavaScript

"use strict";

var SampleNamespace = SampleNamespace || {};

/**
* Constructor of JSAngularJSFlipControl
*
*/
SampleNamespace.JSAngularJSFlipControl = function() {
// Element id of the ng-app div. Type: string
var _appDivId;

// ng-app app id. Type: string
var _appId;

// ng-controller. Type: string
var _controllerId;

// PCF framework delegate which will be assigned to this object which would be called whenever any update happens. Type: function
var _notifyOutputChanged;

// Model of the bind field. Type: Bollean
var _currentValue;

// Option Label Text when Option is True. The Text is from attribute customization. Type: string
var _optionTrueLabel;

// Option Label Text when Option is False. The Text is from attribute customization. Type: string
var _optionFalseLabel;
}

/**
* Used to initialize the control instance. Controls can kick off remote server calls and other initialization actions here.
* Data-set values are not initialized here, use updateView.
* @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to property names defined in the manifest, as well as utility functions.
* @param notifyOutputChanged A callback method to alert the framework that the control has new outputs ready to be retrieved asynchronously.
* @param state A piece of data that persists in one session for a single user. Can be set at any point in a controls life cycle by calling 'setControlState' in the Mode interface.
* @param container If a control is marked control-type='starndard', it will receive an empty div element within which it can render its content.
*/
SampleNamespace.JSAngularJSFlipControl.prototype.init = function (context, notifyOutputChanged, state, container) {

var _this = this;

// We need a random integer from 1-100, so that for a form of multiple fields bind to same attribute, we could differentiate
var randomInt = Math.floor(Math.floor(100)*Math.random());
this._appDivId = this.createUniqueId(context, "angularflip_controlid", randomInt);
this._appId = this.createUniqueId(context, "JSAngularJSFlipControl", randomInt);
this._controllerId = this.createUniqueId(context, "powerApps.angularui.demo", randomInt);
this._notifyOutputChanged = notifyOutputChanged;

// Assign Model the value of the bind attribute
this._currentValue = context.parameters.flipModel.raw;

// Initialize the True/False Label texts from the attribute metadata
this.initializeOptionsLabel(context);

// Create HTML structure for the control
var appDiv = document.createElement('div');
appDiv.setAttribute("id",this._appDivId);
appDiv.setAttribute("ng-controller",this._appId);
appDiv.setAttribute("ng-app",this._controllerId);

// Below sample html are from Angular-UI single toggle sample code
// https://angular-ui.github.io/bootstrap/
appDiv.innerHTML="<pre>{{labelModel}}</pre><button type='button' class='btn btn-primary' ng-model='flipButtonModel' uib-btn-checkbox btn-checkbox-true='1' btn-checkbox-false='0'>Flip</button>";

// Container appends the HTML structure
container.appendChild(appDiv);

// Angular code. Angular module/controller initialization.
angular.module(this._controllerId, ['ngAnimate', 'ngSanitize', 'ui.bootstrap']);
angular.module(this._controllerId).controller(this._appId, function ($scope){

// Intialize 'labelModel'. Assign initial option text to the Angular $scope labelModel. It will be revealed in '<pre>{{labelModel}}</pre>'
$scope.labelModel = _this._currentValue ? _this._optionTrueLabel : _this._optionFalseLabel;

// Intialize 'flipButtonModel'. Assign bind attribute value to Angular $scope flipButtonModel. The Flip button also bind to this 'flipButtonModel', so when we click, it will flip
$scope.flipButtonModel = _this._currentValue ? 1 : 0;

// Watch the click of the flip button
$scope.$watchCollection('flipButtonModel', function () {

// Update the label text when Flip Button clicks
if($scope.flipButtonModel){
$scope.labelModel =  _this._optionTrueLabel;
}
else{
$scope.labelModel = _this._optionFalseLabel;
}

// Call updateOutputIfNeeded and inform PCF framework that bind attribute value need update
_this.updateOutputIfNeeded($scope.flipButtonModel);

});
});

// Angular code. Create an App based on the new appDivId
angular.element(document).ready(function() {
angular.bootstrap(document.getElementById(_this._appDivId),[_this._controllerId]);
});
};

/**
* Get UniqueId so as to avoid id conflict between multiple fields bind to same attribute
* @param context The "Input Properties" containing the parameters, control metadata and interface functions.
* @param passInString input string as suffix
* @param randomInt random integer
* @returns a string of uniqueId includes attribute logicalname + passIn specialized string + random Integer
*/
SampleNamespace.JSAngularJSFlipControl.prototype.createUniqueId = function (context, passInString, randomInt) {
return context.parameters.flipModel.attributes.LogicalName + "-" + passInString + randomInt;
}

/**
* Initialize Options Label to use the attribute label from Metadata
* @param context The "Input Properties" containing the parameters, control metadata and interface functions.
*/
SampleNamespace.JSAngularJSFlipControl.prototype.initializeOptionsLabel = function (context) {
var _this = this;

// Get option label texts from metadata
var optionsMetadata = context.parameters.flipModel.attributes.Options;
optionsMetadata.forEach(function(option){
if(option.Value){
_this._optionTrueLabel = option.Label;
}
else{
_this._optionFalseLabel = option.Label;
}
});
};

/**
* Called when any value in the property bag has changed. This includes field values, data-sets, global values such as container height and width, offline status, control metadata values such as label, visible, etc.
* @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to names defined in the manifest, as well as utility functions
*/
SampleNamespace.JSAngularJSFlipControl.prototype.updateView = function (context) {

// An attribute value from Control Framework could be updated even after init cycle, clientAPI, post Save response can update the attribute value and the Flip control should reveal the new value.
this.updateFlipButtonModelIfNeeded(context.parameters.flipModel.raw);
};

/**
* Update Angular 'flipButtonModel' if needed
* @param newValue new value
*/
SampleNamespace.JSAngularJSFlipControl.prototype.updateFlipButtonModelIfNeeded = function (newValue) {
if((newValue && !this._currentValue) || (!newValue && this._currentValue)){
this._currentValue = newValue;

// Angular Code. Update the 'flipButtonModel' value
var $scope = angular.element(document.getElementById(this._appDivId)).scope();
$scope.$apply(function() {
// 'flipButtonModel' value is either 1 or 0
$scope.flipButtonModel = newValue ? 1:0;
});
}
};

/**
* Update value in Power Control Framework
* @param newValue new value
*/
SampleNamespace.JSAngularJSFlipControl.prototype.updateOutputIfNeeded = function (newValue) {
if((newValue && !this._currentValue) || (!newValue && this._currentValue)){
this._currentValue = newValue ? true:false;
this._notifyOutputChanged();
}
};

/**
* It is called by the framework prior to a control receiving new data.
* @returns an object based on nomenclature defined in manifest, expecting object[s] for property marked as “bound” or “output”
*/
SampleNamespace.JSAngularJSFlipControl.prototype.getOutputs = function () {
var returnValue = this._currentValue;
return {
flipModel: returnValue
};
};

/**
* Called when the control is to be removed from the DOM tree. Controls should use this call for cleanup.
* i.e. cancelling any pending remote calls, removing listeners, etc.
*/
SampleNamespace.JSAngularJSFlipControl.prototype.destroy = function () {

};
```

### Related topics

[PowerApps Control Framework Manifest Schema Reference](../manifest-schema-reference/index.md)<br />
[PowerApps Control Framework API Reference](../index.md)<br />
[PowerApps Control Framework Overview](../powerapps-control-framework-overview.md)
