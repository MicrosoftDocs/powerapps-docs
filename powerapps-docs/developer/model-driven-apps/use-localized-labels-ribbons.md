---
title: "Use localized labels with ribbons (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about using localized labels with ribbons." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "KumarVivek" # GitHub ID
ms.subservice: mda-developer
ms.author: "kvivek" # MSFT alias of Microsoft employees only
manager: "shilpas" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Use localized labels with ribbons

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/customize-dev/use-localized-labels-ribbons -->

Although Ribbon elements that display text allow for direct entry of text, it is a best practice to use localized labels to define text displayed in the ribbon. This enables multi-language capabilities and better management of shared text.  
  
## Using localized labels  

 The `<RibbonDiffXml>` element includes the `<LocLabels>` element. 
 As shown in the following example, this is where you can specify which text to display in the ribbon labels and tooltips using the `<Titles>` element.  
  
```xml  
<LocLabels>  
 <LocLabel Id="MyISV.account.SendToOtherSystem.LabelText">  
  <Titles>  
   <Title languagecode="1033"  
          description="Send to Other System" />  
  </Titles>  
 </LocLabel>  
 <LocLabel Id="MyISV.account.SendToOtherSystem.ToolTip">  
  <Titles>  
   <Title languagecode="1033"  
          description="Sends this Record to another system" />  
  </Titles>  
 </LocLabel>  
</LocLabels>  
```  
  
 Within the definition of a ribbon element that displays text, the following example show how the localized label can be referenced using the `$LocLabels:` directive.  
  
```xml  
ToolTipTitle="$LocLabels:MyISV.account.SendToOtherSystem.LabelText"  
ToolTipDescription="$LocLabels:MyISV.account.SendToOtherSystem.ToolTip"  
```  
  
## Force a line break in a ribbon control label  

 If you have a ribbon control label that is very long, the text will wrap to fit the available space. You can specify where you want to include a line break by using the following characters: `&#x200b;&#x200b;`.  
  
 If the label text is very long without a space for the text to wrap, the width of the control expands to allow for the entire label to be displayed.  
  
### See also  
 [Customize commands and the ribbon](customize-commands-ribbon.md)   
 [Export, prepare to edit, and import the Ribbon](export-prepare-edit-import-ribbon.md)   
 [Use localized labels with Ribbons](use-localized-labels-ribbons.md)   
 [Define Ribbon Commands](define-ribbon-commands.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]