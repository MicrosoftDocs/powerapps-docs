---
title: "reflow (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 6833e4ea-70fc-4ee0-8aab-68cc55e21444
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# reflow (Client API reference)



[!INCLUDE[./includes/reflow-description.md](./includes/reflow-description.md)]

## Syntax

`formContext.ui.process.reflow(updateUI, parentStage, nextStage);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|updateUI|Boolean|Yes|Specify **true** to update the UI of the process control; **false** otherwise.|
|parentStage|String|Yes|Specify the ID of the parent stage in the GUID format.|
|nextStage|String|Yes|Specify the ID of the next stage in the GUID format.|

### Related topics

[formContext.ui.process](../formContext-ui-process.md)



