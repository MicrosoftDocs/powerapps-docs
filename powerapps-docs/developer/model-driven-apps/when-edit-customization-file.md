---
title: "When to edit customizations file (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This topic covers when to edit customizations file and different possible ways to do that" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/14/2021
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "KumarVivek" # GitHub ID
ms.author: "kvivek" # MSFT alias of Microsoft employees only
manager: "shilpas" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# When to edit the customizations file

The customizations.xml file that is exported as part of an unmanaged solution can be edited to perform specific customization tasks. After editing the file you can compress the modified file together with the other files exported in the unmanaged solution. You apply the changes by importing that modified unmanaged solution.  
  
 Editing a complex XML file like the customizations.xml file is much easier and less prone to errors if you use a program designed to support schema validation. While it is possible to edit this file using a simple text editor like Notepad, this is not recommended unless you are very familiar with editing this file. For more information, see [Edit the Customizations file with Schema Validation](edit-customizations-xml-file-schema-validation.md).  
  
> [!IMPORTANT]
>  Invalid XML or incorrect definition of solution components can cause errors that will prevent importing a manually edited unmanaged solution.  
  
## Supported tasks  
 You can edit the customization.xml file to perform the following tasks.  
  
 **Editing the ribbon**  
 This documentation describes the process of editing the ribbon by editing the customization.xml file directly. Several people have created ribbon editors that provide a user interface to make editing the ribbon easier. The most popular one so far is the [Ribbon Workbench](https://www.develop1.net/public/rwb/ribbonworkbench.aspx). For support using this program, contact the program publisher.  
  
 For more information about editing the ribbon by editing the customization.xml manually, see [Customize the Ribbon](customize-commands-ribbon.md).  
  
 **Editing the SiteMap**  
 The SDK describes the process of editing the SiteMap by editing the customization.xml file directly. However, its recommended that you use the site map designer in Model-driven apps to create or update site maps. More information: [Tutorial: Create a Model-driven app site map for an app using the site map designer](../../maker/model-driven-apps/create-site-map-app.md)  
  
 You can also use one of the community-developed site map editors, such as the [XrmToolBox Site Map Editor](https://www.xrmtoolbox.com/plugins/MsCrmTools.SiteMapEditor/).   
  
 For more information, see [Change Application Navigation using the SiteMap](../../maker/model-driven-apps/create-site-map-app.md)  
  
 **Editing FormXml**  
 FormXml is used to define forms and dashboards. The form editor and dashboard designer in the application are the most commonly used tools for this purpose. Editing the customizations.xml file is an alternative method. For more information, see [Customize forms](customize-entity-forms.md) and [Create a Dashboard](create-dashboard.md).  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

 **Editing saved queries**  
 Definitions of views for tables are included in the customizations.xml file and may be manually edited. The view editor in the application is the most commonly used tool for this purpose. Editing customizations.xml is an alternative method. For more information, see [Customize views](customize-entity-views.md).  
  
 **Editing the ISV.config**  
  For Microsoft Dataverse, the Ribbon provides the way to extend the application. The only remaining capability left in ISV.Config is to customize the appearance of the Service Calendar. For more information, see  [Service calendar appearance configuration](/dynamics365/customer-engagement/developer/customize-dev/service-calendar-appearance-configuration).  
  
## Unsupported tasks  

 Defining any other solution components by editing the exported customizations.xml file is not supported. This includes the following:  
  
-  Tables  
  
-   Columns  
  
-   Table Relationships  
  
-   Table Messages  
  
-   Choice 
  
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
 [Customization XML reference](customization-xml-reference.md)   
 [Customization solutions file schema](../data-platform/customization-solutions-file-schema.md)   
 [Ribbon core schema](ribbon-core-schema.md)
 [Ribbon types schema](ribbon-types-schema.md)
 [Ribbon WSS schema](ribbon-wss-schema.md)   
 [Form XML schema](form-xml-schema.md)   
 [Schema Support for the Customization File](edit-customizations-xml-file-schema-validation.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]