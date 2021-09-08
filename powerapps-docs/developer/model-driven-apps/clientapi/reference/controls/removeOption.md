---
title: "removeOption (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the removeOption method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 09fd288c-d687-4976-b708-29a466fc35b1
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# removeOption (Client API reference)

Removes an option from a control. 

## Control types supported

choice, choices

## Syntax

`formContext.getControl(arg).removeOption(value);`

## Parameters

|Name | Type | Required | Description|
|--|--|--|--|
|value |Number |Yes|The value of the option you want to remove.|

### Related topics

[addOption](addOption.md)

[clearOptions](clearOptions.md)

 




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]