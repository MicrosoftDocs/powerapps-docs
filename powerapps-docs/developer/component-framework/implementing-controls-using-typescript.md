---
title: "Implementing code components using TypeScript | MicrosoftDocs"
description: "How to implement code components using TypeScript"
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.topic: "index-page"
ms.assetid: 18e88d702-3349-4022-a7d8-a9adf52cd34f
ms.author: "nabuthuk"
author: Nkrb
---

# Implement components using TypeScript

This tutorial walks you through the process of creating a new code component in TypeScript. The sample component is a linear input component that enables users to enter numeric values using a visual slider instead of typing the values in the field. 

## Creating a new component project

To create a new project:

1. Open a **Developer Command Prompt for VS 2017** window.
1. Create a new folder for the project using the following command: 
    ```CLI
    mkdir LinearComponent
    ```

1. Go into the new directory using the command `cd LinearComponent`. 
   
1. Run the following command to create a new component project passing basic parameters.

   ```CLI
    pac pcf init --namespace SampleNamespace --name TSLinearInputComponent --template field
    ``` 

1. Install the project build tools using the command `npm install`. 
2. Open your project folder `C:\Users\<your name>\Documents\<My_PCF_Component>` in a developer environment of your choice and get started with your code component development. The quickest way to start is by running `code .` from the command prompt once you are in the `C:\Users\<your name>\Documents\<My_PCF_Component>` directory. This command opens your component project in Visual Studio Code.

## Implementing manifest

Manifest is an XML file that contains the metadata of the code component. It also defines the behavior of the code component. In this tutorial, this manifest file is created under the `<Your component Name>` subfolder. When you open the `ControlManifest.Input.xml` file in Visual Studio Code, you'll notice that the manifest file is predefined with some properties. Make changes to the predefined manifest file, as shown here:

1. The [control](manifest-schema-reference/control.md) node defines the namespace, version, and display name of the code component. Now, define each property of the [control](manifest-schema-reference/control.md) node as shown here:

   - **namespace**: Namespace of the code component. 
   - **Constructor**: Constructor of the code component.
   - **Version**: Version of the component. Whenever you update the component, you need to update the version to see the changes in the runtime.
   - **display-name-key**: Name of the code component that is displayed on the UI.
   - **description-name-key**: Description of the code component that is displayed on the UI.
   - **control-type**: The code component type. Only *standard* type of code components are supported.

     ```XML
      <?xml version="1.0" encoding="utf-8" ?>
      <manifest>
      <control namespace="SampleNameSpace" constructor="TSLinearInputComponent" version="1.0.0" display-name-key="Linear Input Component" description-key="Allows you to enter the numeric values using the visual slider." control-type="standard">
     ```

2. The [property](manifest-schema-reference/property.md) node defines the properties of the code component like defining the data type of field. The property node is specified as the child element under the control element. Define the [property](manifest-schema-reference/property.md) node as shown here:

   - **name**: Name of the property.
   - **display-name-key**: Display name of the property that is displayed on the UI.
   - **description-name-key**: Description of the property that is displayed on the UI. 
   - **of-type-group**: The [of-type-group](manifest-schema-reference/type-group.md) is used when you want to have more than two data type fields. Add the [of-type-group](manifest-schema-reference/type-group.md) element as a sibling to the `property` element in the manifest. The `of-type-group` specifies the component value and can contain whole, currency, floating point, or decimal values.
   - **usage**: Has two properties, *bound* and *input*. Bound properties are bound only to the value of the field. Input properties are either bound to a field or allow a static value.
   - **required**: Defines whether the property is required.

     ```XML
      <property name="sliderValue" display-name-key="sliderValue_Display_Key" description-key="sliderValue_Desc_Key" of-type-group="numbers" usage="bound" required="true" />
      ```
3. The [resources](manifest-schema-reference/resources.md) node defines the visualization of the code component. It contains all the resources that make up the code component. The [code](manifest-schema-reference/code.md) is specified as a child element under the resources element. Define the [resources](manifest-schema-reference/resources.md) as shown here:

   - **code**: Refers to the path where all the resource files are located.
 
      ```XML
      <resources>
	    <code path="index.ts" order="1" />
	    <css path="css/TS_LinearInputComponent.css" order="1" />
	    </resources>
        ```
      The overall manifest file should look something like this: 

     ```XML
      <?xml version="1.0" encoding="utf-8" ?>
      <manifest>
      <control namespace="SampleNamespace" constructor="TSLinearInputComponent" version="1.0.0" display-name-key="Linear Input Component" description-key="Allows you to enter the numeric values using the visual slider." control-type="standard">
	    <type-group name="numbers">
		  <type>Whole.None</type>
		  <type>Currency</type>
		  <type>FP</type>
		  <type>Decimal</type>
	     </type-group>
	    <property name="sliderValue" display-name-key="sliderValue_Display_Key" description-key="sliderValue_Desc_Key" of-type-group="numbers" usage="bound" required="true" />
	   <resources>
		 <code path="index.ts" order="1" />
		 <css path="css/TS_LinearInputComponent.css" order="1" />
	   </resources>
      </control>
     </manifest>
     ```

4. Save the changes to the `ControlManifest.Input.xml` file.
5. Now, create a new folder inside the `TSLinearInputComponent` folder and name it as **css**.
6. Create a CSS file to [add styling to the code component](#adding-style-to-the-code-component).
7. Build the component project using the command `npm run build`.
8. The build generates an updated TypeScript type declaration file under the `TSLinearInputComponent/generated` folder.

## Implementing component logic

The next step after implementing the manifest file is to implement the component logic using TypeScript. The component logic should be implemented inside the `index.ts` file. When you open the `index.ts` file in the Visual Studio Code, you notice that the four essential classes are predefined. Now, let's implement the logic for the code component. 

1. Open the `index.ts` file in the code editor of your choice.
2. Update the `TSLinearInputComponent` class with the following code:

```TypeScript
import { IInputs, IOutputs } from "./generated/ManifestTypes";
export class TSLinearInputComponent
  implements ComponentFramework.StandardControl<IInputs, IOutputs> {
  // Value of the field is stored and used inside the component
  private _value: number;
  // PowerApps component framework delegate which will be assigned to this object which would be called whenever any update happens.
  private _notifyOutputChanged: () => void;
  // label element created as part of this component
  private labelElement: HTMLLabelElement;
  // input element that is used to create the range slider
  private inputElement: HTMLInputElement;
  // reference to the component container HTMLDivElement
  // This element contains all elements of our code component example
  private _container: HTMLDivElement;
  // reference to PowerApps component framework Context object
  private _context: ComponentFramework.Context<IInputs>;
  // Event Handler 'refreshData' reference
  private _refreshData: EventListenerOrEventListenerObject;

  constructor() {}

  public init(
    context: ComponentFramework.Context<IInputs>,
    notifyOutputChanged: () => void,
    state: ComponentFramework.Dictionary,
    container: HTMLDivElement
  ) {
    this._context = context;
    this._container = document.createElement("div");
    this._notifyOutputChanged = notifyOutputChanged;
    this._refreshData = this.refreshData.bind(this);
    // creating HTML elements for the input type range and binding it to the function which refreshes the component data
    this.inputElement = document.createElement("input");
    this.inputElement.setAttribute("type", "range");
    this.inputElement.addEventListener("input", this._refreshData);
    //setting the max and min values for the component.
    this.inputElement.setAttribute("min", "1");
    this.inputElement.setAttribute("max", "1000");
    this.inputElement.setAttribute("class", "linearslider");
    this.inputElement.setAttribute("id", "linearrangeinput");
    // creating a HTML label element that shows the value that is set on the linear range component
    this.labelElement = document.createElement("label");
    this.labelElement.setAttribute("class", "TS_LinearRangeLabel");
    this.labelElement.setAttribute("id", "lrclabel");
    // retrieving the latest value from the component and setting it to the HTML elements.
    this._value = context.parameters.sliderValue.raw
      ? context.parameters.sliderValue.raw
      : 0;
    this.inputElement.setAttribute(
      "value",
      context.parameters.sliderValue.formatted
        ? context.parameters.sliderValue.formatted
        : "0"
    );
    this.labelElement.innerHTML = context.parameters.sliderValue.formatted
      ? context.parameters.sliderValue.formatted
      : "0";
    // appending the HTML elements to the component's HTML container element.
    this._container.appendChild(this.inputElement);
    this._container.appendChild(this.labelElement);
    container.appendChild(this._container);
  }

  /**
   * Updates the values to the internal value variable we are storing and also updates the html label that displays the value
   * @param context : The "Input Properties" containing the parameters, component metadata and interface functions
   */

  public refreshData(evt: Event): void {
    this._value = (this.inputElement.value as any) as number;
    this.labelElement.innerHTML = this.inputElement.value;
    this._notifyOutputChanged();
  }

  public updateView(context: ComponentFramework.Context<IInputs>): void {
    // storing the latest context from the control.
    this._value = context.parameters.sliderValue.raw
      ? context.parameters.sliderValue.raw
      : 0;
    this._context = context;
    this.inputElement.setAttribute(
      "value",
      context.parameters.sliderValue.formatted
        ? context.parameters.sliderValue.formatted
        : ""
    );
    this.labelElement.innerHTML = context.parameters.sliderValue.formatted
      ? context.parameters.sliderValue.formatted
      : "";
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

3. Rebuild the project using the command `npm run build`. 
 
4. The component is compiled into the `out/controls/TSLinearInputComponent` folder. The build artifacts include:

   - bundle.js – Bundled component source code. 
   - ControlManifest.xml – Actual component manifest file that is uploaded to the Common Data Service organization.

## Adding style to the code component

Developers and app makers can define their styling to represent their code components visually using CSS. CSS allows the developers to describe the presentation of code components, including style, colors, layouts, and fonts. The linear input component’s [init](reference/control/init.md) method creates an input element and sets the class attribute to `linearslider`. The style for the `linearslider` class is defined in a separate `CSS` file. Additional component resources like `CSS` files can be included with the code component to support further customizations.

1. Create a new `css` subfolder under the `TSLinearInputComponent` folder. 
2. Create a new `TS_LinearInputComponent.css` file inside the `css` subfolder. 
3. Add the following style content to the `TS_LinearInputComponent.css` file:

    ```CSS
    .SampleNamespace\.TSLinearInputComponent input[type=range].linearslider {
      margin: 1px 0;
      background: transparent;
      -webkit-appearance: none;
      width: 100%;
      padding: 0;
      height: 24px;
      -webkit-tap-highlight-color: transparent
    }

    .SampleNamespace\.TSLinearInputComponent input[type=range].linearslider:focus {
      outline: none;
    }

    .SampleNamespace\.TSLinearInputComponent input[type=range].linearslider::-webkit-slider-runnable-track {
      background: #666;
      height: 2px;
      cursor: pointer
    }

    .SampleNamespace\.TSLinearInputComponent input[type=range].linearslider::-webkit-slider-thumb {
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

    .SampleNamespace\.TSLinearInputComponent input[type=range].linearslider::-moz-range-track {
      background: #666;
      height: 2px;
      cursor: pointer
    }

    .SampleNamespace\.TSLinearInputComponent input[type=range].linearslider::-moz-range-thumb {
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

    .SampleNamespace\.TSLinearInputComponent input[type=range].linearslider::-ms-track {
      background: #666;
      height: 2px;
      cursor: pointer
    }

    .SampleNamespace\.TSLinearInputComponent input[type=range].linearslider::-ms-thumb {
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

5. Save the `TS_LinearInputComponent.css` file.
6. Edit the `ControlManifest.Input.xml` file to include the `CSS` resource file inside the resources element.
 
    ```XML
    <resources> 
      <code path="index.ts" order="1"/> 
      <css path="css/TS_LinearInputComponent.css" order="1"/> 
    </resources> 
     ```
7. Rebuild the project using the following command: 
   ```CLI
   npm run build
   ```
8. Inspect the build output under the **./out/controls/TSLinearInputComponent** and observe that the **TS_LinearInputComponent.css** file is now included with the compiled build artifacts. 

## Debugging your code component

Once you are done implementing your code component logic, run the following command to start the debugging process. More information: [Debug code components](debugging-custom-controls.md)

```CLI
npm start
```

## Packaging your code components

Follow these steps to create and import a [solution](https://docs.microsoft.com/dynamics365/customer-engagement/customize/solutions-overview) file:

1. Create a new folder **Solutions** inside the **LinearComponent** folder and navigate into the folder. 
2. Create a new solution project in the **LinearComponent** folder using the following command:
 
    ```CLI
     pac solution init --publisher-name developer --publisher-prefix dev 
    ```

   > [!NOTE]
   > The [publisher-name](https://docs.microsoft.com/powerapps/developer/common-data-service/reference/entities/publisher) and [publisher-prefix](https://docs.microsoft.com/powerapps/maker/common-data-service/change-solution-publisher-prefix) values must be unique to your environment.
 
3. Once the new solution project is created, you need to refer to the location where the created component is located. You can add the reference by using the following command:

    ```CLI
     pac solution add-reference --path c:\users\LinearComponent
    ```

4. To generate a zip file from your solution project, you need to `cd` into your solution project directory and build the project using the following command: 

    ```CLI
     msbuild /t:restore
    ```

5. Again, run the following command msbuild:
    ```CLI
     msbuild
    ```

    > [!NOTE]
    > Make sure that **NuGet targets & Build Tasks** is checked. To enable it:
    > - Open **Visual Studio Installer**.
    > - For Visual Studio 2017, select **Modify**.
    > - Select **Individual Components**.
    > - Under **Code Tools**, check **NuGet targets & Build Tasks**.

6. The generated solution zip file is located in the `Solution\bin\debug` folder.
7. Manually [import the solution into Common Data Service](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/customize/import-update-upgrade-solution) using the web portal once the zip file is ready or see the [Authenticating to your organization](import-custom-controls.md#authenticating-to-your-organization) and [Deployment](import-custom-controls.md#deploying-code-components) sections to import using PowerApps CLI commands.

## Adding code components in model-driven apps

To add a code component like a linear input component, follow the steps mentioned in the topic [Add components to fields and entities](add-custom-controls-to-a-field-or-entity.md).

## Adding code components to a canvas app

To add the code components to a canvas app, follow the steps in the topic [Add code components to a canvas app](component-framework-for-canvas-apps.md#add-components-to-a-canvas-app).

### See also

[Download sample components](https://go.microsoft.com/fwlink/?linkid=2088525)<br/>
[Update existing PowerApps component framework components](updating-existing-controls.md)<br/>
[PowerApps component framework API reference](reference/index.md)<br/>
[PowerApps component framework overview](overview.md)
