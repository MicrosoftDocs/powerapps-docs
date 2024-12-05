---
title: "removeOption (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the removeOption method.
author: MitiJ
ms.author: mijosh
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# removeOption (Client API reference)

Removes an option from a control.

## Control types supported

choice, choices

## Syntax

`formContext.getControl(arg).removeOption(value);`

## Parameters

|Name | Type | Required | Description|
|----|----|----|----|
|`value` |Number |Yes|The value of the option you want to remove.|

### Related articles

[addOption](addOption.md)   
[clearOptions](clearOptions.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
