---
title: "addOption (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 9798f168-7b94-411d-9aed-6471042ff11a
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# addOption (Client API reference)



Adds an option to a control. 

## Control types supported

OptionSet, MultiSelectOptionSet

## Syntax

`formContext.getControl(arg).addOption(option, index);`

## Parameters

|Name | Type | Required | Description|
|--|--|--|--|
|option |Object |Yes|The option to add. The object contains the following attributes:<br/>**- text**: String. The label for the option.<br/>**- value**: Number. The value for the option.|
|index |Number |No|The index position to place the new option in. If not provided, the option will be added to the end.|

### Related topics

[clearOptions](clearOptions.md)

[removeOption](removeOption.md)