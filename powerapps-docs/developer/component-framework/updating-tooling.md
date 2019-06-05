---
title: Updating PowerApps CLI| Microsoft Docs
description: Updating the PowerApps CLI
keywords: PowerApps component framework, Custom components, Component Framework
ms.author: nabuthuk
manager: kvivek
ms.date: 05/23/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 47c4426c-e963-4ef6-a4b7-d56591ca8ac2
---

# Updating tooling to latest version

To update your Microsoft PowerApps CLI to the latest version 02.856.1 and take advantage of all the latest capabilities, run the following command in the Developer Command Prompt for VS 2017.

```CLI
pac install latest
```

## What else do I need to know?

If you have already created a solution project or PowerApps component framework project, ensure to update these projects to the latest packages. This will help you leverage newly added capabilities with your existing projects. Newly created projects will already contain these settings.

- Update the version tag in your `pcfproj` located within your PowerApps component framework project folder:

   ```XML
   <PackageReference Include="Microsoft.PowerApps.MSBuild.Pcf" Version="0.*"/>
   ```
- Update the version tag in your `cdsproj` located within your solution project folder:

   ```XML
   <PackageReference Include="Microsoft.PowerApps.MSBuild.Solution" Version="0.*"/>
   ```

    > [!NOTE] 
    > After making the above changes, run the command `msbuild /t:restore` to update your project to the correct version.


- Update the version tag in your `package.json` file located within your PowerApps component framework project folder:

  ```JSON
  "devDependencies":{
   "pcf-scripts": "^0",
   "pcf-start": "^0"
    }
  ```
   > [!NOTE]
   > After making above changes, using 'npm update' in the command prompt will always update your project to the correct version.
