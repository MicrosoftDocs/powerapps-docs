---
title: Common issues and workarounds (Power Apps Component Framework) | Microsoft Docs
description: Provides information on know issues and workarounds some come across while working with Power Apps component framework and CLI
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

# Common issues and workarounds

Here are some common issues that you might come across while using the Power Apps component framework and Power Apps CLI.

**Msbuild error MSB4036**

1. The name of the task in the project file is same as the name of the task class.
2. The task class is public and implements the Microsoft.Build.Framework.ITask interface.
3. The task is correctly declared with *\<UsingTask>* in the project file or in the *.tasks files located in the path directory.

**Workaround**:

1. Open Visual Studio Installer. 
1. For Visual Studio 2017, select **Modify**. 
1. Select **Individual Components**.
1. Under Code Tools, check **NuGet targets & Build Tasks**.

> [!NOTE]
> We will be constantly adding common issues and workarounds as we come across during the development process. If you encounter an issue and have a workaround and you think that is helpful, raise the issue [here](https://powerusers.microsoft.com/t5/Power-Apps-Component-Framework/bd-p/pa_component_framework) or raise a pull request so that we can review and add it to the list.

**Publisher Prefix**

If a component is created using the CLI version lower than 0.4.3, you will encounter an error while trying to reimport the solution file into Common Data Service. 

**Workaround**:

- Delete the solution containing the relevant component from Common Data Service. 
- The component needs to be removed from the filed or grid if the component is already configured to avoid dependencies.
- Import the new solution with updates to the component built by the latest CLI version.
- Newly imported components can now be configured on forms or grids.  

**Issues while updating existing code components**

1. If you get a 1ES notification asking how pcf-scripts are being used, note that these scripts are only used to build the code components but they are not bundled or used by the resulting component.  
2. If you have created a code component using the CLI version 0.1.817.1 or earlier and want to ensure that the latest build and debug modules are being used, make the updates to the `package.json` file as shown below:
   
   ```JSON
   "dependencies": { "@types/node": "^10.12.18", "@types/powerapps-component-framework": "1.1.0"}, "devDependencies": { "pcf-scripts": "~0", "pcf-start": "~0" } 
   ```

3. Error **Failed to retrieve information about Microsoft.PowerApps.MSBuild.Pcf from remote source <Feed Url>** when the build fails for authorization issues. 

   **Workaround**

   - Open the `NuGet.Config` file from **%APPDATA%\NuGet**. The feed from which the user is getting the error should be present in this file. 
   - Remove the feed from the `NuGet.Config file` or generate a PAT token and add it to the` Nuget.Config file`. For example:

     ```XML
     <?xml version="1.0" encoding="utf-8"?>  
     <configuration>  
     <packageSources>  
         <add key="CRMSharedFeed" value="https://dynamicscrm.pkgs.visualstudio.com/_packaging/CRMSharedFeed/nuget/v3/index.json" />  
      </packageSources>  
      <packageSourceCredentials>  
      <CRMSharedFeed>  
      <add key="Username" value="anything" />  
      <add key="Password" value="User PAT" />  
        </CRMSharedFeed>  
        </packageSourceCredentials>  
       </configuration>
     ```
