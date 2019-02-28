---
title: Create custom controls using PowerApps Control Framework Tooling| Microsoft Docs
description: Start creating controls using the PowerApps control Framework Tooling
keywords: PowerApps Control Framework, Custom Controls, Control Framework
ms.author: nabuthuk
manager: kvivek
ms.date: 03/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d2cbf58a-9112-45c2-b823-2c07a310714c
---

# Create Controls using PowerApps Control Framework Tooling

[!INCLUDE[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This topic shows how to create custom controls using **PowerApps CLI (Command Line Interface)**. Use the **PowerApps CLI** to create, debug and deploy custom controls. **The PowerApps CLI** will enable developers to quickly create PCF controls and in the coming months the set of capabilities will expand to include plugin development and aid the **Microsoft** recommended **Application Lifecycle Management (ALM) processes**.

**Microsoft PowerApps CLI** is a simple, single-stop developer command line interface which offers you everything that is required to create a custom control and enable you to perform all the development tasks via a simple and efficient set of commands. The **PowerApps CLI** is the first step towards a comprehensive **ALM** story where Enterprise developers and ISVs can create, build, debug and publish their extensions and customizations quickly and efficiently. The significance here is a shift towards a source centric approach, to provide better support for continuous validation starting from internal development loop through to AppSource publishing and end-customer deployment. 
 
Developers will be empowered to identify problems early and operations like adding a component to a solution, or publishing to upstream environments can be automated with simple tasks as we enable deeper integration with **Azure DevOps**.

## Prerequisites to use PowerApps CLI

To use PowerApps CLI you will need the following: 

- Install [Node.js](https://nodejs.org/en/).
- Install CLI from NuGet (path to be provided). 
- Install the PCF modules (includes typescript) from `npm` by using tge command `npm install pcf-scripts`.  
- Install Visual Studio Code (optional).  
- To deploy your custom control, you will need Common Data Service for Apps environment with System administrator or System customizer privileges.

## Creating custom controls

To get started, open a command line interface (**PowerShell**).

1. Create a new folder where desired on your local hard drive.
2. Use a single command to create a new control project with some basic parameters
 `pac pcf init --namespace <specify your namespace here> --name <put control name here> --template <control type>`
 
> [!NOTE]
>Today we offer two types of controls field and dataset.

3. To retrieve all required project dependencies, run the command `npm install`.
4. Open your project in any developer environment of your choice and get started with your custom control development.
5. Implement the custom logic for the control. More information: [Implementing custom controls using TypeScript](implementing-controls-using-typescript.md).
6. To build your control you can use **Visual Studio Code** by using the (Ctrl-Shift-B) command, then selecting your build options or you can build your control quickly using `npm run build` command.

## Telemetry

The feature team is aggregating anonymized telemetry in order to understand which features/capabilities in the **Microsoft PowerApps CLI** tool are most often used by developers. The aggregated data allows us to provide the best experience to our customers by focusing on what’s truly important.

If for any reason you would like to disable telemetry collection, run the command `pac telemetry - -enabled false`. To turn telemetry back on, use the  command `pac telemetry- -enabled true`.


> [!div class="nextstepaction"]
> [Implementing controls using TypeScript](implementing-controls-using-typescript.md)
> [Import controls](import-custom-controls.md)
> [Debug controls](debugging-custom-controls.md)
