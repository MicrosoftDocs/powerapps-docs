---
title: Create custom component using PowerApps CLI| Microsoft Docs
description: Start creating a component using the PowerApps CLI
keywords: PowerApps component framework, Custom components, Component Framework
ms.author: nabuthuk
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d2cbf58a-9112-45c2-b823-2c07a310714c
---

## Creating a new component project

Use Microsoft PowerApps CLI tool to create your custom components. To create a new project for your custom component, follow the steps below:

1. Open **Developer command prompt for VS 2017** .
2. Create a new folder for the project using the command 
   ```CLI
   mkdir <Name of the folder>
   ```
3. Navigate into the new directory using the command 
   ```CLI
    cd <Name of the folder>
   ```
4. Create the component project using the command 
   ```CLI
    pac pcf init --namespace <Namespace for your component> --name <Name of the custom component> --template < component type >
   ```
    > [!NOTE]
    > Today we only support two component types field and dataset

5. Install the project dependencies using the command 
    ```CLI
    npm install
    ```
6. Open the project in any developer environment of your choice. 
7. Open the **ControlManifest,xml** file and configure the properties that are required to create your custom component. More information [Manifest](manifest-schema-reference/manifest.md)
8. Create a new folder inside the **Sample Component\mycomponent** and name it as **css**.
9. Create a new css file to add styling to the custom component. 
10. Open the **index.ts** file to implement the custom logic

## See also

[Debug custom components](debugging-custom-controls.md)

