---
title: Model apps for developers| Microsoft Docs
description: Learn how developers can add value to model apps.
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 02/20/2018
ms.author: jdaly
---
# Introduction to model apps for developers
PowerApps offers users, businesses, partners, independent software vendors (ISVs), and systems integrators (SIs) a powerful platform for building line-of-business apps. The new addition to PowerApps in this release are model apps built using the new Common Data Service (CDS). The new CDS now contains the core functionality of the Dynamics 365 Customer Engagement  applications. With model apps, you can build apps that use the same extensibility capabilities as those applications or extend those applications.

## Get a developer instance
The first thing to do is get an environment you can experiment with as you learn.

- TODO: Link to how to get an instance
- TODO: Describe the developer licence
- TODO: Describe next steps to get set up for full ISV licensing

## Get Started
If you are already experienced with the Dynamics 365 Customer Engagement apps, you will find that you will be able to apply your experience building model apps. There are some new designers available to you, but generally the concepts are the same.

If you are new to the Dynamics 365 Customer Engagement applications, the following topics provide a high-level overview of the important concepts to help you get started working with model apps.
- [Understand what developers get with model apps](what-developers-can-do-with-model-apps.md)
- [Introduction to solutions](introduction-solutions.md)
- [Apply Business Logic with code](apply-business-logic-with-code.md)
- [Use Web Services](use-web-services.md)

> [!NOTE]
> Because the new CDS in this preview release is an instance of Dynamics 365 Customer Engagement, you will find more complete information for developers in the [Developer Guide for Dynamics 365 Customer Engagement](/dynamics365/customer-engagement/developer/developer-guide). These topics will provide an overview with links to the developer guide and other guides for more information.


## Tools and resources for developers

Developers will use the following tools and resources when working with model apps.

### Tools available for download from NuGet

The following tools are distributed in NuGet packages. The [Developer Guide: Download tools from NuGet](/dynamics365/customer-engagement/developer/download-tools-nuget) includes a PowerShell script you can use to download and extract the latest versions of these tools.

|Tool  |Description  |
|---------|---------|
|Code generation tool `CrmSvcUtil.exe`|A command-line code generation tool that generates early-bound .NET Framework classes that represent the entity data model used by the organization service. <br />More information: <br />[Organization Service](use-web-services.md#organization-service)<br />[Developer Guide: Create early bound entity classes with the code generation tool ](/dynamics365/customer-engagement/developer/org-service/create-early-bound-entity-classes-code-generation-tool)|
|Configuration Migration tool `DataMigrationUtility.exe`|Used to move configuration data across environments. Configuration data is used to define custom functionality  and is typically stored in custom entities. This tool is not designed to move business data. <br /> More information: [Administrator Guide: Move configuration data across instances and organizations with the Configuration Migration tool](/dynamics365/customer-engagement/admin/manage-configuration-data)|
|Package Deployer `PackageDeployer.exe`|Used to deploy packages on CDS instances. A package is an installable unit that includes solutions. <br /> More information: <br />[Deploy Solution Packages](introduction-solutions.md#deploy-solution-packages)<br />[Distribute your apps on AppSource](what-developers-can-do-with-model-apps.md#distribute-your-apps-on-appsource)<br />[Developer Guide: Create packages for the Dynamics 365 Package Deployer](/dynamics365/customer-engagement/developer/create-packages-package-deployer)|
|Plug-in Registration Tool `PluginRegistration.exe`|A tool used to subscribe .NET assembly plug-in classes to server events. <br />More information: <br />[Create a plug-in](apply-business-logic-with-code.md#create-a-plug-in)<br />[Developer Guide: Walkthrough: Register a plug-in using the plug-in registration tool](/dynamics365/customer-engagement/developer/walkthrough-register-plugin-using-plugin-registration-tool)|
|SolutionPackager tool `SolutionPackager.exe`|A tool that can reversibly decompose a CDS compressed solution file into multiple XML files and other files so that these files can be easily managed by a source control system.<br /> More information: <br />[Team development of solutions](introduction-solutions.md#team-development-of-solutions)<br />[Developer Guide: Use the SolutionPackager tool to compress and extract a solution file](/dynamics365/customer-engagement/developer/compress-extract-solution-file-solutionpackager)|

### .NET SDK Assemblies 

The following are assemblies .NET developers can use to interact with the organization service and discovery services. The latest versions are available to download in the corresponding NuGet packages.


|Assembly  |NuGet Package  |Namespaces  |
|---------|---------|---------|
|Microsoft.Crm.Sdk.Proxy.dll|[Microsoft.CrmSdk.CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/)|[Microsoft.Crm.Sdk](/dotnet/api/microsoft.crm.sdk)<br />[Microsoft.Crm.Sdk.Messages](/dotnet/api/microsoft.crm.sdk.messages)|
|Microsoft.Xrm.Sdk.dll|[Microsoft.CrmSdk.CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/)|[Microsoft.Xrm.Sdk](/dotnet/api/microsoft.xrm.sdk)<br />[Microsoft.Xrm.Sdk.Client](/dotnet/api/microsoft.xrm.sdk.client)<br />[Microsoft.Xrm.Sdk.Discovery](/dotnet/api/microsoft.xrm.sdk.discovery)<br />[Microsoft.Xrm.Sdk.Messages](/dotnet/api/microsoft.xrm.sdk.messages)<br />[Microsoft.Xrm.Sdk.Metadata](/dotnet/api/microsoft.xrm.sdk.metadata)<br />[Microsoft.Xrm.Sdk.Metadata.Query](/dotnet/api/microsoft.xrm.sdk.metadata.query)<br />[Microsoft.Xrm.Sdk.Organization](/dotnet/api/microsoft.xrm.sdk.organization)<br />[Microsoft.Xrm.Sdk.Query](/dotnet/api/microsoft.xrm.sdk.query)<br />[Microsoft.Xrm.Sdk.WebServiceClient](/dotnet/api/microsoft.xrm.sdk.webserviceclient)|

<!-- TODO add information about other assemblies -->

### Community Tools

The Dynamics 365 community creates tools! Many of the most popular ones are distributed via in the [XrmToolBox](https://www.xrmtoolbox.com/). XrmToolBox is a Windows application that connects to CDS, providing tools to ease customization, configuration and operation tasks. It is shipped with more than 30 plugins to make administration, customization or configuration tasks easier and less time consuming.

The following is a selected list of community tools distributed via the XrmToolBox

|Tool  |Description  |
|---------|---------|
|[Attribute Manager](https://www.xrmtoolbox.com/plugins/DLaB.Xrm.AttributeManager/)|Used to rename/delete/or change the type of an attribute.|
|[Early Bound Generator](https://www.xrmtoolbox.com/plugins/DLaB.Xrm.EarlyBoundGenerator/)|Generates Early Bound Entities/Option Sets/Actions. Uses CrmSvcUtil from the SDK, and shows command line used to create the classes.|
|[Easy Translator](https://www.xrmtoolbox.com/plugins/MsCrmTools.Translator/)|Exports and Imports translations with contextual information|
|[Export to Excel](https://www.xrmtoolbox.com/plugins/Ryr.XrmToolBox.ExportToExcel/)|Easily export records from the selected view/fetchxml to Excel.|
|[FetchXML Builder](https://www.xrmtoolbox.com/plugins/Cinteros.Xrm.FetchXmlBuilder/)|Create and test FetchXml Queries|
|[Iconator](https://www.xrmtoolbox.com/plugins/MscrmTools.Iconator/)|Manage custom entities icons in a single screen|
|[Metadata Browser](https://www.xrmtoolbox.com/plugins/MsCrmTools.MetadataBrowser/)|Browse metadata from your Dynamics CRM organization|
|[Plugin Trace Viewer](https://www.xrmtoolbox.com/plugins/Cinteros.XrmToolBox.PluginTraceViewer/)|Investigate the Plug-in Trace Log with easy filtering and display possibilities|
|[Ribbon Workbench 2016](https://www.xrmtoolbox.com/plugins/RibbonWorkbench2016/)|Edit the Dynamics CRM Ribbon or Command Bar from inside the XrmToolbox|
|[User Settings Utility](https://www.xrmtoolbox.com/plugins/MsCrmTools.UserSettingsUtility/)|Manage users personal settings in bulk|
|[View Designer](https://www.xrmtoolbox.com/plugins/Cinteros.XrmToolBox.ViewDesigner/)|Easy UI to design view layouts and alter queries using FetchXML Builder|
|[View Layout Replicator](https://www.xrmtoolbox.com/plugins/MsCrmTools.ViewLayoutReplicator/)|Apply same layout to multiple views of the same entity in a single operation|
|[WebResources Manager](https://www.xrmtoolbox.com/plugins/MsCrmTools.WebResourcesManager/)|Manage your web resources easily|

Another tool that is not distributed via the XrmToolBox is Jason Lattimer's [CRM REST Builder](https://github.com/jlattimer/CRMRESTBuilder). This tool generates JavaScript code for use with the Web API.


> [!NOTE]
> Tools created by the community are not supported by Microsoft. If you have questions or issues with community tools, contact the publisher of the tool.




