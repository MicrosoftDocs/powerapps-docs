---
title: "setRequiredLevel (Client API reference)| MicrosoftDocs"
description: Includes description and supported parameters for the setRequiredLevel method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 67a96fc4-4d65-4858-90da-f41eeba0365a
author: "Nkrb"
ms.subservice: mda-developer
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# setRequiredLevel (Client API reference)

Sets whether data is required or recommended for the column before the record can be saved.

> [!IMPORTANT]
> Reducing the required level of a column can cause an error when the page is saved. If the column is required by the server, an error will occur if there is no value for the column. 

## Column types supported

All

## Syntax

`formContext.getAttribute(arg).setRequiredLevel(requirementLevel)`

## Parameters

**Type**: String. 

**Description**: Set the level to one of the following values:
- none
- required
- recommended

### Related topic
[getRequiredLevel (Client API reference)](getRequiredLevel.md)




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]