---
title: "Developer tools and resources (Microsoft Dataverse) | Microsoft Docs" 
description: "Learn about available tools and resources when working with solutions."
ms.date: 08/17/2022
ms.reviewer: phecke
ms.topic: article
author: shmcarth # GitHub ID
ms.subservice: dataverse-developer
ms.author: shmcarth # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Developer tools and resources

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

Developers will use the following tools and resources when working with solutions using Microsoft Dataverse.

## Integrated Development Environment (IDE) extensions

*Power Platform Tools for Visual Studio* - supports the rapid creation, debugging, and deployment of plug-ins. Other capabilities currently in preview include development of custom workflow activities, web resources, integration technologies like Azure Service endpoints and webhooks, and more. To learn more about the tool, install the [extension](tools/devtools-install.md) and try the available [quickstart](tools/devtools-create-project.md) topics.

*Microsoft Power Platform CLI* - a simple, one-stop developer CLI that empowers developers and ISVs to perform various operations in Microsoft Power Platform related to environment lifecycle features, and to authenticate and work with Microsoft Dataverse environments, solution packages, portals, code components, and so on. To learn more about the tool, see [What is Microsoft Power Platform CLI?](powerapps-cli.md).

## Tools available for download from NuGet

The following tools are distributed in NuGet packages. The [Download tools from NuGet](download-tools-nuget.md) topic includes a PowerShell script you can use to download and extract the latest versions of these tools.

|Tool  |Description  |
|---------|---------|
|Code Generation tool `CrmSvcUtil.exe`|A command-line code generation tool that generates early-bound .NET Framework classes that represent the Entity Data Model used by the Organization service. <br />More information: <br />[Organization service](work-with-data.md#organization-service)<br />[Create early bound table classes with the Code Generation tool](org-service/generate-early-bound-classes.md)|
|Configuration Migration tool `DataMigrationUtility.exe`|Used to move configuration data across environments. Configuration data is used to define custom functionality  and is typically stored in custom tables. This tool is not designed to move business data. <br /> More information: [Dataverse Administrator Guide: Move configuration data across environments and organizations with the Configuration Migration tool](/power-platform/admin/manage-configuration-data)|
|Package Deployer `PackageDeployer.exe`|Used to deploy packages on Dataverse environments. A package is an installable unit that includes solutions. <br /> More information: <br />[Deploy packages](/power-platform/admin/deploy-packages-using-package-deployer-windows-powershell)<br />[Create packages for the Package Deployer](/power-platform/alm/package-deployer-tool)|
|Plug-in Registration tool `PluginRegistration.exe`|A tool used to subscribe .NET assembly plug-in classes to data transaction events. <br />More information: <br />[Create a plug-in](apply-business-logic-with-code.md#create-a-plug-in)<br />[Register a plug-in](register-plug-in.md)|
|SolutionPackager tool `SolutionPackager.exe`|A tool that can reversibly decompose a Dataverse compressed solution file into multiple XML files and other files so that these files can be easily managed by a source control system.<br /> More information: <br />[Team development](/power-platform/alm/team-development-alm)<br />[SolutionPackager tool](/power-platform/alm/solution-packager-tool)|

## Dataverse SDK for .NET

The following describes available Dataverse SDK assemblies for .NET code development. The latest versions are available to download in the corresponding NuGet packages.

### Work with data

Use these assemblies to interact with the Organization service and Discovery service.

More information: [Use the Microsoft Dataverse Organization Service](org-service/overview.md)

**NuGet Package**: [Microsoft.CrmSdk.CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/)

|Assembly  |Namespaces  |
|---------|---------|
|Microsoft.Crm.Sdk.Proxy.dll|[Microsoft.Crm.Sdk](/dotnet/api/microsoft.crm.sdk)<br />[Microsoft.Crm.Sdk.Messages](/dotnet/api/microsoft.crm.sdk.messages)|
|Microsoft.Xrm.Sdk.dll|[Microsoft.Xrm.Sdk](/dotnet/api/microsoft.xrm.sdk)<br />[Microsoft.Xrm.Sdk.Client](/dotnet/api/microsoft.xrm.sdk.client)<br />[Microsoft.Xrm.Sdk.Discovery](/dotnet/api/microsoft.xrm.sdk.discovery)<br />[Microsoft.Xrm.Sdk.Messages](/dotnet/api/microsoft.xrm.sdk.messages)<br />[Microsoft.Xrm.Sdk.Metadata](/dotnet/api/microsoft.xrm.sdk.metadata)<br />[Microsoft.Xrm.Sdk.Metadata.Query](/dotnet/api/microsoft.xrm.sdk.metadata.query)<br />[Microsoft.Xrm.Sdk.Organization](/dotnet/api/microsoft.xrm.sdk.organization)<br />[Microsoft.Xrm.Sdk.Query](/dotnet/api/microsoft.xrm.sdk.query)<br />[Microsoft.Xrm.Sdk.WebServiceClient](/dotnet/api/microsoft.xrm.sdk.webserviceclient)|

### Create Process Designer (workflow) extensions

Use this assembly to add custom activities to the Process Designer.

More information [Workflow extensions](workflow/workflow-extensions.md)

**NuGet Package**: [Microsoft.CrmSdk.Workflow](https://www.nuget.org/packages/Microsoft.CrmSdk.Workflow/) 

|Assembly|Namespaces|
|---------|---------|
|Microsoft.Xrm.Sdk.Workflow.dll|[Microsoft.Xrm.Sdk.Workflow](/dotnet/api/microsoft.xrm.sdk.workflow)<br />[Microsoft.Xrm.Sdk.Workflow.Activities](/dotnet/api/microsoft.xrm.sdk.workflow.activities)<br />[Microsoft.Xrm.Sdk.Workflow.Designers](/dotnet/api/microsoft.xrm.sdk.workflow.designers)|

### Build windows client applications

Use these assemblies to facilitate connecting to the Organization service and to build Microsoft Windows client applications.

More information [Build Windows client applications using the XRM tools](xrm-tooling/build-windows-client-applications-xrm-tools.md)

**NuGet Packages**:

- [Microsoft.CrmSdk.XrmTooling.CoreAssembly](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.CoreAssembly/) (Microsoft.Xrm.Tooling.Connector.dll)
- [Microsoft.CrmSdk.XrmTooling.WpfControls](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.WpfControls/) 

|Assembly|Namespaces  |
|---------|---------|
|Microsoft.Xrm.Tooling.Connector.dll|[Microsoft.Xrm.Tooling.Connector](/dotnet/api/microsoft.xrm.tooling.connector)<br />[Microsoft.Xrm.Tooling.Connector.Model](/dotnet/api/microsoft.xrm.tooling.connector.model)|
|Microsoft.Xrm.Tooling.CrmConnectControl.dll|[Microsoft.Xrm.Tooling.CrmConnectControl](/dotnet/api/microsoft.xrm.tooling.crmconnectcontrol)<br />[Microsoft.Xrm.Tooling.CrmConnectControl.Model](/dotnet/api/microsoft.xrm.tooling.crmconnectcontrol.model)<br />[Microsoft.Xrm.Tooling.CrmConnectControl.Properties](/dotnet/api/microsoft.xrm.tooling.crmconnectcontrol.properties)<br />[Microsoft.Xrm.Tooling.CrmConnectControl.Utility](/dotnet/api/microsoft.xrm.tooling.crmconnectcontrol.utility)|
|Microsoft.Xrm.Tooling.WebResourceUtility.dll|[Microsoft.Xrm.Tooling.WebResourceUtility](/dotnet/api/microsoft.xrm.tooling.webresourceutility)|

### Create packages

Use these assemblies to create packages for the Package Deployer tool.

More information: [Create packages for the Package Deployer](/power-platform/alm/package-deployer-tool)

**NuGet Package**: [Microsoft.CrmSdk.XrmTooling.PackageDeployment](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.PackageDeployment/)

|Assembly|Namespace  |
|---------|---------|
|Microsoft.Xrm.Tooling.PackageDeployment.CrmPackageExtentionBase.dll|[Microsoft.Xrm.Tooling.PackageDeployment.CrmPackageExtentionBase](/dotnet/api/microsoft.xrm.tooling.packagedeployment.crmpackageextentionbase)|

### Create Custom virtual table data providers

Use this assembly to create custom virtual table data providers.

More information: [Get started with virtual tables (entities)](virtual-entities/get-started-ve.md)

**NuGet Package**: [Microsoft.CrmSdk.Data](https://www.nuget.org/packages/Microsoft.CrmSdk.Data/)

|Assembly  |Namespaces  |
|---------|---------|
|Microsoft.Xrm.Sdk.Data.dll|<xref:Microsoft.Xrm.Sdk.Data><br /><xref:Microsoft.Xrm.Sdk.Data.CodeGen><br /><xref:Microsoft.Xrm.Sdk.Data.Converters><br /><xref:Microsoft.Xrm.Sdk.Data.Exceptions><br /><xref:Microsoft.Xrm.Sdk.Data.Expressions><br /><xref:Microsoft.Xrm.Sdk.Data.Mappings>|


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
