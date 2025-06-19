---
title: "Dataverse development tools (Microsoft Dataverse) | Microsoft Docs"
description: "Download and launch the Plug-in Registration, Package Deployment, and other Dataverse development tools."
ms.date: 05/27/2025
ms.reviewer: pehecke
ms.topic: article
author: davidjenni # GitHub ID
ms.subservice: "dataverse-developer"
ms.author: davidjen
---

# Dataverse development tools

There are many tools for developers you can use for different aspects of Microsoft Dataverse code development. The following table describes them briefly. Instructions to install and launch the tools are found in the next section that follows the table.

|Tool|Description|Documentation|
|-|-|-|
|Configuration Migration tool (CMT)|Transport configuration and test data from one environment to another|[Configuration Migraton tool](/power-platform/alm/configure-and-deploy-tools)|
|Package Deployer (PD)|Deploy packages to Dataverse environments where the packages contain solutions, custom code, HTML files, and more|[Deploy a package](/power-platform/alm/package-deployer-tool#deploy-a-package)|
|Plug-in Registration tool (PRT)|Registers custom code (plug-ins, custom workflow activities), service endpoints, and more|[Register a plug-in](register-plug-in.md)<br/>[Tutorial: Write and register a plug-in](tutorial-write-plug-in.md)|
|SolutionPackager tool (SP)|A tool that can reversibly decompose a Dataverse compressed solution file into multiple XML files and other files so that a source control system can manage these files|[SolutionPackager tool](/power-platform/alm/solution-packager-tool)|
|Code Generation tool (CG)|`CrmSvcUtil.exe` is a command-line code generation tool for use with Dynamics 365 Customer Engagement (on-premises) and Dataverse. You can use it to generate early-bound (strong-typed) .NET Framework classes that represent the Entity Data Model (EDM) used by Dataverse, but we recommend you use the [Power Platform CLI pac modelbuilder build command](/power-platform/developer/cli/reference/modelbuilder#pac-modelbuilder-build) instead.<br/><br/>`pac modelbuilder build` is capable of generating classes that support .NET Framework and cross-platform .NET (Core) compilation. [Learn more about using pac modelbuilder build to create early-bound classes for the SDK for .NET](org-service/generate-early-bound-classes.md)|[Use CrmSvcUtil.exe to generate early-bound classes for the SDK for .NET](/dynamics365/customerengagement/on-premises/developer/org-service/create-early-bound-entity-classes-code-generation-tool)|

> [!NOTE]
> The CMT, PD, and PRT tools provide a Windows (WPF) user interface and only run on a Microsoft Windows operating system. Also, the `pac tool` command only is available on a Windows install of the CLI.

All the above mentioned tools, except the Code Generation tool, are described in this article.

## Download and launch tools using Power Platform CLI

Follow these instructions to download and launch the Dataverse development tools.

> [!NOTE]
> The Dataverse tools are not longer available individually by a direct download. The tools are now distributed in several NuGet packages.
> We provide a Power Platform CLI command to download the correct package, extract and launch each tool, and update the installed tools.

You need version 1.19.3 (or newer) of [Power Platform CLI](/power-platform/developer/cli/introduction) installed on your computer to follow along with these instructions.
Start by using the Power Platform CLI to get help on the tools.

```bash
> pac tool help

Microsoft PowerPlatform CLI
Version: 1.19.3

Help: 
Power Platform tools that can be installed and launched

Commands: 
Usage: pac tool [list] [prt] [cmt] [pd]

  list                        List the launchable tools and their local install state and version.
  prt                         Launch Plug-in Registration Tool (PRT)
  cmt                         Launch Configuration Migration Tool (CMT)
  pd                          Launch Package Deployer (PD)
```

More information: [pac tool](/power-platform/developer/cli/reference/tool)

Now let's see what tools are installed.

```bash
> pac tool list

ToolName Installed Version Nuget     Status
CMT      No        N/A     9.1.0.80  not yet installed; 'pac tool CMT' will install on first launch
PD       No        N/A     9.1.0.104 not yet installed; 'pac tool PD' will install on first launch
PRT      No        N/A     9.1.0.155 not yet installed; 'pac tool PRT' will install on first launch
```

No tools are installed in the above example. They are installed on first launch. More information: [pac tool list](/power-platform/developer/cli/reference/tool#pac-tool-list)

Let's download and launch PRT.

```bash
> pac tool prt

Installing 9.1.0.155 version of PRT....
Shortcut in start menu created for 'Plugin Registration Tool'
Installation complete
Launched PRT (9.1.0.155).
```

More information: [pac tool prt](/power-platform/developer/cli/reference/tool#pac-tool-prt)

Now our tool list looks like this.

```bash
> pac tool list

ToolName Installed Version   Nuget     Status
CMT      No        N/A       9.1.0.80  not yet installed; 'pac tool CMT' will install on first launch
PD       No        N/A       9.1.0.104 not yet installed; 'pac tool PD' will install on first launch
PRT      Yes       9.1.0.155 9.1.0.155 ok
```

Follow the same procedure to download and launch the CMT and PD tools. If a tool is already installed, the `pac tool <toolname>` command launches the latest installed version of the tool.

More information: [pac tool cmt](/power-platform/developer/cli/reference/tool#pac-tool-cmt), [pac tool pd](/power-platform/developer/cli/reference/tool#pac-tool-pd)

## Update tools using Power Platform CLI

Updating the installed tools is easier using the Power Platform CLI. Let's take a look at the tool list.

```bash
> pac tool list

ToolName Installed Version   Nuget     Status
CMT      No        N/A       9.1.0.80  not yet installed; 'pac tool CMT' will install on first launch
PD       No        N/A       9.1.0.104 not yet installed; 'pac tool PD' will install on first launch
PRT      Yes       9.1.0.155 9.1.0.155 ok
```

If there was a tool update available, the NuGet column would have a newer version number than the Installed Version column, and the Status column would contain instructions about how to update the tool. For example, say the PRT has an update. The Status column would say "Newer version available, run 'pac tool PRT --update'".

We can take a look at the options available for any tool like so.

```bash
> pac tool prt help

Microsoft PowerPlatform CLI
Version: 1.19.3

Help: 
Launch Plug-in Registration Tool (PRT)

Commands:
Usage: pac tool prt [--update] [--clear]

  --update                    Update tool to latest available version from nuget.org (alias: -u)
  --clear                     Clear tool from local file cache (alias: -c)
```

The CLI doesn't delete older installed (cached) versions of the tools. You can delete those older versions, keeping the latest version, by using the `--clear` parameter.

```bash
> pac tool <toolname> --clear
```

## Use Solution Packager from Power Platform CLI

While the Solution Packager standalone tool can be downloaded from NuGet, it isn't necessary to do so. You can use the Solution Packager capability built into Power Platform CLI.

```bash
> pac solution pack help

Microsoft PowerPlatform CLI
Version: 1.19.3

Help:
Package solution components on local filesystem into solution.zip (SolutionPackager)

Commands:
Usage: pac solution pack --zipfile [--folder] [--packagetype] [--log] [--errorlevel] [--singleComponent] [--allowDelete] [--allowWrite] [--clobber] [--map] [--sourceLoc] [--localize] [--useLcid] [--useUnmanagedFileForMissingManaged] [--disablePluginRemap] [--processCanvasApps]

  --zipfile                   The full path to the solution ZIP file (alias: -z)
  --folder                    The path to the root folder on the local filesystem. When unpacking/extractins, this will be written to, when packing this will be read from. (alias: -f)
  --packagetype               When unpacking/extracting, use to specify dual Managed and Unmanaged operation. When packing, use to specify Managed or Unmanaged from a previous unpack 'Both'. Can be: 'Unmanaged', 'Managed' or 'Both'; default: 'Unmanaged' (alias: -p) 
  --log                       The path to the log file. (alias: -l)
  --errorlevel                Minimum logging level for log output [Verbose|Info|Warning|Error|Off]; default: Info (alias: -e)       
  --singleComponent           Only perform action on a single component type [WebResource|Plugin|Workflow|None]; default: None. (alias: -sc)
  --allowDelete               Dictates if delete operations may occur; default: false. (alias: -ad)
  --allowWrite                Dictates if write operations may occur; default: false. (alias: -aw)
  --clobber                   Enables that files marked read-only can be deleted or overwritten; default: false. (alias: -c)
  --map                       The full path to a mapping xml file from which to read component folders to pack. (alias: -m)
  --sourceLoc                 Generates a template resource file. Valid only on Extract. Possible Values are auto or an LCID/ISO code of the language you wish to export. When Present, this will extract the string resources from the given locale as a neutral .resx. If auto or just the long or short form of the switch is specified the base locale for the solution will be used. (alias: -src)        
  --localize                  Extract or merge all string resources into .resx files. (alias: -loc)
  --useLcid                   Use LCID's (1033) rather than ISO codes (en-US) for language files. (alias: -lcid)
  --useUnmanagedFileForMissingManaged Use the same XML source file when packaging for Managed and only Unmanaged XML file is found; applies to AppModuleSiteMap, AppModuleMap, FormXml files (alias: -same)
  --disablePluginRemap        Disabled plug-in fully qualified type name remapping. default: false (alias: -dpm)
  --processCanvasApps         (Preview) Pack/unpack any Canvas apps (.msapp) while processing the solution. default: false (alias: -pca)
```

Similarly, for available options to unpack a solution, use `pac solution unpack help`.

### See Also

[Power Platform developer tools](/power-platform/developer/tools)  
[Generate early-bound classes for the SDK for .NET](org-service/generate-early-bound-classes.md)  
[Browse the metadata for your organization](browse-your-metadata.md)  
[Deploy packages using Package Deployer and Windows PowerShell](/power-platform/admin/deploy-packages-using-package-deployer-windows-powershell)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
