---
title: "<Topic Title> (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "shmcarth" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
<!-- The information about SDK assemblies should be found elsewhere
Perhaps this topic should call out the available tools at a high level?
Community tools should go here?
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/developer-tools -->

# Developer tools and resources

Developers will use the following tools and resources when working with solutions using Common Data Service for apps.

## Tools available for download from NuGet

The following tools are distributed in NuGet packages. The [Developer Guide: Download tools from NuGet](/dynamics365/customer-engagement/developer/download-tools-nuget) topic includes a PowerShell script you can use to download and extract the latest versions of these tools.

|Tool  |Description  |
|---------|---------|
|Code generation tool `CrmSvcUtil.exe`|A command-line code generation tool that generates early-bound .NET Framework classes that represent the entity data model used by the organization service. <br />More information: <br />[Organization Service](work-with-data-cds.md#organization-service)<br />[Create early bound entity classes with the code generation tool ](/dynamics365/customer-engagement/developer/org-service/create-early-bound-entity-classes-code-generation-tool)|
|Configuration Migration tool `DataMigrationUtility.exe`|Used to move configuration data across environments. Configuration data is used to define custom functionality  and is typically stored in custom entities. This tool is not designed to move business data. <br /> More information: [Common Data Service for Apps Administrator Guide: Move configuration data across instances and organizations with the Configuration Migration tool](/dynamics365/customer-engagement/admin/manage-configuration-data)|
|Package Deployer `PackageDeployer.exe`|Used to deploy packages on Common Data Service for Apps instances. A package is an installable unit that includes solutions. <br /> More information: <br />[Deploy Solution Packages](introduction-solutions.md#deploy-solution-packages)<br />[Create packages for the CDS for Apps Package Deployer](/dynamics365/customer-engagement/developer/create-packages-package-deployer)|
|Plug-in Registration Tool `PluginRegistration.exe`|A tool used to subscribe .NET assembly plug-in classes to server events. <br />More information: <br />[Create a plug-in](apply-business-logic-with-code.md#create-a-plug-in)<br />[Walkthrough: Register a plug-in using the plug-in registration tool](/dynamics365/customer-engagement/developer/walkthrough-register-plugin-using-plugin-registration-tool)|
|SolutionPackager tool `SolutionPackager.exe`|A tool that can reversibly decompose a Common Data Service for Apps compressed solution file into multiple XML files and other files so that these files can be easily managed by a source control system.<br /> More information: <br />[Team development of solutions](introduction-solutions.md#team-development-of-solutions)<br />[Use the SolutionPackager tool to compress and extract a solution file](/dynamics365/customer-engagement/developer/compress-extract-solution-file-solutionpackager)|

## .NET SDK Assemblies 

The following are assemblies .NET developers can use. The latest versions are available to download in the corresponding NuGet packages.

### Work with data

Use these assemblies to interact with the organization service and discovery services.

More information: [Use the CDS for Apps Organization service](/dynamics365/customer-engagement/developer/use-microsoft-dynamics-365-organization-service)

**NuGet Package**: [Microsoft.CrmSdk.CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/)

|Assembly  |Namespaces  |
|---------|---------|
|Microsoft.Crm.Sdk.Proxy.dll|[Microsoft.Crm.Sdk](/dotnet/api/microsoft.crm.sdk)<br />[Microsoft.Crm.Sdk.Messages](/dotnet/api/microsoft.crm.sdk.messages)|
|Microsoft.Xrm.Sdk.dll|[Microsoft.Xrm.Sdk](/dotnet/api/microsoft.xrm.sdk)<br />[Microsoft.Xrm.Sdk.Client](/dotnet/api/microsoft.xrm.sdk.client)<br />[Microsoft.Xrm.Sdk.Discovery](/dotnet/api/microsoft.xrm.sdk.discovery)<br />[Microsoft.Xrm.Sdk.Messages](/dotnet/api/microsoft.xrm.sdk.messages)<br />[Microsoft.Xrm.Sdk.Metadata](/dotnet/api/microsoft.xrm.sdk.metadata)<br />[Microsoft.Xrm.Sdk.Metadata.Query](/dotnet/api/microsoft.xrm.sdk.metadata.query)<br />[Microsoft.Xrm.Sdk.Organization](/dotnet/api/microsoft.xrm.sdk.organization)<br />[Microsoft.Xrm.Sdk.Query](/dotnet/api/microsoft.xrm.sdk.query)<br />[Microsoft.Xrm.Sdk.WebServiceClient](/dotnet/api/microsoft.xrm.sdk.webserviceclient)|

### Create Process Designer (Workflow) extensions

Use this assembly to add custom activities to the Process designer. 

More information [Custom workflow activities (workflow assemblies)](/dynamics365/customer-engagement/developer/custom-workflow-activities-workflow-assemblies)

**NuGet Package**: [Microsoft.CrmSdk.Workflow](https://www.nuget.org/packages/Microsoft.CrmSdk.Workflow/) 

|Assembly|Namespaces|
|---------|---------|
|Microsoft.Xrm.Sdk.Workflow.dll|[Microsoft.Xrm.Sdk.Workflow](/dotnet/api/microsoft.xrm.sdk.workflow)<br />[Microsoft.Xrm.Sdk.Workflow.Activities](/dotnet/api/microsoft.xrm.sdk.workflow.activities)<br />[Microsoft.Xrm.Sdk.Workflow.Designers](/dotnet/api/microsoft.xrm.sdk.workflow.designers)|

### Build windows client applications

Use these assemblies to facilitate connecting to the organization service and to build windows client applications. 

More information [Build Windows client applications using the XRM tools](/dynamics365/customer-engagement/developer/build-windows-client-applications-xrm-tools)

**NuGet Packages**:
- [Microsoft.CrmSdk.XrmTooling.CoreAssembly](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.CoreAssembly/) (Microsoft.Xrm.Tooling.Connector.dll)
- [Microsoft.CrmSdk.XrmTooling.WpfControls](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.WpfControls/) 

|Assembly|Namespaces  |
|---------|---------|
|Microsoft.Xrm.Tooling.Connector.dll|[Microsoft.Xrm.Tooling.Connector](/dotnet/api/microsoft.xrm.tooling.connector)<br />[Microsoft.Xrm.Tooling.Connector.Model](/dotnet/api/microsoft.xrm.tooling.connector.model)|
|Microsoft.Xrm.Tooling.CrmConnectControl.dll|[Microsoft.Xrm.Tooling.CrmConnectControl](/dotnet/api/microsoft.xrm.tooling.crmconnectcontrol)<br />[Microsoft.Xrm.Tooling.CrmConnectControl.Model](/dotnet/api/microsoft.xrm.tooling.crmconnectcontrol.model)<br />[Microsoft.Xrm.Tooling.CrmConnectControl.Properties](/dotnet/api/microsoft.xrm.tooling.crmconnectcontrol.properties)<br />[Microsoft.Xrm.Tooling.CrmConnectControl.Utility](/dotnet/api/microsoft.xrm.tooling.crmconnectcontrol.utility)|
|Microsoft.Xrm.Tooling.WebResourceUtility.dll|[Microsoft.Xrm.Tooling.WebResourceUtility](/dotnet/api/microsoft.xrm.tooling.webresourceutility)|

### Create packages

Use these assemblies to create packages for the Package Deployer.

More information: [Create packages for the CDS for Apps Package Deployer](/dynamics365/customer-engagement/developer/create-packages-package-deployer)

**NuGet Package**: [Microsoft.CrmSdk.XrmTooling.PackageDeployment](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.PackageDeployment/)

|Assembly|Namespace  |
|---------|---------|
|Microsoft.Xrm.Tooling.PackageDeployment.CrmPackageExtentionBase.dll|[Microsoft.Xrm.Tooling.PackageDeployment.CrmPackageExtentionBase](/dotnet/api/microsoft.xrm.tooling.packagedeployment.crmpackageextentionbase)|

### Create Custom virtual entity data providers

Use this assembly to create custom virtual entity data providers. 

More information: [Get started with virtual entities](/dynamics365/customer-engagement/developer/virtual-entities/get-started-ve)

**NuGet Package**: [Microsoft.CrmSdk.Data](https://www.nuget.org/packages/Microsoft.CrmSdk.Data/)

|Assembly  |Namespaces  |
|---------|---------|
|Microsoft.Xrm.Sdk.Data.dll|[Microsoft.Xrm.Sdk.Data](/dotnet/api/microsoft.xrm.sdk.data)<br />[Microsoft.Xrm.Sdk.Data.CodeGen](/api/microsoft.xrm.sdk.data.codegen)<br />[Microsoft.Xrm.Sdk.Data.Converters](/dotnet/api/microsoft.xrm.sdk.data.converters)<br />[Microsoft.Xrm.Sdk.Data.Exceptions](/dotnet/api/microsoft.xrm.sdk.data.exceptions)<br />[Microsoft.Xrm.Sdk.Data.Expressions](/dotnet/api/microsoft.xrm.sdk.data.expressions)<br />[Microsoft.Xrm.Sdk.Data.Infra](/dotnet/api/microsoft.xrm.sdk.data.infra)<br />[Microsoft.Xrm.Sdk.Data.Mappings](/dotnet/api/microsoft.xrm.sdk.data.mappings)|

### Extend Outlook Client

Use this assembly to interact with Microsoft Dynamics 365 for Outlook and Microsoft CDS for Apps for Microsoft Office Outlook with Offline Access. 

More information: [Extend Dynamics 365 for Outlook](/dynamics365/customer-engagement/developer/extend-customer-engagement-outlook)

**NuGet Package**: [Microsoft.CrmSdk.Outlook](https://www.nuget.org/packages/Microsoft.CrmSdk.Outlook/)

|Assembly|Namespace|
|---------|---------|
|Microsoft.Crm.Outlook.Sdk.dll|[Microsoft.Crm.Outlook.Sdk](/dotnet/api/microsoft.crm.outlook.sdk)|

