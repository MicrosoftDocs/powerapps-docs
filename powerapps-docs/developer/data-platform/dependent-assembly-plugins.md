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

[Workflow extensions](workflow/workflow-extensions.md), also known as *workflow assemblies*, *workflow activities* or *custom workflow activities* are not supported.

## Create a Visual Studio project

Use the PAC CLI `pac plugin init` command to create a Visual Studio project that will streamline your development process with dependent assemblies.

## Add a dependent assembly using NuGet

## Add another dependent file or assembly

## Register your plug-in package

## Update your plug-in package