---
title: Get tooling for PowerApps component framework | Microsoft Docs
description: "Get the Microsoft PowerApps CLI to create, debug and deploy custom components using PowerApps component framework."
keywords: PowerApps component framework, Custom components, Component Framework
ms.author: nabuthuk
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: f393f227-7a88-4f25-9036-780b3bf14070
---

# Get tooling for PowerApps component framework

[!INCLUDE[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Use **Microsoft PowerApps CLI** (command-line interface) to create, debug and deploy custom components using PowerApps component framework. PowerApps CLI enables developers to quickly create PowerApps component framework components and will in the future be expanded to include support for additional development and Application Lifecycle Management (ALM) experiences. 

## What is Microsoft PowerApps CLI? 

Microsoft PowerApps CLI is a simple, single-stop developer command line interface enabling you to create custom component. PowerApps CLI is also the first step towards a comprehensive ALM story where enterprise developers and ISVs can create, build, debug and publish their PowerApps and Dynamics 365 for Customer Engagement apps extensions and customizations quickly and efficiently.  

> [!IMPORTANT]
> - Microsoft PowerApps CLI tools are a pre-release version and may be different from the commercially released version.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)] 
> - If you give feedback about the software to Microsoft, you give to Microsoft, without charge, the right to use, share and commercialize your feedback in any way and for any purpose. 
> - Microsoft doesn't provide support for this preview feature. Microsoft Technical Support won’t be able to help you with issues or questions.

## Install Microsoft PowerApps CLI

To use Microsoft PowerApps CLI, do the following:

1. Install [Npm](https://www.npmjs.com/get-npm) (comes with Node.js) or install [Node.js](https://nodejs.org/en/) (comes with npm). We recommend LTS (Long Term Support) version 10.15.3 LTS as it seems to be most stable.

1. If you don’t already have Visual Studio 2017 or later, follow one of the options below:
   - Option 1: Install Visual Studio 2017 or later
   - Option 2: Install .NET Core 2.2 SDK and install Visual Studio Code

1. Install Microsoft PowerApps CLI from [here](http://download.microsoft.com/download/D/B/E/DBE69906-B4DA-471C-8960-092AB955C681/powerapps-cli-0.1.51.msi)



> [!NOTE]
> - To deploy your custom component using PowerApps CLI, you must have a Common Data Service environment with system administrator or system customizer privileges.
> - Currently, PowerApps CLI is supported only on Windows 10.

## Update Microsoft PowerApps CLI to the latest version

To update your Microsoft PowerApps CLI to the latest version 02.856.1 and take advantage of all the latest capabilities, run the following command in the Developer Command Prompt for VS 2017:

```CLI
pac install latest
```

### What else do I need to know?

If you have already created a solution project or PowerApps component framework project, ensure to update these projects to the latest packages. This will help you leverage newly added capabilities with your existing projects. Newly created projects will already contain these settings.

- Update the version tag in your `pcfproj` located within your PowerApps component framework project folder:

   ```XML
   <PackageReference Include="Microsoft.PowerApps.MSBuild.Pcf" Version="0.*"/>
   ```
- Update the version tag in your `cdsproj` located within your solution project folder:

   ```XML
   <PackageReference Include="Microsoft.PowerApps.MSBuild.Solution" Version="0.*"/>
   ```

    > [!NOTE] 
    > After making the above changes, run the command `msbuild /t:restore` to update your project to the correct version.


- Update the version tag in your `package.json` file located within your PowerApps component framework project folder:

  ```JSON
  "devDependencies":{
   "pcf-scripts": "^0",
   "pcf-start": "^0"
    }
  ```
   > [!NOTE]
   > After making above changes, using 'npm update' in the command prompt will always update your project to the correct version.

## Microsoft PowerApps CLI telemetry

The feature team is aggregating anonymized telemetry in order to understand which features or capabilities in the PowerApps CLI tool are most often used by the developers. The aggregated data allows us to provide the best experience to the customers by focusing on what’s truly is important.

> [!NOTE]
> To disable the telemetry collection, run the command `pac telemetry --enable false`. To turn the telemetry back, use the command `pac telemetry --enable true`.

## Uninstall Microsoft PowerApps CLI

To uninstall the CLI tool please run the MSI from [here](http://download.microsoft.com/download/D/B/E/DBE69906-B4DA-471C-8960-092AB955C681/powerapps-cli-0.1.51.msi). If you are Private Preview Participant and have an older version of CLI, please follow below manual steps:

1. To find out where PowerApps CLI is installed, open a command prompt and type `where pac`
1. Delete the PowerAppsCLI folder.
1. Open Environment Variables tool by running command `rundll32 sysdm.cpl,EditEnvironmentVariables` in the command prompt
1. Double-click on `Path` under `User variable for...` section
1. Select the row containing PowerAppsCLI path and click the Delete button on the right-hand side
1. Click **OK** twice.

### See also

[Implementing components in TypeScript](implementing-controls-using-typescript.md)<br/>

