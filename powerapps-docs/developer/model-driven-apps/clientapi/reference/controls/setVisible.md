---
title: "setVisible (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the setVisible method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 21368fac-d4bc-4f75-8a9c-cce098fa0b45
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

Sets a value that indicates whether the control is visible. 

## Control types supported

All

## Syntax

`formContext.getControl(arg).setVisible(bool);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|bool|Boolean|Yes|Specify **true** to show the control; **false** to hide the control.|

>[!NOTE]
> If a control is set to false and is in a section that is hidden and if you set the control to true, the section will be visible.

### Related topics

[getVisible](getVisible.md)





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]