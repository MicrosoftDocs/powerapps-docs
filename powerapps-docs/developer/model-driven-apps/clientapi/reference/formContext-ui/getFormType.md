---
title: "getFormType (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getFormType method.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# getFormType (Client API reference)



[!INCLUDE[./includes/getFormType-description.md](./includes/getFormType-description.md)]

## Syntax

`formContext.ui.getFormType();`

## Return Value

**Type**: Number

**Description**: Form type. Returns one of the following values 

|Value |Form type |
|---|---|
|0|Undefined|
|1|Create|
|2|Update|
|3|Read Only|
|4|Disabled|
|6|Bulk Edit|

>[!NOTE]
>Quick Create forms return 1.


### Related topics

[formContext.ui](../formContext-ui.md)

[formContext](../../clientapi-form-context.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]