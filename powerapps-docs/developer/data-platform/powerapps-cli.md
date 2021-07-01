---
title: Microsoft Power Platform CLI | Microsoft Docs
description: "Install Microsoft Power Platform CLI to create, debug, and deploy code components using Power Apps component framework."
keywords: Microsoft Power Platform CLI, code components, component framework, CLI
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 06/14/2021
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: f393f227-7a88-4f25-9036-780b3bf14070
---

# What is Microsoft Power Platform CLI? 

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

> [!NOTE] 
> Effective June 2021, *Microsoft Power Apps CLI* is rebranded to *Microsoft Power Platform CLI*. More information: [Blog: Microsoft Power Platform is the best way for teams to build together](https://cloudblogs.microsoft.com/powerplatform/2021/05/25/microsoft-power-platform-is-the-best-way-for-teams-to-build-together/).

Microsoft Power Platform CLI is a simple, single-stop developer command-line interface that empowers developers and ISV to perform various operations in Microsoft Power Platform related to environment lifecycle features, authenticate and work with Dataverse environments, solution packages, portals, code components, and so on.  

## Install Microsoft Power Platform CLI

To get Microsoft Power Platform CLI, do the following:

1. Install [Microsoft Power Platform CLI](https://aka.ms/PowerAppsCLI).
1. To take advantage of all the latest capabilities, update Microsoft Power Platform CLI tooling to the latest version using this command (not applicable for Visual Studio Code Extension):

    ```CLI
    pac install latest
    ```


> [!NOTE]
> - Currently, Microsoft Power Platform CLI is supported only on Windows 10.
> - Power Platform Extension for Visual Studio Code is in public preview and works on both Windows 10 and macOS. 

## Install Power Platform Extension for Visual Studio Code

You can also install the [Power Platform Extension for Visual Studio Code](https://aka.ms/ppcvscode) which installs Microsoft Power Platform CLI for use within Visual Studio Code. The Power Platform extension makes it easy to manage Power Platform environments and allows the developer to create, build packages, deploy solutions, and portals.

> [!IMPORTANT]
> - Power Platform Extension for Visual Studio Code is in public preview. 
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - Microsoft Power Platform CLI version that is included with this extension may also be a public preview version. We recommend you to install the latest version using the steps mentioned above.

## Common commands

This table lists some of the common commands used in the CLI:

|Command|Description|
|-------|-----------|
|[admin](#admin)|Commands for environment lifecycle features.|
|[auth](#auth)|Commands to [authenticate to Dataverse](../component-framework/import-custom-controls.md#connecting-to-your-environment).|
|[canvas](#canvas)|Commands for working with canvas app source files.|
|[org](#org)|Commands for working with Dataverse environment.|
|[package](#package)|Commands for working with [Solution Packages](/power-platform/alm/package-deployer-tool).|
|[paportal](#paportal)|Commands for working with [Power Apps portals (Preview)](../../maker/portals/power-apps-cli.md).|
|[pcf](#pcf)|Commands to work with [Power Apps component framework](../component-framework/overview.md).|
|[plugin](#plugin)|Command to create a [plug-in](./plug-ins.md) project.|
|[solution](#solution)|Commands for working with [Microsoft Dataverse solution projects](../../maker/data-platform/solutions-overview.md).|
|[telemetry](#telemetry)|Manages the telemetry settings.|


### Admin

Commands to work with environment lifecycle features. It has the following parameters:

#### Parameters

|Property Name|Description|
|-------------|-----------|
|list|Lists all environments from the tenant. It has the following parameters <br/> - *environment-id*: List all environments that contain a given string in their ID (alias: -id). <br/> - *url*: List all environments that contain a given string in their url (alias -u). <br/> - *type*: Lists all environments of the given type (alias: -t). <br/>  -  *name*: List all environments that contain a given string in their name (alias: -n). <br/> -  *organization-id*: List all environments that contain a given string in their organization ID (alias: -oi). |
|create|Creates a new environment. It has the following parameters: <br/> - *name*: Sets the name of the environment (alias: -n).<br/> - *region*: Sets the environment's region name. Defaults to `unitedstates` if not specified (alias -r). <br/> - *type*: Sets the type of the environment. Available values are Trial, Sandbox, Production, SubscriptionBasedTrial (alias: -t).<br/> - *currency*: Sets the default currency used in the environment. Defaults to USD if not specific (alias: -c).<br/> - *language*: Sets the default language of the environment. Defaults to english if not specified (alias: -l).<br/> - *templates*: Sets the Dynamics 365 apps that should be deployed to the environment. Pass as comma-separated values (alias: -t).<br/> - *domain*: Sets the domain name that is part of the environment URL. If domain name is already in use, a numeric value will be appended to the domain name. For example, if `contoso` is already in use, then the environment URL will become `https://contoso0.crm.dynamics.com` (alias -d). <br/> - *input-file*: Arguments can be passed in a `.json` input file instead of through the command line. For example, {"name" : "contoso"}. The arguments passed through command-line will take precedence over arguments from the `.json` input file (alias: -if). |
|backup|Takes the backup of an environment. It has the following parameters: <br/> - *url*: Url of the environment to be backed up. (alias: -u).<br/> - *label*: Sets the backup label as provided (alias: -l). <br/> - *environment-id*: ID of the environment to be backed up (alias: -id).<br/> - *notes*: Additional notes provided for the backup (alias: -n). |
|delete|Deletes an environment. It has the following parameters: <br/> - *url*: Url of the environment to be deleted (alias: -u). <br/> - *environment-id*: ID of the environment to be deleted (alias: -id).|
|reset|Resets an environment. It has the following parameters: <br/> - *url*: Url of the environment to reset (alias: -u) <br/> - *name*: Sets the name of the environment (alias: -n).<br/> - *currency*: Sets the default currency used in the environment. Defaults to USD if not specific (alias: -c)<br/>- *purpose*: Sets the description used to associate the environment with a specific intent (alias: -p) <br/> - *language*: Sets the default language of the environment. Defaults to english if not specified (alias: -l).<br/> - *templates*: Sets the Dynamics 365 apps that should be deployed to the environment. Pass as comma-separated values (alias: -t).<br/> - *domain*: Sets the domain name that is part of the environment URL. If domain name is already in use, a numeric value will be appended to the domain name. For example, if `contoso` is already use, then the environment URL will become `https://contoso0.crm.dynamics.com` (alias -d). <br/> - *input-file*: Arguments can be passed in a `.json` input file instead of through the command line. For example, {"name" : "contoso"}. The arguments passed through command-line will take precedence over arguments from the `.json` input file (alias: -if).|
|list-backups|Lists all available backups. environment. It has the following parameters: <br/> - *url*: Url of the environment for which you want to list backups (alias: -u). <br/> - *environment-id*: ID of the environment for which you want to list backups (alias: -id).|
|restore|Restores an environment from a given backup. It has the following parameters: <br/> - *source-url*: Url of the source environment to be restored from (alias: -s). <br/> - *target-url*: Url of the target environment to be restored to (alias: -t). <br/> - *selected-backup*: DateTime of the backup in `mm/dd/yyyy hh:mm` format or latest (alias: -sb). <br/> - *name*: Optional name of the restored environment (alias: -n).|
|copy|Copies a source environment to a destination environment. It has the following parameters: <br/> - *source-url*: Url of the source environment to be copied from (alias: -su). <br/> - *target-url*: Url of the target environment to be copied to (alias: -tu). <br/> - *source-environment-id*: ID of the source environment to be copied from (alias: -si). <br/> - *target-environment-id*: Id of the target environment to be copied to (alias: -ti). <br/> - *name*: Name to be used for the target environment. (alias: -n).  <br/> - *type*: Type of copy. Available values are: None, MinimalCopy, Fullcopy  (alias: -t).|

### Canvas

Commands for working with canvas app source files. Edit, manage, and collaborate on your app outside of Power Apps Studio with tools such as VS Code and GitHub.

> [!NOTE]
> The Canvas commands are in public preview. They may not be available in the version of Microsoft Power Platform CLI that you are using currently. 

#### Parameters

|Property Name|Description|Example|
|-------------|-----------|-------|
| unpack | Unpacks the `.msapp`  source file.<br/> Download the `.msapp` file from Power Apps Studio by navigating to **File** > **Save as** > **This computer**.<br/>  If the **sources** parameter is not specified, a directory with the same name and location as the `.msapp` file is used with `_src` suffix.  | `pac canvas unpack --msapp HelloWorld.msapp --sources MyHelloWorldFiles`<br/>`pac canavs unpack --msapp HelloWorld.msapp`<br/>*unpacks to default* `HelloWorld_src` *directory* |
| pack | Creates an `.msapp` file from the previously unpacked source files. <br/>The result can be opened in Power Apps Studio by navigating to **File** > **Open** > **Browse**.<br/> The source files can be edited and managed with external tools after being unpacked, such as Visual Studio Code and GitHub. | `pac canvas pack --sources MyHelloWorldFiles --msapp HelloWorld.msapp` |

#### Folder structure

Unpack and pack use the following folder structure:

- **\src** - Control and component files. This contains the sources.
   - ***\*.fx.yaml*** - The formulas extracted from the `control.json` file.  *This is the place to edit your formulas.*
   - ***CanvasManifest.json*** - A manifest file that contains the information normally present in the header, properties, and publishInfo.
   - ***\*.json*** - The raw `control.json` file.
   - ***\EditorState\*.editorstate.json*** - Cached information for studio to use.
- **\DataSources** - All the data sources used by the app.
- **\Connections** - Connection instances saved with the app and used when reloading into the studio. 
- **\Assets** - Media files embedded in the app.
- **\pkgs** - A downloaded copy of external references, such as templates, API definition files, and component libraries. These are similar to NuGet/NPM references. 
- **\other** - All miscellaneous files needed to recreate the `.msapp`.
   - ***entropy.json*** - Volatile elements (like timestamps) are extracted to this file. This helps reduce noisy differences in other files while ensuring that we can still round trip.
   - Holds other files from the msapp, such as what is in \references.

#### File format

The `.fx.yaml` files uses a subset of [YAML](https://yaml.org/spec/1.2/spec.html). Similar to Excel, all the expressions should begin with an `=` sign. More information: [Power Fx YAML Formula Grammar](/power-platform/power-fx/yaml-formula-grammar).

#### Merging changes with Power Apps Studio

When merging changes, that are made in two different studio sessions:

- Ensure that all the control names are unique. For example, inserting a button in two different sessions can result in two `Button1` controls. We recommend to name the controls soon after you create them. The tool doesn't accept two controls with the same name.  
- For these files, merge them as you normally do:
   - \src\*.fx.yaml
- If there are conflicts or errors, you can delete these files:
   - \src\editorstate\*.json  - These files contain optional information in studio.
   - \other\entropy.json  
- For any conflict in these files, it’s ok to accept the latest version: 
   - \checksum.json
- If there are any merge conflicts under these paths, it is not safe to merge. Let us know if this happens often and we will work on restructuring the file format to avoid conflicts.
   - \Connections\*
   - \DataSources\*
   - \pkgs\*
   - CanvasManifest.json

#### Open source

The canvas commands in Microsoft Power Platform CLI are open source. Discuss improvements, raise issues, and access the code from [Power Apps language tooling repository](https://github.com/microsoft/PowerApps-Language-Tooling).

### Package

Command to work with solution packages. It has the following parameters:

#### Parameters

|Property Name|Description|Example|
|-------------|-----------|-------|
|init|Initializes a new package project. It has the following parameter: <br/> - *outputdirectory*: Output directly where the package is created.| `pac package init --outputdirectory c:\samplepackage`|
|add-reference|Sets the reference path to the solution project folder by passing the `path` parameter.|`pac package add-reference --path c:\Users\Downloads\SampleSolution`|
|show| Shows the content of a package dll or a zip file with a package. <br/> It has the following parameter: <br/> - *package*: The path location to the package dll (library) or the zip file.| `pac package show c:\samplepackage.dll`|
|deploy| Deployes the package dll or the zip file with a package. <br/> It has the following parameters: <br/> - *logFile*:  Path to a log file location where the logs are redirected.  <br/> - *logConsole*: This option is used if you want to direct the logs to the console. <br/> - *package*: The path location to the package dll (library) or a zip file with a package.  <br/> **Note**: You can use both `logFile` and `logConsole` parameters together or use one parameter or the other. | `pac package deploy --logFile c:\samplelogdata --package c:\samplepackage`

### Paportal

Commands to work with [Power Apps portals (Preview)](../../maker/portals/power-apps-cli.md). It has the following parameters:

#### Parameters

|Property Name|Description|Example|
|-------------|-----------|-------|
|list|Lists all portal websites from the current Dataverse environment. |`pac paportal list`|
|download|Download portal website content from the current Dataverse environment. It has the following parameters: <br/> - *path*: Path where the website content will be downloaded (alias: -p).<br/> - *webSiteId*: Portal website ID to download (alias: -id).<br/> - *overwrite*: (Optional) true - to overwrite existing content, false - to fail if the folder already has website content (alias: -o).|`pac paportal download --path "C:\portals" --webSiteId f88b70cc-580b-4f1a-87c3-41debefeb902`|
|upload|Upload portal website content to the current Dataverse environment. It has the following parameter: <br/> - *path*: Path where the website content is stored (alias: -p)|`pac paportal upload --path "C:\portals\starter-portal"`|

### PCF

Commands to work with [Power Apps component framework](../component-framework/overview.md). It has the following parameters:

#### Parameters

|Property Name|Description|Example|
|-------------|-----------|-------|
|init|Initializes the code component project. It has the following parameters: <br/> - *namespace*: Namespace of the code component. <br/> - *name*: Name of the code component. <br/> - *template*: Field or dataset| `pac pcf init --namespace SampleNameSpace --name SampleComponent --template field`|
|push|Pushes the code component to the Dataverse instance with all the latest changes. It has the following parameter: <br/> - *publisher-prefix*: Publisher prefix of the organization.|`pac pcf push --publisher-prefix dev`|
|version|Updates the component manifest file with the specified patch version. It has the following parameters: <br/> - *patchversion*: Patch version of the code component. `patchversion` will only take value of the third part of the version tuple: `Major.Minor.Patch`.<br/> - *path*: Absolute or relative path of the component manifest file.<br/> - *allmanifests*: Updates the patch version for all the component manifest files. <br/> - *updatetarget*: Updates the specified manifest file. It has two values, build and project.<br/> - *strategy*: Updates patch version for the manifest files using specified strategy values. It has the following values: <br/> - *gittags*: Use git tags to decide if a particular component’s patch version needs to be updated.<br/> *filetracking*: Use .csv file to decide if a particular component’s patch version needs to be updated. <br/> - *manifest*: Increments the patch version by 1 for all the components.|`pac pcf version --patchversion 1.0.0.0 --path c:\Users\Downloads\SampleComponent --allmanifests`  <br/><br/> `pac pcf version --strategy gittags`|


### Solution

Commands for working with [Dataverse solution projects](../../maker/data-platform/solutions-overview.md). It has the following parameters:

#### Parameters

|Property Name|Description|Example|
|-------------|-----------|-------|
|init|Initializes the solution project.  It has the following parameters:<br/>  - *publisher-name*: Publisher name of the organization. <br/>  - *publisher-prefix*: Publisher prefix of the organization.|`pac solution init --publisher-name developer --publisher-prefix dev`  |
|add-reference|Sets the reference path to the component project folder by passing the `path` parameter.|`pac solution add-reference --path c:\Users\Downloads\SampleComponent`|
|clone|Creates a solution project based up on the existing solution project. It has the following parameters:<br/> -*name*: The name of the solution to be exported.<br/> -*targetversion*: The version that the exported solution supports.<br/> -*include*: Settings that should be included in the solution being exported. <br/> It has the following values: autonumbering, calendar, customization, emailtracking, externalapplications, general, isvconfig, marketing, outlooksynchronization, relationshiproles, sales|`pac solution clone -–name  sampleSolution --version 1.0.0.2 --include general`|
|import|Imports a Dataverse solution to an environment. It requires that you are connected to an environment [Auth commands](#auth) and has the following parameters:<br/>  -*activate-plugins*: Activates plug-ins and workflows in the environment after the import (alias: -ap). <br/>  -*async*: Imports the solution asynchronously (alias: -a). <br/>  -*force-overwrite*: Forces an overwrite of unmanaged customizations (alias: -f). <br/>  -*import-as-holding*: Imports the solution as a holding solution (alias: -h). <br/>  -*max-async-wait-time*: Maximum asynchronous wait time in minutes. Default value is 60 mintues (alias: -wt). <br/>  -*path*: Path to solution zip file. If not specified, assumes the current folder (alias: -p). <br/>  -*publish-changes*: Publishes changes after successful import (alias: -pc). <br/>  -*skip-dependency-check*: Skips dependency check against dependencies flagged as product update (alias: -s). <br/> - *convert-to-managed*: convert the solution as managed upon import|`pac solution import --path c:\Users\Documents\Solution.zip `|
|export|Exports a Dataverse solution from an environment. It requires that you are connected to an environment [Auth commands](#auth) and has the following parameters:<br/> -*path*: Complete file name where the exported solution zip file will be saved.<br/> - *name*: Name of the solution that needs to be exported.<br/> - *managed*: Defines whether the solution should be exported as a managed solution or not.<br/>-*targetversion*: The version that the exported solution supports.<br/> -*include*: Settings that should be included in the solution being exported.|`pac solution export --path c:\Users\Documents\Solution.zip -- name SampleComponentSolution --managed true --targetversion 10.0.03 --include general`|
|list|List all Solutions from a Dataverse environment. It requires that you are connected to an environment [Auth commands](#auth). This command has no parameters.|`pac solution list`  |


### Auth

Commands to [authenticate to Dataverse](../component-framework/import-custom-controls.md#connecting-to-your-environment). It has the following parameters:

#### Parameters

|Parameter Name|Description|Example|
|-------------|-----------|-------|
|create| Creates the authentication profile for your organization by passing the `url` parameter. Shows AAD dialog if log in credentials are not specified.<br/>It has the following arguments:<br/>  -*name*: The name to give to this auth profile, max 12 characters (alias: -n). <br/>  -*kind*: Kind of auth profile, defaults to Dataverse (alias: -k). <br/>  -*url*: Resource URL to connect to (alias: -u). <br/>  -*username*: Optional: username to authenticate with (alias: -un). <br/>  -*password*: Optional: password to authenticate with (alias: -p). <br/>  -*applicationId*: Optional: application id to authenticate with (alias: -id). <br/>  -*clientSecret*: Optional: client secret to authenticate with (alias: -cs). <br/>  -*tenant*: Optional: tenant id if using app id & secret (alias: -t). <br/>  -*cloud*: Optional: cloud instance to authenticate with. Values: Public, Tip1, Tip2, UsGov, UsGovHigh, UsGovDod (alias: -ci). <br/>|`pac auth create --url https://Myorg.crm.dynamics.com`|
|list|Provides the list of authentication profiles stored on current computer. This command has no arguments.|`pac auth list`|
|select|Provides a way to switch between previously created authentication profiles by passing the `index` parameter.<br/>It has the following arguments:<br/>  -*index*: The index of the profile to be active (alias: -i). <br/>  -*name*: The name of the profile to be active (alias: -n).|`pac auth select --index 2`|
|delete|Deletes the authentication profile created by passing  the `index` parameter.<br/>It has the following arguments:<br/>  -*index*: The index of the profile to be deleted (alias: -i). <br/>  -*name*: The name of the profile to be deleted (alias: -n).|`pac auth delete --index 2`|
|clear|Clears all the authentication profile created on the local machine. This command has no arguments.|  `pac auth clear`|

### Telemetry

Manages the telemetry settings. It has the following parameters:

#### Parameters

|Parameter Name|Description|Example|
|------------|------------|---------|
|enable|Enables the telemetry option.|`pac telemetry enable`|
|disable|Disables the telemetry option.| `pac telemetry disable`|
|status|Returns whether the telemetry is enabled or disabled.|`pac telemetry status`|

### Org

Command to work with Dataverse organizations.

#### Parameters

|Parameter Name|Description|Example|
|-------------|-----------|--------|
|who|Displays information about the current Dataverse organizations.|`pac org who`|


### Plugin

Manages to create a [plug-in](./plug-ins.md) project.

#### Parameters

|Parameter Name|Description|Example|
|-------------|-----------|--------|
|init|Initializes a directory with a new plugin class library.|`pac plugin init`|

## Uninstall Microsoft Power Platform CLI 

To uninstall Microsoft Power Platform CLI tooling, run the MSI from [here](https://aka.ms/PowerAppsCLI).

If you are a **Private Preview** participant and have an older version of CLI, follow these steps:

1. To find out where Microsoft Power Platform CLI is installed, open a command prompt and type `where pac`.

1. Delete the PowerAppsCLI folder.

1. Open the Environment Variables tool by running the command `rundll32 sysdm.cpl,EditEnvironmentVariables` in the command prompt.

1. Double-click `Path` under the `User variable for...` section.

1. Select the row containing the PowerAppsCLI path and select the **Delete** button on the right-hand side.

1. Select **OK** twice.


## See also

[Power Apps component framework](../component-framework/overview.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
