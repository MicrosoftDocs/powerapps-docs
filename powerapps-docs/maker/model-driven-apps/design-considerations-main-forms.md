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
ms.subservice: mda-maker
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Design considerations for model-driven app main forms

Main forms are the primary user interface where people view and interact with their data. Main forms provide the widest range of presentation options that are available for model-driven apps.

Other [form types](../../maker/model-driven-apps/types-forms.md) include Quick view, Quick Create and Card.
  
One of the fundamental qualities of model-driven apps is that they are responsive to the size and type of device used when interacting with them.  This affects the position of the controls on the form in addition to the way in which they behave.  This is most notably the case with main forms.

One of the main design objectives for main forms is that they are designed once per table and deployed everywhere required. The same main form designed for a model-driven app is also used in Dynamics 365 for Outlook and Dynamics 365 for tablets. The advantage to this approach is that it is not necessary to integrate changes into multiple forms.

However there are several important factors to consider in designing these forms.  
  
<a name="BKMK_CustomFormsForGroups"></a>   

## Custom forms for different groups

Because multiple main forms can be created and assigned to different security roles, it is possible to present different groups in an organization with a form that is optimized for how the group uses the application. It is also possible to provide each group with different options so that they have different forms to choose from. More information: [Control access to forms](control-access-forms.md)  
  
Managers and decisions makers will want forms that are optimized to provide quick reference to key data points. They will like to see charts more than lists and they may not perform a lot of data entry.  
  
People who interact directly with customers may need forms tailored to tasks they perform most frequently. They may want forms that allow for the most efficient data entry.  
  
Form creation might be an iterative process where input is gathered and the user interface is developed. Keep in mind that there are a variety of tools available to developers and that not everything has to be done within the form. Use [business rules](../model-driven-apps/model-driven-app-glossary.md#business-rule), workflow processes, dialogs and [business process flows](../model-driven-apps/model-driven-app-glossary.md#business-process-flow) together with main forms to provide a solution that works for the organization.  
  
Creating and editing forms is relatively easy, but as more forms are created more forms need to be maintained.  
  
<a name="BKMK_PresentationDifferences"></a>   
## Form presentation differences

Although it is not necessary to manage multiple forms for each delivery mechanism (web, tablet, phone), a maker must consider how differences in the presentation can be accounted for in the main form.
 
[Main form appearance](main-form-presentations.md) describes the different ways that the main form may be presented. The primary things to take into consideration are:  
  
- Dynamics 365 for tablets doesn’t support image, HTML, or Silverlight web resources to be added to forms.  
  
- The layout of Dynamics 365 for tablets forms is auto-generated based on the main form. There is no special form editor for Dynamics 365 for tablets forms.  It is necessary to verify that the form presentation works well for both clients.  
  
- If there are unsupported scripts that interact with DOM elements found in the web application, those scripts won’t work in the Dynamics 365 for tablets forms because the same DOM elements aren’t available.  
  
- Dynamics 365 for Outlook Reading Pane forms don’t allow for scripting. The visibility of form elements depend on the default settings and can’t be changed at runtime using scripts.  
  
<a name="BKMK_FormPerformance"></a>
## Form performance

Forms that load slowly or don’t respond quickly might affect productivity and user adoption of the app. [Design forms for performance in model-driven apps](design-performant-forms.md) provides a number of recommendations to be considered when designing forms so that customizations don’t adversely affect form performance.  

## Design forms for efficiency

Form layout and design are important to building better forms. Designing forms where tasks can be completed quickly and effectively is crucial to user satisfaction. More information: [Design productive main forms in model-driven apps](design-productive-forms.md)

## Next steps

 [Create or edit a main form overview](create-edit-main-forms.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]