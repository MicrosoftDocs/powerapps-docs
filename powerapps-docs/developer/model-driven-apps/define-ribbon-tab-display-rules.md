---
title: "Define ribbon tab display rules (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "Learn about defining ribbon tab displays rules." # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 10/31/2018
ms.service:
  - "powerapps"
ms.custom:
  - ""
ms.topic: article
ms.assetid: 916f4e82-01a3-2476-c2a4-ff71caa4195c
author: JimDaly # GitHub ID
ms.author: jdaly # MSFT alias of Microsoft employees only
manager: shilpas # MSFT alias of manager or PM counterpart
ms.reviewer: 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Define ribbon tab display rules

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/customize-dev/define-ribbon-tab-display-rules -->

Tab display rules control whether a specific tab is displayed for a ribbon or not.  
  
 Unlike other ribbon elements like groups or specific controls, you must explicitly provide a tab display rule for a tab to be displayed in the ribbon. By default, other ribbon elements will always display unless a display rule removes them.  
  
 `<TabDisplayRule>` elements require that the `TabCommand` attribute matches a `<Tab>` `Command` attribute value.  
  
 In the `RibbonDiffXml`, tabs can be defined for specific entities or defined globally. 
 If the tab is defined for an entity, the only valid type of rule is `<EntityRule>`. 
 Because defining a tab in the scope of a particular entity already limits the tab to only that entity, the only valid attributes are `AppliesTo` (`PrimaryEntity` or `SelectedEntity`) and `Context` (`Form`, `HomePageGrid`, `SubGridStandard`, or `SubGridAssociated`).  
  
 When you define a tab display rule globally in the `RibbonDiffXml` for the application ribbons, you can apply both `EntityRule` elements and `<PageRule>` elements.  
  
### See also  
 [Customize commands and the ribbon](customize-commands-ribbon.md)   
 [Define Scaling for Ribbon Elements](define-scaling-ribbon-elements.md)   
 [Pass Parameters to a URL By Using the Ribbon](pass-parameters-url-by-using-ribbon.md)