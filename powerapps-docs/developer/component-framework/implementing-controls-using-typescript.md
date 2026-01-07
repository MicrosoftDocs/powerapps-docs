---
title: "Create your first component using Power Apps Component Framework in Microsoft Dataverse| MicrosoftDocs"
description: "Learn how to implement code components using Power Apps component framework"
author: anuitz
ms.author: anuitz
ms.date: 02/06/2023
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: pcf
contributors:
 - JimDaly
---

# Create your first component

In this tutorial, we demonstrate how to build a linear slider code component that enables users to change the numeric values using a visual slider instead of typing the values in the column.

:::image type="content" source="media/sample-linear-input-control-mda.png" alt-text="Linear input control in a model-driven app.":::

The sample code for the completed linear slider code component is available here: [PowerApps-Samples/component-framework/LinearInputControl/](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/LinearInputControl)

The following steps are required to build a linear slider code component:

- [Create a new component project](#creating-a-new-component-project)
- [Implementing manifest](#implementing-manifest)
- [Implement component logic using TypeScript](#implementing-component-logic)
- [Add style to the code components](#adding-style-to-the-code-component)
- [Build your code components](#build-your-code-components)
- [Packaging code components](#packaging-your-code-components)
- [Add your code component to an app](#add-your-code-component-to-an-app)

## Prerequisites

For this tutorial you need install the following components:

1. [Visual Studio Code (VSCode)](https://code.visualstudio.com/Download) (Ensure the Add to PATH option is select)
1. [node.js](https://nodejs.org/en/download/) (LTS version is recommended)
1. [Microsoft Power Platform CLI](/powerapps/developer/data-platform/powerapps-cli#install-power-apps-cli) (Use either Power Platform Tools for Visual Studio Code or Power Platform CLI for Windows)
1. .NET Build tools by installing one of the following: (At minimum select the workload `.NET build tools`.)
   - Visual Studio 2022
      - [Visual Studio 2022 for Windows & Mac](https://visualstudio.microsoft.com/downloads/). 
      - [Build Tools for Visual Studio 2022](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022).
   - Visual Studio 2019
      - [Visual Studio 2019 downloads](https://visualstudio.microsoft.com/vs/older-downloads/#visual-studio-2019-and-other-products).

> [!NOTE]
> You may prefer to use the [.NET 6.x SDK](https://dotnet.microsoft.com/download/dotnet/6.0) instead of the Build Tools for Visual Studio. In this case, instead of using `msbuild` you would use `dotnet build`.

> [!TIP]
> It is also recommended to install [git for source control](https://git-scm.com/downloads).

## Creating a new component project

For the purpose of this tutorial we will start in a folder located at `C:\repos`, but you can use any folder you like. The folder should represent a place you want to check in your code.


1. Create a new folder named `LinearInput`.
1. Open the `LinearInput` folder using Visual Studio Code.

   The quickest way to start is by using a command prompt window and navigate to your `LinearInput` folder and type `code .`.

   ```CLI
   c:\repos\LinearInput>code .
   ```

   This command opens your component project in Visual Studio Code.

1. Open a new terminal inside Visual Studio Code using **Terminal** -> **New Terminal**.
1. At the terminal prompt, create a new component project by passing basic parameters using the [pac pcf init](/power-platform/developer/cli/reference/pcf#pac-pcf-init) command.
   
   ```CLI
    pac pcf init --namespace SampleNamespace --name LinearInputControl --template field --run-npm-install
   ```
   
1. The above command also runs the `npm install` command for you to setup the project build tools.
   
   ```
   Running 'npm install' for you...
   ```

   > [!NOTE]
   > If you receive the error `The term 'npm' is not recognized as the name of a cmdlet, function, script file, or operable program.`, make sure you have installed [node.js](https://nodejs.org/en/download/) (LTS version is recommended) and all other prerequisites.
   
## Implementing manifest

The control manifest is an XML file that contains the metadata of the code component. It also defines the behavior of the code component. In this tutorial, this manifest file is created under the `LinearInputControl` subfolder. When you open the `ControlManifest.Input.xml` file in Visual Studio Code, you'll notice that the manifest file is predefined with some properties. More information: [Manifest](manifest-schema-reference/manifest.md).

The [control](manifest-schema-reference/control.md) node defines the namespace, version, and display name of the code component.
   
The tooling has generated the [control](manifest-schema-reference/control.md) element that is a good starting point for your control.

[!INCLUDE [cc_tip-format-xml](includes/cc_tip-format-xml.md)]

|Attribute|Description|
|---------|---------|
|`namespace`|Namespace of the code component.|
|`constructor`|Constructor of the code component.|
|`version`|Version of the component. Whenever you update the component, you need to update the version to see the latest changes in the runtime.|
|`display-name-key`|Name of the code component that is displayed on the UI.|
|`description-key`|Description of the code component that is displayed on the UI.|
|`control-type`|The code component type. This will be a `standard` control. |

If you ignore the commented areas and format the document, this is the manifest that was generated for you:

```XML
<?xml version="1.0" encoding="utf-8" ?>
<manifest>
<control namespace="SampleNamespace"
   constructor="LinearInputControl"
   version="0.0.1"
   display-name-key="LinearInputControl"
   description-key="LinearInputControl description"
   control-type="standard">
   <external-service-usage enabled="false">
   </external-service-usage>
   <property name="sampleProperty"
      display-name-key="Property_Display_Key"
      description-key="Property_Desc_Key"
      of-type="SingleLine.Text"
      usage="bound"
      required="true" />
   <resources>
      <code path="index.ts"
         order="1" />
   </resources>
</control>
</manifest>
```

From this starting point, make the following changes:

1. [Add type-group element](#add-type-group-element)
1. [Edit the property element](#edit-the-property-element)
1. [Edit resources element](#edit-resources-element)
  
### Add type-group element

Add the definition of a [type-group](manifest-schema-reference/type-group.md) element named `numbers` within the `control` element. This element specifies the component value and can contain whole, currency, floating point, or decimal values.
  
Replace the `external-service-usage` element with the `type-group` since `external-service-usage` functionality isn't used by this  control.

#### [Before](#tab/before)

```xml
<control namespace="SampleNamespace"
   constructor="LinearInputControl"
   version="0.0.1"
   display-name-key="LinearInputControl"
   description-key="LinearInputControl description"
   control-type="standard">
   <external-service-usage enabled="false">
   </external-service-usage>
   <property name="sampleProperty"
      display-name-key="Property_Display_Key"
      description-key="Property_Desc_Key"
      of-type="SingleLine.Text"
      usage="bound"
      required="true" />
   <resources>
      <code path="index.ts"
         order="1" />
   </resources>
   </control>
```

#### [After](#tab/after)

```xml
<control namespace="SampleNamespace"
   constructor="LinearInputControl"
   version="0.0.1"
   display-name-key="LinearInputControl"
   description-key="LinearInputControl description"
   control-type="standard">
   <type-group name="numbers">
      <type>Whole.None</type>
      <type>Currency</type>
      <type>FP</type>
      <type>Decimal</type>
   </type-group>
   <property name="sampleProperty"
      display-name-key="Property_Display_Key"
      description-key="Property_Desc_Key"
      of-type="SingleLine.Text"
      usage="bound"
      required="true" />
   <resources>
      <code path="index.ts"
         order="1" />
   </resources>
   </control>
```

---
   
### Edit the property element

Edit the generated `sampleProperty` [property](manifest-schema-reference/property.md) element within the `control` element. This element defines the properties of the code component like defining the data type of the column.

|Attribute|Description|
|---------|---------|
|`name`|Name of the property.|
|`display-name-key`|Display name of the property that is displayed on the UI.|
|`description-key`|Description of the property that is displayed on the UI.|
|`of-type-group`|Use the `of-type-group` attribute when you want refer to the name of a specific type group.<br /> Here, we are referring to the `type-group` named `numbers` created in the previous step.|
|`usage`|Has two properties, `bound` and `input`.<br /><br />- Bound properties are bound only to the value of the column.<br /><br />- Input properties are either bound to a column or allow a static value.|
|`required`|Defines whether the property is required.|


Edit the [property](manifest-schema-reference/property.md) node as shown here:

### [Before](#tab/before)

```xml
<property name="sampleProperty"
   display-name-key="Property_Display_Key"
   description-key="Property_Desc_Key"
   of-type="SingleLine.Text"
   usage="bound"
   required="true" />
```

### [After](#tab/after)

```xml
<property name="controlValue"
   display-name-key="Control Value"
   description-key="Control value description."
   of-type-group="numbers"
   usage="bound"
   required="true" />
```

---
   
### Edit resources element

The [resources](manifest-schema-reference/resources.md) node defines the visualization of the code component. It contains all the resources that build the visualization and styling of the code component. The [code](manifest-schema-reference/code.md) is specified as a child element under the resources element.

The generated manifest already includes a definition of the [code element](manifest-schema-reference/code.md) with `path` and `order` attribute values set. We will use these. In the following [Adding style to the code component](#adding-style-to-the-code-component) section, we will add CSS styles for the control. To support that, let's edit the manifest to add them while we have it open.

Edit the [resources](manifest-schema-reference/resources.md) node to add the following [css element](manifest-schema-reference/css.md):

### [Before](#tab/before)

```xml
<resources>
   <code path="index.ts"
   order="1" />
</resources>
```

### [After](#tab/after)

```xml
<resources>
   <code path="index.ts"
   order="1" />
   <css path="css/LinearInputControl.css"
   order="1" />
</resources>
```

---

### Completed manifest
   
The completed manifest file should look like this:

```XML
<?xml version="1.0" encoding="utf-8" ?>
<manifest>
   <control namespace="SampleNamespace"
      constructor="LinearInputControl"
      version="0.0.1"
      display-name-key="LinearInputControl"
      description-key="LinearInputControl description"
      control-type="standard">
      <type-group name="numbers">
         <type>Whole.None</type>
         <type>Currency</type>
         <type>FP</type>
         <type>Decimal</type>
      </type-group>
      <property name="controlValue"
         display-name-key="Control Value"
         description-key="Control value description."
         of-type-group="numbers"
         usage="bound"
         required="true" />
      <resources>
         <code path="index.ts"
            order="1" />
         <css path="css/LinearInputControl.css"
            order="1" />
      </resources>
   </control>
</manifest>
```

1. Save the changes to the `ControlManifest.Input.xml` file.
1. Generate `ManifestDesignTypes.d.ts` file using the following command.
   
   ```CLI
   npm run refreshTypes
   ```

   The output should look like this:
 
   ```CLI
   PS C:\repos\LinearInput> npm run refreshTypes

   > pcf-project@1.0.0 refreshTypes
   > pcf-scripts refreshTypes

   [12:38:06 PM] [refreshTypes]  Initializing...
   [12:38:06 PM] [refreshTypes]  Generating manifest types...
   [12:38:06 PM] [refreshTypes]  Generating design types...
   [12:38:06 PM] [refreshTypes]  Succeeded
   ```

1. To see the results, open the `C:\repos\LinearInput\LinearInputControl\generated\ManifestTypes.d.ts` file to see the types generated:

   ```typescript
   /*
   *This is auto generated from the ControlManifest.Input.xml file
   */

   // Define IInputs and IOutputs Type. They should match with ControlManifest.
   export interface IInputs {
      controlValue: ComponentFramework.PropertyTypes.NumberProperty;
   }
   export interface IOutputs {
      controlValue?: number;
   }
   ```

## Implementing component logic

The next step after implementing the manifest file is to implement the component logic using TypeScript. The component logic should be implemented inside the `index.ts` file. When you open the `index.ts` file in the Visual Studio Code, you'll notice that the four essential functions ([init](reference/control/init.md), [updateView](reference/control/updateview.md) , [getOutputs](reference/control/getoutputs.md), and [destroy](reference/control/destroy.md)) are predefined. Now, let's implement the logic for the code component.

Open the `index.ts` file in the code editor of your choice and make the following changes:

1. [Add properties for the control](#add-properties-for-the-control)
1. [Add the `refreshData` function as the event handler](#add-the-refreshdata-function-as-the-event-handler)
1. [Update the `init` function](#update-the-init-function)
1. [Edit the `updateView` function](#edit-the-updateview-function)
1. [Edit the `getOutputs` function](#edit-the-getoutputs-function)
1. [Edit the `destroy` function](#edit-the-destroy-function)


### Add properties for the control

#### [Before](#tab/before)

```typescript
export class LinearInputControl
implements ComponentFramework.StandardControl<IInputs, IOutputs>
{
/**
   * Empty constructor.
*/
constructor() {}
```
#### [After](#tab/after)

```typescript
export class LinearInputControl
implements ComponentFramework.StandardControl<IInputs, IOutputs>
{
private _value: number;
private _notifyOutputChanged: () => void;
private labelElement: HTMLLabelElement;
private inputElement: HTMLInputElement;
private _container: HTMLDivElement;
private _context: ComponentFramework.Context<IInputs>;
private _refreshData: EventListenerOrEventListenerObject;
/**
   * Empty constructor.
*/
constructor() {}
```

---
   
### Add the `refreshData` function as the event handler
   
```typescript
public refreshData(evt: Event): void {
   this._value = this.inputElement.value as any as number;
   this.labelElement.innerHTML = this.inputElement.value;
   this._notifyOutputChanged();
}
```
   
### Update the `init` function

#### [Before](#tab/before)

```typescript
public init(
   context: ComponentFramework.Context<IInputs>,
   notifyOutputChanged: () => void,
   state: ComponentFramework.Dictionary,
   container: HTMLDivElement
   ): void {
      // Add control initialization code
   }
```

#### [After](#tab/after)

```typescript
public init(
   context: ComponentFramework.Context<IInputs>,
   notifyOutputChanged: () => void,
   state: ComponentFramework.Dictionary,
   container: HTMLDivElement
   ): void {
      // Add control initialization code
   this._context = context;
   this._container = document.createElement("div");
   this._notifyOutputChanged = notifyOutputChanged;
   this._refreshData = this.refreshData.bind(this);

   // creating HTML elements for the input type range and binding it to the function which 
   // refreshes the control data
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
   this.labelElement.setAttribute("class", "LinearRangeLabel");
   this.labelElement.setAttribute("id", "lrclabel");

   // retrieving the latest value from the control and setting it to the HTMl elements.
   this._value = context.parameters.controlValue.raw!;
   this.inputElement.setAttribute(
      "value",
      context.parameters.controlValue.formatted
      ? context.parameters.controlValue.formatted
      : "0"
   );
   this.labelElement.innerHTML = context.parameters.controlValue.formatted
      ? context.parameters.controlValue.formatted
      : "0";

   // appending the HTML elements to the control's HTML container element.
   this._container.appendChild(this.inputElement);
   this._container.appendChild(this.labelElement);
   container.appendChild(this._container);
}
```

---
   
### Edit the `updateView` function

#### [Before](#tab/before)

```typescript
public updateView(context: ComponentFramework.Context<IInputs>): void {
   // Add code to update control view
}
```

#### [After](#tab/after)

```typescript
public updateView(context: ComponentFramework.Context<IInputs>): void {
   // Add code to update control view
   // storing the latest context from the control.
   this._value = context.parameters.controlValue.raw!;
   this._context = context;
   this.inputElement.setAttribute(
      "value",
      context.parameters.controlValue.formatted
      ? context.parameters.controlValue.formatted
      : ""
   );
   this.labelElement.innerHTML = context.parameters.controlValue.formatted
      ? context.parameters.controlValue.formatted
      : "";
}
```

---

### Edit the `getOutputs` function

#### [Before](#tab/before)

```typescript
public getOutputs(): IOutputs {
   return {};
}
```


#### [After](#tab/after)

```typescript
public getOutputs(): IOutputs {
   return {
      controlValue: this._value,
   };
}
```

---
   
### Edit the `destroy` function

#### [Before](#tab/before)

```typescript
public destroy(): void {
   // Add code to cleanup control if necessary
   }
}
```


#### [After](#tab/after)

```typescript
public destroy(): void {
   // Add code to cleanup control if necessary
   this.inputElement.removeEventListener("input", this._refreshData);
   }
}
```

---

The complete `index.ts` file should look like this:

```typescript
import { IInputs, IOutputs } from "./generated/ManifestTypes";

export class LinearInputControl
implements ComponentFramework.StandardControl<IInputs, IOutputs>
{
private _value: number;
private _notifyOutputChanged: () => void;
private labelElement: HTMLLabelElement;
private inputElement: HTMLInputElement;
private _container: HTMLDivElement;
private _context: ComponentFramework.Context<IInputs>;
private _refreshData: EventListenerOrEventListenerObject;
/**
   * Empty constructor.
*/
constructor() {}

/**
   * Used to initialize the control instance. Controls can kick off remote server calls 
      and other initialization actions here.
   * Data-set values are not initialized here, use updateView.
   * @param context The entire property bag available to control via Context Object; 
      It contains values as set up by the customizer mapped to property names defined 
      in the manifest, as well as utility functions.
   * @param notifyOutputChanged A callback method to alert the framework that the 
      control has new outputs ready to be retrieved asynchronously.
   * @param state A piece of data that persists in one session for a single user. 
      Can be set at any point in a controls life cycle by calling 'setControlState' 
      in the Mode interface.
   * @param container If a control is marked control-type='standard', it will receive 
      an empty div element within which it can render its content.
*/
public init(
   context: ComponentFramework.Context<IInputs>,
   notifyOutputChanged: () => void,
   state: ComponentFramework.Dictionary,
   container: HTMLDivElement
): void {
   // Add control initialization code
   this._context = context;
   this._container = document.createElement("div");
   this._notifyOutputChanged = notifyOutputChanged;
   this._refreshData = this.refreshData.bind(this);

   // creating HTML elements for the input type range and binding it to the function which 
   // refreshes the control data
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
   this.labelElement.setAttribute("class", "LinearRangeLabel");
   this.labelElement.setAttribute("id", "lrclabel");

   // retrieving the latest value from the control and setting it to the HTMl elements.
   this._value = context.parameters.controlValue.raw!;
   this.inputElement.setAttribute(
      "value",
      context.parameters.controlValue.formatted
      ? context.parameters.controlValue.formatted
      : "0"
   );
   this.labelElement.innerHTML = context.parameters.controlValue.formatted
      ? context.parameters.controlValue.formatted
      : "0";

   // appending the HTML elements to the control's HTML container element.
   this._container.appendChild(this.inputElement);
   this._container.appendChild(this.labelElement);
   container.appendChild(this._container);
}

public refreshData(evt: Event): void {
   this._value = this.inputElement.value as any as number;
   this.labelElement.innerHTML = this.inputElement.value;
   this._notifyOutputChanged();
}

/**
   * Called when any value in the property bag has changed. This includes field values, 
      data-sets, global values such as container height and width, offline status, control 
      metadata values such as label, visible, etc.
   * @param context The entire property bag available to control via Context Object; 
      It contains values as set up by the customizer mapped to names defined in the manifest, 
      as well as utility functions
*/
public updateView(context: ComponentFramework.Context<IInputs>): void {
   // Add code to update control view
   // storing the latest context from the control.
   this._value = context.parameters.controlValue.raw!;
   this._context = context;
   this.inputElement.setAttribute(
      "value",
      context.parameters.controlValue.formatted
      ? context.parameters.controlValue.formatted
      : ""
   );
   this.labelElement.innerHTML = context.parameters.controlValue.formatted
      ? context.parameters.controlValue.formatted
      : "";
}

/**
   * It is called by the framework prior to a control receiving new data.
   * @returns an object based on nomenclature defined in manifest, 
      expecting object[s] for property marked as "bound" or "output"
*/
public getOutputs(): IOutputs {
   return {
      controlValue: this._value,
   };
}

/**
   * Called when the control is to be removed from the DOM tree. 
      Controls should use this call for cleanup.
   * i.e. cancelling any pending remote calls, removing listeners, etc.
*/
public destroy(): void {
   // Add code to cleanup control if necessary
   this.inputElement.removeEventListener("input", this._refreshData);
      }
}
```
   
When you are finished, save the changes to the `index.ts` file
   
## Adding style to the code component

Developers and app makers can define their styling to represent their code components visually using CSS. CSS allows the developers to describe the presentation of code components, including style, colors, layouts, and fonts. The linear input component's [init](reference/control/init.md) method creates an input element and sets the class attribute to `linearslider`. The style for the `linearslider` class is defined in a separate `CSS` file. Additional component resources like `CSS` files can be included with the code component to support further customizations.

> [!IMPORTANT]
> When you implement styling to your code components using CSS, ensure that the CSS is scoped to your control using the automatically generated CSS classes applied to the container `DIV` element for your component.
>
> If your CSS is scoped globally, it will likely break the existing styling of the form or screen where the code component is rendered.
>
> If using a third-party CSS framework, use a version of that framework that is already namespaced or otherwise wrap that framework in a namespace manually either by hand or using a CSS preprocessor.

1. Create a new `css` subfolder under the `LinearInputControl` folder. 
1. Create a new `LinearInputControl.css` file inside the `css` subfolder. 
1. Add the following style content to the `LinearInputControl.css` file:
   
    ```CSS
    .SampleNamespace\.LinearInputControl input[type=range].linearslider {   
       margin: 1px 0;   
       background:transparent;
       -webkit-appearance:none;
       width:100%;padding:0;
       height:24px;
       -webkit-tap-highlight-color:transparent
    }
    .SampleNamespace\.LinearInputControl input[type=range].linearslider:focus {
       outline: none;
    }
    .SampleNamespace\.LinearInputControl input[type=range].linearslider::-webkit-slider-runnable-track {   
       background: #666;
       height:2px;
       cursor:pointer
    }   
    .SampleNamespace\.LinearInputControl input[type=range].linearslider::-webkit-slider-thumb {   
       background: #666;   
       border:0 solid #f00;
       height:24px;
       width:10px;
       border-radius:48px;
       cursor:pointer;
       opacity:1;
       -webkit-appearance:none;
       margin-top:-12px
    }    
    .SampleNamespace\.LinearInputControl input[type=range].linearslider::-moz-range-track {   
       background: #666;   
       height:2px;
       cursor:pointer  
    }   
    .SampleNamespace\.LinearInputControl input[type=range].linearslider::-moz-range-thumb {   
       background: #666;   
       border:0 solid #f00;
       height:24px;
       width:10px;
       border-radius:48px;
       cursor:pointer;
       opacity:1;
       -webkit-appearance:none;
       margin-top:-12px
    }   
    .SampleNamespace\.LinearInputControl input[type=range].linearslider::-ms-track {   
       background: #666;   
       height:2px;
       cursor:pointer  
    }    
    .SampleNamespace\.LinearInputControl input[type=range].linearslider::-ms-thumb {   
       background: #666;   
       border:0 solid #f00;
       height:24px;
       width:10px;
       border-radius:48px;
       cursor:pointer;
       opacity:1;
       -webkit-appearance:none;
    }
    ```
    
1. Save the `LinearInputControl.css` file.
1. Note that the `ControlManifest.Input.xml` file already includes the `css` resource file inside the resources element because that was completed in the [Implementing manifest](#implementing-manifest) section earlier.
   
    ```XML
   <resources>
   <code path="index.ts"
      order="1" />
   <css path="css/LinearInputControl.css"
      order="1" />
   </resources>
    ```

> [!NOTE]
> Power Apps component framework uses [RESX web resources](../model-driven-apps/resx-web-resources.md) to manage the localized strings shown on any user interface. The resources to support localization are also registered in the `resources` node.
>
> This first tutorial does not include localization capability. Localization is included in other tutorials.
> 
> See the [Localization API](sample-controls/localization-api-control.md) sample, to learn how to localize  code components using `resx` web resources.

## Build your code components

After you finish adding manifest, component logic, and styling, build the code components using the command:

```CLI
npm run build
```

The output should look something like this:

```CLI
> pcf-project@1.0.0 build
> pcf-scripts build

[2:05:41 PM] [build]  Initializing...
[2:05:41 PM] [build]  Validating manifest...
[2:05:41 PM] [build]  Validating control...
[2:05:42 PM] [build]  Running ESLint...
[2:05:43 PM] [build]  Generating manifest types...
[2:05:43 PM] [build]  Generating design types...
[2:05:43 PM] [build]  Compiling and bundling control...
[Webpack stats]:
asset bundle.js 6.56 KiB [emitted] (name: main)
./LinearInputControl/index.ts 4.9 KiB [built] [code generated]
webpack 5.75.0 compiled successfully in 2049 ms
[2:05:45 PM] [build]  Generating build outputs...
[2:05:45 PM] [build]  Succeeded
PS C:\repos\LinearInput\LinearInputcontrol> 
```

The build generates an updated TypeScript type declaration file under the `LinearInputControl/generated` folder.
The component is compiled into the `out/controls/LinearInputControl` folder. The build artifacts include:

- `bundle.js` – Bundled component source code.
- `ControlManifest.xml` – Actual component manifest file that is uploaded to the Microsoft Dataverse organization.

> [!NOTE]
> eslint rules may impact your build, depending on how they have been configured. If you receive an error during build:
> 
> ```
> [12:58:30 PM] [build]  Failed:
> [pcf-1065] [Error] ESLint validation error:
> C:\project\LinearInput\LinearInputControl\index.ts
>   10:26  error  'EventListenerOrEventListenerObject' is not defined  no-undef
> ```
>
> Check your eslint rules in `.eslintrc.json` and set linting rules to `["warn"]`. For example, if you receive the error:
> 
> ```error  'EventListenerOrEventListenerObject' is not defined  no-undef```
> 
> Then you can open `.eslintrc.json` and edit the rules to add a `["warn"]` value for the rule `no-undef`:
>
> ```json
>     "rules": {
>       "no-unused-vars": "off",
>       "no-undef": ["warn"]
>     }
> ```
> 
> With the eslint rules updated, your control should build cleanly.

## Debugging your code component

Once you're done implementing the code component logic, run the following command to start the debugging process. More information: [Debug code components](debugging-custom-controls.md)

```CLI
npm start watch
```

The output should look something like this:

```CLI
> pcf-project@1.0.0 start
> pcf-scripts start "watch"

[2:09:10 PM] [start] [watch] Initializing...
[2:09:10 PM] [start] [watch] Validating manifest...
[2:09:10 PM] [start] [watch] Validating control...
[2:09:11 PM] [start] [watch] Generating manifest types...
[2:09:11 PM] [start] [watch] Generating design types...
[2:09:11 PM] [start] [watch] Compiling and bundling control...
[Webpack stats]:
asset bundle.js 6.56 KiB [emitted] (name: main)
./LinearInputControl/index.ts 4.9 KiB [built] [code generated]
webpack 5.75.0 compiled successfully in 2060 ms
[2:09:13 PM] [start] [watch] Generating build outputs...
[2:09:13 PM] [start] [watch] Starting control harness...

Starting control harness...

[Browsersync] Access URLs:

 ----------------------------
 Local: http://localhost:8181
 ----------------------------

[Browsersync] Serving files from: C:\repos\LinearInput\out\controls\LinearInputControl

[Browsersync] Watching files...

```

And a browser should open to the PCF Control Sandbox so that you can see the control and test it.

:::image type="content" source="../model-driven-apps/clientapi/media/linear-input-control-pcf-control-sandbox.png" alt-text="Linear input control in PCF Control Sandbox":::

## Packaging your code components

Follow these steps to create and import a [solution](../../maker/data-platform/solutions-overview.md) file:

1. Create a new folder named **Solutions** inside the **LinearInputControl** folder and navigate into the folder. 

   ```CLI
     mkdir Solutions
     cd Solutions
   ```

1. Create a new solution project in the **LinearInputControl** folder using the [pac solution init](/power-platform/developer/cli/reference/solution#pac-solution-init) command:

   ```CLI
     pac solution init --publisher-name Samples --publisher-prefix samples 
   ```

   > [!NOTE]
   > The [publisher-name](/power-platform/developer/cli/reference/solution#--publisher-name--pn) and [publisher-prefix](/power-platform/developer/cli/reference/solution#--publisher-prefix--pp) values must be the same as either an existing solution publisher, or a new one that you want to create in your target environment.
   > 
   > You can retrieve a list of current values using this query on your target environment:
   >
   > `[Environment URI]/api/data/v9.2/publishers?$select=uniquename,customizationprefix`
   >
   > More information: [Query data using the Web API](../data-platform/webapi/query/overview.md)



   The output of the pac solution init command should look like this:

   ```CLI
   Dataverse solution project with name 'solutions' created successfully in: 'C:\repos\LinearInput\linearinputcontrol\solutions'
   Dataverse solution files were successfully created for this project in the sub-directory Other, using solution name solutions, publisher name Samples, and customization prefix samples.
   Please verify the publisher information and solution name found in the Solution.xml file.
   PS C:\repos\LinearInput\linearinputcontrol\solutions> 
   ```

1. Once the new solution project is created, you need to refer to the location where the created component is located. You can add the reference by using the following command:
   
    ```CLI
    pac solution add-reference --path ..\..\
    ```
   
    > [!NOTE]
    > The path provided here is related to the current **Solutions** folder that was created underneath the **LinearInputControl** folder. You can also provide an absolute path.
   
   The output of the command should look like this:
   
   ```CLI
   Project reference successfully added to Dataverse solution project.
   ```
   
1. To generate a zip file from your solution project, when inside the `cdsproj` solution project directory, using the following command:

   ```CLI
   msbuild /t:restore
   ```

   Or if you have installed the .NET 6 SDK:

   ```CLI
   dotnet build
   ```

1. Run the following command again:

   ```CLI
   msbuild
   ```

   > [!NOTE]
   > If you receive the error `Missing required tool: MSBuild.exe/dotnet.exe`. Add `MSBuild.exe/dotnet.exe` in Path environment variable or use `Developer Command Prompt for Visual Studio Code`. As mentioned in [Prerequisites](#prerequisites), you must install .NET build tools.
   > [!TIP]
   > You will see the message *Do not use the `eval` function or its functional equivalents*, when you build the solution file using the `msbuild` command and import it into Dataverse and run the solution checker.
   > Re build the solution file using the command `msbuild/property:configuration=Release` and reimport the solution into Dataverse and run the solution checker. More information:  [Debug code components](debugging-custom-controls.md).

1. The generated solution zip file is located in the `Solution\bin\debug` folder.
1. Manually [import the solution into Dataverse](../../maker/data-platform/import-update-export-solutions.md) using [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) once the zip file is ready or automatically using the [Microsoft Power Platform Build Tools](https://marketplace.visualstudio.com/items?itemName=microsoft-IsvExpTools.PowerPlatform-BuildTools).

> [!NOTE]
> Manually publish the customizations if you are importing unmanaged solution.

## Add your code component to an app

To add a code component to an app, follow the steps in these articles:

- [Add components to columns and tables for model-driven apps](add-custom-controls-to-a-field-or-entity.md)
- [Add code components to a canvas app](component-framework-for-canvas-apps.md#add-components-to-a-canvas-app)
- [Use code components in portals](/powerapps/maker/portals/component-framework-tutorial)


### See also

[Download sample components](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework)<br/>
[Learn Power Apps component framework](/training/paths/use-power-apps-component-framework)<br/>
[Overview of tools and apps used with ALM](/power-platform/alm/tools-apps-used-alm)<br/>
[Power Apps component framework API reference](reference/index.md)<br/>
[Power Apps component framework overview](overview.md)<br/>
[Debug code components](debugging-custom-controls.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
