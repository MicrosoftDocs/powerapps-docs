---
title: "save (Client API reference) in model-driven apps| MicrosoftDocs"
description: Saves the record asynchronously with the option to close the form or open a new form after the save is completed.
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: a27f8267-9b24-42b7-a075-420a26db6693
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# save (Client API reference)

[!INCLUDE[./includes/save-description.md](./includes/save-description.md)]

## Syntax

`formContext.data.entity.save(saveOption);`

> [!NOTE]
> This method is deprecated and we recommend to use the [formContext.data.save](../formContext-data/save.md) method.

## Parameters

|Name|Type|Required|Description|
|--|--|--|--|
|saveOption|String|No|Specify options for saving the record. If no parameter is included in the method, the record will simply be saved. This is the equivalent of using the **Save** command.<br/>You can specify one of the following values:<br/><br/>- **saveandclose**: This is the equivalent of using the **Save and Close** command.<br/><br/>- **saveandnew**: This is the equivalent of the using the **Save and New** command.|

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Example

To open a new form after the save is completed:

`formContext.data.entity.save("saveandnew");`

### Related topics

[formContext.data.save](../formContext-data/save.md)

[formContext](../../clientapi-form-context.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]