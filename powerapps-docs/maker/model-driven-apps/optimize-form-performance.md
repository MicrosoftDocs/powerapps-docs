---
title: "Optimize model-driven app form performance in Power Apps | MicrosoftDocs"
description: "Learn how to avoid form designs that cause a form to load slowly"
ms.custom: ""
ms.date: 04/24/2020
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
author: "Mattp123"
ms.assetid: 59cfa5e6-638a-437f-a462-fddfd26fb07d
caps.latest.revision: 8
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Optimize model-driven app form performance

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Forms that load slowly can reduce productivity and user adoption. Follow these recommendations to maximize how quickly your forms will load. Many of these recommendations are about how a developer may implement form scripts for your organization. Be sure to discuss these recommendations with developers who create form scripts for your forms.  
  
<a name="BKMK_FormDesign"></a>   
## Form design  
 Think about the interaction the user will have with the form and the amount of data that must be displayed within it.  
  
 **Keep the number of table columns to a minimum**  
 The more table columns (formerly referred to as fields) you have in a form, the more data that needs to be downloaded to view each record.
 
 **Design for performance**  
 When designing forms and pages, put what is most important at the top to make it most easily accessible for your users. Move infrequently used components to other tabs on a form, use role-based forms instead of showing and hiding components, and make sure that different workflows have dedicated dashboards and views. Feel free to use sections to organize your controls – this won’t make your forms slower.
 
<a name="BKMK_FormScripts"></a>   
## Form scripts  
 When you have customizations using form scripts make sure that the developer understands these strategies to improve performance. 
 
**Minimize the number of network requests and the amount of data requested in the OnLoad event**  
The higher the number of network requests made during a form load, and the more amount of data downloaded from those requests, the more time it will take for a form to load. Only request the minimum amount of data needed. Also, consider caching the data when possible to avoid requesting data unnecessarily on future page loads.
  
**Avoid using synchronous network requests**  
Synchronous network requests can cause slow page loads and unresponsive forms. [Use asynchronous requests instead](../../developer/model-driven-apps/best-practices/business-logic/interact-http-https-resources-asynchronously.md). See [this blog post](https://powerapps.microsoft.com/en-us/blog/turbocharge-your-model-driven-apps-by-transitioning-away-from-synchronous-requests/) for more examples.
  
**Avoid including unnecessary JavaScript web resource libraries**  
The more scripts you add to the form, the more time it will take to download them. Usually scripts are cached in your browser after they are loaded the first time, but the performance the first time a form is viewed often creates a significant impression.  
  
**Avoid loading all scripts in the Onload event**  
If you have code that only supports `OnChange` events for columns or the `OnSave` event, make sure to set the script library with the event handler for those events instead of the `OnLoad` event. This way loading those libraries can be deferred and increase performance when the form loads.  
  
 **Use collapsed tabs to defer loading web resources**  
 When web resources or IFRAMES are included in sections inside a collapsed tab they will not be loaded if the tab is collapsed. They will be loaded when the tab is expanded. When the tab state changes the `TabStateChange` event occurs. Any code that is required to support web resources or IFRAMEs within collapsed tabs can use event handlers for the **TabStateChange** event and reduce code that might otherwise have to occur in the `OnLoad` event.  
  
**Set default visibility options**  
Avoid using form scripts in the `OnLoad` event that hide form elements. Instead set the default visibility options for form elements that might be hidden to not be visible by default when the form loads. Then, use scripts in the `OnLoad` event to show those form elements you want to display.  
  
<a name="BKMK_CommandBar"></a>   
## Command bar or ribbon  
 Keep these recommendations in mind as you edit the command bar or ribbon.  
  
 **Keep the number of controls to a minimum**  
 Within the command bar or the ribbon for the form, evaluate what controls are necessary and hide any that you don’t need. Every control that is displayed increases resources that need to be downloaded to the browser.
 
 **Use asynchronous network requests in Custom Rules**  
 When using custom rules that make network requests in Unified Interface, [use asynchronous rule evaluation](../../developer/model-driven-apps/define-ribbon-enable-rules.md#custom-rule).
  
## Next steps  
 [Create and design forms](create-design-forms.md)    
    
 


[!INCLUDE[footer-include](../../includes/footer-banner.md)]