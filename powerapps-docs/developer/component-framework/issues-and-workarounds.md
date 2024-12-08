---
title: Common issues and workarounds (Power Apps Component Framework) | Microsoft Docs
description: Provides information on known issues and workarounds some come across while working with Power Apps component framework and CLI
author: anuitz
ms.author: anuitz
ms.date: 10/28/2024
ms.reviewer: jdaly
ms.topic: article
ms.subservice: pcf
contributors:
 - JimDaly
---

# Common issues and workarounds

Here are some common issues that you might come across while using the Power Apps component framework and Microsoft Power Platform CLI.

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

## Component changes aren't reflected after the updated solution import?

Update the component version (minor or patch) in the component manifest file (for example, 1.0.0 to 1.0.1). Every update in the component needs a component version bump to be reflected on the Microsoft Dataverse server.

```XML
 <control namespace="SampleNamespace" constructor="TSLinearInputControl"
   version="1.0.1"
    display-name-key="TSLinearInputControl_Display_Key" description-key="TSLinearInputControl_Desc_Key" control-type="standard">
```

## Msbuild error MSB4036

- The name of the task in the project file is same as the name of the task class.
- The task class is public and implements the Microsoft.Build.Framework.ITask interface.
- The task is correctly declared with *\<UsingTask>* in the project file or in the *.tasks files located in the path directory.

**Workaround**:

- Open Visual Studio Installer.
- For Visual Studio 2017 or higher, select **Modify**.
- Select **Individual Components**.
- Under Code Tools, check **NuGet targets & Build Tasks**.

> [!NOTE]
> We will be constantly adding common issues and workarounds as we come across during the development process. If you encounter an issue and have a workaround and you think that is helpful, raise the issue [here](https://powerusers.microsoft.com/t5/Power-Apps-Component-Framework/bd-p/pa_component_framework) or raise a pull request so that we can review and add it to the list.

## Issues while updating existing code components

- If you created a code component using CLI version 0.1.817.1 or earlier and want to ensure that the latest build and debug modules are being used, make the following updates to the `package.json` file:

   ```JSON
   "dependencies": { "@types/node": "^10.12.18", "@types/powerapps-component-framework": "1.1.0"}, "devDependencies": { "pcf-scripts": "~0", "pcf-start": "~0" }
   ```

## Error: Failed to retrieve information about Microsoft.PowerApps.MSBuild.Pcf from remote source &lt;Feed Url&gt; when the build fails for authorization issues.

   **Workaround**

   - Open the `NuGet.Config` file from **%APPDATA%\NuGet**. The feed from which the user is getting the error should be present in this file.
   - Remove the feed from the `NuGet.Config file` or generate a PAT token and add it to the` Nuget.Config file`. For example:

     ```XML
     <?xml version="1.0" encoding="utf-8"?>
     <configuration>
     <packageSources>
         <add key="YourFeedName" value="https://contoso.com/_packaging/YourFeedName/nuget/v3/index.json" />
      </packageSources>
      <packageSourceCredentials>
      <YourFeedName>
      <add key="Username" value="anything" />
      <add key="Password" value="User PAT" />
        </YourFeedName>
        </packageSourceCredentials>
       </configuration>
     ```

## Web resource size is too large

Error  **Import Solution Failed: Web resource content size is too big**.

### Workarounds

There are two ways to work around this error:

 - [Build the PCF using the release configuration](#build-the-pcf-using-the-release-configuration)
 - [Increase the maximum size for email attachments](#increase-the-maximum-size-for-email-attachments)


#### Build the PCF using the release configuration


- Build  the `.pcfproj` as release configuration, which sets the web pack to production mode using the command:

  ```CLI
  msbuild /property:configuration=Release
  ```

- Run the msbuild command with the following extra property:

  ```CLI
  msbuild /p:PcfBuildMode=production
  ```

- Edit the `.pcfproj` to always build the web pack in production mode by setting the property `PcfBuildMode` to production:

  ```XML
  <PropertyGroup>
    <Name>TS_ReactStandardControl</Name>
    <ProjectGuid>0df84c56-2f55-4a80-ac9f-85b7a14bf378</ProjectGuid>
    <OutputPath>$(MSBuildThisFileDirectory)out\controls</OutputPath>
    <PcfBuildMode>production</PcfBuildMode>
  </PropertyGroup>
  ```

#### Increase the maximum size for email attachments

The size limit for files used by PCF controls is limited by the same setting that limits the size of email attachments. See the **Maximum file size for attachments** setting described in [Manage email settings](/power-platform/admin/settings-email).

This value is set in the [Organization.MaxUploadFileSize](../data-platform/reference/entities/organization.md#BKMK_MaxUploadFileSize) column. [Learn how to read and update environment settings using code](../data-platform/organization-table.md)

## When running Power Apps checker with the solution built using CLI tooling in default configuration

**Error: Do not use the eval function or its functional equivalents**

This warning is by design since the default `msbuild` configuration is `Configuration=Debug`. This in turn instructs web pack (used to bundle the code component) to package in development mode, which emits `eval()`.

**Workaround**

Re build the solution file using  the following either of the commands and reimport the solution into Dataverse.

```CLI
msbuild/property:configuration:Release
```

```CLI
npm run build -- --buildMode production
```

<!--## Power Apps component framework Datasets getValue by property alias doesn't work

Power Apps component framework dataset API's getValue function only searches record by the dataset column name and not the property alias set in the manifest. Attempting to get value by property alias will return an empty value.

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

## Power Apps component framework Datasets SharePoint issue

Power Apps component framework dataset component currently does not properly show the records from SharePoint. While the network request will succeed with the correct data records returned, the deserialization fails and an empty dataset is returned.

**Workaround**

No workaround as of now. We are working on pushing a fix to our deployment trains.-->


## Authentication for third party services fails in Canvas

PCF authentication for third parties isn't supported.

**Workaround**

Use combination of a [custom page](../../maker/model-driven-apps/model-app-page-overview.md) and a [connector](../../maker/canvas-apps/connections-list.md).

## Control can't finish loading

If you use [refresh](./reference/dataset/refresh.md) in `updateView` you must include a guarding condition, otherwise it creates an infinite loop. Whenever `refresh` is called, it resets the page number to 1, and then fetch the first page of records under the current filtering and sorting criteria. When the client recieves the  updated data, `updateView` is called to update the display. The result is that the control can't finish loading and won't be able to fetch records beyond the first page.

## Same page is loaded rather than the expected one

[refresh](./reference/dataset/refresh.md), [loadExactPage](./reference/paging/loadExactPage.md), [loadNextPage](./reference/paging/loadnextpage.md), [loadPreviousPage](./reference/paging/loadpreviouspage.md) don't support parallel execution.

When these functions are called, the results for the requested page won't be available immediately in the next line. Instead they'll trigger `updateView` on the control with newly fetched results.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
