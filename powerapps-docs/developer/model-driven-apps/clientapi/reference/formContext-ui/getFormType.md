---
title: "getFormType (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 6c57db71-a76d-404c-852e-9c36a1c549ee
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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

