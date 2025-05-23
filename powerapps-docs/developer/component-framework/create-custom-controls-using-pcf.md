---
title: Create and build a code component| Microsoft Docs
description: Start creating a component using the Power Apps component framework tooling.
keywords: Power Apps component framework, code components, Component Framework
author: anuitz
ms.author: anuitz
ms.date: 01/27/2023
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: pcf
contributors:
 - JimDaly
 - kaushikkaul
---

# Create and build a code component

This article demonstrates how to create and deploy code components using Microsoft Power Platform CLI.

## Prerequisites

You need install the following components:

1. [Visual Studio Code (VSCode)](https://code.visualstudio.com/Download) (Ensure the Add to PATH option is select)
1. [node.js](https://nodejs.org/en/download/) (LTS version is recommended)
1. [Microsoft Power Platform CLI](/powerapps/developer/data-platform/powerapps-cli#install-power-apps-cli) (Use the Visual Studio Code extension)

## Create a new component

Open Visual Studio code and open a new terminal window by selecting **Terminal** > **New Terminal**.
1. In the terminal window, create a new folder on your local machine, for example, *C:\projects\My_code_Component* using the command `mkdir <Specify the folder name>`.
1. Go to the newly created folder using the command `cd <specify your new folder path>`.
1. Create a new component project by passing some basic parameters using the [pac pcf init](/power-platform/developer/cli/reference/pcf#pac-pcf-init) command:

    ```CLI
    pac pcf init --namespace <specify your namespace here> --name <Name of the code component> --template <component type> --run-npm-install
    ```
1. The above command will also run `npm install` command for you to retrieve all the required project dependencies.
1. Open your project folder `C:\projects\My_code_Component` in any developer environment of your choice and get started with your code component development. The quickest way to get started is by running `code .` from your command prompt once you are in the `C:\projects\My_code_Component` directory. This command opens your component project in Visual Studio Code.
1. Implement the required artifacts for the component like manifest, component logic, and styling and then build the component project. More information: [Create your first code component](implementing-controls-using-typescript.md)

## Build your component

To build the component project, open the project folder that contains `package.json` in Visual Studio Code and use the (Ctrl-Shift-B) command, then select the build options.

Alternatively, you can build the component quickly using the `npm run build` command in the Visual Studio Code terminal window for development purposes, or use `npm run build -- --buildMode production` for building a release version.

> [!TIP]
> To debug the component during or after the build operation, see [Debug a code component](debugging-custom-controls.md).

Finally when you're done implementing the component logic in TypeScript, you need to bundle all the code component elements into a solution file so that you can import the solution into Microsoft Dataverse. More information: [Package a code component](import-custom-controls.md)

### See also

[Debug code components](debugging-custom-controls.md)<br/>
[Package a code component](import-custom-controls.md)<br/>
[Add code components to a column or table](add-custom-controls-to-a-field-or-entity.md)<br/>
[Power Apps component framework API reference](reference/index.md)<br/>
[Power Apps component framework overview](overview.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
