---
title: "clearNotification (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 4d025f92-db16-440c-9f82-e40d71e09862
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# clearNotification (Client API reference)



Remove a message already displayed for a control.

## Control types supported

All

## Syntax

`formContext.getControl(arg).clearNotification(uniqueId);`

## Parameters

|Name | Type | Required | Description|
|--|--|--|--|
|uniqueId |String |No|The ID to use to clear a specific message that was set using **setNotification** or **addNotification**. If the **uniqueId** parameter isn’t specified, the currently displayed notification will be cleared.| 


## Return Value

**Type**: Boolean 

**Description**: Indicates whether the method succeeded. 

### Related topics

[addNotification](addNotification.md)

[setNotification](setNotification.md)