---
title: Microsoft PowerApps CLI| Microsoft Docs
description: Start creating a component using the PowerApps CLI
keywords: PowerApps component framework, Custom components, Component Framework
ms.author: nabuthuk
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: bc960df3-5418-45b2-9a25-3424ba40b8b4
---

# Microsoft PowerApps CLI

[!INCLUDE[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Use PowerApps Command Line Interface (CLI) to create, debug and deploy custom PowerApps component framework components. PowerApps CLI will enable developers to quickly create PowerApps component framework components and will in the future be expanded to include support for additional development and Application Lifecycle Management (ALM) experiences. 

Microsoft PowerApps CLI is a simple, single-stop developer command line interface enabling you to create custom component. PowerApps CLI is also the first step towards a comprehensive ALM story where enterprise developers and ISVs can create, build, debug and publish their PowerApps and Dynamics 365 for Customer Engagement apps extensions and customizations quickly and efficiently.  

> [!IMPORTANT]
> - Microsoft PowerApps CLI tools are a pre-release version and may be different from the commercially released version.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)] 
> - If you give feedback about the software to Microsoft, you give to Microsoft, without charge, the right to use, share and commercialize your feedback in any way and for any purpose. 
> - Microsoft doesn't provide support for this preview feature. Microsoft Technical Support won’t be able to help you with issues or questions.

## Prerequisites 

To use PowerApps CLI you will need the following:

- Install [Npm](https://www.npmjs.com/get-npm)(comes with Node.js) or install [Node.js](https://nodejs.org/en/) (comes with npm). We recommend LTS (Long Term Support) version 10.15.3 LTS as it seems to be most stable.
- If you don’t have Visual Studio 2017 or later, follow one of the options below:
   - Option 1: Install Visual Studio 2017 or later
   - Option 2: Install .NET Core 2.2 SDK and install Visual Studio Code
- Install Microsoft PowerApps CLI from [here](http://download.microsoft.com/download/D/B/E/DBE69906-B4DA-471C-8960-092AB955C681/powerapps-cli-0.1.51.msi)

> [!NOTE]
> Currently PowerApps CLI is supported only on Windows 10.

## Creating custom components

To create, debug and deploy your custom components using Microsoft PowerApps CLI, see [Creating components using PowerApps CLI](implementing-controls-using-typescript)

## Telemetry

The feature team is aggregating anonymized telemetry in order to understand which features or capabilities in the PowerApps CLI tool are most often used by the developers. The aggregated data allows us to provide the best experience to the customers by focusing on what’s truly is important.

> [!NOTE]
> To disable the telemetry collection, run the command `pac telemetry --enable false`. To turn the telemetry back, use the command `pac telemetry --enable true`.

## How to uninstall Microsoft PowerApps CLI

To uninstall the CLI tool please run the MSI from [here](http://download.microsoft.com/download/D/B/E/DBE69906-B4DA-471C-8960-092AB955C681/powerapps-cli-0.1.51.msi). If you are Private Preview Participant and have an older version of CLI, please follow below manual steps:

1. To find out where PowerApps CLI is installed, open a command prompt and type `where pac`
1. Delete the PowerAppsCLI folder.
1. Open Environment Variables tool by running command `rundll32 sysdm.cpl,EditEnvironmentVariables` in the command prompt
1. Double-click on **Path** under **User variable for...** section
1. Select the row containing PowerAppsCLI path and click the **Delete** button on the right-hand side
1. Click OK twice

## Known configuration issues and workarounds

**Msbuild error MSB4036:**

1. The name of the task in the project file is same as the name of the task class.
2. The task class is public and implements the Microsoft.Build.Framework.ITask interface.
3. The task is correctly declared with <UsingTask> in the project file or in the *.tasks files located in the <path> directory

**Resolution:**

1. Open **Visual Studio Installer** 
1. For VS 2017, click on **Modify** 
1. Click on **Individual Components** tab
1. Under **Code Tools**, check **NuGet targets & Build Tasks**

### See also

[Implementing components using PowerApps CLI](implementing-controls-using-typescript.md)<br/>
[Updating existing components into new tools format](updating-existing-controls.md)<br/>
[PowerApps component framework API Reference](reference/index.md)<br/>
[PowerApps component framework Overview](overview.md)