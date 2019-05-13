---
title: "Implementing Custom Components using TypeScript | MicrosoftDocs"
description: "How to implement a custom components using TypeScript"
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.topic: "index-page"
ms.assetid: 18e88d702-3349-4022-a7d8-a9adf52cd34f
ms.author: "nabuthuk"
---

# Implement components using TypeScript

[!INCLUDE[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This tutorial will walk you through creating a new custom component in Typescript. The sample component is a linear input component. The linear input component enables users to enter numeric values using a visual slider instead of directly keying in values. 

## Creating a new component project

To create a new project, follow the steps below:

1. Open a **Developer Command Prompt for VS 2017** window.
2. Create a new folder for the project using the command 
   ```CLI
   mkdir LinearControl
   ```
3. Navigate into the new directory using the command 
   ```CLI
    cd LinearControl
   ```
4. Create the component project using the command 
   ```CLI
    pac pcf init --namespace SampleNamespace --name TSLinearInputControl --template field
   ```
4. Install the project build tools using the command 
    ```CLI
    npm install
    ```

## Implementing Manifest

A custom component is defined by the information in the `ControlManifest.Input.xml` manifest file. In this walkthrough, this file is created under the `<Your component Name>` sub folder. For the linear input component, a property will be defined to store the numeric value of the slider input.

1. Open the `ControlManifest.Input.xml` file in the code editor (Visual Studio Code). The `ControlManifest.Input.xml` file defines an initial component property called `sampleProperty`.

    ```XML
    <property name="sampleProperty" display-name-key="Property_Display_Key" description-key="Property_Desc_Key" of-type="SingleLine.Text" usage="bound" required="true" /> 
    ```

2. Rename the `sampleProperty` and change the property type

    ```XML
    <property name="sliderValue" display-name-key="sliderValue_Display_Key" description-key="sliderValue_Desc_Key" of-type-group="numbers" usage="bound" required="true" /> 
    ```

3. The of-type-group attribute references a group of allowable numbers. Add the following type-group element as a sibling to the <property> element in the manifest. The type-group specifies the component value and can contain whole, currency, floating point, or decimal values.

    ```XML
    <type-group name="numbers"> 
      <type>Whole.None</type> 
      <type>Currency</type> 
      <type>FP</type> 
      <type>Decimal</type> 
     </type-group> 
    ```

4. Save the changes to the `ControlManifest.Input.xml` file.
5. Build the component project using the command 
   ```CLI
   npm run build
   ```
6. The build generates an updated Typescript type declaration file under `TSLinearInputControl/generated folder`.  The `ManifestTypes.d.ts` file defines the properties that your component will have access to Typescript source code.

## Implementing component logic

Source for the custom component is implemented in the `index.ts` file. The `index.ts` file includes scaffolding for interface methods that are required by the PowerApps component framework. 

1. Open the `index.ts` file in code editor of your choice.
2. Update the `TSLinearInputControl` class with the following

```TypeScript
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
    this._value = context.parameters.sliderValue.raw;
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
    this._value = context.parameters.sliderValue.raw;
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

3. Rebuild the project using the command 
   ```CLI
   npm run build
   ```
 
4. The component is compiled into the `out/controls/TSLinearInputControl` folder. The build artifacts includes:

   - bundle.js – Bundled component source code 
   - ControlManifest.xml – Actual component manifest file that will be uploaded to Common Data Service organization.

## Adding Style to the custom component

The linear input control’s `init` method creates an input element and sets the class attribute to `linearslider`. The style for the `linearslider` class is defined in a separate `css` file. Additional component resources like `css` files can be included with the custom component to support further customizations.

1. Edit the `ControlManifest.Input.xml` file to include an additional `css` resource inside the <resources> element
 
    ```XML
    <resources> 
      <code path="index.ts" order="1"/> 
      <css path="css/TS_LinearInputControl.css" order="1"/> 
    </resources> 
     ```

2. Create a new `css` sub folder under the `TSLinearInputControl` folder. 
3. Create a new `TS_LinearInputControl.css` file inside the `css` sub folder. 
4. Add the following style content to `TS_LinearInputControl.css` file

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

5. Save the `TS_LinearInputControl.css` 
6. Rebuild the project using the command 
   ```CLI
   npm run build
   ```
7. Inspect the build output under `./out/controls/TSLinearInputControl` and observe that the `TS_LinearInputControl.css` file is now included with the compiled build artifacts. 

## Debugging your custom component

Once you are done implementing your custom component logic, run the following command to start the debugging process

```CLI
npm start
```

> [!NOTE]
> Today you can only visualize your field component, but dataset support is coming soon. Below image shows a sample component implemented in the tutorial below just as an example. 

> [!div class="mx-imgBorder"]
> ![local-host](media/local-host.png "local host")

As shown in the image above, the browse window will open with 3 sections. Your component will be rendered in the left pane while the right pane consists of **Inputs** and **Outputs** sections

  - **Inputs** section is an interactive UI that displays all properties and their types or type-groups defined in the manifest file. It allows you to key in mock data for each property. 
  - **Outputs** section renders the output whenever a component's `getOutputs` method gets called.  
 
> [!NOTE]
> If you want to modify the manifest file or create additional properties, you will need to restart the debug process before they appear in the inputs section.

As you are inputting mock data, you can use the browser’s debugging capabilities to observe the component behavior. Each browser provides you with a debugging tool to help you debug your code natively in the browser. Typically, you can activate debugging in your browser by pressing the **F12** key to display the native developer tool used for debugging. Today both Chrome and Edge browsers are supported.

For example, on **Microsoft Edge**,

- Press **F12** to open inspector.
- Click on your component
- On top bar, go to **Debugger**, and then start searching for the component name described in the Manifest file in the search bar. For example, type your component name like `Hello World component`.

     > [!div class="mx-imgBorder"]
     > ![debug-component](media/debug-control.png "Debug component")

> [!NOTE]
> It is always a good practice to set breakpoints on the component's life cycle methods like `init` and `updateView`

You can also interact with the component locally in real time and observe elements in the DOM by setting a breakpoint in the sources tab as follows:

> [!div class="mx-imgBorder"]
> ![local-host](media/local-host.png "local host")

> [!div class="mx-imgBorder"]
> ![debug-component](media/debug-control-1.png "Debug component 1")


 > [!NOTE]
 > You can also use the following steps to perform outer loop debugging using fiddler.
 >    1. Install [Fiddler](https://www.telerik.com/download/fiddler)
 >    2. Follow the steps to configure [AutoResponder](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/streamline-javascript-development-fiddler-autoresponder)

## Deploying your custom components

Once the development and debugging is finished, you just have one step remaining to deploy your new component.  

Follow the steps below to create and import a [solution](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/customize/solutions-overview) file:

1. Create a new directory and go to it 'cd <new directory name>'
2. Create a new solution project in the directory of your choice by using the command 
 
    ```CLI
     pac solution init --publisherName <enter your publisher name> --customizationPrefix <enter your publisher name>` after `cd <your new folder>
    ```

   > [!NOTE]
   > The [publisherName](https://docs.microsoft.com/en-us/powerapps/developer/common-data-service/reference/entities/publisher) and [cutomizationPrefix](https://docs.microsoft.com/en-us/powerapps/maker/common-data-service/change-solution-publisher-prefix) values must be unique to your environment.
 
3. Once the new solution project is created, you need to refer to the location where the created component is located. You can add the reference by using the command

    ```CLI
     pac solution add-reference --path <path or relative path of your PowerApps component framework project on disk>
    ```

4. To generate a zip file from your solution project, you will need to `cd` into your solution project directory and build the project using the command `msbuild /t:restore` then `msbuild`

    > [!NOTE]
    > If msbuild 15 is not in the path, open Developer Command Prompt for Vs 2017 to run the `msbuild` commands.

    > [!NOTE]
    > Building the solution in the debug configuration, generates an unmanaged solution package. A managed solution package is generated by building the solution in release configuration. These settings can be overridden by specifying SolutionPackageType property in `cdsproj` file.
    
    > [!NOTE]
    > If you would like your project build to emit a managed solution or both managed and unmanaged, open the folder where you created your solution project, edit the `cdsproj` file and uncomment the below property group:
      ```XML
         <PropertyGroup>
          <SolutionPackageType>Managed</SolutionPackageType>
           </PropertyGroup>
      ```

    > [!NOTE]
    > You can also enable additional solution packaging [capabilities](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/compress-extract-solution-file-solutionpackager) by adding any of the property group elements below:

     ```XML
       <PropertyGroup>
         <SolutionPackageErrorLevel />
         <SolutionPackageEnableLocalization />
        <SolutionPackagerWorkingDirectory />
        <SolutionPackageLogFilePath />
        <SolutionPackageZipFilePath />
        <SolutionPackageMapFilePath />
       </PropertyGroup>
     ```

5. The generated solution zip file is located in `\bin\debug\`.
6. You should manually [import the solution](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/customize/import-update-export-solutions) using the web portal once the zip file is ready.

## Adding custom components to a field or an entity

To add a custom component like data-set component or simple table component to a grid or view, follow the steps mentioned in the topic [Add components to fields and entities](add-custom-controls-to-a-field-or-entity.md).


### See also

[Download sample components](https://go.microsoft.com/fwlink/?linkid=2088525)<br/>
[Update existing PowerApps component framework controls](updating-existing-controls.md)<br/>
[PowerApps component framework API Reference](reference/index.md)<br/>
[PowerApps component framework Overview](overview.md)
