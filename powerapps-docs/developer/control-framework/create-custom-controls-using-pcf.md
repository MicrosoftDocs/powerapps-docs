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

# Create Controls using PowerApps Component Framework tooling

This topic shows how to create custom controls using the **PowerApps CLI (Command Line Interface)**. Use the PowerApps CLI to create, debug and deploy custom controls. The PowerApps CLI will enable developers to quickly create PCF controls and in the coming months the set of capabilities will expand to include plugin development and aid the Microsoft recommended Application Lifecycle Management (ALM) processes.

Microsoft PowerApps CLI is a simple, single-stop developer command line interface which offers you everything that is required to create a custom control and enable you to perform all the development tasks via a simple and efficient set of commands. The PowerApps CLI is the first step towards a comprehensive **ALM** story where enterprise developers and ISVs can create, build, debug and publish their extensions and customizations quickly and efficiently. The significance here is a shift towards a source centric approach, to provide better support for continuous validation starting from internal development loop through to AppSource publishing and end-customer deployment.
 
Developers will be empowered to identify problems early and operations like adding a component to a solution, or publishing to upstream environments can be automated with simple tasks as we enable deeper integration with Azure DevOps.

## Prerequisites to use PowerApps CLI

To use PowerApps CLI you will need the following:

- Install [Node.js](https://nodejs.org/en/).
- If you don’t have Visual Studio 2017 or later, follow one of the options below:
   - Option 1: Install Visual Studio 2017 or later
   - Option 2: Install .NET Core 2.2 SDK and install Visual Studio Code
- Install Microsoft CLI using the steps below:
    1. Create a directory on your machine, called something like `c:\pac` 
    2. Open the command line interface as `adminitrator` and navigate to the directory that you created above `Cd c:\pac` 
    3. Run the below command
 `powershell Invoke-Command -ScriptBlock ([scriptblock]::Create(((New-Object System.Net.WebClient).DownloadString('https://powerappsclipreview.blob.core.windows.net/install/InstallAndConfigureCLI.ps1')))) -ArgumentList "stable"`   
- To deploy your custom control, you will need Common Data Service environment with System administrator or System customizer privileges.

> [!NOTE]
> PowerApps Component Framework is only supported in new  unified interface and only for online deployment types.

> Currently PowerApps CLI is supported only on Windows 10.

## Creating custom controls

To get started, open command prompt for vs 2017 after installing PowerApps CLI.

1. In the developer command prompt for vs 2017, create a new folder on your local hard drive for example, `C:\Users\<your name>\Documents\My_PCF_Control`.
2. Go to the newly created folder using the command `cd <specify your new folder path>`.
3. Run the following command to create a new control project by passing some basic parameters
 `pac pcf init --namespace <specify your namespace here> --name <put control name here> --template <control type>`
 
   > [!NOTE]
   >Today we offer two types of controls field and dataset.

4. To retrieve all the required project dependencies, run the command `npm install`.
5. Open your project in any developer environment of your choice and get started with your custom control development.
6. Implement the custom logic for the control. More information: [Implementing custom controls using TypeScript](implementing-controls-using-typescript.md).

## Building your controls

To build your control you can open the folder in Visual Studio Code and use the (Ctrl-Shift-B) command, and select your build options or you can build your control quickly using  `npm run build` command.

## Debugging Custom Controls

Once you are done implementing your custom control logic, run the following command to start the debugging process
`npm start`

> [!NOTE]
> Today you can only visualize your field control, but dataset support is coming soon.

> [!div class="mx-imgBorder"]
> ![local-host](media/local-host.png "local host")

As show in the image above, the browse window will open with 3 sections. Your control will be rendered in the left pane while the right pane consists of **Inputs** and **Outputs** sections

  - **Inputs** section is an interactive UI that displays all properties and their types/type-groups defined in the manifest.xml. It allows you to key in mock data for each property. 
  - **Outputs** section renders the output whenever a control's `getOutputs` method gets called.  
 
> [!NOTE]
> If you want to modify the `manifest.xml` or create additional properties, you will need to restart the debug process before they appear in the inputs section.

As you are inputting mock data, you can use the browser’s debugging capabilities to observe the control behavior. Each browser provides you with a debugging tool to help you debug your code natively in the browser. Typically, you can activate debugging in your browser by pressing the **F12** key to display the native developer tool used for debugging.

For example, on **Microsoft Edge**,

- Press **F12** to open inspector.
- Click on your control
- On top bar, go to **Debugger**, and then start searching for the control name described in the Manifest file in the search bar. For example, type your control name like `Hello World Control`.

     > [!div class="mx-imgBorder"]
     > ![debug-control](media/debug-control.png "Debug control")

> [!NOTE]
> It is always a good practice to set breakpoints on the control's life cycle methods like `init` and `updateView`

You can also interact with the control locally in real time and observe elements in the DOM by setting a breakpoint in the sources tab as follows

> [!div class="mx-imgBorder"]
> ![local-host](media/local-host.png "local host")

> [!div class="mx-imgBorder"]
> ![debug-control](media/debug-control-1.png "Debug control 1")

## Fiddler AutoResponder

Use the Fiddler AutoResponder to quickly debug your custom controls. Install [Fiddler](https://www.telerik.com/download/fiddler) and follow the steps to configure [AutoResponder](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/streamline-javascript-development-fiddler-autoresponder)

## Deploying controls into Common Data Service

This topic demonstrates how to import custom controls into Common Data Service. After developing custom controls using the PowerApps CLI, next step is to import those controls, so that you can see the controls in runtime.

Follow the steps below to create and import a solution file:

1. Create a new solution project in the directory of your choice by using the command `pac solution init --publisherName <enter your publisher name> --customizationPrefix <enter your publisher name>` after `cd <your new folder>`.

   > [!NOTE]
   > The `publisherName` and `cutomizationPrefix` values must be unique to your environment.
 
2. Once the new solution project is created, you need to refer to the location where the created control is located. You can add the reference by using the command
`pac solution add-reference --<path of your pcf project on disk>`
3. To generate a zip file from your solution project, you will need to `cd` into your solution project directory and build the project using the command `msbuild/t:restore` and `msbuild`

    > [!NOTE]
    > If msbuild 15 is not in the path, open Developer Command Prompt for Vs 2017 to run the msbuild commands.

    > [!NOTE]
    > Building the solution in the debug configuration, generates an unmanaged solution package. A managed solution package is generated by building the solution in release configuration. These settings can be overridden by specifying SolutionPackageType property in cdsproj file.

4. The generated solution files are located in `\bin\debug\`.
5. You should manually import the solution using the web portal.

## Telemetry

The feature team is aggregating anonymized telemetry in order to understand which features or capabilities in the PowerApps CLI tool are most often used by the developers. The aggregated data allows to provide the best experience to the customers by focusing on what’s truly is important.

To disable the telemetry collection, run the command `pac telemetry - -enabled false`. To turn the telemetry back, use the command `pac telemetry- -enabled true`.

### See also

[Add Controls to entities or fields](add-custom-controls-to-a-field-or-entity.md)
