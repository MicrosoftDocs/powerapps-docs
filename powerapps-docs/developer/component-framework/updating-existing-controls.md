---
title: Update existing custom components using PowerApps component framework Tooling| Microsoft Docs
description: Update components using the PowerApps component framework Tooling
keywords: PowerApps component framework, Custom component, component Framework
ms.author: nabuthuk
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d2cbf58a-9112-45c2-b823-2c07a310714c
---
# Updating existing custom components 

[!INCLUDE[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

If you are a PowerApps component framework Private Preview participant and have already built custom components, you will need to make some minor updates to make it compatible with the new ALM-centric project structures. To use the new PowerApps component framework build tools with your existing PowerApps component framework custom component source, a few changes are required.

## Creating an empty project

Use PowerApps CLI to create a new empty project for your custom component. More information [Create components using tooling](create-custom-controls-using-pcf.md).
Once the project has been created migrate your custom component source to the new project:

1. Copy or replace the component source from the old source file into **index.ts**.
2. Copy or replace the contents of **ControlManifest.xml** into **ControlManifest.Input.xml** file.
3. Copy all other peripheral component resources such as css, resx, img into the corresponding subfolder from the old project to the new project.

## Updating Manifest file

The `ControlManifest.xml` file that defines the custom component properties is been replaced with a `ControlManifest.Input.xml` file. There should otherwise be very little change in schema between the two files.
There are a couple of important semantic changes.

1. The `code` resource entry must now point to the pre-compiled source file of the custom component. The file name has been defaulted to **index.ts**.
For example, if your component source is implemented in a file called `MyControl.ts`, then the `code` entry in `ControlManifest.Input.xml` must point to that file. The `code` file must also be a valid Typescript file. This is in contrast to legacy manifest files that specified the compiled JS output file in the `code` entry.
2. The `path` attribute of the resource element like `code` or `css` now refers to the local path to the file on disk. For example,

    ```XML
   <resources>
    <css path="css/YourControlName" order="1"/>
    </resources>
    ```

The `path` attribute above indicates that the `YourControlName.css` file is located in `css` subfolder relative to the current directory where the `ControlManifest.Input.xml` resides on disk.
Update the ControlManifest.Input.xml files as follows:

1. Edit the `code` entry in `ControlManifest.Input.xml` to the pre-compiled source file of your custom component (typically this is will be index.ts).
2. Edit any paths of the resources to correctly refer to the relative paths to files on disk.

## Using ES6 Module Syntax

The build tools expect the component source to be exported using standard ES6 module format. Legacy controls are typically exported as internal modules (aka namespaces). To align with the new build tools the component source must be modified as follows.

1. Open the source file that implements the custom component (e.g. index.ts).
2. Use standard ES6 export syntax by removing the module declaration

     Before:
     ```TypeScript
     module SampleNamespace
     {
    export class TSLinearInputControl implements ComponentFramework.StandardControl<InputsOutputs.IInputBag, InputsOutputs.IOutputBag> {
	      <your class implementation>
	       }
            }
     
      ```
    After:
    ```TypeScript
     export class YourControlName implements ComponentFramework.StandardControl<IInputs, IOutputs> { 
          <your class implementation>
          }
   ```

## Using Generated Manifest Typing file

Legacy projects required manually creating and editing an `inputsOutputs.d.ts` typing file. This file is typically located under `private_typing` subfolder. The new tooling now automatically generate this file upon build. Code-gen ensures that `type` definitions used in the component source code stays in-sync with `types` defined in the component manifest file.  
The typing file is renamed to `ManifestTypes.d.ts` and it is now generated into a subfolder named `generated`. In addition, the `InputsOutputs.IInputBag` and `InputsOutputs.IOutputBag` types are renamed to `IInputs` and `IOutputs` respectively.
To use the new typing file:

1. Import the new `ManifestTypes.d.ts` file by adding the following line at the top of the component source file:
    import { IInputs, IOutputs } from `./generated/ManifestTypes`.
2. Rename all references of **InputsOutputs.IInputBag** to **IInputs**.
3. Rename all references of **InputsOutputs.IOutputBag** to IOutputs**.
4. Build the project to generate a new **ManifestTypes.d.ts** file using the command `npm run build`.

### See also

[Limitations of PowerApps component framework](limitations.md)<br/>
[PowerApps component framework API Reference](reference/index.md)<br/>
[PowerApps component framework Overview](overview.md)
