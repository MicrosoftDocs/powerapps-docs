---
title: "Understand how managed solutions are merged(Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "To avoid multiple installed solutions from interfering with one another, follow best practices while constructing a solution" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "shmcarth" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Understand how managed solutions are merged

When you prepare your managed solution to be installed, remember that an organization may have multiple solutions installed or that other solutions may be installed in the future. Construct a solution that follows best practices so that your solution will not interfere with other solutions.  
  
 The processes that Common Data Service for Apps uses to merge customizations emphasize maintaining the functionality of the solution. While every effort is made to preserve the presentation, some incompatibilities between customizations may require that the computed resolution will change some presentation details in favor of maintaining the customization functionality.  
  
<a name="BKMK_MergingFormCustomizations"></a>   

## Merge form customizations  
 The only form customizations that have to be merged are those that are performed on any entity forms that are already in the organization. Typically, this means that form customizations only have to be merged when your solution customizes the forms that were included for entities created when CDS for Apps was installed. One way to avoid form merging is to provide new forms for any CDS for Apps entities. Forms for custom entities will not require merging unless you are creating a solution that updates or modifies an existing managed solution that created the custom entities and their forms.  
  
 When a solution is packaged as a managed solution the form definitions stored in FormXML are compared to the original FormXML and only the differences are included in the managed solution. When the managed solution is installed in a new organization, the form customization differences are then merged with the FormXML for the existing form to create a new form definition. This new form definition is what the user sees and what a system customizer can modify. When the managed solution is uninstalled, only those form elements found in the managed solution are removed.  
  
 When you add new elements to a form that is to be merged, we recommend that you include your new elements within new container elements (tabs or sections). Additions to any container will be appended to the end of the container. For example, fields added to a section will be positioned at the end of the section. It is expected that a customizer installing a solution will then modify the form to re-arrange elements after it is installed.  
  
 Managed solutions that contain forms that use new security roles depend on those roles. You should include these security roles with your managed solution. If there are security roles associated with a form that are not in the organization that the managed solution is being installed on, the installation will not fail but the forms may not be associated with any security roles. When the managed solution is uninstalled, any security roles included with it will be removed. Any forms outside the managed solution can no longer be associated with those security roles.  
  
> [!NOTE]
>  When a managed solution entity contains multiple forms and the organization entity form also contains multiple forms, the new forms are not appended to the bottom of the list of available forms – they are interleaved with the original entity forms.  
  
<a name="BKMK_MergingNavigationCustomizations"></a>   
## Merge navigation (SiteMap) customizations  
 When a solution is packaged as managed the SiteMap XML is compared to the original SiteMap XML and any other customizations made to the SiteMap. Only the differences are included in the managed solution. These differences include items that are changed, moved, added or removed. When the managed solution is installed in a new organization, the SiteMap changes are merged with the SiteMap XML found for the organization where the managed solution is being installed. A new SiteMap definition is what people see.  
  
 At this point, a customizer can export the SiteMap to an unmanaged solution and that SiteMap definition will include all the elements of the active SiteMap. A customizer can then modify the SiteMap and re-import it as an unmanaged customization.  Later, if the managed solution is uninstalled, the SiteMap XML that was imported with the managed solution will be referenced to remove the changes introduced with that managed solution. A new active SiteMap is then calculated.  
  
 Whenever a new visible element is added to the SiteMap, it appears at the bottom of whatever container it belongs in. For example, a new area appears at the bottom of the Navigation area. To position the elements that have been added, you must export the SiteMap, edit it to set the precise position and then import it again as an unmanaged solution.  
  
> [!NOTE]
>  Only one SiteMap customization can be applied between publishing. Any unpublished SiteMap customizations will be lost when a new SiteMap definition is imported.  
  
<a name="BKMK_MergingOptionSetOptions"></a>   
## Merge option set options  
 Each new option set option is initialized with an integer value assigned that includes an option value prefix. The option value prefix is a set of five digits prepended to the option value. An option value prefix is generated based on the solution publishers customization prefix but may be set to any value. The option value prefix helps differentiate new option set options created in the context of a specific solution publisher and reduces the opportunity for collisions of option values. Using the option value prefix is recommended but not required.  
  
 A managed solution usually updates or adds options for option sets that are already in the organization, for example, the account Category or Industry option sets. When a managed solution modifies the options available in an option set, all the options defined in the managed solution are available in the organization. When the managed solution is uninstalled, the option set options will be returned to their original state.  
  
### See also  
 [Plan for Solution Development](plan-solution-development.md)   
 [Use Managed Properties](use-managed-properties.md)   
 [Package and Distribute Extensions with CDS for Apps Solutions](package-distribute-extensions-use-solutions.md)   
 [Customize Entity Forms](/dynamics365/customer-engagement/developer/customize-dev/customize-entity-forms)   
 [Change Application Navigation using the SiteMap](/dynamics365/customer-engagement/developer/customize-dev/change-application-navigation-using-sitemap)
