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

> [!NOTE]
> This method is supported only on the Unified Interface.

## Syntax

`tabObj.setContentType(contentType);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|contentType|String|Yes| Defines the content type. It has the following parameters: <br/> - **cardSection**: The default tab behavior. <br/> - **singleComponent**: Maximizes the content of the first custom component. |
||||

### Related topics

[getContentType](getContentType.md)