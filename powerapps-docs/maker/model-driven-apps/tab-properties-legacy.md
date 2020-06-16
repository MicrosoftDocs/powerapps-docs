---
title: Tab properties for for model-driven app forms in Power Apps | MicrosoftDocs
description: Understand the tab properties for main forms
Keywords: Tab properties; Dynamics 365; Main forms
author: matp
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
ms.author: Mattp123
manager: kvivek
ms.date: 03/17/2020
ms.service: powerapps
ms.topic: article
ms.assetid: e0790865-c5a4-4e86-bce2-584af2b8ed93
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Tab properties for model-driven app forms overview

 In the body of a form, tabs provide horizontal separation. Tabs have a label that can be displayed. If the label is displayed, tabs can be expanded or collapsed to show or hide their content by choosing the label.  
  
 Tabs contain up to three columns and the width of each column can be set to a percentage of the total width. When you create a new tab, each column is pre-populated with a section.  

You can access **Tab properties** from the Power Apps site. 
1.  Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

2.  Expand **Data**, select **Entities**, select the entity that you want, and then select the **Forms** tab.  

3.  In the list of forms, open the form of type **Main**. Then select one of the tabs on the form to view the tab properties.

|Property|Description|  
|--------------|-----------------|  
|**Tab label**|**Required**: The localizable label for the tab visible to users.|  
|**Name**|**Required**: The unique name for the tab that is used when referencing it in scripts. The name can contain only alphanumeric characters and underscores.|  
|**Expand this tab by default**|The tab state can toggle between expanded or collapsed using form scripts or by people selecting the label. Choose the default state for the tab.|  
|**Hide tab**|Showing the tab is optional and can be controlled using scripts. Choose whether to make the tab visible. More information: [Visibility options](visibility-options-legacy.md)|  
|**Hide on phone**|Choose if you want the tab to be available on the phone. For a condensed version of this form on phone screens, you can hide the tab.|  
|**Formatting**|Tabs may have up to three columns. Use these options to set the number of tabs and what percentage of the total width they should fill.|  

  > [!div class="mx-imgBorder"] 
  > ![tab-properties](media/newform-tab-properties.png "Tab properties")

## Tab properties for model-driven app main forms: Classic

These are the properties available to configure when using a tab on a form using the classic form designer. The following table shows properties that you can set for tabs on the form:
  
|Tab|Property|Description|  
|---------|--------------|-----------------|  
|**Display**|**Name**|**Required**: The unique name for the tab that is used when referencing it in scripts. The name can contain only alphanumeric characters and underscores.|  
||**Label**|**Required**: The localizable label for the tab visible to users.|  
||**Show the label of this tab on the Form**|When the label is displayed people can select it to toggle whether the tab is expanded or collapsed. Choose whether you want to show the label.|  
||**Expand this tab by default**|The tab state can toggle between expanded or collapsed using form scripts or by people selecting the label. Choose the default state for the tab.|  
||**Visible by default**|Showing the tab is optional and can be controlled using scripts. Choose whether to make the tab visible. More information: [Visibility options](visibility-options-legacy.md)|  
||**Availability**|Choose if you want the tab to be available on the phone.|  
|**Formatting**|**Layout**|Tabs may have up to three columns. Use these options to set the number of tabs and what percentage of the total width they should fill.|  
|**Events**|**Form Libraries**|Specify any JavaScript web resources that will be used in the tab `TabStateChange` event handler.<br /><br />|  
||**Event Handlers**|Configure the functions from the libraries that should be called for the tab `TabStateChange` event. More information: [Configure Event Handlers](configure-event-handlers-legacy.md)|  

  > [!div class="mx-imgBorder"] 
  > ![tab-properties classic](media/tab-properties.png "Tab properties in Classic")

## Next steps

[Use the Main form and its components](use-main-form-and-components.md)
