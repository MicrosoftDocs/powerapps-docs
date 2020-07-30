---
title: Install Power Apps CLI | Microsoft Docs
description: "Get the Microsoft Power Apps CLI to create, debug, and deploy code components using Power Apps component framework."
keywords: Power Apps CLI, code components, component framework, CLI
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 01/28/2020
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: f393f227-7a88-4f25-9036-780b3bf14070
---

# What is Microsoft Power Apps CLI? 

Microsoft Power Apps CLI is a simple, single-stop developer command-line interface that empowers developers and app makers to create code components. 

Power Apps CLI tooling is the first step toward a comprehensive application life-cycle management (ALM) story where the enterprise developers and ISVs can create, build, debug, and publish their extensions and customizations quickly and efficiently.  

## Install Power Apps CLI

To get Power Apps CLI, do the following:

1. Install [Npm](https://www.npmjs.com/get-npm) (comes with Node.js) or [Node.js](https://nodejs.org/en/) (comes with npm). We recommend LTS (Long Term Support) version 10.15.3 or higher.

1. Install [.NET Framework 4.6.2 Developer Pack](https://dotnet.microsoft.com/download/dotnet-framework/net462). 

1. If you don’t already have Visual Studio 2017 or later, follow one of these options:
   - Option 1: Install [Visual Studio 2017](https://docs.microsoft.com/visualstudio/install/install-visual-studio?view=vs-2017) or later.
   - Option 2: Install [.NET Core 3.1 SDK](https://dotnet.microsoft.com/download/dotnet-core/current) and then install [Visual Studio Code](https://code.visualstudio.com/Download).

1. Install [Power Apps CLI](https://aka.ms/PowerAppsCLI).

1. To take advantage of all the latest capabilities, update the Power Apps CLI tooling to the latest version using this command:

    ```CLI
    pac install latest
    ```

> [!NOTE]
> Currently, Power Apps CLI is supported only on Windows 10.

## Common commands

This table lists some of the common commands used in the CLI:

|Command|Description|
|-------|-----------|
|[pcf](#pcf)|Commands to work with [Power Apps component framework](/powerapps/developer/component-framework/overview).|
|[solution](#solution)|Commands for working with [Common Data Service solution projects](/powerapps/maker/common-data-service/solutions-overview).|
|[auth](#auth)|Commands to [authenticate to Common Data Service](/powerapps/developer/component-framework/import-custom-controls#connecting-to-your-environment).|
|[telemetry](#telemetry)|Manages the telemetry settings.|
|[plugin](#plugin)|Manages to create a [plug-in](/powerapps/developer/common-data-service/plug-ins) project.|
|[org](#org)|Command to work with Common Data Service environment.|

### Pcf

Commands to work with [Power Apps component framework](/powerapps/developer/component-framework/overview). It has the following parameters:

#### Parameters

|Property Name|Description|Example|
|-------------|-----------|-------|
|init|Initializes the code component project. It has the following parameters <br/> - *namespace*: Namespace of the code component. <br/> - *name*: Name of the code component. <br/> - *template*: Field or dataset| `pac pcf init --namespace<SampleNameSpace --name SampleComponent --template field`|
|push|Pushes the code component to the Common Data Service instance with all the latest changes. It has the following parameter: <br/> - *publisher-prefix*: Publisher prefix of the organization.|`pac pcf push --publisher-prefix dev`|
|version|Updates the component manifest file with the specified patch version. It has the following parameters: <br/> - *patchversion*: Patch version of the code component. `patchversion` will only take value of the third part of the version tuple: `Major.Minor.Patch`.<br/> - *path*: Absolute or relative path of the component manifest file.<br/> - *allmanifests*: Updates the patch version for all the component manifest files. <br/> - *updatetarget*: Updates the specified manifest file. It has two values, build and project.<br/> - *strategy*: Updates patch version for the manifest files using specified strategy values. It has the following values: <br/> - *gittags*: Use git tags to decide if a particular component’s patch version needs to be updated.<br/> *filetracking*: Use .csv file to decide if a particular component’s patch version needs to be updated. <br/> - *manifest*: Increments the patch version by 1 for all the components.|`pac pcf version --patchversion 1.0.0.0 --path c:\Users\Downloads\SampleComponent --allmanifests`  <br/><br/> `pac pcf version --strategy gittags`|


### Solution

Commands for working with [Common Data Service solution projects](/powerapps/maker/common-data-service/solutions-overview). It has the following parameters:

#### Parameters

|Property Name|Description|Example|
|-------------|-----------|-------|
|init|Initializes the solution project.  It has the following parameters:<br/>  - *publisher-name*: Publisher name of the organization. <br/>  - *publisher-prefix*: Publisher prefix of the organization.|`pac solution init --publisher-name developer --publisher-prefix dev`  |
|add-reference|Sets the reference path to the component project folder by passing the `path` parameter.|`pac solution add-reference --path c:\Users\Downloads\SampleComponent`|
|clone|Creates a solution project based up on the existing solution project. It has the following parameters:<br/> -*name*: The name of the solution to be exported.<br/> -*targetversion*: The version that the exported solution supports.<br/> -*include*: Settings that should be included in the solution being exported. <br/> It has the following values: autonumbering, calendar, customization, emailtracking, externalapplications, general, isvconfig, marketing, outlooksynchronization, relationshiproles, sales|`pac solution clone -–name  sampleSolution --version 1.0.0.2 --include general`|
|export|Exports a Common Data Service solution project from the current organization. It has the following parameters:<br/> -*path*: Place where the exported solution zip file will be saved.<br/> - *name*: Name oft he solution that needs to be exported.<br/> - *managed*: Defines whether the solution should be exported as a managed solution or not.<br/>-*targetversion*: The version that the exported solution supports.<br/> -*include*: Settings that should be included in the solution being exported.|`pac solution export --path c:\Users\Documents -- name SampleComponentSolution -- managed true -- targetversion 10.0.03 --include general`|

### Auth

Commands to [authenticate to Common Data Service](/powerapps/developer/component-framework/import-custom-controls#connecting-to-your-environment). It has the following parameters:

#### Parameters

|Parameter Name|Description|Example|
|-------------|-----------|-------|
|create| Creates the authentication profile for your organization by passing the `url` parameter. Pass the organization url for the `url` parameter.|`pac auth create --url https://Myorg.crm.dynamics.com`|
|list|Provides the list of authentication profiles.|`pac auth list`|
|select|Provides a way to switch between previously created authentication profiles by passing the `index` parameter.|`pac auth select --index 2`|
|delete|Deletes the authentication profile created by passing  the `index` parameter.|`pac auth delete --index 2`|
|clear|Clears all the authentication profile created on the local machine.|  `pac auth clear`|

### Telemetry

Manages the telemetry settings. It has the following parameters:

#### Parameters

|Parameter Name|Description|Example|
|------------|------------|---------|
|enable|Enables the telemetry option.|`pac telemetry enable`|
|disable|Disables the telemetry option.| `pac telemetry disable`|
|status|Returns whether the telemetry is enabled or disabled.|`pac telemetry status`|

### Org

Command to work with Common Data Service organizations.

#### Parameters

|Parameter Name|Description|Example|
|-------------|-----------|--------|
|who|Displays information about the current Common Data Service organizations.|`pac org who`|


### Plugin

Manages to create a [plug-in](/powerapps/developer/common-data-service/plug-ins) project.

#### Parameters

|Parameter Name|Description|Example|
|-------------|-----------|--------|
|init|Initializes a directory with a new plugin class library.|`pac plugin init`|


<!--|Command|Description|Examples|
|------|-----------|--------|
|**pcf**|Commands for working with [Power Apps component framework](/powerapps/developer/component-framework/overview). It has the following parameters: <br/> - **init**: Initializes the code component project. It has the following parameters <br/> - *namespace*: Namespace of the code component. <br/> - *name*: Name of the code component. <br/> - *template*: Field or dataset <br/> - **push**: Pushes the code component to the Common Data Service instance with all the latest changes. It has the following parameter: <br/> - *publisher-prefix*: Publisher prefix of the organization.<br/> - **Version**: Updates the component manifest file with the specified patch version. It has the following parameters: <br/> - *patchversion*: Patch version of the code component. `patchversion` will only take value of the third part of the version tuple: `Major.Minor.Patch`.<br/> - *path*: Absolute or relative path of the component manifest file.<br/> - *allmanifests*: Updates the patch version for all the component manifest files. <br/> - *strategy*: Updates patch version for the manifest files using specified strategy values.| `pac pcf init --namespace <specify your namespace here> --name <Name of the code component> --template <component type>` <br/> <br/> `pac pcf push --publisher-prefix <your publisher prefix>` <br/><br/> `pac pcf version --patchversion <number> --path <Absolute or relative path to component manifest file --allmanifests`  <br/><br/> `pac pcf version --strategy gittags`|
|**solution**|Commands for working with [Common Data Service solution projects](/powerapps/maker/common-data-service/solutions-overview). It has the following parameters: <br/> - **init**: Initializes the solution project. It has the following parameters:<br/>  - *publisher-name*: Publisher name of the organization. <br/>  - *publisher-prefix*: Publisher prefix of the organization. <br/> - **add-reference**: Sets the reference path to the component project folder by passing the `path` parameter.<br/> - **clone**: Creates a solution project based up on the existing solution project by passing the following parameters:<br/> -*name*: The name of the solution to be exported.<br/> -*targetversion*: The version that the exported solution supports.<br/> -*include*: Settings that should be included in the solution being exported.<br/> -**Export**: Exports a Common Data Service solution project from the current organization. It has the following parameters:<br/> -*path*: Place where the exported solution zip file will be saved.<br/> - *name*: Name oft he solution that needs to be exported.<br/> - *managed*: Defines whether the solution should be exported as a managed solution or not.<br/>-*targetversion*: The version that the exported solution supports.<br/> -*include*: Settings that should be included in the solution being exported.|`pac solution init --publisher-name <enter your publisher name> --publisher-prefix <enter your publisher prefix>` <br/><br/> `pac solution add-reference --path <path to your Power Apps component framework project>`<br/><br/> `pac solution clone –name<name of the solution to be exported> --version <version of your solution> --include <settings that should be included>`|
|**auth**|Commands to [authenticate to Common Data Service](/powerapps/developer/component-framework/import-custom-controls#connecting-to-your-environment). It has the following parameters: <br/> - **create**: Creates the authentication profile for your organization by passing the `url` parameter. Pass the organization url for the `url` parameter. <br/> - **list**: Provides the list of authentication profiles. <br/> - **select**: Provides a way to switch between previously created authentication profiles by passing the `index` parameter.<br/> - **delete**: Deletes the authentication profile created by passing  the `index` parameter.<br/> - **clear**: Clears all the authentication profile created on the local machine.|`pac auth create --url <your Common Data Service org’s url>` <br/> <br/> `pac auth list` <br/><br/> `pac auth select --index <index of the active profile>`<br/><br/> `pac auth clear`|
|**telemetry**|Manages the telemetry settings. It has the following parameters: <br/>- *enable*: Enables the telemetry option.<br/> - *disable*: Disables the telemetry option.<br/> - *status*: Returns whether the telemetry is enabled or disabled.|`pac telemetry enable` <br/><br/> `pac telemetry disable`|
|**org**|Command to work with Common Data Service.|`pac org who`|
|**plugin**|Manages to create a [plug-in](/powerapps/developer/common-data-service/plug-ins) project|`pac plugin init`|-->

## Uninstall Power Apps CLI

To uninstall the Power Apps CLI tooling, run the MSI from [here](https://aka.ms/PowerAppsCLI).

If you are a **Private Preview** participant and have an older version of CLI, follow these steps:

1. To find out where the Power Apps CLI is installed, open a command prompt and type `where pac`.

1. Delete the PowerAppsCLI folder.

1. Open the Environment Variables tool by running the command `rundll32 sysdm.cpl,EditEnvironmentVariables` in the command prompt.

1. Double-click `Path` under the `User variable for...` section.

1. Select the row containing the PowerAppsCLI path and select the **Delete** button on the right-hand side.

1. Select **OK** twice.


## See also

[Power Apps component framework](../component-framework/overview.md)
