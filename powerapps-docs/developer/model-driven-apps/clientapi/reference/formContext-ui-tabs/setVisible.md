---
title: "setVisible (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
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

### Related topics

[getVisible](getVisible.md)



