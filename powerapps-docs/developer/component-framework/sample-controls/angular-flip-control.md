---
title: " Flip component| Microsoft Docs" 
description: "Implementing a Flip component using Angular JS" 
ms.custom: ""
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.topic: "article"
ms.author: "nabuthuk" 
author: Nkrb
---

# Implementing Flip component

This sample shows how to use third-party libraries to create components in PowerApps component framework.  The flip sample component is implemented based on angular.js, angular-ui, angular-animate, angular-sanitize, bootstrap. The code may not reveal the best practices for the mentioned third-party libraries.

> [!div class="mx-imgBorder"]
> ![Angular Flip](../media/angular-flip.png "Angular Flip")

## Available for 

Model-driven apps and canvas apps (experimental preview) 

## Manifest

```XML
<?xml version="1.0" encoding="utf-8"?>
<manifest>
	<control namespace="SampleNamespace" constructor="JSAngularJSFlipControl" version="1.0.0" display-name-key="JS_AngularJSFlipControl_Display_Key" description-key="JS_AngularJSFlipControl_Desc_Key" control-type="standard">
		<property name="flipModel" display-name-key="flipModel_Display_Key" description-key="flipModel_Desc_Key" of-type="TwoOptions" usage="bound" required="true" />
		<resources>
			<code path="index.ts" order="5" />
			<css path="css/bootstrap-associated.css" order="1" />
		</resources>
	</control>
</manifest>
```

## overview

This sample provides examples on how to add dependencies for third-party libraries, showcasing how to perform data-binding between PowerApps component framework, component model and third-party inner data model in bi-direction.

The flip component sample consists of a label and a button. When you click on the button, the text on the label toggles.

- When the component is loaded, the label shows the text based on the bind attribute value. The `context.parameters.[property_name].attributes` contains the associated metadata.
- For TwoOptions fields, `context.parameters.[property_name].Options` will include both true and false value option. 
- Clicking on the Flip button, the label will update value using **notifyOutputEvents** method, [getOutputs](../reference/control/getoutputs.md) method will be called asynchronously and will flow to PowerApps component framework. 
- ClientAPI updates the bind attribute value, and the updated value flows to the component label. You can also use `ClientAPI` to update an attribute value to trigger control’s [updateView](../reference/control/updateview.md) method. The component then updates the third-party model and the label gets updated.


## Code

```TypeScript

import { IInputs, IOutputs } from "./generated/ManifestTypes";
import * as angular from "angular";
export class JSAngularJSFlipControl
  implements ComponentFramework.StandardControl<IInputs, IOutputs> {
  // Element id of the ng-app div. Type: string
  private _appDivId: string;
  // ng-app app id. Type: string
  private _appId: string;
  // ng-controller. Type: string
  private _controllerId: string;
  // PCF framework delegate which will be assigned to this object which would be called whenever an update happens. Type: function
  private _notifyOutputChanged: () => void;
  // Model of the bind field. Type: Boolean
  private _currentValue: boolean;
  // Option Label Text when Option is True. The Text is from attribute customization. Type: string
  private _optionTrueLabel: string;
  // Option Label Text when Option is False. The Text is from attribute customization. Type: string
  private _optionFalseLabel: string;
  /**
   * Empty constructor.
   */
  constructor() {}
  /**
   * Used to initialize the control instance. Controls can kick off remote server calls and other initialization actions here.
   * Data-set values are not initialized here, use updateView.
   * @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to property names defined in the manifest, as well as utility functions.
   * @param notifyOutputChanged A callback method to alert the framework that the control has new outputs ready to be retrieved asynchronously.
   * @param state A piece of data that persists in one session for a single user. Can be set at any point in a controls life cycle by calling 'setControlState' in the Mode interface.
   * @param container If control is marked control-type='standard', it receives an empty div element within which it can render its content.
   */
  public init(
    context: ComponentFramework.Context<IInputs>,
    notifyOutputChanged: () => void,
    state: ComponentFramework.Dictionary,
    container: HTMLDivElement
  ) {
    // We need a random integer from 1-100, so that for a form of multiple fields bind to same attribute, we could differentiate
    let randomInt: number = Math.floor(Math.floor(100) * Math.random());
    let _this = this;
    this._appDivId = this.createUniqueId(
      context,
      "angularflip_controlid",
      randomInt
    );
    this._appId = this.createUniqueId(
      context,
      "JSAngularJSFlipControl",
      randomInt
    );
    this._controllerId = this.createUniqueId(
      context,
      "powerApps.angularui.demo",
      randomInt
    );
    this._notifyOutputChanged = notifyOutputChanged;
    // Assign Model the value of the bind attribute
    this._currentValue = context.parameters.flipModel.raw;
    // Initialize the True/False Label texts from the attribute metadata
    this.initializeOptionsLabel(context);
    // Create HTML structure for the control
    let appDiv: HTMLDivElement = document.createElement("div");
    appDiv.setAttribute("id", this._appDivId);
    appDiv.setAttribute("ng-controller", this._appId);
    appDiv.setAttribute("ng-app", this._controllerId);
    // Below sample html are from Angular-UI single toggle sample code
    // https://angular-ui.github.io/bootstrap/
    appDiv.innerHTML =
      "<pre>{{labelModel}}</pre><button type='button' class='btn btn-primary' ng-model='flipButtonModel' uib-btn-checkbox btn-checkbox-true='1' btn-checkbox-false='0'>Flip</button>";
    // Container appends the HTML structure
    container.appendChild(appDiv);
    // Angular code. Angular module/controller initialization.
    angular.module(this._controllerId, [
      "ngAnimate",
      "ngSanitize",
      "ui.bootstrap"
    ]);
    angular.module(this._controllerId).controller(this._appId, $scope => {
      // Intialize 'labelModel'. Assign initial option text to the Angular $scope labelModel. It will be revealed in '<pre>{{labelModel}}</pre>'
      $scope.labelModel = _this._currentValue
        ? _this._optionTrueLabel
        : _this._optionFalseLabel;
      // Intialize 'flipButtonModel'. Assign bind attribute value to Angular $scope flipButtonModel. The Flip button also bind to this 'flipButtonModel', so when we click, it will flip
      $scope.flipButtonModel = _this._currentValue ? 1 : 0;
      // Watch the click of the flip button
      $scope.$watchCollection("flipButtonModel", () => {
        // Update the label text when Flip Button clicks
        if ($scope.flipButtonModel) {
          $scope.labelModel = _this._optionTrueLabel;
        } else {
          $scope.labelModel = _this._optionFalseLabel;
        }
        // Call updateOutputIfNeeded and inform PCF framework that bind attribute value need update
        _this.updateOutputIfNeeded($scope.flipButtonModel);
      });
    });
    // Angular code. Create an App based on the new appDivId
    angular.element(document).ready(() => {
      angular.bootstrap(document.getElementById(_this._appDivId)!, [
        _this._controllerId
      ]);
    });
  }
  /**
   * Get UniqueId so as to avoid id conflict between multiple fields bind to same attribute
   * @param context The "Input Properties" containing the parameters, control metadata and interface functions.
   * @param passInString input string as suffix
   * @param randomInt random integer
   * @returns a string of uniqueId includes attribute logicalname + passIn specialized string + random Integer
   */
  private createUniqueId(
    context: ComponentFramework.Context<IInputs>,
    passInString: string,
    randomInt: number
  ): string {
    return (
      context.parameters!.flipModel.attributes!.LogicalName +
      "-" +
      passInString +
      randomInt
    );
  }
  /**
   * Initialize Options Label to use the attribute label from Metadata
   * @param context The "Input Properties" containing the parameters, control metadata and interface functions.
   */
  private initializeOptionsLabel(
    context: ComponentFramework.Context<IInputs>
  ): void {
    var _this = this;
    // Get option label texts from metadata
    var optionsMetadata = context.parameters.flipModel.attributes!.Options;
    optionsMetadata.forEach((option: any) => {
      if (option.Value) {
        _this._optionTrueLabel = option.Label;
      } else {
        _this._optionFalseLabel = option.Label;
      }
    });
  }
  /**
   * Update Angular 'flipButtonModel' if needed
   * @param newValue new value
   */
  private updateFlipButtonModelIfNeeded(newValue: boolean): void {
    if (
      (newValue && !this._currentValue) ||
      (!newValue && this._currentValue)
    ) {
      this._currentValue = newValue;
      // Angular Code. Update the 'flipButtonModel' value
      var $scope = angular
        .element(document.getElementById(this._appDivId)!)
        .scope();
      $scope.$apply(($scope: any) => {
        // 'flipButtonModel' value is either 1 or 0
        $scope.flipButtonModel = newValue ? 1 : 0;
      });
    }
  }
  /**
   * Update value in PowerApps component framework
   * @param newValue new value
   */
  private updateOutputIfNeeded(newValue: boolean): void {
    if (
      (newValue && !this._currentValue) ||
      (!newValue && this._currentValue)
    ) {
      this._currentValue = newValue ? true : false;
      this._notifyOutputChanged();
    }
  }
  /**
   * Called when any value in the property bag has changed. This includes field values, data-sets, global values such as container height and width, offline status, control metadata values such as label, visible, etc.
   * @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to names defined in the manifest, as well as utility functions
   */
  public updateView(context: ComponentFramework.Context<IInputs>): void {
    // An attribute value from Control Framework could be updated even after init cycle, clientAPI, post Save response can update the attribute value and the Flip control should reveal the new value.
    this.updateFlipButtonModelIfNeeded(context.parameters.flipModel.raw);
  }
  /**
   * It is called by the framework prior to a control receiving new data.
   * @returns an object based on nomenclature defined in manifest, expecting object[s] for property marked as “bound” or “output”
   */
  public getOutputs(): IOutputs {
    var returnValue = this._currentValue;
    return { flipModel: returnValue };
  }
  /**
   * Called when the control is to be removed from the DOM tree. Controls should use this call for cleanup.
   * i.e. canceling any pending remote calls, removing listeners, etc.
   */
  public destroy(): void {
    // Add code to cleanup control if necessary
  }
}
```

### Resources

```css
.SampleNamespace\.JSAngularJSFlipControl pre {
  display: block;
  padding: 9.5px;
  margin: 0 0 10px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #333;
  word-break: break-all;
  word-wrap: break-word;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.SampleNamespace\.JSAngularJSFlipControl pre {
  font-family: Menlo, Monaco, Consolas, "Courier New", monospace;
}
.SampleNamespace\.JSAngularJSFlipControl pre {
  overflow: auto;
}
.SampleNamespace\.JSAngularJSFlipControl .btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.SampleNamespace\.JSAngularJSFlipControl .btn-primary.focus,
.SampleNamespace\.JSAngularJSFlipControl .btn-primary:focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.SampleNamespace\.JSAngularJSFlipControl .btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.SampleNamespace\.JSAngularJSFlipControl .btn-primary.active,
.SampleNamespace\.JSAngularJSFlipControl .btn-primary:active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.SampleNamespace\.JSAngularJSFlipControl .btn-primary.active.focus,
.SampleNamespace\.JSAngularJSFlipControl .btn-primary.active:focus,
.SampleNamespace\.JSAngularJSFlipControl .btn-primary.active:hover,
.SampleNamespace\.JSAngularJSFlipControl .btn-primary:active.focus,
.SampleNamespace\.JSAngularJSFlipControl .btn-primary:active:focus,
.SampleNamespace\.JSAngularJSFlipControl .btn-primary:active:hover,
.open > .dropdown-toggle.btn-primary.focus,
.open > .dropdown-toggle.btn-primary:focus,
.open > .dropdown-toggle.btn-primary:hover {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.SampleNamespace\.JSAngularJSFlipControl .btn-primary.active,
.SampleNamespace\.JSAngularJSFlipControl .btn-primary:active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.SampleNamespace\.JSAngularJSFlipControl .btn-primary.disabled.focus,
.SampleNamespace\.JSAngularJSFlipControl .btn-primary.disabled:focus,
.SampleNamespace\.JSAngularJSFlipControl .btn-primary.disabled:hover,
.SampleNamespace\.JSAngularJSFlipControl .btn-primary[disabled].focus,
.SampleNamespace\.JSAngularJSFlipControl .btn-primary[disabled]:focus,
.SampleNamespace\.JSAngularJSFlipControl .btn-primary[disabled]:hover,
fieldset[disabled].btn-primary.focus,
fieldset[disabled].btn-primary:focus,
fieldset[disabled].btn-primary:hover {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.SampleNamespace\.JSAngularJSFlipControl .btn-primary.badge {
  color: #337ab7;
  background-color: #fff;
}
.SampleNamespace\.JSAngularJSFlipControl .btn {
  display: inline-block;
  padding: 6px 12px;
  margin-bottom: 0;
  font-size: 14px;
  font-weight: 400;
  line-height: 1.42857143;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  -ms-touch-action: manipulation;
  touch-action: manipulation;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 4px;
}

```

### Related topics

[PowerApps component framework manifest schema reference](../manifest-schema-reference/index.md)<br />
[PowerApps component framework API reference](../reference/index.md)<br />
[PowerApps component framework overview](../overview.md)
