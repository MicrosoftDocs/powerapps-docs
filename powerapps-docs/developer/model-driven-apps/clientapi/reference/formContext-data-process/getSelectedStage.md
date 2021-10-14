---
title: "getSelectedStage (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getSelectedStage method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: ac9a8c97-ad4d-4ed8-8eb0-51b2693253dc
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getSelectedStage (Client API reference)



[!INCLUDE[./includes/getSelectedStage-description.md](./includes/getSelectedStage-description.md)]

## Syntax

`formContext.data.process.getSelectedStage();`

## Return Value

**Type**: Stage. 

**Description**: The currently selected stage. See [Stage methods](../formContext-data-process.md#stage-methods) for the methods to access the properties of the stage returned.

### Related topics

[getActiveStage (Client API reference)](activestage/getActiveStage.md)

[formContext.data.process](../formContext-data-process.md)
 




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]