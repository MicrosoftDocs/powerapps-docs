---
title: Package a Code Component in a Solution File
description: Learn how to package a code component in a solution file, import it into Microsoft Dataverse, and deploy updates with Microsoft Power Platform CLI.
author: anuitz
ms.author: anuitz
ms.date: 08/25/2026
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: pcf
contributors:
 - JimDaly
---

# Package a code component

Learn how to package a code component in a solution file and import it into Microsoft Dataverse so it's available at runtime. You also learn how to connect to an environment, deploy updates with Microsoft Power Platform CLI, and remove components from a solution.

## Process

To create and import a solution file:

1. Create a new folder inside the sample component folder and name it **Solutions** (or any name you choose) by using the command `mkdir Solutions`. Navigate into the directory by using the command `cd Solutions`.

1. Create a new solutions project by using the [pac solution init](/power-platform/developer/cli/reference/solution) command. Use the solution project for bundling the code component into a solution ZIP file that you import into Dataverse.
   
   ```CLI
   pac solution init --publisher-name developer --publisher-prefix dev
   ```

   > [!NOTE]
   > The `publisher-name` and `publisher-prefix` values must be unique to your environment.
 
1. After you create the new solution project, set the **Solutions** folder as the location for the created sample component. Add the reference by using the [pac solution add-reference](/power-platform/developer/cli/reference/solution) command. This reference informs the solution project about which code components to add during the build. You can add references to multiple components in a single solution project.

   ```CLI   
    pac solution add-reference --path c:\downloads\mysamplecomponent
   ```

1. To generate a ZIP file from the solution project, go into your solution project directory and build the project by using the following command. This command uses *MSBuild* to build the solution project by pulling down the *NuGet* dependencies as part of the restore. Use the `/restore` flag only the first time you build the solution project. For every build after that, run the command `msbuild`.

   ```CLI
   msbuild /t:restore
   ```
   ```CLI
   msbuild
   ```

   Or if you have installed the .NET SDK, version 6 or later:

   ```CLI
   dotnet build
   ```


    > [!TIP]
    > - If msbuild 15.9.* isn't in the path, open Developer Command Prompt for VS 2017 to run the `msbuild` commands.
    > - Building the solution in the *debug* configuration generates an unmanaged solution package. Building the solution in *release* configuration generates a managed solution package. You can override these settings by specifying the `SolutionPackageType` property in the `cdsproj` file.
    > - Set the msbuild configuration to `Release` to issue a production build. Example: `msbuild /p:configuration=Release`
    > - If you encounter an error that says *Ambiguous project name* when running the `msbuild` command on your solution, ensure that your solution name and project name aren't the same.

1. After the build succeeds, find the generated solution files inside the `\bin\debug\` folder.
1. [Import the solution into Dataverse](../../maker/data-platform/import-update-export-solutions.md) manually by using the web portal or automatically by using the [Microsoft Power Platform Build Tools](https://marketplace.visualstudio.com/items?itemName=microsoft-IsvExpTools.PowerPlatform-BuildTools).

## Connect to your environment

You can deploy the code components directly from Microsoft Power Platform CLI by connecting to the Dataverse environment and then pushing the updated components.

Follow the steps in the following list to create the authentication profile, connect to Dataverse, and push the updated components. 
 
1. Create your authentication profile by using the [pac auth create](/power-platform/developer/cli/reference/auth) command. 
 
    ```CLI
    pac auth create --url https://xyz.crm.dynamics.com 
    ```
 
1. If you previously created an authentication profile, view all existing profiles by using the [pac auth list](/power-platform/developer/cli/reference/auth) command. 

   ```CLI
    pac auth list 
   ```
 
1. Switch between previously created authentication profiles by using the [pac auth select](/power-platform/developer/cli/reference/auth) command. 
   
   ```CLI
    pac auth select --index <index of the active profile>
    ``` 

1. Get basic information about the environment by using the [pac org who](/power-platform/developer/cli/reference/org) command. The connection uses the default authentication profile. 

    ```CLI
    pac org who 
    ```
 
1. Delete a particular authentication profile by using the [pac auth delete](/power-platform/developer/cli/reference/auth) command with the `pac auth delete --index <index of the profile>` syntax. 
1. Clear all authentication profiles from your local machine by using the [pac auth clear](/power-platform/developer/cli/reference/auth) command. This action is irreversible because it completely deletes the `authprofile.json` file and token cache file from your local machine. 

## Deploy code components

After you create an authentication profile, start pushing the code components to the Dataverse instance with all the latest changes. 

The `push` capability speeds up the inner-developer cycle development because it bypasses the code component versioning requirements and doesn't require that you build your solution (cdsproj) to import the code component. 

To use the `push` capability, follow these steps:

1. Ensure that you have a valid authentication profile.
1. Go to the directory where the sample component file is located.
1. Run the [pac pcf push](/power-platform/developer/cli/reference/pcf) command.

   ```CLI
   pac pcf push --publisher-prefix <your publisher prefix>
   ```

   > [!NOTE]
   > The publisher prefix that you use with the `push` command should match the publisher prefix of your solution where you include the components.

## Remove components from a solution

If you want to remove a code component from a solution file:

1. Edit the `cdsproj` file in the solution project directory and remove the references to the component. Here's an example of a component reference:

   ```XML
   <ItemGroup>
       <Projectreference Include="..\pcf_component\pcf_component.pcfproj">
         <Project>0481bd83-ffb0-4b70-b526-e0b3dd63e7ef</Project>
         <Name>pcf_component</Name>
         <Targets>Build</Targets>
         <referenceOutputAssembly>false</referenceOutputAssembly>
         <OutputItemType>Content</OutputItemType>
         <CopyToOutputDirectory>Always</CopyToOutputDirectory>
       </Projectreference>
   </ItemGroup>
   ```

1. Perform a rebuild (or clean) by using the following command:
   
    ```CLI
    msbuild /t:rebuild
    ```

### See also

[Add code components to a column or table in model-driven apps](add-custom-controls-to-a-field-or-entity.md)<br/>
[Add components to a canvas app](component-framework-for-canvas-apps.md#add-components-to-a-canvas-app)<br/>
[Power Apps component framework API reference](reference/index.md)<br/>
[Power Apps component framework overview](overview.md)<br />
[Microsoft Power Platform CLI Command Groups](/power-platform/developer/cli/reference/)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
