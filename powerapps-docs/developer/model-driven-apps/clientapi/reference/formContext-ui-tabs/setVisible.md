---
title: "setVisible (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the setVisible method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 485d9843-5907-49e4-971b-0e86f3bd1eb8
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# setVisible (Client API reference)



[!INCLUDE[./includes/setVisible-description.md](./includes/setVisible-description.md)] 

## Syntax

`tabObj.setVisible(bool);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|bool|Boolean|Yes|Specify **true** to show the tab; **false** to hide the tab.|

## Remarks

Another way to hide a tab is to hide all the sections within it. If all the sections within a tab are not visible, the tab will not be visible.

> [!NOTE]
> If you set the value to false, the first visible tab is shown by default. If there are no visible tabs, the body of the form will show as a blank page.

### Related topics

[getVisible](getVisible.md)





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]