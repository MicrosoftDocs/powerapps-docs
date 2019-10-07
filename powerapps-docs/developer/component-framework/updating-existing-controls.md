---
title: Update existing code components using PowerApps component framework tooling| Microsoft Docs
description: Update components using the PowerApps component framework tooling
keywords: PowerApps component framework, code component, component Framework
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

If you are a PowerApps component framework Private Preview participant for model-driven apps and have already built code components, you need to make some minor updates to make it compatible with the new ALM-centric project structures. 

A few changes are required to use the new PowerApps CLI tooling with your existing PowerApps component framework code components.

> [!NOTE]
> This topic is applicable only for updating code components for model-driven apps because the PowerApps CLI tooling is not available at the time of private preview for the model-driven apps.  

## Creating an empty project

Use PowerApps CLI to create a new empty project for your code component. More information: [Create components using tooling](create-custom-controls-using-pcf.md)

Once the project is created, migrate your code component source to the new project:

1. Copy or replace the component source file from the old source file into **index.ts**.
2. Copy or replace the contents of **ControlManifest.xml** into **ControlManifest.Input.xml** file.
3. Copy all other peripheral component resources such as CSS, RESX, or IMG into the corresponding subfolder from the old project to the new project.

## Updating manifest file

The `ControlManifest.xml` file that defines the code component properties gets replaced with the `ControlManifest.Input.xml` file. There should otherwise be very little change in schema between the two files.

But there are a couple of important semantic changes:

1. The `code` resource entry must now point to the precompiled source file of the code component. The file name defaults to **index.ts**.

   For example, if your component source is implemented in a file called `MyControl.ts`, then the `code` entry in `ControlManifest.Input.xml` must point to that file. The `code` file must also be a valid TypeScript file. This is in contrast to legacy manifest files that specified the compiled JS output file in the `code` entry.
2. The `path` attribute of the resource element like `code` or `css` now refers to the local path to the file on disk. For example:

    ```XML
   <resources>
    <css path="css/YourControlName" order="1"/>
    </resources>
    ```

The `path` attribute above indicates that the `YourControlName.css` file is located in the `css` subfolder relative to the current directory where the `ControlManifest.Input.xml` resides on disk.

Update the ControlManifest.Input.xml files as follows:

1. Edit the `code` entry in `ControlManifest.Input.xml` to the precompiled source file of your code component (typically index.ts).
2. Edit any paths of the resources to correctly refer to the relative paths to files on the disk.

## Updating the project files

If you have created a component using the older version of the tooling and want to take advantage of the latest capabilities, make sure to update your project files as shown here:

1. Update your existing projects to use the latest modules.
 
   - Update the version tag in your `pcfproj` located within your PowerApps component framework project folder as follows:

      ```XML
      <PackageReference Include="Microsoft.PowerApps.MSBuild.Pcf" Version="1.*"/>
      ```
   - Update the version tag in your `cdsproj` located within your solution project folder as follows:

      ```XML
      <PackageReference Include="Microsoft.PowerApps.MSBuild.Solution" Version="1.*"/>
      ```

      > [!NOTE] 
      > After making the above changes, run the command `msbuild /t:restore` to update your project to the correct version.


   - Update the version tag in your `package.json` file located within your PowerApps component framework project folder:

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


<!--from editor: Is the file located "under" or "in" the subfolder? -->


Legacy projects require manually creating and editing an `inputsOutputs.d.ts` typing file, which is typically located under the `private_typing` subfolder. The PowerApps CLI tooling now automatically generates this file upon build. 

Code-gen ensures that `type` definitions used in the component source code stay in sync with `types` defined in the component manifest file.

The typing file is renamed to `ManifestTypes.d.ts` and it is now generated into a subfolder named `generated`. In addition, the `InputsOutputs.IInputBag` and `InputsOutputs.IOutputBag` types are renamed to `IInputs` and `IOutputs` respectively.

To use the new typing file:

1. Import the new `ManifestTypes.d.ts` file by adding the following line at the top of the component source file:

    import { IInputs, IOutputs } from `./generated/ManifestTypes`.
2. Rename all references of **InputsOutputs.IInputBag** to **IInputs**.
3. Rename all references of **InputsOutputs.IOutputBag** to **IOutputs**.
4. Build the project to generate a new **ManifestTypes.d.ts** file using the command `npm run build`.

## Troubleshooting and workarounds

1. If you get a 1ES notification asking how pcf-scripts are being used, note that these scripts are only used to build the code components but they are not bundled or used by the resulting component.  
2. If you have previously created a code component using the tooling version 0.1.817.1 or earlier and want to ensure that the latest build and debug modules are being used, make updates to the package.json as shown:
   
    ```JSON
     "dependencies": { "@types/node": "^10.12.18", "@types/powerapps-component-framework": "1.1.0"}, "devDependencies": { "pcf-scripts": "~0", "pcf-start": "~0" } 
    ```
3. The user gets the error `Failed to retrieve information about Microsoft.PowerApps.MSBuild.Pcf from remote s​ource <Feed Url>` when the build fails for authorization issues. Here is the workaround for this:

   - Open the NuGet.Config file from **%APPDATA%\NuGet**. The feed from which the user is getting the error should be present in this file. 
   - Remove the feed from the NuGet.Config file or generate a PAT token and add it to the Nuget.Config file. For example:


<!--from editor: Something below isn't indented right. On the live page, there's no code after User PAT. And the final three backticks are visible. -->


     ```XML
     <?xml version="1.0" encoding="utf-8"?>  
     <configuration>  
     <packageSources>  
         <add key="CRMSharedFeed" value="https://dynamicscrm.pkgs.visualstudio.com/_packaging/CRMSharedFeed/nuget/v3/index.json" />  
      </packageSources>  
     <packageSourceCredentials>  
      <CRMSharedFeed>  
      <add key="Username" value="anything" />  
      <add key="Password" value="User PAT" />  
    </CRMSharedFeed>  
     </packageSourceCredentials>  
   </configuration>
     ```

### See also

[Limitations of PowerApps component framework](limitations.md)<br/>
[PowerApps component framework API reference](reference/index.md)<br/>
[PowerApps component framework overview](overview.md)
