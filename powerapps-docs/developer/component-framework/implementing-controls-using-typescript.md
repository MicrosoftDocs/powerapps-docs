---
title: "Create your first component using Power Apps Component Framework in Microsoft Dataverse| MicrosoftDocs"
description: "Learn how to implement code components using Power Apps component framework"
manager: kvivek
ms.date: 04/01/2021
ms.service: "powerapps"
ms.custom: "intro-internal"
ms.topic: "index-page"
ms.assetid: 18e88d702-3349-4022-a7d8-a9adf52cd34f
ms.author: "nabuthuk"
author: Nkrb
---

# Create your first component 

 In this tutorial, we demonstrate how to build a linear slider code component that enables users to change the numeric values using a visual slider instead of typing the values in the column. 

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

The following steps are required to build a linear slider code component:

- [Create a new component project](#creating-a-new-component-project)
- [Implementing manifest](#implementing-manifest)
- [Implement component logic using TypeScript](#implementing-component-logic)
- [Add style to the code components](#adding-style-to-the-code-component)
- [Build your code components](#build-your-code-components)
- [Packaging code components](#packaging-your-code-components)
- [Adding component to a model-driven app](#adding-code-components-in-model-driven-apps)
- [Adding component to a canvas app](#adding-code-components-to-a-canvas-app)

## Creating a new component project

To create a new project:

1. Open a **Developer Command Prompt for VS 2017 or higher** window. Create a new folder for the project using the following command: 
    ```CLI
     mkdir LinearComponent
    ```
                     
1. Go into the component folder using the command `cd LinearComponent`. 
         
1. Create a new component project by passing basic parameters using the command.

   ```CLI
    pac pcf init --namespace SampleNamespace --name TSLinearInputComponent --template field
    ``` 

1. Install the project build tools using the command `npm install`. 
1. Open your project folder in a developer environment of your choice and get started with your code component development. The quickest way to start is by running `code .` from the command prompt once you are in the project directory. This command opens your component project in Visual Studio Code.

## Implementing manifest

Manifest is an XML file that contains the metadata of the code component. It also defines the behavior of the code component. In this tutorial, this manifest file is created under the `<Your component Name>` subfolder. When you open the `ControlManifest.Input.xml` file in Visual Studio Code, you'll notice that the manifest file is predefined with some properties. More information: [Manifest](manifest-schema-reference/manifest.md).

Make changes to the predefined manifest file, as shown here:

1. The [control](manifest-schema-reference/control.md) node defines the namespace, version, and display name of the code component. Now, define each property of the [control](manifest-schema-reference/control.md) node as shown here:

   - **namespace**: Namespace of the code component. 
   - **Constructor**: Constructor of the code component.
   - **Version**: Version of the component. Whenever you update the component, you need to update the version to see the latest changes in the runtime.
   - **display-name-key**: Name of the code component that is displayed on the UI.
   - **description-name-key**: Description of the code component that is displayed on the UI.
   - **control-type**: The code component type. Only *standard* types of code components are supported.

     ```XML
      <?xml version="1.0" encoding="utf-8" ?>
      <manifest>
      <control namespace="SampleNameSpace" constructor="TSLinearInputComponent" version="1.0.0" display-name-key="TSLinearInputComponent_Display_Key" description-key="TSLinearInputComponent_Desc_Key" control-type="standard">
     ```

2. The [property](manifest-schema-reference/property.md) node defines the properties of the code component like defining the data type of the column. The property node is specified as the child element under the `control` element. Define the [property](manifest-schema-reference/property.md) node as shown here:

   - **name**: Name of the property.
   - **display-name-key**: Display name of the property that is displayed on the UI.
   - **description-name-key**: Description of the property that is displayed on the UI. 
   - **of-type-group**: The [of-type-group](manifest-schema-reference/type-group.md) is used when you want to have more than two data type columns. Add the [of-type-group](manifest-schema-reference/type-group.md) element as a sibling to the `property` element in the manifest. The `of-type-group` specifies the component value and can contain whole, currency, floating point, or decimal values.
   - **usage**: Has two properties, *bound* and *input*. Bound properties are bound only to the value of the column. Input properties are either bound to a column or allow a static value.
   - **required**: Defines whether the property is required.

     ```XML
      <property name="sliderValue" display-name-key="sliderValue_Display_Key" description-key="sliderValue_Desc_Key" of-type-group="numbers" usage="bound" required="true" />
      ```

3. The [resources](manifest-schema-reference/resources.md) node defines the visualization of the code component. It contains all the resources that build the visualization and styling of the code component. The [code](manifest-schema-reference/code.md) is specified as a child element under the resources element. Define the [resources](manifest-schema-reference/resources.md) as shown here:

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
      <control namespace="SampleNamespace" constructor="TSLinearInputComponent" version="1.0.0" display-name-key="TSLinearInputComponent_Display_Key" description-key="TSLinearInputComponent_Desc_Key" control-type="standard">
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

## Implementing component logic

The next step after implementing the manifest file is to implement the component logic using TypeScript. The component logic should be implemented inside the `index.ts` file. When you open the `index.ts` file in the Visual Studio Code, you'll notice that the four essential functions are predefined. Now, let's implement the logic for the code component. 

1. Open the `index.ts` file in the code editor of your choice.
2. Update the `TSLinearInputComponent` class with the following code:

```TypeScript
import { IInputs, IOutputs } from "./generated/ManifestTypes";
export class TSLinearInputComponent
  implements ComponentFramework.StandardControl<IInputs, IOutputs> {
  // Value of the column is stored and used inside the component
  private _value: number;
  // Power Apps component framework delegate which will be assigned to this object which would be called whenever any update happens.
  private _notifyOutputChanged: () => void;
  // label element created as part of this component
  private labelElement: HTMLLabelElement;
  // input element that is used to create the range slider
  private inputElement: HTMLInputElement;
  // reference to the component container HTMLDivElement
  // This element contains all elements of our code component example
  private _container: HTMLDivElement;
  // reference to Power Apps component framework Context object
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
    this.inputElement.value =
      context.parameters.sliderValue.formatted
        ? context.parameters.sliderValue.formatted
        : "0";
    
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
    this.inputElement.value =
     
      context.parameters.sliderValue.formatted
        ? context.parameters.sliderValue.formatted
        : "";
    
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

3. Save the change to the `index.ts` file.

## Adding style to the code component

Developers and app makers can define their styling to represent their code components visually using CSS. CSS allows the developers to describe the presentation of code components, including style, colors, layouts, and fonts. The linear input component's [init](reference/control/init.md) method creates an input element and sets the class attribute to `linearslider`. The style for the `linearslider` class is defined in a separate `CSS` file. Additional component resources like `CSS` files can be included with the code component to support further customizations.

> [!IMPORTANT]
> When you implement styling to your code components using CSS, ensure that the CSS is scoped to your control using the automatically generated CSS classes applied to the container `DIV` element for your component. If your CSS is scoped globally, it will likely break the existing styling of the form or screen where the code component is rendered. If using a third-party CSS framework, use a version of that framework that is already namespaced or otherwise wrap that framework in a namespace manually either by hand or using a CSS preprocessor.

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

> [!NOTE]
> Power Apps component framework uses the concept of implementing String(resx) web resources that is used to manage the localized strings shown on any user interface. More information: [String(Resx) web resources](/dynamics365/customerengagement/on-premises/developer/resx-web-resources).
> See [Localization API](sample-controls/localization-api-control.md) sample, to learn how to localize  code components using `resx` web resources. 


## Build your code components

After you finish adding manifest, component logic, and styling, build the code components using the command:
```
npm run build
```

Alternatively, to build the component project, open the project folder that contains `package.json` in Visual Studio Code and use the (Ctrl-Shift-B) command, then select the build options. 
The build generates an updated TypeScript type declaration file under the `TSLinearInputComponent/generated` folder.
The component is compiled into the `out/controls/TSLinearInputComponent` folder. The build artifacts include:

   - bundle.js – Bundled component source code. 
   - ControlManifest.xml – Actual component manifest file that is uploaded to the Microsoft Dataverse organization.

## Debugging your code component

Once you're done implementing the code component logic, run the following command to start the debugging process. More information: [Debug code components](debugging-custom-controls.md)

```CLI
npm start
```

## Packaging your code components

Follow these steps to create and import a [solution](../../maker/data-platform/solutions-overview.md) file:

1. Create a new folder **Solutions** inside the **LinearComponent** folder and navigate into the folder. 
2. Create a new solution project in the **LinearComponent** folder using the following command:
 
    ```CLI
     pac solution init --publisher-name developer --publisher-prefix dev 
    ```

   > [!NOTE]
   > The [publisher-name](../data-platform/reference/entities/publisher.md) and [publisher-prefix](/powerapps/maker/data-platform/change-solution-publisher-prefix) values must be unique to your environment.
 
3. Once the new solution project is created, you need to refer to the location where the created component is located. You can add the reference by using the following command:

    ```CLI
     pac solution add-reference --path c:\users\LinearComponent
    ```

4. To generate a zip file from your solution project, you need to `cd` into your solution project directory and build the project using the following command: 

    ```CLI
     msbuild /t:restore
    ```

5. Again, run the following command:
    ```CLI
     msbuild
    ```
    > [!TIP]
    > You will be hit with the error: *Do not use the `eval` function or its functional equivalents*, when you build the solution file using the `msbuild` command and import it into Dataverse and run the solution checker.
    > Re build the solution file using the command `msbuild/property:configuration=Release` and reimport the solution into Dataverse and run the solution checker.
      
    > [!NOTE]
    > Make sure that **NuGet targets & Build Tasks** is checked. To enable it:
    > - Open **Visual Studio Installer**.
    > - For Visual Studio 2017 or higher, select **Modify**.
    > - Select **Individual Components**.
    > - Under **Code Tools**, check **NuGet targets & Build Tasks**.

6. The generated solution zip file is located in the `Solution\bin\debug` folder.
7. Manually [import the solution into Dataverse](../../maker/data-platform/import-update-export-solutions.md) using the web portal once the zip file is ready or automatically using the [Microsoft Power Platform Build Tools](https://marketplace.visualstudio.com/items?itemName=microsoft-IsvExpTools.PowerPlatform-BuildTools).

## Adding code components in model-driven apps

To add a code component like a linear input component, follow the steps mentioned in the article [Add components to columns and tables](add-custom-controls-to-a-field-or-entity.md).

## Adding code components to a canvas app

To add the code components to a canvas app, follow the steps in the article [Add code components to a canvas app](component-framework-for-canvas-apps.md#add-components-to-a-canvas-app).

### See also

[Download sample components](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework)<br/>
[Learn Power Apps component framework](/learn/paths/use-power-apps-component-framework)<br/>
[Update existing Power Apps component framework components](updating-existing-controls.md)<br/>
[Microsoft Power Platform Build Tools](/powerapps/developer/data-platform/build-tools-overview)<br/>
[Power Apps component framework API reference](reference/index.md)<br/>
[Power Apps component framework overview](overview.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]