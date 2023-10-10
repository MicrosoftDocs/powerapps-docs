---
title: Dependent Assembly plug-ins (preview)
description: Learn how to include more assemblies that your plug-in assembly can depend on.
ms.date: 08/08/2023
ms.reviewer: jdaly
ms.topic: article
author: divkamath
ms.subservice: dataverse-developer
ms.author: dikamath
search.audienceType: 
  - developer
contributors:
  - PHecke
  - JimDaly
---
# Dependent Assembly plug-ins (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

It's frequently valuable to include another assembly or a resource file within a plug-in. For example, you may want to use Newtonsoft.Json.dll or another assembly. You may want to access a list of localized strings.  

Without dependent assemblies, all plug-ins are registered as individual .NET Framework assemblies. The only way to include another assembly is to combine it into one using [ILMerge](https://github.com/dotnet/ILMerge). While ILMerge worked for many, Dataverse never supported it, and it didn't always work. ILMerge is no longer being maintained.

With dependent assemblies, rather than register an individual .NET assembly, you upload a NuGet Package that contains your plug-in assembly AND any dependent assemblies. This NuGet package file is stored in a new table called [PluginPackage](reference/entities/pluginpackage.md). The contents of the NuGet package is stored in file storage rather than SQL.

> [!IMPORTANT]
> - This is a preview feature.
> - Preview features aren't meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
>
> This document previously described a process to include additional files with the plug-in package that would be available in the assembly run-time. This capability will not be supported. We cannot guarantee that the runtime will allow access to these files.

When you upload your NuGet package, any assemblies that contain classes that implement the [IPlugin Interface](xref:Microsoft.Xrm.Sdk.IPlugin) are registered in [PluginAssembly](reference/entities/pluginassembly.md) table and associated with the `PluginPackage`. As you develop and maintain your project, you continue to update the `PluginPackage` and changes to the related plugin assemblies are managed on the server.

At runtime, Dataverse copies the contents of the NuGet package from the `PluginPackage` row and extracts it to the sandbox runtime. This way, any dependent assemblies needed for the plug-in are available.

You're still able to register plug-in assemblies individually, but using `PluginPackage` will become the recommended approach. Even if your current plug-in project doesn't require access to a dependent assembly, if you start with a project configured to support dependent assemblies you can add a dependent assembly later if you need to. There's no work planned to convert existing plug-in assembly projects to use `PluginPackage`.

## Send feedback

If you have questions or issues with this feature, you can contact technical support. If you have suggestions, post them on the [Power Apps Ideas Forum](https://ideas.powerapps.com/) site.

## Limitations

The following limitations apply to dependent assembly plug-ins.

- [Workflow extensions](workflow/workflow-extensions.md), also known as *workflow assemblies*, *workflow activities* or *custom workflow activities* aren't supported.
- Plug-ins for virtual table data providers aren't supported.
- On-premises environments aren't supported.
- Unmanaged code isn't supported. You can't include references to unmanaged resources.

## Signing Assemblies

You aren't required to sign plug-in assemblies used in plugin packages.

When you register individual plug-in assemblies without the dependent assemblies feature, signing is required because it provides a unique name for the assembly. But with plug-in assemblies within plug-in package, the assemblies are loaded on the sandbox server using a different mechanism, so signing isn't necessary.

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
|PAC CLI and Plug-in Registration tool (PRT)|Microsoft Power Platform CLI is a simple, one-stop developer CLI that empowers developers and ISVs to perform various operations in Microsoft Power Platform related to environment lifecycle, authentication, and work with Microsoft Dataverse environments, solution packages, portals, code components, and more.<br/><br/> PRT is a Windows application you can use to manage registering plug-in assemblies and register plug-in step registrations.<br /><br />See instructions in: [Use PAC CLI and PRT](#use-pac-cli-and-prt)|
|Use Power Platform Tools for Visual Studio|Power Platform Tools for Visual Studio supports the rapid creation, debugging, and deployment of plug-ins. Other capabilities include development of custom workflow activities, web resources, integration technologies like Azure Service endpoints and webhooks, and more. <br /><br />See instructions in: [Use Power Platform Tools for Visual Studio](#use-power-platform-tools-for-visual-studio)|


## Use PAC CLI and PRT

Use PAC CLI to create a Visual Studio project and PRT to manage your packages and register steps.

### Prerequisites

To use this feature with PAC CLI and PRT, you should use these tools and applications.

|Tool/App|Instructions |
|---------|---------|
|**Microsoft Power Platform CLI**|You must have version 1.17 or higher.<br />The preferred installation method is using Visual Studio Code. See [Power Platform Tools](https://aka.ms/ppcvscode).<br /><br />You can also download and install the Windows version here: [https://aka.ms/PowerAppsCLI](https://aka.ms/PowerAppsCLI).<br />If you have already installed the Windows version, make sure you run `pac install latest` to get the latest version.<br /><br />More information: [What is Microsoft Power Platform CLI?](/power-platform/developer/cli/introduction)|
|**PRT**|You should use version 9.1.0.184 or higher.<br /><br />Use these instructions to install the latest version: [Dataverse development tools](download-tools-nuget.md).|
|**Visual Studio**|We require Visual Studio 2019 or newer.|

### Create a Visual Studio project

Use the PAC CLI [pac plugin init](/power-platform/developer/cli/reference/plugin#pac-plugin-init) command to create a Visual Studio project that  streamlines your development process with dependent assemblies.

1. Create a folder for your plug-in project. The name of this folder determines the name of the Visual Studio .NET Framework Class library project for your plug-in.
1. Open a PowerShell terminal window in Visual Studio Code to navigate to the folder and run the command [pac plugin init](/power-platform/developer/cli/reference/plugin#pac-plugin-init). For plug-in packages, we recommend that you use the `--skip-signing` parameter so that your plug-in assemblies aren't signed.

   Example:
   ```powershell
   PS E:\projects\mypluginproject> pac plugin init --skip-signing
   ```

> [!NOTE]
> It is no longer required to sign the assemblies when using dependent assemblies. If you sign your assembly, all dependent assemblies must also be signed. More information: [Signing Assemblies](#signing-assemblies)
>
> The [pac plugin init](/power-platform/developer/cli/reference/plugin#pac-plugin-init) command has a number of optional parameters. You must use the [--skip-signing](/power-platform/developer/cli/reference/plugin#--skip-signing--ss) parameter if you do not want to sign your plug-in assembly.

These commands create a Visual Studio .NET Framework class library project based on the name of the folder it was created in.

Depending on your Visual Studio solution configuration, when you open the Visual Studio project in Visual Studio and build it, a NuGet package is generated for the project in the `bin\Debug` or `bin\Release` folder. Each time you build your project, this NuGet package is updated. The NuGet package is the file you upload using the Plug-in Registration tool.

### Add a dependent assembly using NuGet

You can add a NuGet Package to your Visual Studio project as you normally do. After you build the project, you should find the assembly in the NuGet package.

You can use [NuGet Package Explorer](https://www.microsoft.com/p/nuget-package-explorer/9wzdncrdmdm3) to examine the NuGet package.

### Add a dependent assembly without using NuGet

If you have an assembly that isn't distributed as a NuGet package, you can add it to your project as you normally do. In **Solution Explorer**, right-click **Dependencies** and choose **Add Assembly Reference...**. Select the assembly you want to add.

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

This command opens a dialog to select the plug-in package.

You can select an existing solution or create a new one.

:::image type="content" source="media/prt-import-new-plugin-package-dialog.png" alt-text="Dialog to import a new plug-in package.":::

From the **Display by Package** view, you can select the assembly and register steps.

:::image type="content" source="media/prt-new-plug-in package-view.png" alt-text="Showing a newly uploaded plug-in package in the Display by Package view.":::

The assembly is also available within the **Display by Assembly** view.

:::image type="content" source="media/prt-show-pluginpackage-assembly-display-by-assembly-view.png" alt-text="Showing the plugin package assembly in the Display by Assembly view.":::

#### Update a plugin package

While viewing the list of plugin packages using the **Display by Package** view, select the plugin package and select the **Update** command.

:::image type="content" source="media/prt-pluginpackage-update-command.png" alt-text="Showing the Update command while a plugin package is selected.":::

This command opens a dialog so you can select the NuGet Package with changes.

:::image type="content" source="media/prt-update-pluginpackage-dialog.png" alt-text="The update Plugin Package dialog.":::

> [!IMPORTANT]
> If your update removes any plug-in assemblies, or types which are used in plug-in step registrations, the update will be rejected. You must manually remove any step registrations that use plug-in assemblies or plugin types that you want to remove with your update.
>
> The version of the plug-in package or plug-in assembly is not a factor in any upgrade behaviors. You can update the versions of these items as you need.

#### Delete plugin packages

While viewing the list of plugin packages using the **Display by Package** view, select the plugin package and select the **Unregister** command.

:::image type="content" source="media/prt-pluginpackage-unregister-command.png" alt-text="Showing the Unregister command while a plugin package is selected.":::

> [!IMPORTANT]
> You cannot unregister a package that has any plug-in step registrations for any plug-in assemblies in the package. You must first unregister all step registrations for the assemblies in the package before you can delete the package.

## Use Power Platform Tools for Visual Studio

Use Power Platform Tools for Visual Studio create a Visual Studio project, manage your packages and register steps.

### Prerequisites

To use this feature with Power Platform Tools for Visual Studio, you must have Visual Studio 2019 and install Power Platform Tools for Visual Studio.

See the following articles related to installing and using Power Platform Tools for Visual Studio to work with plug-ins.

- [Install Power Platform Tools](tools/devtools-install.md)
- [Quickstart: Create a Power Platform Tools project](tools/devtools-create-project.md)
- [Quickstart: Create a plug-in using Power Platform Tools](tools/devtools-create-plugin.md)

You'll generally use the same process to create and manage plug-ins using Power Platform Tools for Visual Studio, however signing the assemblies is no longer required. More information: [Signing Assemblies](#signing-assemblies).

#### Enable Plugin Packages for Power Platform Tools

Power Platform Tools for Visual Studio provides several configuration options as described in [Power Platform Tools options](tools/devtools-install.md#power-platform-tools-options).

1. In Visual Studio, go to **Tools** > **Options** and search for **Power Platform tools**.
1. Select **Use nuget package for deploying Plugins to Dataverse**.

   :::image type="content" source="media/power-platform-tools-options.png" alt-text="Select Use NuGet package for deploying Plugins to Dataverse.":::

> [!NOTE]
> When this option is selected, all your plug-in projects will be deployed with Plug-in packages.

#### Add a dependent assembly using NuGet with Power Platform Tools

You can add a NuGet Package to your Visual Studio project as you normally do. After you build the project, you should find the assembly in the NuGet package. The NuGet package is in the `bin\outputPackages` folder.

You can use [NuGet Package Explorer](https://www.microsoft.com/p/nuget-package-explorer/9wzdncrdmdm3) to examine the NuGet package.

#### Add a dependent assembly without using NuGet with Power Platform Tools

If you have an assembly that isn't distributed as a NuGet package, you can add it to your project as you normally do. In **Solution Explorer**, right-click **Dependencies** and choose **Add Assembly Reference...**. Select the assembly you want to add.

#### Deploy Plugin Packages for Power Platform Tools

To deploy your plug-in package, in **Solution Explorer** right-click the plug-in project and select **Deploy** from the context menu.

:::image type="content" source="media/power-platform-deploy-pluginpackage.png" alt-text="foo":::

When you deploy for the first time, you should see a message in the output window that informs you that the plug-in package was created:

```
6/22/2022 3:03:17 PM : registration of Plugin Package sample_PowerPlatformVSSolution.ExamplePlugins, 
at E:\projects\PowerPlatformVSSolution\ExamplePlugins\bin\outputPackages\PowerPlatformVSSolution.ExamplePlugins.1.0.0.nupkg was successful. 
ID allotted was 06a20e15-77f2-ec11-bb3c-000d3a892245.
```

Each time you deploy after that, you'll see a message in the output window that informs you that the plug-in package was updated.

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
> However, you can create a new plug-in package from a Nuget package using the following steps.

1. Within the Power Platform Explorer, select **Plug-in Packages** and select **Create** from the context menu.

   :::image type="content" source="media/power-platform-create-pluginpackage.png" alt-text="Within the Power Platform Explorer, select Plug-in Packages and select Create from the context menu.":::

1. This command opens the **Import new Plugin package** dialog.

   :::image type="content" source="media/power-platform-create-pluginpackage-dialog.png" alt-text="The **Import new Plugin package dialog":::

   Select the NuGet package and choose which solution it should be added to, or create a new solution.

#### Update a Plugin Package with Power Platform Tools

> [!NOTE]
> As mentioned in [Deploy Plugin Packages for Power Platform Tools](#deploy-plugin-packages-for-power-platform-tools), you will not typically have to update a plug-in package in the usual flow of creating a plug-in. It will be updated automatically each time you deploy the plug-in while the **Use nuget package for deploying Plugins to Dataverse** option is set in Visual Studio.
> However, you can update a new plug-in package from a Nuget package using the steps below.

Within the **Power Platform Explorer**, select a plug-in package and select **Update** from the context menu.

:::image type="content" source="media/power-platform-update-pluginpackage.png" alt-text="Select a plug-in package and select Update from the context menu":::

This command opens a dialog so you can select a NuGet package to update the plug-in package.

## Design notes

The Visual Studio project created using [pac plugin init](/power-platform/developer/cli/reference/plugin#pac-plugin-init) uses Visual Studio capabilities that enable generating NuGet Packages. This method uses the [SDK-style](/nuget/resources/check-project-format) project format. Power Platform Tools for Visual Studio uses the [Non-SDK-style](/nuget/resources/check-project-format) project format.

You aren't required to use these tools to generate a NuGet package with your plug-ins. You can use whatever capabilities you choose to generate a NuGet package, but you must use the tooling available to upload the package to Dataverse.

More information:

- [Create a NuGet package using MSBuild](/nuget/create-packages/creating-a-package-msbuild)
- [NuGet pack and restore as MSBuild targets](/nuget/reference/msbuild-targets)


## Using System.Text.Json

If you use [System.Text.Json](xref:System.Text.Json), pay special attention to explicitly add a reference to the [System.Text.Json NuGet package](https://www.nuget.org/packages/System.Text.Json/).

With dependent assemblies, you must include NuGet package dependencies for any external libraries you use. Including these dependencies is required so that you can refer to those types at design time. Your class library project must also include a reference to the [Microsoft.CrmSdk.CoreAssemblies NuGet package](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies) so that you can refer to essential interfaces to write your plug-in.

Because the [Microsoft.CrmSdk.CoreAssemblies NuGet package has a dependency on System.Text.Json](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies#dependencies-body-tab), you're able to refer to `System.Text.Json` types at design time without explicitly adding the `System.Text.Json` NuGet package. However, the `System.Text.Json` NuGet package isn't included in your plug-in package due to this indirect dependency. You must explicitly add it as a first level dependency for your plug-in package.

Currently, `System.Text.Json` is the only dependency in the Microsoft.CrmSdk.CoreAssemblies NuGet package. This guidance will be true if any other  new dependencies are added in the future.


## FAQ

### Q: Can I continue to use ILMerge?

**A**: We have never supported ILMerge. This dependent assemblies feature provides a solution we can support with the same functionality and more. But nothing else has changed. If ILMerge works for you, you can continue to use it. We recommend using dependent assemblies because we can support this solution.

## Known issues

The following are known issues that should be resolved before dependent assemblies for plug-ins becomes generally available.

### Custom API export key changes

When importing a solution that contains a custom API that uses a plug-in package, you may encounter the following error:

`Lookup value <plugintypeexportkey>{guid value}</plugintypeexportkey> is not resolvable.`

This error occurs only for solutions that were exported/generated before May 2023. The exact date varies by region. The fix to this issue was deployed to North America region on May 26, 2023.

To resolve this issue you need to update the plug-in package, export/generate the solution and reinstall it.

More information: [Set a relation to a plug-in type (optional)](create-custom-api-solution.md#set-a-relation-to-a-plug-in-type-optional)

### Plug-in profiler

To debug plug-ins that are part of a plug-in package, you must:

1. Use the latest version of the Plug-in Registration tool (PRT). Version 9.1.0.184 or higher.

   Use the pac CLI [pac tool prt](/power-platform/developer/cli/reference/tool#pac-tool-prt) command with the `--update` switch to update.

1. In the folder that contains the PRT, edit the `appsettings.json` file. Set `LegacyPluginProfiler` to `false`.

   If you have installed using pac CLI, the folder should be:
   
   `C:\Users\<you>\AppData\Local\Microsoft\PowerPlatform\PRT\9.1.0.184\tools`

More information:

- [pac tool prt](/power-platform/developer/cli/reference/tool#pac-tool-prt)
- [Use Plug-in profiler](debug-plug-in.md#use-plug-in-profiler)

### See also

[Use plug-ins to extend business processes](plug-ins.md)<br />
[PAC CLI pac plugin init](cli/reference/plugin-command.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
