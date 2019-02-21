---
title: Import Controls into Model-driven Apps | Microsoft Docs
description: Process to import custom controls
keywords:
ms.author: nabuthuk
manager: kvivek
ms.date: 03/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.topic: "article"
---

# Import controls into Mode-driven apps

[!INCLUDE[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This topic demonstrates how to create a solution file using the PowerShell script to import controls into Model-driven apps.

After developing custom controls using PowerApps Control Framework, next step is to import those controls into Model-driven apps, so that we can see the controls in runtime.

## Prerequisites

Download the [PowerAppsControlFramework_Preview.zip]() file and extract it so that you will have a copy in your local folder. When you extract it you will see

1. `Docs` folder which has documentation files for all the individual sample controls.
2. `src` folder which has two sub folders `controls` and `typing`.

   - `controls` folder has all the sample controls.
   - `typing` folder contains the TypeScript file for the control framework APIs.
3. `solution_template` folder which has all the necessary template files for building the solution package file.
4. A PowerShell script **Create_Preview_Solution.ps1** which generates a solution file for the controls.
5. LegacyWebResource folder which contains a sample `HTML` web resource.

In the controls folder you have an option to choose either a **TypeScript** or **JavaScript** control for creating your custom control. All the TypeScript controls starts with `TS_(name)` and all the JavaScript controls start with `JS_(name)`.  

> [!NOTE]
> Copy and paste your custom control inside the `controls` folder. If you copy and paste it outside the `controls` folder and when you run the script to build the solution file, this control is not included in the solution package. 

## Create a solution zip file using PowerShell script

The `Create_Preview_Solution.ps1` PowerShell script creates the solution package file for the controls. It is recommended to change the publisher and solution unique name in the solution.xml file in `solution_template` folder. 

### Run the PowerShell script in file explorer  

1. Right click on the Create_Preview_Solution and click on Run with PowerShell as shown in the screenshot.
2. A `drop` folder is created which has the solution package file, that you can import manually. A target folder is also created at the same time. When you run the script, initially the files are copied over to the target folder and then a drop package is built from the contents of the target folder.

### Run the PowerShell script using Windows PowerShell

1. Open the Windows PowerShell application. 
2. Navigate to the directory where you have downloaded and extracted the folder, for example, assuming the folder is downloaded at `C:\Users\YourUsername`  
3. Run the command `C:\Users\YourUsername\Get-ExecutionPolicy` to check whether the execution policy is **Restricted** on your local machine. 
4. If the command returns **Restricted**. Run the following command to change the policy `C:\Users\YourUsername\Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`
5. Now, run the command below, to a generate solution package `C:\Users\username\PowerAppsControlFramework_Preview\create_preview_solution.ps1-uploadToServer $true`
6. When you run the above command, it will automatically import the solution file into the org and it also creates a drop folder which has the solution file, that you can import manually.
7. If you don't want to automatically import the solution file into the org, run the following command. `C:\Users\username\PowerAppsControlFramework_Preview\Create_Preview_Solution.ps1-uploadToServer $false`

> [!div class="nextstepaction"]
> [Add Controls to entities or fields](add-custom-controls-to-a-field-or-entity.md)