---
title: "addOption (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the addOption method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 9798f168-7b94-411d-9aed-6471042ff11a
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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
|--|--|--|--|
|option |Object |Yes|The option to add. The object contains the following:<br/>**- text**: String. The label for the option.<br/>**- value**: Number. The value for the option.|
|index |Number |No|The index position to place the new option in. If not provided, the option will be added to the end.|

### Related topics

[clearOptions](clearOptions.md)

[removeOption](removeOption.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]