---
title: Microsoft Power Platform CLI solution command| Microsoft Docs
description: "Includes descriptions and supported parameters for the solution command."
keywords: Microsoft Power Platform CLI, code components, component framework, CLI
ms.subservice: dataverse-developer
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 09/15/2021
ms.service: "powerapps"
ms.topic: "article"
---

# Solution

Commands for working with [Dataverse solution projects](../../maker/data-platform/solutions-overview.md).

## Parameters

|Property Name|Description|Example|
|-------------|-----------|-------|
|add-license|Add license and plan info the solution. It has the following parameters: <ul><li>*planDefinitionFile*: License plan definition file in CSV format; expected columns: *Service ID, Display name, More info URL* (alias: -pd)</li><li>*planMappingFile*: License plan mapping file in CSV format; expected values: *Service ID, Component name* (alias: -pm)</li></ul>|
|add-reference|Sets the reference path to the component project folder by passing the `path` parameter.|`pac solution add-reference --path c:\Users\Downloads\SampleComponent`|
|check|Perform static analysis check on the solutions against a set of best practices. It has the following parameters: <ul><li> *path*: Path to the solution zip file (alias: -p).</li><li> *outputDirectory*: Output directory where the solution zip file should be stored (alias: -o).</li><li> *geo*: The geographical location of the environment where the solution checker should run. It has the following values: *PreviewUnitedStates, UnitedStates,Europe, Asia, Australia, Japan, India, Canada, SouthAmerica, UnitedKingdom, France, Germany, UnitedArabEmirates, Switzerland, USGovernment, USGovernmentL4, USGovernmentL5DoD, China*</li><li> *ruleLevelOverride*: Path to the file containing a JSON array rules and levels to override. It has the following values: *Critical, High, Low, Medium, Informational*|`pac solution check --path c:\Users\Documents\Solution.zip --outputDirectory c:\samplepackage --geo UnitedStates`|
|clone|Creates a solution project based on the existing solution project. It has the following parameters:<ul><li>*name*: The name of the solution to be exported.</li><li>*targetversion*: The version that the exported solution supports.</li><li>*include*: Settings that should be included in the solution being exported. It has the following values: *autonumbering, calendar, customization, emailtracking, externalapplications, general, isvconfig, marketing, outlooksynchronization, relationshiproles, sales*</li></ul>|`pac solution clone -–name  sampleSolution --version 1.0.0.2 --include general`|
|create-settings|Provides the ability to create a settings file that captures the environment variables and connection references in the setting. It has the following parameters: <ul><li>*solution zip*: Absolute path name or relative path name to the exported solution file (alias: -z).</li><li>*solution folder*: Folder location of the cloned solution on the filesystem, you can either use solution zip file or the solution folder location, not both together (alias: -f).</li><li> *settings file*: Location of the file to be created with the environment variable and connection reference information. The format of the created file is JSON (alias: -s).</li></ul>|`pac solution create-settings --solution-zip C:\SampleSolution.zip --settings-file .\SampleDeploymentSettingsDev.json`|
|export|Exports a Dataverse solution from an environment. It requires that you be connected to an environment [Auth commands](#auth), and has the following parameters:<ul><li>*path*: Complete file name where the exported solution .zip file will be saved.</li><li>*name*: Name of the solution that needs to be exported.</li><li>*managed*: Defines whether the solution should be exported as a managed solution.</li><li>*targetversion*: The version that the exported solution supports.</li><li>*include*: Settings that should be included in the solution being exported.</li></ul>|`pac solution export --path c:\Users\Documents\Solution.zip --name SampleComponentSolution --managed true --targetversion 10.0.03 --include general`|
|import|Imports a Dataverse solution to an environment. It requires that you be connected to an environment [Auth commands](#auth), and has the following parameters:<ul><li>*activate-plugins*: Activates plug-ins and workflows in the environment after the import (alias: -ap).</li><li>*async*: Imports the solution asynchronously (alias: -a).</li><li>*force-overwrite*: Forces an overwrite of unmanaged customizations (alias: -f). </li><li>*import-as-holding*: Imports the solution as a holding solution (alias: -h).</li><li>*max-async-wait-time*: Maximum asynchronous wait time in minutes. Default value is 60 minutes (alias: -wt).</li><li>*path*: Path to the solution .zip file. If not specified, assumes the current folder (alias: -p).</li><li>*publish-changes*: Publishes changes after successful import (alias: -pc). </li><li>*skip-dependency-check*: Skips the dependency check against dependencies flagged as product update (alias: -s). </li><li>*convert-to-managed*: Converts the solution as managed upon import.</li></ul>|`pac solution import --path c:\Users\Documents\Solution.zip `|
|init|Initializes the solution project.  It has the following parameters:<ul><li>*publisher-name*: Publisher name of the organization.</li><li> *publisher-prefix*: Publisher prefix of the organization.</li></ul>|`pac solution init --publisher-name developer --publisher-prefix dev`  |
|list|Lists all solutions from a Dataverse environment. It requires that you be connected to an environment [Auth commands](#auth). This command has no parameters.|`pac solution list`  |
|pack|Provides the ability to pack files on a filesystem into a solution zip file. It has the following parameters: <ul><li>*zip file*: Absolute path name or relative path name to the generated solution zip file (alias: -z).</li><li>*folder*: The path to the root folder on the local filesystem, this will be the folder from where the contents will be read from (alias: -f).</li><li> *package type*: Use to specify dual managed and unmanaged operation (alias: -p).</li> <li> *log*: The path to the log file (alias: -l).</li><li> *error level*: Minimum logging level for log output. It has the following values: *Verbose, Info, Warning, Error, Off*. Default value is *Info* (alias: -e).</li><li> *single Component*: Performs the action on a single component type. It has the following values: *WebResource, Plugin, Workflow, None*. Default value is *None* (alias: -sc).</li><li> *allow Delete*: Specifies if the delete operations should occur or not. It has the following values: *Yes, No, Prompt*. Default is *Prompt* (alias: -ad).</li><li> *allow Write*: Specifies if the write operations should occur or not. Default value is false (alias: -aw).</li><li> *clobber*: Enables to delete or overwrite the files that are marked as read-only. Default value is false (alias: -c).</li><li> *map*: The full path to the mapping XML file that reads component folders to pack (alias: -m).</li><li> *sourceLoc*: Generates a template resource file. It has the following values: *auto, LCID, ISO code* of the language you wish to export. When set, this will extract the string resources from the given locale as a neutral resx file. If auto or just the long or short form of the switch is specified the base locale for the solution will be used (alias: -src).</li><li> *localize*: Extract or merge all string resources into `.resx` files (alias: -loc)</li><li> *use Lcid*: Use LCID's (1033) rather than ISO codes (en-US) for language files (alias: -lcid).</li><li> *use Unmanaged File for Missing Managed*: Use the same XML source file when packaging for managed and only unmanaged XML file is found. Applies to `AppModuleSiteMap`, `AppModuleMap`, `FormXml` files (alias: -same).</li></ul>|`pac solution pack --solution-zip C:\SampleSolution.zip --folder .\SampleSolutionUnpacked\.`|
|publish|Publishes all the customizations.|`pac solution publish`|
|unpack|Provides the ability to unpack solution zip files after they have been exported to the filesystem. It has the following parameters: <ul><li>*zip file*: Absolute path name or relative path name to the exported solution file (alias: -z).</li><li>*folder*: The path to the root folder on the local filesystem. This will be the folder where the unpacked contents will be written (alias: -f).</li><li> *package type*: Use to specify dual managed and unmanaged operation (alias: -p).</li> <li> *log*: The path to the log file (alias: -l).</li><li> *error level*: Minimum logging level for log output. It has the following values: *Verbose, Info, Warning, Error, Off*. Default value is *Info* (alias: -e).</li><li> *single Component*: Performs the action on a single component type. It has the following values: *WebResource, Plugin, Workflow, None*. Default value is *None* (alias: -sc).</li><li> *allow Delete*: Specifies if the delete operations should occur or not. It has the following values: *Yes, No, Prompt*. Default is *Prompt* (alias: -ad).</li><li> *allow Write*: Specifies if the write operations should occur or not. Default value is false (alias: -aw).</li><li> *clobber*: Enables to delete or overwrite the files that are marked as read-only. Default value is false (alias: -c).</li><li> *map*: The full path to the mapping XML file that reads component folders to pack (alias: -m).</li><li> *sourceLoc*: Generates a template resource file. It has the following values: *auto, LCID, ISO code* of the language you wish to export. When set, this will extract the string resources from the given locale as a neutral resx file. If auto or just the long or short form of the switch is specified the base locale for the solution will be used (alias: -src).</li><li> *localize*: Extract or merge all string resources into `.resx` files (alias: -loc)</li><li> *use Lcid*: Use LCID's (1033) rather than ISO codes (en-US) for language files (alias: -lcid).</li><li> *use Unmanaged File for Missing Managed*: Use the same XML source file when packaging for managed and only unmanaged XML file is found. Applies to `AppModuleSiteMap`, `AppModuleMap`, `FormXml` files (alias: -same).</li></ul>|`pac solution unpack --solution-zip C:\SampleSolution.zip --folder .\SampleSolutionUnpacked\.`|
|upgrade|Command to upgrade the solution. It has the following parameters: <ul><li> *solution-name*: Name of the solution (alias:-sn).</li><li> *async*: Upgrades the solution asynchronously (alias: -a).</li><li>*max-async-wait-time*: Maximum asynchronous wait time in minutes. Default value is 60 minutes (alias: -wt).</li></ul>|`pac solution upgrade --solution-name SampleSolution --async --max-async-wait-time 60`|
|version|Updates the version of the existing solution. It has the following parameters:<ul><li>*patchversion*: Patch version of the solution (alias: -pv).</li><li> *strategy*: Updates patch version for `Solution.xml` file using specified strategy. It has the following values: <ul><li>*gittags*: Use Git tags to decide whether a particular solution's patch version needs to be updated. Set the personal access token in the `PacCli.PAT` environment variable (alias: -s).</li><li>*filetracking*: Use a .csv file to decide whether a particular solution's patch version needs to be updated.</li><li>*solution*: The solution file whose patch version should be updated.</li></ul><li> *filename*: CSV file name to be used when using `filetracking` as a stategy. Default value is `ControlStateVersionInfo.csv` (alias: -fn).|`pac solution version --patchversion 1.0.0.0`  <br/><br/> `pac solution version --strategy gittags`|




## Differences between pac solution clone and export

There are situations where you're unsure when to use `pac solution clone` or `pac solution export` command. You can use one of the commands in the following scenarios:

- Use `pac solution clone` when you need to add new components to the solution.
- Use `pac solution export` when you want to modify the existing content in a solution file but not adding any new components to the solution.

**pac solution clone**

The exported solution looks like a Visual Studio project when you export the solution using the `pac solution clone` command. Instead of a `.csproj` (as in Visual Studio), you'll see a `cdsproj` file. The `cdsproj` file has all the components information that is required to build the project. The build output is a solution zip file which you can import into different environments.

:::image type="content" source="media/pac-solution-clone.png" alt-text="Pac solution clone." lightbox="media/pac-solution-clone.png":::

The developer does not have to unpack the cloned solution because it is rendered in an unpacked format within the src (source) folder. 

:::image type="content" source="media/pac-solution-unpack.png" alt-text="Pac solution unpack." lightbox="media/pac-solution-unpack.png":::

Now, if you want to associate a newly created plug-in with this solution, with the solution unpacked, you can use the `pac solution add-reference` command to update the `.cdsproj` file to add the new plug-in. Then, you can build the project using either `dotnet build` or `msbuild`. 
   
It is recommended to do a build restore first before building the project. A build restore (dotnet build does a restore first automatically) will restore the required .NET libraries to generate a packed solution.

**pac solution export**

When you export the solution using `pac solution export` you feel like exporting the solution using the maker portal, and the resulting output is a solution zip file.  

:::image type="content" source="media/pac-solution-export.png" alt-text="Pac solution export." lightbox="media/pac-solution-export.png":::

When you unpack the solution zip file (we do not recommend that you open the zip with standard tools and use the appropriate command from CLI). The resulting directory structure  is similar to the structure in `pac solution clone`. The only difference is that you cannot add references to this unpacked solution, as it doesn't have the `.cdsproj` project file. 

:::image type="content" source="media/pac-solution-structure.png" alt-text="Pac solution solution structure." lightbox="media/pac-solution-structure.png":::

You can modify the relevant set of files that you want to update and then proceed with the solution pack, which generates the solution zip file again to facilitate importing the solution into the target environment. The result from the action is a solution zip file with updated contents and an updated timestamp.

### See also

[Power Apps component framework overview](../../../component-framework/overview.md)

[What is Microsoft Power Platform CLI](../../powerapps-cli.md)