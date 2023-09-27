---
title: "Subscribe to SDK assembly updates using NuGet (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Microsoft Dataverse SDK assemblies and some command-line tools are available through nuget.org. Use of NuGet packages in your application project enables you to keep your project up-to-date with the latest releases of the SDK assemblies and tools." # 115-145 characters including spaces. This abstract displays in the search result.
ms.collection: get-started
ms.date: 04/14/2023
ms.reviewer: pehecke
ms.topic: article
author: phecke # GitHub ID
ms.author: pehecke # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
contributors:
 - JimDaly
---

# Subscribe to SDK assembly updates using NuGet

Microsoft Dataverse SDK for .NET assemblies and some command-line tools are available through a software distribution website called [NuGet](https://www.nuget.org). Use of NuGet packages in your application project enables you to keep your project up-to-date with the latest releases of the SDK assemblies and tools. Visual Studio has supported this capability since version 2010 and there is even a standalone NuGet client for those developers that don’t develop in Visual Studio. Another advantage of using NuGet packages in your projects is that assembly references and dependencies are automatically taken care of for you.

## Where to find the NuGet SDK packages

The complete list of available Dataverse SDK packages are found under the [crmsdk](https://www.nuget.org/profiles/crmsdk) profile on the NuGet site. These are the official packages produced by the Dataverse product teams at Microsoft. The following list highlights some of the packages you might use depending on what kind of code you are writing.

[Microsoft.CrmSdk.CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/)  
Contains the Microsoft.Xrm.Sdk.dll and Microsoft.Crm.Sdk.Proxy.dll assemblies when targeting .NET Framework development.

[Microsoft.PowerPlatform.Dataverse.Client](https://www.nuget.org/packages/Microsoft.PowerPlatform.Dataverse.Client)  
Contains the Microsoft.Xrm.Sdk.dll and Microsoft.Crm.Sdk.Proxy.dll assemblies when targeting .NET Framework and .NET Core development. Use this package, instead of CoreAssemblies, for new Dataverse development.

[Microsoft.CrmSdk.CoreTools](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreTools/)  
Contains Dataverse development tools. See [Dataverse development tools](../download-tools-nuget.md) for instructions on how to install and update these tools.

[Microsoft.CrmSdk.Deployment](https://www.nuget.org/packages/Microsoft.CrmSdk.Deployment/)  
Contains the Microsoft.Xrm.Sdk.Deployment.dll assembly. Use this package for deployment, configuration, and monitoring of organizations (environments).

[Microsoft.CrmSdk.Outlook](https://www.nuget.org/packages/Microsoft.CrmSdk.Outlook/)  
Contains the Microsoft.Crm.Outlook.dll assembly. Use this package for Outlook client and service related development.

[Microsoft.CrmSdk.Workflow](https://www.nuget.org/packages/Microsoft.CrmSdk.Workflow/)  
Contains the Microsoft.Xrm.Sdk.Workflow.dll assembly. Use this package for custom workflow activity development.

[Microsoft.CrmSdk.XrmTooling.CoreAssembly](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.CoreAssembly/)  
Contains the Microsoft.Xrm.Tooling.Connector assembly. Use this package for [XRM Tooling](../xrm-tooling/build-windows-client-applications-xrm-tools.md) based Windows client application development.

[Microsoft.CrmSdk.XrmTooling.CrmConnector.PowerShell](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.CrmConnector.PowerShell/)  
Contains the assemblies for using the XRM Tooling connector with Powershell.

[Microsoft.CrmSdk.XrmTooling.PackageDeployment.PowerShell](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.PackageDeployment.PowerShell/)  
Contains the assemblies for Dataverse package deployment using Powershell.

[Microsoft.CrmSdk.XrmTooling.PackageDeployment](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.PackageDeployment/)  
Contains the Microsoft.Xrm.Tooling.PackageDeployment.CrmPackageExtentionBase.dll assembly.

[Microsoft.CrmSdk.XrmTooling.PluginRegistrationTool](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.PluginRegistrationTool/)  
Contains the Plug-in Registration tool used for registering plug-in assemblies, custom workflow activity assemblies, virtual entitles, and service endpoints with Dataverse. See [Dataverse development tools](../download-tools-nuget.md) for instructions on how to install and update the tool.

## How to install a package in your project

 For information about installing NuGet packages into your project, see [Install and manage packages in Visual Studio using the NuGet Package Manager](/nuget/consume-packages/install-use-packages-visual-studio).
  
### See also

[NuGet Documentation](/nuget/)  
[Install NuGet client tools](https://learn.microsoft.com/nuget/install-nuget-client-tools)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
