---
title: "Subscribe to SDK assembly updates using NuGet (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: ".NET SDK assemblies and some command-line tools are available through a software distribution website called nuget.org. Use of NuGet packages in your application project enables you to keep your project up-to-date with the latest releases of the SDK assemblies and tools." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Subscribe to SDK assembly updates using NuGet

.NET SDK assemblies and some command-line tools are available through a software distribution website called [nuget.org](http://www.nuget.org). Use of NuGet  packages in your application project enables you to keep your project up-to-date with the latest releases of the SDK assemblies and tools. Visual Studio has supported this capability since version 2010 and there is even a standalone NuGet  client for those developers that don’t develop in Visual Studio. Another advantage of using NuGet  packages in your projects is that assembly references and dependencies are automatically taken care of for you. NuGet  packages are available for Common Data Service for Apps as well as for earlier versions of Dynamics 365 Customer Engagement.  
  
<a name="BKMK_GetNuGetPackages"></a>

## Where to find the NuGet SDK packages

The NuGet SDK are found under the [crmsdk](https://www.nuget.org/profiles/crmsdk) profile. These are the official CDS for Apps packages. Select any package in the list to navigate to the package details page. The following are the current NuGet packages relevant for CDS for Apps.  


|Package|Description|
|---------|---------|
|[Microsoft.CrmSdk.CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/)|Contains the Microsoft.Xrm.Sdk.dll and Microsoft.Crm.Sdk.Proxy.dll assemblies plus tools|
|[Microsoft.CrmSdk.CoreTools](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreTools/)|Contains the SDK tools authored by the Microsoft Dynamics 365 team.|
|[Microsoft.CrmSdk.Deployment](https://www.nuget.org/packages/Microsoft.CrmSdk.Deployment/)|Contains the Microsoft.Xrm.Sdk.Deployment.dll assembly|
|[Microsoft.CrmSdk.Outlook](https://www.nuget.org/packages/Microsoft.CrmSdk.Outlook/)|Contains the Microsoft.Crm.Outlook.dll assembly|
|[Microsoft.CrmSdk.WebApi.Samples.HelperCode](https://www.nuget.org/packages/Microsoft.CrmSdk.WebApi.Samples.HelperCode/)|C# helper code authored by the Microsoft Dynamics 365  Customer Engagement Developer documentation team. This code is for use with the Web API. These classes provide web service authentication for both on-premises and online deployments, error handling, and connection string configuration. These classes are used in our Web API samples|
|[Microsoft.CrmSdk.Workflow](https://www.nuget.org/packages/Microsoft.CrmSdk.Workflow/)|Contains the Microsoft.Xrm.Sdk.Workflow.dll assembly|
|[Microsoft.CrmSdk.XrmTooling.CoreAssembly](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.CoreAssembly/)|Contains the  Microsoft.Xrm.Tooling.Connector assembly |
|[Microsoft.CrmSdk.XrmTooling.CrmConnector.PowerShell](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.CrmConnector.PowerShell/)|Contains the assemblies for Xrm.Tooling.Connector Powershell |
|[Microsoft.CrmSdk.XrmTooling.PackageDeployment.PowerShell](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.PackageDeployment.PowerShell/)| Contains the assemblies for Package Deployer Powershell        |
|[Microsoft.CrmSdk.XrmTooling.PackageDeployment.Wpf](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.PackageDeployment.Wpf/)|Contains the Dynamics 365 Package Deployer|
|[Microsoft.CrmSdk.XrmTooling.PackageDeployment](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.PackageDeployment/)|Contains the Microsoft.Xrm.Tooling.PackageDeployment.CrmPackageExtentionBase.dll assembly|
|[Microsoft.CrmSdk.XrmTooling.PluginRegistrationTool](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.PluginRegistrationTool/)|Contains the Plugin Registration Tool required to manage Plugin assemblies,Workflow assemblies,Virtual Entitles, and Service endpoints for Microsoft Dynamics 365.|
|[Microsoft.CrmSdk.XrmTooling.WpfControls](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.WpfControls/)|Contains the Microsoft.Xrm.Tooling.CrmConnectControl.dll, Microsoft.Xrm.Tooling.Ui.Styles.dll, and Microsoft.Xrm.Tooling.WebResourceUtility.dll assemblies|

## How to install a package in your project  
 For information about installing NuGet  packages into your project, see [Managing NuGet Packages Using the Dialog](http://docs.nuget.org/docs/start-here/managing-nuget-packages-using-the-dialog).  

## Download Tools from Nuget

You can download tools used in development from NuGet using the  powershell script found in this topic: [Download tools from NuGet](../download-tools-nuget.md)
  
### See also  
 [NuGet Documentation](/nuget/)   
 [Installing NuGet](http://docs.nuget.org/docs/start-here/installing-nuget)