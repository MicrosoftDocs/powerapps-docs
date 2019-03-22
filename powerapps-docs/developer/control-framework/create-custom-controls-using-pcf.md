---
title: Create custom controls using PowerApp Component Framework Tooling| Microsoft Docs
description: Start creating controls using the PowerApps Component Framework Tooling
keywords: PowerApps Component Framework, Custom Controls, Component Framework
ms.author: nabuthuk
manager: kvivek
ms.date: 03/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d2cbf58a-9112-45c2-b823-2c07a310714c
---

# Create Controls using PowerApps Component Framework Tooling

[!INCLUDE[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This topic shows how to create custom controls using **PowerApps CLI (Command Line Interface)**. Use the PowerApps CLI to create, debug and deploy custom controls. The PowerApps CLI will enable developers to quickly create PCF controls and in the coming months the set of capabilities will expand to include plugin development and aid the Microsoft recommended Application Lifecycle Management (ALM) processes.

Microsoft PowerApps CLI is a simple, single-stop developer command line interface which offers you everything that is required to create a custom control and enable you to perform all the development tasks via a simple and efficient set of commands. The PowerApps CLI is the first step towards a comprehensive **ALM** story where enterprise developers and ISVs can create, build, debug and publish their extensions and customizations quickly and efficiently. The significance here is a shift towards a source centric approach, to provide better support for continuous validation starting from internal development loop through to AppSource publishing and end-customer deployment.
 
Developers will be empowered to identify problems early and operations like adding a component to a solution, or publishing to upstream environments can be automated with simple tasks as we enable deeper integration with Azure DevOps.

## Prerequisites to use PowerApps CLI

To use PowerApps CLI you will need the following:

- Install [Node.js](https://nodejs.org/en/).
- If you don’t have Visual Studio 2017 or later, follow one of the options below:
   - Option 1: Install Visual Studio 2017 or later
   - Option 2: Install .NET Core 2.2 SDK and install Visual Studio Code
- Install Microsoft CLI using the steps below
    1. Create a directory on your machine, called something like `c:\pac` 
    2. Open the command line interface and navigate to the directory that you created above `Cd c:\pac` 
    3. Run the below command
 `powershell -ExecutionPolicy Bypass -Command "Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://powerappsclipreview.blob.core.windows.net/install/InstallAndConfigureCLI.ps1'))"`  
- To deploy your custom control, you will need Common Data Service environment with System administrator or System customizer privileges.

## Creating custom controls

To get started, open a command line interface (PowerShell).

1. Make sure that you restart your command line interface after installing **PowerApps CLI**. 
2. Create a new folder where desired on your local hard drive for example, `C:\Users\<your name>\Documents\My_PCF_Control`.
3. Use a single command to create a new control project with some basic parameters
 `pac pcf init --namespace <specify your namespace here> --name <put control name here> --template <control type>`
 
> [!NOTE]
>Today we offer two types of controls field and dataset.

4. To retrieve all the required project dependencies, run the command `npm install`.
5. Open your project in any developer environment of your choice and get started with your custom control development.
6. Implement the custom logic for the control. More information: [Implementing custom controls using TypeScript](implementing-controls-using-typescript.md).
7. To build your control you can use **Visual Studio Code** by using the (Ctrl-Shift-B) command, and selecting your build options or you can build your control quickly using `npm run build` command.

## Telemetry

The feature team is aggregating anonymized telemetry in order to understand which features or capabilities in the PowerApps CLI tool are most often used by the developers. The aggregated data allows to provide the best experience to the customers by focusing on what’s truly is important.

If you would like to disable the telemetry collection, run the command `pac telemetry - -enabled false`. To turn the telemetry back, use the command `pac telemetry- -enabled true`.

> [!div class="nextstepaction"]
> [Implementing controls using TypeScript](implementing-controls-using-typescript.md)<br />
> [Import controls](import-custom-controls.md)<br />
> [Debug controls](debugging-custom-controls.md)
