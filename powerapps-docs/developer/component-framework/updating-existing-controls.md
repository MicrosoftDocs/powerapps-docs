---
title: Update existing code components using Power Apps component framework tooling| Microsoft Docs
description: Update components using the Power Apps component framework tooling
keywords: Power Apps component framework, code component, component Framework
ms.subservice: pcf
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d2cbf58a-9112-45c2-b823-2c07a310714c
---
# Update existing code components 

If you are a Power Apps component framework Private Preview participant for model-driven apps and have already built code components, you need to make some minor updates to make it compatible with the new ALM-centric project structures. 

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

A few changes are required to use the new Microsoft Power Platform CLI tooling with your existing Power Apps component framework code components.

> [!NOTE]
> This topic is applicable only for updating code components for model-driven apps because Microsoft Power Platform CLI tooling is not available at the time of private preview for the model-driven apps.  

## Creating an empty project

Use Microsoft Power Platform CLI to create a new empty project for your code component. More information: [Create components using tooling](create-custom-controls-using-pcf.md)

Once the project is created, migrate your code component source to the new project:

1. Copy or replace the component source file from the old source file into **index.ts**.
2. Copy or replace the contents of **ControlManifest.xml** into **ControlManifest.Input.xml** file.
3. Copy all other peripheral component resources such as CSS, RESX, or IMG into the corresponding subfolder from the old project to the new project.

## Updating manifest file

The `ControlManifest.xml` file that defines the code component properties gets replaced with the `ControlManifest.Input.xml` file. There should otherwise be very little change in schema between the two files.

But there are a couple of important semantic changes:

1. The `code` resource entry must now point to the precompiled source file of the code component. The file name defaults to **index.ts**.

   For example, if your component source is implemented in a file called `MyControl.ts`, then the `code` entry in `ControlManifest.Input.xml` must point to that file. The `code` file must also be a valid TypeScript file. This is in contrast to legacy manifest files that specified the compiled JS output file in the `code` entry.
2. The `path` parameter of the resource element like `code` or `css` now refers to the local path to the file on disk. For example:

    ```XML
   <resources>
    <css path="css/YourControlName" order="1"/>
    </resources>
    ```

The `path` parameter above indicates that the `YourControlName.css` file is located in the `css` subfolder relative to the current directory where the `ControlManifest.Input.xml` resides on disk.

Update the ControlManifest.Input.xml files as follows:

1. Edit the `code` entry in `ControlManifest.Input.xml` to the precompiled source file of your code component (typically index.ts).
2. Edit any paths of the resources to correctly refer to the relative paths to files on the disk.

## Updating the project files

If you have created a component using the older version of the tooling and want to take advantage of the latest capabilities, make sure to update your project files as shown here:

1. Update your existing projects to use the latest modules.
 
   - Update the version tag in your `pcfproj` located within your Power Apps component framework project folder as follows:

      ```XML
      <Packagereference Include="Microsoft.PowerApps.MSBuild.Pcf" Version="1.*"/>
      ```
   - Update the version tag in your `cdsproj` located within your solution project folder as follows:

      ```XML
      <Packagereference Include="Microsoft.PowerApps.MSBuild.Solution" Version="1.*"/>
      ```

      > [!NOTE] 
      > After making the above changes, run the command `msbuild /t:restore` to update your project to the correct version.


   - Update the version tag in your `package.json` file located within your Power Apps component framework project folder:

      ```JSON
      "devDependencies":{
       "pcf-scripts": "^1",
       "pcf-start": "^1"
          }
      ```
     > [!NOTE]
     > After making the above changes, run the `npm update` command to update your project to the correct version.

2. If you have previously created an auth profile, you need to recreate it. This is because a new property was added to the profile to support non-public cloud. You can do this by:
 
    - Running the command `pac auth clear`.
    - Running the command `pac auth create --url <your org url>`.

## Updating your project with the latest node modules

Legacy projects require the latest npm modules to be retrieved to take advantage of the latest CLI capabilities. To update the node modules that you previously downloaded, go to your project directory in the developer command prompt and run the command `npm update`. 

## Using ES6 module syntax

The build tools expect the component source to be exported using standard ES6 module format. Legacy components typically get exported as internal modules (also known as namespaces). The component source file must be modified as below, to align with the new build tools.

1. Open the source file that implements the code component (for example, index.ts).
2. Use standard ES6 export syntax by removing the module declaration.

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

## Using generated manifest typing file

Legacy projects require manually creating and editing an `inputsOutputs.d.ts` typing file, which is typically located under the `private_typing` subfolder. Microsoft Power Platform CLI tooling now automatically generates this file upon build. 

Code-gen ensures that `type` definitions used in the component source code stay in sync with `types` defined in the component manifest file.

The typing file is renamed to `ManifestTypes.d.ts` and it is now generated into a subfolder named `generated`. In addition, the `InputsOutputs.IInputBag` and `InputsOutputs.IOutputBag` types are renamed to `IInputs` and `IOutputs` respectively.

To use the new typing file:

1. Import the new `ManifestTypes.d.ts` file by adding the following line at the top of the component source file:

    import { IInputs, IOutputs } from `./generated/ManifestTypes`.
2. Rename all references of **InputsOutputs.IInputBag** to **IInputs**.
3. Rename all references of **InputsOutputs.IOutputBag** to **IOutputs**.
4. Build the project to generate a new **ManifestTypes.d.ts** file using the command `npm run build`.


### See also

[Limitations of Power Apps component framework](limitations.md)<br/>
[Power Apps component framework API reference](reference/index.md)<br/>
[Power Apps component framework overview](overview.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]