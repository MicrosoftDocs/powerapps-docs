---
title: Known issues and workarounds (Power Apps Component Framework) | Microsoft Docs
description: Provides information on know issues and workarounds some commonly encountered issues while working with Power Apps component framework and CLI
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

# Known issues and workarounds

**Msbuild error MSB4036**

1. The name of the task in the project file is the same as the name of the task class.
2. The task class is public and implements the Microsoft.Build.Framework.ITask interface.
3. The task is correctly declared with *\<UsingTask>* in the project file or in the *.tasks files located in the path directory.

**Workaround**:

1. Open Visual Studio Installer. 
1. For Visual Studio 2017, select **Modify**. 
1. Select **Individual Components**.
1. Under Code Tools, check **NuGet targets & Build Tasks**.

> [!NOTE]
> We will be constantly adding known issues and workarounds as we encounter during the development process. If you encounter an issue and have a workaround and you think this is helpful, raise the issue [here](https://powerusers.microsoft.com/t5/Power-Apps-Component-Framework/bd-p/pa_component_framework) so that we will review and add it to the list.

**Publisher Prefix**

If a component is created using a Power Apps CLI tooling version lower than 0.4.3,  you will hit an error while trying to re-import the solution file into Common Data Service. The error is thrown because the newly imported component name is now being appended with the publisher prefix to ensure its uniqueness and to avoid collisions.

**Workaround**:

- Delete the solution containing the relevant component from Common Data Service. If the component is already configured on a form or grid, it needs to be removed there first because the component solution had a dependency on the configuration.  
- Import the new solution with updates to the component built by the latest CLI version.
- Newly imported components can now be configured on forms or grids.  