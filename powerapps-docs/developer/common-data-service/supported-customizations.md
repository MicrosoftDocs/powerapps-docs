---
title: "<Topic Title> (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "shmcarth" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---

<!-- This is the portion of the old topic that applies to CDS
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/supported-extensions
 -->


# Supported Customizations for Common Data Service for Apps

You can customize Common Data Service for Apps by using tools that are available in the PowerApps portal or that are described in the official documentation. These customizations are supported and can be upgraded.

Customizations made using methods other than those described here are unsupported and could cause problems during updates and upgrades to CDS for Apps. For more information, see [Unsupported Customizations](#unsupported-customizations).

Topics covered in technical articles published on Microsoft sites such as doc.microsoft.com, msdn.microsoft.com or technet.microsoft.com are supported, but might not be upgradable.


## Customizations using PowerApps portal

There are a variety of tools included with CDS for apps that you can use to customize it. Customizations made using the PowerApps portal tools and web application are fully supported and fully upgradeable.

The following customization methods can be used to produce fully supported customizations:

- Customization in the PowerApps portal or solution explorer. For more information, see [What is Common Data Service for Apps?](../../maker/common-data-service/data-platform-intro.md)

- Settings in the web application. For more information, see [Administer Dynamics 365 Customer Engagement](/dynamics365/customer-engagement/admin/admin-guide).

- Reporting Services. For more information, see [Reporting and Analytics Guide for Dynamics 365 Customer Engagement](/dynamics365/customer-engagement/analytics/reporting-analytics-with-dynamics-365).

> [!NOTE]
> Fully supported means that developer support can provide assistance for customizations and that application support can help customers running those modifications.

For more information about using the customization tools in the web application, see the [What is Common Data Service for Apps?](../../maker/common-data-service/data-platform-intro.md).


## Customizations applied using code

The documentation on this site for developers, technical articles, and sample code published on this site, and information released by the CDS for Apps Developer Support Team are included in the area of customizations applied using code. The specific actions and levels of supportability and upgradeability are described later in this topic.

### CDS for Apps web services

Use of the web services are fully supported. This includes: Web API, Organization Service, Discovery Service, and the Organization Data Service. We strive to keep the APIs backward compatible but reserve the right to change APIs for additional features. Entity attributes may also change in future versions.

### Solution file

Modification of an unmanaged solution file is supported as described in this documentation. Certain customization tasks for model-driven apps can be performed using these steps:

1. Export a solution component as an unmanaged solution.
2. Extract the contents of the solution package.
3. Edit the Customizations.xml file.
4. Repackage the solutions file.
5. Import the modified solution.

> [!NOTE]
> Changes to the `Customizations.xml` file must conform to the `CustomizationsSolution.xsd` schema. For more information, see [Customization solutions file schema](customization-solutions-file-schema.md).

The following supported tasks can be performed using this procedure:

- Ribbon customization.
- Application navigation customization using SiteMap.
- Form and dashboard customization using FormXml.
- Saved query customization.

### Plug-ins

The ability to create custom business logic using the plug-in mechanism described in this documentation is fully supported and upgradeable. Plug-ins can only be registered and executed in the sandbox (isolation). More information: [Plug-ins](plug-ins.md)

### Workflow extensions

The ability to create custom workflow activities (assemblies) to be called from workflow rules is fully supported and upgradeable. Custom workflow activities can only be registered and executed in the sandbox (isolation). More information: [Workflow extensions](workflow/workflow-extensions.md) Automate your business processes in Customer Engagement

## Support for .NET Framework Versions

The following describes the support considerations for custom code written the Microsoft .NET Framework 4.5.2.

- Any web service client created by using the Microsoft .NET Framework 4.5.2 or higher that calls the web services is fully supported in CDS for Apps.

> [!IMPORTANT]
> You should build any custom client applications using Microsoft .NET Framework 4.6.2 or later. Only applications using Transport Level Security (TLS) 1.2 or better security will be allowed to connect. TLS 1.2 is not the default protocol used by .NET Framework 4.5.2, but it is in .NET Framework 4.6.2.
> 
> If clients designed for earlier versions of  Dynamics 365 Customer Engagement are designed to connect to any version or deployment type you can prepare by re-compiling the application to use .NET Framework 4.6.2. More information: [Blog Post: Updates coming to Dynamics 365 Customer Engagement connection security](https://blogs.msdn.microsoft.com/crm/2017/09/28/updates-coming-to-dynamics-365-customer-engagement-connection-security/)

- Any .NET assembly that is created with the Microsoft .NET Framework 4.5.2 for use in CDS for Apps as a plug-in assembly or as a custom workflow activity is supported.
- Any visualization (chart) that is created with .NET Framework 4.5.2 .

## Unsupported customizations

Modifications to CDS for Apps that are made without using either the methods described in this documentation or CDS for Apps tools are not supported and are not preserved during updates or upgrades of CDS for Apps. Anything that is not documented in this documentation and supporting documents is not supported. Additionally, unsupported modifications could cause problems when you update through the addition of hotfixes or service packs or upgrade CDS for Apps. 

The following is a list of unsupported action types that are frequently asked about:

- Referencing any CDS for Apps dynamic-link libraries (DLLs) other than the following:

    - Microsoft.Crm.Outlook.Sdk.dll
    - Microsoft.Crm.Sdk.Proxy.dll
    - Microsoft.Xrm.Sdk.dll
    - Microsoft.Xrm.Sdk.Data.dll
    - Microsoft.Xrm.Sdk.Deployment.dll
    - Microsoft.Xrm.Sdk.Workflow.dll
    - Microsoft.Xrm.Tooling.Connector.dll
    - Microsoft.Xrm.Tooling.CrmConnectControl.dll
    - Microsoft.Xrm.Tooling.PackageDeployment.CrmPackageExtentionBase.dll
    - Microsoft.Xrm.Tooling.WebResourceUtility.dll

- The use of application programming interfaces (APIs) other than the documented APIs in the web services: Web API, Organization Service, Deployment Service, Discovery Service, Organization Data Service.

- Plugin and Workflow Assemblies must contain all the necessary logic within the respective dll. Plugins may reference some core .Net assemblies. However, we do not support dependencies on .Net assemblies that interact with low-level Windows APIs, such as the graphics design interface. Previously, Dynamics 365 allowed for assemblies to refer to these interfaces, but to adhere to our security standards, changes to this behavior are required.

- Creating a plug-in assembly for a standard CDS for Apps assembly (Microsoft.Crm.*.dll) or performing an update or delete of a platform created `pluginassembly` is not supported.

- Editing a solutions file to edit any solution components other than ribbons, forms, SiteMap, or saved queries is not supported. For more information, see [When to edit the customizations file](when-edit-customization-file.md). Defining new solution components by editing the solutions file is not supported. Editing web resource files exported with a solution is not supported. Except for the steps documented in [Maintain managed solutions](maintain-managed-solutions.md), editing the contents of a managed solution is not supported.

### Outlook Client
- Modifications to any one of the Dynamics 365 forms or adding new forms, such as custom .aspx pages, directly to Office Outlook or making changes to .pst files. These changes will not be upgraded.
- Making customizations using any means other than the supported tools.

### See also

[Supported customizations for model-driven apps](../model-driven-apps/supported-customizations.md)




