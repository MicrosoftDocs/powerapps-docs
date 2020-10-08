---
title: "setContentType (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/09/2020
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
# setContentType (Client API reference)

[!INCLUDE[./includes/setContentType-description.md](./includes/setContentType-description.md)] 

## Syntax

`formContext.ui.tabs.get(tab-name).setContentType(expandAvailableSpace);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|expandAvailableSpace|String|Yes| The first visible component of the form is maximized to fill the whole space allocated to the form.|
||||

### Related topics

[formContext.ui.tabs](../formContext-ui-tabs.md)