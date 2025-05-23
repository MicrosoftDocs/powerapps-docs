---
title: "addOption (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the addOption method.
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
# addOption (Client API reference)

Adds an option to a control. 

## Control types supported

Choice, Choices

## Syntax

`formContext.getControl(arg).addOption(option, index);`

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Parameters

|Name | Type | Required | Description|
|----|----|----|----|
|`option` |Object |Yes|The option to add. The object contains the following:<br/>**- `text`**: String. The label for the option.<br/>**- `value`**: Number. The value for the option.|
|`index` |Number |No|The index position to place the new option in. If not provided, the option will be added to the end.|

### Related articles

[clearOptions](clearOptions.md)   
[removeOption](removeOption.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
