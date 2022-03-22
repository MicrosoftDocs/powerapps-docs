---
title: "setDisabled (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the setDisabled method.
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