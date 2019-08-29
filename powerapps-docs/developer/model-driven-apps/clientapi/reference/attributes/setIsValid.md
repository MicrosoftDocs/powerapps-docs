---
title: "setIsValid (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 08/28/2019
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# setIsValid (Client API reference)

Sets a value for an attribute to determine whether it is valid or invalid with a message.

## Attribute types supported

All

## Syntax 

`formContext.getAttribute(arg).setIsValid(bool, message);` 

## Parameters

|Name|Type|Required|Description|
|----|----|------|------------|
|bool|Boolean|Yes|Specify false to set the attribute value to invalid and true to set the value to valid|
|message|String|No|The message to display| 
