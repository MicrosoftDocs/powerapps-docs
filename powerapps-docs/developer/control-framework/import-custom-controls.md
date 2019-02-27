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

This topic demonstrates how to import custom controls into Model-driven apps. After developing custom controls using PowerApps CLI, next step is to import those controls into Model-driven apps, so that we can see the controls in runtime.

Follow the steps below to create and import a solution file:

1. Create a new solution project in a directory of your choice by using the command `pac solution init` after `cd <your new folder>`.

> [!NOTE]
> The solution project is created using default values. If you have a requirement to specify for example, a non-default publisher or to version your solution up, please modify the appropriate fields in solution.xml file directly. This xml file will be in folder which you created above. If you aren’t sure what custom values are needed, you can always export any existing solution from your environment and check the contents of its xml file.
 
2. Once your new solution project is created, it will need to know where your newly created control is. You can add the reference by using the command
`pac solution add-reference --<path of your pcf project on disk>`
3. To generate a zip file from your solution project, you will need to `cd` into your solution project directory and build the project using the command `msbuild` 
4. The generated solution files are located in `\bin\debug\`.
5. You should manually import the solution using the web portal.

> [!div class="nextstepaction"]
> [Add Controls to entities or fields](add-custom-controls-to-a-field-or-entity.md)