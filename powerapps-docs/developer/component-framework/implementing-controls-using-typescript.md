---
title: "Implementing code components using TypeScript | MicrosoftDocs"
description: "How to implement a code components using TypeScript"
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.topic: "index-page"
ms.assetid: 18e88d702-3349-4022-a7d8-a9adf52cd34f
ms.author: "nabuthuk"
author: Nkrb
---

# Implement components using TypeScript

[!INCLUDE[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This tutorial walks you through the process of creating a new code component in Typescript. The sample component is a linear input component which enables users to enter numeric values using a visual slider instead of directly typing the values in the field. 

## Creating a new component project

To create a new project:

1. Open a Developer Command Prompt for VS 2017 window.
1. Create a new folder for the project using the command 
    ```CLI
    mkdir LinearComponent
    ```

1. `cd` into the new directory and run the command `cd LinearComponent` 
1. Create the component project using the command 
    ```CLI
    pac pcf init --namespace SampleNamespace --name TSLinearInputControl --template field
    ``` 

1. Install the project build tools using the command `npm install` 
2. Open the project in any developer environment of your choice and start implementing your code component.

## Implementing Manifest

A code component is defined by the information in the `ControlManifest.Input.xml` manifest file. In this walkthrough, this file is created under the `<Your component Name>` sub folder. For the linear input component, a property will be defined to store the numeric value of the slider input.

1. Open the `ControlManifest.Input.xml` file in the code editor (Visual Studio Code). The `ControlManifest.Input.xml` file defines an initial component property called `sampleProperty`.

    ```XML
    <property name="sampleProperty" display-name-key="Property_Display_Key" description-key="Property_Desc_Key" of-type="SingleLine.Text" usage="bound" required="true" /> 
    ```

2. Rename the `sampleProperty` and change the property type

    ```XML
    <property name="sliderValue" display-name-key="sliderValue_Display_Key" description-key="sliderValue_Desc_Key" of-type-group="numbers" usage="bound" required="true" /> 
    ```

3. The of-type-group attribute references a group of allowable numbers. Add the following type-group element as a sibling to the property element in the manifest. The type-group specifies the component value and can contain whole, currency, floating point, or decimal values.

    ```XML
    <type-group name="numbers"> 
      <type>Whole.None</type> 
      <type>Currency</type> 
      <type>FP</type> 
      <type>Decimal</type> 
     </type-group> 
    ```

4. Save the changes to the `ControlManifest.Input.xml` file.
5. Now, create a new folder inside the `TSLinearInputControl` folder and name it as **css**.
6. Create a CSS file to [add styling to the code component](#adding-style-to-the-code-component)
7. Build the component project using the command `npm run build`.
8. The build generates an updated Typescript type declaration file under `TSLinearInputControl/generated folder`.

## Implementing component logic

Source for the code component is implemented in the `index.ts` file. The `index.ts` file includes scaffolding for interface methods that are required by the PowerApps component framework. 

1. Open the `index.ts` file in the code editor of your choice.
2. Update the `TSLinearInputControl` class with the following

```TypeScript
import { IInputs, IOutputs } from "./generated/ManifestTypes";
export class TSLinearInputControl implements ComponentFramework.StandardControl<IInputs, IOutputs> {
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
  // Reference to ComponentFramework Context object
  private _context: ComponentFramework.Context<IInputs>;
  // Event Handler 'refreshData' reference
  private _refreshData: EventListenerOrEventListenerObject;

  constructor() {
  }

  public init(context: ComponentFramework.Context<IInputs>, notifyOutputChanged: () => void, state: ComponentFramework.Dictionary, container: HTMLDivElement) {
    this._context = context;
    this._container = document.createElement("div");
    this._notifyOutputChanged = notifyOutputChanged;
    this._refreshData = this.refreshData.bind(this);
    // creating HTML elements for the input type range and binding it to the function which refreshes the control data
    this.inputElement = document.createElement("input");
    this.inputElement.setAttribute("type", "range");
    this.inputElement.addEventListener("input", this._refreshData);
    //setting the max and min values for the control.
    this.inputElement.setAttribute("min", "1");
    this.inputElement.setAttribute("max", "1000");
    this.inputElement.setAttribute("class", "linearslider");
    this.inputElement.setAttribute("id", "linearrangeinput");
    // creating a HTML label element that shows the value that is set on the linear range control
    this.labelElement = document.createElement("label");
    this.labelElement.setAttribute("class", "TS_LinearRangeLabel");
    this.labelElement.setAttribute("id", "lrclabel");
    // retrieving the latest value from the control and setting it to the HTMl elements.
    this._value = context.parameters.sliderValue.raw ? context.parameters.sliderValue.raw : 0;
    this.inputElement.setAttribute("value", context.parameters.sliderValue.formatted ? context.parameters.sliderValue.formatted : "0");
    this.labelElement.innerHTML = context.parameters.sliderValue.formatted ? context.parameters.sliderValue.formatted : "0";
    // appending the HTML elements to the control's HTML container element.
    this._container.appendChild(this.inputElement);
    this._container.appendChild(this.labelElement);
    container.appendChild(this._container);
  }

  /**
  * Updates the values to the internal value variable we are storing and also updates the html label that displays the value
  * @param context : The "Input Properties" containing the parameters, control metadata and interface functions
  */

  public refreshData(evt: Event): void {
    this._value = (this.inputElement.value as any) as number;
    this.labelElement.innerHTML = this.inputElement.value;
    this._notifyOutputChanged();
  }

  public updateView(context: ComponentFramework.Context<IInputs>): void {
    // storing the latest context from the control.
    this._value = context.parameters.sliderValue.raw ? context.parameters.sliderValue.raw : 0;
    this._context = context;
    this.inputElement.setAttribute("value",context.parameters.sliderValue.formatted ? context.parameters.sliderValue.formatted : "");
    this.labelElement.innerHTML = context.parameters.sliderValue.formatted ? context.parameters.sliderValue.formatted : "";
  }

  public getOutputs(): IOutputs {
    return {
      sliderValue: this._value
    };
  }

  public destroy() {
    this.inputElement.removeEventListener("input", this._refreshData);
  }
}
```

3. Rebuild the project using the command `npm run build` 
 
4. The component is compiled into the `out/controls/TSLinearInputControl` folder. The build artifacts include:

   - bundle.js – Bundled component source code 
   - ControlManifest.xml – Actual component manifest file that is uploaded to the Common Data Service organization.

## Adding style to the code component

The linear input component’s `init` method creates an input element and sets the class attribute to `linearslider`. The style for the `linearslider` class is defined in a separate `CSS` file. Additional component resources like `CSS` files can be included with the code component to support further customizations.

1. Create a new `css` subfolder under the `TSLinearInputControl` folder. 
2. Create a new `TS_LinearInputControl.css` file inside the `css` subfolder. 
3. Add the following style content to `TS_LinearInputControl.css` file

    ```CSS
    .SampleNamespace\.TSLinearInputControl input[type=range].linearslider {
      margin: 1px 0;
      background: transparent;
      -webkit-appearance: none;
      width: 100%;
      padding: 0;
      height: 24px;
      -webkit-tap-highlight-color: transparent
    }

    .SampleNamespace\.TSLinearInputControl input[type=range].linearslider:focus {
      outline: none;
    }

    .SampleNamespace\.TSLinearInputControl input[type=range].linearslider::-webkit-slider-runnable-track {
      background: #666;
      height: 2px;
      cursor: pointer
    }

    .SampleNamespace\.TSLinearInputControl input[type=range].linearslider::-webkit-slider-thumb {
      background: #666;
      border: 0 solid #f00;
      height: 24px;
      width: 10px;
      border-radius: 48px;
      cursor: pointer;
      opacity: 1;
      -webkit-appearance: none;
      margin-top: -12px
    }

    .SampleNamespace\.TSLinearInputControl input[type=range].linearslider::-moz-range-track {
      background: #666;
      height: 2px;
      cursor: pointer
    }

    .SampleNamespace\.TSLinearInputControl input[type=range].linearslider::-moz-range-thumb {
      background: #666;
      border: 0 solid #f00;
      height: 24px;
      width: 10px;
      border-radius: 48px;
      cursor: pointer;
      opacity: 1;
      -webkit-appearance: none;
      margin-top: -12px
    }

    .SampleNamespace\.TSLinearInputControl input[type=range].linearslider::-ms-track {
      background: #666;
      height: 2px;
      cursor: pointer
    }

    .SampleNamespace\.TSLinearInputControl input[type=range].linearslider::-ms-thumb {
      background: #666;
      border: 0 solid #f00;
      height: 24px;
      width: 10px;
      border-radius: 48px;
      cursor: pointer;
      opacity: 1;
      -webkit-appearance: none;
    }
    ```

5. Save the `TS_LinearInputControl.css` file.
6. Edit the `ControlManifest.Input.xml` file to include the `CSS` resource file inside the resources element
 
    ```XML
    <resources> 
      <code path="index.ts" order="1"/> 
      <css path="css/TS_LinearInputControl.css" order="1"/> 
    </resources> 
     ```
7. Rebuild the project using the command 
   ```CLI
   npm run build
   ```
8. Inspect the build output under the **./out/controls/TSLinearInputControl** and observe that the **TS_LinearInputControl.css** file is now included with the compiled build artifacts. 

## Debugging your code component

Once you are done implementing your code component logic, run the following command to start the debugging process. More information: [Debugging code components](debugging-custom-controls.md)

```CLI
npm start
```

## Packaging your code components

Follow the steps below to create and import a [solution](https://docs.microsoft.com/dynamics365/customer-engagement/customize/solutions-overview) file:

1. Create a new folder **Solutions** inside the **LinearComponent** folder and navigate into the folder. 
2. Create a new solution project in the **LinearComponent** folder using the command 
 
    ```CLI
     pac solution init --publisher-name developer --publisher-prefix dev 
    ```

   > [!NOTE]
   > The [publisher-name](https://docs.microsoft.com/powerapps/developer/common-data-service/reference/entities/publisher) and [publisher-prefix](https://docs.microsoft.com/powerapps/maker/common-data-service/change-solution-publisher-prefix) values must be unique to your environment.
 
3. Once the new solution project is created, you need to refer to the location where the created component is located. You can add the reference by using the command

    ```CLI
     pac solution add-reference --path c:\users\LinearComponent
    ```

4. To generate a zip file from your solution project, you need to `cd` into your solution project directory and build the project using the command 

    ```CLI
     msbuild /t:restore
    ```

5. Again run the following command msbuild
    ```CLI
     msbuild
    ```

    > [!NOTE]
    > Make sure that the **NuGet targets & Build Tasks** is checked. To enable it
    > - Open **Visual Studio Installer**
    > - For VS 2017, click on **Modify**
    > - Click on **Individual Components**
    > - Under **Code Tools**, check **NuGet targets & Build Tasks**

6. The generated solution zip file is located in `Solution\\bin\debug\`.
7. You should manually [import the solution into Common Data Service](https://docs.microsoft.com/dynamics365/customer-engagement/customize/import-update-export-solutions) using the web portal once the zip file is ready or see [Authenticating to your organization](import-custom-controls.md#authenticating-to-your-organization) and [Deployment](import-custom-controls.md#deploying-code-components) sections to import using PowerApps CLI commands.

## Adding code components in model-driven apps

To add a code component like a linear input component, follow the steps mentioned in the topic [Add components to fields and entities](add-custom-controls-to-a-field-or-entity.md).

## Adding code components to a canvas app

To add the code components to a canvas app, follow the steps mentioned in this topic [Add code components to a canvas app](component-framework-for-canvas-apps.md#add-components-to-a-canvas-app)

### See also

[Download sample components](https://go.microsoft.com/fwlink/?linkid=2088525)<br/>
[Update existing PowerApps component framework controls](updating-existing-controls.md)<br/>
[PowerApps component framework API Reference](reference/index.md)<br/>
[PowerApps component framework Overview](overview.md)
