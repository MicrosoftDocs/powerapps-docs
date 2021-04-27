---
title: "getActiveStage (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getActiveStage method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 57a17f91-38f2-4666-bd23-0b7c63b0516f
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getActiveStage (Client API reference)



[!INCLUDE[./includes/getActiveStage-description.md](./includes/getActiveStage-description.md)]

## Syntax

`formContext.data.process.getActiveStage();`

## Return Value

**Type**: Stage. 

**Description**: The currently active stage. See [Stage methods](../../formContext-data-process.md#stage-methods) for the methods to access the properties of the stage returned.

### Related topics

[setActiveStage)](setActiveStage.md)

[getSelectedStage (Client API reference)](../getSelectedStage.md)

[formContext.data.process](../../formContext-data-process.md)
 




[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]