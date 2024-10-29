---
title: "Developer tools and resources (Microsoft Dataverse) | Microsoft Docs" 
description: "Learn about available tools and resources when working with solutions."
ms.date: 03/27/2023
ms.reviewer: pehecke
ms.topic: article
author: shmcarth # GitHub ID
ms.subservice: dataverse-developer
ms.author: shmcarth # MSFT alias of Microsoft employees only
---

# Developer tools and resources

Developers will use the following tools and resources when working with Dataverse and Power Platform.

## Dataverse development tools

There are several tools commonly used during Dataverse code development. Some of these tools have a user interface and some are command driven. Use this article to learn how to easily install, update, and launch these tools: [Dataverse development tools](download-tools-nuget.md)

## Dataverse SDK for .NET

The following describes available Dataverse SDK assemblies for .NET code development. The latest versions are available to download in the corresponding NuGet packages.

### Work with data

Use these assemblies to interact with the Organization service and Discovery service.

More information: [Use the Microsoft Dataverse SDK for .NET](org-service/overview.md)

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

Use these assemblies to facilitate connecting with the SDK for .NET and to build Microsoft Windows client applications.

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

## Power Platform development tools

In addition to the Dataverse development tools and Dataverse SDK for .NET, you can use the tools listed in this article to extend other features and capabilities of Power Platform using code: [Power Platform developer tools](/power-platform/developer/tools)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
