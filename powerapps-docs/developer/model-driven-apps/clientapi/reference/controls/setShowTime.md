---
title: "setShowTime (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 77999c82-3d6a-4db9-af9c-7322491768d9
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# setShowTime (Client API reference)



Specify whether a date control should show the time portion of the date. 

## Control types supported

standard control for **datetime** attributes.

## Syntax

`formContext.getControl(arg).setShowTime(bool);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|bool|Boolean|Yes|Specify true to show the time portion of the date; false otherwise.|

## Remarks

This method will show or hide the time component of a date control where the attribute uses the **DateAndTime** format. This method will have no effect when the **DateOnly** format is used.

### Related topics

[getShowTime](getShowTime.md)

