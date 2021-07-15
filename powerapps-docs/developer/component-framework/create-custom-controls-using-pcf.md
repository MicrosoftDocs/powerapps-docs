---
title: Create and build a code component in Microsoft Dataverse| Microsoft Docs
description: Start creating a component using the Power Apps component framework tooling.
keywords: Power Apps component framework, code components, Component Framework
ms.subservice: pcf
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

This article demonstrates how to create and deploy code components using Microsoft Power Platform CLI. Ensure that you have installed [Microsoft Power Platform CLI](https://aka.ms/PowerAppsCLI).

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

## Create a new component

To begin, open **Developer Command Prompt for VS 2017 or higher** after installing Microsoft Power Platform CLI.

1. In the Developer Command Prompt, create a new folder on your local machine, for example, *C:\Users\your name\Documents\My_code_Component* using the command `mkdir <Specify the folder name>`.
2. Go to the newly created folder using the command `cd <specify your new folder path>`.
3. Create a new component project by passing some basic parameters using the command:

    ```CLI
    pac pcf init --namespace <specify your namespace here> --name <Name of the code component> --template <component type>
    ```
4. To retrieve all the required project dependencies, run the command `npm install`.
5. Open your project folder `C:\Users\<your name>\Documents\<My_code_Component>` in any developer environment of your choice and get started with your code component development. The quickest way to get started is by running `code .` from your command prompt once you are in the `C:\Users\<your name>\Documents\<My_code_Component>` directory. This command opens your component project in Visual Studio Code.
6. Implement the required artifacts for the component like manifest, component logic, and styling and then build the component project. More information: [Create your first code component](implementing-controls-using-typescript.md)

## Build your component

To build the component project, open the project folder that contains `package.json` in Visual Studio Code and use the (Ctrl-Shift-B) command, then select the build options. 

Alternatively, you can build the component quickly using the `npm run build` command in the Developer Command Prompt for VS 2017 window.

> [!TIP]
> To debug the component during or after the build operation, see [Debug a code component](debugging-custom-controls.md).

Finally when you're done implementing the component logic in TypeScript, you need to bundle all the code component elements into a solution file so that you can import the solution into Microsoft Dataverse. More information: [Package a code component](import-custom-controls.md)

### See also

[Debug code components](debugging-custom-controls.md)<br/>
[Package a code component](import-custom-controls.md)<br/>
[Add code components to a column or table](add-custom-controls-to-a-field-or-entity.md)<br/>
[Updating existing code components](updating-existing-controls.md)<br/>
[Power Apps component framework API reference](reference/index.md)<br/>
[Power Apps component framework overview](overview.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]