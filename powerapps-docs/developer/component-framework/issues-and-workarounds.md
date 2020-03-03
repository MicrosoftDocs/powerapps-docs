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

1. **Msbuild error MSB4036**

   - The name of the task in the project file is same as the name of the task class.
   - The task class is public and implements the Microsoft.Build.Framework.ITask interface.
   - The task is correctly declared with *\<UsingTask>* in the project file or in the *.tasks files located in the path directory.

    **Workaround**:

    - Open Visual Studio Installer.
    - For Visual Studio 2017, select **Modify**.
    - Select **Individual Components**.
    - Under Code Tools, check **NuGet targets & Build Tasks**.

> [!NOTE]
> We will be constantly adding common issues and workarounds as we come across during the development process. If you encounter an issue and have a workaround and you think that is helpful, raise the issue [here](https://powerusers.microsoft.com/t5/Power-Apps-Component-Framework/bd-p/pa_component_framework) or raise a pull request so that we can review and add it to the list.

2. **Publisher Prefix**

   If a component is created using the CLI version lower than 0.4.3, you will encounter an error while trying to reimport the solution file into Common Data Service. 

   **Workaround**:

    - Delete the solution containing the relevant component from Common Data Service. 
    - The component needs to be removed from the filed or grid if the component is already configured to avoid dependencies.
    - Import the new solution with updates to the component built by the latest CLI version.
    - Newly imported components can now be configured on forms or grids.  

3. **Issues while updating existing code components**

   - If you get a 1ES notification asking how pcf-scripts are being used, note that these scripts are only used to build the code components but they are not bundled or used by the resulting component.
   - If you have created a code component using the CLI version 0.1.817.1 or earlier and want to ensure that the latest build and debug modules are being used, make the updates to the `package.json` file as shown below:
   
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

4. **Web resource size is too big**

   Error  **Import Solution Failed: Web resource content size is too big**.

   **Workaround**

   - When you're creating the `bundle.js` file from the CLI tooling, it bundles lot of components which makes the file large. Remove some of the components that are not necessary.
   - Build the component in `production` mode by modifying the `node_modules/pcf-scripts/webpackconfig.js` file.

5. **Power Apps component framework Datasets getValue by property alias doesn't work**

   Power Apps component framework dataset APIs getValue function only searches record by the dataset column name and not the property alias set in the manifest. Attempting to get value by property alias will return an empty value.

   **Workaround**

   Use the dataset column name (component can get the dataset column name by searching the column array using the alias). 

      ***Expected Behavior*** 

      ```TypeScript
      long  = dataSet.records[currentRecordId].getValue("Longitude") //based on property set in manifest"-122.3514661"
      ```

      ***Current Workaround***

      ```TypeScript
      lat = dataSet.records[currentRecordId].getValue("Address_x0020_1_x003a__x0020_Latitude")//based on the dataset column name
      ```

6. **Power Apps component framework Datasets SharePoint issue**

    Power Apps component framework dataset component currently does not properly show the records from SharePoint. While the network request will succeed with the correct data records returned, the deserialization fails and an empty dataset is returned.

    **Workaround**

    No workaround as of now. We are working on pushing a fix to our deployment trains.

