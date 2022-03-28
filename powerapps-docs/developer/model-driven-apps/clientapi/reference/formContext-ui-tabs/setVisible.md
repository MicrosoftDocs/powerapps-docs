---
title: "tab.setVisible (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the tab.setVisible method.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# tab.setVisible (Client API reference)



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