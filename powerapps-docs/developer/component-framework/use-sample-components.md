---
title: How to use the sample components that are built using Power Apps component framework in Microsoft Dataverse | Microsoft Docs
description: Provides information on how you can use the sample components created using Power Apps Component Framework in your model-driven and canvas apps
keywords:
author: Nkrb
ms.author: nabuthuk
manager: kvivek
ms.date: 06/08/2021
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
---

# How to use the sample components?

All the sample components listed under this section are available to download from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework) so that you can try them out in your model-driven or canvas apps.

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

The individual sample component topics under this section provide you an overview of the sample component, it's visual appearance, and a link to the complete sample component.

## Before you can try the sample components

To try the sample components, you must first:

- [Download](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework) the sample components so that you have a local copy.
- Install [Microsoft Power Platform CLI](https://aka.ms/PowerAppsCLI).

## Try the sample components

Follow the steps below to import and try the sample components in your model-driven or canvas app:

1. Navigate to the folder on your computer where you have downloaded the sample components, and extract the .zip file.  
1. Open Developer Command Prompt for Visual Studio 2017 or higher and navigate to the sample component folder in the extracted folder that you want to see it in runtime. For example, navigate to the `/extracted_folder/IncrementComponent` folder.

   >[!NOTE]
   > You need to go into the specific component folder if you wish to see that particular component in runtime. You can add multiple components into a single solution file during the build process.

1. Run the following command to get all the required dependencies:
    ```CLI
    npm install
    ```
1. Create a new folder using the command `mkdir <folder name>` inside the sample component folder that has the `pcfproj` file and navigate into the folder using the command `cd <folder name>`. 
1. Create a new solution project inside the folder using the following command:
    ```CLI
    pac solution init --publisher-name <Name of the publisher> --publisher-prefix <Publisher prefix>
    ```
1. After the new solution project is created, refer to the location where the sample component is located. You can add the reference using the following command:
    ```CLI
    pac solution add-reference --path <Path to the root of the sample component>
    ```
1. To generate a zip file from your solution project, you need to `cd` into your solution project directory and build the project using the following command:
    
     ```CLI
     msbuild /t:restore
    ```
1. Again, run the command `msbuild`.
1. The generated solution zip file will be available at `Solution\bin\debug` folder. Manually [import the solution](../../maker/data-platform/import-update-export-solutions.md) into your Microsoft Dataverse environment using the web portal once the zip file is ready. Alternatively, to import the solution using Microsoft Power Platform CLI commands, see the [Connecting to your environment](./import-custom-controls.md#connecting-to-your-environment) and [Deployment](./import-custom-controls.md#deploying-code-components) sections.
1. Finally, to add code components to your model-driven and canvas apps, see [Add components to model-driven apps](./add-custom-controls-to-a-field-or-entity.md) and [Add components to canvas apps](./component-framework-for-canvas-apps.md#add-components-to-a-canvas-app).


[!INCLUDE[footer-include](../../includes/footer-banner.md)]