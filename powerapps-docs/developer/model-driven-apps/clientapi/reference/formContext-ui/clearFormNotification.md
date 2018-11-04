---
title: "clearFormNotification (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 6c57db71-a76d-404c-852e-9c36a1c549ee
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# clearFormNotification (Client API reference)



[!INCLUDE[./includes/clearFormNotification-description.md](./includes/clearFormNotification-description.md)]

## Syntax

`formContext.ui.clearFormNotification(uniqueId)`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|uniqueId|String|Yes|A unique identifier for the message to be cleared that was set using the [setFormNotification](setFormNotification.md) method.|

## Return Value

**Type**: Boolean

**Description**: true if the method succeeded, false otherwise. 


### Related topics

[setFormNotification](setFormNotification.md)

[formContext.ui](../formContext-ui.md)

[formContext](../../clientapi-form-context.md)

