---
title: Create and build a code component| Microsoft Docs
description: Start creating a component using the Power Apps component framework tooling
keywords: Power Apps component framework, code components, Component Framework
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 06/20/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d2cbf58a-9112-45c2-b823-2c07a310714c
---

# Create and build a code component

This topic demonstrates how to create and deploy code components using Power Apps CLI. Ensure that you have installed [Microsoft Power Apps CLI](https://aka.ms/PowerAppsCLI).

## Create a new component

To begin, open **Developer Command Prompt for VS 2017** after installing Power Apps CLI.

1. In the Developer Command Prompt for VS 2017, create a new folder on your local machine, for example, *C:\Users\your name\Documents\My_code_Component* using the command `mkdir <Specify the folder name>`.
2. Go to the newly created folder using the command `cd <specify your new folder path>`.
3. Create a new component project by passing some basic parameters using the command:

    `pac pcf init --namespace <specify your namespace here> --name <Name of the code component> --template <component type>`
 
   > [!NOTE]
   > Currently, Power Apps CLI supports two types of components: **field** and **dataset** for model-driven apps.  For canvas apps, only the **field** type is supported for this experimental preview.

4. To retrieve all the required project dependencies, run the command `npm install`.
5. Open your project folder `C:\Users\<your name>\Documents\<My_code_Component>` in any developer environment of your choice and get started with your code component development. The quickest way to get started is by running `code .` from your command prompt once you are in the `C:\Users\<your name>\Documents\<My_code_Component>` directory. This command opens your component project in Visual Studio Code.
6. Implement the required artifacts for the component like manifest, component logic and styling and then build the component project. More information: [Implementing sample component](implementing-controls-using-typescript.md)

## Build your component

To build the component project, open the project folder that contains `package.json` in Visual Studio Code and use the (Ctrl-Shift-B) command, then select the build options. Alternatively, you can build the component quickly using the `npm run build` command in the Developer Command Prompt for VS 2017 window.

> [!TIP]
> To debug the component during or after the build operation, see [Debug a code component](debugging-custom-controls.md).

Once you're done implementing the component logic in TypeScript, you need to bundle all the code component elements into a solution file so that you can import the solution into Common Data Service. More information: [Package a code component](import-custom-controls.md)

## Known configuration issues and workarounds

**Msbuild error MSB4036:**

1. The name of the task in the project file is the same as the name of the task class.
2. The task class is public and implements the Microsoft.Build.Framework.ITask interface.
3. The task is correctly declared with *\<UsingTask>* in the project file or in the *.tasks files located in the path directory.

**Resolution:**

1. Open Visual Studio Installer. 
1. For Visual Studio 2017, select **Modify**. 
1. Select **Individual Components**.
1. Under Code Tools, check **NuGet targets & Build Tasks**.

**Publisher Prefix**

If a component is created using a Power Apps CLI tooling version lower than 0.4.3,  you will hit an error while trying to re-import the solution file into Common Data Service. The error is thrown because the newly imported component name is now being appended with the publisher prefix to ensure its uniqueness and to avoid collisions.

**Workaround**:

- Delete the solution containing the relevant component from Common Data Service. If the component is already configured on a form or grid, it needs to be removed there first because the component solution had a dependency on the configuration.  
- Import the new solution with updates to the component built by the latest CLI version.
- Newly imported components can now be configured on forms or grids.  


<!--2. When the components are created with the publisher prefix in mixed or upper case using the new CLI tooling version, it throws an error while importing the solution. This happens because the updated tooling version (0.4.3 and newer) now enforces the platform standard for lower case publisher prefix.

   **Workaround**:

    Update the solution and customizations to ensure that the associated prefix is modified to lower case and import the new solution into Common Data Service.-->


### See also

[Debug code components](debugging-custom-controls.md)<br/>
[Package a code component](import-custom-controls.md)<br/>
[Add code components to a field or entity](add-custom-controls-to-a-field-or-entity.md)<br/>
[Updating existing code components](updating-existing-controls.md)<br/>
[Power Apps component framework API reference](reference/index.md)<br/>
[Power Apps component framework overview](overview.md)
