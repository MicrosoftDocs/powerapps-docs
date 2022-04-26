---
title: Microsoft Power Platform CLI package command| Microsoft Docs
description: "Includes descriptions and supported parameters for the package command."
keywords: Microsoft Power Platform CLI, code components, component framework, CLI
ms.subservice: dataverse-developer
author: kkanakas
ms.author: kartikka
manager: pemikkel
ms.date: 04/01/2022
ms.reviewer: jdaly
ms.topic: reference
contributors: 
  - JimDaly
---

# Package

Command to work with solution packages.

## Parameters

|Property Name|Description|Example|
|-------------|-----------|-------|
|add-reference|Sets the reference path to the solution project folder by passing the `path` parameter.|`pac package add-reference --path c:\Users\Downloads\SampleSolution`|
|init|Initializes a new package project. It has the following parameter: <ul><li>*outputdirectory*: Output directory where the package is created.</li></ul>| `pac package init --outputdirectory c:\samplepackage`|
|deploy| Deploys the package .dll or the .zip file with a package. It has the following parameters:<ul><li>*logFile*: Path to a log file location where the logs are redirected. </li><li>*logConsole*: This option is used if you want to direct the logs to the console.</li><li>*package*: The path location to the package .dll (library) or a .zip file with a package.</li></ul>**Note**: You can use both `logFile` and `logConsole` parameters together, or use one parameter or the other. | `pac package deploy --logFile c:\samplelogdata --package c:\samplepackage` |
|show| Shows the content of a package .dll or a .zip file with a package. It has the following parameter: <ul><li>*package*: The path location to the package .dll (library) or the .zip file.</li></ul>| `pac package show c:\samplepackage.dll`|


### See also

[Power Apps component framework overview](../../../component-framework/overview.md)

[What is Microsoft Power Platform CLI](../../powerapps-cli.md)