---
title: Get tooling for Power Apps component framework | Microsoft Docs
description: "Get the Microsoft Power Apps CLI to create, debug, and deploy code components using Power Apps component framework."
keywords: Power Apps component framework, code components, Component Framework
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: f393f227-7a88-4f25-9036-780b3bf14070
---

# Get tooling for Power Apps component framework

Use **Microsoft Power Apps CLI** (command-line interface) to create, debug, and deploy code components using Power Apps component framework. Power Apps CLI enables developers to create code components quickly. In the future it will be expanded to include support for additional development and application lifecycle management (ALM) experiences. 

## What is Microsoft Power Apps CLI 

Microsoft Power Apps CLI is a simple, single-stop developer command-line interface that empowers the developers and app makers to create code components. Power Apps CLI tooling is the first step toward a comprehensive ALM story where the enterprise developers and ISVs can create, build, debug, and publish their extensions and customizations quickly and efficiently.  

## Install Microsoft Power Apps CLI

To get Microsoft Power Apps CLI, do the following:

1. Install [Npm](https://www.npmjs.com/get-npm) (comes with Node.js) or [Node.js](https://nodejs.org/en/) (comes with npm). We recommend LTS (Long Term Support) version 10.15.3 or higher.

1. Install [.NET Framework 4.6.2 Developer Pack](https://dotnet.microsoft.com/download/dotnet-framework/net462). 

1. If you don’t already have Visual Studio 2017 or later, follow one of these options:
   - Option 1: Install [Visual Studio 2017](https://docs.microsoft.com/visualstudio/install/install-visual-studio?view=vs-2017) or later.
   - Option 2: Install [.NET Core 2.2 SDK](https://dotnet.microsoft.com/download/dotnet-core/2.2) and then install [Visual Studio Code](https://code.visualstudio.com/Download).

1. Install [Microsoft Power Apps CLI](https://aka.ms/PowerAppsCLI).
1. To take advantage of all the latest capabilities, update the Power Apps CLI tooling to the latest version using this command:

    ```CLI
    pac install latest
    ```

> [!NOTE]
> - To deploy your code component using Power Apps CLI, you must have a Common Data Service environment with system administrator or system customizer privileges.
> - Currently, Power Apps CLI is supported only on Windows 10.

## Microsoft Power Apps CLI telemetry

The feature team is aggregating the telemetry to understand what features or capabilities developers most often use in the Power Apps CLI tool. The aggregated data allows us to provide the best experience to the customers by focusing on what is essential.

> [!NOTE]
> To disable the telemetry collection, run the command `pac telemetry disable`. To turn the telemetry back, use the command `pac telemetry enable`.


## Uninstall Microsoft Power Apps CLI

To uninstall the Power Apps CLI tooling, run the MSI from [here](https://aka.ms/PowerAppsCLI). 

If you are a Private Preview participant and have an older version of CLI, follow these steps:

1. To find out where Power Apps CLI is installed, open a command prompt and type `where pac`.
1. Delete the PowerAppsCLI folder.
1. Open the Environment Variables tool by running the command `rundll32 sysdm.cpl,EditEnvironmentVariables` in the command prompt.
1. Double-click `Path` under the `User variable for...` section.
1. Select the row containing the PowerAppsCLI path and select the **Delete** button on the right-hand side.
1. Select **OK** twice.

### See also

[Implement components using TypeScript](implementing-controls-using-typescript.md)<br/>
