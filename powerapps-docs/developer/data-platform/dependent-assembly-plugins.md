---
title: "Dependent Assembly plug-ins (preview) (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to include additional assemblies that your plug-in assembly can depend on." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 06/03/2022
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

It is frequently valuable to include another assembly within a plug-in. For example, you may want to use Newtonsoft.Json.dll or another assembly.  

Today, without dependent assemblies, all plug-ins are registered as individual .NET Framework assemblies. The only way to include another assembly is to combine it into one using [ILMerge](https://github.com/dotnet/ILMerge). While ILMerge worked for many, it was never supported by Dataverse and it didn't always work. ILMerge is no longer being maintained.

With dependent assemblies, rather than register an individual .NET assembly, you will upload a NuGet Package that contains your plug-in assembly AND any dependent assemblies. This NuGet package file is stored in a new table called [PluginPackage](reference/entities/pluginpackage.md).

When you upload your NuGet package, any assemblies that contain classes that implement the <xref:Microsoft.Xrm.Sdk.IPlugin?text=IPlugin Interface> will be registered in [PluginAssembly](reference/entities/pluginassembly.md) table and associated with the `PluginPackage`. As you develop and maintain your project, you will continue to update the `PlugPackage` and changes to the related plugin assemblies will be managed on the server.

At runtime, the contents of the NuGet package is copied from the `PluginPackage` row and extracted to the sandbox runtime. This way, any dependent assemblies needed for the plug-in are available.

You will still be able to register plug-in assemblies individually, but using `PluginPackage` will become the recommended approach. Even if your current plug-in project doesn't require access to a dependent assembly, if you start with a project configured to support dependent assemblies you will be able to add a dependent assembly later. There is no work planned to convert existing plug-in assembly projects to use `PluginPackage`.

## Send feedback

<!-- Need to provide people with a way to send feedback. Ideas site? -->

## Limitations

The following limitations apply to dependent assembly plug-ins.

- [Workflow extensions](workflow/workflow-extensions.md), also known as *workflow assemblies*, *workflow activities* or *custom workflow activities* are not supported.
- On-premises environments are not supported.

## Prerequisites

To use this feature, you should use these tools and applications.

|Tool/App|Instructions |
|---------|---------|
|**Microsoft Power Platform CLI**|The preferred installation method is using Visual Studio Code. See [Power Platform Tools](https://aka.ms/ppcvscode).<br /><br />You can also download and install the stand-alone version here: [https://aka.ms/PowerAppsCLI](https://aka.ms/PowerAppsCLI).<br />If you have already installed the stand-alone version, make sure you run `pac install latest` to get the latest version.<br /><br />More information: [What is Microsoft Power Platform CLI?](powerapps-cli.md)|
|**Plug-in Registration tool (PRT)**|You should use version X.X.<br /><br />Use these instructions to install the latest version: [Download tools from NuGet](download-tools-nuget.md).|
|**Visual Studio**|We recommend Visual Studio 2019 or newer|

## Create a Visual Studio project

Use the PAC CLI `pac plugin init` command to create a Visual Studio project that will streamline your development process with dependent assemblies.

1. Create a folder for your plug-in project. The name of this folder will determin the name of the Visual Studio .NET Framework Class library project for your plug-in.
1. Open a PowerShell terminal window in Visual Studio Code to navigate to the folder and run the command `pac plugin init`.

You will find a Visual Studio .NET Framework class library project created based on the name of the folder it was created in.

Depending on your Visual Studio solution configuration, when you open the Visual Studio project in Visual Studio and build it, you will find a NuGet package generated for the promect in the bin\Debug or bin\Release folder. Each time you build your project, this NuGet package will be updated. This is the file you will upload using the Plug-in Registration tool.

> [!NOTE]
> It is no longer required to sign the assemblies when using dependent assemblies. But in .NET, signed assemblies cannot use resources contained within unsigned assemblies, so you may still want to sign your assemblies.


## Add a dependent assembly using NuGet

You can add a NuGet Package to your Visual Studio project as you normally do. After you build the project, you should find the assembly in the NuGet package.

You can use [NuGet Package Explorer](https://www.microsoft.com/p/nuget-package-explorer/9wzdncrdmdm3) to examine the NuGet package.

## Add another dependent file or assembly

To include another file or assembly that will be available in the runtime for your plug-in.

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

## Use the Plug-in Registration tool

You can use the Plug-in Registration tool (PRT) to perform the following tasks:

1. View list of available plugin packages.
1. Register a NuGet package as a plugin package.
1. Update a plugin package.
1. Delete plugin packages.

### View list of available plugin packages

PRT has a new **Display by Package** view to list any plug-in packages previously imported:
<!-- TODO: Update all screenshots -->
:::image type="content" source="media/prt-display-by-package-view.png" alt-text="View a list of plug-in packages using the plug-in registration tool.":::

### Register a NuGet package as a plugin package

PRT has a new command to select a NuGet package to import/register as a plug-in package.

:::image type="content" source="media/prt-register-new-package-command.png" alt-text="Command to register a plug-in package using the plug-in registration tool.":::

This will open a dialog to select the plug-in package.

You have the option to select an existing solution or create a new one.

:::image type="content" source="media/prt-import-new-plugin-package-dialog.png" alt-text="Dialog to import a new plug-in package.":::

From the **Display by Package** view, you can select the assembly and register steps.

:::image type="content" source="media/prt-new-plug-in package-view.png" alt-text="Showing a newly uploaded plug-in package in the Display by Package view.":::

The assembly is also available within the **Display by Assembly** view.

:::image type="content" source="media/prt-show-pluginpackage-assembly-display-by-assembly-view.png" alt-text="Showing the pluginpackage assembly in the Display by Assembly view.":::

### Update a plugin package

While viewing the list of pluginpackages using the **Display by Package** view, select the pluginpackage and click the **Update** command.

:::image type="content" source="media/prt-pluginpackage-update-command.png" alt-text="Showing the Update command while a pluginpackage is selected.":::

This opens a dialog to allow you to select the NuGet Package with changes.

:::image type="content" source="media/prt-update-pluginpackage-dialog.png" alt-text="The update Plugin Package dialog.":::

> [!IMPORTANT]
> If your update removes any plug-in assemblies, or types which are used in plug-in step registrations, the update will be rejected. You must manually remove any step registrations that use plug-in assembies or plugin types that you want to remove with your update.
>
> The version of the plug-in package or plug-in assembly is not a factor in any upgrade behaviors. You can update the versions of these items as you need.
<!-- Impact for 1P teams b/c they work in solutions the whole removal cannot be done in one solution upgrade, they will need to wait until their next release to actuall remove the unused assembly or type. -->


### Delete plugin packages

While viewing the list of pluginpackages using the **Display by Package** view, select the pluginpackage and click the **Unregister** command.

:::image type="content" source="media/prt-pluginpackage-unregister-command.png" alt-text="Showing the Unregister command while a plugin package is selected.":::

> [!IMPORTANT]
> Unregistering a package will delete the package, all assemblies within it, all plug-ins within the assembly, and any plug-in step registrations for the plug-ins.


## Design notes

<!-- Think David J/ Andrew should provide this: This section should describe the details of the design so that advanced users can understand what they can or cannot do.
Assuming that this is all built using MS technologies, we can have links to any concepts -->
### See also

[Use plug-ins to extend business processes](plug-ins.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
