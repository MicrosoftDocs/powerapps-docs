---
title: Microsoft Power Platform CLI pcf command| Microsoft Docs
description: "Includes descriptions and supported parameters for the pcf command."
keywords: Microsoft Power Platform CLI, code components, component framework, CLI
ms.subservice: dataverse-developer
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 09/15/2021
ms.service: "powerapps"
ms.topic: "article"
---

# PCF

Commands to work with [Power Apps component framework](../component-framework/overview.md). 

## Parameters

|Property Name|Description|Example|
|-------------|-----------|-------|
|init|Initializes the code component project. It has the following parameters: <ul><li>*namespace*: Namespace of the code component. </li><li>*name*: Name of the code component.</li><li>*template*: Field or dataset</li></ul>| `pac pcf init --namespace SampleNameSpace --name SampleComponent --template field`|
|push|Pushes the code component to the Dataverse instance with all the latest changes. It has the following parameter:<ul><li>*publisher-prefix*: Publisher prefix of the organization.</li></ul>|`pac pcf push --publisher-prefix dev`|
|version|Updates the component manifest file with the specified patch version. It has the following parameters: <ul><li>*patchversion*: Patch version of the code component. `patchversion` will only take value of the third part of the version tuple: `Major.Minor.Patch`.</li><li>*path*: Absolute or relative path of the component manifest file.</li><li>*allmanifests*: Updates the patch version for all the component manifest files.</li><li>*updatetarget*: Updates the specified manifest file. It has two values, build and project.</li><li>*strategy*: Updates the patch version for the manifest files by using specified strategy values. It has the following values: <ul><li>*gittags*: Use Git tags to decide whether a particular component's patch version needs to be updated.</li><li>*filetracking*: Use a .csv file to decide whether a particular component's patch version needs to be updated.</li><li>*manifest*: Increments the patch version by 1 for all the components.</li></li></ul>|`pac pcf version --patchversion 1.0.0.0 --path c:\Users\Downloads\SampleComponent --allmanifests`  <br/><br/> `pac pcf version --strategy gittags`|