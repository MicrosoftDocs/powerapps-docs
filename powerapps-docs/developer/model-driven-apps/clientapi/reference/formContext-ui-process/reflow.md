---
title: "reflow (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the reflow method.
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
# reflow (Client API reference)

[!INCLUDE[./includes/reflow-description.md](./includes/reflow-description.md)]

## Syntax

`formContext.ui.process.reflow(updateUI, parentStage, nextStage);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|updateUI|Boolean|No|Specify **true** to update the UI of the process control; **false** otherwise.|
|parentStage|String|No|Specify the ID of the parent stage in the GUID format.|
|nextStage|String|No|Specify the ID of the next stage in the GUID format.|

### Related topics

[formContext.ui.process](../formContext-ui-process.md)





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]