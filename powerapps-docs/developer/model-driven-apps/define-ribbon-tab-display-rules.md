---
title: "Define ribbon tab display rules (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "Learn about defining ribbon tab displays rules." # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 04/14/2021
ms.service: powerapps
ms.custom:
  - ""
ms.topic: article
ms.assetid: 916f4e82-01a3-2476-c2a4-ff71caa4195c
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

# Define ribbon tab display rules

Tab display rules control whether a specific tab is displayed for a ribbon or not.  
  
Unlike other ribbon elements like groups or specific controls, you must explicitly provide a tab display rule for a tab to be displayed in the ribbon. By default, other ribbon elements will always display unless a display rule removes them.  
  
 `<TabDisplayRule>` elements require that the `TabCommand` parameter matches a `<Tab>` `Command` value.  
  
In the `RibbonDiffXml`, tabs can be defined for specific tables or defined globally. If the tab is defined for a table, the only valid type of rule is `<EntityRule>`. Because defining a tab in the scope of a particular table already limits the tab to only that table, the only valid parameters are `AppliesTo` (`PrimaryEntity` or `SelectedEntity`) and `Context` (`Form`, `HomePageGrid`, `SubGridStandard`, or `SubGridAssociated`).  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

When you define a tab display rule globally in the `RibbonDiffXml` for the application ribbons, you can apply both `EntityRule` elements and `<PageRule>` elements.  
  
### See also  
 [Customize commands and the ribbon](customize-commands-ribbon.md)   
 [Define scaling for ribbon elements](define-scaling-ribbon-elements.md)   
 [Pass parameters to a URL by using the ribbon](pass-parameters-url-by-using-ribbon.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]