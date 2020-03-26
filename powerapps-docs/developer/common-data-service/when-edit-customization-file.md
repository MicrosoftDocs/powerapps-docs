---
title: "When to edit the customizations file (Common Data Service) | Microsoft Docs"
description: "The customizations.xml file that is exported as part of an unmanaged solution can be edited to perform specific customization tasks. After editing the file you can compress the modified file together with the other files exported in the unmanaged solution. You apply the changes by importing that modified unmanaged solution."
keywords: ""
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: article
ms.assetid: cac303a6-70f9-3962-879a-fbf7fdc2364f
author: shmcarth # GitHub ID
ms.author: jdaly # MSFT alias of Microsoft employees only
manager: ryjones # MSFT alias of manager or PM counterpart
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# When to edit the customizations file

The customizations.xml file that is exported as part of an unmanaged solution can be edited to perform specific customization tasks. After editing the file you can compress the modified file together with the other files exported in the unmanaged solution. You apply the changes by importing that modified unmanaged solution.  
  
 Editing a complex XML file like the customizations.xml file is much easier and less prone to errors if you use a program designed to support schema validation. While it is possible to edit this file using a simple text editor like Notepad, this is not recommended unless you are very familiar with editing this file. For more information, see [Edit the Customizations file with Schema Validation](../model-driven-apps/edit-customizations-xml-file-schema-validation.md). 
  
> [!IMPORTANT]
>  Invalid XML or incorrect definition of solution components can cause errors that will prevent importing a manually edited unmanaged solution.  
  
## Supported tasks  
 You can edit the customization.xml file to perform the following tasks.  
  
 **Editing the ribbon**  
 This documentation describes the process of editing the ribbon by editing the customization.xml file directly. Several people have created ribbon editors that provide a user interface to make editing the ribbon easier. The most popular one so far is the [Ribbon Workbench](https://www.develop1.net/public/rwb/ribbonworkbench.aspx). For support using this program, contact the program publisher.  
  
 For more information about editing the ribbon by editing the customization.xml manually, see [Customize the Ribbon for Microsoft Dynamics 365](../model-driven-apps/customize-commands-ribbon.md).  
  
 **Editing the SiteMap**  
 The SDK describes the process of editing the SiteMap by editing the customization.xml file directly. However, its recommended that you use the site map designer in Common Data Service to create or update site maps. More information: [Create a site map for an app using the site map designer](../../maker/model-driven-apps/create-site-map-app.md)
  
 You can also use one of the community-developed site map editors, such as the [XrmToolBox Site Map Editor](https://www.xrmtoolbox.com/plugins/MsCrmTools.SiteMapEditor/).   
  
 For more information, see [Change Application Navigation using the SiteMap](/dynamics365/customer-engagement/developer/customize-dev/change-application-navigation-using-sitemap) 
 
  
 **Editing FormXml**  
 FormXml is used to define entity forms and dashboards. The form editor and dashboard designer in the application are the most commonly used tools for this purpose. Editing the customizations.xml file is an alternative method. For more information, see [Customize Entity Forms in Microsoft Dynamics 365](../model-driven-apps/customize-entity-forms.md)and [Create a Dashboard](../model-driven-apps/create-dashboard.md).
  
 **Editing saved queries**  
 Definitions of views for entities are included in the customizations.xml file and may be manually edited. The view editor in the application is the most commonly used tool for this purpose. Editing customizations.xml is an alternative method. For more information, see [Customize Entity Views in Microsoft Dynamics 365](../model-driven-apps/customize-entity-views.md).
  
 **Editing the ISV.config**  
 In earlier versions of Dynamics 365 Common Data Service, ISV.Config was the way to add client application extensions as well as some other configuration options. For Microsoft Dynamics CRM 2011 and Microsoft Dynamics 365 Online, the Ribbon provides the way to extend the application. The only remaining capability left in ISV.Config is to customize the appearance of the Service Calendar. For more information, see [Service Calendar Appearance Configuration](/dynamics365/customer-engagement/developer/customize-dev/service-calendar-appearance-configuration)
  
## Unsupported tasks  
 Defining any other solution components by editing the exported customizations.xml file is not supported. This includes the following:  
  
-   Entities  
  
-   Attributes  
  
-   Entity Relationships  
  
-   Entity Messages  
  
-   Option Sets  
  
-   Web Resources  
  
-   Processes (Workflows)  
  
-   Plugin Assemblies  
  
-   SDK Message Processing steps  
  
-   Service Endpoints  
  
-   Reports  
  
-   Connection Roles  
  
-   Article Templates  
  
-   Contract Templates  
  
-   E-mail Templates  
  
-   Mail Merge Templates  
  
-   Security Roles  
  
-   Field Security Profiles  
  
### See also  
 [Customize Microsoft Dynamics 365 and Microsoft Dynamics 365 (online)](/dynamics365/customer-engagement/developer/customize-dev/customize-applications)   <!-- TODO Need to find the topic in powerapps repo-->
 [Customization XML Reference](../model-driven-apps/customization-xml-reference.md)
 [Customization Solutions File Schema](customization-solutions-file-schema.md)  
 [Ribbon core schema](../model-driven-apps/ribbon-core-schema.md)
 [Ribbon types schema](../model-driven-apps/ribbon-types-schema.md)
 [Ribbon WSS schema](../model-driven-apps/ribbon-wss-schema.md)   
 [SiteMap schema](/dynamics365/customer-engagement/developer/customize-dev/sitemap-schema)
 [Form XML schema](../model-driven-apps/form-xml-schema.md)   
 [Schema Support for the Customization File](../model-driven-apps/edit-customizations-xml-file-schema-validation.md)