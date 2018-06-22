# Supported customizations for model-driven apps

You can customize Model-driven apps by using tools that are available in the Power-apps portal  or that are described in the documentation. These customizations are supported and can be upgraded.

Customizations made using methods other than those described here are unsupported and could cause problems during updates and upgrades to model-driven apps. For more information, see [Unsupported customizations](#unsupported-customizations)

Topics covered in technical articles published on Microsoft sites such as this one are supported, but might not be upgradable.


## Customizations using Power-apps portal

There are a variety of tools included with model-driven apps that you can use to customize them. Customizations made using the model-driven app tools  are fully supported and fully upgradeable.

The following customization methods can be used to produce fully supported customizations:

- Customization in the PowerApps portal or solution explorer. For more information, see [Overview of building a model-driven app](../../maker/model-driven-apps/model-driven-app-overview.md)

- Settings in the web application. For more information, see [Administer model-driven apps](/dynamics365/customer-engagement/admin/admin-guide).

- Reporting Services. For more information, see [Reporting and Analytics Guide for model-driven apps](/dynamics365/customer-engagement/analytics/reporting-analytics-with-dynamics-365).

> [!NOTE]
> The behavior of model-driven apps depend on customizations applied to the associated Common Data Service for Apps. More information: [Supported Customizations for Common Data Service for Apps](../common-data-service/supported-customizations.md)
> *Fully supported* means that developer support can provide assistance for customizations and that application support can help customers running those modifications.



## Customizations applied using code

The documentation on this site for developers, technical articles, and sample code published on this site, and information released by the CDS for Apps Developer Support Team are included in the area of customizations applied using code. The specific actions and levels of supportability and upgradeability are described later in this topic.

### Client-side JavaScript

You can use JavaScript within model-driven apps in three areas:

- **Form Script event handlers**: You can configure form event handlers to call functions defined in JavaScript web resources.

- **Command bar (ribbon) commands**: You can use the `<CustomRule>` or `<JavaScriptFunction>` elements to define actions that call functions defined within JavaScript web resources.

- **Web resources and IFRAMEs**: You can use JavaScript web resources within HTML web resources. IFRAMES configured to allow cross-site scripting, or scripts within HTML web resources included in a form may interact with the documented Xrm.Page or Xrm.Utility methods within the form via the parent reference.

<!-- TODO: Continue from here -->

All interaction with Dynamics 365 application pages must only be performed through the methods with the methods documented in the Client API Reference. Directly accessing the Document Object Model (DOM) of any Dynamics 365 application pages is not supported. The use of jQuery in form scripts and commands is not recommended. More information: Client scripting in model-driven apps using JavaScript

You can open Dynamics 365 forms, views, dialogs, and reports using the methods documented in Open Forms, Views, Dialogs and Reports with a URL.

Ribbon customization
Use of RibbonDiffXml to add, remove, or hide ribbon elements is supported. Reuse of ribbon commands defined by Dynamics 365 is supported; however, we reserve the right to change or deprecate the available commands. Reuse of JavaScript functions defined within ribbon commands is not supported.

Solution file
Modification of an unmanaged solution file is supported as described in this documentation. Certain customization tasks are performed using these steps:

Export a solution component as an unmanaged solution.
Extract the contents of the solution package.
Edit the Customizations.xml file.
Repackage the solutions file.
Import the modified solution.

Note

Changes to the Customizations.xml file must conform to the CustomizationsSolution.xsd schema. For more information, see Schemas Used in Dynamics 365.

The following supported tasks require this procedure:

Ribbon customization.
Application navigation customization using SiteMap.
Form and dashboard customization using FormXml.
Saved query customization.
Plug-ins
The ability to create custom business logic using the plug-in mechanism described in this documentation is fully supported and upgradeable. This feature is available for all Dynamics 365 deployments, including on-premises, IFD, and Online deploments. However, plug-ins can only be registered and executed in the sandbox (isolation) of Dynamics 365 (online). More information: Plug-ins for Extending Dynamics 365

Adding your plug-in and custom workflow activity assemblies to the %installdir%\server\bin\ folder is supported on Dynamics 365 on-premises and IFD server installations only.

Workflow
The ability to create custom workflow activities (assemblies) to be called from workflow rules is fully supported and upgradeable. This feature is available for Dynamics 365 on-premises, IFD, and Online. However, custom workflow activities can only be registered and executed in the sandbox (isolation) of Dynamics 365 (online). More information: Automate your business processes in model-driven apps

The ability to edit XAML workflows is fully supported and upgradeable. However, this feature is available for Dynamics 365 on-premises and IFD only. More information: Automate your business processes in model-driven apps


Support for .NET Framework Versions
The following describes the support considerations for custom code written the Microsoft .NET Framework 4.5.2.

Any web service client created by using the Microsoft .NET Framework 4.5.2 or higher that calls the Dynamics 365 web services is fully supported in Dynamics 365.

Important

You should build any custom client applications using Microsoft .NET Framework 4.6.2 or later. Starting with the Dynamics 365 (online), version 9.0, only applications using Transport Level Security (TLS) 1.2 or better security will be allowed to connect. TLS 1.2 is not the default protocol used by .NET Framework 4.5.2, but it is in .NET Framework 4.6.2.

Enforcement of this higher standard for security will only be applied to Dynamics 365 (online), version 9.0 at this time. If your clients are designed to connect to any version or deployment type you can prepare by re-compling the application to use .NET Framework 4.6.2. More information: Blog Post: Updates coming to model-driven apps connection security

Any .NET assembly that is created with the Microsoft .NET Framework 4.5.2 for use in Dynamics 365 as a Dynamics 365 plug-in assembly or as a Dynamics 365 custom workflow activity is supported.
Any visualization (chart) that is created with .NET Framework 4.5.2 .

## Unsupported customizations

Modifications to Dynamics 365 that are made without using either the methods described in this documentation or Dynamics 365 tools are not supported and are not preserved during updates or upgrades of Dynamics 365. Anything that is not documented in this documentation and supporting documents is not supported. Additionally, unsupported modifications could cause problems when you update through the addition of hotfixes or service packs or upgrade Dynamics 365. To minimize update and upgrade issues, do not modify any Dynamics 365 file that you did not create yourself.

The following is a list of unsupported action types that are frequently asked about:

Modifications to any .aspx, .css, .htm, .js, .xml, .jpg, or .gif files or the addition of files in the wwwroot directories of the Dynamics 365 application, Dynamics 365 tools, or Dynamics 365 files located at Program Files\Dynamics 365. However, if you have made changes to these files, these files are checked for modifications and will not be overwritten.

Modifications to the Dynamics 365 website (file and website settings). Custom applications should be installed in a different website. This includes modifications to the file system access control lists (ACLs) of any files on the Dynamics 365 server.

Use of client certificates is not supported. If you configure the Dynamics 365 website to require IIS client certificates, you will get authentication failures for any applications that were built using the SDK.

Modifications to the physical schema of the database, other than adding or updating indexes. This includes any actions performed against the database without using the System Customization capabilities in the web application or using the metadata APIs that are described in this SDK documentation. Modifying tables, stored procedures, or views in the database is not supported. Adding tables, stored procedures, or views to the database is also not supported because of referential integrity or upgrade issues. For Dynamics 365 (online) on-premises deployments, adding indexes is supported per the guidelines in the Deploying and administering Microsoft Dynamics 365 (on-premises) documentation. This applies to all Dynamics 365 databases and the Dynamics 365 for Outlook local database.

Important

When you change the database without using the support methods for system customization, you run the risk of problems occurring during updates and upgrades.

Data (record) changes in the Dynamics 365 database using SQL commands or any technology other than those described in this documentation.

Referencing any Dynamics 365 dynamic-link libraries (DLLs) other than the following:

Microsoft.Crm.Outlook.Sdk.dll
Microsoft.Crm.Sdk.Proxy.dll
Microsoft.Xrm.Sdk.dll
Microsoft.Xrm.Sdk.Data.dll
Microsoft.Xrm.Sdk.Deployment.dll
Microsoft.Xrm.Sdk.Workflow.dll
Microsoft.Xrm.Tooling.Connector.dll
Microsoft.Xrm.Tooling.CrmConnectControl.dll
Microsoft.Xrm.Tooling.PackageDeployment.CrmPackageExtentionBase.dll
Microsoft.Xrm.Tooling.WebResourceUtility.dll
The use of application programming interfaces (APIs) other than the documented APIs in the web services: Web API, Organization Service, Deployment Service, Discovery Service, Organization Data Service.

To achieve the appearance and behavior of Dynamics 365, the reuse of any Dynamics 365 user interface controls, including the grid controls. These controls may change or be overwritten during an upgrade. We do not recommend that you use or change the Default.css file in the Dynamics 365 root installation folder.

The reuse of any Dynamics 365 JavaScript code, including ribbon commands. This code may change or be overwritten during an upgrade.

Modifications to any one of the Dynamics 365 forms or adding new forms, such as custom .aspx pages, directly to Office Outlook or making changes to .pst files. These changes will not be upgraded.

Making customizations except when you use the Dynamics 365 supported tools available offline in the Dynamics 365 for Outlook.

The use of custom HttpModules to inject HTML/DHTML into the Dynamics 365 Forms.

Creating a plug-in assembly for a standard Dynamics 365 assembly (Microsoft.Crm.*.dll) or performing an update or delete of a platform created pluginassembly is not supported.

Creating an Internet Information Services (IIS) application inside the Dynamics 365 website for any VDir and specifically within the ISV folder is not supported. The <crmwebroot>\ISV folder is no longer supported.

Editing a solutions file to edit any solution components other than ribbons, forms, SiteMap, or saved queries is not supported. For more information, see Support for Editing the Customization File. Defining new solution components by editing the solutions file is not supported. Editing web resource files exported with a solution is not supported. Except for the steps documented in Maintain Managed Solutions, editing the contents of a managed solution is not supported.

Silverlight Application Library Caching is not supported.

Displaying an entity form within an IFrame embedded in another entity form is not supported.

Plugin and Workflow Assemblies must contain all the necessary logic within the respective dll. Plugins may reference some core .Net assemblies. However, we do not support dependencies on .Net assemblies that interact with low-level Windows APIs, such as the graphics design interface. Previously, Dynamics 365 allowed for assemblies to refer to these interfaces, but to adhere to our security standards, changes to this behavior are required.

### See also

[Supported Customizations for Common Data Service for Apps](../common-data-service/supported-customizations.md)