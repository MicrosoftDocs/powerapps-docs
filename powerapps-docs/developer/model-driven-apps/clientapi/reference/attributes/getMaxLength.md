---
title: "getMaxLength (Client API reference)| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 67a96fc4-4d65-4858-90da-f41eeba0365a
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getMaxLength (Client API reference)



Returns a number indicating the maximum length of a string or memo attribute. 

## Attribute types supported

string, memo

## Syntax

`formContext.getAttribute(arg).getMaxLength()`

## Return Value

**Type**: Number. 

**Description**: The maximum allowed length of a string for this attribute.

> [!NOTE]
> The email form description attribute is a memo attribute, but it does not have a `getMaxLength` method.