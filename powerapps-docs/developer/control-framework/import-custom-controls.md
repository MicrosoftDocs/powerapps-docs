---
title: Import Controls  | Microsoft Docs
description: Process to import custom controls
keywords:
ms.author: nabuthuk
manager: kvivek
ms.date: 03/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.topic: "article"
---

# Import controls into Common Data Service


This topic demonstrates how to import custom controls into Common Data Service. After developing custom controls using the PowerApps CLI, next step is to import those controls, so that you can see the controls in runtime.

Follow the steps below to create and import a solution file:

1. Create a new solution project in the directory of your choice by using the command `pac solution init` after `cd <your new folder>`.

> [!NOTE]
> The [publisherName]() and [cutomizationPrefix]() values must be unique to your environment.
 
2. Once your new solution project is created, it will need to know where your newly created control is. You can add the reference by using the command
`pac solution add-reference --<path of your pcf project on disk>`
3. To generate a zip file from your solution project, you will need to `cd` into your solution project directory and build the project using the command `msbuild` 
4. The generated solution files are located in `\bin\debug\`.
5. You should manually import the solution using the web portal.

### See also

[Add Controls to entities or fields](add-custom-controls-to-a-field-or-entity.md)