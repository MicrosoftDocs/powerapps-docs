---
title: How to use the sample components? (Power Apps Component Framework) | Microsoft Docs
description: Provides information on how you can use the sample components created using Power Apps Component Framework in your model-driven and canvas apps
keywords:
author: Nkrb
ms.author: nabuthuk
manager: kvivek
ms.date: 11/25/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
---

# How to use the sample components?

All the sample components listed under this section are available to download from [here](https://go.microsoft.com/fwlink/?linkid=2088525) so that you can try them out in your model-driven or canvas apps.

The individual sample component topics under this section provide you an overview of the sample component, it's visual appearance, and the manifest, code, and resources for the sample component.

## Before you can try the sample components
To try the sample components, you must first:
- [Download](https://go.microsoft.com/fwlink/?linkid=2088525) the sample components so that you have a local copy.
- Install [Power Apps CLI](https://aka.ms/PowerAppsCLI).

## Try the sample components
Follow the steps below to import and try the sample components in your model-driven or canvas app:

1. Navigate to the folder on your computer where you have downloaded the sample components, and extract the .zip file.  
1. Open Developer Command Prompt for Visual Studio 2017 and navigate to the sample component folder in the extracted folder that you want to see it in runtime. For example, navigate to the \<extracted_folder>/TS_IncrementComponent folder.
1. Run the following command to get all the required dependencies:
    ```
    npm install
    ```
1. Create a new folder using the command `mkdir <folder name>` inside the sample component folder and navigate into the folder using the command `cd <folder name>`. 
1. Create a new solution project inside the folder using the following command:
    ```
    pac solution init --publisher-name <Name of the publisher> --publisher-prefix <Publisher prefix>
    ```
1. After the new solution project is created, refer to the location where the sample component is located. You can add the reference using the following command:
    ```
    pac solution add-reference --path <Path to the root of the sample component>
    ```
1. To generate a zip file from your solution project, you need to `cd` into your solution project directory and build the project using the following command:
    ```msbuild /t:restore
    ```
1. Again, run the command `msbuild`.
1. The generated solution zip file will be available at `Solution\bin\debug` folder. Manually [import the solution](/powerapps/maker/common-data-service/import-update-export-solutions) into your Common Data Service environment using the web portal once the zip file is ready. Alternatively, to import the solution using Power Apps CLI commands, see the [Connecting to your environment](https://docs.microsoft.com/powerapps/developer/component-framework/import-custom-controls#connecting-to-your-environment) and [Deployment](https://docs.microsoft.com/powerapps/developer/component-framework/import-custom-controls#deploying-code-components) sections.
1. Finally, to add code components to your model-driven and canvas apps, see [Add components to model-driven apps](https://docs.microsoft.com/powerapps/developer/component-framework/add-custom-controls-to-a-field-or-entity) and [Add components to canvas apps](https://docs.microsoft.com/powerapps/developer/component-framework/component-framework-for-canvas-apps#add-components-to-a-canvas-app).
