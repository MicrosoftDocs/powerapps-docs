---
title: "Define ribbon actions (model-driven apps)"
description: "Learn about defining the actions to be performed by a command bar or ribbon control in a <CommandDefinition> element together with rules that control whether the control is enabled or visible in the ribbon."
author: clromano
ms.author: clromano
ms.date: 05/24/2022
ms.reviewer: jdaly
ms.topic: article
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---

# Define ribbon actions

[!INCLUDE [cc-modern-commanding](../data-platform/includes/cc-modern-commanding.md)]

Define the actions to be performed by a command bar or ribbon control in a `<CommandDefinition>` element together with rules that control whether the control is enabled or visible in the ribbon.  
  
 A Ribbon control can perform two types actions and may include multiple actions:  
  
- **JavaScript Functions**: A `<JavaScriptFunction>` element references a function defined in a [JavaScript web resource](./script-jscript-web-resources.md).  
  
- **Open a URL**: The ribbon opens a URL using the value from an Address attribute in the `<Url>` element. Additional parameters can pass information about how what querystring parameters are passed and the mode in which the window opens.  
  
     You have several options to pass parameters to a URL using the ribbon. More information: [Passing Parameters to a URL using the Ribbon](pass-parameters-url-by-using-ribbon.md)  
  
## Passing parameters to ribbon actions  

 Use the following elements to define data to pass to your custom action:  
  
 `<BoolParameter>`  
[!INCLUDE[ribbon_element_BoolParameter](../../includes/ribbon-element-boolparameter.md)]
  
 `<CrmParameter>`  
 [!INCLUDE[ribbon_element_CrmParameter](../../includes/ribbon-element-crmparameter.md)] More information: [Pass data from a page as a parameter to Ribbon Actions](pass-data-page-parameter-ribbon-actions.md) 
  
 `<DecimalParameter>`  
 [!INCLUDE[ribbon_element_DecimalParameter](../../includes/ribbon-element-decimalparameter.md)]
  
 `<IntParameter>`  
 [!INCLUDE[ribbon_element_IntParameter](../../includes/ribbon-element-intparameter.md)]
  
 `<StringParameter>`  
 [!INCLUDE[ribbon_element_StringParameter](../../includes/ribbon-element-stringparameter.md)]
  
 When parameters are passed to a `<Url>` element they are passed as a query string. Therefore, they must include a name value to represent the "key" in the query string key/value pair.  
  
 Parameters passed to a `<JavaScriptFunction>` do not require a name but they must be included in the order expected by the function and be of the correct data type.  
  
## See also  

 [Customize commands and the ribbon](customize-commands-ribbon.md)   
 [Define Ribbon display rules](define-ribbon-display-rules.md)   
 [Pass data from a page as a parameter to Ribbon actions](pass-data-page-parameter-ribbon-actions.md)  




[!INCLUDE[footer-include](../../includes/footer-banner.md)]
