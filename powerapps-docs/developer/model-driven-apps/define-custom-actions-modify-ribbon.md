---
title: "Define custom actions to modify the ribbon (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "Learn about defining custom actions to modify the ribbon." # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 10/31/2018
ms.service:
  - "powerapps"
ms.custom:
  - ""
ms.topic: article
ms.assetid: 72544b02-4eed-4d70-666e-a0d880f526af
author: JimDaly # GitHub ID
ms.author: jdaly # MSFT alias of Microsoft employees only
manager: shilpas # MSFT alias of manager or PM counterpart
ms.reviewer: 
---

# Define custom actions to modify the ribbon

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/customize-dev/define-custom-actions-modify-ribbon -->

The default, an application command bar or ribbon is defined by Common Data Service for Apps metadata. This default data can’t be changed, but you can include definitions of specific actions that will override the default ribbon.  
  
## Types of custom actions  
 There are two types of custom actions for ribbons:  
  
- `<CustomAction>`: [!INCLUDE[ribbon_element_CustomAction](../../includes/ribbon-element-customaction.md)]  
  
- `<HideCustomAction>` : [!INCLUDE[ribbon_element_HideCustomAction](../../includes/ribbon-element-hidecustomaction.md)]  
  
### Custom actions  
 A custom action is a statement of how you want to change the default ribbon definition. It is evaluated and applied to the ribbon at runtime. To set the context for a custom action, you must include information about the location of the items that you want to change. Use the `Location` attribute to specify where your change applies.  
  
 When you add a new ribbon element, you refer to the containing element, for example, an existing tab or group. You then include the suffix `._children` to indicate that this custom action will add something to an existing item.  
  
 When you change the definition of an existing item, the `Location` value will match the ID of that item.  
  
 You must also specify a unique identifier for the custom action. Use the **Id** attribute to set this value. We strongly recommend that you use a naming convention that will guarantee a unique value. For consistency and readability, we recommend that you use a period to separate consistent components. The first item in your naming convention should be something related to your solutions publisher or solution, for example, `Contoso.contact.form.CustomButton.CustomAction`.  
  
> [!TIP]
>  Consistently applying your `Id` attribute naming conventions will greatly enhance your productivity while editing RibbonDiffXml.  
  
 Based on the location information that you provide, the `Sequence` attribute value determines the order in which to render items. If you want a custom control to appear between two existing controls, you must select a sequence value that is in between the sequence values of the existing items.  
  
### Hide custom actions  
 A `<HideCustomAction>` is a statement that you use when you want to remove an existing ribbon element so that it is not rendered. This does not hide the ribbon element, it actually removes the ribbon element at runtime so that it doesn’t exist in the ribbon.  
  
> [!NOTE]
>  Because the `HideCustomAction` element removes a specified node from the ribbon, removing ribbon elements in this manner may not be the best option for every situation.  
> 
> - If you want to remove a button that is associated with a specific privilege, you should adjust the privileges for the entity in the security roles in your implementation. This will allow the default ribbon display and enables rules to hide or disable ribbon elements from users who do not have the necessary privileges to perform those actions.  
>   -   If you want to replace an existing ribbon element with a custom ribbon element, you can overwrite that element by specifying a `CustomAction.Location` value identical to the existing element.  
  
 The **HideActionId** element provides a unique ID for the action. For consistency and readability, you should follow the same naming convention described for `<CustomAction>` elements. The **Location** attribute must match the Id of the ribbon element you want to remove.  
  
### See also  
 [Customize commands and the ribbon](customize-commands-ribbon.md)   
 [Pass data from a page as a parameter to Ribbon Actions](/dynamics365/customer-engagement/developer/customize-dev/pass-dynamics-365-data-page-parameter-ribbon-actions)<br/>   <!-- TODO need to update the relevant PowerApps repo link-->
 [Define Scaling for Ribbon Elements](define-scaling-ribbon-elements.md)
