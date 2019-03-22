---
title: Update existing custom controls using PowerApps Component Framework Tooling| Microsoft Docs
description: Update controls using the PowerApps Component Framework Tooling
keywords: PowerApps ContrComponentol Framework, Custom Controls, Control Framework
ms.author: nabuthuk
manager: kvivek
ms.date: 03/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d2cbf58a-9112-45c2-b823-2c07a310714c
---
# Updating existing custom controls 

To use the new **PowerApps Component Framework (PCF)** build tools with your existing PCF custom control source, a few changes are required.

## Creating an empty project

Use the PowerApps CLI to create a new empty project for your custom control. More information [Create Controls using tooling](create-custom-controls-using-pcf.md).
Once the project has been created migrate your custom control source to the new project:

1. Copy or replace the control source from the old source file into **index.ts**.
2. Copy or replace the contents of **ControlManifest.xml** into **ControlManifest.Input.xml** file.
3. Copy all other peripheral control resources such as css, resx, img into the corresponding subfolder from the old project to the new project.

    > [!div class="mx-imgBorder"]
    > ![Old control project](media/old-control-project.png "Old control project")

    > [!div class="mx-imgBorder"]
    > ![New control project](media/new-control-project.png "New control project")

## Updating Manifest file

The `ControlManifest.xml` file that defines the custom control properties is been replaced with a `ControlManifest.Input.xml` file. There should otherwise be very little change in schema between the two files.
There are a couple of important semantic changes.

1. The `code` resource entry must now point to the pre-compiled source file of the custom control. The file name has been defaulted to **index.ts**.
For example, if your control source is implemented in a file called `MyControl.ts`, then the `code` entry in `ControlManifest.Input.xml` must point to that file. The `code` file must also be a valid Typescript file. This is in contrast to legacy manifest files that specified the compiled JS output file in the `code` entry.
2. The `path` attribute of the resource element like `code` or `css` now refers to the local path to the file on disk. For example,

    ```XML
   <resources>
    <css path="css/TS_LinearInputControl.css" order="1"/>
    </resources>
    ```

The `path` attribute above indicates that the `TS_LinearInputControl.css` file is located in `css` subfolder relative to the current directory where the `ControlManifest.Input.xml` resides on disk.
Update the ControlManifest.Input.xml files as follows:

1. Edit the `code` entry in `ControlManifest.Input.xml` to the pre-compiled source file of your custom control (typically this is will be index.ts).
2. Edit any paths of the resources to correctly refer to the relative paths to files on disk.

## Using ES6 Module Syntax

The build tools expect the control source to be exported using standard ES6 module format. Legacy controls are typically exported as internal modules (aka namespaces). To align with the new build tools the control source must be modified as follows.

1. Open the source file that implements the custom control (e.g. index.ts).
2. Use standard ES6 export syntax by removing the module declaration

     Before:
     ```TypeScript
     module SampleNamespace
     {
    export class TSLinearInputControl implements ControlFramework.StandardControl<InputsOutputs.IInputBag, InputsOutputs.IOutputBag> {
	      <your class implementation>
	       }
            }
     
      ```
    After:
    ```TypeScript
     export class TSLinearInputControl implements ControlFramework.StandardControl<InputsOutputs.IInputBag, InputsOutputs.IOutputBag> {
	 <your class implementation>
          }
   ```

## Using Generated Manifest Typing file

Legacy projects required manually creating and editing an `inputsOutputs.d.ts` typing file. This file is typically located under `private_typing` subfolder. The new tooling now automatically generate this file upon build. Code-gen ensures that `type` definitions used in the control source code stays in-sync with `types` defined in the control manifest file.  
The typing file is renamed to `ManifestTypes.d.ts` and it is now generated into a subfolder named `generated`. In addition, the `InputsOutputs.IInputBag` and `InputsOutputs.IOutputBag` types are renamed to `IInputs` and `IOutputs` respectively.
To use the new typing file:

1.	Import the new `ManifestTypes.d.ts` file by adding the following line at the top of the control source file:
import { IInputs, IOutputs } from `./generated/ManifestTypes`.
2.	Rename all references of **InputsOutputs.IInputBag** to **IInputs**.
3.	Rename all references of **InputsOutputs.IOutputBag** to IOutputs**.
4.	Build the project to generate a new **ManifestTypes.d.ts** file using the command `npm run build`.

### See also

[Implementing controls using TypeScript](implementing-controls-using-typescript.md)<br />
[Import controls](import-custom-controls.md)<br />
[Debug controls](debugging-custom-controls.md)
