---
title: How to run the samples | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: kvivek
ms.date: 11/25/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: c003d29d-feef-4209-810e-8f1abe11dd6e
---

1. Download the [sample components](https://go.microsoft.com/fwlink/?linkid=2088525) so that you have a local copy. Install [PowerApps CLI](https://aka.ms/PowerAppsCLI).
2. Go into the directory where you have downloaded the folder. 
3. Open Developer Command Prompt for VS 2017 and go into the sample component folder, which you want to see it in runtime (for example, Increment component).
4. Run the command `npm install` to get all the required dependencies.
5. Create a new folder using the command `mkdir <folder name>` inside the sample component folder (for example, Increment component) and navigate into the folder using the command `cd <folder name>`. 
6. Create a new solution project inside the folder using the command `pac solution init --publisher-name <Name of the publisher> --publisher-prefix <Publisher prefix>`.
7. Once the new solution project is created, you need to refer to the location where the sample component is located. You can add the reference using the command `pac solution add-reference --path <Path to the root of the sample component>`.
8. To generate a zip file from your solution project, you need to `cd` into your solution project directory and build the project using the command `msbuild /t:restore`.
9. Again, run the command `msbuild`.
10. The generated solution zip file is located in the `Solution\bin\debug` folder.
11. Manually [import the solution into Common Data Service](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/customize/import-update-upgrade-solution) using the web portal once the zip file is ready or see the [Authenticating to your organization](https://docs.microsoft.com/en-us/powerapps/developer/component-framework/import-custom-controls#authenticating-to-your-organization) and [Deployment](https://docs.microsoft.com/en-us/powerapps/developer/component-framework/import-custom-controls#deploying-code-components) sections to import using PowerApps CLI commands.
12. To add code components to model-driven apps and canvas apps, see topics [Add components to model-driven apps](https://docs.microsoft.com/en-us/powerapps/developer/component-framework/add-custom-controls-to-a-field-or-entity) and [Add components to canvas apps](https://docs.microsoft.com/en-us/powerapps/developer/component-framework/component-framework-for-canvas-apps#add-components-to-a-canvas-app)