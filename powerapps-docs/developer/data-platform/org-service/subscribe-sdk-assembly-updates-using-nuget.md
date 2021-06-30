---
title: "Subscribe to SDK assembly updates using NuGet (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Microsoft Dataverse (.NET Framework) SDK assemblies and some command-line tools are available through a software distribution website called nuget.org. Use of NuGet packages in your application project enables you to keep your project up-to-date with the latest releases of the SDK assemblies and tools." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: intro-internal
ms.date: 10/31/2018
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Subscribe to SDK assembly updates using NuGet

.NET Framework based SDK assemblies and some command-line tools are available through a software distribution website called [nuget.org](https://www.nuget.org). Use of NuGet  packages in your application project enables you to keep your project up-to-date with the latest releases of the SDK assemblies and tools. Visual Studio has supported this capability since version 2010 and there is even a standalone NuGet  client for those developers that don’t develop in Visual Studio. Another advantage of using NuGet  packages in your projects is that assembly references and dependencies are automatically taken care of for you.  
  
<a name="BKMK_GetNuGetPackages"></a>

## Where to find the NuGet SDK packages

The NuGet SDK are found under the [crmsdk](https://www.nuget.org/profiles/crmsdk) profile. These are the official Microsoft Dataverse packages. Select any package in the list to navigate to the package details page. The following are the current NuGet packages relevant for Dataverse.  


|Package|Description|
|---------|---------|
|[Microsoft.CrmSdk.CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/)|Contains the Microsoft.Xrm.Sdk.dll and Microsoft.Crm.Sdk.Proxy.dll assemblies plus tools|
|[Microsoft.CrmSdk.CoreTools](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreTools/)|Contains the SDK tools authored by the Microsoft Dynamics 365 team.|
|[Microsoft.CrmSdk.Deployment](https://www.nuget.org/packages/Microsoft.CrmSdk.Deployment/)|Contains the Microsoft.Xrm.Sdk.Deployment.dll assembly|
|[Microsoft.CrmSdk.Outlook](https://www.nuget.org/packages/Microsoft.CrmSdk.Outlook/)|Contains the Microsoft.Crm.Outlook.dll assembly|
|[Microsoft.CrmSdk.WebApi.Samples.HelperCode](https://www.nuget.org/packages/Microsoft.CrmSdk.WebApi.Samples.HelperCode/)|C# helper code authored by the Power Apps documentation team. This code is for use with the Web API. These classes provide web service authentication for both on-premises and online deployments, error handling, and connection string configuration. These classes are used in our Web API samples|
|[Microsoft.CrmSdk.Workflow](https://www.nuget.org/packages/Microsoft.CrmSdk.Workflow/)|Contains the Microsoft.Xrm.Sdk.Workflow.dll assembly|
|[Microsoft.CrmSdk.XrmTooling.CoreAssembly](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.CoreAssembly/)|Contains the  Microsoft.Xrm.Tooling.Connector assembly |
|[Microsoft.CrmSdk.XrmTooling.CrmConnector.PowerShell](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.CrmConnector.PowerShell/)|Contains the assemblies for Xrm.Tooling.Connector Powershell |
|[Microsoft.CrmSdk.XrmTooling.PackageDeployment.PowerShell](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.PackageDeployment.PowerShell/)| Contains the assemblies for Package Deployer Powershell        |
|[Microsoft.CrmSdk.XrmTooling.PackageDeployment.Wpf](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.PackageDeployment.Wpf/)|Contains the Dynamics 365 Package Deployer|
|[Microsoft.CrmSdk.XrmTooling.PackageDeployment](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.PackageDeployment/)|Contains the Microsoft.Xrm.Tooling.PackageDeployment.CrmPackageExtentionBase.dll assembly|
|[Microsoft.CrmSdk.XrmTooling.PluginRegistrationTool](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.PluginRegistrationTool/)|Contains the Plugin Registration Tool required to manage Plugin assemblies,Workflow assemblies,Virtual Entitles, and Service endpoints for Microsoft Dynamics 365.|
|[Microsoft.CrmSdk.XrmTooling.WpfControls](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.WpfControls/)|Contains the Microsoft.Xrm.Tooling.CrmConnectControl.dll, Microsoft.Xrm.Tooling.Ui.Styles.dll, and Microsoft.Xrm.Tooling.WebResourceUtility.dll assemblies|

## How to install a package in your project

 For information about installing NuGet  packages into your project, see [Managing NuGet packages Using the dialog](https://docs.nuget.org/docs/start-here/managing-nuget-packages-using-the-dialog).  

## Download Tools from NuGet

You can download tools used in development from NuGet using the powershell script found in this topic: [Download tools from NuGet](../download-tools-nuget.md)
  
### See also

 [NuGet Documentation](/nuget/)  
 [Installing NuGet](https://docs.nuget.org/docs/start-here/installing-nuget)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]