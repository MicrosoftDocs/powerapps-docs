---
title: "Define custom actions to modify the ribbon (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "Learn about defining custom actions to modify the ribbon." # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: article
ms.assetid: 72544b02-4eed-4d70-666e-a0d880f526af
author: Nkrb # GitHub ID
ms.subservice: mda-developer
ms.author: nabuthuk # MSFT alias of Microsoft employees only
manager: shilpas # MSFT alias of manager or PM counterpart
ms.reviewer: 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Define custom actions to modify the ribbon

The default, an application command bar or ribbon is defined by Microsoft Dataverse metadata. This default data can’t be changed, but you can include definitions of specific actions that will override the default ribbon.  
  
## Types of custom actions

 There are two types of custom actions for ribbons:  
  
- `<CustomAction>`: [!INCLUDE[ribbon_element_CustomAction](../../includes/ribbon-element-customaction.md)]  
  
- `<HideCustomAction>` : [!INCLUDE[ribbon_element_HideCustomAction](../../includes/ribbon-element-hidecustomaction.md)]  
  
### Custom actions  

 A custom action is a statement of how you want to change the default ribbon definition. It is evaluated and applied to the ribbon at runtime. To set the context for a custom action, you must include information about the location of the items that you want to change. Use the `Location` parameter to specify where your change applies.  
  
 When you add a new ribbon element, you refer to the containing element, for example, an existing tab or group. You then include the suffix `._children` to indicate that this custom action will add something to an existing item.  
  
 When you change the definition of an existing item, the `Location` value will match the ID of that item.  
  
 You must also specify a unique identifier for the custom action. Use the **Id** parameter to set this value. We strongly recommend that you use a naming convention that will guarantee a unique value. For consistency and readability, we recommend that you use a period to separate consistent components. The first item in your naming convention should be something related to your solutions publisher or solution, for example, `Contoso.contact.form.CustomButton.CustomAction`.  
  
> [!TIP]
> Consistently applying your `Id` parameter naming conventions will greatly enhance your productivity while editing RibbonDiffXml.  
  
 Based on the location information that you provide, the `Sequence` value determines the order in which to render items. If you want a custom control to appear between two existing controls, you must select a sequence value that is in between the sequence values of the existing items.  
  
### Hide custom actions  

 A `<HideCustomAction>` is a statement that you use when you want to remove an existing ribbon element so that it is not rendered. This does not hide the ribbon element, it actually removes the ribbon element at runtime so that it doesn’t exist in the ribbon.  

The **HideActionId** element provides a unique ID for the action. For consistency and readability, you should follow the same naming convention described for `<CustomAction>` elements. The **Location** parameter must match the Id of the ribbon element you want to remove.  
  
> [!NOTE]
> Because the `HideCustomAction` element removes a specified node from the ribbon, removing ribbon elements in this manner may not be the best option for every situation.  
> 
> - If you want to remove a button that is associated with a specific privilege, you should adjust the privileges for the table in the security roles in your implementation. This will allow the default ribbon display and enables rules to hide or disable ribbon elements from users who do not have the necessary privileges to perform those actions.  
>   -   If you want to replace an existing ribbon element with a custom ribbon element, you can overwrite that element by specifying a `CustomAction.Location` value identical to the existing element.  
> - To remove the `HideCustomAction` element you need to create a new updated version of the same solution that installed the `HideCustomAction` element. A new patch of the solution cannot remove the `HideCustomAction` element.

The `HideCustomAction` element cannot be removed, once added, except by creating a new updated solution. Instead, ribbon buttons should be hidden using a `DisplayRule` element that always evaluate to false. Having both `Mscrm.HideOnModern` and `Mscrm.ShowOnlyOnModern` would always evaluate to false. For example, to hide a deactivate button:

```xml
<CommandDefinition Id="Mscrm.HomepageGrid.Deactivate">
    <EnableRules>
      </EnableRules>
      <DisplayRules>
        <DisplayRule Id="Mscrm.HideOnModern" />
        <DisplayRule Id="Mscrm.ShowOnlyOnModern" />
      </DisplayRules>
      <Actions>
        </Actions>
    </CommandDefinition>
```
  

  
### See also  

[Customize commands and the ribbon](customize-commands-ribbon.md)   
[Pass data from a page as a parameter to ribbon actions](/dynamics365/customerengagement/on-premises/developer/customize-dev/pass-dynamics-365-data-page-parameter-ribbon-actions)<br> 
[Define scaling for ribbon elements](define-scaling-ribbon-elements.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]