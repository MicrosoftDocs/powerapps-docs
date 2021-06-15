---
title: "Design considerations for model-driven app main forms with Power Apps | MicrosoftDocs"
description: "Learn how to design main forms"
ms.custom: ""
ms.date: 06/27/2018
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: a83872f4-9e36-413b-8561-41a1e5ffe5dd
caps.latest.revision: 17
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Design considerations for model-driven app main forms

Main forms are the primary user interface where people view and interact with their data. Main forms provide the widest range of options and are available for model-driven apps, the exception being Dynamics 365 for phones.  
  
 One of the main design objectives for main forms is that you design them once and deploy them everywhere. The same main form you design for a model-driven app is also used in Dynamics 365 for Outlook and Dynamics 365 for tablets. The advantage to this approach is that you don’t have to integrate changes into multiple forms. However there are several important factors to consider in designing these forms.  
  
<a name="BKMK_CustomFormsForGroups"></a>   

## Custom forms for different groups  
 Because you can create multiple main forms and assign different security roles to each form you can present different groups in your organization with a form that is optimized for how they use the application. You can even provide each group with different options so that they have different forms to choose from. More information: [Control access to forms](control-access-forms.md)  
  
 You can expect that managers and decisions makers will want forms that are optimized to provide quick reference to key data points. They will like to see charts more than lists and they may not perform a lot of data entry.  
  
 People who interact directly with customers may need forms tailored to tasks they perform most frequently. They may want forms that allow for the most efficient data entry.  
  
 You’ll need to find out what people in your organization want and need. This is frequently an iterative process where you gather input, try different things and build forms that people can use. Keep in mind that you have a variety of tools available to you and that not everything has to be done within the form. Use business rules, workflow processes, dialogs and business process flows together with your forms to provide a solution that works for your organization.  
  
 You’ll have to balance this with the amount of time you want to spend managing forms. Creating and editing forms is relatively easy, but as you create more forms, you have to manage more forms.  
  
<a name="BKMK_PresentationDifferences"></a>   
## Presentation differences  
 Although you don’t have to manage multiple forms for each presentation, you must consider how differences in the presentation can be accounted for in the main form. [Main form presentations](main-form-presentations.md) describes the different ways that the main form may be presented. The primary things to take into consideration are:  
  
- Dynamics 365 for tablets doesn’t support image, HTML, or Silverlight web resources to be added to forms.  
  
-   The layout of Dynamics 365 for tablets forms is auto-generated based on the main form. There is no special form editor for Dynamics 365 for tablets forms. You need to verify that the form presentation works well for both clients.  
  
-   If you have unsupported scripts that interact with DOM elements found in the web application, those scripts won’t work in the Dynamics 365 for tablets forms because the same DOM elements aren’t available.  
  
- Dynamics 365 for Outlook Reading Pane forms don’t allow for scripting. The visibility of form elements depend on the default settings and can’t be changed at runtime using scripts.  
  
<a name="BKMK_FormPerformance"></a>   
## Form performance  
 Forms that load slowly or don’t respond quickly are sure to affect productivity and user adoption of the app. [Optimize form performance](optimize-form-performance.md) provides a number of recommendations you should consider when designing forms so that customizations don’t adversely affect form performance.  
  
### Next steps 
 [Create and design forms](create-design-forms.md)    
 [Create and edit quick create forms](create-edit-quick-create-forms.md)   

 


[!INCLUDE[footer-include](../../includes/footer-banner.md)]