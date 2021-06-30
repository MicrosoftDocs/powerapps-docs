---
title: "setDisabled (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the setDisabled method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 86383cb1-c4c8-4e82-9f60-1dc4588b519d
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# setDisabled (Client API reference)



Sets whether the control is disabled.

## Control types supported

All except **kbsearch** control type

## Syntax

`formContext.getControl(arg).setDisabled(bool);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|bool|Boolean|Yes|Specify **true** or **false** to disable or enable the control.|

### Related topics

[getDisabled](getDisabled.md)





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]