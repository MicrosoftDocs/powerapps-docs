---
title: "setContentType (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the setContentType method.
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
# setContentType (Client API reference)

[!INCLUDE[./includes/setContentType-description.md](./includes/setContentType-description.md)] 

> [!NOTE]
> This method is supported only on Unified Interface.

## Syntax

`tabObj.setContentType(contentType);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|contentType|String|Yes| Defines the content type. It has the following parameters: <br/> - **cardSections**: The default tab behavior. <br/> - **singleComponent**: Maximizes the content of the first component in the tab. |
||||

### Related topics

[getContentType](getContentType.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]