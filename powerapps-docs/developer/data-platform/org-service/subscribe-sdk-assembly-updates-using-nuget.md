---
title: "Subscribe to SDK assembly updates using NuGet (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Microsoft Dataverse (.NET Framework) SDK assemblies and some command-line tools are available through nuget.org. Use of NuGet packages in your application project enables you to keep your project up-to-date with the latest releases of the SDK assemblies and tools." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: intro-internal
ms.date: 04/013/2023
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

The available Dataverse SDK packages are listed under the [crmsdk](https://www.nuget.org/profiles/crmsdk) profile on the NuGet site. These are the official packages produced by the Dataverse product teams at Microsoft. Select any package link in the following table to navigate to the package details page on nuget.org.

|Package|Description|
|---------|---------|
|[Microsoft.CrmSdk.CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/)|Contains the Microsoft.Xrm.Sdk.dll and Microsoft.Crm.Sdk.Proxy.dll core assemblies for .NET Framework development|
|[Microsoft.CrmSdk.CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/)|Contains the Microsoft.Xrm.Sdk.dll and Microsoft.Crm.Sdk.Proxy.dll core assemblies for .NET Framework and .NET Core development. This package is recommended for new development.|
|[Microsoft.CrmSdk.CoreTools](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreTools/)|Contains Dataverse development tools. See [Dataverse development tools](../download-tools-nuget.md) for instructions on how to install and update these tools using Power Platform CLI.|
|[Microsoft.CrmSdk.Deployment](https://www.nuget.org/packages/Microsoft.CrmSdk.Deployment/)|Contains the Microsoft.Xrm.Sdk.Deployment.dll assembly|
|[Microsoft.CrmSdk.Outlook](https://www.nuget.org/packages/Microsoft.CrmSdk.Outlook/)|Contains the Microsoft.Crm.Outlook.dll assembly|
|[Microsoft.CrmSdk.Workflow](https://www.nuget.org/packages/Microsoft.CrmSdk.Workflow/)|Contains the Microsoft.Xrm.Sdk.Workflow.dll assembly|
|[Microsoft.CrmSdk.XrmTooling.CoreAssembly](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.CoreAssembly/)|Contains the  Microsoft.Xrm.Tooling.Connector assembly |
|[Microsoft.CrmSdk.XrmTooling.CrmConnector.PowerShell](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.CrmConnector.PowerShell/)|Contains the assemblies for Xrm.Tooling.Connector Powershell |
|[Microsoft.CrmSdk.XrmTooling.PackageDeployment.PowerShell](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.PackageDeployment.PowerShell/)| Contains the assemblies for Package Deployer Powershell        |
|[Microsoft.CrmSdk.XrmTooling.PackageDeployment.Wpf](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.PackageDeployment.Wpf/)|Contains the Dynamics 365 Package Deployer|
|[Microsoft.CrmSdk.XrmTooling.PackageDeployment](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.PackageDeployment/)|Contains the Microsoft.Xrm.Tooling.PackageDeployment.CrmPackageExtentionBase.dll assembly|
|[Microsoft.CrmSdk.XrmTooling.PluginRegistrationTool](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.PluginRegistrationTool/)|Contains the Plugin Registration Tool required to manage Plugin assemblies,Workflow assemblies,Virtual Entitles, and Service endpoints for Microsoft Dynamics 365.|
|[Microsoft.CrmSdk.XrmTooling.WpfControls](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.WpfControls/)|Contains the Microsoft.Xrm.Tooling.CrmConnectControl.dll, Microsoft.Xrm.Tooling.Ui.Styles.dll, and Microsoft.Xrm.Tooling.WebResourceUtility.dll assemblies|

## How to install a package in your project

 For information about installing NuGet packages into your project, see [Install and manage packages in Visual Studio using the NuGet Package Manager](/nuget/consume-packages/install-use-packages-visual-studio).

## Download Tools from NuGet

You can obtain Dataverse development tools from NuGet by following the instructions in this topic: [Dataverse development tools](../download-tools-nuget.md)
  
### See also

 [NuGet Documentation](/nuget/)  
 [Install NuGet client tools](https://learn.microsoft.com/nuget/install-nuget-client-tools)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
