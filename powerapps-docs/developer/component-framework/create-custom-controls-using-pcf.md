---
title: Create and build a custom component| Microsoft Docs
description: Start creating a component using the PowerApps component framework Tooling
keywords: PowerApps component framework, Custom components, Component Framework
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

# Create and build a custom component

[!INCLUDE[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This topic demonstrates how to create and deploy custom components using PowerApps component framework. Ensure that you have installed Microsoft PowerApps CLI

## Create a new component

To get started, open a new Developer Command Prompt for VS 2017 after installing PowerApps CLI.

1. In the Developer Command Prompt for VS 2017, create a new folder on your local hard drive for example, *C:\Users\your name\Documents\My_PCF_Componet*
2. Go to the newly created folder using the command `cd <specify your new folder path>`
3. Run the command to create a new component project by passing some basic parameters:

    `pac pcf init --namespace <specify your namespace here> --name <put component name here> --template <component type>`
 
   > [!NOTE]
   > Currently, PowerApps CLI supports two types of components: **field** and **dataset**.  For canvas apps, only field type is supported for experimental preview.

4. To retrieve all the required project dependencies, run the command `npm install`.
5. Open your project folder (`C:\Users\<your name>\Documents\My_PCF_Component\<component name>`) in any developer environment of your choice and get started with your custom component development.

## Build your component

To build the component project, open the project folder in Visual Studio Code and use the (Ctrl-Shift-B) command, then select the build options. Alternatively, you can also build the component quickly using the `npm run build` command in the Developer Command Prompt for VS 2017 window.

> [!TIP]
> To debug the component during or after the build operation, see [Debug a custom component](debugging-custom-controls.md).

## Known Configuration issues and Workarounds

**Msbuild error MSB4036:**

1. The name of the task in the project file is the same as the name of the task class.
2. The task class is public and implements the Microsoft.Build.Framework.ITask interface.
3. The task is correctly declared with \<UsingTask> in the project file or in the *.tasks files located in the path directory.

**Resolution:**

1. Open Visual Studio Installer. 
1. For VS 2017, select **Modify**. 
1. Click on Individual Components.
1. Under Code Tools, check **NuGet targets & Build Tasks**.

### See also

[Debug custom components](debugging-custom-controls.md)<br/>
[Package a custom component](import-custom-controls.md)<br/>
[Add custom components to a field or entity](add-custom-controls-to-a-field-or-entity.md)<br/>
[Updating existing custom components](updating-existing-controls.md)<br/>
[PowerApps component framework API Reference](reference/index.md)<br/>
[PowerApps component framework Overview](overview.md)
