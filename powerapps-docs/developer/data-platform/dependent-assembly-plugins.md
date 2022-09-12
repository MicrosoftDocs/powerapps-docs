---
title: "Dependent Assembly plug-ins (preview) (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to include additional assemblies that your plug-in assembly can depend on." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 08/23/2022
ms.reviewer: jdaly
ms.topic: article
author: divka78 # GitHub ID
ms.subservice: dataverse-developer
ms.author: dikamath # MSFT alias of Microsoft employees only
manager: sunilg # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - PHecke
  - JimDaly
---
# Dependent Assembly plug-ins (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

It is frequently valuable to include another assembly or a resource file within a plug-in. For example, you may want to use Newtonsoft.Json.dll or another assembly. You may want to access a list of localized strings.  

Without dependent assemblies, all plug-ins are registered as individual .NET Framework assemblies. The only way to include another assembly is to combine it into one using [ILMerge](https://github.com/dotnet/ILMerge). While ILMerge worked for many, it was never supported by Dataverse and it didn't always work. ILMerge is no longer being maintained.

With dependent assemblies, rather than register an individual .NET assembly, you will upload a NuGet Package that contains your plug-in assembly AND any dependent assemblies. Unlike ILMerge, you can also include other file resources, such as JSON files containing localized strings. This NuGet package file is stored in a new table called [PluginPackage](reference/entities/pluginpackage.md). The contents of the NuGet package is stored in file storage rather than SQL.

> [!IMPORTANT]
> - This is a preview feature.
> - Preview features aren't meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - This feature is being gradually rolled out across regions and might not be available yet in your region.

When you upload your NuGet package, any assemblies that contain classes that implement the <xref:Microsoft.Xrm.Sdk.IPlugin?text=IPlugin Interface> will be registered in [PluginAssembly](reference/entities/pluginassembly.md) table and associated with the `PluginPackage`. As you develop and maintain your project, you will continue to update the `PluginPackage` and changes to the related plugin assemblies will be managed on the server.

At runtime, Dataverse copies the contents of the NuGet package from the `PluginPackage` row and extracts it to the sandbox runtime. This way, any dependent assemblies needed for the plug-in are available.

You will still be able to register plug-in assemblies individually, but using `PluginPackage` will become the recommended approach. Even if your current plug-in project doesn't require access to a dependent assembly, if you start with a project configured to support dependent assemblies you will be able to add a dependent assembly later. There is no work planned to convert existing plug-in assembly projects to use `PluginPackage`.

## Send feedback

If you have questions or issues with this feature you can contact technical support. If you have suggestions please post them on the [Power Apps Ideas](https://powerusers.microsoft.com/t5/Power-Apps-Ideas/idb-p/PowerAppsIdeas) site.

## Limitations

The following limitations apply to dependent assembly plug-ins.

- A plugin package is limited to 16 MB in size or 50 assemblies.
- [Workflow extensions](workflow/workflow-extensions.md), also known as *workflow assemblies*, *workflow activities* or *custom workflow activities* are not supported.
- On-premises environments are not supported.

## Signing Assemblies

You are not required to sign plug-in assemblies used in plugin packages.

When registering individual plug-in assemblies without the dependent assemblies feature, signing is required because it provides a unique name for the assembly. But with plug-in assemblies within plug-in package, the assemblies are loaded on the sandbox server using a different mechanism, so signing is not necessary.

> [!NOTE]
> If you sign your assemblies, be aware that signed assemblies cannot use resources contained in unsigned assemblies. If you sign your plug-in assemblies or any dependent assembly, all the assemblies that those assemblies depend on must be signed. If any signed assemblies depend on unsigned assemblies, you will get an error like the following: `Could not load file or assembly '<AssemblyName>, Version=<Version>, Culture=neutral, PublicKeyToken=null' or one of its dependencies. A strongly-named assembly is required.`
>
> When you use the Microsoft Power Platform CLI (pac cli), the default settings will sign the assembly for you. You must opt out of signing by using the `--skip-signing` parameter. More information: [Create a Visual Studio project](#create-a-visual-studio-project).
>
> Power Platform Tools will not sign your plug-in assembly for you.

## Tooling options

You can use this feature with two tooling options:


|Tools  |Overview|
|---------|---------|
|PAC CLI and Plug-in Registration tool (PRT)|Microsoft Power Platform CLI is a simple, one-stop developer CLI that empowers developers and ISVs to perform various operations in Microsoft Power Platform related to environment lifecycle, authentication, and work with Microsoft Dataverse environments, solution packages, portals, code components, and more.<br/><br/> PRT is a Windows application you can use to manage registering plug-in assemblies and register plug-in step registrations.<br /><br />See instructions below: [Use PAC CLI and PRT](#use-pac-cli-and-prt)|
|Use Power Platform Tools for Visual Studio|Power Platform Tools for Visual Studio supports the rapid creation, debugging, and deployment of plug-ins. Other capabilities include development of custom workflow activities, web resources, integration technologies like Azure Service endpoints and webhooks, and more. <br /><br />See instructions below: [Use Power Platform Tools for Visual Studio](#use-power-platform-tools-for-visual-studio)|


## Use PAC CLI and PRT

Use PAC CLI to create a Visual Studio project and PRT to manage your packages and register steps.

### Prerequisites

To use this feature with PAC CLI and PRT, you should use these tools and applications.

|Tool/App|Instructions |
|---------|---------|
|**Microsoft Power Platform CLI**|You must have version 1.17 or higher.<br />The preferred installation method is using Visual Studio Code. See [Power Platform Tools](https://aka.ms/ppcvscode).<br /><br />You can also download and install the Windows version here: [https://aka.ms/PowerAppsCLI](https://aka.ms/PowerAppsCLI).<br />If you have already installed the Windows version, make sure you run `pac install latest` to get the latest version.<br /><br />More information: [What is Microsoft Power Platform CLI?](/power-platform/developer/cli/introduction)|
|**PRT**|You should use version 9.1.0.155 or higher.<br /><br />Use these instructions to install the latest version: [Download tools from NuGet](download-tools-nuget.md).|
|**Visual Studio**|We require Visual Studio 2019 or newer.|

### Create a Visual Studio project

Use the PAC CLI [pac plugin init](/power-platform/developer/cli/reference/plugin#pac-plugin-init) command to create a Visual Studio project that will streamline your development process with dependent assemblies.

1. Create a folder for your plug-in project. The name of this folder will determine the name of the Visual Studio .NET Framework Class library project for your plug-in.
1. Open a PowerShell terminal window in Visual Studio Code to navigate to the folder and run the command [pac plugin init](/power-platform/developer/cli/reference/plugin#pac-plugin-init). For plug-in packages we recommend that you use the `--skip-signing` parameter so that your plug-in assemblies are not signed.

   Example:
   ```powershell
   PS E:\projects\mypluginproject> pac plugin init --skip-signing
   ```

> [!NOTE]
> It is no longer required to sign the assemblies when using dependent assemblies. If you sign your assembly, all dependent assemblies must also be signed. More information: [Signing Assemblies](#signing-assemblies)
>
> The [pac plugin init](/power-platform/developer/cli/reference/plugin#pac-plugin-init) command has a number of optional parameters. You must use the [--skip-signing](/power-platform/developer/cli/reference/plugin#--skip-signing--ss) parameter if you do not want to sign your plug-in assembly.

You will find a Visual Studio .NET Framework class library project created based on the name of the folder it was created in.

Depending on your Visual Studio solution configuration, when you open the Visual Studio project in Visual Studio and build it, you will find a NuGet package generated for the project in the `bin\Debug` or `bin\Release` folder. Each time you build your project, this NuGet package will be updated. This is the file you will upload using the Plug-in Registration tool.

### Add a dependent assembly using NuGet

You can add a NuGet Package to your Visual Studio project as you normally do. After you build the project, you should find the assembly in the NuGet package.

You can use [NuGet Package Explorer](https://www.microsoft.com/p/nuget-package-explorer/9wzdncrdmdm3) to examine the NuGet package.

### Add a dependent assembly without using NuGet

If you have an assembly that is not distributed as a NuGet package, you can add it to your project as you normally do. In **Solution Explorer**, right-click **Dependencies** and choose **Add Assembly Reference...**. Select the assembly you want to add.

### Add a file resource

To include another file resource that will be available in the runtime for your plug-in.

1. Add the file to your Visual Studio project.
1. Set the **Copy to Output Directory** property of the file to **Copy if newer**.

   :::image type="content" source="media/add-dependent-file-or-assembly.png" alt-text="Adding a file to the Visual Studio project.":::

If you view the csproj file, you will find that an `ItemGroup` like following will be added by Visual Studio:

```xml
<ItemGroup>
  <None Update="strings.localized.json">
    <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
  </None>
</ItemGroup> 
```

The file will be included with the NuGet package. You can verify by using NuGet Package Explorer.

### Use the Plug-in Registration tool

You can use the Plug-in Registration tool (PRT) to perform the following tasks:

1. View list of available plugin packages.
1. Register a NuGet package as a plugin package.
1. Update a plugin package.
1. Delete plugin packages.

#### View list of available plugin packages

PRT has a new **Display by Package** view to list any plug-in packages previously imported:

:::image type="content" source="media/prt-display-by-package-view.png" alt-text="View a list of plug-in packages using the plug-in registration tool.":::

#### Register a NuGet package as a plugin package

PRT has a new command to select a NuGet package to import/register as a plug-in package.

:::image type="content" source="media/prt-register-new-package-command.png" alt-text="Command to register a plug-in package using the plug-in registration tool.":::

This will open a dialog to select the plug-in package.

You have the option to select an existing solution or create a new one.

:::image type="content" source="media/prt-import-new-plugin-package-dialog.png" alt-text="Dialog to import a new plug-in package.":::

From the **Display by Package** view, you can select the assembly and register steps.

:::image type="content" source="media/prt-new-plug-in package-view.png" alt-text="Showing a newly uploaded plug-in package in the Display by Package view.":::

The assembly is also available within the **Display by Assembly** view.

:::image type="content" source="media/prt-show-pluginpackage-assembly-display-by-assembly-view.png" alt-text="Showing the pluginpackage assembly in the Display by Assembly view.":::

#### Update a plugin package

While viewing the list of plugin packages using the **Display by Package** view, select the plugin package and click the **Update** command.

:::image type="content" source="media/prt-pluginpackage-update-command.png" alt-text="Showing the Update command while a plugin package is selected.":::

This opens a dialog to allow you to select the NuGet Package with changes.

:::image type="content" source="media/prt-update-pluginpackage-dialog.png" alt-text="The update Plugin Package dialog.":::

> [!IMPORTANT]
> If your update removes any plug-in assemblies, or types which are used in plug-in step registrations, the update will be rejected. You must manually remove any step registrations that use plug-in assemblies or plugin types that you want to remove with your update.
>
> The version of the plug-in package or plug-in assembly is not a factor in any upgrade behaviors. You can update the versions of these items as you need.

#### Delete plugin packages

While viewing the list of plugin packages using the **Display by Package** view, select the plugin package and click the **Unregister** command.

:::image type="content" source="media/prt-pluginpackage-unregister-command.png" alt-text="Showing the Unregister command while a plugin package is selected.":::

> [!IMPORTANT]
> Unregistering a package will delete the package, all assemblies within it, all plug-ins within the assembly, and any plug-in step registrations for the plug-ins.

## Use Power Platform Tools for Visual Studio

Use Power Platform Tools for Visual Studio create a Visual Studio project, manage your packages and register steps.

### Prerequisites

To use this feature with Power Platform Tools for Visual Studio, you must have Visual Studio 2019 and install Power Platform Tools for Visual Studio.

See the following topics related to installing and using Power Platform Tools for Visual Studio to work with plug-ins.

- [Install Power Platform Tools](tools/devtools-install.md)
- [Quickstart: Create a Power Platform Tools project](tools/devtools-create-project.md)
- [Quickstart: Create a plug-in using Power Platform Tools](tools/devtools-create-plugin.md)

You will generally use the same process to create and manage plug-ins using Power Platform Tools for Visual Studio, however signing the assemblies is no longer required. More information: [Signing Assemblies](#signing-assemblies).

#### Enable Plugin Packages for Power Platform Tools

Power Platform Tools for Visual Studio provides several configuration options as described in [Power Platform Tools options](tools/devtools-install.md#power-platform-tools-options).

1. In Visual Studio, go to **Tools** > **Options** and search for **Power Platform tools**.
1. Select **Use nuget package for deploying Plugins to Dataverse**.

   :::image type="content" source="media/power-platform-tools-options.png" alt-text="Select Use nuget package for deploying Plugins to Dataverse.":::

> [!NOTE]
> When this option is selected, all your plug-in projects will be deployed with Plug-in packages.

#### Add a dependent assembly using NuGet with Power Platform Tools

You can add a NuGet Package to your Visual Studio project as you normally do. After you build the project, you should find the assembly in the NuGet package. The nuget package will be in the `bin\outputPackages` folder

You can use [NuGet Package Explorer](https://www.microsoft.com/p/nuget-package-explorer/9wzdncrdmdm3) to examine the NuGet package.

#### Add a dependent assembly without using NuGet with Power Platform Tools

If you have an assembly that is not distributed as a NuGet package, you can add it to your project as you normally do. In **Solution Explorer**, right-click **Dependencies** and choose **Add Assembly Reference...**. Select the assembly you want to add.

#### Add a file resource with Power Platform Tools

To include another file that will be available in the runtime for your plug-in.

1. Add the file to your Visual Studio project.
1. Set the **Copy to Output Directory** property of the file to **Copy if newer**.

   :::image type="content" source="media/power-platform-add-strings.localized.json.png" alt-text="Set the Copy to Output Directory property of the file to Copy if newer":::

If you unload the project file and view csproj file, you will find that an `ItemGroup` like following will be added by Visual Studio:

```xml
<ItemGroup>
  <None Update="strings.localized.json">
    <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
  </None>
</ItemGroup> 
```

#### Deploy Plugin Packages for Power Platform Tools

To deploy your plug-in package, in **Solution Explorer** right-click the plug-in project and select **Deploy** from the context menu.

:::image type="content" source="media/power-platform-deploy-pluginpackage.png" alt-text="foo":::

When you deploy for the first time, you should see a message in the output window that informs you that the plug-in package was created:

```
6/22/2022 3:03:17 PM : registration of Plugin Package sample_PowerPlatformVSSolution.ExamplePlugins, 
at E:\projects\PowerPlatformVSSolution\ExamplePlugins\bin\outputPackages\PowerPlatformVSSolution.ExamplePlugins.1.0.0.nupkg was successful. 
ID allotted was 06a20e15-77f2-ec11-bb3c-000d3a892245.
```

Each time you deploy after that, you will see a message in the output window that informs you that the plug-in package was updated.

```
6/22/2022 3:20:14 PM : update of Plugin Package sample_PowerPlatformVSSolution.ExamplePlugins, at
E:\projects\PowerPlatformVSSolution\ExamplePlugins\bin\outputPackages\PowerPlatformVSSolution.ExamplePlugins.1.0.0.nupkg was successful.

```
> [!IMPORTANT]
> If your update removes any plug-in assemblies, or types which are used in plug-in step registrations, the update will be rejected. You must manually remove any step registrations that use plug-in assemblies or plugin types that you want to remove with your update.
>
> The version of the plug-in package or plug-in assembly is not a factor in any upgrade behaviors. You can update the versions of these items as you need.

#### View Plugin Packages with Power Platform Tools

Within the Power Platform Explorer, you can view available plug-in packages.

:::image type="content" source="media/power-platform-explorer-plug-in-packages.png" alt-text="Within the Power Platform Explorer, you can view available plug-in packages":::


#### Delete a Plugin Package with Power Platform Tools

Within the Power Platform Explorer, select a plug-in package and select **Delete** from the context menu.

:::image type="content" source="media/power-platform-delete-pluginpackage.png" alt-text="Select a plug-in package and select Delete from the context menu":::

> [!IMPORTANT]
> Deleting a package will delete the package, all assemblies within it, all plug-ins within the assembly, and any plug-in step registrations for the plug-ins.

#### Create a Plugin Package with Power Platform Tools

> [!NOTE]
> As mentioned in [Deploy Plugin Packages for Power Platform Tools](#deploy-plugin-packages-for-power-platform-tools), you will not typically have to create a plug-in package in the usual flow of creating a plug-in. It will be created automatically the first time you deploy the plug-in while the **Use nuget package for deploying Plugins to Dataverse** option is set in Visual Studio.
> However, you can create a new plug-in package from a Nuget package using the steps below. 

1. Within the Power Platform Explorer, select **Plug-in Packages** and select **Create** from the context menu.

   :::image type="content" source="media/power-platform-create-pluginpackage.png" alt-text="Within the Power Platform Explorer, select Plug-in Packages and select Create from the context menu.":::

1. This will open the **Import new Plugin package** dialog.

   :::image type="content" source="media/power-platform-create-pluginpackage-dialog.png" alt-text="The **Import new Plugin package dialog":::

   Select the NuGet package and choose which solution it should be added to, or create a new solution.

#### Update a Plugin Package with Power Platform Tools

> [!NOTE]
> As mentioned in [Deploy Plugin Packages for Power Platform Tools](#deploy-plugin-packages-for-power-platform-tools), you will not typically have to update a plug-in package in the usual flow of creating a plug-in. It will be updated automatically each time you deploy the plug-in while the **Use nuget package for deploying Plugins to Dataverse** option is set in Visual Studio.
> However, you can update a new plug-in package from a Nuget package using the steps below.

Within the **Power Platform Explorer**, select a plug-in package and select **Update** from the context menu.

:::image type="content" source="media/power-platform-update-pluginpackage.png" alt-text="Select a plug-in package and select Update from the context menu":::

This will open an dialog to allow you to select a nuget package to update the plug-in package.

## Design notes

The Visual Studio project created using [pac plugin init](/power-platform/developer/cli/reference/plugin#pac-plugin-init) leverages Visual Studio capabilities that enable generating NuGet Packages. This method uses the [SDK-style](/nuget/resources/check-project-format) project format. Power Platform Tools for Visual Studio uses the [Non-SDK-style](/nuget/resources/check-project-format) project format.

You are not required to use these tools to generate a NuGet package with your plug-ins. You can use whatever capabilities you choose to generate a NuGet package, but you must use the tooling available to upload the package to Dataverse.

More information:

- [Create a NuGet package using MSBuild](/nuget/create-packages/creating-a-package-msbuild)
- [NuGet pack and restore as MSBuild targets](/nuget/reference/msbuild-targets)

## FAQ

### Q: Can I continue to use ILMerge?

**A**: We have never supported ILMerge. This dependent assemblies feature provides a solution we can support with the same functionality and more. But nothing else has changed. If ILMerge works for you, you can continue to use it. We recommend using dependent assemblies because we can support this solution.

## Known issues

You cannot use Plug-in Profiler to debug plug-ins that are part of a plug-in package.

### See also

[Use plug-ins to extend business processes](plug-ins.md)<br />
[PAC CLI pac plugin init](cli/reference/plugin-command.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
