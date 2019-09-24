---
title: "Quick start sample code components | MicrosoftDocs"
description: "How to implement a simple code components using TypeScript"
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.topic: "index-page"
ms.assetid: 18e88d702-3349-4022-a7d8-a9adf52cd34f
ms.author: "nabuthuk"
author: Nkrb
---

# Implement components using TypeScript

This quick start tutorial walks you through the process of creating a simple **HelloWorld** code component in Typescript. This sample code component replaces a text field and displays *Hello World* text.

## Creating a new component project

To create a new project:

1. Open a Developer Command Prompt for VS 2017 window.
1. Create a new folder for the project using the command. 
    ```CLI
    mkdir HelloWorldComponent
    ```

1. Navigate into the new directory using the command `cd LinearComponent`. 
1. Create the component project using the command. 
    ```CLI
    pac pcf init --namespace SampleNamespace --name TSHelloWorld --template field
    ``` 

1. Install the project build tools using the command `npm install`.
1. Open your project folder C:\Users\<your name>\Documents\<My_PCF_Component> in any developer environment of your choice and get started with your code component development. The quickest way to get started is by running `code .` from your command prompt once you are in the C:\Users\<your name>\Documents\<My_PCF_Component> directory. This command opens your component project in Visual Studio Code.

## Implementing Manifest

Manifest is an XML file that contains the metadata of the code component. It also defines the behavior of the code component. In this quick start tutorial, this manifest file is created under the `<Your component Name>` sub folder. When you open the `ControlManifest.Input.xml` file in Visual Studio Code, you will notice that the manifest file is predefined with some properties. Make changes to the predefined manifest file as shown below:

The [control](manifest-schema-reference/control.md) node defines the namespace, version and display name of the code component. Now, define each property of the [control](manifest-schema-reference/control.md) node as shown below:

 - **namespace**: The namespace of the code component. 
 - **Constructor**: 
 - **Version**: The version of the component. Whenever you update the component, you need to update the version inorder to see the changes in the run time.
 - **display-name-key**: The name of the code component that is displayed on the UI.
 - **description-name-key**: The description of the code component that is displayed on the UI.
 - **control-type**" The code component type. Only *standard* type of code components are supported.

   ```XML
   <?xml version="1.0" encoding="utf-8" ?>
   <manifest>
    <control namespace="SampleNameSpace" constructor="TSHelloWorldComponent" version="1.0.0" display-name-key="Hello World Component" description-key="Displays the Hello World text inside the field." control-type="standard">
   ```

 The [property](manifest-schema-reference/property.md) node defines the properties of the code component like defining the data type of field. The  property node is specified as child element under the control element. Define the [property](manifest-schema-reference/property.md) node as shown below:

  - **name**: Name of the property.
  - **display-name-key**: The display name of the property that is displayed on the UI.
  - **description-name-key**: The description of the property that is displayed on the UI. 
  - **of-type**: The data type of the field that you want to bind the code component. The **of-type-group** is used when you want to have more than two data type fields.
  - **usage**: It has two properties *bound* and *input*. Bound properties are the one that are only bound to the value of the field. Input properties are the one that are either bound to a field or allows a static value.
  - **required**: Defines whether the property is required or not.

    ```XML
    <property name="myFirstProperty" display-name-key="myFirstProperty_Display_Key" description-key="myFirstProperty_Desc_Key" of-type="SingleLine.Text" usage="bound" required="true" />
    ```
The [resources](manifest-schema-reference/resources.md) node defines the visualization of the code component. It contains all the resources that makes up the code component. The [code](manifest-schema-reference/code.md) is specified as child element under the resources element. Define the [resources](manifest-schema-reference/resources.md) as shown below:

 - **code**: Refers to the path where all the resource files are located.
 
   ```XML
   <resources>
	  <code path="index.ts" order="1" />
	  <css path="css/TS_HelloWorldControl.css" order="1" />
	</resources>
   ```
The overall manifest file should look something like this: 

```XML
<?xml version="1.0" encoding="utf-8" ?>
<manifest>
	<control namespace="MyNameSpace" constructor="TSHelloWorldComponent" version="1.0.0" display-name-key="Hello World Component" description-key="Displays the Hello World text inside the field." control-type="standard">
		<property name="myFirstProperty" display-name-key="myFirstProperty_Display_Key" description-key="myFirstProperty_Desc_Key" of-type="SingleLine.Text" usage="bound" required="true" />
		<resources>
			<code path="index.ts" order="1" />
			<css path="css/TS_HelloWorldComponent.css" order="1" />
		</resources>
	</control>
</manifest>
```

## Implement component logic

The next step after implementing the manifest file, is to implement the component logic using TypeScript. The component logic should be implemented inside the `index.ts` file. When you open the `index.ts` file in Visual Studio Code, you will notice that the four important classes are predefined. Now, let's implement the logic for the code component. First thing you need to do is to define the `labelElement` as shown below:

```TypeScript
module MyNameSpace
{
    export class TSHelloWorldComponent implements ControlFramework.StandardControl<InputsOutputs.IInputs, InputsOutputs.IOutputs> {

        private _labelElement: HTMLLabelElement;
```

Now, let's go ahead and implement the [init](reference/control/init.md) method which executes when the page loads. Define the code elements and add the code elements to div as shown below:

```TypeScript
public init(context: ControlFramework.Context<InputsOutputs.IInputs>, notifyOutputChanged: () => void, state: ControlFramework.Dictionary, container:HTMLDivElement)
        {
            this._labelElement = document.createElement("label");
			this._labelElement.setAttribute("class", "TS_HelloWorldColor");
            container.appendChild(this._labelElement);
        }
```

Now implement the [updateView](reference/control/updateview.md) method as hown below. The `updateView` method is called whenever there are some updates to the field. 

```TypeScript
public updateView(context: ControlFramework.Context<InputsOutputs.IInputs>,)
        {
            this._labelElement.innerText = "Hello World! (TS)";
        }
```
Similarly, implement the [getOutputs](reference/control/getoutputs.md) and [destroy](reference/control/destroy.md) methods as shown below:

```TypeScript
public getOutputs(): InputsOutputs.IOutputs
{
    return {};
  }

public destroy()
{
    }
```

### Complete code 

```TypeScript
import { IInputs, IOutputs } from "./generated/ManifestTypes";
module MyNameSpace
{
    export class TSHelloWorldControl implements ControlFramework.StandardControl<InputsOutputs.IInputs, InputsOutputs.IOutputs> {

    private _labelElement: HTMLLabelElement;

public init(context: ControlFramework.Context<InputsOutputs.IInputs>, notifyOutputChanged: () => void, state: ControlFramework.Dictionary, container:HTMLDivElement)
{
    this._labelElement = document.createElement("label");
	this._labelElement.setAttribute("class", "TS_HelloWorldColor");
    container.appendChild(this._labelElement);
        }

public updateView(context: ControlFramework.Context<InputsOutputs.IInputs>,)
    {
        this._labelElement.innerText = "Hello World";
    }

public getOutputs(): InputsOutputs.IOutputs
  {
     return {};
    }

public destroy()
        {
          
        }
    }
}
```

## Adding style to the code component

The component’s [init](reference/control/init.md) method creates an label element and sets the class attribute. The style for the `HelloWorld` class is defined in a separate `CSS` file. Additional component resources like `CSS` files can be included with the code component to support further customizations.

1. Create a new `css` subfolder under the `TSHelloWorldComponent` folder. 
2. Create a new `TS_HelloWorldComponent.css` file inside the `css` subfolder. 
3. Add the following style content to `TS_HelloWorldComponent.css` file.

    ```CSS
    .MyNameSpace\.TSHelloWorldComponent .TS_HelloWorldColor{
	color: green;
     }
    ```